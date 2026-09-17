# Migrazione a Neo4j con retrieval ibrido a tre indici (Lucene + Range + HNSW) e reranking WRRF

Contesto: ADR-0002 aveva scelto SQLite dietro un'interfaccia a grafo astratta, esplicitamente per restare leggeri a scala di pilota, ma pensata per essere sostituibile "senza riscrivere il codice applicativo" quando la scala lo avesse richiesto. Il censimento oggi è piccolo (112 nodi), ma la fonte esterna `wiki/3. concepts/Hybrid Retrieval (Multi-Index).md` (nota di dominio su architetture di retrieval legale) descrive il pattern a tre indici paralleli — full-text Lucene, range temporale, vector HNSW — con reranking pesato, nativo su Neo4j 5.x.

## Decisione

L'utente ha deciso esplicitamente di anticipare la migrazione **prima** che la crescita del censimento la renda necessaria, non dopo: la crescita attesa è esponenziale una volta che il sistema è in uso reale (più fonti normative, più giurisdizioni, più versioni temporali), e la migrazione costa meno ora (112 nodi, poche query da riscrivere) che a corpus grande con più consumatori del dato. Questo non contraddice ADR-0002, ne esegue il piano: "quella migrazione diventa cambiare l'implementazione dietro l'interfaccia", non un cambio di principio architetturale.

Sostituito: storage SQLite → **Neo4j 5.x**. La tabella `relazioni` polimorfica (ADR-0004/0005) diventa archi tipizzati nativi (`evidence_type`/`confidence` come proprietà d'arco, invariati); `obblighi`/`principi` diventano nodi con le stesse colonne come proprietà.

## Chiarimento: SAT-Graph, Neo4j e Hybrid Retrieval sono tre cose distinte

La fonte esterna (`wiki/3. concepts/`) descrive tre concetti separati, facilmente confondibili perché co-occorrono negli stessi esempi:

- **SAT-Graph** (`SAT-Graph.md`): pattern di *modellazione dati*, ontologia a 4 livelli Work → Temporal Version → Language Version → Text Unit. Agnostico dal motore di storage (la nota stessa elenca Neo4j, Oracle 23ai, Postgres+pgvector come alternative equivalenti). **Non adottato da questo censimento**: il modello Obbligo/Principio/Fonte/relazioni non è il modello Work/TV/LV/TU — sono ontologie diverse, fuori scope per questo ADR. Nessuna migrazione a SAT-Graph è stata decisa.
- **Hybrid Retrieval (Multi-Index)** (`Hybrid Retrieval (Multi-Index).md`): pattern di *retrieval*, tre indici + fusione pesata. Anche questo agnostico dal motore — realizzabile su qualunque storage con un indice lessicale, un filtro range e un indice vettoriale (es. SQLite FTS5 + WHERE + qmd, oppure Neo4j Lucene + range index + HNSW).
- **Neo4j**: motore di storage concreto scelto per implementare l'Hybrid Retrieval qui. Non è un requisito del pattern, è una scelta di implementazione — motivata sotto, non dedotta dalla nota.

Perché Neo4j specificamente (e non hybrid retrieval su SQLite, opzione più leggera valutata e scartata): l'utente ha scelto di anticipare la migrazione allo storage che regge la crescita attesa, invece di implementare l'hybrid retrieval due volte (una versione leggera su SQLite ora, poi una riscrittura su graph DB quando la scala lo richiede). Traversal multi-hop nativo O(1)/O(log n) e vector index nativo sono capacità che SQLite non offre senza estensioni aggiuntive (sqlite-vec, FTS5 già coperto) — Neo4j le dà entrambe nello stesso motore già scelto per il retrieval ibrido, invece di sommare estensioni SQLite più una futura migrazione separata.

## Architettura a tre indici

1. **Full-text Lucene** — su `testo`, `riferimento`, `testo_integrale`. Sostituisce lo scan Python case-insensitive attuale (`web_ui.py`, `/api/obblighi`, `/api/principi`) con ranking BM25 reale invece di binario include/exclude.
2. **Range index** — su `data_inizio_vigore`/`data_fine_vigore` (colonne già esistenti in `schema.sql`, oggi mostrate in UI ma **mai usate come filtro di ricerca** — gap preesistente che questa migrazione chiude). Aggiunge anche un range/categorical su `jurisdiction` quando il censimento coprirà più giurisdizioni oltre IT/EU.
3. **Vector HNSW** — embedding di `testo`/`testo_integrale`. Sorgente dell'embedding: resta il modello locale già in uso via `qmd` (nessuna API key esterna, coerente con ADR-0003 — quel vincolo riguarda l'estrazione LLM delle bozze, non il calcolo di embedding), ma i vettori vengono scritti nell'indice HNSW nativo di Neo4j invece che nel file-store di `qmd`: elimina il doppio giro export-markdown → re-indicizzazione `qmd` (`export_qmd.py` + `qmd_search.sync_qmd`) in favore di scrittura diretta nodo→proprietà vettoriale. Il meccanismo esatto (chiamata diretta al modello di embedding locale usato da `qmd`, o wrapper che estrae i vettori da `qmd` prima di scriverli su Neo4j) è dettaglio di implementazione, non bloccante per questa decisione.

## Range come pre-filtro, non come termine pesato — deviazione esplicita dalla nota di dominio

La nota propone di includere il range index come terzo termine nella somma pesata WRRF (`0.2 * 1/range_rank`). Non adottato: un obbligo/principio non più in vigore alla data di riferimento **non deve mai comparire** in risultato, indipendentemente da quanto sia lessicalmente o semanticamente rilevante — trattarlo come termine pesato permetterebbe a un articolo scaduto ma molto pertinente di superare in ranking uno valido ma meno pertinente. Il range resta quindi un `WHERE` applicato **prima** del retrieval (come già nell'esempio Cypher della nota stessa, sezione "Query Example"), non un fattore nella formula di fusione. Stesso trattamento per i filtri faceted già esistenti (`fonte_id`, `tipo_obbligo`, `stato_obbligo`, `categoria_soggetto`, `stato_validazione`): pre-filtro, non segnale di ranking.

## Pesi WRRF: lessicale vs semantico

Fusione a due termini (non tre, per la ragione sopra):

```
score = 0.55 * (1 / lucene_rank) + 0.45 * (1 / vector_rank)
```

**Perché 0.55/0.45 e non 0.5/0.5 o i pesi della nota (0.3/0.5 normalizzati):** il corpus è citazioni normative dense — query tipiche sono riferimenti puntuali ("Art. 35", "art. 24 §2(fb)") dove il match lessicale esatto è il segnale primario e un mismatch semantico rischia di far scomparire il risultato giusto dietro paraphrase plausibili ma sbagliate (stesso rischio di ambiguità-di-versione che la nota segnala per il vector puro). Si parte quindi leggermente sbilanciati verso il lessicale invece che alla pari.

**Provvisorietà esplicita:** questi pesi sono una stima ragionata, non tarata su dati — non esiste ancora un query log reale né un eval set con giudizi di rilevanza. Da rivedere non appena si accumula un numero sufficiente di query reali in produzione (soglia indicativa: 50+ query loggate) confrontando risultati con i pesi di default 0.5/0.5 come baseline.

## Multi-hop traversal pesato

`_vicini_di` (oggi 1-hop, non pesato) viene sostituito da traversal Cypher nativo multi-hop, con ranking per: distanza (hop count) + direttezza del tipo di relazione. Ordine di direttezza (dal più diretto al meno diretto, coerente con ADR-0005): `sostituisce`/`abroga` > `modifica`/`specifica` > `si applica a`/`attua`/`sanziona` > `richiama`/`si sovrappone a` > `richiede come precondizione`/`è condizionato da`. Non ancora tradotto in pesi numerici: da fare in fase di implementazione, quando il traversal multi-hop viene effettivamente scritto.

## Non fatto in questo cambiamento

Questo ADR fissa la decisione e l'architettura target, non esegue la migrazione: non c'è ancora uno script di migrazione dati SQLite→Neo4j, non c'è ancora un'istanza Neo4j provisionata, `web_ui.py` continua a girare su SQLite finché l'implementazione non è fatta. Vedi `CLAUDE.md` per lo stato corrente (ancora SQLite) finché questa migrazione non è eseguita.
