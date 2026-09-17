"""Relazioni cross-fonte CAD -> eIDAS/eIDAS2 (2026-09-16).

Modulo "capitolo virtuale" (nessuna riga obbligo/principio propria, solo
RELAZIONI) nel senso del contratto di app/seed_data/lib.py:inserisci_capitoli,
usato per collegare i 594 nodi CAD gia' importati (cap01-cap07) ai nodi
eIDAS/eIDAS2 gia' presenti nel registro al momento in cui viene processato.

Pipeline di generazione (non ripetere a mano):
1. candidati da citazione testuale esplicita nel testo ufficiale CAD (grep
   su "articolo N ... del regolamento ... 910/2014|eIDAS") + candidati da
   similarita' vettoriale (KNN sull'indice idxEmbeddingObbligo/Principio gia'
   popolato da embed_neo4j.py, soglia score >= 0.80) -- zero token LLM.
2. classificazione LLM in batch da 10 nodi CAD (completion() con schema JSON,
   system prompt con la tassonomia di CONTEXT.md ristretta a
   richiama/si sovrappone a·duplica/recepisce/specifica/attua) sul solo
   shortlist dello stadio 1, non sul prodotto cartesiano CAD x eIDAS.
3. filtro confidence >= 0.5 (le relazioni testuali esplicite hanno tutte
   confidence >= 0.7) e validazione di ogni riferimento contro i nodi reali
   in Neo4j prima di scrivere questo file.
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI = [
    {
        "nodo_da": ("principio", None, 'art. 1 c.1 lett.dd)'),
        "nodo_a": ("principio", 1, 'art. 12 §1'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("principio", None, 'art. 1 c.1 lett.n-ter)'),
        "nodo_a": ("principio", 1, 'art. 43 §2'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ("principio", None, 'art. 1 c.1 lett.v-bis)'),
        "nodo_a": ("principio", 1, 'art. 43 §2'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ("principio", None, 'art. 1 c.1-bis'),
        "nodo_a": ("principio", 2, 'art. 3 (definizioni)'),
        "tipo_relazione": 'recepisce',
        "evidence_type": 'textual',
        "confidence": 0.95,
    },
    {
        "nodo_da": ("principio", None, 'art. 1 c.1-ter'),
        "nodo_a": ("principio", 2, 'art. 44 §1-bis'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 14-bis c.2 lett.i'),
        "nodo_a": ("principio", 1, 'art. 17 §4 (abrogato)'),
        "tipo_relazione": 'recepisce',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 14-bis c.2 lett.i'),
        "nodo_a": ("principio", 1, 'art. 17 §2 (abrogato)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.7,
    },
    {
        "nodo_da": ("principio", None, 'art. 20 c.1-ter'),
        "nodo_a": ("principio", 1, 'art. 25 §2'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("principio", None, 'art. 20 c.5-bis'),
        "nodo_a": ("principio", 2, 'art. 34 §1-bis'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("principio", None, 'art. 24 c.2'),
        "nodo_a": ("principio", 1, 'art. 25 §2'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 24 c.3'),
        "nodo_a": ("obbligo", 1, 'art. 32 §1-§2'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("principio", None, 'art. 24 c.4-bis'),
        "nodo_a": ("principio", 1, 'art. 28 §4'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ("principio", None, 'art. 24 c.4-bis'),
        "nodo_a": ("principio", 1, 'art. 28 §5'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("principio", None, 'art. 24 c.4-ter'),
        "nodo_a": ("principio", 2, 'art. 24 bis §1'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ("principio", None, 'art. 24 c.4-ter'),
        "nodo_a": ("principio", 2, 'art. 24 bis §3'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("principio", None, 'art. 25 c.1'),
        "nodo_a": ("principio", 1, 'art. 25 §2'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ("principio", None, 'art. 28 c.3'),
        "nodo_a": ("principio", 1, 'art. 28 §3'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 28 c.3-bis'),
        "nodo_a": ("obbligo", 1, 'art. 24 §4'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 28 c.4'),
        "nodo_a": ("obbligo", 1, 'art. 24 §4'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 29 c.2'),
        "nodo_a": ("obbligo", 1, 'art. 24 §1 (abrogato, testo originario 2014)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 29 c.2'),
        "nodo_a": ("obbligo", 1, 'art. 24 §2(b)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 29 c.2'),
        "nodo_a": ("obbligo", 1, 'art. 24 §2(c)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 29 c.2'),
        "nodo_a": ("obbligo", 1, 'art. 24 §2(f)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 29 c.2'),
        "nodo_a": ("obbligo", 1, 'art. 24 §2(k)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 29 c.2'),
        "nodo_a": ("obbligo", 1, 'art. 24 §3'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 29 c.2'),
        "nodo_a": ("obbligo", 1, 'art. 24 §4'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 30 c.1'),
        "nodo_a": ("obbligo", 2, 'art. 13 §1 (testo vigente, eIDAS2)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 32 c.2'),
        "nodo_a": ("obbligo", 2, "art. 24 §2(fa) (nuovo, eIDAS2 — successore dell'art. 19§1)"),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 32 c.3 lett.a'),
        "nodo_a": ("obbligo", 1, 'art. 24 §1 (abrogato, testo originario 2014)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 32 c.3 lett.c'),
        "nodo_a": ("obbligo", 1, 'art. 24 §1 (abrogato, testo originario 2014)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 32 c.3 lett.e'),
        "nodo_a": ("obbligo", 1, 'art. 24 §2(d) (abrogato, testo originario 2014)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.65,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 32 c.3 lett.i'),
        "nodo_a": ("obbligo", 1, 'art. 24 §3'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.65,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 32 c.3 lett.j'),
        "nodo_a": ("obbligo", 2, 'art. 24 §2(h) (vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 32 c.3 lett.l'),
        "nodo_a": ("obbligo", 2, 'art. 24 §2(d) (vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 32 c.3 lett.m'),
        "nodo_a": ("obbligo", 1, 'art. 24 §2(f)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 32 c.3 lett.m'),
        "nodo_a": ("obbligo", 1, 'art. 24 §4'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 32 c.4'),
        "nodo_a": ("obbligo", 1, 'art. 24 §1 (abrogato, testo originario 2014)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 32 c.5'),
        "nodo_a": ("obbligo", 1, 'art. 24 §2(f)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 32 c.5'),
        "nodo_a": ("obbligo", 1, 'art. 24 §2(j) (abrogato senza successore, testo originario 2014)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 35 c.1-bis'),
        "nodo_a": ("obbligo", 1, 'art. 29 §1'),
        "tipo_relazione": 'attua',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 35 c.4'),
        "nodo_a": ("obbligo", 1, 'art. 30 §3'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.65,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 35 c.5'),
        "nodo_a": ("obbligo", 1, 'art. 30 §3'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ("principio", None, 'art. 35 c.6'),
        "nodo_a": ("principio", 1, 'art. 30 §1'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ("principio", None, 'art. 35 c.6'),
        "nodo_a": ("principio", 1, 'art. 30 §2'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ("principio", None, 'art. 36 c.3'),
        "nodo_a": ("principio", 1, 'art. 28 §5'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ("principio", None, 'art. 36 c.4'),
        "nodo_a": ("principio", 1, 'art. 28 §5'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 37 c.1'),
        "nodo_a": ("obbligo", 2, 'art. 24 §2(a) (vigente, eIDAS2)'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 37 c.2'),
        "nodo_a": ("obbligo", 1, 'art. 24 §2(a) (abrogato, testo originario 2014)'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 37 c.3'),
        "nodo_a": ("obbligo", 1, 'art. 24 §2(h) (abrogato, testo originario 2014)'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ("obbligo", None, 'art. 51 c.1'),
        "nodo_a": ("obbligo", 2, 'art. 24 §2(e) (vigente, eIDAS2)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ("principio", None, 'art. 64 c.2-duodecies'),
        "nodo_a": ("principio", 1, 'art. 8 §1'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.75,
    },
    {
        "nodo_da": ("principio", None, 'art. 64 c.2-duodecies'),
        "nodo_a": ("principio", 1, 'art. 8 §2'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.75,
    },
    {
        "nodo_da": ("principio", None, 'art. 65 c.2'),
        "nodo_a": ("principio", 1, 'art. 25 §2'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
]
