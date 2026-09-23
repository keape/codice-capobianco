"""Regolamento di esecuzione (UE) 2015/1502 (fonte_id=14) - capitolo virtuale di
collegamento cross-fonte (ADR-0009), fase 6 obbligatoria.

Pipeline eseguita nella sessione principale (mai a subagent), 2026-09-23:

1) Generazione candidati a zero token LLM:
   - Grep sul testo ufficiale grezzo (app/.source_cache/reg_ue_2015_1502/cap0[1-3].txt,
     ricostruito dal testo salvato in fase di split) per citazioni esplicite ad
     altre fonti censite: zero occorrenze di "82/2005" (CAD), "22 febbraio 2013"/
     "DPCM"/"SPID"/"19 ottobre 2021"/"319 412-5"/"2025/1566"/"119 461"/
     "319 401"/"119 431"/"modalità attuative" - il testo ufficiale di questo
     regolamento cita solo "910/2014" (eIDAS/eIDAS2, in particolare l'art. 8 §3
     come base abilitante, ripreso più volte nell'art. 1 e nel preambolo) e
     "765/2008" (Regolamento CE sull'accreditamento, non una Fonte censita in
     questo grafo - nessuna relazione possibile).
   - KNN sull'indice vettoriale HNSW (idxEmbeddingObbligo/idxEmbeddingPrincipio,
     soglia 0.80) dai 29 nodi di questa fonte verso tutti i nodi delle altre 13
     Fonti: 704 coppie candidate (29 nodi -> media 24,3 candidati/nodo, valore
     alto atteso vista la contiguità tematica forte tra "livelli di garanzia
     eID" e più standard ETSI/norme italiane SPID già censiti).

2) Classificazione LLM sulla shortlist di 704 coppie (non sul prodotto
   cartesiano 29x2543), 29 chiamate completion() dirette in parallelo (una per
   nodo di questa fonte, gruppate per nodo di partenza), system prompt con
   tassonomia ristretta a attua/specifica/si applica a/richiama/si sovrappone
   a/definisce (le uniche plausibili per relazioni cross-fonte tematiche),
   output a schema JSON, prompt esplicitamente conservativo e con avvertenza
   esplicita sul rischio di falsi positivi da linguaggio giuridico UE
   generico condiviso (già osservato nell'import del Reg. 2025/1566). Esito
   grezzo: 51 proposte (7% delle 704 coppie), disperse tra
   si-sovrappone-a/specifica/attua/richiama.

3) Validazione (fase eseguita con attenzione critica, non solo filtro
   automatico per soglia di confidence, perché la classificazione ha mostrato
   due pattern sistematici di generalizzazione da correggere manualmente):
   - Il pattern "attua/specifica -> eIDAS 'art. 8 §1' (fonte_id=1)" è stato
     proposto per 9 nodi di partenza diversi (2.1.1, 2.2.1, 2.2.2, 2.2.3,
     2.2.4, 2.4.1, 2.4.3, 2.4.6, art. 1 §3) a confidence 0.55-0.90: è una
     ridondanza strutturale, non 9 fatti giuridici distinti. Il testo
     ufficiale di questo regolamento cita esplicitamente **una sola volta**
     la base abilitante precisa, "l'articolo 8, paragrafo 3" (non §1) del
     regolamento (UE) n. 910/2014 - e tale paragrafo, nel grafo, è tracciato
     come Principio "art. 8 §3" sotto **fonte_id=2** (eIDAS2, versione
     vigente), non fonte_id=1. Le 9 proposte sono scartate come falsi
     positivi da sovrapposizione lessicale generica ("livello di garanzia",
     "regime notificato" - esattamente il tipo di rumore descritto nel
     prompt di classificazione); sostituite da UNA sola coppia di relazioni
     native mancanti nel modulo cap01.py (omissione della sessione di
     dispatch originaria, corretta qui): l'art. 1 §1 (designazione generale
     dell'allegato come sede delle specifiche ex art. 8 §3) e l'art. 1 §2
     (mappatura letterale delle 4 lettere a)-d) dell'art. 8 §3) verso il
     Principio eIDAS2 "art. 8 §3".
   - Il pattern "richiama -> DPCM 19/10/2021 'art. 1' (fonte_id=6)" è stato
     proposto per 6 nodi di partenza diversi (2.2.3, art. 1 §1, art. 2,
     allegato punto 2 intro, allegato punto 2.4 intro) a confidence 0.90 -
     stessa causa (score KNN alto per similarità lessicale generica su
     "art. 1"/"2.4", non aggancio reale). Riletto però il testo ufficiale del
     nodo target (fonte_id=6, "art. 1"): è **esattamente** la disposizione
     che inserisce nelle premesse del DPCM 24/10/2014 un richiamo esplicito,
     con numeri di paragrafo, a "l'art. 1, comma 2 e il numero 2.4.1
     (Disposizioni generali) del relativo allegato" di *questo* regolamento
     (2015/1502) - citazione testuale letterale, non un candidato KNN da
     accettare per sovrapposizione lessicale ma un rinvio esplicito reale.
     Le 6 proposte generiche sono scartate; sostituite dalle 2 relazioni
     puntuali effettivamente citate (art. 1 §2 e allegato punto 2.4.1).
   - Indagine aggiuntiva mirata (non generata dal prefiltro KNN, che non
     l'aveva proposta con score sufficiente): il nodo Principio fonte_id=13
     "Avviso AgID n. 10 del 13 luglio 2018" (Regolamento AgID modalità
     attuative SPID) cita testualmente "il paragrafo 2.2.3(3) dell'allegato
     al Regolamento di esecuzione (UE) 2015/1502" come motivo
     dell'inapplicabilità parziale degli artt. 20/23 SPID (riattivazione
     automatica dopo 30 giorni) - verificato leggendo per intero
     `testo_integrale` del nodo (non emerso come candidato KNN ad alto score
     perché il testo dell'Avviso è dominato da contenuto SPID, non dal
     linguaggio del regolamento citato). Aggiunta come relazione "richiama"
     esplicita verso il nodo "allegato, punto 2.2.3" di questa fonte (che
     copre per intero il punto 2.2.3, incluso l'elemento numerato (3) citato
     dall'Avviso).
   - Le restanti ~33 proposte a confidence 0.50-0.70 sono state scartate:
     quasi tutte le motivazioni della classificazione ammettevano
     esplicitamente "sovrapposizione concettuale... pur in contesti
     normativi distinti/diversi" - cioè la stessa ammissione di non-relazione
     prevista come bandiera rossa nel prompt di classificazione (regola 1-2).
     Due sole eccezioni mantenute per genuina sovrapposizione su un concetto
     tecnico specifico (non un argomento generico), a evidence_type
     "inferred" (nessuna citazione testuale, solo sovrapposizione
     concettuale motivata):
     - allegato punto 1(1) "fonte autorevole" <-> ETSI TS 119 461 clausola
       4.4 "Authoritative and supplementary evidence" (fonte_id=9): stesso
       concetto tecnico specifico (non solo "identità" in generale) definito
       in modo sostanzialmente equivalente da due standard/atti diversi
       senza gerarchia tra loro - "si sovrappone a", confidence 0.65.
     - allegato punto 2.4.2 (pubblicazione di avvisi/informazioni per gli
       utenti) <-> ETSI EN 319 401 REQ-6.2-03 (fonte_id=10): stesso obbligo
       specifico di informativa preventiva chiara su termini/condizioni/
       limitazioni d'uso del servizio, non solo un tema generico di
       trasparenza - "si sovrappone a", confidence 0.62.

Esito finale fase 6: 7 relazioni cross-fonte (2 native mancanti aggiunte qui
verso eIDAS2/fonte_id=2 "attua"/"specifica"; 2 verso DPCM 19/10/2021/
fonte_id=6 "richiama", con evidence_type "textual" per citazione letteraria
con numeri di paragrafo espliciti; 1 verso Regolamento AgID modalità
attuative SPID/fonte_id=13 "richiama", evidence_type "textual"; 2 verso
standard ETSI/fonte_id=9 e fonte_id=10 "si sovrappone a", evidence_type
"inferred"); zero verso CAD/DPCM 22-2-2013/SPID (DPCM 24-10-2014)/ETSI EN 319
412-5/Regolamento (UE) 2025/1566/ETSI TS 119 431-1/ETSI TS 119 431-2 - esito
verificato con la pipeline completa (grep + KNN + classificazione LLM +
validazione critica manuale), non fase saltata.
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI = [
    {
        "nodo_da": ("principio", None, "art. 1 §1"),
        "nodo_a": ("principio", 2, "art. 8 §3"),
        "tipo_relazione": "attua",
        "evidence_type": "textual",
        "confidence": 0.92,
    },
    {
        "nodo_da": ("principio", None, "art. 1 §2"),
        "nodo_a": ("principio", 2, "art. 8 §3"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 6, "art. 1"),
        "nodo_a": ("principio", None, "art. 1 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
    {
        "nodo_da": ("principio", 6, "art. 1"),
        "nodo_a": ("obbligo", None, "allegato, punto 2.4.1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
    {
        "nodo_da": ("principio", 13, "Avviso AgID n. 10 del 13 luglio 2018"),
        "nodo_a": ("obbligo", None, "allegato, punto 2.2.3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("principio", None, "allegato, punto 1(1) (fonte autorevole)"),
        "nodo_a": ("principio", 9, "clausola 4.4 (Authoritative and supplementary evidence)"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.65,
    },
    {
        "nodo_da": ("obbligo", None, "allegato, punto 2.4.2"),
        "nodo_a": ("obbligo", 10, "REQ-6.2-03"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.62,
    },
]
