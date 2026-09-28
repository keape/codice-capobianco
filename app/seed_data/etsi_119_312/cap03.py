"""ETSI TS 119 312 V2.1.1 (2026-06) - Electronic Signatures and Trust
Infrastructures (ESI); Cryptographic Suites. Capitolo 3: clausole 7 (Signature
suites), 8 (Hash functions and key sizes suitability end dates). Testo
ufficiale in app/.source_cache/etsi_119_312/cap03.txt; manifest di split in
app/.source_cache/etsi_119_312/manifest.json. Il file non importa nulla: gli id
e le relazioni sono risolti per riferimento dalla sessione principale
(app/seed.py - questo modulo NON tocca seed.py) tramite app/seed_data/lib.py.

Perimetro coperto (7 item di indice, 4 Obblighi + 3 Principi):
- clausola 7.1 (Introduction) -> Principio "altro"
- clausola 7.2 (General) -> Obbligo "tecnico/sicurezza"
- clausola 7.3 (Signature suites) -> Obbligo "tecnico/sicurezza"
- clausola 8.1 (Introduction) -> Principio "altro"
- clausola 8.2 (Basis for the recommendations) -> Obbligo "tecnico/sicurezza"
- clausola 8.4 (Recommended end dates for key sizes) -> Obbligo "tecnico/sicurezza"
- clausola 8.5 (Post-Quantum Cryptography Migration) -> Principio "altro"

Scelte di modellazione non ovvie:
- Le intestazioni di puro raggruppamento "7 (Signature suites)" e "8 (Hash
  functions and key sizes suitability end dates)" NON generano ne' nodo ne'
  item di indice: il testo ufficiale non associa loro alcun periodo proprio
  (passano direttamente alle rispettive sottoclawse x.1). Stesso trattamento
  riservato alle intestazioni di raggruppamento delle altre fonti ETSI gia'
  censite.
- La clausola 8.3 (Void), il cui intero contenuto e' la dicitura "Table 5:
  Void", NON genera ne' nodo ne' item di indice: e' un segnaposto di
  redazione per una tabella soppressa, senza alcun contenuto normativo
  autonomo ne' effetto giuridico proprio. Stesso trattamento gia' riservato ai
  "Void." puntuali e alle sottoclawse "Void" di ETSI TS 119 431-1/119 431-2.
  Le analoghe "Table 8/9/10: Void" cadono invece dentro la clausola 8.4 e
  sono riportate nel suo `testo_integrale`, perche' ivi sono parte del
  contenuto della clausola che le contiene.
- Clausola 7.1 (Introduction) -> Principio "altro": la clausola contiene una
  sola NOTE con i criteri primari di inclusione di un algoritmo nel documento
  (accordo ECCG [14]; uso comune; riferibilita' non ambigua, ad esempio
  tramite OID). Sono criteri di selezione, non prescrizioni a un soggetto:
  nessun "shall"/"should" e nessun destinatario obbligato.
- Clausola 7.2 (General) -> Obbligo "tecnico/sicurezza": oltre alle NOTE 1-2
  esplicative (componenti di una suite di firma; legame hash/schema di firma
  perche' altrimenti la funzione di hash piu' debole disponibile definisce il
  livello di sicurezza complessivo), la clausola chiude con una prescrizione
  in senso proprio ("algorithms and parameters for secure signatures shall be
  used only in predefined combinations referred to as the signature suites").
  Una sola clausola numerata = un solo nodo (ADR-0007), quindi il nodo e' un
  Obbligo e le NOTE restano in `testo_integrale` senza generare nodi propri.
- Clausola 8.1 (Introduction) -> Principio "altro": dichiara di cosa trattano
  le raccomandazioni della clausola 8 (uso delle funzioni di hash della
  clausola 5 e dimensioni di chiave degli algoritmi della clausola 6) e come
  la clausola e' strutturata (8.2 basi, 8.4 date di fine idoneita' delle
  chiavi, 8.5 tempistica di migrazione PQC). Descrizione di impianto, non
  perimetro di applicazione del documento: stesso tipo scelto per la clausola
  6.1 (Introduction) di ETSI TS 119 432 in questo censimento.
- Clausola 8.2 (Basis for the recommendations) -> Obbligo "tecnico/sicurezza":
  la clausola e' in prevalenza esplicativa (NOTE 1-3: metodo di stima delle
  robustezze, assenza di prove di sicurezza rigorose, esigenza di stabilita'
  dei requisiti), ma il suo periodo finale enuncia un parametro minimo
  prescrittivo ("ECCG recommended mechanisms should provide at least 125 bits
  of security against offline attacks. 100 bits of security may be used by
  ECCG legacy mechanisms"). Per la regola di classificazione ("should" con
  destinatario individuabile -> Obbligo) la clausola e' modellata come
  Obbligo, con destinatario il soggetto che seleziona i meccanismi
  crittografici (QTSP/gestore); modellarla come Principio avrebbe perso la
  soglia dei 125/100 bit.
- Clausole 7.3, 8.4 -> Obbligo "tecnico/sicurezza": elenchi di parametri
  ammessi e divieti d'uso ("shall be used", "should be used", "shall not be
  used"), destinatario il QTSP/gestore che implementa o emette certificati.
- Clausola 8.5 (Post-Quantum Cryptography Migration) -> Principio "altro":
  dichiara un fatto organizzativo (le classificazioni R/L sono indipendenti
  dalle fasi di dispiegamento; pianificazione della migrazione, fasi di
  transizione e scadenze di conformita' PQC saranno trattate nel documento di
  migrazione post-quantistica in sviluppo, richiamato dall'autorita'
  emittente). Nessun obbligo a carico di un soggetto censito in questa
  clausola, quindi nessun nodo Obbligo: un "should" o un "shall" qui non
  esiste.
- Soggetti: il soggetto obbligato tipico dello standard e' chi implementa le
  suite di firma e chi emette certificati, censito come "QTSP/gestore" (ruolo
  "obbligato"). Nessuna clausola della porzione nomina parti affidanti o
  sottoscrittori, quindi non e' stato aggiunto il ruolo "destinatario".
  `severita`/`sanzioni` restano assenti (standard tecnico, nessuna sanzione);
  `stato` sempre "vigente".
- RELAZIONI: lista vuota per contratto. I rinvii testuali presenti (alle
  clausole 5, 6, 6.2.2.3, 6.2.2.5, 6.2.2.6 e a FIPS 186-5/IETF RFC 8032) sono
  lasciati alla sessione principale, che li risolve con le relazioni
  tipizzate dopo l'inserimento di tutti i capitoli della fonte.

Convenzioni di trascrizione applicate a `testo_integrale` (nessuna parola
rimossa; per ogni clausola il testo del sorgente e' stato confrontato con il
paragrafo ricomposto):
- i wrap fisici di riga introdotti da pdftotext -layout sono ricomposti in
  paragrafi separati da riga vuota;
- i marcatori di pagina (riga "ETSI" + "19/20/21 ETSI TS 119 312 V2.1.1
  (2026-06)") sono paratesto della conversione e sono rimossi;
- il padding dei label ("NOTE:", "NOTE 1:" ecc.) e' normalizzato a un solo
  spazio dopo il label;
- il glifo privato U+F0A7 (pallino di elenco prodotto dalla conversione) e'
  normalizzato al pallino "•";
- le Tabelle 4, 6 e 7 sono state ricostruite riga per riga come tabelle
  Markdown (`|cella|cella|` con separatore `|---|---|`): la conversione
  layout-only aveva perso i confini di colonna, spezzando su piu' righe le
  intestazioni ("Entry name for the signature algorithm" era spezzata in
  "Entry name for the signature" + "algorithm"). Nessun valore perso: le 25
  righe della Tabella 4 sono riportate una per record, con la colonna R/L di
  ciascuna. In ogni riga il campo "Entry name of the signature suite" occupa
  esattamente la propria colonna nel sorgente, quindi nessuna cella risulta
  troncata; le stringhe "rsa-pss with mgf1SHA2-Identifier" e "rsa-pss with
  mgf1SHA3-Identifier" sono riportate come nel sorgente (senza spazio tra
  "mgf1" e "SHA2"/"SHA3").
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 7.2 (General)",
        "testo": (
            "Una suite di firma crittografica e' una combinazione di funzioni di codifica del messaggio "
            "(incluse le funzioni di hash) e di uno schema di firma definito che usa un algoritmo di firma "
            "standardizzato: le sue componenti sono quindi un metodo di codifica del messaggio che include la "
            "funzione di hash e un algoritmo di firma con i relativi parametri. Il ricorso a una funzione di "
            "hash permette di firmare e verificare messaggi di lunghezza piu' o meno arbitraria operando su un "
            "hash di dimensione fissa; e' importante legare la funzione di hash allo schema di firma, perche' "
            "altrimenti la funzione di hash piu' debole disponibile puo' definire il livello di sicurezza "
            "complessivo. Prescrizione: a causa delle possibili interazioni che possono influenzare la "
            "sicurezza delle firme, gli algoritmi e i parametri per firme sicure devono essere usati solo in "
            "combinazioni predefinite, denominate suite di firma."
        ),
        "testo_integrale": (
            """NOTE 1: A cryptographic signature suite is a combination of message encoding functions including a hash function and a defined signature scheme using a standardized signature algorithm. A signature suite consists therefore of the following components:

• a message encoding method including the hash function; and

• a signature algorithm and its associated parameters.

NOTE 2: To allow signing of more or less arbitrarily long messages, a signature suite uses a hash function, so that the signing/verification algorithms operate on a fixed-size hash of the message. An important issue is to tie the hash function to the signature scheme. Without this, the weakest available hash function can define the overall security level.

Due to possible interactions which can influence security of signatures, algorithms and parameters for secure signatures shall be used only in predefined combinations referred to as the signature suites."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7.3 (Signature suites)",
        "testo": (
            "La Tabella 4 riporta le combinazioni raccomandate di funzioni di hash e algoritmi di firma. Le "
            "suite su curve ellittiche sono implementabili in linea di principio con qualunque curva "
            "raccomandata, ma il documento raccomanda solo le combinazioni in cui la lunghezza dell'output "
            "della funzione di hash coincide con la dimensione della chiave della curva ellittica "
            "corrispondente. Prescrizione: le suite di firma elencate nella Tabella 4 devono essere usate. "
            "Tabella 4 (R = Recommended, L = legacy; hash e algoritmo di firma): sha224-with-rsa (SHA-224, "
            "RSA-PKCSv1_5, L[2028]); sha256-with-rsa (SHA-256, RSA-PKCSv1_5, L); sha384-with-rsa (SHA-384, "
            "RSA-PKCSv1_5, L); sha512-with-rsa (SHA-512, RSA-PKCSv1_5, L); rsa-pss with "
            "mgf1SHA2-Identifier (SHA-256, SHA-384 o SHA-512, RSA-PSS, R); rsa-pss with "
            "mgf1SHA3-Identifier (SHA3-256, SHA3-384 o SHA3-512, RSA-PSS, R); sha2-with-dsa (SHA-256, "
            "SHA-384, SHA-512, DSA, R); sha3-with-dsa (SHA3-256, SHA3-384, SHA3-512, DSA, R); "
            "sha2-with-ecdsa (SHA-256, SHA-384 o SHA-512, ECDSA, R); sha3-with-ecdsa (SHA3-256, SHA3-384 o "
            "SHA3-512, ECDSA, R); sha2-with-ecsdsa (SHA-256, SHA-384 o SHA-512, EC-SDSA-opt, L) e "
            "sha3-with-ecsdsa (SHA3-256, SHA3-384 o SHA3-512, EC-SDSA-opt, L); ed25519 (SHA-512 interna, "
            "Ed25519, R); ed448 (SHAKE256 interna, Ed448, R); ml-dsa-44, ml-dsa-65 e ml-dsa-87 (SHAKE256 "
            "interna, ML-DSA-44/ML-DSA-65/ML-DSA-87, R); slh-dsa-sha2-192s e slh-dsa-sha2-192f (SHA-256 "
            "interna), slh-dsa-shake-192s e slh-dsa-shake-192f (SHAKE256 interna), slh-dsa-sha2-256s e "
            "slh-dsa-sha2-256f (SHA-512 interna), slh-dsa-shake-256s e slh-dsa-shake-256f (SHAKE256 "
            "interna), tutti con algoritmo SLH-DSA e classificazione R. Note della clausola: con RSA l'uso di "
            "SHA-384 non da' vantaggi di sicurezza rispetto a SHA-512, essendo una derivazione troncata di "
            "SHA-512 (incluso solo per compatibilita'); con le curve ellittiche, se l'output della funzione "
            "di hash supera la dimensione n della chiave si usano i primi n bit del blocco di output "
            "(FIPS Publication 186-5, pagina 37); per ML-DSA e SLH-DSA pure la funzione di hash e' intrinseca "
            "all'algoritmo di firma ed e' determinata dal parameter set (nessun identificatore esterno di "
            "hash), mentre per le varianti pre-hash HashML-DSA e HashSLH-DSA la funzione di hash e' un "
            "parametro esplicito fornito dall'esterno dal chiamante e non fissato dal parameter set, con uso "
            "soggetto alle restrizioni delle clausole 6.2.2.5 e 6.2.2.6; le suite EC-SDSA-opt sono "
            "considerate legacy L per mancanza di supporto nelle librerie crittografiche diffuse (clausola "
            "6.2.2.3)."
        ),
        "testo_integrale": (
            """Table 4 reflects the combination of the recommended hash functions and signature algorithms.

Whereas the signature suites based on elliptic curves can be implemented in principle with any recommended curve, only those combinations are recommended by the present document where the output length of the hash function is the same as the key size of the corresponding elliptic curve.

NOTE 1: In case of RSA the use of SHA-384 gives no security advantage over SHA-512, because it is a truncated derivation of the SHA-512 algorithm. Nevertheless, it is included here for reasons of compatibility.

NOTE 2: If in case of elliptic curves the output length of the hash function is greater than the key size n, then the leftmost n bits of the hash function output block is used in the calculations using the hash function output during the generation or verification of a digital signature output (FIPS Publication 186-5 [2], page 37).

NOTE 3: For pure ML-DSA and pure SLH-DSA, the hash function is intrinsic to the signature algorithm and is determined by the parameter set; no external hash-algorithm identifier is required. For HashML-DSA and HashSLH-DSA, the hash function is an explicit parameter supplied externally by the caller and is not fixed by the parameter set; the use of these pre-hash variants is subject to the restrictions defined in clauses 6.2.2.5 and 6.2.2.6.

The signature suites listed in Table 4 shall be used.

Table 4: List of signature suites

| Entry name of the signature suite | Entry name for the hash function | Entry name for the signature algorithm | R/L |
|---|---|---|---|
| sha224-with-rsa | SHA-224 | RSA-PKCSv1_5 | L[2028] |
| sha256-with-rsa | SHA-256 | RSA-PKCSv1_5 | L |
| sha384-with-rsa | SHA-384 | RSA-PKCSv1_5 | L |
| sha512-with-rsa | SHA-512 | RSA-PKCSv1_5 | L |
| rsa-pss with mgf1SHA2-Identifier | SHA-256, SHA-384 or SHA-512 | RSA-PSS | R |
| rsa-pss with mgf1SHA3-Identifier | SHA3-256, SHA3-384 or SHA3-512 | RSA-PSS | R |
| sha2-with-dsa | SHA-256, SHA-384, SHA-512 | DSA | R |
| sha3-with-dsa | SHA3-256, SHA3-384, SHA3-512 | DSA | R |
| sha2-with-ecdsa | SHA-256, SHA-384 or SHA-512 | ECDSA | R |
| sha3-with-ecdsa | SHA3-256, SHA3-384 or SHA3-512 | ECDSA | R |
| sha2-with-ecsdsa | SHA-256, SHA-384 or SHA-512 | EC-SDSA-opt | L |
| sha3-with-ecsdsa | SHA3-256, SHA3-384 or SHA3-512 | EC-SDSA-opt | L |
| ed25519 | SHA-512 (internal) | Ed25519 | R |
| ed448 | SHAKE256 (internal) | Ed448 | R |
| ml-dsa-44 | SHAKE256 (internal) | ML-DSA-44 | R |
| ml-dsa-65 | SHAKE256 (internal) | ML-DSA-65 | R |
| ml-dsa-87 | SHAKE256 (internal) | ML-DSA-87 | R |
| slh-dsa-sha2-192s | SHA-256 (internal) | SLH-DSA-SHA2-192s | R |
| slh-dsa-sha2-192f | SHA-256 (internal) | SLH-DSA-SHA2-192f | R |
| slh-dsa-shake-192s | SHAKE256 (internal) | SLH-DSA-SHAKE-192s | R |
| slh-dsa-shake-192f | SHAKE256 (internal) | SLH-DSA-SHAKE-192f | R |
| slh-dsa-sha2-256s | SHA-512 (internal) | SLH-DSA-SHA2-256s | R |
| slh-dsa-sha2-256f | SHA-512 (internal) | SLH-DSA-SHA2-256f | R |
| slh-dsa-shake-256s | SHAKE256 (internal) | SLH-DSA-SHAKE-256s | R |
| slh-dsa-shake-256f | SHAKE256 (internal) | SLH-DSA-SHAKE-256f | R |

NOTE 4: EC-SDSA-opt suites are considered legacy L due to lack of support in widely used cryptographic libraries (see clause 6.2.2.3)."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 8.2 (Basis for the recommendations)",
        "testo": (
            "Basi delle raccomandazioni della clausola 8. Le raccomandazioni sulle robustezze di algoritmi e "
            "parametri sono caratterizzate prendendo un margine ragionevole sopra le lunghezze minime di "
            "chiave, sulla base sia dell'estrapolazione delle tendenze in corso sia di stime della potenza di "
            "calcolo necessaria per violare un dato algoritmo; tali estrapolazioni sono fatte negli ECCG "
            "Agreed Cryptographic Mechanisms [14] e valutazioni analoghe si trovano in letteratura (report "
            "ECRYPT 2018 su algoritmi, dimensioni di chiave e protocolli [i.1]). Non esistono prove di "
            "sicurezza rigorose per le componenti degli schemi di firma (funzione di hash, algoritmo di "
            "firma, RNG): tutte le affermazioni di sicurezza si basano sui migliori attacchi noti al momento "
            "della stesura, e non si puo' escludere teoricamente la rottura completa di una componente (es. "
            "un algoritmo di fattorizzazione universale veloce contro RSA o un computer quantistico che "
            "esegue l'algoritmo di Shor); il documento ECCG introduce misure specifiche per mitigare la "
            "minaccia \"harvest now, decrypt later\" posta dai futuri computer quantistici. La stabilita' dei "
            "requisiti e' altamente desiderabile per affidabilita' di pianificazione, ma la transizione alla "
            "crittografia post-quantistica (PQC) richiede aggiustamenti del ciclo di vita degli algoritmi "
            "classici: le tabelle seguenti contengono raccomandazioni sulla durata di vita delle chiavi, "
            "scelte secondo gli ECCG Agreed Cryptographic Mechanisms piu' il periodo di validita' predefinito "
            "dei certificati di entita' finale. Parametro minimo prescrittivo: i meccanismi raccomandati ECCG "
            "devono fornire almeno 125 bit di sicurezza contro attacchi offline; 100 bit di sicurezza "
            "possono essere usati dai meccanismi legacy ECCG, che pero' offrono un margine di sicurezza "
            "inferiore."
        ),
        "testo_integrale": (
            """NOTE 1: The recommendations for algorithm and parameter strengths are characterized by taking a reasonable margin above minimum key lengths based on both extrapolations of current trends as well as estimations based on the necessary computing power needed to break a given algorithm. Such extrapolations are made in the ECCG Agreed Cryptographic Mechanisms [14]. Similar assessments can be found also elsewhere in the literature, e.g. in the ECRYPT report on algorithms, key size and protocols report (2018) [i.1].

NOTE 2: There are no rigorous security proofs for the components of signature schemes (hash function, signature algorithm, RNG), basically all security statements rely on results about the most effective attacks known at the time of writing of the present document. The possibility of a complete break of such a component (like, e.g. a fast universal factorization algorithm against RSA or a quantum computer running Shor's algorithm) that renders it useless can theoretically not completely be excluded. The ECCG document introduces specific measures to mitigate the "harvest now, decrypt later" threat posed by future quantum computers.

NOTE 3: Stability of the requirements in the present document is highly desirable for reasons of planning reliability. However, the transition to Post-Quantum Cryptography (PQC) requires adjustments to the lifecycle of classical algorithms. The following tables contain recommendations for the lifetime of keys and were chosen according to the ECCG Agreed Cryptographic Mechanisms plus the default validity period of end-entity certificates.

ECCG recommended mechanisms should provide at least 125 bits of security against offline attacks. 100 bits of security may be used by ECCG legacy mechanisms, but they provide a lower security margin."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 8.4 (Recommended end dates for key sizes)",
        "testo": (
            "Date di fine idoneita' raccomandate per le dimensioni delle chiavi: i parametri definiti nella "
            "Tabella 6 e nella Tabella 7, derivati dagli ECCG Agreed Cryptographic Mechanisms [14], devono "
            "essere usati. Per RSA la dimensione della chiave (parametro di sicurezza) e' la lunghezza in bit "
            "del modulo n: chiavi con log2(n) >= 1 900 e < 3 000 bit hanno fine idoneita' 2026-12-31 e "
            "classificazione L[2026]; chiavi con log2(n) >= 3 000 bit sono R (nessuna data di fine "
            "idoneita'). Divieti e condizioni: le chiavi RSA di almeno 1 900 bit e meno di 3 000 bit non "
            "devono essere usate per emettere nuovi certificati dopo il 2026-12-31; i certificati basati su "
            "tali chiavi emessi entro il 2026-12-31 devono avere un periodo di validita' che termina non "
            "oltre il 2028-12-31; la stessa coppia di chiavi non deve essere usata per ottenere un nuovo "
            "certificato dopo la scadenza, indipendentemente dai parametri crittografici del nuovo "
            "certificato; dopo il 2026-12-31, per i certificati di nuova emissione devono essere usate solo "
            "chiavi RSA di almeno 3 000 bit o schemi di firma marcati Recommended (R) nel documento. Per DSA "
            "la dimensione della chiave (parametro di sicurezza) e' costituita dalle lunghezze in bit dei "
            "numeri primi p e q, ordine di un sottogruppo del gruppo moltiplicativo del campo primo GF(p): "
            "log2(p) >= 1 900 e < 3 000 bit con log2(q) >= 200 e < 250 bit ha fine idoneita' 2026-12-31 e "
            "classificazione L[2026]; log2(p) >= 3 000 bit con log2(q) >= 250 bit e' R. Note: la transizione "
            "alla crittografia post-quantistica e le raccomandazioni degli ECCG Agreed Mechanisms v2.0 [14] "
            "richiedono la dismissione accelerata delle chiavi RSA di dimensione inferiore a 3 000 bit entro "
            "la fine del 2026, prevalendo sulle indicazioni precedenti; EdDSA (Ed25519, Ed448) usa parametri "
            "e dimensioni di chiave fissi come definito in IETF RFC 8032 [23] ed e' considerato Recommended "
            "(R) senza date di fine idoneita' specifiche in questa clausola. Le Tabelle 8, 9 e 10 sono Void "
            "(segnaposto di redazione, nessun contenuto)."
        ),
        "testo_integrale": (
            """The parameters defined in Table 6 and Table 7, derived from ECCG Agreed Cryptographic Mechanisms [14], should be used.

The key size (security parameter) for RSA is the bit length of the modulus n.

Table 6: Recommended end dates for RSA key sizes

| Key size (log2(n) in bits) | End date | Recommendation |
|---|---|---|
| ≥ 1 900 and < 3 000 | 2026-12-31 | L[2026] |
| ≥ 3 000 | n/a | R |

RSA keys with a length of at least 1 900 bits and less than 3 000 bits shall not be used to issue new certificates after 2026-12-31. Certificates based on such keys that were issued on or before 2026-12-31 shall have a validity period ending no later than 2028-12-31. The same key pair shall not be used to obtain a new certificate after expiry, regardless of the cryptographic parameters of that new certificate. After 2026-12-31, only RSA keys with a length of at least 3 000 bits or signature schemes marked as Recommended (R) in the present document shall be used for newly issued certificates.

NOTE 1: The transition to Post-Quantum Cryptography and the recommendations in ECCG Agreed Mechanisms v2.0 [14] require expedited phasing out of RSA key sizes < 3 000 bits by the end of 2026, overriding previous guidance.

The key sizes (security parameters) for DSA are the bit lengths of the prime p and q the order of a subgroup of the multiplicative group of the prime field GF(p).

Table 7: Recommended end dates for DSA key sizes

| Key size (log2(p), log2(q) in bits) | End date | Recommendation |
|---|---|---|
| log2(p) ≥ 1 900 and < 3 000, log2(q) ≥ 200 and < 250 | 2026-12-31 | L[2026] |
| log2(p) ≥ 3 000, log2(q) ≥ 250 | n/a | R |

NOTE 2: EdDSA (Ed25519, Ed448) uses fixed parameters and key sizes as defined in IETF RFC 8032 [23]. They are considered Recommended (R) without specific end dates in this clause.

Table 8: Void

Table 9: Void

Table 10: Void"""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 7.1 (Introduction)",
        "testo": (
            "Criteri primari di inclusione di un algoritmo nel documento: l'algoritmo e' considerato "
            "concordato dall'ECCG [14]; l'algoritmo e' comunemente usato; l'algoritmo puo' essere "
            "riferito in modo semplice e non ambiguo (ad esempio per mezzo di un OID). Criteri di selezione "
            "editoriale del documento, senza soggetto obbligato e senza effetto giuridico proprio: nessun "
            "\"shall\"/\"should\"."
        ),
        "testo_integrale": (
            """NOTE: The primary criteria for inclusion of an algorithm in the present document are:

• the algorithm is considered as agreed on by ECCG [14];

• the algorithm is commonly used; and

• the algorithm can easily and unambiguously be referenced (for example by means of an OID)."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 8.1 (Introduction)",
        "testo": (
            "Introduzione alla clausola 8: fornisce raccomandazioni sull'uso delle funzioni di hash indicate "
            "nella clausola 5 e sulle dimensioni delle chiavi da usare con gli algoritmi menzionati nella "
            "clausola 6. Struttura dichiarata: la clausola 8.2 spiega le considerazioni su cui si basano le "
            "raccomandazioni; la clausola 8.4 raccomanda le date di fine idoneita' delle dimensioni delle "
            "chiavi; la clausola 8.5 definisce la tempistica di migrazione verso la crittografia "
            "post-quantistica."
        ),
        "testo_integrale": (
            """In this clause recommendations are provided regarding the use of hash functions given in clause 5 and the key sizes to be used with the algorithms mentioned in clause 6. This clause is structured as follows:

• Clause 8.2 explains the considerations on which the recommendations are based.

• In clause 8.4, key sizes end dates are recommended.

• In clause 8.5, the migration timeline for the transition to Post-Quantum Cryptography is defined."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 8.5 (Post-Quantum Cryptography Migration)",
        "testo": (
            "Migrazione post-quantistica: il documento fornisce classificazioni di idoneita' dei meccanismi "
            "(R/L) indipendenti dalle tempistiche delle fasi di dispiegamento; la pianificazione della "
            "migrazione, le fasi di transizione e le scadenze di conformita' per il passaggio alla "
            "crittografia post-quantistica sono previste essere trattate nel documento di migrazione "
            "post-quantistica attualmente in sviluppo, richiamato dall'autorita' emittente. Una NOTE rinvia, "
            "per orientamenti sulle tempistiche di migrazione PQC per i servizi fiduciari europei, ai "
            "documenti pubblicati dal NIS Cooperation Group [i.28] e da ENISA. Nessun obbligo a carico di un "
            "soggetto in questa clausola."
        ),
        "testo_integrale": (
            """The present document provides mechanism suitability classifications (R/L) that are independent of deployment-phase timelines. Migration scheduling, transition phases, and compliance deadlines for the transition to Post-Quantum Cryptography is planned to be addressed in the applicable post-quantum migration document currently under development referenced by the issuing authority.

NOTE: Guidance on PQC migration timelines for European trust services may be found in documents published by the NIS Cooperation Group [i.28] and ENISA."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 7.1 (Introduction)",
    "clausola 7.2 (General)",
    "clausola 7.3 (Signature suites)",
    "clausola 8.1 (Introduction)",
    "clausola 8.2 (Basis for the recommendations)",
    "clausola 8.4 (Recommended end dates for key sizes)",
    "clausola 8.5 (Post-Quantum Cryptography Migration)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

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
