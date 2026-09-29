"""ETSI EN 319 132-1 V1.3.1 (2024-07) - Electronic Signatures and Trust
Infrastructures (ESI); XAdES digital signatures; Part 1: Building blocks and
XAdES baseline signatures. Blocco B (famiglia AdES del lotto 2). Capitolo 7
dello split: clausola 6 (XAdES baseline signatures) - 6.1 (Signature levels),
6.2.1 (Algorithm requirements), 6.2.2 (Notation for requirements), 6.3
(Requirements on XAdES signature's elements, qualifying properties and
services, con la Tabella 2 e i requisiti addizionali a)-cc)) e 6.4 (Legacy
XAdES baseline signatures). Conteggio di questo capitolo: 32 Obblighi, 2
Principi, 34 item di indice, 29 relazioni interne (tutte dalla riga 6.3 ai
singoli requisiti addizionali della Tabella 2). Questo modulo e' puro dato:
non importa nulla, non legge file e NON tocca app/seed.py - la numerazione
degli id e' risolta per riferimento dalla sessione principale tramite
app/seed_data/lib.py, e le relazioni verso altri capitoli di questa fonte o
verso altre fonti le costruisce sempre la sessione principale (fase 6,
ADR-0009).

Provenienza del testo: app/.source_cache/etsi_319_132/cap07.txt, porzione
dello split deterministico descritto in
app/.source_cache/etsi_319_132/manifest.json (capitolo "cap07", titolo "6 -
XAdES baseline signatures") del testo ufficiale completo in
app/.source_cache/etsi_319_132/raw.txt, raw_body.txt e raw.pdf. Da
app/.source_cache/etsi_319_132/provenance.json: URL ufficiale
https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf,
versione ETSI "01.03.01_60" (EN 319 132-1 V1.3.1, 2024-07), data_fetch
2026-09-29T12:56:34Z, sha256 del PDF grezzo
83fc87ee09de90274131a1f60cb73edb742cebc7cd8961342586ed06133664c5, formato "PDF
ETSI deliver (pdftotext -layout)" (tutti i valori dal provenance.json della
fonte).

## Perimetro

Clausola 6 completa, dal titolo "6 XAdES baseline signatures" fino alla
clausola 6.4 inclusa: il capitolo successivo dello split (cap08) apre l'Annex
A (normative). Il file assegnato non contiene front matter, Contents,
Foreword, History ne' l'elenco dei riferimenti bibliografici (clausola 2 e
"References" finali): comincia con il titolo della clausola 6 e termina con la
clausola 6.4.

## Granularita' voce per voce (ADR-0007)

34 item di indice = 34 righe:

- le 4 sottoclausole numerate con contenuto proprio (6.1, 6.2.1, 6.2.2, 6.3) e
  la clausola 6.4, una riga ciascuna;
- i 29 requisiti addizionali della Tabella 2, etichettati dal documento con le
  lettere a)-cc): un id = una riga, come da precedente fissato per i venti
  requisiti a)-t) della clausola 6.3 di ETSI EN 319 122-1 (cap04 di quella
  fonte). Le lettere NON sono elenco di dettaglio interno a un requisito: sono
  i requisiti stessi, numerati dal documento e usati come indice dalla colonna
  "Additional requirements and notes" della Tabella 2 (clausola 6.2.2, punto
  8: "This cell contains numbers referencing notes and/or letters referencing
  additional requirements on the qualifying property or the other signature's
  element. Both notes and additional requirements are listed below the
  table."). Ciascuna lettera nomina l'elemento o il servizio a cui si
  riferisce e ha un verbo deontico proprio ("shall include", "should be
  avoided", "may be used"), quindi e' un'unita' di prescrizione autonoma.

Intestazioni di puro raggruppamento, senza testo proprio, NON generano nodo
ne' item di indice (verificato sul testo: sono seguite immediatamente dalla
prima sottoclausta, senza una riga propria da assorbire): "6 XAdES baseline
signatures" (titolo del capitolo), "6.2 General requirements" (seguito da
6.2.1) e la rubrica "Additional requirements:" (etichetta del blocco i cui
item sono i nodi a)-cc)). Stesso criterio delle intestazioni di raggruppamento
delle altre fonti ETSI censite (ETSI EN 319 122-1 clausola 6.2, ETSI EN 319
132-1 cap03 clausole 4/4.3/4.4).

Le righe della Tabella 2 NON sono item di indice a se': non hanno un id
proprio (la loro identita' e' il nome dell'elemento, della qualifying property
o del servizio) e il loro contenuto prescrittivo per livello e' indicizzato
dal documento attraverso le lettere dei requisiti addizionali. La tabella
resta quindi contenuto del nodo della clausola 6.3, come da criterio gia'
applicato alla Tabella 1 di ETSI EN 319 122-1 clausola 6.3 (cap04 di quella
fonte). Alternativa scartata: un unico nodo per l'intera clausola 6.3
(paragrafo introduttivo + NOTE 1-10 + Tabella 2 + lettere a)-cc)). Avrebbe
reso non rintracciabili singolarmente 29 prescrizioni che il documento numera
e che la tabella cita una per una, e avrebbe prodotto un nodo di quasi 20 KB
di testo con prescrizioni di tipo diverso (algoritmi di canonicalizzazione, attributi
di marca temporale, materiale di convalida, dati di revoca, digest rinnovati).

Le note della clausola 6.3: le NOTE 1 e 2 (premessa e carattere del livello
B-B) e le NOTE 3-10 (apparato della Tabella 2: certificati, canonicalizzazione
"with comments", SigningCertificateV2, DataObjectFormat, servizio di
incorporazione dei dati di convalida, marche temporali) sono mantenute per
intero nel nodo della clausola 6.3, benche' il testo ufficiale collochi le
NOTE 3-10 dopo i requisiti addizionali a)-cc): il nodo 6.3 riporta percio' la
rubrica "Additional requirements:" (l'etichetta del blocco i cui item sono i
nodi a)-cc) di questo modulo) e subito dopo le NOTE 3-10, che annotano righe
della tabella e non singole lettere. Nessuna NOTA e' stata spostata o
duplicata in un nodo a)-cc).

Il paragrafo "Table 2 contains 8 columns. Below follows a detailed explanation
of their meanings and contents:" con i punti 1)-8) e i relativi sottopunti
(1a, 1b, 1c) e elenchi di valori ammessi NON produce righe separate: descrive
la notazione della tabella, non impone comportamenti autonomi (i "shall" che vi
compaiono definiscono il significato dei valori di notazione). Stesso criterio
della clausola 6.2.2 di ETSI EN 319 122-1 cap04. Lo stesso vale per gli elenchi
puntati dei valori ammessi nei requisiti d) e g) e per i quattro punti di aa):
sono il contenuto del requisito che li introduce, non requisiti a se'.

## Obbligo o Principio, riga per riga

- 6.1 (Signature levels) -> Principio "definitorio". Disposizione dichiarativa:
  definisce i quattro livelli XAdES baseline (B-B, B-T, B-LT, B-LTA) e la
  finalita' di ciascuno, senza imporre alcun comportamento a un soggetto; le
  NOTE 1-4 (informative: ciclo di vita della firma, casi d'uso dei livelli c) e
  d), disponibilita'/integrita' a lungo termine, rapporto con altre tecniche di
  conservazione) restano nel nodo, come da convenzione gia' adottata per le
  NOTE informative interne a una clausola (ETSI EN 319 122-1 cap04 6.1).
- 6.2.1 (Algorithm requirements) -> Obbligo "tecnico/sicurezza". Contiene una
  raccomandazione ("should be as specified in ETSI TS 119 312 [i.14]") e un
  divieto secco ("MD5 algorithm shall not be used as digest algorithm"): la
  sottoclausta e' indivisibile ai fini dell'indice, quindi un solo nodo, con il
  verbo modale conservato nel `testo`. Le NOTE 1 e 2 (raccomandazioni nazionali
  che possono prevalere su ETSI TS 119 312; URI di sicurezza XML aggiuntivi di
  IETF RFC 6931) restano in `testo_integrale`: la prima ha contenuto
  interpretativo, la seconda e' mera informazione complementare.
- 6.2.2 (Notation for requirements) -> Principio "definitorio": definisce la
  notazione della Tabella 2 (le 8 colonne, i valori ammessi nelle colonne di
  presenza, i valori di cardinalita', il ruolo delle colonne "References" e
  "Additional notes and requirements") con un EXAMPLE di lettura. I "shall" che
  vi compaiono sono la definizione del significato dei valori di notazione, non
  prescrizioni autonome su un soggetto (i comportamenti stanno nelle righe
  della tabella e nei requisiti a)-cc), nodi separati).
- 6.3 (Requirements on XAdES signature's elements, qualifying properties and
  services) -> Obbligo "tecnico/sicurezza". La clausola impone che i quattro
  livelli siano costruiti come da clausola 4, che le qualifying property della
  clausola 5 siano incorporate solo con il meccanismo di incorporazione diretta
  della clausola 4.4 e che le qualifying property contenitore di marche
  temporali incapsulino solo marche IETF RFC 3161 aggiornate da IETF RFC 5816;
  la Tabella 2 fissa presenza e cardinalita' di ciascun elemento, qualifying
  property e servizio per i quattro livelli ("shall be present", "shall not be
  present", "may be present", "shall be provided", "conditioned presence", "*").
- 6.3, requisiti addizionali a)-cc) -> 29 Obblighi "tecnico/sicurezza". Ciascuna
  lettera nomina l'elemento o il servizio a cui si riferisce ("Requirement for
  ds:KeyInfo/X509Data", "Requirement for SignatureTimeStamp", "Requirement for
  service \"incorporation of validation data for electronic time-stamps\"", ...)
  e prescrive come costruire o aumentare la firma XAdES (inclusione del
  certificato di firma e del materiale di convalida, algoritmi di
  canonicalizzazione e trasformazioni ammessi, riferimenti ai certificati,
  DataObjectFormat per oggetto firmato, incorporazione condizionata di
  SignaturePolicyStore/CertificateValues/AttrAuthoritiesCertValues/
  AttributeCertificateRefsV2/AttributeRevocationValues/RevocationValues/
  AnyValidationData, marche temporali di firma, ArchiveTimeStamp, digest
  rinnovati).
- 6.4 (Legacy XAdES baseline signatures) -> Obbligo "tecnico/sicurezza" con
  `condizione_applicabilita`: si applica quando nuove qualifying property non
  firmate vengono incorporate in firme XAdES baseline legacy, che devono
  risultare conformi al presente documento.

Modulazione deontica: i requisiti il cui unico verbo modale e' "should" o "may"
(b), c), e), g), j), l) ha "shall" sulla cardinalita' ma nessun obbligo di
comportamento, p), q), t), u), v), y), z), cc), piu' la raccomandazione di
6.2.1) restano Obblighi, non Principi: il censimento non ha un tipo di obbligo
"raccomandazione" e nessuna delle categorie di `tipo_principio` descrive una
raccomandazione operativa rivolta a un soggetto o a un elemento identificabile;
la forza deontica resta nel campo `testo` ("dovrebbe"/"puo'") e in
`testo_integrale` resta il testo ufficiale. Precedenti in questo senso: ETSI EN
319 122-1 cap04 (i "should"/"may" restano nella riga Obbligo) ed ETSI EN 319
401. Precedente di segno opposto, non seguito qui: ETSI EN 319 411-1 cap04,
dove i "should" a livello di id di requisito generano Principi "altro".
DUBBIO DI CLASSIFICAZIONE APERTO per la revisione umana: b), c), e), g), j),
p), q), t), u), v), y), z), cc) sono i tredici requisiti in cui l'unico verbo
modale e' "should"/"may"; se la revisione preferisse la convenzione di ETSI EN
319 411-1 andrebbero riclassificati come Principi "altro" (la sostanza del
testo non cambia).

Soggetti: il testo nomina espressamente "the generator" / "generators" in a),
b), c), e), f), h), i): quelle righe portano "Utente/titolare" role
"obbligato" (chi genera o aumenta la firma: firmatario / applicazione di
creazione della firma), con la stessa convenzione con cui ETSI EN 319 132-1
cap04 mappa "the signer" e con cui ETSI EN 319 122-1 cap04 mappa "the
generator". I requisiti b) e c) nominano anche i "verifiers" come destinatari
dell'inclusione dei certificati -> aggiunta "Terza parte", ruolo "destinatario"
(convenzione gia' usata in ETSI EN 319 122-1 cap04 per i requisiti omologhi
della sua clausola 6.3). Tutte le altre righe restano senza `soggetti`,
compresa la riga della clausola 6.3: la clausola e la tabella prescrivono
sull'elemento o sulla qualifying property ("shall be present", "shall be
incorporated ... using only the direct incorporation mechanism") e non
nominano chi deve conformarsi. DUBBIO APERTO: ETSI EN 319 122-1 cap04 ha
assegnato "Utente/titolare"/"obbligato" anche alla riga della tabella (6.3) per
inferenza dai requisiti addizionali della stessa clausola; qui si e' preferita
la regola piu' stretta (soggetto solo se nominato nel testo della riga), gia'
adottata da ETSI EN 319 132-1 cap03/cap04, per non attribuire un ruolo che il
testo della riga non enuncia.

Nessun `oggetti_giuridici` valorizzato: il testo nomina firme XAdES, firme
baseline, elementi XML e marche temporali elettroniche generiche, mai uno degli
oggetti della tassonomia eIDAS (firma elettronica qualificata, sigillo
elettronico, marca temporale elettronica qualificata, ...): l'oggetto_giuridico
si dichiara solo se il testo lo nomina davvero, e "electronic time-stamp" senza
qualificazione non e' la marca temporale elettronica qualificata. Stesso
criterio di ETSI EN 319 132-1 cap04 e di ETSI EN 319 122-1 cap04.

`severita` e `sanzioni` assenti (standard tecnico, nessuna sanzione); `stato`
"vigente" su tutte le righe.

## Fedelta' dell'estrazione

- Tabella 2: `pdftotext -layout` spezza ogni record su piu' righe e disallinea
  le colonne (le celle lunghe traboccano nella colonna adiacente, le celle corte
  vanno a capo). Ricostruzione: una riga per record, colonne separate da " | ",
  zero celle riscritte o abbreviate. Riportati come nel testo ufficiale, senza
  correzioni: la cella della colonna "Additional requirements and notes" della
  riga RevocationValues, che nel documento si chiude con una virgola sospesa
  ("t, u, v,"); la cella della riga AnyValidationData senza spazi dopo le virgole
  ("q,u,v,cc"); la cella vuota (assenza di lettere o numeri) delle righe
  ds:Reference e CompleteRevocationRefs; la cella "References" vuota della riga
  "Service: Incorporation of validation data for electronic time-stamps". Le
  celle andate a capo sono state ricucite: "XMLDSIG [1]," + "clause 4.5.4";
  "a, b, c" + "3, 4, 5"; "B-B, B-T: 0 or 1" + "B-LT, B-LTA: 0"; "B-B: ≥ 0" +
  "B-T, B-LT, B-LTA: ≥ 1"; "x, y" + "9"; "z, aa"; l'elemento
  "DataObjectFormat's ObjectReference" + "attribute"; l'elemento
  "ArchiveTimeStamp (defined in namespace" + "whose URI is
  \"http://uri.etsi.org/01903/v1.4.1#\")"; "SPO: certificate and revocation
  values" + "embedded in the electronic time-stamp" + "itself". Il rientro di
  impaginazione delle righe di sotto-elemento (ds:Reference/ds:Transforms,
  DataObjectFormat/...) non e' riprodotto: e' artefatto di layout, non contenuto.
  Le intestazioni di colonna ripetute in testa a ogni pagina della tabella sono
  riportate una sola volta, in testa alla tabella.
- Testo dei requisiti a)-cc): ricucito riga per riga dalle righe spezzate; il
  solo trattino a fine riga del capitolo e' in o)
  ("signature-\ntime-stamp") ed e' un trattino proprio del composto
  "signature-time-stamp", non una sillabazione da sciogliere. In o) il periodo
  termina senza punto nel testo ufficiale ("... or has expired"): lasciato
  senza punto.
- Nella clausola 6.3 il testo ufficiale ha una parentesi non chiusa nel periodo
  di rinvio alla Tabella 2 ("... namely: XAdES-B-B, XAdES-B-T, XAdES-B-LT, and
  XAdES-B-LTA)."): refuso del documento, riportato come sta.
- Paratesto escluso: piede di pagina "ETSI", testatina "ETSI EN 319 132-1
  V1.3.1 (2024-07)", numeri di pagina 53-63, righe vuote di impaginazione.
- Le NOTE 1-4 di 6.1, le NOTE 1-2 di 6.2.1, la NOTE non numerata di 6.2.2 e le
  NOTE 3-10 di 6.3 sono mantenute integralmente in `testo_integrale`, ciascuna
  nel nodo della clausola a cui il testo ufficiale le colloca.

## Rinvii demandati alla fase 6 (nessuna relazione creata qui)

- Rinvii ad altre clausole del presente documento (capitoli coperti da altri
  moduli dello split): 6.2.2 -> "table 2", che vive nel nodo della clausola 6.3
  di questo stesso modulo (bersaglio-tabella, non un nodo di prescrizione ne'
  una partizione ex ADR-0012: nessun arco, la citazione e' verificabile nel
  `testo_integrale` di 6.2.2); 6.3 -> clausole 4, 4.4 e 5; 6.3 NOTE 8 -> clausola
  5.2.4; colonna "References" della Tabella 2 -> XMLDSIG [1] clausole 4.5.4,
  4.4.1, 4.4.3, 4.4.3.4 e clausole 5.2.1, 5.2.2, 5.2.3, 5.2.4, 5.2.5, 5.2.6,
  5.2.7.2, 5.2.8.1, 5.2.8.2, 5.2.9, 5.2.10, 5.3, 5.4.2, 5.4.3, 5.4.4, 5.4.5,
  5.4.6, 5.5.1, 5.5.2, 5.5.3, A.1.1, A.1.2, A.1.3, A.1.4, A.1.5.1, A.1.5.2;
  k) -> elemento SignedProperties (clausola 4.3.2); m) ->
  SignaturePolicyIdentifier/SigPolicyHash (clausola 5.2.9); p) -> clausola
  5.4.2; r) -> clausola 5.4.4; t) -> clausola 5.4.3; w) -> clausola 5.4.5; x)
  -> TimeStampValidationData (clausola 5.5.1) e AnyValidationData (clausola
  5.4.6); z) e aa) -> ArchiveTimeStamp (clausola 5.5.2); bb) -> RenewedDigestsV2
  (clausola 5.5.3); cc) -> AnyValidationData (clausola 5.4.6); 6.2.2 EXAMPLE ->
  CompleteCertificateRefsV2 (Annex A.1.1); 6.1 NOTE 4 -> Annex C.
- Rinvii interni al perimetro di questo modulo non modellati con un arco:
  f) cita "additional requirement d)" (entrambe le righe sono nodi di questo
  modulo, ma la citazione nomina la lettera e non il numero di clausola 6.3:
  un arco dichiarato "textual" verrebbe segnalato da
  app/tools/verifica_relazioni_textual.py, che cerca una traccia testuale del
  riferimento del bersaglio); e) cita "note 6", che non e' un nodo (vive dentro
  il `testo_integrale` della clausola 6.3). Entrambi sono rinvii recuperabili
  in un secondo momento senza toccare la copertura.
- Rinvii ad altre fonti (collegamento cross-fonte, ADR-0009): IETF RFC 6283
  [i.16], IETF RFC 4998 [i.15] ed ETSI TR 119 100 [i.11] (6.1 NOTE 1 e NOTE 4);
  ETSI TS 119 511 [i.13] (6.1 NOTE 4); ETSI TS 119 312 [i.14] (6.2.1);
  IETF RFC 6931 [i.8] e XMLDSIG [1] (6.2.1 NOTE 2 e 6.2.2); IETF RFC 3161 [7]
  e IETF RFC 5816 [16] (6.3); CD 2009/767/EC modificata da CD 2010/425/EU [i.5]
  (6.3 NOTE 4); ETSI TS 119 612 [i.12] (c)); W3C Canonical XML v1.1 [11],
  Exclusive Canonicalization [10] e Canonical XML v1.0 [9] (d) e f)); XMLDSIG
  [1] clausole 6.6.2-6.6.5 (g)); XML-Signature XPath Filter 2.0 [13] e [14]
  clausola 12.2.4.26 (g)).

## Relazioni dichiarate

Le 29 relazioni sono i rinvii interni della Tabella 2 ai requisiti addizionali
della stessa clausola, letti nella colonna "Additional requirements and notes"
(es. riga ds:KeyInfo/X509Data ... "a, b, c 3, 4, 5"; riga AnyValidationData ...
"q,u,v,cc"; riga ArchiveTimeStamp v1.4.1 ... "z, aa"). `nodo_da` = nodo della
clausola 6.3, `nodo_a` = singolo requisito addizionale, `tipo_relazione`
"richiama" (rinvio/citazione esplicita di un nodo verso un altro, CONTEXT.md),
`evidence_type` "textual" (la lettera compare letteralmente nel
`testo_integrale` del nodo citante, nella cella della tabella), `confidence`
None (nessuno score reale, ADR-0005). Una relazione per lettera: la dedup evita
archi multipli quando la stessa lettera compare in piu' righe della tabella (j
in tre righe, q in tre, s in due, v in tre, y in quattro, 10 in due). Tutte e
29 le lettere a)-cc) sono citate almeno una volta dalla tabella, quindi il
blocco ha 29 archi e nessuna lettera resta scollegata. Nessuna relazione verso
altri capitoli di questa fonte ne' verso altre fonti: le partizioni e i
collegamenti cross-fonte sono costruiti dalla sessione principale in fase 6
(ADR-0012, ADR-0009).

## Copertura

34 item di indice, 34 righe: 32 obblighi + 2 principi.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 6.2.1 (Algorithm requirements)",
        "testo": (
            "Gli algoritmi e le lunghezze di chiave usati per generare e per aumentare le firme "
            "digitali dovrebbero essere quelli specificati in ETSI TS 119 312 [i.14]; l'algoritmo MD5 "
            "non deve essere usato come algoritmo di digest."
        ),
        "testo_integrale": (
            """6.2.1 Algorithm requirements: The algorithms and key lengths used to generate and augment digital signatures should be as specified in ETSI TS 119 312 [i.14].

NOTE 1: Cryptographic suites recommendations defined in ETSI TS 119 312 [i.14] can be superseded by national recommendations.

NOTE 2: IETF RFC 6931 [i.8] defines a set of additional XML security URIs, which complement those ones defined in XMLDSIG [1].

In addition, MD5 algorithm shall not be used as digest algorithm."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)",
        "testo": (
            "I quattro livelli di firma XAdES del presente documento (XAdES-B-B, XAdES-B-T, "
            "XAdES-B-LT e XAdES-B-LTA) devono essere costruiti come specificato nella clausola 4 e le "
            "qualifying property XAdES della clausola 5 devono essere incorporate nella firma usando "
            "solo il meccanismo di incorporazione diretta della clausola 4.4 (restano quindi dentro un "
            "unico elemento QualifyingProperties, figlio di un solo elemento ds:Object, senza alcun "
            "QualifyingPropertiesReference); le qualifying property che fungono da contenitore di "
            "marche temporali elettroniche devono incapsulare solo marche IETF RFC 3161 aggiornate da "
            "IETF RFC 5816. La Tabella 2 fissa presenza e cardinalita' di ciascun elemento di firma, "
            "qualifying property e servizio elencato nella prima colonna per i quattro livelli "
            "(ciascuna riga rinvia alla clausola che definisce l'elemento e alle lettere dei requisiti "
            "addizionali che lo dettagliano); i requisiti addizionali a)-cc) sono riportati sotto la "
            "tabella e le NOTE 3-10 annotano singole righe della tabella."
        ),
        "testo_integrale": (
            """6.3 Requirements on XAdES signature's elements, qualifying properties and services: The four XAdES signature levels specified in the present clause shall be built as specified in clause 4. The XAdES qualifying properties specified in clause 5 shall be incorporated into the signature using only the direct incorporation mechanism specified in clause 4.4.

NOTE 1: This means that all the XAdES qualifying properties remain within one single QualifyingProperties element, which in turn is the child of one ds:Object element within the signature, and that in consequence, no QualifyingPropertiesReference element is present.

Table 2 shows the presence and cardinality requirements on the signature elements, qualifying properties, and services indicated in the first column for the four XAdES baseline signature levels, namely: XAdES-B-B, XAdES-B-T, XAdES-B-LT, and XAdES-B-LTA). Additional requirements are detailed below the table suitably labelled with the letter indicated in the last column.

NOTE 2: XAdES-B-B signatures that incorporate only the elements/qualifying properties that are mandatory in table 2, and that implement the mandatory requirements, contain the lowest number of elements/qualifying properties, with the consequent benefits for interoperability.

In XAdES baseline signatures the qualifying properties that act as electronic time-stamps containers shall encapsulate only IETF RFC 3161 [7] updated by IETF RFC 5816 [16] electronic time-stamps.

Table 2: Requirements for XAdES-B-B, XAdES-B-T, XAdES-B-LT, and XAdES-B-LTA signatures

Elements/Qualifying properties/Services | Presence in B-B level | Presence in B-T level | Presence in B-LT level | Presence in B-LTA level | Cardinality | References | Additional requirements and notes
ds:KeyInfo/X509Data | shall be present | shall be present | shall be present | shall be present | 1 | XMLDSIG [1], clause 4.5.4 | a, b, c 3, 4, 5
ds:SignedInfo/ds:CanonicalizationMethod | shall be present | shall be present | shall be present | shall be present | 1 | XMLDSIG [1], clause 4.4.1 | d, e 6
ds:Reference | shall be present | shall be present | shall be present | shall be present | ≥2 | XMLDSIG [1], clause 4.4.3 |
ds:Reference/ds:Transforms | may be present | may be present | may be present | may be present | 0 or 1 | XMLDSIG [1], clause 4.4.3.4 | f, g
SigningTime | shall be present | shall be present | shall be present | shall be present | 1 | Clause 5.2.1 | h
SigningCertificateV2 | shall be present | shall be present | shall be present | shall be present | 1 | Clause 5.2.2 | i, j 7
SigningCertificate | shall not be present | shall not be present | shall not be present | shall not be present | 0 | - |
DataObjectFormat | conditioned presence | conditioned presence | conditioned presence | conditioned presence | ≥0 | Clause 5.2.4 | k
DataObjectFormat/Description | may be present | may be present | may be present | may be present | 0 or 1 | Clause 5.2.4 | l 8
DataObjectFormat/ObjectIdentifier | may be present | may be present | may be present | may be present | 0 or 1 | Clause 5.2.4 | l
DataObjectFormat/MimeType | shall be present | shall be present | shall be present | shall be present | 1 | Clause 5.2.4 | l
DataObjectFormat/Encoding | may be present | may be present | may be present | may be present | 0 or 1 | Clause 5.2.4 | l
DataObjectFormat's ObjectReference attribute | shall be present | shall be present | shall be present | shall be present | 1 | Clause 5.2.4 | l
SignerRole | shall not be present | shall not be present | shall not be present | shall not be present | 0 | - |
SignerRoleV2 | may be present | may be present | may be present | may be present | 0 or 1 | Clause 5.2.6 |
CommitmentTypeIndication | may be present | may be present | may be present | may be present | ≥0 | Clause 5.2.3 |
SignatureProductionPlaceV2 | may be present | may be present | may be present | may be present | 0 or 1 | Clause 5.2.5 |
SignatureProductionPlace | shall not be present | shall not be present | shall not be present | shall not be present | 0 | - |
CounterSignature | may be present | may be present | may be present | may be present | ≥0 | Clause 5.2.7.2 |
AllDataObjectsTimeStamp | may be present | may be present | may be present | may be present | ≥0 | Clause 5.2.8.1 | 10
IndividualDataObjectsTimeStamp | may be present | may be present | may be present | may be present | ≥0 | Clause 5.2.8.2 | 10
SignaturePolicyIdentifier | may be present | may be present | may be present | may be present | 0 or 1 | Clause 5.2.9 |
SignaturePolicyStore | conditioned presence | conditioned presence | conditioned presence | conditioned presence | 0 or 1 | Clause 5.2.10 | m
SignatureTimeStamp | * | shall be present | shall be present | shall be present | B-B: ≥ 0 B-T, B-LT, B-LTA: ≥ 1 | Clause 5.3 | n, o 10
CertificateValues | * | * | conditioned presence | conditioned presence | 0 or 1 | Clause 5.4.2 | p, q
AnyValidationData | * | * | conditioned presence | conditioned presence | ≥0 | Clause 5.4.6 | q,u,v,cc
CompleteCertificateRefsV2 | * | * | shall not be present | shall not be present | B-B, B-T: 0 or 1 B-LT, B-LTA: 0 | Clause A.1.1 | j
CompleteCertificateRefs | shall not be present | shall not be present | shall not be present | shall not be present | 0 | - |
AttrAuthoritiesCertValues | * | * | conditioned presence | conditioned presence | 0 or 1 | Clause 5.4.4 | q, r
AttributeCertificateRefsV2 | * | * | shall not be present | shall not be present | B-B, B-T: 0 or 1 B-LT, B-LTA: 0 | Clause A.1.3 | j, s
AttributeCertificateRefs | shall not be present | shall not be present | shall not be present | shall not be present | 0 | - |
RevocationValues | * | * | conditioned presence | conditioned presence | 0 or 1 | Clause 5.4.3 | t, u, v,
CompleteRevocationRefs | * | * | shall not be present | shall not be present | B-B, B-T: 0 or 1 B-LT, B-LTA: 0 | Clause A.1.2 |
AttributeRevocationValues | * | * | conditioned presence | conditioned presence | 0 or 1 | Clause 5.4.5 | v, w
AttributeRevocationRefs | * | * | shall not be present | shall not be present | B-B, B-T: 0 or 1 B-LT, B-LTA: 0 | Clause A.1.4 | s
SigAndRefsTimeStampV2 | * | * | shall not be present | shall not be present | B-B, B-T: ≥ 0 B-LT, B-LTA: 0 | Clause A.1.5.1 |
SigAndRefsTimeStamp | shall not be present | shall not be present | shall not be present | shall not be present | 0 | - |
RefsOnlyTimeStampV2 | * | * | shall not be present | shall not be present | B-B, B-T: ≥ 0 B-LT, B-LTA: 0 | Clause A.1.5.2 |
RefsOnlyTimeStamp | shall not be present | shall not be present | shall not be present | shall not be present | 0 | - |
Service: Incorporation of validation data for electronic time-stamps | * | * | shall be provided | shall be provided | - | - | x, y 9
SPO: TimeStampValidationData | * | * | conditioned presence | conditioned presence | ≥0 | Clause 5.5.1 | y
SPO: certificate and revocation values embedded in the electronic time-stamp itself | * | * | conditioned presence | conditioned presence | ≥0 | - | y
SPO: AnyValidationData | * | * | conditioned presence | conditioned presence | ≥0 | Clause 5.4.6 | y
ArchiveTimeStamp (defined in namespace whose URI is "http://uri.etsi.org/01903/v1.4.1#") | * | * | * | shall be present | ≥1 | Clause 5.5.2 | z, aa
ArchiveTimeStamp (defined in namespace whose URI is "http://uri.etsi.org/01903/v1.3.2#") | shall not be present | shall not be present | shall not be present | shall not be present | 0 | - |
RenewedDigestsV2 | * | * | * | conditioned presence | ≥0 | Clause 5.5.3 | bb

Additional requirements:

NOTE 3: On ds:KeyInfo/X509Data/X509Certificate. A certificate is considered available to the verifier if reliable information about its location is known and allows automated retrieval of the certificate (for instance through an Authority Info Access Extension or equivalent information present in a TSL).

NOTE 4: On ds:KeyInfo/X509Data/X509Certificate. Requirement c) applies specifically but not exclusively to signing certificates that are EU qualified and supported by Trusted Lists as defined in CD 2009/767/EC amended by CD 2010/425/EU [i.5].

NOTE 5: On ds:KeyInfo/X509Data/X509Certificate. In the general case, different verifiers can have different trust parameters and can validate the signing certificate through different chains. Therefore, generators may not know which certificates will be relevant for path building. However, in practice, generators can often clearly identify such certificates. In this case, including them in the signature is a good practice, unless verifiers can automatically retrieve them.

NOTE 6: On ds:SignedInfo/CanonicalizationMethod. Support of canonicalization algorithms "with comments" is for residual interoperability in the signature validation process.

NOTE 7: On SigningCertificateV2. The presence of the signing certificate within ds:KeyInfo ensures a way to locate it (on the basis of digest equality with the value within SigningCertificateV2/CertDigest) within the signature.

NOTE 8: On DataObjectFormat. Clause 5.2.4 of the present document establishes that this signed property "qualifies one specific signed data object". This is done by forcing that ObjectReference attribute refers to a ds:Reference. However, the aforementioned clause does not mandate this ds:Reference to be a child of ds:SignedInfo; it actually could be a ds:Reference within a signed ds:Manifest, as the object referenced in this way is also a signed object.

NOTE 9: On service "incorporation of validation data for electronic time-stamps": the incorporation of the validation material of the electronic time-stamps ensures that the XAdES signature actually contains all the validation material needed.

NOTE 10: On SignatureTimeStamp, IndividualDataObjectsTimeStamp, AllDataObjectsTimeStamp: Several instances of these qualifying properties can be incorporated into the XAdES signature, coming from different TSAs."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale a)",
        "testo": (
            "Il generatore deve includere il certificato di firma come contenuto dell'elemento "
            "ds:KeyInfo/X509Data/X509Certificate."
        ),
        "testo_integrale": (
            "a) Requirement for ds:KeyInfo/X509Data. The generator shall include the signing certificate "
            "as content of ds:KeyInfo/X509Data/X509Certificate element."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale b)",
        "testo": (
            "Per facilitare la costruzione del percorso di certificazione, i generatori dovrebbero "
            "includere nello stesso elemento ds:KeyInfo/X509Data del requisito a) tutti i certificati "
            "non disponibili ai verificatori che possono essere usati durante la costruzione del "
            "percorso."
        ),
        "testo_integrale": (
            "b) Requirement for ds:KeyInfo/X509Data. In order to facilitate path-building, generators "
            "should include in the same ds:KeyInfo/X509Data element as in requirement a) all "
            "certificates not available to verifiers that can be used during path building."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale c)",
        "testo": (
            "Se la firma deve essere convalidata tramite una Trusted List come specificato in ETSI TS "
            "119 612 [i.12], il generatore dovrebbe includere tutti i certificati intermedi che formano "
            "una catena fra il certificato di firma e una CA presente nella Trusted List e che non sono "
            "disponibili ai verificatori."
        ),
        "testo_integrale": (
            "c) Requirement for ds:KeyInfo/X509Data. If the signature is to be validated through a "
            "Trusted List as specified in ETSI TS 119 612 [i.12], then the generator should include all "
            "intermediary certificates forming a chain between the signing certificate and a CA present "
            "in the Trusted List, which are not available to verifiers."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale d)",
        "testo": (
            "L'attributo Algorithm dell'elemento figlio ds:CanonicalizationMethod di ds:SignedInfo deve "
            "avere uno dei valori elencati dal requisito (\"http://www.w3.org/2006/12/xml-c14n11\", "
            "\"http://www.w3.org/2001/10/xml-exc-c14n#\", "
            "\"http://www.w3.org/TR/2001/REC-xml-c14n-20010315\" e le rispettive varianti "
            "\"#WithComments\"), e il corrispondente algoritmo di canonicalizzazione (Canonical XML v1.1, "
            "Exclusive Canonicalization o Canonical XML v1.0, con o senza commenti) deve essere "
            "supportato."
        ),
        "testo_integrale": (
            """d) Requirement for ds:SignedInfo/ds:CanonicalizationMethod element. The Algorithm attribute of ds:SignedInfo's ds:CanonicalizationMethod child element shall have one of the following values:

- "http://www.w3.org/2006/12/xml-c14n11". The corresponding canonicalization algorithm Canonical XML v1.1 (omits comments) [11] shall be supported.

- "http://www.w3.org/2001/10/xml-exc-c14n#". The corresponding canonicalization algorithm Exclusive Canonicalization (omits comments) [10] shall be supported.

- "http://www.w3.org/TR/2001/REC-xml-c14n-20010315". The corresponding canonicalization algorithm Canonical XML v1.0 (omits comments) [9] shall be supported.

- "http://www.w3.org/2006/12/xml-c14n11#WithComments". The corresponding canonicalization algorithm Canonical XML v1.1 (with comments) [11] shall be supported.

- "http://www.w3.org/2001/10/xml-exc-c14n#WithComments". The corresponding canonicalization algorithm Exclusive Canonicalization (with comments) [10] shall be supported. Or

- "http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments". The corresponding canonicalization algorithm Canonical XML v1.0 (with comments) [9] shall be supported."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale e)",
        "testo": (
            "Il generatore non dovrebbe usare algoritmi di canonicalizzazione \"with comments\" (v. "
            "NOTE 6)."
        ),
        "testo_integrale": (
            "e) Requirement for ds:SignedInfo/CanonicalizationMethod element. The generator should not "
            "use canonicalization algorithms \"with comments\". See note 6."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale f)",
        "testo": (
            "Se la trasformazione indicata dall'elemento figlio ds:Transform di "
            "ds:Reference/ds:Transforms e' una canonicalizzazione, il suo attributo Algorithm deve avere "
            "uno dei valori elencati nel requisito addizionale d) e il generatore non dovrebbe usare "
            "algoritmi di canonicalizzazione \"with comments\"."
        ),
        "testo_integrale": (
            "f) Requirement for ds:Reference/ds:Transforms element. If the transform indicated by a "
            "ds:Reference/ds:Transforms's ds:Transform child element is a canonicalization, its Algorithm "
            "attribute shall have one of the values listed in the present clause, additional requirement "
            "d) and the generator should not use canonicalization algorithms \"with comments\"."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale g)",
        "testo": (
            "Se la trasformazione indicata dall'elemento figlio ds:Transform di "
            "ds:Reference/ds:Transforms non e' una canonicalizzazione, il suo attributo Algorithm "
            "dovrebbe essere uno dei valori elencati dal requisito (Base 64, XPath, Enveloped Signature, "
            "XSLT, XML-Signature XPath Filter 2.0 e Relationships), per ciascuno dei quali la "
            "trasformazione corrispondente deve essere supportata."
        ),
        "testo_integrale": (
            """g) Requirement for ds:Reference/ds:Transforms element. If the transform indicated by a ds:Reference/ds:Transforms's ds:Transform child element is not a canonicalization, its Algorithm attribute should be one of the following values:

- "http://www.w3.org/2000/09/xmldsig#base64". The corresponding Base 64 transform, whose usage within XML signatures is specified in clause 6.6.2 of [1], shall be supported.

- "http://www.w3.org/TR/1999/REC-xpath-19991116". The corresponding XPath transform, whose usage within XML signatures is specified in clause 6.6.3 of [1], shall be supported.

- "http://www.w3.org/2000/09/xmldsig#enveloped-signature". The corresponding Enveloped Signature transform, whose usage within XML signatures is specified in clause 6.6.4 of [1], shall be supported.

- "http://www.w3.org/TR/1999/REC-xslt-19991116". The corresponding XSLT transform, whose usage within XML signatures is specified in clause 6.6.5 of [1], shall be supported.

- "http://www.w3.org/2002/06/xmldsig-filter2". The corresponding XML-Signature XPath Filter 2.0, which is specified in [13], shall be supported. Or

- "http://schemas.openxmlformats.org/package/2006/RelationshipTransform". The corresponding Relationships transform, which is specified in clause 12.2.4.26 of [14], shall be supported."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale h)",
        "testo": (
            "Il generatore deve includere come contenuto della qualifying property SigningTime l'ora UTC "
            "dichiarata al momento in cui la firma e' stata generata."
        ),
        "testo_integrale": (
            "h) Requirement for SigningTime. The generator shall include the claimed UTC time when the "
            "signature was generated as content of the SigningTime qualifying property."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale i)",
        "testo": (
            "Il generatore non deve generare l'attributo opzionale URI degli elementi figli Cert di "
            "SigningCertificateV2/Cert."
        ),
        "testo_integrale": (
            "i) Requirement for SigningCertificateV2/Cert. The generator shall not generate Cert "
            "children's URI optional attribute."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale j)",
        "testo": (
            "I riferimenti ai certificati (in SigningCertificateV2, CompleteCertificateRefsV2 e "
            "AttributeCertificateRefsV2) non dovrebbero includere l'elemento IssuerSerialV2."
        ),
        "testo_integrale": (
            "j) Requirement for SigningCertificateV2, CompleteCertificateRefsV2, and "
            "AttributeCertificateRefsV2. The references to certificates should not include the "
            "IssuerSerialV2 element."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale k)",
        "testo": (
            "Deve essere generato un DataObjectFormat per ciascun oggetto di dati firmato, tranne "
            "l'elemento SignedProperties e tranne il caso in cui la firma sia una firma baseline che "
            "controfirma un'altra firma: la firma baseline che controfirma un'altra firma e firma solo le "
            "proprie signed properties e la firma controfirmata non deve includere alcun attributo "
            "firmato DataObjectFormat; se invece firma anche altri oggetti di dati, deve includere un "
            "DataObjectFormat per ciascuno di questi ultimi."
        ),
        "testo_integrale": (
            "k) Requirement for DataObjectFormat. One DataObjectFormat shall be generated for each "
            "signed data object, except the SignedProperties element, and except if the signature is a "
            "baseline signature countersigning a signature. If the signature is a baseline signature "
            "countersigning another signature, and if it only signs its own signed properties and the "
            "countersigned signature, then it shall not include any DataObjectFormat signed property. If "
            "the signature is a baseline signature countersigning another signature and if it signs its "
            "own signed properties, the countersigned signature, and other data object(s), then it shall "
            "include one DataObjectFormat signed property for each of these other signed data object(s) "
            "aforementioned."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale l)",
        "testo": (
            "Il numero di occorrenze ammesso del componente XML interessato all'interno di un elemento "
            "DataObjectFormat deve essere quello indicato nella colonna \"Cardinality\" della Tabella 2."
        ),
        "testo_integrale": (
            "l) Requirement for XML components within DataObjectFormat. The number of occurrences allowed "
            "of the concerned XML component within one DataObjectFormat element, shall be as indicated in "
            "column \"Cardinality\"."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale m)",
        "testo": (
            "La qualifying property SignaturePolicyStore puo' essere incorporata nella firma XAdES solo "
            "se e' incorporato anche SignaturePolicyIdentifier e questo contiene l'elemento SigPolicyHash "
            "con il valore di digest del documento di signature policy; altrimenti SignaturePolicyStore "
            "non deve essere incorporata nella firma XAdES."
        ),
        "testo_integrale": (
            "m) Requirement for SignaturePolicyStore. This qualifying property may be incorporated into "
            "the XAdES signature only if the SignaturePolicyIdentifier is also incorporated and it "
            "contains the SigPolicyHash element with the digest value of the signature policy document. "
            "Otherwise the SignaturePolicyStore shall not be incorporated into the XAdES signature."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale n)",
        "testo": (
            "Ogni elemento SignatureTimeStamp deve contenere una sola marca temporale elettronica."
        ),
        "testo_integrale": (
            "n) Requirement for SignatureTimeStamp. Each SignatureTimeStamp element shall contain only "
            "one electronic time-stamp."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale o)",
        "testo": (
            "Le marche temporali elettroniche incapsulate negli attributi signature-time-stamp devono "
            "essere create prima che il certificato di firma sia stato revocato o sia scaduto."
        ),
        "testo_integrale": (
            "o) Requirement for SignatureTimeStamp. The electronic time-stamps encapsulated within the "
            "signature-time-stamp attributes shall be created before the signing certificate has been "
            "revoked or has expired"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale p)",
        "testo": (
            "Se viene generata una firma XAdES-B-LT o XAdES-B-LTA, l'incorporazione di CertificateValues "
            "puo' essere usata per incorporare i certificati elencati nella clausola 5.4.2."
        ),
        "testo_integrale": (
            "p) Requirement for incorporation of CertificateValues. If a XAdES-B-LT or a XAdES-B-LTA "
            "signature is generated, the incorporation of CertificateValues may be used for incorporating "
            "the certificates enumerated in clause 5.4.2."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale q)",
        "testo": (
            "La duplicazione di valori di certificato all'interno della firma (in CertificateValues, "
            "AttrAuthoritiesCertValues e AnyValidationData) dovrebbe essere evitata."
        ),
        "testo_integrale": (
            "q) Requirement for CertificateValues, AttrAuthoritiesCertValues, and AnyValidationData. "
            "Duplication of certificate values within the signature should be avoided."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale r)",
        "testo": (
            "La qualifying property AttrAuthoritiesCertValues puo' essere usata quando almeno un "
            "certificato di attributo o un'asserzione firmata e' incorporato in una firma XAdES-B-LT o "
            "XAdES-B-LTA, per incorporare i certificati elencati nella clausola 5.4.4; altrimenti non "
            "deve essere usata."
        ),
        "testo_integrale": (
            "r) Requirement for incorporation of AttrAuthoritiesCertValues. The AttrAuthoritiesCertValues "
            "qualifying property may be used when a at least an attribute certificate or a signed "
            "assertion is incorporated into a XAdES-B-LT or a XAdES-B-LTA signature for incorporating the "
            "certificates enumerated in clause 5.4.4. Otherwise, AttrAuthoritiesCertValues qualifying "
            "property shall not be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale s)",
        "testo": (
            "Le qualifying property AttributeCertificateRefsV2 e AttributeRevocationRefs possono essere "
            "usate quando almeno un certificato di attributo o un'asserzione firmata e' incorporato nella "
            "firma XAdES; altrimenti non devono essere usate."
        ),
        "testo_integrale": (
            "s) The AttributeCertificateRefsV2 and AttributeRevocationRefs qualifying properties may be "
            "used when a at least an attribute certificate or a signed assertion is incorporated into the "
            "XAdES signature. Otherwise, AttributeCertificateRefsV2 and AttributeRevocationRefs "
            "qualifying properties shall not be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale t)",
        "testo": (
            "Se viene generata una firma XAdES-B-LT o XAdES-B-LTA, l'incorporazione di RevocationValues "
            "puo' essere usata per incorporare i valori di stato dei certificati elencati nella clausola "
            "5.4.3."
        ),
        "testo_integrale": (
            "t) Requirement for incorporation of RevocationValues. If a XAdES-B-LT or a XAdES-B-LTA "
            "signature is generated, the incorporation of RevocationValues may be used for incorporating "
            "the certificate status values data enumerated in clause 5.4.3."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale u)",
        "testo": (
            "I valori di stato dei certificati dovrebbero essere inclusi nelle qualifying property "
            "RevocationValues o AnyValidationData, invece che nell'elemento ds:KeyInfo."
        ),
        "testo_integrale": (
            "u) Requirement for RevocationValues and AnyValidationData. Certificate status values should "
            "be included within RevocationValues or AnyValidationData qualifying properties instead "
            "within ds:KeyInfo element."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale v)",
        "testo": (
            "La duplicazione di valori di stato dei certificati all'interno della firma (in "
            "RevocationValues, AttributeRevocationValues e AnyValidationData) dovrebbe essere evitata."
        ),
        "testo_integrale": (
            "v) Requirement for RevocationValues, AttributeRevocationValues, and AnyValidationData. "
            "Duplication of certificate status values within the signature should be avoided."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale w)",
        "testo": (
            "La qualifying property AttributeRevocationValues puo' essere usata quando almeno un "
            "certificato di attributo o un'asserzione firmata e' incorporato in una firma XAdES-B-LT o "
            "XAdES-B-LTA, per incorporare i valori di stato dei certificati elencati nella clausola "
            "5.4.5; altrimenti non deve essere usata."
        ),
        "testo_integrale": (
            "w) Requirement for incorporation of AttributeRevocationValues. The AttributeRevocationValues "
            "qualifying property may be used when a at least an attribute certificate or a signed "
            "assertion is incorporated into a XAdES-B-LT or a XAdES-B-LTA signature for incorporating the "
            "certificate status values enumerated in clause 5.4.5. Otherwise, AttributeRevocationValues "
            "qualifying property shall not be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale x)",
        "testo": (
            "I dati di convalida delle marche temporali elettroniche devono essere presenti nella "
            "qualifying property TimeStampValidationData, o nella qualifying property AnyValidationData, "
            "o incapsulati nella stessa marca temporale elettronica."
        ),
        "testo_integrale": (
            "x) Requirement for service \"incorporation of validation data for electronic time-stamps\". "
            "The validation data for electronic time-stamps shall be present within the "
            "TimeStampValidationData qualifying property, or AnyValidationData qualifying property, or "
            "embedded in the electronic time-stamp itself."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale y)",
        "testo": (
            "I dati di convalida delle marche temporali elettroniche (il servizio e le sue tre opzioni) "
            "dovrebbero essere inclusi nella qualifying property TimeStampValidationData oppure nella "
            "qualifying property AnyValidationData."
        ),
        "testo_integrale": (
            "y) Requirement for service \"incorporation of validation data for electronic time-stamps\" "
            "and its three options. The validation data for electronic time-stamps should be included "
            "either in the TimeStampValidationData qualifying property, or the AnyValidationData "
            "qualifying property."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale z)",
        "testo": (
            "Ciascuna qualifying property ArchiveTimeStamp definita nel namespace il cui URI e' "
            "\"http://uri.etsi.org/01903/v1.4.1#\" puo' contenere piu' di una marca temporale "
            "elettronica emessa da TSA diverse."
        ),
        "testo_integrale": (
            "z) Requirement for ArchiveTimeStamp defined in the namespace whose URI is "
            "\"http://uri.etsi.org/01903/v1.4.1#\". Each ArchiveTimeStamp qualifying property defined in "
            "the namespace whose URI is http://uri.etsi.org/01903/v1.4.1# may contain more than one "
            "electronic time-stamp issued by different TSAs."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale aa)",
        "testo": (
            "Prima di generare e incorporare una nuova qualifying property ArchiveTimeStamp definita nel "
            "namespace il cui URI e' \"http://uri.etsi.org/01903/v1.4.1#\" deve essere incluso tutto il "
            "materiale di convalida necessario a convalidare i dati firmati nella firma XAdES, cioe' "
            "tutti i certificati e tutte le informazioni sullo stato dei certificati (come CRL o risposte "
            "OCSP) necessari per convalidare il certificato di firma, il certificato di firma di ogni "
            "controfirma incorporata nella firma, ogni certificato di attributo o asserzione firmata "
            "presente nella firma e il certificato di firma di ogni marca temporale elettronica "
            "precedente gia' incorporata nella firma in una qualifying property contenitore di marche "
            "temporali XAdES (comprese le ArchiveTimeStamp nello stesso namespace)."
        ),
        "testo_integrale": (
            """aa) Requirement for ArchiveTimeStamp defined in the namespace whose URI is "http://uri.etsi.org/01903/v1.4.1#". Before generating and incorporating a new ArchiveTimeStamp qualifying property defined in the namespace whose URI is "http://uri.etsi.org/01903/v1.4.1#", all the validation material required for validating the signed data in the XAdES signature shall be included. This validation material shall include all the certificates and all certificate status information (like CRLs or OCSP responses) required for:

- validating the signing certificate;

- validating the signing certificate of any countersignature incorporated into the signature;

- validating any attribute certificate or signed assertion present in the signature; and

- validating the signing certificate of any previous electronic time-stamp already incorporated into the signature within any XAdES electronic time-stamp container qualifying property (including any ArchiveTimeStamp defined in the namespace whose URI is "http://uri.etsi.org/01903/v1.4.1#")."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale bb)",
        "testo": (
            "Se la firma XAdES firma oggetti di dati esterni tramite un ds:Manifest firmato e si sospetta "
            "che alcuni degli algoritmi di digest usati per calcolare alcuni dei valori di digest in quel "
            "ds:Manifest diventino deboli al punto da rappresentare una minaccia, dovrebbe essere usato "
            "l'elemento RenewedDigest per contrastare tale minaccia."
        ),
        "testo_integrale": (
            "bb) Requirement for RenewedDigestsV2. If the XAdES signature signs external data objects "
            "through a signed ds:Manifest, and some of the digest algorithms used for computing some of "
            "the digest values within the aforementioned ds:Manifest is suspected to become weak enough "
            "as to represent a threat, the RenewedDigest element should be used to counter this threat."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale cc)",
        "testo": (
            "Se viene generata una firma XAdES-B-LT o XAdES-B-LTA, l'incorporazione di AnyValidationData "
            "puo' essere usata per incorporare ogni certificato mancante e ogni valore di stato dei "
            "certificati mancante richiesti per convalidare la firma XAdES."
        ),
        "testo_integrale": (
            "cc) Requirement for AnyValidationData. If a XAdES-B-LT or a XAdES-B-LTA signature is "
            "generated, the incorporation of AnyValidationData may be used for incorporating any missing "
            "certificate and any missing certificate status values required for validating the XAdES "
            "signature."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.4 (Legacy XAdES baseline signatures)",
        "testo": (
            "Quando nuove qualifying property non firmate vengono incorporate in firme XAdES baseline "
            "legacy, tali qualifying property devono essere conformi al presente documento."
        ),
        "testo_integrale": (
            "6.4 Legacy XAdES baseline signatures: If new unsigned qualifying properties are incorporated "
            "into legacy XAdES baseline signatures, these qualifying properties shall comply with the "
            "present document."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Si applica quando nuove qualifying property non firmate vengono incorporate in firme XAdES "
            "baseline legacy."
        ),
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 6.1 (Signature levels)",
        "testo": (
            "La clausola 6 definisce quattro livelli di firma XAdES baseline, volti a facilitare "
            "l'interoperabilita' e a coprire il ciclo di vita della firma XAdES: B-B (requisiti per "
            "l'incorporazione di qualifying property firmate e di alcune non firmate quando la firma "
            "viene generata), B-T (generazione e inclusione, per una firma esistente, di un token fidato "
            "che provi che la firma esisteva a una certa data e ora), B-LT (incorporazione nel documento "
            "di firma di tutto il materiale necessario a convalidare la firma, per la disponibilita' a "
            "lungo termine del materiale di convalida) e B-LTA (incorporazione di marche temporali "
            "elettroniche che consentono la convalida della firma molto tempo dopo la sua generazione, "
            "per la disponibilita' e l'integrita' a lungo termine del materiale di convalida)."
        ),
        "testo_integrale": (
            """6.1 Signature levels: Clause 6 defines four levels of XAdES baseline signatures, intended to facilitate interoperability and to encompass the life cycle of XAdES signature, namely:

a) B-B level provides requirements for the incorporation of signed and some unsigned qualifying properties when the signature is generated.

b) B-T level provides requirements for the generation and inclusion, for an existing signature, of a trusted token proving that the signature itself actually existed at a certain date and time.

c) B-LT level provides requirements for the incorporation of all the material required for validating the signature in the signature document. This level aims to tackle the long term availability of the validation material.

d) B-LTA level provides requirements for the incorporation of electronic time-stamps that allow validation of the signature long time after its generation. This level aims to tackle the long term availability and integrity of the validation material.

NOTE 1: ETSI TR 119 100 [i.11] provides a description on the life-cycle of a signature and the rationales on which level is suitable in which situation.

NOTE 2: The levels c) to d) are appropriate where the technical validity of signature needs to be preserved for a period of time after signature creation where certificate expiration, revocation and/or algorithm obsolescence is of concern. The specific level applicable depends on the context and use case.

NOTE 3: B-LTA level targets long term availability and integrity of the validation material of digital signatures over long term. The B-LTA level can help to validate the signature beyond many events that limit its validity (for instance, the weakness of used cryptographic algorithms, or expiration of validation data). The use of B-LTA level is considered an appropriate preservation and transmission technique for signed data.

NOTE 4: Conformance to B-LT level, when combined with appropriate additional preservation techniques tackling the long term availability and integrity of the validation material is sufficient to allow validation of the signature long time after its generation. The assessment of the effectiveness of preservation techniques for signed data other than implementing the B-LTA level are out of the scope of the present document. The reader is advised to consider legal instruments in force and/or other standards (for example ETSI TS 119 511 [i.13], or IETF RFC 4998 [i.15], or IETF RFC 6283 [i.16]) or that can indicate other preservation techniques. Annex C defines what needs to be taken into account when using other techniques for long term availability and integrity of validation data and incorporating a new unsigned property derived from these techniques into the signature."""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.2.2 (Notation for requirements)",
        "testo": (
            "Clausola che definisce la notazione usata per i requisiti dei livelli di firma XAdES: il "
            "significato delle 8 colonne della Tabella 2 (elemento/qualifying property/servizio, presenza "
            "nei quattro livelli B-B, B-T, B-LT e B-LTA, cardinalita', riferimenti, note e requisiti "
            "aggiuntivi), i valori ammessi nelle colonne di presenza (\"shall be present\", \"shall not "
            "be present\", \"may be present\", \"shall be provided\", \"conditioned presence\", "
            "\"*\"), i valori di cardinalita' (0, 1, 0 o 1, maggiore o uguale a 0, maggiore o uguale a "
            "1), il ruolo delle colonne \"References\" e \"Additional notes and requirements\" e un "
            "esempio di lettura della tabella."
        ),
        "testo_integrale": (
            """6.2.2 Notation for requirements: The present clause describes the notation used for defining the requirements of the different XAdES signature levels.

The requirements on the qualifying properties and certain other signature's elements for each XAdES signature level are expressed in table 2. A row in the table either specifies requirements for a qualifying property, other signature's element, or a service.

A service can be provided by different qualifying properties, by other signature's elements, or by other mechanisms (service provision options hereinafter). In these cases, the specification of the requirements for a service is provided by three or more rows. The first row contains the requirements of the service. The requirements for the qualifying properties, other signature's elements, and/or mechanisms used to provide the service are stated in the following rows.

Table 2 contains 8 columns. Below follows a detailed explanation of their meanings and contents:

1) Column "Elements/Qualifying properties/Services":

a) In the case where the cell identifies a Service, the cell content starts with the keyword "Service" followed by the name of the service.

b) In the case where the qualifying property or other signature's element provides a service, this cell contains "SPO" (for Service Provision Option), followed by the name of the qualifying property or the other signature's element.

c) Otherwise, this cell contains the name of the qualifying property or the other signature's element.

2) Column "Presence in B-B-Level": This cell contains the specification of the presence of the qualifying property or other signature's element, or the provision of a service, for XAdES-B-B signatures.

3) Column "Presence in B-T level": This cell contains the specification of the presence of the qualifying property or other signature's element, or the provision of a service, for XAdES-B-T signatures.

4) Column "Presence in B-LT level": This cell contains the specification of the presence of the qualifying property or other signature's element, or the provision of a service, for XAdES-B-LT signatures.

5) Column "Presence in B-LTA level": This cell contains the specification of the presence of the qualifying property or other signature's element, or the provision of a service, for XAdES-B-LTA signatures. Below follow the values that can appear in columns "Presence in B-B", "Presence in B-T", "Presence in B-LT", and "Presence in B-LTA":

- "shall be present": means that the qualifying property or signature's element shall be incorporated to the signature, and shall be as specified in the document referenced in column "References", further profiled with the additional requirements referenced in column "Requirements", and with the cardinality indicated in column "Cardinality".

- "shall not be present": means that the qualifying property or signature's element shall not be incorporated to the signature.

- "may be present": means that the qualifying property or signature's element may be incorporated to the signature, and shall be as specified in the document referenced in column "References", further profiled with the additional requirements referenced in column "Requirements", and with the cardinality indicated in column "Cardinality".

- "shall be provided": means that the service identified in the first column of the row shall be provided as further specified in the SPO-related rows. This value only appears in rows that contain requirements for services. It does not appear in rows that contain requirements for qualifying properties or signature's elements.

- "conditioned presence": means that the incorporation to the signature of the item identified in the first column is conditioned as per the requirements referenced in column "Requirements" and requirements in specifications and clauses referenced by column "References", with the cardinality indicated in column "Cardinality".

- "*": means that the qualifying property or signature's element (service) identified in the first column should not be incorporated to the signature (provided) in the corresponding level. Upper signature levels may specify other requirements.

NOTE: Incorporating an unsigned property that is marked with a "*" into a signature can lead to cases where a higher level cannot be achieved, except by removing the corresponding unsigned property.

6) Column "Cardinality": This cell indicates the cardinality of the qualifying property or other signature's element. If the cardinality is the same for all the levels, only the values listed below appear. Otherwise the content specifies the cardinality for each level. See the example at the end of the present clause showing this situation. Below follow the values indicating the cardinality:

- 0: The signature shall not incorporate any instance of the qualifying property or the signature's element.

- 1: The signature shall incorporate exactly one instance of the qualifying property or the signature's element.

- 0 or 1: The signature shall incorporate zero or one instance of the qualifying property or the signature's element.

- ≥ 0: The signature shall incorporate zero or more instances of the qualifying property or the signature's element.

- ≥ 1: The signature shall incorporate one or more instances of the qualifying property or the signature's element.

7) Column "References": This shall contain either the number of the clause specifying the qualifying property in the present document, or a reference to the document and clause that specifies the other signature's element.

8) Column "Additional notes and requirements": This cell contains numbers referencing notes and/or letters referencing additional requirements on the qualifying property or the other signature's element. Both notes and additional requirements are listed below the table.

Names of XML elements in the namespace whose URI is http://www.w3.org/2000/09/xmldsig# are preceded by prefix ds.

EXAMPLE: In table 2, the row corresponding to CompleteCertificateRefsV2 qualifying property has a value "*" in the cells in columns "Presence in B-B level" and "Presence in B-T level", and "shall not be present" in cells in columns "Presence in B-LT level" and "Presence in B-LTA level". The cell in column "Cardinality" indicates the cardinality for each level as follows: "B-B, B-T: 0 or 1" indicates that XAdES-B-B and XAdES-B-T signatures can incorporate one instance of CompleteCertificateRefsV2 qualifying property; "B-LT, B-LTA: 0" indicates that XAdES-B-LT and XAdES-B-LTA do not incorporate the CompleteCertificateRefsV2 qualifying property."""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 6.1 (Signature levels)",
    "clausola 6.2.1 (Algorithm requirements)",
    "clausola 6.2.2 (Notation for requirements)",
    "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)",
    "clausola 6.3, requisito addizionale a)",
    "clausola 6.3, requisito addizionale b)",
    "clausola 6.3, requisito addizionale c)",
    "clausola 6.3, requisito addizionale d)",
    "clausola 6.3, requisito addizionale e)",
    "clausola 6.3, requisito addizionale f)",
    "clausola 6.3, requisito addizionale g)",
    "clausola 6.3, requisito addizionale h)",
    "clausola 6.3, requisito addizionale i)",
    "clausola 6.3, requisito addizionale j)",
    "clausola 6.3, requisito addizionale k)",
    "clausola 6.3, requisito addizionale l)",
    "clausola 6.3, requisito addizionale m)",
    "clausola 6.3, requisito addizionale n)",
    "clausola 6.3, requisito addizionale o)",
    "clausola 6.3, requisito addizionale p)",
    "clausola 6.3, requisito addizionale q)",
    "clausola 6.3, requisito addizionale r)",
    "clausola 6.3, requisito addizionale s)",
    "clausola 6.3, requisito addizionale t)",
    "clausola 6.3, requisito addizionale u)",
    "clausola 6.3, requisito addizionale v)",
    "clausola 6.3, requisito addizionale w)",
    "clausola 6.3, requisito addizionale x)",
    "clausola 6.3, requisito addizionale y)",
    "clausola 6.3, requisito addizionale z)",
    "clausola 6.3, requisito addizionale aa)",
    "clausola 6.3, requisito addizionale bb)",
    "clausola 6.3, requisito addizionale cc)",
    "clausola 6.4 (Legacy XAdES baseline signatures)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Relazioni interne alla clausola 6.3 (rinvii della Tabella 2 ai requisiti
# addizionali, colonna "Additional requirements and notes"), una per lettera.
# Nessuna relazione verso altri capitoli di questa fonte o verso altre fonti:
# vedi docstring di modulo e ADR-0009/ADR-0012.
RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale a)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale b)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale c)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale d)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale e)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale f)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale g)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale h)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale i)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale j)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale k)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale l)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale m)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale n)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale o)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale p)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale q)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale r)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale s)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale t)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale u)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale v)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale w)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale x)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale y)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale z)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale aa)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale bb)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale cc)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
