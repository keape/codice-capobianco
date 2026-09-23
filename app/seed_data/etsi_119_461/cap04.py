"""ETSI TS 119 461 V2.1.1 (2025-02) - Policy and security requirements for trust
service components providing identity proofing of trust service subjects. Fonte 9
(cablaggio in seed.py demandato a un'altra sessione). Questo modulo copre clausola 8.1
"Initiation" (requisiti INI-8.1-XX) e clausola 8.2 "Attribute and evidence collection"
(sottoclausole 8.2.1-8.2.9, requisiti COL-8.2.x-XX).
Testo ufficiale: app/.source_cache/etsi_119_461/cap04.txt.

Nota terminologica: l'assegnazione di lavoro per questo capitolo indicava id di esempio
con prefisso "ATT-" (es. "ATT-8.2-03"). Il testo ufficiale della clausola 8.2 usa invece
sistematicamente il prefisso "COL-" (es. "COL-8.2.1-01X") - "Requirements on attribute
and evidence collection", confermato anche dalla legenda ufficiale di clausola 3.4
"Notations" letta dal capitolo che copre clausola 1-4 (nessun prefisso "ATT" esiste nel
documento). Tutti i `riferimento` di questo modulo usano quindi "COL-", il prefisso
letterale del testo, come richiesto dalla convenzione "riferimento esatto come appare
nel testo".

Modellazione (ADR-0007):
- "shall"/"shall not" con soggetto individuabile (l'IPSP/il processo di identity
  proofing, cioe' il TSP o il suo componente di identity proofing) -> Obbligo, categoria
  "QTSP/gestore", ruolo "obbligato".
- "should"/"should not" (raccomandazione RFC 2119, piu' debole di "shall" ma comunque
  dotata di un proprio requirement id numerato nel testo) e "may"/"may not"
  (facolta') -> Principio, tipo_principio "altro" (non "definitorio" ne' "scopo/ambito":
  sono raccomandazioni o facolta' operative su un singolo requisito, non definizioni ne'
  disposizioni di scopo). Stesso criterio ("may" -> Principio) gia' usato in
  etsi_319_412_5/cap01.py, esteso qui a "should" per coerenza (entrambi non impongono un
  obbligo vincolante in senso stretto, a differenza di "shall").
- tipo_obbligo: "tecnico/sicurezza" per i requisiti che impongono direttamente un'azione
  tecnica di raccolta/validazione/verifica su attributi o evidenze (default per la
  famiglia COL, come da assegnazione); "procedurale" per i requisiti che impongono di
  documentare un aspetto del processo nella identity proofing practice statement (cosa
  deve essere descritto in policy - liste di mezzi/documenti/registri accettati, casi
  d'uso supportati, condizioni di accettazione), distinti dai requisiti che impongono
  un'azione tecnica diretta; "informativo/trasparenza" per i requisiti INI che
  riguardano informazione/consenso del richiedente prima dell'avvio del processo;
  "organizzativo" per INI-8.1-04 (accessibilita' del servizio a persone con disabilita' -
  requisito di disegno organizzativo del servizio, non un controllo tecnico ne' un
  obbligo informativo in senso stretto).
- Categoria soggetto: "QTSP/gestore" (obbligato) per tutti i requisiti INI/COL il cui
  soggetto e' il TSP/IPSP. "Utente/titolare" (destinatario) aggiunto sui soli requisiti
  INI che hanno il richiedente (applicant) come beneficiario esplicito di
  informazione/accessibilita' (INI-8.1-01X, INI-8.1-03X, INI-8.1-04): i requisiti COL
  non hanno mai il richiedente come destinatario esplicito, essendo tutti formulati come
  azioni interne del processo di identity proofing (raccolta/validazione), non
  transazioni informative verso il richiedente.
- Clausole [CONDITIONAL] a livello di (sotto)clausola (es. "[CONDITIONAL] If the
  applicant is a natural person, the requirements in the present clause apply.",
  presenti in apertura delle sottoclausole 8.2.2.1, 8.2.2.2, 8.2.2.3, 8.2.3, 8.2.4, 8.2.5,
  8.2.6, 8.2.7, 8.2.8, 8.2.9): non generano un proprio nodo Principio/Obbligo, perche'
  prive di contenuto sostanziale autonomo oltre alla delimitazione di applicabilita' dei
  requisiti numerati che seguono (analogo al trattamento di "void" in etsi_319_412_5:
  mero rinvio strutturale, qui un mero gate condizionale). Il loro contenuto e' invece
  riportato nel campo `condizione_applicabilita` di CIASCUN requisito numerato della
  sottoclausola che non abbia gia' una propria condizione [CONDITIONAL] piu' specifica.
  Quando un requisito numerato ha una propria etichetta "[CONDITIONAL]" con una
  condizione piu' specifica (es. COL-8.2.3-04X "se sono usati documenti fisici come
  evidenza autoritativa", nidificata dentro il gate piu' ampio di clausola 8.2.3 "se sono
  usati documenti fisici/digitali come evidenza"), si usa la condizione specifica (che
  logicamente implica quella piu' ampia della sottoclausola).
- **[CONDITIONAL] COL-8.2.4-04** e **[CONDITIONAL] COL-8.2.5-05** sono "VOID, moved to
  clause C.2" nel testo: nessun contenuto autonomo oltre al rinvio strutturale -> nessun
  nodo, stesso trattamento di "void" in etsi_319_412_5.
- NOTE/EXAMPLE annessi a un requisito: assorbiti in `testo_integrale` (dopo l'id del
  requisito) solo quando aggiungono una condizione/eccezione/precisazione sostanziale al
  requisito (es. NOTE 7 su COL-8.2.2.1-02A: l'esito pseudonimo non esonera dall'accertare
  l'identita' reale; NOTE 3/4 su COL-8.2.3-02X: eccezione per evidenza supplementare senza
  foto, perimetro limitato a biometria del volto; NOTE 7 su COL-8.2.3-05X: significato
  operativo di "forma originale"; NOTE 4 su COL-8.2.5-02: il campo Subject non prova da
  solo l'autorizzazione a rappresentare). Le pure esemplificazioni (EXAMPLE, e NOTE senza
  contenuto normativo aggiuntivo, es. mero rinvio a atti/standard esterni o spiegazioni
  del "perche'" senza una nuova condizione) sono scartate.
- Le sottoclausole 8.2.2.3 (COL-8.2.2.3-01/-02) e 8.2.9 (COL-8.2.9-01/-02) rinviano per
  relationem a un'INTERA sottoclausola (rispettivamente 8.2.2.1/8.2.2.2 e 8.2.3-8.2.8),
  non a un singolo requisito puntuale: nessuna relazione interna e' stata creata per
  questi rinvii, in applicazione del criterio "in caso di dubbio ometti la relazione"
  (un arco RELAZIONI ha un solo nodo_a, mentre questi rinvii hanno piu' target candidati
  senza un requisito puntuale da preferire). Per lo stesso motivo non sono state create
  relazioni per il rinvio di COL-8.2.3-02X (NOTE) alla clausola 8.4 (Binding, fuori da
  questo capitolo) ne' per i "moved to clause C.2" dei due requisiti VOID. Nessuna
  citazione a un id di requisito puntuale di un'ALTRA sottoclausola di questo stesso
  capitolo e' stata trovata nel testo -> RELAZIONI e' vuoto per questo modulo.
- Copertura completa (ADR-0007): 60 nodi per 62 id di requisito presenti nel testo, meno
  i 2 "VOID" senza contenuto proprio (COL-8.2.4-04, COL-8.2.5-05).
"""

RIGHE_OBBLIGHI = [
    {
        'riferimento': 'INI-8.1-01X',
        'testo': "Prima dell'avvio del processo di identity proofing, il richiedente (applicant) deve essere informato dello scopo del processo e dei relativi termini e condizioni, richiesti dal contesto di identity proofing, e deve accettarli attivamente prima che il processo abbia inizio.",
        'testo_integrale': "8.1 Initiation — INI-8.1-01X: The applicant shall be informed of, and shall actively accept before the identity proofing process is started, the purpose of the identity proofing and the related terms and conditions as required by the identity proofing context.",
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}, {'categoria': 'Utente/titolare', 'ruolo': 'destinatario'}],
    },
    {
        'riferimento': 'INI-8.1-03X',
        'testo': "Il richiedente deve ricevere indicazioni chiare su come sara' condotto il processo di identity proofing, sulle informazioni identificative che saranno raccolte, su quali dati sono conservati e per quanto tempo, sulle evidenze che e' tenuto a presentare e su qualsiasi strumento che e' tenuto a utilizzare.",
        'testo_integrale': "8.1 Initiation — INI-8.1-03X: The applicant shall receive clear guidance regarding how the identity proofing process will be carried out, regarding the identity information that will be collected, regarding what data is kept and for how long, regarding the evidence that the applicant is required to present, and regarding any tool that the applicant is required to use.",
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}, {'categoria': 'Utente/titolare', 'ruolo': 'destinatario'}],
    },
    {
        'riferimento': 'INI-8.1-04',
        'testo': "Il processo di identity proofing, o almeno un processo se sono disponibili processi alternativi, deve essere accessibile alle persone con disabilita' conformemente alla legislazione applicabile.",
        'testo_integrale': "8.1 Initiation — INI-8.1-04: The identity proofing process, or at least one process if alternative processes are available, shall be available to persons with disabilities in accordance with the applicable legislation.",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}, {'categoria': 'Utente/titolare', 'ruolo': 'destinatario'}],
    },
    {
        'riferimento': 'COL-8.2.1-01X',
        'testo': "Per ciascun contesto di identity proofing devono essere definiti gli attributi identificativi obbligatori e quelli facoltativi da raccogliere.",
        'testo_integrale': "8.2.1 General requirements — COL-8.2.1-01X: Mandatory and optional identity attributes to collect shall be defined for each identity proofing context.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.1-01A',
        'testo': "Tutti gli attributi obbligatori per uno specifico contesto di identity proofing devono essere raccolti.",
        'testo_integrale': "8.2.1 General requirements — COL-8.2.1-01A: All mandatory attributes for a specific identity proofing context shall be collected.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.1-02',
        'testo': "Gli attributi identificativi raccolti devono garantire l'identificazione univoca del richiedente nel contesto di identity proofing.",
        'testo_integrale': "8.2.1 General requirements — COL-8.2.1-02: The identity attributes collected shall provide unique identification of the applicant for the identity proofing context.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.1-03X',
        'testo': "Gli attributi identificativi raccolti devono essere convalidati mediante una o piu' evidenze autoritative e, facoltativamente, una o piu' evidenze supplementari.",
        'testo_integrale': "8.2.1 General requirements — COL-8.2.1-03X: The identity attributes collected shall be validated by use of one or more authoritative evidence and optionally one or more supplementary evidence.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.1-04',
        'testo': "L'evidenza raccolta deve soddisfare i requisiti del contesto di identity proofing.",
        'testo_integrale': "8.2.1 General requirements — COL-8.2.1-04: The evidence collected shall meet the requirements of the identity proofing context.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.1-05',
        'testo': "L'evidenza deve essere rilasciata da soggetti considerati affidabili nel contesto di identity proofing.",
        'testo_integrale': "8.2.1 General requirements — COL-8.2.1-05: The evidence shall be issued by entities trusted in the identity proofing context.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.1-06X',
        'testo': "L'identity proofing practice statement deve individuare l'elenco dei casi d'uso di identity proofing supportati, l'evidenza autoritativa (e facoltativamente supplementare) considerata affidabile e, per quanto possibile, i contesti di identity proofing supportati.",
        'testo_integrale': "8.2.1 General requirements — COL-8.2.1-06X: The identity proofing practice statement shall identify a list of the identity proofing use cases supported, the authoritative and optionally supplementary evidence that shall be trusted, and, as far as possible, the identity proofing contexts supported.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.1-07',
        'testo': "La freschezza degli attributi identificativi ottenuti dall'evidenza deve essere valutata rispetto ai requisiti di freschezza del contesto di identity proofing.",
        'testo_integrale': "8.2.1 General requirements — COL-8.2.1-07: The freshness of the identity attributes obtained from evidence shall be evaluated against the freshness requirements of the identity proofing context.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.2.1-01X',
        'testo': "Per ciascun contesto di identity proofing supportato, l'identity proofing practice statement deve individuare i mezzi utilizzati per raccogliere gli attributi identificativi di una persona fisica (es. da documento di identita' fisico o digitale, da eID, da certificato di firma digitale, direttamente dal richiedente con validazione successiva, da fonti autoritative o da fonti ausiliarie).",
        'testo_integrale': "8.2.2.1 Attribute collection for natural person — [CONDITIONAL] If the applicant is a natural person, the requirements in the present clause apply. COL-8.2.2.1-01X: The identity proofing practice statement shall identify for each identity proofing context supported, the means used to collect identity attributes for a natural person (examples: from a physical or digital identity document; from the use of an eID authenticating the applicant; from a certificate supporting a digital signature applied by the applicant; directly from the applicant, subject to validation against authoritative sources; from authoritative sources such as public registers; from existing information in auxiliary data sources; from other documents or sources).",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente (applicant) e' una persona fisica (natural person) — clausola 8.2.2.1.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.2.1-02',
        'testo': "Se il richiedente e' una persona fisica, devono essere raccolti almeno i seguenti attributi: a) cognome/i, nome/i, preferibilmente i nomi correnti; b) ulteriori informazioni necessarie a identificare univocamente il richiedente come persona fisica nel contesto di identity proofing.",
        'testo_integrale': "8.2.2.1 Attribute collection for natural person — COL-8.2.2.1-02: The following attributes shall at a minimum be collected if the applicant is a natural person: a) family name(s), first name(s), which should be current names; b) further information as needed to uniquely identify the applicant as a natural person in the identity proofing context.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica — clausola 8.2.2.1.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.2.1-03',
        'testo': "Gli attributi da raccogliere devono essere determinati dal contesto di identity proofing.",
        'testo_integrale': "8.2.2.1 Attribute collection for natural person — COL-8.2.2.1-03: The attributes to collect shall be as determined by the identity proofing context.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica — clausola 8.2.2.1.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.2.1-04',
        'testo': "Il processo di identity proofing non deve raccogliere attributi identificativi che non sono inclusi nel risultato dell'identity proofing, salvo quando tali attributi sono necessari per la validazione di attributi/evidenza e/o per il binding al richiedente.",
        'testo_integrale': "8.2.2.1 Attribute collection for natural person — COL-8.2.2.1-04: The identity proofing process shall not collect identity attributes that are not included in the result of the identity proofing, except when such attributes are required for attribute and evidence validation and/or binding to applicant.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica — clausola 8.2.2.1.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.2.2-01X',
        'testo': "Per ciascun contesto di identity proofing supportato, l'identity proofing practice statement deve individuare i mezzi utilizzati per raccogliere gli attributi identificativi di una persona giuridica.",
        'testo_integrale': "8.2.2.2 Attribute collection for legal person — [CONDITIONAL] If the applicant is a legal person, the requirements in the present clause apply. COL-8.2.2.2-01X: For each identity proofing context supported, the means used to collect identity attributes for a legal person shall be identified by the identity proofing practice statement.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona giuridica (legal person) — clausola 8.2.2.2.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.2.2-02',
        'testo': "Gli attributi raccolti devono identificare univocamente il richiedente come persona giuridica nel contesto di identity proofing.",
        'testo_integrale': "8.2.2.2 Attribute collection for legal person — COL-8.2.2.2-02: The attributes collected shall uniquely identify the applicant as a legal person in the identity proofing context.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona giuridica — clausola 8.2.2.2.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.2.2-03',
        'testo': "Se il richiedente e' una persona giuridica, devono essere raccolti almeno i seguenti attributi: a) denominazione completa della persona giuridica; b) paese di registrazione; c) identificativo univoco e relativo tipo (salvo che tale identificativo non esista).",
        'testo_integrale': "8.2.2.2 Attribute collection for legal person — COL-8.2.2.2-03: The following attributes shall, as a minimum, be collected if the applicant is a legal person: a) full name of the legal person; b) country of registration of the legal person; c) unique identifier and type of identifier for the legal person (unless such identifier does not exist).",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona giuridica — clausola 8.2.2.2.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.2.3-01',
        'testo': "Gli attributi identificativi della persona fisica devono essere raccolti secondo i requisiti della clausola 8.2.2.1.",
        'testo_integrale': "8.2.2.3 Attribute collection for natural person representing legal person — [CONDITIONAL] If the applicant is a natural person representing a legal person, the requirements in the present clause apply. COL-8.2.2.3-01: Identity attributes for the natural person shall be collected according to the requirements in clause 8.2.2.1 of the present document.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica che rappresenta una persona giuridica — clausola 8.2.2.3.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.2.3-02',
        'testo': "Gli attributi identificativi della persona giuridica devono essere raccolti secondo i requisiti della clausola 8.2.2.2.",
        'testo_integrale': "8.2.2.3 Attribute collection for natural person representing legal person — COL-8.2.2.3-02: Identity attributes for the legal person shall be collected according to the requirements in clause 8.2.2.2 of the present document.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica che rappresenta una persona giuridica — clausola 8.2.2.3.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.2.3-03',
        'testo': "Devono essere raccolti il ruolo della persona fisica rispetto alla persona giuridica e l'individuazione della fonte dell'autorizzazione della persona fisica a rappresentare la persona giuridica.",
        'testo_integrale': "8.2.2.3 Attribute collection for natural person representing legal person — COL-8.2.2.3-03: The role of the natural person with respect to the legal person and identification of the source of the authorization of the natural person to represent the legal person shall be collected.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica che rappresenta una persona giuridica — clausola 8.2.2.3.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.3-01X',
        'testo': "Un documento di identita' utilizzato come evidenza deve essere in forma fisica o digitale.",
        'testo_integrale': "8.2.3 Use of physical or digital identity document as evidence — [CONDITIONAL] If physical and/or digital identity documents are used as evidence, the requirements in the present clause apply. COL-8.2.3-01X: An identity document used as evidence shall be in physical or digital form.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando come evidenza vengono utilizzati documenti di identita' fisici e/o digitali — clausola 8.2.3.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.3-02X',
        'testo': "Un documento utilizzato come evidenza autoritativa deve contenere una fotografia del volto e/o altre informazioni che consentano di identificare univocamente il richiedente confrontandolo con il suo aspetto fisico. Cio' non esclude l'uso, come evidenza supplementare, di documenti privi di fotografia o informazioni analoghe; il presente documento specifica requisiti di binding al richiedente solo tramite biometria del volto e/o verifica manuale del volto, senza escludere l'uso di altre biometrie.",
        'testo_integrale': "8.2.3 Use of physical or digital identity document as evidence — COL-8.2.3-02X: A document used as authoritative evidence shall contain a face photo and/or other information that can be used to uniquely identify the applicant when compared with the applicant's physical appearance. NOTE 3: This does not exclude the use of documents without a face photo or similar information as supplementary evidence. NOTE 4: The present document only specifies requirements for binding to applicant using face biometrics and/or manual face verification; it does not exclude the possibility of using other biometrics, e.g. fingerprint or iris, but does not specify requirements for such use cases.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando come evidenza vengono utilizzati documenti di identita' fisici e/o digitali — clausola 8.2.3.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.3-03X',
        'testo': "Per ciascun contesto di identity proofing supportato, l'identity proofing practice statement deve individuare un elenco dei documenti di identita' accettati.",
        'testo_integrale': "8.2.3 Use of physical or digital identity document as evidence — COL-8.2.3-03X: For each identity proofing context supported, a list of the identity documents that are accepted shall be identified by the identity proofing practice statement.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando come evidenza vengono utilizzati documenti di identita' fisici e/o digitali — clausola 8.2.3.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.3-04X',
        'testo': "Se come evidenza autoritativa sono utilizzati documenti di identita' fisici, devono essere accettati solo passaporti, carte d'identita' nazionali e altri documenti di identita' ufficiali che, secondo il contesto di identity proofing, offrono un'affidabilita' pari o superiore; il giudizio di affidabilita' comparabile deve basarsi su una valutazione delle caratteristiche di sicurezza e del processo di rilascio dell'altro documento rispetto a quelle di passaporto e/o carta d'identita'.",
        'testo_integrale': "8.2.3 Use of physical or digital identity document as evidence — [CONDITIONAL] COL-8.2.3-04X: If physical identity documents are used as authoritative evidence, only passports, national identity cards and other official identity documents that according to the identity proofing context offer the same or higher reliability of the identity shall be accepted, where the judgement on comparable reliability shall be based on an assessment of the security features and issuance process of the other identity document towards the security features and issuance process of passport and/or identity card.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se come evidenza autoritativa sono utilizzati documenti di identita' fisici.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.3-05X',
        'testo': "Se un documento di identita' fisico e' utilizzato come evidenza, l'IPSP deve verificare che il documento sia presentato nella sua forma originale (il richiedente deve presentare l'originale per provare il possesso del documento; il processo puo' successivamente acquisirne un'altra rappresentazione, es. video, immagine o scansione).",
        'testo_integrale': "8.2.3 Use of physical or digital identity document as evidence — [CONDITIONAL] COL-8.2.3-05X: If a physical identity document is used as evidence, the IPSP shall verify that the document is presented in its original form. NOTE 7: Meaning the applicant is required to present the original in the identity proofing process to evidence proof of possession of the identity document; the identity proofing process can subsequently capture another representation of the document, e.g. by a video sequence, image, or scan.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se un documento di identita' fisico e' utilizzato come evidenza.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.3-06X',
        'testo': "Se come evidenza autoritativa sono utilizzati documenti di identita' digitali, devono essere accettati solo documenti di identita' digitali eMRTD conformi a ICAO 9303 parte 10 e altri documenti digitali che, secondo il contesto di identity proofing, offrono affidabilita' pari o superiore, valutata rispetto alle caratteristiche di sicurezza e al processo di rilascio richiesti da ICAO 9303 parte 10.",
        'testo_integrale': "8.2.3 Use of physical or digital identity document as evidence — [CONDITIONAL] COL-8.2.3-06X: If digital identity documents are used as authoritative evidence, only eMRTD digital identity documents according to ICAO 9303 part 10 [2] and other digital documents that according to the identity proofing context offer the same or higher reliability of the identity shall be accepted, where the judgement on comparable reliability shall be based on an assessment of the security features and issuance process of the other identity document towards the security features and issuance process required by ICAO 9303 part 10 [2].",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se come evidenza autoritativa sono utilizzati documenti di identita' digitali.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.3-07',
        'testo': "Se gli attributi richiesti non possono essere validati mediante il documento di identita', tali attributi devono essere raccolti da altre fonti e validati, incluso valutare che siano vincolati (bound) al richiedente, mediante l'uso di altre fonti autoritative in conformita' al contesto di identity proofing.",
        'testo_integrale': "8.2.3 Use of physical or digital identity document as evidence — [CONDITIONAL] COL-8.2.3-07: If required attributes to be collected cannot be validated by the identity document, these attributes shall be collected from other sources and validated, including assessing that the attributes are bound to the applicant, by use of other authoritative sources in accordance with the identity proofing context.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se gli attributi richiesti non possono essere validati mediante il documento di identita'.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.4-01X',
        'testo': "Per ciascun contesto di identity proofing supportato, l'identity proofing practice statement deve individuare le condizioni che un eID o uno schema eID deve soddisfare per essere accettato ai fini dell'identity proofing.",
        'testo_integrale': "8.2.4 Use of existing eID means as evidence — [CONDITIONAL] If existing eID means for authentication is used as evidence, the requirements in the present clause apply. COL-8.2.4-01X: For each identity proofing context supported, the conditions that an eID or eID scheme is required to fulfil to be accepted for identity proofing shall be identified by the identity proofing practice statement.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando come evidenza viene utilizzato un mezzo di identificazione elettronica (eID) esistente — clausola 8.2.4.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.4-02X',
        'testo': "Se e' previsto (targeted) il Baseline LoIP, l'eID deve conformarsi almeno al livello eIDAS LoA substantial oppure a un altro framework di livelli di garanzia che offra un'assicurazione comparabile a eIDAS LoA substantial.",
        'testo_integrale': "8.2.4 Use of existing eID means as evidence — [CONDITIONAL] COL-8.2.4-02X: If the Baseline LoIP is targeted, the eID shall at least conform to eIDAS LoA substantial or conform to another assurance level framework offering comparable assurance to eIDAS LoA substantial.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se e' previsto (targeted) il Baseline LoIP.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.4-02A',
        'testo': "Se e' previsto (targeted) l'Extended LoIP, l'eID deve conformarsi al livello eIDAS LoA high oppure a un altro framework di livelli di garanzia che offra un'assicurazione comparabile a eIDAS LoA high.",
        'testo_integrale': "8.2.4 Use of existing eID means as evidence — [CONDITIONAL] COL-8.2.4-02A: If the Extended LoIP is targeted, the eID shall conform to eIDAS LoA high or conform to another assurance level framework offering comparable assurance to eIDAS LoA high.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se e' previsto (targeted) l'Extended LoIP.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.4-03X',
        'testo': "Se gli attributi richiesti non possono essere validati mediante l'autenticazione con il mezzo eID, tali attributi devono essere raccolti da altre fonti e validati, incluso valutare che siano vincolati al richiedente, mediante l'uso di altre fonti autoritative in conformita' al contesto di identity proofing.",
        'testo_integrale': "8.2.4 Use of existing eID means as evidence — [CONDITIONAL] COL-8.2.4-03X: If required attributes to be collected cannot be validated by the authentication using the eID means, these attributes shall be collected from other sources and validated, including assessing that the attributes are bound to the applicant, by use of other authoritative sources in accordance with the identity proofing context.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se gli attributi richiesti non possono essere validati mediante l'autenticazione con il mezzo eID.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.5-01X',
        'testo': "Per ciascun contesto di identity proofing supportato, l'identity proofing practice statement deve individuare le condizioni alle quali firme digitali e certificati sono accettati.",
        'testo_integrale': "8.2.5 Use of existing digital signature means as evidence — [CONDITIONAL] If an existing digital signature means with a supporting certificate is used as evidence, the requirements in the present clause apply. COL-8.2.5-01X: For each identity proofing context supported, the conditions under which digital signatures and certificates are accepted shall be identified by the identity proofing practice statement.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando come evidenza viene utilizzato un mezzo di firma digitale esistente con certificato di supporto — clausola 8.2.5.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.5-03X',
        'testo': "Se e' dichiarato (claimed) il Baseline LoIP, il certificato della firma digitale deve essere stato rilasciato sulla base di un identity proofing effettuato a livello Baseline o Extended LoIP.",
        'testo_integrale': "8.2.5 Use of existing digital signature means as evidence — [CONDITIONAL] COL-8.2.5-03X: If the Baseline LoIP is claimed, the certificate of the digital signature shall have been issued based on identity proofing to Baseline or Extended LoIP.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se e' dichiarato (claimed) il Baseline LoIP.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.5-03A',
        'testo': "Se e' dichiarato (claimed) l'Extended LoIP, il certificato della firma digitale deve essere stato rilasciato sulla base di un identity proofing effettuato a livello Extended LoIP.",
        'testo_integrale': "8.2.5 Use of existing digital signature means as evidence — [CONDITIONAL] COL-8.2.5-03A: If the Extended LoIP is claimed, the certificate of the digital signature shall have been issued based on identity proofing to Extended LoIP.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se e' dichiarato (claimed) l'Extended LoIP.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.5-04X',
        'testo': "Se gli attributi richiesti non sono presenti nel certificato, tali attributi devono essere raccolti da altre fonti e validati, incluso valutare che siano vincolati al richiedente, mediante l'uso di altre fonti autoritative in conformita' al contesto di identity proofing.",
        'testo_integrale': "8.2.5 Use of existing digital signature means as evidence — [CONDITIONAL] COL-8.2.5-04X: If required attributes to be collected are not present in the certificate, these attributes shall be collected from other sources and validated, including assessing that the attributes are bound to the applicant, by use of other authoritative sources in accordance with the identity proofing context.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se gli attributi richiesti non sono presenti nel certificato.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.5-06X',
        'testo': "La firma digitale deve essere apposta sotto garanzia di controllo esclusivo (sole control) del firmatario quando il firmatario e' una persona fisica, e sotto garanzia di controllo quando il firmatario e' una persona giuridica.",
        'testo_integrale': "8.2.5 Use of existing digital signature means as evidence — COL-8.2.5-06X: The digital signature shall be made under a guarantee of sole control by the signer when the signer is a natural person and under a guarantee of control when the signer is a legal person.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando come evidenza viene utilizzato un mezzo di firma digitale esistente con certificato di supporto — clausola 8.2.5.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.6-01X',
        'testo': "Per ciascun contesto di identity proofing supportato, l'identity proofing practice statement deve individuare un elenco dei registri fidati utilizzati per raccogliere e/o validare gli attributi, e se la consultazione di tali registri e' obbligatoria o facoltativa.",
        'testo_integrale': "8.2.6 Use of trusted register as supplementary evidence — [CONDITIONAL] If a trusted register is used as supplementary evidence, the requirements in the present clause apply. COL-8.2.6-01X: For each identity proofing context supported, a list of the trusted registers used to collect and/or validate attributes, and whether lookup in these registers is mandatory or optional, shall be identified by the identity proofing practice statement.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando come evidenza supplementare viene utilizzato un registro fidato (trusted register) — clausola 8.2.6.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.6-01A',
        'testo': "Gli attributi raccolti da un registro fidato devono essere collegati in modo affidabile al richiedente.",
        'testo_integrale': "8.2.6 Use of trusted register as supplementary evidence — COL-8.2.6-01A: Attributes collected from a trusted register shall be reliably linked to the applicant.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando come evidenza supplementare viene utilizzato un registro fidato (trusted register) — clausola 8.2.6.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.6-03X',
        'testo': "Se il richiedente e' una persona giuridica ed e' registrato in un registro fidato disponibile accettato come fonte autoritativa, tale registro deve essere utilizzato per la raccolta e/o validazione degli attributi della persona giuridica.",
        'testo_integrale': "8.2.6 Use of trusted register as supplementary evidence — [CONDITIONAL] COL-8.2.6-03X: If the applicant is a legal person and is registered in an available trusted register accepted as authoritative source, this register shall be used for collection and/or validation of the attributes of the legal person.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se il richiedente e' una persona giuridica ed e' registrato in un registro fidato disponibile accettato come fonte autoritativa.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.7-01X',
        'testo': "Per ciascun contesto di identity proofing supportato, l'identity proofing practice statement deve individuare un elenco dei meccanismi di prova di accesso richiesti o accettati come evidenza supplementare e gli attributi raccolti e/o validati da tali meccanismi.",
        'testo_integrale': "8.2.7 Use of proof of access as supplementary evidence — [CONDITIONAL] If proof of access is used as supplementary evidence, the requirements in the present clause apply. COL-8.2.7-01X: For each identity proofing context supported, a list of the proof of access mechanisms that are required or accepted as supplementary evidence of identity and the attributes that are collected and/or validated from these mechanisms shall be identified by the identity proofing practice statement.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando come evidenza supplementare viene utilizzata una prova di accesso (proof of access) — clausola 8.2.7.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.7-02',
        'testo': "Gli attributi restituiti dalla prova di accesso devono essere collegati in modo affidabile al richiedente.",
        'testo_integrale': "8.2.7 Use of proof of access as supplementary evidence — COL-8.2.7-02: The attributes returned from the proof of access shall be reliably linked to the applicant.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando come evidenza supplementare viene utilizzata una prova di accesso (proof of access) — clausola 8.2.7.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.7-03X',
        'testo': "L'affidabilita' degli attributi ottenuti dai meccanismi di prova di accesso deve essere valutata e deve essere sufficiente per il contesto di identity proofing.",
        'testo_integrale': "8.2.7 Use of proof of access as supplementary evidence — COL-8.2.7-03X: The reliability of attributes obtained from proof of access mechanisms shall be evaluated and be sufficient for the identity proofing context.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando come evidenza supplementare viene utilizzata una prova di accesso (proof of access) — clausola 8.2.7.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.8-01X',
        'testo': "Per ciascun contesto di identity proofing supportato, l'identity proofing practice statement deve individuare un elenco dei documenti e/o attestazioni richiesti o accettati come evidenza supplementare e gli attributi raccolti o validati da tale documentazione.",
        'testo_integrale': "8.2.8 Use of documents and attestations as supplementary evidence — [CONDITIONAL] If documents and attestations are used as supplementary evidence, the requirements in the present clause apply. COL-8.2.8-01X: For each identity proofing context supported, a list of the documents and/or attestations required or accepted as supplementary evidence of identity and the attributes that are collected or validated from this documentation shall be identified by the identity proofing practice statement.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando come evidenza supplementare vengono utilizzati documenti e attestazioni — clausola 8.2.8.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.8-01A',
        'testo': "Gli attributi raccolti da documenti e attestazioni devono essere collegati in modo affidabile al richiedente.",
        'testo_integrale': "8.2.8 Use of documents and attestations as supplementary evidence — COL-8.2.8-01A: Attributes collected from documents and attestations shall be reliably linked to the applicant.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando come evidenza supplementare vengono utilizzati documenti e attestazioni — clausola 8.2.8.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.8-03X',
        'testo': "L'affidabilita' degli attributi ottenuti da documenti e attestazioni deve essere valutata e deve essere sufficiente per il contesto di identity proofing.",
        'testo_integrale': "8.2.8 Use of documents and attestations as supplementary evidence — COL-8.2.8-03X: The reliability of attributes obtained from documents and attestations shall be evaluated and be sufficient for the identity proofing context.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando come evidenza supplementare vengono utilizzati documenti e attestazioni — clausola 8.2.8.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.9-01',
        'testo': "L'evidenza dell'identita' della persona fisica deve essere raccolta secondo i requisiti pertinenti delle clausole da 8.2.3 a 8.2.8.",
        'testo_integrale': "8.2.9 Evidence collection for natural person representing legal person — [CONDITIONAL] If the applicant is a natural person purporting to represent a legal person, the requirements in the present clause apply. COL-8.2.9-01: Evidence for the natural person's identity shall be collected according to the relevant requirements from clauses 8.2.3 to 8.2.8 of the present document.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica che dichiara di rappresentare una persona giuridica — clausola 8.2.9.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.9-02',
        'testo': "L'evidenza dell'identita' della persona giuridica deve essere raccolta secondo i requisiti pertinenti delle clausole da 8.2.3 a 8.2.8.",
        'testo_integrale': "8.2.9 Evidence collection for natural person representing legal person — COL-8.2.9-02: Evidence for the legal person's identity shall be collected according to the relevant requirements from clauses 8.2.3 to 8.2.8 of the present document.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica che dichiara di rappresentare una persona giuridica — clausola 8.2.9.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.9-03X',
        'testo': "Per ciascun contesto di identity proofing supportato, l'identity proofing practice statement deve individuare i mezzi accettati per evidenziare il collegamento tra l'identita' della persona fisica e quella della persona giuridica.",
        'testo_integrale': "8.2.9 Evidence collection for natural person representing legal person — COL-8.2.9-03X: For each identity proofing context supported, the accepted means to evidence the link between the natural person's identity and the legal person's identity shall be identified by the identity proofing practice statement.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica che dichiara di rappresentare una persona giuridica — clausola 8.2.9.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.9-04X',
        'testo': "Per ciascun contesto di identity proofing supportato, le posizioni, i ruoli o le altre relazioni accettati affinche' una persona fisica rappresenti una persona giuridica devono essere individuati nell'identity proofing practice statement.",
        'testo_integrale': "8.2.9 Evidence collection for natural person representing legal person — COL-8.2.9-04X: For each identity proofing context supported, the positions, roles, or other relationships accepted for a natural person to represent a legal person shall be identified in the identity proofing practice statement.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica che dichiara di rappresentare una persona giuridica — clausola 8.2.9.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.9-05X',
        'testo': "Per ciascun contesto di identity proofing supportato, l'identity proofing practice statement deve individuare ogni requisito di freschezza (attualita') applicabile a dichiarazioni o documenti relativi alla relazione tra la persona fisica e la persona giuridica.",
        'testo_integrale': "8.2.9 Evidence collection for natural person representing legal person — COL-8.2.9-05X: For each identity proofing context supported, any freshness (current) requirement applicable to any statement or document regarding the natural person's relationship to the legal person shall be identified by the identity proofing practice statement.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica che dichiara di rappresentare una persona giuridica — clausola 8.2.9.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.9-06X',
        'testo': "Se la persona giuridica e' elencata in un registro fidato, il ruolo della persona fisica rispetto alla persona giuridica deve essere raccolto da tale registro o validato rispetto ad esso, nella misura in cui il registro sia accessibile e gli attributi richiesti siano presenti nel registro.",
        'testo_integrale': "8.2.9 Evidence collection for natural person representing legal person — [CONDITIONAL] COL-8.2.9-06X: If the legal person is listed in a trusted register, the role of the natural person concerning the legal person shall be collected from or validated against this register to the extent that the register is accessible and that the required attributes are present in the register.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se la persona giuridica e' elencata in un registro fidato.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'COL-8.2.9-07X',
        'testo': "Se la persona giuridica non e' elencata in un registro fidato, oppure gli attributi richiesti per raccogliere o validare il ruolo della persona fisica rispetto alla persona giuridica non sono presenti nel registro, tale ruolo deve essere raccolto o validato con altri mezzi che offrano la stessa affidabilita' di un registro fidato.",
        'testo_integrale': "8.2.9 Evidence collection for natural person representing legal person — [CONDITIONAL] COL-8.2.9-07X: If the legal person is not listed in a trusted register, or the required attributes to collect or validate the role of the natural person concerning the legal person are not present in the register, the role of the natural person concerning the legal person shall be collected or validated by other means providing the same confidence as a trusted register would do.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se la persona giuridica non e' elencata in un registro fidato, oppure gli attributi richiesti non sono presenti nel registro.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
]

RIGHE_PRINCIPI = [
    {
        'riferimento': 'INI-8.1-02X',
        'testo': "Se sono disponibili processi di identity proofing alternativi per raggiungere lo scopo dell'identity proofing, il richiedente dovrebbe poter scegliere quale dei processi alternativi utilizzare.",
        'testo_integrale': "8.1 Initiation — INI-8.1-02X: If alternative identity proofing processes are available to achieve the purpose of the identity proofing, the applicant should be allowed to select which of the alternative processes to use.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando, per lo stesso scopo dell'identity proofing, sono disponibili processi alternativi.",
    },
    {
        'riferimento': 'COL-8.2.2.1-02A',
        'testo': "L'esito del processo di identity proofing puo' essere un'identita' pseudonima; cio' non significa tuttavia che l'identity proofing conforme al presente documento non richieda comunque l'identificazione dell'identita' reale della persona, come determinata da documenti di identita' applicabili, registri fidati o altre fonti autoritative.",
        'testo_integrale': "8.2.2.1 Attribute collection for natural person — COL-8.2.2.1-02A: The outcome of the identity proofing process may be a pseudonymous identity. NOTE 7: Although the outcome of the identity proofing can be a pseudonym identity, identity proofing conforming to the present document requires identification of the real identity of the person as determined by applicable identity documents, trusted registers or other authoritative sources.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica nell'ambito della raccolta di attributi per persona fisica (clausola 8.2.2.1).",
    },
    {
        'riferimento': 'COL-8.2.5-02',
        'testo': "Se una firma digitale con certificato di supporto e' accettata come evidenza di identita' per una persona fisica che rappresenta una persona giuridica, il certificato dovrebbe attestare il collegamento tra la persona fisica e la persona giuridica; per un certificato X.509 cio' implica tipicamente che il campo Subject identifichi entrambe le persone, ma tale identificazione di per se' non prova che la persona fisica sia autorizzata a rappresentare la persona giuridica ai fini dell'identity proofing.",
        'testo_integrale': "8.2.5 Use of existing digital signature means as evidence — [CONDITIONAL] COL-8.2.5-02: If a digital signature with a supporting certificate is accepted as evidence of identity for a natural person representing a legal person, the certificate should evidence the connection between the natural and the legal person. NOTE 4: For an X.509 certificate, this will typically imply that the Subject field of the certificate identifies both the natural and the legal person; however, such identification in itself does not evidence that the natural person is authorized to represent the legal person for the identity proofing.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se una firma digitale con certificato di supporto e' accettata come evidenza di identita' per una persona fisica che rappresenta una persona giuridica.",
    },
    {
        'riferimento': 'COL-8.2.6-02',
        'testo': "Dovrebbero essere accettati come registri fidati solo i registri ufficiali nazionali o approvati a livello nazionale.",
        'testo_integrale': "8.2.6 Use of trusted register as supplementary evidence — COL-8.2.6-02: Only official national or nationally approved registers should be accepted as trusted registers.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica nell'ambito dell'uso di un registro fidato come evidenza supplementare (clausola 8.2.6).",
    },
    {
        'riferimento': 'COL-8.2.8-02',
        'testo': "Se il richiedente e' una persona giuridica, puo' essere accettata come evidenza una dichiarazione di una persona fisica verificata come rappresentante della persona giuridica.",
        'testo_integrale': "8.2.8 Use of documents and attestations as supplementary evidence — [CONDITIONAL] COL-8.2.8-02: If the applicant is a legal person, a statement from a natural person verified to represent the legal person may be accepted as evidence.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica se il richiedente e' una persona giuridica.",
    },
    {
        'riferimento': 'COL-8.2.8-04',
        'testo': "L'accettazione di documenti e attestazioni digitali dovrebbe essere limitata a quelli attestati dalla firma digitale dell'emittente.",
        'testo_integrale': "8.2.8 Use of documents and attestations as supplementary evidence — COL-8.2.8-04: Acceptance of digital documents and attestations should be limited to digital documents and attestations that are evidenced by the issuer's digital signature.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica nell'ambito dell'uso di documenti e attestazioni come evidenza supplementare (clausola 8.2.8).",
    },
    {
        'riferimento': 'COL-8.2.9-08',
        'testo': "Documenti e attestazioni provenienti dalla persona giuridica interessata possono essere utilizzati come evidenza dell'autorizzazione della persona fisica a rappresentarla.",
        'testo_integrale': "8.2.9 Evidence collection for natural person representing legal person — COL-8.2.9-08: Documents and attestations from the concerned legal person may be used as evidence of a natural person's authorization to represent the legal person.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica nell'ambito della raccolta di evidenza per persona fisica che rappresenta persona giuridica (clausola 8.2.9).",
    },
]

INDICE_ARTICOLI_LOCALE = [
    'INI-8.1-01X',
    'INI-8.1-02X',
    'INI-8.1-03X',
    'INI-8.1-04',
    'COL-8.2.1-01X',
    'COL-8.2.1-01A',
    'COL-8.2.1-02',
    'COL-8.2.1-03X',
    'COL-8.2.1-04',
    'COL-8.2.1-05',
    'COL-8.2.1-06X',
    'COL-8.2.1-07',
    'COL-8.2.2.1-01X',
    'COL-8.2.2.1-02',
    'COL-8.2.2.1-02A',
    'COL-8.2.2.1-03',
    'COL-8.2.2.1-04',
    'COL-8.2.2.2-01X',
    'COL-8.2.2.2-02',
    'COL-8.2.2.2-03',
    'COL-8.2.2.3-01',
    'COL-8.2.2.3-02',
    'COL-8.2.2.3-03',
    'COL-8.2.3-01X',
    'COL-8.2.3-02X',
    'COL-8.2.3-03X',
    'COL-8.2.3-04X',
    'COL-8.2.3-05X',
    'COL-8.2.3-06X',
    'COL-8.2.3-07',
    'COL-8.2.4-01X',
    'COL-8.2.4-02X',
    'COL-8.2.4-02A',
    'COL-8.2.4-03X',
    'COL-8.2.5-01X',
    'COL-8.2.5-02',
    'COL-8.2.5-03X',
    'COL-8.2.5-03A',
    'COL-8.2.5-04X',
    'COL-8.2.5-06X',
    'COL-8.2.6-01X',
    'COL-8.2.6-01A',
    'COL-8.2.6-02',
    'COL-8.2.6-03X',
    'COL-8.2.7-01X',
    'COL-8.2.7-02',
    'COL-8.2.7-03X',
    'COL-8.2.8-01X',
    'COL-8.2.8-01A',
    'COL-8.2.8-02',
    'COL-8.2.8-03X',
    'COL-8.2.8-04',
    'COL-8.2.9-01',
    'COL-8.2.9-02',
    'COL-8.2.9-03X',
    'COL-8.2.9-04X',
    'COL-8.2.9-05X',
    'COL-8.2.9-06X',
    'COL-8.2.9-07X',
    'COL-8.2.9-08',
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
