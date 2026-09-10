Type: grilling
Status: resolved
Blocked by: 03

## Question

Definire l'insieme esatto dei tool MCP esposti da questo strumento (analogo agli 8 tool di sgsi-rag) e il contratto di ciascuno (input/output). Coprire almeno: interrogazione ibrida in NL (faceted + semantico + sintesi), avvio dell'estrazione LLM di una porzione di Fonte (scrive bozze in coda di revisione), stato del monitoraggio (fonti con modifiche rilevate), e le operazioni di consultazione dirette del grafo (es. relazioni di un obbligo). Dipende dallo schema dati (ticket 03) per i contratti concreti di input/output.

## Answer

Deciso tramite grilling il 9/9/2026.

### Decisioni chiave

- **8 tool granulari**, uno per operazione (non tool "dispatcher" consolidati) — coerente con il pattern già validato in `sgsi-rag/mcp_server.py` (8 tool, uno per operazione, dispatch comune con cattura eccezioni).
- **Nessun tool fa sintesi testuale né chiama un LLM proprio** (ADR-0003): `interroga_obblighi` restituisce solo dati grezzi ordinati (filtro faceted + ranking semantico via similarità vettoriale su Qdrant, nessuna generazione); la sintesi in linguaggio naturale la produce la sessione Claude Code chiamante, che ha già i risultati come contesto.
- **`scrivi_bozze_obblighi` non estrae, persiste soltanto**: l'estrazione (lettura del testo della Fonte, identificazione degli Obblighi) è compito della sessione Claude Code; il tool si limita a scrivere righe con `stato_validazione = 'bozza'`. Il testo integrale della Fonte non è cache-ato nello schema (tabelle `fonti`/`obblighi` non lo prevedono) — la sessione lo recupera direttamente dall'URL sorgente (EUR-Lex/Normattiva) con le proprie capacità di lettura web, fuori da questo set di tool.
- **Filtri faceted a lista, OR entro campo / AND tra campi**: riflette che `obbligo_soggetti` è multi-valore e che l'utente può voler includere più categorie/stati in una stessa domanda.
- **Bozze escluse di default dalle risposte** (`solo_validati=True` in `interroga_obblighi`): le domande operative reali non devono essere inquinate da bozze non ancora validate da un umano.
- **Valori di lookup non auto-creati**: `scrivi_bozze_obblighi` rifiuta con errore esplicito una bozza che usa un valore di `tipo_obbligo`/`stato_obbligo`/`categoria_soggetto`/`tipo_relazione` non presente in lookup, invece di crearlo implicitamente — l'estendibilità delle lookup (ticket 03) è pensata per un'evoluzione deliberata dello schema di classificazione, decisa da un umano, non per assorbire varianti quasi-duplicate prodotte da un'estrazione LLM. Da qui la necessità di `valori_lookup`, perché la sessione chiamante sappia in anticipo quali stringhe sono valide.
- **Tool di monitoraggio a contratto minimo**: il ticket 05 (meccanismo di diff tra versioni di una Fonte) è ancora aperto, quindi `monitoraggio_stato` fissa solo `fonte_id`, `nome`, `data_rilevamento`; altri campi (riassunto diff, obblighi impattati) restano espliciti "TBD — ticket 05".
- **Convenzione di errore comune**, coerente con `sgsi-rag`: ogni tool restituisce sempre `{status: "ok"|"error", ...}` (con `message` in caso di errore), nessuna eccezione propagata al chiamante MCP.

### I tool

1. **`interroga_obblighi`** — interrogazione ibrida: filtro faceted sui metadati + ranking semantico sul sottoinsieme.

   ```
   interroga_obblighi(
       query_semantica: str,
       fonte_id: list[int] | None = None,
       tipo_obbligo: list[str] | None = None,
       stato_obbligo: list[str] | None = None,
       categoria_soggetto: list[str] | None = None,
       ruolo: Literal["obbligato","destinatario"] | None = None,
       solo_validati: bool = True,
       n_risultati: int = 10,
   ) -> {
       status: "ok"|"error", message?: str,
       risultati: [{ obbligo_id, punteggio, fonte, riferimento, testo,
                      tipo_obbligo, stato_obbligo, ... }]
   }
   ```

2. **`scrivi_bozze_obblighi`** — scrive bozze già estratte dalla sessione chiamante in coda di revisione.

   ```
   scrivi_bozze_obblighi(
       fonte_id: int,
       bozze: list[{
           riferimento: str, testo: str, tipo_obbligo: str,
           stato_obbligo: str, severita: str | None, sanzioni: str | None,
           condizione_applicabilita: str | None,
           soggetti_obbligati: list[str], destinatari: list[str],
       }]
   ) -> { status: "ok"|"error", message?: str, obbligo_id?: [int] }
   ```

   Errore esplicito (nessuna auto-creazione) se un valore di lookup referenziato non esiste.

3. **`monitoraggio_stato`** — fonti con modifica rilevata non ancora esaminata.

   ```
   monitoraggio_stato() -> {
       status: "ok",
       fonti_con_modifiche: [{ fonte_id: int, nome: str, data_rilevamento: str, ... }]
       # campi aggiuntivi da definire con ticket 05
   }
   ```

4. **`obbligo_dettaglio`** — attributi pieni di un Obbligo.

   ```
   obbligo_dettaglio(obbligo_id: int) -> {
       status: "ok"|"error", message?: str,
       obbligo?: { ...tutti i campi di `obblighi`, fonte: {...},
                    soggetti_obbligati: [str], destinatari: [str] }
   }
   ```

5. **`obbligo_vicini`** — wrapper arricchito di `InterfacciaGrafo.vicini` (ticket 03).

   ```
   obbligo_vicini(
       obbligo_id: int, tipo_relazione: str | None = None,
       direzione: Literal["uscenti","entranti","entrambe"] = "entrambe",
   ) -> {
       status: "ok"|"error", message?: str,
       vicini?: [{ obbligo_id, tipo_relazione, relazione_id, riferimento, testo }]
   }
   ```

6. **`obbligo_cammino`** — wrapper arricchito di `InterfacciaGrafo.cammino` (ticket 03).

   ```
   obbligo_cammino(obbligo_da_id: int, obbligo_a_id: int, max_salti: int) -> {
       status: "ok"|"error", message?: str,
       cammino?: [{ obbligo_id, tipo_relazione, relazione_id, riferimento, testo }] | None
   }
   ```

7. **`fonte_lista`** — punto di ingresso per navigare le Fonti censite senza conoscerne l'id.

   ```
   fonte_lista() -> {
       status: "ok",
       fonti: [{ fonte_id, nome, versione, stato, url_sorgente }]
   }
   ```

8. **`valori_lookup`** — valori validi delle enumerazioni, per guidare estrazione e filtri.

   ```
   valori_lookup() -> {
       status: "ok",
       tipi_obbligo: [str], stati_obbligo: [str],
       categorie_soggetto: [str], tipi_relazione: [{nome, nome_inverso}]
   }
   ```
