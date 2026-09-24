"""Regole Tecniche e Raccomandazioni AgID 13/2/2020 (fonte_id=15) - capitolo
virtuale di collegamento cross-fonte (ADR-0009), fase 6 obbligatoria.

Pipeline eseguita nella sessione principale (mai a subagent), 2026-09-23:

1) Generazione candidati a zero token LLM:
   - Grep sul testo ufficiale grezzo (app/.source_cache/agid_reg_tec_cert_qual/raw.txt)
     per citazioni esplicite ad altre fonti censite: "82/2005"/CAD (1 occorrenza,
     nella definizione di «CAD» e nella base giuridica "ai sensi dell'articolo 71
     del CAD"), "910/2014"/eIDAS (15 occorrenze, artt. 21, 24, 27, 32, 37, 40, 42
     e allegati I/III/IV), "319-412"/ETSI (11 occorrenze, ma tutte a EN 319-412-1/
     -2/-3/-4 - parti diverse dall'unica parte censita in questo grafo, EN
     319-412-5/QCStatements, fonte_id=7 - nessuna citazione testuale diretta alla
     parte -5). Zero occorrenze di "22 febbraio 2013"/"24 ottobre 2014"/"19
     ottobre 2021"/"2025/1566"/"119 461"/"319-401"/"119 431"/"modalità
     attuative"/"2015/1502"/"319-422" (quest'ultimo citato ma è lo standard sulle
     marche temporali, non uno standard censito in questo grafo).
   - KNN sull'indice vettoriale HNSW (idxEmbeddingObbligo/idxEmbeddingPrincipio,
     soglia 0.80) dai 49 nodi di questa fonte verso tutti i nodi delle altre 14
     Fonti: 407 coppie candidate, ridotte alla shortlist di 300 coppie (top 8 per
     nodo di partenza, 44 dei 49 nodi con almeno un candidato).

2) Classificazione LLM sulla shortlist di 300 coppie (non sul prodotto
   cartesiano 49x2543), 44 chiamate completion() dirette in parallelo (una per
   nodo di partenza con candidati), system prompt con tassonomia ristretta a
   attua/specifica/si applica a/richiama/si sovrappone a/definisce, regole
   esplicite anti-generalizzazione (niente relazioni per sovrapposizione
   lessicale generica su termini comuni come "certificato qualificato"/"QTSP"/
   "sicurezza"; per aspetti tecnici molto specifici la relazione è valida solo
   se il nodo di partenza tratta ESATTAMENTE lo stesso aspetto tecnico
   specifico), output a schema JSON. Esito grezzo: 37 proposte.

3) Validazione critica (lettura diretta di ogni testo target proposto, non solo
   filtro per soglia di confidence):
   - 3 proposte per il nodo "art. 1, def. «Agenzia»" verso le identiche
     definizioni di "Agenzia"/"AgID" in DPCM 24/10/2014 SPID (fonte_id=5, "art.
     1 c.1 lett.a)", testo verbatim identico), DPCM 22/2/2013 (fonte_id=4, "art.
     1 c.1 lett.c)", quasi identico) e CAD (fonte_id=3, "art. 1 c.1 lett.0a)",
     stesso ente) confermate: duplicazione genuina della stessa definizione
     legislativa in più fonti, tipo corretto "si sovrappone a" (non "definisce":
     nessuna delle due parti manca di una propria definizione autonoma),
     evidence_type "textual" per verbatim quasi identico.
   - "art. 1, def. «CAD»" -> proposta verso CAD "art. 1 c.1" (clausola generica
     di rinvio alle definizioni del CAD) scartata come ridondante rispetto alla
     proposta più specifica verso DPCM 22/2/2013 "art. 1 c.1 lett.a)" (che
     definisce esplicitamente «Codice» = CAD, stesso referente, testo
     verificato) - mantenuta solo quest'ultima, "si sovrappone a", textual.
   - "art. 1, def. «regolamento eIDAS»" -> proposta "definisce" verso eIDAS
     "art. 1" riclassificata "richiama" (il nostro nodo non definisce il
     contenuto dell'art. 1 eIDAS, identifica solo l'atto citandolo per
     nome/data/numero); la proposta duplicata verso eIDAS2 "art. 1" (fonte_id=2)
     scartata come anacronistica (il documento AgID è del 2020, precedente a
     eIDAS2/2024, e cita esplicitamente "Regolamento (UE) n.910/2014" senza
     menzionare eIDAS2); la proposta verso ETSI TS 119 461 clausola 3.1 (Terms)
     scartata per sovrapposizione lessicale generica su un glossario ampio
     (violazione regola 1).
   - "par. 2 §1" (Principio, scopo del provvedimento che cita art. 32 e,
     mutatis mutandis, art. 40 eIDAS) -> le proposte verso eIDAS2 "art. 32 §1
     (presunzione)" e "art. 40-bis" sostituite, dopo lettura del testo target,
     con i nodi eIDAS (fonte_id=1, non eIDAS2) effettivamente citati nel 2020:
     "art. 32 §1-§2" e "art. 40" (nodi non toccati da eIDAS2, quindi ancora i
     riferimenti corretti per un documento del 2020), tipo "richiama" (citazione
     esplicita per nome di articolo, non specificazione del contenuto); la
     proposta verso DPCM 22/2/2013 "art. 2 c.1" (clausola di scopo del DPCM
     stesso) scartata per sovrapposizione generica (entrambe le fonti hanno una
     propria clausola di scopo, nessun aggancio specifico tra i due contenuti).
   - "par. 3.1 §1" (adeguatezza di hash/algoritmi crittografici) -> proposta
     verso DPCM 22/2/2013 "art. 19 c.5" (periodo di validità dei certificati in
     base alla robustezza delle chiavi) scartata: stesso tema generale (robustezza
     crittografica) ma aspetto tecnico specifico diverso (scelta di
     algoritmi/hash adeguati vs durata di validità del certificato) - violazione
     regola 2.
   - "par. 3.2" (informativa su applicazione/disapplicazione raccomandazioni) ->
     confermata verso ETSI EN 319 401 REQ-6.2-03 (fonte_id=10, dovere di
     informativa chiara e completa ai subscriber/relying party prima del
     rapporto contrattuale): stesso specifico dovere di trasparenza
     pre-contrattuale, "si sovrappone a", inferred.
   - "par. 4 (intro)" -> entrambe le proposte (ETSI EN 319 401 REQ-6.3-02,
     comunicazione di modifiche alla politica di sicurezza; DPCM 22/2/2013 art.
     43 c.2, elenco pubblico dei certificatori) scartate: aspetti tecnici
     specifici diversi dalla dichiarazione di impegno alle raccomandazioni
     (violazione regola 2).
   - "par. 4.1 punto 9" (ulteriori estensioni non marcate critiche) -> confermata
     verso ETSI EN 319 412-5 QCS-4.1-02 (fonte_id=7, "l'estensione qcStatements
     non deve essere marcata come critica"): stesso specifico requisito tecnico
     (non-criticità dell'estensione), pur applicato dal nostro nodo a "ulteriori
     estensioni" in generale e da QCS-4.1-02 a una estensione specifica -
     sovrapposizione concettuale genuina, "si sovrappone a", inferred,
     confidence ridotta a 0.65 per la generalità del nostro nodo. La proposta
     duplicata dal nodo "par. 4.2 punto 4 lett. e" (stesso requisito, ma
     riferito ai certificati di certificazione, non ai certificati qualificati -
     contesto meno pertinente a QCS-4.1-02, specifico dei certificati
     qualificati) scartata come ridondante e meno precisa. Le proposte verso
     QCS-4.1-01 (conformità RFC 3739 del campo qcStatements, aspetto tecnico
     diverso: formato vs criticità) scartate per violazione regola 2.
   - "par. 4.2 punto 1" (profilo dei certificati di certificazione conforme RFC
     5280) -> proposte verso QCS-4.1-01 (formato qcStatements, RFC 3739 - tipo
     di certificato e standard diversi: certificati di certificazione vs
     certificati qualificati) e verso eIDAS "art. 28 §1" (allegato I, requisiti
     dei certificati di firma - non i certificati di certificazione/CA)
     scartate per mismatch del tipo di certificato (violazione regola 2).
   - "par. 4.2 punto 5 lett. a/b/d/e" (estensioni X.509 dei certificati di
     marcatura temporale: keyUsage/extendedKeyUsage/authorityKeyIdentifier/
     subjectKeyIdentifier) -> tutte e 4 le proposte verso DPCM 22/2/2013 "art.
     50 c.2" (contenuto: identificativo del sistema di marcatura temporale, un
     campo diverso dalle estensioni X.509 citate) scartate: stesso tipo di
     certificato (marcatura temporale) ma aspetto tecnico specifico diverso in
     tutti e 4 i casi (violazione regola 2 - pattern di generalizzazione
     strutturale analogo a quello già osservato nell'import del Reg. (UE)
     2015/1502, dove lo stesso nodo target veniva proposto per piu' nodi di
     partenza distinti sulla base di una sovrapposizione lessicale generica sul
     tipo di certificato, non sul contenuto specifico).
   - "par. 4.3" (formati di firme/sigilli, rinvio a Decisione UE 1506/2015) ->
     proposta verso ETSI TS 119 431-1 OVR-A.3-02 (certificazione del QSCD nella
     practice statement) scartata: argomento diverso (formati di firma vs
     certificazione del dispositivo), violazione regola 1/2.
   - "par. 4.4 §1" (OCSP/CRLDistributionPoints, configurazione tecnica delle
     estensioni) -> tutte e 3 le proposte verso DPCM 22/2/2013 (art. 26 c.1
     sospensione via CRL, art. 22 c.1 revoca via CRL, art. 4 c.2 elenco
     generico di materie rinviate alle regole AgID) scartate: il nostro nodo
     riguarda la configurazione tecnica delle estensioni certificate (OCSP/
     CRLDistributionPoints), i nodi target riguardano l'atto sostanziale di
     sospensione/revoca o un rinvio generico - aspetto tecnico specifico
     diverso in tutti i casi.
   - "par. 4.4 §3" (informazioni su revoca/sospensione liberamente accessibili
     in rete) -> confermata verso DPCM 22/2/2013 "art. 34 c.1" ("le liste dei
     certificati revocati e sospesi devono essere rese pubbliche"): stesso
     specifico requisito sostanziale di accessibilità pubblica delle
     informazioni di stato, "si sovrappone a", evidence_type "textual" per
     quasi-identità sostanziale; confermata anche verso eIDAS "art. 24 §4"
     (fonte_id=1: "il prestatore qualificato... trasmette alle parti facenti
     affidamento informazioni sull'esistenza [del certificato]"), "attua",
     textual, confidence alta. Scartate le proposte verso DPCM art. 34 c.1
     duplicate su altri nodi, verso CAD "art. 6-quinquies c.1" (elenchi
     PEC/domicili digitali, concetto di "elenco" non pertinente alle liste di
     revoca) per mismatch semantico (falso positivo da omonimia "elenco/lista").
   - "par. 5, comma 1" (condizioni di conferma della validità in sede di
     convalida, art. 32 eIDAS) -> confermata verso eIDAS "art. 32 §1-§2"
     (fonte_id=1, citazione esplicita "articolo 32 del regolamento eIDAS" nel
     testo ufficiale), "attua", textual, confidence 0.95; confermata (una sola
     delle due proposte quasi-duplicate) verso ETSI TS 119 461 QTS-C.3.3-06
     ("la firma deve essere convalidata secondo la convalida della firma
     eIDAS"): stesso specifico rinvio al processo di convalida eIDAS, "si
     sovrappone a", inferred; scartata la proposta duplicata QTS-C.2.3-05
     (testo sostanzialmente identico, stesso concetto) e la proposta verso
     eIDAS2 "art. 32-bis §1-§2" (firme AVANZATE, non QUALIFICATE - tipo di
     firma diverso, violazione regola 2).
   - "par. 5, comma 2" (raccomandazione sulla verifica delle marche detached e
     dei formati RFC 5544) -> confermata verso DPCM 22/2/2013 "art. 46 c.1"
     (obbligo dei certificatori accreditati di fornire un sistema per
     verificare le marche temporali): sovrapposizione funzionale genuina sulla
     capacità di verifica delle marche temporali, "si sovrappone a", inferred,
     confidence contenuta (0.55) per la genericità del collegamento.
   - Ricerca testuale mirata aggiuntiva (non generata dal prefiltro KNN, letta
     manualmente dal testo ufficiale): la base giuridica esplicita del
     provvedimento, "il presente provvedimento, emanato ai sensi dell'articolo
     71 del CAD" (nodo "par. 2 §3", cap01.py), collegata con "richiama" verso
     CAD "art. 71 c.1" (fonte_id=3, Obbligo); le citazioni letterali di
     articolo/paragrafo/lettera del capitolo 3 (Obblighi) collegate con "attua"
     verso i nodi eIDAS2 vigenti corrispondenti (fonte_id=2: "art. 24 §2(e)"
     per par. 3.1 §1, "art. 21 §2" e "art. 24 §2(a)" per par. 3.1 §2, "art. 24
     §2(d)" per par. 3.2) - collegate alla versione vigente eIDAS2 anziché al
     testo originario 2014 (alcune lettere dell'art. 24 §2 sono state
     riformulate da eIDAS2, verificato dal marcatore "(vigente, eIDAS2)" sui
     nodi target) perché il provvedimento AgID, pur emanato nel 2020, resta
     tuttora vigente e va letto oggi insieme al testo eIDAS attualmente in
     vigore.

Esito finale fase 6: 19 relazioni cross-fonte (4 verso eIDAS2/fonte_id=2
"attua", citazione testuale esplicita di articolo/paragrafo/lettera; 1 verso
CAD/fonte_id=3 "richiama"; 3 verso definizioni duplicate di "Agenzia"/"AgID"
in DPCM 24/10/2014 SPID/fonte_id=5, DPCM 22/2/2013/fonte_id=4, CAD/fonte_id=3
"si sovrappone a"; 1 verso "Codice"=CAD in DPCM 22/2/2013/fonte_id=4 "si
sovrappone a"; 1 verso eIDAS/fonte_id=1 "richiama" per l'identificazione
dell'atto citato; 2 verso eIDAS/fonte_id=1 "richiama" per gli artt. 32/40
citati nello scopo del provvedimento; 3 verso eIDAS/fonte_id=1 "attua"/"si
sovrappone a" per la convalida (art. 32, art. 24 §4) e l'informativa sullo
stato dei certificati; 1 verso ETSI EN 319 401/fonte_id=10 "si sovrappone a";
1 verso ETSI EN 319 412-5/fonte_id=7 "si sovrappone a"; 1 verso ETSI TS 119
461/fonte_id=9 "si sovrappone a"; 1 verso DPCM 22/2/2013/fonte_id=4 "si
sovrappone a" per la pubblicità delle liste di revoca/sospensione; 1 verso
DPCM 22/2/2013/fonte_id=4 "si sovrappone a" per la verifica delle marche
temporali); zero verso DPCM 24/10/2014 SPID (oltre alla definizione di
"Agenzia"), DPCM 19/10/2021, Regolamento AgID modalità attuative SPID,
Regolamento (UE) 2025/1566, Regolamento (UE) 2015/1502, ETSI TS 119 431-1
(oltre al falso positivo scartato), ETSI TS 119 431-2 - esito verificato con
la pipeline completa (grep + KNN + classificazione LLM + validazione critica
manuale su ogni testo target), non fase saltata.
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI = [
    # --- citazioni testuali esplicite (capitolo 3, Obblighi ex art.24/21 eIDAS) ---
    {
        "nodo_da": ("obbligo", None, "par. 3.1 §1"),
        "nodo_a": ("obbligo", 2, "art. 24 §2(e) (vigente, eIDAS2)"),
        "tipo_relazione": "attua",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", None, "par. 3.1 §2"),
        "nodo_a": ("principio", 2, "art. 21 §2 (vigente, eIDAS2)"),
        "tipo_relazione": "attua",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", None, "par. 3.1 §2"),
        "nodo_a": ("obbligo", 2, "art. 24 §2(a) (vigente, eIDAS2)"),
        "tipo_relazione": "attua",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", None, "par. 3.2"),
        "nodo_a": ("obbligo", 2, "art. 24 §2(d) (vigente, eIDAS2)"),
        "tipo_relazione": "attua",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    # --- base giuridica ex art. 71 CAD ---
    {
        "nodo_da": ("principio", None, "par. 2 §3"),
        "nodo_a": ("obbligo", 3, "art. 71 c.1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    # --- definizioni duplicate di "Agenzia"/"AgID"/"CAD" in altre fonti nazionali ---
    {
        "nodo_da": ("principio", None, "art. 1, def. «Agenzia»"),
        "nodo_a": ("principio", 5, "art. 1 c.1 lett.a)"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("principio", None, "art. 1, def. «Agenzia»"),
        "nodo_a": ("principio", 4, "art. 1 c.1 lett.c)"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", None, "art. 1, def. «Agenzia»"),
        "nodo_a": ("principio", 3, "art. 1 c.1 lett.0a)"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
    {
        "nodo_da": ("principio", None, "art. 1, def. «CAD»"),
        "nodo_a": ("principio", 4, "art. 1 c.1 lett.a)"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    # --- identificazione/citazione del regolamento eIDAS e dei suoi articoli ---
    {
        "nodo_da": ("principio", None, "art. 1, def. «regolamento eIDAS»"),
        "nodo_a": ("principio", 1, "art. 1 (testo originario 2014)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", None, "par. 2 §1"),
        "nodo_a": ("obbligo", 1, "art. 32 §1-§2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("principio", None, "par. 2 §1"),
        "nodo_a": ("principio", 1, "art. 40"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    # --- convalida (capitolo 5) ---
    {
        "nodo_da": ("obbligo", None, "par. 5, comma 1"),
        "nodo_a": ("obbligo", 1, "art. 32 §1-§2"),
        "tipo_relazione": "attua",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
    {
        "nodo_da": ("obbligo", None, "par. 5, comma 1"),
        "nodo_a": ("obbligo", 9, "QTS-C.3.3-06"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.65,
    },
    {
        "nodo_da": ("obbligo", None, "par. 5, comma 2"),
        "nodo_a": ("obbligo", 4, "art. 46 c.1"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    # --- informativa pre-contrattuale (capitolo 3/4) ---
    {
        "nodo_da": ("obbligo", None, "par. 3.2"),
        "nodo_a": ("obbligo", 10, "REQ-6.2-03"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    # --- estensioni non marcate critiche (capitolo 4.1) ---
    {
        "nodo_da": ("obbligo", None, "par. 4.1 punto 9"),
        "nodo_a": ("obbligo", 7, "Parte 5: QCS-4.1-02"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.65,
    },
    # --- informazioni sullo stato dei certificati (capitolo 4.4) ---
    {
        "nodo_da": ("obbligo", None, "par. 4.4 §3"),
        "nodo_a": ("obbligo", 4, "art. 34 c.1"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", None, "par. 4.4 §3"),
        "nodo_a": ("obbligo", 1, "art. 24 §4"),
        "tipo_relazione": "attua",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
]
