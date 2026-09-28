# Piano di import — lotto 1: atti di esecuzione eIDAS2 + standard ETSI mancanti

Creato 2026-09-28. Eseguito dalla sessione pi in autonomia, un import per
volta, con commit separato a ogni import chiuso.

Motivo del lotto: `docs/fonti-censite.md` documenta, import per import, le
citazioni a fonti non censite che ogni giro di Fase 6 (ADR-0009) ha dovuto
scartare "per assenza di nodo controparte". Aggregando quelle annotazioni
emerge che il censimento copre il testo di eIDAS2 ma **non il suo livello
operativo** (gli atti di esecuzione che nominano le norme di riferimento:
1 atto su oltre 30 adottati è censito, il Reg. 2025/1566) e non copre la
famiglia di standard ETSI più citata dai testi già nel grafo.

## 1. Perimetro del lotto

| # | Fonte | `fonte_id` | slug `app/seed_data/` | testo ufficiale | dim. stimata |
|---|---|---|---|---|---|
| 1 | Reg. di esecuzione (UE) 2025/1567 (29/7/2025) — dispositivi qualificati per la creazione a distanza di firma/sigillo come servizi fiduciari qualificati | **12** | `reg_ue_2025_1567` | CELEX `32025R1567` | ~9.700 car. |
| 2 | Reg. di esecuzione (UE) 2025/1569 (29/7/2025) — attestati elettronici qualificati di attributi (QEAA) e attestati di attributi da organismo del settore pubblico su fonte autentica | 22 | `reg_ue_2025_1569` | CELEX `32025R1569` | 28.500 car. di articolato (preambolo escluso): 53 nodi, 102 item |
| 3 | Reg. di esecuzione (UE) 2025/2531 (16/12/2025) — norme di riferimento e specifiche per i registri elettronici qualificati | 23 | `reg_ue_2025_2531` | CELEX `32025R2531` | ~22.200 car. |
| 4 | Reg. di esecuzione (UE) 2025/2532 (16/12/2025) — norme di riferimento e specifiche per i servizi di archiviazione elettronica qualificati | 24 | `reg_ue_2025_2532` | CELEX `32025R2532` | ~17.200 car. |
| 5 | ETSI TS 119 312 — Cryptographic Suites, **V2.1.1 (2026-06)** | 25 | `etsi_119_312` | `etsi_ts/119300_119399/119312/02.01.01_60/ts_119312v020101p.pdf` | da misurare |
| 6 | ETSI TS 119 101 — Policy and security requirements for applications for signature creation and signature validation, **V1.1.1 (2016-03)** (unica versione pubblicata) | 26 | `etsi_119_101` | `etsi_ts/119100_119199/119101/01.01.01_60/ts_119101v010101p.pdf` | da misurare |
| 7 | ETSI EN 319 102-1 — Procedures for Creation and Validation of AdES Digital Signatures, Parte 1: Creation and Validation, **V1.4.1 (2024-06)** | 27 | `etsi_319_102` | `etsi_en/319100_319199/31910201/01.04.01_60/en_31910201v010401p.pdf` | da misurare |

`fonte_id=12` è l'unico id libero nella tabella `fonti` (occupati: 1-11,
13-21; il 12 era la ex-Fonte "ETSI TS 119 431-2", consolidata nella 11 il
2026-09-23). Gli id successivi ripartono da 22.

**Fonte unica multi-parte**: ETSI EN 319 102 è un deliverable multi-parte.
Per il criterio già applicato a ETSI EN 319 412, TS 119 431 ed EN 319 411
("stessa normativa, stessa Fonte", con prefisso `"Parte N: "` nel
`riferimento`), la Fonte 27 nasce **coprendo la sola Parte 1** e la Parte 2
(TS 119 102-2, Signature Validation Report) si aggiungerà come incremento
successivo nella stessa Fonte — stesso percorso già seguito da ETSI EN 319 412
(Parte 5 prima, Parti 1-4 dopo).

## 2. Ordine di esecuzione

L'ordine è quello indicato dall'utente: 1567 → 1569 → 2531 → 2532 →
TS 119 312 → TS 119 101 → EN 319 102.

Criterio di fatto: prima gli atti eIDAS2 (che *nominano* gli standard), poi
gli standard nominati. Un atto di esecuzione censito prima rende la Fase 6
degli standard ETSI molto più produttiva: le relazioni "richiama"/
"specifica" verso l'atto si generano da citazione letterale, non da KNN.

## 3. Regole invarianti (non negoziabili in nessun import del lotto)

Derivano dalla skill `import-fonte-normativa` e non vanno ri-derivate:
ADR-0007 (un nodo per articolo/comma/clausola, nessun discrimine di
rilevanza, incluse scopo/ambito e definizioni); ADR-0010 (nessun
`testo_integrale` troncato o eliso — guardia bloccante in
`inserisci_capitoli`); ADR-0009 (Fase 6 obbligatoria contro **tutte** le
fonti già nel grafo, esito riportato anche quando è zero); ADR-0011 (MCP
solo per ispezione, la scrittura passa da `seed.py`).

## 4. Passi per ogni import

1. **Fetch** del testo ufficiale una volta sola:
   - atti UE: `app/.venv/bin/python app/tools/cellar_fetch.py <CELEX> <slug>` →
     `app/.source_cache/<slug>/raw.txt` in italiano (XHTML ufficiale del
     CELLAR, `Accept-Language: ita`) + `provenance.json` (URL risolto,
     lingua, data, sha256).
   - standard ETSI: PDF da `etsi.org/deliver/…` con **User-Agent browser**
     (senza, il sito risponde 403 a una richiesta non interattiva). La
     versione corrente non va indovinata: il percorso si risolve leggendo il
     listing della famiglia (`https://www.etsi.org/deliver/etsi_ts/<range>/<num>/`,
     che elenca le sottocartelle di versione) e prendendo la piu' recente per
     data. Verificato il 2026-09-28: TS 119 312 e' alla **V2.1.1 (2026-06)**,
     non alla V1.4.1 citata dagli altri standard censiti; TS 119 101 ha come
     **unica** versione pubblicata la V1.1.1 (2016-03); EN 319 102-1 e' alla
     V1.4.1 (2024-06). Poi `pdftotext -layout` → `raw.txt`.
   - Il testo non viene mai incollato inline nei prompt: si passa
     `local://<testo_path>`.
2. **Split** se il documento è troppo grande per una sola sessione:
   `boundaries.json` + `app/tools/split_source.py`. Gli atti 1567, 2531,
   2532 stanno in un capitolo unico (precedente Reg. 2025/1566: atto breve
   estratto direttamente in sessione principale, nessun subagent). 1569 e
   gli standard ETSI si dividono in capitoli se il testo supera ~25k car.
3. **Modulo capitolo** `app/seed_data/<slug>/capNN.py` con
   `RIGHE_OBBLIGHI`/`RIGHE_PRINCIPI`/`INDICE_ARTICOLI_LOCALE`/
   `MAPPATURA_LOCALE`/`RELAZIONI` secondo il contratto di
   `app/seed_data/lib.py` (id risolti per riferimento dal registro, mai
   assegnati a mano).
4. **Wiring** in `app/seed.py`: riga in `fonti` + blocco
   `seed_lib.inserisci_capitoli(...)` con la numerazione definitiva cablata
   dalla sessione principale (i moduli capitolo non toccano mai `seed.py`).
5. **Seed e verifica**: `app/.venv/bin/python app/seed.py`;
   `app/.venv/bin/python app/tools/verifica_troncamento.py --fonte-id <N>`;
   controllo che tutte le nuove righe siano `stato_validazione='bozza'`.
6. **Fase 6** (ADR-0009): grep delle citazioni esplicite su `raw.txt` + KNN
   sui nodi delle altre Fonti (soglia 0.85), classificazione solo sullo
   shortlist, validazione anti-allucinazione dei `riferimento` proposti
   contro Neo4j, inserimento come modulo "capitolo virtuale" (solo
   `RELAZIONI`, con `evidence_type`/`confidence` valorizzati).
   **Modifica di procedura emersa con la Fonte 22**: lo stadio 1 si esegue con
   `app/tools/fase6_candidati_knn.py`, che calcola al volo l'embedding dei nodi
   nuovi (stesso modello e stesso campo `testo` di `app/embed_neo4j.py`) e li
   interroga contro l'indice HNSW già popolato. Così la Fase 6 gira **prima**
   del seed e serve un solo lancio di `app/seed.py` per import (i moduli
   `fase6_candidati_431/432/612.py` precedenti lavoravano sugli embedding già
   in Neo4j e imponevano due seed). Vale per gli import successivi del lotto.
7. **Documentazione**: voce in `docs/fonti-censite.md` (categoria corretta,
   `fonte_id`, moduli, conteggi, esito Fase 6) e aggiornamento della
   checklist §6 di questo piano. Commit `Import granulare <fonte>`.

### Adattamento di harness (solo per lo stadio 2 della Fase 6)

`docs/adr/0009` descrive la classificazione come chiamate `completion()`
dirette in parallelo con `wait()` dentro sessioni Claude Code. In sessione pi
lo stadio 2 è eseguito **inline dall'agente** (che è l'LLM) con lo stesso
schema di prompt e output JSON dell'ADR, per lo stesso motivo per cui l'ADR
esclude i subagent: su shortlist di decine di coppie l'overhead di dispatch
supera il beneficio. Resta invariata la separazione: prefiltro a zero token
LLM, classificazione **solo** sullo shortlist, mai sul prodotto cartesiano
fonte×fonte. Nessun'altra fase cambia.

## 5. Criteri di modellazione specifici degli atti di esecuzione

Mutuali dal precedente Reg. 2025/1566 (`app/seed_data/reg_ue_2025_1566/cap01.py`),
che è il modello di riferimento per una fonte di questo tipo:

- **Articolo di mero rinvio** ("le norme di riferimento figurano
  nell'allegato") → Principio, `tipo_principio` "altro": non è definitorio
  né di scopo/ambito, e la tassonomia non ha un tipo dedicato.
- **Entrata in vigore** e **applicazione differita** → due nodi distinti
  (sono fatti giuridici con effetti diversi, spazio temporale di vigenza
  diverso); entrambi Principio "altro".
- **Formula di chiusura** ("obbligatorio in tutti i suoi elementi e
  direttamente applicabile") → nessun nodo: elemento di formattazione
  dell'atto, non un comma.
- **Allegato**: una riga per ogni punto con identità e contenuto proprio
  (come i 6 punti di adeguamento del 1566, con requisito/id citato nel
  `riferimento`). Un allegato che sia **elenco puramente enumerativo** di
  norme di riferimento, senza prescrizione autonoma per voce, riceve
  **una sola riga**, con ogni voce indicizzata separatamente in
  `INDICE_ARTICOLI_LOCALE`/`MAPPATURA_LOCALE` — stesso trattamento già
  riservato alle liste definitorie (art. 3 eIDAS).
- **Soggetto obbligato**: distinzione già in uso fra `QTSP/gestore` (il
  prestatore) e `Terza parte` (organismo di valutazione della conformità,
  laboratorio accreditato, autorità nazionale competente): la seconda è
  frequente in questi atti e non va forzata nella prima.
- **Citazioni testuali** di articoli eIDAS2 o di clausole ETSI già nel grafo
  → relazione nativa in fase 3 (non differita a Fase 6), con
  `evidence_type='textual'`.

## 6. Checklist di avanzamento

| # | Fonte | `fonte_id` | fetch | estrazione | seed | Fase 6 | docs+cross | commit |
|---|---|---|---|---|---|---|---|---|
| 1 | Reg. 2025/1567 | 12 | ☑ | ☑ | ☑ | ☑ 8 rel. | ☑ | ☑ |
| 2 | Reg. 2025/1569 | 22 | ☑ | ☑ 3 cap. | ☑ | ☑ 4 rel. | ☑ | ☑ |
| 3 | Reg. 2025/2531 | 23 | ☑ | ☑ 1 cap. | ☑ | ☑ 3 rel. | ☑ | ☑ |
| 4 | Reg. 2025/2532 | 24 | ☑ | ☑ 1 cap. | ☑ | ☑ 3 rel. | ☑ | ☑ |
| 5 | ETSI TS 119 312 | 25 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 6 | ETSI TS 119 101 | 26 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| 7 | ETSI EN 319 102-1 | 27 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |

## 7. Fuori perimetro di questo lotto (backlog, non eseguito)

Elencato per non perderlo, non come lavoro in corso:

- **NIS2**: direttiva (UE) 2022/2555, D.Lgs. 138/2024 (recepimento italiano,
  ACN autorità competente), regolamento di esecuzione (UE) 2024/2690
  (requisiti tecnico-metodologici e incidenti significativi, con i
  prestatori di servizi fiduciari espressamente in ambito).
- **Altri atti di esecuzione eIDAS2**: Reg. 2025/1567-bis e successivi —
  QTSP (art. 24 §5), convalida (artt. 32 §3, 40), certificati qualificati
  (artt. 28 §6, 38 §6), QWAC (art. 45 §2), formati AdES (artt. 27 §5, 37 §5),
  registri/archivi qualificati, notifica servizi (art. 21 §4), onboarding
  remoto (Reg. 2026/798), modifica protocolli/trust framework
  (Reg. 2026/1731). 1567/1569/2531/2532 sono il primo sottoinsieme.
  Aggiunto durante l'import di 1569 (2026-09-28): **Reg. di esecuzione (UE)
  2024/2979** (integrità e funzionalità di base dei portafogli europei di
  identità digitale), citato testualmente nell'allegato II punto 1 di 1569
  come sede dei formati ammessi per gli attestati — quindi non un atto di
  contorno ma una norma di riferimento richiamata da un atto già censito.
  Aggiunti durante gli import di 2531 e 2532 (2026-09-28), tutti richiamati
  come norme di riferimento dagli allegati di quegli atti e quindi rilevanti
  per chi eroga registri elettronici o archiviazione qualificata:
  **CEN/TS 18170:2025** (norma CEN su cui poggia l'intero allegato di 2532:
  è l'unico caso del lotto in cui la fonte portante non è ETSI — il
  censimento oggi non ha nessuna fonte CEN); **regg. di esecuzione (UE)
  2024/482 e 2024/3144** (sistema europeo di certificazione della
  cibersicurezza basato sui criteri comuni, EUCC); **ISO 14721:2025** (OAIS),
  **ISO 23257:2022** e **ISO/TS 23635:2022** (blockchain/DLT); **IETF RFC
  7515** (JWS); **FIPS PUB 140-3**; **ISO/IEC 15408:2022**; il documento
  ENISA «Agreed Cryptographic Mechanisms» del gruppo ECCG.
- **eIDAS1 di cornice**: CID (UE) 2015/1505 (trusted list), CID (UE)
  2015/1506 (formati firme/sigilli riconosciuti dalla PA), CID (UE) 2016/650
  (standard di valutazione di sicurezza dei QSCD).
- **Standard ETSI**: EN/TS 319 403 (conformity assessment), EN 319 102-1
  Parte 2 e TS 119 102-2, TS 119 615, TS 119 172-1…-4, TS 119 511/512
  (preservation), EN 319 521/522 (ERDS), EN 319 532 (REM), EN 419 241-1/-2
  (server signing), famiglia AdES baseline (EN 319 122-1 CAdES, 132-1 XAdES,
  142-1 PAdES, 162-1 ASiC, TS 119 182-1 JAdES), TS 119 495 (PSD2).
- **Nazionale**: Linee guida AgID su formazione, gestione e conservazione dei
  documenti informatici (art. 71 CAD); regole tecniche PEC; verifica dello
  stato di vigenza residua di DPCM 3/12/2013 e DPCM 13/11/2014.
- **Dati e sicurezza**: Reg. (UE) 2016/679 (GDPR); DORA (2022/2554) e CRA
  (2024/2847) da valutare in base al perimetro dei servizi.

## 8. Angolo morto noto

Gli atti del lotto sono recenti e in movimento (il Reg. 2026/1731 modifica
tre atti già adottati). Il grafo non ha un ciclo di riverifica: una volta
seedata, una Fonte resta ferma finché non la si aggiorna a mano. Dopo questo
lotto vale la pena verificare se il meccanismo `modifiche_rilevate` (ticket
05) copre anche le Fonti normative e non solo gli obblighi, altrimenti gli
atti di esecuzione sono la prima categoria di Fonti che invecchia male.
