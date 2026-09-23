"""Regolamento AgID recante le modalità attuative per la realizzazione dello
SPID (art. 4 c.2 DPCM 24/10/2014), v2.0 (22/07/2016) - Sezione IV (Rilascio e
consegna delle credenziali SPID, artt. 15-18) e CAPO III (Gestione del ciclo
di vita dell'identità digitale, artt. 19-24).

Estrazione granulare ADR-0007 dal testo ufficiale consolidato con Avviso
AgID n.10/2018 e Determinazione AgID n.425/2020 (fonte:
app/.source_cache/spid_modalita_attuative/cap02.txt).

Note di modellazione:

- Granularità di riga assegnata dal dispatch (INDICE_ARTICOLI_LOCALE fornito
  con un item per articolo intero, non per comma/lettera come nei capitoli
  DPCM/eIDAS/CAD): ogni articolo (artt. 15-24) riceve esattamente UNA riga
  (Obbligo o Principio), poiché `verifica_copertura` richiede che ciascun
  item dell'indice sia coperto da esattamente una riga e qui l'indice è
  definito a livello di intero articolo. Gli articoli di questa sezione sono
  descrizioni tecnico-procedurali continue (creazione/consegna/attivazione/
  conservazione/rinnovo delle credenziali, gestione del ciclo di vita
  dell'identità) senza commi numerati autonomi scindibili in prescrizioni
  indipendenti: l'accorpamento a livello di articolo rispetta comunque il
  criterio ADR-0007 (un'unica prescrizione continua per riga) applicato qui
  all'intero articolo anziché al comma.

- `riferimento` di riga usa la forma breve "art. N" (coerente con il
  precedente di app/seed_data/spid/cap01.py per articoli non scissi, es.
  "art. 4 c.1", e con app/seed_data/spid_modalita_attuative/cap04.py, che
  referenzia "art. 2"/"art. 12" in questo stesso formato); `MAPPATURA_LOCALE`
  mappa la forma breve alla stringa descrittiva completa richiesta in
  INDICE_ARTICOLI_LOCALE.

- Art. 17 (Attivazione delle credenziali) è puramente descrittivo/definitorio
  (nessun "deve" rivolto a un soggetto: descrive cos'è il processo di
  attivazione e da cosa dipende) -> Principio tipo "definitorio", stesso
  criterio di app/seed_data/spid/cap01.py per le disposizioni di cornice.
  Tutti gli altri nove articoli (15, 16, 18-24) contengono almeno una
  prescrizione comportamentale vincolante ("deve"/"devono"/tempi e modalità
  imposte) rivolta al gestore dell'identità digitale e/o all'utente ->
  Obbligo.

- Art. 19 e art. 20/23 impongono comportamenti sia al gestore sia
  all'utente (es. art. 19: l'utente è tenuto ad aggiornare i propri
  attributi, il gestore deve rendere disponibili area web e help desk; art.
  23: l'utente deve richiedere immediata sospensione in caso di
  smarrimento/furto, il gestore deve sospendere tempestivamente) -> entrambe
  le categorie compaiono in `soggetti` con ruolo "obbligato".

- Art. 20 e art. 23 (Avviso AgID n.10/2018 - inapplicabilità parziale): il
  testo ufficiale consolidato riporta in coda a ciascuno dei due articoli
  una NOTA che segnala l'inapplicabilità, per incompatibilità con il
  paragrafo 2.2.3(3) dell'allegato al Regolamento di esecuzione (UE)
  2015/1502, della sola previsione di riattivazione automatica dopo 30
  giorni di sospensione. La NOTA è testo ufficiale del regolamento
  consolidato (non un'elisione né un commento redazionale aggiunto in
  estrazione): è quindi inclusa verbatim in `testo_integrale` di entrambi
  gli Obblighi art. 20 e art. 23, non omessa né segnalata con marcatori di
  troncamento. Il contenuto integrale dell'Avviso n. 10 del 13 luglio 2018 è
  inoltre modellato come nodo Principio autonomo (tipo "altro"), NON incluso
  in INDICE_ARTICOLI_LOCALE/MAPPATURA_LOCALE (è un atto amministrativo
  separato dal regolamento, non un articolo di questo testo, quindi esente
  dalla verifica di copertura), collegato ad art. 20 e art. 23 con due
  relazioni "deroga a" (l'Avviso introduce un'eccezione puntuale alla
  riattivazione automatica, che per il resto degli effetti dei due articoli
  resta vigente: coerente con la definizione di "deroga a" in CLAUDE.md,
  diversa da "modifica"/"abroga").

- Art. 21 enumera alle lettere a)-f) i sei sotto-processi del ciclo di vita
  delle credenziali (creazione, consegna, attivazione, conservazione,
  sospensione/revoca, rinnovo/sostituzione), ciascuno trattato in dettaglio
  da un articolo dedicato di questo stesso capitolo (art. 15, 16, 17, 22,
  23, 24 rispettivamente): sei relazioni "specifica" (nodo_da = articolo di
  dettaglio, nodo_a = art. 21, che ne resta la cornice generale) rendono
  esplicito questo rapporto testuale. Art. 23 richiama esplicitamente art.
  20 ("Si veda il paragrafo sulla sospensione e revoca dell'identità
  digitale") con una relazione "richiama" testuale diretta.

- I riferimenti al "DPCM" presenti nel testo (es. art. 19 "attributi
  secondari così come definiti all'articolo 1, comma d) del DPCM", art. 20
  "ai sensi dell'articolo 8, comma 3... del DPCM") rimandano al DPCM 24
  ottobre 2014 (fonte_id=5), una Fonte diversa da questa (fonte_id=13):
  nessuna relazione cross-fonte è tentata in questo modulo, come da
  istruzioni di dispatch (causa nota di KeyError su merge parallelo).
  Analogamente nessuna relazione è tentata verso gli altri capitoli di
  questa stessa fonte (cap01, cap03, cap04) oltre a quanto confermato via
  coordinamento hub, per evitare riferimenti non verificati.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 15",
        "testo": "Il gestore dell'identità digitale crea le credenziali (o i mezzi per produrle), con eventuale personalizzazione e inizializzazione, e applica requisiti tecnici differenziati per livello di sicurezza SPID: al livello 1 password con requisiti minimi di complessità e durata massima 180 giorni; ai livelli 2 e 3 autenticazione a due fattori, quest'ultimo basato su certificati digitali.",
        "testo_integrale": "1. Il processo di creazione delle credenziali comprende le attività necessarie a dare origine ad una credenziale o ai mezzi per la sua produzione. 2. In alcuni casi le credenziali, o i mezzi usati per la loro produzione, richiedono una fase di pre-elaborazione prima della loro emissione, ad esempio personalizzazioni sulla base dell'identità a cui esse vengono rilasciate. In questi casi la personalizzazione può avvenire secondo diverse modalità in relazione alla tipologia di credenziale da emettere (ad esempio la personalizzazione di un dispositivo (card, token) che contiene le credenziali può includere la stampa (all'esterno del dispositivo) o la scrittura (sul chip del dispositivo) del nome del soggetto per cui le credenziali saranno emesse). Ovviamente alcune tipologie di credenziali, ad esempio la password, non richiedono alcun intervento di personalizzazione. Segue l'attività di inizializzazione delle credenziali operata al fine di assicurare che tutti i mezzi usati per la loro produzione siano successivamente idonei a supportare tutte le funzionalità attese. Per esempio, potrebbe essere richiesto che il chip della smart card calcoli la coppia di chiavi crittografiche. Analogamente, una smart card potrebbe essere emessa in uno stato \"bloccato\" e richiedere un PIN nel successivo processo di attivazione. Deve essere pure definita un'associazione fra una credenziale, o i mezzi usati per la sua produzione, e il soggetto per la quale viene emessa. Le modalità con cui viene operata tale associazione e il legame instaurato tra le credenziali e l'utente a cui afferiscono, dipendono anche dal livello di sicurezza SPID per il quale le stesse credenziali sono rilasciate. Per il livello 1 SPID (corrispondente al LoA2 dell'ISO-IEC 29115) sono accettabili credenziali composte da un singolo fattore (ad es. password). In particolare, in relazione al tipo della password, si raccomanda di adottare regole per ottenere password complesse e difficilmente attaccabili rispettando almeno i seguenti accorgimenti: a) lunghezza minima di otto caratteri; b) uso di caratteri maiuscoli e minuscoli; c) inclusione di uno o più caratteri numerici; d) non deve contenere più di due caratteri identici consecutivi. e) inclusione di almeno un carattere speciale ad es #, $, % ecc. Si raccomanda poi di vietare l'uso di informazioni non segrete riconducibili all'utente (ad es. codice fiscale, patente auto, sigle documenti, date, includere nomi, account-Id ecc.). Le password devono avere una durata massima non superiore a 180 giorni e non possono essere riusate, o avere elementi di similitudine, prima di cinque variazioni e comunque non prima di 15 mesi: in questa materia resta valida la normativa prevista dal Codice in materia di protezione dei dati personali (Artt. da 33 a 36) e, in particolare, dal Disciplinare tecnico in materia di misure minime di sicurezza (Allegato B del Codice privacy) aggiornato periodicamente in relazione all'evoluzione tecnica e all'esperienza maturata nel settore. Il Gestore dell'Identità adotta una procedura di sollecito con la quale invita l'utente a modificare la Password. Per il livello 2 SPID (corrispondente al LoA3 dell'ISO-IEC 29115), il gestore delle identità digitali deve rendere disponibili sistemi di autenticazione informatica a due fattori, non necessariamente basati su certificati digitali. In questo caso è accettabile l'utilizzo di una password (come sopra descritto) e l'adozione di una OTP generata, a titolo esemplificativo, con l'ausilio di un dispositivo fisico, l'invio di un SMS, liste-tabelle predefinite o applicazioni mobile per smartphone o tablet collegati in rete; resta chiaro che, trattandosi di un OTP, la sua validità è limitata solo ad una transazione nell'ambito della sessione applicativa e per un tempo limitato e dipendente dal contesto del servizio richiesto. Per il livello 3 SPID (corrispondente al LoA4 dell'ISO-IEC 29115), il gestore delle identità digitali deve rendere disponibili sistemi di autenticazione informatica a due fattori, basati su certificati digitali e criteri di custodia delle chiavi private su dispositivi che soddisfano i requisiti dell'Allegato II del Regolamento 910/2014. In merito alle possibili minacce che possono essere associabili alle varie tipologie di token, si veda l'Appendice B al presente documento. In appendice D è inoltre riportata una tassonomia dei tipi di token.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 16",
        "testo": "Il gestore delle identità digitali consegna le credenziali al legittimo destinatario con modalità e criteri di riservatezza adeguati al livello di sicurezza, garantendo l'informativa sugli obblighi di protezione delle credenziali e sulla procedura di autenticazione, nonché la conformità alla normativa privacy.",
        "testo_integrale": "Anche in questo caso, la complessità del processo dipende dal livello di sicurezza di autenticazione informatica SPID associato alla determinata credenziale. La consegna delle credenziali deve essere operata con modalità e strumenti che assicurino che la stessa sia effettuata al legittimo destinatario con adeguati criteri di riservatezza che salvaguardino il contenuto. Per alti livelli di sicurezza deve essere prevista una consegna con attestazione dell'effettivo ricevimento delle credenziali; per dispositivi software ciò può essere fatto attraverso sessioni protette per la spedizione in modalità elettronica che assicurino la verifica della corrispondenza tra richiedente dell'identità e destinatario delle credenziali. Per livelli più bassi può essere sufficiente inviare una password o un PIN direttamente all'indirizzo fisico, ad esempio con posta raccomandata, al domicilio elettronico, tramite posta elettronica o PEC, oppure tramite comunicazioni inviate al dispositivo mobile del titolare (smartphone, tablet, cellulare, ecc.). Il gestore delle identità digitali nella consegna delle credenziali garantisce: a) che il richiedente sia espressamente informato in modo compiuto e chiaro riguardo: 1) agli obblighi da quest'ultimo assunti in merito alla protezione della segretezza delle credenziali; 2) sulla procedura di autenticazione e sui necessari requisiti tecnici per accedervi; b) la rispondenza del proprio sistema di sicurezza dei dati alle misure di sicurezza per il trattamento dei dati personali, secondo quanto previsto dal decreto legislativo 30 giugno 2003, n. 196.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 18",
        "testo": "Il gestore dell'identità digitale, su richiesta dell'utente, segnala via email o SMS ogni utilizzo delle credenziali di accesso, con i relativi estremi (data, ora, fornitore del servizio).",
        "testo_integrale": "Il gestore dell'identità digitale, su richiesta dell'utente, segnala via email o via sms, rispettivamente alla casella di posta o sul riferimento telefonico indicato dall'utente ogni avvenuto utilizzo delle credenziali di accesso, inviandone gli estremi di utilizzo della credenziale (data, ora, fornitore del servizio) ad uno degli attributi secondari a tale scopo indicato dall'utente.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "su richiesta dell'utente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 19",
        "testo": "L'utente deve mantenere aggiornati i propri attributi identificativi (documento di riconoscimento, attributi secondari, dati della persona giuridica); il gestore dell'identità digitale rende disponibile un'area web dedicata e un servizio di help desk per gli aggiornamenti, verificandoli prima di registrarli e notificandoli all'utente.",
        "testo_integrale": "L'utente è tenuto a mantenere aggiornati, in maniera proattiva o a seguito di segnalazione da parte del gestore, i contenuti degli attributi identificativi di seguito elencati. a) Per le persone fisiche: 1. estremi del documento di riconoscimento e relativa scadenza; 2. gli attributi secondari così come definiti all'articolo 1, comma d) del DPCM; b) Per le persone giuridiche: 1. indirizzo sede legale 2. codice fiscale o P.IVA (nei rari casi di variazione a seguito di particolari mutazioni societarie) 3. rappresentante legale della società 4. attributi secondari così come definiti all'articolo 1, comma d) del DPCM. L'utente, in caso di dichiarazioni non fedeli o mendaci, si assume le responsabilità previste dalla legislazione vigente. Le modalità operative per gli aggiornamenti devono essere rese possibili attraverso un'area web dedicata del gestore delle identità digitali, accessibile mediante le credenziali SPID, di livello massimo tra quelle fornite all'utente dal gestore dell'identità digitale. Il gestore dell'identità digitale deve inoltre prevedere un servizio di help desk tramite mail o compilando un form on-line sul sito web. Inoltre potrà essere previsto un sistema attraverso il quale l'utente potrà effettuare autonomamente alcune operazioni. Ad ogni variazione da operare sugli attributi relativi ad una identità, il gestore dell'identità digitale, prima di aggiornare i dati registrati, deve eseguire le fasi di esame e verifica in relazione al livello SPID associato all'identità digitale. La richiesta di aggiornamento e aggiornamento devono essere notificati all'utente utilizzando un attributo secondario funzionale alle comunicazioni (ad es. l'indirizzo di posta elettronica se non è stato modificato durante la sessione di aggiornamento). Futuri sviluppi potranno includere aggiornamenti automatici sulla base di modifiche degli attributi identificativi o secondari effettuati da pubbliche amministrazioni (ad es. ANPR, comuni, motorizzazione ecc.).",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 20",
        "testo": "Il gestore dell'identità digitale revoca o sospende l'identità digitale nei casi tipizzati (inattività, decesso/estinzione, uso illecito, richiesta dell'utente, scadenza contrattuale o del documento), con obblighi di comunicazione e avvisi scaglionati all'utente e, nei casi di sospensione su richiesta, ripristino automatico trascorsi 30 giorni salvo conferma della revoca. Nota (Avviso AgID n.10/2018): la riattivazione automatica dopo 30 giorni non si applica per incompatibilità con il Regolamento di esecuzione (UE) 2015/1502, salvo che l'identità mantenga gli stessi requisiti di garanzia.",
        "testo_integrale": "Ai sensi dell'articolo 8, comma 3 e dell'articolo 9 del DPCM, il gestore revoca l'identità digitale nei casi seguenti: 1) risulta non attiva per un periodo superiore a 24 mesi; 2) per decesso della persona fisica; 3) per estinzione della persona giuridica; 4) per uso illecito dell'identità digitale; 5) per richiesta dell'utente; 6) per scadenza contrattuale; 7) per scadenza documento identità. Nel caso previsto dai punti 1 e 6, il gestore dell'identità digitale revoca di propria iniziativa l'identità, mettendo in atto meccanismi con i quali comunica la causa e la data della revoca al utente, con avvisi ripetuti (90, 30 e 10 giorni nonché il giorno precedente la revoca definitiva), utilizzando l'indirizzo di posta elettronica e il recapito di telefonia mobile (attributi secondari essenziali forniti per la comunicazione). Nei casi previsti dai punti 2 e 3, il gestore dell'identità digitale procede alla revoca dell'identità digitale, previo accertamento operato anche utilizzando i servizi messi a disposizione dalle convenzioni di cui all'articolo 4, comma 1, lettera c) del DPCM. In assenza di disponibilità dei predetti servizi, dovrà essere cura dei rappresentanti del soggetto utente (eredi o procuratore, amministrazione, società subentrante) presentare la documentazione necessaria all'accertamento della cessata sussistenza dei presupposti per l'esistenza dell'identità digitale. Il gestore, una volta in possesso della documentazione suddetta, dovrà procedere tempestivamente alla revoca. Nel caso previsto dal punto 7, il gestore dell'identità digitale sospende di propria iniziativa l'identità, mettendo in atto meccanismi con i quali comunica la causa e la data della sospensione al utente, utilizzando l'indirizzo di posta elettronica e il recapito di telefonia mobile (attributi secondari essenziali forniti per la comunicazione). Nel caso previsto dal punto 4, ovvero nel caso in cui il utente ritenga che la propria identità digitale sia stata utilizzata fraudolentemente, lo stesso può chiederne la sospensione con una delle seguenti modalità: a) richiesta al gestore inviata via PEC; b) richiesta, in formato elettronico e sottoscritta con firma digitale o elettronica, inviata tramite la casella di posta appositamente predisposta dal gestore. Il gestore deve fornire esplicita evidenza al utente dell'avvenuta presa in carico della richiesta e procedere alla immediata sospensione dell'identità digitale. Contestualmente il utente potrà richiedere al fornitore dei servizi presso il quale ritiene che la propria identità sia stata utilizzata fraudolentemente il blocco all'accesso della propria identità inviando una richiesta in tal senso con le stesse modalità sopra previste ad una casella di posta appositamente predisposta dal fornitore di servizi. Trascorsi trenta giorni dalla suddetta sospensione, il gestore provvede al ripristino dell'identità precedentemente sospesa qualora non riceva copia della denuncia presentata all'autorità giudiziaria per gli stessi fatti sui quali è stata basata la richiesta di sospensione. In caso contrario l'identità digitale viene ripristinata. Nel caso previsto dal punto 5, l'utente può chiedere al gestore dell'identità digitale, in qualsiasi momento e a titolo gratuito, la sospensione o la revoca della propria identità digitale seguendo modalità analoghe a quelle previste dal precedente punto 4, ovvero attraverso: c) richiesta al gestore inviata via PEC; d) richiesta inviata tramite la casella di posta nota al gestore in formato elettronico e sottoscritta con firma digitale o elettronica. Nel caso di richiesta di sospensione, trascorsi trenta giorni dalla suddetta sospensione, il gestore provvede al ripristino dell'identità precedentemente sospesa qualora non pervenga con le modalità sopra indicate una richiesta di revoca. La revoca di una identità digitale comporta conseguentemente la revoca delle relative credenziali. I gestori dell'identità digitale conservano la documentazione inerente al processo di adesione per un periodo pari a venti anni decorrenti dalla revoca dell'identità digitale. NOTA (Avviso AgID n. 10 del 13 luglio 2018): in considerazione del processo di notifica dello SPID di cui all'articolo 9 del Regolamento eIDAS, le previsioni del presente articolo in merito alla riattivazione automatica dell'identità sospesa dopo trenta giorni dalla sospensione non devono essere applicate, per incompatibilità con il paragrafo 2.2.3(3) dell'allegato al Regolamento di esecuzione (UE) 2015/1502, salvo che l'identità soddisfi gli stessi requisiti di garanzia posseduti prima della sospensione. Testo integrale dell'Avviso n. 10 riportato separatamente (vedi nodo dedicato).",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 21",
        "testo": "Il gestore documenta ogni fase del ciclo di vita delle credenziali (creazione, consegna, attivazione, conservazione, sospensione/revoca, rinnovo/sostituzione), conservando almeno data di creazione, identificativo, soggetto titolare, stato e date dei relativi eventi, nel rispetto della normativa privacy.",
        "testo_integrale": "La gestione del ciclo di vita delle credenziali può comprendere i seguenti processi: a) creazione delle credenziali; b) consegna delle credenziali o dei mezzi usati per la loro produzione; c) attivazione delle credenziali o dei mezzi usati per la loro produzione; d) conservazione delle credenziali; e) sospensione e revoca delle credenziali o mezzi usati per la loro produzione; f) rinnovo e sostituzione delle credenziali o mezzi usati per la loro produzione. Alcuni dei processi sopra elencati possono essere influenzati dal fatto che le credenziali siano rese operative attraverso l'ausilio di un dispositivo hardware. In merito alle possibili minacce associate al processo di emissione delle credenziali, si veda l'Appendice B al presente documento. Adeguata documentazione deve essere conservata per tutto il ciclo di vita di una credenziale. Come condizione minima, la documentazione dovrà essere mantenuta per avere traccia delle seguenti informazioni: a) la creazione della credenziale b) l'identificativo della credenziale; c) il soggetto per il quale è stata emessa; d) lo stato della credenziale. Opportuna documentazione sarà conservata per ogni sottoprocesso (creazione, emissione, attivazione, revoca, sospensione, rinnovo e sostituzione) del processo di gestione delle credenziali, nel pieno rispetto della normativa in materia di tutela dei dati personali di cui al decreto legislativo 30 giugno 2003, n. 196. Dovranno essere conservate almeno le informazioni relative alla data di creazione della credenziale, allo stato della stessa, alle date di consegna, di attivazione (se prevista) e di eventuale sospensione, revoca o cancellazione.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 22",
        "testo": "Il gestore protegge i file delle credenziali da accessi non autorizzati, limitandone l'accesso ad amministratori e applicazioni autorizzate e vietando la conservazione delle password in chiaro, con misure di crittografia o hashing/salt adeguate al livello SPID.",
        "testo_integrale": "Questo processo riguarda la conservazione delle credenziali o dei mezzi usati per loro produzione, in modo da garantirne la protezione contro abusi ed usi non autorizzati. A livello 1 SPID, i file delle credenziali devono essere protetti da un sistema di controllo in modo da limitare l'accesso agli amministratori e alle applicazioni autorizzate. Questi file non devono mai contenere le password in chiaro; allo scopo possono essere usate tecniche, come da standard internazionali e approvate dall'Agenzia, di crittografia o algoritmi di salt e hashing. A livello 2 e 3 SPID, vale quanto indicato a livello 1 con i necessari allineamenti e conformità agli standard e alla normativa vigente per i moduli crittografici e di sicurezza software/hardware, avendo cura di approntare misure adeguate a mitigare gli specifici rischi derivanti dalla particolare tecnologia adottata.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 23",
        "testo": "In caso di smarrimento, furto, uso fraudolento o emissione di una nuova credenziale sostitutiva, l'utente richiede immediatamente la sospensione delle credenziali e il gestore la dispone tempestivamente per un massimo di 30 giorni, ripristinandole automaticamente in assenza di denuncia o richiesta di revoca. Nota (Avviso AgID n.10/2018): la riattivazione automatica dopo 30 giorni non si applica per incompatibilità con il Regolamento di esecuzione (UE) 2015/1502, salvo che l'identità mantenga gli stessi requisiti di garanzia.",
        "testo_integrale": "La revoca è il processo che annulla definitivamente la validità delle credenziali. Diversamente, la sospensione è associata ad un processo di annullamento temporaneo. La revoca è disposta nei seguenti casi: 1) smarrimento, furto o altri danni/compromissioni (con formale denuncia presentata all'autorità giudiziaria); 2) utilizzo per scopi non autorizzati, abusivi o fraudolenti da parte di un terzo soggetto; 3) emissione di una nuova credenziale in sostituzione di una già in possesso dell'utente; emissione di una nuova credenziale in sostituzione di una scaduta. Nel caso previsto dal numero 1, l'utente deve effettuare immediata richiesta di sospensione delle credenziali. Se la richiesta dell'utente non viene effettuata tramite posta elettronica certificata, o sottoscritta con firma digitale o firma elettronica qualificata, il gestore dell'identità digitale deve verificare, anche attraverso uno o più attributi secondari, la provenienza della richiesta di sospensione da parte del soggetto utente. Il gestore dell'identità digitale sospende tempestivamente l'identità digitale per un periodo massimo di trenta giorni informandone il richiedente. Durante questo periodo può accadere che: a) il richiedente annulla la richiesta di sospensione (ad es. per ritrovamento) e quindi l'identità digitale viene ripristinata; b) il richiedente formalizza la richiesta presentando copia della denuncia presentata all'autorità giudiziaria, quindi l'identità digitale viene revocata. In assenza di quanto indicato nelle lettere a) o b), l'identità digitale sarà automaticamente ripristinata scaduto il periodo di 30 giorni dalla data della richiesta. Nel caso previsto dal numero 2, anche a seguito di segnalazioni ai sensi dell'articolo 8, comma 4 del DPCM, l'utente richiede la sospensione immediata dell'identità digitale al gestore del servizio. Si veda il paragrafo sulla sospensione e revoca dell'identità digitale. NOTA (Avviso AgID n. 10 del 13 luglio 2018): in considerazione del processo di notifica dello SPID di cui all'articolo 9 del Regolamento eIDAS, le previsioni del presente articolo in merito alla riattivazione automatica dell'identità sospesa dopo trenta giorni dalla sospensione non devono essere applicate, per incompatibilità con il paragrafo 2.2.3(3) dell'allegato al Regolamento di esecuzione (UE) 2015/1502, salvo che l'identità soddisfi gli stessi requisiti di garanzia posseduti prima della sospensione. Testo integrale dell'Avviso n. 10 riportato separatamente (vedi nodo dedicato).",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 24",
        "testo": "Alla scadenza, guasto o upgrade tecnologico, il gestore emette una nuova credenziale in sostituzione della precedente e ne revoca automaticamente la vecchia, comunicando la revoca all'utente con avvisi scaglionati; per alcune tipologie è prevista anche la distruzione fisica della credenziale revocata.",
        "testo_integrale": "Alcune tipologie di credenziali prevedono una scadenza temporale per l'uso. In questo caso il gestore dovrà provvedere tempestivamente alla creazione di una nuova credenziale da consegnare all'utente in sostituzione della vecchia scaduta. Situazione analoga è quella della sostituzione di una credenziale a seguito di guasto o per upgrade tecnologico (ad esempio nel caso di credenziali di livello 3 passaggio da chiavi da 128 bit a quelle da 256). Il gestore dell'identità, nel primo caso su richiesta dell'utente, nel secondo su sua iniziativa, emette la nuova credenziale e revoca automaticamente la vecchia. In entrambi i casi devono essere previsti meccanismi con i quali il gestore comunica la revoca all'utente, con avvisi ripetuti (90, 30 e 10 giorni nonché il giorno precedente la revoca definitiva), utilizzando l'indirizzo di posta elettronica e il recapito di telefonia mobile (attributi secondari essenziali forniti per la comunicazione). Si noti che, per alcune tipologie di credenziali, come ad es. quelle contenute su un dispositivo, può essere prevista (successivamente alla sua revoca) anche la distruzione fisica.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 17",
        "testo": "Definisce l'attivazione delle credenziali come il processo che rende le credenziali (o i mezzi per produrle) effettivamente operative e pronte all'utilizzo, con modalità dipendenti dalla tipologia di credenziale adottata (es. sblocco tramite password/codice iniziale, riattivazione dopo una sospensione).",
        "testo_integrale": "L'attivazione delle credenziali è il processo durante il quale le credenziali o i mezzi usati per produrle, sono rese effettivamente operative e pronte all'utilizzo. Il processo di attivazione dipende direttamente dalla tipologia di credenziali adottate, ad esempio in alcuni casi le credenziali sono definite in uno stato di blocco quando sono inizializzate e restano in questo stato fino alla consegna al soggetto richiedente, in modo da prevenire qualsiasi abuso. In altri casi può essere prevista una password o codice iniziale per lo sblocco delle credenziali. Si consideri pure che le credenziali possono essere attivate anche successivamente ad una sospensione, quando ad esempio la loro validità sia stata temporaneamente annullata.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Avviso AgID n. 10 del 13 luglio 2018",
        "testo": "L'Avviso AgID n. 10 del 13 luglio 2018 dichiara la parziale inapplicabilità degli artt. 20 e 23 del Regolamento nella parte in cui prevedono la riattivazione automatica dell'identità/credenziale sospesa dopo trenta giorni, per incompatibilità con il paragrafo 2.2.3(3) dell'allegato al Regolamento di esecuzione (UE) 2015/1502, salvo che l'identità soddisfi ancora gli stessi requisiti di garanzia posseduti prima della sospensione.",
        "testo_integrale": "SPID - Sistema Pubblico per l'Identità Digitale. Avviso nr. 10, 13 luglio 2018. Regolamento recante le modalità attuative. In considerazione del processo di notifica dello SPID di cui all'articolo 9 del Regolamento eIDAS, le previsioni contenute negli articoli 20 e 23 del Regolamento recante le modalità attuative per la realizzazione dello SPID, emesso ai sensi dell'articolo 4, comma 2, DPCM 24 ottobre 2014, in merito alla riattivazione automatica dell'identità sospesa dopo trenta giorni dalla sospensione, non devono essere applicate, per incompatibilità con il paragrafo 2.2.3 (3) dell'allegato al Regolamento di esecuzione (UE) 2015/1502, salvo che l'identità soddisfi gli stessi requisiti di garanzia posseduti prima della sospensione. Il Responsabile del progetto SPID.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 15 (Creazione delle credenziali)",
    "art. 16 (Consegna delle credenziali)",
    "art. 17 (Attivazione delle credenziali)",
    "art. 18 (Segnalazioni sull'utilizzo delle credenziali)",
    "art. 19 (Gestione attributi)",
    "art. 20 (Sospensione e revoca dell'identità digitale)",
    "art. 21 (Gestione del ciclo di vita delle credenziali)",
    "art. 22 (Conservazione delle credenziali)",
    "art. 23 (Sospensione e revoca delle credenziali)",
    "art. 24 (Rinnovo e sostituzione delle credenziali)",
]

MAPPATURA_LOCALE = {
    "art. 15": ["art. 15 (Creazione delle credenziali)"],
    "art. 16": ["art. 16 (Consegna delle credenziali)"],
    "art. 17": ["art. 17 (Attivazione delle credenziali)"],
    "art. 18": ["art. 18 (Segnalazioni sull'utilizzo delle credenziali)"],
    "art. 19": ["art. 19 (Gestione attributi)"],
    "art. 20": ["art. 20 (Sospensione e revoca dell'identità digitale)"],
    "art. 21": ["art. 21 (Gestione del ciclo di vita delle credenziali)"],
    "art. 22": ["art. 22 (Conservazione delle credenziali)"],
    "art. 23": ["art. 23 (Sospensione e revoca delle credenziali)"],
    "art. 24": ["art. 24 (Rinnovo e sostituzione delle credenziali)"],
}

RELAZIONI = [
    {
        "nodo_da": ("principio", None, "Avviso AgID n. 10 del 13 luglio 2018"),
        "nodo_a": ("obbligo", None, "art. 20"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
    {
        "nodo_da": ("principio", None, "Avviso AgID n. 10 del 13 luglio 2018"),
        "nodo_a": ("obbligo", None, "art. 23"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
    {
        "nodo_da": ("obbligo", None, "art. 23"),
        "nodo_a": ("obbligo", None, "art. 20"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", None, "art. 15"),
        "nodo_a": ("obbligo", None, "art. 21"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, "art. 16"),
        "nodo_a": ("obbligo", None, "art. 21"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
    {
        "nodo_da": ("principio", None, "art. 17"),
        "nodo_a": ("obbligo", None, "art. 21"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, "art. 22"),
        "nodo_a": ("obbligo", None, "art. 21"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, "art. 23"),
        "nodo_a": ("obbligo", None, "art. 21"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, "art. 24"),
        "nodo_a": ("obbligo", None, "art. 21"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
]
