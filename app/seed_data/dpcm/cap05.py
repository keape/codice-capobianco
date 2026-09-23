"""Estrazione granulare DPCM 22/2/2013 - Titolo III, Certificatori accreditati
(artt. 42-46: obblighi per i certificatori accreditati, elenco pubblico dei
certificatori accreditati, rappresentazione del documento informatico,
limitazioni d'uso, verifica delle marche temporali).

Testo ufficiale vigente al 17/09/2026, fonte app/.source_cache/dpcm/cap05.txt (ADR-0007).
Modulo generato secondo il contratto di app/seed_data/lib.py: nessun discrimine di rilevanza,
copertura completa comma/lettera per comma/lettera.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 42 c.1",
        "testo": "Il certificatore accreditato genera, pubblica nel proprio registro e rende "
                 "accessibile per via telematica un certificato per ciascuna chiave di firma "
                 "usata dall'Agenzia per sottoscrivere l'elenco pubblico dei certificatori, al "
                 "fine di consentirne la verifica; chi consulta tali informazioni può usarle "
                 "solo per le finalità consentite dalla legge.",
        "testo_integrale": "Il certificatore accreditato genera un certificato per ciascuna "
                            "delle chiavi di firma utilizzate dall'Agenzia per la sottoscrizione "
                            "dell'elenco pubblico dei certificatori, lo pubblica nel proprio "
                            "registro dei certificati e lo rende accessibile per via telematica "
                            "al fine di verificare la validità delle chiavi utilizzate "
                            "dall'Agenzia. Tali informazioni sono utilizzate, da chi le "
                            "consulta, solo per le finalità consentite dalla legge.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 42 c.2",
        "testo": "Il certificatore accreditato garantisce che il proprio prodotto di verifica "
                 "sia interoperabile con i documenti informatici sottoscritti dall'Agenzia con "
                 "firme elettroniche qualificate e digitali, nell'ambito delle attività di "
                 "vigilanza di cui all'art. 31 del Codice.",
        "testo_integrale": "Il certificatore accreditato garantisce l'interoperabilità del "
                            "prodotto di verifica di cui all'art. 14 del presente decreto con i "
                            "documenti informatici sottoscritti mediante firme elettroniche "
                            "qualificate e digitali ad opera dell'Agenzia, nell'ambito delle "
                            "attività di cui all'art. 31 del Codice.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 42 c.3",
        "testo": "Il certificatore accreditato conserva copia della lista dei certificati "
                 "delle chiavi di certificazione, sottoscritta dall'Agenzia, e la rende "
                 "accessibile per via telematica ai soli fini della verifica delle firme "
                 "elettroniche qualificate e digitali.",
        "testo_integrale": "Il certificatore accreditato mantiene copia della lista, "
                            "sottoscritta dall'Agenzia, dei certificati relativi alle chiavi di "
                            "certificazione di cui all'art. 43, comma 1, lettera e) del "
                            "presente decreto, che rende accessibile per via telematica per la "
                            "specifica finalità della verifica delle firme elettroniche "
                            "qualificate e digitali.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 42 c.4",
        "testo": "Per ottenere e mantenere il riconoscimento ex art. 29, comma 1, del Codice, "
                 "i certificatori accreditati svolgono l'attività in conformità con i "
                 "provvedimenti dell'Agenzia adottati ai sensi dell'art. 4, comma 2.",
        "testo_integrale": "I certificatori accreditati, al fine di ottenere e mantenere il "
                            "riconoscimento di cui all'art. 29, comma 1 del Codice, svolgono la "
                            "propria attività in conformità con quanto previsto dai "
                            "provvedimenti emanati dall'Agenzia ai sensi dell'art. 4, comma 2. "
                            "Fino all'emanazione di tali provvedimenti continua ad applicarsi "
                            "la deliberazione CNIPA 21 maggio 2009, n. 45, recante regole per "
                            "il riconoscimento e la verifica del documento informatico e "
                            "successive modificazioni.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Fino all'emanazione dei provvedimenti dell'Agenzia ex "
                                     "art. 4, comma 2, resta applicabile la deliberazione CNIPA "
                                     "21 maggio 2009, n. 45, e successive modificazioni.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 42 c.5",
        "testo": "I certificatori accreditati valorizzano l'estensione qcStatements "
                 "id-etsi-qcs-QcSSCD esclusivamente nei certificati qualificati la cui chiave "
                 "privata è custodita nei dispositivi di cui all'art. 12.",
        "testo_integrale": "I certificatori accreditati, al fine di ottenere e mantenere il "
                            "riconoscimento di cui all'art. 29, comma 1, del Codice assicurano "
                            "la valorizzazione dell'estensione qcStatements "
                            "id-etsi-qcs-QcSSCD esclusivamente nei certificati qualificati la "
                            "cui corrispondente chiave privata sia custodita nei dispositivi di "
                            "cui all'art. 12.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 42 c.6",
        "testo": "I sistemi di generazione e verifica delle firme qualificate e digitali "
                 "forniti o indicati dal certificatore non devono permettergli di conoscere il "
                 "contenuto del documento informatico oggetto di sottoscrizione o verifica.",
        "testo_integrale": "I sistemi di generazione e verifica delle firme elettroniche "
                            "qualificate e delle firme digitali, forniti o indicati dal "
                            "certificatore accreditato ai sensi degli articoli 11, comma 8 e "
                            "14, comma 1, non devono consentire a quest'ultimo di conoscere gli "
                            "atti o fatti rappresentati nel documento informatico oggetto del "
                            "processo di sottoscrizione o verifica.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 42 c.7",
        "testo": "Ai fini della vigilanza di cui all'art. 31 del Codice, il certificatore "
                 "consegna all'Agenzia un esemplare dei dispositivi di firma qualificata e "
                 "digitale forniti ai titolari, salvo che si tratti di dispositivi HSM.",
        "testo_integrale": "Al fine dell'attività di cui all'art. 31 del Codice, il "
                            "certificatore deve consegnare all'Agenzia un esemplare dei "
                            "dispositivi di firma elettronica qualificata e di firma digitale "
                            "forniti ai titolari. Il primo periodo non si applica in relazione "
                            "ai dispositivi di firma HSM.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Non si applica ai dispositivi di firma HSM.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 42 c.8",
        "testo": "Ai fini della vigilanza di cui all'art. 31 del Codice, il certificatore "
                 "consegna all'Agenzia copia delle applicazioni di generazione e verifica delle "
                 "firme qualificate o digitali fornite ai titolari per uso personale.",
        "testo_integrale": "Al fine dell'attività di cui all'art. 31 del Codice, il "
                            "certificatore deve consegnare all'Agenzia copia delle applicazioni "
                            "di generazione e verifica delle firme elettroniche qualificate o "
                            "delle firme digitali fornite ai titolari per uso personale.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 42 c.9",
        "testo": "Per mantenere l'accreditamento ex art. 29 del Codice, il certificatore "
                 "partecipa alle sessioni di test di interoperabilità indicate dall'Agenzia.",
        "testo_integrale": "Al fine del mantenimento dell'accreditamento di cui all'art. 29 del "
                            "Codice, il certificatore è obbligato a partecipare alle sessioni "
                            "di test di interoperabilità indicate dall'Agenzia.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 42 c.10",
        "testo": "I certificatori rendono disponibile all'Agenzia un servizio che consenta di "
                 "verificare, per un dato codice fiscale, se sia stato emesso un certificato "
                 "qualificato e la relativa scadenza; l'Agenzia, sentite le associazioni di "
                 "categoria e il Garante privacy, ne definisce con proprio provvedimento "
                 "caratteristiche, modalità e vincoli di fruizione.",
        "testo_integrale": "I certificatori rendono disponibile all'Agenzia un servizio che "
                            "consenta, ai fini dell'art. 34, comma 4, di conoscere se, per un "
                            "determinato codice fiscale, sia stato emesso un certificato "
                            "qualificato e, in caso affermativo, la sua scadenza. L'Agenzia, "
                            "sentite le associazioni di categoria e il Garante per la "
                            "protezione dei dati personali, indica in un proprio provvedimento "
                            "le caratteristiche del servizio, le modalità e i vincoli per la "
                            "sua fruizione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 43 c.1",
        "testo": "L'elenco pubblico dei certificatori accreditati tenuto dall'Agenzia contiene, "
                 "per ogni certificatore, almeno: denominazione, sede legale e relativo "
                 "indirizzo, indirizzi internet con informazioni in italiano e inglese "
                 "sull'attività svolta, lista dei certificati delle chiavi di certificazione, "
                 "indirizzo email, data di accreditamento volontario, eventuale data di "
                 "cessazione ed eventuale certificatore sostitutivo.",
        "testo_integrale": "L'elenco pubblico dei certificatori accreditati tenuto "
                            "dall'Agenzia ai sensi dell'art. 29, comma 6, del Codice, e del "
                            "decreto legislativo 1 dicembre 2009, n. 177, contiene per ogni "
                            "certificatore accreditato almeno le seguenti informazioni: "
                            "a) denominazione; b) sede legale; c) indirizzo della sede legale; "
                            "d) indirizzi internet ove il certificatore pubblica in lingua "
                            "italiana e lingua inglese informazioni inerenti all'attività "
                            "svolta; e) lista dei certificati delle chiavi di certificazione; "
                            "f) indirizzo di posta elettronica; g) data di accreditamento "
                            "volontario; h) eventuale data di cessazione; i) eventuale "
                            "certificatore sostitutivo.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 43 c.2",
        "testo": "L'Agenzia sottoscrive e rende disponibile per via telematica l'elenco "
                 "pubblico, per verificare le firme qualificate e digitali e diffondere i dati "
                 "dei certificatori; chi lo consulta può usare le informazioni solo per le "
                 "finalità consentite dalla legge; l'Agenzia ne stabilisce il formato con "
                 "propria deliberazione.",
        "testo_integrale": "L'elenco pubblico è sottoscritto e reso disponibile per via "
                            "telematica dall'Agenzia al fine di verificare le firme "
                            "elettroniche qualificate e digitali e diffondere i dati dei "
                            "certificatori accreditati. Tali informazioni sono utilizzate, da "
                            "chi le consulta, solo per le finalità consentite dalla legge. "
                            "L'Agenzia stabilisce il formato dell'elenco pubblico attraverso "
                            "propria deliberazione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 43 c.3",
        "testo": "L'elenco pubblico è sottoscritto elettronicamente dal Presidente "
                 "dell'Agenzia o da soggetti da lui designati.",
        "testo_integrale": "L'elenco pubblico è sottoscritto elettronicamente dal Presidente "
                            "dell'Agenzia o dai soggetti da lui designati.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 43 c.4",
        "testo": "L'Agenzia pubblica sul proprio sito istituzionale i manuali operativi, "
                 "sottoscritti secondo le modalità del comma 3.",
        "testo_integrale": "L'Agenzia pubblica sul proprio sito istituzionale i manuali "
                            "operativi di cui all'art. 40, sottoscritti ai sensi del comma 3.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 43 c.5",
        "testo": "Nella Gazzetta Ufficiale è dato avviso: dei soggetti preposti alla "
                 "sottoscrizione dell'elenco pubblico; del valore dei codici identificativi del "
                 "certificato delle chiavi di sottoscrizione dell'elenco; con almeno sessanta "
                 "giorni di preavviso, della sostituzione di tali chiavi in scadenza; della "
                 "revoca dei certificati di sottoscrizione dell'elenco per ragioni di "
                 "sicurezza.",
        "testo_integrale": "Nella Gazzetta Ufficiale della Repubblica italiana è dato avviso: "
                            "a) dell'indicazione dei soggetti preposti alla sottoscrizione "
                            "dell'elenco pubblico di cui al comma 3; b) del valore dei codici "
                            "identificativi del certificato relativo alle chiavi utilizzate per "
                            "la sottoscrizione dell'elenco pubblico, generati attraverso gli "
                            "algoritmi di cui all'art. 4; c) con almeno sessanta giorni di "
                            "preavviso rispetto alla scadenza del certificato, della "
                            "sostituzione delle chiavi utilizzate per la sottoscrizione "
                            "dell'elenco pubblico; d) della revoca dei certificati utilizzati "
                            "per la sottoscrizione dell'elenco pubblico sopravvenuta per "
                            "ragioni di sicurezza.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 44 c.1",
        "testo": "Il certificatore indica nel manuale operativo i formati del documento "
                 "informatico e le modalità operative che il titolare deve seguire per evitare "
                 "le conseguenze previste dall'art. 4, comma 3.",
        "testo_integrale": "Il certificatore indica nel manuale operativo i formati del "
                            "documento informatico e le modalità operative a cui il titolare "
                            "deve attenersi per evitare le conseguenze previste dall'art. 4, "
                            "comma 3.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 45 c.1",
        "testo": "Su richiesta del titolare, del terzo interessato o dell'Agenzia, il "
                 "certificatore inserisce nel certificato qualificato le eventuali limitazioni "
                 "d'uso.",
        "testo_integrale": "Il certificatore, su richiesta del titolare, del terzo interessato "
                            "o dell'Agenzia, è tenuto a inserire nel certificato qualificato "
                            "eventuali limitazioni d'uso.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Su richiesta del titolare, del terzo interessato o "
                                     "dell'Agenzia.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 45 c.2",
        "testo": "L'Agenzia definisce, con proprio provvedimento, le modalità di "
                 "rappresentazione dei limiti d'uso e di valore di cui all'art. 28, comma 3, "
                 "del Codice.",
        "testo_integrale": "La modalità di rappresentazione dei limiti d'uso e di valore di "
                            "cui all'art. 28, comma 3, del Codice è definita dall'Agenzia con "
                            "uno dei provvedimenti di cui all'art. 4, comma 2.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 45 c.3",
        "testo": "Il certificatore indica, in italiano e in inglese, la limitazione d'uso dei "
                 "certificati utilizzati per la verifica delle firme di cui all'art. 35, "
                 "comma 3, del Codice.",
        "testo_integrale": "Il certificatore è tenuto ad indicare, in lingua italiana e lingua "
                            "inglese, la limitazione d'uso dei certificati utilizzati per la "
                            "verifica delle firme di cui all'art. 35, comma 3, del Codice.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 46 c.1",
        "testo": "I certificatori accreditati forniscono o indicano almeno un sistema, "
                 "conforme al comma 2, che consenta di verificare le marche temporali.",
        "testo_integrale": "I certificatori accreditati forniscono ovvero indicano almeno un "
                            "sistema, conforme al successivo comma 2, che consenta di "
                            "effettuare la verifica delle marche temporali.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 46 c.2",
        "testo": "L'Agenzia, con i propri provvedimenti, stabilisce le regole di "
                 "interoperabilità per la verifica della marca temporale, anche quando "
                 "associata al documento informatico cui si riferisce.",
        "testo_integrale": "L'Agenzia con i provvedimenti di cui all'art. 4, comma 2, "
                            "stabilisce le regole di interoperabilità per la verifica della "
                            "marca temporale, anche associata al documento informatico cui si "
                            "riferisce.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terzi affidanti/pubblico", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = [
    "art. 42 c.1",
    "art. 42 c.2",
    "art. 42 c.3",
    "art. 42 c.4",
    "art. 42 c.5",
    "art. 42 c.6",
    "art. 42 c.7",
    "art. 42 c.8",
    "art. 42 c.9",
    "art. 42 c.10",
    "art. 43 c.1",
    "art. 43 c.1 lett.a",
    "art. 43 c.1 lett.b",
    "art. 43 c.1 lett.c",
    "art. 43 c.1 lett.d",
    "art. 43 c.1 lett.e",
    "art. 43 c.1 lett.f",
    "art. 43 c.1 lett.g",
    "art. 43 c.1 lett.h",
    "art. 43 c.1 lett.i",
    "art. 43 c.2",
    "art. 43 c.3",
    "art. 43 c.4",
    "art. 43 c.5",
    "art. 43 c.5 lett.a",
    "art. 43 c.5 lett.b",
    "art. 43 c.5 lett.c",
    "art. 43 c.5 lett.d",
    "art. 44 c.1",
    "art. 45 c.1",
    "art. 45 c.2",
    "art. 45 c.3",
    "art. 46 c.1",
    "art. 46 c.2",
]

MAPPATURA_LOCALE = {
    "art. 42 c.1": ["art. 42 c.1"],
    "art. 42 c.2": ["art. 42 c.2"],
    "art. 42 c.3": ["art. 42 c.3"],
    "art. 42 c.4": ["art. 42 c.4"],
    "art. 42 c.5": ["art. 42 c.5"],
    "art. 42 c.6": ["art. 42 c.6"],
    "art. 42 c.7": ["art. 42 c.7"],
    "art. 42 c.8": ["art. 42 c.8"],
    "art. 42 c.9": ["art. 42 c.9"],
    "art. 42 c.10": ["art. 42 c.10"],
    "art. 43 c.1": [
        "art. 43 c.1",
        "art. 43 c.1 lett.a",
        "art. 43 c.1 lett.b",
        "art. 43 c.1 lett.c",
        "art. 43 c.1 lett.d",
        "art. 43 c.1 lett.e",
        "art. 43 c.1 lett.f",
        "art. 43 c.1 lett.g",
        "art. 43 c.1 lett.h",
        "art. 43 c.1 lett.i",
    ],
    "art. 43 c.2": ["art. 43 c.2"],
    "art. 43 c.3": ["art. 43 c.3"],
    "art. 43 c.4": ["art. 43 c.4"],
    "art. 43 c.5": [
        "art. 43 c.5",
        "art. 43 c.5 lett.a",
        "art. 43 c.5 lett.b",
        "art. 43 c.5 lett.c",
        "art. 43 c.5 lett.d",
    ],
    "art. 44 c.1": ["art. 44 c.1"],
    "art. 45 c.1": ["art. 45 c.1"],
    "art. 45 c.2": ["art. 45 c.2"],
    "art. 45 c.3": ["art. 45 c.3"],
    "art. 46 c.1": ["art. 46 c.1"],
    "art. 46 c.2": ["art. 46 c.2"],
}

RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "art. 42 c.3"),
        "nodo_a": ("obbligo", None, "art. 43 c.1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 43 c.4"),
        "nodo_a": ("obbligo", None, "art. 43 c.3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 43 c.5"),
        "nodo_a": ("obbligo", None, "art. 43 c.3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 46 c.1"),
        "nodo_a": ("obbligo", None, "art. 46 c.2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
