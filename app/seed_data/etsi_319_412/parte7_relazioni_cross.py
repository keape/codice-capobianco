"""Relazioni cross-fonte e relazioni interne fra le 5 Parti di ETSI EN 319 412
(Fase 6, ADR-0009), per i 158 nodi delle Parti 1-4 importate 2026-09-23 (le
relazioni della Parte 5 preesistente restano in parte6_relazioni_cross.py,
non toccate). Modulo "capitolo virtuale" nel senso del contratto di
app/seed_data/lib.py:inserisci_capitoli (nessuna riga obbligo/principio
propria, solo RELAZIONI), eseguito nella sessione principale (mai da
subagent).

Pipeline effettivamente usata (3 stadi, ADR-0009):

1. Candidati da citazione testuale esplicita: grep su
   app/.source_cache/etsi_319_412/parte[1-4]_raw.txt per nomi di altre Fonti
   gia' censite ("910/2014", "319 411", "319 401", "2015/1502", "2025/1566",
   "CAD", "SPID", "119 461", "119 431"). Trovate citazioni esplicite e
   puntuali (non generiche al regolamento nel suo complesso) solo verso: (a)
   ETSI EN 319 411-1 (REV-6.2.4-03A citato per nome nella nota di Parte 1
   clausola 5.2.2; clausola 6.4.5 citata per l'audit log in Parte 2
   NAT-4.2.4-12A), (b) ETSI EN 319 411-2 (clausola 5.3 "identificatori delle
   policy" citata esplicitamente da Parte 2 QCS-5.2-1), (c) ETSI EN 319 401
   (clausola 3 "terms given in ETSI EN 319 401 apply", citata da Parte 1
   clausola 3). Nessuna citazione puntuale risolvibile a un nodo specifico
   verso eIDAS/eIDAS2 (i riferimenti a "Regulation (EU) No 910/2014" sono
   quasi tutti generici al regolamento nel suo complesso, non a un articolo
   o Allegato puntuale — unica eccezione, "Annex I (i)" in Parte 2
   GEN-4.3.11-2A/GEN-4.4.1-8A, non risolvibile: nessun nodo eIDAS/eIDAS2
   modella l'Allegato I come nodo autonomo o via articolo dedicato
   individuabile con certezza, quindi omessa per non inventare — coerente
   con la relazione "si sovrappone a" verso CSS-6.3.10-01B di ETSI EN 319
   411-1 trovata via KNN, che copre lo stesso concetto (No Revocation
   Available) con evidenza piu' solida).
2. Candidati aggiuntivi via KNN sull'indice vettoriale HNSW gia' popolato
   (idxEmbeddingObbligo/idxEmbeddingPrincipio, top-4 per nodo, soglia
   score >= 0.86) verso le altre Fonti tecniche piu' affini per perimetro
   tematico (ETSI EN 319 411-1/-2, che condividono con EN 319 412 lo stesso
   dominio "profili di certificato" — EN 319 411-1/-2 specifica i requisiti
   organizzativi per i TSP che DEVONO poi emettere certificati conformi ai
   profili di EN 319 412). 24 coppie con score >= 0.86 (incluse le 4
   citazioni testuali sopra, gia' presenti nella shortlist KNN salvo
   "clausola 3 -> EN 319 401" che il KNN non aveva incluso ed e' stata
   aggiunta manualmente dalla citazione testuale).
3. Classificazione LLM via completion() in batch da 8, in parallelo con
   wait() (non subagent), su riferimento+testo sintetico (mai testo_integrale
   o testo ufficiale grezzo). Filtro: confidence >= 0.55 E tipo_relazione
   valido nella tassonomia di neo4j_common.TIPO_RELAZIONE_TO_ARCO (uno score
   ha prodotto un nome di relazione inversa non valido, "e' precondizione
   di" — scartato per non correggere a mano la direzione senza riverifica).
   10 relazioni esterne confermate dopo il filtro (verso ETSI EN 319 411-1:
   4; verso ETSI EN 319 401: 1 manuale da citazione testuale; verso ETSI EN
   319 411-2: 5).

Verificato (esito, non fase saltata) zero citazioni dirette risolvibili
verso: CAD (fonte_id=3), DPCM 22/2/2013 (fonte_id=4, unica coincidenza KNN
trovata — "art. 19 c.7"/"art. 19 c.1 lett.a)" — era una coincidenza lessicale
priva di corrispondenza sostanziale, scartata dal classificatore con
tipo_relazione=null), SPID/DPCM 24-10-2014 (fonte_id=5), DPCM 19-10-2021
(fonte_id=6), Regolamento (UE) 2025/1566 (fonte_id=8), ETSI TS 119 461
(fonte_id=9, una coincidenza KNN su GEN-4.2.3.2-7 scartata come priva di
citazione o sovrapposizione sostanziale), ETSI TS 119 431-1/-2 (fonte_id=11,
12), Regolamento AgID modalita' attuative SPID (fonte_id=13), Regolamento
(UE) 2015/1502 (fonte_id=14, una coincidenza KNN su GEN-4.1-1/par. 4.2 punto
1 scartata), Regole Tecniche AgID certificati qualificati (fonte_id=15),
Codice Civile (fonte_id=16, import selettivo, nessuna sovrapposizione
tematica con profili di certificato tecnici).

Relazioni interne fra le 5 Parti dello stesso deliverable ETSI (stessa
Fonte, fonte_id_o_None=None su entrambi i lati): individuate dalle
dichiarazioni esplicite "builds on"/"shall comply with"/"the following
requirements shall apply" con cui ciascuna Parte 2-4 si aggancia
esplicitamente a Parte 1 (struttura/semantica comune) e Parte 2/3
(profili via via piu' specifici: Parte 3 legal person costruisce su Parte 2
natural person; Parte 4 web site richiama sia Parte 2 sia Parte 3 a seconda
del tipo di soggetto), e con cui Parte 2/4 si agganciano a Parte 5
(QCStatements) per i certificati qualificati UE. Non esaustive (centinaia di
overlap concettuali minori fra le 5 Parti sarebbero rumore, non evidenza),
limitate ai punti di aggancio esplicito piu' significativi.
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI = [
    # --- Relazioni interne fra le 5 Parti (fonte_id_o_None=None su entrambi i lati) ---
    {
        "nodo_da": ("principio", None, "Parte 2: clausola 3 (Definition of terms, symbols, abbreviations and notations)"),
        "nodo_a": ("principio", None, "Parte 1: clausola 3 (definizioni, simboli, abbreviazioni, notazioni)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 3: LEG-4.1-1"),
        "nodo_a": ("obbligo", None, "Parte 2: GEN-4.1-1"),
        "tipo_relazione": "richiede come precondizione",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 4: WEB-4.1.3-2"),
        "nodo_a": ("obbligo", None, "Parte 2: GEN-4.1-1"),
        "tipo_relazione": "si applica a",
        "evidence_type": "textual",
        "confidence": 0.65,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 4: WEB-4.1.3-3"),
        "nodo_a": ("obbligo", None, "Parte 3: LEG-4.2.1-1"),
        "tipo_relazione": "si applica a",
        "evidence_type": "textual",
        "confidence": 0.65,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: QCS-5.1-1"),
        "nodo_a": ("obbligo", None, "Parte 5: QCS-5-01"),
        "tipo_relazione": "richiede come precondizione",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 4: QCS-4.2-1"),
        "nodo_a": ("obbligo", None, "Parte 5: QCS-5-01"),
        "tipo_relazione": "richiede come precondizione",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    # --- Relazioni cross-fonte esterne (KNN + classificazione LLM, confidence >= 0.55) ---
    {
        "nodo_da": ("obbligo", None, "Parte 2: GEN-4.4.1-8A"),
        "nodo_a": ("obbligo", 17, "Parte 1: CSS-6.3.10-01B"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: GEN-4.3.11-2A"),
        "nodo_a": ("obbligo", 17, "Parte 1: CSS-6.3.10-01B"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: QCS-5.1-1"),
        "nodo_a": ("obbligo", 17, "Parte 2: GEN-6.6.1-02"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("principio", None, "Parte 1: clausola 4.1 (General approach)"),
        "nodo_a": ("principio", 17, "Parte 1: clausola 6.2.1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 3: LEG-4.1-1"),
        "nodo_a": ("obbligo", 17, "Parte 1: OVR-7.1-11"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: QCS-5.2-2"),
        "nodo_a": ("obbligo", 17, "Parte 2: OVR-6.9.4-02"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        "nodo_da": ("principio", None, "Parte 2: clausola 1 (Scope)"),
        "nodo_a": ("principio", 17, "Parte 1: clausola 6.2.1"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        "nodo_da": ("principio", None, "Parte 1: clausola 5.2.2 (Validity Assured - Short Term)"),
        "nodo_a": ("obbligo", 17, "Parte 1: REV-6.2.4-03A"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: NAT-4.2.4-12A"),
        "nodo_a": ("obbligo", 17, "Parte 1: OVR-6.4.5-01"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, "Parte 2: QCS-5.2-1"),
        "nodo_a": ("principio", 17, "Parte 2: clausola 5.3 (identificatori delle policy)"),
        "tipo_relazione": "attua",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("principio", None, "Parte 1: clausola 3 (definizioni, simboli, abbreviazioni, notazioni)"),
        "nodo_a": ("principio", 10, "clausola 3.1 (Terms)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
]
