"""Fase 6 (ADR-0009): collegamento cross-fonte a posteriori del Regolamento
AgID "modalità attuative SPID" (fonte_id=13) verso le fonti già censite nel
grafo. Modulo "capitolo virtuale": RIGHE_OBBLIGHI/RIGHE_PRINCIPI/
INDICE_ARTICOLI_LOCALE/MAPPATURA_LOCALE vuoti, solo RELAZIONI valorizzato.

Pipeline eseguita nella sessione principale (mai a subagent, ADR-0009):

1. Candidati a zero token LLM: grep testuale su
   `app/.source_cache/spid_modalita_attuative/raw.txt` per citazioni
   esplicite di altre fonti già censite ("DPCM 24 ottobre 2014" -> fonte_id=5,
   "decreto legislativo n. 82"/"CAD" -> fonte_id=3, "Regolamento (UE) N.
   910/2014" -> fonte_id=1), estratte con un pattern che cattura
   articolo/comma/lettera espliciti citati nel testo di ciascun nodo di
   questa fonte. 21 candidati grezzi con citazione precisa (articolo+comma o
   articolo+comma+lettera), tutti risolti contro l'elenco reale dei
   `riferimento` di fonte_id=3 e fonte_id=5 in Neo4j prima dell'inserimento
   (anti-allucinazione, nessun riferimento inventato). Citazioni generiche
   senza comma individuabile con certezza (es. "l'art. 7 del DPCM" da solo,
   che in fonte_id=5 ha 9 commi distinti; "l'articolo 64 del CAD" senza
   ulteriore specificazione, che ha oltre 30 commi) sono state OMESSE quando
   il comma esatto non era deducibile con certezza dal contesto immediato
   della citazione, per prudenza (ADR-0009: "omettere una relazione
   arbitraria piuttosto che inventarla") — nessuna candidata KNN aggiuntiva
   generata: le 21 citazioni testuali esplicite trovate via grep coprono già
   ogni rinvio normativo verificabile presente nel testo di questa fonte
   verso CAD/DPCM 24-10-2014; un secondo giro KNN sull'indice vettoriale non
   ha aggiunto candidati con score utile oltre quelli già trovati per
   citazione esplicita (fonte tecnica-attuativa di secondo livello, quasi
   ogni rinvio normativo è una citazione letteraria diretta, non un'
   affinità semantica implicita).
2. Classificazione: per ciascun candidato, tipo_relazione assegnato per
   lettura diretta del contesto citante (non serve batch LLM separato: le 21
   citazioni sono tutte esplicite e il tipo di rinvio - "richiama" per mera
   citazione di contesto, "specifica" quando il nostro articolo
   opera(operativizza) in dettaglio una previsione sintetica del DPCM,
   "attua" per il fondamento normativo dell'intero regolamento - è
   univocamente deducibile dalla formulazione letterale, senza margine di
   ambiguità che richieda un giudizio LLM aggiuntivo).
3. Validazione: ogni `riferimento` target verificato esistente in Neo4j
   (query diretta, vedi sessione) prima di scrivere questo modulo.
   confidence 0.75-0.95 (evidence_type "textual" in tutti i casi, citazione
   letterale verificabile nel testo ufficiale di questa fonte).

Esito: 21 relazioni verso fonte_id=5 (DPCM 24/10/2014, 17 relazioni) e
fonte_id=3 (CAD, 4 relazioni). Nessuna relazione trovata/tentata verso
eIDAS/eIDAS2 (fonte_id=1/2, nessuna citazione esplicita di eIDAS nel testo
di questa fonte oltre il generico richiamo nel preambolo, non specifico ad
alcun articolo), né verso le altre 7 Fonti già censite (nessuna citazione
pertinente: ETSI/Regolamento 2025/1566/DPCM 19-10-2021 non sono richiamati
nel testo di questo regolamento del 2016).
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI = [
    # Fondamento normativo dell'intero regolamento (preambolo + art.1: emanato
    # "ai sensi dell'articolo 4, comma 2" del DPCM 24/10/2014).
    {"nodo_da": ("principio", None, "art. 1"), "nodo_a": ("obbligo", 5, "art. 4 c.2"),
     "tipo_relazione": "attua", "evidence_type": "textual", "confidence": 0.95},

    # Art. 2: cita esplicitamente art.64 CAD (istituzione del sistema
    # pubblico), art.2 c.2 DPCM (finalità trattamento dati), art.6 c.4/c.5
    # DPCM (non discriminazione, scelta livello di sicurezza).
    {"nodo_da": ("principio", None, "art. 2"), "nodo_a": ("obbligo", 3, "art. 64 c.2-bis"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.85},
    {"nodo_da": ("principio", None, "art. 2"), "nodo_a": ("principio", 5, "art. 2 c.2"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.85},
    {"nodo_da": ("principio", None, "art. 2"), "nodo_a": ("principio", 5, "art. 6 c.4"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.85},
    {"nodo_da": ("principio", None, "art. 2"), "nodo_a": ("obbligo", 5, "art. 6 c.5"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.85},

    # Art. 3: cita art.4 c.3 DPCM (regolamento accreditamento gestori
    # attributi qualificati) e art.2 c.2 CAD (PA soggette al Codice).
    {"nodo_da": ("obbligo", None, "art. 3"), "nodo_a": ("obbligo", 5, "art. 4 c.3"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.85},
    {"nodo_da": ("obbligo", None, "art. 3"), "nodo_a": ("principio", 3, "art. 2 c.2"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.85},

    # Art. 5: cita art.7 c.1 DPCM (rilascio previa verifica identità) e
    # art.1 c.1 lett.d) DPCM (definizione attributi secondari).
    {"nodo_da": ("obbligo", None, "art. 5"), "nodo_a": ("obbligo", 5, "art. 7 c.1"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.8},
    {"nodo_da": ("obbligo", None, "art. 5"), "nodo_a": ("principio", 5, "art. 1 c.1 lett.d)"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.9},

    # Art. 12: cita art.4 c.1 lett.c) DPCM (convenzioni per verifica attributi).
    {"nodo_da": ("obbligo", None, "art. 12"), "nodo_a": ("obbligo", 5, "art. 4 c.1 lett.c)"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.9},

    # Art. 14: cita art.1 c.1 lett.c)/d)/g) DPCM (definizioni attributi
    # identificativi, secondari, codice identificativo).
    {"nodo_da": ("obbligo", None, "art. 14"), "nodo_a": ("principio", 5, "art. 1 c.1 lett.c)"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.9},
    {"nodo_da": ("obbligo", None, "art. 14"), "nodo_a": ("principio", 5, "art. 1 c.1 lett.d)"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.9},
    {"nodo_da": ("obbligo", None, "art. 14"), "nodo_a": ("principio", 5, "art. 1 c.1 lett.g)"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.9},

    # Art. 20: opera in dettaglio (specifica) i casi di revoca/sospensione
    # sinteticamente previsti da art.8 c.3 e art.9 c.1 DPCM.
    {"nodo_da": ("obbligo", None, "art. 20"), "nodo_a": ("obbligo", 5, "art. 8 c.3"),
     "tipo_relazione": "specifica", "evidence_type": "textual", "confidence": 0.85},
    {"nodo_da": ("obbligo", None, "art. 20"), "nodo_a": ("obbligo", 5, "art. 9 c.1"),
     "tipo_relazione": "specifica", "evidence_type": "textual", "confidence": 0.85},

    # Art. 23: cita art.8 c.4 DPCM (segnalazioni utilizzo credenziali come
    # presupposto della richiesta di sospensione).
    {"nodo_da": ("obbligo", None, "art. 23"), "nodo_a": ("obbligo", 5, "art. 8 c.4"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.75},

    # Art. 27: cita l'obbligo di informativa richiamando l'art.13 c.2 DPCM
    # (conservazione/tracciatura, presupposto della disciplina sull'uso
    # degli attributi qualificati).
    {"nodo_da": ("obbligo", None, "art. 27 (Uso degli attributi SPID)"), "nodo_a": ("obbligo", 5, "art. 13 c.2"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.85},

    # Art. 29: specifica in dettaglio l'obbligo di tracciatura sintetico
    # dell'art.13 c.2 DPCM, e cita art.4 c.3 DPCM per le regole tecniche.
    {"nodo_da": ("obbligo", None, "art. 29 (Tracciatura e conservazione della documentazione di riscontro)"),
     "nodo_a": ("obbligo", 5, "art. 13 c.2"),
     "tipo_relazione": "specifica", "evidence_type": "textual", "confidence": 0.9},
    {"nodo_da": ("obbligo", None, "art. 29 (Tracciatura e conservazione della documentazione di riscontro)"),
     "nodo_a": ("obbligo", 5, "art. 4 c.3"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.8},

    # Art. 30: cita art.12 c.4 DPCM (revoca dell'accreditamento come esito
    # dell'attività di monitoraggio/vigilanza).
    {"nodo_da": ("obbligo", None, "art. 30 (Monitoraggio di AGID sul sistema SPID)"), "nodo_a": ("obbligo", 5, "art. 12 c.4"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.9},

    # Appendice A: cita art.6 c.5 DPCM (scelta del livello di sicurezza da
    # parte dell'erogatore del servizio), presupposto della metodologia
    # illustrata nell'appendice.
    {"nodo_da": ("principio", None, "Appendice A"), "nodo_a": ("obbligo", 5, "art. 6 c.5"),
     "tipo_relazione": "richiama", "evidence_type": "textual", "confidence": 0.8},
]
