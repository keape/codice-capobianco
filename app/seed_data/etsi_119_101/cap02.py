"""Estrazione granulare ETSI TS 119 101 V1.1.1 (2016-03) — Capitolo 2:
clausole 5 (General requirements: 5.1 User interface, 5.2 General security
measures, 5.3 System completeness requirements), 6 (Legal driven policy
requirements: 6.1 Introduction, 6.2 Processing of personal data, 6.3
Accessibility for persons with disabilities) e 7 (Information security
(management system) requirements: 7.1 Introduction, 7.2 Network protection,
7.3 Information systems protection, 7.4 Software integrity of the
application, 7.5 Data storage security, 7.6 Event logs).

Fonte 26 (numerazione definitiva cablata dalla sessione principale in
app/seed.py — questo modulo NON tocca seed.py). Testo ufficiale in
app/.source_cache/etsi_119_101/cap02.txt. Manifest di split:
app/.source_cache/etsi_119_101/manifest.json.

Perimetro: SOLO le clausole 5-7 (righe 1-320 del file capitolo). La clausola
2 "References" e la sezione finale "History" non compaiono in questo file
(cadono fuori dal marker di split); in ogni caso entrambe sono paratesto
(bibliografia/registro di versione) e per ADR-0007 non generano nodi né item
di indice.

Modellazione (ADR-0007). Questo documento numera le proprie prescrizioni
come "controls" con id proprio (UI 1, GSM 1.1, ..., EL 8), non come clausole
numerate con prosa continua: è lo stesso genere di fonte di ETSI EN 319 401
(Fonte 10), TS 119 461 (Fonte 9) e TS 119 431-1 (Fonte 11), dove l'unità di
copertura è il requisito numerato e il `riferimento` è l'id letterale del
testo, non "clausola X.Y". Granularità applicata qui:

- Ciascuno dei 44 control numerati -> un Obbligo, `riferimento` = SOLO l'id
  esatto come appare nel testo (es. "GSM 1.1", "EL 3"), senza prefisso di
  clausola: è la forma con cui si risolvono le citazioni già presenti nel
  grafo (ETSI TS 119 431-2 richiama "UI 1", "UI 2", "GSM 1.2", "GSM 1.3",
  "GSM 1.4", "GSM 2.4"). L'id non incorpora il numero di clausola (a
  differenza di "REQ-7.10-01" di EN 319 401): la legenda è UI=5.1, GSM=5.2,
  SC=5.3, PD=6.2, APD=6.3, ISMS=7.1, NP=7.2, ISP=7.3, SIA=7.4, DSS=7.5,
  EL=7.6.
- GSM 1.5 NON esiste nel testo ufficiale (la numerazione salta da GSM 1.4 a
  GSM 1.6): nessun nodo inventato per colmare il buco, coerente con ADR-0010.
- La prosa non numerata ha un nodo proprio per ogni blocco distinto, un
  Principio tipo "altro": "clausola 6.1 (Introduction)" e "clausola 7.1
  (Introduction)" per le due introduzioni, "clausola X.Y (Titolo) — control
  objective N" per ciascun blocco "Control objective" (5.1 e 5.2 ne hanno
  due ciascuna: l'obiettivo non è assorbito nel primo control del gruppo
  perché più di un control vi si riferisce, es. l'obiettivo 1 di 5.2 copre
  sia il gruppo GSM 1.x sia il gruppo GSM 2.x). Criterio generale del
  censimento: un nodo per unità prescrittiva dotata di identità propria —
  l'id del control quando c'è, la clausola quando non c'è (questo documento
  non dà un id ai blocchi di obiettivo). Item e testo di questi Principi
  coprono SOLO la prosa non numerata; i control della stessa clausola
  restano item distinti: nessuna porzione di testo è rappresentata due
  volte.
- "Control Objective"/"Controls (...)" (intestazioni di blocco) e le
  etichette di gruppo "GSM 1: Appropriate security measures:" e "GSM 2:
  Specific application environment:" non generano nodi propri (puri
  raggruppatori, senza contenuto oltre al titolo): le due etichette GSM
  restano verbatim come prefisso del primo control del gruppo (GSM 1.1,
  GSM 2.1), le intestazioni di blocco sono omesse.
- NOTE ed EXAMPLE annessi a un control sono assorbiti nel
  `testo_integrale` del control a cui sono appesi (precedente: EN 319 401
  cap05, TS 119 461 cap03): NOTE 1 (qualifica di "recognized" secondo la
  code signing policy applicabile) e NOTE 2 (misure dell'ambiente come
  esito dell'analisi del rischio del sistema di gestione, rinvio alla
  clausola 7) sono chiarimenti sostanziali e restano; NOTE 3 ("The
  corresponding information can be part of the SCA/SVA/SAA documentation")
  è un'indicazione sull'adempimento e resta; l'EXAMPLE di APD 1 cita il
  Regolamento (UE) n. 910/2014 sull'accessibilità ed è sostanziale.
- Soggetti: obblighi posti alla SCA/SVA/SAA, alla DA o all'organizzazione
  che implementa -> "QTSP/gestore" ruolo "obbligato": la tassonomia del
  censimento non ha una categoria per l'organizzazione utilizzatrice
  (driving application), che è comunque il soggetto che implementa e opera
  l'applicazione in questo contesto. Quando il control impone di informare o
  fornire qualcosa all'utente finale (UI 1, UI 2, GSM 3) il soggetto
  "Utente/titolare" è aggiunto come "destinatario".
- tipo_obbligo: "tecnico/sicurezza" per misure di protezione e
  configurazione applicate a sistemi/componenti (segmentazione di rete,
  firewall, controllo accessi, anti-virus, patch, change detection,
  riservatezza/integrità dei flussi, cancellazione sicura dei dati);
  "organizzativo" per il governo di sicurezza a livello di organizzazione
  (adozione di ISO/IEC 27002 o di un'analisi del rischio, ISMS, completezza
  del sistema, evidenza della conformità privacy, accessibilità,
  gestione delle patch come processo); "informativo/trasparenza" per gli
  obblighi di informazione all'utente (GSM 3); "procedurale" per ISP 5
  (documentazione del motivo di non applicazione di una patch); "di
  conservazione" per l'intera clausola 7.6 (EL 1-EL 8), che è registrazione
  a fini di prova — stesso trattamento della clausola 7.10 di EN 319 401.
- `condizione_applicabilita` valorizzata solo dove il testo subordina
  esplicitamente l'obbligo a una condizione ("If applicable", "If ...",
  "When ...", o il rinvio alla legge applicabile di APD 1): GSM 1.6, GSM
  1.7, GSM 2.1, GSM 2.2, GSM 2.6, NP 1, ISP 2, SIA 4, APD 1. Le condizioni
  introdotte da un evento già occorso (SIA 3: componenti "that have been
  subject to viruses or malicious software attack") non sono condizioni di
  applicabilità ma il fatto stesso della fattispecie e non sono valorizzate
  come tali.
- Refusi del testo ufficiale conservati verbatim in `testo_integrale`
  (mai corretti, ratione ADR-0010): "this cause" per "this clause" in ISMS 1
  e "SCA/SVA/SAADA" in SIA 3.
- RELAZIONI: vuoto, per vincolo esplicito dell'incarico (nessun
  collegamento cross-fonte durante l'import granulare parallelo: la Fase 6
  /ADR-0009 li costruisce nella sessione principale). Le citazioni interne
  di questo capitolo (DSS 3 in DSS 4, clausola 7 in NOTE 2 di GSM 2.6, ISO/
  IEC 27002, ETSI EN 301 549, Regolamento (UE) n. 910/2014) restano
  descritte nel testo, senza archi.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "UI 1",
        "testo": (
            "L'interfaccia utente dovrebbe: a) fornire indicazioni non ambigue sull'uso della "
            "SCA/SVA/SAA e, se applicabile, sull'installazione e la configurazione del sistema; "
            "b) essere auto-descrittiva, così che ogni passo di dialogo sia comprensibile tramite "
            "il riscontro del sistema o sia spiegato all'utente su richiesta; c) essere tollerante "
            "agli errori, se nonostante errori evidenti in input il risultato voluto è raggiungibile "
            "con un intervento correttivo minimo; d) produrre segnalazioni di errore informative che "
            "guidino l'utente; e) fornire un riscontro che confermi che l'azione compiuta dall'utente "
            "è corretta (o non corretta); f) quando usa indicazioni cromatiche, usare il rosso per gli "
            "errori e il verde per procedere; g) poter annullare in qualsiasi momento l'operazione in "
            "corso e tornare al menu principale, oppure uscire completamente dal sistema; h) proteggere "
            "la riservatezza dell'individuo, ad esempio rendendo le informazioni non accessibili ad altri "
            "sull'interfaccia utente; e i) chiedere conferma delle decisioni e scelte chiave dell'utente."
        ),
        "testo_integrale": (
            "UI 1: The user interface should:\n"
            "    a) provide unambiguous user guidance on how to use the SCA/SVA/SAA, and, if applicable, to install and configure the system;\n"
            "    b) be self-descriptive to the extent that each dialogue step is easy to understand through feedback from the system or is explained to the user upon request;\n"
            "    c) be error tolerant if, despite evident errors in input, the intended result can be achieved with minimal corrective action;\n"
            "    d) deliver informative error reporting to lead the user forward;\n"
            "    e) provide feedback to confirm that the action carried out by the user is correct (or incorrect);\n"
            "    f) when using colour indication, use red for errors and green for go/proceed;\n"
            "    g) be able, at any time, to cancel the current operation and return to the main menu; or, to exit the system completely;\n"
            "    h) protect privacy for the individual, e.g. by making the information not accessible to others at the user interface; and\n"
            "    i) ask for confirmation of the key decisions and choices of the user."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "UI 2",
        "testo": (
            "La SCA/SVA/SAA deve fornire un manuale utente dettagliato che guidi gli utenti al primo "
            "utilizzo attraverso il processo di generazione, augmentation e convalida di una firma."
        ),
        "testo_integrale": (
            "UI 2: The SCA/SVA/SAA shall provide a detailed user's guide leading first time users through the process of generating, augmenting and validating a signature."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "GSM 1.1",
        "testo": (
            "Le misure di sicurezza per i sistemi su cui l'applicazione è sviluppata dovrebbero essere "
            "quelle di ISO/IEC 27002 [i.6] oppure basate su un'analisi del rischio dettagliata; i punti "
            "di attenzione specifici sono elencati nei control da GSM 1.2 a GSM 1.7."
        ),
        "testo_integrale": (
            "GSM 1: Appropriate security measures:\n"
            "   GSM 1.1:      The security measures for the systems on which the application is developed should be as in ISO/IEC 27002 [i.6] or based on a detailed risk analysis. Specific points of attention are listed below."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "GSM 1.2",
        "testo": (
            "Dovrebbe essere usato l'ambiente applicativo più recente (ambienti software gestiti), "
            "incluse correzioni di sicurezza aggiornate."
        ),
        "testo_integrale": (
            "GSM 1.2:      The latest application environment (managed software environments) should be used including up to date security fixes."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "GSM 1.3",
        "testo": (
            "Devono essere usate implementazioni ben testate e riesaminate di protocolli e librerie "
            "standardizzati."
        ),
        "testo_integrale": (
            "GSM 1.3:      Well-tested and reviewed implementations of standardized protocol(s) and libraries shall be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "GSM 1.4",
        "testo": (
            "Devono essere usate librerie crittografiche testate rispetto allo standard corrispondente; "
            "dovrebbero essere usate librerie consolidate."
        ),
        "testo_integrale": (
            "GSM 1.4:      Cryptographic libraries tested against the corresponding standard shall be used. Established libraries should be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "GSM 1.6",
        "testo": (
            "Se applicabile, devono essere implementate protezioni anti-virus e anti-spyware (incluse "
            "per le parti dell'applicazione che possono essere scaricate)."
        ),
        "testo_integrale": (
            "GSM 1.6:      If applicable, anti-virus, spyware protection (incl. for application parts that could be downloadable) shall be implemented."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "Se applicabile (necessità di protezione anti-virus e anti-spyware per il sistema su cui "
            "l'applicazione è sviluppata, incluse le parti dell'applicazione che possono essere scaricate)."
        ),
    },
    {
        "riferimento": "GSM 1.7",
        "testo": "Se applicabile, deve essere usato un personal firewall.",
        "testo_integrale": (
            "GSM 1.7:      If applicable, personal firewall shall be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "Se applicabile (necessità di un personal firewall per il sistema su cui l'applicazione è "
            "sviluppata o usata)."
        ),
    },
    {
        "riferimento": "GSM 2.1",
        "testo": (
            "Quando la SCA, la SVA o la SAA è distribuita come pacchetto software, essa dovrebbe essere "
            "firmata digitalmente."
        ),
        "testo_integrale": (
            "GSM 2: Specific application environment:\n"
            "   GSM 2.1:      When the SCA, SVA or SAA is delivered as a software package, it should be digitally signed."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "Quando la SCA, la SVA o la SAA è distribuita come pacchetto software."
        ),
    },
    {
        "riferimento": "GSM 2.2",
        "testo": (
            "Quando il codice distribuito, o parte di esso, è firmato digitalmente, la firma dovrebbe "
            "essere apposta con un certificato di firma del codice fornito da un prestatore di servizi "
            "fiduciari riconosciuto che emette certificati, e la firma dovrebbe contenere una marca "
            "temporale di un'autorità di marcatura temporale riconosciuta; per \"riconosciuto\" si "
            "intende secondo la policy di firma del codice applicabile."
        ),
        "testo_integrale": (
            "GSM 2.2:      When the delivered code or part of it is digitally signed, this should be done using a code-signing certificate provided by a recognized trust service provider issuing certificates and the signature should contain a time-stamp from a recognized time-stamping authority.\n\n"
            "   NOTE 1: Recognized according to the applicable code signing signature policy."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "Quando il codice distribuito, o parte di esso, è firmato digitalmente."
        ),
    },
    {
        "riferimento": "GSM 2.3",
        "testo": (
            "La DA (applicazione che richiama la SCA/SVA/SAA) dovrebbe mantenere integrità e "
            "riservatezza di tutte le informazioni fornite dall'utente e di ogni dato che transita tra "
            "l'applicazione e l'utente, anche nel caso di un ambiente applicativo pubblico."
        ),
        "testo_integrale": (
            "GSM 2.3:      The DA should maintain integrity and confidentiality of all information supplied by the user and of any data flowing between the application and the user, even in the case of a public application environment."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "GSM 2.4",
        "testo": (
            "La SCA/SVA/SAA deve mantenere integrità e riservatezza di tutte le informazioni fornite "
            "dall'utente e di ogni dato che transita tra l'applicazione e l'utente, anche nel caso di un "
            "ambiente applicativo pubblico."
        ),
        "testo_integrale": (
            "GSM 2.4:      The SCA/SVA/SAA shall maintain integrity and confidentiality of all information supplied by the user and of any data flowing between the application and the user, even in the case of a public application environment."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "GSM 2.5",
        "testo": (
            "I dati di autenticazione del firmatario devono essere cancellati in modo sicuro "
            "dall'applicazione alla fine della sessione, per evitare attacchi di replay da parte di "
            "altri utenti."
        ),
        "testo_integrale": (
            "GSM 2.5:     Signer's authentication data shall be securely deleted at the session end by the application to avoid any replay attack of other users."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "GSM 2.6",
        "testo": (
            "Se l'applicazione è usata da utenti diversi, deve assicurarsi che tutti i dati relativi a "
            "un processo di firma siano cancellati dalle aree pubblicamente accessibili (inclusi caching "
            "e archivi di certificati) dopo il completamento della firma, e non deve copiare tali "
            "elementi a soggetti non autorizzati dall'utente; le misure specifiche dell'ambiente in cui "
            "la SCA/SVA/SAA è usata possono derivare dall'analisi del rischio del sistema di gestione "
            "della sicurezza delle informazioni (clausola 7)."
        ),
        "testo_integrale": (
            "GSM 2.6:     If the application is used by different users, then the application shall make sure that all data related to a signature process is erased from public available areas (including caching, or certificates stores) after having completed the signature. The application shall not copy these elements to any party not authorized by the user.\n\n"
            "    NOTE 2: Security measures specific to the environment in which the SCA/SVA/SAA is used can be a result of a risk analysis done by the information security management system, see clause 7."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "Se l'applicazione è usata da utenti diversi.",
    },
    {
        "riferimento": "GSM 3",
        "testo": (
            "La SCA/SVA/SAA dovrebbe informare l'utente sulle buone pratiche di protezione dei personal "
            "computer (anti-virus, personal firewall, ecc.); tale informazione può far parte della "
            "documentazione della SCA/SVA/SAA."
        ),
        "testo_integrale": (
            "GSM 3: The SCA/SVA/SAA should inform the user of best practices in protecting personal computers (anti-virus, personal firewall, etc.).\n\n"
            "    NOTE 3: The corresponding information can be part of the SCA/SVA/SAA documentation."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "SC 1",
        "testo": (
            "In un sistema completo devono essere implementati tutti i requisiti obbligatori enunciati "
            "nel presente documento, inclusi quelli che possono essere implementati indifferentemente "
            "dalla DA o dalla SVA/SCA/SAA."
        ),
        "testo_integrale": (
            "SC 1:     In a complete system, all mandatory requirements stated in the present document shall be implemented."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "PD 1",
        "testo": (
            "Deve essere fornita evidenza di come sono soddisfatti i requisiti della normativa "
            "applicabile in materia di privacy e protezione dei dati (es. direttiva europea sulla "
            "protezione dei dati [i.2])."
        ),
        "testo_integrale": (
            "PD 1:     Evidence shall be provided on how requirements of applicable Privacy and Data Protection regulation legislation (e.g. European Data Protection Directive [i.2]) are met."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "PD 2",
        "testo": (
            "Devono essere adottate misure tecniche appropriate contro il trattamento non autorizzato o "
            "illecito dei dati personali e contro la perdita, la distruzione o il danneggiamento "
            "accidentali di dati personali."
        ),
        "testo_integrale": (
            "PD 2:     Appropriate technical measures shall be taken against unauthorized or unlawful processing of personal data and against accidental loss or destruction of, or damage to, personal data."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "APD 1",
        "testo": (
            "Se l'accessibilità per le persone con disabilità è richiesta dalla legge applicabile, la "
            "SCA/SVA/SAA deve essere resa accessibile alle persone con disabilità ove fattibile; si "
            "dovrebbe tener conto di standard applicabili come ETSI EN 301 549 [i.27]. Esempio: il "
            "Regolamento (UE) n. 910/2014 [i.1] prevede che, ove fattibile, l'accessibilità per le "
            "persone con disabilità sia presa in considerazione."
        ),
        "testo_integrale": (
            "APD 1:    If accessibility for persons with disabilities is required by applicable law, SCA/SVA/SAA shall be made accessible for persons with disabilities where feasible. Applicable standards such as ETSI EN 301 549 [i.27] should be taken into account.\n\n"
            "    EXAMPLE:         Regulation (EU) No 910/2014 [i.1] states that where feasible, accessibility for persons with disabilities is required to be taken into account."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "Se l'accessibilità per le persone con disabilità è richiesta dalla legge applicabile."
        ),
    },
    {
        "riferimento": "ISMS 1",
        "testo": (
            "I controlli identificati in questa clausola devono essere applicati nel contesto del "
            "sistema di gestione della sicurezza delle informazioni dell'organizzazione."
        ),
        "testo_integrale": (
            "ISMS 1: The controls identified in this cause shall be applied in the context of the organization information security management system."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "ISMS 2",
        "testo": (
            "Per un'organizzazione che integra processi di creazione e convalida di firme, la sicurezza "
            "delle informazioni dovrebbe essere implementata sulla base di ISO/IEC 27001 [i.5], "
            "debitamente integrata con le disposizioni che seguono."
        ),
        "testo_integrale": (
            "ISMS 2: For an organization integrating signature creation and validation processes, information security should be implemented based on ISO/IEC 27001 [i.5], duly integrated with the following provisions."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "NP 1",
        "testo": (
            "Se la SCA/SVA/SAA è implementata in un ambiente applicativo con componenti a livelli di "
            "sicurezza diversi che comunicano su rete, le reti che trasmettono dati riservati da o "
            "verso la SCA/SVA/SAA dovrebbero essere adeguatamente segmentate per impedire l'accesso "
            "diretto da sistemi meno affidabili a sistemi più affidabili che contengono o trattano dati "
            "riservati; i dati riservati non dovrebbero essere trasmessi su reti non controllate o non "
            "protette."
        ),
        "testo_integrale": (
            "NP 1:     If the SCA/SVA/SAA is implemented within an application environment containing components of different levels of security which communicate over networks, then the networks that transmit confidential data to or from the SCA/SVA/SAA should be adequately segmented to prohibit direct access from less trusted systems to higher trusted systems that contain or process confidential data. Confidential data should not be transmitted over uncontrolled or unprotected networks."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "Se la SCA/SVA/SAA è implementata in un ambiente applicativo con componenti a livelli di "
            "sicurezza diversi che comunicano su rete."
        ),
    },
    {
        "riferimento": "NP 2",
        "testo": (
            "L'accesso di rete ai sistemi informativi che conservano o trattano dati riservati deve "
            "essere adeguatamente limitato mediante dispositivi di filtraggio quali i firewall; le "
            "regole devono proteggere i sistemi informativi sia dal traffico in entrata sia da quello "
            "in uscita non autorizzati."
        ),
        "testo_integrale": (
            "NP 2:     Network access to information systems storing or processing confidential data shall be adequately restricted using filtering devices such as firewalls. Rules shall protect the information systems from both unauthorized incoming and outgoing traffic."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "ISP 1",
        "testo": (
            "I sistemi informativi devono essere protetti dall'uso malevolo con meccanismi quali "
            "anti-virus, anti-spyware o altri meccanismi di prevenzione."
        ),
        "testo_integrale": (
            "ISP 1:    Information systems shall be protected against malicious use with mechanisms such as anti-virus and anti-spyware or other prevention mechanisms."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "ISP 2",
        "testo": (
            "Se la SCA/SVA/SAA gira su un sistema informativo per più utenti, un adeguato meccanismo "
            "di controllo degli accessi deve impedire qualsiasi accesso non autorizzato ai dati "
            "riservati."
        ),
        "testo_integrale": (
            "ISP 2:    If the SCA/SVA/SAA runs on an information system for several users, then an adequate access control mechanism shall prevent any unauthorized access to confidential data."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "Se la SCA/SVA/SAA gira su un sistema informativo utilizzato da più utenti."
        ),
    },
    {
        "riferimento": "ISP 3",
        "testo": (
            "Le patch e le correzioni di sicurezza dovrebbero essere seguite e monitorate su base "
            "continuativa."
        ),
        "testo_integrale": (
            "ISP 3:    Security patches and fixes should be followed-up on a continuous basis."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "ISP 4",
        "testo": (
            "L'installazione delle patch dovrebbe essere prioritizzata: le patch di sicurezza per "
            "sistemi critici o a rischio vanno installate appena possibile e comunque entro 30 giorni "
            "dalla disponibilità delle patch, le altre patch a rischio inferiore entro 90 giorni."
        ),
        "testo_integrale": (
            "ISP 4:    Patch installations should be prioritized such that security patches for critical or at-risk systems are installed as soon as possible and within 30 days of the availability of the patches, and other lower-risk patches are installed within 90 days."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "ISP 5",
        "testo": (
            "Una patch di sicurezza non deve essere applicata se introdurrebbe vulnerabilità o "
            "instabilità aggiuntive che superano i benefici dell'applicazione della patch; il motivo "
            "della mancata applicazione di patch di sicurezza dovrebbe essere documentato."
        ),
        "testo_integrale": (
            "ISP 5:    A security patch needs not be applied if it would introduce additional vulnerabilities or instabilities that outweigh the benefits of applying the security patch. The reason for not applying any security patches should be documented."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "SIA 1",
        "testo": (
            "I componenti SCA/SVA/SAA/DA devono essere protetti da virus e software malevolo per "
            "garantirne l'integrità."
        ),
        "testo_integrale": (
            "SIA 1:    SCA/SVA/SAA/DA components shall be protected against viruses and malicious software to ensure their integrity."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "SIA 2",
        "testo": (
            "Deve essere dispiegato un meccanismo di rilevamento delle modifiche (ad esempio strumenti "
            "di monitoraggio dell'integrità dei file) per rilevare modifiche non autorizzate (incluse "
            "modifiche, aggiunte e cancellazioni) di componenti critici SCA/SVA/SAA/DA, come ad "
            "esempio i file di configurazione."
        ),
        "testo_integrale": (
            "SIA 2:    A change-detection mechanism (for example, file-integrity monitoring tools) shall be deployed to detect unauthorized modification (including changes, additions, and deletions) of critical SCA/SVA/SAA/DA components, like for example configuration files."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "SIA 3",
        "testo": (
            "I componenti SCA/SVA/SAA/DA che sono stati oggetto di virus o di attacchi di software "
            "malevolo devono essere riparati o disabilitati fino a quando la riparazione non è "
            "possibile."
        ),
        "testo_integrale": (
            "SIA 3:    SCA/SVA/SAADA components that have been subject to viruses or malicious software attack shall be repaired or disabled until repair is possible."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "SIA 4",
        "testo": (
            "Se componenti software della SCA, della SVA, della SAA o della DA sono destinati a essere "
            "pubblicati o distribuiti, tali componenti devono essere distribuiti, installati e "
            "configurati in modo sicuro."
        ),
        "testo_integrale": (
            "SIA 4:    If software components of the SCA, SVA, SAA or DA are intended to be published or delivered, these components shall be securely delivered, installed and configured."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "Se componenti software della SCA, della SVA, della SAA o della DA sono destinati a essere "
            "pubblicati o distribuiti."
        ),
    },
    {
        "riferimento": "DSS 1",
        "testo": (
            "I sistemi informativi che conservano dati riservati dovrebbero essere configurati secondo "
            "una baseline di sicurezza predefinita basata su una valutazione del rischio."
        ),
        "testo_integrale": (
            "DSS 1:    Information systems storing confidential data should be configured according to a predefined security baseline based on a risk assessment."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "DSS 2",
        "testo": (
            "I dati riservati devono essere protetti da accessi non autorizzati e da modifiche e "
            "perdite non autorizzate o involontarie."
        ),
        "testo_integrale": (
            "DSS 2:    Confidential data shall be protected against unauthorized access and unauthorized or unintentional changes and loss."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "DSS 3",
        "testo": (
            "La SCA/SVA/SAA e il suo ambiente applicativo devono supportare misure appropriate di "
            "sicurezza della conservazione dei dati."
        ),
        "testo_integrale": (
            "DSS 3:    The SCA/SVA/SAA and its application environment shall support appropriate data storage security measures."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "DSS 4",
        "testo": (
            "Le misure di sicurezza della conservazione dei dati introdotte in DSS 3 dovrebbero essere "
            "quelle definite in ISO/IEC 27002 [i.6] oppure basate su un'analisi del rischio "
            "dettagliata."
        ),
        "testo_integrale": (
            "DSS 4:    The data storage security measures introduced in DSS 3 should be as defined in ISO/IEC 27002 [i.6] or based on a detailed risk analysis."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "EL 1",
        "testo": (
            "I sistemi informativi che conservano o trattano registri di eventi dovrebbero essere "
            "configurati secondo una baseline di sicurezza predefinita basata su una valutazione del "
            "rischio."
        ),
        "testo_integrale": (
            "EL 1:     Information systems storing or processing event logs should be configured according to a predefined security baseline based on a risk assessment."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "EL 2",
        "testo": (
            "I registri di eventi devono essere protetti da accessi non autorizzati e da manomissioni "
            "o cancellazioni non autorizzate o involontarie."
        ),
        "testo_integrale": (
            "EL 2:     Event logs shall be protected against unauthorized access, and unauthorized or unintentional tampering or deletion."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "EL 3",
        "testo": (
            "La SCA/SVA/SAA deve: a) registrare essa stessa gli eventi necessari; oppure b) fornire i "
            "dati necessari all'applicazione che la richiama (driving application)."
        ),
        "testo_integrale": (
            "EL 3:     The SCA/SVA/SAA shall:\n\n"
            "    a)   log the needed events itself; or\n\n"
            "    b)   provide the necessary data to the driving application."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "EL 4",
        "testo": (
            "Se la SCA/SVA/SAA non registra l'evento necessario, deve registrarlo la DA "
            "(applicazione che la richiama)."
        ),
        "testo_integrale": (
            "EL 4:     If the SCA/SVA/SAA does not log the needed event, the DA shall log them."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "EL 5",
        "testo": "Deve essere registrata ogni creazione di firma.",
        "testo_integrale": (
            "EL 5:     Any signature creation shall be logged."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "EL 6",
        "testo": "Dovrebbe essere registrata ogni convalida di firma.",
        "testo_integrale": (
            "EL 6:     Any signature validation should be logged."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "EL 7",
        "testo": "I registri di eventi devono essere marcati con l'ora dell'evento.",
        "testo_integrale": (
            "EL 7:     Event logs shall be marked with the time of the event."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "EL 8",
        "testo": (
            "I registri di eventi dovrebbero includere il tipo di evento, l'esito positivo o negativo "
            "dell'evento e un identificatore della persona e/o del componente responsabile "
            "dell'evento."
        ),
        "testo_integrale": (
            "EL 8:     Event logs should include the type of the event, the event success or failure, and an identifier of the person and/or component responsible for such an event."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 5.1 (User interface) — control objective 1",
        "testo": (
            "Obiettivo di controllo: assicurare che l'interfaccia utente (che può far parte della "
            "SCA/SVA/SAA o della DA che richiama la SCA/SVA/SAA) sia ben progettata e facile da "
            "usare, per evitare problemi e malintesi nell'interazione con l'applicazione e garantire "
            "così la fiducia dell'utente."
        ),
        "testo_integrale": (
            "Control Objective\n\n"
            "Ensure that the user interface is well designed and easy to use to avoid any problems and misunderstandings in the interaction with the application. This ensures the user confidence. The user interface can be part of the SCA/SVA/SAA or the DA which calls the SCA/SVA/SAA."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.1 (User interface) — control objective 2",
        "testo": (
            "Obiettivo di controllo: fornire all'utente informazioni sufficienti a comprendere il "
            "processo di generazione, augmentation e convalida della firma."
        ),
        "testo_integrale": (
            "Control Objective\n\n"
            "Provide the user with sufficient information to understand the process of generating, augmenting and validating the signature."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2 (General security measures) — control objective 1",
        "testo": (
            "Obiettivo di controllo: assicurare che i sistemi su cui l'applicazione è sviluppata "
            "applichino misure di sicurezza appropriate e si adattino a specifici ambienti "
            "applicativi."
        ),
        "testo_integrale": (
            "Control objective\n\n"
            "Ensure that the systems on which the application is developed apply appropriate security measures and adapt to specific application environments."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2 (General security measures) — control objective 2",
        "testo": (
            "Obiettivo di controllo: informare l'utente sulle misure di sicurezza raccomandate "
            "quando si usa una SCA/SVA/SAA."
        ),
        "testo_integrale": (
            "Control objective\n\n"
            "Inform the user on recommended security measures when applying a SCA/SVA/SAA."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.3 (System completeness requirements) — control objective 1",
        "testo": (
            "Obiettivo di controllo della clausola: assicurare che un sistema completo implementi tutti "
            "i requisiti obbligatori, inclusi quelli che possono essere implementati indifferentemente "
            "dalla DA oppure dalla SVA/SCA/SAA."
        ),
        "testo_integrale": (
            "Control objective\n\n"
            "Ensure that a complete system implements all the mandatory requirements including those that can be implemented either by the DA or by the SVA/SCA/SAA."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.1 (Introduction)",
        "testo": (
            "Nell'analisi del contesto dell'applicazione di business che implementa le firme si "
            "considerano diversi aspetti giuridici; le clausole seguenti della clausola 6 definiscono "
            "obiettivi di controllo in relazione al trattamento dei dati personali e all'accessibilità "
            "per le persone con disabilità."
        ),
        "testo_integrale": (
            "When analysing the context of the business application implementing signatures, several legal aspects are considered. In the following clauses, control objectives are defined in connection with the processing of personal data and the accessibility for persons with disabilities."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.2 (Processing of personal data) — control objective 1",
        "testo": (
            "Obiettivo di controllo della clausola: assicurare che i dati personali siano trattati in "
            "modo leale e lecito, in conformità alla normativa applicabile in materia di protezione dei "
            "dati personali."
        ),
        "testo_integrale": (
            "Control objective\n\n"
            "Ensure that personal data are processed fairly and lawfully in accordance with applicable personal data protection legislation."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3 (Accessibility for persons with disabilities) — control objective 1",
        "testo": (
            "Obiettivo di controllo della clausola: assicurare che la SCA/SVA/SAA sia accessibile alle "
            "persone con disabilità."
        ),
        "testo_integrale": (
            "Control objective\n\n"
            "Ensure that SCA/SVA/SAA are accessible for persons with disabilities."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 7.1 (Introduction)",
        "testo": (
            "La clausola contiene i requisiti più importanti per la sicurezza delle informazioni e per "
            "i sistemi di gestione della sicurezza delle informazioni (descrizione di dettaglio anche "
            "nella serie ISO/IEC 27000 [i.4]); i controlli definiti coprono l'ambiente in cui sono "
            "applicate la SCA/SVA/SAA e le applicazioni che la richiamano."
        ),
        "testo_integrale": (
            "This clause contains the most important requirements for information security and information security management systems. A detailed description can also be found in the ISO/IEC 27000 series [i.4]. The controls defined in this clause cover the environment in which the SCA/SVA/SAA and the driving applications are applied."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 7.2 (Network protection) — control objective 1",
        "testo": (
            "Obiettivo di controllo della clausola: se la SCA/SVA/SAA riceve o invia dati riservati su "
            "una rete, garantire la protezione di tali dati nelle reti e la protezione dalle minacce "
            "di rete sull'infrastruttura che supporta il trattamento e la conservazione dei dati "
            "riservati."
        ),
        "testo_integrale": (
            "Control objective\n\n"
            "If the SCA/SVA/SAA receives or sends confidential data over a network, guarantee the protection of this data in networks as well as the protection against network threats on the infrastructure supporting the processing and storage of confidential data."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 7.3 (Information systems protection) — control objective 1",
        "testo": (
            "Obiettivo di controllo della clausola: assicurare che i sistemi informativi che trattano "
            "dati di firma e l'ambiente della SCA/SVA/SAA siano protetti da accessi non autorizzati e "
            "uso improprio, generino adeguati allarmi di sicurezza e, ove applicabile, che gli eventi "
            "di sicurezza siano registrati."
        ),
        "testo_integrale": (
            "Control objective\n\n"
            "Ensure that the information systems handling signature data and the environment of the SCA/SVA/SAA are secured against unauthorized access and misuse, trigger suitable security alarms, and, when applicable, that security events are recorded."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 7.4 (Software integrity of the application) — control objective 1",
        "testo": (
            "Obiettivo di controllo della clausola: assicurare che l'integrità della SCA, della SVA, "
            "della SAA e della DA sia adeguatamente protetta."
        ),
        "testo_integrale": (
            "Control objective\n\n"
            "Ensure that integrity of the SCA, SVA, SAA and DA is properly protected."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 7.5 (Data storage security) — control objective 1",
        "testo": (
            "Obiettivo di controllo della clausola: assicurare che nella SCA/SVA/SAA e nell'ambiente "
            "applicativo siano implementate misure appropriate di sicurezza della conservazione dei "
            "dati, a protezione dei dati riservati."
        ),
        "testo_integrale": (
            "Control objective\n\n"
            "Ensure that appropriate data storage security measures are implemented in the SCA/SVA/SAA as well as in the application environment to protect any confidential data."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 7.6 (Event logs) — control objective 1",
        "testo": (
            "Obiettivo di controllo della clausola: usare i registri di eventi nella SCA/SVA/SAA, "
            "nell'applicazione che la richiama o nell'ambiente applicativo per provare le attività "
            "relative alla creazione e alla convalida delle firme, catturando le informazioni che "
            "possono servire come prova successiva."
        ),
        "testo_integrale": (
            "Control objective\n\n"
            "To prove the activities related to the signature creation and validation, use event logs in the SCA/SVA/SAA, the driving application or the application environment to capture information which might be needed for later evidences."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 5.1 (User interface) — control objective 1",
    "clausola 5.1 (User interface) — control objective 2",
    "UI 1",
    "UI 2",
    "clausola 5.2 (General security measures) — control objective 1",
    "clausola 5.2 (General security measures) — control objective 2",
    "GSM 1.1",
    "GSM 1.2",
    "GSM 1.3",
    "GSM 1.4",
    "GSM 1.6",
    "GSM 1.7",
    "GSM 2.1",
    "GSM 2.2",
    "GSM 2.3",
    "GSM 2.4",
    "GSM 2.5",
    "GSM 2.6",
    "GSM 3",
    "clausola 5.3 (System completeness requirements) — control objective 1",
    "SC 1",
    "clausola 6.1 (Introduction)",
    "clausola 6.2 (Processing of personal data) — control objective 1",
    "PD 1",
    "PD 2",
    "clausola 6.3 (Accessibility for persons with disabilities) — control objective 1",
    "APD 1",
    "clausola 7.1 (Introduction)",
    "ISMS 1",
    "ISMS 2",
    "clausola 7.2 (Network protection) — control objective 1",
    "NP 1",
    "NP 2",
    "clausola 7.3 (Information systems protection) — control objective 1",
    "ISP 1",
    "ISP 2",
    "ISP 3",
    "ISP 4",
    "ISP 5",
    "clausola 7.4 (Software integrity of the application) — control objective 1",
    "SIA 1",
    "SIA 2",
    "SIA 3",
    "SIA 4",
    "clausola 7.5 (Data storage security) — control objective 1",
    "DSS 1",
    "DSS 2",
    "DSS 3",
    "DSS 4",
    "clausola 7.6 (Event logs) — control objective 1",
    "EL 1",
    "EL 2",
    "EL 3",
    "EL 4",
    "EL 5",
    "EL 6",
    "EL 7",
    "EL 8",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []