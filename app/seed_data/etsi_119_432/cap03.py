"""ETSI TS 119 432 V1.3.1 (2026-03) - Electronic Signatures and Trust
Infrastructures (ESI); Protocols for remote digital signature creation.
Fonte 20 (la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 3:
clausola 5.3 (Signatures creation authorization: 5.3.1 Overview, 5.3.2
Creating a remote signature with a credential protected by signature creation
service-managed authorization, 5.3.3 Create a remote signature with a
credential protected by OAuth2), clausola 5.4 (Credential creation
authorization), clausola 5.5 (Credential deletion authorization). Documento
unico (non multi-parte): i `riferimento` NON portano prefisso di Parte. Testo
ufficiale in app/.source_cache/etsi_119_432/cap03.txt (letto sempre con
selettore `:raw`, altrimenti il tool tronca le righe lunghe a 768 caratteri
introducendo "..." e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_119_432/manifest.json.

Modellazione (ADR-0007), stesso criterio gia' applicato alle altre fonti ETSI
gia' censite e alle clausole di uno standard tecnico: un nodo per ogni
clausola/sottoclavola numerata che porta contenuto proprio; le intestazioni di
puro raggruppamento non generano ne' nodo ne' item di indice. Questo capitolo
produce 4 Obblighi e 1 Principio su 5 item di indice. Scelte voce per voce:

- Clausola 5.3 (Signatures creation authorization) -> NESSUN nodo, NESSUN
  item di indice: e' un'intestazione di puro raggruppamento che introduce le
  tre sottoclausole 5.3.1-5.3.3 senza una riga di testo proprio (il testo
  ufficiale passa direttamente dal titolo a "5.3.1 Overview"). Stesso
  trattamento riservato alle intestazioni di raggruppamento delle altre fonti
  ETSI censite.
- Clausola 5.3.1 (Overview) -> 1 Principio "altro", riferimento "clausola
  5.3.1 (Overview)". Clausola descrittiva, priva di soggetto obbligato e di
  verbo prescrittivo: enuncia che la richiesta di creazione di firme a un
  servizio di creazione di firme richiede un'autorizzazione dell'utente che
  possiede e controlla la chiave di firma (esistente o generata al volo);
  presenta i due livelli di confidenza del controllo della chiave definiti in
  ETSI EN 419 241-1 [6] (SCAL1, autenticazione di base e nessun binding
  crittografico fra Signature Activation Data e dati da firmare; SCAL2,
  autenticazione piu' forte e binding crittografico fra SAD e dati da
  firmare); osserva che la credenziale di firma usata dall'applicazione
  driver puo' essere protetta direttamente dallo SCSP o tramite un framework
  come OAuth2; annuncia infine che le clausole seguenti descrivono i
  diagrammi di sequenza delle operazioni piu' comuni di richiesta e
  autorizzazione di una firma remota, con particolare riferimento all'uso
  dell'EUDIW (LoA High) come fattore di autenticazione del firmatario. E'
  descrizione di architettura/flusso, non definizione di un termine del
  documento (le definizioni stanno nella clausola 3, gia' censita in cap01)
  ne' perimetro del documento (clausola 1): "altro" e' il tipo corretto.
  Nemmeno "scopo/ambito di applicazione" sarebbe appropriato: la clausola non
  delimita cio' che il documento copre, anticipa il contenuto delle clausole
  successive.
  `oggetti_giuridici`: "servizio di gestione di dispositivo di creazione di
  firma elettronica a distanza" (id 28 in seed.py). L'oggetto della clausola
  e' l'autorizzazione all'uso di una credenziale di firma custodita da un
  servizio remoto, cioe' il servizio fiduciario di gestione a distanza
  introdotto dall'art. 29-bis eIDAS2; nessun altro valore del vocabolario
  chiuso e' pertinente (non si tratta della firma o del sigillo qualificato
  in se', ne' di un QSCD, ne' del portafoglio: l'EUDIW e' citato solo come
  possibile fattore di autenticazione).
- Clausola 5.3.2 (Creating a remote signature with a credential protected by
  signature creation service-managed authorization) -> 1 Obbligo
  "tecnico/sicurezza", soggetto QTSP/gestore obbligato. La sottoclausola e'
  un'unica unita' indivisibile senza numerazione interna: accorpa la NOTE
  iniziale (l'autorizzazione esplicita richiede all'applicazione driver di
  raccogliere i fattori di autenticazione nel proprio ambiente, con
  complessita' di raccolta e conservazione sicura, e il meccanismo non
  dovrebbe essere idoneo a soddisfare i requisiti SCAL2), la didascalia della
  Figure 4 e tutte le prescrizioni "shall" sui quattro metodi CSC API:
  credentials/authorize (clausola 11.8), credentials/authorizeCheck (clausola
  11.9), credentials/extendTransaction (clausola 11.11) e
  credentials/getChallenge (clausola 11.10), ciascuna nella forma "The <API>
  API identified in CSC API [1], clause X shall apply" piu' "The message ...
  shall contain the components defined in CSC API [1], clause X section
  Input/Output". Soggetto delle prescrizioni e' il prestatore del servizio di
  creazione di firme, cioe' l'implementazione CSC API del servizio ->
  QTSP/gestore obbligato. tipo_obbligo "tecnico/sicurezza": le prescrizioni
  vincolano l'interfaccia e i messaggi del protocollo (conformita' ai metodi
  e ai componenti di Input/Output di CSC API), non un adempimento
  organizzativo ne' un obbligo informativo verso terzi. La NOTE resta
  integralmente nel `testo_integrale` (ADR-0010) e il suo "should" non e'
  promosso a nodo separato: la NOTE non ha numerazione propria e non
  costituisce una clausola autonoma.
- Clausola 5.3.3 (Create a remote signature with a credential protected by
  OAuth2) -> 1 Obbligo "tecnico/sicurezza", soggetto QTSP/gestore obbligato.
  Accorpa l'introduzione descrittiva su OAuth 2.0 (accesso delegato e
  limitato alle risorse di un resource owner senza condividerne i dati di
  autenticazione; l'applicazione driver e' l'applicazione client), la
  didascalia della Figure 5 e le prescrizioni sui quattro metodi oauth2/*:
  oauth2/authorize (CSC API clausola 8.2.2), oauth2/pushed_authorize
  (clausola 8.2.3), oauth2/token (clausola 8.2.4) e oauth2/revoke (clausola
  8.2.5), con il contenuto prescritto dei messaggi di richiesta (Input) e di
  ritorno (Output). Due peculiarita' riportate verbatim: la richiesta di
  request URI deve contenere i componenti della clausola 8.2.2 section Input
  "apart from the request_uri parameter" e il messaggio di ritorno del
  request URI segue IETF RFC 9126 [18] clause 2.2 (non CSC API); oauth2/revoke
  non ha valori di output e risponde con HTTP 204 "No Content" (IETF RFC
  9110 [16] clausola 15.3.5).
- Clausola 5.4 (Credential creation authorization) -> 1 Obbligo
  "tecnico/sicurezza", soggetto QTSP/gestore obbligato. Accorpa
  l'introduzione (la richiesta di creazione di una credenziale al servizio di
  creazione di firme richiede l'autorizzazione dell'utente a cui la
  credenziale sara' vincolata; CSC API supporta a questo fine solo
  l'autorizzazione OAuth 2.0), la didascalia della Figure 6, le prescrizioni
  sui metodi oauth2/authorize (clausola 8.2.2, con la section Credential
  creation scope and authorization details), oauth2/pushed_authorize
  (clausola 8.2.3), oauth2/token (clausola 8.2.4) e credentials/create
  (clausola 11.4), e la lista non esaustiva delle modalita' con cui il
  servizio di creazione di firme puo' raccogliere i subject data necessari
  alla certificate signing request (Rich Authorization Requests;
  authorization details del token di accesso; custom claims nel token;
  token introspection endpoint). La lista e' esemplificativa, ma non ha
  numerazione propria ed e' interna a una clausola prescrittiva indivisibile:
  resta accorpata nell'unico nodo, come da criterio "non spezzare una
  clausola priva di numerazione propria". Nota verbatim: il messaggio di
  ritorno dell'authorization code per la creazione di credenziale dice "for
  signatures creation authorization" nel testo ufficiale (refuso del
  documento, riprodotto letteralmente per ADR-0010, non corretto).
- Clausola 5.5 (Credential deletion authorization) -> 1 Obbligo
  "tecnico/sicurezza", soggetti QTSP/gestore obbligato e Utente/titolare
  destinatario. Accorpa i motivi di cancellazione (fine del ciclo di vita,
  ragioni di sicurezza, conformita' regolamentare per obsolescenza degli
  algoritmi crittografici), la regola di autorizzazione (autorizzazione
  dell'utente che possiede e controlla la credenziale, oppure di
  un'applicazione driver fidata o di una terza parte fidata), la
  raccomandazione "the SCSP should inform the credential owner when a
  credential is deleted" quando l'autorizzazione non e' richiesta al
  titolare, l'affermazione che CSC API supporta solo OAuth 2.0 per questa
  autorizzazione, e le prescrizioni sui metodi oauth2/authorize (clausola
  8.2.2, section Credential deletion scope and authorization details, e
  clausola 8.2.3, con Authorization Code flow o Client Credential flow per le
  applicazioni driver fidate), oauth2/token e credentials/delete (clausola
  11.5). La seconda categoria di soggetto e' "destinatario" perche' il
  "should inform" ha per destinatario il titolare della credenziale
  (precedente identico: OVR-6.6-01 di ETSI EN 319 421, che aggiunge il terzo
  affidante come destinatario). tipo_obbligo "tecnico/sicurezza" e non
  "informativo/trasparenza": l'obbligo informativo verso il titolare e' una
  singola sotto-prescrizione, mentre il contenuto dominante della clausola e'
  la conformita' ai metodi OAuth2/CSC del processo di cancellazione.

Completezza verbatim (ADR-0010): questo capitolo non contiene alcun
marcatore di elisione. Le clausole 5.3-5.5 del testo ufficiale non hanno
blocchi EXAMPLE con payload JSON/HTTP abbreviati (solo didascalie di figure e
liste di metodi API), quindi la terza convenzione di esenzione della guardia
`verifica_completezza_testo_integrale` (ellissi nei payload di esempio di
ETSI TS 119 432) non trova qui alcuna occorrenza. I `testo_integrale` sono
copie letterali integrali, con la sola normalizzazione degli spazi di
impaginazione (righe del PDF unite, "•" reso "-"), senza omettere NOTE,
didascalie di figura o elenchi puntati.

`condizione_applicabilita`: non valorizzata su nessuna riga. L'unica
condizione presente nel perimetro (5.5, "In cases where credential deletion
authorization is not requested to the credential owner") condiziona una
singola sotto-prescrizione interna alla clausola, non l'intera riga:
valorizzarla sull'intero nodo lo presenterebbe come requisito condizionale
nella sua interezza, cosa che il testo non dice.

`stato`: "vigente" su tutte le righe (nessuna evidenza di abrogazione o di
transizione eIDAS->eIDAS2 in questo capitolo).

RELAZIONI interne: nessuna, come da istruzione di capitolo. Tutti i rinvii
testuali di questo capitolo sono a clausole di specifiche esterne - CSC API
[1] (clausole 8.2.2-8.2.5, 11.4, 11.5, 11.8-11.11, 11.13, 11.14), IETF RFC
9110 [16] (clausole 15.3.3 e 15.3.5), IETF RFC 6749 [17] (Section 4.1),
IETF RFC 9126 [18] (clause 2.2), ETSI EN 419 241-1 [6] - e nessuno di essi
cita letteralmente il `riferimento` di un altro nodo di questa Fonte, unica
condizione ammessa per una relazione interna. Il collegamento cross-fonte
verso le altre 19 Fonti e' demandato alla Fase 6 della sessione principale
(ADR-0009).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": (
            "clausola 5.3.2 (Creating a remote signature with a credential protected by signature creation "
            "service-managed authorization)"
        ),
        "testo": (
            "La sottoclausola descrive il flusso generale in cui un'applicazione driver richiede la creazione di "
            "firme a un servizio di creazione di firme con una credenziale protetta da autorizzazione gestita "
            "dallo SCSP (Figura 4). Una NOTE iniziale avverte che l'autorizzazione esplicita richiede "
            "all'applicazione driver di raccogliere i fattori di autenticazione (es. PIN, OTP) nel proprio "
            "ambiente, con complessita' di raccolta e conservazione sicura dei fattori, e che tale meccanismo "
            "non dovrebbe essere idoneo a soddisfare i requisiti SCAL2. Lo schema si realizza in CSC API "
            "invocando credentials/authorize, passando, oltre ai valori che identificano la credenziale di firma "
            "e i DTBSR, gli authentication objects necessari a completare l'autorizzazione alla creazione di "
            "firme (la clausola 11.8 di CSC API definisce un modo generico di gestire il controllo di accesso "
            "alle credenziali, associando a ciascuna credenziale un insieme di tipi di authentication object e "
            "una access rule che descrive la precondizione per autorizzarne accesso e uso); "
            "credentials/authorizeCheck e credentials/extendTransaction possono essere invocati per recuperare i "
            "dati di autorizzazione e per estendere la validita' dei dati di autorizzazione di una transazione "
            "multi-firma; quando il processo di autorizzazione si basa su un protocollo challenge-response, "
            "credentials/getChallenge puo' essere invocato per richiedere una challenge al servizio di creazione "
            "di firme. La firma si ottiene poi con signatures/signHash o signatures/signDoc (clausole 11.13 e "
            "11.14 di CSC API). Sono prescritti: l'applicabilita' dei metodi credentials/authorize (clausola "
            "11.8), credentials/authorizeCheck (clausola 11.9), credentials/extendTransaction (clausola 11.11) e "
            "credentials/getChallenge (clausola 11.10) di CSC API; l'inclusione degli authentication objects e "
            "dei corrispondenti valori raccolti dall'utente nei componenti definiti nella section Input delle "
            "medesime clausole; e il contenuto dei messaggi di ritorno (section Output), incluso il polling "
            "dello stato di una precedente richiesta credentials/authorize conclusa con codice di stato HTTP 202 "
            "\"Accepted\" (IETF RFC 9110, clausola 15.3.3), che indica un processo di autorizzazione ancora in "
            "corso."
        ),
        "testo_integrale": (
            "5.3.2 Creating a remote signature with a credential protected by signature creation service-managed "
            "authorization: NOTE: Explicit authorization requires the driving application to collect "
            "authentication factors (e.g. PIN, OTP) within its own environment. This introduces complexity in "
            "ensuring secure factor collection and storage. This mechanism should not be suitable to satisfy "
            "SCAL2 requirements. Below is a sequence diagram illustrating a general flow involving a driving "
            "application requesting signatures creation to a signature creation service with a credential "
            "protected by SCSP-managed authorization. Figure 4: A general flow involving a driving application "
            "requesting signatures creation to a signature creation service with a credential protected by "
            "SCSP-managed authorization The above scheme is implemented in CSC API by invoking the API - "
            "credentials/authorize, passing, in addition to the values identifying the signing credential and "
            "the DTBSR, the authentication objects needed to complete signatures creation authorization; CSC API "
            "specification [1] in section Authentication objects of clause 11.8 defines a generic way to manage "
            "access control to signing credentials associating each signing credential with a set of "
            "authentication object types and an access rule describing the precondition to authorize the signing "
            "credential access and usage; credentials/authorizeCheck and credentials/extendTransaction may be "
            "invoked for retrieving authorization data and for extending the validity of a multi signature "
            "transaction authorization data; when the authorization process is based on a challenge response "
            "protocol, credentials/getChallenge may be invoked to request a challenge from the signature "
            "creation service - signatures/signHash or signatures/signDoc to obtain the requested signature "
            "objects or signed documents as specified in clause 11.13 and 11.14 of CSC API. By invoking the "
            "credentials/authorize API the driving application can obtain the authorization data for making use "
            "of a signing credential to create signatures, according to the authorization mechanisms associated "
            "to the credential itself. The credentials/authorize API identified in CSC API [1], clause 11.8 "
            "shall apply. The authentication objects and corresponding values collected from the user shall be "
            "included in the components defined in CSC API [1], clause 11.8 section Input for creating the "
            "request message. The message for returning the authorization data for signing credential usage "
            "shall contain the components defined in CSC API [1], clause 11.8 section Output. By invoking the "
            "credentials/authorizeCheck API the driving application can poll the authorization state of a "
            "previous credentials/authorize request terminated with HTTP status code 202 \"Accepted\", defined in "
            "clause 15.3.3 of IETF RFC 9110 [16], representing that some authorization process was still "
            "underway. The credentials/authorizeCheck API identified in CSC API [1], clause 11.9 shall apply. "
            "The message for polling the authorization state of a previous credentials/authorize request "
            "terminated with HTTP status code 202 \"Accepted\", defined in clause 15.3.3 of IETF RFC 9110 [16], "
            "shall contain the components defined in CSC API [1], clause 11.9 section Input. The message for "
            "returning the authorization data for signing credential usage shall contain the components defined "
            "in CSC API [1], clause 11.9 section Output. By invoking the credentials/extendTransaction API the "
            "driving application can extend the validity of a multi-signature transaction authorization by "
            "obtaining new authorization data so that, i.e. the API method signatures/signHash can be invoked "
            "multiple times with a single credential authorization event. The credentials/extendTransaction API "
            "identified in CSC API [1], clause 11.11 shall apply. The message for extending the validity of a "
            "multi-signature transaction authorization shall contain the components defined in CSC API [1], "
            "clause 11.11 section Input. The message for returning the new authorization data for signing "
            "credential usage shall contain the components defined in CSC API [1], clause 11.11 section Output. "
            "By invoking the credentials/getChallenge API the driving application can request a challenge needed "
            "to perform a challenge response protocol for the access to a credential for remote signing. The "
            "credentials/getChallenge API identified in CSC API [1], clause 11.10 shall apply. The message for "
            "requesting a challenge for an authentication object shall contain the components defined in CSC API "
            "[1], clause 11.10 section Input. The message for returning the requested challenge or for "
            "indicating that a challenge has been sent by out-of-band means shall contain the components defined "
            "in CSC API [1], clause 11.10 section Output."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": (
            "clausola 5.3.3 (Create a remote signature with a credential protected by OAuth2)"
        ),
        "testo": (
            "La sottoclausola descrive il flusso generale in cui un'applicazione driver richiede la creazione di "
            "firme a un servizio di creazione di firme con una credenziale protetta da OAuth2 (Figura 5). OAuth "
            "2.0 e' un framework diffuso che consente alle applicazioni di ottenere accesso limitato alle "
            "risorse di un utente su un servizio senza bisogno dei suoi dati di autenticazione (es. la password) "
            "e fornisce alle applicazioni client un accesso delegato sicuro alle risorse del server per conto di "
            "un resource owner; nel contesto della creazione di firme remote l'applicazione driver e' "
            "l'applicazione client, il che consente ai titolari delle credenziali di firma di autorizzarne l'uso "
            "da parte di terzi senza condividere i propri dati di autenticazione e/o autorizzazione. Lo schema "
            "si realizza in CSC API con oauth2/authorize (e oauth2/pushed_authorize se necessario), "
            "oauth2/token, oauth2/revoke e signatures/signHash o signatures/signDoc. Sono prescritti: "
            "l'applicabilita' dei metodi oauth2/authorize (clausola 8.2.2), oauth2/pushed_authorize (clausola "
            "8.2.3), oauth2/token (clausola 8.2.4) e oauth2/revoke (clausola 8.2.5) di CSC API; il contenuto dei "
            "messaggi di richiesta, cioe' la richiesta dell'authorization code con i componenti della section "
            "Input della clausola 8.2.2 e le section Service scope e Credential scope and authorization details, "
            "la richiesta del request URI con i componenti della clausola 8.2.2 section Input tranne il "
            "parametro request_uri, la richiesta dell'access token (clausola 8.2.4 section Input) e "
            "l'invalidazione di un access o refresh token (clausola 8.2.5 section Input); e il contenuto dei "
            "messaggi di ritorno, cioe' l'authorization code (clausola 8.2.2 section Output), il request URI "
            "secondo IETF RFC 9126 clause 2.2, l'access token (clausola 8.2.4 section Output) e, per "
            "oauth2/revoke, l'assenza di valori di output con codice di stato HTTP 204 \"No Content\" (IETF RFC "
            "9110, clausola 15.3.5). Le richieste di autorizzazione sono gestite con l'Authorization Code flow "
            "(IETF RFC 6749, Section 4.1)."
        ),
        "testo_integrale": (
            "5.3.3 Create a remote signature with a credential protected by OAuth2: OAuth 2.0 authorization is a "
            "widely used framework that allows applications to obtain limited access to a user's resources on a "
            "service, without needing the user's authentication data (i.e. the user's password). OAuth 2.0 can "
            "provide client applications a secure delegated access to server resources on behalf of a resource "
            "owner. In the context of remote signatures creation, the driving application is the client "
            "application. This allows signing credentials owners to authorize third-party usage of their signing "
            "credentials without sharing their authentication and/or authorization data. Figure 5: A general "
            "flow involving a driving application requesting signatures creation to a signature creation service "
            "with a credential protected by OAuth2 authorization server The above scheme is implemented in CSC "
            "API [1] by invoking the API: - oauth2/authorize (and oauth2/pushed_authorize if needed), passing "
            "the needed information about the data to be signed and the signing credential to be used according "
            "to the parameters defined in clause 8.2.2 and 8.2.3 of CSC API [1], that manages authorization "
            "requests using the Authorization Code flow as described in Section 4.1 of IETF RFC 6749 [17]. - "
            "oauth2/token to obtain an OAuth 2.0 bearer access token from the authorization server by passing "
            "the authorization code or refresh token returned by the authorization server after a successful "
            "signatures creation authorization. - oauth2/revoke passing the access or refresh token, that was "
            "obtained from the authorization server, to be revoked. - signatures/signHash or signatures/signDoc "
            "to obtain the requested signature objects or signed documents as specified in clause 11.13 and "
            "11.14 of CSC API [1]. By invoking the oauth2/authorize API, via the user agent, the driving "
            "application can obtain an authorization code for signatures creation authorization from the "
            "authorization server of the signature creation service. The oauth2/authorize API identified in CSC "
            "API [1], clause 8.2.2 shall apply. The message for requesting the authorization code for signatures "
            "creation authorization shall contain the components defined in CSC API [1], clause 8.2.2 section "
            "Input considering what specified in sections Service scope and Credential scope and authorization "
            "details. The message for returning the authorization code for signatures creation authorization "
            "shall contain the components defined in CSC API [1], clause 8.2.2 section Output. By invoking the "
            "oauth2/pushed_authorize API the driving application can push the payload of an OAuth 2.0 "
            "authorization request to the authorization server via a direct request and obtain a request URI to "
            "be used as reference to the data in a subsequent call to the authorization endpoint "
            "(oauth2/authorize) of the remote service. The oauth2/pushed_authorize API identified in CSC API "
            "[1], clause 8.2.3 shall apply. The message for requesting the request URI that will be used as "
            "reference to the data in a subsequent call to the authorization endpoint shall contain the "
            "components defined in CSC API [1], clause 8.2.2 section Input apart from the request_uri parameter. "
            "The message for returning the request URI shall contain the components defined in IETF RFC 9126 "
            "[18], clause 2.2. By invoking the oauth2/token API the driving application can obtain an access "
            "token for signatures creation authorization from the authorization server of the remote service. "
            "The oauth2/token API identified in CSC API [1], clause 8.2.4 shall apply. The message for "
            "requesting the access token for signatures creation authorization shall contain the components "
            "defined in CSC API [1], clause 8.2.4 section Input. The message for returning the access token for "
            "signatures creation authorization shall contain the components defined in CSC API [1], clause 8.2.4 "
            "section Output. By invoking the oauth2/revoke API the driving application can invalidate access or "
            "refresh token obtained from the authorization server of the signature creation service so that any "
            "further access by reusing the token itself is prevented. The oauth2/revoke API identified in CSC "
            "API [1], clause 8.2.5 shall apply. The message for invalidating an access or refresh token for "
            "signatures creation authorization shall contain the components defined in CSC API [1], clause 8.2.5 "
            "section Input. The oauth2/revoke API has no output values, the HTTP status code 204 \"No Content\", "
            "defined in clause 15.3.5 of IETF RFC 9110 [16], is provided in response."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": (
            "clausola 5.4 (Credential creation authorization)"
        ),
        "testo": (
            "La sottoclausola disciplina l'autorizzazione alla creazione di credenziali: la richiesta di "
            "creazione di una credenziale al servizio di creazione di firme richiede l'autorizzazione "
            "dell'utente a cui la credenziale da creare sara' vincolata, e CSC API supporta a questo fine solo "
            "l'autorizzazione OAuth 2.0 (Figura 6). Lo schema si realizza in CSC API con oauth2/authorize (e "
            "oauth2/pushed_authorize se necessario), passando eventualmente i subject data necessari alla "
            "certificate signing request secondo i parametri delle clausole 8.2.2 e 8.2.3, con oauth2/token e "
            "con credentials/create, che puo' richiedere informazioni sul nuovo certificato di firma e/o sui "
            "meccanismi di autorizzazione richiesti per autorizzare l'uso della nuova credenziale per la firma "
            "(clausola 11.4 di CSC API). Sono prescritti l'applicabilita' dei metodi oauth2/authorize (clausola "
            "8.2.2), oauth2/pushed_authorize (clausola 8.2.3) e oauth2/token (clausola 8.2.4), il contenuto dei "
            "messaggi di richiesta (authorization code con la section Credential creation scope and "
            "authorization details; request URI con i componenti delle section Input e Credential creation scope "
            "and authorization details della clausola 8.2.2 tranne request_uri; access token con la clausola "
            "8.2.4 section Input) e dei messaggi di ritorno (authorization code e access token secondo le "
            "section Output delle clausole 8.2.2 e 8.2.4; request URI secondo IETF RFC 9126, clause 2.2). Il "
            "servizio di creazione di firme puo' inoltre raccogliere i subject data necessari alla certificate "
            "signing request in modi diversi, elencati in modo non esaustivo: quando sono supportate le Rich "
            "Authorization Requests (RAR), i subject data possono essere forniti nella authorization request; "
            "oppure i subject data possono essere raccolti dall'authorization server e resi disponibili al "
            "servizio remoto di creazione di firme negli authorization details dell'access token, come custom "
            "claims nell'access token o presso un token introspection endpoint."
        ),
        "testo_integrale": (
            "5.4 Credential creation authorization: Requesting credential creation to the signature creation "
            "service requires an authorization from the user to whom the credential to be created will be bound. "
            "CSC API [1] only supports OAuth 2.0 authorization to grant credential creation authorization. "
            "Figure 6: A general flow involving a driving application requesting signing credential creation to "
            "a signature creation service with an authorization process managed by an OAuth2 authorization "
            "server The above scheme is implemented in CSC API [1] by invoking the API: - oauth2/authorize (and "
            "oauth2/pushed_authorize if needed), possibly passing the subject data needed for the certificate "
            "signing request according to the parameters defined in clauses 8.2.2 and 8.2.3 of CSC API [1], that "
            "manages authorization requests using the Authorization Code flow as described in Section 4.1 of "
            "IETF RFC 6749 [17]. - oauth2/token to obtain an OAuth 2.0 bearer access token from the "
            "authorization server by passing the authorization code or refresh token returned by the "
            "authorization server after a successful credential creation authorization. - credentials/create to "
            "requests credential creation possibly requesting information about the new signing certificate "
            "and/or about the authorization mechanisms required to authorize the usage of the new credential for "
            "signing as specified in clause 11.4 of CSC API [1]. By invoking the oauth2/authorize API, via the "
            "user agent, the driving application can obtain an authorization code for credential creation "
            "authorization from the authorization server of the signature creation service. The oauth2/authorize "
            "API identified in CSC API [1], in clause 8.2.2 shall apply. The message for requesting the "
            "authorization code for credential creation authorization shall contain the components defined in "
            "CSC API [1], clause 8.2.2 considering what specified in section Credential creation scope and "
            "authorization details. The message for returning the authorization code for signatures creation "
            "authorization shall contain the components defined in CSC API [1], clause 8.2.2 section Output. By "
            "invoking the oauth2/pushed_authorize API the driving application can push the payload of an OAuth "
            "2.0 authorization request to the authorization server via a direct request and obtain a request URI "
            "to be used as reference to the data in a subsequent call to the authorization endpoint "
            "(oauth2/authorize) of the remote service. The oauth2/pushed_authorize API identified in CSC API "
            "[1], clause 8.2.3 shall apply. The message for requesting the request URI that will be used as "
            "reference to the data in a subsequent call to the authorization endpoint shall contain the "
            "components defined in CSC API [1], clause 8.2.2 sections Input and Credential creation scope and "
            "authorization details apart from the request_uri parameter. The message for returning the request "
            "URI shall contain the components defined in IETF RFC 9126 [18], clause 2.2. By invoking the "
            "oauth2/token API the driving application can obtain an access token for credential creation "
            "authorization from the authorization server of the remote service. The oauth2/token API identified "
            "in CSC API [1], clause 8.2.4 shall apply. The message for requesting the access token for "
            "credential creation authorization shall contain the components defined in CSC API [1], clause 8.2.4 "
            "section Input. The message for returning the access token for credential creation authorization "
            "shall contain the components defined in CSC API [1], clause 8.2.4 section Output. The signature "
            "creation service may collect the subject data needed for the certificate signing request in "
            "different ways. The following is a non-exhaustive list of possible ways: - when Rich Authorization "
            "Requests (RAR) are supported, the subject data may be provided in the authorization request; - the "
            "subject data may be collected by the authorization server and made available to the signature "
            "creation service remote service: - in the authorization details of the access token; - as custom "
            "claims in the access token [i.16]; - at a token introspection endpoint [i.8]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": (
            "clausola 5.5 (Credential deletion authorization)"
        ),
        "testo": (
            "La sottoclausola disciplina l'autorizzazione alla cancellazione di credenziali. Una credenziale "
            "puo' essere cancellata per vari motivi: fine del ciclo di vita (non piu' necessaria o scaduta), "
            "ragioni di sicurezza (compromissione o richiesta di revoca dell'utente) o conformita' regolamentare "
            "(obsolescenza degli algoritmi crittografici). La richiesta di cancellazione al servizio di "
            "creazione di firme richiede l'autorizzazione dell'utente che possiede e controlla la credenziale, "
            "oppure di un'applicazione driver fidata o di una terza parte fidata; quando l'autorizzazione alla "
            "cancellazione non e' richiesta al titolare della credenziale, lo SCSP dovrebbe informare il "
            "titolare quando una credenziale viene cancellata. CSC API supporta a questo fine solo "
            "l'autorizzazione OAuth 2.0. Il processo di cancellazione si realizza in CSC API invocando "
            "oauth2/authorize (e oauth2/pushed_authorize se necessario) secondo i parametri della clausola "
            "8.2.2, in particolare la section Credential deletion scope and authorization details, e della "
            "clausola 8.2.3, che gestiscono le richieste di autorizzazione con l'Authorization Code flow o, nel "
            "caso di applicazioni driver fidate, con il Client Credential flow (IETF RFC 6749, Section 4.1 e "
            "4.4); oauth2/token, eventualmente, per ottenere un bearer access token dall'authorization server "
            "passando l'authorization code o il refresh token restituiti dopo una cancellazione autorizzata; e "
            "credentials/delete come specificato nella clausola 11.5 di CSC API."
        ),
        "testo_integrale": (
            "5.5 Credential deletion authorization: A credential may be deleted for various reasons: - End of "
            "lifecycle: the credential is no longer needed or has expired. - Security reasons: the credential "
            "may be compromised or the user requests revocation. - Regulatory compliance: certain frameworks "
            "require deletion because of cryptographic algorithms obsolescence Requesting credential deletion to "
            "the signature creation service requires an authorization from the user who owns and controls the "
            "credential or from a trusted driving application or trusted third-party. In cases where credential "
            "deletion authorization is not requested to the credential owner, the SCSP should inform the "
            "credential owner when a credential is deleted. CSC API [1] only supports OAuth 2.0 authorization to "
            "grant credential deletion authorization. The deletion process is implemented in CSC API [1] by "
            "invoking the API: - oauth2/authorize (and oauth2/pushed_authorize if needed) according to the "
            "parameters defined in clause 8.2.2, specifically in section Credential deletion scope and "
            "authorization details, and clause 8.2.3 of CSC API [1], that manages authorization requests using "
            "the Authorization Code flow or the Client Credential flow, in case of trusted driving applications, "
            "as described respectively in Section 4.1 and 4.4 of IETF RFC 6749 [17]. - oauth2/token, possibly, "
            "to obtain an OAuth 2.0 bearer access token from the authorization server by passing the "
            "authorization code or refresh token returned by the authorization server after a successful "
            "credential deletion authorization. - credentials/delete to requests credential deletion as "
            "specified in clause 11.5 of CSC API [1]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": (
            "clausola 5.3.1 (Overview)"
        ),
        "testo": (
            "La sottoclausola inquadra l'autorizzazione alla creazione di firme: la richiesta a un servizio di "
            "creazione di firme richiede l'autorizzazione dell'utente che possiede e controlla la chiave di "
            "firma da usare, esistente o generata al volo. Sono considerati due livelli di confidenza del "
            "controllo della chiave definiti in ETSI EN 419 241-1: SCAL1, che assicura che l'operazione di firma "
            "sia eseguita per conto del firmatario ma con confidenza limitata (tipicamente autenticazione di "
            "base come username/password o PIN, senza binding crittografico fra Signature Activation Data e dati "
            "da firmare); e SCAL2, che richiede autenticazione piu' forte (es. multi-fattore, challenge-response "
            "crittografico) e binding crittografico fra SAD e dati da firmare, con la SAD collegata allo "
            "specifico documento o hash firmato e rischio di uso improprio ridotto. La credenziale di firma "
            "usata dall'applicazione driver puo' essere protetta direttamente dallo SCSP o tramite un framework "
            "come OAuth2, che consente alle applicazioni driver di accedere alla credenziale di firma "
            "dell'utente senza bisogno dei suoi dati di autenticazione. Le clausole successive descrivono i "
            "diagrammi di sequenza delle operazioni piu' comuni di richiesta e autorizzazione di una firma "
            "remota, con particolare riferimento all'uso del portafoglio europeo di identita' digitale (EUDIW), "
            "concepito per operare a livello di garanzia elevato (LoA High), come fattore di autenticazione del "
            "firmatario."
        ),
        "testo_integrale": (
            "5.3.1 Overview: Requesting signatures creation to a signature creation service requires an "
            "authorization from the user who owns and controls the signing key to be used for signatures "
            "creation. The user might authorize signatures creation with an already existing signing key or with "
            "a signing key to be created on-the-fly. Two different levels of confidence of the control of the "
            "signing key, as defined in EN 419 241-1 [6], are considered in the present document: - SCAL1 - Sole "
            "Control Assurance Level 1 that ensures that the signature operation is performed on behalf of the "
            "signer, but with limited confidence. Typically relies on basic authentication mechanisms (e.g. "
            "username/password or PIN). There is no cryptographic binding between the Signature Activation Data "
            "(SAD) and the data to be signed. - SCAL2 - Sole Control Assurance Level 2 that requires stronger "
            "authentication (e.g. multi-factor, cryptographic challenge-response) and cryptographic binding "
            "between the SAD and the data to be signed. This means the SAD is linked to the specific document or "
            "hash being signed, reducing the risk of misuse. The signing credential use by the driving "
            "application may be protected directly by the Signature Creation Service Provider (SCSP) or by means "
            "of a framework, like OAuth2, that allows the driving applications to obtain access to the user's "
            "signing credential without needing the user's authentication data. In the following clauses the "
            "sequence diagrams of some of the most common operations needed to request and authorize a remote "
            "signature creation are described, with particular reference to the possible use of the European "
            "Digital Identity Wallet (EUDIW), designed to operate at a Level of Assurance High (LoA), as a "
            "signer authentication factor."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["servizio di gestione di dispositivo di creazione di firma elettronica a distanza"],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 5.3.1 (Overview)",
    (
        "clausola 5.3.2 (Creating a remote signature with a credential protected by signature "
        "creation service-managed authorization)"
    ),
    "clausola 5.3.3 (Create a remote signature with a credential protected by OAuth2)",
    "clausola 5.4 (Credential creation authorization)",
    "clausola 5.5 (Credential deletion authorization)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Nessuna citazione letterale interna tra clausole/annessi della stessa Fonte
# in questo capitolo (tutti i rinvii sono a CSC API [1], IETF RFC 9110/6749/9126
# e ETSI EN 419 241-1): RELAZIONI vuoto. Il collegamento cross-fonte e' demandato
# alla Fase 6 della sessione principale (ADR-0009).
RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_completezza_testo_integrale, verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    verifica_completezza_testo_integrale([sys.modules[__name__]])
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
