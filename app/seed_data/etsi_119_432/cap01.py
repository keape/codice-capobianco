"""ETSI TS 119 432 V1.3.1 (2026-03) - Electronic Signatures and Trust
Infrastructures (ESI); Protocols for remote digital signature creation.
Fonte 20 (la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 1:
clausole 1 (Scope), 2 (References: 2.1 Normative references, 2.2 Informative
references), 3 (Definition of terms, symbols and abbreviations: 3.1 Terms,
3.2 Symbols, 3.3 Abbreviations). Documento unico (non multi-parte): i
`riferimento` NON portano prefisso di Parte. Testo ufficiale in
app/.source_cache/etsi_119_432/cap01.txt (letto sempre con selettore `:raw`,
altrimenti il tool tronca le righe lunghe a 768 caratteri introducendo "..."
e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_119_432/manifest.json.

Modellazione (ADR-0007), stesso criterio gia' applicato alle altre fonti
ETSI gia' censite (ETSI EN 319 401, ETSI EN 319 412, ETSI EN 319 421, ETSI
EN 319 422) e adattato alle clausole/sottoclausole di uno standard tecnico:
un nodo per ogni clausola/sottoclasse numerata che porta contenuto proprio;
per le clausole di cornice prive di requisito numerato un solo nodo Principio
dedicato. Questo capitolo non contiene alcun requisito numerato: 0 Obblighi,
4 Principi. Scelte voce per voce:

- Clausola 1 (Scope) -> 1 Principio "scopo/ambito di applicazione",
  riferimento "clausola 1 (Scope)". Perimetro in senso proprio: dichiara che
  il documento specifica protocolli e interfacce applicabili quando la
  creazione di firme digitali AdES (come definite in ETSI EN 319 102-1
  [i.12]) e/o di valori di firma digitale, a partire da Data To Be Signed
  Representations, e' svolta da una soluzione distribuita composta da due o
  piu' sistemi/servizi/componenti; limita l'ambito alla firma remota su
  server (chiave di firma custodita in un servizio remoto condiviso);
  esclude esplicitamente la creazione di firma con firma locale; dichiara
  che il documento non specifica alcun binding obbligatorio; richiama, ove
  possibile, costrutti delle specifiche JSON di CSC API [1] e XML di OASIS
  DSS-X [4], specificando altrimenti nuovi componenti semanticamente e
  sintatticamente; considera alcune modalita' con cui il processo di
  verifica dell'identita' utente e quello di autorizzazione delle firme
  dell'utente possono essere svolti dal fornitore del servizio. Nessun verbo
  prescrittivo ("shall"/"should") e nessun soggetto obbligato: e'
  dichiarazione di perimetro, non prescrizione. La clausola contiene una
  NOTE ufficiale (esclusione della firma locale), riportata in
  `testo_integrale` per completezza verbatim (ADR-0010).
- Clausola 2 (References: 2.1 Normative references, 2.2 Informative
  references) -> NESSUN nodo, NESSUN item di indice. E' bibliografia/
  paratesto puro: un elenco di documenti citati numerati [1]-[31]
  (normative) e [i.1]-[i.21] (informative) con le sole regole redazionali
  ETSI su riferimenti specifici/non specifici e le NOTE ETSI sulla validita'
  a lungo termine degli hyperlink, nessun contenuto normativo autonomo ne'
  effetto giuridico proprio. Stesso trattamento gia' riservato alla clausola
  2 di ETSI EN 319 401, ETSI EN 319 421 e ETSI EN 319 422 (cap01). Si noti
  che la conversione PDF->markdown spezza entrambi gli elenchi con
  interruzioni di pagina ("***ETSI***" / "<!-- Page N -->"): paratesto spurio
  che conferma l'assenza di contenuto prescrittivo.
- Clausola 3.1 (Terms) -> 1 Principio "definitorio" riassuntivo, NON un nodo
  per singolo termine: la clausola e' un glossario piatto senza struttura a
  lettere/numeri propria, quindi N nodi sarebbero N item di indice fittizi
  per un'unica clausola. Definisce 26 termini propri del documento: AdES
  (digital) signature; client application; digital signature; digital
  signature value; driving application; FAPI; intermediary; relying party;
  remote signature creation device; remote signing server; server signing
  application; server signing application service component; server signing
  application service provider; service authorization; signature activation
  data; signature activation module; signature creation application;
  signature creation application service component; signature creation
  application service provider; signature creation constraint; signature
  creation device; signature creation policy; signature creation service;
  signature creation service provider; signing credential; user agent. In
  `testo_integrale` sono riportate tutte le definizioni verbatim in ordine,
  precedute dalla formula introduttiva ufficiale ("For the purposes of the
  present document, the terms given in ETSI TR 119 001 [i.3] and the
  following apply:"). Le NOTE ufficiali presenti sotto alcune definizioni
  (signature activation module, signature creation application, signature
  creation service provider, user agent) sono incluse in `testo_integrale`
  per completezza verbatim (ADR-0010).
- Clausola 3.2 (Symbols) -> 1 Principio "definitorio". Il testo ufficiale
  della clausola e' integralmente "Void.", cioe' dichiara che il documento
  non definisce alcun simbolo. E' una dichiarazione di contenuto (vuoto) di
  cornice, priva di soggetto obbligato: si censisce comunque, per copertura
  completa per clausola (ADR-0007), come unico nodo Principio "definitorio"
  con `testo_integrale` = "3.2 Symbols: Void.".
- Clausola 3.3 (Abbreviations) -> 1 Principio "definitorio" riassuntivo. La
  clausola elenca le abbreviazioni usate nel documento, precedute dalla
  formula introduttiva ufficiale ("For the purposes of the present document,
  the following abbreviations apply:"). La tabella PDF->markdown risulta
  parzialmente disallineata (alcune righe, es. "QR code" o "SD-JWT VC",
  hanno l'etichetta e la forma estesa distribuite su righe adiacenti, e un
  paio di voci portano una NOTE): le coppie sono quindi ricostruite in forma
  esplicita "ETICHETTA: Forma estesa." in `testo_integrale`, come gia' fatto
  per la clausola 3.2 di ETSI EN 319 422. Sono incluse tutte le
  abbreviazioni della lista (dalla API alla XSD, 96 voci), con le NOTE ufficiali
  (QR code, SCAL1, SCAL2, SIC) riportate verbatim, per completezza verbatim
  della clausola (ADR-0010).

Nessun Obbligo in questo capitolo: nessuna delle clausole coperte contiene un
verbo prescrittivo che imponga un comportamento a un soggetto identificabile.
La costruzione di relazioni e' demandata alla Fase 6 della sessione principale
(ADR-0009); non ci sono citazioni letterali interne tra clausole della stessa
Fonte.
"""

RIGHE_OBBLIGHI: list[dict] = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 1 (Scope)",
        "testo": (
            "Il documento specifica protocolli e interfacce applicabili quando la creazione di firme "
            "digitali AdES (come definite in ETSI EN 319 102-1) e/o di valori di firma digitale, a partire da "
            "Data To Be Signed Representations, e' svolta da una soluzione distribuita composta da due o piu' "
            "sistemi/servizi/componenti. L'ambito e' limitato alla firma remota su server, con la chiave di "
            "firma custodita in un servizio remoto condiviso; la creazione di firma con firma locale (chiave "
            "sul dispositivo personale del firmatario) e' esclusa. Il documento non specifica alcun binding "
            "obbligatorio; ove possibile richiama costrutti delle specifiche JSON di CSC API e XML di OASIS "
            "DSS-X, specificando altrimenti nuovi componenti anche sintatticamente. Considera infine alcune "
            "modalita' con cui il fornitore del servizio puo' svolgere la verifica dell'identita' utente e "
            "l'autorizzazione delle firme dell'utente."
        ),
        "testo_integrale": (
            "1 Scope: The present document specifies protocols and interfaces applicable when the process of "
            "creating AdES digital signatures as defined by ETSI EN 319 102-1 [i.12] and/or digital signature "
            "values, as result of Data To Be Signed Representations signatures, is carried out by a "
            "distributed solution comprised of two or more systems/services/components. The present document "
            "is limited to remote server signing, i.e. the signing key is held in a remote shared service. "
            "NOTE: Remote signature creation with local signing, i.e. the signing key is held with the "
            "signer's personal device but other steps in the signature creation are carried out by means of "
            "networked services, is a possible solution but protocols for such architecture are not covered "
            "in the present document. Finally, the present document does not specify any mandatory binding. "
            "As far as it has been possible and suitable, references to constructs of CSC API [1] JSON "
            "specifications and OASIS DSS-X [4] XML specifications are specified in the present document. "
            "When this has not been possible the present document specifies new components semantically and "
            "also syntactically. The authorized signer's use of its key for signing requires users to provide "
            "multiple proofs of their claimed identity before being granted access to the needed set of "
            "resources. The present document considers some ways in which the user identity verification "
            "process and the user signatures authorization process can be carried out by the service "
            "provider."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.1 (Terms)",
        "testo": (
            "La clausola definisce 26 termini propri del documento (oltre ai termini di ETSI TR 119 001, "
            "richiamati dalla formula introduttiva): AdES (digital) signature (firma CAdES, PAdES o XAdES); "
            "client application (applicazione che richiede autorizzazione a un Authorization Server per "
            "conto di un resource owner); digital signature; digital signature value; driving application "
            "(applicazione che usa un servizio SCASC o SSASC per creare una firma); FAPI (working group "
            "OpenID Foundation); intermediary (entita' che agisce per conto di una relying party verso "
            "l'EUDIW); relying party; remote signature creation device; remote signing server; server "
            "signing application; server signing application service component/provider; service "
            "authorization; signature activation data; signature activation module; signature creation "
            "application; signature creation application service component/provider; signature creation "
            "constraint; signature creation device; signature creation policy; signature creation service; "
            "signature creation service provider; signing credential; user agent."
        ),
        "testo_integrale": (
            "3.1 Terms: For the purposes of the present document, the terms given in ETSI TR 119 001 [i.3] "
            "and the following apply: AdES (digital) signature: digital signature that is either a CAdES "
            "signature, or a PAdES signature or a XAdES signature client application: application that "
            "requests authorization from an Authorization Server on behalf of a resource owner (signer in "
            "the present document), in order to access protected resources at a Resource Server (signer's "
            "private key usage in the present document) digital signature: data appended to, or a "
            "cryptographic transformation of a data unit that allows a recipient of the data unit to prove "
            "the source and integrity of the data unit and protect against forgery (e.g. by the recipient) "
            "digital signature value: result of the cryptographic transformation of a data unit that allows "
            "a recipient of the data unit to prove the source and integrity of the data unit and protect "
            "against forgery (e.g. by the recipient) driving application: application that uses a SCASC or a "
            "SSASC service to create a signature FAPI: an OpenID Foundation working group, where FAPI was "
            "previously known as the Financial-grade API but where consensus was reached within the working "
            "group to update the name to just FAPI to reflect that the specification was appropriate for "
            "many high-value use-cases requiring a more secure model beyond just financial services "
            "intermediary: entity acting on behalf of a relying party for the purpose of transmitting or "
            "facilitating requests to the EUDIW relying party: entity that relies upon the output of a trust "
            "service, in particular upon a certificate, an electronic signature/seal, or the result of its "
            "validation; in a remote signature architecture, it can be the entity that requests remote "
            "signature creation and then relies on the result and/or the recipient that verifies and then "
            "relies upon the AdES/QES generated by the remote signing service remote signature creation "
            "device: signature creation device used remotely from signer perspective and providing control "
            "of signing operation on the signer's behalf remote signing server: server application using a "
            "signature creation device to create a digital signature value on behalf of a signer server "
            "signing application: application using a remote signature creation device to create a digital "
            "signature value on behalf of a signer server signing application service component: TSP service "
            "component employing a server signing application server signing application service provider: "
            "TSP operating a server signing application service component service authorization: process of "
            "verifying and enforcing that a client (such as an application, user, or system component) has "
            "the necessary permissions and rights to access and invoke specific operations or endpoints "
            "exposed by a service API, according to predefined policies or access control rules signature "
            "activation data: set of data used to control with a high level of confidence a given signature "
            "operation, performed by a cryptographic module on behalf of the signer, that is under sole "
            "control of the signer signature activation module: configured software that uses the SAD in "
            "order to guarantee with a high level of confidence that the signing keys are used under sole "
            "control of the signer NOTE: As defined in EN 419 241-1 [6]. signature creation application: "
            "application within the signature creation system that creates the AdES digital signature and "
            "relies on the SCDev to create a digital signature value NOTE: The SCDev can be managed by the "
            "SSASC. signature creation application service component: TSP service component employing a "
            "signature creation application signature creation application service provider: TSP operating "
            "a signature creation application service component signature creation constraint: criteria used "
            "when creating a digital signature signature creation device: configured software or hardware "
            "used to implement the signature creation data and to create a digital signature value signature "
            "creation policy: set of signature creation constraints processed or to be processed by the "
            "SCASC or the SSASC signature creation service: TSP service implementing a signature creation "
            "application and/or a server signing application signature creation service provider: service "
            "provider offering a signature creation service NOTE: As defined in EN 419 241-1 [6]. signing "
            "credential: set of the signing key and the corresponding signing certificate user agent: "
            "software component acting on behalf of the resource owner (the signer in the context of the "
            "present document) that interacts with the authorization server and the driving application "
            "NOTE: Typically, this is the web browser or application through which the user accesses the "
            "driving application. The user agent is responsible for presenting the authorization interface "
            "to the user and forwarding requests and responses between the driving application and the "
            "authorization server."
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
            "La clausola elenca le abbreviazioni usate nel documento: API, AS, AS/SAM, CA, CBOR, CEN, CMS, "
            "CR, CRL, CSC, CSC API, CSC DM, DA, DC, DCQL, DPoP, DSS-X, DSV, DTBS, DTBSF, DTBSR, ECDSA, "
            "eIDAS, EN, EUDI, EUDIW, FIDO2, HMAC, HTTP, HTTPS, ISO, JAR, JSON, JWS, JWT, LT, LTA, mTLS, NFC, "
            "OASIS, OCSP, OID, OIDC, OpenID, OpenID4VP, OTP, PAR, PID, PIN, PKCE, PKI, QES, QR code, QSCD, "
            "QTSP, RA, RAR, RP, RSA, RSSP, SAD, SAM, SAML, SCA, SCAL, SCAL1, SCAL2, SCASC, SCDev, SCS, SCSP, "
            "SD, SD-JWT VC, SDO, SDOC, SDR, SHA, SIC, SMS, SRI, SSA, SSASC, SSH, TLS, TR, TSP, URI, URL, "
            "URN, UTF-8, UX, VP, WRP, WUA, XML, XSD."
        ),
        "testo_integrale": (
            "3.3 Abbreviations: For the purposes of the present document, the following abbreviations "
            "apply: API: Application Program Interface. AS: Authorization Server. AS/SAM: Authorization "
            "Server / Signature Activation Module. CA: Certification Authority. CBOR: Concise Binary Object "
            "Representation. CEN: European Committee for Standardization. CMS: Cryptographic Message Syntax. "
            "CR: Change Request. CRL: Certificate Revocation List. CSC: Cloud Signature Consortium. CSC API: "
            "CSC Standard: \"Architectures and protocols for remote signature applications\". CSC DM: CSC "
            "Standard: \"Data model for remote signature applications\". DA: Driving Application. DC: "
            "Digital Credential. DCQL: Digital Credentials Query Language. DPoP: Demonstrating "
            "Proof-of-Possession. DSS-X: Digital Signature Services eXtended. DSV: Digital Signature Value. "
            "DTBS: Data To Be Signed. DTBSF: Data To Be Signed Formatted. DTBSR: Data To Be Signed "
            "Representation. ECDSA: Elliptic Curve Digital Signature Algorithm. eIDAS: electronic "
            "Identification And trust Services. EN: European Norm. EUDI: European Digital Identity. EUDIW: "
            "European Digital Identity Wallet. FIDO2: Fast IDentity Online 2. HMAC: Hashed Message "
            "Authentication Code. HTTP: Hyper Text Transfer Protocol. HTTPS: HyperText Transfer Protocol "
            "Secure. ISO: International Organization for Standardization. JAR: JWT-Secured Authorization "
            "Request. JSON: Java Script Object Notation. JWS: JSON Web Signature. JWT: JSON Web Token. LT: "
            "Long Term. LTA: Long Term Archival. mTLS: mutual Transport Layer Security. NFC: Near Field "
            "Communication. OASIS: Organization for the Advancement of Structured Information Standards. "
            "OCSP: Online Certificate Status Protocol. OID: Object IDentifier. OIDC: OpenID Connect. "
            "OpenID: OpenID foundation. OpenID4VP: OpenID for Verifiable Presentations. OTP: One-Time "
            "Password. PAR: Pushed Authorization Requests. PID: Person Identification Data. PIN: Personal "
            "Identification Number. PKCE: Proof Key for Code Exchange. PKI: Public Key Infrastructure. QES: "
            "Qualified Electronic Signature. QR code: Quick Response code. NOTE: Two-dimensional "
            "machine-readable optical barcode that contains information about the item to which it is "
            "attached. QSCD: Qualified electronic Signature Creation Device. QTSP: Qualified Trust Service "
            "Provider. RA: Registration Authority. RAR: Rich Authorization Request. RP: Relying Party. RSA: "
            "Rivest, Shamir, & Adleman. RSSP: Remote Signing Server Provider. SAD: Signature Activation "
            "Data. SAM: Signature Activation Module. SAML: Security Access Markup Language. SCA: Signature "
            "Creation Application. SCAL: Sole Control Assurance Level. SCAL1: Sole Control Assurance Level "
            "1. NOTE: As defined in EN 419 241-1 [6]. SCAL2: Sole Control Assurance Level 2. NOTE: As "
            "defined in EN 419 241-1 [6]. SCASC: Signature Creation Application Service Component. SCDev: "
            "Signature Creation Device. SCS: Signature Creation Service. SCSP: Signature Creation Service "
            "Provider. SD: Signer's Document. SD-JWT VC: Selective Disclosure based JSON Web Token "
            "Verifiable Credentials. SDO: Signed Data Object. SDOC: Signed Data Object Composer. SDR: "
            "Signer's Document Representation. SHA: Secure Hash Algorithm. SIC: Signature Interaction "
            "Component. NOTE: As defined in EN 419 241-1 [6]. SMS: Short Message Service. SRI: SubResource "
            "Integrity. SSA: Server Signing Application. SSASC: Server Signing Application Service "
            "Component. SSH: Secure Shell Protocol. TLS: Transport Layer Security. TR: Technical Report. "
            "TSP: Trust Service Provider. URI: Uniform Resource Identifier. URL: Uniform Resource Locator. "
            "URN: Uniform Resource Name. UTF-8: Unicode Transformation Format - 8 bit. UX: User eXperience. "
            "VP: Verifiable Presentation. WRP: Wallet-Relying Party. WUA: Wallet Unit Attestation. XML: "
            "eXtended Markup Language. XSD: XML Schema Definition."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 1 (Scope)",
    "clausola 3.1 (Terms)",
    "clausola 3.2 (Symbols)",
    "clausola 3.3 (Abbreviations)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Nessuna citazione letterale interna tra clausole/annessi della stessa Fonte
# in questo capitolo: RELAZIONI vuoto. Il collegamento cross-fonte e' demandato
# alla Fase 6 della sessione principale (ADR-0009).
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
