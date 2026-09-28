# Fonti censite

Elenco delle Fonti presenti nel grafo, raggruppate per categoria logica
anziché per ordine cronologico di import. Referenziato da `CLAUDE.md`
(che non elenca le singole Fonti per evitare di crescere indefinitamente ad
ogni import) e dalla skill `import-fonte-normativa`.

Ogni voce riporta `fonte_id` (colonna `fonti.id` in Neo4j), stato di
copertura, e riferimento al modulo/ai moduli `app/seed_data/<fonte>/` che la
importano. "Copertura granulare completa" = ADR-0007 (un nodo per
articolo/comma/clausola, nessun discrimine di rilevanza) + ADR-0010
(nessun troncamento verbatim in `testo_integrale`). "Cross-collegata" =
almeno un giro di Fase 6 (ADR-0009) eseguito, con esito riportato
esplicitamente nel commento di wiring in `app/seed.py` anche quando zero
relazioni sono emerse.

Aggiornare questo file, non `CLAUDE.md`, ad ogni nuovo import — vedi
`docs/procedura-import-granulare.md` § 6.

## 1. Fonti internazionali

Regolamenti UE direttamente applicabili (nessun atto di recepimento
nazionale necessario).

- **eIDAS** — Regolamento (UE) n. 910/2014. `fonte_id=1`. Import storico
  (2026-09-15), pre-ADR-0007 su parte del testo, poi esteso a copertura
  granulare completa. Modellato come Fonte separata da eIDAS2 (vedi nota
  "Inconsistenza nota" in `CLAUDE.md` — divergenza dichiarata rispetto a
  `CONTEXT.md`, non ancora riconciliata con l'utente).
- **eIDAS2** — Regolamento (UE) 2024/1183, modifica di eIDAS. `fonte_id=2`.
  Stesso import storico di eIDAS, Fonte separata.
- **Regolamento di esecuzione (UE) 2025/1566** — modalità di applicazione
  dell'art. 24 §1-quater eIDAS2 sulle norme di riferimento per la verifica
  identità/attributi ai fini di un certificato qualificato o QEAA.
  `fonte_id=8`. Import 2026-09-21/22, 1 capitolo
  (`app/seed_data/reg_ue_2025_1566/cap01.py`). 3 relazioni native + 3 cross
  verso eIDAS/eIDAS2 dopo pipeline grep+KNN+LLM (116 coppie candidate)
  — modulo `cap02_relazioni_cross.py`.
- **Regolamento di esecuzione (UE) 2025/1567** — modalità di applicazione
del regolamento (UE) n.910/2014 per quanto riguarda la gestione di
dispositivi qualificati per la creazione di una firma elettronica a
distanza e di dispositivi qualificati per la creazione di un sigillo
elettronico a distanza come servizi fiduciari qualificati (art. 29 bis §2
e art. 39 bis eIDAS2). `fonte_id=12`. Import 2026-09-28, testo ufficiale
italiano acquisito con `app/tools/cellar_fetch.py` (CELEX `32025R1567`,
provenienza e sha256 in `app/.source_cache/reg_ue_2025_1567/`), un solo
capitolo (`app/seed_data/reg_ue_2025_1567/cap01.py` + capitolo virtuale di
Fase 6 `cap02_relazioni_cross.py`). Atto breve (2 articoli + allegato di 7
punti di adeguamento a ETSI TS 119 431-1 V1.3.1): 14 nodi (9 obblighi, 5
principi), 14 item di indice — un nodo per articolo/comma e **per ogni
requirement id introdotto dall'atto** (OVR-6.1-04, OVR-6.4.4-02/-03,
OVR-6.4.9-02, OVR-6.5.5-02/-03, OVR-6.8.5-01/-02, OVR-A.3-02), esclusa la
sola formula di chiusura dell'art. 2 comma 3. **20 relazioni**: 12 native
(2 "attua" verso eIDAS2 artt. 29 bis §2 e 39 bis; 7 "modifica" verso i
requisiti delle clausole che l'atto integra in ETSI TS 119 431-1; 1
"specifica" verso la sua clausola 1; 2 "richiama" verso eIDAS2 art. 24 §5 ed
ETSI EN 319 401 REQ-7.8-13) + 8 dal giro Fase 6 (7 "si sovrappone a" — i
requisiti di ETSI EN 319 401 tradotti nella norma, la formula di
pubblicazione internazionale di ETSI EN 319 411-1 `DIS-6.1-08` e l'obbligo
sul piano di cessazione già presente nel Reg. 2025/1566 — e 1 "specifica"
verso la clausola A.2 di ETSI TS 119 431-1, policy EUSPv2). `fonte_id=12`
era l'unico id libero della tabella `fonti` (ex-Fonte "ETSI TS 119 431-2",
consolidata nella 11 il 2026-09-23). **Limite noto**: l'atto designa ETSI EN
319 401 V3.1.1 (2024-06), mentre la Fonte 10 censita è la V3.2.1 (2026-01);
le relazioni della Fase 6 verso quella Fonte vanno riverificate insieme ad
essa, non separatamente. 4 dei 14 nodi restano senza archi tipizzati oltre
`DA_FONTE` (art. 2 «entrata in vigore» e «applicazione», l'aggiunta
bibliografica di cui al punto 1 dell'allegato e il punto 6 OVR-6.8.5-02 sul
rinvio ai meccanismi crittografici ENISA, documento non censito): nessuno è
un'isola quanto a `DA_FONTE`, e le relazioni "entrata in vigore" ↔ "entrata
in vigore" proposte dal KNN a score 1.0 sono state scartate come nel giro
Fase 6 del Reg. 2025/1566.
- **Regolamento di esecuzione (UE) 2015/1502** — specifiche/procedure
  tecniche minime sui livelli di garanzia (basso/significativo/elevato) dei
  mezzi di identificazione elettronica, ex art. 8 §3 eIDAS. `fonte_id=14`.
  Import 2026-09-22/23, 3 capitoli (`app/seed_data/reg_ue_2015_1502/`),
  29 nodi (18 obblighi, 11 principi). Fase 6 in due passaggi: 2 relazioni
  native corrette (omesse per errore nell'estrazione originaria) + 7
  relazioni da pipeline grep+KNN+LLM (704 candidati) verso DPCM 19/10/2021,
  Regolamento AgID modalità attuative SPID e 2 standard ETSI — modulo
  `cap04_relazioni_cross.py`.

## 2. Fonti nazionali

Diritto italiano (leggi, decreti, regolamenti AgID).

- **CAD** — Codice dell'Amministrazione Digitale (D.Lgs. 82/2005 e succ.
  mod.). `fonte_id=3`. Import granulare 2026-09-16/17 secondo
  `docs/procedura-import-granulare.md` (primo import a beneficiare della
  procedura post-ADR eIDAS). 594 nodi, cross-collegato con eIDAS/eIDAS2
  (53 relazioni, ADR-0009).
- **DPCM 22 febbraio 2013** — regole tecniche FEA/firme elettroniche.
  `fonte_id=4`. Riestratto granularmente il 2026-09-17 (289 nodi: 218
  obblighi + 71 principi su 63 articoli/6 Titoli,
  `app/seed_data/dpcm/cap0[1-8].py`), sostituendo la precedente estrazione
  selettiva pre-ADR-0007. Cross-collegato con CAD (92 relazioni) ed
  eIDAS/eIDAS2 (13 relazioni) in `app/seed_data/dpcm/cap09_relazioni_cross.py`.
- **DPCM 24 ottobre 2014** (SPID) — testo vigente comprensivo delle
  modifiche del DPCM 19/10/2021, recuperato da Normattiva. `fonte_id=5`.
  Import 2026-09-21: 118 nodi (81 obblighi + 37 principi su 17 articoli),
  3 moduli capitolo (`app/seed_data/spid/cap0[1-3].py`), 47 relazioni
  interne. Cross-collegato con CAD (15, incl. 8 textual), eIDAS (3),
  eIDAS2 (3), DPCM 22/2/2013 (4) in `app/seed_data/spid/cap04_relazioni_cross.py`.
- **DPCM 19 ottobre 2021** — modifiche al DPCM 24/10/2014 (SPID).
  `fonte_id=6`. Import 2026-09-22/23, decreto interamente novellistico:
  ogni articolo censito come Principio tipo "altro" con relazione
  "modifica"/"abroga" verso il nodo Fonte 5 realmente inciso, costruita
  nativamente in fase di estrazione (non differita a Fase 6). In
  corrispondenza di questo import sono stati corretti anche ~9 nodi
  Fonte 5 che riportavano per errore il testo previgente 2014
  (`app/seed_data/spid/cap02.py`). Modulo unico `dpcm2021/cap01.py`.
- **Regolamento AgID — modalità attuative SPID** (art. 4 c.2 DPCM
  24/10/2014, v2.0 del 22/07/2016, consolidato con Avviso AgID n.10/2018 e
  Determinazione AgID n.425/2020). `fonte_id=13`. Import 2026-09-22/23, 4
  capitoli (`app/seed_data/spid_modalita_attuative/cap0[1-4].py`, incluse le
  Appendici A-D come Principi "definitorio"); la deroga parziale artt.20/23
  dell'Avviso AgID è un nodo Principio dedicato con relazioni "deroga a". 21
  relazioni cross verso DPCM 24/10/2014 e CAD; verificato zero verso le
  altre 7 Fonti al momento dell'import (`cap05_relazioni_cross.py`).
- **Regole Tecniche e Raccomandazioni AgID sui certificati elettronici
  qualificati** (13 febbraio 2020, regole tecniche ex art. 71 CAD, sostituisce
  la Deliberazione CNIPA n.45/2009). `fonte_id=15`. Import 2026-09-23, testo
  breve (21 pagine nominali) estratto direttamente in sessione principale
  senza subagent/split_source.py, 3 capitoli
  (`app/seed_data/agid_reg_tec_cert_qual/cap0[1-3].py`: cap01 Definizioni +
  Scopo e ambito di applicazione + Obblighi; cap02 Raccomandazioni (profilo
  certificati qualificati/di certificazione/di marcatura temporale, formati
  firme/sigilli, informazioni di stato); cap03 Convalida + Norme transitorie e
  abrogazioni). 49 nodi (38 obblighi, 11 principi); le "raccomandazioni" del
  capitolo 4/par.5 comma 2, pur non essendo "obblighi" in senso stretto nel
  testo originale (disapplicazione non invalida firme/sigilli, RFC 2119), sono
  modellate come Obbligo nel nostro schema — nota di modellazione completa in
  `cap02.py`. 19 relazioni cross verso eIDAS (`fonte_id=1`, 5: attua/richiama),
  eIDAS2 (`fonte_id=2`, 4: attua, citazione testuale esplicita di
  articolo/paragrafo/lettera), CAD (`fonte_id=3`, 2: si sovrappone a/richiama),
  DPCM 22/2/2013 (`fonte_id=4`, 4: si sovrappone a), DPCM 24/10/2014 SPID
  (`fonte_id=5`, 1: si sovrappone a, definizione duplicata di "Agenzia"), ETSI
  EN 319 412 (Parte 5) (`fonte_id=7`, 1: si sovrappone a), ETSI TS 119 461
  (`fonte_id=9`, 1: si sovrappone a), ETSI EN 319 401 (`fonte_id=10`, 1: si
  sovrappone a); verificato zero verso DPCM 19/10/2021, Regolamento AgID
  modalità attuative SPID, Regolamento (UE) 2025/1566, Regolamento (UE)
  2015/1502, ETSI TS 119 431 (`cap04_relazioni_cross.py`).
- **Codice Civile** (R.D. 16 marzo 1942, n. 262). `fonte_id=16`. **Import
  selettivo, non granulare — deroga esplicita ad ADR-0007** concordata con
  l'utente il 2026-09-23: il Codice Civile conta circa 3.000 articoli,
  copertura completa non richiesta né voluta per questa Fonte. Importati
  solo i 6 articoli espressamente citati da CAD (`fonte_id=3`) e DPCM
  22/2/2013 (`fonte_id=4`) già censiti — artt. 1350, 2702, 2703, 2712,
  2714, 2715 — individuati con ricerca full-text sul grafo stesso (non
  esiste un testo ufficiale grezzo del Codice Civile in
  `app/.source_cache/`), modulo unico `app/seed_data/codice_civile/cap01.py`.
  6 nodi Principio, 7 relazioni cross native (6 "richiama", 1 "modifica")
  verso CAD/DPCM 22/2/2013 — direzione invertita rispetto al caso tipico
  ADR-0009 (qui è la Fonte già censita a citare quella nuova). CAD art. 61
  c.1 (rinvio generico "ai principi stabiliti dal codice civile", senza
  articolo puntuale) escluso su indicazione esplicita dell'utente.

## 3. Fonti locali

Nessuna fonte regionale/comunale importata ad oggi. Sezione tenuta come
placeholder per quando emergerà un caso reale (es. regolamenti regionali
sull'identità digitale, ordinanze comunali con rilevanza QTSP).

## 4. Standard tecnici

Standard ETSI (ESI — Electronic Signatures and Trust Infrastructures),
strutturati in clausole/sottoclausole invece che articoli/commi. Stesso
criterio ADR-0007 di copertura completa, adattato: un nodo per
clausola/requisito numerato del testo, front matter puramente
amministrativo/bibliografico escluso (mai un nodo Obbligo/Principio per
Contents/Foreword/Modal verbs terminology/ecc., stesso trattamento del
preambolo delle fonti legislative).

- **ETSI EN 319 412** (Certificate Profiles, deliverable multi-parte). `fonte_id=7`.
  Trattata come **Fonte unica** che copre le 5 Parti, su richiesta esplicita
  dell'utente (2026-09-23). Import iniziale in deroga al criterio applicato
  a ETSI TS 119 431 ed ETSI EN 319 411 (allora Fonti separate per ciascuna
  Parte) — incoerenza segnalata all'utente e corretta nella stessa sessione
  (vedi voci sotto: entrambe consolidate a Fonte unica). Per disambiguare la
  numerazione di clausola (non unica tra le 5 Parti dello stesso
  deliverable), ogni `riferimento` porta il prefisso letterale `"Parte N: "`.
  Moduli in `app/seed_data/etsi_319_412/parte[1-5].py` + due moduli
  "capitolo virtuale" di relazioni cross (`parte6_relazioni_cross.py` per la
  Parte 5, `parte7_relazioni_cross.py` per le Parti 1-4, quest'ultimo
  agganciato dopo il wiring di ETSI EN 319 411 perché referenzia i suoi
  nodi). 189 nodi totali: Parte 1 (`fonte_id=7`, Overview and common data
  structures) 38 nodi — import 2026-09-21 originario copriva solo la Parte 5
  (allora "ETSI EN 319 412-5", 31 nodi, QCStatements, sede del troncamento
  verbatim che ha originato ADR-0010); Parte 2 (Certificate profile per
  persone fisiche) 78 nodi; Parte 3 (persone giuridiche) 16 nodi; Parte 4
  (certificati per siti web) 26 nodi — Parti 1-4 importate 2026-09-23 via 4
  subagent paralleli (documenti brevi, 10-18 pagine ciascuno). 6 relazioni
  interne fra le 5 Parti (es. Parte 3 "richiede come precondizione" verso
  Parte 2, Parte 2/4 "richiede come precondizione" verso Parte 5 per gli
  QCStatement). Cross-fonte: 5 relazioni preesistenti della Parte 5 verso
  eIDAS/eIDAS2 (mapping Annex A → Allegati I/III/IV, citazione esplicita
  art. 24 eIDAS2) e DPCM 22/2/2013 (OID id-etsi-qcs-QcSSCD, artt. 13/42); 11
  nuove relazioni delle Parti 1-4 verso ETSI EN 319 411 Parte 1 (4, incl.
  citazione esplicita REV-6.2.4-03A e clausola 6.4.5), ETSI EN 319 411 Parte
  2 (5, incl. citazione esplicita clausola 5.3) ed ETSI EN 319 401 (1,
  "terms given in EN 319 401 apply"), via pipeline grep+KNN (soglia 0.86)+
  classificazione LLM (confidence ≥ 0.55); verificato zero verso le altre 9
  fonti censite (nessuna citazione puntuale risolvibile, solo generici
  rinvii al regolamento 910/2014 nel suo complesso).
- **ETSI TS 119 461 V2.1.1** (identity proofing dei soggetti dei servizi
  fiduciari). `fonte_id=9`. Import 2026-09-22, 8 capitoli via subagent
  paralleli (`app/seed_data/etsi_119_461/cap0[1-8].py`, 81 pagine), 435
  item di indice, 50 relazioni interne. 113 relazioni cross (10 textual,
  103 inferred validate) verso le altre Fonti, incluso il collegamento
  inverso puntuale da Reg. (UE) 2025/1566, Annex C clausola C.3 —
  `cap09_relazioni_cross.py`.
- **ETSI EN 319 401 V3.2.1** (General Policy Requirements for Trust
  Service Providers). `fonte_id=10`. Import 2026-09-22, 5 capitoli
  (`app/seed_data/etsi_319_401/cap0[1-5].py`, 55 pagine), 326 item di
  indice, nessuna relazione interna (vincolo di dispatch parallelo). 26
  relazioni cross (15 textual — inclusa la tabella ufficiale Annex B
  "Mapping ... with eIDAS Regulation" — 11 inferred) verso eIDAS/eIDAS2 —
  `cap06_relazioni_cross.py`.
- **ETSI TS 119 431** (Policy and security requirements for trust service
  providers, deliverable multi-parte). `fonte_id=11`. **Fonte unica** che
  copre le 2 Parti (correzione 2026-09-23: import originario 2026-09-22
  aveva trattato le due Parti come Fonti separate, `fonte_id=11`/`12`, su
  richiesta esplicita dell'utente — incoerenza poi segnalata e corretta su
  richiesta dello stesso utente, che ha imposto lo stesso criterio "stessa
  normativa, stessa Fonte" applicato a ETSI EN 319 412). Ogni `riferimento`
  porta il prefisso `"Parte 1: "`/`"Parte 2: "`. Moduli in
  `app/seed_data/etsi_119_431_1/cap0[1-2].py` (Parte 1, TSP che operano un
  QSCD/SCDev remoto, 31 pagine, 159 item di indice, 23 relazioni interne) e
  `app/seed_data/etsi_119_431_2/cap0[1-2].py` (Parte 2, componenti TSP a
  supporto della creazione di firme AdES, 26 pagine, 95 item di indice, 41
  relazioni interne). 254 nodi totali. Le relazioni reciproche fra le due
  Parti (originariamente cross-fonte 11↔12) sono ora relazioni interne alla
  stessa Fonte 11, col prefisso di parte corretto — moduli
  `cap03_relazioni_cross.py` di entrambe le Parti, retrofit 2026-09-23
  (fonte_id 12→11 sul lato Parte 2, fonte_id 11 invariato sul lato Parte 1,
  solo aggiunta di prefisso). Relazioni cross verso fonti esterne (eIDAS,
  eIDAS2, CAD, ETSI EN 319 401) invariate nella sostanza, solo col prefisso
  di parte aggiunto sul lato Fonte 11.
- **ETSI EN 319 411** (Policy and security requirements for Trust Service
  Providers issuing certificates, deliverable multi-parte). `fonte_id=17`.
  **Fonte unica** che copre le 2 Parti (correzione 2026-09-23: import
  originario 2026-09-23 aveva trattato le due Parti come Fonti separate,
  `fonte_id=17`/`18`, su richiesta esplicita dell'utente — stessa
  incoerenza di ETSI TS 119 431, corretta nella stessa passata). Ogni
  `riferimento` porta il prefisso `"Parte 1: "`/`"Parte 2: "`. Moduli in
  `app/seed_data/etsi_319_411_1/cap0[1-5].py` (Parte 1, General
  requirements, 60 pagine, 377 item di indice, nessuna relazione interna)
  e `app/seed_data/etsi_319_411_2/cap0[1-3].py` (Parte 2, Requirements for
  trust service providers issuing EU qualified certificates, costruita
  sopra la Parte 1, 33 pagine, 173 item di indice, nessuna relazione
  interna). 550 nodi totali. Fase 6 (ADR-0009) originaria: 192 relazioni da
  Parte 1 (verso DPCM 22/2/2013, ETSI EN 319 412 Parte 5, TS 119 461, EN
  319 401, ETSI TS 119 431 Parte 1/2, Reg. (UE) 2015/1502, Regole Tecniche
  AgID certificati qualificati, EN 319 411 Parte 2) + 128 relazioni da
  Parte 2 (verso eIDAS2, ETSI EN 319 412 Parte 5, Reg. (UE) 2025/1566, TS
  119 461, EN 319 401, ETSI TS 119 431 Parte 1, Regole Tecniche AgID
  certificati qualificati, EN 319 411 Parte 1); zero verso eIDAS/CAD/SPID/
  DPCM 19-10-2021/Reg. AgID modalità attuative SPID/Codice Civile. Le
  relazioni fra le due Parti stesse (originariamente cross-fonte 17↔18)
  sono ora relazioni interne alla stessa Fonte 17; quelle verso ETSI TS 119
  431 portano il prefisso di parte corretto sul lato Fonte 11 (anch'essa
  consolidata da due Fonti in una nella stessa passata) — moduli
  `cap06_relazioni_cross.py`/`cap04_relazioni_cross.py`, retrofit
  2026-09-23.
- **ETSI EN 319 421 V1.3.1 (2025-07)** (Policy and Security Requirements for
  Trust Service Providers issuing Time-Stamps). `fonte_id=18`. Documento **non
  multi-parte** (una sola Parte, nessun prefisso di parte nei `riferimento`).
  Import 2026-09-24 via 6 subagent paralleli, 6 moduli
  `app/seed_data/etsi_319_421/cap0[1-6].py` (cap01 clausole 1-4; cap02
  clausole 5-6; cap03 clausola 7.1-7.6.7; cap04 clausola 7.7-7.16; cap05
  clausola 8; cap06 annex informative A-H). 138 nodi totali (118 obblighi, 20
  principi), 138 item di indice — un item per requirement id del testo
  ufficiale (`OVR-…`/`TIS-…`, inclusi i suffissi letterali tipo `OVR-5.2-01A`)
  più un item per ciascuna clausola di cornice priva di requisito numerato
  (`"clausola X.Y (Title)"`). Clausola 2 (References) e clausola 3.2
  (Symbols, testo integralmente "Void.") fuori perimetro in quanto
  bibliografia/paratesto, History escluso — stesso criterio già applicato a
  ETSI EN 319 401. 8 relazioni interne, tutte da citazione letterale di un
  requirement id (`cap01.py` 1: clausola 4.3 → TIS-7.7.1-08; `cap03.py` 3;
  `cap04.py` 4). Fase 6 (ADR-0009): 733 coppie candidate a zero token (563
  KNN, k=6 soglia 0.84; 170 da citazioni testuali a clausola di standard ETSI
  o articolo eIDAS risolte contro i `riferimento` reali), classificazione LLM
  su 122 nodi di partenza (266 proposte), validazione → **227 relazioni
  cross-fonte** (165 richiama, 61 si sovrappone a, 1 specifica; 164 textual,
  63 inferred) in `app/seed_data/etsi_319_421/cap07_relazioni_cross.py`, verso
  ETSI EN 319 401 (160), ETSI EN 319 411 (33), ETSI TS 119 431 (11), ETSI TS
  119 461 (9), eIDAS2 (6), eIDAS (5), DPCM 22/2/2013 (3). Le proposte verso
  nodi eIDAS dell'art. 24 §2 marcati abrogati sono state rimappate ai
  successori vigenti in eIDAS2 (lettera (j), abrogata senza successore,
  scartata). Le citazioni a standard non censiti nel grafo al momento di
  questo giro (ETSI TS 119 312/119 612/119 615, EN 419231, TS
  419221-2/-3/-4/-5, ISO/IEC 15408/19790, FIPS PUB 140-2/-3, CID (EU)
  2015/1505, direttiva 93/13/EEC) non producono relazioni per assenza di nodo
  controparte. ETSI EN 319 422, citato in questo giro quando non era ancora
  censito, è stato importato successivamente come Fonte 19 (vedi voce sotto):
  i rinvii 319 421 ↔ 319 422 sono ora registrati dal lato Fonte 19. Nessun
  nodo isolato: tutti i 138 nodi hanno almeno un arco.
- **ETSI EN 319 422 V1.1.1 (2016-03)** (Time-stamping protocol and time-stamp
  token profiles). `fonte_id=19`. Documento **non multi-parte**. Import
  2026-09-24 via 4 subagent paralleli, 4 moduli
  `app/seed_data/etsi_319_422/cap0[1-4].py` (cap01 clausole 1-3; cap02
  clausole 4-5; cap03 clausole 6-8; cap04 clausola 9 + Annexes A-C normative).
  27 nodi totali (21 obblighi, 6 principi), 27 item di indice — uno per
  clausola/sottoclasse numerata con contenuto proprio, con `riferimento` nel
  formato `"clausola X.Y (Titolo)"` (il documento non usa requirement id
  OVR-/TIS- come 319 401/319 421) e `"Annex X (Titolo)"` per gli allegati.
  Le intestazioni di puro raggruppamento (clausole 2, 3, 4, 4.1, 4.2, 5, 5.1,
  5.2, 6, 9) non generano nodo; clausola 2 (References) esclusa in quanto
  bibliografia/paratesto; History escluso. 0 relazioni interne (il documento
  non cita requirement id propri). Fase 6 (ADR-0009): 87 coppie candidate a
  zero token (83 KNN, k=8 soglia 0.80; 4 da citazioni esplicite a ETSI EN 319
  412-2/-3 e Reg. 910/2014 risolte contro i `riferimento` reali),
  classificazione LLM sullo shortlist (22 proposte), validazione → **22
  relazioni cross-fonte** (16 si sovrappone a, 5 richiama, 1 attua; 16
  inferred, 6 textual) in `app/seed_data/etsi_319_422/cap05_relazioni_cross.py`,
  verso ETSI EN 319 412 (6), ETSI EN 319 421 (6), ETSI TS 119 431 (5),
  Regole Tecniche AgID certificati qualificati (2), eIDAS (1), DPCM 22/2/2013
  (1), ETSI EN 319 401 (1). Le citazioni a standard non censiti (IETF RFC
  3161/5816/3739/6838/7230-7235/2818, ETSI TS 119 312, ETSI EN 319 102-1,
  ETSI TS 101 861) non producono relazioni per assenza di nodo controparte.
  Nessun nodo isolato: tutti i 27 nodi hanno almeno un arco.
- **ETSI TS 119 432 V1.3.1 (2026-03)** (Protocols for remote digital signature
  creation). `fonte_id=20`. Documento **non multi-parte**. Import 2026-09-24
  via 7 subagent paralleli, 7 moduli `app/seed_data/etsi_119_432/cap0[1-7].py`
  (cap01 clausole 1-3; cap02 clausola 4 + 5.1-5.2; cap03 clausole 5.3-5.5;
  cap04 clausola 6, architetture e casi d'uso incl. EUDIW; cap05 clausole 7-8,
  API del servizio di creazione di firme e profilo OASIS DSS-X; cap06 Annex A
  normativo, profilo OpenID4VP EUDIW-centric; cap07 Annex B + Annex C
  normativi). 118 nodi (69 obblighi, 49 principi), 118 item di indice — uno per
  clausola/sottoclavola numerata con contenuto proprio, con `riferimento` nel
  formato `"clausola X.Y (Titolo)"` / `"Annex X.Y (Titolo)"`. Fuori perimetro:
  front matter non numerato, clausola 2 (References), Annex D (informative,
  Change history), History. 12 relazioni interne da citazione letterale
  (11 textual, 1 inferred). Il testo ufficiale abbrevia con `...` i payload
  negli EXAMPLE (token JWT/Base64, `?token=...`, `{...}`): unico caso finora
  in cui l'ellissi è contenuto autentico e non troncamento, gestito estendendo
  `_senza_omissis_legittimi` in `app/seed_data/lib.py` con una terza
  convenzione a tre condizioni strette (stringa quotata, dopo `=`/`{`, oppure
  incollata a un token con cifre/run maiuscolo — un `...` su prosa resta
  bloccato); `app/tools/verifica_troncamento.py` ora importa la stessa
  normalizzazione invece di duplicarla, dopo che il primo giro aveva prodotto
  6 falsi positivi su questa Fonte. Fase 6 (ADR-0009): 164 coppie candidate
  KNN (soglia 0.80) + citazioni esplicite rilevate a grep (eIDAS 11 estratti,
  eIDAS2 2, ETSI TS 119 431-1/-2 4 ma solo bibliografiche), shortlist estesa
  con 21 nodi eIDAS/eIDAS2 degli istituti pertinenti per i 10 nodi che citano
  il regolamento, classificazione LLM in due passate (33 proposte grezze),
  validazione con risoluzione per `fonte_id` (necessaria: le stringhe
  "Parte 1/2: …" sono condivise fra Fonte 11 e Fonte 17, e "art. 26" fra più
  Fonti) → **24 relazioni cross-fonte** (8 specifica, 8 si applica a, 6 si
  sovrappone a, 1 richiama, 1 attua; 21 inferred, 3 textual) in
  `app/seed_data/etsi_119_432/cap08_relazioni_cross.py`, verso eIDAS2 (16:
  artt. 29 §1-bis, 29-bis §1, 5 bis §4(e)/§5(g)), eIDAS (3: artt. 26, 29 §1),
  ETSI TS 119 431 (4) e DPCM 22/2/2013 (1). Le citazioni a standard non
  censiti (CSC API/CSC DM — 130 occorrenze, IETF RFC, OASIS DSS-X, ETSI EN 419
  241, EUDI ARF) non producono relazioni per assenza di nodo controparte.
  4 nodi restano senza archi oltre `DA_FONTE` (clausole 3.1 Terms, 3.2 Symbols,
  3.3 Abbreviations e 6.4.5.1 Introduction): sono paratesto/glossario, stessa
  condizione di nodi analoghi già presenti in altre Fonti (es. ETSI EN 319
  421/422), e le proposte di relazione glossario-contro-glossario sono state
  scartate in validazione perché prive di contenuto normativo proprio.
- **ETSI TS 119 612 V2.4.1 (2025-08)** (Trusted Lists). `fonte_id=21`.
  Documento **non multi-parte** (nessun prefisso di parte nei `riferimento`).
  Import 2026-09-24 via 8 subagent paralleli, 8 moduli
  `app/seed_data/etsi_119_612/cap0[1-8].py` (cap01 clausole 1, 3, 4; cap02
  clausola 5 intro + 5.1-5.3; cap03 5.4 + 5.5.1-5.5.8; cap04 5.5.9 + 5.5.10 +
  5.6 + 5.7; cap05 clausola 6 + Annex A/B; cap06 Annex C/D; cap07 Annex E/F/G;
  cap08 Annex H/I/J). 118 nodi (91 obblighi, 27 principi), 118 item di indice —
  un nodo per clausola/sottoclausola numerata con contenuto proprio, con
  `riferimento` nel formato `"clausola X.Y (Titolo)"` / `"Annex X.Y (Titolo)"`;
  le intestazioni di puro raggruppamento (5, 5.1, 5.3, 5.4, 5.5, 5.6, 5.7,
  Annex D, Annex E/F/G, Annex H/I/J) non generano nodo. Fuori perimetro: front
  matter (copertina/notice/Contents/IPR/Foreword/Modal verbs/Introduction),
  clausola 2 (References: bibliografia) e History — stesso criterio delle altre
  Fonti ETSI. 164 relazioni interne fra i capitoli (tutte "richiama"/textual,
  da rinvii testuali puntuali a clausole/annessi). Peculiarità: il testo
  ufficiale è stato estratto con `pdftotext -layout` invece della pipeline
  markdown usata dalle altre Fonti ETSI, perché questo documento conserva i
  numeri di clausola nelle intestazioni (decisivi per la copertura ADR-0007);
  i marcatori `<!-- Page N -->` sono separatori di pagina. Il testo ufficiale
  contiene ellissi autentiche in Annex D.0/D.6 (radix degli URI registrati,
  `"…/19612/……"`, `"…/TrstSvc/……"`) e nella clausola 5.5.3 (segnaposto di
  segmento dentro un pattern di URI non quotato, `…/Svctype/.../nothavingPKIid`):
  gestite estendendo `_senza_omissis_legittimi` in `app/seed_data/lib.py` con
  `_ELLISSI_SU_RADIX_URI`/`_ELLISSI_IN_URI` (stessa normalizzazione importata
  dall'audit `app/tools/verifica_troncamento.py`). Fase 6 (ADR-0009): 321
  coppie candidate a zero token (258 KNN, k=8 soglia 0.80 + 63 da citazioni
  esplicite del Reg. (UE) 910/2014, del Reg. (UE) 2024/1183 e di ETSI EN 319
  412-5), classificazione LLM sull'intero shortlist (60 proposte), validazione
  → **54 relazioni cross-fonte** (31 si sovrappone a, 19 specifica, 3 richiama,
  1 richiede come precondizione; 53 inferred, 1 textual) in
  `app/seed_data/etsi_119_612/cap09_relazioni_cross.py`, verso eIDAS (21:
  artt. 22 §1-§5 — ETSI TS 119 612 è la specifica tecnica di formato/semantica/
  accesso degli elenchi di fiducia — e art. 23 §1), ETSI EN 319 412 (10), ETSI
  EN 319 401 (5), ETSI EN 319 411 (5), Regole Tecniche AgID certificati
  qualificati (4), DPCM 22/2/2013 (3), ETSI EN 319 421 (3), eIDAS2 (2), ETSI
  TS 119 431 (1). La sola relazione "textual" è la clausola 5.5.1.2, che cita
  letteralmente "Article 3(16)"/"Article 3(46) of Regulation (EU) 910/2014":
  risolta sul nodo vigente "art. 3 (definizioni)" di eIDAS2, perché in eIDAS
  (fonte 1) l'art. 3 non ha un nodo — stessa rimappatura sui successori vigenti
  già applicata nel giro Fase 6 di ETSI EN 319 421. Verificato zero verso CAD,
  SPID (DPCM 24/10/2014), DPCM 19/10/2021, Reg. (UE) 2025/1566, ETSI TS 119
  461, Reg. AgID modalità attuative SPID, Reg. (UE) 2015/1502, ETSI EN 319 422
  ed ETSI TS 119 432. Le citazioni a fonti non censite (Commission Decision
  2009/767/EC, ETSI TS 119 312, ISO/IEC 15408 e 19790, IETF RFC 3161/5280,
  CID (EU) 2015/1505, direttiva (UE) 2022/2555) non producono relazioni per
  assenza di nodo controparte. 34 dei 118 nodi restano senza archi tipizzati
  oltre `DA_FONTE` (clausole di campo, registri di URI e annessi senza rinvii
  interni espliciti) — nessun nodo isola quanto a `DA_FONTE`, e le proposte
  glossario-contro-glossario sono state scartate come per la Fonte 20.


## Riepilogo

| Categoria | Fonti | Totale |
|---|---|---|
| Internazionali | eIDAS, eIDAS2, Reg. (UE) 2025/1566, Reg. (UE) 2025/1567, Reg. (UE) 2015/1502 | 5 |
| Nazionali | CAD, DPCM 22/2/2013, DPCM 24/10/2014, DPCM 19/10/2021, Reg. AgID modalità attuative SPID, Regole Tecniche AgID certificati qualificati 13/2/2020, Codice Civile (selettivo) | 7 |
| Locali | — | 0 |
| Standard tecnici | ETSI EN 319 412 (5 Parti, Fonte unica), ETSI TS 119 461, ETSI EN 319 401, ETSI TS 119 431 (2 Parti, Fonte unica), ETSI EN 319 411 (2 Parti, Fonte unica), ETSI EN 319 421, ETSI EN 319 422, ETSI TS 119 432, ETSI TS 119 612 | 9 |
| **Totale** | | **21** |

20 delle 21 Fonti hanno copertura granulare completa (ADR-0007) e sono
cross-collegate; nessuna resta isola nel grafo. Il Codice Civile
(`fonte_id=16`) è l'unica eccezione deliberata: copertura selettiva (6
articoli su ~3.000), deroga esplicita ad ADR-0007 concordata con l'utente
il 2026-09-23 — vedi voce dedicata sopra. Nessuna Fonte multi-parte tratta
le proprie Parti come Fonti separate: ETSI EN 319 412 (5 Parti), ETSI TS
119 431 (2 Parti) ed ETSI EN 319 411 (2 Parti) sono tutte Fonti uniche —
correzione 2026-09-23 dell'incoerenza iniziale su TS 119 431/EN 319 411
(import per Parte separata), applicata su richiesta esplicita dell'utente
per uniformare il criterio di modellazione a tutte le fonti multi-parte
censite.

**Allineamento codice/commit**: non dichiarato qui, per non invecchiare al
primo commit. Prima di ogni import, verificare con `git status --short` e
`git log --oneline -- app/seed_data app/seed.py docs/fonti-censite.md` quali
Fonti siano già committate e quali siano solo su disco: la nota di stato
precedente (2026-09-24) indicava come non committati gli import di ETSI EN
319 421/422, già chiusi in `15ffd30`.
