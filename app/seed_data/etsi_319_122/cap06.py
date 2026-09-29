"""ETSI EN 319 122-1 V1.3.1 (2023-06) - Electronic Signatures and Trust
Infrastructures (ESI); CAdES digital signatures; Part 1: Building blocks and
CAdES baseline signatures. Capitolo 6 dello split: Annex D (normative)
"Signature Format Definitions Using X.680 ASN.1 Syntax", cioe' i due moduli
ASN.1 dell'annex con gli object identifier degli attributi CAdES e le
definizioni dei tipi che li portano. Fonte del blocco B (famiglia AdES del
lotto 2); la numerazione definitiva della fonte e' cablata dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py, non importa
nulla e non legge file: e' puro dato.

Provenienza del testo
---------------------
- testo ufficiale: ETSI EN 319 122-1 V1.3.1 (2023-06), deliver "01.03.01_60".
- file di capitolo: app/.source_cache/etsi_319_122/cap06.txt (570 righe: pagine
  50-57 del PDF), porzione della conversione PDF (pdftotext -layout) di
  app/.source_cache/etsi_319_122/raw.pdf. Ogni blocco di testo_integrale di
  questo modulo e' stato estratto per intervallo di riga dal file di capitolo
  (mai ritrascritto a mano) e verificato per contenimento letterale sul testo
  sorgente dopo normalizzazione degli spazi e rimozione del paratesto di
  pagina.
- metadati da app/.source_cache/etsi_319_122/manifest.json e
  app/.source_cache/etsi_319_122/provenance.json: url
  https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf,
  versione "01.03.01_60", data_fetch 2026-09-29T12:56:34Z, sha256_raw_pdf
  e99e76e519d9bd8e1410775bccedb1a588021e5e7c705c9fcc1f91c6a6227c21,
  formato "PDF ETSI deliver (pdftotext -layout)". Il capitolo occupa le pagine
  50-57; ogni pagina porta come paratesto le righe "ETSI" e
  "<numero> ETSI EN 319 122-1 V1.3.1 (2023-06)", rimosse da testo_integrale
  (mai contenuto normativo) e ricucendo l'ASN.1 interrotto dal salto di pagina
  (es. la coda di IMPORTS ... FROM PKIXTSP, interrotta fra pagina 50 e 51).

Perimetro del capitolo
----------------------
Il file copre l'intero Annex D, dal titolo "Annex D (normative): Signature
Format Definitions Using X.680 ASN.1 Syntax" all'ultimo "END" del secondo
modulo ASN.1 (pagina 57). Non contiene front matter, Contents, Foreword ne'
History: nel file non c'e' nulla di quel paratesto da escludere, il capitolo
inizia direttamente con il titolo dell'annex. I due moduli dell'annex sono:
- ETSI-CAdES-ExplicitSyntax97 { ... id-mod(0) cades-explicit97(1) }, che
  definisce gli arc degli OID e, per ogni attributo CAdES censito, l'OID
  dell'attributo e i tipi che lo compongono, ciascuno preceduto dal commento
  ASN.1 "-- <nome attributo> (clause X.Y.Z)" che lo lega alla clausola del
  corpo che lo descrive;
- ETSI-CAdES-19122v121 { ... id-mod(0) cades-19122v121(2) }, aggiunto nella
  V1.2.1, che importa l'attributo di protezione degli algoritmi CMS (IETF RFC
  6211) e definisce l'arc delle signed assertions e l'OID della
  signed-SAML-assertion.

Granularita' (ADR-0007, nessun discrimine di rilevanza)
------------------------------------------------------
L'Annex D non numera proprie sottoclauste (nessun D.1, D.2, ...): la sua
struttura e' quella dei due moduli ASN.1, e ogni blocco di definizione e'
introdotto da un commento "--" che nomina l'attributo (o l'arc) e la clausola
del corpo a cui corrisponde. Unita' di prescrizione adottata: il blocco
introdotto da un commento, cioe' un attributo censito = una riga (un OID di
attributo = una riga), come da assegnazione del perimetro. Bilancio: 31 item
di indice e 31 righe, mappatura 1:1.

Criterio Obbligo/Principio applicato in questo capitolo
------------------------------------------------------
Le definizioni ASN.1 dell'annex sono dichiarative: fissano l'object identifier
e la sintassi dei tipi, senza imporre comportamenti a un soggetto; il
contenuto prescrittivo per attributo e' nella clausola del corpo che il
commento ASN.1 richiama, gia' censita come Obbligo "tecnico/sicurezza" in
app/seed_data/etsi_319_122/cap03.py. Di conseguenza le 30 righe di
definizione sono Principi "definitorio" - stesso trattamento gia' riservato al
modulo ASN.1 di Annex B di ETSI EN 319 422 (cap04 di quella fonte) e di Annex
B di ETSI EN 319 412-5 (parte5).
Unica eccezione, la premessa dell'annex: contiene due "shall" che prescrivono
la sintassi di interpretazione dei moduli e le importazioni ammesse, quindi e'
modellata come Obbligo "tecnico/sicurezza" (rinvio per valore, non
descrizione: coerente con la classificazione gia' data in cap03 alle clausole
il cui contenuto e' "shall be as defined in ...").
Nessuna riga di questo capitolo e' "organizzativo", "informativo/trasparenza",
"procedurale", "di conservazione" o "sanzionatorio": sono tutte definizioni di
formato e codifica -> "tecnico/sicurezza" per l'unico Obbligo e "definitorio"
per i Principi.
`soggetti`/`oggetti_giuridici` restano vuoti su tutte le righe: il testo non
nomina mai un soggetto obbligato (parla di moduli, attributi, tipi e OID) ne'
un oggetto giuridico (definisce identificatori e sintassi, non situazioni
giuridiche; stesso criterio di Annex C di ETSI EN 319 422).

Decisioni di modellazione, voce per voce (31 righe)
--------------------------------------------------
- premessa dell'annex (righe 1-10) -> 1 Obbligo "tecnico/sicurezza", senza
  soggetti. Tre prescrizioni/dichiarazioni in un'unica unita' indivisa: (a)
  "In case of discrepancy in the ASN.1 definitions between the previous clauses
  and this annex, this annex takes precedence" - dichiarativa, fissa la
  precedenza dell'annex sulle definizioni ASN.1 delle clausole precedenti
  (quelle copiate per informazione in clausola 5, cap03 di questa fonte); (b)
  "The following ASN.1 modules shall be interpreted using the syntax defined in
  Recommendation ITU-T X.680 [16]"; (c) "The ASN.1 modules defined in this
  clause shall import the types and structures from IETF RFC 6268 [12], IETF
  RFC 5911 [10], IETF RFC 5912 [11], IETF RFC 6960 [14] and IETF RFC 3161 [4]
  as written in the import part of the module". (b) e (c) impongono un
  comportamento verificabile (sintassi X.680; elenco chiuso di importazioni),
  quindi il nodo e' un Obbligo e non un Principio, nonostante la frase (a) sia
  dichiarativa: separare la frase (a) in un nodo a se' avrebbe creato un nodo
  per una singola frase priva di unita' di indice propria, dentro una premessa
  non numerata. Il titolo dell'annex ("Annex D (normative): Signature Format
  Definitions Using X.680 ASN.1 Syntax") e' riportato in testa al
  testo_integrale di questa riga, come per Annex B di ETSI EN 319 422.
- intestazione del primo modulo ASN.1 (righe 11-88) -> 1 Principio
  "definitorio": nome del modulo e suo OID, "DEFINITIONS EXPLICIT TAGS",
  "EXPORTS All" e la lista IMPORTS completa (CMS/PKIX da IETF RFC 6268, ESS da
  RFC 5911, PKIX1Explicit-2009 e PKIX1Implicit-2009 da RFC 5912,
  PKIXAttributeCertificate-2009, OCSP-2013-08 da RFC 6960, PKIXTSP da RFC 3161,
  DirectoryString{} da SelectedAttributeTypes X.520). E' struttura di modulo,
  non prescrizione propria: la prescrizione di importare e' nella premessa.
  Alternativa scartata: assorbirla nella riga della premessa (un solo nodo per
  tutto il front matter del primo modulo). Avrebbe fatto sparire dal grafo le
  importazioni, che sono proprio il contenuto che la premessa rende
  prescrittivo ("as written in the import part of the module"), e avrebbe
  prodotto un nodo di oltre 80 righe con dentro prosa, intestazione di modulo e
  lista di importazioni; stesso criterio per l'intestazione del secondo modulo
  (riga "modulo ETSI-CAdES-19122v121").
- quattro arc di OID della sezione "Definitions of Object Identifier arcs used
  in the present document" (id-etsi-es-attributes, id-etsi-cades-attributes,
  id-etsi-cades-spq, id-etsi-cades-mod) -> 4 Principi "definitorio", una riga
  per ciascun arc: ognuno ha un commento proprio che ne dichiara l'uso e
  ognuno e' un OID distinto (assegnazione "ogni attributo/OID censito ha una
  riga"). Ogni riga porta il commento ufficiale piu' la definizione.
- 22 attributi del primo modulo -> 22 Principi "definitorio", uno per
  attributo con OID proprio: commitment-type (id-aa-ets-commitmentType, clause
  5.2.3), mime-type (id-aa-ets-mimeType, 5.2.4.2), signer-location
  (id-aa-ets-signerLocation, 5.2.5), signer-attributes-v2
  (id-aa-ets-signerAttrV2, 5.2.6.1), claimed-SAML-assertion
  (id-aa-ets-claimedSAML, 5.2.6.2), content-timestamp
  (id-aa-ets-contentTimestamp, 5.2.8), signature-policy-identifier
  (id-aa-ets-sigPolicyId, 5.2.9.1), spuri (id-spq-ets-uri, 5.2.9.2),
  sp-user-notice (id-spq-ets-unotice, 5.2.9.2), sp-doc-specification
  (id-spq-ets-docspec, 5.2.9.2), signature-policy-store
  (id-aa-ets-sigPolicyStore, 5.2.10), signature-timestamp
  (id-aa-signatureTimeStampToken, 5.3), ats-hash-index-v3
  (id-aa-ATSHashIndex-v3, 5.5.2), archive-time-stamp-v3
  (id-aa-ets-archiveTimestampV3, 5.5.3), complete-certificate-references
  (id-aa-ets-certificateRefs, A.1.1.1), certificate-values
  (id-aa-ets-certValues, A.1.1.2), complete-revocation-references
  (id-aa-ets-revocationRefs, A.1.2.1), certificate-revocation-values
  (id-aa-ets-revocationValues, A.1.2.2), attribute-certificate-references
  (id-aa-ets-attrCertificateRefs, A.1.3), attribute-revocation-references
  (id-aa-ets-attrRevocationRefs, A.1.4), time-stamped-certs-crls-references
  (id-aa-ets-certCRLTimestamp, A.1.5.1), CAdES-C-timestamp
  (id-aa-ets-escTimeStamp, A.1.5.2). Per ciascuno, testo_integrale = commento
  "-- <attributo> (clause X)" piu' l'OID e tutti i tipi definiti in quel
  blocco, ASN.1 riportato con l'impaginazione originale del PDF.
- i tre qualificatori di signature policy sono tre righe distinte (e non una
  per il blocco "-- Signature policy qualifiers types (clause 5.2.9.2)" che li
  raggruppa) perche' sono tre OID diversi e sono referenziati uno per uno
  dalla lista SupportedSigPolicyQualifiers del blocco signature-policy-identifier;
  il commento di raggruppamento resta fuori da testo_integrale (v. Esclusioni).
- signature-policy-identifier (righe 227-285) e' il blocco piu' esteso del
  modulo (15 tipi, dalla classe SIG-POLICY-QUALIFIER ai valori noticeToUser,
  pointerToSigPolSpec e sigPolDocSpecification): resta un solo nodo perche'
  ha un solo OID di attributo e un solo commento ufficiale, e i tipi che
  definisce sono usati dentro lo stesso blocco.
- tipo OCTET STRING di claimed-SAML-assertion e signed-SAML-assertion: la
  grafia del testo ufficiale e' "ClaimedSAMLAssertion ::= OCTET STRING" e
  "SignedSAMLAssertion ::= OCTET      STRING" (spazi multipli compresi),
  riportata verbatim come nel PDF.
- "END" che chiude i due moduli: nessun nodo proprio (e' sintassi di modulo,
  non contenuto), riportato in coda al testo_integrale dell'ultimo blocco del
  modulo (CAdES-C-timestamp per il primo modulo, signed-SAML-assertion per il
  secondo) con la riga vuota che lo separa nel testo ufficiale. Stesso
  trattamento gia' applicato al modulo ASN.1 di Annex B di ETSI EN 319 412-5.
- "The following module was added in V1.2.1." (riga 529) -> nessun nodo
  proprio: e' la frase che introduce il secondo modulo, ed e' assorbita in
  testa al testo_integrale della riga "modulo ETSI-CAdES-19122v121".
- id-etsi-cades-spq nel secondo modulo (righe 548-550) -> riga distinta da
  id-etsi-cades-spq del primo modulo, perche' il testo ufficiale riusa lo
  stesso nome con valore diverso (signed-assertions(3) invece di id-spq(2)):
  due definizioni diverse, due riferimenti di riga distinti (il riferimento di
  riga e' la chiave del registro di lib.py, quindi non puo' essere duplicato).
  E' un refuso dello standard, riportato verbatim e non emendato in un modulo
  dati; la riga lo dichiara nel proprio `testo`.

Esclusioni (cosa non e' stato censito e perche')
-----------------------------------------------
Nessuna riga di contenuto normativo e' esclusa: tutti i blocchi di definizione
del capitolo sono coperti. Restano fuori solo:
- i cinque commenti ASN.1 di solo raggruppamento, che non hanno testo proprio ma
  solo la funzione di separatore di sezione: "-- Definitions of Object
  Identifier arcs used in the present document" con la riga di "=" che lo
  sottolinea (righe 90-91), "-- Attributes for basic CAdES signatures" con la
  riga di "=" (111-112), "-- Signature policy qualifiers types (clause
  5.2.9.2)" (288), "-- Archive validation data" con la riga di "=" (356-357),
  "-- Additional attributes for validation data" con la riga di "=" (379-380).
  Stesso criterio gia' applicato alle intestazioni di solo raggruppamento
  delle altre fonti ETSI censite (ETSI EN 319 422 clausola 9 e relative
  intestazioni, ETSI EN 319 122-1 clausola 6 in cap04 di questa fonte): un
  commento di sezione non e' una clausola, non ha numerazione ne' contenuto, e
  il suo contenuto informativo (il legame con la clausola 5.2.9.2) e' portato
  dai tre riferimenti di riga dei qualificatori.
- il paratesto di pagina ("ETSI", "<numero> ETSI EN 319 122-1 V1.3.1
  (2023-06)") e le righe vuote di impaginazione, non contenuto normativo.
Nessuna front matter, Contents, Foreword, History o tabella di soli
riferimenti bibliografici cade in questo capitolo. Non esiste in Annex D alcun
EXAMPLE ne' nota NOTE: il testo e' composto da prosa introduttiva, ASN.1 e
commenti ASN.1, tutti riportati integralmente.

Relazioni interne dichiarate (9, tutte "richiama", tutte `textual`)
------------------------------------------------------------------
Sono i riferimenti interni fra blocchi del modulo (citazione letterale di un
identificatore definito in un altro blocco di questo stesso file, verificata
dentro il testo_integrale del nodo citante):
- signature-policy-identifier -> spuri, sp-user-notice, sp-doc-specification:
  i tre valori noticeToUser / pointerToSigPolSpec / sigPolDocSpecification
  usano SIG-POLICY-QUALIFIER-ID id-spq-ets-uri, id-spq-ets-unotice e
  id-spq-ets-docspec, definiti nei tre blocchi successivi.
- signature-policy-store -> sp-doc-specification: il campo spDocSpec di
  SignaturePolicyStore e' di tipo SPDocSpecification.
- complete-certificate-references -> signature-policy-identifier: il tipo
  OtherHash di questo blocco sceglie OtherHashValue o OtherHashAlgAndValue,
  definiti in quest'ultimo blocco.
- complete-revocation-references -> complete-certificate-references: il campo
  otherCertHash/crlHash/ocspRefHash e' di tipo OtherHash.
- certificate-revocation-values -> complete-revocation-references: il campo
  otherRevVals di OtherRevVals e' dichiarato come "SEQUENCE OF
  OTHER-REVOCATION-REF.&Type", e OTHER-REVOCATION-REF e' la classe definita
  nel blocco complete-revocation-references (il testo ufficiale scrive
  OTHER-REVOCATION-REF anche nel blocco certificate-revocation-values, dove la
  classe definita e' OTHER-REVOCATION-VAL: evidente refuso dello standard,
  riportato verbatim e non emendato; la relazione documenta la citazione
  letterale, non l'intenzione).
- attribute-certificate-references -> complete-certificate-references:
  AttributeCertificateRefs e' una sequenza di OtherCertID.
- attribute-revocation-references -> complete-revocation-references:
  AttributeRevocationRefs e' una sequenza di CrlOcspRef.
Nessuna relazione verso altri capitoli di questa fonte o verso altre fonti:
quei rinvii sono elencati qui sotto e restano alla fase 6 (ADR-0012).

Rinvii demandati alla fase 6 (nessuna relazione dichiarata qui)
--------------------------------------------------------------
- I commenti "-- <attributo> (clause X.Y.Z)" di ogni blocco rinviano alla
  clausola del corpo che descrive l'attributo: clausole 5.2.3, 5.2.4.2, 5.2.5,
  5.2.6.1, 5.2.6.2, 5.2.8, 5.2.9.1, 5.2.9.2, 5.2.10, 5.3, 5.5.2, 5.5.3 ->
  nodi di app/seed_data/etsi_319_122/cap03.py (stessa fonte, altro capitolo).
- I commenti dei blocchi dei dati di validazione rinviano alle clausole
  A.1.1.1, A.1.1.2, A.1.2.1, A.1.2.2, A.1.3, A.1.4, A.1.5.1, A.1.5.2 ->
  Annex A della stessa fonte (cap05 dello split, non ancora censito al momento
  della scrittura di questo modulo: le partizioni "Annex A ..." esistono solo
  quando quelle righe saranno inserite).
- La premessa stabilisce la precedenza dell'annex sulle definizioni ASN.1
  "copied here for information" nelle clausole del corpo (5.2.6.1, 5.2.9.1,
  5.2.9.2, 5.5.2 in cap03): relazione di precedenza demandata alla fase 6
  (bersaglio in un altro capitolo).
- Le clausole 4.x e 6 di questa fonte (cap02 e cap04) rinviano ad annex D per
  le definizioni dei formati di firma: stessa sorte.
- Importazioni e fonti esterne citate nel capitolo (IETF RFC 6268, 5911, 5912,
  6960, 3161, 6211; SelectedAttributeTypes di ITU-T X.520; la sintassi di
  ITU-T X.680; la parametrizzazione di X.683): nessuna di queste specifiche e'
  una Fonte censita, quindi nessun nodo bersaglio esiste e nessuna relazione
  cross-fonte e' dichiarata.

Conteggio di copertura
----------------------
31 item di indice, 31 righe: 1 obbligo + 30 principi; 9 relazioni interne.
"""
RIGHE_OBBLIGHI = [
    {
        "riferimento": "Annex D (normative), premessa (precedenza dei moduli ASN.1 e sintassi di interpretazione)",
        "testo": (
            "Il testo ASN.1 dell'Annex D prevale sulle definizioni ASN.1 riportate nelle clausole "
            "precedenti in caso di discrepanza; i moduli ASN.1 dell'annex devono essere interpretati "
            "con la sintassi della Raccomandazione ITU-T X.680 e devono importare i tipi e le "
            "strutture da IETF RFC 6268, RFC 5911, RFC 5912, RFC 6960 e RFC 3161 come scritto nella "
            "parte IMPORTS del modulo."
        ),
        "testo_integrale": (
            """Annex D (normative):
Signature Format Definitions Using X.680 ASN.1 Syntax
In case of discrepancy in the ASN.1 definitions between the previous clauses and this annex, this annex takes precedence.

The following ASN.1 modules shall be interpreted using the syntax defined in Recommendation ITU-T X.680 [16].

The ASN.1 modules defined in this clause shall import the types and structures from IETF RFC 6268 [12], IETF RFC 5911 [10], IETF RFC 5912 [11], IETF RFC 6960 [14] and IETF RFC 3161 [4] as written in the import part of the module."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "Annex D, modulo ETSI-CAdES-ExplicitSyntax97 (intestazione, EXPORTS e IMPORTS)",
        "testo": (
            "Intestazione del primo modulo ASN.1 dell'annex, ETSI-CAdES-ExplicitSyntax97 { itu-t(0) "
            "identified-organization(4) etsi(0) cades(19122) id-mod(0) cades-explicit97(1) }, con "
            "DEFINITIONS EXPLICIT TAGS, EXPORTS All e la lista delle importazioni: i tipi CMS e PKIX "
            "di IETF RFC 6268, RFC 5911, RFC 5912, RFC 6960 e RFC 3161 (compresi i tipi di "
            "PKIX1Implicit-2009 e PKIXAttributeCertificate-2009) e DirectoryString{} dai "
            "SelectedAttributeTypes di X.520."
        ),
        "testo_integrale": (
            """ETSI-CAdES-ExplicitSyntax97 { itu-t(0) identified-organization(4) etsi(0) cades(19122)
    id-mod(0) cades-explicit97(1)}

DEFINITIONS EXPLICIT TAGS ::=
BEGIN
-- EXPORTS All -

IMPORTS

-- Imports from Additional New ASN.1 Modules for the Cryptographic Message Syntax (CMS) and the
-- Public Key Infrastructure Using X.509 (PKIX): IETF RFC 6268
-- (update for module from Imports from Cryptographic Message Syntax (CMS): IETF RFC 5652)
        ContentInfo, ContentType, id-data, id-signedData, SignedData, EncapsulatedContentInfo,
        SignerInfo, id-contentType, id-messageDigest, MessageDigest, id-signingTime, SigningTime,
        id-countersignature, Countersignature, RevocationInfoChoices, Attribute
            FROM CryptographicMessageSyntax-2010
                { iso(1) member-body(2) us(840) rsadsi(113549)
                  pkcs(1) pkcs-9(9) smime(16) modules(0) id-mod-cms-2009(58) }

-- Imports from New ASN.1 Modules for Cryptographic Message Syntax (CMS) and S/MIME:
-- IETF RFC 5911
-- (updated for module from Enhanced Security Services (ESS) Update: Adding CertID Algorithm Agility
-- IETF RFC 5035)
        id-aa-signingCertificate, SigningCertificate, IssuerSerial, id-aa-contentReference,
        ContentReference, id-aa-contentIdentifier, ContentIdentifier, id-aa-signingCertificateV2,
        SigningCertificateV2
            FROM ExtendedSecurityServices-2009
                { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-9(9)
                  smime(16) modules(0) id-mod-ess-2006-02(42) }

-- Imports from New ASN.1 Modules for the Public Key Infrastructure Using X.509 (PKIX):
-- IETF RFC 5912
-- (updated for module from Internet X.509 Public Key Infrastructure - Certificate and CRL
-- Profile: IETF RFC 5280)
        Certificate, AlgorithmIdentifier, CertificateList, Name
            FROM PKIX1Explicit-2009
                { iso(1) identified-organization(3) dod(6) internet(1) security(5) mechanisms(5)
                  pkix(7) id-mod(0) id-mod-pkix1-explicit-02(51)}

          GeneralNames, GeneralName, PolicyInformation
              FROM PKIX1Implicit-2009
                  { iso(1) identified-organization(3) dod(6) internet(1) security(5) mechanisms(5)
                    pkix(7) id-mod(0) id-mod-pkix1-implicit-02(59)}

-- Imports from New ASN.1 Modules for the Public Key Infrastructure Using X.509 (PKIX):
-- IETF RFC 5912
-- (updated for module from Internet Attribute Certificate Profile for Authorization: IETF RFC 5755)
        AttributeCertificate
            FROM PKIXAttributeCertificate-2009
                { iso(1) identified-organization(3) dod(6) internet(1) security(5)
                  mechanisms(5) pkix(7) id-mod(0) id-mod-attribute-cert-02(47)}

-- Imports from X.509 Internet Public Key Infrastructure - Online Certificate Status Protocol – OCSP
-- IETF RFC 6960
        BasicOCSPResponse, ResponderID
            FROM OCSP-2013-08
                 { iso(1) identified-organization(3) dod(6) internet(1) security(5)
                   mechanisms(5) pkix(7) id-mod(0) id-mod-ocsp-2013-08(82) }

-- Imports from Internet X.509 Public Key Infrastructure - Time-Stamp Protocol (TSP), IETF RFC 3161
        TimeStampToken
            FROM PKIXTSP

                { iso(1) identified-organization(3) dod(6) internet(1) security(5)
                  mechanisms(5) pkix(7) id-mod(0) id-mod-tsp(13)}
-- Imports from Information technology - Open Systems Interconnection –
-- The Directory: Selected attribute types - X.520
        DirectoryString{}
            FROM SelectedAttributeTypes
                { joint-iso-itu-t ds(5) module(1) selectedAttributeTypes(5) 6 }

;"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-etsi-es-attributes (arc degli attributi definiti in TS 101 733)",
        "testo": (
            "Definisce l'object identifier arc id-etsi-es-attributes { itu-t(0) "
            "identified-organization(4) etsi(0) electronic-signature-standard (1733) attributes(2) }, "
            "sotto cui stanno gli attributi definiti per la prima volta in ETSI TS 101 733."
        ),
        "testo_integrale": (
            """-- Object Identifier arc for attributes first defined in TS 101 733
id-etsi-es-attributes OBJECT IDENTIFIER ::=
    { itu-t(0) identified-organization(4) etsi(0)
      electronic-signature-standard (1733) attributes(2) }"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-etsi-cades-attributes (arc degli attributi CAdES di EN 319 122-1)",
        "testo": (
            "Definisce l'object identifier arc id-etsi-cades-attributes { itu-t(0) "
            "identified-organization(4) etsi(0) cades(19122) attributes(1) }, sotto cui stanno gli "
            "attributi definiti per la prima volta nel presente documento."
        ),
        "testo_integrale": (
            """-- Object Identifier arc for attributes first defined in the present document
id-etsi-cades-attributes OBJECT IDENTIFIER ::=
    { itu-t(0) identified-organization(4) etsi(0) cades(19122) attributes(1) }"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-etsi-cades-spq (arc dei qualificatori di signature policy)",
        "testo": (
            "Definisce l'object identifier arc id-etsi-cades-spq { itu-t(0) "
            "identified-organization(4) etsi(0) cades(19122) id-spq(2) }, sotto cui stanno i "
            "qualificatori di signature policy definiti per la prima volta nel presente documento."
        ),
        "testo_integrale": (
            """-- Object Identifier arc for signature policy qualifier first defined in the present document
id-etsi-cades-spq OBJECT IDENTIFIER ::=
    { itu-t(0) identified-organization(4) etsi(0) cades(19122) id-spq(2) }"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-etsi-cades-mod (arc dei moduli ASN.1 di EN 319 122-1)",
        "testo": (
            "Definisce l'object identifier arc id-etsi-cades-mod { itu-t(0) "
            "identified-organization(4) etsi(0) cades(19122) id-mod(0) }, sotto cui stanno i moduli "
            "ASN.1 definiti nel presente documento."
        ),
        "testo_integrale": (
            """-- Object Identifier arc for ASN.1 modules defined in the present document
id-etsi-cades-mod OBJECT IDENTIFIER ::=
    { itu-t(0) identified-organization(4) etsi(0) cades(19122) id-mod(0) }"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-commitmentType (commitment-type attribute, clause 5.2.3)",
        "testo": (
            "Definisce l'OID id-aa-ets-commitmentType { iso(1) member-body(2) us(840) rsadsi(113549) "
            "pkcs(1) pkcs-9(9) smime(16) id-aa(2) 16 } e i tipi del commitment-type attribute "
            "(clausola 5.2.3): CommitmentTypeIndication (commitmentTypeId piu' un "
            "commitmentTypeQualifier opzionale), CommitmentTypeIdentifier, CommitmentTypeQualifier e "
            "la classe aperta COMMITMENT-QUALIFIER con la relativa WITH SYNTAX."
        ),
        "testo_integrale": (
            """-- commitment-type attribute (clause 5.2.3)

id-aa-ets-commitmentType OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 16}

CommitmentTypeIndication ::= SEQUENCE {
  commitmentTypeId         CommitmentTypeIdentifier,
  commitmentTypeQualifier SEQUENCE SIZE (1..MAX) OF CommitmentTypeQualifier OPTIONAL
}

CommitmentTypeIdentifier ::= OBJECT IDENTIFIER

CommitmentTypeQualifier ::= SEQUENCE {
  commitmentQualifierId   COMMITMENT-QUALIFIER.&id,
  qualifier               COMMITMENT-QUALIFIER.&Qualifier OPTIONAL
}

COMMITMENT-QUALIFIER ::= CLASS {
  &id         OBJECT IDENTIFIER UNIQUE,
  &Qualifier OPTIONAL }
WITH SYNTAX {
  COMMITMENT-QUALIFIER-ID &id
  [COMMITMENT-TYPE         &Qualifier] }"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-mimeType (mime-type attribute, clause 5.2.4.2)",
        "testo": (
            "Definisce l'OID id-aa-ets-mimeType { itu-t(0) identified-organization(4) etsi(0) "
            "electronic-signature-standard (1733) attributes(2) 1 } e il tipo MimeType ::= UTF8String "
            "del mime-type attribute (clausola 5.2.4.2)."
        ),
        "testo_integrale": (
            """-- mime-type attribute (clause 5.2.4.2)

id-aa-ets-mimeType OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4) etsi(0)
    electronic-signature-standard (1733) attributes(2) 1 }

MimeType::= UTF8String"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-signerLocation (signer-location attribute, clause 5.2.5)",
        "testo": (
            "Definisce l'OID id-aa-ets-signerLocation { iso(1) member-body(2) us(840) rsadsi(113549) "
            "pkcs(1) pkcs-9(9) smime(16) id-aa(2) 17 } e i tipi del signer-location attribute "
            "(clausola 5.2.5): SignerLocation, i cui campi countryName, localityName e postalAddress "
            "sono tutti opzionali ma di cui almeno uno deve essere presente come precisa il commento "
            "ASN.1, e PostalAddress, sequenza di 1..6 DirectoryString con la parametrizzazione "
            "maxSize di X.683."
        ),
        "testo_integrale": (
            """-- signer-location attribute (clause 5.2.5)

id-aa-ets-signerLocation OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 17 }

SignerLocation ::= SEQUENCE { -- at least one of the following shall be present
  countryName   [0] DirectoryString OPTIONAL, -- As used to name a Country in X.520
  localityName [1] DirectoryString OPTIONAL, -- As used to name a locality in X.520
  postalAddress [2] PostalAddress OPTIONAL
}

PostalAddress ::= SEQUENCE SIZE(1..6) OF DirectoryString{maxSize}
                                -- maxSize parametrization as specified in X.683"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-signerAttrV2 (signer-attributes-v2 attribute, clause 5.2.6.1)",
        "testo": (
            "Definisce l'OID id-aa-ets-signerAttrV2 { itu-t(0) identified-organization(4) etsi(0) "
            "cades(19122) attributes(1) 1 } e i tipi del signer-attributes-v2 attribute (clausola "
            "5.2.6.1): SignerAttributeV2, con claimedAttributes, certifiedAttributesV2 e "
            "signedAssertions opzionali; ClaimedAttributes (sequenza di Attribute); "
            "CertifiedAttributesV2 (certificato di attributo o otherAttributeCertificate); "
            "OtherAttributeCertificate; SignedAssertions e SignedAssertion; le classi aperte "
            "OTHER-ATTRIBUTE-CERT e SIGNED-ASSERTION con le loro WITH SYNTAX."
        ),
        "testo_integrale": (
            """-- signer-attributes-v2 attribute (clause 5.2.6.1)

id-aa-ets-signerAttrV2 OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4)
    etsi(0) cades(19122) attributes(1) 1 }

SignerAttributeV2 ::= SEQUENCE {
  claimedAttributes     [0] ClaimedAttributes OPTIONAL,
  certifiedAttributesV2 [1] CertifiedAttributesV2 OPTIONAL,
  signedAssertions      [2] SignedAssertions OPTIONAL
}

ClaimedAttributes ::= SEQUENCE OF Attribute

CertifiedAttributesV2 ::= SEQUENCE OF CHOICE {
  attributeCertificate      [0] AttributeCertificate,
  otherAttributeCertificate [1] OtherAttributeCertificate
}

OtherAttributeCertificate ::= SEQUENCE {
  otherAttributeCertID OTHER-ATTRIBUTE-CERT.&id,
  otherAttributeCert    OTHER-ATTRIBUTE-CERT.&OtherAttributeCert OPTIONAL
}

OTHER-ATTRIBUTE-CERT ::= CLASS {
  &id                  OBJECT IDENTIFIER UNIQUE,
  &OtherAttributeCert OPTIONAL }
WITH SYNTAX {
  OTHER-ATTRIBUTE-CERT-ID    &id
  [OTHER-ATTRIBUTE-CERT-TYPE    &OtherAttributeCert] }

SignedAssertions ::= SEQUENCE OF SignedAssertion

SignedAssertion ::= SEQUENCE {
  signedAssertionID SIGNED-ASSERTION.&id,
  signedAssertion    SIGNED-ASSERTION.&Assertion OPTIONAL
}

SIGNED-ASSERTION::= CLASS {
  &id         OBJECT IDENTIFIER UNIQUE,
  &Assertion OPTIONAL }
WITH SYNTAX {
  SIGNED-ASSERTION-ID     &id
  [SIGNED-ASSERTION-TYPE &Assertion] }"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-claimedSAML (claimed-SAML-assertion attribute, clause 5.2.6.2)",
        "testo": (
            "Definisce l'OID id-aa-ets-claimedSAML { itu-t(0) identified-organization(4) etsi(0) "
            "cades(19122) attributes(1) 2 } e il tipo ClaimedSAMLAssertion ::= OCTET STRING del "
            "claimed-SAML-assertion attribute (clausola 5.2.6.2)."
        ),
        "testo_integrale": (
            """-- claimed-SAML-assertion attribute (clause 5.2.6.2)

id-aa-ets-claimedSAML OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4)
    etsi(0) cades(19122) attributes(1) 2 }

ClaimedSAMLAssertion ::= OCTET STRING"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-contentTimestamp (content-timestamp attribute, clause 5.2.8)",
        "testo": (
            "Definisce l'OID id-aa-ets-contentTimestamp { iso(1) member-body(2) us(840) "
            "rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 20 } e il tipo ContentTimestamp ::= "
            "TimeStampToken del content-timestamp attribute (clausola 5.2.8)."
        ),
        "testo_integrale": (
            """-- content-timestamp attribute (clause 5.2.8)

id-aa-ets-contentTimestamp OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 20 }

ContentTimestamp::= TimeStampToken"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-sigPolicyId (signature-policy-identifier attribute, clause 5.2.9.1)",
        "testo": (
            "Definisce l'OID id-aa-ets-sigPolicyId { iso(1) member-body(2) us(840) rsadsi(113549) "
            "pkcs(1) pkcs9(9) smime(16) id-aa(2) 15 } (si noti la grafia pkcs9(9) del testo "
            "ufficiale) e i tipi del signature-policy-identifier attribute (clausola 5.2.9.1): "
            "SignaturePolicyIdentifier, scelta fra SignaturePolicyId e SignaturePolicyImplied "
            "(quest'ultimo NULL e non usato in questa versione); SignaturePolicyId; SigPolicyId; "
            "SigPolicyHash; OtherHashAlgAndValue; OtherHashValue; SigPolicyQualifierInfo con la lista "
            "SupportedSigPolicyQualifiers dei tre qualificatori ammessi (noticeToUser, "
            "pointerToSigPolSpec e sigPolDocSpecification); e la classe SIG-POLICY-QUALIFIER con i "
            "valori noticeToUser, pointerToSigPolSpec e sigPolDocSpecification."
        ),
        "testo_integrale": (
            """-- signature-policy-identifier attribute (clause 5.2.9.1)

id-aa-ets-sigPolicyId OBJECT IDENTIFIER ::= { iso(1) member-body(2) us(840)
    rsadsi(113549) pkcs(1) pkcs9(9) smime(16) id-aa(2) 15 }

SignaturePolicyIdentifier ::= CHOICE {
  signaturePolicyId      SignaturePolicyId,
  signaturePolicyImplied SignaturePolicyImplied -- not used in this version
}

SignaturePolicyId ::= SEQUENCE {
  sigPolicyId          SigPolicyId,
  sigPolicyHash        SigPolicyHash,
  sigPolicyQualifiers SEQUENCE SIZE (1..MAX) OF SigPolicyQualifierInfo OPTIONAL

}

SignaturePolicyImplied ::= NULL

SigPolicyId ::= OBJECT IDENTIFIER

SigPolicyHash ::= OtherHashAlgAndValue

OtherHashAlgAndValue ::= SEQUENCE {
  hashAlgorithm AlgorithmIdentifier,
  hashValue      OtherHashValue }

OtherHashValue ::= OCTET STRING

SigPolicyQualifierInfo ::= SEQUENCE {
  sigPolicyQualifierId SIG-POLICY-QUALIFIER.&id ({SupportedSigPolicyQualifiers}),
  qualifier             SIG-POLICY-QUALIFIER.&Qualifier
     ({SupportedSigPolicyQualifiers} {@sigPolicyQualifierId}) OPTIONAL
}

SupportedSigPolicyQualifiers SIG-POLICY-QUALIFIER ::= { noticeToUser |
  pointerToSigPolSpec | sigPolDocSpecification }

SIG-POLICY-QUALIFIER ::= CLASS {
  &id         OBJECT IDENTIFIER UNIQUE,
  &Qualifier OPTIONAL }
WITH SYNTAX {
  SIG-POLICY-QUALIFIER-ID &id
  [SIG-QUALIFIER-TYPE      &Qualifier] }

noticeToUser SIG-POLICY-QUALIFIER ::= {
  SIG-POLICY-QUALIFIER-ID id-spq-ets-unotice SIG-QUALIFIER-TYPE SPUserNotice }

pointerToSigPolSpec SIG-POLICY-QUALIFIER ::= {
  SIG-POLICY-QUALIFIER-ID id-spq-ets-uri SIG-QUALIFIER-TYPE SPuri }

sigPolDocSpecification SIG-POLICY-QUALIFIER ::= {
  SIG-POLICY-QUALIFIER-ID id-spq-ets-docspec SIG-QUALIFIER-TYPE SPDocSpecification }"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-spq-ets-uri (qualificatore spuri, clause 5.2.9.2)",
        "testo": (
            "Definisce l'OID id-spq-ets-uri { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) "
            "pkcs9(9) smime(16) id-spq(5) 1 } e il tipo SPuri ::= IA5String del qualificatore spuri "
            "(clausola 5.2.9.2)."
        ),
        "testo_integrale": (
            """-- spuri
id-spq-ets-uri OBJECT IDENTIFIER ::= { iso(1)
    member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs9(9)
    smime(16) id-spq(5) 1 }

SPuri ::= IA5String"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-spq-ets-unotice (qualificatore sp-user-notice, clause 5.2.9.2)",
        "testo": (
            "Definisce l'OID id-spq-ets-unotice { iso(1) member-body(2) us(840) rsadsi(113549) "
            "pkcs(1) pkcs9(9) smime(16) id-spq(5) 2 } e i tipi del qualificatore sp-user-notice "
            "(clausola 5.2.9.2): SPUserNotice, con noticeRef ed explicitText opzionali; "
            "NoticeReference, con organization e noticeNumbers; e DisplayText, scelta fra "
            "VisibleString, BMPString e UTF8String, ciascuno di lunghezza 1..200."
        ),
        "testo_integrale": (
            """-- sp-user-notice
id-spq-ets-unotice OBJECT IDENTIFIER ::= { iso(1)
    member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs9(9)
    smime(16) id-spq(5) 2 }

SPUserNotice ::= SEQUENCE {
  noticeRef     NoticeReference OPTIONAL,
  explicitText DisplayText OPTIONAL
}

NoticeReference ::= SEQUENCE {
  organization   DisplayText,
  noticeNumbers SEQUENCE OF INTEGER
}

DisplayText ::= CHOICE {
  visibleString VisibleString     (SIZE (1..200)),
  bmpString      BMPString        (SIZE (1..200)),
  utf8String     UTF8String       (SIZE (1..200))
}"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-spq-ets-docspec (qualificatore sp-doc-specification, clause 5.2.9.2)",
        "testo": (
            "Definisce l'OID id-spq-ets-docspec { itu-t(0) identified-organization(4) etsi(0) "
            "cades(19122) id-spq (2) 1 } e il tipo SPDocSpecification, scelta fra un OID e un URI, "
            "del qualificatore sp-doc-specification (clausola 5.2.9.2)."
        ),
        "testo_integrale": (
            """-- sp-doc-specification
id-spq-ets-docspec OBJECT IDENTIFIER ::=    { itu-t(0) identified-organization(4)
    etsi(0) cades(19122) id-spq (2) 1 }

SPDocSpecification ::= CHOICE {
  oid OBJECT IDENTIFIER,
  uri IA5String
}"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-sigPolicyStore (signature-policy-store attribute, clause 5.2.10)",
        "testo": (
            "Definisce l'OID id-aa-ets-sigPolicyStore { itu-t(0) identified-organization(4) etsi(0) "
            "cades(19122) attributes(1) 3 } e i tipi del signature-policy-store attribute (clausola "
            "5.2.10): SignaturePolicyStore, con spDocSpec e spDocument; e SignaturePolicyDocument, "
            "scelta fra sigPolicyEncoded e sigPolicyLocalURI."
        ),
        "testo_integrale": (
            """-- signature-policy-store attribute (clause 5.2.10)

id-aa-ets-sigPolicyStore OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4)
    etsi(0) cades(19122) attributes(1) 3 }

SignaturePolicyStore ::= SEQUENCE {
  spDocSpec   SPDocSpecification ,
  spDocument SignaturePolicyDocument
}

SignaturePolicyDocument ::= CHOICE {
  sigPolicyEncoded OCTET STRING,
  sigPolicyLocalURI IA5String
}"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-signatureTimeStampToken (signature-timestamp attribute, clause 5.3)",
        "testo": (
            "Definisce l'OID id-aa-signatureTimeStampToken { iso(1) member-body(2) us(840) "
            "rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 14 } e il tipo "
            "SignatureTimeStampToken ::= TimeStampToken del signature-timestamp attribute (clausola "
            "5.3)."
        ),
        "testo_integrale": (
            """-- signature-timestamp attribute (clause 5.3)

id-aa-signatureTimeStampToken OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 14 }

SignatureTimeStampToken ::= TimeStampToken"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ATSHashIndex-v3 (ats-hash-index-v3 attribute, clause 5.5.2)",
        "testo": (
            "Definisce l'OID id-aa-ATSHashIndex-v3 { itu-t(0) identified-organization(4) etsi(0) "
            "cades(19122) attributes(1) 5 } e il tipo ATSHashIndexV3, con hashIndAlgorithm, "
            "certificatesHashIndex, crlsHashIndex e unsignedAttrValuesHashIndex, "
            "dell'ats-hash-index-v3 attribute (clausola 5.5.2)."
        ),
        "testo_integrale": (
            """-- ats-hash-index-v3 attribute (clause 5.5.2)
id-aa-ATSHashIndex-v3 OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4)
    etsi(0) cades(19122) attributes(1) 5 }

ATSHashIndexV3 ::= SEQUENCE {
  hashIndAlgorithm              AlgorithmIdentifier,
  certificatesHashIndex         SEQUENCE OF OCTET STRING,
  crlsHashIndex                 SEQUENCE OF OCTET STRING,
  unsignedAttrValuesHashIndex   SEQUENCE OF OCTET STRING
}"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-archiveTimestampV3 (archive-time-stamp-v3 attribute, clause 5.5.3)",
        "testo": (
            "Definisce l'OID id-aa-ets-archiveTimestampV3 { itu-t(0) identified-organization(4) "
            "etsi(0) electronic-signature-standard(1733) attributes(2) 4 } e il tipo "
            "ArchiveTimeStampToken ::= TimeStampToken dell'archive-time-stamp-v3 attribute (clausola "
            "5.5.3)."
        ),
        "testo_integrale": (
            """-- archive-time-stamp-v3 attribute (clause 5.5.3)

id-aa-ets-archiveTimestampV3 OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4)
    etsi(0) electronic-signature-standard(1733) attributes(2) 4 }

ArchiveTimeStampToken ::= TimeStampToken"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-certificateRefs (complete-certificate-references attribute, clause A.1.1.1)",
        "testo": (
            "Definisce l'OID id-aa-ets-certificateRefs { iso(1) member-body(2) us(840) rsadsi(113549) "
            "pkcs(1) pkcs-9(9) smime(16) id-aa(2) 21 } e i tipi del complete-certificate-references "
            "attribute (clausola A.1.1.1): CompleteCertificateRefs, sequenza di OtherCertID; "
            "OtherCertID, con otherCertHash e issuerSerial opzionale; e OtherHash, scelta fra "
            "sha1Hash (che contiene un hash SHA-1) e otherHash."
        ),
        "testo_integrale": (
            """-- complete-certificate-references attribute (clause A.1.1.1)

id-aa-ets-certificateRefs OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 21 }

CompleteCertificateRefs ::=   SEQUENCE OF OtherCertID

OtherCertID ::= SEQUENCE {
  otherCertHash OtherHash,
  issuerSerial   IssuerSerial OPTIONAL
}

OtherHash ::= CHOICE {
  sha1Hash   OtherHashValue, -- This contains a SHA-1 hash
  otherHash OtherHashAlgAndValue
}"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-certValues (certificate-values attribute, clause A.1.1.2)",
        "testo": (
            "Definisce l'OID id-aa-ets-certValues { iso(1) member-body(2) us(840) rsadsi(113549) "
            "pkcs(1) pkcs-9(9) smime(16) id-aa(2) 23 } e il tipo CertificateValues ::= SEQUENCE OF "
            "Certificate del certificate-values attribute (clausola A.1.1.2)."
        ),
        "testo_integrale": (
            """-- certificate-values attribute (clause A.1.1.2)

id-aa-ets-certValues OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 23 }

CertificateValues ::=   SEQUENCE OF Certificate"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-revocationRefs (complete-revocation-references attribute, clause A.1.2.1)",
        "testo": (
            "Definisce l'OID id-aa-ets-revocationRefs { iso(1) member-body(2) us(840) rsadsi(113549) "
            "pkcs(1) pkcs-9(9) smime(16) id-aa(2) 22 } e i tipi del complete-revocation-references "
            "attribute (clausola A.1.2.1): CompleteRevocationRefs, sequenza di CrlOcspRef; "
            "CrlOcspRef, con crlids, ocspids e otherRev opzionali; CRLListID; CrlValidatedID; "
            "CrlIdentifier; OcspListID; OcspResponsesID; OcspIdentifier (che riprende i tipi della "
            "risposta OCSP); OtherRevRefs; e la classe aperta OTHER-REVOCATION-REF."
        ),
        "testo_integrale": (
            """-- complete-revocation-references attribute (clause A.1.2.1)

id-aa-ets-revocationRefs OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 22 }

CompleteRevocationRefs ::=   SEQUENCE OF CrlOcspRef

CrlOcspRef ::= SEQUENCE {
  crlids   [0] CRLListID   OPTIONAL,
  ocspids [1] OcspListID OPTIONAL,
  otherRev [2] OtherRevRefs OPTIONAL
}
CRLListID ::= SEQUENCE {
  crls SEQUENCE OF CrlValidatedID
}

CrlValidatedID ::= SEQUENCE {
  crlHash        OtherHash,
  crlIdentifier CrlIdentifier OPTIONAL
}

CrlIdentifier ::= SEQUENCE {
  crlissuer      Name,
  crlIssuedTime UTCTime,
  crlNumber      INTEGER OPTIONAL
}

OcspListID ::= SEQUENCE {
  ocspResponses SEQUENCE OF OcspResponsesID
}

OcspResponsesID ::= SEQUENCE {
  ocspIdentifier OcspIdentifier,
  ocspRefHash     OtherHash   OPTIONAL
}

OcspIdentifier ::= SEQUENCE {
  ocspResponderID ResponderID,     -- As in OCSP response data
  producedAt       GeneralizedTime -- As in OCSP response data
}

OtherRevRefs ::= SEQUENCE {
    otherRevRefType OTHER-REVOCATION-REF.&id,
    otherRevRefs    SEQUENCE OF OTHER-REVOCATION-REF.&Type
 }

OTHER-REVOCATION-REF ::= CLASS {
  &Type,
  &id   OBJECT IDENTIFIER UNIQUE }
WITH SYNTAX {
  WITH SYNTAX &Type ID &id }"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-revocationValues (certificate-revocation-values attribute, clause A.1.2.2)",
        "testo": (
            "Definisce l'OID id-aa-ets-revocationValues { iso(1) member-body(2) us(840) "
            "rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 24 } e i tipi del "
            "certificate-revocation-values attribute (clausola A.1.2.2): RevocationValues, con "
            "crlVals, ocspVals e otherRevVals opzionali; OtherRevVals, che nel testo ufficiale "
            "dichiara la sequenza dei valori come OTHER-REVOCATION-REF.&Type; e la classe aperta "
            "OTHER-REVOCATION-VAL."
        ),
        "testo_integrale": (
            """-- certificate-revocation-values attribute (clause A.1.2.2)

id-aa-ets-revocationValues OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 24 }

RevocationValues ::= SEQUENCE {
  crlVals      [0] SEQUENCE OF CertificateList OPTIONAL,
  ocspVals     [1] SEQUENCE OF BasicOCSPResponse OPTIONAL,
  otherRevVals [2] OtherRevVals OPTIONAL
}

OtherRevVals ::= SEQUENCE {
  otherRevValType OTHER-REVOCATION-VAL.&id,
  otherRevVals     SEQUENCE OF OTHER-REVOCATION-REF.&Type
}

OTHER-REVOCATION-VAL ::= CLASS {
  &Type,
  &id   OBJECT IDENTIFIER UNIQUE }
WITH SYNTAX {
  WITH SYNTAX &Type ID &id }"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-attrCertificateRefs (attribute-certificate-references attribute, clause A.1.3)",
        "testo": (
            "Definisce l'OID id-aa-ets-attrCertificateRefs { iso(1) member-body(2) us(840) "
            "rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 44 } e il tipo "
            "AttributeCertificateRefs ::= SEQUENCE OF OtherCertID "
            "dell'attribute-certificate-references attribute (clausola A.1.3)."
        ),
        "testo_integrale": (
            """-- attribute-certificate-references attribute (clause A.1.3)

id-aa-ets-attrCertificateRefs OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 44 }

AttributeCertificateRefs ::=     SEQUENCE OF OtherCertID"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-attrRevocationRefs (attribute-revocation-references attribute, clause A.1.4)",
        "testo": (
            "Definisce l'OID id-aa-ets-attrRevocationRefs { iso(1) member-body(2) us(840) "
            "rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 45 } e il tipo "
            "AttributeRevocationRefs ::= SEQUENCE OF CrlOcspRef dell'attribute-revocation-references "
            "attribute (clausola A.1.4)."
        ),
        "testo_integrale": (
            """-- attribute-revocation-references attribute (clause A.1.4)

id-aa-ets-attrRevocationRefs OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 45 }

AttributeRevocationRefs ::=     SEQUENCE OF CrlOcspRef"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-certCRLTimestamp (time-stamped-certs-crls-references attribute, clause A.1.5.1)",
        "testo": (
            "Definisce l'OID id-aa-ets-certCRLTimestamp { iso(1) member-body(2) us(840) "
            "rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 26 } e il tipo TimestampedCertsCRLs "
            "::= TimeStampToken del time-stamped-certs-crls-references attribute (clausola A.1.5.1)."
        ),
        "testo_integrale": (
            """-- time-stamped-certs-crls-references attribute (clause A.1.5.1)

id-aa-ets-certCRLTimestamp OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 26}

TimestampedCertsCRLs ::= TimeStampToken"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-aa-ets-escTimeStamp (CAdES-C-timestamp attribute, clause A.1.5.2)",
        "testo": (
            "Definisce l'OID id-aa-ets-escTimeStamp { iso(1) member-body(2) us(840) rsadsi(113549) "
            "pkcs(1) pkcs-9(9) smime(16) id-aa(2) 25 } e il tipo ESCTimeStampToken ::= TimeStampToken "
            "del CAdES-C-timestamp attribute (clausola A.1.5.2); chiude il primo modulo ASN.1 "
            "dell'annex con la parola chiave END."
        ),
        "testo_integrale": (
            """-- CAdES-C-timestamp attribute (clause A.1.5.2)

id-aa-ets-escTimeStamp OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 25}

ESCTimeStampToken ::= TimeStampToken

END"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, modulo ETSI-CAdES-19122v121 (intestazione, EXPORTS e IMPORTS)",
        "testo": (
            "Intestazione del secondo modulo ASN.1 dell'annex, aggiunto nella V1.2.1 "
            "(ETSI-CAdES-19122v121 { itu-t(0) identified-organization(4) etsi(0) cades(19122) "
            "id-mod(0) cades-19122v121(2) }), con DEFINITIONS EXPLICIT TAGS, EXPORTS All e "
            "l'importazione di id-aa-CMSAlgorithmProtection e CMSAlgorithmProtection dal modulo "
            "CMSAlgorithmProtectionAttribute di IETF RFC 6211."
        ),
        "testo_integrale": (
            """The following module was added in V1.2.1.
ETSI-CAdES-19122v121 { itu-t(0) identified-organization(4) etsi(0) cades(19122)
    id-mod(0) cades-19122v121(2)}

DEFINITIONS EXPLICIT TAGS ::=
BEGIN
EXPORTS All;

IMPORTS

-- Imports from Cryptographic Message Syntax (CMS) Algorithm Identifier Protection Attribute:
-- IETF RFC 6211
        id-aa-CMSAlgorithmProtection, CMSAlgorithmProtection
            FROM CMSAlgorithmProtectionAttribute
    { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) modules(0)
      id-mod-cms-algorithmProtect(52) }

;"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-etsi-cades-spq (arc delle signed assertions, modulo ETSI-CAdES-19122v121)",
        "testo": (
            "Definisce, nel secondo modulo, l'object identifier arc id-etsi-cades-spq { itu-t(0) "
            "identified-organization(4) etsi(0) cades(19122) signed-assertions(3) }, destinato alle "
            "signed assertions dentro il campo signer-attribute-v2; il testo ufficiale riusa il nome "
            "id-etsi-cades-spq gia' assegnato in questo annex all'arc dei qualificatori di signature "
            "policy."
        ),
        "testo_integrale": (
            """-- Object Identifier arc signed assertions within the signer-attribute-v2
id-etsi-cades-spq OBJECT IDENTIFIER ::=
    { itu-t(0) identified-organization(4) etsi(0) cades(19122) signed-assertions(3) }"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, id-ets-signedSAML (signed-SAML-assertion, modulo ETSI-CAdES-19122v121)",
        "testo": (
            "Definisce l'OID id-ets-signedSAML { itu-t(0) identified-organization(4) etsi(0) "
            "cades(19122) signed-assertions (3) 0 } e il tipo SignedSAMLAssertion ::= OCTET STRING "
            "della signed-SAML-assertion, e chiude il secondo modulo ASN.1 dell'annex con la parola "
            "chiave END."
        ),
        "testo_integrale": (
            """-- signed-SAML-assertion
-- ==================================================================
id-ets-signedSAML OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4)
    etsi(0) cades(19122) signed-assertions (3) 0 }

SignedSAMLAssertion ::= OCTET      STRING

END"""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "Annex D (normative), premessa (precedenza dei moduli ASN.1 e sintassi di interpretazione)",
    "Annex D, modulo ETSI-CAdES-ExplicitSyntax97 (intestazione, EXPORTS e IMPORTS)",
    "Annex D, id-etsi-es-attributes (arc degli attributi definiti in TS 101 733)",
    "Annex D, id-etsi-cades-attributes (arc degli attributi CAdES di EN 319 122-1)",
    "Annex D, id-etsi-cades-spq (arc dei qualificatori di signature policy)",
    "Annex D, id-etsi-cades-mod (arc dei moduli ASN.1 di EN 319 122-1)",
    "Annex D, id-aa-ets-commitmentType (commitment-type attribute, clause 5.2.3)",
    "Annex D, id-aa-ets-mimeType (mime-type attribute, clause 5.2.4.2)",
    "Annex D, id-aa-ets-signerLocation (signer-location attribute, clause 5.2.5)",
    "Annex D, id-aa-ets-signerAttrV2 (signer-attributes-v2 attribute, clause 5.2.6.1)",
    "Annex D, id-aa-ets-claimedSAML (claimed-SAML-assertion attribute, clause 5.2.6.2)",
    "Annex D, id-aa-ets-contentTimestamp (content-timestamp attribute, clause 5.2.8)",
    "Annex D, id-aa-ets-sigPolicyId (signature-policy-identifier attribute, clause 5.2.9.1)",
    "Annex D, id-spq-ets-uri (qualificatore spuri, clause 5.2.9.2)",
    "Annex D, id-spq-ets-unotice (qualificatore sp-user-notice, clause 5.2.9.2)",
    "Annex D, id-spq-ets-docspec (qualificatore sp-doc-specification, clause 5.2.9.2)",
    "Annex D, id-aa-ets-sigPolicyStore (signature-policy-store attribute, clause 5.2.10)",
    "Annex D, id-aa-signatureTimeStampToken (signature-timestamp attribute, clause 5.3)",
    "Annex D, id-aa-ATSHashIndex-v3 (ats-hash-index-v3 attribute, clause 5.5.2)",
    "Annex D, id-aa-ets-archiveTimestampV3 (archive-time-stamp-v3 attribute, clause 5.5.3)",
    "Annex D, id-aa-ets-certificateRefs (complete-certificate-references attribute, clause A.1.1.1)",
    "Annex D, id-aa-ets-certValues (certificate-values attribute, clause A.1.1.2)",
    "Annex D, id-aa-ets-revocationRefs (complete-revocation-references attribute, clause A.1.2.1)",
    "Annex D, id-aa-ets-revocationValues (certificate-revocation-values attribute, clause A.1.2.2)",
    "Annex D, id-aa-ets-attrCertificateRefs (attribute-certificate-references attribute, clause A.1.3)",
    "Annex D, id-aa-ets-attrRevocationRefs (attribute-revocation-references attribute, clause A.1.4)",
    "Annex D, id-aa-ets-certCRLTimestamp (time-stamped-certs-crls-references attribute, clause A.1.5.1)",
    "Annex D, id-aa-ets-escTimeStamp (CAdES-C-timestamp attribute, clause A.1.5.2)",
    "Annex D, modulo ETSI-CAdES-19122v121 (intestazione, EXPORTS e IMPORTS)",
    "Annex D, id-etsi-cades-spq (arc delle signed assertions, modulo ETSI-CAdES-19122v121)",
    "Annex D, id-ets-signedSAML (signed-SAML-assertion, modulo ETSI-CAdES-19122v121)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-sigPolicyId (signature-policy-identifier attribute, clause 5.2.9.1)"),
        "nodo_a": ("principio", None, "Annex D, id-spq-ets-uri (qualificatore spuri, clause 5.2.9.2)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-sigPolicyId (signature-policy-identifier attribute, clause 5.2.9.1)"),
        "nodo_a": ("principio", None, "Annex D, id-spq-ets-unotice (qualificatore sp-user-notice, clause 5.2.9.2)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-sigPolicyId (signature-policy-identifier attribute, clause 5.2.9.1)"),
        "nodo_a": ("principio", None, "Annex D, id-spq-ets-docspec (qualificatore sp-doc-specification, clause 5.2.9.2)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-certificateRefs (complete-certificate-references attribute, clause A.1.1.1)"),
        "nodo_a": ("principio", None, "Annex D, id-aa-ets-sigPolicyId (signature-policy-identifier attribute, clause 5.2.9.1)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-revocationRefs (complete-revocation-references attribute, clause A.1.2.1)"),
        "nodo_a": ("principio", None, "Annex D, id-aa-ets-certificateRefs (complete-certificate-references attribute, clause A.1.1.1)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-revocationValues (certificate-revocation-values attribute, clause A.1.2.2)"),
        "nodo_a": ("principio", None, "Annex D, id-aa-ets-revocationRefs (complete-revocation-references attribute, clause A.1.2.1)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-attrCertificateRefs (attribute-certificate-references attribute, clause A.1.3)"),
        "nodo_a": ("principio", None, "Annex D, id-aa-ets-certificateRefs (complete-certificate-references attribute, clause A.1.1.1)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-attrRevocationRefs (attribute-revocation-references attribute, clause A.1.4)"),
        "nodo_a": ("principio", None, "Annex D, id-aa-ets-revocationRefs (complete-revocation-references attribute, clause A.1.2.1)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-sigPolicyStore (signature-policy-store attribute, clause 5.2.10)"),
        "nodo_a": ("principio", None, "Annex D, id-spq-ets-docspec (qualificatore sp-doc-specification, clause 5.2.9.2)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
