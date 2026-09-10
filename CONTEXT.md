# CONTEXT.md

Glossario di dominio per il censimento strutturato degli obblighi normativi applicabili ai servizi fiduciari qualificati (QTSP). Progetto separato da `RAG-QTSP/sgsi-rag` (RAG documentale generico su SGSI/ISO27001), affiancato ad esso.

## Entità

### Fonte (normativa)

L'atto normativo o standard nella sua interezza (es. "Regolamento eIDAS", "CAD - D.Lgs. 82/2005", "ETSI EN 319 401"). Esiste una volta sola nel censimento. Ha propri metadati: versione, data di entrata in vigore, stato (vigente / abrogata / in transizione), **URL sorgente ufficiale** (es. pagina EUR-Lex o Normattiva da cui il testo è stato scaricato, usata sia per il caricamento iniziale sia per i controlli periodici di aggiornamento).

Una Fonte contiene molti Obblighi, ciascuno con un riferimento puntuale (articolo/comma/allegato) al suo interno.

### Obbligo (= Requisito)

L'unità atomica del censimento: una prescrizione normativa specifica che impone un comportamento a un soggetto. "Obbligo" e "Requisito" sono usati come **sinonimi** — "obbligo" è il termine canonico nello schema dati, "requisito" è il modo colloquiale in cui l'utente formula una domanda ("quali requisiti mi impattano questo dubbio?"), ma la risposta è sempre espressa in termini di Obblighi.

Attributi:
- **Fonte** + **riferimento puntuale** (articolo/comma/allegato all'interno della Fonte)
- **Soggetto obbligato** — chi deve materialmente rispettare l'obbligo
- **Destinatario/beneficiario** — a favore di chi è posto l'obbligo (può differire dal soggetto obbligato)
- **Testo dell'obbligo** (estratto letterale o parafrasi normalizzata)
- **Tipo di obbligo** (organizzativo, tecnico/di sicurezza, informativo/di trasparenza, procedurale, di conservazione, sanzionatorio, ...)
- **Stato/validità temporale** (vigente, abrogato, in transizione eIDAS→eIDAS2)
- **Severità/rischio di non conformità** (scala qualitativa)
- **Sanzioni previste** (se sì: tipo e riferimento normativo della sanzione)
- **Validato da / data di validazione** — chi ha validato la bozza generata dall'LLM e quando (pilota a uso individuale: un solo possibile valore, ma il campo resta per uno storico minimo)
- **Condizione di applicabilità** — testo libero che descrive un fatto esterno non tracciato nel censimento da cui dipende l'applicabilità dell'obbligo (es. "solo se il breach riguarda dati qualificati"). Distinta dalla relazione "è condizionato da" (vedi sotto), che collega a un altro Obbligo tracciato.

Soggetto obbligato e Destinatario/beneficiario sono attributi **indipendenti**: non sono in corrispondenza fissa, e ciascuno assume valori dall'insieme delle Categorie di soggetto (vedi sotto). Un obbligo può avere più valori per ciascuno dei due attributi.

### Principio

Il secondo tipo di nodo del censimento (accanto a Obbligo): una disposizione normativa che **non impone un comportamento a un soggetto**, ma stabilisce un effetto giuridico, una presunzione legale o un divieto di discriminazione — es. art. 25 eIDAS ("a una firma elettronica non sono negati gli effetti giuridici e l'ammissibilità come prova in giudizio per il solo motivo della sua forma elettronica"). Non ha soggetto obbligato: è per questo che non rientra nella definizione di Obbligo, non per un limite di estrazione.

Attributi:
- **Fonte** + **riferimento puntuale**, come per l'Obbligo
- **Testo del principio** (estratto letterale o parafrasi normalizzata)
- **Tipo di principio**: non discriminazione, equivalenza giuridica, valore probatorio, presunzione legale, altro
- **Oggetto giuridico** a cui si applica — multi-valore, dall'insieme: firma elettronica (semplice/avanzata/qualificata), sigillo elettronico (semplice/avanzato/qualificato), marca temporale elettronica qualificata, documento elettronico, servizio di recapito elettronico certificato, identificazione elettronica, altro. Questo attributo è ciò che permette a una domanda come "può un giudice non considerare un documento firmato elettronicamente?" di trovare l'art. 25 anche se il testo letterale non contiene "giudice" o "documento": la domanda si aggancia all'oggetto giuridico, non solo al testo.
- **Stato/validità temporale**, **condizione di applicabilità**, **stato di validazione/validato da/data di validazione** — stessa semantica dell'Obbligo (lookup `stati_norma`, condiviso tra i due tipi di nodo)

Perimetro: qualunque norma dichiarativa di eIDAS o CAD, non solo quelle relative a strumenti gestiti dai QTSP — decisione presa perché l'utente deve poter rispondere a quesiti operativi reali (es. di natura probatoria/processuale) con richiami puntuali alle norme, anche quando la norma non riguarda direttamente un obbligo di un QTSP. Questo allarga la Destination del progetto oltre i soli "obblighi applicabili ai QTSP" (vedi map.md).

### Categorie di soggetto

Insieme di valori condiviso da Soggetto obbligato e Destinatario/beneficiario:

- **QTSP/gestore** — il prestatore di servizi fiduciari qualificati
- **Utente/titolare** — il cliente/titolare del servizio (es. titolare di un certificato o di una firma)
- **Terza parte** — soggetto con un rapporto identificabile e tracciabile (es. RA esterna, subappaltatore, auditor, altro provider)
- **Terzi affidanti/pubblico** — relying party indeterminato, senza rapporto diretto né con il QTSP né con l'utente (es. chiunque verifichi una firma digitale facendo affidamento su un certificato qualificato)

### Censimento

L'artefatto complessivo: un **knowledge graph** di due tipi di nodo, Obbligo e Principio, non una tabella piatta. I nodi sono collegati da relazioni tipizzate ed esplicitamente navigabili (non solo un campo testuale di link), a prescindere dal tipo di nodo alle due estremità. Questa è una decisione architetturale deliberata — vedi ADR-0001 (grafo vs. tabella piatta) e ADR-0004 (secondo tipo di nodo, grafo eterogeneo).

### Relazioni tipizzate tra nodi (Obbligo o Principio)

- **Sostituisce / è sostituito da** — relazione temporale tra versioni normative (es. un obbligo eIDAS2 che sostituisce il corrispondente in eIDAS)
- **Specifica / è specificato da** — un nodo generale reso operativo da un nodo più specifico (es. un Principio generale specificato da un Obbligo tecnico, o un Obbligo generale specificato da uno più tecnico)
- **Si sovrappone a / duplica** — stesso contenuto sostanziale espresso in fonti diverse, senza gerarchia tra loro (es. eIDAS e CAD che dicono la stessa cosa)
- **Richiede come precondizione** — un nodo non può dirsi soddisfatto se un altro nodo collegato non è già rispettato
- **È condizionato da / condiziona** — un nodo la cui applicabilità dipende da un altro nodo tracciato nel censimento (distinta dalla Condizione di applicabilità in testo libero, che dipende da un fatto esterno non tracciato)

## Perimetro del pilota

Fonti: **eIDAS** (incluso eIDAS2 dove applicabile) e **CAD**. Altre fonti (AgID, ETSI, ISO, GDPR) restano fuori dal pilota, da estendere in iterazioni successive.

Contenuto: obblighi applicabili ai QTSP **e** principi/effetti giuridici dichiarativi di eIDAS/CAD in generale (non solo quelli relativi a strumenti gestiti dai QTSP) — vedi entità Principio sopra e map.md per la cronologia della decisione.
