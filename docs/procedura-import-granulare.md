# Procedura import granulare per fonte (CAD, DPCM)

Sostituisce, per le prossime fonti (CAD, poi DPCM), il modo in cui è stato
condotto l'import granulare eIDAS/eIDAS2 del 2026-09-15. Vedi
`docs/runbook-neo4j-import.md` per i problemi infrastrutturali noti (da
tenere separati da questa procedura, mai diagnosticati dentro la stessa
sessione di estrazione).

## Perché è cambiata

L'import eIDAS ha richiesto due sessioni interattive intere (limite delle 5
ore raggiunto due volte) per: 460 righe nuove su 7 subagent per capitolo.
Tre cause strutturali, ora rimosse dagli strumenti sotto:

1. Ogni subagent riceveva il testo ufficiale incollato inline nel prompt →
   duplicazione del contesto normativo per ogni subagent.
2. Due subagent hanno scritto sullo stesso file di output (nessuna
   assegnazione di path precedente al dispatch) → lavoro perso e rifatto.
3. Ogni riga porta un id intero assegnato a mano con range globali
   concordati a priori tra fonti/capitoli → fragile, impossibile da
   garantire con autoria parallela.

## Passi

### 1. Fetch del testo ufficiale (una volta sola, sessione principale)

Leggere il testo ufficiale con lo strumento `read` sull'URL Normattiva/EUR-Lex
(già presente nel blocco `fonti` di `app/seed.py` per la fonte in questione),
poi salvarlo con `write` in:

```
app/.source_cache/<fonte>/raw.txt
```

(`<fonte>` = slug minuscolo, es. `cad`, `dpcm`). Cartella gitignorata — non
finisce in nessun commit.

### 2. Split deterministico in capitoli

Decidere la suddivisione in capitoli/sezioni (stesso criterio già usato per
eIDAS: un capitolo ≈ un Titolo/Capo del testo, dimensione tale da stare
comodamente nel contesto di un singolo subagent). Scrivere
`boundaries.json` con marker letterali in ordine di comparizione nel testo,
poi:

```bash
app/.venv/bin/python app/tools/split_source.py <fonte> app/.source_cache/<fonte>/raw.txt boundaries.json
```

Produce `app/.source_cache/<fonte>/cap0N.txt` (porzione di testo per
capitolo) e `app/.source_cache/<fonte>/manifest.json` (con `testo_path` e
`modulo_path` già assegnati per ciascun capitolo — vedi
`app/tools/split_source.py` per il formato).

### 2-bis. Lingua dei riferimenti e delle citazioni (regola di valorizzazione)

Il censimento tiene i `riferimento` in **forma italiana convenzionale e omogenea**
(`clausola 5.4.2 (titolo)`, `Annex A, clausola A.1.1`, `art. 5 bis §4(a)`, `allegato IV,
sezione IV.3`), anche quando il testo ufficiale è in inglese: serve a rendere confrontabili
fonti diverse e a far funzionare il registro del seed e le partizioni (ADR-0012).

Il **testo citante**, invece, nomina il bersaglio nella lingua che gli è propria: gli
standard ETSI scrivono "clause 5.4.2", "see Annex A", "as defined in 5.2.2"; gli atti UE
scrivono "l'articolo 13, paragrafo 2". **Un rinvio fra testi in lingue diverse è una
relazione legittima**, non un'etichetta gonfiata: `evidence_type="textual"` resta corretto
quando la citazione è letterale nella lingua del testo, e l'audit
`app/tools/verifica_relazioni_textual.py` accetta come traccia sia la forma italiana sia
quella inglese (singolare e plurale), la numerazione nuda multi-segmento e, negli annessi
tecnici, gli id ASN.1 e i nomi di tipo. Decisione presa con l'utente il 2026-09-29.

Conseguenza operativa per chi scrive un modulo: non tradurre il riferimento del bersaglio
per "farlo combaciare" con la lingua del testo citante, e non rinunciare alla relazione
solo perché le due lingue differiscono.

### 3. Dispatch dei subagent per capitolo

Un `task` per capitolo, in batch unico. Nel prompt di ciascuno, passare
**solo**:
- `local://<testo_path>` del manifest (mai testo incollato inline);
- il `modulo_path` del manifest come unico file da scrivere (path già
  assegnato, il subagent non lo sceglie);
- la forma dict esatta attesa, copiata dalla docstring di
  `app/seed_data/lib.py` (RIGHE_OBBLIGHI, RIGHE_PRINCIPI,
  INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE, RELAZIONI);
- il criterio ADR-0007 (copertura completa, un nodo per disposizione, nessun
  discrimine di rilevanza) e il perimetro/le categorie Obbligo/Principio
  applicabili;
- se la fonte rinvia ad un'altra fonte già importata (es. CAD → eIDAS), il
  `fonte_id` di quella fonte e l'elenco dei `riferimento` rilevanti per le
  relazioni cross-fonte (`RELAZIONI` con `fonte_da`/`fonte_a` espliciti,
  vedi docstring `lib.py`).

Concorrenza: partire da 3-4 paralleli, non 7 — se non si osserva rate limit
del provider, aumentare nel batch successivo; se si osserva, il redispatch
riguarda solo il/i capitoli falliti (già isolati per file, nessun impatto
sugli altri).

### 3-bis. Granularità fine: ogni voce enumerata con precetto è una riga

Decisione dell'utente, 2026-09-29, valida per **tutte** le Fonti:

> ogni voce enumerata che porta una prescrizione ha una riga propria — passi `1)` `2)` `3)`…,
> lettere `a)` `b)` `c)`…, qualifier, elenchi indicizzati — **anche quando il documento non la
> richiama per numero altrove**. Restano nella riga della clausola/comma solo le intestazioni
> di puro raggruppamento e le parti non prescrittive (elenchi di documenti, tabelle
> informative, rubriche).

**Perché**: l'obiettivo del censimento è sapere *quale singolo aspetto* di un requisito è
prescritto, così da poterlo collegare a un obbligo esterno e da poter dire quale aspetto è
stato violato. Una clausola intera non lo permette.

**Come si applica nel prompt del worker**: va scritta come regola, senza la condizione
"dove il documento la numera e la richiama altrove" — quella clausola ha prodotto, il
2026-09-29, due moduli di XAdES con i passi numerati dentro la riga della sottoclausta,
difformi dal resto della stessa Fonte. Un esempio da citare ai worker: `app/seed_data/etsi_319_122/cap04.py`
(clausola 6.3 di CAdES: una riga per ciascuno dei venti requisiti a)-t)).

**Costo dichiarato**: più nodi (indicativamente +10-20% sulle fonti che enumerano molto) e
quindi più righe in coda di validazione umana. È il prezzo scelto per avere il dettaglio.

Elenca le Fonti già censite su cui la regola non è stata applicata, con la misura dei nodi
candidati e il metodo di decisione: `docs/plan-retrofit-regole-import.md` § 3.1.

### 4. Merge e verifica di copertura (script, non lettura manuale)

Ogni capitolo produce un modulo Python indipendente
(`app/seed_data/<fonte>/cap0N.py`). Wiring in `app/seed.py`, dove oggi c'è
il blocco inline della fonte da sostituire:

```python
from seed_data import lib as seed_lib
from seed_data.cad import cap01, cap02, cap03  # ordine = ordine del manifest

registro = {}  # o il registro cross-fonte già popolato dalle fonti precedenti
lookup = seed_lib.costruisci_lookup(conn)
seed_lib.inserisci_capitoli(cursor, fonte_id=3, capitoli=[cap01, cap02, cap03],
                             lookup=lookup, registro=registro)
```

`inserisci_capitoli` esegue `verifica_copertura` e
`verifica_completezza_testo_integrale` automaticamente sull'indice/sulle
righe aggregate di tutti i capitoli **prima** di inserire qualunque riga —
se `verifica_copertura` fallisce (item mancante o doppio) o se
`verifica_completezza_testo_integrale` fallisce (un `testo_integrale`
contiene un marcatore di elisione `...`/`…`/`[...]`, segno di
troncamento in estrazione — vedi ADR-0010), lo script si ferma con
l'elenco esatto, senza bisogno che l'agente rilegga e confronti a mano
centinaia di righe o di caratteri.

Per la ricognizione prima di arrivare a quel punto — capire dove guardare
prima di lanciare lo script — l'agente ha a disposizione il canale MCP in
sola lettura (ADR-0011): `read-cypher` permette di contare i nodi di una
fonte, elencare i riferimenti già presenti per un capitolo, o cercare
marcatori di elisione in `testo_integrale`, senza scrivere uno script Python
e senza passare dal venv. Resta uno strumento di **ispezione**: la verifica
che blocca il merge è `inserisci_capitoli` (e, a posteriori,
`app/tools/verifica_troncamento.py`), non una query MCP.

### 5. Seed e verifica finale

```bash
app/.venv/bin/python app/seed.py
```

Stessa procedura di verifica finale già in uso per eIDAS (conteggi
SQLite-in-memory/Neo4j combacianti, `stato_validazione='bozza'` su tutte le
nuove righe, coda di revisione UI).

Controllo aggiuntivo, riusabile anche fuori da un seed (es. dopo una
correzione manuale via Cypher, o come audit periodico su fonti già
seedate prima dell'introduzione della guardia in ADR-0010):

```bash
app/.venv/bin/python app/tools/verifica_troncamento.py [--fonte-id N]
```

Con il canale MCP di ADR-0011 lo stesso audit si può lanciare come query di
ricognizione in `read-cypher` (cercare `...`/`…`/`[...]` nei
`testo_integrale` di una fonte) prima di eseguire lo script: l'esito
autorevole resta quello dello script, che importa la stessa normalizzazione
di `seed_data.lib` e quindi conosce le convenzioni in cui un'ellissi è
contenuto autentico del testo ufficiale.

### 6. Collegamento cross-fonte a posteriori (opzionale, fonte già importata)

Se al passo 3 non sono state costruite relazioni cross-fonte (caso comune:
i subagent per capitolo sono stati istruiti a evitarle per non rischiare
`KeyError` su `riferimento` di un'altra fonte non ancora verificati durante
un merge parallelo), la fonte appena importata resta un'isola nel grafo
finché non si esegue un giro dedicato. Procedura completa — prefiltro
economico (grep + KNN vettoriale, zero token LLM) seguito da
classificazione LLM solo sullo shortlist risultante, mai sul prodotto
cartesiano fonte×fonte — in `docs/adr/0009-collegamento-cross-fonte-a-posteriori.md`.
Esito di riferimento: import CAD, 594 nodi, shortlist di 293 coppie
candidate (non 245.000), 53 relazioni finali verso eIDAS/eIDAS2.

Output: un modulo "capitolo virtuale" (`RIGHE_OBBLIGHI`/`RIGHE_PRINCIPI`/
`INDICE_ARTICOLI_LOCALE`/`MAPPATURA_LOCALE` vuoti, solo `RELAZIONI` con
`nodo_a`/`nodo_da` a fonte esplicita — vedi `app/seed_data/cad/cap08_relazioni_eidas.py`
per un esempio completo), agganciato in coda alla lista `capitoli` passata
a `inserisci_capitoli` nel wiring di `seed.py`.

### 7. Aggiornamento di `docs/fonti-censite.md` (obbligatorio, non opzionale)

Ultimo passo di ogni import, eseguito solo dopo che il passo 6 ha un esito
verificato (anche "zero relazioni trovate" è un esito valido, purché
riportato esplicitamente). Aggiungere la Fonte appena importata alla
categoria corretta (fonti internazionali / fonti nazionali / fonti locali /
standard tecnici) in `docs/fonti-censite.md`, con `fonte_id`, moduli
`app/seed_data/<fonte>/` coinvolti, conteggio nodi/relazioni interne e esito
del collegamento cross-fonte — stesso livello di dettaglio delle voci già
presenti. Non aggiungere l'elenco delle Fonti a `CLAUDE.md`: quel file
rimanda a `docs/fonti-censite.md` apposta per non crescere ad ogni import.
Un import non è completo finché questo passo non è stato eseguito, sullo
stesso principio del passo 6 (un nodo/una fonte non collegata o non
documentata è un'isola, anche se tecnicamente presente nel grafo).
