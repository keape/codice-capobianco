"""ETSI TS 119 312 V2.1.1 (2026-06) — Electronic Signatures and Trust
Infrastructures (ESI); Cryptographic Suites. Capitolo 2: clausola 5 (Hash
functions) e clausola 6 (Signature schemes). Testo ufficiale in
app/.source_cache/etsi_119_312/cap02.txt (raw completo in
app/.source_cache/etsi_119_312/raw.txt).

Copertura (ADR-0007): un nodo per ogni clausola/sottoclavola numerata con
contenuto proprio — 5.1, 5.2.1, 5.2.2, 6.1, 6.2.1, 6.2.2.1, 6.2.2.2, 6.2.2.3,
6.2.2.4, 6.2.2.5, 6.2.2.6, 6.2.2.7, 6.3, 6.4.1, 6.4.2 (15 item di indice).
Le intestazioni di puro raggruppamento — 5 ("Hash functions"), 5.2
("Recommendations for SHA hash functions"), 6 ("Signature schemes"), 6.2
("Signature algorithms"), 6.2.2 ("Signature algorithms"), 6.4 ("Hybrid
Cryptographic Schemes") — non contengono alcun testo oltre il titolo e i
riferimenti alle sottoclausole, quindi non generano nodo né item di indice
(stesso criterio già applicato alle clausole di puro raggruppamento delle
altre fonti ETSI del censimento). La clausola 2 (References) non ricade in
questo capitolo e non è mai un nodo in questo censimento (bibliografia).

Classificazione (regola del task):
- 5.1, 5.2.1, 5.2.2, 6.2.1, 6.2.2.1-6.2.2.7, 6.3, 6.4.1, 6.4.2 -> Obbligo
  "tecnico/sicurezza" con soggetto obbligato "QTSP/gestore": sono elenchi di
  meccanismi crittografici ammessi/raccomandati e parametri minimi ("shall be
  used", "should be used", "may be used", "shall not be used"). Il destinatario
  individuabile è chi implementa il servizio fiduciario (il testo parla di
  "implementations"/"implementers"). La forza deontica del testo (shall vs
  should vs may) resta visibile nel campo `testo` (deve / si raccomanda /
  può), non è appiattita dalla classificazione.
- 6.1 (Introduction) -> Principio "definitorio": la clausola è composta dalla
  sola NOTE che definisce che cosa è uno "signature scheme" (tre algoritmi:
  generazione chiave, creazione firma, verifica firma) e la nozione di "coppia
  di algoritmi" usata in tutto il resto del documento; nessun destinatario
  obbligato. Non è "scopo/ambito di applicazione": non delimita l'ambito del
  documento ma fissa una definizione terminologica.

Scelte di modellazione non ovvie:
- Le tabelle sono contenuto della clausola che le contiene (Tabella 1 in 5.1,
  Tabella 2 in 6.2.1, Tabella 3 in 6.2.2.3, Tabella 3.1 in 6.2.2.5, Tabella
  3.2 in 6.2.2.6, Tabella 3.3 in 6.4.2): ogni record è riportato per intero in
  `testo_integrale`, una riga per record, con colonne separate da " | ",
  ricostruito dall'impaginazione a colonne del PDF (le celle non sono mai
  troncate; la ricostruzione riguarda solo la spaziatura/ordine delle colonne,
  che `pdftotext -layout` conserva già riga per riga).
- Clausola 6.2.2.1 (RSA): il testo convertito dal PDF riporta "216 < e < 2256"
  per il vincolo sull'esponente pubblico, esito del collasso degli apici
  (pedici/apici persi nella conversione: FIPS 186-4 esprime lo stesso vincolo
  come 2^16 < e < 2^256). In `testo_integrale` il vincolo è riportato come
  "2^16 < e < 2^256" — unica ricostruzione di questo capitolo, segnalata al
  main nel rapporto finale — perché "216 < e < 2256" è privo di senso tecnico e
  falserebbe la ricerca/lettura del nodo.
- La legge di 5.2.2 (SHA-256 insufficiente per l'archiviazione a lungo termine)
  e la condizione di inidoneità di SHA-224 (L[2028]) sono date di fine
  idoneità: restano nel testo delle rispettive clausole (il capitolo 3 copre le
  clausole 7-8, che le trattano sistematicamente).
- Le NOTE sono contenuto della clausola che le ospita (in questa porzione non
  esiste una clausola fatta di sole NOTE tranne 6.1): sono incluse integralmente
  in `testo_integrale` e sintetizzate in `testo` quando aggiungono un criterio
  tecnico (es. esclusione di HashML-DSA, gestione dello stato per LMS/XMSS,
  External Mu).

RELAZIONI: lista vuota. I collegamenti verso le altre fonti (eIDAS/eIDAS2,
altri standard ETSI, regolamenti di esecuzione) sono costruiti dalla sessione
principale in Fase 6; questo modulo non ne tenta nessuno, nemmeno verso le
citazioni interne del documento (clausola 6.4, clausola 8, Tabella 2) perché i
nodi di destinazione appartengono ad altri capitoli della stessa fonte.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 5.1 (General)",
        "testo": (
            "Le funzioni di hash utilizzabili sono quelle elencate nella Tabella 1 e devono essere "
            "implementate secondo il riferimento ivi indicato, seguendo le raccomandazioni delle ECCG "
            "Agreed Cryptographic Mechanisms; il documento fornisce raccomandazioni aggiuntive nelle "
            "clausole successive. Elenco della Tabella 1: SHA-224 (FIPS Publication 180-4, stato L con "
            "fine idoneità 2028), SHA-256, SHA-384, SHA-512 (FIPS Publication 180-4, R), SHA3-256, "
            "SHA3-384, SHA3-512 (FIPS Publication 202, R)."
        ),
        "testo_integrale": (
            "The list of hash functions in Table 1 shall be used. The functions shall be implemented as "
            "per the reference listed in Table 1 and shall follow the recommendations provided in the "
            "ECCG Agreed Cryptographic Mechanisms [14]. The present document provides additional "
            "recommendations in the following clauses.\n"
            "Table 1: Hash Functions\n"
            "Short hash function name | References | R/L\n"
            "SHA-224 | FIPS Publication 180-4 [1] | L[2028]\n"
            "SHA-256 | FIPS Publication 180-4 [1] | R\n"
            "SHA-384 | FIPS Publication 180-4 [1] | R\n"
            "SHA-512 | FIPS Publication 180-4 [1] | R\n"
            "SHA3-256 | FIPS Publication 202 [15] | R\n"
            "SHA3-384 | FIPS Publication 202 [15] | R\n"
            "SHA3-512 | FIPS Publication 202 [15] | R"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.1 (SHA-512/256)",
        "testo": (
            "Si raccomanda di usare SHA3-256 oppure SHA-512 al posto di SHA-512/256. Nota: la differenza "
            "rispetto a SHA-256 è il maggiore stato interno, che dà una migliore resistenza alle "
            "collisioni."
        ),
        "testo_integrale": (
            "SHA3-256 or SHA-512 should be used instead of SHA-512/256.\n"
            "NOTE: The difference to SHA-256 is the bigger inner state, which gives a better collision "
            "resistance."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.2 (Hash Functions for use in post-quantum contexts)",
        "testo": (
            "Raccomandazioni sulle funzioni di hash nei contesti post-quantistici: per le firme digitali "
            "che usano algoritmi classici (es. ECDSA, RSA) si raccomandano SHA-256, SHA-384 e SHA-512; per "
            "le firme digitali ibride e per l'archiviazione a lungo termine (oltre 20 anni) si "
            "raccomandano SHA-384, SHA-512, SHA3-384 e SHA3-512, in modo da garantire almeno 192 bit di "
            "sicurezza classica. Nota: SHA-256 può essere considerato insufficiente per l'archiviazione a "
            "lungo termine perché il suo margine di sicurezza classica di 128 bit è inferiore al livello "
            "minimo di 192 bit raccomandato dalle ECCG Agreed Cryptographic Mechanisms per i meccanismi "
            "post-quantistici; gli algoritmi quantistici di ricerca di collisioni non riducono la "
            "resistenza alle collisioni di SHA-256 e quindi non sono alla base di questa raccomandazione."
        ),
        "testo_integrale": (
            "For digital signatures using classical algorithms (e.g. ECDSA, RSA): SHA-256, SHA-384, and "
            "SHA-512 should be used.\n"
            "For hybrid digital signatures and long-term archiving (> 20 years): SHA-384, SHA-512, "
            "SHA3-384, and SHA3-512 should be used in order to provide at least 192 bits of classical "
            "security.\n"
            "NOTE: SHA-256 may be considered insufficient for long-term archiving use cases due to its "
            "classical security margin of 128 bits being below the minimum classical security level of "
            "192 bits recommended by the ECCG Agreed Cryptographic Mechanisms for post-quantum "
            "mechanisms. Quantum collision-finding algorithms do not reduce the collision resistance of "
            "SHA-256 and thus do not constitute the basis for this recommendation."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Secondo paragrafo: firme digitali ibride e archiviazione a lungo termine (oltre 20 anni)."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.2.1 (General)",
        "testo": (
            "Gli algoritmi di firma utilizzabili sono quelli elencati nella Tabella 2 e devono essere "
            "implementati secondo il riferimento ivi indicato, seguendo ove applicabile le raccomandazioni "
            "delle ECCG Agreed Cryptographic Mechanisms; il documento fornisce raccomandazioni e requisiti "
            "aggiuntivi nelle clausole successive. Elenco della Tabella 2 (nome breve, riferimento, "
            "stato): RSA-PKCS#1v1_5 (IETF RFC 8017, L); RSA-PSS (IETF RFC 8017, R); DSA (FIPS "
            "Publication 186-5, ISO/IEC 14888-3, R); ECDSA (FIPS Publication 186-5, R); EdDSA (IETF RFC "
            "8032, R - vedi nota 1); ML-DSA (NIST FIPS Publication 204, R); SLH-DSA (NIST FIPS "
            "Publication 205, R); EC-SDSA-opt (ISO/IEC 14888-3, L); LMS (IETF RFC 8554, R condizionato, "
            "vedi nota 2); XMSS (IETF RFC 8391, R condizionato, vedi nota 2). Nota 1: EdDSA non è uno "
            "schema di firma digitale concordato nell'ambito delle ECCG Agreed Cryptographic Mechanisms; "
            "lo stato \"R\" assegnato a EdDSA nella Tabella 2 riflette la raccomandazione del presente "
            "documento, indipendentemente dalle ECCG ACM. Nota 2: LMS e XMSS sono schemi di firma basati "
            "su hash e con stato; il loro uso richiede che l'implementatore stabilisca e mantenga "
            "procedure di gestione sicura dello stato per evitare il riuso della chiave privata - un "
            "fallimento nella gestione dello stato può portare alla compromissione completa della chiave "
            "di firma - e resta quindi limitato ad ambienti di deployment in cui la gestione dello stato "
            "può essere rigorosamente applicata."
        ),
        "testo_integrale": (
            "The list of signature algorithms given in Table 2 shall be used. The algorithms shall be "
            "implemented as per the reference listed in Table 2 and shall follow the recommendations "
            "provided in the ECCG Agreed Cryptographic Mechanisms [14], where applicable. The present "
            "document provides additional recommendations and requirements in the following clauses.\n"
            "Table 2: Digital Signature Algorithms\n"
            "Short signature algorithm name | References | R/L\n"
            "RSA-PKCS#1v1_5 | IETF RFC 8017 [3] | L\n"
            "RSA-PSS | IETF RFC 8017 [3] | R\n"
            "DSA | FIPS Publication 186-5, ISO/IEC 14888-3 [4] | R\n"
            "ECDSA | FIPS Publication 186-5 [2] | R\n"
            "EdDSA | IETF RFC 8032 [23] | R (see note 1)\n"
            "ML-DSA | NIST FIPS Publication 204 [26] | R\n"
            "SLH-DSA | NIST FIPS Publication 205 [27] | R\n"
            "EC-SDSA-opt | ISO/IEC 14888-3 [4] | L\n"
            "LMS | IETF RFC 8554 [28] | R (conditional, see note 2)\n"
            "XMSS | IETF RFC 8391 [29] | R (conditional, see note 2)\n"
            "NOTE 1: EdDSA is not an agreed digital signature scheme under the ECCG Agreed Cryptographic "
            "Mechanisms [14]. The \"R\" status assigned to EdDSA in Table 2 reflects the recommendation of "
            "the present document independently of the ECCG ACM.\n"
            "NOTE 2: LMS and XMSS are stateful hash-based signature schemes. Their use requires that the "
            "implementer establishes and maintains secure state management procedures to prevent private "
            "key reuse. Failure to manage state correctly may result in complete compromise of the "
            "signing key. The use of LMS and XMSS is therefore restricted to deployment environments "
            "where state management can be strictly enforced.\n"
            "NOTE: The notation given in parentheses in previous versions of the present document "
            "regarding SOG-IS document has been aligned with ECCG terminology."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.2.2.1 (RSA)",
        "testo": (
            "Deve essere usato l'algoritmo RSA con lo schema di padding RSASSA-PSS (meccanismo "
            "raccomandato ECCG); RSA con lo schema di padding legacy RSASSA-PKCS-v1_5 può essere usato "
            "(meccanismo legacy ECCG). La lunghezza della chiave deve essere scelta secondo la clausola 8. "
            "L'esponente pubblico e deve essere un intero positivo dispari tale che 2^16 < e < 2^256. Nei "
            "casi d'uso in cui è richiesta protezione dagli attacchi che sfruttano i computer quantistici "
            "(es. validità a lungo termine della firma oltre il 2030), RSA deve essere usato in uno schema "
            "ibrido come specificato nella clausola 6.4, oppure sostituito da un algoritmo quantum-safe. "
            "Nota: RSA è vulnerabile ad attacchi che sfruttano i computer quantistici (es. algoritmo di "
            "Shor)."
        ),
        "testo_integrale": (
            "The RSA algorithm with the padding scheme RSASSA-PSS [3], section 8.1 shall be used (ECCG "
            "recommended mechanism). RSA with the legacy padding scheme RSASSA-PKCS-v1_5 [3], section "
            "8.2, may be used (ECCG legacy mechanism). The key length shall be selected according to "
            "clause 8.\n"
            "The public exponent e shall be an odd positive integer such that 2^16 < e < 2^256.\n"
            "In use cases where protection against attacks leveraging quantum computers is required "
            "(e.g. where the long-term validity of the signature extends beyond 2030), RSA shall be used "
            "in a hybrid scheme as specified in clause 6.4, or shall be replaced by a quantum-safe "
            "algorithm.\n"
            "NOTE: RSA is vulnerable to attacks leveraging quantum computers (e.g. Shor's algorithm)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Terzo capoverso: casi d'uso in cui è richiesta protezione dagli attacchi con computer "
            "quantistici (es. validità a lungo termine della firma oltre il 2030)."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.2.2.2 (DSA)",
        "testo": (
            "L'algoritmo DSA può essere usato (meccanismo raccomandato ECCG) se la lunghezza della chiave "
            "è scelta secondo la clausola 8. Nei casi d'uso in cui è richiesta protezione dagli attacchi "
            "che sfruttano i computer quantistici, DSA deve essere usato in uno schema di firma ibrido "
            "come specificato nella clausola 6.4, oppure sostituito da un algoritmo quantum-safe. Nota: "
            "DSA è incluso per supportare librerie largamente usate (es. Bouncy Castle) ai fini "
            "dell'interoperabilità."
        ),
        "testo_integrale": (
            "The DSA algorithm may be used (ECCG recommended mechanism) if the key length is chosen "
            "according to clause 8.\n"
            "In use cases where protection against attacks leveraging quantum computers is required, DSA "
            "shall be used in a hybrid signature scheme as specified in clause 6.4, or shall be replaced "
            "by a quantum-safe algorithm.\n"
            "NOTE: DSA is included to support widely used libraries (e.g. Bouncy Castle) for "
            "interoperability."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Secondo capoverso: casi d'uso in cui è richiesta protezione dagli attacchi con computer "
            "quantistici."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.2.2.3 (EC based DSA algorithms)",
        "testo": (
            "Deve essere usato l'algoritmo ECDSA (meccanismo raccomandato ECCG); le lunghezze di chiave "
            "sono implicitamente date dalle curve nominate elencate. ECDSA deve essere usato solo se le "
            "curve ellittiche sono selezionate dalla Tabella 3: famiglia FR FRP256v1 (ANSSI [i.21]); "
            "famiglia Brainpool brainpoolP256r1, brainpoolP384r1, brainpoolP512r1 (IETF RFC 5639 [5]); "
            "famiglia NIST P-256, P-384, P-521 (NIST Special Publication 800-186 [22]) - tutte con stato R. "
            "Nei casi d'uso in cui è richiesta protezione dagli attacchi che sfruttano i computer "
            "quantistici, ECDSA deve essere usato in uno schema di firma ibrido come specificato nella "
            "clausola 6.4, oppure sostituito da un algoritmo quantum-safe. Nota: EC-SDSA-opt è considerato "
            "legacy L per mancanza di supporto nelle librerie crittografiche largamente usate. Quando "
            "usati, gli algoritmi devono essere quelli specificati dai riferimenti della Tabella 3, "
            "derivati da ECCG Agreed Cryptographic Mechanisms [14], pagina 26."
        ),
        "testo_integrale": (
            "The ECDSA algorithm shall be used (ECCG recommended mechanism). Key lengths are implicitly "
            "given by the named curves listed below.\n"
            "ECDSA shall be used (ECCG recommended mechanisms) only if the elliptic curves are selected "
            "from the following Table 3.\n"
            "In use cases where protection against attacks leveraging quantum computers is required, "
            "ECDSA shall be used in a hybrid signature scheme as specified in clause 6.4, or shall be "
            "replaced by a quantum-safe algorithm.\n"
            "NOTE: EC-SDSA-opt is considered legacy L due to lack of support in widely used cryptographic "
            "libraries.\n"
            "When used, the algorithms shall be as specified by the references provided in Table 3, "
            "derived from [14], page 26.\n"
            "Table 3: Elliptic Curve Parameters\n"
            "Curve family | Short curve name | References | R/L\n"
            "FR | FRP256v1 | ANSSI [i.21] | R\n"
            "Brainpool | brainpoolP256r1 | IETF RFC 5639 [5] | R\n"
            "Brainpool | brainpoolP384r1 | IETF RFC 5639 [5] | R\n"
            "Brainpool | brainpoolP512r1 | IETF RFC 5639 [5] | R\n"
            "NIST | P-256 | NIST Special Publication 800-186 [22] | R\n"
            "NIST | P-384 | NIST Special Publication 800-186 [22] | R\n"
            "NIST | P-521 | NIST Special Publication 800-186 [22] | R"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Secondo capoverso: uso di ECDSA ammesso solo con curve ellittiche selezionate dalla Tabella "
            "3. Terzo capoverso: casi d'uso in cui è richiesta protezione dagli attacchi con computer "
            "quantistici."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.2.2.4 (Edwards-Curve DSA (EdDSA) algorithms)",
        "testo": (
            "Deve essere usato l'Edwards-Curve Digital Signature Algorithm (EdDSA), incluse le varianti "
            "Ed25519 e Ed448 definite in IETF RFC 8032 [23], come meccanismo raccomandato. EdDSA fornisce "
            "firme deterministiche e resistenza agli attacchi side-channel; Ed25519 fornisce circa 128 bit "
            "di sicurezza, Ed448 circa 224 bit. Nei casi d'uso in cui è richiesta protezione dagli "
            "attacchi che sfruttano i computer quantistici, EdDSA deve essere usato in uno schema di firma "
            "ibrido come specificato nella clausola 6.4, oppure sostituito da un algoritmo quantum-safe. "
            "Nota: EdDSA non è vulnerabile agli attacchi side-channel che sfruttano valori casuali "
            "distorti durante la firma; può però essere vulnerabile ad attacchi di fault e la sua "
            "resistenza agli altri attacchi side-channel dipende dall'implementazione specifica. La nota "
            "ACM 49-DSARandom, che riguarda i requisiti di casualità per gli algoritmi di tipo DSA, non "
            "si applica a EdDSA."
        ),
        "testo_integrale": (
            "The Edwards-Curve Digital Signature Algorithm (EdDSA) including variants Ed25519 and Ed448 "
            "(as defined in IETF RFC 8032 [23]) shall be used as recommended mechanisms. EdDSA provides "
            "deterministic signatures and resistance to side-channel attacks. Ed25519 provides "
            "approximately 128 bits of security; Ed448 provides approximately 224 bits of security.\n"
            "In use cases where protection against attacks leveraging quantum computers is required, "
            "EdDSA shall be used in a hybrid signature scheme as specified in clause 6.4, or shall be "
            "replaced by a quantum-safe algorithm.\n"
            "NOTE: EdDSA provides deterministic signatures and is not vulnerable to side-channel attacks "
            "that exploit biased random values during signing. However, EdDSA may be vulnerable to fault "
            "attacks, and its resistance to other side-channel attacks depends on the specific "
            "implementation. The ACM Note 49-DSARandom, which concerns randomness requirements for "
            "DSA-type algorithms, does not apply to EdDSA."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Secondo capoverso: casi d'uso in cui è richiesta protezione dagli attacchi con computer "
            "quantistici."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.2.2.5 (ML-DSA)",
        "testo": (
            "Deve essere usato il Module-Lattice-Based Digital Signature Standard (ML-DSA) come "
            "specificato in NIST FIPS 204 [26], come meccanismo raccomandato; deve essere usato solo "
            "ML-DSA puro, mentre HashML-DSA non deve essere usato. I parameter set ML-DSA utilizzabili "
            "sono quelli della Tabella 3.1: ML-DSA-44 (sicurezza ≈ 128 bit, R con nota: soddisfa la "
            "soglia minima per i meccanismi raccomandati e il suo uso è accettabile dove ML-DSA-65 o "
            "ML-DSA-87 non sono praticabili, ma per i nuovi deployment si raccomanda di preferire "
            "ML-DSA-65 o ML-DSA-87); ML-DSA-65 (≥ 192 bit, R); ML-DSA-87 (≥ 256 bit, R). L'uso di ML-DSA "
            "in uno schema di firma ibrido come specificato nella clausola 6.4 è raccomandato; la "
            "pianificazione della migrazione sarà affrontata nel documento di migrazione post-quantistica "
            "in preparazione. Note 1-2: HashML-DSA è escluso perché rimuove la proprietà di "
            "non-resignability del ML-DSA puro, introduce rischio di confusione di algoritmo tramite un "
            "identificatore di funzione di hash fornito dall'esterno, richiede l'impegno della chiave "
            "pubblica a una specifica modalità di firma al momento dell'emissione del certificato ed è "
            "escluso da IETF RFC 9881 [i.29] (X.509), IETF RFC 9882 [i.30] (CMS) e NSA CNSA 2.0 [i.33]; "
            "per scenari con HSM o firma remota su messaggi grandi, il metodo di pre-calcolo External Mu "
            "- calcolo del rappresentante di messaggio μ di 64 byte in un modulo crittografico separato, "
            "come consentito dall'Algoritmo 7 di FIPS 204 - costituisce un'implementazione conforme di "
            "ML-DSA puro e non richiede HashML-DSA."
        ),
        "testo_integrale": (
            "The Module-Lattice-Based Digital Signature Standard (ML-DSA) as specified in NIST FIPS 204 "
            "[26] shall be used as a recommended mechanism. Only pure ML-DSA as specified in NIST FIPS "
            "204 [26] shall be used. HashML-DSA shall not be used.\n"
            "The ML-DSA parameter sets listed in Table 3.1 shall be used.\n"
            "Table 3.1: ML-DSA parameter sets\n"
            "ML-DSA parameter set | Security level | R/L\n"
            "ML-DSA-44 | ≈ 128 bits | R (see note)\n"
            "ML-DSA-65 | ≥ 192 bits | R\n"
            "ML-DSA-87 | ≥ 256 bits | R\n"
            "NOTE: ML-DSA-44 provides a security level of approximately 128 bits, which meets the minimum "
            "threshold for recommended mechanisms in the present document. Its use is acceptable where "
            "ML-DSA-65 or ML-DSA-87 is not feasible. Implementers should prefer ML-DSA-65 or ML-DSA-87 "
            "for new deployments.\n"
            "The use of ML-DSA in a hybrid signature scheme as specified in clause 6.4 is recommended; "
            "migration scheduling is planned to be addressed in the applicable post-quantum migration "
            "document currently under development.\n"
            "NOTE 1: HashML-DSA is excluded because: (a) it removes the non-resignability property of "
            "pure ML-DSA; (b) it introduces algorithm-confusion risk through an externally supplied "
            "hash-algorithm identifier; (c) it requires public-key commitment to a specific signing mode "
            "at certificate issuance time; and (d) it is excluded from IETF RFC 9881 [i.29] (X.509), IETF "
            "RFC 9882 [i.30] (CMS), and NSA CNSA 2.0 [i.33].\n"
            "NOTE 2: For HSM-based or remote signing scenarios involving large messages, the External Mu "
            "pre-computation method - comprising computation of the 64-byte message representative μ in a "
            "separate cryptographic module as permitted under FIPS 204 Algorithm 7 - constitutes a "
            "conformant implementation of pure ML-DSA and does not require HashML-DSA."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.2.2.6 (SLH-DSA)",
        "testo": (
            "Deve essere usato lo Stateless Hash-Based Digital Signature Standard (SLH-DSA) come "
            "specificato in NIST FIPS 205 [27], come meccanismo raccomandato. I parameter set SLH-DSA "
            "utilizzabili sono quelli della Tabella 3.2: slh-dsa-sha2-192s / slh-dsa-sha2-192f (variante "
            "hash SHA-2, 192 bit, R); slh-dsa-shake-192s / slh-dsa-shake-192f (SHAKE, 192 bit, R); "
            "slh-dsa-sha2-256s / slh-dsa-sha2-256f (SHA-2, 256 bit, R); slh-dsa-shake-256s / "
            "slh-dsa-shake-256f (SHAKE, 256 bit, R). Per i certificati PKIX e le strutture correlate, "
            "HashSLH-DSA come specificato in IETF RFC 9909 [i.31] è ammesso come meccanismo raccomandato "
            "alle seguenti condizioni: la funzione di pre-hash usata deve avere resistenza alle collisioni "
            "di almeno 192 bit; la coppia di chiavi deve essere impegnata a SLH-DSA puro o a HashSLH-DSA "
            "al momento della generazione della coppia di chiavi, poiché le due varianti usano object "
            "identifier distinti e distinte procedure Verify(). Per i formati di firma AdES basati su CMS "
            "(CAdES, PAdES, XAdES) deve essere usato solo SLH-DSA puro, coerentemente con IETF RFC 9814 "
            "[i.32]. L'uso di SLH-DSA in uno schema di firma ibrido come specificato nella clausola 6.4 è "
            "opzionale. Note 1-2: HashSLH-DSA impegna la chiave a una specifica modalità di firma al "
            "momento della generazione della coppia di chiavi; per i nuovi deployment è raccomandato "
            "SLH-DSA puro, per evitare questo vincolo. IETF RFC 9909 [i.31] ammette HashSLH-DSA per le "
            "strutture X.509 per i vincoli di dimensione di CRL e certificati sugli HSM; IETF RFC 9814 "
            "[i.32] lo esclude da CMS perché il meccanismo dei signed-attributes risolve il vincolo di "
            "dimensione del messaggio senza gli svantaggi associati."
        ),
        "testo_integrale": (
            "The Stateless Hash-Based Digital Signature Standard (SLH-DSA) as specified in NIST FIPS 205 "
            "[27] shall be used as a recommended mechanism.\n"
            "The SLH-DSA parameter sets listed in Table 3.2 shall be used.\n"
            "Table 3.2: SLH-DSA parameter sets\n"
            "SLH-DSA parameter set | Hash variant | Security level | R/L\n"
            "slh-dsa-sha2-192s / slh-dsa-sha2-192f | SHA-2 | 192 bits | R\n"
            "slh-dsa-shake-192s / slh-dsa-shake-192f | SHAKE | 192 bits | R\n"
            "slh-dsa-sha2-256s / slh-dsa-sha2-256f | SHA-2 | 256 bits | R\n"
            "slh-dsa-shake-256s / slh-dsa-shake-256f | SHAKE | 256 bits | R\n"
            "For PKIX certificates and certificate-related structures: HashSLH-DSA as specified in IETF "
            "RFC 9909 [i.31] is permitted as a recommended mechanism, subject to the following "
            "conditions:\n"
            "1) The pre-hash function used shall have a collision resistance of at least 192 bits.\n"
            "2) The key-pair shall be committed to either pure SLH-DSA or HashSLH-DSA at the time of "
            "key-pair generation, as the two variants use distinct object identifiers and distinct "
            "Verify() procedures.\n"
            "For CMS-based AdES signature formats (CAdES, PAdES, XAdES): only pure SLH-DSA shall be used, "
            "consistent with IETF RFC 9814 [i.32].\n"
            "The use of SLH-DSA in a hybrid signature scheme as specified in clause 6.4 is optional.\n"
            "NOTE 1: HashSLH-DSA commits the key to a specific signing mode at the time of key-pair "
            "generation, because HashSLH-DSA and pure SLH-DSA use distinct object identifiers and "
            "distinct Verify() procedures. Pure SLH-DSA is recommended for new deployments to avoid this "
            "constraint.\n"
            "NOTE 2: IETF RFC 9909 [i.31] permits HashSLH-DSA for X.509 structures due to CRL and "
            "certificate size constraints on HSMs. IETF RFC 9814 [i.32] excludes it from CMS because the "
            "signed-attributes mechanism resolves the message-size constraint without the associated "
            "drawbacks."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "HashSLH-DSA ammesso solo per certificati PKIX e strutture correlate; per i formati AdES "
            "basati su CMS (CAdES, PAdES, XAdES) solo SLH-DSA puro."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.2.2.7 (LMS and XMSS)",
        "testo": (
            "Devono essere usati come meccanismi raccomandati il Leighton-Micali Signature scheme (LMS) "
            "come specificato in IETF RFC 8554 [28] e l'eXtended Merkle Signature Scheme (XMSS) come "
            "specificato in IETF RFC 8391 [29], alle condizioni indicate nella nota. L'uso di LMS o XMSS "
            "in uno schema di firma ibrido come specificato nella clausola 6.4 è opzionale. LMS e XMSS "
            "sono schemi di firma basati su hash e con stato: la loro sicurezza dipende dal fatto che non "
            "vengano mai generate due firme con la stessa chiave monouso; gli implementatori devono "
            "stabilire, documentare e far rispettare procedure di gestione sicura dello stato per evitare "
            "il riuso della chiave privata, poiché un fallimento nella gestione dello stato può portare "
            "alla compromissione completa della chiave di firma. Il loro uso è quindi limitato ad ambienti "
            "di deployment in cui la gestione dello stato può essere rigorosamente applicata, come "
            "all'interno di un Hardware Security Module (HSM) certificato. Nota: LMS e XMSS sono "
            "specificamente adatti a casi d'uso come la firma di firmware e la marcatura temporale, dove "
            "l'entità firmataria è un componente di sistema controllato con capacità di gestione dello "
            "stato ben definite."
        ),
        "testo_integrale": (
            "The Leighton-Micali Signature scheme (LMS) as specified in IETF RFC 8554 [28] and the "
            "eXtended Merkle Signature Scheme (XMSS) as specified in IETF RFC 8391 [29] shall be used as "
            "recommended mechanisms, subject to the condition specified in note below.\n"
            "The use of LMS or XMSS in a hybrid signature scheme as specified in clause 6.4 is optional.\n"
            "LMS and XMSS are stateful hash-based signature schemes. Their security depends on the "
            "property that no two signatures are ever generated using the same one-time key. Implementers "
            "shall establish, document, and enforce secure state management procedures to prevent private "
            "key reuse. Failure to manage state correctly may result in complete compromise of the "
            "signing key. The use of LMS and XMSS is therefore restricted to deployment environments "
            "where state management can be strictly enforced, such as within a certified Hardware "
            "Security Module (HSM).\n"
            "NOTE: LMS and XMSS are specifically suitable for use cases such as firmware signing and "
            "time-stamping where the signing entity is a controlled system component with well-defined "
            "state management capabilities."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Uso limitato ad ambienti di deployment in cui la gestione sicura dello stato (per evitare il "
            "riuso della chiave privata) può essere rigorosamente applicata, come all'interno di un HSM "
            "certificato."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3 (Key generation)",
        "testo": (
            "La generazione delle chiavi deve seguire le raccomandazioni e i requisiti contenuti nei "
            "riferimenti normativi della Tabella 2 e nelle ECCG Agreed Cryptographic Mechanisms."
        ),
        "testo_integrale": (
            "The key generation shall follow the recommendations and requirements in their normative "
            "references of Table 2 and the ECCG Agreed Cryptographic Mechanisms."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.4.1 (Digital Signature Hybrid Modes)",
        "testo": (
            "Per le firme ibride le implementazioni devono combinare una firma classica e una firma "
            "post-quantistica; l'accettazione richiede che entrambe le firme siano valide."
        ),
        "testo_integrale": (
            "For hybrid signatures, implementations shall combine a classical signature and a "
            "post-quantum signature. Acceptance requires both signatures to be valid."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.4.2 (Recommended Hybrid Suites)",
        "testo": (
            "Le combinazioni raccomandate per gli schemi di firma ibridi sono elencate nella Tabella 3.3: "
            "RSA-PSS (≥ 3 000 bit) + ML-DSA-65 (uso generale, certificati); RSA-PSS (≥ 3 000 bit) + "
            "ML-DSA-87 (alta sicurezza, lungo termine); ECDSA (P-256/P-384) + ML-DSA-65 "
            "(CAdES/XAdES/PAdES); ECDSA (P-384/P-521) + ML-DSA-87 (alta sicurezza, lungo termine); EdDSA "
            "(Ed25519) + ML-DSA-65 (uso generale); EdDSA (Ed448) + ML-DSA-87 (alta sicurezza); ECDSA o "
            "EdDSA + SLH-DSA (Livello 3 o Livello 5) (marche temporali, firma di firmware). Il requisito "
            "di ibridazione del presente documento può essere soddisfatto da: a) ibridi a livello di "
            "algoritmo - due primitive di firma indipendenti calcolate e verificate separatamente sugli "
            "stessi dati di messaggio; oppure b) ibridi a livello di protocollo - meccanismi forniti dal "
            "protocollo o dal formato dati incapsulante, come il meccanismo dei signed-attributes in CMS "
            "(applicabile a CAdES e PAdES) o le costruzioni multi-firma in XAdES. Entrambi gli approcci "
            "sono considerati conformi ai fini del presente documento. Nota: i requisiti specifici di "
            "codifica e interoperabilità per gli schemi di firma ibridi sono fuori dall'ambito del "
            "presente documento e saranno affrontati negli standard di profilo applicabili e nel documento "
            "di migrazione post-quantistica in preparazione."
        ),
        "testo_integrale": (
            "The recommended combinations for hybrid signature schemes are listed in Table 3.3.\n"
            "Table 3.3: Algorithm-level hybrid combinations\n"
            "Classical component | PQC component | Use case\n"
            "RSA-PSS (≥ 3 000 bit) | ML-DSA-65 | General purpose, certificates\n"
            "RSA-PSS (≥ 3 000 bit) | ML-DSA-87 | High-security, long-term\n"
            "ECDSA (P-256/P-384) | ML-DSA-65 | CAdES/XAdES/PAdES\n"
            "ECDSA (P-384/P-521) | ML-DSA-87 | High-security, long-term\n"
            "EdDSA (Ed25519) | ML-DSA-65 | General purpose\n"
            "EdDSA (Ed448) | ML-DSA-87 | High-security\n"
            "ECDSA or EdDSA | SLH-DSA (Level 3 or Level 5) | Time-stamps, firmware signing\n"
            "The hybrid requirement of the present document may be satisfied by:\n"
            "a) algorithm-level hybrids: two independent signature primitives computed and verified "
            "separately over the same message data; or\n"
            "b) protocol-level hybrids: mechanisms provided by the encapsulating protocol or data format, "
            "such as the signed-attributes mechanism in CMS (applicable to CAdES and PAdES) or "
            "multi-signature constructions in XAdES.\n"
            "Both approaches are considered conformant for the purposes of the present document.\n"
            "NOTE: The specific encoding and interoperability requirements for hybrid signature schemes "
            "are outside the scope of the present document and is planned to be addressed in the "
            "applicable profile standards and the post-quantum migration document currently under "
            "development."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 6.1 (Introduction)",
        "testo": (
            "Definizione di schema di firma (signature scheme): è composto da tre algoritmi - un algoritmo "
            "di generazione della chiave, un algoritmo di creazione della firma e un algoritmo di verifica "
            "della firma. I due algoritmi di creazione e verifica sono qui identificati come \"coppia di "
            "algoritmi\" (pair of algorithms); ogni coppia ha un proprio nome. È la nozione su cui si "
            "fondano le raccomandazioni per singolo algoritmo delle clausole 6.2 e seguenti."
        ),
        "testo_integrale": (
            "NOTE: A signature scheme consists of three algorithms: a key generation algorithm, a "
            "signature creation algorithm and a signature verification algorithm. The two latter are "
            "identified hereafter as a pair of algorithms. Each pair has its own name."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 5.1 (General)",
    "clausola 5.2.1 (SHA-512/256)",
    "clausola 5.2.2 (Hash Functions for use in post-quantum contexts)",
    "clausola 6.1 (Introduction)",
    "clausola 6.2.1 (General)",
    "clausola 6.2.2.1 (RSA)",
    "clausola 6.2.2.2 (DSA)",
    "clausola 6.2.2.3 (EC based DSA algorithms)",
    "clausola 6.2.2.4 (Edwards-Curve DSA (EdDSA) algorithms)",
    "clausola 6.2.2.5 (ML-DSA)",
    "clausola 6.2.2.6 (SLH-DSA)",
    "clausola 6.2.2.7 (LMS and XMSS)",
    "clausola 6.3 (Key generation)",
    "clausola 6.4.1 (Digital Signature Hybrid Modes)",
    "clausola 6.4.2 (Recommended Hybrid Suites)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {
    "clausola 5.1 (General)": ["clausola 5.1 (General)"],
    "clausola 5.2.1 (SHA-512/256)": ["clausola 5.2.1 (SHA-512/256)"],
    "clausola 5.2.2 (Hash Functions for use in post-quantum contexts)": [
        "clausola 5.2.2 (Hash Functions for use in post-quantum contexts)"
    ],
    "clausola 6.1 (Introduction)": ["clausola 6.1 (Introduction)"],
    "clausola 6.2.1 (General)": ["clausola 6.2.1 (General)"],
    "clausola 6.2.2.1 (RSA)": ["clausola 6.2.2.1 (RSA)"],
    "clausola 6.2.2.2 (DSA)": ["clausola 6.2.2.2 (DSA)"],
    "clausola 6.2.2.3 (EC based DSA algorithms)": ["clausola 6.2.2.3 (EC based DSA algorithms)"],
    "clausola 6.2.2.4 (Edwards-Curve DSA (EdDSA) algorithms)": [
        "clausola 6.2.2.4 (Edwards-Curve DSA (EdDSA) algorithms)"
    ],
    "clausola 6.2.2.5 (ML-DSA)": ["clausola 6.2.2.5 (ML-DSA)"],
    "clausola 6.2.2.6 (SLH-DSA)": ["clausola 6.2.2.6 (SLH-DSA)"],
    "clausola 6.2.2.7 (LMS and XMSS)": ["clausola 6.2.2.7 (LMS and XMSS)"],
    "clausola 6.3 (Key generation)": ["clausola 6.3 (Key generation)"],
    "clausola 6.4.1 (Digital Signature Hybrid Modes)": ["clausola 6.4.1 (Digital Signature Hybrid Modes)"],
    "clausola 6.4.2 (Recommended Hybrid Suites)": ["clausola 6.4.2 (Recommended Hybrid Suites)"],
}

RELAZIONI: list[dict] = []
