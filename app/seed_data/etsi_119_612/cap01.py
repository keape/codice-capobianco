"""ETSI TS 119 612 V2.4.1 (2025-08) - Electronic Signatures and Trust
Infrastructures (ESI); Trusted Lists.
Fonte 21 (la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 1:
clausola 1 (Scope), clausola 3 (Definition of terms, symbols and
abbreviations: 3.1 Terms, 3.2 Symbols, 3.3 Abbreviations), clausola 4
(Overall structure of trusted lists). Testo ufficiale in
app/.source_cache/etsi_119_612/cap01.txt (letto sempre con selettore `:raw`,
altrimenti il tool tronca le righe lunghe a 768 caratteri introducendo "..."
e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_119_612/manifest.json (md5 di cap01.txt:
b8328fcc9474334a3a4aa5cad9c23694).

Modellazione (ADR-0007), stesso criterio gia' applicato alle altre fonti
ETSI gia' censite (ETSI EN 319 401, ETSI EN 319 412, ETSI EN 319 421, ETSI TS
119 432) e adattato alle clausole/sottoclausole di uno standard tecnico: un
nodo per ogni clausola/sottoclasse numerata che porta contenuto proprio; per
le clausole di cornice un solo nodo dedicato. La clausola 1 dichiara il
perimetro, la clausola 3 e' un apparato terminologico (glossario, simboli,
abbreviazioni), la clausola 4 e' la descrizione d'insieme della struttura
della TL: nessuna delle tre enuncia un requisito operativo numerato (i
requisiti del documento vivono nelle clausole 5, 6 e negli annessi).
Questo capitolo non contiene alcun Obbligo: 0 Obblighi, 5 Principi. Scelte
voce per voce:

- Clausola 1 (Scope) -> 1 Principio "scopo/ambito di applicazione",
  riferimento "clausola 1 (Scope)". Riporta i quattro paragrafi ufficiali:
  (i) il documento specifica formato e meccanismi per istituire, localizzare,
  accedere e autenticare una trusted list che rende disponibili informazioni
  sullo stato dei servizi fiduciari, definisce formato e semantica della TL
  e i meccanismi di accesso, e fornisce guida per localizzarle e
  autenticarle; (ii) si applica alle TL degli Stati membri UE come mezzo per
  esprimere lo stato dei servizi fiduciari rispetto al Regolamento (UE) n.
  910/2014 [i.10] e alla sua legislazione secondaria; (iii) in contesti non
  UE o di organizzazioni internazionali gli scheme operator POSSONO emettere
  TL conformi al documento per facilitare il mutuo riconoscimento delle
  firme digitali; (iv) il documento definisce inoltre requisiti per le
  relying party che usano le TL e le informazioni di stato in esse
  contenute. Nessun verbo prescrittivo con soggetto obbligato ("may" al
  punto iii e' facolta' di contesto non UE, non requisito): e' dichiarazione
  di perimetro. La clausola non contiene NOTE ufficiali.
- Clausola 2 (References: 2.1 Normative references, 2.2 Informative
  references) -> NESSUN nodo, NESSUN item di indice, come da perimetro del
  brief: bibliografia/paratesto puro (elenco [1]-[17] normativo e
  [i.1]-[i.13] informativo, piu' le NOTE redazionali ETSI sui riferimenti
  specifici/non specifici e sulla validita' a lungo termine degli
  hyperlink), nessun contenuto normativo autonomo. Stesso trattamento gia'
  riservato alla clausola 2 di ETSI EN 319 401/319 421/319 422.
- Clausola 3.1 (Terms) -> 1 Principio "definitorio" riassuntivo, NON un nodo
  per singolo termine: la clausola e' un glossario piatto senza struttura a
  lettere/numeri propria (38 termini in ordine alfabetico), quindi 38 nodi
  sarebbero 38 item di indice fittizi per un'unica clausola. In
  `testo_integrale` sono riportate TUTTE le 38 definizioni verbatim,
  precedute dalla formula introduttiva ufficiale ("For the purposes of the
  present document, the following terms apply:"), incluse tutte le NOTE
  ufficiali (certification authority: NOTE 1 sui due casi di CA e NOTE 2 sul
  rinvio a ISO/IEC 9594-8 [i.12] e ITU-T X.509 [1]; conformity assessment:
  NOTE sulla provenienza da Reg. (EC) 765/2008 [i.4] e clausola 2.1 di
  ISO/IEC 17000 [i.8]; trust service: NOTE sull'uso tipico ma non necessario
  di tecniche crittografiche; trust service token: NOTE con esempi di token
  binari e fisici; trusted list: NOTE sul contesto UE e sul contesto non UE).
  Parecchie definizioni sono definizioni per rinvio ("As defined in
  Regulation (EU) No 910/2014 [i.10]" o "As defined in Directive 1999/93/EC
  [i.3]"): riportate verbatim come nel testo ufficiale, senza sostituirle
  con il contenuto della fonte esterna.
- Clausola 3.2 (Symbols) -> 1 Principio "definitorio" con il testo ufficiale
  integrale, che e' il solo segnaposto di redazione "Void." (il documento
  non definisce alcun simbolo). Il nodo e' mantenuto per copertura completa
  della clausola numerata (ADR-0007): e' la stessa scelta adottata per la
  clausola 3.2 di ETSI TS 119 432, mentre per ETSI 119 431-1 un "Void." puro
  era stato escluso - qui si segue l'indicazione del task di capitolo.
- Clausola 3.3 (Abbreviations) -> 1 Principio "definitorio" riassuntivo. La
  clausola elenca le 63 abbreviazioni usate nel documento, precedute dalla
  formula introduttiva ufficiale ("For the purposes of the present document,
  the following abbreviations apply:"). L'estrazione pdftotext -layout
  conserva l'etichetta e la forma estesa su una stessa riga ma con
  allineamento a colonne: le coppie sono ricostruite in forma esplicita
  "ETICHETTA: Forma estesa." in `testo_integrale` (stessa convenzione della
  clausola 3.3 di ETSI TS 119 432 e di ETSI EN 319 422), senza perdere alcun
  valore. Le due NOTE ufficiali della clausola (EL: codice ISO 3166-1 [15]
  Alpha 2 per la Grecia; UK: codice ISO 3166-1 [15] Alpha 2 per la
  Gran Bretagna) sono riportate in coda alla rispettiva abbreviazione.
- Clausola 4 (Overall structure of trusted lists) -> 1 Principio "altro",
  riferimento "clausola 4 (Overall structure of trusted lists)". La clausola
  descrive la struttura logica della TL: i TLSO che mantengono una TL
  conforme al documento devono rispettare il formato e la semantica della TL
  (clausola 5) e i meccanismi per localizzare, accedere e autenticare le TL
  (clausola 6); i sei componenti logici (1 tag, 2 scheme information, 3 TSP
  information, 4 service information, 5 service approval history, 6 digital
  signature) con la regola che i componenti 1., 2. e 6. hanno una sola
  occorrenza mentre gli altri sono replicabili. Il testo contiene la frase
  prescrittiva "shall comply with" ma il suo contenuto e' interamente
  ricognitivo/strutturale (rinvia in blocco a clausole 5 e 6, dove i
  requisiti sono censiti come Obblighi nei rispettivi capitoli): il nodo e'
  quindi modellato come Principio "altro" secondo l'indicazione del task di
  capitolo, senza duplicare come Obbligo il rinvio strutturale. In
  `testo_integrale` sono riportati integralmente i punti 1)-6), le due
  chiusure ("The number of TSPs, of services per TSP, and of history
  sections per service is unbounded." e "The structure of the TL is further
  described in the following clauses by each component part and its
  fields.") e il rimando testuale alla figure 1. NON e' riportato il dump
  testuale dei riquadri della figure 1 ("Tag TSL tag (clause 5.2.1) ...
  Figure 1: Logical model of the trusted list"): e' il contenuto di un
  diagramma immagine - ricostruito da pdftotext con layout disallineato -
  non testo normativo, e il suo contenuto prescrittivo/descrittivo e' gia'
  tutto nei punti 1)-6) e nelle clausole 5.2-5.7.

RELAZIONI: 1 sola, interna alla Fonte e con riscontro testuale puntuale. La
clausola 4 punto 1) cita esplicitamente "The contents of the tag are
specified in clause 5.2.1": relazione `richiama` dal nodo di clausola 4 al
nodo "clausola 5.2.1 (TSL Tag)" del capitolo 2 (stringa confermata dal
subagent Etsi612Cap02, che ne detiene la scrittura). Non sono state create
relazioni per gli altri rinvii della clausola 4 ("as specified in clause 5",
"clause 6", "specified in clause 5.3", "5.4", "5.5", "5.6", "5.7"): sono
intestazioni di puro raggruppamento che non portano testo proprio e quindi
non generano alcun nodo nel censimento (confermato dai subagent dei capitoli
2/3: 5, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7 senza nodo), e una relazione verso un
riferimento inesistente farebbe fallire con KeyError il merge dell'intero
seed (app/seed_data/lib.py:inserisci_capitoli). Anche il dump dei riquadri
della figure 1 (che elenca 5.3.1-5.3.18, 5.4.1-5.4.6, 5.5.1-5.5.10,
5.6.1-5.6.6, 5.7.2, 5.7.3) non e' stato trasformato in relazioni: e'
contenuto di diagramma, non rinvio testuale in prosa, ed era escluso dal
`testo_integrale` per le ragioni sopra.

Citazioni esterne notate ma NON trasformate in relazioni (vietato in questa
fase, ADR-0009: il cross-collegamento e' una fase successiva della sessione
principale): Regolamento (UE) n. 910/2014 [i.10] e legislazione secondaria
(clausola 1, definizioni 3.1); Regolamento (CE) n. 765/2008 [i.4], ISO/IEC
17000 [i.8], ISO/IEC 9594-8 [i.12], ITU-T X.509 [1], Direttiva 1999/93/EC
[i.3], ETSI EN 319 132-1 [3], ISO 3166-1 [15] (NOTE di 3.1 e 3.3).

Self-check: `python3 app/seed_data/etsi_119_612/cap01.py` (o il venv
app/.venv/bin/python) stampa "OK: 0 obblighi, 5 principi, 5 item di indice
coperti.".
"""

RIGHE_OBBLIGHI: list[dict] = []

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 1 (Scope)",
        "testo": (
            "Il documento specifica un formato e dei meccanismi per istituire, localizzare, accedere e "
            "autenticare una trusted list che rende disponibili informazioni sullo stato dei servizi "
            "fiduciari, cosi' che le parti interessate possano determinare in un dato momento lo stato di un "
            "servizio fiduciario elencato; definisce il formato e la semantica della TL nonche' i meccanismi "
            "di accesso alle TL e fornisce guida per localizzarle e autenticarle. Si applica alle trusted "
            "list degli Stati membri dell'Unione Europea come mezzo per esprimere lo stato dei servizi "
            "fiduciari rispetto alle disposizioni del Regolamento (UE) n. 910/2014 e della sua legislazione "
            "secondaria applicabile. In contesti di Paesi non UE o organizzazioni internazionali gli scheme "
            "operator possono emettere trusted list conformi al documento per facilitare il mutuo "
            "riconoscimento delle firme digitali. Il documento definisce inoltre requisiti per le relying "
            "party che usano le TL e le informazioni di stato in esse contenute."
        ),
        "testo_integrale": (
            "1 Scope: The present document specifies a format and mechanisms for establishing, locating, "
            "accessing and authenticating a trusted list which makes available trust service status "
            "information so that interested parties may determine the status of a listed trust service at a "
            "given time. It defines the format and semantics of a TL as well as the mechanisms for accessing "
            "TLs. It also provides guidance for locating and authenticating TLs. The present document applies "
            "to European Union Member State (EU MS) trusted lists as a means to express trust service status "
            "information with regards to their compliance with the relevant provisions laid down in "
            "Regulation (EU) No 910/2014 [i.10] and in its applicable secondary legislation. In the context "
            "of non-EU countries or international organizations, scheme operators may issue trusted lists in "
            "accordance with the present document to facilitate mutual recognition of digital signatures. In "
            "addition, the present document defines requirements for relying parties to use TLs and the "
            "status information held within them."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.1 (Terms)",
        "testo": (
            "La clausola definisce 38 termini specifici del documento, preceduti dalla formula ufficiale di "
            "glossario. Molte definizioni sono definite per rinvio al Regolamento (UE) n. 910/2014 "
            "('advanced electronic seal', 'advanced electronic signature', 'electronic archiving', "
            "'electronic attestation of attributes', 'electronic ledger', 'electronic seal', 'electronic "
            "signature', '(EU) qualified certificate', 'qualified electronic archiving service', 'qualified "
            "electronic attestation of attributes', 'qualified electronic ledger', 'qualified electronic "
            "seal', 'qualified electronic signature', 'qualified electronic signature/seal creation device', "
            "'remote qualified electronic seal creation device', 'remote qualified electronic signature "
            "creation device', 'seal creator', 'signatory') o alla Direttiva 1999/93/EC "
            "('certification-service-provider', 'advanced electronic signature under e-signature Directive', "
            "'qualified certificate under e-signature Directive', 'secure signature creation device') o a "
            "ETSI EN 319 132-1 per 'XML Advanced Electronic Signature (XAdES)'. Le definizioni proprie del "
            "documento riguardano il governo degli schemi di approvazione ('approval', 'approval scheme', "
            "'scheme operator', 'supervision system', '(voluntary) accreditation'), la terminologia "
            "certificatoria ('certification authority', 'conformity assessment', 'digital signature', "
            "'signer' con il correlato 'signatory', 'remote electronic seal creation devices', 'remote "
            "electronic signature creation devices') e il perimetro dei servizi fiduciari e delle liste "
            "('trust service', 'trust service provider', 'trust service token', 'trusted list'). Sono "
            "incluse le NOTE ufficiali su certification authority, conformity assessment, trust service, "
            "trust service token e trusted list."
        ),
        "testo_integrale": (
            "3.1 Terms: For the purposes of the present document, the following terms apply: advanced "
            "electronic seal: As defined in Regulation (EU) No 910/2014 [i.10]. advanced electronic "
            "signature: As defined in Regulation (EU) No 910/2014 [i.10]. advanced electronic signature "
            "under e-signature Directive: Advanced electronic signature as defined in Directive 1999/93/EC "
            "[i.3]. approval: assertion that a trust service, falling within the oversight of a particular "
            "scheme, has been either positively endorsed or assessed for compliance against the relevant "
            "requirements (active approval) or has received no explicit restriction since the time at which "
            "the scheme was aware of the existence of the said service (passive approval) approval scheme: "
            "any organized process of supervision, monitoring, assessment or such practices that are "
            "intended to apply oversight with the objective of ensuring adherence to specific criteria in "
            "order to maintain trust in the services under the scope of the scheme certification authority: "
            "authority trusted by one or more users to create and assign certificates NOTE 1: A "
            "certification authority can be: 1) a trust service provider that creates and assigns public key "
            "certificates; or 2) a technical certificate generation service that is used by a "
            "certification-service-provider that creates and assign public key certificates. NOTE 2: See "
            "ISO/IEC 9594-8 [i.12] and Recommendation ITU-T X.509 [1]. certification-service-provider: As "
            "defined in Directive 1999/93/EC [i.3]. conformity assessment: process demonstrating whether "
            "specified requirements relating to a product, process, service, system, person or body have "
            "been fulfilled NOTE: From Regulation (EC) No 765/2008 [i.4] and clause 2.1 of ISO/IEC 17000 "
            "[i.8]. digital signature: data appended to, or a cryptographic transformation (see "
            "cryptography) of a data unit that allows a recipient of the data unit to prove the source and "
            "integrity of the data unit and protect against forgery e.g. by the recipient electronic "
            "archiving: As defined in Regulation (EU) No 910/2014 [i.10]. electronic attestation of "
            "attributes: As defined in Regulation (EU) No 910/2014 [i.10]. electronic ledger: As defined in "
            "Regulation (EU) No 910/2014 [i.10]. electronic seal: As defined in Regulation (EU) No 910/2014 "
            "[i.10]. electronic signature: As defined in Regulation (EU) No 910/2014 [i.10]. (EU) qualified "
            "certificate: Qualified certificate as specified in Regulation (EU) No 910/2014 [i.10]. "
            "qualified certificate under e-signature Directive: public key certificate which meets the "
            "requirements laid down in Directive 1999/93/EC [i.3] annex I, and is provided by a "
            "certification-service-provider who fulfils the requirements laid down in its annex II qualified "
            "electronic archiving service: As defined in Regulation (EU) No 910/2014 [i.10]. qualified "
            "electronic attestation of attributes: As defined in Regulation (EU) No 910/2014 [i.10]. "
            "qualified electronic ledger: As defined in Regulation (EU) No 910/2014 [i.10]. qualified "
            "electronic seal: As defined in Regulation (EU) No 910/2014 [i.10]. qualified electronic "
            "signature: As defined in Regulation (EU) No 910/2014 [i.10]. qualified electronic "
            "signature/seal creation device: As defined in Regulation (EU) No 910/2014 [i.10]. remote "
            "electronic seal creation devices: configured software or hardware used to create an electronic "
            "seal and that is managed by a trust service provider remote electronic signature creation "
            "devices: configured software or hardware used to create an electronic signature and that is "
            "managed by a trust service provider remote qualified electronic seal creation device: As "
            "defined in Regulation (EU) No 910/2014 [i.10]. remote qualified electronic signature creation "
            "device: As defined in Regulation (EU) No 910/2014 [i.10]. scheme operator: body responsible for "
            "the operation and/or management of any kind of assessment scheme, whether they are "
            "governmental, industry or private, etc. seal creator: As defined in Regulation (EU) No "
            "910/2014 [i.10]. secure signature creation device: Signature creation device, as defined in "
            "Article 2.5 of Directive 1999/93/EC [i.3], which meets the requirements laid down in annex III "
            "of [i.3]. signatory: As defined in Regulation (EU) No 910/2014 [i.10]. signer: entity being the "
            "creator of a signature supervision system: system that allows for the supervision of trust "
            "service providers and the services they provide, for compliance with relevant requirements "
            "trust service: electronic service which enhances trust and confidence in electronic "
            "transactions NOTE: Such trust services are typically but not necessarily using cryptographic "
            "techniques or involving confidential material. trust service provider: entity which provides "
            "one or more electronic trust services trust service token: physical or binary (logical) object "
            "generated or issued as a result of the use of a trust service NOTE: Examples of binary trust "
            "service tokens are: certificates, CRLs, time-stamp tokens, OCSP responses. Physical tokens can "
            "be devices on which binary objects (tokens or credentials) are stored. Equally, a token can be "
            "the performance of an act and the generation of an electronic record, e.g. an insurance policy "
            "or share certificate. trusted list: list that provides information about the status and the "
            "status history of the trust services from trust service providers regarding compliance with the "
            "applicable requirements and the relevant provisions of the applicable legislation NOTE: In the "
            "context of European Union Member States, as specified in Regulation (EU) No 910/2014 [i.10], it "
            "refers to a EU Member State list including information related to the qualified trust service "
            "providers for which it is responsible, together with information related to the qualified trust "
            "services provided by them. In the context of non-EU countries or international organizations, "
            "it refers to a list meeting the requirements of the present document and providing assessment "
            "scheme based approval status information about trust services from trust service providers, for "
            "compliance with the relevant provisions of the applicable approval scheme and the relevant "
            "legislation. (voluntary) accreditation: any permission, setting out rights and obligations "
            "specific to the provision of trust services, to be granted upon request by the trust service "
            "provider concerned, by the public or private body charged with the elaboration of, and "
            "supervision of compliance with, such rights and obligations, where the trust service provider "
            "is not entitled to exercise the rights stemming from the permission until it has received the "
            "decision by the body XML Advanced Electronic Signature (XAdES): As defined in ETSI EN 319 "
            "132-1 [3]."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.2 (Symbols)",
        "testo": (
            "La clausola dichiara che il documento non definisce alcun simbolo: il suo testo ufficiale e' "
            "integralmente 'Void.'."
        ),
        "testo_integrale": "3.2 Symbols: Void.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.3 (Abbreviations)",
        "testo": (
            "La clausola elenca 63 abbreviazioni usate nel documento: ACA (Attribute Certification "
            "Authority), AP (Asia Pacific), ARL (Authority Revocation List), BMP (Basic Multilingual "
            "Plane), CA (Certification Authority), CC (Country Code), CP (Certificate Policy), CPS "
            "(Certification Practices Statement), CR (Carriage Return), CRL (Certificate Revocation List), "
            "DN (Distinguished Name), EC (European Commission), ECDSA (Elliptic Curve Digital Signature "
            "Algorithm), EDS (Electronic Delivery Service), EEA (European Economic Area), EL (Ellada, "
            "Grecia), EU (European Union), EUMS (European Union Member States), FTP (File Transfer "
            "Protocol), GCC (Gulf Cooperation Council), GTC (General Terms & Conditions), HTML (HyperText "
            "Markup Language), HTTP (HyperText Transfer Protocol), ISO (International Organization for "
            "Standardization), LDAP (Lightweight Directory Access Protocol), LF (Line Feed), LOTL (List Of "
            "Trusted Lists), MS (Member State), OCSP (Online Certificate Status Protocol), OID (Object "
            "IDentifier), OJEU (Official Journal of the European Union), PIN (Personal Identification "
            "Number), PKC (Public Key Certificate), PKI (Public Key Infrastructure), PSES (Preservation "
            "Service for Electronic Signatures), QC (Qualified Certificate), QCP (Qualified Certificate "
            "Policy), QSCD (Qualified Signature/Seal Creation Device), RA (Registration Authority), REM "
            "(Registered Electronic Mail), RGS (Referentiel General de Securite), RTF (Rich Text Format), "
            "SGML (Standard Generalized Markup Language), SHA (Secure Hash Algorithm), SSCD (Secure "
            "Signature Creation Device), TAB (TABulator), TC (Technical Committee), TDP (TL Distribution "
            "Point), TL (Trusted List), TLSO (Trusted List Scheme Operator), TSA (Time-Stamping Authority), "
            "TSL (Trust-service Status List), TSP (Trust Service Provider), TST (Time-Stamp Token), TSU "
            "(Time Stamping Unit), UCS (Universal Character Set), UK (United Kingdom), URI (Uniform "
            "Resource Identifier), UTC (Coordinated Universal Time), UTF (Unicode Transformation Format), "
            "WWW (World Wide Web), XHTML (eXtended HTML), XML (eXtensible Markup Language). Le NOTE "
            "ufficiali precisano che EL e UK sono codici ISO 3166-1 Alpha 2 rispettivamente per la Grecia e "
            "per la Gran Bretagna."
        ),
        "testo_integrale": (
            "3.3 Abbreviations: For the purposes of the present document, the following abbreviations "
            "apply: ACA: Attribute Certification Authority. AP: Asia Pacific. ARL: Authority Revocation "
            "List. BMP: Basic Multilingual Plane. CA: Certification Authority. CC: Country Code. CP: "
            "Certificate Policy. CPS: Certification Practices Statement. CR: Carriage Return. CRL: "
            "Certificate Revocation List. DN: Distinguished Name. EC: European Commission. ECDSA: Elliptic "
            "Curve Digital Signature Algorithm. EDS: Electronic Delivery Service. EEA: European Economic "
            "Area. EL: Elláda (Greece). NOTE: ISO 3166-1 [15] Alpha 2 country code for Greece. EU: European "
            "Union. EUMS: European Union Member States. FTP: File Transfer Protocol. GCC: Gulf Cooperation "
            "Council. GTC: General Terms & Conditions. HTML: HyperText Markup Language. HTTP: HyperText "
            "Transfer Protocol. ISO: International Organization for Standardization. LDAP: Lightweight "
            "Directory Access Protocol. LF: Line Feed. LOTL: List Of Trusted Lists. MS: Member State. OCSP: "
            "Online Certificate Status Protocol. OID: Object IDentifier. OJEU: Official Journal of the "
            "European Union. PIN: Personal Identification Number. PKC: Public Key Certificate. PKI: Public "
            "Key Infrastructure. PSES: Preservation Service for Electronic Signatures. QC: Qualified "
            "Certificate. QCP: Qualified Certificate Policy. QSCD: Qualified Signature/Seal Creation "
            "Device. RA: Registration Authority. REM: Registered Electronic Mail. RGS: Référentiel Général "
            "de Sécurité. RTF: Rich Text Format. SGML: Standard Generalized Markup Language. SHA: Secure "
            "Hash Algorithm. SSCD: Secure Signature Creation Device. TAB: TABulator. TC: Technical "
            "Committee. TDP: TL Distribution Point. TL: Trusted List. TLSO: Trusted List Scheme Operator. "
            "TSA: Time-Stamping Authority. TSL: Trust-service Status List. TSP: Trust Service Provider. "
            "TST: Time-Stamp Token. TSU: Time Stamping Unit. UCS: Universal Character Set. UK: United "
            "Kingdom. NOTE: ISO 3166-1 [15] Alpha 2 country code for Great-Britain. URI: Uniform Resource "
            "Identifier. UTC: Coordinated Universal Time. UTF: Unicode Transformation Format. WWW: World "
            "Wide Web. XHTML: eXtended HTML. XML: eXtensible Markup Language."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4 (Overall structure of trusted lists)",
        "testo": (
            "La clausola descrive la struttura logica della trusted list. I Trusted List Scheme Operator "
            "(TLSO) che mantengono una TL conforme al documento devono rispettare: il formato e la semantica "
            "della TL, come specificato nella clausola 5; i meccanismi da usare per consentire alle relying "
            "party di localizzare, accedere e autenticare le TL, come specificato nella clausola 6. La TL ha "
            "sei componenti logici: 1) un trusted list tag (Tag), che ne facilita l'identificazione durante "
            "le ricerche elettroniche, il cui contenuto e' specificato nella clausola 5.2.1; 2) le "
            "informazioni sulla trusted list e sullo scheme che la emette (Scheme information), "
            "specificate nella clausola 5.3 e comprendenti l'identificatore di versione del formato, il "
            "numero di sequenza (o release), il tipo di TL, le informazioni sullo scheme operator e sul "
            "contatto del soggetto che istituisce, pubblica in modo sicuro e mantiene la TL, le "
            "informazioni sullo/gli scheme di approvazione sottostante (inclusi il Paese di applicazione, "
            "il luogo in cui reperire le informazioni sullo scheme, il periodo di conservazione delle "
            "informazioni storiche), la policy e/o l'avviso legale con responsabilita', la data e ora di "
            "emissione e il prossimo aggiornamento previsto; 3) le informazioni identificative non ambigue "
            "su ogni TSP riconosciuto nello scheme (TSP information, clausola 5.4), con la ragione sociale "
            "del TSP usata nelle registrazioni legali formali, l'indirizzo e i contatti e informazioni "
            "aggiuntive incluse direttamente o per riferimento; 4) per ciascun TSP elencato, i dettagli dei "
            "suoi specifici servizi fiduciari il cui stato corrente e' registrato nella TL (Service "
            "information, clausola 5.5), con identificatore del tipo di servizio, nome (commerciale) del "
            "servizio, identificatore univoco del servizio, identificatore dello stato corrente, data e ora "
            "di inizio dello stato corrente e informazioni aggiuntive sul servizio; 5) per ciascun servizio "
            "elencato, le informazioni sullo storico degli stati ove applicabile (Service approval history, "
            "clausola 5.6); 6) una firma digitale (Digital signature, clausola 5.7), la TL essendo una "
            "lista firmata digitalmente a fini di autenticazione. Si prevede una sola occorrenza dei "
            "componenti 1., 2. e 6., mentre gli altri possono essere replicati come illustrato nella figure "
            "1; il numero di TSP, di servizi per TSP e di sezioni di storico per servizio non e' limitato."
        ),
        "testo_integrale": (
            "4 Overall structure of trusted lists: Trusted List Scheme Operators (TLSOs) which maintain a "
            "TL in compliance with the present document shall comply with: - the format and semantics of a "
            "TL, as specified in clause 5; - the mechanisms to be used to support relying parties locating, "
            "accessing and authenticating TLs, as specified in clause 6. The logical model of the trusted "
            "list is shown in figure 1. It has the following logical component parts. There shall be only "
            "one occurrence of the first two and last components (i.e. 1., 2. and 6.). The other components "
            "may be replicated as illustrated in figure 1: 1) A trusted list tag (Tag): This tag facilitates "
            "the identification of the trusted list during electronic searches. The contents of the tag are "
            "specified in clause 5.2.1. 2) Information on the trusted list and its issuing scheme (Scheme "
            "information): The list commences with key information about the list itself and the nature of "
            "the scheme which has determined the information found in, and through, the list. This TL and "
            "scheme information is specified in clause 5.3 and it includes: - A trusted list format version "
            "identifier. - A trusted list sequence (or release) number. - A trusted list type information. - "
            "A trusted list scheme operator information (e.g. name, address, contact information of the body "
            "in charge of establishing, publishing securely and maintaining the trusted list). - Information "
            "about the underlying approval scheme(s) to which the trusted list is associated, including but "
            "not limited to: - the country in which it applies; - information on or reference to the "
            "location where information on the approval scheme(s) can be found (scheme model, rules, "
            "criteria, applicable community, type, etc.); - period of retention of (historical) information. "
            "- Trusted list policy and/or legal notice, liabilities, responsibilities. - Trusted list issue "
            "date and time and next planned update. 3) Unambiguous identification information about every "
            "TSP recognized in the scheme (TSP information): It is a sequence of fields holding unambiguous "
            "identification information about every listed TSP under the scheme. The contents of the TSP "
            "information fields are specified in clause 5.4 and include: - The TSP organization name as used "
            "in formal legal registrations. - The TSP address and contact information. - Additional "
            "information on the TSP either included directly or by reference to a location from where such "
            "information can be downloaded. 4) For each of the listed TSPs, the details of their specific "
            "trust services (Service information) whose current status is recorded within the TL are "
            "provided as a sequence of fields holding unambiguous identification of a listed trust service "
            "provided by the TSP. The contents of the service information field are specified in clause 5.5 "
            "and it includes the following for each trust service from a listed TSP: - An identifier of the "
            "type of service. - (Trade) name of this service. - An unambiguous unique identifier of the "
            "service. - An identifier of the current status of the service. - The current status starting "
            "date and time. - Additional information on the service (directly included or included by "
            "reference to a location from which information can be downloaded): service definition "
            "information provided by the scheme operator, access information with regards to the service, "
            "service definition information provided by the TSP and service information extensions. 5) "
            "(Service approval history) For each listed trust service, information on the status history "
            "when applicable is available in the service approval history information or a sequence of such "
            "information. The contents of the history information fields are specified in clause 5.6. 6) "
            "(Digital signature) The TL is a digitally signed list for authentication purposes. The contents "
            "of the digital signature field are specified in clause 5.7. The number of TSPs, of services per "
            "TSP, and of history sections per service is unbounded. The structure of the TL is further "
            "described in the following clauses by each component part and its fields."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 1 (Scope)",
    "clausola 3.1 (Terms)",
    "clausola 3.2 (Symbols)",
    "clausola 3.3 (Abbreviations)",
    "clausola 4 (Overall structure of trusted lists)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        # Clausola 4 punto 1): "The contents of the tag are specified in
        # clause 5.2.1." Riferimento esatto confermato dal subagent
        # Etsi612Cap02 (cap02.py), che scrive il nodo di 5.2.1.
        "nodo_da": ("principio", None, "clausola 4 (Overall structure of trusted lists)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.1 (TSL Tag)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
