"""Regolamento di esecuzione (UE) 2024/3144 della Commissione, del 18 dicembre
2024, che modifica il regolamento di esecuzione (UE) 2024/482 per quanto
riguarda le norme internazionali applicabili e che rettifica tale regolamento
di esecuzione (GU L, 2024/3144, 19.12.2024). Fonte 30 (`reg_ue_2024_3144`),
capitolo 3 di 5 (vedi app/.source_cache/reg_ue_2024_3144/manifest.json):
articoli 2-3 (rettifiche al regolamento di esecuzione (UE) 2024/482 ed entrata
in vigore). I punti 1-8 dell'articolo 1 sono coperti dal cap01 (punti 1-3) e
dal cap02 (punti 4-8), i due allegati dal cap04 e dal cap05: nessuno di quei
file e' toccato qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_3144/cap03.txt, tratto di
raw.txt compreso fra "Articolo 2" e l'inizio di "ALLEGATO I" (verificato:
cap03.txt coincide con quel tratto di raw.txt). Il raw.txt integrale e' stato
acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R3144, lingua italiana; URL
risolto
http://publications.europa.eu/resource/cellar/12c401d0-bdaa-11ef-91ed-01aa75ed71a1.0014.03/DOC_1,
XHTML della Gazzetta ufficiale; fetch 2026-09-29, 22.217 caratteri di testo,
sha256 del raw.txt
7ced6d4bfe633cf367b3c72ec593ebd5e49c369c7f86f4386984fe81cb81493a - dettagli in
provenance.json). L'epigrafe, i "visto" e i considerando stanno a monte
dell'articolo 1 e non sono in questa porzione.

Modellazione (ADR-0007, nessun comma o lettera con precetto autonomo non
coperto, nessuno coperto due volte):
- L'atto e' novellistico: le disposizioni di questo perimetro non introducono
  un precetto proprio, ma dispongono sostituzioni e una soppressione nel
  regolamento di esecuzione (UE) 2024/482 (Fonte 29) o fissano la vigenza
  dell'atto. Stesso trattamento del DPCM 19 ottobre 2021 (Fonte 6), l'altro
  atto censito interamente novellistico: ogni unita' dell'atto modificativo e'
  un nodo Principio tipo "altro" (in tassonomia non esiste un tipo dedicato
  alla novella o alla rettifica). Il contenuto prescrittivo che i punti
  introducono (per esempio il nuovo articolo 16 di Fonte 29, che impone al
  richiedente la certificazione di fornire le informazioni in forma completa e
  corretta) vive nella Fonte 29 e non e' censito qui: duplicarlo come Obbligo
  di questa Fonte darebbe due nodi dello stesso precetto, con un soggetto
  obbligato che il testo di questo atto non disciplina. Lettura alternativa
  dichiarata: classificando sulla sostanza del testo sostitutivo, i punti 1,
  2, 3 e 5 sarebbero Obblighi che ricalcano la classificazione dei nodi
  corrispondenti di Fonte 29 ("procedurale" per "art. 5 §1" del cap01 e per
  "art. 8 §1" del cap02, "procedurale" con soggetto "Terza parte" per
  "art. 16" del cap03, "sanzionatorio" con il campo sanzioni per "art. 29
  §2" del cap05) e solo il punto 4, abrogativo, resterebbe un Principio. Il
  cap01 di questa stessa Fonte ha in effetti classificato come Obbligo
  "procedurale" il punto 3 dell'articolo 1, che inserisce il nuovo articolo
  20 bis, mentre il cap02 ha tenuto i suoi cinque punti come Principi
  "altro". Qui prevale la lettura uniforme dei cinque punti come novelle
  (nessun precetto proprio, nessun duplicato dei nodi di Fonte 29); la
  divergenza e' fra moduli della Fonte, non dentro questo modulo, ed e'
  dichiarata fra i dubbi aperti.
- Unita' di copertura dell'articolo 2: i cinque punti numerati -> cinque
  righe, una per punto ("art. 2, punto 1" ... "art. 2, punto 5"), stessa
  granularita' con cui i punti 1-8 dell'articolo 1 sono coperti dal cap01 e
  dal cap02. Le lettere interne a un punto (le lettere a) e b) del punto 2,
  che sostituiscono rispettivamente il titolo e il paragrafo 1 dell'articolo 8
  di Fonte 29) restano nel testo_integrale della riga del punto che le
  dispone e non hanno item propri: sono le due operazioni di un'unica
  rettifica, non precetti autonomi - stesso criterio del DPCM 2021, art. 3, le
  cui lettere incidono su quattro disposizioni diverse dell'articolo 10 del
  DPCM 2014 e restano in un'unica riga. Se si volesse la granularita' per
  lettera, gli item sarebbero "art. 2, punto 2(a)" e "art. 2, punto 2(b)",
  mappati entrambi alla riga "art. 2, punto 2".
- Chapeau dell'articolo 2 (la formula che annuncia la rettifica) -> nessun
  nodo e nessun item: e' la formula introduttiva dell'elenco dei punti, senza
  contenuto normativo proprio; un item senza riga farebbe fallire
  verifica_copertura e una riga di sola formula sarebbe un nodo di puro
  annuncio (stessa scelta del chapeau nudo "I fornitori di portafogli:" in
  Reg. 2024/2979 art. 6 §3, che non riceve item ne' riga). La formula resta
  comunque verbatim in testa al testo_integrale di "art. 2, punto 1", insieme
  all'intestazione "Articolo 2", come l'intestazione e la rubrica degli
  articoli nelle Fonti gia' censite: nessuna parte del testo ufficiale di
  questa porzione resta fuori dai nodi. Dubbio aperto dichiarato: se la
  sessione principale preferisse un nodo anche per la formula che individua
  l'atto rettificato, la riga sarebbe "art. 2" (item "art. 2", testo_integrale
  = la sola formula); nessuna delle due letture rompe la copertura dei punti.
- Art. 3 -> due righe, per i due paragrafi non numerati con contenuto di
  vigenza: "art. 3, entrata in vigore" (l'entrata in vigore il ventesimo
  giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione
  europea) e "art. 3, applicazione" (l'articolo 1, paragrafo 4, si applica a
  decorrere dall'8 gennaio 2025), entrambi Principio tipo "altro": sono fatti
  giuridici temporali, senza soggetto obbligato. Convenzione delle Fonti
  regolamentari gia' censite per i paragrafi finali non numerati (Reg.
  2025/1566 "art. 2, entrata in vigore" e "art. 2, applicazione"; Reg.
  2024/482 "art. 50, entrata in vigore" e "art. 50, applicazione").
- Formula di chiusura dell'articolo 3 (ultimo periodo, sull'obbligatorieta' in
  tutti gli elementi e l'applicabilita' diretta negli Stati membri) -> nessun
  nodo: e' la formula standard di ogni regolamento UE self-executing, esclusa
  da tutte le Fonti UE gia' censite (Reg. 2025/1566, 2025/2531, 2025/2532,
  2024/2979, 2025/1569, 2015/1502), senza contenuto normativo distinto dalla
  forma giuridica "regolamento" gia' presupposta dal censimento. Non e' un
  comma numerato e l'articolo 3 resta coperto dai suoi due item.
- Paratesto -> nessun nodo: la firma ("Fatto a Bruxelles, il 18 dicembre
  2024", "Per la Commissione", "La presidente", "Ursula VON DER LEYEN") e le
  note a pie' di pagina (1)-(6) che corredano l'atto (nota (1) GU del
  regolamento (UE) 2019/881; (2) regolamento di esecuzione (UE) 2024/482;
  (3) regolamento di esecuzione (UE) 2016/799; (4) regolamento (UE)
  n. 910/2014; (5) decisione di esecuzione (UE) 2016/650; (6) regolamento di
  esecuzione (UE) 2024/3143). Le note sono corredo bibliografico degli atti
  citati, non disposizioni di questo regolamento: nessun nodo e nessuna
  relazione verso le Fonti citate. Precisazione sul paratesto finale: la riga
  ELI .../reg_impl/2024/3144/oj e la riga ISSN 1977-0707 non sono in questa
  porzione - raw.txt le riporta in coda all'ALLEGATO II, quindi sono nel cap05,
  mentre cap03.txt termina con la nota (6) (verificato sul file).
- testo_integrale: verbatim e integrale. Il marcatore del punto ("1)" ... "5)")
  e' unito al testo che segue; il marcatore della lettera sostituita ("b)") e'
  unito al testo della lettera dentro i medesimi caporali in cui il testo
  ufficiale la racchiude; la scansione tipografica colloca la punteggiatura
  finale del punto (";", ".") su una riga isolata dopo il blocco fra caporali
  ed e' stata ricucita in coda al blocco (profilo di protezione.»; e
  dell'articolo 20.».), senza togliere o aggiungere parole. Il testo
  sostitutivo introdotto dal punto 3 conserva l'intestazione "Articolo 16" e
  la rubrica, che il testo ufficiale premette al comma. Nessun marcatore di
  elisione (guardia verifica_completezza_testo_integrale, ADR-0010): il testo
  di questa porzione non contiene ellissi e non ne sono state introdotte. I
  simboli ufficiali (« », virgolette basse) sono conservati e il testo non e'
  stato corretto. `testo` e' la sintesi compressa di ciascun punto, che nomina
  anche l'articolo e il comma o la lettera della Fonte 29 incisi.
- Nessuna riga valorizza soggetti, oggetti_giuridici, severita' o sanzioni, e
  la sola riga con condizione_applicabilita e' "art. 3, applicazione": le
  righe di questo capitolo non impongono comportamenti propri e non si
  riferiscono a strumenti giuridici eIDAS (il perimetro dell'atto e' la
  certificazione EUCC dei prodotti TIC e dei profili di protezione, non un
  servizio fiduciario).
- RELAZIONI = []: il modulo non dichiara alcuna relazione. Nessuna riga di
  questo capitolo rinvia a un'altra riga di questo stesso modulo; tutti i
  bersagli dei rinvii (le disposizioni del regolamento di esecuzione (UE)
  2024/482 e i punti dell'articolo 1 di questa stessa Fonte) stanno fuori dal
  modulo, e quei collegamenti li costruisce la sessione principale in fase 6
  (ADR-0009), non questo file.

Rinvii demandati alla fase 6, riga per riga (tipo di intervento e bersaglio
verificati sul testo della Fonte 29 cosi' come censito nei suoi moduli):
- "art. 2, punto 1" -> sostituisce la lettera b) dell'articolo 5, paragrafo 1,
  del regolamento di esecuzione (UE) 2024/482: bersaglio il nodo "art. 5 §1"
  (cap01 di Fonte 29, item "art. 5 §1(b)"), che porta ancora il testo
  previgente ("integrando un profilo di protezione certificato come parte del
  processo TIC"); intervento parziale su una lettera di un paragrafo che resta
  in vigore: "modifica", non "sostituisce".
- "art. 2, punto 2" -> due interventi sull'articolo 8 di Fonte 29 nella stessa
  riga: la lettera a) sostituisce il titolo dell'articolo (che in Fonte 29 non
  ha un nodo proprio: la rubrica vive dentro il testo_integrale del nodo
  "art. 8 §1", cap02), la lettera b) sostituisce il paragrafo 1 (nodo
  "art. 8 §1", che porta "nel quadro dell'EUCC" e si chiude su "attivita' di
  certificazione.", mentre il testo rettificato dice "nell'ambito dell'EUCC" e
  "attivita' di certificazione e valutazione."); intervento parziale:
  "modifica".
- "art. 2, punto 3" -> sostituisce integralmente l'articolo 16 di Fonte 29,
  rubrica compresa: bersaglio il nodo "art. 16" (cap03 di Fonte 29, articolo
  senza commi numerati, che porta la rubrica "Informazioni necessarie per la
  certificazione dei profili di protezione" e non la formula "in forma
  completa e corretta"); intervento integrale su un articolo: "sostituisce".
- "art. 2, punto 4" -> sopprime il paragrafo 1 dell'articolo 17 di Fonte 29:
  bersaglio il nodo "art. 17 §1" (cap03 di Fonte 29); nessun testo sostitutivo
  introdotto: "abroga".
- "art. 2, punto 5" -> sostituisce il paragrafo 2 dell'articolo 29 di Fonte 29:
  bersaglio il nodo "art. 29 §2" (cap05 di Fonte 29), che porta ancora
  "revocato in conformita' degli articoli 14 e 20", mentre il testo rettificato
  dice "revocato in conformita' dell'articolo 14 o dell'articolo 20";
  intervento parziale su un paragrafo che resta in vigore: "modifica".
- "art. 3, applicazione" -> rinvio all'articolo 1, paragrafo 4, di questa
  stessa Fonte: il testo pubblicato usa "paragrafo 4" mentre l'articolo 1
  dell'atto enumera punti ("1)" ... "8)"), coperti dal cap01 (punti 1-3) e dal
  cap02 (punti 4-8). Il modulo riporta il rinvio come pubblicato e non lo
  interpreta: la scelta del nodo bersaglio spetta alla fase 6 (il punto 4
  dell'articolo 1 e' la soppressione degli articoli 23 e 24 di Fonte 29). In
  ogni caso e' un collegamento interno alla Fonte, non fra fonti, e quindi non
  dichiarabile qui.
- Rinvii interni ai testi sostitutivi, che appartengono alla Fonte 29: il
  nuovo articolo 16 richiama l'articolo 8, paragrafi 2, 3, 4 e 7, e il nuovo
  paragrafo 2 dell'articolo 29 richiama il paragrafo 1 dello stesso articolo
  29, l'articolo 30, l'articolo 14 e l'articolo 20. Sono rinvii dentro il
  regolamento rettificato: eventuali relazioni vanno costruite sulla Fonte 29,
  non da questa riga.
- Nessun'altra Fonte e' citata nel testo di questa porzione: il regolamento
  (UE) 2019/881 e il regolamento di esecuzione (UE) 2016/799 compaiono solo
  nelle note a pie' di pagina (1) e (3), che non sono censite.

Copertura: 7 item di indice (i 5 punti dell'articolo 2 e i 2 paragrafi con
contenuto dell'articolo 3), 7 righe (0 Obblighi + 7 Principi), 0 relazioni.

Dubbi di classificazione rimasti aperti (dichiarati, non risolti in modo
univoco dal testo):
(1) Obbligo o Principio per i punti che sostituiscono una disposizione con
un testo prescrittivo (punti 1, 2, 3 e 5): la lettura qui adottata - novella,
quindi Principio tipo "altro" - e' quella del DPCM 2021 e del cap02 di questa
Fonte, ma il cap01 di questa Fonte ha classificato come Obbligo il punto che
introduce il nuovo articolo 20 bis. La scelta incide solo sul tipo di nodo e
sul campo tipo_obbligo, non sulla copertura: se la sessione principale
volesse allineare i moduli, i punti 1, 2, 3 e 5 diventerebbero Obblighi
"procedurale" (il 5 con il campo sanzioni, come "art. 29 §2" di Fonte 29) e
resterebbero invariati riferimenti, testi_integrali e item di indice.
(2) Chapeau dell'articolo 2: qui non riceve ne' riga ne' item (e' verbatim in
testa al testo_integrale di "art. 2, punto 1"). L'alternativa - riga
"art. 2" con item "art. 2" - e' praticabile senza toccare i cinque punti, ma
introdurrebbe un nodo di sola formula di annuncio; il cap01 e il cap02 di
questa Fonte hanno scelto come qui (il chapeau sta nella prima riga del primo
punto), il cap05 ha invece dato al proprio chapeau una riga e un item propri
perche' quel chapeau nomina il regolamento, la sezione e i punti incisi.
(3) Le lettere a) e b) del punto 2 restano nella riga del punto senza item
propri, come nei punti 1-8 dell'articolo 1 coperti dal cap01 e dal cap02; il
cap04 e il cap05 di questa Fonte indicizzano invece le lettere (e i punti
numerati) interni ai testi sostitutivi degli allegati, che sono contenuto e
non operazioni di novella. Se si volesse la stessa granularita' qui, gli item
sarebbero "art. 2, punto 2(a)" e "art. 2, punto 2(b)", entrambi mappati alla
riga "art. 2, punto 2".
(4) Il rinvio del secondo paragrafo dell'articolo 3 all'"articolo 1,
paragrafo 4" dell'atto e' ambiguo per costruzione (l'articolo 1 e' numerato
per punti): qui e' riportato come pubblicato, con la lettura piu' plausibile
indicata nella sezione dei rinvii di fase 6 (punto 4 dell'articolo 1, censito
nel cap02) e la stessa avvertenza del cap02 di questa Fonte, che non ha
riportato la data nella riga "art. 1, punto 4".
"""

RIGHE_OBBLIGHI: list[dict] = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 2, punto 1",
        "testo": "Rettifica sostitutiva: la lettera b) dell'articolo 5, paragrafo 1, del regolamento di esecuzione (UE) 2024/482 è sostituita dalla lettera che prevede di dichiarare la conformità a un profilo di protezione certificato come parte del processo TIC, qualora il prodotto TIC rientri nella categoria di prodotti TIC contemplata da tale profilo di protezione.",
        "testo_integrale": "Articolo 2\n\nIl regolamento di esecuzione (UE) 2024/482 è così rettificato:\n\n1) all'articolo 5, paragrafo 1, la lettera b) è sostituita dalla seguente: «b) dichiarando la conformità a un profilo di protezione certificato come parte del processo TIC, qualora il prodotto TIC rientri nella categoria di prodotti TIC contemplata da tale profilo di protezione.»;",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2, punto 2",
        "testo": "Rettifica sostitutiva dell'articolo 8 del regolamento di esecuzione (UE) 2024/482 su due punti: la lettera a) sostituisce il titolo dell'articolo con «Informazioni necessarie per la certificazione e la valutazione»; la lettera b) sostituisce il paragrafo 1, secondo cui il richiedente la certificazione nell'ambito dell'EUCC fornisce o mette altrimenti a disposizione dell'organismo di certificazione e dell'ITSEF tutte le informazioni necessarie per le attività di certificazione e valutazione.",
        "testo_integrale": "2) l'articolo 8 è così rettificato:\n\na) il titolo è sostituito dal seguente: «Informazioni necessarie per la certificazione e la valutazione»;\n\nb) il paragrafo 1 è sostituito dal seguente: «1. Il richiedente la certificazione nell'ambito dell'EUCC fornisce o mette altrimenti a disposizione dell'organismo di certificazione e dell'ITSEF tutte le informazioni necessarie per le attività di certificazione e valutazione.»;",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2, punto 3",
        "testo": "Rettifica sostitutiva integrale dell'articolo 16 del regolamento di esecuzione (UE) 2024/482: il nuovo testo dell'articolo (rubrica «Informazioni necessarie per la certificazione e la valutazione dei profili di protezione») impone al richiedente la certificazione di un profilo di protezione di fornire o mettere altrimenti a disposizione dell'organismo di certificazione e dell'ITSEF tutte le informazioni, in forma completa e corretta, necessarie per le attività di certificazione e valutazione, e richiama in via di applicazione mutatis mutandis l'articolo 8, paragrafi 2, 3, 4 e 7, dello stesso regolamento.",
        "testo_integrale": "3) l'articolo 16 è sostituito dal seguente: «\nArticolo 16\n\nInformazioni necessarie per la certificazione e la valutazione dei profili di protezione\n\nIl richiedente la certificazione di un profilo di protezione fornisce o mette altrimenti a disposizione dell'organismo di certificazione e dell'ITSEF tutte le informazioni, in forma completa e corretta, necessarie per le attività di certificazione e valutazione. Si applicano, mutatis mutandis, le disposizioni dell'articolo 8, paragrafi 2, 3, 4 e 7.»;",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2, punto 4",
        "testo": "Rettifica abrogativa: il paragrafo 1 dell'articolo 17 del regolamento di esecuzione (UE) 2024/482 è soppresso, senza alcun testo sostitutivo.",
        "testo_integrale": "4) all'articolo 17, il paragrafo 1 è soppresso;",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2, punto 5",
        "testo": "Rettifica sostitutiva: il paragrafo 2 dell'articolo 29 del regolamento di esecuzione (UE) 2024/482 è sostituito dal paragrafo secondo cui, se il titolare del certificato EUCC non propone misure correttive adeguate durante il periodo di cui al paragrafo 1, il certificato è sospeso in conformità dell'articolo 30 o revocato in conformità dell'articolo 14 o dell'articolo 20.",
        "testo_integrale": "5) all'articolo 29, il paragrafo 2 è sostituito dal seguente: «2. Se il titolare del certificato EUCC non propone misure correttive adeguate durante il periodo di cui al paragrafo 1, il certificato è sospeso in conformità dell'articolo 30 o revocato in conformità dell'articolo 14 o dell'articolo 20.».",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 3, entrata in vigore",
        "testo": "Il presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea.",
        "testo_integrale": "Articolo 3\n\nIl presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 3, applicazione",
        "testo": "L'articolo 1, paragrafo 4, del presente regolamento si applica a decorrere dall'8 gennaio 2025: è la disposizione che fissa l'applicazione temporalmente delimitata di una singola prescrizione dell'atto.",
        "testo_integrale": "L'articolo 1, paragrafo 4, si applica a decorrere dall'8 gennaio 2025.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Disposizione di applicazione temporalmente delimitata: l'articolo 1, paragrafo 4, si applica a decorrere dall'8 gennaio 2025.",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 2, punto 1",
    "art. 2, punto 2",
    "art. 2, punto 3",
    "art. 2, punto 4",
    "art. 2, punto 5",
    "art. 3, entrata in vigore",
    "art. 3, applicazione",
]

MAPPATURA_LOCALE = {
    "art. 2, punto 1": ["art. 2, punto 1"],
    "art. 2, punto 2": ["art. 2, punto 2"],
    "art. 2, punto 3": ["art. 2, punto 3"],
    "art. 2, punto 4": ["art. 2, punto 4"],
    "art. 2, punto 5": ["art. 2, punto 5"],
    "art. 3, entrata in vigore": ["art. 3, entrata in vigore"],
    "art. 3, applicazione": ["art. 3, applicazione"],
}

RELAZIONI: list[dict] = []
