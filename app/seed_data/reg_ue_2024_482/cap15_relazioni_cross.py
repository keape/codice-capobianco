"""Fase 6 (ADR-0009) di Fonte 29 - Regolamento di esecuzione (UE) 2024/482
(EUCC, sistema europeo di certificazione della cibersicurezza basato sui
criteri comuni). Capitolo virtuale: solo RELAZIONI, nessun nodo proprio
(`RIGHE_OBBLIGHI`/`RIGHE_PRINCIPI`/`INDICE_ARTICOLI_LOCALE`/`MAPPATURA_LOCALE`
vuoti), stesso formato di app/seed_data/cad/cap08_relazioni_eidas.py.

Le relazioni *interne* di ciascun capitolo (86 in totale, tutte fra righe dello
stesso modulo) stanno nei moduli cap01-cap14, non qui.

## Pipeline eseguita (2026-09-29, sessione principale)

Stadio 1 - candidati a zero token LLM:

(a) direzione diretta (Fonte nuova -> fonti esistenti), con
    `app/tools/fase6_candidati_knn.py` sui 14 moduli (196 nodi), k=8, soglia
    0.84: 1.220 coppie candidate, shortlist in
    app/.source_cache/reg_ue_2024_482/fase6_candidati.json. Esito della
    lettura: sotto 0.92 le coppie sono somiglianza di linguaggio normativo UE
    (atti di certificazione, autorita', revoca, registri), non corrispondenza
    di istituti - l'EUCC certifica *prodotti TIC*, mentre il corpus censito e'
    fatto di servizi fiduciari, certificati X.509, formati AdES, marche
    temporali e identity proofing. I candidati a score pieno (0.99-1.00) sono
    le clausole di entrata in vigore/applicazione differita, gia' scartate per
    convenzione negli altri giri di Fase 6.

(b) direzione inversa (fonti esistenti -> Fonte nuova), con query su
    `testo_integrale` in Neo4j per "2024/482" e "2024/3144": tre nodi, tutti
    in Fonti 23 e 24. Due sono voci di un elenco bibliografico ("riferimenti
    normativi" dei regg. 2025/2531 e 2025/2532) e restano senza arco, come da
    convenzione del progetto per i rinvii puramente bibliografici (Fonte 25,
    Fonte 17 Parte 1 clausola 2.2). Il terzo e' qui sotto.

(c) direzione cross-capitolo (dentro la stessa Fonte), con un estrattore
    meccanico delle citazioni letterali nel `testo_integrale` di ogni riga,
    risolte contro l'indice dei riferimenti della Fonte.

    **Regola di miraggio (ADR-0012)**: una citazione che nomina il paragrafo
    ("il riesame e' effettuato applicando le condizioni di cui all'articolo 15,
    paragrafo 2") va al **nodo di quel comma**; una citazione dell'articolo o
    dell'allegato **in blocco** ("in conformita' degli articoli 13 e 19", "si
    applica l'allegato IV") va alla **partizione** di quell'unita' indivisa.
    Prima dell'ADR-0012 questo secondo caso non aveva bersaglio: gli archi
    venivano ancorati a un comma scelto con una soglia arbitraria ("articoli con
    al piu' 3 commi", 81 archi) e 51 rinvii restavano senza arco. Con le
    partizioni quei 51 sono stati creati e i bersagli arbitrari sono stati
    sostituiti dalla partizione: **130 relazioni verso partizioni** e
    **9 verso nodi di comma** (queste ultime su citazione di paragrafo
    esplicita), 143 in totale con le quattro cross-fonte.

Stadio 2 - classificazione nella sessione principale (mai a subagent, stessa
ratio dell'ADR-0009), leggendo le controparti in Neo4j prima di decidere.

Stadio 3 - validazione: esistenza e tipo (Obbligo/Principio/Partizione) di ogni
`riferimento` proposto verificati prima della scrittura; i bersagli a
partizione sono verificabili sui moduli con `neo4j_common.partizioni_di`, quelli
a comma contro l'indice della Fonte.

## Esito: 143 relazioni

Cross-fonte (4):

1. art. 3 -> Fonte 1 "art. 30 §3" (si sovrappone a, inferred, 0.70): entrambe
   le disposizioni designano i criteri comuni (ISO/IEC 15408 / CC) come base
   della certificazione di sicurezza di un prodotto - in eIDAS la
   certificazione dei dispositivi per la creazione di firma qualificata da
   parte dell'organismo designato (con l'elenco di norme adottato dalla
   Commissione, decisione 2016/650), nell'EUCC la certificazione dei prodotti
   TIC. Nessuna delle due cita l'altra: la relazione e' di contenuto.
2. art. 5 quater §2 eIDAS2 -> art. 1 (richiama, inferred, 0.65): eIDAS2 impone
   che la conformita' del portafoglio europeo di identita' digitale sia
   certificata "in conformita' dei sistemi europei di certificazione della
   cibersicurezza" del regolamento (UE) 2019/881; l'EUCC e' uno di quei
   sistemi. Il testo cita la categoria, non l'atto: da qui `inferred` e una
   confidence prudente. Bersaglio: art. 1 (oggetto e ambito), perche' e' la
   riga che istituisce il sistema.
3. art. 12-bis §2 eIDAS2 -> art. 1 (richiama, inferred, 0.65): stessa
   fattispecie per la certificazione dei regimi di identificazione elettronica
   da notificare.
4. Fonte 24 "allegato, adeguamento e) controlli e monitoraggio crittografici"
   -> art. 1 (richiama, textual, 0.85): direzione inversa. Il punto impone
   all'EATSP che la chiave di firma sia custodita in un dispositivo
   crittografico sicuro certificato "al sistema europeo di certificazione
   della cibersicurezza basato sui criteri comuni (regolamento (UE) 2024/482,
   regolamento (UE) 2024/3144)". La menzione del regolamento (UE) 2024/3144
   nello stesso nodo non genera un arco verso Fonte 30: l'atto modificativo
   non aggiunge nulla ai requisiti di certificazione a cui il nodo rinvia.

Cross-capitolo e partizioni (130 + 9): tutte "richiama"
`textual` con confidence 0.80, su citazione letterale verificata nel testo della
riga citante. Il bersaglio piu' frequente e' la partizione dell'art. 3 ("norme di
valutazione": criteri comuni e metodologia comune), che e' la norma di
riferimento dell'intero regolamento e l'articolo piu' citato: vi rinvia buona
parte dei capitoli degli allegati (relazione di certificazione, valutazione
inter pares, dichiarazione del pacchetto di affidabilita'). Fra le partizioni
bersaglio compaiono anche i sei allegati richiamati dagli articoli (allegato I,
II, IV, V, VI, VII) e le loro sezioni (allegato IV, sezione IV.2).

## Rinvii lasciati senza relazione (dichiarati, non omessi per svista)

- Norme esterne non censite, citate dall'atto: regolamento (UE) 2019/881
  (artt. 49, 51-52, 53, 55, 56, 57, 58, 59 §3(d), 60 §1, 61 §4 e allegato),
  regolamento (CE) n. 765/2008, regolamento (UE) 2019/1020, ISO/IEC 15408 e
  18045, regolamento di esecuzione (UE) 2016/799, regolamento (UE) n. 165/2014,
  regolamento (CE) n. 1360/2002, direttiva (UE) 2022/2555, EN ISO/IEC 30111,
  decisione di esecuzione (UE) 2016/650. Nessuna ha un nodo controparte: sono
  rinvii a norme fuori dal censimento, non relazioni omesse.
- Voci bibliografiche e "documenti sullo stato dell'arte" designati dagli
  allegati (profili di protezione BSI/ANSSI, GlobalPlatform, GSMA, W3C):
  elenchi di documenti, non disposizioni con bersaglio puntuale.
- Gruppo europeo per la certificazione della cibersicurezza ed ENISA: organi
  nominati da molte righe, non nodi del censimento.

## Limite noto

L'EUCC e' la prima Fonte del censimento che non riguarda servizi fiduciari ma
*certificazione di prodotti TIC*: il collegamento al resto del grafo passa per
tre soli archi (due da eIDAS2, uno verso eIDAS) piu' un rinvio inverso da
Fonte 24. Non e' un esito per difetto: e' la conseguenza di un perimetro
diverso. Riverificare questo modulo quando il censimento importera' i
regolamenti di esecuzione (UE) 2024/3143 (notifiche degli organismi di
valutazione della conformita': l'art. 1, punto 4 di Fonte 30 sopprime gli
artt. 23-24 proprio in vista di quell'atto).
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = []

MAPPATURA_LOCALE = {}

RELAZIONI = []

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = []

MAPPATURA_LOCALE = {}

RELAZIONI = [
    # --- cross-fonte -----------------------------------------------------
    {
        "nodo_da": ("principio", None, "art. 3"),
        "nodo_a": ("obbligo", 1, "art. 30 §3"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.70,
    },
    {
        "nodo_da": ("principio", 2, "art. 5 quater §2"),
        "nodo_a": ("principio", None, "art. 1"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": 0.65,
    },
    {
        "nodo_da": ("principio", 2, "art. 12-bis §2"),
        "nodo_a": ("principio", None, "art. 1"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": 0.65,
    },
    {
        "nodo_da": ("obbligo", 24, "allegato, adeguamento e) controlli e monitoraggio crittografici"),
        "nodo_a": ("principio", None, "art. 1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },

    # --- cross-capitolo e verso le partizioni (ADR-0012) ------------------
    # Citazione con paragrafo -> nodo di quel comma; citazione dell'articolo o
    # dell'allegato "in blocco" -> partizione (art. N, allegato N[, sezione S]).
    {
        "nodo_da": ("obbligo", None, "art. 4 §1"),
        "nodo_a": ("partizione", None, "art. 4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 5 §1"),
        "nodo_a": ("partizione", None, "art. 5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 2"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 4 §4"),
        "nodo_a": ("partizione", None, "allegato VIII"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 §1"),
        "nodo_a": ("partizione", None, "art. 7"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 §1"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 §1"),
        "nodo_a": ("partizione", None, "allegato I"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 §1"),
        "nodo_a": ("partizione", None, "allegato II"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 §3"),
        "nodo_a": ("partizione", None, "allegato I"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 §3"),
        "nodo_a": ("partizione", None, "allegato II"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 8 §1"),
        "nodo_a": ("partizione", None, "art. 8"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 §1"),
        "nodo_a": ("partizione", None, "art. 9"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 §1"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 §1"),
        "nodo_a": ("partizione", None, "art. 7"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 §2"),
        "nodo_a": ("partizione", None, "art. 11"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 10 §1"),
        "nodo_a": ("partizione", None, "art. 10"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 10 §1"),
        "nodo_a": ("partizione", None, "allegato VII"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 10 §4"),
        "nodo_a": ("partizione", None, "art. 7"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 10 §4"),
        "nodo_a": ("partizione", None, "allegato V"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 11 §3"),
        "nodo_a": ("partizione", None, "allegato IX"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 11 §4"),
        "nodo_a": ("partizione", None, "allegato V"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 12 §1"),
        "nodo_a": ("partizione", None, "art. 12"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 13 §1"),
        "nodo_a": ("partizione", None, "art. 13"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 13 §1"),
        "nodo_a": ("partizione", None, "allegato IV"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 13 §2"),
        "nodo_a": ("partizione", None, "art. 14"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 14 §1"),
        "nodo_a": ("partizione", None, "art. 14"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 14 §2"),
        "nodo_a": ("partizione", None, "art. 50"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 8 §3"),
        "nodo_a": ("partizione", None, "art. 49"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 11 §1"),
        "nodo_a": ("partizione", None, "art. 11"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 11 §1"),
        "nodo_a": ("partizione", None, "allegato IX"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 13 §3"),
        "nodo_a": ("partizione", None, "art. 30"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 15 §1"),
        "nodo_a": ("partizione", None, "art. 15"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 15 §1"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 15 §1"),
        "nodo_a": ("partizione", None, "allegato I"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 16"),
        "nodo_a": ("obbligo", None, "art. 8 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 17 §1"),
        "nodo_a": ("partizione", None, "art. 17"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 18 §1"),
        "nodo_a": ("partizione", None, "art. 18"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 19 §1"),
        "nodo_a": ("partizione", None, "art. 19"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 19 §1"),
        "nodo_a": ("partizione", None, "art. 15"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 19 §2"),
        "nodo_a": ("partizione", None, "art. 20"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 20 §1"),
        "nodo_a": ("partizione", None, "art. 20"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 20 §1"),
        "nodo_a": ("partizione", None, "art. 14"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 17 §2"),
        "nodo_a": ("partizione", None, "art. 9"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 17 §2"),
        "nodo_a": ("partizione", None, "art. 10"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 21 §1"),
        "nodo_a": ("partizione", None, "art. 21"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 21 §1"),
        "nodo_a": ("partizione", None, "art. 22"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 21 §1"),
        "nodo_a": ("partizione", None, "art. 43"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 21 §2"),
        "nodo_a": ("partizione", None, "art. 49"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 22 §1"),
        "nodo_a": ("partizione", None, "art. 22"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 22 §1"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 22 §1"),
        "nodo_a": ("partizione", None, "art. 43"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 22 §1"),
        "nodo_a": ("partizione", None, "allegato I"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 22 §3"),
        "nodo_a": ("partizione", None, "art. 49"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 23 §1"),
        "nodo_a": ("partizione", None, "art. 23"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 24"),
        "nodo_a": ("partizione", None, "art. 23"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 25 §1"),
        "nodo_a": ("partizione", None, "art. 25"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 25 §6"),
        "nodo_a": ("partizione", None, "allegato IV, sezione IV.2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 26 §1"),
        "nodo_a": ("partizione", None, "art. 26"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 26 §2"),
        "nodo_a": ("obbligo", None, "art. 9 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 27 §1"),
        "nodo_a": ("partizione", None, "art. 27"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §1"),
        "nodo_a": ("partizione", None, "art. 28"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §5"),
        "nodo_a": ("partizione", None, "art. 13"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §5"),
        "nodo_a": ("partizione", None, "art. 19"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §6"),
        "nodo_a": ("partizione", None, "art. 30"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §6"),
        "nodo_a": ("partizione", None, "art. 14"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §1"),
        "nodo_a": ("partizione", None, "art. 29"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §1"),
        "nodo_a": ("obbligo", None, "art. 9 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §1"),
        "nodo_a": ("principio", None, "art. 17 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §1"),
        "nodo_a": ("partizione", None, "art. 27"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §1"),
        "nodo_a": ("partizione", None, "art. 41"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §2"),
        "nodo_a": ("partizione", None, "art. 30"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §2"),
        "nodo_a": ("partizione", None, "art. 14"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §2"),
        "nodo_a": ("partizione", None, "art. 20"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §3"),
        "nodo_a": ("partizione", None, "art. 14"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §3"),
        "nodo_a": ("partizione", None, "art. 20"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 30 §1"),
        "nodo_a": ("partizione", None, "art. 30"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 30 §5"),
        "nodo_a": ("obbligo", None, "art. 42 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 31 §1"),
        "nodo_a": ("partizione", None, "art. 31"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 31 §2"),
        "nodo_a": ("partizione", None, "art. 14"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 31 §2"),
        "nodo_a": ("partizione", None, "art. 20"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 26 §3"),
        "nodo_a": ("obbligo", None, "art. 9 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 28 §4"),
        "nodo_a": ("partizione", None, "art. 30"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 33 §1"),
        "nodo_a": ("partizione", None, "art. 33"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 34 §1"),
        "nodo_a": ("partizione", None, "art. 34"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 34 §2"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 34 §2"),
        "nodo_a": ("partizione", None, "allegato I"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 35 §1"),
        "nodo_a": ("partizione", None, "art. 35"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 35 §6"),
        "nodo_a": ("partizione", None, "art. 14"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 36"),
        "nodo_a": ("partizione", None, "art. 13"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 37 §1"),
        "nodo_a": ("partizione", None, "art. 37"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 38 §1"),
        "nodo_a": ("partizione", None, "art. 38"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 38 §1"),
        "nodo_a": ("partizione", None, "art. 37"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 39"),
        "nodo_a": ("partizione", None, "art. 12"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 35 §5"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 40 §1"),
        "nodo_a": ("partizione", None, "art. 40"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 40 §2"),
        "nodo_a": ("obbligo", None, "art. 13 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 41 §1"),
        "nodo_a": ("partizione", None, "art. 41"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 41 §3"),
        "nodo_a": ("obbligo", None, "art. 13 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 42 §1"),
        "nodo_a": ("partizione", None, "art. 42"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 42 §1"),
        "nodo_a": ("partizione", None, "art. 50"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 42 §1"),
        "nodo_a": ("partizione", None, "art. 47"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 42 §1"),
        "nodo_a": ("partizione", None, "allegato I"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 44 §1"),
        "nodo_a": ("partizione", None, "art. 44"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 44 §3"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 44 §3"),
        "nodo_a": ("partizione", None, "allegato I"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 45 §1"),
        "nodo_a": ("partizione", None, "art. 45"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 45 §1"),
        "nodo_a": ("partizione", None, "allegato VI"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 45 §3"),
        "nodo_a": ("partizione", None, "art. 47"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 46 §1"),
        "nodo_a": ("partizione", None, "art. 46"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 47 §1"),
        "nodo_a": ("partizione", None, "art. 47"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 45 §6"),
        "nodo_a": ("partizione", None, "allegato VI"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 48 §1"),
        "nodo_a": ("partizione", None, "art. 48"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 49 §1"),
        "nodo_a": ("partizione", None, "art. 49"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 49 §2"),
        "nodo_a": ("partizione", None, "art. 50"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 50, entrata in vigore"),
        "nodo_a": ("partizione", None, "art. 50"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 50, applicazione"),
        "nodo_a": ("partizione", None, "allegato V"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "allegato III"),
        "nodo_a": ("partizione", None, "allegato I"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "allegato III, lettera c)"),
        "nodo_a": ("partizione", None, "allegato I"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato IV, sezione IV.2, punto 4"),
        "nodo_a": ("partizione", None, "art. 13"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "allegato IV, sezione IV.4, punto 3"),
        "nodo_a": ("partizione", None, "art. 13"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato V, sezione V.1, punto 4"),
        "nodo_a": ("partizione", None, "allegato IV, sezione IV.4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato V, sezione V.1, punto 9"),
        "nodo_a": ("obbligo", None, "art. 7 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato V, sezione V.1, punto 13"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato V, sezione V.1, punto 14"),
        "nodo_a": ("partizione", None, "art. 4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato V, sezione V.1, punto 14"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato V, sezione V.2, punto 3"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato V, sezione V.2, punto 4"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "allegato V, sezione V.1, punto 17"),
        "nodo_a": ("partizione", None, "art. 11"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VI, sezione VI.2, punto 1"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VII, lettera c)"),
        "nodo_a": ("partizione", None, "art. 4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VII, lettera c)"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VII, lettera c)"),
        "nodo_a": ("partizione", None, "allegato V"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VII, lettera c)"),
        "nodo_a": ("partizione", None, "allegato VIII"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VII, lettera d)"),
        "nodo_a": ("partizione", None, "art. 11"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VIII, punto 1"),
        "nodo_a": ("partizione", None, "allegato VIII"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "allegato VI, sezione VI.1, punto 1"),
        "nodo_a": ("partizione", None, "allegato VI"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "allegato VI, sezione VI.1, punto 1"),
        "nodo_a": ("partizione", None, "allegato I"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "allegato VI, sezione VI.1, punto 1"),
        "nodo_a": ("partizione", None, "allegato II"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "allegato VIII, punto 2"),
        "nodo_a": ("partizione", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
]
