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

- **ETSI EN 319 412-5 V2.5.1** (QCStatements). `fonte_id=7`. Import
  2026-09-21, 1 capitolo (`app/seed_data/etsi_319_412_5/cap01.py`, 21
  pagine). 5 relazioni cross verso eIDAS/eIDAS2 (mapping Annex A →
  Allegati I/III/IV, citazione esplicita art. 24 eIDAS2) e DPCM 22/2/2013
  (OID id-etsi-qcs-QcSSCD, artt. 13/42) — `cap02_relazioni_cross.py`.
  Sede del troncamento verbatim scoperto in `testo_integrale` che ha
  originato ADR-0010 (vedi `CLAUDE.md`).
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
- **ETSI TS 119 431-1 V1.3.1** (TSP che operano un QSCD/SCDev remoto).
  `fonte_id=11`. Import 2026-09-22, 2 capitoli
  (`app/seed_data/etsi_119_431_1/cap0[1-2].py`, 31 pagine), 159 item di
  indice, 23 relazioni interne. Censita come Fonte autonoma e indipendente
  da ETSI TS 119 431-2 su richiesta esplicita dell'utente, pur essendo due
  Parti dello stesso deliverable multi-parte — `cap03_relazioni_cross.py`.
- **ETSI TS 119 431-2 V1.2.1** (componenti TSP a supporto della creazione
  di firme AdES). `fonte_id=12`. Import 2026-09-22, 2 capitoli
  (`app/seed_data/etsi_119_431_2/cap0[1-2].py`, 26 pagine), 95 item di
  indice, 41 relazioni interne (1 cross-capitolo verso cap01 di questa
  stessa Fonte). Relazioni cross reciproche con ETSI TS 119 431-1 inserite
  solo dopo che entrambe le Fonti erano nel registro simbolico —
  `cap03_relazioni_cross.py`.

## Riepilogo

| Categoria | Fonti | Totale |
|---|---|---|
| Internazionali | eIDAS, eIDAS2, Reg. (UE) 2025/1566, Reg. (UE) 2015/1502 | 4 |
| Nazionali | CAD, DPCM 22/2/2013, DPCM 24/10/2014, DPCM 19/10/2021, Reg. AgID modalità attuative SPID | 5 |
| Locali | — | 0 |
| Standard tecnici | ETSI EN 319 412-5, ETSI TS 119 461, ETSI EN 319 401, ETSI TS 119 431-1, ETSI TS 119 431-2 | 5 |
| **Totale** | | **14** |

Tutte e 14 le Fonti hanno oggi copertura granulare completa e sono
cross-collegate; nessuna resta isola nel grafo.

**Nota di stato repo (2026-09-23)**: l'import delle 8 Fonti aggiunte dopo il
2026-09-21 (codice in `app/seed_data/`, wiring in `app/seed.py`, guardia
`verifica_completezza_testo_integrale` in `app/seed_data/lib.py`, questo
file, `CLAUDE.md`, `CONTEXT.md`) risulta scritto su disco ma non ancora
committato — commit previsto in sessione separata.
