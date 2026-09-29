"""ETSI EN 319 122-1 V1.3.1 (2023-06) - Electronic Signatures and Trust
Infrastructures (ESI); CAdES digital signatures; Part 1: Building blocks and
CAdES baseline signatures.
Capitolo 2 del manifest: clausola 4 (General syntax), sottoclauste 4.1-4.9.
La numerazione della Fonte e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py.

Provenienza del testo
---------------------
Testo ufficiale in app/.source_cache/etsi_319_122/cap02.txt, porzione della
clausola 4 dello standard, estratta da app/.source_cache/etsi_319_122/raw.txt
(manifest di split: app/.source_cache/etsi_319_122/manifest.json, capitolo
"cap02", titolo "4 - General syntax"). Provenienza dal provenance.json della
fonte: URL https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf,
versione ETSI "01.03.01_60" (EN 319 122-1 V1.3.1, 2023-06), data di fetch
2026-09-29T12:56:34Z, sha256 del PDF grezzo
e99e76e519d9bd8e1410775bccedb1a588021e5e7c705c9fcc1f91c6a6227c21, formato
"PDF ETSI deliver (pdftotext -layout)".

Perimetro del capitolo
----------------------
Clausola 4 completa: 4.1 General requirements, 4.2 The data content type,
4.3 The signed-data content type, 4.4 The SignedData type, 4.5 The
EncapsulatedContentInfo type, 4.6 The SignerInfo type, 4.7 ASN.1 Encoding
(4.7.1 DER, 4.7.2 BER), 4.8 Other standard data structures (4.8.1 Time-stamp
token format, 4.8.2 Additional types), 4.9 Attributes. Nessun requisito
numerato con id proprio in questa clausola: ETSI EN 319 122-1 numera per
clausola/sottoclausta e non usa identificatori di requisito del tipo
GEN-/OVR-/REQ-/SDP- (verificato sull'intero testo ufficiale: zero occorrenze in
raw.txt). La granularita' e' quindi la sottoclausta, come per ETSI TS 119 612 e
ETSI EN 319 102-1 gia' censiti.

Modellazione (ADR-0007: copertura completa, un nodo per unita' numerata con
contenuto proprio; nessun discrimine di rilevanza). Scelte voce per voce:

- 4.1 General requirements -> 1 Obbligo "tecnico/sicurezza". Contiene due
  prescrizioni ("CAdES signatures shall build on CMS ...", "CAdES signatures
  shall comply with clauses 2, 3, 4 and 5 of IETF RFC 5652 [7]") piu' il
  periodo di raccordo "The following clauses list the types that are used in
  the attributes described in clause 5.1.": il periodo di raccordo non e' una
  unita' numerata a se' e resta nel nodo della sottoclausta che lo contiene
  (stesso criterio dei periodi introduttivi "In particular:" di ETSI EN
  319 401). Il vincolo e' di conformazione sintattica (fondarsi su CMS), non
  un processo organizzativo.
- 4.2 The data content type -> 1 Obbligo "tecnico/sicurezza": "shall be as
  defined in CMS" e' un requisito di conformazione del formato, stesso
  trattamento riservato in questo censimento agli analoghi "shall be as
  defined in <standard>" (es. OVR-6.6.2-01 "The CRL shall be as defined in
  ISO/IEC 9594-8", QCS-4.3.2-01 "The currency codes shall be as defined in
  ISO 4217"). La NOTE con l'object identifier id-data e' il blocco ASN.1
  della clausola ed e' riportata verbatim (righe ricucite).
- 4.3 The signed-data content type -> 1 Obbligo "tecnico/sicurezza".
- 4.4 The SignedData type -> 1 Obbligo "tecnico/sicurezza". Oltre al rinvio a
  CMS fissa il valore di CMSVersion e introduce la notazione SignedData.xxx /
  SignedData.xxx.yyy usata nel resto del documento; NOTE verbatim.
- 4.5 The EncapsulatedContentInfo type -> 1 Obbligo "tecnico/sicurezza". Il
  secondo periodo usa "should" (non "shall") per la validazione di lungo
  termine: lo schema non distingue shall da should (unico tipo prescrittivo
  disponibile) e la raccomandazione resta nello stesso nodo, come gia' fatto
  per le clausole 6.3 di ETSI TS 119 612 e 6.2 di ETSI EN 319 401. NOTE 1 e
  NOTE 2 hanno contenuto interpretativo sostanziale (perche' l'OCTET STRING
  deve restare identico; cosa comporta presenza/assenza dell'eContent) e sono
  riportate per intero.
- 4.6 The SignerInfo type -> 1 Obbligo "tecnico/sicurezza". Il divieto "The
  degenerate case where there are no signers shall not be used" e' una
  prescrizione negativa della stessa clausola: resta nel nodo, non e' una
  unita' numerata autonoma.
- 4.7.1 DER -> 1 Obbligo "tecnico/sicurezza" (rinvio normativo a ITU-T X.690).
- 4.7.2 BER -> 1 Obbligo "tecnico/sicurezza" (condizionale nell'uso, non
  condizionale nell'applicabilita' del nodo: la clausola esiste sempre, il
  testo non e' marcato [CONDITIONAL], quindi nessun
  `condizione_applicabilita`).
- 4.8.1 Time-stamp token format -> 1 Obbligo "tecnico/sicurezza" (rinvio a
  IETF RFC 3161 aggiornato da IETF RFC 5816); la NOTE che rinvia al profilo di
  ETSI EN 319 422 [i.9] e' di solo rimando bibliografico e non aggiunge
  contenuto interpretativo, ma non e' stata scartata: il testo della clausola
  e' riportato integralmente (nessuna elisione, ADR-0010).
- 4.8.2 Additional types -> 1 Obbligo "tecnico/sicurezza". Sottoclausta senza
  requisiti numerati propri, composta da nove periodi indipendenti, tutti
  nella forma "The X type shall be as defined in <standard>": restano un solo
  nodo (la sottoclausta e' l'unita' numerata; spezzarla per periodo
  inventerebbe item di indice non numerati dal testo).
- 4.9 Attributes -> 1 Principio "definitorio". La sottoclausta e' dichiarativa
  e non prescrive comportamenti propri: (a) rinvia alla clausola 5 per i
  dettagli sugli attributi CMS/ESS e per i nuovi attributi CAdES; (b) definisce
  la distinzione fra attributi firmati e non firmati e chi li aggiunge
  (firmatario, verificatore, altre parti) senza imporre loro alcunche'; (c)
  dichiara dove sono memorizzati (signedAttrs/unsignedAttrs di SignerInfo) e
  che i signedAttrs sono DER encoded, richiamando le clausole 4.6 e 4.7.1. E'
  lo stesso trattamento riservato alle clausole "Description"/"Introduction"
  degli altri standard ETSI censiti. Se in futuro servisse un nodo
  prescrittivo per il formato degli attributi, la fonte e' la clausola 5
  (capitolo 3 di questa fonte), non 4.9.

Obbligo/Principio e soggetti: nessuna riga di questo capitolo porta
`soggetti`. Le prescrizioni della clausola 4 sono rivolte alle "CAdES
signatures" e ai tipi ASN.1 (conformazione del formato), mai a un soggetto
nominato nel testo ("il firmatario", "il prestatore", "la parte che verifica"):
l'unico riferimento a persone compare in 4.9 ("the signer, the verifier or
other parties") in forma descrittiva, dentro un nodo che e' Principio. Non
sono state attribuite categorie di soggetto per inferenza: la categoria va
messa solo se il testo la nomina (stesso criterio delle altre fonti ETSI,
dove le righe senza soggetto nominato restano senza `soggetti`).
`oggetti_giuridici` non valorizzati: il testo nomina CAdES e i tipi CMS, non
un oggetto giuridico eIDAS (firma elettronica avanzata, documento elettronico,
...), che sarebbe un'inferenza.

Normalizzazione di resa: il marcatore di elenco puntato della NOTE 2 di 4.5 e'
estratto da pdftotext come U+F0A7 (glifo del font Symbol, non un carattere
Unicode testuale): e' reso con "•" come negli altri moduli ETSI censiti (es.
ETSI TS 119 101). Nessun'altra alterazione: le righe spezzate dal PDF sono
ricucite, le parole sono quelle del testo ufficiale, nessun marcatore di
elisione e' stato introdotto (verificato: il capitolo non contiene alcun
"..." o "…" nel testo ufficiale).

Esclusioni (paratesto, non clausole): l'intestazione "4 General syntax" e le
intestazioni di puro raggruppamento "4.7 ASN.1 Encoding" e "4.8 Other standard
data structures" non generano nodo, perche' non hanno periodo proprio e sono
seguite immediatamente dalla prima sottoclausta (stesso criterio applicato a
6/6.2/6.2.1 e B.1 di ETSI TS 119 612). Sono escluse le righe di testatina e
piede pagina della conversione PDF ("ETSI", "13 ETSI EN 319 122-1 V1.3.1
(2023-06)", "14 ..."), che sono paratesto di impaginazione e non testo
normativo. Nessun'altra parte del capitolo e' stata scartata: front matter,
Contents, Foreword e History dello standard sono fuori dal perimetro di questo
modulo (non presenti in cap02.txt).

Rinvii demandati alla fase 6 (nessuna relazione creata verso di essi: ADR-0009
e ADR-0012, le partizioni "clausola 4" e "clausola 5" esistono apposta per
questi archi):
- 4.1 -> "clausola 5.1" (capitolo 3 di questa fonte, ETSI EN 319 122-1):
  "by incorporation of signed and unsigned attributes as defined in clause
  5.1" e "The following clauses list the types that are used in the attributes
  described in clause 5.1";
- 4.9 -> "clausola 5" (capitolo 3): "Clause 5 provides details on attributes
  specified within CMS ..., ESS ... and defines new attributes for building
  CAdES signatures";
- 4.1 -> clausole 4.2-4.9 di questo stesso capitolo: "The following clauses
  list the types that are used in the attributes described in clause 5.1"
  rinvia in blocco alle sottoclauste seguenti senza nominarne una in
  particolare. Non e' stato creato alcun arco verso l'insieme (le relazioni del
  censimento collegano unita' singole, e un arco verso un raggruppamento non
  numerato sarebbe un bersaglio inventato): il rinvio resta annotato qui;
- rinvii a standard esterni non censiti nel grafo o non collegabili in questa
  fase (annotati, non trasformati in archi): IETF RFC 5652 [7] (CMS, clausole
  2-5 e 11.x), IETF RFC 3161 [4] e IETF RFC 5816 [9] (marche temporali), IETF
  RFC 5755 [8] (AttributeCertificate), IETF RFC 6960 [14] (OCSP), IETF RFC
  5280 [6] (Name, Certificate, AlgorithmIdentifier, Attribute, CertificateList),
  IETF RFC 2634 [3] e IETF RFC 5035 [5] (ESS), ITU-T X.680 [16], X.690 [17],
  X.520 [15], X.501 [i.17], X.509 [i.18], ETSI EN 319 422 [i.9] (profilo delle
  marche temporali).

RELAZIONI interne a questo modulo (2, entrambe "richiama", entrambe con
riscontro testuale letterale e puntuale nel `testo_integrale` del nodo
citante; `confidence` None perche' nessuna estrazione LLM ha prodotto uno
score, coerente con ADR-0005):
- 4.9 -> "clausola 4.6 (The SignerInfo type)": "Signed and unsigned attributes
  are stored, respectively, in the signedAttrs and unsignedAttrs fields of
  SignerInfo (see clause 4.6)".
- 4.9 -> "clausola 4.7.1 (DER)": NOTE di 4.9, "The signedAttrs fields of the
  SignerInfo are DER encoded (see clause 4.7.1) as stated in IETF RFC 5652
  [7], clause 5.3".

Verifica di copertura incrociata eseguita in fase di scrittura: ogni riga non
di intestazione del capitolo (escluse testatine e piedi di pagina) e'
contenuta verbatim in un `testo_integrale` di questo modulo, e ogni frammento
riportato e' stato ritrovato nel testo ufficiale dopo la ricucitura delle righe
spezzate dal PDF.

Conteggio di copertura: 11 item di indice, 11 righe (10 Obblighi + 1
Principio), 2 relazioni interne. MAPPATURA_LOCALE mappa ogni item su se
stesso: nessun accorpamento, nessun item coperto da piu' righe.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 4.1 (General requirements)",
        "testo": (
            "Le firme CAdES devono fondarsi su CMS (IETF RFC 5652 [7]) mediante incorporazione "
            "degli attributi firmati e non firmati definiti nella clausola 5.1, e devono essere "
            "conformi alle clausole 2, 3, 4 e 5 di IETF RFC 5652 [7]. Le clausole seguenti elencano "
            "i tipi usati negli attributi descritti nella clausola 5.1."
        ),
        "testo_integrale": (
            "4.1 General requirements: CAdES signatures shall build on Cryptographic Message Syntax "
            "(CMS), as defined in IETF RFC 5652 [7], by incorporation of signed and unsigned "
            "attributes as defined in clause 5.1.\n"
            "CAdES signatures shall comply with clauses 2, 3, 4 and 5 of IETF RFC 5652 [7].\n"
            "The following clauses list the types that are used in the attributes described in "
            "clause 5.1."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.2 (The data content type)",
        "testo": (
            "Il tipo di contenuto data deve essere quello definito in CMS (IETF RFC 5652 [7], "
            "clausola 4) e serve a riferirsi a stringhe di ottetti arbitrarie. La NOTE riporta "
            "l'object identifier id-data con cui il tipo e' identificato."
        ),
        "testo_integrale": (
            "4.2 The data content type: The data content type shall be as defined in CMS (IETF RFC "
            "5652 [7], clause 4). It is used to refer to arbitrary octet strings.\n"
            "NOTE: The data content type is identified by the object identifier id-data OBJECT "
            "IDENTIFIER ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs7(7) 1 }."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3 (The signed-data content type)",
        "testo": (
            "Il tipo di contenuto signed-data deve essere quello definito in CMS (IETF RFC 5652 [7], "
            "clausola 5); rappresenta il contenuto da firmare e uno o piu' valori di firma."
        ),
        "testo_integrale": (
            "4.3 The signed-data content type: The signed-data content type shall be as defined in "
            "CMS (IETF RFC 5652 [7], clause 5). It represents the content to sign and one or more "
            "signature values."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.4 (The SignedData type)",
        "testo": (
            "Il tipo SignedData deve essere quello definito in CMS (IETF RFC 5652 [7], clausola 5.1) "
            "e la CMSVersion va impostata come specificato nella clausola 5.1 di IETF RFC 5652 [7]. "
            "La clausola fissa anche la notazione SignedData.xxx / SignedData.xxx.yyy usata nel "
            "documento per riferirsi agli elementi del tipo, e la NOTE riassume quando la versione "
            "CMS deve essere 3 e quando 1."
        ),
        "testo_integrale": (
            "4.4 The SignedData type: The SignedData type shall be as defined in CMS (IETF RFC 5652 "
            "[7], clause 5.1). The CMSVersion shall be set as specified in clause 5.1 of IETF RFC "
            "5652 [7].\n"
            "SignedData.xxx refers to the element xxx within the SignedData type, like for example "
            "SignedData.certificates, or SignedData.crls. In the same way, if xxx is of type XXX, "
            "SignedData.xxx.yyy is used to refer to the element yyy of type XXX, like for example "
            "SignedData.crls.crl or SignedData.crls.other.\n"
            "NOTE: Clause 5.1 of IETF RFC 5652 [7] requires that the CMS SignedData version be set "
            "to 3 if certificates from SignedData is present AND (any version 1 attribute "
            "certificates are present OR any SignerInfo structures are version 3 OR eContentType "
            "from encapContentInfo is other than id-data). Otherwise, the CMS SignedData version is "
            "required to be set to 1."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.5 (The EncapsulatedContentInfo type)",
        "testo": (
            "Il tipo EncapsulatedContentInfo deve essere quello definito in CMS (IETF RFC 5652 [7], "
            "clausola 5.2). Ai fini della validazione di lungo termine l'eContent dovrebbe essere "
            "presente, oppure i dati firmati dovrebbero essere archiviati in modo da preservare la "
            "codifica dei dati. Le NOTE 1 e 2 spiegano perche' l'OCTET STRING usato per generare la "
            "firma deve restare identico e cosa comportano la presenza o l'assenza dell'eContent."
        ),
        "testo_integrale": (
            "4.5 The EncapsulatedContentInfo type: The EncapsulatedContentInfo type shall be as "
            "defined in CMS (IETF RFC 5652 [7], clause 5.2).\n"
            "For the purpose of long-term validation, either the eContent should be present, or the "
            "data that is signed should be archived in such a way as to preserve any data "
            "encoding.\n"
            "NOTE 1: It is important that the OCTET STRING used to generate the signature remains "
            "the same every time either the verifier or an arbitrator validates the signature.\n"
            "NOTE 2: The eContent is optional in CMS:\n"
            "• When it is present, this allows the signed data to be encapsulated in the SignedData "
            "structure which then contains both the signed data and the signature. However, the "
            "signed data can only be accessed by a verifier able to decode the ASN.1 encoded "
            "SignedData structure.\n"
            "• When it is missing, this allows the signed data to be sent or stored separately from "
            "the signature, and the SignedData structure only contains the signature. Under these "
            "circumstances, the data object that is signed needs to be stored and distributed in "
            "such a way as to preserve any data encoding."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.6 (The SignerInfo type)",
        "testo": (
            "Il tipo SignerInfo della firma digitale deve essere quello definito in CMS (IETF RFC "
            "5652 [7], clausola 5.3). Le informazioni per firmatario sono rappresentate nel tipo "
            "SignerInfo: in caso di firme parallele multiple c'e' una istanza di questo campo per "
            "ciascun firmatario, e il caso degenere in cui non vi sono firmatari non deve essere "
            "usato."
        ),
        "testo_integrale": (
            "4.6 The SignerInfo type: The SignerInfo type of the digital signature shall be as "
            "defined in CMS (IETF RFC 5652 [7], clause 5.3).\n"
            "The per-signer information is represented in the type SignerInfo. In the case of "
            "multiple parallel signatures, there is one instance of this field for each signer.\n"
            "The degenerate case where there are no signers shall not be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.7.1 (DER)",
        "testo": (
            "Le Distinguished Encoding Rules (DER) per i tipi ASN.1 devono essere quelle definite "
            "nella Raccomandazione ITU-T X.690 [17]."
        ),
        "testo_integrale": (
            "4.7.1 DER: Distinguished Encoding Rules (DER) for ASN.1 types shall be as defined in "
            "Recommendation ITU-T X.690 [17]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.7.2 (BER)",
        "testo": (
            "Se per alcuni tipi ASN.1 si usano le Basic Encoding Rules (BER), esse devono essere "
            "quelle definite nella Raccomandazione ITU-T X.690 [17]."
        ),
        "testo_integrale": (
            "4.7.2 BER: If Basic Encoding Rules (BER) are used for some ASN.1 types, it shall be as "
            "defined in Recommendation ITU-T X.690 [17]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.8.1 (Time-stamp token format)",
        "testo": (
            "Il tipo TimeStampToken deve essere quello definito in IETF RFC 3161 [4] e aggiornato da "
            "IETF RFC 5816 [9]; la NOTE rinvia al profilo delle marche temporali in ETSI EN 319 422 "
            "[i.9]."
        ),
        "testo_integrale": (
            "4.8.1 Time-stamp token format: The TimeStampToken type shall be as defined in IETF RFC "
            "3161 [4] and updated by IETF RFC 5816 [9].\n"
            "NOTE: Time-stamp tokens are profiled in ETSI EN 319 422 [i.9]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.8.2 (Additional types)",
        "testo": (
            "I tipi aggiuntivi usati da CAdES - VisibleString, BMPString, IA5String, GeneralizedTime "
            "e UTCTime, DirectoryString, AttributeCertificate, ResponderID, OCSPResponse e "
            "BasicOCSPResponse, Name, Certificate e AlgorithmIdentifier, Attribute, CertificateList, "
            "RevocationInfoChoices - devono essere quelli definiti nelle rispettive Raccomandazioni "
            "ITU-T e RFC IETF indicate nella clausola, con la compatibilita' dichiarata verso X.509 "
            "[i.18] per AttributeCertificate e CertificateList e verso X.501 [i.17] per Attribute."
        ),
        "testo_integrale": (
            "4.8.2 Additional types: The VisibleString, BMPString, IA5String, GeneralizedTime and "
            "UTCTime types shall be as defined in Recommendation ITU-T X.680 [16].\n"
            "The DirectoryString type shall be as defined in Recommendation ITU-T X.520 [15].\n"
            "The AttributeCertificate type shall be as defined in IETF RFC 5755 [8] which is "
            "compatible with the definition in Recommendation ITU-T X.509 [i.18].\n"
            "The ResponderID, OCSPResponse and BasicOCSPResponse types shall be as defined in IETF "
            "RFC 6960 [14].\n"
            "The Name, Certificate and AlgorithmIdentifier types shall be as defined in IETF RFC "
            "5280 [6].\n"
            "The Attribute type shall be as defined in IETF RFC 5280 [6] which is compatible with "
            "the definition in Recommendation ITU-T X.501 [i.17].\n"
            "The CertificateList type shall be as defined in IETF RFC 5280 [6] which is compatible "
            "with the X.509 v2 CRL syntax in Recommendation ITU-T X.509 [i.18].\n"
            "The RevocationInfoChoices type shall be as defined in IETF RFC 5652 [7]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 4.9 (Attributes)",
        "testo": (
            "La clausola dichiara che la clausola 5 detta i dettagli sugli attributi specificati in "
            "CMS (IETF RFC 5652 [7]) ed ESS (IETF RFC 2634 [3] e IETF RFC 5035 [5]) e definisce i "
            "nuovi attributi per costruire firme CAdES, e distingue i due tipi principali di "
            "attributi: quelli firmati, coperti dal valore di firma prodotto dal firmatario con la "
            "propria chiave privata, e quelli non firmati, aggiunti dal firmatario, dal verificatore "
            "o da altre parti dopo la produzione della firma e non protetti dalla firma nel "
            "SignerInfo, ma potenzialmente coperti da marche temporali successive. Attributi firmati "
            "e non firmati sono memorizzati rispettivamente nei campi signedAttrs e unsignedAttrs di "
            "SignerInfo (clausola 4.6), e i signedAttrs sono codificati in DER (clausola 4.7.1)."
        ),
        "testo_integrale": (
            "4.9 Attributes: Clause 5 provides details on attributes specified within CMS (IETF RFC "
            "5652 [7]), ESS (IETF RFC 2634 [3] and IETF RFC 5035 [5]), and defines new attributes "
            "for building CAdES signatures.\n"
            "The clause distinguishes between two main types of attributes: signed attributes and "
            "unsigned attributes. The first ones are attributes that are covered by the digital "
            "signature value produced by the signer using his/her private key, which implies that "
            "the signer has processed these attributes before creating the signature. The unsigned "
            "attributes are added by the signer, by the verifier or by other parties after the "
            "production of the signature. They are not secured by the signature in the SignerInfo "
            "element (the one computed by the signer); however they can be actually covered by "
            "subsequent times-stamp attributes.\n"
            "Signed and unsigned attributes are stored, respectively, in the signedAttrs and "
            "unsignedAttrs fields of SignerInfo (see clause 4.6).\n"
            "NOTE: The signedAttrs fields of the SignerInfo are DER encoded (see clause 4.7.1) as "
            "stated in IETF RFC 5652 [7], clause 5.3."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 4.1 (General requirements)",
    "clausola 4.2 (The data content type)",
    "clausola 4.3 (The signed-data content type)",
    "clausola 4.4 (The SignedData type)",
    "clausola 4.5 (The EncapsulatedContentInfo type)",
    "clausola 4.6 (The SignerInfo type)",
    "clausola 4.7.1 (DER)",
    "clausola 4.7.2 (BER)",
    "clausola 4.8.1 (Time-stamp token format)",
    "clausola 4.8.2 (Additional types)",
    "clausola 4.9 (Attributes)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Relazioni interne al capitolo (bersagli verificabili in questo stesso file):
# le due citazioni letterali di 4.9 alle clausole 4.6 e 4.7.1. I rinvii alla
# clausola 5 (capitolo 3 di questa Fonte) e alle clausole di IETF RFC 5652
# sono demandati alla fase 6 (ADR-0009/ADR-0012) e non diventano archi qui.
RELAZIONI: list[dict] = [
    {
        "nodo_da": ("principio", None, "clausola 4.9 (Attributes)"),
        "nodo_a": ("obbligo", None, "clausola 4.6 (The SignerInfo type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "clausola 4.9 (Attributes)"),
        "nodo_a": ("obbligo", None, "clausola 4.7.1 (DER)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
