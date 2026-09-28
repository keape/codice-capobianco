"""Fase 6 (ADR-0009) di Fonte 26 - ETSI TS 119 101 V1.1.1 (2016-03),
"Electronic Signatures and Trust Infrastructures (ESI); Policy and security
requirements for applications for signature creation and signature
validation". Capitolo virtuale: solo RELAZIONI.

Nessuna relazione *nativa*: TS 119 101 rinvia a IETF RFC, a direttive e ad
altri standard ETSI non censiti (TS 119 102, TS 119 172, TS 119 104/124/134/
144/164/174, ISO/IEC 15504), nessuno dei quali ha un nodo nel grafo.

## Il giro che conta e' in direzione inversa

Come per Fonte 25: il contributo sono le fonti **gia' censite** che citano
questa. Ricognizione con query su tutti i nodi il cui `testo_integrale`
contiene "119 101", etichettando quale delle tre fonti in arrivo ciascun nodo
cita (per non attribuire a questa le citazioni di 119 312 o 319 102): 9 nodi
della sola Fonte 11 (ETSI TS 119 431 Parte 2) la richiamano, e sei di essi lo
fanno **per id di controllo** - non per clausola.

## Esito: 14 relazioni, tutte "richiama" su citazione letterale

Dodici agganciano il controllo puntuale citato dall'id (la granularita'
per id di Fonte 26 serve esattamente a questo: con nodi di clausola non
esisterebbe un bersaglio), due sono rinvii generici alla norma nel suo insieme.

| nodo citante (Fonte 11, Parte 2) | -> nodo di TS 119 101 | citazione |
|---|---|---|
| ASI-8.1-07 | UI 1, UI 2 | "the requirements UI 1 and UI 2 from ETSI TS 119 101" |
| ASI-8.1-09 | SCP 13, SCP 47 | "SCP 13 and SCP 47 of ETSI TS 119 101 shall apply" |
| OVR-7.6-02 | GSM 1.4 | "clause 5.2 shall apply to the SCA: GSM 1.4" |
| OVR-7.7-02 | GSM 1.2, GSM 1.3 | "clause 5.2 should apply to the SCA: GSM 1.2 and GSM 1.3" |
| OVR-7.7-03 | GSM 2.4 | "clause 5.2 shall apply to the SCA: GSM 2.4" |
| OVR-8.2-04 | SCP 14, SCP 31, SCP 37, SCP 61 | "SCP 14, SCP 31, SCP 37 and SCP 61 of ETSI TS 119 101 shall apply" |
| OVR-7.7-04 | clausola 1 (Scope) | rinvio generico ("all mandatory requirements from ETSI TS 119 101 referenced above") |
| clausola 1 (Scope) | clausola 1 (Scope) | menzione della norma nel proprio ambito |

Le quattro relazioni di OVR-8.2-04 (SCP 14/31/37/61) sono un caso interessante:
l'id citato e' **SCP** in un documento (TS 119 431-2) le cui proprie
prescrizioni usano altri prefissi, e SCP 14/31/37/61 riguardano la creazione
della firma lato componente, non la convalida: il rinvio va letto nel testo del
controllo, non dedotto dal prefisso.

## Proposte valutate e scartate

- Fonte 11 Parte 2 "Annex C" (tabella informativa di mapping fra i requisiti
  dello standard e gli obblighi eIDAS): menziona TS 119 101 in un elenco
  bibliografico, senza indicare quale requisito ne dipende. Scartata.
- Coerenza interna di Fonte 26 (clausola 10 -> Annex A, TC 2.3 -> TC 2.2):
  sono rinvii *interni* alla stessa Fonte, non relazioni cross-fonte; la
  clausola 10 obbliga gia' a conformarsi all'Annex A nel proprio testo.
- La direzione diretta (KNN) non e' stata usata per questa Fonte: vedi sotto.

## Perche' non c'e' un giro KNN per questa Fonte

Il giro KNN in direzione diretta su una fonte di 275 nodi produce uno shortlist
di migliaia di coppie, quasi tutte rumore: TS 119 101 e' un catalogo di
controlli tecnici per un'applicazione di firma, e la sua prossimita' semantica
con gli altri standard censiti e' dominata dal lessico comune ("signature",
"certificate", "user", "shall") piu' che da corrispondenze prescrittive. Le
corrispondenze reali sono gia' state trovate per citazione letterale, che e' la
classe di evidenza piu' forte disponibile in questo censimento. Il limite e'
dichiarato qui invece di essere mascherato da un elenco di proposte scartate:
se in futuro si vorra' un giro completo, va fatto con il classificatore LLM su
shortlist ristretto per nodo, non con una soglia globale.

## Limite noto

Le citazioni inverse sono ricostruite sul testo di Fonte 11, non su quello di
TS 119 101: se un id citato non esistesse nel testo di questa fonte (es. un
controllo rinumerato o soppresso in una riedizione futura), la relazione
resterebbe appesa a un nodo assente e il seed fallirebbe in modo esplicito.
Verificato a mano che tutti e 12 gli id citati esistono con questa grafia
esatta in Fonte 26 (UI 1, UI 2, SCP 13, SCP 14, SCP 31, SCP 37, SCP 47, SCP 61,
GSM 1.2, GSM 1.3, GSM 1.4, GSM 2.4).
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = []

MAPPATURA_LOCALE = {}

RELAZIONI = [
    # --- ASI-8.1-07 / ASI-8.1-09 (interfaccia utente e presentazione del
    #     documento nel componente di creazione) -----------------------------
    {
        'nodo_da': ('obbligo', 11, 'Parte 2: ASI-8.1-07'),
        'nodo_a': ('obbligo', None, 'UI 1'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 2: ASI-8.1-07'),
        'nodo_a': ('obbligo', None, 'UI 2'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 2: ASI-8.1-09'),
        'nodo_a': ('obbligo', None, 'SCP 13'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 2: ASI-8.1-09'),
        'nodo_a': ('obbligo', None, 'SCP 47'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    # --- OVR-7.6-02 / OVR-7.7-02 / OVR-7.7-03 (misure di sicurezza generali
    #     del componente di creazione) ---------------------------------------
    {
        'nodo_da': ('obbligo', 11, 'Parte 2: OVR-7.6-02'),
        'nodo_a': ('obbligo', None, 'GSM 1.4'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 2: OVR-7.7-02'),
        'nodo_a': ('obbligo', None, 'GSM 1.2'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 2: OVR-7.7-02'),
        'nodo_a': ('obbligo', None, 'GSM 1.3'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 2: OVR-7.7-03'),
        'nodo_a': ('obbligo', None, 'GSM 2.4'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    # --- OVR-8.2-04 (controlli di creazione della firma applicabili al
    #     componente) --------------------------------------------------------
    {
        'nodo_da': ('obbligo', 11, 'Parte 2: OVR-8.2-04'),
        'nodo_a': ('obbligo', None, 'SCP 14'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 2: OVR-8.2-04'),
        'nodo_a': ('obbligo', None, 'SCP 31'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 2: OVR-8.2-04'),
        'nodo_a': ('obbligo', None, 'SCP 37'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', 11, 'Parte 2: OVR-8.2-04'),
        'nodo_a': ('obbligo', None, 'SCP 61'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    # --- rinvii generici alla norma nel suo insieme --------------------------
    {
        'nodo_da': ('obbligo', 11, 'Parte 2: OVR-7.7-04'),
        'nodo_a': ('principio', None, 'clausola 1 (Scope)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('principio', 11, 'Parte 2: clausola 1 (Scope)'),
        'nodo_a': ('principio', None, 'clausola 1 (Scope)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.6,
    },
]
