"""Regolamento di esecuzione (UE) 2024/482 della Commissione, del 31 gennaio
2024 - modalita' di applicazione del regolamento (UE) 2019/881 del Parlamento
europeo e del Consiglio per quanto riguarda l'adozione del sistema europeo di
certificazione della cibersicurezza basato sui criteri comuni (EUCC). Fonte 29
(slug `reg_ue_2024_482`), capitolo 12 di 14 (vedi
app/.source_cache/reg_ue_2024_482/manifest.json): Allegato V - Contenuto della
relazione di certificazione, per intero (sezione "V.1 Relazione di
certificazione", punti 1-19; sezione "V.2 Adattamento di un traguardo di
sicurezza ai fini della pubblicazione", punti 1-4). Gli artt. 1-50 e gli
allegati I-IV e VI-IX appartengono ai capitoli 1-11 e 13-14 della stessa
Fonte, assegnati ad altri moduli: nessuno di quei file e' toccato qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_482/cap12.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R0482, lingua italiana; URL
risolto
http://publications.europa.eu/resource/cellar/687c0d05-c580-11ee-95d9-01aa75ed71a1.0014.03/DOC_1,
XHTML della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 540.435 byte
scaricati, 135.367 caratteri di testo, sha256 del raw.txt
b46d08cab6d63b2c190ae767042c07c1fc324955c22ef491eb314556b28ca5b8 - dettagli
completi in app/.source_cache/reg_ue_2024_482/provenance.json). Il perimetro e'
stato verificato con un diff: le 364 righe di cap12.txt sono identiche alla
porzione di raw.txt compresa fra l'intestazione "ALLEGATO V" (riga 1899 del
raw.txt) e la riga che precede "ALLEGATO VI" (riga 2263), quindi il capitolo
contiene l'allegato per intero e nient'altro. Il preambolo (considerando
1-33), l'epigrafe, la firma, le note a pie' di pagina e la formula di chiusura
stanno in altre porzioni del documento; la riga ELI e la riga "ISSN 1977-0707
(electronic edition)" chiudono il documento in coda all'allegato IX (cap14).

Modellazione (ADR-0007, nessun punto dell'allegato non coperto, nessuno
coperto due volte):
- Unita' di riga: il punto numerato. Le due sezioni dell'allegato sono
  organizzate in punti numerati che ricominciano da 1, e ogni punto enuncia il
  proprio precetto in un chapeau ("La relazione di certificazione contiene
  almeno le sezioni seguenti:", "La sintesi ... include le informazioni
  seguenti:", "Il contenuto del traguardo di sicurezza adattato e' conforme ai
  requisiti minimi seguenti:") di cui le lettere e le voci numerate sono
  l'elenco: le lettere restano nel `testo_integrale` della riga del punto e
  ricevono item di indice propri. E' la convenzione gia' in uso in questa
  stessa Fonte (cap02: art. 9 §1 e §2, art. 10 §1; cap06: art. 35 §2, "un
  comma = una riga, lettere comprese") e nel cap09 di questa Fonte ("un punto
  numerato = una riga, lettere comprese": i due settori tecnici e le relative
  lettere dell'allegato I stanno in una riga sola), non quella del cap10 (una
  riga per lettera), che li' era giustificata perche' in quell'allegato la
  lettera designava essa stessa una categoria di prodotti TIC e i profili
  raccomandati per essa. Nota del capitolo ("censisci i sottopunti con
  precetto autonomo come righe proprie solo se portano un requisito
  distinto") applicata e documentata: nessuna lettera di questo allegato porta
  un requisito distinto dal punto che la regge - sono voci di elenco rette dal
  chapeau, senza soggetto e senza verbo proprio (punto 3: i nomi delle sezioni
  della relazione; punti 4, 5, 13, 14, 18: i nomi delle informazioni da
  includere; punti 7 e 9: le politiche e le ipotesi da rappresentare) - con
  l'eccezione dichiarata del punto 3 della sezione V.2, le cui lettere sono
  frasi compiute con verbo proprio; vedi i dubbi lasciati aperti in chiusura.
- Punti 1-7 e 9-15, 18 e 19 della sezione V.1 -> Obblighi. L'allegato e'
  interamente dedicato al contenuto della relazione di certificazione che
  l'organismo di certificazione deve elaborare a norma dell'art. 10 §4 (cap02),
  e i punti che prescrivono che cosa la relazione, la sua sintesi o una sua
  sezione deve contenere (punti 2-7, 9-15, 18, 19) sono Obblighi
  "informativo/trasparenza": e' la stessa classificazione che il cap02 da'
  all'art. 10 §1-§2 (contenuto del certificato e della relazione di
  certificazione), cioe' ai requisiti sull'informazione resa al mercato e al
  titolare. Il punto 1 e' Obbligo "procedurale" (soggetto: l'organismo di
  certificazione che redige e pubblica la relazione - come l'art. 10 §4 del
  cap02, anch'esso "procedurale").
- Punti 8, 16 e 17 della sezione V.1 -> Principi "altro". Sono gli unici tre
  punti puramente permissivi dell'allegato - "la politica puo' includere le
  condizioni relative all'utilizzo di una procedura di gestione delle patch"
  (punto 8), "il traguardo di sicurezza puo' essere adattato in conformita'
  della sezione VI.2" (punto 16), "il marchio o l'etichetta ... possono essere
  inseriti nella relazione di certificazione" (punto 17) - e una facolta' non
  impone un comportamento a un soggetto identificabile: stessa classificazione
  usata dal cap01 di Reg. 2025/2532 per la facolta' dell'art. 1 §2 ("possono
  avvalersi di un servizio di conservazione qualificato") e dal cap05 di
  Reg. 2024/2979 per l'allegato III ("gli utenti del portafoglio possono
  divulgare ..."). Il punto 16 e il punto 17 rinviano per l'esercizio della
  facolta' a un'altra disposizione (sezione V.2 per il primo, art. 11 per il
  secondo): il rinvio non trasforma la facolta' in obbligo.
- Punti 1-4 della sezione V.2: punto 1 -> Principio "altro" (facolta' di
  adattare il traguardo di sicurezza rimuovendo o parafrasando le informazioni
  tecniche proprietarie); punto 2 -> Obbligo "informativo/trasparenza", perche'
  pur essendo la prosecuzione della facolta' del punto 1 contiene un divieto
  ("il traguardo di sicurezza adattato non puo' omettere le informazioni
  necessarie per comprendere le proprieta' di sicurezza ... e l'ambito della
  valutazione"); punto 3 -> Obbligo "informativo/trasparenza" (requisiti minimi
  di contenuto del traguardo adattato); punto 4 -> Obbligo "procedurale"
  (l'organismo di certificazione garantisce la conformita' del traguardo
  adattato a quello completo e valutato e indica entrambe le versioni nella
  relazione: garanzia interna al procedimento di certificazione, come l'art. 9
  §1 e l'art. 10 §4 del cap02).
- Soggetti: l'allegato non nomina il soggetto tenuto, che i punti descrivono in
  forma impersonale o passiva ("la relazione di certificazione contiene ...",
  "il prodotto TIC valutato e' chiaramente identificato", "e' fornito un elenco
  completo ..."). La categoria "Terza parte" (ruolo "obbligato") e' stata
  assegnata a tutte le righe di Obbligo, perche' il soggetto e' l'organismo di
  certificazione, che a norma dell'art. 10 §4 (cap02) elabora la relazione in
  conformita' dell'allegato V: e' la stessa deduzione che il cap05 di questa
  Fonte documenta per l'art. 30 §5 ("la sospensione ... e' notificata", forma
  passiva senza soggetto nominato) e la stessa categoria che il cap02 usa per
  l'organismo di certificazione. Il ruolo "destinatario" e' valorizzato solo
  dove il testo nomina o identifica chi beneficia dell'informazione:
  "Terzi affidanti/pubblico" nei punti 1 (relazione "da pubblicare insieme al
  corrispondente certificato EUCC"), 2 ("rilevanti per gli utenti e i portatori
  di interesse"), 10 ("consentire agli utenti del prodotto TIC certificato di
  prendere decisioni consapevoli") e 15 ("fornito insieme alla stessa ai fini
  della pubblicazione"). Nessuna riga ha soggetto o destinatario
  "QTSP/gestore": l'atto non riguarda i servizi fiduciari qualificati.
- `oggetti_giuridici` non valorizzato per nessuna riga (ne' sui tre Principi
  ne' sugli Obblighi, che non lo prevedono): fra i valori censiti non ce n'e'
  uno che corrisponda a "prodotto TIC", "categoria di prodotti TIC",
  "relazione di certificazione" o "traguardo di sicurezza", e la voce generica
  "altro" non e' stata forzata (stesso criterio del cap09 e del cap10 di questa
  Fonte).
- Nessuna riga valorizza `severita` o `sanzioni`: l'atto non gradua i requisiti
  ne' prevede sanzioni proprie (l'apparato sanzionatorio dell'EUCC sta nel
  regolamento (UE) 2019/881, non in questo regolamento di esecuzione, come gia'
  rilevato dai cap01-cap11). `stato` = "vigente" per tutte le righe; la data di
  applicazione differita dell'allegato V e' fissata dall'art. 50 §2 (cap08:
  il regolamento si applica dal 27 febbraio 2025, il capo IV e l'allegato V
  dalla data di entrata in vigore) e non e' stata replicata riga per riga:
  sarebbe una `condizione_applicabilita` desunta, non enunciata dai punti.
  `condizione_applicabilita` e' valorizzata sulle tre righe dei punti 2, 3 e 4
  della sezione V.2, che presuppongono l'adattamento del traguardo di
  sicurezza ai fini della pubblicazione disciplinato dal punto 1 della stessa
  sezione ("il traguardo di sicurezza adattato che ne risulta", "anche se il
  traguardo di sicurezza adattato non e' formalmente valutato"). Il punto 8
  della sezione V.1 si apre con "Se applicabile", ma la condizione non e'
  specificata dal testo e non e' stata inventata: resta dichiarata nel `testo`
  come il testo ufficiale la formula.
- Riferimenti: "allegato V, sezione V.1, punto 3", con lettera "allegato V,
  sezione V.1, punto 3(a)" e con voce numerata "allegato V, sezione V.1, punto
  4(e)(1)" (stessa forma di "allegato III, punto 2(a)" e "allegato I, punto
  1(a)(1)"). La sezione e' indicata nel riferimento perche' i punti
  ricominciano da 1 in ciascuna delle due sezioni e un "allegato V, punto 1"
  sarebbe ambiguo fra la sezione V.1 e la sezione V.2; e' anche la forma con
  cui il cap05 di questa Fonte nomina la sezione IV.2 dell'allegato IV ("il
  bersaglio e' censito ... allegato IV, sezione IV.2"). Nessun item a livello
  di allegato ("allegato V"): l'intestazione e il titolo dell'allegato sono
  paratesto e i punti sono numerati, quindi un item unico non sarebbe mappabile
  su 23 righe distinte (criterio del cap09 di questa Fonte). Refuso del testo
  ufficiale da non correggere (ADR-0010): i due rinvii interni del testo
  ufficiale citano le sezioni come "VI.1" e "VI.2" (sezione V.1 punto 16,
  sezione V.2 punto 1) mentre le intestazioni delle sezioni sono "V.1" e
  "V.2"; nel `testo_integrale` i rinvii sono riportati verbatim ("sezione
  VI.2", "sezione VI.1, punto 1") e le relazioni di questo modulo puntano alle
  righe della sezione V.2, che e' la sezione effettivamente intesa.
- `testo_integrale`: verbatim e integrale, ricucito dalle righe spezzate dalla
  conversione XHTML -> testo. I marcatori isolati su riga propria ("1."-"19."
  per i punti, "(a)"-"(l)" per le lettere, "(1)"-"(8)" per le voci numerate)
  sono riuniti al testo che seguono, per esempio "1. Sulla base delle relazioni
  tecniche di valutazione fornite dall'ITSEF, ..." e "(a) sintesi;"; ogni
  punto, lettera o voce resta in un blocco separato da riga vuota nell'ordine
  del testo ufficiale. La punteggiatura ufficiale e' conservata com'e',
  compreso il punto fermo dopo "bibliografia." (lettera (l) del punto 3) e
  l'uso del congiuntivo "se diversa" in "il nome dell'ITSEF che ha effettuato
  la valutazione, se diversa dall'organismo di certificazione" (lettera (b) del
  punto 13). Nessun marcatore di elisione (vincolo
  `verifica_completezza_testo_integrale`, ADR-0010). `testo` e' invece la
  sintesi compressa (1-3 frasi) di ogni riga, che nomina gli elementi
  richiesti per renderli cercabili senza aprire l'integrale.
- RELAZIONI: sei, tutte fra righe di questo modulo e tutte rinvii letterali
  verificati sul `testo_integrale` della riga citante, quindi `evidence_type`
  = "textual": (1) sezione V.1 punto 10 -> sezione V.1 punto 9 ("Le
  informazioni elencate al punto 9 sono il piu' possibile comprensibili"); (2)
  sezione V.1 punto 16 -> le quattro righe della sezione V.2 ("puo' essere
  adattato in conformita' della sezione VI.2"): la citazione e' letterale e
  riguarda la sezione nel suo complesso, e poiche' il grafo non ha nodi di
  sezione la relazione e' dichiarata verso ciascuna delle quattro righe che la
  compongono (stesso trattamento riservato dal cap05 al rinvio dell'art. 29 §1
  "agli articoli 27 e 41", dichiarato verso entrambi i commi dell'art. 27);
  (6) sezione V.2 punto 1 -> sezione V.1 punto 1 ("a norma della sezione VI.1,
  punto 1"). `confidence` = None su tutte (ADR-0005: nessuno score reale da
  riportare, non va inventato). Nessuna relazione verso altri capitoli di
  questa Fonte o verso altre Fonti: le costruisce la sessione principale in
  fase 6, e dichiararle qui in import parallelo per capitolo imporrebbe di
  indovinare i `riferimento` dei nodi scritti da moduli paralleli (un
  riferimento sbagliato fa fallire il seed con KeyError).
- Rinvii demandati alla fase 6 (nessuna relazione dichiarata qui; accanto a
  ogni rinvio e' indicato il `riferimento` con cui il nodo bersaglio e'
  dichiarato, o si prevede che sia dichiarato, nel modulo del capitolo che lo
  contiene):
  * verso altri capitoli di questa Fonte: art. 3 (norme e criteri di
    valutazione della sicurezza), citato in V.1 punto 13(c) ("in base alle
    norme di cui all'articolo 3"), V.2 punto 3(f) e V.2 punto 4 -> riga "art.
    3" (cap01); art. 4 (livelli di affidabilita'), citato in V.1 punto 14(a)
    ("di cui all'articolo 4 del presente regolamento") -> riga "art. 4" (cap01);
    art. 7 §1(c) (uso previsto del prodotto TIC), citato in V.1 punto 9
    ("come indicato nell'articolo 7, paragrafo 1, lettera c)") -> riga "art. 7
    §1" (cap02); art. 11 (norme e procedure di utilizzo del marchio e
    dell'etichetta), citato in V.1 punto 17 -> righe "art. 11 §1" e "art. 11
    §2" (cap02); allegato IV, sezione IV.4 (procedura di gestione delle patch
    approvata), citato in V.1 punto 4(e)(7) -> cap11 (non ancora scritto: il
    capitolo cita la stessa sezione come "allegato IV, sezione IV.2" per
    l'altra sezione, quindi si prevede "allegato IV, sezione IV.4, punto N").
  * rinvii entranti, da costruire sui nodi di questo modulo: art. 10 §4 (cap02,
    "elabora una relazione di certificazione in conformita' dell'allegato V
    per ciascun certificato EUCC rilasciato") -> l'allegato nel suo complesso,
    per il quale l'ancora piu' vicina e' la riga "allegato V, sezione V.1,
    punto 1" (elaborazione e pubblicazione della relazione) insieme alla riga
    "allegato V, sezione V.1, punto 3" (sezioni che la relazione contiene);
    art. 11 §4(b) (cap02, le informazioni sulla certificazione degli allegati V
    e VII nel sito web collegato al codice QR) -> le stesse due righe; art. 50
    §2 (cap08, applicazione del capo IV e dell'allegato V a partire dalla data
    di entrata in vigore) -> tutte le righe dell'allegato; cap14 ricorda nella
    propria docstring il rinvio del "allegato V punto 17" all'articolo 11 ->
    riga "allegato V, sezione V.1, punto 17" di questo modulo.
  * verso altre Fonti: articolo 55 del regolamento (UE) 2019/881 (informazioni
    supplementari sulla cibersicurezza che il titolare del certificato rende
    pubbliche), citato in V.1 punto 5(g) e V.1 punto 12, e articolo 52 del
    medesimo regolamento (livelli di affidabilita'), citato in V.1 punto
    4(e)(2) e V.1 punto 14(a): il regolamento (UE) 2019/881 non e' fra le
    Fonti censite in docs/fonti-censite.md e non esistono nodi bersaglio in
    `app/seed_data/`; nessun arco, come per gli stessi rinvii nei cap02 e
    cap05 di questa Fonte. I "criteri comuni" e la progettazione dei
    sottosistemi ADV_TDS nominati in V.1 punto 11, i profili di protezione
    nominati in V.1 punto 13(f), le norme citate in V.1 punto 13(c) e le
    politiche del titolare nominate in V.1 punto 7 non sono Fonti del
    censimento: nessun arco.

Copertura: 89 item di indice, 23 righe (19 Obblighi + 4 Principi), 6 relazioni
interne.

Dubbi di classificazione rimasti aperti (dichiarati, non risolti in modo
univoco dal testo):
(1) Punto 3 della sezione V.2 (requisiti minimi del traguardo di sicurezza
adattato) tenuto come una riga sola con le nove lettere come item, mentre le
lettere (a) e (b) e (d)-(h) enunciano obblighi distinti con verbo proprio e le
lettere (c), (g) e (i) facolta' distinte ("puo' essere ridotta", "possono
essere adattate"): la lettura alternativa e' una riga per lettera, con la
lettera del chapeau come riga a se' (come fa il cap10 per il chapeau
dell'allegato III) e con tre delle nove lettere classificate Principio. La
scelta fatta privilegia l'uniformita' dell'unita' di riga (il punto numerato)
e non perde informazione, perche' le nove lettere restano integrali nel
`testo_integrale` della riga e hanno item di indice propri; chi preferisse la
granularita' per lettera puo' scindere la riga senza toccare la copertura,
perche' gli item esistono gia' tutti.
(2) Punto 2 della sezione V.1 come Obbligo "informativo/trasparenza": la prima
meta' del punto e' descrittiva ("La relazione di certificazione e' la fonte di
informazioni dettagliate e pratiche ...") e la seconda e' una precisazione di
contenuto ("pertanto include tutte le informazioni disponibili e condivisibili
pubblicamente rilevanti per gli utenti e i portatori di interesse"), con una
facolta' in coda ("puo' fare riferimento a informazioni disponibili e
condivisibili pubblicamente"). E' stata seguita la parte prescrittiva sul
contenuto; chi leggesse il punto come descrizione dell'oggetto della relazione
lo classificherebbe Principio "altro" (come il chapeau del cap10) e il
`testo_integrale` resterebbe invariato.
(3) Punto 19 della sezione V.1 come "informativo/trasparenza": l'identificazione
univoca della documentazione (data di rilascio e numero di versione corretti)
serve alla riproducibilita' della valutazione ed e' anche un adempimento
documentale; "procedurale" resta una lettura difendibile.
(4) Punto 4 della sezione V.2 come "procedurale": vi convivono la garanzia di
conformita' (controllo interno al procedimento) e l'indicazione di entrambe le
versioni del traguardo nella relazione (informativo/trasparenza). La prima ha
prevalso, con la stessa scelta fatta dal cap02 per l'art. 9 §1 e per i commi
sulla relazione di certificazione.
(5) Soggetto "Terza parte" dedotto per tutte le righe di Obbligo: l'allegato
non nomina alcun soggetto e i titolari di certificato EUCC, gli ITSEF e le
autorita' di certificazione nazionali compaiono solo come termini delle
informazioni da rappresentare (punti 4(b), 5(e), 5(g), 7, 13(a), 13(b),
13(f)(4)), non come soggetti tenuti. In alternativa nessuna riga avrebbe
`soggetti` valorizzati, come nel cap09 e nel cap10 di questa Fonte; la deduzione
segue l'art. 10 §4 del cap02 e la convenzione del cap05.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "allegato V, sezione V.1, punto 1",
        "testo": "Sulla base delle relazioni tecniche di valutazione fornite dall'ITSEF, l'organismo di certificazione redige una relazione di certificazione da pubblicare insieme al corrispondente certificato EUCC.",
        "testo_integrale": "1. Sulla base delle relazioni tecniche di valutazione fornite dall'ITSEF, l'organismo di certificazione redige una relazione di certificazione da pubblicare insieme al corrispondente certificato EUCC.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 2",
        "testo": "La relazione di certificazione è la fonte di informazioni dettagliate e pratiche sul prodotto TIC o sulla categoria di prodotti TIC e sulla diffusione sicura degli stessi, e include pertanto tutte le informazioni disponibili e condivisibili pubblicamente rilevanti per gli utenti e i portatori di interesse; può fare riferimento a informazioni disponibili e condivisibili pubblicamente.",
        "testo_integrale": "2. La relazione di certificazione è la fonte di informazioni dettagliate e pratiche sul prodotto TIC o sulla categoria di prodotti TIC e sulla diffusione sicura degli stessi, e pertanto include tutte le informazioni disponibili e condivisibili pubblicamente rilevanti per gli utenti e i portatori di interesse. La relazione di certificazione può fare riferimento a informazioni disponibili e condivisibili pubblicamente.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 3",
        "testo": "La relazione di certificazione contiene almeno dodici sezioni: sintesi; identificazione del prodotto TIC o della categoria di prodotti TIC per i profili di protezione; servizi di sicurezza; ipotesi e chiarimento dell'ambito di applicazione; informazioni sull'architettura; informazioni supplementari sulla cibersicurezza, se applicabili; prove del prodotto TIC, se sono state eseguite; se del caso, identificazione dei processi di gestione del ciclo di vita e degli impianti di produzione del titolare del certificato; risultati della valutazione e informazioni relative al certificato; sintesi del traguardo di sicurezza del prodotto TIC sottoposto a certificazione; se disponibile, marchio o etichetta associati al sistema; bibliografia.",
        "testo_integrale": "3. La relazione di certificazione contiene almeno le sezioni seguenti:\n\n(a) sintesi;\n\n(b) identificazione del prodotto TIC o della categoria di prodotti TIC per i profili di protezione;\n\n(c) servizi di sicurezza;\n\n(d) ipotesi e chiarimento dell'ambito di applicazione;\n\n(e) informazioni sull'architettura;\n\n(f) informazioni supplementari sulla cibersicurezza, se applicabili;\n\n(g) prove del prodotto TIC, se sono state eseguite;\n\n(h) se del caso, l'identificazione dei processi di gestione del ciclo di vita e degli impianti di produzione del titolare del certificato;\n\n(i) risultati della valutazione e informazioni relative al certificato;\n\n(j) sintesi del traguardo di sicurezza del prodotto TIC sottoposto a certificazione;\n\n(k) se disponibile, il marchio o l'etichetta associati al sistema;\n\n(l) bibliografia.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 4",
        "testo": "La sintesi è un breve riassunto dell'intera relazione di certificazione, con una panoramica chiara e concisa dei risultati della valutazione, e contiene: nome del prodotto TIC valutato, componenti oggetto della valutazione e versione; nome dell'ITSEF che ha effettuato la valutazione e, se del caso, elenco dei subcontraenti; data di conclusione della valutazione; riferimento alla relazione tecnica di valutazione redatta dall'ITSEF; breve descrizione dei risultati, tra cui versione e eventuale release dei criteri comuni applicati, pacchetto di affidabilità e componenti della garanzia della sicurezza (livello AVA_VAN applicato e livello di affidabilità di cui all'articolo 52 del regolamento (UE) 2019/881), funzionalità di sicurezza, sintesi delle minacce e delle politiche di sicurezza organizzativa, requisiti speciali di configurazione, ipotesi sull'ambiente operativo, eventuale presenza di una procedura di gestione delle patch approvata in conformità dell'allegato IV, sezione IV.4, e una o più clausole di esclusione della responsabilità.",
        "testo_integrale": "4. La sintesi è un breve riassunto dell'intera relazione di certificazione. La sintesi fornisce una panoramica chiara e concisa dei risultati della valutazione e include le informazioni seguenti:\n\n(a) nome del prodotto TIC valutato, elenco dei componenti del prodotto che fanno parte della valutazione e versione del prodotto TIC;\n\n(b) nome dell'ITSEF che ha effettuato la valutazione e se del caso elenco dei subcontraenti;\n\n(c) data di conclusione della valutazione;\n\n(d) riferimento alla relazione tecnica di valutazione redatta dall'ITSEF;\n\n(e) breve descrizione dei risultati della relazione di certificazione, tra cui:\n\n(1) la versione e l'eventuale release dei criteri comuni applicata alla valutazione;\n\n(2) il pacchetto di affidabilità dei criteri comuni e i componenti della garanzia della sicurezza, compreso il livello AVA_VAN applicato durante la valutazione e il corrispondente livello di affidabilità di cui all'articolo 52 del regolamento (UE) 2019/881 a cui si riferisce il certificato EUCC;\n\n(3) la funzionalità di sicurezza del prodotto TIC valutato;\n\n(4) una sintesi delle minacce e delle politiche di sicurezza organizzativa trattate dal prodotto TIC valutato;\n\n(5) requisiti speciali di configurazione;\n\n(6) ipotesi sull'ambiente operativo;\n\n(7) se applicabile, la presenza di una procedura di gestione delle patch approvata in conformità dell'allegato IV, sezione IV.4;\n\n(8) una o più clausole di esclusione della responsabilità.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 5",
        "testo": "Il prodotto TIC valutato è chiaramente identificato, anche indicando: il nome del prodotto TIC valutato; l'elenco dei componenti che fanno parte della valutazione; il numero di versione dei componenti; l'identificazione di requisiti aggiuntivi per l'ambiente operativo del prodotto TIC certificato; il nome e le informazioni di contatto del titolare del certificato EUCC; ove applicabile, la procedura di gestione delle patch inclusa nel certificato; il link al sito web del titolare del certificato EUCC con le informazioni supplementari sulla cibersicurezza in conformità dell'articolo 55 del regolamento (UE) 2019/881.",
        "testo_integrale": "5. Il prodotto TIC valutato è chiaramente identificato, anche indicando le informazioni seguenti:\n\n(a) il nome del prodotto TIC valutato;\n\n(b) un elenco dei componenti del prodotto TIC che fanno parte della valutazione;\n\n(c) il numero di versione dei componenti del prodotto TIC;\n\n(d) l'identificazione di requisiti aggiuntivi per l'ambiente operativo del prodotto TIC certificato;\n\n(e) il nome e le informazioni di contatto del titolare del certificato EUCC;\n\n(f) ove applicabile, la procedura di gestione delle patch inclusa nel certificato;\n\n(g) il link al sito web del titolare del certificato EUCC dove sono fornite informazioni supplementari sulla cibersicurezza per il prodotto TIC certificato in conformità dell'articolo 55 del regolamento (UE) 2019/881.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 6",
        "testo": "Le informazioni incluse in questa sezione sono il più possibile accurate, per garantire una rappresentazione completa e precisa del prodotto TIC che può essere riutilizzata nelle valutazioni future.",
        "testo_integrale": "6. Le informazioni incluse in questa sezione sono il più possibile accurate per garantire una rappresentazione completa e precisa del prodotto TIC che può essere riutilizzata nelle valutazioni future.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 7",
        "testo": "La sezione sulle politiche di sicurezza contiene la descrizione della politica di sicurezza del prodotto TIC, nonché delle politiche o norme che il prodotto TIC valutato applica o rispetta, e include un riferimento e una descrizione della politica di gestione delle vulnerabilità del titolare del certificato e della politica di continuità dell'affidabilità del titolare del certificato.",
        "testo_integrale": "7. La sezione sulle politiche di sicurezza contiene la descrizione della politica di sicurezza del prodotto TIC, nonché le politiche o le norme che il prodotto TIC valutato applica o rispetta. Essa include un riferimento e una descrizione delle politiche seguenti:\n\n(a) la politica di gestione delle vulnerabilità del titolare del certificato;\n\n(b) la politica di continuità dell'affidabilità del titolare del certificato.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 9",
        "testo": "La sezione relativa alle ipotesi e al chiarimento dell'ambito di applicazione contiene informazioni esaurienti sulle circostanze e sugli obiettivi relativi all'uso previsto del prodotto, come indicato nell'articolo 7, paragrafo 1, lettera c): ipotesi sull'utilizzo e sulla diffusione del prodotto TIC sotto forma di requisiti minimi, come la corretta installazione e configurazione e il soddisfacimento dei requisiti hardware, e ipotesi sull'ambiente per il funzionamento del prodotto TIC nel rispetto delle norme.",
        "testo_integrale": "9. La sezione relativa alle ipotesi e al chiarimento dell'ambito di applicazione contiene informazioni esaurienti sulle circostanze e sugli obiettivi relativi all'uso previsto del prodotto, come indicato nell'articolo 7, paragrafo 1, lettera c). Le informazioni comprendono:\n\n(a) ipotesi sull'utilizzo e sulla diffusione del prodotto TIC sotto forma di requisiti minimi, come la corretta installazione e configurazione e il soddisfacimento dei requisiti hardware;\n\n(b) ipotesi sull'ambiente per il funzionamento del prodotto TIC nel rispetto delle norme.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 10",
        "testo": "Le informazioni elencate al punto 9 sono il più possibile comprensibili, in modo da consentire agli utenti del prodotto TIC certificato di prendere decisioni consapevoli sui rischi associati al suo utilizzo.",
        "testo_integrale": "10. Le informazioni elencate al punto 9 sono il più possibile comprensibili, in modo da consentire agli utenti del prodotto TIC certificato di prendere decisioni consapevoli sui rischi associati al suo utilizzo.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 11",
        "testo": "La sezione relativa alle informazioni sull'architettura include una descrizione di alto livello del prodotto TIC e dei suoi componenti principali in conformità con la progettazione dei sottosistemi ADV_TDS dei criteri comuni.",
        "testo_integrale": "11. La sezione relativa alle informazioni sull'architettura include una descrizione di alto livello del prodotto TIC e dei suoi componenti principali in conformità con la progettazione dei sottosistemi ADV_TDS dei criteri comuni.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 12",
        "testo": "In conformità dell'articolo 55 del regolamento (UE) 2019/881 è fornito un elenco completo delle informazioni supplementari sulla cibersicurezza del prodotto TIC, e tutta la documentazione pertinente è indicata con i numeri di versione.",
        "testo_integrale": "12. In conformità dell'articolo 55 del regolamento (UE) 2019/881 è fornito un elenco completo delle informazioni supplementari sulla cibersicurezza del prodotto TIC. Tutta la documentazione pertinente è indicata con i numeri di versione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 13",
        "testo": "La sezione relativa alle prove del prodotto TIC include: il nome e il punto di contatto dell'autorità o dell'organismo che ha rilasciato il certificato, compresa l'autorità nazionale di certificazione della cibersicurezza responsabile; il nome dell'ITSEF che ha effettuato la valutazione, se diversa dall'organismo di certificazione; l'identificazione dei componenti dell'affidabilità utilizzati in base alle norme di cui all'articolo 3; la versione del documento sullo stato dell'arte e ulteriori criteri di valutazione della sicurezza utilizzati; le impostazioni e la configurazione complete e precise del prodotto TIC durante la valutazione, comprese le note e le osservazioni operative, se disponibili; l'eventuale profilo di protezione utilizzato, con autore, nome e identificatore, identificatore del certificato, nome e dati di contatto dell'organismo di certificazione e dell'ITSEF coinvolti nella valutazione del profilo di protezione e pacchetto o pacchetti di affidabilità richiesti per un prodotto conforme al profilo di protezione.",
        "testo_integrale": "13. La sezione relativa alle prove del prodotto TIC include le informazioni seguenti:\n\n(a) il nome e il punto di contatto dell'autorità o dell'organismo che ha rilasciato il certificato, compresa l'autorità nazionale di certificazione della cibersicurezza responsabile;\n\n(b) il nome dell'ITSEF che ha effettuato la valutazione, se diversa dall'organismo di certificazione;\n\n(c) l'identificazione dei componenti dell'affidabilità utilizzati in base alle norme di cui all'articolo 3;\n\n(d) la versione del documento sullo stato dell'arte e ulteriori criteri di valutazione della sicurezza utilizzati nella valutazione;\n\n(e) le impostazioni e la configurazione complete e precise del prodotto TIC durante la valutazione, comprese le note e le osservazioni operative, se disponibili;\n\n(f) l'eventuale profilo di protezione utilizzato, comprese le informazioni seguenti:\n\n(1) l'autore del profilo di protezione;\n\n(2) il nome e l'identificatore del profilo di protezione;\n\n(3) l'identificatore del certificato del profilo di protezione;\n\n(4) il nome e i dati di contatto dell'organismo di certificazione e dell'ITSEF coinvolti nella valutazione del profilo di protezione;\n\n(5) il pacchetto o i pacchetti di affidabilità richiesti per un prodotto conforme al profilo di protezione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 14",
        "testo": "La sezione relativa ai risultati della valutazione e alle informazioni sul certificato include: la conferma del livello di affidabilità raggiunto di cui all'articolo 4 del presente regolamento e all'articolo 52 del regolamento (UE) 2019/881; i requisiti di affidabilità in base alle norme di cui all'articolo 3 che il prodotto TIC o il profilo di protezione effettivamente soddisfa, compreso il livello AVA_VAN; la descrizione dettagliata dei requisiti di affidabilità e delle modalità con cui il prodotto soddisfa ciascuno di essi; la data di rilascio e il periodo di validità del certificato; l'identificatore unico del certificato.",
        "testo_integrale": "14. La sezione relativa ai risultati della valutazione e alle informazioni sul certificato include le informazioni seguenti:\n\n(a) conferma del livello di affidabilità raggiunto di cui all'articolo 4 del presente regolamento e all'articolo 52 del regolamento (UE) 2019/881;\n\n(b) requisiti di affidabilità in base alle norme di cui all'articolo 3 che il prodotto TIC o il profilo di protezione effettivamente soddisfa, compreso il livello AVA_VAN;\n\n(c) descrizione dettagliata dei requisiti di affidabilità, nonché informazioni dettagliate relative alle modalità con cui il prodotto soddisfa ciascuno di essi;\n\n(d) la data di rilascio e il periodo di validità del certificato;\n\n(e) l'identificatore unico del certificato.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 15",
        "testo": "Il traguardo di sicurezza è incluso oppure menzionato e riassunto nella relazione di certificazione e fornito insieme alla stessa ai fini della pubblicazione.",
        "testo_integrale": "15. Il traguardo di sicurezza è incluso oppure menzionato e riassunto nella relazione di certificazione e fornito insieme alla stessa ai fini della pubblicazione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 18",
        "testo": "La sezione relativa alla bibliografia contiene i riferimenti a tutti i documenti utilizzati per la compilazione della relazione di certificazione e comprende almeno: i criteri di valutazione della sicurezza, i documenti sullo stato dell'arte e le altre specifiche pertinenti utilizzati e la loro versione; la relazione tecnica di valutazione; la relazione tecnica di valutazione per la valutazione dei compositi, ove applicabile; la documentazione tecnica di riferimento; la documentazione dello sviluppatore utilizzata per la valutazione.",
        "testo_integrale": "18. La sezione relativa alla bibliografia contiene i riferimenti a tutti i documenti utilizzati per la compilazione della relazione di certificazione. Tali informazioni comprendono almeno gli elementi seguenti:\n\n(a) i criteri di valutazione della sicurezza, i documenti sullo stato dell'arte e altre specifiche pertinenti utilizzati e la loro versione;\n\n(b) la relazione tecnica di valutazione;\n\n(c) la relazione tecnica di valutazione per la valutazione dei compositi, ove applicabile;\n\n(d) la documentazione tecnica di riferimento;\n\n(e) la documentazione dello sviluppatore utilizzata per la valutazione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 19",
        "testo": "Al fine di garantire la riproducibilità della valutazione, tutta la documentazione a cui si fa riferimento deve essere identificata in modo univoco con la data di rilascio e il numero di versione corretti.",
        "testo_integrale": "19. Al fine di garantire la riproducibilità della valutazione, tutta la documentazione a cui si fa riferimento deve essere identificata in modo univoco con la data di rilascio e il numero di versione corretti.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato V, sezione V.2, punto 2",
        "testo": "Il traguardo di sicurezza adattato è una rappresentazione reale della sua versione originale completa e non può omettere le informazioni necessarie per comprendere le proprietà di sicurezza dell'oggetto della valutazione e l'ambito della valutazione.",
        "testo_integrale": "2. Il traguardo di sicurezza adattato che ne risulta è una rappresentazione reale della sua versione originale completa. Ciò significa che il traguardo di sicurezza adattato non può omettere le informazioni necessarie per comprendere le proprietà di sicurezza dell'oggetto della valutazione e l'ambito della valutazione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica al traguardo di sicurezza adattato ai fini della pubblicazione (sezione V.2, punto 1).",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato V, sezione V.2, punto 3",
        "testo": "Il contenuto del traguardo di sicurezza adattato è conforme ai requisiti minimi seguenti: l'introduzione non è adattata, perché generalmente non contiene informazioni proprietarie; il traguardo adattato ha un identificatore unico, distinto dalla versione originale completa; la descrizione dell'oggetto della valutazione può essere ridotta se contiene informazioni proprietarie e dettagli di progettazione che non dovrebbero essere pubblicati; la descrizione dell'ambiente di sicurezza (ipotesi, minacce, politiche di sicurezza organizzativa) non è ridotta nella misura necessaria a comprendere l'ambito della valutazione; gli obiettivi di sicurezza non sono ridotti; tutti i requisiti di sicurezza sono resi pubblici, e le note applicative possono spiegare come sono stati utilizzati i requisiti funzionali dei criteri comuni di cui all'articolo 3; la sintesi delle specifiche dell'oggetto della valutazione include tutte le sue funzioni di sicurezza, mentre le informazioni proprietarie aggiuntive possono essere adattate; sono inclusi i riferimenti ai profili di protezione applicati all'oggetto della valutazione; le motivazioni possono essere adattate per rimuovere le informazioni proprietarie.",
        "testo_integrale": "3. Il contenuto del traguardo di sicurezza adattato è conforme ai requisiti minimi seguenti:\n\n(a) la sua introduzione non è adattata, dal momento che generalmente non contiene informazioni proprietarie;\n\n(b) il traguardo di sicurezza adattato deve avere un identificatore unico, distinto dalla sua versione originale completa;\n\n(c) la descrizione dell'oggetto della valutazione può essere ridotta in quanto potrebbe includere informazioni proprietarie e dettagliate sulla progettazione dell'oggetto della valutazione che non dovrebbero essere pubblicate;\n\n(d) la descrizione dell'ambiente di sicurezza dell'oggetto della valutazione (ipotesi, minacce, politiche di sicurezza organizzativa) non è ridotta, nella misura in cui tali informazioni siano necessarie per comprendere l'ambito della valutazione;\n\n(e) gli obiettivi di sicurezza non sono ridotti, poiché tutte le informazioni devono essere rese pubbliche per comprendere l'intenzione del traguardo di sicurezza e dell'oggetto della valutazione;\n\n(f) tutti i requisiti di sicurezza sono resi pubblici. Le note applicative possono fornire informazioni sulle modalità con cui i requisiti funzionali dei criteri comuni di cui all'articolo 3 sono stati utilizzati per comprendere il traguardo di sicurezza;\n\n(g) la sintesi delle specifiche dell'oggetto della valutazione include tutte le funzioni di sicurezza dell'oggetto della valutazione, ma le informazioni proprietarie aggiuntive possono essere adattate;\n\n(h) sono inclusi i riferimenti ai profili di protezione applicati all'oggetto della valutazione;\n\n(i) le motivazioni possono essere adattate al fine di rimuovere le informazioni proprietarie.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica al traguardo di sicurezza adattato ai fini della pubblicazione (sezione V.2, punto 1).",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato V, sezione V.2, punto 4",
        "testo": "Anche se il traguardo di sicurezza adattato non è formalmente valutato in conformità delle norme di valutazione di cui all'articolo 3, l'organismo di certificazione garantisce che sia conforme al traguardo di sicurezza completo e valutato e che nella relazione di certificazione siano indicati sia il traguardo di sicurezza completo sia quello adattato.",
        "testo_integrale": "4. Anche se il traguardo di sicurezza adattato non è formalmente valutato in conformità delle norme di valutazione di cui all'articolo 3, l'organismo di certificazione garantisce che sia conforme al traguardo di sicurezza completo e valutato e che nella relazione di certificazione siano indicati sia il traguardo di sicurezza completo sia quello adattato.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica al traguardo di sicurezza adattato ai fini della pubblicazione (sezione V.2, punto 1).",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "allegato V, sezione V.1, punto 8",
        "testo": "Facoltà e non obbligo: se applicabile, la politica può includere le condizioni relative all'utilizzo di una procedura di gestione delle patch durante la validità del certificato. Il testo non specifica quale fatto renda applicabile la condizione.",
        "testo_integrale": "8. Se applicabile, la politica può includere le condizioni relative all'utilizzo di una procedura di gestione delle patch durante la validità del certificato.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 16",
        "testo": "Facoltà e non obbligo: il traguardo di sicurezza può essere adattato in conformità della sezione VI.2 dell'allegato (il testo ufficiale cita la sezione come \"VI.2\" mentre l'intestazione della sezione è \"V.2\").",
        "testo_integrale": "16. Il traguardo di sicurezza può essere adattato in conformità della sezione VI.2.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato V, sezione V.1, punto 17",
        "testo": "Facoltà e non obbligo: il marchio o l'etichetta associati all'EUCC possono essere inseriti nella relazione di certificazione in conformità delle norme e delle procedure stabilite dall'articolo 11.",
        "testo_integrale": "17. Il marchio o l'etichetta associati all'EUCC possono essere inseriti nella relazione di certificazione in conformità delle norme e delle procedure stabilite dall'articolo 11.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato V, sezione V.2, punto 1",
        "testo": "Facoltà e non obbligo: il traguardo di sicurezza da includere o a cui si fa riferimento nella relazione di certificazione a norma della sezione VI.1, punto 1, può essere adattato rimuovendo o parafrasando le informazioni tecniche proprietarie (il testo ufficiale cita la sezione come \"VI.1\" mentre l'intestazione della sezione è \"V.1\").",
        "testo_integrale": "1. Il traguardo di sicurezza da includere o a cui si fa riferimento nella relazione di certificazione a norma della sezione VI.1, punto 1, può essere adattato rimuovendo o parafrasando le informazioni tecniche proprietarie.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "allegato V, sezione V.1, punto 1",
    "allegato V, sezione V.1, punto 2",
    "allegato V, sezione V.1, punto 3",
    "allegato V, sezione V.1, punto 3(a)",
    "allegato V, sezione V.1, punto 3(b)",
    "allegato V, sezione V.1, punto 3(c)",
    "allegato V, sezione V.1, punto 3(d)",
    "allegato V, sezione V.1, punto 3(e)",
    "allegato V, sezione V.1, punto 3(f)",
    "allegato V, sezione V.1, punto 3(g)",
    "allegato V, sezione V.1, punto 3(h)",
    "allegato V, sezione V.1, punto 3(i)",
    "allegato V, sezione V.1, punto 3(j)",
    "allegato V, sezione V.1, punto 3(k)",
    "allegato V, sezione V.1, punto 3(l)",
    "allegato V, sezione V.1, punto 4",
    "allegato V, sezione V.1, punto 4(a)",
    "allegato V, sezione V.1, punto 4(b)",
    "allegato V, sezione V.1, punto 4(c)",
    "allegato V, sezione V.1, punto 4(d)",
    "allegato V, sezione V.1, punto 4(e)",
    "allegato V, sezione V.1, punto 4(e)(1)",
    "allegato V, sezione V.1, punto 4(e)(2)",
    "allegato V, sezione V.1, punto 4(e)(3)",
    "allegato V, sezione V.1, punto 4(e)(4)",
    "allegato V, sezione V.1, punto 4(e)(5)",
    "allegato V, sezione V.1, punto 4(e)(6)",
    "allegato V, sezione V.1, punto 4(e)(7)",
    "allegato V, sezione V.1, punto 4(e)(8)",
    "allegato V, sezione V.1, punto 5",
    "allegato V, sezione V.1, punto 5(a)",
    "allegato V, sezione V.1, punto 5(b)",
    "allegato V, sezione V.1, punto 5(c)",
    "allegato V, sezione V.1, punto 5(d)",
    "allegato V, sezione V.1, punto 5(e)",
    "allegato V, sezione V.1, punto 5(f)",
    "allegato V, sezione V.1, punto 5(g)",
    "allegato V, sezione V.1, punto 6",
    "allegato V, sezione V.1, punto 7",
    "allegato V, sezione V.1, punto 7(a)",
    "allegato V, sezione V.1, punto 7(b)",
    "allegato V, sezione V.1, punto 8",
    "allegato V, sezione V.1, punto 9",
    "allegato V, sezione V.1, punto 9(a)",
    "allegato V, sezione V.1, punto 9(b)",
    "allegato V, sezione V.1, punto 10",
    "allegato V, sezione V.1, punto 11",
    "allegato V, sezione V.1, punto 12",
    "allegato V, sezione V.1, punto 13",
    "allegato V, sezione V.1, punto 13(a)",
    "allegato V, sezione V.1, punto 13(b)",
    "allegato V, sezione V.1, punto 13(c)",
    "allegato V, sezione V.1, punto 13(d)",
    "allegato V, sezione V.1, punto 13(e)",
    "allegato V, sezione V.1, punto 13(f)",
    "allegato V, sezione V.1, punto 13(f)(1)",
    "allegato V, sezione V.1, punto 13(f)(2)",
    "allegato V, sezione V.1, punto 13(f)(3)",
    "allegato V, sezione V.1, punto 13(f)(4)",
    "allegato V, sezione V.1, punto 13(f)(5)",
    "allegato V, sezione V.1, punto 14",
    "allegato V, sezione V.1, punto 14(a)",
    "allegato V, sezione V.1, punto 14(b)",
    "allegato V, sezione V.1, punto 14(c)",
    "allegato V, sezione V.1, punto 14(d)",
    "allegato V, sezione V.1, punto 14(e)",
    "allegato V, sezione V.1, punto 15",
    "allegato V, sezione V.1, punto 16",
    "allegato V, sezione V.1, punto 17",
    "allegato V, sezione V.1, punto 18",
    "allegato V, sezione V.1, punto 18(a)",
    "allegato V, sezione V.1, punto 18(b)",
    "allegato V, sezione V.1, punto 18(c)",
    "allegato V, sezione V.1, punto 18(d)",
    "allegato V, sezione V.1, punto 18(e)",
    "allegato V, sezione V.1, punto 19",
    "allegato V, sezione V.2, punto 1",
    "allegato V, sezione V.2, punto 2",
    "allegato V, sezione V.2, punto 3",
    "allegato V, sezione V.2, punto 3(a)",
    "allegato V, sezione V.2, punto 3(b)",
    "allegato V, sezione V.2, punto 3(c)",
    "allegato V, sezione V.2, punto 3(d)",
    "allegato V, sezione V.2, punto 3(e)",
    "allegato V, sezione V.2, punto 3(f)",
    "allegato V, sezione V.2, punto 3(g)",
    "allegato V, sezione V.2, punto 3(h)",
    "allegato V, sezione V.2, punto 3(i)",
    "allegato V, sezione V.2, punto 4",
]

# Le lettere e le voci numerate di ogni punto sono mappate alla riga del punto
# che le regge (un punto = una riga, lettere comprese: convenzione del cap02,
# del cap06 e del cap09 di questa Fonte, vedi la docstring).
MAPPATURA_LOCALE = {
    "allegato V, sezione V.1, punto 1": ["allegato V, sezione V.1, punto 1"],
    "allegato V, sezione V.1, punto 2": ["allegato V, sezione V.1, punto 2"],
    "allegato V, sezione V.1, punto 3": [
        "allegato V, sezione V.1, punto 3",
        "allegato V, sezione V.1, punto 3(a)",
        "allegato V, sezione V.1, punto 3(b)",
        "allegato V, sezione V.1, punto 3(c)",
        "allegato V, sezione V.1, punto 3(d)",
        "allegato V, sezione V.1, punto 3(e)",
        "allegato V, sezione V.1, punto 3(f)",
        "allegato V, sezione V.1, punto 3(g)",
        "allegato V, sezione V.1, punto 3(h)",
        "allegato V, sezione V.1, punto 3(i)",
        "allegato V, sezione V.1, punto 3(j)",
        "allegato V, sezione V.1, punto 3(k)",
        "allegato V, sezione V.1, punto 3(l)",
    ],
    "allegato V, sezione V.1, punto 4": [
        "allegato V, sezione V.1, punto 4",
        "allegato V, sezione V.1, punto 4(a)",
        "allegato V, sezione V.1, punto 4(b)",
        "allegato V, sezione V.1, punto 4(c)",
        "allegato V, sezione V.1, punto 4(d)",
        "allegato V, sezione V.1, punto 4(e)",
        "allegato V, sezione V.1, punto 4(e)(1)",
        "allegato V, sezione V.1, punto 4(e)(2)",
        "allegato V, sezione V.1, punto 4(e)(3)",
        "allegato V, sezione V.1, punto 4(e)(4)",
        "allegato V, sezione V.1, punto 4(e)(5)",
        "allegato V, sezione V.1, punto 4(e)(6)",
        "allegato V, sezione V.1, punto 4(e)(7)",
        "allegato V, sezione V.1, punto 4(e)(8)",
    ],
    "allegato V, sezione V.1, punto 5": [
        "allegato V, sezione V.1, punto 5",
        "allegato V, sezione V.1, punto 5(a)",
        "allegato V, sezione V.1, punto 5(b)",
        "allegato V, sezione V.1, punto 5(c)",
        "allegato V, sezione V.1, punto 5(d)",
        "allegato V, sezione V.1, punto 5(e)",
        "allegato V, sezione V.1, punto 5(f)",
        "allegato V, sezione V.1, punto 5(g)",
    ],
    "allegato V, sezione V.1, punto 6": ["allegato V, sezione V.1, punto 6"],
    "allegato V, sezione V.1, punto 7": [
        "allegato V, sezione V.1, punto 7",
        "allegato V, sezione V.1, punto 7(a)",
        "allegato V, sezione V.1, punto 7(b)",
    ],
    "allegato V, sezione V.1, punto 8": ["allegato V, sezione V.1, punto 8"],
    "allegato V, sezione V.1, punto 9": [
        "allegato V, sezione V.1, punto 9",
        "allegato V, sezione V.1, punto 9(a)",
        "allegato V, sezione V.1, punto 9(b)",
    ],
    "allegato V, sezione V.1, punto 10": ["allegato V, sezione V.1, punto 10"],
    "allegato V, sezione V.1, punto 11": ["allegato V, sezione V.1, punto 11"],
    "allegato V, sezione V.1, punto 12": ["allegato V, sezione V.1, punto 12"],
    "allegato V, sezione V.1, punto 13": [
        "allegato V, sezione V.1, punto 13",
        "allegato V, sezione V.1, punto 13(a)",
        "allegato V, sezione V.1, punto 13(b)",
        "allegato V, sezione V.1, punto 13(c)",
        "allegato V, sezione V.1, punto 13(d)",
        "allegato V, sezione V.1, punto 13(e)",
        "allegato V, sezione V.1, punto 13(f)",
        "allegato V, sezione V.1, punto 13(f)(1)",
        "allegato V, sezione V.1, punto 13(f)(2)",
        "allegato V, sezione V.1, punto 13(f)(3)",
        "allegato V, sezione V.1, punto 13(f)(4)",
        "allegato V, sezione V.1, punto 13(f)(5)",
    ],
    "allegato V, sezione V.1, punto 14": [
        "allegato V, sezione V.1, punto 14",
        "allegato V, sezione V.1, punto 14(a)",
        "allegato V, sezione V.1, punto 14(b)",
        "allegato V, sezione V.1, punto 14(c)",
        "allegato V, sezione V.1, punto 14(d)",
        "allegato V, sezione V.1, punto 14(e)",
    ],
    "allegato V, sezione V.1, punto 15": ["allegato V, sezione V.1, punto 15"],
    "allegato V, sezione V.1, punto 16": ["allegato V, sezione V.1, punto 16"],
    "allegato V, sezione V.1, punto 17": ["allegato V, sezione V.1, punto 17"],
    "allegato V, sezione V.1, punto 18": [
        "allegato V, sezione V.1, punto 18",
        "allegato V, sezione V.1, punto 18(a)",
        "allegato V, sezione V.1, punto 18(b)",
        "allegato V, sezione V.1, punto 18(c)",
        "allegato V, sezione V.1, punto 18(d)",
        "allegato V, sezione V.1, punto 18(e)",
    ],
    "allegato V, sezione V.1, punto 19": ["allegato V, sezione V.1, punto 19"],
    "allegato V, sezione V.2, punto 1": ["allegato V, sezione V.2, punto 1"],
    "allegato V, sezione V.2, punto 2": ["allegato V, sezione V.2, punto 2"],
    "allegato V, sezione V.2, punto 3": [
        "allegato V, sezione V.2, punto 3",
        "allegato V, sezione V.2, punto 3(a)",
        "allegato V, sezione V.2, punto 3(b)",
        "allegato V, sezione V.2, punto 3(c)",
        "allegato V, sezione V.2, punto 3(d)",
        "allegato V, sezione V.2, punto 3(e)",
        "allegato V, sezione V.2, punto 3(f)",
        "allegato V, sezione V.2, punto 3(g)",
        "allegato V, sezione V.2, punto 3(h)",
        "allegato V, sezione V.2, punto 3(i)",
    ],
    "allegato V, sezione V.2, punto 4": ["allegato V, sezione V.2, punto 4"],
}

# Relazioni interne all'allegato V, tutte rinvii letterali verificati sul
# `testo_integrale` della riga citante (evidence_type "textual"):
# - sezione V.1 punto 10 -> sezione V.1 punto 9 ("Le informazioni elencate al
#   punto 9 sono il piu' possibile comprensibili");
# - sezione V.1 punto 16 -> ciascuna delle quattro righe della sezione V.2
#   ("Il traguardo di sicurezza puo' essere adattato in conformita' della
#   sezione VI.2"): la citazione e' letterale ma riguarda la sezione nel suo
#   complesso e il grafo non ha nodi di sezione, quindi la relazione e'
#   dichiarata verso tutte le righe che la compongono;
# - sezione V.2 punto 1 -> sezione V.1 punto 1 ("da includere o a cui si fa
#   riferimento nella relazione di certificazione a norma della sezione VI.1,
#   punto 1"): il testo ufficiale scrive "VI.1" dove l'intestazione della
#   sezione e' "V.1" (refuso non corretto, ADR-0010), e il bersaglio e' la
#   riga della sezione V.1 che disciplina l'elaborazione della relazione.
# I rinvii ad altri capitoli di questa Fonte (art. 3, art. 4, art. 7 §1(c),
# art. 11, allegato IV sezione IV.4) e ad altre Fonti (articolo 52 e articolo
# 55 del regolamento (UE) 2019/881), nonche' i rinvii entranti (art. 10 §4,
# art. 11 §4(b), art. 50 §2), sono elencati nella docstring sotto "rinvii
# demandati alla fase 6": dichiararli qui imporrebbe di indovinare i
# `riferimento` dei nodi scritti da moduli paralleli e un riferimento sbagliato
# fa fallire il seed con KeyError. `confidence` = None: nessuno score reale da
# riportare (ADR-0005).
RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "allegato V, sezione V.1, punto 10"),
        "nodo_a": ("obbligo", None, "allegato V, sezione V.1, punto 9"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # NOTA DI REVISIONE (2026-09-29, sessione principale, da
    # `verifica_relazioni_textual.py --fonte-id 29`): il punto 16 della sezione
    # V.1 rinvIa "alla sezione VI.2", ma la sezione che disciplina l'adattamento
    # del traguardo di sicurezza ai fini della pubblicazione e' la V.2 ("V.2
    # Adattamento di un traguardo di sicurezza ai fini della pubblicazione"):
    # nel testo ufficiale la numerazione romana di questi rinvii interni e'
    # sbagliata di uno (stessa anomalia documentata nel campo `testo` di
    # "allegato V, sezione V.2, punto 1", che cita "VI.1" per la V.1). Il
    # bersaglio e' quindi scelto per contenuto, non per citazione letterale:
    # `evidence_type` e' "inferred" (non "textual") e la confidence e' 0.70.
    # Nessun arco verso "allegato VI, sezione VI.2", che riguarda la
    # composizione del gruppo di valutazione inter pares e non l'adattamento del
    # traguardo di sicurezza.
    {
        "nodo_da": ("principio", None, "allegato V, sezione V.1, punto 16"),
        "nodo_a": ("principio", None, "allegato V, sezione V.2, punto 1"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": 0.70,
    },
    {
        "nodo_da": ("principio", None, "allegato V, sezione V.1, punto 16"),
        "nodo_a": ("obbligo", None, "allegato V, sezione V.2, punto 2"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": 0.70,
    },
    {
        "nodo_da": ("principio", None, "allegato V, sezione V.1, punto 16"),
        "nodo_a": ("obbligo", None, "allegato V, sezione V.2, punto 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": 0.70,
    },
    {
        "nodo_da": ("principio", None, "allegato V, sezione V.1, punto 16"),
        "nodo_a": ("obbligo", None, "allegato V, sezione V.2, punto 4"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": 0.70,
    },
    {
        "nodo_da": ("principio", None, "allegato V, sezione V.2, punto 1"),
        "nodo_a": ("obbligo", None, "allegato V, sezione V.1, punto 1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
