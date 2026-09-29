"""ETSI EN 319 132-1 V1.3.1 (2024-07) - Electronic Signatures and Trust
Infrastructures (ESI); XAdES digital signatures; Part 1: Building blocks and
XAdES baseline signatures. Blocco B (famiglia AdES del lotto 2). Capitolo 2
dello split: clausola 3 (Definition of terms, symbols, abbreviations and
terminology), sottoclausole 3.1 (Terms), 3.2 (Symbols), 3.3 (Abbreviations) e
3.4 (Terminology). Conteggio di questo capitolo: 0 Obblighi, 4 Principi, 4
item di indice, 0 relazioni. Questo modulo NON tocca app/seed.py: gli id sono
risolti per riferimento dalla sessione principale tramite
app/seed_data/lib.py, e le relazioni verso altri capitoli della stessa fonte
o verso altre fonti le costruisce sempre la sessione principale (fase 6,
ADR-0009).

Provenienza del testo: app/.source_cache/etsi_319_132/cap02.txt (143 righe),
estratto dal PDF ufficiale ETSI deliver
https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf
versione 01.03.01_60, formato "PDF ETSI deliver (pdftotext -layout)",
data_fetch 2026-09-29T12:56:34Z, sha256 del PDF raw
83fc87ee09de90274131a1f60cb73edb742cebc7cd8961342586ed06133664c5 (tutti i
valori da app/.source_cache/etsi_319_132/provenance.json). Manifest di split:
app/.source_cache/etsi_319_132/manifest.json (voce cap02: testo_path
app/.source_cache/etsi_319_132/cap02.txt, modulo_path
app/seed_data/etsi_319_132/cap02.py). Il file di capitolo inizia alla riga
"3 Definition of terms, symbols, abbreviations and" (l'intestazione continua
sulla riga successiva con "terminology") e termina con l'ultimo paragrafo
della clausola 3.4; la clausola 4 (General Syntax) apre il capitolo
successivo (cap03).

## Perimetro del capitolo

Clausola di cornice, nessuna prescrizione: 3.1, 3.3 e 3.4 sono dichiarazioni
di vocabolario ("For the purposes of the present document ... apply", "The
present document uses the term ... for denoting ..."), 3.2 e' il segnaposto
di redazione "Void.". Nessun verbo prescrittivo con destinatario (nessun
"shall", nessun obbligo) in tutto il capitolo: nessuna riga Obbligo.

- Clausola 3.1 (Terms) -> 1 Principio "definitorio". Glossario alfabetico
  piatto, senza struttura a lettere o a numeri propri, di 17 termini:
  attribute certificate, certificate revocation list, data object, digital
  signature, digital signature value, electronic time-stamp, legacy XAdES
  101 903 signature, legacy XAdES baseline signature, legacy XAdES signature,
  message imprint, signature augmentation policy, signature creation policy,
  signature policy, signature validation policy, trust anchor, validation
  data, XAdES signature. Tutti riportati verbatim nel `testo_integrale`
  nell'ordine del testo ufficiale, con la frase di rinvio iniziale ai termini
  gia' dati in ETSI TR 119 001 [i.4]. Le 4 NOTE interne alle definizioni sono
  mantenute: (a) su data object (la definizione e' parte della definizione di
  questo termine in XMLDSIG [1]); (b) su electronic time-stamp (nel
  protocollo IETF RFC 3161 [7], aggiornato da IETF RFC 5816 [16], la marca
  temporale elettronica e' il campo timeStampToken dell'elemento
  TimeStampResp, cioe' la risposta della TSA al client richiedente); (c) su
  message imprint (corrisponde al valore di digest incorporato nel campo
  hashedMessage del tipo MessageImprint); (d) su signature augmentation
  policy (copre la raccolta di informazioni e la creazione di nuove strutture
  che consentono di eseguire nel lungo termine la convalida di una firma).
  Nessuna e' una mera citazione bibliografica: tutte aggiungono contenuto
  interpretativo al termine. I riferimenti bibliografici interni alle singole
  definizioni (XMLDSIG [1], ETSI TS 101 903 (V1.4.2) [i.2], ETSI TS 103 171
  (V2.1.1) [i.3], IETF RFC 3161 [7], IETF RFC 5816 [16], ETSI EN 319 132-2
  [i.17], ETSI TS 119 132-3 [i.18], ETSI TR 119 001 [i.4]) restano dentro il
  `testo_integrale` come parte integrante della definizione, senza generare
  relazione.
- Clausola 3.2 (Symbols) -> 1 Principio "definitorio" con `testo_integrale`
  "3.2 Symbols: Void.". Scelta di modellazione esplicita, non un giudizio di
  rilevanza: la clausola dichiara che per gli scopi del documento non si
  applica alcun simbolo e non ha contenuto oltre il segnaposto di redazione,
  ma e' una sottoclavola numerata reale della clausola 3 e ADR-0007 vieta
  ogni discrimine di rilevanza in estrazione (l'omissione sarebbe un giudizio
  di merito non coperto dal criterio). In questa famiglia di fonti esistono
  entrambe le convenzioni (ETSI EN 319 401 e EN 319 421 la escludono; ETSI TS
  119 432, TS 119 612, EN 319 411-1, EN 319 102-1, EN 319 122-1 ed ETSI TS
  119 312 la includono con il solo segnaposto): qui si include, come fa il
  modulo gemello ETSI EN 319 122-1 cap01.
- Clausola 3.3 (Abbreviations) -> 1 Principio "definitorio". Elenco di 31
  abbreviazioni con la forma estesa (ASN.1, BER, CA, CD, CER, CRL, DER, ERS,
  HTTP, MD5, MIME, OCSP, OID, PER, PI, PKI, SAML, SIM, SPO, TSA, TSL, TSP,
  TSU, URI, URL, URN, UTC, XER, XML, XMLDSIG, XSLT), preceduto dalla frase di
  rinvio "For the purposes of the present document, the following
  abbreviations apply:" (questa fonte non rinvia ad altre liste di
  abbreviazioni, a differenza di ETSI EN 319 122-1 clausola 3.3). La
  conversione PDF->testo rende la tabella come coppia etichetta/forma estesa
  sulla stessa riga, con le colonne allineate a spazi e la tabella spezzata
  dal salto di pagina fra MIME e OCSP: in `testo_integrale` le coppie sono
  ricostruite nella forma esplicita "ETICHETTA: Forma estesa", una per riga,
  nell'ordine del testo, senza perdere ne' riordinare alcun valore. Le
  irregolarita' tipografiche del testo ufficiale sono riportate come tali,
  senza correzioni: "european Commission Decision" (iniziale minuscola) per
  CD, "eXtensible Markup Language" e "eXtensible Markup Language Digital
  SIGnature" per XML e XMLDSIG, "Object IDentifier" per OID, il plurale di
  TSA ("Time-Stamping Authorities") e TSP ("Trusted Service Providers").
- Clausola 3.4 (Terminology) -> 1 Principio "definitorio". Sei paragrafi non
  numerati che fissano, voce per voce, il significato dei termini usati dal
  documento nel contesto XML: "qualifying property" (elemento XML che
  qualifica la firma, gli oggetti di dati firmati o il firmatario),
  "element" (esclusivamente elementi XML), "element"/"container" (i nuovi
  elementi XML contenitori di qualifying property, es. QualifyingProperties,
  SignedProperties, UnsignedProperties), "attribute" (sia gli attributi XML
  degli elementi XML sia gli attributi posseduti dal firmatario, come nella
  clausola 5.2.6), "child element" (esclusivamente nel contesto del contenuto
  XML) e "XAdES components" (qualunque elemento della firma XAdES e qualunque
  qualifying property XAdES incorporata nella firma). Paragrafi non numerati:
  restano tutti nel nodo della sottoclavola 3.4, come da convenzione adottata
  per le clausole di terminologia delle altre fonti ETSI censite (ETSI EN 319
  122-1 clausola 3.1, ETSI TS 119 312 clausola 3.1).

Granularita'. "Un item di indice per voce" e' letto come una riga e un item
di indice per ciascuna sottoclavola numerata della clausola 3 (3.1, 3.2,
3.3, 3.4), non un nodo per singolo termine, abbreviazione o paragrafo: e' la
convenzione costante delle fonti ETSI gia' censite (un glossario alfabetico
piatto e un elenco di abbreviazioni non hanno item di indice propri;
spezzarli in 48 item fittizi attribuirebbe a questa fonte una granularita'
che il testo non ha e romperebbe i rinvii cross-fonte verso "clausola 3.1",
usati per esempio dalla definizione di "attribute" nella clausola 3.4 e dalle
altre parti del deliverable). Le sottoclausole non sono elenchi di requisiti
in lettere o numerati: la regola dell'id-per-riga non ha qui alcun oggetto, i
termini e le abbreviazioni restano integralmente indicizzati dal full-text su
`testo_integrale`. Anche i `riferimento` seguono la forma convenzionale
italiana senza prefisso di parte ("clausola 3.1 (Terms)"), per restare
omogenei ai moduli fratelli della stessa Fonte.

Esclusioni: front matter, pagine di copertina, Contents, Foreword, History e
la sezione bibliografica (esclusi a monte dallo split deterministico); il
paratesto di pagina ripetuto dalla conversione PDF (footer "ETSI",
intestazione "ETSI EN 319 132-1 V1.3.1 (2024-07)", numeri di pagina 11-12,
righe vuote di impaginazione); l'intestazione della clausola 3 (righe 1-2 del
file di capitolo), che non ha contenuto proprio oltre il titolo e le sue
quattro sottoclausole (stesso criterio gia' applicato alle intestazioni di
raggruppamento di ETSI EN 319 122-1, ETSI TS 119 312, ETSI EN 319 401). E'
escluso, per esplicita scelta di perimetro confermata dall'utente, anche
l'elenco bibliografico della clausola 2 (References: 18 riferimenti normativi
[1]-[18] e 22 informativi [i.1]-[i.22] in questa versione): e' bibliografia e
paratesto puro, nessuna delle sue voci e' un'unita' di prescrizione ne' puo'
essere il bersaglio di un rinvio a una clausola di questo standard; l'intera
clausola 2 ricade nel capitolo precedente dello split (cap01.txt, clausole
1-2) e non produce alcun item di indice in questo modulo.

Rinvii demandati alla fase 6 (nessuna relazione dichiarata in questo modulo,
che non contiene rinvii fra le proprie righe; RELAZIONI e' vuota):
- altre fonti: ETSI TR 119 001 [i.4] (lista di termini richiamata dalla
  clausola 3.1), XMLDSIG [1] (NOTE della definizione di data object), ETSI TS
  101 903 (V1.4.2) [i.2] ed ETSI TS 103 171 (V2.1.1) [i.3] (famiglie legacy
  XAdES), IETF RFC 3161 [7] e IETF RFC 5816 [16] (NOTE di electronic
  time-stamp e message imprint), ETSI EN 319 132-2 [i.17] ed ETSI TS 119
  132-3 [i.18] (definizione di XAdES signature), ETSI EN 319 102-1 (procedure
  di creazione, augmentation e convalida citate dallo Scope di questa fonte,
  non da questo capitolo);
- internamente alla fonte: "clause 5.2.6" citata letteralmente dal quarto
  paragrafo della clausola 3.4 ("attributes owned by the signer (as in clause
  5.2.6 for instance)") -> clausola 5.2.6, attributo signer-attributes-v2,
  coperta dal capitolo cap04 di questa fonte: bersaglio di un rinvio interno
  alla Fonte, quindi nessun arco qui (le relazioni interne sono comunque
  costruite dalla sessione principale in fase 6).

Conteggio di copertura di questo capitolo: 4 item di indice, 4 righe (0
obblighi + 4 principi), 0 relazioni.
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 3.1 (Terms)",
        "testo": (
            "La clausola definisce, per gli scopi del documento e in aggiunta ai termini gia' dati "
            "in ETSI TR 119 001 [i.4], 17 termini in ordine alfabetico: attribute certificate, "
            "certificate revocation list, data object, digital signature, digital signature value, "
            "electronic time-stamp, legacy XAdES 101 903 signature, legacy XAdES baseline signature, "
            "legacy XAdES signature, message imprint, signature augmentation policy, signature "
            "creation policy, signature policy, signature validation policy, trust anchor, validation "
            "data e XAdES signature (firma digitale che soddisfa i requisiti del presente documento o "
            "di ETSI EN 319 132-2 [i.17] o di ETSI TS 119 132-3 [i.18]). Le quattro NOTE interne alle "
            "definizioni precisano il significato dei termini nel contesto tecnologico: data object e' "
            "definito come in XMLDSIG [1]; electronic time-stamp, nel protocollo IETF RFC 3161 [7] "
            "aggiornato da IETF RFC 5816 [16], e' il campo timeStampToken dell'elemento TimeStampResp; "
            "message imprint corrisponde al valore di digest incorporato nel campo hashedMessage del "
            "tipo MessageImprint; signature augmentation policy copre la raccolta di informazioni e la "
            "creazione di nuove strutture che consentono di convalidare una firma nel lungo termine."
        ),
        "testo_integrale": (
            "3.1 Terms: For the purposes of the present document, the terms given in ETSI TR 119 001 "
            "[i.4] and the following apply:\n"
            "attribute certificate: data structure, digitally signed by an attribute authority, that "
            "binds some attribute values with identification information about its holder\n"
            "certificate revocation list: signed list indicating a set of certificates that are no "
            "longer considered valid by the certificate issuer\n"
            "data object: actual binary/octet data being operated on (transformed, digested, or "
            "signed) by an application\n"
            "NOTE: This definition of term is part of the definition of this term within XMLDSIG [1].\n"
            "digital signature: data appended to, or a cryptographic transformation of a data unit "
            "that allows a recipient of the data unit to prove the source and integrity of the data "
            "unit and protect against forgery e.g. by the recipient\n"
            "digital signature value: result of cryptographic transformation of a data unit that "
            "allows a recipient of the data unit to prove the source and integrity of the data unit "
            "and protect against forgery e.g. by the recipient\n"
            "electronic time-stamp: data in electronic form which binds other electronic data to a "
            "particular time establishing evidence that these data existed at that time\n"
            "NOTE: In the case of IETF RFC 3161 [7] protocol, updated by IETF RFC 5816 [16], the "
            "electronic time-stamp is referring to the timeStampToken field within the TimeStampResp "
            "element (the TSA's response returned to the requesting client).\n"
            "legacy XAdES 101 903 signature: digital signature generated according to ETSI TS 101 903 "
            "(V1.4.2) [i.2]\n"
            "legacy XAdES baseline signature: digital signature generated according to ETSI TS 103 171 "
            "(V2.1.1) [i.3]\n"
            "legacy XAdES signature: legacy XAdES 101 903 signature or legacy XAdES baseline "
            "signature\n"
            "message imprint: digest value of the data that is going to be time-stamped\n"
            "NOTE: In the case of electronic time-stamps compliant with IETF RFC 3161 [7], as updated "
            "by IETF RFC 5816 [16], it corresponds to the digest value incorporated into the "
            "hashedMessage field of MessageImprint type.\n"
            "signature augmentation policy: set of rules, applicable to one or more digital "
            "signatures, that defines the technical and procedural requirements for their "
            "augmentation, in order to meet a particular business need, and under which the digital "
            "signature(s) can be determined to be conformant\n"
            "NOTE: This covers collection of information and creation of new structures that allows "
            "performing, on the long term, validations of a signature.\n"
            "signature creation policy: set of rules, applicable to one or more digital signatures, "
            "that defines the technical and procedural requirements for their creation, in order to "
            "meet a particular business need, and under which the digital signature(s) can be "
            "determined to be conformant\n"
            "signature policy: signature creation policy, signature augmentation policy, signature "
            "validation policy or any combination thereof, applicable to the same signature or set of "
            "signatures\n"
            "signature validation policy: set of rules, applicable to one or more digital signatures, "
            "that defines the technical and procedural requirements for their validation, in order to "
            "meet a particular business need, and under which the digital signature(s) can be "
            "determined to be valid\n"
            "trust anchor: entity that is trusted by a relying party and used for validating "
            "certificates in certification paths\n"
            "validation data: data that is used to validate a digital signature\n"
            "XAdES signature: digital signature that satisfies the requirements specified within the "
            "present document or ETSI EN 319 132-2 [i.17] or ETSI TS 119 132-3 [i.18]."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.2 (Symbols)",
        "testo": (
            "La clausola non definisce alcun simbolo: il testo ufficiale della clausola 3.2 (Symbols) "
            "e' integralmente 'Void.', cioe' dichiara che per gli scopi del documento non si applica "
            "alcun simbolo. Nessun contenuto oltre il segnaposto di redazione, ma la sottoclavola "
            "numerata e' censita per copertura completa della clausola 3."
        ),
        "testo_integrale": "3.2 Symbols: Void.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.3 (Abbreviations)",
        "testo": (
            "La clausola elenca le 31 abbreviazioni usate dal documento, ciascuna con la propria forma "
            "estesa, senza rinviare ad altre liste di abbreviazioni di altre fonti: ASN.1, BER, CA, CD, "
            "CER, CRL, DER, ERS, HTTP, MD5, MIME, OCSP, OID, PER, PI, PKI, SAML, SIM, SPO, TSA, TSL, "
            "TSP, TSU, URI, URL, URN, UTC, XER, XML, XMLDSIG e XSLT. Le forme estese sono quelle del "
            "testo ufficiale, comprese le sue irregolarita' tipografiche ('european Commission "
            "Decision' per CD, 'eXtensible Markup Language'/Digital SIGnature per XML e XMLDSIG, il "
            "plurale 'Time-Stamping Authorities'/'Trusted Service Providers' per TSA e TSP)."
        ),
        "testo_integrale": (
            "3.3 Abbreviations: For the purposes of the present document, the following abbreviations "
            "apply:\n"
            "ASN.1: Abstract Syntax Notation 1\n"
            "BER: Basic Encoding Rules\n"
            "CA: Certification Authority\n"
            "CD: european Commission Decision\n"
            "CER: Canonical Encoding Rules\n"
            "CRL: Certificate Revocation List\n"
            "DER: Distinguished Encoding Rules\n"
            "ERS: Evidence Record Syntax\n"
            "HTTP: Hyper Text Transfer Protocol\n"
            "MD5: Message-Digest Algorithm 5\n"
            "MIME: Multipurpose Internet Mail Extensions\n"
            "OCSP: Online Certificate Status Protocol\n"
            "OID: Object IDentifier\n"
            "PER: Packed Encoding Rules\n"
            "PI: Processing Instruction\n"
            "PKI: Public Key Infrastructure\n"
            "SAML: Security Assertion Markup Language\n"
            "SIM: Subscriber Identity Module\n"
            "SPO: Service Provision Option\n"
            "TSA: Time-Stamping Authorities\n"
            "TSL: Trust-service Status List\n"
            "TSP: Trusted Service Providers\n"
            "TSU: Time-Stamping Unit\n"
            "URI: Uniform Resource Identifier\n"
            "URL: Uniform Resource Locator\n"
            "URN: Uniform Resource Name\n"
            "UTC: Coordinated Universal Time\n"
            "XER: XML Encoding Rules\n"
            "XML: eXtensible Markup Language\n"
            "XMLDSIG: eXtensible Markup Language Digital SIGnature\n"
            "XSLT: eXtensible Stylesheet Language Transformations"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.4 (Terminology)",
        "testo": (
            "La clausola fissa il vocabolario XML del documento attraverso sei dichiarazioni d'uso dei "
            "termini: 'qualifying property' denota un elemento XML che qualifica la firma, gli oggetti "
            "di dati firmati o il firmatario; 'element' denota esclusivamente elementi XML; i nuovi "
            "elementi XML definiti dal documento che contengono qualifying property (per esempio "
            "QualifyingProperties, SignedProperties o UnsignedProperties) sono denotati come 'element' "
            "o 'container'; 'attribute' denota sia gli attributi XML degli elementi XML sia gli "
            "attributi posseduti dal firmatario (come nella clausola 5.2.6), per cui una qualifying "
            "property, essendo un elemento XML, puo' avere attributi (XML); 'child element' e' usato "
            "esclusivamente nel contesto del contenuto XML, per denotare un elemento XML figlio di un "
            "altro elemento XML; 'XAdES components' denota qualunque elemento di una firma XAdES e "
            "qualunque qualifying property XAdES incorporata nella firma."
        ),
        "testo_integrale": (
            "3.4 Terminology: The present document uses the term \"qualifying property\" for denoting "
            "an XML element that qualifies the signature, the signed data objects, or the signer.\n"
            "\n"
            "The present document uses the term \"element\" exclusively for denoting XML elements.\n"
            "\n"
            "The present document defines new XML elements that are containers of qualifying "
            "properties (for instance QualifyingProperties, SignedProperties, or UnsignedProperties). "
            "The present document uses the terms \"element\" or \"container\" when refers to them.\n"
            "\n"
            "The present document uses the term \"attribute\" for denoting either XML attributes of "
            "XML elements or for denoting attributes owned by the signer (as in clause 5.2.6 for "
            "instance). Consequently, a qualifying property, being an XML element, can have (XML) "
            "attributes.\n"
            "\n"
            "The present document uses the term \"child element\" exclusively in the context of XML "
            "content, for denoting an XML element that is a child element of another XML element.\n"
            "\n"
            "The present document uses the term \"XAdES components\" for denoting any XAdES "
            "signature's element, and any XAdES qualifying property incorporated into the XAdES "
            "signature."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 3.1 (Terms)",
    "clausola 3.2 (Symbols)",
    "clausola 3.3 (Abbreviations)",
    "clausola 3.4 (Terminology)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
