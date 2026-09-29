"""Fase 6 (ADR-0009) di Fonte 29 - Regolamento di esecuzione (UE) 2024/482
(EUCC, sistema europeo di certificazione della cibersicurezza basato sui
criteri comuni). Capitolo virtuale: solo RELAZIONI, nessun nodo proprio
(`RIGHE_OBBLIGHI`/`RIGHE_PRINCIPI`/`INDICE_ARTICOLI_LOCALE`/`MAPPATURA_LOCALE`
vuoti), stesso formato di app/seed_data/cad/cap08_relazioni_eidas.py.

Le relazioni *interne* di ciascun capitolo (86 in totale, tutte fra righe dello
stesso modulo) stanno nei moduli cap01-cap14, non qui.

## Pipeline eseguita (2026-09-29, sessione principale)

Stadio 1 - candidati a zero token LLM, nelle due direzioni:

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
    Fonte 17 Parte 1 clausola 2.2): non indicano una disposizione puntuale ne'
    un obbligo che ne dipenda. Il terzo e' sostanziale ed e' qui sotto.

(c) direzione cross-capitolo (dentro la stessa Fonte), con un estrattore
    meccanico delle citazioni letterali di articoli ("articolo N", con o senza
    "paragrafo M") nel `testo_integrale` di ogni riga, risolte contro l'indice
    dei riferimenti della Fonte: 132 candidati. Di questi ne sono stati tenuti
    81, quelli il cui articolo bersaglio ha **al piu' 3 righe**;
    restano fuori 51 candidati verso articoli spezzati in molti
    commi, dove l'ancoraggio a un comma singolo sarebbe arbitrario (es. "il
    riesame e' effettuato in conformita' degli articoli 13 e 19" non dice
    *quale* comma dell'art. 13). Sono lo stesso limite di modellazione
    dichiarato per Fonte 28 (citazione all'art. 5 bis §4 eIDAS2, paragrafo
    senza nodo di chapeau): la grana del rinvio e' l'articolo, quella del nodo
    e' il comma. La lista completa dei candidati scartati si rigenera
    rieseguendo l'estrattore documentato nel docstring di questo capitolo
    virtuale (app/tools/preflight_relazioni.py non lo copre: verifica solo che
    i riferimenti dichiarati esistano).

Stadio 2 - classificazione nella sessione principale (mai a subagent, stessa
ratio dell'ADR-0009), leggendo le controparti in Neo4j prima di decidere.

Stadio 3 - validazione: esistenza e tipo (Obbligo/Principio) di ogni
`riferimento` proposto verificati con query mirata su Neo4j prima della
scrittura; `preflight_relazioni.py 29 app/seed_data/reg_ue_2024_482` prima del
seed.

## Esito: 85 relazioni

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

Cross-capitolo (81): tutte "richiama" `textual` con confidence 0.80,
su citazione letterale verificata nel testo della riga citante. Il bersaglio
piu' frequente e' l'art. 3 ("norme di valutazione": criteri comuni e metodologia
comune), che e' la norma di riferimento dell'intero regolamento e la riga piu'
citata: vi rinvia buona parte dei capitoli degli allegati (relazione di
certificazione, valutazione inter pares, dichiarazione del pacchetto di
affidabilita').

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
- Rinvii interni "in blocco" a articoli spezzati in piu' di 3 commi
  (51 candidati meccanici): vedi stadio 1(c).

## Limite noto

L'EUCC e' la prima Fonte del censimento che non riguarda servizi fiduciari ma
*certificazione di prodotti TIC*: il collegamento al resto del grafo passa per
tre soli archi (due da eIDAS2, uno verso eIDAS) piu' un rinvio inverso da
Fonte 24. Non e' un esito per difetto: e' la conseguenza di un perimetro
diverso. Riverificare questo modulo quando il censimento importera' i
regolamenti di esecuzione (UE) 2024/3143 (notifiche degli organismi di
valutazione della conformita': l'art. 1, punto 4 di Fonte 30 sopprime gli
artt. 23-24 proprio in vista di quell'atto) e 2024/482 e' modificato da
Fonte 30, gia' censita, con cui questo modulo condivide il capo IV.
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

    # --- cross-capitolo (citazioni letterali di articoli, ancorate a un articolo
    # --- bersaglio con al piu' 3 righe: oltre quella soglia il rinvio "in blocco"
    # --- produrrebbe un fan-out arbitrario su singoli commi, e resta da rivedere)
    {
        "nodo_da": ("obbligo", None, "art. 7 §1"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 §1"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 8 §3"),
        "nodo_a": ("principio", None, "art. 49 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 8 §3"),
        "nodo_a": ("principio", None, "art. 49 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 8 §3"),
        "nodo_a": ("principio", None, "art. 49 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 15 §1"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 20 §1"),
        "nodo_a": ("obbligo", None, "art. 14 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 20 §1"),
        "nodo_a": ("obbligo", None, "art. 14 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 20 §1"),
        "nodo_a": ("principio", None, "art. 14 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 17 §2"),
        "nodo_a": ("obbligo", None, "art. 9 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 17 §2"),
        "nodo_a": ("obbligo", None, "art. 9 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 17 §2"),
        "nodo_a": ("obbligo", None, "art. 9 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 21 §1"),
        "nodo_a": ("obbligo", None, "art. 43"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 21 §2"),
        "nodo_a": ("principio", None, "art. 49 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 21 §2"),
        "nodo_a": ("principio", None, "art. 49 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 21 §2"),
        "nodo_a": ("principio", None, "art. 49 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 22 §1"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 22 §1"),
        "nodo_a": ("obbligo", None, "art. 43"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 22 §3"),
        "nodo_a": ("principio", None, "art. 49 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 22 §3"),
        "nodo_a": ("principio", None, "art. 49 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 22 §3"),
        "nodo_a": ("principio", None, "art. 49 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 26 §2"),
        "nodo_a": ("obbligo", None, "art. 9 §1"),
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
        "nodo_da": ("obbligo", None, "art. 26 §2"),
        "nodo_a": ("obbligo", None, "art. 9 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §5"),
        "nodo_a": ("obbligo", None, "art. 13 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §5"),
        "nodo_a": ("obbligo", None, "art. 13 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §5"),
        "nodo_a": ("principio", None, "art. 13 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §5"),
        "nodo_a": ("obbligo", None, "art. 19 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §5"),
        "nodo_a": ("obbligo", None, "art. 19 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §6"),
        "nodo_a": ("obbligo", None, "art. 14 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §6"),
        "nodo_a": ("obbligo", None, "art. 14 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §6"),
        "nodo_a": ("principio", None, "art. 14 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §2"),
        "nodo_a": ("obbligo", None, "art. 14 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §2"),
        "nodo_a": ("obbligo", None, "art. 14 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §2"),
        "nodo_a": ("principio", None, "art. 14 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §2"),
        "nodo_a": ("obbligo", None, "art. 20 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §2"),
        "nodo_a": ("obbligo", None, "art. 20 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §3"),
        "nodo_a": ("obbligo", None, "art. 14 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §3"),
        "nodo_a": ("obbligo", None, "art. 14 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §3"),
        "nodo_a": ("principio", None, "art. 14 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §3"),
        "nodo_a": ("obbligo", None, "art. 20 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §3"),
        "nodo_a": ("obbligo", None, "art. 20 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 31 §2"),
        "nodo_a": ("obbligo", None, "art. 14 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 31 §2"),
        "nodo_a": ("obbligo", None, "art. 14 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 31 §2"),
        "nodo_a": ("principio", None, "art. 14 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 31 §2"),
        "nodo_a": ("obbligo", None, "art. 20 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 31 §2"),
        "nodo_a": ("obbligo", None, "art. 20 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 26 §3"),
        "nodo_a": ("obbligo", None, "art. 9 §1"),
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
        "nodo_da": ("principio", None, "art. 26 §3"),
        "nodo_a": ("obbligo", None, "art. 9 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 34 §2"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 35 §6"),
        "nodo_a": ("obbligo", None, "art. 14 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 35 §6"),
        "nodo_a": ("obbligo", None, "art. 14 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 35 §6"),
        "nodo_a": ("principio", None, "art. 14 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 36"),
        "nodo_a": ("obbligo", None, "art. 13 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 36"),
        "nodo_a": ("obbligo", None, "art. 13 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 36"),
        "nodo_a": ("principio", None, "art. 13 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 39"),
        "nodo_a": ("obbligo", None, "art. 12 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 39"),
        "nodo_a": ("obbligo", None, "art. 12 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 39"),
        "nodo_a": ("obbligo", None, "art. 12 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "art. 35 §5"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 40 §2"),
        "nodo_a": ("obbligo", None, "art. 13 §1"),
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
        "nodo_da": ("obbligo", None, "art. 40 §2"),
        "nodo_a": ("principio", None, "art. 13 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 41 §3"),
        "nodo_a": ("obbligo", None, "art. 13 §1"),
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
        "nodo_da": ("obbligo", None, "art. 41 §3"),
        "nodo_a": ("principio", None, "art. 13 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "art. 44 §3"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato IV, sezione IV.2, punto 4"),
        "nodo_a": ("obbligo", None, "art. 13 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato IV, sezione IV.2, punto 4"),
        "nodo_a": ("obbligo", None, "art. 13 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato IV, sezione IV.2, punto 4"),
        "nodo_a": ("principio", None, "art. 13 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "allegato IV, sezione IV.4, punto 3"),
        "nodo_a": ("obbligo", None, "art. 13 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "allegato IV, sezione IV.4, punto 3"),
        "nodo_a": ("obbligo", None, "art. 13 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "allegato IV, sezione IV.4, punto 3"),
        "nodo_a": ("principio", None, "art. 13 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato V, sezione V.1, punto 13"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato V, sezione V.1, punto 14"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato V, sezione V.2, punto 3"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato V, sezione V.2, punto 4"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VI, sezione VI.2, punto 1"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VII, lettera c)"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "allegato VIII, punto 2"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
]
