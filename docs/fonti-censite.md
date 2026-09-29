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
- **Regolamento di esecuzione (UE) 2025/1569** — modalità di applicazione
del regolamento (UE) n.910/2014 per quanto riguarda gli attestati
elettronici qualificati di attributi (QEAA) e gli attestati elettronici di
attributi rilasciati da un organismo del settore pubblico responsabile di una
fonte autentica o per suo conto (basi giuridiche dichiarate: artt. 45
quinquies §5, 45 sexies §2, 45 septies §6 e §7 eIDAS2). `fonte_id=22`. Import
2026-09-28, testo ufficiale italiano via `app/tools/cellar_fetch.py` (CELEX
`32025R1569`), 11 articoli + 3 allegati (28.500 caratteri di articolato, il
preambolo resta fuori perimetro), diviso in 3 capitoli con
`app/tools/split_source.py` ed estratto da 3 subagent paralleli con path di
output assegnati prima del dispatch (`cap0[1-3].py`) più il capitolo virtuale
di Fase 6 (`cap04_relazioni_cross.py`). 53 nodi (41 obblighi, 12 principi),
102 item di indice: un nodo per articolo e per comma, con le lettere
indicizzate separatamente e mappate al nodo del proprio comma quando non
hanno prescrizione autonoma (art. 4 §3 a-c, art. 6 §2 e §3, art. 7 §5 a-h,
art. 8 §3 a-i). 13 relazioni: 9 native (4 "attua" dall'art. 1 verso le
quattro basi giuridiche, 3 "richiama" verso eIDAS2 artt. 45 septies §3 e 45
sexies §1, 1 "specifica" verso la clausola 1 di ETSI EN 319 401) + 4 dal giro
Fase 6 (2 "specifica" verso eIDAS2 artt. 45 quinquies §1 e 24 §4-bis, 2 "si
sovrappone a" verso ETSI TS 119 461 `QTS-C.2.3-03` ed ETSI EN 319 411-1
`Parte 1: REG-6.3.1-00F`). Primo giro di Fase 6 del progetto eseguito **senza
seedare prima la Fonte nuova** (candidati KNN calcolati al volo con
`app/tools/fase6_candidati_knn.py`): un solo `seed.py` per import. Il numero
contenuto di relazioni è un esito verificato, non una fase saltata: gli
istituti dell'atto (catalogo degli attributi, catalogo dei regimi, attestati
per il portafoglio EUDI, notifica degli organismi del settore pubblico) sono
in larga parte nuovi rispetto al corpus censito, orientato a certificati,
formati AdES, marche temporali e identity proofing; 10 dei 53 nodi non hanno
alcun candidato sopra soglia. Nota di perimetro: l'allegato II punto 1 rinvia
ai formati del **Reg. di esecuzione (UE) 2024/2979** (portafogli EUDI), non
ancora censito al momento dell'import — vedi backlog in
`docs/plan-import-lotto-eidas2-standard.md` § 7. **Aggiornamento
2026-09-29**: il Reg. 2024/2979 è stato importato come Fonte 28 e quel rinvio
è ora un arco tipizzato (Fonte 22 «allegato II, punto 1» —`richiama`→ Fonte 28
«allegato II»), creato dal giro di Fase 6 della Fonte 28. Il modulo
`app/seed_data/reg_ue_2025_1569/cap04_relazioni_cross.py` lo elenca ancora tra
i rinvii senza bersaglio (nota storica della sessione, non più vera).
- **Regolamento di esecuzione (UE) 2025/2531** — norme di riferimento e
specifiche applicabili ai registri elettronici qualificati (art. 45 terdecies
§3 eIDAS2). `fonte_id=23`. Import 2026-09-28, testo ufficiale italiano via
`app/tools/cellar_fetch.py` (CELEX `32025R2531`), 2 articoli + 1 allegato,
capitolo unico (`app/seed_data/reg_ue_2025_2531/cap01.py` + capitolo virtuale
`cap02_relazioni_cross.py`) estratto da un solo subagent worker. 26 nodi (18
obblighi, 8 principi), 53 item di indice: art. 1 (rinvio all'allegato), art. 2
(entrata in vigore — l'atto **non** ha una disposizione di applicazione
differita, quindi un solo nodo e non due), allegato punto 1 (15 definizioni
distribuite, una riga), punto 2, punto 3 (chapeau: creare, aggiornare e
mantenere il registro), punto 3(a) e 3(b) (designazione delle norme di
riferimento), punto 3(a) 2.1 (aggiunte bibliografiche: ENISA, RFC 7515, FIPS
PUB 140-3, regg. (UE) 2024/482 e 2024/3144, ISO/IEC 15408:2022) e 16 nodi,
uno per id di requisito, per gli adattamenti a ETSI EN 319 401. **18
relazioni**: 15 native (art. 45 terdecies §3 come base giuridica; specifica
dell'art. 45 terdecies §1; rinvio alla clausola 1 della Fonte 10; 12
"modifica" verso requisiti della stessa norma: `REQ-6.2-03`, `REQ-6.3-04`,
`REQ-7.2-04`, `REQ-7.2-05`, `REQ-7.5-01`, `REQ-7.5-05`, `REQ-7.8-14`,
`REQ-7.8-18`, `REQ-7.8-22`, `REQ-7.9.1-02`, `REQ-7.12-02` + richiamo
all'art. 24 §5 eIDAS2) + 3 dal giro Fase 6 (2 "si sovrappone a" verso gli
atti gemelli del lotto — Fonti 8 e 12 — per la clausola sul piano di
cessazione, 1 verso il DPCM 22/2/2013 per il dispositivo sicuro di firma).
**Avvertenza di mappatura**: la numerazione dell'atto non coincide sempre con
quella della Fonte 10, perché l'atto adegua la V3.1.1 (2024-06) e la Fonte 10
censisce la V3.2.1 (2026-01): il requisito sui firewall è `REQ-7.8-21X`
nell'atto ma `REQ-7.8-22` nella norma censita, e l'atto cita come
`REQ-7.8-17X` il requisito sul test di penetrazione che nella versione
censita è `REQ-7.8-18`. Le relazioni sono agganciate per contenuto, non per
numero, e ciascuna porta la nota dello scostamento. `REQ-6.1-12` (contenuto
della dichiarazione sulla pratica) è invece un requisito **nuovo** — la
clausola 6.1 della Fonte 10 si ferma a `REQ-6.1-11` — e resta senza relazioni.
- **Regolamento di esecuzione (UE) 2025/2532** — norme di riferimento e
specifiche per i servizi di archiviazione elettronica qualificati (art. 45
undecies §2 eIDAS2). `fonte_id=24`. Import 2026-09-28, testo ufficiale
italiano via `app/tools/cellar_fetch.py` (CELEX `32025R2532`), 3 articoli + 1
allegato, capitolo unico (`app/seed_data/reg_ue_2025_2532/cap01.py` + capitolo
virtuale `cap02_relazioni_cross.py`) estratto da un subagent worker. 14 nodi
(9 obblighi, 5 principi), 53 item di indice: art. 1 §1 (obbligo di
conservazione), art. 1 §2 (facoltà di avvalersi di un servizio di conservazione
qualificato), art. 2 (rinvio), art. 3 (entrata in vigore — un solo nodo,
nessuna applicazione differita), chapeau dell'allegato che designa
**CEN/TS 18170:2025** e le nove lettere di adeguamento a)-i), una per lettera,
con le voci interne indicizzate. **12 relazioni**: 9 native (art. 45 undecies
§1 e §2; art. 24 §5 per le lettere b) e h); citazione letterale di
`REQ-7.8-13` — scansione delle vulnerabilità trimestrale — e di
`REQ-7.8-17X`, che nella Fonte 10 censita è `REQ-7.8-18`; e le tre clausole sul
piano di cessazione che **completano a rete completa** il gruppo di clausole
identiche dei quattro atti del lotto: Fonti 8, 12, 23 e 24 si vedono ora
a vicenda) + 3 dal giro Fase 6 (personale in ruoli di fiducia verso
`REQ-7.2-04`/`REQ-7.2-05`; dispositivo sicuro di firma verso il DPCM
22/2/2013 art. 11 c.1). **Primo caso del censimento in cui la norma portante
non è ETSI ma CEN**: CEN/TS 18170:2025 è la sede dell'intero allegato e non è
censita (backlog del piano § 7). I rinvii di clausola — ETSI EN 319 401 punti
5, 7.5, 7.8, 7.10 e CEN/TS 18170 punti 6.1, 6.2, 7.3, 7.13, 13.3.1 — non
producono relazioni, perché la Fonte 10 ha nodi per id di requisito e non per
clausola: nessun aggancio arbitrario, esito documentato nel modulo. È il motivo
per cui questo atto, pur essendo il più dipendente da norme tecniche, è quello
con meno relazioni del lotto.
- **Regolamento di esecuzione (UE) 2015/1502** — specifiche/procedure
  tecniche minime sui livelli di garanzia (basso/significativo/elevato) dei
  mezzi di identificazione elettronica, ex art. 8 §3 eIDAS. `fonte_id=14`.
  Import 2026-09-22/23, 3 capitoli (`app/seed_data/reg_ue_2015_1502/`),
  29 nodi (18 obblighi, 11 principi). Fase 6 in due passaggi: 2 relazioni
  native corrette (omesse per errore nell'estrazione originaria) + 7
  relazioni da pipeline grep+KNN+LLM (704 candidati) verso DPCM 19/10/2021,
  Regolamento AgID modalità attuative SPID e 2 standard ETSI — modulo
  `cap04_relazioni_cross.py`.
- **Regolamento di esecuzione (UE) 2024/2979** — modalità di applicazione del
  regolamento (UE) n. 910/2014 per quanto riguarda l'integrità e le
  funzionalità di base dei portafogli europei di identità digitale (base
  giuridica: art. 5 bis §23 eIDAS2). `fonte_id=28`. Primo import del lotto 2
  (blocco A, `docs/plan-import-lotto-2-backlog-e-ades.md`). Testo ufficiale
  italiano acquisito con `app/tools/cellar_fetch.py` (CELEX `32024R2979`,
  provenienza e sha256 in `app/.source_cache/reg_ue_2024_2979/`), split in 5
  capitoli (Capi I-IV + Allegati I-V) e autoria su 5 subagent paralleli:
  `app/seed_data/reg_ue_2024_2979/cap0[1-6].py`. 48 nodi (35 obblighi, 13
  principi), 95 item di indice — un nodo per comma e per lettera, gli allegati
  per punto numerato, l'art. 2 (15 definizioni) come **un solo** Principio
  definitorio con le 15 voci indicizzate una per una. **25 relazioni**: 14
  native interne (rinvii tra articoli e all'allegato I) + 10 dal giro di Fase
  6 in `cap06_relazioni_cross.py` — 9 in direzione diretta (1 «attua»
  dall'art. 1 verso eIDAS2 art. 5 bis §23 come base giuridica dell'atto; 4
  «specifica» verso eIDAS2 art. 5 bis — §5(e) politiche di divulgazione
  incorporate, §4(b) pseudonimi, §4(d) registro delle transazioni, §4(e)
  firma/sigillo qualificato; 3 «richiama» verso il Reg. 2015/1502, in
  particolare l'allegato punto 2.2.1 per la progettazione del mezzo di
  identificazione a livello elevato; 1 «si sovrappone a» verso Fonte 22 per la
  stessa lista di norme sugli attestati, imposta dal lato del fornitore e dal
  lato del portafoglio) **+ 1 in direzione inversa** (Fonte 22 «allegato II,
  punto 1» —`richiama`→ «allegato II» di questa Fonte): è il rinvio che il
  modulo di Fase 6 di Fonte 22 dichiarava senza bersaglio. **Limite
dichiarato**: la citazione dell'art. 3 §1 all'art. 5 bis §4 eIDAS2 resta
  senza arco **fino al 2026-09-29**, perché Fonte 2 modella quel paragrafo per
  lettere (§4(a)-(g)) senza un nodo di chapeau del paragrafo, e agganciarlo a una
  lettera sarebbe arbitrario. Il rinvio è ora un arco verso la partizione
  "art. 5 bis" di Fonte 2 (ADR-0012). **Audit § 10 di `docs/verifiche-aperte.md`**: 11 relazioni
  `textual` di questa Fonte segnalate senza traccia del riferimento citato, di
  cui 7 falsi positivi dello strumento (il testo cita «i paragrafi 1 e 2» o
  «la lettera b)» in una forma che l'estrattore non riconosce) e 4 con
  bersaglio scelto per contenuto (base giuridica nel preambolo; tre richiami
  al Reg. 2015/1502 senza numero di articolo/allegato nel testo citante).
- **Regolamento di esecuzione (UE) 2024/482** — EUCC: sistema europeo di
  certificazione della cibersicurezza basato sui criteri comuni (modalità di
  applicazione del regolamento (UE) 2019/881). `fonte_id=29`. Secondo import
  del lotto 2. Testo ufficiale italiano via `app/tools/cellar_fetch.py` (CELEX
  `32024R0482`, 135k caratteri, provenienza e sha256 in
  `app/.source_cache/reg_ue_2024_482/`), il documento più esteso del lotto:
  14 capitoli (Capi I-XI + Allegati I-IX), autoria su 14 subagent worker.
  **256 nodi** (196 obblighi, 60 principi), 572 item di indice — un comma una
  riga, le lettere mappate al comma di appartenenza quando non hanno precetto
  autonomo, gli allegati censiti per punto e sezione. **229 relazioni**: 86
  interne ai capitoli (rinvii fra commi dello stesso articolo e fra articoli
  dello stesso capitolo) + **143 nel capitolo virtuale**
  `app/seed_data/reg_ue_2024_482/cap15_relazioni_cross.py` — 139 «richiama»
  `textual` cross-capitolo (citazioni letterali risolte con la regola di
  miraggio dell'ADR-0012: **130 verso partizioni** di articolo o allegato citati
  «in blocco», compresi i 51 rinvii che prima restavano senza arco, e **9 verso
  nodi di comma** su citazione di paragrafo esplicita) e 4 cross-fonte: 2 «richiama» `inferred` da
  eIDAS2 artt. 5 quater §2 e 12-bis §2 (la certificazione di portafoglio e
  regimi va fatta «in conformità dei sistemi europei di certificazione della
  cibersicurezza», categoria di cui l'EUCC è un'istanza), 1 «si sovrappone a»
  `inferred` dall'art. 3 (criteri comuni come base della valutazione) verso
  eIDAS art. 30 §3 (certificazione dei dispositivi per la creazione di firma
  qualificata), 1 «richiama» `textual` in direzione inversa (Fonte 24,
  adeguamento e) sui controlli crittografici: il dispositivo crittografico
  sicuro dell'EATSP è certificato EUCC). **Note di revisione dichiarate**: il
  criterio di `tipo_obbligo` per le conseguenze della non conformità è
  disomogeneo fra i capitoli e richiede una decisione —
  `docs/verifiche-aperte.md` § 3-bis; i rinvii a norme esterne non censite
  (regolamento (UE) 2019/881, ISO/IEC 15408 e 18045, regg. 2016/799 e
  765/2008, decisione 2016/650, direttiva (UE) 2022/2555) restano senza arco.
- **Regolamento di esecuzione (UE) 2024/3144** — modifica del regolamento di
  esecuzione (UE) 2024/482 per quanto riguarda le norme internazionali
  applicabili e rettifica di tale regolamento (atto **modificativo e
  rettificativo** della Fonte 29). `fonte_id=30`. Terzo import del lotto 2;
  testo ufficiale italiano via `app/tools/cellar_fetch.py` (CELEX `32024R3144`,
  22k caratteri, provenienza in `app/.source_cache/reg_ue_2024_3144/`), 5
  capitoli, autoria su 5 subagent worker. **19 nodi** (3 obblighi, 16
  principi), 37 item di indice: le righe sono le disposizioni *dell'atto
  modificativo* (i punti dell'art. 1 e dell'art. 2, gli artt. 2-3, i suoi due
  allegati), con il testo sostitutivo fra virgolette nel `testo_integrale`; le
  disposizioni del regolamento modificato non sono duplicate (vivono in Fonte
  29). **17 relazioni**: 1 interna + **16 nel capitolo virtuale**
  `app/seed_data/reg_ue_2024_3144/cap06_relazioni_cross.py`, tutte `textual` e
  tutte verso la Fonte 29 tranne una — 7 «sostituisce» (partizioni artt. 2, 3,
  16 e allegato I, nodo art. 29 §2, nodi «allegato IV, sezione IV.3, punto 5 e
  6»), 3 «abroga» (partizioni artt. 23 e 24, soppressi in vista del reg. di
  esecuzione (UE) 2024/3143, più il nodo art. 17 §1), 5 «modifica» (partizioni
  artt. 48 e 49 e allegato IV sezione IV.3, nodi artt. 5 §1 e 8 §1) e 1
  «richiama» `inferred` (0.60) verso eIDAS art. 30 §3. Con la regola di
  miraggio dell'ADR-0012 gli interventi su un'unità indivisa vanno alla
  partizione dell'unità (l'abrogazione degli artt. 23-24 è due archi invece di
  sei, la sostituzione dell'allegato I un arco invece di due) e restano sul nodo
  di comma solo gli interventi puntuali. L'art. 1,
  punto 3 (nuovo art. 20 bis sull'accreditamento) resta senza arco: nessun
  nodo controparte, l'articolo è nuovo.

- **ETSI EN 319 122-1 V1.3.1 (2023-06)** — CAdES digital signatures, Parte 1 (building
  blocks e firme baseline). `fonte_id=31`. **Primo import del blocco B** (famiglia AdES,
  `docs/plan-import-lotto-2-backlog-e-ades.md` § 5). Testo ufficiale dal deliver ETSI
  (PDF, `pdftotext -layout`; provenienza, versione e sha256 in
  `app/.source_cache/etsi_319_122/provenance.json`): 63 pagine, 194.767 caratteri, corpo
  tagliato dal front matter (l'indice ripete i titoli delle clausole) e diviso in 7
  capitoli, autoria su 7 subagent worker. **125 nodi** (76 obblighi, 49 principi), 125
  item di indice: granularità alla clausola/sottoclausta, all'id di requisito dove lo
  standard ne numera, e — nella clausola 6.3 — **una riga per ciascuno dei venti requisiti
  aggiuntivi a)-t)** delle firme baseline, che il documento stesso indicizza dalla tabella
  1 (scelta di granularità fine documentata nel modulo `cap04.py`; è il punto su cui si
  può decidere una convenzione di famiglia prima degli altri quattro standard AdES).
  **185 relazioni**: 50 interne ai capitoli + **135 nel capitolo virtuale**
  `app/seed_data/etsi_319_122/cap08_relazioni_cross.py` — 100 «richiama» `textual`
  cross-capitolo o verso annessi, risolte con la regola di miraggio dell'ADR-0012 (nodo
  della clausola se esiste, altrimenti partizione padre più specifica: `clausola 5.4`,
  `Annex A, clausola A.1`, `Annex A`); 5 «si sovrappone a» `inferred` verso Fonti 27
  (attributi CAdES che EN 319 102-1 elenca come attributi da elaborare in convalida:
  commitment-type-indication, signature-policy-store, signer-attributes-v2), 25 (sezione
  CRL di TS 119 312) e 7 (moduli ASN.1 di dichiarazioni di EN 319 412-5); **30 in
  direzione inversa** (`richiama`, `textual`, 0.85) dai nodi già censiti che nominano la
  norma, ancorati alla partizione `clausola 1 (Scope)` perché il rinvio è allo standard
  come insieme. **Note**: i 434 candidati KNN sono in maggioranza rumore da titoli di
  clausola identici fra standard diversi («clausola 3.2 (Symbols)», «clausola 3.1
  (Terms)»); le cinque coppie tenute sono state verificate leggendo entrambe le parti.
  Dubbi di classificazione dichiarati nel modulo: le lettere di requisito con solo
  «should» censite come Obblighi (precedente EN 319 401/319 102-1, divergente da EN 319
  411-1), `clausola 3.2 (Symbols)` inclusa («Void.») mentre altri moduli della famiglia la
  escludono, Annex C (Void) e Annex F (Change History) inclusi per istruzione del batch.

- **ETSI EN 319 132-1 V1.3.1 (2024-07)** — XAdES digital signatures, Parte 1 (building
  blocks e firme baseline). `fonte_id=32`. **Secondo standard del blocco B** (famiglia
  AdES). Testo ufficiale dal deliver ETSI (PDF; provenienza, versione e sha256 in
  `app/.source_cache/etsi_319_132/provenance.json`): 77 pagine, 266.763 caratteri, corpo
  tagliato dal front matter e diviso in 10 capitoli (clausola 1; clausola 3; clausola 4;
  clausola 5 in tre porzioni; clausola 6; Annex A con B e C; Annex D; Annex E),
  autoria su 10 subagent worker. **154 nodi** (141 obblighi, 13 principi), 154 item di
  indice, con **granularità fine** dove il documento numera o indicizza i requisiti
  (lettere a)-cc) della clausola 6.3 delle firme baseline, passi numerati delle procedure
  di convalida, qualifier): è la convenzione di famiglia fissata con EN 319 122-1.
  **269 relazioni**: 124 interne ai capitoli + **145 nel capitolo virtuale**
  `app/seed_data/etsi_319_132/cap11_relazioni_cross.py` — 92 «richiama» `textual`
  cross-capitolo o verso annessi (regola di miraggio ADR-0012: nodo se la clausola esiste
  come riga, altrimenti partizione padre più specifica) e le altre in direzione inversa,
  dai nodi già censiti che nominano la norma (fra cui quelli di CAdES, Fonte 31: i due
  standard si rinviano a vicenda). **Note dichiarate**: il giro KNN cross-fonte è stato
  lanciato ma non ancora incorporato nel modulo (resa attesa bassa, per CAdES 5 relazioni
  utili su 434 coppie); due capitoli della clausola 5 tengono i requisiti numerati dentro
  la riga della sottoclausta dove il documento non le richiama per numero, mentre la
  clausola 6 e gli annessi le scompongono — differenza documentata nei moduli, da
  riconciliare se la revisione vuole la granularità fine ovunque; le 5 relazioni `textual`
  che citano una voce con numero nudo («references in 1) and 3)») sono segnalate
  dall'audit § 10 perché lo strumento non le sa cercare.

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
- **ETSI TS 119 312 V2.1.1 (2026-06)** (Cryptographic Suites). `fonte_id=25`.
Documento **non multi-parte** (nessun prefisso di parte nei `riferimento`).
Import 2026-09-28 via `app/tools/split_source.py` + 4 subagent paralleli (38
pagine di testo + annessi A-D), moduli `app/seed_data/etsi_119_312/cap0[1-4].py`
(cap01 clausole 1-4; cap02 clausole 5-6; cap03 clausole 7-8; cap04 clausole
9-10 + annessi A-D, perché il file assegnato arriva a fine documento; Annex E
Bibliography e History esclusi come paratesto). 57 nodi (42 obblighi, 15
principi), 57 item di indice. **Questa fonte non ha id di requisito nel
testo**: la granularità è quindi di clausola/sottoclavola numerata, a
differenza di ETSI TS 119 101 e di ETSI EN 319 102-1 che usano requirement id
propri. Il front matter è stato tagliato prima dello split (`body.txt`),
perché l'indice del documento ripete i titoli dei capitoli e avrebbe reso
ambigui i marker. Peculiarità: il documento è molto citato *verso l'interno*
(48 occorrenze di sé stesso) e cita solo IETF RFC, FIPS, ISO/IEC e standard
ETSI non censiti (EN 319 122/132/142, TS 101 733/903, TS 102 778, TS 102
176-1): **zero relazioni native**. Il valore dell'import è tutto nel giro
inverso: **21 relazioni "richiama"** in `cap05_relazioni_cross.py`, dalle
fonti già censite verso questa — 20 nodi in 7 Fonti (7, 10, 11, 17, 18, 19,
21) la richiamavano e quei rinvii restavano muti per assenza di nodo
controparte. È il caso che l'ADR-0009 non copre (la sua pipeline guarda solo
"fonte nuova → fonti esistenti"); lo stesso fenomeno già visto con il Codice
Civile, qui in scala molto maggiore. Gli agganci sono **per contenuto, non per
numero**: le citazioni più vecchie usano la numerazione V1.x (annessi A.8/A.9,
clausola 11) mentre la V2.1.1 ha rinumerato in clausole 5, 6, 7, 9 e 10 — solo
le lunghezze di chiave conservano lo stesso numero (9.3). Tabella di mappatura
completa, proposte scartate e limite noto nel docstring del modulo.
- **ETSI TS 119 101 V1.1.1 (2016-03)** (Policy and security requirements for
applications for signature creation and signature validation). `fonte_id=26`.
Documento **non multi-parte**. Import 2026-09-28 via `split_source.py` + 4
subagent paralleli (42 pagine), moduli `app/seed_data/etsi_119_101/cap0[1-5].py`
(cap01 clausole 1-4; cap02 clausole 5-7; cap03 clausola 8; cap04 clausole 9-10
+ Annex A; cap05 capitolo virtuale di Fase 6). 275 nodi (204 obblighi, 71
principi), 275 item di indice, front matter tagliato prima dello split.
**Granularità a id di controllo, non a clausola**: questa fonte numera le
proprie prescrizioni con id propri (UI, GSM, SC, PD, APD, ISMS, NP, ISP, SIA,
DSS, EL nelle clausole 5-7; SCP 1-94, SVP 1-23, SAP 1-9 nella clausola 8; SDM
e TC nelle clausole 9-10) e ciascuno ha destinatario e forza deontica propri, a
differenza di ETSI TS 119 312 che non ha id. I blocchi "Control objective"
(privi di id) e le sottoclavole senza controlli sono nodi Principio con
riferimento sintetico. La decisione è stata presa in corso d'opera su
richiesta di due subagent della stessa fonte e applicata **retroattivamente**
a cap04, che era stato scritto a granularità di clausola: senza di essa la
Fonte sarebbe risultata internamente disomogenea. 14 relazioni "richiama" nel
solo giro **inverso** (`cap05_relazioni_cross.py`): 9 nodi della Fonte 11
(ETSI TS 119 431 Parte 2) citano questa norma e sei lo fanno **per id di
controllo** (`UI 1`, `UI 2`, `SCP 13`, `SCP 14`, `SCP 31`, `SCP 37`, `SCP 47`,
`SCP 61`, `GSM 1.2`, `GSM 1.3`, `GSM 1.4`, `GSM 2.4`) — è il motivo per cui la
granularità a id non è un dettaglio redazionale ma la condizione perché quei
rinvii trovino un bersaglio puntuale. Per questa Fonte **non** è stato eseguito
il giro KNN in direzione diretta: su 275 nodi lo shortlist è dominato dal
lessico comune degli standard ETSI e non da corrispondenze prescrittive; il
limite è dichiarato nel docstring del modulo invece di essere mascherato da
un elenco di proposte scartate.
- **ETSI EN 319 102-1 V1.4.1 (2024-06)** (Procedures for Creation and
Validation of AdES Digital Signatures; Parte 1: Creation and Validation).
`fonte_id=27`. Documento **multi-parte** di cui è censita la sola Parte 1.
Import 2026-09-28, il più esteso del lotto (88 pagine): front matter tagliato
prima dello split, 8 capitoli via `split_source.py` e 8 subagent in due lotti
(la clausola 5 è spaccata in cinque capitoli: 5.1 / 5.2 / 5.3-5.4 / 5.5 /
5.6), moduli `app/seed_data/etsi_319_102/cap0[1-9].py`. 136 nodi (**94
obblighi, 42 principi**), 136 item di indice. Annex D (Change history) e la
sezione History esclusi come paratesto editoriale (decisione presa in corso
d'opera su richiesta del subagent di cap08). **9 relazioni "richiama"** nel solo
giro inverso (`cap09_relazioni_cross.py`): nodi delle Fonti 9, 19 e 20 citano
questa norma, e due di essi la citano con il risultato di convalida
(TOTAL-PASSED) definito dallo standard; Fonte 20 lo cita una volta con
riferimento **puntuale di sottoclavola** («Figure 1 (derived from ETSI EN 319
102-1, clause 4.2.1)»). Terzo caso del lotto di relazioni inverse, dopo Fonti
25 e 26.
  - **Nota sul prefisso di parte**: i `riferimento` di questa Fonte non portano
    `"Parte 1: "`, a differenza di ETSI EN 319 412/TS 119 431/EN 319 411. È una
    decisione documentata (sezione "Decisione presa in corso d'import" di
    `docs/plan-import-lotto-eidas2-standard.md`): con una sola Parte nella Fonte
    non esiste ambiguità, e il prefisso va aggiunto — su questi 8 moduli, sul
    capitolo di Fase 6 e sui riferimenti a Fonte 27 in altre Fonti — se e quando
    si importerà TS 119 102-2 nella stessa Fonte.
  - **Criterio di classificazione delle clausole con tabella "Requirement"**
    (deciso con l'utente il 2026-09-28, applicato su cap04 e cap07): una clausola
    la cui tabella ha la colonna `Requirement` (Mandatory/Optional) è
    prescrittiva sul processo e va censita come Obbligo "tecnico/sicurezza"
    anche senza `shall` esplicito; restano Principio le clausole dichiarative o
    di interfaccia senza quella colonna. La Fonte era internamente incoerente
    (cap05/cap06 Obbligo, cap04/cap07 Principio sulle stesse tabelle, verificato
    su 5.2.2.2 e 5.3.2): 12 clausole sono state riclassificate — 7 "Inputs" di
    cap04 (5.2.2.2-5.2.8.2) e 5 "Input" di cap07 (5.6.2.1.2-5.6.3.2). Le guardie
    di copertura **non** rilevano questo tipo di incoerenza: verificano che ogni
    item sia coperto, non che i criteri di classificazione siano omogenei.
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
| Internazionali | eIDAS, eIDAS2, Reg. (UE) 2025/1566, Reg. (UE) 2025/1567, Reg. (UE) 2025/1569, Reg. (UE) 2025/2531, Reg. (UE) 2025/2532, Reg. (UE) 2015/1502, Reg. (UE) 2024/2979, Reg. (UE) 2024/482 (EUCC), Reg. (UE) 2024/3144 (atto modificativo) | 11 |
| Nazionali | CAD, DPCM 22/2/2013, DPCM 24/10/2014, DPCM 19/10/2021, Reg. AgID modalità attuative SPID, Regole Tecniche AgID certificati qualificati 13/2/2020, Codice Civile (selettivo) | 7 |
| Locali | — | 0 |
| Standard tecnici | ETSI EN 319 412 (5 Parti, Fonte unica), ETSI TS 119 461, ETSI EN 319 401, ETSI TS 119 431 (2 Parti, Fonte unica), ETSI EN 319 411 (2 Parti, Fonte unica), ETSI EN 319 421, ETSI EN 319 422, ETSI TS 119 432, ETSI TS 119 612, ETSI TS 119 312, ETSI TS 119 101, ETSI EN 319 102-1, ETSI EN 319 122-1 (CAdES), ETSI EN 319 132-1 (XAdES) | 14 |
| **Totale** | | **32** |

31 delle 32 Fonti hanno copertura granulare completa (ADR-0007) e sono
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
