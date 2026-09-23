"""Estrazione granulare DPCM 22/2/2013 (ADR-0007) — Titolo IV - Regole per la validazione
temporale mediante marca temporale: artt. 47-54.

Fonte: DPCM 22 febbraio 2013 (fonte_id=4 nel censimento), testo ufficiale.
Testo ufficiale: app/.source_cache/dpcm/cap06.txt.

Contenuto: art. 47 (Validazione temporale con marca temporale), 48 (Informazioni contenute
nella marca temporale), 49 (Chiavi di marcatura temporale), 50 (Gestione dei certificati e
delle chiavi), 51 (Precisione dei sistemi di validazione temporale), 52 (Sicurezza dei sistemi
di validazione temporale), 53 (Registrazione delle marche generate), 54 (Richiesta di marca
temporale).

Copertura completa per comma (nessun discrimine di rilevanza, ADR-0007): tutti gli 8 articoli
sono articolati in commi non numerati esplicitamente nel testo (nessun "1." ripetuto con bis/ter),
ciascuno mappato a un solo nodo. Quando un comma elenca, tramite lettere a)...g), sfaccettature
omogenee di un'unica prescrizione continua (art. 47 c.2, requisiti del sistema di validazione
temporale; art. 48 c.1, informazioni obbligatorie della marca temporale), l'intero comma è
modellato come un solo nodo (un solo item di indice), con `testo_integrale` che riporta l'intero
comma comprese tutte le lettere — stessa convenzione già applicata nell'import CAD.

Soggetto obbligato di default per gli obblighi tecnici/organizzativi di questo capitolo è il
certificatore che eroga il servizio di validazione temporale, categoria "QTSP/gestore" (nel
lessico del DPCM 22/2/2013, antecedente a eIDAS, "certificatore accreditato"). L'art. 52 c.4 è
l'unico obbligo di questo capitolo il cui soggetto obbligato è l'Agenzia (categoria "Terzi
affidanti/pubblico"), con il certificatore come destinatario dell'esito della verifica.

Relazioni (RELAZIONI): limitate ai rinvii testuali espliciti interni a questo stesso capitolo
(art. 47 c.2 lett. b) cita esplicitamente gli artt. 48 e 51; art. 50 c.1 cita l'art. 49 c.3;
art. 52 c.1 cita l'art. 51 c.1; art. 53 c.2 cita il comma 1 dello stesso articolo). I rinvii
espliciti verso articoli di altri capitoli dello stesso DPCM (art. 50 c.2 e art. 54 c.3, che
citano entrambi "l'art. 4, comma 2", di competenza del capitolo cap02) e il rinvio verso l'art.
31 del Codice (art. 52 c.4, cross-fonte verso CAD) non sono modellati come RELAZIONI in questa
fase, per evitare la classe di bug nota di KeyError su merge parallelo tra subagent diversi;
restano tuttavia leggibili nel testo integrale delle rispettive righe.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        'riferimento': 'art. 47 c.2',
        'testo': "Le marche temporali sono generate da un apposito sistema di validazione temporale, sottoposto a personalizzazioni che ne innalzano il livello di sicurezza, in grado di: garantire l'esattezza del riferimento temporale come richiesto dal decreto; generare la struttura dei dati temporali secondo quanto specificato negli artt. 48 e 51; sottoscrivere elettronicamente tale struttura di dati.",
        'testo_integrale': "Le marche temporali sono generate da un apposito sistema di validazione temporale, sottoposto ad opportune personalizzazioni atte a innalzarne il livello di sicurezza, in grado di: a) garantire l'esattezza del riferimento temporale conformemente a quanto richiesto dal presente decreto; b) generare la struttura dei dati temporali secondo quanto specificato negli articoli 48 e 51; c) sottoscrivere elettronicamente la struttura di dati di cui alla lettera b).",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 48 c.1',
        'testo': "La marca temporale contiene almeno: identificativo dell'emittente, numero di serie, algoritmo di sottoscrizione, certificato relativo alla chiave di verifica, riferimento temporale della generazione, identificativo della funzione di hash utilizzata e valore dell'impronta dell'evidenza informatica.",
        'testo_integrale': "Una marca temporale contiene almeno le seguenti informazioni: a) identificativo dell'emittente; b) numero di serie della marca temporale; c) algoritmo di sottoscrizione della marca temporale; d) certificato relativo alla chiave utilizzata per la verifica della marca temporale; e) riferimento temporale della generazione della marca temporale; f) identificativo della funzione di hash utilizzata per generare l'impronta dell'evidenza informatica sottoposta a validazione temporale; g) valore dell'impronta dell'evidenza informatica.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 49 c.1',
        'testo': "Dal certificato relativo alla coppia di chiavi utilizzate per la validazione temporale deve essere possibile individuare il sistema di validazione temporale.",
        'testo_integrale': "Dal certificato relativo alla coppia di chiavi utilizzate per la validazione temporale deve essere possibile individuare il sistema di validazione temporale.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 49 c.2',
        'testo': "Per limitare il numero di marche temporali generate con la stessa coppia di chiavi, le chiavi di marcatura temporale sono sostituite e un nuovo certificato è emesso dopo non più di tre mesi di utilizzazione, indipendentemente dalla durata residua di validità e senza revocare il certificato della chiave precedente; il periodo è indicato nel manuale operativo e, previa valutazione, ritenuto congruente dall'Agenzia.",
        'testo_integrale': "Al fine di limitare il numero di marche temporali generate con la medesima coppia, le chiavi di marcatura temporale sono sostituite ed un nuovo certificato è emesso, in relazione alla robustezza delle chiavi crittografiche utilizzate, dopo non più di tre mesi di utilizzazione, indipendentemente dalla durata del loro periodo di validità e senza revocare il certificato corrispondente alla chiave precedentemente in uso. Detto periodo è indicato nel manuale operativo e, previa valutazione, ritenuto congruente dall'Agenzia.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 49 c.3',
        'testo': "Per la sottoscrizione dei certificati relativi a chiavi di marcatura temporale sono utilizzate chiavi di certificazione appositamente generate.",
        'testo_integrale': "Per la sottoscrizione dei certificati relativi a chiavi di marcatura temporale sono utilizzate chiavi di certificazione appositamente generate.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 49 c.4',
        'testo': "Le chiavi di certificazione e di marcatura temporale possono essere generate esclusivamente in presenza dei responsabili dei rispettivi servizi.",
        'testo_integrale': "Le chiavi di certificazione e di marcatura temporale possono essere generate esclusivamente in presenza dei responsabili dei rispettivi servizi.",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 50 c.1',
        'testo': "Alle chiavi di certificazione utilizzate per sottoscrivere i certificati relativi alle chiavi di marcatura temporale si applica quanto previsto per le chiavi di certificazione utilizzate per sottoscrivere i certificati relativi alle chiavi di sottoscrizione.",
        'testo_integrale': "Alle chiavi di certificazione utilizzate, ai sensi dell'art. 49, comma 3, per sottoscrivere i certificati relativi a chiavi di marcatura temporale, si applica quanto previsto per le chiavi di certificazione utilizzate per sottoscrivere certificati relativi a chiavi di sottoscrizione.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 50 c.2',
        'testo': "I certificati relativi a una coppia di chiavi di marcatura temporale, oltre a essere conformi ai requisiti generali dei certificati, contengono l'identificativo del sistema di marcatura temporale che utilizza le chiavi.",
        'testo_integrale': "I certificati relativi ad una coppia di chiavi di marcatura temporale, oltre ad essere conformi a quanto stabilito ai sensi dell'art. 4, comma 2, contengono l'identificativo del sistema di marcatura temporale che utilizza le chiavi.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 51 c.1',
        'testo': "Il riferimento temporale assegnato a una marca temporale coincide con il momento della sua generazione, con uno scarto non superiore a un secondo rispetto alla scala di tempo UTC(IEN).",
        'testo_integrale': "Il riferimento temporale assegnato ad una marca temporale coincide con il momento della sua generazione, con una differenza non superiore ad un minuto secondo rispetto alla scala di tempo UTC(IEN), di cui al decreto del Ministro dell'industria, del commercio e dell'artigianato 30 novembre 1993, n. 591.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 51 c.2',
        'testo': "Il riferimento temporale contenuto nella marca temporale è espresso con riferimento al Tempo Universale Coordinato (UTC).",
        'testo_integrale': "Il riferimento temporale contenuto nella marca temporale è specificato con riferimento al Tempo Universale Coordinato (UTC).",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 52 c.1',
        'testo': "Qualsiasi anomalia o tentativo di manomissione che possa rendere il sistema di validazione temporale incompatibile con i requisiti del decreto, in particolare con quello sulla precisione, è annotato sul giornale di controllo e causa il blocco del sistema.",
        'testo_integrale': "Qualsiasi anomalia o tentativo di manomissione che possa modificare il funzionamento del sistema di validazione temporale in modo da renderlo incompatibile con i requisiti previsti dal presente decreto, ed in particolare con quello di cui all'art. 51, comma 1, è annotato sul giornale di controllo e causa il blocco del sistema medesimo.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 52 c.2',
        'testo': "Il blocco del sistema di validazione temporale può essere rimosso esclusivamente con l'intervento di personale espressamente autorizzato.",
        'testo_integrale': "Il blocco del sistema di validazione temporale può essere rimosso esclusivamente con l'intervento di personale espressamente autorizzato.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 52 c.3',
        'testo': "I sistemi operativi dei sistemi di elaborazione utilizzati nelle attività di validazione temporale devono essere stati oggetto di opportune personalizzazioni atte a innalzarne il livello di sicurezza (hardening).",
        'testo_integrale': "I sistemi operativi dei sistemi di elaborazione utilizzati nelle attività di validazione temporale devono essere stati oggetto di opportune personalizzazioni atte a innalzarne il livello di sicurezza (hardening).",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 52 c.4',
        'testo': "Ai sensi dell'art. 31 del Codice, l'Agenzia verifica l'idoneità delle personalizzazioni di sicurezza dei sistemi di validazione temporale e indica al certificatore le eventuali azioni correttive da adottare.",
        'testo_integrale': "Ai sensi dell'art. 31 del Codice, l'Agenzia verifica l'idoneità delle personalizzazioni, di cui al comma 3, e indica al certificatore eventuali azioni correttive.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'Terzi affidanti/pubblico', 'ruolo': 'obbligato'},
            {'categoria': 'QTSP/gestore', 'ruolo': 'destinatario'},
        ],
    },
    {
        'riferimento': 'art. 53 c.1',
        'testo': "Tutte le marche temporali emesse da un sistema di validazione sono conservate in un apposito archivio digitale non modificabile per un periodo non inferiore a venti anni, oppure per un periodo maggiore su richiesta dell'interessato, alle condizioni previste dal certificatore.",
        'testo_integrale': "Tutte le marche temporali emesse da un sistema di validazione sono conservate in un apposito archivio digitale non modificabile per un periodo non inferiore a venti anni ovvero, su richiesta dell'interessato, per un periodo maggiore, alle condizioni previste dal certificatore.",
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 54 c.1',
        'testo': "Il certificatore stabilisce, pubblicandole nel manuale operativo, le procedure per l'invio della richiesta di marca temporale.",
        'testo_integrale': "Il certificatore stabilisce, pubblicandole nel manuale operativo, le procedure per l'invio della richiesta di marca temporale.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 54 c.4',
        'testo': "La generazione delle marche temporali garantisce un tempo di risposta, misurato come differenza tra il momento della ricezione della richiesta e l'ora riportata nella marca temporale, non superiore a un minuto primo.",
        'testo_integrale': "La generazione delle marche temporali garantisce un tempo di risposta, misurato come differenza tra il momento della ricezione della richiesta e l'ora riportata nella marca temporale, non superiore al minuto primo.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        'riferimento': 'art. 47 c.1',
        'testo': "La validazione temporale di un'evidenza informatica consiste nella generazione e nell'applicazione di una marca temporale alla relativa impronta.",
        'testo_integrale': "Una evidenza informatica è sottoposta a validazione temporale mediante generazione e applicazione di una marca temporale alla relativa impronta.",
        'tipo_principio': 'definitorio',
        'stato': 'vigente',
        'oggetti_giuridici': ['marca temporale elettronica qualificata'],
    },
    {
        'riferimento': 'art. 47 c.3',
        'testo': "L'evidenza informatica sottoposta a validazione temporale può essere costituita da un insieme di più impronte.",
        'testo_integrale': "L'evidenza informatica da sottoporre a validazione temporale può essere costituita da un insieme di impronte.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'oggetti_giuridici': ['marca temporale elettronica qualificata'],
    },
    {
        'riferimento': 'art. 48 c.2',
        'testo': "La marca temporale può inoltre contenere un codice identificativo dell'oggetto a cui appartiene l'impronta dell'evidenza informatica.",
        'testo_integrale': "La marca temporale può inoltre contenere un Codice identificativo dell'oggetto a cui appartiene l'impronta di cui al comma 1, lettera g).",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'oggetti_giuridici': ['marca temporale elettronica qualificata'],
    },
    {
        'riferimento': 'art. 53 c.2',
        'testo': "La marca temporale è valida per il periodo di conservazione stabilito o concordato con il certificatore.",
        'testo_integrale': "La marca temporale è valida per il periodo di conservazione, stabilito o concordato con il certificatore, di cui al comma 1.",
        'tipo_principio': 'valore probatorio',
        'stato': 'vigente',
        'oggetti_giuridici': ['marca temporale elettronica qualificata'],
    },
    {
        'riferimento': 'art. 54 c.2',
        'testo': "La richiesta di marca temporale contiene l'evidenza informatica alla quale la marca temporale deve essere applicata.",
        'testo_integrale': "La richiesta contiene l'evidenza informatica alla quale applicare la marca temporale.",
        'tipo_principio': 'definitorio',
        'stato': 'vigente',
        'oggetti_giuridici': ['marca temporale elettronica qualificata'],
    },
    {
        'riferimento': 'art. 54 c.3',
        'testo': "L'evidenza informatica può essere sostituita da una o più impronte, calcolate con funzioni di hash scelte dal certificatore tra quelle stabilite dal decreto.",
        'testo_integrale': "L'evidenza informatica può essere sostituita da una o più impronte, calcolate con funzioni di hash scelte dal certificatore tra quelle stabilite ai sensi dell'art. 4, comma 2.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'oggetti_giuridici': ['marca temporale elettronica qualificata'],
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    'art. 47 c.1',
    'art. 47 c.2',
    'art. 47 c.3',
    'art. 48 c.1',
    'art. 48 c.2',
    'art. 49 c.1',
    'art. 49 c.2',
    'art. 49 c.3',
    'art. 49 c.4',
    'art. 50 c.1',
    'art. 50 c.2',
    'art. 51 c.1',
    'art. 51 c.2',
    'art. 52 c.1',
    'art. 52 c.2',
    'art. 52 c.3',
    'art. 52 c.4',
    'art. 53 c.1',
    'art. 53 c.2',
    'art. 54 c.1',
    'art. 54 c.2',
    'art. 54 c.3',
    'art. 54 c.4',
]

MAPPATURA_LOCALE: dict[str, list[str]] = {
    'art. 47 c.1': ['art. 47 c.1'],
    'art. 47 c.2': ['art. 47 c.2'],
    'art. 47 c.3': ['art. 47 c.3'],
    'art. 48 c.1': ['art. 48 c.1'],
    'art. 48 c.2': ['art. 48 c.2'],
    'art. 49 c.1': ['art. 49 c.1'],
    'art. 49 c.2': ['art. 49 c.2'],
    'art. 49 c.3': ['art. 49 c.3'],
    'art. 49 c.4': ['art. 49 c.4'],
    'art. 50 c.1': ['art. 50 c.1'],
    'art. 50 c.2': ['art. 50 c.2'],
    'art. 51 c.1': ['art. 51 c.1'],
    'art. 51 c.2': ['art. 51 c.2'],
    'art. 52 c.1': ['art. 52 c.1'],
    'art. 52 c.2': ['art. 52 c.2'],
    'art. 52 c.3': ['art. 52 c.3'],
    'art. 52 c.4': ['art. 52 c.4'],
    'art. 53 c.1': ['art. 53 c.1'],
    'art. 53 c.2': ['art. 53 c.2'],
    'art. 54 c.1': ['art. 54 c.1'],
    'art. 54 c.2': ['art. 54 c.2'],
    'art. 54 c.3': ['art. 54 c.3'],
    'art. 54 c.4': ['art. 54 c.4'],
}

RELAZIONI: list[dict] = [
    {
        'nodo_da': ('obbligo', None, 'art. 47 c.2'),
        'nodo_a': ('obbligo', None, 'art. 48 c.1'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'art. 47 c.2'),
        'nodo_a': ('obbligo', None, 'art. 51 c.1'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'art. 50 c.1'),
        'nodo_a': ('obbligo', None, 'art. 49 c.3'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'art. 52 c.1'),
        'nodo_a': ('obbligo', None, 'art. 51 c.1'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': None,
    },
    {
        'nodo_da': ('principio', None, 'art. 53 c.2'),
        'nodo_a': ('obbligo', None, 'art. 53 c.1'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'textual',
        'confidence': None,
    },
]
