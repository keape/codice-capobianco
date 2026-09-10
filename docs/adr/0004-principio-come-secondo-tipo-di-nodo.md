# Principio come secondo tipo di nodo del grafo, con relazioni polimorfiche non vincolate a livello di FK

Contesto: il censimento (ADR-0001) modella solo Obblighi — prescrizioni che impongono un comportamento a un soggetto (CONTEXT.md). Un caso reale ha mostrato il limite: la domanda "può un giudice non tenere in considerazione un documento firmato con firma elettronica?" non trova risposta, perché la norma che la governa (art. 25 eIDAS, non discriminazione della firma elettronica) non impone un comportamento a nessuno — dichiara un effetto giuridico. `seed.py` la escludeva esplicitamente per questo motivo.

Due alternative erano possibili per rappresentarla:

1. Rilassare "Obbligo" per ammettere righe senza soggetto obbligato.
2. Introdurre un secondo tipo di nodo, "Principio", con attributi propri (tipo di principio, oggetto giuridico a cui si applica) invece del solo soggetto obbligato/destinatario.

Deciso: (2). Un Obbligo e un Principio sono concettualmente due cose diverse (prescrizione vs. dichiarazione di effetto) e confonderli in un'unica tabella con colonne opzionali avrebbe reso "soggetto obbligato NULL" un modo implicito e ambiguo per dire "questo non è un vero obbligo" — meno esplicito di un tipo di nodo dedicato, e più difficile da filtrare correttamente nelle interrogazioni.

Il grafo (ADR-0001) diventa quindi eterogeneo: due tipi di nodo, con relazioni tipizzate che possono collegare Obbligo↔Obbligo, Obbligo↔Principio, Principio↔Principio (es. un Obbligo tecnico su validazione firme può "specificare" il Principio generale sull'equivalenza giuridica della firma qualificata).

Conseguenza sullo schema (ADR-0002, ADR-0003 schema dati): `relazioni` non può più avere `obbligo_da_id`/`obbligo_a_id` con `REFERENCES obblighi(id)`, perché l'estremità può appartenere a `obblighi` o a `principi`. Due opzioni erano possibili:

- **Tabella `nodi` di supertipo**, con `obblighi` e `principi` che vi si agganciano 1:1, e `relazioni` con FK verso `nodi(id)` — mantiene l'integrità referenziale a livello di database.
- **Colonne discriminanti senza FK** (`nodo_da_tipo`, `nodo_da_id`, `nodo_a_tipo`, `nodo_a_id`), con l'integrità verificata a livello applicativo.

Deciso: colonne discriminanti senza FK. La tabella di supertipo raddoppierebbe ogni scrittura (riga in `obblighi`/`principi` + riga in `nodi`) per un beneficio — l'integrità referenziale a livello di database sulle relazioni — che l'architettura a tool MCP granulari (ticket 04) già rinuncia altrove: `scrivi_bozze_obblighi` valida a mano i valori di lookup invece di delegarli a un vincolo DB, con lo stesso argomento (l'unico punto di scrittura è un tool applicativo, non SQL sparso). La stessa disciplina si estende naturalmente alla validazione delle estremità di una relazione. Trade-off accettato consapevolmente: un `INSERT` in `relazioni` con un `nodo_da_id` inesistente per il tipo dichiarato non viene bloccato dal database, solo dal tool che lo scrive.

Perché fissarlo ora e non quando arriverà un terzo tipo di nodo: cambiare la forma di `relazioni` dopo che il grafo è popolato richiederebbe ri-migrare tutte le righe esistenti (stesso argomento tempificazione di ADR-0001) — e il primo caso concreto che avrebbe richiesto la migrazione è già qui.
