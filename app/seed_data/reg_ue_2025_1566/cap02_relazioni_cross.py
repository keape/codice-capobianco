"""Regolamento di esecuzione (UE) 2025/1566 (fonte_id=8) - capitolo virtuale di
collegamento cross-fonte (ADR-0009), fase 6 obbligatoria.

Pipeline eseguita nella sessione principale (mai a subagent), 2026-09-21:
1) Generazione candidati a zero token LLM: grep sul testo ufficiale grezzo
   (app/.source_cache/reg-ue-2025-1566/raw.txt) per citazioni esplicite ad
   altre fonti censite - nessuna occorrenza di "82/2005" (CAD), "22 febbraio
   2013" (Fonte 4), "24 ottobre 2014"/SPID (Fonte 5), "19 ottobre 2021"
   (Fonte 6), "319 412-5" (Fonte 7); solo citazioni a eIDAS/eIDAS2 (910/2014,
   2024/1183), già modellate come relazioni native nel modulo cap01.py.
   KNN sull'indice vettoriale HNSW (idxEmbeddingObbligo/idxEmbeddingPrincipio,
   soglia 0.80) dai 9 nodi di questo capitolo verso tutti i nodi delle altre
   7 fonti: 116 coppie candidate (9 nodi -> media 12.9 candidati/nodo).
2) Classificazione LLM sullo shortlist di 116 coppie (non sul prodotto
   cartesiano 9x1453), 9 chiamate completion() dirette in parallelo (una per
   nodo di questo capitolo, 10-14 candidati ciascuna), system prompt con
   tassonomia ristretta a specifica/si applica a/attua/richiama/si sovrappone
   a/definisce (le uniche plausibili per relazioni cross-fonte tematiche, non
   novellistiche), output a schema JSON, prompt esplicitamente conservativo.
   Esito: 114 delle 116 coppie scartate come falsi positivi lessicali del
   prefiltro vettoriale (linguaggio giuridico UE generico condiviso da gran
   parte del censimento - "deve essere accreditato", "conformemente a",
   "entro il termine" - senza sovrapposizione concettuale reale). Notevole:
   il candidato con score piu' alto in assoluto (1.0, "art. 2, entrata in
   vigore" vs eIDAS "art. 52 §1") e' stato correttamente scartato dal
   classificatore: le due clausole sono testualmente identiche solo perche'
   condividono la formula standard di entrata in vigore di ogni regolamento
   UE, non perche' esiste una relazione giuridica tra i due atti.
3) Validazione: delle 2 coppie proposte con confidence >= 0.6, una
   ("art. 1" -> "art. 24 §1-quater eIDAS2", attua, 0.9) duplica la relazione
   nativa già inserita in cap01.py (stesso nodo_da/nodo_a/tipo_relazione,
   solo con confidence leggermente diversa) - scartata come duplicato, non
   re-inserita. L'altra ("allegato, punto 6" -> "art. 24 §2(i) eIDAS2",
   attua, 0.75) e' ridondante con la relazione "specifica" già inserita
   nativamente verso lo stesso nodo target - scartata per lo stesso motivo
   (evita due archi paralleli di tipo diverso tra la stessa coppia di nodi
   per lo stesso fatto giuridico). Riletto pero' il testo del punto 2
   dell'allegato (QTS-C3-01): la sua intestazione di clausola cita
   esplicitamente "in conformità all'articolo 24, paragrafi 1, 1 bis e 1
   ter, del regolamento (UE) n.910/2014" - citazione testuale diretta non
   colta nelle relazioni native di cap01.py (che collegava solo l'art. 1 del
   regolamento all'art. 24 §1-quater, la base abilitante generale, non i
   tre paragrafi tecnici che l'allegato specifica nel dettaglio). Aggiunta
   qui come relazione "specifica" (evidence_type "textual", citazione
   esplicita nell'intestazione della clausola C.3 dell'allegato) verso i tre
   obblighi eIDAS2 corrispondenti (art. 24 §1, §1-bis, §1-ter).

Esito finale fase 6: 3 relazioni cross-fonte aggiuntive (tutte verso
eIDAS2/fonte_id=2, tutte "specifica"/evidence_type "textual"), zero verso
CAD/DPCM 22-2-2013/SPID/DPCM 19-10-2021/ETSI EN 319 412-5 - esito verificato
con la pipeline completa, non fase saltata.
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI = [
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 2 (QTS-C3-01)'),
        'nodo_a': ('obbligo', 2, 'art. 24 §1 (vigente, eIDAS2)'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 2 (QTS-C3-01)'),
        'nodo_a': ('obbligo', 2, "art. 24 §1-bis (nuovo, eIDAS2 — metodi di verifica dell'identità)"),
        'tipo_relazione': 'specifica',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 2 (QTS-C3-01)'),
        'nodo_a': ('obbligo', 2, 'art. 24 §1-ter (nuovo, eIDAS2 — metodi di verifica degli attributi)'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
]
