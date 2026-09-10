Type: grilling
Status: resolved
Blocked by: 03, 04 (li estende)

## Question

Un test della UI web (ticket 07) su una domanda operativa reale — "può un giudice non tenere in considerazione un documento firmato con firma elettronica?" — non ha trovato risultati pertinenti. La norma che risponde (art. 25 eIDAS, non discriminazione della firma elettronica) è esclusa esplicitamente da `seed.py` perché non impone un comportamento a un soggetto: non è un Obbligo secondo CONTEXT.md. Come estendere il modello per coprire anche queste norme, e qual è l'impatto su schema dati (ticket 03) e contratto tool MCP (ticket 04)?

## Answer

Deciso il 9/9/2026, in sessione con l'utente (domain modeling).

### Decisioni chiave

- **Nuovo tipo di nodo "Principio"**, non un rilassamento di "Obbligo" — vedi [ADR-0004](../../../Censimento-Obblighi-QTSP/docs/adr/0004-principio-come-secondo-tipo-di-nodo.md) e la voce "Principio" in CONTEXT.md. Attributi: fonte + riferimento, testo, tipo di principio (non discriminazione / equivalenza giuridica / valore probatorio / presunzione legale / altro), oggetto giuridico multi-valore (firma elettronica per livello, sigillo elettronico per livello, marca temporale, documento elettronico, servizio di recapito, identificazione elettronica, altro), stato normativo, condizione di applicabilità, ciclo di validazione bozza/validato/rifiutato — stessa semantica di Obbligo dove applicabile.
- **Perimetro allargato**: non solo principi legati a strumenti QTSP, ma qualunque norma dichiarativa di eIDAS/CAD — la Destination del progetto (map.md) passa da "obblighi applicabili ai QTSP" a "obblighi e principi applicabili al perimetro eIDAS+CAD". Motivazione esplicita dell'utente: deve poter rispondere a quesiti operativi reali con richiami puntuali alle norme, anche quando la norma non è un obbligo QTSP in senso stretto.
- **Stesso grafo di relazioni tipizzate** di Obbligo (non un nodo isolato) — un Obbligo tecnico può "specificare" un Principio generale, coerente con l'asset di navigazione già richiesto fin dal pilota (ADR-0001).
- **`relazioni` diventa polimorfica** (`nodo_da_tipo`/`nodo_da_id`/`nodo_a_tipo`/`nodo_a_id` al posto di `obbligo_da_id`/`obbligo_a_id`), senza FK a livello di database sulle estremità — l'integrità è responsabilità del livello applicativo (stesso principio già adottato per i valori di lookup in `scrivi_bozze_obblighi`, ticket 04). Dettagli e alternative scartate in ADR-0004.
- **Lookup `stati_obbligo` rinominata `stati_norma`**: condivisa tra Obbligo e Principio (stessa semantica vigente/abrogato/in transizione), non duplicata.
- **Impatto sui tool MCP (ticket 04)**: il contratto degli 8 tool esistenti resta targato su Obbligo; servirà un secondo gruppo di tool analoghi per Principio (`scrivi_bozze_principi`, `principio_dettaglio`) o una generalizzazione con parametro `tipo_nodo` — **non ancora deciso**, resta in "Not yet specified" di map.md perché serve prima vedere l'uso reale nella UI. `interroga_obblighi`/`valori_lookup` dovranno restituire/filtrare anche sui Principi perché una domanda in linguaggio naturale non sa a priori se la risposta è un Obbligo o un Principio.
- **UI web (ticket 07) e seed**: aggiornati nella stessa sessione per dimostrare il caso concreto — art. 25 e art. 46 eIDAS (effetti giuridici di firme e documenti elettronici) aggiunti come Principi di esempio, con oggetto giuridico taggato, cosi' la domanda che ha originato questo ticket trova risposta nella consultazione faceted.

### Non ancora deciso

- Se Principio abbia anche un attributo "beneficiario" (chi trae l'effetto giuridico, es. "chi produce il documento in giudizio") — rimandato: non necessario per il caso che ha originato questo ticket, la faceted su oggetto giuridico + tipo di principio è sufficiente per ora.
- Contratto esatto dei tool MCP per Principio (vedi sopra).
- Se estendere l'estrazione al CAD (fonte non ancora caricata nel censimento) per i suoi articoli analoghi (art. 20-21, valore probatorio del documento informatico) — probabile prossimo passo naturale, ma fuori da questa sessione.
