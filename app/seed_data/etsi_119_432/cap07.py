"""ETSI TS 119 432 V1.3.1 (2026-03) - Electronic Signatures and Trust
Infrastructures (ESI); Protocols for remote digital signature creation.
Fonte 20 (la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 7:
Annex B (normative): EUDIW QES creation approval profile (B.1-B.12, con le
sottoclausole B.6.1-B.6.3 e B.8.1-B.8.2) e Annex C (normative): Specific
recommendations for qualified signatures and/or seals creation (C.1-C.7).
Documento unico (non multi-parte): i `riferimento` NON portano prefisso di
Parte. Testo ufficiale in app/.source_cache/etsi_119_432/cap07.txt (letto
sempre con selettore `:raw`, altrimenti il tool tronca le righe lunghe a 768
caratteri introducendo "..." e mutilando la copia verbatim). Manifest di
split: app/.source_cache/etsi_119_432/manifest.json.

Modellazione (ADR-0007), stesso criterio gia' applicato agli altri capitoli di
questa Fonte (cap01-cap03) e alle altre fonti ETSI censite: un nodo per ogni
clausola/sottoclavola numerata che porta contenuto proprio; le intestazioni di
puro raggruppamento non generano ne' nodo ne' item di indice. Questo capitolo
produce 15 Obblighi e 7 Principi su 22 item di indice. Scelte voce per voce:

- Annex B (normative): EUDIW QES creation approval profile -> NESSUN nodo
  "Annex B (...)" e nessun item: l'annesso e' interamente suddiviso in
  sottoclausole con numerazione propria (B.1-B.12), quindi la sua intestazione
  non porta contenuto autonomo. Il riferimento "Annex B (...)" sarebbe
  appropriato solo per un annesso non suddiviso.
- Clausola B.1 (Overview) -> 1 Principio "altro", oggetti_giuridici firma e
  sigillo elettronico qualificato, servizi di gestione a distanza del
  dispositivo di creazione e portafoglio europeo di identita' digitale.
  Clausola descrittiva: enuncia cosa specifica il profilo (come il servizio
  remoto di creazione di firme di un QTSP possa chiedere a un EUDIW
  l'approvazione alla creazione di QES/QSeal via OpenID4VP e binding CSC) e a
  quali documenti si allinea (CSC DM, EN 419 241-1, ETSI EN 319 102-1).
  Nessun verbo prescrittivo e nessun soggetto obbligato: e' presentazione di
  un profilo, non una prescrizione. "altro" e non "scopo/ambito di
  applicazione": non delimita cio' che il documento copre (quello sta nella
  clausola 1, censita in cap01), descrive il contenuto dell'annesso.
- Clausola B.2 (Roles and architecture) -> 1 Principio "altro". Elenca i tre
  ruoli del profilo (RSSP del QTSP in assetto RSSP-centric con AS+SAM davanti
  a un QSCD; EUDI Wallet come Driving Application; QSCD) e cosa fa ciascuno.
  Descrizione di architettura priva di soggetto obbligato, come B.1.
- Clausola B.3 (Signature authorization attestation) -> 1 Obbligo
  "tecnico/sicurezza", soggetto QTSP/gestore obbligato. Soggetto esplicito
  ("The QTSP managing SCS creates and issues this attestation") e verbo
  prescrittivo nella tabella delle claim ("purpose_of_use ... It shall be
  "signature creation authorization""). tipo_obbligo "tecnico/sicurezza": il
  contenuto prescrittivo e' la struttura e il binding crittografico
  dell'attestazione (claim minime, hash del certificato/SKID-AKID/hash della
  chiave pubblica, proof-of-possession), non un adempimento organizzativo ne'
  un obbligo informativo verso terzi.
- Clausola B.4 (Profile scope & transport) -> 1 Principio "altro". Voce di
  classificazione ambigua, risolta come da istruzione di capitolo
  (B.1/B.2/B.4/B.5/B.9/B.12 descrittive -> Principio "altro"). La clausola
  contiene due "shall" ("The response_type parameter value shall be vp_token";
  "The RP shall return redirect_uri in response to the HTTP POST request from
  the EUDIW") con soggetto identificabile (l'RP), che secondo il criterio
  generale sarebbero materia di Obbligo: il testo e' stato comunque censito
  come unico Principio "altro" perche' il tenore dominante della clausola e'
  la descrizione del profilo di trasporto (OAuth2 Authorization Request /
  Response di OpenID4VP 1.0, Request Object firmato JAR presso request_uri,
  schema custom openid4vp://) e i due "shall" citano vincoli gia' definiti dal
  protocollo OpenID4VP 1.0 (Section 8.2) e da JAR (IETF RFC 9101), non
  requisiti nuovi posti da questo documento. Resta un nodo unico perche' la
  clausola non ha numerazione interna.
- Clausola B.5 (Profile identifiers) -> 1 Principio "altro". Elenco
  descrittivo degli identificatori del profilo (tipo di transaction data
  qes-approval, nome del risultato qesApproval, identificatori di formato
  della credenziale). Nessun soggetto obbligato, nessun "shall".
- Clausola B.6 (Data model for approval) -> NESSUN nodo, NESSUN item di
  indice: intestazione di puro raggruppamento (il testo ufficiale passa
  direttamente dal titolo a "B.6.1 Introduction").
- Clausola B.6.1 (Introduction) -> 1 Obbligo "tecnico/sicurezza", soggetto
  QTSP/gestore obbligato: "The SCSP shall use OpenID4VP 1.0 and send an
  OAuth/OIDC authorization request with the parameters specified below". Lo
  SCSP e' il prestatore del servizio di creazione di firme -> categoria
  QTSP/gestore.
- Clausola B.6.2 (qesApprovalRequest) -> 1 Obbligo "tecnico/sicurezza",
  soggetto QTSP/gestore obbligato. Unita' indivisibile (nessuna numerazione
  interna) che accorpa: l'inclusione dell'oggetto qesApprovalRequest (CSC
  data model bindings clausola 7.1.1); l'inclusione di un oggetto
  signatureCreationApproval in ogni qesApprovalRequest (CSC DM clausola 10.1)
  con la diversa definizione di documentDigests come Array di unione di
  documentInfo e documentReference; l'associazione dei transaction data a una
  credenziale di approvazione identificata dal campo credential_ids; l'esempio
  non normativo di transaction_data e le NOTE 1-3. Il testo integrale riporta
  il blocco JSON con la sua impaginazione (il payload di esempio abbrevia
  legittimamente l'URL con "?token=..." - vedi sotto).
- Clausola B.6.3 (Computing qesApproval (EUDIW)) -> 1 Obbligo
  "tecnico/sicurezza", soggetto Utente/titolare obbligato. La clausola
  prescrive all'EUDIW il calcolo di qesApproval ("The EUDIW computes
  qesApproval = base64(hash(...))", con "Embedding depends on the approval
  credential format") e le due modalita' di inserimento per ISO/IEC 18013-5
  mdoc e SD-JWT VC. L'EUDIW e' il portafoglio dell'utente che agisce per il
  titolare della credenziale: il vocabolario chiuso non ha una categoria
  "portafoglio" e "Terza parte" lo rappresenterebbe scorrettamente come
  soggetto esterno all'utente, quindi la categoria usata e' "Utente/titolare"
  (stessa lettura per B.8.1 e B.10).
- Clausola B.7 (OpenID4VP request (QTSP -> Wallet)) -> 1 Obbligo
  "tecnico/sicurezza", soggetto QTSP/gestore obbligato (l'AS dello SCSP che
  agisce come Verifier). Prescrive i tre contenuti della richiesta
  (response_type=vp_token con scelta del response_mode; dcql_query che
  seleziona la credenziale di approvazione; transaction_data = base64url del
  JSON qesApprovalRequest) e include l'esempio decodificato.
- Clausola B.8 (EUDIW response (EUDIW -> QTSP)) -> NESSUN nodo, NESSUN item:
  intestazione di puro raggruppamento (passa direttamente a "B.8.1").
- Clausola B.8.1 (VP Token / DC API response) -> 1 Obbligo
  "tecnico/sicurezza", soggetti Utente/titolare obbligato (l'EUDIW che
  restituisce la presentazione con qesApproval, in DeviceResponse per ISO mdoc
  o con Key Binding JWT per SD-JWT VC) e QTSP/gestore obbligato (l'AS dello
  SCSP che valida la presentazione come Verifier ed estrae qesApproval).
  Entrambi i soggetti sono "obbligato": la clausola prescrive sia il formato
  della risposta sia la validazione, ciascuno in capo al proprio attore.
- Clausola B.8.2 (Using qesApproval at the AS/SCSP) -> 1 Obbligo
  "tecnico/sicurezza", soggetto QTSP/gestore obbligato: dopo la validazione
  l'AS verifica la corrispondenza del digest con l'esatto qesApprovalRequest
  inviato (sotto hashAlgorithmOID) e la corrispondenza del credentialID e
  dell'identita' utente con la credenziale del QSCD remoto e la policy, poi
  l'AS/SAM autorizza la firma.
- Clausola B.9 (Processing & rendering requirements (EUDIW)) -> 1 Principio
  "altro". Seconda voce di classificazione ambigua, risolta come da
  istruzione di capitolo. La clausola e' intitolata "requirements (EUDIW)" e
  contiene due prescrizioni in forma imperativa per l'EUDIW (cosa mostrare in
  fase di render; le tre condizioni di abort), che il criterio generale
  leggerebbe come Obbligo tecnico/sicurezza a carico del portafoglio. E'
  stata censita come Principio "altro" perche' l'istruzione di capitolo
  classifica espressamente B.9 tra le clausole descrittive e perche' il testo
  non usa alcun verbo modale prescrittivo ("shall"/"should"): enuncia
  requisiti di resa e condizioni di annullamento in forma di elenco
  descrittivo, senza la formula normativa usata altrove nel documento.
  Segnalato come scelta da riconciliare se la sessione principale preferisce
  il criterio sostanziale (presenza di un comportamento imposto) a quello
  formale (presenza del verbo modale).
- Clausola B.10 (Security & privacy) -> 1 Obbligo "tecnico/sicurezza",
  soggetti QTSP/gestore obbligato e Utente/titolare obbligato. Contiene due
  "shall" espliciti: se lo SCSP trasporta la richiesta di approvazione in un
  JWT "it shall be signed" (obbligo dello SCSP) e "the EUDIW shall validate
  signature and issuer authorization" (obbligo del portafoglio); le altre due
  voci (codifiche base64url/base64; controllo esclusivo via SAD e trusted
  path, uso di qesApproval entro validita' e scopo) ricadono su AS/SAM.
  La voce "Encodings" non ha un verbo modale ma e' interna a una clausola
  prescrittiva indivisibile e resta accorpata.
- Clausola B.11 (Conformance checklist (SCSP)) -> 1 Obbligo "procedurale",
  soggetto QTSP/gestore obbligato. E' una checklist numerata in quattro passi
  per lo SCSP (costruire la richiesta OpenID4VP con dcql_query; includere i
  transaction_data con signatureCreationApproval; validare la presentazione ed
  estrarre qesApproval vincolato ai byte esatti della richiesta; autorizzare
  lo step di firma sul QSCD presso l'AS/SAM solo se i binding corrispondono
  alla policy EN 419 241-1). tipo_obbligo "procedurale" e non
  "tecnico/sicurezza": il tenore della clausola e' la sequenza di passi del
  processo di conformita', non la specifica di un'interfaccia o di un
  meccanismo di sicurezza.
- Clausola B.12 (Working sequence) -> 1 Principio "altro". Sequenza di lavoro
  in quattro passi (richiesta AS -> EUDIW; resa e approvazione con calcolo di
  qesApproval; risposta EUDIW -> AS; validazione AS/SAM e chiamata al QSCD).
  E' la descrizione del flusso, non una prescrizione: nessun verbo modale,
  nessun soggetto obbligato. "altro" e non "scopo/ambito di applicazione".
- Annex C (normative): Specific recommendations for qualified signatures
  and/or seals creation -> NESSUN nodo "Annex C (...)" e nessun item:
  annesso interamente suddiviso in C.1-C.7.
- Clausola C.1 (Introduction) -> 1 Principio "altro": dichiara che l'annesso
  fornisce raccomandazioni formali per implementare flussi di creazione di QES
  assicurando la separazione tra livello di autenticazione/autorizzazione e
  livello dell'API di creazione della firma. Nessun verbo prescrittivo.
- Clausole C.2-C.7 -> 6 Obblighi "tecnico/sicurezza", soggetto QTSP/gestore
  obbligato. Sono raccomandazioni in forma "should" (forma raccomandatoria
  normativa): la scelta di modellarle come Obbligo e' la stessa gia' fatta per
  le "raccomandazioni" delle Regole Tecniche AgID 13/2/2020, perche' in uno
  standard ETSI "should" e' un verbo modale normativo che prescrive un
  comportamento a un soggetto identificabile (qui il prestatore del servizio
  di creazione di firme / il gestore dello SCS), non una descrizione. Il
  contenuto: C.2 autenticazione e autorizzazione fuori dallo SCS con
  meccanismi ad alta garanzia e SCS responsabile della sola creazione della
  firma nel QSCD remoto; C.3 il livello di autenticazione/autorizzazione
  implementa OAuth 2.0/OIDC con PAR, PKCE e private_key_jwt; C.4 lo SCS valida
  i token di autorizzazione e il binding dei DTBS; C.5 i token di
  autorizzazione incorporano hash dei DTBS, identificatori di credenziale e
  parametri di firma per non ripudio e anti-replay; C.6 quando l'EUDIW e'
  client OAuth si adottano i meccanismi FAPI 2.0 (private_key_jwt con chiavi
  WUA, PAR, mTLS/DPoP); C.7 le chiamate alle API dello SCS sono autenticate
  con access token OAuth, eventualmente con vincoli mTLS/DPoP, validando i
  nonce e imponendo oggetti di autorizzazione a uso singolo. In C.5 e C.7 il
  soggetto e' implicito nel possesso/uso dei token da parte del prestatore;
  resta QTSP/gestore obbligato.

Fuori perimetro (nessun nodo, nessun item di indice): Annex D (informative):
Change history, che e' una tabella storica delle versioni del documento
(1.1.1 marzo 2019, 1.1.2 giugno 2020, 1.2.13 febbraio 2026) con i CR
incorporati - contenuto informativo, non normativo, senza alcun precetto; e la
sezione History (tabella finale delle versioni pubblicate). Entrambe sono
paratesto di cronologia editoriale, come la clausola 2 (References) di cap01.
Annex A (normative): OpenID4VP EUDIW-centric signing flow profile non
appartiene a questo capitolo (coperto dal modulo cap06): nessun nodo e nessun
item di questo modulo lo riguarda.

Completezza verbatim (ADR-0010): i `testo_integrale` sono copie letterali
integrali delle clausole, con le sole normalizzazioni di impaginazione rese
necessarie dalla conversione PDF -> testo: righe unite in un unico flusso,
spazi multipli collassati, elenchi puntati resi con "- " (il "•" del PDF), la
tabella delle claim di B.3 ricostruita come coppie "claim: purpose" (riga di
intestazione compresa, resa come "Claim: Purpose"), e i
blocchi JSON di esempio (B.6.2, B.7, B.8.1) riprodotti con le loro
interruzioni di riga per preservare la struttura del payload. Sono stati
rimossi i soli header/footer di pagina ("ETSI", "<!-- Page N -->", "N ETSI TS
119 432 V1.3.1 (2026-03)"), paratesto spurio della conversione. I 13 trattini
non-breaking (U+2011) che la conversione PDF ha staccato dalla parola di
appartenenza e collocato su una riga propria sono stati riagganciati alla
parola corretta, verificando la posizione orizzontale del glifo sul PDF
(pdftotext -bbox): ne risultano le forme corrette "EN 419 241-1",
"(RSSP-centric)", "SD-JWT VC" (4 occorrenze), "EUDIW-local", "UTF-8" (2),
"ISO/IEC 18013-5", "top-level", "same-device" e "cross-device"; le frecce
staccate dal titolo/paragrafo di appartenenza sono state riagganciate
("RSSP → EUDIW" in B.4; "(QTSP → Wallet)" e "(EUDIW → QTSP)" nei titoli di
B.7/B.8, ripresi con la freccia "→" nei `riferimento`). I "..." presenti nel
payload di esempio di B.6.2 ("https://protected.example/doc-01.pdf?token=...")
sono contenuto autentico del testo ufficiale, non un'elisione
dell'estrazione: la guardia
`verifica_completezza_testo_integrale` li esenta (terza convenzione di
esenzione, ellissi dentro una stringa quotata). Nessun altro marcatore di
elisione e' presente nel capitolo; NOTE 1-3 di B.6.2 e tutte le NOTE/EXAMPLE
sono riportate integralmente.

`condizione_applicabilita`: valorizzata solo su C.6 ("quando l'EUDIW agisce
come client OAuth"), che condiziona l'intera raccomandazione (adozione dei
meccanismi FAPI 2.0). Non valorizzata altrove: le condizioni interne alle
altre clausole (es. "if the SCSP transports the approval request in a JWT" in
B.10) condizionano una singola sotto-prescrizione, non l'intera riga.

`stato`: "vigente" su tutte le righe (nessuna evidenza di abrogazione o di
transizione eIDAS->eIDAS2 in questo capitolo).

RELAZIONI interne: 1 relazione testuale, l'unica citazione letterale di una
clausola della stessa Fonte presente nel capitolo - B.7 rinvia a B.6.2
("include transaction_data = base64url (JSON qesApprovalRequest as in clause
B.6.2)"), modellata come "richiama" (rinvio a un nodo che resta vigente e non
viene incorporato ne' modificato). Tutti gli altri rinvii del capitolo sono a
documenti esterni (CSC data model bindings [3] clausole 7.1/7.1.1/8.1 e CSC
DM clausola 10.1, ETSI EN 419 241-1 [6], ETSI EN 319 102-1 [i.12], IETF RFC
9101 [31], Section 8.2 di OpenID for Verifiable Presentations 1.0) e non
generano relazioni interne. Il collegamento cross-fonte verso le altre 19
Fonti e' demandato alla Fase 6 della sessione principale (ADR-0009).
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "Annex B.3 (Signature authorization attestation)",
        "testo": (
            "L'attestazione di autorizzazione alla firma e' creata ed emessa dal QTSP che gestisce lo SCS e deve "
            "riportare almeno le claim raccomandate: iss (identificatore del QTSP), sub (identificatore "
            "pseudonimo del titolare del portafoglio, non il PID), purpose_of_use (che deve valere \"signature "
            "creation authorization\"), certificate_binding (riferimento al certificato o alla chiave di firma da "
            "usare), valid_for (una sola operazione di firma o un arco temporale limitato), aud (l'Authorization "
            "Server / Signing Service) e nonce/challenge (per prevenire il replay). L'attestazione garantisce il "
            "binding al certificato o alla chiave di firma con due modalita' raccomandate: (A) binding al "
            "certificato di firma, tramite hash del certificato (SHA 256), SKID/AKID o hash della chiave "
            "pubblica; (B) binding all'istanza del portafoglio (opzionale), con un elemento di "
            "proof-of-possession come le jwks usate nella WUA. Cio' impedisce l'inoltro o l'uso improprio."
        ),
        "testo_integrale": (
            "B.3 Signature authorization attestation: The QTSP managing SCS creates and issues this attestation. "
            "Recommended minimal claims: Claim: Purpose; iss: QTSP identifier; sub: Wallet holder pseudonymous "
            "identifier (NOT "
            "PID); purpose_of_use: It shall be \"signature creation authorization\"; certificate_binding: Reference "
            "to the signing certificate or key to be used; valid_for: One signing operation or limited timeframe; "
            "aud: The Authorization Server / Signing Service; nonce / challenge: Prevent replay\n"
            "It ensures binding to the certificate or signing key. Two recommended bindings: (A) Binding to the "
            "signing certificate including one of: - signing certificate hash (SHA 256) - SKID / AKID - public "
            "key hash (B) Binding to the wallet instance (optional) including a proof-of-possession element "
            "similar to: - jwks (as used in WUA) This prevents forwarding or misuse."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex B.6.1 (Introduction)",
        "testo": (
            "Lo SCSP deve usare OpenID4VP 1.0 e inviare una richiesta di autorizzazione OAuth/OIDC con i "
            "parametri specificati nelle sottoclausole seguenti."
        ),
        "testo_integrale": (
            "B.6.1 Introduction: The SCSP shall use OpenID4VP 1.0 and send an OAuth/OIDC authorization request "
            "with the parameters specified below."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex B.6.2 (qesApprovalRequest)",
        "testo": (
            "I transaction data con cui si richiede l'autorizzazione alla creazione di una firma devono includere "
            "l'oggetto qesApprovalRequest specificato in CSC data model bindings, clausola 7.1.1. Ogni oggetto "
            "qesApprovalRequest deve includere un oggetto signatureCreationApproval (CSC DM, clausola 10.1) che "
            "rappresenta le informazioni richieste al firmatario per prestare il consenso alla creazione della "
            "firma; a differenza di quanto stabilito nella clausola 10.1 di CSC DM, il parametro documentDigests "
            "e' definito come Array di unione di documentInfo e documentReference. L'identificatore del tipo di "
            "transaction data per l'approvazione di firme o sigilli qualificati (QES) e' "
            "\"https://cloudsignatureconsortium.org/2025/qes-approval\" e i transaction data devono essere "
            "associati a una credenziale di approvazione identificabile tramite il campo credential_ids (CSC data "
            "model bindings, clausola 7.1), ad esempio con un oggetto x509MetadataQuery (clausola 8.1). Il testo "
            "riporta l'esempio non normativo di transaction_data decodificato da base64url e le tre NOTE "
            "ufficiali (identificatore locale dell'EUDIW distinto dal credentialID dello SCSP; contenuto di "
            "signatureCreationApproval e ruolo di hashAlgorithmOID; semantica dei valori hashType sodr/dtbsr e "
            "del checksum di integrita' base64 con prefisso di algoritmo)."
        ),
        "testo_integrale": (
            "B.6.2 qesApprovalRequest: The transaction data for requesting authorization to a signature creation "
            "shall include the qesApprovalRequest object specified in CSC data model bindings [3], clause 7.1.1. "
            "A signatureCreationApproval object, specified in CSC DM clause 10.1, representing information "
            "required by the signer to give consent to a signature creation, shall be included in any "
            "qesApprovalRequest object. Differently from signatureCreationApproval object specification stated in "
            "CSC DM clause 10.1 the parameter documentDigests is defined as Array of union of documentInfo and "
            "documentReference. The transaction data type identifier for approving Qualified Electronic "
            "Signatures or seals (QES) is: \"https://cloudsignatureconsortium.org/2025/qes-approval\". The "
            "transaction data shall be associated with a credential for approval of QES creation that can be "
            "identified by a field credential_ids as specified in CSC data model bindings [3] clause 7.1. One way "
            "to identify the credential is an x509MetadataQuery object as specified in CSC data model bindings "
            "[3], clause 8.1. The following is a non-normative example of a transaction_data after base64url "
            "decoding\n"
            "{\n"
            "\"type\": \"https://cloudsignatureconsortium.org/2025/qes-approval\",\n"
            "\"credential_ids\": [\"xyz123\"],\n"
            "\"credentialID\": \"GX0112348\",\n"
            "\"signatureQualifier\": \"eu_eidas_qes\",\n"
            "\"numSignatures\": 2,\n"
            "\"documentDigests\": [{\n"
            "\"label\": \"Example Contract\",\n"
            "\"hash\": \"sTOgwOm+474gFj0q0x1iSNspKqbcse4IeiqlDg/HWuI=\",\n"
            "\"hashType\": \"sodr\",\n"
            "\"access\": { \"type\": \"OTP\", \"oneTimePassword\": \"51623\" },\n"
            "\"href\": \"https://protected.example/doc-01.pdf?token=...\",\n"
            "\"checksum\": {\n"
            "\"value\": \" HZQzZmMAIWekfGH0/ZKW1nsdt0xg3H6bZYztgsMTLw0=\",\n"
            "\"algorithmOID\": \"2.16.840.1.101.3.4.2.1\"\n"
            "}\n"
            "},\n"
            "{\n"
            "\"label\": \"Terms of Service\",\n"
            "\"hash\": \"HZQzZmMAIWekfGH0/ZKW1nsdt0xg3H6bZYztgsMTLw0=\",\n"
            "\"hashType\": \"sodr\",\n"
            "\"access\": { \"type\": \"public\" },\n"
            "\"href\": \"https://public.example/tos.pdf\",\n"
            "\"checksum\": {\n"
            "\"value\": \" HZQzZmMAIWekfGH0/ZKW1nsdt0xg3H6bZYztgsMTLw0=\",\n"
            "\"algorithmOID\": \"2.16.840.1.101.3.4.2.1\"\n"
            "}\n"
            "}],\n"
            "\"hashAlgorithmOID\": \"2.16.840.1.101.3.4.2.1\"\n"
            "}\n"
            "NOTE 1: credential_ids binds to an EUDIW-local identifier per OpenID4VP (distinct from the SCSP's "
            "credentialID). NOTE 2: signatureCreationApproval, defined in CSC DM, includes the QTSP credentialID "
            "(if known) or at least signatureQualifier, numSignatures, and an array of documentDigests with the "
            "digests and optional href/checksum/access for render and integrity checks. hashAlgorithmOID "
            "identifies the digest algorithm. NOTE 3: hashType values like sodr/dtbsr follow CSC DM semantics; "
            "integrity checksum is base64 and includes algorithm prefix per CSC DM."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex B.6.3 (Computing qesApproval (EUDIW))",
        "testo": (
            "L'EUDIW deve calcolare qesApproval come base64 dell'hash del qesApprovalRequest originale in UTF-8, "
            "usando l'algoritmo di hash indicato in hashAlgorithmOID della richiesta; la codifica dell'input "
            "dell'hash deve preservare il JSON UTF-8 originale (decodificando base64url se i transaction_data "
            "sono arrivati in quella forma). L'inserimento dipende dal formato della credenziale di approvazione: "
            "in ISO/IEC 18013-5 mdoc qesApproval va posto come data element DeviceSigned nel namespace "
            "org.cloudsignatureconsortium.dm.1, con identificatore qesApproval e valore di tipo bstr contenente "
            "il digest grezzo (senza base64 dentro il CBOR); in SD-JWT VC va incluso un claim di primo livello "
            "org.cloudsignatureconsortium.dm.1.qesApproval nel Key Binding JWT, con valore String (base64 del "
            "digest)."
        ),
        "testo_integrale": (
            "B.6.3 Computing qesApproval (EUDIW): - The EUDIW computes qesApproval = base64(hash(original UTF-8 "
            "qesApprovalRequest)); the hash algorithm is the request's hashAlgorithmOID. The encoding of hash "
            "input preserves the original UTF-8 JSON (decode base64url if transaction_data came that way). - "
            "Embedding depends on the approval credential format: - ISO/IEC 18013-5 mdoc [i.21]: put qesApproval "
            "as a DeviceSigned data element under namespace org.cloudsignatureconsortium.dm.1, identifier "
            "qesApproval, value type bstr of the raw digest (no base64 inside CBOR). - SD-JWT VC [i.13]: include "
            "a top-level claim org.cloudsignatureconsortium.dm.1.qesApproval in the Key Binding JWT; value is a "
            "String (base64 of the digest)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex B.7 (OpenID4VP request (QTSP → Wallet))",
        "testo": (
            "L'AS dello SCSP, agendo come Verifier, invia una richiesta di autorizzazione OpenID4VP: con "
            "response_type=vp_token e scelta del response_mode (fragment, direct_post o direct_post.jwt) a "
            "seconda che il flusso sia same-device o cross-device; includendo una dcql_query che seleziona la "
            "credenziale di approvazione da presentare (es. un'attestazione di servizio emessa all'utente che "
            "supporti qesApproval), eventualmente richiedendo i claim/doctype specifici necessari a veicolare "
            "qesApproval; includendo transaction_data = base64url del JSON qesApprovalRequest di cui alla "
            "clausola B.6.2. Il testo riporta l'esempio decodificato della richiesta, con la credenziale "
            "qscd_service_attestation e i claim userName, credentialID e qesApproval."
        ),
        "testo_integrale": (
            "B.7 OpenID4VP request (QTSP → Wallet): The SCSP's AS, acting as Verifier, sends an OpenID4VP "
            "authorization request: - response_type=vp_token; choose response_mode (fragment, direct_post, or "
            "direct_post.jwt) for same-device vs cross-device. - include dcql_query selecting the approval "
            "credential to be presented (e.g. a service attestation issued to the user that supports "
            "qesApproval). The query can request specific claims/doctype needed to carry qesApproval. - include "
            "transaction_data = base64url (JSON qesApprovalRequest as in clause B.6.2). Example (decoded)\n"
            "{\n"
            "\"dcql_query\": {\n"
            "\"credentials\": [{\n"
            "\"id\": \"qscd_service_attestation\",\n"
            "\"format\": \"mso_mdoc\",\n"
            "\"meta\": { \"doctype_value\": \"com.example.service.1.attestation\" },\n"
            "\"claims\": [\n"
            "{ \"path\": [\"com.example.service.1\", \"userName\"], \"values\": [\"willeke\"] },\n"
            "{ \"path\": [\"com.example.service.1\", \"credentialID\"], \"values\": [\"GX0112348\"] },\n"
            "{ \"path\": [\"org.cloudsignatureconsortium.dm.1\", \"qesApproval\"] }\n"
            "]\n"
            "}]\n"
            "},\n"
            "\"transaction_data\": [ \"<base64url of qesApprovalRequest JSON>\" ]\n"
            "}"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex B.8.1 (VP Token / DC API response)",
        "testo": (
            "L'EUDIW restituisce una presentazione verificabile contenente la credenziale di approvazione "
            "selezionata con qesApproval valorizzato: per ISO mdoc si tratta di una DeviceResponse, per SD-JWT VC "
            "della presentazione con un Key Binding JWT che include il claim "
            "org.cloudsignatureconsortium.dm.1.qesApproval. L'AS dello SCSP valida la presentazione come un "
            "normale Verifier ed estrae qesApproval. Il testo riporta l'esempio concettuale della risposta."
        ),
        "testo_integrale": (
            "B.8.1 VP Token / DC API response: The EUDIW returns a verifiable presentation containing the "
            "selected approval credential with qesApproval set. For ISO mdoc this is a DeviceResponse; for SD-JWT "
            "VC it is the presentation with a Key Binding JWT that includes the claim "
            "org.cloudsignatureconsortium.dm.1.qesApproval. Example (conceptual)\n"
            "{\n"
            "\"qscd_service_attestation\": [\n"
            "\"<base64url-encoded DeviceResponse or SD-JWT VC presentation with qesApproval>\"]\n"
            "}\n"
            "The SCSP's AS validates the presentation like a normal Verifier and extracts qesApproval."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "Annex B.8.2 (Using qesApproval at the AS/SCSP)",
        "testo": (
            "Dopo la validazione, l'AS verifica che il digest contenuto in qesApproval coincida con l'hash "
            "dell'esatto qesApprovalRequest inviato, secondo hashAlgorithmOID, e che il credentialID e "
            "l'identita' utente vincolati nella credenziale di approvazione corrispondano alla credenziale del "
            "QSCD remoto e alla policy di destinazione; l'AS/SAM autorizza quindi la firma (es. CSC API "
            "signatures/signHash o signatures/signDoc)."
        ),
        "testo_integrale": (
            "B.8.2 Using qesApproval at the AS/SCSP: After successful validation, the AS verifies: - The digest "
            "in qesApproval equals hash (the exact qesApprovalRequest it sent) under hashAlgorithmOID. - The "
            "bound credentialID/user identity in the approval credential matches the targeted remote QSCD "
            "credential and policy. Then the AS/SAM authorizes the signature (e.g. CSC API signatures/signHash or "
            "signatures/signDoc)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex B.10 (Security & privacy)",
        "testo": (
            "Sicurezza e privacy: se lo SCSP trasporta la richiesta di approvazione in un JWT, questo deve essere "
            "firmato e l'EUDIW deve validarne la firma e l'autorizzazione dell'emittente; i transaction_data "
            "esterni sono codificati in base64url mentre il checksum di integrita' e gli eventuali elementi "
            "binari definiti da CSC DM restano base64 (con padding); l'AS/SAM deve imporre il controllo esclusivo "
            "tramite SAD e trusted path e usare qesApproval solo entro la sua validita' e per lo scopo previsto."
        ),
        "testo_integrale": (
            "B.10 Security & privacy: - JWT/issuer: if the SCSP transports the approval request in a JWT, it "
            "shall be signed; the EUDIW shall validate signature and issuer authorization. - Encodings: "
            "transaction_data outer is base64url encoded; integrity checksum and any binary items defined by CSC "
            "DM remain base64 (padded). - AS/SAM: enforce sole control via SAD and trusted path; use qesApproval "
            "only within its lifetime/purpose."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "Annex B.11 (Conformance checklist (SCSP))",
        "testo": (
            "Checklist di conformita' per lo SCSP: 1) costruire la richiesta OpenID4VP con una dcql_query che "
            "chiede una credenziale di approvazione (doctype/claim che supportino qesApproval); 2) includere "
            "transaction_data = base64url(JSON) del qesApprovalRequest con signatureCreationApproval (etichette, "
            "hash, hashAlgorithmOID, conteggi); 3) validare la presentazione restituita ed estrarre qesApproval "
            "vincolato ai byte esatti della richiesta; 4) autorizzare lo step di firma sul QSCD presso l'AS/SAM "
            "solo se qesApproval e i binding utente/credenziale corrispondono alla policy (EN 419 241-1)."
        ),
        "testo_integrale": (
            "B.11 Conformance checklist (SCSP): 1) Build OpenID4VP request with dcql_query asking for an approval "
            "credential (doctype/claims supporting qesApproval). 2) Include transaction_data = base64url(JSON) of "
            "qesApprovalRequest with signatureCreationApproval (labels, hashes, hashAlgorithmOID, counts). 3) "
            "Validate the returned presentation and extract qesApproval bound to the exact bytes of the request. "
            "4) Authorize the QSCD signing step at the AS/SAM only if qesApproval and user/credential bindings "
            "match policy (EN 419 241-1 [6])."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex C.2 (Separation of Responsibilities)",
        "testo": (
            "L'autenticazione e l'autorizzazione dovrebbero essere eseguite all'esterno dello SCS con meccanismi "
            "ad alta garanzia (es. OAuth 2.0, OIDC, FAPI 2.0); lo SCS e' responsabile esclusivamente della "
            "creazione della firma all'interno del QSCD remoto gestito dal QTSP."
        ),
        "testo_integrale": (
            "C.2 Separation of Responsibilities: Authentication and authorization should be performed outside the "
            "SCS using high-assurance mechanisms (e.g. OAuth 2.0, OIDC, FAPI 2.0). The SCS is responsible "
            "exclusively for signature creation within the remote QSCD operated by the QTSP."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex C.3 (Authentication and Authorization Layer)",
        "testo": (
            "Il livello di autenticazione/autorizzazione responsabile della verifica dell'identita' dell'utente "
            "dovrebbe implementare OAuth 2.0/OIDC con PAR e PKCE e i meccanismi di autenticazione "
            "private_key_jwt."
        ),
        "testo_integrale": (
            "C.3 Authentication and Authorization Layer: The authentication/authorization layer responsible for "
            "user identity verification should implement OAuth 2.0/OIDC with PAR and PKCE, and private_key_jwt "
            "authentication mechanisms."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex C.4 (Signature Creation Service)",
        "testo": (
            "Lo SCS che fornisce operazioni standardizzate di elenco delle credenziali, recupero delle "
            "informazioni sulle credenziali, autorizzazione delle credenziali e creazione della firma dovrebbe "
            "validare i token di autorizzazione e il binding dei DTBS."
        ),
        "testo_integrale": (
            "C.4 Signature Creation Service: The SCS that provides standardized operations for credential "
            "listing, credential information retrieval, credential authorization, and signature creation should "
            "validate authorization tokens and DTBS binding."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex C.5 (Strong Binding Between Consent and DTBS)",
        "testo": (
            "I token di autorizzazione dovrebbero incorporare gli hash specifici dei DTBS, gli identificatori "
            "delle credenziali e i parametri di firma, per garantire il non ripudio e prevenire gli attacchi di "
            "replay."
        ),
        "testo_integrale": (
            "C.5 Strong Binding Between Consent and DTBS: Authorization tokens should embed specific DTBS hashes, "
            "credential identifiers and signature parameters to ensure non-repudiation and prevent replay "
            "attacks."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex C.6 (Use of FAPI 2.0 for EUDIW-Based Clients)",
        "testo": (
            "Quando l'EUDIW agisce come client OAuth, dovrebbero essere adottati i meccanismi FAPI 2.0: "
            "private_key_jwt con le chiavi della WUA, PAR per l'integrita' della richiesta e mTLS/DPoP per access "
            "token vincolati al mittente."
        ),
        "testo_integrale": (
            "C.6 Use of FAPI 2.0 for EUDIW-Based Clients: When the EUDIW acts as the OAuth client, FAPI 2.0 "
            "mechanisms should be adopted: private_key_jwt with WUA keys, PAR for request integrity, and "
            "mTLS/DPoP for sender-constrained access tokens."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "quando l'EUDIW agisce come client OAuth (\"When the EUDIW acts as the OAuth client\")",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex C.7 (SCS API Security Recommendations)",
        "testo": (
            "Tutte le chiamate alle API dello SCS dovrebbero essere autenticate con access token OAuth, "
            "eventualmente con vincoli mTLS o DPoP, validando i nonce e imponendo oggetti di autorizzazione a uso "
            "singolo."
        ),
        "testo_integrale": (
            "C.7 SCS API Security Recommendations: All SCS API calls should be authenticated using OAuth access "
            "tokens, possibly following mTLS or DPoP constraints, validating nonces, and enforcing one-time-use "
            "authorization objects."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "Annex B.1 (Overview)",
        "testo": (
            "Questo profilo specifica come il servizio remoto di creazione di firme di un QTSP possa chiedere a "
            "un EUDI Wallet (EUDIW) l'approvazione alla creazione di una firma o di un sigillo elettronico "
            "qualificato, usando OpenID for Verifiable Presentations (OpenID4VP) e i binding del data model CSC. "
            "Definisce richieste, risposte e la struttura transaction_data che vincola il consenso dell'utente ai "
            "dati concreti da firmare e all'operazione sul QSCD remoto o alla credenziale di destinazione. Il "
            "profilo si allinea a: CSC DM, per l'oggetto signatureCreationApproval, i digest dei documenti, il "
            "tipo di transaction data https://cloudsignatureconsortium.org/2025/qes-approval e la componente "
            "qesApproval; EN 419 241-1 (SAM, SAD e controllo esclusivo) come baseline architetturale del QSCD "
            "remoto, con l'approvazione usata da AS/SAM per autorizzare la firma; ETSI EN 319 102-1 per le "
            "procedure di creazione e validazione AdES richiamate dalle policy del QTSP."
        ),
        "testo_integrale": (
            "B.1 Overview: This profile specifies how a QTSP's remote signature creation service can request "
            "approval for Qualified Electronic Signature/Seal creation from an EUDI Wallet (EUDIW) using the "
            "OpenID for Verifiable Presentations (OpenID4VP) protocol and the CSC data model bindings [3]. It "
            "defines requests, responses, and the transaction_data structure that binds the user's consent to "
            "concrete data to be signed and to the target credential/remote QSCD operation. It aligns with: - CSC "
            "DM, for signatureCreationApproval object and document digests, and CSC data model bindings [3] "
            "defining https://cloudsignatureconsortium.org/2025/qes-approval transaction data type identifier and "
            "qesApproval data component. - EN 419 241-1 [6] (SAM, SAD and sole control) as architectural baseline "
            "for remote QSCD; the approval is used by the AS/SAM to authorize the signature. - ETSI EN 319 102-1 "
            "[i.12] for AdES creation/validation procedures referenced by QTSP policies."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "firma elettronica qualificata",
            "sigillo elettronico qualificato",
            "servizio di gestione di dispositivo di creazione di firma elettronica a distanza",
            "servizio di gestione di dispositivo di creazione di sigillo elettronico a distanza",
            "portafoglio europeo di identità digitale",
        ],
    },
    {
        "riferimento": "Annex B.2 (Roles and architecture)",
        "testo": (
            "Ruoli e architettura del profilo: il Remote Signing Server del QTSP, in assetto RSSP-centric, esegue "
            "Authorization Server (AS) e SAM davanti a un QSCD; l'AS e' il Verifier in OpenID4VP e chiede "
            "all'EUDIW la presentazione di una credenziale contenente QES Approval, il SAM usa il token ottenuto "
            "con il codice fornito dall'AS dopo la validazione di qesApproval per autorizzare l'operazione sulla "
            "chiave, e il QTSP crea ed emette l'attestazione la cui presentazione e' richiesta all'EUDIW per "
            "autorizzare la creazione di firme. L'EUDI Wallet agisce come Driving Application: riceve la "
            "richiesta di approvazione (OpenID4VP), rende i transaction data, raccoglie il consenso dell'utente e "
            "restituisce una presentazione che incorpora qesApproval nel formato della credenziale (ISO mdoc o "
            "SD-JWT VC). Il QSCD esegue l'operazione con la chiave privata una volta che il SAM ha validato "
            "l'approvazione e i vincoli di policy."
        ),
        "testo_integrale": (
            "B.2 Roles and architecture: - QTSP Remote Signing Server (RSSP-centric): runs Authorization Server "
            "(AS) + SAM in front of a QSCD. The AS is the Verifier in OpenID4VP and asks the EUDIW for a "
            "presentation of a credential containing QES Approval. The SAM uses the token obtained with the code "
            "provided by the AS after successful validation of qesApproval to authorize the key operation. The "
            "QTSP creates and issues the attestation whose presentation is requested to EUDIW to authorize "
            "signatures creation. - EUDI Wallet (Driving Application): receives the approval request (OpenID4VP), "
            "renders the transaction data, collects user consent, and returns a presentation embedding "
            "qesApproval per credential format (ISO mdoc or SD-JWT VC). - QSCD: Performs the private key "
            "operation once the SAM validates the approval and policy constraints."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "servizio di gestione di dispositivo di creazione di firma elettronica a distanza",
            "portafoglio europeo di identità digitale",
        ],
    },
    {
        "riferimento": "Annex B.4 (Profile scope & transport)",
        "testo": (
            "Il profilo usa la OAuth2 Authorization Request / Response come definita da OpenID for Verifiable "
            "Presentations 1.0. Nel flusso RSSP -> EUDIW un Request Object firmato (JAR) e' fornito presso "
            "request_uri e l'EUDIW lo risolve dopo che l'utente ha aperto un deep link o scansionato un codice "
            "QR; per invocare l'EUDIW puo' essere supportato anche uno schema URL personalizzato openid4vp://. Il "
            "valore del parametro response_type deve essere vp_token, il valore di response_mode dovrebbe essere "
            "direct_post o direct_post.jwt, e l'RP deve restituire redirect_uri in risposta alla richiesta HTTP "
            "POST dell'EUDIW (come definito nella Section 8.2 di OpenID for Verifiable Presentations 1.0). "
            "L'Authorization Request e' inviata con il parametro request_uri come definito in JWT-Secured "
            "Authorization Request (JAR), IETF RFC 9101."
        ),
        "testo_integrale": (
            "B.4 Profile scope & transport: The profile makes use of OAuth2 Authorization Request / Response as "
            "defined by OpenID for Verifiable Presentations 1.0. In the flow RSSP → EUDIW a signed Request Object "
            "(JAR) is provided at request_uri. EUDIW resolves it after the user opens a deep link or scans a QR "
            "code. In order to invoke the EUDIW, a custom URL scheme openid4vp:// may be supported in addition to "
            "other ways to invoke the EUDIW. The response_type parameter value shall be vp_token. The "
            "response_mode parameter value should be direct_post or direct_post.jwt. The RP shall return "
            "redirect_uri in response to the HTTP POST request from the EUDIW, where the EUDIW redirects the user "
            "to, as defined in Section 8.2 of OpenID for Verifiable Presentations 1.0. The Authorization Request "
            "is sent using the request_uri parameter as defined in JWT-Secured Authorization Request (JAR) IETF "
            "RFC 9101 [31]."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["portafoglio europeo di identità digitale"],
    },
    {
        "riferimento": "Annex B.5 (Profile identifiers)",
        "testo": (
            "Identificatori del profilo: il tipo di transaction data di approvazione e' "
            "https://cloudsignatureconsortium.org/2025/qes-approval (qesApprovalRequest); il nome del risultato "
            "dell'approvazione e' qesApproval (un digest hash codificato in base64 e vincolato alla richiesta "
            "originale); gli identificatori del formato della credenziale che porta qesApproval sono, ad esempio, "
            "ISO mdoc o SD-JWT VC come definiti in CSC data model bindings."
        ),
        "testo_integrale": (
            "B.5 Profile identifiers: - Approval transaction data type: "
            "https://cloudsignatureconsortium.org/2025/qes-approval (qesApprovalRequest). - Approval result name: "
            "qesApproval (a base64-encoded hash digest bound to the original request). - Credential format "
            "identifiers (for the presented credential carrying qesApproval), e.g. ISO mdoc or SD-JWT VC as "
            "defined in CSC data model bindings [3]."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["attestato elettronico di attributi", "portafoglio europeo di identità digitale"],
    },
    {
        "riferimento": "Annex B.9 (Processing & rendering requirements (EUDIW))",
        "testo": (
            "Requisiti di elaborazione e di resa grafica per l'EUDIW: mostrare se si tratta di QES o di sigillo, "
            "il trust framework (eIDAS), le etichette dei documenti, l'href e se l'integrita' (checksum) e' stata "
            "verificata, nonche' l'OTP se presente per consentire all'utente di sbloccare le risorse protette; "
            "annullare l'operazione se il controllo di integrita' dell'hash fallisce, se il numero di elementi "
            "differisce da numSignatures o se il signatureQualifier richiesto non puo' essere prodotto con la "
            "credenziale di approvazione e il QSCD remoto disponibili."
        ),
        "testo_integrale": (
            "B.9 Processing & rendering requirements (EUDIW): - Render: Show QES vs Seal, trust framework "
            "(eIDAS), document labels, href, and whether integrity (checksum) was verified; show OTP if present "
            "so the user can release protected resources. - Abort if: hash integrity check fails, number of items "
            "differs from numSignatures, or the requested signatureQualifier cannot be produced with the approval "
            "credential/remote QSCD."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["portafoglio europeo di identità digitale"],
    },
    {
        "riferimento": "Annex B.12 (Working sequence)",
        "testo": (
            "Sequenza di lavoro: 1) l'AS dello SCSP invia all'EUDIW l'Authorization Request OpenID4VP con "
            "dcql_query (attestazione di servizio) e transaction_data (qes-approval); 2) l'EUDIW rende i dati, "
            "l'utente approva, l'EUDIW calcola qesApproval e produce la presentazione; 3) l'EUDIW restituisce "
            "all'AS dello SCSP la VP/DeviceResponse con qesApproval; 4) l'AS/SAM valida la presentazione, "
            "verifica qesApproval e chiama il QSCD (es. CSC API signatures/signHash e/o signatures/signDoc) per "
            "creare la QES."
        ),
        "testo_integrale": (
            "B.12 Working sequence: 1) SCSP AS → EUDIW: OpenID4VP Authorization Request with dcql_query (service "
            "attestation) + transaction_data (qes-approval). 2) EUDIW: Renders data, user approves; computes "
            "qesApproval; produces presentation. 3) EUDIW → SCSP AS: VP/DeviceResponse with qesApproval. 4) "
            "AS/SAM: Validates presentation; verifies qesApproval; calls QSCD (e.g. CSC API signatures/signHash "
            "and/or signatures/signDoc) to create the QES."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "firma elettronica qualificata",
            "servizio di gestione di dispositivo di creazione di firma elettronica a distanza",
            "portafoglio europeo di identità digitale",
        ],
    },
    {
        "riferimento": "Annex C.1 (Introduction)",
        "testo": (
            "L'annesso fornisce raccomandazioni formali per implementare flussi di creazione di firma elettronica "
            "qualificata (QES), assicurando una chiara separazione tra il livello di "
            "autenticazione/autorizzazione e il livello dell'API di creazione della firma."
        ),
        "testo_integrale": (
            "C.1 Introduction: This annex provides formal recommendations for implementing Qualified Electronic "
            "Signature (QES) creation workflows, while ensuring a clear separation between the "
            "authentication/authorization layer and the signature creation API layer."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica qualificata"],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Annex B.1 (Overview)",
    "Annex B.2 (Roles and architecture)",
    "Annex B.3 (Signature authorization attestation)",
    "Annex B.4 (Profile scope & transport)",
    "Annex B.5 (Profile identifiers)",
    "Annex B.6.1 (Introduction)",
    "Annex B.6.2 (qesApprovalRequest)",
    "Annex B.6.3 (Computing qesApproval (EUDIW))",
    "Annex B.7 (OpenID4VP request (QTSP → Wallet))",
    "Annex B.8.1 (VP Token / DC API response)",
    "Annex B.8.2 (Using qesApproval at the AS/SCSP)",
    "Annex B.9 (Processing & rendering requirements (EUDIW))",
    "Annex B.10 (Security & privacy)",
    "Annex B.11 (Conformance checklist (SCSP))",
    "Annex B.12 (Working sequence)",
    "Annex C.1 (Introduction)",
    "Annex C.2 (Separation of Responsibilities)",
    "Annex C.3 (Authentication and Authorization Layer)",
    "Annex C.4 (Signature Creation Service)",
    "Annex C.5 (Strong Binding Between Consent and DTBS)",
    "Annex C.6 (Use of FAPI 2.0 for EUDIW-Based Clients)",
    "Annex C.7 (SCS API Security Recommendations)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Unica citazione letterale interna alla stessa Fonte presente nel capitolo: B.7 rinvia
# a B.6.2 ("include transaction_data = base64url (JSON qesApprovalRequest as in clause
# B.6.2)") -> relazione "richiama", evidence_type "textual". Tutti gli altri rinvii del
# capitolo puntano a documenti esterni (CSC data model bindings [3], CSC DM, ETSI EN 419
# 241-1 [6], ETSI EN 319 102-1 [i.12], IETF RFC 9101 [31], OpenID for Verifiable
# Presentations 1.0) e non generano relazioni interne. Il collegamento cross-fonte e'
# demandato alla Fase 6 della sessione principale (ADR-0009).
RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "Annex B.7 (OpenID4VP request (QTSP → Wallet))"),
        "nodo_a": ("obbligo", None, "Annex B.6.2 (qesApprovalRequest)"),
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
