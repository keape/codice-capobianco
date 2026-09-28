"""ETSI TS 119 432 V1.3.1 (2026-03) - Electronic Signatures and Trust
Infrastructures (ESI); Protocols for remote digital signature creation.
Fonte 20 (documento unico, non multi-parte: i `riferimento` NON portano alcun
prefisso di Parte, a differenza di ETSI EN 319 412/411 e di ETSI TS 119 431;
la numerazione degli id e' risolta per riferimento dalla sessione principale
in app/seed.py - questo modulo NON tocca seed.py). Capitolo 2: clausola 4
(Signature creation process, service decomposition: 4.1, 4.2, 4.3 con
4.3.1-4.3.4, 4.4.1 con 4.4.1.1-4.4.1.3) e clausole 5.1 (Introduction) e 5.2
(Service authorization: 5.2.1 Overview, 5.2.2 HTTP Basic Authentication and
HTTP Digest Authentication, 5.2.3 OAuth 2.0, 5.2.4 Other authentication
mechanisms). Le clausole 5.3-5.5 sono coperte da cap03 e non compaiono qui.
Testo ufficiale in app/.source_cache/etsi_119_432/cap02.txt (letto sempre con
selettore `:raw`, altrimenti il tool tronca le righe lunghe a 768 caratteri
introducendo "..." e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_119_432/manifest.json.

Modellazione (ADR-0007, nessun discrimine di rilevanza), stesso criterio gia'
applicato alle altre fonti ETSI gia' censite (EN 319 401, EN 319 412, EN 319
421, EN 319 422, TS 119 431, TS 119 461) e adattato alla struttura di uno
standard tecnico di protocollo: un nodo per ogni clausola/sottoclavola
numerata che porta contenuto proprio. Il capitolo copre 14 clausole numerate
con contenuto proprio -> 14 nodi: 4 Obblighi e 10 Principi. Scelte voce per
voce:

- Clausola 4.1 (Signature creation process steps and data elements) -> 1
  Principio "altro". Descrive (con rinvio alla Figure 1, derivata da ETSI EN
  319 102-1) i passi del processo di creazione della firma e i relativi data
  element, la loro ripartizione tra piu' componenti nella creazione remota e
  i limiti espliciti dell'illustrazione (non specifica soluzioni per
  autenticazione del firmatario, autorizzazione all'uso della chiave,
  disponibilita' del certificato). Nessun verbo prescrittivo ("shall"/
  "should") e nessun soggetto obbligato: e' descrizione di processo/
  architettura, non prescrizione. Non e' "scopo/ambito di applicazione"
  (quello e' la clausola 1 del documento, in cap01) ne' "definitorio" (non
  introduce termini con valenza definitoria propria). La didascalia "Figure
  1: Process Steps and Data Elements in Signature Creation" e' inclusa in
  `testo_integrale` per completezza verbatim (stessa convenzione gia' usata
  in etsi_119_431_2/cap01.py per le didascalie delle figure).
- Clausola 4.2 (Service main components and interfaces) -> 1 Principio
  "definitorio". Non contiene alcun "shall": enuncia lo scenario (chiave di
  firma in un SCDev gestito da un SCSP), individua e DEFINISCE i due
  componenti principali con interfacce distinte - Server Signing Application
  Service Component (SSASC), che supporta la creazione del valore di firma
  digitale, e Signature Creation Application Service Component (SCASC), che
  supporta la creazione della firma AdES - con input/output principali di
  ciascuna interfaccia, e DEFINISCE l'acronimo SCS ("a TSP service
  implementing a Signature Creation Application (SCA) and/or a Server
  Signing Application (SSA)"). E' quindi la clausola che fissa il significato
  dei termini/componenti usati in tutto il documento: "definitorio" (stesso
  trattamento riservato alla clausola 4.3 Architecture di ETSI TS 119 431-2
  in cap01 di quella fonte). Le varianti possibili delle interfacce e il
  rinvio alle clausole seguenti ("The following clauses specify main
  information objects and processes in SCASC and SSASC") sono parte della
  stessa clausola indivisibile.
- Clausola 4.3.1 (Signer's document and hashing) -> 1 Principio "altro".
  Descrive l'avvio del processo (SD -> SDR -> DTBS) e due osservazioni
  introdotte dalla formula "The following observations are made", piu' una
  considerazione di design ("An important design decision ..."). Il verbo
  "can be done" esprime possibilita' operativa, non prescrizione: nessun
  "shall", nessun soggetto obbligato.
- Clausola 4.3.2 (DTBS composition and formatting) -> 1 Principio "altro".
  Descrizione tecnica della composizione/formattazione del DTBSF. "further
  signed attributes are required or allowed by the ETSI standard signature
  formats" e' una constatazione su cio' che gli altri standard ETSI
  richiedono/ammettono, non un requisito posto da questo documento; "are
  available to the SCASC when the DTBSF is created by the SCASC" e'
  dichiarativo. Nessun "shall".
- Clausola 4.3.3 (DTBS preparation) -> 1 Principio "altro". Il presente
  indicativo ("The SCASC prepares the entire DTBSF, calculates the hash, and
  sends the hash value (DTBSR) as input to an SSASC") descrive il passo, non
  impone un obbligo con "shall": descrizione di flusso -> Principio.
- Clausola 4.3.4 (SDO composer) -> 1 Principio "altro". Descrive il passo
  finale di costruzione dell'SDO e le tre denominazioni della firma
  (Enveloped/Enveloping/Detached) in un elenco esemplificativo; chiude con
  "The SDO composing is done by a separate service instance or integrated
  with other functions in the SCASC", che ammette due alternative
  architetturali senza imporne alcuna.
- Clausola 4.4.1.1 (Introduction) -> 1 Principio "altro". Dichiara lo scopo
  del processo (prendere il DTBSR e creare un valore di firma sotto il
  controllo del firmatario) e come esso e' gestito nel contesto del
  documento (SSASC + chiave in SCDev, attivazione con processo sicuro di
  autorizzazione/attivazione, ossia il protocollo di EN 419 241-1).
  Descrittiva.
- Clausola 4.4.1.2 (Signature activation) -> 1 Principio "altro". Descrive
  l'uso dello SCDev remoto, il ruolo del Signature Activation Module (SAM) e
  dei Signature Activation Data (SAD) per il controllo esclusivo, e i due
  livelli di confidenza SCAL1/SCAL2 con le rispettive caratteristiche. Le
  sotto-voci di SCAL1/SCAL2 sono descrizioni di livello di garanzia, non
  requisiti posti da questo documento (i livelli sono definiti in ETSI EN 419
  241-1). La NOTE su SCAL1 ("It is not expected that such implementations
  would meet the requirements of sole control as it would be expected for a
  stand-alone QSCD as defined in the eIDAS [i.1] Regulation") e' inclusa
  verbatim in `testo_integrale` (ADR-0010: nessuna omissione di NOTE) e non
  cambia la classificazione: e' un'aspettativa/avvertenza dichiarativa priva
  di soggetto obbligato e di "shall".
- Clausola 4.4.1.3 (Signature creation by SCDev) -> 1 Principio "altro".
  Descrive chi esegue la creazione (lo SCDev) e restringe il perimetro alle
  architetture con SCDev remoto; "the signing key can be used to generate the
  digital signature value creation after a successful signer authentication
  by the SSASC (SCAL1) or after a successful SAD verification by the SAM" e'
  descrittiva delle due modalita' corrispondenti ai livelli di garanzia.
  Nessun "shall".
- Clausola 5.1 (Introduction) -> 1 OBBLIGO, tipo_obbligo "tecnico/sicurezza",
  soggetto "Terza parte" obbligato. Classificazione ambigua risolta in favore
  di Obbligo: la clausola e' intitolata "Introduction" e contiene anche
  affermazioni dichiarative (raccomandazione generale di proteggere i servizi
  da accessi non autorizzati; necessita' di un'autorizzazione dell'utente;
  possibilita' per l'utente di autorizzare una o piu' firme; ruolo di client
  della driving application), MA contiene un "shall" esplicito con soggetto
  identificabile - "Any driving application shall be authenticated when
  invoking a signature creation service" - che e' il criterio decisivo di
  ADR-0007 per il nodo Obbligo. La clausola e' indivisibile (nessuna
  numerazione propria delle frasi) e viene quindi accorpata in un unico nodo
  Obbligo, con il resto del testo nella sintesi e in `testo_integrale`. Il
  soggetto e' la driving application (applicazione richiedente terza, non il
  QTSP ne' l'utente) -> categoria "Terza parte" con ruolo "obbligato", stessa
  convenzione gia' adottata per i soggetti obbligati non-QTSP in
  etsi_119_461/cap06.py, agid_reg_tec_cert_qual/cap03.py e
  reg_ue_2025_1566/cap01.py. tipo_obbligo "tecnico/sicurezza" perche' il
  contenuto del requisito e' l'autenticazione all'invocazione del servizio.
- Clausola 5.2.1 (Overview) -> 1 OBBLIGO, tipo_obbligo "tecnico/sicurezza",
  soggetto "Terza parte" obbligato. "the driving application shall adopt any
  of those available from the signature creation service" e' un "shall" con
  soggetto esplicito (driving application) e oggetto determinato (adozione di
  uno dei meccanismi di autorizzazione resi disponibili dal servizio). La
  prima parte ("Various types of authorization mechanisms may be supported")
  e' dichiarativa e resta assorbita nello stesso nodo (clausola indivisibile).
- Clausola 5.2.2 (HTTP Basic Authentication and HTTP Digest Authentication)
  -> 1 OBBLIGO, tipo_obbligo "tecnico/sicurezza", soggetti: "QTSP/gestore"
  obbligato + "Terza parte" destinatario. La clausola contiene i "shall" che
  impongono al servizio di creazione di firma l'adozione delle API e la
  struttura dei messaggi ("The auth/login API identified in CSC API [1],
  clause 11.2 shall apply"; "The message for requesting the access token for
  service authorization shall contain the components defined in CSC API [1],
  clause 11.2 section Input"; e gli analoghi per Output, per auth/revoke e per
  il messaggio di invalidazione): il soggetto obbligato e' il prestatore del
  servizio (QTSP/gestore). La NOTE iniziale e' una raccomandazione negativa
  rivolta all'utilizzatore ("HTTP Basic Authentication [i.10] is an unsafe
  mechanism, and therefore it should not be used, especially by driving
  application running as a service ... HTTP Basic Authentication should not
  be employed in processes implementing qualified electronic signature or
  seal creation"): essendo la clausola indivisibile non genera un nodo
  separato, ma il suo destinatario e' registrato come "Terza parte" con ruolo
  "destinatario" per non perdere l'informazione. La parte descrittiva (quadro
  challenge-response di HTTP, flusso di richiesta/risposta, confronto con
  HTTP Digest, didascalia della Figure 2) e' inclusa verbatim nello stesso
  nodo. Nota di perimetro: i rinvii "clause 15.5.2/15.5.8/15.3.5 of IETF RFC
  9110 [16]" e "CSC API [1], clause 11.2/11.3" sono a documenti ESTERNI, non
  generano relazioni interne.
- Clausola 5.2.3 (OAuth 2.0) -> 1 OBBLIGO, tipo_obbligo "tecnico/sicurezza",
  soggetto "QTSP/gestore" obbligato. La clausola contiene il "shall" tecnico
  "It shall be ensured that the JWT is signed with strong algorithms and that
  remote signature creation services trust the issuer's public key securely"
  (il soggetto che deve assicurarlo e' il prestatore/gestore del servizio di
  creazione di firma, nonche' il servizio che deve fidarsi dell'issuer) e i
  "shall" di conformita' alle API e ai messaggi ("The oauth2/authorize API
  identified in CSC API [1], clause 8.2.2 shall apply" e gli analoghi per
  oauth2/pushed_authorize (clause 8.2.3), oauth2/token (clause 8.2.4),
  oauth2/revoke (clause 8.2.5), piu' i relativi "The message ... shall
  contain the components ..."). La numerazione interna "Main steps: 1) Client
  Registration, 2) Authorization Flow, 3) Token Issuance, 4) API Access" NON
  e' una numerazione di clausole/sottoclausole (non esiste 5.2.3.1): e' un
  elenco di passi dentro la clausola indivisibile, quindi non genera item di
  indice ne' nodi separati, ed e' riprodotto verbatim nel `testo_integrale`
  del nodo 5.2.3. Lo stesso vale per la NOTE su pushed_authorize (IETF RFC
  9126 [18]) e per la didascalia della Figure 3. In questo capitolo non
  esiste alcun blocco "EXAMPLE" (verificato sul testo: 0 occorrenze) e nessun
  marcatore di ellissi (0 occorrenze di "..."), quindi non ci sono nodi
  Principio "altro" da payload illustrativi.
- Clausola 5.2.4 (Other authentication mechanisms) -> 1 Principio "altro".
  Elenca in modo esemplificativo le alternative di autenticazione dei client
  (mTLS con certificati client, HMAC-Signed Requests, Signed JWT Assertions,
  SAML 2.0 Assertions bearer/Holder-of-Key, SSH mutual authentication via
  reverse tunnel, challenge-response con chiave qualificata del client,
  FIDO2/Passkey) introdotte da "The following alternatives can be
  considered", e chiude dichiarando che l'elenco non e' esaustivo ("The above
  list is not exhaustive, further different solutions can be operational
  too"). "may ensure" e "can be considered" esprimono possibilita', non
  autorizzazione vincolata: nessun "shall", nessun soggetto obbligato ->
  elenco illustrativo di flussi, Principio "altro".

Esclusioni (nessun nodo, nessun item di indice), verificate caso per caso sul
testo ufficiale:
- Clausola 4 (Signature creation process, service decomposition), clausola 4.3
  (Signature Creation Application), clausola 4.4 (Server Signing Application),
  clausola 4.4.1 (Signature creation), clausola 5 (Authentication and
  authorization), clausola 5.2 (Service authorization): intestazioni di puro
  raggruppamento, prive di qualunque periodo proprio nel testo ufficiale (la
  sottoclavola numerata segue immediatamente l'intestazione). Non generano
  nodo ne' item di indice, coerentemente con la convenzione del batch.
- Clausole 5.3/5.4/5.5 (Signatures creation authorization, Credential creation
  authorization, Credential deletion authorization): fuori dal perimetro di
  questo capitolo (coperte da cap03).
- Front matter e paratesto non numerato (IPR, Foreword, Modal verbs
  terminology, Executive summary, Introduction, clausola 2 References, Annex
  D informative, History): fuori perimetro per istruzione del batch; non
  compaiono in cap02.txt.

Relazioni: RELAZIONI = [] (nessuna citazione letterale interna). Tutte le
citazioni letterali presenti nel capitolo puntano a documenti ESTERNI alla
Fonte 20 e quindi non generano relazioni in questa fase (le relazioni
cross-fonte sono demandate alla Fase 6 della sessione principale, ADR-0009):
"EN 419 241-1 [6]" (4.1, 4.4.1.1, 4.4.1.2), "ETSI EN 319 102-1 [i.12], clause
4.2.1" (4.1), "eIDAS [i.1]" (4.4.1.2), "IETF RFC 9110 [16], clause
15.5.2/15.5.8/15.3.5" (5.2.2), "CSC API [1], clause 11.2/11.3" (5.2.2), "IETF
RFC 6749 [17], Section 4.1" e "CSC API [1], clause 8.2.2/8.2.3/8.2.4/8.2.5"
(5.2.3), "IETF RFC 9126 [18], clause 2.2" (5.2.3), "[27]/[28]/[29]/[30]/[20]/
[17]" (5.2.4). Anche il rinvio di 4.4.1.3 ("According to the above sole
control assurance levels ...") e' stato escluso: e' un riferimento deittico
al contenuto di 4.4.1.2, non una citazione letterale di una clausola (che il
criterio del batch richiede), quindi non e' modellato come relazione
"richiama".
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 5.1 (Introduction)",
        "testo": (
            "Il documento raccomanda di proteggere i servizi di creazione di firma remota dagli accessi non "
            "autorizzati: ogni driving application DEVE essere autenticata quando invoca un servizio di "
            "creazione di firma. Per creare firme e' richiesta un'autorizzazione dell'utente che possiede e "
            "controlla la chiave di firma; l'utente puo' autorizzare la creazione di una o piu' firme con un "
            "certificato di firma di un certo tipo, eventualmente usando chiavi e certificati a breve termine "
            "creati al volo. La driving application, responsabile di richiedere la creazione della firma, nei "
            "flussi di autenticazione e autorizzazione descritti nelle clausole seguenti assume anche il ruolo "
            "di client, implementando le necessarie procedure di autenticazione e autorizzazione del client."
        ),
        "testo_integrale": (
            "5.1 Introduction: The present document recommends protecting remote signature creation services "
            "from unauthorized access. Any driving application shall be authenticated when invoking a "
            "signature creation service. In order to create signatures an authorization from the user who "
            "owns and controls the signing key is required. The user may authorize the creation of one or "
            "more signatures with a signing certificate of a certain type possibly using short-lived signing "
            "keys and certificates to be created on-the-fly. The driving application, responsible for "
            "requesting signature creation, in the authentication and authorization flows described in the "
            "following clauses assumes also the client role implementing the necessary client authentication "
            "and authorization procedures."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.2.1 (Overview)",
        "testo": (
            "Possono essere supportati vari tipi di meccanismi di autorizzazione; la driving application DEVE "
            "adottare uno qualunque di quelli resi disponibili dal servizio di creazione di firma."
        ),
        "testo_integrale": (
            "5.2.1 Overview: Various types of authorization mechanisms may be supported, and the driving "
            "application shall adopt any of those available from the signature creation service."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.2.2 (HTTP Basic Authentication and HTTP Digest Authentication)",
        "testo": (
            "NOTE: l'autenticazione HTTP Basic e' un meccanismo insicuro e non dovrebbe essere usata, "
            "specialmente da driving application che girano come servizio; va usata solo con un alto grado di "
            "fiducia tra utente e driving application e quando non siano disponibili altri tipi di "
            "autorizzazione, potendo essere deprecata in future release del documento, e non deve essere "
            "impiegata in processi che implementano la creazione di firma o sigillo elettronico qualificato "
            "perche' non raggiunge il livello di garanzia di sicurezza richiesto. HTTP definisce un quadro "
            "generale di autenticazione challenge-response: a una richiesta a una risorsa protetta il server "
            "risponde con lo stato 401 \"Unauthorized\" e un header WWW-Authenticate con una o piu' "
            "challenge, e il client ripete la richiesta con le credenziali nell'header Authorization (le "
            "varianti proxy usano lo stato 407 \"Proxy Authentication Required\"). La driving application "
            "puo' ottenere un access token per l'autorizzazione al servizio direttamente dal servizio di "
            "creazione di firma usando HTTP Basic Authentication, con fattori di autenticazione (es. utente e "
            "password) assegnati al firmatario passati nell'header HTTP come authorization grant; poiche' "
            "Base64 e' una codifica e non una cifratura, TLS (HTTPS) dovrebbe essere usato per proteggere le "
            "credenziali in transito. Il flusso challenge-response: il servizio risponde alla driving "
            "application con 401 \"Unauthorized\" indicando come autorizzarsi con un header WWW-Authenticate "
            "contenente almeno una challenge; il client che vuole autenticarsi include un header "
            "Authorization con i fattori di autenticazione; di norma la driving application presenta un "
            "prompt di password al firmatario e poi invia la richiesta con l'header Authorization corretto "
            "(Figure 2). Lo schema \"Basic\" invia i fattori codificati ma non cifrati, quindi sarebbe del "
            "tutto insicuro se lo scambio non avvenisse su connessione sicura (HTTPS/TLS). Il flusso "
            "generale e' lo stesso per la maggior parte degli schemi di autenticazione, cambiando il "
            "contenuto e la codifica degli header; HTTP Digest migliora HTTP Basic evitando la trasmissione "
            "di password in chiaro (il server invia una challenge con realm, nonce, algorithm e qop; il "
            "client risponde con un hash che prova la conoscenza della password, incorporando method e URI e "
            "parametri di freschezza nonce, cnonce, nonce count). Lo schema HTTP Basic e' implementato in CSC "
            "API invocando auth/login (username e password del firmatario direttamente nell'header HTTP come "
            "authorization grant) e auth/revoke (token da revocare). La driving application ottiene l'access "
            "token dal servizio remoto con HTTP Basic o HTTP Digest authentication. Requisiti: l'API "
            "auth/login identificata in CSC API, clausola 11.2 DEVE applicarsi; il messaggio di richiesta "
            "dell'access token DEVE contenere i componenti definiti in CSC API, clausola 11.2 sezione Input; "
            "il messaggio di ritorno dell'access token DEVE contenere i componenti definiti in CSC API, "
            "clausola 11.2 sezione Output. Invocando auth/revoke la driving application puo' invalidare un "
            "access o refresh token ottenuto dal servizio remoto o da un authorization server associato, "
            "impedendo ogni ulteriore accesso riusando il token. Requisiti: l'API auth/revoke identificata in "
            "CSC API, clausola 11.3 DEVE applicarsi; il messaggio di invalidazione DEVE contenere i "
            "componenti definiti in CSC API, clausola 11.3 sezione Input; l'API auth/revoke non ha valori di "
            "output e in risposta e' fornito lo stato HTTP 204 \"No Content\"."
        ),
        "testo_integrale": (
            "5.2.2 HTTP Basic Authentication and HTTP Digest Authentication: NOTE: HTTP Basic "
            "Authentication [i.10] is an unsafe mechanism, and therefore it should not be used, especially "
            "by driving application running as a service. It should only be used when there is a high degree "
            "of trust between the user and driving application and when other authorization types are not "
            "available. This mechanism may also be deprecated in future releases of the present document. "
            "HTTP Basic Authentication should not be employed in processes implementing qualified "
            "electronic signature or seal creation, as it does not meet the required security assurance "
            "level. HTTP defines a general challenge-response authentication framework. When a client "
            "requests a protected resource, the server replies with the HTTP status code 401 \"Unauthorized\", "
            "defined in clause 15.5.2 of IETF RFC 9110 [16], and a WWW-Authenticate header advertising one "
            "or more authentication challenges; the client retries the request including credentials in the "
            "Authorization header. Proxy variants use the HTTP status code 407 \"Proxy Authentication "
            "Required\", defined in clause 15.5.8 of IETF RFC 9110 [16]. The driving application may obtain "
            "an access token for service authorization directly from the signature creation service using "
            "HTTP Basic Authentication, as defined in IETF RFC 9110 [16], using authentication factors (like "
            "user and password) assigned to the signer. These authentication factors will be passed directly "
            "in the HTTP header as an authorization grant to obtain an access token to use for the "
            "subsequent requests within the same session. HTTP Basic Authentication is a simple scheme that "
            "sends credentials as base64 (username:password) in the Authorization header. Base64 is an "
            "encoding, not encryption, therefore TLS (HTTPS) should be used to protect credentials in "
            "transit. The challenge and response flow works like this: - The signature creation service "
            "responds to the driving application with the HTTP status code 401 \"Unauthorized\", defined in "
            "clause 15.5.2 of IETF RFC 9110 [16], and provides information on how to authorize with a "
            "WWW-Authenticate response header containing at least one challenge. - A client that wants to "
            "authenticate itself with the signature creation service can do so by including an Authorization "
            "request header with the authentication factors. - Usually, a driving application will present a "
            "password prompt to the signer and will then issue the request including the correct "
            "Authorization header. Figure 2: Messages between a driving application and a signature creation "
            "service in a common authentication scheme. The \"Basic\" authentication scheme used in the "
            "diagram above sends the authentication factors encoded but not encrypted. This would be "
            "completely insecure unless the exchange is over a secure connection (HTTPS/TLS). The general "
            "message flow above is the same for most authentication schemes. The actual information in the "
            "headers and the way it is encoded may change. HTTP Digest authentication [i.15] improves on "
            "HTTP Basic Authentication by avoiding transmission of plaintext passwords. The server issues a "
            "challenge containing parameters such as realm, nonce, algorithm, and qop (quality of protection "
            "values supported by the server). The client responds with a hash that proves knowledge of the "
            "password, incorporating method and URI, and freshness parameters (nonce, cnonce, nonce count). "
            "The above HTTP Basic Authentication scheme is implemented in CSC API [1] by invoking the API: - "
            "auth/login passing the username and password assigned to the signer directly in the HTTP header "
            "as an authorization grant. - auth/revoke passing the token, that was obtained from the remote "
            "service, to be revoked. By invoking the auth/login API the driving application can obtain an "
            "access token for service authorization from the remote service using HTTP Basic Authentication "
            "or HTTP Digest authentication, as defined in IETF RFC 9110 [16]. The auth/login API identified "
            "in CSC API [1], clause 11.2 shall apply. The message for requesting the access token for "
            "service authorization shall contain the components defined in CSC API [1], clause 11.2 section "
            "Input. The message for returning the access token for service authorization shall contain the "
            "components defined in CSC API [1], clause 11.2 section Output. By invoking the auth/revoke API "
            "the driving application can invalidate access or refresh token obtained from the remote service "
            "or an associated authorization server so that any further access by reusing the token itself is "
            "prevented. The auth/revoke API identified in CSC API [1], clause 11.3 shall apply. The message "
            "for invalidating an access or refresh token for service authorization shall contain the "
            "components defined in CSC API [1], clause 11.3 section Input. The auth/revoke API has no output "
            "values, the HTTP status code 204 \"No Content\", defined in clause 15.3.5 of IETF RFC 9110 "
            "[16], is provided in response."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.2.3 (OAuth 2.0)",
        "testo": (
            "Quando l'autenticazione e' sotto il controllo del servizio di creazione di firma, il servizio "
            "puo' adottare una modalita' indiretta di autorizzazione all'accesso all'API usando OAuth 2.0 "
            "(framework di autorizzazione che puo' essere sfruttato anche per l'autenticazione), spesso "
            "combinato con OpenID Connect (OIDC) per l'autenticazione dell'utente e, opzionalmente, la "
            "delega dell'autorizzazione: l'utente si autentica presso un Identity Provider (interno o "
            "esterno) che emette un access token e, con OIDC, un identity token (JWT) con le informazioni di "
            "identita'; la driving application include il token nelle chiamate API e il servizio di creazione "
            "di firma lo valida per accertare che la driving application sia autorizzata ad accedere alla "
            "risorsa richiesta. Passi principali: 1) Client Registration (la driving application si registra "
            "presso l'Authorization Server del servizio remoto ottenendo client_id ed eventualmente "
            "client_secret); 2) Authorization Flow (l'utente/firmatario e' rediretto all'Authorization "
            "Server, si autentica con le proprie credenziali di identita' e concede il consenso all'accesso "
            "all'API del servizio); 3) Token Issuance (dopo autenticazione e consenso l'Authorization Server "
            "emette l'Access Token usato dalla driving application per invocare l'API e, opzionalmente se si "
            "usa OIDC, l'ID Token con le informazioni di identita' dell'utente); 4) API Access (la driving "
            "application include l'Access Token nell'header Authorization: Bearer <access_token>, e il "
            "servizio valida il token prima di consentire operazioni come l'elenco delle credenziali o il "
            "recupero dei certificati). Un formato di token comune e' il JWT, token firmati digitalmente che "
            "possono portare come claim l'identita' del firmatario (subject), l'issued-at, la scadenza e "
            "ruoli o scope; sono comodi perche' stateless, verificabili da qualunque servizio con una chiave "
            "pubblica senza interrogare l'issuer a ogni richiesta. Requisito: DEVE essere assicurato che il "
            "JWT sia firmato con algoritmi forti e che i servizi di creazione di firma remota si fidino in "
            "modo sicuro della chiave pubblica dell'issuer; con scope o claim JWT si puo' implementare "
            "un'autorizzazione a grana fine. Nella Figure 3 (Authorization Code Grant): se l'utente concede "
            "l'autorizzazione, la driving application ottiene dall'authorization server un access token da "
            "usare nell'header Authorization con tipo Bearer; se non la concede, l'authorization server "
            "restituisce un messaggio di errore e nessun accesso all'API autenticata sara' possibile. NOTE: "
            "per garantire sicurezza e integrita' delle richieste di autorizzazione, IETF RFC 9126 "
            "raccomanda di invocare prima pushed_authorize per trasmettere in modo sicuro la richiesta di "
            "autorizzazione, immutabile e protetta da manomissioni o fuga, e poi l'endpoint authorize che "
            "avra' bisogno solo del riferimento leggero request_uri, minimizzando il rischio e mitigando gli "
            "attacchi di injection. Lo schema e' implementato in CSC API invocando: oauth2/authorize (e "
            "oauth2/pushed_authorize se necessario), che gestisce le richieste di autorizzazione con "
            "l'Authorization Code flow; oauth2/token per ottenere un bearer access token OAuth 2.0 "
            "dall'authorization server passando le credenziali client (id e secret) pre-assegnate alla "
            "driving application, oppure l'authorization code o il refresh token restituiti dopo "
            "l'autenticazione dell'utente; oauth2/revoke per revocare il token. Requisiti: l'API "
            "oauth2/authorize identificata in CSC API, clausola 8.2.2 DEVE applicarsi; il messaggio di "
            "richiesta dell'authorization code DEVE contenere i componenti definiti in CSC API, clausola "
            "8.2.2 sezione Input, considerando quanto specificato nella sezione Service scope; il messaggio "
            "di ritorno DEVE contenere i componenti definiti in CSC API, clausola 8.2.2 sezione Output; "
            "l'API oauth2/pushed_authorize identificata in CSC API, clausola 8.2.3 DEVE applicarsi; il "
            "messaggio di richiesta del request URI DEVE contenere i componenti definiti in CSC API, clausola "
            "8.2.2 sezione Input, tranne il parametro request_uri; il messaggio di ritorno del request URI "
            "DEVE contenere i componenti definiti in IETF RFC 9126, clausola 2.2; l'API oauth2/token "
            "identificata in CSC API, clausola 8.2.4 DEVE applicarsi e i messaggi di richiesta e ritorno "
            "dell'access token DEVONO contenere i componenti definiti in CSC API, clausola 8.2.4 sezioni "
            "Input e Output; l'API oauth2/revoke identificata in CSC API, clausola 8.2.5 DEVE applicarsi e "
            "il messaggio di invalidazione DEVE contenere i componenti definiti in CSC API, clausola 8.2.5 "
            "sezione Input; l'API oauth2/revoke non ha valori di output e in risposta e' fornito lo stato "
            "HTTP 204 \"No Content\"."
        ),
        "testo_integrale": (
            "5.2.3 OAuth 2.0: When the authentication is under the control of the signature creation "
            "service the signature creation service may adopt an indirect way of authorizing access to the "
            "API by using OAuth 2.0 [17] that is primarily an authorization framework, but that can also be "
            "leveraged for authentication when interacting with a signature creation service API. OAuth 2.0 "
            "ensures that only authorized applications and users can access sensitive signing operations "
            "without exposing credentials directly. A common approach is to combine OAuth 2.0 with OpenID "
            "Connect (OIDC) [21] to handle user authentication and, optionally, authorization delegation. "
            "OAuth 2.0 defines a framework for token-based authorization, while OIDC adds an identity layer "
            "for authentication. In this flow, the user authenticates through an Identity Provider, which "
            "issues an access token for authorization and, in the case of OIDC, an identity token (JWT "
            "[i.4] may be used) that conveys identity information. These tokens can then be presented to the "
            "signature creation service. The Identity Provider can be an internal authentication service or "
            "an external one. A driving application will include a token in its API calls to the signature "
            "creation service, representing the user's identity and permissions. The signature creation "
            "service validates this token to ensure the driving application is authorized and allowed to "
            "access the requested resource. Main steps: 1) Client Registration The driving application "
            "(client) registers with the remote signing server's Authorization Server to obtain a client_id "
            "and possibly a client_secret. 2) Authorization Flow The user (signatory) is redirected to the "
            "signature creation service's Authorization Server. The user authenticates using their identity "
            "credentials. The user grants consent for the driving application to access signature creation "
            "service API. 3) Token Issuance After successful authentication and consent, the Authorization "
            "Server issues: - Access Token, used by the driving application to invoke the signature "
            "creation service API. - ID Token (optional, if OpenID Connect is used), that provides user "
            "identity information for authentication purposes. 4) API Access The driving application "
            "includes the Access Token in the Authorization header: - Authorization: Bearer "
            "<access_token> The signature creation service validates the token before allowing operations "
            "like listing credentials or retrieving certificates. A common token format is JSON Web Tokens "
            "(JWT), which are digitally signed tokens that can carry signer identity (subject), issued-at "
            "time, expiry, and roles or scopes as claims. They are convenient in services invocation "
            "because they are stateless - any service can verify the token with a public key without "
            "needing to call back to the issuer for each request. It shall be ensured that the JWT is "
            "signed with strong algorithms and that remote signature creation services trust the issuer's "
            "public key securely. Using JWT scopes or claims, a fine-grained authorization can be "
            "implemented. Figure 3: Authorization Code Grant between a driving application and a signature "
            "creation service. In the above diagram, if the user grants authorization, the driving "
            "application will obtain from the authorization server an access token that can be used for "
            "authorizing requests to signature creation service by using an Authorization header with "
            "Bearer type followed by that access token. If the user does not grant authorization, the "
            "authorization server will return an error message and no access to authenticated API of the "
            "signature creation service will be possible. NOTE: In order to ensure security and integrity "
            "of authorization requests, IETF RFC 9126 [18] recommends invoking first pushed_authorize to "
            "securely transmit the authorization request, immutable, and protected from tampering or "
            "leakage and then the authorize endpoint that will only need the request_uri lightweight "
            "reference, minimizing risk and mitigating injection attacks. The above scheme is implemented "
            "in CSC API [1] by invoking the API: - oauth2/authorize (and oauth2/pushed_authorize if "
            "needed), that manages authorization requests using the Authorization Code flow as described "
            "in Section 4.1 of IETF RFC 6749 [17]. - oauth2/token to obtain an OAuth 2.0 bearer access "
            "token [19] from the authorization server by passing either the client credentials (id and "
            "secret) pre-assigned by the authorization server to the driving application, or the "
            "authorization code or refresh token returned by the authorization server after a successful "
            "user authentication. - oauth2/revoke passing the access or refresh token, that was obtained "
            "from the authorization server, to be revoked. By invoking the oauth2/authorize API the "
            "driving application can obtain an authorization code for service authorization from the "
            "authorization server of the remote signing service. The oauth2/authorize API identified in "
            "CSC API [1], clause 8.2.2 shall apply. The message for requesting the authorization code for "
            "service authorization shall contain the components defined in CSC API [1], clause 8.2.2 "
            "section Input considering what specified in section Service scope. The message for returning "
            "the authorization code for service authorization shall contain the components defined in CSC "
            "API [1], clause 8.2.2 section Output. By invoking the oauth2/pushed_authorize API the driving "
            "application can push the payload of an OAuth 2.0 authorization request to the authorization "
            "server via a direct request and obtain a request URI to be used as reference to the data in a "
            "subsequent call to the authorization endpoint (oauth2/authorize) of the authorization server. "
            "The oauth2/pushed_authorize API identified in CSC API [1], clause 8.2.3 shall apply. The "
            "message for requesting the request URI that will be used as reference to the data in a "
            "subsequent call to the authorization endpoint shall contain the components defined in CSC API "
            "[1], clause 8.2.2 section Input apart from the request_uri parameter. The message for "
            "returning the request URI shall contain the components defined in IETF RFC 9126 [18], clause "
            "2.2. By invoking the oauth2/token API the driving application can obtain an access token for "
            "service authorization from the authorization server of the signature creation service. The "
            "oauth2/token API identified in CSC API [1], clause 8.2.4 shall apply. The message for "
            "requesting the access token for service authorization shall contain the components defined in "
            "CSC API [1], clause 8.2.4 section Input. The message for returning the access token for "
            "service authorization shall contain the components defined in CSC API [1], clause 8.2.4 "
            "section Output. By invoking the oauth2/revoke API the driving application can invalidate "
            "access or refresh token obtained from the authorization server of the signature creation "
            "service so that any further access by reusing the token itself is prevented. The "
            "oauth2/revoke API identified in CSC API [1], clause 8.2.5 shall apply. The message for "
            "invalidating an access or refresh token for service authorization shall contain the "
            "components defined in CSC API [1], clause 8.2.5 section Input. The oauth2/revoke API has no "
            "output values, the HTTP status code 204 \"No Content\", defined in clause 15.3.5 of IETF RFC "
            "9110 [16], is provided in response."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 4.1 (Signature creation process steps and data elements)",
        "testo": (
            "La Figure 1 (derivata da ETSI EN 319 102-1, clausola 4.2.1) mostra i passi e i data element "
            "correlati del processo di creazione della firma. Nella creazione di firma remota i diversi passi "
            "sono eseguiti secondo una decomposizione in piu' componenti, che accedono o rendono disponibili "
            "i corrispondenti data element. Il processo illustrato e' limitato ai building block e alle "
            "informazioni necessarie a creare una firma, senza specificare possibili soluzioni per attivita' "
            "come l'autenticazione del firmatario, l'autorizzazione all'uso della chiave di firma o la "
            "disponibilita' del certificato di firma. Il modulo di attivazione della firma nell'area tamper "
            "protected e' necessario solo quando il Signature Creation Service (SCS) rispetta il meccanismo "
            "di attivazione del Sole Control Assurance Level 2 (SCAL2) definito in EN 419 241-1."
        ),
        "testo_integrale": (
            "4.1 Signature creation process steps and data elements: Figure 1 (derived from ETSI EN 319 "
            "102-1 [i.12], clause 4.2.1) shows the various steps and the related data elements for a "
            "signature creation process. For remote signature creation, different steps of this process are "
            "carried out according to a decomposition into several components, which will have access to or "
            "make available the corresponding data elements. The process illustrated in the figure below is "
            "limited to the buildings blocks and information needed for creating a signature without "
            "specifying possible solutions for tasks such as signer authentication, authorization to the "
            "signing key usage or signing certificate availability. The signature activation module in the "
            "tamper protected area is needed only when the Signature Creation Service (SCS) complies to the "
            "Sole Control Assurance Level 2 (SCAL2) signature activation mechanism as defined in EN 419 "
            "241-1 [6]. Figure 1: Process Steps and Data Elements in Signature Creation."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "servizio di gestione di dispositivo di creazione di firma elettronica a distanza",
            "firma elettronica avanzata",
        ],
    },
    {
        "riferimento": "clausola 4.2 (Service main components and interfaces)",
        "testo": (
            "Il processo presuppone scenari in cui la firma AdES e/o il Digital Signature Value (DSV) sono "
            "creati con una chiave di firma custodita in un modulo crittografico denominato Signature "
            "Creation Device (SCDev), gestito da un Signature Creation Service Provider (SCSP). In base ai "
            "tipi di dati gestiti in richieste e risposte si identificano due componenti principali, con "
            "interfacce distinte per la gestione della firma: il Server Signing Application Service "
            "Component (SSASC) e il Signature Creation Application Service Component (SCASC). L'SSASC e' il "
            "componente che supporta la creazione dei valori di firma digitale, puo' interagire con lo SCDev "
            "che custodisce la chiave privata del firmatario (che cosi' controlla la chiave con un certo "
            "livello di confidenza), e ha come input principale il Data To Be Signed Representation (DTBSR) "
            "e altri parametri e come output principale il valore di firma digitale. Lo SCASC e' il "
            "componente che supporta la creazione della firma digitale AdES e svolge diverse parti "
            "specifiche del processo, interagendo con l'SSASC per richiedere la creazione dei valori di "
            "firma; ha come input principale il documento o i documenti da firmare (SD) o la loro "
            "rappresentazione (SDR) e altri parametri, e come output il documento o i documenti firmati o "
            "la firma o le firme digitali. SCS indica un servizio TSP che implementa una Signature Creation "
            "Application (SCA) e/o una Server Signing Application (SSA). Sono possibili alcune varianti di "
            "queste interfacce a seconda della ripartizione funzionale tra SCS e sistema locale del "
            "firmatario."
        ),
        "testo_integrale": (
            "4.2 Service main components and interfaces: The above process points out scenarios where the "
            "AdES and/or Digital Signature Value (DSV) are created using a signing key held within a "
            "cryptographic security module named Signature Creation Device (SCDev) operated by a Signature "
            "Creation Service Provider (SCSP). Based on the different types of data managed in requests and "
            "responses, two main components can be identified in the above schema providing different "
            "interfaces for signing management: the Server Signing Application Service Component (SSASC) "
            "and the Signature Creation Application Service Component (SCASC) defined below. The SSASC is "
            "the component supporting digital signature values creation. The SSASC can interact with the "
            "SCDev holding the signer's private key. When the SSASC uses the SCDev, the authorized signer "
            "controls the signing key with a certain level of confidence. The SSASC interface has the Data "
            "To Be Signed Representation (DTBSR) and other parameters as main input and the digital "
            "signature value as main output. The SCASC is the component supporting AdES digital signature "
            "creation and carries out several specific parts of the signature creation process. The SCASC "
            "interacts with the SSASC for requesting digital signature values creation. The SCASC interface "
            "has the document(s) to be signed (SD) or its (their) representation (SDR) and other parameters "
            "as main input and the signed document(s) or the digital signature(s) as main output. SCS "
            "denotes a TSP service implementing a Signature Creation Application (SCA) and/or a Server "
            "Signing Application (SSA). Some variants of these interfaces are possible depending on the "
            "functional split between the SCS and the signer's local system. The following clauses specify "
            "main information objects and processes in SCASC and SSASC."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": [
            "servizio di gestione di dispositivo di creazione di firma elettronica a distanza",
            "firma elettronica avanzata",
        ],
    },
    {
        "riferimento": "clausola 4.3.1 (Signer's document and hashing)",
        "testo": (
            "Il processo di creazione della firma inizia dal documento del firmatario (SD) da firmare. L'SD "
            "e' rappresentato (SDR) da un valore di hash nel Data To Be Signed (DTBS). Osservazioni: la "
            "creazione dell'SDR (l'hashing) puo' avvenire dove e' custodito l'SD oppure essere fatta dallo "
            "SCASC - nel primo caso l'SDR e' trasferito allo SCASC, nel secondo caso e' l'SD a essere "
            "trasferito allo SCASC; l'SD fa parte del Signed Data Object (SDO) finale e parte della funzione "
            "Signed Data Object Composer (SDOC), che costruisce il formato AdES finale, consiste nel "
            "correlare il valore di firma digitale all'SD. Una decisione di progetto importante per i "
            "servizi di creazione di firma remota e' dove l'SD, e quindi il suo contenuto, deve essere "
            "disponibile: rendere disponibile solo l'SDR limita le minacce alla riservatezza ma puo' "
            "comportare limitazioni funzionali (es. quando occorre creare firme enveloping o enveloped, o "
            "includere la rappresentazione visiva della firma)."
        ),
        "testo_integrale": (
            "4.3.1 Signer's document and hashing: The signature creation process starts with the signer's "
            "document (SD), which is to be signed. The SD is represented (SDR) by a hash value in the Data "
            "To Be Signed (DTBS). The following observations are made: - The creation of the SDR (the "
            "hashing) can be done where the SD is stored or by the SCASC. In the former case, the SDR is "
            "transferred to the SCASC while in the latter case, the SD is transferred to the SCASC. - The "
            "SD is part of the final Signed Data Object (SDO). Part of the Signed Data Object Composer "
            "(SDOC) function (building of the final AdES format) is to relate the digital signature value "
            "to the SD. An important design decision for remote signature creation services is where the "
            "SD, and thus its content, needs to be available. Making available only the SDR limits threats "
            "to confidentiality but may result in limitations in the functionality of the remote signature "
            "creation solution (i.e. when enveloping or enveloped signatures need to be created, or when "
            "visual representation of the signature needs to be included)."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "firma elettronica avanzata",
            "documento elettronico",
        ],
    },
    {
        "riferimento": "clausola 4.3.2 (DTBS composition and formatting)",
        "testo": (
            "Nei due processi di composizione e formattazione del DTBS, considerati insieme nel contesto del "
            "documento, l'SDR (hash del documento da firmare o hash di una versione formattata del documento "
            "da firmare) e gli hash degli attributi/proprieta' firmati sono assemblati nel Data To Be Signed "
            "Formatted (DTBSF). Oltre a un identificatore di certificato (hash del certificato di firma, "
            "possibilmente anche di ulteriori certificati della catena) come indicato nella figura, "
            "ulteriori attributi firmati sono richiesti o ammessi dai formati di firma standard ETSI "
            "(C/X/J/PAdES): ad esempio tutte le varianti baseline CAdES e XAdES richiedono la presenza degli "
            "attributi firmati \"document type\" (dell'SD) e \"claimed signing time\". Gli attributi firmati "
            "o i loro valori di hash, la cui presenza e' necessaria nel DTBS, sono disponibili allo SCASC "
            "quando il DTBSF e' creato dallo SCASC."
        ),
        "testo_integrale": (
            "4.3.2 DTBS composition and formatting: In the two processes of DTBS composition and "
            "formatting, which in the context of the present document are considered together, the SDR "
            "(hash of the document to be signed or hash of a formatted version of the document to be "
            "signed) and hashes of signed attributes/properties are assembled into the Data To Be Signed "
            "Formatted (DTBSF). In addition to a certificate identifier (hash of signing certificate, "
            "possibly also of further certificates in a certificate chain) as indicated in the figure, "
            "further signed attributes are required or allowed by the ETSI standard signature formats "
            "(C/X/J/PAdES). For example all baseline CAdES and XAdES variants require the presence of the "
            "signed attributes \"document type\" (of SD) and \"claimed signing time\". The signed attributes "
            "or their hash values, whose presence is needed in the DTBS, are available to the SCASC when "
            "the DTBSF is created by the SCASC."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "firma elettronica avanzata",
        ],
    },
    {
        "riferimento": "clausola 4.3.3 (DTBS preparation)",
        "testo": (
            "Questo passo consiste nel creare il DTBSR a partire dal DTBSF: lo SCASC prepara l'intero "
            "DTBSF, ne calcola l'hash e invia il valore di hash (DTBSR) come input a un SSASC."
        ),
        "testo_integrale": (
            "4.3.3 DTBS preparation: This step consists of creating the DTBSR from the DTBSF. The SCASC "
            "prepares the entire DTBSF, calculates the hash, and sends the hash value (DTBSR) as input to "
            "an SSASC."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "firma elettronica avanzata",
        ],
    },
    {
        "riferimento": "clausola 4.3.4 (SDO composer)",
        "testo": (
            "Come passo finale viene costruito l'SDO (il formato AdES): si combinano il valore di firma "
            "digitale e altri parametri nel formato richiesto. A seconda del formato, la firma digitale resa "
            "disponibile per l'SD si denomina: Enveloped (la firma e' aggiunta all'SD, es. firma PAdES); "
            "Enveloping (la firma avvolge l'SD, es. alcuni formati CAdES); Detached (la firma e' un oggetto "
            "separato collegato all'SD). La composizione dell'SDO e' fatta da una istanza di servizio "
            "separata oppure integrata con altre funzioni nello SCASC."
        ),
        "testo_integrale": (
            "4.3.4 SDO composer: As the final step, the SDO (the AdES format) is constructed. This consists "
            "of combining the digital signature value with other parameters into the requested format. "
            "Depending on the format, the digital signature made available for the SD is named: - "
            "Enveloped: The signature is added to the SD (e.g. PAdES signature). - Enveloping: The "
            "signature wraps the SD (e.g. certain CAdES formats). - Detached: The signature is a separate "
            "object linked to the SD. The SDO composing is done by a separate service instance or "
            "integrated with other functions in the SCASC."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "firma elettronica avanzata",
            "documento elettronico",
        ],
    },
    {
        "riferimento": "clausola 4.4.1.1 (Introduction)",
        "testo": (
            "Scopo del processo di creazione della firma e' prendere il DTBSR e creare un valore di firma "
            "digitale sotto il controllo del firmatario. Nel contesto del documento, la creazione del valore "
            "di firma digitale e' gestita da un SSASC che usa una chiave di firma custodita in un modulo "
            "crittografico di sicurezza (SCDev), che i firmatari possono attivare mediante un processo "
            "sicuro di autorizzazione e attivazione (ossia applicando il protocollo di attivazione della "
            "firma specificato in EN 419 241-1)."
        ),
        "testo_integrale": (
            "4.4.1.1 Introduction: The purpose of the signature creation process is to take the DTBSR and "
            "create a digital signature value under the control of the signer. In the context of the "
            "present document, the creation of the digital signature value is managed by an SSASC that uses "
            "a signing key, held within a cryptographic security module (SCDev), that the signers can "
            "activate by means of a secure authorization and activation process (i.e. by applying the "
            "signature activation protocol specified in EN 419 241-1 [6])."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "servizio di gestione di dispositivo di creazione di firma elettronica a distanza",
            "firma elettronica avanzata",
        ],
    },
    {
        "riferimento": "clausola 4.4.1.2 (Signature activation)",
        "testo": (
            "L'SSASC usa uno SCDev remoto per generare, mantenere e usare le chiavi di firma sotto il "
            "controllo dei rispettivi firmatari autorizzati. Il firmatario autorizzato controlla "
            "remotamente la chiave di firma con un certo livello di confidenza, possibilmente mediante il "
            "Signature Activation Module (SAM). Il SAM e' un componente software che usa i Signature "
            "Activation Data (SAD) per imporre il controllo esclusivo nella creazione di firme remote, con "
            "il firmatario che conferma la propria autorizzazione ad attivare la chiave di firma al fine di "
            "firmare il DTBSR; questo processo assicura la confidenza che le chiavi di firma siano sotto il "
            "controllo esclusivo del firmatario. Nel documento sono considerati due livelli di confidenza "
            "del controllo della chiave di firma, definiti in EN 419 241-1: SCAL1 - Sole Control Assurance "
            "Level 1 (le chiavi di firma sono usate con un basso livello di confidenza sotto il controllo "
            "esclusivo del firmatario; l'uso della chiave da parte del firmatario autorizzato e' imposto "
            "dall'SSASC, che autentica il firmatario, e l'attivazione della chiave puo' permanere per un "
            "dato periodo e/o per un dato numero di firme; NOTE: non ci si aspetta che tali implementazioni "
            "soddisfino i requisiti di controllo esclusivo attesi per un QSCD stand-alone come definito dal "
            "regolamento eIDAS); SCAL2 - Sole Control Assurance Level 2 (le chiavi di firma sono usate con "
            "un alto livello di confidenza sotto il controllo esclusivo del firmatario; l'uso della chiave "
            "da parte del firmatario autorizzato e' imposto dal modulo di attivazione della firma mediante "
            "signature activation data forniti dal firmatario con un protocollo di attivazione della firma, "
            "per abilitare l'uso della corrispondente chiave a firmare documenti specifici)."
        ),
        "testo_integrale": (
            "4.4.1.2 Signature activation: The SSASC uses a remote SCDev to generate, maintain and use the "
            "signing keys under the control of their authorized signers. The authorized signer remotely "
            "controls the signing key with a certain level of confidence possibly by means of the Signature "
            "Activation Module (SAM). The SAM is a software component using the Signature Activation Data "
            "(SAD) for enforcing sole control in remote signatures creation from the signer confirming its "
            "authorization to activate its signing key for the purpose of signing the DTBSR. This process "
            "ensures confidence that the signing keys are under the sole control of the signer. Two "
            "different levels of confidence of the control of the signing key, as defined in EN 419 241-1 "
            "[6], are considered in the present document: - Sole Control Assurance Level 1 (SCAL1): - The "
            "signing keys are used, with a low level of confidence, under the sole control of the signer. - "
            "The authorized signer's use of its key for signing is enforced by the SSASC which "
            "authenticates the signer. The activation of the signing key can remain for a given period "
            "and/or for a given number of signatures. NOTE: It is not expected that such implementations "
            "would meet the requirements of sole control as it would be expected for a stand-alone QSCD as "
            "defined in the eIDAS [i.1] Regulation. - Sole Control Assurance Level 2 (SCAL2): - The signing "
            "keys are used, with a high level of confidence, under the sole control of the signer. - The "
            "authorized signer's use of its key for signing is enforced by the signature activation module "
            "by means of signature activation data provided, by the signer, using a signature activation "
            "protocol, in order to enable the use of the corresponding signing key to sign specific "
            "documents."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "servizio di gestione di dispositivo di creazione di firma elettronica a distanza",
            "dispositivo qualificato di creazione di firma elettronica",
        ],
    },
    {
        "riferimento": "clausola 4.4.1.3 (Signature creation by SCDev)",
        "testo": (
            "Il processo di creazione della firma e' eseguito dallo SCDev. Nel contesto del documento sono "
            "considerate solo architetture in cui il processo di creazione della firma e' svolto da uno "
            "SCDev remoto. Secondo i livelli di controllo esclusivo sopra richiamati, la chiave di firma "
            "puo' essere usata per generare il valore di firma digitale dopo una autenticazione del "
            "firmatario andata a buon fine da parte dell'SSASC (SCAL1) oppure dopo una verifica dei SAD "
            "andata a buon fine da parte del SAM."
        ),
        "testo_integrale": (
            "4.4.1.3 Signature creation by SCDev: The signature creation process is performed by the SCDev. "
            "In the context of the present document, only architectures where the signature creation "
            "process is carried out by a remote SCDev are considered. According to the above sole control "
            "assurance levels the signing key can be used to generate the digital signature value creation "
            "after a successful signer authentication by the SSASC (SCAL1) or after a successful SAD "
            "verification by the SAM."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "servizio di gestione di dispositivo di creazione di firma elettronica a distanza",
            "firma elettronica avanzata",
        ],
    },
    {
        "riferimento": "clausola 5.2.4 (Other authentication mechanisms)",
        "testo": (
            "La comunicazione sottostante tra driving application e servizio di creazione di firma puo' "
            "garantire il controllo degli accessi in modi diversi da OAuth 2.0 o dall'autenticazione HTTP "
            "Basic o Digest. Le seguenti alternative possono essere considerate per autenticare i client a "
            "un servizio di creazione di firma: Mutual TLS (mTLS) con certificati client (la driving "
            "application presenta un certificato X.509 durante l'handshake TLS; il servizio lo valida per "
            "catena, revoca e policy e autorizza in base a identita'/attributi del certificato); "
            "HMAC-Signed Requests (ogni driving application ha una API key e un secret, calcola HMAC "
            "(secret, canonical_request) e invia firma e metadati come timestamp e nonce); Signed JWT "
            "Assertions (le driving application auto-emettono un'asserzione firmata JWT che prova identita' "
            "e claim di autorizzazione; il servizio valida la firma contro la chiave pubblica del client o "
            "la propria CA e i claim standard aud, exp, nbf, jti); SAML 2.0 Assertions usate nel framework "
            "di autenticazione SAML oppure nel framework OAuth 2.0 come Bearer o Holder-of-Key (le driving "
            "application ottengono l'asserzione SAML da un Identity Provider e la presentano al servizio; "
            "con Holder-of-Key provano il possesso di una chiave, piu' forte del bearer); SSH Mutual "
            "Authentication via Reverse Tunnel (tunnel SSH con autenticazione mutua a chiave pubblica); "
            "Challenge-Response con la chiave qualificata del client (il servizio emette un nonce e un "
            "eventuale context hash; la driving application firma il nonce con una chiave privata "
            "QSCD/certificato qualificato compatibile CAdES/XAdES/JAdES e restituisce la firma; il servizio "
            "valida la firma prima di consentire l'invocazione API richiesta); FIDO2/Passkey "
            "(autenticazione multi-fattore strong resistente al phishing). L'elenco sopra non e' esaustivo: "
            "ulteriori soluzioni diverse possono essere ugualmente operative."
        ),
        "testo_integrale": (
            "5.2.4 Other authentication mechanisms: The underlying communication between the driving "
            "application and the signature creation service may ensure access control in some other "
            "different ways than OAuth 2.0 or HTTP Basic or Digest Authentication. The following "
            "alternatives can be considered for authenticating clients to a signature creation service: - "
            "Mutual TLS (mTLS) with client certificates. The driving application presents an X.509 "
            "certificate during the TLS handshake. The signature creation service validates it (chain, "
            "revocation, policy) and authorizes based on the certificate's identity/attributes. - "
            "HMAC-Signed Requests. Each driving application has an API key + secret. It computes HMAC "
            "(secret, canonical_request) and sends signature + metadata (timestamp, nonce). - Signed JWT "
            "Assertions. Driving applications self-issue a signed assertion (JWT) proving identity and "
            "authorization claims. The signature creation service validates signature (against client "
            "public key or its own CA) and standard claims (aud, exp, nbf, jti). - SAML 2.0 Assertions "
            "used within the SAML authentication framework (see [27] and [28]) or alternatively within the "
            "OAuth2.0 framework (see [17]) like Bearer (or Holder-of-Key) (see [29]). Driving applications "
            "obtain a SAML assertion from an Identity Provider and present it to the signature creation "
            "service, with Holder-of-Key, the driving applications prove possession of a key (stronger than "
            "bearer). - SSH Mutual Authentication via Reverse Tunnel. Establishing an SSH tunnel with "
            "mutual public-key auth. - Challenge-Response with Client's Qualified Key (Nonce Signing). The "
            "signature creation service issues a nonce (and optional context hash). The driving "
            "application signs the nonce with a QSCD/qualified certificate private key (CAdES/XAdES/JAdES "
            "compatible) and returns signature. The signature creation service validates the signature "
            "before allowing the requested API invocation. - FIDO2/Passkey phishing-resistant strong "
            "multi-factor authentication (see [30] and [20]). The above list is not exhaustive, further "
            "different solutions can be operational too."
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
    "clausola 4.1 (Signature creation process steps and data elements)",
    "clausola 4.2 (Service main components and interfaces)",
    "clausola 4.3.1 (Signer's document and hashing)",
    "clausola 4.3.2 (DTBS composition and formatting)",
    "clausola 4.3.3 (DTBS preparation)",
    "clausola 4.3.4 (SDO composer)",
    "clausola 4.4.1.1 (Introduction)",
    "clausola 4.4.1.2 (Signature activation)",
    "clausola 4.4.1.3 (Signature creation by SCDev)",
    "clausola 5.1 (Introduction)",
    "clausola 5.2.1 (Overview)",
    "clausola 5.2.2 (HTTP Basic Authentication and HTTP Digest Authentication)",
    "clausola 5.2.3 (OAuth 2.0)",
    "clausola 5.2.4 (Other authentication mechanisms)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Nessuna citazione letterale interna alla Fonte 20 in questo capitolo: tutti i
# rinvii presenti (EN 419 241-1, ETSI EN 319 102-1, eIDAS, IETF RFC 9110/6749/
# 9126, CSC API, SAML/FIDO) puntano a documenti esterni e le relazioni
# cross-fonte sono demandate alla Fase 6 della sessione principale (ADR-0009).
# Il rinvio deittico di 4.4.1.3 ("the above sole control assurance levels") non
# e' una citazione letterale di clausola e non e' modellato come relazione.
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
