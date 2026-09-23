"""Relazioni cross-fonte ETSI TS 119 431-2 (fonte_id=12) verso tutte le altre
fonti gia' censite nel grafo (2026-09-22, ADR-0009 - fase 6 obbligatoria).

Modulo "capitolo virtuale" (nessuna riga obbligo/principio propria, solo
RELAZIONI) agganciato in coda alla lista capitoli di ETSI TS 119 431-2
(fonte_id=12) passata a inserisci_capitoli.

Pipeline eseguita nella sessione principale (mai a subagent), stessi 3 stadi
del modulo gemello app/seed_data/etsi_119_431_1/cap03_relazioni_cross.py (si
rimanda al suo docstring per il dettaglio completo della pipeline, eseguita
in un unico giro combinato per le due fonti):

1. KNN (soglia 0.80, top-8/nodo) dai 95 nodi di questa fonte verso tutti i
   nodi delle altre 11 fonti (incluso ETSI TS 119 431-1, trattata come fonte
   autonoma) -> 199 coppie candidate. Grep di corroborazione su
   app/.source_cache/etsi_119_431_2/raw.txt per citazioni esplicite (eIDAS,
   ETSI EN 319 401, ETSI TS 119 431-1).
2. Classificazione LLM su shortlist (17 batch da 12 coppie, completion()
   parallele + wait(), stessa tassonomia/schema/prompt conservativo del
   modulo gemello).
3. Validazione: confidence >= 0.6, verifica esistenza in Neo4j di ogni
   riferimento proposto (0 scarti), deduplica su (nodo_da, nodo_a).

Esito per fonte 12: 44 relazioni cross-fonte (si sovrappone a 34, richiama 4,
attua 2, specifica 4 - incluse 2 relazioni con nodo_da in ETSI EN 319 401
stesso, REQ-6.1-08 -> OVR-9-07 e REQ-7.1.2-03 -> OVR-9-08, la fonte 10
specifica requisiti di questa fonte sul processo di revisione della policy).
Per fonte target: ETSI TS 119 431-1 (33, il piu' alto per affinita'
tematica diretta essendo le due Parti dello stesso deliverable multi-parte),
ETSI EN 319 401 (7, coerente con l'incorporazione esplicita per riferimento
dei requisiti EN 319 401 dichiarata nel testo), ETSI TS 119 461 (2), eIDAS2
(2). Zero verso CAD/DPCM 22-2-2013/SPID/DPCM 19-10-2021/ETSI EN 319 412-5/
Regolamento (UE) 2025/1566/eIDAS (nessun candidato sopra soglia con
confidence sufficiente). Tutte "inferred" (nessuna citazione testuale
abbastanza esplicita da giustificare "textual" in questo giro).
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI = [
    {
        'nodo_da': ('principio', 12, 'clausola 3.3 (Abbreviations)'),
        'nodo_a': ('principio', 11, 'clausola 3.3 (Abbreviations)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('principio', 12, 'clausola 3.4 (Notations)'),
        'nodo_a': ('principio', 11, 'clausola 3.4 (Notations)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('principio', 12, 'clausola 4.1 (General policy requirements concepts)'),
        'nodo_a': ('principio', 11, 'clausola 4.1 (General policy requirements concepts)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('principio', 12, 'clausola 4.2.1 (SCASC practice statement)'),
        'nodo_a': ('principio', 11, 'clausola 4.3.1 (SSAS practice statement)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.65,
    },
    {
        'nodo_da': ('principio', 12, 'clausola 4.2.2 (SCASC policy)'),
        'nodo_a': ('principio', 11, 'clausola 4.3.2 (SSAS policy)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.65,
    },
    {
        'nodo_da': ('principio', 12, 'clausola 4.2.3 (Terms and conditions)'),
        'nodo_a': ('principio', 11, 'clausola 4.3.3 (Terms and conditions)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.65,
    },
    {
        'nodo_da': ('principio', 12, 'clausola 4.3 (Architecture)'),
        'nodo_a': ('principio', 11, 'clausola 4.3.1 (SSAS practice statement)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('principio', 12, 'clausola 4.3 (Architecture)'),
        'nodo_a': ('principio', 11, 'clausola 1 (Scope)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('principio', 12, 'clausola 4.3 (Architecture)'),
        'nodo_a': ('principio', 11, 'clausola 4.4 (SSAS component services)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('principio', 12, 'Annex C'),
        'nodo_a': ('principio', 3, 'art. 20 c.1-bis'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.65,
    },
    {
        'nodo_da': ('principio', 12, 'Annex C'),
        'nodo_a': ('principio', 1, 'art. 27 §4 (abrogato)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-5-01'),
        'nodo_a': ('obbligo', 11, 'OVR-6.4.1-01'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-5-01'),
        'nodo_a': ('obbligo', 11, 'OVR-6.8.4-01'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-5-01'),
        'nodo_a': ('obbligo', 11, 'OVR-6.4.9-01'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-5-01'),
        'nodo_a': ('obbligo', 11, 'OVR-6.4.2-01'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-6.1-01'),
        'nodo_a': ('obbligo', 11, 'OVR-6.8.4-01'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-6.1-01'),
        'nodo_a': ('obbligo', 11, 'OVR-6.4.2-01'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-6.1-01'),
        'nodo_a': ('obbligo', 11, 'OVR-6.4.1-01'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-7.3-01'),
        'nodo_a': ('obbligo', 9, 'OVR-7.3-01'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-7.5-01'),
        'nodo_a': ('obbligo', 9, 'OVR-7.5-01'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-7.8-01'),
        'nodo_a': ('obbligo', 9, 'OVR-7.8-01'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-7.11-02'),
        'nodo_a': ('obbligo', 10, 'REQ-7.6-06'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('obbligo', 12, 'ASI-8.1-02'),
        'nodo_a': ('obbligo', 11, 'LNK-6.2.2-10A'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-8.2-01'),
        'nodo_a': ('obbligo', 10, 'REQ-7.10-02'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-8.2-07'),
        'nodo_a': ('obbligo', 11, 'LNK-6.2.2-02C'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-8.2-08'),
        'nodo_a': ('obbligo', 11, 'SIG-A.6-07'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-03'),
        'nodo_a': ('obbligo', 11, 'OVR-7-03'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.65,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-03'),
        'nodo_a': ('obbligo', 11, 'OVR-7-01'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-04'),
        'nodo_a': ('obbligo', 11, 'OVR-7-04'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-04'),
        'nodo_a': ('obbligo', 10, 'REQ-6.1-06'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-05'),
        'nodo_a': ('obbligo', 11, 'OVR-7-05'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-05'),
        'nodo_a': ('obbligo', 10, 'REQ-4.2-03'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.65,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-05'),
        'nodo_a': ('obbligo', 10, 'REQ-5-02'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-05'),
        'nodo_a': ('obbligo', 10, 'REQ-4.2-01'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-06'),
        'nodo_a': ('obbligo', 11, 'OVR-7-06'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.65,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-06'),
        'nodo_a': ('obbligo', 11, 'OVR-7-07'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-07'),
        'nodo_a': ('obbligo', 11, 'OVR-7-07'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-07'),
        'nodo_a': ('obbligo', 11, 'OVR-7-03'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-08'),
        'nodo_a': ('obbligo', 11, 'OVR-7-08'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.65,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-08'),
        'nodo_a': ('obbligo', 11, 'OVR-7-09'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-09'),
        'nodo_a': ('obbligo', 11, 'OVR-7-09'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 12, 'OVR-9-10'),
        'nodo_a': ('obbligo', 11, 'OVR-7-10'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 10, 'REQ-6.1-08'),
        'nodo_a': ('obbligo', 12, 'OVR-9-07'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 10, 'REQ-7.1.2-03'),
        'nodo_a': ('obbligo', 12, 'OVR-9-08'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
]
