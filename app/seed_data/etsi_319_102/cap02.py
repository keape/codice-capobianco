"""Estrazione granulare ETSI EN 319 102-1 V1.4.1 (2024-06) - Electronic
Signatures and Infrastructures (ESI); Procedures for Creation and Validation
of AdES Digital Signatures; Part 1: Creation and Validation.

Capitolo 2: clausola 4 (Signature creation) - 4.1 Signature creation model,
4.2 Signature creation information model (4.2.1-4.2.11, con 4.2.5.1-4.2.5.10
per i singoli attributi di firma), 4.3 Signature Classes and Creation
Processes (4.3.1-4.3.5, fino a quattro livelli di numerazione). Fonte
"etsi_319_102" (numerazione definitiva cablata dalla sessione principale in
app/seed.py: questo modulo NON tocca seed.py). Testo ufficiale in
app/.source_cache/etsi_319_102/cap02.txt. Manifest di split:
app/.source_cache/etsi_319_102/manifest.json.

Perimetro: SOLO la clausola 4. La clausola 2 "References" non e' in questa
porzione di testo (bibliografia/paratesto: nessun nodo e nessun item di
indice in ogni caso). L'ultima riga del capitolo e' l'intestazione "5
Signature validation", che apre il capitolo successivo (cap03): intestazione
di puro raggruppamento senza contenuto proprio, quindi nessun nodo e nessun
item di indice qui (la sua materia sta interamente in cap03). Nessuna
sezione "History" in questa porzione.

Modellazione (ADR-0007) - 44 item di indice, 38 Obblighi, 6 Principi:

- Un nodo per ogni clausola/sottoclavola numerata con contenuto proprio. Le
  intestazioni di puro raggruppamento (una clausola che non contiene nulla
  oltre il titolo) non generano nodo: 4 (Signature creation), 4.2 (Signature
  creation information model), 4.2.5 (Signature attributes), 4.3 (Signature
  Classes and Creation Processes), 4.3.2 (Creation of Basic Signatures),
  4.3.2.4 (Processing), 4.3.3, 4.3.4 e 4.3.5: la loro materia e' interamente
  nelle sottoclavole numerate.
- 4.2.1 (Introduction) e 4.3.2.1 (Description) hanno invece un nodo proprio
  pur essendo clausole di rimando: il loro corpo contiene la didascalia della
  figura della clausola (Figure 2, Figure 5), che e' contenuto della clausola
  e non un semplice titolo di raggruppamento; senza il nodo quella figura non
  sarebbe rappresentata da nessun nodo. Sono Principi ("altro"): nessun
  destinatario obbligato, solo l'inquadramento del modello informativo e della
  figura.
- Classificazione: le clausole che impongono un comportamento ("shall",
  "should", "is required to") sono Obblighi; le clausole che definiscono un
  oggetto, una classe o un modello senza destinatario obbligato sono Principi.
  Tipo dei Principi: "definitorio" quando la sostanza e' la definizione di un
  oggetto o di una classe di firma (4.2.3 SD, 4.3.1 classi di firma e
  Signature Augmentation, 4.3.3.1 Signature with Time); "altro" quando la
  sostanza e' descrittiva/di inquadramento (4.2.1, 4.3.2.1, 4.3.4.1).
- 4.1 e' un Obbligo e non un Principio "modello": accanto al modello funzionale
  dello SCE contiene quattro prescrizioni esplicite sullo SCDev ("shall hold
  the signing certificates", "shall hold the corresponding signature creation
  data", "shall be able to authenticate the signer", "shall create the
  signature value") e una raccomandazione sull'SCS ("should return additional
  information"); il modello funzionale resta nel testo della riga.
- 4.3.5.1 ha titolo "Description" ma e' un Obbligo: il contenuto e' una
  raccomandazione con destinatario individuabile (la firma con materiale di
  convalida a lungo termine "should be protected by applying one or more
  time-assertions" e la creazione delle time-assertions "should be repeated in
  time ... and should make use of stronger algorithms or longer key lengths").
  Allo stesso modo 4.2.6-4.2.10, pur essendo in larga parte descrittivi del
  processo, contengono "shall" e sono Obblighi.
- 4.2.5.6 (Commitment type indication) e le clausole condizionate dal contesto
  legale/funzionale (4.3.2.4.3 presentazione pre-firma, 4.3.2.4.4 invocazione
  della firma, 4.3.2.4.6 autenticazione del firmatario) portano
  `condizione_applicabilita`.
- Soggetti: il modello della clausola 4 e' locale (DA, SCA, SCS, SCDev sono
  componenti dell'ambiente del firmatario), ma nel censimento il soggetto su
  cui ricadono i requisiti di implementazione ed esercizio del sistema di
  creazione della firma e' il QTSP/gestore. Utente/titolare compare come
  destinatario nelle clausole che esistono per informare o proteggere il
  firmatario: 4.3.2.4.1 (avviso in caso di esito TOTAL-FAILED o
  INDETERMINATE), 4.3.2.4.3 (presentazione e ispezione del documento),
  4.3.2.4.4 (informativa sulle implicazioni della firma e consenso),
  4.3.2.4.6 (autenticazione del firmatario).
- Tabelle e NOTE sono contenuto della clausola che le contiene e sono
  riportate per intero in `testo_integrale`: Table 1 (input della creazione di
  una Basic Signature), Table 2 (input della creazione di Signatures with
  Time), Table 3 (input della creazione di Signatures with Long-Term
  Validation Material), Table 4 (input della creazione di Signatures providing
  Long Term Availability and Integrity of Validation Material) - una riga per
  record con separatore " | ".
- Conversione del testo: nell'file di cache la testatina/pie' di pagina
  corrente ("ETSI" e "16 ETSI EN 319 102-1 V1.4.1 (2024-06)", con pagina
  variabile) e' paratesto e non e' riportata in `testo_integrale`; le righe
  mandate a capo dal PDF sono ricomposte in paragrafi; le didascalie delle
  figure ("Figure N: ...") sono mantenute perche' parte del testo della
  clausola; gli elenchi puntati sono resi con il pallino "•" (nel testo
  convertito i sotto-elenchi della NOTE 2 di 4.1 usano il glifo wingdings
  U+F0A7, normalizzato allo stesso pallino); le due righe della didascalia di
  Table 3 e di Table 4 sono ricomposte in una sola, e la cella di Table 4
  spezzata su due righe
  ("Signature with Long-Term Validation Material or / Signature providing Long
  Term Availability and Integrity of Validation Material") e' ricostruita in
  un unico record di input.
- RELAZIONI = []: i collegamenti verso le altre fonti (compreso il rinvio
  della clausola 4 di ETSI TS 119 432 a 4.2.1 di questo documento) li
  costruisce la sessione principale; questo modulo non ne tenta nessuno.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "clausola 4.1 (Signature creation model)",
        "testo": (
            "La creazione della firma ha per obiettivo generare una firma che copra il documento del "
            "firmatario (Signer's Document, SD), il certificato di firma o un riferimento a esso, nonché "
            "gli attributi di firma che supportano la firma, la sua interpretazione e la sua finalità. Il "
            "documento adotta il modello funzionale di un Signature Creation Environment (SCE) composto "
            "da un firmatario, da una Driving Application (DA) - l'ambiente (es. un'applicazione "
            "gestionale) con cui il firmatario accede alla funzionalità di firma - e da un Signature "
            "Creation System (SCS) che implementa la funzionalità di firma; il SCS contiene a sua volta "
            "una Signature Creation Application (SCA) e un Signature Creation Device (SCDev). Le clausole "
            "4.2 e 4.3 specificano i dettagli del processo di firma: l'SCS riceve l'SD o una sua "
            "rappresentazione (SDR) insieme ad altri input dalla DA, li compone in Data To Be Signed "
            "(DTBS), li formatta in DTBSF, produce una firma sul DTBSF, formatta il risultato in un "
            "Signed Data Object (SDO) conforme al formato di firma desiderato (es. CAdES, XAdES, PAdES) e "
            "restituisce l'SDO e un'indicazione di stato alla DA. In caso di errore l'SCS dovrebbe "
            "restituire informazioni aggiuntive che consentano alla DA o al firmatario di gestirlo "
            "correttamente. Il Signature Creation Device (SCDev) deve custodire i certificati di firma "
            "(o riferimenti non ambigui a essi), custodire i corrispondenti dati di creazione della firma, "
            "essere in grado di autenticare il firmatario e creare il valore di firma usando i dati di "
            "creazione della firma del firmatario."
        ),
        "testo_integrale": (
            "The objective of signature creation is to generate a signature covering the Signer's "
            "Document (SD), the signing certificate or a reference to it, as well as signature attributes "
            "supporting the signature and its interpretation and purpose.\n"
            "The present document uses the functional model of a Signature Creation Environment (SCE) "
            "consisting of:\n"
            "• a signer that wants to create a signature;\n"
            "• a Driving Application (DA) which represents the environment (e.g. a business application) "
            "that the signer uses to access signing functionality; and\n"
            "• a Signature Creation System (SCS) which implements the signing functionality.\n"
            "NOTE 1: The involvement of a human signer is not always needed; signing can be an automated "
            "process implemented in the DA.\n"
            "Figure 1 illustrates this model. It does not distinguish between hardware or software "
            "implementations, and the model does not specify the nature of any inputs/outputs or "
            "information transfer paths between the different components (which might take the form of "
            "direct I/O devices, hardwired connections or be distributed over communications links). "
            "Also, it makes no statement about the distribution of the functions over different "
            "platforms. These aspects are implementation issues which are out of scope of the present "
            "document.\n"
            "Figure 1: Functional Model of Signature Creation\n"
            "The Signature Creation System (SCS) contains:\n"
            "• a Signature Creation Application (SCA); and\n"
            "• a Signature Creation Device (SCDev).\n"
            "Clauses 4.2 and 4.3 specify the details of the signing process, which consist of the "
            "following steps:\n"
            "• the SCS receives the Signer's Document (SD) or a Signer's Document Representation (SDR) "
            "together with other input from the DA;\n"
            "• composes this into Data To Be Signed (DTBS);\n"
            "• formats this into Data To Be Signed (Formatted) (DTBSF);\n"
            "• produces a signature over the DTBSF;\n"
            "• formats the result into a Signed Data Object (SDO) conforming to the desired signature "
            "format (e.g. CAdES [i.2], XAdES [i.4] and PAdES [i.6]); and\n"
            "• returns the SDO and a status indication to the DA.\n"
            "In case of an error, the SCS should return additional information allowing the DA or the "
            "signer to properly deal with the error.\n"
            "The Signature Creation Device (SCDev):\n"
            "• shall hold the signing certificates (or unambiguous references to them);\n"
            "• shall hold the corresponding signature creation data;\n"
            "• shall be able to authenticate the signer; and\n"
            "• shall create the signature value using the signer's signature creation data.\n"
            "NOTE 2: There are varieties of ways to implement the signature creation procedures, such "
            "as:\n"
            "• running as (part of) an application software on a device like a PC with a graphical user "
            "interface;\n"
            "• as a web service;\n"
            "• a web application;\n"
            "• a command-line tool;\n"
            "• an integrated library or a middleware for other applications."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.2 (Signature Creation Constraints)",
        "testo": (
            "Il processo di creazione della firma deve essere controllato da un insieme di vincoli di "
            "creazione (creation constraints). Tali vincoli possono essere definiti mediante una "
            "specifica formale di policy (es. una signature creation policy elaborabile "
            "automaticamente), esplicitamente in dati di controllo specifici del sistema (es. file di "
            "configurazione convenzionali come file di proprietà o file .ini, oppure memorizzati in un "
            "registro o in un database) o implicitamente dall'implementazione stessa. Vincoli aggiuntivi "
            "possono essere forniti dalla DA alla SCA tramite parametri selezionati dall'applicazione o "
            "dal firmatario: questi vincoli influenzano il processo e il risultato della creazione, "
            "indipendentemente da dove sono stati definiti."
        ),
        "testo_integrale": (
            "The signature creation process shall be controlled by a set of creation constraints. These "
            "constraints may be defined:\n"
            "• using a formal policy specification, e.g. a (machine processable) signature creation "
            "policy;\n"
            "• explicitly in system specific control data: e.g. in conventional configuration-files like "
            "property or .ini-files or stored in a registry or database; or\n"
            "• implicitly by the implementation itself.\n"
            "Additional constraints may be provided by the DA to the SCA via parameters selected by the "
            "application or the signer. These constraints influence the creation process and the creation "
            "result, irrespective of where these constraints have been defined."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.4 (Signer's Document Representation (SDR))",
        "testo": (
            "L'SDR è usato nel calcolo della firma come rappresentazione dell'SD e può essere fornito "
            "dalla DA alla SCA; quando la DA non fornisce l'SDR, la SCA deve calcolare l'SDR dall'SD "
            "applicando l'algoritmo specificato dalla signature creation policy in uso. Deve essere "
            "inattuabile (infeasible) trovare un altro SD rappresentato dallo stesso SDR. Nota: alcuni "
            "formati di firma non incorporano direttamente l'SD nella firma; un tipico SDR può basarsi su "
            "una funzione di hash crittografica, ma specificare i dettagli del calcolo di un SDR è fuori "
            "dal perimetro del documento - si tratta di calcoli specifici del formato, che possono essere "
            "complessi, specialmente nel caso di ASIC o XMLDSig."
        ),
        "testo_integrale": (
            "The SDR is used in the calculation of the signature as a representation of the SD. The SDR "
            "may be provided by the DA to the SCA. Whenever the DA does not provide the SDR, the SCA "
            "shall calculate the SDR from the SD by applying the algorithm specified by the signature "
            "creation policy in use.\n"
            "It shall be infeasible to find another SD that is represented by the same SDR.\n"
            "NOTE: Some signature formats do not incorporate the SD directly into the signature. While a "
            "typical SDR can be based on a cryptographic hash function, it is out of scope for the "
            "present document to specify details of the calculation of an SDR. Such calculations are "
            "format specific and can be complex, especially in the case of ASIC or XMLDSig."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.5.1 (General requirements)",
        "testo": (
            "Gli attributi di firma devono essere informazioni che supportano la firma AdES, la sua "
            "interpretazione e la sua finalità e che possono essere coperte dalla firma insieme all'SD; "
            "devono essere forniti direttamente dal firmatario, oppure selezionati tramite la DA, oppure "
            "inseriti automaticamente nella firma dall'SCS. Gli attributi devono essere attributi firmati "
            "(coperti dalla firma) oppure attributi non firmati (non protetti dalla firma); gli attributi "
            "non firmati possono anche essere aggiunti a una firma in una fase successiva. L'insieme "
            "degli attributi inclusi in una firma è definito dalla signature creation policy utilizzata "
            "o, quando si aumenta (augment) una firma, dalla signature augmentation policy utilizzata "
            "(ETSI TS 119 172-1) e può anche essere specifico del formato. Le clausole da 4.2.5.2 a "
            "4.2.5.10 specificano gli attributi di firma di uso comune, i cui esempi e usi sono nelle "
            "specifiche delle firme AdES ETSI EN 319 122-1 (CAdES), ETSI EN 319 132-1 (XAdES) ed ETSI EN "
            "319 142-1 (PAdES). Una firma può contenere altri attributi di firma specifici "
            "dell'applicazione. Nota: l'implementazione degli attributi dentro una firma dipende dal "
            "formato e le specifiche di formato usano termini diversi (property, attribute o dictionary "
            "entries); \"attribute\" è stato scelto come termine generico."
        ),
        "testo_integrale": (
            "Signature attributes shall be pieces of information that support the AdES signature and its "
            "interpretation and purpose and which may be covered by the signature together with the SD. "
            "The signature attributes shall be either directly provided by the signer or selected through "
            "the DA or automatically inserted into the signature by the SCS.\n"
            "Attributes shall either be signed attributes, i.e. attributes that are covered by the "
            "signature, or unsigned attributes, i.e. attributes that are not secured by the signature. "
            "Unsigned attributes may also be added to a signature at a later stage. The set of attributes "
            "included in a signature is defined by the signature creation policy used or, when augmenting "
            "a signature, by the signature augmentation policy (ETSI TS 119 172-1 [4]) used and can also "
            "be format specific.\n"
            "Clauses 4.2.5.2 to 4.2.5.10 specify signature attributes that are commonly used. Examples "
            "of this information and its uses are contained in the ETSI AdES signatures specifications "
            "ETSI EN 319 122-1 [i.2], ETSI EN 319 132-1 [i.4], ETSI EN 319 142-1 [i.6].\n"
            "A signature may contain other signature attributes that are application-specific.\n"
            "NOTE: How attributes are implemented within a signature is format-dependent and format "
            "specifications use different terms for this: property, attribute or dictionary entries. "
            "\"Attribute\" has been chosen as the generic term."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.5.2 (Signing certificate identifier)",
        "testo": (
            "L'attributo identificativo del certificato di firma (signing certificate identifier) deve "
            "essere un attributo firmato e deve contenere un riferimento al certificato di firma. Nota 1: "
            "l'attributo impedisce la sostituzione del certificato referenziato con un altro di semantica "
            "diversa ma con la stessa chiave pubblica; se il firmatario possiede certificati diversi "
            "legati a dati di creazione della firma diversi, indica al verificatore i corretti dati di "
            "verifica della firma. L'attributo può anche contenere riferimenti ad alcuni o a tutti i "
            "certificati del percorso del certificato di firma, compreso un riferimento all'anchor di "
            "fiducia quando questo è un certificato (Nota 2: in tal caso i riferimenti identificano un "
            "insieme di certificati raccomandato come catena di certificati per convalidare il certificato "
            "di firma). Per ciascun certificato l'attributo deve contenere un digest unitamente a un "
            "identificatore univoco dell'algoritmo usato per calcolare quel digest; tale algoritmo deve "
            "essere una funzione di hash crittografica."
        ),
        "testo_integrale": (
            "This attribute shall be a signed attribute.\n"
            "This attribute shall contain one reference to the signing certificate.\n"
            "NOTE 1: This attribute prevents substitution of the referenced certificate with another one "
            "with different semantics but the same public key. If the signer holds different certificates "
            "related to different signature creation data it indicates the correct signature verification "
            "data to the verifier.\n"
            "This attribute may also contain references to some of or all the certificates within the "
            "signing certificate path, including one reference to the trust anchor when this is a "
            "certificate.\n"
            "NOTE 2: If so, these references identify a set of certificates that are recommended as the "
            "certificate chain used to validate the signing certificate.\n"
            "For each certificate, the attribute shall contain a digest together with a unique identifier "
            "of the algorithm that has been used to calculate that digest. This algorithm shall be a "
            "cryptographic hash function."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.5.3 (Signature policy identifier)",
        "testo": (
            "L'attributo identificativo della policy di firma (signature policy identifier) deve essere "
            "un attributo firmato e può contenere un identificatore univoco che identifica la signature "
            "creation policy applicata durante la creazione della firma (Nota 1: per requisiti aggiuntivi "
            "si vedano le specifiche delle firme AdES; Nota 2: l'attributo può essere presente se "
            "richiesto dal contesto di firma, ad esempio in un accordo commerciale specificato - una "
            "signature creation policy può servire a chiarire il ruolo preciso e gli impegni che il "
            "firmatario intende assumere rispetto all'SD). L'attributo deve inoltre contenere un digest "
            "il cui valore è calcolato sul documento della policy di firma, unitamente a un "
            "identificatore dell'algoritmo usato per calcolare quel digest, oppure una versione "
            "trasformata del documento della policy di firma."
        ),
        "testo_integrale": (
            "This attribute shall be a signed attribute.\n"
            "The signature policy identifier attribute may contain a unique identifier identifying the "
            "signature creation policy that has been applied during signature creation.\n"
            "NOTE 1: See AdES digital signatures specifications for additional requirements.\n"
            "NOTE 2: This attribute can be present if required by the signing context (e.g. in a "
            "specified trading agreement). For instance, a signature creation policy can be used to "
            "clarify the precise role and commitments that the signer intends to assume with respect to "
            "the SD.\n"
            "This attribute shall also contain a digest whose value is computed on the signature policy "
            "document, together with an identifier for the algorithm used to calculate that digest, or a "
            "transformed version of the signature policy document."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.5.4 (Signature policy store)",
        "testo": (
            "L'attributo signature policy store deve essere un attributo non firmato e deve contenere il "
            "documento della policy di firma referenziato nell'attributo signature policy identifier, in "
            "modo che possa essere usato per la convalida offline e a lungo termine, oppure un URI che "
            "referenzia un archivio locale dove il documento può essere recuperato. L'attributo deve "
            "contenere un identificatore della sintassi usata per produrre il documento della policy di "
            "firma."
        ),
        "testo_integrale": (
            "This attribute shall be an unsigned attribute.\n"
            "This attribute shall hold:\n"
            "• the signature policy document which is referenced in the signature policy identifier "
            "attribute so that it can be used for offline and long-term validation; or\n"
            "• a URI referencing a local store where the present document can be retrieved.\n"
            "The attribute shall contain an identifier of the syntax used for producing the signature "
            "policy document."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.5.5 (Data content type)",
        "testo": (
            "L'attributo data content type deve essere un attributo firmato e deve indicare il tipo "
            "dell'SD. Nota: attributi aggiuntivi possono specificare ulteriori informazioni sul documento "
            "firmato - ad esempio, nel presentare dati firmati a un utente umano può essere importante che "
            "non vi sia ambiguità sulla presentazione del Signed Data Object alla relying party: perché "
            "la relying party possa selezionare la rappresentazione appropriata (es. testo, audio o "
            "video), l'informazione sul content type può essere indicata dal firmatario."
        ),
        "testo_integrale": (
            "This attribute shall be a signed attribute.\n"
            "The data content type attribute shall indicate the type of the SD.\n"
            "NOTE: Additional attributes can specify additional information about the signed document. "
            "For instance, when presenting signed data to a human user, having no ambiguity as to the "
            "presentation of the Signed Data Object to the relying party can be important. In order for "
            "the appropriate representation (e.g. text, sound or video) to be selected by the relying "
            "party, information on the content type can be indicated by the signer."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.5.6 (Commitment type indication)",
        "testo": (
            "L'attributo commitment type indication deve essere un attributo firmato e deve indicare "
            "l'impegno (commitment) o gli impegni assunti dal firmatario firmando determinati documenti. "
            "Il commitment type indicato deve essere espresso nella forma di un OID oppure di un URI e "
            "può contenere una sequenza di qualificatori che forniscono maggiori informazioni "
            "sull'impegno. Se è presente un riferimento a una signature policy e la policy referenziata "
            "elenca un insieme di commitment type ammessi, il contenuto di questo attributo deve essere "
            "selezionato dall'insieme specificato da quella policy. Nota: se una firma AdES non contiene "
            "un commitment type riconosciuto, la semantica della firma AdES dipende dalla semantica del "
            "documento firmato e dal contesto in cui è usata."
        ),
        "testo_integrale": (
            "This attribute shall be a signed attribute.\n"
            "This attribute shall indicate commitment(s) made by the signer when signing certain "
            "documents.\n"
            "The commitment type indicated shall be expressed in form of either an OID or a URI. It may "
            "contain a sequence of qualifiers providing more information about the commitment.\n"
            "If a signature policy reference is present, and the referenced policy lists a set of "
            "allowed commitment types, the content of this attribute shall be selected from the set "
            "specified by that policy.\n"
            "NOTE: If an AdES signature does not contain a recognized commitment type then the semantics "
            "of the AdES signature is dependent on the semantics of the document being signed and the "
            "context in which it is being used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Ultimo requisito (selezione dall'insieme ammesso): solo se è presente un riferimento a una "
            "signature policy e la policy referenziata elenca un insieme di commitment type ammessi."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.5.7 (Counter signatures)",
        "testo": (
            "L'attributo delle controfirme (counter signatures) deve essere un attributo non firmato e "
            "deve contenere una controfirma della firma. Nota: le controfirme sono firme applicate una "
            "dopo l'altra e sono usate quando è importante l'ordine in cui le firme sono applicate; in "
            "queste situazioni la prima firma firma i documenti firmati e ciascuna firma aggiuntiva può "
            "firmare a sua volta l'ultima firma generata in precedenza, oppure tutte le firme generate in "
            "precedenza insieme al documento firmato."
        ),
        "testo_integrale": (
            "This attribute shall be an unsigned attribute.\n"
            "This attribute shall contain one countersignature of the signature.\n"
            "NOTE: Countersignatures are signatures that are applied one after the other and are used "
            "where the order in which the signatures are applied is important. In these situations, the "
            "first signature signs the signed documents. Each additional signature can sign in turn the "
            "latest previously generated signature, or all the previously generated signatures together "
            "with the signed document."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.5.8 (Claimed signing time)",
        "testo": (
            "L'attributo claimed signing time deve essere un attributo firmato e deve contenere l'ora in "
            "cui il firmatario dichiara di avere eseguito il processo di firma. Nota: come nel caso delle "
            "firme su carta, l'ora della firma può essere solo dichiarata (claimed); se le policy di "
            "firma richiedono più di una dichiarazione sull'ora della firma occorre usare metodi come le "
            "marche temporali."
        ),
        "testo_integrale": (
            "This attribute shall be a signed attribute.\n"
            "This attribute shall contain the time at which the signer claims to having performed the "
            "signing process.\n"
            "NOTE: As is the case with paper-based signatures, the time of the signature can only be a "
            "claimed one. Methods like time-stamps will need to be used in case the signature policies "
            "require more than claims for the signature time."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.5.9 (Claimed signer location)",
        "testo": (
            "L'attributo claimed signer location deve essere un attributo firmato e deve specificare un "
            "indirizzo associato al firmatario in una particolare localizzazione geografica (es. città) "
            "dove il firmatario dichiara di avere prodotto la firma. Nota: in alcune transazioni è "
            "necessario il luogo in cui il firmatario si trovava al momento della creazione della firma."
        ),
        "testo_integrale": (
            "This attribute shall be a signed attribute.\n"
            "This attribute shall specify an address associated with the signer at a particular "
            "geographical (e.g. city) location where the signer claims to having produced the signature.\n"
            "NOTE: In some transactions, the place where the signer was at the time of signature "
            "creation is needed."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.5.10 (Signer's attributes)",
        "testo": (
            "L'attributo signer's attributes deve essere un attributo firmato e deve contenere attributi "
            "o asserzioni firmate che il firmatario dichiara o prova di possedere al momento in cui la "
            "firma è stata generata; ciò deve avvenire usando un attributo dichiarato dal firmatario "
            "(signer's claimed attribute), un attribute certificate emesso da un'attribute authority, "
            "oppure asserzioni firmate emesse da un prestatore di servizi. Nota: se il nome del "
            "firmatario è importante, la posizione del firmatario all'interno di una azienda o "
            "organizzazione può esserlo ancora di più - alcuni contratti possono essere validi solo se "
            "firmati da un utente in un ruolo particolare, es. un direttore commerciale: in molti casi "
            "non è tanto importante sapere chi sia realmente il direttore commerciale, quanto essere "
            "certi che il firmatario sia autorizzato dalla sua azienda a esserlo."
        ),
        "testo_integrale": (
            "This attribute shall be a signed attribute.\n"
            "This attribute shall contain attributes or signed assertions that the signer claims or "
            "proves to be in possession of when the signature was generated. This shall be done using:\n"
            "• a signer's claimed attribute;\n"
            "• an attribute certificate issued by an attribute authority; or\n"
            "• signed assertions issued by a service provider.\n"
            "NOTE: While the name of the signer is important, the position of the signer within a "
            "company or an organization can be even more important. Some contracts can only be valid if "
            "signed by a user in a particular role, e.g. a sales director. In many cases, it is not that "
            "important to know who the sales director really is, but being sure that the signer is "
            "empowered by his company to be the sales director can be fundamental."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.6 (Data To Be Signed (DTBS))",
        "testo": (
            "I dati da firmare (Data To Be Signed, DTBS) devono essere costruiti dagli oggetti "
            "informativi che devono essere coperti dalla firma: l'SD o l'SDR, e gli attributi di firma "
            "selezionati per essere firmati insieme all'SD. La costruzione del DTBS può includere una "
            "pre-elaborazione specifica del formato. Nota 1: una firma è tipicamente calcolata sull'SDR e "
            "su alcuni attributi; quando non ci sono attributi, alcuni formati di firma consentono di "
            "usare direttamente l'SDR nella creazione della firma. Nota 2: esempi di pre-elaborazione "
            "opzionale sono la canonicalizzazione/normalizzazione, il filtraggio XPath o la "
            "trasformazione XSL; il risultato di questo passo è l'oggetto informativo coperto dalla "
            "firma come risultato dei processi di firma, incluso nel calcolo e nella verifica della "
            "firma."
        ),
        "testo_integrale": (
            "The data to be signed shall be constructed from the information objects that are to be "
            "covered by the signature. These are:\n"
            "• the SD or the SDR; and\n"
            "• the signature attributes selected to be signed together with the SD.\n"
            "The construction of the DTBS may include format-specific pre-processing.\n"
            "NOTE 1: A signature is typically made over the SDR and some attributes. When there are no "
            "attributes, some signature formats allow using the SDR directly when creating the "
            "signature.\n"
            "NOTE 2: Examples for optional pre-processing include canonicalization/normalization, XPath "
            "filtering or XSL transformation. The result of this step is the information object that is "
            "covered by the signature as the result of the signing processes and which is included in "
            "the signature calculation and verification."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.7 (Data To Be Signed (Formatted) (DTBSF))",
        "testo": (
            "Il DTBSF (Data To Be Signed (Formatted)) deve essere creato a partire dagli oggetti DTBS, "
            "formattandoli e disponendoli nella sequenza corretta per il processo di firma."
        ),
        "testo_integrale": (
            "The DTBSF shall be created from the DTBS objects by formatting them and placing them in the "
            "correct sequence for the signing process."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.8 (Data To Be Signed Representation (DTBSR))",
        "testo": (
            "Il componente di preparazione del DTBS deve prendere il DTBSF e calcolarne l'hash secondo "
            "l'algoritmo di hash specificato nella suite crittografica; il risultato di questo processo è "
            "il DTBSR, che viene poi usato per creare la firma. Nota: perché l'hash prodotto sia "
            "rappresentativo del DTBSF, la funzione di hash ha la proprietà di rendere "
            "computazionalmente inattuabile trovare collisioni per la vita attesa della firma; se la "
            "funzione di hash dovesse indebolirsi in futuro si possono adottare misure di sicurezza "
            "aggiuntive, come l'applicazione di time-stamp token."
        ),
        "testo_integrale": (
            "The DTBS preparation component shall take the DTBSF and hash it according to the hash "
            "algorithm specified in the cryptographic suite. The result of this process is the DTBSR, "
            "which is then used to create the signature.\n"
            "NOTE: In order for the produced hash to be representative of the DTBSF, the hashing "
            "function has the property that it is computationally infeasible to find collisions for the "
            "expected signature lifetime. Should the hash function become weak in the future, additional "
            "security measures, such as applying time-stamp tokens, can be taken."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.9 (Signature)",
        "testo": (
            "Lo SCDev deve prendere il DTBSR e applicare l'algoritmo di firma specificato nella suite "
            "crittografica; il risultato di questo processo deve essere il valore di firma (signature "
            "value)."
        ),
        "testo_integrale": (
            "The SCDev shall take the DTBSR and apply the signature algorithm specified in the "
            "cryptographic suite. The result of this process shall be the signature value."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.10 (Signed Data Object (SDO))",
        "testo": (
            "Il Signed Data Object Composer deve produrre un SDO prendendo il valore di firma calcolato "
            "e formattandolo secondo il tipo di SDO (SDO Type). L'SDO deve contenere il valore di firma e "
            "gli attributi firmati; può inoltre contenere l'SD o l'SDR e/o attributi non firmati "
            "aggiuntivi di supporto."
        ),
        "testo_integrale": (
            "The Signed Data Object Composer shall produce a SDO by taking the signature value "
            "calculated and formatting it according to the SDO Type. The SDO shall contain:\n"
            "• the signature value; and\n"
            "• the signed attributes.\n"
            "The SDO may additionally contain the following:\n"
            "• the SD or SDR; and/or\n"
            "• additional supportive unsigned attributes."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.11 (Validation data)",
        "testo": (
            "Alcune classi di firme AdES incorporano dati aggiuntivi necessari per la convalida: questi "
            "dati aggiuntivi, chiamati validation data, sono il risultato di un processo di signature "
            "augmentation e devono includere i certificati di chiave pubblica (Public Key Certificates, "
            "PKC), istanze di dati di revoca (revocation data) e time-assertions applicate alla firma. Le "
            "validation data possono anche includere altri dati aggiuntivi necessari o utili alla "
            "convalida, come gli attribute certificate (AC) e le informazioni sullo stato di revoca degli "
            "AC. Le validation data possono essere raccolte dal firmatario e/o dal verificatore."
        ),
        "testo_integrale": (
            "Some classes of AdES signatures incorporate additional data needed for validation. This "
            "additional data, called validation data, is the result of a signature augmentation process "
            "and shall include:\n"
            "• Public Key Certificates (PKCs);\n"
            "• Instances of revocation data; and\n"
            "• time-assertions applied to the signature.\n"
            "Validation data may also include other additional data necessary or useful for validation "
            "like Attributes Certificates (ACs) and revocation status information for ACs.\n"
            "The validation data may be collected by the signer and/or the verifier."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.2.2 (Inputs)",
        "testo": (
            "Input della creazione di una Basic Signature (Tabella 1): documento del firmatario (SD) o "
            "sua rappresentazione (SDR), obbligatorio; certificato di firma, obbligatorio; altri "
            "attributi di firma, opzionali; signature creation policy, opzionale. Nota della tabella: una "
            "firma può anche contenere l'ora in cui è stata creata; si assume che l'ora corrente sia "
            "disponibile in modo accurato alla SCA e non è elencata come input per evitare di dare "
            "l'impressione che questo valore di tempo possa essere scelto a piacere."
        ),
        "testo_integrale": (
            "Table 1: Inputs to the Basic Signature Creation process\n"
            "Input | Requirement\n"
            "Signer's Document or Signer's Document Representation | Mandatory\n"
            "Signing Certificate | Mandatory\n"
            "Other Signature Attributes | Optional\n"
            "Signature Creation Policy | Optional\n"
            "NOTE: A signature can also contain the time when the signature has been created. It is "
            "assumed that the current time is accurately available to the SCA. It is not listed as an "
            "input to avoid giving the impression that this time value can be selected at will."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.2.3 (Outputs)",
        "testo": (
            "L'output del processo di creazione di una Basic Signature è un SDO che deve contenere il "
            "valore di firma, un riferimento al certificato di firma o una sua copia come attributo "
            "firmato, e gli eventuali attributi firmati o non firmati opzionali (es. un signature policy "
            "identifier, clausola 4.2.5.3). Nota 1: una Basic Signature è progettata per prevenire "
            "semplici attacchi di sostituzione e riemissione e per specificare il certificato da usare "
            "per verificare la firma. Nota 2: attributi obbligatori aggiuntivi possono essere definiti "
            "specificamente dal formato. La Figura 6 illustra una Basic Signature."
        ),
        "testo_integrale": (
            "The output of the Basic Signature creation process is an SDO that shall contain:\n"
            "• the signature value;\n"
            "• a reference to or a copy of the signing certificate as a signed attribute; and\n"
            "• any optional signed or unsigned attributes (e.g. a signature policy identifier (see "
            "clause 4.2.5.3)).\n"
            "NOTE 1: A Basic Signature is designed to prevent simple substitution and reissuing attacks "
            "and to specify the certificate to be used for verifying the signature.\n"
            "NOTE 2: Additional mandatory attributes can be format specifically defined.\n"
            "Figure 6 illustrates a Basic Signature.\n"
            "Figure 6: Basic Signature"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.2.4.1 (Selection of documents to sign)",
        "testo": (
            "La Driving Application deve selezionare uno o più documenti da firmare, automaticamente "
            "oppure esplicitamente da parte del firmatario tramite un'interfaccia utente; il processo di "
            "selezione può specificare che solo determinate parti di un documento siano da firmare "
            "(Nota: requisiti legali possono imporre il coinvolgimento esplicito del firmatario nella "
            "selezione del documento da firmare). Quando un documento è selezionato per la firma, ogni "
            "firma esistente sul documento o allegata a esso dovrebbe essere convalidata; se la firma è "
            "convalidata, deve essere fornito un avviso nel caso in cui la convalida di una firma "
            "esistente produca un risultato TOTAL-FAILED o INDETERMINATE."
        ),
        "testo_integrale": (
            "The Driving Application shall select one or more documents to be signed either "
            "automatically or explicitly by the signer through a user interface.\n"
            "The selection process may specify that only certain parts of a document are to be signed.\n"
            "NOTE: Legal requirements can mandate explicit signer involvement in selection of document "
            "to sign.\n"
            "When a document is selected for signing, any existing signature on or attached to the "
            "document should be validated. If the signature is validated, a warning shall be provided in "
            "case validation of an existing signature yields a TOTAL-FAILED or INDETERMINATE result."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 4.3.2.4.2 (Signature attribute and parameters selection)",
        "testo": (
            "L'attributo signing certificate identifier (clausola 4.2.5.2) deve essere incluso nel DTBS "
            "ogni volta che il formato e il contenuto della firma lo richiedono; altri attributi possono "
            "essere inclusi nel DTBS o come attributi non firmati nell'SDO risultante (Nota 1: nelle "
            "firme XAdES è possibile firmare il certificato di firma presente nell'elemento ds:Keyinfo; "
            "in questo caso l'attributo signing certificate identifier non è richiesto). Il processo di "
            "firma deve essere guidato da parametri aggiuntivi che devono almeno determinare il formato "
            "dell'SDO (es. CAdES, XAdES, PAdES) e la classe della firma da creare (es. Basic Signature, "
            "Signature with Time, ecc.) e, quando necessario, se debba essere creata una firma detached, "
            "enveloped o enveloping. Il certificato e altri attributi e parametri devono essere "
            "selezionati da uno o da una combinazione dei seguenti: la DA, che trasmette gli attributi "
            "come parametri sull'interfaccia verso la SCA; il firmatario, tramite un'interfaccia utente "
            "offerta dalla DA o dal SCS; la configurazione locale nel SCS; oppure altri mezzi, come "
            "l'importazione di una Signature Policy nella DA o nel SCS (Nota 2: il certificato di firma, "
            "ed eventualmente l'intero percorso del certificato, può molto spesso essere ottenuto dallo "
            "SCDev del firmatario)."
        ),
        "testo_integrale": (
            "The signing certificate identifier attribute (see clause 4.2.5.2) shall be included in the "
            "DTBS whenever required by the format and the contents of the signature. Other attributes "
            "may be included in the DTBS or as unsigned attributes in the resulting SDO.\n"
            "NOTE 1: In XAdES signatures, it is possible to sign the signing certificate present within "
            "the ds:Keyinfo element. In this case, the signing certificate identifier attribute is not "
            "required.\n"
            "The signing process shall be guided by additional parameters that at least shall determine "
            "the format of the SDO (e.g. CAdES, XAdES, PAdES) and the class (e.g. Basic Signature, "
            "Signature with Time, etc.) of the signature to create, and when necessary whether a "
            "detached, enveloped or enveloping signature shall be created.\n"
            "Certificate and other attributes and parameters shall be selected by one or a combination "
            "of:\n"
            "• The DA, conveying the attributes as parameters over the interface to the SCA.\n"
            "• The signer through a user interface offered by the DA or the SCS.\n"
            "• Local configuration in the SCS. Or\n"
            "• Other means, such as importing a Signature Policy to the DA or the SCS.\n"
            "NOTE 2: The signing certificate, possibly the complete certificate path, can most often be "
            "obtained from the signer's SCDev."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.2.4.3 (Pre-signature presentation)",
        "testo": (
            "Quando requisiti legali o funzionali specifici richiedono che un documento da firmare sia "
            "presentato al firmatario, la DA deve presentare il documento da firmare; negli altri casi la "
            "DA dovrebbe mettere il firmatario in grado di ispezionare il documento da firmare. Nota 1: "
            "la presentazione del documento da firmare non è sempre opportuna - un esempio è la firma in "
            "blocco di molti documenti in una sola operazione (es. fatture), un altro è la firma di "
            "prescrizioni mediche, dove il dialogo utente presenta le informazioni sui medicinali ma non "
            "necessariamente i documenti di prescrizione finali (più prescrizioni per un paziente possono "
            "essere firmate a seguito di un unico consenso dell'utente). Il documento presentato deve "
            "essere uguale nel contenuto al documento che viene firmato (Nota 2: si usa \"uguale nel "
            "contenuto\" invece di \"lo stesso\", perché la rappresentazione firmata può essere in un "
            "formato diverso da quello visualizzato, es. XML). La DA dovrebbe mettere il firmatario in "
            "grado di ispezionare gli attributi selezionati per il processo di firma; la DA può affidarsi "
            "al SCS per tutta o parte della presentazione del documento da firmare e degli attributi. "
            "Quando un documento da firmare è presentato, il risultato di convalida di ogni firma "
            "esistente sul documento o allegata a esso dovrebbe essere presentato al firmatario come da "
            "clausola 4.3.2.4.1. La SCA può consentire al firmatario di ispezionare un documento da "
            "firmare e/o gli attributi selezionati per il processo di firma tramite un'interfaccia utente "
            "separata, esterna all'ambiente della DA."
        ),
        "testo_integrale": (
            "When specific legal or functional requirements require that a document to sign is presented "
            "to the signer, the DA shall present the document to sign. In other cases, the DA should "
            "enable the signer to inspect the document to sign.\n"
            "NOTE 1: Presentation of a document to sign is not always convenient. One example is bulk "
            "signing of many documents in one operation (e.g. invoices). Another example is signing of "
            "medical prescriptions where the user dialogue presents the medication information but not "
            "necessarily the final prescription documents (several prescriptions for one patient can be "
            "signed following one user consent).\n"
            "The presented document shall be equal in content to the document that is signed.\n"
            "NOTE 2: \"Equal in content\" is used instead of \"the same\", as the representation that is "
            "signed can be another format than the one displayed (e.g. XML).\n"
            "The DA should enable the signer to inspect attributes selected for the signing process.\n"
            "The DA may rely upon the SCS for whole or parts of the presentation of a document to sign "
            "and of attributes.\n"
            "When a document to sign is presented, the validation result of any existing signature on or "
            "attached to the document should be presented to the signer as per clause 4.3.2.4.1.\n"
            "The SCA may allow the signer to inspect a document to sign and/or attributes selected for "
            "the signing process through a separate user interface, outside of the DA environment."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Presentazione obbligatoria solo quando requisiti legali o funzionali specifici richiedono "
            "che il documento da firmare sia presentato al firmatario; negli altri casi resta la "
            "raccomandazione di consentirne l'ispezione."
        ),
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 4.3.2.4.4 (Signature invocation)",
        "testo": (
            "Quando requisiti legali o funzionali specifici richiedono il consenso dell'utente prima "
            "dell'invocazione della firma, la DA deve: a) seguire la procedura di cui alla clausola "
            "4.3.2.4.3; b) informare il firmatario delle implicazioni della firma; c) ottenere il "
            "consenso dal firmatario. La DA può affidarsi al SCS per tutta o parte del dialogo utente. "
            "Una volta ricevuto il consenso dell'utente, la DA deve invocare la firma al SCS/SCA."
        ),
        "testo_integrale": (
            "When specific legal or functional requirements require user consent prior to signature "
            "invocation, the DA shall:\n"
            "a) follow the procedure as per clause 4.3.2.4.3;\n"
            "b) inform the signer of the implications of signing; and\n"
            "c) get consent from the signer.\n"
            "The DA may rely upon the SCS for whole or parts of the user dialogue.\n"
            "Once user consent has been received, the DA shall invoke the signature to the SCS/SCA."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Requisiti a)-c) e invocazione subordinata al consenso: solo quando requisiti legali o "
            "funzionali specifici richiedono il consenso dell'utente prima dell'invocazione della firma."
        ),
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 4.3.2.4.5 (Signing)",
        "testo": (
            "Lo SCDev deve eseguire l'operazione di firma (Nota: per requisiti aggiuntivi "
            "sull'autenticazione dell'utente per l'attivazione dei dati di creazione della firma si veda "
            "la clausola 4.3.2.4.6). Prima di invocare l'uso dei dati di creazione della firma, il SCS "
            "(SCA o SCDev) dovrebbe verificare che il certificato di firma sia valido (corretto "
            "crittograficamente, entro il suo periodo di validità e non revocato). Quando lo SCDev "
            "restituisce la firma, la SCA dovrebbe verificarla usando la chiave pubblica del certificato "
            "del firmatario."
        ),
        "testo_integrale": (
            "The SCDev shall perform the signing operation.\n"
            "NOTE: See clause 4.3.2.4.6 for additional requirements on user authentication for the "
            "activation of the signature creation data.\n"
            "Before invoking use of the signature creation data, the SCS (SCA or SCDev) should check "
            "that the signing certificate is valid (cryptographically correct, within its validity "
            "period and not revoked).\n"
            "When the SCDev returns the signature, the SCA should verify the signature using the public "
            "key from the signer's certificate."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.2.4.6 (Signer authentication)",
        "testo": (
            "L'uso dei dati di creazione della firma del firmatario (la chiave privata) nello SCDev può "
            "richiedere che il firmatario sia autenticato verso lo SCDev. A seconda del metodo o dei "
            "metodi di autenticazione specifici, l'utente può interagire con l'interfaccia utente della "
            "DA, della SCA o dello SCDev; più di un meccanismo di autenticazione può essere usato per "
            "fornire sufficiente assurance di autenticazione. Un meccanismo di autenticazione del "
            "firmatario può essere di una forma che previene attacchi di impersonificazione anche da "
            "parte della DA o della SCA e del loro ambiente. Nota 1: la natura dei meccanismi di "
            "autenticazione è determinata dallo SCDev usato; esistono standard per diverse interfacce, "
            "tipi di SCDev e meccanismi di autenticazione. Nota 2: in alcuni casi l'autenticazione del "
            "firmatario sarà obbligatoria e potranno essere imposti ulteriori requisiti sulla natura dei "
            "meccanismi di autenticazione e delle interfacce."
        ),
        "testo_integrale": (
            "The use of the signer's signature creation data (the private key) in the SCDev may require "
            "the signer to be authenticated towards the SCDev.\n"
            "Depending on the specific authentication method(s), the user may interact with the user "
            "interface to the DA, to the SCA, or the SCDev. More than one authentication mechanism may "
            "be used to provide sufficient authentication assurance.\n"
            "A signer authentication mechanism may be of a form that prevents impersonation attacks even "
            "from the DA or the SCA and their environment.\n"
            "NOTE 1: The nature of authentication mechanisms are determined by the SCDev used. Standards "
            "exist for different interfaces, SCDev types, and authentication mechanisms.\n"
            "NOTE 2: In some cases, signer authentication will be mandatory and further requirements on "
            "the nature of the authentication mechanisms and interfaces can be imposed."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Autenticazione del firmatario verso lo SCDev: richiesta quando l'uso dei dati di creazione "
            "della firma la impone (in alcuni casi sarà obbligatoria, Nota 2); i meccanismi che "
            "prevengono l'impersonificazione anche da DA/SCA restano una possibilità."
        ),
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 4.3.2.4.7 (SDO composition)",
        "testo": (
            "Al ritorno della firma dallo SCDev, la SCA deve comporre l'SDO secondo il formato richiesto; "
            "ulteriori attributi possono essere inclusi nell'SDO. Alla DA deve essere restituita "
            "un'indicazione di stato, che deve avere uno di due valori: OK - la firma è stata creata con "
            "successo, e in questo caso l'SDO deve essere restituito alla DA; FAILED - l'SCS non è stato "
            "in grado di creare una firma. In caso di errore l'SCS dovrebbe restituire informazioni "
            "aggiuntive che consentano alla DA o al firmatario di gestirlo correttamente."
        ),
        "testo_integrale": (
            "Upon return of the signature from the SCDev, the SCA shall compose the SDO according to the "
            "required format. Further attributes may be included in the SDO.\n"
            "A status indication shall be returned to the DA.\n"
            "The status indication shall have one of two values:\n"
            "• OK: The signature has been successfully created; in this case, the SDO shall also be "
            "returned to the DA;\n"
            "• FAILED: The SCS was unable to create a signature.\n"
            "In case of an error, the SCS should return additional information allowing the DA or the "
            "signer to properly deal with the error."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.3.2 (Inputs)",
        "testo": (
            "Input del processo di creazione di una Signature with Time (Tabella 2): Basic Signature, "
            "obbligatoria; signature augmentation policy, opzionale."
        ),
        "testo_integrale": (
            "Table 2: Inputs to the creation process for Signatures with Time\n"
            "Input | Requirement\n"
            "Basic Signature | Mandatory\n"
            "Signature Augmentation Policy | Optional"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.3.3 (Outputs)",
        "testo": (
            "Il processo di creazione di una Signature with Time deve restituire la firma fornita con "
            "l'aggiunta di un attributo non firmato contenente un time-stamp token sulla firma."
        ),
        "testo_integrale": (
            "The process for creating a Signature with Time shall return the signature provided with an "
            "added unsigned attribute containing a time-stamp token on the signature."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.3.4 (Process)",
        "testo": (
            "Il processo di signature augmentation deve: 1) richiedere uno o più time-stamp token alle "
            "TSA appropriate come definite nella signature policy o nella configurazione locale - il "
            "time-stamp token deve coprire il valore di firma; 2) produrre un attributo di firma che "
            "incapsula i time-stamp token prodotti al passo 1); 3) aggiungere l'attributo di firma del "
            "passo 2) come attributo non firmato all'SDO. Nota: quando la convalida di una firma fallisce, "
            "l'aggiunta di una marca temporale non sempre aiuta a preservare la firma - l'SVA può "
            "opzionalmente convalidare la firma prima di richiedere una marca temporale e, in caso di "
            "TOTAL-FAILED, interrompere il processo."
        ),
        "testo_integrale": (
            "The signature augmentation process shall:\n"
            "1) Request one or more time-stamp tokens from appropriate TSAs as defined in the signature "
            "policy or local configuration. The time-stamp token shall cover the signature value.\n"
            "2) Produce a signature attribute encapsulating the time-stamp token(s) produced in step 1). "
            "And\n"
            "3) Add the signature attribute of step 2) as an unsigned attribute to the SDO.\n"
            "NOTE: When the validation of a signature fails, adding a time-stamp will not always help "
            "preserving the signature. The SVA can optionally validate the signature before requesting a "
            "time-stamp and in case of TOTAL-FAILED abort the process."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.4.2 (Inputs)",
        "testo": (
            "Input del processo di creazione di una Signature with Long-Term Validation Material "
            "(Tabella 3): Signature with Time, obbligatoria; signature augmentation policy, opzionale."
        ),
        "testo_integrale": (
            "Table 3: Inputs to the creation process for Signatures with Long-Term Validation Material\n"
            "Input | Requirement\n"
            "Signature with Time | Mandatory\n"
            "Signature Augmentation Policy | Optional"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.4.3 (Outputs)",
        "testo": (
            "Il processo di creazione di una Signature with Long-Term Validation Material deve "
            "restituire un'indicazione di stato della convalida della firma fornita, insieme alla firma "
            "creata con materiale di convalida a lungo termine."
        ),
        "testo_integrale": (
            "The process for creating a Signature with Long-Term Validation Material shall return a "
            "status indication of the validation of the signature provided together with the created "
            "signature with Long-Term Validation Material."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.4.4 (Process)",
        "testo": (
            "Quando aggiunge un attributo contenente dati di convalida a lungo termine, il processo di "
            "signature augmentation deve: 1) convalidare la Signature with Time nel suo stato corrente, "
            "usando la convalida definita nella clausola 5.5; 2) aggiungere alla firma tutto il materiale "
            "o/e i riferimenti a esso che è stato usato durante la convalida e che non è già presente "
            "nella firma; 3) restituire la firma aumentata, possibilmente con le informazioni sullo stato "
            "di convalida e il rapporto di convalida forniti dall'SVA. Nota: l'augmentation può essere "
            "significativa anche per firme in cui la convalida restituisce uno stato TOTAL-FAILED, perché "
            "consente di assicurare l'integrità e la disponibilità a lungo termine del materiale che può "
            "provare che la convalida della firma è fallita."
        ),
        "testo_integrale": (
            "When adding an attribute containing long-term-validation data, the signature augmentation "
            "process shall:\n"
            "1) validate the Signature with Time in its current state, using the validation defined in "
            "clause 5.5;\n"
            "2) add to the signature all material or/and references to it that has been used during "
            "validation and that is not already present in the signature; and\n"
            "3) return the augmented signature possibly with the validation status information and the "
            "validation report provided by the SVA.\n"
            "NOTE: Augmentation can be meaningful even for signatures where validation returns a "
            "TOTAL-FAILED status indication, since it allows ensuring the integrity and Long Term "
            "Availability of the material that can prove that the signature validation failed."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.5.1 (Description)",
        "testo": (
            "Prima che gli algoritmi, le chiavi e gli altri dati crittografici usati quando la firma è "
            "stata costruita diventino deboli e le funzioni crittografiche diventino vulnerabili, o che "
            "i certificati che supportano time-assertions precedenti scadano o siano revocati, il "
            "documento del firmatario, la firma e gli attributi contenuti in una firma con materiale di "
            "convalida a lungo termine dovrebbero essere protetti applicando una o più time-assertions. "
            "Le time-assertions legano i dati a un momento particolare, stabilendo la prova che quei dati "
            "esistevano in quel momento; tali time-assertions aggiuntive sono aggiunte alla firma come "
            "attributi non firmati per fornire disponibilità e integrità a lungo termine del materiale di "
            "convalida (attributi per la disponibilità e l'integrità a lungo termine del materiale di "
            "convalida). La creazione di time-assertions dovrebbe essere ripetuta nel tempo, prima che la "
            "protezione fornita da una time-assertion precedente diventi debole, e dovrebbe fare uso di "
            "algoritmi più forti o di lunghezze di chiave maggiori di quelli usati nelle firme originali o "
            "nelle time-assertions precedenti. Se il processo è ripetuto, con una firma possono "
            "verificarsi più istanze di time-assertions: la Figura 10 mostra un esempio di firma a cui "
            "sono state applicate due time-assertions."
        ),
        "testo_integrale": (
            "Before algorithms, keys, and other cryptographic data used at the time a signature was "
            "built become weak and the cryptographic functions become vulnerable, or the certificates "
            "supporting previous time-assertions expire or are revoked, the signer's document, the "
            "signature as well as any attributes contained in a signature with Long-Term Validation "
            "Material should be protected by applying one or more time-assertions. Time-assertions bind "
            "data to a particular time establishing evidence that the latter data existed at that time. "
            "Such additional time-assertions are added to the signature as unsigned attributes in order "
            "to provide long term availability and integrity of validation material and thus are called "
            "attributes for long term availability and integrity of validation material. The creation of "
            "time-assertions should be repeated in time before the protection provided by a previous "
            "time-assertion becomes weak and should make use of stronger algorithms or longer key lengths "
            "than have been used in the original signatures or previous time-assertions.\n"
            "Figure 9: Signature providing Long Term Availability and Integrity of Validation Material\n"
            "If the process is repeated, several instances of time-assertions may occur with a signature. "
            "Figure 10 shows an example of a signature where two time-assertions have been applied.\n"
            "Figure 10: Signature providing Long Term Availability and Integrity of Validation Material "
            "after repetition"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.5.2 (Inputs)",
        "testo": (
            "Input del processo di creazione di una Signature providing Long Term Availability and "
            "Integrity of Validation Material (Tabella 4): Signature with Long-Term Validation Material "
            "oppure Signature providing Long Term Availability and Integrity of Validation Material, "
            "obbligatoria; signature augmentation policy, opzionale."
        ),
        "testo_integrale": (
            "Table 4: Inputs to the creation process for Signatures providing Long Term Availability and "
            "Integrity of Validation Material\n"
            "Input | Requirement\n"
            "Signature with Long-Term Validation Material or Signature providing Long Term Availability "
            "and Integrity of Validation Material | Mandatory\n"
            "Signature Augmentation Policy | Optional"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.5.3 (Outputs)",
        "testo": (
            "Il processo di creazione di una Signature providing Long Term Availability and Integrity of "
            "Validation Material deve, se ha successo, restituire la firma fornita come input, aumentata "
            "con un attributo non firmato aggiunto per la disponibilità e l'integrità a lungo termine del "
            "materiale di convalida, cioè un time-stamp token o un evidence record sulla firma; inoltre "
            "materiale di convalida aggiuntivo può essere stato incluso come attributi non firmati dentro "
            "la firma. Se il processo non è stato eseguito con successo, deve essere restituita "
            "un'indicazione di errore insieme a tutte le informazioni disponibili che spiegano l'errore."
        ),
        "testo_integrale": (
            "The process for creating a Signature providing Long Term Availability and Integrity of "
            "Validation Material shall, if successful, return the signature provided as input, which has "
            "been augmented by an added unsigned attribute for long term availability and integrity of "
            "validation material, i.e. a time-stamp token or an evidence record on the signature. Also, "
            "additional validation material may have been included as unsigned attributes within the "
            "signature.\n"
            "If the process has not been executed successfully, an error indication shall be returned "
            "together with all information available explaining the error."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.3.5.4 (Process)",
        "testo": (
            "Il processo di signature augmentation può: 1) convalidare la firma nel suo stato corrente, "
            "usando il processo di convalida definito nella clausola 5.5; 2) se il processo di convalida "
            "restituisce TOTAL-FAILED, restituire questa indicazione insieme a tutte le informazioni sul "
            "problema fornite dal processo di convalida; 3) aggiungere tutto il materiale di convalida "
            "necessario a convalidare la firma che non è già presente nella firma - ciò deve includere i "
            "dati di convalida delle time-assertions aggiunte in precedenza; 4) richiedere una o più "
            "time-assertions alle TSA appropriate come definite nella signature policy o nella "
            "configurazione locale - la time-assertion deve coprire il documento del firmatario nonché "
            "tutti gli oggetti dati contenuti nella firma; 5) produrre l'attributo o gli attributi di "
            "firma che incapsulano le time-assertions prodotte al passo 4); 6) aggiungere l'attributo o "
            "gli attributi di firma come attributi non firmati alla firma."
        ),
        "testo_integrale": (
            "The signature augmentation process may:\n"
            "1) Validate the signature in its current state, using the validation process defined in "
            "clause 5.5.\n"
            "2) If the validation process returns TOTAL-FAILED, return this indication together with all "
            "information about the problem as provided by the validation process.\n"
            "3) Add any validation material required for validating the signature that is not already "
            "present in the signature. This shall include any validation data of previously added "
            "time-assertions.\n"
            "4) Request one or more time-assertions from appropriate TSAs as defined in the signature "
            "policy or local configuration. The time-assertion shall cover the signer's document as well "
            "as all data objects contained in the signature.\n"
            "5) Produce signature attribute(s) encapsulating the time-assertion(s) produced in step 4). "
            "And\n"
            "6) Add the signature attribute(s) as unsigned attribute(s) to the signature."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 4.2.1 (Introduction)",
        "testo": (
            "La Figura 2 delinea i blocchi costitutivi per la creazione di una firma e illustra il flusso "
            "dei dati del processo di generazione di una firma; le clausole da 4.2.2 a 4.2.11 "
            "specificano gli oggetti informativi usati in questo processo."
        ),
        "testo_integrale": (
            "Figure 2 outlines the building blocks for creating a signature and illustrates the data "
            "flow for the process of the generation of a signature. Clauses 4.2.2 to 4.2.11 specify "
            "information objects used in this process.\n"
            "Figure 2: Information Model of Signature Creation"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.2.3 (Signer's Document (SD))",
        "testo": (
            "Il Signer's Document (SD) è il documento sul quale la firma è generata e al quale è "
            "associata; è selezionato o composto dal firmatario o dalla DA e in alcuni casi, invece "
            "dell'SD completo, ai processi di firma può essere presentata una rappresentazione dell'SD "
            "(Signer's Document Representation, SDR). Nota: l'SD ha potenzialmente una serie di varianti "
            "e componenti importanti che incidono sul processo di firma e sullo stato della firma: 1) può "
            "essere in un formato revisionabile (documento di videoscrittura, messaggio o file "
            "modificabile) la cui presentazione dipende dalla configurazione corrente del dispositivo di "
            "visualizzazione, e in cui al firmatario può essere presentata una rappresentazione dell'SD "
            "di aspetto diverso da quella presentata al verificatore; 2) può essere in una forma non "
            "ambigua (es. txt, Postscript, ODA final form), che contiene regole di presentazione complete "
            "tali da garantire che firmatario e verificatore vedano l'SD allo stesso modo se le stesse "
            "regole di presentazione sono seguite; 3) può essere presente informazione codificata nascosta "
            "(es. macro, testo nascosto, componenti attive o calcolate, virus), invisibile al firmatario "
            "durante l'anteprima e la verifica e di cui il firmatario può non essere consapevole: "
            "potenziali ambiguità dell'SD; 4) può essere in una forma non normalmente presentata "
            "direttamente al firmatario o al verificatore, oppure presentata intrinsecamente in modi "
            "diversi pur rappresentando la stessa semantica (es. formati di Electronic Data Interchange, "
            "pagine web HTML, XML, SGML, file); 5) può essere in una forma che rappresenta più documenti "
            "individuali, referenziati o impacchettati insieme con un qualche formato dati (es. ASIC o "
            "XMLDSig), dove ciascun documento individuale può essere qualunque cosa, da dati casuali a "
            "documenti commerciali."
        ),
        "testo_integrale": (
            "The Signer's Document (SD) is the document upon which the signature is generated and to "
            "which it is associated. The SD is selected or composed by the signer or by the DA. In some "
            "cases, a Signer's Document Representation (SDR) of the SD can be presented to the signature "
            "processes instead of the complete SD.\n"
            "NOTE: The SD potentially has a number of important variants and components that impact the "
            "signing process and the status of the signature:\n"
            "1) It can be in revisable format such as a word processor document or a message or file "
            "that can be edited, and where its presentation is dependent on the current configuration of "
            "the viewing device, and where the signer can potentially be presented a representation of "
            "the SD having an appearance different from that presented to the verifier.\n"
            "2) It can be in an unambiguous form (e.g. txt, Postscript, ODA final form, etc.). These "
            "formats contain complete presentation rules that guarantee that the signer and verifier can "
            "be presented the SD in the same way if the same presentation rules are followed.\n"
            "3) Hidden encoded information can be present (e.g. macros, hidden text, active or "
            "calculated components, viruses, etc.). These can be invisible to the signer during the "
            "preview and verification processes, and the signer can be unaware of their presence. These "
            "represent potential ambiguities in the SD.\n"
            "4) It can be in a form that is not normally presented to the signer or verifier directly, "
            "or it can be in a form that is inherently presented to the signer and verifier in different "
            "ways (whilst representing the same semantics). Examples of these formats are Electronic "
            "Data Interchange formats, Web Pages (HTML), XML, SGML, and computer files.\n"
            "5) It can be in a form representing multiple individual documents, either referenced or "
            "packed together using some data format. Each of these individual documents can be anything, "
            "from random data to business documents. Examples for such forms are ASIC or XMLDSig."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.1 (Introduction)",
        "testo": (
            "La Figura 3 illustra la struttura di una firma comune a tutte le classi di firma definite "
            "in questa clausola: il documento del firmatario e gli attributi firmati, entrambi input del "
            "calcolo del valore di firma, il valore di firma stesso e gli eventuali attributi non firmati "
            "inclusi nella firma. La Figura 4 illustra il ciclo di vita di una firma - la maggior parte "
            "delle firme create attraversa solo alcuni dei passi di tale ciclo di vita - e i passi del "
            "ciclo di vita sono definiti qui come classi di firma con proprietà comuni; il processo di "
            "creazione di un'istanza di una classe di firma a partire da una firma di un'altra classe "
            "lungo quel ciclo di vita è chiamato Signature Augmentation ed è governato da una signature "
            "augmentation policy. Ciascuna delle classi di firma corrisponde a una combinazione "
            "significativa di attributi aggiunti a una firma allo scopo di migliorare la capacità di "
            "convalidare la firma in futuro, quando il certificato corrispondente o altro materiale "
            "necessario a una convalida riuscita può essere scaduto, revocato, o gli algoritmi usati non "
            "più sufficientemente forti da essere affidabili. Le classi: una Basic Signature è una firma "
            "convalidabile finché i certificati corrispondenti non sono né revocati né scaduti; una "
            "Signature with Time è una firma che prova che la firma esisteva già a un dato momento (Nota "
            "1: può essere usata per convalidare una firma quando un certificato è stato revocato dopo la "
            "creazione della firma); una Signature with Long-Term Validation Material è una firma che "
            "fornisce la disponibilità a lungo termine del materiale di convalida incorporando tutto il "
            "materiale, o i riferimenti al materiale, richiesto per convalidare la firma; una Signature "
            "providing Long Term Availability and Integrity of Validation Material mira alla "
            "disponibilità e integrità a lungo termine del materiale di convalida delle firme digitali "
            "sul lungo periodo e può aiutare a convalidare la firma oltre molti eventi che ne limitano la "
            "validità (per esempio la debolezza degli algoritmi crittografici usati, o la scadenza dei "
            "dati di convalida) (Nota 2: le firme possono poi essere ancora convalidate quando i "
            "certificati scadono o vengono revocati, e anche quando la sicurezza degli algoritmi "
            "applicati diventa discutibile o le dimensioni delle chiavi usate non sono più allo stato "
            "dell'arte)."
        ),
        "testo_integrale": (
            "Figure 3 illustrates the structure of a signature common to all classes of signatures "
            "defined in this clause. It consists of the signer's document and signed attributes, both of "
            "which are input to the calculation of the signature value, the signature value itself as "
            "well as any unsigned attributes included into the signature.\n"
            "Figure 3: Digital Signature\n"
            "Figure 4 illustrates the life cycle of a signature. Most signatures created only encounter "
            "some of the steps in the life cycle. The steps in the life cycle are defined here as classes "
            "of signatures that have common properties as specified below. The process of creating an "
            "instance of a signature class based on a signature of another class following that "
            "lifecycle is also called Signature Augmentation and is governed by a signature augmentation "
            "policy.\n"
            "Figure 4: Signature Lifecycle\n"
            "Each of the signature classes below corresponds to a meaningful combination of attributes "
            "added to a signature aiming at improving the ability to validate a signature in the future, "
            "when the corresponding certificate or any other material needed for successful validation "
            "may have expired, been revoked, or used algorithms are no longer strong enough to be "
            "trustworthy.\n"
            "A Basic Signature is a signature that can be validated as long as the corresponding "
            "certificates are neither revoked nor expired.\n"
            "A Signature with Time is a signature that proves that the signature already existed at a "
            "given point in time.\n"
            "NOTE 1: It can be used to validate a signature when a certificate has been revoked after "
            "the signature has been created.\n"
            "A Signature with Long-Term Validation Material is a signature that provides the long term "
            "availability of the validation material by incorporating all the material or references to "
            "material required for validating the signature.\n"
            "A Signature providing Long Term Availability and Integrity of Validation Material targets "
            "long term availability and integrity of the validation material of digital signatures over "
            "long term and can help to validate the signature beyond many events that limit its validity "
            "(for instance, the weakness of used cryptographic algorithms, or expiration of validation "
            "data).\n"
            "NOTE 2: Signatures can then still be validated when certificates expire or become revoked, "
            "and also when the security of applied algorithms becomes questionable or used key sizes are "
            "no longer state of the art."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.2.1 (Description)",
        "testo": (
            "La Figura 5 mostra i passi coinvolti nella creazione di una Basic Signature; le clausole da "
            "4.3.2.4.1 a 4.3.2.4.7 specificano tali passi."
        ),
        "testo_integrale": (
            "Figure 5 shows the steps involved in creation of a Basic Signature. Clauses 4.3.2.4.1 to "
            "4.3.2.4.7 specify these steps.\n"
            "Figure 5: Basic Signature Creation"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.3.1 (Description)",
        "testo": (
            "Una Signature with Time è una firma che prova che la firma esisteva già a un dato momento. "
            "L'ora è fornita da un time-stamp token sulla firma, come proprietà non firmata aggiunta "
            "alla Basic Signature a seguito della signature augmentation (Figura 7). Nota 1: un time-mark "
            "fornito da un Trusted Service avrebbe effetto simile alla marca temporale, ma in quel caso "
            "nessuna proprietà è aggiunta alla firma, essendo responsabilità del TSP fornire evidenza di "
            "un time mark quando richiesto; la gestione dei time mark è fuori dal perimetro del "
            "documento. Nota 2: il time-stamp token fornisce i passi iniziali verso la validità a lungo "
            "termine - i time-stamp token devono essere creati prima che un certificato sia stato revocato "
            "o sia scaduto; se ciò non può essere ottenuto, la convalida della firma creata può fallire. "
            "Nota 3: la Signature with Time fornisce evidenza indipendente dell'esistenza della firma "
            "prima dell'indicazione del time-stamp token; per ridurre il rischio di ripudio della "
            "creazione della firma, il time-stamp token è idealmente il più vicino possibile al momento "
            "in cui la firma è stata creata - la Signature with Time può essere fornita dal firmatario o "
            "da un TSP; se non l'ha fornita il firmatario o la TSA usata dal firmatario non è fidata dal "
            "verificatore, il verificatore può creare una Signature with Time alla prima ricezione di una "
            "firma."
        ),
        "testo_integrale": (
            "A Signature with Time is a signature that proves that the signature already existed at a "
            "given point in time. The time is provided by a time-stamp token on the signature as an "
            "unsigned property added to the Basic Signature as a result of the signature augmentation.\n"
            "Figure 7: Signature with Time\n"
            "NOTE 1: A time-mark provided by a Trusted Service would have similar effect to the "
            "time-stamp but in this case no property is added to the signature as it is the "
            "responsibility of the TSP to provide evidence of a time mark when required to do so. The "
            "management of time marks is outside the scope of the present document.\n"
            "NOTE 2: Time-stamp token provides the initial steps towards providing long term validity. "
            "The time-stamp tokens need to be created before a certificate has been revoked or expired. "
            "If this cannot be achieved, validation of the created signature can fail.\n"
            "NOTE 3: The Signature with Time provides independent evidence of the existence of the "
            "signature prior to the time-stamp token indication. To reduce the risk of repudiating "
            "signature creation, the time-stamp token ideally is as close as possible to the time the "
            "signature was created. The signer or a TSP could provide the Signature with Time. If the "
            "signer did not provide it or the TSA the signer used is not trusted by the verifier, the "
            "verifier can create a Signature with Time on first receipt of a signature."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.4.1 (Description)",
        "testo": (
            "Finché un algoritmo di convalida può valutare la validità di una Signature with Time, questa "
            "può essere aumentata (augmented) a una Signature with Long-Term Validation Material "
            "aggiungendo attributi non firmati; questa augmentation può essere fatta dalla SCA, oppure da "
            "una terza parte, oppure da un verificatore che usa un SVA (Figura 8). Nota 1: un algoritmo "
            "di convalida della firma può valutare la validità di una Signature with Time solo finché i "
            "dati di convalida necessari a convalidare la firma sono ancora disponibili on-line ai "
            "verificatori e i POE della firma sono disponibili; quando non è certo che i dati di "
            "convalida necessari resteranno disponibili on-line ai verificatori, o che alcuni "
            "verificatori non possano accedere a quei dati, è necessario catturare quei dati dentro la "
            "firma. Nota 2: una Signature with Long-Term Validation Material include i dati di convalida "
            "necessari a verificare la firma oltre la fine della validità del certificato di firma, in "
            "particolare per accertare lo stato di revoca di tutti i certificati end-entity contenuti "
            "nella firma (certificato di firma, certificati delle unità di marcatura temporale, attribute "
            "certificate, ecc.); possono esserci più elementi del necessario e anche meno elementi del "
            "necessario se si prevede che i destinatari abbiano un mezzo alternativo per ottenere gli "
            "elementi mancanti."
        ),
        "testo_integrale": (
            "As long as a validation algorithm can assess the validity of a Signature with Time, it can "
            "be augmented to a Signature with Long-Term Validation Material by adding unsigned "
            "attributes. This augmentation can be done either by the SCA, or by a third party or by a "
            "verifier using an SVA.\n"
            "NOTE 1: A signature validation algorithm can assess the validity of a Signature with Time "
            "only as long as the validation data required to validate the signature is still on-line "
            "available to the verifiers and signature POE are available. In case it is unsure that the "
            "validation data required to validate the signature will still be on-line available to the "
            "verifiers or that some verifiers cannot access that data, then it is necessary to capture "
            "that data inside the signature.\n"
            "Figure 8: Signature with Long-Term Validation Material\n"
            "NOTE 2: A Signature with Long-Term Validation Material includes the validation data that is "
            "necessary to verify the signature beyond the end of the validity of the signing "
            "certificate, in particular to ascertain the revocation status of all end-entity "
            "certificates (signing certificate, time-stamping units certificates, attribute "
            "certificates, etc.) contained in the signature. There can be more elements than necessary "
            "and can also be fewer elements than necessary if it is expected that recipients have an "
            "alternate means of obtaining the missing elements."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 4.1 (Signature creation model)",
    "clausola 4.2.1 (Introduction)",
    "clausola 4.2.2 (Signature Creation Constraints)",
    "clausola 4.2.3 (Signer's Document (SD))",
    "clausola 4.2.4 (Signer's Document Representation (SDR))",
    "clausola 4.2.5.1 (General requirements)",
    "clausola 4.2.5.2 (Signing certificate identifier)",
    "clausola 4.2.5.3 (Signature policy identifier)",
    "clausola 4.2.5.4 (Signature policy store)",
    "clausola 4.2.5.5 (Data content type)",
    "clausola 4.2.5.6 (Commitment type indication)",
    "clausola 4.2.5.7 (Counter signatures)",
    "clausola 4.2.5.8 (Claimed signing time)",
    "clausola 4.2.5.9 (Claimed signer location)",
    "clausola 4.2.5.10 (Signer's attributes)",
    "clausola 4.2.6 (Data To Be Signed (DTBS))",
    "clausola 4.2.7 (Data To Be Signed (Formatted) (DTBSF))",
    "clausola 4.2.8 (Data To Be Signed Representation (DTBSR))",
    "clausola 4.2.9 (Signature)",
    "clausola 4.2.10 (Signed Data Object (SDO))",
    "clausola 4.2.11 (Validation data)",
    "clausola 4.3.1 (Introduction)",
    "clausola 4.3.2.1 (Description)",
    "clausola 4.3.2.2 (Inputs)",
    "clausola 4.3.2.3 (Outputs)",
    "clausola 4.3.2.4.1 (Selection of documents to sign)",
    "clausola 4.3.2.4.2 (Signature attribute and parameters selection)",
    "clausola 4.3.2.4.3 (Pre-signature presentation)",
    "clausola 4.3.2.4.4 (Signature invocation)",
    "clausola 4.3.2.4.5 (Signing)",
    "clausola 4.3.2.4.6 (Signer authentication)",
    "clausola 4.3.2.4.7 (SDO composition)",
    "clausola 4.3.3.1 (Description)",
    "clausola 4.3.3.2 (Inputs)",
    "clausola 4.3.3.3 (Outputs)",
    "clausola 4.3.3.4 (Process)",
    "clausola 4.3.4.1 (Description)",
    "clausola 4.3.4.2 (Inputs)",
    "clausola 4.3.4.3 (Outputs)",
    "clausola 4.3.4.4 (Process)",
    "clausola 4.3.5.1 (Description)",
    "clausola 4.3.5.2 (Inputs)",
    "clausola 4.3.5.3 (Outputs)",
    "clausola 4.3.5.4 (Process)",
]

MAPPATURA_LOCALE = {
    "clausola 4.1 (Signature creation model)": ["clausola 4.1 (Signature creation model)"],
    "clausola 4.2.1 (Introduction)": ["clausola 4.2.1 (Introduction)"],
    "clausola 4.2.2 (Signature Creation Constraints)": [
        "clausola 4.2.2 (Signature Creation Constraints)"
    ],
    "clausola 4.2.3 (Signer's Document (SD))": ["clausola 4.2.3 (Signer's Document (SD))"],
    "clausola 4.2.4 (Signer's Document Representation (SDR))": [
        "clausola 4.2.4 (Signer's Document Representation (SDR))"
    ],
    "clausola 4.2.5.1 (General requirements)": ["clausola 4.2.5.1 (General requirements)"],
    "clausola 4.2.5.2 (Signing certificate identifier)": [
        "clausola 4.2.5.2 (Signing certificate identifier)"
    ],
    "clausola 4.2.5.3 (Signature policy identifier)": [
        "clausola 4.2.5.3 (Signature policy identifier)"
    ],
    "clausola 4.2.5.4 (Signature policy store)": ["clausola 4.2.5.4 (Signature policy store)"],
    "clausola 4.2.5.5 (Data content type)": ["clausola 4.2.5.5 (Data content type)"],
    "clausola 4.2.5.6 (Commitment type indication)": [
        "clausola 4.2.5.6 (Commitment type indication)"
    ],
    "clausola 4.2.5.7 (Counter signatures)": ["clausola 4.2.5.7 (Counter signatures)"],
    "clausola 4.2.5.8 (Claimed signing time)": ["clausola 4.2.5.8 (Claimed signing time)"],
    "clausola 4.2.5.9 (Claimed signer location)": ["clausola 4.2.5.9 (Claimed signer location)"],
    "clausola 4.2.5.10 (Signer's attributes)": ["clausola 4.2.5.10 (Signer's attributes)"],
    "clausola 4.2.6 (Data To Be Signed (DTBS))": ["clausola 4.2.6 (Data To Be Signed (DTBS))"],
    "clausola 4.2.7 (Data To Be Signed (Formatted) (DTBSF))": [
        "clausola 4.2.7 (Data To Be Signed (Formatted) (DTBSF))"
    ],
    "clausola 4.2.8 (Data To Be Signed Representation (DTBSR))": [
        "clausola 4.2.8 (Data To Be Signed Representation (DTBSR))"
    ],
    "clausola 4.2.9 (Signature)": ["clausola 4.2.9 (Signature)"],
    "clausola 4.2.10 (Signed Data Object (SDO))": ["clausola 4.2.10 (Signed Data Object (SDO))"],
    "clausola 4.2.11 (Validation data)": ["clausola 4.2.11 (Validation data)"],
    "clausola 4.3.1 (Introduction)": ["clausola 4.3.1 (Introduction)"],
    "clausola 4.3.2.1 (Description)": ["clausola 4.3.2.1 (Description)"],
    "clausola 4.3.2.2 (Inputs)": ["clausola 4.3.2.2 (Inputs)"],
    "clausola 4.3.2.3 (Outputs)": ["clausola 4.3.2.3 (Outputs)"],
    "clausola 4.3.2.4.1 (Selection of documents to sign)": [
        "clausola 4.3.2.4.1 (Selection of documents to sign)"
    ],
    "clausola 4.3.2.4.2 (Signature attribute and parameters selection)": [
        "clausola 4.3.2.4.2 (Signature attribute and parameters selection)"
    ],
    "clausola 4.3.2.4.3 (Pre-signature presentation)": [
        "clausola 4.3.2.4.3 (Pre-signature presentation)"
    ],
    "clausola 4.3.2.4.4 (Signature invocation)": ["clausola 4.3.2.4.4 (Signature invocation)"],
    "clausola 4.3.2.4.5 (Signing)": ["clausola 4.3.2.4.5 (Signing)"],
    "clausola 4.3.2.4.6 (Signer authentication)": ["clausola 4.3.2.4.6 (Signer authentication)"],
    "clausola 4.3.2.4.7 (SDO composition)": ["clausola 4.3.2.4.7 (SDO composition)"],
    "clausola 4.3.3.1 (Description)": ["clausola 4.3.3.1 (Description)"],
    "clausola 4.3.3.2 (Inputs)": ["clausola 4.3.3.2 (Inputs)"],
    "clausola 4.3.3.3 (Outputs)": ["clausola 4.3.3.3 (Outputs)"],
    "clausola 4.3.3.4 (Process)": ["clausola 4.3.3.4 (Process)"],
    "clausola 4.3.4.1 (Description)": ["clausola 4.3.4.1 (Description)"],
    "clausola 4.3.4.2 (Inputs)": ["clausola 4.3.4.2 (Inputs)"],
    "clausola 4.3.4.3 (Outputs)": ["clausola 4.3.4.3 (Outputs)"],
    "clausola 4.3.4.4 (Process)": ["clausola 4.3.4.4 (Process)"],
    "clausola 4.3.5.1 (Description)": ["clausola 4.3.5.1 (Description)"],
    "clausola 4.3.5.2 (Inputs)": ["clausola 4.3.5.2 (Inputs)"],
    "clausola 4.3.5.3 (Outputs)": ["clausola 4.3.5.3 (Outputs)"],
    "clausola 4.3.5.4 (Process)": ["clausola 4.3.5.4 (Process)"],
}

RELAZIONI = []
