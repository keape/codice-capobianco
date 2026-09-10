Type: grilling
Status: resolved
Blocked by: 03

## Question

Definire il formato esatto del processo di estrazione guidato da Claude Code: come si struttura la richiesta (es. "estrai gli obblighi dall'articolo N della Fonte X") in modo che le bozze generate rispettino lo schema dati (ticket 03) fin dalla generazione, come vengono scritte nella coda di revisione (tabella/stato "bozza" vs "validato"), e cosa succede se l'LLM propone relazioni tipizzate verso obblighi non ancora esistenti nel censimento (es. riferimento a un obbligo di una Fonte non ancora estratta).

## Answer

Deciso senza grilling il 9/9/2026 — le scelte discendono direttamente dai contratti già fissati in 03/04; l'unico punto realmente aperto (relazioni verso obblighi non ancora esistenti) è risolto qui in modo coerente con il resto.

### Decisioni chiave

- **Formato della richiesta**: in linguaggio naturale, del tipo "estrai gli obblighi dall'articolo N della Fonte X" (o un intervallo di articoli) — non un formato strutturato separato. Non serve un parser dedicato: è la sessione Claude Code stessa a interpretare la richiesta e orchestrare i passi sotto, gli unici punti che *devono* essere strutturati sono le chiamate ai tool MCP (04), non la richiesta dell'utente.
- **Passi della sessione** (nessun passo chiama un LLM esterno al di fuori della sessione stessa, coerente con ADR-0003):
  1. `valori_lookup()` — recupera le stringhe enum valide *prima* di estrarre, così l'estrazione produce fin da subito valori accettati da `scrivi_bozze_obblighi` (niente tentativi-ed-errori sul tool).
  2. Recupero del testo dell'articolo dalla `url_sorgente` della Fonte (via `fonte_lista()` per risolvere l'id → url), usando le capacità di lettura web della sessione — non un tool MCP dedicato: il testo integrale non è cache-ato nello schema (già deciso in 04), quindi non c'è un tool "leggi articolo" da chiamare.
  3. Estrazione strutturata del testo in bozze conformi allo schema (03): un Obbligo per prescrizione atomica identificata nel testo, con `riferimento` preciso (articolo/comma/lettera).
  4. `scrivi_bozze_obblighi(fonte_id, bozze)` — persiste con `stato_validazione='bozza'` (default già nello schema 03); nessuna scrittura diretta a SQL, sempre tramite il tool.
  5. Riepilogo testuale all'utente delle bozze scritte, con invito a validarle nella coda di revisione della UI (ticket 07) — la sessione non valida le proprie bozze.
- **Coda di revisione**: nessuna tabella separata — le bozze *sono* righe di `obblighi` con `stato_validazione='bozza'` (decisione già presa in 03). La UI (07) filtra su questo stato per popolare la coda; non serve un meccanismo di trasferimento tra tabelle "bozze" e "obblighi validati".
- **Relazioni verso obblighi non ancora esistenti — la vera domanda aperta**: lo schema (03) impone `relazioni.obbligo_da_id`/`obbligo_a_id` come FK verso `obblighi` esistenti (`ON DELETE RESTRICT`), e il contratto originale di `scrivi_bozze_obblighi` (04) scrive solo Obblighi, non Relazioni — non esisteva alcun modo per proporre una relazione durante l'estrazione. Risolto estendendo il contratto:
  - `scrivi_bozze_obblighi` accetta un campo opzionale per bozza, `relazioni_proposte: list[{tipo_relazione: str, verso_riferimento: str, fonte_riferimento_id: int | None}]` (se `fonte_riferimento_id` è `None`, si assume la stessa Fonte dell'obbligo corrente).
  - Per ciascuna relazione proposta, il tool cerca un Obbligo esistente con quel `riferimento`/`fonte_id`: se lo trova, crea la riga in `relazioni`; **se non lo trova, scarta la relazione e la riporta in un campo `relazioni_scartate` della risposta** (non è un errore bloccante: l'Obbligo stesso viene comunque persistito come bozza). La sessione che ha ricevuto `relazioni_scartate` informa l'utente che quella relazione andrà riproposta manually una volta estratta anche la Fonte/l'articolo di destinazione.
  - Coerente con il principio già stabilito in 04 per i valori di lookup ("nessuna auto-creazione implicita"): qui il nodo target mancante non viene creato come segnaposto, per non popolare il censimento di Obblighi fantasma senza testo né validazione.
  - Contratto aggiornato: `scrivi_bozze_obblighi(...) -> { status, message?, obbligo_id?: [int], relazioni_scartate?: [{riferimento_sorgente, tipo_relazione, verso_riferimento}] }`.
