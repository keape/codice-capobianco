"""Regolamento di esecuzione (UE) 2024/482 della Commissione, del 31 gennaio
2024 - modalita' di applicazione del regolamento (UE) 2019/881 per quanto
riguarda l'adozione del sistema europeo di certificazione della cibersicurezza
basato sui criteri comuni (EUCC). Fonte 29 (`reg_ue_2024_482`), capitolo 6 di
14 (vedi app/.source_cache/reg_ue_2024_482/manifest.json): Capo VI - Gestione
e divulgazione delle vulnerabilita' (articoli 32-39), con le due sezioni
interne "SEZIONE I - Gestione delle vulnerabilita'" (artt. 33-36, precedute
dall'art. 32 fuori sezione) e "SEZIONE II - Divulgazione delle vulnerabilita'"
(artt. 37-39). Gli artt. 1-31, 40-50 e gli allegati I-IX sono nei capitoli 1-5
e 7-14, assegnati ad altri moduli: nessuno di quei file e' toccato qui. La
porzione assegnata inizia con l'intestazione del Capo VI e si chiude con
l'art. 39: l'art. 40 apre il Capo VII ed e' nel cap07, quindi questa porzione
non contiene nessuna formula di chiusura dell'atto.

Provenienza del testo: app/.source_cache/reg_ue_2024_482/cap06.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R0482, lingua italiana; URL
risolto .../cellar/687c0d05-c580-11ee-95d9-01aa75ed71a1.0014.03/DOC_1, XHTML
della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 540.435 byte
scaricati, 135.367 caratteri di testo, sha256 del raw.txt
b46d08cab6d63b2c190ae767042c07c1fc324955c22ef491eb314556b28ca5b8 - dettagli
completi in provenance.json). Il preambolo (considerando) e' a monte del Capo I
e non e' in questa porzione. Verifica fatta prima di scrivere: le righe
1060-1161 del raw.txt (dall'intestazione "CAPO VI" alla riga dell'art. 39,
inclusa, prima di "CAPO VII") sono identiche byte per byte a cap06.txt, quindi
la porzione non ha perso pezzi in fase di split.

Modellazione (ADR-0007, nessun discrimine di rilevanza):
- Paratesto -> nessun nodo: i marcatori di struttura "CAPO VI" / "GESTIONE E
  DIVULGAZIONE DELLE VULNERABILITA'" (con l'accento in "VULNERABILITÀ", come
  nel testo ufficiale), "SEZIONE I" / "Gestione delle vulnerabilita'" e
  "SEZIONE II" / "Divulgazione delle vulnerabilita'" e le intestazioni degli
  otto articoli ("Articolo N" + rubrica) non sono articoli, commi o lettere.
  Le rubriche restano coperte perche' incluse nel `testo_integrale` della
  prima riga di ogni articolo (convenzione dei moduli gia' censiti, es. art. 3
  del Reg. 2024/2979, art. 25 del cap05 di questa Fonte); il titolo di capitolo
  e quello delle sezioni non sono item di indice. Nota a pie' di pagina (5)
  (direttiva (UE) 2022/2555, NIS 2, richiamata nell'art. 39) -> nessun nodo:
  e' un riferimento bibliografico all'atto citato, non una disposizione di
  questo regolamento; il segnaposto "(5)" resta nel `testo_integrale` verbatim
  dell'art. 39, dove il testo ufficiale lo colloca (stesso criterio del cap02
  di questa Fonte e del cap02 del Reg. 2024/2979). Non compaiono in questa
  porzione epigrafe, firma, formula di chiusura, riga ELI ("ELI: http://data.
  europa.eu/eli/reg_impl/2024/482/oj") ne' ISSN (sono in coda al cap08),
  quindi non producono nodi ne' item di indice. Il capitolo e' contiguo:
  nessuna disposizione di questa porzione e' stata saltata.
- Unita' di copertura: un articolo o un comma = una riga. Gli articoli 32, 36 e
  39 non hanno commi numerati ("art. 32", "art. 36", "art. 39"): un solo item
  di indice e una sola riga ciascuno, col testo integrale di tutti i periodi
  del comma unico dentro il `testo_integrale`. Le lettere dell'art. 35 §2 sono
  item di indice distinti ("art. 35 §2(a)" ... "art. 35 §2(d)") mappati tutti
  alla riga del loro comma, col testo verbatim delle lettere dentro il
  `testo_integrale` di quella riga (stessa convenzione di "art. 25 §1(a)"
  ... "art. 25 §1(d)" del cap05). Il chapeau dell'art. 35 §2 ("La relazione
  sull'analisi dell'impatto delle vulnerabilita' contiene una valutazione degli
  elementi seguenti:") non ha un item proprio oltre a "art. 35 §2", perche' e'
  parte del precetto unico di cui le lettere sono specificazione: tutte e
  quattro sono sintagmi nominali senza verbo proprio, retti dal chapeau, con lo
  stesso soggetto implicito (il titolare che redige la relazione). Nessuna
  riga accorpa piu' commi: ogni comma di questo capitolo ha la propria riga.
- Obbligo vs Principio. Sono Obblighi i commi che prescrivono un comportamento
  a un soggetto identificabile, anche quando la forma e' passiva ma il
  destinatario del precetto e' ricavabile dal testo (precedente: art. 17 §4 del
  cap03 di questa Fonte, "Un profilo di protezione e' certificato unicamente:
  ..."). I titolari del certificato EUCC formano l'oggetto di quasi tutte le
  righe di questo capo; l'obbligo del titolare di gestire e divulgare le
  vulnerabilita' del proprio prodotto certificato e' esattamente cio' che
  l'art. 29 §1(b) del cap05 individua come "quanto stabilito ... dal capo VI
  del presente regolamento". Sono Principi le tre disposizioni che non impongono
  alcun comportamento:
  * art. 32 ("Il presente capo si applica ai prodotti TIC per i quali e' stato
    rilasciato un certificato EUCC") -> Principio "scopo/ambito di
    applicazione": clausola che delimita l'ambito del capo, non un precetto
    (stesso trattamento dell'art. 28 §7 del cap05);
  * art. 35 §5 ("si applica l'articolo 36") -> Principio "scopo/ambito di
    applicazione": regola di applicabilita' condizionata dell'art. 36, che non
    impone a nessuno di fare qualcosa (l'obbligo sta nell'art. 36, censito come
    Obbligo proprio); la lettura alternativa ("altro", come le facolta' del
    cap05) e' dichiarata fra i dubbi aperti in chiusura, ed e' per questo che
    la relazione art. 35 §5 -> art. 36 e' "richiama" e non "specifica";
  * art. 38 §2 ("Altre autorita' ... possono decidere di analizzare
    ulteriormente la vulnerabilita' o ... chiedere agli organismi di
    certificazione competenti di valutare ...") -> Principio "altro": mera
    facolta' discrezionale delle autorita' nazionali (stesso trattamento
    dell'art. 25 §7, dell'art. 26 §3 e dell'art. 28 §4 del cap05).
  E' invece Obbligo il comma misto art. 34 §1: la prima frase ("L'analisi
  dell'impatto delle vulnerabilita' si riferisce all'oggetto della valutazione
  e alle dichiarazioni di affidabilita' contenute nel certificato") e'
  descrittiva, ma la seconda ("L'analisi ... e' effettuata in un intervallo di
  tempo adeguato in relazione alla sfruttabilita' e alla criticita' della
  potenziale vulnerabilita'") prescrive come e quando l'analisi va effettuata;
  prevale la parte prescrittiva, con lo stesso criterio applicato dal cap05
  all'art. 30 §6 (facolta' + limite imperativo). L'alternativa (Principio
  "definitorio" per la prima frase) e' dichiarata fra i dubbi aperti.
- `tipo_obbligo` riga per riga. "tecnico/sicurezza" per i commi il cui
  contenuto e' l'analisi o il monitoraggio di sicurezza (art. 33 §3, che
  registra la vulnerabilita' e ne effettua l'analisi dell'impatto; art. 34 §1 e
  §2, che disciplinano l'analisi dell'impatto e il calcolo del potenziale di
  attacco; art. 35 §3, che protegge la riservatezza dei dettagli di
  sfruttamento; art. 35 §7, che monitora le vulnerabilita' residue): stessa
  lettura del cap05 per l'art. 27 §1 (monitoraggio delle vulnerabilita' del
  prodotto certificato). "informativo/trasparenza" per i commi il cui contenuto
  e' comunicare, pubblicare o delimitare cio' che si comunica (art. 33 §2, che
  pubblica i metodi di ricezione delle segnalazioni; art. 33 §4, che informa i
  titolari dei certificati dipendenti; art. 33 §5, che trasmette le
  informazioni all'organismo di certificazione; art. 35 §4, che trasmette la
  relazione; art. 37 §1 e §2, che determinano il contenuto delle informazioni
  condivise con l'autorita' nazionale; art. 38 §1, che condivide le
  informazioni con le altre autorita' e con l'ENISA; art. 39, che divulga e
  registra la vulnerabilita' nella banca dati europea). "procedurale" per i
  commi che sono passi interni della procedura di gestione delle
  vulnerabilita' (art. 35 §1, che elabora la relazione; art. 35 §2, che ne
  fissa il contenuto; art. 36, che trasmette la proposta di misura correttiva e
  fa riesaminare il certificato).
  "sanzionatorio" per l'art. 35 §6, che stabilisce la conseguenza della
  vulnerabilita' non risolvibile (revoca del certificato in conformita'
  dell'articolo 14): stessa scelta, e stesso dubbio aperto, dichiarati dal cap05
  per art. 28 §6, art. 29 §2 e art. 29 §3. "organizzativo" per l'art. 33 §1
  (il titolare istituisce e mantiene in essere le procedure di gestione delle
  vulnerabilita' e, se necessario, le integra con la norma EN ISO/IEC 30111):
  e' l'assetto organizzativo/documentale del titolare, non un passo della
  procedura ne' un controllo tecnico, e l'unica riga del capo in cui il
  precetto non ha a oggetto una singola vulnerabilita' ma l'apparato con cui
  gestirle. Non tutte le righe classificano una materia identica allo stesso
  modo: l'art. 37 §2 (le informazioni condivise non contengono dettagli sulle
  modalita' di sfruttamento) e' "informativo/trasparenza" e non
  "tecnico/sicurezza", perche' non impone misure di sicurezza sui dati ma
  delimita il contenuto di cio' che si comunica (ed e' stato tenuto distinto
  anche da "procedurale": non disciplina un passo della procedura, ma cosa le
  informazioni possono contenere), mentre l'art. 35 §3, che impone di trattare
  le informazioni con misure di sicurezza adeguate, e' "tecnico/sicurezza";
  l'art. 33 §2, che pubblica i metodi per ricevere le segnalazioni, e'
  "informativo/trasparenza" (la pubblicazione e' il fulcro del precetto), pur
  avendo anche una componente organizzativa ("mantiene in essere").
- Soggetti. Questo capo non riguarda i QTSP: la categoria "QTSP/gestore" non
  compare in nessuna riga. Le categorie censite sono state applicate cosi'
  (convenzione del cap05 di questa Fonte):
  * "Utente/titolare" (ruolo "obbligato") per il titolare di un certificato
    EUCC, che e' il soggetto di tutti gli obblighi degli artt. 33, 34, 35 e 39
    (il cap05 usa la stessa categoria per lo stesso soggetto: "il
    cliente/titolare del servizio (es. titolare di un certificato o di una
    firma)" e' la definizione di CONTEXT.md);
  * "Terza parte" (ruolo "obbligato") per l'organismo di certificazione (artt.
    36, 37) e per l'autorita' nazionale di certificazione della cibersicurezza
    e l'ENISA (artt. 37, 38), e come "destinatario" dove il comma impone a un
    titolare di trasmettere informazioni a uno di questi soggetti (art. 33 §5
    verso l'organismo di certificazione, art. 35 §4 verso l'organismo di
    certificazione o l'autorita' nazionale);
  * "Terzi affidanti/pubblico" (ruolo "destinatario") solo nell'art. 39, dove
    la vulnerabilità va divulgata nella banca dati europea delle vulnerabilita'
    o in altri archivi online pubblici: e' la stessa scelta del cap05 per
    l'art. 30 §3 (informazioni "rese pubbliche ... dal titolare del
    certificato"). Non e' stata usata per l'art. 33 §2: la pubblicazione dei
    metodi di ricezione delle segnalazioni e' volta a fonti esterne
    (ricercatori, utenti, organismi) che non fanno affidamento sul certificato,
    quindi il destinatario non ricade in una categoria censita.
  Il ruolo "destinatario" non e' stato valorizzato dove il destinatario e' della
  stessa categoria del soggetto obbligato (art. 33 §4, che informa altri
  titolari di certificati EUCC; art. 37 §2, art. 38 §1): la riga direbbe due
  volte la stessa cosa (criterio del cap05).
- Art. 36 ha due soggetti obbligati di categorie diverse nella stessa riga:
  il titolare del certificato EUCC ("trasmette all'organismo di certificazione
  una proposta contenente una misura correttiva adeguata") e l'organismo di
  certificazione ("riesamina il certificato in conformita' dell'articolo 13").
  Il comma non e' numerato e i due precetti concorrono alla stessa fattispecie
  (la risoluzione della vulnerabilita' non residua), quindi non e' stato
  scisso in due righe; il precedente di una riga con piu' obbligati di
  categorie diverse esiste in questo censimento (ETSI TS 119 432 cap06,
  Annex A.10).
- `severita` non e' valorizzata da nessuna riga: questo regolamento non gradua
  la gravita' delle violazioni (stessa scelta di tutti i capitoli di questa
  Fonte). `sanzioni` e' valorizzata solo sull'art. 35 §6, con il tipo di
  conseguenza e il rinvio all'articolo che la disciplina.
- `condizione_applicabilita` valorizzata dove il comma subordina la propria
  applicabilita' a una circostanza enunciata (art. 33 §3, §4, §5; art. 34 §2;
  art. 35 §1, §3, §6; art. 39). Non valorizzata dove il comma rinvia a un altro
  comma ("Le informazioni fornite in conformita' del paragrafo 1" in art. 37
  §2, "le informazioni pertinenti ricevute in conformita' dell'articolo 37" in
  art. 38 §1): quello e' un rinvio tra nodi tracciati, dichiarato come
  relazione, non una condizione su un fatto esterno. L'art. 32 (ambito del
  capo) non e' una condizione di applicabilita' delle singole righe ma la
  clausola di ambito del capo, e resta un nodo autonomo.
- `oggetti_giuridici` non e' valorizzato per nessuno dei tre Principi: gli
  oggetti censiti sono quelli dei servizi fiduciari eIDAS (firme, sigilli,
  marche temporali, attestati, portafogli, ...) e il certificato EUCC di un
  prodotto TIC, pur essendo un oggetto di certificazione, non vi rientra
  (scelta gia' dichiarata dal cap05 per l'art. 28 §7).
- `testo_integrale`: verbatim e integrale, ricucendo le righe spezzate dalla
  conversione XHTML -> testo. In questa porzione ogni comma e' una riga fisica
  del file e ogni lettera dell'art. 35 §2 e' spezzata in tre righe (il
  marcatore "(a)" da solo, una riga vuota, il testo della lettera): il
  marcatore ufficiale e' stato ricucito al testo della lettera ("(a) l'impatto
  della vulnerabilita' sul prodotto TIC certificato;"), mantenendo le parentesi
  come nel testo ufficiale, e i commi sono separati da riga vuota.
  L'intestazione "Articolo N" + rubrica e' premessa alla prima riga di ogni
  articolo (per gli artt. 33-35 e 37-38 la riga "§1"), dove il testo ufficiale
  la precede immediatamente; per gli artt. 32, 36 e 39, privi di commi
  numerati, precede l'unico comma. Nessun marcatore di elisione (vincolo
  `verifica_completezza_testo_integrale`, ADR-0010). `testo` e' invece la
  sintesi compressa (1-3 frasi) di ciascun comma, che nomina anche le
  condizioni e i limiti determinanti (probabile impatto sulla conformita' in
  art. 35 §1; i quattro elementi della valutazione in art. 35 §2; "senza
  indebito ritardo" in art. 35 §4; il rinvio all'art. 36 se la vulnerabilita'
  non e' residua e puo' essere risolta in art. 35 §5; la revoca in art. 35 §6;
  il livello AVA_VAN e il rinvio all'articolo 3 e all'allegato I in art. 34 §2;
  "in caso di revoca di un certificato" in art. 39).
- Unita' di indice: articolo + paragrafo con "§" ("art. 33 §1") e lettera tra
  parentesi ("art. 35 §2(a)"), e solo l'articolo quando il testo non numera i
  commi ("art. 32", "art. 36", "art. 39") - convenzione gia' in uso in questo
  censimento per gli atti UE (Reg. 2024/2979 "art. 5 §1(a)"; cap03 di questa
  Fonte "art. 16"; cap04 "art. 24"). Le rubriche degli articoli e i titoli di
  capitolo e di sezione non sono item di indice.
- RELAZIONI: solo interne a questo capitolo, tutte con `fonte_id_o_None = None`
  su entrambi gli estremi, tutte rinvii letterali verificati sul
  `testo_integrale` della riga citante, quindi `evidence_type = "textual"`;
  `confidence` resta None perche' non esiste uno score reale da riportare
  (ADR-0005: non va inventato). Sono tre: art. 35 §5 -> art. 36 ("si applica
  l'articolo 36"); art. 37 §2 -> art. 37 §1 ("Le informazioni fornite in
  conformita' del paragrafo 1"); art. 38 §1 -> art. 37 §1 ("le informazioni
  pertinenti ricevute in conformita' dell'articolo 37": il rinvio e' a livello
  di articolo e il bersaglio e' il §1, il comma che individua quali
  informazioni l'organismo di certificazione fornisce all'autorita' nazionale,
  mentre il §2 ne delimita il contenuto - stesso trattamento del rinvio "di cui
  all'articolo 6" nel Reg. 2024/2979 e dell'art. 28 §6 -> art. 30 §1 nel cap05).
  Avvertenza per l'audit `verifica_relazioni_textual.py`: la relazione verso
  "art. 37 §1" e' un rinvio letterale a livello di articolo ("dell'articolo
  37"), il gate dello script cerca una traccia del riferimento citato e la
  trova nel numero dell'articolo, non in "paragrafo 1". Non e' stata dichiarata
  alcuna relazione inferita (i legami sostanziali fra la registrazione
  dell'art. 33 §3, l'analisi dell'art. 34 e la relazione dell'art. 35 sarebbero
  un giudizio non verificabile dal testo: stessa scelta del cap05), ne' alcuna
  relazione per la clausola di rinvio di sezione dell'art. 33 §1 ("le procedure
  ... necessarie in conformita' delle norme di cui alla presente sezione"), che
  non indica un nodo puntuale ma l'intera Sezione I.
- Rinvii demandati alla fase 6 (nessuna relazione dichiarata, per istruzione
  del batch: i collegamenti tra capitoli della stessa fonte e verso altre fonti
  li costruisce la sessione principale con ADR-0009). Verso altri capitoli di
  questa fonte, con il capitolo in cui il bersaglio e' censito secondo il
  manifest: articolo 3 (norme tecniche di riferimento) in art. 34 §2 e art. 35
  §5 (cap01); allegato I (documenti sullo stato dell'arte) in art. 34 §2
  (cap09); articolo 13 (riesame del certificato) in art. 36 (cap02); articolo
  14 (revoca del certificato EUCC) in art. 35 §6 (cap02). Verso altre fonti:
  regolamento (UE) 2019/881 e segnatamente l'articolo 56, paragrafo 8 (art. 35
  §4) e l'articolo 55, paragrafo 1, lettera d) (art. 39); direttiva (UE)
  2022/2555, articolo 12, istitutivo della banca dati europea delle
  vulnerabilita' (art. 39, con la nota a pie' di pagina (5) che ne riporta gli
  estremi); norma EN ISO/IEC 30111 (art. 33 §1, standard non censito fra le
  Fonti). La clausola di salvezza dell'art. 37 §2 ("lascia impregiudicati i
  poteri di indagine dell'autorita' nazionale di certificazione della
  cibersicurezza") e' un rinvio implicito ai poteri di cui al regolamento (UE)
  2019/881 e non e' stata trasformata in relazione.

Dubbi di classificazione lasciati aperti (segnalati, non risolti in
autonomia):
- art. 35 §5 -> Principio "scopo/ambito di applicazione" anziche' "altro":
  la clausola non delimita l'ambito di un articolo ma dichiara quale
  procedura si applica quando la vulnerabilita' non e' residua e puo' essere
  risolta. Entrambe le letture restano difendibili; il tipo scelto e' quello
  che il cap05 ha usato per la clausola di rinvio dell'art. 28 §7.
- art. 35 §6 -> Obbligo "sanzionatorio" anziche' "procedurale", e art. 34 §1
  -> "tecnico/sicurezza" anziche' "definitorio"/"procedurale": stesso dubbio
  gia' dichiarato dal cap05 per art. 28 §6 e art. 29 §2-§3 (revoca disposta per
  violazione come sanzione) e la stessa tensione fra comma descrittivo e comma
  prescrittivo. Da riconciliare con i capitoli 2 e 5 di questa Fonte.
- art. 33 §3 -> "tecnico/sicurezza" anziche' "procedurale": il comma comincia
  con la registrazione delle informazioni sulle vulnerabilita' (adempimento
  documentale) e prosegue con l'analisi dell'impatto (attivita' di sicurezza);
  si e' data prevalenza alla seconda, per coerenza con l'art. 27 §1 del cap05.
- art. 34 §1 -> soggetto obbligato "Utente/titolare": il comma non nomina il
  titolare del certificato (forma passiva, "e' effettuata"), che e' ricavato
  dagli artt. 33 §3 e 35 §1, dove l'analisi e' effettuata dal titolare. Stessa
  attribuzione per implicazione praticata dal cap05 per le forme passive.
- art. 38 §2 -> Principio "altro" e non Obbligo: la facolta' delle autorita'
  nazionali ("possono decidere") include una condizione procedurale ("dopo aver
  informato il titolare del certificato EUCC") che, letta come adempimento
  imposto alla autorita' richiedente, potrebbe giustificare un Obbligo
  "informativo/trasparenza"; si e' seguita la lettura del cap05 per le facolta'
  di "puo'" (art. 25 §7, art. 26 §3, art. 28 §4).

Copertura: 25 item di indice, 21 righe (18 Obblighi + 3 Principi), 3 relazioni
interne.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 33 §1",
        "testo": "Il titolare di un certificato EUCC istituisce e mantiene in essere tutte le procedure di gestione delle vulnerabilità necessarie in conformità delle norme di cui alla presente sezione e, se necessario, le integra con le procedure stabilite nella norma EN ISO/IEC 30111.",
        "testo_integrale": "Articolo 33\n\nProcedure di gestione delle vulnerabilità\n\n1. Il titolare di un certificato EUCC istituisce e mantiene in essere tutte le procedure di gestione delle vulnerabilità necessarie in conformità delle norme di cui alla presente sezione e, se necessario, le integra con le procedure stabilite nella norma EN ISO/IEC 30111.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 33 §2",
        "testo": "Il titolare di un certificato EUCC mantiene in essere e pubblica metodi appropriati per ricevere informazioni sulle vulnerabilità relative ai propri prodotti trasmesse da fonti esterne, compresi gli utenti, gli organismi di certificazione e i ricercatori nel settore della sicurezza.",
        "testo_integrale": "2. Il titolare di un certificato EUCC mantiene in essere e pubblica metodi appropriati per ricevere informazioni sulle vulnerabilità relative ai propri prodotti trasmesse da fonti esterne, compresi gli utenti, gli organismi di certificazione e i ricercatori nel settore della sicurezza.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 33 §3",
        "testo": "Se rileva una potenziale vulnerabilità che interessa un suo prodotto TIC certificato o riceve informazioni in merito, il titolare di un certificato EUCC registra tali informazioni ed effettua un'analisi dell'impatto delle vulnerabilità.",
        "testo_integrale": "3. Qualora rilevi una potenziale vulnerabilità che interessa un suo prodotto TIC certificato o riceva informazioni in merito, il titolare di un certificato EUCC registra tali informazioni ed effettua un'analisi dell'impatto delle vulnerabilità.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica qualora il titolare del certificato rilevi una potenziale vulnerabilità che interessa un suo prodotto TIC certificato o riceva informazioni in merito.",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 33 §4",
        "testo": "Se una potenziale vulnerabilità interessa un prodotto composito, il titolare del certificato EUCC ne informa il titolare dei certificati EUCC da esso dipendenti.",
        "testo_integrale": "4. Se una potenziale vulnerabilità interessa un prodotto composito, il titolare del certificato EUCC ne informa il titolare dei certificati EUCC da esso dipendenti.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se una potenziale vulnerabilità interessa un prodotto composito.",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 33 §5",
        "testo": "In risposta a una richiesta ragionevole dell'organismo di certificazione che ha rilasciato il certificato, il titolare di un certificato EUCC trasmette a tale organismo tutte le informazioni pertinenti sulle potenziali vulnerabilità.",
        "testo_integrale": "5. In risposta a una richiesta ragionevole dell'organismo di certificazione che ha rilasciato il certificato, il titolare di un certificato EUCC trasmette a tale organismo tutte le informazioni pertinenti sulle potenziali vulnerabilità.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica in risposta a una richiesta ragionevole dell'organismo di certificazione che ha rilasciato il certificato.",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 34 §1",
        "testo": "L'analisi dell'impatto delle vulnerabilità si riferisce all'oggetto della valutazione e alle dichiarazioni di affidabilità contenute nel certificato ed è effettuata in un intervallo di tempo adeguato in relazione alla sfruttabilità e alla criticità della potenziale vulnerabilità del prodotto TIC certificato.",
        "testo_integrale": "Articolo 34\n\nAnalisi dell'impatto delle vulnerabilità\n\n1. L'analisi dell'impatto delle vulnerabilità si riferisce all'oggetto della valutazione e alle dichiarazioni di affidabilità contenute nel certificato. L'analisi dell'impatto delle vulnerabilità è effettuata in un intervallo di tempo adeguato in relazione alla sfruttabilità e alla criticità della potenziale vulnerabilità del prodotto TIC certificato.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 34 §2",
        "testo": "Se del caso, è effettuato un calcolo del potenziale di attacco in conformità della metodologia pertinente inclusa nelle norme di cui all'articolo 3 e dei documenti sullo stato dell'arte pertinenti di cui all'allegato I, al fine di determinare la sfruttabilità della vulnerabilità, tenendo conto del livello AVA_VAN del certificato EUCC.",
        "testo_integrale": "2. Se del caso, è effettuato un calcolo del potenziale di attacco in conformità della metodologia pertinente inclusa nelle norme di cui all'articolo 3 e dei documenti sullo stato dell'arte pertinenti di cui all'allegato I, al fine di determinare la sfruttabilità della vulnerabilità. Si tiene conto del livello AVA_VAN del certificato EUCC.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se del caso, quando occorre determinare la sfruttabilità della vulnerabilità del prodotto TIC certificato.",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 35 §1",
        "testo": "Se dall'analisi dell'impatto emerge un probabile impatto della vulnerabilità sulla conformità del prodotto TIC al relativo certificato, il titolare elabora una relazione sull'analisi dell'impatto delle vulnerabilità.",
        "testo_integrale": "Articolo 35\n\nRelazione sull'analisi dell'impatto delle vulnerabilità\n\n1. Se dall'analisi dell'impatto emerge un probabile impatto della vulnerabilità sulla conformità del prodotto TIC al relativo certificato, il titolare elabora una relazione sull'analisi dell'impatto delle vulnerabilità.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se dall'analisi dell'impatto emerge un probabile impatto della vulnerabilità sulla conformità del prodotto TIC al relativo certificato.",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 35 §2",
        "testo": "La relazione sull'analisi dell'impatto delle vulnerabilità contiene una valutazione dell'impatto della vulnerabilità sul prodotto TIC certificato, dei possibili rischi associati alla prossimità o alla disponibilità di un attacco, della possibilità di risolvere la vulnerabilità e, laddove la vulnerabilità possa essere risolta, delle possibili modalità di risoluzione.",
        "testo_integrale": "2. La relazione sull'analisi dell'impatto delle vulnerabilità contiene una valutazione degli elementi seguenti:\n\n(a) l'impatto della vulnerabilità sul prodotto TIC certificato;\n\n(b) i possibili rischi associati alla prossimità o alla disponibilità di un attacco;\n\n(c) la possibilità di risolvere la vulnerabilità;\n\n(d) laddove la vulnerabilità possa essere risolta, le possibili modalità di risoluzione.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 35 §3",
        "testo": "La relazione sull'analisi dell'impatto delle vulnerabilità contiene, se del caso, dettagli sulle possibili modalità di sfruttamento della vulnerabilità; tali informazioni sono trattate conformemente a misure di sicurezza adeguate per proteggerne la riservatezza e garantirne, se necessario, una diffusione limitata.",
        "testo_integrale": "3. La relazione sull'analisi dell'impatto delle vulnerabilità contiene, se del caso, dettagli sulle possibili modalità di sfruttamento della vulnerabilità. Le informazioni relative alle possibili modalità di sfruttamento della vulnerabilità sono trattate conformemente a misure di sicurezza adeguate per proteggerne la riservatezza e garantirne, se necessario, una diffusione limitata.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "L'inclusione dei dettagli sulle possibili modalità di sfruttamento della vulnerabilità si applica se del caso; le relative informazioni sono in ogni caso trattate con misure di sicurezza adeguate a proteggerne la riservatezza e a garantirne, se necessario, una diffusione limitata.",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 35 §4",
        "testo": "In conformità dell'articolo 56, paragrafo 8, del regolamento (UE) 2019/881, il titolare di un certificato EUCC trasmette senza indebito ritardo una relazione sull'analisi dell'impatto delle vulnerabilità all'organismo di certificazione o all'autorità nazionale di certificazione della cibersicurezza.",
        "testo_integrale": "4. In conformità dell'articolo 56, paragrafo 8, del regolamento (UE) 2019/881, il titolare di un certificato EUCC trasmette senza indebito ritardo una relazione sull'analisi dell'impatto delle vulnerabilità all'organismo di certificazione o all'autorità nazionale di certificazione della cibersicurezza.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 35 §6",
        "testo": "Se dalla relazione sull'analisi dell'impatto delle vulnerabilità emerge che la vulnerabilità non è residua e che non può essere risolta, il certificato EUCC è revocato in conformità dell'articolo 14.",
        "testo_integrale": "6. Se dalla relazione sull'analisi dell'impatto delle vulnerabilità emerge che la vulnerabilità non è residua e che non può essere risolta, il certificato EUCC è revocato in conformità dell'articolo 14.",
        "tipo_obbligo": "sanzionatorio",
        "stato": "vigente",
        "sanzioni": "Revoca del certificato EUCC in conformità dell'articolo 14, se dalla relazione sull'analisi dell'impatto delle vulnerabilità emerge che la vulnerabilità non è residua e che non può essere risolta.",
        "condizione_applicabilita": "Si applica se dalla relazione sull'analisi dell'impatto delle vulnerabilità emerge che la vulnerabilità non è residua e che non può essere risolta.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 35 §7",
        "testo": "Il titolare del certificato EUCC monitora le eventuali vulnerabilità residue per garantire che non possano essere sfruttate in caso di modifiche dell'ambiente operativo.",
        "testo_integrale": "7. Il titolare del certificato EUCC monitora le eventuali vulnerabilità residue per garantire che non possano essere sfruttate in caso di modifiche dell'ambiente operativo.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 36",
        "testo": "Il titolare di un certificato EUCC trasmette all'organismo di certificazione una proposta contenente una misura correttiva adeguata; l'organismo di certificazione riesamina il certificato in conformità dell'articolo 13 e l'ambito di applicazione del riesame è determinato in base alla proposta di risoluzione della vulnerabilità.",
        "testo_integrale": "Articolo 36\n\nRisoluzione delle vulnerabilità\n\nIl titolare di un certificato EUCC trasmette all'organismo di certificazione una proposta contenente una misura correttiva adeguata. L'organismo di certificazione riesamina il certificato in conformità dell'articolo 13. L'ambito di applicazione del riesame è determinato in base alla proposta di risoluzione della vulnerabilità.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 37 §1",
        "testo": "Le informazioni fornite dall'organismo di certificazione all'autorità nazionale di certificazione della cibersicurezza includono tutti gli elementi necessari a quest'ultima per comprendere l'impatto della vulnerabilità, le modifiche da apportare al prodotto TIC e, se disponibili, le eventuali informazioni dell'organismo di certificazione sulle implicazioni più ampie della vulnerabilità per altri prodotti TIC certificati.",
        "testo_integrale": "Articolo 37\n\nInformazioni condivise con l'autorità nazionale di certificazione della cibersicurezza\n\n1. Le informazioni fornite dall'organismo di certificazione all'autorità nazionale di certificazione della cibersicurezza includono tutti gli elementi necessari a quest'ultima per comprendere l'impatto della vulnerabilità, le modifiche da apportare al prodotto TIC e, se disponibili, le eventuali informazioni da parte dell'organismo di certificazione sulle implicazioni più ampie della vulnerabilità per altri prodotti TIC certificati.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 37 §2",
        "testo": "Le informazioni fornite in conformità del paragrafo 1 non contengono dettagli sulle modalità di sfruttamento della vulnerabilità; la disposizione lascia impregiudicati i poteri di indagine dell'autorità nazionale di certificazione della cibersicurezza.",
        "testo_integrale": "2. Le informazioni fornite in conformità del paragrafo 1 non contengono dettagli sulle modalità di sfruttamento della vulnerabilità. La presente disposizione lascia impregiudicati i poteri di indagine dell'autorità nazionale di certificazione della cibersicurezza.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 38 §1",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza condivide le informazioni pertinenti ricevute in conformità dell'articolo 37 con le altre autorità nazionali di certificazione della cibersicurezza e con l'ENISA.",
        "testo_integrale": "Articolo 38\n\nCooperazione con altre autorità nazionali di certificazione della cibersicurezza\n\n1. L'autorità nazionale di certificazione della cibersicurezza condivide le informazioni pertinenti ricevute in conformità dell'articolo 37 con le altre autorità nazionali di certificazione della cibersicurezza e con l'ENISA.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 39",
        "testo": "In caso di revoca di un certificato, il titolare del certificato EUCC divulga e registra qualsiasi vulnerabilità del prodotto TIC pubblicamente nota e risolta nella banca dati europea delle vulnerabilità, istituita in conformità dell'articolo 12 della direttiva (UE) 2022/2555, o in altri archivi online di cui all'articolo 55, paragrafo 1, lettera d), del regolamento (UE) 2019/881.",
        "testo_integrale": "Articolo 39\n\nPubblicazione della vulnerabilità\n\nIn caso di revoca di un certificato, il titolare del certificato EUCC divulga e registra qualsiasi vulnerabilità del prodotto TIC pubblicamente nota e risolta nella banca dati europea delle vulnerabilità, istituita in conformità dell'articolo 12 della direttiva (UE) 2022/2555 del Parlamento europeo e del Consiglio (5), o in altri archivi online di cui all'articolo 55, paragrafo 1, lettera d), del regolamento (UE) 2019/881.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica in caso di revoca di un certificato.",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 32",
        "testo": "Il capo VI si applica ai prodotti TIC per i quali è stato rilasciato un certificato EUCC: è una clausola di delimitazione dell'ambito del capo, non un comportamento imposto ad alcun soggetto.",
        "testo_integrale": "Articolo 32\n\nAmbito della gestione delle vulnerabilità\n\nIl presente capo si applica ai prodotti TIC per i quali è stato rilasciato un certificato EUCC.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 35 §5",
        "testo": "Se dalla relazione sull'analisi dell'impatto delle vulnerabilità emerge che la vulnerabilità non è residua ai sensi delle norme di cui all'articolo 3 e che può essere risolta, si applica l'articolo 36: è una regola di applicabilità condizionata, che non impone di per sé alcun comportamento.",
        "testo_integrale": "5. Se dalla relazione sull'analisi dell'impatto delle vulnerabilità emerge che la vulnerabilità non è residua ai sensi delle norme di cui all'articolo 3 e che può essere risolta, si applica l'articolo 36.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 38 §2",
        "testo": "Altre autorità nazionali di certificazione della cibersicurezza possono decidere di analizzare ulteriormente la vulnerabilità o, dopo aver informato il titolare del certificato EUCC, chiedere agli organismi di certificazione competenti di valutare se la vulnerabilità possa interessare altri prodotti TIC certificati: è una facoltà discrezionale, non un comportamento imposto.",
        "testo_integrale": "2. Altre autorità nazionali di certificazione della cibersicurezza possono decidere di analizzare ulteriormente la vulnerabilità o, dopo aver informato il titolare del certificato EUCC, chiedere agli organismi di certificazione competenti di valutare se la vulnerabilità possa interessare altri prodotti TIC certificati.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 32",
    "art. 33 §1",
    "art. 33 §2",
    "art. 33 §3",
    "art. 33 §4",
    "art. 33 §5",
    "art. 34 §1",
    "art. 34 §2",
    "art. 35 §1",
    "art. 35 §2",
    "art. 35 §2(a)",
    "art. 35 §2(b)",
    "art. 35 §2(c)",
    "art. 35 §2(d)",
    "art. 35 §3",
    "art. 35 §4",
    "art. 35 §5",
    "art. 35 §6",
    "art. 35 §7",
    "art. 36",
    "art. 37 §1",
    "art. 37 §2",
    "art. 38 §1",
    "art. 38 §2",
    "art. 39",
]

# Gli articoli 32, 36 e 39 non hanno commi numerati (un solo item di indice
# ciascuno); l'art. 35 §2 copre il proprio comma per intero, lettere comprese
# (vedi la docstring: un comma = una riga), per questo le lettere sono mappate
# al riferimento del comma e non a un item proprio.
MAPPATURA_LOCALE = {
    "art. 32": ["art. 32"],
    "art. 33 §1": ["art. 33 §1"],
    "art. 33 §2": ["art. 33 §2"],
    "art. 33 §3": ["art. 33 §3"],
    "art. 33 §4": ["art. 33 §4"],
    "art. 33 §5": ["art. 33 §5"],
    "art. 34 §1": ["art. 34 §1"],
    "art. 34 §2": ["art. 34 §2"],
    "art. 35 §1": ["art. 35 §1"],
    "art. 35 §2": ["art. 35 §2", "art. 35 §2(a)", "art. 35 §2(b)", "art. 35 §2(c)", "art. 35 §2(d)"],
    "art. 35 §3": ["art. 35 §3"],
    "art. 35 §4": ["art. 35 §4"],
    "art. 35 §5": ["art. 35 §5"],
    "art. 35 §6": ["art. 35 §6"],
    "art. 35 §7": ["art. 35 §7"],
    "art. 36": ["art. 36"],
    "art. 37 §1": ["art. 37 §1"],
    "art. 37 §2": ["art. 37 §2"],
    "art. 38 §1": ["art. 38 §1"],
    "art. 38 §2": ["art. 38 §2"],
    "art. 39": ["art. 39"],
}

# Relazioni interne a questa Fonte (fonte_id_o_None = None su entrambi gli
# estremi), tutte rinvii letterali verificati sul `testo_integrale` della riga
# citante: art. 35 §5 cita "si applica l'articolo 36"; art. 37 §2 cita "Le
# informazioni fornite in conformità del paragrafo 1"; art. 38 §1 cita "le
# informazioni pertinenti ricevute in conformità dell'articolo 37" (bersaglio
# il §1, il comma che individua quali informazioni fornisce l'organismo di
# certificazione). I rinvii ad altri capitoli di questa fonte (artt. 3, 13, 14,
# allegato I) e ad altre fonti (regolamento (UE) 2019/881, direttiva (UE)
# 2022/2555, norma EN ISO/IEC 30111) non sono dichiarati qui: sono collegamenti
# demandati alla sessione principale (fase ADR-0009), elencati nella docstring.
# `confidence` = None: nessuno score reale da riportare.
RELAZIONI = [
    {
        "nodo_da": ("principio", None, "art. 35 §5"),
        "nodo_a": ("obbligo", None, "art. 36"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 37 §2"),
        "nodo_a": ("obbligo", None, "art. 37 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 38 §1"),
        "nodo_a": ("obbligo", None, "art. 37 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
