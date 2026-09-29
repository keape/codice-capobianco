"""Fase 6 (ADR-0009) di Fonte 30 - Regolamento di esecuzione (UE) 2024/3144,
atto MODIFICATIVO e RETTIFICATIVO del regolamento di esecuzione (UE) 2024/482
(EUCC, Fonte 29). Capitolo virtuale: solo RELAZIONI, nessun nodo proprio
(`RIGHE_OBBLIGHI`/`RIGHE_PRINCIPI`/`INDICE_ARTICOLI_LOCALE`/`MAPPATURA_LOCALE`
vuoti), stesso formato di app/seed_data/cad/cap08_relazioni_eidas.py.

Qui vivono le relazioni che l'atto modificativo intrattiene con il regolamento
modificato: la natura di questa Fonte e' interamente relazionale, e i moduli
cap01-cap05 hanno per questo documentato riga per riga, nel proprio docstring,
quale articolo o allegato di Fonte 29 ciascun punto tocca e con quale tipo di
intervento, senza dichiarare l'arco (istruzione del batch: nessuna relazione
cross-fonte in fase di autoria per capitolo).

## Pipeline eseguita (2026-09-29, sessione principale)

Stadio 1 - candidati. Per un atto modificativo il "grep delle citazioni" e' il
testo stesso dell'atto: ogni punto nomina l'articolo o l'allegato che tocca
("l'articolo 3 e' sostituito dal seguente", "gli articoli 23 e 24 sono
soppressi", "l'allegato I e' sostituito dal testo di cui all'allegato I del
presente regolamento"). I 21 archi di questo modulo derivano quindi
dall'elenco dei bersagli documentato dai cinque moduli di capitolo, non da un
giro KNN: per un atto modificativo il KNN misura solo la somiglianza di
formulario. Direzione inversa (fonti esistenti -> questa Fonte) verificata con
query su `testo_integrale` in Neo4j per "2024/3144": due nodi, entrambi voci di
elenchi bibliografici ("riferimenti normativi" di Fonti 23 e 24) e le stesse
che citano la Fonte 29: restano senza arco, come da convenzione del progetto
per i rinvii puramente bibliografici.

Stadio 2 - classificazione nella sessione principale, leggendo il testo
verbatim di ciascun punto (nel `testo_integrale` del modulo che lo dichiara)
prima di scegliere il tipo di relazione.

Stadio 3 - validazione: esistenza e tipo (Obbligo/Principio) di ogni bersaglio
verificati risolvendo i `riferimento` contro i moduli di Fonte 29 (la Fonte non
e' ancora nel grafo quando questo modulo viene scritto: `preflight_relazioni.py`
segnala percio' i suoi archi come riferimenti esterni non trovati, e la verifica
va letta contro i moduli, non contro Neo4j).

## Esito: 21 relazioni, tutte verso Fonte 29 tranne una

Tutte `evidence_type="textual"`: il testo dell'atto modificativo nomina
letteralmente l'articolo o l'allegato che tocca, e per i bersagli qui sotto
l'arco e' la trascrizione esatta dell'intervento disposto. `confidence` fra
0.85 e 0.90.

- **`sostituisce` (8)**: art. 1, punto 1 -> "art. 2" (i punti 1 e 2 delle
  definizioni); art. 1, punto 2 -> "art. 3" (norme di valutazione, sostituito
  integralmente dal nuovo testo che fissa ISO/IEC 15408-*:2022 e ISO/IEC
  18045:2022 e la disciplina transitoria fino al 31 dicembre 2027); art. 1,
  punto 7 -> "allegato I, punto 1" e "allegato I, punto 2" (sostituzione
  integrale dell'allegato I: due archi, uno per ciascuna riga dell'allegato
  censito); art. 2, punto 3 -> "art. 16"; art. 2, punto 5 -> "art. 29 §2";
  allegato II, punto 5 -> "allegato IV, sezione IV.3, punto 5" e allegato II,
  punto 6 -> "allegato IV, sezione IV.3, punto 6" (i due punti dell'allegato
  IV sostituiti dal testo di cui all'allegato II della 3144).
- **`abroga` (7)**: art. 1, punto 4 -> "art. 23 §1" ... "art. 23 §5" (cinque
  archi: la soppressione dell'articolo 23 colpisce tutti i suoi commi, non
  esistendo un nodo di chapeau dell'articolo) e -> "art. 24" (soppresso con
  l'articolo 23 in vista del regolamento di esecuzione (UE) 2024/3143 sulle
  notifiche); art. 2, punto 4 -> "art. 17 §1" (soppressione del solo primo
  paragrafo).
- **`modifica` (5)**: art. 1, punto 5 -> "art. 48 §1" (aggiunta di un
  paragrafo 4: l'ancora e' il primo comma dell'articolo, perche' l'articolo non
  ha un nodo di chapeau e il nuovo paragrafo si colloca in coda); art. 1, punto
  6 -> "art. 49 §1" (stessa fattispecie); art. 1, punto 8 -> "allegato IV,
  sezione IV.3" (l'allegato IV e' modificato conformemente all'allegato II
  dell'atto: qui l'ancora e' la sezione, che e' la riga che il regolamento
  modificato dedica alla sezione intervenuta); art. 2, punto 1 -> "art. 5 §1"
  (sostituzione della sola lettera b) del primo comma); art. 2, punto 2 ->
  "art. 8 §1" (rettifica della rubrica dell'articolo e del primo comma).
- **`richiama` (1, `inferred`, confidence 0.60)**: art. 1, punto 2 -> Fonte 1
  "art. 30 §3". Il testo sostitutivo dell'art. 3, paragrafo 4 nomina il
  regolamento (UE) n. 910/2014 fra gli atti il cui uso di un profilo di
  protezione basato sulle norme precedenti resta ammesso: il rinvio e' al
  regolamento come fonte di obblighi, non a una sua disposizione, e l'ancora
  scelta (la norma eIDAS che governa la certificazione dei dispositivi per la
  creazione di firma qualificata e l'elenco di norme adottato con la decisione
  di esecuzione (UE) 2016/650, nominata nella stessa frase) e' per contenuto,
  non per citazione: da qui `inferred` e una confidence prudente.

## Rinvii lasciati senza relazione (dichiarati, non omessi per svista)

- **art. 1, punto 3** (inserimento del nuovo articolo 20 bis sull'accreditamento
  degli organismi di valutazione della conformita'): nessun arco, perche' non
  esiste in Fonte 29 un nodo controparte - l'articolo e' nuovo e la disposizione
  non modifica alcuna riga esistente. Il contenuto resta nella riga di Fonte 30.
- **allegato I di questa Fonte (cap04)**: nessun arco proprio, per non
  duplicare la "sostituisce" gia' dichiarata dall'art. 1, punto 7, che e' la
  disposizione che ordina la sostituzione; le due righe dell'allegato portano
  il testo sostitutivo, non un intervento ulteriore.
- **art. 3, entrata in vigore / applicazione**: nessun arco (disposizione sulla
  vigenza dell'atto, senza bersaglio in Fonte 29).
- **Norme esterne citate e non censite**: regolamento (UE) 2019/881 (artt. 49 e
  66 §2), regolamento di esecuzione (UE) 2024/3143, regolamento di esecuzione
  (UE) 2016/799, decisione di esecuzione (UE) 2016/650, ISO/IEC 15408:2022 e
  18045:2022. Nessuna ha un nodo controparte.
- **Voci bibliografiche di Fonti 23 e 24** che nominano questa Fonte (elenchi
  "riferimenti normativi"): vedi stadio 1, direzione inversa.
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = []

MAPPATURA_LOCALE = {}

RELAZIONI = [
    # --- Fonte 29, Reg. di esecuzione (UE) 2024/482 (EUCC) ----------------
    {
        "nodo_da": ("principio", None, "art. 1, punto 1"),
        "nodo_a": ("principio", 29, "art. 2"),
        "tipo_relazione": "sostituisce",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("principio", None, "art. 1, punto 2"),
        "nodo_a": ("principio", 29, "art. 3"),
        "tipo_relazione": "sostituisce",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("principio", None, "art. 1, punto 4"),
        "nodo_a": ("obbligo", 29, "art. 23 §1"),
        "tipo_relazione": "abroga",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("principio", None, "art. 1, punto 4"),
        "nodo_a": ("obbligo", 29, "art. 23 §2"),
        "tipo_relazione": "abroga",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("principio", None, "art. 1, punto 4"),
        "nodo_a": ("obbligo", 29, "art. 23 §3"),
        "tipo_relazione": "abroga",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("principio", None, "art. 1, punto 4"),
        "nodo_a": ("obbligo", 29, "art. 23 §4"),
        "tipo_relazione": "abroga",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("principio", None, "art. 1, punto 4"),
        "nodo_a": ("obbligo", 29, "art. 23 §5"),
        "tipo_relazione": "abroga",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("principio", None, "art. 1, punto 4"),
        "nodo_a": ("obbligo", 29, "art. 24"),
        "tipo_relazione": "abroga",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("principio", None, "art. 1, punto 5"),
        "nodo_a": ("principio", 29, "art. 48 §1"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", None, "art. 1, punto 6"),
        "nodo_a": ("principio", 29, "art. 49 §1"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", None, "art. 1, punto 7"),
        "nodo_a": ("principio", 29, "allegato I, punto 1"),
        "tipo_relazione": "sostituisce",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("principio", None, "art. 1, punto 7"),
        "nodo_a": ("principio", 29, "allegato I, punto 2"),
        "tipo_relazione": "sostituisce",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("principio", None, "art. 1, punto 8"),
        "nodo_a": ("principio", 29, "allegato IV, sezione IV.3"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", None, "art. 2, punto 1"),
        "nodo_a": ("obbligo", 29, "art. 5 §1"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", None, "art. 2, punto 2"),
        "nodo_a": ("obbligo", 29, "art. 8 §1"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", None, "art. 2, punto 3"),
        "nodo_a": ("obbligo", 29, "art. 16"),
        "tipo_relazione": "sostituisce",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("principio", None, "art. 2, punto 4"),
        "nodo_a": ("obbligo", 29, "art. 17 §1"),
        "tipo_relazione": "abroga",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("principio", None, "art. 2, punto 5"),
        "nodo_a": ("obbligo", 29, "art. 29 §2"),
        "tipo_relazione": "sostituisce",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("obbligo", None, "allegato II, punto 5"),
        "nodo_a": ("obbligo", 29, "allegato IV, sezione IV.3, punto 5"),
        "tipo_relazione": "sostituisce",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    {
        "nodo_da": ("obbligo", None, "allegato II, punto 6"),
        "nodo_a": ("obbligo", 29, "allegato IV, sezione IV.3, punto 6"),
        "tipo_relazione": "sostituisce",
        "evidence_type": "textual",
        "confidence": 0.90,
    },
    # --- Fonte 1, Regolamento eIDAS (UE) 910/2014 -------------------------
    {
        "nodo_da": ("principio", None, "art. 1, punto 2"),
        "nodo_a": ("obbligo", 1, "art. 30 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": 0.60,
    },
]
