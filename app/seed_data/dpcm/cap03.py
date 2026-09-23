"""Estrazione granulare DPCM 22 febbraio 2013 - Titolo II parte 2 (artt. 15-31): informazioni
riguardanti i certificatori, comunicazione tra certificatore e Agenzia, generazione e uso delle
chiavi del certificatore, generazione dei certificati qualificati, informazioni contenute nei
certificati, revoca e sospensione del certificato qualificato in tutte le sue varianti (iniziativa
del certificatore, richiesta del titolare, richiesta del terzo interessato), codice di emergenza,
sostituzione e revoca delle chiavi di certificazione.

Testo ufficiale vigente al 17/09/2026, fonte app/.source_cache/dpcm/cap03.txt (ADR-0007).
Modulo generato secondo il contratto di app/seed_data/lib.py: nessun discrimine di rilevanza,
copertura completa comma/lettera per comma/lettera. Le relazioni (RELAZIONI) sono limitate a
rinvii interni al presente capitolo (fonte_id_o_None sempre None); i rinvii al Codice (CAD) e ad
altri capitoli del DPCM (es. artt. 35, 40, 43) sono cross-fonte/cross-capitolo e restano fuori
scope di questo import.
"""

RIGHE_OBBLIGHI = [{'riferimento': 'art. 15 c.1 lett.a)',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Il certificatore che rilascia al pubblico certificati qualificati fornisce '
           "all'Agenzia i propri dati anagrafici ovvero la denominazione o ragione sociale.",
  'testo_integrale': 'I certificatori che rilasciano al pubblico certificati qualificati ai '
                     "sensi del Codice forniscono all'Agenzia le seguenti informazioni e "
                     'documenti a loro relativi: a) dati anagrafici ovvero denominazione o '
                     'ragione sociale;',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 15 c.1 lett.b)',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "Il certificatore fornisce all'Agenzia la propria residenza ovvero sede legale.",
  'testo_integrale': 'b) residenza ovvero sede legale;',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 15 c.1 lett.c)',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "Il certificatore fornisce all'Agenzia l'elenco delle proprie sedi operative.",
  'testo_integrale': 'c) sedi operative;',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 15 c.1 lett.d)',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "Il certificatore fornisce all'Agenzia il nominativo del proprio rappresentante "
           'legale.',
  'testo_integrale': 'd) rappresentante legale;',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 15 c.1 lett.e)',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "Il certificatore fornisce all'Agenzia i certificati delle proprie chiavi di "
           'certificazione.',
  'testo_integrale': 'e) certificati delle chiavi di certificazione;',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 15 c.1 lett.f)',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "Il certificatore fornisce all'Agenzia il proprio piano per la sicurezza.",
  'testo_integrale': "f) piano per la sicurezza di cui all'art. 35;",
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 15 c.1 lett.g)',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "Il certificatore fornisce all'Agenzia il proprio manuale operativo.",
  'testo_integrale': "g) manuale operativo di cui all'art. 40;",
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 15 c.1 lett.h)',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "Il certificatore fornisce all'Agenzia una relazione sulla propria struttura "
           'organizzativa.',
  'testo_integrale': 'h) relazione sulla struttura organizzativa;',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 15 c.1 lett.i)',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "Il certificatore fornisce all'Agenzia copia di una polizza assicurativa a copertura "
           'dei rischi della propria attività e dei danni causati a terzi.',
  'testo_integrale': "i) copia di una polizza assicurativa a copertura dei rischi dell'attività "
                     'e dei danni causati a terzi.',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 15 c.2',
  'soggetti': [{'categoria': 'Terzi affidanti/pubblico', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "L'Agenzia pubblica in via telematica i dati anagrafici, la sede legale, i "
           'certificati delle chiavi di certificazione e il manuale operativo del certificatore, '
           "per renderne pubblica l'identificazione; chi consulta tali informazioni può "
           'utilizzarle solo per le finalità consentite dalla legge.',
  'testo_integrale': "L'Agenzia rende accessibili, in via telematica, le informazioni di cui al "
                     'comma 1, lettere a), b), e), g) al fine di rendere pubbliche le '
                     'informazioni che individuano il certificatore qualificato. Tali '
                     'informazioni sono utilizzate, da chi le consulta, solo per le finalità '
                     'consentite dalla legge.',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 16 c.1',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Il certificatore che rilascia al pubblico certificati qualificati comunica '
           "all'Agenzia la casella di posta elettronica certificata da usare per lo scambio "
           'delle informazioni previste dal decreto.',
  'testo_integrale': 'I certificatori che rilasciano al pubblico certificati qualificati '
                     "comunicano all'Agenzia la casella di posta elettronica certificata da "
                     'utilizzare per realizzare un sistema di comunicazione attraverso il quale '
                     'scambiare le informazioni previste dal presente decreto.',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 16 c.2',
  'soggetti': [{'categoria': 'Terzi affidanti/pubblico', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "L'Agenzia pubblica sul proprio sito internet l'indirizzo della propria casella di "
           'posta elettronica certificata.',
  'testo_integrale': "L'Agenzia rende disponibile sul proprio sito internet l'indirizzo della "
                     'propria casella di posta elettronica certificata.',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 17 c.1',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'La generazione delle chiavi di certificazione deve rispettare quanto previsto dalle '
           'regole tecniche del decreto.',
  'testo_integrale': 'La generazione delle chiavi di certificazione avviene in modo conforme a '
                     'quanto previsto dalle presenti regole tecniche.',
  'tipo_obbligo': 'tecnico/sicurezza'},
 {'riferimento': 'art. 17 c.2',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Per ogni chiave di certificazione il certificatore genera un certificato firmato con '
           'la chiave privata della relativa coppia.',
  'testo_integrale': 'Per ciascuna chiave di certificazione il certificatore genera un '
                     'certificato sottoscritto con la chiave privata della coppia cui il '
                     'certificato si riferisce.',
  'tipo_obbligo': 'tecnico/sicurezza'},
 {'riferimento': 'art. 17 c.3',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'I campi del certificato delle chiavi di certificazione sono codificati in modo da '
           'non creare equivoci sul nome o sulla denominazione del certificatore.',
  'testo_integrale': 'I valori contenuti nei singoli campi del certificato delle chiavi di '
                     'certificazione sono codificati in modo da non generare equivoci relativi '
                     'al nome, ragione o denominazione sociale del certificatore.',
  'tipo_obbligo': 'tecnico/sicurezza'},
 {'riferimento': 'art. 17 c.4',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'I dispositivi sicuri per la creazione di una firma usati per le chiavi indicate '
           'devono avere una certificazione di sicurezza non inferiore al livello EAL 4+ ISO/IEC '
           '15408 secondo i profili di protezione della decisione della Commissione europea del '
           '14 luglio 2003, oppure al livello e ai profili di protezione o traguardi di '
           'sicurezza giudicati adeguati dagli organismi indicati dalla direttiva 1999/93/CE.',
  'testo_integrale': 'La certificazione di sicurezza dei dispositivi sicuri per la creazione di '
                     "una firma utilizzati per le chiavi di cui all'art. 5, comma 4, lettere b), "
                     'c) e d), è effettuata secondo criteri non inferiori a quelli previsti: a) '
                     'dal livello EAL 4+ della norma ISO/IEC 15408 in conformità ai profili di '
                     'protezione indicati nella decisione della Commissione europea 14 luglio '
                     '2003 e successive modificazioni; b) dal livello di certificazione e in '
                     'conformità ai profili di protezione o traguardi di sicurezza giudicati '
                     "adeguati dagli organismi di cui all'art. 11, comma 1, lettera b) della "
                     'Direttiva europea 1999/93/EU.',
  'tipo_obbligo': 'tecnico/sicurezza'},
 {'riferimento': 'art. 18 c.1 lett.a)',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "All'emissione del certificato qualificato il certificatore accerta l'autenticità "
           'della richiesta.',
  'testo_integrale': "Fermo restando quanto previsto dall'art. 32 del Codice, all'atto "
                     "dell'emissione del certificato qualificato, il certificatore: a) accerta "
                     "l'autenticità della richiesta;",
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 18 c.1 lett.b)',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Se le chiavi sono generate dallo stesso certificatore, questo assicura la consegna '
           'al legittimo titolare; se le chiavi non sono generate dal certificatore, questo '
           'verifica il possesso della chiave privata da parte del titolare e il corretto '
           'funzionamento della coppia di chiavi.',
  'testo_integrale': 'b) nel caso di chiavi generate dallo stesso certificatore, assicura la '
                     'consegna al legittimo titolare ovvero, nel caso di chiavi non generate '
                     'dallo stesso certificatore, verifica il possesso della chiave privata da '
                     'parte del titolare e il corretto funzionamento della coppia di chiavi.',
  'tipo_obbligo': 'tecnico/sicurezza'},
 {'riferimento': 'art. 18 c.2',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Il certificato qualificato è generato con un sistema conforme a quanto previsto '
           "dall'art. 33.",
  'testo_integrale': 'Il certificato qualificato è generato con un sistema conforme a quanto '
                     "previsto dall'art. 33.",
  'tipo_obbligo': 'tecnico/sicurezza'},
 {'riferimento': 'art. 18 c.3',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Il periodo di validità del certificato qualificato termina almeno due anni prima del '
           'termine di validità del certificato delle chiavi di certificazione usato per '
           "verificarne l'autenticità.",
  'testo_integrale': 'Il termine del periodo di validità del certificato qualificato precede di '
                     'almeno due anni il termine del periodo di validità del certificato delle '
                     "chiavi di certificazione utilizzato per verificarne l'autenticità.",
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 18 c.4',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "L'emissione dei certificati qualificati è registrata nel giornale di controllo, con "
           'indicazione del riferimento temporale della registrazione.',
  'testo_integrale': "L'emissione dei certificati qualificati è registrata nel giornale di "
                     'controllo specificando il riferimento temporale relativo alla '
                     'registrazione.',
  'tipo_obbligo': 'di conservazione'},
 {'riferimento': 'art. 19 c.1 lett.a)',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'I certificati qualificati contengono almeno il codice identificativo del titolare '
           'presso il certificatore.',
  'testo_integrale': "Fatto salvo quanto previsto dall'art. 28 del Codice, i certificati "
                     'qualificati contengono almeno le seguenti ulteriori informazioni: a) '
                     'Codice identificativo del titolare presso il certificatore;',
  'tipo_obbligo': 'tecnico/sicurezza'},
 {'riferimento': 'art. 19 c.1 lett.b)',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "I certificati qualificati contengono almeno l'indicazione della tipologia della "
           "coppia di chiavi in base all'uso cui sono destinate.",
  'testo_integrale': "b) tipologia della coppia di chiavi in base all'uso cui sono destinate.",
  'tipo_obbligo': 'tecnico/sicurezza'},
 {'riferimento': 'art. 19 c.2',
  'soggetti': [{'categoria': 'Terzi affidanti/pubblico', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Le informazioni personali del certificato qualificato possono essere usate solo per '
           'identificare il titolare della firma elettronica qualificata o digitale, per '
           'verificare la firma del documento informatico, o per indicarne le qualifiche '
           'specifiche.',
  'testo_integrale': 'Le informazioni personali contenute nel certificato qualificato ai sensi '
                     "di quanto previsto nell'art. 28 del Codice sono utilizzabili unicamente "
                     'per identificare il titolare della firma elettronica qualificata o della '
                     'firma digitale, per verificare la firma del documento informatico, nonché '
                     'per indicare eventuali qualifiche specifiche del titolare.',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 19 c.3',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'I campi del certificato qualificato sono codificati in modo da non generare equivoci '
           'sul nome o sulla denominazione del certificatore.',
  'testo_integrale': 'I valori contenuti nei singoli campi del certificato qualificato sono '
                     'codificati in modo da non generare equivoci relativi al nome, ragione o '
                     'denominazione sociale del certificatore.',
  'tipo_obbligo': 'tecnico/sicurezza'},
 {'riferimento': 'art. 19 c.4 lett.a)',
  'soggetti': [{'categoria': 'Utente/titolare', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Su richiesta del titolare, il certificatore inserisce le informazioni e qualifiche '
           "di cui all'art. 28 c.3 lett.a) del Codice nel certificato qualificato senza "
           "indicazione dell'organizzazione di appartenenza; a tal fine il titolare fornisce al "
           'certificatore una dichiarazione sostitutiva ai sensi del DPR 445/2000.',
  'testo_integrale': "Le informazioni e le qualifiche di cui all'art. 28, comma 3, lettera a) "
                     'del Codice, codificate secondo le modalità indicate dai provvedimenti di '
                     "cui all'art. 4, comma 2, del presente decreto, sono inserite dal "
                     'certificatore su richiesta del titolare: a) nel certificato qualificato '
                     "senza l'indicazione dell'organizzazione di appartenenza. A tal fine, il "
                     'titolare del certificato fornisce al certificatore una dichiarazione '
                     'sostitutiva ai sensi del decreto del Presidente della Repubblica 28 '
                     'dicembre 2000, n. 445;',
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 19 c.4 lett.b)',
  'soggetti': [{'categoria': 'Utente/titolare', 'ruolo': 'obbligato'},
               {'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'In alternativa, tali informazioni sono inserite nel certificato di attributo o nel '
           "certificato qualificato con indicazione dell'organizzazione di appartenenza: il "
           "titolare chiede all'organizzazione un'autorizzazione all'emissione e comunica "
           "all'organizzazione il certificatore prescelto; l'organizzazione ha l'obbligo di "
           "rilasciare l'autorizzazione e di chiedere al certificatore la revoca del certificato "
           'se viene a conoscenza di variazioni delle informazioni o qualifiche in esso '
           'contenute.',
  'testo_integrale': 'b) ovvero, nel certificato di attributo o nel certificato qualificato con '
                     "l'indicazione dell'organizzazione di appartenenza. A tal fine, il titolare "
                     "del certificato richiede all'organizzazione di appartenenza una "
                     "autorizzazione all'emissione del certificato, qualificato o di attributo "
                     "che consegna al certificatore. L'organizzazione, che ha l'obbligo di "
                     "fornire tale autorizzazione, assume l'impegno di richiedere al "
                     'certificatore la revoca del certificato qualificato qualora venga a '
                     'conoscenza della variazione delle informazioni o delle qualifiche '
                     "contenute nello stesso. Il titolare, nel richiedere l'autorizzazione, ha "
                     "l'obbligo di comunicare all'organizzazione di appartenenza il "
                     'certificatore cui intende rivolgersi.',
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 19 c.5',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Salvo quanto previsto dal comma 6, il certificatore determina il periodo di validità '
           'dei certificati qualificati anche in base alla robustezza crittografica delle chiavi '
           'impiegate.',
  'testo_integrale': 'Il certificatore, salvo quanto disposto al comma 6, determina il periodo '
                     'di validità dei certificati qualificati anche in funzione della robustezza '
                     'crittografica delle chiavi impiegate.',
  'tipo_obbligo': 'tecnico/sicurezza'},
 {'riferimento': 'art. 19 c.6',
  'soggetti': [{'categoria': 'Terzi affidanti/pubblico', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "L'Agenzia determina il periodo massimo di validità del certificato qualificato in "
           'base agli algoritmi e alle caratteristiche delle chiavi.',
  'testo_integrale': "L'Agenzia, ai sensi dell'art. 4, comma 2, determina il periodo massimo di "
                     'validità del certificato qualificato in funzione degli algoritmi e delle '
                     'caratteristiche delle chiavi.',
  'tipo_obbligo': 'tecnico/sicurezza'},
 {'condizione_applicabilita': 'il certificatore ha notizia della compromissione della chiave '
                              'privata o del dispositivo sicuro per la generazione delle firme',
  'riferimento': 'art. 20 c.1',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Il certificatore revoca o sospende il certificato qualificato quando ha notizia '
           'della compromissione della chiave privata o del dispositivo sicuro per la '
           'generazione delle firme elettroniche qualificate o digitali.',
  'testo_integrale': "Fatto salvo quanto previsto dall'art. 36 del Codice, il certificato "
                     "qualificato è revocato o sospeso dal certificatore, ove quest'ultimo abbia "
                     'notizia della compromissione della chiave privata o del dispositivo sicuro '
                     'per la generazione delle firme elettroniche qualificate o digitali.',
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 20 c.2',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Il certificatore conserva le richieste di revoca e sospensione per lo stesso periodo '
           "previsto dall'art. 32, comma 3, lettera j) del Codice.",
  'testo_integrale': 'Il certificatore conserva le richieste di revoca e sospensione per lo '
                     "stesso periodo previsto all'art. 32, comma 3, lettera j) del Codice.",
  'tipo_obbligo': 'di conservazione'},
 {'riferimento': 'art. 21 c.1',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
               {'categoria': 'Utente/titolare', 'ruolo': 'destinatario'}],
  'stato': 'vigente',
  'testo': 'Per ogni certificato qualificato emesso, il certificatore fornisce al titolare '
           'almeno un codice riservato, da usare per chiedere la sospensione del certificato nei '
           'casi di emergenza indicati nel manuale operativo e comunicati al titolare.',
  'testo_integrale': 'Per ciascun certificato qualificato emesso il certificatore fornisce al '
                     'titolare almeno un Codice riservato, da utilizzare per richiedere la '
                     'sospensione del certificato nei casi di emergenza indicati nel manuale '
                     "operativo di cui all'art. 40 e comunicati al titolare.",
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 21 c.2',
  'soggetti': [{'categoria': 'Utente/titolare', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'La richiesta di sospensione fatta con il codice di emergenza è successivamente '
           'confermata dal titolare con una delle modalità previste dal certificatore.',
  'testo_integrale': 'La richiesta di cui al comma 1 è successivamente confermata utilizzando '
                     'una delle modalità previste dal certificatore.',
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 21 c.3',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Il certificatore adotta specifiche misure di sicurezza per garantire la segretezza '
           'del codice di emergenza.',
  'testo_integrale': 'Il certificatore adotta specifiche misure di sicurezza per assicurare la '
                     'segretezza del Codice di emergenza.',
  'tipo_obbligo': 'tecnico/sicurezza'},
 {'riferimento': 'art. 22 c.1',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Il certificatore revoca il certificato qualificato relativo a chiavi di '
           'sottoscrizione inserendo il relativo codice identificativo in una delle liste dei '
           'certificati revocati e sospesi (CRL).',
  'testo_integrale': 'La revoca del certificato qualificato relativo a chiavi di sottoscrizione '
                     "viene effettuata dal certificatore mediante l'inserimento del suo Codice "
                     'identificativo in una delle liste di certificati revocati e sospesi (CRL).',
  'tipo_obbligo': 'procedurale'},
 {'condizione_applicabilita': 'la revoca è dovuta alla possibile compromissione della chiave '
                              'privata',
  'riferimento': 'art. 22 c.2',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Se la revoca è dovuta alla possibile compromissione della chiave privata, il '
           "certificatore pubblica tempestivamente l'aggiornamento della lista di revoca.",
  'testo_integrale': 'Se la revoca avviene a causa della possibile compromissione della chiave '
                     'privata, il certificatore deve procedere tempestivamente alla '
                     "pubblicazione dell'aggiornamento della lista di revoca.",
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 22 c.3',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "La revoca dei certificati è annotata nel giornale di controllo con la data e l'ora "
           'di pubblicazione della CRL.',
  'testo_integrale': 'La revoca dei certificati è annotata nel giornale di controllo con la '
                     "specificazione della data e dell'ora della pubblicazione della CRL.",
  'tipo_obbligo': 'di conservazione'},
 {'riferimento': 'art. 22 c.4',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
               {'categoria': 'Utente/titolare', 'ruolo': 'destinatario'},
               {'categoria': 'Terza parte', 'ruolo': 'destinatario'}],
  'stato': 'vigente',
  'testo': "Il certificatore comunica tempestivamente al titolare e all'eventuale terzo "
           "interessato l'avvenuta revoca, specificando data e ora a partire dalle quali il "
           'certificato risulta revocato.',
  'testo_integrale': "Il certificatore comunica tempestivamente l'avvenuta revoca al titolare e "
                     "all'eventuale terzo interessato specificando la data e l'ora a partire "
                     'dalla quale il certificato qualificato risulta revocato.',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'condizione_applicabilita': 'salvo i casi di motivata urgenza',
  'riferimento': 'art. 23 c.1',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
               {'categoria': 'Utente/titolare', 'ruolo': 'destinatario'}],
  'stato': 'vigente',
  'testo': 'Salvo motivata urgenza, il certificatore che intende revocare un certificato '
           'qualificato ne dà preventiva comunicazione al titolare, indicando i motivi della '
           "revoca e la data e l'ora a partire dalle quali diventa efficace.",
  'testo_integrale': 'Salvo i casi di motivata urgenza, il certificatore che intende revocare un '
                     'certificato qualificato ne dà preventiva comunicazione al titolare, '
                     "specificando i motivi della revoca nonché la data e l'ora a partire dalla "
                     'quale la revoca è efficace.',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 24 c.1',
  'soggetti': [{'categoria': 'Utente/titolare', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Il titolare inoltra al certificatore la richiesta di revoca, sottoscritta e con '
           "l'indicazione della decorrenza.",
  'testo_integrale': 'La richiesta di revoca è inoltrata al certificatore munita della '
                     'sottoscrizione del titolare e con la specificazione della sua decorrenza.',
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 24 c.2',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Il certificatore indica nel manuale operativo le modalità di inoltro della richiesta '
           'di revoca.',
  'testo_integrale': 'Le modalità di inoltro della richiesta sono indicate dal certificatore nel '
                     "manuale operativo di cui all'art. 40.",
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 24 c.3',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "Il certificatore verifica l'autenticità della richiesta e procede alla revoca entro "
           'il termine richiesto; sono considerate autentiche le richieste inoltrate secondo le '
           'modalità indicate nel manuale operativo.',
  'testo_integrale': "Il certificatore verifica l'autenticità della richiesta e procede alla "
                     'revoca entro il termine richiesto. Sono considerate autentiche le '
                     'richieste inoltrate con le modalità previste dal comma 2.',
  'tipo_obbligo': 'procedurale'},
 {'condizione_applicabilita': 'il certificatore non ha la possibilità di accertare in tempo '
                              "utile l'autenticità della richiesta di revoca",
  'riferimento': 'art. 24 c.4',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "Se il certificatore non riesce ad accertare in tempo utile l'autenticità della "
           'richiesta, procede alla sospensione del certificato.',
  'testo_integrale': 'Se il certificatore non ha la possibilità di accertare in tempo utile '
                     "l'autenticità della richiesta, procede alla sospensione del certificato.",
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 25 c.1',
  'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Il terzo interessato da cui derivano i poteri di firma del titolare inoltra al '
           "certificatore la richiesta di revoca, sottoscritta e con l'indicazione della "
           'decorrenza.',
  'testo_integrale': 'La richiesta di revoca da parte del terzo interessato da cui derivano i '
                     'poteri di firma del titolare è inoltrata al certificatore munita di '
                     'sottoscrizione e con la specificazione della sua decorrenza.',
  'tipo_obbligo': 'procedurale'},
 {'condizione_applicabilita': 'cessazione o modifica delle qualifiche o del titolo inserite nel '
                              'certificato su richiesta del terzo interessato',
  'riferimento': 'art. 25 c.2',
  'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Se cessano o cambiano le qualifiche o il titolo inseriti nel certificato su '
           'richiesta del terzo interessato, questi inoltra la richiesta di revoca non appena '
           'viene a conoscenza della variazione.',
  'testo_integrale': 'In caso di cessazione o modifica delle qualifiche o del titolo inserite '
                     'nel certificato su richiesta del terzo interessato, la richiesta di revoca '
                     'di cui al comma 1 è inoltrata non appena il terzo venga a conoscenza della '
                     'variazione di stato.',
  'tipo_obbligo': 'procedurale'},
 {'condizione_applicabilita': 'il certificatore non ha la possibilità di accertare in tempo '
                              "utile l'autenticità della richiesta di revoca del terzo "
                              'interessato',
  'riferimento': 'art. 25 c.3',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "Se il certificatore non riesce ad accertare in tempo utile l'autenticità della "
           'richiesta di revoca del terzo interessato, procede alla sospensione del certificato.',
  'testo_integrale': 'Se il certificatore non ha la possibilità di accertare in tempo utile '
                     "l'autenticità della richiesta, procede alla sospensione del certificato.",
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 26 c.1',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Il certificatore sospende il certificato qualificato inserendo il relativo codice '
           'identificativo in una delle liste dei certificati revocati e sospesi (CRL).',
  'testo_integrale': 'La sospensione del certificato qualificato è effettuata dal certificatore '
                     "mediante l'inserimento del suo Codice identificativo in una delle liste "
                     'dei certificati revocati e sospesi (CRL).',
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 26 c.2',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
               {'categoria': 'Utente/titolare', 'ruolo': 'destinatario'},
               {'categoria': 'Terza parte', 'ruolo': 'destinatario'}],
  'stato': 'vigente',
  'testo': "Il certificatore comunica tempestivamente al titolare e all'eventuale terzo "
           "interessato l'avvenuta sospensione, specificando data e ora a partire dalle quali il "
           'certificato risulta sospeso.',
  'testo_integrale': "Il certificatore comunica tempestivamente l'avvenuta sospensione al "
                     "titolare e all'eventuale terzo interessato specificando la data e l'ora a "
                     'partire dalla quale il certificato qualificato risulta sospeso.',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 26 c.3',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Il certificatore indica nel manuale operativo la durata massima del periodo di '
           'sospensione e le azioni da intraprendere al suo termine in assenza di diverse '
           'indicazioni da parte di chi ha richiesto la sospensione.',
  'testo_integrale': "Il certificatore indica nel manuale operativo, ai sensi dell'art. 40, "
                     'comma 3, lettera l), la durata massima del periodo di sospensione e le '
                     'azioni intraprese al termine dello stesso in assenza di diverse '
                     'indicazioni da parte del soggetto che ha richiesto la sospensione.',
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 26 c.5',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'La sospensione e la sua cessazione sono annotate nel giornale di controllo con data '
           "e ora di esecuzione dell'operazione.",
  'testo_integrale': 'La sospensione e la cessazione della stessa sono annotate nel giornale di '
                     "controllo con l'indicazione della data e dell'ora di esecuzione "
                     "dell'operazione.",
  'tipo_obbligo': 'di conservazione'},
 {'riferimento': 'art. 26 c.6',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
               {'categoria': 'Utente/titolare', 'ruolo': 'destinatario'},
               {'categoria': 'Terza parte', 'ruolo': 'destinatario'}],
  'stato': 'vigente',
  'testo': 'La cessazione dello stato di sospensione, dopo la quale il certificato è considerato '
           "come mai sospeso, è comunicata tempestivamente al titolare e all'eventuale terzo "
           "interessato con l'indicazione di data e ora del cambio di stato.",
  'testo_integrale': 'La cessazione dello stato di sospensione del certificato, che sarà '
                     'considerato come mai sospeso, è tempestivamente comunicata al titolare e '
                     "all'eventuale terzo interessato specificando la data e l'ora a partire "
                     'dalla quale il certificato ha cambiato stato.',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'condizione_applicabilita': "salvo casi d'urgenza, da motivare contestualmente alla "
                              'comunicazione della sospensione',
  'riferimento': 'art. 27 c.1',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
               {'categoria': 'Utente/titolare', 'ruolo': 'destinatario'},
               {'categoria': 'Terza parte', 'ruolo': 'destinatario'}],
  'stato': 'vigente',
  'testo': "Salvo casi d'urgenza da motivare contestualmente alla comunicazione della "
           'sospensione, il certificatore che intende sospendere un certificato qualificato ne '
           "dà preventiva comunicazione al titolare e all'eventuale terzo interessato, indicando "
           'i motivi e la durata della sospensione.',
  'testo_integrale': "Salvo casi d'urgenza che il certificatore è tenuto a motivare "
                     'contestualmente alla comunicazione conseguente alla sospensione di cui al '
                     'comma 2, il certificatore che intende sospendere un certificato '
                     "qualificato ne dà preventiva comunicazione al titolare e all'eventuale "
                     'terzo interessato specificando i motivi della sospensione e la sua durata.',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'condizione_applicabilita': 'la sospensione è causata da una richiesta di revoca motivata '
                              'dalla possibile compromissione della chiave privata',
  'riferimento': 'art. 27 c.2',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Se la sospensione è dovuta a una richiesta di revoca motivata dalla possibile '
           'compromissione della chiave privata, il certificatore pubblica tempestivamente la '
           'sospensione.',
  'testo_integrale': 'Se la sospensione è causata da una richiesta di revoca motivata dalla '
                     'possibile compromissione della chiave privata, il certificatore procede '
                     'tempestivamente alla pubblicazione della sospensione.',
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 28 c.1',
  'soggetti': [{'categoria': 'Utente/titolare', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "Il titolare inoltra al certificatore la richiesta di sospensione, con l'indicazione "
           'della durata, secondo le modalità indicate nel manuale operativo approvato '
           "dall'Agenzia.",
  'testo_integrale': 'La richiesta di sospensione del certificato qualificato, con la '
                     'specificazione della sua durata, è inoltrata al certificatore, secondo le '
                     "modalità indicate nel manuale operativo approvato dall'Agenzia.",
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 28 c.2',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "Il certificatore verifica l'autenticità della richiesta e procede alla sospensione "
           'entro il termine richiesto; sono considerate autentiche le richieste inoltrate '
           'secondo le modalità del comma 1.',
  'testo_integrale': "Il certificatore verifica l'autenticità della richiesta e procede alla "
                     'sospensione entro il termine richiesto. Sono considerate autentiche le '
                     'richieste inoltrate con le modalità previste dal precedente comma 1.',
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 29 c.1',
  'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'Il terzo interessato da cui derivano i poteri di firma del titolare inoltra al '
           "certificatore la richiesta di sospensione, sottoscritta e con l'indicazione della "
           'durata.',
  'testo_integrale': 'La richiesta di sospensione del certificato qualificato da parte del terzo '
                     'interessato, da cui derivano i poteri di firma del titolare, è inoltrata '
                     'al certificatore munita di sottoscrizione e con la specificazione della '
                     'sua durata.',
  'tipo_obbligo': 'procedurale'},
 {'riferimento': 'art. 30 c.1',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'La procedura di sostituzione delle chiavi generate dal certificatore in conformità '
           "all'art. 17 assicura il rispetto del termine di cui all'art. 18, comma 3.",
  'testo_integrale': 'La procedura di sostituzione delle chiavi, generate dal certificatore in '
                     "conformità all'art. 17, assicura il rispetto del termine di cui all'art. "
                     '18, comma 3.',
  'tipo_obbligo': 'tecnico/sicurezza'},
 {'riferimento': 'art. 30 c.2',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'I certificati generati a seguito della sostituzione delle chiavi di certificazione '
           "sono inviati all'Agenzia.",
  'testo_integrale': 'I certificati generati a seguito della sostituzione delle chiavi di '
                     "certificazione sono inviati all'Agenzia.",
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 31 c.2',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': 'La revoca del certificato di chiavi di certificazione è comunicata entro '
           "ventiquattro ore all'Agenzia ed è resa nota a tutti i titolari di certificati "
           'qualificati sottoscritti con la chiave privata la cui chiave pubblica corrispondente '
           'è contenuta nel certificato revocato.',
  'testo_integrale': "La revoca è comunicata entro ventiquattro ore all'Agenzia e resa nota a "
                     'tutti i titolari di certificati qualificati sottoscritti con la chiave '
                     'privata la cui corrispondente chiave pubblica è contenuta nel certificato '
                     'revocato.',
  'tipo_obbligo': 'informativo/trasparenza'},
 {'riferimento': 'art. 31 c.3',
  'soggetti': [{'categoria': 'Terzi affidanti/pubblico', 'ruolo': 'obbligato'}],
  'stato': 'vigente',
  'testo': "La revoca dei certificati di chiavi di certificazione pubblicati dall'Agenzia "
           "nell'elenco pubblico dei certificatori è resa nota attraverso lo stesso elenco.",
  'testo_integrale': "La revoca di certificati di cui al comma 1, pubblicati dall'Agenzia "
                     "nell'elenco pubblico dei certificatori di cui all'art. 43, è resa nota "
                     'attraverso il medesimo elenco.',
  'tipo_obbligo': 'informativo/trasparenza'}]

RIGHE_PRINCIPI = [{'oggetti_giuridici': ['dispositivo qualificato di creazione di firma elettronica'],
  'riferimento': 'art. 17 c.5',
  'stato': 'vigente',
  'testo': 'In alternativa, la certificazione di sicurezza dei dispositivi può basarsi sul '
           "livello di valutazione E3 e robustezza HIGH dell'ITSEC (o superiore), con un "
           "traguardo di sicurezza ritenuto adeguato dall'Agenzia.",
  'testo_integrale': 'La certificazione di sicurezza di cui al comma 4 può inoltre essere '
                     'effettuata secondo i criteri previsti dal livello di valutazione E3 e '
                     "robustezza HIGH dell'ITSEC, o superiori, con un traguardo di sicurezza "
                     "giudicato adeguato dall'Agenzia nell'ambito dell'attività di cui agli "
                     'articoli 29 e 31 del Codice.',
  'tipo_principio': 'altro'},
 {'oggetti_giuridici': ['certificato qualificato di firma elettronica'],
  'riferimento': 'art. 19 c.7',
  'stato': 'vigente',
  'testo': "Il certificato qualificato può indicare che l'uso della chiave privata per generare "
           'la firma è subordinato alla verifica, da parte del certificatore, della validità del '
           "certificato qualificato e dell'eventuale certificato di attributo; l'attuazione di "
           'questa facoltà segue le modalità stabilite dai provvedimenti attuativi.',
  'testo_integrale': "Il certificato qualificato può contenere l'indicazione che l'utilizzo "
                     'della chiave privata per la generazione della firma è subordinato alla '
                     'verifica da parte del certificatore della validità del certificato '
                     "qualificato e dell'eventuale certificato di attributo. All'attuazione del "
                     'presente comma si provvede con le modalità stabilite dai provvedimenti di '
                     "cui all'art. 4, comma 2.",
  'tipo_principio': 'altro'},
 {'riferimento': 'art. 26 c.4',
  'stato': 'vigente',
  'testo': 'Se un certificato qualificato sospeso viene poi revocato, la data della revoca '
           'decorre dalla data di inizio del periodo di sospensione.',
  'testo_integrale': 'In caso di revoca di un certificato qualificato sospeso, la data della '
                     'stessa decorre dalla data di inizio del periodo di sospensione.',
  'tipo_principio': 'altro'},
 {'oggetti_giuridici': ['dispositivo qualificato di creazione di firma elettronica'],
  'riferimento': 'art. 31 c.1',
  'stato': 'vigente',
  'testo': 'La revoca del certificato relativo a una coppia di chiavi di certificazione è '
           'ammessa solo in caso di compromissione della chiave privata, malfunzionamento '
           'irrecuperabile del dispositivo sicuro per la generazione delle firme, o cessazione '
           "dell'attività.",
  'testo_integrale': 'La revoca del certificato relativo ad una coppia di chiavi di '
                     'certificazione è consentita solo nei seguenti casi: a) compromissione '
                     'della chiave privata; b) malfunzionamento irrecuperabile del dispositivo '
                     "sicuro per la generazione delle firme; c) cessazione dell'attività.",
  'tipo_principio': 'altro'}]

INDICE_ARTICOLI_LOCALE = ['art. 15 c.1 lett.a)',
 'art. 15 c.1 lett.b)',
 'art. 15 c.1 lett.c)',
 'art. 15 c.1 lett.d)',
 'art. 15 c.1 lett.e)',
 'art. 15 c.1 lett.f)',
 'art. 15 c.1 lett.g)',
 'art. 15 c.1 lett.h)',
 'art. 15 c.1 lett.i)',
 'art. 15 c.2',
 'art. 16 c.1',
 'art. 16 c.2',
 'art. 17 c.1',
 'art. 17 c.2',
 'art. 17 c.3',
 'art. 17 c.4 lett.a)',
 'art. 17 c.4 lett.b)',
 'art. 17 c.5',
 'art. 18 c.1 lett.a)',
 'art. 18 c.1 lett.b)',
 'art. 18 c.2',
 'art. 18 c.3',
 'art. 18 c.4',
 'art. 19 c.1 lett.a)',
 'art. 19 c.1 lett.b)',
 'art. 19 c.2',
 'art. 19 c.3',
 'art. 19 c.4 lett.a)',
 'art. 19 c.4 lett.b)',
 'art. 19 c.5',
 'art. 19 c.6',
 'art. 19 c.7',
 'art. 20 c.1',
 'art. 20 c.2',
 'art. 21 c.1',
 'art. 21 c.2',
 'art. 21 c.3',
 'art. 22 c.1',
 'art. 22 c.2',
 'art. 22 c.3',
 'art. 22 c.4',
 'art. 23 c.1',
 'art. 24 c.1',
 'art. 24 c.2',
 'art. 24 c.3',
 'art. 24 c.4',
 'art. 25 c.1',
 'art. 25 c.2',
 'art. 25 c.3',
 'art. 26 c.1',
 'art. 26 c.2',
 'art. 26 c.3',
 'art. 26 c.4',
 'art. 26 c.5',
 'art. 26 c.6',
 'art. 27 c.1',
 'art. 27 c.2',
 'art. 28 c.1',
 'art. 28 c.2',
 'art. 29 c.1',
 'art. 30 c.1',
 'art. 30 c.2',
 'art. 31 c.1 lett.a)',
 'art. 31 c.1 lett.b)',
 'art. 31 c.1 lett.c)',
 'art. 31 c.2',
 'art. 31 c.3']

MAPPATURA_LOCALE = {'art. 15 c.1 lett.a)': ['art. 15 c.1 lett.a)'],
 'art. 15 c.1 lett.b)': ['art. 15 c.1 lett.b)'],
 'art. 15 c.1 lett.c)': ['art. 15 c.1 lett.c)'],
 'art. 15 c.1 lett.d)': ['art. 15 c.1 lett.d)'],
 'art. 15 c.1 lett.e)': ['art. 15 c.1 lett.e)'],
 'art. 15 c.1 lett.f)': ['art. 15 c.1 lett.f)'],
 'art. 15 c.1 lett.g)': ['art. 15 c.1 lett.g)'],
 'art. 15 c.1 lett.h)': ['art. 15 c.1 lett.h)'],
 'art. 15 c.1 lett.i)': ['art. 15 c.1 lett.i)'],
 'art. 15 c.2': ['art. 15 c.2'],
 'art. 16 c.1': ['art. 16 c.1'],
 'art. 16 c.2': ['art. 16 c.2'],
 'art. 17 c.1': ['art. 17 c.1'],
 'art. 17 c.2': ['art. 17 c.2'],
 'art. 17 c.3': ['art. 17 c.3'],
 'art. 17 c.4': ['art. 17 c.4 lett.a)', 'art. 17 c.4 lett.b)'],
 'art. 17 c.5': ['art. 17 c.5'],
 'art. 18 c.1 lett.a)': ['art. 18 c.1 lett.a)'],
 'art. 18 c.1 lett.b)': ['art. 18 c.1 lett.b)'],
 'art. 18 c.2': ['art. 18 c.2'],
 'art. 18 c.3': ['art. 18 c.3'],
 'art. 18 c.4': ['art. 18 c.4'],
 'art. 19 c.1 lett.a)': ['art. 19 c.1 lett.a)'],
 'art. 19 c.1 lett.b)': ['art. 19 c.1 lett.b)'],
 'art. 19 c.2': ['art. 19 c.2'],
 'art. 19 c.3': ['art. 19 c.3'],
 'art. 19 c.4 lett.a)': ['art. 19 c.4 lett.a)'],
 'art. 19 c.4 lett.b)': ['art. 19 c.4 lett.b)'],
 'art. 19 c.5': ['art. 19 c.5'],
 'art. 19 c.6': ['art. 19 c.6'],
 'art. 19 c.7': ['art. 19 c.7'],
 'art. 20 c.1': ['art. 20 c.1'],
 'art. 20 c.2': ['art. 20 c.2'],
 'art. 21 c.1': ['art. 21 c.1'],
 'art. 21 c.2': ['art. 21 c.2'],
 'art. 21 c.3': ['art. 21 c.3'],
 'art. 22 c.1': ['art. 22 c.1'],
 'art. 22 c.2': ['art. 22 c.2'],
 'art. 22 c.3': ['art. 22 c.3'],
 'art. 22 c.4': ['art. 22 c.4'],
 'art. 23 c.1': ['art. 23 c.1'],
 'art. 24 c.1': ['art. 24 c.1'],
 'art. 24 c.2': ['art. 24 c.2'],
 'art. 24 c.3': ['art. 24 c.3'],
 'art. 24 c.4': ['art. 24 c.4'],
 'art. 25 c.1': ['art. 25 c.1'],
 'art. 25 c.2': ['art. 25 c.2'],
 'art. 25 c.3': ['art. 25 c.3'],
 'art. 26 c.1': ['art. 26 c.1'],
 'art. 26 c.2': ['art. 26 c.2'],
 'art. 26 c.3': ['art. 26 c.3'],
 'art. 26 c.4': ['art. 26 c.4'],
 'art. 26 c.5': ['art. 26 c.5'],
 'art. 26 c.6': ['art. 26 c.6'],
 'art. 27 c.1': ['art. 27 c.1'],
 'art. 27 c.2': ['art. 27 c.2'],
 'art. 28 c.1': ['art. 28 c.1'],
 'art. 28 c.2': ['art. 28 c.2'],
 'art. 29 c.1': ['art. 29 c.1'],
 'art. 30 c.1': ['art. 30 c.1'],
 'art. 30 c.2': ['art. 30 c.2'],
 'art. 31 c.1': ['art. 31 c.1 lett.a)', 'art. 31 c.1 lett.b)', 'art. 31 c.1 lett.c)'],
 'art. 31 c.2': ['art. 31 c.2'],
 'art. 31 c.3': ['art. 31 c.3']}

RELAZIONI = [{'confidence': None,
  'evidence_type': 'textual',
  'nodo_a': ('obbligo', None, 'art. 17 c.1'),
  'nodo_da': ('obbligo', None, 'art. 30 c.1'),
  'tipo_relazione': 'richiama'},
 {'confidence': None,
  'evidence_type': 'textual',
  'nodo_a': ('obbligo', None, 'art. 18 c.3'),
  'nodo_da': ('obbligo', None, 'art. 30 c.1'),
  'tipo_relazione': 'richiama'},
 {'confidence': 0.6,
  'evidence_type': 'inferred',
  'nodo_a': ('obbligo', None, 'art. 17 c.1'),
  'nodo_da': ('obbligo', None, 'art. 18 c.1 lett.b)'),
  'tipo_relazione': 'richiede come precondizione'},
 {'confidence': 0.75,
  'evidence_type': 'inferred',
  'nodo_a': ('obbligo', None, 'art. 20 c.1'),
  'nodo_da': ('obbligo', None, 'art. 22 c.1'),
  'tipo_relazione': 'specifica'},
 {'confidence': 0.75,
  'evidence_type': 'inferred',
  'nodo_a': ('obbligo', None, 'art. 20 c.1'),
  'nodo_da': ('obbligo', None, 'art. 23 c.1'),
  'tipo_relazione': 'specifica'},
 {'confidence': 0.7,
  'evidence_type': 'inferred',
  'nodo_a': ('obbligo', None, 'art. 20 c.1'),
  'nodo_da': ('obbligo', None, 'art. 24 c.1'),
  'tipo_relazione': 'specifica'},
 {'confidence': 0.7,
  'evidence_type': 'inferred',
  'nodo_a': ('obbligo', None, 'art. 20 c.1'),
  'nodo_da': ('obbligo', None, 'art. 25 c.1'),
  'tipo_relazione': 'specifica'},
 {'confidence': 0.75,
  'evidence_type': 'inferred',
  'nodo_a': ('obbligo', None, 'art. 20 c.1'),
  'nodo_da': ('obbligo', None, 'art. 26 c.1'),
  'tipo_relazione': 'specifica'},
 {'confidence': 0.7,
  'evidence_type': 'inferred',
  'nodo_a': ('obbligo', None, 'art. 20 c.1'),
  'nodo_da': ('obbligo', None, 'art. 27 c.1'),
  'tipo_relazione': 'specifica'},
 {'confidence': 0.7,
  'evidence_type': 'inferred',
  'nodo_a': ('obbligo', None, 'art. 20 c.1'),
  'nodo_da': ('obbligo', None, 'art. 28 c.1'),
  'tipo_relazione': 'specifica'},
 {'confidence': 0.7,
  'evidence_type': 'inferred',
  'nodo_a': ('obbligo', None, 'art. 20 c.1'),
  'nodo_da': ('obbligo', None, 'art. 29 c.1'),
  'tipo_relazione': 'specifica'},
 {'confidence': 0.65,
  'evidence_type': 'inferred',
  'nodo_a': ('obbligo', None, 'art. 26 c.1'),
  'nodo_da': ('obbligo', None, 'art. 21 c.1'),
  'tipo_relazione': 'si applica a'},
 {'confidence': 0.8,
  'evidence_type': 'inferred',
  'nodo_a': ('obbligo', None, 'art. 24 c.4'),
  'nodo_da': ('obbligo', None, 'art. 25 c.3'),
  'tipo_relazione': 'si sovrappone a'},
 {'confidence': 0.6,
  'evidence_type': 'inferred',
  'nodo_a': ('obbligo', None, 'art. 20 c.1'),
  'nodo_da': ('principio', None, 'art. 26 c.4'),
  'tipo_relazione': 'si applica a'},
 {'confidence': 0.7,
  'evidence_type': 'inferred',
  'nodo_a': ('principio', None, 'art. 31 c.1'),
  'nodo_da': ('obbligo', None, 'art. 31 c.2'),
  'tipo_relazione': 'richiede come precondizione'},
 {'confidence': 0.65,
  'evidence_type': 'inferred',
  'nodo_a': ('obbligo', None, 'art. 31 c.2'),
  'nodo_da': ('obbligo', None, 'art. 31 c.3'),
  'tipo_relazione': 'attua'},
 {'confidence': None,
  'evidence_type': 'textual',
  'nodo_a': ('obbligo', None, 'art. 15 c.1 lett.a)'),
  'nodo_da': ('obbligo', None, 'art. 15 c.2'),
  'tipo_relazione': 'si applica a'},
 {'confidence': None,
  'evidence_type': 'textual',
  'nodo_a': ('obbligo', None, 'art. 15 c.1 lett.b)'),
  'nodo_da': ('obbligo', None, 'art. 15 c.2'),
  'tipo_relazione': 'si applica a'},
 {'confidence': None,
  'evidence_type': 'textual',
  'nodo_a': ('obbligo', None, 'art. 15 c.1 lett.e)'),
  'nodo_da': ('obbligo', None, 'art. 15 c.2'),
  'tipo_relazione': 'si applica a'},
 {'confidence': None,
  'evidence_type': 'textual',
  'nodo_a': ('obbligo', None, 'art. 15 c.1 lett.g)'),
  'nodo_da': ('obbligo', None, 'art. 15 c.2'),
  'tipo_relazione': 'si applica a'}]
