"""ETSI TS 119 432 V1.3.1 (2026-03) - Electronic Signatures and Trust
Infrastructures (ESI); Protocols for remote digital signature creation.
Fonte 20 (la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 5:
clausola 7 (Remote signatures creation service API: 7.1 Introduction, 7.2
Service information API, 7.3 Credentials list API, 7.4 Credentials info API,
7.5 Hash(es) signing API, 7.6 Document(s) signing API, 7.7 Signature(s)
creation polling API, 7.8 Credentials creation API, 7.9 Credentials deletion
API) e clausola 8 (Remote signatures creation service API based on OASIS
DSS-X: 8.1 Introduction and General Provisions, 8.2-8.8). Documento unico
(non multi-parte): i `riferimento` NON portano prefisso di Parte. Testo
ufficiale in app/.source_cache/etsi_119_432/cap05.txt (letto sempre con
selettore `:raw`, altrimenti il tool tronca le righe lunghe a 768 caratteri
introducendo "..." e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_119_432/manifest.json.

Modellazione (ADR-0007), stesso criterio gia' applicato alle altre fonti ETSI
gia' censite (ETSI EN 319 401, ETSI EN 319 412, ETSI EN 319 421, ETSI EN 319
422, ETSI TS 119 431-1, ETSI TS 119 461) e alle clausole gia' importate di
questa Fonte (cap01, cap02, cap03): un nodo per ogni clausola/sottoclavola
numerata che porta contenuto proprio; le intestazioni di puro raggruppamento
non generano ne' nodo ne' item di indice. Questo capitolo produce 31 Obblighi
e 3 Principi su 34 item di indice. Scelte voce per voce:

CLAUSOLA 7 - API DI CREAZIONE DI FIRME REMOTE

- Clausola 7.1 (Introduction) -> 1 Principio "definitorio", riferimento
  "clausola 7.1 (Introduction)". La clausola inquadra l'API (il modo con cui
  una driving application interagisce con un SCS conforme al documento; le
  coppie messaggio di richiesta/risposta sono specificate rinviando a CSC API
  [1] quando possibile, altrimenti dettagliando nuovi componenti in una
  tabella con nome, presenza, tipo e breve descrizione del componente) e
  contiene la Tabella 1, che DEFINISCE il significato dei valori della colonna
  "Presence" usata da tutte le tabelle della clausola 7: M = il componente
  DEVE essere incluso nella richiesta o risposta all'SCS; O = il componente
  PUO' essere incluso; C = il componente DEVE essere incluso in base al
  verificarsi di determinate condizioni. Il contenuto sostanziale della
  clausola e' quindi una definizione di notazione (il "shall" della Tabella 1
  definisce il valore "M", non impone un comportamento a un soggetto
  identificabile): "definitorio" e' il tipo corretto, non "altro" (che resta
  riservato ai blocchi descrittivi/esemplificativi privi di contenuto
  definitorio) ne' "scopo/ambito di applicazione" (la clausola non delimita
  cio' che il documento copre, spiega come sono costruite le tabelle delle
  clausole successive). Nessun soggetto obbligato: Principio e non Obbligo.
  `oggetti_giuridici`: "servizio di gestione di dispositivo di creazione di
  firma elettronica a distanza" (l'API e' l'interfaccia del servizio di
  creazione di firme remote) e "firma elettronica avanzata" (le firme create
  per il tramite di quell'API sono AdES), stessa coppia gia' usata in
  cap02/cap03 di questa Fonte per le clausole sull'API del servizio.
- Clausole 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8 e 7.9 (le otto sezioni "Service
  information API" ... "Credentials deletion API") -> per ciascuna: 1 Obbligo
  per la sottoclausola x.1 (Description), 1 Obbligo per x.2.1 (Component for
  requesting ...) e 1 Obbligo per x.3.1 (Component for responding to ...), per
  un totale di 24 Obblighi; la clausola 7.8 ha una quarta sottoclausola 7.8.4
  (Subject distinguished name of the new credential certificate) -> 1 ulteriore
  Obbligo (25 Obblighi nella clausola 7). Tutti "tecnico/sicurezza", soggetto
  "QTSP/gestore" obbligato (il prestatore del servizio di creazione di firme,
  cioe' l'implementazione del servizio e della sua interfaccia API).
  Motivazione del tipo: le prescrizioni vincolano l'interfaccia del servizio e
  il contenuto dei messaggi di protocollo ("The <API> API method referenced in
  CSC API [1], clause X shall be applied and fully implemented/may be
  implemented"; "The message for requesting/returning ... shall contain the
  components defined in CSC API [1], clause X section Input/Output"), non un
  adempimento organizzativo, informativo, procedurale o di conservazione.
  Le sottoclausole x.1 sono prescrittive perche' contengono un "shall" con
  soggetto identificabile (il servizio), anche quando sono intitolate
  "Description" e iniziano con una frase dichiarativa ("Returns information
  about the remote service and the list of the API methods it supports"):
  criterio decisivo identico a quello adottato in cap02 per la clausola 5.1
  (Introduction). Le clausole indivisibili accorpano in un unico nodo la
  prosa descrittiva, i "shall" e le permissioni "need not be supported"
  (nessuna numerazione interna). Soggetto aggiuntivo "Terza parte" obbligato
  SOLO in 7.5.1 e 7.6.1, dove il testo impone un comportamento all'APPLICAZIONE
  DRIVER ("The driving application shall pass the authorization data that
  allows the signing credential usage"): la driving application non e' ne' il
  QTSP ne' l'utente, stessa convenzione gia' adottata in cap02 di questa Fonte
  per la clausola 5.1 (e in etsi_119_461/cap06.py, agid_reg_tec_cert_cap/cap03.py,
  reg_ue_2025_1566/cap01.py). Nessun ruolo "destinatario": in questo capitolo
  non ci sono "should inform" verso terzi.
- Clausola 7.8.4 (Subject distinguished name of the new credential certificate)
  -> 1 Obbligo "tecnico/sicurezza", soggetto QTSP/gestore obbligato. E' una
  sottoclausola di quarto livello con numerazione propria: prescrive che il
  servizio di creazione di firma remota DEVE supportare il parametro
  subjectData di credentialCreationRequest per costruire il subject
  distinguished name del certificato della nuova credenziale; quando sono
  supportate le Rich Authorization Requests DEVE supportare la ricezione dei
  subject data dal server di autorizzazione negli authorization details
  dell'access token (notazione dei claim OIDC) e PUO' supportarne la ricezione
  come claim personalizzati o via token introspection endpoint; PUO' ignorare
  o sovrascrivere i dati forniti con subjectData. Fissa inoltre il regime dei
  subject data espressi con claim OIDC standard: DEVE raccogliere given_name,
  family_name, gender, birthdate, address:country; DOVREBBE raccogliere sub;
  PUO' raccogliere address:locality, address:region, email. Nessun nodo
  separato per il "should" su sub: la sottoclausola e' indivisibile e i tre
  livelli modali (shall/should/may) si applicano a elenchi di dati interni
  alla stessa prescrizione, non a clausole autonome.
- Esclusioni nella clausola 7: le intestazioni "7 Remote signatures creation
  service API", "7.2 Service information API" ... "7.9 Credentials deletion
  API", nonche' ogni "7.x.2 Request message" e "7.x.3 Response message", NON
  generano nodo ne' item di indice: sono intestazioni di puro raggruppamento,
  il cui contenuto proprio e' interamente nelle sottoclausole numerate
  (x.2.1/x.3.1) che seguono immediatamente. Le figure/Tabelle 1 e 2 restano
  nel `testo_integrale` della clausola che le contiene (7.1 e 7.2.3.1), senza
  generare nodi propri: non hanno numerazione di clausola.

CLAUSOLA 8 - API BASATA SU OASIS DSS-X

- Clausola 8.1 (Introduction and General Provisions) -> 1 OBBLIGO
  "tecnico/sicurezza", soggetto QTSP/gestore obbligato. Classificazione
  ambigua risolta in favore di Obbligo con lo stesso criterio di cap02
  (clausola 5.1): la clausola e' intitolata "Introduction and General
  Provisions" e contiene ampie parti dichiarative (descrizione dell'API come
  interfaccia di un'applicazione client verso un SCS; ordine di presentazione
  degli elementi DSS-X modellato su quello degli elementi CSC API; NOTE 1 e 2
  su paradigmi di progettazione diversi e sulla sintassi astratta con
  mappatura XML/JSON; raccomandazione del binding HTTP Post; elenco dei
  meccanismi di trasmissione dei signature activation data), MA contiene due
  "shall" con soggetto identificabile: "Reliable DSS-X security bindings shall
  apply to all protocol messages in the context of the present document" e
  "The service metadata (see clauses 8.2 and 8.3 of the present document)
  shall provide details regarding the applicable mechanism" - e' il criterio
  decisivo di ADR-0007. La clausola e' indivisibile (nessuna numerazione
  propria delle frasi) e viene quindi accorpata in un unico nodo, con il resto
  del testo nella sintesi e in `testo_integrale`. tipo_obbligo
  "tecnico/sicurezza": il contenuto prescrittivo riguarda i binding di
  sicurezza dei messaggi di protocollo e il contenuto informativo dei
  metadati del servizio.
- Clausole 8.2.1, 8.3.1, 8.5.1, 8.6.1, 8.7.1 (Description delle sezioni 8.2,
  8.3, 8.5, 8.6, 8.7) -> 5 Obblighi "tecnico/sicurezza", soggetto QTSP/gestore
  obbligato. Ciascuna contiene "shall" con soggetto identificabile (il
  servizio e i suoi metadati) che rinviano a elementi OASIS DSS-X esterni:
  8.2.1 (la specifica dei nomi degli elementi della clausola 3.2 di [5] DEVE
  applicarsi; un'istanza di metadati DEVE essere completa quanto necessario;
  per l'individuazione dei metadati DEVE applicarsi il meccanismo della
  clausola 4 di [5]); 8.3.1 (i metadati DEVONO indicare, tramite la clausola
  3.1.5 di [5], quale degli approcci di disponibilita' del certificato del
  firmatario il servizio supporta); 8.5.1 (DEVE applicarsi la SignRequest con
  la variante DocumentHash di InputDocuments; KeySelector DEVE applicarsi se
  la chiave non e' determinabile implicitamente); 8.6.1 (DEVE applicarsi la
  SignRequest con la variante Document; TransformedData PUO' essere piu'
  appropriata per DTBS complessi, in particolare XAdES, ed e' ammissibile;
  KeySelector DEVE applicarsi se la chiave non e' determinabile
  implicitamente); 8.7.1 (DEVE applicarsi l'elemento PendingRequest). Le parti
  dichiarative (descrizione della funzione dell'API, motivazione della scelta
  di DSS-X, elenco di approcci alternativi) restano assorbite nello stesso
  nodo perche' le clausole sono indivisibili.
- Clausola 8.4.1 (Description) -> 1 Principio "altro", riferimento "clausola
  8.4.1 (Description)". La clausola e' interamente dichiarativa - "Retrieves a
  credential and returns information about signing certificate and
  authorization mechanisms required to authorize the usage of the credential
  for remote signing." - seguita da un rinvio letterale alla clausola 8.3
  della stessa Fonte ("See clause 8.3 of the present document."). Nessun
  "shall"/"should", nessun soggetto obbligato: e' la descrizione della
  funzione dell'API e del suo rapporto con la clausola 8.3, quindi Principio
  "altro" e non Obbligo. Il rinvio interno genera una relazione (v. sotto).
- Clausola 8.8.1 (Description) -> 1 Principio "altro", riferimento "clausola
  8.8.1 (Description)". Dichiarativa e priva di verbo prescrittivo: constata
  che l'API credentials/create crea una nuova credenziale di firma, che
  OASIS DSS-X non fornisce un'API specifica di creazione del certificato del
  firmatario (la creazione avviene implicitamente quando l'implementazione
  della SignRequest crea il certificato al volo per uso singolo, previo
  consenso dell'utente, mentre la creazione di certificati di firmatario
  validi a lungo termine e' oggetto di un processo PKI dedicato fuori dal
  perimetro del processo di creazione di firma) e che, di conseguenza, nel
  profilo DSS-X del presente documento un'API di creazione di credenziali NON
  e' applicabile. La constatazione di non applicabilita' non impone alcun
  comportamento: Principio "altro".
- Esclusioni nella clausola 8: le intestazioni "8 Remote signatures creation
  service API based on OASIS DSS-X" e "8.2 Service information API" ...
  "8.8 Credentials creation API" NON generano nodo ne' item di indice
  (raggruppamento puro: il contenuto e' nelle rispettive x.1). Le sezioni 8.2,
  8.3, 8.4, 8.5, 8.6, 8.7, 8.8 hanno una sola sottoclausola di contenuto
  (x.1) e quindi un solo nodo ciascuna.

PERIMETRO ED ESCLUSIONI GENERALI: restano fuori da questo modulo la clausola 6
(Architectures and use cases for server signing, in cap04), gli Annex A/B/C
(cap06/cap07), il front matter non numerato (IPR, Foreword, Modal verbs
terminology, Executive summary, Introduction), la clausola 2 (References:
bibliografia/paratesto) e la clausola 3 (definizioni, in cap01), nonche'
Annex D (Change history) e "History". Nessun nodo di questo capitolo copre
clausole di altri capitoli della stessa Fonte.

COMPLETEZZA VERBATIM (ADR-0010): i `testo_integrale` sono copie letterali
integrali delle clausole, con la sola normalizzazione degli spazi di
impaginazione (righe del PDF unite, "•" reso "-", interruzioni di pagina e
paratesto spurio "ETSI" / "ETSI TS 119 432 V1.3.1 (2026-03)" / numeri di
pagina / "<!-- Page N -->" rimossi), senza omettere NOTE, tabelle o elenchi
puntati. Il testo ufficiale di questo capitolo non contiene alcun marcatore di
elisione (nessun blocco EXAMPLE con payload abbreviati): la terza convenzione
di esenzione della guardia `verifica_completezza_testo_integrale` non trova
qui alcuna occorrenza, quindi nessun `...` e' presente nei `testo_integrale`.
Due refusi del documento ufficiale sono riprodotti letteralmente (mai
corretti, per ADR-0010): il titolo della clausola 7.9.2.1 e' "Component for
requesting credential creation" pur disciplinando la CANCELLAZIONE di una
credenziale, e il testo di 7.6.2.1 dice "The message for requesting the
hash(es) signature creation" pur trattando la creazione di firme su DOCUMENTI
(clausola 11.14 di CSC API, signatures/signDoc).

`condizione_applicabilita`: non valorizzata su nessuna riga. Le condizioni
presenti nel perimetro (7.5.3.1/7.6.3.1 "if the input parameter operationMode
is not supported"; 7.7.1 "unless signatures creation in asynchronous operation
mode is supported by the SSASC"; 7.8.4 "When Rich Authorization Requests (RAR)
are supported") condizionano singole sotto-prescrizioni interne a clausole
indivisibili, non l'intera riga: valorizzarle sull'intero nodo lo
presenterebbe come requisito condizionale nella sua interezza, cosa che il
testo non dice (stesso ragionamento di cap03).

`severita`/`sanzioni`: non valorizzati. E' uno standard tecnico ETSI privo di
apparato sanzionatorio proprio.

`stato`: "vigente" su tutte le righe (nessuna evidenza di abrogazione o di
transizione eIDAS->eIDAS2 in questo capitolo).

RELAZIONI interne (8): solo citazioni letterali di clausole della STESSA
Fonte, con `fonte_id_o_None = None`; nessuna relazione cross-fonte (Fase 6,
ADR-0009). Tutti i rinvii delle clausole 7.x e di 8.2.1/8.3.1/8.5.1/8.6.1/
8.7.1 sono a documenti ESTERNI (CSC API [1] clausole 11.1/11.4/11.5/11.6/
11.7/11.13/11.14/11.15, OASIS DSS-X [4] e il suo documento complementare [5],
IETF RFC 9110 [16], IETF RFC 9449 [25], OIDC) e non generano relazioni.
Le sole citazioni interne sono nella clausola 8.1 e in 8.4.1:
- 8.1 -> 7.1: "in the order of the above-cited CSC API elements (see clause 7
  of the present document)". Il rinvio e' alla clausola 7 NEL SUO COMPLESSO,
  che il grafo non censisce come nodo (intestazione di puro raggruppamento):
  la relazione punta al nodo di ingresso della clausola 7, cioe' la clausola
  7.1 (Introduction) che ne enuncia l'impianto, con `evidence_type`
  "inferred" perche' la citazione e' letterale ma la risoluzione al singolo
  nodo e' un'inferenza dell'estrazione. Non si emette un fan-out verso tutti i
  25 nodi della clausola 7: il rinvio e' di ordinamento espositivo, non
  un'incorporazione dei requisiti (a differenza del caso di
  etsi_319_422/cap05_relazioni_cross.py, dove "shall apply" incorpora davvero
  ogni requisito della clausola citata).
- 8.1 -> 8.2.1 e 8.1 -> 8.3.1: "The service metadata (see clauses 8.2 and 8.3
  of the present document) shall provide details ...". Ciascuna delle clausole
  citate ha un solo nodo di contenuto proprio (8.2.1, 8.3.1), quindi la
  risoluzione e' univoca -> `evidence_type` "textual".
- 8.1 -> 8.4.1, 8.1 -> 8.5.1, 8.1 -> 8.6.1, 8.1 -> 8.7.1: "can identify the
  signatory regarding service calls described in clauses 8.3, 8.4, 8.5, 8.6
  and 8.7 of the present document". La clausola 8.3 e' gia' coperta dalla
  relazione 8.1 -> 8.3.1 (una sola relazione per coppia nodo_da/nodo_a/tipo,
  nessun arco duplicato); le clausole 8.4-8.7 hanno un solo nodo di contenuto
  ciascuna -> `evidence_type` "textual".
- 8.4.1 -> 8.3.1: "See clause 8.3 of the present document." Unico nodo della
  clausola 8.3 e' 8.3.1 -> `evidence_type` "textual".
Tutte le relazioni sono di tipo "richiama" (rinvio a un'altra clausola della
stessa Fonte, senza incorporazione ne' modifica). `confidence` resta None:
non esiste uno score reale da registrare e non va inventato (ADR-0005).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "clausola 7.2.1 (Description)",
        "testo": (
            "L'API di informazione del servizio restituisce informazioni sul servizio remoto e l'elenco dei "
            "metodi API che supporta. Il metodo info di CSC API, clausola 11.1, DEVE essere applicato e "
            "integralmente implementato per garantire la conformita' al presente documento."
        ),
        "testo_integrale": (
            "7.2.1 Description: Returns information about the remote service and the list of the API methods "
            "it supports. The info API method referenced in CSC API [1], Clause 11.1 shall be applied and "
            "fully implemented to ensure compliance with the present document."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.2.2.1 (Component for requesting service information)",
        "testo": (
            "Il messaggio per richiedere le informazioni sul servizio DEVE contenere i componenti definiti "
            "nella clausola 11.1, section Input, di CSC API."
        ),
        "testo_integrale": (
            "7.2.2.1 Component for requesting service information: The message for requesting the service "
            "information shall contain the components defined in CSC API [1], clause 11.1 section Input."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.2.3.1 (Component for responding to service information requests)",
        "testo": (
            "Il messaggio di ritorno delle informazioni sul servizio DEVE contenere i componenti definiti "
            "nella clausola 11.1, section Output, di CSC API, con l'aggiunta dei componenti della Tabella 2: "
            "il parametro opzionale oauth2FAPIsupport (booleano) DEVE valere \"true\" se l'authorization "
            "server dell'SCS supporta il FAPI 2.0 Security Profile e puo' autenticare i client con "
            "private_key_jwt come specificato nella Section 9 di OIDC ed emettere access token "
            "sender-constrained secondo il metodo DPoP descritto in IETF RFC 9449."
        ),
        "testo_integrale": (
            "7.2.3.1 Component for responding to service information requests: The message for returning the "
            "service information shall contain the components defined in CSC API [1], clause 11.1 section "
            "Output with the addition of the components defined in Table 2.\n\n"
            "**Table 2**\n\n"
            "|Parameter|Presence|Type|Description|\n"
            "|---|---|---|---|\n"
            "|oauth2FAPIsupport|O|boolean|This parameter shall be \"true\" if the SCS authorization server "
            "supports the FAPI 2.0 Security Profile and can - authenticate clients using private_key_jwt as "
            "specified in Section 9 of OIDC; - issue sender-constrained access tokens according to DPoP "
            "method as described in IETF RFC 9449 [25].|"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.3.1 (Description)",
        "testo": (
            "L'API restituisce l'elenco delle credenziali di un certo utente (un utente puo' avere una o piu' "
            "credenziali ospitate da un unico RSSP). Se richiesto, DEVE restituire anche informazioni sui "
            "certificati di firma e/o sui meccanismi di autorizzazione necessari ad autorizzare l'uso delle "
            "credenziali per la firma remota. Il metodo credentials/list di CSC API, clausola 11.6, DEVE "
            "essere applicato e integralmente implementato per garantire la conformita' alla presente "
            "specifica."
        ),
        "testo_integrale": (
            "7.3.1 Description: Returns the list of credentials of a certain user. A user may have one or "
            "multiple credentials hosted by a single RSSP.\n\n"
            "If requested, it shall also return information about the signing certificate(s) and/or about the "
            "authorization mechanisms required to authorize the usage of the credentials for remote signing."
            "\n\n"
            "The credentials/list API method referenced in CSC API [1], clause 11.6 shall be applied and fully "
            "implemented to ensure compliance with the present specification."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.3.2.1 (Component for requesting credentials list)",
        "testo": (
            "Il messaggio per richiedere l'elenco delle credenziali DEVE contenere i componenti definiti "
            "nella clausola 11.6, section Input, di CSC API; il parametro onlyValid non deve necessariamente "
            "essere supportato."
        ),
        "testo_integrale": (
            "7.3.2.1 Component for requesting credentials list: The message for requesting the list of "
            "credentials shall contain the components defined in CSC API [1], clause 11.6 section Input. The "
            "parameter onlyValid needs not be supported."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.3.3.1 (Component for responding to credentials list requests)",
        "testo": (
            "Il messaggio di ritorno dell'elenco di credenziali richiesto DEVE contenere i componenti "
            "definiti nella clausola 11.6, section Output, di CSC API; il parametro onlyValid non deve "
            "necessariamente essere supportato se non e' supportato il parametro di input omonimo."
        ),
        "testo_integrale": (
            "7.3.3.1 Component for responding to credentials list requests: The message for returning the "
            "requested list of credentials information shall contain the components defined in CSC API [1], "
            "clause 11.6 section Output. The parameter onlyValid needs not be supported if the input "
            "parameter of the same name is not supported."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.4.1 (Description)",
        "testo": (
            "L'API recupera una credenziale e restituisce informazioni sul certificato di firma e sui "
            "meccanismi di autorizzazione necessari ad autorizzare l'uso della credenziale per la firma "
            "remota. Il metodo credentials/info di CSC API, clausola 11.7, DEVE essere applicato e puo' essere "
            "implementato per garantire la conformita' al presente documento."
        ),
        "testo_integrale": (
            "7.4.1 Description: Retrieves a credential and returns information about signing certificate and "
            "authorization mechanisms required to authorize the usage of the credential for remote signing."
            "\n\n"
            "The credentials/info API method referenced in CSC API [1], clause 11.7 shall be applied and may "
            "be implemented to ensure compliance with the present document."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.4.2.1 (Component for requesting credential information)",
        "testo": (
            "Il messaggio per richiedere le informazioni su una credenziale DEVE contenere i componenti "
            "definiti nella clausola 11.7, section Input, di CSC API."
        ),
        "testo_integrale": (
            "7.4.2.1 Component for requesting credential information: The message for requesting the "
            "information about a credential shall contain the components defined in CSC API [1], clause 11.7 "
            "section Input."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.4.3.1 (Component for responding to credential information requests)",
        "testo": (
            "Il messaggio di ritorno delle informazioni sul servizio DEVE contenere i componenti definiti "
            "nella clausola 11.7, section Output, di CSC API."
        ),
        "testo_integrale": (
            "7.4.3.1 Component for responding to credential information requests: The message for returning "
            "the service information shall contain the components defined in CSC API [1], clause 11.7 section "
            "Output."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.5.1 (Description)",
        "testo": (
            "L'API calcola la firma digitale di uno o piu' valori di hash. L'applicazione driver DEVE "
            "trasmettere i dati di autorizzazione che consentono l'uso della credenziale di firma. Il metodo "
            "signatures/signHash di CSC API, clausola 11.13, DEVE essere applicato e integralmente "
            "implementato per garantire la conformita' alla presente specifica."
        ),
        "testo_integrale": (
            "7.5.1 Description: Computes the digital signature of one or multiple hash values. The driving "
            "application shall pass the authorization data that allows the signing credential usage.\n\n"
            "The signatures/signHash API method referenced in CSC API [1], clause 11.13 shall be applied and "
            "fully implemented to ensure compliance with the present specification."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 7.5.2.1 (Component for requesting hash(es) signature creation)",
        "testo": (
            "Il messaggio per richiedere la creazione della firma di uno o piu' hash DEVE contenere i "
            "componenti definiti nella clausola 11.13, section Input, di CSC API; i parametri operationMode, "
            "validity_period e response_uri non devono necessariamente essere supportati, cosi' che solo la "
            "modalita' operativa sincrona DEVE essere supportata dall'SSASC."
        ),
        "testo_integrale": (
            "7.5.2.1 Component for requesting hash(es) signature creation: The message for requesting the "
            "hash(es) signature creation shall contain the components defined in CSC API [1], clause 11.13 "
            "section Input. The parameters operationMode, validity_period and response_uri need not be "
            "supported, so that only synchronous operation mode shall be supported by the SSASC."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.5.3.1 (Component for responding to hash(es) signature creation requests)",
        "testo": (
            "Il messaggio di ritorno degli hash firmati DEVE contenere i componenti definiti nella clausola "
            "11.13, section Output, di CSC API; il parametro responseID non deve necessariamente essere "
            "supportato se non e' supportato il parametro di input operationMode."
        ),
        "testo_integrale": (
            "7.5.3.1 Component for responding to hash(es) signature creation requests: The message for "
            "returning the signed hash(es) shall contain the components defined in CSC API [1], clause 11.13 "
            "section Output. The parameter responseID needs not be supported if the input parameter "
            "operationMode is not supported."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.6.1 (Description)",
        "testo": (
            "L'API crea una o piu' firme AdES. L'applicazione driver DEVE trasmettere i dati di "
            "autorizzazione che consentono l'uso della credenziale di firma. Il metodo signatures/signDoc di "
            "CSC API, clausola 11.14, DEVE essere applicato e dovrebbe essere implementato per garantire la "
            "conformita' alla presente specifica."
        ),
        "testo_integrale": (
            "7.6.1 Description: Creates one or more AdES signatures. The driving application shall pass the "
            "authorization data that allows the signing credential usage.\n\n"
            "The signatures/signDoc API method referenced in CSC API [1], clause 11.14 shall be applied and "
            "should be implemented to ensure compliance with the present specification."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 7.6.2.1 (Component for requesting documents signature creation)",
        "testo": (
            "Il messaggio per richiedere la creazione della firma di uno o piu' hash DEVE contenere i "
            "componenti definiti nella clausola 11.14, section Input, di CSC API; i parametri operationMode, "
            "validity_period e response_uri non devono necessariamente essere supportati, cosi' che solo la "
            "modalita' operativa sincrona DEVE essere supportata dall'SSASC; non devono necessariamente "
            "essere supportati i valori \"C\", \"X\" e \"J\" assegnabili al parametro signature_format "
            "dell'oggetto adesParameters che compone l'oggetto signatureCreationRequest, ne' i valori "
            "\"AdES-B\", \"AdES-T\", \"AdES-LT\" e \"AdES-LTA\" assegnabili al parametro conformance_level "
            "del medesimo oggetto."
        ),
        "testo_integrale": (
            "7.6.2.1 Component for requesting documents signature creation: The message for requesting the "
            "hash(es) signature creation shall contain the components defined in CSC API [1], clause 11.14 "
            "section Input. The parameters operationMode, validity_period and response_uri need not be "
            "supported, so that only synchronous operation mode shall be supported by the SSASC. The values "
            "\"C\", \"X\" and \"J\" that can be assigned to the parameter signature_format defined in the "
            "object adesParameters that is one of the objects that compose the object signatureCreationRequest "
            "need not be supported. The values \"AdES-B\", \"AdES-T\", \"AdES-LT\" and \"AdES-LTA\" that can "
            "be assigned to the parameter conformance_level defined in the object adesParameters that is one "
            "of the objects that compose the object signatureCreationRequest need not be supported."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.6.3.1 (Component for responding to documents signature creation requests)",
        "testo": (
            "Il messaggio di ritorno degli hash firmati DEVE contenere i componenti definiti nella clausola "
            "11.14, section Output, di CSC API; il parametro responseID non deve necessariamente essere "
            "supportato se non e' supportato il parametro di input operationMode."
        ),
        "testo_integrale": (
            "7.6.3.1 Component for responding to documents signature creation requests: The message for "
            "returning the signed hash(es) shall contain the components defined in CSC API [1], clause 11.14 "
            "section Output. The parameter responseID needs not be supported if the input parameter "
            "operationMode is not supported."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.7.1 (Description)",
        "testo": (
            "L'API restituisce l'esito corrispondente a una precedente richiesta di creazione di firme "
            "elaborata in modalita' asincrona, oppure l'indicazione che il processo di firma non e' ancora "
            "stato completato. Il metodo signatures/signPolling di CSC API, clausola 11.15, DEVE essere "
            "applicato; il medesimo metodo non deve necessariamente essere supportato, a meno che la creazione "
            "di firme in modalita' operativa asincrona sia supportata dall'SSASC."
        ),
        "testo_integrale": (
            "7.7.1 Description: Returns the outcome corresponding to a previous signature(s) creation request "
            "when processed in asynchronous mode or the indication that the signing process has not yet been "
            "completed.\n\n"
            "The signatures/signPolling API method referenced in CSC API [1], clause 11.15 shall be applied. "
            "The signatures/signPolling API method needs not be supported, unless signatures creation in "
            "asynchronous operation mode is supported by the SSASC."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.7.2.1 (Component for polling previous signature creation requests)",
        "testo": (
            "Il messaggio per richiedere le risposte corrispondenti a una precedente richiesta di creazione "
            "di firme DEVE contenere i componenti definiti nella clausola 11.15, section Input, di CSC API."
        ),
        "testo_integrale": (
            "7.7.2.1 Component for polling previous signature creation requests: The message for requesting "
            "the responses corresponding to a previous signature(s) creation request shall contain the "
            "components defined in CSC API [1], clause 11.15 section Input."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.7.3.1 (Component for responding to polling previous signature creation requests)",
        "testo": (
            "Il messaggio di ritorno dell'esito di una precedente richiesta di creazione di firme DEVE "
            "contenere i componenti definiti nella clausola 11.15, section Output, di CSC API."
        ),
        "testo_integrale": (
            "7.7.3.1 Component for responding to polling previous signature creation requests: The message "
            "for returning the outcome of a previous signature creation request shall contain the components "
            "defined in CSC API [1], clause 11.15 section Output."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.8.1 (Description)",
        "testo": (
            "Il metodo credentials/create di CSC API, clausola 11.4, crea una nuova credenziale di firma; se "
            "richiesto puo' anche restituire il nuovo certificato di firma, l'intera catena di certificati "
            "associata, informazioni aggiuntive sul certificato di firma e/o informazioni sul meccanismo di "
            "autorizzazione richiesto per autorizzare l'accesso alla credenziale per la firma remota. Il "
            "metodo richiede un'autorizzazione alla creazione di credenziali. Il servizio di creazione di "
            "firma remota DEVE raccogliere i subject data necessari al certificato della nuova credenziale. "
            "Il metodo credentials/create DEVE essere applicato e integralmente implementato per garantire la "
            "conformita' alla presente specifica."
        ),
        "testo_integrale": (
            "7.8.1 Description: The credentials/create API method identified in CSC API [1], clause 11.4 "
            "creates a new signing credential. If requested, it can also return the new signing certificate, "
            "the whole associated certificate chain, additional information about the signing certificate "
            "and/or information about the authorization mechanism required to authorize the access to the "
            "credential for remote signing.\n\n"
            "This method requires credential creation authorization.\n\n"
            "The remote signature creation service shall collect the subject data needed for the certificate "
            "for the new credential.\n\n"
            "The credentials/create API method referenced in CSC API [1], clause 11.4, shall be applied and "
            "fully implemented to ensure compliance with the present specification."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.8.2.1 (Component for requesting credential creation)",
        "testo": (
            "Il messaggio per richiedere la creazione di una credenziale DEVE contenere i componenti definiti "
            "nella clausola 11.4, section Input, di CSC API."
        ),
        "testo_integrale": (
            "7.8.2.1 Component for requesting credential creation: The message for requesting a credential "
            "creation shall contain the components defined in CSC API [1], clause 11.4 section Input."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.8.3.1 (Component for responding to credential creation requests)",
        "testo": (
            "Il messaggio di ritorno delle informazioni sulla credenziale appena creata DEVE contenere i "
            "componenti definiti nella clausola 11.4, section Output, di CSC API."
        ),
        "testo_integrale": (
            "7.8.3.1 Component for responding to credential creation requests: The message for returning the "
            "information of the newly created credential shall contain the components defined in CSC API [1], "
            "clause 11.4 section Output."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.8.4 (Subject distinguished name of the new credential certificate)",
        "testo": (
            "Il servizio di creazione di firma remota DEVE supportare il parametro subjectData dato nel "
            "parametro di input credentialCreationRequest, per costruire il subject distinguished name del "
            "certificato della nuova credenziale. Quando sono supportate le Rich Authorization Requests "
            "(RAR), il servizio DEVE supportare la ricezione dei subject data necessari a costruire il "
            "subject distinguished name dal server di autorizzazione, negli authorization details del token "
            "di accesso espressi con la notazione dei claim OIDC, e PUO' supportarne la ricezione come claim "
            "personalizzati nel token di accesso o il recupero da un token introspection endpoint; il "
            "servizio PUO' inoltre ignorare o sovrascrivere in tutto o in parte i subject distinguished name "
            "data forniti con il parametro subjectData. Devono essere raccolti i subject data espressi con i "
            "claim OIDC standard given_name, family_name, gender, birthdate e address:country; dovrebbe "
            "essere raccolto sub (se fornito, DEVE contenere un identificatore univoco del soggetto assegnato "
            "da un'autorita' governativa o civile); possono essere raccolti address:locality, address:region "
            "ed email."
        ),
        "testo_integrale": (
            "7.8.4 Subject distinguished name of the new credential certificate: The remote signature "
            "creation service shall support the parameter subjectData given in the credentialCreationRequest "
            "input parameter in order to construct the subject distinguished name of the certificate for the "
            "new credential.\n\n"
            "When Rich Authorization Requests (RAR) are supported, the remote signature creation service "
            "shall support receiving the subject data needed to construct the subject distinguished name of "
            "the certificate for the new credential from the authorization server in the authorization "
            "details of the access token expressed using OIDC claims notation. When Rich Authorization "
            "Requests (RAR) are supported, the remote signature creation service may support receiving the "
            "subject distinguished name data of the certificate for the new credential from the authorization "
            "server as custom claims in the access token [i.16] or retrieving them at a token introspection "
            "endpoint [i.8]. The remote signature creation service may ignore or overwrite all or some of the "
            "subject distinguished name data provided by the parameter subjectData given in the "
            "credentialCreationRequest input parameter.\n\n"
            "The following subject data expressed using standard OIDC claims shall be collected by the remote "
            "signature creation service: given_name, family_name, gender, birthdate, address:country. The "
            "following subject data expressed using standard OIDC claims should be collected by the remote "
            "signature creation service: sub (if provided it shall contain a subject unique identifier "
            "assigned by a government or civil authority). The following subject data expressed using "
            "standard OIDC claims may be collected by the remote signature creation service: "
            "address:locality, address:region, email."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.9.1 (Description)",
        "testo": (
            "Il metodo credentials/delete di CSC API, clausola 11.5, cancella una credenziale di firma. Il "
            "metodo richiede un'autorizzazione alla cancellazione di credenziali; DEVE essere applicato e "
            "puo' essere implementato per garantire la conformita' alla presente specifica."
        ),
        "testo_integrale": (
            "7.9.1 Description: The credentials/delete API identified in CSC API [1], clause 11.5 deletes a "
            "signing credential.\n\n"
            "This method requires credential deletion authorization. The credentials/delete API method "
            "referenced in CSC API [1], clause 11.5, shall be applied and may be implemented to ensure "
            "compliance with the present specification."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.9.2.1 (Component for requesting credential creation)",
        "testo": (
            "Il messaggio per richiedere la cancellazione di una credenziale DEVE contenere i componenti "
            "definiti nella clausola 11.5, section Input, di CSC API. Il titolo ufficiale della sottoclausola "
            "parla di creazione (\"Component for requesting credential creation\") pur disciplinando la "
            "cancellazione: refuso del documento, riprodotto letteralmente."
        ),
        "testo_integrale": (
            "7.9.2.1 Component for requesting credential creation: The message for requesting a credential "
            "deletion shall contain the components defined in CSC API [1], clause 11.5 section Input."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.9.3.1 (Component for responding to credential deletion requests)",
        "testo": (
            "L'API non ha valori di output e in risposta e' fornito il codice di stato HTTP 204 \"No "
            "Content\", definito nella clausola 15.3.5 di IETF RFC 9110, come specificato nella clausola "
            "11.5, section Output, di CSC API."
        ),
        "testo_integrale": (
            "7.9.3.1 Component for responding to credential deletion requests: This API has no output values "
            "and the HTTP status code 204 \"No Content\", defined in clause 15.3.5 of IETF RFC 9110 [16], is "
            "provided in response as specified in CSC API [1], clause 11.5 section Output."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 8.1 (Introduction and General Provisions)",
        "testo": (
            "Introduzione e disposizioni generali del profilo DSS-X: l'API e' il modo con cui qualsiasi "
            "applicazione client interagisce con un SCS conforme al documento; le clausole successive "
            "presentano gli elementi dell'API DSS-X nell'ordine degli elementi dell'API CSC API (clausola 7) "
            "e, richiamando taluni elementi obbligatori, definiscono implicitamente un profilo di DSS-X "
            "rispetto al contesto applicativo del documento. Due NOTE chiariscono che DSS-X e CSC seguono "
            "paradigmi di progettazione diversi (con numerosi schemi equivalenti possibili per la natura "
            "generica di DSS-X) e che DSS-X ha una sintassi astratta con mappatura XML e una mappatura "
            "alternativa JSON. Il documento raccomanda il binding HTTP Post (sezione 8.1 di OASIS DSS-X) ma "
            "ammette trasporti alternativi; binding di sicurezza DSS-X affidabili DEVONO applicarsi a tutti i "
            "messaggi di protocollo, con TLS che dovrebbe fornire il livello di sicurezza di base e livelli "
            "di sicurezza alternativi o complementari ammissibili (ad esempio la firma digitale dei messaggi "
            "DSS-X, con il formato di firma ammissibile determinato dalla variante sintattica DSS-X scelta). "
            "I metadati del servizio (clausole 8.2 e 8.3) DEVONO fornire dettagli sul meccanismo applicabile "
            "di trasmissione dei signature activation data, tra: il componente opzionale ClaimedIdentity "
            "(sezione 4.4.9 di OASIS DSS-X), che puo' identificare il firmatario per le chiamate di servizio "
            "delle clausole 8.3-8.7 con SupportingInfo che porta opzionalmente i dati di autorizzazione "
            "(approccio raccomandato con OAuth 2.0, ad esempio nel contesto dell'EUDIW); il binding di "
            "trasporto o un livello di sicurezza sottostante, o una loro combinazione (ad esempio un "
            "envelope SAML esterno che identifica e autorizza il firmatario di un livello DSS-X interno, "
            "oppure un livello di sicurezza esterno particolarmente adatto a un servizio automatico di "
            "creazione di sigilli quando il richiedente il servizio e' anche il firmatario); un "
            "sotto-protocollo che interlaccia uno scenario DSS SignRequest/SignResponse."
        ),
        "testo_integrale": (
            "8.1 Introduction and General Provisions: In the present document, the API represent the way by "
            "which any client application can interact with any SCS conforming to the present document. The "
            "following clauses define the API that a client application can invoke within an SCS. For "
            "simplifying API mapping comparison, the subsequent sections presents DSS-X API elements in the "
            "order of the above-cited CSC API elements (see clause 7 of the present document). The subsequent "
            "clauses also reference certain mandatory elements and thus implicitly define a profile of DSS-X "
            "with regard to the application context of the present document.\n\n"
            "NOTE 1: Given the fact that OASIS DSS-X and CSC follow different protocol design paradigms, API "
            "elements may not match regarding all details of the abstract signature creation process. "
            "Nevertheless, and specifically due to the generic nature of DSS-X, numerous equivalent patterns "
            "exist for implementing the same approach using either protocol.\n\n"
            "NOTE 2: DSS-X has an abstract syntax specification with a mapping to XML and an alternative "
            "mapping to JSON.\n\n"
            "DSS-X can have various transport bindings as specified in section 8 of [4]. The present document "
            "recommends the HTTP Post binding (see section 8.1 of [4]), but also admits alternative "
            "transports.\n\n"
            "DSS-X can have various security bindings to ensure authenticity, integrity and confidentiality "
            "of protocol messages as detailed in section 8.3 of [4]. Reliable DSS-X security bindings shall "
            "apply to all protocol messages in the context of the present document. In particular, TLS (see "
            "[7]) should supply the security base layer, while alternative and/or complementary security "
            "layers are admissible. For instance, a complementary security layer may consist in digitally "
            "signing DSS-X messages, with the chosen DSS-X syntax variant (see section 2.2.5 of [4]) "
            "determining an eligible signature format (see [8] and [9]).\n\n"
            "DSS-X supports various options for transmitting signature activation data. The service metadata "
            "(see clauses 8.2 and 8.3 of the present document) shall provide details regarding the applicable "
            "mechanism embodied by one of the following variants:\n\n"
            "- The ClaimedIdentity optional component (see section 4.4.9 of [4]) can identify the signatory "
            "regarding service calls described in clauses 8.3, 8.4, 8.5, 8.6 and 8.7 of the present "
            "document, with the SupportingInfo optionally carrying corresponding authorization data. This is "
            "the recommended approach when using the API in combination with the OAuth2.0 authorization "
            "framework (e.g. when using the API in the context of the European Digital Identity Wallet).\n"
            "- The transport binding or an underlying security layer, or a combination of both can identify "
            "the signatory and carry authorization data. For instance, when using the API in combination "
            "with SAMLv2, an outer SAML envelope can provide identification and authorization data regarding "
            "the signatory of an inner DSS-X layer. Alternatively, an outer security layer can implicitly "
            "identify the signatory and provide authorization data. This latter approach is particularly "
            "suitable for an automated electronic seal creation service, when the service requestor is also "
            "the signatory.\n"
            "- Finally, a sub-protocol that interleaves a DSS SignRequest and SignResponse scenario, may be "
            "used for identifying the signatory and providing authorization data."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 8.2.1 (Description)",
        "testo": (
            "L'API restituisce informazioni tecniche sul servizio. OASIS DSS-X offre varie opzioni per "
            "veicolare informazioni specifiche del servizio, dettagliate nella clausola 4 di [5], documento "
            "complementare di DSS-X. La specifica dei nomi degli elementi della clausola 3.2 di [5] DEVE "
            "applicarsi. Un'istanza di metadati DEVE essere completa quanto necessario a consentire agli "
            "integratori di ottenere informazioni accurate sul supporto delle funzionalita' disponibili nel "
            "servizio. Per consentire l'individuazione dei metadati DEVE applicarsi il meccanismo descritto "
            "nella clausola 4 di [5]."
        ),
        "testo_integrale": (
            "8.2.1 Description: Returns technical information about the service.\n\n"
            "OASIS DSS-X [4] provides various options for conveying service-specific information as detailed "
            "in clause 4 of [5] that represents a complementary standard document of DSS-X.\n\n"
            "The element name specification of clause 3.2 of [5] shall apply.\n\n"
            "A metadata instance shall be as complete as necessary to enable integrators for obtaining "
            "accurate information regarding available feature support of the service.\n\n"
            "For enabling metadata discovery, the mechanism described in clause 4 of [5] shall apply."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 8.3.1 (Description)",
        "testo": (
            "L'API restituisce l'elenco delle credenziali di un certo utente. OASIS DSS-X non fornisce "
            "un'API specifica per richiedere le credenziali dell'utente, il che protegge specificamente la "
            "privacy dell'utente non esponendo alcuna credenziale senza autenticazione esplicita o senza "
            "consenso dell'utente; l'elemento AuthInfo dei metadati (clausola 3.2 di [5]) puo' invece fornire "
            "informazioni generali sui meccanismi di autenticazione supportati dal servizio di firma "
            "sottostante. Se il certificato del firmatario e' richiesto in anticipo per preparare una "
            "richiesta di firma (ad esempio per calcolare l'hash del certificato del firmatario come parte "
            "dei DTBS o per specificare l'aspetto di una firma PDF basato sul subject distinguished name del "
            "certificato), il servizio di firma PUO' esporre mezzi per richiedere esplicitamente il "
            "certificato del firmatario, ad esempio una VerifyRequest contenente un componente OptionalInputs "
            "con un elemento ReturnSignerIdentity (clausola 4.4.5 di [4]); in alternativa il certificato puo' "
            "essere fornito dalla risposta del protocollo di autenticazione applicato, puo' essere gia' "
            "disponibile lato client per via extra-banda, oppure non essere affatto richiesto in anticipo "
            "(ad esempio quando il certificato del firmatario e' creato al volo per uso singolo, nella forma "
            "di un certificato a breve termine a validita' assicurata). I metadati DEVONO indicare, tramite "
            "la clausola 3.1.5 di [5], quale degli approcci sopra citati il servizio supporta."
        ),
        "testo_integrale": (
            "8.3.1 Description: Returns the list of credentials of a certain user.\n\n"
            "OASIS DSS-X [4] does not provide a specific API for requesting user credentials, which "
            "specifically protects privacy of the user by not exposing any credentials without explicit "
            "authentication or without user consent. By contrast, the metadata AuthInfo element (see clause "
            "3.2 of [5]) can supply general information about the authentication mechanisms supported by the "
            "underlying signature service.\n\n"
            "If the signer certificate is required upfront for preparing a signature request, e.g. for "
            "calculating a signer certificate hash as part of the DTBS or for specifying a PDF signature "
            "appearance based on the signer certificate subject Distinguished Name, the signature service may "
            "expose means for explicitly requesting the signer certificate. Such a request may consist of a "
            "VerifyRequest containing an OptionalInputs component with a ReturnSignerIdentity element (see "
            "clause 4.4.5 of [4]).\n\n"
            "Alternatively, the response of the applied authentication protocol may supply the signer "
            "certificate.\n\n"
            "Alternatively, the signer certificate may already be available on the client side by out-of-band "
            "means.\n\n"
            "Alternatively, no signer certificate may be required upfront on the client side, e.g. when "
            "creating a signer certificate on the fly for single use, e.g. in the form of a validity-assured "
            "short-term certificate.\n\n"
            "The metadata shall indicate via clause 3.1.5 of [5], which of the above-cited approaches the "
            "service supports."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 8.5.1 (Description)",
        "testo": (
            "L'API calcola la firma digitale di uno o piu' valori di hash. A tal fine DEVE applicarsi la "
            "SignRequest con la variante DocumentHash del componente InputDocuments (clausola 4.5.5 di [4]); "
            "il componente KeySelector (clausola 4.4.12 di [4]) DEVE applicarsi ogniqualvolta la chiave di "
            "firma non possa essere determinata implicitamente."
        ),
        "testo_integrale": (
            "8.5.1 Description: Computes the digital signature of one or multiple hash values.\n\n"
            "For this purpose, the SignRequest with the DocumentHash variant of the InputDocuments component "
            "(see clause 4.5.5 of [4]) shall apply. The KeySelector component (see clause 4.4.12 of [4]) "
            "shall apply whenever the signing key cannot be determined implicitly."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 8.6.1 (Description)",
        "testo": (
            "L'API crea una o piu' firme AdES. A tal fine DEVE applicarsi la SignRequest con la variante "
            "Document del componente InputDocuments (clausola 4.5.3 di [4]); per veicolare DTBS piu' "
            "complessi, in particolare nel caso di XAdES, la variante TransformedData (clausola 4.5.4 di "
            "[4]) puo' essere piu' appropriata ed e' quindi un'alternativa ammissibile; il componente "
            "KeySelector (clausola 4.4.12 di [4]) DEVE applicarsi ogniqualvolta la chiave di firma non possa "
            "essere determinata implicitamente."
        ),
        "testo_integrale": (
            "8.6.1 Description: Creates one or more AdES signatures.\n\n"
            "For this purpose, the SignRequest with the Document variant of the InputDocuments component (see "
            "clause 4.5.3 of [4]) shall apply. For conveying more complex DTBS, particularly in the case of "
            "XAdES, the TransformedData variant (see clause 4.5.4 of [4]) may be more appropriate and is "
            "therefore an admissible alternative. The KeySelector component (see clause 4.4.12 of [4]) shall "
            "apply whenever the signing key cannot be determined implicitly."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 8.7.1 (Description)",
        "testo": (
            "L'API restituisce l'esito corrispondente a una precedente richiesta di creazione di firme "
            "elaborata in modalita' asincrona, oppure l'indicazione che il processo di firma non e' ancora "
            "stato completato. A tal fine DEVE applicarsi l'elemento PendingRequest (clausole 4.3.5 e 7 di "
            "[4])."
        ),
        "testo_integrale": (
            "8.7.1 Description: Returns the outcome corresponding to a previous signature(s) creation "
            "request when processed in asynchronous mode or the indication that the signing process has not "
            "yet completed.\n\n"
            "For this purpose, the PendingRequest element (see clauses 4.3.5 and 7 of [4]) shall apply."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 7.1 (Introduction)",
        "testo": (
            "La clausola inquadra l'API: e' il modo con cui qualsiasi driving application puo' interagire con "
            "qualsiasi SCS conforme al presente documento, e le clausole seguenti definiscono l'API che una "
            "driving application puo' invocare all'interno di un SCS. Per ogni API la coppia messaggio di "
            "richiesta/risposta e' specificata rinviando a CSC API, quando possibile, altrimenti dettagliando "
            "nuovi componenti definiti nel presente documento, per mezzo di una tabella che indica il nome "
            "del componente, la sua presenza, il suo tipo di dato e una breve descrizione. La Tabella 1 "
            "definisce il significato dei valori della colonna \"Presence\": M = il componente DEVE essere "
            "incluso nella richiesta o nella risposta all'SCS; O = il componente PUO' essere incluso; C = il "
            "componente DEVE essere incluso nella richiesta o nella risposta in base al verificarsi di "
            "determinate condizioni."
        ),
        "testo_integrale": (
            "7.1 Introduction: In the present document the API represent the way by which any driving "
            "application can interact with any SCS conforming to the present document. The following clauses "
            "define the API that a driving application can invoke within an SCS. For any API the request and "
            "response messages pair is specified referring to CSC API [1], when possible, otherwise detailing "
            "new components defined in the present document, by means of a table where the following "
            "information are provided:\n\n"
            "- the components name;\n"
            "- the presence of the component;\n"
            "- the data type of the component;\n"
            "- a brief description of the component.\n\n"
            "The value included in the column \"Presence\" of the tables has the meaning defined in table 1."
            "\n\n"
            "**Table 1**\n\n"
            "|Value|Description|\n"
            "|---|---|\n"
            "|M|The component shall be included in the request to or response from the SCS.|\n"
            "|O|The component may be included in the request to or response from the SCS.|\n"
            "|C|The component shall be included in the request or response based on the occurrence of certain "
            "conditions.|"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": [
            "servizio di gestione di dispositivo di creazione di firma elettronica a distanza",
            "firma elettronica avanzata",
        ],
    },
    {
        "riferimento": "clausola 8.4.1 (Description)",
        "testo": (
            "La clausola descrive la funzione dell'API: recupera una credenziale e restituisce informazioni "
            "sul certificato di firma e sui meccanismi di autorizzazione necessari ad autorizzare l'uso della "
            "credenziale per la firma remota. Per il resto rinvia alla clausola 8.3 del presente documento. "
            "Nessun verbo prescrittivo: e' descrizione, non prescrizione."
        ),
        "testo_integrale": (
            "8.4.1 Description: Retrieves a credential and returns information about signing certificate and "
            "authorization mechanisms required to authorize the usage of the credential for remote signing."
            "\n\n"
            "See clause 8.3 of the present document."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "servizio di gestione di dispositivo di creazione di firma elettronica a distanza",
            "firma elettronica avanzata",
        ],
    },
    {
        "riferimento": "clausola 8.8.1 (Description)",
        "testo": (
            "La clausola constata che l'API credentials/create crea una nuova credenziale di firma, che "
            "OASIS DSS-X non fornisce un'API specifica per la creazione del certificato del firmatario (la "
            "creazione avviene implicitamente quando la corrispondente implementazione della SignRequest crea "
            "il certificato del firmatario al volo per uso singolo, ad esempio nella forma di un certificato "
            "a breve termine a validita' assicurata previo consenso dell'utente, mentre la creazione di "
            "certificati di firmatario validi a lungo termine e' oggetto di un processo PKI dedicato, fuori "
            "dal perimetro del processo di creazione di firma) e che, di conseguenza, nel caso del presente "
            "profilo DSS-X un'API di creazione di credenziali non e' applicabile. Nessun verbo prescrittivo: "
            "e' una dichiarazione di non applicabilita', non una prescrizione."
        ),
        "testo_integrale": (
            "8.8.1 Description: The API credentials/create creates a new signing credential.\n\n"
            "OASIS DSS-X does not provide a specific API for signer certificate creation. This happens "
            "implicitly when the corresponding SignRequest implementation creates the signer certificate on "
            "the fly for single use, e.g. in the form of a validity-assured short-term certificate upon user "
            "consent, while creation of long-term valid signer certificates is subject to a dedicated PKI "
            "process outside the scope of a signature creation process.\n\n"
            "Consequently, a credential creation API is not applicable in the case of the present DSS-X "
            "profile."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "servizio di gestione di dispositivo di creazione di firma elettronica a distanza",
            "firma elettronica avanzata",
        ],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 7.1 (Introduction)",
    "clausola 7.2.1 (Description)",
    "clausola 7.2.2.1 (Component for requesting service information)",
    "clausola 7.2.3.1 (Component for responding to service information requests)",
    "clausola 7.3.1 (Description)",
    "clausola 7.3.2.1 (Component for requesting credentials list)",
    "clausola 7.3.3.1 (Component for responding to credentials list requests)",
    "clausola 7.4.1 (Description)",
    "clausola 7.4.2.1 (Component for requesting credential information)",
    "clausola 7.4.3.1 (Component for responding to credential information requests)",
    "clausola 7.5.1 (Description)",
    "clausola 7.5.2.1 (Component for requesting hash(es) signature creation)",
    "clausola 7.5.3.1 (Component for responding to hash(es) signature creation requests)",
    "clausola 7.6.1 (Description)",
    "clausola 7.6.2.1 (Component for requesting documents signature creation)",
    "clausola 7.6.3.1 (Component for responding to documents signature creation requests)",
    "clausola 7.7.1 (Description)",
    "clausola 7.7.2.1 (Component for polling previous signature creation requests)",
    "clausola 7.7.3.1 (Component for responding to polling previous signature creation requests)",
    "clausola 7.8.1 (Description)",
    "clausola 7.8.2.1 (Component for requesting credential creation)",
    "clausola 7.8.3.1 (Component for responding to credential creation requests)",
    "clausola 7.8.4 (Subject distinguished name of the new credential certificate)",
    "clausola 7.9.1 (Description)",
    "clausola 7.9.2.1 (Component for requesting credential creation)",
    "clausola 7.9.3.1 (Component for responding to credential deletion requests)",
    "clausola 8.1 (Introduction and General Provisions)",
    "clausola 8.2.1 (Description)",
    "clausola 8.3.1 (Description)",
    "clausola 8.4.1 (Description)",
    "clausola 8.5.1 (Description)",
    "clausola 8.6.1 (Description)",
    "clausola 8.7.1 (Description)",
    "clausola 8.8.1 (Description)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Solo citazioni letterali interne alla stessa Fonte (fonte_id_o_None = None),
# tutte di tipo "richiama". Nessuna relazione cross-fonte (Fase 6, ADR-0009).
# `confidence` None su tutte: non esiste uno score reale da registrare.
RELAZIONI: list[dict] = [
    # 8.1: "in the order of the above-cited CSC API elements (see clause 7 of the
    # present document)" — rinvio all'intera clausola 7, che il grafo non censisce
    # come nodo (intestazione di puro raggruppamento): la relazione punta al nodo di
    # ingresso della clausola 7 (7.1 Introduction, che ne enuncia l'impianto) con
    # evidence_type "inferred" (citazione letterale, risoluzione al singolo nodo
    # inferita dall'estrazione).
    {
        "nodo_da": ("obbligo", None, "clausola 8.1 (Introduction and General Provisions)"),
        "nodo_a": ("principio", None, "clausola 7.1 (Introduction)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    # 8.1: "The service metadata (see clauses 8.2 and 8.3 of the present document)
    # shall provide details ..." — ciascuna delle clausole 8.2 e 8.3 ha un solo nodo
    # di contenuto proprio (8.2.1, 8.3.1), quindi la risoluzione e' univoca.
    {
        "nodo_da": ("obbligo", None, "clausola 8.1 (Introduction and General Provisions)"),
        "nodo_a": ("obbligo", None, "clausola 8.2.1 (Description)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 8.1 (Introduction and General Provisions)"),
        "nodo_a": ("obbligo", None, "clausola 8.3.1 (Description)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # 8.1: "service calls described in clauses 8.3, 8.4, 8.5, 8.6 and 8.7 of the
    # present document" — 8.3 gia' coperta dall'arco precedente (nessun arco
    # duplicato per la stessa coppia nodo/tipo); 8.4-8.7 hanno un solo nodo di
    # contenuto ciascuna (x.1).
    {
        "nodo_da": ("obbligo", None, "clausola 8.1 (Introduction and General Provisions)"),
        "nodo_a": ("principio", None, "clausola 8.4.1 (Description)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 8.1 (Introduction and General Provisions)"),
        "nodo_a": ("obbligo", None, "clausola 8.5.1 (Description)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 8.1 (Introduction and General Provisions)"),
        "nodo_a": ("obbligo", None, "clausola 8.6.1 (Description)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 8.1 (Introduction and General Provisions)"),
        "nodo_a": ("obbligo", None, "clausola 8.7.1 (Description)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # 8.4.1: "See clause 8.3 of the present document." — unico nodo della clausola
    # 8.3 e' 8.3.1 (Description).
    {
        "nodo_da": ("principio", None, "clausola 8.4.1 (Description)"),
        "nodo_a": ("obbligo", None, "clausola 8.3.1 (Description)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_completezza_testo_integrale, verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    verifica_completezza_testo_integrale([sys.modules[__name__]])
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
