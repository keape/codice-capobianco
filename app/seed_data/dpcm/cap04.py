"""Estrazione granulare DPCM 22 febbraio 2013 - Titolo II parte 3 (artt. 32-41: requisiti
di sicurezza dei sistemi operativi, sistema di generazione dei certificati qualificati,
accesso del pubblico ai certificati, piano per la sicurezza, giornale di controllo,
sistema di qualita' del certificatore, organizzazione del personale, requisiti di
competenza ed esperienza del personale, manuale operativo, riferimenti temporali
opponibili ai terzi).

Testo ufficiale fonte app/.source_cache/dpcm/cap04.txt (ADR-0007). Modulo generato
secondo il contratto di app/seed_data/lib.py: nessun discrimine di rilevanza, copertura
completa comma/lettera per comma/lettera.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 32 c.1",
        "testo": "Il certificatore deve sottoporre i sistemi operativi utilizzati per la "
                 "generazione delle chiavi, dei certificati qualificati e per la gestione del "
                 "registro dei certificati a un intervento di hardening che ne innalzi il "
                 "livello di sicurezza.",
        "testo_integrale": "I sistemi operativi dei sistemi di elaborazione utilizzati nelle "
                            "attivita' di certificazione per la generazione delle chiavi, la "
                            "generazione dei certificati qualificati e la gestione del registro "
                            "dei certificati qualificati, devono essere stati oggetto di "
                            "opportune personalizzazioni atte a innalzarne il livello di "
                            "sicurezza (hardening) a cura del certificatore.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 32 c.2",
        "testo": "L'Agenzia verifica l'idoneita' delle personalizzazioni di hardening "
                 "effettuate dal certificatore e gli indica eventuali azioni correttive da "
                 "adottare.",
        "testo_integrale": "Ai sensi dell'art. 31 del Codice, l'Agenzia verifica l'idoneita' "
                            "delle personalizzazioni di cui al comma 1 e indica al certificatore "
                            "eventuali azioni correttive.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 33 c.1",
        "testo": "I certificati qualificati sono generati su un sistema dedicato "
                 "esclusivamente a tale funzione, collocato in locali adeguatamente protetti.",
        "testo_integrale": "La generazione dei certificati qualificati avviene su un sistema "
                            "utilizzato esclusivamente per la generazione di certificati, situato "
                            "in locali adeguatamente protetti.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 33 c.2",
        "testo": "L'entrata e l'uscita dai locali protetti in cui avviene la generazione dei "
                 "certificati sono registrate sul giornale di controllo.",
        "testo_integrale": "L'entrata e l'uscita dai locali protetti e' registrata sul giornale "
                            "di controllo.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 33 c.3",
        "testo": "L'accesso ai sistemi di elaborazione per la generazione dei certificati e' "
                 "consentito, nei limiti delle funzioni assegnate, esclusivamente al personale "
                 "autorizzato e riconosciuto dal sistema all'apertura di ciascuna sessione.",
        "testo_integrale": "L'accesso ai sistemi di elaborazione e' consentito, limitatamente "
                            "alle funzioni assegnate, esclusivamente al personale autorizzato, "
                            "identificato attraverso un'opportuna procedura di riconoscimento da "
                            "parte del sistema al momento di apertura di ciascuna sessione.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 33 c.4",
        "testo": "L'inizio e la fine di ciascuna sessione di accesso ai sistemi di generazione "
                 "dei certificati sono registrati sul giornale di controllo.",
        "testo_integrale": "L'inizio e la fine di ciascuna sessione sono registrati sul "
                            "giornale di controllo.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 34 c.1",
        "testo": "Le liste dei certificati revocati e sospesi devono essere rese pubbliche.",
        "testo_integrale": "Le liste dei certificati revocati e sospesi sono rese pubbliche.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 34 c.2",
        "testo": "Su richiesta del titolare, i certificati qualificati possono essere resi "
                 "consultabili dal pubblico o comunicati a terzi per la verifica delle firme "
                 "digitali, solo nei casi consentiti dal titolare e nel rispetto della "
                 "disciplina sulla protezione dei dati personali.",
        "testo_integrale": "I certificati qualificati, su richiesta del titolare, possono "
                            "essere accessibili alla consultazione del pubblico nonche' "
                            "comunicati a terzi, al fine di verificare le firme digitali, "
                            "esclusivamente nei casi consentiti dal titolare del certificato e "
                            "nel rispetto del decreto legislativo 30 giugno 2003, n. 196.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "su richiesta del titolare del certificato ed "
                                     "esclusivamente nei casi da questi consentiti, nel rispetto "
                                     "del d.lgs. 196/2003",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 34 c.3",
        "testo": "Chi consulta le liste pubblicate dei certificati revocati e sospesi, o i "
                 "certificati qualificati resi accessibili al pubblico, puo' utilizzarli "
                 "esclusivamente ai fini della verifica della validita' delle firme "
                 "elettroniche qualificate e digitali.",
        "testo_integrale": "Le liste pubblicate dei certificati revocati e sospesi, nonche' i "
                            "certificati qualificati eventualmente resi accessibili alla "
                            "consultazione del pubblico, sono utilizzabili da chi li consulta "
                            "per le sole finalita' di applicazione delle norme che disciplinano "
                            "la verifica e la validita' delle firme elettroniche qualificate e "
                            "digitali.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 35 c.1",
        "testo": "Il certificatore definisce un piano per la sicurezza che contiene almeno: "
                 "struttura generale e logistica; infrastruttura di sicurezza fisica; "
                 "allocazione di servizi/uffici; funzioni e allocazione del personale; "
                 "attribuzione delle responsabilita'; algoritmi crittografici e sistemi "
                 "utilizzati; procedure operative; dispositivi installati; flussi di dati; "
                 "procedura di backup; procedura di continuita' operativa del servizio di "
                 "pubblicazione delle liste di revoca/sospensione; analisi dei rischi; "
                 "contromisure; verifiche e ispezioni; le misure adottate ai sensi degli artt. "
                 "32 comma 1 e 47 comma 2; procedura di gestione dei disastri; la procedura di "
                 "cui all'art. 8 comma 3 su conservazione/protezione dei supporti con le chiavi "
                 "esportate; misure di sicurezza e custodia dei dispositivi di firma remota; "
                 "modalita' di controllo esclusivo delle chiavi private sui dispositivi di "
                 "firma remota (art. 11 c.3); misure per la distruzione dei dispositivi HSM e "
                 "delle chiavi in caso di guasto che comprometta le funzionalita' di sicurezza "
                 "certificate.",
        "testo_integrale": "Il certificatore definisce un piano per la sicurezza nel quale "
                            "sono contenuti almeno i seguenti elementi: a) struttura generale, "
                            "modalita' operativa e struttura logistica; b) descrizione "
                            "dell'infrastruttura di sicurezza fisica rilevante ai fini "
                            "dell'attivita' di certificatore; c) allocazione dei servizi e "
                            "degli uffici negli immobili rilevanti ai fini dell'attivita' di "
                            "certificatore; d) descrizione delle funzioni del personale e sua "
                            "allocazione ai fini dell'attivita' di certificatore; e) "
                            "attribuzione delle responsabilita'; f) algoritmi crittografici o "
                            "altri sistemi utilizzati; g) descrizione delle procedure "
                            "utilizzate nell'attivita' di certificatore; h) descrizione dei "
                            "dispositivi installati; i) descrizione dei flussi di dati; l) "
                            "procedura di gestione delle copie di sicurezza dei dati; m) "
                            "procedura di continuita' operativa del servizio di pubblicazione "
                            "delle liste di revoca e sospensione; n) analisi dei rischi; o) "
                            "descrizione delle contromisure; p) descrizione delle verifiche e "
                            "delle ispezioni; q) descrizione delle misure adottate ai sensi "
                            "degli articoli 32, comma 1, e 47, comma 2; r) procedura di "
                            "gestione dei disastri; s) descrizione della procedura di cui "
                            "all'art. 8, comma 3, ponendo in rilievo le modalita' di "
                            "conservazione e protezione dei supporti contenenti le chiavi "
                            "esportate; t) misure di sicurezza per la protezione dei "
                            "dispositivi di firma remota, ivi comprese le modalita' di "
                            "custodia; u) limitatamente a quanto previsto all'art. 11, comma 3, "
                            "modalita' con cui e' assicurato il controllo esclusivo delle "
                            "chiavi private custodite sui dispositivi di firma remota; v) le "
                            "misure procedurali e tecniche applicate per la distruzione dei "
                            "dispositivi HSM e delle chiavi che contengono in caso di guasto "
                            "del dispositivo HSM che non consente l'applicazione delle "
                            "funzionalita' di sicurezza certificate implementate dai "
                            "dispositivi medesimi.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 35 c.4",
        "testo": "Il piano per la sicurezza, firmato dal legale rappresentante del "
                 "certificatore o dal responsabile della sicurezza delegato, e' consegnato "
                 "all'Agenzia in busta sigillata o cifrato, secondo le indicazioni "
                 "dell'Agenzia, per garantirne la riservatezza.",
        "testo_integrale": "Il piano per la sicurezza, sottoscritto dal legale rappresentante "
                            "del certificatore, ovvero dal responsabile della sicurezza da "
                            "questo delegato, e' consegnato all'Agenzia in busta sigillata o "
                            "cifrato, al fine di garantirne la riservatezza, in base alle "
                            "indicazioni fornite dall'Agenzia.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 35 c.5",
        "testo": "Il piano per la sicurezza deve rispettare le misure di sicurezza previste "
                 "dal Titolo V, Parte I, del d.lgs. 196/2003.",
        "testo_integrale": "Il piano per la sicurezza si attiene alle misure di sicurezza "
                            "previste dal Titolo V della Parte I del decreto legislativo 30 "
                            "giugno 2003, n. 196.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 36 c.3",
        "testo": "A ciascuna registrazione del giornale di controllo deve essere apposto un "
                 "riferimento temporale.",
        "testo_integrale": "A ciascuna registrazione e' apposto un riferimento temporale.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 36 c.4",
        "testo": "Il giornale di controllo deve essere tenuto in modo da garantire "
                 "l'autenticita' delle annotazioni e consentire la ricostruzione accurata di "
                 "tutti gli eventi rilevanti per la sicurezza.",
        "testo_integrale": "Il giornale di controllo e' tenuto in modo da garantire "
                            "l'autenticita' delle annotazioni e consentire la ricostruzione, "
                            "con la necessaria accuratezza, di tutti gli eventi rilevanti ai "
                            "fini della sicurezza.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 36 c.5",
        "testo": "L'integrita' del giornale di controllo deve essere verificata con frequenza "
                 "almeno mensile.",
        "testo_integrale": "L'integrita' del giornale di controllo e' verificata con frequenza "
                            "almeno mensile.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 36 c.6",
        "testo": "Le registrazioni del giornale di controllo devono essere conservate per "
                 "venti anni, salvo quanto previsto dall'art. 11 del d.lgs. 196/2003.",
        "testo_integrale": "Le registrazioni contenute nel giornale di controllo sono "
                            "conservate per un periodo pari a venti anni, salvo quanto "
                            "previsto dall'art. 11 del decreto legislativo n. 196 del 2003.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "condizione_applicabilita": "salvo quanto previsto dall'art. 11 del d.lgs. 196/2003",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 37 c.1",
        "testo": "Entro un anno dall'avvio dell'attivita' di certificazione, il certificatore "
                 "deve dichiarare la conformita' del proprio sistema di qualita' alle norme "
                 "ISO 9000 o a norme equivalenti.",
        "testo_integrale": "Entro un anno dall'avvio dell'attivita' di certificazione, il "
                            "certificatore dichiara la conformita' del proprio sistema di "
                            "qualita' alle norme ISO 9000, successive modifiche o a norme "
                            "equivalenti.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 37 c.2",
        "testo": "Il manuale della qualita' deve essere depositato presso l'Agenzia e reso "
                 "disponibile presso il certificatore.",
        "testo_integrale": "Il manuale della qualita' e' depositato presso l'Agenzia e reso "
                            "disponibile presso il certificatore.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 38 c.1",
        "testo": "Salvo quanto previsto al comma 3, l'organizzazione del certificatore deve "
                 "prevedere almeno le seguenti figure: responsabile della sicurezza; "
                 "responsabile del servizio di certificazione e validazione temporale; "
                 "responsabile della conduzione tecnica dei sistemi; responsabile dei servizi "
                 "tecnici e logistici; responsabile delle verifiche e delle ispezioni "
                 "(auditing).",
        "testo_integrale": "Fatto salvo quanto previsto al comma 3, l'organizzazione del "
                            "certificatore prevede almeno le seguenti figure professionali: a) "
                            "responsabile della sicurezza; b) responsabile del servizio di "
                            "certificazione e validazione temporale; c) responsabile della "
                            "conduzione tecnica dei sistemi; d) responsabile dei servizi "
                            "tecnici e logistici; e) responsabile delle verifiche e delle "
                            "ispezioni (auditing).",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "fatto salvo quanto previsto al comma 3",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 38 c.2",
        "testo": "Non e' consentito attribuire alla stessa persona piu' delle funzioni "
                 "previste dal comma 1.",
        "testo_integrale": "Non e' possibile attribuire al medesimo soggetto piu' funzioni tra "
                            "quelle previste dal comma 1.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 38 c.3",
        "testo": "Fermo restando che la responsabilita' resta del certificatore, alcune delle "
                 "responsabilita' previste possono essere affidate ad altre organizzazioni; in "
                 "tal caso il responsabile della sicurezza o altro dipendente designato "
                 "gestisce i rapporti con tali organizzazioni.",
        "testo_integrale": "Ferma restando la responsabilita' del certificatore, "
                            "l'organizzazione dello stesso puo' prevedere che alcune delle "
                            "suddette responsabilita' siano affidate ad altre organizzazioni. "
                            "In questo caso il responsabile della sicurezza o altro dipendente "
                            "appositamente designato gestisce i rapporti con tali figure "
                            "professionali.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 38 c.4",
        "testo": "La possibilita' di delega di cui al comma 3 non si applica in nessun caso "
                 "alle figure professionali del responsabile della sicurezza e del "
                 "responsabile delle verifiche e ispezioni (comma 1, lettere a) ed e)).",
        "testo_integrale": "In nessun caso quanto previsto al comma 3 si applica per le figure "
                            "professionali di cui al comma 1, lettere a) ed e).",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "con riferimento alle figure professionali di cui al comma "
                                     "1, lettere a) ed e)",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 39 c.1",
        "testo": "Il personale a cui sono attribuite le funzioni di cui all'art. 38 deve avere "
                 "almeno cinque anni di esperienza professionale nelle tecnologie informatiche "
                 "e delle telecomunicazioni.",
        "testo_integrale": "Il personale cui sono attribuite le funzioni previste dall'art. "
                            "38 deve aver maturato una esperienza professionale nelle "
                            "tecnologie informatiche e delle telecomunicazioni almeno "
                            "quinquennale.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 39 c.2",
        "testo": "Ogni aggiornamento del sistema di certificazione richiede un apposito "
                 "addestramento del personale.",
        "testo_integrale": "Per ogni aggiornamento apportato al sistema di certificazione e' "
                            "previsto un apposito addestramento.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 40 c.2",
        "testo": "Il manuale operativo deve essere depositato presso l'Agenzia e pubblicato "
                 "dal certificatore in modo da essere consultabile per via telematica.",
        "testo_integrale": "Il manuale operativo e' depositato presso l'Agenzia e pubblicato a "
                            "cura del certificatore in modo da essere consultabile per via "
                            "telematica.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 40 c.3",
        "testo": "Il manuale operativo deve contenere almeno: dati identificativi del "
                 "certificatore; dati e versione del manuale; responsabile del manuale; "
                 "obblighi di certificatore/titolare/richiedenti le informazioni di verifica; "
                 "responsabilita' e limitazioni agli indennizzi; indirizzo del sito con le "
                 "tariffe; modalita' di identificazione/registrazione degli utenti; modalita' "
                 "di generazione delle chiavi; modalita' di emissione dei certificati; "
                 "modalita' di gestione di sospensione/revoca; modalita' di sostituzione delle "
                 "chiavi; modalita' di gestione e accesso al registro dei certificati; "
                 "modalita' di apposizione del riferimento temporale; modalita' di protezione "
                 "dei dati personali; modalita' operative per il sistema di verifica delle "
                 "firme (art. 14 c.1); modalita' operative per la generazione della firma "
                 "elettronica qualificata e digitale.",
        "testo_integrale": "Il manuale contiene almeno le seguenti informazioni: a) dati "
                            "identificativi del certificatore; b) dati identificativi della "
                            "versione del manuale operativo; c) responsabile del manuale "
                            "operativo; d) definizione degli obblighi del certificatore, del "
                            "titolare e dei richiedenti le informazioni per la verifica delle "
                            "firme; e) definizione delle responsabilita' e delle eventuali "
                            "limitazioni agli indennizzi; f) indirizzo del sito web del "
                            "certificatore ove sono pubblicate le tariffe; g) modalita' di "
                            "identificazione e registrazione degli utenti; h) modalita' di "
                            "generazione delle chiavi per la creazione e la verifica della "
                            "firma; i) modalita' di emissione dei certificati; l) modalita' di "
                            "inoltro delle richieste e della gestione di sospensione e revoca "
                            "dei certificati; m) modalita' di sostituzione delle chiavi; n) "
                            "modalita' di gestione del registro dei certificati; o) modalita' "
                            "di accesso al registro dei certificati; p) modalita' per "
                            "l'apposizione e la definizione del riferimento temporale; q) "
                            "modalita' di protezione dei dati personali; r) modalita' "
                            "operative per l'utilizzo del sistema di verifica delle firme di "
                            "cui all'art. 14, comma 1; s) modalita' operative per la "
                            "generazione della firma elettronica qualificata e della firma "
                            "digitale.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 41 c.3",
        "testo": "L'ora assegnata ai riferimenti temporali di cui al comma 2 deve "
                 "corrispondere alla scala di tempo UTC(IEN) con uno scarto non superiore a un "
                 "minuto primo.",
        "testo_integrale": "L'ora assegnata ai riferimenti temporali di cui al comma 2 del "
                            "presente articolo, deve corrispondere alla scala di tempo "
                            "UTC(IEN), di cui al decreto del Ministro dell'industria, del "
                            "commercio e dell'artigianato 30 novembre 1993, n. 591, con una "
                            "differenza non superiore ad un minuto primo.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 32 c.3",
        "testo": "L'obbligo di hardening di cui al comma 1 non si applica al sistema "
                 "operativo dei dispositivi di firma.",
        "testo_integrale": "Il comma 1 non si applica al sistema operativo dei dispositivi di "
                            "firma.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 34 c.4",
        "testo": "Chiunque ha diritto di sapere se un certificato qualificato sia stato "
                 "rilasciato a proprio nome; le relative modalita' sono stabilite dal "
                 "provvedimento di cui all'art. 42, comma 10.",
        "testo_integrale": "Chiunque ha diritto di conoscere se a proprio nome sia stato "
                            "rilasciato un certificato qualificato. Le modalita' per ottenere "
                            "l'informazione di cui al primo periodo sono definite con il "
                            "provvedimento di cui all'art. 42, comma 10, del presente decreto.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["certificato qualificato di firma elettronica"],
    },
    {
        "riferimento": "art. 35 c.2",
        "testo": "Le informazioni previste dalle lettere t) e u) del comma 1 possono essere "
                 "oggetto di dichiarazioni separate del certificatore, a integrazione del "
                 "piano per la sicurezza.",
        "testo_integrale": "Quanto previsto dalle lettere t) e u) del comma 1 puo' essere "
                            "oggetto di dichiarazioni separate da parte del certificatore, ad "
                            "integrazione del piano per la sicurezza.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["dispositivo qualificato di creazione di firma elettronica"],
    },
    {
        "riferimento": "art. 35 c.3",
        "testo": "A seguito dell'analisi delle dichiarazioni di cui alle lettere t) e u) del "
                 "comma 1, l'Agenzia puo' imporre al certificatore limitazioni d'uso e di "
                 "valore sui certificati qualificati per la firma remota.",
        "testo_integrale": "L'Agenzia, a seguito dell'analisi di quanto dichiarato alle "
                            "lettere t) e u) del comma 1, puo' imporre al certificatore di "
                            "inserire nei certificati qualificati afferenti la firma remota "
                            "limitazioni d'uso e di valore.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "a seguito dell'analisi da parte dell'Agenzia di quanto "
                                     "dichiarato alle lettere t) e u) del comma 1",
        "oggetti_giuridici": [
            "certificato qualificato di firma elettronica",
            "dispositivo qualificato di creazione di firma elettronica",
        ],
    },
    {
        "riferimento": "art. 36 c.1",
        "testo": "Il giornale di controllo e' l'insieme delle registrazioni, anche "
                 "automatiche, effettuate dai dispositivi installati presso il certificatore "
                 "al verificarsi delle condizioni previste dal decreto.",
        "testo_integrale": "Il giornale di controllo e' costituito dall'insieme delle "
                            "registrazioni effettuate anche automaticamente dai dispositivi "
                            "installati presso il certificatore, allorche' si verificano le "
                            "condizioni previste dal presente decreto.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 36 c.2",
        "testo": "Le registrazioni del giornale di controllo possono essere effettuate anche "
                 "indipendentemente, su supporti distinti e di tipo diverso.",
        "testo_integrale": "Le registrazioni possono essere effettuate indipendentemente "
                            "anche su supporti distinti e di tipo diverso.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 40 c.1",
        "testo": "Il manuale operativo definisce le procedure applicate dal certificatore che "
                 "rilascia certificati qualificati nello svolgimento della sua attivita'.",
        "testo_integrale": "Il manuale operativo definisce le procedure applicate dal "
                            "certificatore che rilascia certificati qualificati nello "
                            "svolgimento della sua attivita'.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["certificato qualificato di firma elettronica"],
    },
    {
        "riferimento": "art. 41 c.1",
        "testo": "I riferimenti temporali realizzati dai certificatori accreditati in "
                 "conformita' al titolo IV sono opponibili ai terzi ai sensi dell'art. 20, "
                 "comma 3, del Codice.",
        "testo_integrale": "I riferimenti temporali realizzati dai certificatori accreditati "
                            "in conformita' con quanto disposto dal titolo IV sono opponibili "
                            "ai terzi ai sensi dell'art. 20, comma 3, del Codice.",
        "tipo_principio": "valore probatorio",
        "stato": "vigente",
        "oggetti_giuridici": ["marca temporale elettronica qualificata"],
    },
    {
        "riferimento": "art. 41 c.2",
        "testo": "I riferimenti temporali apposti sul giornale di controllo da un "
                 "certificatore accreditato, secondo il proprio manuale operativo, sono "
                 "opponibili ai terzi ai sensi dell'art. 20, comma 3, del Codice.",
        "testo_integrale": "I riferimenti temporali apposti sul giornale di controllo da un "
                            "certificatore accreditato, secondo quanto indicato nel proprio "
                            "manuale operativo, sono opponibili ai terzi ai sensi dell'art. "
                            "20, comma 3, del Codice.",
        "tipo_principio": "valore probatorio",
        "stato": "vigente",
        "oggetti_giuridici": ["marca temporale elettronica qualificata"],
    },
    {
        "riferimento": "art. 41 c.4",
        "testo": "Costituiscono altresi' validazione temporale: il riferimento temporale "
                 "nella segnatura di protocollo (D.P.C.M. 31/10/2000); quello ottenuto tramite "
                 "la procedura di conservazione dei documenti da parte di un pubblico "
                 "ufficiale o di una pubblica amministrazione; quello ottenuto tramite posta "
                 "elettronica certificata (art. 48 del Codice); quello ottenuto tramite la "
                 "marcatura postale elettronica secondo la Convenzione postale universale.",
        "testo_integrale": "Costituiscono inoltre validazione temporale: a) il riferimento "
                            "temporale contenuto nella segnatura di protocollo di cui all'art. "
                            "9 del decreto del Presidente del Consiglio dei Ministri, 31 "
                            "ottobre 2000, pubblicato nella Gazzetta Ufficiale 21 novembre "
                            "2000, n. 272; b) il riferimento temporale ottenuto attraverso la "
                            "procedura di conservazione dei documenti in conformita' alle "
                            "norme vigenti, ad opera di un pubblico ufficiale o di una "
                            "pubblica amministrazione; c) il riferimento temporale ottenuto "
                            "attraverso l'utilizzo di posta elettronica certificata ai sensi "
                            "dell'art. 48 del Codice; d) il riferimento temporale ottenuto "
                            "attraverso l'utilizzo della marcatura postale elettronica ai "
                            "sensi dell'art. 14, comma 1, punto 1.4 della Convenzione postale "
                            "universale, come modificata dalle decisioni adottate dal XXIII "
                            "Congresso dell'Unione postale universale, recepite dal "
                            "Regolamento di esecuzione emanato con il decreto del Presidente "
                            "della Repubblica 12 gennaio 2007, n. 18.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 32 c.1", "art. 32 c.2", "art. 32 c.3",
    "art. 33 c.1", "art. 33 c.2", "art. 33 c.3", "art. 33 c.4",
    "art. 34 c.1", "art. 34 c.2", "art. 34 c.3", "art. 34 c.4",
    "art. 35 c.1 lett.a)", "art. 35 c.1 lett.b)", "art. 35 c.1 lett.c)",
    "art. 35 c.1 lett.d)", "art. 35 c.1 lett.e)", "art. 35 c.1 lett.f)",
    "art. 35 c.1 lett.g)", "art. 35 c.1 lett.h)", "art. 35 c.1 lett.i)",
    "art. 35 c.1 lett.l)", "art. 35 c.1 lett.m)", "art. 35 c.1 lett.n)",
    "art. 35 c.1 lett.o)", "art. 35 c.1 lett.p)", "art. 35 c.1 lett.q)",
    "art. 35 c.1 lett.r)", "art. 35 c.1 lett.s)", "art. 35 c.1 lett.t)",
    "art. 35 c.1 lett.u)", "art. 35 c.1 lett.v)",
    "art. 35 c.2", "art. 35 c.3", "art. 35 c.4", "art. 35 c.5",
    "art. 36 c.1", "art. 36 c.2", "art. 36 c.3", "art. 36 c.4", "art. 36 c.5",
    "art. 36 c.6",
    "art. 37 c.1", "art. 37 c.2",
    "art. 38 c.1 lett.a)", "art. 38 c.1 lett.b)", "art. 38 c.1 lett.c)",
    "art. 38 c.1 lett.d)", "art. 38 c.1 lett.e)",
    "art. 38 c.2", "art. 38 c.3", "art. 38 c.4",
    "art. 39 c.1", "art. 39 c.2",
    "art. 40 c.1", "art. 40 c.2",
    "art. 40 c.3 lett.a)", "art. 40 c.3 lett.b)", "art. 40 c.3 lett.c)",
    "art. 40 c.3 lett.d)", "art. 40 c.3 lett.e)", "art. 40 c.3 lett.f)",
    "art. 40 c.3 lett.g)", "art. 40 c.3 lett.h)", "art. 40 c.3 lett.i)",
    "art. 40 c.3 lett.l)", "art. 40 c.3 lett.m)", "art. 40 c.3 lett.n)",
    "art. 40 c.3 lett.o)", "art. 40 c.3 lett.p)", "art. 40 c.3 lett.q)",
    "art. 40 c.3 lett.r)", "art. 40 c.3 lett.s)",
    "art. 41 c.1", "art. 41 c.2", "art. 41 c.3",
    "art. 41 c.4 lett.a)", "art. 41 c.4 lett.b)", "art. 41 c.4 lett.c)",
    "art. 41 c.4 lett.d)",
]

MAPPATURA_LOCALE = {
    "art. 32 c.1": ["art. 32 c.1"],
    "art. 32 c.2": ["art. 32 c.2"],
    "art. 32 c.3": ["art. 32 c.3"],
    "art. 33 c.1": ["art. 33 c.1"],
    "art. 33 c.2": ["art. 33 c.2"],
    "art. 33 c.3": ["art. 33 c.3"],
    "art. 33 c.4": ["art. 33 c.4"],
    "art. 34 c.1": ["art. 34 c.1"],
    "art. 34 c.2": ["art. 34 c.2"],
    "art. 34 c.3": ["art. 34 c.3"],
    "art. 34 c.4": ["art. 34 c.4"],
    "art. 35 c.1": [
        "art. 35 c.1 lett.a)", "art. 35 c.1 lett.b)", "art. 35 c.1 lett.c)",
        "art. 35 c.1 lett.d)", "art. 35 c.1 lett.e)", "art. 35 c.1 lett.f)",
        "art. 35 c.1 lett.g)", "art. 35 c.1 lett.h)", "art. 35 c.1 lett.i)",
        "art. 35 c.1 lett.l)", "art. 35 c.1 lett.m)", "art. 35 c.1 lett.n)",
        "art. 35 c.1 lett.o)", "art. 35 c.1 lett.p)", "art. 35 c.1 lett.q)",
        "art. 35 c.1 lett.r)", "art. 35 c.1 lett.s)", "art. 35 c.1 lett.t)",
        "art. 35 c.1 lett.u)", "art. 35 c.1 lett.v)",
    ],
    "art. 35 c.2": ["art. 35 c.2"],
    "art. 35 c.3": ["art. 35 c.3"],
    "art. 35 c.4": ["art. 35 c.4"],
    "art. 35 c.5": ["art. 35 c.5"],
    "art. 36 c.1": ["art. 36 c.1"],
    "art. 36 c.2": ["art. 36 c.2"],
    "art. 36 c.3": ["art. 36 c.3"],
    "art. 36 c.4": ["art. 36 c.4"],
    "art. 36 c.5": ["art. 36 c.5"],
    "art. 36 c.6": ["art. 36 c.6"],
    "art. 37 c.1": ["art. 37 c.1"],
    "art. 37 c.2": ["art. 37 c.2"],
    "art. 38 c.1": [
        "art. 38 c.1 lett.a)", "art. 38 c.1 lett.b)", "art. 38 c.1 lett.c)",
        "art. 38 c.1 lett.d)", "art. 38 c.1 lett.e)",
    ],
    "art. 38 c.2": ["art. 38 c.2"],
    "art. 38 c.3": ["art. 38 c.3"],
    "art. 38 c.4": ["art. 38 c.4"],
    "art. 39 c.1": ["art. 39 c.1"],
    "art. 39 c.2": ["art. 39 c.2"],
    "art. 40 c.1": ["art. 40 c.1"],
    "art. 40 c.2": ["art. 40 c.2"],
    "art. 40 c.3": [
        "art. 40 c.3 lett.a)", "art. 40 c.3 lett.b)", "art. 40 c.3 lett.c)",
        "art. 40 c.3 lett.d)", "art. 40 c.3 lett.e)", "art. 40 c.3 lett.f)",
        "art. 40 c.3 lett.g)", "art. 40 c.3 lett.h)", "art. 40 c.3 lett.i)",
        "art. 40 c.3 lett.l)", "art. 40 c.3 lett.m)", "art. 40 c.3 lett.n)",
        "art. 40 c.3 lett.o)", "art. 40 c.3 lett.p)", "art. 40 c.3 lett.q)",
        "art. 40 c.3 lett.r)", "art. 40 c.3 lett.s)",
    ],
    "art. 41 c.1": ["art. 41 c.1"],
    "art. 41 c.2": ["art. 41 c.2"],
    "art. 41 c.3": ["art. 41 c.3"],
    "art. 41 c.4": [
        "art. 41 c.4 lett.a)", "art. 41 c.4 lett.b)", "art. 41 c.4 lett.c)",
        "art. 41 c.4 lett.d)",
    ],
}

RELAZIONI = [
    {
        "nodo_da": ("principio", None, "art. 32 c.3"),
        "nodo_a": ("obbligo", None, "art. 32 c.1"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 35 c.1"),
        "nodo_a": ("obbligo", None, "art. 32 c.1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "art. 35 c.2"),
        "nodo_a": ("obbligo", None, "art. 35 c.1"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "art. 35 c.3"),
        "nodo_a": ("obbligo", None, "art. 35 c.1"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 38 c.3"),
        "nodo_a": ("obbligo", None, "art. 38 c.1"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 38 c.2"),
        "nodo_a": ("obbligo", None, "art. 38 c.1"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 38 c.4"),
        "nodo_a": ("obbligo", None, "art. 38 c.3"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 39 c.1"),
        "nodo_a": ("obbligo", None, "art. 38 c.1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 41 c.3"),
        "nodo_a": ("principio", None, "art. 41 c.2"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": None,
    },
]
