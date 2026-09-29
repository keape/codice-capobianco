"""ETSI EN 319 122-1 V1.3.1 (2023-06) - Electronic Signatures and Trust
Infrastructures (ESI); CAdES digital signatures; Part 1: Building blocks and
CAdES baseline signatures. Blocco B (famiglia AdES del lotto 2). Capitolo 7
dello split: Annex E (informative) "Example Structured Contents and MIME"
(E.1.1-E.1.4, E.2.1-E.2.3, E.3) e Annex F (informative) "Change History".
Conteggio di questo capitolo: 0 Obblighi, 9 Principi, 9 item di indice, 2
relazioni. Questo modulo e' puro dato: non importa nulla e non legge file; la
numerazione degli id e' risolta per riferimento dalla sessione principale in
app/seed.py (che questo modulo NON tocca), tramite app/seed_data/lib.py.

Provenienza del testo
---------------------
- testo ufficiale: ETSI EN 319 122-1 V1.3.1 (2023-06), deliver "01.03.01_60",
  formato "PDF ETSI deliver (pdftotext -layout)".
- file di capitolo: app/.source_cache/etsi_319_122/cap07.txt (346 righe),
  porzione dello split deterministico di app/.source_cache/etsi_319_122/raw.txt.
- metadati da app/.source_cache/etsi_319_122/provenance.json: url
  https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf,
  versione "01.03.01_60", data_fetch 2026-09-29T12:56:34Z, sha256_raw_pdf
  e99e76e519d9bd8e1410775bccedb1a588021e5e7c705c9fcc1f91c6a6227c21.
- perimetro: dal titolo "Annex E (informative):" (riga 1 del file) fino
  all'ultima riga della tabella dell'Annex F (righe 292-321), cioe' tutti gli
  annessi contenuti nel file assegnato. La sezione "History"/"Document
  history" che segue (righe 331-341 del file di capitolo; righe 3871-3881 di
  raw.txt) resta fuori: non e' un annesso, vedi "Esclusioni".

Convenzione dei riferimenti
---------------------------
Il testo ufficiale usa "Annex": i `riferimento` mantengono la forma ufficiale
del testo per le sottoclausole dell'Annex E ("Annex E, clause E.1.1 (MIME
Structure)") e la forma "Annex F (Change History)" per l'Annex F, che non ha
numerazione interna ed e' quindi esso stesso l'unita' indivisa (stessa forma
gia' usata per gli annessi non suddivisi di ETSI TS 119 612: "Annex F (TL
manual/auto field usage)", "Annex J (Migration of EU MS trusted lists in the
context of Regulation (EU) No 910/2014)").
Le clausole del corpo del documento portano invece "clausola x.y" nei moduli
fratelli di questa Fonte (cap01-cap04): qui non ve ne sono.

## Granularita' (ADR-0007, nessun discrimine di rilevanza)

Uno standard che numera i propri requisiti con id dedicati (REQ-x.y-nn,
GEN-x.y-z) viene censito all'id di requisito; l'Annex E di ETSI EN 319 122-1
non numera i requisiti (non contiene alcun "shall": l'unico verbo deontico di
tutto il capitolo e' un "may" in E.1.1 e uno "should" in E.3, entrambi
descrittivi), quindi l'unita' di indice e' la clausola/sottoclausta numerata
del documento. Bilancio: 9 item di indice -> 9 righe, 1:1.

- E.1.1, E.1.2, E.1.3, E.1.4 -> 4 item.
- E.2.1, E.2.2, E.2.3 -> 3 item.
- E.3 -> 1 item.
- Annex F (Change History) -> 1 item.

Intestazioni senza testo proprio -> nessun nodo e nessun item di indice
(stesso criterio gia' applicato alle intestazioni di raggruppamento della
clausola 6 di questa Fonte, cap04, e delle altre fonti ETSI censite):
- "Annex E (informative): Example Structured Contents and MIME": intestazione
  dell'annesso, seguita immediatamente da "E.1 Use of MIME to Encode Data";
- "E.1 Use of MIME to Encode Data": sottoclavola di raggruppamento, seguita
  immediatamente da "E.1.1 MIME Structure", senza una riga di testo proprio
  da assorbire;
- "E.2 S/MIME": idem, seguita immediatamente da "E.2.1 Using S/MIME";
- "Annex F (informative): Change History": l'intestazione e il titolo
  dell'annesso appartengono alla riga dell'Annex F, non a un item a se'.

L'Annex F e' censito come 1 Principio per istruzione esplicita di questo
batch ("il file contiene piu' annessi, censisci tutti e distingui i
riferimenti"): l'annesso e' un'unita' di indice reale del documento (compare
nel Contents a pag. 62 con la propria numerazione) e ADR-0007 vieta ogni
discrimine di rilevanza in estrazione. DUBBIO DI CLASSIFICAZIONE APERTO per
la revisione umana: altri batch hanno dato istruzione opposta per il blocco
"Change history"/"History" (ETSI EN 319 431-1, EN 319 431-2, TS 119 461, TS
119 432, EN 319 102-1), escludendolo come paratesto editoriale; se la
revisione preferisse quella convenzione, la riga dell'Annex F va rimossa
insieme al suo item di indice (resterebbero 8 item e 8 righe).

## Obbligo o Principio, riga per riga

L'intero capitolo e' un annesso *informative* di esempi e spiegazioni: nessuna
delle 9 righe impone un comportamento a un soggetto identificabile, quindi
RIGHE_OBBLIGHI e' vuoto e tutte e 9 le righe sono Principi.

- E.1.1 (MIME Structure) -> Principio "altro". Spiega cos'e' MIME, perche'
  le sue funzionalita' sono utili alla codifica di documenti elettronici e
  dati multimediali (elenco di 4 funzionalita'), e come e' fatto un oggetto
  MIME singolo: l'enunciato "The signed content may be structured using
  Multipurpose Internet Mail Extensions (MIME)" usa il verbo modale "may" ed
  e' quindi una facolta' descrittiva, non una prescrizione rivolta a un
  destinatario. Non "scopo/ambito di applicazione": il perimetro del
  documento sta nella clausola 1 (cap01) e nella clausola 4.1, mentre qui si
  descrive una tecnologia di codifica, non l'ambito del documento.
  Non "definitorio": i termini del documento sono censiti nella clausola 3.1
  (cap01), e questo annesso non definisce termini usati altrove.
- E.1.2 (Header Information) -> Principio "altro". Descrizione di cosa
  contiene un'intestazione MIME (versione, tipo di contenuto, codifica del
  contenuto, altre informazioni) piu' due esempi di intestazione (oggetto di
  testo e file binario PDF). Il rinvio interno "(see below about encoding
  supported by MIME)" punta a E.1.3 ed e' l'unica relazione dichiarata di
  questa riga.
- E.1.3 (Content Encoding) -> Principio "altro". Descrizione dei meccanismi
  di codifica di MIME (testo trasparente a 7/8 bit, quoted-printable, binario
  a 8 bit o Base64) con la NOTE informativa sull'uso di Base64 su Internet.
- E.1.4 (Multi-Part Content) -> Principio "altro". Descrizione del contenuto
  multi-parte (tipo "multipart" e stringa di separazione, intestazione per il
  contenuto complessivo piu' intestazione di ogni parte, annidamento) con un
  esempio completo di messaggio multipart.
- E.2.1 (Using S/MIME) -> Principio "altro". Nome e uso di S/MIME (MIME che
  trasporta dati protetti CMS estesi), la figura E.1 e le due modalita' con
  cui S/MIME trasporta le firme digitali (application/pkcs7-mime oppure
  multipart/signed). Nessun obbligo: descrive alternative possibili, non
  impone quale usare.
- E.2.2 (Using application/pkcs7-mime) -> Principio "altro". Descrizione
  della prima modalita' ("can be included"), con la figura E.2 e un esempio
  di dati firmati cosi' codificati.
- E.2.3 (Using multipart/signed and application/pkcs7-signature) ->
  Principio "altro". Descrizione della seconda modalita' (dati non inclusi
  nel SignedData; la struttura CMS contiene solo la firma), con la figura
  E.3, un esempio completo e il vantaggio della modalita' (decodificabilita'
  da qualunque sistema compatibile MIME).
- E.3 (Use of MIME in the signature) -> Principio "altro". Descrizione dei
  due modi in cui CAdES puo' includere il tipo MIME dei dati firmati
  (elemento contentDescription dell'attributo content-hints, oppure attributo
  mime-type) e della loro utilita', piu' i due esempi numerati 1) e 2). Il
  "should" della riga ("how the driving application should decode or display
  the signed data") non e' un requisito rivolto a un soggetto: enuncia a cosa
  serve l'informazione per l'applicazione di guida.
- Annex F (Change History) -> Principio "altro". Tabella di cronologia
  redazionale (data, versione, change request attuate): nessun requisito,
  nessun principio giuridico, nessun soggetto.

`tipo_principio` "altro" per tutte e 9 le righe: nessuna delle quattro
categorie sostanziali (non discriminazione, equivalenza giuridica, valore
probatorio, presunzione legale) ha riscontro in un annesso informativo di
esempi tecnici, e le due categorie di cornice non si applicano (nessuna riga
delimita l'ambito del documento: sta nella clausola 1; nessuna riga definisce
termini del documento: stanno nella clausola 3.1, cap01). Stessa scelta gia'
fatta per le clausole descrittive degli annessi informativi di ETSI TS 119
432 cap07 (B.1, B.2, B.4, B.5 -> Principio "altro").

`oggetti_giuridici`: non valorizzato in nessuna riga. Il testo nomina "signed
content", "electronic documents", "digital signatures" e oggetti MIME/CMS, ma
mai un oggetto giuridico della tassonomia del censimento in quanto tale (e'
il contenuto tecnico trasportato o codificato, non l'oggetto giuridico della
firma); stessa scelta conservativa del modulo cap04 di questa Fonte, che non
valorizza `oggetti_giuridici` per la clausola 6 (l'attributo ammette solo i
valori enumerati dal censimento e va dichiarato solo se il testo lo nomina
davvero). Analogamente `soggetti`, che non si applica ai Principi.

## Fedelta' dell'estrazione

- Prosa: le righe spezzate da `pdftotext -layout` sono ricucite in paragrafi
  (una riga per paragrafo, una riga per item di elenco, prefisso "• " per gli
  elenchi puntati come nei moduli fratelli). Nessuna elisione, nessun
  riassunto, nessuna riformulazione: il contenuto verbale e' integrale.
- Figure E.1, E.2, E.3: in questo file la conversione PDF ha estratto il
  contenuto delle figure come testo (casella disegnata con caratteri ASCII),
  non come immagine; conseguenza: e' riprodotto verbatim in `testo_integrale`
  insieme alla didascalia letterale ("Figure E.1: Illustration of relation of
  using S/MIME", "Figure E.2: Signing Using application/pkcs7-mime", "Figure
  E.3: Signing Using application/pkcs7-signature"), senza ritocchi. La
  casella della figura E.2 e' visibilmente scomposta dalla conversione
  (colonne disallineate): e' riportata cosi' come il file la presenta, non
  corretta a mano (stesso principio con cui cap04 riporta i refusi della
  Tabella 1 di questa Fonte). Regola gia' in uso nelle fonti ETSI censite: la
  didascalia della figura e' sempre parte del testo della clausola; il
  contenuto grafico e' riprodotto solo quando la conversione lo estrae come
  testo (ETSI EN 319 431-1 cap02 documenta il caso opposto: figura non
  estraibile -> sola didascalia).
- Esempi di messaggi (E.1.2, E.1.4, E.2.2, E.2.3, E.3): riprodotti riga per
  riga con l'indentazione del file, inclusi gli header MIME, i boundary, il
  testo del corpo del messaggio multipart di esempio e i blocchi Base64
  (verbatim, anche se abbreviati dal documento stesso: nessun marcatore di
  elisione nel file di capitolo).
- Tabella di Annex F: `pdftotext -layout` spezza ogni record su piu' righe e
  disallinea le colonne. Ricostruzione: una riga per record, celle separate
  da " | ", con la data riportata prima della versione nell'ordine delle
  colonne del testo ufficiale ("Date | Version | Information about changes");
  nessuna cella riscritta o abbreviata, le liste di change request della
  colonna "Information about changes" riportate per intero (compresa la
  continuazione "clarification on order of signed attributes due to comments
  from the plugtest" spezzata su due righe dal PDF).
- Paratesto escluso dalla copia: piede di pagina "ETSI", testatina "ETSI EN
  319 122-1 V1.3.1 (2023-06)", numeri di pagina 58-63, righe vuote di
  impaginazione.

## Esclusioni

- Front matter, Contents, Foreword e clausola 2 (References): fuori dal file
  assegnato, gia' esclusi dallo split deterministico (il file comincia con
  "Annex E (informative):").
- Sezione finale "History"/"Document history" (righe 331-341 del file di
  capitolo, righe 3871-3881 di raw.txt): non e' un annesso (non compare nel
  Contents come Annex, e' la tabella di cronologia delle edizioni del
  deliverable) e non porta alcuna prescrizione: esclusa dal censimento come
  in tutte le fonti ETSI gia' importate (ETSI EN 319 431-1/431-2, TS 119 461,
  TS 119 432, EN 319 401, EN 319 102-1, TS 119 612).
- Nessuna tabella di soli riferimenti bibliografici nel perimetro.

## Rinvii demandati alla fase 6 (nessuna relazione creata qui)

- Rinvii ad altre parti del presente documento (altri capitoli di questa
  Fonte, gia' coperti da altri moduli dello split):
  - E.3 -> attributo content-hints (elemento contentDescription) e attributo
    mime-type, definiti nella clausola 5 (cap03);
  - E.1.1 -> la clausola 3.3 (cap01) definisce l'abbreviazione MIME;
  - E.1.2, E.1.4 e gli esempi di E.2.2/E.2.3 usano tipi MIME e strutture CMS
    (SignedData, Content-Type) la cui specifica vive nelle clausole 4
    (cap02) e 5 (cap03);
  - E.2.1 e i rinvii interni "figure E.1/E.2/E.3" puntano a figure contenute
    nella stessa riga che le cita (nessun arco).
- Rinvii ad altre fonti (collegamento cross-fonte, ADR-0009): IETF RFC 2045
  [2] (E.1.1) e IETF RFC 3851 [i.14] citato in E.2.1 ("see IETF RFC 3851
  [i.14]"), E.2.2 ("See IETF RFC 3851 [i.14], clause 3.4.2") ed E.2.3 ("See
  IETF RFC 3851 [i.14], clause 3.4.3"); Regolamento (UE) n. 910/2014 e le
  altre fonti non sono citati in questo capitolo.
- Nodi di partizione (ADR-0012): i riferimenti "E.1.1", "E.2.3" ecc. sono
  gia' unita' indivise (le sottoclausole non hanno commi/lettere interne), e
  l'Annex F condivide la partizione dell'annesso; le partizioni sono generate
  automaticamente da `neo4j_common.partizioni_di`, non dichiarate qui.

## Relazioni dichiarate (2, entrambe interne a questo modulo)

- E.1.2 -> E.1.3, "richiama", evidence_type "textual": il testo di E.1.2
  contiene letteralmente "(see below about encoding supported by MIME)" e la
  sola clausola sottostante che tratti di codifica e' E.1.3 (Content
  Encoding); il rinvio e' esplicito, il numero di clausola e' indicato in
  forma descrittiva invece che numerica. confidence None (nessuno score
  reale, ADR-0005).
- E.2.1 -> E.2.2, "richiama", evidence_type "textual": il riferimento
  letterale "see clause E.2.2" compare nell'elenco puntato di E.2.1.
  confidence None.
- Non dichiarata (deliberatamente): E.2.1 -> E.2.3. Il secondo item
  dell'elenco di E.2.1 descrive la modalita' multipart/signed di E.2.3 senza
  citarne il riferimento ("a "multipart/signed" object with the signed data
  and the signature encoded as separate MIME objects."): nessuna citazione
  letterale, quindi nessun arco.
- Nessuna relazione verso altri capitoli di questa Fonte ne' verso altre
  fonti: le costruisce la sessione principale in fase 6 (ADR-0009/ADR-0012).

## Copertura

9 item di indice, 9 righe: 0 obblighi + 9 principi.
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "Annex E, clause E.1.1 (MIME Structure)",
        "testo": (
            "Il contenuto firmato puo' essere strutturato usando Multipurpose Internet Mail "
            "Extensions (MIME) (IETF RFC 2045 [2]). MIME, nato per la posta elettronica su "
            "Internet, ha caratteristiche che lo rendono utile per dare una struttura comune "
            "alla codifica di documenti elettronici e di altri dati multimediali: segnalare il "
            "tipo di oggetto trasportato, associare un nome di file a un oggetto, combinare "
            "piu' oggetti indipendenti in un oggetto multi-parte, gestire dati testuali o "
            "binari ri-codificando il binario come testo quando necessario. Quando si codifica "
            "un singolo oggetto MIME consiste di informazioni di intestazione seguite dal "
            "contenuto codificato, e questa struttura puo' essere estesa per supportare "
            "contenuti multi-parte."
        ),
        "testo_integrale": (
            """E.1.1 MIME Structure: The signed content may be structured using Multipurpose Internet Mail Extensions (MIME) (IETF RFC 2045 [2]).

Whilst the MIME structure was initially developed for Internet email, it has a number of features that make it useful to provide a common structure for encoding a range of electronic documents and other multi-media data (e.g. photographs, video). These features include:

• providing a means of signalling the type of "object" being carried (e.g. text, image, ZIP file, application data);

• providing a means of associating a file name with an object;

• associating several independent objects (e.g. a document and image) to form a multi-part object;

• handling data encoded in text or binary and, if necessary, re-encoding the binary as text.

When encoding a single object, MIME consists of:

• header information;

• followed by encoded content.

This structure can be extended to support multi-part content."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex E, clause E.1.2 (Header Information)",
        "testo": (
            "Un'intestazione MIME comprende: le informazioni sulla versione MIME, le "
            "informazioni sul tipo di contenuto sufficienti per presentarlo a un utente o a un "
            "processo applicativo (tipo di media, tipo di applicazione destinataria, set di "
            "caratteri nel caso di testo), le informazioni sulla codifica del contenuto e "
            "altre informazioni sul contenuto come una descrizione o il nome di file "
            "associato. Il testo riporta due esempi di intestazione MIME, per un oggetto di "
            "testo e per un file binario contenente un documento PDF."
        ),
        "testo_integrale": (
            """E.1.2 Header Information: A MIME header includes:

• MIME Version information:
   e.g.: MIME-Version: 1.0

• Content type information, which includes information describing the content sufficient for it to be presented to a user or application process, as required. This includes information on the "media type" (e.g. text, image, audio) or whether the data is for passing to a particular type of application. In the case of text, the content type includes information on the character set used.
   e.g. Content-Type: text/plain; charset="us-ascii"

• Content-encoding information, which defines how the content is encoded (see below about encoding supported by MIME).

• Other information about the content, such as a description or an associated file name.

An example MIME header for text object is:
Mime-Version: 1.0
Content-Type: text/plain; charset=ISO-8859-1
Content-Transfer-Encoding: quoted-printable

An example MIME header for a binary file containing a PDF document is:
Content-Type: application/pdf
Content-Transfer-Encoding: base64
Content-Description: JCFV201.pdf
Content-Disposition: filename="JCFV201.pdf"
"""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex E, clause E.1.3 (Content Encoding)",
        "testo": (
            "MIME supporta diversi meccanismi per codificare dati testuali e binari. Il testo "
            "puo' essere trasportato trasparentemente come righe di caratteri ASCII a 7 o 8 bit, "
            "e MIME include anche una codifica \"quoted-printable\" che converte i caratteri "
            "diversi dall'ASCII di base in una sequenza ASCII; i dati binari possono essere "
            "trasportati trasparentemente come ottetti a 8 bit oppure convertiti in un insieme "
            "di caratteri di base con il sistema chiamato Base64. La NOTE precisa che, essendo "
            "alcune infrastrutture di posta in grado di gestire solo ASCII a 7 bit, su Internet "
            "la codifica Base64 e' quella di norma usata."
        ),
        "testo_integrale": (
            """E.1.3 Content Encoding: MIME supports a range of mechanisms for encoding both text and binary data.

Text data can be carried transparently as lines of text data encoded in 7- or 8-bit ASCII characters. MIME also includes a "quoted-printable" encoding that converts characters other than the basic ASCII into an ASCII sequence.

Binary can either be carried:

• transparently as 8-bit octets; or

• converted to a basic set of characters using a system called Base64.

NOTE: As there are some mail relays that can only handle 7-bit ASCII, Base64 encoding is usually used on the Internet."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex E, clause E.1.4 (Multi-Part Content)",
        "testo": (
            "Piu' oggetti (es. un testo e un allegato) possono essere associati insieme usando "
            "uno speciale tipo di contenuto \"multi-part\", indicato dal tipo \"multipart\" con "
            "l'indicazione della stringa da usare come separazione fra le parti; oltre a "
            "un'intestazione per il contenuto multipart complessivo, ogni parte porta una "
            "propria intestazione con il tipo di contenuto interno e la codifica. Il contenuto "
            "multipart puo' essere annidato (un insieme di oggetti associati puo' essere "
            "trattato come singolo allegato di un altro oggetto) e il Content-Type di ciascuna "
            "parte del messaggio MIME indica il tipo di contenuto; il testo riporta un esempio "
            "completo di contenuto multipart."
        ),
        "testo_integrale": (
            """E.1.4 Multi-Part Content: Several objects (e.g. text and a file attachment) can be associated together using a special "multi-part" content type. This is indicated by the content type "multipart" with an indication of the string to be used indicating a separation between each part.

In addition to a header for the overall multipart content, each part includes its own header information indicating the inner content type and encoding.

An example of a multipart content is:
Mime-Version: 1.0
Content-Type: multipart/mixed; boundary="----=_NextPart_000_01BC4599.98004A80"
Content-Transfer-Encoding: 7bit

------=_NextPart_000_01BC4599.98004A80
Content-Type: text/plain; charset=ISO-8859-1
Content-Transfer-Encoding: 7bit

Per your request, I've attached our proposal for the Java Card Version
2.0 API and the Java Card FAQ.

------=_NextPart_000_01BC4599.98004A80
Content-Type: application/pdf; name="JCFV201.pdf"
Content-Transfer-Encoding: base64
Content-Description: JCFV201.pdf
Content-Disposition: attachment; filename="JCFV201.pdf"

0M8R4KGxGuEAAAAAAAAAAAAAAAAAAAAAPgADAP7/CQAGAAAAAAAAAAAAAAACAAAAAgAAAAAAAAAA
EAAAtAAAAAEAAAD+////AAAAAAMAAAAGAAAA////////////////////////////////////////
AANhAAQAYg==

------=_NextPart_000_01BC4599.98004A80--

Multipart content can be nested. So a set of associated objects (e.g. HTML text and images) can be handled as a single attachment to another object (e.g. text).

The Content-Type from each part of the MIME message indicates the type of content."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex E, clause E.2.1 (Using S/MIME)",
        "testo": (
            "L'uso specifico di MIME per trasportare dati protetti CMS (esteso come definito "
            "nel presente documento) e' chiamato S/MIME (IETF RFC 3851 [i.14]). S/MIME "
            "trasporta le firme digitali in due modi: come oggetto \"application/pkcs7-mime\" "
            "con il CMS portato come allegato binario (PKCS7 e' il nome della versione iniziale "
            "di CMS, v. clausola E.2.2), oppure come oggetto \"multipart/signed\" con i dati "
            "firmati e la firma codificati come oggetti MIME separati; la figura E.1 illustra "
            "la relazione d'uso di S/MIME."
        ),
        "testo_integrale": (
            """E.2.1 Using S/MIME: The specific use of MIME to carry CMS (extended as defined in the present document) secured data is called S/MIME (see IETF RFC 3851 [i.14]).

           E-mail               S/MIME              CMS + ETSI               MIME                 Word File
                                                       ES
       From: Smith           Content-Type =                              Content-Type =         Dear Mr. Smith
       To: Jones             application/pkcs7-    SignedData            application/octet-     Received 100 tins.
       Subject: Signed       mime                      eContent          stream
       doc.                                                                                         Mr. Jones

                               Figure E.1: Illustration of relation of using S/MIME

S/MIME carries digital signatures as either:

• an "application/pkcs7-mime" object with the CMS carried as binary attachment (PKCS7 is the name of the early version of CMS), see clause E.2.2; or

• a "multipart/signed" object with the signed data and the signature encoded as separate MIME objects."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex E, clause E.2.2 (Using application/pkcs7-mime)",
        "testo": (
            "I dati da firmare possono essere inclusi nel SignedData all'interno di CAdES, che "
            "a sua volta puo' essere incluso in un unico oggetto S/MIME (IETF RFC 3851 [i.14], "
            "clausola 3.4.2, e figura E.2). L'approccio e' simile al trattamento dei dati "
            "firmati come qualunque altro allegato binario; il testo riporta un esempio di "
            "dati firmati codificati in questo modo."
        ),
        "testo_integrale": (
            """E.2.2 Using application/pkcs7-mime: The data to be signed can be included in the SignedData within CAdES, which itself can be included in a single S/MIME object. See IETF RFC 3851 [i.14], clause 3.4.2 and figure E.2.
                          +-------------++----------++-------------++------------+
                           |             ||          ||             ||            |
                           |   S/MIME    || CAdES    ||    MIME     || pdf file |
                           |             ||          ||             ||            |
                           |Content-Type=||SignedData||Content-Type=||Dear MrSmith|
                           |application/ || eContent ||application/ ||Received    |
                           |pkcs7-mime   ||          ||pdf          || 100 tins |
                           |             ||          ||             ||            |
                           |smime-type= ||      /|   ||       /|    || Mr.Jones |
                           |signed-data ||     / -----+      / ------+            |
                           |             ||    \\ -----+      \\ ------+            |
                           |             ||     \\|   ||       \\|    |+------------+
                           |             ||          |+-------------+
                           |             |+----------+
                            +-------------+

                              Figure E.2: Signing Using application/pkcs7-mime

This approach is similar to handling signed data as any other binary file attachment.

An example of signed data encoded using this approach is:
Content-Type: application/pkcs7-mime; smime-type=signed-data;
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename=smime.p7m

  567GhIGfHfYT6ghyHhHUujpfyF4f8HHGTrfvhJhjH776tbB9HG4VQbnj7
  77n8HHGT9HG4VQpfyF467GhIGfHfYT6rfvbnj756tbBghyHhHUujhJhjH
  HUujhJh4VQpfyF467GhIGfHfYGTrfvbnjT6jH7756tbB9H7n8HHGghyHh
  6YT64V0GhIGfHfQbnj75"""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex E, clause E.2.3 (Using multipart/signed and application/pkcs7-signature)",
        "testo": (
            "In questa seconda modalita' i dati firmati non sono inclusi nel SignedData e la "
            "struttura CMS contiene solo la firma (IETF RFC 3851 [i.14], clausola 3.4.3, e "
            "figura E.3): si usa un messaggio multipart/signed in cui la firma e' inclusa come "
            "application/pkcs7-signature. Il testo riporta un esempio completo di dati firmati "
            "cosi' codificati e rileva il vantaggio dell'approccio: i dati firmati possono "
            "essere decodificati da qualunque sistema compatibile con MIME anche se non "
            "riconosce le firme digitali codificate in CMS."
        ),
        "testo_integrale": (
            """E.2.3 Using multipart/signed and application/pkcs7-signature: The signed data is not included in the SignedData, and the CMS structure only includes the signature. See IETF RFC 3851 [i.14], clause 3.4.3 and figure E.3.

CMS also supports an alternative structure where the signature and data being protected are separate MIME objects carried within a single message. In this case, the data to be signed is not included in the SignedData, and the CMS structure only includes the signature. See IETF RFC 3851 [i.14], clause 3.4.3 and figure E.3 hereafter. In this case a multipart/signed message is used, where the signature is included as application/pkcs7-signature.

An example of signed data encoded using this approach is:
Content-Type: multipart/signed;
          protocol="application/pkcs7-signature";
          micalg=sha1; boundary=boundary42

        --boundary42
        Content-Type: text/plain

        This is a clear-signed message.

        --boundary42
        Content-Type: application/pkcs7-signature; name=smime.p7s
        Content-Transfer-Encoding: base64
        Content-Disposition: attachment; filename=smime.p7s

        ghyHhHUujhJhjH77n8HHGTrfvbnj756tbB9HG4VQpfyF467GhIGfHfYT6
        4VQpfyF467GhIGfHfYT6jH77n8HHGghyHhHUujhJh756tbB9HGTrfvbnj
        n8HHGTrfvhJhjH776tbB9HG4VQbnj7567GhIGfHfYT6ghyHhHUujpfyF4
        7GhIGfHfYT64VQbnj756

        --boundary42--

With this second approach, the signed data passes through the CMS process and is carried as part of a multiple-parts signed MIME structure, as illustrated in figure E.3. The CMS structure just holds the digital signature.
                       +---------------++----------++-------------++------------+
                        |               ||          ||             ||            |
                        |     MIME      || CAdES    ||    MIME     || pdf file |
                        |               ||          ||             ||            |
                        |Content-Type= ||SignedData||Content-Type=||Dear MrSmith|
                        |multipart/     ||          ||application/ ||Received    |
                        |signed         ||          ||pdf          || 100 tins |
                        |        /|     ||          ||             ||            |
                        |       / -------------------+        /|   || Mr.Jones |
                        |       \\ -------------------+       / -----+            |
                        |        \\|     ||          ||       \\ -----+            |
                        |Content-Type= ||           ||        \\|   |+------------+
                        |application/   ||          |+-------------+
                        |pdf            ||          |
                        |               |+----------+
                       +----------------+

                            Figure E.3: Signing Using application/pkcs7-signature

This second approach (multipart/signed) has the advantage that the signed data can be decoded by any MIME-compatible system even if it does not recognize CMS-encoded digital signatures."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex E, clause E.3 (Use of MIME in the signature)",
        "testo": (
            "CAdES consente due modi di includere il tipo MIME dei dati da firmare: "
            "nell'elemento contentDescription dell'attributo content-hints oppure nell'attributo "
            "mime-type. Il tipo MIME incluso informa l'applicazione di guida su come "
            "decodificare o presentare i dati firmati, e include inoltre il tipo MIME nella "
            "firma puo' aiutare a prevenire attacchi basati sul fatto che un file binario puo' "
            "cambiare significato o uso a seconda dell'applicazione che lo elabora. Quali "
            "informazioni dell'intestazione MIME siano incluse come tipo MIME nella firma "
            "dipende dalle esigenze dell'applicazione di guida: il testo riporta due esempi "
            "(solo l'applicazione o il Content-Type; oppure l'intera intestazione MIME)."
        ),
        "testo_integrale": (
            """E.3 Use of MIME in the signature: CAdES allows two ways to include the MIME type of the data to be signed, either in the contentDescription element of the content-hints attribute or in the mime-type attribute. The included MIME type allows to give information on how the driving application should decode or display the signed data. Thus these attributes allow to give the application useful information. In addition, including the MIME type into the signature can also help to prevent attacks based on the fact that a binary data file might change its meaning/use depending on the application used to process the data.

Which information of the MIME header is included as MIME type into the signature depends on the needs of the driving application. Two examples follow:

1) For most applications, it will be sufficient to know the application corresponding to signed data, thus they will put only the application or only the Content-Type as MIME-type into the signature, for example:

- application/pdf; or

- text/plain; charset="us-ascii".

2) In the case that the driving application is interested in all the details of the MIME header, it can put the whole header as MIME-type into the signature, like for example:
Content-Type: application/pdf
Content-Transfer-Encoding: base64
Content-Description: JCFV201.pdf
Content-Disposition: filename="JCFV201.pdf"
"""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex F (Change History)",
        "testo": (
            "Annesso informativo con la cronologia delle modifiche del documento: per ciascuna "
            "versione (1.1.2, 1.1.3, 1.1.4, 1.1.5, 1.1.6, 1.2.2, 1.2.3) la data e l'elenco "
            "delle change request ETSI attuate (es. specifica dell'hash della zero policy "
            "CAdES in 1.1.2, chiarimenti sul calcolo del campo unsignedAttrValuesHashIndex in "
            "1.1.3 e 1.1.4, inclusione del tipo MIME e ordine dell'hash index in 1.1.5). Non "
            "contiene requisiti ne' principi giuridici: e' cronologia redazionale, censita per "
            "copertura completa di tutti gli annessi del capitolo."
        ),
        "testo_integrale": (
            """Annex F (informative): Change History

Date | Version | Information about changes
October 2019 | 1.1.2 | Implementation of change request ESI(19)68_052r3: Specification of CAdES zero policy hash
October 2020 | 1.1.3 | Implementation of change request ESI(20)071_021r1: clarification on computation of unsignedAttrValuesHashIndex field of ats-hash-index-v3 attribute
November 2020 | 1.1.4 | Implementation of change request ESI(20)071_021r2: clarification on computation of unsignedAttrValuesHashIndex field of ats-hash-index-v3 attribute as accepted during ESi#71
May 2021 | 1.1.5 | Implementation of • CR#1 order of hash index: ESI(21)072014r1 • CR#2 inclusion of mime type: ESI(21)072015r1 • CR#3 clarification on usage of countersignatures: ESI(21)072016r1 • CR#4 OID for SAMLv2 to be included in signer-attributes-v2: ESI(21)072017r2 • CR#5 include signed attribute to protect algorithm used: ESI(21)072018r2 • CR#6 Reference to specific version of legacy documents: ESI(21)072051 • CR#7 remove informative ASN.1 annex: ESI(21)072060 • CR#8 less restrictions on CMS Version: ESI(21)073017
July 2021 | 1.1.6 | Adding of the change history
January 2023 | 1.2.2 | Implementation of • CR#2 reference new preservation document • CR#4 reference ETSI TS 119 122-3 in the foreword
February 2023 | 1.2.3 | Implementation of • CR#3 clarify when cms-algorithm-protection attribute is useful • CR#5 clarification on order of signed attributes due to comments from the plugtest"""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Annex E, clause E.1.1 (MIME Structure)",
    "Annex E, clause E.1.2 (Header Information)",
    "Annex E, clause E.1.3 (Content Encoding)",
    "Annex E, clause E.1.4 (Multi-Part Content)",
    "Annex E, clause E.2.1 (Using S/MIME)",
    "Annex E, clause E.2.2 (Using application/pkcs7-mime)",
    "Annex E, clause E.2.3 (Using multipart/signed and application/pkcs7-signature)",
    "Annex E, clause E.3 (Use of MIME in the signature)",
    "Annex F (Change History)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Due rinvii interni al capitolo, entrambi con citazione letterale presente nel
# testo citante (evidence_type "textual"): E.1.2 -> E.1.3 "(see below about
# encoding supported by MIME)" e E.2.1 -> E.2.2 "see clause E.2.2". I rinvii ad
# altri capitoli di questa Fonte (clausole 3.3, 4, 5) e ad altre fonti (IETF
# RFC 2045 [2], IETF RFC 3851 [i.14]) sono elencati nel docstring e restano
# alla fase 6 (ADR-0009/ADR-0012).
RELAZIONI = [
    {
        "nodo_da": ("principio", None, "Annex E, clause E.1.2 (Header Information)"),
        "nodo_a": ("principio", None, "Annex E, clause E.1.3 (Content Encoding)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Annex E, clause E.2.1 (Using S/MIME)"),
        "nodo_a": ("principio", None, "Annex E, clause E.2.2 (Using application/pkcs7-mime)"),
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
