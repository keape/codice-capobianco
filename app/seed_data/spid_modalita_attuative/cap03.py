"""Regolamento AgID recante le modalità attuative per la realizzazione dello
SPID (art. 4 comma 2 DPCM 24/10/2014), v2.0 (22/07/2016), consolidato con
Avviso AgID n.10/2018 e Determinazione AgID n.425/2020 — CAPO IV "Utilizzo
di SPID" (artt. 25-29) e Sezione V "Monitoraggio e convenzioni" (artt. 30,
30-bis, 31).

Estrazione granulare ADR-0007 dal testo ufficiale consolidato (fonte:
app/.source_cache/spid_modalita_attuative/cap03.txt).

Note di modellazione:

- Granularità: a differenza di altri capitoli SPID (es.
  app/seed_data/spid/cap01.py, indicizzato a livello di comma/lettera),
  l'assegnazione di questo modulo fissa esplicitamente
  INDICE_ARTICOLI_LOCALE a livello di intero articolo (8 item, uno per
  art. 25-29, 30, 30-bis, 31): questi articoli sono prosa normativa
  continua priva di commi/lettere autonomamente scindibili (fanno
  eccezione le liste numerate interne, es. i 6 passaggi dell'art. 25 o le
  5 categorie di disservizio dell'art. 30, che sono passaggi/voci di
  un'unica procedura descritta dall'articolo e non prescrizioni autonome
  separabili). Ogni articolo riceve quindi esattamente una riga
  (Obbligo o Principio), con `testo_integrale` pari al testo verbatim
  completo dell'intero articolo (tutti i paragrafi, comprese liste
  numerate e la tabella di classificazione dei disservizi dell'art. 30,
  riportata per intero in forma testuale leggibile).

- Art. 25 (Autenticazione) e art. 26 (Registro SPID) descrivono un
  processo/oggetto di sistema senza imporre un comportamento vincolato a
  un soggetto individuabile in senso stretto (sono descrizioni tecniche
  del funzionamento del protocollo SAML e della funzione del registro):
  modellati come Principio di tipo "definitorio", sul modello già
  adottato per le definizioni tecniche in app/seed_data/spid/cap01.py.

- Art. 27, 28, 29, 30, 30-bis, 31 impongono invece comportamenti vincolati
  a soggetti individuabili (fornitori di servizi, gestori dell'identità
  digitale) e sono modellati come Obbligo. L'art. 31 (Convenzioni) è
  interamente rivolto all'attività regolamentare di AgID, che non compare
  tra le categorie di soggetto del censimento: è quindi un Obbligo senza
  chiave `soggetti`, sullo stesso pattern già usato in
  app/seed_data/spid/cap01.py per le norme indirizzate esclusivamente ad
  AgID.

- I riferimenti incrociati agli articoli del DPCM 24/10/2014 presenti nel
  testo (es. art. 29 "Il comma 2 dell'articolo 13 del DPCM...", art. 30
  "ai sensi dell'articolo 12, comma 4 del DPCM", art. 30-bis "di cui
  all'articolo 4, comma 1, lett. b), del DPCM"/"dell'articolo 3, comma 1,
  lett. a), b) e c) del DPCM"/"dell'art. 11, comma 1, lett. o) del DPCM")
  sono rinvii verso un'ALTRA Fonte (DPCM 24/10/2014, fonte_id=5) e non
  vengono tradotti in RELAZIONI in questo modulo, come da istruzioni per
  l'import granulare (nessun tentativo cross-fonte in questa fase; il
  collegamento a posteriori DPCM modalità attuative -> DPCM 24/10/2014
  resta lavoro futuro secondo la pipeline ADR-0009). Sono invece
  modellati i rinvii testuali espliciti interni a questo stesso testo
  (es. art. 25 -> art. 27 per le modalità di richiesta/impiego degli
  attributi, art. 25 e art. 27 -> art. 26 per il Registro SPID).

Nessuna relazione verso gli altri capitoli di questa stessa fonte
(cap01, cap02, cap04) è tentata in questo modulo: non essendo certo il
riferimento esatto usato dai capitoli paralleli, si preferisce ometterle
piuttosto che rischiare un riferimento inesistente nel registro
condiviso.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 27 (Uso degli attributi SPID)",
        "testo": "I fornitori di servizi richiedono ai gestori dell'identità digitale solo gli attributi minimi e pertinenti per l'accesso al servizio, li mantengono solo per il tempo necessario e assolvono agli obblighi di informativa verso l'utente previsti dal Codice privacy; per gli attributi qualificati si rivolgono, tramite il Registro SPID, ai relativi gestori.",
        "testo_integrale": "I fornitori di servizi, per verificare le policy di sicurezza relativi all'accesso ai servizi da essi erogati potrebbero avere necessità di informazioni relative ad attributi riferibili ai soggetti richiedenti. Tali policy dovranno essere concepite in modo da richiedere per la verifica il set minimo di attributi pertinenti e non eccedenti le necessità effettive del servizio offerto e mantenuti per il tempo strettamente necessario alla verifica stessa, come previsto dall'articolo 11 del decreto legislativo n. 196 del 2003. I fornitori di servizio dovranno segnalare ai gestori delle identità quali attributi identificativi e secondari dovranno essere attestati con l'asserzione emessa a seguito dell'autenticazione dei soggetti richiedenti i servizi. I gestori dell'identità, al momento dell'autenticazione e prima di emettere l'asserzione, devono ottemperare all'obbligo di informativa di cui all'articolo 13 del decreto legislativo n. 196 del 2003. Nel caso in cui per l'applicazione delle policy di accesso relative al servizio invocato si rendesse necessaria la verifica di attributi qualificati riferibili al richiedente, i fornitori di servizio si rivolgeranno ai gestori degli attributi qualificati in grado di certificare tali attributi, individuabili attraverso il registro SPID. Per far ciò, prima di procedere, ai sensi del comma 2 dell'articolo 13 del DPCM, danno evidenza all'utente degli attributi qualificati necessari in ottemperanza all'obbligo di informativa di cui all'articolo 13 del decreto legislativo n. 196 del 2003.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 28 (Gestione delle sessioni di autenticazione)",
        "testo": "Il gestore dell'identità digitale garantisce la cifratura del canale di comunicazione e indica le versioni minime di browser supportate; per il livello 1 SPID è ammessa una sessione di autenticazione condivisa tra più fornitori di servizi (con obbligo di informativa e logout), mentre per i livelli 2 e 3 non sono ammesse sessioni condivise e ciascun fornitore gestisce autonomamente la propria sessione con l'utente.",
        "testo_integrale": "Il modello di gestione delle sessioni di autenticazione in SPID si differenzia a seconda del livello SPID con il quale viene instaurato un contesto di autenticazione. Inoltre per la sicurezza del canale di comunicazione tra utente e gestore è necessario che il gestore IdP garantisca la cifratura mediante l'adozione di meccanismi standard e protocolli aggiornati alle versioni più recenti e renda possibile l'utilizzo delle funzionalità di accesso web mediante le tipologie di browser più diffuse ma con limitazioni per le versioni più obsolete indicando le versioni minime necessarie per accedere al servizio SPID nel Manuale Operativo e nella Guida Utente. Per particolari esigenze, può essere temporaneamente consentito l'uso di versioni precedenti di meccanismi e protocolli se preventivamente autorizzati dalla Agenzia e nei termini da questa indicati.\n\nA) Gestione delle sessioni per il livello 1 SPID\n\nPer il livello 1 SPID è ammessa l'instaurazione di una sessione di autenticazione, associata ad un determinato utente titolare di identità digitale, mantenuta dal gestore dell'identità digitale e condivisa da tutti i fornitori di servizio che nel corso di vita della sessione stessa erogano servizi per quel determinato utente. Per ogni nuovo fornitore di servizi che si aggiunge al contesto di autenticazione, il gestore dell'identità digitale dovrà dare informativa all'utente ai sensi dell'articolo 13 del decreto legislativo n. 196 del 2003. Il fornitore di servizi che condivide una sessione di autenticazione di un dato gestore di identità digitale, può instaurare con l'utente una sessione finalizzata al solo accesso al servizio richiesto e per questa sessione deve fornire meccanismi espliciti per il logout dell'utente. Per la chiusura della sessione comune è previsto un meccanismo logout globale secondo il single logout profile di SAML (cfr par. 4.4 del documento Profiles for the OASIS Security Assertion Markup Language (SAML) V2.0).\n\nB) Gestione delle sessioni per i livelli 2 e 3 SPID\n\nPer i livelli 2 e 3 SPID, allo scopo di garantire la massima sicurezza e stabilità del sistema, non si prevede la possibilità di mantenimento di sessioni condivise di autenticazione. Pertanto:\n\n1) il gestore dell'identità digitale non deve mantenere alcuna sessione di autenticazione con l'utente;\n2) ogni fornitore di servizi deve gestire per proprio conto l'eventuale sessione con l'utente. Per la chiusura dovranno essere forniti meccanismi espliciti per il logout.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 29 (Tracciatura e conservazione della documentazione di riscontro)",
        "testo": "I fornitori di servizi conservano per ventiquattro mesi le registrazioni (richiesta e asserzione SAML) necessarie a imputare le operazioni alle singole identità digitali, garantendo riservatezza, inalterabilità, integrità e cifratura; analogo registro delle transazioni è tenuto dal gestore dell'identità digitale, con separazione obbligatoria tra i due registri quando lo stesso soggetto riveste entrambi i ruoli.",
        "testo_integrale": "Il comma 2 dell'articolo 13 del DPCM obbliga i fornitori di servizi alla conservazione per ventiquattro mesi delle informazioni necessarie a imputare alle singole identità digitali le operazioni effettuate sui propri sistemi. Tali informazioni saranno costituite da registrazioni composte dal messaggio SAML di richiesta di autenticazione e della relativa asserzione emessa dal gestore delle identità. Tali messaggi riportano identificativi e date di emissione e sono firmati, rispettivamente, dallo stesso fornitore di servizi e dal gestore dell'identità digitale; quest'ultima caratteristica fornisce le necessarie garanzie di integrità e non ripudio. L'insieme delle Registrazioni costituisce il Registro delle transazioni del fornitore del servizio. Le tracciature devono avere caratteristiche di riservatezza, inalterabilità e integrità e sono conservate adottando idonee misure di sicurezza ai sensi dell'articolo 31 del decreto legislativo 30 giugno 2003, n. 196, sotto la responsabilità del titolare del trattamento; l'accesso ai dati è riservato a personale espressamente autorizzato e incaricato del trattamento dei dati personali. Devono essere utilizzati meccanismi di cifratura. Analogo registro dovrà essere tenuto dal gestore delle identità digitali, secondo modalità definite nelle regole tecniche di cui all'articolo 4, comma 3 del DPCM. Nel caso in cui uno stesso soggetto sia, allo stesso tempo, gestore dell'identità digitale e fornitore di servizi devono essere mantenuti separati i registri di tracciatura delle transazioni così come le banche dati relative alla gestione delle identità digitali. Tale vincolo di separazione deve essere applicato anche nei confronti degli accessi degli operatori di help desk e nella gestione di cruscotti di self-caring.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "condizione_applicabilita": "conservazione delle registrazioni per ventiquattro mesi",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 30 (Monitoraggio di AGID sul sistema SPID)",
        "testo": "AgID monitora il sistema SPID e i gestori dell'identità digitale sono tenuti a comunicarle incidenti di sicurezza, soddisfazione dei clienti, servizi aggiuntivi e disservizi (classificati in 5 categorie con codici A/B a seconda che siano rilevati dal gestore o da terzi), entro trenta minuti o due ore a seconda della gravità, oltre a dati statistici bimestrali; in caso di inadempienza AgID può contestare le violazioni e revocare l'accreditamento.",
        "testo_integrale": "L'Agenzia svolge funzioni di monitoraggio, anche sulla base delle segnalazioni fatte dai cittadini, allo scopo di valutare e garantire usabilità, accessibilità e corretto utilizzo degli elementi identificativi SPID e indica le migliori pratiche da adottare. Ai fini dell'attività di vigilanza, i gestori di identità digitali rendono disponibili all'Agenzia:\n\n1) gli incidenti di sicurezza rilevati;\n2) le informazioni circa il livello di soddisfazione dei propri clienti;\n3) le caratteristiche di eventuali servizi aggiuntivi offerti;\n4) le informazioni relative a disservizi, secondo la classificazione e le modalità riportate nella tabella seguente.\n\nClassificazione dei disservizi in relazione agli effetti prodotti e relativi codici identificativi:\n\n1. Comportamento anomalo e non circoscritto: comportamento difforme dalle regole tecniche per il quale non è circoscritto il potenziale impatto (codice 1A, se rilevato dal gestore; codice 1B, se rilevato da terzi).\n2. Comportamento anomalo circoscritto: comportamento difforme dalle regole tecniche per il quale è circoscritto il potenziale impatto (codice 2A, se rilevato dal gestore; codice 2B, se rilevato da terzi).\n3. Malfunzionamento bloccante: tipologia di malfunzionamento a causa del quale le funzionalità del sistema del gestore delle identità digitali, come definite nelle regole tecniche, non possono essere utilizzate in tutto o in parte consistente dagli utenti (codice 3A, se rilevato dal gestore; codice 3B, se rilevato da terzi).\n4. Malfunzionamento grave: tipologia di malfunzionamento a causa del quale in alcune circostanze le funzionalità del sistema del gestore delle identità digitali, come definite nelle regole tecniche, possono essere utilizzate parzialmente dagli utenti (codice 4A, se rilevato dal gestore; codice 4B, se rilevato da terzi).\n5. Malfunzionamento: situazione a causa della quale le funzionalità del sistema del gestore delle identità digitali, come definite nelle regole tecniche, in tutto o in parte, risultano degradate ovvero il sistema ha un comportamento anomalo in situazioni circoscritte e per funzionalità secondarie (codice 5A, se rilevato dal gestore; codice 5B, se rilevato da terzi).\n\nI gestori dell'identità digitale hanno l'obbligo di comunicare all'Agenzia, entro trenta minuti dalla rilevazione dell'evento stesso, i disservizi contraddistinti da uno dei seguenti codici: 1A, 1B, 2A, 2B, 3A, 3B ed entro due ore i disservizi contraddistinti dai codici 4A, 4B, 5A e 5B.\n\nLa comunicazione deve fornire anche una prima valutazione dell'incidente, le eventuali misure adottate al riguardo e la tempistica prevista per il ripristino della normale operatività.\n\nA seguito delle risultanze dell'attività di monitoraggio e della rilevanza/frequenza dei disservizi, nell'ipotesi di inosservanza di uno o più degli obblighi posti a carico del gestore delle identità digitali, l'Agenzia in esito all'accertamento contesta le violazioni disponendo l'eventuale sospensione, prescrivendo le attività da porre in essere per l'adeguamento da parte del gestore, indicando nel contempo il termine entro il quale il gestore stesso deve conformarsi agli obblighi previsti. Qualora il gestore non provveda in tal senso nei tempi indicati, l'Agenzia, con provvedimento motivato notificato all'interessato, adotta, nei casi più gravi, un provvedimento di revoca dell'accreditamento ai sensi dell'articolo 12, comma 4 del DPCM.\n\nI gestori delle identità digitali inviano all'Agenzia, con cadenza almeno bimestrale, i dati statistici relativi all'utilizzo del sistema, le metriche quantitative e qualitative che saranno definite e concordate a valle dello start up di SPID.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 30-bis (Collaborazione fra AGID ed il Garante per la protezione dei dati personali)",
        "testo": "AgID e Garante privacy collaborano nella vigilanza sui soggetti SPID: AgID segnala al Garante possibili violazioni della normativa privacy riscontrate nell'attività di vigilanza, il Garante effettua audit di sicurezza anche a campione, e i gestori dell'identità digitale devono comunicare al Garante (e per conoscenza ad AgID) le violazioni di dati personali entro 24 ore (comunicazione sommaria) e 3 giorni (comunicazione dettagliata), oltre a informare gli interessati quando vi sia pregiudizio; Garante e AgID stipulano un protocollo d'intesa attuativo.",
        "testo_integrale": "Nell'ambito dell'attività di vigilanza di cui all'articolo 4, comma 1, lett. b), del DPCM sull'operato dei soggetti che partecipano a SPID, l'AGID ove riscontri casi in cui sussistano elementi per ritenere la violazione della normativa in materia di protezione dei dati personali, ne informa tempestivamente il garante per la protezione dei dati personali.\n\nIl Garante, anche sulla base delle informazioni di cui sopra o di quelle concernenti violazioni di dati personali di cui all'articolo 4, comma 3 lett. g-bis, del decreto legislativo 30 giugno 2003 n. 196, eventualmente ricevute ai sensi dell'art. 11, comma 1, lett. o) del DPCM, sottopone a un audit di sicurezza, anche a campione, i soggetti partecipanti allo SPID di cui all'articolo 3, comma 1, lett. a), b) e c) del DPCM, tenuto conto delle diverse categorie dei soggetti interessati. I risultati dell'audit sono inseriti nella relazione annuale del Garante.\n\nI gestori dell'identità digitale comunicano al garante, e per conoscenza all'AGID, la violazione dei dati personali di cui sopra entro 24 ore dell'avvenuta conoscenza della violazione per la prima sommaria comunicazione ed entro 3 giorni dalla stessa per una comunicazione dettagliata. La comunicazione è effettuata mediante apposito modello predisposto dal garante e disponibile on line sul sito dell'autorità. Qualora si verifichi una violazione di dati personali e dalla stessa possa derivare un pregiudizio ai dati personali o alla riservatezza di un utente o di altre persone, ossia dei soggetti cui si riferiscono i dati violati, oltre alla comunicazione al Garante i gestori sono tenuti a comunicare l'avvenuta violazione, senza ritardo, anche a tali soggetti, utilizzando il modello predisposto da Garante. Si applicano, in quanto compatibili, le disposizioni di cui al provvedimento in materia di attuazione della disciplina sulla comunicazione delle violazioni di dati personali (c.d. data breach) adottato dal Garante il 4 aprile 2013 e pubblicato sulla gazzetta ufficiale n.97 del 4 aprile 2013.\n\nIl Garante e l'AGID stipulano un protocollo di intesa per l'attuazione delle disposizioni del presente articolo nel rispetto delle rispettive competenze.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 31 (Convenzioni)",
        "testo": "Gli schemi di convenzione tra AgID e, rispettivamente, i gestori dell'identità digitale/pubbliche amministrazioni fornitrici di servizi e i gestori di attributi qualificati/fornitori di servizi privati sono definiti con appositi regolamenti emanati da AgID.",
        "testo_integrale": "Gli schemi di convenzione per i gestori dell'identità digitale e per le pubbliche amministrazioni in qualità di fornitori di servizi sono definiti nell'ambito di specifici regolamenti emanati dall'Agenzia.\n\nGli schemi di convenzione per i gestori degli attributi qualificati e per i fornitori di servizi privati sono definiti nell'ambito di specifici regolamenti emanati dall'Agenzia.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 25 (Autenticazione)",
        "testo": "Descrive il processo di autenticazione SPID basato sul modello federato SAML (OASIS): il fornitore di servizi individua il gestore dell'identità digitale scelto dall'utente, richiede l'autenticazione al livello SPID necessario, riceve l'asserzione SAML emessa dal gestore (ed eventualmente dal gestore di attributi qualificati) e decide se consentire l'accesso al servizio, secondo il profilo Web Browser SSO in modalità SP-Initiated.",
        "testo_integrale": "L'autenticazione è il processo in cui l'utente, usando le proprie credenziali SPID, dimostra la propria identità al gestore dell'identità digitale al fine di accedere a servizi disponibili in rete. Per la realizzazione del processo di autenticazione, SPID adotta il modello federato delle identità digitali definito dalle specifiche SAML emesse dal consorzio OASIS (cfr Regole Tecniche SPID).\n\nLe relazioni tra i soggetti coinvolti nel processo (l'utente, il gestore dell'identità digitale, il fornitore di servizi ed, eventualmente, il gestore di attributi qualificati) si evidenziano nelle interazioni necessarie al completamento delle attività che, a partire da una richiesta avanzata dal soggetto titolare di una identità digitale, portano all'autorizzazione o al diniego della fruizione di un servizio erogato da un fornitore di servizi. Tali interazioni determinano la produzione di certificazioni (Asserzioni nella nomenclatura SAML) da parte dei gestori delle Identità digitali ed, eventualmente, dei gestori di attributi qualificati, e l'utilizzo delle stesse da parte dei fornitori di servizi.\n\nI passaggi previsti sono i seguenti:\n\n1) il titolare dell'identità digitale richiede l'accesso ad un servizio collegandosi telematicamente al portale del fornitore di servizi; il fornitore dei servizi, per poter procedere, deve individuare il gestore dell'Identità digitale in grado di autenticare il soggetto richiedente. Per far ciò il fornitore dei servizi chiede indicazioni allo stesso utente, ad esempio, facendo scegliere il proprio gestore dell'identità digitale da un elenco riportante tutti i gestori di identità aderenti a SPID;\n2) il fornitore dei servizi indirizza il soggetto titolare dell'identità digitale presso il gestore dell'identità digitale, individuato al passaggio precedente, richiedendo l'autenticazione con il livello SPID associato al servizio richiesto e l'eventuale attestazione di attributi necessari per l'autorizzazione all'accesso;\n3) il gestore dell'identità digitale verifica l'identità del soggetto sulla base di credenziali fornite dallo stesso. Se tale verifica ha esito positivo viene emessa, ad uso del fornitore dei servizi, una asserzione di autenticazione SAML attestante gli attributi eventualmente richiesti; le modalità per la richiesta e l'impiego degli attributi deve avvenire secondo quanto specificato al successivo art. 27;\n4) il titolare dell'identità digitale viene quindi reindirizzato, portando con sé l'asserzione prodotta, verso il fornitore dei servizi;\n5) il fornitore dei servizi può, a questo punto, avere la necessità di verificare attributi qualificati riferibili all'utente qualora questi fossero richiesti dalle policy di sicurezza che regolano l'accesso al servizio. In questo caso:\na) individuati, per il tramite del registro SPID, i gestori di attributi qualificati in grado di certificare gli attributi necessari, inoltra agli stessi una richiesta di attestazione presentando i riferimenti dell'identità digitale per la quale si richiede la verifica;\nb) il risultato della richiesta è l'emissione, da parte del gestore di attributi qualificati, di una asserzione SAML;\n6) il fornitore dei servizi, raccolte tutte le necessarie asserzioni SAML, verifica le policy di accesso al servizio richiesto e decide se accettare o rigettare la richiesta.\n\nIl protocollo descritto viene realizzato secondo il profilo \"Web Browser SSO\" dello standard SAML, nella modalità cosiddetta \"SP-Initiated\" e nelle versioni \"Redirect/POST binding\" e \"POST/POST binding\". Tale modalità prevede che il processo di autenticazione sia innescato dalla richiesta operata dall'utente, tramite il suo web browser, presso il sito del fornitore di servizi, il quale, a sua volta, si rivolge al gestore dell'identità inoltrando una richiesta di autenticazione SAML basata sul costrutto <AuthnRequest> e usando il binding HTTP Redirect o il binding HTTP POST.\n\nLa relativa risposta SAML, basata sul costrutto <Response>, veicolante una asserzione di autenticazione, viene restituita al richiedente tramite il binding HTTP POST.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 26 (Registro SPID)",
        "testo": "Il Registro SPID, tenuto da AgID, elenca i soggetti convenzionati che operano nello SPID e certifica la relazione di fiducia tra loro, basata sulla condivisione dei criteri di sicurezza e delle regole di interoperabilità SPID.",
        "testo_integrale": "Il Registro SPID contiene le informazioni relative ai soggetti che hanno in corso un'apposita convenzione con AgID per operare nell'ambito dello SPID ed assolve la funzione di registro di federazione, certificando la relazione di fiducia stabilita tra i soggetti appartenenti a SPID. Tale relazione di fiducia si fonda nella condivisione dei criteri di sicurezza e delle regole di interoperabilità previste da SPID.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 25 (Autenticazione)",
    "art. 26 (Registro SPID)",
    "art. 27 (Uso degli attributi SPID)",
    "art. 28 (Gestione delle sessioni di autenticazione)",
    "art. 29 (Tracciatura e conservazione della documentazione di riscontro)",
    "art. 30 (Monitoraggio di AGID sul sistema SPID)",
    "art. 30-bis (Collaborazione fra AGID ed il Garante per la protezione dei dati personali)",
    "art. 31 (Convenzioni)",
]

MAPPATURA_LOCALE = {
    "art. 25 (Autenticazione)": ["art. 25 (Autenticazione)"],
    "art. 26 (Registro SPID)": ["art. 26 (Registro SPID)"],
    "art. 27 (Uso degli attributi SPID)": ["art. 27 (Uso degli attributi SPID)"],
    "art. 28 (Gestione delle sessioni di autenticazione)": [
        "art. 28 (Gestione delle sessioni di autenticazione)"
    ],
    "art. 29 (Tracciatura e conservazione della documentazione di riscontro)": [
        "art. 29 (Tracciatura e conservazione della documentazione di riscontro)"
    ],
    "art. 30 (Monitoraggio di AGID sul sistema SPID)": [
        "art. 30 (Monitoraggio di AGID sul sistema SPID)"
    ],
    "art. 30-bis (Collaborazione fra AGID ed il Garante per la protezione dei dati personali)": [
        "art. 30-bis (Collaborazione fra AGID ed il Garante per la protezione dei dati personali)"
    ],
    "art. 31 (Convenzioni)": ["art. 31 (Convenzioni)"],
}

RELAZIONI = [
    {
        "nodo_da": ("principio", None, "art. 25 (Autenticazione)"),
        "nodo_a": ("obbligo", None, "art. 27 (Uso degli attributi SPID)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", None, "art. 25 (Autenticazione)"),
        "nodo_a": ("principio", None, "art. 26 (Registro SPID)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "art. 27 (Uso degli attributi SPID)"),
        "nodo_a": ("principio", None, "art. 26 (Registro SPID)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "art. 30-bis (Collaborazione fra AGID ed il Garante per la protezione dei dati personali)"),
        "nodo_a": ("obbligo", None, "art. 30 (Monitoraggio di AGID sul sistema SPID)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.6,
    },
]
