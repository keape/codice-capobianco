"""ETSI TS 119 312 V2.1.1 (2026-06) - Electronic Signatures and Trust
Infrastructures (ESI); Cryptographic Suites. Capitolo 4: clausola 9 (Life time
and resistance of hash functions and keys), clausola 10 (Practical ways to
identify hash functions and signature algorithms), Annex A (normative:
Algorithms for various data structures), Annex B (informative: Signature
maintenance), Annex C (informative: Machine processable formats of the Algo
Paper) e Annex D (informative: Discontinued algorithms). Testo ufficiale in
app/.source_cache/etsi_119_312/cap04.txt; manifest di split in
app/.source_cache/etsi_119_312/manifest.json. Il file non importa nulla: gli id
e le relazioni sono risolti per riferimento dalla sessione principale
(app/seed.py - questo modulo NON tocca seed.py) tramite app/seed_data/lib.py.

Perimetro coperto (29 item di indice, 23 Obblighi + 6 Principi):
- clausola 9.1 (General notes) -> Principio "altro"
- clausola 9.2 (Time period resistance for hash functions) -> Obbligo
- clausola 9.3 (Time period resistance for signer's key) -> Obbligo
- clausola 9.4 (Time period resistance for trust anchors) -> Obbligo
- clausola 9.5 (Time period resistance for other keys) -> Obbligo
- clausola 10.1 (General) -> Obbligo
- clausola 10.2.1 (Introduction) -> Principio "altro"
- clausola 10.2.2 (Hash functions) -> Obbligo (Tabella 11, OID)
- clausola 10.2.3 (Elliptic curves) -> Obbligo (Tabella 12, OID)
- clausola 10.2.4 (Signature algorithms) -> Obbligo (Tabella 13, OID)
- clausola 10.2.5 (Signature suites) -> Obbligo (Tabella 14, OID)
- clausola 10.3.1 (Hash functions) -> Obbligo (Tabella 15, URI)
- clausola 10.3.2 (Signature algorithms) -> Principio "altro"
- clausola 10.3.3 (Signature suites) -> Obbligo (Tabella 16, URI)
- Annex A.1 (Introduction) -> Obbligo
- Annex A.2 (CAdES and PAdES) -> Obbligo (Tabella A.1)
- Annex A.3 (XAdES) -> Obbligo (Tabella A.2)
- Annex A.4 (Signer's certificates) -> Obbligo (Tabella A.3)
- Annex A.5 (CRLs) -> Obbligo (Tabella A.4)
- Annex A.6 (OCSP responses) -> Obbligo (Tabella A.5)
- Annex A.7 (CA certificates) -> Obbligo (Tabella A.6)
- Annex A.8 (Self-signed certificates for CA issuing CA certificates) -> Obbligo (Tabella A.7)
- Annex A.9 (TSTs based on IETF RFC 3161) -> Obbligo (Tabella A.8)
- Annex A.10 (TSU certificates) -> Obbligo (Tabella A.9)
- Annex A.11 (Self-signed certificates for CAs issuing TSU certificates) -> Obbligo
- Annex B (Signature maintenance) -> Obbligo
- Annex C.1 (JSON file location) -> Principio "altro"
- Annex C.2 (XML file location) -> Principio "altro"
- Annex D (Discontinued algorithms) -> Principio "altro" (Tabelle D.1-D.3)

Scelte di modellazione non ovvie:
- Il titolo del capitolo nel manifest ("clausole 9-10") descrive solo il
  marker di inizio: cap04 e' l'ultimo capitolo dello split, quindi il file
  assegnato prosegue fino alla fine del documento e contiene anche Annex A
  (normativo), Annex B, Annex C, Annex D, Annex E e la sezione History. Il
  perimetro effettivamente coperto e' quindi tutto il testo del file tranne
  le due esclusioni sotto: non esiste alcun altro capitolo della fonte che
  possa coprire gli annessi, e ADR-0007 impone che nessuna clausola numerata
  resti scoperta (Annex A e' per di piu' normativo e contiene i requisiti
  algoritmici per le strutture dati delle firme).
- ESCLUSO Annex E (informative: Bibliography): elenco di quattro documenti
  citati (IETF RFC 3526, NIST FIPS 203, ETSI TR 103 619, BSI TR-02102-1),
  nessun contenuto normativo ne' effetto giuridico proprio. Stesso
  trattamento della clausola 2 (References) di tutte le fonti ETSI gia'
  censite: nessun nodo, nessun item di indice. Per coerenza con ETSI EN 319
  411-1/411-2 (dove bibliografia e change history sono stati esclusi in
  blocco) anche la sezione finale "History" (cronologia delle versioni del
  documento) e' esclusa come paratesto.
- Intestazioni di puro raggruppamento, senza periodo proprio nel testo
  ufficiale (passano direttamente alle sottoclausole): clausola 9, clausola
  10 (titolo su due righe), clausola 10.2, clausola 10.3, intestazione
  "Annex A (normative): Algorithms for various data structures" e
  intestazione "Annex C (informative): Machine processable formats of the Algo
  Paper". Nessuna di esse genera nodo o item di indice.
- Clausola 10.4 (Void) -> NESSUN nodo, NESSUN item di indice: e' un
  segnaposto di redazione privo di contenuto autonomo. Stesso trattamento
  gia' riservato ai "Void." puntuali, alla clausola 3.2 di ETSI TS 119 431-1 e
  alla clausola 8.3 di cap03 di questa stessa fonte.
- Clausole con sole NOTE, senza alcun verbo prescrittivo -> 1 Principio
  "altro" ciascuna, non un nodo per singola NOTA: clausola 9.1 (General
  notes: NOTE 1-2 su contesto d'uso delle funzioni di hash/algoritmi di firma
  e sul periodo di confidenzialita' di una chiave), clausola 10.2.1
  (Introduction: unica NOTE sul repository degli OID), clausola 10.3.2
  (Signature algorithms: unica NOTE che motiva l'assenza di URI per gli
  algoritmi di firma). Un solo nodo per clausola numerata (ADR-0007), quindi
  le NOTE restano nel `testo_integrale`.
- Clausole con raccomandazione ("should"/"RECOMMENDED") rivolta a un
  destinatario individuabile -> Obbligo, per la regola di classificazione
  dello standard ("should" con destinatario -> Obbligo "tecnico/sicurezza"):
  A.1 (l'unico periodo prescrittivo e' "the use of hybrid schemes ...
  should be considered for new implementations as indicated in clause 6.4",
  in un capitolo per il resto introduttivo), Annex B (informative ma con
  "PQC Transition Recommendation: ... it is RECOMMENDED that the maintenance
  process ... utilizes ..." a carico di chi esegue la manutenzione della
  firma) e A.11 ("shall apply" al rinvio normativo + "strongly RECOMMENDED
  for new TSU Root CAs").
- Annex D (informative) -> 1 Principio "altro": enuncia i criteri con cui
  determinare una data di scadenza di un algoritmo (data dell'attacco
  pratico noto, data di pubblicazione dell'ultima specifica che lo
  raccomandava, anni di resistenza dichiarati, data della successiva
  specifica in cui ha smesso di essere raccomandato) e riporta le Tabelle
  D.1-D.3 con i vincoli crittografici utilizzabili "by default". Il testo e'
  dichiarativo ("can be used by default"), non impone comportamenti a un
  soggetto censito: nessun nodo Obbligo.
- Annex C.1/C.2 -> 1 Principio "altro" ciascuno: dichiarano soltanto la
  posizione del file JSON e del file XML in cui e' pubblicata la versione
  machine-readable del documento (URL versionato + NOTE con il link alla
  versione piu' recente). Nessun "shall"/"should", nessun soggetto
  obbligato.
- Soggetti. Il soggetto obbligato tipico dello standard e' chi implementa le
  suite crittografiche ed emette/protegge le strutture dati (certificati,
  CRL, risposte OCSP, token di marca temporale): censito come "QTSP/gestore"
  (ruolo "obbligato"). Le Tabelle A.1-A.9 hanno una colonna per gli emittenti
  e una per gli utilizzatori ("Issuers of ..." / "Users of ...", piu' le
  quattro colonne di Tabella A.8): poiche' i "shall support" vincolano anche
  il lato utilizzatore, dove la tabella nomina esplicitamente gli
  utilizzatori e' stata aggiunta come "obbligato" la categoria
  "Terzi affidanti/pubblico" (chi deve supportare gli algoritmi per
  elaborare/validare le strutture) e, per Tabella A.8, "Utente/titolare" per
  i TST requesters. Sono poi "obbligato" sia "QTSP/gestore" sia
  "Utente/titolare" nella clausola 9.3, dove il requisito ha per oggetto la
  chiave del firmatario. Nessuna riga usa il ruolo "destinatario": le
  clausole di questo capitolo non configurano un obbligo a carico di un
  soggetto con altri meri destinatari.
- `severita`/`sanzioni` restano assenti (standard tecnico, nessuna
  sanzione); `stato` sempre "vigente".
- RELAZIONI: lista vuota per contratto. I rinvii testuali presenti (alle
  clausole 5, 6.4, 8.5, 9.4 e A.8 di questa stessa fonte, alle clausole
  3.2.6/4.3 di IETF RFC 3739/6960 e agli standard ETSI esterni) sono
  lasciati alla sessione principale (ADR-0009).

Convenzioni di trascrizione applicate a `testo_integrale` (nessuna parola
rimossa; il testo di ciascuna clausola e' stato confrontato con il paragrafo
ricomposto e, per le tabelle ambigue, con il rendering della pagina PDF):
- i wrap fisici di riga introdotti da pdftotext -layout sono ricomposti in
  paragrafi separati da riga vuota;
- i marcatori di pagina (riga "ETSI" + "22-37 ETSI TS 119 312 V2.1.1
  (2026-06)") sono paratesto della conversione e sono rimossi;
- il padding dei label ("NOTE:", "NOTE 1:", "1)", "•") e' normalizzato a un
  solo spazio dopo il label;
- le Tabelle 11-16, A.1-A.9 e D.1-D.3 sono ricostruite riga per record come
  tabelle Markdown (`|cella|cella|` con separatore `|---|---|`): la
  conversione layout-only spezza su piu' righe sia le celle lunghe (OID/URI)
  sia le celle multi-riga dei requisiti. Gli a-capo interni a una cella sono
  resi con "; " (una cella Markdown non puo' contenere newline), senza
  aggiungere o togliere parole. Celle ricostruite/segnalate:
  - Tabella 14: le righe id-Ed25519 e id-Ed448 hanno la cella OID
    effettivamente VUOTA nel documento ufficiale (verificato sul rendering
    di pagina 25; gli OID degli stessi algoritmi sono in Tabella 13:
    1.3.101.112 e 1.3.101.113). La cella vuota e' riportata come tale, senza
    dedurne il valore dalle altre tabelle.
  - Tabella D.1: la cella "Not recommended since" di SHA-224 e' "ETSI TS 119
    312 V2.1.1 (2026-06) (the present document)": la conversione separa le due
    righe di testo della cella e le interleave con la riga SHA-224
    (verificato sul rendering di pagina 35). Senza il rendering, il
    frammento "ETSI TS 119 312 V2.1.1 (2026-06)" sarebbe stato attribuito per
    errore alla riga SHA-1.
  - Tabella A.6: la cella "Users of CA certificates" della riga "Issuer CA
    public keys" contiene nel documento ufficiale "hall support RSA, DSA,
    EdDSA, ECDSA" (refuso del documento, non "shall"): riportato verbatim
    (verificato sul rendering di pagina 30).
  - Tabella 13: la riga "id-slh-dsa-shake-192f:" porta il carattere ":" dopo
    il nome dell'oggetto nel documento ufficiale (refuso presente anche nel
    testo estraibile del PDF): riportato verbatim, per non introdurre una
    correzione non documentata.
- Ambiguita' risolte: la clausola 10.2.3 dichiara "The signature algorithms
  shall be identified using the OIDs in Table 12" pur trattando curve
  ellittiche (formulazione del documento ufficiale): riportata verbatim nel
  `testo_integrale` e chiarita nella sintesi italiana; la Tabella A.1 e'
  intitolata "...for PAdES and CAdES" mentre la sua intestazione di colonna
  recita "CAdES [i.6] and PAdES [i.8]" (ordine invertito nel solo titolo):
  entrambe le formulazioni riportate come nel sorgente.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 9.2 (Time period resistance for hash functions)",
        "testo": (
            "Durata di resistenza delle funzioni di hash. Le funzioni di hash dovrebbero restare idonee "
            "finche' deve ancora essere eseguita una verifica di firma; in caso contrario deve essere eseguito "
            "uno specifico processo di manutenzione della firma (vedi Annex B). Una funzione di hash usata per "
            "calcolare l'hash di un certificato, se questo non e' auto-firmato, dovrebbe restare idonea durante "
            "il periodo di validita' di quel certificato; una funzione di hash usata per calcolare l'hash di un "
            "certificato auto-firmato deve resistere durante il periodo di validita' di quel certificato "
            "auto-firmato. Una funzione di hash usata per calcolare l'impronta di un messaggio contenuta in un "
            "token di marca temporale non dovrebbe mai essere un meccanismo legacy al momento della creazione "
            "della marca temporale. Note: nei casi sopra la funzione di hash produce il message digest da "
            "firmare e la lunghezza del suo output dipende in generale dai parametri dello schema di firma, ma "
            "cio' non vale per tutti i ruoli critici di sicurezza che una funzione di hash puo' svolgere nei "
            "servizi fiduciari (l'impronta di un messaggio in un token di marca temporale non e' usata in "
            "combinazione con uno schema di firma e la lunghezza del suo output non dipende dalla dimensione "
            "dei parametri dello schema di firma); se la suite di firma usata dal firmatario e' un meccanismo "
            "raccomandato, il processo di manutenzione della firma puo' essere minimizzato."
        ),
        "testo_integrale": (
            """Hash functions should remain suitable as long as a signature verification still needs to be done.

If not, a specific signature maintenance process shall be performed (see annex B for more information).

A hash function used to compute the hash of a certificate, which is not a self-signed certificate, should remain suitable during the validity period of that certificate.

A hash function used to compute the hash of a self-signed certificate shall resist during the validity period of that self-signed certificate.

NOTE 1: In the cases above, a hash function is used to produce a message digest to be signed. In these cases, the output length of the hash function will in general depend on the parameters of the signature scheme. However, this reasoning does not apply to all security critical roles that hash functions may fulfil in the context of trust services. A hash function used to compute the imprint of a message placed in a time-stamp token, for instance, is not used in combination of a signature scheme, but generates only part of the message to be signed. The length of its output is not dependent upon the size of the parameters of the signature scheme.

A hash function used to compute the imprint of a message placed in a time-stamp token should never be a legacy mechanism at the time of time stamp creation.

NOTE 2: If the signature suite that has been used by the signer is a recommended mechanism, the signature maintenance process can be minimized."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 9.3 (Time period resistance for signer's key)",
        "testo": (
            "Durata di resistenza della chiave del firmatario. Le chiavi del firmatario devono restare idonee "
            "durante il periodo di manutenzione del certificato associato (comunemente detto periodo di "
            "validita', da notBefore a notAfter). Note: l'attenzione e' molto spesso posta sulla resistenza "
            "delle chiavi del firmatario; se queste diventano deboli per progressi della ricerca crittografica "
            "sara' necessaria la revoca, con un onere elevato di riemissione di nuove chiavi e certificati, ma "
            "dopo la revoca non si configura una violazione di sicurezza; se una chiave del firmatario non "
            "resta idonea durante il periodo di validita' del certificato associato, l'uso della marca "
            "temporale e' sufficiente a fornire una protezione adeguata, purche' una marca temporale con "
            "meccanismi raccomandati possa essere prodotta in un momento in cui la suite di firma conserva "
            "almeno lo stato legacy."
        ),
        "testo_integrale": (
            """Signer's keys shall remain suitable during the certificate maintenance period (commonly called validity period from notBefore to notAfter) of the associated certificate.

NOTE 1: The focus is very often placed on the resistance of signer's keys.

NOTE 2: If they become weak due to progress in cryptographic research, revocation will be necessary, and there would be a large burden to re-issue new keys and certificates. However, there is no security breach after revocation.

NOTE 3: If a signer's key does not remain suitable during the validity period of its associated certificate, then the use of time-stamping is sufficient to provide adequate protection, if a time stamp using recommended mechanisms can be produced at a time when the signature suite retains at least legacy status."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 9.4 (Time period resistance for trust anchors)",
        "testo": (
            "Durata di resistenza delle trust anchor. Una trust anchor deve restare sicura per l'intero "
            "periodo di tempo durante il quale una firma elettronica avanzata basata su ETSI TS 101 733, ETSI "
            "TS 101 903, ETSI TS 102 778, ETSI EN 319 122, ETSI EN 319 132 ed ETSI EN 319 142 deve essere "
            "verificata. Note: tale periodo puo' essere piu' lungo della vita del certificato associato; se la "
            "trust anchor diventa debole non puo' piu' essere usata per verifiche immediate, ma puo' essere "
            "usata per verifiche successive se un processo di manutenzione specifico e' eseguito prima che "
            "diventi insicura; questa e' una differenza importante rispetto alla stima della vita della chiave "
            "del firmatario."
        ),
        "testo_integrale": (
            """A trust anchor shall remain secure during the whole time period during which advanced electronic signature ETSI TS 101 733 [i.6], ETSI TS 101 903 [i.7], ETSI TS 102 778 [i.8], ETSI EN 319 122 [i.17], ETSI EN 319 132 [i.18] and ETSI EN 319 142 [i.19] needs to be verified.

NOTE 1: This can be longer than the life time of the associated certificate. If it becomes weak, it cannot be used anymore for immediate verifications. It can be used for subsequent verifications, if a specific maintenance process is performed before the trust anchor becomes insecure.

NOTE 2: This is an important difference to the estimation of the life time for signers' key."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 9.5 (Time period resistance for other keys)",
        "testo": (
            "Durata di resistenza delle altre chiavi. Tutte le altre chiavi (chiavi di TSU, chiavi di CA, "
            "chiavi dell'emittente di CRL, chiavi del risponditore OCSP) dovrebbero resistere durante il "
            "periodo di validita' del certificato associato e dei certificati che si fondano sulla sua "
            "validita'. I loro parametri di sicurezza devono quindi essere scelti almeno tanto forti quanto i "
            "parametri corrispondenti delle chiavi certificate. Se non restano idonee per il periodo previsto, "
            "deve essere applicato un processo di manutenzione prima che l'algoritmo sia rotto. Per queste "
            "chiavi vale la stessa regola prevista per le trust anchor nella clausola 9.4."
        ),
        "testo_integrale": (
            """All other keys (TSU keys, CA keys, CRL issuer keys, OCSP responder keys) should resist during the validity period of the associated certificate and the certificates that rely on its validity.

Their security parameters shall then be chosen at least as strong as the corresponding parameters of the certified keys.

If they do not remain suitable for the foreseen time period, a maintenance process shall be applied before the algorithm is broken.

For these keys the same rule as for trust anchors in clause 9.4 applies."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 10.1 (General)",
        "testo": (
            "Le funzioni di hash e gli algoritmi di firma devono essere referenziati usando un OID e/o un URN. "
            "Note: solo il proprietario dell'OID o dell'URN e' autorizzato a definirne il significato e quindi "
            "il significato dell'algoritmo, di norma rinviando a un altro documento; se tale OID/URN non e' "
            "disponibile, l'algoritmo e' inutilizzabile."
        ),
        "testo_integrale": (
            """Hash functions and signatures algorithms shall be referenced using an OID and/or a URN.

NOTE 1: Only the owner of the OID or the URN is allowed to define its meaning and thus the meaning of the algorithm, usually referencing another document.

NOTE 2: If such an OID/URN is not available the algorithm is unusable."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 10.2.2 (Hash functions)",
        "testo": (
            "Le funzioni di hash devono essere identificate usando gli OID della Tabella 11: id-sha224, "
            "id-sha256, id-sha384, id-sha512 (IETF RFC 4055 [8]), id-sha512-256 (IETF RFC 8017 [3]), "
            "id-sha3-256, id-sha3-384, id-sha3-512 (IETF RFC 9688 [21]). Tutti gli OID appartengono all'arco "
            "{joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistalgorithm(4) "
            "hashalgs(2) n} con n = 4 (id-sha224), 1 (id-sha256), 2 (id-sha384), 3 (id-sha512), 6 "
            "(id-sha512-256), 8 (id-sha3-256), 9 (id-sha3-384) e 10 (id-sha3-512)."
        ),
        "testo_integrale": (
            """The hash functions shall be identified using the OIDs in Table 11.

Table 11: OIDs of suitable hash functions

| Short object name | OID | References |
|---|---|---|
| id-sha224 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistalgorithm(4) hashalgs(2) 4 } | IETF RFC 4055 [8] |
| id-sha256 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistalgorithm(4) hashalgs(2) 1 } | IETF RFC 4055 [8] |
| id-sha384 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistalgorithm(4) hashalgs(2) 2 } | IETF RFC 4055 [8] |
| id-sha512 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistalgorithm(4) hashalgs(2) 3 } | IETF RFC 4055 [8] |
| id-sha512-256 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistalgorithm(4) hashalgs(2) 6 } | IETF RFC 8017 [3] |
| id-sha3-256 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistalgorithm(4) hashalgs(2) 8 } | IETF RFC 9688 [21] |
| id-sha3-384 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistalgorithm(4) hashalgs(2) 9 } | IETF RFC 9688 [21] |
| id-sha3-512 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistalgorithm(4) hashalgs(2) 10 } | IETF RFC 9688 [21] |"""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 10.2.3 (Elliptic curves)",
        "testo": (
            "Le curve ellittiche idonee devono essere identificate usando gli OID della Tabella 12 "
            "(il documento formula il requisito come \"The signature algorithms shall be identified using the "
            "OIDs in Table 12\" pur elencando curve): FRP256v1 (ANSSI [i.21]); brainpoolP256r1, brainpoolP384r1 "
            "e brainpoolP512r1 (IETF RFC 5639 [5]); P-256 (secp256r1), P-384 (secp384r1) e P-521 (secp521r1) "
            "(IETF RFC 5480 [16]). Gli OID brainpool sono nella forma {iso(1) "
            "identified-organization(3) teletrust(36) algorithm(3) signatureAlgorithm(3) ecSign(2) "
            "ecStdCurvesAndGeneration(8) ellipticCurve(1) versionOne(1) brainpoolPnnnr1(n)}."
        ),
        "testo_integrale": (
            """The signature algorithms shall be identified using the OIDs in Table 12.

Table 12: OIDs of suitable elliptic curves

| Short object name | OID | References |
|---|---|---|
| FRP256v1 | {iso(1) member-body(2) fr(250) type-org(1) 223 101 256 1} | ANSSI [i.21] |
| brainpoolP256r1 | {iso(1) identified-organization(3) teletrust(36) algorithm(3) signatureAlgorithm(3) ecSign(2) ecStdCurvesAndGeneration(8) ellipticCurve(1) versionOne(1) brainpoolP256r1(7)} | IETF RFC 5639 [5] |
| brainpoolP384r1 | {iso(1) identified-organization(3) teletrust(36) algorithm(3) signatureAlgorithm(3) ecSign(2) ecStdCurvesAndGeneration(8) ellipticCurve(1) versionOne(1) brainpoolP384r1(11)} | IETF RFC 5639 [5] |
| brainpoolP512r1 | {iso(1) identified-organization(3) teletrust(36) algorithm(3) signatureAlgorithm(3) ecSign(2) ecStdCurvesAndGeneration(8) ellipticCurve(1) versionOne(1) brainpoolP512r1(13)} | IETF RFC 5639 [5] |
| P-256 (secp256r1) | {iso(1) member-body(2) us(840) ansi-X9-62(10045) curves(3) prime(1) 7 } | IETF RFC 5480 [16] |
| P-384 (secp384r1) | {iso(1) identified-organization(3) certicom(132) curve(0) 34 } | IETF RFC 5480 [16] |
| P-521 (secp521r1) | {iso(1) identified-organization(3) certicom(132) curve(0) 35 } | IETF RFC 5480 [16] |"""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 10.2.4 (Signature algorithms)",
        "testo": (
            "Gli algoritmi di firma devono essere identificati usando gli OID della Tabella 13: rsaEncryption "
            "1.2.840.113549.1.1.1 e id-dsa 1.2.840.10040.4.1 (IETF RFC 3279 [7]); id-ecPublicKey "
            "{iso(1) member-body(2) us(840) 10045 2 1} (IETF RFC 5753 [9]); id-Ed25519 "
            "{iso(1) identified-organization(3) thawte(101) 112} e id-Ed448 "
            "{iso(1) identified-organization(3) thawte(101) 113} (IETF RFC 8410 [24]); id-ml-dsa-44/65/87 "
            "(NIST FIPS Publication 204 [26]) e id-slh-dsa-sha2-192s/192f/"
            "256s/256f, id-slh-dsa-shake-192s/192f/256s/256f (NIST FIPS 205 [27]), tutti nell'arco "
            "{joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) "
            "sigAlgs(3) n}."
        ),
        "testo_integrale": (
            """The signature algorithms shall be identified using the OIDs in Table 13.

Table 13: OIDs of suitable signature algorithms

| Short object name | OID | References |
|---|---|---|
| rsaEncryption | { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-1(1) 1 } | IETF RFC 3279 [7] |
| id-dsa | { iso(1) member-body(2) us(840) x9-57(10040) x9cm(4) 1 } | IETF RFC 3279 [7] |
| id-ecPublicKey | { iso(1) member-body(2) us(840) 10045 2 1 } | IETF RFC 5753 [9] |
| id-Ed25519 | { iso(1) identified-organization(3) thawte(101) 112 } | IETF RFC 8410 [24] |
| id-Ed448 | { iso(1) identified-organization(3) thawte(101) 113 } | IETF RFC 8410 [24] |
| id-ml-dsa-44 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 17 } | NIST FIPS Publication 204 [26] |
| id-ml-dsa-65 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 18 } | NIST FIPS Publication 204 [26] |
| id-ml-dsa-87 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 19 } | NIST FIPS Publication 204 [26] |
| id-slh-dsa-sha2-192s | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 22 } | NIST FIPS 205 [27] |
| id-slh-dsa-sha2-192f | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 23 } | NIST FIPS 205 [27] |
| id-slh-dsa-sha2-256s | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 24 } | NIST FIPS 205 [27] |
| id-slh-dsa-sha2-256f | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 25 } | NIST FIPS 205 [27] |
| id-slh-dsa-shake-192s | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 28 } | NIST FIPS 205 [27] |
| id-slh-dsa-shake-192f: | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 29 } | NIST FIPS 205 [27] |
| id-slh-dsa-shake-256s | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 30 } | NIST FIPS 205 [27] |
| id-slh-dsa-shake-256f | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 31 } | NIST FIPS 205 [27] |"""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 10.2.5 (Signature suites)",
        "testo": (
            "Le suite di firma devono essere identificate usando gli OID della Tabella 14: "
            "sha256WithRSAEncryption (pkcs-1(1) 11), sha512WithRSAEncryption (pkcs-1(1) 13), id-RSASSA-PSS "
            "(pkcs-1(1) 10) con IETF RFC 4055 [8]; ecdsa-with-SHA224/256/384/512 (ansi-X9-62(10045) "
            "signatures(4) ecdsa-with-Specified(3) 1/2/3/4) con IETF RFC 5758 [19]; id-ecdsa-with-sha3-256/"
            "384/512 (nistAlgorithm(4) sigAlgs(3) 10/11/12) con NIST CSOR [17]; id-Ed25519, id-Ed448 "
            "(cella OID vuota nel documento) con IETF RFC 8410 [24]; id-hash-slh-dsa-sha2-192s/192f/256s/"
            "256f-with-sha512 (sigAlgs 37/38/39/40) e id-hash-slh-dsa-shake-192s/192f/256s/256f-with-shake256 "
            "(sigAlgs 43/44/45/46) con NIST FIPS 205 [27]. Nota: IETF RFC 4055 [8] ha definito per "
            "RSASSA-PSS un OID indipendente dalla funzione di hash, che e' specificata nei parametri "
            "dell'algoritmo (quindi applicabile sia a SHA2 sia a SHA3)."
        ),
        "testo_integrale": (
            """The signature suites shall be identified using the OIDs in Table 14.

Table 14: OIDs of suitable signatures suites

| Short object name | OID | References |
|---|---|---|
| sha256WithRSAEncryption | { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-1(1) 11 } | IETF RFC 4055 [8] |
| sha512WithRSAEncryption | { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-1(1) 13 } | IETF RFC 4055 [8] |
| id-RSASSA-PSS | { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-1(1) 10 } | IETF RFC 4055 [8] |
| ecdsa-with-SHA224 | { iso(1) member-body(2) us(840) ansi-X9-62(10045) signatures(4) ecdsa-with-Specified(3) 1 } | IETF RFC 5758 [19] |
| ecdsa-with-SHA256 | { iso(1) member-body(2) us(840) ansi-X9-62(10045) signatures(4) ecdsa-with-Specified(3) 2 } | IETF RFC 5758 [19] |
| ecdsa-with-SHA384 | { iso(1) member-body(2) us(840) ansi-X9-62(10045) signatures(4) ecdsa-with-Specified(3) 3 } | IETF RFC 5758 [19] |
| ecdsa-with-SHA512 | { iso(1) member-body(2) us(840) ansi-X9-62(10045) signatures(4) ecdsa-with-Specified(3) 4 } | IETF RFC 5758 [19] |
| id-ecdsa-with-sha3-256 | {joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 10} | NIST CSOR [17] |
| id-ecdsa-with-sha3-384 | {joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 11} | NIST CSOR [17] |
| id-ecdsa-with-sha3-512 | {joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 12} | NIST CSOR [17] |
| id-Ed25519 |  | IETF RFC 8410 [24] |
| id-Ed448 |  | IETF RFC 8410 [24] |
| id-hash-slh-dsa-sha2-192s-with-sha512 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 37 } | NIST FIPS 205 [27] |
| id-hash-slh-dsa-sha2-192f-with-sha512 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 38 } | NIST FIPS 205 [27] |
| id-hash-slh-dsa-sha2-256s-with-sha512 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 39 } | NIST FIPS 205 [27] |
| id-hash-slh-dsa-sha2-256f-with-sha512 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 40 } | NIST FIPS 205 [27] |
| id-hash-slh-dsa-shake-192s-with-shake256 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 43 } | NIST FIPS 205 [27] |
| id-hash-slh-dsa-shake-192f-with-shake256 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 44 } | NIST FIPS 205 [27] |
| id-hash-slh-dsa-shake-256s-with-shake256 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 45 } | NIST FIPS 205 [27] |
| id-hash-slh-dsa-shake-256f-with-shake256 | { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) sigAlgs(3) 46 } | NIST FIPS 205 [27] |

NOTE: IETF RFC 4055 [8] defined a hash-independent OID for the RSASSA-PSS signature algorithm. The OID for the specific hash function used in these algorithms is included in the algorithm parameters. So it is applicable for SHA2 and SHA3."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 10.3.1 (Hash functions)",
        "testo": (
            "Le funzioni di hash devono essere identificate usando gli URI della Tabella 15: sha224 "
            "(http://www.w3.org/2001/04/xmldsig-more#sha224), sha384 "
            "(http://www.w3.org/2001/04/xmldsig-more#sha384) con IETF RFC 6931 [10]; sha256 "
            "(http://www.w3.org/2001/04/xmlenc#sha256) e sha512 (http://www.w3.org/2001/04/xmlenc#sha512) con "
            "W3C Recommendation XML Encryption Syntax and Processing, April 2013 [11]; sha3-256, sha3-384 e "
            "sha3-512 (http://www.w3.org/2007/05/xmldsig-more#sha3-256, #sha3-384, #sha3-512) con IETF RFC "
            "9231 [20]."
        ),
        "testo_integrale": (
            """The hash functions shall be identified using the URIs in Table 15.

Table 15: URIs of suitable hash functions

| Short object name | URI | References |
|---|---|---|
| sha224 | http://www.w3.org/2001/04/xmldsig-more#sha224 | IETF RFC 6931 [10] |
| sha256 | http://www.w3.org/2001/04/xmlenc#sha256 | W3C® Recommendation XML Encryption Syntax and Processing, April 2013 [11] |
| sha384 | http://www.w3.org/2001/04/xmldsig-more#sha384 | IETF RFC 6931 [10] |
| sha512 | http://www.w3.org/2001/04/xmlenc#sha512 | W3C® Recommendation XML Encryption Syntax and Processing, April 2013 [11] |
| sha3-256 | http://www.w3.org/2007/05/xmldsig-more#sha3-256 | IETF RFC 9231 [20] |
| sha3-384 | http://www.w3.org/2007/05/xmldsig-more#sha3-384 | IETF RFC 9231 [20] |
| sha3-512 | http://www.w3.org/2007/05/xmldsig-more#sha3-512 | IETF RFC 9231 [20] |"""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 10.3.3 (Signature suites)",
        "testo": (
            "Le suite di firma devono essere identificate usando gli URI della Tabella 16: rsa-sha224, "
            "ecdsa-sha3-256/384/512, ed25519, ed448 con IETF RFC 9231 [20]; rsa-sha256/384/512, "
            "rsapss-with-parameters (http://www.w3.org/2007/05/xmldsig-more#rsa-pss), "
            "rsapss-with-defaults-sha224/256/384/512 (http://www.w3.org/2007/05/xmldsig-more#shaNNN-rsa-MGF1), "
            "rsapss-with-sha3-224/256/384/512 (http://www.w3.org/2007/05/xmldsig-more#sha3-NNN-rsa-MGF1), "
            "ecdsa-sha224/256/384/512 con IETF RFC 6931 [10]. Note 1: l'URI rsapss-with-parameters consente "
            "anche la parametrizzazione con SHA-3. Note 2: non sono definiti URI per RSA con padding "
            "PKCS#1v1.5 e SHA-3."
        ),
        "testo_integrale": (
            """The signature suites shall be identified using the URIs in Table 16.

Table 16: URIs of suitable signature suites

| Short object name | URI | References |
|---|---|---|
| rsa-sha224 | http://www.w3.org/2001/04/xmldsig-more#rsa-sha224 | IETF RFC 9231 [20] |
| rsa-sha256 | http://www.w3.org/2001/04/xmldsig-more#rsa-sha256 | IETF RFC 6931 [10] |
| rsa-sha384 | http://www.w3.org/2001/04/xmldsig-more#rsa-sha384 | IETF RFC 6931 [10] |
| rsa-sha512 | http://www.w3.org/2001/04/xmldsig-more#rsa-sha512 | IETF RFC 6931 [10] |
| rsapss-with-parameters | http://www.w3.org/2007/05/xmldsig-more#rsa-pss | IETF RFC 6931 [10] |
| rsapss-with-defaults-sha224 | http://www.w3.org/2007/05/xmldsig-more#sha224-rsa-MGF1 | IETF RFC 6931 [10] |
| rsapss-with-defaults-sha256 | http://www.w3.org/2007/05/xmldsig-more#sha256-rsa-MGF1 | IETF RFC 6931 [10] |
| rsapss-with-defaults-sha384 | http://www.w3.org/2007/05/xmldsig-more#sha384-rsa-MGF1 | IETF RFC 6931 [10] |
| rsapss-with-defaults-sha512 | http://www.w3.org/2007/05/xmldsig-more#sha512-rsa-MGF1 | IETF RFC 6931 [10] |
| rsapss-with-sha3-224 | http://www.w3.org/2007/05/xmldsig-more#sha3-224-rsa-MGF1 | IETF RFC 6931 [10] |
| rsapss-with-sha3-256 | http://www.w3.org/2007/05/xmldsig-more#sha3-256-rsa-MGF1 | IETF RFC 6931 [10] |
| rsapss-with-sha3-384 | http://www.w3.org/2007/05/xmldsig-more#sha3-384-rsa-MGF1 | IETF RFC 6931 [10] |
| rsapss-with-sha3-512 | http://www.w3.org/2007/05/xmldsig-more#sha3-512-rsa-MGF1 | IETF RFC 6931 [10] |
| ecdsa-sha224 | http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha224 | IETF RFC 6931 [10] |
| ecdsa-sha256 | http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256 | IETF RFC 6931 [10] |
| ecdsa-sha384 | http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha384 | IETF RFC 6931 [10] |
| ecdsa-sha512 | http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha512 | IETF RFC 6931 [10] |
| ecdsa-sha3-256 | http://www.w3.org/2021/04/xmldsig-more#ecdsa-sha3-256 | IETF RFC 9231 [20] |
| ecdsa-sha3-384 | http://www.w3.org/2021/04/xmldsig-more#ecdsa-sha3-384 | IETF RFC 9231 [20] |
| ecdsa-sha3-512 | http://www.w3.org/2021/04/xmldsig-more#ecdsa-sha3-512 | IETF RFC 9231 [20] |
| ed25519 | http://www.w3.org/2021/04/xmldsig-more#ed25519 | IETF RFC 9231 [20] |
| ed448 | http://www.w3.org/2021/04/xmldsig-more#ed448 | IETF RFC 9231 [20] |

NOTE 1: The URI rsapss-with-parameters allows also the parametrization with SHA-3.

NOTE 2: There are no URI defined for RSA with PKCS#1v1.5 padding and SHA-3."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.1 (Introduction)",
        "testo": (
            "Introduzione all'Annex A (normativo). ETSI TS 101 733, ETSI TS 101 903, ETSI TS 102 778, ETSI EN "
            "319 122, ETSI EN 319 132 ed ETSI EN 319 142 definiscono i formati delle firme elettroniche "
            "avanzate (digitali) e rinviano ad altri documenti che definiscono le strutture dati "
            "standardizzate: certificati del firmatario, liste di revoca dei certificati (CRL), risposte OCSP, "
            "certificati di autorita' di certificazione, certificati auto-firmati per certificati di CA, "
            "token di marca temporale (TST), certificati di Time-Stamping Unit (TSU), certificati auto-firmati "
            "per certificati TSU e certificati di attributi (Ac). Per ogni struttura dati e' specificato "
            "l'insieme di algoritmi da usare. Poiche' molti di questi documenti sono stati pubblicati anni fa "
            "e non sono aggiornati agli ultimi avanzamenti crittografici, gli algoritmi che presentano "
            "debolezze o che sono ormai rotti non sono elencati nelle tabelle dell'annesso; gli algoritmi "
            "obsoleti utilizzabili nella verifica di firme archiviate (es. SHA-1) non sono menzionati, e i "
            "requisiti dell'annesso si applicano alla data di emissione del presente documento; non sono "
            "indicati nemmeno gli algoritmi che emittenti o utilizzatori possono supportare "
            "addizionalmente. Raccomandazione: per la transizione alla crittografia post-quantistica, l'uso "
            "di schemi ibridi (combinazione di algoritmi classici e post-quantistici) dovrebbe essere "
            "considerato per le nuove implementazioni, come indicato nella clausola 6.4; le tabelle "
            "dell'annesso elencano sia algoritmi classici sia post-quantistici per facilitare questa "
            "transizione."
        ),
        "testo_integrale": (
            """ETSI TS 101 733 [i.6], ETSI TS 101 903 [i.7], ETSI TS 102 778 [i.8], ETSI EN 319 122 [i.17], ETSI EN 319 132 [i.18] and ETSI EN 319 142 [i.19] define the formats of advanced (digital) signatures. These documents reference other documents defining various standardized data structures.

These other documents or companion documents define the algorithms which can be supported by the issuers of the data structures and the algorithms which will (for interoperability purposes) and can be supported by the users of the data structures:

• Signer Certificates (IETF RFC 5280 [i.9] and IETF RFC 3279 [7]).

• Certificate Revocation Lists (IETF RFC 5280 [i.9] and IETF RFC 3279 [7]).

• OCSP responses (IETF RFC 6960 [13]).

• Certification Authority Certificates (IETF RFC 5280 [i.9] and IETF RFC 3279 [7]).

• Self-signed certificates for CA certificates (IETF RFC 5280 [i.9] and IETF RFC 3279 [7]).

• Time-Stamping Tokens (TSTs) (IETF RFC 3161 [12] and ETSI EN 319 422 [i.15]).

• Time-Stamping Unit certificates (IETF RFC 3161 [12] and ETSI EN 319 422 [i.15]).

• Self-signed certificates for TSU Certificates (IETF RFC 5280 [i.9] and IETF RFC 3279 [7]).

• Attribute Certificates (Acs) (IETF RFC 5280 [i.9] and IETF RFC 3279 [7]).

For each data structure, the set of algorithms to be used is specified.

Since many of these documents have been published some years ago, they cannot be all up to date with the latest cryptographic advancements. In particular, some of the algorithms specified in the above documents exhibit weaknesses or, worse, are now broken. These algorithms are not listed in the following tables.

Despite outdated algorithms may be used in the verification of archive signatures, e.g. SHA-1, they are not mentioned in the following. The requirements of this annex apply to the date of issuance of the present document.

Algorithms which may be additionally supported by issuers or users are not indicated too.

For the transition to Post-Quantum Cryptography, the use of hybrid schemes (combining classical and post-quantum algorithms) should be considered for new implementations as indicated in clause 6.4. The tables below list both classical and post-quantum algorithms to facilitate this transition."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.2 (CAdES and PAdES)",
        "testo": (
            "Funzioni di hash e algoritmi di firma per CAdES e PAdES. Una firma digitale basata su CMS (ETSI "
            "TS 101 733/ETSI EN 319 122 ed ETSI TS 102 778/ETSI EN 319 142) contiene un identificatore della "
            "funzione di hash usata (elemento digestAlgorithm della struttura SignerInfo) e un identificatore "
            "dell'algoritmo di firma usato (elemento signatureAlgorithm della struttura SignerInfo), coerente "
            "con l'identificatore dell'algoritmo di firma contenuto nel certificato del firmatario. I "
            "requisiti della Tabella A.1 si applicano a CAdES e PAdES, sia alla funzione di hash sia "
            "all'algoritmo di firma. Funzioni di hash: gli emittenti di AdES devono supportare SHA-256 e "
            "dovrebbero supportare SHA-512 e SHA3-512; gli utilizzatori di AdES devono supportare SHA-256, "
            "SHA-384 e SHA-512 e dovrebbero supportare SHA3-256, SHA3-384 e SHA3-512. Algoritmi di firma: gli "
            "emittenti dovrebbero supportare RSA-PSS, DSA, EdDSA o ECDSA e ML-DSA o SLH-DSA (PQC); gli "
            "utilizzatori devono supportare RSA-PKCS1v1_5, RSA-PSS, DSA, EdDSA, ECDSA e ML-DSA, SLH-DSA "
            "(PQC). Legacy: gli emittenti possono supportare RSA-PKCS1v1_5; gli utilizzatori dovrebbero "
            "supportare EC-SDSA-opt (L). Note: l'uso di EdDSA (Ed25519, Ed448) e di algoritmi "
            "post-quantistici (ML-DSA, SLH-DSA) implica spesso funzioni di hash interne o gestione di stato "
            "definite dall'OID dell'algoritmo, e in tal caso la riga \"Hash functions\" si riferisce "
            "all'algoritmo di message digest usato per calcolare l'hash del contenuto prima "
            "dell'applicazione della primitiva di firma (es. l'attributo message-digest in CMS); durante la "
            "transizione PQC gli schemi ibridi possono richiedere due firme indipendenti o una struttura di "
            "firma composita, e in tal caso i requisiti si applicano a entrambe le componenti della suite "
            "ibrida; EC-SDSA-opt e' considerato legacy (L) e non raccomandato per nuove firme per il limitato "
            "supporto nelle librerie crittografiche diffuse."
        ),
        "testo_integrale": (
            """A CMS based digital signature (ETSI TS 101 733 [i.6]/ETSI EN 319 122 [i.17] and ETSI TS 102 778 [i.8]/ETSI EN 319 142 [i.19]) contains an identifier of the hash function that has been used (contained in the digestAlgorithm element from the SignerInfo data structure) and an identifier of the signature algorithm that has been used (contained in the signatureAlgorithm element from the SignerInfo data structure) which will be consistent with the identifier of the signature algorithm contained in the signer's certificate.

Requirements in Table A.1 apply to CAdES [i.6] and PAdES [i.8]. They apply both to the hash function and the signature algorithm.

Table A.1: Hash functions and signature algorithms for PAdES and CAdES

| CAdES [i.6] and PAdES [i.8] | Issuers of AdES | Users of AdES |
|---|---|---|
| Hash functions | shall support SHA-256; should support SHA-512; should support SHA3-512 | shall support SHA-256, SHA-384, SHA-512; should support SHA3-256, SHA3-384, SHA3-512 |
| Signature algorithms | should support RSA-PSS, DSA, EdDSA or ECDSA; should support ML-DSA or SLH-DSA (PQC) | shall support RSA-PKCS1v1_5, RSA-PSS , DSA, EdDSA,ECDSA; shall support ML-DSA, SLH-DSA (PQC) |
| Legacy | may support RSA-PKCS1v1_5 | should support EC-SDSA-opt (L) |

NOTE 1: The use of EdDSA (Ed25519, Ed448) and Post-Quantum algorithms (ML-DSA, SLH-DSA) often implies specific internal hash functions or state handling defined by the algorithm OID. In these cases, the "Hash functions" row applies to the message digest algorithm used to hash the content before the signature primitive is applied (e.g. the message-digest attribute in CMS).

NOTE 2: During the transition to Post-Quantum Cryptography, hybrid schemes may require two independent signatures or a composite signature structure. In such cases, the requirements apply to both components of the hybrid suite.

NOTE 3: EC-SDSA-opt is considered legacy (L) and not recommended for new signatures due to limited support in widely deployed cryptographic libraries."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "Annex A.3 (XAdES)",
        "testo": (
            "Funzioni di hash e algoritmi di firma per XAdES. ETSI TS 101 903/ETSI EN 319 132 usano un URI "
            "per referenziare la funzione di hash nell'elemento ds:DigestMethod; poiche' sono costruiti su XML "
            "DigSig, i requisiti algoritmici di XML DigSig [11] si applicano con le modifiche definite nella "
            "Tabella A.2. Funzioni di hash: gli emittenti di AdES devono supportare SHA-256 e dovrebbero "
            "supportare SHA-512 e SHA3-512; gli utilizzatori devono supportare SHA-256, SHA-384, SHA-512 e "
            "dovrebbero supportare SHA3-256, SHA3-384, SHA3-512. Algoritmi di firma: gli emittenti "
            "dovrebbero supportare RSA-PSS, DSA, EdDSA o ECDSA e ML-DSA o SLH-DSA (PQC); gli utilizzatori "
            "devono supportare RSA-PKCS1v1_5, RSA-PSS, DSA, EdDSA, ECDSA e ML-DSA, SLH-DSA (PQC). Legacy: gli "
            "emittenti possono supportare RSA-PKCS1v1_5; gli utilizzatori dovrebbero supportare EC-SDSA-opt "
            "(L). Per la canonicalizzazione: dovrebbe essere usato Canonical XML (omette i commenti) "
            "(http://www.w3.org/TR/2001/REC-xml-c14n-20010315); puo' essere usato Canonical XML with Comments "
            "(http://www.w3.org/TR/2002/REC-xml-exc-c14n-20020718). Note: EdDSA e algoritmi post-quantistici "
            "implicano spesso funzioni di hash interne definite dall'OID (la riga \"Hash functions\" si "
            "riferisce allora al message digest del contenuto); EC-SDSA-opt e' legacy e non raccomandato per "
            "nuove firme; durante la transizione PQC possono essere richiesti schemi ibridi (es. ECDSA "
            "combinata con ML-DSA) e le implementazioni dovrebbero riferirsi alla clausola 6.4 per le regole "
            "di composizione ibrida."
        ),
        "testo_integrale": (
            """ETSI TS 101 903 [i.7]/ETSI EN 319 132 [i.18] use a URI to reference the hash function in the ds:DigestMethod element. Since ETSI TS 101 903 [i.7]/ETSI EN 319 132 [i.18] are built upon XML DigSig, the algorithm requirements from XML DigSig [11] shall apply with the amendments defined in Table A.2.

Table A.2: Hash functions and signature algorithms for XAdES

| XAdES [i.7] | Issuers of AdES | Users of AdES |
|---|---|---|
| Hash functions | shall support SHA-256; should support SHA-512; should support SHA3-512 | shall support SHA-256, SHA-384, SHA-512; should support SHA3-256, SHA3-384, SHA3-512 |
| Signature algorithms | should support RSA-PSS, DSA, EdDSA or ECDSA; should support ML-DSA or SLH-DSA (PQC) | shall support RSA-PKCS1v1_5, RSA-PSS , DSA, EdDSA,ECDSA; shall support ML-DSA, SLH-DSA (PQC) |
| Legacy | may support RSA-PKCS1v1_5 | should support EC-SDSA-opt (L) |

For canonicalization:

1) the following Canonical XML (omits comments) [i.10] should be used: http://www.w3.org/TR/2001/REC-xml-c14n-20010315;

2) the following Canonical XML with Comments [i.11] may be used: http://www.w3.org/TR/2002/REC-xml-exc-c14n-20020718.

NOTE 1: The use of EdDSA (Ed25519, Ed448) and Post-Quantum algorithms (ML-DSA, SLH-DSA) often implies specific internal hash functions or state handling defined by the algorithm OID. In these cases, the "Hash functions" row applies to the message digest algorithm used to hash the content before the signature primitive is applied (e.g. the message-digest attribute in CMS).

NOTE 2: EC-SDSA-opt is considered legacy (L) and not recommended for new signatures due to limited support in widely deployed cryptographic libraries.

NOTE 3: During the transition to Post-Quantum Cryptography, hybrid schemes (e.g. combining ECDSA with ML-DSA) may be required. Implementations should refer to clause 6.4 for hybrid composition rules."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "Annex A.4 (Signer's certificates)",
        "testo": (
            "Certificati del firmatario. Un certificato del firmatario contiene una chiave pubblica del "
            "soggetto ed e' firmato da una chiave emittente di CA; IETF RFC 5280 non richiede l'uso di "
            "algoritmi crittografici particolari, mentre IETF RFC 3279 si', e i requisiti di IETF RFC 3279 si "
            "applicano alle chiavi pubbliche del firmatario e alle chiavi emittenti di CA con le modifiche "
            "della Tabella A.3. Funzioni di hash (in tabella, riga delle chiavi pubbliche): gli emittenti di "
            "certificati del firmatario dovrebbero supportare RSA, DSA, EdDSA o ECDSA e ML-DSA o SLH-DSA "
            "(PQC); gli utilizzatori devono supportare RSA, DSA, EdDSA, ECDSA e ML-DSA, SLH-DSA. Algoritmi di "
            "firma: gli emittenti devono supportare RSA, EdDSA o ECDSA e dovrebbero supportare schemi ibridi "
            "(classici + ML-DSA/SLH-DSA); gli utilizzatori devono supportare RSA, DSA, EdDSA, ECDSA e ML-DSA, "
            "SLH-DSA. Legacy: gli emittenti possono supportare RSA-PKCS1v1_5; gli utilizzatori dovrebbero "
            "supportare EC-SDSA-opt (L). Con RSA e DSA le funzioni di hash SHA-256 e SHA-512 dovrebbero "
            "essere usate al posto di SHA-224 o SHA-384. Note: l'uso di EdDSA (Ed25519, Ed448) implica "
            "formati specifici di subject public key information (IETF RFC 8410); per la crittografia "
            "post-quantistica (ML-DSA, SLH-DSA) le strutture di subject public key information sono definite "
            "in NIST FIPS 204 e NIST FIPS 205 (o nei corrispondenti IETF RFC); durante la transizione PQC i "
            "certificati ibridi contenenti chiavi classiche e post-quantistiche (o piu' certificati collegati "
            "tramite estensioni specifiche) sono RACCOMANDATI per le chiavi emittenti di CA, per garantire "
            "sicurezza a lungo termine."
        ),
        "testo_integrale": (
            """A signer certificate contains a subject public key and is signed by a CA issuing key. IETF RFC 5280 [i.9] does not require to use any particular cryptographic algorithms. However, IETF RFC 3279 [7] does. The requirements in IETF RFC 3279 [7] shall apply to signer public keys and CA issuing keys with the amendments defined in Table A.3.

Table A.3: Algorithms for signer public keys and CA issuing keys

| Signer certificates | Issuers of signer certificates | Users of signer certificates |
|---|---|---|
| Hash functions | should support RSA, DSA, EdDSA or ECDSA; should support ML-DSA or SLH-DSA (PQC) | shall support RSA, DSA, EdDSA, ECDSA; shall support ML-DSA, SLH-DSA |
| Signature algorithms | shall support RSA, EdDSA or ECDSA; should support Hybrid (Classical + ML-DSA/SLH-DSA) | shall support RSA, DSA, EdDSA, ECDSA; shall support ML-DSA, SLH-DSA |
| Legacy | may support RSA-PKCS1v1_5 | should support EC-SDSA-opt (L) |

With RSA and DSA, the hash functions SHA-256 and SHA-512 should be used instead of SHA-224 or SHA-384.

NOTE 1: The use of EdDSA (Ed25519, Ed448) implies specific subject public key information formats as defined in IETF RFC 8410 [24].

NOTE 2: For Post-Quantum Cryptography (ML-DSA, SLH-DSA), the subject public key information structures are defined in NIST FIPS 204 and NIST FIPS 205 (or the corresponding IETF RFCs).

NOTE 3: During the transition to Post-Quantum Cryptography, hybrid certificates containing both classical and post-quantum keys (or multiple certificates linked via specific extensions) are RECOMMENDED for CA issuing keys to ensure long-term security."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "Annex A.5 (CRLs)",
        "testo": (
            "Liste di revoca dei certificati (CRL). Una CRL e' firmata da un emittente di CRL; IETF RFC 5280 "
            "non richiede l'uso di algoritmi crittografici particolari, mentre IETF RFC 3279 si', e i "
            "requisiti di IETF RFC 3279 si applicano alle chiavi pubbliche dell'emittente di CRL con le "
            "modifiche della Tabella A.4. Chiavi dell'emittente di CRL: gli emittenti di CRL devono "
            "supportare RSA con SHA-256 e dovrebbero supportare EdDSA o ECDSA e ML-DSA o SLH-DSA; gli "
            "utilizzatori di CRL devono supportare RSA, DSA, EdDSA, ECDSA e ML-DSA, SLH-DSA. Note: poiche' "
            "l'uso di SHA-224 con RSA e DSA non offre vantaggi rispetto a SHA-256 ne' in sicurezza ne' in "
            "prestazioni, non esiste alcun requisito di supporto di SHA-224 con questi algoritmi; per EdDSA "
            "(Ed25519, Ed448) e per gli algoritmi post-quantistici (ML-DSA, SLH-DSA) la funzione di hash e' "
            "spesso intrinseca alla definizione dell'algoritmo di firma. Con RSA e DSA le funzioni di hash "
            "SHA-256 e SHA-512 dovrebbero essere usate al posto di SHA-224 o SHA-384."
        ),
        "testo_integrale": (
            """A CRL is signed by a CRL Issuer. IETF RFC 5280 [i.9] does not require to use any particular cryptographic algorithms. However, IETF RFC 3279 [7] does. The requirements defined in IETF RFC 3279 [7] shall apply to CRL Issuer public keys with the amendments defined in Table A.4.

Table A.4: Algorithms for CRL issuer public keys

| CRLs | Issuers of CRLs | Users of CRLs |
|---|---|---|
| CRL issuer keys | shall support RSA with SHA-256; should support EdDSA or ECDSA; should support ML-DSA or SLH-DSA | shall support RSA, DSA, EdDSA, ECDSA; shall support ML-DSA, SLH-DSA |

NOTE 1: Because the usage of SHA-224 with RSA and DSA gives no advantage compared with SHA-256 neither in security nor in performance there is no requirement on SHA-224 support with these algorithms.

NOTE 2: For EdDSA (Ed25519, Ed448) and Post-Quantum algorithms (ML-DSA, SLH-DSA), the hash function is often intrinsic to the signature algorithm definition.

With RSA and DSA the hash functions SHA-256 and SHA-512 should be used instead of SHA-224 or SHA-384."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "Annex A.6 (OCSP responses)",
        "testo": (
            "Risposte OCSP. Una risposta OCSP e' firmata da un risponditore OCSP; i requisiti algoritmici "
            "della clausola 4.3 di IETF RFC 6960 si applicano con le modifiche della Tabella A.5, sia "
            "all'algoritmo di hash sia all'algoritmo di firma usati dai risponditori OCSP. Chiavi del "
            "risponditore OCSP: gli emittenti di risposte OCSP devono supportare RSA con SHA-256 e dovrebbero "
            "supportare EdDSA o ECDSA e ML-DSA o SLH-DSA; gli utilizzatori di risposte OCSP devono supportare "
            "RSA, DSA, EdDSA, ECDSA e ML-DSA, SLH-DSA. Note: per EdDSA (Ed25519, Ed448) e per gli algoritmi "
            "post-quantistici (ML-DSA, SLH-DSA) la funzione di hash e' intrinseca alla definizione "
            "dell'algoritmo di firma o specificata nel parameter set; durante la transizione PQC i "
            "risponditori OCSP possono firmare le risposte con schemi ibridi (es. firma classica + firma "
            "post-quantistica) per garantire non ripudio a lungo termine."
        ),
        "testo_integrale": (
            """An OCSP response is signed by an OCSP responder. The algorithm requirements from IETF RFC 6960 [13], clause 4.3 shall apply with the amendments defined in Table A.5. These requirements shall apply to the hash algorithm and the signature algorithm used by OCSP responders.

Table A.5: Algorithms for OCSP responders

| OCSP response | Issuers of OCSP responses | Users of OCSP response |
|---|---|---|
| OCSP responder keys | shall support RSA with SHA-256; should support EdDSA or ECDSA; should support ML-DSA or SLH-DSA | shall support RSA, DSA, EdDSA, ECDSA; shall support ML-DSA, SLH-DSA |

NOTE 1: For EdDSA (Ed25519, Ed448) and Post-Quantum algorithms (ML-DSA, SLH-DSA), the hash function is intrinsic to the signature algorithm definition or specified within the parameter set.

NOTE 2: During the transition to Post-Quantum Cryptography, OCSP responders may sign responses using hybrid schemes (e.g. classical signature + post-quantum signature) to ensure long-term non-repudiation."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "Annex A.7 (CA certificates)",
        "testo": (
            "Certificati di autorita' di certificazione. Un certificato di CA contiene una chiave pubblica di "
            "CA ed e' firmato da una chiave privata di CA; per le chiavi pubbliche di CA (come soggetto) e le "
            "chiavi pubbliche di CA (come emittente) si applicano i requisiti algoritmici di IETF RFC 3279 "
            "con le modifiche della Tabella A.6. Chiave pubblica di CA soggetto: gli emittenti di certificati "
            "di CA dovrebbero supportare RSA, EdDSA o ECDSA e ML-DSA (PQC); gli utilizzatori devono "
            "supportare RSA, DSA, EdDSA, ECDSA e ML-DSA, SLH-DSA. Chiavi pubbliche di CA emittente: gli "
            "emittenti dovrebbero supportare RSA, EdDSA o ECDSA e schemi ibridi (classici + ML-DSA); gli "
            "utilizzatori devono supportare RSA, DSA, EdDSA, ECDSA e ML-DSA, SLH-DSA (il documento ufficiale "
            "riporta per questa cella \"hall support\", refuso per \"shall support\"). Note: l'uso di SHA-224 "
            "con RSA e DSA non offre vantaggi rispetto a SHA-256 ne' in sicurezza ne' in prestazioni e non "
            "esiste quindi requisito di supporto di SHA-224 con questi algoritmi; per EdDSA (Ed25519, Ed448) "
            "e per gli algoritmi post-quantistici (ML-DSA, SLH-DSA) la funzione di hash e' spesso intrinseca "
            "alla definizione dell'algoritmo di firma (es. SHA-512 per Ed25519, SHAKE256 per Ed448/ML-DSA); "
            "durante la transizione PQC i certificati di CA ibridi (es. con estensioni X.509 di chiave "
            "pubblica alternativa o chiavi composite) sono RACCOMANDATI per le chiavi di CA emittente, per "
            "garantire la sicurezza a lungo termine della gerarchia PKI. Con RSA e DSA, SHA-256 e SHA-512 "
            "dovrebbero essere usati al posto di SHA-224 o SHA-384."
        ),
        "testo_integrale": (
            """A CA certificate contains a CA public key and is signed by a CA private key. For CA public keys (as subject) and CA public keys (as issuer), the algorithm requirements from IETF RFC 3279 [7] shall apply with the amendments defined in Table A.6.

Table A.6: Algorithms for certification authorities

| CA certificates | Issuers of CA certificates | Users of CA certificates |
|---|---|---|
| Subject CA public key | should support RSA, EdDSA or ECDSA; should support ML-DSA (PQC) | shall support RSA, DSA, EdDSA, ECDSA; shall support ML-DSA, SLH-DSA |
| Issuer CA public keys | should support RSA, EdDSA or ECDSA; should support Hybrid (Classical + ML-DSA) | hall support RSA, DSA, EdDSA, ECDSA; shall support ML-DSA, SLH-DSA |

NOTE 1: Because the usage of SHA-224 with RSA and DSA gives no advantage compared with SHA-256 neither in security nor in performance there is no requirement on SHA-224 support with these algorithms.

NOTE 2: For EdDSA (Ed25519, Ed448) and Post-Quantum algorithms (ML-DSA, SLH-DSA), the hash function is often intrinsic to the signature algorithm definition (e.g. SHA-512 for Ed25519, SHAKE256 for Ed448/ML-DSA).

NOTE 3: During the transition to Post-Quantum Cryptography, hybrid CA certificates (e.g. using X.509 alternative public key extensions or composite keys) are RECOMMENDED for Issuer CA keys to ensure long-term security of the PKI hierarchy.

With RSA and DSA, SHA-256 and SHA-512 should be used instead of SHA-224 or SHA-384."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "Annex A.8 (Self-signed certificates for CA issuing CA certificates)",
        "testo": (
            "Certificati auto-firmati per CA che emettono certificati di CA. Un certificato auto-firmato "
            "contiene una sola chiave pubblica di CA radice; per le chiavi pubbliche di CA radice si applicano "
            "i requisiti algoritmici di IETF RFC 3279 con le modifiche della Tabella A.7. Chiavi pubbliche di "
            "CA radice: gli emittenti di certificati auto-firmati devono supportare RSA con SHA-256/512 e "
            "dovrebbero supportare EdDSA o ECDSA e ML-DSA o SLH-DSA (PQC); gli utilizzatori devono supportare "
            "RSA, DSA, EdDSA, ECDSA e ML-DSA, SLH-DSA. Note: i certificati auto-firmati devono resistere a "
            "lungo (es. piu' di 10 o 20 anni), quindi la scelta di algoritmi e dimensioni di chiave richiede "
            "di considerare la sicurezza a lungo termine, inclusa la resistenza agli attacchi con computer "
            "quantistici (clausola 8.5); per EdDSA (Ed25519, Ed448) e per gli algoritmi post-quantistici "
            "(ML-DSA, SLH-DSA) la funzione di hash e' intrinseca alla definizione dell'algoritmo di firma; "
            "per garantire sicurezza a lungo termine durante la transizione PQC gli emittenti dovrebbero "
            "considerare l'uso di schemi ibridi (es. estensioni X.509 di chiave pubblica alternativa per "
            "portare una chiave PQC accanto a una classica) per le CA radice. Con RSA e DSA, SHA-256 e "
            "SHA-512 dovrebbero essere usati al posto di SHA-224 o SHA-384."
        ),
        "testo_integrale": (
            """A self-signed certificate contains a single root CA public key. For root CA public keys, the algorithm requirements from IETF RFC 3279 [7] shall apply with the amendments defined in Table A.7.

NOTE 1: Self-signed certificates need to resist quite long (e.g. more than 10 or 20 years). Therefore, the selection of algorithms and key sizes requires consideration of long-term security, including resistance against quantum computing attacks (see clause 8.5).

Table A.7: Algorithms for self-signed certificates

| Self-signed certificates | Issuers of self-signed certificates | Users of self-signed certificates |
|---|---|---|
| Root CA public keys | shall support RSA with SHA-256/512; should support EdDSA or ECDSA; should support ML-DSA or SLH-DSA (PQC) | shall support RSA, DSA, EdDSA, ECDSA; shall support ML-DSA, SLH-DSA |

NOTE 2: For EdDSA (Ed25519, Ed448) and Post-Quantum algorithms (ML-DSA, SLH-DSA), the hash function is intrinsic to the signature algorithm definition.

NOTE 3: To ensure long-term security during the transition to Post-Quantum Cryptography, issuers should consider using hybrid schemes (e.g. using X.509 alternative public key extensions to carry a PQC key alongside a classical key) for Root CAs.

With RSA and DSA, SHA-256 and SHA-512 should be used instead of SHA-224 or SHA-384."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "Annex A.9 (TSTs based on IETF RFC 3161)",
        "testo": (
            "Token di marca temporale (TST) basati su IETF RFC 3161: i requisiti seguenti si applicano alle "
            "funzioni di hash e agli algoritmi di firma dei TST, e i requisiti algoritmici di IETF RFC 3161 si "
            "applicano con le modifiche della Tabella A.8. Funzione di hash: i richiedenti TST devono "
            "supportare SHA-256 e dovrebbero supportare SHA-384 e SHA-512; gli emittenti TST devono "
            "supportare SHA-256 e dovrebbero supportare SHA-384 e SHA-512; i verificatori TST devono "
            "supportare SHA-256, SHA-384 e SHA-512. Algoritmi di firma del TST: i richiedenti devono "
            "supportare RSA, DSA, EdDSA, ECDSA; gli emittenti devono supportare RSA, EdDSA, ECDSA e "
            "dovrebbero supportare SLH-DSA, XMSS o LMS (PQC); i verificatori devono supportare RSA, DSA, "
            "EdDSA, ECDSA e SLH-DSA, XMSS, LMS. Note: per l'archiviazione a lungo termine (piu' di 20 anni) "
            "e' richiesto l'uso della crittografia post-quantistica; XMSS (IETF RFC 8391) e LMS (IETF RFC "
            "8554) sono schemi di firma hash-based con stato, specificamente raccomandati per casi d'uso come "
            "aggiornamenti firmware e marcatura temporale, dove la gestione dello stato puo' essere gestita in "
            "modo sicuro dalla TSU; per EdDSA (Ed25519, Ed448) e per gli algoritmi post-quantistici (ML-DSA, "
            "SLH-DSA) la funzione di hash e' spesso intrinseca alla definizione dell'algoritmo di firma; nel "
            "contesto della transizione PQC sono RACCOMANDATE funzioni di hash con lunghezza di output di "
            "almeno 384 bit (es. SHA-384, SHA-512)."
        ),
        "testo_integrale": (
            """The following requirements apply to hash functions and TST signature algorithms. The algorithm requirements from IETF RFC 3161 [12] shall apply with the amendments defined in Table A.8.

Table A.8: Algorithms for timestamps

| Time-Stamping Tokens | TST requesters | TST issuers | TST verifiers |
|---|---|---|---|
| Hash function | shall support SHA-256; should support SHA-384, SHA-512 | shall support SHA-256; should support SHA-384, SHA-512 | shall support SHA-256, SHA-384, SHA-512 |
| TST signature algorithms | shall support RSA, DSA, EdDSA, ECDSA | shall support RSA, EdDSA, ECDSA; should support SLH-DSA, XMSS or LMS (PQC) | shall support RSA, DSA, EdDSA, ECDSA; shall support SLH-DSA, XMSS, LMS |

NOTE 1: For long-term archiving (> 20 years), the use of Post-Quantum Cryptography is required. XMSS (IETF RFC 8391 [29]) and LMS (IETF RFC 8554 [28]) are stateful hash-based signature schemes specifically recommended for use cases like firmware updates and time-stamping, where the state management can be securely handled by the TSU.

NOTE 2: For EdDSA (Ed25519, Ed448) and Post-Quantum algorithms (ML-DSA, SLH-DSA), the hash function is often intrinsic to the signature algorithm definition.

NOTE 3: In the context of PQC transition, hash functions with an output length of at least 384 bits (e.g. SHA-384, SHA-512) are RECOMMENDED."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "Annex A.10 (TSU certificates)",
        "testo": (
            "Certificati di Time-Stamping Unit (TSU). Un certificato TSU contiene una chiave pubblica di TSU "
            "ed e' firmato da una chiave privata di CA; per le chiavi pubbliche di TSU (come soggetto) e le "
            "chiavi pubbliche di CA (come emittente) si applicano i requisiti algoritmici di IETF RFC 3279 "
            "con le modifiche della Tabella A.9. Chiave pubblica di TSU: gli emittenti di certificati TSU "
            "dovrebbero supportare RSA, EdDSA o ECDSA e SLH-DSA, XMSS o LMS (PQC); gli utilizzatori devono "
            "supportare RSA, DSA, EdDSA, ECDSA e SLH-DSA, XMSS, LMS. Chiavi pubbliche di CA emittente: gli "
            "emittenti dovrebbero supportare RSA, EdDSA o ECDSA e schemi ibridi (classici + ML-DSA); gli "
            "utilizzatori devono supportare RSA, DSA, EdDSA, ECDSA e ML-DSA, SLH-DSA. Note: XMSS (IETF RFC "
            "8391) e LMS (IETF RFC 8554) sono schemi di firma hash-based con stato, specificamente "
            "RACCOMANDATI per le Time-Stamping Unit dove la gestione dello stato puo' essere imposta "
            "rigorosamente dal modulo crittografico, con elevate garanzie di sicurezza contro attacchi con "
            "computer quantistici per la validazione a lungo termine; per EdDSA (Ed25519, Ed448) e per gli "
            "algoritmi post-quantistici (ML-DSA, SLH-DSA, XMSS, LMS) la funzione di hash e' spesso intrinseca "
            "alla definizione dell'algoritmo di firma; durante la transizione PQC i certificati TSU hanno in "
            "genere periodi di validita' piu' brevi dei certificati di CA, ma la chiave pubblica della TSU "
            "(e le marche temporali risultanti) devono restare verificabili a lungo, quindi l'uso di "
            "algoritmi PQC o di schemi ibridi per la chiave TSU e' critico. Con RSA e DSA, SHA-256 e SHA-512 "
            "dovrebbero essere usati al posto di SHA-224 o SHA-384."
        ),
        "testo_integrale": (
            """A TSU certificate contains a TSU public key and is signed by a CA private key. For TSU public keys (as subject) and CA public keys (as issuer), the algorithm requirements from IETF RFC 3279 [7] shall apply with the amendments defined in Table A.9.

Table A.9: Algorithms for timestamping units

| TSU certificates | Issuers of TSU certificates | Users of TSU certificates |
|---|---|---|
| TSU public key | should support RSA, EdDSA or ECDSA; should support SLH-DSA, XMSS or LMS (PQC) | shall support RSA, DSA, EdDSA, ECDSA; shall support SLH-DSA, XMSS, LMS |
| Issuer CA public keys | should support RSA, EdDSA or ECDSA; should support Hybrid (Classical + ML-DSA) | shall support RSA, DSA, EdDSA, ECDSA; shall support ML-DSA, SLH-DSA |

NOTE 1: XMSS (IETF RFC 8391 [29]) and LMS (IETF RFC 8554 [28]) are stateful hash-based signature schemes. They are specifically RECOMMENDED for Time-Stamping Units (TSUs) where state management can be strictly enforced by the cryptographic module, providing high security assurances against quantum computer attacks for long-term validation.

NOTE 2: For EdDSA (Ed25519, Ed448) and Post-Quantum algorithms (ML-DSA, SLH-DSA, XMSS, LMS), the hash function is often intrinsic to the signature algorithm definition.

NOTE 3: During the transition to Post-Quantum Cryptography, TSU certificates typically have shorter validity periods than CA certificates. However, the TSU public key itself (and the resulting time-stamps) is expected to remain verifiable for long periods. Therefore, the use of PQC-algorithms or hybrid schemes for the TSU key is critical.

With RSA and DSA, SHA-256 and SHA-512 should be used instead of SHA-224 or SHA-384."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "Annex A.11 (Self-signed certificates for CAs issuing TSU certificates)",
        "testo": (
            "Certificati auto-firmati per CA che emettono certificati TSU. Un certificato auto-firmato "
            "contiene una sola chiave pubblica di CA radice; per i certificati auto-firmati delle CA che "
            "emettono certificati TSU si applicano i requisiti algoritmici di IETF RFC 3279 con le modifiche "
            "della Tabella A.7 (vedi clausola A.8). Note: i certificati auto-firmati per le gerarchie TSU "
            "fungono spesso da trust anchor per la validazione a lungo termine (es. archiviazione elettronica "
            "qualificata) e devono quindi resistere ad attacchi criptanalitici per periodi molto lunghi (es. "
            "piu' di 20 anni); di conseguenza l'uso della crittografia post-quantistica (in particolare "
            "SLH-DSA o ML-DSA in modalita' ibrida) come definito nella Tabella A.7 e' fortemente "
            "RACCOMANDATO per le nuove CA radice TSU, per garantire che le marche temporali restino "
            "verificabili anche dopo l'avvento di computer quantistici crittograficamente rilevanti."
        ),
        "testo_integrale": (
            """A self-signed certificate contains a single root CA public key. For self-signed certificates for CAs issuing TSU certificates, the algorithm requirements from IETF RFC 3279 [7] shall apply with the amendments defined in Table A.7 (see clause A.8).

NOTE 1: Self-signed certificates for TSU hierarchies often serve as trust anchors for long-term validation (e.g. Qualified Electronic Archiving) and therefore need to resist cryptanalytic attacks for very long periods (e.g. > 20 years).

NOTE 2: Consequently, the use of Post-Quantum Cryptography (specifically SLH-DSA or ML-DSA in hybrid modes) as defined in Table A.7 is strongly RECOMMENDED for new TSU Root CAs to ensure that timestamps remain verifiable beyond the entry of cryptographically relevant quantum computers."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex B (Signature maintenance)",
        "testo": (
            "Manutenzione della firma (annesso informativo ma con raccomandazione operativa). Una firma "
            "elettronica avanzata (digitale) puo' essere verificata secondo una signature policy che "
            "soddisfi le esigenze di business; la policy puo' includere vincoli su quali algoritmi e "
            "dimensioni di chiave siano appropriati e/o definire un momento oltre il quale gli "
            "algoritmi/chiavi relativi a una firma elettronica avanzata non dovrebbero piu' essere "
            "considerati affidabili in assenza di misure di sicurezza aggiuntive. Puo' essere necessario "
            "riverificare le firme avanzate (verifica successiva) ben oltre il momento della verifica "
            "iniziale: a quel punto trust anchor e algoritmi definiti nella policy iniziale possono non "
            "essere piu' sicuri e occorre adottare misure di sicurezza aggiuntive. Considerazione specifica "
            "per la crittografia post-quantistica: con l'avvento di computer quantistici crittograficamente "
            "rilevanti (CRQC) gli algoritmi asimmetrici classici (RSA, DSA, ECDSA, EdDSA) diventeranno "
            "insicuri, e per le firme che richiedono validita' a lungo termine (es. archiviazione "
            "elettronica qualificata superiore a 10 anni) il processo di manutenzione della firma deve "
            "affrontare proattivamente questa minaccia. Cio' vale anche quando chiavi sicure al momento "
            "della verifica iniziale non lo siano piu' in seguito (es. compromissione della chiave). In "
            "entrambi i casi la sicurezza di una firma avanzata gia' verificata con successo puo' essere "
            "mantenuta con: archiviazione sicura della definizione della signature policy (o di un "
            "riferimento non ambiguo a essa) e di tutti i dati inizialmente usati per verificarla; oppure "
            "archiviazione sicura della definizione della signature policy e aggiunta alla firma di altri "
            "dati (es. marche temporali) che consentano le verifiche successive. Raccomandazione per la "
            "transizione PQC: si RACCOMANDA che il processo di manutenzione (es. applicazione di Archive "
            "Time-Stamps) utilizzi algoritmi quantum-safe (firme hash-based come SLH-DSA, XMSS, LMS, o "
            "schemi ibridi per le autorita' di marcatura temporale che proteggono l'archivio) e funzioni di "
            "hash robuste con output piu' lunghi (es. SHA-384, SHA-512, SHA3-384) per resistere agli "
            "attacchi di collisione quantistici. Tali misure possono essere definite nella signature policy "
            "stessa o in un insieme di regole denominato signature maintenance policy; un'applicazione "
            "tempestiva del processo di manutenzione consente la riverifica delle firme avanzate anche in un "
            "momento in cui algoritmi e dimensioni di chiave originariamente usati non sono piu' sicuri: "
            "prima il processo viene applicato, meglio e'."
        ),
        "testo_integrale": (
            """An advanced (digital) signature (see ETSI TS 101 733 [i.6], ETSI TS 101 903 [i.7], ETSI TS 102 778 [i.8], ETSI EN 319 122 [i.17], ETSI EN 319 132 [i.18] and ETSI EN 319 142 [i.19]) can be verified according to a signature policy that meets the business needs.

A signature policy can include constraints about which algorithms and key lengths are deemed appropriate under that policy and/or define a time beyond which the algorithms/keys related to an advanced electronic signature should not be trusted anymore, unless additional security measures are taken.

It may be required to re-verify advanced signatures (this is called a subsequent verification) well beyond the time they were initially verified. At the time of re-verification, trust anchors and algorithms that were initially defined in the signature policy may not be secure anymore. Additional security measures need to be taken so that this can be accomplished.

Specific Consideration for Post-Quantum Cryptography: In particular, with the advent of Cryptographically Relevant Quantum Computers (CRQC), classical asymmetric algorithms (RSA, DSA, ECDSA, EdDSA) are expected to become insecure. For signatures requiring long-term validity (e.g. Qualified Electronic Archiving > 10 years), the signature maintenance process is expected to address this threat proactively.

It can also happen that some keys were secure at the time the initial verification of an advanced signature was performed, but due to some "accident" this is no more the case later on (e.g. due to a key compromise).

In both cases, it is possible to maintain the security of an advanced signature which has already been successfully verified. This can be achieved with security measures such as:

• the secure archival of both the definition of the signature policy (or an unambiguous reference to it) and all the data initially used to verify the advanced signature according to that signature policy; or

• the secure archival of both the definition of the signature policy and the addition to the advanced signature of other data (e.g. time-stamps) that will allow subsequent verifications.

PQC Transition Recommendation: During the transition to Post-Quantum Cryptography, it is RECOMMENDED that the maintenance process (e.g. applying Archive Time-Stamps) utilizes:

1) Quantum-Safe Algorithms: Use of hash-based signatures (e.g. SLH-DSA, XMSS, LMS) or hybrid schemes for the time-stamping authorities protecting the archive; and

2) Strong Hash Functions: Use of hash functions with larger outputs (e.g. SHA-384, SHA-512, SHA3-384) to resist quantum collision attacks.

These measures can be defined in the signature policy itself or "elsewhere" in a set of rules called a "signature maintenance policy" which will allow maintenance of the validity of advanced signatures.

A timely application of a signature maintenance process allows for re-verification of advanced signatures under a given signature policy even at a point in time where it is possible or likely that the algorithms and key lengths originally used will not be secure anymore. The sooner the process is applied, the better."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 9.1 (General notes)",
        "testo": (
            "Note generali sulla durata e resistenza di funzioni di hash e chiavi. Le funzioni di hash e gli "
            "algoritmi di firma definiti nel presente documento sono utilizzabili nel contesto delle firme "
            "elettroniche avanzate definite in ETSI TS 101 733, ETSI TS 101 903, ETSI TS 102 778, ETSI EN 319 "
            "122, ETSI EN 319 132 ed ETSI EN 319 142. Il periodo di tempo per cui una data chiave deve "
            "restare confidenziale dipende dall'uso della chiave; piu' in generale, il periodo di tempo per "
            "cui un dato meccanismo deve resistere ad attacchi criptanalitici dipende dal modo in cui viene "
            "usato, e determinare tale periodo consente di applicare i valori forniti nella clausola 9 per "
            "derivare i parametri appropriati. Note esplicative, nessun obbligo a carico di un soggetto."
        ),
        "testo_integrale": (
            """NOTE 1: The hash functions and signature algorithms defined in the present document are suitable to be used in the context of advanced electronic signatures ETSI TS 101 733 [i.6], ETSI TS 101 903 [i.7], ETSI TS 102 778 [i.8], ETSI EN 319 122 [i.17], ETSI EN 319 132 [i.18] and ETSI EN 319 142 [i.19].

NOTE 2: The time period over which a given key needs to remain confidential depends on the usage of the key. More generally, the period of time over which a given mechanism needs to resist cryptanalytic attacks depends on the way it is being used. Determining this time period for a given mechanism allows one to then apply the figures provided in clause 9 to derive appropriate parameters."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 10.2.1 (Introduction)",
        "testo": (
            "Introduzione alla clausola 10.2: tutti gli OID elencati nella clausola sono reperibili nell'OID "
            "repository (riferimento informativo [i.13]). Nota esplicativa, nessun obbligo."
        ),
        "testo_integrale": (
            "NOTE: All listed here OID can be found in the OID repository [i.13]."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 10.3.2 (Signature algorithms)",
        "testo": (
            "Algoritmi di firma identificati tramite URI: non e' necessario definire tali URI, poiche' XAdES "
            "usa gli algoritmi di firma contenuti nei certificati X.509, referenziati tramite OID. Nota "
            "esplicativa, nessun obbligo."
        ),
        "testo_integrale": (
            "NOTE: There is no need to define such URIs since XAdES uses the signature algorithms contained in X.509 certificates which are referenced using OIDs."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex C.1 (JSON file location)",
        "testo": (
            "Posizione del file JSON della versione machine-readable del documento: il file "
            "https://forge.etsi.org/rep/esi/x19_312_crypto_suites/raw/v2.1.1/19312MachineReadable.json "
            "(19312MachineReadable.json) contiene la versione JSON del presente documento. Nota: "
            "indipendentemente dal presente documento, la versione piu' recente del file JSON e' collegata a "
            "https://forge.etsi.org/rep/esi/x19_312_crypto_suites/-/blob/main/19312MachineReadable.json. "
            "Dichiarazione di fatto, nessun obbligo."
        ),
        "testo_integrale": (
            """The file at https://forge.etsi.org/rep/esi/x19_312_crypto_suites/raw/v2.1.1/19312MachineReadable.json (19312MachineReadable.json) contains the JSON version of the present document.

NOTE: Independent of the present document, the latest version of the JSON file is linked to https://forge.etsi.org/rep/esi/x19_312_crypto_suites/-/blob/main/19312MachineReadable.json."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex C.2 (XML file location)",
        "testo": (
            "Posizione del file XML della versione machine-readable del documento: il file "
            "https://forge.etsi.org/rep/esi/x19_312_crypto_suites/raw/v2.1.1/19312MachineReadable.xml "
            "(19312MachineReadable.xml) contiene la versione XML del presente documento. Nota: "
            "indipendentemente dal presente documento, la versione piu' recente del file XML e' collegata a "
            "https://forge.etsi.org/rep/esi/x19_312_crypto_suites/-/blob/main/19312MachineReadable.xml. "
            "Dichiarazione di fatto, nessun obbligo."
        ),
        "testo_integrale": (
            """The file at https://forge.etsi.org/rep/esi/x19_312_crypto_suites/raw/v2.1.1/19312MachineReadable.xml (19312MachineReadable.xml) contains the XML version of the present document.

NOTE: Independent of the present document, the latest version of the XML file is linked to https://forge.etsi.org/rep/esi/x19_312_crypto_suites/-/blob/main/19312MachineReadable.xml."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D (Discontinued algorithms)",
        "testo": (
            "Algoritmi dismessi (annesso informativo): elenca gli algoritmi non piu' raccomandati, nemmeno "
            "con stato legacy, che erano raccomandati in versioni precedenti del documento. L'informazione "
            "puo' essere usata come base per i vincoli crittografici specificati da ETSI TS 119 172-1, "
            "clausola A.4.2.1, Tabella A.2 riga p, per la validazione di firme elettroniche nel passato, "
            "tipicamente basata su informazioni di prova dell'esistenza (es. marche temporali), come "
            "specificato in ETSI EN 319 102-1, clausola 5. Un modo per determinare una data di scadenza per "
            "un algoritmo, o per una combinazione di algoritmo e dimensione di chiave, e' considerare: la "
            "data di un eventuale attacco pratico noto; la data di pubblicazione dell'ultima specifica che "
            "raccomandava l'algoritmo o la combinazione; il numero di anni di resistenza dichiarato da quella "
            "specifica; e la data di pubblicazione della specifica successiva in cui ha smesso di essere "
            "raccomandato. I periodi di resistenza elencati in versioni precedenti del documento sono stati "
            "comunemente interpretati come relativi alla data di creazione della firma o all'emissione di un "
            "certificato per una chiave, invece che alla data di pubblicazione della versione del documento "
            "che conteneva la raccomandazione: il periodo d'uso effettivo puo' quindi estendersi oltre la "
            "data in cui l'algoritmo o la dimensione di chiave ha smesso di essere raccomandato in una "
            "versione successiva (es. RSA con 1 536 bit ha smesso di essere raccomandato in 2018-09, ma un "
            "certificato per una chiave RSA da 1 536 bit puo' essere stato emesso poco prima con validita' "
            "di 1 anno, secondo la raccomandazione precedente, terminando quindi solo un anno dopo, in "
            "2019-09). Nelle Tabelle D.1-D.3 l'ultima colonna indica i vincoli crittografici utilizzabili "
            "per default, in assenza di considerazioni divergenti di interoperabilita' o sicurezza "
            "specifiche dell'applicazione; i vincoli derivano da un'interpretazione indulgente dei periodi "
            "di resistenza, salvo smentita da un attacco pratico pubblicato. Tabella D.1 (funzioni di hash "
            "dismesse): RIPEMD160 (ultima raccomandazione ETSI TS 102 176-1 V2.0.0, 3 anni di resistenza, "
            "non raccomandato da ETSI TS 102 176-1 V2.1.1 (maggio 2011), nessun attacco pratico noto, "
            "vincolo < 2014-08-01); SHA-1 (idem, 1 anno, non raccomandato da ETSI TS 102 176-1 V2.1.1, "
            "attacco pratico noto febbraio 2017, vincolo < 2012-08-01); SHA-224 (ultima raccomandazione ETSI "
            "TS 119 312 V1.5.1, Legacy, non raccomandato da ETSI TS 119 312 V2.1.1 (2026-06, il presente "
            "documento), nessun attacco pratico noto, vincolo < 2026-01-01); WHIRLPOOL (ultima "
            "raccomandazione ETSI TS 102 176-1 V2.1.1 (2011-07), 6 anni, non raccomandato da ETSI TS 119 312 "
            "V1.1.1 (2014-11), nessun attacco pratico noto, vincolo < 2020-12-01). Tabella D.2 (combinazioni "
            "algoritmo/dimensione di chiave dismesse): DSA 1 024 bit (1 anno, non raccomandato da ETSI TS 119 "
            "312 V1.1.1, vincolo < 2015-12-01); RSA 786 bit (3 anni, attacco pratico agosto 2010, vincolo < "
            "2010-08-01); RSA 1 024 bit (1 anno, vincolo < 2019-10-01); RSA 1 536 bit (1 anno, non "
            "raccomandato da ETSI TS 119 312 V1.2.2, vincolo < 2019-10-01); RSA < 3 000 bit (Legacy, non "
            "raccomandato da ETSI TS 119 312 V2.1.1, vincolo < 2026-01-01); ECDSA 163 bit (1 anno, vincolo < "
            "2012-08-01); ECDSA 224 bit (3 anni, non raccomandato da ETSI TS 119 312 V1.2.2, vincolo < "
            "2021-10-01); EC-SDSA-opt (tutte le dimensioni, N/A, rimosso per mancanza di supporto nelle "
            "librerie diffuse e non per debolezza crittografica, vincolo < 2026-06-01). Tabella D.3 (suite "
            "dismesse, casi speciali): RSASSA-PSS with mgf1SHA-1Identifier, 1 536 bit (1 anno, non "
            "raccomandato da ETSI TS 119 312 V1.2.2, nessun attacco pratico noto, vincolo < 2019-10-01). "
            "Criteri e vincoli dichiarativi: nessun obbligo a carico di un soggetto."
        ),
        "testo_integrale": (
            """This annex lists algorithms that are not recommended anymore, not even with "legacy" status, and that were listed as recommended in earlier versions of the present document. The information provided here may be used as a basis for cryptographic constraints as specified by ETSI TS 119 172-1 [i.22], clause A.4.2.1, Table A.2 row p, for the purpose of validating electronic signatures in the past, typically based on proof-of-existence information (e.g. time-stamps), as for example specified in ETSI EN 319 102-1 [i.20], clause 5.

One way to determine an expiration date for a given algorithm, or combination of algorithm and key size, is to take into consideration:

1) the date of any known practical attack;

2) the publication date of the last specification recommending the algorithm, or combination of algorithm and key size;

3) the number of years of resistance stated by that specification; and

4) the publication date of the subsequent specification where it stopped being recommended;

as given in the tables below.

Note that the resistance periods listed in earlier versions of the present document have commonly been interpreted as relative to the date of signature creation or to the issuance of a certificate for a key, instead of relative to the publication date of the version of the present document containing the recommendation. The actual usage period therefore potentially extends beyond the date when the algorithm or key length stopped being recommended in a subsequent version of the present document. For example, RSA with 1 536 bits stopped being recommended in 2018-09, but a certificate for a 1536-bits RSA key may conceivably have been issued shortly before, with a validity period of 1 year in accordance with the previous recommendation, thus only ending a year later in 2019-09.

In tables D.1 to D.3, the last column indicates cryptographic constraints that can be used by default, in the absence of diverging application-specific interoperability or security considerations. The constraints are derived from a lenient interpretation of the resistance periods, unless overturned by the publication of a practical attack.

Table D.1: Discontinued cryptographic hash functions

| Hash function | Last listed as recommended in | Resistance (a) | Not recommended since | First known practical attack | Suggested cryptographic constraint |
|---|---|---|---|---|---|
| RIPEMD160 | ETSI TS 102 176-1 V2.0.0 (2007-11) | 3 years | ETSI TS 102 176-1 V2.1.1 (2011-07) | none [i.23] | < 2014-08-01 |
| SHA-1 | ETSI TS 102 176-1 V2.0.0 (2007-11) | 1 year (b) | ETSI TS 102 176-1 V2.1.1 (2011-07) | February 2017 [i.24] | < 2012-08-01 |
| SHA-224 | ETSI TS 119 312 V1.5.1 | Legacy (d) | ETSI TS 119 312 V2.1.1 (2026-06) (the present document) | none | < 2026-01-01 |
| WHIRLPOOL | ETSI TS 102 176-1 V2.1.1 (2011-07) | 6 years (c) | ETSI TS 119 312 V1.1.1 (2014-11) | none | < 2020-12-01 |

(a) As last stated by the specification in the preceding column.
(b) Resistance for 3 years was listed as "unknown", and 6 years as "unusable".
(c) Resistance for up to 10 years was speculatively listed as "usable".
(d) Insufficient security margin against quantum attacks and low performance advantage over SHA-256.

Table D.2: Discontinued signature algorithm and key size combinations

| Algorithm | Key size | Last listed as recommended in | Resistance (a) | Not recommended since | First known practical attack | Suggested cryptographic constraint |
|---|---|---|---|---|---|---|
| DSA | 1 024 bits | ETSI TS 102 176-1 V2.1.1 (2011-07) | 1 year | ETSI TS 119 312 V1.1.1 (2014-11) | none | < 2015-12-01 |
| RSA (b) | 786 bits | ETSI TS 102 176-1 V1.2.1 (2005-07) | 3 years | ETSI TS 102 176-1 V2.0.0 (2007-11) | August 2010 [i.25] | < 2010-08-01 |
| RSA (b) | 1 024 bits | ETSI TS 102 176-1 V2.0.0 (2007-11) | 1 year (c) | ETSI TS 102 176-1 V2.1.1 (2011-07) | none | < 2019-10-01 (c) |
| RSA (b) | 1 536 bits | ETSI TS 119 312 V1.1.1 (2014-11) | 1 year | ETSI TS 119 312 V1.2.2 (2018-09) | none | < 2019-10-01 |
| RSA (b) | < 3 000 bits | ETSI TS 119 312 V1.5.1 (2024-12) | Legacy | ETSI TS 119 312 V2.1.1 | none | < 2026-01-01 |
| ECDSA | 163 bits | ETSI TS 102 176-1 V2.0.0 (2007-11) | 1 year | ETSI TS 102 176-1 V2.1.1 (2011-07) | none | < 2012-08-01 |
| ECDSA | 224 bits | ETSI TS 119 312 V1.1.1 (2014-11) | 3 years | ETSI TS 119 312 V1.2.2 (2018-09) | none | < 2021-10-01 |
| EC-SDSA-opt | all | ETSI TS 119 312 V1.5.1 (2024-12) | N/A (d) | ETSI TS 119 312 V2.1.1 | none | < 2026-06-01 |

(a) As last stated by the specification in the preceding column.
(b) Regardless of padding scheme, i.e. for both PKCS#1-v1.5 and PSS.
(c) RSA with 1 024 bits was still stated as being secure for up to 1 year in ETSI TS 102 176-1 V2.1.1 (2011-07), clause 9.3, note 2 and ETSI TS 119 312 V1.1.1 (2014-11) clause 9.3, note 5. This statement was removed with ETSI TS 119 312 V1.2.2 (2018-09).
(d) Removed due to lack of support in widely deployed libraries (interoperability issues), not due to cryptographic weakness.

Certain signature suites (i.e. combinations of hash algorithms and signature algorithms) had recommendations that did not match the combined minimum of the separate individual recommendations for the hash algorithm and signature algorithm. Such special-case recommendations are listed in Table D.3.

Table D.3: Discontinued signature suites (special cases)

| Signature suite | Key size | Last listed as recommended in | Resistance (a) | Not recommended since | First known practical attack | Suggested cryptographic constraint |
|---|---|---|---|---|---|---|
| RSASSA-PSS with mgf1SHA-1Identifier | 1 536 bits | ETSI TS 119 312 V1.1.1 (2014-11) | 1 year | ETSI TS 119 312 V1.2.2 (2018-09) | none | < 2019-10-01 |

(a) As last stated by the specification in the preceding column."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 9.1 (General notes)",
    "clausola 9.2 (Time period resistance for hash functions)",
    "clausola 9.3 (Time period resistance for signer's key)",
    "clausola 9.4 (Time period resistance for trust anchors)",
    "clausola 9.5 (Time period resistance for other keys)",
    "clausola 10.1 (General)",
    "clausola 10.2.1 (Introduction)",
    "clausola 10.2.2 (Hash functions)",
    "clausola 10.2.3 (Elliptic curves)",
    "clausola 10.2.4 (Signature algorithms)",
    "clausola 10.2.5 (Signature suites)",
    "clausola 10.3.1 (Hash functions)",
    "clausola 10.3.2 (Signature algorithms)",
    "clausola 10.3.3 (Signature suites)",
    "Annex A.1 (Introduction)",
    "Annex A.2 (CAdES and PAdES)",
    "Annex A.3 (XAdES)",
    "Annex A.4 (Signer's certificates)",
    "Annex A.5 (CRLs)",
    "Annex A.6 (OCSP responses)",
    "Annex A.7 (CA certificates)",
    "Annex A.8 (Self-signed certificates for CA issuing CA certificates)",
    "Annex A.9 (TSTs based on IETF RFC 3161)",
    "Annex A.10 (TSU certificates)",
    "Annex A.11 (Self-signed certificates for CAs issuing TSU certificates)",
    "Annex B (Signature maintenance)",
    "Annex C.1 (JSON file location)",
    "Annex C.2 (XML file location)",
    "Annex D (Discontinued algorithms)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
