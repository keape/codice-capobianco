> **STORICO — superato dalla migrazione a Neo4j (ADR-0006, eseguita).** Questa spec descriveva
> l'implementazione via `qmd` (indice vettoriale file-based, `app/qmd_search.py`/`app/export_qmd.py`).
> La migrazione decisa in ADR-0006 è stata eseguita (`docs/plan-migrazione-neo4j.md`): lo storage è
> ora Neo4j, con vector index HNSW nativo popolato da `app/embed_neo4j.py` e un endpoint di ricerca
> ibrida a fusione WRRF (`GET /api/ricerca` in `app/web_ui.py`), sostituendo interamente `qmd`. I file
> `app/qmd_search.py`, `app/export_qmd.py` e la directory `app/qmd_export/` sono stati rimossi. Questo
> documento resta solo come riferimento storico della decisione pre-migrazione, non descrive più il
> comportamento attuale del sistema — vedi `CLAUDE.md` per lo stato corrente.

# Spec: ricerca semantica su codice-capobianco via qmd

## Contesto

Repo: `codice-capobianco` (censimento obblighi/principi QTSP, SQLite + FastAPI in `app/web_ui.py`, schema in `app/schema.sql`). Leggere `CLAUDE.md` del repo prima di iniziare.

Stato attuale della ricerca (`app/web_ui.py`, endpoint `/api/obblighi` e `/api/principi`):
- Scansione Python su tutte le righe delle tabelle `obblighi`/`principi`.
- Match case-insensitive su `testo` (sintesi LLM), `riferimento`, e ora anche `testo_integrale` (esteso in sessione precedente).
- Nessuna ricerca semantica/vettoriale esiste. `CONTEXT.md`/`CLAUDE.md` la segnalano come funzione futura `interroga_obblighi`, mai implementata.

Ogni riga `obblighi`/`principi` ha: `id`, `riferimento`, `testo` (sintesi), `testo_integrale` (testo normativo pieno, spesso presente ma non sempre), `fonte_id`, `stato_validazione` (`bozza`/`validato`).

## Obiettivo

Aggiungere una ricerca semantica che affianchi (non sostituisca) quella full-text esistente, usando il tool CLI esterno `qmd` (già installato: `~/.nvm/versions/node/v20.20.2/bin/qmd`, dati su `/Volumes/Ext.Lexar/Costola del Mac/qmd`, config in `~/.config/qmd/index.yml`, leggere `qmd`'s `CLAUDE.md` in quella cartella per i comandi).

`qmd` indicizza **file** su filesystem (BM25 + vettoriale + reranking), non righe SQLite: non ha integrazione diretta col DB. Serve quindi un layer di export + wiring.

## Passi implementativi

1. **Export DB → file markdown**
   Script (es. `app/export_qmd.py`) che legge `obblighi` e `principi` da `censimento.db` e scrive un file `.md` per ciascun record in `app/qmd_export/` (es. `obbligo-{id}.md`, `principio-{id}.md`), contenente `riferimento`, `fonte`, `testo`, `testo_integrale`. Deve poter girare da zero (rigenera tutto) e in modo idempotente.

2. **Registrazione collection qmd**
   ```
   qmd collection add app/qmd_export --name codice-capobianco --mask "**/*.md"
   qmd embed
   ```
   Verificare con `qmd status` / `qmd collection list`.

3. **Sincronizzazione export ↔ DB**
   Decidere quando rigenerare l'export: ad ogni avvio di `web_ui.py`? Dopo ogni scrittura (validazione, edit) via hook nell'endpoint POST/PUT? Minimo indispensabile: comando manuale documentato in `CLAUDE.md`, da rilanciare dopo `seed.py` o dopo modifiche in coda di revisione. Senza questo passo l'indice diverge silenziosamente dal DB (rischio reale, va reso visibile — es. timestamp export vs `mtime` del DB mostrato in UI o loggato).

4. **Wiring in `web_ui.py`**
   Nuovo endpoint, es. `GET /api/ricerca-semantica?q=...`, che invoca `qmd query <q> -c codice-capobianco --json -n <k>` via `subprocess`, parsa il JSON risultato (contiene path/docid/score), estrae `id` e tipo (`obbligo`/`principio`) dal nome file, e joina con il DB per restituire le righe complete (stesso formato di `_riga_obbligo`/`_riga_principio`). Gestire: `qmd` non installato/non raggiungibile, timeout, nessun risultato.

5. **UI**
   Aggiungere in frontend (stringa `INDEX_HTML` in `web_ui.py`) un modo per lanciare la ricerca semantica separata da quella full-text esistente (es. toggle o box "ricerca per significato"), mostrando risultati con score.

6. **Decisioni aperte da confermare con l'utente prima di implementare**
   - Sincrona (chiamata `qmd` bloccante in richiesta HTTP) vs pre-calcolata/cache.
   - Usare `qmd query` (con reranking, più lento, usa LLM locale) o `qmd vsearch` (solo vettoriale, più veloce, no LLM) — vedi trade-off in `qmd`'s `CLAUDE.md`.
   - Come gestire righe non ancora validate (`stato_validazione='bozza'`): includerle nell'export/ricerca semantica o no (coerenza con `solo_validati` esistente in full-text).
   - Chi/cosa triggera il re-export (manuale, hook, cron).

## File da toccare

- Nuovo: `app/export_qmd.py`
- Nuovo (generato, non versionato): `app/qmd_export/*.md`
- Modificato: `app/web_ui.py` (nuovo endpoint + frontend)
- Eventuale: `.gitignore` per `app/qmd_export/`
- Documentare comando di re-export in `CLAUDE.md` del repo (sezione Comandi)

## Non fare

- Non sostituire la ricerca full-text esistente (`testo`/`riferimento`/`testo_integrale`) — la semantica è aggiuntiva.
- Non chiamare LLM esterni con API key propria per generare embedding: `qmd` gira in locale (modelli GGUF cache in `models/`), coerente con ADR-0003 del repo (estrazione LLM solo dentro sessioni Claude Code, mai batch autonomo con API key propria) — verificare che questo vincolo si applichi anche a `qmd embed`/`qmd query` o se va trattato come eccezione esplicita da discutere con l'utente.
