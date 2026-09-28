"""ETSI TS 119 432 V1.3.1 (2026-03) - Electronic Signatures and Trust
Infrastructures (ESI); Protocols for remote digital signature creation.
Fonte 20 (la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 4 del
manifest: clausola 6 (Architectures and use cases for server signing) con le
sottoclausole 6.1 (Introduction), 6.2 e 6.3 (architetture con credenziale
protetta da autorizzazione gestita dal servizio di creazione della firma / da
OAuth 2.0), 6.4 (architetture basate sul portafoglio europeo di identita'
digitale) con 6.4.1 (Overview), 6.4.2, 6.4.3, 6.4.4 (6.4.4.1 Introduction,
6.4.4.2 EUDIW registration, 6.4.4.3 EUDIW authentication, 6.4.4.4 Security
requirements, 6.4.4.5 Examples con 6.4.4.5.1-6.4.4.5.6) e 6.4.5 (6.4.5.1
Introduction, 6.4.5.2 client registration). Testo ufficiale in
app/.source_cache/etsi_119_432/cap04.txt (letto con selettore `:raw`, altrimenti
il tool tronca le righe lunghe a 768 caratteri introducendo ellissi e mutilando
la copia verbatim). Manifest di split:
app/.source_cache/etsi_119_432/manifest.json.

Modellazione (ADR-0007), stesso criterio dei capitoli cap01-cap03 di questa
fonte e delle altre fonti ETSI censite: un nodo per ogni clausola/sottoclasola
numerata con contenuto proprio (nessun discrimine di rilevanza), un nodo
Principio per le parti descrittive/illustrative. Il capitolo produce 6 Obblighi
e 12 Principi su 18 item di indice. Scelte voce per voce:

- Clausola 6 (Architectures and use cases for server signing) -> NESSUN nodo:
  intestazione di puro raggruppamento, il testo ufficiale non le associa alcun
  periodo proprio (segue immediatamente 6.1 Introduction). Stesso trattamento
  per le intestazioni di raggruppamento 6.4 (Architectures for creating remote
  signatures using the European Digital Identity Wallet), 6.4.4 (EUDIW
  registration and authentication to authorization servers), 6.4.4.5 (Examples)
  e 6.4.5 (DA / SCA registration and authentication to authorization servers):
  tutte immediatamente seguite dalla rispettiva sottoclasola
  "Introduction"/"Overview"/"Examples", senza testo proprio.
- Clausola 6.1 (Introduction) -> 1 Principio "altro": descrive l'impianto del
  capitolo (tre classi di modelli architetturali, governance e responsabilita'
  finale in capo al prestatore del servizio di creazione della firma,
  ammissibilita' di modelli diversi con livelli di sicurezza comparabili,
  equivalenza delle considerazioni su CSC per OASIS DSS-X). Nessun verbo
  prescrittivo e nessun soggetto obbligato: e' una introduzione descrittiva,
  non la clausola di scopo del documento (che e' la clausola 1, capitolo
  cap01), quindi "altro" e non "scopo/ambito di applicazione" (punto 1 delle
  clausole ambigue).
- Clausola 6.2 (Architectures for creating remote signatures with a credential
  protected by signature creation service-managed authorization) -> 1 Principio
  "altro": architetture illustrate da esempi (diagrammi di sequenza, figure
  7-9). La NOTE premessa contiene un "should not be suitable to satisfy SCAL2
  requirements": e' un giudizio di idoneita' privo di soggetto obbligato e
  collocato in una nota, quindi non e' stato modellato come Obbligo.
- Clausola 6.3 (Architectures for creating remote signatures with a credential
  protected by OAuth2) -> 1 Principio "altro": descrizione dell'uso
  dell'authorization server OAuth 2.0 e delle possibili modalita' di richiesta
  di autorizzazione (parametri credentialID/signatureQualifier, dati da
  firmare, numero di firme, attributi firmati). I rinvii alle clausole 8.2.2 e
  8.2.3 di CSC API sono a una fonte esterna e non generano relazioni in questa
  fase.
- Clausola 6.4.1 (Overview) -> 1 Obbligo "tecnico/sicurezza": la clausola
  inquadra il ricorso all'EUDIW ma contiene due prescrizioni con soggetto
  identificabile ("EUDIWs shall allow users to sign using qualified electronic
  signatures and to seal using qualified electronic seals. In particular, they
  shall support common protocols and standardized interfaces for creating
  qualified electronic signatures or seals through qualified electronic
  signature or seal creation devices."), quindi Obbligo e non Principio; la
  clausola e' indivisibile ai fini dell'indice (una sola sottoclasola
  numerata) e il resto del testo, descrittivo, e' comunque riportato per intero
  in `testo_integrale`.
- Clausola 6.4.2 (EUDIW as authentication and authorization layer for creating
  remote signatures) -> 1 Principio "altro": architettura descritta per figure
  (12-19), varianti e passi chiave. I due "may" presenti ("the Authorization
  Server may transmit an OpenID4VP request to the EUDIW SIC component ...",
  "Additional delivery mechanisms may be supported if implemented by the EUDIW
  SIC component") sono possibilita' tecniche senza obbligo di risultato e senza
  soggetto determinato: Principio e non Obbligo (punto 3 delle clausole
  ambigue).
- Clausola 6.4.3 (EUDIW participating in the signature creation process) -> 1
  Obbligo "organizzativo": la clausola descrive i modelli in cui l'EUDIW
  partecipa alla creazione della firma, ma i "Key Steps" contengono un obbligo
  esplicito e soggettivato ("Before interacting with the EUDIW, the WRP shall:
  register with a Wallet-Relying Party Registrar in its member state; provide
  legal identifiers and contact details, a Registration Certificate specifying
  the intended use of the data and an Access Certificate proving its identity
  and authorization."), che vincola il Wallet Relying Party, cioe' la parte
  affidante, e non il QTSP. Clausola indivisibile ai fini dell'indice: un solo
  nodo, con `condizione_applicabilita` che esplicita la condizione ("Before
  interacting with the EUDIW").
- Clausola 6.4.4.1 (Introduction) -> 1 Principio "scopo/ambito di
  applicazione": "This clause defines the requirements for an EUDIW acting as
  an OAuth 2.0 client to register and authenticate to an authorization
  server ..." dichiara l'ambito dei requisiti delle sottoclausole seguenti,
  senza prescrivere alcun comportamento.
- Clausola 6.4.4.2 (EUDIW registration) -> 1 Obbligo "tecnico/sicurezza":
  sequenza di "shall" su authorization server, EUDIW e SCS (implementazione di
  FAPI 2.0 Security Profile e IETF RFC 7591, contenuto obbligatorio della
  registrazione dinamica, inclusione della chiave pubblica WUA nel jwks,
  gestione del claim client_attestation, codici di risposta HTTP 201 e HTTP
  400). Un solo nodo perche' la clausola e' indivisibile ai fini dell'indice; i
  "may" (convalida dell'evidenza WUA, ignorare claim/parametri non supportati)
  restano descritti in `testo` e verbatim in `testo_integrale` come facolta' del
  soggetto obbligato.
- Clausola 6.4.4.3 (EUDIW authentication) -> 1 Obbligo "tecnico/sicurezza":
  cinque "shall" sull'EUDIW (capacita' di client OAuth 2.0, Authorization Code
  Flow con PKCE, PAR con JAR firmato, autenticazione private_key_jwt, uso di
  state/nonce e convalida dei metadati dell'issuer).
- Clausola 6.4.4.4 (Security requirements) -> 1 Obbligo "tecnico/sicurezza":
  "shall" su authorization server, EUDIW e SCS per l'emissione di access token
  e refresh token sender-constrained con DPoP e per la convalida delle prove
  DPoP; i due "should" (raccomandazioni di IETF RFC 8725, accettazione dei
  token con prove DPoP da parte della SCS) sono assorbiti nello stesso nodo
  indivisibile.
- Clausole 6.4.4.5.1-6.4.4.5.6 -> 6 Principi "altro", uno per sottoclasola:
  sono blocchi EXAMPLE (payload JSON, risposte e richieste HTTP, reindirizzo
  con authorization code) privi di valore prescrittivo. `testo_integrale`
  riporta il blocco verbatim conservando la struttura di riga originale (le
  righe di payload non sono state unite come la prosa) e riproducendo
  letteralmente i `...` interni ai token JWT/Base64: in questo standard
  l'abbreviazione dei payload di esempio e' contenuto autentico del testo
  ufficiale, non un'elisione di estrazione (la guardia
  `verifica_completezza_testo_integrale` esenta questa convenzione fra le tre
  note).
- Clausola 6.4.5.1 (Introduction) -> 1 Principio "scopo/ambito di
  applicazione": dichiara l'ambito (requisiti per una DA o una SCA come client
  OAuth 2.0) e fissa la convenzione terminologica ("client" = DA o SCA).
- Clausola 6.4.5.2 (client registration) -> 1 Obbligo "tecnico/sicurezza":
  come 6.4.4.2 ma per il client DA/SCA; il "may" sulla registrazione dinamica e
  quello sulla configurazione pre-registrata (statica) sono facolta' del
  client, mentre i "shall" su authorization server (implementazione FAPI 2.0 e
  RFC 7591, convalida dell'evidenza WUA, restituzione non modificata del
  software statement, errori HTTP 400) sono obblighi. Il soggetto "client" e'
  la DA (che puo' essere erogata dalla parte affidante) o la SCA (presso il
  QTSP): entrambe le categorie sono state censite come soggetti obbligati
  (punto 6 delle clausole ambigue).

Convenzioni di trascrizione applicate a `testo_integrale` (nessuna incide sul
contenuto normativo):
- header/footer di pagina del PDF ("ETSI TS 119 432 V1.3.1 (2026-03)", "ETSI",
  numeri di pagina, "<!-- Page N -->") rimossi: sono paratesto spurio della
  conversione, non testo di clausola;
- i caratteri "‑" (non-breaking hyphen) isolati su una riga o a fine riga
  sono artefatti di conversione dell'andata a capo del PDF e sono stati
  rimossi ricongiungendo la prosa; i due U+2011 interni a parola
  ("browser‑based", "EUDIW‑resident") sono stati normalizzati al
  trattino ASCII "-" per consentire la ricerca full-text;
- il glifo privato U+F0A7 (pallino di elenco in font Symbol prodotto dalla
  conversione) e' stato normalizzato al pallino "•";
- le didascalie delle figure ("Figure 7: ...", "Figure 12: ...", ecc.) sono
  parte del testo ufficiale della clausola e sono state riportate in
  `testo_integrale` (stessa convenzione gia' usata nei moduli delle altre fonti
  ETSI censite), non nella sintesi `testo`;
- la prosa e' stata ricomposta unendo le righe di ciascun paragrafo (l'andata a
  capo a ~120 caratteri e' un artefatto del PDF), mentre i blocchi di esempio
  di 6.4.4.5.x conservano la struttura di riga originale.

RELAZIONI: una sola relazione interna alla Fonte, testuale. In 6.4.3 il testo
cita letteralmente l'annesso A ("In annex A, a profile designing such a
request-response protocol is defined."): la relazione e' ancorata alla prima
sottoclasola numerata dell'annesso, "Annex A.1 (Overview)" (capitolo cap06,
autoria parallela), perche' l'intestazione dell'annesso e' pura intestazione di
raggruppamento (immediatamente seguita da A.1) e quindi non genera nodo. Se
cap06 nominasse la sottoclasola in modo diverso, la stringa va allineata in sede
di merge, altrimenti la relazione non e' risolvibile dal registro. Tutte le
altre citazioni del capitolo (CSC API, CSC data model bindings, OpenID for
Verifiable Presentations, Digital Credentials API, IETF RFC, SCAL2, EUDIW
reference architectures) sono a fonti esterne: il collegamento cross-fonte e'
demandato alla Fase 6 della sessione principale (ADR-0009) e non genera
relazioni qui.

Clausole di classificazione ambigua (scelta fatta e motivo):
1. 6.1 Introduction: "altro" invece di "scopo/ambito di applicazione" - la
   clausola descrive l'impianto del capitolo, non l'ambito di applicazione del
   documento, e non ha effetto giuridico specifico ne' soggetto obbligato.
2. 6.4.1 Overview: Obbligo "tecnico/sicurezza" invece di Principio - la
   clausola e' prevalentemente descrittiva, ma contiene due "shall" con
   soggetto identificabile (i portafogli elettronici di identita' digitale) e
   ADR-0007 ammette un solo nodo per clausola numerata: la presenza di un
   obbligo determina la classificazione. Soggetto censito come "QTSP/gestore":
   il vocabolario chiuso non prevede una categoria per il fornitore del
   portafoglio, e questa e' la categoria con cui il censimento eIDAS2 gia' in
   seed.py mappa gli obblighi dei fornitori di portafogli (art. 5 bis).
3. 6.4.2: i "may" sulle modalita' di consegna della richiesta OpenID4VP sono
   facolta' tecniche senza obbligo di risultato -> Principio "altro" e non
   Obbligo.
4. 6.4.3: Obbligo "organizzativo" (non "tecnico/sicurezza") perche' il
   requisito con soggetto identificabile e' la registrazione del WRP presso il
   registrar e la messa a disposizione di identificativi, dati di contatto e
   certificati: adempimento organizzativo, non prescrizione tecnica.
5. 6.4.4.1 e 6.4.5.1: "scopo/ambito di applicazione" invece di "altro" perche'
   dichiarano espressamente ("This clause defines the requirements for ...")
   l'ambito dei requisiti delle sottoclausole successive; la clausola
   introduttiva 6.1 resta invece "altro".
6. 6.4.5.2: soggetti obbligati sia "QTSP/gestore" (authorization server e
   SCA) sia "Terzi affidanti/pubblico" (il client DA, quando erogato dalla
   parte affidante): la clausola usa "client" per entrambe le configurazioni.
7. 6.4.4.2/6.4.4.3/6.4.4.4: soggetto unico "QTSP/gestore" per authorization
   server, EUDIW e SCS, che il vocabolario chiuso non distingue (stessa scelta
   del punto 2); i ruoli effettivi restano espliciti in `testo`.
8. 6.4.4.5.1-6.4.4.5.6: Principio "altro" e non "definitorio" - non
   definiscono termini ma esemplificano payload e scambi HTTP.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 6.4.1 (Overview)",
        "testo": (
            "Clausola di inquadramento dell'uso del portafoglio europeo di identita' digitale (EUDIW) per "
            "la creazione di firme remote: nell'Unione le firme elettroniche qualificate sono disciplinate "
            "dal regolamento eIDAS, che definisce l'EUDIW come mezzo di identificazione elettronica che "
            "consente all'utente di conservare, gestire e convalidare in modo sicuro dati di "
            "identificazione personale e attestati elettronici di attributi, di presentarli a parti "
            "affidanti e ad altri portafogli e di creare firme elettroniche qualificate o sigilli "
            "elettronici qualificati. I portafogli elettronici di identita' digitale devono consentire agli "
            "utenti di firmare con firme elettroniche qualificate e di sigillare con sigilli elettronici "
            "qualificati e, in particolare, devono sostenere protocolli comuni e interfacce standardizzate "
            "per la creazione di firme o sigilli elettronici qualificati tramite dispositivi qualificati di "
            "creazione di firma o sigillo elettronico. Per la creazione di firme remote con l'EUDIW sono "
            "possibili piu' modelli, nei quali il portafoglio svolge due ruoli principali: livello di "
            "autenticazione e autorizzazione limitato all'autenticazione dell'utente e alla conferma del "
            "consenso, senza eseguire la creazione della firma; oppure mediatore del flusso di dati, che "
            "inoltra in modo sicuro i dati da firmare (DTBS) o il loro hash al servizio di creazione della "
            "firma e assume il ruolo primario di richiedente che avvia il processo di creazione quando "
            "implementa la DA o la SCA."
        ),
        "testo_integrale": (
            """Overview: In the European Union, Qualified Electronic Signatures (QES) are governed by the eIDAS Regulation [i.1]. This regulation defines the European Digital Identity Wallet (EUDIW) as an electronic identification means that enables users to securely store, manage, and validate personal identification data and electronic attestations of attributes. The EUDIW serves the purpose of presenting these credentials to relying parties and other EUDIW users, and of performing qualified electronic signatures or qualified electronic seals.

EUDIWs shall allow users to sign using qualified electronic signatures and to seal using qualified electronic seals. In particular, they shall support common protocols and standardized interfaces for creating qualified electronic signatures or seals through qualified electronic signature or seal creation devices.

Several models may be implemented for remote signature creation using the EUDIW, depending on the signature creation flow and the authorization process. In these models two main roles can be played by the EUDIW:

   •     EUDIW serves as the authentication and authorization layer restricted to user authentication and consent confirmation without performing signature creation.

   •     EUDIW serves as a mediator for the data flow, acting as a secure party that relays the Data To Be Signed (DTBS) or its hash to the signature creation service, while also assuming a primary role as the requestor initiating the signature creation process when implementing the DA or SCA."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.4.3 (EUDIW participating in the signature creation process)",
        "testo": (
            "Descrive i modelli in cui l'EUDIW partecipa al processo di creazione della firma: il "
            "portafoglio coordina la creazione di firme AdES tramite una SCASC (che puo' far parte "
            "dell'EUDIW o del suo backend) che interagisce con la SSASC erogata dal QTSP; il Wallet Relying "
            "Party (WRP) trasmette all'EUDIW i dati da firmare attraverso un processo strutturato e "
            "regolato che assicura fiducia, trasparenza e controllo dell'utente; il portafoglio raccoglie "
            "il consenso e i documenti o i DTBS/R da firmare, impacchetta l'AdES e richiede alla SSASC il "
            "valore crittografico della firma (in alternativa la SCA e' implementata nello stesso "
            "dispositivo dell'EUDIW, senza farne parte). Requisito organizzativo: prima di interagire con "
            "l'EUDIW il WRP deve registrarsi presso un Wallet-Relying Party Registrar del proprio Stato "
            "membro e fornire identificativi legali e dati di contatto, un certificato di registrazione che "
            "specifichi l'uso previsto dei dati e un certificato di accesso che provi la sua identita' e la "
            "sua autorizzazione. Il WRP costruisce poi una richiesta di presentazione comprendente i dati "
            "da firmare (ad esempio una challenge o i dettagli della transazione), lo scopo della richiesta "
            "coerente con l'uso dichiarato e il certificato di accesso, e la trasmette all'EUDIW in flusso "
            "same-device, cross-device o di prossimita'. L'EUDIW convalida il certificato del WRP e la "
            "catena di fiducia, verifica che la richiesta di dati sia coerente con lo scopo dichiarato, "
            "presenta la richiesta all'utente per il consenso e, se l'utente approva, firma i dati con la "
            "credenziale o la chiave appropriata e restituisce i dati firmati al WRP. Il contenuto "
            "dell'oggetto della richiesta di firma passato all'EUDIW e della relativa risposta sono "
            "specificati nella clausola 8 di CSC data model bindings; l'identificatore del tipo di dati di "
            "transazione per richiedere all'EUDIW la creazione di firme o sigilli elettronici qualificati "
            "e' https://cloudsignatureconsortium.org/2025/qes; nell'annesso A e' definito un profilo che "
            "progetta tale protocollo di richiesta-risposta."
        ),
        "testo_integrale": (
            """EUDIW participating in the signature creation process: In the model outlined in Figure 20, the EUDIW coordinates AdES signature creation through a SCASC, that may be part of the EUDIW or of the EUDIW backend, interacting with the QTSP-operated SSASC. The Wallet Relying Party (WRP) can pass data to be signed by the EUDIW through a structured and regulated process that ensures trust, transparency, and user control. The user's EUDIW plays the central role in managing the signature process to sign documents and to control and approve necessary transactions. The EUDIW collects consent and documents or DTBS/R to be signed, packages AdES, and requests the cryptographic signature value from the SSASC.

In the model outlined in Figure 21, the SCA is implemented in the same user device where the EUDIW is implemented too but is not part of the EUDIW itself.

           Figure 20: Architecture with SCA and DA at different independent intermediaries and with EUDIW integrating SCA and SIC

             Figure 21: Architecture with SCA and DA at different independent intermediaries and with EUDIW and SCA in the same user device

Key Steps:

   •    WRP Registration and Trust Establishment. Before interacting with the EUDIW, the WRP shall:

        -     register with a Wallet-Relying Party Registrar in its member state;

        -     provide legal identifiers and contact details, a Registration Certificate specifying the intended use of the data and an Access Certificate proving its identity and authorization.

   •    Presentation Request with Data to be Signed. To pass data to be signed by the EUDIW, the WRP constructs a Presentation Request that includes:

        -     the data to be signed (e.g. a challenge, transaction details);

        -     the purpose of the request, aligned with the declared intended use;

        -     the Access Certificate to authenticate itself.

   •    The Presentation Request is sent to the EUDIW either in a Same-Device flow (where WRP service and EUDIW run on the same device, e.g. using a deep link) or in a Cross-Device flow (where WRP service runs on one device, e.g. PC browser, and EUDIW runs on another, e.g. mobile app, often using QR codes) or in a Proximity-Based flow (e.g. using NFC or Bluetooth®).

   •    Wallet Validation and User Consent. The EUDIW validates the WRP's certificate and the trust chain, checks that the data request aligns with the RP's declared purpose, presents the request to the user for consent, if the user approves, the EUDIW signs the data using the appropriate credential or key and returns the signed data to the WRP.

    In Figure 22 representing a simplified signature model with EUDIW integrating SCA and SIC, the data flows between different components are outlined.

        Figure 22: Generic simplified signature model flow with EUDIW integrating SCA and SIC

The content of the signature request object passed to the EUDIW and of its response are specified in clause 8 of CSC data model bindings [3]. The transaction data type identifier is https://cloudsignatureconsortium.org/2025/qes for requesting qualified electronic signatures or seals creation to EUDIW. Other more suitable request-response protocols for data other than verifiable presentations can arise in the future and could be used for this purpose. In annex A, a profile designing such a request-response protocol is defined."""
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": (
            "quando il Wallet Relying Party (WRP) interagisce con il portafoglio europeo di identita' "
            "digitale per ottenere la firma di dati"
        ),
        "soggetti": [{"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.4.4.2 (EUDIW registration)",
        "testo": (
            "Registrazione dell'EUDIW come client OAuth 2.0: gli authorization server devono implementare "
            "il FAPI 2.0 Security Profile e IETF RFC 7591 (OAuth 2.0 Dynamic Client Registration Protocol) "
            "e accettare richieste di registrazione che includano valori di metadati del client specificati "
            "come claim in un software statement. L'EUDIW deve registrarsi dinamicamente fornendo: "
            "redirect_uris; jwks (il JSON Web Key Set del portafoglio, che contiene le sue chiavi pubbliche "
            "e deve includere la chiave pubblica della Wallet Unit Attestation usata dall'EUDIW); "
            "token_endpoint_auth_method con valore private_key_jwt; grant_types con il valore "
            "\"authorization_code\"; response_types con il valore \"code\"; software_statement con i claim "
            "software_id (identificativo univoco del software del client, che deve includere l'attributo "
            "refNum con il numero di riferimento della soluzione di portafoglio), client_name (nome "
            "leggibile, che deve includere la stringa \"European Digital Identity Wallet\") e "
            "client_attestation opzionale (attestazione che l'authorization server puo' usare per valutare "
            "se accettare la registrazione in base al rapporto di fiducia con l'emittente del software "
            "statement, comprendente la WUA e in particolare la chiave pubblica del claim jwks, che "
            "l'authorization server puo' ignorare); altri parametri opzionali di OpenID Connect Relying "
            "Party Metadata Choices 1.0 - draft 04, che l'authorization server puo' ignorare se non "
            "supportati. L'authorization server puo' convalidare l'evidenza della WUA e rifiutare la "
            "registrazione se l'attestazione e' invalida, scaduta o revocata; la SCS deve fornire "
            "l'informazione che indica se il claim client_attestation e' obbligatorio, opzionale o non "
            "supportato. In caso di registrazione riuscita l'authorization server deve rispondere con il "
            "codice HTTP 201 \"Created\" e un corpo di tipo application/json con client_id (identificativo "
            "che non dovrebbe essere valido per altri client registrati) e tutti i metadati registrati del "
            "portafoglio, incluso il software statement restituito non modificato; in caso di registrazione "
            "non riuscita deve restituire il codice HTTP 400 con content type application/json e un oggetto "
            "JSON con error e error_description (opzionale)."
        ),
        "testo_integrale": (
            """EUDIW registration:    •      The authorization servers shall implement the FAPI 2.0 Security Profile and IETF RFC 7591 [11], OAuth 2.0 Dynamic Client Registration Protocol.

   •      The authorization servers shall accept registration requests including client metadata values specified as claims in a software statement.

   •      The EUDIW shall register dynamically implementing requirements specified in IETF RFC OAuth 2.0 Dynamic Client Registration Protocol providing:

          -    redirect_uris: the redirection URI strings for use in redirect-based flows;

          -    jwks: EUDIW's JSON Web Key Set as specified in IETF RFC 7517 [12], which contains the EUDIW's public keys, the WUA public key used by the EUDIW shall be included;

          -    token_endpoint_auth_method: containing the value private_key_jwt;

          -    grant_types: the grant type strings that the EUDIW can use at the token endpoint, the value "authorization_code", representing the authorization code grant type defined in OAuth 2.0 clause 4.1, shall be included;

          -    response_types: the OAuth 2.0 response type strings that the EUDIW can use at the authorization endpoint, the value "code", representing the authorization code response type defined in OAuth 2.0 clause 4.1, shall be included;

          -    software_statement: metadata values about the EUDIW software including the following claims:

               •     software_id: a unique identifier string used by registration endpoints to identify the client software to be dynamically registered, it shall include the attribute refNum, that specifies the reference number of the wallet solution, as defined in class WalletSolution as defined in the specification of systems enabling the notification and subsequent publication of EUDIW provider information;

               •     client_name: human-readable string name of the EUDIW to be presented to the end-user during authorization, it shall include the string "European Digital Identity Wallet";

               •     client_attestation (optional): an attestation that the authorization server may use to evaluate whether accepting or not the registration request depending on the trust relationship the authorization server has with the issuer of the software statement, if provided it shall include the EUDIW's Wallet Unit Attestation (WUA), allowing authorization servers to trust the integrity of digital identities and attributes stored within the EUDIW, in particular the public key included in the claim jwks, the authorization servers may ignore this claim.

          -    other optional client metadata parameters defined in OpenID Connect Relying Party Metadata Choices 1.0 - draft 04 [13] that the authorization server may ignore if not supported.

  •       The authorization servers may validate WUA evidence and reject registration if the attestation is invalid, expired, or revoked.

  •       The SCS shall provide the information stating if the client_attestation claim is mandatory or optional or not supported.

  •       Upon a successful registration request, the authorization server shall respond with an HTTP 201 "Created status" code and a body of type "application/json" with the following fields:

          -    client_id: the OAuth 2.0 client identifier string that should not be valid for any other registered client, though an authorization server may issue the same client identifier to multiple instances of a registered client at its discretion;

          -    all registered metadata about the EUDIW, including the software statement used as part of the registration request whose value shall be returned unmodified in the response.

  •       Upon an unsuccessful registration request, the authorization server shall return an HTTP 400 status code with content type "application/json" consisting of a JSON object (IETF RFC 8259 [i.9]), describing the error in the response body, with two members:

          -    error: single ascii error code string.

          -    error_description: human-readable ASCII text description of the error (optional)."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.4.4.3 (EUDIW authentication)",
        "testo": (
            "Autenticazione dell'EUDIW: il portafoglio deve implementare le capacita' di client OAuth 2.0, "
            "deve usare l'Authorization Code Flow con PKCE (IETF RFC 7636) e deve usare PAR (IETF RFC 9126) "
            "con un JAR firmato (IETF RFC 9101) per l'integrita' della richiesta; l'autenticazione "
            "dell'EUDIW agli endpoint PAR e token deve essere supportata tramite private_key_jwt come "
            "specificato nella Sezione 9 di OIDC; il portafoglio deve inoltre usare i claim state e nonce e "
            "convalidare i metadati dell'issuer (IETF RFC 8414) come specificato in IETF RFC 9207."
        ),
        "testo_integrale": (
            """EUDIW authentication:   •       The EUDIW shall implement OAuth 2.0 client capabilities.

  •       The EUDIW shall use Authorization Code Flow with PKCE (IETF RFC 7636 [14]).

  •       The EUDIW shall use PAR (IETF RFC 9126 [18]) with a signed JAR (IETF RFC 9101 [31]) for request integrity.

  •       The EUDIW authentication at PAR and token endpoints shall be supported via private_key_jwt as specified in Section 9 of OIDC.

    •     The EUDIW shall use state and nonce claims and validate issuer metadata (IETF RFC 8414 [15]) as specified in IETF RFC 9207 [24]."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.4.4.4 (Security requirements)",
        "testo": (
            "Requisiti di sicurezza per i token vincolati al possessore: l'authorization server deve "
            "supportare l'emissione di access token e refresh token sender-constrained implementando il "
            "meccanismo a livello applicativo DPoP (Demonstrating Proof of Possession) come specificato in "
            "IETF RFC 9449 e previsto da FAPI; l'EUDIW deve firmare il DPoP secondo la sintassi JWT con la "
            "chiave privata la cui parte pubblica e' inclusa nella WUA; il DPoP deve includere i campi "
            "specificati nella clausola 4.2 di IETF RFC 9449; nella creazione del DPoP secondo la sintassi "
            "JWT dovrebbero essere seguite le raccomandazioni di IETF RFC 8725; la SCS dovrebbe accettare "
            "access token con prove DPoP e, se li accetta, deve convalidare ogni JWT di prova DPoP."
        ),
        "testo_integrale": (
            """Security requirements:     •     The authorization server shall support issuance of sender-constrained access and refresh tokens by implementing the application-level mechanism Demonstrating Proof of Possession (DPoP), as specified in IETF RFC 9449 [25] as per FAPI.

    •     The EUDIW shall sign the DPoP according to JWT syntax with the private key whose public part is included in the WUA.

    •     The DPoP shall include the fields specified in clause 4.2 of IETF RFC 9449 [25].

    •     When creating the DPoP according to JWT syntax the recommendations provided in IETF RFC 8725 [26] should be followed.

    •     SCS should accept access tokens with DPoP proofs.

    •     If SCS accepts access tokens with DPoP proofs it shall validate any DPoP proof JWT."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.4.5.2 (client registration)",
        "testo": (
            "Registrazione del client (DA o SCA) come client OAuth 2.0: l'authorization server deve "
            "implementare il FAPI 2.0 Security Profile e IETF RFC 7591 (OAuth 2.0 Dynamic Client "
            "Registration Protocol) e accettare richieste di registrazione che includano valori di metadati "
            "del client specificati come claim in un software statement. Il client puo' registrarsi "
            "dinamicamente fornendo redirect_uris; jwks o jwks_uri (il JSON Web Key Set del client, che "
            "deve includere la chiave pubblica del suo certificato di registrazione); "
            "token_endpoint_auth_method con valore private_key_jwt; grant_types con il valore "
            "\"authorization_code\"; response_types con il valore \"code\"; software_statement con i claim "
            "software_id, client_name e client_attestation (attestazione che l'authorization server usa per "
            "valutare se accettare la registrazione in base al rapporto di fiducia con l'emittente del "
            "software statement, comprendente il certificato di registrazione del client e in particolare "
            "la chiave pubblica del claim jwks); altri parametri opzionali di OpenID Connect Relying Party "
            "Metadata Choices 1.0 - draft 04, che l'authorization server puo' ignorare se non supportati. "
            "L'authorization server deve convalidare l'evidenza della WUA e rifiutare la registrazione se "
            "l'attestazione e' invalida, scaduta o revocata. In caso di registrazione riuscita "
            "l'authorization server deve rispondere con il codice HTTP 201 \"Created\" e un corpo di tipo "
            "application/json con client_id e tutti i metadati registrati, incluso il software statement "
            "restituito non modificato; in caso di registrazione non riuscita deve restituire il codice "
            "HTTP 400 con content type application/json e un oggetto JSON con error e error_description "
            "(opzionale). Il client puo' inoltre essere configurato con dati di autenticazione "
            "pre-registrati (statici), appropriati nel caso di ecosistemi chiusi, applicazioni di guida "
            "emesse da un'autorita' nazionale o authorization server e client appartenenti allo stesso "
            "quadro di fiducia: in tal caso la registrazione avviene manualmente fuori banda con "
            "l'operatore dell'authorization server, che rilascia client_id e uno tra client_secret, una "
            "chiave pubblica (se si usa private_key_jwt) o un certificato (se si usa mTLS)."
        ),
        "testo_integrale": (
            """client registration:     •     The authorization server shall implement the FAPI 2.0 Security Profile and IETF RFC 7591 [11] OAuth 2.0 Dynamic Client Registration Protocol.

    •     The authorization server shall accept registration requests including client metadata values specified as claims in a software statement.

    •     The client may register dynamically implementing requirements specified in IETF RFC OAuth 2.0 Dynamic Client Registration Protocol providing:

          -    redirect_uris: the redirection URI strings for use in redirect-based flows;

    -    jwks: client's JSON Web Key Set as specified in IETF RFC 7517 [12], which contains the client's public keys, the client's registration certificate public key shall be included;

    -    jwks_uri: URL string referencing the client's JSON Web Key Set as specified in IETF RFC 7517 [12], which contains the client's public keys, the client's registration certificate public key shall be included;

    -    token_endpoint_auth_method: containing the value private_key_jwt;

    -    grant_types: the grant type strings that the client can use at the token endpoint, the value "authorization_code", representing the authorization code grant type defined in OAuth 2.0 clause 4.1, shall be included;

    -    response_types: the OAuth 2.0 response type strings that the client can use at the authorization endpoint, the value "code", representing the authorization code response type defined in OAuth 2.0 clause 4.1, shall be included;

    -    software_statement: metadata values about the client software including the following claims:

         •     software_id: a unique identifier string used by registration endpoints to identify the client software to be dynamically registered;

         •     client_name: human-readable string name of the client to be presented to the end-user during authorization;

         •     client_attestation: an attestation that the authorization server uses to evaluate whether accepting or not the registration request depending on the trust relationship the authorization server has with the issuer of the software statement, it shall include the client's registration certificate, allowing authorization servers to trust the integrity of the client's digital identities and attributes, in particular the public key included in the claim jwks;

    -    other optional client metadata parameters defined in OpenID Connect Relying Party Metadata Choices 1.0 - draft 04 [13] that the authorization server may ignore if not supported.

•   The authorization server shall validate WUA evidence and reject registration if the attestation is invalid, expired, or revoked.

•   Upon a successful registration request, the authorization server shall respond with an HTTP 201 "Created status" code and a body of type "application/json" with the following fields:

    -    client_id: the OAuth 2.0 client identifier string that should not be valid for any other registered client, though an authorization server may issue the same client identifier to multiple instances of a registered client at its discretion;

    -    all registered metadata about the EUDIW, including the software statement used as part of the registration request whose value shall be returned unmodified in the response.

•   Upon an unsuccessful registration request, the authorization server shall return an HTTP 400 status code with content type "application/json" consisting of a JSON object (IETF RFC 8259 [i.9]), describing the error in the response body, with two members:

    -    error: single ascii error code string;

    -    error_description: human-readable ASCII text description of the error (optional).

• The client may be configured with pre registered (static) client authentication data. Appropriate in the case of

    closed ecosystems, driving applications issued by a national authority, authorization server and client belonging to the same trust framework. The client is manually registered out of band with the authorization server operator, who issues:

    -    client_id.

    -    one of:

         •     client_secret.

         •     a public key, if using private_key_jwt.

               •     a certificate, if using mTLS."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}, {"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 6.1 (Introduction)",
        "testo": (
            "Il capitolo introduce i modelli architetturali per la creazione di firme elettroniche remote, "
            "distinti dal meccanismo di protezione della credenziale del firmatario e di gestione "
            "dell'autorizzazione richiesta per la creazione della firma: la prima classe di architetture "
            "protegge la credenziale con un meccanismo di autorizzazione interamente gestito dal servizio "
            "di creazione della firma, la seconda si basa su OAuth 2.0 per una delega di autorizzazione "
            "standardizzata e interoperabile, la terza impiega il portafoglio europeo di identita' digitale "
            "(EUDIW) come componente centrale di autenticazione, autorizzazione e orchestrazione della "
            "creazione della firma. La governance e la responsabilita' finale dei meccanismi di "
            "autenticazione e autorizzazione restano in capo al prestatore del servizio di creazione della "
            "firma; modelli architetturali diversi da quelli descritti sono ammessi purche' raggiungano "
            "livelli di sicurezza comparabili. Dove nelle sottoclausole successive si fa riferimento a CSC, "
            "valgono in genere le stesse considerazioni per OASIS DSS-X."
        ),
        "testo_integrale": (
            """Introduction: The following clauses describe a set of architectural models for the creation of remote electronic signatures, each distinguished by the mechanisms used to protect the signer's credential and to manage the authorization required for signature creation. The models differ in the interaction between components and in the authentication and authorization flows, but the governance and final responsibility of authentication and authorization mechanisms remain with the signature creation service provider.

The first clause presents architectures in which the signature creation credential is protected by an authorization mechanism fully managed by the signature creation service. The second clause introduces architectures leveraging OAuth 2.0-based protection of the signature creation credential, focusing on standardized authorization delegation and

interoperability. The third clause describes architectures that employ the EUDIW as a central component for user authentication, authorization, and orchestration of signature creation operations.

Together, these clauses provide a comprehensive overview of the main architectural models currently applicable to remote signature creation, supporting diverse deployment scenarios and regulatory requirements but other architectural models can be implemented achieving comparable levels of security.

Where CSC is referenced in the subsequent sub-clauses, the same considerations generally apply to OASIS DSS X."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica", "portafoglio europeo di identità digitale"],
    },
    {
        "riferimento": "clausola 6.2 (Architectures for creating remote signatures with a credential protected by signature creation service-managed authorization)",
        "testo": (
            "Descrive le architetture in cui la credenziale di firma e' protetta da un meccanismo di "
            "autorizzazione gestito dal servizio di creazione della firma, illustrandone i flussi con "
            "diagrammi di sequenza derivati principalmente da CSC API: creazione di una firma remota su "
            "hash con credenziale protetta dai meccanismi di autorizzazione del servizio; creazione di una "
            "firma remota su hash con credenziale protetta da PIN e OTP forniti tramite un canale di "
            "comunicazione concordato gestito dal servizio (SMS, app, e-mail); creazione di piu' firme "
            "remote a partire da una lista di valori di hash con credenziale protetta da PIN. La NOTE "
            "premessa avverte che l'autorizzazione esplicita richiede all'applicazione di guida di "
            "raccogliere i fattori di autenticazione (ad esempio PIN, OTP) nel proprio ambiente, con "
            "complessita' aggiuntiva nel garantire raccolta e conservazione sicure dei fattori, e che tale "
            "meccanismo non dovrebbe essere idoneo a soddisfare i requisiti SCAL2."
        ),
        "testo_integrale": (
            """Architectures for creating remote signatures with a credential protected by signature creation service-managed authorization:    NOTE:      Explicit authorization requires the driving application to collect authentication factors (e.g. PIN, OTP) within its own environment. This introduces complexity in ensuring secure factor collection and storage. This mechanism should not be suitable to satisfy SCAL2 requirements.

Creating a remote signature using a signing credential protected by a signature creation service can be implemented in some different ways and involving the usage of different authorization data. Moreover, remote signatures creation under the eIDAS [i.1] Regulation involves a well-defined rationale rooted in security, compliance, and usability.

Below some examples of sequence diagrams illustrating specific different flows between a driving application and a signature creation service in the case of remote signatures creation with a signing credential protected by signature creation service-managed authorization mainly derived from CSC API [1].

Figure 7: Remote hashes signature creation by using a signing credential whose usage is protected by authorization mechanisms managed by the signature creation service

Figure 8: Remote hashes signature creation by using a signing credential whose usage is protected by a PIN and an OTP provided through an agreed communication channel managed by the signature creation service (i.e. SMS, app, email)

       Figure 9: Multiple remote signatures creation from a list of hash values by using a signing credential whose usage is protected by PIN"""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica"],
    },
    {
        "riferimento": "clausola 6.3 (Architectures for creating remote signatures with a credential protected by OAuth2)",
        "testo": (
            "Descrive le architetture in cui la credenziale di firma e' protetta da un authorization server "
            "OAuth 2.0: l'applicazione di guida usa l'authorization server del servizio di creazione della "
            "firma remota per l'autenticazione dell'utente e per l'autorizzazione all'uso della credenziale "
            "di firma e, dopo un'autenticazione e un'autorizzazione riuscite, riceve un access token con "
            "cui autorizzare l'accesso alle risorse del servizio (le credenziali di firma degli utenti). La "
            "credenziale di firma puo' essere indicata nel parametro credentialID oppure selezionata in "
            "base al valore del parametro signatureQualifier, che specifica il tipo di firma da creare; i "
            "dati da firmare possono essere identificati come rappresentazione dei dati da firmare, come "
            "documento del firmatario o come rappresentazione del documento del firmatario (hash del "
            "documento) insieme a un'etichetta con la descrizione leggibile del documento; possono inoltre "
            "essere forniti il numero di firme da autorizzare e una lista di attributi firmati da includere "
            "nella firma. Le possibili scelte di selezione della credenziale e di indicazione dei dati da "
            "firmare sono specificate nelle clausole 8.2.2 e 8.2.3 di CSC API; i diagrammi di sequenza "
            "illustrano un flusso di authorization code tra applicazione di guida e servizio di creazione "
            "della firma, anche nella variante con richiesta di autorizzazione pushed e rich."
        ),
        "testo_integrale": (
            """Architectures for creating remote signatures with a credential protected by OAuth2: Using the OAuth 2.0 authorization scheme, the driving application will use the remote signature creation service's authorization server for user authentication and signing credential usage authorization. After a successful authentication and authorization, the authorization server of the signature creation service will provide the driving application with an access token that the driving application will use to authorize access to the signature creation service's resources (that's the users signing credentials).

There are some different ways in which requesting a remote signature creation authorization by means of an OAuth2 authorization server. In clauses 8.2.2 and 8.2.3 of CSC API [1] possible choices for selecting the signing credential and providing information about the data to be signed are specified.

The signing credential may be indicated in the credentialID parameter or selected according to the signatureQualifier parameter value that specifies the kind of signature to be created.

The data to be signed may be identified as data to be signed representation or as signer's document or signer's document representation (i.e. hash of SD) together with a label containing a human-readable description of the respective document.

Moreover, the number of signatures to authorize and a list of signed attributes to be included in the signature may be provided too.

Below some examples of sequence diagrams illustrating specific different flows between a driving application and a signature creation service in the case of remote signatures creation with a signing credential protected by an OAuth2 authorization server mainly derived from CSC API [1].

                 Figure 10: Sequence diagram illustrating an authorization code flow between a driving application requesting signatures creation to a signature creation service with a credential protected by OAuth2 authorization server

              Figure 11: Sequence diagram illustrating an authorization code flow between a driving application requesting signatures creation to a signature creation service with a credential protected by OAuth2 authorization server by a pushed and rich authorization request"""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica"],
    },
    {
        "riferimento": "clausola 6.4.2 (EUDIW as authentication and authorization layer for creating remote signatures)",
        "testo": (
            "Descrive l'architettura in cui l'EUDIW funge da livello di autenticazione e autorizzazione per "
            "la creazione di firme remote: il firmatario usa il portafoglio per autorizzare un QTSP a "
            "firmare un documento per suo conto, il QTSP e la parte affidante (RP) svolgono i ruoli "
            "centrali nella gestione del processo di creazione della firma mentre l'EUDIW e' primariamente "
            "responsabile dell'autorizzazione alla creazione; il componente di interazione con il "
            "firmatario (SIC) e' rappresentato in due parti distinte (livello di interazione utente basato "
            "su browser e livello di esecuzione fidato residente nell'EUDIW); l'applicazione di guida opera "
            "nell'ambiente della RP e interagisce con l'authorization server tramite lo user agent, "
            "richiedendo la creazione di firme AdES al QTSP che integra la SCA, ad esempio invocando l'API "
            "CSC signDoc. Sono elencate le varianti realizzabili (user agent ed EUDIW sullo stesso "
            "dispositivo; SCA presso una parte indipendente, un intermediario o la RP; applicazione di "
            "guida presso una parte indipendente; authorization server presso il QTSP che eroga la SSA) con "
            "le relative figure, e i passi chiave del flusso: trasmissione del documento o del suo hash "
            "all'authorization server, autorizzazione della firma da parte dell'utente tramite l'EUDIW "
            "(autenticazione e consenso), richiesta di creazione della firma al QTSP, creazione con "
            "dispositivo qualificato di creazione della firma e restituzione del documento o dei dati "
            "firmati. L'authorization server puo' trasmettere una richiesta OpenID4VP al componente SIC "
            "dell'EUDIW con lo schema URL personalizzato openid4vp:// o tramite i metodi Digital "
            "Credentials API, e ulteriori meccanismi di consegna possono essere supportati se implementati "
            "dal SIC; l'autenticazione del servizio e il recupero delle informazioni sulla credenziale di "
            "firma possono essere omessi se l'applicazione di guida conosce in anticipo la credenziale "
            "dell'utente; il contenuto dell'oggetto della richiesta passato all'EUDIW e della relativa "
            "risposta sono specificati nella clausola 7 di CSC data model bindings; l'identificatore del "
            "tipo di dati di transazione per approvare la creazione di firme o sigilli elettronici "
            "qualificati e' \"https://cloudsignatureconsortium.org/2025/qes-approval\"; la creazione delle "
            "firme remote puo' essere eseguita invocando gli endpoint SSA CSC signatures/signHash o "
            "signatures/signDoc."
        ),
        "testo_integrale": (
            """EUDIW as authentication and authorization layer for creating remote signatures: In this architecture, as outlined in Figure 12, the signer uses the EUDIW to authorize a QTSP to sign a document on his/her behalf, the QTSP and the RP play the central roles in managing the signature creation process, while the EUDIW is primarily responsible for authorizing the signature creation. The Signer Interaction Component (SIC) is represented in two distinct parts, SIC Part 1 and SIC Part 2, to reflect the separation of responsibilities between the browser-based user interaction layer and the EUDIW-resident trusted execution layer. This split aligns with the functional decomposition defined in the EUDIW reference architectures, where different parts of the signature orchestration process may be executed in different security domains. The driving application runs in the RP environment and interacts with the authorization server via the user agent. The driving application requests AdES signatures creation to the QTSP which is integrating the SCA, i.e. by invoking CSC signDoc API.

                           Figure 12: Architecture with SCA at QTSP and DA at RP

Different variations of the above architecture may be implemented according to the following alternatives:

   •     The user agent and the EUDIW may be in the same user device.

   •     The SCA may be implemented by an independent party or intermediary or by the RP that will operate both the driving application and the SCA.

   •     The driving application may be implemented by an independent party.

   •     The authorization server may be implemented by the QTSP operating the SSA.

Figure 13 shows an architecture in which the user agent and the EUDIW are in the same user device and the SCA and the driving application are implemented by different independent parties.

Figure 14 shows a slightly different architecture in which the user agent and the EUDIW are in different user devices and the SCA and the driving application are implemented by different independent parties.

Figure 15 shows an architecture in which the user agent and the EUDIW are in different user devices, the driving application is implemented at RP and the SCA is implemented by an independent party.

Figure 16 shows an architecture in which the user agent and the EUDIW are in different user devices, the driving application and the SCA are implemented at RP.

Figure 17 shows an architecture in which the user agent and the EUDIW are in different user devices, the SCA and the driving application are implemented by different independent parties, and the authorization server is implemented by the QTSP operating the SSA.

     Figure 13: Architecture with SCA and DA at different parties and with EUDIW and user agent in the same user device

Figure 14: Architecture with SCA and DA at different parties

Figure 15: Architecture with DA at RP and SCA at independent party

Figure 16: Architecture with DA and SCA at RP

 Figure 17: Architecture with authorization server at QTSP and with SCA and DA at different parties

In the above scenarios, the Authorization Server may transmit an OpenID4VP request to the EUDIW SIC component using the openid4vp:// custom URL scheme, as specified in Section 12.1.2 of OpenID for Verifiable Presentations 1.0 [22], or via Digital Credentials API methods [23]. Additional delivery mechanisms may be supported if implemented by the EUDIW SIC component. The EUDIW processes the OpenID4VP request for example using PID presentation or transaction approval. The driving application can run in the local environment of the signer or in the environment of a relying party or in the environment of an independent intermediary. The driving application may request AdES signatures or digital signature values creation to the QTSP, i.e. by invoking CSC API [1].

Key Steps:

   •     Document or Hash Transmission. The driving application (it can be managed by a relying party, e.g. a bank, government agency, or business) sends the document or its hash to the authorization server requesting signatures creation authorization.

   •     Signature Authorization. The EUDIW is used by the user (signer) to authorize the signature operation. This typically involves user authentication and consent via the EUDIW.

   •     Signature creation request. The driving application requests AdES signatures or digital signature values creation to the QTSP.

   •     Signature Creation. If authorized, the QTSP uses a Qualified Signature Creation Device (QSCD) to generate the Qualified Electronic Signature (QES).

   •     Return of Signed Document or Signed Data. The signed document or signature is returned to the driving application.

Below a sequence diagram illustrating a generic signatures creation flow in an architecture where EUDIW serves as the authentication and authorization layer.

The driving application can be hosted at a relying party, at a TSP, or even an intermediary.

The signature creation application can be implemented at the driving application or at the signature creation service.

        Figure 18: Generic simplified flow with EUDIW as authentication and authorization layer

Below another example of sequence diagrams illustrating a different flow in an architecture where EUDIW serves as the authentication and authorization layer.

The driving application can be hosted at a relying party, at a TSP, or even an intermediary.

The signature creation application can be implemented at the driving application or at the signature creation service.

     Figure 19: Remote signature creation with OAuth2 Authorization Code flow and Pushed and Rich Authorization Request with EUDIW as authentication and authorization layer

Service authentication and retrieval of the signing credential information may be omitted if the driving application knows in advance the user signing credential. The content of the request object passed to the EUDIW and of its response are specified in clause 7 of CSC data model bindings [3]. The transaction data type identifier for approving Qualified Electronic Signatures or seals (QES) creation is: "https://cloudsignatureconsortium.org/2025/qes-approval". The remote signatures creation may be performed by invoking the SSA CSC signatures/signHash or signatures/signDoc endpoints."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["portafoglio europeo di identità digitale", "firma elettronica qualificata"],
    },
    {
        "riferimento": "clausola 6.4.4.1 (Introduction)",
        "testo": (
            "Clausola di ambito: definisce i requisiti per un EUDIW che, in qualita' di client OAuth 2.0, "
            "si registra e si autentica presso un authorization server usando l'OpenID Foundation FAPI 2.0 "
            "Security Profile, con integrazione esplicita della chiave pubblica della Wallet Unit "
            "Attestation nella registrazione dinamica del client."
        ),
        "testo_integrale": (
            """Introduction: This clause defines the requirements for an EUDIW acting as an OAuth 2.0 client to register and authenticate to an authorization server using the OpenID Foundation FAPI 2.0 Security Profile [10], with explicit integration of Wallet Unit Attestation public key during dynamic client registration."""
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": ["portafoglio europeo di identità digitale"],
    },
    {
        "riferimento": "clausola 6.4.4.5.1 (Dynamic Client Registration request payload (JSON))",
        "testo": (
            "Blocco di esempio (illustrativo, privo di valore prescrittivo): payload JSON di una richiesta "
            "di Dynamic Client Registration (POST /oauth/register) con i metadati del client del "
            "portafoglio (client_name, application_type, redirect_uris, grant_types, response_types, "
            "token_endpoint_auth_method, token_endpoint_auth_signing_alg, jwks con chiave EC P-256, "
            "tls_client_certificate_bound_access_tokens, require_pushed_authorization_requests, "
            "request_object_signing_alg, authorization_details_types, software_statement e scope)."
        ),
        "testo_integrale": (
            """Dynamic Client Registration request payload (JSON)
POST /oauth/register HTTP/1.1
Host: as.example.eu
Content-Type: application/json

{
    "client_name": "European Digital Identity Wallet (MemberState-X)",
    "application_type": "native",
    "redirect_uris": [
      "eudiwallet://cb",
      "https://wallet.example.ms/callback"
    ],
    "grant_types": ["authorization_code"],
    "response_types": ["code"],
    "token_endpoint_auth_method": "private_key_jwt",
    "token_endpoint_auth_signing_alg": "ES256",
    "jwks": {
      "keys": [
        {
          "kty": "EC",
          "crv": "P-256",
          "use": "sig",
          "alg": "ES256",
          "kid": "wua-key-2026-01",
          "x": "TCAER19Zvu3OHF4j4W4vfSVoHIP1ILilDls7vCeGemc",
          "y": "ZxjiWWbZMQGHVWKVQ4hbSIirsVfuecCE6t4jT9F2HZQ"
        }
      ]
    }
    "tls_client_certificate_bound_access_tokens": true,
    "require_pushed_authorization_requests": true,
    "request_object_signing_alg": "ES256",
    "authorization_details_types": ["openid_credential_issuance"],
    "software_statement": "<signed-JWT>",
    "scope": "openid profile"
}"""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["portafoglio europeo di identità digitale"],
    },
    {
        "riferimento": "clausola 6.4.4.5.2 (Authorization server response)",
        "testo": (
            "Blocco di esempio (illustrativo, privo di valore prescrittivo): risposta HTTP 201 Created di "
            "un authorization server a una richiesta di registrazione dinamica, con client_id, "
            "client_id_issued_at, registration_access_token, registration_client_uri, i metadati registrati "
            "del portafoglio e il software statement."
        ),
        "testo_integrale": (
            """Authorization server response
HTTP/1.1 201 Created
Content-Type: application/json
Cache-Control: no-store

{

    "client_id": "client-9f7e2",
    "client_id_issued_at": 1736940201,
    "registration_access_token": "eyJraWQiOiJtZy0yMDI2LTAxIn0.eyJzY29wZSI6...",
    "registration_client_uri": "https://as.example.eu/oauth/register/client-9f7e2",
    "client_name": "European Digital Identity Wallet (MemberState-X)",
    "application_type": "native",
    "redirect_uris": ["eudiwallet://cb"],
    "grant_types": ["authorization_code"],
    "response_types": ["code"],
    "token_endpoint_auth_method": "private_key_jwt",
    "token_endpoint_auth_signing_alg": "ES256",
    "jwks": {
      "keys": [
        {
          "kty": "EC",
          "crv": "P-256",
          "use": "sig",
          "alg": "ES256",
          "kid": "wua-key-2026-01",
          "x": "TCAER19Zvu3OHF4j4W4vfSVoHIP1ILilDls7vCeGemc",
          "y": "ZxjiWWbZMQGHVWKVQ4hbSIirsVfuecCE6t4jT9F2HZQ"
        }
      ]
    },
    "request_object_signing_alg": "ES256",
    "require_pushed_authorization_requests": true,
    "tls_client_certificate_bound_access_tokens": true,
    "software_statement": "<signed-JWT>",
    "scope": "openid profile"
}"""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["portafoglio europeo di identità digitale"],
    },
    {
        "riferimento": "clausola 6.4.4.5.3 (EUDIW authorization request payload (JSON))",
        "testo": (
            "Blocco di esempio (illustrativo, privo di valore prescrittivo): richiesta di autorizzazione "
            "pushed (PAR) inviata dall'EUDIW con JAR firmato (JWS), preceduta dall'elenco dei requisiti "
            "FAPI 2.0 (PAR per tutte le richieste di autorizzazione, JAR come request object, "
            "response_type=code, PKCE S256, token sender constrained DPoP o mTLS, request object firmato "
            "contenente tutti i parametri) e seguita dalle note su protezione dell'integrita' dei "
            "parametri, autenticazione del client al PAR con private_key_jwt o DPoP e uso della chiave "
            "attestata dalla WUA (kid)."
        ),
        "testo_integrale": (
            """EUDIW authorization request payload (JSON)
FAPI 2.0 requires:

    •    PAR (Pushed Authorization Request) for all authorization requests

• JAR (JWT Secured Authorization Request) as the request object

    •    response_type=code (only)

    •    PKCE (S256)

• sender constrained tokens (DPoP or mTLS)

    •    Signed request object containing all parameters (AS ignores URL parameters except client_id).

FAPI also mandates use of request object signing and PAR.

EUDIW sends a pushed authorization request with a signed JAR (JWS).

POST /par HTTP/1.1
Host: as.example.eu
Content-Type: application/x-www-form-urlencoded
Authorization: DPoP eyJhbGciOiJFUzI1NiIsInR5cCI6ImRwb3A...
DPoP: eyJhbGciOiJFUzI1NiIsInR5cCI6ImRwb3AifQ...

client_id=client-12345&
request=eyJhbGciOiJQUzI1NiIsImtpZCI6Ind1YS1rZXktMjAyNi0wMSIsInR5cCI6Im9hdXRoLXJlcXVlc3Qrand0In0.
eyJpc3MiOiJjbGllbnQtMTIzNDUiLCJhdWQiOiJodHRwczovL2FzLmV4YW1wbGUuZXUiLCJyZXNwb25zZV90eX
BlIjoiY29kZSIsImNsaWVudF9pZCI6ImNsaWVudC0xMjM0NSIsInJlZGlyZWN0X3VyaSI6ImV1ZGl3YWxsZXQ6L
y9jYiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUiLCJzdGF0ZSI6ImFmMGlmanNsZGtqIiwibm9uY2UiOiJuLTBTNl9Xek
EyTWoiLCJjb2RlX2NoYWxsZW5nZSI6InM0UW1ab2R3SmFZRmpUZlZLbHBjRUYiLCJjb2RlX2NoYWxsZW5nZ
V9tZXRob2QiOiJTNTYiLCJleHAiOjE3MzY5NDAxMDAsIm5iZiI6MTczNjkzOTQwMH0.VERY-LONG-
SIGNATURE...

The request parameter contains a signed JAR (JSON Web Signature) as specified in IETF RFC 9101 [31].

FAPI 2.0 requires PAR so that all request parameters are integrity protected.

Client authentication at PAR will use private_key_jwt or DPoP.

JWS header uses the WUA attested key (kid)."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["portafoglio europeo di identità digitale"],
    },
    {
        "riferimento": "clausola 6.4.4.5.4 (PAR Response (from AS to EUDIW))",
        "testo": (
            "Blocco di esempio (illustrativo, privo di valore prescrittivo): risposta PAR "
            "dell'authorization server all'EUDIW con request_uri (utilizzabile una sola volta) e "
            "expires_in; l'authorization server ignora tutti i parametri della richiesta di autorizzazione "
            "tranne client_id e request_uri."
        ),
        "testo_integrale": (
            """PAR Response (from AS to EUDIW)
HTTP/1.1 201 Created
Content-Type: application/json
Cache-Control: no-store
{
    "request_uri": "urn:as:par:cx298dhasd98hasd9",
    "expires_in": 90
}

request_uri can only be used once, an authorization server ignores all authorization request parameters except client_id
and request_uri."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["portafoglio europeo di identità digitale"],
    },
    {
        "riferimento": "clausola 6.4.4.5.5 (Authorization Request (from EUDIW to authorization endpoint))",
        "testo": (
            "Blocco di esempio (illustrativo, privo di valore prescrittivo): richiesta di autorizzazione "
            "inviata dall'EUDIW all'authorization endpoint contenente soltanto client_id e request_uri, "
            "poiche' tutti i parametri di sicurezza risiedono nel JAR firmato precedentemente inviato via "
            "PAR."
        ),
        "testo_integrale": (
            """Authorization Request (from EUDIW to authorization endpoint)
GET /authorize?
 client_id=client-12345&
 request_uri=urn:as:par:cx298dhasd98hasd9
HTTP/1.1
Host: as.example.eu

This request contains almost nothing except client_id and request_uri. All security parameters are inside the signed JAR
that was previously pushed via PAR. request URI points to the previously registered JAR as stated in FAPI."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["portafoglio europeo di identità digitale"],
    },
    {
        "riferimento": "clausola 6.4.4.5.6 (Authorization server redirects back with authorization code)",
        "testo": (
            "Blocco di esempio (illustrativo, privo di valore prescrittivo): reindirizzamento "
            "dell'authorization server con il codice di autorizzazione (HTTP 302 Found su eudiwallet://cb) "
            "dopo autenticazione e consenso riusciti dell'utente; lo state e' restituito esattamente come "
            "fornito dal client, il codice e' vincolato al client tramite emissione di token "
            "sender-constrained con DPoP e il response mode e' quello predefinito (query) poiche' "
            "response_type=code."
        ),
        "testo_integrale": (
            """Authorization server redirects back with authorization code
If the user authenticates successfully and consents, the authorization server redirects:

HTTP/1.1 302 Found
Location: eudiwallet://cb?
 code=SplxlOBeZQQYbYS6WxSbIA&
 state=af0ifjsldkj

state is returned exactly as provided by the client, code is bound to the client through sender constrained token issuance
with DPoP. Response mode is the default (query mode) because response_type=code only."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["portafoglio europeo di identità digitale"],
    },
    {
        "riferimento": "clausola 6.4.5.1 (Introduction)",
        "testo": (
            "Clausola di ambito: definisce i requisiti per una DA o una SCA che, in qualita' di client "
            "OAuth 2.0, si registra e si autentica presso un authorization server; nelle clausole seguenti "
            "il termine generico \"client\" designa la DA o la SCA."
        ),
        "testo_integrale": (
            """Introduction: This clause defines the requirements for a DA or a SCA acting as an OAuth 2.0 client to register and authenticate to an authorization server. In the following clauses the generic term "client" will be used to refer to DA or SCA."""
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 6.1 (Introduction)",
    "clausola 6.2 (Architectures for creating remote signatures with a credential protected by signature creation service-managed authorization)",
    "clausola 6.3 (Architectures for creating remote signatures with a credential protected by OAuth2)",
    "clausola 6.4.1 (Overview)",
    "clausola 6.4.2 (EUDIW as authentication and authorization layer for creating remote signatures)",
    "clausola 6.4.3 (EUDIW participating in the signature creation process)",
    "clausola 6.4.4.1 (Introduction)",
    "clausola 6.4.4.2 (EUDIW registration)",
    "clausola 6.4.4.3 (EUDIW authentication)",
    "clausola 6.4.4.4 (Security requirements)",
    "clausola 6.4.4.5.1 (Dynamic Client Registration request payload (JSON))",
    "clausola 6.4.4.5.2 (Authorization server response)",
    "clausola 6.4.4.5.3 (EUDIW authorization request payload (JSON))",
    "clausola 6.4.4.5.4 (PAR Response (from AS to EUDIW))",
    "clausola 6.4.4.5.5 (Authorization Request (from EUDIW to authorization endpoint))",
    "clausola 6.4.4.5.6 (Authorization server redirects back with authorization code)",
    "clausola 6.4.5.1 (Introduction)",
    "clausola 6.4.5.2 (client registration)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        # 6.4.3: "In annex A, a profile designing such a request-response
        # protocol is defined." - unica citazione letterale interna alla Fonte
        # in questo capitolo. Ancorata alla prima sottoclasola numerata
        # dell'annesso (cap06), perche' l'intestazione dell'annesso e' pura
        # intestazione di raggruppamento e non genera nodo.
        "nodo_da": ("obbligo", None, "clausola 6.4.3 (EUDIW participating in the signature creation process)"),
        "nodo_a": ("principio", None, "Annex A.1 (Overview)"),
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
