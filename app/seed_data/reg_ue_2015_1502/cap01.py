"""Regolamento di esecuzione (UE) 2015/1502 della Commissione, dell'8
settembre 2015 - specifiche e procedure tecniche minime per i livelli di
garanzia basso, significativo ed elevato dei mezzi di identificazione
elettronica, ex art. 8 §3 eIDAS (regolamento (UE) n. 910/2014). Fonte 14,
capitolo 1 di 3 (vedi app/.source_cache/reg_ue_2015_1502/manifest.json):
Articoli 1-2 del regolamento + Allegato punto 1 "Definizioni applicabili" +
Allegato punto 2 (intro "Specifiche e procedure tecniche") + punto 2.1
"Registrazione" con le sottosezioni 2.1.1-2.1.4. Testo ufficiale in
app/.source_cache/reg_ue_2015_1502/cap01.txt.

Modellazione (ADR-0007):
- Art. 1 §1 -> Principio, tipo "scopo/ambito di applicazione" (designa
  l'allegato come sede delle specifiche/procedure che determinano i tre
  livelli di garanzia).
- Art. 1 §2 -> Principio, tipo "definitorio" (elenca i 4 elementi - a)
  registrazione, b) gestione dei mezzi, c) autenticazione, d) gestione e
  organizzazione - di cui l'allegato determina affidabilità/qualità,
  ciascuno mappato a una lettera dell'art. 8 §3 eIDAS; trattato come nodo
  distinto da §1 perché ha contenuto proprio - la mappatura sezione
  allegato -> lettera eIDAS - non solo una designazione generica).
- Art. 1 §3 (equivalenza crescente: chi soddisfa un livello superiore
  soddisfa anche quello inferiore) e §4 (cumulatività dei requisiti per il
  livello dichiarato, salvo indicazione contraria) -> due Principi
  autonomi, tipo "altro" (norme dichiarative trasversali che governano la
  lettura di tutto l'allegato, non designazioni/definizioni in senso
  proprio).
- Art. 2: un solo nodo "art. 2" (Principio, tipo "altro"), non due come nel
  precedente Reg. (UE) 2025/1566 (dove "entrata in vigore" e
  "applicazione" erano due frasi con contenuto giuridico distinto per il
  differimento esplicito di 24 mesi motivato nel considerando). Qui l'art.
  2 ha due sole frasi: "entra in vigore il ventesimo giorno..." (nessun
  differimento dell'applicazione, il regolamento è pienamente applicabile
  da subito) e "è obbligatorio in tutti i suoi elementi e direttamente
  applicabile..." - quest'ultima è la formula di chiusura standard di ogni
  regolamento UE self-executing, esclusa per lo stesso motivo del Reg.
  2025/1566 (nessun contenuto normativo autonomo). Con una sola frase
  sostanziale, un unico nodo "entrata in vigore ed efficacia" è la scelta
  più corretta - creare un secondo nodo vuoto di contenuto avrebbe
  significato duplicare artificiosamente la stessa informazione.
- Allegato, punto 1 "Definizioni applicabili": le 4 definizioni numerate
  (fonte autorevole; fattore di autenticazione, comprensivo delle 3
  sottocategorie possesso/conoscenza/intrinseco riportate verbatim nella
  stessa riga; autenticazione dinamica; sistema di gestione della
  sicurezza delle informazioni) -> 4 Principi distinti, tipo "definitorio",
  oggetto giuridico "identificazione elettronica" (oggetto specifico di
  questo regolamento).
- Allegato, punto 2 (intro, prima di 2.1): paragrafo di cornice che spiega
  la funzione generale delle specifiche/procedure tecniche dell'allegato
  rispetto ai requisiti dell'art. 8 eIDAS -> Principio, tipo "scopo/ambito
  di applicazione" (nessun soggetto obbligato né effetto giuridico
  specifico, pura disposizione di cornice per l'intero allegato punti
  2.1-2.4, di cui punti 2.2/2.3 sono nel capitolo 2 e punto 2.4 nel
  capitolo 3 - questo nodo, presente fisicamente nel testo di questo
  capitolo, copre la frase di cornice per l'intera sezione 2).
- Allegato punti 2.1.1/2.1.2/2.1.3: ciascuno un solo Obbligo (soggetto
  obbligato categoria "QTSP/gestore", stessa convenzione già adottata per
  Fonte 5/Fonte 13 nonostante il "gestore"/"entità responsabile della
  registrazione" non sia tecnicamente un prestatore di servizi fiduciari
  in senso stretto). tipo_obbligo "procedurale" per tutti e tre - coerente
  con il trattamento già riservato a obblighi di "verifica dell'identità
  del richiedente" nelle Fonti SPID (es. spid/cap02.py, dpcm/cap07.py):
  sono prescrizioni sui passi di un processo di registrazione/verifica, non
  requisiti di sicurezza tecnica in senso stretto né di organizzazione
  interna. Ciascun testo_integrale riporta per intero, in prosa (Livello
  Basso: ... Livello Significativo: ... Livello Elevato: ...), la tabella
  a tre livelli così come appare nel testo ufficiale (il separatore
  letterale " | " della resa testuale della tabella originale è solo
  formattazione, sostituito qui senza alcuna omissione/parafrasi); la
  sintesi in `testo` segnala esplicitamente quando i tre livelli sono
  sostanzialmente diversi tra loro (2.1.2/2.1.3, dove Significativo ed
  Elevato aggiungono opzioni alternative distinte) o quando sono
  identici (2.1.1, dove i tre livelli coincidono testualmente - "Come per
  il livello basso").
  - 2.1.1 aggiunge anche un soggetto destinatario "Utente/titolare" (il
    richiedente) perché il punto individua esplicitamente un dovere
    informativo verso di lui (deve conoscere termini/condizioni e
    precauzioni di sicurezza), diversamente da 2.1.2/2.1.3 che sono
    requisiti di verifica interni al processo dell'entità responsabile
    della registrazione, senza un destinatario/beneficiario distinto
    testualmente foregrounded.
- Allegato punto 2.1.4 "Collegamento tra i mezzi di identificazione
  elettronica delle persone fisiche e delle persone giuridiche": come
  indicato nell'assegnazione, 3 nodi separati anziché uno solo, perché le
  condizioni (1) e (2) hanno contenuto normativo autonomo (obbligo di
  supportare sospensione/revoca; facoltà di delega con responsabilità che
  resta al delegante) distinto dalla tabella a tre livelli del punto (3)
  (modalità di accertamento del collegamento). Tutti e tre gli obblighi
  portano `condizione_applicabilita` valorizzata perché l'intero punto
  2.1.4 si apre con "Ove applicabile" - si applica solo se un regime
  notificato prevede un collegamento persona fisica/persona giuridica, non
  è un requisito universale di ogni mezzo di identificazione elettronica.
  La frase di cornice "Ove applicabile, ... si applicano le seguenti
  condizioni." è riportata verbatim solo nel testo_integrale del punto (1)
  (primo elemento del gruppo), stesso criterio di sintesi già usato per le
  intestazioni di gruppo negli altri capitoli di questo censimento.
  - (1) sospensione/revoca + ciclo di vita del collegamento e (2) delega
    con responsabilità del delegante -> tipo_obbligo "organizzativo"
    (gestione del ciclo di vita/allocazione della responsabilità, non
    requisiti tecnici né passi di un processo di verifica).
  - (2) aggiunge anche un soggetto destinatario "Utente/titolare" perché
    la norma individua esplicitamente la persona fisica delegante/delegata
    come parte cui si applica l'effetto giuridico (responsabilità che
    resta al delegante), diversamente da (1) che è un requisito di sistema
    puro in capo al gestore.
  - (3) tabella dei livelli -> tipo_obbligo "procedurale", stesso
    trattamento di 2.1.1/2.1.2/2.1.3 (è a sua volta un processo di
    verifica/accertamento graduato per livello).

Relazioni interne al capitolo (nessuna relazione cross-fonte/cross-capitolo
tentata, per evitare la nota causa di KeyError su merge parallelo):
- art. 1 §3 e §4 (equivalenza crescente/cumulatività) "si applica a" il
  punto 2 (intro) dell'allegato, perché sono le due regole di lettura
  trasversali che governano l'intera sezione 2 (di cui il punto 2.1 di
  questo capitolo è solo la prima sottosezione, le altre nei capitoli
  successivi) - evidence_type "inferred" perché la relazione è strutturale
  (l'art. 1 §§3-4 non cita testualmente "punto 2"), non una citazione
  esplicita.
- la definizione di "fonte autorevole" (allegato punto 1(1)) "definisce" i
  tre obblighi di questo capitolo che riusano il termine in modo
  sostanziale per l'accertamento del requisito (2.1.2, 2.1.3, 2.1.4(3)) -
  evidence_type "textual" perché il termine compare letteralmente e
  ripetutamente nel testo di quei tre punti. Non collegata a 2.1.1 (che non
  cita mai "fonte autorevole") né a 2.1.4(1)/(2) (che non lo citano
  neppure).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "allegato, punto 2.1.1",
        "testo": "Nella fase di domanda/registrazione, l'entità responsabile della registrazione (QTSP/gestore) deve accertarsi che il richiedente conosca i termini e le condizioni d'uso del mezzo di identificazione elettronica e le precauzioni di sicurezza raccomandate, e deve raccogliere i dati identificativi necessari al controllo e alla verifica dell'identità. Per questo punto il regolamento non prevede alcun requisito aggiuntivo per i livelli significativo ed elevato rispetto al livello basso: i tre livelli di garanzia hanno qui lo stesso contenuto prescrittivo.",
        "testo_integrale": "2.1.1.Domanda e registrazione\n\nLivello Basso: 1.Accertarsi che il richiedente conosca i termini e le condizioni per l'uso del mezzo di identificazione elettronica. 2.Accertarsi che il richiedente conosca le precauzioni di sicurezza raccomandate per l'uso del mezzo di identificazione elettronica. 3.Raccogliere i dati identificativi necessari per il controllo e la verifica dell'identità. Livello Significativo: Come per il livello basso. Livello Elevato: Come per il livello basso.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato, punto 2.1.2",
        "testo": "Il controllo e la verifica dell'identità della persona fisica richiedente devono garantire, al livello Basso, il possesso di una prova d'identità riconosciuta, la sua autenticità/esistenza secondo una fonte autorevole e la presunzione di unicità della persona. Il livello Significativo aggiunge, in alternativa, una delle quattro opzioni rafforzative: verifica di autenticità della prova o collegamento a una fonte autorevole con misure antifrode; presentazione di un documento d'identità in un processo di registrazione nello Stato di rilascio con misure antifrode; riconoscimento di una garanzia equivalente già accertata in precedenza da un organismo di valutazione della conformità per un altro scopo; oppure rilascio basato su un mezzo di identificazione elettronica notificato già di livello significativo o elevato. Il livello Elevato richiede il rispetto di una tra due vie ulteriormente rafforzate rispetto al Significativo: verifica biometrica/fotografica con confronto delle caratteristiche fisiche tramite fonte autorevole (o, in alternativa, riconoscimento di una garanzia equivalente pregressa con verifica di persistente validità, o rilascio da un mezzo notificato già di livello elevato), oppure - se il richiedente non dispone di una fotografia o prova biometrica riconosciuta - applicazione delle stesse procedure nazionali usate dall'entità responsabile della registrazione per ottenerla.",
        "testo_integrale": "2.1.2.Controllo e verifica dell'identità (persona fisica)\n\nLivello Basso: 1.La persona può essere ritenuta in possesso di una prova riconosciuta dallo Stato membro in cui è presentata la domanda di rilascio del mezzo di identificazione elettronica e attestante l'identità dichiarata. 2.La prova può essere ritenuta autentica o esistente in virtù di una fonte autorevole ed è all'apparenza valida. 3.L'esistenza dell'identità dichiarata è accertata mediante una fonte autorevole e si può presumere che la persona che sostiene di possederla sia la stessa e unica persona. Livello Significativo: Livello basso, più una delle opzioni elencate di seguito ai punti da 1 a 4: 1.è stato verificato il possesso da parte della persona di una prova riconosciuta dallo Stato membro in cui è presentata la domanda di rilascio del mezzo di identificazione elettronica e attestante l'identità dichiarata e la prova è verificata per stabilirne l'autenticità oppure, secondo una fonte autorevole, esiste ed è collegata a una persona reale e sono state adottate misure per ridurre al minimo il rischio che l'identità della persona non corrisponda a quella dichiarata, tenendo conto ad esempio del rischio di smarrimento, furto, sospensione, revoca o scadenza della prova o 2.è presentato un documento d'identità durante un processo di registrazione nello Stato membro in cui è stato rilasciato il documento e quest'ultimo all'apparenza si riferisce alla persona che lo presenta e sono state adottate misure per ridurre al minimo il rischio che l'identità della persona non corrisponda a quella dichiarata, tenendo conto ad esempio del rischio di smarrimento, furto, sospensione, revoca o scadenza dei documenti o 3.ove procedure utilizzate in precedenza da un soggetto pubblico o privato nello stesso Stato membro per un fine diverso dal rilascio di mezzi di identificazione elettronica forniscano una garanzia equivalente a quelle definite nella sezione 2.1.2 per il livello di garanzia significativo, l'entità responsabile della registrazione non è tenuta a ripeterle, purché detta garanzia equivalente sia confermata da un organismo di valutazione della conformità ai sensi dell'articolo 2, punto 13, del regolamento (CE) n. 765/2008 del Parlamento europeo e del Consiglio(1) o da un organismo equivalente o 4.se i mezzi di identificazione elettronica sono rilasciati sulla base di un mezzo di identificazione elettronica notificato valido avente livello di garanzia significativo o elevato, e tenendo conto dei rischi di variazione dei dati di identificazione personale, non è necessario ripetere i processi di controllo e verifica dell'identità. Laddove il mezzo di identificazione elettronica che funge da base non sia stato notificato, il livello di garanzia significativo o elevato deve essere confermato da un organismo di valutazione della conformità ai sensi dell'articolo 2, punto 13, del regolamento (CE) n. 765/2008 o da un organismo equivalente. Livello Elevato: Devono essere rispettati i requisiti di cui al punto 1 o 2. 1.Livello significativo, più una delle opzioni elencate di seguito alle lettere da a) a c): a)qualora sia stato verificato il possesso da parte della persona di una fotografia o di una prova di identificazione biometrica riconosciuta dallo Stato membro in cui è presentata la domanda di rilascio del mezzo di identificazione elettronica e qualora tale prova corrisponda all'identità dichiarata, la prova è verificata per stabilirne la validità in virtù di una fonte autorevole e il richiedente è identificato come corrispondente all'identità dichiarata tramite il confronto di una o più sue caratteristiche fisiche con una fonte autorevole o b)ove procedure utilizzate in precedenza da un soggetto pubblico o privato nello stesso Stato membro per un fine diverso dal rilascio di mezzi di identificazione elettronica forniscano una garanzia equivalente a quelle definite nella sezione 2.1.2 per il livello di garanzia elevato, l'entità responsabile della registrazione non è tenuta a ripeterle, purché detta garanzia equivalente sia confermata da un organismo di valutazione della conformità ai sensi dell'articolo 2, punto 13, del regolamento (CE) n. 765/2008 o da un organismo equivalente e sono intraprese azioni per dimostrare che i risultati delle procedure utilizzate in precedenza sono ancora validi o c)se i mezzi di identificazione elettronica sono rilasciati sulla base di un mezzo di identificazione elettronica notificato valido avente livello di garanzia elevato, e tenendo conto dei rischi di variazione dei dati di identificazione personale, non è necessario ripetere i processi di controllo e verifica dell'identità. Laddove il mezzo di identificazione elettronica che funge da base non sia stato notificato, il livello di garanzia elevato deve essere confermato da un organismo di valutazione della conformità ai sensi dell'articolo 2, punto 13, del regolamento (CE) n. 765/2008 o da un organismo equivalente. e sono intraprese azioni per dimostrare che i risultati della precedente procedura di rilascio di un mezzo di identificazione elettronica notificato sono ancora validi. OPPURE 2.Qualora il richiedente non presenti una fotografia o una prova di identificazione biometrica riconosciuta, sono applicate le stesse procedure utilizzate a livello nazionale nello Stato membro dell'entità responsabile della registrazione per l'ottenimento di tale fotografia o prova di identificazione biometrica riconosciuta.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 2.1.3",
        "testo": "Il controllo e la verifica dell'identità della persona giuridica richiedente devono garantire, al livello Basso, che l'identità dichiarata sia dimostrata da una prova riconosciuta, apparentemente valida e/o esistente secondo una fonte autorevole (con inclusione volontaria della persona giuridica), e che la persona giuridica non sia impedita ad agire come tale. Il livello Significativo aggiunge, in alternativa, una delle tre opzioni rafforzative: prova con nome, forma giuridica ed eventuale numero di registrazione, verificata o confermata da una fonte autorevole in cui l'inclusione sia necessaria per operare nel settore, con misure antifrode; riconoscimento di una garanzia equivalente già accertata in precedenza da un organismo di valutazione della conformità per un altro scopo; oppure rilascio basato su un mezzo di identificazione elettronica notificato già di livello significativo o elevato. Il livello Elevato riprende la stessa struttura a tre opzioni del Significativo, rafforzata: prova con nome, forma giuridica e un identificativo univoco nazionale verificata per validità tramite fonte autorevole; oppure riconoscimento di una garanzia equivalente pregressa con verifica di persistente validità; oppure rilascio da un mezzo notificato già di livello elevato.",
        "testo_integrale": "2.1.3.Controllo e verifica dell'identità (persona giuridica)\n\nLivello Basso: 1.L'identità dichiarata della persona giuridica è dimostrata sulla base di una prova riconosciuta dallo Stato membro in cui è presentata la domanda di rilascio del mezzo di identificazione elettronica. 2.La prova è all'apparenza valida e può essere ritenuta autentica, o esistente in virtù di una fonte autorevole, laddove l'inclusione della persona giuridica nella fonte autorevole sia volontaria e regolamentata da un accordo tra la persona giuridica e la fonte autorevole. 3.A quanto risulta a una fonte autorevole, la persona giuridica non si trova in una condizione che le impedisce di agire in qualità di persona giuridica. Livello Significativo: Livello basso, più una delle opzioni elencate di seguito ai punti da 1 a 3: 1.l'identità dichiarata della persona giuridica è dimostrata sulla base di una prova riconosciuta dallo Stato membro in cui è presentata la domanda di rilascio del mezzo di identificazione elettronica, compresi il nome della persona giuridica, la forma giuridica e, se del caso, il numero di registrazione e la prova è verificata per stabilirne l'autenticità o è ritenuta esistente in virtù di una fonte autorevole, ove l'inclusione della persona giuridica nella fonte autorevole sia necessaria perché la persona giuridica possa operare nel suo settore e sono state adottate misure per ridurre al minimo il rischio che l'identità della persona giuridica non corrisponda a quella dichiarata, tenendo conto ad esempio del rischio di smarrimento, furto, sospensione, revoca o scadenza dei documenti o 2.ove procedure utilizzate in precedenza da un soggetto pubblico o privato nello stesso Stato membro per un fine diverso dal rilascio di mezzi di identificazione elettronica forniscano una garanzia equivalente a quelle definite nella sezione 2.1.3 per il livello di garanzia significativo, l'entità responsabile della registrazione non è tenuta a ripeterle, purché detta garanzia equivalente sia confermata da un organismo di valutazione della conformità ai sensi dell'articolo 2, punto 13, del regolamento (CE) n. 765/2008 o da un organismo equivalente o 3.se i mezzi di identificazione elettronica sono rilasciati sulla base di un mezzo di identificazione elettronica notificato valido avente livello di garanzia significativo o elevato, non è necessario ripetere i processi di controllo e verifica dell'identità. Laddove il mezzo di identificazione elettronica che funge da base non sia stato notificato, il livello di garanzia significativo o elevato deve essere confermato da un organismo di valutazione della conformità ai sensi dell'articolo 2, punto 13, del regolamento (CE) n. 765/2008 o da un organismo equivalente. Livello Elevato: Livello significativo, più una delle opzioni elencate di seguito ai punti da 1 a 3: 1.l'identità dichiarata della persona giuridica è dimostrata sulla base di una prova riconosciuta dallo Stato membro in cui è presentata la domanda di rilascio del mezzo di identificazione elettronica, compresi il nome della persona giuridica, la forma giuridica e almeno un identificativo univoco che rappresenti la persona giuridica utilizzato in un contesto nazionale e la prova è verificata per stabilirne la validità in virtù di una fonte autorevole o 2.ove procedure utilizzate in precedenza da un soggetto pubblico o privato nello stesso Stato membro per un fine diverso dal rilascio di mezzi di identificazione elettronica forniscano una garanzia equivalente a quelle definite nella sezione 2.1.3 per il livello di garanzia elevato, l'entità responsabile della registrazione non è tenuta a ripeterle, purché detta garanzia equivalente sia confermata da un organismo di valutazione della conformità ai sensi dell'articolo 2, punto 13, del regolamento (CE) n. 765/2008 o da un organismo equivalente e sono intraprese azioni per dimostrare che i risultati di tale procedura utilizzata in precedenza sono ancora validi o 3.se i mezzi di identificazione elettronica sono rilasciati sulla base di un mezzo di identificazione elettronica notificato valido avente livello di garanzia elevato, non è necessario ripetere i processi di controllo e verifica dell'identità. Laddove il mezzo di identificazione elettronica che funge da base non sia stato notificato, il livello di garanzia elevato deve essere confermato da un organismo di valutazione della conformità ai sensi dell'articolo 2, punto 13, del regolamento (CE) n. 765/2008 o da un organismo equivalente. e sono intraprese azioni per dimostrare che i risultati della precedente procedura di rilascio di un mezzo di identificazione elettronica notificato sono ancora validi.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 2.1.4(1)",
        "testo": "Ove sia previsto un collegamento tra il mezzo di identificazione elettronica di una persona fisica e quello di una persona giuridica, deve essere possibile sospendere e/o revocare tale collegamento; l'intero ciclo di vita del collegamento (attivazione, sospensione, rinnovo, revoca) è gestito secondo procedure riconosciute a livello nazionale.",
        "testo_integrale": "Ove applicabile, per stabilire un collegamento tra il mezzo di identificazione elettronica di una persona fisica e il mezzo di identificazione elettronica di una persona giuridica («collegamento»), si applicano le seguenti condizioni. (1)Deve essere possibile sospendere e/o revocare un collegamento. Il ciclo di vita di un collegamento (ad esempio attivazione, sospensione, rinnovo, revoca) è gestito secondo procedure riconosciute a livello nazionale.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo ove sia previsto un collegamento («collegamento») tra il mezzo di identificazione elettronica di una persona fisica e quello di una persona giuridica; non è un requisito universale di ogni mezzo di identificazione elettronica.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 2.1.4(2)",
        "testo": "Ove sia previsto un collegamento tra il mezzo di identificazione elettronica di una persona fisica e quello di una persona giuridica, la persona fisica titolare può delegare l'esercizio del collegamento a un'altra persona fisica, secondo procedure riconosciute a livello nazionale; la responsabilità del collegamento resta però sempre in capo alla persona fisica delegante, anche dopo la delega.",
        "testo_integrale": "(2)La persona fisica il cui mezzo di identificazione elettronica è collegato al mezzo di identificazione elettronica della persona giuridica può delegare l'esercizio del collegamento a un'altra persona fisica sulla base di procedure riconosciute a livello nazionale. Tuttavia la responsabilità continua a incombere alla persona fisica delegante.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo ove sia previsto un collegamento («collegamento») tra il mezzo di identificazione elettronica di una persona fisica e quello di una persona giuridica, e la persona fisica titolare scelga di delegarne l'esercizio a un'altra persona fisica.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato, punto 2.1.4(3)",
        "testo": "Le modalità con cui è stabilito il collegamento sono graduate per livello di garanzia. Al livello Basso occorre verificare che il controllo dell'identità della persona fisica che agisce per la persona giuridica sia stato eseguito almeno al livello basso, stabilire il collegamento secondo procedure nazionali riconosciute e verificare, tramite fonte autorevole, che la persona fisica non sia impedita ad agire per la persona giuridica. Il livello Significativo riprende il punto 3 del livello Basso e aggiunge: verifica del controllo dell'identità almeno al livello significativo, registrazione del collegamento in una fonte autorevole tramite procedure nazionali riconosciute, e verifica del collegamento sulla base di informazioni di una fonte autorevole. Il livello Elevato riprende il punto 3 del Basso e il punto 2 del Significativo, e aggiunge: verifica del controllo dell'identità al livello elevato, e verifica del collegamento basata su un identificativo univoco nazionale della persona giuridica combinato con informazioni di una fonte autorevole che identificano univocamente la persona fisica.",
        "testo_integrale": "(3)Il collegamento è stabilito nel modo seguente: Livello Basso: 1.È effettuata una verifica per accertare che il controllo dell'identità della persona fisica che agisce per conto della persona giuridica sia stato eseguito al livello basso o a un livello superiore. 2.Il collegamento è stabilito secondo procedure riconosciute a livello nazionale. 3.A quanto risulta a una fonte autorevole, la persona fisica non si trova in una condizione che le impedisce di agire per conto della persona giuridica. Livello Significativo: Punto 3 del livello basso, più i seguenti elementi: 1.È effettuata una verifica per accertare che il controllo dell'identità della persona fisica che agisce per conto della persona giuridica sia stato eseguito al livello significativo o elevato. 2.Il collegamento è stabilito secondo procedure riconosciute a livello nazionale, sfociate nella sua registrazione in una fonte autorevole. 3.Il collegamento è verificato sulla base di informazioni provenienti da una fonte autorevole. Livello Elevato: Punto 3 del livello basso e punto 2 del livello significativo, più i seguenti elementi: 1.È effettuata una verifica per accertare che il controllo dell'identità della persona fisica che agisce per conto della persona giuridica sia stato eseguito al livello elevato. 2.Il collegamento è verificato sulla base di un identificativo univoco che rappresenta la persona giuridica ed è utilizzato nel contesto nazionale, nonché sulla base di informazioni, provenienti da una fonte autorevole, che rappresentano in modo univoco la persona fisica.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo ove sia previsto un collegamento («collegamento») tra il mezzo di identificazione elettronica di una persona fisica e quello di una persona giuridica.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 1 §1",
        "testo": "L'allegato del regolamento determina, mediante specifiche e procedure tecniche, i livelli di garanzia basso, significativo ed elevato applicabili ai mezzi di identificazione elettronica rilasciati nell'ambito di un regime di identificazione elettronica notificato.",
        "testo_integrale": "Articolo 1\n\n1.I livelli di garanzia basso, significativo ed elevato per i mezzi di identificazione elettronica rilasciati nell'ambito di un regime di identificazione elettronica notificato sono determinati facendo riferimento alle specifiche e alle procedure fissate nell'allegato.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 §2",
        "testo": "Le specifiche e procedure dell'allegato servono a determinare l'affidabilità e la qualità di quattro elementi del mezzo di identificazione elettronica, ciascuno mappato a una lettera dell'art. 8 §3 eIDAS: a) la registrazione (sezione 2.1 dell'allegato, art. 8 §3 lett. a); b) la gestione dei mezzi di identificazione elettronica (sezione 2.2, lett. b) ed f); c) l'autenticazione (sezione 2.3, lett. c); d) la gestione e l'organizzazione (sezione 2.4, lett. d) ed e).",
        "testo_integrale": "2.Le specifiche e le procedure fissate nell'allegato sono utilizzate per specificare il livello di garanzia dei mezzi di identificazione elettronica rilasciati nell'ambito di un regime di identificazione elettronica notificato determinando l'affidabilità e la qualità dei seguenti elementi: a)la registrazione, di cui alla sezione 2.1 dell'allegato del presente regolamento, a norma dell'articolo 8, paragrafo 3, lettera a), del regolamento (UE) n. 910/2014; b)la gestione dei mezzi di identificazione elettronica, di cui alla sezione 2.2 dell'allegato del presente regolamento, a norma dell'articolo 8, paragrafo 3, lettere b) e f), del regolamento (UE) n. 910/2014; c)l'autenticazione, di cui alla sezione 2.3 dell'allegato del presente regolamento, a norma dell'articolo 8, paragrafo 3, lettera c), del regolamento (UE) n. 910/2014; d)la gestione e l'organizzazione, di cui alla sezione 2.4 dell'allegato del presente regolamento, a norma dell'articolo 8, paragrafo 3, lettere d) ed e), del regolamento (UE) n. 910/2014.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 §3",
        "testo": "Se un mezzo di identificazione elettronica soddisfa un requisito previsto per un livello di garanzia superiore, si ritiene che soddisfi anche il requisito equivalente del livello inferiore (principio di equivalenza crescente tra livelli).",
        "testo_integrale": "3.Se i mezzi di identificazione elettronica rilasciati nell'ambito di un regime di identificazione elettronica notificato soddisfano un requisito elencato in un livello di garanzia superiore, si ritiene che essi soddisfino il requisito equivalente di un livello di garanzia inferiore.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 §4",
        "testo": "Salvo diversa indicazione della parte pertinente dell'allegato, per essere conformi al livello di garanzia dichiarato occorre soddisfare cumulativamente tutti gli elementi elencati nell'allegato per quello specifico livello (principio di cumulatività dei requisiti).",
        "testo_integrale": "4.Salvo indicazione contraria nella parte pertinente dell'allegato, ai fini della corrispondenza al livello di garanzia dichiarato devono essere soddisfatti tutti gli elementi elencati nell'allegato per lo specifico livello di garanzia dei mezzi di identificazione elettronica rilasciati nell'ambito di un regime di identificazione elettronica notificato.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 2",
        "testo": "Il regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'UE, senza differimento della data di applicazione (a differenza di altri atti di esecuzione eIDAS2 come il Reg. (UE) 2025/1566, che invece differisce l'applicazione di 24 mesi). La formula di chiusura standard sull'obbligatorietà in tutti gli elementi e sull'applicabilità diretta in ciascuno Stato membro non costituisce un contenuto normativo autonomo (è la clausola finale standard di ogni regolamento UE self-executing) e non è qui riportata come nodo separato.",
        "testo_integrale": "Articolo 2\n\nIl presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "allegato, punto 1(1) (fonte autorevole)",
        "testo": "Definizione di «fonte autorevole»: qualsiasi fonte, in qualunque forma, su cui è possibile fare affidamento per ottenere dati, informazioni e/o elementi di prova esatti utili a dimostrare l'identità.",
        "testo_integrale": "1.Definizioni applicabili\n\nAi fini del presente allegato si intende per:\n\n(1)«fonte autorevole», qualsiasi fonte, a prescindere dalla forma, sulla quale si possa fare affidamento per l'ottenimento di dati, informazioni e/o elementi di prova esatti da utilizzare per dimostrare l'identità;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "allegato, punto 1(2) (fattore di autenticazione)",
        "testo": "Definizione di «fattore di autenticazione» (fattore associato con certezza a una persona) e delle sue tre sottocategorie: basato sul possesso (il soggetto dimostra di possederlo), basato sulla conoscenza (il soggetto dimostra di conoscerlo) e intrinseco (basato su una caratteristica fisica della persona, che il soggetto dimostra di possedere).",
        "testo_integrale": "(2)«fattore di autenticazione», un fattore associato con certezza a una persona e rientrante in una delle seguenti categorie: a)«fattore di autenticazione basato sul possesso», un fattore di autenticazione che il soggetto è tenuto a dimostrare di possedere; b)«fattore di autenticazione basato sulla conoscenza», un fattore di autenticazione che il soggetto è tenuto a dimostrare di conoscere; c)«fattore di autenticazione intrinseco», un fattore di autenticazione basato su una caratteristica fisica di una persona fisica, che il soggetto è tenuto a dimostrare di possedere;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "allegato, punto 1(3) (autenticazione dinamica)",
        "testo": "Definizione di «autenticazione dinamica»: processo elettronico che, tramite crittografia o altre tecniche, genera su richiesta una prova elettronica del controllo/possesso dei dati di identificazione da parte del soggetto, prova che cambia a ogni interazione di autenticazione tra il soggetto e il sistema che ne verifica l'identità.",
        "testo_integrale": "(3)«autenticazione dinamica», un processo elettronico che utilizza la crittografia o altre tecniche per fornire un mezzo che consente di creare su richiesta una prova elettronica che attesti il controllo o il possesso dei dati di identificazione da parte del soggetto e che cambia ad ogni interazione di autenticazione tra il soggetto e il sistema che ne verifica l'identità;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "allegato, punto 1(4) (sistema di gestione della sicurezza delle informazioni)",
        "testo": "Definizione di «sistema di gestione della sicurezza delle informazioni»: insieme di processi e procedure volti a mantenere a livelli accettabili i rischi connessi alla sicurezza delle informazioni.",
        "testo_integrale": "(4)«sistema di gestione della sicurezza delle informazioni», un insieme di processi e procedure intesi a gestire a livelli accettabili i rischi connessi alla sicurezza delle informazioni.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "allegato, punto 2 (intro)",
        "testo": "Le specifiche e procedure tecniche di questo allegato servono a determinare le modalità applicative dei requisiti e criteri dell'art. 8 eIDAS per i mezzi di identificazione elettronica rilasciati nell'ambito di un regime notificato; è la disposizione di cornice che apre l'intera sezione 2 (punti 2.1-2.4, ripartiti tra i tre capitoli di questa fonte).",
        "testo_integrale": "2.Specifiche e procedure tecniche\n\nGli elementi delle procedure e delle specifiche tecniche descritti nel presente allegato sono utilizzati per determinare in che modo sono applicati i requisiti e i criteri di cui all'articolo 8 del regolamento (UE) n.910/2014 per i mezzi di identificazione elettronica rilasciati nell'ambito di un regime di identificazione elettronica.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 1 §1",
    "art. 1 §2",
    "art. 1 §3",
    "art. 1 §4",
    "art. 2",
    "allegato, punto 1(1) (fonte autorevole)",
    "allegato, punto 1(2) (fattore di autenticazione)",
    "allegato, punto 1(3) (autenticazione dinamica)",
    "allegato, punto 1(4) (sistema di gestione della sicurezza delle informazioni)",
    "allegato, punto 2 (intro)",
    "allegato, punto 2.1.1",
    "allegato, punto 2.1.2",
    "allegato, punto 2.1.3",
    "allegato, punto 2.1.4(1)",
    "allegato, punto 2.1.4(2)",
    "allegato, punto 2.1.4(3)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI = [
    {
        "nodo_da": ("principio", None, "art. 1 §3"),
        "nodo_a": ("principio", None, "allegato, punto 2 (intro)"),
        "tipo_relazione": "si applica a",
        "evidence_type": "inferred",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("principio", None, "art. 1 §4"),
        "nodo_a": ("principio", None, "allegato, punto 2 (intro)"),
        "tipo_relazione": "si applica a",
        "evidence_type": "inferred",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("principio", None, "allegato, punto 1(1) (fonte autorevole)"),
        "nodo_a": ("obbligo", None, "allegato, punto 2.1.2"),
        "tipo_relazione": "definisce",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("principio", None, "allegato, punto 1(1) (fonte autorevole)"),
        "nodo_a": ("obbligo", None, "allegato, punto 2.1.3"),
        "tipo_relazione": "definisce",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("principio", None, "allegato, punto 1(1) (fonte autorevole)"),
        "nodo_a": ("obbligo", None, "allegato, punto 2.1.4(3)"),
        "tipo_relazione": "definisce",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
]
