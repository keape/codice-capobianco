"""ETSI EN 319 422 V1.1.1 (2016-03) - Fase 6 (ADR-0009): capitolo virtuale
per le relazioni cross-fonte.

RIGHE_OBBLIGHI/RIGHE_PRINCIPI/INDICE_ARTICOLI_LOCALE/MAPPATURA_LOCALE vuoti:
questo modulo non contribuisce nodi, solo archi `RELAZIONI`. Ogni arco ha
`nodo_da` a fonte implicita (None -> la fonte corrente, 19) e `nodo_a` a
fonte esplicita (l'intero e' il `fonte_id` della fonte controparte gia'
inserita dalle chiamate precedenti di `seed.py`).

Pipeline di generazione (ADR-0009, eseguita nella sessione principale il
2026-09-24, dopo il seed dei 27 nodi di questa fonte):
  1. Candidati a zero token LLM su `app/.source_cache/etsi_319_422/raw.txt`:
     grep per citazioni esplicite di altre fonti (trovate: eIDAS Reg.
     910/2014, ETSI EN 319 412-2/-3, ETSI EN 319 421) + KNN sull'indice
     vettoriale HNSW (`idxEmbeddingObbligo`/`idxEmbeddingPrincipio`,
     soglia 0.80, top_k 8) -> 83 coppie KNN + 4 coppie da citazione
     esplicita risolte a mano sul `riferimento` esatto = 87 coppie.
  2. Classificazione LLM (`completion()` in batch da 10, in parallelo con
     `wait()`, mai subagent) sullo shortlist, con tassonomia ristretta ai
     tipi rilevanti e prompt esplicitamente conservativo -> 22 proposte.
  3. Validazione: soglia `confidence` >= 0.5, verifica che ogni
     `riferimento` (lato fonte 19 e lato controparte) esista davvero in
     Neo4j -> 22/22 valide, 0 scartate.

Esito: 22 relazioni cross-fonte, tutte con `evidence_type`/`confidence`
per-arco (ADR-0005): 16 "si sovrappone a", 5 "richiama", 1 "attua"; 16
inferred, 6 textual. Per fonte controparte: ETSI EN 319 412 (fonte 7) 6,
ETSI EN 319 421 (fonte 18) 6, ETSI TS 119 431 (fonte 11) 5, Regole Tecniche
AgID certificati qualificati (fonte 15) 2, eIDAS (fonte 1) 1, DPCM 22/2/2013
(fonte 4) 1, ETSI EN 319 401 (fonte 10) 1.

Le citazioni a standard non censiti nel grafo (IETF RFC 3161/5816/3739/6838/
7230-7235/2818, ETSI TS 119 312, ETSI EN 319 102-1, ETSI TS 101 861) non
producono relazioni per assenza di nodo controparte.
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "clausola 9.1 (Regulation compliance statement)"),
        "nodo_a": ("obbligo", 1, "art. 42 §1"),
        "tipo_relazione": "attua",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        "nodo_da": ("principio", None, "clausola 3.1 (Definitions)"),
        "nodo_a": ("principio", 4, "art. 1 c.1 lett.i)"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.1 (General requirements)"),
        "nodo_a": ("principio", 7, "Parte 2: clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.1 (General requirements)"),
        "nodo_a": ("principio", 7, "Parte 3: clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.2 (Subject name requirements)"),
        "nodo_a": ("obbligo", 7, "Parte 2: NAT-4.2.4-1"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.2 (Subject name requirements)"),
        "nodo_a": ("obbligo", 7, "Parte 3: LEG-4.2.1-4"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.5 (Algorithm requirements)"),
        "nodo_a": ("obbligo", 7, "Parte 2: GEN-4.2.5-1"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 9.1 (Regulation compliance statement)"),
        "nodo_a": ("obbligo", 7, "Parte 5: QCS-4.1-01"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.5 (Algorithm requirements)"),
        "nodo_a": ("obbligo", 10, "REQ-7.5-05"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 4.2.3 (Algorithms to be supported)"),
        "nodo_a": ("obbligo", 11, "Parte 2: OVR-8.2-02"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 4.2.4 (Key lengths to be supported)"),
        "nodo_a": ("obbligo", 11, "Parte 2: OVR-8.2-02"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.3 (Algorithms to be used)"),
        "nodo_a": ("obbligo", 11, "Parte 2: OVR-8.2-02"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Key lengths requirements)"),
        "nodo_a": ("obbligo", 11, "Parte 2: OVR-8.2-02"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.5 (Algorithm requirements)"),
        "nodo_a": ("obbligo", 11, "Parte 2: OVR-8.2-02"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.1 (General requirements)"),
        "nodo_a": ("obbligo", 15, "par. 4.2 punto 2"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 9.1 (Regulation compliance statement)"),
        "nodo_a": ("obbligo", 15, "par. 4.2 punto 5 lett. f"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A (Structure for the policy field)"),
        "nodo_a": ("obbligo", 18, "OVR-5.2-01"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A (Structure for the policy field)"),
        "nodo_a": ("obbligo", 18, "OVR-5.2-01A"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A (Structure for the policy field)"),
        "nodo_a": ("obbligo", 18, "OVR-5.2-02"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("principio", None, "clausola 3.1 (Definitions)"),
        "nodo_a": ("principio", 18, "clausola 3.1 (Terms)"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Key lengths requirements)"),
        "nodo_a": ("obbligo", 18, "TIS-7.6.2-05"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.65,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.5 (Algorithm requirements)"),
        "nodo_a": ("obbligo", 18, "TIS-7.6.2-05"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.65,
    },
]
