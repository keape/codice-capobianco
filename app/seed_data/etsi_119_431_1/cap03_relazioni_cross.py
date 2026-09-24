"""Relazioni cross-fonte ETSI TS 119 431-1 (fonte_id=11) verso tutte le altre
fonti gia' censite nel grafo (2026-09-22, ADR-0009 - fase 6 obbligatoria).

Modulo "capitolo virtuale" (nessuna riga obbligo/principio propria, solo
RELAZIONI) agganciato in coda alla lista capitoli di ETSI TS 119 431-1
(fonte_id=11) passata a inserisci_capitoli.

Pipeline eseguita nella sessione principale (mai a subagent), 3 stadi:

1. Generazione candidati a zero token LLM: KNN sull'indice vettoriale HNSW
   gia' popolato (idxEmbeddingObbligo/idxEmbeddingPrincipio, soglia 0.80,
   top-8/nodo) dai 159 nodi di questa fonte verso tutti i nodi delle altre 11
   fonti censite (incluso ETSI TS 119 431-2, trattata come fonte autonoma su
   richiesta esplicita dell'utente pur essendo la Parte 2 dello stesso
   deliverable multi-parte) -> 294 coppie candidate. Grep di corroborazione
   sul testo ufficiale grezzo (app/.source_cache/etsi_119_431_1/raw.txt) per
   citazioni esplicite ad altre fonti (eIDAS/eIDAS2, ETSI TS 119 461, ETSI EN
   319 401, ETSI TS 119 431-2): usato per marcare evidence_type "textual"
   quando il nodo_da cita esplicitamente il documento del nodo_a.
2. Classificazione LLM sullo shortlist di 294 coppie (mai sul prodotto
   cartesiano 159 x ~2300 nodi): 25 chiamate completion() dirette in
   parallelo con wait() (batch da 12 coppie), system prompt con tassonomia
   ristretta a specifica/si sovrappone a/attua/richiama/si applica
   a/richiede come precondizione/definisce, output a schema JSON, prompt
   esplicitamente conservativo (omettere piuttosto che inventare).
3. Validazione: filtro confidence >= 0.6 (soglia piu' alta del minimo 0.5
   raccomandato da ADR-0009, per compensare l'assenza di revisione umana
   in questo giro), verifica che ogni riferimento proposto (sia nodo_da sia
   nodo_a) esista realmente in Neo4j (anti-allucinazione - query diretta per
   riferimento/fonte_id, 0 scarti su 90 proposte totali del giro combinato
   fonte 11+fonte 12), deduplica su (nodo_da, nodo_a) tenendo la confidence
   piu' alta in caso di piu' proposte sulla stessa coppia.

Esito per fonte 11: 46 relazioni cross-fonte (si sovrappone a 21, attua 12,
specifica 7, richiede come precondizione 3, richiama 2, definisce 1). Per
fonte target: ETSI TS 119 431-2 (33), ETSI EN 319 401 (7), ETSI TS 119 461
(5, incluse 2 relazioni "specifica" con nodo_da in ETSI TS 119 461 stesso -
QTS-C.2.4-01/02 -> LNK-6.2.2-02A, la fonte 9 specifica un requisito di questa
fonte), eIDAS2 (1). Zero verso CAD/DPCM 22-2-2013/SPID/DPCM 19-10-2021/ETSI
EN 319 412-5/Regolamento (UE) 2025/1566/eIDAS (nessun candidato KNN sopra
soglia con confidence sufficiente dopo classificazione - documento troppo
specifico su gestione chiavi di firma remota per sovrapporsi tematicamente a
quelle fonti). Tutte le relazioni "inferred" (nessuna citazione testuale
abbastanza esplicita da giustificare "textual" con confidence >= 0.7 in
questo giro - il forte overlap concettuale con ETSI TS 119 431-2 e ETSI EN
319 401 e' colto dalla classificazione semantica, non da citazioni dirette
puntuali per articolo/clausola).
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI = [
    {
        'nodo_da': ('principio', 11, 'Parte 1: clausola 1 (Scope)'),
        'nodo_a': ('principio', 11, 'Parte 2: clausola 1 (Scope)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('principio', 11, 'Parte 1: clausola 1 (Scope)'),
        'nodo_a': ('principio', 10, 'clausola 1 (Scope)'),
        'tipo_relazione': 'attua',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('principio', 11, 'Parte 1: clausola 3.1 (Terms)'),
        'nodo_a': ('principio', 11, 'Parte 2: clausola 3.1 (Terms)'),
        'tipo_relazione': 'definisce',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('principio', 11, 'Parte 1: clausola 3.1 (Terms)'),
        'nodo_a': ('principio', 2, 'art. 45 septies §1'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('principio', 11, 'Parte 1: clausola 3.1 (Terms)'),
        'nodo_a': ('principio', 2, 'art. 5 quater §2'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('principio', 11, 'Parte 1: clausola 3.4 (Notations)'),
        'nodo_a': ('principio', 11, 'Parte 2: clausola 3.4 (Notations)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('principio', 11, 'Parte 1: clausola 4.1 (General policy requirements concepts)'),
        'nodo_a': ('principio', 2, 'art. 45 terdecies §2'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('principio', 11, 'Parte 1: clausola 4.1 (General policy requirements concepts)'),
        'nodo_a': ('principio', 11, 'Parte 2: clausola 4.1 (General policy requirements concepts)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('principio', 11, 'Parte 1: clausola 4.3.1 (SSAS practice statement)'),
        'nodo_a': ('principio', 11, 'Parte 2: clausola 4.2.1 (SCASC practice statement)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('principio', 11, 'Parte 1: clausola 4.3.2 (SSAS policy)'),
        'nodo_a': ('principio', 11, 'Parte 2: clausola 4.2.2 (SCASC policy)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('principio', 11, 'Parte 1: clausola 4.3.3 (Terms and conditions)'),
        'nodo_a': ('principio', 11, 'Parte 2: clausola 4.2.3 (Terms and conditions)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('principio', 11, 'Parte 1: clausola 4.3.3 (Terms and conditions)'),
        'nodo_a': ('principio', 10, 'clausola 1 (Scope)'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('principio', 11, 'Parte 1: clausola 5.2 (SP name and identification)'),
        'nodo_a': ('principio', 11, 'Parte 2: clausola 4.2.2 (SCASC policy)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('principio', 11, 'Parte 1: A.1'),
        'nodo_a': ('principio', 10, 'clausola 1 (Scope)'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-5.1-02'),
        'nodo_a': ('obbligo', 10, 'REQ-5-03'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-5.1-03'),
        'nodo_a': ('obbligo', 10, 'REQ-6.1-05'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-5.1-03'),
        'nodo_a': ('obbligo', 10, 'REQ-6.1-03'),
        'tipo_relazione': 'attua',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-6.1-01'),
        'nodo_a': ('obbligo', 10, 'REQ-6.1-05'),
        'tipo_relazione': 'attua',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-6.1-01'),
        'nodo_a': ('obbligo', 10, 'REQ-7.14.3-04'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-6.1-02'),
        'nodo_a': ('obbligo', 1, 'art. 28 §1'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: SIG-6.3.1-12'),
        'nodo_a': ('obbligo', 9, 'COL-8.2.1-02'),
        'tipo_relazione': 'richiede come precondizione',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: SIG-6.3.1-14'),
        'nodo_a': ('obbligo', 9, 'VAL-8.3.1-07'),
        'tipo_relazione': 'richiede come precondizione',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: DEL-6.3.2-01'),
        'nodo_a': ('obbligo', 4, 'art. 3 c.6'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-6.4.5-02'),
        'nodo_a': ('obbligo', 10, 'REQ-7.9.1-01'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-6.4.6-01'),
        'nodo_a': ('obbligo', 10, 'REQ-7.10-07'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-6.5.3-01A'),
        'nodo_a': ('obbligo', 10, 'REQ-7.4.6-01'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-7-01'),
        'nodo_a': ('obbligo', 11, 'Parte 2: OVR-9-03'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-7-03'),
        'nodo_a': ('obbligo', 11, 'Parte 2: OVR-9-03'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-7-04'),
        'nodo_a': ('obbligo', 11, 'Parte 2: OVR-9-04'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-7-05'),
        'nodo_a': ('obbligo', 11, 'Parte 2: OVR-9-05'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-7-06'),
        'nodo_a': ('obbligo', 11, 'Parte 2: OVR-9-06'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-7-06'),
        'nodo_a': ('obbligo', 11, 'Parte 2: OVR-9-07'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-7-07'),
        'nodo_a': ('obbligo', 11, 'Parte 2: OVR-9-07'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-7-08'),
        'nodo_a': ('obbligo', 11, 'Parte 2: OVR-9-08'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-7-09'),
        'nodo_a': ('obbligo', 11, 'Parte 2: OVR-9-09'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-7-10'),
        'nodo_a': ('obbligo', 11, 'Parte 2: OVR-9-10'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: GEN-A.4-01'),
        'nodo_a': ('obbligo', 4, 'art. 7 c.3'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: GEN-A.4-02'),
        'nodo_a': ('obbligo', 2, 'art. 45 §1 (vigente, eIDAS2)'),
        'tipo_relazione': 'attua',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: GEN-A.4-02'),
        'nodo_a': ('obbligo', 2, 'art. 45 quinquies §1'),
        'tipo_relazione': 'attua',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: SIG-A.5-02'),
        'nodo_a': ('obbligo', 2, 'art. 45 §1 (vigente, eIDAS2)'),
        'tipo_relazione': 'attua',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: SIG-A.5-02'),
        'nodo_a': ('obbligo', 2, 'art. 45 quinquies §1'),
        'tipo_relazione': 'attua',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: LNK-A.7-01'),
        'nodo_a': ('obbligo', 9, 'QTS-C.3.4-05'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: LNK-A.7-01'),
        'nodo_a': ('obbligo', 9, 'USE-9.5.1-01'),
        'tipo_relazione': 'richiede come precondizione',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 1: OVR-6.4.2-01'),
        'nodo_a': ('obbligo', 11, 'Parte 2: OVR-6.2-01'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('obbligo', 9, 'QTS-C.2.4-01'),
        'nodo_a': ('obbligo', 11, 'Parte 1: LNK-6.2.2-02A'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', 9, 'QTS-C.2.4-02'),
        'nodo_a': ('obbligo', 11, 'Parte 1: LNK-6.2.2-02A'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
]
