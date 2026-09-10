Type: grilling
Status: resolved
Blocked by: 04, 08 (li estende)

## Question

Il contratto degli 8 tool MCP (ticket 04) è targato solo su Obbligo. Con l'introduzione di Principio come secondo tipo di nodo (ticket 08 / ADR-0004), come si estende il contratto? In particolare: `interroga_obblighi` deve poter rispondere anche quando la risposta è un Principio (una domanda in NL non sa a priori quale dei due tipi di nodo le risponde — è esattamente il caso che ha originato il ticket 08); `obbligo_vicini`/`obbligo_cammino` navigano un grafo che ora è eterogeneo.

## Answer

Deciso il 9/9/2026, in continuità con i criteri già fissati nel ticket 04.

### Decisioni chiave

- **Tool "di scrittura" restano separati per tipo di nodo** (`scrivi_bozze_obblighi` invariato + nuovo `scrivi_bozze_principi`), non un unico tool con campi condizionali: Obbligo e Principio hanno forme diverse (soggetti obbligati/destinatari vs. oggetti giuridici multi-valore), coerente con il criterio già in ticket 04 ("un tool per operazione", dove qui "scrivere un Obbligo" e "scrivere un Principio" sono operazioni diverse per forma del dato, non solo per tipo).
- **Tool di "lettura puntuale" restano separati per tipo** (`obbligo_dettaglio` invariato + nuovo `principio_dettaglio`), stesso motivo: gli attributi pieni restituiti sono diversi.
- **Tool di navigazione del grafo generalizzati, non duplicati**: "vicini di un nodo" e "cammino tra due nodi" sono la stessa operazione a prescindere dal tipo di nodo alle estremità (la stessa `InterfacciaGrafo` del ticket 03 lo dimostra: non ha mai saputo di Obbligo, solo di ID di nodo). Rinominati e parametrizzati con un discriminante `tipo_nodo`:
  - `obbligo_vicini` → **`nodo_vicini`**
  - `obbligo_cammino` → **`nodo_cammino`**
- **`interroga_obblighi` → `interroga_censimento`**: deve restituire sia Obblighi sia Principi nello stesso risultato ordinato, ciascuno con un campo `tipo_nodo` discriminante — è il motivo diretto per cui è nata questa estensione (una domanda in NL non sa a priori quale tipo di nodo le risponde). I filtri specifici di un tipo (`tipo_obbligo`, `categoria_soggetto` da un lato; `tipo_principio`, `oggetto_giuridico` dall'altro) si applicano solo ai risultati del tipo pertinente, senza escludere l'altro tipo dai risultati — stesso comportamento già validato nella UI web (ticket 07).
- **`valori_lookup` esteso**: aggiunge `tipi_principio` e `oggetti_giuridici`; la chiave `stati_obbligo` diventa `stati_norma` (condivisa tra i due tipi, ticket 08).
- **`monitoraggio_stato` esteso**: il matching "obblighi impattati" per `fonte_id`+`riferimento` (ticket 05) deve cercare anche tra i Principi, non solo tra gli Obblighi — un cambiamento di fonte può impattare un principio dichiarativo tanto quanto un obbligo. Campo di risposta rinominato `nodi_impattati` (ciascuno con `tipo_nodo`).
- **`fonte_lista` invariato**: il concetto di Fonte non è toccato da questa estensione.

### I tool (10, non più 8)

1. `interroga_censimento` (era `interroga_obblighi`) — ora restituisce Obblighi e Principi, discriminati da `tipo_nodo` in ogni risultato.
2. `scrivi_bozze_obblighi` — invariato.
3. `scrivi_bozze_principi` (nuovo) — stesso pattern di `scrivi_bozze_obblighi` (persiste soltanto, nessuna estrazione; rifiuta valori di lookup sconosciuti senza auto-crearli), campi: `riferimento`, `testo`, `tipo_principio`, `stato_norma`, `condizione_applicabilita`, `oggetti_giuridici: list[str]`.
4. `monitoraggio_stato` — esteso a `nodi_impattati` (Obblighi e Principi).
5. `obbligo_dettaglio` — invariato.
6. `principio_dettaglio` (nuovo) — analogo a `obbligo_dettaglio` per Principio.
7. `nodo_vicini` (era `obbligo_vicini`) — parametro aggiuntivo `tipo_nodo: Literal["obbligo","principio"]` per il nodo di partenza; ogni vicino nella risposta porta il proprio `tipo_nodo`.
8. `nodo_cammino` (era `obbligo_cammino`) — richiede `tipo_nodo_da` e `tipo_nodo_a` oltre agli id, perché le due estremità possono essere di tipo diverso.
9. `fonte_lista` — invariato.
10. `valori_lookup` — esteso con `tipi_principio`, `oggetti_giuridici`; `stati_obbligo` → `stati_norma`.

### Non ancora deciso

- Se e come ordinare/pesare insieme risultati Obbligo e Principio nel ranking semantico di `interroga_censimento` quando l'implementazione reale (Qdrant) sarà collegata — allo stato attuale (solo full-text) i due risultati sono semplicemente concatenati, senza un punteggio comune da confrontare.
