"""ETSI TS 119 461 V2.1.1 (2025-02) - Policy and security requirements for
trust service components providing identity proofing of trust service
subjects. Fonte 9 (cablaggio finale in seed.py demandato alla sessione
principale). Capitolo 5 di 8 (vedi manifest.json): clausola 8.3 "Attribute
and evidence validation", sottoclausole 8.3.1-8.3.8 (requisiti VAL-8.3.x-xx).
Testo ufficiale: app/.source_cache/etsi_119_461/cap05.txt.

Convenzione generale di modellazione per questo documento (vedi anche
cap01.py per clausola 3.4 "Notations", legenda ufficiale dei prefissi
requisito: OVR/INI/COL/VAL/BIN/ISS/USE/QTS - solo VAL compare in questo
capitolo, nessuna incongruenza rilevata):

- Ogni requisito con id proprio (**VAL-8.3.x-nn**) -> un nodo, `riferimento`
  = id esatto senza il marcatore "[CONDITIONAL]" (spostato in
  `condizione_applicabilita`).
- I requisiti "VOID" (VAL-8.3.1-09, "merged with VAL-8.3.1-08X"; VAL-8.3.5-03,
  "moved to clauses C.2.3 and C.3.3") non generano un nodo autonomo (nessun
  contenuto proprio oltre il rimando strutturale) e sono esclusi da
  INDICE_ARTICOLI_LOCALE, coerentemente con la convenzione già usata per le
  clausole "void" di ETSI EN 319 412-5.
- Le NOTE annesse a un requisito non generano un nodo a sé: il loro contenuto
  è assorbito in `testo_integrale` (talvolta anche in `testo`) quando aggiunge
  condizioni/precisazioni sostanziali (es. NOTE 1 sotto VAL-8.3.1-08X, che
  precisa cosa si intende per evidenza "genuina"), scartato quando è mera
  esemplificazione (es. EXAMPLE 1/2 sotto 8.3.1-03X/04X sulle differenze di
  trascrizione tra alfabeti). Le NOTE con specifiche tecniche concrete (es.
  frame rate/risoluzione in EXAMPLE 3/4 sotto VAL-8.3.3-04A/04C) sono trattate
  come sostanziali e riportate.
- Ogni sottoclausola 8.3.2-8.3.8 si apre con una frase "[CONDITIONAL]" priva
  di id proprio ("If a digital identity document is used as authoritative
  evidence, the requirements in the present clause apply.") che definisce
  l'ambito di applicazione dell'intera sottoclausola. Non ha un id di
  requisito secondo la notazione 3.4 del documento (solo gli item con id
  proprio sono "requisiti" in senso stretto) ma ha contenuto sostanziale
  proprio (delimita quando l'intera sottoclausola si applica) -> un nodo
  Principio per sottoclausola, tipo "scopo/ambito di applicazione",
  `riferimento` = "clausola 8.3.X (ambito di applicazione)" (stessa
  convenzione di "clausola 1 (Scope)" in ETSI EN 319 412-5). La clausola
  8.3.1 "General requirements" non ha una frase di ambito introduttiva
  analoga (si applica sempre) e non genera un nodo di questo tipo.
  Per rendere ogni nodo autosufficiente (leggibile senza risalire al nodo
  Principio della sottoclausola), la stessa condizione di ambito è comunque
  ripetuta in `condizione_applicabilita` di ciascun Obbligo/Principio della
  sottoclausola, insieme a eventuali condizioni [CONDITIONAL] più specifiche
  proprie del singolo requisito.
- Requisiti che iniziano con "Successful validation/authentication of X shall
  imply that Y" (VAL-8.3.2-00, VAL-8.3.3-00, VAL-8.3.4-02, VAL-8.3.5-00,
  VAL-8.3.6-00, VAL-8.3.7-00) non impongono un comportamento a un soggetto
  obbligato ma dichiarano l'effetto giuridico/procedurale del completamento
  con successo della validazione (stessa struttura del "secondo tipo di nodo"
  del censimento, Principio dichiarativo senza soggetto obbligato, es. art. 25
  eIDAS) -> Principio, tipo "altro" (non "definitorio": non definiscono un
  termine, dichiarano un effetto). La sottoclausola 8.3.8 non ha un item "-00"
  analogo (il testo passa direttamente al requisito operativo VAL-8.3.8-01,
  un vero Obbligo "shall verify...").
- Tutti gli altri requisiti "shall"/"shall not"/"should" con soggetto
  implicito (il TSP o l'IPSP che conduce il processo di identity proofing,
  incluso il registration officer come suo personale) -> Obbligo, categoria
  "QTSP/gestore", ruolo "obbligato". `tipo_obbligo` e' uniformemente
  "tecnico/sicurezza" per l'intero capitolo, come indicato nell'assegnazione
  di lavoro (clausola 8.3 = validazione tecnica di documenti/evidenze/eID/
  firma digitale/registri fidati/prova di accesso/documenti e attestazioni:
  anche i requisiti apparentemente organizzativi in questa clausola, es.
  "specificare nella practice statement come trattare le discrepanze tra
  fonti" VAL-8.3.1-03X/04X/8.3.6-06X/8.3.7-05X/8.3.8-05X, o i requisiti sulla
  formazione dei registration officer VAL-8.3.3-14X/14A/15X, restano parte
  integrante del processo tecnico di validazione dell'evidenza, non policy
  aziendale generale in senso proprio).
- Requisiti "should" (raccomandazione, non prescrizione assoluta) restano
  Obbligo, stessa convenzione già usata in ETSI EN 319 412-5 (es.
  QCS-4.3.2-02); la sfumatura "should" vs "shall" e' preservata nel testo.
- Riferimenti a standard tecnici esterni citati esplicitamente nel testo dei
  requisiti (ICAO Doc 9303 parte 10, ISO/IEC 30107-1/3, TS 18099, elencati
  come riferimenti normativi in clausola 2.1, letta in cap01) sono riportati
  nel testo/testo_integrale del nodo pertinente (VAL-8.3.2-02, VAL-8.3.2-04X,
  VAL-8.3.3-02X, VAL-8.3.3-05A) ma NON generano relazioni cross-fonte: questi
  standard non sono Fonti di questo censimento.
- Quando un requisito elenca lettere a)...f) come sfaccettature omogenee di
  un'unica prescrizione continua (VAL-8.3.3-14X, elenco argomenti di
  formazione del registration officer) e' modellato come un solo nodo, stessa
  convenzione gia' usata per gli elenchi puntati del CAD.
- RELAZIONI interne: due relazioni "richiama" (evidence_type "textual") da
  VAL-8.3.1-10X (che impone di documentare le caratteristiche di sicurezza da
  verificare) verso VAL-8.3.3-07X e VAL-8.3.3-07A, citati esplicitamente in
  NOTE 2 sotto VAL-8.3.1-10X ("see requirements VAL-8.3.3-07X and
  VAL-8.3.3-07A"). Due ulteriori relazioni "richiama" (evidence_type
  "textual") da VAL-8.3.3-05B verso OVR-5-07 e OVR-5-08 (clausola 5,
  capitolo 2 di questa stessa fonte), citati esplicitamente in NOTE 6 sotto
  VAL-8.3.3-05B ("See requirements OVR-5-07 and OVR-5-08 regarding attack
  potential"): tipo (Obbligo) confermato via coordinamento diretto con il
  subagent Etsi461Cap02, che li ha gia' scritti in modo stabile nel proprio
  modulo (app/seed_data/etsi_119_461/cap02.py) con riferimento esatto
  "OVR-5-07"/"OVR-5-08" prima della scrittura di queste relazioni.
"""

SOGGETTO_QTSP = [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}]

RIGHE_OBBLIGHI: list[dict] = [
    # 8.3.1 General requirements
    {
        "riferimento": "VAL-8.3.1-01X",
        "testo": "Tutti gli attributi identificativi necessari devono essere validati al livello di affidabilita' richiesto da una fonte autorevole (authoritative source).",
        "testo_integrale": "VAL-8.3.1-01X: All necessary identity attributes shall be validated to the required reliability by an authoritative source.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "VAL-8.3.1-02",
        "testo": "Le prove del processo di identity proofing devono essere raccolte e conservate in modo sicuro, a supporto dei requisiti della clausola 8.5.2 del presente documento.",
        "testo_integrale": "VAL-8.3.1-02: Evidence of the identity proofing process shall be collected and secured supporting requirements in clause 8.5.2 of the present document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "VAL-8.3.1-03X",
        "testo": "Il trattamento delle differenze di codifica degli attributi identificativi, tra evidenze diverse o tra un'evidenza e attributi raccolti da altre fonti, deve essere specificato nella dichiarazione delle pratiche (practice statement).",
        "testo_integrale": "VAL-8.3.1-03X: The handling of differences in encoding of identity attributes between different evidence or between evidence and attributes collected from other sources than evidence shall be specified in the practice statement. EXAMPLE 1: fonti tipiche di differenza sono la traslitterazione tra alfabeti (es. cirillico/latino), da script non alfabetici (es. cinese) a un alfabeto, la trascrizione di caratteri di lingue nazionali (es. norvegese) in caratteri latini, e la trascrizione di segni diacritici (es. francese) in caratteri latini.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "VAL-8.3.1-04X",
        "testo": "Il trattamento delle differenze negli attributi del nome, tra evidenze diverse o tra un'evidenza e attributi raccolti da altre fonti, deve essere specificato nella dichiarazione delle pratiche.",
        "testo_integrale": "VAL-8.3.1-04X: The handling of differences in name attributes between different evidence or between evidence and attributes collected from other sources than evidence shall be specified in the practice statement. EXAMPLE 2: nomi mancanti (secondi nomi o primi nomi), cambio di nome non riflesso, uso di iniziali, troncamento, uso di prefisso (es. Dr) o suffisso (es. Jr).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "VAL-8.3.1-05",
        "testo": "Il processo di identity proofing deve verificare che l'evidenza sia di un tipo accettato secondo il contesto di identity proofing.",
        "testo_integrale": "VAL-8.3.1-05: The identity proofing process shall verify that the evidence is of a type accepted according to the identity proofing context.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "VAL-8.3.1-06X",
        "testo": "Il processo di identity proofing deve verificare che l'emittente dell'evidenza sia fidato secondo il contesto di identity proofing.",
        "testo_integrale": "VAL-8.3.1-06X: The identity proofing process shall verify that the issuer of evidence is trusted according to the identity proofing context.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "VAL-8.3.1-07",
        "testo": "Se l'evidenza ha un periodo di validita' esplicito, il processo di identity proofing deve verificare che il momento dell'identity proofing rientri in tale periodo.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.1-07: If the evidence has an explicit validity period, the identity proofing process shall verify that the time of the identity proofing is within this validity period. EXAMPLE 3: attributi valid from/valid to di un certificato di firma digitale, data di scadenza di un documento di identita'.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica solo se l'evidenza ha un periodo di validita' esplicito",
    },
    {
        "riferimento": "VAL-8.3.1-08X",
        "testo": "Il processo di identity proofing deve verificare l'autenticita' e l'integrita' dell'evidenza, cioe' che l'evidenza sia genuina e presentata nella sua forma originale (un tipo di evidenza effettivamente esistente, non contraffatto, non manomesso e, ove applicabile, non una copia dell'originale).",
        "testo_integrale": "VAL-8.3.1-08X: The identity proofing process shall verify the authenticity and integrity of the evidence, i.e. that the evidence is genuine and presented in its original form. NOTE 1: An evidence of a type that actually exists, and that is not counterfeit, has not been tampered with and, where applicable, is not a copy of the original. (VAL-8.3.1-09: VOID, merged with il presente requisito).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "VAL-8.3.1-10X",
        "testo": "L'IPSP deve documentare, per tutte le evidenze accettate, le caratteristiche di sicurezza da verificare (non e' necessario documentare tutti gli elementi di sicurezza; una selezione sufficiente per valutare la genuinita' dell'evidenza puo' essere applicata, vedi VAL-8.3.3-07X e VAL-8.3.3-07A; la pubblicazione della selezione non e' raccomandata, si presume documentazione interna; un processo remoto potrebbe non permettere la verifica di tutti gli elementi).",
        "testo_integrale": "VAL-8.3.1-10X: The IPSP shall for all accepted evidence document the security features that are to be verified. NOTE 2: This needs not be all security elements of e.g. a physical identity document. A selection of suitable elements sufficient for assessing that the evidence is genuine can be applied, see requirements VAL-8.3.3-07X and VAL-8.3.3-07A. NOTE 3: Publication of the selection of features is not recommended. Internal documentation is assumed. NOTE 4: A remote identity proofing process might not allow verification of all security elements.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "VAL-8.3.1-11X",
        "testo": "Il processo di identity proofing deve, ogniqualvolta praticamente possibile, verificare che l'evidenza sia valida al momento dell'identity proofing (un documento puo' essere dichiarato smarrito, rubato o revocato, ma non tutti gli emittenti offrono un servizio di stato online, e certificati/eID possono essere revocati prima della scadenza).",
        "testo_integrale": "VAL-8.3.1-11X: The identity proofing process shall whenever practically possible verify that the evidence is valid at the time of the identity proofing. EXAMPLE 4: An identity document can be declared lost, stolen, or revoked, but not all document issuers provide an online status service that can be used to check current status, and if an online status service exists, its availability can be restricted. EXAMPLE 5: Certificates and eIDs can be revoked before their expiry time. This includes certificates of evidence issuers, where the identity proofing context determines if an evidence is accepted or not if the issuer's certificate has expired or is revoked.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "VAL-8.3.1-12",
        "testo": "La validazione dell'evidenza deve avvenire in un ambiente controllato dall'attore responsabile del processo di identity proofing (non vieta l'accesso remoto a tale ambiente da parte dei registration officer, ne' l'hosting su servizio cloud dell'ambiente).",
        "testo_integrale": "VAL-8.3.1-12: Validation of evidence shall be done in an environment controlled by the actor responsible for the identity proofing process. NOTE 5: This requirement does not prohibit remote access to this environment by registration officers. NOTE 6: This requirement does not prohibit cloud service hosting of the environment.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # 8.3.2 Validation of digital identity document
    {
        "riferimento": "VAL-8.3.2-01",
        "testo": "Se il documento di identita' digitale e' usato in un processo di identity proofing remoto, i dati del documento devono essere trasferiti in un ambiente controllato dall'attore responsabile del processo in modo da garantire autenticita', integrita' e riservatezza del contenuto del documento.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.2-01: If the digital identity document is used in a remote identity proofing process, the data from the identity document shall be transferred to an environment controlled by the actor responsible for the identity proofing process in a manner that ensures authenticity, integrity, and confidentiality of the document content.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' digitale e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.2) e il processo e' remoto",
    },
    {
        "riferimento": "VAL-8.3.2-02",
        "testo": "Il documento di identita' digitale deve essere accettato solo se la firma digitale dell'emittente sul documento e' validata con successo (di norma un risultato TOTAL-PASSED secondo ETSI EN 319 102-1; per un documento eMRTD conforme a ICAO Doc 9303 parte 10, sono necessari i certificati di firma nazionali, es. dal Public Key Database ICAO).",
        "testo_integrale": "VAL-8.3.2-02: The digital identity document shall only be accepted if the issuer's digital signature on the document is successfully validated. NOTE 2: Usually this means that the validation result is TOTAL-PASSED as defined by ETSI EN 319 102-1 [i.5]. NOTE 3: For an eMRTD document following ICAO 9303 part 10 [2], country signing certificates, e.g. downloaded from the ICAO PKD (Public Key Database), are needed for validation.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' digitale e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.2)",
    },
    {
        "riferimento": "VAL-8.3.2-03",
        "testo": "Se esiste ed e' praticamente disponibile un servizio online per confermare la validita' del documento, il processo deve utilizzarlo per verificare che il documento sia attualmente valido (non revocato, sospeso o segnalato come smarrito/rubato; puo' esservi ritardo dell'ordine di giorni tra revoca e aggiornamento del servizio; l'accesso a molti servizi di stato diversi puo' essere impraticabile per documenti poco frequenti).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.2-03: If an online status service to confirm the document's validity exists and is practically available, the process shall use this service to verify that the document is currently valid. NOTE 4/5: [meaning e limiti pratici, vedi testo].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' digitale e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.2) e un servizio online di verifica dello stato di validita' del documento esiste ed e' disponibile in pratica",
    },
    {
        "riferimento": "VAL-8.3.2-04X",
        "testo": "Se il documento di identita' digitale deve essere letto da un chip incorporato in un documento di identita' fisico, il processo di identity proofing deve proteggere contro l'iniezione nel processo, da parte del richiedente o di un attaccante esterno, di una copia di un documento di identita' digitale precedentemente ottenuta e conservata dall'attaccante (mezzi per il rilevamento di attacchi di iniezione biometrica, es. TS 18099, possono essere usati come base anche per rilevare questo tipo di attacco).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.2-04X: If the digital identity document is required to be read from a chip embedded in a physical identity document, the identity proofing process shall protect against injection into the process, by the applicant or an external attacker, of a copy of a digital identity document that has previously been obtained and stored by the attacker. NOTE 8: Means for biometric injection attack detection, e.g. as per TS 18099 [5], can be used as a basis to also detect this type of injection attack.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' digitale e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.2) e il documento deve essere letto da un chip incorporato in un documento di identita' fisico",
    },
    {
        "riferimento": "VAL-8.3.2-04A",
        "testo": "Se il documento di identita' digitale deve essere letto da un chip incorporato in un documento di identita' fisico, in caso di interruzione del processo di identity proofing per qualunque motivo (es. perdita della connessione internet), se il processo viene ripreso, il documento di identita' deve essere riletto dal chip.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.2-04A: If the digital identity document is required to be read from a chip embedded in a physical identity document, in case of an interruption of the identity proofing process for any reason (e.g. loosing internet connection), if the identity proofing process is resumed, the identity document shall be reread from the chip.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' digitale e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.2), il documento deve essere letto da un chip incorporato in un documento di identita' fisico, e il processo, interrotto per qualunque motivo, viene ripreso",
    },
    {
        "riferimento": "VAL-8.3.2-05",
        "testo": "Le informazioni ottenute dal documento di identita' digitale devono essere registrate nella misura necessaria per l'associazione al richiedente e per documentare il processo di identity proofing (oltre agli attributi identificativi, tipicamente almeno emittente, periodo di validita' e numero identificativo univoco del documento).",
        "testo_integrale": "VAL-8.3.2-05: Information obtained from the digital identity document shall be recorded as needed for binding to applicant and to evidence the identity proofing process. NOTE 9: In addition to identity attributes, required information to be recorded is typically at least issuer, validity period, and the document's unique identification number.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' digitale e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.2)",
    },
    {
        "riferimento": "VAL-8.3.2-06",
        "testo": "La foto del volto contenuta nel documento di identita' digitale deve essere estratta per consentire l'associazione al richiedente.",
        "testo_integrale": "VAL-8.3.2-06: The face photo contained in the digital identity document shall be extracted to enable binding to applicant.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' digitale e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.2)",
    },
    # 8.3.3 Validation of physical identity document
    {
        "riferimento": "VAL-8.3.3-01",
        "testo": "Il processo deve verificare che il documento di identita' fisico presentato sia visivamente uguale all'aspetto visivo atteso per quel tipo di documento.",
        "testo_integrale": "VAL-8.3.3-01: The process shall verify that the physical identity document presented is visually equal to the expected visual appearance of the document type.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3)",
    },
    {
        "riferimento": "VAL-8.3.3-02X",
        "testo": "Se il documento di identita' fisico e' usato come evidenza in un processo di identity proofing remoto, il processo deve assicurare che il richiedente abbia il documento in mano e lo presenti in tempo reale davanti a una telecamera (la sottomissione di una foto/video pre-registrato non soddisfa i requisiti per il Baseline o Extended LoIP; mezzi di rilevamento di attacchi di presentazione, es. ISO/IEC 30107-1/3, e di iniezione, es. TS 18099, possono essere usati per rilevare l'uso di video pre-registrati o generati artificialmente).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-02X: If a physical identity document is used as evidence in a remote identity proofing process, the process shall ensure that the applicant has the document in hand and presents the document in real-time in front of a camera. NOTE 2: It is required that this happens at the time of the identity proofing; submission of a pre-recorded photo or video stream of an identity document is considered not to meet the requirements for identity proofing to Baseline or Extended LoIP. Means for biometric presentation attack detection, e.g. as specified by ISO/IEC 30107-1 [i.16] and 3 [3], can be used as a basis to detect a presentation attack using a pre-recorded or artificially generated video of an identity document. Means for biometric injection attack detection, e.g. as per TS 18099 [5] can be used as a basis to detect an injection attack using a pre-recorded or artificially generated video of an identity document. NOTE 3: This can rely on the applicant's use of software approved for the identity proofing process, e.g. mobile app functionality.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e il processo e' remoto",
    },
    {
        "riferimento": "VAL-8.3.3-03",
        "testo": "Il processo deve assicurare che il documento presentato dal richiedente sia un documento di identita' fisico genuino, non contraffatto ne' falsificato/modificato.",
        "testo_integrale": "VAL-8.3.3-03: The process shall ensure that the document presented by the applicant is a genuine, physical identity document that is not counterfeited or falsified/modified.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3)",
    },
    {
        "riferimento": "VAL-8.3.3-04X",
        "testo": "Se il documento di identita' fisico e' usato in un processo di identity proofing remoto, la presentazione del documento davanti a una telecamera deve includere la registrazione, al momento dell'identity proofing, di una sequenza video che visualizzi le caratteristiche fisiche del documento e i suoi elementi di sicurezza, coprendo ciascun lato rilevante del documento (l'uso di una sola foto statica non e' considerato sufficiente per Baseline o Extended LoIP).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-04X: If the physical identity document is used in a remote identity proofing process, the applicant's presentation of the identity document in front of a camera shall include recording at the time of the identity proofing of a video sequence to visualize the physical characteristics of the identity document and its security features. The recording shall cover each relevant side of the identity document presented by the applicant. EXAMPLE 1: The applicant can be given instructions for the movement of the identity document, where the specific actions and/or their sequence are unpredictable to the applicant. NOTE 4: With the current state of technology, the use of only a still photo of the identity document is not considered sufficient for Baseline or Extended LoIP. EXAMPLE 2: Both the front and back sides of a national identity card will usually need to be presented.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e il documento e' usato in un processo remoto",
    },
    {
        "riferimento": "VAL-8.3.3-04A",
        "testo": "Se il documento di identita' fisico e' usato in un processo remoto, la registrazione video del documento deve usare un frame rate e una risoluzione sufficienti per l'analisi del documento (es. 25 fotogrammi al secondo e risoluzione 1280x720 o 960x720 orizzontale, o 720x1280 o 720x960 verticale).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-04A: If the physical identity document is used in a remote identity proofing process, the video recording of the document shall use frame rate and resolution sufficient for the analysis of the document. EXAMPLE 3: A frame rate of 25 frames per second and a resolution of 1280\u00d7720 pixels or 960\u00d7720 pixels (landscape) or 720\u00d71280 pixels or 720\u00d7960 pixels (portrait).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e il documento e' usato in un processo remoto",
    },
    {
        "riferimento": "VAL-8.3.3-04B",
        "testo": "Se il documento di identita' fisico e' usato in un processo remoto, il processo dovrebbe catturare, dalla sequenza video o in modo integrato ad essa, una o piu' immagini di ciascun lato rilevante del documento.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-04B: If the physical identity document is used in a remote identity proofing process, the process should capture from or integral to the video sequence one or more images of each relevant side of the identity document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e il documento e' usato in un processo remoto",
    },
    {
        "riferimento": "VAL-8.3.3-04C",
        "testo": "Se il documento di identita' fisico e' usato in un processo remoto e nel processo viene acquisita un'immagine del documento, l'immagine deve avere risoluzione sufficiente per l'analisi del documento (es. 1280x720 o 960x720 orizzontale, o 720x1280 o 720x960 verticale).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-04C: If the physical identity document is used in a remote identity proofing process, and an image of the document is captured in the process, the image shall have sufficient resolution for the analysis of the document. EXAMPLE 4: A resolution of 1280\u00d7720 pixels or 960\u00d7720 pixels (landscape) or 720\u00d71280 pixels or 720\u00d7960 pixels (portrait).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3), il documento e' usato in un processo remoto ed e' acquisita un'immagine del documento",
    },
    {
        "riferimento": "VAL-8.3.3-05X",
        "testo": "Se il documento di identita' fisico e' usato in un processo remoto, il processo deve assicurare che il flusso video e le immagini catturate siano trasmesse a un ambiente controllato dall'attore responsabile del processo in modo da garantire autenticita', integrita' e riservatezza del flusso video e delle immagini.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-05X: If the physical identity document is used in a remote identity proofing process, the process shall ensure that the video stream and any images captured are transmitted to an environment controlled by the actor responsible for the identity proofing process in a manner that ensures authenticity, integrity, and confidentiality of the video stream and images.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e il documento e' usato in un processo remoto",
    },
    {
        "riferimento": "VAL-8.3.3-05A",
        "testo": "Se il documento di identita' fisico e' usato in un processo remoto, il processo deve proteggere contro l'iniezione nel processo, da parte del richiedente o di un attaccante esterno, di un flusso video precedentemente registrato o generato artificialmente (mezzi per il rilevamento di attacchi di iniezione biometrica, es. TS 18099, possono essere usati come base per rilevare anche questo tipo di attacco).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-05A: If the physical identity document is used in a remote identity proofing process, the process shall protect against injection into the process, by the applicant or an external attacker, of a previously recorded or artificially generated video stream. NOTE 5: Means for biometric injection attack detection, e.g. as per TS 18099 [5], can be used as a basis to also detect this type of injection attack.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e il documento e' usato in un processo remoto",
    },
    {
        "riferimento": "VAL-8.3.3-05B",
        "testo": "Se il documento di identita' fisico e' usato in un processo remoto, il processo deve applicare mezzi in grado di rilevare in modo affidabile documenti di identita' generati artificialmente o manipolati da un attaccante con il relativo potenziale di attacco (vedi anche i requisiti OVR-5-07 e OVR-5-08, clausola 5, sul potenziale di attacco).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-05B: If the physical identity document is used in a remote identity proofing process, the process shall apply means that are reliably able to detect identity documents that are artificially generated or have been manipulated by an attacker with the relevant attack potential. NOTE 6: See requirements OVR-5-07 and OVR-5-08 regarding attack potential.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e il documento e' usato in un processo remoto",
    },
    {
        "riferimento": "VAL-8.3.3-05C",
        "testo": "Se il documento di identita' fisico e' usato in un processo remoto, l'usabilita' (es. condizioni di illuminazione, riflessi, nitidezza) del video e di ogni immagine catturata o derivata dalla sequenza video deve essere valutata; video e immagini devono essere rigettati se non usabili, con istruzioni al richiedente di ripetere il processo in condizioni migliori.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-05C: If the physical identity document is used in a remote identity proofing process, the useability (e.g. lighting conditions, reflections, sharpness) of video and any images captured in the same process or derived from the video sequence shall be assessed, and video and images shall be rejected if they are not useable, with instructions to the applicant to repeat the process under better conditions.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e il documento e' usato in un processo remoto",
    },
    {
        "riferimento": "VAL-8.3.3-05D",
        "testo": "Deve esistere un limite massimo al numero di tentativi di acquisizione video prima che il processo sia interrotto con esito fallito.",
        "testo_integrale": "VAL-8.3.3-05D: There shall be an upper limit on the number of retries on the video capture before the process is aborted with failed result.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3)",
    },
    {
        "riferimento": "VAL-8.3.3-06",
        "testo": "Se il processo e' svolto con validazione manuale del documento di identita' fisico, il registration officer deve avere accesso a fonti autorevoli di informazione sull'aspetto e sulla validazione dei documenti (es. PRADO - Public Register of Authentic Travel and Identity Documents Online).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-06: If the process is performed with manual validation of the physical identity document, the registration officer shall have access to authoritative sources of information on document appearance and document validation. EXAMPLE 5: Public Register of Authentic Travel and Identity Documents Online (PRADO).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e il processo e' svolto con validazione manuale del documento",
    },
    {
        "riferimento": "VAL-8.3.3-07X",
        "testo": "Un numero sufficiente, e almeno tre, di diversi elementi di sicurezza dei documenti di identita' fisici devono essere verificati in modo affidabile, considerando un attaccante con il relativo potenziale di attacco (es. filigrane, ologrammi, tecniche di stampa, pattern a luce visibile/ultravioletta, elementi trasparenti; PRADO pubblica una panoramica degli elementi di sicurezza).",
        "testo_integrale": "VAL-8.3.3-07X: A sufficient number of, and at least three, different security features of physical identity documents shall be reliably verified considering an attacker with the relevant attack potential. EXAMPLE 6: Security elements can be watermarks, holograms, printing techniques, visual and ultraviolet light patterns, and see-through elements. The reliability of remote verification of different security elements can vary. NOTE 7: PRADO has published an overview of security features [i.27] of identity documents.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3)",
    },
    {
        "riferimento": "VAL-8.3.3-07A",
        "testo": "Se il documento di identita' fisico e' usato in un processo remoto, almeno due degli elementi di sicurezza verificati devono essere elementi otticamente variabili (un documento con meno di due elementi otticamente variabili non puo' essere usato in processi di identity proofing remoti).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-07A: If the physical identity document is used in a remote identity proofing process, at least two of the security features verified shall be optically variable features. NOTE 8: This implies that a document that has less than two optically variable features cannot be used in remote identity proofing processes.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e il documento e' usato in un processo remoto",
    },
    {
        "riferimento": "VAL-8.3.3-07B",
        "testo": "La selezione degli elementi di sicurezza variabili dei documenti di identita' fisici da verificare dovrebbe avere un certo grado di casualita', per ostacolare gli attaccanti che mirano a falsificare elementi specifici.",
        "testo_integrale": "VAL-8.3.3-07B: Selection of which variable security elements of physical identity documents to verify should have some randomness to hamper attackers targeting falsifying specific elements.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3)",
    },
    {
        "riferimento": "VAL-8.3.3-07C",
        "testo": "Il processo di verifica per tutti gli elementi di sicurezza rientranti nell'ambito del servizio dell'IPSP deve essere documentato (la pubblicazione del processo non e' raccomandata, si presume documentazione interna).",
        "testo_integrale": "VAL-8.3.3-07C: The verification process for all security elements in scope of the IPSP's service shall be documented. NOTE 9: Publication of the verification process information is not recommended. Internal documentation is assumed.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3)",
    },
    {
        "riferimento": "VAL-8.3.3-08",
        "testo": "Se il processo e' svolto con presentazione fisica del documento, il registration officer deve verificare gli elementi di sicurezza ottici e aptici/tattili se presenti (la selezione degli elementi da verificare puo' dipendere dagli strumenti disponibili: senza strumenti solo gli elementi di Livello 1, con lente d'ingrandimento o lampada UV anche di Livello 2).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-08: If the process is performed with the physical presentation of physical identity documents, the registration officer shall verify optical and haptic/tactile security features if any. NOTE 10: Selection of security features to verify can depend on the tools that the registration officer has available, If no tool is available, only Level 1 security features can be verified. With tools such as magnifying glass or UV lamp, Level 2 security features can be verified.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e il processo e' svolto con presentazione fisica del documento",
    },
    {
        "riferimento": "VAL-8.3.3-09",
        "testo": "Se esiste ed e' praticamente disponibile un servizio online per confermare la validita' del documento di identita' fisico, il processo deve utilizzarlo per verificare che il documento sia attualmente valido (non revocato, sospeso o segnalato come smarrito/rubato; puo' esservi ritardo tra revoca e aggiornamento del servizio; l'accesso a molti servizi diversi puo' essere impraticabile per documenti poco frequenti).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-09: If an online status service to confirm the physical identity document's validity exists and is practically available, the process shall use this service to verify that the document is currently valid. NOTE 11: Meaning not revoked, suspended, or reported as lost/stolen. Not all document issuers have available lookup services to check validity, and in some cases access to lookup services is restricted. Regarding current validity, note that there can be a delay in the order of days between the events of revoking a document and updating a status service. NOTE 12: If physical identity documents from many different sources are accepted, online access (interactive or by API) to all the different status services can be impractical for documents that occur infrequently.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e un servizio online di verifica dello stato di validita' del documento esiste ed e' disponibile in pratica",
    },
    {
        "riferimento": "VAL-8.3.3-10",
        "testo": "Le informazioni stampate sui documenti di identita' fisici devono essere registrate nella misura necessaria per l'associazione al richiedente e per documentare il processo di identity proofing (estrazione tramite trascrizione manuale, scansione ottica/OCR, o foto/fotocopia; tipicamente almeno emittente, periodo di validita' e numero identificativo univoco).",
        "testo_integrale": "VAL-8.3.3-10: Information printed on physical identity documents shall be recorded as needed for binding to applicant and to evidence the identity proofing process. NOTE 13: Information can be extracted by manual transcription, automatically for example by optical scanning and OCR techniques, and in some cases by photo/photocopy of the document. NOTE 14: In addition to identity attributes, required information to be recorded is typically at least issuer, validity period, and the document's unique identification number.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3)",
    },
    {
        "riferimento": "VAL-8.3.3-11",
        "testo": "Se i dati biometrici del volto sono applicati per associare il documento di identita' fisico al richiedente, la foto del volto stampata sul documento deve essere estratta.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-11: If face biometrics is applied to bind the physical identity document to the applicant, the face photo printed on the identity document shall be extracted.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e sono applicati dati biometrici del volto per associare il documento al richiedente",
    },
    {
        "riferimento": "VAL-8.3.3-12X",
        "testo": "Se il documento di identita' fisico e' usato in un processo remoto e il documento ha una zona a lettura ottica (MRZ), le informazioni della MRZ devono essere estratte, validate e confrontate con le informazioni della parte visibile del documento.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-12X: If the physical identity document is used in a remote identity proofing process, and the identity document has an Machine Readable Zone (MRZ), the information from the MRZ shall be extracted, validated, and compared with the information from the visible part of the identity document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3), il documento e' usato in un processo remoto e il documento ha una zona a lettura ottica (MRZ)",
    },
    {
        "riferimento": "VAL-8.3.3-13",
        "testo": "Se il documento di identita' fisico e' validato con procedure manuali, il compito di validazione dovrebbe essere assegnato in modo casuale tra i registration officer disponibili.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-13: If the physical identity document is validated by manual procedures, the validation task should be assigned randomly among available registration officers.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e il documento e' validato con procedure manuali",
    },
    {
        "riferimento": "VAL-8.3.3-14X",
        "testo": "Se la validazione dei documenti di identita' fisici e' svolta manualmente, essa deve essere effettuata da un registration officer che ha ricevuto una formazione adeguata che copra almeno: a) prevenzione delle frodi e rilevamento della contraffazione; b) protezione dei dati; c) formazione alla comunicazione (quando il registration officer deve comunicare con il richiedente); d) formazione su software e attrezzature utilizzate; e) formazione sulla verifica dei documenti e dei loro elementi di sicurezza; f) formazione sul rilevamento di attacchi di presentazione e di iniezione.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-14X: If validation of physical identity documents is done manually, the validation shall be carried out by a registration officer that has received appropriate training covering at least the following: a) Fraud prevention and detection of forgery. b) Data protection. c) Communication training (when the registration officer is required to communicate with the applicant). d) Training on software and equipment used. e) Training on verification of documents and their security elements. f) Training on detection of presentation and injection attacks.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e la validazione del documento e' svolta manualmente",
    },
    {
        "riferimento": "VAL-8.3.3-14A",
        "testo": "Se la validazione dei documenti di identita' fisici e' svolta manualmente, al registration officer deve essere concesso tempo sufficiente per la validazione e condizioni di lavoro che non compromettano il suo giudizio.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-14A: If validation of physical identity documents is done manually, the registration officer shall be allowed sufficient time for the validation and have working conditions that do not impair the registration officer's judgement.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e la validazione del documento e' svolta manualmente",
    },
    {
        "riferimento": "VAL-8.3.3-15X",
        "testo": "Se la validazione dei documenti di identita' fisici e' svolta manualmente, la formazione dei registration officer deve essere ripetuta o aggiornata come richiesto dall'intelligence sulle minacce, dagli aggiornamenti di procedure o strumenti, e almeno annualmente.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-15X: If validation of physical identity documents is done manually, the training of the registration officers shall be repeated or refreshed as required by threats intelligence, updates to procedures or tools, and at least annually.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e la validazione del documento e' svolta manualmente",
    },
    {
        "riferimento": "VAL-8.3.3-16",
        "testo": "Se la validazione dei documenti di identita' fisici e' svolta manualmente con presentazione fisica del documento, il registration officer dovrebbe disporre di strumenti che ne rafforzino l'affidabilita' (es. lente d'ingrandimento e lampada UV; senza strumenti si possono verificare solo elementi di sicurezza di Livello 1 secondo ICAO).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-16: If validation of physical identity documents is done manually, and the process is performed with the physical presentation of the document, the registration officer should have available tools to enhance the reliability of the validation. EXAMPLE 7: Magnifying glass and ultraviolet lamp. Without tools, only Level 1 security features as defined by ICAO can be verified.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3), la validazione del documento e' svolta manualmente e il processo avviene con presentazione fisica del documento",
    },
    {
        "riferimento": "VAL-8.3.3-17",
        "testo": "Se la validazione dei documenti di identita' fisici e' svolta manualmente e il documento e' usato in un processo remoto, il registration officer deve disporre di strumenti che ne rafforzino l'affidabilita' (es. strumento informatico per ingrandire i dettagli del documento).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-17: If validation of physical identity documents is done manually, and the document is used in a remote identity proofing process, the registration officer shall have available tools to enhance the reliability of the validation. EXAMPLE 8: Computerized tool to zoom in on details of the document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3), la validazione del documento e' svolta manualmente e il documento e' usato in un processo remoto",
    },
    {
        "riferimento": "VAL-8.3.3-18",
        "testo": "Mezzi automatizzati e tecnologia di apprendimento automatico dovrebbero essere usati per analizzare le caratteristiche dei documenti di identita' fisici rispetto al loro aspetto atteso, inclusa l'analisi degli elementi di sicurezza e di eventuali manipolazioni (un processo puramente manuale resta ammesso sia in presenza fisica sia da remoto, ma l'uso di mezzi automatizzati aggiuntivi e' raccomandato; per l'identity proofing remoto non presidiato, un processo puramente manuale puo' supportare solo il Baseline LoIP, vedi clausola 9.2.3.2; il tipo di documento puo' essere un parametro di input o determinato dall'analisi automatizzata stessa; analisi automatizzata e manuale possono essere combinate, es. con ricorso alla verifica manuale in caso di esito incerto dell'automatismo).",
        "testo_integrale": "VAL-8.3.3-18: Automated means and machine-learning technology should be used to analyse the characteristics of physical identity documents against their expected appearance, including analysis of security elements of documents and potential manipulation of documents. NOTE 15: This requirement implies that a purely manual process for validating a physical identity document is allowed both for physical presence and for remote identity proofing. However, the use of (additional) automated means is recommended. NOTE 16: For unattended remote identity proofing, a purely manual validation process can only support the Baseline LoIP, see clause 9.2.3.2 of the present document. NOTE 17: The document type, e.g. a passport of a specific country, can be an input parameter to the analysis, or the analysis can determine the type by automated means. NOTE 18: Automated and manual analysis can be used in combination, e.g. with fall-back to manual analysis if the automated process yields an uncertain result, or by using automated analysis as a tool for a registration officer.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3)",
    },
    {
        "riferimento": "VAL-8.3.3-19X",
        "testo": "Se il documento di identita' fisico e' usato in un processo remoto, il flusso video e ogni immagine registrata devono avere qualita' sufficiente per l'analisi tramite mezzi automatizzati e tecnologia di apprendimento automatico e/o verifica manuale.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-19X: If the physical identity document is used in a remote identity proofing process, the video stream and any image recorded shall be of sufficient quality for analysis by automated means and machine-learning technology and/or manual verification.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e il documento e' usato in un processo remoto",
    },
    {
        "riferimento": "VAL-8.3.3-20",
        "testo": "Se sono utilizzati mezzi automatizzati e tecnologia di apprendimento automatico per analizzare i documenti di identita' fisici, gli algoritmi e la tecnologia devono essere testati sistematicamente rispetto a dataset di riferimento e mantenuti aggiornati per far fronte ai cambiamenti nel quadro delle minacce e del rischio.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.3-20: If automated means and machine-learning technology are used to analyse physical identity documents, the algorithms and technology shall be systematically tested against reference datasets and be kept updated to cope with changes in the threats and risk situation.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3) e sono utilizzati mezzi automatizzati e tecnologia di apprendimento automatico per analizzare i documenti",
    },
    # 8.3.4 Validation of eID means
    {
        "riferimento": "VAL-8.3.4-01X",
        "testo": "Deve essere eseguito un protocollo di autenticazione che confermi, a un livello di garanzia simile al LoA dell'eID utilizzato, che il titolare del mezzo eID e' autenticato con successo e che il mezzo eID utilizzato e' valido (non scaduto, sospeso o revocato).",
        "testo_integrale": "VAL-8.3.4-01X: An authentication protocol that confirms at an assurance level similar to the LoA of the eID used that the holder of the eID means is successfully authenticated and that the eID means used is valid (not expired, suspended, or revoked) shall be executed.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se l'autenticazione tramite un mezzo eID esistente e' usata come evidenza nel processo di identity proofing (clausola 8.3.4)",
    },
    # 8.3.5 Validation of digital signature with certificate
    {
        "riferimento": "VAL-8.3.5-01",
        "testo": "La firma digitale deve essere creata come parte del processo di identity proofing, per evitare minacce derivanti dall'uso di documenti precedentemente firmati dal richiedente.",
        "testo_integrale": "VAL-8.3.5-01: The digital signature shall be created as part of the identity proofing process. NOTE 3: This is to avoid threats from the use of documents previously signed by the applicant.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se una firma digitale con certificato e' usata come evidenza nel processo di identity proofing (clausola 8.3.5)",
    },
    {
        "riferimento": "VAL-8.3.5-02X",
        "testo": "La firma digitale deve essere validata, e il certificato di firma deve essere usato come evidenza per gli attributi identificativi solo se la firma e' valida e confermata come creata nell'ambito del processo di identity proofing.",
        "testo_integrale": "VAL-8.3.5-02X: The digital signature shall be validated and the signing certificate shall only be used as evidence for identity attributes if the signature is valid and confirmed to have been created as part of the identity proofing process.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se una firma digitale con certificato e' usata come evidenza nel processo di identity proofing (clausola 8.3.5)",
    },
    # 8.3.6 Validation of trusted registers
    {
        "riferimento": "VAL-8.3.6-01",
        "testo": "Se la comunicazione verso il registro fidato e' online, il canale di comunicazione deve essere protetto usando una versione aggiornata del protocollo TLS o un altro protocollo che offra un livello di sicurezza comparabile.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.6-01: If the communication towards the trusted register is online, the communication channel shall be secured by using an up to date version of the TLS protocol or another protocol offering a comparable level of security.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un registro fidato e' usato come evidenza supplementare nel processo di identity proofing (clausola 8.3.6) e la comunicazione verso il registro fidato e' online",
    },
    {
        "riferimento": "VAL-8.3.6-02",
        "testo": "Se la comunicazione verso il registro fidato e' online, il registro fidato deve essere autenticato (es. tramite certificato del sito web).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.6-02: If the communication towards the trusted register is online, the trusted register shall be authenticated. EXAMPLE 1: By a website certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un registro fidato e' usato come evidenza supplementare nel processo di identity proofing (clausola 8.3.6) e la comunicazione verso il registro fidato e' online",
    },
    {
        "riferimento": "VAL-8.3.6-03",
        "testo": "Se la comunicazione verso il registro fidato e' basata su messaggi, tutti i messaggi devono essere autenticati e protetti nell'integrita' (es. tramite firme digitali; il contesto di identity proofing puo' porre requisiti che la firma digitale deve soddisfare per essere accettata).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.6-03: If the communication towards the trusted register is message-based, all messages shall be authenticated and integrity protected. EXAMPLE 2: By use of digital signatures. The identity proofing context can pose requirements that a digital signature is required to fulfil to be accepted.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un registro fidato e' usato come evidenza supplementare nel processo di identity proofing (clausola 8.3.6) e la comunicazione verso il registro fidato e' basata su messaggi",
    },
    {
        "riferimento": "VAL-8.3.6-04",
        "testo": "Se la comunicazione verso il registro fidato e' basata su messaggi, tutti i messaggi contenenti informazioni identificative personali devono essere cifrati.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.6-04: If the communication towards the trusted register is message-based, all messages containing personal identity information shall be encrypted.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un registro fidato e' usato come evidenza supplementare nel processo di identity proofing (clausola 8.3.6) e la comunicazione verso il registro fidato e' basata su messaggi",
    },
    {
        "riferimento": "VAL-8.3.6-05X",
        "testo": "L'integrita' e l'autenticita' degli attributi identificativi ottenuti dal registro fidato devono essere validate.",
        "testo_integrale": "VAL-8.3.6-05X: The integrity and authenticity of identity attributes obtained from the trusted register shall be validated.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un registro fidato e' usato come evidenza supplementare nel processo di identity proofing (clausola 8.3.6)",
    },
    {
        "riferimento": "VAL-8.3.6-06X",
        "testo": "La procedura da applicare in caso di discrepanze tra gli attributi identificativi ottenuti dal registro fidato e le informazioni da altre evidenze deve essere specificata nella dichiarazione delle pratiche (il registro fidato puo' prevalere su altre evidenze, o viceversa, o puo' essere usata una procedura di arbitrato; il contesto di identity proofing puo' porre requisiti).",
        "testo_integrale": "VAL-8.3.6-06X: The procedure to apply in case of discrepancies between the identity attributes obtained from trusted registers and information from other evidence shall be specified in the practice statement. EXAMPLE 3: A trusted register can override identity attributes obtained from other evidence. The identity proofing context can pose requirements.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se un registro fidato e' usato come evidenza supplementare nel processo di identity proofing (clausola 8.3.6)",
    },
    # 8.3.7 Validation of proof of access
    {
        "riferimento": "VAL-8.3.7-01",
        "testo": "Deve essere eseguito un protocollo di prova di accesso per assicurare che il richiedente controlli l'elemento in questione (es. per confermare il possesso di un numero di cellulare, di un indirizzo email o di un conto bancario).",
        "testo_integrale": "VAL-8.3.7-01: A proof of access protocol shall be executed to ensure that the applicant controls the item in question. EXAMPLE 1: To confirm possession of mobile phone number, email address, or bank account.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se una prova di accesso e' usata come evidenza supplementare nel processo di identity proofing (clausola 8.3.7)",
    },
    {
        "riferimento": "VAL-8.3.7-02X",
        "testo": "Gli attributi identificativi ottenuti devono essere trasferiti o comunque resi disponibili al processo di identity proofing in modo da garantire l'autenticita' della fonte dell'informazione e l'integrita' e riservatezza dell'informazione.",
        "testo_integrale": "VAL-8.3.7-02X: The identity attributes obtained shall be transferred or otherwise be made available for the identity proofing process in a way that ensures the authenticity of the source of information and integrity and confidentiality of the information.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se una prova di accesso e' usata come evidenza supplementare nel processo di identity proofing (clausola 8.3.7)",
    },
    {
        "riferimento": "VAL-8.3.7-03",
        "testo": "L'integrita' e l'autenticita' degli attributi identificativi ottenuti devono essere validate (es. informazioni da un record cliente esistente presso una banca o un fornitore di servizi di telecomunicazione).",
        "testo_integrale": "VAL-8.3.7-03: The integrity and authenticity of the identity attributes obtained shall be validated. EXAMPLE 2: Information from an existing customer record of a bank or a telecommunications service provider.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se una prova di accesso e' usata come evidenza supplementare nel processo di identity proofing (clausola 8.3.7)",
    },
    {
        "riferimento": "VAL-8.3.7-04",
        "testo": "Se la prova di accesso a un conto bancario e' usata come evidenza supplementare, l'accesso del richiedente al conto bancario deve essere autenticato in modo affidabile (es. tramite mezzi eID conformi ai requisiti di Strong Customer Authentication della direttiva PSD2, o tramite un pagamento effettuato dal richiedente verso un conto associato al processo di identity proofing).",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.7-04: If proof of access to a bank account is used as supplementary evidence, the applicant's access to the bank account shall be reliably authenticated. EXAMPLE 3: By use of eID means fulfilling requirements for EU Payment Services Directive (PSD2) Strong Customer Authentication (SCA) [i.2]. EXAMPLE 4: A payment made by the applicant to an account associated with the identity proofing process can be part of the proof of access protocol.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se una prova di accesso e' usata come evidenza supplementare nel processo di identity proofing (clausola 8.3.7) e la prova di accesso e' relativa a un conto bancario",
    },
    {
        "riferimento": "VAL-8.3.7-05X",
        "testo": "La procedura da applicare in caso di discrepanze tra gli attributi identificativi ottenuti dalla prova di accesso e gli attributi identificativi da altre evidenze deve essere specificata nella dichiarazione delle pratiche.",
        "testo_integrale": "VAL-8.3.7-05X: The procedure to apply in case of discrepancies between the identity attributes obtained from proof of access and identity attributes from other evidence shall be specified in the practice statement. EXAMPLE 5: The identity attributes obtained from proof of access can be regarded as authoritative and override other sources of attributes, or other evidence can be regarded as authoritative, or an arbitration procedure can be used. The identity proofing context can pose requirements.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se una prova di accesso e' usata come evidenza supplementare nel processo di identity proofing (clausola 8.3.7)",
    },
    # 8.3.8 Validation of documents and attestations
    {
        "riferimento": "VAL-8.3.8-01",
        "testo": "Il processo di identity proofing deve verificare che il documento o l'attestazione presentata sia di un tipo accettato e sia emessa da un attore fidato secondo il contesto di identity proofing.",
        "testo_integrale": "VAL-8.3.8-01: The identity proofing process shall verify that the document or attestation presented is of an accepted type and is issued by an actor trusted according to the identity proofing context.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se documenti o attestazioni sono usati come evidenza supplementare nel processo di identity proofing (clausola 8.3.8)",
    },
    {
        "riferimento": "VAL-8.3.8-02X",
        "testo": "L'identita' dell'emittente del documento o dell'attestazione, e l'autenticita' e l'integrita' degli attributi identificativi in esso contenuti, devono essere verificate garantendone al contempo la riservatezza (per un documento digitale cio' puo' implicare la validazione di una firma digitale sul documento; per un documento fisico, cio' puo' avvenire tramite firme o sigilli fisici, loghi e altri elementi visivi, ed esaminando il documento per rilevare falsificazioni e manomissioni; quando gli attributi provengono da un Portafoglio Europeo di Identita' Digitale o mezzo eID simile, il protocollo utilizzato puo' garantire autenticita', integrita' e riservatezza).",
        "testo_integrale": "VAL-8.3.8-02X: The identity of the issuer of the document or attestation, and the authenticity and integrity of the contained identity attributes, shall be verified while ensuring their confidentiality. NOTE 2: For a digital document, this can imply validating a digital signature on the document or attestation. The identity proofing context can pose requirements that a digital signature is required to fulfil to be accepted. NOTE 3: When attributes are conveyed from a European Digital Identity Wallet as specified by the amended eIDAS regulation [i.25] or similar eID means, the protocol used can guarantee authenticity, integrity and confidentiality. NOTE 4: For a physical document, this can be by physical signatures or seals, logos and other visual elements, and by examining the document to detect falsification and tampering.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se documenti o attestazioni sono usati come evidenza supplementare nel processo di identity proofing (clausola 8.3.8)",
    },
    {
        "riferimento": "VAL-8.3.8-03",
        "testo": "Se il documento o l'attestazione e' in forma fisica o in forma digitale resa per la validazione umana, il processo di identity proofing deve verificare che il documento presentato sia visivamente uguale all'aspetto atteso.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.8-03: If a document or attestation is in physical form or digital form rendered for human validation, the identity proofing process shall verify that the document presented is visually equal to the expected visual appearance.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se documenti o attestazioni sono usati come evidenza supplementare nel processo di identity proofing (clausola 8.3.8) e il documento o l'attestazione e' in forma fisica o in forma digitale resa per la validazione umana",
    },
    {
        "riferimento": "VAL-8.3.8-04",
        "testo": "Se il documento o l'attestazione e' in forma fisica e il tipo di documento contiene elementi di sicurezza, tali elementi devono essere verificati nella misura richiesta dal contesto di identity proofing.",
        "testo_integrale": "[CONDITIONAL] VAL-8.3.8-04: If a document or attestation is in physical form and the document type contains security elements, these security elements shall be verified to the extent required by the identity proofing context.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se documenti o attestazioni sono usati come evidenza supplementare nel processo di identity proofing (clausola 8.3.8), il documento o l'attestazione e' in forma fisica e il tipo di documento contiene elementi di sicurezza",
    },
    {
        "riferimento": "VAL-8.3.8-05X",
        "testo": "La procedura da applicare in caso di discrepanze tra gli attributi identificativi ottenuti da documenti e attestazioni e gli attributi identificativi da altre evidenze deve essere specificata nella dichiarazione delle pratiche.",
        "testo_integrale": "VAL-8.3.8-05X: The procedure to apply in case of discrepancies between the identity attributes obtained from documents and attestations and identity attributes from other evidence shall be specified in the practice statement. EXAMPLE: The identity attributes obtained from documents and attestations can be regarded as authoritative and override other sources of identity attributes, or other evidence can be regarded as authoritative, or an arbitration procedure can be used. The identity proofing context can pose requirements.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
        "condizione_applicabilita": "si applica se documenti o attestazioni sono usati come evidenza supplementare nel processo di identity proofing (clausola 8.3.8)",
    },
]

RIGHE_PRINCIPI: list[dict] = [
    # 8.3.2
    {
        "riferimento": "clausola 8.3.2 (ambito di applicazione)",
        "testo": "Se un documento di identita' digitale e' usato come evidenza autoritativa, si applicano i requisiti della presente sottoclausola (alcune legislazioni limitano l'accesso al chip delle carte d'identita' nazionali per la lettura del documento di identita' digitale o della foto del volto: se tali limitazioni si applicano a un documento usato nel contesto di identity proofing, il documento digitale non puo' essere usato come evidenza).",
        "testo_integrale": "[CONDITIONAL] If a digital identity document is used as authoritative evidence, the requirements in the present clause apply. NOTE 1: Some legislations restrict access to the chip of national identity cards for reading of the digital identity document or of the face photo. If such restrictions apply to a document used in an identity proofing context, the digital document cannot be used as evidence.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "VAL-8.3.2-00",
        "testo": "La validazione con successo di un documento di identita' digitale implica che il documento di identita' come evidenza e' validato e che gli attributi identificativi trasmessi dal documento di identita' sono validati.",
        "testo_integrale": "VAL-8.3.2-00: Successful validation of a digital identity document shall imply that the identity document as evidence is validated and that the identity attributes conveyed from the identity document are validated.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "si applica se un documento di identita' digitale e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.2)",
    },
    # 8.3.3
    {
        "riferimento": "clausola 8.3.3 (ambito di applicazione)",
        "testo": "Se un documento di identita' fisico e' usato come evidenza autoritativa, si applicano i requisiti della presente sottoclausola (un documento di identita' fisico puo' essere usato con la presenza fisica del richiedente o da remoto, presentando il documento davanti a una telecamera).",
        "testo_integrale": "[CONDITIONAL] If a physical identity document is used as authoritative evidence, the requirements in the present clause apply. NOTE 1: A physical identity document can be used with the applicant's physical presence and remotely by the applicant presenting the document in front of a camera.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "VAL-8.3.3-00",
        "testo": "La validazione con successo di un documento di identita' fisico implica che il documento di identita' come evidenza e' validato e che gli attributi identificativi trasmessi dal documento di identita' sono validati.",
        "testo_integrale": "VAL-8.3.3-00: Successful validation of a physical identity document shall imply that the identity document as evidence is validated and that the identity attributes conveyed from the identity document are validated.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "si applica se un documento di identita' fisico e' usato come evidenza autoritativa nel processo di identity proofing (clausola 8.3.3)",
    },
    # 8.3.4
    {
        "riferimento": "clausola 8.3.4 (ambito di applicazione)",
        "testo": "Se l'autenticazione tramite un mezzo eID esistente e' usata come evidenza, si applicano i requisiti della presente sottoclausola.",
        "testo_integrale": "[CONDITIONAL] If authentication by use of an existing eID means is used as evidence, the requirements in the present clause apply.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "VAL-8.3.4-02",
        "testo": "L'autenticazione con successo implica che il mezzo eID come evidenza e' validato e che gli attributi identificativi trasmessi dal mezzo eID sono validati e associati al richiedente (il mezzo eID puo' rappresentare una persona fisica, una persona giuridica, o una persona fisica che rappresenta una persona giuridica; il protocollo di autenticazione puo' includere attributi trasmessi da un Portafoglio Europeo di Identita' Digitale secondo il regolamento eIDAS modificato o mezzo eID simile).",
        "testo_integrale": "VAL-8.3.4-02: Successful authentication shall imply that the eID means as evidence is validated and that the identity attributes conveyed from the eID means are validated and bound to the applicant. NOTE 1: The eID means can represent a natural person, a legal person, or a natural person representing a legal person. NOTE 2: The authentication protocol can include attributes conveyed from a European Digital Identity Wallet as specified by the amended eIDAS regulation [i.25] or similar eID means.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "si applica se l'autenticazione tramite un mezzo eID esistente e' usata come evidenza nel processo di identity proofing (clausola 8.3.4)",
    },
    # 8.3.5
    {
        "riferimento": "clausola 8.3.5 (ambito di applicazione)",
        "testo": "Se una firma digitale con certificato e' usata come evidenza, si applicano i requisiti della presente sottoclausola.",
        "testo_integrale": "[CONDITIONAL] If a digital signature with certificate is used as evidence, the requirements in the present clause apply.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "VAL-8.3.5-00",
        "testo": "La validazione con successo della firma digitale implica che gli attributi identificativi trasmessi dal certificato a supporto della firma digitale sono validati e associati al richiedente (di norma un risultato TOTAL-PASSED secondo ETSI EN 319 102-1; il certificato puo' rappresentare una persona fisica, una persona giuridica, o una persona fisica che rappresenta una persona giuridica).",
        "testo_integrale": "VAL-8.3.5-00: Successful validation of the digital signature shall imply that the identity attributes conveyed from the certificate supporting the digital signature are validated and bound to the applicant. NOTE 1: Usually, this means that the validation result is TOTAL-PASSED as defined by ETSI EN 319 102-1 [i.5]. NOTE 2: The certificate can represent a natural person, a legal person, or a natural person representing a legal person.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "si applica se una firma digitale con certificato e' usata come evidenza nel processo di identity proofing (clausola 8.3.5)",
    },
    # 8.3.6
    {
        "riferimento": "clausola 8.3.6 (ambito di applicazione)",
        "testo": "Se un registro fidato e' usato come evidenza supplementare, si applicano i requisiti della presente sottoclausola (un registro fidato puo' essere una fonte autentica come definita dal regolamento eIDAS modificato).",
        "testo_integrale": "NOTE 1: A trusted register can be an authentic source as defined by the amended eIDAS regulation [i.25]. [CONDITIONAL] If a trusted register is used as supplementary evidence in an identity proofing process, the requirements in the present clause apply.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "VAL-8.3.6-00",
        "testo": "L'autenticazione con successo di un registro fidato e la validazione dell'autenticita' e dell'integrita' della comunicazione con il registro fidato implicano che la dichiarazione del registro fidato sulla validita' degli attributi identificativi sia fidata (il registro fidato puo' essere usato in due modi: interrogato per trasmettere attributi registrati sul richiedente, oppure inviandogli attributi gia' raccolti per la validazione, con risposta anche solo si'/no).",
        "testo_integrale": "VAL-8.3.6-00: Successful authentication of a trusted register and validation of authenticity and integrity of the communication with the trusted register shall imply that the statement of the trusted register on validity of identity attributes is trusted. NOTE 2: A trusted register can be used in two ways: either the trusted register can be queried to convey identity attributes registered on the applicant, or previously collected attributes can be sent to the trusted register for validation. In the latter case, the response can be just a yes/no answer on validity of the attributes.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "si applica se un registro fidato e' usato come evidenza supplementare nel processo di identity proofing (clausola 8.3.6)",
    },
    # 8.3.7
    {
        "riferimento": "clausola 8.3.7 (ambito di applicazione)",
        "testo": "Se una prova di accesso e' usata come evidenza supplementare, si applicano i requisiti della presente sottoclausola.",
        "testo_integrale": "[CONDITIONAL] If proof of access is used as supplementary evidence in an identity proofing process, the requirements in the present clause apply.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "VAL-8.3.7-00",
        "testo": "La validazione con successo della prova di accesso implica che gli attributi identificativi trasmessi dalla prova di accesso sono validati.",
        "testo_integrale": "VAL-8.3.7-00: Successful validation of proof of access shall imply that the identity attributes conveyed from the proof of access are validated.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "si applica se una prova di accesso e' usata come evidenza supplementare nel processo di identity proofing (clausola 8.3.7)",
    },
    # 8.3.8
    {
        "riferimento": "clausola 8.3.8 (ambito di applicazione)",
        "testo": "Se documenti o attestazioni sono usati come evidenza supplementare, si applicano i requisiti della presente sottoclausola (le attestazioni possono essere attestazioni elettroniche (qualificate) di attributi come definite dal regolamento eIDAS modificato).",
        "testo_integrale": "NOTE 1: Attestations can be (qualified) electronic attestation of attributes as defined by the amended eIDAS regulation [i.25]. [CONDITIONAL] If documents and attestations are used as supplementary evidence in an identity proofing process, the requirements in the present clause apply.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "VAL-8.3.1-01X", "VAL-8.3.1-02", "VAL-8.3.1-03X", "VAL-8.3.1-04X",
    "VAL-8.3.1-05", "VAL-8.3.1-06X", "VAL-8.3.1-07", "VAL-8.3.1-08X",
    "VAL-8.3.1-10X", "VAL-8.3.1-11X", "VAL-8.3.1-12",
    "clausola 8.3.2 (ambito di applicazione)", "VAL-8.3.2-00", "VAL-8.3.2-01",
    "VAL-8.3.2-02", "VAL-8.3.2-03", "VAL-8.3.2-04X", "VAL-8.3.2-04A",
    "VAL-8.3.2-05", "VAL-8.3.2-06",
    "clausola 8.3.3 (ambito di applicazione)", "VAL-8.3.3-00", "VAL-8.3.3-01",
    "VAL-8.3.3-02X", "VAL-8.3.3-03", "VAL-8.3.3-04X", "VAL-8.3.3-04A",
    "VAL-8.3.3-04B", "VAL-8.3.3-04C", "VAL-8.3.3-05X", "VAL-8.3.3-05A",
    "VAL-8.3.3-05B", "VAL-8.3.3-05C", "VAL-8.3.3-05D", "VAL-8.3.3-06",
    "VAL-8.3.3-07X", "VAL-8.3.3-07A", "VAL-8.3.3-07B", "VAL-8.3.3-07C",
    "VAL-8.3.3-08", "VAL-8.3.3-09", "VAL-8.3.3-10", "VAL-8.3.3-11",
    "VAL-8.3.3-12X", "VAL-8.3.3-13", "VAL-8.3.3-14X", "VAL-8.3.3-14A",
    "VAL-8.3.3-15X", "VAL-8.3.3-16", "VAL-8.3.3-17", "VAL-8.3.3-18",
    "VAL-8.3.3-19X", "VAL-8.3.3-20",
    "clausola 8.3.4 (ambito di applicazione)", "VAL-8.3.4-01X", "VAL-8.3.4-02",
    "clausola 8.3.5 (ambito di applicazione)", "VAL-8.3.5-00", "VAL-8.3.5-01",
    "VAL-8.3.5-02X",
    "clausola 8.3.6 (ambito di applicazione)", "VAL-8.3.6-00", "VAL-8.3.6-01",
    "VAL-8.3.6-02", "VAL-8.3.6-03", "VAL-8.3.6-04", "VAL-8.3.6-05X",
    "VAL-8.3.6-06X",
    "clausola 8.3.7 (ambito di applicazione)", "VAL-8.3.7-00", "VAL-8.3.7-01",
    "VAL-8.3.7-02X", "VAL-8.3.7-03", "VAL-8.3.7-04", "VAL-8.3.7-05X",
    "clausola 8.3.8 (ambito di applicazione)", "VAL-8.3.8-01", "VAL-8.3.8-02X",
    "VAL-8.3.8-03", "VAL-8.3.8-04", "VAL-8.3.8-05X",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "VAL-8.3.1-10X"),
        "nodo_a": ("obbligo", None, "VAL-8.3.3-07X"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "VAL-8.3.1-10X"),
        "nodo_a": ("obbligo", None, "VAL-8.3.3-07A"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "VAL-8.3.3-05B"),
        "nodo_a": ("obbligo", None, "OVR-5-07"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "VAL-8.3.3-05B"),
        "nodo_a": ("obbligo", None, "OVR-5-08"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
