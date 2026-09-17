# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Progetto

Censimento strutturato degli obblighi normativi applicabili ai servizi fiduciari qualificati (QTSP): eIDAS/eIDAS2, CAD, DPCM 22/2/2013. Progetto separato da `RAG-QTSP/sgsi-rag` (RAG documentale generico su SGSI/ISO27001, punta sulla base documentale SharePoint aziendale per individuare gap di conformità rispetto a un framework come ISO 27001), affiancato ad esso ma indipendente: `codice-capobianco` non fa gap analysis e non legge SharePoint, è un censimento normativo strutturato a grafo (obblighi/principi con relazioni tipizzate esplicite), non un motore di ricerca documentale generico.

## Comandi

Tutto vive sotto `app/`, con un venv locale già creato in `app/.venv` (Python 3.14; dipendenze: fastapi, uvicorn, pydantic, neo4j, sentence-transformers — nessun `requirements.txt`/`pyproject.toml`, installate direttamente nel venv).

Storage: **Neo4j** (Neo4j Desktop, istanza locale `codice-capobianco`, Bolt su `bolt://127.0.0.1:7687`). Credenziali in `app/.env` (copiare da `app/.env.example`, mai committare `.env`). Avviare l'istanza da Neo4j Desktop prima di eseguire uno qualsiasi dei comandi sotto.

Applicare/aggiornare schema, indici e vincoli (idempotente, `CREATE ... IF NOT EXISTS`):
```bash
app/.venv/bin/python -c "
from pathlib import Path
import sys; sys.path.insert(0, 'app')
from neo4j_common import get_driver, get_database, SCHEMA_CYPHER_PATH
stmts = [s.strip() for s in SCHEMA_CYPHER_PATH.read_text().split(';') if s.strip() and not s.strip().startswith('//')]
d = get_driver()
with d.session(database=get_database()) as s:
    for stmt in stmts: s.run(stmt)
d.close()
"
```
(schema Cypher in `app/neo4j_schema.cypher`).

Ripopolare Neo4j da zero con i dati di estrazione (droppa e ricrea nodi/archi + monitoraggio.db + embedding, scrive direttamente su Neo4j senza passare da un file SQLite intermedio):
```bash
app/.venv/bin/python app/seed.py
```

In alternativa, se si riparte dal backup storico `app/censimento.db` invece che dai dati letterali in `seed.py` (due comandi separati, la migrazione strutturale non calcola gli embedding):
```bash
app/.venv/bin/python app/migrate_to_neo4j.py   # SQLite (censimento.db) -> Neo4j, con verifica conteggi
app/.venv/bin/python app/embed_neo4j.py        # (ri)calcola gli embedding per la ricerca semantica
```

Avviare la web UI (default `http://127.0.0.1:8010`, opzioni `--host`/`--port`):
```bash
app/.venv/bin/python app/web_ui.py
```

Non esistono test automatizzati né linter configurati nel repo.

## Architettura

### Il censimento è un knowledge graph, non una tabella piatta

Due tipi di nodo — **Obbligo** (prescrizione che impone un comportamento a un soggetto) e **Principio** (norma dichiarativa che stabilisce un effetto giuridico/presunzione/non discriminazione senza soggetto obbligato, es. art. 25 eIDAS) — collegati da **relazioni tipizzate** esplicitamente navigabili: sostituisce/è sostituito da, specifica/è specificato da, si sovrappone a/duplica, richiede come precondizione, è condizionato da/condiziona, 7 tipi aggiunti in ADR-0005 (attua, richiama, si applica a, modifica, abroga, definisce, sanziona), più 2 tipi aggiunti in ADR-0008 (deroga a/è derogato da, recepisce/è recepito da) — 14 tipi totali (vedi CONTEXT.md per l'elenco completo con descrizione). Decisione deliberata fin dal pilota: vedi `docs/adr/0001-censimento-come-knowledge-graph.md` e `docs/adr/0004-principio-come-secondo-tipo-di-nodo.md`. `CONTEXT.md` …

### Neo4j + hybrid retrieval (ADR-0006, migrazione eseguita)

Storage: **Neo4j 5.x** (Neo4j Desktop, istanza locale), non più SQLite. Migrazione eseguita secondo `docs/plan-migrazione-neo4j.md`: schema Cypher in `app/neo4j_schema.cypher`, script di migrazione strutturale una tantum in `app/migrate_to_neo4j.py` (riusato anche da `seed.py` tramite `migrate_from_connection`), pipeline di embedding in `app/embed_neo4j.py` (modello locale `paraphrase-multilingual-mpnet-base-v2`, 768 dimensioni, nessuna API key esterna). `app/censimento.db` resta come backup storico/fonte di export una tantum, non è più letto da `web_ui.py`.

Mappatura schema -> grafo: `:Obbligo`/`:Principio` come nodi con le colonne di `schema.sql` come proprietà (incluse `tipo_obbligo`/`tipo_principio`/`stato_obbligo`, ex-lookup-table, ora stringhe dirette sul nodo — niente join per valori enumerativi senza attributi propri); `:Fonte` con arco `DA_FONTE`; `:CategoriaSoggetto`/`:OggettoGiuridico` come nodi con archi `HA_SOGGETTO {ruolo}`/`HA_OGGETTO`. Le 14 relazioni tipizzate (ADR-0004/0005/0008) sono archi Cypher nativi con proprietà `relazione_id`/`evidence_type`/`confidence`/`tipo_relazione` (mappatura nome->tipo arco in `neo4j_common.TIPO_RELAZIONE_TO_ARCO`); la relazione inversa (`nome_inverso`) si ottiene via traversal a ritroso in `_vicini_di`, non è duplicata come arco separato. `modifiche_rilevate` (monitor…

Retrieval ibrido a tre indici paralleli (ADR-0006): full-text Lucene (`idxTestoObbligo`/`idxTestoPrincipio`, sostituisce lo scan Python case-insensitive pre-migrazione), range temporale su `data_inizio_vigore`/`data_fine_vigore` (pre-filtro `WHERE`, mai termine pesato — un nodo non vigente non deve mai comparire indipendentemente dalla rilevanza), vector HNSW (`idxEmbeddingObbligo`/`idxEmbeddingPrincipio`, 768 dim, cosine). Reranking a fusione pesata (WRRF) tra lessicale e semantico, pesi 0.55/0.45 (costanti `PESO_LESSICALE`/`PESO_SEMANTICO` in `web_ui.py`, provvisori — vedi ADR-0006 per il piano di revisione). `_vicini_di` è un traversal Cypher nativo multi-hop (parametro `profondita`, default 1): ranking per hop crescente poi per direttezza del tipo di relazione decrescente (`neo4j_common.DIRETTEZZA_PESO`).

### Estrazione LLM solo dentro sessioni Claude Code

Le bozze di Obbligo/Principio sono generate da LLM solo dentro sessioni Claude Code interattive (mai come chiamata batch autonoma né con una API key propria verso un servizio LLM) — vedi `docs/adr/0003-estrazione-solo-dentro-sessioni-claude-code.md`. La web UI (`web_ui.py`) è puramente di lettura/scrittura sul DB: consultazione, coda di revisione, nessuna chiamata LLM propria.

Ogni riga estratta nasce con `stato_validazione='bozza'` e richiede validazione umana esplicita (coda di revisione in UI) prima di essere considerata autorevole; i campi `validato_da`/`data_validazione` tracciano chi/quando.

### `web_ui.py`: backend FastAPI + SPA inline, un solo file

`app/web_ui.py` è insieme il backend FastAPI e il frontend: l'HTML/CSS/JS della SPA è una stringa Python inline (`INDEX_HTML`), niente build step né framework (React/Vue) — solo DOM manipulation e `fetch`. Tutte le API REST e l'intera UI vivono in questo unico file.

### Ricerca: faceted full-text su `/api/obblighi`/`/api/principi`, ibrida WRRF su `/api/ricerca`

`GET /api/obblighi`/`GET /api/principi` restano il listato faceted (filtri fonte/tipo/stato/categoria + `q` opzionale): il match testuale su `q` usa l'indice full-text Lucene (query a frase con boost sul campo `riferimento`, `_query_lucene` in `web_ui.py`) invece dello scan Python case-insensitive pre-migrazione, ma il filtraggio per facet resta in Python sull'intero risultato (dataset piccolo, nessuna necessità di spingere i filtri in Cypher).

`GET /api/ricerca` (Fase 6, ADR-0006) è l'endpoint di ricerca per rilevanza: pre-filtra per facet + range temporale (`data_riferimento`, mai un termine pesato — un nodo non vigente non deve mai comparire), poi fonde con WRRF il ranking full-text Lucene e il ranking vettoriale (embedding calcolato al volo con lo stesso modello di `embed_neo4j.py`, caricato pigramente al primo uso — `_embedding_model()` in `web_ui.py`). Pannello "Ricerca ibrida" nel frontend.

### Testo integrale in UI: presente in DB, ora anche in dettaglio

Sia `obblighi` che `principi` hanno un campo `testo_integrale` (testo normativo pieno, distinto dalla sintesi in `testo`) che prima era scritto nel DB ma **mai esposto** dalla UI (né dalle API né dal frontend). La detail view di obbligo/principio ora lo mostra in un blocco `<details>` collassabile "Testo normativo integrale" (fallback "non disponibile" se `NULL`). Attenzione quando si ragiona su un obbligo/principio: la sintesi in `testo` è una bozza-LLM compressa e può omettere condizioni/eccezioni presenti solo in `testo_integrale` — per interpretazione normativa affidabile, verificare sempre `testo_integrale` quando disponibile, non fermarsi alla sintesi.

### Provenienza per-arco: `evidence_type`/`confidence` sulle relazioni

Ogni riga di `relazioni` porta `evidence_type` (`textual`/`inferred`/`human-curated`, default `inferred`) e `confidence` (REAL 0–1, nullable) — stessa semantica di provenienza di `stato_validazione` sui nodi, ma per arco anziché per nodo. Introdotti in ADR-0005 insieme ai 7 nuovi tipi di relazione, esposti da `_vicini_di` in `web_ui.py` e mostrati come badge nel pannello "Relazioni tipizzate (grafo)" del frontend. `confidence` resta `NULL` finché non esiste un'estrazione LLM che produce davvero uno score — non va inventato. Vedi `docs/adr/0005-tassonomia-estesa-relazioni-e-provenienza.md` per il ragionamento completo (incluse le alternative scartate: relazioni gerarchiche pure, `valid_from`/`valid_to`, `source_span`).

### Storico "ticket" nei commenti

`schema.sql` e `seed.py` referenziano numeri di "ticket" sequenziali (03, 04, 05, 07, 08) come origine di varie decisioni di design (es. `modifiche_rilevate` da ticket 05, nodo Principio da ticket 08/ADR-0004). Un file `map.md` è citato nei commenti come riferimento per la cronologia di queste decisioni ma non è presente nell'albero del repo (potrebbe esistere solo nella storia git).

### Inconsistenza nota: eIDAS/eIDAS2 come due Fonti

`CONTEXT.md` dichiara che una Fonte esiste una volta sola nel censimento, ma `seed.py` modella eIDAS 910/2014 ed eIDAS2 (2024/1183) come **due righe `fonti` separate** (scelta esplicita per permettere confronto prima/dopo), segnalata in un commento di `seed.py` come divergenza da riconciliare con l'utente, non ancora risolta.

### Copertura completa per articolo (ADR-0007): nessun discrimine di rilevanza in estrazione

Il DB attuale (dati letterali in `seed.py`) **non** copre tutti gli articoli delle 4 Fonti: `seed.py` estraeva storicamente solo le disposizioni che impongono un obbligo a un soggetto censito o che dichiarano un effetto giuridico in senso stretto, escludendo esplicitamente le disposizioni di scopo/ambito/definizioni (es. art. 1 eIDAS, "Oggetto" — cercarlo nel censimento oggi non lo trova). Con ADR-0007 questo criterio è superato per le estrazioni **future**: ogni articolo/comma di una Fonte importata deve avere esattamente un nodo (Obbligo o Principio), con due nuovi valori di `tipo_principio` — "scopo/ambito di applicazione", "definitorio" — per le disposizioni di cornice prive di soggetto obbligato e di effetto giuridico specifico. Non è una retroestrazione automatica: il backfill degli articoli oggi mancanti nelle 4 Fonti già censite è un lavoro a parte, già speced in `docs/superpowers/specs/2026-09-11-censimento-granulare-design.md` e pianificato in `docs/superpowers/plans/2026-09-11-censimento-granulare.md`, non ancora eseguito (nessun `app/seed_data/` nel repo a oggi).

### Import granulare eIDAS (2026-09-15): costato due finestre di 5 ore, causa e rimedio strutturale

L'import granulare eIDAS/eIDAS2 (ADR-0007, 460 righe nuove via 7 subagent
paralleli per capitolo) ha esaurito due volte la finestra di 5 ore del piano
Pro. Cause identificate: (1) testo ufficiale incollato inline in ogni
prompt subagent invece che passato per riferimento — duplicazione del
contesto normativo ×7; (2) due subagent hanno scritto sullo stesso file di
output per assenza di un'assegnazione di path esplicita e precedente al
dispatch; (3) id interi assegnati a mano con range concordati a priori tra
fonti (`seed.py`: "eIDAS/eIDAS2: id 1-100, CAD/DPCM: id 101-135") —
fragile con autoria parallela; (4) debug infrastrutturale (driver `neo4j`
incompatibile, venv sotto iCloud, Neo4j Desktop non responsivo) condotto
dentro la stessa sessione di estrazione anziché isolato.

Rimedio strutturale per le prossime fonti (CAD, poi DPCM), non ancora
applicato retroattivamente a eIDAS/eIDAS2 (restano inline in `seed.py` con
la numerazione manuale esistente): `app/seed_data/lib.py` fornisce
`verifica_copertura`/`costruisci_lookup`/`inserisci_capitoli`, che
risolvono gli id per riferimento simbolico tramite un registro
`(tipo, fonte_id, riferimento) -> id` invece di interi assegnati a mano;
`app/tools/split_source.py` divide il testo ufficiale in porzioni per
capitolo con path di output assegnati centralmente prima del dispatch dei
subagent (elimina la classe di bug "collisione di path"). Guardia
automatica contro la regressione nota del driver `neo4j` in
`neo4j_common.get_driver()` (`VERSIONE_DRIVER_ATTESA`). Procedura completa
in `docs/procedura-import-granulare.md`, problemi infrastrutturali noti in
`docs/runbook-neo4j-import.md`.

### Deroga/recepisce (ADR-0008) e collegamento cross-fonte a posteriori (ADR-0009)

ADR-0008 (17/09) ha portato la tassonomia da 12 a 14 tipi di relazione: `deroga a`/`è derogato da` (eccezione puntuale a un nodo che resta vigente fuori dai casi derogati — diverso da `modifica`/`abroga`) e `recepisce`/`è recepito da` (un nodo incorpora formalmente il contenuto di un altro in un contesto normativo diverso, non limitato al caso direttiva UE → recepimento nazionale). Nessuna istanza seedata da questa ADR: popolamento demandato a estrazione LLM interattiva quando emerga riscontro testuale reale.

ADR-0009 (16/09) risponde al fatto che l'import granulare per capitolo (subagent paralleli, vedi sotto) produce sottografi isolati per fonte — i subagent erano istruiti a non tentare relazioni cross-fonte durante l'import per evitare errori di merge parallelo. Pipeline a 3 stadi per collegare fonti già presenti nel grafo, pensata per essere riusabile su qualunque coppia: (1) generazione candidati **a zero token LLM** — grep testuale sul testo ufficiale grezzo per citazioni esplicite + KNN sull'indice vettoriale HNSW già popolato, soglia di score configurabile; (2) classificazione LLM **solo sullo shortlist** risultante, via chiamate `completion()` dirette in batch eseguite in parallelo con `wait()` (non subagent — l'overhead di dispatch supera il beneficio su shortlist già piccoli), output vincolato a schema JSON, prompt esplicitamente conservativo; (3) validazione (soglia `confidence`, verifica che ogni `riferimento` proposto esista davvero in Neo4j) e inserimento come "capitolo virtuale" con solo `RELAZIONI` valorizzato, stesso meccanismo di `app/seed_data/lib.py`. Applicata a CAD↔eIDAS/eIDAS2 (53 relazioni inserite); DPCM↔eIDAS/eIDAS2 resta fuori scope finché non richiesto esplicitamente.

### Stato copertura per fonte (aggiornato 2026-09-17)

eIDAS/eIDAS2 e CAD importati con copertura granulare completa per articolo (ADR-0007) e collegati tra loro (ADR-0009). DPCM 22/2/2013 ancora da importare con lo stesso criterio granulare — oggi presente nel censimento solo nella forma storica pre-ADR-0007 (solo disposizioni con soggetto obbligato/effetto giuridico esplicito). Procedura di riferimento per il prossimo import: `docs/procedura-import-granulare.md`; problemi infrastrutturali noti: `docs/runbook-neo4j-import.md`.
