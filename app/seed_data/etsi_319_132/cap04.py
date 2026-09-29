"""ETSI EN 319 132-1 V1.3.1 (2024-07) - Electronic Signatures and Trust
Infrastructures (ESI); XAdES digital signatures; Part 1: Building blocks and
XAdES baseline signatures. Capitolo 4 dello split: clausola 5 (Qualifying
properties semantics and syntax), da 5.1 (Auxiliary syntax) a 5.2.8.1 (The
AllDataObjectsTimeStamp qualifying property) inclusa.

Provenienza del testo: app/.source_cache/etsi_319_132/cap04.txt (porzione
dello split deterministico; testo ufficiale completo in
app/.source_cache/etsi_319_132/raw.txt, raw_body.txt e raw.pdf). Versione
ETSI EN 319 132-1 V1.3.1 (2024-07), deliver "01.03.01_60"; da
app/.source_cache/etsi_319_132/provenance.json: data_fetch
2026-09-29T12:56:34Z, sha256_raw_pdf
83fc87ee09de90274131a1f60cb73edb742cebc7cd8961342586ed06133664c5, formato
"PDF ETSI deliver (pdftotext -layout)". Manifest di split:
app/.source_cache/etsi_319_132/manifest.json (cap04 = clausola 5; il capitolo
successivo, cap05.txt, riprende da 5.2.8.2). Questo modulo e' puro dato: non
importa nulla e non legge file; la numerazione degli id e' risolta per
riferimento dalla sessione principale in app/seed.py (che questo modulo NON
tocca).

## Perimetro e granularita' (ADR-0007)

20 item di indice = 20 righe: una riga per ciascuna sottoclausta numerata del
perimetro (5.1.1, 5.1.2, 5.1.3, 5.1.4.1, 5.1.4.2, 5.1.4.3, 5.1.4.4.1,
5.1.4.4.2.1, 5.1.4.4.2.2, 5.1.4.4.2.3, 5.1.4.5, 5.2.1, 5.2.2, 5.2.3, 5.2.4,
5.2.5, 5.2.6, 5.2.7.1, 5.2.7.2, 5.2.8.1), con la sua semantica e la sua
sintassi. In questa clausola lo standard non numera requisiti con id propri:
l'unita' di prescrizione e' la sottoclausta che definisce un tipo o una
qualifying property, delimitata dalle etichette "Semantics" e "Syntax".
Precedente della stessa famiglia (blocco B AdES): ETSI EN 319 122-1 cap03
(clausola 5, una sottoclausta/attributo = una riga) e cap04 (una
sottoclausta = una riga).

Intestazioni di puro raggruppamento, senza testo proprio, NON generano nodo
ne' item di indice: 5, 5.1, 5.1.4, 5.1.4.4, 5.1.4.4.2, 5.2, 5.2.7, 5.2.8.
Verificato sul testo: ciascuna e' seguita immediatamente dalla prima
sottoclausta, senza una riga propria da assorbire (stesso criterio gia'
applicato a ETSI EN 319 122-1 e alle altre fonti ETSI censite).

Gli elenchi interni a una sottoclausta restano dentro il nodo della
sottoclausta: le quattro voci di 5.1.4.2, le sei di 5.1.4.3, i tre punti sul
valore di URI in 5.1.4.4.2.1, i passi numerati dei due processing model
5.1.4.4.2.2 e 5.1.4.4.2.3, i passi 1)-2) con le lettere a)-d) di 5.2.8.1 e i
due requirements numerati 1)-2) di 5.2.2 e 5.2.3 sono dettaglio della stessa
prescrizione, non unita' autonome: nessuna voce nomina un soggetto proprio ne'
ha un indice con cui il documento la richiami altrove (criterio con cui ETSI
EN 319 102-1 cap04 tiene le procedure numerate nel nodo della clausola di
Processing). La granularita' per lettera/voce si applica dove il documento
numera requisiti propri e li usa come indice (ETSI EN 319 122-1 clausola 6.3,
lettere a)-t)); qui il documento numera solo clausole, tipi e property.

## Obbligo o Principio, riga per riga

- 5.1.1 (AnyType) -> Obbligo "tecnico/sicurezza": modello di contenuto del
  tipo, enunciato con "shall".
- 5.1.2 (ObjectIdentifierType) -> Obbligo "tecnico/sicurezza": requisiti su
  Identifier (unico e permanente, mai riassegnato), sui due meccanismi URI/OID
  e sui valori ammessi dell'attributo Qualifier.
- 5.1.3 (EncapsulatedPKIDataType) -> Obbligo "tecnico/sicurezza": contenuto
  base 64, valori ammessi dell'attributo Encoding, default DER.
- 5.1.4.1 (Semantics) -> Principio "scopo/ambito di applicazione": dichiara
  che cosa il documento specifica in materia di contenitori di marche
  temporali e che cosa queste possono marcare; nessun comportamento imposto
  ("may time-stamp").
- 5.1.4.2 (Containers for electronic time-stamps) -> Principio "definitorio":
  elenca le property contenitore definite dal documento e che cosa provano,
  senza prescrivere alcunche'.
- 5.1.4.3 (GenericTimeStampType) -> Obbligo "tecnico/sicurezza": requisiti sul
  tipo base, su ds:CanonicalizationMethod e sull'incapsulamento della marca
  temporale.
- 5.1.4.4.1 (Semantics and syntax) -> Obbligo "tecnico/sicurezza": uso
  prescritto del tipo XAdESTimeStampType per incorporare marche temporali.
- 5.1.4.4.2.1 (Semantics and syntax) -> Obbligo "tecnico/sicurezza":
  requisiti sull'elemento Include, sull'ordine di comparsa e sul valore
  dell'attributo URI.
- 5.1.4.4.2.2 (Processing model for URI attribute) -> Obbligo
  "tecnico/sicurezza": processing model prescrittivo ("shall be parsed",
  "shall be processed").
- 5.1.4.4.2.3 (Processing model for Include element) -> Obbligo
  "tecnico/sicurezza": i quattro passi prescritti ("shall be processed").
- 5.1.4.5 (OtherTimeStampType) -> Obbligo "tecnico/sicurezza": contenuto del
  tipo, input del calcolo dell'impronta, requisiti sui ReferenceInfo.
- 5.2.1 (SigningTime) -> Obbligo "tecnico/sicurezza": proprieta' firmata e
  contenuto del valore.
- 5.2.2 (SigningCertificateV2) -> Obbligo "tecnico/sicurezza": numero e ordine
  dei riferimenti, digest e identificatore di algoritmo, contenuto di
  IssuerSerialV2.
- 5.2.3 (CommitmentTypeIndication) -> Obbligo "tecnico/sicurezza": tipo di
  impegno espresso con URI, requisiti su CommitmentTypeId e sugli
  ObjectReference.
- 5.2.4 (DataObjectFormat) -> Obbligo "tecnico/sicurezza": contenuto minimo
  della property, obbligo su ObjectReference, uguaglianza dei valori MimeType
  ed Encoding.
- 5.2.5 (SignatureProductionPlaceV2) -> Obbligo "tecnico/sicurezza": indirizzo
  associato al firmatario e divieto di generare property vuote.
- 5.2.6 (SignerRoleV2) -> Obbligo "tecnico/sicurezza": requisiti su
  ClaimedRoles, CertifiedRolesV2 e SignedAssertions, divieto di generare
  property vuote.
- 5.2.7.1 (Countersignature identifier) -> Obbligo "tecnico/sicurezza":
  valore URI definito dal documento e costruzione prescritta del
  ds:Reference.
- 5.2.7.2 (CounterSignature) -> Obbligo "tecnico/sicurezza": contenuto della
  property, obbligo sul ds:Reference verso SignatureValue e sul digest,
  vincolo sulle controfirme dopo una marca temporale di archivio.
- 5.2.8.1 (AllDataObjectsTimeStamp) -> Obbligo "tecnico/sicurezza": marche
  temporali incapsulate, input del calcolo e suoi passi.

Nessun tipo di obbligo diverso da "tecnico/sicurezza": il capitolo vincola il
contenuto, la codifica e la costruzione della firma XAdES e dei suoi elementi
(tipi XML, attributi delle qualifying properties, controfirma, marche
temporali), non comportamenti organizzativi, informativi, procedurali, di
conservazione o sanzionatori. DUBBIO DI CLASSIFICAZIONE APERTO per la
revisione umana: i due processing model 5.1.4.4.2.2 e 5.1.4.4.2.3 prescrivono
come eseguire un'elaborazione e potrebbero essere "procedurale"; restano
"tecnico/sicurezza" per coerenza con il resto del capitolo e con ETSI EN 319
102-1 cap04 (procedure di convalida censite come tecnico/sicurezza).

Soggetti: valorizzati solo dove il testo nomina davvero il soggetto. "the
signer" -> 'Utente/titolare' obbligato in 5.2.1 (l'ora dichiarata dal
firmatario), 5.2.3 (impegno assunto dal firmatario), 5.2.5 (indirizzo
associato al firmatario) e 5.2.6 (attributi del firmatario); stesso criterio
con cui ETSI EN 319 122-1 cap03 assegna 'Utente/titolare' obbligato alle
proprie clausole che nominano "the signer". Tutte le altre righe restano
senza soggetti: il testo prescrive sul tipo o sull'elemento ("the X
qualifying property shall ...", "The Identifier element shall ...") e non
nomina chi deve conformarsi. In 5.1.4.3, 5.1.4.4.1, 5.2.6 e 5.2.7.2 sono
nominati soggetti che non sono ne' obbligati ne' destinatari del requisito
(la TSA che genera la marca temporale, l'Attribute Authority che rilascia i
certificati di attributo, la terza parte che firma le assertion): non sono
mappati, per non attribuire loro un ruolo che il testo non assegna. In
5.2.7.2 la controfirma e' per definizione apposta da una parte terza rispetto
al firmatario, ma il testo non la nomina: la riga resta senza soggetti invece
di attribuirle 'Terza parte' per inferenza (stesso dubbio lasciato aperto da
ETSI EN 319 122-1 cap03 sulla clausola countersignature).

Nessun `oggetti_giuridici`: il testo nomina tipi XML, attributi XAdES, firme
XAdES e marche temporali elettroniche generiche, mai uno degli oggetti della
tassonomia eIDAS (firma elettronica qualificata, sigillo elettronico,
marca temporale elettronica qualificata, ...): l'oggetto_giuridico si dichiara
solo se il testo lo nomina davvero, e "electronic time-stamp" senza
qualificazione non e' la marca temporale elettronica qualificata. Stesso
criterio di ETSI EN 319 122-1 cap04.

`severita` e `sanzioni` assenti (standard tecnico, nessuna sanzione); `stato`
sempre "vigente"; `condizione_applicabilita` mai valorizzata: nessuna
sottoclausta del perimetro e' condizionata a un fatto esterno non tracciato
nel censimento (le condizioni interne, es. in 5.1.4.4.2.1 "when the Include
element and the time-stamped data object are in the same document", sono
parte della prescrizione e restano nel testo).

## Fedelta' dell'estrazione

- pie' di pagina e testatine delle pagine 21-35 ("ETSI" e "<n> ETSI EN 319
  132-1 V1.3.1 (2024-07)", separate da form feed): rimossi, sono paratesto di
  impaginazione intercalato alle sottoclausole dalle interruzioni di pagina.
- righe spezzate a meta' frase: ricucite in un'unica riga. Il trattino di fine
  riga appartiene sempre alla parola (mai una sillabazione da rimuovere): il
  nome del file di schema "1913201-" + "XAdES01903v132.xsd" e "DER-" +
  "encoded" sono ricomposti senza spazio.
- due interruzioni di pagina cadono dentro un blocco di schema XML (dentro
  <xsd:complexType name="OtherTimeStampType"> e dentro
  <xsd:complexType name="ClaimedRolesListType">): il blocco e' stato ricucito
  come continua nel testo ufficiale, senza righe vuote introdotte dal salto di
  pagina.
- l'intestazione della clausola NON e' ripetuta dentro `testo_integrale` (il
  riferimento del nodo la porta gia'); le etichette interne "Semantics" e
  "Syntax" sono mantenute e unite alla prima frase della loro sezione.
- elenchi: i pallini di primo livello restano "•", i sottopunti "-" restano
  "-", il carattere privato usato da pdftotext per i pallini di terzo livello
  e' normalizzato a "•" con indentazione crescente per livello (stessa
  normalizzazione gia' applicata a ETSI EN 319 122-1 cap03 e a ETSI TS 119 432
  cap04); i passi numerati "1)" e le lettere "a)" restano a inizio riga come
  nel testo.
- blocchi XML degli schemi: riportati per intero, con l'impaginazione del
  testo (comprese le righe che lo standard stesso spezza dentro un attributo,
  es. <xsd:element name="EncapsulatedTimeStamp"> / type=
  "EncapsulatedPKIDataType"/>), separati dal testo da riga vuota. Nessun
  carattere del testo ufficiale e' stato modificato o abbreviato.
- nessun refuso da segnalare nel perimetro e nessuna correzione apportata al
  testo dello standard.

## Esclusioni (paratesto, non contenuto normativo)

- front matter, Contents, Foreword, History, elenco dei riferimenti
  bibliografici (clausola 2 References) e tutte le clausole fuori dal
  perimetro: non fanno parte di cap04.txt e non sono censiti qui;
- intestazioni di raggruppamento della clausola 5 senza testo proprio
  (5, 5.1, 5.1.4, 5.1.4.4, 5.1.4.4.2, 5.2, 5.2.7, 5.2.8): nessun nodo e
  nessun item di indice, per non creare item fittizi;
- la figura di 5.2.7.2 ("Figure 1: Use of CounterSignature element"): e' un
  disegno, non testo estraibile; la didascalia e la frase che vi rinvia
  ("Figure 1 illustrates this qualifying property and its relationship with
  the countersigned XAdES signature.") restano nel `testo_integrale` della
  riga. Unico elemento del capitolo non riproducibile come testo: il
  contenuto grafico della figura.

## Rinvii demandati alla fase 6 (nessuna relazione creata verso di essi)

- clausole di altri capitoli dello stesso documento: 5.1.1, 5.1.2, 5.1.3,
  5.1.4.3 (semantica e sintassi), 5.1.4.4.1, 5.1.4.5, 5.2.1-5.2.6, 5.2.7.2 e
  5.2.8.1 rinviano alla clausola C.1 per la posizione del file di schema XML
  (Annex C, dentro cap08.txt); 5.1.4.3 e 5.1.4.4.2.3 rinviano alla clausola
  4.5 (canonicalizzazione) e 5.1.4.5 e 5.2.8.1 alla stessa clausola 4.5
  (clausola 4 General Syntax, cap03.txt); 5.1.4.4.1 rinvia alle clausole 5.3
  (cap05.txt), 5.5.2.3 (cap06.txt), A.1.5.1.2 e A.1.5.2.2 (Annex A,
  cap08.txt); 5.1.4.2 rinvia all'Annex A (SigAndRefsTimeStampV2,
  RefsOnlyTimeStampV2); 5.2.7.2 rinvia alla clausola 5.5.2 e alla clausola
  5.4.6 (entrambe dentro cap05.txt, che copre da 5.2.8.2 a 5.5.2.3 esclusa).
- rinvii a intestazioni di raggruppamento senza nodo proprio, che la fase 6
  collega alle partizioni generate dalle righe di questo modulo: 5.1.4.3 ->
  "clause 5.1.4.4" (contenuto nel nodo 5.1.4.4.1) e 5.1.4.4.1 ->
  "Clause 5.1.4.4.2" (contenuto nel nodo 5.1.4.4.2.1).
- norme e specifiche esterne: XMLDSIG [1] (5.1.3, 5.1.4.3, 5.1.4.5,
  5.1.4.4.2.3, 5.2.7.2, 5.2.8.1), IETF RFC 3061 [8] (5.1.2), IETF RFC 3161 [7] e IETF RFC
  5816 [16] (5.1.4.3, 5.1.4.4.2.3), IETF RFC 5035 [17] (5.2.2), IETF RFC 2045
  [18] (5.2.4), Recommendation ITU-T X.509 [4] (5.2.6), SAML [i.9] (5.2.6),
  ETSI TS 119 172-1 [i.7] (5.2.3).

## Relazioni dichiarate

Otto relazioni "richiama" fra righe di questo modulo. Cinque con
`evidence_type` "textual" (citazione letterale del numero di clausola nel
`testo_integrale` del nodo citante): 5.1.4.3 -> 5.1.4.5 ("clause 5.1.4.5 for
OtherTimeStampType"); 5.1.4.4.1 -> 5.2.8.1 (fra le clausole del meccanismo
implicito, "clauses 5.2.8.1, 5.3, ..."); 5.1.4.4.2.1 -> 5.1.4.4.2.3 (la NOTE
rinvia a "clause 5.1.4.4.2.3"); 5.1.4.4.2.3 -> 5.1.4.4.2.2 (il passo 1) rinvia
a "clause 5.1.4.4.2.2"); 5.2.8.1 -> 5.1.4.4.1 ("see clause 5.1.4.4.1").
Tre con `evidence_type` "inferred" (l'evidenza e' il contenuto, non un numero
di clausola): 5.1.4.5 -> 5.1.4.4.1 ("shall be used exactly as in
XAdESTimeStampType"), 5.2.3 -> 5.1.2 e 5.2.4 -> 5.1.2 (CommitmentTypeId
"element of ObjectIdentifierType type" / elemento ObjectIdentifier di quel
tipo).
`confidence` resta null su tutte: non esiste uno score reale da riportare
(ADR-0005).

## Copertura

20 item di indice, 20 righe: 18 obblighi + 2 principi. Nessun item doppio,
nessun item mancante, nessuna riga fuori indice.

## Dubbi di classificazione aperti (per la revisione umana)

1) 5.1.4.1 e' classificata Principio "scopo/ambito di applicazione": e' una
   sottoclausta "Semantics" che dichiara che cosa il documento specifica in
   questa materia, senza alcun "shall" (le marche temporali "may time-stamp").
   Se la revisione preferisse classificarla "definitorio" (delimita i tipi
   contenitore), la sostanza del testo non cambia.
2) 5.1.4.4.2.2 e 5.1.4.4.2.3 (processing model): tipo_obbligo alternativo
   "procedurale" (vedi sopra).
3) 5.2.7.2: possibile mappatura di 'Terza parte' obbligata, non fatta perche'
   il testo nomina la controfirma e non il controfirmatario.
4) 5.1.4.3, 5.1.4.4.1, 5.2.6: i soggetti nominati ma non obbligati (TSA,
   Attribute Authority, terza parte che firma le assertion) restano fuori da
   `soggetti`; se la revisione preferisse tracciarli, la categoria sarebbe
   'Terza parte'.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 5.1.1 (The AnyType data type)",
        "testo": (
            "Il tipo AnyType deve avere un modello di contenuto che ammetta una sequenza di elementi XML "
            "arbitrari di lunghezza illimitata (mescolati a testo), che ammetta il solo contenuto testuale e "
            "che ammetta un numero illimitato di attributi arbitrari sull'elemento. La sintassi e' quella "
            "definita nel file di schema XML 1913201-XAdES01903v132.xsd, la cui collocazione e' indicata "
            "nella clausola C.1 e che e' copiato nella stessa sottoclausta per informazione."
        ),
        "testo_integrale": (
            """Semantics: The AnyType Schema data type shall have a content model allowing a sequence of arbitrary XML elements that (mixed with text) is of unrestricted length.

The AnyType Schema data type shall have a content model allowing for text content only.

The AnyType Schema data type shall have a content model allowing an element of this data type to bear an unrestricted number of arbitrary attributes.

Syntax: The AnyType type shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="Any" type="AnyType"/>

    <xsd:complexType name="AnyType" mixed="true">
    <xsd:sequence minOccurs="0" maxOccurs="unbounded">
        <xsd:any namespace="##any" processContents="lax"/>
    </xsd:sequence>
    <xsd:anyAttribute namespace="##any"/>
</xsd:complexType>

NOTE: The AnyType data type is used throughout the remaining parts of the present document wherever the content of an XML element has been left open."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.1.2 (The ObjectIdentifierType data type)",
        "testo": (
            "Le istanze del tipo ObjectIdentifierType devono contenere un identificatore unico e permanente "
            "di un oggetto (una volta assegnato, non puo' essere riassegnato) e possono contenere una "
            "descrizione testuale e riferimenti documentali. L'elemento Identifier ammette due meccanismi: se "
            "l'oggetto e' identificato da un URI, il valore deve essere quell'URI senza attributo Qualifier; "
            "se e' identificato da un OID, il valore deve essere l'OID codificato come URN (Qualifier = "
            "OIDASURN, codifica IETF RFC 3061) o come URI non URN (Qualifier = OIDAsURI); se esistono "
            "entrambi, dovrebbe essere usato l'URI."
        ),
        "testo_integrale": (
            """Semantics: Instances of ObjectIdentifierType data type shall contain a unique and permanent identifier of one data object.

Instances of ObjectIdentifierType data type may contain a textual description of the nature of the data object qualified by the instance of the ObjectIdentifierType data type.

Instances of ObjectIdentifierType data type may contain a number of references to documents where additional information about the nature of the data object qualified by the instance of the ObjectIdentifierType data type, can be found.

Syntax: The ObjectIdentifierType shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="ObjectIdentifier" type="ObjectIdentifierType"/>

<xsd:complexType name="ObjectIdentifierType">
  <xsd:sequence>
    <xsd:element name="Identifier" type="IdentifierType"/>
    <xsd:element name="Description" type="xsd:string" minOccurs="0"/>
    <xsd:element name="DocumentationReferences"
     type="DocumentationReferencesType" minOccurs="0"/>
  </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="IdentifierType">
  <xsd:simpleContent>
    <xsd:extension base="xsd:anyURI">
      <xsd:attribute name="Qualifier" type="QualifierType"
        use="optional"/>
    </xsd:extension>
  </xsd:simpleContent>
</xsd:complexType>

<xsd:simpleType name="QualifierType">
  <xsd:restriction base="xsd:string">
    <xsd:enumeration value="OIDAsURI"/>
    <xsd:enumeration value="OIDAsURN"/>
  </xsd:restriction>
</xsd:simpleType>

<xsd:complexType name="DocumentationReferencesType">
  <xsd:sequence maxOccurs="unbounded">
    <xsd:element name="DocumentationReference" type="xsd:anyURI"/>
  </xsd:sequence>
</xsd:complexType>

The Identifier element shall contain a permanent identifier. Once the identifier is assigned, it shall not be re-assigned again.

The Identifier element supports two mechanisms for identifying objects:

  •   if a URI identifies the object, then the value of the Identifier element shall be this URI and the Qualifier attribute shall not be present; or

  •   if an Object Identifier (OID) identifies the object, then the value of the Identifier element shall be the OID value encoded either as a Uniform Resource Name (URN), or as URI that is not a URN. The following rules shall apply in this case:

    -   if the OID is encoded as a URN, then:

      •   the Qualifier attribute shall be present and shall have the value "OIDASURN"; and

      •   the OID shall be encoded as an URN as specified by the IETF RFC 3061 [8]; or

    -   if the OID is encoded as a URI that is not a URN, then the Qualifier attribute shall be present and shall have the value "OIDAsURI".

If both an OID and a URI exist identifying one object, the URI value should be used in the Identifier element.

The Description element shall contain an informal text describing the object.

The DocumentationReferences element shall contain an arbitrary number of references pointing to further explanatory documentation of the data object."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.1.3 (The EncapsulatedPKIDataType data type)",
        "testo": (
            "Il tipo EncapsulatedPKIDataType deve essere usato per incorporare oggetti PKI non XML nella "
            "firma XAdES (es. certificati X.509, elenchi di revoca, risposte OCSP, certificati di attributo, "
            "marche temporali): il contenuto e' l'oggetto PKI codificato in base 64, l'attributo Encoding "
            "deve essere un URI che identifica la codifica originale (DER, BER, CER, PER o XER) e in sua "
            "assenza i dati devono essere dati ASN.1 codificati in DER; l'attributo Id serve a referenziare "
            "l'elemento."
        ),
        "testo_integrale": (
            """Semantics: The EncapsulatedPKIDataType shall be used to incorporate PKI objects, which can be non-XML encoded, into the XAdES signature.

NOTE 1: Examples of such PKI objects, include X.509 certificates and revocation lists, OCSP responses, attribute certificates, and electronic time-stamps.

Syntax: The EncapsulatedPKIDataType type shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1, and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="EncapsulatedPKIData" type="EncapsulatedPKIDataType"/>

<xsd:complexType name="EncapsulatedPKIDataType">
  <xsd:simpleContent>
    <xsd:extension base="xsd:base64Binary">
      <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
      <xsd:attribute name="Encoding" type="xsd:anyURI"
        use="optional"/>
    </xsd:extension>
  </xsd:simpleContent>
</xsd:complexType>

The content of this data type shall be the PKI object, base-64 encoded as defined in [1].

The Encoding attribute value shall be a URI identifying the encoding used in the original PKI object. The following URIs shall be used:

  •   http://uri.etsi.org/01903/v1.2.2#DER for denoting that the original PKI data were ASN.1 data encoded in DER;

  •   http://uri.etsi.org/01903/v1.2.2#BER for denoting that the original PKI data were ASN.1 data encoded in BER;

  •   http://uri.etsi.org/01903/v1.2.2#CER for denoting that the original PKI data were ASN.1 data encoded in CER;

  •   http://uri.etsi.org/01903/v1.2.2#PER for denoting that the original PKI data were ASN.1 data encoded in PER; or

  •   http://uri.etsi.org/01903/v1.2.2#XER for denoting that the original PKI data were ASN.1 data encoded in XER.

If the Encoding attribute is not present, then the PKI data shall be ASN.1 data encoded in DER.

NOTE 2: In some clauses of the present document, specific XAdES qualifying properties related to these data restrict the encoding options to only one certain type of the aforementioned PKI data.

The Id attribute shall be used to reference an element of this data type."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.1.4.3 (The GenericTimeStampType data type)",
        "testo": (
            "Il tipo GenericTimeStampType deve permettere di incapsulare marche temporali conformi a IETF RFC "
            "3161 aggiornata dalla IETF RFC 5816 (istanze del tipo TimeStampToken), marche temporali XML, "
            "marche temporali in altri formati e piu' marche temporali per lo stesso insieme di oggetti, deve "
            "offrire mezzi per gestire marche temporali calcolate su componenti XAdES, su componenti XAdES e "
            "oggetti firmati separati o su dati esterni, e deve specificare meccanismi per identificare che "
            "cosa e' marcato e come generare l'input dell'impronta. La sintassi e' quella dello schema XML "
            "(clausola C.1); l'elemento ds:CanonicalizationMethod deve indicare l'algoritmo di "
            "canonicalizzazione (si applica la clausola 4.5), la marca temporale conforme a IETF RFC 3161 "
            "deve essere inclusa in EncapsulatedTimeStamp e quella codificata in XML in XMLTimeStamp."
        ),
        "testo_integrale": (
            """Semantics: The GenericTimeStampType type shall:

  •   allow encapsulating IETF RFC 3161 [7] updated by IETF RFC 5816 [16] electronic time-stamps, which shall be instances of TimeStampToken type specified in section 2.4.2 of IETF RFC 3161 [7];

  •   allow encapsulating XML electronic time-stamps;

  •   allow encapsulating other formats of electronic time-stamps;

  •   allow encapsulating more than one electronic time-stamp generated for the same set of data objects (each one issued by different TSAs, for instance);

  •   provide means for managing electronic time-stamps computed on XAdES components, electronic time-stamps computed on XAdES components and detached signed data objects, or electronic time-stamps computed on external data; and

  •   specify mechanisms for explicitly identifying what is time-stamped and how to generate the input data for the computation of the message imprint to be sent to the TSA.

Syntax: The GenericTimeStampType type shall be the abstract base type defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1, and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="Include" type="IncludeType"/>

<xsd:complexType name="IncludeType">
<xsd:attribute name="URI" type="xsd:anyURI" use="required"/>
<xsd:attribute name="referencedData" type="xsd:boolean" use="optional"/>
</xsd:complexType>

<xsd:element name="ReferenceInfo" type="ReferenceInfoType"/>

<xsd:complexType name="ReferenceInfoType">
  <xsd:sequence>
    <xsd:element ref="ds:DigestMethod"/>
    <xsd:element ref="ds:DigestValue"/>
  </xsd:sequence>
  <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
  <xsd:attribute name="URI" type="xsd:anyURI" use="optional"/>
</xsd:complexType>

<xsd:complexType name="GenericTimeStampType" abstract="true">
  <xsd:sequence>
    <xsd:choice minOccurs="0">
      <xsd:element ref="Include" minOccurs="0" maxOccurs="unbounded"/>
      <xsd:element ref="ReferenceInfo" maxOccurs="unbounded"/>
    </xsd:choice>
    <xsd:element ref="ds:CanonicalizationMethod" minOccurs="0"/>
    <xsd:choice maxOccurs="unbounded">
      <xsd:element name="EncapsulatedTimeStamp"
        type="EncapsulatedPKIDataType"/>
      <xsd:element name="XMLTimeStamp" type="AnyType"/>
    </xsd:choice>
  </xsd:sequence>
  <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

The ds:CanonicalizationMethod element shall indicate the canonicalization algorithm used for canonicalizing XML node sets resulting after retrieving (and processing when required) the data objects time-stamped by the electronic time-stamp(s).

Clause 4.5 shall apply when dealing with the ds:CanonicalizationMethod element.

If the electronic time-stamp generated by the TSA is conformant to IETF RFC 3161 [7] as updated by IETF RFC 5816 [16], it shall be included within the EncapsulatedTimeStamp element. If the electronic time-stamp generated by the TSA is encoded as XML [1] then it shall be included within XMLTimeStamp element.

Details on the different elements and supporting types are given in the clauses that define the two concrete types: clause 5.1.4.4 for XAdESTimeStampType and clause 5.1.4.5 for OtherTimeStampType."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.1.4.4.1 (Semantics and syntax)",
        "testo": (
            "Le istanze del tipo XAdESTimeStampType devono essere usate per incorporare nelle firme XAdES "
            "marche temporali su componenti XAdES, o su componenti XAdES e oggetti firmati separati. La "
            "sintassi e' quella dello schema XML (clausola C.1). Il tipo offre due meccanismi per "
            "identificare gli oggetti marcati e calcolare l'impronta: quello esplicito (elemento Include) e "
            "quello implicito, per cui le clausole che definiscono le singole property (5.2.8.1, 5.3, "
            "5.5.2.3, A.1.5.1.2 e A.1.5.2.2) stabiliscono che cosa e' marcato e come contribuisce all'input; "
            "i principi del meccanismo esplicito sono esposti in 5.1.4.4.2."
        ),
        "testo_integrale": (
            """Semantics: Instances of XAdESTimeStampType type shall be used for incorporating electronic time-stamps on XAdES components, or electronic time-stamps on XAdES components and detached signed data objects, into XAdES signatures.

Syntax: The XAdESTimeStampType type shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1, and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="XAdESTimeStamp" type="XAdESTimeStampType"/>

<xsd:complexType name="XAdESTimeStampType">
  <xsd:complexContent>
    <xsd:restriction base="GenericTimeStampType">
      <xsd:sequence>
        <xsd:element ref="Include" minOccurs="0" maxOccurs="unbounded"/>
        <xsd:element ref="ds:CanonicalizationMethod" minOccurs="0"/>
        <xsd:choice maxOccurs="unbounded">
          <xsd:element name="EncapsulatedTimeStamp" type="EncapsulatedPKIDataType"/>
          <xsd:element name="XMLTimeStamp" type="AnyType"/>
        </xsd:choice>
      </xsd:sequence>
      <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
    </xsd:restriction>
  </xsd:complexContent>
</xsd:complexType>

This type provides two mechanisms for identifying data objects that are time-stamped by the electronic time-stamp present in the container, and for specifying how to compute the electronic time-stamp's message imprint:

  •   Explicit. This mechanism shall use the Include element for referencing specific data objects and for indicating their contribution to the input of the message imprint's computation; or

  •   Implicit. For certain time-stamp container qualifying properties under certain circumstances, no explicit indications are required for knowing what data objects are time-stamped by the electronic time-stamps and how they contribute to the input of the message imprint's computation. The present document specifies, in the clauses defining such qualifying properties (clauses 5.2.8.1, 5.3, 5.5.2.3, A.1.5.1.2 and A.1.5.2.2), what data objects are time-stamped by the electronic time-stamps and how they contribute to the input of the message imprint's computation.

Clause 5.1.4.4.2 shows the principles that govern the explicit indication mechanism."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.1.4.4.2.1 (Semantics and syntax)",
        "testo": (
            "Gli elementi Include devono referenziare esplicitamente gli oggetti che contribuiscono all'input "
            "del calcolo dell'impronta della marca temporale (e che quindi sono marcati), e il loro ordine di "
            "comparsa deve indicare l'ordine di contribuzione. L'attributo URI deve referenziare un solo "
            "oggetto: con parte non frammento vuota e frammento XPointer bare-name se l'oggetto e' nello "
            "stesso documento, con parte non frammento non vuota altrimenti, e in tal caso uguale alla parte "
            "non frammento del Target (o dell'URI di QualifyingPropertiesReference) delle "
            "QualifyingProperties che racchiudono l'oggetto marcato; l'attributo referencedData non deve "
            "essere presente se l'oggetto non e' un ds:Reference e puo' esserlo se lo e'."
        ),
        "testo_integrale": (
            """Semantics: Include elements shall explicitly reference data objects that contribute to the input of the electronic time-stamp's message imprint computation, and consequently are time-stamped by the electronic time-stamp.

The order of appearance of the Include elements shall indicate the order in which the referenced data objects contribute to the input of the electronic time-stamp's message imprint computation.

Syntax: The URI attribute in Include element shall reference one data object that contributes to the input of the electronic time-stamp's message imprint computation.

The value of URI attribute follows the rules indicated below:

  •   It shall have an empty non-fragment part and a bare-name XPointer fragment when the Include element and the time-stamped data object are in the same document.

  •   It shall have a not empty non-fragment part and a bare-name XPointer fragment when the Include element and the time-stamped data object are not in the same document.

  •   If not empty, its non-fragment part shall be equal to:

    -   the non-fragment part of the Target attribute of the QualifyingProperties enclosing the Include element if the time-stamped data object is enveloped by the XAdES signature; or

    -   the non-fragment part of the URI attribute of the QualifyingPropertiesReference element referencing the QualifyingProperties element enveloping the time-stamped data object if this QualifyingProperties element is not enveloped by the XAdES signature.

If the object referenced by the URI attribute is not a ds:Reference element, the referencedData attribute shall not be present.

If the object referenced by the URI attribute is a ds:Reference element, the referencedData attribute may be present.

NOTE: The presence and value of referencedData attribute impacts the computation of the octets that will contribute to the input of the electronic time-stamp's message imprint computation as specified below in clause 5.1.4.4.2.3."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.1.4.4.2.2 (Processing model for URI attribute)",
        "testo": (
            "La risorsa recuperata deve essere analizzata (parsed) e poi deve essere processato l'XPointer "
            "bare-name: come contesto di valutazione si usa il nodo radice del documento XML che contiene "
            "l'elemento referenziato dalla parte non frammento del valore dell'attributo URI, e dal "
            "location-set risultante si deriva un node-set XPath sostituendo il nodo elemento E con E e tutti "
            "i suoi discendenti (testo, commenti, PI, elementi) e i nodi namespace e attributo di E e dei "
            "suoi discendenti, ed eliminando tutti i nodi commento."
        ),
        "testo_integrale": (
            """The retrieved resource shall be parsed, and then the bare-name XPointer shall be processed.

The bare-name XPointer shall be processed as follows:

1) use as XPointer evaluation context the root node of the XML document that contains the element referenced by the not-fragment part of URI attribute's value; and

2) derive a XPath node-set from the resultant location-set as indicated below:

a) replace the element node E retrieved by the bare-name XPointer with E plus all descendants of E (text, comments, PIs, elements) and all namespace and attribute nodes of E and its descendant elements; and

b) delete all the comment nodes."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.1.4.4.2.3 (Processing model for Include element)",
        "testo": (
            "Ogni elemento Include di una qualifying property contenitore di marche temporali deve essere "
            "processato: 1) recuperare l'oggetto referenziato nell'attributo URI come in 5.1.4.4.2.2; 2) se "
            "l'oggetto recuperato e' un ds:Reference e referencedData vale \"true\", prendere il risultato del "
            "processamento secondo il modello di XMLDSIG (clausola 4.4.3.2), altrimenti conservare l'oggetto "
            "recuperato; 3) se l'oggetto ottenuto e' un node set XML, canonicalizzarlo come in clausola 4.5; "
            "4) concatenare gli ottetti risultanti all'input del calcolo dell'impronta risultante dal "
            "processamento precedente."
        ),
        "testo_integrale": (
            """Each Include element within a time-stamp container qualifying property shall be processed as detailed below:

1) retrieve the data object referenced in the URI attribute as specified in clause 5.1.4.4.2.2;

2) if the retrieved data object is a ds:Reference element and the referencedData attribute is set to the value "true", take the result of processing the retrieved ds:Reference element according to the reference processing model of XMLDSIG [1], clause 4.4.3.2; otherwise keep the retrieved data object retrieved in 1);

3) if the data object obtained after step 2) is an XML node set, canonicalize it as specified in clause 4.5; and

4) concatenate the resulting octets to the input of the electronic time-stamp's message imprint computation resulting from previous processing as indicated in the corresponding time-stamp container qualifying property."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.1.4.5 (The OtherTimeStampType data type)",
        "testo": (
            "Il tipo derivato concreto OtherTimeStampType deve contenere marche temporali calcolate su una "
            "collezione di oggetti non incorporati nella firma XAdES: l'input effettivo del calcolo "
            "dell'impronta e' la concatenazione, nell'ordine di comparsa, degli elementi ReferenceInfo "
            "presenti, canonicalizzata come in clausola 4.5. Ogni ReferenceInfo deve contenere il digest di "
            "un oggetto esterno (l'attributo URI referenzia l'oggetto, ds:DigestMethod identifica l'algoritmo "
            "e ds:DigestValue il valore del digest in base 64); l'attributo Id e gli elementi "
            "ds:CanonicalizationMethod, EncapsulatedTimeStamp e XMLTimeStamp si usano come nel tipo "
            "XAdESTimeStampType."
        ),
        "testo_integrale": (
            """Semantics: This concrete derived type shall contain electronic time-stamps computed on a collection of data objects that are not incorporated into the XAdES signature.

Syntax: The OtherTimeStampType type shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="OtherTimeStamp" type="OtherTimeStampType"/>

<xsd:complexType name="OtherTimeStampType">
    <xsd:complexContent>
        <xsd:restriction base="GenericTimeStampType">
            <xsd:sequence>
                <xsd:element ref="ReferenceInfo" maxOccurs="unbounded"/>
                <xsd:element ref="ds:CanonicalizationMethod" minOccurs="0"/>
                <xsd:choice>
                    <xsd:element name="EncapsulatedTimeStamp"
                type="EncapsulatedPKIDataType"/>
                    <xsd:element name="XMLTimeStamp" type="AnyType"/>
            </xsd:choice>
            </xsd:sequence>
            <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
        </xsd:restriction>
    </xsd:complexContent>
</xsd:complexType>

For this type the actual input to the computation of the message imprint shall be the concatenation (in the order of appearance) of the present ReferenceInfo elements, canonicalized as specified in clause 4.5.

Each ReferenceInfo element shall contain the digest of one external data object.

The URI attribute shall reference the data object contributing to the input of the electronic time-stamp's message imprint. As in XMLDSIG, if it is omitted, the context where the XAdES signature is used shall allow to know the identity of the referenced object.

Element ds:DigestMethod shall identify the digest algorithm applied to the external data object.

Element ds:DigestValue shall contain the base-64 encoded value of the digest of the referenced data object.

Attribute Id shall be used for referencing this element from elsewhere.

Attribute Id and elements ds:CanonicalizationMethod, EncapsulatedTimeStamp and XMLTimeStamp shall be used exactly as in XAdESTimeStampType."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.1 (The SigningTime qualifying property)",
        "testo": (
            "La qualifying property SigningTime deve essere una qualifying property firmata che qualifica la "
            "firma e il suo valore deve indicare il momento in cui il firmatario dichiara di aver eseguito il "
            "processo di firma. Sintassi: elemento SigningTime di tipo xsd:dateTime, come definito nello "
            "schema XML (clausola C.1)."
        ),
        "testo_integrale": (
            """Semantics: The SigningTime qualifying property shall be a signed qualifying property that qualifies the signature.

The SigningTime qualifying property's value shall specify the time at which the signer claims to having performed the signing process.

Syntax: The SigningTime qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="SigningTime" type="xsd:dateTime"/>"""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.2 (The SigningCertificateV2 qualifying property)",
        "testo": (
            "La qualifying property SigningCertificateV2 deve essere una qualifying property firmata che "
            "qualifica la firma, deve contenere un riferimento al certificato di firma e puo' contenere "
            "riferimenti ad alcuni o tutti i certificati del percorso di certificazione (compreso il trust "
            "anchor quando e' un certificato); per ogni certificato deve contenere un digest e "
            "l'identificatore univoco dell'algoritmo usato per calcolarlo, e il primo riferimento deve essere "
            "quello del certificato di firma. CertDigest contiene il digest del certificato referenziato "
            "(ds:DigestMethod identifica l'algoritmo, ds:DigestValue il digest in base 64 calcolato sul "
            "certificato codificato DER); IssuerSerialV2 contiene la codifica base 64 di un'istanza DER del "
            "tipo IssuerSerial di IETF RFC 5035; l'attributo URI indica dove trovare il certificato."
        ),
        "testo_integrale": (
            """Semantics: The SigningCertificateV2 qualifying property shall be a signed qualifying property that qualifies the signature.

The SigningCertificateV2 qualifying property shall contain one reference to the signing certificate.

The SigningCertificateV2 qualifying property may contain references to some of or all the certificates within the signing certificate path, including one reference to the trust anchor when this is a certificate.

NOTE 1: For instance, the signature validation policy can mandate other certificates to be present which can include all the certificates up to the trust anchor.

For each certificate, the SigningCertificateV2 qualifying property shall contain a digest value together with a unique identifier of the algorithm that has been used to calculate it.

The first reference in SigningCertificateV2 qualifying property shall be the reference of the signing certificate.

Syntax: The SigningCertificateV2 qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="SigningCertificateV2" type="CertIDListV2Type"/>

<xsd:complexType name="CertIDListV2Type">
    <xsd:sequence>
        <xsd:element name="Cert" type="CertIDTypeV2" maxOccurs="unbounded"/>
    </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="CertIDTypeV2">
    <xsd:sequence>
        <xsd:element name="CertDigest" type="DigestAlgAndValueType"/>
        <xsd:element name="IssuerSerialV2" type="xsd:base64Binary" minOccurs="0"/>
    </xsd:sequence>
    <xsd:attribute name="URI" type="xsd:anyURI" use="optional"/>
</xsd:complexType>

<xsd:complexType name="DigestAlgAndValueType">
    <xsd:sequence>
        <xsd:element ref="ds:DigestMethod"/>
        <xsd:element ref="ds:DigestValue"/>
    </xsd:sequence>
</xsd:complexType>

The element CertDigest shall contain the digest of the referenced certificate.

CertDigest's children elements satisfy the following requirements:

1) ds:DigestMethod element shall identify the digest algorithm; and

2) ds:DigestValue element shall contain the base-64 encoded value of the digest computed on the DER-encoded certificate.

The content of IssuerSerialV2 element shall be the base-64 encoding of one DER-encoded instance of type IssuerSerial type defined in IETF RFC 5035 [17].

NOTE 2: The information in the IssuerSerialV2 element is only a hint, that can help to identify the certificate whose digest matches the value present in the reference. But the binding information is the digest of the certificate.

The URI attribute shall provide an indication of where the referenced certificate can be found.

NOTE 3: It is intended that this attribute be used as a hint, as implementations can have alternative ways for retrieving the referenced certificate if it is not found at the referenced place."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.3 (The CommitmentTypeIndication qualifying property)",
        "testo": (
            "La qualifying property CommitmentTypeIndication deve essere una qualifying property firmata che "
            "qualifica gli oggetti firmati e deve indicare un impegno assunto dal firmatario al momento della "
            "firma (per un sottoinsieme o per l'insieme completo degli oggetti firmati), esprimendo il tipo "
            "di impegno con un URI e potendo contenere qualificatori aggiuntivi. L'elemento CommitmentTypeId "
            "e' di tipo ObjectIdentifierType: il suo Identifier deve avere come valore un URI che identifica "
            "univocamente l'impegno e non deve avere l'attributo Qualifier; ogni ObjectReference deve "
            "referenziare un ds:Reference dentro ds:SignedInfo o dentro un ds:Manifest firmato; per un "
            "impegno su tutti gli oggetti firmati si usa un elemento vuoto AllSignedDataObjects oppure un "
            "ObjectReference per ciascun oggetto firmato tranne SignedProperties."
        ),
        "testo_integrale": (
            """Semantics: The CommitmentTypeIndication qualifying property shall be a signed qualifying property that qualifies signed data object(s).

The CommitmentTypeIndication qualifying property shall indicate one commitment made by the signer when signing.

The CommitmentTypeIndication qualifying property may indicate one commitment made by the signer for a subset of the set of signed data objects.

The CommitmentTypeIndication qualifying property may also indicate one commitment made by the signer for the complete set of signed data objects.

The CommitmentTypeIndication qualifying property shall express the commitment type with a URI.

The CommitmentTypeIndication qualifying property may contain a sequence of qualifiers providing more information about the commitment.

NOTE 1: The commitment type can be:

      •   defined as part of the signature policy, in which case, the commitment type has precise semantics that are defined as part of the signature policy; or

      •   be a registered type, in which case, the commitment type has precise semantics defined by registration, under the rules of the registration authority. Such a registration authority can be a trading association or a legislative authority.

NOTE 2: The specification of commitment type identifiers is outside the scope of the present document. For a list of predefined commitment type identifiers, see ETSI TS 119 172-1 [i.7].

Syntax: The CommitmentTypeIndication qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="CommitmentTypeIndication" type="CommitmentTypeIndicationType"/>

<xsd:complexType name="CommitmentTypeIndicationType">
    <xsd:sequence>
        <xsd:element name="CommitmentTypeId"
       type="ObjectIdentifierType"/>
        <xsd:choice>
            <xsd:element name="ObjectReference" type="xsd:anyURI"
         maxOccurs="unbounded"/>
            <xsd:element name="AllSignedDataObjects"/>
        </xsd:choice>
        <xsd:element name="CommitmentTypeQualifiers"
      type="CommitmentTypeQualifiersListType" minOccurs="0"/>
    </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="CommitmentTypeQualifiersListType">
    <xsd:sequence>
        <xsd:element name="CommitmentTypeQualifier"
      type="AnyType" minOccurs="0" maxOccurs="unbounded"/>
    </xsd:sequence>
</xsd:complexType>

The CommitmentTypeId element is an element of ObjectIdentifierType type, which fulfils the following requirements:

1) its Identifier child shall have a URI as value, uniquely identifying one commitment made by the signer; and

2) its Identifier child shall not have a Qualifier attribute (i.e. the aforementioned URI shall not represent an OID value).

Each ObjectReference shall reference one ds:Reference element within the ds:SignedInfo element or within a signed ds:Manifest element.

If a commitment is made only for a subset (different from the full set) of signed data objects, the CommitmentTypeIndication element shall incorporate one ObjectReference element for each one of signed data objects in the aforementioned subset.

If a certain commitment is made for all the signed data objects, the CommitmentTypeIndication qualifying property shall contain:

  •   one AllSignedDataObjects empty element; or

  •   one ObjectReference element for each one of the signed data objects except the SignedProperties element (XAdES signed qualifying properties).

The CommitmentTypeQualifiers element provides means to include additional qualifying information on the commitment made by the signer."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.4 (The DataObjectFormat qualifying property)",
        "testo": (
            "La qualifying property DataObjectFormat deve essere una qualifying property firmata che "
            "qualifica un oggetto firmato specifico e deve contenere informazioni che ne descrivono il "
            "formato (Description testuale, ObjectIdentifier del tipo assegnato da un'autorita', MimeType con "
            "valori definiti da IETF RFC 2045, Encoding), dovendo contenere almeno uno fra Description, "
            "ObjectIdentifier e MimeType. L'attributo ObjectReference deve referenziare il ds:Reference "
            "figlio di ds:SignedInfo o un ds:Manifest firmato che referenzia l'oggetto qualificato; se la "
            "property referenzia un ds:Reference che a sua volta referenzia un ds:Object della firma e questo "
            "ha gli attributi MimeType e/o Encoding, i figli MimeType ed Encoding di DataObjectFormat devono "
            "avere esattamente gli stessi valori, quando presenti."
        ),
        "testo_integrale": (
            """Semantics: The DataObjectFormat qualifying property shall be a signed qualifying property that qualifies one specific signed data object.

The DataObjectFormat qualifying property shall contain information that describes the format of the signed data object.

Syntax: The DataObjectFormat qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="DataObjectFormat" type="DataObjectFormatType"/>

<xsd:complexType name="DataObjectFormatType">
    <xsd:sequence>
        <xsd:element name="Description" type="xsd:string" minOccurs="0"/>
        <xsd:element name="ObjectIdentifier" type="ObjectIdentifierType"
      minOccurs="0"/>
        <xsd:element name="MimeType" type="xsd:string" minOccurs="0"/>
        <xsd:element name="Encoding" type="xsd:anyURI" minOccurs="0"/>
    </xsd:sequence>
    <xsd:attribute name="ObjectReference" type="xsd:anyURI"
   use="required"/>
</xsd:complexType>

Element Description shall contain textual information related to the signed data object.

Element ObjectIdentifier shall contain an identifier of the type of the signed data object, as assigned by an authority that defines that type.

Element MimeType shall contain a MIME type value indicating the format of the signed data object. Its content shall be a string containing values defined by IETF RFC 2045 [18].

Element Encoding shall contain an indication of the encoding of the signed data object.

This qualifying property shall contain at least one of the following elements: Description, ObjectIdentifier and MimeType.

The ObjectReference attribute shall reference the ds:Reference child of the ds:SignedInfo or a signed ds:Manifest element referencing the signed data object qualified by this qualifying property.

If the DataObjectFormat qualifying property references a ds:Reference that in turn references a ds:Object within the XAdES signature, and if this ds:Object element has the MimeType or (and) the Encoding attribute(s), then DataObjectFormat's children MimeType and Encoding shall have exactly the same values, if they are present."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.5 (The SignatureProductionPlaceV2 qualifying property)",
        "testo": (
            "La qualifying property SignatureProductionPlaceV2 deve essere una qualifying property firmata "
            "che qualifica il firmatario e deve specificare un indirizzo associato al firmatario in una "
            "determinata localita' geografica (es. la citta'). Sintassi: Tipo con i cinque elementi "
            "facoltativi City, StreetAddress, StateOrProvince, PostalCode e CountryName come definiti nello "
            "schema XML (clausola C.1); le qualifying property vuote non devono essere generate."
        ),
        "testo_integrale": (
            """Semantics: The SignatureProductionPlaceV2 qualifying property shall be a signed qualifying property that qualifies the signer.

The SignatureProductionPlaceV2 qualifying property shall specify an address associated with the signer at a particular geographical (e.g. city) location.

Syntax: The SignatureProductionPlaceV2 qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="SignatureProductionPlaceV2" type="SignatureProductionPlaceV2Type"/>

<xsd:complexType name="SignatureProductionPlaceV2Type">
    <xsd:sequence>
        <xsd:element name="City" type="xsd:string" minOccurs="0"/>
        <xsd:element name="StreetAddress" type="xsd:string" minOccurs="0"/>
        <xsd:element name="StateOrProvince" type="xsd:string" minOccurs="0"/>
        <xsd:element name="PostalCode" type="xsd:string" minOccurs="0"/>
        <xsd:element name="CountryName" type="xsd:string" minOccurs="0"/>
    </xsd:sequence>
</xsd:complexType>

Empty SignatureProductionPlaceV2 qualifying properties shall not be generated."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.6 (The SignerRoleV2 qualifying property)",
        "testo": (
            "La qualifying property SignerRoleV2 deve essere una qualifying property firmata che qualifica il "
            "firmatario e deve incapsulare gli attributi del firmatario (es. il ruolo), potendo incapsulare "
            "attributi dichiarati dal firmatario, attributi certificati in certificati di attributo "
            "rilasciati da un'Attribute Authority e/o assertion firmate da una terza parte. ClaimedRoles deve "
            "contenere una sequenza non vuota di ruoli dichiarati e non certificati; CertifiedRolesV2 una "
            "sequenza non vuota di attributi certificati (codifica base 64 di certificati di attributo X509 "
            "conformi a Raccomandazione ITU-T X.509, oppure certificati di attributo in sintassi diversa); "
            "SignedAssertions una sequenza non vuota di assertion firmate da una terza parte. Le qualifying "
            "property vuote non devono essere generate."
        ),
        "testo_integrale": (
            """Semantics: The SignerRoleV2 qualifying property shall be a signed qualifying property that qualifies the signer.

The SignerRoleV2 qualifying property shall encapsulate signer attributes (e.g. role). This qualifying property may encapsulate the following types of attributes:

  •   attributes claimed by the signer;

  •   attributes certified in attribute certificates issued by an Attribute Authority; or/and

  •   assertions signed by a third party.

Syntax: The SignerRoleV2 qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1, and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="SignerRoleV2" type="SignerRoleV2Type"/>

<xsd:complexType name="SignerRoleV2Type">
    <xsd:sequence>
        <xsd:element ref="ClaimedRoles" minOccurs="0"/>
        <xsd:element ref="CertifiedRolesV2" minOccurs="0"/>
        <xsd:element ref="SignedAssertions" minOccurs="0"/>
    </xsd:sequence>
</xsd:complexType>

<xsd:element name="ClaimedRoles" type="ClaimedRolesListType"/>
<xsd:element name="CertifiedRolesV2" type="CertifiedRolesListTypeV2"/>
<xsd:element name="SignedAssertions" type="SignedAssertionsListType"/>

<xsd:complexType name="ClaimedRolesListType">
    <xsd:sequence>
        <xsd:element name="ClaimedRole" type="AnyType" maxOccurs="unbounded"/>
    </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="CertifiedRolesListTypeV2">
    <xsd:sequence>
        <xsd:element name="CertifiedRole" type="CertifiedRoleTypeV2" maxOccurs="unbounded"/>
    </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="CertifiedRoleTypeV2">
    <xsd:choice>
        <xsd:element ref="X509AttributeCertificate"/>
        <xsd:element ref="OtherAttributeCertificate"/>
    </xsd:choice>
</xsd:complexType>

<xsd:element name="X509AttributeCertificate" type="EncapsulatedPKIDataType"/>
<xsd:element name="OtherAttributeCertificate" type="AnyType"/>

<xsd:complexType name="SignedAssertionsListType">
    <xsd:sequence>
        <xsd:element ref="SignedAssertion" maxOccurs="unbounded"/>
    </xsd:sequence>
</xsd:complexType>

<xsd:element name="SignedAssertion" type="AnyType"/>

The ClaimedRoles element shall contain a non-empty sequence of roles claimed by the signer but which are not certified.

Additional content types may be defined on a domain application basis and be part of this element.

NOTE 1: The namespaces given to the corresponding XML schemas allow their unambiguous identification in the case these attributes are expressed in XML syntax (e.g. SAML assertions [i.9] of different versions).

The CertifiedRolesV2 element shall contain a non-empty sequence of certified attributes, which shall be one of the following:

  •   the base-64 encoding of DER-encoded X509 attribute certificates conformant to Recommendation ITU-T X.509 [4] issued to the signer, within the X509AttributeCertificate element; or

  •   attribute certificates (issued, in consequence, by Attribute Authorities) in different syntax than the one specified in Recommendation ITU-T X.509 [4], within the OtherAttributeCertificate element. The definition of specific OtherAttributeCertificate is outside of the scope of the present document.

The SignedAssertions element shall contain a non-empty sequence of assertions signed by a third party.

NOTE 2: A signed assertion is stronger than a claimed attribute, since a third party asserts with a signature that the attribute of the signer is valid. However, it is less restrictive than an attribute certificate.

The definition of specific content types for SignedAssertions is outside of the scope of the present document.

NOTE 3: A possible content can be a signed SAML [i.9] assertion.

Empty SignerRoleV2 qualifying properties shall not be generated."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.7.1 (Countersignature identifier in Type attribute of ds:Reference)",
        "testo": (
            "Il documento definisce il valore URI http://uri.etsi.org/01903#CountersignedSignature: una firma "
            "XAdES che contiene un elemento ds:Reference con l'attributo Type uguale a questo valore indica "
            "che si tratta della controfirma della firma referenziata da quell'elemento. L'elemento "
            "ds:Reference deve essere costruito in modo che la controfirma firmi l'elemento ds:SignatureValue "
            "della firma controfirmata, e nel suo processamento si applicano tutte le regole di XMLDSIG."
        ),
        "testo_integrale": (
            """The present document defines the following URI value:

  •   http://uri.etsi.org/01903#CountersignedSignature.

A XAdES signature containing a ds:Reference element whose Type attribute has this value shall indicate that it is a countersignature of the signature referenced by this element.

The ds:Reference element shall be built so that the countersignature signs the ds:SignatureValue element of the countersigned signature.

All the XMLDSIG rules shall apply in the processing of the aforementioned ds:Reference element.

NOTE: The only purpose of this definition is to serve as an easy identification of a signature as being a countersignature."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.7.2 (Enveloped countersignatures: the CounterSignature qualifying property)",
        "testo": (
            "La qualifying property CounterSignature deve essere una qualifying property non firmata che "
            "qualifica la firma e deve contenere una controfirma della firma XAdES in cui e' incorporata (che "
            "puo' essere a sua volta una firma XAdES). Il contenuto deve essere una firma XMLDSIG o XAdES il "
            "cui ds:SignedInfo contenga un ds:Reference che referenzia l'elemento ds:SignatureValue della "
            "firma XAdES incorporante e controfirmata, con ds:DigestValue pari al digest codificato in base "
            "64 dell'elemento ds:SignatureValue completo e canonicalizzato (tag di apertura e chiusura "
            "inclusi); possono essere aggiunti altri ds:Reference. Una controfirma puo' a sua volta essere "
            "controfirmata con la stessa costruzione; una volta aggiunta una marca temporale di archivio, il "
            "contenuto delle controfirme incorporate non puo' essere modificato e i nuovi materiali di "
            "convalida si incorporano con il materiale xades:AnyValidationData (clausola 5.4.6)."
        ),
        "testo_integrale": (
            """Semantics: The CounterSignature qualifying property shall be an unsigned qualifying property that qualifies the signature.

The CounterSignature qualifying property shall contain one countersignature of the XAdES signature where CounterSignature is incorporated. This countersignature may also be a XAdES signature.

Syntax: The CounterSignature qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="CounterSignature" type="CounterSignatureType" />

<xsd:complexType name="CounterSignatureType">
    <xsd:sequence>
        <xsd:element ref="ds:Signature"/>
    </xsd:sequence>
    <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

NOTE 1: The Id attribute has been incorporated in the definition of CounterSignatureType for allowing this unsigned property to be referenced by a URI in case the signature uses indirect incorporation of properties and an electronic time-stamp container needs to refer to the counter-signature through an Include element.

The content of this qualifying property shall be a XMLDSIG [1] or XAdES signature whose ds:SignedInfo shall contain one ds:Reference element referencing the ds:SignatureValue element of the embedding and countersigned XAdES signature.

The content of the ds:DigestValue in the aforementioned ds:Reference element of the countersignature shall be the base-64 encoded digest of the complete (and canonicalized) ds:SignatureValue element (i.e. including the starting and closing tags) of the embedding and countersigned XAdES signature.

Other ds:Reference elements referencing other data objects may be added to the countersignature.

NOTE 2: This includes, for instance, ds:Reference elements referencing the ds:SignatureValue elements of previously existent CounterSignature elements. This allows for building arbitrarily long chains of explicit countersignatures.

A countersignature may itself be signed using a CounterSignature qualifying property, which shall have a ds:Reference element referencing the ds:SignatureValue of the first countersignature, built as described above.

NOTE 3: This is an alternative way of constructing arbitrarily long series of countersignatures, each one signing the ds:SignatureValue element of the one where it is directly embedded.

Once an archive time-stamp has been added to the XAdES signature (see clause 5.5.2 of the present document) the contents of any enveloped countersignature can not be modified. Therefore, if there is the need of incorporating new validation material for these countersignatures, this may be done using the xades:AnyValidationData unsigned qualifying material specified in clause 5.4.6 of the present document.

Figure 1 illustrates this qualifying property and its relationship with the countersigned XAdES signature.

Figure 1: Use of CounterSignature element"""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.8.1 (The AllDataObjectsTimeStamp qualifying property)",
        "testo": (
            "La qualifying property AllDataObjectsTimeStamp deve essere una qualifying property firmata che "
            "qualifica gli oggetti firmati e deve incapsulare una o piu' marche temporali generate prima "
            "della produzione della firma, il cui input di calcolo dell'impronta e' la concatenazione di "
            "tutti gli oggetti ottenuti processando come in XMLDSIG (clausola 4.4.3.2) tutti i ds:Reference "
            "di ds:SignedInfo tranne quello che referenzia l'elemento SignedProperties, nel loro ordine di "
            "comparsa. Per generarla si usa il meccanismo implicito (5.1.4.4.1) e l'input si calcola "
            "inizializzando un flusso di ottetti vuoto, processando ogni ds:Reference (recupero dell'oggetto, "
            "canonicalizzazione se node-set o applicazione delle trasformazioni, concatenazione degli "
            "ottetti)."
        ),
        "testo_integrale": (
            """Semantics: The AllDataObjectsTimeStamp qualifying property shall be a signed qualifying property that qualifies signed data objects.

The AllDataObjectsTimeStamp qualifying property shall encapsulate one or more electronic time-stamps, generated before the signature production, whose message imprint computation input is the concatenation of all the objects obtained after processing as specified in XMLDSIG [1], clause 4.4.3.2; all the ds:Reference elements within the ds:SignedInfo except the one referencing the SignedProperties element, in their order of appearance.

Syntax: The AllDataObjectsTimeStamp qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="AllDataObjectsTimeStamp" type="XAdESTimeStampType"/>

The Implicit mechanism (see clause 5.1.4.4.1) shall be used for generating this qualifying property.

The input to the computation of the message imprint shall be computed as follows:

1) Initialize the final octet stream as an empty octet stream.

2) Take all the ds:Reference elements in their order of appearance within ds:SignedInfo, except the one referencing the SignedProperties element. Process each one as indicated below:

a) Retrieve the data object referenced by the URI attribute of the ds:Reference element, as specified in clause 4.4.3.2 of XMLDSIG [1].

NOTE 1: Clause 4.4.3.2 of XMLDSIG [1], specifies rules for URI dereferencing. For instance, it mandates that the dereferencing of a non 'same-document' reference (which XMLDSIG [1] defines as "a URI-Reference that consists of a hash sign ('#') followed by a fragment or alternatively consists of an empty URI") is always an octet-stream.

b) If the ds:Reference element does not contain the ds:Transforms element, then:

    -   if the retrieved data object is an XML node-set, then canonicalize it as specified in clause 4.5 of the present document;

    -   else proceed to step d).

c) If the ds:Reference element contains the ds:Transforms element, then apply all the transforms indicated within the ds:Transform children elements. After that:

    -   if the output of the last transform is a XML node-set according to XMLDSIG [1], canonicalize it as specified in clause 4.5 of the present document;

    -   else proceed to step d).

d) Concatenate the resulting octets to the final octet stream.

NOTE 2: Values of data objects referenced by ds:Reference elements present within signed ds:Manifest do not contribute to the message imprint computation input. However, the digest values of data objects that are referenced by ds:Reference elements within ds:Manifest elements that are referenced by ds:Reference elements within ds:SignedInfo, do contribute to the message imprint computation input."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 5.1.4.1 (Semantics)",
        "testo": (
            "Il presente documento specifica le qualifying property che fungono da contenitori di marche "
            "temporali elettroniche: le marche temporali contenute possono marcare elementi definiti in "
            "XMLDSIG, qualifying property del presente documento e/o oggetti firmati separati. La NOTE "
            "delimita l'ambito: una definizione di schema XML di un tipo base astratto e due tipi derivati "
            "concreti usati come contenitori, piu' un certo numero di qualifying property di quei tipi."
        ),
        "testo_integrale": (
            """The present document specifies qualifying properties that act as electronic time-stamps containers.

Electronic time-stamps within the aforementioned containers may time-stamp elements defined in XMLDSIG [1] and/or qualifying properties specified in the present document, and/or detached signed data objects.

NOTE: The present document specifies:

      •   an XML schema definition of an abstract base type and two concrete derived types used as containers for electronic time-stamps; and

      •   a number of qualifying properties of one of the aforementioned concrete types."""
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.1.4.2 (Containers for electronic time-stamps)",
        "testo": (
            "Elenca le qualifying property contenitore di marche temporali definite dal presente documento: i "
            "contenitori che provano che alcuni o tutti gli oggetti firmati sono stati creati prima di un "
            "certo istante (AllDataObjectsTimeStamp e IndividualDataObjectsTimeStamp), il contenitore che "
            "prova che SignatureValue e' stato creato prima di un certo istante (SignatureTimeStamp), il "
            "contenitore per firme XAdES a lungo termine (ArchiveTimeStamp, nel namespace della versione "
            "1.4.1) e le due property dell'Annex A (SigAndRefsTimeStampV2 e RefsOnlyTimeStampV2)."
        ),
        "testo_integrale": (
            """Below follows the list of the electronic time-stamps container qualifying properties that are defined by the present document:

  •   Containers for electronic time-stamps proving that some or all the signed data objects have been created before certain time instant: AllDataObjectsTimeStamp and IndividualDataObjectsTimeStamp;

  •   Container for electronic time-stamps proving that the SignatureValue element has been created before a certain time instant (to protect against repudiation in case of a key compromise): SignatureTimeStamp;

  •   Container for electronic time-stamps time-stamping the signature and validation data values, for providing long term XAdES signatures: ArchiveTimeStamp qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.4.1#; and

  •   Annex A specifies two qualifying properties that contain electronic time-stamps on qualifying properties that contain references to validation data, namely: SigAndRefsTimeStampV2 and RefsOnlyTimeStampV2."""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

# UNA riga per sottoclausta: il riferimento del nodo e' anche il suo item di indice.
INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 5.1.1 (The AnyType data type)",
    "clausola 5.1.2 (The ObjectIdentifierType data type)",
    "clausola 5.1.3 (The EncapsulatedPKIDataType data type)",
    "clausola 5.1.4.1 (Semantics)",
    "clausola 5.1.4.2 (Containers for electronic time-stamps)",
    "clausola 5.1.4.3 (The GenericTimeStampType data type)",
    "clausola 5.1.4.4.1 (Semantics and syntax)",
    "clausola 5.1.4.4.2.1 (Semantics and syntax)",
    "clausola 5.1.4.4.2.2 (Processing model for URI attribute)",
    "clausola 5.1.4.4.2.3 (Processing model for Include element)",
    "clausola 5.1.4.5 (The OtherTimeStampType data type)",
    "clausola 5.2.1 (The SigningTime qualifying property)",
    "clausola 5.2.2 (The SigningCertificateV2 qualifying property)",
    "clausola 5.2.3 (The CommitmentTypeIndication qualifying property)",
    "clausola 5.2.4 (The DataObjectFormat qualifying property)",
    "clausola 5.2.5 (The SignatureProductionPlaceV2 qualifying property)",
    "clausola 5.2.6 (The SignerRoleV2 qualifying property)",
    "clausola 5.2.7.1 (Countersignature identifier in Type attribute of ds:Reference)",
    "clausola 5.2.7.2 (Enveloped countersignatures: the CounterSignature qualifying property)",
    "clausola 5.2.8.1 (The AllDataObjectsTimeStamp qualifying property)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Otto rinvii interni al perimetro di questo capitolo (vedi docstring). Nessuna
# relazione verso altri capitoli di questa fonte o verso altre fonti: le
# partizioni e i collegamenti cross-fonte sono costruiti dalla sessione principale
# in fase 6 (ADR-0009, ADR-0012).
RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.4.3 (The GenericTimeStampType data type)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4.5 (The OtherTimeStampType data type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.4.4.1 (Semantics and syntax)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.8.1 (The AllDataObjectsTimeStamp qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.4.4.2.1 (Semantics and syntax)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4.4.2.3 (Processing model for Include element)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.4.4.2.3 (Processing model for Include element)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4.4.2.2 (Processing model for URI attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.4.5 (The OtherTimeStampType data type)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4.4.1 (Semantics and syntax)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.3 (The CommitmentTypeIndication qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.2 (The ObjectIdentifierType data type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.4 (The DataObjectFormat qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.2 (The ObjectIdentifierType data type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.8.1 (The AllDataObjectsTimeStamp qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4.4.1 (Semantics and syntax)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
