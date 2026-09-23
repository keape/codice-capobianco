"""Estrazione granulare ETSI TS 119 461 V2.1.1 (2025-02) — Capitolo 2: clausole
4 (General concepts, sottoclausole 4.1-4.6) e 5 (Operational risk assessment).

Fonte 9 (numerazione definitiva cablata dalla sessione principale in
app/seed.py — questo modulo NON tocca seed.py). Testo ufficiale in
app/.source_cache/etsi_119_461/cap02.txt. Manifest di split:
app/.source_cache/etsi_119_461/manifest.json.

Modellazione (ADR-0007), stesso criterio già applicato a ETSI EN 319 412-5
(fonte 7) per uno standard tecnico ETSI a clausole/sottoclausole invece che
articoli/commi di un atto legislativo:

Clausola 4 (General concepts) — contenuto descrittivo/di inquadramento senza
soggetto obbligato, un Principio per sottoclausola pertinente (nessuna
sottoclausola generatrice di requisiti numerati con id proprio in questo
capitolo — quelli iniziano in clausola 5):

- 4.1 "Identity proofing actors" -> Principio, tipo "altro". Descrive i
  ruoli (TSP, IPSP, applicant, registration officer) già definiti
  formalmente in clausola 3 (letta dal capitolo 1): qui sono solo
  contestualizzati/relazionati tra loro, nessuna definizione nuova.
- 4.2 "Identity proofing process" -> Principio, tipo "definitorio". A
  differenza di 4.1, questa sottoclausola introduce un elemento concettuale
  NON presente nelle definizioni di clausola 3 (che definisce solo il
  singolo termine "identity proofing (process)" in una frase): la
  scomposizione formale del processo in cinque task nominati (Initiation,
  Attribute and evidence collection, Attribute and evidence validation,
  Binding to applicant, Issuing of identity proofing result), che è la
  tassonomia strutturale su cui si fonda l'intera organizzazione a blocchi
  della clausola 8 (8.1-8.5) del documento — una vera e propria definizione
  di modello concettuale, non solo una descrizione contestuale.
- 4.3 "Identity proofing context" -> Principio, tipo "altro". Il termine
  "identity proofing context" è già definito in clausola 3; questa
  sottoclausola lo elabora con esempi e un elenco di aspetti che il
  contesto può restringere, senza introdurre un concetto nuovo distinto
  dalla definizione di clausola 3.
- 4.4 "Authoritative evidence and supplementary evidence" -> Principio,
  tipo "definitorio". Anche "authoritative evidence" e "supplementary
  evidence" sono già definiti in clausola 3, ma qui il documento introduce
  la tassonomia specifica dei tipi ammessi come prova autoritativa (physical
  identity document, digital identity document, eID means, certificato di
  firma digitale) e come prova complementare (trusted register, proof of
  access, documents and attestations/EAA) — un secondo livello di
  definizione (elenco chiuso dei tipi) che va oltre la definizione generica
  di clausola 3 e struttura i requisiti di raccolta/validazione della
  clausola 8.2/8.3.
- 4.5 "Consideration of threats" -> Principio, tipo "altro". Descrive il
  panorama di minacce (falsified/counterfeited evidence, impersonation,
  attacks on the system, social engineering, più i due sotto-tipi
  presentation/injection attack per il remote identity proofing) a scopo di
  inquadramento del rischio che giustifica le contromisure delle clausole
  8/9, non introduce termini di glossario riusati altrove nel documento con
  un id proprio — è motivazione/contesto, non definizione tecnica. La
  Figura 2 (mappa minaccia/contromisura) è sintetizzata testualmente nel
  campo `testo`/`testo_integrale` invece di essere ricopiata verbatim: il
  testo estratto dal PDF per quella tabella è visibilmente corrotto
  dall'estrazione (celle mescolate, es. "C E|The identity proofing process
  is compromised by|Verify..."), quindi la sintesi discorsiva del contenuto
  informativo (mappatura minaccia -> contromisura -> clausola che la
  indirizza) è più fedele del testo grezzo.
- 4.6 "Identity proofing service policy" -> Principio, tipo "altro".
  Descrive la policy di servizio facoltativa dell'IPSP e i due OID
  informativi (baseline/extended); nessun comportamento imposto, nessuna
  definizione di concetto nuovo.

Clausola 5 (Operational risk assessment) — dieci requisiti con id proprio
OVR-5-01 .. OVR-5-10, ciascuno -> Obbligo, categoria_soggetto "QTSP/gestore"
(il documento tratta l'IPSP come "componente" del TSP ai fini del
censimento, per esplicita indicazione dell'incarico), ruolo "obbligato",
tipo_obbligo "organizzativo" (valutazione del rischio operativo, gestione
interna — nessuno di questi dieci requisiti è un requisito tecnico di
raccolta/validazione/binding in senso stretto, tutti riguardano il processo
di risk management dell'IPSP). Note tecniche:

- OVR-5-01: la NOTE 1 ("quando l'identity proofing è svolto dal TSP stesso,
  la valutazione del rischio del TSP può coprire l'identity proofing") è
  una precisazione sostanziale sull'applicabilità (non mera esemplificazione)
  ed è quindi assorbita nel `testo_integrale`, non scartata. Il rinvio a
  ETSI EN 319 401 clausola 5 non genera una relazione cross-fonte: quello
  standard non è una Fonte separata in questo censimento (stesso trattamento
  già riservato a ETSI EN 319 401 in reg_ue_2025_1566/cap01.py, punto 1).
- OVR-5-03 elenca due sfaccettature omogenee (a, b) della stessa
  prescrizione continua ("copertura almeno di due categorie di rischio") ->
  un solo nodo, stesso criterio già usato in cad/cap03.py per gli elenchi
  a lettere di un unico comma.
- OVR-5-05: l'EXAMPLE (riferimento al report ENISA) è informativo/non
  normativo come una NOTE — non genera un item di indice a sé, ma il suo
  contenuto è comunque riportato in `testo_integrale` perché identifica la
  metodologia di riferimento attesa per la procedura di threats
  intelligence, informazione utile all'interpretazione dell'obbligo.
- OVR-5-07 e OVR-5-08 sono marcati "[CONDITIONAL]" nel testo ->
  `condizione_applicabilita` valorizzata con la condizione (Baseline LoIP /
  Extended LoIP dichiarato), "[CONDITIONAL]" omesso dal `riferimento` come
  da istruzione. La NOTE 2 di OVR-5-08 (rinvio a clausola 3.1 per le
  definizioni di potenziale di attacco moderato/alto, e al report ENISA) è
  assorbita in `testo_integrale` per lo stesso motivo di OVR-5-05.
- OVR-5-10: la NOTE 3 (chiarisce che i termini "false acceptance"/"false
  rejection", normalmente biometrici, si applicano qui a tutti i casi d'uso
  della clausola 9/Annex C, inclusa la presenza fisica) è una precisazione
  sostanziale sull'ambito applicativo dell'obbligo -> assorbita in
  `testo_integrale`.

RELAZIONI (tutte interne a questo capitolo, fonte_id_o_None=None):
- OVR-5-02/03/04 "specifica" OVR-5-01: i tre requisiti aggiungono ciascuno
  un aspetto specifico (cadenza, contenuto minimo, trigger di modifica
  processo) al dovere generale di valutazione del rischio richiamato da
  OVR-5-01 (applicazione di ETSI EN 319 401 clausola 5) — nessuna citazione
  testuale esplicita tra i due id, quindi evidence_type "inferred".
- OVR-5-06 "richiama" OVR-5-05: OVR-5-06 cita testualmente "findings from
  the threats intelligence procedure", che è esattamente l'oggetto della
  procedura istituita da OVR-5-05 ("documented and effective procedure for
  threats intelligence") -> evidence_type "textual".
- OVR-5-09 "richiama" OVR-5-05 e OVR-5-06: OVR-5-09 cita testualmente
  "findings from the threats intelligence procedure" (-> OVR-5-05) "and
  changes to the risk assessment" (-> l'aggiornamento di OVR-5-06, che è
  l'aggiornamento della valutazione del rischio guidato proprio da quelle
  risultanze) -> evidence_type "textual" per entrambe.
- OVR-5-07/08 "specifica" OVR-5-03: i due requisiti condizionali
  aggiungono, per Baseline/Extended LoIP, il livello di potenziale di
  attacco che la valutazione del rischio (il cui contenuto minimo è fissato
  da OVR-5-03) deve considerare -> evidence_type "inferred" (nessuna
  citazione testuale diretta dell'id OVR-5-03).
- OVR-5-05 "richiama" clausola 4.5 (Consideration of threats): la procedura
  di threats intelligence opera sul panorama di minacce descritto in 4.5 ->
  evidence_type "inferred" (collegamento concettuale, non citazione
  testuale — il testo di clausola 5 non cita "clausola 4.5" per numero),
  confidence 0.6.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "OVR-5-01",
        "testo": "I requisiti di cui alla clausola 5 di ETSI EN 319 401 si applicano al processo di identity proofing. Quando l'identity proofing è svolto dal TSP stesso, la valutazione del rischio del TSP può coprire anche l'identity proofing.",
        "testo_integrale": "OVR-5-01: The requirements specified in ETSI EN 319 401 [1], clause 5 shall apply. NOTE 1: When the identity proofing is done by the TSP itself, the TSP's risk assessment can cover the identity proofing.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-5-02",
        "testo": "La valutazione del rischio dell'IPSP deve essere aggiornata con cadenza annuale.",
        "testo_integrale": "OVR-5-02: The IPSP's risk assessment shall be updated yearly.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-5-03",
        "testo": "La valutazione del rischio dell'IPSP deve coprire i rischi rilevanti relativi all'identity proofing e, almeno: a) una valutazione dei rischi relativi alla frode d'identità; e b) una valutazione dei rischi relativi alla sicurezza dei sistemi informativi.",
        "testo_integrale": "OVR-5-03: The IPSP's risk assessment shall cover relevant risks related to identity proofing and at least: a) An assessment of the risks related to identity fraud; and b) An assessment of the risks related to information systems security.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-5-04",
        "testo": "La valutazione del rischio dell'IPSP deve essere aggiornata se un processo di identity proofing viene modificato.",
        "testo_integrale": "OVR-5-04: The IPSP's risk assessment shall be updated if an identity proofing process is changed.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-5-05",
        "testo": "L'IPSP deve disporre di una procedura documentata ed efficace per l'intelligence sulle minacce, che assicuri l'adeguamento del servizio dell'IPSP alle nuove minacce.",
        "testo_integrale": "OVR-5-05: The IPSP shall have a documented and effective procedure for threats intelligence that ensures that the IPSP's service is adapted to new threats. EXAMPLE: Based on the ENISA report \"Methodology for sectoral cybersecurity assessments\" [i.28].",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-5-06",
        "testo": "La valutazione del rischio dell'IPSP deve essere aggiornata in base alle risultanze della procedura di intelligence sulle minacce.",
        "testo_integrale": "OVR-5-06: The IPSP's risk assessment shall be updated according to findings from the threats intelligence procedure.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-5-07",
        "testo": "Se si dichiara conformità al livello Baseline LoIP, la valutazione del rischio deve considerare almeno attaccanti con potenziale di attacco moderato.",
        "testo_integrale": "[CONDITIONAL] OVR-5-07: If the Baseline LoIP is claimed, the risk assessment shall consider at least attackers with moderate attack potential.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'IPSP dichiara conformità al Baseline LoIP",
    },
    {
        "riferimento": "OVR-5-08",
        "testo": "Se si dichiara conformità al livello Extended LoIP, la valutazione del rischio deve considerare almeno attaccanti con potenziale di attacco elevato.",
        "testo_integrale": "[CONDITIONAL] OVR-5-08: If the Extended LoIP is claimed, the risk assessment shall consider at least attackers with high attack potential. NOTE 2: See clause 3.1 of the present document for definitions of moderate and high attack potential. The ENISA report \"Methodology for sectoral cybersecurity assessments\" [i.28], clauses 5 (especially clause 5.4) and 9 can be used as basis for describing attack potential.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'IPSP dichiara conformità all'Extended LoIP",
    },
    {
        "riferimento": "OVR-5-09",
        "testo": "In base alle risultanze della procedura di intelligence sulle minacce e alle modifiche della valutazione del rischio, deve essere valutata la necessità di formazione del personale, ed erogata la formazione se necessaria.",
        "testo_integrale": "OVR-5-09: Based on findings from the threats intelligence procedure and changes to the risk assessment, the need for training of personnel shall be assessed and training be carried out if needed.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-5-10",
        "testo": "L'IPSP deve indicare nella propria dichiarazione delle pratiche (practice statement) gli obiettivi di qualità e sicurezza in termini di resilienza al falso accettato e al falso rifiutato dei richiedenti, ed effettuare test periodici delle prestazioni rispetto a tali obiettivi.",
        "testo_integrale": "OVR-5-10: The IPSP shall state in its practice statement goals for quality and security in terms of resilience to false acceptance and false rejection of applicants and perform regular testing of the performance against these goals. NOTE 3: While false acceptance and rejection are terms normally used for biometrics, the terms in this requirement apply to all use cases of clause 9 and Annex C of the present document, e.g. including physical presence.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 4.1 (Identity proofing actors)",
        "testo": "Né il regolamento eIDAS originario né quello modificato definiscono l'identity proofing come servizio fiduciario autonomo: il presente documento lo tratta come componente di servizio, che può essere parte integrante dell'erogazione del TSP oppure affidato in subappalto a un Identity Proofing Service Provider (IPSP) specializzato, sotto la responsabilità del TSP — il documento si applica a entrambi gli scenari. Un IPSP può erogare identity proofing in subappalto a più TSP e ad altri tipi di prestatori di servizi. Gli attori principali di un processo di identity proofing sono: il TSP, che richiede l'identity proofing ed è il destinatario del relativo esito; ove pertinente, l'IPSP che eroga il servizio in subappalto al TSP; e il richiedente (applicant), la cui identità deve essere provata, che può essere una persona fisica, una persona giuridica, o una persona fisica che rappresenta una persona giuridica. Se il processo utilizza procedure manuali, queste sono svolte da personale nel ruolo di addetto alla registrazione (registration officer).",
        "testo_integrale": "4.1 Identity proofing actors: Neither the original eIDAS regulation [i.1] nor the amended eIDAS regulation [i.25] define identity proofing as a trust service on its own. In the present document, identity proofing is defined as a trust service component. The identity proofing service component can be an integral part of the Trust Service Provider's (TSP) service provisioning, but the service component can also be the task of a specialized Identity Proofing Service Provider (IPSP) acting as a subcontractor to the TSP under the TSP's responsibility. The present document is applicable to both of these scenarios. An IPSP as a specialized service provider can provide identity proofing subcontracted to many different TSPs as well as to other types of service providers. The main actors of an identity proofing process are the TSP that requests the identity proofing and is the receiver of the identity proofing result, where relevant the IPSP that delivers the identity proofing service subcontracted to the TSP, and the applicant whose identity is to be proven. The applicant can be a natural person, a legal person, or a natural person representing a legal person. If the identity proofing process uses manual procedures, these procedures are carried out by personnel in the role of registration officer.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.2 (Identity proofing process)",
        "testo": "L'identity proofing è il processo di provare, con il grado di affidabilità richiesto, che l'identità dichiarata da un richiedente è corretta; il grado richiesto è, ai fini del presente documento, il Baseline LoIP o l'Extended LoIP. Il richiedente è identificato da un insieme di attributi di identità, e viene fornita evidenza per collegare tali attributi al richiedente (il concetto di identity proofing copre anche il proofing di attributi ulteriori, non identificativi, rilevanti in particolare per gli attestati elettronici di attributi - EAA). Il processo può essere automatizzato, condotto da un addetto alla registrazione, o una combinazione dei due; può basarsi sulla presenza fisica del richiedente o su identity proofing remoto tramite rete di comunicazione. Il processo di identity proofing è tipicamente scomposto in cinque task: 1) Initiation (avvio); 2) Attribute and evidence collection (raccolta di attributi ed evidenza); 3) Attribute and evidence validation (validazione di attributi ed evidenza); 4) Binding to applicant (collegamento al richiedente); 5) Issuing of identity proofing result (emissione dell'esito). I task non sono necessariamente sequenziali: per alcuni processi sono intrecciati, e il processo può essere sincrono (tutti i passi in un unico flusso continuo) o asincrono (validazione, binding ed emissione dell'esito svolti in un momento successivo). Il presente documento copre l'identity proofing iniziale di un nuovo richiedente che diventa soggetto o sottoscrittore di un servizio fiduciario, non le eventuali semplificazioni per un richiedente già noto, né l'identity proofing continuo (basato sul comportamento del soggetto nel tempo), entrambi fuori campo di applicazione. I requisiti del documento sono strutturati come segue: la clausola 5 pone requisiti di valutazione del rischio e threats intelligence; la clausola 6 requisiti su practice statement, termini e condizioni, e politica di sicurezza delle informazioni; la clausola 7 requisiti di gestione e operatività del servizio; la clausola 8 è strutturata in sottoclausole che fungono da blocchi costitutivi per i diversi casi d'uso (8.1 avvio, 8.2 raccolta di attributi ed evidenza, 8.3 validazione, 8.4 binding al richiedente, 8.5 emissione dell'esito e creazione dell'evidenza del processo); la clausola 9 combina questi blocchi in casi d'uso tipici che soddisfano i requisiti per il Baseline e l'Extended LoIP.",
        "testo_integrale": "4.2 Identity proofing process: Identity proofing is the process of proving with the required degree of reliability that the purported identity of an applicant is correct. In the present document, the required degree of reliability is assumed to be either the Baseline LoIP or the Extended LoIP. The applicant is identified by a set of identity attributes, and evidence is provided to link these attributes to the applicant. Especially for Electronic Attestation of Attributes (EAA), further identifying or non-identifying attributes can be collected and linked to the applicant; the term identity proofing as used in the present document covers proofing of such additional attributes where relevant. The identity proofing process can be carried out automated, by a registration officer, or by a combination of human-controlled and automated. The identity proofing process can be based on the physical presence of the applicant, or on remote identity proofing based on remote communication with the applicant using a communications network. The different approaches imply different risks. For each approach, the present document sets the minimum requirements to mitigate those risks to reach either Baseline or Extended LoIP. The identity proofing process is commonly broken down into five tasks: 1) Initiation. 2) Attribute and evidence collection. 3) Attribute and evidence validation. 4) Binding to applicant. 5) Issuing of identity proofing result. The subsequent use of the identity proofing result by a TSP or other type of service provider is out of scope of the present document. EXAMPLE 1: A typical case is issuing of a digital signature certificate for the proven identity. The process can be illustrated by Figure 1 (from [i.15]), also showing that an identity proofing process can be iterative. The tasks are not necessarily carried out as consecutive steps of an identity proofing process. For some processes, they can be intertwined, e.g. that attributes are collected from an identity document integral to the validation of the same document. An identity proofing process can be synchronous, meaning that all steps of the identity proofing process, including issuing of proof, are carried out in one continuous process, or asynchronous, where the validation and binding tasks and issuing of proof are done at a later time. Figure 1: Tasks of an identity proofing process. The present document covers initial identity proofing of a new applicant to become a subject or a subscriber of a trust service. The present document does not consider possible simplifications of the process if the applicant is a known subject, e.g. in cases where identity proofing is required to be repeated regularly. In some cases, identity proofing can be regarded as a continuous process, where the behaviour of the subject over time can be used to determine the risk or the likelihood that the identity is correct. In such cases, the reliability of the correct identity of a subject can increase or decrease over time. Continuous identity proofing is out of the scope of the present document. The present document poses requirements to identity proofing processes in the following structured manner. Clause 5 has requirements for risk assessment and threats intelligence to ensure the IPSP's service stays up to date. Clause 6 states requirements on identity proofing services practice statement, terms and conditions, and information security policy. Clause 7 sets requirements for service management and operation, requiring an IPSP to adhere to the same requirements as a TSP. Clause 8 is structured into subclauses that serve as building blocks for different identity proofing use cases: Clause 8.1 states requirements for initiation of an identity proofing process. Clause 8.2 states requirements for the collection of attributes, meaning the identity information to prove, and for collection of the evidence needed to prove the identity attributes. Clause 8.3 states requirements for validation of attributes against the provided evidence and requirements to ensure that the evidence in itself is genuine and valid. Clause 8.4 states requirements for binding to applicant, meaning ensuring that the applicant presenting the authoritative evidence really is the person identified by the evidence. Binding to applicant can be done manually by a registration officer, or automated, notably by face biometrics for natural persons, or by a combination of manual and automated. Other biometric modes than face are currently out of scope of the present document. Clause 8.5 states requirements for issuing the identity proofing result and for the creation of evidence of the identity proofing process to be able to prove in retrospect why the identity proofing process yielded the given identity proofing result. Clause 9 sets requirements for the combination of the building blocks from clause 8 into some typical identity proofing use cases that are considered to fulfil the requirements for the Baseline and Extended LoIP. Requirements are specified for six use cases and sub-cases when the applicant is a natural person: 1) Use of an identity document in a physical presence context: a) Manual operation. b) Hybrid manual and automated operation. c) Automated operation. 2) Use of an identity document in an attended remote context, where the applicant presents an identity document in a remote session and communicates in real-time with a registration officer: a) Manual operation with validation and binding to applicant done manually by the registration officer-only accepted for Baseline LoIP. b) Hybrid manual and automated operation. 3) Use of an identity document in an unattended remote context, where the applicant presents an identity document in a remote session without human supervision: a) Manual operation with validation and binding to applicant done afterwards by a registration officer-only accepted for Baseline LoIP. b) Hybrid manual and automated operation with validation and binding to applicant done afterwards by a combination of automated analysis and a registration officer. c) Automated operation with no involvement of a registration officer. 4) Use of eID means. 5) Use of digital signature with certificate. 6) Additional identity proofing to enhance an identity proven to Baseline LoIP by use of eID means to Extended LoIP. Table 1 below shows an overview of the use cases for use of identity documents for identity proofing. Table 1: Use cases for identity proofing using identity documents. |Applicant presence||Operation Clause|Identity document|Evidence validation|Binding to applicant|Example| |---|---|---|---|---|---|---| |||Manual 9.2.1.2 Physical||Manual|Manual|Manual enrolment at registration office.| |Physical||Hybrid 9.2.1.3 Automated 9.2.1.4 Manual 9.2.2.2 Physical|Digital|Digital Automated Manual Manual Digital Automated Manual|Automated Automated Manual|Similar to manual border control, with automated validation of digital doc. and manual face verification by registration officer. Similar to unassisted border control with automated validation of digital doc. and biometric face verification. Manual enrolment at a virtual registration office where registration officer manually verifies physical doc. and face-only for Baseline LoIP. Manual enrolment at a virtual registration office with automated validation of digital doc. and manual face verification.| |Remote attended||Hybrid 9.2.2.3|Physical Physical|Digital Automated Combined automated and manual Combined automated and manual|Combined manual and automated Manual Combined automated and manual|Manual enrolment at a virtual registration office with automated validation of digital doc. and both biometric and manual face verification. Manual enrolment at a virtual registration office with both automated and manual validation of doc. and manual face verification. Manual enrolment at a virtual registration office with both automated and manual validation of doc. and both manual and biometric face verification.| |Applicant presence||Operation Clause|Identity document|Evidence validation|Binding to applicant|Example| |---|---|---|---|---|---|---| |||Manual 9.2.3.2 Physical||Manual Digital Automated Manual|Manual|Remote enrolment process, with subsequent manual verification of doc. and manual face verification-only for Baseline LoIP. Remote enrolment process with automated validation of digital doc. and subsequent manual face verification-only for Baseline LoIP.| |Remote unattended||Hybrid 9.2.3.3|Physical Physical|Digital Automated Combined automated and manual Combined automated and manual|Combined manual and automated Manual Combined automated and manual|Remote enrolment process with automated validation of digital doc. and subsequent both manual and biometric face verification. Remote enrolment process with subsequent both automated and manual validation of doc. and manual face verification-only for Baseline LoIP. Remote enrolment process with subsequent both automated and manual validation of doc. and both manual and biometric face verification.| ||Automated|9.2.3.4|Digital|Automated|Automated|Fully automated process.| Annex B provides (from [i.15]) an overview of typical threats to identity proofing and how the present document addresses these threats. Annex C further profiles the use cases of clause 9 specifically for identity proofing to support EU qualified trust services according to both the original eIDAS regulation [i.1] and the amended eIDAS regulation [i.25]. To claim compliance with the present document, an IPSP is obliged to identify the use case(s) from clause 9 and/or Annex C that the IPSP applies in its service, and fulfil all relevant requirements from the present document for each use case. Automated operation is considered not relevant to the attended remote case since a registration officer is anyway needed for communication with the applicant. For the unattended remote case, while the communication with the applicant is automated, the tasks of validation and binding to applicant can be done by all the three alternatives manual, hybrid, or automated. Manual only validation of a physical identity document is considered to only be able to reach Baseline LoIP. For the unattended remote case, manual only binding to applicant is considered to only be able to reach Baseline LoIP. Use of hybrid manual and automated operation is strongly encouraged for both validation of physical identity document and binding to applicant. Fully automated, remote operation with use of an identity document requires the use of a digital identity document and face biometrics for binding to applicant. An identity proofing context can pose limitations on the selection of use cases to apply. Clause 8 specifies means that can be combined into identity proofing use cases in a flexible way to be able to fulfil restrictions imposed by a wide variety of identity proofing contexts. Other use cases than those specified in clause 9 can be possible to achieve the Baseline or Extended LoIP, notably when specific combinations of different evidence are required by an identity proofing context. The present document does not pose requirements on the process flow of an identity proofing process. Each of the use cases specified in clause 9 can be fulfilled by various process flows leading to the same LoIP result. The building block structure of clause 8 ensures that requirements regarding specific means are consistent across identity proofing use cases. EXAMPLE 2: All use cases that use physical identity document as evidence will adhere to the same set of base requirements, whether the physical identity document is used with physical presence, remote with automated validation, or remote with manual validation, but conditional requirements are used where use cases differ. For example, some checks of a physical identity document are only possible with physical presence.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3 (Identity proofing context)",
        "testo": "Il contesto di identity proofing è l'insieme delle condizioni esterne di cornice a cui è soggetto un processo di identity proofing, che possono imporre requisiti e restrizioni; un elemento centrale del contesto sono i requisiti regolatori imposti dalla legislazione applicabile per lo scopo definito (es. il rilascio di certificati qualificati di firma elettronica nell'UE è soggetto al regolamento eIDAS modificato e a eventuali requisiti aggiuntivi della legislazione nazionale del paese di registrazione del TSP). Il contesto varia tra scopi di identity proofing e tra paesi, e può restringere almeno: il LoIP richiesto (Baseline o Extended); gli attributi di identità da raccogliere (obbligatori, vietati o facoltativi — es. il numero di identità nazionale può essere obbligatorio in alcuni paesi e vietato in altri); l'evidenza da utilizzare (evidenza o combinazioni di evidenza che possono essere imposte, vietate o presunte disponibili dalla legislazione — es. restrizione ai soli documenti d'identità nazionali, o validazione obbligatoria contro un registro di popolazione nazionale); i mezzi da usare per la validazione degli attributi/evidenza e per il binding al richiedente (es. presenza fisica obbligatoria per certi scopi, o restrizione dei casi d'uso remoti ammessi); l'emissione dell'esito e dell'evidenza del processo, ossia quali informazioni possono essere comunicate al TSP e quali possono essere conservate come evidenza del processo (es. la conservazione di una foto/fotocopia del documento d'identità può essere richiesta in alcuni paesi e vietata in altri). La specificazione dei contesti di identity proofing è fuori campo di applicazione del presente documento, che intende fornire mezzi per soddisfare i requisiti di un'ampia varietà di contesti.",
        "testo_integrale": "4.3 Identity proofing context: The identity proofing context is the set of external framing conditions that an identity proofing process is subject to and that can impose requirements and restrictions on identity proofing. A core element of the identity proofing context is the regulatory requirements imposed on identity proofing for the defined purpose by the applicable legislation. EXAMPLE 1: Issuing of qualified certificates for electronic signatures in the EU is subject to the requirements of the amended eIDAS regulation [i.25] and possibly additional requirements from the national legislation of the country where the TSP is registered. The identity proofing context will vary between purposes of identity proofing and between countries. The identity proofing context can restrict at least the following aspects of an identity proofing process: The required LoIP, assumed to be Baseline or Extended as defined by the present document. The identity attributes to collect, meaning attributes that are mandatory, prohibited, or optional. EXAMPLE 2: In some countries, the collection of a national identity number can be mandatory for the identity proofing context, while other countries do not use such numbers or the use of the national identity number is prohibited for most identity proofing contexts. The evidence to use, meaning evidence or combinations of evidence that can be mandated or prohibited by legislative rules or that can be assumed to be available. EXAMPLE 3: National legislation can restrict identity documents to passports and national identity cards from the same country or from selected countries. EXAMPLE 4: In some countries, validation of identity attributes against a national population register can be mandatory, while other countries do not have such registers. EXAMPLE 5: In some countries, all citizens can be assumed to possess a national identity card, while other countries do not issue such cards. The means to use for attribute and evidence validation and for binding to applicant, meaning that certain process steps can be mandated or prohibited. EXAMPLE 6: In some countries, physical presence can be mandated for certain purposes of identity proofing, or remote identity proofing can be restricted to allow only specific use cases. The issuing of the result of the identity proofing process and the evidence of the identity proofing process, meaning what information can be conveyed to the TSP and what information can be retained as evidence of the process. EXAMPLE 7: In some countries, a photo or photocopy of a physical identity document can be required as part of the evidence of the identity proofing process, while in other countries retaining such copies can be prohibited. Specification of identity proofing contexts is out of the scope of the present document, but the present document is intended to provide means to fulfil the requirements of a wide variety of identity proofing contexts.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.4 (Authoritative and supplementary evidence)",
        "testo": "Un processo di identity proofing richiede evidenza autoritativa sull'identità del richiedente: evidenza emessa da una fonte autoritativa, quindi attendibile per gli attributi di identità che trasmette e per il collegamento di tali attributi al richiedente che la presenta. Quando il richiedente è una persona fisica o una persona fisica che rappresenta una persona giuridica, un processo conforme al presente documento usa almeno uno dei seguenti tipi come evidenza autoritativa: documento d'identità fisico, documento d'identità digitale, mezzo di eID usato in un protocollo di autenticazione, o certificato di firma digitale (ciò non esclude il caso in cui l'identity proofing per un servizio fiduciario sia svolto da un'autorità governativa, es. rilascio di un certificato qualificato contestuale al rilascio di una carta d'identità nazionale). Il documento specifica inoltre l'uso, come evidenza complementare, di: registro fidato (incluse le fonti autentiche ex regolamento eIDAS modificato), prova di accesso (in particolare a un conto bancario), e documenti e attestazioni (inclusi gli attestati elettronici di attributi). A seconda del contesto, l'evidenza complementare può essere la fonte autoritativa per gli attributi di identità, ma solo se combinata con l'uso di uno dei tipi di evidenza autoritativa sopra elencati (es. un registro di popolazione nazionale può essere considerato fonte autoritativa solo se l'identità del richiedente è ulteriormente provata da una delle evidenze autoritative; in certi contesti, informazioni identificative ottenute da una banca possono essere considerate autoritative). Nessuna delle evidenze autoritative documento d'identità, mezzi eID e firma digitale può essere considerata comunemente disponibile per le persone giuridiche: per queste, il registro fidato e i documenti e attestazioni assumono il ruolo autoritativo, e il caso d'uso di clausola 9.3 per persona giuridica non impone l'uso di alcuna delle evidenze autoritative elencate. Più evidenze dello stesso tipo o di tipo diverso possono essere usate; anche altra evidenza non coperta dal presente documento può essere usata.",
        "testo_integrale": "4.4 Authoritative evidence and supplementary evidence: An identity proofing process requires authoritative evidence on the identity of the applicant. Authoritative evidence is issued by an authoritative source and is hence trusted regarding the identity attributes the evidence conveys and for the binding of these attributes to the applicant presenting the evidence. When the applicant is a natural person or a natural person representing a legal person, an identity proofing process compliant with the present document uses at least one of the following types of evidence as authoritative evidence: physical identity document, digital identity document, eID means used in an authentication protocol, or certificate of a digital signature. Use of these evidence types as authoritative evidence requires fulfilment of the relevant requirements of the present document. NOTE: This does not exclude the case where identity proofing for a trust service is done by a government authority, e.g. issuing of a (qualified) certificate in conjunction with issuing of a national identity card. If the identity proofing process is sufficient to issue an identity document that could subsequently be used in identity proofing for a trust service, then the process in itself is clearly also sufficient for identity proofing for the same trust service. The present document additionally specifies the use of the following as supplementary evidence: trusted register (including authentic source as defined by the amended eIDAS regulation [i.25]), proof of access (in particular of a bank account), and documents and attestations (including electronic attestation of attributes as defined by the amended eIDAS regulation [i.25]). Depending on the identity proofing context, such supplementary evidence can be the authoritative source for identity attributes, but, as specified by the present document, only when combined with the use of one of the authoritative evidence types listed above. EXAMPLE 1: A national population register can be considered as the authoritative source for information about the applicant, but only if the applicant's identity is additionally proven by one of the authoritative evidence listed above. EXAMPLE 2: In certain identity proofing contexts, identity information obtained from a bank can be regarded as authoritative. None of the authoritative evidence identity document, eID means, and digital signature can be expected to be commonly available for legal persons. While the use of eID means and digital signature is not ruled out, trusted register and documents and attestations are expected to take an authoritative role. Hence, the identity proofing use case for a legal person in clause 9.3 of the present document does not mandate use of any of the authoritative evidence types. Multiple evidence of the same type or different types can be used. Other evidence in addition to those covered by the present document can be used.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.5 (Consideration of threats)",
        "testo": "I requisiti del presente documento (controlli numerati) mirano a conseguire obiettivi di sicurezza necessari a indirizzare sia i rischi operativi (clausole 6 e 7) sia i rischi inerenti specifici dell'identity proofing (clausole 8 e 9), derivanti da due categorie principali di minacce: 1) l'impostore tenta di usare evidenza falsificata o contraffatta (fasulla o manomessa) per ottenere un identity proofing approvato con un'identità non corretta (reale di un'altra persona, o inesistente); 2) l'impostore tenta un'impersonificazione, usando evidenza genuina associata a un'altra persona per ottenere un identity proofing approvato sotto l'identità di quest'ultima. Sono inoltre in campo due ulteriori categorie: attacchi al sistema (l'impostore viola la sicurezza dei sistemi informativi usati per l'identity proofing per alterare illegittimamente informazioni o imporre un determinato esito) e ingegneria sociale (l'impostore inganna o costringe il legittimo titolare dell'evidenza a svolgere l'identity proofing in modo da ottenere il controllo delle credenziali risultanti). Per l'identity proofing remoto con documenti d'identità sono di particolare interesse due tipi di attacco: presentation attack (evidenza falsificata/contraffatta o impersonificazione tentata davanti alla telecamera di acquisizione) e injection attack (bypass della telecamera/sensori iniettando flussi video registrati o generati artificialmente). I contenuti generati artificialmente (i cosiddetti 'deep fake') sono sempre più usati dagli impostori, combinati con presentation o injection attack; lo stato dell'arte evolve rapidamente sia per la generazione sia per il rilevamento. In base all'EU Cybersecurity Act, ci si può attendere che parti di un sistema/servizio di identity proofing per il mercato UE diventino in futuro soggette a certificazione europea di cibersicurezza (specialmente per la biometria, con il livello di garanzia 'alta' che implicherebbe test e certificazione da parte di laboratori accreditati indipendenti); il presente documento richiede che i mezzi dell'IPSP per il rilevamento di injection attack e presentation attack biometrici siano sottoposti a test indipendenti.",
        "testo_integrale": "4.5 Consideration of threats: The requirements in the present document are provided in the form of requirements (numbered controls) that aim to achieve security objectives perceived necessary to address operational risks (clauses 6 and 7) as well as the inherent risks specific to identity proofing (clauses 8 and 9). These specific risks result from two main categories of threats, namely: 1) The imposter attempts to use falsified or counterfeited evidence, meaning the evidence is fake or has been tampered with in order for the applicant to obtain an approved identity proofing with an incorrect identity. This can be the real identity of another person or a non-existent identity. 2) The imposter attempts an impersonation, meaning the imposter uses genuine evidence associated with another person in order to obtain an approved identity proofing under this other person's identity. Two other categories of threats are in scope: 1) Attacks on the system where the imposter breaks the security of the information systems used for identity proofing to illegitimately change information or enforce a specific identity proofing result. 2) Social engineering where the imposter misleads or forces the legitimate owner of the evidence to carry out the identity proofing in a way that results in the imposter obtaining control of credentials issued as a result of the identity proofing. Figure 2 summarizes typical attack scenarios for falsified/counterfeited evidence and impersonation and the related countermeasures specified by the present document. Two specific attack types of concern for remote identity proofing using identity documents are: Presentation attack, where use of falsified or counterfeited evidence or impersonation is attempted in front of the camera used to capture evidence. Injection attack, where camera or other sensors are bypassed injecting recorded or artificially generated video streams as falsified or counterfeited evidence or impersonation. Artificially generated content, also called \"deep fakes\", is increasingly used by imposters. This can be a deep fake of a victim's face or an artificially generated representation of a physical identity document showing a victim's identity. An attacker needs to combine artificially generated content with presentation or injection attack. State of the art in artificially generated content is rapidly evolving, including artificial intelligence based logic, such as \"face swapping\", to react in real time to instructions such as movements or speech. At the same time, protection measures, also based on artificial intelligence, are rapidly evolving to detect deep fakes. Protection measures include both prevention of presentation and injection attacks and detection of the same types of attacks and of deep fakes. Figure 2: Risks and countermeasure for identity proofing. Related attack Countermeasures AUTHORITATIVE EVIDENCE Use authoritative (trusted) sources The identity proofing process is compromised by the use of evidence of insufficient quality Use the required set of attributes allowing unique identification ADRESSED IN CLAUSE 8.2 GENUINE EVIDENCE |C E|The identity proofing process is compromised by|Verify the security features and/or| |---|---|---| |EN|counterfeited and/or manipulated evidence|assurance level of the evidence| |ID EV||ADRESSED IN CLAUSE 8.3| |ED||VALID EVIDENCE| |IT FE|The identity proofing process is compromised by use|Verify that the evidence is still valid,| |ER T|of evidence that is terminated, revoked or reported|have not been revoked or declared| |N U|as lost/stolen|lost/stolen| |C O||ADRESSED IN CLAUSE 8.3| |R O||SECURE COLLECTION AND| |ED||TRANSMISSION OF EVIDENCE AND| |IFI||APPLICANT APPEARANCE (see| |LS||note)| |FA|N O The identity proofing process is compromised by TI manipulation of image capturing systems or A N transmission channels (for remote identity proofing) SO ER P M I The identity proofing process is compromised by an imposter claiming the legitimate identity of another|Use solutions that ensure authenticity and integrity of evidence from capture to the system that does the validation. Similarly for capture and transmission of the applicant's appearance where relevant. ADRESSED IN CLAUSES 8.3 and 8.4 LEGITIMATE OWNERSHIP Ensure that only the legitimate holder| of the evidence can claim the identity person ADRESSED IN CLAUSE 8.4 NOTE: The secure collection and transmission of evidence dimension only applies to remote identity proofing and addresses both the falsified or counterfeited evidence and impersonation threats. Following the EU Cybersecurity Act [i.26], it can be expected that the whole or parts of an identity proofing system or service serving the EU market in the future will become subject to European cybersecurity certification. Especially, this can be expected for biometrics, where CEN TC/224 WG18 is in the process of developing a multi-part standard for \"European requirements for biometric products\". TS 18099 [5] \"Biometric data injection detection\" can also be referenced from a European certification scheme. Several ISO/IEC standards cover testing of biometric systems, e.g. ISO/IEC 19792 [i.29] and ISO/IEC 19795-1 [4], ISO/IEC 30107 Parts 1 [i.16] and 3 [3], and ISO/IEC 19989-1 [i.30]. The Cybersecurity Act specifies three assurance levels for certification, 'basic', 'substantial', and 'high'. Identity proofing for EU qualified trust services could in the future be subject to certification at assurance level 'high', which will imply requirements for testing and certification by independent, accredited laboratories under the auspices of an accredited cybersecurity certification body. This could apply to all of manual, automated, and hybrid manual/automated services. The present document requires an IPSP's means for biometric injection attack detection and presentation attack detection to go through independent testing by an accredited laboratory every second year. To allow IPSPs, laboratories, and national accreditation authorities reasonable time to prepare for these requirements, the time for the first independent testing is set to before end of 2026. As the European cybersecurity certification system and related standards evolve, this can be referenced from future versions of the present document. The present document poses requirements for an IPSP to perform cyberthreat intelligence, keep the security of the service updated according to changes in the threats and risk landscape, and to test security and performance. No normative requirements on how to perform these tasks are defined in the present document, but a good reference, also considering preparation for possible cybersecurity certification schemes, is the ENISA report \"Methodology for sectoral cybersecurity assessments\" [i.28] under the EU Cybersecurity Certification Framework. The report covers topics such as cyberthreat intelligence, types of attackers, characterization of attackers, and attack potential. More detailed examples of threats are provided in Annex B, based on ENISA's report \"Remote ID proofing-Analysis of methods to carry out identity proofing remotely\" [i.15], with an indication of coverage by the countermeasures specified by the present document. Annex B can help organizations relying on an identity proofing process to assess the requirements of the present document against the organization's risk assessment for the identity proofing.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.6 (Identity proofing service policy)",
        "testo": "Quando l'identity proofing è fornito da un IPSP in subappalto al TSP, l'IPSP può definire una policy di servizio di identity proofing che descrive quanto offerto e che può contenere informazioni diverse, oltre il campo di applicazione del presente documento; la policy può indicare l'applicabilità del componente di servizio e i contesti di identity proofing a cui può essere applicato. I destinatari della policy possono essere i TSP e altri attori a cui l'IPSP fornisce i propri servizi, e gli organismi di valutazione della conformità (CAB) che svolgono audit dell'IPSP e dei TSP interessati. Il presente documento può essere richiamato da una policy di servizio di identity proofing per fornire informazioni sul LoIP del servizio. Un IPSP conforme ai requisiti normativi del presente documento per il Baseline LoIP o l'Extended LoIP per almeno un caso d'uso della clausola 9 o dell'Annex C può usare nella propria documentazione i seguenti Object Identifier (OID) specifici, oltre al riferimento ai casi d'uso supportati: itu-t(0) identified-organization(4) etsi(0) IDENTITY-PROOFING-policies(19461) policy-identifiers(1) baseline(1); e ... extended(2).",
        "testo_integrale": "4.6 Identity proofing service policy: When identity proofing is provided by an IPSP subcontracted to the TSP, the IPSP can define an identity proofing service policy that describes what is offered, and that can contain diverse information beyond the scope of the present document. An identity proofing service policy can indicate the applicability of the identity proofing service component and the identity proofing contexts to which the identity proofing service component can be applied. The recipients of the policy can be the TSPs and other actors that the IPSP provides its services to, and Conformity Assessment Bodies (CAB) performing audits of the IPSP and the concerned TSPs. The present document can be referred by an identity proofing service policy to provide information about the LoIP of the service. An IPSP conforming to the present document's normative requirements for Baseline LoIP or Extended LoIP for at least one use case defined in clause 9 or Annex C of the present document may use in its documentation the following specific Object Identifiers (OID) in addition to reference to the specific use cases from clause 9 and/or Annex C of the present document supported by the IPSP: itu-t(0) identified-organization(4) etsi(0) IDENTITY-PROOFING-policies(19461) policy-identifiers(1) baseline(1); itu-t(0) identified-organization(4) etsi(0) IDENTITY-PROOFING-policies(19461) policy-identifiers(1) extended(2).",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 4.1 (Identity proofing actors)",
    "clausola 4.2 (Identity proofing process)",
    "clausola 4.3 (Identity proofing context)",
    "clausola 4.4 (Authoritative and supplementary evidence)",
    "clausola 4.5 (Consideration of threats)",
    "clausola 4.6 (Identity proofing service policy)",
    "OVR-5-01", "OVR-5-02", "OVR-5-03", "OVR-5-04", "OVR-5-05",
    "OVR-5-06", "OVR-5-07", "OVR-5-08", "OVR-5-09", "OVR-5-10",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "OVR-5-02"),
        "nodo_a": ("obbligo", None, "OVR-5-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "OVR-5-03"),
        "nodo_a": ("obbligo", None, "OVR-5-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "OVR-5-04"),
        "nodo_a": ("obbligo", None, "OVR-5-01"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "OVR-5-06"),
        "nodo_a": ("obbligo", None, "OVR-5-05"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "OVR-5-09"),
        "nodo_a": ("obbligo", None, "OVR-5-05"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "OVR-5-09"),
        "nodo_a": ("obbligo", None, "OVR-5-06"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "OVR-5-07"),
        "nodo_a": ("obbligo", None, "OVR-5-03"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "OVR-5-08"),
        "nodo_a": ("obbligo", None, "OVR-5-03"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "OVR-5-05"),
        "nodo_a": ("principio", None, "clausola 4.5 (Consideration of threats)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
]
