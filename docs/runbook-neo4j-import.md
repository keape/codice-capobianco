# Runbook infrastrutturale — import granulare su Neo4j

Problemi già incontrati e risolti durante l'import granulare eIDAS/eIDAS2
(2026-09-15, ADR-0007). Consultare **prima** di rimettersi a diagnosticare
da zero un ambiente che non risponde: il costo di questi problemi, la
prima volta, è stato di ore di debug alla cieca dentro la sessione di
estrazione — con guardie e procedure note, dovrebbe essere zero.

## 1. Il driver Python `neo4j` si blocca indefinitamente

**Sintomo:** una query dal driver Python (`GraphDatabase.driver(...).session()...run(...)`)
non ritorna mai, né errore né risultato. `cypher-shell` e una connessione
socket raw alla porta bolt rispondono normalmente nello stesso momento —
il server non è il problema.

**Causa:** `neo4j==6.3.0` è incompatibile con questa istanza Neo4j Desktop
(server `2026.08.1`).

**Fix:** `pip install 'neo4j==5.28.1'` nel venv usato per gli script
(`seed.py`, `migrate_to_neo4j.py`, `embed_neo4j.py`, `web_ui.py`).

**Guardia automatica:** `app/neo4j_common.get_driver()` verifica ora la
versione installata (`importlib.metadata.version("neo4j")`) e solleva
`RuntimeError` immediato con messaggio esplicito se diversa da `5.28.1`
(`VERSIONE_DRIVER_ATTESA` in `app/neo4j_common.py`). Se il pin va aggiornato
di proposito (nuova versione verificata compatibile), aggiornare quella
costante nello stesso commit.

## 2. Il venv `app/.venv` si blocca in modo intermittente e indipendente dal driver

**Sintomo:** comandi Python/pip lenti o bloccati anche per operazioni che
non toccano Neo4j.

**Causa:** `app/.venv` vive dentro iCloud Drive (il repo è sotto
`~/Library/Mobile Documents/com~apple~CloudDocs/...`); iCloud materializza
i file on-demand e può bloccare l'accesso a moduli del venv non ancora
scaricati localmente.

**Fix:** usare un venv operativo fuori iCloud per eseguire gli script,
`~/venvs/compliance-rag` (stesse dipendenze di `app/.venv`: fastapi,
uvicorn, pydantic, `neo4j==5.28.1`, sentence-transformers). Se non esiste
ancora sulla macchina in uso:

```bash
python3 -m venv ~/venvs/compliance-rag
~/venvs/compliance-rag/bin/pip install fastapi uvicorn pydantic 'neo4j==5.28.1' sentence-transformers
```

Usare `~/venvs/compliance-rag/bin/python` al posto di `app/.venv/bin/python`
per `seed.py`/`web_ui.py`/`embed_neo4j.py`/`migrate_to_neo4j.py` se
`app/.venv` mostra blocchi anomali. `app/.venv` resta quello canonico
documentato in CLAUDE.md; il venv fuori iCloud è un fallback operativo, non
una sostituzione permanente.

## 3. Neo4j Desktop smette di accettare connessioni bolt

**Sintomo:** la porta TCP 7687 è aperta (si connette) ma nessuna query,
neanche da `cypher-shell`, va a buon fine.

**Causa osservata:** Neo4j Desktop (la GUI) diventa non responsiva senza
killare il processo del DBMS sottostante in modo pulito.

**Fix:** avviare l'istanza direttamente col binario Neo4j, bypassando la
GUI, gestito come processo `hub` con nome fisso così resta ispezionabile
tra una sessione e l'altra:

```
hub op=start name=neo4j-direct application=<path-binario-neo4j> args=[console]
```

(path esatto del binario e della cartella dati: dipende dall'installazione
Neo4j Desktop locale — verificare con `computer`/Finder la posizione
dell'istanza `compliance-rag` prima di lanciare, non indovinare un path).

**Verifica di readiness:** `ready: { port: 7687, timeout: 30 }` sullo start,
poi una query di prova (`cypher-shell` o driver) prima di procedere con
`seed.py`.

## 4. Prima di ogni sessione di import

Checklist rapida (sostituisce la diagnosi da zero):

1. Neo4j Desktop avviato e responsivo? Se no, punto 3.
2. `python -c "from importlib.metadata import version; print(version('neo4j'))"`
   nel venv che si userà → deve stampare `5.28.1`. Se no, punto 1 (la
   guardia in `get_driver()` lo segnala comunque al primo uso).
3. Se il venv sotto iCloud mostra blocchi anomali su comandi banali → punto 2.

Se uno di questi problemi si ripresenta in una forma nuova (non coperta
sopra), risolverlo **in una sessione/subagent dedicato alla sola
infrastruttura**, non dentro la sessione che sta autorando contenuto
normativo — altrimenti il rumore diagnostico si accumula nello stesso
contesto del lavoro di dominio e ne gonfia il costo (vedi
`docs/procedura-import-granulare.md` per la separazione dei ruoli).

## Log interventi

**2026-09-16** — Verifica strumentale dei punti 1-2: `app/.venv` (sotto
iCloud Drive) aveva ancora `neo4j==6.3.0` installato. Riprodotto live il
sintomo del punto 1: `import neo4j` si blocca indefinitamente (timeout
15s, nessun errore, nessun output) usando `app/.venv/bin/python`. Lo
stesso comando su `~/venvs/compliance-rag` (venv fuori iCloud, pin
corretto `5.28.1`) risponde in 0.2s.

Tentativo di fix in-place (`app/.venv/bin/pip install neo4j==5.28.1`) con
timeout brevi (40s, 60s): **si blocca anch'esso**, non solo a runtime ma
già in fase di scrittura del pacchetto scaricato su disco (log verboso:
richiesta HTTP e download del wheel completano, il comando si blocca dopo
`Downloading neo4j-5.28.1-py3-none-any.whl (312 kB)` senza mai arrivare a
`Successfully installed`) — conferma che il problema del punto 2 (iCloud
che blocca l'accesso ai file del venv) non è limitato alla lettura di
moduli già installati, riguarda anche le scritture nuove (disinstallazione
del vecchio pacchetto + scrittura del nuovo).

**Risolto** con un timeout più lungo (240s): l'operazione (uninstall
`neo4j-6.3.0` + install `neo4j-5.28.1`) è effettivamente completata,
richiedendo probabilmente 1-4 minuti per la sincronizzazione iCloud dei
file del venv, non bloccata in modo permanente. Verificato: `import neo4j`
in `app/.venv` ora risponde in 0.29s, guardia versione passata.
`app/.venv` è di nuovo utilizzabile.

**Conclusione operativa:** se `app/.venv` mostra questo sintomo, non è
detto sia rotto in modo permanente — può essere solo lento per via di
iCloud. Primo tentativo: `pip install` con **timeout lungo (≥3-4 minuti)**
prima di considerarlo bloccato e passare al venv di fallback
`~/venvs/compliance-rag`. Non lanciare altro lavoro nella stessa sessione
mentre si attende, per non confondere lentezza-per-attesa con blocco
reale. Se anche con timeout lungo non completa, usare il fallback (punto
2) senza insistere oltre.
