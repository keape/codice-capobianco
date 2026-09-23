"""Estrazione granulare ETSI TS 119 461 V2.1.1 (2025-02) — clausola 6 "Policies
and practices" e clausola 7 "Identity proofing service management and
operation" (14 sottoclausole 7.1-7.14, mutuate dalla struttura ISMS di ETSI
EN 319 401).

Fonte 9 (sarà cablata nel wiring finale da un'altra sessione).
Testo ufficiale: app/.source_cache/etsi_119_461/cap03.txt.

Modellazione (ADR-0007), stesso genere di fonte di ETSI EN 319 412-5/Fonte 7
(standard tecnico ETSI a clausole/requisiti numerati, non atto legislativo ad
articoli/commi):

- Ogni requisito con id proprio (prefisso "OVR-", famiglia "Overall
  requirements" per le clausole 6/7 secondo la legenda di clausola 3.4) ->
  un nodo Obbligo, `riferimento` = id esatto come appare nel testo (es.
  "OVR-6.1-02"). Nessuna sottoclausola di questo capitolo ha contenuto
  sostanziale privo di id di requisito (a differenza di ETSI 319 412-5, qui
  ogni sottoclausola apre direttamente con un **OVR-x.y-NN:** senza premessa
  descrittiva autonoma) -> nessun nodo Principio "clausola X.Y" in questo
  capitolo.
- Tutte le 22 righe sono Obbligo, non Principio: anche i requisiti che si
  limitano a rinviare a un'intera clausola di ETSI EN 319 401 (es. "The
  requirements specified in ETSI EN 319 401 [1], clause 7.1 shall apply")
  impongono comunque un comportamento vincolante all'IPSP — l'applicazione
  di quel corpo di requisiti in questo contesto — quindi sono un Obbligo a
  tutti gli effetti, non un mero principio descrittivo. ETSI EN 319 401 è
  citata come riferimento normativo [1] ma non è (ancora) una Fonte separata
  di questo censimento: nessuna relazione viene creata verso di essa (nessun
  nodo esiste a cui collegarsi), il rinvio resta descritto nel testo del
  nodo.
- categoria_soggetto: "QTSP/gestore" per tutti i 22 requisiti (soggetto
  obbligato è sempre l'IPSP, esplicitamente definito dal documento come
  "componente" del TSP ai fini di questo censimento).
- tipo_obbligo: "organizzativo" per default (policy, gestione interna,
  risorse umane, asset, controllo accessi, sicurezza fisica, continuità
  operativa, cessazione, conformità, supply chain — tutte materie di
  governance/ISMS anche quando il testo rinvia a un intero corpo di
  requisiti EN 319 401), salvo le due sottoclausole esplicitamente tecniche
  indicate nell'assegnazione: 7.5 "Cryptographic controls" e 7.8 "Network
  security" -> "tecnico/sicurezza".
- NOTE annesse ai requisiti non generano mai un nodo/item di indice a sé:
  quando aggiungono un'eccezione, un'estensione di ambito o un chiarimento
  sostanziale sull'adempimento dell'obbligo (es. NOTE 1 sotto OVR-6.1-02:
  possibilità di non avere una practice statement separata quando TSP e
  IPSP coincidono; NOTE sotto OVR-6.2-01: rapporto con i T&C del servizio
  fiduciario; NOTE 1/NOTE 2 sotto OVR-7.10-01: chi può adempiere alla
  conservazione a lungo termine delle prove, ed estensione ai requisiti
  della clausola 8.5.2; NOTE sotto OVR-7.12-01: possibilità di assistenza
  reciproca/unilaterale IPSP/TSP nei piani di cessazione) il loro contenuto
  è assorbito nel `testo`/`testo_integrale` del nodo a cui sono annesse.
  Quando sono mera esemplificazione (NOTE "E.g. separated from office
  support systems" sotto OVR-7.8-02; EXAMPLE "Reporting to the supervisory
  authority..." sotto OVR-7.9-02; NOTE 2 sotto OVR-6.1-03 sui casi d'uso
  tipicamente supportati) sono scartate, senza impatto sul contenuto
  normativo del requisito.
- OVR-6.1-03 (id di requisito) non va confuso con NOTE 2 annessa: l'id del
  requisito resta univoco e "pulito", solo il contenuto della NOTE è escluso
  per genuina irrilevanza normativa (mero commento su prassi tipica, non
  un'eccezione/condizione).
- OVR-7.10-01: la NOTE 2 ("The requirements of clause 8.5.2 of the present
  document apply") è assorbita nel testo del nodo come chiarimento
  sostanziale, ma NON genera una relazione "richiama" verso un id preciso:
  "clausola 8.5.2" è un rimando all'intera sottoclausola (verosimilmente
  coperta da un capitolo diverso di questo stesso import, con propri id di
  requisito distinti tipo "ISS-8.5.2-xx"), non un id di requisito singolo
  verificabile testualmente — per evitare un riferimento inventato la
  relazione viene omessa, come da istruzione esplicita in caso di dubbio.
- OVR-7.12-01 è esplicitamente uno degli unici requisiti di questo capitolo
  con un'esclusione di ambito testuale ("excluding REQ-7.12-11"): riportata
  nel testo del nodo, non modellata come `condizione_applicabilita` (non è
  una condizione di applicabilità del requisito, ma una restrizione fissa e
  permanente del suo perimetro rispetto al corpo di requisiti richiamato).
- Nessuna relazione interna (RELAZIONI vuoto): gli unici rimandi testuali
  espliciti in questo capitolo puntano a clausole/requisiti di ETSI EN 319
  401 (non modellata come Fonte) o a "clausola 8.5.2 del presente
  documento" (rimando di sottoclausola, non di id di requisito preciso, per
  cui l'istruzione impone di omettere piuttosto che rischiare un
  riferimento inventato) — nessun rimando testuale a un id di requisito
  esatto di un ALTRO capitolo di questo stesso documento è presente nel
  testo di clausola 6/7.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "OVR-6.1-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 6.1 (dichiarazione delle pratiche del servizio di identity proofing).",
        "testo_integrale": "OVR-6.1-01: The requirements specified in ETSI EN 319 401 [1], clause 6.1 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.1-02",
        "testo": "L'IPSP che dichiara la conformità al presente documento deve identificare nella propria dichiarazione delle pratiche (practice statement) i casi d'uso per cui la conformità è dichiarata; quando l'identity proofing è svolto dallo stesso TSP, la dichiarazione delle pratiche del TSP può coprire tale informazione senza necessità di un documento separato.",
        "testo_integrale": "OVR-6.1-02: An IPSP claiming compliance with the present document shall identify in its practice statement the use cases for which compliance is claimed. NOTE 1: When the identity proofing is done by the TSP itself, the TSP's practice statement can cover the information on the identity proofing and there is no need for a specific practice statement for identity proofing.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.1-03",
        "testo": "L'identificazione dei casi d'uso per cui la conformità è dichiarata deve avvenire per riferimento a parti specifiche della clausola 9 e/o dell'Allegato C del presente documento.",
        "testo_integrale": "OVR-6.1-03: Identification of use cases for which compliance is claimed shall be by reference to specific parts of clause 9 and/or Annex C of the present document.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 6.2 (termini e condizioni); i termini e le condizioni per l'identity proofing possono essere parte dei termini e condizioni d'uso del servizio fiduciario per cui l'identity proofing è svolto.",
        "testo_integrale": "OVR-6.2-01: The requirements specified in ETSI EN 319 401 [1], clause 6.2 shall apply. NOTE: Terms and conditions for identity proofing can be part of the terms and conditions for use of the trust service for which the identity proofing is done.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.3-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 6.3 (politica di sicurezza delle informazioni).",
        "testo_integrale": "OVR-6.3-01: The requirements specified in ETSI EN 319 401 [1], clause 6.3 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.1-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 7.1 (organizzazione interna).",
        "testo_integrale": "OVR-7.1-01: The requirements specified in ETSI EN 319 401 [1], clause 7.1 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.2-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 7.2 (risorse umane).",
        "testo_integrale": "OVR-7.2-01: The requirements specified in ETSI EN 319 401 [1], clause 7.2 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.3-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 7.3 (gestione degli asset).",
        "testo_integrale": "OVR-7.3-01: The requirements specified in ETSI EN 319 401 [1], clause 7.3 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.4-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 7.4 (controllo degli accessi).",
        "testo_integrale": "OVR-7.4-01: The requirements specified in ETSI EN 319 401 [1], clause 7.4 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.5-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 7.5 (controlli crittografici).",
        "testo_integrale": "OVR-7.5-01: The requirements specified in ETSI EN 319 401 [1], clause 7.5 shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.6-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 7.6 (sicurezza fisica e ambientale).",
        "testo_integrale": "OVR-7.6-01: The requirements specified in ETSI EN 319 401 [1], clause 7.6 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.7-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 7.7 (sicurezza operativa).",
        "testo_integrale": "OVR-7.7-01: The requirements specified in ETSI EN 319 401 [1], clause 7.7 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.8-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 7.8 (sicurezza di rete).",
        "testo_integrale": "OVR-7.8-01: The requirements specified in ETSI EN 319 401 [1], clause 7.8 shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.8-02",
        "testo": "Il sistema informativo che assume la decisione di identity proofing deve essere separato, logicamente o fisicamente, dai sistemi informativi non critici dell'IPSP.",
        "testo_integrale": "OVR-7.8-02: The information system making the identity proofing decision shall be logically or physically separated from non-critical information systems at the IPSP.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.9-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 7.9 (gestione delle vulnerabilità e degli incidenti).",
        "testo_integrale": "OVR-7.9-01: The requirements specified in ETSI EN 319 401 [1], clause 7.9 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.9-02",
        "testo": "Gli obblighi di segnalazione previsti da ETSI EN 319 401, REQ-7.9.2-02X e clausola 7.9.3, devono essere adempiuti secondo quanto richiesto dal contesto dell'identity proofing e dagli obblighi dei TSP che si avvalgono del servizio dell'IPSP.",
        "testo_integrale": "OVR-7.9-02: Reporting obligations according to ETSI EN 319 401 [1] REQ-7.9.2-02X and clause 7.9.3 shall be fulfilled as required by the identity proofing context and the obligations of the TSPs relying on the IPSP's service.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.10-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 7.10 (raccolta delle prove); i requisiti di conservazione a lungo termine delle prove possono essere adempiuti dal TSP richiedente l'identity proofing anziché dall'IPSP quando TSP e IPSP sono entità distinte; si applicano inoltre i requisiti della clausola 8.5.2 del presente documento.",
        "testo_integrale": "OVR-7.10-01: The requirements specified in ETSI EN 319 401 [1], clause 7.10 shall apply. NOTE 1: Long-term requirements for retention of evidence can be fulfilled by the TSP requesting the identity proofing instead of by the IPSP when the TSP and the IPSP are different entities. NOTE 2: The requirements of clause 8.5.2 of the present document apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.11-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 7.11 (gestione della continuità operativa).",
        "testo_integrale": "OVR-7.11-01: The requirements specified in ETSI EN 319 401 [1], clause 7.11 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.11-02",
        "testo": "I processi di gestione delle crisi secondo ETSI EN 319 401, REQ-7.11.3-01X, devono essere conformi a quanto richiesto dal contesto dell'identity proofing e dagli obblighi dei TSP che si avvalgono del servizio dell'IPSP.",
        "testo_integrale": "OVR-7.11-02: Processes for crisis management according to ETSI EN 319 401 [1], REQ-7.11.3-01X shall be as required by the identity proofing context and the obligations of the TSPs relying on the IPSP's service.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.12-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 7.12 (cessazione e piani di cessazione), con l'esclusione del requisito REQ-7.12-11; quando l'IPSP e il TSP richiedente l'identity proofing sono entità distinte, possono concordare assistenza reciproca o unilaterale nella predisposizione dei piani di cessazione.",
        "testo_integrale": "OVR-7.12-01: The requirements specified in ETSI EN 319 401 [1], clause 7.12, excluding REQ-7.12-11, shall apply. NOTE: When the IPSP and the TSP requesting the identity proofing are different entities, they can agree mutual or unilateral assistance in establishing termination plans.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.13-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 7.13 (conformità).",
        "testo_integrale": "OVR-7.13-01: The requirements specified in ETSI EN 319 401 [1], clause 7.13 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.14-01",
        "testo": "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 7.14 (catena di fornitura).",
        "testo_integrale": "OVR-7.14-01: The requirements specified in ETSI EN 319 401 [1], clause 7.14 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = []

INDICE_ARTICOLI_LOCALE: list[str] = [
    "OVR-6.1-01",
    "OVR-6.1-02",
    "OVR-6.1-03",
    "OVR-6.2-01",
    "OVR-6.3-01",
    "OVR-7.1-01",
    "OVR-7.2-01",
    "OVR-7.3-01",
    "OVR-7.4-01",
    "OVR-7.5-01",
    "OVR-7.6-01",
    "OVR-7.7-01",
    "OVR-7.8-01",
    "OVR-7.8-02",
    "OVR-7.9-01",
    "OVR-7.9-02",
    "OVR-7.10-01",
    "OVR-7.11-01",
    "OVR-7.11-02",
    "OVR-7.12-01",
    "OVR-7.13-01",
    "OVR-7.14-01",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
