Type: feature
Status: risolto
Blocked by: 03

## Question

Costruire la UI web (analoga a `web_ui.py` di sgsi-rag, sola lettura + coda di revisione) che copra: consultazione/ricerca del censimento con visualizzazione delle relazioni tipizzate del grafo, coda di revisione delle bozze generate dall'estrazione (validare/correggere/rifiutare), e badge di notifica attiva per le fonti con modifiche rilevate dal monitoraggio. Serve a far reagire l'utente a un artefatto concreto prima di impegnarsi sui tool MCP definitivi. Dipende dallo schema dati (ticket 03) per usare dati realistici.

## Realizzato

Costruito il 9/9/2026 in [app/](../../Censimento-Obblighi-QTSP/app/) (FastAPI + SQLite, HTML/JS inline — stesso pattern di `sgsi-rag/web_ui.py`): `schema.sql` (schema 03 + tabella `modifiche_rilevate` di 05), `seed.py` (prima con dati di esempio parafrasati, poi sostituiti dalla prima estrazione reale — vedi ticket 08 e map.md), `web_ui.py` (le tre viste: Consultazione con filtri faceted + dettaglio/grafo, Coda di revisione editabile con valida/rifiuta, Monitoraggio con diff e obblighi impattati collegabili). Avvio:

```
.venv\Scripts\python.exe seed.py
.venv\Scripts\python.exe web_ui.py --port 8010
```

Verificato in browser: ricerca/filtri, dettaglio con relazioni navigabili, validazione di una bozza (persiste in SQLite, aggiorna il badge), vista monitoraggio con diff testuale e link agli obblighi impattati. Riusa l'ambiente virtuale di `RAG-QTSP/sgsi-rag` (fastapi/uvicorn già installati) senza modificarlo. La reazione dell'utente è stata raccolta e ha portato al ticket 08; l'utente ha inoltre deciso di considerare questa UI e il censimento sottostante come strumento in produzione (non più un prototipo) da adesso in poi. Restano da fare i tool MCP definitivi (04) e il meccanismo di monitoraggio (05).
