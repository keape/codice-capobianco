"""Regolamento AgID recante le modalità attuative per la realizzazione dello
SPID (art. 4 c.2 DPCM 24/10/2014), v2.0 (22/07/2016) - Appendici A-D:
allegati tecnici integranti del regolamento, esplicitamente richiamati da
più articoli del corpo normativo (es. art. 2, art. 12, art. 15, art. 21
rinviano ad Appendice A/B/C).

Estrazione granulare ADR-0007 dal testo ufficiale consolidato (fonte:
app/.source_cache/spid_modalita_attuative/cap04.txt, pagine finali del
documento, "Stato: Emanato Versione: 2").

Note di modellazione:

- Le quattro Appendici (A: criteri di attribuzione dei livelli di
  sicurezza dei servizi; B: minacce associate al ciclo di vita delle
  identità digitali; C: tassonomia dei tipi di token; D: usabilità e
  accessibilità) non sono articoli del regolamento ma contenuto
  tecnico-descrittivo integrante, privo di soggetto obbligato diretto e
  privo di un comportamento prescritto in senso stretto (nessun "deve"
  rivolto a un soggetto censito che non sia già coperto dall'articolo che
  rinvia all'appendice) — sono quindi modellate come Principio di tipo
  "definitorio" (contenuto tecnico che definisce criteri/tassonomie/soglie
  richiamati per relationem dagli articoli sostanziali), un nodo per
  appendice, seguendo lo stesso criterio già applicato in
  app/seed_data/spid/cap01.py per le definizioni dell'art. 1.

- L'Appendice D contiene due prescrizioni comportamentali in forma
  elencativa ("i fornitori di servizi e i gestori delle identità digitali
  devono garantire: l'usabilità...; l'accessibilità...") che a rigore
  configurerebbero un Obbligo organizzativo sui due soggetti indicati; si è
  scelto comunque di mantenere l'intera Appendice D come un unico nodo
  Principio "definitorio" (non scissa in una riga Obbligo separata) per
  coerenza con le altre tre appendici, che sono tutte contenuto di cornice
  tecnica dello stesso rango documentale (allegati, non articolato), e
  perché il contenuto in senso stretto normativo/prescrittivo su usabilità
  e accessibilità è già ripreso nel corpo articolato dal rinvio esplicito
  dell'articolo di riferimento (coperto dal capitolo che modella quella
  parte del regolamento) — l'appendice stessa resta descrittiva delle
  modalità con cui tale obbligo va soddisfatto, non lo istituisce essa
  stessa.

- Le tabelle presenti in Appendice A (Impatto Potenziale/Livello di
  Sicurezza SPID; Classificazione dato/Tipo di accesso) e Appendice B
  (Minacce nel processo di registrazione; Minacce/Processo di emissione;
  Minacce/Tipo token) sono riportate in `testo_integrale` in forma
  testuale strutturata riga per riga ("Voce — valore per colonna"),
  seguendo il criterio ADR-0010 (mai omesse né troncate, ma nemmeno
  richiesto un markup tabellare che il modello dati non prevede).

- Relazioni verso il resto del regolamento: art. 2 (riferimento esatto
  "art. 2", Principio "definitorio" nel capitolo cap01 di questa stessa
  fonte — copre l'intero articolo incluso il rinvio ai 3 livelli di
  sicurezza/LoA e il rimando all'Appendice A, confermato dal subagent
  responsabile di cap01 via coordinamento hub) richiama l'Appendice A per
  i criteri di attribuzione dei livelli di sicurezza; art. 12 (riferimento
  esatto "art. 12", Obbligo procedurale nel capitolo cap01 — copre
  l'intero articolo incluse le tabelle di verifica dell'identità e il
  rimando all'Appendice B, confermato allo stesso modo) richiama
  l'Appendice B, il cui primo paragrafo tratta esplicitamente le "Minacce
  per il processo verifica dell'identità dichiarata in fase di
  registrazione". Art. 15 e art. 21 (riferimenti esatti "art. 15" e
  "art. 21", entrambi Obbligo nel capitolo cap02 di questa stessa fonte,
  granularità intero articolo, confermati dal subagent responsabile di
  cap02 via coordinamento hub) richiamano l'Appendice C per la tassonomia
  dei tipi di token. Nessun'altra relazione interna o cross-capitolo è
  stata aggiunta.

Nessuna relazione cross-fonte (verso CAD/eIDAS/eIDAS2/DPCM) è tentata in
questo modulo.
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "Appendice A",
        "testo": (
            "Criteri per l'attribuzione dei livelli di sicurezza (LoA) ai servizi SPID: la "
            "scelta del livello deve basarsi sulle conseguenze di un accesso improprio, con "
            "tabelle di riferimento impatto/livello e classificazione dato/tipo di accesso."
        ),
        "testo_integrale": (
            "Appendice A – Criteri per l'attribuzione dei livelli di sicurezza dei servizi\n\n"
            "Il sistema SPID è basato su tre livelli di sicurezza di autenticazione informatica, "
            "con il livello 1 associato a quello più basso ed il livello 3 a quello più elevato. "
            "Ai sensi dell'articolo 6, comma 5 del DPCM, l'erogatore del servizio deve scegliere "
            "il livello di sicurezza da associare all'accesso del servizio stesso.\n\n"
            "La scelta del livello di sicurezza (LoA) deve essere fondamentalmente basata sulle "
            "conseguenze derivanti da un accesso improprio a sistemi o applicazioni determinato "
            "dalla probabilità di errore che si può commettere nel processo di autenticazione; "
            "livelli di sicurezza (LoA) più alti saranno associati a servizi per i quali un "
            "accesso improprio comporta conseguenze e impatti più significativi (come sistemi che "
            "trattano dati sensibili o dati relativi a reddito o patrimonio) mentre richieste a "
            "carattere informativo possono essere associate a livelli più bassi.\n\n"
            "È importante evidenziare il fatto che la scelta dei livelli di sicurezza è operata a "
            "tutela degli interessi reciproci degli utenti fruitori che degli erogatori dei "
            "servizi. Ad evidenziare ciò basta riferirsi a servizi relativi a operazioni "
            "dispositive, come bonifici on line effettuati attraverso servizi di home banking. È "
            "chiaro che se la banca, erogatrice dei servizio, ha interesse a tutelarsi contro i "
            "furti on-line operati, ad esempio, attraverso furti di identità, questo interesse "
            "coincide con quello del titolare del conto corrente online dal quale vengono "
            "fraudolentemente sottratti i fondi.\n\n"
            "La metodologia suggerita dall'Agenzia prevede l'identificazione dei rischi per ogni "
            "specifico servizio e la conseguente assegnazione dei livelli di sicurezza previsti "
            "in ambito SPID; ovviamente la misura dello impatto potenziale di questi rischi "
            "individuati dipende dallo specifico contesto e dalle entità coinvolte da impropria "
            "autenticazione.\n\n"
            "Tabella \"Impatto Potenziale/Livello di Sicurezza SPID\" (impatto causato da un "
            "accesso improprio; colonne: Livello 1, Livello 2, Livello 3):\n"
            "- Sistema di autenticazione — Livello 1: a singolo fattore, discreta sicurezza sulla "
            "fedeltà/esattezza dell'identità asserita; Livello 2: a doppio fattore, alta "
            "sicurezza; Livello 3: a doppio fattore basato su certificati digitali, elevatissima "
            "sicurezza.\n"
            "- Potenziale danno di reputazione — Livello 1: Basso; Livello 2: Moderato; Livello 3: "
            "Alto.\n"
            "- Potenziali danni finanziari dell'utente e dell'erogatore del servizio — Livello 1: "
            "Basso; Livello 2: Moderato; Livello 3: Alto.\n"
            "- Potenziale danno per rilascio di informazioni sensibili dell'utente — Livello 1: "
            "N/A; Livello 2: Basso; Livello 3: Moderato-Alto.\n"
            "- Potenziale danno per violazioni di carattere civile (es. non conformità a "
            "regolamenti, norme) — Livello 1: N/A; Livello 2: Basso-Moderato; Livello 3: Alto.\n"
            "- Potenziali danni a programmi di interesse pubblico — Livello 1: Basso; Livello 2: "
            "Moderato; Livello 3: Alto.\n"
            "- Impatto potenziale per la sicurezza personale dell'utente e dell'erogatore del "
            "servizio — Livello 1: N/A; Livello 2: Basso; Livello 3: Moderato-Alto.\n\n"
            "Dove per il valore (basso, moderato, alto) assegnato ai potenziali impatti è stato "
            "scelto la definizione normalmente adottata nell'ISO/IEC 27001 framework e FIPS 199:\n"
            "- Basso: la perdita di confidenzialità, integrità e disponibilità ha un effetto "
            "negativo limitato per l'operatività delle organizzazioni, per i beni e per le "
            "persone.\n"
            "- Moderato: la perdita di confidenzialità, integrità e disponibilità potrebbe avere "
            "un serio effetto negativo per l'operatività delle organizzazioni, per i beni e per "
            "le persone.\n"
            "- Alto: la perdita di confidenzialità, integrità e disponibilità potrebbe avere un "
            "severo o catastrofico effetto negativo per l'operatività delle organizzazioni, per i "
            "beni e per le persone.\n\n"
            "Ulteriori considerazioni possono essere fatte in relazione alla classificazione dei "
            "dati secondo lo schema riportato in tabella, fermo restando la facoltà della singola "
            "Amministrazione di definire criteri diversi in base alle diverse modalità di "
            "erogazione dei servizi e ai dati resi disponibili:\n\n"
            "Tabella \"Classificazione dato/Tipo di accesso\":\n"
            "- Livello nessuno, classificazione Pubblico: non è richiesto nessun livello di "
            "autenticazione (esempio: area informativa del sito www.agid.gov.it; "
            "www.comune.milano.it).\n"
            "- Livello 1, classificazione Pubblico/Interno: adeguato per utenti iscritti ad un "
            "sito ma senza la possibilità di eseguire operazioni dispositive (esempio: area "
            "cittadini ma non dispositiva di un comune).\n"
            "- Livello 2, classificazione Interno: adeguato per utenti che accedono ad "
            "informazioni relative a pagamento di tasse e tributi, inoltro di richieste/domande, "
            "o per utenti che per motivazioni professionali possono trattare informazioni di "
            "soggetti terzi (esempio: area riservata dei comuni per richieste, interrogazioni, "
            "aggiornamenti e cancellazioni che non riguardano dati sensibili).\n"
            "- Livello 3, classificazione Riservato: necessario per utenti che sulla base di "
            "ruoli/responsabilità possono accedere ad informazioni di tipo riservato (esempio: "
            "siti che trattano dati sensibili, transazioni con trasferimento di fondi, accesso a "
            "documenti riservati o rilevanti per amministrazioni e imprese).\n\n"
            "L'Agenzia, al fine di rendere omogenei i LoA associati ai servizi su tutto il "
            "territorio nazionale, promuove e pubblica, nella sezione SPID del proprio sito "
            "istituzionale il LoA da associare alle categorie di servizi che presentano carattere "
            "di omogeneità."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Appendice B",
        "testo": (
            "Minacce associate al ciclo di vita delle identità digitali: registrazione (furto di "
            "identità, ripudio), emissione delle credenziali (divulgazione, manomissione, "
            "emissione non autorizzata) e token (furto, scoperta, duplicazione, intercettazione, "
            "offline cracking, phishing/pharming, ingegneria sociale, guessing online), con "
            "relative strategie di mitigazione."
        ),
        "testo_integrale": (
            "Appendice B – Minacce associate alla gestione del ciclo di vita delle identità "
            "digitali\n\n"
            "Minacce per il processo verifica dell'identità dichiarata in fase di registrazione. "
            "In generale sussistono due categorie di minacce nel processo di registrazione:\n\n"
            "a) furto/usurpazione di identità\n"
            "b) compromissione o uso non corretto della infrastruttura associata ai servizi "
            "erogati dal gestore delle identità digitali. Questa problematica rientra in quella "
            "generale relativa ai controlli di sicurezza (separazione dei compiti, conservazione "
            "della documentazione, audit indipendenti).\n\n"
            "Tabella \"Minacce nel processo di registrazione\":\n"
            "- Furto/usurpazione di identità — esempio: un richiedente dichiara una identità non "
            "corretta ad es. usando un documento d'identità contraffatto.\n"
            "- Ripudio/disconoscimento della registrazione — esempio: un cittadino/impresa nega "
            "la registrazione affermando che non ha mai richiesto la registrazione.\n\n"
            "Le minacce di registrazione possono essere impedite, o almeno dissuase, rendendo più "
            "complessa la possibilità di effettuare un furto di identità e aumentando la "
            "probabilità di rilevazione di queste evenienze. A qualsiasi livello devono essere "
            "utilizzati dei metodi (1) per verificare l'esistenza di una persona con l'identità "
            "dichiarata, (2) che il richiedente sia effettivamente l'utente titolare dell'identità "
            "dichiarata e (3) che lo stesso non può successivamente disconoscere la registrazione."
            "\n\n"
            "Minacce associate al processo di emissione delle credenziali: attacchi causati da "
            "furti/usurpazione di identità e da meccanismi di trasporto per l'emissione delle "
            "credenziali.\n\n"
            "Tabella \"Minacce/Processo di emissione\":\n"
            "- Divulgazione/rivelazione — esempio: una chiave generata dal gestore delle identità "
            "digitali è copiata da un aggressore informatico; strategia di mitigazione: emissione "
            "delle credenziali di persona, spedizione in buste sigillate con posta raccomandata, "
            "uso di una sessione protetta per la spedizione in modalità elettronica.\n"
            "- Manomissione — esempio: una nuova password generata dal sottoscrittore viene "
            "modificata da un aggressore informatico; strategia di mitigazione: emissione delle "
            "credenziali di persona, spedizione in buste sigillate con posta raccomandata, uso di "
            "protocolli di comunicazione che proteggono la sessione dati.\n"
            "- Emissione non autorizzata — esempio: rilascio delle credenziali ad una persona che "
            "afferma di essere il sottoscrittore (e in effetti non lo è); strategia di "
            "mitigazione: definizione di una procedura che assicura che la persona destinataria "
            "delle credenziali sia la stessa persona che ha partecipato nel processo di "
            "registrazione.\n\n"
            "Minacce associate ai token: un potenziale aggressore malevolo può prendere il "
            "controllo di un token e fingere di essere il legittimo proprietario del token. Le "
            "minacce sono classificate in base alla tipologia dei token:\n"
            "- Qualcosa che abbiamo: può essere perso, danneggiato, rubato o clonato (es. computer "
            "copiato, token hardware rubato/manomesso/duplicato).\n"
            "- Qualcosa che conosciamo: l'aggressore potrebbe indovinare la password/PIN o "
            "installare software maligno (keylogger), catturare il traffico di rete o usare "
            "social engineering.\n"
            "- Qualcosa che siamo: può essere replicato (es. copia di impronte digitali) se il "
            "sistema biometrico non usa tecniche di rilevazione robuste.\n\n"
            "Tabella \"Minacce/Tipo token\" con esempi e tecniche di mitigazione:\n"
            "- Furto (un token fisico viene rubato, es. furto di cellulare/dispositivo fisico) — "
            "mitigazione: usare token multi-fattore attivabili tramite PIN o elementi biometrici.\n"
            "- Scoperta (risposte a domande di sicurezza facilmente deducibili, es. \"quale liceo "
            "hai frequentato?\" reperibile sui social) — mitigazione: usare metodologie che "
            "rendano complessa la deduzione di una risposta.\n"
            "- Duplicazione (il token è copiato con o senza l'assenso dell'utente, es. password su "
            "post-it copiata) — mitigazione: usare token difficilmente duplicabili come token "
            "crittografici hardware.\n"
            "- Intercettazione (il token viene rilevato al momento dell'immissione, es. password "
            "dedotta osservando la tastiera o con keylogger) — mitigazione: usare tecniche di "
            "autenticazione dinamica per cui la conoscenza di una parola non fornisca "
            "informazione utile in autenticazioni successive.\n"
            "- Offline cracking (tecniche analitiche offline sui token rubati, es. analisi "
            "differenziale o attacchi da dizionario) — mitigazione: usare token con elevata "
            "entropia e blocco dopo un numero limitato di tentativi.\n"
            "- Phishing o pharming (l'utente crede che l'aggressore sia il fornitore di "
            "servizi/identità, es. DNS re-routing o sito civetta) — mitigazione: usare tecniche di "
            "autenticazione dinamica.\n"
            "- Ingegneria sociale (l'aggressore convince l'utente a rivelare il contenuto del "
            "token, es. telefonata fingendosi amministratore di sistema) — mitigazione: usare "
            "tecniche di autenticazione dinamica.\n"
            "- Provare a indovinare online (attacchi basati su dizionari o password note) — "
            "mitigazione: usare token con elevata entropia e blocco dopo un numero limitato di "
            "tentativi.\n\n"
            "A queste tecniche possono essere applicate strategie addizionali come l'uso di "
            "fattori multipli, meccanismi di sicurezza fisica, regole di complessità sulle "
            "password, sistematici controlli di sicurezza sulla rete e sui sistemi, tecniche out "
            "of band per la verifica del possesso di dispositivi registrati, addestramento "
            "periodico e informazione preventiva su potenziali minacce."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Appendice C",
        "testo": (
            "Tassonomia dei tipi di token utilizzabili per l'autenticazione informatica SPID "
            "(hardware/software, single-factor/multi-factor, OTP, crittografico, con "
            "segreto memorizzato, con conoscenza pre-registrata, con tabella di codici, out of "
            "band), con criteri per il riconoscimento dell'autenticazione multi-fattore."
        ),
        "testo_integrale": (
            "Appendice C - Tipi di token e loro Tassonomia\n\n"
            "Per le credenziali a doppio fattore viene normalmente utilizzato un token di tipo "
            "hardware o di tipo software.\n\n"
            "- Token di tipo hardware: dispositivo elettronico portatile di piccole dimensioni, "
            "alimentato a batteria con autonomia nell'ordine di qualche anno, dotato di uno "
            "schermo e talvolta di una tastiera numerica (alcuni token possono essere collegati "
            "ad un computer tramite una porta USB per facilitare lo scambio di dati).\n"
            "- Token di tipo software: le informazioni necessarie risiedono direttamente "
            "nell'apparato dell'utente (PC, tablet, ecc.), e non in un oggetto esterno.\n\n"
            "In particolare nei token crittografici multi-fattore, una chiave crittografica viene "
            "direttamente contenuta nel dispositivo hardware o viene immagazzinata su un disco, o "
            "equivalente media \"soft\", nel caso di token software ne viene richiesta "
            "l'attivazione attraverso un secondo fattore di autenticazione. L'autenticazione, in "
            "questo caso, è ottenuta provando sia il possesso che il controllo della chiave. Il "
            "convalidatore del token dipende strettamente dallo specifico protocollo "
            "crittografico, generalmente basato su qualche tipo di messaggio firmato, ad esempio, "
            "nel caso del protocollo TLS, è previsto il messaggio di \"certificate verify\".\n\n"
            "I token del tipo one-time password (OTP) multi-fattore, sono dispositivi hardware "
            "che generano una password valida una sola volta nella fase di attivazione e che "
            "richiedono l'attivazione attraverso un secondo fattore di autenticazione. Il secondo "
            "fattore di autenticazione può essere ottenuto attraverso \"qualcosa che conosciamo\" "
            "ad es. un PIN o \"qualcosa che siamo\" ad esempio attraverso la lettura di elementi "
            "biometrici (impronte digitali). La password one-time viene normalmente visualizzata "
            "sul dispositivo e deve essere digitata manualmente (in alcuni casi può essere "
            "prevista la lettura diretta dal computer attraverso, ad esempio, l'interfaccia USB)."
            "\n\n"
            "Per completezza, i processi di autenticazione multi-stadio nel quale viene "
            "utilizzato un token a singolo fattore per ottenere un secondo token non "
            "costituiscono una vera autenticazione multi-fattore, in questo caso il livello di "
            "sicurezza dell'autenticazione della soluzione combinata è pari a quello del token "
            "più debole. Ad esempio, alcune soluzioni in mobilità si basano su chiavi "
            "crittografiche complete o parziali memorizzate su un server online e scaricate sul "
            "computer locale del richiedente dopo una prima autenticazione basata sull'uso di "
            "password. Successivamente, il richiedente può usare il token crittografico "
            "precedentemente scaricato per autenticarsi con un gestore di identità remoto; "
            "questo tipo di soluzione deve essere considerata dello stesso livello di sicurezza "
            "della password usata dal richiedente per ottenere il token crittografico.\n\n"
            "In alcuni casi può essere preferibile elevare il livello di sicurezza "
            "dell'autenticazione durante una sessione applicativa, ciò può essere considerato un "
            "caso speciale di autenticazione multi-token dove un primo token (ad es. la password) "
            "viene utilizzato per stabilire una sessione sicura ed un secondo token (ad es. un "
            "out of band token) viene utilizzato per attivare una particolare transazione durante "
            "la sessione. Anche se i due token sono usati in fasi differenti, viene normalmente "
            "riconosciuto questo risultato come uno schema di autenticazione multi-token che può "
            "elevare il livello globale di sicurezza dell'autenticazione se i due token "
            "appartengono a due tipologie (\"che abbiamo\", \"che conosciamo\", \"che siamo\") "
            "differenti.\n\n"
            "Di seguito si descrivono i principali tipi di token utilizzabili per l'autenticazione "
            "informatica:\n"
            "- Token con segreto memorizzato: tipicamente è composto da una stringa di caratteri "
            "(password) o una sequenza di cifre (PIN); nel caso SPID per essere considerato a "
            "livello 1 di sicurezza di autenticazione informatica devono essere rispettate le "
            "caratteristiche, policy e regole di complessità delle password indicate al paragrafo "
            "relativo alla creazione delle credenziali.\n"
            "- Token con conoscenza pre-registrata: normalmente una serie di richieste o "
            "indicazioni (prompt o challenge) che vengono stabilite tra l'utente e il gestore "
            "delle identità digitali durante la fase di registrazione (ad es. una risposta del "
            "tipo \"il nome di tua madre da nubile?\").\n"
            "- Token con tabella dei codici/segreti: un token fisico o elettronico che contiene "
            "una tabella di codici riservati, all'utente può essere richiesto di rispondere con "
            "il codice/segreto corrispondente ad una specifica posizione della tabella.\n"
            "- Token out of band: un token fisico indirizzabile in modo univoco che può ricevere "
            "un codice/segreto selezionato dal gestore dell'identità per essere usato una sola "
            "volta durante la sessione di servizio (ad esempio un codice inviato via SMS ad un "
            "numero di cellulare certificato).\n"
            "- Dispositivo a singolo fattore (SF) del tipo One-Time Password (OTP): un dispositivo "
            "hardware che supporta la generazione automatica di una OTP (ad es. un codice "
            "composto da sei caratteri).\n"
            "- Dispositivo Crittografico a singolo fattore (SF): un dispositivo hardware che "
            "esegue operazioni crittografiche su un input al dispositivo. Il dispositivo non "
            "richiede l'attivazione attraverso un secondo fattore di autenticazione. Questo "
            "dispositivo usa chiavi crittografiche asimmetriche o simmetriche embedded (integrate "
            "nel dispositivo stesso).\n"
            "- Token crittografico software multi-fattore (MF): una chiave crittografica è "
            "memorizzata su un disco o un altro \"media\" e richiede l'attivazione attraverso un "
            "secondo fattore di autenticazione. L'autenticazione viene quindi ottenuta provando "
            "il possesso e il controllo della chiave. Questo sistema è basato su certificati "
            "digitali e criteri di custodia delle chiavi private su dispositivi che soddisfano i "
            "requisiti dell'Allegato II del Regolamento 910/2014.\n"
            "- Dispositivo multi-fattore (MF) del tipo One-Time Password (OTP): un dispositivo "
            "hardware che genera una one-time password per l'uso durante l'autenticazione e che "
            "richiede l'attivazione attraverso un secondo fattore di autenticazione (ad es. un "
            "dato biometrico, un dato digitato su un pad integrato ecc.).\n"
            "- Dispositivo Crittografico multi-fattore (MF): un dispositivo hardware che contiene "
            "chiavi crittografiche che richiedono l'attivazione attraverso un secondo fattore di "
            "autenticazione. L'autenticazione viene quindi ottenuta provando il possesso e il "
            "controllo della chiave. Questo sistema è basato su certificati digitali e criteri di "
            "custodia delle chiavi private su dispositivi che soddisfano i requisiti "
            "dell'Allegato II del Regolamento 910/2014."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "Appendice D",
        "testo": (
            "Requisiti di usabilità e accessibilità dell'interfaccia utente SPID a carico di "
            "fornitori di servizi e gestori delle identità digitali, incluso il vincolo di "
            "un'interfaccia unica di iscrizione/login per tutti i gestori (salvo il logo)."
        ),
        "testo_integrale": (
            "Appendice D – Usabilità e Accessibilità\n\n"
            "Per lo sviluppo dell'interfaccia utente, i fornitori di servizi e i gestori delle "
            "identità digitali devono garantire:\n"
            "- l'usabilità, ovvero la facilità d'uso come la presentazione delle informazioni e "
            "delle scelte in modo chiaro e conciso, la mancanza di ambiguità e il posizionamento "
            "di elementi importanti in aree appropriate, e la garanzia del funzionamento su "
            "diversi dispositivi e browser secondo lo stato dell'arte della tecnologia;\n"
            "- l'accessibilità per tutelare il diritto di accesso ai servizi informatici e "
            "telematici della pubblica amministrazione da parte dei disabili in coerenza con "
            "Legge n. 4 del 9 gennaio 2004, aggiornato dal DM 20 marzo 2013, e le indicazioni Web "
            "Accessibility Initiative (WAI) del World Wide Web Consortium (W3C).\n\n"
            "Al fine di ricondurre a una user experience comune per tutti gli utenti, "
            "limitandone l'eventuale disorientamento nell'accesso tramite diversi gestori "
            "dell'identità digitale, l'interfaccia del percorso di iscrizione (sign up) presso i "
            "gestori di identità digitale, nonché del login per l'accesso ai fornitori di "
            "servizi, sarà unica per tutti i gestori, fatto salvo lo spazio predisposto per la "
            "visualizzazione del proprio logo.\n\n"
            "Nella sezione SPID del sito AgID saranno pubblicati tutti gli aggiornamenti e le "
            "linee guida relative alle interfacce di autenticazione e gestione della "
            "registrazione con le ulteriori indicazioni necessarie per garantire una omogenea "
            "user experience."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Appendice A",
    "Appendice B",
    "Appendice C",
    "Appendice D",
]

MAPPATURA_LOCALE = {
    "Appendice A": ["Appendice A"],
    "Appendice B": ["Appendice B"],
    "Appendice C": ["Appendice C"],
    "Appendice D": ["Appendice D"],
}

RELAZIONI = [
    {
        "nodo_da": ("principio", None, "art. 2"),
        "nodo_a": ("principio", None, "Appendice A"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", None, "art. 12"),
        "nodo_a": ("principio", None, "Appendice B"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", None, "art. 15"),
        "nodo_a": ("principio", None, "Appendice C"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", None, "art. 21"),
        "nodo_a": ("principio", None, "Appendice C"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
]
