"""Estrazione granulare ETSI TS 119 431-2 V1.2.1 (2023-06) — Capitolo 2/2 (Fonte
12, numerazione definitiva cablata dalla sessione principale in app/seed.py —
questo modulo NON tocca seed.py): clausola 7 "Signature creation application
service management and operation" (OVR-7.1..7.13), clausola 8 "Signature
creation application service component technical requirements" (ASI-8.1,
OVR-8.2), clausola 9 "Framework for definition of signature creation
application service component policy built on a trust service policy defined
in the present document" (OVR-9), Annex A (informativo, Table of contents for
SCASC practice statement), Annex B (normativo, EU specific requirements
related to Regulation (EU) No 910/2014), Annex C (informativo, Mapping to
advance electronic signatures or seals). Testo ufficiale in
app/.source_cache/etsi_119_431_2/cap02.txt (226 righe).

Modellazione (ADR-0007/ADR-0010), stesso criterio già applicato a ETSI TS 119
461 e a ETSI EN 319 401 per questo genere di fonte (standard tecnico ETSI a
requisiti numerati OVR-x.y-nn/ASI-x.y-nn):

- Un nodo Obbligo per ogni requisito numerato (prefissi OVR-/ASI-), categoria
  soggetto "QTSP/gestore", ruolo "obbligato" (il documento tratta il SCASC/
  SCASP come componente del TSP ai fini del censimento). `riferimento` = id
  esatto del requisito, senza il marcatore "[CONDITIONAL]"/"[CONDITONAL]"
  (typo del documento, presente identico in entrambe le forme nel testo
  originale) quando presente — riportato invece in `condizione_applicabilita`
  con la condizione testuale, SOLO per i requisiti effettivamente marcati
  come tali nel testo (non per ogni costrutto "When X, Y shall..." non
  taggato, che resta descrittivo nel solo `testo`/`testo_integrale`, es.
  OVR-7.13-02/03).
- Clausola 7 (24 sottoclausole 7.1-7.13, tutte per rinvio a ETSI EN 319 401):
  ogni sottoclausola ha un requisito base "OVR-7.X-01: i requisiti di
  clausola 7.X di EN 319 401 si applicano", talvolta seguito da uno o più
  requisiti particolari con id proprio (es. OVR-7.6-02, OVR-7.7-02..04,
  OVR-7.10-02..06, OVR-7.11-02..03, OVR-7.13-02..04) imposti in aggiunta:
  ciascuno è un nodo separato (mai un unico nodo per sottoclausola), con
  testo_integrale segmentato esattamente al confine tra un id e il successivo
  (nessun contenuto perso o duplicato tra nodi contigui). `tipo_obbligo`
  assegnato per coerenza con la tipizzazione già usata per le stesse
  sottoclausole nel capitolo di ETSI EN 319 401 di questo censimento
  (app/seed_data/etsi_319_401/cap03-05.py): "organizzativo" per 7.1
  (Internal organization), 7.2 (Human resources), 7.3 (Asset management),
  7.11 (Business continuity), 7.12 (Termination), 7.13-01/02/04 (Compliance);
  "tecnico/sicurezza" per 7.4 (Access control), 7.5 (Cryptographic
  controls), 7.6 (Physical/environmental security), 7.7 (Operation
  security), 7.8 (Network security), 7.9 (Incident management);
  "di conservazione" per 7.10 (Collection of evidence) e per OVR-7.13-03
  (non conservare i dati da firmare dopo l'elaborazione quando non
  necessario, stessa natura di conservazione/log-retention di clausola
  7.10).
- Clausola 8.1 "Interface" (ASI-8.1-01..12): requisiti tecnici
  sull'interfaccia del SCASC, in gran parte condizionati dal costrutto
  "[CONDITIONAL] When the SCASC presents the document to the signer, ...".
  ASI-8.1-04 nel testo ufficiale porta l'id refuso "ASI-8-1-04" (trattino al
  posto del punto, unico caso nella serie ASI-8.1-xx): `riferimento`
  normalizzato a "Parte 2: ASI-8.1-04" per coerenza con gli id contigui e per la
  risolvibilità delle relazioni interne; il refuso originale è preservato
  verbatim in `testo_integrale` (che riporta l'id così come stampato nel
  documento, "ASI-8-1-04:"), nessuna informazione persa. `tipo_obbligo`:
  "tecnico/sicurezza" per i requisiti di sicurezza/funzionamento
  dell'interfaccia (01, 02, 06, 07, 08, 09, 10); "procedurale" per i
  requisiti che impongono di descrivere/dichiarare qualcosa nella practice
  statement o nei termini e condizioni (03, 04, 05); "di conservazione" per
  i due requisiti di logging (11, 12).
- Clausola 8.2 "AdES digital signature creation" (OVR-8.2-01..09, incluso il
  requisito con suffisso di lettera OVR-8.2-08A introdotto tra 08 e 09):
  "tecnico/sicurezza" per i requisiti di integrità/riservatezza/crittografia
  (01, 02, 03, 04, 06); "informativo/trasparenza" per i requisiti che
  impongono di rendere nota al firmatario un'informazione (05, 07, 08);
  "procedurale" per i requisiti sulla consegna dell'output al firmatario
  (08A, 09). La NOTE 3 sotto OVR-8.2-09 dichiara esplicitamente che
  "OVR-8.2-09 follows directly from OVR-8.2-08A" quando la firma è
  enveloped/enveloping rispetto ai dati firmati: relazione "specifica"
  OVR-8.2-09 -> OVR-8.2-08A, evidence_type "textual" (citazione esplicita di
  entrambi gli id).
- Clausola 9: il NOTE introduttivo (prima di OVR-9-01) definisce il concetto
  cardine dell'intera clausola — la policy SCASC "costruita su" (built on)
  una trust service policy del presente documento, distinta dall'uso diretto
  delle policy di clausola 4.2.2 — enunciato normativo/definitorio autonomo
  non assorbito in nessun requisito numerato: 1 Principio "definitorio",
  riferimento "Parte 2: 9 (nota introduttiva)" (ADR-0007, disposizione di cornice con
  contenuto sostanziale proprio). OVR-9-01 ("Void.") ESCLUSO dall'indice:
  segnaposto redazionale privo di contenuto proprio (stesso trattamento
  riservato ai requisiti "Void" nelle fonti precedenti, es. ETSI TS 119 461).
  OVR-9-01A e OVR-9-02..10 sono dieci requisiti, tutti condizionati dallo
  stesso costrutto "[CONDITIONAL] When building a SCASC policy on a trust
  service policy defined in the present document" (stessa
  condizione_applicabilita per tutti e dieci) — un elenco di prescrizioni
  puntuali di governance della policy (identificazione della base,
  variazioni, informativa ai sottoscrittori, organo di approvazione, risk
  assessment, processo di revisione, disponibilità pubblica delle policy e
  delle revisioni, OID) modellato con relazioni "specifica" (inferred, nessun
  id citato esplicitamente) da ciascuno di OVR-9-02..10 verso OVR-9-01A (il
  requisito che introduce l'obbligo-base di identificare la policy adottata
  come riferimento), più "specifica" (inferred, confidence 0.7) da OVR-9-01A
  verso il Principio introduttivo "Parte 2: 9 (nota introduttiva)" che ne definisce il
  concetto. `tipo_obbligo`: "organizzativo" per la generalità dei dieci
  (governance/documentazione della policy); "informativo/trasparenza" per i
  tre che impongono di informare/rendere disponibile qualcosa a sottoscrittori
  o utenti (OVR-9-03, OVR-9-08, OVR-9-09).
- Annex A (informativo, "Table of contents for SCASC practice statement"):
  è un indice/modello di struttura raccomandata per la dichiarazione delle
  pratiche del SCASC (3 sezioni, ~30 sottovoci), MA non è paratesto puro come
  un sommario o una tabella di cronologia — contiene passaggi discorsivi con
  contenuto normativo/interpretativo autonomo non altrove censito (es. 1.4.3:
  elenco dei documenti minimi che il TSP deve avere e brevemente descrivere;
  2.1: rinvio esplicito a EN 319 401; 3.1/3.2: collegamento esplicito alle
  clausole 8.1/8.2 del presente documento). Trattato come UN solo Principio
  aggregato, tipo "altro", riferimento "Parte 2: Annex A", che riassume la struttura e
  la funzione dell'annesso senza creare un nodo per ogni sottovoce dell'indice
  (che duplicherebbe la struttura del documento senza introdurre disposizioni
  proprie) — stesso criterio già applicato in ETSI TS 119 461 (Annex B,
  tabella minaccia/copertura, app/seed_data/etsi_119_461/cap08.py) per un
  annesso informativo con contenuto sostanziale ma privo di righe
  singolarmente normative.
- Annex B (normativo, "EU specific requirements related to Regulation (EU)
  No 910/2014..."): 3 Obblighi (OVR-B.1-01..03), tipo_obbligo
  "tecnico/sicurezza" (contenuto del certificato di firma usato per creare
  la firma/il sigillo elettronico avanzato). Il NOTE introduttivo
  dell'annesso ("This clause aims at providing best practices...") è breve e
  meramente di scopo: assorbito nel testo_integrale di OVR-B.1-01 (primo
  requisito che segue), non genera un nodo a sé (a differenza del NOTE di
  clausola 9, sostanzialmente più esteso e definitorio di un concetto
  autonomo).
- Annex C (informativo, "Mapping to advance electronic signatures or seals
  as by Regulation (EU) No 910/2014"): tre tabelle (C.1 firma avanzata art.
  26, C.2 sigillo avanzato art. 36, C.3 validazione QES art. 32 §1) che
  mappano requisiti già censiti (OVR-B.1-01..03, OVR-8.2-02, OVR-8.2-04) sui
  singoli alinea degli articoli eIDAS corrispondenti. Nessun nodo per riga di
  tabella (duplicherebbe i nodi Obbligo già censiti in Annex B/clausola 8.2):
  UN solo Principio aggregato, tipo "altro", riferimento "Parte 2: Annex C",
  oggetti_giuridici ["firma elettronica avanzata", "sigillo elettronico
  avanzato"], con 6 relazioni "richiama" (evidence_type "textual", citazione
  esplicita dell'id in tabella) verso OVR-B.1-01, OVR-B.1-02, OVR-B.1-03,
  OVR-8.2-02, OVR-8.2-04 e OVR-6.2-05. Quest'ultimo è un riferimento del
  capitolo 1 di questa stessa fonte (clausola 6.2, non assegnata a questo
  capitolo), citato letteralmente "(OVR-6.2-05)" nella NOTA ricorrente sotto
  le tabelle C.1/C.2: relazione cross-capitolo verificata leggendo
  app/seed_data/etsi_119_431_2/cap01.py (completato da Etsi431_2Cap01 durante
  questo stesso import), dove "Parte 2: OVR-6.2-05" è confermato come riferimento
  esatto — nodo_a risolto con `("obbligo", None, "Parte 2: OVR-6.2-05")`, che risolve
  automaticamente alla fonte corrente indipendentemente dal capitolo. Le
  lettere (a)-(f) di Tabella C.3 sono dichiarate "Not applicable, specific to
  the qualified case"/"...responsibility of the CA" dal documento stesso:
  nessun requisito viene da esse introdotto, sono parte del riassunto
  descrittivo del nodo aggregato, non di righe a sé.
- Annex D (informativo, "Change history") ED il blocco finale "History" /
  "Document history" (dopo Annex D, senza propria lettera di annesso) sono
  ESCLUSI dall'indice: entrambi sono paratesto editoriale puro (tabella di
  cronologia delle versioni del documento, senza alcun contenuto normativo),
  stesso trattamento già riservato ai blocchi "History"/"Change history" di
  tutte le fonti ETSI precedenti di questo censimento (EN 319 401, TS 119
  461, EN 319 412-5).
- Nessuna relazione cross-fonte in questo import (demandate alla pipeline di
  Fase 6/ADR-0009 eseguita dalla sessione principale, inclusa l'eventuale
  relazione verso ETSI TS 119 431-1, verso EN 319 401 e verso eIDAS/eIDAS2).
  L'unica relazione verso il capitolo 1 di questa stessa fonte (Annex C ->
  OVR-6.2-05) è stata verificata contro il file cap01.py effettivamente
  scritto, non ipotizzata.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "Parte 2: OVR-7.1-01",
        "testo": "Si applicano al SCASC i requisiti di cui alla clausola 7.1 di ETSI EN 319 401 (Organizzazione interna).",
        "testo_integrale": "OVR-7.1-01: The requirements specified in ETSI EN 319 401 [9], clause 7.1 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.2-01",
        "testo": "Si applicano al SCASC i requisiti di cui alla clausola 7.2 di ETSI EN 319 401 (Risorse umane).",
        "testo_integrale": "OVR-7.2-01: The requirements specified in ETSI EN 319 401 [9], clause 7.2 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.3-01",
        "testo": "Si applicano al SCASC i requisiti di cui alla clausola 7.3 di ETSI EN 319 401 (Gestione degli asset).",
        "testo_integrale": "OVR-7.3-01: The requirements specified in ETSI EN 319 401 [9], clause 7.3 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.4-01",
        "testo": "Si applicano al SCASC i requisiti di cui alla clausola 7.4 di ETSI EN 319 401 (Controllo degli accessi).",
        "testo_integrale": "OVR-7.4-01: The requirements specified in ETSI EN 319 401 [9], clause 7.4 shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.5-01",
        "testo": "Si applicano al SCASC i requisiti di cui alla clausola 7.5 di ETSI EN 319 401 (Controlli crittografici).",
        "testo_integrale": "OVR-7.5-01: The requirements specified in ETSI EN 319 401 [9], clause 7.5 shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.6-01",
        "testo": "Si applicano al SCASC i requisiti di cui alla clausola 7.6 di ETSI EN 319 401 (Sicurezza fisica e ambientale); in aggiunta si applica il requisito particolare OVR-7.6-02.",
        "testo_integrale": "OVR-7.6-01: The requirements specified in ETSI EN 319 401 [9], clause 7.6 shall apply. In addition the following particular requirement apply:",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.6-02",
        "testo": "Alla SCA (signature creation application) si applica il requisito GSM 1.4 di cui alla clausola 5.2 di ETSI TS 119 101.",
        "testo_integrale": "OVR-7.6-02: The following requirement specified in ETSI TS 119 101 [1], clause 5.2 shall apply to the SCA: GSM 1.4.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.7-01",
        "testo": "Si applicano al SCASC i requisiti di cui alla clausola 7.7 di ETSI EN 319 401 (Sicurezza operativa); in aggiunta si applicano i requisiti particolari OVR-7.7-02, OVR-7.7-03 e OVR-7.7-04.",
        "testo_integrale": "OVR-7.7-01: The requirements specified in ETSI EN 319 401 [9], clause 7.7 shall apply. In addition, the following particular requirements apply:",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.7-02",
        "testo": "Alla SCA dovrebbero applicarsi i requisiti GSM 1.2 e GSM 1.3 di cui alla clausola 5.2 di ETSI TS 119 101.",
        "testo_integrale": "OVR-7.7-02: The following requirements specified in ETSI TS 119 101 [1], clause 5.2 should apply to the SCA: GSM 1.2 and GSM 1.3.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.7-03",
        "testo": "Alla SCA si applica il requisito GSM 2.4 di cui alla clausola 5.2 di ETSI TS 119 101.",
        "testo_integrale": "OVR-7.7-03: The following requirements specified in ETSI TS 119 101 [1], clause 5.2 shall apply to the SCA: GSM 2.4.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.7-04",
        "testo": "Il SCASC deve implementare tutti i requisiti obbligatori di ETSI TS 119 101 sopra richiamati, indipendentemente dal fatto che il requisito sia imposto alla DA (Driving Application) o alla SCA.",
        "testo_integrale": "OVR-7.7-04: The SCASC shall implement all mandatory requirements from ETSI TS 119 101 [1] referenced above regardless of whether the requirement is imposed on the DA or the SCA.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.8-01",
        "testo": "Si applicano al SCASC i requisiti di cui alla clausola 7.8 di ETSI EN 319 401 (Sicurezza di rete).",
        "testo_integrale": "OVR-7.8-01: The requirements specified in ETSI EN 319 401 [9], clause 7.8 shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.9-01",
        "testo": "Si applicano al SCASC i requisiti di cui alla clausola 7.9 di ETSI EN 319 401 (Gestione degli incidenti).",
        "testo_integrale": "OVR-7.9-01: The requirements specified in ETSI EN 319 401 [9], clause 7.9 shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.10-01",
        "testo": "Si applicano al SCASC i requisiti di cui alla clausola 7.10 di ETSI EN 319 401 (Raccolta delle evidenze); in aggiunta si applicano i requisiti particolari OVR-7.10-02..06.",
        "testo_integrale": "OVR-7.10-01: The requirements specified in ETSI EN 319 401 [9], clause 7.10 shall apply. In addition the following particular requirements apply:",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.10-02",
        "testo": "Ogni operazione di creazione di firma digitale AdES deve essere registrata (logged), insieme all'identificazione del sottoscrittore quando tale informazione è nota.",
        "testo_integrale": "OVR-7.10-02: Any AdES digital signature creation operation shall be logged, together with identification of the subscriber when this information is known.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.10-03",
        "testo": "I log degli eventi devono riportare l'orario dell'evento.",
        "testo_integrale": "OVR-7.10-03: Event logs shall be marked with the time of the event.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.10-04",
        "testo": "La frequenza di elaborazione, il periodo di conservazione, la protezione, le procedure di backup del sistema di raccolta, le procedure di archiviazione e la valutazione delle vulnerabilità dei log degli eventi devono essere documentati nella dichiarazione delle pratiche (practice statement) del SCASC.",
        "testo_integrale": "OVR-7.10-04: The frequency of processing, the retention period, the protection, the back-up procedures of the collection system, the archiving procedures and the vulnerability assessment of the event logs shall be documented in the SCASC practice statement.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.10-05",
        "testo": "L'attuazione dei requisiti OVR-7.10-01 e OVR-7.10-02 deve tenere conto dei requisiti applicabili in materia di privacy.",
        "testo_integrale": "OVR-7.10-05: The implementation of requirements OVR-7.10.1 and OVR-7.10.2 shall take the applicable privacy requirements into account.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.10-06",
        "testo": "I log degli eventi dovrebbero includere il tipo di evento, l'esito (successo o fallimento) dell'evento e un identificatore della persona e/o del componente all'origine dell'evento.",
        "testo_integrale": "OVR-7.10-06: Event logs should include the type of the event, the event success or failure, and an identifier of the person and/or component at the origin for such an event.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.11-01",
        "testo": "Si applicano al SCASC i requisiti di cui alla clausola 7.11 di ETSI EN 319 401 (Gestione della continuità operativa); in aggiunta, per garantire la continuità operativa come specificato nei termini e condizioni, si applicano i requisiti particolari OVR-7.11-02 e OVR-7.11-03.",
        "testo_integrale": "OVR-7.11-01: The requirements specified in ETSI EN 319 401 [9], clause 7.11 shall apply. In addition, in order to provide business continuity as specified in the terms and conditions the following particular requirements apply:",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.11-02",
        "testo": "Dovrebbero essere implementate misure per evitare interruzioni del servizio dovute a comportamenti intenzionali o non intenzionali di utenti o terze parti.",
        "testo_integrale": "OVR-7.11-02: Measures should be implemented to avoid interruptions of the service due to intentional or unintentional behaviour of users or third parties.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.11-03",
        "testo": "Quando vengono aggiunte marche temporali alla firma, lo SLA del SCASP dovrebbe tenere conto dello SLA della corrispondente TSA (Time-Stamping Authority).",
        "testo_integrale": "OVR-7.11-03: [CONDITIONAL] When adding time-stamps to the signature, the SLA of the SCASP should take the SLA of the corresponding TSA into account.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando vengono aggiunte marche temporali (time-stamp) alla firma",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.12-01",
        "testo": "Si applicano al SCASC i requisiti di cui alla clausola 7.12 di ETSI EN 319 401 (Cessazione e piani di cessazione).",
        "testo_integrale": "OVR-7.12-01: The requirements specified in ETSI EN 319 401 [9], clause 7.12 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.13-01",
        "testo": "Si applicano al SCASC i requisiti di cui alla clausola 7.13 di ETSI EN 319 401 (Conformità e requisiti legali); in aggiunta si applicano i requisiti particolari OVR-7.13-02..04.",
        "testo_integrale": "OVR-7.13-01: The requirements specified in ETSI EN 319 401 [9], clause 7.13 shall apply. In addition, the following particular requirements apply:",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.13-02",
        "testo": "Quando i dati personali sono trattati da una terza parte, se richiesto dalla legge, deve essere stipulato un accordo appropriato con i responsabili del trattamento terzi dei dati personali per assicurare che rispettino i requisiti legali, incluse misure tecniche, organizzative e legali a protezione dei dati personali (i dati da firmare sono considerati dati personali).",
        "testo_integrale": "OVR-7.13-02: When personal data is processed by a third party, if needed by the law, an appropriate agreement shall be made with third party processors of personal data in order to ensure that they do comply with the legal requirements, including the implementation of technical, organizational and legal measures to protect the personal data. NOTE 1: The data to be signed is to be considered as personal data.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.13-03",
        "testo": "Il SCASC non deve conservare i dati da firmare (SD) dopo l'elaborazione, quando non necessario (fermo restando che, se il SCASP opera in combinazione con un servizio di conservazione, può sussistere la necessità di conservare tali dati).",
        "testo_integrale": "OVR-7.13-03: The SCASC shall not store the SD after processing when not necessary. NOTE 2: If the SCASP works in combination of a preservation service there can be a need to keep such data.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.13-04",
        "testo": "Il SCASP ha la responsabilità complessiva di soddisfare i requisiti definiti nelle clausole da 5 a 8, anche quando alcune o tutte le sue funzionalità sono svolte da subappaltatori.",
        "testo_integrale": "OVR-7.13-04: The SCASP shall have the overall responsibility for meeting the requirements defined in clauses 5 to 8 even when some or all of its functionalities are undertaken by sub-contractors.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: ASI-8.1-01",
        "testo": "Quando il SCASC dispone di un'interfaccia accessibile a macchina per contattare il proprio servizio, dovrebbe usare il protocollo definito in ETSI TS 119 432.",
        "testo_integrale": "ASI-8.1-01: [CONDITONAL] When the SCASC has a machine accessible interface to contact its service, it should use the protocol defined in ETSI TS 119 432 [i.9].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando il SCASC dispone di un'interfaccia accessibile a macchina (machine accessible interface) per contattare il proprio servizio",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: ASI-8.1-02",
        "testo": "La connessione tra il SCASC e lo SCDev utilizzato per la creazione del valore della firma digitale deve essere protetta.",
        "testo_integrale": "ASI-8.1-02: The connection between the SCASC and the SCDev used for creation of the digital signature value shall be secured.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: ASI-8.1-03",
        "testo": "Quando il SCASC presenta il documento al firmatario, deve descrivere nella propria dichiarazione delle pratiche (practice statement) come garantisce il principio What You See Is What You Sign (WYSIWYS).",
        "testo_integrale": "ASI-8.1-03: [CONDITIONAL] When the SCASC presents the document to the signer, it shall describe in its SCASC practice statement how it guarantees that What You See Is What You Sign (WYSIWYS).",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando il SCASC presenta il documento al firmatario",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: ASI-8.1-04",
        "testo": "Quando il SCASC presenta il documento al firmatario in forma interpretata, la dichiarazione delle pratiche deve indicare chiaramente come interpreta i dati specifici (es. per un documento in formato XML, quale software è usato per la presentazione o quali regole sono seguite per presentare i diversi tag XML).",
        "testo_integrale": "ASI-8-1-04: [CONDITIONAL] When the SCASC presents the document to the signer in an interpreted way, the SCASC practice statement shall clearly state how it interprets specific data. EXAMPLE: The document to be signed is XML format, and the practice statement states which software is used for the presentation or which rules are followed to present the different XML tags.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando il SCASC presenta il documento al firmatario in forma interpretata",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: ASI-8.1-05",
        "testo": "Quando il SCASC presenta il documento al firmatario, la dichiarazione delle pratiche o i termini e condizioni devono indicare quali tipi di contenuto possono essere presentati correttamente.",
        "testo_integrale": "ASI-8.1-05: [CONDITIONAL] When the SCASC presents the document to the signer, the SCASC practice statement or the terms and conditions shall state which content types can be correctly presented.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando il SCASC presenta il documento al firmatario",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: ASI-8.1-06",
        "testo": "Quando il SCASC presenta il documento al firmatario, l'interfaccia deve avvisare il firmatario se non è in grado di presentare accuratamente tutte le parti dei dati da firmare (SD) in base al tipo di contenuto dei dati.",
        "testo_integrale": "ASI-8.1-06: [CONDITIONAL] When the SCASC presents the document to the signer, the interface shall warn the signer if it cannot accurately present all parts of the SD according to the data content type.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando il SCASC presenta il documento al firmatario",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: ASI-8.1-07",
        "testo": "Quando il SCASC fornisce un'interfaccia utente grafica al client, dovrebbero applicarsi i requisiti UI 1 e UI 2 di ETSI TS 119 101.",
        "testo_integrale": "ASI-8.1-07: [CONDITIONAL] When the SCASC provides a graphical user interface to the client the requirements UI 1 and UI 2 from ETSI TS 119 101 [1] should apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando il SCASC fornisce un'interfaccia utente grafica (graphical user interface) al client",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: ASI-8.1-08",
        "testo": "Quando il SCASC presenta il documento al firmatario, deve prevedere un workflow in cui sia chiaro al firmatario che egli acconsente alla firma del documento.",
        "testo_integrale": "ASI-8.1-08: [CONDITIONAL] When the SCASC presents the document to the signer, it shall have a workflow where it is clear to the signer that the signer consents to the signing of the document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando il SCASC presenta il documento al firmatario",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: ASI-8.1-09",
        "testo": "Quando il SCASC presenta il documento al firmatario, si applicano SCP 13 e SCP 47 di ETSI TS 119 101.",
        "testo_integrale": "ASI-8.1-09: [CONDITIONAL] When the SCASC presents the document to the signer, SCP 13 and SCP 47 of ETSI TS 119 101 [1] shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando il SCASC presenta il documento al firmatario",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: ASI-8.1-10",
        "testo": "Quando il SCASC presenta il documento al firmatario, dovrebbe consentire di scaricare il documento da firmare.",
        "testo_integrale": "ASI-8.1-10: [CONDITIONAL] When the SCASC presents the document to the signer, the SCASC should allow to download the document to be signed.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando il SCASC presenta il documento al firmatario",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: ASI-8.1-11",
        "testo": "Quando il SCASC presenta il documento al firmatario, dovrebbe registrare (log) per quanto tempo il documento è stato presentato al firmatario.",
        "testo_integrale": "ASI-8.1-11: [CONDITIONAL] When the SCASC presents the document to the signer, the SCASC should log for how long the document was presented to the signer.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando il SCASC presenta il documento al firmatario",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: ASI-8.1-12",
        "testo": "Quando il SCASC presenta il documento al firmatario e il documento è stato scaricato, dovrebbe registrare (log) tale evento.",
        "testo_integrale": "ASI-8.1-12: [CONDITIONAL] When the SCASC presents the document to the signer and the document was downloaded, the SCASC should log such an event.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando il SCASC presenta il documento al firmatario e il documento è stato scaricato",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-8.2-01",
        "testo": "Il SCASC deve garantire l'integrità e la riservatezza delle informazioni ricevute.",
        "testo_integrale": "OVR-8.2-01: The SCASC shall guarantee the integrity and confidentiality of the received information.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-8.2-02",
        "testo": "Gli algoritmi crittografici utilizzati dovrebbero essere selezionati tra quelli raccomandati da ETSI TS 119 312 (le raccomandazioni di tale standard possono essere superate da raccomandazioni nazionali).",
        "testo_integrale": "OVR-8.2-02: The cryptographic algorithms used should be selected from algorithms recommended by ETSI TS 119 312 [i.5]. NOTE 1: Cryptographic suites recommendations defined in ETSI TS 119 312 [i.5] can be superseded by national recommendations.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-8.2-03",
        "testo": "Gli algoritmi crittografici applicati devono essere quelli definiti nella signature creation policy.",
        "testo_integrale": "OVR-8.2-03: The cryptographic algorithms applied shall be as defined in signature creation policy.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-8.2-04",
        "testo": "Si applicano SCP 14, SCP 31, SCP 37 e SCP 61 di ETSI TS 119 101.",
        "testo_integrale": "OVR-8.2-04: SCP 14, SCP 31, SCP 37 and SCP 61 of ETSI TS 119 101 [1] shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-8.2-05",
        "testo": "Il SCASC deve informare il firmatario del tipo di impegno (commitment type); tale informazione può essere fornita all'interno della signature policy.",
        "testo_integrale": "OVR-8.2-05: The SCASC shall inform the signer of the commitment type. NOTE 2: This information can be given within the signature policy.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-8.2-06",
        "testo": "Il SCASC dovrebbe includere la catena del certificato di firma nella firma.",
        "testo_integrale": "OVR-8.2-06: The SCASC should include the signing certificate chain into the signature.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-8.2-07",
        "testo": "Il firmatario deve poter conoscere quale signature creation policy sarà applicata.",
        "testo_integrale": "OVR-8.2-07: The signer shall be able to know which signature creation policy will be applied.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-8.2-08",
        "testo": "Il firmatario deve poter conoscere quale signature creation policy è stata applicata al momento della creazione di una specifica firma (tale informazione può risultare, ad esempio, dall'account utente del firmatario, essere aggiunta come attributo firmato alla firma, oppure derivare dal fatto che il SCASP dispone di una sola policy in vigore in ogni momento).",
        "testo_integrale": "OVR-8.2-08: The signer shall be able to know which signature creation policy was applied when creating a specific the signature. EXAMPLE 1: The information on which signature creation policy will or was applied for a specific signature can be known from the user account of the signer. EXAMPLE 2: The signature creation policy can be added as a signed attribute to the signature. EXAMPLE 3: The SCASP has only one signature creation policy in force at each time, and from the time of signature it is clear which version applies.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-8.2-08A",
        "testo": "Il SCASC dovrebbe fornire la firma al firmatario.",
        "testo_integrale": "OVR-8.2-08A: The SCASC should provide the signature to the signer.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-8.2-09",
        "testo": "Se il SCASC ha accesso ai dati firmati, dovrebbe fornire i dati firmati insieme alla firma al firmatario (se la firma è enveloped/enveloping rispetto ai dati firmati, OVR-8.2-09 discende direttamente da OVR-8.2-08A).",
        "testo_integrale": "OVR-8.2-09: [CONDITIONAL] If the SCASC has access to the signed data, it should provide the signed data together with the signature to the signer. NOTE 3: In case the signature is enveloped in or enveloping the signed data, OVR-8.2-09 follows directly from OVR-8.2-08A.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando il SCASC ha accesso ai dati firmati (SD)",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-9-01A",
        "testo": "Quando costruisce una policy SCASC su una trust service policy definita nel presente documento, la policy SCASC deve identificare quale delle trust service policy definite nel presente documento adotta come base.",
        "testo_integrale": "OVR-9-01A: [CONDITIONAL] When building a SCASC policy on a trust service policy defined in the present document, the SCASC policy shall identify which of the trust service policies defined in the present document it adopts as the basis.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando la policy del SCASC è costruita su una trust service policy definita nel presente documento (clausola 4.2.2)",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-9-02",
        "testo": "La policy deve identificare le eventuali varianti che sceglie di applicare.",
        "testo_integrale": "OVR-9-02: [CONDITIONAL] When building a SCASC policy on a trust service policy defined in the present document; the policy shall identify any variances it chooses to apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando la policy del SCASC è costruita su una trust service policy definita nel presente documento (clausola 4.2.2)",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-9-03",
        "testo": "I sottoscrittori devono essere informati, nell'ambito dell'attuazione dei termini e condizioni, del modo in cui la policy specifica si aggiunge o limita ulteriormente i requisiti della policy definita nel presente documento.",
        "testo_integrale": "OVR-9-03: [CONDITIONAL] When building a SCASC policy on a trust service policy defined in the present document; subscribers shall be informed, as part of implementing the terms and conditions, of the ways in which the specific policy adds to or further constrains the requirements of the policy as defined in the present document.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando la policy del SCASC è costruita su una trust service policy definita nel presente documento (clausola 4.2.2)",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-9-04",
        "testo": "Deve esistere un organismo (ad es. una policy management authority) con autorità e responsabilità finale per specificare e approvare la policy.",
        "testo_integrale": "OVR-9-04: [CONDITIONAL] When building a SCASC policy on a trust service policy defined in the present document; there shall be a body (e.g. a policy management authority) with final authority and responsibility for specifying and approving the policy.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando la policy del SCASC è costruita su una trust service policy definita nel presente documento (clausola 4.2.2)",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-9-05",
        "testo": "Dovrebbe essere condotta una valutazione del rischio per valutare i requisiti di business e determinare i requisiti di sicurezza da includere nella policy per la comunità e l'ambito di applicabilità dichiarati.",
        "testo_integrale": "OVR-9-05: [CONDITIONAL] When building a SCASC policy on a trust service policy defined in the present document; a risk assessment should be carried out to evaluate business requirements and determine the security requirements to be included in the policy for the stated community and applicability.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando la policy del SCASC è costruita su una trust service policy definita nel presente documento (clausola 4.2.2)",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-9-06",
        "testo": "La policy deve essere approvata e modificata in conformità a un processo di revisione definito, incluse le responsabilità per il suo mantenimento.",
        "testo_integrale": "OVR-9-06: [CONDITIONAL] When building a SCASC policy on a trust service policy defined in the present document; the policy shall be approved and modified in accordance with a defined review process, including responsibilities for maintaining the policy.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando la policy del SCASC è costruita su una trust service policy definita nel presente documento (clausola 4.2.2)",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-9-07",
        "testo": "Deve esistere un processo di revisione definito per assicurare che la policy sia supportata dalle dichiarazioni delle pratiche (practice statement).",
        "testo_integrale": "OVR-9-07: [CONDITIONAL] When building a SCASC policy on a trust service policy defined in the present document; a defined review process shall exist to ensure that the policy is supported by the practices statements.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando la policy del SCASC è costruita su una trust service policy definita nel presente documento (clausola 4.2.2)",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-9-08",
        "testo": "Il TSP dovrebbe rendere disponibili alla propria comunità di utenti le policy supportate dal TSP.",
        "testo_integrale": "OVR-9-08: [CONDITIONAL] When building a SCASC policy on a trust service policy defined in the present document; the TSP should make available the policies supported by the TSP to its user community.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando la policy del SCASC è costruita su una trust service policy definita nel presente documento (clausola 4.2.2)",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-9-09",
        "testo": "Le revisioni delle policy supportate dal TSP dovrebbero essere rese disponibili ai sottoscrittori.",
        "testo_integrale": "OVR-9-09: [CONDITIONAL] When building a SCASC policy on a trust service policy defined in the present document; revisions to policies supported by the TSP should be made available to subscribers.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando la policy del SCASC è costruita su una trust service policy definita nel presente documento (clausola 4.2.2)",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-9-10",
        "testo": "Deve essere ottenuto un identificativo univoco di oggetto (es. OID o URI) per la policy.",
        "testo_integrale": "OVR-9-10: [CONDITIONAL] When building a SCASC policy on a trust service policy defined in the present document; a unique object identifier shall be obtained for the policy (e.g. OID or URI).",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando la policy del SCASC è costruita su una trust service policy definita nel presente documento (clausola 4.2.2)",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-B.1-01",
        "testo": "Quando il SCASC è utilizzato per creare una firma elettronica avanzata, il certificato di firma deve identificare il firmatario.",
        "testo_integrale": "NOTE: This clause aims at providing best practices for the creation of advanced electronic signatures/seals based on X.509 certificates. OVR-B.1-01: [CONDITONAL] Where the SCASC is used to create an advanced electronic signature, the signing certificate shall identify the signatory.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando il SCASC è utilizzato per creare una firma elettronica avanzata",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-B.1-02",
        "testo": "Quando il SCASC è utilizzato per creare un sigillo elettronico avanzato, il certificato di firma deve identificare il creatore del sigillo.",
        "testo_integrale": "OVR-B.1-02: [CONDITONAL] Where the SCASC is used to create an advanced electronic seal, the signing certificate shall identify the creator of the seal.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "si applica quando il SCASC è utilizzato per creare un sigillo elettronico avanzato",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-B.1-03",
        "testo": "Il certificato di firma deve essere contenuto nella firma AdES creata.",
        "testo_integrale": "OVR-B.1-03: The signing certificate shall be contained in the created AdES signature.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "Parte 2: 9 (nota introduttiva)",
        "testo": "Il TSP può utilizzare direttamente le trust service policy identificate alla clausola 4.2.2, oppure può fare riferimento a una trust service policy che, pur basandosi su quelle policy, aggiunge ulteriori requisiti o vincoli rispetto al presente documento. Quest'ultimo caso è definito come la policy SCASC \"costruita su\" (built on) una trust service policy definita nel presente documento: è il concetto su cui si fonda l'intera clausola 9 e su cui operano i requisiti OVR-9-01A..OVR-9-10.",
        "testo_integrale": "NOTE: The TSP can use directly the trust service policies identified in clause 4.2.2, or the TSP can reference a trust service policy that is based on the policies identified in clause 4.2.2 but adds additional requirements or additional constraints to the requirements of the present document. The latter case is described as the SCASC policy being built on a trust service policy defined in the present document.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: Annex A",
        "testo": "Annex A (informativo) propone un indice raccomandato per la dichiarazione delle pratiche (practice statement) del SCASC, articolato in tre sezioni: 1. Introduction (identificazione del TSP e delle policy SCASC supportate, ambiente e attori del servizio, definizioni/abbreviazioni, policy e prassi — inclusa l'indicazione che, come minimo, devono esistere e essere brevemente descritti la practice statement stessa, i termini e condizioni e la service policy, oltre a risk assessment e information security policy); 2. Trust Service management and operation (clausola comune a tutti i servizi del TSP salvo i servizi CA, per cui si raccomanda invece la struttura di IETF RFC 3647 — sottovoci 2.1-2.13 che rispecchiano le sottoclausole 7.1-7.13 del presente documento); 3. Signature creation application service component technical requirements (sottovoci 3.1 Interfaces e 3.2 AdES digital signature creation, esplicitamente collegate alle clausole 8.1 e 8.2 del presente documento). È un modello di struttura raccomandata per la documentazione del TSP, non un elenco di requisiti sostanziali autonomi ulteriori rispetto a quelli già censiti nelle clausole 7, 8 e 9: le singole sottovoci non generano nodi propri.",
        "testo_integrale": "##### 1. Introduction\n1.1 Overview\n1.1.1 TSP identification\n1.1.2 Supported signature creation application service component policy/policies (formal OID/URI identification)\n1.2 Signature creation application service component environment\n1.2.1 SCASC actors\n1.2.3 Service architecture\n1.3 Definitions and abbreviations\n1.3.1 Definitions\n1.3.2 Abbreviations\n1.4 Policies and practices\n1.4.1 Organization administrating the TSP documentation\n1.4.2 Contact person\n1.4.3 TSP (public) documentation applicability This clause describes the set of documents related to the SCASC, their applicability, and position of the present practice statement within the documentation, their distribution points. At a minimum the following documents exist and need a short description:\n- the present practice statement (formal OID/URI identification should be used)\n- the terms and conditions\n- the service policy (can be referred)\none or more of the above documents identify the supported signature creation policy/policies (with formal OID/URI identification). The supported signature creation policy/policies are generally detailed in the SCASC service policy/policies.\n- risk assessment and Information security policy NOTE: The description of any business (application) domain or any transactional context can be described in a \"signature applicability rules\" document. There is no obligation for a TSP to support and publish signature applicability rules.\n##### 2. Trust Service management and operation\nThis clause may be common to all services offered by the TSP-except for CA services where the table of content described by IETF RFC 3647 [i.10] should be applied. (Either the same clause is reproduced for each service practice statement, in which case, because every service policy and security requirements add elements specific to the services, such requirements need to be addressed in addition, OR there is a common clause that is referred to from each service practice statement).\n2.1 Internal organization\n2.1.1 Organization reliability (This clause identifies the obligations of all external organizations supporting the TSP services including the applicable policies and practices (per ETSI EN 319 401 [9])\n2.1.2 Segregation of duties\n2.2 Human resources\n2.3 Asset management\n2.3.1 General requirements\n2.3.2 Media handling\n2.4 Access control\n2.5 Cryptographic controls\n2.6 Physical and environmental security\n2.7 Operation security\n2.8 Network security\n2.9 Incident management\n2.10 Collection of evidence\n2.11 Business continuity management\n2.12 TSP termination and termination plans\n2.13 Compliance\n##### 3. Signature creation application service component technical requirements\n3.1 Interfaces This clause contains requirements, control objectives and controls in connection with clause 8.1 in ETSI TS 119 431-2 (the present document).\n3.2 AdES digital signature creation This clause contains requirements, control objectives and controls in connection with clause 8.2 in ETSI TS 119 431-2 (the present document).",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: Annex C",
        "testo": "Annex C (informativo) mappa i requisiti del presente documento sui requisiti per la firma elettronica avanzata (Tabella C.1, art. 26 Regolamento (UE) n. 910/2014) e per il sigillo elettronico avanzato (Tabella C.2, art. 36), oltre che sui requisiti di validazione della firma elettronica qualificata (Tabella C.3, art. 32 §1). Il collegamento univoco al firmatario/creatore del sigillo è coperto da OVR-B.1-01/OVR-B.1-02 (identificazione nel certificato) e da OVR-8.2-04 (protezione SCP 37 del riferimento al certificato di firma all'interno della firma, ex ETSI TS 119 101); la capacità di identificare il firmatario/creatore del sigillo è coperta da OVR-B.1-03 (certificato contenuto nella firma AdES); il collegamento ai dati firmati in modo da rilevare modifiche successive è coperto da OVR-8.2-02 (algoritmi crittografici raccomandati) e, per il sigillo, da OVR-8.2-04 (SCP 14). Il requisito che i dati di creazione della firma/sigillo siano usati sotto il controllo esclusivo del firmatario/creatore (sole control) è dichiarato fuori ambito del presente documento: se si utilizza uno SSASC, è coperto da ETSI TS 119 431-1. Le lettere (a)-(f) della Tabella C.3 (requisiti di validazione della firma elettronica qualificata specifici del caso qualificato) sono dichiarate non applicabili al presente documento, salvo la lettera (g) (integrità dei dati firmati, coperta da OVR-8.2-02) e la lettera (h) (rinvio alla Tabella C.1). Una NOTA ricorrente in Tabella C.2/C.1 richiama inoltre OVR-6.2-05 (limitazione dell'elenco degli SCDev supportati nei termini e condizioni), riferimento del capitolo 1 di questa stessa fonte.",
        "testo_integrale": "## Annex C (informative): Mapping to advance electronic signatures or seals as by Regulation (EU) No 910/2014\nTable C.1 maps the requirements from the present document with the requirements on advanced electronic signatures or seals as specified directly by Regulation (EU) No 910/2014 [i.1], Tables 1 and 2 or indirectly via requirements on valid QES as specified by Regulation (EU) No 910/2014 [i.1], Table 3.\nTable C.1: Mapping of the requirements in the present document to requirements for advanced electronic signatures as defined by Regulation (EU) No 910/2014\nRegulation (EU) No 910/2014 | Applicable requirements\nArticle 26 Requirements for advanced electronic signatures\n\"An advanced electronic signature shall meet the following requirements:\n(a) it is uniquely linked to the signatory;\" | OVR-B.1-01, OVR-8.2-04 referencing from ETSI TS 119 101 [1] SCP 37: \"The SCA shall protect the reference to or copy of the signing certificate within the signature from undetected replacement after the signature has been created.\"\n\"(b) it is capable of identifying the signatory;\" | OVR-B.1-03\n\"(c) it is created using electronic signature creation data that the signatory can, with a high level of confidence, use under his sole control; and\" | The sole control is out of scope of the present document. If a SSASC is used, this is covered in ETSI TS 119 431-1 [i.8]. See note.\n\"(d) it is linked to the data signed therewith in such a way that any subsequent change in the data is detectable.\" | OVR-8.2-02 The cryptographic algorithms used should be selected from algorithms recommended by ETSI TS 119 312 [i.5]. NOTE: The SSASC can limit the list of supported SCDev in its terms and conditions (OVR-6.2-05).\nTable C.2: Mapping of the requirements in the present document to requirements for advanced electronic seals as defined by Regulation (EU) No 910/2014\nRegulation (EU) No 910/2014 Article 36 Requirements for advanced electronic seals\n\"An advanced electronic seal shall meet the following requirements:\n(a) it is uniquely linked to the creator of the seal;\" | OVR-B.1-02, OVR-8.2-04 referencing from ETSI TS 119 101 [1] SCP 37\n\"(b) it is capable of identifying the creator of the seal;\" | OVR-B.1-03\n\"(c) it is created using electronic seal creation data that the creator of the seal can, with a high level of confidence under its control, use for electronic seal creation; and\" | The sole control is out of scope of the present document. If a SSASC is used, this is covered in ETSI TS 119 431-1 [i.8]. See note.\n\"(d) it is linked to the data to which it relates in such a way that any subsequent change in the data is detectable.\" | OVR-8.2-04 referencing from ETSI TS 119 101 [1] SCP 14\nNOTE: The SSASC can limit the list of supported SCDev in its terms and conditions (OVR-6.2-05).\nTable C.3: Mapping of the requirements in the present document to requirements that have to be fulfilled for a valid advanced electronic signature/seal as defined by Regulation (EU) No 910/2014\nRegulation (EU) No 910/2014 | Applicable requirements\nArticle 32.1 Requirements for the validation of qualified electronic signatures \"1. The process for the validation of a qualified electronic signature shall confirm the validity of a qualified electronic signature provided that:\n(a) the certificate that supports the signature was, at the time of signing, a qualified certificate for electronic signature complying with Annex I; | Not applicable, specific to the qualified case\n(b) the qualified certificate was issued by a qualified trust service provider and was valid at the time of signing; | Not applicable, specific to the qualified case\n(c) the signature validation data corresponds to the data provided to the relying party; | Not applicable, this is the responsibility of the CA and the SSASC\n(d) the unique set of data representing the signatory in the certificate is correctly provided to the relying party; | Not applicable, this is the responsibility of the CA\n(e) the use of any pseudonym is clearly indicated to the relying party if a pseudonym was used at the time of signing; | Not applicable, this is the responsibility of the CA\n(f) the electronic signature was created by a qualified electronic signature creation device; | Not applicable, specific to the qualified case\n(g) the integrity of the signed data has not been compromised; | OVR-8.2-02\n(h) the requirements provided for in Article 26 were met at the time of signing.\" | See table C.1",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica avanzata", "sigillo elettronico avanzato"],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Parte 2: OVR-7.1-01",
    "Parte 2: OVR-7.2-01",
    "Parte 2: OVR-7.3-01",
    "Parte 2: OVR-7.4-01",
    "Parte 2: OVR-7.5-01",
    "Parte 2: OVR-7.6-01",
    "Parte 2: OVR-7.6-02",
    "Parte 2: OVR-7.7-01",
    "Parte 2: OVR-7.7-02",
    "Parte 2: OVR-7.7-03",
    "Parte 2: OVR-7.7-04",
    "Parte 2: OVR-7.8-01",
    "Parte 2: OVR-7.9-01",
    "Parte 2: OVR-7.10-01",
    "Parte 2: OVR-7.10-02",
    "Parte 2: OVR-7.10-03",
    "Parte 2: OVR-7.10-04",
    "Parte 2: OVR-7.10-05",
    "Parte 2: OVR-7.10-06",
    "Parte 2: OVR-7.11-01",
    "Parte 2: OVR-7.11-02",
    "Parte 2: OVR-7.11-03",
    "Parte 2: OVR-7.12-01",
    "Parte 2: OVR-7.13-01",
    "Parte 2: OVR-7.13-02",
    "Parte 2: OVR-7.13-03",
    "Parte 2: OVR-7.13-04",
    "Parte 2: ASI-8.1-01",
    "Parte 2: ASI-8.1-02",
    "Parte 2: ASI-8.1-03",
    "Parte 2: ASI-8.1-04",
    "Parte 2: ASI-8.1-05",
    "Parte 2: ASI-8.1-06",
    "Parte 2: ASI-8.1-07",
    "Parte 2: ASI-8.1-08",
    "Parte 2: ASI-8.1-09",
    "Parte 2: ASI-8.1-10",
    "Parte 2: ASI-8.1-11",
    "Parte 2: ASI-8.1-12",
    "Parte 2: OVR-8.2-01",
    "Parte 2: OVR-8.2-02",
    "Parte 2: OVR-8.2-03",
    "Parte 2: OVR-8.2-04",
    "Parte 2: OVR-8.2-05",
    "Parte 2: OVR-8.2-06",
    "Parte 2: OVR-8.2-07",
    "Parte 2: OVR-8.2-08",
    "Parte 2: OVR-8.2-08A",
    "Parte 2: OVR-8.2-09",
    "Parte 2: 9 (nota introduttiva)",
    "Parte 2: OVR-9-01A",
    "Parte 2: OVR-9-02",
    "Parte 2: OVR-9-03",
    "Parte 2: OVR-9-04",
    "Parte 2: OVR-9-05",
    "Parte 2: OVR-9-06",
    "Parte 2: OVR-9-07",
    "Parte 2: OVR-9-08",
    "Parte 2: OVR-9-09",
    "Parte 2: OVR-9-10",
    "Parte 2: Annex A",
    "Parte 2: OVR-B.1-01",
    "Parte 2: OVR-B.1-02",
    "Parte 2: OVR-B.1-03",
    "Parte 2: Annex C",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.6-02"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.6-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.7-02"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.7-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.7-03"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.7-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.7-04"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.7-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.10-02"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.10-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.10-03"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.10-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.10-04"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.10-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.10-06"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.10-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.11-02"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.11-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.11-03"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.11-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.13-02"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.13-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.13-03"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.13-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.13-04"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.13-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.10-05"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.10-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-7.10-05"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-7.10-02"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: ASI-8.1-04"),
        "nodo_a": ("obbligo", None, "Parte 2: ASI-8.1-03"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: ASI-8.1-05"),
        "nodo_a": ("obbligo", None, "Parte 2: ASI-8.1-03"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: ASI-8.1-06"),
        "nodo_a": ("obbligo", None, "Parte 2: ASI-8.1-03"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: ASI-8.1-08"),
        "nodo_a": ("obbligo", None, "Parte 2: ASI-8.1-03"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: ASI-8.1-09"),
        "nodo_a": ("obbligo", None, "Parte 2: ASI-8.1-03"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: ASI-8.1-10"),
        "nodo_a": ("obbligo", None, "Parte 2: ASI-8.1-03"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: ASI-8.1-11"),
        "nodo_a": ("obbligo", None, "Parte 2: ASI-8.1-03"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: ASI-8.1-12"),
        "nodo_a": ("obbligo", None, "Parte 2: ASI-8.1-03"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-8.2-09"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-8.2-08A"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-9-02"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-9-01A"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-9-03"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-9-01A"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-9-04"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-9-01A"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-9-05"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-9-01A"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-9-06"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-9-01A"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-9-07"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-9-01A"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-9-08"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-9-01A"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-9-09"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-9-01A"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-9-10"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-9-01A"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: OVR-9-01A"),
        "nodo_a": ("principio", None, "Parte 2: 9 (nota introduttiva)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("principio", None, "Parte 2: Annex C"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-B.1-01"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Parte 2: Annex C"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-B.1-02"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Parte 2: Annex C"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-B.1-03"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Parte 2: Annex C"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-8.2-02"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Parte 2: Annex C"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-8.2-04"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Parte 2: Annex C"),
        "nodo_a": ("obbligo", None, "Parte 2: OVR-6.2-05"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
