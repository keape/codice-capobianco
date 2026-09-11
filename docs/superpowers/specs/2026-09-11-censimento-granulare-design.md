# Censimento granulare per articolo/comma: da import accorpato a produzione

## Contesto

Il censimento (ADR-0001, ADR-0004) è nato in fase prototipo con import selettivo e spesso accorpato: righe `obblighi`/`principi` che sintetizzano più articoli o più commi in un'unica riga con un'unica sintesi (`testo`). Esempi concreti in `app/seed.py` (fonte DPCM 22/2/2013): id 71 (`"art. 6-13"`, 8 articoli compressi in una frase), id 74 (`"art. 20-31"`, 12 articoli compressi in una frase), e altri (id 67-70, 72-73, 75-81) con lo stesso pattern su intervalli più piccoli.

Questo va bene per un prototipo, ma è incompatibile con lo scopo del censimento in fase di produzione: relazionare obblighi/principi provenienti da articoli e commi distinti tra loro (relazioni tipizzate, ADR-0004). Una riga che accorpa 8 articoli non può partecipare a relazioni granulari — non si può dire "l'obbligo dell'art. 8 è precondizione dell'art. 12" se entrambi sono fusi nella stessa riga.

Un errore concreto già occorso (correzione documentata al 2026-09-10 nei commenti di `seed.py`, split degli obblighi 82-88 per il Titolo V del DPCM) ha mostrato che il processo di estrazione stesso — non solo il singolo risultato — deve essere rivisto: mancava un meccanismo che garantisse, per una fonte, che ogni comma del testo ufficiale fosse effettivamente coperto da esattamente una riga.

## Obiettivo

Ristrutturare l'estrazione per tutte e 4 le fonti (eIDAS 910/2014, eIDAS2 2024/1183, CAD, DPCM 22/2/2013) passando a granularità "per unità di prescrizione distinta": niente accorpamento di default, split fino a livello di lettera/punto quando contiene obblighi indipendenti, merge di più commi solo se costituiscono davvero un'unica prescrizione continua. Il processo di estrazione adotta una checklist esplicita e verificata automaticamente. Le relazioni evidenti tra righe vengono create nella stessa passata, non rimandate.

## Decisioni di design confermate

1. **Granularità**: content-driven, non meccanica per comma. Una riga = una prescrizione indipendente; può stare sotto il livello di comma (split di lettere/punti indipendenti) o sopra (più commi fusi solo se genuinamente un'unica prescrizione continua).
2. **Tassonomia nodi**: nessuna nuova categoria pre-progettata oltre Obbligo/Principio (ADR-0004). Decisione caso per caso durante lo split, se emerge un pattern che né Obbligo né Principio rappresentano bene.
3. **Perimetro**: tutte e 4 le fonti in un'unica passata di lavoro (non pilota su una fonte sola).
4. **Relazioni**: create durante questa stessa passata quando evidenti, non rimandate a un secondo giro.
5. **Dati esistenti validati**: si riparte da zero. Il nuovo seed granulare sostituisce l'intero DB; le validazioni umane già fatte sulle righe accorpate vengono rifatte sulle righe granulari (nessuna migrazione incrementale delle validazioni pregresse).

## Architettura

`app/seed.py` diventa un orchestratore puro: importa lo schema, richiama la funzione di seed per ciascuna fonte, esegue la verifica di copertura, inserisce nel DB.

I dati grezzi si spostano in una nuova cartella `app/seed_data/`, un modulo per fonte:
- `eidas.py` (910/2014)
- `eidas2.py` (2024/1183)
- `cad.py`
- `dpcm.py`

Nessuna modifica a `schema.sql`: le relazioni polimorfiche (`nodo_da_tipo`/`nodo_a_tipo` + id senza FK, ADR-0004) restano invariate e bastano per collegare righe granulari tra loro, anche cross-fonte.

## Componenti

Ogni modulo `seed_data/<fonte>.py` espone:

- `RIGHE_OBBLIGHI: list[dict]` — righe granulari, stessa forma record di oggi (riferimento, testo, testo_integrale, categoria soggetto, ecc.), senza id espliciti (autoincrement DB).
- `RIGHE_PRINCIPI: list[dict]` — idem, per nodi Principio.
- `INDICE_ARTICOLI: list[str]` — indice completo delle unità normative attese dal testo ufficiale (es. `"art. 3 c.1"`, `"art. 3 c.2"`, `"art. 3 c.3 lett.a"`), costruito leggendo il testo ufficiale prima di scrivere qualunque riga.
- `MAPPATURA: dict[str, list[str]]` — chiave = riferimento riga, valore = lista di item di `INDICE_ARTICOLI` coperti da quella riga.
- `RELAZIONI: list[dict]` — `{nodo_da_rif, nodo_a_rif, tipo_relazione}`, riferimenti testuali (non id), risolti in id dopo l'insert.

`seed.py` fornisce:

- `verifica_copertura(indice, mappatura)`: controlla che ogni item di `INDICE_ARTICOLI` compaia in esattamente una voce di `MAPPATURA`. Solleva `ValueError` con l'elenco di item mancanti e item doppi se la copertura non torna.
- `inserisci_fonte(modulo)`: inserisce le righe, ottiene gli id reali dal DB, risolve `RELAZIONI` (riferimento testuale → id) e inserisce in `relazioni`.

## Flusso dati

**Fase di sviluppo** (dentro sessione Claude Code interattiva, ADR-0003), per fonte:

1. Costruire `INDICE_ARTICOLI` leggendo il testo ufficiale integrale (indice completo comma/lettera).
2. Scrivere `RIGHE_OBBLIGHI`/`RIGHE_PRINCIPI` granulari, con `testo_integrale` verificato contro il testo ufficiale (non ricostruito a memoria).
3. Scrivere `MAPPATURA` (riga → item indice coperti).
4. Durante la scrittura, se emerge una relazione evidente tra due righe già scritte — della stessa fonte, o di una fonte già completata in precedenza — aggiungerla subito a `RELAZIONI`.
5. Decidere caso per caso, riga per riga, se serve una categoria di nodo diversa da Obbligo/Principio.

**Fase di esecuzione** (`python app/seed.py`):

1. Drop/create schema.
2. Per ciascuna fonte, nell'ordine eIDAS → eIDAS2 → CAD → DPCM: `verifica_copertura` (blocca se l'indice non è coperto) → insert righe → risoluzione e insert relazioni.
3. Se la copertura fallisce su una fonte, stop immediato: nessun insert per le fonti successive (fail-fast).

L'ordine delle fonti (eIDAS → eIDAS2 → CAD → DPCM, dal più a monte temporalmente) conta perché una relazione cross-fonte (es. DPCM abrogato/sostituito da eIDAS2) può riferirsi solo a una fonte già inserita in precedenza.

## Gestione errori

- `verifica_copertura` solleva `ValueError` esplicito con item mancanti (nessuna riga li copre) e item doppi (coperti da più righe). Blocca l'insert della fonte corrente e di tutte le successive.
- Risoluzione `RELAZIONI`: se `nodo_da_rif`/`nodo_a_rif` non è trovato tra le righe appena inserite, `KeyError` esplicito con il riferimento mancante — nessun insert silenzioso di relazione rotta.
- Nessun try/except silenzioso: un fallimento del seed produce un traceback visibile; il comando va rieseguito da capo dopo il fix (schema è drop+recreate in un'unica run, niente stato parziale non segnalato).
- Le validazioni umane pregresse sulle righe accorpate non vengono migrate: si riparte da zero, tutte le righe granulari nascono `stato_validazione='bozza'` e passano di nuovo dalla coda di revisione in `web_ui.py`.

## Testing

Nessuna suite automatizzata nel repo (invariato). Per questo lavoro:

- `verifica_copertura` è il gate automatico eseguito a ogni `python app/seed.py` — sostituisce l'esigenza di test dedicati per la copertura.
- Verifica manuale post-seed, per fonte: conteggio righe inserite vs `len(INDICE_ARTICOLI)`, spot-check a campione di 2-3 `testo_integrale` contro il PDF ufficiale.
- Verifica manuale relazioni: query su `relazioni` per fonte, controllo a vista che `nodo_da_id`/`nodo_a_id` esistano davvero.
- Validazione umana finale invariata: coda di revisione in `web_ui.py`, bozza → validato, fonte per fonte dopo il seed.

## Fuori scope

- Riconciliazione eIDAS/eIDAS2 come due `fonti` separate (inconsistenza nota, documentata in CLAUDE.md, non toccata da questo lavoro).
- Migrazione incrementale delle validazioni pregresse (si riparte da zero, vedi sopra).
- Test automatizzati/CI (non presenti oggi, non richiesti da questo lavoro).
- Stratificazione di nuove fonti normative future sopra questo censimento: questo spec pone le basi (righe granulari collegabili), ma il lavoro di collegare una fonte futura non fa parte di questa passata.
