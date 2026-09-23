"""Regolamento AgID recante le modalità attuative per la realizzazione dello
SPID (art. 4 comma 2 DPCM 24/10/2014), v2.0 (22/07/2016), consolidato con
Avviso AgID n.10/2018 e Determinazione AgID n.425/2020 — CAPO I
(Disposizioni generali, artt. 1-4) e CAPO II (Rilascio delle identità
digitali, artt. 5-14).

Estrazione granulare ADR-0007 dal testo ufficiale consolidato (fonte:
app/.source_cache/spid_modalita_attuative/cap01.txt). Copertura completa
per articolo: nessun discrimine di rilevanza.

Nota di modellazione — granularità ad articolo intero, non a comma/lettera:
diversamente dal precedente diretto app/seed_data/spid/cap01.py (DPCM
24/10/2014, righe a grana comma/lettera perché il DPCM è numerato in commi
e lettere autonomi), questo Regolamento AgID è redatto in prosa continua,
quasi sempre priva di numerazione di comma esplicita (gli artt. 2, 3, 5-14
non hanno "1.", "2." ecc.; solo l'art. 1 e l'art. 4 usano una numerazione
introduttiva). L'INDICE_ARTICOLI_LOCALE assegnato per questo capitolo è
esso stesso a grana articolo intero (14 item = 14 articoli), non a
comma/lettera: si è quindi scelto — coerentemente con ADR-0007, che
consente di accorpare più commi/lettere "se costituiscono un'unica
prescrizione continua" — un nodo (Obbligo o Principio) per ciascun
articolo intero, dato che ogni articolo qui tratta un'unica prescrizione o
un unico gruppo tematico continuo (es. l'intera procedura di
identificazione a vista da remoto dell'art. 8, o l'intera composizione
dell'identità digitale dell'art. 14), senza commi enumerati indipendenti
che richiedano una scomposizione ulteriore.

Classificazione per articolo:

- Art. 1 (Oggetto): Principio "scopo/ambito di applicazione" — individua le
  modalità attuative disciplinate dal regolamento, senza soggetto obbligato.
- Art. 2 (Il sistema pubblico per la gestione dell'identità digitale):
  Principio "definitorio" — descrive i soggetti del sistema SPID (utente,
  gestore dell'identità digitale, gestore di attributi qualificati,
  fornitore di servizi), il principio di necessità nel trattamento dei
  dati e i tre livelli di sicurezza (LoA2/LoA3/LoA4) dell'autenticazione
  informatica.
- Art. 3 (Adesione a SPID): Obbligo "organizzativo" — impone requisiti di
  accreditamento/convenzione a gestori e fornitori di servizi e un termine
  di adesione alle pubbliche amministrazioni.
- Art. 4 (Rilascio e gestione delle identità digitali SPID): Obbligo
  "organizzativo" — articola i processi di rilascio e di gestione del
  ciclo di vita a carico dei gestori (stesso criterio di app/seed_data/
  spid/cap01.py art. 4 c.1, "L'Agenzia cura l'attivazione... svolgendo le
  seguenti attività", anch'esso un elenco organizzativo strutturale
  modellato come Obbligo). Gli artt. 5-14 (CAPO II) specificano le singole
  fasi elencate in questo articolo: la relazione "specifica" è resa
  esplicita in RELAZIONI per ciascuna fase pertinente.
- Artt. 5-12, 14: Obbligo, tipo "procedurale" salvo l'art. 8 (vedi sotto) e
  l'art. 14 (tipo "tecnico/sicurezza": specifica requisiti tecnici
  vincolanti sul formato del codice identificativo e sulla codifica UTF-8
  degli attributi). Tutti con soggetto "QTSP/gestore" ruolo "obbligato"
  (i gestori dell'identità digitale sono i destinatari operativi di ogni
  fase del processo di rilascio); l'art. 5 aggiunge "Utente/titolare"
  "obbligato" per la sottoscrizione della dichiarazione di responsabilità
  sulla veridicità delle informazioni fornite (art. 76 D.P.R. 445/2000).
- Art. 8 (Identificazione a vista da remoto): Obbligo "tecnico/sicurezza"
  per istruzione esplicita del task — l'articolo è ricchissimo di
  prescrizioni operative sulla sessione audio/video (cifratura del canale,
  requisiti di qualità audio/video, conservazione ventennale con modalità
  crittografiche, script formalizzato in tredici passaggi lett. a)-m)),
  soggetto "QTSP/gestore" "obbligato". Il testo_integrale include, come
  ultimo paragrafo, il testo aggiunto in fine dalla Determinazione AgID
  n. 425/2020 del 1° ottobre 2020 (sui poteri del Direttore generale di
  definire ulteriori procedure di identificazione a vista da remoto,
  sentito il Garante): è testo ufficiale verbatim del regolamento
  consolidato vigente, non un'elisione — nessun marcatore di troncamento.
- Art. 13 (Conservazione e registrazione dei documenti): Obbligo "di
  conservazione" — tipo dedicato esistente in tassonomia, calzante per
  l'intero contenuto dell'articolo (documentazione da conservare per
  ciascuna modalità di identificazione, termini di conservazione,
  requisiti di integrità/disponibilità/accesso limitato e tracciato).

Nessuna relazione cross-fonte (verso CAD/eIDAS/eIDAS2/DPCM 22-2-2013/DPCM
24-10-2014) è tentata in questo modulo, anche quando il testo cita
esplicitamente un altro atto (es. art. 2, 3, 5, 6, 12, 13 citano il DPCM
24/10/2014 o il d.lgs. 196/2003): il collegamento cross-fonte è demandato
alla pipeline a posteriori di ADR-0009. Nessuna relazione è tentata verso
gli altri capitoli di questa stessa fonte (cap02/cap03/cap04) per
incertezza sui riferimenti simbolici esatti che useranno — coordinamento
via hub in corso con SpidAttCap04 sui riferimenti "art. 2"/"art. 12" per
le sue relazioni verso le Appendici A/B; le relazioni RELAZIONI di questo
modulo restano quindi tutte interne agli artt. 1-14 qui coperti.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 3",
        "testo": "Disciplina l'adesione a SPID: gestori dell'identità digitale e gestori di attributi qualificati aderiscono previo accreditamento e convenzione con AgID; i fornitori di servizi stipulano una convenzione motivando le scelte sui livelli di sicurezza e sulla necessità delle informazioni richieste; le pubbliche amministrazioni aderiscono entro ventiquattro mesi dall'accreditamento del primo gestore; AgID vigila sull'operato dei partecipanti.",
        "testo_integrale": "Possono aderire a SPID:\n\na) i gestori dell'identità digitale e i gestori di attributi qualificati, previo accreditamento e stipula di apposite convenzioni con Agid secondo le modalità definite con regolamento adottato ai sensi dell'articolo 4, comma 3, del DPCM 24 ottobre 2014; i gestori dell'identità digitale sono tenuti inoltre ad aderire alle apposite convenzioni che l'Agenzia stipula con i soggetti che attestano la validità degli attributi identificativi e consentono la verifica dei documenti di identità;\nb) i fornitori dei servizi stipulando una convenzione con l'Agenzia. Ai fini della stipula, i fornitori dei servizi indicano all'Agenzia i servizi erogati e, per ciascuno di questi servizi, motivano le scelte in relazione ai livelli di sicurezza adottati e alla necessità di informazioni richieste relative ad attributi identificativi, non identificativi e qualificati. Per i servizi qualificati, i predetti soggetti motivano le circostanze per cui le informazioni sono necessarie e non eccedenti per l'erogazione dei singoli servizi.\n\nAderiscono a SPID le pubbliche amministrazioni di cui all'articolo 2, comma 2, del CAD, entro i ventiquattro mesi successivi all'accreditamento del primo gestore dell'identità digitale.\n\nL'Agenzia vigila sull'operato dei soggetti che partecipano a SPID.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 4",
        "testo": "Definisce l'articolazione dei processi di rilascio dell'identità digitale SPID (richiesta e identificazione, esame e verifica, conservazione documenti, emissione, creazione e consegna delle credenziali) e di gestione del ciclo di vita (attributi, sospensione/revoca, conservazione/sospensione-revoca/rinnovo-sostituzione delle credenziali) a carico dei gestori dell'identità digitale.",
        "testo_integrale": "Il rilascio dell'identità digitale SPID e la gestione del ciclo di vita della stessa da parte dei gestori dell'identità digitale sono così articolati:\n\n1) Il rilascio delle identità digitali si articola nei seguenti processi:\na) richiesta dell'identità digitale e identificazione del richiedente;\nb) esame e verifica dell'identità del richiedente;\nc) conservazione e registrazione dei documenti;\nd) emissione dell'identità digitale;\ne) creazione e consegna delle credenziali.\n2) La gestione del ciclo di vita dell'identità digitale si articola nei seguenti processi:\na) gestione degli attributi;\nb) sospensione e revoca dell'identità;\nc) gestione del ciclo di vita delle credenziali che si articola in:\n1) conservazione;\n2) sospensione e revoca;\n3) rinnovo e sostituzione.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 5",
        "testo": "Disciplina la richiesta di identità digitale: il gestore rilascia l'identità su richiesta tramite modulo di adesione contenente i dati identificativi e secondari obbligatori (persona fisica/giuridica), la verifica di email e telefono mobile, e la dichiarazione di responsabilità sottoscritta dal richiedente sulla veridicità delle informazioni fornite.",
        "testo_integrale": "Le identità digitali sono rilasciate dal gestore dell'identità digitale, su richiesta di un soggetto interessato secondo quanto previsto dall'art. 7 del DPCM mediante presentazione di un modulo di richiesta di adesione che contiene tutte le informazioni necessarie per l'identificazione del soggetto richiedente.\n\nIl modulo di richiesta di adesione contiene:\n\na) i dati identificativi del richiedente, che costituiscono gli attributi identificativi dell'identità digitale;\nb) le informazioni che consentono di gestire in maniera efficace il rapporto tra il gestore delle identità digitali e il richiedente dell'identità digitale, che costituiscono gli attributi secondari dell'identità digitale;\n\nPer le persone fisiche sono obbligatorie le seguenti informazioni:\n\na) cognome e nome;\nb) sesso, data e luogo di nascita;\nc) codice fiscale;\nd) estremi di un valido documento di identità\ne) gli attributi secondari così come definiti all'art. 1 comma 1 lettera d) del DPCM.\n\nPer le persone giuridiche sono obbligatorie le seguenti informazioni:\n\na) denominazione/ragione sociale;\nb) codice fiscale o P.IVA (se uguale al codice fiscale);\nc) sede legale;\nd) visura camerale attestante lo stato di rappresentante legale del soggetto richiedente l'identità per conto della società (in alternativa atto notarile di procura legale);\ne) estremi del documento di identità utilizzato dal rappresentante legale;\nf) gli attributi secondari così come definiti all'art. 1 comma 1 lettera d) del DPCM.\n\nPer gli attributi secondari, sono forniti almeno un indirizzo di posta elettronica e un recapito di telefonia mobile, entrambi verificati dal gestore di identità digitale nel corso del processo di identificazione, inviando un messaggio di posta all'indirizzo dichiarato, contenente una URL per la verifica e un SMS al numero di cellulare con un codice numerico di controllo che deve essere riportato in risposta. Inoltre, per quanto riguarda l'indirizzo di posta elettronica, i gestori dovranno accertarsi che lo stesso sia un indirizzo corrispondente a una reale casella di posta.\n\nNel modulo, il soggetto richiedente sottoscrive l'apposita dichiarazione con cui si assume la responsabilità, ai sensi dell'articolo 76 del decreto del Presidente della Repubblica 28 dicembre 2000, n. 445, della veridicità delle informazioni fornite.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 6",
        "testo": "Il gestore dell'identità digitale identifica il richiedente al ricevimento della richiesta tramite personale qualificato e formato, fornisce l'informativa sul trattamento dei dati, assicura la consapevolezza del richiedente su termini/condizioni e precauzioni d'uso (proponendo il servizio di segnalazione ex art. 18) e acquisisce i dati necessari alla dimostrazione dell'identità.",
        "testo_integrale": "Al ricevimento della richiesta, il gestore dell'identità digitale procede all'identificazione del soggetto richiedente, che consiste nell'accertamento delle informazioni sufficienti a identificare il soggetto richiedente sulla base di documenti forniti dallo stesso. Tale processo è effettuato da personale qualificato e opportunamente formato.\n\nLe modalità di consegna della richiesta e il supporto utilizzato (cartaceo o digitale) dipendono da quale modalità, tra quelle previste dall'art. 7 del DPCM il gestore dell'identità digitale adotta per operare il processo di identificazione.\n\nIl gestore dell'identità digitale, per una corretta e sicura attuazione del processo,\n\na) fornisce l'informativa sul trattamento dei dati (articolo 13 del D.lgs. 196 del 2003);\nb) si assicura che il richiedente sia consapevole dei termini e delle condizioni associati all'utilizzo del servizio di identità digitale;\nc) si assicura che il richiedente sia consapevole delle raccomandazioni e delle precauzioni da adottare per l'uso delle identità digitale e propone l'attivazione del servizio di segnalazione di cui all'art. 18;\nd) acquisisce i dati necessari alla dimostrazione di identità.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7",
        "testo": "Nell'identificazione a vista presso le sedi individuate, il richiedente presenta il modulo cartaceo sottoscritto e un documento di identità valido (per le persone giuridiche anche la visura camerale e l'identificazione del rappresentante legale); l'operatore verifica il documento e il codice fiscale tramite tessera sanitaria e sospende o blocca l'iscrizione se i documenti sono carenti.",
        "testo_integrale": "Nel caso di identificazione a vista del soggetto richiedente presso le sedi allo scopo individuate si procede con l'acquisizione del modulo di richiesta di adesione in formato cartaceo compilato e sottoscritto dall'utente e con l'esibizione di un valido documento di identità.\n\nNel caso in cui il soggetto richiedente sia una persona giuridica, deve essere fornita la visura camerale attestante i poteri di rappresentanza conferiti alla persona fisica che sottoscrive e presenta l'istanza. Il rappresentante legale dovrà a sua volta essere identificato tramite un valido documento d'identità.\n\nL'operatore che effettua l'identificazione accerta l'identità del richiedente tramite la verifica di un documento di riconoscimento integro e in corso di validità rilasciato da un'Amministrazione dello Stato, munito di fotografia e firma autografa dello stesso e controlla la validità del codice fiscale verificando la tessera sanitaria anch'essa in corso di validità.\n\nSe i documenti esibiti dal richiedente risultano carenti delle caratteristiche di cui sopra, deve esserne esclusa l'ammissibilità e il processo di iscrizione deve essere sospeso o bloccato fino all'esibizione di documenti validi e integri.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 8",
        "testo": "Disciplina l'identificazione a vista da remoto tramite audio/video: cifratura del canale prima della sessione, requisiti di qualità audio/video, verifica del documento di riconoscimento e del codice fiscale, facoltà dell'operatore di escludere l'ammissibilità della sessione, registrazione conservata venti anni con accesso crittograficamente limitato, procedura scritta formalizzata in tredici passaggi (lett. a)-m)) e possibilità per il Direttore generale AgID, sentito il Garante, di definire ulteriori procedure (paragrafo aggiunto dalla Determinazione AgID n.425/2020).",
        "testo_integrale": "L'identificazione a vista della persona fisica richiedente un'identità SPID da parte del gestore dell'identità può essere effettuata dai gestori dell'identità digitale anche in digitale da remoto tramite strumenti di registrazione audio/video nel rispetto del decreto legislativo 30 giugno 2003, n.196.\n\nIl gestore deve implementare un sistema che garantisca, preliminarmente all'instaurazione della sessione audio/video, la cifratura del canale di comunicazione mediante l'adozione di meccanismi standard, applicativi e protocolli aggiornati alla versione più recente. Inoltre deve garantire l'utilizzo di applicativi orientati all'usabilità e all'accessibilità da parte dell'utente.\n\nL'identificazione da remoto deve avvenire in una modalità tale da consentire la raccolta di elementi probanti, utili in caso di un eventuale disconoscimento dell'identità da parte dell'utente nel rispetto delle seguenti condizioni:\n\na) le immagini video devono essere a colori e consentire una chiara visualizzazione dell'interlocutore in termini di luminosità, nitidezza, contrasto, fluidità delle immagini;\nb) l'audio deve essere chiaramente udibile, privo di evidenti distorsioni o disturbi.\nc) la sessione audio/video, che ha ad oggetto le immagini video e l'audio del soggetto richiedente l'identità e dell'operatore, deve essere effettuata in ambienti privi di particolari elementi di disturbo.\n\nIl gestore è responsabile della valutazione in merito alla sussistenza delle condizioni suddette e l'operatore preposto all'attività può sospendere o non avviare il processo di identificazione nel caso in cui la qualità audio/video sia scarsa o ritenuta non adeguata a consentire la verifica dell'identità del soggetto.\n\nL'operatore che effettua l'identificazione accerta l'identità del richiedente tramite la verifica di un documento di riconoscimento in corso di validità, purché munito di fotografia recente e riconoscibile e firma autografa del richiedente stesso, rilasciato da un'Amministrazione dello Stato e verifica il codice fiscale tramite la tessera sanitaria in corso di validità.\n\nL'operatore che effettua l'identificazione può escludere l'ammissibilità della sessione audio/video per qualunque ragione, inclusa l'eventuale inadeguatezza del documento presentato dal richiedente (ad esempio perché logoro o carente delle caratteristiche elencate).\n\nLa sessione audio/video è interamente registrata e conservata per venti anni decorrenti dalla scadenza o dalla revoca dell'identità digitale con modalità crittografiche atte a garantirne l'accesso esclusivamente dietro richiesta dell'autorità giudiziaria, dell'Agenzia nel corso delle attività di vigilanza, dell'utente e dell'autorità giudiziaria in caso di disconoscimento della stessa.\n\nNel caso l'identificazione a vista da remoto sia solo una delle modalità predisposte per la verifica dell'identità del richiedente, il gestore dell'identità deve richiedere il consenso al trattamento dei dati personali contenuti nelle riprese audio-video, specificando tale aspetto nell'informativa da rendere all'interessato ai sensi dell'articolo 13 del Codice. Nel caso in cui l'identificazione a vista da remoto sia l'unica modalità disponibile per la verifica dell'identità del richiedente, ciò deve essere messo in specifica evidenza, oltre che nelle condizioni e termini del contratto, anche nell'informativa da rendere all'interessato ai sensi dell'articolo 13 del Codice.\n\nLa sessione audio/video deve essere condotta seguendo una procedura scritta e formalizzata dal gestore che prevede almeno le seguenti attività:\n\na) l'acquisizione del consenso, qualora necessario, alla videoregistrazione e alla sua conservazione per 20 anni come previsto dalla normativa vigente in materia. L'operatore informa che la videoregistrazione sarà conservata in modalità protetta;\nb) l'operatore dichiara i propri dati identificativi;\nc) il soggetto conferma le proprie generalità;\nd) il soggetto conferma la data e l'ora della registrazione;\ne) il soggetto conferma di volersi dotare di un'identità digitale e conferma i dati inseriti nella modulistica online in fase di pre-registrazione;\nf) il soggetto conferma il proprio numero di telefonia mobile e l'indirizzo mail;\ng) l'operatore invia un sms che il soggetto richiedente è tenuto a esporre al dispositivo di ripresa e una mail all'indirizzo di posta elettronica dichiarato, con un link ad una URL appositamente predisposta per la verifica;\nh) l'operatore chiede e ottiene conferma dal soggetto circa la conoscenza delle tipologie di credenziali di cui disporrà per l'accesso ai servizi in rete;\ni) l'operatore chiede di inquadrare, fronte e retro, il documento di riconoscimento utilizzato dal soggetto, assicurandosi che sia possibile visualizzare chiaramente la fotografia e leggere tutte le informazioni contenute nello stesso (dati anagrafici, numero del documento, data di rilascio e di scadenza, amministrazione rilasciante);\nj) l'operatore chiede di mostrare la tessera sanitaria su cui è riportato il codice fiscale del soggetto;\nk) il soggetto conferma di aver preso visione e di accettare le condizioni contrattuali e d'uso disponibili sul sito web del gestore di identità;\nl) l'operatore chiede al soggetto di compiere una o più azioni casuali volte a rafforzare l'autenticità della richiesta;\nm) l'operatore riassume sinteticamente la volontà espressa dal soggetto di dotarsi di identità digitale e raccoglie conferma dallo stesso.\n\nI dati di registrazione, costituiti da file audio-video, immagini e metadati strutturati in formato elettronico, vengono conservati e trattati in base all'articolo 7, commi 8 e 9 del DPCM.\n\nPer la conservazione dei dati di registrazione si applica quanto stabilito all'articolo 13.\n\nCon una o più determinazioni del Direttore generale, da adottare acquisito il parere del Garante per la protezione dei dati personali, possono essere definite ulteriori procedure di identificazione a vista da remoto che, pubblicate sul sito istituzionale dell'Agenzia, costituiscono parte integrante del presente regolamento. [Paragrafo aggiunto all'articolo 8, in fine, dalla Determinazione AgID n. 425/2020 del 1° ottobre 2020]",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 9",
        "testo": "Nell'identificazione informatica tramite documenti digitali di identità (TS-CNS, CNS o carte conformi ex art. 64 CAD), il gestore verifica i documenti digitali che prevedono riconoscimento a vista all'attivazione e garantisce che la richiesta di rilascio dell'identità digitale sia riconducibile all'uso di tali strumenti.",
        "testo_integrale": "Nel caso di identificazione informatica tramite documenti digitali di identità di cui all'art. 64 del Dlgs. n.82/2005, l'identificazione avviene tramite verifica dei documenti digitali che prevedono il riconoscimento a vista del richiedente all'atto dell'attivazione, fra cui la tessera sanitaria-carta nazionale dei servizi (TS-CNS), CNS o carte ad essa conformi. Il gestore dell'identità digitale deve garantire che la richiesta di rilascio dell'identità digitale sia riconducibile all'utilizzo degli strumenti di cui al presente articolo.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10",
        "testo": "L'identificazione informatica tramite altre identità SPID avviene con modulo digitale sottoscritto elettronicamente e accesso con credenziali SPID di livello di sicurezza pari o superiore a quello oggetto della richiesta, applicabile solo quando la nuova identità è richiesta presso lo stesso gestore che ha rilasciato l'identità SPID utilizzata.",
        "testo_integrale": "Nel caso di identificazione informatica tramite altre identità SPID si procede con l'acquisizione del modulo di richiesta di adesione in formato digitale, messo a disposizione in rete dal gestore dell'identità digitale, compilato e sottoscritto elettronicamente (ad esempio con firme qualificate valide solo per la sessione in corso o per un periodo limitato). L'identificazione avviene attraverso l'accesso, utilizzando credenziali SPID di livello di sicurezza pari o superiore a quella oggetto della richiesta, a un servizio reso disponibile allo scopo da parte dal gestore dell'identità digitale. Questa modalità di identificazione è applicabile quando la richiesta di una nuova identità è effettuata presso lo stesso gestore che ha rilasciato l'identità SPID utilizzata per la richiesta.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11",
        "testo": "L'identificazione informatica tramite firma elettronica qualificata o firma digitale avviene con modulo digitale sottoscritto con tale firma; il gestore verifica la firma apposta sulla richiesta e considera la fase di identificazione espletata dal fornitore della firma qualificata o digitale.",
        "testo_integrale": "Nel caso di identificazione informatica tramite firma elettronica qualificata o firma digitale si procede con l'acquisizione del modulo di richiesta di adesione in formato digitale, messo a disposizione in rete dal gestore dell'identità digitale, compilato e sottoscritto con firma elettronica qualificata o con firma digitale. L'identificazione avviene tramite la verifica della firma elettronica qualificata o firma digitale apposta sulla richiesta. Anche in questo caso il gestore delle identità digitali, considera che la fase di identificazione sia stata correttamente espletata dal fornitore di firma elettronica qualificata o digitale.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 12",
        "testo": "Il gestore verifica l'identità dichiarata tramite fonti autoritative istituzionali (convenzioni ex art. 4 c.1 lett.c) DPCM o, in mancanza, archivi delle amministrazioni certificanti) e il servizio di verifica del codice fiscale dell'Agenzia delle Entrate, secondo requisiti differenziati per persona fisica e persona giuridica riportati in tabella, con rinvio all'Appendice B per le minacce al processo di verifica.",
        "testo_integrale": "La verifica dell'identità consiste nel rafforzamento del livello di attendibilità degli attributi di identità, raccolti in fase di identificazione, compiuta attraverso accertamenti effettuati tramite fonti autoritative istituzionali, in grado di dare conferma della veridicità dei dati raccolti.\n\nL'accesso alle fonti autoritative da parte dei gestori dell'identità ai fini dell'attività di verifica è effettuato secondo le convenzioni di cui all'articolo 4, comma 1, lettera c) del DPCM e, nei casi in cui le informazioni necessarie non siano accessibili per mezzo dei servizi convenzionati, tramite verifiche sulla base di documenti, dati o informazioni ottenibili da archivi delle amministrazioni certificanti, ai sensi dell'art. 43, comma 2, del D.P.R. 28 dicembre 2000, n. 445.\n\nI gestori dell'identità digitale e i gestori degli attributi qualificati usufruiscono del servizio di verifica del codice fiscale e dei dati anagrafici ad esso strettamente correlati fornito dall'Agenzia delle Entrate.\n\nSia il processo di identificazione che il processo di verifica sono eseguiti allo scopo di ottenere un adeguato grado di affidabilità, tenuto conto anche dello specifico livello di sicurezza di SPID.\n\nLe tabelle seguenti rappresentano i requisiti relativi alla verifica di identità in relazione al livello di sicurezza nel caso di persona fisica e di persona giuridica.\n\nTabella - Requisiti da soddisfare per la verifica di identità (persona fisica), validi per tutti i livelli di sicurezza SPID:\n1) Può essere ragionevolmente assunto che la persona in possesso dei documenti di identità e codice fiscale/tessera sanitaria rappresenti l'identità dichiarata.\n2) I documenti sono autentici e validi sulla base di quanto risulta da soggetti istituzionali competenti (articolo 4, comma 1, lettera c del DPCM o, in assenza di convenzioni con l'Agenzia, tramite verifiche sulla base di documenti, dati o informazioni ottenibili da archivi delle amministrazioni certificanti, ai sensi dell'art. 43, comma 2, del D.P.R. 28 dicembre 2000, n. 445). Il richiedente viene identificato usando le informazioni ottenute da soggetti istituzionali competenti con i quali l'Agenzia stipulerà apposite convenzioni.\n\nTabella - Requisiti da soddisfare per la verifica di identità (persona giuridica), validi per tutti i livelli di sicurezza SPID:\n1) L'esistenza della persona giuridica è basata su evidenze riconosciute dal sistema delle imprese in ambito nazionale.\n2) Le evidenze sono tutte valide e autentiche sulla base di quanto risulta da soggetti istituzionali competenti.\n3) Effettuata l'associazione amministratore o rappresentante legale, all'impresa-persona giuridica, si procede alla verifica-come persona fisica-dell'amministratore o del legale rappresentante, come indicato nella tabella precedente per l'identificazione di una persona fisica.\n\nIn merito alle possibili minacce associabili al processo di verifica dell'identità, si veda l'Appendice B al presente documento.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 13",
        "testo": "I gestori conservano i riscontri dei processi di identificazione (a vista, remota audio/video, informatica, tramite firma) e di verifica per l'intera documentazione di creazione/rilascio dell'identità digitale ai sensi dell'art. 7 commi 8-9 DPCM, con un processo formalizzato che garantisce integrità, disponibilità, accesso limitato e tracciato ai soli soggetti designati, soggetto a valutazione di adeguatezza da parte di AgID in sede di vigilanza.",
        "testo_integrale": "Il processo di registrazione dei documenti completa la fase di rilascio di un'identità SPID a un soggetto. La documentazione da conservare include le informazioni e i documenti che sono stati raccolti nel corso dell'attività di registrazione. I gestori dell'identità digitale, al fine di poter documentare la corretta esecuzione dei precedenti processi relativi all'attività di rilascio e di verifica, conservano i riscontri relativi ai processi di identificazione e verifica.\n\nIn merito al processo di richiesta e identificazione del richiedente devono essere conservati:\n\n1) nel caso di identificazione tramite esibizione a vista:\na) identificazione \"de visu\": copia per immagine di tutta la documentazione esibita (documento d'identità e codice fiscale per persone fisiche, procura per persone giuridiche) e modulo di richiesta su supporto cartaceo sottoscritto in modalità autografa;\nb) identificazione remota con strumenti audio/video: i dati di registrazione, nonché l'esplicita volontà del soggetto di dotarsi di identità digitale memorizzati in file audio-video, immagini e metadati strutturati in formato elettronico;\n2) nel caso di identificazione informatica:\na) log della transazione contestualizzato alla specifica richiesta di rilascio dell'identità SPID;\n3) nel caso di firma elettronica qualificata o digitale:\na) modulo di richiesta di adesione allo SPID in formato digitale sottoscritto digitalmente;\nb) tutti i documenti e dati utilizzati per l'associazione e la verifica degli attributi.\n\nIn merito al processo di verifica devono essere conservati i riscontri ottenuti a seguito degli accessi alle fonti autoritative.\n\nTutta la documentazione inerente alla creazione e al rilascio di una identità digitale deve essere conservata ai sensi dell'articolo 7, commi 8 e 9, del DPCM.\n\nAl fine della conservazione, il gestore predispone e formalizza un processo di conservazione atto a garantire l'integrità, la disponibilità e la protezione delle informazioni conservate, siano esse analogiche o digitali. Tale processo deve garantire che l'accesso alle informazioni conservate sia limitato esclusivamente a soggetti appositamente designati, per la gestione di motivate richieste da parte dell'utente ovvero per le attività svolte in sede di vigilanza o da parte dell'autorità giudiziaria. Ogni accesso deve essere rilevato, riscontrabile nel tempo, consentire di accertare quando e quali soggetti hanno acceduto alla specifica informazione e la causale dell'accesso. In sede di vigilanza l'Agenzia valuta l'adeguatezza del processo e ne verifica l'effettiva applicazione.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 14",
        "testo": "Espletati i processi precedenti, il gestore crea e rilascia l'identità digitale composta da attributi identificativi, attributi secondari e codice identificativo; il codice identificativo (4 lettere + 10 caratteri alfanumerici univoci nel dominio del gestore) è assegnato dal gestore e deve essere univoco in ambito SPID; la codifica degli attributi deve usare lo standard UTF-8 (RFC 3629).",
        "testo_integrale": "Espletate con successo tutte le attività previste dai processi precedenti, l'identità digitale viene creata e rilasciata dal gestore. L'identità digitale è costituita da un insieme di attributi:\n\na) attributi identificativi, come specificato dalla lettera c) del comma 1 dell'articolo 1 del DPCM;\nb) attributi secondari, come specificato dalla lettera d) del comma 1 dell'articolo 1 del DPCM;\nc) codice identificativo, come specificato dalla lettera g) del comma 1 dell'articolo 1 del DPCM;\n\nIl codice identificativo è assegnato dal gestore dell'identità digitale, deve essere univoco in ambito SPID. Tale codice identificativo è definito dalla seguente regola:\n\n<codice Identificativo> = <cod_IdP><numero unico> Dove:\n\na) <cod_IdP>: è un codice composto da 4 lettere;\nb) <numero unico>: è un codice alfanumerico composto da 10 caratteri univoco nel dominio del gestore.\n\nAl fine di supportare anche i caratteri diacritici la codifica degli attributi, primari e secondari di SPID, deve essere effettuata utilizzando lo standard UTF-8 (RFC 3629).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 1",
        "testo": "Il regolamento individua le modalità attuative per l'adesione dei soggetti a SPID previo accreditamento e convenzione, il rilascio dell'identità digitale previa verifica dell'identità del richiedente, la gestione del ciclo di vita (sospensione e revoca comprese), l'autenticazione del richiedente e il monitoraggio da parte di AgID.",
        "testo_integrale": "Ai fini della realizzazione di SPID, il presente regolamento individua le modalità attuative:\na) con cui i soggetti aderiscono al sistema, previo accreditamento e stipula di convenzioni;\nb) di rilascio dell'identità digitale, previa verifica dell'identità del soggetto richiedente e rilascio delle credenziali;\nc) di gestione del ciclo di vita dell'identità digitale, ivi compresa la sospensione e la revoca;\nd) di autenticazione del soggetto che richiede il servizio;\ne) di monitoraggio da parte dell'Agid.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 2",
        "testo": "Descrive i soggetti del sistema SPID (utente, gestore dell'identità digitale, gestore di attributi qualificati, fornitore di servizi), il principio di necessità nel trattamento dei dati e i tre livelli di sicurezza (LoA2/LoA3/LoA4, corrispondenti a ISO/IEC 29115) dell'autenticazione informatica, rinviando all'Appendice A per la relativa metodologia di attribuzione.",
        "testo_integrale": "SPID prevede diversi soggetti:\n\na) l'utente, che potrà disporre di uno o più identità digitali, che contengono alcune informazioni identificative obbligatorie, come il codice fiscale, il nome, il cognome, il luogo di nascita, la data di nascita e il sesso;\nb) il gestore dell'identità digitale. Si tratta di un soggetto, che dovrà essere accreditato dall'Agenzia per l'Italia Digitale e che avrà il ruolo di creare e gestire le identità digitali;\nc) il gestore di attributi qualificati che, in base alle norme vigenti, può certificare attributi qualificati, come il possesso di un titolo di studio, l'appartenenza ad un ordine professionale;\nd) il fornitore di Servizi – soggetto pubblico o privato – che eroga servizi on-line, previo riconoscimento dell'utente da parte del gestore dell'identità digitale.\n\nIl Sistema SPID si conforma al principio di necessità nel trattamento dei dati di cui all'articolo 3 del decreto legislativo 30 giugno 2003, n. 196, in base al quale i sistemi informativi e i programmi informatici sono configurati riducendo al minimo l'utilizzazione di dati personali e di dati identificativi. I trattamenti dei dati personali in applicazione del presente regolamento sono effettuati esclusivamente per le finalità previste dall'articolo 64 del CAD e dall'articolo 2, comma 2, del DPCM 24 ottobre 2014 e con le modalità individuate dal presente regolamento, nel rispetto delle garanzie previste dal medesimo decreto legislativo n. 196 del 2003.\n\nIl sistema SPID è basato su tre livelli di sicurezza di autenticazione informatica.\n\nIl processo di autenticazione informatica è diretto alla verifica dell'identità digitale associata a un soggetto ai fini della erogazione di un servizio fornito in rete. A tale verifica di identità è associato un livello di sicurezza o di garanzia (level of assurance-LoA) progressivamente crescente in termini di sicurezza.\n\nIl livello di sicurezza è il risultato dell'intero procedimento che sottende all'attività di autenticazione. Tale processo va dalla preliminare associazione tra un soggetto e un'identità digitale che lo rappresenta in rete, con annessa attribuzione di credenziali in grado di comprovare tale associazione, ai meccanismi che realizzano il protocollo di autenticazione al momento della richiesta di un servizio in rete. In SPID sono definiti tre livelli di sicurezza, corrispondenti ad altrettanti livelli specificati nella ISO-IEC 29115, rispetto al rischio di uso abusivo o alterazione di identità. In particolare:\n\na) livello 1 (corrispondente al LoA2 dell'ISO-IEC 29115): è caratterizzato da un'affidabilità e una qualità delle specifiche tecniche, norme e procedure dello strumento di identificazione elettronica tali da ridurre il rischio di uso abusivo o di alterazione di identità. A tale livello è associato un rischio moderato e compatibile con l'impiego di un sistema autenticazione a singolo fattore, ad es. la password; questo livello può essere considerato applicabile nei casi in cui il danno causato, da un utilizzo indebito dell'identità digitale, ha un basso impatto per le attività del cittadino/impresa/amministrazione;\nb) livello 2 (corrispondente al LoA3 dell'ISO-IEC 29115): è caratterizzato da un'affidabilità e una qualità delle specifiche tecniche, norme e procedure dello strumento di identificazione elettronica tali da ridurre significativamente il rischio di uso abusivo o di alterazione di identità. A tale livello è associato un rischio notevole e compatibile con l'impiego di un sistema di autenticazione informatica a due fattori non necessariamente basato su certificati digitali; questo livello è adeguato per tutti i servizi per i quali un indebito utilizzo dell'identità digitale può provocare un danno consistente;\nc) livello 3 (corrispondente al LoA4 dell'ISO-IEC 29115): è caratterizzato da un'affidabilità e una qualità delle specifiche tecniche, norme e procedure dello strumento di identificazione elettronica il cui scopo è quello di impedire l'uso abusivo o l'alterazione dell'identità e garantisce con un altissimo grado di affidabilità l'identità accertata nel corso dell'attività di autenticazione. A tale livello è associato un rischio altissimo e compatibile con l'impiego di un sistema di autenticazione informatica a due fattori basato su certificati digitali e criteri di custodia delle chiavi private su dispositivi che soddisfano i requisiti dell'Allegato II del Regolamento 910/2014; questo è il livello di garanzia più elevato e da associare a quei servizi che possono subire un serio e grave danno per cause imputabili ad abusi di identità; questo livello è adeguato per tutti i servizi per i quali un indebito utilizzo dell'identità digitale può provocare un danno serio e grave.\n\nAi sensi dell'articolo 6, commi 4 e 5, del DPCM 24 ottobre 2014 (di seguito: \"DPCM\"), i fornitori di servizi scelgono il livello di sicurezza SPID necessario per accedere ai propri servizi e non possono discriminare l'accesso ai propri servizi sulla base del gestore di identità che l'ha fornita.\n\nNell'Appendice A è riportata, a titolo esemplificativo, una metodologia da adottare allo scopo.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 1 (Oggetto)",
    "art. 2 (Il sistema pubblico per la gestione dell'identità digitale)",
    "art. 3 (Adesione a SPID)",
    "art. 4 (Rilascio e gestione delle identità digitali SPID)",
    "art. 5 (Richiesta dell'identità digitale)",
    "art. 6 (Identificazione del soggetto richiedente)",
    "art. 7 (Identificazione a vista del soggetto richiedente)",
    "art. 8 (Identificazione a vista da remoto)",
    "art. 9 (Identificazione informatica tramite documenti digitali di identità)",
    "art. 10 (Identificazione informatica tramite altre identità SPID)",
    "art. 11 (Identificazione informatica tramite firma elettronica qualificata o firma digitale)",
    "art. 12 (Verifica dell'identità dichiarata)",
    "art. 13 (Conservazione e registrazione dei documenti)",
    "art. 14 (Emissione dell'identità digitale)",
]

MAPPATURA_LOCALE = {
    "art. 1": ["art. 1 (Oggetto)"],
    "art. 2": ["art. 2 (Il sistema pubblico per la gestione dell'identità digitale)"],
    "art. 3": ["art. 3 (Adesione a SPID)"],
    "art. 4": ["art. 4 (Rilascio e gestione delle identità digitali SPID)"],
    "art. 5": ["art. 5 (Richiesta dell'identità digitale)"],
    "art. 6": ["art. 6 (Identificazione del soggetto richiedente)"],
    "art. 7": ["art. 7 (Identificazione a vista del soggetto richiedente)"],
    "art. 8": ["art. 8 (Identificazione a vista da remoto)"],
    "art. 9": ["art. 9 (Identificazione informatica tramite documenti digitali di identità)"],
    "art. 10": ["art. 10 (Identificazione informatica tramite altre identità SPID)"],
    "art. 11": ["art. 11 (Identificazione informatica tramite firma elettronica qualificata o firma digitale)"],
    "art. 12": ["art. 12 (Verifica dell'identità dichiarata)"],
    "art. 13": ["art. 13 (Conservazione e registrazione dei documenti)"],
    "art. 14": ["art. 14 (Emissione dell'identità digitale)"],
}

RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "art. 3"),
        "nodo_a": ("principio", None, "art. 1"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "art. 4"),
        "nodo_a": ("principio", None, "art. 1"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "art. 5"),
        "nodo_a": ("obbligo", None, "art. 4"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, "art. 6"),
        "nodo_a": ("obbligo", None, "art. 4"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, "art. 6"),
        "nodo_a": ("obbligo", None, "art. 5"),
        "tipo_relazione": "richiede come precondizione",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7"),
        "nodo_a": ("obbligo", None, "art. 6"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "art. 8"),
        "nodo_a": ("obbligo", None, "art. 6"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9"),
        "nodo_a": ("obbligo", None, "art. 6"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "art. 10"),
        "nodo_a": ("obbligo", None, "art. 6"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "art. 11"),
        "nodo_a": ("obbligo", None, "art. 6"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "art. 8"),
        "nodo_a": ("obbligo", None, "art. 13"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", None, "art. 12"),
        "nodo_a": ("obbligo", None, "art. 4"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "art. 12"),
        "nodo_a": ("obbligo", None, "art. 6"),
        "tipo_relazione": "richiede come precondizione",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "art. 13"),
        "nodo_a": ("obbligo", None, "art. 4"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "art. 13"),
        "nodo_a": ("obbligo", None, "art. 12"),
        "tipo_relazione": "richiede come precondizione",
        "evidence_type": "textual",
        "confidence": 0.65,
    },
    {
        "nodo_da": ("obbligo", None, "art. 14"),
        "nodo_a": ("obbligo", None, "art. 4"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("obbligo", None, "art. 14"),
        "nodo_a": ("obbligo", None, "art. 13"),
        "tipo_relazione": "richiede come precondizione",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("principio", None, "art. 2"),
        "nodo_a": ("obbligo", None, "art. 10"),
        "tipo_relazione": "definisce",
        "evidence_type": "textual",
        "confidence": 0.6,
    },
]
