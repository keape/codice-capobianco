"""ETSI EN 319 421 V1.3.1 (2025-07) - Electronic Signatures and Trust
Infrastructures (ESI); Policy and Security Requirements for Trust Service
Providers issuing Time-Stamps. Fonte 18 (la numerazione degli id e' risolta
per riferimento dalla sessione principale in app/seed.py - questo modulo NON
tocca seed.py). Capitolo 1: clausole 1 (Scope), 2 (References: 2.1 Normative
references, 2.2 Informative references), 3 (Definition of terms, symbols,
abbreviations and notation: 3.1 Terms, 3.2 Symbols, 3.3 Abbreviations, 3.4
Notation), 4 (General concepts: 4.1 General policy requirements concepts,
4.2 Time-stamping services, 4.3 Time-Stamping Authority (TSA), 4.4
Subscriber, 4.5 Time-stamp policy and TSA practice statement). Testo
ufficiale in app/.source_cache/etsi_319_421/cap01.txt (letto sempre con
selettore `:raw`, altrimenti il tool tronca le righe lunghe a 768 caratteri
introducendo "…" e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_319_421/manifest.json.

Modellazione (ADR-0007), stesso criterio gia' applicato ai quattro standard
ETSI gia' censiti (ETSI TS 119 461, ETSI EN 319 401, ETSI EN 319 412, ETSI
TS 119 431, ETSI EN 319 411) e adattato alle clausole/sottoclausole di uno
standard tecnico: un nodo per ogni requisito numerato; per le clausole di
cornice prive di requisito numerato un solo nodo Principio dedicato. Questo
capitolo non contiene alcun requisito numerato: 0 Obblighi, 9 Principi.
Scelte voce per voce:

- Clausola 1 (Scope) -> 1 Principio "scopo/ambito di applicazione",
  riferimento "clausola 1 (Scope)". Perimetro in senso proprio: dichiara a
  chi si applica il documento (TSP che emettono marche temporali), a cosa
  servono tali marche (supporto a firme digitali o a qualunque applicazione
  che debba provare che un dato esisteva prima di un certo momento), che il
  documento puo' essere usato da organismi indipendenti come base per
  confermare l'affidabilita' di un TSP, e cosa il documento NON copre
  (protocolli di accesso alle TSU; modalita' di valutazione da parte di una
  parte indipendente). Le tre NOTE ufficiali sono mantenute in
  `testo_integrale`: NOTE 1 individua dove e' definito il protocollo di
  marcatura temporale (IETF RFC 3161 con aggiornamento RFC 5816, profilato
  in ETSI EN 319 422), NOTE 2 rinvia a ETSI EN 319 403-1 per la guida sulla
  valutazione dei processi e servizi del TSP, NOTE 3 dichiara la dipendenza
  del documento da ETSI EN 319 401 per i requisiti generali comuni a tutte
  le classi di servizi del TSP. Tutte e tre delimitano il perimetro
  applicativo del documento (cosa e' coperto, cosa e' demandato, su cosa il
  documento si fonda), quindi non sono mera bibliografia decorativa e sono
  assorbite.
- Clausola 2 (References: 2.1 Normative references, 2.2 Informative
  references) -> NESSUN nodo, NESSUN item di indice. E' bibliografia/
  paratesto puro: un elenco di documenti citati numerati [1]-[8] (normative)
  e [i.1]-[i.19] (informative) con le sole regole redazionali ETSI su
  riferimenti specifici/non specifici, nessun contenuto normativo autonomo
  ne' effetto giuridico proprio. Stesso trattamento gia' riservato alla
  clausola 2 di ETSI EN 319 401 (cap01) e di ETSI TS 119 461. La numerazione
  stessa e' resa in modo spurio dalla conversione PDF->markdown (le etichette
  [i.N] arrivano disallineate rispetto ai titoli dei documenti, con [i.10]
  "Void." riportato a parte), il che conferma che nulla di prescrittivo va
  estratto da questa clausola.
- Clausola 3.1 (Terms) -> 1 Principio "definitorio" riassuntivo, NON un nodo
  per singolo termine: la clausola e' un glossario alfabetico piatto senza
  struttura a lettere/numeri propria, quindi 16 nodi sarebbero 16 item di
  indice fittizi per un'unica clausola. Il testo rinvia ai termini gia'
  dati in ETSI EN 319 401 [4] e definisce 16 termini propri del documento:
  certificate validity period; Coordinated Universal Time (UTC); leap
  second; relying party; secure cryptographic device; subscriber;
  time-stamp; time-stamp policy; Time-Stamping Authority (TSA);
  time-stamping service; Time-Stamping Unit (TSU); trust service; Trust
  Service Provider (TSP); TSA disclosure statement; TSA practice statement;
  UTC(k). In
  `testo_integrale` sono riportate tutte le definizioni verbatim con le
  relative NOTE. Trattamento delle NOTE della clausola: la NOTE redazionale
  iniziale ("Where a definition is copied from a referenced document this is
  indicated by inclusion of the reference identifier number at the end of
  the definition or in a note") e' mantenuta perche' spiega la convenzione
  di marcatura dei rinvii usata da tutto il glossario; la NOTE su
  notBefore/notAfter ("The notBefore and notAfter terms are defined in IETF
  RFC 5280 [i.18]") e' mantenuta perche' completa la definizione di
  "certificate validity period" indicando dove sono definiti gli estremi
  temporali ivi citati; la NOTE lunga su UTC (compromesso tra tempo atomico
  TAI e tempo solare, relazione con GMST, rinvio all'annex C) e' NOTE
  interpretativa e va mantenuta; la NOTE su "time-stamp policy" (tipo
  specifico di trust service policy definito in ETSI EN 319 401 [4]), quella
  su "TSA practice statement" (tipo specifico di trust service practice
  statement) e quella su UTC(k) (elenco dei laboratori in clausola 1 di
  Circular T [i.6] diffuso dal BIPM, con URL) sono anch'esse mantenute
  perche' precisano la natura/il perimetro del concetto definito. Nessuna
  NOTE puramente bibliografica da scartare in questa clausola.
- Clausola 3.2 (Symbols) -> NESSUN nodo, NESSUN item di indice: il testo
  della clausola e' integralmente "Void." senza alcun contenuto oltre il
  segnaposto; stesso trattamento gia' riservato a clausola 3.2 di ETSI EN
  319 401.
- Clausola 3.3 (Abbreviations) -> 1 Principio "definitorio" riassuntivo. La
  clausola rinvia alle abbreviazioni gia' date in ETSI EN 319 401 [4] e ne
  aggiunge 15 proprie: BIPM (Bureau International des Poids et Mesures),
  BTSP (Best practices Time-Stamp Policy), CA (Certification Authority), CID
  (Commission Implementing Decision), EAL (Evaluation Assurance Level), IERS
  (International Earth Rotation and Reference System Service), IT
  (Information Technology), NIST (National Institute of Standards and
  Technology), OVR (General requirement), TAI (International Atomic Time),
  TIS (Time-stamp Issuance Services), TSA (Time-Stamping Authority), TSP
  (Trust Service Provider), TSU (Time-Stamping Unit), UTC (Coordinated
  Universal Time). La conversione PDF->markdown rende la tabella come un
  unico flusso etichetta/forma estesa alternato (una riga piatta, non una
  tabella a due colonne), ma l'alternanza e' qui completa e non ambigua:
  ogni etichetta e' immediatamente seguita dalla propria forma estesa, come
  verificato sul raw di app/.source_cache/etsi_319_421/cap01.txt. In
  `testo_integrale` le coppie sono riportate in forma esplicita
  "ETICHETTA: Forma estesa." per non lasciare la ricostruzione implicita.
  OVR e TIS non sono mere abbreviazioni: sono i due prefissi (service
  components) della notazione dei requirement id definita in clausola 3.4,
  per cui sono riportate anche nella relativa riga di Principio.
- Clausola 3.4 (Notation) -> 1 Principio "definitorio", riferimento
  "clausola 3.4 (Notation)". NODO CRUCIALE per l'intero documento e per i
  capitoli successivi (cap02-cap06): riporta la legenda COMPLETA e verbatim
  (a) delle tre categorie di requisiti - nessuna marcatura (requisito
  applicabile a qualunque policy), "[CONDITIONAL]" (requisito applicabile
  solo a certe condizioni), "[CHOICE]" (requisito che comprende piu' opzioni
  da selezionare secondo la situazione applicabile); (b) del formato
  dell'identificatore di requisito <3 lettere service component>-<numero di
  clausola>-<numero progressivo a 2 cifre>; (c) delle due sole famiglie di
  prefisso usate nel documento: OVR (General requirement, requisito
  applicabile a piu' di una componente) e TIS (Time-stamp Issuance
  Services); (d) delle quattro regole di gestione degli identificatori per
  le edizioni successive (inserimento in coda -> incremento del progressivo;
  inserimento tra due requisiti esistenti -> lettere maiuscole aggiunte
  all'id del requisito precedente; requisito cancellato -> id mantenuto e
  completato con "Void"; requisito modificato -> id lasciato void e nuovo
  requisito identificato da lettera/e maiuscola/e aggiunta/e al numero
  iniziale). Questa e' la regola che spiega i suffissi letterali
  (es. OVR-5.2-01A) che i capitoli successivi incontreranno: gli id con
  lettera aggiunta sono requisiti distinti e vanno modellati come nodi
  distinti. Si noti che in questa versione lo standard NON usa la marcatura
  "[PRO]" ne' il prefisso REQ di ETSI EN 319 401: i prefissi sono solo OVR
  e TIS, quindi la notazione NON va copiata per analogia da EN 319 401.
- Clausola 4.1 (General policy requirements concepts) -> 1 Principio
  "scopo/ambito di applicazione". Non definisce un concetto nuovo ma
  stabilisce la cornice dei requisiti generali di policy applicabili: rinvia
  a ETSI EN 319 401 [4] per i requisiti generici comuni a tutte le classi di
  servizi del TSP, dichiara che tali requisiti di policy si fondano sull'uso
  di crittografia a chiave pubblica, certificati a chiave pubblica e fonti
  temporali affidabili, e stabilisce che sottoscrittori e terzi affidanti
  sono tenuti a consultare la TSA practice statement per i dettagli su come
  la specifica time-stamp policy e' implementata dalla singola TSA (es. i
  protocolli usati). E' perimetro/vincolativita' di cornice, non definizione
  di un concetto, per cui "scopo/ambito di applicazione" e' piu' preciso di
  "definitorio". Nessun requisito numerato, quindi nessun Obbligo; la
  formulazione "are expected to consult" (aspettativa, non "shall") non
  impone un obbligo prescrittivo, coerente con il criterio gia' adottato per
  le clausole discorsive.
- Clausola 4.2 (Time-stamping services) -> 1 Principio "definitorio".
  Definisce la scomposizione del servizio di marcatura temporale nelle due
  componenti usate per classificare i requisiti nei capitoli successivi:
  "Time-stamping provision" (genera marche temporali) e "Time-stamping
  management" (monitora e controlla l'operazione del servizio, con
  responsabilita' di installazione e disinstallazione della componente di
  provision; EXAMPLE: garantisce che l'orologio usato per la marcatura sia
  correttamente sincronizzato con UTC), precisando che la suddivisione vale
  solo ai fini della chiarezza dei requisiti e non pone restrizioni su alcuna
  partizione implementativa. E' classificazione definitoria di concetti, non
  perimetro di applicazione del documento: "definitorio".
- Clausola 4.3 (Time-Stamping Authority (TSA)) -> 1 Principio "definitorio".
  Definisce chi e' la TSA (TSP che fornisce servizi di marcatura temporale
  al pubblico) e l'allocazione delle responsabilita': responsabilita'
  complessiva sull'erogazione dei servizi di clausola 4.2; responsabilita'
  sull'operazione di una o piu' TSU che creano e firmano per conto della
  TSA; identificabilita' della TSA che emette una marca temporale (il testo
  cita letteralmente "see TIS-7.7.1-08"); possibilita' di avvalersi di terze
  parti per parti del servizio con mantenimento della responsabilita'
  complessiva (as per clause 6.5) e dell'assicurazione del rispetto dei
  requisiti; EXAMPLE del subappalto integrale con chiavi private
  identificabili come appartenenti alla TSA; possibilita' di operare piu'
  unita' di marcatura identificabili; qualificazione della TSA come trust
  service provider ai sensi di ETSI EN 319 401 [4]. Il testo e' dichiarativo
  (nessun "shall": usa "is called", "has overall responsibility", "may make
  use of"), quindi non genera Obblighi ma un solo Principio definitorio che
  fissa il concetto e la titolarita' delle responsabilita'. NOTA di
  coordinamento per la sessione principale: in questa clausola compare la
  citazione letterale di un requirement id ("(see TIS-7.7.1-08)"), che
  punta a un requisito del capitolo 4 (clausola 7.7.1). Non e' stata
  inserita una relazione "richiama": l'assegnazione di questo capitolo fissa
  `RELAZIONI` a vuoto, e cap01 e' inserito per primo dalla sessione
  principale, quindi il nodo di destinazione (cap04) non sarebbe ancora
  risolvibile nel registro al momento dell'INSERT. La citazione resta
  comunque integralmente riportata in `testo_integrale`; l'eventuale
  relazione va costruita a posteriori (Fase 6 / ADR-0009) oppure
  riassegnando la relazione al capitolo che possiede il nodo di
  destinazione.
- Clausola 4.4 (Subscriber) -> 1 Principio "definitorio". Definisce il
  regime di imputazione degli obblighi del sottoscrittore: quando il
  sottoscrittore e' un'organizzazione, essa comprende piu' utenti finali (o
  un singolo utente finale) e alcuni obblighi dell'organizzazione si
  applicano anche agli utenti finali; l'organizzazione resta comunque
  responsabile se gli obblighi degli utenti finali non sono correttamente
  adempiuti e pertanto e' tenuta a informare adeguatamente i propri utenti
  finali; quando il sottoscrittore e' un utente finale, questi e' tenuto
  direttamente responsabile dell'adempimento. Il testo e' dichiarativo ("is
  an organization", "will be held responsible", "is expected to") senza
  requisito numerato: definisce la nozione di sottoscrittore e il criterio di
  responsabilita', quindi "definitorio" e non "scopo/ambito di
  applicazione".
- Clausola 4.5 (Time-stamp policy and TSA practice statement) -> 1 Principio
  "definitorio". Definisce i ruoli relativi di time-stamp policy e TSA
  practice statement senza porre restrizioni sulla loro forma: una
  time-stamp policy e' una forma di Trust Service Policy ai sensi di ETSI EN
  319 401 [4] applicabile ai TSP che emettono marche temporali; la TSA
  Practice Statement e' una forma di Trust Service Practice Statement ai
  sensi di ETSI EN 319 401 [4] applicabile ai TSP che emettono marche
  temporali; il documento specifica una time-stamp policy per soddisfare i
  requisiti generali dei servizi di marcatura temporale affidabili, mentre le
  TSA specificano nelle proprie practice statement come tali requisiti sono
  soddisfatti. E' definizione di due concetti e del loro rapporto, quindi
  "definitorio" e non "scopo/ambito di applicazione".

Copertura di clausola 2 e 3.2: escluse dall'indice per i motivi sopra (la
copertura aggregata dei 6 capitoli della Fonte 18 e' verificata
programmaticamente dalla sessione principale: ogni item di indice deve
essere coperto esattamente una volta, quindi clausola 2 e clausola 3.2 non
compaiono ne' qui ne' altrove, coerentemente con il manifest di split).

RELAZIONI: una sola, interna alla Fonte 18. L'unica citazione letterale di un
requirement id dell'intero capitolo e' in clausola 4.3 ("see TIS-7.7.1-08",
identificazione del TSA responsabile dell'emissione): e' una citazione
letterale puntuale, quindi genera una relazione tipizzata "richiama"
(Principio 4.3 -> Obbligo TIS-7.7.1-08, che vive nel capitolo 4 ma e'
risolvibile via registro perche' `inserisci_capitoli` risolve tutte le
relazioni dopo aver inserito le righe di tutti i capitoli della stessa
chiamata). I rinvii di clausola ("see annex C" in 3.1, "as per clause 6.5" e
"clause 4.2" in 4.3, "ETSI EN 319 401 [4]" in piu' clausole) NON generano
relazioni: sono rinvii di clausola o a standard esterni, non citazioni
letterali di un requirement id, e la costruzione di relazioni cross-fonte e'
demandata alla Fase 6 della sessione principale (ADR-0009).
"""

RIGHE_OBBLIGHI: list[dict] = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 1 (Scope)",
        "testo": (
            "Il documento specifica requisiti di policy e di sicurezza relativi alle prassi operative e di "
            "gestione dei TSP che emettono marche temporali; tali requisiti di policy si applicano ai TSP che "
            "emettono marche temporali. Le marche temporali possono essere usate a supporto di firme digitali "
            "o per qualunque applicazione che debba provare che un dato esisteva prima di un momento "
            "determinato. Il documento puo' essere usato da organismi indipendenti come base per confermare "
            "che un TSP e' affidabile nell'emettere marche temporali. Il documento non specifica i protocolli "
            "usati per accedere alle TSU, ne' come i requisiti individuati possano essere valutati da una "
            "parte indipendente (inclusi i requisiti sulle informazioni da rendere disponibili a tali "
            "valutatori indipendenti e i requisiti sui valutatori stessi)."
        ),
        "testo_integrale": (
            "1 Scope: The present document specifies policy and security requirements relating to the "
            "operation and management practices of TSPs issuing time-stamps. These policy requirements are "
            "applicable to TSPs issuing time-stamps. Such time-stamps can be used in support of digital "
            "signatures or for any application requiring to prove that a datum existed before a particular "
            "time. The present document can be used by independent bodies as the basis for confirming that a "
            "TSP can be trusted for issuing time-stamps. The present document does not specify protocols used "
            "to access the TSUs. NOTE 1: A time-stamping protocol is defined in IETF RFC 3161 [i.2] including "
            "optional update in IETF RFC 5816 [i.3] and profiled in ETSI EN 319 422 [5]. The present document "
            "does not specify how the requirements identified can be assessed by an independent party, "
            "including requirements for information to be made available to such independent assessors, or "
            "requirements on such assessors. NOTE 2: See ETSI EN 319 403-1 [i.9] for guidance on assessment "
            "of TSP's processes and services. NOTE 3: The present document references ETSI EN 319 401 [4] for "
            "general policy requirements common to all classes of TSP's services."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.1 (Terms)",
        "testo": (
            "La clausola rinvia ai termini definiti in ETSI EN 319 401 [4] e definisce 16 termini propri del "
            "documento: 'certificate validity period' (intervallo temporale, estremi inclusi, durante il quale "
            "la Certification Authority garantisce di mantenere le informazioni sullo stato del certificato); "
            "'Coordinated Universal Time (UTC)' (scala temporale basata sul secondo come definito nella "
            "Raccomandazione ITU-R TF.460-6); 'leap second' (secondo saltato o aggiunto nell'ultimo secondo di "
            "un mese UTC); 'relying party' (destinatario di una marca temporale che su di essa si affida); "
            "'secure cryptographic device' (dispositivo che detiene la chiave privata dell'utente, la protegge "
            "dal compromesso ed esegue funzioni di firma o decifratura per conto dell'utente); 'subscriber' "
            "(persona giuridica o fisica a cui e' emessa una marca temporale e che e' vincolata a obblighi di "
            "sottoscrittore); 'time-stamp' (dati in forma elettronica che legano altri dati elettronici a un "
            "momento determinato, provando che quei dati esistevano a quel momento); 'time-stamp policy' "
            "(insieme denominato di regole che indica l'applicabilita' di una marca temporale a una comunita' "
            "e/o classe di applicazioni con requisiti di sicurezza comuni; tipo specifico di trust service "
            "policy); 'Time-Stamping Authority (TSA)' (TSP che fornisce servizi di marcatura temporale tramite "
            "una o piu' unita' di marcatura); 'time-stamping service' (servizio fiduciario di emissione di "
            "marche temporali); 'Time-Stamping Unit (TSU)' (insieme di hardware e software gestito come unita' "
            "con una sola chiave di firma di marca temporale attiva per volta); 'trust service' (servizio "
            "elettronico che accresce fiducia e affidabilita' nelle transazioni elettroniche); 'Trust Service "
            "Provider (TSP)' (entita' che fornisce uno o piu' servizi fiduciari); 'TSA disclosure statement' "
            "(insieme di dichiarazioni sulle policy e prassi di una TSA che richiedono particolare enfasi o "
            "disclosure verso sottoscrittori e terzi affidanti, ad esempio per soddisfare requisiti "
            "regolatori); 'TSA practice statement' (dichiarazione delle prassi che una TSA impiega "
            "nell'emettere marche temporali; tipo specifico di trust service practice statement); 'UTC(k)' "
            "(scala temporale realizzata dal laboratorio 'k' e mantenuta in stretto accordo con UTC, con "
            "obiettivo di raggiungere ±100 ns)."
        ),
        "testo_integrale": (
            "3.1 Terms: For the purposes of the present document, the terms given in ETSI EN 319 401 [4] and "
            "the following apply: NOTE: Where a definition is copied from a referenced document this is "
            "indicated by inclusion of the reference identifier number at the end of the definition or in a "
            "note. certificate validity period: time interval (notBefore and notAfter inclusive) during which "
            "the Certification Authority (CA) warrants that it will maintain information about the status of "
            "the certificate NOTE: The notBefore and notAfter terms are defined in IETF RFC 5280 [i.18]. "
            "Coordinated Universal Time (UTC): time scale based on the second as defined in Recommendation "
            "ITU-R TF.460-6 [1] NOTE: For most practical purposes UTC is equivalent to mean solar time at the "
            "prime meridian (0°). More specifically, UTC is a compromise between the highly stable atomic time "
            "(Temps Atomique International-TAI) and solar time derived from the irregular Earth rotation "
            "(related to the Greenwich Mean Sidereal Time (GMST) by a conventional relationship) (see annex C "
            "for more details). leap second: adjustment to UTC by skipping or adding an extra second on the "
            "last second of a UTC month relying party: recipient of a time-stamp who relies on that time-stamp "
            "secure cryptographic device: device which holds the user's private key, protects this key against "
            "compromise and performs signing or decryption functions on behalf of the user subscriber: legal "
            "or natural person to whom a time-stamp is issued and who is bound to any subscriber obligations "
            "time-stamp: data in electronic form which binds other electronic data to a particular time "
            "establishing evidence that these data existed at that time time-stamp policy: named set of rules "
            "that indicates the applicability of a time-stamp to a particular community and/or class of "
            "application with common security requirements NOTE: This is a specific type of trust service "
            "policy as defined in ETSI EN 319 401 [4]. Time-Stamping Authority (TSA): TSP providing "
            "time-stamping services using one or more time-stamping units time-stamping service: trust "
            "service for issuing time-stamps Time-Stamping Unit (TSU): set of hardware and software which is "
            "managed as a unit and has a single time-stamp signing key active at a time trust service: "
            "electronic service that enhances trust and confidence in electronic transactions Trust Service "
            "Provider (TSP): entity which provides one or more trust services TSA disclosure statement: set of "
            "statements about the policies and practices of a TSA that particularly require emphasis or "
            "disclosure to subscribers and relying parties, for example to meet regulatory requirements TSA "
            "practice statement: statement of the practices that a TSA employs in issuing time-stamp NOTE: "
            "This is a specific type of trust service practice statement as defined in ETSI EN 319 401 [4]. "
            "UTC(k): time scale realized by the laboratory \"k\" and kept in close agreement with UTC, with "
            "the goal to reach ±100 ns NOTE: A list of UTC(k) laboratories is given in clause 1 of Circular T "
            "[i.6] disseminated by BIPM and available from the BIPM website (https://www.bipm.org/)."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.3 (Abbreviations)",
        "testo": (
            "La clausola rinvia alle abbreviazioni gia' date in ETSI EN 319 401 [4] e ne definisce 15 proprie: "
            "BIPM (Bureau International des Poids et Mesures), BTSP (Best practices Time-Stamp Policy), CA "
            "(Certification Authority), CID (Commission Implementing Decision), EAL (Evaluation Assurance "
            "Level), IERS (International Earth Rotation and Reference System Service), IT (Information "
            "Technology), NIST (National Institute of Standards and Technology), OVR (General requirement), "
            "TAI (International Atomic Time), TIS (Time-stamp Issuance Services), TSA (Time-Stamping "
            "Authority), TSP (Trust Service Provider), TSU (Time-Stamping Unit), UTC (Coordinated Universal "
            "Time). OVR e TIS sono i due prefissi (componenti di servizio) usati nella notazione degli "
            "identificatori dei requisiti definita in clausola 3.4."
        ),
        "testo_integrale": (
            "3.3 Abbreviations: For the purposes of the present document, the abbreviations given in ETSI EN "
            "319 401 [4] and the following apply: BIPM: Bureau International des Poids et Mesures. BTSP: Best "
            "practices Time-Stamp Policy. CA: Certification Authority. CID: Commission Implementing Decision. "
            "EAL: Evaluation Assurance Level. IERS: International Earth Rotation and Reference System "
            "Service. IT: Information Technology. NIST: National Institute of Standards and Technology. OVR: "
            "General requirement. TAI: International Atomic Time. TIS: Time-stamp Issuance Services. TSA: "
            "Time-Stamping Authority. TSP: Trust Service Provider. TSU: Time-Stamping Unit. UTC: Coordinated "
            "Universal Time."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.4 (Notation)",
        "testo": (
            "La clausola definisce la notazione degli identificatori dei requisiti. I requisiti si dividono in "
            "tre categorie: (a) applicabili a qualunque policy, indicati senza marcatura aggiuntiva; (b) "
            "applicabili solo a determinate condizioni, marcati '[CONDITIONAL]'; (c) comprensivi di piu' "
            "opzioni da selezionare secondo la situazione applicabile, marcati '[CHOICE]'. Ogni requisito e' "
            "identificato come <3 lettere di componente di servizio>-<numero di clausola>-<numero "
            "progressivo a 2 cifre>. Le componenti di servizio (prefissi) usate nel documento sono due: OVR "
            "(General requirement, requisito applicabile a piu' di una componente) e TIS (Time-stamp Issuance "
            "Services). La gestione degli identificatori per le edizioni successive del documento e' la "
            "seguente: un requisito inserito in coda a una clausola incrementa il numero progressivo a 2 cifre "
            "al primo valore disponibile; un requisito inserito tra due requisiti esistenti usa lettere "
            "maiuscole aggiunte all'identificatore del requisito precedente; l'identificatore di un requisito "
            "cancellato resta e viene completato con 'Void'; l'identificatore di un requisito modificato viene "
            "lasciato void e il requisito modificato e' identificato da lettera/e maiuscola/e aggiunta/e al "
            "numero iniziale del requisito."
        ),
        "testo_integrale": (
            "3.4 Notation: The requirements identified in the present document include: a) Requirements "
            "applicable to any policy. Such requirements are indicated by clauses without any additional "
            "marking. b) Requirements applicable under certain conditions. Such requirements are indicated by "
            "clauses marked by \"[CONDITIONAL]\". c) Requirements that include several choices which ought to "
            "be selected according to the applicable situation. Such requirements are indicated by clauses "
            "marked by \"[CHOICE]\". Each requirement is identified as follows: <3 letters service "
            "component>-< the clause number>- <2 digit number-incremental>. The service components are: - "
            "OVR: General requirement (requirement applicable to more than 1 component) - TIS: Time-stamp "
            "Issuance Services The management of the requirement identifiers for subsequent editions of the "
            "present document is as follows: - When a requirement is inserted at the end of a clause, the 2 "
            "digit number above is incremented to the next available digit. - When a requirement is inserted "
            "between two existing requirements, capital letters appended to the previous requirement "
            "identifier are used to distinguish new requirements. - The requirement identifier for deleted "
            "requirements is left and completed with \"Void\". - The requirement identifier for modified "
            "requirement is left void and the modified requirement is identified by capital letter(s) "
            "appended to the initial requirement number."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.1 (General policy requirements concepts)",
        "testo": (
            "Il documento rinvia a ETSI EN 319 401 [4] per i requisiti generici di policy comuni a tutte le "
            "classi di servizi dei trust service provider. Tali requisiti di policy si fondano sull'uso di "
            "crittografia a chiave pubblica, certificati a chiave pubblica e fonti temporali affidabili. "
            "Sottoscrittori e terzi affidanti sono tenuti a consultare la TSA practice statement per ottenere "
            "ulteriori dettagli su come la specifica time-stamp policy e' implementata dalla particolare TSA "
            "(es. i protocolli usati nell'erogare il servizio)."
        ),
        "testo_integrale": (
            "4.1 General policy requirements concepts: The present document references ETSI EN 319 401 [4] "
            "for generic policy requirements common to all classes of trust service providers service. These "
            "policy requirements are based upon the use of public key cryptography, public key certificates "
            "and reliable time sources. Subscriber and relying parties are expected to consult the TSA's "
            "practice statement to obtain further details of precisely how this time-stamp policy is "
            "implemented by the particular TSA (e.g. protocols used in providing this service)."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.2 (Time-stamping services)",
        "testo": (
            "L'erogazione dei servizi di marcatura temporale e' scomposta nel documento, ai fini della "
            "classificazione dei requisiti, nelle seguenti componenti di servizio: 'Time-stamping provision' "
            "(questa componente genera le marche temporali) e 'Time-stamping management' (questa componente "
            "monitora e controlla l'operazione dei servizi di marcatura temporale per assicurare che il "
            "servizio erogato sia come specificato dalla TSA; ha la responsabilita' dell'installazione e della "
            "disinstallazione della componente di provision; esempio: la gestione della marcatura temporale "
            "assicura che l'orologio usato per la marcatura sia correttamente sincronizzato con UTC). Tale "
            "suddivisione dei servizi vale solo ai fini della chiarezza dei requisiti specificati nel documento "
            "e non pone alcuna restrizione su come un'implementazione dei servizi di marcatura temporale "
            "possa essere suddivisa."
        ),
        "testo_integrale": (
            "4.2 Time-stamping services: The provision of time-stamping services is broken down in the present "
            "document into the following component services for the purposes of classifying requirements: - "
            "Time-stamping provision: This service component generates time-stamps. - Time-stamping "
            "management: This service component monitors and controls the operation of the time-stamping "
            "services to ensure that the service provided is as specified by the TSA. This service component "
            "has responsibility for the installation and de-installation of the time-stamping provision "
            "service. EXAMPLE: Time-stamping management ensures that the clock used for time-stamping is "
            "correctly synchronized with UTC. This subdivision of services is only for the purposes of "
            "clarifying the requirements specified in the present document and places no restrictions on any "
            "subdivision of an implementation of time-stamping services."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3 (Time-Stamping Authority (TSA))",
        "testo": (
            "Un Trust Service Provider (TSP) che fornisce servizi di marcatura temporale al pubblico e' "
            "chiamato Time-Stamping Authority (TSA). La TSA ha la responsabilita' complessiva dell'erogazione "
            "dei servizi di marcatura temporale individuati in clausola 4.2. La TSA ha la responsabilita' "
            "dell'operazione di una o piu' TSU, che creano e firmano per conto della TSA. La TSA responsabile "
            "dell'emissione di una marca temporale e' identificabile (si veda TIS-7.7.1-08). La TSA puo' "
            "avvalersi di altre parti per fornire parti dei servizi di marcatura temporale; tuttavia la TSA "
            "mantiene sempre la responsabilita' complessiva (come da clausola 6.5) e assicura che i requisiti "
            "di policy individuati nel documento siano soddisfatti. Esempio: una TSA subappalta tutte le "
            "componenti di servizio, incluse quelle che generano le marche temporali usando le chiavi delle "
            "TSU; la chiave o le chiavi private usate per generare le marche temporali sono comunque "
            "identificate come appartenenti alla TSA, che mantiene la responsabilita' complessiva del "
            "soddisfacimento dei requisiti definiti nel documento. Una TSA puo' operare piu' unita' di "
            "marcatura temporale identificabili. Una TSA e' un trust service provider come descritto in ETSI "
            "EN 319 401 [4] che emette marche temporali."
        ),
        "testo_integrale": (
            "4.3 Time-Stamping Authority (TSA): A Trust Service Provider (TSP) providing time-stamping "
            "services to the public, is called the Time-Stamping Authority (TSA). The TSA has overall "
            "responsibility for the provision of the time-stamping services identified in clause 4.2. The TSA "
            "has responsibility for the operation of one or more TSUs which creates and signs on behalf of "
            "the TSA. The TSA responsible for issuing a time-stamp is identifiable (see TIS-7.7.1-08). The "
            "TSA may make use of other parties to provide parts of the time-stamping services. However, the "
            "TSA always maintains overall responsibility (as per clause 6.5) and ensures that the policy "
            "requirements identified in the present document are met. EXAMPLE: A TSA sub-contracts all the "
            "component services, including the services which generate time-stamps using the TSU's keys. "
            "However, the private key or keys used to generate the time-stamps are identified as belonging to "
            "the TSA which maintains overall responsibility for meeting the requirements defined in the "
            "present document. A TSA may operate several identifiable time-stamping units. A TSA is a trust "
            "service provider as described in ETSI EN 319 401 [4] which issues time-stamps."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.4 (Subscriber)",
        "testo": (
            "Quando il sottoscrittore e' un'organizzazione, essa comprende piu' utenti finali o un singolo "
            "utente finale e alcuni degli obblighi che si applicano a tale organizzazione dovranno applicarsi "
            "anche agli utenti finali. In ogni caso l'organizzazione sara' ritenuta responsabile se gli "
            "obblighi degli utenti finali non sono correttamente adempiuti e pertanto ci si attende che tale "
            "organizzazione informi adeguatamente i propri utenti finali. Quando il sottoscrittore e' un "
            "utente finale, l'utente finale sara' ritenuto direttamente responsabile se i propri obblighi non "
            "sono correttamente adempiuti."
        ),
        "testo_integrale": (
            "4.4 Subscriber: When the subscriber is an organization, it comprises several end-users or an "
            "individual end-user and some of the obligations that apply to that organization will have to "
            "apply as well to the end-users. In any case the organization will be held responsible if the "
            "obligations from the end-users are not correctly fulfilled and therefore such an organization is "
            "expected to suitably inform its end users. When the subscriber is an end-user, the end-user will "
            "be held directly responsible if its obligations are not correctly fulfilled."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.5 (Time-stamp policy and TSA practice statement)",
        "testo": (
            "La clausola spiega i ruoli relativi di time-stamp policy e TSA practice statement e non pone "
            "alcuna restrizione sulla forma di una specifica di time-stamp policy o di practice statement. Una "
            "time-stamp policy e' una forma di Trust Service Policy come specificato in ETSI EN 319 401 [4], "
            "applicabile ai trust service provider che emettono marche temporali. La TSA Practice Statement "
            "e' una forma di Trust Service Practice Statement come specificato in ETSI EN 319 401 [4], "
            "applicabile ai trust service provider che emettono marche temporali. Il documento specifica una "
            "time-stamp policy per soddisfare i requisiti generali dei servizi di marcatura temporale "
            "affidabili. Le TSA specificano nelle proprie TSA practice statement come tali requisiti sono "
            "soddisfatti."
        ),
        "testo_integrale": (
            "4.5 Time-stamp policy and TSA practice statement: This clause explains the relative roles of "
            "time-stamp policy and TSA practice statement. It places no restriction on the form of a "
            "time-stamp policy or practice statement specification. A time-stamp policy is a form of Trust "
            "Service Policy as specified in ETSI EN 319 401 [4] applicable to trust service providers issuing "
            "time-stamps. TSA Practice Statement is a form of Trust Service Practice Statement as specified "
            "in ETSI EN 319 401 [4] applicable to trust service providers issuing time-stamps. The present "
            "document specifies a time-stamp policy to meet general requirements for trusted time-stamping "
            "services. TSAs specify in TSA practice statements how these requirements are met."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 1 (Scope)",
    "clausola 3.1 (Terms)",
    "clausola 3.3 (Abbreviations)",
    "clausola 3.4 (Notation)",
    "clausola 4.1 (General policy requirements concepts)",
    "clausola 4.2 (Time-stamping services)",
    "clausola 4.3 (Time-Stamping Authority (TSA))",
    "clausola 4.4 (Subscriber)",
    "clausola 4.5 (Time-stamp policy and TSA practice statement)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("principio", None, "clausola 4.3 (Time-Stamping Authority (TSA))"),
        "nodo_a": ("obbligo", None, "TIS-7.7.1-08"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
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
