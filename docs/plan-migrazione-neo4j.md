# Piano di esecuzione: migrazione a Neo4j + hybrid retrieval

Questo documento è il piano operativo per eseguire la decisione presa in `docs/adr/0006-migrazione-neo4j-hybrid-retrieval.md`. Scritto per essere eseguito da una sessione Claude Code senza contesto pregresso: leggere prima `CLAUDE.md` (stato progetto), poi `docs/adr/0006-migrazione-neo4j-hybrid-retrieval.md` (decisione e architettura target), poi questo file (come farlo).

Non eseguire le fasi fuori ordine: ognuna assume che la precedente sia stata completata e verificata (criteri di accettazione in fondo a ciascuna).

---

## Fase 0 — Decisioni da confermare con l'utente prima di scrivere codice

Non bloccanti per iniziare il lavoro di provisioning (Fase 1), ma bloccanti prima della Fase 4 (embedding) e Fase 5 (cutover):

1. **Modello di embedding.** Proposta: un modello locale multilingue via `sentence-transformers` (es. `paraphrase-multilingual-mpnet-base-v2`, 768 dimensioni — stessa dimensionalità già usata come esempio in ADR-0006/schema Neo4j) invocato direttamente in Python durante l'indicizzazione, **non** più tramite `qmd` come CLI esterna. Motivo: `qmd` è file-based e pensato per un flusso export→reindex separato (ADR pre-0006); calcolare l'embedding direttamente nello script di indicizzazione Neo4j elimina un giro di serializzazione e la dipendenza da un binario esterno con path non garantito (`qmd_search._qmd_bin()` oggi ha già un fallback hardcoded perché non è sempre su PATH). Nessuna API key esterna, coerente con ADR-0003. **Da confermare:** nome esatto del modello (il testo è in italiano — verificare che il modello scelto abbia training multilingue adeguato, non solo inglese).
2. **Deployment Neo4j.** Proposta: Docker (`neo4j:5-community`), locale, porte 7474 (HTTP browser)/7687 (Bolt), volume dati persistito in `app/neo4j_data/` (gitignored). Nessun servizio cloud. **Da confermare:** Docker è installato/disponibile sulla macchina target: verificare con `docker --version` prima della Fase 1; se assente, alternativa è Neo4j Desktop (stessa configurazione Bolt, gestione manuale invece che via compose).
3. **Cutover vs periodo di doppio storage.** Proposta: cutover netto, non doppio storage temporaneo — `censimento.db` resta come **fonte di export una tantum** per la migrazione dati (Fase 3), poi `web_ui.py` legge/scrive solo su Neo4j. Coerente con la regola del repo "clean cutover, no shim". `censimento.db` non viene cancellato (resta come backup/riferimento storico), ma smette di essere la fonte live.

Se l'utente non è raggiungibile per confermare, procedere con le proposte di default sopra e segnalarlo esplicitamente nel riepilogo finale della sessione.

---

## Fase 1 — Provisioning Neo4j locale

**File:** nuovo `docker-compose.yml` (root repo o `app/`), nuovo `.env`/`.env.example` per credenziali (mai hardcoded in `web_ui.py`).

- `docker compose up -d` con immagine `neo4j:5-community`, plugin APOC non necessario per questo scope (Lucene full-text, range index e vector index sono tutti nativi in Neo4j 5.x, nessun plugin richiesto).
- Credenziali via variabile d'ambiente (`NEO4J_AUTH=neo4j/<password locale>`), lette da `web_ui.py` via `os environ`, mai committate.
- Aggiungere `neo4j` (driver Python ufficiale) al venv: `app/.venv/bin/pip install neo4j`. Il repo non ha `requirements.txt`: verificare se questa migrazione è l'occasione per introdurne uno (decisione minore, segnalare ma non bloccante).

**Accettazione:** `docker compose ps` mostra il container up; una query Cypher minima (`RETURN 1`) eseguita dal driver Python ritorna risultato, confermando connettività Bolt.

---

## Fase 2 — Schema Neo4j: nodi, archi, indici

**File:** nuovo `app/neo4j_schema.cypher` (equivalente concettuale di `schema.sql`, non generato da ORM).

Mappatura da `schema.sql` (leggere prima le tabelle `obblighi`, `principi`, `fonti`, `relazioni`, `obbligo_soggetti`, `principio_oggetti`, `tipi_relazione`, `tipi_obbligo`, `tipi_principio`, `stati_norma`, `stati_fonte`, `categorie_soggetto`, `oggetti_giuridici`):

- Nodi `:Obbligo` e `:Principio` — stesse colonne di `obblighi`/`principi` come proprietà (incluso `stato_validazione`, `validato_da`, `data_validazione`, `data_inizio_vigore`, `data_fine_vigore`, `testo`, `testo_integrale`, `riferimento`).
- Nodo `:Fonte` — da tabella `fonti`; arco `(:Obbligo|:Principio)-[:DA_FONTE]->(:Fonte)`.
- Archi tipizzati per le relazioni (ADR-0004/0005): un arco Neo4j per riga `relazioni`, tipo dell'arco = valore di `tipi_relazione.nome` (12 tipi totali, vedi `CONTEXT.md`), proprietà `evidence_type`/`confidence` invariate. La direzione dell'arco Neo4j riflette `nodo_da`→`nodo_a`; la relazione inversa (`nome_inverso`) si ottiene via traversal a ritroso, non va duplicata come arco separato.
- Nodo `:CategoriaSoggetto` + archi `(:Obbligo)-[:HA_SOGGETTO {ruolo: 'obbligato'|'destinatario'}]->(:CategoriaSoggetto)` al posto di `obbligo_soggetti`.
- Nodo `:OggettoGiuridico` + archi `(:Principio)-[:HA_OGGETTO]->(:OggettoGiuridico)` al posto di `principio_oggetti`.
- Tabelle di lookup puramente enumerative senza altri attributi (`tipi_obbligo`, `tipi_principio`, `stati_norma`, `stati_fonte`) diventano proprietà stringa dirette sui nodi (es. `Obbligo.tipo_obbligo = "obbligo di sicurezza"`), non nodi separati — evita join inutili per valori che non hanno mai attributi propri oltre al nome.
- `modifiche_rilevate` (monitoraggio automatico) resta fuori scope di questa migrazione se non referenziata da altre entità del grafo: valutare se serve davvero il grafo o se può restare relazionale (anche in una piccola tabella SQLite separata, non tutto deve vivere in Neo4j) — decisione da prendere in questa fase, documentarla nel file cypher con un commento.

Indici (i tre pilastri di ADR-0006):

```cypher
CREATE FULLTEXT INDEX idxTestoObbligo FOR (n:Obbligo) ON EACH [n.testo, n.riferimento, n.testo_integrale];
CREATE FULLTEXT INDEX idxTestoPrincipio FOR (n:Principio) ON EACH [n.testo, n.riferimento, n.testo_integrale];
CREATE RANGE INDEX idxVigoreObbligo FOR (n:Obbligo) ON (n.data_inizio_vigore, n.data_fine_vigore);
CREATE RANGE INDEX idxVigorePrincipio FOR (n:Principio) ON (n.data_inizio_vigore, n.data_fine_vigore);
CREATE VECTOR INDEX idxEmbeddingObbligo FOR (n:Obbligo) ON (n.embedding)
  OPTIONS { indexConfig: { `vector.dimensions`: 768, `vector.similarity_function`: 'cosine' } };
CREATE VECTOR INDEX idxEmbeddingPrincipio FOR (n:Principio) ON (n.embedding)
  OPTIONS { indexConfig: { `vector.dimensions`: 768, `vector.similarity_function`: 'cosine' } };
```

(768 dimensioni assume la Decisione 1 di Fase 0 confermata; aggiornare se il modello scelto ha dimensionalità diversa.)

**Accettazione:** `SHOW INDEXES` in Neo4j Browser elenca i 6 indici come `ONLINE`.

---

## Fase 3 — Script di migrazione dati SQLite → Neo4j

**File:** nuovo `app/migrate_to_neo4j.py`, eseguibile standalone (`app/.venv/bin/python app/migrate_to_neo4j.py`), idempotente (droppa e ricrea i nodi/archi del censimento, stesso spirito di `seed.py` — "una tantum / per ripartire puliti").

- Legge da `censimento.db` con `sqlite3` (stesso pattern di lettura già in `web_ui.py::_conn`).
- Scrive nodi/archi via driver `neo4j`, in transazioni batch (non una query per riga — 112+ nodi sono pochi ma la pratica corretta vale anche qui, e vale sicuramente quando il censimento crescerà, che è la ragione stessa di questa migrazione).
- **Non** calcola gli embedding in questo script: quella è la Fase 4, separata, perché il calcolo embedding è la parte più lenta/con dipendenza da modello — separare le fasi rende ripetibile la sola migrazione strutturale senza ricalcolare vettori ogni volta.
- Verifica di integrità post-migrazione: conteggio nodi/archi in Neo4j deve combaciare con conteggio righe in SQLite (`obblighi`, `principi`, `relazioni`, `obbligo_soggetti`, `principio_oggetti`).

**Accettazione:** conteggi combacianti (script stampa un riepilogo `sqlite: N obblighi / neo4j: N Obbligo`, ecc., per ogni tabella/label); una query Cypher di traversal manuale su un caso noto (es. un obbligo con relazione `sostituisce`) ritorna lo stesso vicino che `_vicini_di` ritorna oggi su SQLite per lo stesso nodo — confronto diretto, non assunto.

---

## Fase 4 — Pipeline di embedding

**File:** nuovo `app/embed_neo4j.py` (o esteso dentro `migrate_to_neo4j.py` come step separato invocabile a parte).

- Per ogni nodo `:Obbligo`/`:Principio`, calcola embedding su `testo` (sintesi) — non su `testo_integrale` per intero se supera la finestra del modello: riusare la logica di chunking già scritta in `export_qmd.py::_dividi_testo_integrale` per capire dove il testo va spezzato, ma la scelta se indicizzare 1 vettore per nodo (sul solo `testo`, più corto e già pensato per essere una sintesi densa) o 1 vettore per chunk (come faceva `qmd` con `testo_integrale`) è una decisione di design da prendere qui, non assunta: 1 vettore per nodo è più semplice (un solo `Obbligo.embedding` per la vector index sopra) ma perde granularità sui nodi con `testo_integrale` lungo; N vettori per nodo richiederebbe nodi `:TextUnit` satellite (introduce un pezzo di SAT-Graph non deciso — vedi il chiarimento in ADR-0006 sul perché SAT-Graph non è stato adottato). **Raccomandazione: 1 vettore per nodo su `testo`**, coerente con "non adottare SAT-Graph"; se in seguito emerge perdita di recall sui nodi lunghi, riconsiderare.
- Scrive il vettore su `Obbligo.embedding`/`Principio.embedding` (property Neo4j, array di float).

**Accettazione:** una query `db.index.vector.queryNodes` su una query di prova ("requisiti per il responsabile della protezione dei dati" o equivalente italiano nel dominio QTSP) ritorna risultati semanticamente pertinenti (verifica manuale, non automatizzabile senza eval set).

---

## Fase 5 — Riscrittura del data-access layer in `web_ui.py`

Sostituire `sqlite3` con il driver `neo4j` in tutte le funzioni che oggi aprono `_conn()`. Elenco esaustivo delle funzioni/endpoint da riscrivere (verificato dal codice attuale, non stimato):

- `_conn`, `_lookup_maps`, `_tipi_principio_map`, `_soggetti_di`, `_oggetti_di_principio`, `_riga_obbligo`, `_riga_principio` → diventano query Cypher invece di `SELECT`.
- `_vicini_di` → Cypher traversal nativo (vedi Fase 7 per il multi-hop pesato: questa fase può prima fare solo il porting 1:1 dell'attuale comportamento 1-hop, poi Fase 7 lo estende).
- Endpoint di lettura: `GET /api/lookup`, `GET /api/stats`, `GET /api/obblighi`, `GET /api/obblighi/{id}`, `GET /api/principi`, `GET /api/principi/{id}`, `GET /api/revisione`.
- Endpoint di scrittura: `POST /api/revisione/{obbligo_id}/valida`, `POST /api/revisione/{obbligo_id}/rifiuta`, `POST /api/monitoraggio/{modifica_id}/esamina` — verificare se `modifiche_rilevate` resta su Neo4j o SQLite separato per la decisione presa in Fase 2.
- `GET /api/ricerca-semantica` e il modulo `qmd_search.py`/`export_qmd.py` — **da ritirare**, sostituiti dall'endpoint unificato di Fase 6. Non lasciare come shim/alias morto: rimuovere l'endpoint, il pannello "Ricerca per significato" nel frontend (`INDEX_HTML`), e i due file Python, coerente con la regola del repo "clean cutover, no dead code".

**Non toccare in questa fase:** la struttura della SPA inline (`INDEX_HTML`) al di là dei punti sopra — resta un solo file `web_ui.py`, nessun build step introdotto (decisione architetturale invariata, non in discussione qui).

**Accettazione:** avviare `web_ui.py`, verificare manualmente (o con uno script smoke throwaway) che ogni endpoint sopra risponda con dati equivalenti a quelli che restituiva su SQLite per le stesse richieste (stesso obbligo, stessi vicini, stesso conteggio in `/api/stats`).

---

## Fase 6 — Endpoint di ricerca unificato con fusione WRRF

**File:** `app/web_ui.py`, nuovo endpoint (sostituisce `GET /api/obblighi`+`GET /api/ricerca-semantica` come esperienza di ricerca, mantenendo `/api/obblighi`/`/api/principi` per i casi in cui il frontend vuole solo il listato faceted senza query testuale — decidere in questa fase se serve davvero una distinzione o se un solo endpoint con `q` opzionale basta, coerente con "non introdurre due percorsi paralleli per lo stesso scopo").

Implementazione, per query testuale non vuota:

1. Pre-filtro: facet (`fonte_id`, `tipo_obbligo`, `stato_obbligo`, `categoria_soggetto`, `stato_validazione`) + range temporale (`data_riferimento`, nuovo parametro — Cypher `WHERE` su `data_inizio_vigore`/`data_fine_vigore`, non un termine di ranking, per la ragione già in ADR-0006).
2. Due retrieval paralleli sull'insieme pre-filtrato: full-text Lucene (`db.index.fulltext.queryNodes`) e vector HNSW (`db.index.vector.queryNodes` sull'embedding della query, calcolato con lo stesso modello di Fase 4).
3. Fusione WRRF con i pesi decisi in ADR-0006 (`0.55 * 1/lucene_rank + 0.45 * 1/vector_rank`), pesi esposti come costante nominata (non magic number sparso), commentata con riferimento all'ADR.
4. `LIMIT` configurabile (default coerente con quello attuale di `ricerca_semantica`, `n=10`).

**Accettazione:** query di prova con termine lessicale esatto ("Art. 32") restituisce quell'articolo in prima posizione; query semantica pura ("obblighi per la protezione dei dati personali") restituisce risultati pertinenti anche senza match lessicale esatto; query con `data_riferimento` antecedente a `data_inizio_vigore` di un nodo lo esclude sempre, anche se lessicalmente/semanticamente in testa.

---

## Fase 7 — Multi-hop traversal pesato

Estende `_vicini_di` (già portato 1:1 in Fase 5) con:

- Traversal a più hop (parametro `profondita`, default 1 per non cambiare comportamento esistente salvo richiesta esplicita).
- Ranking per distanza + direttezza del tipo di relazione, ordine già fissato in ADR-0006 (`sostituisce`/`abroga` > `modifica`/`specifica` > `si applica a`/`attua`/`sanziona` > `richiama`/`si sovrappone a` > `richiede come precondizione`/`è condizionato da`). Tradurre l'ordine in pesi numerici concreti in questa fase (non prima — ADR-0006 lo lascia esplicitamente aperto).

**Accettazione:** su un nodo con relazioni di più tipi diversi, il traversal a 2 hop restituisce i vicini diretti prima degli indiretti, e a parità di hop i tipi più diretti prima di quelli meno diretti.

---

## Fase 8 — Pulizia

- Rimuovere `app/qmd_search.py`, `app/export_qmd.py`, directory `app/qmd_export/` (generata, verificare se già in `.gitignore`), voce collection `compliance-rag` da `~/.config/qmd/index.yml` (fuori dal repo, ma segnalarlo all'utente — non toccare config utente senza dirlo).
- Rimuovere `docs/qmd-semantic-search-spec.md` o marcarlo esplicitamente come storico/superato (non cancellare cronologia di decisione senza motivo — coerente con come questo stesso repo tratta gli ADR superati altrove: non si cancellano, si sovrascrivono con una nota).
- Aggiornare `CLAUDE.md`: sezione "SQLite dietro un'interfaccia a grafo" diventa sezione "Neo4j + hybrid retrieval" con lo stato **effettivo** post-migrazione (comandi per avviare Neo4j, dove sta lo schema Cypher, come rilanciare la migrazione/embedding), sezione "Ricerca: faceted + full-text, più ricerca semantica via qmd" va riscritta per descrivere l'endpoint unificato di Fase 6. Sezione "Comandi" aggiornata con `docker compose up -d`, comando di migrazione, comando di embedding.
- `censimento.db` e `app/seed.py`: decidere con l'utente se `seed.py` viene riscritto per scrivere direttamente su Neo4j (perdendo SQLite come step intermedio) o se resta il seed SQLite + `migrate_to_neo4j.py` come secondo passo sempre necessario per ripartire puliti — non assumere, chiedere.

**Accettazione:** nessun riferimento morto a `qmd` in `CLAUDE.md`/codice attivo; `git grep -i qmd` nel repo ritorna solo eventuali menzioni storiche negli ADR (che restano, sono cronologia di decisione, non codice).

---

## Ordine di esecuzione consigliato in una singola sessione

Fase 0 (decisioni, veloce) → Fase 1 → Fase 2 → Fase 3 → Fase 4 → Fase 5 → Fase 6 → Fase 7 → Fase 8. Ogni fase ha un criterio di accettazione verificabile: non passare alla successiva senza averlo controllato concretamente (eseguire la query, non assumere che "dovrebbe funzionare"). Se una fase rivela che una decisione di Fase 0 era sbagliata (es. dimensionalità embedding diversa da 768), tornare indietro e aggiornare Fase 2 prima di proseguire — non aggirare con un workaround locale.
