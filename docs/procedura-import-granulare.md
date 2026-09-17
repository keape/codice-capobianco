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

`inserisci_capitoli` esegue `verifica_copertura` automaticamente
sull'indice aggregato di tutti i capitoli **prima** di inserire qualunque
riga — se fallisce (item mancante o doppio), lo script si ferma con
l'elenco esatto, senza bisogno che l'agente rilegga e confronti a mano 600
voci di indice.

### 5. Seed e verifica finale

```bash
app/.venv/bin/python app/seed.py
```

Stessa procedura di verifica finale già in uso per eIDAS (conteggi
SQLite-in-memory/Neo4j combacianti, `stato_validazione='bozza'` su tutte le
nuove righe, coda di revisione UI).

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
