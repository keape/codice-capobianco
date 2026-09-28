"""Fase 6 (ADR-0009) di Fonte 12 - Regolamento di esecuzione (UE) 2025/1567.
Capitolo virtuale: solo RELAZIONI cross-fonte, nessun nodo proprio
(RIGHE_OBBLIGHI/RIGHE_PRINCIPI/INDICE_ARTICOLI_LOCALE/MAPPATURA_LOCALE
vuoti), stesso formato di app/seed_data/cad/cap08_relazioni_eidas.py.

Le 12 relazioni *native* dell'atto (base giuridica abilitante, adeguamenti
delle clausole di ETSI TS 119 431-1, rinvio all'art. 24 §5 eIDAS2) vivono in
cap01.py, non qui: sono citazioni letterali del testo dell'atto, non il
prodotto di questa pipeline.

## Pipeline eseguita (2026-09-28, sessione principale)

Stadio 1 - candidati a zero token LLM:
(a) grep sul testo ufficiale (app/.source_cache/reg_ue_2025_1567/raw.txt).
    Citazioni presenti e loro esito: "ETSI TS 119 431-1 V1.3.1" (Fonte 11,
    gia' modellata nativamente in cap01), "ETSI EN 319 401 V3.1.1 (2024-06)"
    (Fonte 10, nativa in cap01 per REQ-7.8-13), "REQ-7.8-13 di ETSI EN 319
    401" (Fonte 10, nativa), "regolamento (UE) n. 910/2014" (artt. 29 bis §2
    e 39 bis, nativi), "regolamento (UE) 2024/1183" (considerando 5),
    "regolamento (UE) 2016/679", "direttiva 2002/58/CE", "regolamento (UE)
    2018/1725", "direttiva 1999/93/CE" (abrogata) e il documento ENISA
    "Agreed Cryptographic Mechanisms" - questi ultimi cinque fuori dal
    censimento, quindi senza nodo controparte (nessuna relazione possibile,
    non una relazione omessa). Zero citazioni di CAD, DPCM 22/2/2013, SPID,
    DPCM 19/10/2021, Regolamento AgID SPID, Regole Tecniche AgID, Reg. (UE)
    2015/1502, Codice Civile o altri standard ETSI.
(b) KNN sull'indice vettoriale HNSW gia' popolato (db.index.vector.queryNodes
    su idxEmbeddingObbligo/idxEmbeddingPrincipio, k=10, soglia 0.75) dei 14
    nodi di Fonte 12 contro tutti i nodi delle altre 20 Fonti. Soglia piu'
    bassa di quella di riferimento (0.80) perche' questo atto e' quasi
    interamente composto di requisiti *tradotti* da ETSI EN 319 401 e di
    adeguamenti di ETSI TS 119 431-1: alzarla avrebbe nascosto proprio le
    corrispondenze da valutare.

Stadio 2 - classificazione sullo shortlist (eseguita inline dall'agente, non
via subagent: su shortlist di questa dimensione l'overhead di dispatch supera
il beneficio, stessa ratio dell'ADR-0009), con lettura del testo reale dei
nodi candidati in Neo4j prima di decidere.

Stadio 3 - validazione: ogni `riferimento` proposto verificato come esistente
in Neo4j (query mirata sui nodi di Fonte 8, 10, 11, 17) prima della scrittura.

## Esito: 8 relazioni cross-fonte validate

Tutte di tipo "si sovrappone a" tranne una, tutte su testo verbatim
confrontato:

1. punto 3 (OVR-6.4.4-02) -> Fonte 10 "REQ-7.2-04" (0.85, textual): l'atto
   riprende letteralmente il requisito EN 319 401 sul personale in ruoli di
   fiducia (conoscenze, esperienza e qualifiche tramite formazione formale o
   esperienza o loro combinazione).
2. punto 3 (OVR-6.4.4-03) -> Fonte 10 "REQ-7.2-05" (0.9, textual):
   aggiornamenti periodici sulle nuove minacce almeno ogni 12 mesi -
   identico intervallo e identico oggetto.
3. punto 2 (OVR-6.1-04) -> Fonte 17 "Parte 1: DIS-6.1-08" (0.7, inferred):
   stessa formula ("le informazioni individuate in <id> sono disponibili al
   pubblico e a livello internazionale") applicata a un insieme informativo
   diverso (SSASP vs. CA); `inferred` perche' la corrispondenza e' nel
   modello della clausola, non in una citazione.
4. punto 4 (OVR-6.4.9-02) -> Fonte 8 "allegato, punto 6 (OVR-7.12-02)" (0.9,
   textual): stesso obbligo ("il piano di cessazione e' conforme agli atti di
   esecuzione adottati a norma dell'art. 24 §5"), ripetuto per due standard
   diversi in due atti di esecuzione distinti.
5. punto 5 (OVR-6.5.5-02) -> Fonte 10 "REQ-7.8-14" (0.9, textual): "la
   scansione delle vulnerabilita' ... almeno una volta al trimestre" e' la
   traduzione di REQ-7.8-14, non un requisito nuovo.
6. punto 5 (OVR-6.5.5-03) -> Fonte 10 "REQ-7.8-22" (0.95, textual):
   configurazione dei firewall per impedire protocolli e accessi non
   necessari - identico.
7. punto 6 (OVR-6.8.5-01) -> Fonte 10 "REQ-7.5-01" (0.85, textual): controlli
   di sicurezza per la gestione delle tecniche crittografiche durante il
   ciclo di vita (REQ-7.5-01 dice "chiavi, algoritmi e dispositivi
   crittografici"). Colma il vuoto segnalato in cap01: la clausola 6.8.5 di
   ETSI TS 119 431-1 non ha nodo nella Fonte 11, ma il requisito da cui
   l'adeguamento deriva esiste in Fonte 10.
8. allegato, chapeau -> Fonte 11 "Parte 1: A.2" (0.85, textual): A.2 dichiara
   la policy OID "EUSPv2: EU SSAS Policy", cioe' esattamente la policy alla
   cui conformita' il chapeau riferisce la valutazione. Relazione distinta da
   quella nativa verso "Parte 1: clausola 1 (Scope)": il chapeau fa due cose
   diverse (designa la norma e fissa l'oggetto della valutazione).

## Proposte valutate e scartate (non silenziose, come da ADR-0009)

- Tutte le coppie di clausole boilerplate emerse dal KNN a score 0.99-1.0:
  "art. 1" contro "art. 1" di altre fonti, "art. 2, entrata in vigore" contro
  "art. 2, entrata in vigore" del Reg. 2025/1566 (score 1.0) e dell'art. 52 §1
  eIDAS, "art. 2, applicazione" contro "art. 2, applicazione" del Reg.
  2025/1566 (0.991) e contro gli artt. 2/52 §2 di altre fonti. Sono formule
  di chiusura identiche senza relazione giuridica reale: stesso falso
  positivo gia' scartato nel giro Fase 6 del Reg. 2025/1566.
- punto 7 (OVR-A.3-02) vs Fonte 17 "Parte 2: SDP-6.5.1-02" (0.90), "Parte 2:
  OVR-6.3.5-01" (0.92); Fonte 7 "Parte 4: QCS-4.2-1" (0.90), "Parte 5:
  QCS-4.1-01" (0.89); Fonte 9 "QTS-C.2.4-07" (0.91): soggetto affine (QSCD
  qualificato) ma contenuto precettivo diverso - SDP-6.5.1-02 impone al TSP
  di *verificare* la certificazione del QSCD, OVR-A.3-02 impone alla
  dichiarazione sulla prassi di *menzionarla*; QCS-4.2-1/QCS-4.1-01
  riguardano i QCStatements nel certificato, non la practice statement.
  Scartate per non forzare un "si sovrappone a" su prescrizioni distinte.
- punto 6 (OVR-6.8.5-01) vs Fonte 10 "REQ-7.6-05", "REQ-7.4.5-01",
  "REQ-7.14.3-07" e Fonte 2 "art. 24 §2(e)": controlli di sicurezza generici
  o requisiti su oggetti diversi, nessuno e' il requisito tradotto.
- punto 5 vs Fonte 10 "REQ-7.8-21" (0.936): requisito contiguo (difesa dei
  domini di rete interni), oggetto diverso da OVR-6.5.5-03 (protocolli e
  accessi non necessari).
- punto 2 vs Fonte 11 "Parte 1: DIS..."-family e "OVR-6.5.3-01A": nessuna
  corrispondenza di contenuto, solo vicinanza nel documento.
- lato Principi: nessuna proposta oltre a quella sul chapeau; il resto dello
  shortlist era boilerplate da atti UE (art. 1 che "designa l'allegato"
  contro l'art. 1 di ogni altro atto).

## Limite noto di questo giro

La Fonte 10 censita e' ETSI EN 319 401 **V3.2.1 (2026-01)**, mentre l'atto
designa e adegua la **V3.1.1 (2024-06)**: i requisiti REQ-7.2-04/-05,
REQ-7.5-01, REQ-7.8-13/-14/-22 qui collegati sono quelli della versione piu'
recente, non quelli della versione vigente al momento dell'adozione dell'atto.
Se una futura riedizione di EN 319 401 rinumerasse o riformulasse quei
requisiti, queste relazioni resterebbero appese a un nodo la cui versione non
e' quella citata dall'atto: da riverificare insieme alla Fonte 10, non
separatamente.
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = []

MAPPATURA_LOCALE = {}

RELAZIONI = [
    # Requisiti di ETSI EN 319 401 (Fonte 10) ripresi dall'atto nella
    # clausola 6.4.4 di ETSI TS 119 431-1.
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3 (OVR-6.4.4-02)'),
        'nodo_a': ('obbligo', 10, 'REQ-7.2-04'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3 (OVR-6.4.4-03)'),
        'nodo_a': ('obbligo', 10, 'REQ-7.2-05'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    # Stessa formula di pubblicazione internazionale delle informazioni, in
    # ETSI EN 319 411-1 (Fonte 17) su un insieme informativo diverso.
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 2 (OVR-6.1-04)'),
        'nodo_a': ('obbligo', 17, 'Parte 1: DIS-6.1-08'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.7,
    },
    # Stesso obbligo sul piano di cessazione, in due atti di esecuzione
    # diversi (Reg. 2025/1566 per ETSI EN 319 401, questo per TS 119 431-1).
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 4 (OVR-6.4.9-02)'),
        'nodo_a': ('obbligo', 8, 'allegato, punto 6 (OVR-7.12-02)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    # Requisiti di sicurezza di rete e crittografici tradotti da EN 319 401.
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 5 (OVR-6.5.5-02)'),
        'nodo_a': ('obbligo', 10, 'REQ-7.8-14'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 5 (OVR-6.5.5-03)'),
        'nodo_a': ('obbligo', 10, 'REQ-7.8-22'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'textual',
        'confidence': 0.95,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 6 (OVR-6.8.5-01)'),
        'nodo_a': ('obbligo', 10, 'REQ-7.5-01'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    # Il chapeau riferisce la valutazione di conformita' alla policy EUSPv2,
    # dichiarata dalla clausola A.2 della norma.
    {
        'nodo_da': ('principio', None, 'allegato, chapeau (norma di riferimento e ambito di applicazione)'),
        'nodo_a': ('principio', 11, 'Parte 1: A.2'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
]
