"""Fase 6 (ADR-0009) di Fonte 28 - Regolamento di esecuzione (UE) 2024/2979
(integrita' e funzionalita' di base dei portafogli europei di identita'
digitale, art. 5 bis §23 eIDAS). Capitolo virtuale: solo RELAZIONI cross-fonte,
nessun nodo proprio (RIGHE_OBBLIGHI/RIGHE_PRINCIPI/INDICE_ARTICOLI_LOCALE/
MAPPATURA_LOCALE vuoti), stesso formato di
app/seed_data/cad/cap08_relazioni_eidas.py.

Le relazioni *interne* di questa Fonte (14: 5 in cap02, 9 in cap03) stanno nei
rispettivi moduli, non qui: sono rinvii tra articoli dello stesso regolamento,
gia' verificati sul testo in fase di autoria per capitolo.

## Pipeline eseguita (2026-09-29, sessione principale)

Stadio 1 - candidati a zero token LLM, nelle due direzioni:

(a) direzione diretta (Fonte nuova -> fonti esistenti), con
    `app/tools/fase6_candidati_knn.py` sui 5 moduli (48 nodi), k=8, soglia
    0.80: 290 coppie candidate dei 45 nodi con almeno un vicino sopra soglia,
    shortlist in app/.source_cache/reg_ue_2024_2979/fase6_candidati.json.
    I rinvii testuali espliciti del regolamento erano gia' stati isolati in
    fase di autoria per capitolo (i docstring di cap01, cap02 e cap03 li
    elencano e li demandano a questa sessione): art. 5 bis §4 eIDAS2 in
    art. 3 §1; regolamento di esecuzione (UE) 2015/1502 in art. 4 §3, art. 5
    §1(b) e §1(g) e art. 13; regolamento di esecuzione (UE) 2024/2980 in
    art. 3 §2; raccomandazione (UE) 2021/946 in art. 1 (considerando e
    art. 1). Fuori dal censimento, quindi senza nodo controparte (nessuna
    relazione possibile, non una relazione omessa): regolamento (UE)
    2024/2980, raccomandazione (UE) 2021/946, GDPR, direttiva 2002/58/CE,
    regolamento (UE) 2018/1725 e le norme tecniche citate negli allegati I
    (GSMA/GlobalPlatform, 7 documenti), II (ISO/IEC 18013-5, W3C VCDM), IV
    (PAdES, XAdES, JAdES, CAdES, ASiC) e V (W3C WebAuthn Level 2).

(b) direzione inversa (fonti esistenti -> Fonte nuova), con query su
    `testo_integrale` in Neo4j: un solo nodo nel grafo cita il regolamento di
    esecuzione (UE) 2024/2979, Fonte 22 "allegato II, punto 1" (richiesta di
    formato degli attestati conforme all'allegato II di questo regolamento).
    Il modulo di Fase 6 di Fonte 22
    (app/seed_data/reg_ue_2025_1569/cap04_relazioni_cross.py) lo dichiarava
    come rinvio senza bersaglio perche' la Fonte non era ancora censita: ora
    il bersaglio esiste.

Stadio 2 - classificazione dello shortlist nella sessione principale (non via
subagent: stessa ratio dell'ADR-0009), leggendo in Neo4j il testo reale delle
controparti prima di decidere.

Stadio 3 - validazione: esistenza e tipo (Obbligo/Principio) di ogni
`riferimento` proposto verificati con query mirata su Neo4j prima della
scrittura.

## Esito: 10 relazioni cross-fonte validate

Testuali, su citazione letterale verificata nel `testo_integrale` del nodo
citante:

1. art. 1 -> Fonte 2 "art. 5 bis §23" (attua, 0.85): base giuridica
   dell'atto - il regolamento di esecuzione e' adottato a norma dell'art. 5
   bis §23 eIDAS2, che conferisce alla Commissione il potere di stabilire il
   quadro tecnico del portafoglio. La citazione e' nell'epigrafe dell'atto
   (fuori dai nodi, che coprono la parte dispositiva): da qui la confidence
   0.85 invece di 0.95, e la nota di provenienza nel campo di questo
   docstring anziche' nel `testo_integrale` di un nodo - stesso trattamento
   della base giuridica abilitante di Fonte 12 (reg_ue_2025_1567/cap01.py).
2. art. 4 §3 -> Fonte 14 "allegato, punto 2.2.1" (richiama, 0.85): "i
   requisiti per le caratteristiche e la progettazione dei mezzi di
   identificazione elettronica a un livello di garanzia elevato stabiliti dal
   regolamento di esecuzione (UE) 2015/1502" - il punto 2.2.1 dell'allegato
   di Fonte 14 e' esattamente la progettazione del mezzo di identificazione
   per i tre livelli di garanzia.
3. art. 5 §1 -> Fonte 14 "allegato, punto 2.2.1" (richiama, 0.85): la stessa
   citazione ripetuta alla lettera b) e alla lettera g) per le applicazioni
   crittografiche sicure.
4. art. 13 -> Fonte 14 "art. 1 §1" (richiama, 0.75): "un livello di garanzia
   elevato di cui al regolamento di esecuzione (UE) 2015/1502" e' un rinvio
   al quadro dei livelli di garanzia nel suo complesso, non a una specifica
   tecnica di progettazione: il bersaglio e' percio' il nodo che istituisce i
   tre livelli (art. 1 §1 di Fonte 14), non il punto 2.2.1 usato per gli
   artt. 4 §3 e 5 §1.
5. Fonte 22 "allegato II, punto 1" -> allegato II (richiama, 0.90):
   direzione inversa. Il nodo di Fonte 22 impone che gli attestati siano
   rilasciati "in un formato conforme a una delle norme di cui all'allegato
   II del regolamento di esecuzione (UE) 2024/2979".

Inferite, su corrispondenza di contenuto (nessuna citazione letterale), tutte
lette e confrontate sulle due parti:

6. art. 10 §1 -> Fonte 2 "art. 5 bis §5(e)" (specifica, 0.75): l'art. 5 bis
   §5(e) prescrive che il portafoglio attui il meccanismo della politica di
   divulgazione incorporata; l'art. 10 §1 e l'allegato III ne danno la
   specifica operativa (le tre politiche: nessuna, solo parti autorizzate,
   root of trust specifica).
7. art. 14 §1 -> Fonte 2 "art. 5 bis §4(b)" (specifica, 0.75): la
   generazione di pseudonimi cifrati e locali prescritta da §4(b) e'
   specificata qui per la generazione (allegato V, W3C WebAuthn Level 2) e
   alla sua variante per parte facente affidamento (art. 14 §2).
8. art. 11 §1 -> Fonte 2 "art. 5 bis §4(e)" (specifica, 0.70): i certificati
   qualificati di firma/sigillo su dispositivi locali, esterni o remoti sono
   l'attuazione della funzionalita' di firma qualificata del portafoglio.
9. art. 9 §1 -> Fonte 2 "art. 5 bis §4(d)" (specifica, 0.70): il registro
   delle transazioni che il portafoglio deve tenere e' il contenuto del
   registro a cui §4(d) da' accesso all'utente tramite il pannello di
   gestione comune.
10. art. 8 -> Fonte 22 "allegato II, punto 1" (si sovrappone a, 0.70):
    entrambe le norme impongono la conformita' alla stessa lista di norme per
    gli attestati elettronici di attributi (allegato II di Fonte 28), ma da
    lati diversi e senza citarsi: Fonte 22 sul fornitore che rilascia
    l'attestato, Fonte 28 sul fornitore del portafoglio che deve poterli
    trattare.

## Proposte valutate e scartate

- **Rinvio ad art. 5 bis §4 eIDAS2 in art. 3 §1**: nessuna relazione, perche'
  Fonte 2 modella l'art. 5 bis §4 per lettere (da §4(a) a §4(g)) senza un nodo
  di chapeau del paragrafo. L'art. 3 §1 rinvia al paragrafo come insieme
  ("nessuna funzionalita' di cui all'articolo 5 bis, paragrafo 4"): agganciarlo
  a una lettera qualsiasi sarebbe arbitrario e sostanzialmente falso (la
  lettera dice una cosa diversa dal paragrafo), quindi il rinvio resta senza
  arco. E' una limitazione di modellazione di Fonte 2, non una relazione
  omessa per svista: se in futuro Fonte 2 ricevesse un nodo di chapeau per il
  §4, la relazione va creata verso quello.
- **Coppie KNN sotto ~0.86 verso Fonte 2, 3, 4, 22**: rumore da linguaggio
  normativo comune (registri, revoca, misure di sicurezza, "informazioni
  necessarie"), verificato leggendo le controparti. Esempi scartati dopo
  lettura: art. 6 §2 -> Fonte 17 "GEN-6.5.2-09" e art. 9 §3 -> Fonte 9
  "ISS-8.5.1-01" (protezione delle chiavi e integrita' delle registrazioni in
  contesti diversi - certificati X.509 e proofing di identita', non
  portafogli); art. 15 -> le clausole di entrata in vigore di Fonte 8/12/23/24
  (0.95-1.00 di similarita' ma puro formulario UE ripetuto, nessuna relazione
  sostanziale); art. 4 §1/§2 -> Fonte 10 "REQ-7.5-01" e Fonte 17
  "SDP-6.5.1-25" (gestione di chiavi e dispositivi crittografici in ambito
  QTSP, istituto diverso dal dispositivo crittografico sicuro del
  portafoglio).
- **Rinvii generici all'art. 8 eIDAS (livelli di garanzia) e al regolamento
  (UE) 2019/881 (EUCC)**: la prima e' materia di Fonte 1/Fonte 14 e passa dai
  richiami testuali gia' registrati; il secondo non e' censito.

## Limite noto

Le relazioni cross-fonte di questa Fonte sono poche rispetto ai 48 nodi,
perche' l'istituto (portafoglio EUDI: integrita', funzionalita' di base,
attestati di unita' di portafoglio, politiche di divulgazione) e' quasi
interamente nuovo nel censimento, che resta orientato a certificati, formati
AdES, marche temporali e identity proofing. Il KNN lo conferma: sotto soglia
0.86 le coppie verso tutte le altre Fonti diventano somiglianza lessicale da
linguaggio normativo UE, non corrispondenza di istituti. Riverificare questo
modulo quando il censimento importera' la famiglia AdES (EN 319 142-1 PAdES,
EN 319 132-1 XAdES, TS 119 182-1 JAdES, EN 319 122-1 CAdES, EN 319 162-1
ASiC): l'allegato IV di questa Fonte nomina quattro di quelle norme come
formati di firma ammessi, e oggi sono l'unico rinvio tecnico di peso rimasto
senza bersaglio.

## Audit delle relazioni `textual` (verifica_relazioni_textual.py, 2026-09-29)

Il giro di controllo su questa Fonte segnala 11 delle sue 17 relazioni
`textual` come prive di traccia del riferimento citato nel `testo_integrale`
del nodo citante. Tutti e 11 i casi sono stati esaminati uno per uno: 7 sono
falsi positivi dello strumento (il testo cita i paragrafi/lettere al plurale o
in forma riassuntiva - "di cui ai paragrafi 1 e 2", "i meccanismi di
autenticazione di cui alla lettera b)", "conforme ai requisiti di cui all'art.
6" - mentre l'estrattore cerca l'ordinale singolare del riferimento bersaglio)
e 4 hanno un bersaglio scelto per contenuto: la base giuridica art. 5 bis §23
(citata nell'epigrafe dell'atto, che non entra in nessun nodo) e i tre richiami
al Reg. 2015/1502 degli artt. 4 §3, 5 §1 e 13, dove il testo nomina il
regolamento senza indicare l'articolo o il punto di allegato agganciato.
Nessuna etichetta gonfiata: nessuna relazione di questa Fonte va declassata a
`inferred` per default. Il caso va invece ricordato in revisione umana, perche'
l'audit lo riproporra' a ogni rilancio finche' questa nota non sara' nella
scheda della Fonte in docs/fonti-censite.md (dove e').
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = []

MAPPATURA_LOCALE = {}

RELAZIONI = [
    # --- Fonte 2 (eIDAS2, Reg. (UE) 2024/1183) ----------------------------
    {
        "nodo_da": ("principio", None, "art. 1"),
        "nodo_a": ("principio", 2, "art. 5 bis §23"),
        "tipo_relazione": "attua",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", None, "art. 10 §1"),
        "nodo_a": ("obbligo", 2, "art. 5 bis §5(e)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, "art. 11 §1"),
        "nodo_a": ("obbligo", 2, "art. 5 bis §4(e)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.70,
    },
    {
        "nodo_da": ("obbligo", None, "art. 14 §1"),
        "nodo_a": ("obbligo", 2, "art. 5 bis §4(b)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 §1"),
        "nodo_a": ("obbligo", 2, "art. 5 bis §4(d)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.70,
    },
    # --- Fonte 14 (Reg. di esecuzione (UE) 2015/1502, livelli di garanzia) -
    {
        "nodo_da": ("obbligo", None, "art. 4 §3"),
        "nodo_a": ("obbligo", 14, "allegato, punto 2.2.1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", None, "art. 5 §1"),
        "nodo_a": ("obbligo", 14, "allegato, punto 2.2.1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", None, "art. 13"),
        "nodo_a": ("principio", 14, "art. 1 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    # --- Fonte 22 (Reg. di esecuzione (UE) 2025/1569, attestati) ----------
    {
        "nodo_da": ("obbligo", 22, "allegato II, punto 1"),
        "nodo_a": ("principio", None, "allegato II"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("obbligo", None, "art. 8"),
        "nodo_a": ("obbligo", 22, "allegato II, punto 1"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.70,
    },
]
