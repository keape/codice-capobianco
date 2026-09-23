"""Regolamento di esecuzione (UE) 2015/1502 della Commissione, dell'8
settembre 2015 - specifiche e procedure tecniche minime relative ai livelli
di garanzia dei mezzi di identificazione elettronica (ex art. 8 §3 eIDAS).
Fonte 14. Questo modulo copre l'allegato, punto 2.4 "Gestione e
organizzazione" (paragrafo introduttivo comune + le 7 sottosezioni
2.4.1-2.4.7), terzo di tre capitoli per questa fonte (cap01: artt. 1-2 +
allegato punto 1 "definizioni" + punto 2.1 "Registrazione"; cap02: allegato
punti 2.2 "Gestione dei mezzi di identificazione elettronica" e 2.3
"Autenticazione"). Testo ufficiale in
app/.source_cache/reg_ue_2015_1502/cap03.txt.

Modellazione (ADR-0007):

- Paragrafo introduttivo di 2.4 (due frasi: (a) i "fornitori" mettono in
  atto prassi documentate di gestione della sicurezza delle informazioni,
  politiche, approcci alla gestione dei rischi e altri controlli
  riconosciuti, per dare agli organi di gestione responsabili dei regimi
  la certezza dell'applicazione di prassi efficaci; (b) tutti i
  requisiti/elementi dell'intera sezione 2.4 si intendono proporzionati ai
  rischi che sussistono a un dato livello) -> UN SOLO nodo Principio,
  riferimento "allegato, punto 2.4 (introduzione)", tipo "scopo/ambito di
  applicazione" (non "altro"): il paragrafo non impone una prescrizione
  tecnica autonoma distinta da quanto già dettagliato puntualmente nelle 7
  sottosezioni che seguono - è una clausola di cornice/portata che (a)
  riassume lo scopo dell'intera sezione 2.4 (dare garanzia di prassi
  efficaci ai regimi) e (b) detta la regola di proporzionalità con cui
  TUTTI i requisiti di 2.4.1-2.4.7 vanno letti e applicati. Trattarlo come
  Obbligo autonomo avrebbe duplicato contenuto già censito puntualmente
  nelle sottosezioni; ometterlo avrebbe violato ADR-0007. `testo_integrale`
  riporta entrambe le frasi verbatim (nessuna elisione: la seconda frase,
  quella di proporzionalità, è la più rilevante ai fini interpretativi ma
  la prima fa comunque parte dello stesso paragrafo unitario del testo
  ufficiale). Oggetto giuridico "identificazione elettronica".
- Le 7 sottosezioni 2.4.1-2.4.7 -> un nodo Obbligo ciascuna
  (riferimento "allegato, punto 2.4.N"), soggetto obbligato categoria
  "QTSP/gestore" (convenzione di modellazione decisa in sessione principale
  per l'intero regolamento, coerente con Fonte 5/Fonte 13: il "fornitore"
  di un regime di identificazione elettronica notificato è mappato come
  "QTSP/gestore" pur non essendo tecnicamente un prestatore di servizi
  fiduciari in senso stretto). Ogni `testo_integrale` riporta per intero e
  verbatim la tabella a tre livelli (Basso/Significativo/Elevato,
  incluse le liste numerate interne), riformattata da tabella a prosa
  (separatore "|" del testo grezzo sostituito da struttura "Livello X:")
  senza alcuna parafrasi/sintesi/omissione di contenuto.
- 2.4.5 "Strutture e personale" ha, oltre alla tabella, una frase
  introduttiva propria ("Nella tabella riportata di seguito sono elencati i
  requisiti relativi alle strutture, al personale e ai subcontraenti...").
  Non le è stato dedicato un nodo separato: è una frase di mero raccordo
  verso la tabella immediatamente seguente (spiega cosa elenca la tabella e
  ribadisce la proporzionalità già stabilita a livello di intera sezione
  2.4), senza contenuto prescrittivo ulteriore rispetto a quanto già
  imposto dagli elementi numerati della tabella stessa - stesso trattamento
  riservato al paragrafo introduttivo della sezione 2.4 nel suo complesso
  ma qui, non introducendo un principio nuovo bensì solo richiamando quello
  già sancito, viene incluso verbatim in apertura del `testo_integrale` del
  nodo Obbligo "allegato, punto 2.4.5" invece di generare un nodo Principio
  duplicato.
- tipo_obbligo per sottosezione: 2.4.1 "organizzativo" (status giuridico del
  fornitore, conformità legale, capacità finanziaria, responsabilità per
  subappalto, piano di cessazione - tutti requisiti organizzativi di
  cornice, coerente con l'uso di "organizzativo" già fatto per il piano di
  cessazione in Fonte 8); 2.4.2 "informativo/trasparenza" (pubblicazione
  della definizione del servizio, notifica delle modifiche, risposta alle
  richieste di informazioni - tutti obblighi di trasparenza verso l'utente,
  per cui questa riga porta anche un soggetto destinatario "Utente/titolare"
  accanto al soggetto obbligato, essendo gli "utenti" espressamente
  individuati come beneficiari diretti); 2.4.3 "tecnico/sicurezza" (sistema
  di gestione della sicurezza delle informazioni, la cui definizione è
  censita come Principio definitorio nel cap01); 2.4.4 "di conservazione"
  (registrazione, conservazione e distruzione sicura dei dati - match
  esatto con questo tipo dedicato in tassonomia); 2.4.5 "organizzativo"
  (personale, subcontraenti, strutture fisiche); 2.4.6 "tecnico/sicurezza"
  (controlli tecnici, canali di comunicazione, materiale crittografico);
  2.4.7 "procedurale" (verifiche/audit di conformità).
- Stratificazione tra livelli: 2.4.1, 2.4.2, 2.4.4 e 2.4.5 sono identici sui
  tre livelli ("Come per il livello basso") - la sintesi in `testo` lo dice
  esplicitamente e non ripete tre volte lo stesso contenuto. 2.4.3, 2.4.6 e
  2.4.7 invece impongono requisiti *diversi* per livello (2.4.3: il livello
  Basso richiede solo un SGSI efficace, Significativo/Elevato richiedono in
  più l'adesione a norme/principi comprovati; 2.4.6: Significativo/Elevato
  aggiungono al Basso la protezione del materiale crittografico anche per
  l'autenticazione, oltre che per il rilascio dei mezzi; 2.4.7: Basso
  richiede solo verifiche interne, Significativo richiede verifiche
  indipendenti interne O esterne, Elevato richiede verifiche esterne
  indipendenti più, se il regime è gestito da un organismo pubblico, una
  verifica ai sensi della legislazione nazionale) - la sintesi in `testo`
  per questi tre nodi riflette esplicitamente la differenza tra livelli,
  come richiesto.
- Nota sulla nota a piè di pagina "(1)Regolamento (CE) n. 765/2008..." in
  coda al testo grezzo di questo capitolo: non è ancorata testualmente ad
  alcuna disposizione della sezione 2.4 (nessun richiamo "accreditamento"/
  "organismo di valutazione della conformità" compare nel testo di 2.4;
  quel lessico compare altrove nel regolamento, es. nelle definizioni di
  "fonte autorevole"/procedure di verifica dell'identità già coperte da
  cap01/cap02) - è un artefatto di impaginazione del PDF sorgente (nota a
  fondo pagina condivisa con contenuto di una pagina adiacente), non un
  comma di questo capitolo: esclusa da questo modulo, nessun nodo dedicato.
- RELAZIONI = [] in questo modulo: il legame naturale tra il principio di
  proporzionalità introduttivo e le 7 sottosezioni Obbligo è già esplicito
  nel testo stesso (l'introduzione dichiara di applicarsi "all'intera
  sezione 2.4") e non richiede un arco tipizzato dedicato per essere
  navigabile; nessuna delle 14 relazioni tipizzate coglie con precisione
  "principio di proporzionalità che qualifica l'applicazione di più
  obblighi dello stesso capitolo" senza forzare la semantica. Nessuna
  relazione cross-fonte/cross-capitolo tentata qui per costruzione (causa
  nota di collisione su merge parallelo, ADR-0009): il collegamento con le
  altre fonti già censite (incluse eIDAS/CAD/DPCM/SPID) è demandato alla
  fase di collegamento a posteriori successiva al merge di tutti i
  capitoli di questa fonte.
"""

RIGHE_OBBLIGHI = [
    {
        'riferimento': 'allegato, punto 2.4.1',
        'testo': "I fornitori di servizi di identificazione elettronica devono essere un'autorità pubblica o un ente giuridico riconosciuto come tale dall'ordinamento di uno Stato membro, con organizzazione stabile e pienamente operativa; devono rispettare gli obblighi giuridici applicabili all'esercizio del servizio (incluse le regole su quali informazioni possono essere richieste, le modalità del controllo dell'identità e la conservazione dei dati); devono dimostrare capacità di assumere il rischio di responsabilità per danni e disporre di risorse finanziarie sufficienti per la continuità del servizio; restano responsabili degli impegni affidati a soggetti esterni come se li svolgessero direttamente; e, se il regime non è costituito secondo il diritto nazionale, devono dotarsi di un piano di cessazione efficace che disciplini l'interruzione regolata o il subentro di un altro fornitore, la comunicazione alle autorità competenti e agli utenti finali, e la protezione/conservazione/distruzione sicura dei dati registrati. Questi cinque requisiti si applicano indistintamente a tutti e tre i livelli di garanzia (basso, significativo, elevato), senza alcuna differenziazione tra livelli.",
        'testo_integrale': "2.4.1. Disposizioni generali — Livello di garanzia: Basso: 1. I fornitori di qualsiasi servizio operativo disciplinato dal presente regolamento sono un'autorità pubblica o un'entità giuridica riconosciuta come tale dall'ordinamento giuridico di uno Stato membro, avente un'organizzazione consolidata e pienamente operativa sotto tutti gli aspetti pertinenti per la fornitura dei servizi. 2. I fornitori rispettano gli obblighi giuridici cui sono soggetti in relazione all'esercizio e alla prestazione del servizio, compresi i tipi di informazioni che possono essere richiesti, le modalità secondo le quali è eseguito il controllo dell'identità e quali informazioni possono essere conservate e per quanto tempo. 3. I fornitori sono in grado di dimostrare il possesso della capacità di assumere il rischio della responsabilità per danni, nonché di risorse finanziarie sufficienti per l'esercizio e la prestazione continuativi dei servizi. 4. I fornitori sono responsabili del rispetto di qualsiasi impegno affidato a un'entità esterna e della relativa conformità alla politica del regime, come se fossero essi stessi a svolgere le funzioni. 5. I regimi di identificazione elettronica non costituiti secondo il diritto nazionale prevedono un piano di cessazione efficace. Tale piano prevede l'interruzione regolata del servizio o la continuazione del servizio da parte di un altro fornitore, disciplina le modalità di comunicazione delle informazioni alle autorità competenti e agli utenti finali e contiene dettagli su come proteggere, conservare e distruggere i dati registrati conformemente alla politica del regime. Livello di garanzia: Significativo: Come per il livello basso. Livello di garanzia: Elevato: Come per il livello basso.",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 2.4.2',
        'testo': "I fornitori devono pubblicare una definizione del servizio comprensiva di tutti i termini, condizioni e tariffe applicabili (incluse eventuali limitazioni d'uso) e di un'informativa sulla privacy; devono mettere in atto politiche e procedure adeguate affinché gli utenti siano informati in modo tempestivo e affidabile di ogni modifica alla definizione del servizio, ai termini, alle condizioni e all'informativa sulla privacy; e devono garantire che le richieste di informazioni ricevano risposte complete ed esatte. Requisiti identici sui tre livelli di garanzia, senza differenziazione.",
        'testo_integrale': "2.4.2. Pubblicazione di avvisi e informazioni per gli utenti — Livello di garanzia: Basso: 1. Esiste una definizione del servizio pubblicata che comprende tutti i termini, le condizioni e le tariffe applicabili, incluse eventuali limitazioni d'uso. La definizione del servizio include un'informativa sulla privacy. 2. Devono essere messe in atto politiche e procedure adeguate al fine di garantire che gli utenti siano informati in modo tempestivo e affidabile delle eventuali modifiche alla definizione del servizio e ai termini, alle condizioni e all'informativa sulla privacy applicabili per il servizio in questione. 3. Devono essere messe in atto politiche e procedure adeguate affinché alle richieste di informazioni sia dato seguito con risposte complete ed esatte. Livello di garanzia: Significativo: Come per il livello basso. Livello di garanzia: Elevato: Come per il livello basso.",
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
            {'categoria': 'Utente/titolare', 'ruolo': 'destinatario'},
        ],
    },
    {
        'riferimento': 'allegato, punto 2.4.3',
        'testo': "Al livello Basso è richiesto un efficace sistema di gestione della sicurezza delle informazioni per la gestione e il controllo dei rischi per la sicurezza delle informazioni. Ai livelli Significativo ed Elevato (identici tra loro) tale sistema deve inoltre attenersi a norme o principi comprovati per la gestione o il controllo di tali rischi: un requisito ulteriore rispetto al livello Basso, non solo un rafforzamento generico.",
        'testo_integrale': "2.4.3. Gestione della sicurezza delle informazioni — Livello di garanzia: Basso: Esiste un efficace sistema di gestione della sicurezza delle informazioni per la gestione e il controllo dei rischi per la sicurezza delle informazioni. Livello di garanzia: Significativo: Livello basso, più: Il sistema di gestione della sicurezza delle informazioni si attiene a norme o principi comprovati per la gestione o il controllo dei rischi per la sicurezza delle informazioni. Livello di garanzia: Elevato: Come per il livello significativo.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 2.4.4',
        'testo': "I fornitori devono registrare e conservare le informazioni pertinenti mediante un sistema di gestione delle registrazioni efficace, nel rispetto della normativa vigente e delle buone prassi in materia di protezione e conservazione dei dati; devono inoltre conservare e proteggere, nella misura consentita dalla legislazione nazionale, i dati registrati per il tempo necessario a consentire verifiche e indagini su violazioni della sicurezza e ai fini della conservazione dei dati, per poi distruggerli in modo sicuro. Requisiti identici sui tre livelli di garanzia.",
        'testo_integrale': "2.4.4. Registrazione dei dati — Livello di garanzia: Basso: 1. Registrare e conservare le informazioni pertinenti mediante un sistema di gestione delle registrazioni efficace, tenendo conto della normativa vigente e delle buone prassi in materia di protezione e conservazione dei dati. 2. Conservare, nella misura consentita dalla legislazione nazionale o da altre disposizioni amministrative nazionali, e proteggere i dati registrati per il tempo necessario al fine di effettuare verifiche e indagini sulle violazioni della sicurezza e ai fini della conservazione dei dati, quindi distruggere i dati registrati in modo sicuro. Livello di garanzia: Significativo: Come per il livello basso. Livello di garanzia: Elevato: Come per il livello basso.",
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 2.4.5',
        'testo': "I fornitori devono garantire procedure per formazione, qualifiche ed esperienza adeguate del personale e dei subcontraenti; personale in numero sufficiente per un funzionamento e una fornitura adeguati del servizio; strutture costantemente monitorate e protette da danni ambientali, accessi non autorizzati e altri fattori di rischio; e restrizione dell'accesso alle aree in cui sono conservate o trattate informazioni personali, crittografiche o altre informazioni sensibili al solo personale o subcontraenti autorizzati. Requisiti identici sui tre livelli di garanzia, ciascuno comunque proporzionato al livello di rischio associato al livello di garanzia fornito.",
        'testo_integrale': "2.4.5. Strutture e personale — Nella tabella riportata di seguito sono elencati i requisiti relativi alle strutture, al personale e ai subcontraenti, se del caso, che svolgono le funzioni disciplinate dal presente regolamento. La conformità a ciascuno dei requisiti è proporzionata al livello di rischio associato al livello di garanzia fornito. Livello di garanzia: Basso: 1. Esistono procedure volte a garantire che il personale e i subcontraenti dispongano di una formazione, di qualifiche e di un'esperienza adeguate in relazione alle competenze richieste dal ruolo che occupano. 2. Il personale e i subcontraenti sono in numero sufficiente a consentire un funzionamento e una fornitura adeguati del servizio nel rispetto delle politiche e delle procedure vigenti. 3. Le strutture utilizzate per la fornitura del servizio sono costantemente monitorate e protette dai danni causati da eventi ambientali, accesso non autorizzato e altri fattori che possono incidere sulla sicurezza del servizio. 4. Le strutture utilizzate per la fornitura del servizio garantiscono che l'accesso alle aree in cui sono conservate o trattate le informazioni personali, crittografiche o altre informazioni sensibili sia limitato al personale o ai subcontraenti autorizzati. Livello di garanzia: Significativo: Come per il livello basso. Livello di garanzia: Elevato: Come per il livello basso.",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 2.4.6',
        'testo': "Al livello Basso i fornitori devono avere controlli tecnici proporzionati per la gestione dei rischi di sicurezza dei servizi (a protezione di riservatezza, integrità e disponibilità delle informazioni trattate); canali di comunicazione elettronici protetti da intercettazioni, manipolazione e attacchi replay; accesso al materiale crittografico sensibile per il rilascio dei mezzi di identificazione elettronica limitato ai ruoli/applicazioni strettamente necessari e mai conservato in chiaro; procedure per mantenere la sicurezza nel tempo e reagire a variazioni di rischio, incidenti e violazioni; e conservazione, trasporto e smaltimento sicuri di ogni supporto con informazioni personali, crittografiche o sensibili. Ai livelli Significativo ed Elevato (identici tra loro) si aggiunge un requisito ulteriore rispetto al Basso: il materiale crittografico sensibile deve essere protetto dalla manomissione non solo per il rilascio dei mezzi di identificazione elettronica ma anche per la funzione di autenticazione.",
        'testo_integrale': "2.4.6. Controlli tecnici — Livello di garanzia: Basso: 1. Esistono controlli tecnici proporzionati per la gestione dei rischi per la sicurezza dei servizi; tali controlli proteggono la riservatezza, l'integrità e la disponibilità delle informazioni trattate. 2. I canali di comunicazione elettronici utilizzati per lo scambio delle informazioni personali o sensibili sono protetti dalle intercettazioni, dalla manipolazione e dagli attacchi di tipo replay. 3. L'accesso al materiale crittografico sensibile utilizzato per il rilascio dei mezzi di identificazione elettronica è limitato ai ruoli e alle applicazioni per i quali è categoricamente richiesto. È fornita la garanzia che tale materiale non è mai conservato stabilmente come testo in chiaro. 4. Esistono procedure a garanzia del mantenimento della sicurezza nel tempo e della capacità di reagire alla variazione dei livelli di rischio, agli incidenti e alle violazioni della sicurezza. 5. Tutti i supporti contenenti informazioni personali, crittografiche o altre informazioni sensibili sono conservati, trasportati e smaltiti in modo sicuro e protetto. Livello di garanzia: Significativo: Come per il livello basso, più: Il materiale crittografico sensibile utilizzato per il rilascio dei mezzi di identificazione elettronica e per fornire l'autenticazione è protetto dalla manomissione. Livello di garanzia: Elevato: Come per il livello significativo.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 2.4.7',
        'testo': "Al livello Basso sono richieste verifiche interne periodiche, calibrate per includere tutte le parti che concorrono alla prestazione dei servizi forniti, volte ad accertarne la conformità alla politica pertinente. Al livello Significativo tali verifiche periodiche devono essere indipendenti, interne o esterne (un rafforzamento rispetto al Basso, che non richiede indipendenza). Al livello Elevato le verifiche periodiche devono essere esterne indipendenti (non più una scelta tra interna o esterna) e, se il regime è gestito direttamente da un organismo pubblico, il regime stesso deve inoltre essere sottoposto a verifica in conformità con la legislazione nazionale: un requisito aggiuntivo condizionato alla natura pubblica della gestione.",
        'testo_integrale': "2.4.7. Conformità e verifiche — Livello di garanzia: Basso: Sono eseguite verifiche interne periodiche calibrate in modo da includere tutte le parti che pertengono alla prestazione dei servizi forniti e intese ad accertarne la conformità alla politica pertinente. Livello di garanzia: Significativo: Sono eseguite periodicamente verifiche indipendenti interne o esterne calibrate in modo da includere tutte le parti che pertengono alla prestazione dei servizi forniti e intese ad accertarne la conformità alla politica pertinente. Livello di garanzia: Elevato: 1. Sono eseguite periodicamente verifiche esterne indipendenti calibrate in modo da includere tutte le parti che pertengono alla prestazione dei servizi forniti e intese ad accertarne la conformità alla politica pertinente. 2. Qualora sia gestito direttamente da un organismo pubblico, il regime è sottoposto a verifica in conformità con la legislazione nazionale.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "Il secondo elemento del livello Elevato (verifica ai sensi della legislazione nazionale) si applica solo se il regime di identificazione elettronica è gestito direttamente da un organismo pubblico.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
]

RIGHE_PRINCIPI = [
    {
        'riferimento': 'allegato, punto 2.4 (introduzione)',
        'testo': "Il paragrafo introduttivo della sezione 2.4 stabilisce che tutti i partecipanti che forniscono un servizio di identificazione elettronica in un contesto transfrontaliero («fornitori») mettono in atto prassi documentate di gestione della sicurezza delle informazioni, politiche, approcci alla gestione dei rischi e altri controlli riconosciuti, per dare agli organi di gestione responsabili dei regimi di identificazione elettronica la certezza dell'applicazione di prassi efficaci; e detta la regola interpretativa di proporzionalità applicabile all'intera sezione 2.4: tutti i requisiti/elementi delle sottosezioni 2.4.1-2.4.7 si intendono proporzionati ai rischi che sussistono al dato livello di garanzia (basso/significativo/elevato).",
        'testo_integrale': "2.4. Gestione e organizzazione — Tutti i partecipanti che forniscono un servizio correlato all'identificazione elettronica in un contesto transfrontaliero («fornitori») mettono in atto prassi documentate per la gestione della sicurezza delle informazioni, politiche, approcci alla gestione dei rischi e altri controlli riconosciuti in modo da dare agli opportuni organi di gestione responsabili dei regimi di identificazione elettronica nei rispettivi Stati membri la certezza dell'applicazione di prassi efficaci. Nell'intera sezione 2.4 tutti i requisiti/elementi si intendono come proporzionati ai rischi che sussistono a un dato livello.",
        'tipo_principio': 'scopo/ambito di applicazione',
        'stato': 'vigente',
        'oggetti_giuridici': ['identificazione elettronica'],
    },
]

INDICE_ARTICOLI_LOCALE = [
    'allegato, punto 2.4 (introduzione)',
    'allegato, punto 2.4.1',
    'allegato, punto 2.4.2',
    'allegato, punto 2.4.3',
    'allegato, punto 2.4.4',
    'allegato, punto 2.4.5',
    'allegato, punto 2.4.6',
    'allegato, punto 2.4.7',
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI = []
