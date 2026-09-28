"""ETSI TS 119 612 V2.4.1 (2025-08) - Electronic Signatures and Trust
Infrastructures (ESI); Trusted Lists. Fonte 21 (la numerazione degli id e'
risolta per riferimento dalla sessione principale in app/seed.py - questo
modulo NON tocca seed.py). Capitolo 3: clausola 5.4 TSP information (5.4.1,
5.4.2, 5.4.3.0, 5.4.3.1, 5.4.3.2, 5.4.4, 5.4.5, 5.4.6) e clausole 5.5.1-5.5.8
Service information (5.5.1.0, 5.5.1.1, 5.5.1.2, 5.5.1.3, 5.5.2, 5.5.3, 5.5.4,
5.5.5, 5.5.6, 5.5.7, 5.5.8). Documento unico (non multi-parte): i
`riferimento` NON portano prefisso di Parte. Testo ufficiale in
app/.source_cache/etsi_119_612/cap03.txt (letto sempre con selettore `:raw`,
altrimenti il tool tronca le righe lunghe a 768 caratteri introducendo "..."
e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_119_612/manifest.json.

Modellazione (ADR-0007), criterio gia' applicato alle altre fonti ETSI censite
e adattato alle clausole di uno standard tecnico: un nodo per ogni
clausola/sottoclausola numerata che porta contenuto proprio, nessun nodo per le
intestazioni di puro raggruppamento. Questo capitolo produce 19 Obblighi e 0
Principi su 19 item di indice: sono tutte clausole di campo della trusted list
(TSP information / Service information), ognuna con la quadrupla ufficiale
Presence/Description/Format/Value e, dove presente, requisiti aggiuntivi, NOTE
ed EXAMPLE; la forma enunciativa tipica e' "shall"/"should"/"may" su un
soggetto identificabile (TLSO, TSP, implementazioni), quindi Obbligo secondo il
criterio "lo schema ha un solo tipo prescrittivo" (precedente delle altre fonti
ETSI gia' censite).

Intestazioni di raggruppamento SENZA nodo e SENZA item di indice (il testo
ufficiale passa direttamente dal titolo alla prima sottoclausola, nessuna riga
di testo proprio): 5.4 (TSP information), 5.4.3 (TSP address), 5.5 (Service
information) e 5.5.1 (Service type identifier, che apre direttamente su 5.5.1.0
General requirements).

Scelte voce per voce:
- 5.4.1 (TSP name) -> Obbligo "informativo/trasparenza": nome legale del
  soggetto responsabile dei servizi del TSP riconosciuti dallo scheme, da usare
  nelle registrazioni formali e al quale indirizzare ogni comunicazione
  formale. Nessuna NOTE ufficiale.
- 5.4.2 (TSP trade name) -> Obbligo "informativo/trasparenza": identificatore
  ufficiale di registrazione (struttura VAT/NTR per le persone giuridiche,
  PAS/IDC/PNO/TIN per le persone fisiche, con codice paese ISO 3166-1,
  hyphen-minus e identificatore), allocazione dell'identificatore da parte del
  TLSO quando non ne esiste uno registrato, uso del nome commerciale
  alternativo. La NOTE finale (piu' voci TSP vs una sola voce con contesto
  specifico) e' riportata integralmente.
- 5.4.3.0 (General) -> Obbligo "informativo/trasparenza": campo multi-parte
  (indirizzo postale della clausola 5.4.3.1 + indirizzo elettronico della
  clausola 5.4.3.2) e sostituzione dell'indirizzo in caso di cessazione
  dell'intero insieme dei servizi del TSP.
- 5.4.3.1 (TSP postal address) -> Obbligo "informativo/trasparenza"; formato
  ripreso dalla clausola 5.3.5.1; indirizzo presso cui il TSP fornisce
  assistenza via posta convenzionale.
- 5.4.3.2 (TSP electronic address) -> Obbligo "informativo/trasparenza"; formato
  ripreso dalla clausola 5.3.5.2; email, telefono opzionale e sito web di
  assistenza.
- 5.4.4 (TSP information URI) -> Obbligo "informativo/trasparenza": URI delle
  Practices Statements e/o Policies (es. CPS/CP), GTC, informazioni legali e di
  assistenza, con URI sostitutivo in caso di cessazione.
- 5.4.5 (TSP information extensions) -> Obbligo "tecnico/sicurezza": campo
  opzionale a formato aperto, il cui significato e' definito dalla specifica di
  origine; nel contesto degli Stati membri UE le estensioni informative del TSP,
  quando usate, non devono essere marcate come critical (vincolo tecnico di
  interoperabilita', da cui il tipo).
- 5.4.6 (TSP Services (list of services)) -> Obbligo "procedurale": elenco dei
  servizi con stato di approvazione e relativa storia, almeno un servizio
  elencato e conservazione delle informazioni storiche anche per servizi
  ritirati.
- 5.5.1.0 (General requirements) -> Obbligo "informativo/trasparenza": URI del
  tipo di servizio scelto fra le clausole 5.5.1.1, 5.5.1.2, 5.5.1.3 o altro URI
  registrato e descritto; la NOTE rinvia al portale ETSI per la richiesta di
  object identifier o radice URI.
- 5.5.1.1 (Regulation (EU) No 910/2014 qualified trust service types) ->
  Obbligo "tecnico/sicurezza": registro completo dei tipi qualificati (a)-(m)
  con URI, Description e Requirements; il contenuto prescrittivo
  (identificazione RootCA-QC tramite estensione, elenco separato dei servizi di
  stato di validita' dei certificati, appartenenza o non appartenenza alla
  categoria dei servizi non basati su PKI, divieto di elenco per eredita' per i
  servizi qualificati di marca temporale) e' tecnico, da cui il tipo. La NOTE
  di (a) e' riportata integralmente.
- 5.5.1.2 (Regulation (EU) No 910/2014 non qualified trust service types) ->
  Obbligo "tecnico/sicurezza": registro completo dei tipi non qualificati
  (a)-(x) con URI, Description e Requirements.
- 5.5.1.3 (Trust service types not defined in Regulation (EU) No 910/2014 but
  nationally defined) -> Obbligo "tecnico/sicurezza": registro completo dei tipi
  nazionali (a)-(o), incluse le voci il cui URI termina con "/nothavingPKIid"
  (che ricadono espressamente fra i servizi non basati su PKI) e il tipo
  "unspecified".
- 5.5.2 (Service name) -> Obbligo "informativo/trasparenza": nome con cui il TSP
  fornisce il servizio, in stringhe multilingua.
- 5.5.3 (Service digital identity) -> Obbligo "tecnico/sicurezza": e' la
  clausola piu' densa del capitolo, con 3 EXAMPLE e 5 NOTE ufficiali riportati
  integralmente; vincoli sulle rappresentazioni ammesse della chiave pubblica,
  unicita' della chiave per tipo di servizio, disallineamento dell'attributo
  "O=" rispetto al 'TSP Name' (dichiarazione formale nello 'Scheme service
  definition URI' ed elenco come 'TSP Trade Name'), coerenza del contenuto di
  X509SKI con l'estensione SubjectKeyIdentifier, uso della chiave di una CA
  root o di livello superiore come 'Sdi' e uso degli identificatori di servizio
  come trust anchor.
- 5.5.4 (Service current status) -> Obbligo "informativo/trasparenza": valori di
  stato ammessi per i tipi 5.5.1.1 (granted/withdrawn) e 5.5.1.2-5.5.1.3
  (recognisedatnationallevel/deprecatedatnationallevel), flusso di stati,
  migrazione al 01/07/2016 come da annex J, valori definiti dallo scheme per
  Paesi terzi e organizzazioni internazionali.
- 5.5.5 (Current status starting date and time) -> Obbligo
  "informativo/trasparenza": data e ora UTC di efficacia dello stato corrente,
  coerenza con l'(ri)emissione della trusted list e divieto di retrodatazione.
  La NOTE (uso dell'informazione da parte dei terzi affidanti) e' riportata
  integralmente.
- 5.5.6 (Scheme service definition URI) -> Obbligo "informativo/trasparenza":
  campo opzionale con gli URI delle informazioni di servizio fornite dallo
  scheme operator, inclusi il TSP di fallback e le qualificazioni nazionali.
- 5.5.7 (Service supply points) -> Obbligo "informativo/trasparenza": campo
  opzionale con gli URI di accesso al servizio; l'EXAMPLE ufficiale (testo
  descrittivo, CRL distribution point, responder OCSP) e la NOTE finale sono
  riportati integralmente.
- 5.5.8 (TSP service definition URI) -> Obbligo "informativo/trasparenza":
  presenza obbligatoria solo per il tipo NationalRootCA-QC (clausola 5.5.1.3) e
  opzionale negli altri casi; per quel tipo sono richiesti anche dettagli sulle
  regole di istituzione e gestione dei servizi e la legislazione nazionale
  rilevante.

`testo_integrale` (ADR-0010): testo ufficiale inglese verbatim e completo per
ogni nodo, senza elisioni. Normalizzazione adottata: i wrap fisici di riga
introdotti da `pdftotext -layout` sono sostituiti da uno spazio singolo e ogni
unita' logica (Presence/Description/Format/Value, lettere e numeri romani, voci
di registro URI + Description + Requirement(s), NOTE, EXAMPLE, paragrafi) e'
riportata su una riga a se' stante, eliminando i rientri di pura impaginazione.
Le tre clausole di registro 5.5.1.1/.2/.3 riportano TUTTE le voci della
rispettiva tabella (URI + Description + Requirement(s)), una voce per lettera,
senza perdere alcun valore. Verifica di completezza eseguita in fase di
generazione: il multiset dei token del capitolo ricostruito dai 19
`testo_integrale` coincide con quello del file sorgente a meno dei soli 4
titoli di raggruppamento (13 token) che non generano nodo. La Figura 2 della
clausola 5.5.4 e' un diagramma raster nel PDF ufficiale, non testo estraibile:
nel `testo_integrale` resta la sua didascalia "Figure 2" e nulla e' stato
inventato al suo posto. L'ellissi della clausola 5.5.3 in
"http://uri.etsi.org/TrstSvc/Svctype/.../nothavingPKIid" e' contenuto ufficiale
autentico (radix di URI), riportato verbatim come da ADR-0010.

RELAZIONI: 49 relazioni, tutte interne a ETSI TS 119 612 e tutte
`richiama`/"textual", costruite solo su rinvii testuali puntuali del capitolo
(forma "(see clause X.Y)", "(clause X.Y)", "(as defined in clause D.5)", "as
specified in annex J"). Nessuna relazione cross-fonte in questa fase (fase 6
della sessione principale, ADR-0009). Riferimenti a clausole che NON generano
nodo, e che quindi non producono relazione per non inventare un nodo
inesistente: "Service Information element (see clause 5.5)" e "Service History
Instance elements (see clause 5.6)" in 5.4.6; "Service type identifier (clause
5.5.1)" in 5.5.2, 5.5.3 e 5.5.7; "Qualification extension when applicable (see
clause 5.5.9.2)" in 5.5.1.1 (5.5.9.2 e' intestazione di raggruppamento: il
primo nodo e' 5.5.9.2.0).

Citazioni esterne notate ma NON trasformate in relazioni: Reg. (UE) No 910/2014
[i.10] (incluse le disposizioni da esso definite e l'Annex II dello stesso
Regolamento), Direttiva 1999/93/EC [i.3], Decisione 2009/767/EC [i.2],
XML-Signature [4], ISO 3166-1 [15], i riferimenti [12] (CRL distribution point)
e [i.11] (OCSP) degli EXAMPLE e il rinvio al portale ETSI
(https://portal.etsi.org/PNNS.aspx). I rinvii interni alla Fonte (5.1.3, 5.1.4,
5.3.5.1, 5.3.5.2, 5.3.7, 5.3.10, 5.3.12, 5.3.14, 5.5.9, 5.5.9.4, Annex D.4,
Annex D.5, Annex J) usano le stringhe di `riferimento` confermate dai capitoli
proprietari.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 5.4.1 (TSP name)",
        "testo": (
            "Campo obbligatorio che identifica il nome della persona giuridica, o quando applicabile della persona"
            " fisica, responsabile dei servizi del TSP riconosciuti dallo scheme, in particolare dei servizi"
            " approvati sotto lo scheme applicabile. Il valore deve essere il nome usato nelle registrazioni legali"
            " formali e nei registri ufficiali, al quale indirizzare ogni comunicazione formale, fisica o"
            " elettronica; il formato e' una sequenza di stringhe di caratteri multilingua (clausola 5.1.4). Nessuna"
            " NOTE ufficiale in questa clausola."
        ),
        "testo_integrale": (
            "5.4.1 TSP name: Presence: This field shall be present.\nDescription: It specifies the name of the legal"
            " entity, or when applicable the natural person, responsible for the TSP's services that are or were"
            " recognized by the scheme, in particular for the TSP's services that are or were approved under the"
            " applicable scheme.\nFormat: A sequence of multilingual character strings (see clause 5.1.4).\nValue:"
            " The name of the legal entity, or when applicable the natural person, responsible for the TSP shall be"
            " the name which is used in formal legal registrations and official records and to which any formal"
            " communication, whether physical or electronic, should be addressed."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.4.2 (TSP trade name)",
        "testo": (
            "Campo obbligatorio che riporta un identificatore di registrazione ufficiale del TSP, ove esista, e che"
            " puo' servire anche a indicare un nome alternativo con cui il TSP si identifica nel contesto dei servizi"
            " elencati nella TL sotto la voce 'TSP name' (clausola 5.4.1). Il valore deve includere l'identificatore"
            " ufficiale con struttura codificata: per le persone giuridiche 3 caratteri di tipo identita' ('VAT' o"
            " 'NTR'), 2 caratteri di codice paese ISO 3166-1, hyphen-minus '-' e l'identificatore; se non esiste un"
            " identificatore registrato il TLSO deve allocarne uno, registrarlo a livello di TLSO e usare 'NTR'. Per"
            " le persone fisiche i tipi sono 'PAS', 'IDC', 'PNO' e 'TIN', con la stessa struttura. La NOTE finale"
            " chiarisce che, in presenza di piu' nomi commerciali o contesti specifici, si possono avere piu' voci"
            " TSP (Name/Trade Name) oppure una sola voce con informazioni di contesto specifiche per servizio, scelta"
            " da concordare tra Scheme Operator e TSP."
        ),
        "testo_integrale": (
            "5.4.2 TSP trade name: Presence: This field shall be present.\nDescription: It specifies an official"
            " registration identifier as registered in official records, where such a registered identifier exists,"
            " that unambiguously identifies the TSP.\nIt may additionally be used to specify an alternative name"
            " under which the TSP identifies itself in the specific context of the provision of those of its services"
            " which are to be found in this TL under its 'TSP name' (clause 5.4.1) entry.\nFormat: A sequence of"
            " multilingual character strings (see clause 5.1.4).\nValue: It shall include an official registration"
            " identifier as registered in official records, where such a registered identifier exists, that"
            " unambiguously identifies the TSP.\nWhen the TSP is a legal person, that identifier shall be expressed"
            " using the following structure for the corresponding character string in the presented order:\na) 3"
            " character legal person identity type reference, having one of the following defined values:\ni) \"VAT\""
            " for identification based on a national value added tax identification number; or\nii) \"NTR\" for"
            " identification based on an identifier from a national register, e.g. a national trade register.\nWhen"
            " both a national value added tax identification number and one (or more) other national identification"
            " number exist, the national value added tax identification number shall be used to identify the listed"
            " TSP.\nWhen no registered identifier exists for a listed TSP, the TLSO shall allocate an identifier,"
            " register such identifier at TLSO level and use the \"NTR\" value for the identity type reference.\nb) 2"
            " character ISO 3166-1 [15] country code;\nc) hyphen-minus \"-\" (0x2D (ASCII), U+002D (UTF-8)); and\nd)"
            " identifier (according to country and identity type reference).\nWhen the TSP is a natural person, that"
            " identifier shall be expressed using the following structure for the corresponding character string in"
            " the presented order:\na) 3 character natural person identity type reference, having one of the"
            " following defined values:\ni) \"PAS\" for identification based on passport number;\nii) \"IDC\" for"
            " identification based on national identity card number;\niii) \"PNO\" for identification based on"
            " (national) personal number (national civic registration number); or\niv) \"TIN\" Tax Identification"
            " Number according to the European Commission - Tax and Customs Union"
            " (http://ec.europa.eu/taxation_customs/tin/tinByCountry.html).\nb) 2 character ISO 3166-1 [15] country"
            " code;\nc) hyphen-minus \"-\" (0x2D (ASCII), U+002D (UTF-8)); and\nd) identifier (according to country"
            " and identity type reference).\nIt may additionally include any name under which the legal entity, or"
            " when applicable the natural person, responsible for the TSP operates, in the specific context of the"
            " delivery of those of its services which are to be found in this TL.\nNOTE: Where a single TSP legal"
            " entity, or when applicable a natural person, is providing services under different trade names or under"
            " different specific contexts, there might be as many TSP entries as such specific contexts (e.g."
            " Name/Trade Name entries). An alternative is to list each and every TSP (legal entity or when applicable"
            " natural person) only once and provide Service specific context information. This is up to the Scheme"
            " Operator to discuss and agree with the TSP the most suitable approach."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.4.3.0 (General)",
        "testo": (
            "Campo obbligatorio che specifica l'indirizzo della persona giuridica o dell'organizzazione mandataria, o"
            " quando applicabile della persona fisica, identificata nel campo 'TSP name' (clausola 5.4.1), per le"
            " comunicazioni sia postali sia elettroniche. E' un campo multi-parte composto dall'indirizzo postale"
            " (clausola 5.4.3.1) e dall'indirizzo elettronico (clausola 5.4.3.2). In caso di cessazione dell'intero"
            " insieme dei servizi di un TSP elencato (es. fallimento), l'indirizzo del TSP deve essere sostituito con"
            " quello usato dallo Scheme Operator per le richieste sui servizi terminati (es. un indirizzo email"
            " dedicato e una pagina web specifica con le informazioni di contatto)."
        ),
        "testo_integrale": (
            "5.4.3.0 General: Presence: This field shall be present.\nDescription: It specifies the address of the"
            " legal entity or mandated organization, or when applicable the natural person, identified in the 'TSP"
            " name' field (clause 5.4.1) for both postal and electronic communications.\nFormat: This is a multi-part"
            " field consisting of the TSP physical address specified in clause 5.4.3.1 and the TSP electronic address"
            " specified in clause 5.4.3.2.\nValue: In case of termination or cessation of the entire set of services"
            " provided by a listed TSP (e.g. bankruptcy), the TSP address shall be replaced by the address the Scheme"
            " Operator uses for enquiries about the terminated services (e.g. a specific dedicated email address and"
            " a specific webpage with relevant information including contact information)."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.4.3.1 (TSP postal address)",
        "testo": (
            "Campo obbligatorio che specifica l'indirizzo postale del TSP identificato nella clausola 5.4.1, con"
            " possibilita' di includerlo in piu' lingue; formato come da clausola 5.3.5.1. Il valore deve essere un"
            " indirizzo postale presso il quale il TSP fornisce un servizio di assistenza (customer care/help line)"
            " gestito tramite posta convenzionale e trattato secondo le normali prassi di servizio."
        ),
        "testo_integrale": (
            "5.4.3.1 TSP postal address: Presence: This field shall be present.\nDescription: It specifies the postal"
            " address of the TSP identified in clause 5.4.1, with the provision for the inclusion of the address in"
            " multiple languages.\nFormat: As specified in clause 5.3.5.1.\nValue: This shall be a postal address at"
            " which the TSP provides a customer care or help line service, operated through conventional (physical)"
            " mail and processed as would be expected by normal business services."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.4.3.2 (TSP electronic address)",
        "testo": (
            "Campo obbligatorio che specifica un indirizzo email, un URI di sito web e un numero di telefono"
            " opzionale del TSP identificato nella clausola 5.4.1, da usare per le comunicazioni elettroniche;"
            " formato come da clausola 5.3.5.2. L'indirizzo email e il numero di telefono, quando presente, devono"
            " essere recapiti presso cui il TSP fornisce un servizio di assistenza relativo ai servizi elencati;"
            " l'URI del sito web deve condurre a una funzionalita' che consenta all'utente di comunicare con tale"
            " assistenza."
        ),
        "testo_integrale": (
            "5.4.3.2 TSP electronic address: Presence: This field shall be present.\nDescription: It specifies an"
            " email address, a web-site URI, and an optional telephone number of the TSP identified in clause 5.4.1,"
            " to be used for electronic communications.\nFormat: As specified in clause 5.3.5.2.\nValue: The e-mail"
            " address, and the telephone number when present, shall be an address, and respectively a phone number"
            " when present, at which the TSP provides a customer care or help line service which is related to the"
            " listed services and which are processed as would be expected by normal business services. As regards a"
            " web-site URI, this shall lead to a capability whereby the user may communicate with a customer care or"
            " help line service which is related to the listed services and which is processed as would be expected"
            " by normal business services."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.4.4 (TSP information URI)",
        "testo": (
            "Campo obbligatorio che indica gli URI presso cui gli utenti (es. terzi affidanti) possono ottenere"
            " informazioni specifiche del TSP: versioni ultima e precedenti delle Practices Statements e/o Policies"
            " del TSP (es. CPS/CP), termini e condizioni generali, questioni legali, politiche di assistenza e altre"
            " informazioni generiche applicabili a tutti i servizi elencati nella voce TSP della TL. Se un TSP eroga"
            " servizi con piu' nomi commerciali o contesti specifici e cio' si riflette in altrettante voci TSP, il"
            " campo deve riportare le informazioni relative allo specifico insieme di servizi elencato. In caso di"
            " cessazione dell'intero insieme dei servizi, l'URI deve essere sostituito con l'URI specifico usato"
            " dallo Scheme Operator per informare sui servizi terminati, incluse le versioni ultima e precedenti di"
            " CPS/CP e GTC, i servizi di stato di validita' dei certificati mantenuti e le ultime CRL/ARL quando"
            " tutti i certificati sono stati revocati."
        ),
        "testo_integrale": (
            "5.4.4 TSP information URI: Presence: This field shall be present.\nDescription: It specifies the URI(s)"
            " where users (e.g. relying parties) can obtain TSP-specific information.\nFormat: Sequence of"
            " multilingual pointers (see clause 5.1.4).\nValue: The referenced URI(s) shall provide a path to"
            " information describing or leading to the description of the last and previous versions of the TSP's"
            " Practices Statements and/or Policies (e.g. CPS/CPs), the general terms and conditions of the TSP, legal"
            " issues, its customer care policies and other generic information which applies to all of its services"
            " listed under its TSP entry in the TL.\nWhere a single TSP entity is providing services under different"
            " trade names or under different specific contexts, and this has been reflected in as many TSP entries as"
            " such specific contexts, this field shall specify information related to the specific set of services"
            " listed under a particular TSP/TradeName entry.\nIn case of termination or cessation of the entire set"
            " of services provided by a listed TSP (e.g. bankruptcy), the TSP information URI shall be replaced by"
            " the specific URI the Scheme Operator uses for providing information about the terminated services (i.e."
            " a specific dedicated webpage with relevant information) including the last and previous versions of the"
            " TSP's Practices Statements and/or Policies (e.g. CPS/CPs), GTC, maintained certificate validity status"
            " services or last CRL(s)/ARL(s) when all certificates have been revoked, etc.)."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.4.5 (TSP information extensions)",
        "testo": (
            "Campo opzionale che gli scheme operator possono usare per fornire informazioni specifiche del TSP,"
            " interpretate secondo le regole dello scheme. Il formato e' una sequenza di estensioni TSP a formato"
            " aperto; ciascuna estensione e' scelta dallo scheme operator in base al significato e alle informazioni"
            " che intende veicolare nella TL, e il suo significato e' definito dalla specifica di origine"
            " (definizione propria dello scheme operator o di altro soggetto, es. comunita'/federazione di scheme,"
            " ente di standardizzazione). Nel contesto delle TL degli Stati membri UE le estensioni informative del"
            " TSP, quando usate, non devono essere marcate come critical."
        ),
        "testo_integrale": (
            "5.4.5 TSP information extensions: Presence: This field is optional.\nDescription: It may be used by"
            " scheme operators to provide specific TSP-related information, to be interpreted according to the"
            " specific scheme's rules.\nFormat: Sequence of TSP extensions whose format is left open.\nValue: Each"
            " TSP information extension may be selected by the scheme operator according to the meaning and"
            " information it wishes to convey within its TL.\nThe meaning of each extension is hence defined by its"
            " source specification, that specification being either the scheme operator's own definition or any other"
            " extension definition produced by another entity, such as a community or federation of schemes, a"
            " standards body, etc.\nIn the context of EU Member State trusted lists, the TSP information extensions,"
            " when used, shall not be made critical."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Campo opzionale; nel contesto delle trusted list degli Stati membri UE, quando usato, non deve"
            " essere marcato come critical."
        ),
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.4.6 (TSP Services (list of services))",
        "testo": (
            "Campo obbligatorio che elenca i servizi riconosciuti del TSP e lo stato di approvazione (con la storia"
            " di tale stato) di ciascun servizio: e' una sequenza di elementi TSP Service, ognuno una tupla formata"
            " da un elemento Service Information (clausola 5.5) e da un elemento condizionale Service History"
            " (clausola 5.6). Deve essere elencato almeno un servizio, anche se l'informazione detenuta e'"
            " interamente storica; poiche' la conservazione delle informazioni storiche sui servizi elencati e'"
            " richiesta dalla clausola 5.3.12, tali informazioni vanno conservate anche quando lo stato attuale del"
            " servizio non ne richiederebbe l'elenco (es. servizio ritirato): il TSP va quindi incluso anche quando"
            " il suo unico servizio elencato e' in tale stato, per preservarne la storia."
        ),
        "testo_integrale": (
            "5.4.6 TSP Services (list of services): Presence: This field shall be present.\nDescription: It contains"
            " a sequence identifying each of the TSP's recognized services and the approval status (and history of"
            " that status) of that service.\nFormat: A sequence of TSP Service elements, where each of such TSP"
            " Service element is a tuple made of a Service Information element (see clause 5.5) and a conditional"
            " Service History element. Each of such Service History element, when present, is a sequence of Service"
            " History Instance elements (see clause 5.6).\nValue: At least one service shall be listed, even if the"
            " information held is entirely historical.\nAs the retention of historical information about listed"
            " services is required by clause 5.3.12, that historical information shall be retained even if the"
            " service's present status would not normally require it to be listed (e.g. the service is withdrawn)."
            " Thus a TSP shall be included even when its only listed service is in such a state, so as to preserve"
            " the history."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.5.1.0 (General requirements)",
        "testo": (
            "Campo obbligatorio che riporta l'identificatore del tipo di servizio, espresso come URI. Il valore deve"
            " essere uno degli URI della clausola 5.5.1.1 (tipi di servizio fiduciario qualificato del Reg. (UE)"
            " 910/2014), oppure della clausola 5.5.1.2 (tipi non qualificati), oppure della clausola 5.5.1.3 (tipi"
            " non previsti dal Regolamento ma definiti su base nazionale di uno Stato membro UE, di un Paese terzo o"
            " di specifiche di organizzazioni internazionali), oppure qualunque altro valore URI registrato e"
            " descritto dallo scheme operator o da altro soggetto. La NOTE finale ricorda che qualunque"
            " organizzazione puo' richiedere un object identifier sotto il nodo etsi-identified organization o una"
            " radice URI secondo le indicazioni del portale ETSI."
        ),
        "testo_integrale": (
            "5.5.1.0 General requirements: Presence: This field shall be present.\nDescription: It specifies the"
            " identifier of the service type.\nFormat: An indicator expressed as a URI.\nValue: The quoted URI shall"
            " be:\na) one of the URIs specified in clause 5.5.1.1 corresponding to the type of listed trust service"
            " for qualified trust services specified in Regulation (EU) No 910/2014 [i.10]; or\nb) one of the URIs"
            " specified in clause 5.5.1.2 corresponding to the type of listed trust service for non-qualified trust"
            " services specified in Regulation (EU) No 910/2014 [i.10]; or\nc) one of the URIs specified in clause"
            " 5.5.1.3 corresponding to the type of listed trust service for trust services that are not specified in"
            " Regulation (EU) No 910/2014 [i.10] but specified on a EU MS national basis, a non-EU country basis or"
            " on the basis of an international organization specifications; or\nd) any other URI value registered and"
            " described by the scheme operator or another entity.\nNOTE: Any organization can request an object"
            " identifier under the etsi-identified organization node or a URI root as detailed on"
            " https://portal.etsi.org/PNNS.aspx."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.5.1.1 (Regulation (EU) No 910/2014 qualified trust service types)",
        "testo": (
            "Registro dei tipi di servizio fiduciario qualificato del Reg. (UE) 910/2014, con URI, descrizione e"
            " requisiti: da (a) CA/QC a (m) Ledgers/Q sono elencati i tipi CA/QC, Certstatus/OCSP/QC,"
            " Certstatus/CRL/QC, TSA/QTST, EDS/Q, EDS/REM/Q, PSES/Q, QESValidation/Q, RemoteQSigCDManagement/Q,"
            " RemoteQSealCDManagement/Q, EAA/Q, ElectronicArchiving/Q e Ledgers/Q. La clausola impone fra l'altro:"
            " l'identificazione ulteriore del servizio di generazione di certificati 'root' mediante l'identificatore"
            " RootCA-QC e l'estensione additionalServiceInformation; l'elenco separato dei servizi di stato di"
            " validita' dei certificati quando non firmati dalla chiave privata corrispondente alla chiave pubblica"
            " elencata e privi di catena di certificazione verso il servizio elencato; l'appartenenza o non"
            " appartenenza di ciascun tipo alla categoria dei servizi non basati su tecnologia a chiave pubblica"
            " (clausola 5.5.3); il divieto di elencare i servizi qualificati di marca temporale per eredita' del tipo"
            " CA/QC, richiedendo una voce separata con 'Sti' distinto. I TLSO di Paesi terzi o organizzazioni"
            " internazionali possono usare questi URI per servizi equivalenti, usando l'opportuna estensione (in"
            " particolare la Qualifications extension). La NOTE di (a) illustra in dettaglio regole e prassi di"
            " elenco dei servizi di stato di validita' (CRL/OCSP) e i casi in cui l'elenco separato e' obbligatorio."
        ),
        "testo_integrale": (
            "5.5.1.1 Regulation (EU) No 910/2014 qualified trust service types: (a) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/CA/QC Description: A qualified certificate issuing trust service"
            " creating and signing qualified certificates based on the identity and other attributes verified by the"
            " relevant registration services, and under which are provided the relevant and related revocation and"
            " certificate validity status information services (e.g. CRLs, OCSP responses) in accordance with EU"
            " Directive 1999/93/EC [i.3] or with Regulation (EU) No 910/2014 [i.10] whichever is in force at the time"
            " of provision. This may also include generation and/or management of the associated private keys on"
            " behalf of the certified entity.\nRequirements: When the listed service is a \"root\" certificate"
            " generation service issuing certificates to one or more subordinates certificate generation services and"
            " from which a certification path can be established down to a certificate generation service issuing"
            " end-entity qualified certificates, this service type shall be further identified by using the"
            " \"http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/RootCA-QC\" identifier (described in clause D.4)"
            " which is included in the additionalServiceInformation extension (clause 5.5.9.4) within a Service"
            " information extension (clause 5.5.9). When applicable, this service type shall be further specified"
            " through the use of an additionalServiceInformation extension (clause 5.5.9.4) within a Service"
            " information extension (clause 5.5.9) by using the appropriate identifiers indicating the nature of the"
            " qualified certificates for which the qualified status has been granted, i.e. qualified certificates for"
            " electronic signatures, qualified certificates for electronic seals, and/or qualified certificates for"
            " website authentication (as specified in clause 5.5.9.4). When, in accordance with Annex II of"
            " Regulation (EU) No 910/2014 [i.10], the above described service includes the management of the"
            " electronic signature creation data on behalf of the signatory for qualified electronic signatures as"
            " part of the provision of qualified electronic signature creation device, and/or includes the management"
            " of the electronic seal creation data on behalf of the seal creator for qualified electronic seals as"
            " part of the provision of qualified electronic signature creation device, then the qualified"
            " certificates for which the private key resides in such a device shall be further identified and"
            " specified through the use of a Qualifications extension (clause 5.5.9.2) within a Service information"
            " extension (clause 5.5.9) by using the appropriate criteria and qualifiers (clause 5.5.9.2.3). When the"
            " certificate validity status information (e.g. CRLs, OCSP responses) related to the qualified"
            " certificates issued by the listed \"CA/QC\" identified service are not signed by the private key"
            " corresponding to the listed public key and when no certificate chain/path exists from the related"
            " certificate validity status information services (either CRL issuing entities or OCSP responders) to"
            " the listed \"CA/QC\" identified service public key, those certificate validity status information"
            " services shall be listed separately. This service shall not fall under the category of services not"
            " using PKI public-key technology (see clause 5.5.3).\nNOTE: In the context of Regulation (EU) 910/2014"
            " [i.10] the qualified status of each qualified trust service has to be provided in the relevant EU MS"
            " TL. This does not preclude technical means to collectively indicate the grant/withdrawal of a qualified"
            " status to a set of trust services in particular when they are components of a logical set of trust"
            " services to which the status is collectively provided. Standard practices lead to CA/QC services for"
            " which the private key corresponding to the listed Sdi public key is used not only to sign qualified"
            " certificates but also to sign certificates issued to certificate validity status information services"
            " (either CRL issuing entities or OCSP responders) when those information (e.g. CRLs, OCSP responses) are"
            " not directly signed by that private key. This is in line with the practices under Directive 1999/93/EC"
            " [i.3] and CD 2009/767/EC [i.2] for listing CA/QC (or even CA/QC being RootCA-QC) and for which it is"
            " not required to separately list the corresponding CRL issuing services or OCSP responders unless, when"
            " best and standard practise are not used by the corresponding TSPs, those entities are not signed by the"
            " listed CA/QC service or no certificate chain/path exists from those entities to the listed service. In"
            " those latter cases, listing those certificate validity status information services as separate entries"
            " in the TL is mandatory. Those are the rules that have been used so far since end 2009. There is"
            " nevertheless the ability for EU MS and TSPs to have their certificate validity status information"
            " services to be listed individually when this would be required. For a TSP situation where a single root"
            " CA is root-signing e.g. 40 issuing CAs each of them using one CRL issuer and one OCSP responder,"
            " requiring to list separately all such 3 component services would lead to have 120 entries in the TL"
            " instead of a single one, for the same effect when anyway the status is granted collectively to the"
            " whole hierarchy. In practice this would mean increasing the size and complexity of TL by at least a"
            " factor 3. Qualified time stamp services are not listed by inheritance of the CA/QC type. A separate"
            " entry with a distinct Sti needs to be used for this. Even when the same private key corresponding to"
            " the listed Sdi public key is used.\n(b) URI: http://uri.etsi.org/TrstSvc/Svctype/Certstatus/OCSP/QC"
            " Description: A certificate validity status information service issuing Online Certificate Status"
            " Protocol (OCSP) signed responses and operating an OCSP-server as part of a service from a (qualified)"
            " trust service provider issuing qualified certificates, in accordance with the applicable national"
            " legislation in the territory identified by the TL Scheme territory (see clause 5.3.10) or with"
            " Regulation (EU) No 910/2014 [i.10] whichever is in force at the time of provision.\nRequirement: This"
            " service shall not fall under the category of services not using PKI public-key technology (see clause"
            " 5.5.3).\n(c) URI: http://uri.etsi.org/TrstSvc/Svctype/Certstatus/CRL/QC Description: A certificate"
            " validity status information services issuing and signing Certificate Revocation Lists (CRLs) and being"
            " part of a service from a (qualified) trust service provider issuing qualified certificates, in"
            " accordance with the applicable national legislation in the territory identified by the TL Scheme"
            " territory (see clause 5.3.10) or with Regulation (EU) No 910/2014 [i.10] whichever is in force at the"
            " time of provision.\nRequirement: This service shall not fall under the category of services not using"
            " PKI public-key technology (see clause 5.5.3).\n(d) URI: http://uri.etsi.org/TrstSvc/Svctype/TSA/QTST"
            " Description: A qualified electronic time stamp generation service creating and signing qualified"
            " electronic time stamps in accordance with the applicable national legislation in the territory"
            " identified by the TL Scheme territory (see clause 5.3.10) or with Regulation (EU) No 910/2014 [i.10]"
            " whichever is in force at the time of provision.\nRequirement: This service shall not fall under the"
            " category of services not using PKI public-key technology (see clause 5.5.3).\n(e) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/EDS/Q Description: A qualified electronic registered delivery"
            " service providing qualified electronic registered deliveries in accordance with the applicable national"
            " legislation in the territory identified by the TL Scheme territory (see clause 5.3.10) or with"
            " Regulation (EU) No 910/2014 [i.10] whichever is in force at the time of provision.\nRequirement: This"
            " service shall not fall under the category of services not using PKI public-key technology (see clause"
            " 5.5.3).\n(f) URI: http://uri.etsi.org/TrstSvc/Svctype/EDS/REM/Q Description: A qualified electronic"
            " registered mail delivery service providing qualified electronic registered mail deliveries in"
            " accordance with the applicable national legislation in the territory identified by the TL Scheme"
            " territory (see clause 5.3.10) or with Regulation (EU) No 910/2014 [i.10] whichever is in force at the"
            " time of provision.\nRequirement: This service shall not fall under the category of services not using"
            " PKI public-key technology (see clause 5.5.3).\n(g) URI: http://uri.etsi.org/TrstSvc/Svctype/PSES/Q"
            " Description: A qualified preservation service for qualified electronic signatures and/or qualified"
            " electronic seals in accordance with the applicable national legislation in the territory identified by"
            " the TL Scheme territory (see clause 5.3.10) or with Regulation (EU) No 910/2014 [i.10] whichever is in"
            " force at the time of provision.\nRequirements: When applicable, this service type shall be further"
            " specified through the use of an additionalServiceInformation extension (clause 5.5.9.4) within a"
            " Service information extension (clause 5.5.9) by using the appropriate identifiers indicating whether it"
            " is provided for electronic signatures and/or for electronic seals (as specified in clause 5.5.9.4)."
            " This service shall not fall under the category of services not using PKI public-key technology (see"
            " clause 5.5.3).\n(h) URI: http://uri.etsi.org/TrstSvc/Svctype/QESValidation/Q Description: A qualified"
            " validation service for qualified electronic signatures and/or qualified electronic seals in accordance"
            " with the applicable national legislation in the territory identified by the TL Scheme territory (see"
            " clause 5.3.10) or with Regulation (EU) No 910/2014 [i.10] whichever is in force at the time of"
            " provision.\nRequirements: When applicable, this service type shall be further specified through the use"
            " of an additionalServiceInformation extension (clause 5.5.9.4) within a Service information extension"
            " (clause 5.5.9) by using the appropriate identifiers indicating whether it is provided for electronic"
            " signatures and/or for electronic seals (as specified in clause 5.5.9.4). This service shall not fall"
            " under the category of services not using PKI public-key technology (see clause 5.5.3).\n(i) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/RemoteQSigCDManagement/Q Description: The management of remote"
            " qualified electronic signature creation devices as a qualified trust service carried out by a qualified"
            " trust service provider, in accordance with Regulation (EU) No 910/2014 [i.10].\nRequirement: This"
            " service may fall under the category of services not using PKI public-key technology (see clause 5.5.3)."
            "\n(j) URI: http://uri.etsi.org/TrstSvc/Svctype/RemoteQSealCDManagement/Q Description: The management of"
            " remote qualified electronic seal creation devices as a qualified trust service carried out by a"
            " qualified trust service provider, in accordance with Regulation (EU) No 910/2014 [i.10].\nRequirement:"
            " This service may fall under the category of services not using PKI public-key technology (see clause"
            " 5.5.3).\n(k) URI: http://uri.etsi.org/TrstSvc/Svctype/EAA/Q Description: The issuance of qualified"
            " electronic attestations of attributes by a qualified trust service provider in accordance with"
            " Regulation (EU) No 910/2014 [i.10].\nRequirement: This service shall not fall under the category of"
            " services not using PKI public-key technology (see clause 5.5.3).\n(l) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/ElectronicArchiving/Q Description: A qualified electronic archiving"
            " service provided by a qualified trust service provider in accordance with Regulation (EU) No 910/2014"
            " [i.10].\nRequirement: This service shall not fall under the category of services not using PKI"
            " public-key technology (see clause 5.5.3).\n(m) URI: http://uri.etsi.org/TrstSvc/Svctype/Ledgers/Q"
            " Description: A qualified trust service for the recording of electronic data in qualified electronic"
            " ledgers by a qualified trust service provider in accordance with Regulation (EU) No 910/2014 [i.10]\n"
            "Requirement: This service may fall under the category of services not using PKI public-key technology"
            " (see clause 5.5.3).\nTLSOs from non-EU countries or international organizations may use the above URI's"
            " to identify the type of listed trust services that are meeting equivalent requirements to those laid"
            " down in the European legislation and in this case should use the appropriate service information"
            " extension (see clause 5.5.9) to further identify those sets of certificates meeting such requirements,"
            " in particular the Qualification extension when applicable (see clause 5.5.9.2)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.5.1.2 (Regulation (EU) No 910/2014 non qualified trust service types)",
        "testo": (
            "Registro dei tipi di servizio fiduciario non qualificato del Reg. (UE) 910/2014: da (a) CA/PKC a (x)"
            " PKCValidation/CertsforOtherTypesOfTS, ciascuno con URI, descrizione e, ove presenti, requisiti"
            " aggiuntivi (specificazione mediante additionalServiceInformation, elenco separato dei servizi di stato"
            " di validita' dei certificati, divieto di ulteriore specificazione per i certificati destinati ad altri"
            " tipi di servizio fiduciario). Salvo quanto esplicitamente indicato, questi servizi non ricadono nella"
            " categoria dei servizi non basati su tecnologia a chiave pubblica (clausola 5.5.3)."
        ),
        "testo_integrale": (
            "5.5.1.2 Regulation (EU) No 910/2014 non qualified trust service types: Unless explicitly stated, those"
            " services shall not fall under the category of services not using PKI public-key technology (see clause"
            " 5.5.3).\n(a) URI: http://uri.etsi.org/TrstSvc/Svctype/CA/PKC Description: A certificate generation"
            " service, not qualified, creating and signing non-qualified public key certificates based on the"
            " identity and other attributes verified by the relevant registration services.\nRequirements: When"
            " applicable, this service type shall be further specified through the use of an"
            " additionalServiceInformation extension (clause 5.5.9.4) within a Service information extension (clause"
            " 5.5.9) by using the appropriate identifiers indicating the nature of the public key certificates for"
            " which the status has been granted, i.e. certificates for electronic signatures, certificates for"
            " electronic seals, and/or certificates for website authentication (as specified in clause 5.5.9.4). When"
            " the certificate validity status information (e.g. CRLs, OCSP responses) related to the certificates"
            " issued by the listed \"CA/PKC\" identified service are not signed by the private key corresponding to"
            " the listed public key and when no certificate chain/path exists from the related certificate validity"
            " status information services (either CRL issuing entities or OCSP responders) to the listed \"CA/PKC\""
            " identified service public key, those certificate validity status information services shall be listed"
            " separately.\n(b) URI: http://uri.etsi.org/TrstSvc/Svctype/Certstatus/OCSP Description: A certificate"
            " validity status service, not qualified, issuing Online Certificate Status Protocol (OCSP) signed"
            " responses.\n(c) URI: http://uri.etsi.org/TrstSvc/Svctype/Certstatus/CRL Description: A certificate"
            " validity status service, not qualified, issuing CRLs.\n(d) URI: http://uri.etsi.org/TrstSvc/Svctype/TSA"
            " Description: A time-stamping generation service, not qualified, creating and signing time-stamps"
            " tokens.\n(e) URI: http://uri.etsi.org/TrstSvc/Svctype/TSA/TSS-QC Description: A time-stamping service,"
            " not qualified, as part of a service from a trust service provider issuing qualified certificates that"
            " issues time-stamp tokens that can be used in the validation process of qualified signatures/seals or"
            " advanced signatures/seals supported by qualified certificates to ascertain and extend the"
            " signature/seal validity when the qualified certificate is (will be) revoked or expired (will expire).\n"
            "(f) URI: http://uri.etsi.org/TrstSvc/Svctype/TSA/TSS-AdESQCandQES Description: A time-stamping service,"
            " not qualified, as part of a service from a trust service provider that issues time-stamp tokens (TST)"
            " that can be used in the validation process of qualified signatures/seals or advanced signatures/seals"
            " supported by qualified certificates to ascertain and extend the signature/seal validity when the"
            " qualified certificate is (will be) revoked or expired (will expire).\n(g) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/EDS Description: An electronic delivery service, not qualified.\n"
            "(h) URI: http://uri.etsi.org/TrstSvc/Svctype/EDS/REM Description: A Registered Electronic Mail delivery"
            " service, not qualified.\n(i) URI: http://uri.etsi.org/TrstSvc/Svctype/PSES Description: A not qualified"
            " preservation service for electronic signatures and/or for electronic seals.\nRequirements: When"
            " applicable, this service type shall be further specified through the use of an"
            " additionalServiceInformation extension (clause 5.5.9.4) within a Service information extension (clause"
            " 5.5.9) by using the appropriate identifiers indicating whether it is provided for electronic signatures"
            " and/or for electronic seals (as specified in clause 5.5.9.4).\n(j) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/AdESValidation Description: A not qualified validation service for"
            " advanced electronic signatures and/or advanced electronic seals.\nRequirements: When applicable, this"
            " service type shall be further specified through the use of an additionalServiceInformation extension"
            " (clause 5.5.9.4) within a Service information extension (clause 5.5.9) by using the appropriate"
            " identifiers indicating whether it is provided for electronic signatures and/or for electronic seals (as"
            " specified in clause 5.5.9.4).\n(k) URI: http://uri.etsi.org/TrstSvc/Svctype/AdESGeneration Description:"
            " A not qualified generation service for advanced electronic signatures and/or advanced electronic seals."
            "\nRequirements: When applicable, this service type shall be further specified through the use of an"
            " additionalServiceInformation extension (clause 5.5.9.4) within a Service information extension (clause"
            " 5.5.9) by using the appropriate identifiers indicating whether it is provided for electronic signatures"
            " and/or for electronic seals (as specified in clause 5.5.9.4). This service may fall under the category"
            " of services not using PKI public-key technology (see clause 5.5.3).\n(l) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/RemoteSigCDManagement Description: A not qualified trust service"
            " for the management of remote electronic signature creation devices, provided by a trust service"
            " provider that generates or manages electronic signature creation data on behalf of the signatory.\n"
            "Requirement: This service may fall under the category of services not using PKI public-key technology"
            " (see clause 5.5.3).\n(m) URI: http://uri.etsi.org/TrstSvc/Svctype/RemoteSealCDManagement Description: A"
            " not qualified trust service for the management of remote electronic seal creation devices, provided by"
            " a trust service provider that generates or manages electronic seal creation data on behalf of the seal"
            " creator.\nRequirement: This service may fall under the category of services not using PKI public-key"
            " technology (see clause 5.5.3).\n(n) URI: http://uri.etsi.org/TrstSvc/Svctype/EAA Description: The"
            " issuance of not qualified electronic attestations of attributes by a trust service provider in"
            " accordance with Regulation (EU) No 910/2014 [i.10].\n(o) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/ElectronicArchiving Description: A not qualified electronic"
            " archiving service provided by a trust service provider in accordance with Regulation (EU) No 910/2014"
            " [i.10].\n(p) URI: http://uri.etsi.org/TrstSvc/Svctype/Ledgers Description: A not qualified trust"
            " service for the recording of electronic data in not qualified electronic ledgers by a trust service"
            " provider in accordance with Regulation (EU) No 910/2014 [i.10].\nRequirement: This service may fall"
            " under the category of services not using PKI public-key technology (see clause 5.5.3).\n(q) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/PKCValidation Description: A not qualified trust service for the"
            " validation of certificates for electronic signatures, certificates for electronic seals, or"
            " certificates for website authentication.\nRequirements: Where applicable, this service type shall be"
            " further specified through the use of an additionalServiceInformation extension (clause 5.5.9.4) within"
            " a Service information extension (clause 5.5.9) by using the appropriate identifiers indicating whether"
            " it is provided for certificates for electronic signatures, certificates for electronic seals, and/or"
            " certificates for website authentication (as specified in clause 5.5.9.4).\n(r) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/PKCPreservation Description: A not qualified trust service for the"
            " preservation of certificates for electronic signatures or certificates for electronic seals.\n"
            "Requirements: Where applicable, this service type shall be further specified through the use of an"
            " additionalServiceInformation extension (clause 5.5.9.4) within a Service information extension (clause"
            " 5.5.9) by using the appropriate identifiers indicating whether it is provided for certificates for"
            " electronic signatures and/or for certificates for electronic seals (as specified in clause 5.5.9.4).\n"
            "(s) URI: http://uri.etsi.org/TrstSvc/Svctype/EAAValidation Description: A not qualified trust service"
            " for the validation of electronic attestation of attributes.\n(t) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/TSTValidation Description: A not qualified trust service for the"
            " validation of electronic timestamps.\n(u) URI: http://uri.etsi.org/TrstSvc/Svctype/EDSValidation"
            " Description: A not qualified trust service for the validation of data transmitted through electronic"
            " registered delivery services and the validation of related evidences.\n(v) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/EAA/Pub-EAA Description: The issuance of not qualified electronic"
            " attestation of attributes as defined in Article 3(46) of Regulation (EU) No 910/2014 [i.10], issued by"
            " or on behalf of a public sector body responsible for an authentic source, acting as a trust service"
            " provider and in accordance with that Regulation.\n(w) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/CA/PKC/CertsforOtherTypesOfTS Description: A certificate generation"
            " service, not qualified, creating and signing non-qualified public key certificates based on the"
            " identity and other attributes verified by the relevant registration services. The nature of those"
            " public key certificates for which the status has been granted are neither certificates for electronic"
            " signatures, nor certificates for electronic seals, nor certificates for website authentication. They"
            " are certificates for the provision of other trust services as referred to in Article 3(16) of"
            " Regulation (EU) 910/2014 [i.10].\nRequirements: This service type shall not be further specified"
            " through the use of an additionalServiceInformation extension (clause 5.5.9.4) within a Service"
            " information extension (clause 5.5.9) using URIs referred to in subpoints (i), (ii) or (iii) of point"
            " (a) of clause 5.5.9.4. When the certificate validity status information (e.g. CRLs, OCSP responses)"
            " related to the certificates issued by the listed \"CA/PKC/CertsforOtherTypesOfTS\" identified service"
            " are not signed by the private key corresponding to the listed public key and when no certificate"
            " chain/path exists from the related certificate validity status information services (either CRL issuing"
            " entities or OCSP responders) to the listed \"CA/PKC\" identified service public key, those certificate"
            " validity status information services shall be listed separately.\n(x) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/PKCValidation/CertsforOtherTypesOfTS Description: A not qualified"
            " trust service for the validation of certificates for the provision of other trust services as referred"
            " to in Article 3(16) of Regulation (EU) 910/2014 [i.10].\nRequirements: This service type shall not be"
            " further specified through the use of an additionalServiceInformation extension (clause 5.5.9.4) within"
            " a Service information extension (clause 5.5.9) using URIs referred to in subpoints (i), (ii) or (iii)"
            " of point (a) of clause 5.5.9.4."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.5.1.3 (Trust service types not defined in Regulation (EU) No 910/2014 but nationally defined)",
        "testo": (
            "Registro dei tipi di servizio fiduciario non definiti nel Reg. (UE) 910/2014 ma definiti a livello"
            " nazionale: da (a) RA a (o) unspecified, ciascuno con URI e descrizione. Alcuni tipi il cui URI termina"
            " con '/nothavingPKIid' (RA, Archiv, IdV, KEscrow, PPwd) ricadono espressamente nella categoria dei"
            " servizi non basati su tecnologia a chiave pubblica (clausola 5.5.3). Per il tipo 'unspecified' le"
            " informazioni su natura e tipo del servizio devono essere fornite in altro modo, ad esempio con"
            " un'estensione a livello di servizio (clausole 5.5.6 o 5.5.9), e il servizio puo' ricadere nella"
            " categoria dei servizi non basati su PKI. Salvo quanto esplicitamente indicato, questi servizi non"
            " ricadono in tale categoria."
        ),
        "testo_integrale": (
            "5.5.1.3 Trust service types not defined in Regulation (EU) No 910/2014 but nationally defined: Unless"
            " explicitly stated, those services shall not fall under the category of services not using PKI"
            " public-key technology (see clause 5.5.3).\n(a) URI: http://uri.etsi.org/TrstSvc/Svctype/RA Description:"
            " A registration service that verifies the identity and, if applicable, any specific attributes of a"
            " subject for which a certificate is applied for, and whose results are passed to the relevant"
            " certificate generation service.\n(b) URI: http://uri.etsi.org/TrstSvc/Svctype/RA/nothavingPKIid"
            " Description: A registration service • that verifies the identity and, if applicable, any specific"
            " attributes of a subject for which a certificate is applied for, and whose results are passed to the"
            " relevant certificate generation service, and • that cannot be identified by a specific PKI-based public"
            " key.\nThis service falls under the category of services not using PKI public-key technology (see clause"
            " 5.5.3).\n(c) URI: http://uri.etsi.org/TrstSvc/Svctype/ACA Description: An attribute certificate"
            " generation service creating and signing attribute certificates based on the identity and other"
            " attributes verified by the relevant registration services.\n(d) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/SignaturePolicyAuthority Description: A service responsible for"
            " issuing, publishing or maintenance of signature policies.\n(e) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/Archiv Description: An Archival service.\n(f) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/Archiv/nothavingPKIid Description: An Archival service that cannot"
            " be identified by a specific PKI-based public key.\nThis service falls under the category of services"
            " not using PKI public-key technology (see clause 5.5.3).\n(g) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/IdV Description: An Identity verification service.\n(h) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/IdV/nothavingPKIid Description: An Identity verification service"
            " that cannot be identified by a specific PKI-based public key.\nThis service falls under the category of"
            " services not using PKI public-key technology (see clause 5.5.3).\n(i) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/KEscrow Description: A Key escrow service.\n(j) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/KEscrow/nothavingPKIid Description: A Key escrow service that"
            " cannot be identified by a specific PKI-based public key.\nThis service falls under the category of"
            " services not using PKI public-key technology (see clause 5.5.3).\n(k) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/PPwd Description: Issuer of PIN- or password-based identity"
            " credentials.\n(l) URI: http://uri.etsi.org/TrstSvc/Svctype/PPwd/nothavingPKIid Description: Issuer of"
            " PIN- or password-based identity credentials that cannot be identified by a specific PKI-based public"
            " key.\nThis service falls under the category of services not using PKI public-key technology (see clause"
            " 5.5.3).\n(m) URI: http://uri.etsi.org/TrstSvc/Svctype/TLIssuer Description: A service issuing trusted"
            " lists.\n(n) URI: http://uri.etsi.org/TrstSvc/Svctype/NationalRootCA-QC Description: A national root"
            " signing CA issuing root-signing or qualified certificates to trust service providers and related"
            " certification or trust services that are accredited against a national voluntary accreditation scheme"
            " or supervised under national law in accordance with the applicable European legislation.\n(o) URI:"
            " http://uri.etsi.org/TrstSvc/Svctype/unspecified Description: A trust service of an unspecified type.\n"
            "Requirements: When the \"unspecified\" Service type identifier is used, information about the nature and"
            " type of the listed service shall be provided in other ways such as through a service level extension"
            " (see clauses 5.5.6 or 5.5.9). This service may fall under the category of services not using PKI"
            " public-key technology (see clause 5.5.3)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.5.2 (Service name)",
        "testo": (
            "Campo obbligatorio che riporta il nome con cui il TSP identificato nel campo 'TSP name' (clausola 5.4.1)"
            " fornisce il servizio il cui tipo e' identificato nel campo 'Service type identifier' (clausola 5.5.1)."
            " Il formato e' una sequenza di stringhe di caratteri multilingua (clausola 5.1.4)."
        ),
        "testo_integrale": (
            "5.5.2 Service name: Presence: This field shall be present.\nDescription: It specifies the name under"
            " which the TSP identified in 'TSP name' (clause 5.4.1) provides the service whose type is identified in"
            " 'Service type identifier' (clause 5.5.1).\nFormat: A sequence of multilingual character strings (see"
            " clause 5.1.4).\nValue: The name under which the TSP provides the service."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.5.3 (Service digital identity)",
        "testo": (
            "Campo obbligatorio che specifica uno e un solo identificatore digitale del servizio, che lo identifica"
            " in modo unico e non ambiguo insieme al tipo associato (clausola 5.5.1): un indicatore espresso come URI"
            " quando non si usa la tecnologia a chiave pubblica (PKI), altrimenti una tupla con uno o piu' elementi"
            " X509Certificate in Base64 e, opzionalmente, X509SubjectName, valore della chiave pubblica (ds:KeyValue)"
            " e Subject Key Identifier (X509SKI). La clausola dettaglia le rappresentazioni ammesse della chiave"
            " pubblica (almeno un X509Certificate, che dovrebbe essere esattamente uno; piu' certificati solo se"
            " riferiti alla stessa chiave e con subject name identici al TSP della clausola 5.4.1), il divieto di"
            " ripetere la stessa chiave pubblica nella TL per lo stesso tipo di servizio, le regole sul"
            " disallineamento dell'attributo 'O=' rispetto al 'TSP Name' (obbligo di dichiarazione formale nello"
            " 'Scheme service definition URI' e di elenco dei valori alternativi come 'TSP Trade Name'), la coerenza"
            " del contenuto di X509SKI con l'estensione SubjectKeyIdentifier, l'uso della chiave pubblica di una CA"
            " root o di livello superiore come 'Sdi' con obbligo di documentazione nello 'Scheme service definition"
            " URI', e l'uso degli identificatori di servizio come trust anchor nella convalida delle firme"
            " elettroniche. Contiene 3 EXAMPLE e 5 NOTE ufficiali, tutte riportate integralmente."
        ),
        "testo_integrale": (
            "5.5.3 Service digital identity: Presence: This field shall be present.\nDescription: It specifies one"
            " and only one service digital identifier uniquely and unambiguously identifying the service with the"
            " type it is associated to (as identified in 'Service type identifier', clause 5.5.1).\nFormat: When not"
            " using PKI public-key technology (e.g. for a service with a service type identifier of structure"
            " http://uri.etsi.org/TrstSvc/Svctype/.../nothavingPKIid or, wherever applicable, for any other URI value"
            " registered and described accordingly), an indicator expressed as a URI.\nWhen using PKI public-key"
            " technology, a tuple giving:\n- one or more X509Certificate elements expressed in Base64 encoded format"
            " as specified in XML-Signature [4];\n- optionally, one X509SubjectName element that contains a"
            " Distinguished Name encoded as established by XML-Signature [4], clause 4.4.4;\n- optionally, a public"
            " key value expressed as a ds:KeyValue element [4];\n- optionally, a public key identifier expressed as"
            " an X.509 certificate Subject Key Identifier (X509SKI element) as specified in XML-Signature [4].\n"
            "Value: When not using PKI public-key technology (e.g. for a service with a service type identifier"
            " ending with the suffix \"/nothavingPKIid\", or wherever applicable), the indicator expressed as a URI"
            " shall be defined by the TLSO in a scheme specific context in such a way that it identifies uniquely and"
            " unambiguously the listed service.\nWhen using PKI public-key technology, the service digital identifier"
            " uniquely and unambiguously identifying the service (with the type it is associated with, as identified"
            " in 'Service type identifier', clause 5.5.1) shall be a public key associated with the TSP service and"
            " used to verify the authenticity of the provided service.\nEXAMPLE 1: The public key used for verifying"
            " signature on certificates, or the public key used for verifying signature on time-stamp tokens, or the"
            " public key for verifying signature on CRLs, or for verifying signature on OCSP responses, or more"
            " generally the public key used to verify signature on trust service outputs.\nNOTE 1: This can be the"
            " public key of a CA issuing end-entity certificates (e.g. non qualified end-entity certificates in the"
            " case of a service of type \"CA/PKC\", or qualified certificates in case of a service of type \"CA/QC\")"
            " or the public key of a root CA belonging to the TSP and from which a path can be found down to"
            " end-entity qualified certificates issued under the responsibility of this TSP. Depending on whether or"
            " not this information and the information to be found in every end-entity certificate issued under this"
            " CA can be used to unambiguously determine the appropriate characteristics of any qualified certificate,"
            " this information (Service digital identity) may need to be completed by 'Service information"
            " extensions' data (see clause 5.5.9).\nThe service digital identifier shall be specified by at least one"
            " representation of this digital identifier. To represent this public key, implementations:\n- shall use"
            " at least one X509Certificate element [4] representing the same public key. It should be represented by"
            " exactly one certificate. The TLSO may list more than one certificate to represent the public key, but"
            " only when all those certificates relate to the same public key and have identical subject names"
            " identifying the TSP identified in clause 5.4.1 as holder of the key. When candidate certificates for"
            " representing the same public key do not have subject names identical to subject names of certificates"
            " already representing the same key, the TLSO shall not use these certificates as representation of this"
            " service digital identifier;\n- should additionally use the following representation of the same public"
            " key:\n• the X509SubjectName element [4] to which the public key relates under the form of a"
            " Distinguished Name.\nthis representation of the public key should not be used by applications in"
            " machine processable way;\n- may additionally use one or both of the following representations of the"
            " same public key:\n• the public key value itself, i.e. a ds:KeyValue element [4];\n• the related public"
            " key identifier, i.e. the X.509 Certificate Subject Key Identifier (X509SKI element [4]).\nIf public key"
            " representations are present more than once, all variants shall refer to the same public key.\nThe same"
            " public key (and hence the same certificate representing this public key) shall not appear more than"
            " once in the trusted list for the same type of service. The same public key may appear more than once in"
            " the TL only when associated to trust services having different 'Service type identifier' ('Sti') values"
            " (e.g. public key used for verifying signatures on different types of Trust Services Tokens) for which"
            " different supervision/accreditation systems apply.\nEXAMPLE 2: When a TSP is using the same private key"
            " to sign on the one hand QCs under an appropriate supervision system for qualified trust services and on"
            " the other hand to sign non-qualified certificates falling under a different supervision/accreditation"
            " system, then in this case, two entries with different 'Sti' values (e.g. respectively CA/QC and CA/PKC"
            " in the given example) and with the same public key as service digital identity would be used.\nNOTE 2:"
            " Providing two or more certificates with the same public key is not regarded as two separate"
            " identifiers, but two representations of the same identifier provided they both have identical X.509"
            " Subject Name values.\nNOTE 3: The re-keying of a trust service is resulting in using a new service"
            " entry in the trusted list (one service entry per new public key).\nWhen additional information needs to"
            " be provided with regard to the identified service entry, then, when appropriate, the TLSO shall"
            " consider the use of the 'additionalServiceInformation' extension (clause 5.5.9.4) of the 'Service"
            " information extension' field (clause 5.5.9) according to the purpose of providing such additional"
            " information. Additionally, the Scheme operator can optionally use the 'Scheme service definition URI'"
            " field (see clause 5.5.6).\nNOTE 4: The same public key, and hence private key, are not expected to be"
            " allocated to different subject names even if those names identify the same entity.\nWith regards to"
            " X.509 Certificates that are candidates to represent a public key identifying a listed service, the TLSO"
            " shall disregard certificates for which the \"O=\" attribute does not strictly match the 'TSP Name'"
            " value (clause 5.4.1) except if no candidate certificate can be found to meet such a requirement. If the"
            " TSP cannot replace the candidate certificates for which the \"O=\" attribute fails to include the 'TSP"
            " Name' value (clause 5.4.1), the TLSO may include them in the TL. When doing so, the TLSO shall provide,"
            " for such listed certificates, a formal statement in the 'Scheme service definition URI' (clause 5.5.6)"
            " indicating that they are issued to and owned by the TSP identified by the 'TSP Name' value even if the"
            " 'TSP Name' value in the TL and the \"O=\" value in the certificate differ. Those \"O=\" values distinct"
            " from the 'TSP Name' value shall then be listed as 'TSP Trade Name' values (clause 5.4.2).\nThe content"
            " of the X509SKI element shall be the same as the content of the SubjectKeyIdentifier extension of the"
            " listed certificate(s).\nTLSO and/or the body in charge to which it depends or by which it is mandated"
            " may decide to use the public key of a Root or Upper level CA from this TSP as the 'Sdi' of a single"
            " entry in the list of services from a listed TSP. The consequences (advantages and disadvantages) of"
            " such a decision shall be notified by the TLSO to the corresponding TSP. In addition, TLSOs shall"
            " provide in 'Scheme service definition URI' (clause 5.5.6) the necessary documentation to facilitate the"
            " certification path building and verification.\nEXAMPLE 3: An example of use of the public key of a Root"
            " or Upper level CA is a Certification Authority not directly issuing end-entity QCs, timestamps or other"
            " trust service outputs but certifying a hierarchy of CAs down to CAs issuing QCs to end-entities, or"
            " down to a TSU issuing timestamps, or down to units signing validation reports or other trust service"
            " outputs.\nNOTE 5: Using a RootCA public key as 'Sdi' value for a listed service will force the TLSO to"
            " consider the whole set of trust services under such a Root CA as a whole with regards to its 'service"
            " status' (clause 5.5.4). The revocation being required for one single CA under the listed root"
            " hierarchy, will force the whole hierarchy to take-on that status change.\nWhen \"Service digital"
            " identifiers\" are used as trust anchors in the context of validating electronic signatures for which"
            " signer's certificate is to be validated against TL information, only the public key and the associated"
            " subject name are needed as trust anchor information. When more than one certificate is representing the"
            " public key identifying the service, they are considered as trust anchor certificates conveying"
            " identical information with regards to the information strictly required as trust anchor information."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.5.4 (Service current status)",
        "testo": (
            "Campo obbligatorio che riporta l'identificatore dello stato corrente del servizio, espresso come URI."
            " Negli Stati membri UE, dalla data di applicazione del Reg. (UE) 910/2014, per i servizi di tipo 5.5.1.1"
            " lo stato e' 'granted' o 'withdrawn', mentre per quelli di tipo 5.5.1.2 o 5.5.1.3 e'"
            " 'recognisedatnationallevel' o 'deprecatedatnationallevel' (come definiti in D.5); i TLSO devono usare"
            " il relativo flusso di stati illustrato nella Figura 2. La migrazione dello stato dei servizi elencati"
            " nelle trusted list degli Stati membri UE al 30 giugno 2016 deve essere eseguita il 1 luglio 2016 come"
            " specificato nell'annex J; dal 1 luglio 2016 lo stato iniziale di un servizio appena approvato e'"
            " 'granted' o 'recognisedatnationallevel'. Per Paesi terzi e organizzazioni internazionali il valore di"
            " stato corrente deve essere uno dei valori specificati dal TLSO tramite lo 'Scheme information URI'"
            " (clausola 5.3.7)."
        ),
        "testo_integrale": (
            "5.5.4 Service current status: Presence: This field shall be present.\nDescription: It specifies the"
            " identifier of the current status of the service.\nFormat: An identifier expressed as an URI.\nValue: In"
            " the context of EU Member States, from the date Regulation (EU) No 910/2014 [i.10] applies:\ni) The"
            " identifier of the status of the services of a type specified in clause 5.5.1.1 shall be either"
            " \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted\" or"
            " \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn\" as defined in clause D.5.\nii) The"
            " identifier of the status of the services of a type specified in clause 5.5.1.2 or in clause 5.5.1.3"
            " shall be either \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/recognisedatnationallevel\" or"
            " \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/deprecatedatnationallevel\" as defined in clause"
            " D.5.\nThe TLSOs shall use respectively the following status flow for the allocation of those 'Service"
            " current status' values:\nFigure 2\nThe migration of the 'Service current status' value of services"
            " listed in EUMS trusted list as of the day before the date Regulation (EU) No 910/2014 [i.10] applies"
            " (i.e. 30 June 2016) shall be executed on the day the Regulation applies (i.e. 01 July 2016) as"
            " specified in annex J.\nAs from the day Regulation (EU) No 910/2014 [i.10] applies (i.e. 01 July 2016),"
            " when a trust service is first approved for being listed in the trusted list, the initial status shall"
            " be respectively \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted\" or"
            " \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/recognisedatnationallevel\".\nIn the context of"
            " non-EU countries and international organizations the current status value shall be one of the values"
            " specified by the TLSO through the 'Scheme information URI' (see clause 5.3.7)."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Negli Stati membri UE, dalla data di applicazione del Reg. (UE) 910/2014; per Paesi terzi e"
            " organizzazioni internazionali il valore ammesso e' uno di quelli definiti dal TLSO tramite lo"
            " 'Scheme information URI' (clausola 5.3.7)."
        ),
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.5.5 (Current status starting date and time)",
        "testo": (
            "Campo obbligatorio che riporta la data e l'ora in cui il corrente stato di approvazione e' divenuto"
            " efficace, in Coordinated Universal Time (formato data-ora, clausola 5.1.3). Il TLSO deve garantire la"
            " coerenza fra la (ri)emissione della trusted list e la data effettiva dell'aggiornamento di stato (es."
            " granted o withdrawn), cioe' 'List issue date and time' (clausola 5.3.14), ora di firma della trusted"
            " list e ora della modifica; la data e ora associate al nuovo stato corrente di un servizio elencato non"
            " devono essere anteriori alla data di (ri)emissione della trusted list, perche' un cambio di stato"
            " retroattivo avrebbe effetti indesiderati sulle validazioni precedenti dei servizi elencati e dei loro"
            " output. La NOTE chiarisce che i terzi affidanti possono applicare questa informazione confrontandola"
            " con altre disponibili (es. data di emissione di un certificato o di una marca temporale) per"
            " determinare se il servizio aveva lo stato di approvazione desiderato al momento della prestazione."
        ),
        "testo_integrale": (
            "5.5.5 Current status starting date and time: Presence: This field shall be present.\nDescription: It"
            " specifies the date and time on which the current approval status became effective.\nFormat: Date-time"
            " value (see clause 5.1.3).\nValue: Coordinated Universal Time (UTC) at which the current approval status"
            " became effective.\nTLSO shall ensure the consistency of the (re)-issuance of a trusted list and the"
            " actual date when a service status has been updated (e.g. granted or withdrawn), i.e. the 'List issue"
            " date and time' (clause 5.3.14), the time of signing the trusted list and the time of change. The date"
            " and time associated to the new current status of a listed service shall not be set before the date of"
            " (re)issuance of the trusted list as retroactive status change can have undesired effects to previous"
            " validations of listed services and of their outputs.\nNOTE: The relying parties can apply this"
            " information by comparing it with other available information, e.g. the date and time on which a"
            " certificate or a time-stamp was issued. From the comparison, the user can determine whether the"
            " specific service of the TSP had the desired approval status under the scheme at the date and time when"
            " the service was provided."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.5.6 (Scheme service definition URI)",
        "testo": (
            "Campo opzionale che indica gli URI presso cui i terzi affidanti possono ottenere informazioni specifiche"
            " del servizio fornite dallo scheme operator della trusted list (formato: sequenza di puntatori"
            " multilingua, clausola 5.1.4). Gli URI devono condurre a informazioni che descrivono il servizio come"
            " specificato dallo scheme; in particolare possono includere: l'URI che indica l'identita' del TSP di"
            " fallback nel caso di supervisione di un servizio in cessazione per cui sia coinvolto un TSP di"
            " fallback, e l'URI a documenti con informazioni aggiuntive sull'uso di qualificazioni specifiche"
            " definite a livello nazionale per un servizio approvato, in coerenza con l'estensione"
            " additionalServiceInformation (clausola 5.5.9.4)."
        ),
        "testo_integrale": (
            "5.5.6 Scheme service definition URI: Presence: This field is optional.\nDescription: It specifies the"
            " URI(s) where relying parties can obtain service-specific information provided by the TL scheme"
            " operator.\nFormat: A sequence of multilingual pointers (see clause 5.1.4).\nValue: The referenced"
            " URI(s) shall provide a path to information describing the service as specified by the scheme. In"
            " particular this may include:\na) URI indicating the identity of the fallback TSP in the event of the"
            " supervision of a service in cessation for which a fallback TSP is involved (see 'Service current"
            " status', clause 5.5.4);\nb) URI leading to documents providing additional information related to the"
            " use of some nationally defined specific qualification for an approved trust service token provisioning"
            " trust service in consistence with the use of 'Service information extension' field (clause 5.5.9) with"
            " an 'additionalServiceInformation' extension as defined in clause 5.5.9.4."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Campo opzionale.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.5.7 (Service supply points)",
        "testo": (
            "Campo opzionale che indica uno o piu' URI presso cui i terzi affidanti possono accedere al servizio, a"
            " servizi componenti o ad altri tipi di servizi correlati, specificando eventualmente per ciascun URI il"
            " tipo di servizio accessibile (formato: sequenza non vuota di URI, ciascuno opzionalmente precisato da"
            " un URI non vuoto). Gli URI devono specificare dove e come il servizio e' accessibile. L'EXAMPLE"
            " ufficiale illustra, per un servizio di tipo CA/QC, un URI verso testo descrittivo su autorita' di"
            " registrazione locali e procedure di rilascio dei certificati qualificati, un URI di CRL distribution"
            " point (che puo' dare accesso a un'ultima CRL finale in caso di terminazione imprevista del servizio) e"
            " un URI di un responder OCSP autorizzato, con i rispettivi tipi Certstatus/CRL/QC e Certstatus/OCSP/QC."
            " La NOTE precisa che i punti di fornitura possono essere sia per elaborazione umana sia per elaborazione"
            " automatica."
        ),
        "testo_integrale": (
            "5.5.7 Service supply points: Presence: This field is optional.\nDescription: It specifies one or more"
            " URIs where relying parties can access the service, or component services or other types of services"
            " related with the service. Optionally, for each URI it specifies the type of service that can be"
            " accessed at this URI.\nFormat: Non-empty sequence of URIs, each such URI being optionally further"
            " specified with a non-empty URI.\nValue: The referenced URI(s) shall specify where and how the service"
            " can be accessed.\nEXAMPLE: A 'Service supply points' field associated to a service (identified in"
            " 'Service digital identity', clause 5.5.3) of a type \"http://uri.etsi.org/TrstSvc/Svctype/CA/QC\" (as"
            " identified in 'Service type identifier', clause 5.5.1) could include:\n- a URI pointing towards a"
            " descriptive text where users could be given information on (local) registration authorities and"
            " procedures to follow for being issued qualified certificates;\n- a URI providing a CRL distribution"
            " point [12] giving certificate status information for qualified certificates issued by or under the"
            " service identified in 'Service digital identity', clause 5.5.3, and further specified by a type having"
            " value \"http://uri.etsi.org/TrstSvc/Svctype/Certstatus/CRL/QC\". Such URI can for example provide"
            " access to a last and final CRL in case of service unexpected termination and/or impossibility to"
            " provide such a final CRL at the CRL distribution point available from issued certificate's extensions;"
            " and/or\n- a URI providing one access location of an OCSP [i.11] responder authorized to provide"
            " certificate status information for qualified certificates issued by or under the service identified in"
            " 'Service digital identity' (clause 5.5.3), and further specified by a type having value"
            " \"http://uri.etsi.org/TrstSvc/Svctype/Certstatus/OCSP/QC\".\nNOTE: Both human processable and machine"
            " processable supply points can be provided."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Campo opzionale.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.5.8 (TSP service definition URI)",
        "testo": (
            "Campo la cui presenza e' obbligatoria quando il tipo di servizio e'"
            " 'http://uri.etsi.org/TrstSvc/Svctype/NationalRootCA-QC' (clausola 5.5.1.3) e opzionale negli altri"
            " casi; indica gli URI presso cui i terzi affidanti possono ottenere informazioni specifiche del servizio"
            " fornite dal TSP (formato: sequenza di puntatori multilingua, clausola 5.1.4). Per il tipo"
            " NationalRootCA-QC il campo deve specificare gli URI dove i terzi affidanti possono ottenere, oltre alle"
            " informazioni specifiche del servizio, dettagli sulle regole di istituzione e gestione di tali servizi e"
            " la legislazione nazionale rilevante, ove esistano regole legislative per lo scheme di root nazionale."
        ),
        "testo_integrale": (
            "5.5.8 TSP service definition URI: Presence: When the service type is"
            " \"http://uri.etsi.org/TrstSvc/Svctype/NationalRootCA-QC\" (clause 5.5.1.3), this field shall be"
            " present. In other cases, this field is optional.\nDescription: It specifies the URI(s) where relying"
            " parties can obtain service-specific information provided by the TSP.\nFormat: A sequence of"
            " multilingual pointers (see clause 5.1.4).\nValue: The referenced URI(s) shall provide a path to"
            " information describing the service as specified by the TSP.\nWhen the service type is"
            " \"http://uri.etsi.org/TrstSvc/Svctype/NationalRootCA-QC\" (clause 5.5.1.3), this field shall specify"
            " the URI(s) where relying parties can obtain service-specific information provided by the TSP including"
            " details on the establishment and management rules of such services and relevant national legislation"
            " where rules for national root scheme exist in legislation."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Obbligatorio quando il tipo di servizio e' 'http://uri.etsi.org/TrstSvc/Svctype/NationalRootCA-QC'"
            " (clausola 5.5.1.3); opzionale negli altri casi."
        ),
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI: list[dict] = []

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 5.4.1 (TSP name)",
    "clausola 5.4.2 (TSP trade name)",
    "clausola 5.4.3.0 (General)",
    "clausola 5.4.3.1 (TSP postal address)",
    "clausola 5.4.3.2 (TSP electronic address)",
    "clausola 5.4.4 (TSP information URI)",
    "clausola 5.4.5 (TSP information extensions)",
    "clausola 5.4.6 (TSP Services (list of services))",
    "clausola 5.5.1.0 (General requirements)",
    "clausola 5.5.1.1 (Regulation (EU) No 910/2014 qualified trust service types)",
    "clausola 5.5.1.2 (Regulation (EU) No 910/2014 non qualified trust service types)",
    "clausola 5.5.1.3 (Trust service types not defined in Regulation (EU) No 910/2014 but nationally defined)",
    "clausola 5.5.2 (Service name)",
    "clausola 5.5.3 (Service digital identity)",
    "clausola 5.5.4 (Service current status)",
    "clausola 5.5.5 (Current status starting date and time)",
    "clausola 5.5.6 (Scheme service definition URI)",
    "clausola 5.5.7 (Service supply points)",
    "clausola 5.5.8 (TSP service definition URI)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.1 (TSP name)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4 (Language support)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.2 (TSP trade name)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.1 (TSP name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.2 (TSP trade name)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4 (Language support)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.3.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.1 (TSP name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.3.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.3.1 (TSP postal address)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.3.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.3.2 (TSP electronic address)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.3.1 (TSP postal address)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.1 (TSP name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.3.1 (TSP postal address)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.5.1 (Scheme operator postal address)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.3.2 (TSP electronic address)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.1 (TSP name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.3.2 (TSP electronic address)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.5.2 (Scheme operator electronic address)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.4 (TSP information URI)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4 (Language support)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.6 (TSP Services (list of services))"),
        "nodo_a": ("obbligo", None, "clausola 5.3.12 (Historical information period)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.0 (General requirements)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.1 (Regulation (EU) No 910/2014 qualified trust service types)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.0 (General requirements)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.2 (Regulation (EU) No 910/2014 non qualified trust service types)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.0 (General requirements)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.3 (Trust service types not defined in Regulation (EU) No 910/2014 but nationally defined)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.1 (Regulation (EU) No 910/2014 qualified trust service types)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.1 (Regulation (EU) No 910/2014 qualified trust service types)"),
        "nodo_a": ("principio", None, "clausola 5.5.9 (Service information extensions)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.1 (Regulation (EU) No 910/2014 qualified trust service types)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.4 (additionalServiceInformation Extension)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.1 (Regulation (EU) No 910/2014 qualified trust service types)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.10 (Scheme territory)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.1 (Regulation (EU) No 910/2014 qualified trust service types)"),
        "nodo_a": ("obbligo", None, "Annex D.4 (Common trusted lists URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.2 (Regulation (EU) No 910/2014 non qualified trust service types)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.2 (Regulation (EU) No 910/2014 non qualified trust service types)"),
        "nodo_a": ("principio", None, "clausola 5.5.9 (Service information extensions)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.2 (Regulation (EU) No 910/2014 non qualified trust service types)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.4 (additionalServiceInformation Extension)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.3 (Trust service types not defined in Regulation (EU) No 910/2014 but nationally defined)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.3 (Trust service types not defined in Regulation (EU) No 910/2014 but nationally defined)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.6 (Scheme service definition URI)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.3 (Trust service types not defined in Regulation (EU) No 910/2014 but nationally defined)"),
        "nodo_a": ("principio", None, "clausola 5.5.9 (Service information extensions)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2 (Service name)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.1 (TSP name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2 (Service name)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4 (Language support)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "nodo_a": ("principio", None, "clausola 5.5.9 (Service information extensions)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.4 (additionalServiceInformation Extension)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.6 (Scheme service definition URI)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.1 (TSP name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.2 (TSP trade name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.4 (Service current status)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.4 (Service current status)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.1 (Regulation (EU) No 910/2014 qualified trust service types)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.4 (Service current status)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.2 (Regulation (EU) No 910/2014 non qualified trust service types)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.4 (Service current status)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.3 (Trust service types not defined in Regulation (EU) No 910/2014 but nationally defined)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.4 (Service current status)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.7 (Scheme information URI)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.4 (Service current status)"),
        "nodo_a": ("principio", None, "Annex D.5 (EU specific trusted lists URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.4 (Service current status)"),
        "nodo_a": ("obbligo", None, "Annex J (Migration of EU MS trusted lists in the context of Regulation (EU) No 910/2014)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.5 (Current status starting date and time)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.3 (Date-time indication)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.5 (Current status starting date and time)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.14 (List issue date and time)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.6 (Scheme service definition URI)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4 (Language support)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.6 (Scheme service definition URI)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.4 (Service current status)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.6 (Scheme service definition URI)"),
        "nodo_a": ("principio", None, "clausola 5.5.9 (Service information extensions)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.6 (Scheme service definition URI)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.4 (additionalServiceInformation Extension)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.7 (Service supply points)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.8 (TSP service definition URI)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.3 (Trust service types not defined in Regulation (EU) No 910/2014 but nationally defined)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.8 (TSP service definition URI)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4 (Language support)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
