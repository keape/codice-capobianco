"""ETSI TS 119 432 V1.3.1 (2026-03) - Electronic Signatures and Trust
Infrastructures (ESI); Protocols for remote digital signature creation.
Fonte 20 (la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 6:
Annex A (normative) "OpenID4VP EUDIW-centric signing flow profile", sottoclavole
A.1 (Overview), A.2 (Roles & Standards), A.3 (Profile scope & transport), A.4
(Profile identifiers), A.5.1-A.5.2 (High-level interaction models), A.6.1-A.6.4
(Request construction: Introduction, Required parameters (OpenID4VP layer),
dcql_query (selecting an acceptable signing certificate), transaction_data (the
QES transaction)), A.7.1-A.7.3 (Response handling: Inline (VP Token) -
x509PresentationResponse, Out of band (HTTP POST to responseURI), EUDIW
processing), A.8 (Transaction data processing & UX rendering (EUDIW)), A.9
(Complementary approval flow), A.10 (Security & privacy requirements), A.11
(Conformance checklist (RP)), A.12.1-A.12.4 (Examples). Documento unico (non
multi-parte): i `riferimento` NON portano prefisso di Parte. Testo ufficiale in
app/.source_cache/etsi_119_432/cap06.txt (letto sempre con selettore `:raw`,
altrimenti il tool tronca le righe lunghe a 768 caratteri introducendo "..."
e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_119_432/manifest.json.

Modellazione (ADR-0007), stesso criterio gia' applicato alle altre fonti ETSI
gia' censite e alle clausole di uno standard tecnico, adattato a un annesso
normativo di profilo: un nodo per ogni sottoclavola numerata che porta
contenuto proprio; le intestazioni di puro raggruppamento non generano ne'
nodo ne' item di indice. Questo capitolo produce 9 Obblighi e 12 Principi su
21 item di indice. Scelte voce per voce:

- Annex A (intestazione dell'annesso, "OpenID4VP EUDIW-centric signing flow
  profile") -> NESSUN nodo, NESSUN item di indice: titolo di annesso senza
  testo proprio, il testo ufficiale passa direttamente al titolo A.1. Stesso
  trattamento delle intestazioni di raggruppamento A.5 ("High-level interaction
  models"), A.6 ("Request construction (RP -> EUDIW)"), A.7 ("Response handling
  (EUDIW -> RP)") e A.12 ("Examples"): solo titolo, nessuna riga di testo prima
  della sottoclavola successiva.
- Annex A.1 (Overview) -> 1 Principio "altro". Dichiarazione di cornice del
  profilo, senza "shall"/"should" e senza soggetto obbligato: enuncia che
  l'annesso definisce un profilo con cui un RP puo' richiedere la creazione di
  QES a un EUDIW che integra una Signature Creation Application, usando
  OpenID4VP e OID4VC come protocolli di trasporto/interazione e CSC DM e CSC
  data model bindings per dati di transazione e risultati; elenca i tre fuochi
  del profilo (richieste, risposte, dati di transazione), il flusso considerato
  in tre passi (l'RP chiede la creazione, l'EUDIW orchestra e raccoglie il
  consenso, l'EUDIW restituisce le firme nella authorization response
  OpenID4VP o a una responseURI), il perimetro (sola interfaccia RP <-> EUDIW,
  interazione interna EUDIW <-> QTSP fuori ambito) e chiude con la NOTE che il
  flusso descritto non e' l'unico possibile. Classificato "altro" e non
  "scopo/ambito di applicazione" perche' non e' la clausola di Scope del
  documento (che e' la clausola 1, nel capitolo 1 di questa Fonte) ma
  l'overview di un profilo d'annesso: la riserva sul valore "scopo/ambito"
  evita di duplicare a livello di annesso il perimetro del documento.
- Annex A.2 (Roles & Standards) -> 1 Principio "altro". Elenco descrittivo dei
  ruoli (Relying Party, EUDIW, Authorization Server / Signature Creation
  Service Provider, QTSP/SAM dichiarato fuori ambito) e delle norme di
  riferimento (EUDI Wallet Architecture and Reference Framework): nessun verbo
  prescrittivo, i comportamenti dei ruoli sono enunciati all'indicativo
  presente ("Uses OpenID4VP authorization request with dcql_query and
  transaction_data", "the SAM may enforce sole control using Signature
  Activation Data (SAD)"). Il "may" dell'ultima voce e' facolta' tecnica del
  fornitore, non obbligo.
- Annex A.3 (Profile scope & transport) -> 1 Obbligo "tecnico/sicurezza",
  soggetto "Terza parte" (RP). Deroga consapevole all'elenco descrittivo del
  mandato di capitolo: pur essendo a prevalenza descrittiva, la clausola
  contiene tre prescrizioni esplicite su un soggetto identificabile — "The
  response_type parameter value shall be vp_token", "The response_mode
  parameter value should be direct_post or direct_post.jwt", "The RP shall
  return redirect_uri in response to the HTTP POST request from the EUDIW" —
  cioe' esattamente il criterio ADR-0007 dell'Obbligo (verbo prescrittivo +
  soggetto identificabile), dello stesso tenore delle prescrizioni su parametri
  di A.6.2; censirla come Principio lascerebbe tre "shall" fuori dal grafo. Lo
  "should" e' trattato come prescrittivo (stessa convenzione delle clausole
  "should" delle altre fonti ETSI censite). Il resto della clausola (uso di
  OAuth2 Authorization Request / Response, Request Object JAR a request_uri,
  schema openid4vp://) resta descrittivo ed e' assorbito nello stesso nodo
  perche' la clausola non ha numerazione interna.
- Annex A.4 (Profile identifiers) -> 1 Principio "altro". Elenco di
  identificatori di tipo (transaction data type per la richiesta QES e per
  l'approvazione QES, formato di credenziale X.509 in OID4VC/VP): valori
  costanti, nessun verbo prescrittivo e nessun soggetto obbligato. Il rinvio
  "(see Annex B)" e' citazione letterale di un annesso della stessa Fonte ma
  vive in un altro capitolo (cap07), non registrato al momento dell'INSERT di
  questo capitolo: nessuna relazione emessa (vedi nota finale).
- Annex A.5.1 (EUDIW: RP <-> EUDIW, EUDIW <-> QTSP) -> 1 Principio "altro".
  Elenco numerato dei tre passi del modello di interazione, all'indicativo
  presente ("RP sends an OpenID4VP Authorization Request that includes...",
  "EUDIW renders transaction data...", "EUDIW returns inline the signatures
  ... or posts out-of-band..."): flusso descrittivo, non prescrizione.
- Annex A.5.2 (QTSP: QTSP <-> EUDIW) -> 1 Principio "altro". Descrive il
  flusso speculare in cui il QTSP chiede all'EUDIW di presentare un'attestazione
  contenente qesApproval, crittograficamente legata ai dati di transazione, e
  l'AS la usa per autorizzare la chiamata di firma CSC API: indicativo presente
  ("requests", "uses"), nessun obbligo.
- Annex A.6.1 (Introduction) -> 1 Obbligo "tecnico/sicurezza", soggetto "Terza
  parte" (RP). "The RP shall use OpenID4VP 1.0 and send an OAuth/OIDC
  authorization request with the parameters specified in the following
  sub-clauses": prescrive il protocollo e la costruzione della richiesta, ed e'
  la chiave di lettura normativa delle sottoclavole A.6.2-A.6.4, che
  dettagliano "the parameters specified".
- Annex A.6.2 (Required parameters (OpenID4VP layer)) -> 1 Obbligo
  "tecnico/sicurezza", soggetto "Terza parte" (RP). I due punti elenco
  prescrivono i parametri obbligatori della richiesta: "response_type=vp_token
  and an appropriate response_mode (fragment, direct_post, or direct_post.jwt)
  per OpenID4VP" (vincolante in quanto specificazione dei parametri richiesti
  dal profilo) e "client_id, redirect_uri, state, nonce and dcql_query and
  transaction_data parameters shall be included as specified in OpenID4VP"
  ("shall" esplicito). Accorpati in un unico nodo: la clausola non ha
  numerazione interna.
- Annex A.6.3 (dcql_query (selecting an acceptable signing certificate)) -> 1
  Obbligo "tecnico/sicurezza", soggetto "Terza parte" (RP). Accorpa la
  prescrittiva della clausola: "The RP shall use the format identifier
  "https://cloudsignatureconsortium.org/2025/x509" and optionally constrain
  policies, keys, or fingerprints", "A request for proof of possession of an
  X.509 certificate shall include transaction_data for creating electronic
  signatures or seals using the queried certificate" e i due punti di
  "Requirements:" ("format identifier shall be
  https://cloudsignatureconsortium.org/2025/x509;", "parameters in the meta
  parameter in the credential query shall have x509MetadataQuery semantics
  (certificateFingerprints, certificatePolicies, keys) as defined in CSC data
  model binding [3] clause 8.1."). I due esempi non normativi di DCQL query
  restano dentro il nodo (clausola indivisibile, MAPPATURA_LOCALE 1:1) e sono
  riportati verbatim in `testo_integrale`, incluso il token base64url troncato
  dal testo ufficiale ("ew0KICAgICJ0eXBlIjogImh0dHBzOi8v...", dentro stringa
  quotata, esentato dalla guardia).
- Annex A.6.4 (transaction_data (the QES transaction)) -> 1 Obbligo
  "tecnico/sicurezza", soggetti "Terza parte" (RP, obbligato) e
  "Utente/titolare" (EUDIW, obbligato). Il nodo accorpa la struttura
  prescrittiva della clausola: "The parameter signatureRequests specifying an
  array of signatureRequest shall be included in the transaction data", "The
  parameter signatureQualifier shall be included in any signatureRequest object
  specifying the value "eu_eidas_qes"", "Any signatureRequest object shall
  include one of the following objects" (documentData o documentReference),
  "The parameter label should be specified in documentData and documentReference
  objects" e i punti di "Requirements:" (type shall be ...; signatureQualifier
  shall be present and shall indicate eu_eidas_qes ...; each signatureRequests
  shall be a CSC DM signatureRequest ...; Data URLs shall be supported ...;
  checksum parameter uses hash object syntax ...; credential_ids may appear ...;
  responseURI shall be included if an out-of-band POST is requested ...), oltre
  al requisito finale "The EUDIW shall render the OTP so the user can release
  the protected resource from the RP's channel", che sposta parte dell'obbligo
  sul portafoglio: da qui il secondo soggetto. L'esempio non normativo di
  transaction_data decodificata e' riportato verbatim.
- Annex A.7.1 (Inline (VP Token) - x509PresentationResponse) -> 1 Obbligo
  "tecnico/sicurezza", soggetto "Utente/titolare" (EUDIW). "If no responseURI
  is provided in the qesRequest, the EUDIW shall return signatures inline in
  the VP token response payload under the credential id, using qesResponse
  object as defined in CSC data model bindings [3] clause 6.2.2 with either
  documentWithSignature ... or signatureObject ...": e' il ramo di risposta
  inline del profilo, prescrizione sul portafoglio (il QTSP qui non e'
  soggetto). `condizione_applicabilita` valorizzata: si applica quando il
  qesRequest non contiene responseURI.
- Annex A.7.2 (Out of band (HTTP POST to responseURI)) -> 1 Obbligo
  "tecnico/sicurezza", soggetti "Utente/titolare" (EUDIW, obbligato: "the
  EUDIW shall POST a JSON qesResponse to that HTTPS endpoint, using HTTP/1.1
  and Content-Type: application/json, then return an empty presentation") e
  "Terza parte" (RP, obbligato: "The server should accept only the first
  successfully received response"). L'ultimo capoverso (response_mode=direct_post
  e direct_post.jwt) e' descrittivo ma appartiene alla stessa clausola indivisa.
  `condizione_applicabilita` valorizzata: si applica quando il qesRequest
  contiene responseURI.
- Annex A.7.3 (EUDIW processing) -> 1 Principio "altro". Deroga consapevole
  all'elenco del mandato di capitolo (che colloca A.7.x tra gli Obblighi): la
  clausola e' interamente descrittiva, priva di "shall"/"should" — "the wallet
  will authenticate the user, display a QES consent screen (with doc labels,
  OTPs, format/conformance, hash algorithm, etc.), and, upon consent, create the
  QES" usa il futuro descrittivo, e i sei passi "The EUDIW 1) ... 6)" sono un
  elenco di flusso all'indicativo presente; per il criterio ADR-0007 un elenco
  di flussi e' Principio, non Obbligo. L'esempio di richiesta GET /authorize?
  e' riportato verbatim, con i "..." autentici del testo ufficiale
  (state=0f0c8d6a..., nonce=8b4d2a67..., dcql_query={...},
  transaction_data=eyJ0eXBlIjoi...).
- Annex A.8 (Transaction data processing & UX rendering (EUDIW)) -> 1 Obbligo
  "tecnico/sicurezza", soggetto "Utente/titolare" (EUDIW). Tre prescrizioni sul
  portafoglio ("the EUDIW shall verify integrity and abort on mismatch", "the
  EUDIW shall abort", "The EUDIW should log transaction data and the user's
  approval/rejection") piu' il requisito di rendering ("EUDIW shall clearly
  render: the type (QES), the trust framework (eIDAS), whether Signature vs
  Seal, document labels, href (and whether integrity was verified), signature
  format/conformance level, and any signed attributes; and show responseURI").
  Il tenore dominante e' tecnico/di sicurezza (verifica di integrita' e
  interruzione della firma su mismatch); la parte di rendering e' trasparenza
  verso l'utente ma non ha numerazione propria e resta assorbita nello stesso
  nodo, senza aprire un secondo Obbligo "informativo/trasparenza" per una
  clausola indivisa.
- Annex A.9 (Complementary approval flow) -> 1 Principio "altro". "The SCSP AS
  may require a separate qesApproval bound to the transaction data. See Annex
  B.": facolta' del fornitore ("may require"), non prescrizione, e nessun
  soggetto obbligato; il rinvio all'Annex B e' citazione di un annesso che vive
  in un altro capitolo (cap07), quindi nessuna relazione emessa.
- Annex A.10 (Security & privacy requirements) -> 1 Obbligo
  "tecnico/sicurezza", soggetti "Terza parte" (RP), "Utente/titolare" (EUDIW) e
  "QTSP/gestore" (SCSP/SAM). Il primo punto e' prescrittivo su RP ed EUDIW ("if
  an RP transports a CSC DM signatureRequest as a JWT, it shall be signed and
  the EUDIW shall validate signature and issuer authorization"); i punti
  successivi enunciano regole di sicurezza in forma impersonale o dichiarativa
  (integrita' delle risorse con SHA-256 o superiore, verificata dall'EUDIW prima
  della firma; regole di codifica base64url per i parametri OpenID4VP e base64
  padded per gli elementi CSC API; formati e livelli di conformita' AdES
  secondo ETSI EN 319 102-1, con il server di firma che applica politiche e
  marche temporali secondo la configurazione del TSP; controllo esclusivo per EN
  419 241-1, con il SAM che valida provenienza e integrita' del SAD): la
  responsabilita' di enforcement ricade sul servizio di creazione della firma
  (QTSP/gestore), da cui il terzo soggetto.
- Annex A.11 (Conformance checklist (RP)) -> 1 Principio "altro". Checklist di
  conformita' per l'RP in cinque punti all'imperativo ("Use OpenID4VP
  authorization_request with vp_token response type and include dcql_query +
  transaction_data (qesRequest)", "Encode transaction_data as base64url of the
  JSON object; include signatureQualifier = eu_eidas_qes", "Provide documents by
  href + checksum (SRI); optionally access {type: "OTP"}", "Choose inline vs
  out-of-band by omitting or setting responseURI", "Constrain acceptable QCerts
  via dcql_query.meta (policies, keys, fingerprints)"): il criterio ADR-0007
  colloca espressamente le checklist di conformita' tra i Principi (nessun
  "shall" e nessun soggetto obbligato esplicito — sono criteri di
  auto-valutazione, non prescrizioni).
- Annex A.12.1 (Authorization request (core parameters)) -> 1 Principio "altro".
  Esempio non normativo di richiesta di autorizzazione completa (blocco HTTP con
  dcql_query e transaction_data in base64url): blocco illustrativo, quindi
  tipo_principio "altro" per gli esempi non normativi. Riportato verbatim, con
  le continuazioni base64url de-impaginate (le righe spezzate dal PDF sono
  ricomposte senza spazio, perche' continuano lo stesso token) e la dicitura
  "(Whitespace added for readability.)".
- Annex A.12.2 (Example 'qesRequest' (transaction_data before base64url
  encoding)) -> 1 Principio "altro". Esempio non normativo del qesRequest prima
  della codifica base64url, con le NOTE interne ("Notes & rules": modalita' di
  input by-reference/inline, modalita' di ritorno embedded/detached, TLS
  mutuamente autenticato raccomandato quando si usa responseURI). Contiene
  l'unico "?token=..." e i commenti "// OPTION A/B" del testo ufficiale.
- Annex A.12.3 (VP Token (inline) - PAdES result) -> 1 Principio "altro".
  Esempio non normativo di risultato PAdES consegnato inline nel VP Token.
- Annex A.12.4 (Out of band POST to responseURI) -> 1 Principio "altro".
  Esempio non normativo di POST fuori banda verso responseURI e nota che il
  Wallet restituisce una presentazione vuota al flusso OpenID4VP.

Copertura: 21 item di indice, uno per sottoclavola numerata con contenuto
proprio; le intestazioni di puro raggruppamento "Annex A (...)", A.5, A.6, A.7
e A.12 sono escluse (nessun testo proprio, solo titolo). Fuori perimetro per
costruzione: la clausola 7 (capitolo 5), l'Annex B e l'Annex C (capitolo 7),
l'Annex D informativo e la History.

Relazioni: due citazioni letterali interne al perimetro di questo capitolo,
entrambe risolvibili nel registro perche' i nodi di destinazione sono in questo
stesso modulo — A.6.4 richiama la clausola A.7.2 ("see clause A.7.2") e
l'esempio di A.7.3 richiama la clausola A.6.3 ("Base64url of the JSON object
from A.6.3"). I rinvii all'Annex B (A.4, A.5.2, A.9) NON generano relazioni: il
nodo di destinazione vive nel capitolo 7, non ancora registrato quando questo
capitolo viene inserito, e `inserisci_capitoli` solleva KeyError su una
relazione non risolvibile (i moduli capitolo non negoziano riferimenti
condivisi); la citazione resta comunque integralmente in `testo_integrale` e il
collegamento va costruito a posteriori (Fase 6 / ADR-0009). Nessuna relazione
cross-fonte in questa fase: demandata alla Fase 6.

Nota sui `...` e sulla normalizzazione: l'annesso contiene ellissi autentiche
del testo ufficiale dentro i payload di esempio (token base64url troncati in
A.6.3, `state=0f0c8d6a...`/`nonce=8b4d2a67...`/`dcql_query={...}`/
`transaction_data=...` in A.7.3, `?token=...` in A.12.2): sono riprodotte
letteralmente e la guardia `verifica_completezza_testo_integrale` le esenta.
Nessun troncamento di prosa. I `testo_integrale` sono copie letterali integrali
(nessuna NOTE o EXAMPLE omesso), con la sola normalizzazione degli spazi di
impaginazione: righe del PDF unite, "•" reso "-", i trattini che la conversione
PDF->testo ha spostato su una riga a parte per la sillabazione reimpaginata
nella parola di origine (es. "UTF-8", "out-of-band", "SHA-256", "EN 319 102-1",
"cross-device", "one-time password"), e gli header/footer di pagina
("ETSI", "<!-- Page N -->", "N ETSI TS 119 432 V1.3.1 (2026-03)") rimossi in
quanto paratesto spurio della conversione. I blocchi di esempio (JSON, HTTP)
conservano le interruzioni di riga del testo ufficiale, con le continuazioni
spezzate dal PDF ricomposte.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "Annex A.3 (Profile scope & transport)",
        "testo": (
            "Il profilo usa la Authorization Request / Response OAuth2 come definita da OpenID for "
            "Verifiable Presentations 1.0: nel flusso RP -> EUDIW un Request Object firmato (JAR) e' "
            "fornito a request_uri e l'EUDIW lo risolve dopo che l'utente apre un deep link o scansiona "
            "un codice QR; per invocare l'EUDIW puo' essere supportato lo schema URL personalizzato "
            "openid4vp://. Il valore del parametro response_type deve essere vp_token; il valore di "
            "response_mode dovrebbe essere direct_post o direct_post.jwt; l'RP deve restituire "
            "redirect_uri in risposta alla richiesta HTTP POST dell'EUDIW, dove l'EUDIW reindirizza "
            "l'utente (Sezione 8.2 di OpenID for Verifiable Presentations 1.0). La Authorization "
            "Request e' inviata con il parametro request_uri come definito in JWT-Secured Authorization "
            "Request (JAR) IETF RFC 9101 [31]; la DCQL query e i parametri di risposta sono definiti "
            "nella Sezione 6 di OpenID for Verifiable Presentations 1.0. Nel flusso EUDIW -> RP i "
            "valori response_mode=direct_post o direct_post.jwt sono usati per restituire vp_token (e "
            "le firme/risultati) in un corpo POST firmato."
        ),
        "testo_integrale": (
            "A.3 Profile scope & transport: The profile makes use of OAuth2 Authorization Request / "
            "Response as defined by OpenID for Verifiable Presentations 1.0. In the flow RP \u2192 "
            "EUDIW a signed Request Object (JAR) is provided at request_uri. EUDIW resolves it after "
            "the user opens a deep link or scans a QR code. In order to invoke the EUDIW, a custom URL "
            "scheme openid4vp:// may be supported in addition to other ways to invoke the EUDIW. The "
            "response_type parameter value shall be vp_token. The response_mode parameter value should "
            "be direct_post or direct_post.jwt. The RP shall return redirect_uri in response to the "
            "HTTP POST request from the EUDIW, where the EUDIW redirects the user to, as defined in "
            "Section 8.2 of OpenID for Verifiable Presentations 1.0. The Authorization Request is sent "
            "using the request_uri parameter as defined in JWT-Secured Authorization Request (JAR) "
            "IETF RFC 9101 [31]. The DCQL query and response parameters are defined in Section 6 of "
            "OpenID for Verifiable Presentations 1.0. In the flow EUDIW \u2192 RP the "
            "response_mode=direct_post or direct_post.jwt values are used to return vp_token (and the "
            "signatures/results) in a signed POST body."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.6.1 (Introduction)",
        "testo": (
            "L'RP deve usare OpenID4VP 1.0 e inviare una richiesta di autorizzazione OAuth/OIDC con i "
            "parametri specificati nelle sottoclavole seguenti del profilo."
        ),
        "testo_integrale": (
            "A.6.1 Introduction: The RP shall use OpenID4VP 1.0 and send an OAuth/OIDC authorization "
            "request with the parameters specified in the following sub-clauses."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.6.2 (Required parameters (OpenID4VP layer))",
        "testo": (
            "Parametri obbligatori del livello OpenID4VP: response_type=vp_token e un response_mode "
            "appropriato (fragment, direct_post o direct_post.jwt) secondo OpenID4VP; i parametri "
            "client_id, redirect_uri, state, nonce, dcql_query e transaction_data devono essere inclusi "
            "come specificato in OpenID4VP."
        ),
        "testo_integrale": (
            "A.6.2 Required parameters (OpenID4VP layer): - response_type=vp_token and an appropriate "
            "response_mode (fragment, direct_post, or direct_post.jwt) per OpenID4VP. - client_id, "
            "redirect_uri, state, nonce and dcql_query and transaction_data parameters shall be "
            "included as specified in OpenID4VP."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.6.3 (dcql_query (selecting an acceptable signing certificate))",
        "testo": (
            "L'RP deve usare l'identificatore di formato "
            "\"https://cloudsignatureconsortium.org/2025/x509\" e puo' facoltativamente vincolare "
            "politiche, chiavi o fingerprint; una richiesta di prova di possesso di un certificato "
            "X.509 deve includere transaction_data per creare firme o sigilli elettronici con il "
            "certificato interrogato. Requisiti: l'identificatore di formato deve essere "
            "https://cloudsignatureconsortium.org/2025/x509; i parametri dentro il parametro meta "
            "della credential query devono avere la semantica x509MetadataQuery "
            "(certificateFingerprints, certificatePolicies, keys) come definita nella clausola 8.1 di "
            "CSC data model binding [3]. Due esempi non normativi illustrano il vincolo sulle "
            "certificate policies e sui certificate fingerprints."
        ),
        "testo_integrale": (
            """A.6.3 dcql_query (selecting an acceptable signing certificate): The RP shall use the format identifier "https://cloudsignatureconsortium.org/2025/x509" and optionally constrain policies, keys, or fingerprints. A request for proof of possession of an X.509 certificate shall include transaction_data for creating electronic signatures or seals using the queried certificate.
A non-normative example DCQL query constraining certificate policies by using the X.509 credential format is:
{
    "dcql_query": {
         "credentials": [{
              "id": "xyz123",
              "format": "https://cloudsignatureconsortium.org/2025/x509",
              "meta": {
                  "certificatePolicies": ["0.4.0.2042.1", "0.4.0.194112.1"]
              }
         }]
    },
    "transaction_data": [
         "ew0KICAgICJ0eXBlIjogImh0dHBzOi8vY2xvdWRzaWduYXR1cmVjb25zb3J0aXVtLm9yZy8yMDI1Lw..."
    ]
}
Another non-normative example DCQL query constraining certificate fingerprints by using the X.509 credential format is:
{
    "dcql_query": {
         "credentials": [{
              "id": "xyz123",
              "format": "https://cloudsignatureconsortium.org/2025/x509",
              "meta": {
                  "certificateFingerprints": [{
                       "hashValue": "Jal8JexCNec2FBjKNGNM6WSiiE44NWjbvJBHav+vCXU=",
                       "hashAlgorithmOID": "2.16.840.1.101.3.4.2.1"
                  },
                  {
                       "hashValue": "ax8xsy0gdqyJtxmcw8xgZ85DbiC905oKdYBQspddxmk=",
                       "hashAlgorithmOID": "2.16.840.1.101.3.4.2.1"
                  }]
              }
         }]
    },
    "transaction_data": [
         "ew0KICAgICJ0eXBlIjogImh0dHBzOi8vY2xvdWRzaWduYXR1cmVjb25zb3J0aXVtLm9yZy8yMDI1Lw..."
    ]
}
Requirements:
- format identifier shall be https://cloudsignatureconsortium.org/2025/x509;
- parameters in the meta parameter in the credential query shall have x509MetadataQuery semantics (certificateFingerprints, certificatePolicies, keys) as defined in CSC data model binding [3] clause 8.1."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.6.4 (transaction_data (the QES transaction))",
        "testo": (
            "transaction_data e' una stringa JSON UTF-8 codificata in base64url il cui contenuto "
            "decodificato e' un oggetto qesRequest come definito nella clausola 6.2.1 di CSC data "
            "model bindings [3]; l'identificatore del tipo di dati di transazione per richiedere QES "
            "e' \"https://cloudsignatureconsortium.org/2025/qes\". Il parametro signatureRequests "
            "(array di signatureRequest) deve essere incluso nei dati di transazione; il parametro "
            "signatureQualifier deve essere incluso in ogni oggetto signatureRequest con valore "
            "\"eu_eidas_qes\" per indicare il trust framework applicabile; ogni oggetto "
            "signatureRequest deve includere documentData (clausola 8.1 di CSC DM) o "
            "documentReference (clausola 8.3 di CSC DM); il parametro label dovrebbe essere "
            "specificato in documentData e documentReference per fornire al titolare dell'EUDIW una "
            "descrizione leggibile del documento da firmare. Requisiti: type deve essere "
            "https://cloudsignatureconsortium.org/2025/qes; signatureQualifier deve essere presente e "
            "indicare eu_eidas_qes (o la variante appropriata) per le richieste di creazione di firme "
            "qualificate; ogni signatureRequests deve essere un signatureRequest CSC DM con semantica "
            "documentReference (href, access, checksum) o documentData (document, documentType) e "
            "includere la semantica adesParameters, con supporto dei Data URL (media type e "
            "dimensione possono essere limitati); il parametro checksum usa la sintassi hash object "
            "della clausola 7.4 di CSC DM; credential_ids puo' comparire per legare la transazione "
            "alla credenziale selezionata nella dcql_query (diverso dal credentialID della CSC API "
            "presso lo SCSP); responseURI deve essere incluso se e' richiesto un POST fuori banda "
            "(clausola A.7.2), altrimenti si attende la risposta inline nel VP Token. Il controllo di "
            "accesso opzionale contro lo shoulder surfing nei flussi cross-device usa una one-time "
            "password (OTP): l'EUDIW deve mostrare l'OTP cosi' che l'utente possa rilasciare la "
            "risorsa protetta dal canale dell'RP."
        ),
        "testo_integrale": (
            """A.6.4 transaction_data (the QES transaction): transaction_data is a base64url-encoded UTF-8 JSON string whose decoded content is a qesRequest object as defined in CSC data model bindings [3] clause 6.2.1.
The transaction data type identifier for requesting QES is "https://cloudsignatureconsortium.org/2025/qes".
The parameter signatureRequests specifying an array of signatureRequest shall be included in the transaction data.
The parameter signatureQualifier shall be included in any signatureRequest object specifying the value "eu_eidas_qes" in order to indicate the applicable trust framework.
Any signatureRequest object shall include one of the following objects:
- documentData as specified in clause 8.1 of CSC DM
- documentReference as specified in clause 8.3 of CSC DM
The parameter label should be specified in documentData and documentReference objects in order to provide a human-readable description of the document to be signed to the EUDIW holder.
The following is a non-normative example of a transaction_data after base64url decoding:
{
    "type": "https://cloudsignatureconsortium.org/2025/qes",
    "credential_ids": ["xyz123"],                   // optional, protocol-dependent
    "signatureRequests": [{
         "label": "Example Terms of Service",
         "access": { "type": "public" },
         "href": "https://public.rp-cdn.example/terms-and-conditions.pdf",
         "checksum": {
              "value": " HZQzZmMAIWekfGH0/ZKW1nsdt0xg3H6bZYztgsMTLw0=",
              "algorithmOID": "2.16.840.1.101.3.4.2.1"
         },
         "signature_format": "P",
         "conformance_level": "AdES-B-B",
         "signed_envelope_property": "Certification",
         "signAlgo": "1.2.840.113549.1.1.1",
         "signatureQualifier": "eu_eidas_qes",
         "responseURI": "https://example.com/signatureResponse/123/"
    }]
}
Requirements:
- type shall be https://cloudsignatureconsortium.org/2025/qes;
- signatureQualifier shall be present and shall indicate eu_eidas_qes (or the appropriate variant) for qualified signatures creation requests;
- each signatureRequests shall be a CSC DM signatureRequest with documentReference semantics (href, access, checksum) or documentData semantics (document, documentType) and include adesParameters semantics. Data URLs shall be supported; media types/size may be restricted;
- checksum parameter uses hash object syntax as defined in clause 7.4 of CSC DM;
- credential_ids may appear to bind the transaction to the credential selected in dcql_query (different from CSC API credentialID at SCSP);
- responseURI shall be included if an out-of-band POST is requested (see clause A.7.2). Otherwise, inline response in VP Token will be expected.
Access control (optional), to mitigate shoulder-surfing in cross-device flows, use one-time password (OTP):
"access": { "type": "OTP", "oneTimePassword": "51623" }
The EUDIW shall render the OTP so the user can release the protected resource from the RP's channel."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "Annex A.7.1 (Inline (VP Token) - x509PresentationResponse)",
        "testo": (
            "Se nel qesRequest non e' fornito alcun responseURI, l'EUDIW deve restituire le firme "
            "inline nel payload della risposta VP token sotto l'id della credenziale, usando l'oggetto "
            "qesResponse come definito nella clausola 6.2.2 di CSC data model bindings [3], con "
            "documentWithSignature quando la firma e' incorporata (es. PAdES) o signatureObject "
            "altrimenti, quando la firma e' detached. documentWithSignature si usa con firma "
            "incorporata, signatureObject altrimenti; i valori sono base64 (padded) per convenzione "
            "CSC API, anche se OpenID4VP usa tipicamente base64url."
        ),
        "testo_integrale": (
            """A.7.1 Inline (VP Token) - x509PresentationResponse: If no responseURI is provided in the qesRequest, the EUDIW shall return signatures inline in the VP token response payload under the credential id, using qesResponse object as defined in CSC data model bindings [3] clause 6.2.2 with either documentWithSignature, when the signature is embedded (e.g. PAdES), or signatureObject otherwise when the signature is detached.
The following is a non-normative example of a response from an EUDIW:
{
    "xyz123": {
        "qes": {
             "documentWithSignature": ["<base64-encoded document 1>", "<base64-encoded document 2>"]
        // or
        // "signatureObject": ["<base64-encoded detached signature>"]
        }
    }
}
documentWithSignature is used when the signature is embedded (e.g. PAdES), signatureObject otherwise. Values are base64 (padded) by CSC API convention (even though OpenID4VP typically uses base64url)."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Si applica quando il qesRequest non contiene il parametro responseURI (consegna inline "
            "delle firme nel VP Token)."
        ),
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.7.2 (Out of band (HTTP POST to responseURI))",
        "testo": (
            "Se il responseURI e' presente nel qesRequest, l'EUDIW deve fare POST di un qesResponse "
            "JSON a quell'endpoint HTTPS, usando HTTP/1.1 e Content-Type: application/json, e poi "
            "restituire una presentazione vuota; il server dovrebbe accettare solo la prima risposta "
            "ricevuta con successo. Se response_mode=direct_post e' impostato, l'EUDIW fa POST dei "
            "parametri di risposta; se invece e' impostato response_mode=direct_post.jwt, l'EUDIW fa "
            "comunque POST ma colloca tutti i parametri di risposta dentro un JWT firmato trasportato "
            "in un unico campo form denominato response."
        ),
        "testo_integrale": (
            """A.7.2 Out of band (HTTP POST to responseURI): If responseURI is present in the qesRequest, the EUDIW shall POST a JSON qesResponse to that HTTPS endpoint, using HTTP/1.1 and Content-Type: application/json, then return an empty presentation. Example response body:
{
    "documentWithSignature": ["<base64-encoded document>"]
}
The server should accept only the first successfully received response.
If response_mode=direct_post is set, the EUDIW POSTs response parameters. If, instead, response_mode=direct_post.jwt is set, the EUDIW still POSTs, but places all response parameters inside a signed JWT carried in a single form field named response."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Si applica quando il qesRequest contiene il parametro responseURI (POST fuori banda del "
            "qesResponse a quell'endpoint)."
        ),
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "Annex A.8 (Transaction data processing & UX rendering (EUDIW))",
        "testo": (
            "Elaborazione dei dati di transazione da parte dell'EUDIW: se un signatureRequest contiene "
            "sia href sia checksum, l'EUDIW deve verificare l'integrita' e interrompere in caso di "
            "mismatch; se un qesRequest referenzia una credenziale X.509 che non puo' produrre una QES "
            "per il signatureQualifier richiesto, l'EUDIW deve interrompere; l'EUDIW dovrebbe "
            "registrare i dati di transazione e l'approvazione/rifiuto dell'utente. L'EUDIW deve "
            "mostrare chiaramente: il tipo (QES), il trust framework (eIDAS), se si tratta di firma o "
            "sigillo, le etichette dei documenti, l'href (e se l'integrita' e' stata verificata), il "
            "formato/livello di conformita' della firma e gli eventuali attributi firmati, oltre a "
            "mostrare il responseURI."
        ),
        "testo_integrale": (
            """A.8 Transaction data processing & UX rendering (EUDIW): Processing
- If a signatureRequest contains both href and checksum, the EUDIW shall verify integrity and abort on mismatch.
- If a qesRequest references an X.509 credential that cannot produce a QES for the requested signatureQualifier, the EUDIW shall abort.
- The EUDIW should log transaction data and the user's approval/rejection.
EUDIW shall clearly render: the type (QES), the trust framework (eIDAS), whether Signature vs Seal, document labels, href (and whether integrity was verified), signature format/conformance level, and any signed attributes; and show responseURI."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.10 (Security & privacy requirements)",
        "testo": (
            "Requisiti di sicurezza e privacy: se un RP trasporta un signatureRequest CSC DM come JWT, "
            "esso deve essere firmato e l'EUDIW deve validare la firma e l'autorizzazione "
            "dell'emittente; il checksum deve usare l'integrita' delle risorse con SHA-256 o "
            "superiore, verificata dall'EUDIW prima della firma; i parametri OpenID4VP "
            "(transaction_data) sono codificati in base64url mentre gli elementi dati della CSC API "
            "interni restano base64 (padded); formati e livelli di conformita' AdES seguono ETSI EN 319 "
            "102-1, con il server di firma che applica politiche e marche temporali secondo la "
            "configurazione del TSP; il controllo esclusivo e' assicurato secondo EN 419 241-1 e il "
            "SAM valida provenienza e integrita' del SAD."
        ),
        "testo_integrale": (
            """A.10 Security & privacy requirements: - JWT signing and issuer validation: if an RP transports a CSC DM signatureRequest as a JWT, it shall be signed and the EUDIW shall validate signature and issuer authorization.
- Checksum: use resources integrity with SHA-256 or stronger; EUDIW verifies before signing.
- Encoding rules: OpenID4VP parameters (transaction_data) are base64url encoded; CSC API data elements inside remain base64 (padded).
- AdES: signature formats and conformance levels follow ETSI EN 319 102-1 [i.12]; server signing enforces policies, timestamps, etc., per TSP configuration.
- SAM & SAD: sole control is enforced per EN 419 241-1 [6]; SAM validates SAD provenance and integrity."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "Annex A.1 (Overview)",
        "testo": (
            "L'annesso definisce un profilo che descrive come un RP puo' richiedere la creazione di "
            "firme/sigilli elettronici qualificati (QES) a un portafoglio europeo di identita' "
            "digitale (EUDIW) che integra una Signature Creation Application, usando OpenID for "
            "Verifiable Presentations (OpenID4VP) e OpenID for Verifiable Credentials (OID4VC) [i.14] "
            "come protocolli di trasporto/interazione e CSC DM [2] e CSC data model bindings [3] per i "
            "dati di transazione e i risultati. Il profilo si concentra su: richieste (come l'RP "
            "formula una richiesta di firma QES verso l'EUDIW con dcql_query + transaction_data, "
            "vincolando facoltativamente le credenziali X.509 accettabili); risposte (come l'EUDIW "
            "restituisce le firme inline via VP Token o fuori banda a una responseURI); dati di "
            "transazione (strutture JSON richieste per qesRequest e, quando la Signature Activation "
            "Component gira lato server presso il TSP, il flusso complementare qesApproval). Il profilo "
            "presuppone l'elaborazione di firme AdES (PAdES/XAdES/CAdES/JAdES) secondo ETSI EN 319 "
            "102-1 [i.12]. Il flusso considerato prevede che la Relying Party (RP/Verifier) chieda "
            "all'EUDIW di creare una o piu' firme elettroniche, che l'EUDIW (portafoglio detenuto "
            "dall'utente) orchestra la creazione raccogliendo il consenso dell'utente, ottenendo le "
            "credenziali necessarie e chiamando un QTSP/servizio di creazione di firma remoto, e che "
            "l'EUDIW restituisca le firme prodotte (o i documenti firmati) all'RP nella authorization "
            "response OpenID4VP o a una responseURI. L'annesso copre solo l'interfaccia RP <-> EUDIW "
            "(richiesta + risposta): l'interazione interna EUDIW <-> QTSP e' fuori dal suo ambito. Una "
            "NOTE finale precisa che il flusso delineato non costituisce l'unico approccio possibile "
            "per implementare un processo di firma in cui si richiede a un EUDIW la creazione di QES e "
            "se ne ottiene la QES corrispondente."
        ),
        "testo_integrale": (
            "A.1 Overview: The present annex defines a profile describing how an RP can request the "
            "creation of qualified electronic signatures/seals (QES) from a European Digital Identity "
            "Wallet (EUDIW) that integrates a Signature Creation Application, using OpenID for "
            "Verifiable Presentations (OpenID4VP) and OpenID for Verifiable Credentials (OID4VC) "
            "[i.14] as the transport/interaction protocols, and the CSC DM [2] and CSC data model "
            "bindings [3] for transaction data and results. The profile focuses on: - Requests: how an "
            "RP formulates a QES signing request towards the EUDIW (dcql_query + transaction_data) and "
            "optionally constrains acceptable X.509 credentials. - Responses: how the EUDIW returns "
            "signatures inline (via VP Token) or out-of-band to a responseURI. - Transaction data: "
            "required JSON structures for qesRequest and, when the Signature Activation Component runs "
            "server-side at the TSP, the complementary qesApproval flow. This profile assumes AdES "
            "signature creation processing (PAdES/XAdES/CAdES/JAdES) per ETSI EN 319 102-1 [i.12]. The "
            "following flow is considered: - the Relying Party (RP/Verifier) asks the EUDIW to create "
            "one or more electronic signatures, - the EUDIW (user-held wallet) orchestrates signature "
            "creation, collects user consent, obtains any required credentials, calls a remote "
            "QTSP/signature creation service to create the signature(s), and - the EUDIW returns the "
            "produced signature(s) (or signed documents) to the RP in the OpenID4VP authorization "
            "response or to a responseURI. The profile defined in the present annex covers only the RP "
            "\u2194 EUDIW interface (request + response). The internal EUDIW \u2194 QTSP interaction is "
            "outside the scope of the profile defined in the present annex. NOTE: The flow outlined "
            "here does not constitute the only possible approach for implementing a signing process in "
            "which requesting to an EUDIW the creation of QES and obtaining the corresponding QES in "
            "response."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "firma elettronica qualificata",
            "sigillo elettronico qualificato",
        ],
    },
    {
        "riferimento": "Annex A.2 (Roles & Standards)",
        "testo": (
            "Ruoli e norme di riferimento del profilo. Relying Party (RP): verificatore che avvia una "
            "transazione di firma verso l'EUDIW, usa la richiesta di autorizzazione OpenID4VP con "
            "dcql_query e transaction_data, fornisce i documenti per riferimento con protezione "
            "dell'integrita' o come data URL e riceve le firme dall'EUDIW. EUDIW: implementa "
            "OpenID4VP, detiene o puo' ottenere una credenziale di firma X.509, presenta le "
            "credenziali, raccoglie il consenso, verifica l'integrita' dei documenti prima della firma, "
            "interagisce con un servizio remoto di creazione della firma via CSC API e restituisce le "
            "firme. Authorization Server (AS) / Signature Creation Service Provider (SCSP): esegue la "
            "firma server con un Signature Creation Device (SCDev/QSCD), applica le politiche di "
            "firma, espone la semantica della CSC API; il SAM puo' imporre il controllo esclusivo "
            "tramite Signature Activation Data (SAD). QTSP/SAM: servizio remoto di creazione della "
            "firma (binding JSON che riusa costrutti della CSC API), dichiarato fuori ambito. Il "
            "profilo si allinea all'EUDI Wallet Architecture and Reference Framework, che prevede la "
            "creazione di QES basata sul portafoglio e protocolli di presentazione interoperabili."
        ),
        "testo_integrale": (
            "A.2 Roles & Standards: - Relying Party (RP): verifier initiating a signature transaction "
            "to the EUDIW. Uses OpenID4VP authorization request with dcql_query and transaction_data. "
            "Provides documents by reference with integrity protection or as data URLs. Receives "
            "signatures from the EUDIW. - EUDIW: implements OpenID4VP; holds or may obtain an X.509 "
            "signing credential, presents credentials, captures consent, verifies documents integrity "
            "before signing, interacts with a remote signature creation service via CSC API and "
            "returns signatures. - Authorization Server (AS) / Signature Creation Service Provider "
            "(SCSP): runs server signing with Signature Creation Device (SCDev/QSCD); enforces "
            "signature policies; exposes CSC API semantics; the SAM may enforce sole control using "
            "Signature Activation Data (SAD). - QTSP/SAM (out of scope here): remote signature "
            "creation service (JSON binding reusing CSC API constructs). This profile aligns with the "
            "EUDI Wallet Architecture and Reference Framework, which foresees wallet-based QES "
            "creation and interoperable presentation protocols."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica qualificata"],
    },
    {
        "riferimento": "Annex A.4 (Profile identifiers)",
        "testo": (
            "Identificatori del profilo: tipo di dati di transazione per la richiesta QES "
            "(https://cloudsignatureconsortium.org/2025/qes); tipo di dati di transazione per "
            "l'approvazione QES (https://cloudsignatureconsortium.org/2025/qes-approval, si veda "
            "l'Annex B); identificatore del formato di credenziale X.509 in OID4VC/VP "
            "(https://cloudsignatureconsortium.org/2025/x509)."
        ),
        "testo_integrale": (
            "A.4 Profile identifiers: - Transaction data type for QES request: "
            "https://cloudsignatureconsortium.org/2025/qes - Transaction data type for QES approval: "
            "https://cloudsignatureconsortium.org/2025/qes-approval (see Annex B) - X.509 credential "
            "format identifier in OID4VC/VP: https://cloudsignatureconsortium.org/2025/x509"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica qualificata"],
    },
    {
        "riferimento": "Annex A.5.1 (EUDIW: RP \u2194 EUDIW, EUDIW \u2194 QTSP)",
        "testo": (
            "Modello di interazione in tre passi: 1) l'RP invia una Authorization Request OpenID4VP "
            "che include una dcql_query che seleziona le credenziali X.509 accettabili e "
            "transaction_data che trasporta qesRequest (JSON codificato in base64url); 2) l'EUDIW "
            "renderizza i dati di transazione, ottiene il consenso e interagisce con il servizio "
            "remoto di creazione della firma per creare le firme; 3) l'EUDIW restituisce inline le "
            "firme nel VP Token oppure le invia fuori banda alla responseURI fornita nella richiesta."
        ),
        "testo_integrale": (
            "A.5.1 EUDIW: RP \u2194 EUDIW, EUDIW \u2194 QTSP: 1) RP sends an OpenID4VP Authorization "
            "Request that includes: - a dcql_query selecting acceptable X.509 credentials, and - "
            "transaction_data carrying qesRequest (base64url-encoded JSON). 2) EUDIW renders "
            "transaction data, obtains consent, and interacts with the remote signature creation "
            "service to create the signatures. 3) EUDIW returns inline the signatures in the VP Token "
            "or posts out-of-band to the responseURI provided in the request."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica qualificata"],
    },
    {
        "riferimento": "Annex A.5.2 (QTSP: QTSP \u2194 EUDIW)",
        "testo": (
            "Flusso speculare in cui il QTSP (che eroga il servizio remoto di creazione della firma) "
            "chiede all'EUDIW di presentare un'attestazione che include qesApproval, legando "
            "crittograficamente l'approvazione ai dati di transazione; l'AS la usa per autorizzare la "
            "chiamata di firma CSC API (si veda l'Annex B)."
        ),
        "testo_integrale": (
            "A.5.2 QTSP: QTSP \u2194 EUDIW: The QTSP (providing remote signature creation service) "
            "requests the EUDIW to present an attestation that includes qesApproval, "
            "cryptographically binding approval to the transaction data; the AS uses it to authorize "
            "the CSC API signing call (see Annex B)."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica qualificata"],
    },
    {
        "riferimento": "Annex A.7.3 (EUDIW processing)",
        "testo": (
            "Elaborazione della richiesta da parte dell'EUDIW: dopo aver ricevuto la dcql_query e la "
            "stringa qesRequest codificata in base64url nella richiesta di autorizzazione OpenID4VP, "
            "il portafoglio autentica l'utente, mostra una schermata di consenso QES (con etichette "
            "dei documenti, OTP, formato/livello di conformita', algoritmo di hash, ecc.) e, previo "
            "consenso, crea la QES. Segue un esempio di richiesta GET /authorize? e l'elenco dei sei "
            "passi dell'EUDIW: risolve e verifica la JAR incluse le firme; se i documenti sono forniti "
            "per riferimento li recupera e ne verifica l'hash di integrita', calcolando il DTBSR per "
            "formato (es. PAdES ByteRange; definizioni DTBS/DTBSR secondo ETSI EN 319 102.1 [i.12]); "
            "mostra all'utente credenziali richieste, nome del documento e DTBSR (hash + algoritmo), "
            "formato/politica di firma e origine dell'RP, raccogliendo il consenso esplicito; presenta "
            "le credenziali come richiesto (DCQL) con OpenID4VP e internamente invoca il QTSP con gli "
            "hash (DTBSR) e i parametri di firma richiesti (politica/formato/algoritmo); post-elabora "
            "l'incorporamento PAdES se la modalita' di ritorno e' embedded, altrimenti mantiene il CMS "
            "detached; restituisce la Authorization Response OpenID4VP includendo le firme o i "
            "riferimenti ai risultati."
        ),
        "testo_integrale": (
            """A.7.3 EUDIW processing: After receiving the `dcql_query` and the base64url-encoded `qesRequest` string inside the OpenID4VP authorization request, the wallet will authenticate the user, display a QES consent screen (with doc labels, OTPs, format/conformance, hash algorithm, etc.), and, upon consent, create the QES.
GET /authorize?
    response_type=vp_token&
  client_id=https%3A%2F%2Frp.example%2Fclient&
  redirect_uri=https%3A%2F%2Frp.example%2Fcb&
  state=0f0c8d6a...&
  nonce=8b4d2a67...&
  // JSON-serialize the object from §3 and url-encode it as a single value
  dcql_query={...}&
  // Base64url of the JSON object from A.6.3
  transaction_data=eyJ0eXBlIjoiaHR0cHM6Ly9jbG91ZHNpZ25hdHVyZWNvbnNvcnR... HTTP/1.1
Host: wallet.example
The EUDIW
   1)   Resolves and verifies the JAR, including signatures.
   2)   If documents are provided by reference, fetches and verifies the integrity hash; computes DTBSR per format (e.g. PAdES ByteRange). (DTBS/DTBSR definitions according to ETSI EN 319 102.1 [i.12].)
   3)   Shows the user: requested credentials, each document name + DTBSR (hash + alg), signature format/policy, and the RP origin; captures explicit consent.
   4)   Presents credentials as requested (DCQL) using OpenID4VP and, internally, invokes the QTSP (as specified in the present document) with the hashes (DTBSRs) and the requested signature parameters (policy/format/alg).
   5)   Post processes PAdES embedding if return mode is embedded; otherwise keeps detached CMS.
   6)   Returns the OpenID4VP Authorization Response including signatures or result references."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica qualificata"],
    },
    {
        "riferimento": "Annex A.9 (Complementary approval flow)",
        "testo": (
            "Il flusso di approvazione complementare: l'AS dello SCSP puo' richiedere una qesApproval "
            "separata, legata ai dati di transazione (si veda l'Annex B)."
        ),
        "testo_integrale": (
            "A.9 Complementary approval flow: The SCSP AS may require a separate qesApproval bound to "
            "the transaction data. See Annex B."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica qualificata"],
    },
    {
        "riferimento": "Annex A.11 (Conformance checklist (RP))",
        "testo": (
            "Checklist di conformita' per l'RP in cinque punti: 1) usare la authorization_request "
            "OpenID4VP con response type vp_token e includere dcql_query + transaction_data "
            "(qesRequest); 2) codificare transaction_data in base64url dell'oggetto JSON e includere "
            "signatureQualifier = eu_eidas_qes; 3) fornire i documenti tramite href + checksum (SRI), "
            "facoltativamente con access {type: \"OTP\"}; 4) scegliere la consegna inline o fuori "
            "banda omettendo o impostando responseURI; 5) vincolare le QCerts accettabili tramite "
            "dcql_query.meta (politiche, chiavi, fingerprint)."
        ),
        "testo_integrale": (
            "A.11 Conformance checklist (RP): 1) Use OpenID4VP authorization_request with vp_token "
            "response type and include dcql_query + transaction_data (qesRequest). 2) Encode "
            "transaction_data as base64url of the JSON object; include signatureQualifier = "
            "eu_eidas_qes. 3) Provide documents by href + checksum (SRI); optionally access {type: "
            "\"OTP\"}. 4) Choose inline vs out-of-band by omitting or setting responseURI. 5) "
            "Constrain acceptable QCerts via dcql_query.meta (policies, keys, fingerprints)."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica qualificata"],
    },
    {
        "riferimento": "Annex A.12.1 (Authorization request (core parameters))",
        "testo": (
            "Esempio non normativo di richiesta di autorizzazione con i parametri principali: GET "
            "/authorize? con response_type=vp_token, client_id, redirect_uri, scope=openid, state, "
            "nonce, dcql_query e transaction_data codificati in base64url (gli spazi bianchi sono "
            "stati aggiunti per leggibilita')."
        ),
        "testo_integrale": (
            """A.12.1 Authorization request (core parameters): GET /authorize?
response_type=vp_token&
client_id=https%3A%2F%2Frp.example%2Fclient&
redirect_uri=https%3A%2F%2Frp.example%2Fcb&
scope=openid&state=af0ifjsldkj&nonce=n-0S6_WzA2Mj&
dcql_query=eyJjcmVkZW50aWFscyI6W3siaWQiOiJ4eXoxMjMiLCJmb3JtYXQiOiJodHRwczovL2Nsb3Vkc2lnbmF0dXJlY29uc29ydGl1bS5vcmcvMjAyNS94NTA5IiwibWV0YSI6eyJjZXJ0aWZpY2F0ZVBvbGljaWVzIjpbIjAuNC4wLjIwNDIuMSIsIjAuNC4wLjE5NDExMi4xIl19fV19&
transaction_data=ew0KICAidHlwZSI6ICJodHRwczovL2Nsb3Vkc2lnbmF0dXJlY29uc29ydGl1bS5vcmcvMjAyNS9xZXMiLA0KICAic2lnbmF0dXJlUmVxdWVzdHMiOiBbDQogICAgew0KICAgICAgImxhYmVsIjogIkV4YW1wbGUgVG9TIEp1bHktMjAyNSIsDQogICAgICAiYWNjZXNzIjogeyAidHlwZSI6ICJwdWJsaWMiIH0sDQogICAgICAiaHJlZiI6ICJodHRwczovL3B1YmxpYy5ycC1jZG4uZXhhbXBsZS90ZXJtcy1hbmQtY29uZGl0aW9ucy5wZGYiLA0KICAgICAgImNoZWNrc3VtIjogInNoYTI1Ni1IWlF6Wm1NQUlXZWtmR0gwL1pLVzFuc2R0MHhnM0g2YlpZenRnc01UTHcwPSIsDQogICAgICAic2lnbmF0dXJlX2Zvcm1hdCI6ICJQIiwNCiAgICAgICJjb25mb3JtYW5jZV9sZXZlbCI6ICJBZEVTLUItQiIsDQogICAgICAic2lnbmVkX2VudmVsb3BlX3Byb3BlcnR5IjogIkNlcnRpZmljYXRpb24iLA0KICAgICAgInNpZ25hdHVyZVF1YWxpZmllciI6ICJldV9laWRhc19xZXMiLA0KICAgICAgInNpZ25BbGdvIjogIjEuMi44NDAuMTEzNTQ5LjEuMS4xIg0KICAgIH0NCiAgXQ0KfQ

(Whitespace added for readability.)"""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica qualificata"],
    },
    {
        "riferimento": "Annex A.12.2 (Example 'qesRequest' (transaction_data before base64url encoding))",
        "testo": (
            "Esempio non normativo del qesRequest prima della codifica base64url, con due "
            "signatureRequest: il primo con documento per riferimento (href verso un PDF protetto con "
            "?token=..., checksum hash-like, accesso OTP) e il secondo con documento inline come data "
            "URL JSON in base64. Le NOTE e regole precisano le modalita' di input (by-reference: il "
            "Wallet recupera il documento e calcola da se' il DTBSR, con integrita' assicurata da "
            "sha256 sui byte recuperati; inline: payload grandi sconsigliati, e in tal caso fornire "
            "base64, mime e dimensione), le modalita' di ritorno (embedded: l'EUDIW restituisce il PDF "
            "con PAdES incorporato all'RP, per riferimento o inline; detached: l'EUDIW restituisce una "
            "firma CMS detached sul DTBSR, con politiche PAdES/XAdES/CAdES secondo ETSI EN 319 102-1 "
            "[i.12]) e che, quando si usa responseURI, il wallet invia la risposta qes a "
            "quell'endpoint, per cui si raccomanda TLS mutuamente autenticato."
        ),
        "testo_integrale": (
            """A.12.2 Example 'qesRequest' (transaction_data before base64url encoding): {
    "type": "https://cloudsignatureconsortium.org/2025/qes",
    "credential_ids": ["qes-cert-1"],
    "signatureRequests": [
    {
         "label": "Service Agreement #2025-09",
         // Integrity pinning via hash-like object checksum (base64)
         "checksum": {
              "value": "sTOgwOm+474gFj0q0x1iSNspKqbcse4IeiqlDg/HWuI=",
              "algorithmOID": "2.16.840.1.101.3.4.2.1"
         },
         // Access control to the document via OTP handshake (optional)
         "access": { "type": "OTP", "oneTimePassword": "51623" },
         // Where the wallet fetches the original document
         "href": "https://protected.rp.example/contracts/2025-09-01.pdf?token=...",
         "signature_format": "P",
         "conformance_level": "AdES-B-B",
         "signed_envelope_property": "Certification",
         "signatureQualifier": "eu_eidas_qes",
         "signAlgo": "1.2.840.113549.1.1.1"
    },
    {
         "label": "Annex A - JSON config",
         // Provide the object inline; wallet still verifies checksum
         "href": "data:application/json;base64,eyJleGFtcGxlS2V5IjoiZXhhbXBsZVZhbHVlIn0K",
         "signature_format": "J",
         "conformance_level": "AdES-B-B",
         "signed_envelope_property": "Attached",
         "signAlgo": "1.2.840.113549.1.1.1",
         "checksum": {
                 "value": "cuKv8Ee9H/rQsteQ1MQZ2Ld2ERXRkkulihFh3/XOXFQ=",
                 "algorithmOID": "2.16.840.1.101.3.4.2.1"
         },
         "signatureQualifier": "eu_eidas_qes"
         // OPTION A: inline delivery (omit responseURI) -> wallet returns QES inside vp_token
         // "responseURI": undefined
         // OPTION B: out-of-band delivery (recommended for large PDFs):
         // "responseURI": "https://rp.example/qes/receive"
         }]
}
Notes & rules:
- input mode:
- by-reference: the Wallet fetches the document and computes DTBSR itself; integrity is assured via sha256 over the fetched bytes;
- inline: large payloads discouraged; if used, provide base64, mime, size.
- return mode:
- embedded \u2192 EUDIW returns PAdES embedded PDF to the RP (by reference or inline);
- detached \u2192 EUDIW returns a detached CMS signature over DTBSR. (PAdES/XAdES/CAdES policies follow ETSI EN 319 102-1 [i.12]);
- when responseURI is used, the wallet POSTs the `qes` response to that endpoint, mutually authenticated TLS is recommended."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica qualificata"],
    },
    {
        "riferimento": "Annex A.12.3 (VP Token (inline) - PAdES result)",
        "testo": (
            "Esempio non normativo di risultato PAdES consegnato inline: nel VP Token, sotto l'id "
            "della credenziale (xyz123), l'oggetto qes contiene documentWithSignature con il PDF "
            "codificato in base64 e PAdES incorporato."
        ),
        "testo_integrale": (
            """A.12.3 VP Token (inline) - PAdES result: {
    "xyz123": {
         "qes": {
                 "documentWithSignature": ["<base64-encoded PDF with embedded PAdES>"]
         }
    }
}"""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica qualificata"],
    },
    {
        "riferimento": "Annex A.12.4 (Out of band POST to responseURI)",
        "testo": (
            "Esempio non normativo di POST fuori banda: POST /signatureResponse/123/ HTTP/1.1 verso "
            "rp.example con Content-Type: application/json e corpo contenente documentWithSignature "
            "con il PDF base64 con PAdES incorporato; il Wallet restituisce poi una presentazione "
            "vuota al flusso OpenID4VP."
        ),
        "testo_integrale": (
            """A.12.4 Out of band POST to responseURI: POST /signatureResponse/123/ HTTP/1.1
Host: rp.example
Content-Type: application/json
{
"documentWithSignature": ["<base64-encoded PDF with embedded PAdES>"]
}
The Wallet returns an empty presentation to the OpenID4VP flow."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica qualificata"],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Annex A.1 (Overview)",
    "Annex A.2 (Roles & Standards)",
    "Annex A.3 (Profile scope & transport)",
    "Annex A.4 (Profile identifiers)",
    "Annex A.5.1 (EUDIW: RP \u2194 EUDIW, EUDIW \u2194 QTSP)",
    "Annex A.5.2 (QTSP: QTSP \u2194 EUDIW)",
    "Annex A.6.1 (Introduction)",
    "Annex A.6.2 (Required parameters (OpenID4VP layer))",
    "Annex A.6.3 (dcql_query (selecting an acceptable signing certificate))",
    "Annex A.6.4 (transaction_data (the QES transaction))",
    "Annex A.7.1 (Inline (VP Token) - x509PresentationResponse)",
    "Annex A.7.2 (Out of band (HTTP POST to responseURI))",
    "Annex A.7.3 (EUDIW processing)",
    "Annex A.8 (Transaction data processing & UX rendering (EUDIW))",
    "Annex A.9 (Complementary approval flow)",
    "Annex A.10 (Security & privacy requirements)",
    "Annex A.11 (Conformance checklist (RP))",
    "Annex A.12.1 (Authorization request (core parameters))",
    "Annex A.12.2 (Example 'qesRequest' (transaction_data before base64url encoding))",
    "Annex A.12.3 (VP Token (inline) - PAdES result)",
    "Annex A.12.4 (Out of band POST to responseURI)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Due citazioni letterali interne al perimetro di questo capitolo, entrambe
# risolvibili nel registro perche' i nodi di destinazione sono in questo stesso
# modulo: A.6.4 richiama la clausola A.7.2 ("see clause A.7.2") e l'esempio di
# A.7.3 richiama la clausola A.6.3 ("Base64url of the JSON object from A.6.3").
# I rinvii all'Annex B (A.4, A.5.2, A.9) NON generano relazioni: il nodo di
# destinazione vive nel capitolo 7 (non ancora registrato quando questo capitolo
# viene inserito) e `inserisci_capitoli` solleva KeyError su una relazione non
# risolvibile. `confidence` resta None: non esiste uno score reale, non va
# inventato. Nessuna relazione cross-fonte in questa fase (Fase 6 / ADR-0009).
RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "Annex A.6.4 (transaction_data (the QES transaction))"),
        "nodo_a": ("obbligo", None, "Annex A.7.2 (Out of band (HTTP POST to responseURI))"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Annex A.7.3 (EUDIW processing)"),
        "nodo_a": ("obbligo", None, "Annex A.6.3 (dcql_query (selecting an acceptable signing certificate))"),
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
