"""Estrazione granulare ETSI EN 319 122-1 V1.3.1 (2023-06) — Capitolo 5 dello
split: Annex A (normative, "Additional Attributes Specification": A.1 attributi
per i dati di validazione — A.1.1 certificati, A.1.2 revoca, A.1.3/A.1.4
certificati e revoca dei certificati di attributo e delle asserzioni firmate,
A.1.5 marche temporali sui riferimenti — e A.2 attributi deprecati, A.2.1
disposizione generale e A.2.2-A.2.6 singoli attributi deprecati) e, in coda,
Annex B (normative, "Alternative mechanisms for long term availability and
integrity of validation data") e Annex C ("Void").

Fonte del blocco B (famiglia AdES del lotto 2); la numerazione definitiva della
fonte e' cablata dalla sessione principale in app/seed.py — questo modulo NON
tocca seed.py, non importa nulla e non legge file: e' puro dato.

Provenienza del testo
---------------------
- testo ufficiale: ETSI EN 319 122-1 V1.3.1 (2023-06), "Electronic Signatures
  and Trust Infrastructures (ESI); CAdES digital signatures; Part 1: Building
  blocks and CAdES baseline signatures".
- file di capitolo: app/.source_cache/etsi_319_122/cap05.txt (641 righe),
  porzione della conversione PDF (pdftotext -layout) di
  app/.source_cache/etsi_319_122/raw.pdf (copia completa dello stesso testo in
  app/.source_cache/etsi_319_122/raw.txt e raw_body.txt).
- metadati da app/.source_cache/etsi_319_122/provenance.json: url
  https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf,
  versione "01.03.01_60", data_fetch 2026-09-29T12:56:34Z, sha256_raw_pdf
  e99e76e519d9bd8e1410775bccedb1a588021e5e7c705c9fcc1f91c6a6227c21.
- perimetro: da "Annex A (normative): Additional Attributes Specification"
  (riga 1 del file) a "Annex C: Void" (righe 631-632). Confine di split pulito
  da entrambi i lati: cap04.txt termina con il footer di pagina 39 (nessuna
  coda della clausola 6) e cap06.txt inizia con "Annex D (normative): Signature
  Format Definitions Using X.680 ASN.1 Syntax".

Granularita' (ADR-0007)
-----------------------
L'annesso non usa id di requisito nella forma <SIGLA>-<clausola>-<NN>: le
unita' numerate con contenuto proprio sono le otto sottoclausole di A.1
(A.1.1.1, A.1.1.2, A.1.2.1, A.1.2.2, A.1.3, A.1.4, A.1.5.1, A.1.5.2), le sei
di A.2 (A.2.1-A.2.6) e i due annessi successivi (Annex B, normativo; Annex C,
Void). Gli elenchi numerati 1)-4) interni a una sottoclausta (quattro punti in
A.1.2.1, tre in A.1.3 e A.1.4, due in A.1.1.1 e A.1.1.2, uno in A.1.2.2) NON
sono unita' di indice a se': sono dettaglio della sottoclausta che li introduce
(stesso criterio delle lettere a)-f) di REQ-5-01 in ETSI EN 319 401, cap02)
e restano nel `testo_integrale` della sottoclausta. Anche i blocchi ASN.1, le
NOTE e gli EXAMPLE (Annex B) restano nel nodo della sottoclausta/annesso che li
contiene: non hanno numerazione propria.

Bilancio: 16 item di indice -> 16 righe, 1:1 (15 Obblighi + 1 Principio).

Intestazioni di solo raggruppamento, senza testo proprio (nessun nodo, nessun
item di indice — stesso criterio gia' applicato a ETSI EN 319 122-1 cap03/cap04
e alle altre fonti ETSI censite): "Annex A (normative): Additional Attributes
Specification" (segue A.1), "A.1 Attributes for validation data" (segue A.1.1),
"A.1.1 Certificates validation data" (segue A.1.1.1), "A.1.2 Revocation
validation data" (segue A.1.2.1), "A.1.5 Time-stamps on references to
validation data" (segue A.1.5.1), "A.2 Deprecated attributes" (segue A.2.1).
In tutti questi casi l'intestazione e' solo titolazione, immediatamente seguita
dalla prima sottoclausta con testo proprio.

Vocabolario dei `riferimento`: per gli annessi si usa il termine del testo
ufficiale ("Annex A.1.1.1 (The complete-certificate-references attribute)"),
coerente con la convenzione gia' usata per gli annessi in ETSI TS 119 612
cap08 ("Annex H.1 (Introduction)"). Le clausole numerate della stessa Fonte
restano invece in forma italiana ("clausola 5.2.2 (...)", moduli cap02/cap03),
perche' li' e' il testo a numerare cosi'.

Classificazione Obbligo/Principio
---------------------------------
- Tutte le sottoclausole di A.1 e di A.2 contengono almeno un requisito
  prescrittivo ("shall"/"should"/"shall not") o un divieto/redirezione
  ("is deprecated ... shall be used"/"shall not be created"): sono Obblighi
  "tecnico/sicurezza" (vincolano contenuto e codifica di cio' che entra nella
  firma CAdES e dei dati di validazione che la accompagnano). Un solo
  Principio in tutto il capitolo (Annex C).
- Annex B -> Obbligo "tecnico/sicurezza": l'annesso e' normativo e usa "shall
  be specified" per imporre il contenuto minimo della specifica di un
  meccanismo alternativo (semantica/sintassi e OID, strategia di protezione,
  gestione degli attributi del presente documento, gestione delle firme legacy).
  Non "organizzativo": l'oggetto della prescrizione e' la specifica tecnica di
  un attributo di firma, non un processo di governance del prestatore.
- Annex C -> Principio "altro": il corpo dell'annesso e' la sola parola "Void".
  Inserito come item perche' il perimetro assegnato chiede di censire tutti e
  tre gli annessi del file e di distinguerne i riferimenti ("Annex A ...",
  "Annex B ...", "Annex C ..."); e' un segnaposto di redazione privo di
  contenuto normativo, quindi Principio e non Obbligo. Nota di coerenza: altri
  moduli del censimento (ETSI TS 119 312 cap03/cap04, ETSI TS 119 431-1 cap01)
  escludono i "Void" *interni* a una numerazione esistente quando sono privi di
  contenuto autonomo; qui il "Void" e' un annesso intero del perimetro
  assegnato, quindi resta come riga minima, senza inventare contenuto.

soggetti/oggetti_giuridici: nessuno in questo capitolo. Il testo non nomina
nessuna delle quattro categorie censite come soggetto obbligato ("the signer"
compare solo in "The signer's certificate is referenced..." di A.1.1.1, dove
e' il certificato a essere nominato, non un obbligato; i requisiti sono
formulati in modo impersonale sugli attributi — "the X attribute shall
contain..."). Anche il "Systems may extend the lifetime..." di A.2.4/A.2.5 non
individua una categoria censita (sono i sistemi che detengono la firma, non il
QTSP come soggetto censito): nessuna riga porta soggetti.

Decisioni di modellazione, riga per riga
----------------------------------------
- Annex A.1.1.1 (The complete-certificate-references attribute) -> Obbligo
  "tecnico/sicurezza". Semantica (attributo unsigned, contenuto ammesso e
  vietato sui riferimenti ai certificati della catena) + Syntax (un componente
  AttributeValue, tipo ASN.1 CompleteCertificateRefs, OID
  id-aa-ets-certificateRefs) + il periodo finale sull'aggiunta al SignedData del
  token di marca temporale. NOTE 1-4 assorbite: interpretano il requisito
  (dove sta il certificato del firmatario; dove finiscono i riferimenti dei
  certificati di attributo; copie dei valori; effetto sul content-time-stamp).
- Annex A.1.1.2 (The certificate-values attribute) -> Obbligo
  "tecnico/sicurezza". Due punti (valori dei certificati referenziati e non
  presenti in SignedData.certificates; nessun altro certificato), Syntax con
  tipo ASN.1 CertificateValues e OID id-aa-ets-certValues, NOTE 1-2 e periodo
  finale sui TSU assorbiti.
- Annex A.1.2.1 (The complete-revocation-references attribute) -> Obbligo
  "tecnico/sicurezza". La sottoclausta piu' densa del capitolo: quattro punti
  sul contenuto (riferimento per il certificato di firma; riferimenti per i
  certificati di CA, esclusa la trust anchor; riferimenti facoltativi per chi
  firma CRL/OCSP; divieto per i certificati dei soli attributi), il periodo
  "should be used in preference to OtherRevocationInfoFormat", la Syntax con il
  blocco ASN.1 completo (CompleteRevocationRefs, CrlOcspRef, CrlValidatedID,
  CrlIdentifier, OcspListID, OcspResponsesID, OcspIdentifier, OtherRevRefs,
  classe OTHER-REVOCATION-REF) e le regole di costruzione che seguono (ordine
  delle voci CrlOcspRef, hash sull'intera CRL DER, crlIdentifier, Delta CRL,
  OcspIdentifier, ocspRefHash, rinvio di tipo alle clausole 5.4.2.1 e 4.8.2,
  limiti di ambito per "other" revocation references), con NOTE 1-6 assorbite.
- Annex A.1.2.2 (The revocation-values attribute) -> Obbligo
  "tecnico/sicurezza". Due punti (elementi corrispondenti ai riferimenti di
  complete-revocation-references e attribute-revocation-references non presenti
  in SignedData.crls; nessun altro elemento), periodo "should be used in
  preference to OtherRevocationInfoFormat", Syntax con tipo ASN.1
  RevocationValues e OID id-aa-ets-revocationValues, blocco ASN.1
  (RevocationValues, OtherRevVals, classe OTHER-REVOCATION-VAL), regole su
  CertificateList (rinvio a 4.8.2), OCSP responses (rinvio a 5.4.2.1 e OID
  id-ri-ocsp-response) e NOTE finale.
- Annex A.1.3 (The attribute-certificate-references attribute) -> Obbligo
  "tecnico/sicurezza". Tre punti sulla condizione "if they are not present
  within complete-certificate-references attribute", Syntax con tipo ASN.1
  AttributeCertificateRefs e OID id-aa-ets-attrCertificateRefs, NOTE assorbita
  (copie dei valori via certificate-values; il certificato di attributo sta in
  signer-attributes-v2).
- Annex A.1.4 (The attribute-revocation-references attribute) -> Obbligo
  "tecnico/sicurezza". Tre punti speculari ad A.1.3 per i dati di revoca
  (nessun riferimento di revoca per la trust anchor), Syntax con tipo ASN.1
  AttributeRevocationRefs e OID id-aa-ets-attrRevocationRefs, NOTE 1-2 e
  periodo finale sulle Delta CRL, tutti assorbiti.
- Annex A.1.5.1 (The time-stamped-certs-crls-references attribute) -> Obbligo
  "tecnico/sicurezza". Semantica (attributo unsigned che incapsula una marca
  temporale dei due attributi di riferimento), Syntax con tipo ASN.1
  TimestampedCertsCRLs e OID id-aa-ets-certCRLTimestamp, regola sul
  messageImprint (hash dei valori concatenati dei due attributi, con
  attrType/attrValues e senza tipo/lunghezza della SEQUENCE esterna), regola di
  codifica DER e rinvio di definizione a TimeStampToken (clausola 4.8.1).
- Annex A.1.5.2 (The CAdES-C-timestamp attribute) -> Obbligo
  "tecnico/sicurezza". Semantica (marca temporale che copre firma, marca
  temporale di firma e i due attributi di riferimento), NOTE sull'ambito
  (CAdES-E-C di ETSI EN 319 122-2), Syntax con tipo ASN.1 ESCTimeStampToken e
  OID id-aa-ets-escTimeStamp, regola sul messageImprint (quattro oggetti
  concatenati), regola di codifica DER e rinvio di definizione a TimeStampToken
  (clausola 4.8.1).
- Annex A.2.1 (Usage of deprecated attributes) -> Obbligo "tecnico/sicurezza".
  Regola generale di A.2: gli attributi deprecati sono mantenuti nel documento
  ma non devono piu' essere aggiunti a una firma, con la sola eccezione
  dell'attributo long-term-validation. E' una prescrizione (divieto), non una
  descrizione: Obbligo.
- Annex A.2.2 / A.2.3 / A.2.6 (other-signing-certificate, signer-attributes,
  ats-hash-index) -> Obbligo "tecnico/sicurezza" ciascuno: "is deprecated.
  Instead ... shall be used" e' un divieto con redirezione all'attributo
  corrente (clausole 5.2.2.3, 5.2.6.1, 5.5.2). La NOTE di A.2.6 (ambiguita' di
  decodifica del vecchio ats-hash-index) e' assorbita perche' motiva la
  redirezione.
- Annex A.2.4 / A.2.5 (archive-time-stamp ATSv2, long-term-validation) ->
  Obbligo "tecnico/sicurezza" ciascuno: divieto di creare nuovi attributi di
  quel tipo, con facolta' espressa ("Systems may extend the lifetime of
  signatures ... by incorporating new ATSv3", clausola 5.5.3) che resta nel
  nodo perche' e' la condizione di applicabilita' del divieto, non un requisito
  autonomo.
- Annex B -> Obbligo "tecnico/sicurezza": rinvio di campo alla clausola 5.5
  ("different from the ones described in clause 5.5"), poi la prescrizione sui
  quattro punti da specificare. NOTE 1-2 (limite: tali meccanismi non
  rappresentano il livello CAdES-B-LTA ne' i livelli CAdES-E-A; possibile
  inclusione in versioni future) ed EXAMPLE (IETF RFC 4998, annex A) assorbiti:
  delimitano la portata del requisito.
- Annex C (Void) -> Principio "altro": solo il segnaposto "Void", nessun
  contenuto normativo (vedi sopra).

Completezza verbatim
--------------------
`testo_integrale` riporta il testo ufficiale per intero, ricucendo le righe
spezzate dalla conversione PDF, senza elisioni ne' riassunti. Convenzioni di
ricostruzione applicate:
- rimossi i footer/header di pagina ("ETSI", "40 ETSI EN 319 122-1 V1.3.1
  (2023-06)", ecc.) che cadono dentro le sottoclausole a cavallo di pagina
  (A.1.1.1, A.1.2.1, A.1.2.2, A.1.3, A.1.4, A.1.5.1, A.2.1);
- ricucite le parole spezzate a fine riga su trattino della parola composta
  ("signing-certificate-reference", "complete-certificate-references",
  "complete-revocation-references", "id-aa-ets-attrCertificateRefs",
  "revocation-values", "signer-attributes-v2", "long-term-validation",
  "ats-hash-index-v3", tutti ricomposti nella forma in cui il testo li usa
  altrove);
- normalizzati gli spazi interni di intestazione (i punti 1)-4) del testo
  ufficiale hanno "   1)    "), mantenendo l'ordine e la numerazione originali;
- in A.1.5.2 corretto "ASN.1structures" in "ASN.1 structures" (difetto di
  conversione: la stessa frase in A.1.5.1 ha lo spazio, e la parola non e'
  spezzata da un trattino);
- etichette di sezione "Semantics"/"Syntax" mantenute come righe di etichetta
  come nel file di origine (in cap03 della stessa Fonte erano state unite al
  periodo seguente con ": "; qui si preferisce la forma del testo);
- blocchi ASN.1 riportati cosi' come sono, allineamenti e commenti ("-- This
  contains a SHA-1 hash", "-- As in OCSP response data") inclusi.

Rinvii demandati alla fase 6 (nessuna relazione nel modulo verso di essi)
------------------------------------------------------------------------
- Verso altre clausole della stessa Fonte (capitoli 1-4 di questo stesso
  import): A.1.1.1 NOTE 1 -> clausola 5.2.2; A.1.1.2 punto 1) -> clausola
  5.2.2 (signing-certificate-reference); A.1.2.1 -> clausola 5.4.2.1 (tipi di
  OCSP response); A.1.2.2 -> clausole 4.8.2 (CertificateList) e 5.4.2.1; A.1.3
  NOTE -> clausola 5.2.6.1 (signer-attributes-v2); A.1.5.1 e A.1.5.2 ->
  clausola 4.7.1 (DER) e clausola 4.8.1 (TimeStampToken); A.2.2 -> clausola
  5.2.2.3; A.2.3 -> clausola 5.2.6.1; A.2.4 e A.2.5 -> clausola 5.5.3; A.2.6 ->
  clausola 5.5.2; Annex B -> clausola 5.5 e clausola 6.
- Verso l'Annex D (normativo, definizioni ASN.1) di questa stessa Fonte, che
  sta nel capitolo 6 dello split: tutti i "The corresponding definitions shall
  be as defined in annex D and are copied here for information." delle otto
  sottoclausole di A.1, piu' A.1.1.2 NOTE 1 (IETF RFC 5280 [6]).
- Verso fonti esterne: ETSI TS 101 733 [1] (origine degli attributi deprecati
  di A.2.1-A.2.6 e compatibilita' all'indietro di A.1.2.1/A.1.2.2), ETSI EN
  319 122-2 [i.6] (livello CAdES-E-C in A.1.5.2, livelli CAdES-E-A in Annex B,
  entrambi non censiti), IETF RFC 5652 [7] (OtherRevocationInfoFormat), IETF RFC
  5280 [6], IETF RFC 4998 [i.15] annex A (EXAMPLE di Annex B), Recommendation
  ITU-T X.509 v3 [i.18].
Menzioni per solo nome di attributi "sorelle" interne all'annesso (es.
"complete-certificate-references attribute" in A.1.3 e A.1.4, "complete-
revocation-references attribute" in A.1.5.1/A.1.5.2, "the long-term-validation
attribute" in A.2.1) non sono state trasformate in archi: non portano un
puntatore di clausola e il bersaglio e' comunque identificato dalle intestazioni
dell'annesso.

Relazioni interne dichiarate (10, tutte "richiama" con evidence_type
"textual"): le citazioni con puntatore di clausola verificabili dentro questo
stesso modulo — A.1.1.1 -> A.1.3 e A.1.1.2; A.1.1.2 -> A.1.1.1 e A.1.3;
A.1.2.1 -> A.1.4 e A.1.2.2; A.1.2.2 -> A.1.2.1 e A.1.4; A.1.3 -> A.1.1.2;
A.1.4 -> A.1.2.2.

Conteggio di copertura: 16 item di indice, 16 righe: 15 obblighi + 1 principio.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "Annex A.1.1.1 (The complete-certificate-references attribute)",
        "testo": (
            "Attributo unsigned che elenca i riferimenti ai certificati usati per "
            "validare la firma: deve contenere il riferimento al certificato di trust "
            "anchor, se esiste, e i riferimenti ai certificati di CA nel percorso del "
            "certificato di firma; non deve contenere il riferimento al certificato di "
            "firma ne' riferimenti a certificati di CA che appartengono esclusivamente "
            "ai percorsi dei certificati di attributo o delle asserzioni firmate. Il "
            "valore deve essere un'istanza del tipo ASN.1 CompleteCertificateRefs e "
            "l'attributo deve essere identificato dall'OID id-aa-ets-certificateRefs. "
            "L'attributo puo' includere la catena di certificazione dei TSU che "
            "forniscono marche temporali, ed e' in tal caso da aggiungere al SignedData "
            "del relativo token."
        ),
        "testo_integrale": (
            """Semantics

The complete-certificate-references attribute shall be an unsigned attribute.

The complete-certificate-references attribute:

1) Shall contain the reference to the certificate of the trust anchor if such certificate does exist, and the references to CA certificates within the signing certificate path.

2) Shall not contain the reference to the signing certificate.

NOTE 1: The signer's certificate is referenced in the signing certificate attribute (see clause 5.2.2). May contain references to the certificates used to sign CRLs or OCSP responses for certificates referenced by references in 1), and references to certificates within their respective certificate paths.

3) Shall not contain references to CA certificates that pertain exclusively to the certificate paths of certificates used to sign attribute certificates or signed assertions within the signer-attributes-v2 attribute.

NOTE 2: The references to certificates exclusively used in the validation of attribute certificate or signed assertions are stored in the attribute-certificate-references attribute (see clause A.1.3).

Syntax

The complete-certificate-references attribute shall contain exactly one component of AttributeValue type.

The complete-certificate-references attribute value shall be an instance of CompleteCertificateRefs ASN.1 type.

The complete-certificate-references attribute shall be identified by the id-aa-ets-certificateRefs OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-certificateRefs OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 21 }

CompleteCertificateRefs ::=         SEQUENCE OF OtherCertID

OtherCertID ::= SEQUENCE {
  otherCertHash OtherHash,
  issuerSerial   IssuerSerial OPTIONAL
}

OtherHash ::= CHOICE {
  sha1Hash   OtherHashValue, -- This contains a SHA-1 hash
  otherHash OtherHashAlgAndValue
}

NOTE 3: Copies of the certificate values can be held using the certificate-values attribute, defined in clause A.1.1.2 or within SignedData.certificates.

This attribute may include references to the certification chain for any TSU that provides time-stamp tokens. In this case, the unsigned attribute shall be added to the SignedData of the relevant time-stamp token.

NOTE 4: In the case of a content-time-stamp, the time-stamp token cannot be changed after the signature without invalidating the signature. Consequently, this unsigned attribute needs to be added before signing."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A.1.1.2 (The certificate-values attribute)",
        "testo": (
            "Attributo unsigned che deve contenere i valori dei certificati "
            "referenziati negli attributi complete-certificate-references, "
            "attribute-certificate-references e signing-certificate-reference che non "
            "siano gia' presenti in SignedData.certificates; nessun altro certificato "
            "deve essere incluso. Il valore deve essere un'istanza del tipo ASN.1 "
            "CertificateValues e l'attributo deve essere identificato dall'OID "
            "id-aa-ets-certValues."
        ),
        "testo_integrale": (
            """Semantics

The certificate-values attribute shall be an unsigned attribute.

The certificate-values attribute:

1) Shall contain the values of the certificates referenced within complete-certificate-references (clause A.1.1.1), attribute-certificate-references (clause A.1.3), and the signing-certificate-reference (clause 5.2.2) attributes, which are not stored SignedData.certificates. Certificate values within SignedData.certificates should not be included.

2) No other certificates shall be included.

Syntax

The certificate-values attribute shall contain exactly one component of AttributeValue type.

The certificate-values attribute value shall be an instance of CertificateValues ASN.1 type.

The certificate-values attribute shall be identified by the id-aa-ets-certValues OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-certValues OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 23 }

CertificateValues ::=       SEQUENCE OF Certificate

NOTE 1: Certificate is defined in IETF RFC 5280 [6] (see annex D) and is a basic syntax to include Recommendation ITU-T X.509 v3 [i.18] certificates.

This attribute may include the certification information for any TSUs that have provided the time-stamp tokens, if these certificates are not already included in the TSTs as part of the TSUs signatures. In this case, the unsigned attribute shall be added to the SignedData of the relevant time-stamp token.

NOTE 2: In the case of a content-time-stamp, the time-stamp token cannot be changed after the signature without invalidating the signature. Consequently, this unsigned attribute needs to be added before signing or somewhere else within the signature, if needed."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A.1.2.1 (The complete-revocation-references attribute)",
        "testo": (
            "Attributo unsigned che deve contenere i riferimenti ai dati di revoca "
            "della catena di certificazione: il riferimento per il certificato di firma, "
            "i riferimenti corrispondenti ai certificati di CA elencati in "
            "complete-certificate-references (escluso il trust anchor, per il quale non "
            "si usa informazione di revoca) e, facoltativamente, quelli dei certificati "
            "usati per firmare CRL o risposte OCSP; non deve contenere riferimenti a "
            "certificati di CA usati solo nei percorsi dei certificati di attributo o "
            "delle asserzioni firmate. Il valore deve essere un'istanza del tipo ASN.1 "
            "CompleteRevocationRefs, identificato dall'OID id-aa-ets-revocationRefs; la "
            "sequenza deve iniziare con il CrlOcspRef del certificato di firma, l'hash "
            "della CRL va calcolato sull'intera CRL codificata in DER e l'ocspRefHash "
            "deve contenere il digest delle risposte OCSP."
        ),
        "testo_integrale": (
            """Semantics

The complete-revocation-references attribute shall be an unsigned attribute.

The complete-revocation-references attribute:

1) Shall contain a reference to a revocation value for the signing certificate.

2) Shall contain the references to the revocation values (e.g. CRLs or OCSP values) corresponding to CA certificates references in the complete-certificate-references attribute, except for the trust anchors. It shall not contain references to revocation values for the trust anchor.

NOTE 1: A trust anchor is by definition trusted, thus no revocation information for the trust anchor is used during the validation.

3) May contain references to the revocation values corresponding to certificates used to sign CRLs or OCSP responses referenced in references from 1) and 2), and to certificates within their respective certificate paths.

4) Shall not contain references to the revocation values corresponding to CA certificates that pertain exclusively to the certificate paths of certificates used to sign attribute certificates or signed assertions within the signer-attributes-v2 attribute.

NOTE 2: The references to revocation values exclusively used in the validation of attribute certificate or signed assertions are stored in the attribute-revocation-references attribute (see clause A.1.4).

The complete-revocation-references attribute should be used in preference to the OtherRevocationInfoFormat specified in IETF RFC 5652 [7] to maintain backwards compatibility with the earlier versions of ETSI TS 101 733 [1].

Syntax

The complete-revocation-references attribute shall contain exactly one component of AttributeValue type.

The complete-revocation-references attribute value shall be an instance of CompleteRevocationRefs ASN.1 type.

The complete-revocation-references attribute shall be identified by the id-aa-ets-revocationRefs OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-revocationRefs OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 22 }

CompleteRevocationRefs ::=        SEQUENCE OF CrlOcspRef

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
  WITH SYNTAX &Type ID &id }

In CompleteRevocationRefs, the sequence shall start with the CrlOcspRef for the signing certificate (see point 1) above. Subsequently, the CrlOcspRef entries corresponding to the values of point 2) above shall be added, in the same order as they appeared in the complete-certificate-references attribute. In the end, the CrlOcspRef elements corresponding to point 3) above may be added.

When creating a crlValidatedID, the crlHash shall be computed over the entire DER encoded CRL including the signature.

The crlIdentifier should be present unless the CRL can be inferred from other information.

The crlIdentifier shall identify the CRL using the issuer name and the CRL issued time, which shall correspond to the time thisUpdate contained in the issued CRL, and if present, the crlNumber.

In the case that the identified CRL is a Delta CRL, then references to the set of CRLs to provide a complete revocation list shall be included.

The OcspIdentifier shall identify the OCSP response using the issuer name and the time of issue of the OCSP response, which shall correspond to the time produced as contained in the issued OCSP response.

The ocspRefHash should be included.

NOTE 3: In earlier versions of ETSI TS 101 733 [1], the ocspRefHash field was optional. In order to provide backward compatibility, the ASN.1 structure was not changed.

NOTE 4: The absence of the ocspRefHash field makes OCSP responses substitutions attacks possible, if for instance OCSP responder keys are compromised. In this case, out-of-band mechanisms can be used to ensure that none of the OCSP responder keys have been compromised at the time of validation.

The ocspRefHash shall include the digest of the OCSP responses using the types stated in clause 5.4.2.1.

NOTE 5: Copies of the CRL and OCSP responses values can be held using the revocation-values attribute defined in clause A.1.2.2 or within SignedData.crls.

The syntax and semantics of other revocation references are outside the scope of the present document. The definition of the syntax of the other form of revocation information shall be as identified by OtherRevRefType.

This attribute may include the references to the full set of the CRL, or OCSP responses that have been used to verify the certification chain for any TSUs that provide time-stamp tokens. In this case, the unsigned attribute shall be added to the SignedData of the relevant time-stamp token.

NOTE 6: In the case of a content-time-stamp, the time-stamp token cannot be changed after the signature without invalidating the signature. Consequently, this unsigned attribute needs to be added before signing."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A.1.2.2 (The revocation-values attribute)",
        "testo": (
            "Attributo unsigned che deve contenere i valori dei dati di revoca "
            "corrispondenti ai riferimenti elencati in complete-revocation-references e "
            "attribute-revocation-references che non siano gia' presenti in "
            "SignedData.crls; nessun altro elemento deve essere incluso. Il valore deve "
            "essere un'istanza del tipo ASN.1 RevocationValues e l'attributo deve essere "
            "identificato dall'OID id-aa-ets-revocationValues."
        ),
        "testo_integrale": (
            """Semantics

The revocation-values attribute shall be an unsigned attribute.

The revocation-values attribute:

1) Shall contain the elements corresponding to the references in complete-revocation-references (clause A.1.2.1) and attribute-revocation-references (clause A.1.4), which are not stored in SignedData.crls.

2) No other element shall be included.

The revocation-values attribute should be used in preference to the OtherRevocationInfoFormat specified in IETF RFC 5652 [7] to maintain backwards compatibility with the earlier version of ETSI TS 101 733 [1].

Syntax

The revocation-values attribute shall contain exactly one component of AttributeValue type.

The revocation-values attribute value shall be an instance of RevocationValues ASN.1 type.

The revocation-values attribute shall be identified by the id-aa-ets-revocationValues OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

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
  WITH SYNTAX &Type ID &id }

The syntax and semantics of the contents of OtherRevVals field are outside the scope of the present document. The definition of the syntax of the other form of revocation information shall be as identified by OtherRevRefType.

CertificateList shall be as defined in clause 4.8.2.

OCSP responses shall be included using the types stated in clause 5.4.2.1.

If an OCSP response is of type OCSPResponse, it shall be included within otherRevVals using the OID id-ri-ocsp-response (1.3.6.1.5.5.7.16.2).

This attribute may include the values of revocation data including CRLs and OCSPs for any TSUs that have provided the time-stamp tokens, if these certificates are not already included in the TSTs as part of the TSUs signatures. In this case, the unsigned attribute shall be added to the SignedData of the relevant time-stamp token.

NOTE: In the case of a content-time-stamp, the time-stamp token cannot be changed after the signature without invalidating the signature. Consequently, this unsigned attribute needs to be added before signing or somewhere else within the signature, if needed."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A.1.3 (The attribute-certificate-references attribute)",
        "testo": (
            "Attributo unsigned che elenca i riferimenti ai certificati impiegati per "
            "validare i certificati di attributo e le asserzioni firmate incorporati "
            "nella firma CAdES (trust anchor, certificati di CA nel percorso del "
            "certificato di firma, certificati di firma degli stessi), limitatamente a "
            "quelli non gia' presenti in complete-certificate-references; puo' anche "
            "contenere i riferimenti ai certificati usati per firmare CRL o risposte "
            "OCSP. Il valore deve essere un'istanza del tipo ASN.1 "
            "AttributeCertificateRefs e l'attributo deve essere identificato dall'OID "
            "id-aa-ets-attrCertificateRefs."
        ),
        "testo_integrale": (
            """Semantics

The attribute-certificate-references attribute shall be an unsigned attribute.

The attribute-certificate-references attribute:

1) Shall contain, if they are not present within complete-certificate-references attribute, the references to the trust anchor and the references to CA certificates within the path of the signing certificate(s) of the attribute certificate(s) and signed assertion(s) incorporated to the CAdES signature. References present within complete-certificate-references attribute should not be included.

2) Shall contain, if they are not present within complete-certificate-references attribute, the reference(s) to the signing certificate(s) of the attribute certificate(s) and signed assertion(s) incorporated to the CAdES signature. References present within complete-certificate-references attribute should not be included.

3) May contain references to the certificates used to sign CRLs or OCSP responses and certificates within their respective certificate paths, which are used for validating the signing certificate(s) of the attribute certificate(s) and signed assertion(s) incorporated to the CAdES signature. References present within complete-certificate-references attribute should not be included.

Syntax

The attribute-certificate-references attribute shall contain exactly one component of AttributeValue type.

The attribute-certificate-references attribute value shall be an instance of AttributeCertificateRefs ASN.1 type.

The attribute-certificate-references attribute shall be identified by the id-aa-ets-attrCertificateRefs OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-attrCertificateRefs OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 44 }

AttributeCertificateRefs ::=         SEQUENCE OF OtherCertID

NOTE: Copies of the certificate values referenced here can be held using the certificate-values attribute defined in clause A.1.1.2 or within SignedData.certificates. The attribute certificate itself is stored in the signer-attributes-v2 as defined in clause 5.2.6.1."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A.1.4 (The attribute-revocation-references attribute)",
        "testo": (
            "Attributo unsigned che elenca i riferimenti ai dati di revoca dei "
            "certificati impiegati per validare i certificati di attributo e le "
            "asserzioni firmate incorporati nella firma CAdES, limitatamente a quelli "
            "non gia' presenti in complete-revocation-references e senza riferimenti di "
            "revoca per la trust anchor. Il valore deve essere un'istanza del tipo ASN.1 "
            "AttributeRevocationRefs, identificato dall'OID id-aa-ets-attrRevocationRefs; "
            "se una CRL identificata e' una Delta CRL l'attributo deve includere i "
            "riferimenti all'insieme di CRL necessario a fornire liste di revoca "
            "complete."
        ),
        "testo_integrale": (
            """Semantics

The attribute-revocation-references attribute shall be an unsigned attribute.

The attribute-revocation-references attribute:

1) Shall contain, if they are not present within the complete-revocation-references attribute, the references to the revocation values corresponding to CA certificates within the path(s) of the signing certificate(s) of the attribute certificate(s) and signed assertion(s) incorporated to the CAdES signature. It shall not contain references to revocation values for the trust anchor. References present within complete-revocation-references attribute should not be included.

NOTE 1: A trust anchor is by definition trusted, thus no revocation information for the trust anchor is used during the validation.

2) Shall contain, if they are not present within the complete-revocation-references attribute, the references to the revocation value(s) for the signing certificate(s) of the attribute certificate(s) and signed assertion(s) incorporated to the CAdES signature. References present within complete-revocation-references attribute should not be included.

3) May contain references to the revocation values on certificates used to sign CRLs or OCSP responses and certificates within their respective certificate paths, which are used for validating the signing certificate(s) of the attribute certificate(s) and signed assertion(s) incorporated to the CAdES signature. References present within complete-revocation-references attribute should not be included.

Syntax

The attribute-revocation-references attribute shall contain exactly one AttributeValue.

The attribute-revocation-references attribute value shall be an instance of AttributeRevocationRefs ASN.1 type.

The attribute-revocation-references attribute shall be identified by the id-aa-ets-attrRevocationRefs OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-attrRevocationRefs OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 45 }

AttributeRevocationRefs ::=       SEQUENCE OF CrlOcspRef

NOTE 2: Copies of the CRL and OCSP responses values referenced here can be held using the revocation-values attribute defined in clause A.1.2.2 or within SignedData.crls.

Should one or more of the identified CRLs be a Delta CRL, this attribute shall include references to the set of CRLs required to provide complete revocation lists."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A.1.5.1 (The time-stamped-certs-crls-references attribute)",
        "testo": (
            "Attributo unsigned che incapsula una marca temporale sugli attributi "
            "complete-certificate-references e complete-revocation-references: il campo "
            "messageImprint della marca deve essere l'hash dei valori concatenati dei due "
            "attributi, ciascuno incluso con attrType e attrValues (tipo e lunghezza "
            "compresi) ma senza tipo e lunghezza della SEQUENCE esterna. Il valore deve "
            "essere un'istanza del tipo ASN.1 TimestampedCertsCRLs e l'attributo deve "
            "essere identificato dall'OID id-aa-ets-certCRLTimestamp; gli attributi "
            "marcati temporalmente dovrebbero essere codificati in DER."
        ),
        "testo_integrale": (
            """Semantics

The time-stamped-certs-crls-references attribute shall be an unsigned attribute.

The time-stamped-certs-crls-references attribute shall encapsulate one time-stamp token of the complete-certificate-references attribute and the complete-revocation-references attribute.

Syntax

The time-stamped-certs-crls-references attribute shall contain exactly one component of AttributeValue type.

The time-stamped-certs-crls-references attribute value shall be an instance of TimestampedCertsCRLs ASN.1 type.

The time-stamped-certs-crls-references attribute shall be identified by the id-aa-ets-certCRLTimestamp OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-certCRLTimestamp OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 26}

TimestampedCertsCRLs ::= TimeStampToken

This attribute shall encapsulate one time-stamp token, whose messageImprint field shall be the hash of the concatenated values of the following data objects, as present within the electronic signature:

  • complete-certificate-references attribute; and

  • complete-revocation-references attribute.

Each attribute shall be included in the hash with the attrType and attrValues (including type and length) but without the type and length of the outer SEQUENCE.

The attributes being time-stamped should be encoded in DER (see clause 4.7.1). If DER is not employed, then the binary encoding of the ASN.1 structures being time-stamped should be preserved to ensure that the recalculation of the data hash is consistent.

For further information and definition of TimeStampToken, see clause 4.8.1."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A.1.5.2 (The CAdES-C-timestamp attribute)",
        "testo": (
            "Attributo unsigned che incapsula una marca temporale che copre la firma, la "
            "marca temporale di firma, l'attributo complete-certificate-references e "
            "l'attributo complete-revocation-references. Il valore deve essere un'istanza "
            "del tipo ASN.1 ESCTimeStampToken e l'attributo deve essere identificato "
            "dall'OID id-aa-ets-escTimeStamp; il campo messageImprint deve essere l'hash "
            "dei valori concatenati dei quattro oggetti elencati (senza la codifica di "
            "tipo o lunghezza per ciascun valore) e gli attributi marcati temporalmente "
            "dovrebbero essere codificati in DER."
        ),
        "testo_integrale": (
            """Semantics

The CAdES-C-time-stamp attribute shall be an unsigned attribute.

The CAdES-C-time-stamp attribute shall encapsulate one time-stamp token covering the signature, the signature timestamp, the complete-certificate-references attribute; and complete-revocation-references attribute.

NOTE: This time-stamp covers the CAdES-E-C level signature as defined in ETSI EN 319 122-2 [i.6].

Syntax

The CAdES-C-time-stamp attribute shall contain exactly one component of AttributeValue type.

The CAdES-C-time-stamp attribute value shall be an instance of ESCTimeStampToken ASN.1 type.

The CAdES-C-time-stamp attribute shall be identified by the id-aa-ets-escTimeStamp OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-escTimeStamp OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 25}

ESCTimeStampToken ::= TimeStampToken

This attribute encapsulates one time-stamp token, whose messageImprint field shall be the hash of the concatenated values (without the ASN.1 type or length encoding for that value) of the following data objects:

  • OCTETSTRING of the signature field within SignerInfo;

  • signature-time-stamp;

  • complete-certificate-references attribute; and

  • complete-revocation-references attribute.

Each attribute shall be included in the hash with the attrType and attrValues (including type and length) but without the type and length of the outer SEQUENCE.

The attributes being time-stamped should be encoded in DER (see clause 4.7.1). If DER is not employed, then the binary encoding of the ASN.1 structures being time-stamped should be preserved to ensure that the recalculation of the data hash is consistent.

For further information and definition of TimeStampToken, see clause 4.8.1."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A.2.1 (Usage of deprecated attributes)",
        "testo": (
            "L'Annex A.2 elenca gli attributi deprecati: sono mantenuti nel documento per "
            "agevolare la gestione delle firme storiche, ma non devono piu' essere "
            "aggiunti a una firma. Unica eccezione e' l'attributo long-term-validation, "
            "che puo' ancora essere aggiunto a firme che gia' lo contengono."
        ),
        "testo_integrale": (
            """Clause A.2 lists deprecated attributes. They are kept in the document to facilitate the handling of legacy signatures but they shall not be added any more to a signature. The only exception is the long-term-validation attribute that may still be added to signatures already containing a long-term-validation attribute."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A.2.2 (The other-signing-certificate attribute)",
        "testo": (
            "L'attributo other-signing-certificate definito in ETSI TS 101 733 e' "
            "deprecato: al suo posto deve essere usato l'attributo signing-certificate-v2 "
            "definito nella clausola 5.2.2.3."
        ),
        "testo_integrale": (
            """The other-signing-certificate attribute as defined in ETSI TS 101 733 [1], is deprecated. Instead, the signing-certificate-v2 attribute as defined in clause 5.2.2.3 shall be used."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A.2.3 (The signer-attributes attribute)",
        "testo": (
            "L'attributo signer-attributes definito in ETSI TS 101 733 e' deprecato: al "
            "suo posto deve essere usato l'attributo signer-attributes-v2 definito nella "
            "clausola 5.2.6.1."
        ),
        "testo_integrale": (
            """The signer-attributes attribute as defined in ETSI TS 101 733 [1], is deprecated. Instead the signer-attributes-v2 as defined in clause 5.2.6.1 shall be used."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A.2.4 (The archive-time-stamp attribute)",
        "testo": (
            "L'attributo archive-time-stamp (ATSv2) definito in ETSI TS 101 733 e' "
            "deprecato e non devono piu' essere creati nuovi attributi ATSv2; i sistemi "
            "possono prolungare la vita delle firme che contengono attributi ATSv2 "
            "incorporando i nuovi ATSv3 come descritto nella clausola 5.5.3."
        ),
        "testo_integrale": (
            """The archive-time-stamp (ATSv2) attribute as defined in ETSI TS 101 733 [1], is deprecated. New ATSv2 attributes shall not be created. Systems may extend the lifetime of signatures containing ATSv2 attributes by incorporating new ATSv3 as described in clause 5.5.3."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A.2.5 (The long-term-validation attribute)",
        "testo": (
            "L'uso dell'attributo long-term-validation definito in ETSI TS 101 733 e' "
            "deprecato e non devono piu' essere creati nuovi attributi "
            "long-term-validation; i sistemi possono prolungare la vita delle firme che "
            "li contengono incorporando i nuovi ATSv3 come definito nella clausola 5.5.3."
        ),
        "testo_integrale": (
            """The use of the long-term-validation attribute as defined in ETSI TS 101 733 [1], is deprecated. New long-term-validation attributes shall not be created. Systems may extend the lifetime of signatures containing long-term-validation attributes by incorporating new ATSv3 as defined in clause 5.5.3."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A.2.6 (The ats-hash-index attribute)",
        "testo": (
            "L'attributo ats-hash-index definito in ETSI TS 101 733 e' deprecato: al suo "
            "posto deve essere usato l'attributo ats-hash-index-v3 definito nella clausola "
            "5.5.2. La definizione ASN.1 del vecchio ats-hash-index puo' dare ambiguita' "
            "in decodifica se si usa l'algoritmo di hash predefinito e non gestiva "
            "l'aggiunta di valori a attributi unsigned gia' coperti da un ATSv3."
        ),
        "testo_integrale": (
            """The ats-hash-index attribute as defined in ETSI TS 101 733 [1], is deprecated. Instead the ats-hash-index-v3 as defined in clause 5.5.2 shall be used.

NOTE: The ASN.1 definition of the ats-hash-index can lead to ambiguities in the decoding if the default hash algorithm is used and was not able to handle the case where values were added to unsigned attributes already covered by an ATSv3."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex B (Alternative mechanisms for long term availability and integrity of validation data)",
        "testo": (
            "Un meccanismo di disponibilita' e integrita' a lungo termine dei dati di "
            "validazione diverso da quelli descritti nella clausola 5.5, se incorporato "
            "nella firma come attributo unsigned, deve specificare: la semantica e la "
            "sintassi dell'attributo, incluso il suo OID; la strategia con cui il "
            "meccanismo garantisce che tutte le parti necessarie della firma siano "
            "protette dall'attributo; la strategia di gestione delle firme che contengono "
            "gli attributi definiti nel presente documento (senza invalidare i token di "
            "marca temporale gia' presenti negli attributi ATSv3 e includendo tutto il "
            "materiale di validazione necessario); la strategia di gestione delle firme "
            "CAdES storiche, senza invalidare gli attributi gia' aggiunti."
        ),
        "testo_integrale": (
            """There may be mechanisms to achieve long term availability and integrity of validation data different from the ones described in clause 5.5.

If such a mechanism is incorporated using an unsigned attribute into the signature, then for this mechanism shall be specified:

1) The clear specification of the semantics and syntax of the attribute including its OID.

2) The strategy of how this mechanism guarantees that all necessary parts of the signature are protected by this attribute.

3) The strategy of how to handle signatures containing attributes defined in the present document. In particular, in case ATSv3 attributes are already included in the signature it shall be ensured that the previous time-stamp tokens within these attributes are not invalidated and that all validation material needed to validate the signature before the incorporation of the new attribute is incorporated into the signature and protected by the new attribute.

4) The strategy of how to handle legacy CAdES signatures. In particular it shall be guaranteed that in case of previously added attributes for long term availability and integrity of validation data they are not invalidated.

NOTE 1: Such mechanisms, defined outside of the present document, can be used to provide long term availability and integrity of validation data. However, they do not represent CAdES-B-LTA level as defined in clause 6 or CAdES-E-A levels as defined in ETSI EN 319 122-2 [i.6].

NOTE 2: Such mechanisms might be included in future versions of the present document and assigned to a corresponding CAdES level.

EXAMPLE: The attributes defined in IETF RFC 4998 [i.15], annex A are examples of such alternative mechanisms but they only handle points 1) and 2)."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "Annex C (Void)",
        "testo": (
            "L'Annex C del documento e' vuoto: il suo intero contenuto e' la dicitura "
            "'Void', senza alcuna disposizione ne' requisito."
        ),
        "testo_integrale": (
            """Void"""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "Annex A.1.1.1 (The complete-certificate-references attribute)",
    "Annex A.1.1.2 (The certificate-values attribute)",
    "Annex A.1.2.1 (The complete-revocation-references attribute)",
    "Annex A.1.2.2 (The revocation-values attribute)",
    "Annex A.1.3 (The attribute-certificate-references attribute)",
    "Annex A.1.4 (The attribute-revocation-references attribute)",
    "Annex A.1.5.1 (The time-stamped-certs-crls-references attribute)",
    "Annex A.1.5.2 (The CAdES-C-timestamp attribute)",
    "Annex A.2.1 (Usage of deprecated attributes)",
    "Annex A.2.2 (The other-signing-certificate attribute)",
    "Annex A.2.3 (The signer-attributes attribute)",
    "Annex A.2.4 (The archive-time-stamp attribute)",
    "Annex A.2.5 (The long-term-validation attribute)",
    "Annex A.2.6 (The ats-hash-index attribute)",
    "Annex B (Alternative mechanisms for long term availability and integrity of validation data)",
    "Annex C (Void)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Dieci rinvii interni al capitolo, tutti con puntatore di clausola letteralmente
# presente nel testo citante (evidence_type "textual"): i riferimenti incrociati
# fra le sottoclausole di A.1. I rinvii alle clausole 4.x/5.x di questa stessa
# Fonte, all'Annex D e alle fonti esterne sono elencati nel docstring e restano
# alla fase 6; le menzioni per solo nome di attributi "sorelle" non diventano
# archi (nessun puntatore di clausola).
RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "Annex A.1.1.1 (The complete-certificate-references attribute)"),
        "nodo_a": ("obbligo", None, "Annex A.1.3 (The attribute-certificate-references attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.1.1 (The complete-certificate-references attribute)"),
        "nodo_a": ("obbligo", None, "Annex A.1.1.2 (The certificate-values attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.1.2 (The certificate-values attribute)"),
        "nodo_a": ("obbligo", None, "Annex A.1.1.1 (The complete-certificate-references attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.1.2 (The certificate-values attribute)"),
        "nodo_a": ("obbligo", None, "Annex A.1.3 (The attribute-certificate-references attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.2.1 (The complete-revocation-references attribute)"),
        "nodo_a": ("obbligo", None, "Annex A.1.4 (The attribute-revocation-references attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.2.1 (The complete-revocation-references attribute)"),
        "nodo_a": ("obbligo", None, "Annex A.1.2.2 (The revocation-values attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.2.2 (The revocation-values attribute)"),
        "nodo_a": ("obbligo", None, "Annex A.1.2.1 (The complete-revocation-references attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.2.2 (The revocation-values attribute)"),
        "nodo_a": ("obbligo", None, "Annex A.1.4 (The attribute-revocation-references attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.3 (The attribute-certificate-references attribute)"),
        "nodo_a": ("obbligo", None, "Annex A.1.1.2 (The certificate-values attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.4 (The attribute-revocation-references attribute)"),
        "nodo_a": ("obbligo", None, "Annex A.1.2.2 (The revocation-values attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from seed_data.lib import verifica_completezza_testo_integrale, verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    verifica_completezza_testo_integrale([sys.modules[__name__]])
    print(
        f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
        f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti, "
        f"{len(RELAZIONI)} relazioni."
    )
