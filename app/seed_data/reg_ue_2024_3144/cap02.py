"""Regolamento di esecuzione (UE) 2024/3144 della Commissione, del 18 dicembre
2024, che modifica il regolamento di esecuzione (UE) 2024/482 (EUCC) per
quanto riguarda le norme internazionali applicabili e che rettifica tale
regolamento di esecuzione. Fonte 30 (`reg_ue_2024_3144` = atto modificativo),
capitolo 2 di 5 (vedi app/.source_cache/reg_ue_2024_3144/manifest.json):
articolo 1, punti 4-8 (soppressione degli articoli 23 e 24 del regolamento
modificato, nuovo paragrafo 4 dell'articolo 48, nuovo paragrafo 4
dell'articolo 49, sostituzione dell'allegato I, modifica dell'allegato IV).
Il chapeau dell'articolo 1 e i punti 1-3 sono nel cap01, gli articoli 2-3 nel
cap03, l'allegato I nel cap04 e l'allegato II nel cap05, assegnati ad altri
moduli: nessuno di quei file e' toccato qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_3144/cap02.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR (CELEX
32024R3144, lingua italiana; URL richiesto
http://publications.europa.eu/resource/celex/32024R3144, URL risolto
http://publications.europa.eu/resource/cellar/12c401d0-bdaa-11ef-91ed-01aa75ed71a1.0014.03/DOC_1,
XHTML della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 74.420 byte
scaricati e 22.217 caratteri di testo, sha256 del raw.txt
7ced6d4bfe633cf367b3c72ec593ebd5e49c369c7f86f4386984fe81cb81493a - dettagli
completi in provenance.json). Il preambolo (considerando 1-14), l'epigrafe, la
formula di adozione, la firma e le note a pie' di pagina stanno a monte o a
valle della porzione assegnata.

Perimetro: atto modificativo. L'unita' di copertura e' il punto numerato
dell'articolo 1, non l'articolo del regolamento modificato che il punto
incide. Le cinque righe di questo capitolo sono quindi i cinque punti 4)-8)
dell'articolo 1, con riferimento interno "art. 1, punto N" (il registro del
seed e MAPPATURA_LOCALE usano gli stessi riferimenti). Il testo sostitutivo
tra virgolette («...») e' riportato verbatim e per intero dentro il
`testo_integrale` del punto che lo introduce: e' cio' che l'atto modificativo
dispone, non una sintesi.

Decisioni di modellazione, riga per riga:
- art. 1, punto 4 ("gli articoli 23 e 24 sono soppressi") -> UNA riga
  Principio, tipo "altro". La disposizione ha natura abrogativa: non impone
  un comportamento a un soggetto identificabile ne' dichiara un effetto
  giuridico riconducibile a uno degli altri tipi di principio; la tassonomia
  non ha un tipo dedicato alla novella/abrogazione, quindi si usa "altro"
  (stesso criterio con cui la Fonte 6, DPCM 19 ottobre 2021 - decreto
  interamente novellistico - e' censita come Principi "altro" in
  app/seed_data/dpcm2021/cap01.py). La riga copre entrambi gli articoli
  soppressi perche' il punto e' un'unica disposizione con un unico predicato
  ("sono soppressi").
- art. 1, punto 5 (inserimento del paragrafo 4 dell'articolo 48 del
  regolamento modificato) -> UNA riga Principio, tipo "altro". Il testo
  inserito fissa la data a decorrere dalla quale i documenti sullo stato
  dell'arte si applicano (la data di applicazione dell'atto modificativo che
  li ha introdotti negli allegati I o II): e' una norma di vigenza e di
  applicazione, senza soggetto obbligato e senza comportamento imposto.
  Classificazione coerente con quella gia' data in Fonte 29 alla stessa
  materia: "art. 50, applicazione" del Reg. 2024/482 e' un Principio "altro"
  (app/seed_data/reg_ue_2024_482/cap08.py).
- art. 1, punto 6 (inserimento del paragrafo 4 dell'articolo 49 del
  regolamento modificato) -> UNA riga Principio, tipo "altro". La prima frase
  e' una facolta' ("possono essere applicate le norme di cui all'articolo 3,
  paragrafo 2"), la seconda una definizione ("La data di rilascio del
  certificato iniziale e' intesa come..."), entrambe prive di soggetto
  obbligato. Stessa classificazione delle righe "art. 49 §2" e "art. 49 §3" di
  Fonte 29 (facolta' transitorie e derogatorie) e dell'art. 1 §2 del Reg.
  2025/2532 (facolta' di avvalersi di un servizio). Il tipo "definitorio" non
  e' stato usato: la riga non e' un elenco definitorio (chapeau + N voci
  numerate), ma una disposizione mista in cui la definizione e' un inciso
  della regola di applicazione.
- art. 1, punto 7 (sostituzione dell'allegato I del regolamento modificato
  con l'allegato I di questo regolamento) -> UNA riga Principio, tipo
  "altro": disposizione di novella, nessun comportamento imposto. Il testo
  sostitutivo (i documenti sullo stato dell'arte) e' censito nel cap04 di
  questa Fonte, non qui.
- art. 1, punto 8 (modifica dell'allegato IV del regolamento modificato
  conformemente all'allegato II di questo regolamento) -> UNA riga Principio,
  tipo "altro", per la stessa ragione. Il testo sostitutivo (sezione IV.3,
  punti 5 e 6 dell'allegato IV) e' censito nel cap05 di questa Fonte.
- Nessuna riga di questo capitolo e' un Obbligo: nessuno dei cinque punti
  impone un comportamento a un soggetto identificabile. I due paragrafi nuovi
  (§4 dell'art. 48 e §4 dell'art. 49) hanno contenuto di vigenza/transizione
  e non precettivo, e i restanti tre punti sono abrogazione, sostituzione e
  modifica di allegati. La questione e' dichiarata fra i dubbi aperti in
  chiusura di questo docstring.

Cosa e' escluso e perche':
- le disposizioni del regolamento modificato (Fonte 29, Reg. di esecuzione
  (UE) 2024/482) non sono nodi di questo modulo: gli articoli 23 e 24
  (cap04), l'articolo 48 e l'articolo 49 (cap08), l'allegato I (cap09) e
  l'allegato IV (cap11) di Fonte 29 restano dove sono e non vanno duplicati
  nell'atto modificativo;
- i paragrafi e le lettere interni al testo sostitutivo (il nuovo §4
  dell'art. 48, il nuovo §4 dell'art. 49) non sono indicizzati come unita'
  autonome e non ricevono un item di indice proprio: sono contenuto del punto
  che li introduce, come da regola per cui un punto che sostituisce un
  articolo e' una sola riga e il nuovo articolo non e' indicizzato come
  articolo autonomo della Fonte 30;
- paratesto -> nessun nodo e nessun item: l'intestazione "Articolo 1" con il
  chapeau "Il regolamento di esecuzione (UE) 2024/482 e' cosi' modificato:"
  (coperta dal cap01 di questa Fonte), il preambolo (considerando 1-14),
  l'epigrafe "Fatto a Bruxelles, il 18 dicembre 2024", la firma della
  presidente, la formula di chiusura dei regolamenti "Il presente regolamento
  e' obbligatorio in tutti i suoi elementi e direttamente applicabile in
  ciascuno degli Stati membri" (nel cap03, con l'articolo 3), le note a pie'
  di pagina (1)-(6) e la riga ELI/ISSN finali. Il punto e virgola di
  chiusura ";" che il testo ufficiale colloca su una riga a se' dopo il testo
  sostitutivo dei punti 5 e 6 e' stato ricucito al punto che lo precede
  (chiude la frase del punto, non apre un comma nuovo): nessuna riga porta un
  ";" orfano e nessuna riga e' stata tagliata.
- il considerando 12 collega la soppressione degli articoli 23 e 24 alla data
  di applicazione del regolamento di esecuzione (UE) 2024/3143: e' contesto
  preambolare, non testo dispositivo, e non entra nel `testo_integrale` ne'
  nel `testo` della riga "art. 1, punto 4".

Rinvii demandati alla fase 6 (nessuna relazione dichiarata in questo modulo:
le relazioni verso il regolamento modificato le costruisce la sessione
principale, e per ogni bersaglio e' indicato qui il `riferimento` con cui il
nodo e' dichiarato nel modulo di Fonte 29, per evitare KeyError):
- "art. 1, punto 4" -> abrogazione degli articoli 23 e 24 di Fonte 29
  (relazione "abroga"). In Fonte 29 l'art. 23 e' censito per commi ("art. 23
  §1" ... "art. 23 §5", cap04) e l'art. 24 come riga unica "art. 24" (cap04).
- "art. 1, punto 5" -> modifica ("modifica") dell'articolo 48 di Fonte 29, che
  aggiunge il paragrafo 4. In Fonte 29 le righe dell'articolo 48 sono "art. 48
  §1", "art. 48 §2", "art. 48 §3" (cap08); non esiste un nodo "art. 48" nudo.
- "art. 1, punto 6" -> modifica ("modifica") dell'articolo 49 di Fonte 29, che
  aggiunge il paragrafo 4. Le righe di Fonte 29 sono "art. 49 §1", "art. 49
  §2", "art. 49 §3" (cap08). Il testo inserito rinvia inoltre (relazione
  "richiama", evidence_type "textual") a: "articolo 3, paragrafo 2" del
  regolamento modificato, cioe' il testo del paragrafo 2 dell'articolo 3 come
  sostituito dall'art. 1, punto 2 di questa Fonte (cap01) - attenzione in fase
  6: in Fonte 29 esiste ancora il nodo "art. 3" con il testo previgente, e il
  rinvio va valutato insieme a "art. 1, punto 2" della Fonte 30; e al
  "riesame di cui al paragrafo 3", cioe' "art. 49 §3" di Fonte 29 (cap08).
- "art. 1, punto 7" -> sostituzione ("sostituisce") integrale dell'allegato I
  di Fonte 29 (righe "allegato I, punto 1" e "allegato I, punto 2", cap09)
  con il testo di cui all'allegato I di questa Fonte (cap04, che e' il modulo
  che copre quegli item di indice).
- "art. 1, punto 8" -> modifica ("modifica") dell'allegato IV di Fonte 29 per
  il tramite dell'allegato II di questa Fonte (cap05); in Fonte 29 il testo
  inciso sono i punti 5 e 6 della sezione IV.3 ("allegato IV, sezione IV.3,
  punto 5" e "allegato IV, sezione IV.3, punto 6", cap11).
- Rinvii interni al testo sostitutivo non modellati qui: "l'allegato I o II"
  del nuovo art. 48 §4 (allegato I di Fonte 29 = cap09, allegato II di Fonte
  29, entrambi incisi o affiancati dagli allegati di questa Fonte); "il
  presente regolamento" dei punti 6-8 e' il regolamento modificativo (Fonte
  30), non il regolamento modificato.

`oggetti_giuridici` non e' valorizzato per nessuna delle cinque righe: fra i
valori censiti in `oggetti_giuridici` non ce n'e' uno che corrisponda alla
certificazione di cibersicurezza EUCC, ai documenti sullo stato dell'arte o
agli allegati di un regolamento di esecuzione, e la voce generica "altro" non
e' stata forzata (stesso criterio del cap05, cap06, cap10, cap11, cap12 e
cap14 di Fonte 29). Nessuna riga valorizza `soggetti`, `severita'` o
`sanzioni`: l'atto non prevede sanzioni proprie ne' grada i requisiti.
`condizione_applicabilita` e' valorizzata solo per "art. 1, punto 6", la cui
norma opera unicamente nel riesame descritto dal testo; per "art. 1, punto 5"
la clausola "Salvo diversa indicazione nell'allegato I o II" e' una riserva
interna alla norma stessa, non un fatto esterno che la condizioni, e resta
quindi nel testo senza essere ripetuta nel campo. `stato` = "vigente" per
tutte le righe.

Copertura: 5 item di indice, 5 righe (0 Obblighi + 5 Principi), 0 relazioni
interne al modulo.

Dubbi di classificazione rimasti aperti (dichiarati, non risolti in modo
univoco dal testo):
(1) I due paragrafi inseriti (nuovo §4 dell'art. 48 e nuovo §4 dell'art. 49)
saranno, dal momento della loro applicazione, norme del regolamento
modificato e non dell'atto modificativo: chi legge l'atto modificativo come
mero veicolo potrebbe volerli censire in Fonte 29 invece che qui. Nulla
cambierebbe per il §4 dell'art. 49 (facolta' e definizione: Principio anche
nel regolamento modificato) e nemmeno per il §4 dell'art. 48 (norma di
applicazione): la differenza sarebbe la Fonte del nodo, non la sua
classificazione. Qui sono censiti nella Fonte dell'atto che li dispone, come
richiesto dal perimetro, e classificati sul testo che li enuncia.
(2) Il rinvio del nuovo art. 49 §4 all'"articolo 3, paragrafo 2" e' ambiguo
per costruzione, perche' lo stesso articolo 3 e' sostituito dall'art. 1,
punto 2 di questa Fonte: il nodo di Fonte 29 oggi in grafo porta il testo
previgente. La scelta di bersaglio in fase 6 va fatta con questa avvertenza,
non e' una svista del modulo.
(3) Punto 4: la soppressione degli articoli 23 e 24 e' collegata alla data di
applicazione del reg. (UE) 2024/3143 dal solo considerando 12, mentre il
testo dispositivo e' incondizionato; il nodo e' comunque "vigente". L'art. 3
di questa Fonte (cap03) prevede l'entrata in vigore il ventesimo giorno
successivo alla pubblicazione e una applicazione differita che il testo
ufficiale riferisce all'"articolo 1, paragrafo 4" dell'atto modificativo,
mentre l'art. 1 di questa Fonte e' numerato per punti: la lettura piu'
plausibile e' che si tratti del punto 4 qui censito, ma la formulazione
dell'atto non e' univoca e la data di applicazione non e' stata quindi
riportata nel testo della riga.
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 1, punto 4",
        "testo": "Gli articoli 23 e 24 del regolamento di esecuzione (UE) 2024/482 sono soppressi: "
                 "e' una disposizione abrogativa che elimina le norme sulla notifica degli organismi di "
                 "certificazione e delle ITSEF, senza imporre alcun comportamento a un soggetto.",
        "testo_integrale": "4) gli articoli 23 e 24 sono soppressi;",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 1, punto 5",
        "testo": "All'articolo 48 del regolamento di esecuzione (UE) 2024/482 e' aggiunto il paragrafo 4: "
                 "salvo diversa indicazione nell'allegato I o II, i documenti sullo stato dell'arte si "
                 "applicano a decorrere dalla data di applicazione dell'atto modificativo mediante il quale "
                 "sono stati introdotti nell'allegato I o II. E' una norma di applicazione dei documenti "
                 "sullo stato dell'arte, che non impone un comportamento a un soggetto.",
        "testo_integrale": "5) all'articolo 48 è aggiunto il seguente paragrafo 4: «4. Salvo diversa "
                           "indicazione nell'allegato I o II, i documenti sullo stato dell'arte si applicano "
                           "a decorrere dalla data di applicazione dell'atto modificativo mediante il quale "
                           "sono stati introdotti nell'allegato I o II.»;",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 1, punto 6",
        "testo": "All'articolo 49 del regolamento di esecuzione (UE) 2024/482 e' aggiunto il paragrafo 4: "
                 "nell'effettuare il riesame di cui al paragrafo 3 entro due anni dal rilascio del "
                 "certificato iniziale, e qualora tale riesame porti al rilascio di un nuovo certificato "
                 "conformemente a tale regolamento, possono essere applicate le norme di cui all'articolo 3, "
                 "paragrafo 2, e la data di rilascio del certificato iniziale e' intesa come la data di "
                 "rilascio dell'ultimo certificato per un prodotto TIC o un profilo di protezione su cui si "
                 "basa l'attuale certificazione. E' una facolta' accompagnata da una definizione, non un "
                 "obbligo.",
        "testo_integrale": "6) all'articolo 49 è aggiunto il seguente paragrafo 4: «4. Nell'effettuare il "
                           "riesame di cui al paragrafo 3 entro due anni dal rilascio del certificato "
                           "iniziale e qualora tale riesame porti al rilascio di un nuovo certificato "
                           "conformemente al presente regolamento, possono essere applicate le norme di cui "
                           "all'articolo 3, paragrafo 2. La data di rilascio del certificato iniziale è "
                           "intesa come la data di rilascio dell'ultimo certificato per un prodotto TIC o "
                           "un profilo di protezione su cui si basa l'attuale certificazione.»;",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Nell'effettuare il riesame di cui all'articolo 49, paragrafo 3, del "
                                    "regolamento di esecuzione (UE) 2024/482, entro due anni dal rilascio "
                                    "del certificato iniziale e qualora tale riesame porti al rilascio di un "
                                    "nuovo certificato conformemente a tale regolamento.",
    },
    {
        "riferimento": "art. 1, punto 7",
        "testo": "L'allegato I del regolamento di esecuzione (UE) 2024/482, recante i documenti sullo stato "
                 "dell'arte a sostegno dei settori tecnici e i documenti relativi all'accreditamento, e' "
                 "sostituito dal testo di cui all'allegato I di questo regolamento: e' una disposizione di "
                 "novella, che non impone un comportamento a un soggetto.",
        "testo_integrale": "7) l'allegato I è sostituito dal testo di cui all'allegato I del presente "
                           "regolamento;",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 1, punto 8",
        "testo": "L'allegato IV del regolamento di esecuzione (UE) 2024/482 e' modificato conformemente "
                 "all'allegato II di questo regolamento, che sostituisce i punti 5 e 6 della sezione IV.3 "
                 "relativi alla relazione di manutenzione: e' una disposizione di novella, che non impone un "
                 "comportamento a un soggetto.",
        "testo_integrale": "8) l'allegato IV è modificato conformemente all'allegato II del presente "
                           "regolamento.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 1, punto 4",
    "art. 1, punto 5",
    "art. 1, punto 6",
    "art. 1, punto 7",
    "art. 1, punto 8",
]

MAPPATURA_LOCALE = {
    "art. 1, punto 4": ["art. 1, punto 4"],
    "art. 1, punto 5": ["art. 1, punto 5"],
    "art. 1, punto 6": ["art. 1, punto 6"],
    "art. 1, punto 7": ["art. 1, punto 7"],
    "art. 1, punto 8": ["art. 1, punto 8"],
}

RELAZIONI = []
