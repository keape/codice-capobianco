"""Relazioni cross-fonte ETSI EN 319 401 V3.2.1 (fonte_id=10) -> eIDAS/eIDAS2/
Reg. UE 2025/1566/ETSI TS 119 461, e viceversa (2026-09-22).

Modulo "capitolo virtuale" (nessuna riga obbligo/principio propria, solo RELAZIONI) nel
senso del contratto di app/seed_data/lib.py:inserisci_capitoli, agganciato in coda alla
lista capitoli di ETSI EN 319 401 (fonte_id=10) passata a inserisci_capitoli (Fase 6,
ADR-0009).

Pipeline eseguita nella sessione principale (nessun subagent), in 3 stadi:

1. Candidati a zero token LLM:
   - grep testuale sul testo ufficiale grezzo ETSI EN 319 401
     (app/.source_cache/etsi_319_401/raw.txt) per citazioni esplicite di altre fonti gia'
     censite: nessuna citazione diretta di CAD/DPCM/SPID/DPCM 19-10-2021/ETSI 319 412-5 nel
     testo ufficiale. Citazioni esplicite puntuali trovate verso eIDAS/eIDAS2 (art. 13,
     15, 19-bis, 20, 24) sia nel corpo dei requisiti (es. REQ-7.1.2-04 cita art. 13; REQ-
     7.9.2-02 cita art. 19a e art. 24(2)(fb)) sia nell'Annex B (informativo, "Mapping ETSI
     EN 319 401 requirements with eIDAS Regulation") - tabella ufficiale di corrispondenza
     articolo eIDAS <-> REQ-x.y-nn di questo standard, usata come fonte primaria ad alta
     confidenza per le citazioni piu' puntuali (13 relazioni "textual"). Un riferimento
     della tabella ("REQ-7.1.1-04") risultava disallineato dalla numerazione corrente del
     testo (corretto in REQ-7.1.2-04, verificato contro il nodo realmente esistente);
     riferimenti generici a intere clausole ("Clause 7.2", "Clause 6.2", "Clause 7.12" senza
     REQ puntuale) scartati per assenza di un nodo target univoco. Annex A (DORA) e Annex C
     (Reg. 2024/2690, NIS2) non hanno fonte corrispondente nel censimento - non usati.
   - KNN sull'indice vettoriale HNSW gia' popolato (idxEmbeddingObbligo/idxEmbeddingPrincipio,
     soglia 0.80, top 8 per indice per nodo, poi top 3 per nodo sorgente): 210 dei 326 nodi
     ETSI 319 401 con almeno un candidato sopra soglia, 525 coppie grezze.
2. Classificazione LLM sullo shortlist (mai sul prodotto cartesiano 326 x ~2500 nodi delle
   altre 9 fonti): 21 batch da 10 coppie, chiamate completion() dirette in parallelo con
   wait(), system prompt con tassonomia CONTEXT.md ristretta ai tipi rilevanti per una fonte
   tecnica generale (attua, specifica, si sovrappone a, richiama, si applica a), output a
   schema JSON, prompt esplicitamente conservativo (omettere piuttosto che inventare) ->
   11 relazioni proposte (rendimento basso, ~2%: atteso per un documento di controlli di
   sicurezza generici, semanticamente distante dal linguaggio degli articoli di legge delle
   altre fonti salvo i pochi punti di sovrapposizione tematica diretta).
3. Validazione: tutte le 11 proposte LLM verificate contro lo shortlist realmente
   sottoposto al batch (anti-allucinazione, nessuno scarto necessario) e confidence >= 0.5
   (nessuno scarto). Deduplica non necessaria (nessuna coppia ripetuta tra stadi). Totale:
   15 relazioni "textual" (Annex B + autocitazioni puntuali) + 11 relazioni "inferred"
   (classificazione LLM) = 26 relazioni cross-fonte. Per tipo: specifica (13), si sovrappone
   a (6), richiama (4), attua (3). Per fonte target: eIDAS2 (15), ETSI TS 119 461 (6), eIDAS
   (4), Reg. UE 2025/1566 (1). Zero verso CAD/DPCM/SPID/DPCM 19-10-2021/ETSI 319 412-5 (nessun
   candidato sopra soglia KNN ne' citazione esplicita nel testo ufficiale verso quelle fonti).
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI = [
    {
        "nodo_da": ('obbligo', 10, 'REQ-6.2-02'),
        "nodo_a": ('obbligo', 1, 'art. 13 §2'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.13-03'),
        "nodo_a": ('obbligo', 2, 'art. 15 (testo vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.13-04'),
        "nodo_a": ('obbligo', 2, 'art. 15 (testo vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-6.3-04'),
        "nodo_a": ('obbligo', 2, 'art. 24 §2(a) (vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.1.2-04'),
        "nodo_a": ('obbligo', 1, 'art. 24 §2(c)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.1.2-04'),
        "nodo_a": ('obbligo', 2, 'art. 13 §1 (testo vigente, eIDAS2)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.6,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.8-21'),
        "nodo_a": ('obbligo', 2, 'art. 24 §2(e) (vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.8-21'),
        "nodo_a": ('obbligo', 1, 'art. 24 §2(f)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.8,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.8-21'),
        "nodo_a": ('obbligo', 2, 'art. 24 §2(g) (vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.8,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.8-22'),
        "nodo_a": ('obbligo', 2, 'art. 24 §2(e) (vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.8-22'),
        "nodo_a": ('obbligo', 1, 'art. 24 §2(f)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.8,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.8-22'),
        "nodo_a": ('obbligo', 2, 'art. 24 §2(g) (vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.8,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.3.3-02'),
        "nodo_a": ('obbligo', 2, 'art. 24 §2(h) (vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.9.2-02'),
        "nodo_a": ('obbligo', 2, 'art. 19-bis §1(a) (nuovo, eIDAS2)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.7,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.9.2-02'),
        "nodo_a": ('obbligo', 2, "art. 24 §2(fb) (nuovo, eIDAS2 — successore dell'art. 19§2)"),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.7,
    },
    {
        "nodo_da": ('principio', 10, 'clausola 1 (Scope)'),
        "nodo_a": ('principio', 9, 'clausola 1 (Scope)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ('principio', 10, 'clausola 1 (Scope)'),
        "nodo_a": ('principio', 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.8,
    },
    {
        "nodo_da": ('principio', 10, 'clausola 3.1 (Terms)'),
        "nodo_a": ('principio', 9, 'clausola 3.3 (Abbreviations)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ('principio', 10, 'clausola 3.3 (Abbreviations)'),
        "nodo_a": ('principio', 9, 'clausola 3.3 (Abbreviations)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ('principio', 10, 'clausola 3.4 (Notation)'),
        "nodo_a": ('principio', 9, 'clausola 3.4 (Notations)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.7,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-5-01'),
        "nodo_a": ('principio', 2, 'art. 46 bis §4'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.8-11'),
        "nodo_a": ('obbligo', 9, 'VAL-8.3.6-01'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.9.2-02'),
        "nodo_a": ('principio', 2, 'art. 46 bis §4'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.65,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.9.3-01'),
        "nodo_a": ('principio', 2, 'art. 21 §2 (vigente, eIDAS2)'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.9.3-02'),
        "nodo_a": ('obbligo', 2, "art. 24 §2(fb) (nuovo, eIDAS2 — successore dell'art. 19§2)"),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ('obbligo', 10, 'REQ-7.10-02'),
        "nodo_a": ('obbligo', 9, 'ISS-8.5.2-06'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
]
