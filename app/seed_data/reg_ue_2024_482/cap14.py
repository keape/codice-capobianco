"""Regolamento di esecuzione (UE) 2024/482 della Commissione, del 31 gennaio
2024 - modalita' di applicazione del regolamento (UE) 2019/881 del Parlamento
europeo e del Consiglio per quanto riguarda l'adozione del sistema europeo di
certificazione della cibersicurezza basato sui criteri comuni (EUCC). Fonte 29
(slug `reg_ue_2024_482`), capitolo 14 di 14 (vedi
app/.source_cache/reg_ue_2024_482/manifest.json): Allegato IX - Marchio ed
etichetta. Gli artt. 1-50 e gli allegati I-VIII appartengono ai capitoli 1-13
della stessa Fonte, assegnati ad altri moduli: nessuno di quei file e' toccato
qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_482/cap14.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R0482, lingua italiana; URL
risolto
http://publications.europa.eu/resource/cellar/687c0d05-c580-11ee-95d9-01aa75ed71a1.0014.03/DOC_1,
XHTML della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 540.435 byte
scaricati, 135.367 caratteri di testo, sha256 del raw.txt
b46d08cab6d63b2c190ae767042c07c1fc324955c22ef491eb314556b28ca5b8 - dettagli
completi in app/.source_cache/reg_ue_2024_482/provenance.json). La porzione
assegnata e' l'allegato IX per intero (398 caratteri nel file di capitolo):
dall'intestazione "ALLEGATO IX" all'ultimo dei suoi tre punti numerati; e' la
porzione finale del documento, seguita solo dalla riga ELI e da "ISSN 1977-0707
(electronic edition)" che chiudono l'atto. Il preambolo (considerando) e' a
monte del Capo I e non e' in questa porzione.

Modellazione (ADR-0007, nessun punto dell'allegato non coperto, nessuno coperto
due volte):
- Paratesto -> nessun nodo e nessun item di indice: l'intestazione "ALLEGATO
  IX" e il suo titolo "Marchio ed etichetta" sono struttura dell'atto, non
  punti numerati, e non sono assorbiti nel `testo_integrale` di alcuna riga
  (convenzione del cap09 di questa stessa Fonte per gli allegati con punti
  numerati: li' i titoli degli allegati I e II restano fuori dal grafo per la
  stessa ragione; il titolo "Marchio ed etichetta" e' comunque presente nel
  censimento come rubrica dell'art. 11, censito nel cap02). La riga "ELI:
  http://data.europa.eu/eli/reg_impl/2024/482/oj" e la riga "ISSN 1977-0707
  (electronic edition)" sono paratesto editoriale: nessun nodo. In questa
  porzione non compaiono epigrafe, firma, formula di chiusura ne' note a pie'
  di pagina (la formula "obbligatorio in tutti i suoi elementi e direttamente
  applicabile in ciascuno degli Stati membri" chiude l'art. 50, quindi sta nel
  cap08).
- Unita' di copertura: i tre punti numerati dell'allegato ("1.", "2.", "3.") ->
  tre righe, un item di indice ciascuno. Nessun item a livello di allegato
  ("allegato IX"): qui i punti sono numerati e allegato IX non ha un testo di
  chiusura proprio, quindi la convenzione applicata e' quella del cap09 di
  questa Fonte (item a livello di allegato solo per gli allegati che non
  numerano i punti; il cap10 lo usa per l'allegato III perche' li' esiste un
  chapeau con testo proprio). Una riga per punto e non una riga unica: i tre
  punti sono tre precetti distinti (formato del marchio; proporzioni in caso di
  ridimensionamento; altezza minima se fisicamente presenti), non un'unica
  prescrizione continua, e nessuno di essi e' un chapeau che regge gli altri.
- La nota di capitolo ("una o due righe, nessuna invenzione e nessun nodo in
  piu' del necessario") e' stata letta come "nessun nodo oltre ai tre punti
  numerati": nessun nodo e' stato creato per il disegno del punto 1, per il
  titolo dell'allegato o per il richiamo all'art. 11 che l'allegato presuppone.
  Le tre righe sono il minimo imposto dalla guardia di copertura (un item di
  indice per punto, mappato su esattamente una riga).
- Allegato IX, punto 1 ("Formato del marchio e dell'etichetta:", seguito dal
  disegno del marchio e dell'etichetta) -> UN Principio "altro": il punto non
  ha verbo ne' soggetto, designa il formato ufficiale attraverso il disegno e
  non enuncia un comportamento; il contenuto prescrittivo sta negli articoli
  che richiamano l'allegato (art. 11 §§1 e 3, cap02) e nei punti 2 e 3, che sul
  disegno costruiscono le loro regole. Stessa classificazione delle
  designazioni del cap09 di questa Fonte (allegato I punto 1 e punto 2, allegato
  II punto 1). Dubbio di classificazione dichiarato: Obbligo
  "informativo/trasparenza" con soggetto "Terza parte" sarebbe sostenibile
  leggendo il punto attraverso l'art. 11 §3 ("il marchio e l'etichetta sono
  conformi al quanto disposto nell'allegato IX"), cioe' come prescrizione della
  forma del marchio in capo al titolare del certificato; scelto il Principio
  perche' il punto, preso nel suo testo, non nomina alcun soggetto e non
  contiene alcun predicato di obbligo.
- Allegato IX, punti 2 e 3 -> Obbligo ciascuno, tipo "informativo/trasparenza",
  soggetto obbligato "Terza parte" (il titolare del certificato che appone
  marchio ed etichetta): il testo impone in forma passiva un requisito sulla
  resa del marchio ("sono rispettate le proporzioni", "hanno un'altezza minima
  di 5 mm"), come l'art. 11 §2 di questa Fonte ("sono apposti in modo visibile,
  leggibile e indelebile") censito nel cap02 - stessa forma passiva, stesso tipo
  di obbligo e stessa categoria di soggetto. Il tipo "informativo/trasparenza" e
  non "tecnico/sicurezza": nel cap02 di questa Fonte tutte le prescrizioni sul
  marchio e sull'etichetta (art. 11 §§2-4, resa, contenuto, codice QR) sono
  classificate "informativo/trasparenza" perche' il marchio serve a rendere
  riconoscibile al mercato la certificazione del prodotto TIC; la grafica e le
  dimensioni minime sono requisiti di leggibilita' di quella informazione.
  Dubbio di classificazione dichiarato: l'allegato non nomina il soggetto
  obbligato, che e' dedotto dall'art. 11 §1 (facolta' del titolare di apporre
  marchio ed etichetta) e dalla convenzione di censimento del cap02, dove
  l'obbligato di tutte le prescrizioni sul marchio e' "Terza parte" e
  "Utente/titolare" compare solo come destinatario dove il testo nomina gli
  utenti (qui non accade).
- `condizione_applicabilita` valorizzata sulle due righe di obbligo, perche'
  entrambe sono testualmente condizionate: punto 2 "In caso di riduzione o di
  ingrandimento del marchio e dell'etichetta"; punto 3 "Se fisicamente
  presenti". Nessuna riga valorizza `severita` o `sanzioni`: l'atto non gradua
  i requisiti ne' prevede sanzioni proprie. `stato` = "vigente" per tutte le
  righe. Nessun `oggetti_giuridici`: fra i valori censiti non ce n'e' uno che
  corrisponda al marchio o all'etichetta EUCC (il "certificato EUCC" non e' un
  oggetto censito) e la voce generica "altro" non e' stata forzata (stesso
  criterio dell'art. 11 §2-§4 del cap02, che non valorizza `oggetti_giuridici`,
  e del cap09/cap10 di questa Fonte).
- Il punto 1 dell'allegato: il disegno e' un'immagine incorporata nel documento
  pubblicato (`<figure><img src="data:image/jpg;base64,<payload>"
  height="139.5" width="581.5" alt="Image 1" class="oj-img"/></figure>`,
  verificato sull'XHTML CELLAR della stessa acquisizione indicata in
  provenance.json), senza alternativa testuale oltre l'`alt` "Image 1": la
  conversione XHTML -> testo non ne conserva alcun contenuto, ed e' la ragione
  per cui cap14.txt passa direttamente dalla dicitura "Formato del marchio e
  dell'etichetta:" al punto "2.". Nessun contenuto del disegno e' stato
  ricostruito a memoria (il marchio EUCC e la sua etichetta non sono descritti
  in forma testuale da nessuna parte dell'allegato) e nessun segnaposto e'
  stato inventato al posto dell'immagine: il `testo_integrale` del punto 1
  riporta verbatim la sola dicitura che l'atto pubblica.
- `testo_integrale`: verbatim e integrale, ricucito dalle righe spezzate dalla
  conversione XHTML -> testo. In cap14.txt i marcatori dei punti ("1.", "2.",
  "3.") stanno su riga propria e sono riuniti al testo che segue, come per i
  punti degli allegati I e II del cap09: le tre stringhe risultanti sono
  "1. Formato del marchio e dell'etichetta:", "2. In caso di riduzione o di
  ingrandimento del marchio e dell'etichetta, sono rispettate le proporzioni
  indicate nel disegno sopra riportato." e "3. Se fisicamente presenti, il
  marchio e l'etichetta hanno un'altezza minima di 5 mm.". Un punto per
  blocco, nell'ordine del testo ufficiale, senza riga vuota interna (ogni
  punto e' un periodo unico). Nessun marcatore di elisione (vincolo
  `verifica_completezza_testo_integrale`, ADR-0010). Gli errori del testo
  ufficiale italiano non sono corretti: "il marchio e l'etichetta hanno
  un'altezza minima di 5 mm" e' riportato com'e' pubblicato, e il refuso
  dell'art. 11 §3 ("al quanto disposto nell'allegato IX") non appartiene a
  questa porzione.
- RELAZIONI: due relazioni interne, tutte fra nodi dichiarati in questo modulo.
  (1) "allegato IX, punto 2" -> "allegato IX, punto 1", tipo "richiama": il
  punto 2 rinvia letteralmente al disegno del punto 1 ("le proporzioni indicate
  nel disegno sopra riportato"). `evidence_type` "inferred" e non "textual": il
  rinvio e' letterale, ma il nodo bersaglio e' identificato per posizione (il
  disegno e' il contenuto del punto 1, introdotto dalla dicitura che lo precede
  e dalla figura che segue), mentre il testo del punto 2 non nomina il
  `riferimento` del bersaglio ("punto 1" ne' "allegato IX"); dichiararlo
  "textual" farebbe scattare la sezione A del gate di
  `app/tools/verifica_relazioni_textual.py`, che cerca nel testo citante una
  traccia del riferimento citato e non la trova. (2) "allegato IX, punto 3" ->
  "allegato IX, punto 1", tipo "specifica": l'altezza minima di 5 mm e' una
  precisazione dimensionale del formato designato dal punto 1, dedotta dal
  contenuto e non citata (il punto 3 non nomina il disegno), quindi
  `evidence_type` "inferred"; direzione specifico -> generale, come le lettere
  dell'allegato III del cap10 di questa Fonte rispetto al proprio chapeau.
  `confidence` None su entrambe: nessuno score reale da riportare (ADR-0005,
  non va inventato). Nessuna relazione verso altri capitoli di questa Fonte o
  verso altre Fonti: dichiararle qui, in import parallelo per capitolo,
  imporrebbe di indovinare i `riferimento` dei nodi scritti da altri moduli e
  un riferimento sbagliato fa fallire il seed con KeyError.
- Rinvii demandati alla fase 6 (nessuna relazione dichiarata qui; accanto a
  ogni rinvio e' indicato il `riferimento` con cui il nodo bersaglio e'
  dichiarato nel modulo del capitolo che lo contiene). Rinvii entranti
  all'allegato IX, verificati sul testo integrale: art. 11 §1 -> riga "art. 11
  §1" (cap02, apposizione di marchio ed etichetta in conformita' del presente
  articolo e dell'allegato IX) e art. 11 §3 -> riga "art. 11 §3" (cap02: "Il
  marchio e l'etichetta sono conformi al quanto disposto nell'allegato IX e
  contengono:"). Sono le uniche due citazioni letterali dell'allegato IX
  nell'intero atto. Le altre disposizioni che nominano il marchio e l'etichetta
  (art. 9 §2, allegato V punto 17 e allegato VIII lettera (d), questi ultimi
  nei capitoli 12-13) rinviano all'articolo 11 e non all'allegato IX: nessun
  arco verso questo capitolo. Nessun altro elemento di questa porzione cita
  altri articoli, allegati o Fonti: nessun rinvio uscente da costruire.

Copertura: 3 item di indice, 3 righe (2 Obblighi + 1 Principio), 2 relazioni
interne.

Dubbi di classificazione rimasti aperti (dichiarati, non risolti in modo
univoco dal testo): (1) il punto 1 come Principio "altro" invece che come
Obbligo "informativo/trasparenza": il formato del marchio e' obbligatorio per
effetto dell'art. 11 §3, che impone la conformita' all'allegato IX, ma il testo
del punto non contiene un precetto proprio (solo la dicitura e il disegno);
(2) il soggetto obbligato dei punti 2 e 3 e' dedotto dall'art. 11 §1-§2 e dalla
convenzione del cap02 ("Terza parte"), l'allegato non nomina alcun soggetto;
(3) la relazione del punto 3 verso il punto 1 e' un'inferenza di contenuto: chi
non la condividesse puo' toglierla senza toccare la copertura (il punto 3 resta
coperto comunque dal proprio item di indice).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "allegato IX, punto 2",
        "testo": "In caso di riduzione o di ingrandimento del marchio e dell'etichetta sono rispettate le proporzioni indicate nel disegno riportato al punto 1 dell'allegato (il disegno del formato ufficiale del marchio e dell'etichetta, incorporato nel testo pubblicato come immagine).",
        "testo_integrale": "2. In caso di riduzione o di ingrandimento del marchio e dell'etichetta, sono rispettate le proporzioni indicate nel disegno sopra riportato.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica in caso di riduzione o di ingrandimento del marchio e dell'etichetta.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato IX, punto 3",
        "testo": "Se il marchio e l'etichetta sono fisicamente presenti, hanno un'altezza minima di 5 mm.",
        "testo_integrale": "3. Se fisicamente presenti, il marchio e l'etichetta hanno un'altezza minima di 5 mm.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se il marchio e l'etichetta sono fisicamente presenti.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "allegato IX, punto 1",
        "testo": "Il punto 1 dell'allegato IX designa il formato del marchio e dell'etichetta: la dicitura «Formato del marchio e dell'etichetta:» e' seguita, nel testo pubblicato, dal disegno del marchio e dell'etichetta (immagine incorporata, priva di contenuto testuale), al quale rinvia il punto 2. Il punto non enuncia alcun comportamento ne' nomina un soggetto.",
        "testo_integrale": "1. Formato del marchio e dell'etichetta:",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "allegato IX, punto 1",
    "allegato IX, punto 2",
    "allegato IX, punto 3",
]

MAPPATURA_LOCALE = {
    "allegato IX, punto 1": ["allegato IX, punto 1"],
    "allegato IX, punto 2": ["allegato IX, punto 2"],
    "allegato IX, punto 3": ["allegato IX, punto 3"],
}

# Relazioni interne a questo modulo (fonte_id_o_None = None su entrambi gli
# estremi), dettagliate nel docstring in testa al file. Nessuna relazione verso
# altri capitoli o altre Fonti: i rinvii entranti (art. 11 §1 e §3, cap02) sono
# elencati nel docstring sotto "rinvii demandati alla fase 6".
RELAZIONI = [
    # Punto 2 -> punto 1: "le proporzioni indicate nel disegno sopra riportato".
    # Rinvio letterale al disegno introdotto dal punto 1; il bersaglio e'
    # identificato per posizione, non dal suo riferimento, quindi l'evidenza
    # resta "inferred" (vedi docstring).
    {
        "nodo_da": ("obbligo", None, "allegato IX, punto 2"),
        "nodo_a": ("principio", None, "allegato IX, punto 1"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    # Punto 3 -> punto 1: l'altezza minima di 5 mm precisa il formato designato
    # dal punto 1 (direzione specifico -> generale, come le lettere
    # dell'allegato III del cap10 rispetto al proprio chapeau).
    {
        "nodo_da": ("obbligo", None, "allegato IX, punto 3"),
        "nodo_a": ("principio", None, "allegato IX, punto 1"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
]
