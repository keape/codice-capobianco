"""ETSI TS 119 612 V2.4.1 (2025-08) - Fase 6 (ADR-0009): capitolo virtuale
per le relazioni cross-fonte.

RIGHE_OBBLIGHI/RIGHE_PRINCIPI/INDICE_ARTICOLI_LOCALE/MAPPATURA_LOCALE vuoti:
questo modulo non contribuisce nodi, solo archi `RELAZIONI`. Ogni arco ha
`nodo_da` a fonte implicita (None -> la fonte corrente, 21) e `nodo_a` a
fonte esplicita (l'intero e' il `fonte_id` della fonte controparte gia'
inserita dalle chiamate precedenti di `seed.py`).

Pipeline di generazione (ADR-0009, eseguita nella sessione principale il
2026-09-24, dopo il seed dei 118 nodi di questa fonte):
  1. Candidati a zero token LLM su `app/.source_cache/etsi_119_612/raw.txt`
     (`app/tools/fase6_candidati_612.py`): grep per citazioni esplicite di
     altre fonti (trovate: Reg. (UE) 910/2014 in 8 nodi, Reg. (UE) 2024/1183,
     ETSI EN 319 412-5, CD 2009/767/EC, ETSI TS 119 312) + KNN sull'indice
     vettoriale HNSW (`idxEmbeddingObbligo`/`idxEmbeddingPrincipio`,
     soglia 0.80, top_k 8) -> 258 coppie KNN uniche + 63 coppie da citazione
     esplicita (10 nodi citanti verso i nodi eIDAS art. 22 §1-§5, art. 23 §1
     ed eIDAS2 art. 3) = 321 coppie.
  2. Classificazione LLM (`completion()` in batch da 10, in parallelo con
     `wait()`, mai subagent) sullo shortlist, tassonomia ristretta ai tipi
     plausibili e prompt esplicitamente conservativo -> 60 proposte.
  3. Validazione: scarto di 7 proposte "si sovrappone a" fra glossario e
     glossario (clausole 3.1 Terms/3.2 Symbols di questa Fonte verso le
     clausole 3.x di ETSI TS 119 431/EN 319 411/EN 319 421/TS 119 432/TS 119
     461: nessun contenuto normativo proprio, stesso criterio gia' applicato
     in ETSI TS 119 432), filtro `confidence` >= 0.5, verifica che ogni
     `riferimento` (lato fonte 21 e lato controparte, con il tipo di nodo)
     esista davvero in Neo4j -> **54 relazioni valide, 0 scartate dalla
     verifica anti-allucinazione**. Aggiunta 1 relazione testuale esplicita
     non emersa dal classificatore: clausola 5.5.1.2 cita letteralmente
     "Article 3(16)" e "Article 3(46) of Regulation (EU) 910/2014", risolti
     sul nodo vigente "art. 3 (definizioni)" di eIDAS2 (in eIDAS la fonte 1
     non ha un nodo per l'art. 3 - le definizioni 2014 sono state catturate
     nel testo vigente eIDAS2, stessa rimappatura gia' applicata nel giro
     Fase 6 di ETSI EN 319 421).

Esito: 54 relazioni cross-fonte, tutte con `evidence_type`/`confidence`
per-arco (ADR-0005): si sovrappone a 31, specifica 19, richiama 3, richiede come precondizione 1; 1 textual (la sola
citazione letterale di articolo), 53 inferred. Per fonte
controparte: eIDAS (fonte_id=1): 21, eIDAS2 (fonte_id=2): 2, DPCM 22/2/2013 (4): 3, ETSI EN 319 412 (7): 10, ETSI EN 319 401 (10): 5, ETSI TS 119 431 (11): 1, Regole Tecniche AgID (15): 4, ETSI EN 319 411 (17): 5, ETSI EN 319 421 (18): 3.

Il grosso delle relazioni e' verso eIDAS (art. 22 §1-§5: l'obbligo per gli
Stati membri di istituire, mantenere e pubblicare gli elenchi di fiducia e le
relative specifiche tecniche - ETSI TS 119 612 e' la specifica tecnica di
formato/semantica/accesso di quegli elenchi; art. 23 §1: registrazione della
qualifica nel TL) e verso gli standard ETSI sui profili di certificato e
sulle policy dei TSP, per sovrapposizione concettuale su singoli campi
(country code, date-time UTC, estensioni di revoca, QCStatement/qualificatori
QSCD, identificatore del firmatario nelle firme XAdES).

Citazioni a fonti NON censite nel grafo al momento di questo giro (CD
2009/767/EC, ETSI TS 119 312, ISO/IEC 15408 e 19790, IETF RFC 3161/5280, CID
(EU) 2015/1505, direttiva (UE) 2022/2555) non producono relazioni per assenza
di nodo controparte. Le citazioni di ETSI EN 319 412-5 nella clausola 2.2
(riferimento informativo [i.9]) sono bibliografiche: nessuna relazione.
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI: list[dict] = [
    {
        # Annex D.5.6 definisce gli URI di stato quali dettagli tecnici dei formati degli elenchi di fiducia richiesti dall'art. 22 §5.
        "nodo_da": ("obbligo", None, "Annex D.5.6 (Service current and previous statuses)"),
        "nodo_a": ("principio", 1, "art. 22 §5"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.65,
    },
    {
        # La LOTL pubblicata dalla Commissione rinvia ai luoghi ove gli Stati membri pubblicano le trusted list ex art. 22 §2: ne presuppone la pubblicazione.
        "nodo_da": ("principio", None, "Annex H.2 (Locating a TL)"),
        "nodo_a": ("principio", 1, "art. 22 §2"),
        "tipo_relazione": "richiede come precondizione",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        # Annex H.2 richiama le trusted list 'come notificate dagli Stati membri', corrispondenti all'obbligo di notifica alla Commissione di cui all'art. 22 §3 eIDAS.
        "nodo_da": ("principio", None, "Annex H.2 (Locating a TL)"),
        "nodo_a": ("principio", 1, "art. 22 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": 0.65,
    },
    {
        # Annex J disciplina la migrazione delle trusted list degli Stati membri nell'ambito del regime degli elenchi di fiducia di cui all'art. 22 §1.
        "nodo_da": ("obbligo", None, "Annex J (Migration of EU MS trusted lists in the context of Regulation (EU) No 910/2014)"),
        "nodo_a": ("principio", 1, "art. 22 §1"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        # Annex J opera nel contesto delle specifiche tecniche e dei formati degli elenchi di fiducia definiti ai sensi dell'art. 22 §5.
        "nodo_da": ("obbligo", None, "Annex J (Migration of EU MS trusted lists in the context of Regulation (EU) No 910/2014)"),
        "nodo_a": ("principio", 1, "art. 22 §5"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        # La clausola 1 di TS 119 612 detta formato, semantica e meccanismi operativi della trusted list, rendendo attuativo l'obbligo generale dell'art. 22 §1 eIDAS.
        "nodo_da": ("principio", None, "clausola 1 (Scope)"),
        "nodo_a": ("principio", 1, "art. 22 §1"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.78,
    },
    {
        # A specifica formato, semantica e meccanismi di accesso/autenticazione della TL firmata, dettagliando operativamente l'art. 22 §2 eIDAS.
        "nodo_da": ("principio", None, "clausola 1 (Scope)"),
        "nodo_a": ("principio", 1, "art. 22 §2"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.76,
    },
    {
        # A definisce formato e semantica della TL, dettaglio tecnico dei formati che l'art. 22 §5 eIDAS demanda alle specifiche della Commissione.
        "nodo_da": ("principio", None, "clausola 1 (Scope)"),
        "nodo_a": ("principio", 1, "art. 22 §5"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        # Il TS 119 612 dettaglia contenuti e formati degli elenchi di fiducia, definendo l'URI del tipo di servizio qualificato elencato ai sensi dell'art. 22 §1.
        "nodo_da": ("obbligo", None, "clausola 5.5.1.0 (General requirements)"),
        "nodo_a": ("principio", 1, "art. 22 §1"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        # Il TS 119 612 specifica formato e firma/sigillo elettronico degli elenchi pubblicati in forma atta al trattamento automatizzato, come previsto dall'art. 22 §2.
        "nodo_da": ("obbligo", None, "clausola 5.5.1.0 (General requirements)"),
        "nodo_a": ("principio", 1, "art. 22 §2"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        # Il TS 119 612 disciplina i dati del gestore e i certificati di firma degli elenchi di fiducia notificati alla Commissione (art. 22 §3).
        "nodo_da": ("obbligo", None, "clausola 5.5.1.0 (General requirements)"),
        "nodo_a": ("principio", 1, "art. 22 §3"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # Il TS 119 612 specifica la lista delle liste di fiducia pubblicata dalla Commissione in forma firmata e leggibile automaticamente (art. 22 §4).
        "nodo_da": ("obbligo", None, "clausola 5.5.1.0 (General requirements)"),
        "nodo_a": ("principio", 1, "art. 22 §4"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        # Il TS 119 612 costituisce la specifica tecnica di informazioni e formati degli elenchi di fiducia prevista dagli atti di esecuzione dell'art. 22 §5.
        "nodo_da": ("obbligo", None, "clausola 5.5.1.0 (General requirements)"),
        "nodo_a": ("principio", 1, "art. 22 §5"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.65,
    },
    {
        # La clausola 5.5.1.1 enumera con URI e requisiti i tipi di servizio fiduciario qualificato che confluiscono negli elenchi di fiducia dell'art. 22 §1.
        "nodo_da": ("obbligo", None, "clausola 5.5.1.1 (Regulation (EU) No 910/2014 qualified trust service types)"),
        "nodo_a": ("principio", 1, "art. 22 §1"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        # La clausola 5.5.1.1 dettaglia i tipi di servizio fiduciario qualificato degli elenchi pubblicati in forma elettronica firmata richiesti dall'art. 22 §2.
        "nodo_da": ("obbligo", None, "clausola 5.5.1.1 (Regulation (EU) No 910/2014 qualified trust service types)"),
        "nodo_a": ("principio", 1, "art. 22 §2"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        # La clausola 5.5.1.1 dettaglia tecnicamente formati e contenuti degli elenchi di fiducia che l'art. 22 §5 demanda alle specifiche tecniche della Commissione.
        "nodo_da": ("obbligo", None, "clausola 5.5.1.1 (Regulation (EU) No 910/2014 qualified trust service types)"),
        "nodo_a": ("principio", 1, "art. 22 §5"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.7,
    },
    {
        # La clausola definisce gli identificatori dei tipi di servizio contenuti negli elenchi di fiducia istituiti dall'art. 22 §1.
        "nodo_da": ("obbligo", None, "clausola 5.5.1.2 (Regulation (EU) No 910/2014 non qualified trust service types)"),
        "nodo_a": ("principio", 1, "art. 22 §1"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        # La clausola fornisce i tipi di servizio in forma strutturata, coerente con il trattamento automatizzato richiesto dall'art. 22 §2.
        "nodo_da": ("obbligo", None, "clausola 5.5.1.2 (Regulation (EU) No 910/2014 non qualified trust service types)"),
        "nodo_a": ("principio", 1, "art. 22 §2"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # Clausola 5.5.1.2 detta il registro dei tipi di servizio/URI e i formati degli elenchi, dettaglio attuativo della specifica tecnica richiesta dall'art. 22 §5.
        "nodo_da": ("obbligo", None, "clausola 5.5.1.2 (Regulation (EU) No 910/2014 non qualified trust service types)"),
        "nodo_a": ("principio", 1, "art. 22 §5"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        # Clausola 5.5.1.3 contribuisce ai formati degli elenchi specificando anche i tipi nazionali, dettaglio della specifica richiesta dall'art. 22 §5.
        "nodo_da": ("obbligo", None, "clausola 5.5.1.3 (Trust service types not defined in Regulation (EU) No 910/2014 but nationally defined)"),
        "nodo_a": ("principio", 1, "art. 22 §5"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        # Clausola 5.5.4 detta il formato del campo di stato, dettaglio delle specifiche tecniche e formati che l'art. 22 §5 demanda alla Commissione.
        "nodo_da": ("obbligo", None, "clausola 5.5.4 (Service current status)"),
        "nodo_a": ("principio", 1, "art. 22 §5"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        # La clausola 3.1 definisce i termini 'per rinvio' alle definizioni del Regolamento (es. electronic archiving, electronic ledger, EAA), senza modificarle.
        "nodo_da": ("principio", None, "clausola 3.1 (Terms)"),
        "nodo_a": ("principio", 2, "art. 3 (definizioni)"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        # Citazione letterale di Article 3(16) e Article 3(46) del Reg. (UE) 910/2014 (nodo vigente in eIDAS2).
        "nodo_da": ("obbligo", None, "clausola 5.5.1.2 (Regulation (EU) No 910/2014 non qualified trust service types)"),
        "nodo_a": ("principio", 2, "art. 3 (definizioni)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
    {
        # Entrambe impongono l'uso della scala UTC per i riferimenti temporali, in contesti diversi (campi TL vs firme).
        "nodo_da": ("obbligo", None, "clausola 5.1.3 (Date-time indication)"),
        "nodo_a": ("obbligo", 4, "art. 41 c.3"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # A richiede valori data-ora espressi in UTC; B dispone che il riferimento temporale della marca sia in UTC. Requisito condiviso.
        "nodo_da": ("obbligo", None, "clausola 5.1.3 (Date-time indication)"),
        "nodo_a": ("obbligo", 4, "art. 51 c.2"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        # A tratta i bit di key usage del certificato; B l'indicazione della tipologia di coppia di chiavi secondo l'uso. Medesima materia, gerarchia assente.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.2.1 (KeyUsage)"),
        "nodo_a": ("obbligo", 4, "art. 19 c.1 lett.b)"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # Entrambe trattano l'uso e l'interpretazione dei codici paese.
        "nodo_da": ("obbligo", None, "clausola 5.1.5 (Value of Country Code fields)"),
        "nodo_a": ("obbligo", 7, "Parte 1: GEN-5.1.1-03"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # Entrambe riguardano l'uso di prefissi/codici paese ISO nel campo identificativo.
        "nodo_da": ("obbligo", None, "clausola 5.1.5 (Value of Country Code fields)"),
        "nodo_a": ("obbligo", 7, "Parte 1: LEG-5.1.4-04"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # Entrambe disciplinano il valore del campo country code/name, senza gerarchia.
        "nodo_da": ("obbligo", None, "clausola 5.1.5 (Value of Country Code fields)"),
        "nodo_a": ("obbligo", 7, "Parte 2: GEN-4.2.3.1-6"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # Entrambe dettano regole sul codice paese/countryName, ma in artefatti diversi.
        "nodo_da": ("obbligo", None, "clausola 5.1.5 (Value of Country Code fields)"),
        "nodo_a": ("obbligo", 7, "Parte 2: GEN-4.2.3.2-4"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # Entrambe dettano vincoli sui valori CountryName codice paese, in contesti distinti.
        "nodo_da": ("obbligo", None, "clausola 5.1.5 (Value of Country Code fields)"),
        "nodo_a": ("obbligo", 7, "Parte 5: QCS-4.2.5-01"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # L'estensione Qualifications della TL codifica qualificatori (certificato qualificato, chiave in QSCD) corrispondenti agli statement QCStatements (esi4-qcStatement-1/-4) di EN 319 412-5.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.0 (General)"),
        "nodo_a": ("obbligo", 7, "Parte 5: QCS-5-01"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        # I qualificatori del QualificationElement (natura di certificato qualificato, residenza chiave in QSCD) corrispondono agli QCStatements esi4-qcStatement-1/-4 di EN 319 412-5.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.1 (QualificationElement)"),
        "nodo_a": ("obbligo", 7, "Parte 5: QCS-5-01"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        # Entrambe disciplinano il contenuto dell'estensione certificatePolicies con identificatori di policy: A come criteri di asserzione, B come requisito di presenza.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.2.2 (PolicySet)"),
        "nodo_a": ("obbligo", 7, "Parte 2: GEN-4.3.3-2"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        # A confronta OID di policy con l'estensione certificatePolicies; B prescrive gli stessi identificatori per i certificati qualificati UE.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.2.2 (PolicySet)"),
        "nodo_a": ("obbligo", 7, "Parte 4: QCS-4.3-1"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        # I qualificatori QCWith/NoSSCD e QCWith/NoQSCD corrispondono concettualmente agli esi4-qcStatement sul QSCD/SSCD di EN 319 412-5.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.3 (Qualifier)"),
        "nodo_a": ("obbligo", 7, "Parte 5: QCS-5-01"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        # A prevede gli URI delle practice statements del TSP; B impone al TSP di disporre di una statement of practices: concetto coincidente.
        "nodo_da": ("obbligo", None, "clausola 5.4.4 (TSP information URI)"),
        "nodo_a": ("obbligo", 10, "REQ-6.1-03"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # A indica gli URI per ottenere practice statements/policy del TSP; B ne impone la messa a disposizione a subscriber e relying party: contenuto sostanziale coincidente.
        "nodo_da": ("obbligo", None, "clausola 5.4.4 (TSP information URI)"),
        "nodo_a": ("obbligo", 10, "REQ-6.1-05"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # A annovera i termini e condizioni tra le informazioni ottenibili via URI; B ne specifica il contenuto: concetto dei termini e condizioni condiviso.
        "nodo_da": ("obbligo", None, "clausola 5.4.4 (TSP information URI)"),
        "nodo_a": ("obbligo", 10, "REQ-6.2-02"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # Entrambi riguardano il trasferimento della responsabilità/obblighi del servizio a un'altra parte o TSP.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.3 (TakenOverBy Extension)"),
        "nodo_a": ("obbligo", 10, "REQ-7.12-10"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # Entrambi richiedono politiche/procedure di sicurezza documentate, attuate e mantenute; contenuto sostanzialmente affine senza gerarchia.
        "nodo_da": ("obbligo", None, "clausola 6.5 (TLSO practices)"),
        "nodo_a": ("obbligo", 10, "REQ-6.3-03"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # Entrambe concernono il certificato del firmatario incluso o rappresentato nella firma AdES/XAdES.
        "nodo_da": ("obbligo", None, "Annex B.1.1 (The scheme operator identifier in XAdES signatures)"),
        "nodo_a": ("obbligo", 11, "Parte 2: OVR-B.1-03"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # Stesso concetto sostanziale: l'estensione ExpiredCertsOnCRL relativa alla revoca dei certificati scaduti, richiesta per le CRL e affine a quella della lista di fiducia.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.1 (expiredCertsRevocationInfo Extension)"),
        "nodo_a": ("obbligo", 15, "par. 4.4 §2"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        # Entrambe trattano l'estensione KeyUsage dei certificati qualificati: A il confronto dei bit, B presenza, criticita' e tipo ammesso.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.2.1 (KeyUsage)"),
        "nodo_a": ("obbligo", 15, "par. 4.1 punto 2"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        # A: PolicySet con identificatori CP da confrontare con l'estensione; B: certificati contenenti certificatePolicies con PolicyIdentifier.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.2.2 (PolicySet)"),
        "nodo_a": ("obbligo", 15, "par. 4.2 punto 4 lett. c"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
    {
        # A confronta identificatori CP con l'estensione; B: certificati di marcatura temporale con estensione certificatePolicies.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.2.2 (PolicySet)"),
        "nodo_a": ("obbligo", 15, "par. 4.2 punto 5 lett. c"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        # Entrambi concernono la gestione delle informazioni di revoca dei certificati scaduti (trattenimento nelle CRL e relativa estensione nella lista di fiducia).
        "nodo_da": ("obbligo", None, "clausola 5.5.9.1 (expiredCertsRevocationInfo Extension)"),
        "nodo_a": ("obbligo", 17, "Parte 2: CSS-6.3.10-04"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # L'estensione expiredCertsRevocationInfo svolge la stessa funzione dell'estensione X.509 ExpiredCertsOnCRL per le informazioni di revoca dei certificati scaduti.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.1 (expiredCertsRevocationInfo Extension)"),
        "nodo_a": ("obbligo", 17, "Parte 2: CSS-6.3.10-05"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        # Entrambe riguardano la revoca/riferimento di revoca di certificati scaduti tramite estensione X.509 (expiredCertsRevocationInfo vs ExpiredCertsOnCRL), senza gerarchia testuale.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.1 (expiredCertsRevocationInfo Extension)"),
        "nodo_a": ("obbligo", 17, "Parte 2: CSS-6.3.10-06"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # A confronta identificatori CP con l'estensione; B definisce quali OID di policy deve contenere il certificato.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.2.2 (PolicySet)"),
        "nodo_a": ("obbligo", 17, "Parte 2: GEN-6.3.3-02"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        # A: qualificatori sullo stato QSCD nel TL; B: qcStatement QSCD nel certificato: stesso concetto, contesti diversi.
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.3 (Qualifier)"),
        "nodo_a": ("obbligo", 17, "Parte 2: GEN-6.6.1-03"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # Entrambe richiedono che i valori temporali siano basati su UTC.
        "nodo_da": ("obbligo", None, "clausola 5.1.3 (Date-time indication)"),
        "nodo_a": ("obbligo", 18, "TIS-7.7.1-04"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
    {
        # Entrambe impongono che i valori temporali facciano riferimento a UTC; contenuto sostanziale condiviso senza gerarchia tra le fonti.
        "nodo_da": ("obbligo", None, "clausola 5.1.3 (Date-time indication)"),
        "nodo_a": ("obbligo", 18, "TIS-7.7.1-05"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.55,
    },
    {
        # Entrambe richiedono valori/clock sincronizzati con UTC.
        "nodo_da": ("obbligo", None, "clausola 5.1.3 (Date-time indication)"),
        "nodo_a": ("obbligo", 18, "TIS-7.7.2-01"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.5,
    },
]


if __name__ == "__main__":
    print(f"OK: {len(RELAZIONI)} relazioni cross-fonte, nessun nodo.")
