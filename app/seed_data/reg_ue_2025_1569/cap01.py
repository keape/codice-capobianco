"""Regolamento di esecuzione (UE) 2025/1569 della Commissione - norme di
riferimento, specifiche e procedure per gli attestati elettronici qualificati
di attributi (QEAA) e per gli attestati elettronici di attributi rilasciati da
un organismo del settore pubblico responsabile di una fonte autentica o per
suo conto (artt. 45 quater-45 septies eIDAS2, regolamento (UE) n. 910/2014
come modificato dal regolamento (UE) 2024/1183). Fonte `reg_ue_2025_1569`,
capitolo 1 di 3 (vedi app/.source_cache/reg_ue_2025_1569/manifest.json):
Articoli 1-5 (oggetto e ambito di applicazione, definizioni, rilascio,
revoca, notifica degli organismi del settore pubblico). Gli allegati I-III
sono nel capitolo 3; gli articoli 6-11 (elenco degli organismi, cataloghi,
verifica rispetto a fonti autentiche, interoperabilita', entrata in vigore e
applicazione) nel capitolo 2. Testo ufficiale (italiano) in
app/.source_cache/reg_ue_2025_1569/cap01.txt, acquisito con
app/tools/cellar_fetch.py (provenienza in provenance.json).

Modellazione (ADR-0007, nessun discrimine di rilevanza):
- Il preambolo (considerando) non e' nella porzione assegnata e comunque non
  produce nodi, come in tutte le Fonti gia' censite.
- Art. 1 (oggetto e ambito: norme di riferimento, specifiche e procedure
  relative a QEAA, attributi da organismo del settore pubblico, elenco dei
  fornitori, cataloghi, verifica rispetto a fonti autentiche) -> un solo
  Principio, tipo "scopo/ambito di applicazione". L'articolo non ha commi: il
  chapeau e i 5 punti numerati che ne precisano l'oggetto sono una sola
  disposizione di cornice, senza autonomia prescrittiva per singolo punto
  (stesso criterio con cui l'elenco a lettere dell'art. 1 §2 del Reg.
  2015/1502 e' coperto da un'unica riga).
- Art. 2 (definizioni: 13 voci) -> un solo nodo, tipo "definitorio", con
  tutte le voci nel `testo_integrale` verbatim: stesso trattamento dell'art. 3
  eIDAS in seed.py (un elenco definitorio non ha autonomia prescrittiva voce
  per voce). Le 13 voci sono indicizzate separatamente e mappate tutte a
  questa riga, come da istruzione del task.
- Art. 3 §1 (rispettare le norme di riferimento e le specifiche dell'allegato
  I; garantire la conformita' degli attestati alle specifiche tecniche
  dell'allegato II) -> Obbligo, "tecnico/sicurezza": due requisiti nello
  stesso comma, un solo nodo (l'unita' di copertura e' il comma).
- Art. 3 §2 -> un solo Obbligo per l'intero comma. Il comma contiene due
  frasi: la prima impone ai fornitori di conformarsi ai requisiti del regime
  per gli attestati di attributi corrispondente; la seconda dichiara che le
  politiche e le procedure degli emittenti rientrano nella valutazione della
  conformita' di cui al regolamento (UE) 910/2014. Poiche' ADR-0007 impone
  un nodo per comma (e un comma coperto da due righe e' un errore), il nodo
  e' un Obbligo - la frase prescrittiva con soggetto obbligato esplicito e'
  la prima - e la seconda frase resta integralmente nel `testo_integrale` e
  e' richiamata nella parafrasi di `testo`. `condizione_applicabilita`
  valorizzata: l'obbligo vale solo per gli attestati inclusi in regimi
  registrati nel catalogo di regimi.
- Art. 4 §1 (politiche scritte e accessibili al pubblico su validita' e
  revoca) -> Obbligo, "organizzativo" (documenti di policy del fornitore),
  con destinatario "Terzi affidanti/pubblico" perche' le politiche sono
  espressamente destinate al pubblico.
- Art. 4 §2 (i fornitori sono gli unici soggetti in grado di revocare gli
  attestati che hanno rilasciato) -> Principio, tipo "altro": dichiara una
  posizione giuridica di esclusivita' (nessun comportamento e' comandato al
  fornitore, ne' e' individuato un obbligato distinto), quindi non rientra
  nella definizione di Obbligo di CONTEXT.md.
- Art. 4 §3 -> un solo Obbligo per l'intero comma: il chapeau impone di
  revocare, le lettere a)-c) enumerano le circostanze minime in cui la revoca
  va disposta, non prescrizioni autonome distinte. `condizione_applicabilita`
  valorizzata (attestati rilasciati con periodo di validita' superiore alle 24
  ore); le lettere sono indicizzate separatamente ma mappate a questa unica
  riga. Destinatario "Utente/titolare": la lettera a) individua la persona cui
  l'attestato e' stato rilasciato (o il soggetto cui si riferisce) come
  soggetto legittimato a chiedere la revoca.
- Art. 4 §4 (tecniche di revoca e metodi di gestione che tutelino la vita
  privata e ostacolino correlabilita' e tracciabilita') -> Obbligo,
  "tecnico/sicurezza", destinatario "Utente/titolare" (la tutela della vita
  privata riguarda il titolare dell'attestato).
- Art. 4 §5 (mettere a disposizione delle parti facenti affidamento sulla
  certificazione informazioni su validita'/revoca con modalita' che ne
  garantiscano integrita' e autenticita') -> Obbligo,
  "informativo/trasparenza", destinatario "Terzi affidanti/pubblico".
- Art. 5 §1, §2, §3 -> Obblighi in capo agli Stati membri, soggetto
  obbligato "Terza parte" (soggetto istituzionale con ruolo identificabile),
  tipo "procedurale" (adempimenti di notifica, come gli obblighi di
  notifica alle autorita' gia' censiti, es. REQ-7.9.3-02 in ETSI EN 319 401).
  Il destinatario "Terza parte" e' valorizzato solo nell'art. 5 §1, dove il
  testo nomina la Commissione (fornisce il sistema elettronico sicuro per le
  notifiche); in §2 e §3 il destinatario non e' nominato e non viene
  inferito. L'art. 5 §3 enuncia anche la non obbligatorieta' della traduzione
  dei documenti di supporto in caso di onere irragionevole: e' la stessa
  notifica, quindi stesso comma, stessa riga.
- Art. 5 §4 (se del caso, la Commissione puo' chiedere agli Stati membri
  informazioni supplementari) -> Principio, tipo "altro": facolta' della
  Commissione, nessun obbligo in capo agli Stati membri.
- Nessuna formula di chiusura in questa porzione: l'entrata in vigore e
  l'applicazione (e la formula "obbligatorio in tutti i suoi elementi e
  direttamente applicabile") sono nell'art. 11, capitolo 2.
- Unita' di indice: articolo/comma. I punti numerati degli artt. 1 e 2 e le
  lettere dell'art. 4 §3 sono indicizzati separatamente e mappati alla riga
  che li copre: nessun item e' coperto da due righe e ogni riga prescrittiva
  resta 1:1 con il proprio comma.
- RELAZIONI = [] per assegnazione esplicita: i collegamenti con le altre
  Fonti (eIDAS/eIDAS2, CAD, DPCM, ETSI) li costruisce la sessione principale
  dopo il merge dei capitoli.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 3 §1",
        "testo": "I fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto rispettano l'elenco delle norme di riferimento e delle specifiche di cui all'allegato I e garantiscono che gli attestati elettronici di attributi da essi rilasciati siano conformi alle specifiche tecniche di cui all'allegato II.",
        "testo_integrale": "Articolo 3\n\nRilascio di attestati elettronici qualificati di attributi e di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto\n\n1. I fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto rispettano l'elenco delle norme di riferimento e delle specifiche di cui all'allegato I e garantiscono che gli attestati elettronici di attributi da essi rilasciati siano conformi alle specifiche tecniche di cui all'allegato II.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 3 §2",
        "testo": "Nel caso di rilascio di attestati elettronici di attributi inclusi in regimi registrati nel catalogo di regimi per gli attestati di attributi, i fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto devono conformarsi ai requisiti del regime per gli attestati di attributi corrispondente. Le politiche e le procedure stabilite dagli emittenti di attestati al fine di garantire la conformità ai requisiti dei regimi rientrano nella valutazione della conformità di cui al regolamento (UE) 910/2014.",
        "testo_integrale": "2. Nel caso di rilascio di attestati elettronici di attributi inclusi in regimi registrati nel catalogo di regimi per gli attestati di attributi, i fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto devono conformarsi ai requisiti del regime per gli attestati di attributi corrispondente. Le politiche e le procedure stabilite dagli emittenti di attestati al fine di garantire la conformità ai requisiti dei regimi per gli attestati di attributi rientrano nella valutazione della conformità di cui al regolamento (UE) 910/2014.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Nel caso di rilascio di attestati elettronici di attributi inclusi in regimi registrati nel catalogo di regimi per gli attestati di attributi.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 4 §1",
        "testo": "I fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto dispongono di politiche scritte e accessibili al pubblico relative alla gestione della situazione di validità o revoca; tali politiche comprendono, se del caso, le condizioni in base alle quali gli attestati elettronici di attributi possono essere revocati senza indugio e misure volte a garantire la disponibilità di informazioni relative alla situazione di validità.",
        "testo_integrale": "Articolo 4\n\nRevoca di attestati elettronici qualificati di attributi e di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto\n\n1. I fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto dispongono di politiche scritte e accessibili al pubblico relative alla gestione della situazione di validità o revoca. Tali politiche comprendono, se del caso, le condizioni in base alle quali gli attestati elettronici di attributi possono essere revocati senza indugio e misure volte a garantire la disponibilità di informazioni relative alla situazione di validità.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 4 §3",
        "testo": "I fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto, qualora tali attestati siano rilasciati con un periodo di validità superiore alle 24 ore, li revocano almeno nelle circostanze seguenti: a) su richiesta esplicita della persona cui è stato rilasciato l'attestato elettronico di attributi o, se del caso, del soggetto cui si riferisce l'attestato; b) se il fornitore è a conoscenza del fatto che la sicurezza o l'affidabilità di tali attestati è stata compromessa; c) in altre situazioni come previsto dal diritto dell'Unione o nazionale o come stabilito nelle politiche dei fornitori di cui al paragrafo 1.",
        "testo_integrale": "3. I fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto, qualora tali attestati siano rilasciati con un periodo di validità superiore alle 24 ore, li revocano almeno nelle circostanze seguenti: a) su richiesta esplicita della persona cui è stato rilasciato l'attestato elettronico di attributi o, se del caso, del soggetto cui si riferisce l'attestato; b) se il fornitore è a conoscenza del fatto che la sicurezza o l'affidabilità degli attestati elettronici qualificati di attributi o degli attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto è stata compromessa; c) in altre situazioni come previsto dal diritto dell'Unione o nazionale o come stabilito nelle politiche dei fornitori di cui al paragrafo 1.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Se gli attestati elettronici di attributi sono rilasciati con un periodo di validità superiore alle 24 ore.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 4 §4",
        "testo": "I fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto istituiscono tecniche di revoca e metodi di gestione che tutelino la vita privata e ostacolino la correlabilità e la tracciabilità.",
        "testo_integrale": "4. I fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto istituiscono tecniche di revoca e metodi di gestione che tutelino la vita privata e ostacolino la correlabilità e la tracciabilità.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 4 §5",
        "testo": "I fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto mettono a disposizione delle parti facenti affidamento sulla certificazione informazioni sulla situazione di validità o di revoca degli attestati elettronici di attributi che hanno rilasciato, con una modalità che garantisca l'integrità e l'autenticità di tali informazioni.",
        "testo_integrale": "5. I fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto mettono a disposizione delle parti facenti affidamento sulla certificazione informazioni sulla situazione di validità o di revoca degli attestati elettronici di attributi che hanno rilasciato con una modalità che garantisca l'integrità e l'autenticità di tali informazioni.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 5 §1",
        "testo": "Gli Stati membri trasmettono almeno le informazioni di cui all'allegato III sugli organismi del settore pubblico di cui all'articolo 45 septies, paragrafo 3, del regolamento (UE) n. 910/2014, attraverso un sistema elettronico sicuro per le notifiche fornito dalla Commissione.",
        "testo_integrale": "Articolo 5\n\nNotifica degli organismi del settore pubblico\n\n1. Gli Stati membri trasmettono almeno le informazioni di cui all'allegato III sugli organismi del settore pubblico di cui all'articolo 45 septies, paragrafo 3, del regolamento (UE) n. 910/2014, attraverso un sistema elettronico sicuro per le notifiche fornito dalla Commissione.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 5 §2",
        "testo": "Gli Stati membri notificano qualsiasi modifica delle informazioni notificate.",
        "testo_integrale": "2. Gli Stati membri notificano qualsiasi modifica delle informazioni notificate.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 5 §3",
        "testo": "Gli Stati membri effettuano le notifiche quanto meno in lingua inglese; non sono tenuti a tradurre alcun documento a sostegno delle notifiche qualora ciò comporti un onere amministrativo o finanziario irragionevole.",
        "testo_integrale": "3. Gli Stati membri effettuano le notifiche quanto meno in lingua inglese. Gli Stati membri non sono tenuti a tradurre alcun documento a sostegno delle notifiche qualora ciò comporti un onere amministrativo o finanziario irragionevole.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 1",
        "testo": "Il presente regolamento stabilisce le norme di riferimento, le specifiche e le procedure, da aggiornare periodicamente per tenere conto degli sviluppi tecnologici, della normazione e del lavoro svolto sulla base della raccomandazione (UE) 2021/946 della Commissione, in particolare dell'architettura e del quadro di riferimento, relative a: 1) gli attestati elettronici qualificati di attributi; 2) gli attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto; 3) l'elenco dei fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto; 4) il catalogo di attributi e il catalogo di regimi per gli attestati di attributi di cui ai punti 1) e 2); 5) la verifica degli attributi rispetto a fonti autentiche o intermediari designati.",
        "testo_integrale": "Articolo 1\n\nOggetto e ambito di applicazione\n\nIl presente regolamento stabilisce le norme di riferimento, le specifiche e le procedure, da aggiornare periodicamente per tenere conto degli sviluppi tecnologici, della normazione e del lavoro svolto sulla base della raccomandazione (UE) 2021/946 della Commissione, in particolare dell'architettura e del quadro di riferimento, relative: 1) agli attestati elettronici qualificati di attributi; 2) agli attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto; 3) all'elenco di fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto; 4) al catalogo di attributi e al catalogo di regimi per gli attestati di attributi di cui ai punti 1) e 2); 5) alla verifica degli attributi rispetto a fonti autentiche o intermediari designati.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2",
        "testo": "Ai fini del presente regolamento si applicano le definizioni seguenti: «unità di portafoglio» (configurazione unica di una soluzione di portafoglio che comprende istanze di portafoglio, applicazioni crittografiche sicure e dispositivi crittografici sicuri per il portafoglio, forniti da un fornitore del portafoglio a un singolo utente del portafoglio); «utente del portafoglio» (chi ha il controllo dell'unità di portafoglio); «catalogo di attributi» (archivio digitale di attributi gestito e pubblicato online dalla Commissione); «regime per gli attestati di attributi» (insieme di norme applicabili a uno o più tipi di attestati elettronici di attributi); «tipo di attestati elettronici di attributi» (gruppo di attestati elettronici di attributi cui sono stati assegnati un nome specifico e una descrizione semantica); «catalogo di regimi per gli attestati di attributi» (archivio digitale contenente l'elenco dei regimi per gli attestati di attributi registrato conformemente al presente regolamento e gestito [e pubblicato online] dalla Commissione); «soluzione di portafoglio» (combinazione di software, hardware, servizi, impostazioni e configurazioni, comprese le istanze di portafoglio, una o più applicazioni crittografiche sicure per il portafoglio e uno o più dispositivi crittografici sicuri per il portafoglio); «istanza di portafoglio» (applicazione installata e configurata su un dispositivo o su un ambiente di un utente del portafoglio, che fa parte di un'unità di portafoglio e che l'utente del portafoglio utilizza per interagire con l'unità di portafoglio); «applicazione crittografica sicura per il portafoglio» (applicazione che gestisce risorse critiche tramite un collegamento alle funzioni crittografiche e non crittografiche fornite dal dispositivo crittografico sicuro per il portafoglio e l'uso di tali funzioni); «dispositivo crittografico sicuro per il portafoglio» (dispositivo resistente alle manomissioni che fornisce un ambiente collegato all'applicazione crittografica sicura per il portafoglio e da essa utilizzato per proteggere le risorse critiche e fornire funzioni crittografiche per l'esecuzione sicura di operazioni critiche); «fornitore del portafoglio» (persona fisica o giuridica che fornisce soluzioni di portafoglio); «risorse critiche» (risorse all'interno di un'unità di portafoglio o ad essa relative, di importanza tale che un'eventuale compromissione della loro disponibilità, riservatezza o integrità avrebbe un effetto estremamente grave e debilitante sulla possibilità di fare affidamento sull'unità di portafoglio); «titolare di un regime per gli attestati di attributi» (entità responsabile dell'istituzione e della gestione di un regime per gli attestati di attributi).",
        "testo_integrale": "Articolo 2\n\nDefinizioni\n\nAi fini del presente regolamento si applicano le definizioni seguenti: 1) \"unità di portafoglio\": una configurazione unica di una soluzione di portafoglio che comprende istanze di portafoglio, applicazioni crittografiche sicure per il portafoglio e dispositivi crittografici sicuri per il portafoglio forniti da un fornitore del portafoglio a un singolo utente del portafoglio; 2) \"utente del portafoglio\": un utente che ha il controllo dell'unità di portafoglio; 3) \"catalogo di attributi\": un archivio digitale di attributi gestito e pubblicato online dalla Commissione; 4) \"regime per gli attestati di attributi\": un insieme di norme applicabili a uno o più tipi di attestati elettronici di attributi; 5) \"tipo di attestati elettronici di attributi\": un gruppo di attestati elettronici di attributi cui sono stati assegnati un nome specifico e una descrizione semantica; 6) \"catalogo di regimi per gli attestati di attributi\": un archivio digitale contenente un elenco di regimi per gli attestati di attributi registrato conformemente al presente regolamento e gestito [e pubblicato online] dalla Commissione; 7) \"soluzione di portafoglio\": una combinazione di software, hardware, servizi, impostazioni e configurazioni, comprese le istanze di portafoglio, una o più applicazioni crittografiche sicure per il portafoglio e uno o più dispositivi crittografici sicuri per il portafoglio; 8) \"istanza di portafoglio\": l'applicazione installata e configurata su un dispositivo o su un ambiente di un utente del portafoglio, che fa parte di un'unità di portafoglio, e che l'utente del portafoglio utilizza per interagire con l'unità di portafoglio; 9) \"applicazione crittografica sicura per il portafoglio\": un'applicazione che gestisce risorse critiche tramite un collegamento alle funzioni crittografiche e non crittografiche fornite dal dispositivo crittografico sicuro per il portafoglio e l'uso di tali funzioni; 10) \"dispositivo crittografico sicuro per il portafoglio\": un dispositivo resistente alle manomissioni che fornisce un ambiente collegato all'applicazione crittografica sicura per il portafoglio e da essa utilizzato per proteggere le risorse critiche e fornire funzioni crittografiche per l'esecuzione sicura di operazioni critiche; 11) \"fornitore del portafoglio\": una persona fisica o giuridica che fornisce soluzioni di portafoglio; 12) \"risorse critiche\": risorse all'interno di un'unità di portafoglio o ad essa relative, di importanza tale che un'eventuale compromissione della loro disponibilità, riservatezza o integrità avrebbe un effetto estremamente grave e debilitante sulla possibilità di fare affidamento sull'unità di portafoglio; 13) \"titolare di un regime per gli attestati di attributi\": un'entità responsabile dell'istituzione e della gestione di un regime per gli attestati di attributi.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 4 §2",
        "testo": "Regola di competenza esclusiva: i fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto sono gli unici soggetti in grado di revocare gli attestati elettronici di attributi che hanno rilasciato.",
        "testo_integrale": "2. I fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto sono gli unici soggetti in grado di revocare gli attestati elettronici di attributi che hanno rilasciato.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 5 §4",
        "testo": "Se del caso, la Commissione può chiedere agli Stati membri di fornire informazioni supplementari.",
        "testo_integrale": "4. Se del caso, la Commissione può chiedere agli Stati membri di fornire informazioni supplementari.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Se del caso.",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 1",
    "art. 1, punto 1",
    "art. 1, punto 2",
    "art. 1, punto 3",
    "art. 1, punto 4",
    "art. 1, punto 5",
    "art. 2",
    "art. 2, punto 1",
    "art. 2, punto 2",
    "art. 2, punto 3",
    "art. 2, punto 4",
    "art. 2, punto 5",
    "art. 2, punto 6",
    "art. 2, punto 7",
    "art. 2, punto 8",
    "art. 2, punto 9",
    "art. 2, punto 10",
    "art. 2, punto 11",
    "art. 2, punto 12",
    "art. 2, punto 13",
    "art. 3 §1",
    "art. 3 §2",
    "art. 4 §1",
    "art. 4 §2",
    "art. 4 §3",
    "art. 4 §3(a)",
    "art. 4 §3(b)",
    "art. 4 §3(c)",
    "art. 4 §4",
    "art. 4 §5",
    "art. 5 §1",
    "art. 5 §2",
    "art. 5 §3",
    "art. 5 §4",
]

MAPPATURA_LOCALE = {
    "art. 1": [
        "art. 1",
        "art. 1, punto 1",
        "art. 1, punto 2",
        "art. 1, punto 3",
        "art. 1, punto 4",
        "art. 1, punto 5",
    ],
    "art. 2": [
        "art. 2",
        "art. 2, punto 1",
        "art. 2, punto 2",
        "art. 2, punto 3",
        "art. 2, punto 4",
        "art. 2, punto 5",
        "art. 2, punto 6",
        "art. 2, punto 7",
        "art. 2, punto 8",
        "art. 2, punto 9",
        "art. 2, punto 10",
        "art. 2, punto 11",
        "art. 2, punto 12",
        "art. 2, punto 13",
    ],
    "art. 3 §1": ["art. 3 §1"],
    "art. 3 §2": ["art. 3 §2"],
    "art. 4 §1": ["art. 4 §1"],
    "art. 4 §2": ["art. 4 §2"],
    "art. 4 §3": ["art. 4 §3", "art. 4 §3(a)", "art. 4 §3(b)", "art. 4 §3(c)"],
    "art. 4 §4": ["art. 4 §4"],
    "art. 4 §5": ["art. 4 §5"],
    "art. 5 §1": ["art. 5 §1"],
    "art. 5 §2": ["art. 5 §2"],
    "art. 5 §3": ["art. 5 §3"],
    "art. 5 §4": ["art. 5 §4"],
}

# Relazioni native (citazioni letterali nel testo dell'atto, non differite a
# Fase 6). Le quattro basi giuridiche dichiarate nei "visti" del regolamento
# (art. 45 quinquies §5, art. 45 sexies §2, art. 45 septies §6 e §7 eIDAS2)
# sono portate dall'art. 1, che ne e' la proiezione sull'oggetto dell'atto;
# art. 5 §1 cita testualmente l'art. 45 septies §3 eIDAS2 come fonte delle
# informazioni da notificare.
RELAZIONI = [
    {
        'nodo_da': ('principio', None, 'art. 1'),
        'nodo_a': ('principio', 2, 'art. 45 quinquies §5'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.95,
    },
    {
        'nodo_da': ('principio', None, 'art. 1'),
        'nodo_a': ('principio', 2, 'art. 45 sexies §2'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.95,
    },
    {
        'nodo_da': ('principio', None, 'art. 1'),
        'nodo_a': ('principio', 2, 'art. 45 septies §6'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.95,
    },
    {
        'nodo_da': ('principio', None, 'art. 1'),
        'nodo_a': ('principio', 2, 'art. 45 septies §7'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.95,
    },
    {
        'nodo_da': ('obbligo', None, 'art. 5 §1'),
        'nodo_a': ('principio', 2, 'art. 45 septies §3'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
]
