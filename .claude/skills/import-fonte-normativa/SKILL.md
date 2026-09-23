---
name: import-fonte-normativa
description: >
  Guida il processo di import granulare di una nuova fonte normativa, o di un nuovo
  capitolo/articolo aggiunto a una fonte già censita, nel censimento a grafo
  codice-capobianco (Neo4j). Use quando l'utente chiede di importare/censire una
  nuova fonte normativa (es. "importa il DPCM", "censisci una nuova fonte",
  "aggiungi capitolo a fonte esistente"), o di creare/verificare relazioni
  tipizzate tra obblighi/principi in fase di estrazione. Impone: copertura
  completa per articolo/comma (nessun discrimine di rilevanza, ADR-0007),
  completezza verbatim del testo di ogni singolo nodo (mai un `testo_integrale`
  troncato/elisо con `...`/`…`/`[...]`, ADR-0010) e collegamento a posteriori
  con TUTTE le fonti già presenti nel grafo come passo finale obbligatorio,
  non opzionale — un import non è completo se i nodi restano un'isola
  scollegata dal resto del censimento o se il loro testo è mutilato.
user-invocable: true
---

# Import granulare di una fonte normativa

Riferimenti canonici (leggere prima di agire, non duplicati qui):
- `docs/procedura-import-granulare.md` — rationale e procedura passo-passo completa
- `docs/runbook-neo4j-import.md` — problemi infrastrutturali noti (driver `neo4j`,
  Neo4j Desktop non responsivo); **mai diagnosticare nella stessa sessione
  di estrazione**, isolare in una sessione/subagent dedicato all'infra
- `docs/adr/0007-copertura-completa-articoli-nessun-discrimine-di-inclusione.md` —
  criterio di copertura (un nodo per articolo/comma, incluse disposizioni di
  scopo/ambito/definizioni)
- `docs/adr/0010-completezza-verbatim-testo-integrale.md` — criterio di
  completezza *dentro* ogni nodo (mai testo troncato/eliso), guardia
  bloccante in `inserisci_capitoli` + audit riusabile
  `app/tools/verifica_troncamento.py`
- `docs/adr/0009-collegamento-cross-fonte-a-posteriori.md` — pipeline di
  collegamento (fase 6 sotto, letta per intero prima di eseguirla)
- `app/seed_data/lib.py` — contratto dati esatto di un modulo capitolo
  (`RIGHE_OBBLIGHI`/`RIGHE_PRINCIPI`/`INDICE_ARTICOLI_LOCALE`/`MAPPATURA_LOCALE`/`RELAZIONI`),
  `verifica_copertura`, `inserisci_capitoli`
- `app/neo4j_common.py` — `TIPO_RELAZIONE_TO_ARCO` (14 tipi di relazione),
  `DIRETTEZZA_PESO`
- `CONTEXT.md` — tassonomia dei 14 tipi di relazione con descrizione, e le
  due categorie Obbligo/Principio

## Fasi 1-5 (import della fonte, in sintesi — dettagli in `procedura-import-granulare.md`)

1. **Fetch testo ufficiale** una volta sola nella sessione principale, salvato
   in `app/.source_cache/<fonte>/raw.txt` (mai incollato inline nei prompt subagent).
2. **Split deterministico**: `app/tools/split_source.py <fonte> raw.txt boundaries.json`
   → assegna centralmente `testo_path`/`modulo_path` per capitolo prima del dispatch.
3. **Dispatch subagent per capitolo**, un `task` a testa in batch unico (3-4
   paralleli per partire). Ogni subagent riceve solo `local://<testo_path>`,
   il proprio `modulo_path` (già assegnato, non a sua scelta), la forma dict
   esatta da `app/seed_data/lib.py`, il criterio ADR-0007. **Istruire
   esplicitamente a NON tentare relazioni cross-fonte in questa fase** — causa
   nota di `KeyError` su merge parallelo; sempre e solo in fase 6.
4. **Merge**: wiring in `app/seed.py` via `seed_lib.inserisci_capitoli(...)`,
   che esegue `verifica_copertura` (copertura per articolo, ADR-0007) e
   `verifica_completezza_testo_integrale` (nessun `testo_integrale` troncato,
   ADR-0010) sull'indice/sulle righe aggregate prima di inserire qualunque
   riga — se fallisce, elenco esatto degli item mancanti/doppi o dei
   riferimenti con testo eliso.
5. **Seed e verifica**: `app/.venv/bin/python app/seed.py`, controllo conteggi
   e `stato_validazione='bozza'` su tutte le nuove righe.

## Fase 6 — Collegamento con le fonti già censite (OBBLIGATORIA)

Un import termina solo dopo questa fase. Non chiedere conferma per saltarla:
se l'utente non specifica altrimenti, eseguirla sempre, contro **ogni** fonte
già presente nel grafo (non solo quella "più ovvia" — es. importando DPCM,
verificare sia contro eIDAS/eIDAS2 sia contro CAD, non solo una delle due).
Se il risultato è zero relazioni trovate, riportarlo esplicitamente come esito
verificato, non come fase saltata.

Pipeline (3 stadi, eseguita nella sessione principale, mai a subagent —
dettagli completi in ADR-0009):

1. **Candidati, zero token LLM**: grep testuale su `app/.source_cache/<fonte>/raw.txt`
   per citazioni esplicite di altre fonti, risolto contro `testo_integrale` in
   Neo4j per ottenere il `riferimento` esatto; più KNN sull'indice vettoriale
   HNSW già popolato (`idxEmbeddingObbligo`/`idxEmbeddingPrincipio`), soglia
   score ~0.80. Unione dei due insiemi.
2. **Classificazione LLM solo sullo shortlist**: mai sul prodotto cartesiano
   fonte×fonte. Chiamate `completion()` dirette in batch (~10 nodi), eseguite
   in parallelo con `wait()` — non subagent, l'overhead di dispatch supera il
   beneficio su shortlist già piccoli. Ogni batch riceve solo `riferimento`+testo
   sintetico (mai `testo_integrale` o testo ufficiale grezzo per intero), system
   prompt con la tassonomia di `CONTEXT.md` ristretta ai tipi rilevanti, output
   a schema JSON, prompt esplicitamente conservativo (omettere piuttosto che
   inventare).
3. **Validazione e inserimento**: filtro `confidence` minima (~0.5; evidenza
   testuale esplicita tipicamente ≥0.7), verifica che ogni `riferimento`
   proposto esista davvero in Neo4j (anti-allucinazione), poi scrittura come
   modulo "capitolo virtuale" — `RIGHE_OBBLIGHI`/`RIGHE_PRINCIPI`/
   `INDICE_ARTICOLI_LOCALE`/`MAPPATURA_LOCALE` vuoti, solo `RELAZIONI` con
   `nodo_da`/`nodo_a` a fonte esplicita (`fonte_id_o_None` non-None per la
   fonte controparte) — vedi `app/seed_data/cad/cap08_relazioni_eidas.py`
   come esempio completo, incluso il docstring che documenta la pipeline
   usata per rigenerarlo. Agganciare in coda alla lista `capitoli` passata a
   `inserisci_capitoli` nel wiring di `seed.py`.

Ogni relazione inserita porta `evidence_type`/`confidence` per-arco (ADR-0005)
— mai `NULL` per default, mai inventata se lo score non la giustifica.

## Guardie

- Mai relazioni cross-fonte durante il dispatch per capitolo (fase 3).
- Mai testo ufficiale completo incollato inline in un prompt subagent.
- Mai path di output scelto dal subagent — sempre assegnato prima del dispatch.
- Problemi infrastrutturali (driver Neo4j, connessione) → sessione dedicata,
  mai dentro la sessione di estrazione/collegamento.
- Import non completo finché la fase 6 non è stata eseguita e il suo esito
  (N relazioni inserite, per tipo) riportato all'utente.
- Mai un `testo_integrale` con marcatore di elisione (`...`/`…`/`[...]`) —
  bloccato in automatico da `inserisci_capitoli` (ADR-0010); se emerge fuori
  da un seed (es. correzione manuale via Cypher), rilanciare
  `app/tools/verifica_troncamento.py` per confermare l'assenza di altre
  troncature prima di considerare il dato affidabile.
