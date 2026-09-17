"""Estrazione granulare CAD (D.Lgs. 82/2005) - Capo II parte 2 (artt. 29-38: prestatori
servizi fiduciari, responsabilita', sanzioni, dispositivi firma qualificata, revoca/sospensione
certificati, cessazione attivita', trasferimenti fondi), Capo III (artt. 39-44-bis: formazione,
protocollo, dematerializzazione e conservazione dei documenti delle pubbliche amministrazioni),
Capo IV parte 1 (artt. 45-47: trasmissione informatica dei documenti).

Testo ufficiale vigente al 16/09/2026, fonte app/.source_cache/cad/cap04.txt (ADR-0007).
Modulo generato secondo il contratto di app/seed_data/lib.py: nessun discrimine di rilevanza,
copertura completa comma/lettera per comma/lettera.
"""

RIGHE_OBBLIGHI = [{'riferimento': 'art. 29 c.1',
  'testo': "I soggetti che intendono fornire servizi fiduciari qualificati o svolgere l'attività "
           "di gestore di posta elettronica certificata presentano all'AgID domanda di "
           'qualificazione, secondo le modalità fissate dalle Linee guida.',
  'testo_integrale': 'I soggetti che intendono fornire servizi fiduciari qualificati o svolgere '
                     "l'attivita' di gestore di posta elettronica certificata ((...)) presentano "
                     "all'AgID domanda di qualificazione, secondo le modalita' fissate dalle Linee "
                     'guida. ((PERIODO SOPPRESSO DAL D.L. 16 LUGLIO 2020, N. 76)).',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 29 c.2',
  'testo': 'Ai fini della qualificazione, i soggetti richiedenti devono possedere i requisiti '
           "dell'art. 24 del Regolamento eIDAS e requisiti di onorabilità, affidabilità, "
           'tecnologici e organizzativi compatibili con la disciplina europea, oltre a garanzie '
           'assicurative adeguate; un DPCM definisce tali requisiti, i criteri per le tariffe '
           "dovute all'AgID e le condizioni per lo svolgimento dell'attività da parte di "
           'amministrazioni pubbliche.',
  'testo_integrale': '((Ai fini della qualificazione, i soggetti di cui al comma 1 devono '
                     "possedere i requisiti di cui all'articolo 24 del Regolamento (UE) 23 luglio "
                     "2014, n. 910/2014, disporre di requisiti di onorabilita', affidabilita', "
                     "tecnologici e organizzativi compatibili con la disciplina europea, nonche' "
                     "di garanzie assicurative adeguate rispetto all'attivita' svolta. Con decreto "
                     'del Presidente del Consiglio dei ministri, o del Ministro delegato per '
                     "l'innovazione tecnologica e la digitalizzazione, sentita l'AgID, nel "
                     'rispetto della disciplina europea, sono definiti i predetti requisiti in '
                     "relazione alla specifica attivita' che i soggetti di cui al comma 1 "
                     "intendono svolgere.)) Il predetto decreto determina altresi' i criteri per "
                     "la fissazione delle tariffe dovute all'AgID per lo svolgimento delle "
                     "predette attivita', nonche' i requisiti e le condizioni per lo svolgimento "
                     "delle attivita' di cui al comma 1 da parte di amministrazioni pubbliche.",
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 29 c.3',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 13 DICEMBRE 2017, N. 217. (29)',
  'tipo_obbligo': 'procedurale',
  'stato': 'abrogato'},
 {'riferimento': 'art. 29 c.5',
  'testo': 'Il termine di novanta giorni per la qualificazione può essere sospeso una sola volta, '
           'entro trenta giorni dalla presentazione della domanda, per richiedere documenti '
           "integrativi non già disponibili o acquisibili autonomamente dall'AgID; il termine "
           'riprende a decorrere dalla ricezione della documentazione integrativa.',
  'testo_integrale': "Il termine di cui al comma 4, puo' essere sospeso una sola volta entro "
                     'trenta giorni dalla data di presentazione della domanda, esclusivamente per '
                     'la motivata richiesta di documenti che integrino o completino la '
                     "documentazione presentata e che non siano gia' nella disponibilita' del AgID "
                     'o che questo non possa acquisire autonomamente. In tale caso, il termine '
                     'riprende a decorrere dalla data di ricezione della documentazione '
                     'integrativa.',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 29 c.6',
  'testo': "A seguito dell'accoglimento della domanda, l'AgID dispone l'iscrizione del richiedente "
           "in un apposito elenco di fiducia pubblico, tenuto dall'AgID e consultabile anche "
           'telematicamente.',
  'testo_integrale': "A seguito dell'accoglimento della domanda, il AgID dispone l'iscrizione del "
                     'richiedente in un apposito elenco di fiducia pubblico, tenuto dal AgID '
                     "stesso e consultabile anche in via telematica, ai fini dell'applicazione "
                     'della disciplina in questione.',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 29 c.7',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_obbligo': 'procedurale',
  'stato': 'abrogato'},
 {'riferimento': 'art. 29 c.8',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_obbligo': 'procedurale',
  'stato': 'abrogato'},
 {'riferimento': 'art. 30 c.1',
  'testo': 'I prestatori di servizi fiduciari qualificati e i gestori di posta elettronica '
           "certificata iscritti nell'elenco, nonché i gestori dell'identità digitale e i "
           'conservatori di documenti informatici, che causano danno ad altri nello svolgimento '
           'della loro attività sono tenuti al risarcimento, salvo che provino di aver adottato '
           'tutte le misure idonee a evitare il danno.',
  'testo_integrale': '((I prestatori di servizi fiduciari qualificati e i gestori di posta '
                     "elettronica certificata, iscritti nell'elenco di cui all'articolo 29, comma "
                     "6, nonche' i gestori dell'identita' digitale e i conservatori di documenti "
                     'informatici)), che cagionano danno ad altri nello svolgimento della loro '
                     "attivita', sono tenuti al risarcimento, se non provano di avere adottato "
                     'tutte le misure idonee a evitare il danno.',
  'tipo_obbligo': 'sanzionatorio',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 30 c.2',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_obbligo': 'sanzionatorio',
  'stato': 'abrogato'},
 {'riferimento': 'art. 32 c.1',
  'testo': 'Il titolare del certificato di firma deve assicurare la custodia del dispositivo di '
           "firma o degli strumenti di autenticazione informatica per l'uso del dispositivo da "
           'remoto, adottare tutte le misure organizzative e tecniche idonee a evitare danno ad '
           'altri, e utilizzare personalmente il dispositivo di firma.',
  'testo_integrale': "Il titolare del certificato di firma e' tenuto ad assicurare la custodia del "
                     'dispositivo di firma o degli strumenti di autenticazione informatica per '
                     "l'utilizzo del dispositivo di firma da remoto, e ad adottare tutte le misure "
                     "organizzative e tecniche idonee ad evitare danno ad altri; e' altresi' "
                     'tenuto ad utilizzare personalmente il dispositivo di firma.',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'Utente/titolare', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.2',
  'testo': 'Il prestatore di servizi di firma elettronica qualificata deve adottare tutte le '
           'misure organizzative e tecniche idonee a evitare danno a terzi.',
  'testo_integrale': "Il prestatore di servizi di firma elettronica qualificata e' tenuto ad "
                     'adottare tutte le misure organizzative e tecniche idonee ad evitare danno a '
                     'terzi.',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.3 lett.a',
  'testo': "Provvedere con certezza all'identificazione della persona che richiede la "
           'certificazione.',
  'testo_integrale': 'Il prestatore di servizi di firma elettronica qualificata che rilascia '
                     '((...)) certificati qualificati deve comunque: a) provvedere con certezza '
                     'alla identificazione della persona che fa richiesta della certificazione;',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.3 lett.b',
  'testo': 'Rilasciare e rendere pubblico il certificato elettronico nei modi o nei casi stabiliti '
           'dalle Linee guida, nel rispetto della disciplina sulla protezione dei dati personali.',
  'testo_integrale': 'b) rilasciare e rendere pubblico il certificato elettronico nei modi o nei '
                     'casi stabiliti dalle ((Linee guida)), nel rispetto del decreto legislativo '
                     '30 giugno 2003, n. 196, e successive modificazioni;',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.3 lett.c',
  'testo': "Specificare nel certificato qualificato, su richiesta dell'istante e col consenso del "
           'terzo interessato, i poteri di rappresentanza o altri titoli professionali, previa '
           'verifica della documentazione presentata.',
  'testo_integrale': "c) specificare, nel certificato qualificato su richiesta dell'istante, e con "
                     'il consenso del terzo interessato, i poteri di rappresentanza o altri titoli '
                     "relativi all'attivita' professionale o a cariche rivestite, previa verifica "
                     'della documentazione presentata dal richiedente che attesta la sussistenza '
                     'degli stessi;',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.3 lett.d',
  'testo': 'Attenersi alle Linee guida.',
  'testo_integrale': 'd) attenersi alle ((Linee guida));',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.3 lett.e',
  'testo': 'Informare i richiedenti in modo compiuto e chiaro sulla procedura di certificazione, '
           "sui requisiti tecnici necessari e sulle caratteristiche e limitazioni d'uso delle "
           'firme emesse.',
  'testo_integrale': 'e) informare i richiedenti in modo compiuto e chiaro, sulla procedura di '
                     'certificazione e sui necessari requisiti tecnici per accedervi e sulle '
                     "caratteristiche e sulle limitazioni d'uso delle firme emesse sulla base del "
                     'servizio di certificazione;',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.3 lett.f',
  'testo': 'Lettera soppressa dal D.Lgs. 30 dicembre 2010, n. 235.',
  'testo_integrale': 'f) LETTERA SOPPRESSA DAL D.LGS. 30 DICEMBRE 2010, N. 235;',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.3 lett.g',
  'testo': 'Procedere alla tempestiva pubblicazione della revoca e della sospensione del '
           'certificato elettronico su richiesta del titolare o del terzo dal cui potere deriva '
           'quello del titolare, in caso di perdita del possesso o compromissione del dispositivo '
           "di firma, provvedimento dell'autorità, cause limitative della capacità del titolare, o "
           'sospetti abusi/falsificazioni.',
  'testo_integrale': 'g) procedere alla tempestiva pubblicazione della revoca e della sospensione '
                     'del certificato elettronico in caso di richiesta da parte del titolare ((di '
                     'firma elettronica qualificata)) o del terzo dal quale derivino i poteri del '
                     'titolare ((di firma elettronica qualificata)) medesimo, di perdita del '
                     'possesso o della compromissione del dispositivo di firma o degli strumenti '
                     "di autenticazione informatica per l'utilizzo del dispositivo di firma, di "
                     "provvedimento dell'autorita', di acquisizione della conoscenza di cause "
                     "limitative della capacita' del titolare ((di firma elettronica "
                     'qualificata)), di sospetti abusi o falsificazioni, secondo quanto previsto '
                     'dalle ((Linee guida));',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.3 lett.h',
  'testo': 'Garantire un servizio di revoca e sospensione dei certificati sicuro e tempestivo, e '
           'il funzionamento efficiente, puntuale e sicuro degli elenchi dei certificati emessi, '
           'sospesi e revocati.',
  'testo_integrale': 'h) garantire un servizio di revoca e sospensione dei certificati elettronici '
                     "sicuro e tempestivo nonche' garantire il funzionamento efficiente, puntuale "
                     'e sicuro degli elenchi dei certificati di firma emessi, sospesi e revocati;',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.3 lett.i',
  'testo': "Assicurare la precisa determinazione della data e dell'ora di rilascio, revoca e "
           'sospensione dei certificati elettronici.',
  'testo_integrale': "i) assicurare la precisa determinazione della data e dell'ora di rilascio, "
                     'di revoca e di sospensione dei certificati elettronici;',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.3 lett.j',
  'testo': 'Tenere registrazione, anche elettronica, di tutte le informazioni relative al '
           "certificato qualificato dal momento dell'emissione, per almeno venti anni, anche a "
           'fini di prova in eventuali procedimenti giudiziari.',
  'testo_integrale': 'j) tenere registrazione, anche elettronica, di tutte le informazioni '
                     'relative al certificato qualificato dal momento della sua emissione almeno '
                     'per venti anni anche al fine di fornire prova della certificazione in '
                     'eventuali procedimenti giudiziari;',
  'tipo_obbligo': 'di conservazione',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.3 lett.k',
  'testo': 'Non copiare né conservare le chiavi private di firma del soggetto cui è stato fornito '
           'il servizio di certificazione.',
  'testo_integrale': "k) non copiare, ne' conservare, le chiavi private di firma del soggetto cui "
                     'il prestatore di servizi di firma elettronica qualificata ha fornito il '
                     'servizio di certificazione;',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.3 lett.l',
  'testo': 'Predisporre su mezzi di comunicazione durevoli tutte le informazioni utili ai '
           "richiedenti il servizio di certificazione (termini e condizioni d'uso, limitazioni, "
           'accreditamento facoltativo, reclami e risoluzione controversie), in linguaggio chiaro '
           "e prima dell'accordo con il richiedente.",
  'testo_integrale': 'l) predisporre su mezzi di comunicazione durevoli tutte le informazioni '
                     'utili ai soggetti che richiedono il servizio di certificazione, tra cui in '
                     "particolare gli esatti termini e condizioni relative all'uso del "
                     "certificato, compresa ogni limitazione dell'uso, l'esistenza di un sistema "
                     'di accreditamento facoltativo e le procedure di reclamo e di risoluzione '
                     'delle controversie; dette informazioni, che possono essere trasmesse '
                     'elettronicamente, devono essere scritte in linguaggio chiaro ed essere '
                     "fornite prima dell'accordo tra il richiedente il servizio ed il prestatore "
                     'di servizi di firma elettronica qualificata;',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.3 lett.m',
  'testo': 'Utilizzare sistemi affidabili per la gestione del registro dei certificati, garantendo '
           "che solo persone autorizzate possano inserire/modificare dati, che l'autenticità sia "
           'verificabile, che i certificati siano consultabili dal pubblico solo nei casi '
           "consentiti dal titolare, e che l'operatore rilevi eventi che compromettano la "
           'sicurezza; su richiesta, elementi pertinenti possono essere resi accessibili a terzi '
           'che facciano affidamento sul certificato.',
  'testo_integrale': 'm) utilizzare sistemi affidabili per la gestione del registro dei '
                     "certificati con modalita' tali da garantire che soltanto le persone "
                     "autorizzate possano effettuare inserimenti e modifiche, che l'autenticita' "
                     'delle informazioni sia verificabile, che i certificati siano accessibili '
                     'alla consultazione del pubblico soltanto nei casi consentiti dal titolare '
                     "del certificato e che l'operatore possa rendersi conto di qualsiasi evento "
                     'che comprometta i requisiti di sicurezza. Su richiesta, elementi pertinenti '
                     'delle informazioni possono essere resi accessibili a terzi che facciano '
                     'affidamento sul certificato.',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.3 lett.m-bis',
  'testo': 'Garantire il corretto funzionamento e la continuità del sistema e comunicare '
           "immediatamente all'AgID e agli utenti eventuali malfunzionamenti che determinano "
           'disservizio, sospensione o interruzione del servizio.',
  'testo_integrale': "m-bis) garantire il corretto funzionamento e la continuita' del sistema e "
                     'comunicare immediatamente a AgID e agli utenti eventuali malfunzionamenti '
                     'che determinano disservizio, sospensione o interruzione del servizio stesso.',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.4',
  'testo': 'Il prestatore di servizi di firma elettronica qualificata è responsabile '
           "dell'identificazione del soggetto che richiede il certificato qualificato di firma, "
           'anche se tale attività è delegata a terzi.',
  'testo_integrale': "Il prestatore di servizi di firma elettronica qualificata e' responsabile "
                     "dell'identificazione del soggetto che richiede il certificato qualificato di "
                     "firma anche se tale attivita' e' delegata a terzi.",
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32 c.5',
  'testo': 'Il prestatore raccoglie i dati personali direttamente dalla persona interessata o, '
           'previo suo esplicito consenso, tramite terzi, solo nella misura necessaria al rilascio '
           "e mantenimento del certificato, fornendo l'informativa privacy; i dati non possono "
           "essere raccolti o elaborati per fini diversi senza l'espresso consenso "
           "dell'interessato.",
  'testo_integrale': 'Il prestatore di servizi di firma elettronica qualificata raccoglie i dati '
                     'personali direttamente dalla persona cui si riferiscono o, previo suo '
                     'esplicito consenso, tramite il terzo, e soltanto nella misura necessaria al '
                     "rilascio e al mantenimento del certificato, fornendo l'informativa prevista "
                     "dall'articolo 13 del decreto legislativo 30 giugno 2003, n. 196. I dati non "
                     "possono essere raccolti o elaborati per fini diversi senza l'espresso "
                     'consenso della persona cui si riferiscono.',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 32-bis c.1',
  'testo': "L'AgID può irrogare ai prestatori di servizi fiduciari qualificati, ai gestori PEC, ai "
           "gestori dell'identità digitale e ai conservatori affidatari ex art. 34 c.1-bis lett.b, "
           'che abbiano violato gli obblighi del Regolamento eIDAS o del Codice, sanzioni '
           'amministrative da 40.000 a 400.000 euro (da 4.000 a 40.000 euro per i conservatori '
           'affidatari), fermo il risarcimento del maggior danno; le violazioni gravi (rischio per '
           'una pluralità di utenti o carenze infrastrutturali significative) comportano anche '
           "cancellazione dall'elenco e divieto di accreditamento fino a due anni; le sanzioni "
           "sono irrogate dal direttore generale dell'AgID; si applica, in quanto compatibile, la "
           'L. 689/1981.',
  'testo_integrale': "L'AgID puo' irrogare ai prestatori di servizi fiduciari qualificati, ai "
                     "gestori di posta elettronica certificata, ai gestori dell'identita' digitale "
                     "e ai soggetti di cui all'articolo 34, comma 1-bis, lettera b) , che abbiano "
                     'violato gli obblighi del Regolamento eIDAS o del presente Codice relative '
                     'alla prestazione dei predetti servizi, sanzioni amministrative in relazione '
                     "alla gravita' della violazione accertata e all'entita' del danno provocato "
                     "all'utenza, per importi da un minimo di euro 40.000,00 a un massimo di euro "
                     '400.000,00, fermo restando il diritto al risarcimento del maggior danno. Le '
                     "sanzioni per le violazioni commesse dai soggetti di cui all'articolo 34, "
                     'comma 1-bis, lettera b), sono fissate nel minimo in euro 4.000,00 e nel '
                     'massimo in euro 40.000,00. Le violazioni del presente Codice idonee a '
                     "esporre a rischio i diritti e gli interessi di una pluralita' di utenti o "
                     'relative a significative carenze infrastrutturali o di processo del '
                     'fornitore di servizio si considerano gravi. AgID, laddove accerti tali gravi '
                     "violazioni, dispone altresi' la cancellazione del fornitore del servizio "
                     "dall'elenco dei soggetti qualificati e il divieto di accreditamento o "
                     'qualificazione per un periodo fino ad un massimo di due anni. Le sanzioni '
                     "vengono irrogate dal direttore generale dell'AgID ((...)).\n"
                     'Si applica, in quanto compatibile, la disciplina della legge 24 novembre '
                     '1981, n. 689.',
  'tipo_obbligo': 'sanzionatorio',
  'stato': 'vigente',
  'severita': 'grave se rischio pluralità utenti o carenze infrastrutturali significative',
  'sanzioni': 'da 40.000 a 400.000 euro (da 4.000 a 40.000 euro per i soggetti ex art. 34 c.1-bis '
              "lett.b); cancellazione dall'elenco e divieto di accreditamento fino a due anni per "
              'violazioni gravi',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'destinatario'}]},
 {'riferimento': 'art. 32-bis c.1-bis',
  'testo': "L'AgID irroga la sanzione amministrativa di cui al comma 1 e diffida i soggetti a "
           'conformare la propria condotta agli obblighi previsti dalla disciplina vigente.',
  'testo_integrale': "L'AgID irroga la sanzione amministrativa di cui al comma 1 e diffida i "
                     'soggetti a conformare la propria condotta agli obblighi previsti dalla '
                     'disciplina vigente.',
  'tipo_obbligo': 'sanzionatorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 32-bis c.2',
  'testo': 'Salvo i casi di forza maggiore o caso fortuito, in caso di malfunzionamento che '
           'determini interruzione del servizio, o di mancata/intempestiva comunicazione del '
           "disservizio all'AgID o agli utenti ex art. 32 c.3 lett.m-bis, l'AgID, ferme le "
           'sanzioni amministrative, diffida i soggetti a ripristinare la regolarità del servizio '
           "o a effettuare le comunicazioni previste; se l'interruzione o la mancata/intempestiva "
           'comunicazione si ripetono in un biennio dopo la prima diffida, si applica la sanzione '
           "della cancellazione dall'elenco pubblico.",
  'testo_integrale': 'Fatti salvi i casi di forza maggiore o di caso fortuito, qualora si '
                     'verifichi un malfunzionamento nei servizi forniti dai soggetti di cui al '
                     "comma 1 che determini l'interruzione del servizio, ovvero in caso di mancata "
                     'o intempestiva comunicazione dello stesso disservizio a AgID o agli utenti, '
                     "ai sensi dell'articolo 32, comma 3, lettera m-bis), AgID, ferma restando "
                     "l'irrogazione delle sanzioni amministrative, diffida altresi' i soggetti di "
                     "cui al comma 1 a ripristinare la regolarita' del servizio o ad effettuare le "
                     "comunicazioni previste. Se l'interruzione del servizio ovvero la mancata o "
                     'intempestiva comunicazione sono reiterati nel corso di un biennio, '
                     'successivamente alla prima diffida si applica la sanzione della '
                     "cancellazione dall'elenco pubblico.",
  'tipo_obbligo': 'sanzionatorio',
  'stato': 'vigente',
  'condizione_applicabilita': 'malfunzionamento con interruzione del servizio o comunicazione '
                              'mancata/intempestiva del disservizio'},
 {'riferimento': 'art. 32-bis c.3',
  'testo': 'Nei casi di cui ai commi 1, 1-bis e 2 può essere applicata la sanzione amministrativa '
           'accessoria della pubblicazione dei provvedimenti di diffida o di cancellazione, '
           'secondo la legislazione vigente in materia di pubblicità legale.',
  'testo_integrale': "Nei casi di cui ai commi 1, 1-bis; e 2 puo' essere applicata la sanzione "
                     'amministrativa accessoria della pubblicazione dei provvedimenti di diffida o '
                     "di cancellazione secondo la legislazione vigente in materia di pubblicita' "
                     'legale.',
  'tipo_obbligo': 'sanzionatorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 32-bis c.4',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_obbligo': 'sanzionatorio',
  'stato': 'abrogato'},
 {'riferimento': 'art. 34 c.1 lett.a',
  'testo': 'Ai fini della sottoscrizione di documenti informatici di rilevanza esterna, le '
           "pubbliche amministrazioni possono svolgere direttamente l'attività di rilascio dei "
           "certificati qualificati, avendo l'obbligo di qualificarsi ex art. 29; tale attività "
           'può essere svolta solo verso i propri organi e uffici e verso categorie di terzi, '
           'pubblici o privati.',
  'testo_integrale': "a) possono svolgere direttamente l'attivita' di rilascio dei certificati "
                     "qualificati avendo a tale fine l'obbligo di qualificarsi ai sensi "
                     "dell'articolo 29; tale attivita' puo' essere svolta esclusivamente nei "
                     "confronti dei propri organi ed uffici, nonche' di categorie di terzi, "
                     'pubblici o privati. PERIODO SOPPRESSO DAL D.LGS. 26 AGOSTO 2016, N. 179;',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 34 c.1 lett.b',
  'testo': 'Le pubbliche amministrazioni possono rivolgersi a prestatori di servizi di firma '
           'digitale o di altra firma elettronica qualificata, secondo la normativa vigente in '
           'materia di contratti pubblici.',
  'testo_integrale': 'b) possono rivolgersi a prestatori di servizi di firma digitale o di altra '
                     'firma elettronica qualificata, secondo la vigente normativa in materia di '
                     'contratti pubblici.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 34 c.1-bis lett.a',
  'testo': 'Le pubbliche amministrazioni possono procedere alla conservazione dei documenti '
           "informatici all'interno della propria struttura organizzativa.",
  'testo_integrale': "a) all'interno della propria struttura organizzativa;",
  'tipo_obbligo': 'di conservazione',
  'stato': 'vigente'},
 {'riferimento': 'art. 34 c.1-bis lett.b',
  'testo': 'Le pubbliche amministrazioni possono affidare la conservazione dei documenti '
           'informatici, in modo totale o parziale, ad altri soggetti pubblici o privati che '
           'possiedano i requisiti di qualità, sicurezza e organizzazione individuati nelle Linee '
           'guida e in un regolamento AgID sui criteri per la fornitura dei servizi di '
           'conservazione, avuto riguardo alla conformità agli originali e alla qualità/sicurezza '
           'del sistema di conservazione.',
  'testo_integrale': 'b) affidandola, in modo totale o parziale, nel rispetto della disciplina '
                     'vigente, ad altri soggetti, pubblici o privati ((che possiedono i requisiti '
                     "di qualita', di sicurezza e organizzazione individuati, nel rispetto della "
                     "disciplina europea, nelle Linee guida di cui all'art 71 relative alla "
                     "formazione, gestione e conservazione dei documenti informatici nonche' in un "
                     'regolamento sui criteri per la fornitura dei servizi di conservazione dei '
                     "documenti informatici emanato da AgID, avuto riguardo all'esigenza di "
                     "assicurare la conformita' dei documenti conservati agli originali nonche' la "
                     "qualita' e la sicurezza del sistema di conservazione.))",
  'tipo_obbligo': 'di conservazione',
  'stato': 'vigente'},
 {'riferimento': 'art. 34 c.2',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 13 DICEMBRE 2017, N. 217.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'abrogato'},
 {'riferimento': 'art. 34 c.3',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'abrogato'},
 {'riferimento': 'art. 34 c.4',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'abrogato'},
 {'riferimento': 'art. 34 c.5',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'abrogato'},
 {'riferimento': 'art. 35 c.1 lett.a',
  'testo': 'La chiave privata deve essere riservata.',
  'testo_integrale': 'I dispositivi sicuri e le procedure utilizzate per la generazione delle '
                     'firme devono presentare requisiti di sicurezza tali da garantire che la '
                     'chiave privata: a) sia riservata;',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 35 c.1 lett.b',
  'testo': 'La chiave privata non deve poter essere derivata e la relativa firma deve essere '
           'protetta da contraffazioni.',
  'testo_integrale': 'I dispositivi sicuri e le procedure utilizzate per la generazione delle '
                     'firme devono presentare requisiti di sicurezza tali da garantire che la '
                     'chiave privata: b) non possa essere derivata e che la relativa firma sia '
                     'protetta da contraffazioni;',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 35 c.1 lett.c',
  'testo': "La chiave privata deve poter essere sufficientemente protetta dal titolare dall'uso da "
           'parte di terzi.',
  'testo_integrale': 'I dispositivi sicuri e le procedure utilizzate per la generazione delle '
                     'firme devono presentare requisiti di sicurezza tali da garantire che la '
                     'chiave privata: c) possa essere sufficientemente protetta dal titolare '
                     "dall'uso da parte di terzi.",
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 35 c.1-bis',
  'testo': 'Fermo quanto previsto dal comma 1, i dispositivi per la creazione di una firma '
           'elettronica qualificata o di un sigillo elettronico devono soddisfare i requisiti '
           "dell'Allegato II del Regolamento eIDAS.",
  'testo_integrale': '1-bis) Fermo restando quanto previsto dal comma 1, i dispositivi per la '
                     'creazione di una firma elettronica qualificata o di un sigillo elettronico '
                     "soddisfano i requisiti di cui all'Allegato II del Regolamento eIDAS.",
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 35 c.2',
  'testo': "I dispositivi sicuri e le procedure devono garantire l'integrità dei documenti "
           'informatici cui la firma si riferisce; i documenti devono essere presentati al '
           "titolare, prima dell'apposizione della firma, chiaramente e senza ambiguità, e deve "
           'essere richiesta conferma della volontà di generare la firma secondo le Linee guida.',
  'testo_integrale': 'I dispositivi sicuri e le procedure di cui al comma 1 devono garantire '
                     "l'integrita' dei documenti informatici a cui la firma si riferisce. I "
                     'documenti informatici devono essere presentati al titolare ((di firma '
                     "elettronica)), prima dell'apposizione della firma, chiaramente e senza "
                     "ambiguita', e si deve richiedere conferma della volonta' di generare la "
                     'firma secondo quanto previsto dalle ((Linee guida)).',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 35 c.3',
  'testo': 'Il secondo periodo del comma 2 (presentazione del documento e richiesta di conferma) '
           'non si applica alle firme apposte con procedura automatica; la firma con procedura '
           "automatica è valida se apposta previo consenso del titolare all'adozione della "
           'procedura.',
  'testo_integrale': 'Il secondo periodo del comma 2 non si applica alle firme apposte con '
                     "procedura automatica. La firma con procedura automatica e' valida se apposta "
                     "previo consenso del titolare all'adozione della procedura medesima.",
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente',
  'condizione_applicabilita': 'firme apposte con procedura automatica',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 35 c.4',
  'testo': 'I dispositivi sicuri di firma devono essere dotati di certificazione di sicurezza ai '
           'sensi dello schema nazionale di cui al comma 5.',
  'testo_integrale': 'I dispositivi sicuri di firma devono essere dotati di certificazione di '
                     'sicurezza ai sensi dello schema nazionale di cui al comma 5.',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 35 c.5',
  'testo': 'La conformità dei requisiti di sicurezza dei dispositivi per la creazione di firma '
           "elettronica qualificata o sigillo elettronico, prescritti dall'Allegato II eIDAS, è "
           "accertata in Italia dall'Organismo di certificazione della sicurezza informatica "
           'secondo lo schema nazionale di valutazione e certificazione fissato con DPCM, senza '
           'nuovi o maggiori oneri per il bilancio dello Stato; lo schema può prevedere anche '
           'ulteriori criteri europei/internazionali. La valutazione di conformità del sistema e '
           'degli strumenti di autenticazione usati dal titolare delle chiavi è effettuata '
           "dall'AgID secondo proprie linee guida, acquisito il parere obbligatorio dell'Organismo "
           'di certificazione.',
  'testo_integrale': "La conformita' dei requisiti di sicurezza dei dispositivi per la creazione "
                     'di una firma elettronica qualificata o di un sigillo elettronico prescritti '
                     "dall'Allegato II del regolamento eIDAS e' accertata, in Italia, "
                     "dall'Organismo di certificazione della sicurezza informatica in base allo "
                     'schema nazionale per la valutazione e certificazione di sicurezza nel '
                     "settore della tecnologia dell'informazione, fissato con decreto del "
                     'Presidente del Consiglio dei Ministri, o, per sua delega, del Ministro per '
                     "l'innovazione e le tecnologie, di concerto con i Ministri delle "
                     "comunicazioni, delle attivita' produttive e dell'economia e delle finanze. "
                     "L'attuazione dello schema nazionale non deve determinare nuovi o maggiori "
                     "oneri per il bilancio dello Stato. Lo schema nazionale puo' prevedere "
                     "altresi' la valutazione e la certificazione relativamente ad ulteriori "
                     'criteri europei ed internazionali, anche riguardanti altri sistemi e '
                     'prodotti afferenti al settore suddetto.\n'
                     "La valutazione della conformita' del sistema e degli strumenti di "
                     "autenticazione utilizzati dal titolare delle chiavi di firma e' effettuata "
                     "dall'Agenzia per l'Italia digitale in conformita' ad apposite linee guida da "
                     "questa emanate, acquisito il parere obbligatorio dell'Organismo di "
                     'certificazione della sicurezza informatica.',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 36 c.1 lett.a',
  'testo': 'Il certificato qualificato deve essere revocato dal certificatore in caso di '
           "cessazione della sua attività, salvo quanto previsto dall'art. 37 c.2.",
  'testo_integrale': 'Il certificato qualificato deve essere a cura del certificatore: a) revocato '
                     "in caso di cessazione dell'attivita' del certificatore salvo quanto previsto "
                     "dal comma 2 dell'articolo 37;",
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 36 c.1 lett.b',
  'testo': 'Il certificato qualificato deve essere revocato o sospeso dal certificatore in '
           "esecuzione di un provvedimento dell'autorità.",
  'testo_integrale': 'Il certificato qualificato deve essere a cura del certificatore: b) revocato '
                     "o sospeso in esecuzione di un provvedimento dell'autorita';",
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 36 c.1 lett.c',
  'testo': 'Il certificato qualificato deve essere revocato o sospeso dal certificatore su '
           'richiesta del titolare o del terzo dal quale derivano i poteri del titolare, secondo '
           'le modalità del Codice.',
  'testo_integrale': 'Il certificato qualificato deve essere a cura del certificatore: c) revocato '
                     'o sospeso a seguito di richiesta del titolare o del terzo dal quale derivano '
                     "i poteri del titolare, secondo le modalita' previste nel presente codice;",
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 36 c.1 lett.d',
  'testo': 'Il certificato qualificato deve essere revocato o sospeso dal certificatore in '
           'presenza di cause limitative della capacità del titolare o di abusi o falsificazioni.',
  'testo_integrale': 'Il certificato qualificato deve essere a cura del certificatore: d) revocato '
                     "o sospeso in presenza di cause limitative della capacita' del titolare o di "
                     'abusi o falsificazioni.',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 36 c.2',
  'testo': 'Il certificato qualificato può inoltre essere revocato o sospeso dal certificatore nei '
           'casi previsti dalle Linee guida, per violazione delle regole tecniche ivi contenute.',
  'testo_integrale': "Il certificato qualificato puo', inoltre, essere revocato o sospeso nei casi "
                     'previsti dalle ((Linee guida))\n'
                     '((, per violazione delle regole tecniche ivi contenute)).',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 37 c.1',
  'testo': "Il prestatore di servizi fiduciari qualificato che intende cessare l'attività deve, "
           "almeno sessanta giorni prima della cessazione, darne avviso all'AgID e informare senza "
           'indugio i titolari dei certificati emessi, specificando che i certificati non scaduti '
           'al momento della cessazione saranno revocati.',
  'testo_integrale': '((Il prestatore di servizi fiduciari qualificato)) che intende cessare '
                     "l'attivita' deve, almeno sessanta giorni prima della data di cessazione, "
                     'darne avviso al ((AgID)) e informare senza indugio i titolari dei '
                     'certificati da lui emessi specificando che tutti i certificati non scaduti '
                     'al momento della cessazione saranno revocati.',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
               {'categoria': 'Utente/titolare', 'ruolo': 'destinatario'}]},
 {'riferimento': 'art. 37 c.2',
  'testo': "Il prestatore che cessa l'attività comunica contestualmente la rilevazione della "
           "documentazione da parte di altro prestatore o l'annullamento della stessa; "
           "l'indicazione di un prestatore sostitutivo evita la revoca di tutti i certificati non "
           'scaduti al momento della cessazione.',
  'testo_integrale': 'Il ((prestatore)) di cui al comma 1 comunica contestualmente la rilevazione '
                     "della documentazione da parte di altro ((prestatore)) o l'annullamento della "
                     "stessa. L'indicazione di un ((prestatore di servizi fiduciari qualificato)) "
                     'sostitutivo evita la revoca di tutti i certificati non scaduti al momento '
                     'della cessazione.',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 37 c.3',
  'testo': "Il prestatore che cessa l'attività indica altro depositario del registro dei "
           'certificati e della relativa documentazione.',
  'testo_integrale': 'Il ((prestatore)) di cui al comma 1 indica altro depositario del registro '
                     'dei certificati e della relativa documentazione.',
  'tipo_obbligo': 'di conservazione',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 37 c.4',
  'testo': "L'AgID rende nota la data di cessazione dell'attività del prestatore tramite l'elenco "
           "di cui all'art. 29 c.6.",
  'testo_integrale': "Il ((AgID)) rende nota la data di cessazione dell'attivita' del ((prestatore "
                     "di cui al comma 1)) tramite l'elenco di cui all'articolo 29, comma 6.",
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 37 c.4-bis',
  'testo': "Se il prestatore cessa l'attività senza indicare un prestatore sostitutivo e senza "
           'impegnarsi a garantire conservazione e disponibilità della documentazione (art. 33 e '
           'art. 32 c.3 lett.j) e delle ultime liste di revoca emesse, deve depositare presso '
           "l'AgID, che ne garantisce la conservazione e disponibilità.",
  'testo_integrale': "Qualora il ((prestatore di cui al comma 1)) cessi la propria attivita' senza "
                     'indicare, ai sensi del comma 2, ((un prestatore di servizi fiduciari '
                     'qualificato)) sostitutivo e non si impegni a garantire la conservazione e la '
                     "disponibilita' della documentazione prevista dagli articoli 33 e 32, comma "
                     '3, lettera j) e delle ultime liste di revoca emesse, deve provvedere al '
                     'deposito presso ((AgID)) che ne garantisce la conservazione e la '
                     "disponibilita'.",
  'tipo_obbligo': 'di conservazione',
  'stato': 'vigente',
  'condizione_applicabilita': 'cessazione senza prestatore sostitutivo né impegno di conservazione',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 37 c.4-ter',
  'testo': "Se il prestatore non ottempera agli obblighi dell'articolo, l'AgID intima di "
           'ottemperarvi entro un termine non superiore a trenta giorni; in caso di mancata '
           "ottemperanza si applicano le sanzioni dell'art. 32-bis, aumentate fino al doppio.",
  'testo_integrale': '((\n'
                     '4-ter.\n'
                     'Nel caso in cui il prestatore di cui al comma 1 non ottemperi agli obblighi '
                     'previsti dal presente articolo, AgID intima al prestatore di ottemperarvi '
                     'entro un termine non superiore a trenta giorni. In caso di mancata '
                     'ottemperanza entro il suddetto termine, si applicano le sanzioni di cui '
                     "all'articolo 32-bis; le sanzioni pecuniarie previste dal predetto articolo "
                     'sono aumentate fino al doppio.\n'
                     '))',
  'tipo_obbligo': 'sanzionatorio',
  'stato': 'vigente',
  'sanzioni': 'sanzioni ex art. 32-bis aumentate fino al doppio',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'destinatario'}]},
 {'riferimento': 'art. 38 c.1',
  'testo': 'Il trasferimento in via telematica di fondi tra pubbliche amministrazioni e tra queste '
           'e soggetti privati è effettuato secondo le Linee guida, sentiti il Dipartimento della '
           "funzione pubblica, i Ministeri della giustizia e dell'economia e delle finanze, il "
           "Garante per la protezione dei dati personali e la Banca d'Italia.",
  'testo_integrale': 'Il trasferimento in via telematica di fondi tra pubbliche amministrazioni e '
                     "tra queste e soggetti privati e' effettuato secondo le ((Linee guida))\n"
                     '((, sentiti il Dipartimento della funzione pubblica, i Ministeri della '
                     "giustizia e dell'economia e delle finanze, nonche')) il Garante per la "
                     "protezione dei dati personali e la Banca d'Italia.",
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 39 c.1',
  'testo': 'I libri, i repertori e le scritture di cui sia obbligatoria la tenuta, compresi quelli '
           "previsti dalla legge sull'ordinamento del notariato e degli archivi notarili, possono "
           'essere formati e conservati su supporti informatici in conformità al Codice e alle '
           'Linee guida.',
  'testo_integrale': 'I libri, i repertori e le scritture, ivi compresi quelli previsti dalla '
                     "legge sull'ordinamento del notariato e degli archivi notarili, di cui sia "
                     'obbligatoria la tenuta possono essere formati e conservati su supporti '
                     "informatici in conformita' alle disposizioni del presente codice e secondo "
                     'le ((Linee guida)).',
  'tipo_obbligo': 'di conservazione',
  'stato': 'vigente'},
 {'riferimento': 'art. 40 c.1',
  'testo': 'Le pubbliche amministrazioni formano gli originali dei propri documenti, inclusi '
           'quelli relativi ad albi, elenchi e pubblici registri, con mezzi informatici secondo il '
           'Codice e le Linee guida.',
  'testo_integrale': 'Le pubbliche amministrazioni formano gli originali dei propri documenti, '
                     'inclusi quelli inerenti ad albi, elenchi e pubblici registri, con mezzi '
                     'informatici secondo le disposizioni di cui al presente codice e le ((Linee '
                     'guida)).',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 40 c.2',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 30 DICEMBRE 2010, N. 235.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'abrogato'},
 {'riferimento': 'art. 40 c.3',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'abrogato'},
 {'riferimento': 'art. 40 c.4',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'abrogato'},
 {'riferimento': 'art. 40-bis c.1',
  'testo': 'Formano comunque oggetto di registrazione di protocollo ex art. 53 DPR 445/2000 le '
           'comunicazioni che provengono da o sono inviate a domicili digitali eletti ex art. '
           "3-bis, nonché le istanze e dichiarazioni di cui all'art. 65, in conformità alle Linee "
           'guida.',
  'testo_integrale': 'Formano comunque oggetto di registrazione di protocollo ai sensi '
                     "dell'articolo 53 del decreto del Presidente della Repubblica 28 dicembre "
                     '2000, n. 445, le comunicazioni che ((provengono da o sono inviate a domicili '
                     "digitali eletti ai sensi di quanto previsto all'articolo 3-bis,)) nonche' le "
                     "istanze e le dichiarazioni di cui all'articolo 65 in conformita' alle "
                     '((Linee guida)).',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 41 c.1',
  'testo': 'Le pubbliche amministrazioni gestiscono i procedimenti amministrativi utilizzando le '
           "tecnologie dell'informazione e della comunicazione; per ciascun procedimento di "
           'propria competenza forniscono gli opportuni servizi di interoperabilità o integrazione '
           'ai sensi degli artt. 12 e 64-bis.',
  'testo_integrale': 'Le pubbliche amministrazioni gestiscono i procedimenti amministrativi '
                     "utilizzando le tecnologie dell'informazione e della comunicazione. Per "
                     'ciascun procedimento amministrativo di loro competenza, esse forniscono gli '
                     "opportuni servizi di interoperabilita' ((o integrazione)), ai sensi di "
                     'quanto previsto ((dagli articoli 12 e 64-bis)).',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 41 c.1-bis',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_obbligo': 'procedurale',
  'stato': 'abrogato'},
 {'riferimento': 'art. 41 c.2',
  'testo': 'La pubblica amministrazione titolare del procedimento raccoglie in un fascicolo '
           'informatico gli atti, i documenti e i dati del procedimento, da chiunque formati; alla '
           "comunicazione dell'avvio del procedimento ex art. 8 L. 241/1990 comunica agli "
           "interessati le modalità per esercitare in via telematica i diritti di cui all'art. 10 "
           'della medesima legge.',
  'testo_integrale': 'La pubblica amministrazione titolare del procedimento raccoglie in un '
                     'fascicolo informatico gli atti, i documenti e i dati del procedimento '
                     "medesimo da chiunque formati; all'atto della comunicazione dell'avvio del "
                     "procedimento ai sensi dell'articolo 8 della legge 7 agosto 1990, n. 241, "
                     "comunica agli interessati le modalita' per esercitare in via telematica i "
                     "diritti di cui all'articolo 10 della citata legge 7 agosto 1990, n. 241. "
                     '(28)',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 41 c.2-bis',
  'testo': 'Il fascicolo informatico è realizzato garantendo la possibilità di essere direttamente '
           'consultato e alimentato da tutte le amministrazioni coinvolte nel procedimento e dagli '
           'interessati, nei limiti e alle condizioni previste dalla disciplina vigente, '
           'attraverso i servizi ex artt. 40-ter e 64-bis; le Linee guida per costituzione, '
           "identificazione, accessibilità e utilizzo del fascicolo, dettate dall'AgID ex art. 71, "
           'sono conformi ai principi di corretta gestione documentale e alla disciplina di '
           'formazione, gestione, conservazione e trasmissione del documento informatico, incluse '
           'le regole sul protocollo informatico e sul sistema pubblico di connettività, nel '
           'rispetto dei criteri di interoperabilità e integrazione.',
  'testo_integrale': "Il fascicolo informatico e' realizzato garantendo la possibilita' di essere "
                     'direttamente consultato ed alimentato da tutte le amministrazioni coinvolte '
                     'nel procedimento ((e dagli interessati, nei limiti ed alle condizioni '
                     'previste dalla disciplina vigente, attraverso i servizi di cui agli articoli '
                     "40-ter e 64-bis)). ((Le Linee guida)) per la costituzione, l'identificazione "
                     "((, l'accessibilita' attraverso i suddetti servizi)) e l'utilizzo del "
                     "fascicolo ((sono dettate dall'AgID ai sensi dell'articolo 71 e)) sono "
                     'conformi ai principi di una corretta gestione documentale ed alla disciplina '
                     'della formazione, gestione, conservazione e trasmissione del documento '
                     'informatico, ivi comprese le regole concernenti il protocollo informatico ed '
                     "il sistema pubblico di connettivita', e comunque rispettano i criteri "
                     "dell'interoperabilita' e ((dell'integrazione)).",
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente'},
 {'riferimento': 'art. 41 c.2-ter lett.a',
  'testo': "Il fascicolo informatico reca l'indicazione dell'amministrazione titolare del "
           'procedimento, che cura la costituzione e la gestione del fascicolo.',
  'testo_integrale': "Il fascicolo informatico reca l'indicazione: a) dell'amministrazione "
                     'titolare del procedimento, che cura la costituzione e la gestione del '
                     'fascicolo medesimo;',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 41 c.2-ter lett.b',
  'testo': "Il fascicolo informatico reca l'indicazione delle altre amministrazioni partecipanti.",
  'testo_integrale': "Il fascicolo informatico reca l'indicazione: b) delle altre amministrazioni "
                     'partecipanti;',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 41 c.2-ter lett.c',
  'testo': "Il fascicolo informatico reca l'indicazione del responsabile del procedimento.",
  'testo_integrale': "Il fascicolo informatico reca l'indicazione: c) del responsabile del "
                     'procedimento;',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 41 c.2-ter lett.d',
  'testo': "Il fascicolo informatico reca l'indicazione dell'oggetto del procedimento.",
  'testo_integrale': "Il fascicolo informatico reca l'indicazione: d) dell'oggetto del "
                     'procedimento;',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 41 c.2-ter lett.e',
  'testo': "Il fascicolo informatico reca l'indicazione dell'elenco dei documenti contenuti, salvo "
           'quanto disposto dal comma 2-quater.',
  'testo_integrale': "Il fascicolo informatico reca l'indicazione: e) dell'elenco dei documenti "
                     'contenuti, salvo quanto disposto dal comma 2-quater.',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 41 c.2-ter lett.e-bis',
  'testo': "Il fascicolo informatico reca l'indicazione dell'identificativo del fascicolo, apposto "
           "con modalità idonee a consentirne l'indicizzazione e la ricerca attraverso il sistema "
           "di cui all'art. 40-ter nel rispetto delle Linee guida.",
  'testo_integrale': "Il fascicolo informatico reca l'indicazione: e-bis) dell'identificativo del "
                     "fascicolo medesimo ((apposto con modalita' idonee a consentirne "
                     "l'indicizzazione e la ricerca attraverso il sistema di cui all'articolo "
                     '40-ter nel rispetto delle Linee guida)).',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 41 c.2-quater',
  'testo': "Il fascicolo informatico può contenere aree cui hanno accesso solo l'amministrazione "
           'titolare e gli altri soggetti da essa individuati; è formato garantendo corretta '
           'collocazione, facile reperibilità e collegabilità dei singoli documenti, ed è '
           "costituito in modo da garantire l'esercizio in via telematica dei diritti ex L. "
           "241/1990 e art. 5 c.2 D.Lgs. 33/2013, nonché l'immediata conoscibilità, anche tramite "
           'i servizi ex artt. 40-ter e 64-bis, dello stato di avanzamento del procedimento e del '
           "nominativo/recapito elettronico del responsabile; l'AgID detta, ex art. 71, Linee "
           "guida per garantire l'interoperabilità tra i sistemi di gestione dei fascicoli e tali "
           'servizi.',
  'testo_integrale': "Il fascicolo informatico puo' contenere aree a cui hanno accesso solo "
                     "l'amministrazione titolare e gli altri soggetti da essa individuati; esso e' "
                     'formato in modo da garantire la corretta collocazione, la facile '
                     "reperibilita' e la collegabilita', in relazione al contenuto ed alle "
                     "finalita', ((dei singoli documenti. Il fascicolo informatico)) e' inoltre "
                     "costituito in modo da garantire l'esercizio in via telematica dei diritti "
                     "previsti dalla citata legge n. 241 del 1990 ((e dall'articolo 5, comma 2, "
                     "del decreto legislativo 14 marzo 2013, n. 33, nonche' l'immediata "
                     "conoscibilita' anche attraverso i servizi di cui agli articoli 40-ter e "
                     '64-bis, sempre per via telematica, dello stato di avanzamento del '
                     'procedimento, del nominativo e del recapito elettronico del responsabile del '
                     "procedimento. AgID detta, ai sensi dell'articolo 71, Linee guida idonee a "
                     "garantire l'interoperabilita' tra i sistemi di gestione dei fascicoli dei "
                     'procedimenti e i servizi di cui agli articoli 40-ter e 64-bis)).',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 41 c.3',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'abrogato'},
 {'riferimento': 'art. 42 c.1',
  'testo': 'Le pubbliche amministrazioni valutano in termini di costi/benefici il recupero su '
           'supporto informatico dei documenti e atti cartacei di conservazione obbligatoria o '
           'opportuna, e predispongono i conseguenti piani di sostituzione degli archivi cartacei '
           'con archivi informatici, nel rispetto delle Linee guida.',
  'testo_integrale': 'Le pubbliche amministrazioni valutano in termini di rapporto tra costi e '
                     'benefici il recupero su supporto informatico dei documenti e degli atti '
                     'cartacei dei quali sia obbligatoria o opportuna la conservazione e '
                     'provvedono alla predisposizione dei conseguenti piani di sostituzione degli '
                     'archivi cartacei con archivi informatici, nel rispetto delle ((Linee '
                     'guida)).',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 43 c.1-bis',
  'testo': 'Se il documento informatico è conservato per legge da uno dei soggetti ex art. 2 c.2, '
           "cessa l'obbligo di conservazione a carico di cittadini e imprese, che possono "
           'richiedere in ogni momento accesso al documento a tali soggetti; le amministrazioni '
           'rendono disponibili a cittadini e imprese i documenti attraverso servizi on-line '
           'accessibili previa identificazione con identità digitale ex art. 64, integrati con i '
           'servizi ex artt. 40-ter e 64-bis.',
  'testo_integrale': "Se il documento informatico e' conservato per legge da uno dei soggetti di "
                     "cui all'articolo 2, comma 2, cessa l'obbligo di conservazione a carico dei "
                     'cittadini e delle imprese che possono in ogni momento richiedere accesso al '
                     "documento stesso ((ai medesimi soggetti di cui all'articolo 2, comma 2. Le "
                     'amministrazioni rendono disponibili a cittadini ed imprese i predetti '
                     'documenti attraverso servizi on-line accessibili previa identificazione con '
                     "l'identita' digitale di cui all'articolo 64 ed integrati con i servizi di "
                     'cui agli articoli 40-ter e 64-bis)).',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente',
  'condizione_applicabilita': 'documento conservato per legge da un soggetto ex art. 2 c.2'},
 {'riferimento': 'art. 43 c.3',
  'testo': 'I documenti informatici di cui è prescritta la conservazione per legge o regolamento '
           'possono essere archiviati per le esigenze correnti anche con modalità cartacee, ma '
           'sono conservati in modo permanente con modalità digitali, nel rispetto delle Linee '
           'guida.',
  'testo_integrale': "I documenti informatici, di cui e' prescritta la conservazione per legge o "
                     'regolamento, possono essere archiviati per le esigenze correnti anche con '
                     "modalita' cartacee e sono conservati in modo permanente con modalita' "
                     'digitali, nel rispetto delle ((Linee guida)).',
  'tipo_obbligo': 'di conservazione',
  'stato': 'vigente'},
 {'riferimento': 'art. 44 c.1',
  'testo': 'Il sistema di gestione informatica dei documenti delle pubbliche amministrazioni, ex '
           'art. 52 DPR 445/2000, è organizzato e gestito anche in modo da assicurare '
           "l'indicizzazione e la ricerca dei documenti e fascicoli informatici attraverso il "
           "sistema di cui all'art. 40-ter, nel rispetto delle Linee guida.",
  'testo_integrale': 'Il sistema di gestione informatica dei documenti delle pubbliche '
                     "amministrazioni, di cui all'articolo 52 del decreto del Presidente della "
                     "Repubblica 28 dicembre 2000, n. 445, e' organizzato e gestito, anche in modo "
                     "da assicurare l'indicizzazione e la ricerca dei documenti e fascicoli "
                     "informatici attraverso il sistema di cui all'articolo 40-ter nel rispetto "
                     'delle Linee guida.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 44 c.1-bis',
  'testo': 'Il sistema di gestione dei documenti informatici delle pubbliche amministrazioni è '
           "gestito da un responsabile che opera d'intesa con il dirigente dell'ufficio ex art. "
           '17, il responsabile del trattamento dati personali ex art. 29 D.Lgs. 196/2003 ove '
           "nominato, e il responsabile del sistema di conservazione; almeno una volta l'anno il "
           'responsabile della gestione documentale trasmette al sistema di conservazione i '
           'fascicoli e le serie documentarie, anche relative a procedimenti non conclusi.',
  'testo_integrale': 'Il sistema di gestione dei documenti informatici delle pubbliche '
                     "amministrazioni e' gestito da un responsabile che opera d'intesa con il "
                     "dirigente dell'ufficio di cui all'articolo 17 del presente Codice, il "
                     "responsabile del trattamento dei dati personali di cui all'articolo 29 del "
                     'decreto legislativo 30 giugno 2003, n. 196, ove nominato, e con il '
                     'responsabile del sistema della conservazione dei documenti informatici delle '
                     "pubbliche amministrazioni, nella definizione e gestione delle attivita' di "
                     "rispettiva competenza. Almeno una volta all'anno il responsabile della "
                     'gestione dei documenti informatici provvede a trasmettere al sistema di '
                     'conservazione i fascicoli e le serie documentarie anche relative a '
                     'procedimenti non conclusi.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 44 c.1-ter',
  'testo': 'In tutti i casi in cui la legge prescrive obblighi di conservazione, anche a carico di '
           'soggetti privati, il sistema di conservazione dei documenti informatici assicura, per '
           'quanto conservato, autenticità, integrità, affidabilità, leggibilità e reperibilità, '
           'secondo le modalità indicate nelle Linee guida.',
  'testo_integrale': '((In tutti i casi in cui la legge prescrive obblighi di conservazione, anche '
                     'a carico di soggetti privati, il sistema)) di conservazione dei documenti '
                     'informatici assicura, per quanto in esso conservato, caratteristiche di '
                     "autenticita', integrita', affidabilita', leggibilita', reperibilita', "
                     "secondo le modalita' indicate nelle Linee guida.",
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 44 c.1-quater',
  'testo': "Il responsabile della conservazione, d'intesa con i responsabili del trattamento dati, "
           'della sicurezza e dei sistemi informativi, può affidare ex art. 34 c.1-bis lett.b la '
           'conservazione dei documenti informatici ad altri soggetti pubblici o privati con '
           'idonee garanzie organizzative, tecnologiche e di protezione dati; il responsabile '
           "della conservazione della pubblica amministrazione, d'intesa anche con il responsabile "
           'della gestione documentale, effettua la conservazione secondo quanto previsto '
           "dall'art. 34 c.1-bis.",
  'testo_integrale': "Il responsabile della conservazione, che opera d'intesa con il responsabile "
                     'del trattamento dei dati personali, con il responsabile della sicurezza e '
                     "con il responsabile dei sistemi informativi, puo' affidare, ai sensi "
                     "dell'articolo 34, comma 1-bis, lettera b), la conservazione dei documenti "
                     'informatici ad altri soggetti, pubblici o privati, che offrono idonee '
                     'garanzie organizzative, e tecnologiche e di protezione dei dati personali. '
                     'Il responsabile della conservazione della pubblica amministrazione, che '
                     "opera d'intesa, oltre che con i responsabili di cui al comma 1-bis, anche "
                     'con il responsabile della gestione documentale, effettua la conservazione '
                     "dei documenti informatici secondo quanto previsto all'articolo 34, comma "
                     '1-bis.',
  'tipo_obbligo': 'di conservazione',
  'stato': 'vigente'},
 {'riferimento': 'art. 46 c.1',
  'testo': 'Al fine di garantire la riservatezza dei dati sensibili o giudiziari ex art. 4 c.1 '
           'lett.d ed e D.Lgs. 196/2003, i documenti informatici trasmessi ad altre pubbliche '
           'amministrazioni per via digitale possono contenere soltanto i dati sensibili e '
           'giudiziari consentiti da legge o regolamento e indispensabili per il perseguimento '
           'delle finalità per cui sono acquisiti.',
  'testo_integrale': 'Al fine di garantire la riservatezza dei dati sensibili o giudiziari di cui '
                     "all'articolo 4, comma 1, lettere d) ed e), del decreto legislativo 30 giugno "
                     '2003, n. 196, i documenti informatici trasmessi ad altre pubbliche '
                     'amministrazioni per via ((digitale)) possono contenere soltanto ((i dati '
                     'sensibili e giudiziari consentiti)) da legge o da regolamento e '
                     "indispensabili per il perseguimento delle finalita' per le quali sono "
                     'acquisite.',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente'},
 {'riferimento': 'art. 47 c.1',
  'testo': 'Le comunicazioni di documenti tra le pubbliche amministrazioni avvengono mediante '
           'posta elettronica o in cooperazione applicativa; sono valide ai fini del procedimento '
           'amministrativo una volta verificata la provenienza; il documento può anche essere reso '
           'disponibile previa comunicazione delle modalità di accesso telematico.',
  'testo_integrale': 'Le comunicazioni di documenti tra le pubbliche amministrazioni avvengono '
                     "mediante l'utilizzo della posta elettronica o in cooperazione applicativa; "
                     'esse sono valide ai fini del procedimento amministrativo una volta che ne '
                     "sia verificata la provenienza. Il documento puo' essere, altresi', reso "
                     "disponibile previa comunicazione delle modalita' di accesso telematico allo "
                     'stesso.',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 47 c.1-bis',
  'testo': "L'inosservanza della disposizione del comma 1, ferma restando l'eventuale "
           'responsabilità per danno erariale, comporta responsabilità dirigenziale e '
           'responsabilità disciplinare.',
  'testo_integrale': "L'inosservanza della disposizione di cui al comma 1, ferma restando "
                     "l'eventuale responsabilita' per danno erariale, comporta responsabilita' "
                     "dirigenziale e responsabilita' disciplinare.",
  'tipo_obbligo': 'sanzionatorio',
  'stato': 'vigente',
  'sanzioni': 'responsabilità dirigenziale, disciplinare ed eventuale responsabilità per danno '
              'erariale'},
 {'riferimento': 'art. 47 c.2 lett.a',
  'testo': 'Ai fini della verifica della provenienza, le comunicazioni tra pubbliche '
           'amministrazioni sono valide se sottoscritte con firma digitale o altro tipo di firma '
           'elettronica qualificata.',
  'testo_integrale': 'Ai fini della verifica della provenienza le comunicazioni sono valide se: a) '
                     'sono sottoscritte con firma digitale o altro tipo di firma elettronica '
                     'qualificata;',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 47 c.2 lett.b',
  'testo': 'Ai fini della verifica della provenienza, le comunicazioni sono valide se dotate di '
           'segnatura di protocollo ex art. 55 DPR 445/2000.',
  'testo_integrale': 'Ai fini della verifica della provenienza le comunicazioni sono valide se: b) '
                     "ovvero sono dotate di segnatura di protocollo di cui all'articolo 55 del "
                     'decreto del Presidente della Repubblica 28 dicembre 2000, n. 445;',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 47 c.2 lett.c',
  'testo': 'Ai fini della verifica della provenienza, le comunicazioni sono valide se è comunque '
           'possibile accertarne altrimenti la provenienza secondo la normativa vigente o le Linee '
           'guida; è in ogni caso esclusa la trasmissione di documenti a mezzo fax.',
  'testo_integrale': 'Ai fini della verifica della provenienza le comunicazioni sono valide se: c) '
                     "ovvero e' comunque possibile accertarne altrimenti la provenienza, secondo "
                     "quanto previsto dalla normativa vigente o dalle ((Linee guida)). E' in ogni "
                     'caso esclusa la trasmissione di documenti a mezzo fax;',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 47 c.2 lett.d',
  'testo': 'Ai fini della verifica della provenienza, le comunicazioni sono valide se trasmesse '
           'attraverso sistemi di posta elettronica certificata ex DPR 68/2005.',
  'testo_integrale': 'Ai fini della verifica della provenienza le comunicazioni sono valide se: d) '
                     'ovvero trasmesse attraverso sistemi di posta elettronica certificata di cui '
                     'al decreto del Presidente della Repubblica 11 febbraio 2005, n. 68.',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 47 c.3',
  'testo': "I soggetti ex art. 2 c.2 lett.a e b provvedono a istituire e pubblicare nell'Indice "
           'dei domicili digitali delle pubbliche amministrazioni e dei gestori di pubblici '
           'servizi almeno una casella PEC per ciascun registro di protocollo; le pubbliche '
           'amministrazioni utilizzano per le comunicazioni con i propri dipendenti la posta '
           'elettronica o altri strumenti informatici, nel rispetto della disciplina protezione '
           'dati personali e previa informativa agli interessati sul grado di riservatezza degli '
           'strumenti utilizzati.',
  'testo_integrale': "((I soggetti di cui all'articolo 2, comma 2, lettere a) e b),)) provvedono "
                     "ad istituire e pubblicare ((nell'Indice dei domicili digitali delle "
                     'pubbliche amministrazioni e dei gestori di pubblici servizi)) almeno una '
                     'casella di posta elettronica certificata per ciascun registro di protocollo. '
                     '((Le pubbliche amministrazioni)) utilizzano per le comunicazioni tra '
                     "l'amministrazione ed i propri dipendenti la posta elettronica o altri "
                     'strumenti informatici di comunicazione nel rispetto delle norme in materia '
                     'di protezione dei dati personali e previa informativa agli interessati in '
                     'merito al grado di riservatezza degli strumenti utilizzati.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'}]

RIGHE_PRINCIPI = [{'riferimento': 'art. 29 c.4',
  'testo': 'La domanda di qualificazione si considera accolta per silenzio-assenso se il '
           "provvedimento di diniego non viene comunicato all'interessato entro novanta giorni "
           'dalla presentazione.',
  'testo_integrale': 'La domanda di qualificazione ((...)) si considera accolta qualora non venga '
                     "comunicato all'interessato il provvedimento di diniego entro novanta giorni "
                     'dalla data di presentazione della stessa.',
  'tipo_principio': 'presunzione legale',
  'stato': 'vigente'},
 {'riferimento': 'art. 29 c.9',
  'testo': "Alle attività previste dall'articolo si provvede nell'ambito delle risorse dell'AgID, "
           'senza nuovi o maggiori oneri per la finanza pubblica.',
  'testo_integrale': "Alle attivita' previste dal presente articolo si fa fronte nell'ambito delle "
                     'risorse del AgID, senza nuovi o maggiori oneri per la finanza pubblica.',
  'tipo_principio': 'altro',
  'stato': 'vigente'},
 {'riferimento': 'art. 30 c.3',
  'testo': 'Il prestatore di servizi di firma digitale o di altra firma elettronica qualificata '
           "non è responsabile dei danni derivanti dall'uso di un certificato qualificato che "
           "ecceda i limiti eventualmente posti ai sensi dell'art. 28 c.3, a condizione che i "
           "limiti d'uso e di valore siano chiaramente riconoscibili secondo l'art. 28 c.3-bis (il "
           'primo periodo del comma è stato soppresso dal D.Lgs. 217/2017).',
  'testo_integrale': 'PERIODO SOPPRESSO DAL D.LGS. 13 DICEMBRE 2017, N. 217. Il prestatore di '
                     "servizi di firma digitale o di altra firma elettronica qualificata non e' "
                     "responsabile dei danni derivanti dall'uso di un certificato qualificato che "
                     "ecceda i limiti eventualmente posti dallo stesso ai sensi dell'articolo 28, "
                     "comma 3, a condizione che limiti d'uso e di valore siano chiaramente "
                     "riconoscibili secondo quanto previsto dall'articolo 28, comma 3-bis.",
  'tipo_principio': 'altro',
  'stato': 'vigente'},
 {'riferimento': 'art. 31',
  'testo': 'Articolo abrogato dal D.Lgs. 26 agosto 2016, n. 179.',
  'testo_integrale': '((ARTICOLO ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179))',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 33',
  'testo': 'Articolo abrogato dal D.Lgs. 13 dicembre 2017, n. 217.',
  'testo_integrale': '((ARTICOLO ABROGATO DAL D.LGS. 13 DICEMBRE 2017, N. 217))',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 35 c.6',
  'testo': 'La conformità di cui al comma 5 è riconosciuta anche se accertata da un organismo '
           'designato da un altro Stato membro e notificato ex art. 30 §2 Regolamento eIDAS; ove '
           'previsto da tale organismo, la valutazione di conformità del sistema e degli strumenti '
           "di autenticazione è effettuata dall'AgID secondo le linee guida di cui al comma 5.",
  'testo_integrale': "La conformita' di cui al comma 5 e' inoltre riconosciuta se accertata da un "
                     "organismo all'uopo designato da un altro Stato membro e notificato ai sensi "
                     "dell'articolo 30, comma 2, del Regolamento eIDAS. Ove previsto "
                     "dall'organismo di cui al periodo precedente, la valutazione della "
                     "conformita' del sistema e degli strumenti di autenticazione utilizzati dal "
                     "titolare delle chiavi di firma e' effettuata dall'AgID in conformita' alle "
                     'linee guida di cui al comma 5.',
  'tipo_principio': 'equivalenza giuridica',
  'stato': 'vigente'},
 {'riferimento': 'art. 36 c.3',
  'testo': 'La revoca o la sospensione del certificato qualificato, qualunque ne sia la causa, ha '
           'effetto dal momento della pubblicazione della lista che lo contiene; il momento della '
           'pubblicazione deve essere attestato mediante adeguato riferimento temporale.',
  'testo_integrale': 'La revoca o la sospensione del certificato qualificato, qualunque ne sia la '
                     'causa, ha effetto dal momento della pubblicazione della lista che lo '
                     'contiene. Il momento della pubblicazione deve essere attestato mediante '
                     'adeguato riferimento temporale.',
  'tipo_principio': 'altro',
  'stato': 'vigente'},
 {'riferimento': 'art. 36 c.4',
  'testo': 'Le modalità di revoca o sospensione dei certificati qualificati sono previste nelle '
           'Linee guida.',
  'testo_integrale': "Le modalita' di revoca o sospensione sono previste nelle ((Linee guida)).",
  'tipo_principio': 'altro',
  'stato': 'vigente'},
 {'riferimento': 'art. 40-ter c.1',
  'testo': 'La Presidenza del Consiglio dei ministri promuove lo sviluppo e la sperimentazione di '
           'un sistema pubblico di ricerca documentale, volto a facilitare la ricerca dei '
           'documenti soggetti a obblighi di pubblicità legale, trasparenza o registrazione di '
           "protocollo ex art. 53 DPR 445/2000, dell'art. 40-bis e dei fascicoli dei procedimenti "
           "ex art. 41, e a consentirne l'accesso on-line agli aventi diritto.",
  'testo_integrale': '((\n'
                     '1.\n'
                     'La Presidenza del Consiglio dei ministri promuove lo sviluppo e la '
                     'sperimentazione di un sistema volto a facilitare la ricerca dei documenti '
                     "soggetti a obblighi di pubblicita' legale, trasparenza o a registrazione di "
                     "protocollo ai sensi dell'articolo 53 del decreto del Presidente della "
                     "Repubblica 28 dicembre 2000, n. 445, e di cui all'articolo 40-bis e dei "
                     "fascicoli dei procedimenti di cui all'articolo 41, nonche' a consentirne "
                     "l'accesso on-line ai soggetti che ne abbiano diritto ai sensi della "
                     'disciplina vigente.\n'
                     '))',
  'tipo_principio': 'scopo/ambito di applicazione',
  'stato': 'vigente'},
 {'riferimento': 'art. 43 c.1',
  'testo': 'Gli obblighi di conservazione e di esibizione di documenti si intendono soddisfatti a '
           'tutti gli effetti di legge mediante documenti informatici, se le relative procedure '
           'garantiscono la conformità ai documenti originali e sono conformi alle Linee guida.',
  'testo_integrale': '((\n'
                     '1.\n'
                     'Gli obblighi di conservazione e di esibizione di documenti si intendono '
                     'soddisfatti a tutti gli effetti di legge a mezzo di documenti informatici, '
                     'se le relative procedure sono effettuate in modo tale da garantire la '
                     "conformita' ai documenti originali e sono conformi alle Linee guida.\n"
                     '))',
  'tipo_principio': 'equivalenza giuridica',
  'stato': 'vigente'},
 {'riferimento': 'art. 43 c.2',
  'testo': 'Restano validi i documenti degli archivi, le scritture contabili, la corrispondenza e '
           'ogni atto, dato o documento già conservati mediante riproduzione su supporto '
           'fotografico, ottico o altro processo idoneo a garantirne la conformità agli originali, '
           "secondo la disciplina vigente al momento dell'invio nel sistema di conservazione.",
  'testo_integrale': 'Restano validi i documenti degli archivi, le scritture contabili, la '
                     "corrispondenza ed ogni atto, dato o documento gia' conservati mediante "
                     'riproduzione su supporto fotografico, su supporto ottico o con altro '
                     "processo idoneo a garantire la conformita' dei documenti agli originali ((ai "
                     "sensi della disciplina vigente al momento dell'invio dei singoli documenti "
                     'nel sistema di conservazione)).',
  'tipo_principio': 'altro',
  'stato': 'vigente'},
 {'riferimento': 'art. 43 c.4',
  'testo': 'Sono fatti salvi i poteri di controllo del Ministero per i beni e le attività '
           'culturali sugli archivi delle pubbliche amministrazioni e sugli archivi privati '
           'dichiarati di notevole interesse storico ex D.Lgs. 42/2004.',
  'testo_integrale': 'Sono fatti salvi i poteri di controllo del Ministero per i beni e le '
                     "attivita' culturali sugli archivi delle pubbliche amministrazioni e sugli "
                     'archivi privati dichiarati di notevole interesse storico ai sensi delle '
                     'disposizioni del decreto legislativo 22 gennaio 2004, n. 42.',
  'tipo_principio': 'altro',
  'stato': 'vigente'},
 {'riferimento': 'art. 44-bis',
  'testo': 'Articolo abrogato dal D.Lgs. 13 dicembre 2017, n. 217.',
  'testo_integrale': '((ARTICOLO ABROGATO DAL D.LGS. 13 DICEMBRE 2017, N. 217))\n((29))',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 45 c.1',
  'testo': 'I documenti trasmessi da chiunque a una pubblica amministrazione con qualsiasi mezzo '
           'telematico o informatico idoneo ad accertarne la provenienza soddisfano il requisito '
           'della forma scritta e la loro trasmissione non deve essere seguita da quella del '
           'documento originale.',
  'testo_integrale': 'I documenti trasmessi da chiunque ad una pubblica amministrazione con '
                     'qualsiasi mezzo telematico o informatico, idoneo ad accertarne la ((...)) '
                     'provenienza, soddisfano il requisito della forma scritta e la loro '
                     'trasmissione non deve essere seguita da quella del documento originale. (28)',
  'tipo_principio': 'equivalenza giuridica',
  'stato': 'vigente'},
 {'riferimento': 'art. 45 c.2',
  'testo': 'Il documento informatico trasmesso per via telematica si intende spedito dal mittente '
           'se inviato al proprio gestore, e si intende consegnato al destinatario se reso '
           "disponibile all'indirizzo elettronico da questi dichiarato, nella casella di posta "
           'elettronica del destinatario messa a disposizione dal gestore.',
  'testo_integrale': 'Il documento informatico trasmesso per via telematica si intende spedito dal '
                     'mittente se inviato al proprio gestore, e si intende consegnato al '
                     "destinatario se reso disponibile all'indirizzo elettronico da questi "
                     'dichiarato, nella casella di posta elettronica del destinatario messa a '
                     'disposizione dal gestore.',
  'tipo_principio': 'presunzione legale',
  'stato': 'vigente'}]

INDICE_ARTICOLI_LOCALE = ['art. 29 c.1',
 'art. 29 c.2',
 'art. 29 c.3',
 'art. 29 c.4',
 'art. 29 c.5',
 'art. 29 c.6',
 'art. 29 c.7',
 'art. 29 c.8',
 'art. 29 c.9',
 'art. 30 c.1',
 'art. 30 c.2',
 'art. 30 c.3',
 'art. 31',
 'art. 32 c.1',
 'art. 32 c.2',
 'art. 32 c.3 lett.a',
 'art. 32 c.3 lett.b',
 'art. 32 c.3 lett.c',
 'art. 32 c.3 lett.d',
 'art. 32 c.3 lett.e',
 'art. 32 c.3 lett.f',
 'art. 32 c.3 lett.g',
 'art. 32 c.3 lett.h',
 'art. 32 c.3 lett.i',
 'art. 32 c.3 lett.j',
 'art. 32 c.3 lett.k',
 'art. 32 c.3 lett.l',
 'art. 32 c.3 lett.m',
 'art. 32 c.3 lett.m-bis',
 'art. 32 c.4',
 'art. 32 c.5',
 'art. 32-bis c.1',
 'art. 32-bis c.1-bis',
 'art. 32-bis c.2',
 'art. 32-bis c.3',
 'art. 32-bis c.4',
 'art. 33',
 'art. 34 c.1 lett.a',
 'art. 34 c.1 lett.b',
 'art. 34 c.1-bis lett.a',
 'art. 34 c.1-bis lett.b',
 'art. 34 c.2',
 'art. 34 c.3',
 'art. 34 c.4',
 'art. 34 c.5',
 'art. 35 c.1 lett.a',
 'art. 35 c.1 lett.b',
 'art. 35 c.1 lett.c',
 'art. 35 c.1-bis',
 'art. 35 c.2',
 'art. 35 c.3',
 'art. 35 c.4',
 'art. 35 c.5',
 'art. 35 c.6',
 'art. 36 c.1 lett.a',
 'art. 36 c.1 lett.b',
 'art. 36 c.1 lett.c',
 'art. 36 c.1 lett.d',
 'art. 36 c.2',
 'art. 36 c.3',
 'art. 36 c.4',
 'art. 37 c.1',
 'art. 37 c.2',
 'art. 37 c.3',
 'art. 37 c.4',
 'art. 37 c.4-bis',
 'art. 37 c.4-ter',
 'art. 38 c.1',
 'art. 39 c.1',
 'art. 40 c.1',
 'art. 40 c.2',
 'art. 40 c.3',
 'art. 40 c.4',
 'art. 40-bis c.1',
 'art. 40-ter c.1',
 'art. 41 c.1',
 'art. 41 c.1-bis',
 'art. 41 c.2',
 'art. 41 c.2-bis',
 'art. 41 c.2-ter lett.a',
 'art. 41 c.2-ter lett.b',
 'art. 41 c.2-ter lett.c',
 'art. 41 c.2-ter lett.d',
 'art. 41 c.2-ter lett.e',
 'art. 41 c.2-ter lett.e-bis',
 'art. 41 c.2-quater',
 'art. 41 c.3',
 'art. 42 c.1',
 'art. 43 c.1',
 'art. 43 c.1-bis',
 'art. 43 c.2',
 'art. 43 c.3',
 'art. 43 c.4',
 'art. 44 c.1',
 'art. 44 c.1-bis',
 'art. 44 c.1-ter',
 'art. 44 c.1-quater',
 'art. 44-bis',
 'art. 45 c.1',
 'art. 45 c.2',
 'art. 46 c.1',
 'art. 47 c.1',
 'art. 47 c.1-bis',
 'art. 47 c.2 lett.a',
 'art. 47 c.2 lett.b',
 'art. 47 c.2 lett.c',
 'art. 47 c.2 lett.d',
 'art. 47 c.3']

MAPPATURA_LOCALE = {'art. 29 c.1': ['art. 29 c.1'],
 'art. 29 c.2': ['art. 29 c.2'],
 'art. 29 c.3': ['art. 29 c.3'],
 'art. 29 c.4': ['art. 29 c.4'],
 'art. 29 c.5': ['art. 29 c.5'],
 'art. 29 c.6': ['art. 29 c.6'],
 'art. 29 c.7': ['art. 29 c.7'],
 'art. 29 c.8': ['art. 29 c.8'],
 'art. 29 c.9': ['art. 29 c.9'],
 'art. 30 c.1': ['art. 30 c.1'],
 'art. 30 c.2': ['art. 30 c.2'],
 'art. 30 c.3': ['art. 30 c.3'],
 'art. 31': ['art. 31'],
 'art. 32 c.1': ['art. 32 c.1'],
 'art. 32 c.2': ['art. 32 c.2'],
 'art. 32 c.3 lett.a': ['art. 32 c.3 lett.a'],
 'art. 32 c.3 lett.b': ['art. 32 c.3 lett.b'],
 'art. 32 c.3 lett.c': ['art. 32 c.3 lett.c'],
 'art. 32 c.3 lett.d': ['art. 32 c.3 lett.d'],
 'art. 32 c.3 lett.e': ['art. 32 c.3 lett.e'],
 'art. 32 c.3 lett.f': ['art. 32 c.3 lett.f'],
 'art. 32 c.3 lett.g': ['art. 32 c.3 lett.g'],
 'art. 32 c.3 lett.h': ['art. 32 c.3 lett.h'],
 'art. 32 c.3 lett.i': ['art. 32 c.3 lett.i'],
 'art. 32 c.3 lett.j': ['art. 32 c.3 lett.j'],
 'art. 32 c.3 lett.k': ['art. 32 c.3 lett.k'],
 'art. 32 c.3 lett.l': ['art. 32 c.3 lett.l'],
 'art. 32 c.3 lett.m': ['art. 32 c.3 lett.m'],
 'art. 32 c.3 lett.m-bis': ['art. 32 c.3 lett.m-bis'],
 'art. 32 c.4': ['art. 32 c.4'],
 'art. 32 c.5': ['art. 32 c.5'],
 'art. 32-bis c.1': ['art. 32-bis c.1'],
 'art. 32-bis c.1-bis': ['art. 32-bis c.1-bis'],
 'art. 32-bis c.2': ['art. 32-bis c.2'],
 'art. 32-bis c.3': ['art. 32-bis c.3'],
 'art. 32-bis c.4': ['art. 32-bis c.4'],
 'art. 33': ['art. 33'],
 'art. 34 c.1 lett.a': ['art. 34 c.1 lett.a'],
 'art. 34 c.1 lett.b': ['art. 34 c.1 lett.b'],
 'art. 34 c.1-bis lett.a': ['art. 34 c.1-bis lett.a'],
 'art. 34 c.1-bis lett.b': ['art. 34 c.1-bis lett.b'],
 'art. 34 c.2': ['art. 34 c.2'],
 'art. 34 c.3': ['art. 34 c.3'],
 'art. 34 c.4': ['art. 34 c.4'],
 'art. 34 c.5': ['art. 34 c.5'],
 'art. 35 c.1 lett.a': ['art. 35 c.1 lett.a'],
 'art. 35 c.1 lett.b': ['art. 35 c.1 lett.b'],
 'art. 35 c.1 lett.c': ['art. 35 c.1 lett.c'],
 'art. 35 c.1-bis': ['art. 35 c.1-bis'],
 'art. 35 c.2': ['art. 35 c.2'],
 'art. 35 c.3': ['art. 35 c.3'],
 'art. 35 c.4': ['art. 35 c.4'],
 'art. 35 c.5': ['art. 35 c.5'],
 'art. 35 c.6': ['art. 35 c.6'],
 'art. 36 c.1 lett.a': ['art. 36 c.1 lett.a'],
 'art. 36 c.1 lett.b': ['art. 36 c.1 lett.b'],
 'art. 36 c.1 lett.c': ['art. 36 c.1 lett.c'],
 'art. 36 c.1 lett.d': ['art. 36 c.1 lett.d'],
 'art. 36 c.2': ['art. 36 c.2'],
 'art. 36 c.3': ['art. 36 c.3'],
 'art. 36 c.4': ['art. 36 c.4'],
 'art. 37 c.1': ['art. 37 c.1'],
 'art. 37 c.2': ['art. 37 c.2'],
 'art. 37 c.3': ['art. 37 c.3'],
 'art. 37 c.4': ['art. 37 c.4'],
 'art. 37 c.4-bis': ['art. 37 c.4-bis'],
 'art. 37 c.4-ter': ['art. 37 c.4-ter'],
 'art. 38 c.1': ['art. 38 c.1'],
 'art. 39 c.1': ['art. 39 c.1'],
 'art. 40 c.1': ['art. 40 c.1'],
 'art. 40 c.2': ['art. 40 c.2'],
 'art. 40 c.3': ['art. 40 c.3'],
 'art. 40 c.4': ['art. 40 c.4'],
 'art. 40-bis c.1': ['art. 40-bis c.1'],
 'art. 40-ter c.1': ['art. 40-ter c.1'],
 'art. 41 c.1': ['art. 41 c.1'],
 'art. 41 c.1-bis': ['art. 41 c.1-bis'],
 'art. 41 c.2': ['art. 41 c.2'],
 'art. 41 c.2-bis': ['art. 41 c.2-bis'],
 'art. 41 c.2-ter lett.a': ['art. 41 c.2-ter lett.a'],
 'art. 41 c.2-ter lett.b': ['art. 41 c.2-ter lett.b'],
 'art. 41 c.2-ter lett.c': ['art. 41 c.2-ter lett.c'],
 'art. 41 c.2-ter lett.d': ['art. 41 c.2-ter lett.d'],
 'art. 41 c.2-ter lett.e': ['art. 41 c.2-ter lett.e'],
 'art. 41 c.2-ter lett.e-bis': ['art. 41 c.2-ter lett.e-bis'],
 'art. 41 c.2-quater': ['art. 41 c.2-quater'],
 'art. 41 c.3': ['art. 41 c.3'],
 'art. 42 c.1': ['art. 42 c.1'],
 'art. 43 c.1': ['art. 43 c.1'],
 'art. 43 c.1-bis': ['art. 43 c.1-bis'],
 'art. 43 c.2': ['art. 43 c.2'],
 'art. 43 c.3': ['art. 43 c.3'],
 'art. 43 c.4': ['art. 43 c.4'],
 'art. 44 c.1': ['art. 44 c.1'],
 'art. 44 c.1-bis': ['art. 44 c.1-bis'],
 'art. 44 c.1-ter': ['art. 44 c.1-ter'],
 'art. 44 c.1-quater': ['art. 44 c.1-quater'],
 'art. 44-bis': ['art. 44-bis'],
 'art. 45 c.1': ['art. 45 c.1'],
 'art. 45 c.2': ['art. 45 c.2'],
 'art. 46 c.1': ['art. 46 c.1'],
 'art. 47 c.1': ['art. 47 c.1'],
 'art. 47 c.1-bis': ['art. 47 c.1-bis'],
 'art. 47 c.2 lett.a': ['art. 47 c.2 lett.a'],
 'art. 47 c.2 lett.b': ['art. 47 c.2 lett.b'],
 'art. 47 c.2 lett.c': ['art. 47 c.2 lett.c'],
 'art. 47 c.2 lett.d': ['art. 47 c.2 lett.d'],
 'art. 47 c.3': ['art. 47 c.3']}

RELAZIONI = [{'nodo_da': ('obbligo', None, 'art. 36 c.1 lett.a'),
  'nodo_a': ('obbligo', None, 'art. 37 c.2'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.9},
 {'nodo_da': ('obbligo', None, 'art. 32-bis c.1'),
  'nodo_a': ('obbligo', None, 'art. 34 c.1-bis lett.b'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.85},
 {'nodo_da': ('obbligo', None, 'art. 32-bis c.2'),
  'nodo_a': ('obbligo', None, 'art. 32 c.3 lett.m-bis'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.9},
 {'nodo_da': ('obbligo', None, 'art. 37 c.4-ter'),
  'nodo_a': ('obbligo', None, 'art. 32-bis c.1'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.85},
 {'nodo_da': ('obbligo', None, 'art. 37 c.4-bis'),
  'nodo_a': ('principio', None, 'art. 33'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.7},
 {'nodo_da': ('obbligo', None, 'art. 37 c.4-bis'),
  'nodo_a': ('obbligo', None, 'art. 32 c.3 lett.j'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.8},
 {'nodo_da': ('obbligo', None, 'art. 44 c.1-quater'),
  'nodo_a': ('obbligo', None, 'art. 34 c.1-bis lett.b'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.85},
 {'nodo_da': ('obbligo', None, 'art. 41 c.2-ter lett.e'),
  'nodo_a': ('obbligo', None, 'art. 41 c.2-quater'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.85},
 {'nodo_da': ('obbligo', None, 'art. 32-bis c.3'),
  'nodo_a': ('obbligo', None, 'art. 32-bis c.1'),
  'tipo_relazione': 'si applica a',
  'evidence_type': 'textual',
  'confidence': 0.7},
 {'nodo_da': ('obbligo', None, 'art. 47 c.1-bis'),
  'nodo_a': ('obbligo', None, 'art. 47 c.1'),
  'tipo_relazione': 'sanziona',
  'evidence_type': 'textual',
  'confidence': 0.8},
 {'nodo_da': ('obbligo', None, 'art. 32-bis c.1'),
  'nodo_a': ('obbligo', None, 'art. 37 c.1'),
  'tipo_relazione': 'sanziona',
  'evidence_type': 'textual',
  'confidence': 0.6}]
