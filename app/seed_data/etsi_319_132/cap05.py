"""ETSI EN 319 132-1 V1.3.1 (2024-07) - Electronic Signatures and Trust
Infrastructures (ESI); XAdES digital signatures; Part 1: Building blocks and
XAdES baseline signatures. Capitolo 5 dello split: clausola 5 (Qualifying
properties semantics and syntax), da 5.2.8.2 (The IndividualDataObjectsTimeStamp
qualifying property) a 5.5.2.2 (Generation and incorporation of
ArchiveTimeStamp) inclusa.

Provenienza del testo: app/.source_cache/etsi_319_132/cap05.txt (porzione dello
split deterministico; testo ufficiale completo in
app/.source_cache/etsi_319_132/raw.txt, raw_body.txt e raw.pdf). Versione ETSI
EN 319 132-1 V1.3.1 (2024-07), deliver "01.03.01_60"; da
app/.source_cache/etsi_319_132/provenance.json: url
https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf,
data_fetch 2026-09-29T12:56:34Z, sha256_raw_pdf
83fc87ee09de90274131a1f60cb73edb742cebc7cd8961342586ed06133664c5, formato
"PDF ETSI deliver (pdftotext -layout)". Manifest di split:
app/.source_cache/etsi_319_132/manifest.json (cap05 = da 5.2.8.2 a 5.5.2.2; il
capitolo precedente, cap04.txt, finisce con 5.2.8.1 e il successivo, cap06.txt,
riprende da 5.5.2.3). Questo modulo e' puro dato: non importa nulla e non legge
file; la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py (che questo modulo NON tocca).

## Perimetro e granularita' (ADR-0007)

15 item di indice = 15 righe: una riga per ciascuna sottoclausta numerata del
perimetro (5.2.8.2, 5.2.9.1, 5.2.9.2, 5.2.10, 5.3, 5.4.1, 5.4.2, 5.4.3, 5.4.4,
5.4.5, 5.4.6, 5.5.1.1, 5.5.1.2, 5.5.2.1, 5.5.2.2), con la sua semantica e la
sua sintassi. In questa clausola lo standard non numera requisiti con id propri
(la forma <SIGLA>-<clausola>-<NN> appartiene alla clausola 6 di ETSI EN 319
122-1, non a questo documento): l'unita' di prescrizione e' la sottoclausta che
definisce un tipo, un attributo o una qualifying property, delimitata dalle
etichette "Semantics" e "Syntax" ovvero da un blocco di passi prescritti.
Precedente identico nella stessa fonte: cap04.py di questo stesso documento
(clausola 5, da 5.1 a 5.2.8.1, una sottoclausta = una riga) e, nel blocco B
della famiglia AdES, ETSI EN 319 122-1 cap03/cap04.

Perche' NON una riga per voce interna. Gli elenchi interni a una sottoclausta
restano nel nodo della sottoclausta: i sei requirements numerati 1)-6) di 5.4.2,
i cinque 1)-5) di 5.4.3, i tre di 5.4.4 e di 5.4.5, i due bullets di 5.4.6 e di
5.2.10, i cinque passi 1)-6) di 5.5.2.2 (con la lettera a)-d) di 5.2.8.2), i
tre di 5.5.1.2 (due volte), i due di 5.3 e i tre qualifier di 5.2.9.2 sono
dettaglio della stessa prescrizione: nessuno di essi ha un id proprio con cui
il documento lo richiami altrove, e i rinvii interni del capitolo citano sempre
una sottoclausta numerata ("see clause 5.5.2.4", "as specified in clause
5.4.3"), mai un requisito numerato o un qualifier. La granularita' per
lettera/voce si applica dove il documento numera requisiti propri e li usa come
indice (ETSI EN 319 122-1 clausola 6.3, lettere a)-t), richiamate dalla colonna
"Additional requirements and notes" della sua Tabella 1): qui il documento non
lo fa. Le righe della tabella di quella clausola e le voci di elenco di questa
sono quindi due casi diversi, non due letture dello stesso criterio.

DUBBIO DI GRANULARITA' APERTO per la revisione umana: 5.2.9.2 ("Signature
policy qualifiers") definisce tre elementi distinti con semantica e sintassi
proprie (SPURI, SPUserNotice, SPDocSpecification) e potrebbe essere letta come
tre righe + chapeau. Qui resta una riga sola per coerenza con cap04.py dello
stesso documento (che tiene nello stesso nodo gli elenchi interni) e con il
fatto che il documento numera 5.2.9.2 come una sola unita'; se la revisione
preferisse la granularita' per elemento, sono separabili senza toccare il resto.

Intestazioni di puro raggruppamento, senza testo proprio, NON generano nodo ne'
item di indice: "5.2.9 The SignaturePolicyIdentifier qualifying property" (seguita
immediatamente da 5.2.9.1), "5.4 Qualifying Properties for validation data
values" (seguita da 5.4.1), "5.5 Qualifying properties for long term
availability and integrity of validation material" (intestazione su due righe,
seguita da 5.5.1), "5.5.1 The TimeStampValidationData qualifying property"
(seguita da 5.5.1.1) e "5.5.2 The ArchiveTimeStamp qualifying property defined
in namespace with URI http://uri.etsi.org/01903/v1.4.1#" (intestazione su due
righe, seguita da 5.5.2.1): ciascuna e' seguita immediatamente dalla prima
sottoclausta, senza una riga di testo proprio da assorbire (stesso criterio di
cap04.py di questa fonte).

## Obbligo o Principio, riga per riga

- 5.2.8.2 (The IndividualDataObjectsTimeStamp qualifying property) -> Obbligo
  "tecnico/sicurezza": proprieta' firmata, marche temporali incapsulate,
  meccanismo esplicito (Include), attributo referencedData obbligatorio e
  procedura di calcolo dell'impronta.
- 5.2.9.1 (Semantics and syntax) -> Obbligo "tecnico/sicurezza": requisiti su
  SignaturePolicyId, SigPolicyId, ds:Transforms, SigPolicyHash, nuova
  trasformazione SPDocDigestAsInSpecification e suo divieto d'uso fuori da
  SignaturePolicyId, SigPolicyQualifier(s), SignaturePolicyImplied.
- 5.2.9.2 (Signature policy qualifiers) -> Obbligo "tecnico/sicurezza":
  requisiti su SPURI, SPUserNotice, ExplicitText, NoticeRef, SPDocSpecification
  e sulla distinzione OID/URI (URN con QualifierType "OIDAsURN").
- 5.2.10 (The SignaturePolicyStore qualifying property) -> Obbligo
  "tecnico/sicurezza": contenuto alternativo (documento in base 64 o URI di uno
  store locale) e requisito su SPDocSpecification.
- 5.3 (The SignatureTimeStamp qualifying property) -> Obbligo
  "tecnico/sicurezza": proprieta' non firmata, marche temporali su
  ds:SignatureValue, meccanismo implicito e costruzione dell'input.
- 5.4.1 (Introduction) -> Principio "scopo/ambito di applicazione": dichiara che
  cosa la clausola 5.4 specifica e che una firma XAdES puo' contenere
  certificati e dati di revoca nelle property di quella clausola, a condizione
  che i requisiti di ciascuna siano rispettati. Disposizione di ambito, priva di
  un comportamento imposto a un soggetto: i requisiti stanno nelle sottoclausole
  seguenti, nodi separati.
- 5.4.2 (CertificateValues) -> Obbligo "tecnico/sicurezza": i sei requirements
  1)-6) di contenuto, piu' i requisiti su EncapsulatedX509Certificate e
  OtherCertificate.
- 5.4.3 (RevocationValues) -> Obbligo "tecnico/sicurezza": i cinque requirements
  1)-5), piu' i requisiti su CRLValues, EncapsulatedCRLValue, Delta CRL,
  OCSPValues, EncapsulatedOCSPValue e OtherValues.
- 5.4.4 (AttrAuthoritiesCertValues) -> Obbligo "tecnico/sicurezza": i tre
  requirements 1)-3) sui certificati degli attestati di attributo e delle
  assertion firmate.
- 5.4.5 (AttributeRevocationValues) -> Obbligo "tecnico/sicurezza": i tre
  requirements 1)-3) e il requisito sulle Delta CRL.
- 5.4.6 (AnyValidationData) -> Obbligo "tecnico/sicurezza": i due bullets di
  contenuto, i requisiti sui figli CertificateValues e RevocationValues e il
  divieto dell'attributo URI.
- 5.5.1.1 (Semantics and syntax) -> Obbligo "tecnico/sicurezza": contenitore di
  dati di validazione delle marche temporali, requisiti sui figli
  CertificateValues/RevocationValues e sugli attributi Id e URI.
- 5.5.1.2 (Use of URI attribute) -> Obbligo "tecnico/sicurezza": i passi di
  creazione e incorporamento della TimeStampValidationData e il comportamento
  prescritto all'applicazione di convalida sull'attributo URI.
- 5.5.2.1 (Semantics and syntax) -> Obbligo "tecnico/sicurezza": proprieta' non
  firmata, marche temporali su tutti gli oggetti incorporati, ordine rispetto
  alla CounterSignature e rinvio a 5.5.2.3/5.5.2.4.
- 5.5.2.2 (Generation and incorporation of ArchiveTimeStamp) -> Obbligo
  "tecnico/sicurezza": i sei passi numerati 1)-6) di aumento della firma.

Nessun tipo di obbligo diverso da "tecnico/sicurezza": il capitolo vincola il
contenuto, la codifica, la costruzione e l'incorporamento delle qualifying
property XAdES e delle marche temporali che esse incapsulano; nessun documento
di questo perimetro impone comportamenti organizzativi, informativi, di
conservazione o sanzionatori. DUBBIO APERTO: 5.5.2.2 prescrive una sequenza di
passi di aumento della firma e potrebbe essere letto come "procedurale"; resta
"tecnico/sicurezza" per coerenza con il resto del capitolo e con cap04.py di
questa fonte (che classifica cosi' i due processing model di 5.1.4.4.2.2 e
5.1.4.4.2.3).

Soggetti: valorizzati solo dove il testo nomina davvero il soggetto.
- 5.5.1.2: "the application shall ignore this value and may try to use the
  validation material" -> 'Terza parte' obbligata (l'applicazione di convalida
  della firma), stessa convenzione con cui ETSI EN 319 122-1 cap03 mappa
  "signature validation applications" su 'Terza parte' obbligato. La riga copre
  anche i passi di creazione, il cui soggetto il testo non nomina (forma
  passiva "shall be created"): il soggetto dichiarato e' quello della parte di
  testo che lo nomina.
- Tutte le altre righe restano senza soggetti: il testo prescrive sul tipo o
  sull'elemento ("the X qualifying property shall ...", "The ExplicitText
  element shall ...") e non nomina chi deve conformarsi.
- Soggetti nominati ma NON mappati, per non attribuire loro un ruolo che il
  testo non assegna: "the relying party should be aware of" in 5.2.9.1 (l'attesa
  e' descritta dentro la definizione della politica implicita, non e' un
  comportamento imposto al terzo affidante); "(signing/validating) applications
  can retrieve the signature policy document" in NOTE 2 di 5.2.9.2 e "the
  application could get the explicit notices from a notices file" nella stessa
  clausola (permissione descrittiva, non requisito sull'applicazione); "It is
  the responsibility of the entity incorporating the signature policy to the
  signature-policy-store to make sure that the correct document is securely
  stored" in NOTE 2 di 5.2.10 (responsabilita' su un soggetto che il documento
  non riconduce a nessuna categoria del censimento: l'entita' che incorpora
  puo' essere indistintamente firmatario o servizio); "a verifier can accept a
  different certificate path" in NOTE 2 di 5.4.6; "the corresponding electronic
  time-stamp Service Providers" cui 5.5.2.2 chiede le marche temporali (destinatari
  della richiesta, non obbligati). DUBBIO APERTO per la revisione umana: se si
  volesse tracciare la NOTE 2 di 5.2.10, la categoria sarebbe 'Terza parte' o
  'Utente/titolare' obbligato, a seconda di come si legge l'entita' che
  incorpora la politica di firma.

Nessun `oggetti_giuridici`: il testo nomina qualifying property XAdES, tipi XML,
marche temporali elettroniche generiche e firme XAdES, mai uno degli oggetti
della tassonomia eIDAS (firma elettronica qualificata, sigillo elettronico,
marca temporale elettronica qualificata, documento elettronico, ...): una
"electronic time-stamp" senza qualificazione non e' la marca temporale
elettronica qualificata, e "XAdES signature" non e' un oggetto dello schema.
Stesso criterio di cap04.py di questa fonte.

`severita` e `sanzioni` assenti (standard tecnico, nessuna sanzione); `stato`
sempre "vigente"; `condizione_applicabilita` mai valorizzata: nessuna
sottoclausta del perimetro dipende da un fatto esterno non tracciato nel
censimento. Le condizioni interne ("If this transform is used", "If the
validation data contain one or more Delta CRLs", "For augmenting a XAdES
signature by incorporation of a new ArchiveTimeStamp", "If a XAdES signature
requires including all the validation data ...") sono parte della prescrizione e
restano nel `testo_integrale` della riga, dove il testo ufficiale le colloca.

## Fedelta' dell'estrazione

- pie' di pagina e testatine delle pagine 36-49 ("ETSI" e "<n> ETSI EN 319
  132-1 V1.3.1 (2024-07)", separate da righe vuote di impaginazione): rimossi,
  sono paratesto. Il file cap05.txt termina con la coppia di righe di pie' di
  pagina della pagina 49: rimossa anche quella.
- righe spezzate a meta' frase: ricucite in un'unica riga. Il trattino di fine
  riga appartiene sempre alla parola, mai una sillabazione da rimuovere: il nome
  del file di schema "1913201-" + "XAdES01903v132.xsd" / "1913201-" +
  "XAdES01903v141.xsd" e' ricomposto senza spazio, come "electronic time-" +
  "stamps" -> "electronic time-stamps" in 5.2.8.2, 5.3 e 5.5.1.1 e "electronic
  time-" + "stamp" -> "electronic time-stamp" in 5.5.1.2.
- una sola interruzione di pagina cade dentro un blocco di schema XML (dentro
  <xsd:complexType name="SignaturePolicyIdentifierType">, fra </xsd:choice> e
  </xsd:complexType>, pagine 36-37): il blocco e' stato ricucito come continua
  nel testo ufficiale, senza righe vuote introdotte dal salto di pagina; le
  righe vuote che separano fra loro i <xsd:complexType> sono quelle presenti nel
  testo. Le altre interruzioni di pagina del capitolo cadono fra due paragrafi
  (5.2.9.1, 5.2.9.2, 5.2.10, 5.4.6, 5.5.1.1, 5.5.1.2, 5.5.2.1), fra il testo e
  una NOTE (5.2.10), fra due requirements numerati (5.4.2 fra 3) e 4), 5.4.3 fra
  4) e 5)), fra due NOTE (5.5.2.1) o fra due sottoclausole (dopo 5.2.8.2, dopo
  5.2.9.1, dopo 5.4.3, dopo 5.4.5): nessuna di esse ha richiesto ricuciture.
- l'intestazione della sottoclausta NON e' ripetuta dentro `testo_integrale` (il
  riferimento del nodo la porta gia', titolo compreso); le etichette interne
  "Semantics" e "Syntax" sono mantenute e unite alla prima frase della loro
  sezione ("Semantics: ..." / "Syntax: ..."), come in cap04.py di questa fonte.
  Le tre sottoclausole che si aprono direttamente con la prosa (5.4.1, 5.5.1.2,
  5.5.2.2) non hanno etichette da unire.
- elenchi e passi: i pallini di primo livello restano "•" con indentazione
  "  •   ", i trattini di sottolivello "-" con indentazione "    -   ", i passi
  numerati "1)" e le lettere "a)" a inizio riga (stessa normalizzazione di
  cap04.py); il sotto-paragrafo di 5.5.2.2 passo 1) ("Any missing certificate
  and/or revocation data may be placed in any XAdES qualifying property ...") e'
  mantenuto indentato di 4 spazi, come nel testo ufficiale, perche' appartiene
  al passo 1) e non all'elenco principale.
- le righe di commento XML dello schema ("<!-- targetNamespace=... -->") restano
  immediatamente dopo la riga che le introduce, senza riga vuota aggiunta, come
  nel testo ufficiale (compresi i commenti su tre righe con la nota sul
  preamble e sulla namespace declaration xmlns:xades).
- refusi del testo ufficiale riportati come sono, senza correzioni: in 5.5.1.2
  NOTE 2 la spaziatura "electronic time- stamp container" (trattino staccato
  dalla parola); in 5.5.2.2 passo 6) la ripetizione "its electronic electronic
  time-stamp(s)"; in 5.5.1.2 il nome "AllDataObjectTimeStamp" (senza la "s" di
  "Objects" usata dal titolo di 5.2.8.1). Nessuna correzione e' stata apportata
  al testo dello standard.

## Esclusioni (paratesto, non contenuto normativo)

- front matter, Contents, Foreword, History, elenco dei riferimenti
  bibliografici (clausola 2 References) e tutte le clausole fuori dal perimetro:
  non fanno parte di cap05.txt e non sono censiti qui (cap05.txt comincia con
  l'intestazione di 5.2.8.2 e finisce con il passo 6) di 5.5.2.2);
- intestazioni di raggruppamento senza testo proprio (5.2.9, 5.4, 5.5, 5.5.1,
  5.5.2): nessun nodo e nessun item di indice, per non creare item fittizi;
- pie' di pagina e testatine di pagina (vedi "Fedelta' dell'estrazione"): il
  file assegnato non contiene figure ne' tabelle, nessun elemento grafico.

## Rinvii demandati alla fase 6 (nessuna relazione creata verso di essi)

- clausole di altri capitoli dello stesso documento: 5.2.8.2, 5.2.9.1, 5.2.9.2,
  5.2.10, 5.3, 5.4.2, 5.4.3, 5.4.4, 5.4.5, 5.4.6, 5.5.1.1, 5.5.2.1 rinviano
  alla clausola C.1 o C.2 per la collocazione del file di schema XML (Annex C,
  cap08.txt); 5.2.8.2, 5.3 e 5.5.2.1 (via le clausole 5.5.2.3/5.5.2.4) rinviano
  alla clausola 4.5 (canonicalizzazione XML, cap03.txt); 5.2.8.2 rinvia al
  meccanismo esplicito (Include) e 5.3 a quello implicito, definiti in 5.1.4.4.1
  e 5.1.4.4.2.1 (cap04.txt); 5.4.1
  rinvia implicitamente alle sottoclausole della stessa clausola 5.4; 5.4.3
  rinvia a IETF RFC 6960 [6] per OCSPResponse; 5.4.2 e 5.4.3 nominano
  SignerRoleV2 (clausola 5.2.6, cap04.txt); 5.4.6 nomina le clausole 5.4.3 e
  5.5.1.2 (relazioni dichiarate qui); 5.5.1.2 rinvia a clause 4.4 (cap03.txt) e
  nomina i contenitori di marche temporali IndividualDataObjectsTimeStamp,
  SignatureTimeStamp e ArchiveTimeStamp (relazioni dichiarate qui),
  AllDataObjectTimeStamp (clausola 5.2.8.1, cap04.txt) e le property
  RefsOnlyTimeStampV2 e SigAndRefsTimeStampV2 (Annex A, cap08.txt); 5.5.2.1
  rinvia a 5.2.7.1
  (cap04.txt) e a 5.5.2.3/5.5.2.4 (cap06.txt); 5.5.2.2 rinvia a 5.5.2.3 e
  5.5.2.4 (cap06.txt).
- rinvii a unita' indivise prive di nodo proprio: 5.5.2.2 passo 1) rinvia a
  "clause 5.4" in blocco (la partizione "clausola 5.4" e' generata dalle righe
  di questo modulo, ma le partizioni come estremo di relazione sono dichiarate
  dalla sessione principale, non da un modulo capitolo: vedi ADR-0012 e i moduli
  capNN_relazioni_cross.py delle altre fonti).
- norme e specifiche esterne: XMLDSIG [1] (5.2.8.2 in piu' punti, 5.2.9.1, 5.4.2
  via la NOTE, 5.4.3 via la NOTE), ETSI TS 119 172-1 [i.7] (NOTE 1 di 5.2.9.1),
  IETF RFC 3061 [8] (5.2.9.2), IETF RFC 6960 [6] (5.4.3), X.509 CRL [15]
  (5.4.3).

## Relazioni dichiarate

Tredici relazioni "richiama" fra righe di questo modulo, tutte interne al
perimetro (nessuna verso altri capitoli o altre fonti: le costruisce la sessione
principale in fase 6, ADR-0009).

Con `evidence_type` "textual" (citazione letterale del numero di clausola nel
`testo_integrale` del nodo citante, verificabile anche con
app/tools/verifica_relazioni_textual.py):
- 5.2.9.1 -> 5.2.9.2 ("the SPDocSpecification qualifier, specified in clause
  5.2.9.2");
- 5.4.6 -> 5.4.3 ("Its syntax shall be as specified in clause 5.4.3 of the
  present document").

Con `evidence_type` "inferred" (l'evidenza e' il nome dell'elemento o del tipo,
non un numero di clausola, come per le relazioni dedotte di cap03/cap04 di questa
fonte):
- 5.2.10 -> 5.2.9.1 ("the signature policy document which is referenced in the
  SignaturePolicyIdentifier qualifying property", piu' SigPolicyHash nella
  NOTE 3) e 5.2.10 -> 5.2.9.2 (NOTE 1: "Contrary to the SPURI, the
  SigPolDocLocalURI points to a local file");
- 5.4.6 -> 5.5.1.2 (NOTE 3: "The URI attribute can be used within
  TimeStampValidationData unsigned qualifying property (see clause 5.5.1.2 of
  the present document for details)"), quest'ultima con evidenza testuale;
- 5.4.4 -> 5.4.2 e 5.4.5 -> 5.4.3 (le due property sono definite dal documento
  con il tipo CertificateValuesType / RevocationValuesType, definito
  rispettivamente in 5.4.2 e 5.4.3);
- 5.4.6 -> 5.4.2 (il figlio CertificateValues e' un xades:CertificateValues,
  property definita in 5.4.2);
- 5.5.1.1 -> 5.4.2 e 5.5.1.1 -> 5.4.3 (i figli CertificateValues e
  RevocationValues di TimeStampValidationData sono gli stessi elementi definiti
  in 5.4.2 e 5.4.3);
- 5.5.1.2 -> 5.2.8.2, 5.5.1.2 -> 5.3 e 5.5.1.2 -> 5.5.2.1 (i contenitori di
  marche temporali IndividualDataObjectsTimeStamp, SignatureTimeStamp e
  ArchiveTimeStamp i cui dati di validazione la property deve portare; gli altri
  contenitori nominati dalla stessa frase, AllDataObjectTimeStamp e
  RefsOnlyTimeStampV2/SigAndRefsTimeStampV2, stanno fuori da questo modulo).

`confidence` resta null su tutte: non esiste uno score reale da riportare
(ADR-0005). Le relazioni sono dichiarate una volta sola, nella direzione del
testo citante (il documento cita un tipo o un elemento definito altrove, non
viceversa); la relazione inversa si ottiene per traversal a ritroso.

## Copertura

15 item di indice, 15 righe: 14 obblighi + 1 principio. Nessun item doppio,
nessun item mancante, nessuna riga fuori indice.

## Dubbi di classificazione aperti (per la revisione umana)

1) 5.4.1 e' classificata Principio "scopo/ambito di applicazione" (dichiara che
   cosa la clausola 5.4 specifica e a quali property si applica). Precedente
   EN 319 122-1 cap03 classifica le due Introduction con "altro": se la
   revisione preferisse quella convenzione, la sostanza del testo non cambia.
2) Granularita' di 5.2.9.2 (tre qualifier in una riga sola) e dei requirements
   numerati di 5.4.2-5.4.5: vedi "Perimetro e granularita'" sopra.
3) Tipo di obbligo di 5.5.2.2: alternativa "procedurale" (vedi sopra).
4) Soggetto della NOTE 2 di 5.2.10 e dell'attributo URI in 5.5.1.2 (l'attesa
   sul terzo affidante in 5.2.9.1): vedi "Soggetti" sopra.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 5.2.8.2 (The IndividualDataObjectsTimeStamp qualifying property)",
        "testo": (
            "La property deve essere una qualifying property firmata che qualifica gli oggetti firmati e "
            "deve incapsulare una o piu' marche temporali generate prima della produzione della firma, il "
            "cui input di calcolo dell'impronta e' la concatenazione degli oggetti ottenuti processando "
            "come in XMLDSIG (clausola 4.4.3.2) alcuni ds:Reference di ds:SignedInfo o di un ds:Manifest "
            "firmato, escluso quello che referenzia SignedProperties. Per generarla si usa il meccanismo "
            "esplicito (Include): ogni elemento Include deve riferirsi ai ds:Reference degli oggetti da "
            "marcare e portare l'attributo referencedData posto a \"true\", e l'input si calcola "
            "inizializzando un flusso di ottetti vuoto, processando ogni ds:Reference nell'ordine di "
            "comparsa negli Include (recupero dell'oggetto referenziato, canonicalizzazione se node-set o "
            "applicazione delle trasformazioni, concatenazione degli ottetti)."
        ),
        "testo_integrale": (
            """Semantics: The IndividualDataObjectsTimeStamp qualifying property shall be a signed qualifying property that qualifies signed data objects.

The IndividualDataObjectsTimeStamp qualifying property shall encapsulate one or more electronic time-stamps, generated before the signature production, whose message imprint computation input is the concatenation of the objects obtained after processing as specified in XMLDSIG [1], clause 4.4.3.2; some of the ds:Reference elements within the ds:SignedInfo or also signed ds:Manifest.

The set of ds:Reference elements processed shall not include the one referencing the SignedProperties element.

Syntax: The IndividualDataObjectsTimeStamp qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="IndividualDataObjectsTimeStamp" type="XAdESTimeStampType"/>

The explicit (Include) mechanism shall be used for generating this qualifying property.

The Include elements shall be composed to refer to those ds:Reference elements referencing the data objects that have to be time-stamped.

The referencedData attribute shall be present in each and every Include element, and set to "true".

The message imprint computation input shall be computed as follows:

1) Initialize the final octet stream as an empty octet stream.

2) Take all the ds:Reference elements within ds:SignedInfo or within a signed ds:Manifest which are referenced within the Include element. Process each one in their order of appearance within the Include element as indicated below:

a) Retrieve the data object referenced by the URI attribute of the ds:Reference element, as specified in clause 4.4.3.2 of XMLDSIG [1].

NOTE: Clause 4.4.3.2 of XMLDSIG [1], specifies rules for URI dereferencing. For instance, it mandates that the dereferencing of a non 'same-document' reference (which XMLDSIG [1] defines as "a URI-Reference that consists of a hash sign ('#') followed by a fragment or alternatively consists of an empty URI") is always an octet-stream.

b) If the ds:Reference element does not contain the ds:Transforms element, then:

    -   if the retrieved data object is an XML node-set, then canonicalize it as specified in clause 4.5 of the present document;

    -   else proceed to step d).

c) If the ds:Reference element contains the ds:Transforms element, then apply all the transforms indicated within the ds:Transform children elements. After that:

    -   if the output of the last transform is a XML node-set according to XMLDSIG [1], canonicalize it as specified in clause 4.5 of the present document;

    -   else proceed to step d).

d) Concatenate the resulting octets to the final octet stream."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.9.1 (Semantics and syntax)",
        "testo": (
            "La property deve essere una qualifying property firmata che qualifica la firma e deve "
            "contenere o un identificatore esplicito di una politica di firma o l'indicazione che esiste "
            "una politica implicita di cui il terzo affidante dovrebbe essere consapevole. Se si usa "
            "l'identificatore esplicito, SignaturePolicyId lo referenzia, SigPolicyId deve identificare "
            "univocamente una versione della politica, ds:Transforms contiene le trasformazioni subite dal "
            "documento prima del calcolo dell'hash e SigPolicyHash l'identificatore dell'algoritmo e il "
            "valore dell'hash; il documento definisce una nuova trasformazione identificata dall'URI "
            ".../SignaturePolicy/SPDocDigestAsInSpecification, che se usata obbliga a qualificare la "
            "property almeno con il qualifier SPDocSpecification (clausola 5.2.9.2) e non puo' essere usata "
            "in elementi diversi da SignaturePolicyId. SigPolicyQualifier puo' contenere informazioni "
            "aggiuntive, SigPolicyQualifiers deve contenerne uno o piu' (anche dello stesso tipo) e "
            "l'elemento vuoto SignaturePolicyImplied indica che gli oggetti firmati e altri dati esterni "
            "implicano la politica."
        ),
        "testo_integrale": (
            """Semantics: The SignaturePolicyIdentifier qualifying property shall be a signed qualifying property qualifying the signature.

The SignaturePolicyIdentifier qualifying property shall contain either an explicit identifier of a signature policy or an indication that there is an implied signature policy that the relying party should be aware of.

NOTE 1: ETSI TS 119 172-1 [i.7] specifies a framework for signature policies.

Syntax: The SignaturePolicyIdentifier qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="SignaturePolicyIdentifier" type="SignaturePolicyIdentifierType"/>

<xsd:complexType name="SignaturePolicyIdentifierType">
  <xsd:choice>
    <xsd:element name="SignaturePolicyId" type="SignaturePolicyIdType"/>
    <xsd:element name="SignaturePolicyImplied"/>
  </xsd:choice>
</xsd:complexType>

<xsd:complexType name="SignaturePolicyIdType">
  <xsd:sequence>
    <xsd:element name="SigPolicyId" type="ObjectIdentifierType"/>
    <xsd:element ref="ds:Transforms" minOccurs="0"/>
    <xsd:element name="SigPolicyHash" type="DigestAlgAndValueType"/>
    <xsd:element name="SigPolicyQualifiers"
      type="SigPolicyQualifiersListType" minOccurs="0"/>
  </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="SigPolicyQualifiersListType">
  <xsd:sequence>
    <xsd:element name="SigPolicyQualifier" type="AnyType"
      maxOccurs="unbounded"/>
  </xsd:sequence>
</xsd:complexType>

The SignaturePolicyId element shall be used for referencing the signature policy explicitly.

The SigPolicyId element shall uniquely identify a specific version of the signature policy.

The ds:Transforms element shall contain the transformations performed on the signature policy document before computing its hash. The processing model for these transformations shall be as described in XMLDSIG [1].

The SigPolicyHash element shall contain the identifier of the hash algorithm and the hash value of the object obtained after processing SigPolicyId and ds:Transforms if present.

The present document defines a new transform, which shall be identified by setting the value of the Algorithm attribute of the ds:Transform element to:

  •   http://uri.etsi.org/01903/v1.3.2/SignaturePolicy/SPDocDigestAsInSpecification.

This transform shall indicate that the hash value of the signature policy document has been computed as specified in a certain technical specification.

If this transform is used, then the SignaturePolicyIdentifier shall be qualified at least by the SPDocSpecification qualifier, specified in clause 5.2.9.2, which identifies the aforementioned technical specification.

NOTE 2: This transform can be used when the technical specification defines a mechanism for computing the hash value of the signature policy document that is not easily implementable using widely used XML technologies (e.g. XPath), as can occur, for instance, when the signature policy document is DER-encoded ASN.1.

This transform shall not be used in elements different than SignaturePolicyId element.

The SigPolicyQualifier element may contain additional information qualifying the signature policy identifier.

The SigPolicyQualifiers element shall contain one or more qualifiers of the signature policy.

The SigPolicyQualifiers element may contain one or more qualifiers of the same type.

The SignaturePolicyImplied empty element shall indicate that the data object(s) being signed and other external data imply the signature policy.

NOTE 3: The SignaturePolicyImplied element can be used when the signature policy can be unambiguously derived from the semantics of the type of data object(s) being signed, and some other information."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.9.2 (Signature policy qualifiers)",
        "testo": (
            "Definisce i tre qualifier della politica di firma: SPURI (URL da cui ottenere una copia del "
            "documento di politica), SPUserNotice (avviso destinato a essere mostrato alla convalida della "
            "firma, con ExplicitText per il testo e NoticeRef per l'organizzazione e i numeri degli avvisi) "
            "e SPDocSpecification (identificatore della specifica tecnica che definisce la sintassi del "
            "documento di politica). SPURI deve contenere un URL, SPUserNotice e ExplicitText le "
            "informazioni da mostrare e NoticeRef deve nominare un'organizzazione e identificare per numeri "
            "un gruppo di dichiarazioni testuali. Se la specifica tecnica e' identificata da un OID, "
            "l'elemento Identifier figlio deve contenere un URN che lo codifica (IETF RFC 3061) e "
            "l'attributo QualifierType deve essere presente con valore \"OIDAsURN\"; se e' identificata da "
            "un URI, Identifier contiene quell'URI e QualifierType non deve essere presente."
        ),
        "testo_integrale": (
            """Semantics: Three qualifiers for the signature policy have been identified so far:

  •   A URL where a copy of the signature policy document can be obtained (SPURI element, defined in the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#).

  •   A user notice that should be displayed when the signature is validated (SPUserNotice element, defined in the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#).

  •   An identifier of the technical specification that defines the syntax used for producing the signature policy document (SPDocSpecification element, defined in the namespace whose URI is http://uri.etsi.org/01903/v1.4.1#).

Syntax: The SPURI and SPUserNotice elements shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1, and are copied below for information:

NOTE 1: These elements are defined within the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="SPURI" type="xsd:anyURI"/>
<xsd:element name="SPUserNotice" type="SPUserNoticeType"/>

<xsd:complexType name="SPUserNoticeType">
  <xsd:sequence>
    <xsd:element name="NoticeRef" type="NoticeReferenceType"
      minOccurs="0"/>
    <xsd:element name="ExplicitText" type="xsd:string"
      minOccurs="0"/>
  </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="NoticeReferenceType">
  <xsd:sequence>
    <xsd:element name="Organization" type="xsd:string"/>
    <xsd:element name="NoticeNumbers" type="IntegerListType"/>
  </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="IntegerListType">
  <xsd:sequence>
    <xsd:element name="int" type="xsd:integer" minOccurs="0"
      maxOccurs="unbounded"/>
  </xsd:sequence>
</xsd:complexType>

The SPURI element shall contain a URL value where a copy of the signature policy document can be obtained.

NOTE 2: This URL can reference, for instance, a remote site (which can be managed by an entity entitled for this purpose) from where (signing/validating) applications can retrieve the signature policy document.

The SPUserNotice element shall contain information that is intended for being displayed whenever the signature is validated.

The ExplicitText element shall contain the text of the notice to be displayed.

NOTE 3: Other notices can come from the organization issuing the signature policy.

The NoticeRef element shall name an organization and shall identify by numbers (NoticeNumbers element) a group of textual statements prepared by that organization, so that the application could get the explicit notices from a notices file.

The SPDocSpecification shall identify the technical specification that defines the syntax used for producing the signature policy document.

The SPDocSpecification shall be defined as in XML Schema file "1913201-XAdES01903v141.xsd", whose location is detailed in clause C.2, and is copied below for information.

NOTE 4: This element is defined within the namespace whose URI is http://uri.etsi.org/01903/v1.4.1#.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.4.1#"

The preamble of the XML Schema file also includes the following namespace declaration:
  xmlns:xades="http://uri.etsi.org/01903/v1.3.2#",
which assigns the prefix "xades" to the namespace whose URI is shown in the declaration.
-->

<xsd:element name="SPDocSpecification" type="xades:ObjectIdentifierType"/>

If the technical specification is identified using an OID, then the Identifier child shall contain a URN encoding this OID as specified in IETF RFC 3061 [8], and its QualifierType attribute shall be present with its value set to "OIDAsURN".

If the technical specification is identified using a URI, then the Identifier child shall contain this URI and its QualifierType attribute shall not be present.

NOTE 5: This qualifier allows identifying whether the signature policy document is human readable, XML encoded, or ASN.1 encoded, by identifying the specific technical specifications where these formats will be defined."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.10 (The SignaturePolicyStore qualifying property)",
        "testo": (
            "La property deve essere una qualifying property non firmata che qualifica la firma e deve "
            "contenere o il documento di politica di firma referenziato nella qualifying property "
            "SignaturePolicyIdentifier (cosi' che possa essere usato per la validazione offline e a lungo "
            "termine) o un URI che referenzia uno store locale da cui il documento puo' essere recuperato. "
            "SignaturePolicyDocument deve contenere la politica di firma codificata in base 64, "
            "SigPolDocLocalURI ha come valore l'URI di uno store locale (a differenza di SPURI, un file "
            "locale) e SPDocSpecification deve identificare la specifica tecnica che definisce la sintassi "
            "del documento di politica."
        ),
        "testo_integrale": (
            """Semantics: The SignaturePolicyStore qualifying property shall be an unsigned qualifying property qualifying the signature.

The SignaturePolicyStore qualifying property shall contain either:

  •   the signature policy document which is referenced in the SignaturePolicyIdentifier qualifying property so that the signature policy document can be used for offline and long-term validation; or

  •   a URI referencing a local store where the signature policy document can be retrieved.

Syntax: The SignaturePolicyStore shall be defined as in XML Schema file "1913201-XAdES01903v141.xsd", whose location is detailed in clause C.2, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.4.1#" -->

<xsd:element name="SignaturePolicyStore" type="SignaturePolicyStoreType"/>

<xsd:complexType name="SignaturePolicyStoreType">
    <xsd:sequence>
        <xsd:element ref="SPDocSpecification"/>
        <xsd:choice>
            <xsd:element name="SignaturePolicyDocument" type="xsd:base64Binary"/>
            <xsd:element name="SigPolDocLocalURI" type="xsd:anyURI"/>
        </xsd:choice>
    </xsd:sequence>
    <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

The SignaturePolicyDocument element shall contain the base-64 encoded signature policy.

The SigPolDocLocalURI element shall have as value the URI referencing a local store where the present document can be retrieved.

NOTE 1: Contrary to the SPURI, the SigPolDocLocalURI points to a local file.

The SPDocSpecification element shall identify the technical specification that defines the syntax used for producing the signature policy document.

NOTE 2: It is the responsibility of the entity incorporating the signature policy to the signature-policy-store to make sure that the correct document is securely stored.

NOTE 3: Being an unsigned qualifying property, it is not protected by the digital signature. If the SignaturePolicyIdentifier qualifying property is incorporated into the signature and contains the SigPolicyHash element with the digest value of the signature policy document, any alteration of the signature policy document present within SignaturePolicyStore or within a local store, would be detected by the failure of the digests comparison."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.3 (The SignatureTimeStamp qualifying property)",
        "testo": (
            "La property deve essere una qualifying property non firmata che qualifica la firma e deve "
            "incapsulare una o piu' marche temporali che marcano l'elemento ds:SignatureValue. Per generarla "
            "si usa il meccanismo implicito e l'input del calcolo dell'impronta della marca temporale e' "
            "costruito prendendo l'elemento ds:SignatureValue con il suo contenuto e canonicalizzandolo come "
            "in clausola 4.5."
        ),
        "testo_integrale": (
            """Semantics: The SignatureTimeStamp qualifying property shall be an unsigned qualifying property qualifying the signature.

The SignatureTimeStamp qualifying property shall encapsulate one or more electronic time-stamps time-stamping the ds:SignatureValue element.

Syntax: The SignatureTimeStamp qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="SignatureTimeStamp" type="XAdESTimeStampType"/>

The Implicit mechanism shall be used for generating this qualifying property.

The input to the electronic time-stamp's message imprint computation shall be built as indicated below:

1) take the ds:SignatureValue element and its contents; and

2) canonicalize it as specified in clause 4.5."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.4.2 (The CertificateValues qualifying property)",
        "testo": (
            "La property deve essere una qualifying property non firmata che qualifica la firma e deve "
            "contenere il certificato dell'anchor di fiducia (se esiste e non e' presente in ds:KeyInfo), i "
            "certificati di CA del percorso del certificato di firma non presenti in ds:KeyInfo, il "
            "certificato di firma se non presente in ds:KeyInfo e i certificati usati per firmare le "
            "informazioni sullo stato di revoca (CRL o risposte OCSP) dei certificati precedenti e dei loro "
            "percorsi; i valori di certificato gia' presenti nella firma, compresi quelli dentro le "
            "informazioni di revoca, non dovrebbero essere inclusi. Non deve contenere certificati di CA "
            "che appartengono esclusivamente ai percorsi di certificati usati per firmare attestati di "
            "attributo, assertion firmate in SignerRoleV2 o marche temporali, e puo' contenere l'insieme di "
            "certificati necessari a validare le controfirme non presenti altrove nella firma. "
            "EncapsulatedX509Certificate deve contenere la codifica base 64 di un certificato X.509 "
            "codificato in DER; OtherCertificate e' un segnaposto per futuri formati di certificato."
        ),
        "testo_integrale": (
            """Semantics: The CertificateValues qualifying property shall be an unsigned qualifying property qualifying the signature.

The CertificateValues qualifying property:

1) Shall contain the certificate of the trust anchor, if such certificate does exist and if it is not present within the ds:KeyInfo. If this certificate is present within the ds:KeyInfo, it should not be included.

2) Shall contain the CA certificates within the signing certificate path that are not present within the ds:KeyInfo. The certificates present within ds:KeyInfo element should not be included.

3) Shall contain the signing certificate if it is not present within the ds:KeyInfo. If this certificate is present within the ds:KeyInfo, it should not be included.

4) Shall contain certificates used to sign revocation status information (e.g. CRLs or OCSP responses) of certificates in 1), 2), and 3), and certificates within their respective certificate paths that are not present in the signature. Certificate values present within the signature, including certificate values within the revocation status information themselves should not be included.

5) Shall not contain CA certificates that pertain exclusively to the certificate paths of certificates used to sign attribute certificates or signed assertions within SignerRoleV2, or electronic time-stamps. And

6) May contain a set of certificates used to validate any countersignature incorporated into the XAdES signature that are not present in other elements of the XAdES signature or its countersignatures. This set may include any of the certificates listed in 1), 2), 3) and 4) referred to signing certificates of countersignatures instead of the signing certificate of the XAdES signature. The certificates present elsewhere in the XAdES signature or its countersignatures should not be included.

Syntax: The CertificateValues qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="CertificateValues" type="CertificateValuesType"/>

<xsd:complexType name="CertificateValuesType">
    <xsd:choice minOccurs="0" maxOccurs="unbounded">
        <xsd:element name="EncapsulatedX509Certificate"
          type="EncapsulatedPKIDataType"/>
        <xsd:element name="OtherCertificate" type="AnyType"/>
    </xsd:choice>
    <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

The EncapsulatedX509Certificate element shall contain the base-64 encoding of a DER-encoded X.509 certificate.

The OtherCertificate element is a placeholder for potential future new formats of certificates.

NOTE: If XML electronic time-stamps based in XMLDSIG are standardized and spread, this type can also be used to contain the certification chain for any TSUs providing such electronic time-stamps, if these certificates are not already present in the electronic time-stamps themselves as part of the TSUs' signatures. In this case, an element of this type can be added as an unsigned property to the XML electronic time-stamp using the incorporation mechanisms defined in the present document."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.4.3 (The RevocationValues qualifying property)",
        "testo": (
            "La property deve essere una qualifying property non firmata che qualifica la firma e deve "
            "contenere i valori di revoca corrispondenti ai certificati di CA del percorso del certificato "
            "di firma non presenti in ds:KeyInfo (mai un valore di revoca per l'anchor di fiducia) e il "
            "valore di revoca del certificato di firma se non presente in ds:KeyInfo; puo' contenere i "
            "valori di revoca dei certificati usati per firmare le CRL o le risposte OCSP dei precedenti e "
            "i valori di revoca del certificato di firma di eventuali controfirme con i certificati di CA "
            "del suo percorso, mentre i valori gia' presenti in ds:KeyInfo o in altri elementi della firma "
            "non dovrebbero essere inclusi. Non deve contenere valori di revoca di certificati di CA che "
            "appartengono esclusivamente ai percorsi di certificati usati per firmare attestati di "
            "attributo, assertion firmate in SignerRoleV2 o marche temporali. CRLValues deve contenere la "
            "sequenza di CRL X.509 codificate (ogni EncapsulatedCRLValue in base 64 DER, con l'insieme di "
            "CRL necessarie se ci sono Delta CRL) e OCSPValues la sequenza di risposte OCSP codificate "
            "(EncapsulatedOCSPValue base 64 di un OCSPResponse DER come definito in IETF RFC 6960); "
            "OtherValues e' un segnaposto per altre informazioni di revoca, fuori dall'ambito del documento."
        ),
        "testo_integrale": (
            """Semantics: The RevocationValues qualifying property shall be an unsigned qualifying property that qualifies the signature.

The RevocationValues qualifying property:

1) Shall contain revocation values corresponding to CA certificates within the signing certificate path if they are not present within the ds:KeyInfo. It shall not contain a revocation value for the trust anchor. The revocation values present within ds:KeyInfo element should not be included.

2) Shall contain a revocation value for the signing certificate if it is not present within the ds:KeyInfo. If it is present within ds:KeyInfo element, it should not be included.

3) May contain revocation values corresponding to certificates used to sign CRLs or OCSP responses of 1) and 2), and certificates within their respective certificate paths. The revocation values present within ds:KeyInfo element should not be included.

4) Shall not contain revocation values corresponding to CA certificates that pertain exclusively to the certificate paths of certificates used to sign attribute certificates or signed assertions within SignerRoleV2, or electronic time-stamps. And

5) May contain revocation values corresponding to the signing certificate of any countersignature incorporated into the XAdES signature as well as to the CA certificates in its certificate path. This set may include any of the revocation values listed in 1), 2), and 3) referred to signing certificates of countersignatures instead of the signing certificate of the XAdES signature. However, those revocation values among the aforementioned ones that are already present in other elements of the XAdES signature should not be included.

Syntax: The RevocationValues qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="RevocationValues" type="RevocationValuesType"/>

<xsd:complexType name="RevocationValuesType">
  <xsd:sequence>
    <xsd:element name="CRLValues" type="CRLValuesType"
      minOccurs="0"/>
    <xsd:element name="OCSPValues" type="OCSPValuesType"
      minOccurs="0"/>
    <xsd:element name="OtherValues" type="OtherCertStatusValuesType"
      minOccurs="0"/>
  </xsd:sequence>
  <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

<xsd:complexType name="CRLValuesType">
  <xsd:sequence>
     <xsd:element name="EncapsulatedCRLValue"
       type="EncapsulatedPKIDataType"
       maxOccurs="unbounded"/>
  </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="OCSPValuesType">
  <xsd:sequence>
      <xsd:element name="EncapsulatedOCSPValue"
        type="EncapsulatedPKIDataType" maxOccurs="unbounded"/>
  </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="OtherCertStatusValuesType">
  <xsd:sequence>
    <xsd:element name="OtherValue" type="AnyType"
      maxOccurs="unbounded"/>
  </xsd:sequence>
</xsd:complexType>

CRLValues element shall contain a sequence of encoded X.509 CRLs [15].

Each EncapsulatedCRLValue child of CRLValues element shall contain the base-64 encoding of a DER-encoded X.509 CRL [15].

If the validation data contain one or more Delta CRLs, the CRLValues element shall contain the set of CRLs required to provide complete revocation lists.

OCSPValues element shall contain a sequence of encoded OCSP responses [6].

Each EncapsulatedOCSPValue child of OCSPValues element shall contain the base-64 encoding of a DER-encoded OCSPResponse defined in IETF RFC 6960 [6].

The OtherValues element provides a placeholder for other revocation information that can be used in the future. Their semantics and syntax are outside the scope of the present document.

NOTE: If XML electronic time-stamps based in XMLDSIG are standardized and spread, this type can also serve to contain the values of revocation data including CRLs and OCSP responses for any TSUs providing such electronic time-stamps, if they are not already present in the electronic time-stamps themselves as part of the TSUs' signatures. In this case, an element of this type can be added as an unsigned property to the XML electronic time-stamp using the incorporation mechanisms defined in the present document."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.4.4 (The AttrAuthoritiesCertValues qualifying property)",
        "testo": (
            "La property deve essere una qualifying property non firmata che qualifica la firma e deve "
            "contenere i valori dei certificati di firma degli attestati di attributo e delle assertion "
            "firmate incorporati nella firma XAdES (requirement 1) e, se non gia' presenti nella firma, i "
            "valori dei certificati degli anchor di fiducia e i certificati di CA nei percorsi di quei "
            "certificati di firma (requirement 2); puo' contenere i valori di certificato usati per firmare "
            "le CRL o le risposte OCSP di quei percorsi (requirement 3). I valori di certificato gia' "
            "presenti nella firma, compresi quelli dentro le informazioni di revoca, non dovrebbero essere "
            "inclusi. La sintassi e' quella del tipo CertificateValuesType."
        ),
        "testo_integrale": (
            """Semantics: The AttrAuthoritiesCertValues qualifying property shall be an unsigned qualifying property that qualifies the signature.

The AttrAuthoritiesCertValues qualifying property:

1) shall contain the value(s) of the signing certificate(s) of the attribute certificate(s) and signed assertion(s) incorporated into the XAdES signature;

2) shall contain, if not present within the signature, the value(s) of the certificate(s) for the trust anchor(s) if such certificates exist, and the CA certificate values within path of the signing certificate(s) of the attribute certificate(s) and signed assertion(s) incorporated into the XAdES signature. Certificate values present within the signature should not be included; and

3) may contain the certificate values used to sign CRLs or OCSP responses and the certificates values within their respective certificate paths, used for validating the signing certificate(s) of the attribute certificate(s) and signed assertion(s) incorporated into the XAdES signature. Certificate values present within the signature, including certificate values within the revocation status information themselves should not be included.

Syntax: The AttrAuthoritiesCertValues qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="AttrAuthoritiesCertValues" type="CertificateValuesType"/>"""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.4.5 (The AttributeRevocationValues qualifying property)",
        "testo": (
            "La property deve essere una qualifying property non firmata che qualifica la firma e deve "
            "contenere i valori di revoca dei certificati che firmano gli attestati di attributo e le "
            "assertion firmate incorporati nella firma XAdES (requirement 1) e, se non gia' incorporati "
            "nella firma, i valori di revoca corrispondenti ai certificati di CA nei percorsi di quei "
            "certificati di firma, mai valori di revoca per gli anchor di fiducia (requirement 2); puo' "
            "contenere i valori di revoca dei certificati usati per firmare le CRL o le risposte OCSP di "
            "quei percorsi (requirement 3). I valori gia' incorporati nella firma non dovrebbero essere "
            "inclusi. Se i dati di validazione contengono una o piu' Delta CRL, la property deve includere "
            "l'insieme di CRL necessario a fornire elenchi di revoca completi."
        ),
        "testo_integrale": (
            """Semantics: The AttributeRevocationValues qualifying property shall be an unsigned qualifying property that qualifies the signature.

The AttributeRevocationValues qualifying property:

1) shall contain the revocation value(s) of the certificate(s) that sign the attribute certificate(s) and signed assertion(s) incorporated into the XAdES signature;

2) shall contain, if not incorporated into the signature, the revocation values corresponding to CA certificates within the path(s) of the signing certificate(s) of the attribute certificate(s) and signed assertion(s) incorporated into the XAdES signature. It shall not contain revocation values for the trust anchors. Values already incorporated into the signature should not be included; and

3) may contain the revocation values on certificates used to sign CRLs or OCSP responses and certificates within their respective certificate paths, which are used for validating the signing certificate(s) of the attribute certificate(s) and signed assertion(s) incorporated into the XAdES signature. Revocation values already incorporated into the signature should not be included.

Syntax: The AttributeRevocationValues qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v132.xsd", whose location is detailed in clause C.1 and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.3.2#" -->

<xsd:element name="AttributeRevocationValues" type="RevocationValuesType"/>

If the validation data contain one or more Delta CRLs, this qualifying property shall include the set of CRLs required to provide complete revocation lists."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.4.6 (The AnyValidationData qualifying property)",
        "testo": (
            "La property deve essere una qualifying property non firmata che qualifica la firma e deve "
            "contenere i valori di certificato usati per validare qualunque firma digitale presente in "
            "qualunque altro componente della firma XAdES, senza restrizioni sugli oggetti firmati "
            "(comprese firma, controfirme, marche temporali, attestati di attributo, assertion firmate, "
            "risposte OCSP e CRL) oppure i valori di revoca dei certificati che sostengono quelle firme, o "
            "entrambi. L'elemento figlio CertificateValues deve contenere i certificati usati nella "
            "validazione (in base 64 DER) e RevocationValues i valori di revoca con la sintassi della "
            "clausola 5.4.3, con l'insieme di CRL necessarie se ci sono Delta CRL; entrambi non dovrebbero "
            "comparire altrove nella firma. L'attributo Id serve a referenziare l'elemento da altrove e "
            "l'attributo URI non deve essere presente."
        ),
        "testo_integrale": (
            """Semantics: The AnyValidationData qualifying property shall be an unsigned qualifying property that qualifies the signature.

The AnyValidationData qualifying property shall contain the certificates identified in 1), or the revocation data identified in 2), or both of them:

1) certificate values that are used for validating any digital signature present within any other component of the XAdES signature regardless of the objects that they are signing (these can be, for instance, the digital signature value within the ds:Signature element itself, any countersignature of the XAdES signature, or the digital signatures within any electronic time-stamp, attribute certificate, signed assertion, OCSP response, or CRL, or any other digital signature), without any restrictions.

2) revocation value(s) of the certificate(s) supporting any signature present within any other component of the XAdES signature mentioned in the previous bullet.

NOTE 1: This property allows to mimic, within XAdES, features already incorporated in PAdES and CAdES, namely: an unsigned qualifier property whose purpose is to contain certificates and validation material that can be used for validating any signature present within XAdES signatures, regardless of what these signatures are signing.

NOTE 2: This property also allows to properly deal with situations where different creation/validation/augmentation signature policies can be used. They, for instance, may establish different requirements on acceptable freshness of revocation material, and also allow different certificate paths. Therefore, a certain set of revocation data fully acceptable for a certain policy A, may be unacceptable, from the point of view of its freshness, for another policy B. Also a verifier can accept a different certificate path. This unsigned qualifying property allows, for instance, including within a XAdES signature a set of revocation data whose freshness is acceptable for this last policy B, making the signature valid under both policies.

Syntax: The AnyValidationData qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v141.xsd", whose location is detailed in clause C.2, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.4.1#"

The preamble of the XML Schema file also includes the following namespace declaration:
  xmlns:xades="http://uri.etsi.org/01903/v1.3.2#",
which assigns the prefix "xades" to the namespace whose URI is shown in the declaration.
-->

<xsd:element name="AnyValidationData" type="ValidationDataType"/>

<xsd:complexType name="ValidationDataType">
    <xsd:sequence>
        <xsd:element ref="xades:CertificateValues" minOccurs="0"/>
        <xsd:element ref="xades:RevocationValues" minOccurs="0"/>
    </xsd:sequence>
    <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
    <xsd:attribute name="URI" type="xsd:anyURI" use="optional"/>
</xsd:complexType>

The CertificateValues child element shall contain the base-64 encoding of DER-encoded X.509 certificates used in the validation of the XAdES signature, as mentioned in bullet 1) of the semantics specification. These certificates should not appear anywhere else within the XAdES signature.

The RevocationValues child element shall contain revocation values used in the validation of the XAdES signature, as mentioned in bullet 2) of the semantics specification. Its syntax shall be as specified in clause 5.4.3 of the present document. These revocation values should not appear anywhere else within the XAdES signature. If the validation data contain one or more Delta CRLs, this child element shall include the set of CRLs required to provide complete revocation lists.

The Id attribute shall be used for referencing this element from elsewhere.

The AnyValidationData qualifying property shall not have the URI attribute.

NOTE 3: The URI attribute can be used within TimeStampValidationData unsigned qualifying property (see clause 5.5.1.2 of the present document for details)."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.1.1 (Semantics and syntax)",
        "testo": (
            "La property deve essere una qualifying property non firmata che qualifica la firma e deve fare "
            "da contenitore dei dati di validazione richiesti per una verifica completa delle marche "
            "temporali incapsulate in una qualunque delle property contenitore di marche temporali definite "
            "dal documento; puo' incorporare valori di certificato e valori di revoca. L'elemento figlio "
            "CertificateValues deve contenere i certificati usati nella verifica completa delle marche "
            "temporali incapsulate in un contenitore di marche temporali XAdES, e puo' contenerli tutti o "
            "solo quelli non presenti altrove nella firma (per esempio nella marca temporale stessa o in "
            "altre TimeStampValidationData); lo stesso vale per RevocationValues rispetto ai valori di "
            "revoca. L'attributo Id serve a referenziare l'elemento da altrove e l'attributo URI, "
            "facoltativo, deve essere usato per referenziare il contenitore delle marche temporali di cui "
            "la property porta i dati di validazione."
        ),
        "testo_integrale": (
            """Semantics: The TimeStampValidationData qualifying property shall be an unsigned qualifying property qualifying the signature.

The TimeStampValidationData qualifying property shall be a container for validation data required for carrying a full verification of the electronic time-stamps embedded within any of the different electronic time-stamp container qualifying properties defined in the present document.

The TimeStampValidationData qualifying property shall allow incorporating certificate values.

The TimeStampValidationData qualifying property shall allow incorporating revocation values.

Syntax: The TimeStampValidationData qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v141.xsd", whose location is detailed in clause C.2, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.4.1#"

The preamble of the XML Schema file also includes the following namespace declaration:
  xmlns:xades="http://uri.etsi.org/01903/v1.3.2#",
which assigns the prefix "xades" to the namespace whose URI is shown in the declaration.
-->

<xsd:element name="TimeStampValidationData" type="ValidationDataType"/>

The CertificateValues child element shall contain certificates used in the full verification of electronic time-stamps embedded in one XAdES time-stamp container.

The CertificateValues child element may contain all the certificates required for a full verification of the electronic time-stamps.

The CertificateValues child element may also contain only some of the certificate values if the rest are present elsewhere in the XAdES signature (for instance within the electronic time-stamp itself, or in other TimeStampValidationData created for other electronic time-stamps).

The RevocationValues child element shall contain revocation values used in the full verification of electronic time-stamps embedded in one XAdES time-stamp container.

The RevocationValues child element may contain all the revocation values required for a full verification of the electronic time-stamps.

The RevocationValues child element may also contain only some of the revocation values if the rest are present elsewhere in the XAdES signature (for instance within the electronic time-stamp itself, or in other TimeStampValidationData created for other electronic time-stamps).

The Id attribute shall be used for referencing this element from elsewhere.

The TimeStampValidationData qualifying property may have the URI attribute. This attribute shall be used for referencing the time-stamp container of the electronic time-stamps whose validation data is contained within this element."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.1.2 (Use of URI attribute)",
        "testo": (
            "Se una firma XAdES richiede di includere tutti i dati di validazione necessari alla verifica "
            "completa di una marca temporale incapsulata in una property SignatureTimeStamp, "
            "RefsOnlyTimeStampV2, SigAndRefsTimeStampV2 o ArchiveTimeStamp (namespace 1.4.1) e parte di "
            "questi dati non e' presente altrove nella firma, occorre creare una nuova "
            "TimeStampValidationData con i dati mancanti, aggiungerla come figlio di "
            "UnsignedSignatureProperties subito dopo il contenitore della marca temporale e, se non e' "
            "incorporata immediatamente dopo (solo con incorporamento indiretto), valorizzare l'attributo "
            "URI verso il contenitore specifico, altrimenti l'URI non dovrebbe essere presente. Per le "
            "marche temporali in IndividualDataObjectsTimeStamp o AllDataObjectTimeStamp la nuova property "
            "va aggiunta come primo figlio di UnsignedSignatureProperties e l'attributo URI deve essere "
            "presente e referenziare il contenitore firmato. In convalida, se la property segue "
            "immediatamente uno dei contenitori elencati e il valore dell'URI non referenzia il contenitore "
            "che la precede, il valore dell'URI deve essere ignorato; se invece non segue immediatamente un "
            "contenitore e il valore dell'URI non referenzia una property contenitore di marche temporali, "
            "l'applicazione deve ignorare quel valore e puo' tentare di usare il materiale di validazione "
            "presente nella TimeStampValidationData per validare le diverse marche temporali incorporate "
            "nella firma."
        ),
        "testo_integrale": (
            """If a XAdES signature requires including all the validation data required for a full verification of an electronic time-stamp embedded in a SignatureTimeStamp, a RefsOnlyTimeStampV2, a SigAndRefsTimeStampV2, or an ArchiveTimeStamp qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.4.1#, and part of that validation data is not present in other parts of the signature, then:

1) a new TimeStampValidationData qualifying property shall be created containing the missing validation data;

2) if direct incorporation as specified in clause 4.4 of the present document is used, the TimeStampValidationData qualifying property shall be added as a child of UnsignedSignatureProperties element immediately after the respective electronic time-stamp container element;

3) if the TimeStampValidationData qualifying property is not incorporated immediately after the respective electronic time-stamp container element (this may only happen when indirect incorporation of properties as specified in clause 4.4 is used), then the URI attribute shall be present and shall reference the specific container encapsulating the electronic time-stamps whose validation data the new TimeStampValidationData qualifying property will contain; otherwise the URI attribute should not be present.

NOTE 1: In the case that the TimeStampValidationData qualifying property is incorporated immediately after the respective electronic time-stamp container element, the URI attribute is not needed because the identification of the related electronic time-stamp container is implicit in the relative position of both elements, the qualifying property containing the electronic time-stamp and the TimeStampValidationData qualifying property.

If a XAdES signature requires including all the validation data required for a full verification of an electronic time-stamp embedded in any of the following qualifying properties containing electronic time-stamps: IndividualDataObjectsTimeStamp or AllDataObjectTimeStamp, and part of that validation data is not present in other parts of the signature, then:

1) a new TimeStampValidationData qualifying property shall be created containing the missing validation data;

2) it shall be added as the first child of the UnsignedSignatureProperties element; and

3) the URI attribute element shall be present and shall reference the specific signed container encapsulating the electronic time-stamps whose validation data the new TimeStampValidationData qualifying property will contain.

NOTE 2: The treatment is different than for the other electronic time-stamp containers because first, there can be more than one signed electronic time- stamp container, and second IndividualDataObjectsTimeStamp and AllDataObjectTimeStamp are signed qualifying properties whereas the corresponding TimeStampValidationData qualifying properties are unsigned and they appear as children of different parents.

When validating a XAdES signature, in the case that the TimeStampValidationData qualifying property appears immediately after one of the following qualifying properties containing electronic time-stamps: SignatureTimeStamp, RefsOnlyTimeStampV2, SigAndRefsTimeStampV2, and ArchiveTimeStamp qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.4.1#, regardless of whether direct or indirect incorporation is used, if the value in URI attribute does not reference the electronic time-stamps container that precedes the TimeStampValidationData qualifying property, this URI attribute's value shall be ignored.

When validating a XAdES signature, in the case that the TimeStampValidationData qualifying property does not appear immediately after one qualifying property containing electronic time-stamps, if the value of URI attribute does not reference a qualifying property containing electronic time-stamps, then the application shall ignore this value and may try to use the validation material within the TimeStampValidationData in the validation of the different electronic time-stamps incorporated to the signature.

NOTE 3: This behaviour is coherent with the fact of considering the value of the URI attribute as a hint that may help signature validation applications to establish a correspondence between the signing certificate of a certain electronic time-stamp and part of its validation data. However, applications can also establish this correspondence without the help of such an URI, and consequently, if the value of the URI attribute is wrong, still the material may correspond to some of the electronic time-stamps incorporated into the signature, and signature validation applications would be able to successfully use that material in the validation of the aforementioned electronic time-stamps."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.5.2.1 (Semantics and syntax)",
        "testo": (
            "La property deve essere una qualifying property non firmata che qualifica la firma e deve "
            "incapsulare marche temporali calcolate su tutti gli oggetti incorporati nella firma XAdES al "
            "momento di generare ciascuna marca temporale, con lo scopo di affrontare la disponibilita' e "
            "l'integrita' a lungo termine del materiale di validazione. Se la firma XAdES incorpora una "
            "CounterSignature non firmata, tutto il materiale necessario a condurre la validazione della "
            "controfirma deve essere incorporato nella firma prima di generare la prima ArchiveTimeStamp "
            "(nella controfirma stessa o nei contenitori della firma controfirmata) e il contenuto della "
            "CounterSignature non dovrebbe essere modificato una volta marcato temporalmente. Il contenuto "
            "della property puo' essere diverso a seconda che le property non firmate marcate e la "
            "ArchiveTimeStamp stessa abbiano o no lo stesso genitore (clausole 5.5.2.3 e 5.5.2.4)."
        ),
        "testo_integrale": (
            """Semantics: The ArchiveTimeStamp qualifying property shall be an unsigned qualifying property qualifying the signature.

The ArchiveTimeStamp qualifying property shall encapsulate electronic time-stamps computed on all the data objects incorporated into the XAdES signature at the time of generating each electronic time-stamp.

NOTE 1: The purpose of this element is to tackle the long term availability and integrity of the validation material.

Syntax: The ArchiveTimeStamp qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v141.xsd", whose location is detailed in clause C.2, and is copied below for information.
<!-- targetNamespace="http://uri.etsi.org/01903/v1.4.1#"

The preamble of the XML Schema file also includes the following namespace declaration:
  xmlns:xades="http://uri.etsi.org/01903/v1.3.2#",
which assigns the prefix "xades" to the namespace whose URI is shown in the declaration.
-->

<xsd:element name="ArchiveTimeStamp" type="xades:XAdESTimeStampType"/>

If the XAdES signature incorporates a CounterSignature unsigned qualifying property, all the required material for conducting the validation of the counter-signature shall be incorporated into the XAdES signature before generating the first ArchiveTimeStamp qualifying property. This may be done within the counter-signature itself or within the containers available within the counter-signed XAdES signature.

The contents of the CounterSignature qualifying property should not be changed, once it has been time-stamped by the ArchiveTimeStamp.

NOTE 2: If a CounterSignature qualifying unsigned property is time-stamped by the ArchiveTimeStamp, any ulterior change of their contents (by addition of unsigned qualifying properties if the counter-signature is a XAdES signature, for instance) would make the validation of the ArchiveTimeStamp and, in consequence, the validation of the countersigned XAdES signature, fail.

NOTE 3: Under these circumstances, the detached counter-signature mechanism specified in clause 5.2.7.1 can be used.

NOTE 4: The present document permits counter-signing a previously time-stamped countersignature with another CounterSignature qualifying property added to the embedding XAdES signature after the time-stamp container.

NOTE 5: Once an ArchiveTimeStamp qualifying property is added to the signature, any ulterior addition of a ds:Object to the signature would make the verification of such time-stamp fail.

Depending whether all the unsigned qualifying properties time-stamped by the electronic time-stamp and the ArchiveTimeStamp qualifying property itself have the same parent or not, its contents may be different. Details are given in clauses 5.5.2.3 and 5.5.2.4."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.2 (Generation and incorporation of ArchiveTimeStamp)",
        "testo": (
            "Per aumentare una firma XAdES incorporando una nuova ArchiveTimeStamp si devono seguire sei "
            "passi: 1) aggiungere i certificati e/o i dati di revoca mancanti per validare gli oggetti "
            "firmati prima di generare le marche temporali da incapsulare (collocandoli in una qualunque "
            "property XAdES della clausola 5.4, rispettandone i requisiti); 2) calcolare l'impronta delle "
            "nuove marche secondo la clausola 5.5.2.3 se le property non firmate marcate non sono "
            "distribuite, altrimenti secondo la clausola 5.5.2.4; 3) richiedere le marche temporali "
            "necessarie ai corrispondenti fornitori di servizi di marca temporale; 4) costruire la nuova "
            "ArchiveTimeStamp incapsulando le marche emesse; 5) incorporarla come nuova property non "
            "firmata della firma XAdES; 6) nel caso distribuito, incorporare dentro la nuova "
            "ArchiveTimeStamp un elemento Include per ogni property non firmata marcata, nello stesso "
            "ordine in cui le property referenziate sono state processate per costruire l'input del calcolo "
            "dell'impronta."
        ),
        "testo_integrale": (
            """For augmenting a XAdES signature by incorporation of a new ArchiveTimeStamp qualifying property, the following steps shall be performed:

1) If the XAdES signature misses certificates and/or revocation data required for validating the signed objects present in the XAdES signature, then these missing certificates and/or revocation data shall be added before generating the electronic time-stamp(s) to be encapsulated by the new ArchiveTimeStamp qualifying property.

    Any missing certificate and/or revocation data may be placed in any XAdES qualifying property specified in clause 5.4 as long as the specific requirements defined for each qualifying property are met.

2) If the new ArchiveTimeStamp qualifying property has to be incorporated to the XAdES signature in such a way that all the unsigned qualifying properties time-stamped by the electronic time-stamp(s) encapsulated within this ArchiveTimeStamp element have the same parent (time-stamped unsigned qualifying properties are not distributed), then compute the message imprint for the new electronic time-stamp(s), as indicated in clause 5.5.2.3; otherwise (time-stamped unsigned qualifying properties are distributed) compute the message imprint for the new electronic time-stamp(s) as indicated in clause 5.5.2.4.

NOTE: Notice that, while the ArchiveTimeStamp element has not been yet created at this point in time, the decision of where to incorporate it to the XAdES signature, once created and built, has already been made, and therefore, which clause to follow for building the input to the message imprint computation, is also known.

3) Request as many electronic time-stamp(s) as required to the corresponding electronic time-stamp Service Providers.

4) Build a new ArchiveTimeStamp qualifying property, encapsulating the electronic time-stamp(s) issued in the previous step.

5) Incorporate the new ArchiveTimeStamp qualifying property generated in the previous step as a new unsigned qualifying property of the XAdES signature.

6) If after its incorporation to XAdES signature, this ArchiveTimeStamp qualifying property and some of the unsigned qualifying properties time-stamped by its electronic electronic time-stamp(s) do not have the same parent (distributed case), then incorporate within this ArchiveTimeStamp qualifying property one Include element for each time-stamped unsigned qualifying property, referencing this qualifying property. These Include elements shall be incorporated in the same order as the referenced unsigned qualifying properties have been processed to build the input to the message imprint computation (see clause 5.5.2.4)."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 5.4.1 (Introduction)",
        "testo": (
            "Introduzione alla clausola 5.4: il presente documento specifica semantica e sintassi delle "
            "qualifying property XAdES che racchiudono certificati e/o dati di revoca. Una firma XAdES "
            "puo' contenere certificati e/o dati di revoca in una qualunque delle qualifying property "
            "specificate in questa clausola 5.4, a condizione che siano rispettati i requisiti specifici "
            "definiti per ciascuna property. Disposizione dichiarativa di ambito, senza requisito ne' "
            "soggetto obbligato."
        ),
        "testo_integrale": (
            """The present clause specifies the semantics and syntax for XAdES qualifying properties that enclose certificates and/or revocation data.

A XAdES signature may contain certificates and/or revocation data within any of the XAdES qualifying properties specified in this clause 5.4 as long as the specific requirements defined for each qualifying property are met."""
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 5.2.8.2 (The IndividualDataObjectsTimeStamp qualifying property)",
    "clausola 5.2.9.1 (Semantics and syntax)",
    "clausola 5.2.9.2 (Signature policy qualifiers)",
    "clausola 5.2.10 (The SignaturePolicyStore qualifying property)",
    "clausola 5.3 (The SignatureTimeStamp qualifying property)",
    "clausola 5.4.1 (Introduction)",
    "clausola 5.4.2 (The CertificateValues qualifying property)",
    "clausola 5.4.3 (The RevocationValues qualifying property)",
    "clausola 5.4.4 (The AttrAuthoritiesCertValues qualifying property)",
    "clausola 5.4.5 (The AttributeRevocationValues qualifying property)",
    "clausola 5.4.6 (The AnyValidationData qualifying property)",
    "clausola 5.5.1.1 (Semantics and syntax)",
    "clausola 5.5.1.2 (Use of URI attribute)",
    "clausola 5.5.2.1 (Semantics and syntax)",
    "clausola 5.5.2.2 (Generation and incorporation of ArchiveTimeStamp)",
]

# UNA riga per sottoclausta: il riferimento del nodo e' anche il suo item di indice.
MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Tredici rinvii interni al perimetro di questo capitolo (vedi docstring). Nessuna
# relazione verso altri capitoli di questa fonte o verso altre fonti: le partizioni e
# i collegamenti cross-fonte sono costruiti dalla sessione principale in fase 6
# (ADR-0009, ADR-0012).
RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.9.1 (Semantics and syntax)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.9.2 (Signature policy qualifiers)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.10 (The SignaturePolicyStore qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.9.1 (Semantics and syntax)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.10 (The SignaturePolicyStore qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.9.2 (Signature policy qualifiers)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.4 (The AttrAuthoritiesCertValues qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.2 (The CertificateValues qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.5 (The AttributeRevocationValues qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.3 (The RevocationValues qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.6 (The AnyValidationData qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.2 (The CertificateValues qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.6 (The AnyValidationData qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.3 (The RevocationValues qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.6 (The AnyValidationData qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.2 (Use of URI attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.1 (Semantics and syntax)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.2 (The CertificateValues qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.1 (Semantics and syntax)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.3 (The RevocationValues qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.2 (Use of URI attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.8.2 (The IndividualDataObjectsTimeStamp qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.2 (Use of URI attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.3 (The SignatureTimeStamp qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.2 (Use of URI attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.1 (Semantics and syntax)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
]
