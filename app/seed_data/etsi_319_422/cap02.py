"""ETSI EN 319 422 V1.1.1 (2016-03) - Electronic Signatures and Trust
Infrastructures (ESI); Time-stamping protocol and time-stamp token profiles.
Fonte 19 (la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 2:
clausola 4 (Requirements for a time-stamping client: 4.1 Profile for the
format of the request -> 4.1.1 Core requirement, 4.1.2 Fields to be
supported, 4.1.3 Hash algorithms to be used; 4.2 Profile for the format of
the response -> 4.2.1 Core requirement, 4.2.2 Fields to be supported, 4.2.3
Algorithms to be supported, 4.2.4 Key lengths to be supported) e clausola 5
(Requirements for a time-stamping server: 5.1 Profile for the format of the
request -> 5.1.1 Core requirement, 5.1.2 Fields to be supported, 5.1.3
Algorithms to be supported; 5.2 Profile for the format of the response ->
5.2.1 Core requirement, 5.2.2 Fields to be supported, 5.2.3 Algorithms to be
used). Testo ufficiale in app/.source_cache/etsi_319_422/cap02.txt (letto
sempre con selettore `:raw`, altrimenti il tool tronca le righe lunghe a 768
caratteri introducendo "…" e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_319_422/manifest.json.

Modellazione (ADR-0007), stesso criterio gia' applicato alle fonti ETSI gia'
censite (ETSI TS 119 461, ETSI EN 319 401, ETSI EN 319 412, ETSI TS 119 431,
ETSI EN 319 411, ETSI EN 319 421) e adattato a uno standard tecnico
"profiling": ETSI EN 319 422 non introduce requisiti organizzativi propri, ma
profila il protocollo di marcatura temporale IETF RFC 3161 (con
l'aggiornamento RFC 5816) fissando per il client e per il server di marcatura
temporale quali messaggi, campi e algoritmi devono o dovrebbero essere
supportati. Ogni sottoclasse numerata di questo capitolo porta quindi un
requisito proprio (shall/should/is required), ed e' modellata come un Obbligo:
13 Obblighi, 0 Principi. Le intestazioni di puro raggruppamento non generano
nodo ne' item di indice: clausola 4 ("Requirements for a time-stamping
client", titolo di capitolo senza testo proprio), clausola 5 (idem per il
server), clausola 4.1 ("Profile for the format of the request", solo titolo),
clausola 4.2 ("Profile for the format of the response", solo titolo),
clausola 5.1 e clausola 5.2 (idem). Scelte voce per voce:

- Clausola 4.1.1 (Core requirement) -> 1 Obbligo "tecnico/sicurezza", soggetto
  "Utente/titolare" (obbligato). Prescrive con "shall" che il time-stamping
  client supporti la time-stamping request come definita in IETF RFC 3161 [1],
  clausola 2.4.1, con gli emendamenti delle clausole seguenti: e' la
  prescrizione di conformazione del messaggio di richiesta lato client.
- Clausola 4.1.2 (Fields to be supported) -> 1 Obbligo "tecnico/sicurezza",
  soggetto "Utente/titolare". Requisito su campi del protocollo (reqPolicy,
  nonce, certReq) formulato con "should be supported": prescrizione di
  supporto di campi tecnici, non di processo organizzativo. Il valore
  prescrittivo attenuato ("should") non muta la classificazione obbligo/
  principio (il criterio e' la presenza di un verbo prescrittivo che impone un
  comportamento a un soggetto identificabile, non la forza shall/should):
  stesso trattamento gia' riservato alle clausole "should" delle fonti ETSI
  gia' censite.
- Clausola 4.1.3 (Hash algorithms to be used) -> 1 Obbligo
  "tecnico/sicurezza", soggetto "Utente/titolare". Rinvia per valore a ETSI TS
  119 312 [i.5] clausola A.8 (suite crittografiche) e alla clausola 9.2 dello
  stesso (confronto funzioni di hash / tempo), con la NOTE ufficiale che
  ammette la supremazia di raccomandazioni nazionali sulle suite: la NOTE
  delimita il valore del rinvio, quindi e' assorbita in `testo_integrale` (non
  e' bibliografia decorativa).
- Clausola 4.2.1 (Core requirement) -> 1 Obbligo "tecnico/sicurezza", soggetto
  "Utente/titolare". Speculare a 4.1.1 sul lato risposta: la time-stamping
  response definita in IETF RFC 3161 [1], clausola 2.4.2, con gli emendamenti
  seguenti.
- Clausola 4.2.2 (Fields to be supported) -> 1 Obbligo "tecnico/sicurezza",
  soggetto "Utente/titolare". Accorpa tre prescrizioni sulla risposta lato
  client: il campo accuracy "shall be supported", il campo nonce "should be
  supported", e il divieto per i client di dipendere dall'ordinamento delle
  marche temporali ("clients should not depend on the ordering of
  time-stamps", motivato dal fatto che una TSU non e' tenuta a supportare
  ordering), con l'eccezione del nonce riflesso nella risposta con lo stesso
  valore quando presente nella richiesta ("shall be present in the response
  with the same value"). NOTA di tracciabilita' per la sessione principale:
  quest'ultima frase ha come soggetto grammaticale il produttore della
  risposta (il time-stamping server/TSU), non il client; e' stata comunque
  registrata sotto l'unico soggetto "Utente/titolare" perche' la clausola vive
  nel profilo dei requisiti del client (clausola 4) e descrive cio' che il
  client deve poter assumere della risposta. Se in Fase 6 si volesse
  rappresentare la doppia imputazione (client e server obbligati sulla stessa
  frase), la riga e' quella da rivedere: nel grafo attuale non esiste un
  secondo soggetto su questa riga.
- Clausola 4.2.3 (Algorithms to be supported) -> 1 Obbligo
  "tecnico/sicurezza", soggetto "Utente/titolare". Rinvio per valore alla
  clausola A.8 di ETSI TS 119 312 [i.5] per gli algoritmi di firma del token
  di marca temporale, con NOTE ufficiale sulle raccomandazioni nazionali
  assorbita.
- Clausola 4.2.4 (Key lengths to be supported) -> 1 Obbligo
  "tecnico/sicurezza", soggetto "Utente/titolare". Rinvio per valore alla
  clausola 9.3 di ETSI TS 119 312 [i.5] per le lunghezze delle chiavi
  dell'algoritmo di firma selezionato, con NOTE ufficiale assorbita.
- Clausola 5.1.1 (Core requirement) -> 1 Obbligo "tecnico/sicurezza", soggetto
  "QTSP/gestore" (obbligato): il time-stamping server (il gestore del servizio
  di marcatura temporale, cioe' la TSA/TSU) deve supportare la richiesta come
  definita in IETF RFC 3161 [1], clausola 2.4.1, con gli emendamenti seguenti.
  Simmetrica a 4.1.1 ma con soggetto obbligato diverso: la stessa clausola di
  RFC 3161 e' profilata separatamente per client e server, quindi le due righe
  restano nodi distinti (non duplicati) perche' diverso e' il soggetto tenuto
  al comportamento.
- Clausola 5.1.2 (Fields to be supported) -> 1 Obbligo "tecnico/sicurezza",
  soggetto "QTSP/gestore". A differenza della simmetrica 4.1.2, qui i tre campi
  (reqPolicy, nonce, certReq) sono tutti con "shall be supported": il profilo
  server e' piu' stringente del profilo client.
- Clausola 5.1.3 (Algorithms to be supported) -> 1 Obbligo
  "tecnico/sicurezza", soggetto "QTSP/gestore". Rinvio per valore alla
  clausola A.8 di ETSI TS 119 312 [i.5] per gli algoritmi di hash dei dati da
  marcare, con il criterio della durata attesa della marca temporale
  (clausola 9.2 di ETSI TS 119 312 [i.5]) e NOTE ufficiale assorbita.
- Clausola 5.2.1 (Core requirement) -> 1 Obbligo "tecnico/sicurezza", soggetto
  "QTSP/gestore": la risposta come definita in IETF RFC 3161 [1], clausola
  2.4.2, con gli emendamenti seguenti.
- Clausola 5.2.2 (Fields to be supported) -> 1 Obbligo "tecnico/sicurezza",
  soggetto "QTSP/gestore". E' la clausola piu' densa del capitolo: richiama in
  blocco i requisiti della clausola 2.4.2 di IETF RFC 3161 [1] ("shall apply")
  e vi aggiunge (a) policy presente come identificatore della time-stamp policy
  e conformita' all'annex A; (b) genTime con valore temporalmente preciso
  quanto basta all'accuracy dichiarata; (c) accuracy presente con minimo di un
  secondo; (d) ordering assente o false; (e) nessuna estensione marcata
  critica; (f) sul contenuto della struttura SignedData che incapsula TSTInfo,
  l'identificatore del certificato della TSU (ESSCertID / ESSCertIDv2) incluso
  come attributo signerInfo in SigningCertificate / SigningCertificateV2 ai
  sensi di IETF RFC 5816 [4], clausola 2.2.1. Classificata "tecnico/sicurezza":
  si e' valutato "procedurale" per il solo punto (a) (conformita' della policy
  dichiarata a un formato prescritto) e "di conservazione" per il solo punto
  (f) (riferimento al certificato di firma), ma entrambi sono vincoli
  strutturali sul contenuto del token/risposta, non fasi di un processo ne'
  regole di conservazione documentale; la clausola e' un unico requisito di
  conformazione tecnica del messaggio di risposta e resta "tecnico/sicurezza".
  I due rinvii interni ("annex A", "clausola 2.4.2") sono rinvii di clausola,
  non citazioni di requirement id (questo standard numera i requisiti con la
  sola numerazione di clausola, non con identificatori TIS-xx), quindi non
  generano relazioni (vedi sotto).
- Clausola 5.2.3 (Algorithms to be used) -> 1 Obbligo "tecnico/sicurezza",
  soggetto "QTSP/gestore". Rinvio per valore alla clausola A.8 di ETSI TS 119
  312 [i.5] per entrambe le famiglie di algoritmi (hash dei dati da marcare e
  firma del token), con NOTE ufficiale assorbita.

Classificazione `tipo_obbligo`: tutte e 13 le voci sono "tecnico/sicurezza".
Motivo: ogni voce di questo capitolo e' un requisito di conformazione tecnica
di un protocollo (quali strutture ASN.1, quali campi, quali algoritmi, quali
lunghezze di chiave devono essere supportati) o un rinvio per valore a una
raccomandazione di suite crittografiche. Nessuna voce impone un processo
organizzativo, un adempimento informativo/trasparente verso terzi, una
procedura di gestione ne' una modalita' di conservazione: "procedurale",
"organizzativo", "informativo/trasparenza", "di conservazione" e
"sanzionatorio" sono stati considerati e scartati per ciascuna voce (il caso
limite 5.2.2 e' argomentato nella voce sopra).

Soggetti: per la clausola 4 (profilo del client) il soggetto obbligato e'
"Utente/titolare" (il time-stamping client, cioe' il richiedente della marca
temporale, ruolo "obbligato"); per la clausola 5 (profilo del server) e'
"QTSP/gestore" (il time-stamping server / TSA / TSU, ruolo "obbligato").
Nessun soggetto compare con ruolo "destinatario" in questo capitolo: tutte le
prescrizioni impongono un comportamento al soggetto che le subisce, non
proteggono un terzo.

Rinvii per valore e rinvii di clausola (nessuna RELAZIONE in questo capitolo):
le clausole 4.1.3, 4.2.3, 4.2.4, 5.1.3 e 5.2.3 rinviano per valore a ETSI TS
119 312 [i.5] (clausola A.8 e clausola 9.2/9.3), che e' uno standard esterno
citato come informativo, non una fonte censita nel grafo: nessuna relazione.
La clausola 5.2.2 richiama la clausola 2.4.2 di IETF RFC 3161 [1] e conformita'
all'annex A dello stesso ETSI EN 319 422 (annex A vive nel capitolo 4 di
questa stessa fonte): e' un rinvio di clausola, non una citazione letterale di
un identificatore di requisito, e l'assegnazione di questo capitolo fissa
`RELAZIONI` a vuoto. L'eventuale collegamento va costruito a posteriori
(Fase 6 / ADR-0009) dalla sessione principale. `RELAZIONI = []`.

Copertura: 13 item di indice, uno per sottoclasse numerata con contenuto
proprio; intestazioni 4, 4.1, 4.2, 5, 5.1, 5.2 escluse (nessun testo proprio,
solo titolo), coerentemente con la copertura aggregata verificata
programmaticamente da `inserisci_capitoli` (ogni item di indice deve essere
coperto esattamente una volta su tutti i capitoli della fonte).
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 4.1.1 (Core requirement)",
        "testo": (
            "Il time-stamping client deve supportare la richiesta di marca temporale (time-stamping request) "
            "cosi' come definita nella clausola 2.4.1 di IETF RFC 3161 [1], con gli emendamenti stabiliti "
            "dalle clausole seguenti del presente documento."
        ),
        "testo_integrale": (
            "4.1.1 Core requirement: A time-stamping client shall support the time-stamping request as "
            "defined in IETF RFC 3161 [1], clause 2.4.1 with the amendments defined in the following clauses."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.1.2 (Fields to be supported)",
        "testo": (
            "L'uso dei seguenti campi nella richiesta di marca temporale dovrebbe essere supportato dal "
            "time-stamping client: il reqPolicy, il nonce e il certReq."
        ),
        "testo_integrale": (
            "4.1.2 Fields to be supported: The use of the following fields in the time-stamping request "
            "should be supported: - the reqPolicy; - the nonce; and - the certReq."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.1.3 (Hash algorithms to be used)",
        "testo": (
            "Gli algoritmi di hash usati per calcolare l'impronta dell'informazione da marcare temporalmente "
            "dovrebbero essere quelli specificati nella clausola A.8 di ETSI TS 119 312 [i.5], tenendo conto "
            "della durata attesa della marca temporale e del confronto tra le funzioni di hash selezionate e "
            "il tempo indicato nella clausola 9.2 di ETSI TS 119 312 [i.5]; le raccomandazioni sulle suite "
            "crittografiche ivi definite possono essere superate da raccomandazioni nazionali."
        ),
        "testo_integrale": (
            "4.1.3 Hash algorithms to be used: Hash algorithms used to hash the information to be "
            "time-stamped should be as specified in clause A.8 of ETSI TS 119 312 [i.5]. This should take "
            "into account the expected duration of the time-stamp and selected hash functions versus time "
            "given in clause 9.2 of ETSI TS 119 312 [i.5]. NOTE: Cryptographic suites recommendations "
            "defined in ETSI TS 119 312 [i.5] can be superseded by national recommendations."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.1 (Core requirement)",
        "testo": (
            "Il time-stamping client deve supportare la risposta di marca temporale (time-stamping response) "
            "cosi' come definita nella clausola 2.4.2 di IETF RFC 3161 [1], con gli emendamenti stabiliti "
            "dalle clausole seguenti del presente documento."
        ),
        "testo_integrale": (
            "4.2.1 Core requirement: A time-stamping client shall support the time-stamping response as "
            "defined in IETF RFC 3161 [1], clause 2.4.2 with the amendments defined in the following clauses."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.2 (Fields to be supported)",
        "testo": (
            "Il time-stamping client deve supportare il campo accuracy della risposta e dovrebbe supportare "
            "il campo nonce; poiche' una TSU non e' tenuta a supportare l'ordinamento, i client non "
            "dovrebbero dipendere dall'ordine delle marche temporali, e se il campo nonce e' presente nella "
            "richiesta il campo nonce deve essere presente nella risposta con lo stesso valore."
        ),
        "testo_integrale": (
            "4.2.2 Fields to be supported: The following requirements apply: - the accuracy field shall be "
            "supported; and - the nonce field should be supported. A TSU needs not support ordering hence "
            "clients should not depend on the ordering of time-stamps. If the nonce field is present in the "
            "request, the nonce field shall be present in the response with the same value."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.3 (Algorithms to be supported)",
        "testo": (
            "Gli algoritmi di firma del token di marca temporale da supportare dovrebbero essere quelli "
            "specificati nella clausola A.8 di ETSI TS 119 312 [i.5]; le raccomandazioni sulle suite "
            "crittografiche ivi definite possono essere superate da raccomandazioni nazionali."
        ),
        "testo_integrale": (
            "4.2.3 Algorithms to be supported: Time-stamp token signature algorithms to be supported should "
            "be as specified in clause A.8 of ETSI TS 119 312 [i.5]. NOTE: Cryptographic suites "
            "recommendations defined in ETSI TS 119 312 [i.5] can be superseded by national recommendations."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 4.2.4 (Key lengths to be supported)",
        "testo": (
            "Le lunghezze delle chiavi dell'algoritmo di firma selezionato dovrebbero essere supportate "
            "secondo le raccomandazioni della clausola 9.3 di ETSI TS 119 312 [i.5]; le raccomandazioni "
            "sulle suite crittografiche ivi definite possono essere superate da raccomandazioni nazionali."
        ),
        "testo_integrale": (
            "4.2.4 Key lengths to be supported: Signature algorithm key lengths for the selected signature "
            "algorithm should be supported as recommended in clause 9.3 of ETSI TS 119 312 [i.5]. NOTE: "
            "Cryptographic suites recommendations defined in ETSI TS 119 312 [i.5] can be superseded by "
            "national recommendations."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.1.1 (Core requirement)",
        "testo": (
            "Il time-stamping server deve supportare la richiesta di marca temporale (time-stamping request) "
            "cosi' come definita nella clausola 2.4.1 di IETF RFC 3161 [1], con gli emendamenti stabiliti "
            "dalle clausole seguenti del presente documento."
        ),
        "testo_integrale": (
            "5.1.1 Core requirement: A time-stamping server shall support the time-stamping request as "
            "defined in IETF RFC 3161 [1], clause 2.4.1 with the amendments defined in the following clauses."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.1.2 (Fields to be supported)",
        "testo": (
            "Il time-stamping server deve supportare il campo reqPolicy, il campo nonce e il campo certReq "
            "della richiesta di marca temporale."
        ),
        "testo_integrale": (
            "5.1.2 Fields to be supported: The following requirements apply: - reqPolicy field shall be "
            "supported; - the nonce field shall be supported; and - certReq field shall be supported."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.1.3 (Algorithms to be supported)",
        "testo": (
            "Gli algoritmi di hash dei dati da marcare temporalmente da supportare dovrebbero essere quelli "
            "specificati nella clausola A.8 di ETSI TS 119 312 [i.5], tenendo conto della durata attesa della "
            "marca temporale e del confronto tra le funzioni di hash selezionate e il tempo indicato nella "
            "clausola 9.2 di ETSI TS 119 312 [i.5]; le raccomandazioni sulle suite crittografiche ivi "
            "definite possono essere superate da raccomandazioni nazionali."
        ),
        "testo_integrale": (
            "5.1.3 Algorithms to be supported: Hash algorithms for the time-stamp data to be supported should "
            "be as specified in clause A.8 of ETSI TS 119 312 [i.5]. This should take into account the "
            "expected duration of the time-stamp and selected hash functions versus time given in clause 9.2 "
            "of ETSI TS 119 312 [i.5]. NOTE: Cryptographic suites recommendations defined in ETSI TS 119 312 "
            "[i.5] can be superseded by national recommendations."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.1 (Core requirement)",
        "testo": (
            "Il time-stamping server deve supportare la risposta di marca temporale (time-stamping response) "
            "cosi' come definita nella clausola 2.4.2 di IETF RFC 3161 [1], con gli emendamenti stabiliti "
            "dalle clausole seguenti del presente documento."
        ),
        "testo_integrale": (
            "5.2.1 Core requirement: A time-stamping server shall support the time-stamping response as "
            "defined in IETF RFC 3161 [1], clause 2.4.2 with the amendments defined in the following clauses."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.2 (Fields to be supported)",
        "testo": (
            "Si applicano i requisiti della clausola 2.4.2 di IETF RFC 3161 [1] e inoltre: il campo policy "
            "deve essere presente come identificatore della time-stamp policy e deve conformarsi all'annex A; "
            "il campo genTime deve avere un valore che rappresenti il tempo con la precisione necessaria a "
            "supportare l'accuracy dichiarata; il campo accuracy deve essere presente e deve essere "
            "supportata un'accuracy minima di un secondo; il campo ordering non deve essere presente o deve "
            "essere posto a false; nessuna estensione deve essere marcata come critica; quanto al contenuto "
            "della struttura SignedData in cui e' incapsulata la struttura TSTInfo, l'identificatore del "
            "certificato della TSU (ESSCertID come in IETF RFC 3161 [1] o ESSCertIDv2 come in IETF RFC 5816 "
            "[4]) deve essere incluso come attributo signerInfo all'interno di un attributo "
            "SigningCertificate o SigningCertificateV2 come specificato nella clausola 2.2.1 di IETF RFC "
            "5816 [4]."
        ),
        "testo_integrale": (
            "5.2.2 Fields to be supported: The requirements from IETF RFC 3161 [1], clause 2.4.2 shall apply "
            "and the following requirements apply: - the policy field shall be present as an identifier for "
            "the time-stamp policy and shall conform to annex A; - a genTime field shall have a value "
            "representing time with a precision necessary to support the declared accuracy shall be "
            "supported; - the accuracy field shall be present and a minimum accuracy of one second shall be "
            "supported; - the ordering field shall not be present or shall be set to false; and - no "
            "extension shall be marked as critical. The following requirement applies to the content of the "
            "SignedData structure in which the TSTInfo structure is encapsulated: - the certificate "
            "identifier of the TSU certificate (ESSCertID as in IETF RFC 3161 [1] or ESSCertIDv2 as in IETF "
            "RFC 5816 [4]) shall be included as a signerInfo attribute inside a SigningCertificate or a "
            "SigningCertificateV2 attribute as specified in IETF RFC 5816 [4], clause 2.2.1."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.3 (Algorithms to be used)",
        "testo": (
            "Gli algoritmi di hash usati per calcolare l'impronta dell'informazione da marcare temporalmente "
            "e gli algoritmi di firma del token di marca temporale dovrebbero essere quelli specificati nella "
            "clausola A.8 di ETSI TS 119 312 [i.5]; le raccomandazioni sulle suite crittografiche ivi "
            "definite possono essere superate da raccomandazioni nazionali."
        ),
        "testo_integrale": (
            "5.2.3 Algorithms to be used: Hash algorithms used to hash the information to be time-stamped "
            "and time-stamp token signature algorithms should be as specified in clause A.8 of ETSI TS 119 "
            "312 [i.5]. NOTE: Cryptographic suites recommendations defined in ETSI TS 119 312 [i.5] can be "
            "superseded by national recommendations."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = []

INDICE_ARTICOLI_LOCALE = [
    "clausola 4.1.1 (Core requirement)",
    "clausola 4.1.2 (Fields to be supported)",
    "clausola 4.1.3 (Hash algorithms to be used)",
    "clausola 4.2.1 (Core requirement)",
    "clausola 4.2.2 (Fields to be supported)",
    "clausola 4.2.3 (Algorithms to be supported)",
    "clausola 4.2.4 (Key lengths to be supported)",
    "clausola 5.1.1 (Core requirement)",
    "clausola 5.1.2 (Fields to be supported)",
    "clausola 5.1.3 (Algorithms to be supported)",
    "clausola 5.2.1 (Core requirement)",
    "clausola 5.2.2 (Fields to be supported)",
    "clausola 5.2.3 (Algorithms to be used)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
