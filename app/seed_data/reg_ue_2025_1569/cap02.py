"""Regolamento di esecuzione (UE) 2025/1569 della Commissione - attestati
elettronici qualificati di attributi (QEAA) e attestati elettronici di
attributi rilasciati da un organismo del settore pubblico responsabile di una
fonte autentica o per suo conto (artt. 45 quater-45 septies eIDAS2). Capitolo
2 di 3 del manifest: articoli 6-11 (pubblicazione dell'elenco degli organismi
del settore pubblico, creazione e mantenimento del catalogo di attributi,
creazione e mantenimento del catalogo di regimi per gli attestati di
attributi, verifica degli attributi rispetto a fonti autentiche o
intermediari designati, interoperabilita' e riutilizzo, entrata in vigore e
applicazione). Testo ufficiale italiano in
app/.source_cache/reg_ue_2025_1569/cap02.txt (manifest e suddivisione in
porzioni prodotti da app/tools/split_source.py).

Copertura (ADR-0007): 30 nodi (24 obblighi, 6 principi) e 54 item di indice
locale, uno per articolo/comma e - per i commi che ne hanno - uno per ciascuna
lettera. Il preambolo non e' nella porzione e non e' censito; la formula di
chiusura dell'art. 11 ("obbligatorio in tutti i suoi elementi e direttamente
applicabile") e i paragrafi amministrativi finali (firma a Bruxelles,
presidente, note GU) non sono disposizioni normative e non producono nodi.

Scelte di modellazione non ovvie:

- Un comma = un nodo. Le lettere (a), (b), ... sono indicizzate come item
  distinti quando il comma ne ha, ma mappate al nodo del loro comma: in questa
  porzione ogni lettera enumera il contenuto o le modalita' di UNA sola
  prescrizione (le forme di accesso all'elenco ex art. 6 §2, le informazioni da
  pubblicare ex art. 6 §3, il contenuto minimo della richiesta ex art. 7 §5 e
  art. 8 §3) e non contiene una prescrizione autonoma distinta: una riga per
  lettera sarebbe una duplicazione del medesimo obbligo, non un nodo in piu'.
  Un testo_integrale copre percio' il comma intero, lettere comprese, in
  verbatim.
- Soggetti istituzionali. Commissione e Stati membri compiono qui atti a essi
  imposti (redigere, pubblicare, valutare, istituire meccanismi): i nodi
  corrispondenti sono Obblighi con categoria "Terza parte" e ruolo "obbligato"
  (soggetto istituzionale con un ruolo identificabile), non Principi: la
  regola del censimento "chi impone un comportamento a un soggetto -> Obbligo"
  non conosce eccezione per gli attori istituzionali, anche dove il pilota
  eIDAS aveva talvolta trattato obblighi della Commissione/sugli Stati membri
  come righe della tabella principi (scelta superata da ADR-0007).
- Disposizioni meramente facoltative. art. 7 §4 (Stati membri e soggetti
  privati possono chiedere l'inclusione di attributi non figuranti
  nell'allegato VI), art. 7 §7 e art. 8 §5 (la Commissione "puo' inserire"
  l'attributo/il regime o la modifica nel catalogo dopo valutazione e verifica
  di completezza), art. 10 §1 (gli Stati membri "possono fare riferimento" ai
  servizi comuni del sistema tecnico ex regolamento (UE) 2018/1724 e
  riutilizzarli) non impongono alcun comportamento: nessun soggetto obbligato,
  quindi Principio tipo "altro" (stessa scelta gia' fatta nel censimento per
  le facolta' di "puo'" della Commissione/sugli Stati membri).
- art. 8 §3 e' un comma misto (facolta' di chiedere l'aggiunta di un regime al
  catalogo + contenuto minimo obbligatorio della richiesta): prevale la parte
  prescrittiva ("contiene almeno"), quindi Obbligo, con la facolta' richiamata
  nella parafrasi.
- art. 9 §2 e' un comma con tre soggetti distinti (il meccanismo di verifica
  degli Stati membri, il prestatore qualificato che conferisce gli attributi al
  punto di verifica su richiesta dell'utente, l'organismo del settore pubblico
  o l'intermediario designato che condivide i risultati): un solo nodo, con due
  categorie di soggetto obbligato (QTSP/gestore e Terza parte), perche' il
  comma non e' scindibile in item d'indice autonomi.
- art. 9 §5 e' un comma misto (facolta' degli Stati membri di imporre controlli
  di accesso e meccanismi di controllo dell'uso dei metodi di verifica +
  obbligo condizionato di pubblicarne la portata): tipo "informativo/
  trasparenza" e `condizione_applicabilita` valorizzata, perche' l'unica parte
  vincolante e' la pubblicazione, che scatta solo se gli Stati membri
  istituiscono quei meccanismi.
- tipo_obbligo: "informativo/trasparenza" per gli obblighi di pubblicazione e
  accessibilita' di informazioni ed elenchi (art. 6 §1-3, art. 7 §8-9, art. 8
  §6-7, art. 9 §5); "organizzativo" per gli obblighi di creare e mantenere il
  catalogo e il sistema sicuro di presentazione delle richieste, quando la
  pubblicazione e' solo uno degli esiti del comma (art. 7 §1, art. 8 §1,
  art. 10 §2); "procedurale" per gli obblighi di valutazione delle richieste,
  di richiesta di inclusione, di rilascio di identificatori e per le regole di
  contenuto di richieste e risultati di verifica (art. 7 §2-3, §5, §10;
  art. 8 §2-3, §8; art. 9 §1-4); "tecnico/sicurezza" per i requisiti di
  firma/sigillo qualificato o avanzato su certificato qualificato a corredo
  della richiesta (art. 7 §6, art. 8 §4).
- art. 11 produce due nodi distinti, "art. 11, entrata in vigore" e
  "art. 11, applicazione" (i due fatti giuridici hanno effetti diversi: il
  differimento al 19 agosto 2026 riguarda solo gli articoli da 6 a 9), stesso
  criterio gia' usato per gli articoli finali delle altre fonti regolamentari.

RELAZIONI: intenzionalmente vuota. I collegamenti con eIDAS/eIDAS2 e con le
altre fonti (in particolare verso gli artt. 45 quater-45 septies eIDAS2 e
verso gli atti di esecuzione collegati) sono costruiti dalla sessione
principale dopo l'inserimento di tutti i capitoli di questa fonte, non da
questo modulo (nessuna relazione cross-fonte tentata in fase di import
parallelo per capitolo).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 6 §1",
        "testo": "La Commissione redige, mantiene e pubblica un elenco dei fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto; l'elenco si basa sulle informazioni notificate dagli Stati membri a norma dell'articolo 5.",
        "testo_integrale": "1. La Commissione redige, mantiene e pubblica un elenco dei fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto sulla base delle informazioni notificate dagli Stati membri a norma dell'articolo 5.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 6 §2",
        "testo": "La Commissione garantisce che sia possibile accedere all'elenco di cui al §1: a) tanto in forma firmata o sigillata elettronicamente e adatta al trattamento automatizzato, quanto attraverso un sito web leggibile da utenti umani; b) senza la necessita' di registrarsi o di essere autenticati; c) solo utilizzando una sicurezza a livello di trasporto (transport layer security) all'avanguardia.",
        "testo_integrale": "2. La Commissione garantisce che sia possibile accedere all'elenco di cui al paragrafo 1. a) tanto in forma firmata o sigillata elettronicamente adatta al trattamento automatizzato, quanto attraverso un sito web leggibile da utenti umani; b) senza la necessità di registrarsi o di essere autenticati; c) solo utilizzando una sicurezza a livello di trasporto (transport layer security) all'avanguardia.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 6 §3",
        "testo": "La Commissione pubblica senza indebito ritardo, attraverso un canale sicuro: a) le specifiche tecniche dell'elenco; b) i dettagli dell'URL presso il quale l'elenco e' pubblicato; c) i certificati da utilizzare per verificare la firma elettronica o il sigillo elettronico apposti sugli elenchi; d) i dettagli relativi ai meccanismi utilizzati per convalidare le successive modifiche dell'ubicazione o dei certificati di cui alle lettere b) e c).",
        "testo_integrale": "3. La Commissione pubblica senza indebito ritardo, attraverso un canale sicuro: a) le specifiche tecniche dell'elenco; b) i dettagli dell'URL presso il quale è pubblicato l'elenco; c) i certificati da utilizzare per verificare la firma elettronica o il sigillo elettronico apposti sugli elenchi; d) i dettagli relativi ai meccanismi utilizzati per convalidare le successive modifiche dell'ubicazione o dei certificati di cui alle lettere b) e c).",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 §1",
        "testo": "La Commissione redige e pubblica un catalogo di attributi e istituisce un sistema sicuro che consente la presentazione di richieste di inclusione di attributi nel catalogo di attributi o di modifica degli attributi in esso registrati.",
        "testo_integrale": "1. La Commissione redige e pubblica un catalogo di attributi e istituisce un sistema sicuro che consente la presentazione di richieste di inclusione di attributi nel catalogo di attributi o di modifica degli attributi in esso registrati.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 §2",
        "testo": "La Commissione, dopo aver preso in considerazione eventuali pareri forniti dal gruppo di cooperazione, valuta le richieste di inclusione di un attributo nel catalogo di attributi o di modifica di un attributo in esso registrato, presentate utilizzando il sistema di cui al §1; nella sua valutazione considera se l'inclusione dell'attributo contribuisce alla creazione di una base comune per interazioni elettroniche sicure e rispettose della vita privata tra cittadini, imprese e autorita' pubbliche e alla promozione dell'interoperabilita', e tiene conto anche della normativa settoriale, ove applicabile.",
        "testo_integrale": "2. La Commissione, dopo aver preso in considerazione eventuali pareri forniti dal gruppo di cooperazione, valuta le richieste di inclusione di un attributo nel catalogo di attributi o di modifica di un attributo in esso registrato, presentate utilizzando il sistema di cui al paragrafo 1. Nella sua valutazione la Commissione considera se l'inclusione dell'attributo contribuisce alla creazione di una base comune per interazioni elettroniche sicure e rispettose della vita privata tra cittadini, imprese e autorità pubbliche e alla promozione dell'interoperabilità. La Commissione tiene conto anche della normativa settoriale, ove applicabile.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 §3",
        "testo": "Gli Stati membri richiedono l'inclusione nel catalogo di attributi degli attributi figuranti nell'allegato VI del regolamento (UE) n. 910/2014, qualora tali attributi facciano affidamento su fonti autentiche ai fini della verifica da parte di prestatori di servizi fiduciari qualificati.",
        "testo_integrale": "3. Gli Stati membri richiedono l'inclusione di attributi figuranti nell'allegato VI del regolamento (UE) n. 910/2014 nel catalogo di attributi qualora tali attributi facciano affidamento su fonti autentiche ai fini della verifica da parte di prestatori di servizi fiduciari qualificati.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "si applica solo agli attributi figuranti nell'allegato VI del regolamento (UE) n. 910/2014 che fanno affidamento su fonti autentiche ai fini della verifica da parte di prestatori di servizi fiduciari qualificati",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 §5",
        "testo": "La richiesta di includere un attributo nel catalogo o di modificare un attributo in esso registrato contiene almeno: a) l'identificazione del soggetto che presenta la richiesta; b) se del caso, un riferimento alla normativa dell'Unione o nazionale o alla prassi amministrativa in virtu' della quale il richiedente e' considerato fonte primaria di informazioni o fonte autentica riconosciuta; c) l'indicazione se la richiesta riguarda un attributo gia' presente nel catalogo o un nuovo attributo; d) uno spazio dei nomi (namespace) per l'identificatore degli attributi, unico all'interno del catalogo; e) un identificatore dell'attributo, unico all'interno dello spazio dei nomi, e la versione dell'attributo; f) la descrizione semantica dell'attributo; g) il tipo di dati dell'attributo; h) il punto di verifica per l'attributo a livello nazionale o un link a una descrizione della procedura per avviare le richieste di verifica.",
        "testo_integrale": "5. La richiesta di includere un attributo nel catalogo o di modificare un attributo in esso registrato contiene almeno le informazioni seguenti: a) identificazione del soggetto che presenta la richiesta; b) se del caso, un riferimento alla normativa dell'Unione o nazionale o alla prassi amministrativa in virtù della quale il soggetto che effettua la richiesta è considerato essere una fonte primaria di informazioni o una fonte autentica riconosciuta; c) se la richiesta riguarda un attributo già presente nel catalogo o un nuovo attributo; d) uno spazio dei nomi (namespace) per l'identificatore degli attributi, il cui valore è unico all'interno del catalogo di attributi; e) un identificatore dell'attributo, unico all'interno dello spazio dei nomi, e la versione dell'attributo; f) la descrizione semantica dell'attributo; g) il tipo di dati dell'attributo; h) il punto di verifica per l'attributo a livello nazionale o un link a una descrizione della procedura per avviare le richieste di verifica.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 §6",
        "testo": "La richiesta di includere o modificare un attributo e' firmata o sigillata dal richiedente mediante una firma elettronica qualificata o un sigillo elettronico qualificato oppure una firma elettronica avanzata o un sigillo elettronico avanzato basati su un certificato qualificato.",
        "testo_integrale": "6. La richiesta di includere o modificare un attributo è firmata o sigillata dal richiedente mediante una firma elettronica qualificata o un sigillo elettronico qualificato oppure una firma elettronica avanzata o un sigillo elettronico avanzato basati su un certificato qualificato.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 §8",
        "testo": "Il catalogo di attributi, sigillato dalla Commissione, e' accessibile al pubblico, attraverso un canale sicuro, gratuitamente e senza previa identificazione o autenticazione, ed e' pubblicato in versioni leggibili da dispositivi automatici e da utenti umani; il catalogo comprende anche una funzione di ricerca.",
        "testo_integrale": "8. Il catalogo di attributi sigillato dalla Commissione è accessibile al pubblico, attraverso un canale sicuro, gratuitamente e senza previa identificazione o autenticazione, ed è pubblicato in versioni leggibili da dispositivi automatici e da utenti umani. Il catalogo comprende anche una funzione di ricerca.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 §9",
        "testo": "La Commissione pubblica le specifiche tecniche da essa utilizzate per il catalogo di attributi.",
        "testo_integrale": "9. La Commissione pubblica le specifiche tecniche da essa utilizzate per il catalogo di attributi.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 §10",
        "testo": "La Commissione rilascia un identificatore unico per ciascun attributo registrato.",
        "testo_integrale": "10. La Commissione rilascia un identificatore unico per ciascun attributo registrato.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 8 §1",
        "testo": "La Commissione redige e pubblica un catalogo di regimi per gli attestati di attributi e istituisce un sistema sicuro che consente la presentazione di richieste di inclusione di regimi per gli attestati di attributi nel catalogo di regimi per gli attestati di attributi o di modifica dei regimi in esso registrati.",
        "testo_integrale": "1. La Commissione redige e pubblica un catalogo di regimi per gli attestati di attributi e istituisce un sistema sicuro che consente la presentazione di richieste di inclusione di regimi per gli attestati di attributi nel catalogo di regimi per gli attestati di attributi o di modifica dei regimi in esso registrati.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 8 §2",
        "testo": "La Commissione, dopo aver preso in considerazione eventuali pareri forniti dal gruppo di cooperazione, valuta le richieste di inclusione di regimi per gli attestati di attributi nel catalogo di regimi per gli attestati di attributi o di modifica dei regimi in esso registrati; nella sua valutazione considera se il regime contribuisce alla creazione di una base comune per interazioni elettroniche sicure e rispettose della vita privata tra cittadini, imprese e autorita' pubbliche e alla promozione dell'interoperabilita', e tiene conto anche della normativa settoriale, ove applicabile.",
        "testo_integrale": "2. La Commissione, dopo aver preso in considerazione eventuali pareri forniti dal gruppo di cooperazione, valuta le richieste di inclusione di regimi per gli attestati di attributi nel catalogo di regimi per gli attestati di attributi o di modifica dei regimi in esso registrati. Nella sua valutazione la Commissione considera se il regime contribuisce alla creazione di una base comune per interazioni elettroniche sicure e rispettose della vita privata tra cittadini, imprese e autorità pubbliche e alla promozione dell'interoperabilità. La Commissione tiene conto anche della normativa settoriale, ove applicabile.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 8 §3",
        "testo": "I titolari di un regime per gli attestati di attributi possono chiedere di aggiungere regimi al catalogo di regimi; la richiesta di includere un regime nel catalogo o di modificare un regime in esso registrato contiene almeno: a) il nome del regime, scelto dal titolare del regime e unico all'interno del catalogo; b) il nome e le informazioni di contatto del titolare del regime; c) lo stato e la versione del regime; d) un riferimento a eventuali leggi, norme o orientamenti specifici cui siano soggetti il rilascio, la convalida o l'utilizzo di un attestato elettronico di attributi rientrante nell'ambito di applicazione del regime; e) il formato o i formati degli attestati elettronici di attributi rientranti nel regime; f) uno o piu' spazi dei nomi, identificatori degli attributi, descrizioni semantiche e tipi di dati di ciascun attributo facente parte di un attestato elettronico di attributi rientrante nel regime, mediante riferimento a un attributo del catalogo di attributi di cui all'articolo 7 oppure mediante un attributo definito in modo analogo nell'ambito di applicazione del regime; g) una descrizione del modello di fiducia e dei meccanismi di governance applicati nell'ambito del regime, compresi i meccanismi di revoca; h) eventuali requisiti relativi ai fornitori degli attestati elettronici di attributi o alle fonti di informazione su cui tali fornitori fanno affidamento per il rilascio, comprese eventuali fonti autentiche, se del caso; i) una dichiarazione che indichi se gli attestati elettronici di attributi rientranti nel regime devono essere rilasciati come attestati elettronici qualificati di attributi, come attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto, o in entrambe le forme.",
        "testo_integrale": "3. I titolari di un regime per gli attestati di attributi possono chiedere di aggiungere regimi al catalogo di regimi. La richiesta di includere un regime nel catalogo di regimi per gli attestati di attributi o di modificare un regime in esso registrato contiene almeno: a) il nome del regime, scelto dal titolare del regime per gli attestati di attributi e unico all'interno del catalogo di regimi per gli attestati di attributi; b) il nome e le informazioni di contatto del titolare del regime per gli attestati di attributi; c) lo stato e la versione del regime; d) un riferimento a eventuali leggi, norme o orientamenti specifici cui siano soggetti il rilascio, la convalida o l'utilizzo di un attestato elettronico di attributi rientrante nell'ambito di applicazione del regime; e) il formato o i formati degli attestati elettronici di attributi che rientrano nell'ambito di applicazione del regime; f) uno o più spazi dei nomi, identificatori degli attributi, descrizioni semantiche e tipi di dati di ciascun attributo facente parte di un attestato elettronico di attributi che rientra nell'ambito di applicazione del regime, mediante riferimento a un attributo nel catalogo di attributi di cui all'articolo 7 oppure mediante un attributo definito in modo analogo nell'ambito di applicazione del regime; g) una descrizione del modello di fiducia e dei meccanismi di governance applicati nell'ambito del regime, compresi i meccanismi di revoca; h) eventuali requisiti relativi ai fornitori degli attestati elettronici di attributi o alle fonti di informazione su cui tali fornitori fanno affidamento per il rilascio di attestati elettronici di attributi, comprese eventuali fonti autentiche, se del caso; i) una dichiarazione che indichi se gli attestati elettronici di attributi che rientrano nell'ambito di applicazione del regime devono essere rilasciati come attestati elettronici qualificati di attributi, come attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto, o in entrambe le forme.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 8 §4",
        "testo": "I regimi oggetto della richiesta di inclusione nel catalogo contengono solo attributi identificabili sulla base di identificatori unici; la richiesta di includere o modificare un regime per gli attestati di attributi e' firmata o sigillata dal richiedente mediante una firma elettronica qualificata o un sigillo elettronico qualificato o una firma elettronica avanzata o un sigillo elettronico avanzato basati su un certificato qualificato.",
        "testo_integrale": "4. I regimi oggetto della richiesta di inclusione nel catalogo contengono solo attributi identificabili sulla base di identificatori unici. La richiesta di includere o modificare un regime per gli attestati di attributi è firmata o sigillata dal richiedente mediante una firma elettronica qualificata o un sigillo elettronico qualificato o una firma elettronica avanzata o un sigillo elettronico avanzato basati su un certificato qualificato.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 8 §6",
        "testo": "Il catalogo di regimi per gli attestati di attributi, sigillato dalla Commissione, e' accessibile al pubblico, attraverso un canale sicuro, gratuitamente e senza previa identificazione o autenticazione, ed e' leggibile da dispositivi automatici e da utenti umani; il catalogo comprende anche una funzione di ricerca ed e' in un formato che garantisce l'integrita' e l'autenticita'.",
        "testo_integrale": "6. Il catalogo di regimi per gli attestati di attributi, sigillato dalla Commissione, è accessibile al pubblico, attraverso un canale sicuro, gratuitamente e senza previa identificazione o autenticazione, ed è leggibile da dispositivi automatici e da utenti umani. Il catalogo comprende anche una funzione di ricerca ed è in un formato che garantisce l'integrità e l'autenticità.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 8 §7",
        "testo": "La Commissione pubblica le specifiche tecniche da essa utilizzate per il catalogo di regimi per gli attestati di attributi.",
        "testo_integrale": "7. La Commissione pubblica le specifiche tecniche da essa utilizzate per il catalogo di regimi per gli attestati di attributi.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 8 §8",
        "testo": "La Commissione rilascia un identificatore unico per ciascun regime per gli attestati di attributi registrato.",
        "testo_integrale": "8. La Commissione rilascia un identificatore unico per ciascun regime per gli attestati di attributi registrato.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 9 §1",
        "testo": "Per consentire, su richiesta dell'utente, la verifica elettronica degli attributi di cui all'articolo 45 sexies, paragrafo 1, del regolamento (UE) n. 910/2014 da parte di prestatori di servizi fiduciari qualificati che rilasciano attestati elettronici qualificati di attributi, gli Stati membri istituiscono meccanismi che consentono tale verifica e possono mettere a disposizione punti di verifica unici per gli attributi di cui all'allegato VI di tale regolamento ogniqualvolta tali attributi facciano affidamento su fonti autentiche all'interno del settore pubblico; gli Stati membri pubblicano inoltre informazioni sulle procedure per avviare le richieste di verifica e per ricevere i risultati della verifica.",
        "testo_integrale": "1. Per consentire, su richiesta dell'utente, la verifica elettronica degli attributi di cui all'articolo 45 sexies, paragrafo 1, del regolamento (UE) n. 910/2014 da parte di prestatori di servizi fiduciari qualificati che rilasciano attestati elettronici qualificati di attributi, gli Stati membri istituiscono meccanismi che consentono tale verifica e possono mettere a disposizione punti di verifica unici per gli attributi di cui all'allegato VI di tale regolamento ogniqualvolta tali attributi facciano affidamento su fonti autentiche all'interno del settore pubblico. Gli Stati membri pubblicano informazioni sulle procedure per avviare le richieste di verifica e per ricevere i risultati della verifica.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 9 §2",
        "testo": "Il meccanismo di verifica fornisce un punto di accesso che i prestatori di servizi fiduciari qualificati che rilasciano attestati elettronici qualificati di attributi possono utilizzare per richiedere per via elettronica la verifica, rispetto a fonti autentiche o intermediari designati riconosciuti a livello nazionale, degli attributi di cui all'articolo 45 sexies, paragrafo 1, del regolamento (UE) n. 910/2014; gli attributi soggetti a verifica sono forniti al punto di verifica dal prestatore di servizi fiduciari qualificato su richiesta dell'utente; l'organismo del settore pubblico o l'intermediario designato condividono, attraverso il punto di verifica, i risultati della verifica con i prestatori di servizi fiduciari qualificati che rilasciano attestati elettronici qualificati di attributi.",
        "testo_integrale": "2. Il meccanismo di verifica fornisce un punto di accesso che i prestatori di servizi fiduciari qualificati che rilasciano attestati elettronici qualificati di attributi possono utilizzare per richiedere per via elettronica la verifica rispetto a fonti autentiche o intermediari designati riconosciuti a livello nazionale degli attributi di cui all'articolo 45 sexies, paragrafo 1, del regolamento (UE) n. 910/2014. Gli attributi soggetti a verifica saranno forniti al punto di verifica dal prestatore di servizi fiduciari qualificato su richiesta dell'utente. L'organismo del settore pubblico o l'intermediario designato condividono, attraverso il punto di verifica, i risultati della verifica con i prestatori di servizi fiduciari qualificati che rilasciano attestati elettronici qualificati di attributi.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 9 §3",
        "testo": "La richiesta di verifica indica gli attributi e i dati identificativi del soggetto cui si riferisce l'attributo per il quale il prestatore di servizi fiduciari qualificato richiede la verifica.",
        "testo_integrale": "3. La richiesta di verifica indica gli attributi e i dati identificativi del soggetto cui si riferisce l'attributo per il quale il prestatore di servizi fiduciari qualificato richiede la verifica.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 9 §4",
        "testo": "Il risultato della verifica indica esclusivamente se l'attributo e' stato verificato o no e specifica l'organismo del settore pubblico responsabile della fonte autentica o, se del caso, l'organismo del settore pubblico designato per agire per conto della fonte autentica rispetto alla quale e' stato verificato l'attributo.",
        "testo_integrale": "4. Il risultato della verifica indica esclusivamente se l'attributo è stato verificato o no e specifica l'organismo del settore pubblico responsabile della fonte autentica o, se del caso, l'organismo del settore pubblico designato per agire per conto della fonte autentica rispetto alla quale è stato verificato l'attributo.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 9 §5",
        "testo": "Gli Stati membri possono imporre controlli di accesso o altri meccanismi di verifica che garantiscano integrita', autenticita' e riservatezza per determinare se il richiedente sia un prestatore di servizi fiduciari qualificato e agisca su richiesta di un utente legittimo, e possono inoltre imporre, ove lo ritengano opportuno, meccanismi di controllo dell'uso dei metodi di verifica, tenendo conto dei fattori pertinenti, tra cui la possibilita' che le fonti autentiche contengano dati personali riservati o sensibili; se istituiscono tali meccanismi di controllo, gli Stati membri pubblicano informazioni sulla loro portata nell'ambito delle informazioni di cui al paragrafo 1.",
        "testo_integrale": "5. Gli Stati membri possono imporre controlli di accesso o altri meccanismi di verifica che garantiscano integrità, autenticità e riservatezza per determinare se il richiedente sia un prestatore di servizi fiduciari qualificato e agisca su richiesta di un utente legittimo. Gli Stati membri possono inoltre imporre meccanismi di controllo dell'uso dei metodi di verifica, ove lo ritengano opportuno, tenendo conto dei fattori pertinenti, tra cui la possibilità che le fonti autentiche contengano dati personali riservati o sensibili. Se istituiscono tali meccanismi di controllo, gli Stati membri pubblicano informazioni sulla loro portata nell'ambito delle informazioni di cui al paragrafo 1.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "l'obbligo di pubblicare informazioni sulla portata dei meccanismi di controllo dell'uso dei metodi di verifica si applica solo se gli Stati membri decidono di istituire tali meccanismi di controllo",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 §2",
        "testo": "Nell'istituire il sistema sicuro per le notifiche e l'elenco degli organismi del settore pubblico di cui agli articoli 5 e 6 e nel redigere i cataloghi di cui agli articoli 7 e 8, la Commissione europea, se del caso, fa riferimento ai servizi comuni del sistema tecnico a norma del regolamento (UE) 2018/1724 e li riutilizza.",
        "testo_integrale": "2. Nell'istituire il sistema sicuro per le notifiche e l'elenco degli organismi del settore pubblico di cui agli articoli 5 e 6 e nel redigere i cataloghi di cui agli articoli 7 e 8 del presente regolamento, la Commissione europea, se del caso, fa riferimento ai servizi comuni del sistema tecnico a norma del regolamento (UE) 2018/1724 e li riutilizza.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "il rinvio ai servizi comuni del sistema tecnico di cui al regolamento (UE) 2018/1724 e il loro riutilizzo sono dovuti solo ove appropriati (\"se del caso\") al sistema sicuro e ai cataloghi interessati",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 7 §4",
        "testo": "Gli Stati membri possono inoltre richiedere l'inclusione nel catalogo di attributi di attributi non figuranti nell'allegato VI del regolamento (UE) n. 910/2014, qualora tali attributi facciano affidamento su fonti autentiche del settore pubblico. I soggetti privati considerati una fonte primaria di informazioni o riconosciuti come autentici conformemente al diritto dell'Unione o nazionale, inclusa la prassi amministrativa, possono richiedere l'inclusione nel catalogo di attributi di attributi non figuranti nell'allegato VI, a condizione che il soggetto richiedente sia responsabile di tali attributi.",
        "testo_integrale": "4. Gli Stati membri possono inoltre richiedere l'inclusione di attributi non figuranti nell'allegato VI nel catalogo di attributi qualora tali attributi facciano affidamento su fonti autentiche del settore pubblico. I soggetti privati che sono considerati una fonte primaria di informazioni o che sono riconosciuti come autentici conformemente al diritto dell'Unione o nazionale, inclusa la prassi amministrativa, possono richiedere l'inclusione di attributi non figuranti nell'allegato VI nel catalogo di attributi a condizione che il soggetto richiedente sia responsabile di tali attributi.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "la facolta' riguarda solo attributi non figuranti nell'allegato VI del regolamento (UE) n. 910/2014: per gli Stati membri a condizione che facciano affidamento su fonti autentiche del settore pubblico, per i soggetti privati a condizione che il richiedente sia responsabile degli attributi e sia considerato fonte primaria di informazioni o riconosciuto come autentico dal diritto dell'Unione o nazionale (inclusa la prassi amministrativa)",
    },
    {
        "riferimento": "art. 7 §7",
        "testo": "La Commissione, a seguito della valutazione di cui al paragrafo 2 e dopo aver verificato che le informazioni fornite nella richiesta di inclusione o modifica di un attributo comprendano tutte le informazioni di cui al paragrafo 5, puo' inserire l'attributo o la modifica oggetto della richiesta nel catalogo di attributi. La disposizione attribuisce una facolta', non un obbligo di inserimento.",
        "testo_integrale": "7. La Commissione, a seguito della valutazione di cui al paragrafo 2 e dopo aver verificato che le informazioni fornite nella richiesta di inclusione o modifica di un attributo comprendano tutte le informazioni di cui al paragrafo 5, può inserire l'attributo o la modifica oggetto della richiesta nel catalogo di attributi.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "la facolta' di inserimento presuppone la valutazione di cui al paragrafo 2 e la verifica che la richiesta contenga tutte le informazioni di cui al paragrafo 5",
    },
    {
        "riferimento": "art. 8 §5",
        "testo": "La Commissione, a seguito della valutazione di cui al paragrafo 2 e dopo aver verificato che le informazioni fornite nella richiesta di inclusione o di modifica di un regime per gli attestati contengano tutti gli elementi elencati ai paragrafi 3 e 4, puo' inserire il regime o la modifica oggetto della richiesta nel catalogo di regimi per gli attestati di attributi. La disposizione attribuisce una facolta', non un obbligo di inserimento.",
        "testo_integrale": "5. La Commissione, a seguito della valutazione di cui al paragrafo 2 e dopo aver verificato che le informazioni fornite nella richiesta di inclusione o di modifica di un regime per gli attestati contengano tutti gli elementi elencati ai paragrafi 3 e 4, può inserire il regime o la modifica oggetto della richiesta nel catalogo di regimi per gli attestati di attributi.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "la facolta' di inserimento presuppone la valutazione di cui al paragrafo 2 e la verifica che la richiesta contenga tutti gli elementi elencati ai paragrafi 3 e 4",
    },
    {
        "riferimento": "art. 10 §1",
        "testo": "Ai fini degli articoli da 3 a 9 del presente regolamento, gli Stati membri possono fare riferimento ai servizi comuni del sistema tecnico di cui all'articolo 14 del regolamento (UE) 2018/1724, nonche' ai componenti nazionali ad essi connessi, e riutilizzarli.",
        "testo_integrale": "1. Ai fini degli articoli da 3 a 9, gli Stati membri possono fare riferimento ai servizi comuni del sistema tecnico di cui all'articolo 14 del regolamento (UE) 2018/1724, nonché ai componenti nazionali ad essi connessi, e riutilizzarli.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 11, entrata in vigore",
        "testo": "Il regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea.",
        "testo_integrale": "Il presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 11, applicazione",
        "testo": "Gli articoli da 6 a 9 del regolamento si applicano a decorrere dal 19 agosto 2026 (differimento dell'applicazione rispetto all'entrata in vigore, che riguarda solo questa porzione di articoli).",
        "testo_integrale": "Gli articoli da 6 a 9 si applicano a decorrere dal 19 agosto 2026.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 6 §1",
    "art. 6 §2",
    "art. 6 §2(a)",
    "art. 6 §2(b)",
    "art. 6 §2(c)",
    "art. 6 §3",
    "art. 6 §3(a)",
    "art. 6 §3(b)",
    "art. 6 §3(c)",
    "art. 6 §3(d)",
    "art. 7 §1",
    "art. 7 §2",
    "art. 7 §3",
    "art. 7 §4",
    "art. 7 §5",
    "art. 7 §5(a)",
    "art. 7 §5(b)",
    "art. 7 §5(c)",
    "art. 7 §5(d)",
    "art. 7 §5(e)",
    "art. 7 §5(f)",
    "art. 7 §5(g)",
    "art. 7 §5(h)",
    "art. 7 §6",
    "art. 7 §7",
    "art. 7 §8",
    "art. 7 §9",
    "art. 7 §10",
    "art. 8 §1",
    "art. 8 §2",
    "art. 8 §3",
    "art. 8 §3(a)",
    "art. 8 §3(b)",
    "art. 8 §3(c)",
    "art. 8 §3(d)",
    "art. 8 §3(e)",
    "art. 8 §3(f)",
    "art. 8 §3(g)",
    "art. 8 §3(h)",
    "art. 8 §3(i)",
    "art. 8 §4",
    "art. 8 §5",
    "art. 8 §6",
    "art. 8 §7",
    "art. 8 §8",
    "art. 9 §1",
    "art. 9 §2",
    "art. 9 §3",
    "art. 9 §4",
    "art. 9 §5",
    "art. 10 §1",
    "art. 10 §2",
    "art. 11, entrata in vigore",
    "art. 11, applicazione",
]

MAPPATURA_LOCALE = {
    "art. 6 §1": ["art. 6 §1"],
    "art. 6 §2": ["art. 6 §2", "art. 6 §2(a)", "art. 6 §2(b)", "art. 6 §2(c)"],
    "art. 6 §3": [
        "art. 6 §3",
        "art. 6 §3(a)",
        "art. 6 §3(b)",
        "art. 6 §3(c)",
        "art. 6 §3(d)",
    ],
    "art. 7 §1": ["art. 7 §1"],
    "art. 7 §2": ["art. 7 §2"],
    "art. 7 §3": ["art. 7 §3"],
    "art. 7 §4": ["art. 7 §4"],
    "art. 7 §5": [
        "art. 7 §5",
        "art. 7 §5(a)",
        "art. 7 §5(b)",
        "art. 7 §5(c)",
        "art. 7 §5(d)",
        "art. 7 §5(e)",
        "art. 7 §5(f)",
        "art. 7 §5(g)",
        "art. 7 §5(h)",
    ],
    "art. 7 §6": ["art. 7 §6"],
    "art. 7 §7": ["art. 7 §7"],
    "art. 7 §8": ["art. 7 §8"],
    "art. 7 §9": ["art. 7 §9"],
    "art. 7 §10": ["art. 7 §10"],
    "art. 8 §1": ["art. 8 §1"],
    "art. 8 §2": ["art. 8 §2"],
    "art. 8 §3": [
        "art. 8 §3",
        "art. 8 §3(a)",
        "art. 8 §3(b)",
        "art. 8 §3(c)",
        "art. 8 §3(d)",
        "art. 8 §3(e)",
        "art. 8 §3(f)",
        "art. 8 §3(g)",
        "art. 8 §3(h)",
        "art. 8 §3(i)",
    ],
    "art. 8 §4": ["art. 8 §4"],
    "art. 8 §5": ["art. 8 §5"],
    "art. 8 §6": ["art. 8 §6"],
    "art. 8 §7": ["art. 8 §7"],
    "art. 8 §8": ["art. 8 §8"],
    "art. 9 §1": ["art. 9 §1"],
    "art. 9 §2": ["art. 9 §2"],
    "art. 9 §3": ["art. 9 §3"],
    "art. 9 §4": ["art. 9 §4"],
    "art. 9 §5": ["art. 9 §5"],
    "art. 10 §1": ["art. 10 §1"],
    "art. 10 §2": ["art. 10 §2"],
    "art. 11, entrata in vigore": ["art. 11, entrata in vigore"],
    "art. 11, applicazione": ["art. 11, applicazione"],
}

# Relazioni native: art. 9 §1 e §2 citano testualmente l'art. 45 sexies §1
# eIDAS2 (verifica elettronica degli attributi rispetto a fonti autentiche),
# cioe' la disposizione di cui il meccanismo istituito dall'articolo da'
# attuazione. Il resto del capitolo (artt. 6-8, 10-11) non cita articoli
# eIDAS2: l'art. 8 §2-bis e' un rinvio interno del regolamento.
RELAZIONI = [
    {
        'nodo_da': ('obbligo', None, 'art. 9 §1'),
        'nodo_a': ('principio', 2, 'art. 45 sexies §1'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, 'art. 9 §2'),
        'nodo_a': ('principio', 2, 'art. 45 sexies §1'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
]
