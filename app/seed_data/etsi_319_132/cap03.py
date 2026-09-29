"""ETSI EN 319 132-1 V1.3.1 (2024-07) - Electronic Signatures and Trust
Infrastructures (ESI); XAdES digital signatures; Part 1: Building blocks and
XAdES baseline signatures. Blocco B (famiglia AdES del lotto 2). Capitolo 3
dello split: clausola 4 (General Syntax) - 4.1 (General requirements), 4.2
(XML Namespaces), 4.3.1-4.3.7 (container QualifyingProperties, SignedProperties,
UnsignedProperties, SignedSignatureProperties, SignedDataObjectProperties,
UnsignedSignatureProperties, UnsignedDataObjectProperties), 4.4.1-4.4.3
(incorporazione delle qualifying properties nella firma XAdES) e 4.5 (Managing
canonicalization of XML nodesets). Conteggio di questo capitolo: 13 Obblighi,
0 Principi, 13 item di indice, 6 relazioni interne (tutte verso sottoclausole
di questo stesso capitolo). Questo modulo e' puro dato: non importa nulla, non
legge file e NON tocca app/seed.py - la numerazione degli id e' risolta per
riferimento dalla sessione principale tramite app/seed_data/lib.py, e le
relazioni verso altri capitoli di questa fonte o verso altre fonti le costruisce
sempre la sessione principale (fase 6, ADR-0009).

Provenienza del testo: app/.source_cache/etsi_319_132/cap03.txt (532 righe),
porzione dello split deterministico descritto in
app/.source_cache/etsi_319_132/manifest.json (capitolo "cap03", titolo "4 -
General Syntax") del testo ufficiale completo in
app/.source_cache/etsi_319_132/raw.txt, raw_body.txt e raw.pdf. Da
app/.source_cache/etsi_319_132/provenance.json: URL ufficiale
https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf,
versione ETSI "01.03.01_60" (EN 319 132-1 V1.3.1, 2024-07), data_fetch
2026-09-29T12:56:34Z, sha256 del PDF grezzo
83fc87ee09de90274131a1f60cb73edb742cebc7cd8961342586ed06133664c5, formato "PDF
ETSI deliver (pdftotext -layout)" (tutti i valori dal provenance.json della
fonte).

## Perimetro

Clausola 4 completa, dal titolo "4 General Syntax" fino alla clausola 4.5
inclusa: il capitolo successivo dello split (cap04) apre la clausola 5
(Qualifying properties semantics and syntax). Nessun requisito numerato con id
proprio in questa clausola: ETSI EN 319 132-1 numera per clausola/sottoclausta
e non usa identificatori del tipo GEN-/REQ-/OVR- (verificato sull'intero
capitolo: zero occorrenze). La granularita' e' quindi la sottoclausta, come per
ETSI EN 319 122-1 cap02 e per le altre fonti ETSI gia' censite.

## Granularita' voce per voce (ADR-0007)

13 item di indice = le 13 sottoclausole numerate con contenuto proprio (4.1,
4.2, 4.3.1-4.3.7, 4.4.1-4.4.3, 4.5), una riga ciascuna, nessun accorpamento e
nessun item coperto da piu' righe.

Intestazioni di raggruppamento -> nessun nodo e nessun item, perche' non hanno
periodo proprio e sono seguite immediatamente dalla prima sottoclausta:
"4 General Syntax" (titolo del capitolo) e "4.3 The QualifyingProperties
container" (seguito da 4.3.1) e "4.4 Incorporating qualifying properties into
XAdES signatures" (seguito da 4.4.1). Stesso criterio delle intestazioni di
raggruppamento delle altre fonti ETSI censite (ETSI EN 319 122-1 clausola 6 e
4.7/4.8, ETSI TS 119 612 clausola 6).

Etichette interne non numerate ("Semantics" e "Syntax", ripetute in 4.3.1-4.3.7
e 4.4.3) -> nessun nodo e nessun item: non sono unita' numerate dal documento,
sono partizioni redazionali della sottoclausta che le contiene, e restano
verbatim dentro il nodo della sottoclausta. Lo stesso vale per i due elenchi
puntati di 4.2 (URI dei namespace), per l'elenco puntato dei due mezzi di
incorporazione e per le quattro restrizioni di 4.4.1 (nessuna di queste voci
porta un id proprio ne' e' usata come indice altrove nel documento: a
differenza del precedente di EN 319 122-1 clausola 6.3, dove le lettere a)-t)
sono requisiti numerati e richiamati singolarmente dalla Tabella 1, qui
l'unita' numerata e citabile resta la sottoclausta). La Tabella 1 di 4.2
(namespace con prefissi costanti) resta contenuto del nodo 4.2: due righe di
dati, senza id proprio.

Le singole qualifying property (SigningTime, SigningCertificate, ...) NON sono
unita' di questo capitolo: sono definite dalla clausola 5 (capitoli cap04-cap06
dello split), e i loro eventuali nodi per attributo/property appartengono a quei
moduli. Qui il perimetro e' la sintassi generale e i contenitori.

## Obbligo o Principio, riga per riga

Tutte e 13 le sottoclausole sono Obblighi "tecnico/sicurezza": ciascuna contiene
almeno una prescrizione di conformazione del formato XAdES ("shall") rivolta
alla costruzione della firma, non una mera dichiarazione. In dettaglio:

- 4.1 -> Obbligo "tecnico/sicurezza": le firme XAdES "shall build on XMLDSIG"
  incorporando signed e unsigned qualifying properties, che "shall be instances
  of XML types" definite con XML Schema [2] e [3]. Il terzo periodo ("The
  present clause defines the namespaces ... also defines the types ...") e' un
  periodo di raccordo, non un'unita' numerata a se': resta nel nodo, come i
  periodi di raccordo delle altre fonti ETSI censite.
- 4.2 -> Obbligo "tecnico/sicurezza". La sottoclausa enumera i quattro namespace
  URI usati, i due file XML Schema, la Tabella 1 dei prefissi costanti ds/xsd e
  riporta integralmente i due xsd:schema, ma la sua parte deontica e' la regola finale:
  "In case of discrepancies ... the XML Schema files shall take precedence".
  Precedente seguito: ETSI TS 119 612 Annex B.0 (General requirements), dove
  l'elenco dei namespace convive con prescrizioni normative nello stesso nodo
  Obbligo "tecnico/sicurezza".
  DUBBIO DI CLASSIFICAZIONE APERTO per la revisione umana: la sottoclausa e' per
  la maggior parte un inventario di namespace e prefissi (contenuto
  definitorio); se la revisione preferisse la convenzione per cui una clausola
  prevalentemente definitoria e' un Principio "definitorio", andrebbe
  riclassificata (nodi e testo restano identici). Non e' stato spezzato in due
  righe (una definitoria, una prescrittiva) perche' l'indice e' la singola
  sottoclausta numerata.
- 4.3.1 -> Obbligo "tecnico/sicurezza": ruolo di contenitore dell'elemento
  QualifyingProperties, divisione fra properties firmate e non firmate, schema
  con Target obbligatorio e Id opzionale, vincoli sul valore di Target e divieto
  di QualifyingProperties vuote.
- 4.3.2 -> Obbligo "tecnico/sicurezza": contenuto di SignedProperties, legame
  con ds:Reference/ds:SignedInfo, schema con il solo attributo Id, rinvii alle
  sottoclausole 4.3.4 e 4.3.5 e divieto di SignedProperties vuote.
- 4.3.3 -> Obbligo "tecnico/sicurezza": contenuto di UnsignedProperties, schema
  con il solo attributo Id, rinvii a 4.3.6 e 4.3.7, divieto di
  UnsignedProperties vuote.
- 4.3.4 -> Obbligo "tecnico/sicurezza": contenuto di SignedSignatureProperties,
  schema con gli otto elementi ammessi e xsd:any su namespace altrui, divieto di
  usare xsd:any per elementi non specificati dal presente multi-part
  deliverable, divieto di incorporare le qualifying property obsolete
  (SigningCertificate, SignatureProductionPlace, SignerRole) e divieto di
  SignedSignatureProperties vuote.
- 4.3.5 -> Obbligo "tecnico/sicurezza": contenuto di SignedDataObjectProperties,
  schema con i quattro elementi ammessi e xsd:any, stessi limiti su xsd:any e
  divieto di elemento vuoto.
- 4.3.6 -> Obbligo "tecnico/sicurezza": contenuto di UnsignedSignatureProperties,
  schema xs:choice con i tredici elementi ammessi e xsd:any, esclusione della
  copertura da parte della firma XML, divieto di usare xsd:any per elementi non
  specificati, obsoletizzazione di CompleteCertificateRefs,
  AttributeCertificateRefs, SigAndRefsTimeStamp, RefsOnlyTimeStamp e
  ArchiveTimeStamp della v1.3.2 con divieto di incorporarli, divieto di
  elemento vuoto.
- 4.3.7 -> Obbligo "tecnico/sicurezza": contenuto di
  UnsignedDataObjectProperties, schema con UnsignedDataObjectProperty di tipo
  AnyType, esclusione della copertura dalla firma XML, divieto di elemento
  vuoto; la NOTE (il documento non specifica alcuna unsigned qualifying
  property di questo tipo, l'elemento esiste per completezza e AnyType e'
  definito in 5.1.1) resta nel nodo.
- 4.4.1 -> Obbligo "tecnico/sicurezza": uso di ds:Object, i due mezzi di
  incorporazione (diretta e indiretta) e le quattro restrizioni su ds:Object,
  QualifyingProperties e QualifyingPropertiesReference.
- 4.4.2 -> Obbligo "tecnico/sicurezza": collocazione delle signed qualifying
  properties, ds:Reference aggiunto per proteggerle, uso di SignedProperties
  come input del digest e valore del Type attribute
  (http://uri.etsi.org/01903#SignedProperties).
- 4.4.3 -> Obbligo "tecnico/sicurezza": semantica di
  QualifyingPropertiesReference, schema con URI obbligatorio e Id opzionale,
  contenuto del URI attribute (frammento XPointer bare-name verso un elemento
  QualifyingProperties esterno).
- 4.5 -> Obbligo "tecnico/sicurezza": obbligo di includere l'identificatore
  dell'algoritmo di canonicalizzazione sia generando nuove firme XAdES sia
  aumentando una firma legacy con una qualifying property che ne ammette uno
  opzionale.

Nessun `condizione_applicabilita`: la clausola 4 non marca alcuna sottoclausa
come condizionale; le due situazioni di 4.5 (generazione di nuove firme /
augmentation di firme legacy) sono i due casi della medesima prescrizione
(unita' di indice indivisibile), non una condizione di applicabilita' esterna
al testo.

Modulazione deontica: i "may"/"needs not" presenti in 4.3.1 ("its not-fragment
part needs not be empty"), 4.3.2/4.3.3 ("may contain qualifying properties
that qualify ...") e 4.4.1 ("may occur", "may contain") restano dentro righe
Obbligo: nessuna delle categorie di `tipo_principio` descrive una facolta'
operativa rivolta alla costruzione della firma, e la forza modale resta nel
`testo` e nel `testo_integrale` (stesso precedente di ETSI EN 319 122-1 cap02
e cap04).

Soggetti: NESSUNA riga di questo capitolo valorizza `soggetti`. Il soggetto
grammaticale delle prescrizioni della clausola 4 sono gli elementi XML e i tipi
di schema ("XAdES signatures shall ...", "The QualifyingProperties element
shall ...", "the XML Schema files shall take precedence"): il testo non nomina
mai una categoria di soggetto del censimento (ne' "the signer", ne' "the
generator", ne' un prestatore di servizi). In 4.5 compaiono attivita' ("When
generating new XAdES signatures", "When augmenting a legacy XAdES signature")
il cui attore implicito esiste, ma la categoria va dichiarata solo se il testo
la nomina: nessuna inferenza. Nota: la NOTE di 4.4.1 nomina "the entity that
has to store them" per dichiarare fuori perimetro i meccanismi di
conservazione delle QualifyingProperties distribuite - non e' un soggetto
obbligato da questa clausola.
`oggetti_giuridici`: non valorizzati. Il testo nomina firme XAdES, elementi XML
e tipi XML Schema, mai un oggetto della tassonomia eIDAS (firma elettronica
avanzata/qualificata, documento elettronico, ...), che sarebbe un'inferenza.

## Fedelta' dell'estrazione (ADR-0010)

- Righe spezzate dalla conversione PDF: ricucite con uno spazio, mai con
  trattino (il testo ufficiale non spezza parole a fine riga con trattino in
  questo capitolo). Verificato meccanicamente in fase di scrittura: dopo la
  normalizzazione degli spazi, il `testo_integrale` di ogni riga e' una
  sottostringa contigua del testo ufficiale (a meno del ": " aggiunto dopo
  l'etichetta numerata della clausola e del separatore " | " con cui sono
  ricostruite le righe della Tabella 1 - vedi sotto).
- Blocchi XML: riportati come il testo li presenta, con la loro indentazione e
  le loro interruzioni di riga reali (non ricuciti: sono codice di schema, non
  prosa). In 4.3.4 il testo ufficiale riporta due volte la dichiarazione
  dell'elemento SignedSignatureProperties - una volta spezzata su due righe e
  una volta su una riga sola: entrambe sono riportate, nessuna correzione.
- Tabella 1: `pdftotext -layout` allinea le due colonne; la tabella e' resa una
  riga per record con le colonne separate da " | " (stessa convenzione di ETSI
  EN 319 122-1 cap04), intestazione di colonna una sola volta. Nessuna cella
  riscritta o abbreviata.
- NOTE: le NOTE 1-4 di 4.2, la NOTE di 4.3.7 e le NOTE 1-2 di 4.5 sono
  riportate per intero nel nodo della sottoclausa che le contiene. Tutte hanno
  contenuto interpretativo (differenze fra le versioni dei file XML Schema,
  perche' l'elemento UnsignedDataObjectProperties esiste, effetti della
  canonicalizzazione sull'ereditarieta' degli attributi di namespace) e nessuna
  e' stata scartata come mero rimando bibliografico.
- Paratesto escluso: piede di pagina "ETSI", testatina "ETSI EN 319 132-1
  V1.3.1 (2024-07)" con il numero di pagina 13-20, righe vuote di impaginazione
  e le righe bianche lasciate dal salto di pagina in mezzo a un blocco XML o a
  un elenco puntato (il contenuto prosegue nella pagina successiva ed e' stato
  ricucito).
- Nessun marcatore di elisione nel testo ufficiale di questo capitolo
  (verificato: zero occorrenze di "..." o "…" in cap03.txt), quindi nessuna
  convenzione di esenzione e' in gioco. Nessun front matter, Contents, Foreword,
  References (clausola 2), History o elenco bibliografico ricade nel file
  assegnato: cap03.txt comincia con il titolo "4 General Syntax" e termina con
  la NOTE 2 della clausola 4.5.
- Normalizzazione di resa: i marcatori di elenco puntato sono U+2022 ("•") nel
  testo ufficiale e sono riportati tali.

## Rinvii demandati alla fase 6 (nessuna relazione creata verso di essi)

Rinvii interni a questa fonte ma fuori da questo modulo (il bersaglio e' un
nodo di un altro capitolo dello split, o una partizione di clausola; ADR-0012):

- 4.3.1 -> clausola C.1 (Annex C, informativo): "whose location is detailed in
  clause C.1" (due volte). NOTA: Annex C non e' tra i capitoli del manifest di
  questa fonte (cap08 = Annex A, cap09 = Annex D, cap10 = Annex E): non esiste
  un nodo a cui collegare il rinvio.
- 4.3.2 -> clausola C.1 ("whose location is detailed in clause C.1").
- 4.3.3 -> clausola C.1 (idem).
- 4.3.4 -> clausola C.1 (idem) e clausole 5.2.2, 5.2.5, 5.2.6: "Qualifying
  properties SigningCertificate, SignatureProductionPlace, and SignerRole are
  obsoleted by SigningCertificateV2, SignatureProductionPlaceV2, and
  SignerRoleV2 respectively (see clauses 5.2.2, 5.2.5 and 5.2.6, respectively)".
- 4.3.5 -> clausola C.1 (idem).
- 4.3.6 -> clausole A.1.1, A.1.3, A.1.5.1 e A.1.5.2 (Annex A, capitolo cap08) e
  clausola 5.5.2 (capitolo cap06): "respectively (see clauses A.1.1, A.1.3,
  A.1.5.1 and A.1.5.2 respectively)" e "see clause 5.5.2".
- 4.3.7 -> clausola C.1 (idem) e clausola 5.1.1 (capitolo cap04): NOTE, "The
  type AnyType is defined in clause 5.1.1".
- 4.4.3 -> clausola C.1 (idem).

Rinvii ad altre fonti o a standard esterni non censiti nel grafo (annotati, non
trasformati in archi):

- 4.1 -> W3C Recommendation "XML Signature Syntax and Processing. Version 1.1"
  [1] (XMLDSIG), W3C "Extensible Markup Language (XML) 1.0" [5], W3C "XML
  Schema Part 1: Structures" [2] e Part 2: Datatypes [3].
- 4.2 -> ETSI EN 319 132-1 (V1.2.1) [i.20] (NOTE 2 e NOTE 4), ETSI TS 101 903
  V1.3.2 [i.21] e V1.4.1 [i.22] (NOTE 3).
- 4.3.1 -> IETF RFC 3986 [12] (URI) per il valore dell'attributo Target.
- 4.4.1 -> W3C XMLDSIG [1] (elemento ds:Object).
- 4.4.2 -> valore URI http://uri.etsi.org/01903#SignedProperties del Type
  attribute.
- 4.5 -> NOTE 1: W3C "Canonical XML Version 1.0" [9] e "Canonical XML Version
  1.1" [11] (URI http://www.w3.org/2006/12/xml-c14n11); NOTE 2: "Canonical XML
  Version 1.0" [9] e "Exclusive XML Canonicalization Version 1.0" [10] (URI
  http://www.w3.org/2001/10/xml-exc-c14n#).

## Relazioni dichiarate (6, tutte interne a questo modulo)

Sei relazioni, tutte "richiama" (rinvio o citazione esplicita di un nodo verso
un altro, CONTEXT.md), tutte con evidenza `textual` perche' la citazione e'
letterale nel `testo_integrale` del nodo citante e punta a una sottoclausola
numerata dichiarata in questo stesso file; `confidence` None perche' nessuna
estrazione LLM ha prodotto uno score (ADR-0005):

- 4.3.2 -> "clausola 4.3.4 (The SignedSignatureProperties container)": "The
  SignedSignatureProperties element shall contain ... This element is specified
  in clause 4.3.4."
- 4.3.2 -> "clausola 4.3.5 (The SignedDataObjectProperties container)": "... This
  element is specified in clause 4.3.5."
- 4.3.3 -> "clausola 4.3.6 (The UnsignedSignatureProperties container)": "... This
  element is specified in clause 4.3.6."
- 4.3.3 -> "clausola 4.3.7 (The UnsignedDataObjectProperties container)": "...
  This element is specified in clause 4.3.7."
- 4.4.1 -> "clausola 4.4.3 (The QualifyingPropertiesReference element)": "...
  (see clause 4.4.3)".
- 4.4.1 -> "clausola 4.4.2 (Signing properties)": "... (see clause 4.4.2 for
  information how to sign qualifying properties); and".

Nessuna relazione verso altri capitoli di questa fonte ne' verso altre fonti:
le partizioni e i collegamenti cross-fonte sono costruiti dalla sessione
principale in fase 6 (ADR-0012, ADR-0009). Nessuna relazione inversa
("e' richiamato da") e' dichiarata: la relazione inversa si ottiene per
traversal a ritroso, non e' duplicata come arco separato.

## Copertura

13 item di indice, 13 righe (13 Obblighi + 0 Principi), 6 relazioni interne.
MAPPATURA_LOCALE mappa ogni item su se stesso: nessun accorpamento, nessun item
coperto da piu' righe.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "clausola 4.1 (General requirements)",
        "testo": (
            "Le firme XAdES devono fondarsi su XMLDSIG come specificato in [1], incorporando qualifying "
            "properties XML [5] firmate e non firmate; tali qualifying properties devono essere istanze "
            "di tipi XML nella sintassi e nelle strutture di XML Schema specificate in [2] e [3]. La "
            "clausola annuncia anche cosa definisce il resto della clausola 4: i namespace usati nelle "
            "definizioni di schema, i tipi per i contenitori delle qualifying properties e i meccanismi "
            "per incorporarle nella firma XAdES."
        ),
        "testo_integrale": (
            """4.1 General requirements:
XAdES signatures shall build on XMLDSIG as specified in [1] by incorporation of XML [5] signed and unsigned
qualifying properties. These qualifying properties shall be instances of XML types using the XML Schema syntax and
structures specified in [2] and [3].

The present clause defines the namespaces used in the aforementioned XML schema definitions.

The present clause also defines the types for the containers of the qualifying properties, and specifies the mechanisms
for incorporating them into the XAdES signature."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.2 (XML Namespaces)",
        "testo": (
            "Il documento usa i namespace URI http://uri.etsi.org/01903/v1.3.2#, http://uri.etsi.org/01903/v1.4.1#, "
            "http://www.w3.org/2000/09/xmldsig# e http://www.w3.org/2001/XMLSchema, definiti dai due file XML Schema "
            "\"1913201-XAdES01903v132.xsd\" e \"1913201-XAdES01903v141.xsd\" i cui xsd:schema sono riportati "
            "integralmente con le NOTE 1-4; la Tabella 1 fissa i due prefissi costanti ds e xsd, mentre il documento "
            "usa altri prefissi negli estratti di schema. In caso di discrepanza fra gli estratti di schema riportati "
            "nel documento e i file XML Schema, i file XML Schema devono prevalere."
        ),
        "testo_integrale": (
            """4.2 XML Namespaces:
The present document uses the URI namespaces listed below:

• http://uri.etsi.org/01903/v1.3.2#

• http://uri.etsi.org/01903/v1.4.1#

• http://www.w3.org/2000/09/xmldsig#

• http://www.w3.org/2001/XMLSchema

ETSI defines two XML Schema files for the present document, namely: "1913201-XAdES01903v132.xsd", and
"1913201-XAdES01903v141.xsd". See annex C for details on their locations.

Table 1 shows two prefixes that refer to the same namespaces in the two XML Schema files. These prefixes are used
throughout the present document to refer to specific elements in the XAdES signature.

Table 1: Namespaces with constant prefixes
XML Namespace URI | Prefix
http://www.w3.org/2000/09/xmldsig# | ds
http://www.w3.org/2001/XMLSchema | xsd

NOTE 1: The present document uses other prefixes in the excerpts of the XML Schema files for referencing XML
elements. The preambles of the corresponding XML Schema files clearly identify the namespace
corresponding to each prefix.

Below follows a copy of the xsd:schema element of the XML Schema file "1913201-XAdES01903v132.xsd",
whose location is detailed in clause C.1, and that defines the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#.
<xsd:schema targetNamespace="http://uri.etsi.org/01903/v1.3.2#"
xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns="http://uri.etsi.org/01903/v1.3.2#"
xmlns:xsd="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">

NOTE 2: The content of the XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in
clause C.1 is identical to the content of the XML Schema file defining types and elements in the
namespace whose URI is http://uri.etsi.org/01903/v1.3.2#, in ETSI EN 319 132-1 (V1.2.1) [i.20].

Below follows a copy of the xsd:schema element of the XML Schema file "1913201-XAdES01903v141.xsd",
whose location is detailed in clause C.2, and that defines the namespace whose URI is http://uri.etsi.org/01903/v1.4.1#.
<xsd:schema targetNamespace="http://uri.etsi.org/01903/v1.4.1#"
xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns="http://uri.etsi.org/01903/v1.4.1#"
xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xades="http://uri.etsi.org/01903/v1.3.2#"
elementFormDefault="qualified">

NOTE 3: The http://uri.etsi.org/01903/v1.3.2# URI was defined by ETSI TS 101 903 (V1.3.2) [i.21]. Most of the
XML elements and types used by XAdES signatures were defined in this namespace. The present
document adds new types and elements to this namespace. Additionally, ETSI TS 101 903 (V1.4.1) [i.22]
defined http://uri.etsi.org/01903/v1.4.1# URI, where new types and elements were defined. The present
document also adds new types and elements to this namespace.

NOTE 4: The content of the XML Schema file "1913201-XAdES01903v141.xsd", whose location is detailed in
clause C.2 is different from the content of the XML Schema file defining types and elements in the
namespace whose URI is http://uri.etsi.org/01903/v1.4.1#, in ETSI EN 319 132-1 (V1.2.1) [i.20].

In case of discrepancies between the xml schema excerpts provided in the present document and the XML Schema files,
the XML Schema files shall take precedence."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.1 (Semantics and syntax)",
        "testo": (
            "L'elemento QualifyingProperties deve fare da contenitore di tutte le qualifying information aggiunte a "
            "una firma XML, e le qualifying properties devono essere divise fra quelle crittograficamente vincolate "
            "(firmate) dalla firma XML e quelle che non lo sono. Lo schema riportato fissa l'attributo Target "
            "obbligatorio, riferito all'attributo Id del ds:Signature corrispondente e valorizzato con un URI [12] "
            "con frammento XPointer bare-name (la parte non-fragment deve essere vuota se la firma XAdES incapsula "
            "l'elemento), e l'attributo Id opzionale che serve a referenziare il contenitore. Nessuna firma XAdES "
            "deve incorporare elementi QualifyingProperties vuoti."
        ),
        "testo_integrale": (
            """4.3.1 Semantics and syntax
Semantics

The QualifyingProperties element shall act as a container element for all the qualifying information that is
added to an XML signature.

The qualifying properties shall be split into qualifying properties that are cryptographically bound to (i.e. signed by) the
XML signature, and qualifying properties that are not cryptographically bound to (i.e. not signed by) the XML
signature.

Syntax

The QualifyingProperties element shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd",
whose location is detailed in clause C.1, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="QualifyingProperties" type="QualifyingPropertiesType"/>

<xsd:complexType name="QualifyingPropertiesType">
    <xsd:sequence>
        <xsd:element ref="SignedProperties" minOccurs="0"/>
        <xsd:element ref="UnsignedProperties" minOccurs="0"/>
    </xsd:sequence>
    <xsd:attribute name="Target" type="xsd:anyURI" use="required"/>
    <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

The Target attribute shall refer to the Id attribute of the corresponding ds:Signature.

The value of Target attribute shall be a URI [12] with a bare-name XPointer fragment. If the XAdES signature
envelops the QualifyingProperties element, its not-fragment part shall be empty. Otherwise, its not-fragment
part needs not be empty.

The Id attribute shall be used to reference the QualifyingProperties container.

A XAdES signature shall not incorporate empty QualifyingProperties elements."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.2 (The SignedProperties container)",
        "testo": (
            "L'elemento SignedProperties deve contenere le qualifying properties firmate collettivamente dalla firma "
            "XML: uno dei figli ds:Reference dell'elemento ds:SignedInfo deve essere generato in modo che "
            "SignedProperties contribuisca al calcolo del valore della firma digitale. L'elemento puo' contenere "
            "qualifying properties che qualificano la firma XML stessa, il firmatario o alcuni dei signed data "
            "object; lo schema riportato fissa il solo attributo Id, che serve a referenziare l'elemento. "
            "SignedSignatureProperties e' specificato nella clausola 4.3.4 e SignedDataObjectProperties nella "
            "clausola 4.3.5; nessuna firma XAdES deve incorporare un elemento SignedProperties vuoto."
        ),
        "testo_integrale": (
            """4.3.2 The SignedProperties container
Semantics

The SignedProperties element shall contain qualifying properties that are collectively signed by the XML
signature. In consequence one of the ds:Reference children of ds:SignedInfo element in the XAdES signature
shall be generated in a way that ensures that the SignedProperties element contributes to the digital signature
value computation.

The SignedProperties element may contain qualifying properties that qualify the XML signature itself, the
signer, or some of the signed data objects.

Syntax

The SignedProperties element shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose
location is detailed in clause C.1, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="SignedProperties" type="SignedPropertiesType" />

<xsd:complexType name="SignedPropertiesType">
    <xsd:sequence>
        <xsd:element ref="SignedSignatureProperties" minOccurs="0"/>
        <xsd:element ref="SignedDataObjectProperties" minOccurs="0"/>
    </xsd:sequence>
    <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

The SignedSignatureProperties element shall contain qualifying properties that qualify the XML signature
itself or the signer. This element is specified in clause 4.3.4.

The SignedDataObjectProperties element shall contain qualifying properties that qualify some of the signed
data objects. This element is specified in clause 4.3.5.

The Id attribute shall be used to reference the SignedProperties element.

A XAdES signature shall not incorporate empty SignedProperties element."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.3 (The UnsignedProperties container)",
        "testo": (
            "L'elemento UnsignedProperties deve contenere le qualifying properties non firmate dalla firma XML e "
            "puo' contenere qualifying properties che qualificano la firma XML stessa, il firmatario o alcuni dei "
            "signed data object; lo schema riportato fissa il solo attributo Id, che serve a referenziare "
            "l'elemento. UnsignedSignatureProperties e' specificato nella clausola 4.3.6 e "
            "UnsignedDataObjectProperties nella clausola 4.3.7; nessuna firma XAdES deve incorporare elementi "
            "UnsignedProperties vuoti."
        ),
        "testo_integrale": (
            """4.3.3 The UnsignedProperties container
Semantics

The UnsignedProperties element shall contain qualifying properties that are not signed by the XML signature.

The UnsignedProperties element may contain qualifying properties that qualify the XML signature itself, the
signer, or some of the signed data objects.

Syntax

The UnsignedProperties element shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd",
whose location is detailed in clause C.1, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="UnsignedProperties" type="UnsignedPropertiesType" />

<xsd:complexType name="UnsignedPropertiesType">
    <xsd:sequence>
        <xsd:element ref="UnsignedSignatureProperties" minOccurs="0"/>
        <xsd:element ref="UnsignedDataObjectProperties" minOccurs="0"/>
    </xsd:sequence>
    <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

The UnsignedSignatureProperties element shall contain qualifying properties that qualify the XML signature
itself or the signer. This element is specified in clause 4.3.6.

The UnsignedDataObjectProperties element shall contain qualifying properties that qualify some of the
signed data objects. This element is specified in clause 4.3.7.

The Id attribute shall be used to reference the UnsignedProperties element.

A XAdES signature shall not incorporate empty UnsignedProperties elements."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.4 (The SignedSignatureProperties container)",
        "testo": (
            "L'elemento SignedSignatureProperties deve contenere le qualifying properties firmate che qualificano la "
            "firma XML; lo schema riportato ammette i figli SigningTime, SigningCertificate, SigningCertificateV2, "
            "SignaturePolicyIdentifier, SignatureProductionPlace, SignatureProductionPlaceV2, SignerRole, "
            "SignerRoleV2 e un xsd:any su namespace diversi da http://uri.etsi.org/01903/v1.3.2# (futuro uso per "
            "qualifying property aggiuntive, che devono essere definite in un namespace diverso), oltre all'attributo "
            "Id opzionale. L'elemento non deve incorporare elementi come istanza di xsd:any non specificati in alcuna "
            "versione di questo multi-part deliverable; le qualifying property SigningCertificate, "
            "SignatureProductionPlace e SignerRole sono obsoletizzate rispettivamente da SigningCertificateV2, "
            "SignatureProductionPlaceV2 e SignerRoleV2 (clausole 5.2.2, 5.2.5 e 5.2.6) e non devono essere "
            "incorporate nella firma; nessuna firma XAdES deve incorporare un elemento SignedSignatureProperties "
            "vuoto."
        ),
        "testo_integrale": (
            """4.3.4 The SignedSignatureProperties container
Semantics

This element shall contain signed qualifying properties that qualify the XML signature.

Syntax

The SignedSignatureProperties element shall be defined as in XML Schema file "1913201-
XAdES01903v132.xsd", whose location is detailed in clause C.1, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#"

The preamble of the XML Schema file also includes the following namespace declaration:
  xmlns:xadestsv132="http://uri.etsi.org/01903/v1.3.2#",
which assigns the prefix "xadestsv132" to the namespace whose URI is shown in the declaration.
-->

<xsd:element name="SignedSignatureProperties"
  type="SignedSignaturePropertiesType" />

<xsd:element name="SignedSignatureProperties" type="SignedSignaturePropertiesType"/>

<xsd:complexType name="SignedSignaturePropertiesType">
    <xsd:sequence>
        <xsd:element ref="SigningTime" minOccurs="0"/>
        <xsd:element ref="SigningCertificate" minOccurs="0"/>
        <xsd:element ref="SigningCertificateV2" minOccurs="0"/>
        <xsd:element ref="SignaturePolicyIdentifier" minOccurs="0"/>
        <xsd:element ref="SignatureProductionPlace" minOccurs="0"/>
        <xsd:element ref="SignatureProductionPlaceV2" minOccurs="0"/>
        <xsd:element ref="SignerRole" minOccurs="0"/>
        <xsd:element ref="SignerRoleV2" minOccurs="0"/>
        <xsd:any namespace="##other" minOccurs="0" maxOccurs="unbounded"/>
    </xsd:sequence>
    <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

Future versions of this multi-part deliverable may use the any element for allowing the incorporation of additional
signed signature qualifying properties. These additional signed signature qualifying properties shall be defined in a
namespace whose URI is different from http://uri.etsi.org/01903/v1.3.2#.

The SignedSignatureProperties element shall not incorporate any elements as an instantiation of xsd:any
that are not specified within any version of this multi-part deliverable.

The Id attribute shall be used to reference the SignedSignatureProperties element.

Qualifying properties SigningCertificate, SignatureProductionPlace, and SignerRole are
obsoleted by SigningCertificateV2, SignatureProductionPlaceV2, and SignerRoleV2 respectively
(see clauses 5.2.2, 5.2.5 and 5.2.6, respectively).

The aforementioned obsoleted qualifying properties shall not be incorporated into the signature.

A XAdES signature shall not incorporate an empty SignedSignatureProperties element."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.5 (The SignedDataObjectProperties container)",
        "testo": (
            "L'elemento SignedDataObjectProperties deve contenere le qualifying properties firmate che qualificano "
            "alcuni dei signed data object; lo schema riportato ammette i figli DataObjectFormat, "
            "CommitmentTypeIndication, AllDataObjectsTimeStamp, IndividualDataObjectsTimeStamp (ciascuno "
            "minOccurs 0 e ripetibile) e un xsd:any su namespace diversi da http://uri.etsi.org/01903/v1.3.2# "
            "(futuro uso per qualifying property aggiuntive, che devono essere definite in un namespace diverso), "
            "oltre all'attributo Id opzionale. L'elemento non deve incorporare elementi come istanza di xsd:any non "
            "specificati in alcuna versione di questo multi-part deliverable; nessuna firma XAdES deve incorporare un "
            "elemento SignedDataObjectProperties vuoto."
        ),
        "testo_integrale": (
            """4.3.5 The SignedDataObjectProperties container
Semantics

This element shall contain signed qualifying properties that qualify some of the signed data objects.

Syntax

The SignedDataObjectProperties element shall be defined as in XML Schema file "1913201-
XAdES01903v132.xsd", whose location is detailed in clause C.1, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:complexType name="SignedDataObjectPropertiesType">
    <xsd:sequence>
        <xsd:element ref="DataObjectFormat" minOccurs="0" maxOccurs="unbounded"/>
        <xsd:element ref="CommitmentTypeIndication" minOccurs="0" maxOccurs="unbounded"/>
        <xsd:element ref="AllDataObjectsTimeStamp" minOccurs="0" maxOccurs="unbounded"/>
        <xsd:element ref="IndividualDataObjectsTimeStamp" minOccurs="0" maxOccurs="unbounded"/>
        <xsd:any namespace="##other" minOccurs="0" maxOccurs="unbounded"/>
    </xsd:sequence>
    <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

Future versions of this multi-part deliverable may use the any element for allowing the incorporation of additional
signed data objects qualifying properties. These additional signed data objects qualifying properties shall be defined in a
namespace whose URI is different from http://uri.etsi.org/01903/v1.3.2#.

The SignedDataObjectProperties element shall not incorporate any element as an instantiation of xsd:any
that are not specified within any version of this multi-part deliverable.

The Id attribute shall be used to reference the SignedDataObjectProperties element.

A XAdES signature shall not incorporate an empty SignedDataObjectProperties element."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.6 (The UnsignedSignatureProperties container)",
        "testo": (
            "L'elemento UnsignedSignatureProperties deve contenere le qualifying properties non firmate che "
            "qualificano la firma XML, e la firma XML non deve coprirne il contenuto; lo schema riportato ammette, "
            "come xsd:choice ripetibile illimitatamente, CounterSignature, SignatureTimeStamp, "
            "CompleteCertificateRefs, CompleteRevocationRefs, AttributeCertificateRefs, AttributeRevocationRefs, "
            "SigAndRefsTimeStamp, RefsOnlyTimeStamp, CertificateValues, RevocationValues, AttrAuthoritiesCertValues, "
            "AttributeRevocationValues, ArchiveTimeStamp e un xsd:any su namespace diversi, oltre all'attributo Id "
            "opzionale. L'elemento non deve incorporare elementi come istanza di xsd:any non specificati in alcuna "
            "versione di questo multi-part deliverable; CompleteCertificateRefs, AttributeCertificateRefs, "
            "SigAndRefsTimeStamp, RefsOnlyTimeStamp (clausole A.1.1, A.1.3, A.1.5.1 e A.1.5.2) e ArchiveTimeStamp "
            "(clausola 5.5.2) definiti nel namespace http://uri.etsi.org/01903/v1.3.2# sono obsoletizzati dalle "
            "versioni V2 definite nel namespace http://uri.etsi.org/01903/v1.4.1# e non devono essere incorporati "
            "nella firma XAdES; nessuna firma XAdES deve incorporare un elemento UnsignedSignatureProperties vuoto."
        ),
        "testo_integrale": (
            """4.3.6 The UnsignedSignatureProperties container
Semantics

This element shall contain unsigned qualifying properties that qualify the XML.

The XML signature shall not cover the content of this element.

Syntax

The UnsignedSignatureProperties element shall be defined as in XML Schema file "1913201-
XAdES01903v132.xsd", whose location is detailed in clause C.1, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="UnsignedSignatureProperties"
  type="UnsignedSignaturePropertiesType"/>

<xsd:complexType name="UnsignedSignaturePropertiesType">
    <xsd:choice maxOccurs="unbounded">
        <xsd:element ref="CounterSignature" />
        <xsd:element ref="SignatureTimeStamp" />
        <xsd:element ref="CompleteCertificateRefs"/>
        <xsd:element ref="CompleteRevocationRefs"/>
        <xsd:element ref="AttributeCertificateRefs"/>
        <xsd:element ref="AttributeRevocationRefs" />
        <xsd:element ref="SigAndRefsTimeStamp" />
        <xsd:element ref="RefsOnlyTimeStamp" />
        <xsd:element ref="CertificateValues" />
        <xsd:element ref="RevocationValues"/>
        <xsd:element ref="AttrAuthoritiesCertValues" />
        <xsd:element ref="AttributeRevocationValues"/>
        <xsd:element ref="ArchiveTimeStamp" />
        <xsd:any namespace="##other"/>
    </xsd:choice>
    <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

Future versions of this multi-part deliverable may use the any element for allowing the incorporation of additional
signed data objects qualifying properties. These additional signed data objects qualifying properties shall be defined in a
namespace whose URI is different from http://uri.etsi.org/01903/v1.3.2#.

The UnsignedSignatureProperties element shall not incorporate any element as an instantiation of xsd:any
that are not specified within any version of this multi-part deliverable.

The Id attribute shall be used to reference the UnsignedSignatureProperties element.

Qualifying properties CompleteCertificateRefs, AttributeCertificateRefs,
SigAndRefsTimeStamp, and RefsOnlyTimeStamp, defined in the namespace whose URI value
http://uri.etsi.org/01903/v1.3.2# (XML Schema file "1913201-XAdES01903v132.xsd") are obsoleted by
CompleteCertificateRefsV2, AttributeCertificateRefsV2, SigAndRefsTimeStampV2,
RefsOnlyTimeStampV2 (defined in the namespace whose URI value is http://uri.etsi.org/01903/v1.4.1#)
respectively (see clauses A.1.1, A.1.3, A.1.5.1 and A.1.5.2 respectively).

Additionally the qualifying property ArchiveTimeStamp defined in the namespace whose URI value
http://uri.etsi.org/01903/v1.3.2# (XML Schema file "1913201-XAdES01903v132.xsd") is obsoleted by
ArchiveTimeStamp defined in the namespace whose URI value is http://uri.etsi.org/01903/v1.4.1# (XML Schema
file "1913201-XAdES01903v141.xsd", see clause 5.5.2).

The aforementioned obsoleted qualifying properties shall not be incorporated into the XAdES signature.

A XAdES signature shall not incorporate an empty UnsignedSignatureProperties element."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.7 (The UnsignedDataObjectProperties container)",
        "testo": (
            "L'elemento UnsignedDataObjectProperties deve contenere le qualifying properties che qualificano alcuni "
            "dei signed data object, e la firma XML non deve coprirne il contenuto; lo schema riportato ammette uno o "
            "piu' elementi UnsignedDataObjectProperty di tipo AnyType, oltre all'attributo Id opzionale che serve a "
            "referenziare l'elemento. Nessuna firma XAdES deve incorporare un elemento UnsignedDataObjectProperties "
            "vuoto. La NOTE dichiara che il documento non specifica l'uso di alcuna unsigned qualifying property di "
            "questo tipo, che l'elemento e' definito per completezza e per future esigenze di inclusione, che lo "
            "schema lascia aperta la definizione del contenuto del tipo e che AnyType e' definito nella clausola 5.1.1."
        ),
        "testo_integrale": (
            """4.3.7 The UnsignedDataObjectProperties container
Semantics

This element shall contain qualifying properties that qualify some of the signed data objects.

The XML signature shall not cover the content of this element.

Syntax

The UnsignedDataObjectProperties element shall be defined as in XML Schema file "1913201-
XAdES01903v132.xsd", whose location is detailed in clause C.1, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="UnsignedDataObjectProperties" type="UnsignedDataObjectPropertiesType"/>

<xsd:complexType name="UnsignedDataObjectPropertiesType">
    <xsd:sequence>
        <xsd:element name="UnsignedDataObjectProperty" type="AnyType" maxOccurs="unbounded"/>
    </xsd:sequence>
    <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

The Id attribute shall be used to reference the UnsignedDataObjectProperties element.

A XAdES signature shall not incorporate empty UnsignedDataObjectProperties element.

NOTE: The present document does not specify the usage of any unsigned qualifying property qualifying the
signed data objects. It, however, defines this element for the sake of completeness and to cope with
potential future needs for inclusion of such kind of qualifying properties. The schema definition leaves
open the definition of the contents of this type. The type AnyType is defined in clause 5.1.1."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.4.1 (General requirements)",
        "testo": (
            "L'elemento ausiliario ds:Object di XMLDSIG [1] deve essere usato per incorporare le qualifying "
            "properties nella firma XAdES, con due mezzi: incorporazione diretta (l'elemento QualifyingProperties e' "
            "figlio del ds:Object) e incorporazione indiretta (uno o piu' elementi QualifyingPropertiesReference "
            "figli del ds:Object, ciascuno con le informazioni su un elemento QualifyingProperties che non deve "
            "essere discendente dell'elemento radice ds:Signature della firma XAdES - clausola 4.4.3). Le quattro "
            "restrizioni sull'uso di ds:Object, QualifyingProperties e QualifyingPropertiesReference impongono che "
            "tutte le istanze incorporate direttamente e tutte le QualifyingPropertiesReference siano in un solo "
            "ds:Object, che in esso ci sia al massimo una istanza di QualifyingProperties, che tutte le signed "
            "qualifying properties siano in un solo elemento QualifyingProperties (figlio di quel ds:Object o "
            "referenziato da una QualifyingPropertiesReference, clausola 4.4.2) e che le istanze di "
            "QualifyingPropertiesReference possano essere zero o piu'. Le firme XAdES possono contenere ds:Object "
            "diversi da quelli che contengono QualifyingProperties o QualifyingPropertiesReference, e nessuna "
            "restrizione si applica alla loro posizione relativa."
        ),
        "testo_integrale": (
            """4.4.1 General requirements:
The ds:Object auxiliary element from XMLDSIG [1] shall be used for incorporating the qualifying properties into
the XAdES signature.

The present document specifies two different means for incorporating qualifying properties:

• direct incorporation means that a QualifyingProperties element shall be a child of the ds:Object;

• indirect incorporation means that one or more QualifyingPropertiesReference elements shall
  appear as children of the ds:Object. Each one shall contain information about one
  QualifyingProperties element that shall not be a descendant element of the ds:Signature XAdES
  signature root element (see clause 4.4.3).

The following restrictions apply for using ds:Object, QualifyingProperties and
QualifyingPropertiesReference:

• all instances of QualifyingProperties directly incorporated into the XAdES signature, and all the
  instances of QualifyingPropertiesReference, shall occur within a single ds:Object element;

• at most one instance of the QualifyingProperties element may occur within this ds:Object
  element;

• all signed qualifying properties shall occur within a single QualifyingProperties element. This
  element shall either be a child of this ds:Object element (direct incorporation), or referenced by a
  QualifyingPropertiesReference element (see clause 4.4.2 for information how to sign qualifying
  properties); and

• zero or more instances of the QualifyingPropertiesReference element may occur within this
  ds:Object element.

XAdES signatures may contain ds:Object elements different from the ds:Object elements containing the
QualifyingProperties or QualifyingPropertiesReference elements.

No restrictions apply to the relative position of the ds:Object containing the QualifyingProperties or
QualifyingPropertiesReference with respect to other ds:Object elements present within
ds:Signature.

NOTE: It is out of the scope of the present document to specify the mechanisms required to guarantee the correct
storage of the distributed QualifyingProperties elements (i.e. that the qualifying properties are
stored by the entity that has to store them and that they are not undetectably modified)."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.4.2 (Signing properties)",
        "testo": (
            "Tutte le signed qualifying properties devono essere figlie di SignedProperties, figlio a sua volta "
            "dell'elemento QualifyingProperties. Per proteggerle con la firma, un elemento ds:Reference deve essere "
            "aggiunto alla firma XML, composto in modo da usare l'elemento SignedProperties come input per il "
            "calcolo del proprio digest, e deve includere l'attributo Type con valore "
            "http://uri.etsi.org/01903#SignedProperties (valore che indica che i dati usati per il digest sono un "
            "elemento SignedProperties e aiuta a individuare le signed qualifying properties di una firma XAdES "
            "conforme al documento)."
        ),
        "testo_integrale": (
            """4.4.2 Signing properties:
All the signed qualifying properties shall be children of the SignedProperties child of the
QualifyingProperties element.

In order to protect the qualifying properties with the signature, a ds:Reference element shall be added to the XML
signature.

This ds:Reference element shall be composed in such a way that it uses the SignedProperties element
mentioned above as the input for computing its corresponding digest.

This ds:Reference element shall include the Type attribute with its value set to:

• http://uri.etsi.org/01903#SignedProperties.

NOTE: This value indicates that the data used for digest computation is a SignedProperties element and
therefore helps to detect the signed qualifying properties of a XAdES signature conforming to the present
document."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.4.3 (The QualifyingPropertiesReference element)",
        "testo": (
            "L'elemento QualifyingPropertiesReference deve contenere le informazioni su un elemento "
            "QualifyingProperties che non e' discendente dell'elemento radice ds:Signature della firma XAdES (per "
            "esempio perche' memorizzato in un altro documento XML); lo schema riportato fissa l'attributo URI "
            "obbligatorio e l'attributo Id opzionale. Il valore di URI deve contenere un frammento XPointer "
            "bare-name e referenziare un elemento QualifyingProperties esterno: la sua parte non-fragment deve "
            "identificare il documento che lo racchiude e il frammento XPointer bare-name l'elemento stesso. "
            "L'attributo Id serve a referenziare l'elemento QualifyingPropertiesReference."
        ),
        "testo_integrale": (
            """4.4.3 The QualifyingPropertiesReference element
Semantics

This element shall contain information about one QualifyingProperties element that is not descendant of the
ds:Signature XAdES signature root element (if for instance, it is stored in another XML document).

Syntax

The QualifyingPropertiesReference element shall be defined as in XML Schema file "1913201-
XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="QualifyingPropertiesReference"
  type="QualifyingPropertiesReferenceType"/>

<xsd:complexType name="QualifyingPropertiesReferenceType">
  <xsd:attribute name="URI" type="xsd:anyURI" use="required"/>
  <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

The URI attribute shall contain a bare-name XPointer fragment and shall reference an external
QualifyingProperties element. Its not-fragment part shall identify the enclosing document and its bare-name
XPointer fragment shall identify the aforementioned element.

The Id attribute shall be used to reference the QualifyingPropertiesReference element."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.5 (Managing canonicalization of XML nodesets)",
        "testo": (
            "Diverse qualifying properties incorporate mezzi opzionali per identificare un algoritmo di "
            "canonicalizzazione con cui calcolare la forma canonica di un certo XML node set: quando si generano "
            "nuove firme XAdES, tutte le qualifying properties che offrono quel mezzo opzionale devono includere "
            "l'identificatore dell'algoritmo di canonicalizzazione, e altrettanto deve fare la qualifying property "
            "(la cui definizione XML Schema prevede un identificatore opzionale dell'algoritmo) generata e "
            "incorporata quando si aumenta una firma XAdES legacy. Le NOTE 1 e 2 illustrano perche' Canonical XML "
            "1.1 (http://www.w3.org/2006/12/xml-c14n11) gestisca correttamente l'ereditarieta' degli attributi del "
            "namespace XML e come la canonicalizzazione esclusiva "
            "(http://www.w3.org/2001/10/xml-exc-c14n#) escluda il contesto degli antenati."
        ),
        "testo_integrale": (
            """4.5 Managing canonicalization of XML nodesets:
A number of qualifying properties specified in the present document incorporate optional means for identifying a
canonicalization algorithm for computing the canonical form of a certain XML node set.

When generating new XAdES signatures, all the XAdES qualifying properties that provide optional means for
indicating the canonicalization algorithm shall include the canonicalization algorithm identifier.

When augmenting a legacy XAdES signature by the generation and incorporation of a certain XAdES qualifying
property specified in the present document, and whose XML Schema definition includes an optional identifier of a
canonicalization algorithm, this qualifying property shall include the canonicalization algorithm identifier.

NOTE 1: Canonical XML 1.0 [9] does not properly process the inheritance of attributes in the XML namespace
(xml:id and xml:base) when canonicalizing document sub-trees. Canonical XML version 1.1 [11]
(whose version omitting comments is identified by the URI http://www.w3.org/2006/12/xml-c14n11),
specifies a variant of the former canonicalization algorithm that properly addresses these issues.

NOTE 2: Canonical XML 1.0 [9] when applied to a XML sub-tree, includes the sub-tree's ancestor context
including all of the namespace declarations and attributes in the "xml:" namespace. The exclusive XML
Canonicalization algorithm [10] (whose version omitting comments is identified by the URI
http://www.w3.org/2001/10/xml-exc-c14n#) completely excludes this ancestor context from the
canonicalized sub-tree."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI: list[dict] = []

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 4.1 (General requirements)",
    "clausola 4.2 (XML Namespaces)",
    "clausola 4.3.1 (Semantics and syntax)",
    "clausola 4.3.2 (The SignedProperties container)",
    "clausola 4.3.3 (The UnsignedProperties container)",
    "clausola 4.3.4 (The SignedSignatureProperties container)",
    "clausola 4.3.5 (The SignedDataObjectProperties container)",
    "clausola 4.3.6 (The UnsignedSignatureProperties container)",
    "clausola 4.3.7 (The UnsignedDataObjectProperties container)",
    "clausola 4.4.1 (General requirements)",
    "clausola 4.4.2 (Signing properties)",
    "clausola 4.4.3 (The QualifyingPropertiesReference element)",
    "clausola 4.5 (Managing canonicalization of XML nodesets)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Rinvii interni alla clausola 4, tutti letterali nei testo_integrale dei nodi
# citanti e tutti verso bersagli dichiarati in questo stesso modulo. Nessuna
# relazione verso altri capitoli di questa fonte ne' verso altre fonti: quelle
# le costruisce la sessione principale in fase 6 (ADR-0009, ADR-0012).
RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "clausola 4.3.2 (The SignedProperties container)"),
        "nodo_a": ("obbligo", None, "clausola 4.3.4 (The SignedSignatureProperties container)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 4.3.2 (The SignedProperties container)"),
        "nodo_a": ("obbligo", None, "clausola 4.3.5 (The SignedDataObjectProperties container)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 4.3.3 (The UnsignedProperties container)"),
        "nodo_a": ("obbligo", None, "clausola 4.3.6 (The UnsignedSignatureProperties container)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 4.3.3 (The UnsignedProperties container)"),
        "nodo_a": ("obbligo", None, "clausola 4.3.7 (The UnsignedDataObjectProperties container)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 4.4.1 (General requirements)"),
        "nodo_a": ("obbligo", None, "clausola 4.4.3 (The QualifyingPropertiesReference element)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 4.4.1 (General requirements)"),
        "nodo_a": ("obbligo", None, "clausola 4.4.2 (Signing properties)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
