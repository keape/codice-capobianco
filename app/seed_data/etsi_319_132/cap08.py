"""ETSI EN 319 132-1 V1.3.1 (2024-07) - Electronic Signatures and Trust
Infrastructures (ESI); XAdES digital signatures; Part 1: Building blocks and
XAdES baseline signatures. Blocco B (famiglia AdES del lotto 2). Capitolo 8
dello split: Annex A (normative) "Additional Qualifying Properties
Specification" (A.1 Qualifying properties for validation data, con
A.1.1-A.1.4, A.1.5/A.1.5.1/A.1.5.1.1-A.1.5.1.3 e A.1.5.2/A.1.5.2.1-A.1.5.2.3;
A.2 Deprecated qualifying properties, con A.2.1 e A.2.2), Annex B (normative)
"Alternative mechanisms for long term availability and integrity of validation
data" e Annex C (normative) "XML Schema files" (C.1 e C.2) - tutti e tre nel
file assegnato, non solo l'Annex A. Conteggio di questo capitolo: 29 Obblighi,
2 Principi, 31 item di indice, 33 relazioni interne (tutte fra righe di questo
modulo). Questo modulo e' puro dato: non importa nulla, non legge file e NON
tocca app/seed.py - la numerazione degli id e' risolta per riferimento dalla
sessione principale tramite app/seed_data/lib.py, e i collegamenti verso altri
capitoli di questa fonte o verso altre fonti li costruisce sempre la sessione
principale (fase 6, ADR-0009/ADR-0012).

Provenienza del testo
---------------------
- Testo ufficiale: ETSI EN 319 132-1 V1.3.1 (2024-07), "Electronic Signatures
  and Trust Infrastructures (ESI); XAdES digital signatures; Part 1: Building
  blocks and XAdES baseline signatures".
- File di capitolo: app/.source_cache/etsi_319_132/cap08.txt (674 righe),
  porzione dello split deterministico descritto in
  app/.source_cache/etsi_319_132/manifest.json (capitolo "cap08", titolo
  "Annex A (normative):"), ritagliata dal testo ufficiale completo in
  app/.source_cache/etsi_319_132/raw.txt (il PDF grezzo dello stesso
  documento e' raw.pdf; raw_body.txt ne e' la copia senza intestazioni
  ripetute). Il capitolo successivo dello split (cap09) apre l'Annex D
  (normative, "Deprecated qualifying properties").
- Da app/.source_cache/etsi_319_132/provenance.json: url ufficiale
  https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf,
  versione "01.03.01_60", data_fetch 2026-09-29T12:56:34Z, sha256_raw_pdf
  83fc87ee09de90274131a1f60cb73edb742cebc7cd8961342586ed06133664c5, formato
  "PDF ETSI deliver (pdftotext -layout)".
- NOTA DI PERIMETRO UTILE ALLA FASE 6: i moduli fratelli cap03, cap04 e cap07
  di questa fonte annotano che l'Annex C non sarebbe tra i capitoli dello
  split, e quindi che i loro rinvii a "clause C.1"/"clause C.2" resterebbero
  senza nodo di destinazione. Non e' cosi': il file assegnato a questo capitolo
  contiene l'Annex C per intero (C.1 e C.2), oltre all'Annex A e all'Annex B.
  I nodi C.1 e C.2 esistono quindi in questo modulo (2 Principi) e la fase 6
  puo' collegarvi i rinvii, compresi i sei rinvii "whose location is detailed
  in clause C.1/C.2" dichiarati qui come relazioni interne.

Perimetro
---------
Tre annessi normativi consecutivi, tutti coperti per intero: Annex A (dal
titolo "Annex A (normative): Additional Qualifying Properties Specification"
fino ad A.2.2 inclusa), Annex B (dal titolo all'ultima NOTE 2) e Annex C (dal
titolo a C.2 inclusa). Il file comincia con il titolo dell'Annex A e termina
con la NOTE di C.2: nessun front matter, Contents, Foreword, History, elenco
dei riferimenti bibliografici o appendice ricade nel perimetro. L'Annex D e'
il capitolo cap09 dello split, l'Annex E (informative, Change history) e' il
capitolo cap10.

Granularita' voce per voce (ADR-0007, decisione dell'utente: granularita' FINE)
-----------------------------------------------------------------------------
31 item di indice = 31 righe, una per unita' numerata con contenuto proprio
piu' una per ciascuna voce numerata che sia prescrizione autonoma:

- A.1.1 -> 1 riga per la sottoclausta (semantica di chiusura e sintassi, schema
  XML copiato in clausola incluso) + 1 riga per ciascuna delle 5 voci numerate
  1)-5) = 6 righe;
- A.1.2 -> idem, 1 + 5 = 6 righe;
- A.1.3 -> 1 + 3 = 4 righe; A.1.4 -> 1 + 3 = 4 righe;
- A.1.5.1.1, A.1.5.1.2, A.1.5.1.3, A.1.5.2.1, A.1.5.2.2, A.1.5.2.3 -> 1 riga
  ciascuna = 6 righe;
- A.2.1, A.2.2 -> 1 riga ciascuna = 2 righe;
- Annex B -> 1 riga (le 4 voci numerate restano nella riga della clausola);
- C.1, C.2 -> 1 riga ciascuna = 2 righe.

Criterio applicato per distinguere cio' che genera una riga propria da cio'
che resta nella riga dell'unita' contenitrice (lo stesso che i moduli fratelli
di questa fonte enunciano): una voce di elenco genera una riga propria quando
il testo la enuncia come prescrizione autonoma della property, con verbo
deontico proprio e oggetto proprio, tanto da restare comprensibile fuori dal
chapeau che la introduce. Vale per le voci 1)-5) di A.1.1 e A.1.2 e per le
voci 1)-3) di A.1.3 e A.1.4 ("Shall contain ...", "Shall not contain ...",
"May contain ..."): sono i requisiti della property stessa, e in A.1.1 voce 4)
e A.1.2 voce 4) il documento le richiama per numero al proprio interno
("references in 1) and 3)", "referenced in references from 1), 2) and 3)"),
quindi hanno un'identita' d'indice come le lettere a)-t) della clausola 6.3 di
ETSI EN 319 122-1.

Non generano riga propria, e restano nella riga della sottoclausta che le
contiene:
- le voci che completano il chapeau senza verbo proprio (Annex B, voci 1)-4):
  "then for this mechanism shall be specified: 1) The clear specification of
  the semantics and syntax of the property including its name, and
  namespace." - il precetto sta nel chapeau, le voci ne sono il contenuto);
- i passi di una procedura di calcolo descritti dal chapeau (le due voci di
  A.1.5.1.2, le due di A.1.5.1.3, i due elenchi di passi di A.1.5.2.3): nessuno
  e' richiamato altrove per numero ne' e' leggibile come prescrizione a se';
- gli elenchi di componenti marcatati (i due elenchi puntati di A.1.5.2.2 e
  A.1.5.2.3 e i cinque sottopunti delle voci 2) di A.1.5.1.2 e 3) di
  A.1.5.1.3): sono l'elenco degli elementi che la marca temporale copre, non
  requisiti;
- le partizioni redazionali non numerate "Semantics" e "Syntax" (etichette
  ripetute in A.1.1-A.1.4 e in A.1.5.x): restano nella riga della
  sottoclausta, come da convenzione gia' fissata in cap03 di questa fonte.

Intestazioni di puro raggruppamento, senza testo proprio, NON generano nodo
ne' item di indice (verificate sul testo: sono seguite immediatamente dalla
prima sottoclausta): "Annex A (normative): Additional Qualifying Properties
Specification", "A.1 Qualifying properties for validation data", "A.1.5
Time-stamps on references to validation data", "A.1.5.1 The
SigAndRefsTimeStampV2 qualifying property" (seguito da A.1.5.1.1), "A.1.5.2
The RefsOnlyTimeStampV2 qualifying property" (seguito da A.1.5.2.1), "A.2
Deprecated qualifying properties" (seguito da A.2.1), "Annex B (normative):
Alternative mechanisms for long term availability and integrity of validation
data" (il cui testo segue direttamente l'intestazione: la riga di Annex B
esiste e coincide con quella intestazione, vedi sotto) e "Annex C (normative):
XML Schema files" (seguito da C.1). Stesso criterio delle intestazioni di
raggruppamento delle altre fonti ETSI censite.

Chapeau di un elenco numerato: resta nella riga della sottoclausta anche
quando le voci sono righe proprie ("The CompleteCertificateRefsV2 qualifying
property:"). Il nodo di una sottoclausta non e' quindi un estratto contiguo
del testo ufficiale: raccoglie tutto il contenuto non numerato della
sottoclausta (etichette Semantics/Syntax comprese), nell'ordine in cui il
testo lo presenta. Stessa convenzione dei moduli fratelli (cap05 e cap06 di
questa fonte), che spostano le NOTE annotatrici accanto alle righe annotate.

DUBBIO DI GRANULARITA' APERTO per la revisione umana: cap05 di questa stessa
fonte, davanti allo stesso caso (requisiti numerati 1)-6) della clausola 5.4.2,
richiamati per numero all'interno della stessa clausola: "certificates in 1),
2), and 3)"), li ha lasciati dentro il nodo della sottoclausta; cap06 ha
invece scomposto i passi numerati di 5.5.2.3 e 5.5.3, richiamati per numero da
altre clausole. Qui e' stata seguita la lettura di cap06 (granularita' fine,
come richiesto). Con la lettura piu' restrittiva le 31 righe diventano 10 (una
per l'Annex A.1.1, A.1.2, A.1.3, A.1.4, A.1.5.1.1, A.1.5.1.2, A.1.5.1.3,
A.1.5.2.1, A.1.5.2.2, A.1.5.2.3, A.2.1, A.2.2, Annex B, C.1 e C.2): e' una
riorganizzazione dei nodi, non un cambio di testo.

Riferimenti: forma italiana convenzionale "Annex A, clausola A.1.1 (titolo)"
per le unita' numerate dell'annesso (l'annesso fa da prefisso alla numerazione
del testo ufficiale, A.1.1, come la clausola 5 di questa fonte si scrive
"clausola 5.2.2 (titolo)"), "Annex A, clausola A.1.1, requisito 1)" per le
voci numerate, "Annex B (titolo)" per l'annesso che e' esso stesso l'unita',
"Annex C, clausola C.1 (titolo)". La scelta fa generare a
neo4j_common.partizioni_di le partizioni corrette ("Annex A, clausola A.1" ->
"Annex A", ADR-0012): verificato sui riferimenti di questo modulo.

Obbligo o Principio, riga per riga
----------------------------------
28 Obblighi nell'Annex A e nell'Annex B, 2 Principi nell'Annex C. Ogni riga
dell'Annex A e dell'Annex B porta almeno un verbo deontico ("shall be", "shall
contain", "shall not contain", "shall be defined as", "shall use", "shall be
built", "shall be specified", "shall be used") o e' la voce numerata di una
prescrizione con verbo deontico nel chapeau.

- A.1.1-A.1.4, riga della sottoclausta -> Obbligo "tecnico/sicurezza": la
  sottoclausta enuncia il tipo della property ("shall be an unsigned
  qualifying property qualifying the signature"), la sintassi ("shall be
  defined as in XML Schema file ..., whose location is detailed in clause
  C.1/C.2") e i requisiti della property che il testo non numera (per A.1.1 e
  A.1.3 il vincolo "all the certificates referenced ... shall be present
  elsewhere in the signature"; per A.1.2 la lunga serie di requisiti sui figli
  di CRLRef/OCSPRef e sui dati di revoca; per A.1.4 il requisito sulle CRL
  differenziali e quello sui dati di revoca presenti altrove).
- A.1.1-A.1.4, righe dei requisiti 1)-5) e 1)-3) -> Obblighi
  "tecnico/sicurezza": ciascuna voce e' un requisito di contenuto della
  property (quali riferimenti a certificati o a valori di revoca devono,
  non devono o possono esserci). La forza modale e' conservata nel `testo`
  ("deve"/"non deve"/"puo'") e resta verbatim in `testo_integrale`; i "should
  not be included" interni alle voci restano in una riga Obbligo per la stessa
  ragione dei moduli fratelli (il censimento non ha un tipo di obbligo
  "raccomandazione" e nessun tipo di principio descrive una raccomandazione
  operativa rivolta all'oggetto della property).
- A.1.5.1.1 e A.1.5.2.1 (Semantics and syntax) -> Obblighi
  "tecnico/sicurezza": enunciano il tipo della property e quali componenti la
  marca temporale deve marcare.
- A.1.5.1.2, A.1.5.1.3, A.1.5.2.2, A.1.5.2.3 -> Obblighi "procedurale":
  prescrivono come costruire l'input di calcolo dell'impronta della marca
  temporale (meccanismo implicito nel caso non distribuito, generazione degli
  Include nel caso distribuito). Stessa classificazione dei passi di calcolo
  della clausola 5.5.2.3 di questa fonte (cap06).
- A.2.1 -> Obbligo "tecnico/sicurezza": le property deprecate sono mantenute
  nel documento ma "shall not be added to any new XAdES signature".
- A.2.2 -> Obbligo "tecnico/sicurezza": la RenewedDigests e' deprecata e "shall
  be used" la RenewedDigestsV2 definita nel presente documento.
- Annex B -> Obbligo "tecnico/sicurezza": se un meccanismo diverso da quelli
  della clausola 5.5 viene incorporato con una property non firmata, per esso
  devono essere specificate semantica e sintassi, strategia di protezione
  della firma, trattamento delle property del presente documento e trattamento
  delle firme XAdES legacy.
- C.1 e C.2 -> Principi "altro". Il testo e' dichiarativo ("The file at
  <url> (<file>.xsd) contains the definitions of qualifying properties defined
  within the namespace whose URI value is <namespace>."): individua il file di
  schema XML normativo di ciascun namespace e le NOTE di annesso lo
  confrontano con il file della versione V1.2.1 [i.20]. Nessun comportamento e'
  imposto in questa clausola: i "shall be defined as in XML Schema file ...,
  whose location is detailed in clause C.1/C.2" stanno nelle clausole
  citanti. DUBBIO APERTO per la revisione umana: la classificazione poteva
  essere "definitorio"; qui si e' preferito "altro" perche' la clausola non
  definisce un concetto ma identifica un artefatto normativo.

Soggetti: nessuna riga di questo capitolo valorizza `soggetti`. Il testo degli
annessi non nomina mai il soggetto obbligato: prescrive sulla property o sui
suoi elementi in forma impersonale ("The CompleteCertificateRefsV2 qualifying
property shall be ...", "The CRLRefs element shall contain ...", "Empty
CompleteRevocationRefs qualifying properties shall not be incorporated"), e
anche dove enuncia un divieto generale ("they shall not be added to any new
XAdES signature", Annex A.2.1) non nomina chi genera la firma. Convenzione
seguita da cap05 di questa fonte ("soggetti valorizzati solo dove il testo
nomina davvero il soggetto").

Nessun `oggetti_giuridici`: il testo nomina qualifying property XAdES,
elementi e tipi XML, marche temporali elettroniche generiche e firme XAdES,
mai uno degli oggetti della tassonomia eIDAS (firma elettronica qualificata,
sigillo elettronico, marca temporale elettronica qualificata, documento
elettronico, ...). "electronic time-stamp" senza qualificazione non e' la
marca temporale elettronica qualificata e "XAdES signature" non e' un oggetto
dello schema: stesso criterio di cap04 e cap05 di questa fonte.

`severita` e `sanzioni` assenti (standard tecnico, nessuna sanzione); `stato`
sempre "vigente", anche per A.2.1/A.2.2, che dichiarano la deprecazione di
property di versioni precedenti: la disposizione che le depreca e' in vigore.
`condizione_applicabilita` mai valorizzata: le condizioni interne del testo
("If at least one of the following unsigned properties ... is incorporated
into the signature", "If such a mechanism is incorporated into the signature
using an unsigned property", "If one or more of the identified CRLs are a
Delta CRL") sono parte della prescrizione e restano nel `testo_integrale`
della riga, dove il testo ufficiale le colloca.

Fedelta' dell'estrazione
------------------------
- Paratesto escluso: il pie' di pagina "ETSI" e la testatina "<n> ETSI EN 319
  132-1 V1.3.1 (2024-07)" delle pagine 64-74, con le righe vuote di
  impaginazione che li circondano. Le intestazioni di pagina non sono contenuto
  normativo.
- Righe spezzate a meta' frase: ricucite in un'unica riga. Il trattino di fine
  riga appartiene sempre alla parola, mai una sillabazione da rimuovere: il
  nome del file di schema "1913201-" + "XAdES01903v132.xsd" / "1913201-" +
  "XAdES01903v141.xsd" e' ricomposto senza spazio, e "out-of-" + "band" ->
  "out-of-band" nella NOTE 6 di A.1.2.
- Blocchi di schema XML: riportati come il testo li presenta, con
  l'indentazione del testo ufficiale. Un'interruzione di pagina cade dentro il
  blocco di A.1.2 (fra </xsd:sequence> e </xsd:complexType> di
  CRLRefsType, pagine 64-65): il blocco e' stato ricucito come continuo, senza
  righe vuote introdotte dal salto di pagina. Le righe vuote fra un
  <xsd:complexType> e il successivo sono quelle presenti nel testo.
- A.1.2: i due commenti XML di intestazione del file di schema ("<!--
  targetNamespace=..." ) sono riportati come nel testo, compresa la forma con
  la dichiarazione di namespace su tre righe, identica in A.1.1, A.1.3,
  A.1.5.1.1 e A.1.5.2.1.
- Refusi del documento conservati, non corretti: "The CertRefs element is of
  type xades:CertIDListV2Type , already defined in clause 5.2.2." (spazio
  prima della virgola); "the base-64 encoding of the DER-encoded of byKey
  field" (A.1.2); "Each OcspRef child of OCSPRefs" con "OcspRef" (maiuscole
  diverse da OCSPRef, A.1.2); "797" non compare, ma il testo di A.1.2 usa
  indifferentemente "defined in namespace whose URI is" e "defined in the
  namespace whose URI is" nei due paragrafi "If at least one ...": entrambe le
  forme sono riportate come nel testo.
- Marcatori di elenco: i punti elenco di A.1.5.1.2 e A.1.5.1.3 sono trattini
  ("- the SignatureTimeStamp qualifying properties;") e quelli di A.1.5.2.2 e
  A.1.5.2.3 sono U+2022 ("• the CompleteCertificateRefsV2 qualifying
  property;"): riportati ciascuno come il testo ufficiale lo presenta.
- Indentazione dei blocchi di testo (voci numerate, NOTE rientrate, elenchi
  puntati) uniformata a inizio riga, come nei moduli fratelli di questa fonte;
  il contenuto verbale non e' stato toccato. La spaziatura irregolare dopo la
  parola chiave "NOTE:" in A.1.4 ("NOTE:      A trust anchor is by definition
  trusted") e' normalizzata a "NOTE: ".
- Le NOTE restano nella riga dell'unita' che annotano, senza duplicazioni ne'
  spostamenti di contenuto: NOTE 1 di A.1.1 va nella riga del requisito 5) (le
  cui voci nomina: i riferimenti a certificati usati esclusivamente per
  certificati di attributo, conservati in AttributeCertificateRefsV2), NOTE 2
  di A.1.1 nella riga della sottoclausta (annota il tipo nel suo insieme),
  NOTE 1 di A.1.2 nella riga del requisito 2) (trust anchor, valori di revoca),
  NOTE 2 di A.1.2 nella riga del requisito 5), NOTE 3-7 di A.1.2 nella riga
  della sottoclausta (annotano i requisiti non numerati su Number, URI,
  DigestAlgAndValue e l'insieme di property; le NOTE 3-7 sono collocate nel
  testo ufficiale dopo i requisiti che annotano, e li' restano), NOTE di A.1.4
  nella riga del requisito 1) (trust anchor), NOTE 1-2 di Annex B nella riga
  dell'annesso (annotano il meccanismo nel suo insieme).

Rinvii demandati alla fase 6 (nessuna relazione creata verso di essi)
--------------------------------------------------------------------
- Clausole di altri capitoli dello stesso documento, citate nei
  `testo_integrale` di queste righe: A.1.1 ("already defined in clause 5.2.2"),
  A.1.1 voce 5) e A.1.2 voce 5) (SignerRoleV2, clausola 5.2.6), A.1.1/A.1.2/
  A.1.3 (CertificateValues, AttrAuthoritiesCertValues, AnyValidationData,
  ArchiveTimeStamp: clausole 5.4.x e 5.5.x), A.1.2 (clausola 4.5.4.1 di XMLDSIG
  per i Distinguished Names, clausola 5.4.x per RevocationValues e
  AttributeRevocationValues), A.1.5.1.1 (le property elencate come componenti
  marcatati: CompleteCertificateRefsV2, CompleteRevocationRefs,
  AttributeCertificateRefsV2, AttributeRevocationRefs, SignatureTimeStamp,
  SignaturePolicyIdentifier... clausole 5.2.x, 5.3 e A.1.x), A.1.5.1.2,
  A.1.5.1.3, A.1.5.2.2 e A.1.5.2.3 (clausola 4.5 per la canonicalizzazione),
  A.1.5.1.3 e A.1.5.2.3 (clausola 5.1.4.4.2.1 per la costruzione degli
  attributi URI), A.2.2 (clausola 5.5.3 del presente documento per
  RenewedDigestsV2, capitolo cap06), Annex B (clausola 5.5 e NOTE 1: clausola 6
  per il livello XAdES-B-LTA, capitolo cap07).
- Unita' indivise senza nodo proprio, da collegare alle partizioni generate
  dalle righe di questo modulo (la sessione principale le dichiara, ADR-0012:
  un modulo capitolo non dichiara archi verso partizioni): A.2.1 -> "Clause
  A.2 lists deprecated qualified properties" (partizione "Annex A, clausola
  A.2", generata dalla riga A.2.1); A.1.5.1.1 e A.1.5.2.1 -> l'intestazione di
  raggruppamento A.1.5.1/A.1.5.2 (partizioni "Annex A, clausola A.1.5.1" e
  "Annex A, clausola A.1.5.2", generate dalle righe A.1.5.1.x e A.1.5.2.x).
- Nomi di property ed elementi citati come componenti marcatati o come
  contenuto ammesso (gli elenchi di A.1.5.1.2, A.1.5.1.3, A.1.5.2.2 e
  A.1.5.2.3, OtherRefs in A.1.2): NON generano archi in questo modulo ne'
  sono annotati come rinvii demandati, perche' sono l'elenco degli elementi
  che la marca temporale copre o ammette, non un rinvio alla clausola che li
  definisce. Decisione esplicita, per non gonfiare il grafo di archi di
  semplice menzione.
- Norme e specifiche esterne, non censite nel grafo: XMLDSIG [1] (clausola
  4.5.4.1, A.1.2), IETF RFC 6960 [6] (A.1.2, ByKey e OCSPResponse), ETSI EN
  319 132-1 (V1.1.1) [i.19] (A.2.1, A.2.2), ETSI EN 319 132-2 [i.17] e ETSI
  EN 319 132-1 (V1.2.1) [i.20] (Annex B NOTE 1, Annex C.1 e C.2 NOTE).

Relazioni dichiarate
--------------------
33 relazioni, tutte fra righe di questo modulo (nessuna verso altri capitoli o
altre fonti: partizioni e collegamenti cross-fonte li costruisce la sessione
principale in fase 6, ADR-0009/ADR-0012). `confidence` resta null su tutte:
non esiste uno score reale da riportare (ADR-0005).

16 relazioni "specifica" con `evidence_type` "inferred": ricostruiscono la
gerarchia fra la riga di una sottoclausta e le righe dei requisiti numerati in
cui e' scomposta (nodo generale reso operativo da nodi piu' specifici,
CONTEXT.md). Sono A.1.1 -> requisiti 1)-5), A.1.2 -> requisiti 1)-5), A.1.3 ->
requisiti 1)-3), A.1.4 -> requisiti 1)-3). Il livello delle partizioni non puo'
derivarle: la catena di `partizioni_di` si ferma ad "Annex A, clausola A.1" e
non conosce il marcatore "requisito N)" (stessa ragione documentata da cap06
per i propri passi numerati).

13 relazioni "richiama" con `evidence_type` "textual", tutte citazioni
letterali presenti nel `testo_integrale` del nodo citante:
- A.1.1 requisito 4) -> requisiti 1) e 3) ("references in 1) and 3)"), 2
  relazioni; A.1.2 requisito 4) -> requisiti 1), 2) e 3) ("referenced in
  references from 1), 2) and 3)"), 3 relazioni. NOTA PER L'AUDIT: nel testo
  citante la voce e' nominata con il solo numero nudo dell'elenco ("1) and
  3)"), traccia che `app/tools/verifica_relazioni_textual.py` non sa cercare
  (la sua lista di tracce copre numeri di clausola, annesso, articolo, comma,
  punto e id ASN.1, non la voce interna di un elenco numerato). L'evidenza e'
  comunque letterale, quindi `textual` e' corretto e le segnalazioni di questi
  5 archi sono attese.
- A.1.1 requisito 5) -> A.1.3 ("see clause A.1.3", NOTE 1); A.1.2 requisito 5)
  -> A.1.4 ("see clause A.1.4", NOTE 2), 2 relazioni.
- A.1.1, A.1.3, A.1.5.1.1 e A.1.5.2.1 -> C.2 ("whose location is detailed in
  clause C.2"); A.1.2 e A.1.4 -> C.1 ("whose location is detailed in clause
  C.1"), 6 relazioni. Sono i soli archi di questo capitolo che escono dal
  perimetro dell'Annex A e legano le property ai Principi C.1/C.2 dello stesso
  modulo (i moduli fratelli li davano per privi di nodo: vedi "Perimetro").

4 relazioni "richiama" con `evidence_type` "inferred": A.1.5.1.1 -> A.1.5.1.2
e A.1.5.1.3; A.1.5.2.1 -> A.1.5.2.2 e A.1.5.2.3. Il rinvio e' letterale ma
privo del numero di clausola ("Details are given in clauses below", una volta
in A.1.5.1.1 e una in A.1.5.2.1): la destinazione e' esplicita nel testo
(sotto-clausole immediatamente seguenti: caso non distribuito e caso
distribuito) ma non verificabile meccanicamente, quindi la provenienza
dichiarata e' la piu' debole.

Copertura
---------
31 item di indice, 31 righe: 29 obblighi + 2 principi. Nessun item doppio,
nessun item mancante, nessuna riga fuori indice. Verifica di completezza fatta
anche per paragrafi sul testo ufficiale del perimetro (confronto su file,
non lettura a occhio): ogni paragrafo delle 674 righe di cap08.txt compare
verbatim, dopo normalizzazione degli spazi, nell'unione dei `testo_integrale`
di questo modulo, con le sole differenze volute dalla ricucitura dei ritorni a
capo del PDF (i nomi di file "1913201-XAdES01903v132.xsd" e
"1913201-XAdES01903v141.xsd" e "out-of-band" ricomposti senza spazio).
Nell'unione non compaiono soltanto i titoli di annesso e di sottoclausta del
testo ufficiale - che vivono nei `riferimento` e negli item di indice ("Annex C
(normative): XML Schema files", "A.1.5.1.3 Distributed case", ...) - e le
etichette "Semantics"/"Syntax", che nei `testo_integrale` sono unite alla
prima frase della rispettiva sezione ("Semantics: The ...", "Syntax: The
..."), come nei moduli fratelli di questa fonte. Nessuna parola di testo
normativo e' assente, nessuna parola e' aggiunta.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "Annex A, clausola A.1.1 (The CompleteCertificateRefsV2 qualifying property)",
        "testo": (
            "La CompleteCertificateRefsV2 deve essere una qualifying property non firmata che qualifica la "
            "firma; l'elemento omonimo e' definito dal file di schema XML 1913201-XAdES01903v141.xsd (clausola "
            "C.2) e contiene un solo figlio CertRefs di tipo xades:CertIDListV2Type, gia' definito nella clausola "
            "5.2.2. Quando nella firma e' incorporata almeno una fra le property non firmate CertificateValues, "
            "AttrAuthoritiesCertValues, AnyValidationData (con figlio CertificateValues non vuoto) o "
            "ArchiveTimeStamp del namespace 1.4.1, tutti i certificati referenziati in CompleteCertificateRefsV2 "
            "devono essere presenti altrove nella firma."
        ),
        "testo_integrale": (
            """Semantics: The CompleteCertificateRefsV2 qualifying property shall be an unsigned qualifying property qualifying the signature.

The CompleteCertificateRefsV2 qualifying property:

Syntax: The CompleteCertificateRefsV2 element shall be defined as in XML Schema file "1913201-XAdES01903v141.xsd", whose location is detailed in clause C.2, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.4.1#"

The preamble of the XML Schema file also includes the following namespace declaration:
  xmlns:xades="http://uri.etsi.org/01903/v1.3.2#",
which assigns the prefix "xades" to the namespace whose URI is shown in the declaration.
-->

<xsd:element name="CompleteCertificateRefsV2" type="CompleteCertificateRefsTypeV2"/>
<xsd:complexType name="CompleteCertificateRefsTypeV2">
    <xsd:sequence>
        <xsd:element name="CertRefs" type="xades:CertIDListV2Type"/>
    </xsd:sequence>
    <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

The CertRefs element is of type xades:CertIDListV2Type , already defined in clause 5.2.2.

If at least one of the following unsigned properties: CertificateValues, AttrAuthoritiesCertValues, AnyValidationData with a non empty CertificateValues child element, or the ArchiveTimeStamp defined in the namespace whose URI is http://uri.etsi.org/01903/v1.4.1#, is incorporated into the signature, all the certificates referenced in CompleteCertificateRefsV2 shall be present elsewhere in the signature.

NOTE 2: If XML electronic time-stamps based in XMLDSIG are standardized and spread, this type can also be used to contain references to the certification chain for any TSUs providing such electronic time-stamps. In this case, an element of this type can be added as an unsigned qualifying property to the XML electronic time-stamp using the incorporation mechanisms defined in the present document."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.1, requisito 1)",
        "testo": (
            "La property deve contenere il riferimento al certificato della trust anchor, se un tale certificato "
            "esiste, e i riferimenti ai certificati di CA che stanno nel percorso del certificato di firma."
        ),
        "testo_integrale": (
            "1) Shall contain the reference to the certificate of the trust anchor if such certificate does "
            "exist, and the references to CA certificates within the signing certificate path."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.1, requisito 2)",
        "testo": "La property non deve contenere il riferimento al certificato di firma.",
        "testo_integrale": (
            "2) Shall not contain the reference to the signing certificate."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.1, requisito 3)",
        "testo": (
            "La property puo' contenere i riferimenti ai certificati che stanno nel percorso dei certificati "
            "usati per firmare le marche temporali elettroniche gia' incorporate nella firma al momento "
            "dell'incorporazione della property, compresi i certificati di firma di quelle marche e i "
            "certificati delle trust anchor, se esistono."
        ),
        "testo_integrale": (
            "3) May contain references to certificates in the path of the certificates used for signing the "
            "electronic time-stamps already incorporated into the signature when the CompleteCertificateRefsV2 "
            "unsigned property is incorporated, including references to the electronic time-stamps' signing "
            "certificates and references to certificates of trust anchors if such certificates do exist."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.1, requisito 4)",
        "testo": (
            "La property puo' contenere i riferimenti ai certificati usati per firmare le CRL o le risposte "
            "OCSP relative ai certificati referenziati nelle voci 1) e 3), e ai certificati che stanno nei "
            "rispettivi percorsi di certificazione."
        ),
        "testo_integrale": (
            "4) May contain references to the certificates used to sign CRLs or OCSP responses for certificates "
            "referenced by references in 1) and 3), and references to certificates within their respective "
            "certificate paths. And"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.1, requisito 5)",
        "testo": (
            "La property non deve contenere riferimenti a certificati di CA che appartengono esclusivamente ai "
            "percorsi di certificazione dei certificati usati per firmare certificati di attributo o assertion "
            "firmate dentro SignerRoleV2; i riferimenti a certificati usati esclusivamente nella convalida di "
            "certificati di attributo o assertion firmate sono conservati nella property "
            "AttributeCertificateRefsV2 (clausola A.1.3)."
        ),
        "testo_integrale": (
            """5) Shall not contain references to CA certificates that pertain exclusively to the certificate paths of certificates used to sign attribute certificates or signed assertions within SignerRoleV2.

NOTE 1: The references to certificates exclusively used in the validation of attribute certificate or signed assertions are stored in the AttributeCertificateRefsV2 qualifying property (see clause A.1.3)."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.2 (The CompleteRevocationRefs qualifying property)",
        "testo": (
            "La CompleteRevocationRefs deve essere una qualifying property non firmata che qualifica la firma; "
            "l'elemento omonimo e' definito dal file di schema XML 1913201-XAdES01903v132.xsd (clausola C.1) e "
            "contiene le sequenze opzionali CRLRefs, OCSPRefs e OtherRefs. La clausola fissa i requisiti di "
            "contenuto dei riferimenti a CRL (CRLRefs, Issuer, IssueTime, Number, attributo URI, CRL "
            "differenziali) e a risposte OCSP (OCSPRefs, ResponderID con ByName o ByKey, ProducedAt, attributo "
            "URI, DigestAlgAndValue), vieta di incorporare property CompleteRevocationRefs vuote e prescrive che, "
            "se nella firma e' incorporata almeno una delle property non firmate RevocationValues, "
            "AttributeRevocationValues, AnyValidationData (con figlio RevocationValues non vuoto) o "
            "ArchiveTimeStamp del namespace 1.4.1, tutti i dati di revoca referenziati siano presenti altrove "
            "nella firma."
        ),
        "testo_integrale": (
            """Semantics: The CompleteRevocationRefs qualifying property shall be an unsigned qualifying property that qualifies the signature.

The CompleteRevocationRefs qualifying property:

References within CompleteRevocationRefs qualifying property may be references to CRLs, OCSP responses and other type of revocation data.

Syntax: The CompleteRevocationRefs qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="CompleteRevocationRefs"
  type="CompleteRevocationRefsType"/>

<xsd:complexType name="CompleteRevocationRefsType">
  <xsd:sequence>
    <xsd:element name="CRLRefs" type="CRLRefsType" minOccurs="0"/>
    <xsd:element name="OCSPRefs" type="OCSPRefsType" minOccurs="0"/>
    <xsd:element name="OtherRefs" type="OtherCertStatusRefsType"
      minOccurs="0"/>
  </xsd:sequence>
  <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

<xsd:complexType name="CRLRefsType">
  <xsd:sequence>
    <xsd:element name="CRLRef" type="CRLRefType"
      maxOccurs="unbounded"/>
  </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="CRLRefType">
  <xsd:sequence>
    <xsd:element name="DigestAlgAndValue"
      type="DigestAlgAndValueType"/>
    <xsd:element name="CRLIdentifier" type="CRLIdentifierType"
      minOccurs="0"/>
  </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="CRLIdentifierType">
  <xsd:sequence>
    <xsd:element name="Issuer" type="xsd:string"/>
    <xsd:element name="IssueTime" type="xsd:dateTime" />
    <xsd:element name="Number" type="xsd:integer" minOccurs="0"/>
  </xsd:sequence>
  <xsd:attribute name="URI" type="xsd:anyURI" use="optional"/>
</xsd:complexType>

<xsd:complexType name="OCSPRefsType">
  <xsd:sequence>
    <xsd:element name="OCSPRef" type="OCSPRefType"
      maxOccurs="unbounded"/>
  </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="OCSPRefType">
  <xsd:sequence>
    <xsd:element name="OCSPIdentifier" type="OCSPIdentifierType"/>
    <xsd:element name="DigestAlgAndValue"
      type="DigestAlgAndValueType"
      minOccurs="0"/>
  </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="ResponderIDType">
  <xsd:choice>
    <xsd:element name="ByName" type="xsd:string"/>
    <xsd:element name="ByKey" type="xsd:base64Binary"/>
  </xsd:choice>
</xsd:complexType>

<xsd:complexType name="OCSPIdentifierType">
  <xsd:sequence>
    <xsd:element name="ResponderID" type="ResponderIDType"/>
    <xsd:element name="ProducedAt" type="xsd:dateTime"/>
  </xsd:sequence>
  <xsd:attribute name="URI" type="xsd:anyURI" use="optional"/>
</xsd:complexType>

<xsd:complexType name="OtherCertStatusRefsType">
  <xsd:sequence>
    <xsd:element name="OtherRef" type="AnyType"
      maxOccurs="unbounded"/>
  </xsd:sequence>
</xsd:complexType>

Empty CompleteRevocationRefs qualifying properties shall not be incorporated.

The CRLRefs element shall contain a sequence of references to CRLs.

Each CRLRef child of CRLRefs shall contain one reference to one CRL.

The DigestAlgAndValue child of CRLRef element shall contain one indication of a digest algorithm, and the base-64 encoding of the digest value of the DER-encoded referenced CRL.

The CRLIdentifier child needs not to be present if the referenced CRL can be inferred from other information.

The CRLIdentifier child of CRLRef element shall include the name issuer in its Issuer element.

The value of Issuer child of CRLIdentifier element shall fulfil the requirements specified in clause 4.5.4.1 of XMLDSIG [1] for strings representing Distinguished Names.

The CRLIdentifier child of CRLRef element shall include the time when the CRL was issued in its IssueTime element.

The CRLIdentifier child of CRLRef element may include the number of the CRL in its Number element.

NOTE 3: The Number element is an optional hint helping to get the CRL whose digest matches the value present in the reference.

URI attribute of CRLIdentifier element shall indicate one place where the referenced CRL can be found.

NOTE 4: It is intended that this attribute be used as a hint, as implementations can have alternative ways for retrieving the referenced CRL if it is not found at the referenced place.

If one or more of the identified CRLs are a Delta CRL, this qualifying property shall include references to the set of CRLs required to provide complete revocation lists.

The OCSPRefs element shall contain a sequence of references to OCSP responses.

Each OcspRef child of OCSPRefs shall contain one reference to one OCSP response.

The OCSPIdentifier child of OCSPRef element shall include an identifier of the responder in its ResponderID child.

If the responder is identified by its name, then this name shall appear within the ByName child of ResponderID element.

The value of ByName element shall fulfil the requirements specified in clause 4.5.4.1 of XMLDSIG [1] for strings representing Distinguished Names.

If the responder is identified by the digest of the server's public key computed as mandated in IETF RFC 6960 [6], then the base-64 encoding of the DER-encoded of byKey field specified in IETF RFC 6960 [6] shall appear within the ByKey child of ResponderID element.

The OCSPIdentifier child of OCSPRef element shall include the generation time of the OCSP response in its ProducedAt child.

The value in ProducedAt child of OCSPIdentifier shall indicate the same time as the time indicated by the ProducedAt field of the referenced OCSP response.

URI attribute of OCSPIdentifier element indicates one place where the referenced OCSP response can be archived.

NOTE 5: It is intended that this attribute be used as a hint, as implementations can have alternative ways for retrieving the referenced OCSP response if it is not found at the referenced place.

The DigestAlgAndValue child of OCSPRef element shall contain one indication of a digest algorithm, and the base-64 encoding of the DER-encoded OCSPResponse field defined in IETF RFC 6960 [6].

The DigestAlgAndValue child element should be included within the OCSPRef element.

NOTE 6: The absence of the DigestAlgAndValue child of OCSPRef element makes OCSP responses substitutions attacks possible, if for instance OCSP responder keys are compromised. In this case, out-of-band mechanisms can be used to ensure that none of the OCSP responder keys have been compromised at the time of validation.

References to alternative forms of validation data may be included in this qualifying property making use of the OtherRefs element, a sequence whose items (OtherRef elements) may contain any kind of information. Their semantics and syntax are outside the scope of the present document.

If at least one of the following unsigned properties: RevocationValues, AttributeRevocationValues, AnyValidationData with a non empty RevocationValues child element, or the ArchiveTimeStamp defined in namespace whose URI is http://uri.etsi.org/01903/v1.4.1#, is incorporated into the signature, all the revocation data referenced in CompleteRevocationRefs shall be present elsewhere in the signature.

NOTE 7: If XML electronic time-stamps based in XMLDSIG are standardized and spread, this type can also serve to contain references to the full set of CRL or OCSP responses that have been used to verify the certification chain for any TSUs providing such electronic time-stamps. In this case, an element of this type can be added as an unsigned qualifying property to the XML electronic time-stamp using the incorporation mechanisms defined in the present document."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.2, requisito 1)",
        "testo": "La property deve contenere un riferimento a un valore di revoca per il certificato di firma.",
        "testo_integrale": (
            "1) Shall contain a reference to a revocation value for the signing certificate."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.2, requisito 2)",
        "testo": (
            "La property deve contenere i riferimenti ai valori di revoca (per esempio CRL o risposte OCSP) "
            "corrispondenti ai certificati di CA che stanno nel percorso del certificato di firma; non deve "
            "contenere riferimenti a valori di revoca per la trust anchor, che per definizione e' fidata e quindi "
            "non richiede informazioni di revoca in convalida."
        ),
        "testo_integrale": (
            """2) Shall contain the references to the revocation values (e.g. CRLs or OCSP values) corresponding to CA certificates within the signing certificate path. It shall not contain references to revocation values for the trust anchor.

NOTE 1: A trust anchor is by definition trusted, thus no revocation information for the trust anchor is used during the validation."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.2, requisito 3)",
        "testo": (
            "La property puo' contenere i riferimenti ai valori di revoca (per esempio CRL o risposte OCSP) "
            "corrispondenti ai certificati che stanno nel percorso dei certificati di firma delle marche "
            "temporali elettroniche gia' incorporate nella firma al momento dell'incorporazione della property; "
            "non deve contenere riferimenti ai valori di revoca delle trust anchor di quei certificati."
        ),
        "testo_integrale": (
            "3) May contain references to revocation values (e.g. CRLs or OCSP values) corresponding to "
            "certificates in the path of signing certificates of electronic time-stamps already incorporated "
            "into the signature when the CompleteRevocationRefs unsigned property is incorporated. It shall not "
            "contain references to revocation values for the trust anchors of these certificates."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.2, requisito 4)",
        "testo": (
            "La property puo' contenere i riferimenti ai valori di revoca corrispondenti ai certificati usati "
            "per firmare le CRL o le risposte OCSP richiamate nelle voci 1), 2) e 3), e ai certificati che "
            "stanno nei rispettivi percorsi di certificazione."
        ),
        "testo_integrale": (
            "4) May contain references to the revocation values corresponding to certificates used to sign CRLs "
            "or OCSP responses referenced in references from 1), 2) and 3), and to certificates within their "
            "respective certificate paths. And"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.2, requisito 5)",
        "testo": (
            "La property non deve contenere riferimenti ai valori di revoca corrispondenti a certificati di CA "
            "che appartengono esclusivamente ai percorsi di certificazione dei certificati usati per firmare "
            "certificati di attributo o assertion firmate dentro le property SignerRoleV2; quei riferimenti sono "
            "conservati nella property AttributeRevocationRefs (clausola A.1.4)."
        ),
        "testo_integrale": (
            """5) Shall not contain references to the revocation values corresponding to CA certificates that pertain exclusively to the certificate paths of certificates used to sign attribute certificates or signed assertions within SignerRoleV2 qualifying properties.

NOTE 2: The references to revocation values exclusively used in the validation of attribute certificate or signed assertions are stored in the AttributeRevocationRefs qualifying property (see clause A.1.4)."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.3 (The AttributeCertificateRefsV2 qualifying property)",
        "testo": (
            "La AttributeCertificateRefsV2 deve essere una qualifying property non firmata che qualifica la "
            "firma; l'elemento omonimo e' definito dal file di schema XML 1913201-XAdES01903v141.xsd (clausola "
            "C.2) ed e' dello stesso tipo CompleteCertificateRefsTypeV2 della CompleteCertificateRefsV2. Se nella "
            "firma e' incorporata almeno una fra le property non firmate CertificateValues, "
            "AttrAuthoritiesCertValues, AnyValidationData (con figlio CertificateValues non vuoto) o "
            "ArchiveTimeStamp del namespace 1.4.1, tutti i certificati referenziati devono essere presenti "
            "altrove nella firma."
        ),
        "testo_integrale": (
            """Semantics: The AttributeCertificateRefsV2 qualifying property shall be an unsigned qualifying property that qualifies the signature.

The AttributeCertificateRefsV2 qualifying property:

Syntax: The AttributeCertificateRefsV2 element shall be defined as in XML Schema file "1913201-XAdES01903v141.xsd", whose location is detailed in clause C.2, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.4.1#"

The preamble of the XML Schema file also includes the following namespace declaration:
  xmlns:xades="http://uri.etsi.org/01903/v1.3.2#",
which assigns the prefix "xades" to the namespace whose URI is shown in the declaration.
-->

<xsd:element name="AttributeCertificateRefsV2" type="CompleteCertificateRefsTypeV2"/>

If at least one of the following unsigned properties: CertificateValues, AttrAuthoritiesCertValues, AnyValidationData with a non empty CertificateValues child element, or the ArchiveTimeStamp defined in namespace whose URI is http://uri.etsi.org/01903/v1.4.1#, is incorporated into the signature, all the certificates referenced in AttributeCertificateRefsV2 shall be present elsewhere in the signature."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.3, requisito 1)",
        "testo": (
            "Se non sono gia' presenti nella CompleteCertificateRefsV2 o nella SigningCertificateV2, la property "
            "deve contenere i riferimenti alle trust anchor (se esistono certificati per esse) e i riferimenti ai "
            "certificati di CA che stanno nel percorso dei certificati di firma dei certificati di attributo e "
            "delle assertion firmate incorporati nella firma XAdES; i riferimenti gia' presenti in quelle due "
            "property non dovrebbero essere ripetuti."
        ),
        "testo_integrale": (
            "1) Shall contain, if they are not present within CompleteCertificateRefsV2 or SigningCertificateV2 "
            "qualifying properties, the references to the trust anchors if certificates exist for them, and the "
            "references to CA certificates within the path of the signing certificate(s) of the attribute "
            "certificate(s) and signed assertion(s) incorporated into the XAdES signature. References present "
            "within CompleteCertificateRefsV2 or SigningCertificateV2 qualifying properties should not be "
            "included."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.3, requisito 2)",
        "testo": (
            "Se non sono gia' presenti nella CompleteCertificateRefsV2 o nella SigningCertificateV2, la property "
            "deve contenere i riferimenti ai certificati di firma dei certificati di attributo e delle assertion "
            "firmate incorporati nella firma XAdES; i riferimenti gia' presenti in quelle due property non "
            "dovrebbero essere ripetuti."
        ),
        "testo_integrale": (
            "2) Shall contain, if they are not present within CompleteCertificateRefsV2 or SigningCertificateV2 "
            "qualifying properties, the reference(s) to the signing certificate(s) of the attribute "
            "certificate(s) and signed assertion(s) incorporated into the XAdES signature. References present "
            "within CompleteCertificateRefsV2 or SigningCertificateV2 qualifying properties should not be "
            "included. And"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.3, requisito 3)",
        "testo": (
            "La property puo' contenere i riferimenti ai certificati usati per firmare le CRL o le risposte OCSP "
            "e ai certificati che stanno nei rispettivi percorsi di certificazione, usati per validare i "
            "certificati di firma dei certificati di attributo e delle assertion firmate incorporati nella firma "
            "XAdES; i riferimenti gia' presenti nella CompleteCertificateRefsV2 o nella SigningCertificateV2 non "
            "dovrebbero essere ripetuti."
        ),
        "testo_integrale": (
            "3) May contain references to the certificates used to sign CRLs or OCSP responses and certificates "
            "within their respective certificate paths, which are used for validating the signing certificate(s) "
            "of the attribute certificate(s) and signed assertion(s) incorporated into the XAdES signature. "
            "References present within CompleteCertificateRefsV2 or SigningCertificateV2 qualifying properties "
            "should not be included."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.4 (The AttributeRevocationRefs qualifying property)",
        "testo": (
            "La AttributeRevocationRefs deve essere una qualifying property non firmata che qualifica la firma; "
            "l'elemento omonimo e' definito dal file di schema XML 1913201-XAdES01903v132.xsd (clausola C.1) ed "
            "e' dello stesso tipo CompleteRevocationRefsType della CompleteRevocationRefs. Se una o piu' delle "
            "CRL identificate e' una CRL differenziale (Delta CRL), la property deve includere i riferimenti "
            "all'insieme di CRL necessarie a fornire elenchi di revoca completi; se nella firma e' incorporata "
            "almeno una fra le property non firmate RevocationValues, AttributeRevocationValues, "
            "AnyValidationData (con figlio RevocationValues non vuoto) o ArchiveTimeStamp del namespace 1.4.1, "
            "tutti i dati di revoca referenziati devono essere presenti altrove nella firma."
        ),
        "testo_integrale": (
            """Semantics: The AttributeRevocationRefs qualifying property shall be an unsigned qualifying property that qualifies the signature.

The AttributeRevocationRefs qualifying property:

Syntax: The AttributeRevocationRefs qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="AttributeRevocationRefs" type="CompleteRevocationRefsType"/>

If one or more of the identified CRLs are a Delta CRL, this property shall include references to the set of CRLs required to provide complete revocation lists.

If at least one of the following unsigned properties: RevocationValues, AttributeRevocationValues, AnyValidationData with a non empty RevocationValues child element, or the ArchiveTimeStamp defined in namespace whose URI is http://uri.etsi.org/01903/v1.4.1#, is incorporated into the signature, all the revocation data referenced in AttributeRevocationRefs shall be present elsewhere in the signature."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.4, requisito 1)",
        "testo": (
            "Se non sono gia' presenti nella property CompleteRevocationRefs, la property deve contenere i "
            "riferimenti ai valori di revoca corrispondenti ai certificati di CA che stanno nei percorsi dei "
            "certificati di firma dei certificati di attributo e delle assertion firmate incorporati nella firma "
            "XAdES; non deve contenere un valore di revoca per le trust anchor (una trust anchor e' per "
            "definizione fidata, quindi nessuna informazione di revoca e' usata in convalida) e i riferimenti "
            "gia' presenti nella CompleteRevocationRefs non dovrebbero essere ripetuti."
        ),
        "testo_integrale": (
            """1) Shall contain, if they are not present within the CompleteRevocationRefs qualifying property, the references to the revocation values corresponding to CA certificates within the path(s) of the signing certificate(s) of the attribute certificate(s) and signed assertion(s) incorporated into the XAdES signature. It shall not contain a revocation value for the trust anchors. References present within CompleteRevocationRefs qualifying property should not be included.

NOTE: A trust anchor is by definition trusted, thus no revocation information for the trust anchor is used during the validation."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.4, requisito 2)",
        "testo": (
            "Se non sono gia' presenti nella property CompleteRevocationRefs, la property deve contenere i "
            "riferimenti ai valori di revoca dei certificati di firma dei certificati di attributo e delle "
            "assertion firmate incorporati nella firma XAdES; i riferimenti gia' presenti nella "
            "CompleteRevocationRefs non dovrebbero essere ripetuti."
        ),
        "testo_integrale": (
            "2) Shall contain, if they are not present within the CompleteRevocationRefs qualifying property, "
            "the references to the revocation value(s) for the signing certificate(s) of the attribute "
            "certificate(s) and signed assertion(s) incorporated into the XAdES signature. References present "
            "within CompleteRevocationRefs property should not be included. And"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.4, requisito 3)",
        "testo": (
            "La property puo' contenere i riferimenti ai valori di revoca dei certificati usati per firmare le "
            "CRL o le risposte OCSP e ai certificati che stanno nei rispettivi percorsi di certificazione, usati "
            "per validare i certificati di firma dei certificati di attributo e delle assertion firmate "
            "incorporati nella firma XAdES; i riferimenti gia' presenti nella CompleteRevocationRefs non "
            "dovrebbero essere ripetuti."
        ),
        "testo_integrale": (
            "3) May contain references to the revocation values on certificates used to sign CRLs or OCSP "
            "responses and certificates within their respective certificate paths, which are used for validating "
            "the signing certificate(s) of the attribute certificate(s) and signed assertion(s) incorporated "
            "into the XAdES signature. References present within CompleteRevocationRefs property should not be "
            "included."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.5.1.1 (Semantics and syntax)",
        "testo": (
            "La SigAndRefsTimeStampV2 deve essere una qualifying property non firmata che qualifica la firma e "
            "deve incapsulare marche temporali elettroniche sul valore della firma digitale, sulla marca "
            "temporale della firma (se presente) e sulle qualifying property XAdES che contengono riferimenti ai "
            "dati di convalida; l'elemento e' definito dal file di schema XML 1913201-XAdES01903v141.xsd "
            "(clausola C.2) come xades:XAdESTimeStampType e la marca temporale che contiene deve marcare "
            "ds:SignatureValue, tutte le property SignatureTimeStamp presenti, CompleteCertificateRefsV2, "
            "CompleteRevocationRefs e, quando presenti, AttributeCertificateRefsV2 e AttributeRevocationRefs."
        ),
        "testo_integrale": (
            """Semantics: The SigAndRefsTimeStampV2 qualifying property shall be an unsigned qualifying property qualifying the signature.

The SigAndRefsTimeStampV2 qualifying property shall encapsulate electronic time-stamps on the digital signature value, the signature time-stamp, if present, and the XAdES qualifying properties containing references to validation data.

Syntax: The SigAndRefsTimeStampV2 qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v141.xsd", whose location is detailed in clause C.2, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.4.1#"

The preamble of the XML Schema file also includes the following namespace declaration:
  xmlns:xades="http://uri.etsi.org/01903/v1.3.2#",
which assigns the prefix "xades" to the namespace whose URI is shown in the declaration.
-->

<xsd:element name="SigAndRefsTimeStampV2" type="xades:XAdESTimeStampType"/>

This qualifying property shall contain an electronic time-stamp that time-stamps the following XAdES components: ds:SignatureValue element, all present SignatureTimeStamp qualifying properties, CompleteCertificateRefsV2, CompleteRevocationRefs, and when present, AttributeCertificateRefsV2 and AttributeRevocationRefs.

Depending whether all the aforementioned time-stamped unsigned qualifying properties and the SigAndRefsTimeStampV2 qualifying property itself have the same parent or not, its contents may be different. Details are given in clauses below."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.5.1.2 (Not distributed case)",
        "testo": (
            "Quando SigAndRefsTimeStampV2 e tutte le property non firmate coperte dalla sua marca temporale "
            "hanno lo stesso genitore, la property deve usare il meccanismo implicito: l'input per il calcolo "
            "dell'impronta e' la concatenazione, nell'ordine, di ds:SignatureValue e delle property non firmate "
            "elencate che compaiono prima della SigAndRefsTimeStampV2 nell'ordine di comparizione dentro "
            "UnsignedSignatureProperties, ciascuna canonicalizzata come specificato nella clausola 4.5."
        ),
        "testo_integrale": (
            """If SigAndRefsTimeStampV2 and all the unsigned qualifying properties covered by its electronic time-stamp have the same parent, this qualifying property shall use the implicit mechanism.

The input to the electronic time-stamp's message imprint computation input shall be the result of taking in order each of the XAdES components listed below, canonicalizing each one as specified in clause 4.5, and concatenating the resulting octet streams:

1) The ds:SignatureValue element.

2) Those among the following unsigned qualifying properties that appear before SigAndRefsTimeStampV2, in their order of appearance within the UnsignedSignatureProperties element:

- the SignatureTimeStamp qualifying properties;

- the CompleteCertificateRefsV2 qualifying property;

- the CompleteRevocationRefs qualifying property;

- the AttributeCertificateRefsV2 qualifying property if it is present; and

- the AttributeRevocationRefs qualifying property if it is present."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.5.1.3 (Distributed case)",
        "testo": (
            "Quando SigAndRefsTimeStampV2 e alcune delle property non firmate coperte dalla sua marca temporale "
            "non hanno lo stesso genitore, la property va costruita generando un elemento Include per ciascuna "
            "property non firmata da marcare (nessun Include per ds:SignatureValue, il cui contributo all'input "
            "del digest e' implicitamente assunto), con gli attributi URI costruiti secondo le regole della "
            "clausola 5.1.4.4.2.1; l'input per il calcolo dell'impronta si costruisce inizializzando un flusso "
            "di ottetti vuoto, inserendovi ds:SignatureValue con il suo contenuto canonicalizzato come "
            "specificato nella clausola 4.5 e poi, nell'ordine degli Include, ciascuna property elencata, "
            "ripulita dai nodi commento e canonicalizzata come specificato nella clausola 4.5."
        ),
        "testo_integrale": (
            """If SigAndRefsTimeStampV2 and some of the unsigned qualifying properties covered by its electronic time-stamp do not have the same parent, this qualifying property shall be built as indicated below:

1) no Include element will be added for ds:SignatureValue. It shall implicitly be assumed its contribution to the digest input (see below in this clause); and

2) generate one Include element for each unsigned qualifying property that shall be covered by the electronic time-stamp in the order they appear listed below:

- the SignatureTimeStamp qualifying properties;

- the CompleteCertificateRefsV2 qualifying property;

- the CompleteRevocationRefs qualifying property;

- the AttributeCertificateRefsV2 qualifying property if it is present; and

- the AttributeRevocationRefs qualifying property if it is present.

The URI attributes shall be built following the rules stated in clause 5.1.4.4.2.1.

The electronic time-stamp's message imprint computation input shall be built as indicated below:

1) initialize the final octet stream as an empty octet stream;

2) take the ds:SignatureValue element and its content. Canonicalize it as specified in clause 4.5, and put the result in the final octet stream; and

3) take each unsigned qualifying property listed above in the order they have been listed above (this order shall be the same as the order the Include elements appear in the property). For each one extract comment nodes, canonicalize it as specified in clause 4.5, and concatenate the resulting octet string to the final octet stream."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.5.2.1 (Semantics and syntax)",
        "testo": (
            "La RefsOnlyTimeStampV2 deve essere una qualifying property non firmata che qualifica la firma e "
            "deve incapsulare marche temporali elettroniche sulle qualifying property XAdES che contengono "
            "riferimenti ai dati di convalida; l'elemento e' definito dal file di schema XML "
            "1913201-XAdES01903v141.xsd (clausola C.2) come xades:XAdESTimeStampType e la marca temporale che "
            "contiene deve marcare CompleteCertificateRefsV2, CompleteRevocationRefs e, quando presenti, "
            "AttributeCertificateRefsV2 e AttributeRevocationRefs."
        ),
        "testo_integrale": (
            """Semantics: The RefsOnlyTimeStampV2 qualifying property shall be an unsigned qualifying property qualifying the signature.

The RefsOnlyTimeStampV2 qualifying property shall encapsulate electronic time-stamps on the XAdES qualifying properties containing references to validation data.

Syntax: The RefsOnlyTimeStampV2 qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v141.xsd", whose location is detailed in clause C.2, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.4.1#"

The preamble of the XML Schema file also includes the following namespace declaration:
  xmlns:xades="http://uri.etsi.org/01903/v1.3.2#",
which assigns the prefix "xades" to the namespace whose URI is shown in the declaration.
-->

<xsd:element name="RefsOnlyTimeStampV2" type="xades:XAdESTimeStampType"/>

This qualifying property shall contain an electronic time-stamp that time-stamps the following XAdES qualifying properties: CompleteCertificateRefsV2, CompleteRevocationRefs, and when present, AttributeCertificateRefsV2 and AttributeRevocationRefs.

Depending whether all the aforementioned time-stamped unsigned qualifying properties and the RefsOnlyTimeStampV2 qualifying property itself have the same parent or not, its contents may be different. Details are given in clauses below."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.5.2.2 (Not distributed case)",
        "testo": (
            "Quando RefsOnlyTimeStampV2 e tutte le property non firmate coperte dalla sua marca temporale hanno "
            "lo stesso genitore, la property deve usare il meccanismo implicito: l'input per il calcolo "
            "dell'impronta e' la concatenazione, nell'ordine, delle property non firmate elencate che compaiono "
            "prima della RefsOnlyTimeStampV2 nell'ordine di comparizione dentro UnsignedSignatureProperties, "
            "ciascuna canonicalizzata come specificato nella clausola 4.5."
        ),
        "testo_integrale": (
            """If RefsOnlyTimeStampV2 and all the unsigned qualifying properties covered by its electronic time-stamp have the same parent, this qualifying property shall use the implicit mechanism. The electronic time-stamp's message imprint computation input shall be the result of taking those of the qualifying unsigned properties listed below that appear before the RefsOnlyTimeStampV2 in their order of appearance within the UnsignedSignatureProperties element, canonicalizing each one as specified in clause 4.5, and concatenating the resulting octet streams:

• the CompleteCertificateRefsV2 qualifying property;

• the CompleteRevocationRefs qualifying property;

• the AttributeCertificateRefsV2 qualifying property if it is present; and

• the AttributeRevocationRefs qualifying property if it is present."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.1.5.2.3 (Distributed case)",
        "testo": (
            "Quando RefsOnlyTimeStampV2 e alcune delle property non firmate coperte dalla sua marca temporale "
            "non hanno lo stesso genitore, va generato un elemento Include per ciascuna property non firmata da "
            "marcare, nell'ordine elencato, con gli attributi URI costruiti secondo le regole della clausola "
            "5.1.4.4.2.1; l'input per il calcolo dell'impronta si costruisce inizializzando un flusso di ottetti "
            "vuoto e inserendovi poi, nell'ordine degli Include, ciascuna property elencata, ripulita dai nodi "
            "commento e canonicalizzata come specificato nella clausola 4.5."
        ),
        "testo_integrale": (
            """If RefsOnlyTimeStampV2 and some of the unsigned qualifying properties covered by its electronic time-stamp do not have the same parent, one Include element shall be generated for each unsigned qualifying property that shall be time-stamped by the electronic time-stamp in the order they appear listed below:

• the CompleteCertificateRefsV2 qualifying property;

• the CompleteRevocationRefs qualifying property;

• the AttributeCertificateRefsV2 qualifying property if it is present; and

• the AttributeRevocationRefs qualifying property if it is present.

The URI attributes shall be built following the rules stated in clause 5.1.4.4.2.1.

The electronic time-stamp's message imprint computation input shall be built as indicated below:

1) initialize the final octet stream as an empty octet stream; and

2) take each unsigned qualifying property listed above in the order they have been listed above (this order shall be the same as the order the Include elements appear in the qualifying property). For each one extract comment nodes, canonicalize it as specified in clause 4.5, and concatenate the resulting octet stream to the final octet stream."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.2.1 (Usage of deprecated qualifying properties)",
        "testo": (
            "La clausola A.2 elenca le property deprecate: sono mantenute nel documento per agevolare il "
            "trattamento delle firme XAdES conformi ai requisiti della versione 1.1.1 di ETSI EN 319 132-1 "
            "[i.19], ma non devono essere aggiunte ad alcuna nuova firma XAdES."
        ),
        "testo_integrale": (
            "Clause A.2 lists deprecated qualified properties. They are kept in the document to facilitate the "
            "handling of XAdES signatures that meet the requirements of version 1.1.1 of ETSI EN 319 132-1 "
            "[i.19], but they shall not be added to any new XAdES signature."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex A, clausola A.2.2 (The RenewedDigests qualifying property)",
        "testo": (
            "La property RenewedDigests, definita nella clausola 5.5.3 di ETSI EN 319 132-1 (V1.1.1) [i.19], e' "
            "deprecata: al suo posto deve essere usata la property RenewedDigestsV2 definita nella clausola "
            "5.5.3 del presente documento."
        ),
        "testo_integrale": (
            "The RenewedDigests qualifying property as defined in clause 5.5.3 of ETSI EN 319 132-1 (V1.1.1) "
            "[i.19] is deprecated. Instead, the RenewedDigestsV2 qualifying property as defined in clause 5.5.3 "
            "of the present document, shall be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex B (Alternative mechanisms for long term availability and integrity of validation data)",
        "testo": (
            "Oltre a quelli descritti nella clausola 5.5, possono esistere meccanismi diversi per garantire la "
            "disponibilita' e l'integrita' a lungo termine dei dati di convalida; se un tale meccanismo viene "
            "incorporato nella firma mediante una property non firmata, per esso devono essere specificati la "
            "semantica e la sintassi della property (nome e namespace inclusi), la strategia con cui il "
            "meccanismo garantisce che tutte le parti necessarie della firma siano protette da quella property, "
            "la strategia di trattamento delle firme che contengono property definite nel presente documento "
            "(senza invalidare le marche temporali gia' incorporate e incorporando e proteggendo tutto il "
            "materiale di convalida necessario) e la strategia di trattamento delle firme XAdES legacy (senza "
            "invalidare le property per la disponibilita' e integrita' a lungo termine gia' incorporate)."
        ),
        "testo_integrale": (
            """There may be mechanisms to achieve long term availability and integrity of validation data different from the ones described in clause 5.5.

If such a mechanism is incorporated into the signature using an unsigned property, then for this mechanism shall be specified:

1) The clear specification of the semantics and syntax of the property including its name, and namespace.

2) The strategy of how this mechanism guarantees that all necessary parts of the signature are protected by this property.

3) The strategy of how to handle signatures containing properties defined in the present document. In particular, in case ArchiveTimeStamp unsigned properties defined in the namespace whose URI is http://uri.etsi.org/01903/v1.4.1# are already incorporated into the signature, it shall be ensured that the previous electronic time-stamps within these properties are not invalidated, and that all validation material needed to validate the signature before the incorporation of the new property is incorporated into the signature and protected by the new property.

4) The strategy of how to handle legacy XAdES signatures. In particular it shall be guaranteed that in case of previously incorporated properties for long term availability and integrity of validation data they are not invalidated.

NOTE 1: Such mechanisms, defined outside of the present document, can be used to provide long term availability and integrity of validation data. However, they do not represent XAdES-B-LTA level as defined in clause 6 or XAdES-E-A levels as defined in ETSI EN 319 132-2 [i.17].

NOTE 2: Such mechanisms might be included in future versions of the present document and assigned to a corresponding XAdES level."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "Annex C, clausola C.1 (XML Schema file location for namespace http://uri.etsi.org/01903/v1.3.2#)",
        "testo": (
            "Individua il file di schema XML che contiene le definizioni delle qualifying property del "
            "namespace il cui URI e' http://uri.etsi.org/01903/v1.3.2#: il file 1913201-XAdES01903v132.xsd, "
            "all'indirizzo https://forge.etsi.org/rep/esi/x19_13201_XAdES/raw/v1.3.1/1913201-XAdES01903v132.xsd. "
            "Il contenuto di questo file e' identico a quello del file di schema XML che definisce tipi ed "
            "elementi nello stesso namespace in ETSI EN 319 132-1 (V1.2.1) [i.20]. Disposizione dichiarativa di "
            "riferimento normativo: non impone alcun comportamento."
        ),
        "testo_integrale": (
            """The file at https://forge.etsi.org/rep/esi/x19_13201_XAdES/raw/v1.3.1/1913201-XAdES01903v132.xsd (1913201-XAdES01903v132.xsd) contains the definitions of qualifying properties defined within the namespace whose URI value is http://uri.etsi.org/01903/v1.3.2#.

NOTE: The content of this XML Schema file is identical to the content of the XML Schema file defining types and elements in the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#, in ETSI EN 319 132-1 (V1.2.1) [i.20]."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex C, clausola C.2 (XML Schema file location for namespace http://uri.etsi.org/01903/v1.4.1#)",
        "testo": (
            "Individua il file di schema XML che contiene le definizioni delle qualifying property del "
            "namespace il cui URI e' http://uri.etsi.org/01903/v1.4.1#: il file 1913201-XAdES01903v141.xsd, "
            "all'indirizzo https://forge.etsi.org/rep/esi/x19_13201_XAdES/raw/v1.3.1/1913201-XAdES01903v141.xsd. "
            "Il contenuto di questo file e' diverso da quello del file di schema XML che definisce tipi ed "
            "elementi nello stesso namespace in ETSI EN 319 132-1 (V1.2.1) [i.20]. Disposizione dichiarativa di "
            "riferimento normativo: non impone alcun comportamento."
        ),
        "testo_integrale": (
            """The file at https://forge.etsi.org/rep/esi/x19_13201_XAdES/raw/v1.3.1/1913201-XAdES01903v141.xsd (1913201-XAdES01903v141.xsd) contains the definitions of qualifying properties defined within the namespace whose URI value is http://uri.etsi.org/01903/v1.4.1#.

NOTE: The content of this XML Schema file is different from the content of the XML Schema file defining types and elements in the namespace whose URI is http://uri.etsi.org/01903/v1.4.1#, in ETSI EN 319 132-1 (V1.2.1) [i.20]."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

# UNA riga per unita' numerata: il riferimento del nodo e' anche il suo item di indice.
INDICE_ARTICOLI_LOCALE: list[str] = [
    "Annex A, clausola A.1.1 (The CompleteCertificateRefsV2 qualifying property)",
    "Annex A, clausola A.1.1, requisito 1)",
    "Annex A, clausola A.1.1, requisito 2)",
    "Annex A, clausola A.1.1, requisito 3)",
    "Annex A, clausola A.1.1, requisito 4)",
    "Annex A, clausola A.1.1, requisito 5)",
    "Annex A, clausola A.1.2 (The CompleteRevocationRefs qualifying property)",
    "Annex A, clausola A.1.2, requisito 1)",
    "Annex A, clausola A.1.2, requisito 2)",
    "Annex A, clausola A.1.2, requisito 3)",
    "Annex A, clausola A.1.2, requisito 4)",
    "Annex A, clausola A.1.2, requisito 5)",
    "Annex A, clausola A.1.3 (The AttributeCertificateRefsV2 qualifying property)",
    "Annex A, clausola A.1.3, requisito 1)",
    "Annex A, clausola A.1.3, requisito 2)",
    "Annex A, clausola A.1.3, requisito 3)",
    "Annex A, clausola A.1.4 (The AttributeRevocationRefs qualifying property)",
    "Annex A, clausola A.1.4, requisito 1)",
    "Annex A, clausola A.1.4, requisito 2)",
    "Annex A, clausola A.1.4, requisito 3)",
    "Annex A, clausola A.1.5.1.1 (Semantics and syntax)",
    "Annex A, clausola A.1.5.1.2 (Not distributed case)",
    "Annex A, clausola A.1.5.1.3 (Distributed case)",
    "Annex A, clausola A.1.5.2.1 (Semantics and syntax)",
    "Annex A, clausola A.1.5.2.2 (Not distributed case)",
    "Annex A, clausola A.1.5.2.3 (Distributed case)",
    "Annex A, clausola A.2.1 (Usage of deprecated qualifying properties)",
    "Annex A, clausola A.2.2 (The RenewedDigests qualifying property)",
    "Annex B (Alternative mechanisms for long term availability and integrity of validation data)",
    "Annex C, clausola C.1 (XML Schema file location for namespace http://uri.etsi.org/01903/v1.3.2#)",
    "Annex C, clausola C.2 (XML Schema file location for namespace http://uri.etsi.org/01903/v1.4.1#)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# 33 relazioni, tutte fra righe di questo modulo (vedi docstring, "Relazioni
# dichiarate"). Nessuna relazione verso altri capitoli di questa fonte ne' verso
# altre fonti: partizioni e collegamenti cross-fonte li costruisce la sessione
# principale in fase 6 (ADR-0009, ADR-0012).
RELAZIONI: list[dict] = [
    # Gerarchia di scomposizione: riga della sottoclausta -> righe dei requisiti
    # numerati (inferred: il marcatore "requisito N)" non e' noto a partizioni_di).
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.1 (The CompleteCertificateRefsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.1, requisito 1)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.1 (The CompleteCertificateRefsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.1, requisito 2)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.1 (The CompleteCertificateRefsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.1, requisito 3)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.1 (The CompleteCertificateRefsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.1, requisito 4)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.1 (The CompleteCertificateRefsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.1, requisito 5)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.2 (The CompleteRevocationRefs qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.2, requisito 1)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.2 (The CompleteRevocationRefs qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.2, requisito 2)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.2 (The CompleteRevocationRefs qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.2, requisito 3)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.2 (The CompleteRevocationRefs qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.2, requisito 4)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.2 (The CompleteRevocationRefs qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.2, requisito 5)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.3 (The AttributeCertificateRefsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.3, requisito 1)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.3 (The AttributeCertificateRefsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.3, requisito 2)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.3 (The AttributeCertificateRefsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.3, requisito 3)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.4 (The AttributeRevocationRefs qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.4, requisito 1)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.4 (The AttributeRevocationRefs qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.4, requisito 2)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.4 (The AttributeRevocationRefs qualifying property)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.4, requisito 3)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    # Rinvii numerici interni a una sottoclausta: la voce e' citata per numero nudo
    # ("references in 1) and 3)", "referenced in references from 1), 2) and 3)").
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.1, requisito 4)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.1, requisito 1)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.1, requisito 4)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.1, requisito 3)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.2, requisito 4)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.2, requisito 1)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.2, requisito 4)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.2, requisito 2)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.2, requisito 4)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.2, requisito 3)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # Rinvii nominati dal testo delle NOTE annotatrici.
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.1, requisito 5)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.3 (The AttributeCertificateRefsV2 qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.2, requisito 5)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.4 (The AttributeRevocationRefs qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # Rinvii alla posizione dei file di schema XML (Annex C, Principi di questo modulo).
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.1 (The CompleteCertificateRefsV2 qualifying property)"),
        "nodo_a": ("principio", None, "Annex C, clausola C.2 (XML Schema file location for namespace http://uri.etsi.org/01903/v1.4.1#)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.2 (The CompleteRevocationRefs qualifying property)"),
        "nodo_a": ("principio", None, "Annex C, clausola C.1 (XML Schema file location for namespace http://uri.etsi.org/01903/v1.3.2#)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.3 (The AttributeCertificateRefsV2 qualifying property)"),
        "nodo_a": ("principio", None, "Annex C, clausola C.2 (XML Schema file location for namespace http://uri.etsi.org/01903/v1.4.1#)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.4 (The AttributeRevocationRefs qualifying property)"),
        "nodo_a": ("principio", None, "Annex C, clausola C.1 (XML Schema file location for namespace http://uri.etsi.org/01903/v1.3.2#)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.5.1.1 (Semantics and syntax)"),
        "nodo_a": ("principio", None, "Annex C, clausola C.2 (XML Schema file location for namespace http://uri.etsi.org/01903/v1.4.1#)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.5.2.1 (Semantics and syntax)"),
        "nodo_a": ("principio", None, "Annex C, clausola C.2 (XML Schema file location for namespace http://uri.etsi.org/01903/v1.4.1#)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # Rinvio letterale ma senza numero di clausola ("Details are given in clauses
    # below"): destinazione esplicita (le due sottoclausole che seguono), traccia
    # non verificabile meccanicamente.
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.5.1.1 (Semantics and syntax)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.5.1.2 (Not distributed case)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.5.1.1 (Semantics and syntax)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.5.1.3 (Distributed case)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.5.2.1 (Semantics and syntax)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.5.2.2 (Not distributed case)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.5.2.1 (Semantics and syntax)"),
        "nodo_a": ("obbligo", None, "Annex A, clausola A.1.5.2.3 (Distributed case)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
]
