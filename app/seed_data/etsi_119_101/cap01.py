"""ETSI TS 119 101 V1.1.1 (2016-03) - Electronic Signatures and
Infrastructures (ESI); Policy and security requirements for applications for
signature creation and signature validation.

Fonte: requisiti di politica e sicurezza per le APPLICAZIONI di creazione,
convalida e augmentation della firma (il software con cui l'utente firma,
verifica e mantiene valida la firma), non per il prestatore di servizi
fiduciari. Capitolo 1: clausola 1 (Scope), clausola 3 (Definitions and
abbreviations: 3.1 Definitions, 3.2 Abbreviations), clausola 4 (Signature
creation/validation/augmentation model).

Testo ufficiale in app/.source_cache/etsi_119_101/cap01.txt (md5
d699d2275914087d068fe0aa5ce0d7b4), estratto dal PDF con pdftotext -layout.
Manifest di split: app/.source_cache/etsi_119_101/manifest.json. La
numerazione degli id e' risolta per riferimento dalla sessione principale in
app/seed.py: questo modulo non tocca seed.py.

Copertura (ADR-0007), criterio applicato voce per voce:

- Clausola 1 (Scope) -> 1 Principio "scopo/ambito di applicazione",
  riferimento "clausola 1 (Scope)". La clausola e' integralmente
  dichiarativa (perimetro, destinatari primari, elenco di cio' che il
  documento copre, rinvio fuori perimetro a CEN EN 419 111, ETSI EN 319 401,
  ETSI TS 119 431, CEN EN 419 241, ETSI TS 119 441): nessun verbo
  prescrittivo con destinatario obbligato, quindi nessun Obbligo.
- Clausola 2 (References: 2.1 Normative references, 2.2 Informative
  references) -> NESSUN nodo e NESSUN item di indice: bibliografia/
  paratesto puro (elenco [i.1]-[i.27] piu' le NOTE redazionali ETSI sui
  riferimenti specifici/non specifici e sulla validita' a lungo termine
  degli hyperlink). Stesso trattamento riservato alla clausola 2 delle altre
  fonti ETSI gia' censite.
- Clausola 3 (Definitions and abbreviations) -> la clausola 3 e' una pura
  intestazione di raggruppamento (solo titolo, tutto il contenuto vive in
  3.1 e 3.2): non genera nodo proprio, i due nodi sono 3.1 e 3.2.
- Clausola 3.1 (Definitions) -> 1 Principio "definitorio" riassuntivo, NON
  un nodo per singolo termine: la clausola e' un glossario piatto senza
  struttura a lettere/numeri propria (31 definizioni in ordine alfabetico
  dopo la formula introduttiva ufficiale), quindi 31 nodi sarebbero 31 item
  di indice fittizi per un'unica clausola numerata. In `testo_integrale`
  sono riportate tutte le 31 definizioni verbatim, con le NOTE e gli EXAMPLE
  ufficiali (signature augmentation application: NOTE 1 e NOTE 2; signature
  class: NOTE 1, NOTE 2 ed EXAMPLE con le classi di firma; signature level:
  EXAMPLE con CAdES-B-B, CAdES-E-EPES, XAdES-B-LTA, XAdES-E-C, PAdES-B-T,
  PAdES-E-LTV; signature validation application: NOTE). Le definizioni per
  rinvio ("As defined in Regulation (EU) No 910/2014" per advanced
  electronic seal e advanced electronic signature) restano verbatim come nel
  testo ufficiale, senza sostituirle con il contenuto della fonte esterna.
  I singoli termini sono comunque indicizzati separatamente dal full-text
  su `testo_integrale`.
- Clausola 3.2 (Abbreviations) -> 1 Principio "definitorio" riassuntivo con
  le 25 abbreviazioni della clausola (CA, CRL, DA, DN, DTBS, DTBSR, EC,
  ICS, ISMS, OCSP, OTP, PIN, PUK, PW, SAA, SAPS, SCA, SCD, SCDev, SD, SDO,
  SSI, SVA, ToC, XML). L'estrazione pdftotext -layout tiene etichetta e
  forma estesa sulla stessa riga in colonne: le coppie sono ricostruite in
  forma esplicita "ETICHETTA: Forma estesa." in `testo_integrale`, senza
  perdere alcun valore (stessa convenzione gia' usata per la clausola 3.3 di
  ETSI TS 119 432 e di ETSI EN 319 422).
- Clausola 4 (Signature creation/validation/augmentation model) -> 1
  Principio "altro". La clausola non ha sottoclavole numerate proprie (il
  modello e' descritto in prosa piu' tre figures) e non enuncia alcun
  requisito operativo: afferma che alcuni obiettivi possono essere
  implementati indifferentemente dalla DA o dalla SCA/SVA/SAA per lasciare
  flessibilita' implementativa e che un sistema completo soddisfa tutti gli
  obiettivi obbligatori (clausola 5.3) indipendentemente da dove sono
  implementati: e' dichiarazione di modello, non prescrizione con
  destinatario individuabile, quindi nessun Obbligo.

Scelte di modellazione non ovvie:

- Il dump testuale dei riquadri delle figures 1-3 (blocchi etichettati
  "Driving application (DA)", "Signature creation system", "Signature
  creation application (SCA)", "User interface", "SCDev/SCA interface
  (SSI)", "Signature creation device (SCDev)", "Network", "Local storage",
  "Operating system and other application processes" e analoghi per
  convalida e augmentation) NON e' riportato in `testo_integrale`: e' il
  contenuto di diagrammi immagine, ricostruito da pdftotext con layout
  disallineato su colonne, non testo normativo in prosa. Restano nel
  verbatim i titoli di ambiente ("Signature creation environment",
  "Signature validation environment", "Signature augmentation
  environment"), le didascalie "Figure 1"/"Figure 2"/"Figure 3", le NOTE e
  l'EXAMPLE ufficiali. Le etichette dei riquadri sono comunque conservate
  nella sintesi italiana (`testo`), che elenca i building block del modello.
  Stessa scelta gia' adottata per la clausola 4 di ETSI TS 119 612 e per la
  clausola 4.4 di ETSI TS 119 431-1.
- I due rinvii della clausola 4 ("see clause 5.3" e "see ETSI TS 119 102
  [i.8]") non generano relazioni: la clausola 5.3 e' coperta dal cap02 di
  questa stessa fonte (scritto da un altro subagent, fuori dal perimetro di
  questo modulo) e il collegamento cross-fonte e' demandato alla sessione
  principale (ADR-0009).
- Questo capitolo non contiene alcun Obbligo: 0 Obblighi, 4 Principi. Non
  esiste una categoria di soggetto per "implementatore/fornitore di
  applicazioni di firma" e la clausola 1 non impone comunque nulla a
  costoro: classificarla come Obbligo avrebbe richiesto un destinatario
  inesistente nell'elenco ammesso.

Item di indice coperti da questo capitolo (4): "clausola 1 (Scope)",
"clausola 3.1 (Definitions)", "clausola 3.2 (Abbreviations)", "clausola 4
(Signature creation/validation/augmentation model)".
"""

RIGHE_OBBLIGHI: list[dict] = []

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 1 (Scope)",
        "testo": (
            "Il documento fornisce requisiti generali di sicurezza e di politica per le applicazioni di "
            "creazione, convalida e augmentation della firma. Destinatari primari: gli implementatori e i "
            "fornitori di applicazioni di creazione/convalida/augmentation della firma, che devono garantire la "
            "copertura dei requisiti pertinenti, e gli attori che integrano componenti di "
            "creazione/convalida/augmentation della firma con software di processo aziendale (o usano software "
            "standalone), che vogliono assicurare il corretto funzionamento dell'intero processo di "
            "creazione/convalida/augmentation e che la creazione o convalida avvenga in un ambiente "
            "sufficientemente sicuro. Il documento si applica a questi attori e ai loro valutatori "
            "(autovalutazione o valutazione di terza parte) come lista di criteri con cui verificare "
            "l'implementazione. I requisiti coprono l'implementazione e la fornitura dei moduli Signature "
            "Creation/Validation/Augmentation Application (SCA/SVA/SAA), la driving application (DA), la "
            "comunicazione tra SCA e dispositivo di creazione della firma (SCDev) e l'ambiente in cui SCA/SVA/SAA "
            "sono usati, oltre a requisiti di interfaccia utente (l'interfaccia utente puo' far parte della "
            "SCA/SVA/SAA o della DA che la richiama; qualsiasi entita' che usa componenti SCA/SVA/SAA nel proprio "
            "processo di business agisce come driving application). Il documento copre: requisiti di politica "
            "legale, requisiti di sicurezza delle informazioni (sistema di gestione), requisiti dei processi di "
            "creazione, convalida e augmentation della firma, requisiti di politica di sviluppo e codifica, "
            "requisiti generali. Fuori perimetro: i Protection Profiles per applicazioni di creazione e convalida "
            "della firma (standard CEN EN 419 111); i requisiti generali per i prestatori di servizi fiduciari "
            "(ETSI EN 319 401) e i requisiti per i prestatori che forniscono servizi di creazione o convalida "
            "della firma, demandati a ETSI TS 119 431 (con CEN EN 419 241 per il dispositivo remoto di creazione "
            "della firma) e a ETSI TS 119 441."
            ),
        "testo_integrale": (
            "1 Scope\nThe present document provides general security and policy requirements for applications for "
            "signature creation,\nvalidation and augmentation.\n\nThe present document is primarily relevant to "
            "the following actors:\n\n    •    Implementers and providers of applications for signature creation, "
            "signature validation and/or signature\n         augmentation, who need to ensure that relevant "
            "requirements are covered.\n\n    •    Actors that integrate applications for signature creation, "
            "signature validation and/or signature augmentation\n         components with business process "
            "software (or use standalone software), who want to ensure proper\n         functioning of the "
            "overall signature creation/validation/augmentation process and that the signature\n         "
            "creation/validation is done in a sufficiently secure environment.\n\nThe present document is "
            "applicable to these actors, and their evaluators (for a self-evaluation or an evaluation by a "
            "third\nparty) to have a list of criteria against which to check the implementation.\n\nThe "
            "requirements cover applications for signature creation, signature validation and/or signature "
            "augmentation, i.e. the\nimplementation and provision of the Signature "
            "Creation/Validation/Augmentation Application modules\n(SCA/SVA/SAA), the driving application (DA), "
            "the communication between the SCA and the signature creation device\n(SCDev) and the environment in "
            "which the SCA/SVA/SAA is used. It also specifies user interface requirements, while\nthe user "
            "interface can be part of the SCA/SVA/SAA or of the DA which calls the SCA/SVA/SAA. Any entity "
            "using\nSCA/SVA/SAA components in its business process acts as driving application.\n\nThe document "
            "covers:\n\n    •    Legal driven policy requirements.\n\n    •    Information security (management "
            "system) requirements.\n\n    •    Signature creation, signature validation and signature "
            "augmentation processes requirements.\n\n    •    Development and coding policy requirements.\n\n    "
            "•    General requirements.\n\nProtection Profiles (PP) for signature creation applications and "
            "signature validation applications are out of scope and are\ndefined in the CEN standard \"Protection "
            "Profiles for Signature Creation & Validation Applications\" [i.9].\n\nGeneral requirements for trust "
            "service providers are provided in ETSI EN 319 401 [i.24]. Requirements for trust service\nproviders "
            "providing signature creation or validation services are out of scope. Requirements on trust service "
            "providers\nproviding signature creation services are to be defined in ETSI TS 119 431 [i.22], with "
            "CEN EN 419 241 [i.21] defining\nrequirements for a remote signature creation device. Requirements on "
            "trust service providers providing signature\nvalidation services are to be defined in ETSI TS 119 "
            "441 [i.23]."
            ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.1 (Definitions)",
        "testo": (
            "La clausola definisce i termini specifici del documento, oltre a quelli gia' dati in ETSI TR 119 "
            "001: 31 definizioni. 'advanced electronic seal' e 'advanced electronic signature': come da "
            "Regolamento (UE) n. 910/2014. 'certificate': chiave pubblica di un'entita' insieme ad altre "
            "informazioni, resa non falsificabile mediante firma digitale con la chiave privata dell'autorita' di "
            "certificazione che l'ha emessa. 'certificate validation': processo di verifica e conferma che un "
            "certificato e' valido. 'data to be signed formatted': dati creati dagli oggetti data to be signed "
            "formattandoli e collocandoli nella sequenza corretta per il calcolo della data to be signed "
            "representation. 'data to be signed representation': hash dei dati formattati da firmare, usato per "
            "calcolare il valore di firma digitale. 'digital signature': dati aggiunti a un'unita' di dati, o "
            "trasformazione crittografica di essa, che consente a un destinatario di provarne origine e "
            "integrita' e protegge da contraffazione anche da parte del destinatario stesso. 'digital signature "
            "value': risultato di quella trasformazione crittografica. 'driving application': applicazione che "
            "usa un sistema di creazione della firma per creare una firma, un'applicazione di convalida per "
            "convalidare firme digitali o un'applicazione di augmentation per aumentare firme digitali. 'personal "
            "data': qualsiasi informazione relativa a una persona fisica identificata o identificabile "
            "(l'interessato). 'signature application practice statement': insieme di regole applicabili "
            "all'applicazione e/o al suo ambiente che implementa creazione, augmentation e/o convalida di firme "
            "digitali. 'signature augmentation': processo di incorporamento in una firma digitale di informazioni "
            "volte a mantenerne la validita' a lungo termine. 'signature augmentation application': applicazione "
            "che implementa l'augmentation della firma, prende input e fornisce la firma aumentata a una driving "
            "application, e puo' essere realizzata come parte della SCA, come parte della SVA o come applicazione "
            "a se' stante. 'signature augmentation policy': insieme di regole applicabili a una o piu' firme "
            "digitali che definisce i requisiti tecnici e procedurali per la loro augmentation per soddisfare una "
            "particolare esigenza di business e al ricorrere delle quali le firme possono essere determinate "
            "conformi. 'signature class': insieme di firme che realizzano una data funzionalita', descritte in "
            "ETSI TS 119 102-1, indipendenti dall'implementazione (esempi: firma con marca temporale, firma con "
            "materiale di validazione a lungo termine, firma che fornisce disponibilita' e integrita' a lungo "
            "termine del materiale di validazione). 'signature creation application': applicazione interna al "
            "sistema di creazione della firma, complementare al dispositivo di creazione, che crea un oggetto di "
            "dati firmato. 'signature creation data': dati univoci, come codici o chiavi crittografiche private, "
            "usati dal firmatario per creare un valore di firma digitale. 'signature creation device': software o "
            "hardware configurato usato per implementare i dati di creazione della firma e creare un valore di "
            "firma digitale. 'signature creation system': sistema complessivo, costituito dall'applicazione e dal "
            "dispositivo di creazione della firma, che crea una firma digitale. 'signature level': definizione "
            "specifica per formato di un insieme di dati incorporati in una firma digitale che consente di "
            "implementare una classe di firma (esempi: CAdES-B-B, CAdES-E-EPES, XAdES-B-LTA, XAdES-E-C, "
            "PAdES-B-T, PAdES-E-LTV). 'signature policy': politica di creazione, di augmentation o di convalida "
            "della firma o loro combinazione, applicabile alla stessa firma o insieme di firme. 'signature "
            "validation': processo di verifica e conferma che una firma e' valida. 'signature validation "
            "application': applicazione che implementa la convalida della firma, prende input e fornisce i "
            "risultati di convalida a una driving application. 'signature verification': processo di controllo "
            "del valore crittografico di una firma mediante i dati di verifica della firma. 'signature "
            "verification data': dati, come codici o chiavi crittografiche pubbliche, usati per verificare una "
            "firma. 'signed data object': struttura dati contenente il valore della firma, gli attributi di firma "
            "e altre informazioni. 'signer': entita' creatrice di una firma digitale. 'time-stamping authority': "
            "prestatore di servizi fiduciari che emette marche temporali usando una o piu' unita' di marcatura "
            "temporale. 'trust service': servizio elettronico che accresce fiducia e affidabilita' nelle "
            "transazioni elettroniche. 'trust service provider': persona fisica o giuridica che fornisce uno o "
            "piu' servizi fiduciari. 'trusted path': connessione che fornisce integrita', autenticita' e "
            "riservatezza dei dati trasmessi."
            ),
        "testo_integrale": (
            "3.1 Definitions\nFor the purposes of the present document, the terms and definitions given in ETSI "
            "TR 119 001 [i.7] and the following\napply:\n\n    NOTE:     For the sake of readability, the "
            "following definitions are reproduced here below.\n\nadvanced electronic seal: As defined in "
            "Regulation (EU) No 910/2014 [i.1].\n\nadvanced electronic signature: As defined in Regulation (EU) "
            "No 910/2014 [i.1].\n\ncertificate: public key of an entity, together with some other information, "
            "rendered unforgeable by digital signature\nwith the private key of the certification authority which "
            "issued it\n\ncertificate validation: process of verifying and confirming that a certificate is "
            "valid\n\ndata to be signed formatted: data created from the data to be signed objects by formatting "
            "them and placing them in\nthe correct sequence for the computation of the data to be signed "
            "representation\n\ndata to be signed representation: hash of the data to be signed formatted, which "
            "is used to compute the digital\nsignature value\n\ndigital signature: data appended to, or a "
            "cryptographic transformation of a data unit that allows a recipient of the data\nunit to prove the "
            "source and integrity of the data unit and protect against forgery e.g. by the recipient.\n\ndigital "
            "signature value: result of the cryptographic transformation of a data unit that allows a recipient "
            "of the data unit\nto prove the source and integrity of the data unit and protect against forgery "
            "e.g. by the recipient\n\ndriving application: application that uses a signature creation system to "
            "create a signature or a signature validation\napplication in order to validate digital signatures or "
            "a signature augmentation application to augment digital signatures\n\npersonal data: any information "
            "relating to an identified or identifiable natural person ('data subject')\n\nsignature application "
            "practice statement: set of rules applicable to the application and/or its environment\nimplementing "
            "the creation, the augmentation and/or the validation of digital signatures\n\nsignature "
            "augmentation: process of incorporating to a digital signature information aiming to maintain the "
            "validity of\nthat signature over the long term\n\nsignature augmentation application: application "
            "that implements signature augmentation\n\n   NOTE 1: The signature augmentation application takes "
            "inputs from and provides the augmented signature to a\n           driving application.\n\n   NOTE 2: "
            "The signature augmentation application can be implemented as part of the signature creation "
            "application\n           or as part of the signature validation application or as a stand-alone "
            "application.\n\nsignature augmentation policy: set of rules, applicable to one or more digital "
            "signatures, that defines the technical and\nprocedural requirements for their augmentation, in order "
            "to meet a particular business need, and under which the digital\nsignature(s) can be determined to "
            "be conformant\n\nsignature class: set of signatures achieving a given functionality\n\n   NOTE 1: "
            "ETSI TS 119 102-1 [i.8] describes different signature classes.\n\n   NOTE 2: A signature class is "
            "implementation independent.\n\n   EXAMPLE:           Signature with time, signature with long term "
            "validation material, Signature providing Long Term\n                      Availability and Integrity "
            "of Validation Material are possible signature classes.\n\nsignature creation application: "
            "application within the signature creation system, complementing the signature creation\ndevice, that "
            "creates a signature data object\n\nsignature creation data: unique data, such as codes or private "
            "cryptographic keys, which are used by the signer to\ncreate a digital signature value\n\nsignature "
            "creation device: configured software or hardware used to implement the signature creation data and "
            "to create\na digital signature value\n\nsignature creation system: overall system, consisting of the "
            "signature creation application and the signature creation\ndevice, that creates a digital "
            "signature\n\nsignature level: format specific definition of a set of data incorporated into a "
            "digital signature, which allows to\nimplement a signature class\n\n   EXAMPLE:           CAdES-B-B, "
            "CAdES-E-EPES [i.15] and [i.16], XAdES-B-LTA, XAdES-E-C [i.17] and [i.18],\n                      "
            "PAdES-B-T, PAdES-E-LTV [i.19] and [i.20] are examples of signature levels.\n\nsignature policy: "
            "signature creation policy, a signature augmentation policy, a signature validation policy or "
            "any\ncombination thereof, applicable to the same signature or set of signatures\n\nsignature "
            "validation: process of verifying and confirming that a signature is valid\n\nsignature validation "
            "application: application that implements signature validation\n\n   NOTE:      The signature "
            "validation application takes inputs from and provides validation results to a driving\n              "
            "application.\n\nsignature verification: process of checking the cryptographic value of a signature "
            "using signature verification data\n\nsignature verification data: data, such as codes or public "
            "cryptographic keys, used for the purpose of verifying a\nsignature\n\nsigned data object: data "
            "structure containing the signature value, signature attributes and other information\n\nsigner: "
            "entity being the creator of a digital signature\n\ntime-stamping authority: trust service provider "
            "which issues time-stamps using one or more time-stamping units\n\ntrust service: electronic service "
            "which enhances trust and confidence in electronic transactions\n\ntrust service provider: natural or "
            "a legal person who provides one or more trust services\n\ntrusted path: connection that provides "
            "integrity, authenticity and confidentiality of the data transmitted"
            ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.2 (Abbreviations)",
        "testo": (
            "La clausola elenca le 25 abbreviazioni usate nel documento, oltre a quelle gia' date in ETSI TR 119 "
            "001: CA = Certification Authority; CRL = Certificate Revocation List; DA = Driving Application; DN = "
            "Distinguished Name; DTBS = Data to be Signed; DTBSR = Data To Be Signed Representation; EC = "
            "European Commission; ICS = Implementation Conformance Statement; ISMS = Controls (Information "
            "Security Management System); OCSP = Online Certificate Status Provider; OTP = One Time Password; PIN "
            "= Personal Identification Number; PUK = Personal Unblocking Key; PW = Password; SAA = Signature "
            "Augmentation Application; SAPS = Signature Application Practice Statement; SCA = Signature Creation "
            "Application; SCD = Signature Creation Data; SCDev = Signature Creation Device; SD = Signer's "
            "Document; SDO = Signed Data Object; SSI = SCDev/SCA interface; SVA = Signature Validation "
            "Application; ToC = Table of Content; XML = eXtensible Markup Language."
            ),
        "testo_integrale": (
            "3.2 Abbreviations\nFor the purposes of the present document, the abbreviations given in ETSI TR 119 "
            "001 [i.7] and the following apply:\n\nCA: Certification Authority\nCRL: Certificate Revocation "
            "List\nDA: Driving Application\nDN: Distinguished Name\nDTBS: Data to be Signed\nDTBSR: Data To Be "
            "Signed Representation\nEC: European Commission\nICS: Implementation Conformance Statement\nISMS: "
            "Controls (Information Security Management System)\nOCSP: Online Certificate Status Provider\nOTP: "
            "One Time Password\nPIN: Personal Identification Number\nPUK: Personal Unblocking Key\nPW: "
            "Password\nSAA: Signature Augmentation Application\nSAPS: Signature Application Practice "
            "Statement\nSCA: Signature Creation Application\nSCD: Signature Creation Data\nSCDev: Signature "
            "Creation Device\nSD: Signer's Document\nSDO: Signed Data Object\nSSI: SCDev/SCA interface\nSVA: "
            "Signature Validation Application\nToC: Table of Content\nXML: eXtensible Markup Language"
            ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4 (Signature creation/validation/augmentation model)",
        "testo": (
            "I sistemi hardware/software per creare, convalidare o aumentare una firma sono modellati attraverso "
            "building block come mostrato nelle figure 1-3. Il modello della creazione comprende: driving "
            "application (DA); sistema di creazione della firma, formato dall'applicazione di creazione (SCA) con "
            "l'interfaccia utente e dall'interfaccia SCDev/SCA (SSI) verso il dispositivo di creazione della "
            "firma (SCDev); e i blocchi d'ambiente rete, storage locale, sistema operativo e altri processi "
            "applicativi. Il modello della convalida sostituisce l'applicazione di convalida (SVA) alla "
            "SCA/SCDev, quello dell'augmentation l'applicazione di augmentation (SAA). Alcuni obiettivi possono "
            "essere implementati dalla DA oppure dalla SVA/SCA/SAA, per lasciare flessibilita' implementativa, ma "
            "un sistema completo soddisfa tutti gli obiettivi obbligatori (clausola 5.3) indipendentemente da "
            "dove sono implementati; la distinzione tra SCA/SVA/SAA e DA serve a semplificare la definizione dei "
            "requisiti e nelle implementazioni concrete puo' non essere fatta (una SCA non necessita di "
            "interfaccia utente, ad esempio quando la creazione della firma e' erogata come servizio remoto, e in "
            "tal caso l'interazione utente, come la selezione della politica di creazione della firma, e' "
            "implementata dalla DA). Nel caso della creazione, la SCA prepara il documento da firmare e crea "
            "l'oggetto di dati firmato dal valore di firma digitale ricevuto dallo SCDev; il valore di firma "
            "digitale e' creato con i dati di creazione della firma dell'utente; la SCA comunica con lo SCDev "
            "tramite la SSI; la DA fornisce l'input alla SCA e ne riceve l'output; l'interfaccia utente puo' "
            "essere (in parte) della DA e/o (in parte) della SCA. Nel caso della convalida la DA fornisce l'input "
            "alla SVA e ne riceve l'output. Nel caso dell'augmentation la DA fornisce l'input alla SAA e riceve "
            "la firma aumentata. L'ambiente di creazione, convalida o augmentation copre l'ambiente in cui DA e "
            "SCA/SCDev, DA e SVA, oppure DA e SAA sono usati, e contiene rete, storage dei dati e il sistema "
            "informativo. In ETSI TS 119 102-1 l'augmentation della firma e' parte della SCA, poiche' aggiunge "
            "informazione alla firma: qui e' trattata separatamente per coprire meglio gli obiettivi di controllo "
            "specifici e per riflettere il fatto che la SAA puo' essere parte della SCA, della SVA o "
            "un'applicazione a se' stante. Per maggiori dettagli sul modello generale di creazione e convalida "
            "della firma si rinvia a ETSI TS 119 102."
            ),
        "testo_integrale": (
            "4 Signature creation/validation/augmentation model\nThe hardware/software systems for creating, "
            "validating or augmenting a signature, are modelled through several\nbuilding blocks as shown in "
            "figures 1 to 3.\n\nSome objectives can be implemented either by the DA or the SVA/SCA/SAA. This is "
            "to allow a flexibility in the\nimplementation. However, a complete system meets all mandatory "
            "objectives (see clause 5.3) independent of where\nimplemented.\n\n    NOTE 1: The distinction "
            "between the SCA/SVA/SAA and DA is done to simplify the definition of requirements. In\n            "
            "concrete implementations, this distinction may not be made.\n\n    EXAMPLE:         A SCA does not "
            "necessarily have a user interface, e.g. when signature creation is provided as a\n                   "
            "remote service. In this case user interaction, like selection of a signature creation policy, is\n   "
            "implemented by the DA.\n\nSignature creation environment\n\nNOTE:     This model is based on ETSI TS "
            "119 102 [i.8] and differs slightly from the model used in CEN\n          EN 419 111 [i.9]. It allows "
            "the user to communicate with the Driving Application and with the SCA. It also\n          uses "
            "signature creation system to group together the SCA and the SCDev.\n\n               Figure 1: Basic "
            "model of an example signature creation environment\n\nIn case of a signature creation, the signature "
            "creation application (SCA) prepares the document to be signed and creates\nthe signed data object "
            "from the digital signature value received from the signature creation device (SCDev). The "
            "digital\nsignature value is created using the signature creation data of the user. The SCA "
            "communicates with the SCDev using\nthe SSI. The driving application provides the input to the "
            "signature creation application and receives the output. The\nuser interface can be (partly) part of "
            "the DA and/or (partly) part of the SCA. The signature creation environment covers\nthe environment "
            "in which the DA, the SCA and the SCDev are used. It contains network, data storage and "
            "the\ninformation system.\n\n   Signature validation environment\n\n   NOTE:      This model is based "
            "on ETSI TS 119 102 [i.8] and differs slightly from the model used in CEN\n              EN 419 111 "
            "[i.9]. It allows the user to communicate with the Driving Application and with the SCA.\n\n          "
            "Figure 2: Basic model of an example signature validation environment\n\nIn the case of a signature "
            "validation, the DA provides the input for the SVA and receives the output. Again, the "
            "user\ninterface can be part of the DA and/or part of the SVA. The signature validation environment "
            "covers the environment in\nwhich the DA and the SVA are used. It contains network, data storage and "
            "the information system.\n\n    Signature augmentation environment\n\n                Figure 3: Basic "
            "model of an example signature augmentation environment\n\n    NOTE 2: In ETSI TS 119 102-1 [i.8], "
            "the signature augmentation is part of the SCA, since it adds information to\n            the "
            "signature. In the present document it is handled separately to better cover the specific control\n   "
            "objectives and to reflect the fact that the SAA can be part of the SCA, the SVA or can be a "
            "stand-alone\n            application.\n\nIn the case of a signature augmentation, the DA provides "
            "the input for the SAA and receives the augmented signature.\nAgain, the user interface can be part "
            "of the DA and/or part of the SAA. The signature augmentation environment covers\nthe environment in "
            "which the DA and the SAA are used. It contains network, data storage and the information "
            "system.\n\nFor more details on the general model for signature creation and validation, see ETSI TS "
            "119 102 [i.8]."
            ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 1 (Scope)",
    "clausola 3.1 (Definitions)",
    "clausola 3.2 (Abbreviations)",
    "clausola 4 (Signature creation/validation/augmentation model)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Nessun rinvio letterale interno a questo capitolo trasformato in relazione: i due
# riferimenti della clausola 4 (clausola 5.3, ETSI TS 119 102) hanno il proprio nodo in
# un altro capitolo di questa fonte o in un'altra fonte. Il collegamento cross-fonte e'
# demandato alla sessione principale (ADR-0009).
RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_completezza_testo_integrale, verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    verifica_completezza_testo_integrale([sys.modules[__name__]])
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
