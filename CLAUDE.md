# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Progetto

Censimento strutturato degli obblighi normativi applicabili ai servizi fiduciari qualificati (QTSP): eIDAS/eIDAS2, CAD, DPCM 22/2/2013. Progetto separato da `RAG-QTSP/sgsi-rag` (RAG documentale generico su SGSI/ISO27001), affiancato ad esso ma indipendente.

## Comandi

Tutto vive sotto `app/`, con un venv locale già creato in `app/.venv` (Python 3.14; dipendenze: fastapi, uvicorn, pydantic — nessun `requirements.txt`/`pyproject.toml`, installate direttamente nel venv).

Ripopolare il DB da zero (droppa e ricrea `app/censimento.db` da `schema.sql` + dati seed):
```bash
app/.venv/bin/python app/seed.py
```

Avviare la web UI (default `http://127.0.0.1:8010`, opzioni `--host`/`--port`):
```bash
app/.venv/bin/python app/web_ui.py
```

Riesportare manualmente DB → markdown per qmd (di solito non serve, vedi sync automatico sotto):
```bash
app/.venv/bin/python app/export_qmd.py
```

Non esistono test automatizzati né linter configurati nel repo.

## Architettura

### Il censimento è un knowledge graph, non una tabella piatta

Due tipi di nodo — **Obbligo** (prescrizione che impone un comportamento a un soggetto) e **Principio** (norma dichiarativa che stabilisce un effetto giuridico/presunzione/non discriminazione senza soggetto obbligato, es. art. 25 eIDAS) — collegati da **relazioni tipizzate** esplicitamente navigabili (sostituisce/è sostituito da, specifica/è specificato da, si sovrappone a/duplica, richiede come precondizione, è condizionato da/condiziona). Decisione deliberata fin dal pilota: vedi `docs/adr/0001-censimento-come-knowledge-graph.md` e `docs/adr/0004-principio-come-secondo-tipo-di-nodo.md`. `CONTEXT.md` è il glossario di dominio canonico (Fonte, Obbligo, Principio, Categorie di soggetto, Relazioni) — leggerlo prima di modificare schema o logica di dominio.

### SQLite dietro un'interfaccia a grafo

Storage su SQLite (non un graph DB dedicato) per restare locale e senza dipendenze esterne alla scala del pilota, ma pensato per essere sostituibile in futuro con un graph DB dedicato senza riscrivere il codice applicativo — vedi `docs/adr/0002-sqlite-dietro-interfaccia-a-grafo.md`. Coerentemente, la tabella `relazioni` è **polimorfica**: `nodo_da_tipo`/`nodo_a_tipo` (`'obbligo'` o `'principio'`) + `nodo_da_id`/`nodo_a_id` come INTEGER **senza FK** sulle estremità — l'integrità referenziale degli archi è verificata solo a livello applicativo (in `web_ui.py`, `_vicini_di` scarta silenziosamente archi il cui nodo target non esiste più), non dal DB.

### Estrazione LLM solo dentro sessioni Claude Code

Le bozze di Obbligo/Principio sono generate da LLM solo dentro sessioni Claude Code interattive (mai come chiamata batch autonoma né con una API key propria verso un servizio LLM) — vedi `docs/adr/0003-estrazione-solo-dentro-sessioni-claude-code.md`. La web UI (`web_ui.py`) è puramente di lettura/scrittura sul DB: consultazione, coda di revisione, nessuna chiamata LLM propria.

Ogni riga estratta nasce con `stato_validazione='bozza'` e richiede validazione umana esplicita (coda di revisione in UI) prima di essere considerata autorevole; i campi `validato_da`/`data_validazione` tracciano chi/quando.

### `web_ui.py`: backend FastAPI + SPA inline, un solo file

`app/web_ui.py` è insieme il backend FastAPI e il frontend: l'HTML/CSS/JS della SPA è una stringa Python inline (`INDEX_HTML`), niente build step né framework (React/Vue) — solo DOM manipulation e `fetch`. Tutte le API REST e l'intera UI vivono in questo unico file.

### Ricerca: faceted + full-text, più ricerca semantica via qmd

La ricerca principale (`/api/obblighi`, `/api/principi`) filtra in Python su scansioni complete delle tabelle (non query SQL con WHERE). Il match testuale copre `testo` (sintesi), `riferimento` **e** `testo_integrale`.

Affiancata (non sostitutiva) a questa, esiste una ricerca semantica sperimentale via il tool CLI esterno `qmd` (modelli locali GGUF, nessuna API key esterna — coerente con ADR-0003, che vincola solo l'estrazione LLM delle bozze, non l'indicizzazione/query locale di qmd): vedi spec originale in `docs/qmd-semantic-search-spec.md` e implementazione in `app/export_qmd.py` + `app/qmd_search.py`, endpoint `GET /api/ricerca-semantica`, pannello "Ricerca per significato" nel frontend.

Decisioni prese (non rimetterle in discussione senza che l'utente lo chieda esplicitamente):
- Chiamata `qmd query` (con reranking, LLM locale) **sincrona/bloccante** dentro la richiesta HTTP — niente cache/precompute, latenza accettata (~8-55s a seconda della cache di qmd) in cambio di risultati migliori. Timeout lato server 120s.
- `qmd query`, non `qmd vsearch` — reranking preferito a velocità pura.
- Le bozze (`stato_validazione='bozza'`) **sono incluse** nell'export/ricerca semantica, non solo i record validati.
- Sync DB → export markdown → re-indicizzazione qmd è **automatico**, non richiede comando manuale: hook in `valida_bozza`/`rifiuta_bozza` (`qmd_search.sync_qmd()`) e all'avvio di `web_ui.py` (`main()`). Il comando manuale `app/export_qmd.py` resta disponibile come opzione fuori-banda (es. dopo `seed.py` a server già avviato, senza riavviarlo).

### Testo integrale in UI: presente in DB, ora anche in dettaglio

Sia `obblighi` che `principi` hanno un campo `testo_integrale` (testo normativo pieno, distinto dalla sintesi in `testo`) che prima era scritto nel DB ma **mai esposto** dalla UI (né dalle API né dal frontend). La detail view di obbligo/principio ora lo mostra in un blocco `<details>` collassabile "Testo normativo integrale" (fallback "non disponibile" se `NULL`). Attenzione quando si ragiona su un obbligo/principio: la sintesi in `testo` è una bozza-LLM compressa e può omettere condizioni/eccezioni presenti solo in `testo_integrale` — per interpretazione normativa affidabile, verificare sempre `testo_integrale` quando disponibile, non fermarsi alla sintesi.

### Storico "ticket" nei commenti

`schema.sql` e `seed.py` referenziano numeri di "ticket" sequenziali (03, 04, 05, 07, 08) come origine di varie decisioni di design (es. `modifiche_rilevate` da ticket 05, nodo Principio da ticket 08/ADR-0004). Un file `map.md` è citato nei commenti come riferimento per la cronologia di queste decisioni ma non è presente nell'albero del repo (potrebbe esistere solo nella storia git).

### Inconsistenza nota: eIDAS/eIDAS2 come due Fonti

`CONTEXT.md` dichiara che una Fonte esiste una volta sola nel censimento, ma `seed.py` modella eIDAS 910/2014 ed eIDAS2 (2024/1183) come **due righe `fonti` separate** (scelta esplicita per permettere confronto prima/dopo), segnalata in un commento di `seed.py` come divergenza da riconciliare con l'utente, non ancora risolta.
