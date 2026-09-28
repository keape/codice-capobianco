"""Regolamento di esecuzione (UE) 2025/2531 della Commissione, del 16 dicembre
2025 - norme di riferimento e specifiche applicabili ai registri elettronici
qualificati (articolo 45 terdecies, paragrafo 3, del regolamento (UE)
n. 910/2014, come modificato dal regolamento (UE) 2024/1183). Fonte
`reg_ue_2025_2531`, capitolo unico (articoli 1-2 + allegato). Testo ufficiale
italiano in app/.source_cache/reg_ue_2025_2531/cap01.txt (provenienza CELLAR
in provenance.json; il preambolo e' fuori dalla porzione assegnata).

Modellazione (ADR-0007, nessun discrimine di rilevanza):
- Paratesto amministrativo (epigrafe "Fatto a Bruxelles", firma della
  presidente, note a pie' di pagina alle citazioni degli atti, intestazione
  "ALLEGATO" e suo titolo, riga ELI/ISSN) -> nessun nodo: non sono articoli,
  commi o punti dell'allegato. Le note a pie' di pagina dell'allegato
  ((1) ISO/IEC 15408, (2)-(3) regolamenti EUCC, (4) FIPS PUB 140-3) non
  producono nodi propri perche' il loro contenuto bibliografico e' gia'
  riportato integralmente nel nodo "allegato, punto 3(a), 2.1 riferimenti
  normativi".
- Art. 1 (designa l'allegato come sede delle norme di riferimento e delle
  specifiche di cui all'art. 45 terdecies §3 eIDAS2) -> Principio tipo
  "altro": disposizione di mero rinvio, non definitoria ne' di
  scopo/ambito (stesso trattamento dell'art. 1 del Reg. 2025/1566 e del
  Reg. 2025/1567).
- Art. 2 -> un solo nodo Principio "altro" ("entrata in vigore", il ventesimo
  giorno successivo alla pubblicazione in GUUE): il testo non contiene una
  disposizione di applicazione differita separata. La formula di chiusura
  "obbligatorio in tutti i suoi elementi e direttamente applicabile in
  ciascuno degli Stati membri" non produce un nodo, come in tutte le Fonti
  gia' censite: e' la formula standard di ogni regolamento UE
  self-executing, senza contenuto normativo distinto dalla forma giuridica
  "regolamento" gia' presupposta dal censimento, non un comma autonomo.
- Allegato, punto 1 (15 definizioni, lettere a)-o)) -> UNA sola riga
  Principio "definitorio": un elenco definitorio non ha autonomia
  prescrittiva voce per voce (stesso criterio dell'art. 3 eIDAS e dell'art. 2
  del Reg. 2025/1569). Le 15 lettere sono indicizzate separatamente
  ("allegato, punto 1(a)" ... "allegato, punto 1(o)") e mappate tutte a
  questa riga.
- Allegato, punto 2 (relazione sul registro prodotta in modo automatizzato)
  -> Obbligo con condizione_applicabilita (il precetto vale solo qualora il
  prestatore debba elaborare una relazione sul registro). tipo_obbligo
  "tecnico/sicurezza": il precetto vincola il modo di produzione
  dell'artefatto (generazione automatica, senza intervento manuale), non un
  obbligo di informare terzi (che sarebbe "informativo/trasparenza").
- Allegato, punto 3, chapeau (creare, aggiornare e mantenere il registro
  elettronico qualificato e registrarvi dati elettronici conformemente alle
  specifiche stabilite nelle lettere a) e b)) -> Obbligo "organizzativo", un
  nodo a se': e' la prescrizione generale, mentre a) e b) designano le norme
  di riferimento a cui essa rinvia.
- Allegato, punto 3(a) e punto 3(b) -> Principio "altro" ciascuno:
  designazione di norme di riferimento (ETSI EN 319 401 v3.1.1 (2024-06) con
  adattamenti per a); ISO 23257:2022 e ISO/TS 23635:2022 per i fornitori che
  utilizzano tecnologie di registro elettronico distribuito per b)), senza
  comportamento imposto proprio (stesso trattamento della designazione di
  norma di riferimento nel chapeau dell'allegato del Reg. 2025/1567).
- Punto 3(b)(1) e 3(b)(2) -> due Principi "altro" distinti: ciascuna delle
  due norme ISO richiamate ha contenuto proprio e diverso (architettura di
  riferimento vs linee guida sulla governance), con la
  condizione_applicabilita ereditata dal chapeau di 3(b).
- Punto 3(a), "2.1 riferimenti normativi" (adattamento alla clausola 2.1 di
  ETSI EN 319 401 con sei aggiunte bibliografiche [1]-[6]) -> Principio
  "altro": aggiunta di riferimenti, nessun comportamento imposto.
- Punto 3(a): ogni adattamento con id proprio REQ-... -> UN nodo Obbligo per
  id (16 in totale), soggetto obbligato "QTSP/gestore" (il fornitore di
  registri elettronici qualificati e' per definizione, punto 1 lett. n), un
  prestatore di servizi fiduciari qualificato). Le lettere interne a un
  requisito (REQ-7.5-03 a)/b)/c), REQ-7.5-04 a)/b), REQ-7.5-05 a)-d),
  REQ-7.5-06 a)-c)) e le sotto-voci elencate con trattino (le sei
  informazioni di REQ-6.1-12, le tre frasi dell'adattamento 5.1.8 dentro
  REQ-7.5-03, le scadenze di REQ-6.3-04X) NON sono nodi separati: sono
  contenuto specificativo del requisito che le introduce e restano
  integralmente nel suo testo_integrale. Le sole lettere interne indicizzate
  come item distinti (per istruzione del task) sono quelle dei requisiti
  della clausola 7.5, mappate al nodo del requisito.
- tipo_obbligo allineato al nodo corrispondente della Fonte ETSI EN 319 401
  dove l'id esiste gia' (REQ-6.2-03 "informativo/trasparenza"; REQ-6.3-04,
  REQ-7.2-04, REQ-7.2-05, REQ-7.12-02 "organizzativo"; REQ-7.5-0x,
  REQ-7.8-1x, REQ-7.8-2x, REQ-7.9.1-02 "tecnico/sicurezza"), per non
  introdurre un'incoerenza di classificazione tra l'originale e il suo
  adattamento. Id nuovi introdotti da questo atto: REQ-6.1-12
  "informativo/trasparenza" (dichiarazione sulla pratica del registro, stessa
  famiglia di REQ-6.1-04); REQ-7.5-06 "tecnico/sicurezza" (dispositivo
  crittografico sicuro per le chiavi di firma).
- Destinatari (ruolo "destinatario") valorizzati solo dove il testo li nomina:
  REQ-6.2-03 informa "gli abbonati" (Utente/titolare) e "le parti facenti
  affidamento" (Terzi affidanti/pubblico). L'organismo di vigilanza,
  destinatario della notifica di REQ-6.3-04X, non e' modellato come
  destinatario/beneficiario: e' il termine di un adempimento informativo
  verso un'autorita' di vigilanza, non un soggetto a favore del quale
  l'obbligo e' posto.
- testo_integrale: sempre verbatim e integrale, ottenuto unendo le righe
  spezzate dalla conversione (le righe "—" isolate diventano il separatore
  inline " — "), con l'intestazione di clausola dove il testo ufficiale la
  premette immediatamente al requisito. Per i requisiti successivi al primo
  della stessa clausola (7.2-05X, 7.5-02 ... 7.5-06, 7.8-18X, 7.8-21X)
  l'intestazione non e' ripetuta: nel testo ufficiale non li precede, e
  ripeterla renderebbe il testo_integrale non contiguo alla fonte. La riga
  "In particolare:" che segue REQ-7.5-02 e' assorbita in quel requisito
  (introduce la lista dei requisiti crittografici che seguono). Nessuna riga
  valorizza severita' o sanzioni: l'atto non gradua i requisiti ne' prevede
  sanzioni proprie.
- RELAZIONI = [] per istruzione del batch: i collegamenti verso eIDAS/eIDAS2
  (art. 45 terdecies §3), verso ETSI EN 319 401 e verso ETSI TS 119 182-1 li
  costruisce la sessione principale, non questo modulo.

Copertura: 53 item di indice, 26 righe (18 Obblighi + 8 Principi).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "allegato, punto 2",
        "testo": "Qualora il prestatore di servizi fiduciari qualificato debba elaborare una relazione sul registro (presentazione strutturata di informazioni verificabili estratte dalle registrazioni di dati di un registro elettronico), tale relazione è prodotta in modo automatizzato.",
        "testo_integrale": "Qualora il prestatore di servizi fiduciari qualificato debba elaborare una relazione sul registro, questa è prodotta in modo automatizzato.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo qualora il prestatore di servizi fiduciari qualificato debba elaborare una relazione sul registro.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3",
        "testo": "I fornitori di registri elettronici qualificati creano, aggiornano e mantengono un registro elettronico qualificato e vi registrano dati elettronici conformemente alle specifiche stabilite in: a) per tutti i fornitori, ETSI EN 319 401 v3.1.1 (2024-06) con gli adattamenti del punto 3(a); b) per tutti i fornitori che utilizzano tecnologie di registro elettronico distribuito, anche nelle norme ISO 23257:2022 (punto 9) e ISO/TS 23635:2022 di cui al punto 3(b).",
        "testo_integrale": "I fornitori di registri elettronici qualificati creano, aggiornano e mantengono un registro elettronico qualificato e vi registrano dati elettronici conformemente alle specifiche stabilite in:",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 6.1 REQ-6.1-12",
        "testo": "La dichiarazione sulla pratica del registro elettronico comprende almeno: le capacità funzionali e tecniche della piattaforma del registro elettronico e il suo utilizzo durante l'intera prestazione del servizio; i meccanismi specifici di autenticazione dell'origine dei dati; i meccanismi specifici di ordinamento cronologico sequenziale dei dati; se del caso, il collegamento crittografico utilizzato per garantire la sequenza delle registrazioni di dati; se del caso, il meccanismo di consenso che garantisce il carattere definitivo e l'integrità delle registrazioni di dati e delle transazioni conservate nel registro, compreso qualsiasi margine temporale supplementare fino al raggiungimento del carattere definitivo e dell'integrità; i meccanismi specifici di integrità dei dati utilizzati per prestare il servizio.",
        "testo_integrale": "6.1 dichiarazione sulla pratica del servizio fiduciario: — REQ-6.1-12 La dichiarazione sulla pratica del registro elettronico comprende almeno le seguenti informazioni: — le capacità funzionali e tecniche della piattaforma del registro elettronico e il suo utilizzo durante l'intera prestazione della registrazione di dati in un registro elettronico qualificato come servizio fiduciario qualificato; — i meccanismi specifici di autenticazione dell'origine dei dati utilizzati durante la prestazione del servizio; — i meccanismi specifici di ordinamento cronologico sequenziale dei dati utilizzati durante la prestazione del servizio; — se del caso, il collegamento crittografico utilizzato per garantire la sequenza delle registrazioni di dati; — se del caso, il meccanismo di consenso che garantisce il carattere definitivo e l'integrità delle registrazioni di dati e delle transazioni conservate nel registro, compreso qualsiasi margine temporale supplementare fino al raggiungimento del carattere definitivo e dell'integrità; — i meccanismi specifici di integrità dei dati utilizzati per prestare il servizio;",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 6.2 REQ-6.2-03",
        "testo": "Prima di avviare una relazione contrattuale, gli abbonati e le parti facenti affidamento sul servizio fiduciario sono informati in modo chiaro, completo e facilmente accessibile, in uno spazio accessibile al pubblico e individualmente, di termini e condizioni precisi, compresi gli elementi elencati da REQ-6.1-12.",
        "testo_integrale": "6.2 termini e condizioni: — REQ-6.2-03 Prima di avviare una relazione contrattuale gli abbonati e le parti facenti affidamento sul servizio fiduciario sono informati in modo chiaro, completo e facilmente accessibile, in uno spazio accessibile al pubblico e individualmente, di termini e condizioni precisi, compresi gli elementi sopraelencati;",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato, punto 3(a), 6.3 REQ-6.3-04X",
        "testo": "Il prestatore di servizi fiduciari stabilisce procedure per notificare all'organismo di vigilanza eventuali modifiche nella prestazione del servizio fiduciario, conformemente ai requisiti commerciali e alle disposizioni legislative e regolamentari pertinenti; la notifica all'organismo di vigilanza è effettuata almeno un mese prima dell'attuazione di qualsiasi modifica e almeno tre mesi prima della cessazione prevista di una prestazione di servizi fiduciari.",
        "testo_integrale": "6.3 politica di sicurezza delle informazioni: — REQ-6.3-04X Il prestatore di servizi fiduciari stabilisce procedure per notificare all'organismo di vigilanza eventuali modifiche nella prestazione del servizio fiduciario, conformemente ai requisiti commerciali e alle disposizioni legislative e regolamentari pertinenti. Il prestatore di servizi fiduciari effettua la notifica all'organismo di vigilanza almeno: — un mese prima dell'attuazione di qualsiasi modifica; — tre mesi prima della cessazione prevista di una prestazione di servizi fiduciari;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 7.2 REQ-7.2-04X",
        "testo": "Il personale del prestatore di servizi fiduciari in ruoli di fiducia è in grado di soddisfare il requisito in materia di «competenze, esperienza e qualifiche» mediante formazione e credenziali formali, o effettiva esperienza, o una combinazione di entrambe.",
        "testo_integrale": "7.2 risorse umane: — REQ-7.2-04X Il personale del prestatore di servizi fiduciari in ruoli di fiducia è in grado di soddisfare il requisito in materia di «competenze, esperienza e qualifiche» mediante formazione e credenziali formali, o effettiva esperienza, o una combinazione di entrambe.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 7.2 REQ-7.2-05X",
        "testo": "Gli aggiornamenti periodici del personale in ruoli di fiducia comprendono aggiornamenti (almeno ogni 12 mesi) sulle nuove minacce e sulle attuali pratiche di sicurezza.",
        "testo_integrale": "REQ-7.2-05X Sono compresi aggiornamenti periodici (almeno ogni 12 mesi) sulle nuove minacce e sulle attuali pratiche di sicurezza;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 7.5 REQ-7.5-01X",
        "testo": "Sono predisposti adeguati controlli di sicurezza per la gestione di qualsiasi chiave crittografica, algoritmo crittografico e dispositivo crittografico durante tutto il loro ciclo di vita, seguendo, se del caso, un approccio di agilità crittografica.",
        "testo_integrale": "7.5 controlli crittografici: — REQ-7.5-01X Sono predisposti adeguati controlli di sicurezza per la gestione di qualsiasi chiave crittografica, algoritmo crittografico e dispositivo crittografico durante tutto il loro ciclo di vita, seguendo, se del caso, un approccio di agilità crittografica.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 7.5 REQ-7.5-02",
        "testo": "Per prestare i suoi servizi fiduciari, il prestatore di servizi fiduciari seleziona e utilizza tecniche crittografiche adeguate conformi ai meccanismi crittografici concordati approvati dal gruppo europeo per la certificazione della cibersicurezza e pubblicati dall'ENISA [1]; in particolare si applicano i requisiti adattati REQ-7.5-03 (origine delle registrazioni di dati), REQ-7.5-04 (ordine cronologico sequenziale univoco), REQ-7.5-05 (integrità delle registrazioni di dati) e REQ-7.5-06 (dispositivo crittografico sicuro per le chiavi di firma private).",
        "testo_integrale": "REQ-7.5-02 Per prestare i suoi servizi fiduciari, il prestatore di servizi fiduciari seleziona e utilizza tecniche crittografiche adeguate conformi ai meccanismi crittografici concordati approvati dal gruppo europeo per la certificazione della cibersicurezza e pubblicati dall'ENISA [1].\n\nIn particolare:",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 7.5 REQ-7.5-03",
        "testo": "I fornitori di registri elettronici qualificati stabiliscono l'origine delle registrazioni di dati nel registro elettronico utilizzando firme elettroniche avanzate basate su certificati qualificati o sigilli elettronici avanzati basati su certificati qualificati creati dagli utenti del servizio, conformemente a: a) ETSI EN 319 122-1 V1.3.1 (2023-06) (CAdES); b) ETSI EN 319 132-1 V1.3.1 (2024-07) (XAdES); c) ETSI TS 119 182-1 V1.2.1 (2024-07) (JAdES), con il seguente adattamento alla clausola 5.1.8: il parametro di intestazione x5c definito al punto 4.1.6 dell'IETF RFC 7515 [2] deve essere presente nella firma JAdES come parametro di intestazione firmato o non firmato, con la semantica e la sintassi specificate al punto 4.1.6 dell'IETF RFC 7515 [2].",
        "testo_integrale": "REQ-7.5-03 I fornitori di registri elettronici qualificati stabiliscono l'origine delle registrazioni di dati nel registro elettronico. A tal fine utilizzano firme elettroniche avanzate basate su certificati qualificati o sigilli elettronici avanzati basati su certificati qualificati creati dagli utenti del servizio conformemente alle norme e specifiche seguenti:\n\na) ETSI EN 319 122-1 V1.3.1 (2023-06). «Electronic Signatures and Infrastructures (ESI); CAdES digital signatures; Part 1: Building blocks and CAdES baseline signatures».\n\nb) ETSI EN 319 132-1 V1.3.1 (2024-07). «Electronic Signatures and Trust Infrastructures (ESI); XAdES digital signatures; Part 1: Building blocks and XAdES baseline signatures».\n\nc) ETSI TS 119 182-1 V1.2.1 (2024-07). «Electronic Signatures and Trust Infrastructures (ESI); JAdES digital signatures; Part 1: Building blocks and JAdES baseline signatures», con il seguente adattamento: — 5.1.8 parametro di intestazione x5c (catena di certificati X.509) — Il parametro di intestazione x5c definito al punto 4.1.6 dell'IETF RFC 7515 [2] deve essere presente nella firma JAdES come parametro di intestazione firmato o non firmato. — Il parametro di intestazione x5c deve avere la semantica specificata al punto 4.1.6 dell'IETF RFC 7515 [2]. — Il parametro di intestazione x5c deve avere la sintassi specificata al punto 4.1.6 dell'IETF RFC 7515 [2].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 7.5 REQ-7.5-04",
        "testo": "I fornitori di registri elettronici qualificati garantiscono l'ordine cronologico sequenziale univoco delle registrazioni di dati nel registro elettronico utilizzando collegamenti crittografici basati su elenchi di hash o alberi di hash, con funzioni crittografiche di hash conformi ai meccanismi crittografici concordati approvati dal gruppo europeo per la certificazione della cibersicurezza e pubblicati dall'ENISA [1] e con dimensione dell'output di SHA-256 o superiore (a) o di SHA3-256 o superiore (b). In alternativa, quando utilizzano la registrazione temporale per garantire tale ordine, utilizzano marcature temporali qualificate.",
        "testo_integrale": "REQ-7.5-04 I fornitori di registri elettronici qualificati garantiscono l'ordine cronologico sequenziale univoco delle registrazioni di dati nel registro elettronico. A tal fine utilizzano collegamenti crittografici, basati su elenchi di hash o alberi di hash, utilizzando funzioni crittografiche di hash, conformemente alle specifiche e alle norme seguenti:\n\na) dimensione dell'output di SHA-256 o superiore, conformemente ai meccanismi crittografici concordati approvati dal gruppo europeo per la certificazione della cibersicurezza e pubblicati dall'ENISA [1].\n\nb) dimensione dell'output di SHA3-256 o superiore, conformemente ai meccanismi crittografici concordati approvati dal gruppo europeo per la certificazione della cibersicurezza e pubblicati dall'ENISA [1].\n\nIn alternativa, quando utilizzano la registrazione temporale per garantire l'ordine cronologico sequenziale univoco delle registrazioni di dati nel registro elettronico, i fornitori di registri elettronici qualificati utilizzano marcature temporali qualificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 7.5 REQ-7.5-05",
        "testo": "I fornitori di registri elettronici qualificati garantiscono l'integrità delle registrazioni di dati nel registro elettronico qualificato utilizzando firme elettroniche avanzate basate su certificati qualificati o sigilli elettronici avanzati basati su certificati qualificati conformi ai meccanismi crittografici concordati approvati dal gruppo europeo per la certificazione della cibersicurezza e pubblicati dall'ENISA [1]: qualsiasi formato di firma o sigillo (a); dimensione dell'output di SHA-256 o superiore (b); dimensione dell'output di SHA3-256 o superiore (c). Garantiscono inoltre l'identificazione immediata di ogni successiva modifica dei dati registrati in un registro elettronico qualificato (d).",
        "testo_integrale": "REQ-7.5-05 I fornitori di registri elettronici qualificati garantiscono l'integrità delle registrazioni di dati nel registro elettronico qualificato. A tal fine utilizzano firme elettroniche avanzate basate su certificati qualificati o sigilli elettronici avanzati basati su certificati qualificati, conformemente alle norme e specifiche seguenti:\n\na) qualsiasi formato di firma o sigillo conforme ai meccanismi crittografici concordati approvati dal gruppo europeo per la certificazione della cibersicurezza e pubblicati dall'ENISA [1];\n\nb) dimensione dell'output di SHA-256 o superiore, conformemente ai meccanismi crittografici concordati approvati dal gruppo europeo per la certificazione della cibersicurezza e pubblicati dall'ENISA [1];\n\nc) dimensione dell'output di SHA3-256 o superiore, conformemente ai meccanismi crittografici concordati approvati dal gruppo europeo per la certificazione della cibersicurezza e pubblicati dall'ENISA [1].\n\nd) I fornitori di registri elettronici qualificati garantiscono l'identificazione immediata di ogni successiva modifica dei dati registrati in un registro elettronico qualificato.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 7.5 REQ-7.5-06",
        "testo": "Qualora siano utilizzati meccanismi di firma digitale, le chiavi di firma private del fornitore di registri elettronici qualificati sono detenute e utilizzate all'interno di un dispositivo crittografico sicuro che è un sistema affidabile certificato conformemente a: a) criteri comuni per la valutazione della sicurezza delle tecnologie informatiche (ISO/IEC 15408 o Common Criteria CC:2022, parti da 1 a 5) a livello EAL 4 o superiore; oppure b) sistema europeo di certificazione della cibersicurezza basato sui criteri comuni (EUCC) a livello EAL 4 o superiore; oppure c) fino al 31.12.2030, FIPS PUB 140-3 livello 3. Tale certificazione riguarda un obiettivo di sicurezza o un profilo di protezione, o la progettazione di un modulo e la documentazione di sicurezza, che soddisfano i requisiti del documento sulla base di un'analisi dei rischi e tenendo conto delle misure di sicurezza fisiche e di altre misure di sicurezza non tecniche. Se il dispositivo beneficia di una certificazione EUCC, è configurato e utilizzato conformemente a tale certificazione.",
        "testo_integrale": "REQ-7.5-06 Qualora siano utilizzati meccanismi di firma digitale, le chiavi di firma private del fornitore di registri elettronici qualificati sono detenute e utilizzate all'interno di un dispositivo crittografico sicuro che è un sistema affidabile certificato conformemente a quanto segue:\n\na) criteri comuni per la valutazione della sicurezza delle tecnologie informatiche, quali definiti nella norma ISO/IEC 15408 (1) [6] o in «Common Criteria for Information Technology Security Evaluation», versione CC:2022, parti da 1 a 5, pubblicato dai partecipanti all'accordo «Arrangement on the Recognition of Common Criteria Certificates in the field of IT Security», e certificati a livello EAL 4 o superiore; oppure\n\nb) sistema europeo di certificazione della cibersicurezza basato sui criteri comuni (EUCC) (2) (3) [4][5], e certificato a livello EAL 4 o superiore; oppure\n\nc) fino al 31.12.2030, FIPS PUB 140-3 (4) [3] livello 3;\n\nTale certificazione riguarda un obiettivo di sicurezza o un profilo di protezione, o la progettazione di un modulo e la documentazione di sicurezza, che soddisfano i requisiti del presente documento, sulla base di un'analisi dei rischi e tenendo conto delle misure di sicurezza fisiche e di altre misure di sicurezza non tecniche.\n\nSe il dispositivo crittografico sicuro beneficia di una certificazione EUCC [4][5], tale dispositivo è configurato e utilizzato conformemente a tale certificazione.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 7.8 REQ-7.8-14X",
        "testo": "La scansione delle vulnerabilità richiesta dal requisito REQ-7.8-13 è eseguita almeno una volta a trimestre.",
        "testo_integrale": "7.8 sicurezza della rete: — REQ-7.8-14X La scansione delle vulnerabilità richiesta dal requisito REQ-7.8-13 è eseguita almeno una volta a trimestre.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 7.8 REQ-7.8-18X",
        "testo": "Il test di penetrazione richiesto dal requisito REQ-7.8-17X è eseguito almeno una volta all'anno.",
        "testo_integrale": "REQ-7.8-18X Il test di penetrazione richiesto dal requisito REQ-7.8-17X è eseguito almeno una volta all'anno.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 7.8 REQ-7.8-21X",
        "testo": "Anche i firewall devono essere configurati in modo da bloccare tutti i protocolli e gli accessi non necessari per il funzionamento del prestatore di servizi fiduciari.",
        "testo_integrale": "REQ-7.8-21X Anche i firewall devono essere configurati in modo da bloccare tutti i protocolli e gli accessi non necessari per il funzionamento del prestatore di servizi fiduciari;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 7.9.1 REQ-7.9.1-02X",
        "testo": "Le attività di monitoraggio tengono conto della sensibilità delle informazioni raccolte o analizzate.",
        "testo_integrale": "7.9.1 monitoraggio e tenuta di registro: — REQ-7.9.1-02X Le attività di monitoraggio tengono conto della sensibilità delle informazioni raccolte o analizzate;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, punto 3(a), 7.12 REQ-7.12-02 A",
        "testo": "Il piano di cessazione del prestatore di servizi fiduciari è conforme ai requisiti stabiliti negli atti di esecuzione adottati a norma dell'articolo 24, paragrafo 5, del regolamento (UE) n. 910/2014 [i.1].",
        "testo_integrale": "7.12 cessazione e piani di cessazione del prestatore di servizi fiduciari: — REQ-7.12-02 A Il piano di cessazione del prestatore di servizi fiduciari è conforme ai requisiti stabiliti negli atti di esecuzione adottati a norma dell'articolo 24, paragrafo 5, del regolamento (UE) n. 910/2014 [i.1].",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 1",
        "testo": "Le norme di riferimento e le specifiche di cui all'articolo 45 terdecies, paragrafo 3, del regolamento (UE) n. 910/2014 figurano, per i registri elettronici qualificati, nell'allegato del presente regolamento (che elenca le specifiche tecniche e le norme di riferimento applicabili ai registri elettronici distribuiti qualificati).",
        "testo_integrale": "Le norme di riferimento e le specifiche di cui all'articolo 45 terdecies, paragrafo 3, del regolamento (UE) n. 910/2014 figurano, per i registri elettronici qualificati, nell'allegato del presente regolamento.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2, entrata in vigore",
        "testo": "Il regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea (nessuna disposizione di applicazione differita).",
        "testo_integrale": "Il presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato, punto 1",
        "testo": "Ai fini del regolamento si applicano 15 definizioni: carattere definitivo; registro elettronico distribuito; nodo di registro elettronico distribuito; rete di registro elettronico distribuito; sistema di registro elettronico distribuito; consenso; meccanismo di consenso; norme di disciplina; transazione; processo di lavoro; transazione convalidata; collegamento crittografico; relazione sul registro (presentazione strutturata di informazioni verificabili estratte dalle registrazioni di dati di un registro elettronico); fornitore di registri elettronici qualificati (prestatore di servizi fiduciari qualificato che presta il servizio fiduciario qualificato consistente nella registrazione di dati in un registro elettronico qualificato); registro elettronico distribuito qualificato.",
        "testo_integrale": "Ai fini del presente regolamento si applicano le definizioni seguenti:\n\na) «carattere definitivo»: lo stato di una registrazione di dati di un registro elettronico in cui è diventata irreversibile e non può essere modificata o rimossa;\n\nb) «registro elettronico distribuito»: un registro elettronico condiviso tra una serie di nodi di registro elettronico distribuito e sincronizzato tra i nodi di registro elettronico distribuito utilizzando un meccanismo di consenso;\n\nc) «nodo di registro elettronico distribuito»: un dispositivo o un processo che fa parte di una rete di registro elettronico distribuito e conserva una copia completa o parziale delle registrazioni di dati di un registro elettronico;\n\nd) «rete di registro elettronico distribuito»: una rete di nodi di registro elettronico distribuito che costituisce un sistema di registro elettronico distribuito;\n\ne) «sistema di registro elettronico distribuito»: un sistema che implementa un registro elettronico distribuito;\n\nf) «consenso»: un accordo tra nodi di registro elettronico distribuito sulla validità delle transazioni e sul mantenimento di un insieme coerente e ordinato di transazioni convalidate in tutto il sistema di registro elettronico distribuito;\n\ng) «meccanismo di consenso»: l'insieme di norme e procedure mediante le quali è raggiunto il consenso;\n\nh) «norme di disciplina»: l'insieme di protocolli, politiche e meccanismi che stabilisce le modalità di funzionamento del sistema di registro elettronico distribuito, di convalida dei dati e di aggiunta degli stessi a un registro elettronico nonché di interazione dei partecipanti;\n\ni) «transazione»: l'unità più piccola di un processo di lavoro all'interno di un registro elettronico;\n\nj) «processo di lavoro»: una o più sequenze di azioni necessarie per produrre un risultato conforme alle norme di disciplina di un registro elettronico;\n\nk) «transazione convalidata»: una transazione per cui l'integrità, l'autenticità e le condizioni specifiche per il protocollo richieste sono state verificate secondo le norme di disciplina del sistema di registro elettronico distribuito;\n\nl) «collegamento crittografico»: un riferimento a dati stabilito utilizzando tecniche crittografiche idonee a garantire l'integrità, l'autenticità o la tracciabilità dei dati referenziati e la corretta sequenza delle registrazioni di dati;\n\nm) «relazione sul registro»: una presentazione strutturata di informazioni verificabili estratte dalle registrazioni di dati di un registro elettronico, che fornisce anche indicazioni su specifiche attività, stati o conformità a norme predefinite;\n\nn) «fornitore di registri elettronici qualificati»: un prestatore di servizi fiduciari qualificato che presta un servizio fiduciario qualificato consistente nella registrazione di dati in un registro elettronico qualificato;\n\no) «registro elettronico distribuito qualificato»: un registro elettronico distribuito che soddisfa i requisiti di un registro elettronico qualificato.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato, punto 3(a)",
        "testo": "Per tutti i fornitori di registri elettronici qualificati la norma di riferimento è ETSI EN 319 401 v3.1.1 (2024-06), con i seguenti adattamenti: la clausola 2.1 (riferimenti normativi) e i requisiti REQ-6.1-12, REQ-6.2-03, REQ-6.3-04X, REQ-7.2-04X, REQ-7.2-05X, REQ-7.5-01X, REQ-7.5-02, REQ-7.5-03, REQ-7.5-04, REQ-7.5-05, REQ-7.5-06, REQ-7.8-14X, REQ-7.8-18X, REQ-7.8-21X, REQ-7.9.1-02X e REQ-7.12-02 A.",
        "testo_integrale": "per tutti i fornitori di registri elettronici qualificati, ETSI EN 319 401 v3.1.1 (2024-06) con i seguenti adattamenti:",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato, punto 3(a), 2.1 riferimenti normativi",
        "testo": "Alla clausola 2.1 (riferimenti normativi) di ETSI EN 319 401 sono aggiunti i riferimenti: [1] meccanismi crittografici concordati del gruppo europeo per la certificazione della cibersicurezza (ENISA); [2] IETF RFC 7515 (maggio 2015) JSON Web Signature; [3] FIPS PUB 140-3 (2019); [4] regolamento di esecuzione (UE) 2024/482 (EUCC); [5] regolamento di esecuzione (UE) 2024/3144, che modifica il precedente; [6] ISO/IEC 15408:2022 (parti da 1 a 5).",
        "testo_integrale": "2.1 riferimenti normativi\n\n[1] gruppo europeo per la certificazione della cibersicurezza, sottogruppo sulla crittografia: «Agreed Cryptographic Mechanisms» (meccanismi crittografici concordati), pubblicati dall'Agenzia europea per la sicurezza delle reti e dell'informazione (ENISA).\n\n[2] IETF RFC 7515 (maggio 2015): «JSON Web Signature (JWS)».\n\n[3] FIPS PUB 140-3 (2019) «Security Requirements for Cryptographic Modules».\n\n[4] Regolamento di esecuzione (UE) 2024/482 della Commissione, del 31 gennaio 2024, recante modalità di applicazione del regolamento (UE) 2019/881 del Parlamento europeo e del Consiglio per quanto riguarda l'adozione del sistema europeo di certificazione della cibersicurezza basato sui criteri comuni (EUCC).\n\n[5] Regolamento di esecuzione (UE) 2024/3144 della Commissione, del 18 dicembre 2024, che modifica il regolamento di esecuzione (UE) 2024/482 per quanto riguarda le norme internazionali applicabili e che rettifica tale regolamento di esecuzione.\n\n[6] ISO/IEC 15408:2022 (parti da 1 a 5): «Information security, cybersecurity and privacy protection – Evaluation criteria for IT security»;",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato, punto 3(b)",
        "testo": "Inoltre, per tutti i fornitori di registri elettronici qualificati che utilizzano tecnologie di registro elettronico distribuito, le norme di riferimento sono: ISO 23257:2022, punto 9; ISO/TS 23635:2022, per quanto riguarda le politiche e le pratiche di governance.",
        "testo_integrale": "Inoltre, per tutti i fornitori di registri elettronici qualificati che utilizzano tecnologie di registro elettronico distribuito:",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo ai fornitori di registri elettronici qualificati che utilizzano tecnologie di registro elettronico distribuito.",
    },
    {
        "riferimento": "allegato, punto 3(b)(1)",
        "testo": "ISO 23257:2022 «Blockchain and distributed ledger technologies – Reference architecture», punto 9, fornisce una descrizione completa del sistema basato sulla tecnologia di registro elettronico distribuito, della corrispondente rete basata su tecnologia di registro elettronico distribuito e dei nodi basati su tecnologia di registro elettronico distribuito.",
        "testo_integrale": "(1) ISO 23257:2022 «Blockchain and distributed ledger technologies – Reference architecture», punto 9, che fornisce una descrizione completa del sistema basato sulla tecnologia di registro elettronico distribuito, della corrispondente rete basata su tecnologia di registro elettronico distribuito e dei nodi basati su tecnologia di registro elettronico distribuito;",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo ai fornitori di registri elettronici qualificati che utilizzano tecnologie di registro elettronico distribuito (condizione del punto 3(b)).",
    },
    {
        "riferimento": "allegato, punto 3(b)(2)",
        "testo": "ISO/TS 23635:2022 «Blockchain and distributed ledger technologies – Guidelines for governance», per quanto riguarda le politiche e le pratiche scritte e accessibili al pubblico relative alla struttura di governance per il servizio di registro elettronico prestato.",
        "testo_integrale": "(2) ISO/TS 23635:2022. «Blockchain and distributed ledger technologies – Guidelines for governance», per quanto riguarda le politiche e le pratiche scritte e accessibili al pubblico relative alla struttura di governance per il servizio di registro elettronico prestato.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo ai fornitori di registri elettronici qualificati che utilizzano tecnologie di registro elettronico distribuito (condizione del punto 3(b)).",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 1",
    "art. 2, entrata in vigore",
    "allegato, punto 1",
    "allegato, punto 1(a)",
    "allegato, punto 1(b)",
    "allegato, punto 1(c)",
    "allegato, punto 1(d)",
    "allegato, punto 1(e)",
    "allegato, punto 1(f)",
    "allegato, punto 1(g)",
    "allegato, punto 1(h)",
    "allegato, punto 1(i)",
    "allegato, punto 1(j)",
    "allegato, punto 1(k)",
    "allegato, punto 1(l)",
    "allegato, punto 1(m)",
    "allegato, punto 1(n)",
    "allegato, punto 1(o)",
    "allegato, punto 2",
    "allegato, punto 3",
    "allegato, punto 3(a)",
    "allegato, punto 3(a), 2.1 riferimenti normativi",
    "allegato, punto 3(a), 6.1 REQ-6.1-12",
    "allegato, punto 3(a), 6.2 REQ-6.2-03",
    "allegato, punto 3(a), 6.3 REQ-6.3-04X",
    "allegato, punto 3(a), 7.2 REQ-7.2-04X",
    "allegato, punto 3(a), 7.2 REQ-7.2-05X",
    "allegato, punto 3(a), 7.5 REQ-7.5-01X",
    "allegato, punto 3(a), 7.5 REQ-7.5-02",
    "allegato, punto 3(a), 7.5 REQ-7.5-03",
    "allegato, punto 3(a), 7.5 REQ-7.5-03 a)",
    "allegato, punto 3(a), 7.5 REQ-7.5-03 b)",
    "allegato, punto 3(a), 7.5 REQ-7.5-03 c)",
    "allegato, punto 3(a), 7.5 REQ-7.5-04",
    "allegato, punto 3(a), 7.5 REQ-7.5-04 a)",
    "allegato, punto 3(a), 7.5 REQ-7.5-04 b)",
    "allegato, punto 3(a), 7.5 REQ-7.5-05",
    "allegato, punto 3(a), 7.5 REQ-7.5-05 a)",
    "allegato, punto 3(a), 7.5 REQ-7.5-05 b)",
    "allegato, punto 3(a), 7.5 REQ-7.5-05 c)",
    "allegato, punto 3(a), 7.5 REQ-7.5-05 d)",
    "allegato, punto 3(a), 7.5 REQ-7.5-06",
    "allegato, punto 3(a), 7.5 REQ-7.5-06 a)",
    "allegato, punto 3(a), 7.5 REQ-7.5-06 b)",
    "allegato, punto 3(a), 7.5 REQ-7.5-06 c)",
    "allegato, punto 3(a), 7.8 REQ-7.8-14X",
    "allegato, punto 3(a), 7.8 REQ-7.8-18X",
    "allegato, punto 3(a), 7.8 REQ-7.8-21X",
    "allegato, punto 3(a), 7.9.1 REQ-7.9.1-02X",
    "allegato, punto 3(a), 7.12 REQ-7.12-02 A",
    "allegato, punto 3(b)",
    "allegato, punto 3(b)(1)",
    "allegato, punto 3(b)(2)",
]

MAPPATURA_LOCALE = {
    "art. 1": ["art. 1"],
    "art. 2, entrata in vigore": ["art. 2, entrata in vigore"],
    "allegato, punto 1": [
        "allegato, punto 1",
        "allegato, punto 1(a)",
        "allegato, punto 1(b)",
        "allegato, punto 1(c)",
        "allegato, punto 1(d)",
        "allegato, punto 1(e)",
        "allegato, punto 1(f)",
        "allegato, punto 1(g)",
        "allegato, punto 1(h)",
        "allegato, punto 1(i)",
        "allegato, punto 1(j)",
        "allegato, punto 1(k)",
        "allegato, punto 1(l)",
        "allegato, punto 1(m)",
        "allegato, punto 1(n)",
        "allegato, punto 1(o)",
    ],
    "allegato, punto 2": ["allegato, punto 2"],
    "allegato, punto 3": ["allegato, punto 3"],
    "allegato, punto 3(a)": ["allegato, punto 3(a)"],
    "allegato, punto 3(a), 2.1 riferimenti normativi": ["allegato, punto 3(a), 2.1 riferimenti normativi"],
    "allegato, punto 3(a), 6.1 REQ-6.1-12": ["allegato, punto 3(a), 6.1 REQ-6.1-12"],
    "allegato, punto 3(a), 6.2 REQ-6.2-03": ["allegato, punto 3(a), 6.2 REQ-6.2-03"],
    "allegato, punto 3(a), 6.3 REQ-6.3-04X": ["allegato, punto 3(a), 6.3 REQ-6.3-04X"],
    "allegato, punto 3(a), 7.2 REQ-7.2-04X": ["allegato, punto 3(a), 7.2 REQ-7.2-04X"],
    "allegato, punto 3(a), 7.2 REQ-7.2-05X": ["allegato, punto 3(a), 7.2 REQ-7.2-05X"],
    "allegato, punto 3(a), 7.5 REQ-7.5-01X": ["allegato, punto 3(a), 7.5 REQ-7.5-01X"],
    "allegato, punto 3(a), 7.5 REQ-7.5-02": ["allegato, punto 3(a), 7.5 REQ-7.5-02"],
    "allegato, punto 3(a), 7.5 REQ-7.5-03": [
        "allegato, punto 3(a), 7.5 REQ-7.5-03",
        "allegato, punto 3(a), 7.5 REQ-7.5-03 a)",
        "allegato, punto 3(a), 7.5 REQ-7.5-03 b)",
        "allegato, punto 3(a), 7.5 REQ-7.5-03 c)",
    ],
    "allegato, punto 3(a), 7.5 REQ-7.5-04": [
        "allegato, punto 3(a), 7.5 REQ-7.5-04",
        "allegato, punto 3(a), 7.5 REQ-7.5-04 a)",
        "allegato, punto 3(a), 7.5 REQ-7.5-04 b)",
    ],
    "allegato, punto 3(a), 7.5 REQ-7.5-05": [
        "allegato, punto 3(a), 7.5 REQ-7.5-05",
        "allegato, punto 3(a), 7.5 REQ-7.5-05 a)",
        "allegato, punto 3(a), 7.5 REQ-7.5-05 b)",
        "allegato, punto 3(a), 7.5 REQ-7.5-05 c)",
        "allegato, punto 3(a), 7.5 REQ-7.5-05 d)",
    ],
    "allegato, punto 3(a), 7.5 REQ-7.5-06": [
        "allegato, punto 3(a), 7.5 REQ-7.5-06",
        "allegato, punto 3(a), 7.5 REQ-7.5-06 a)",
        "allegato, punto 3(a), 7.5 REQ-7.5-06 b)",
        "allegato, punto 3(a), 7.5 REQ-7.5-06 c)",
    ],
    "allegato, punto 3(a), 7.8 REQ-7.8-14X": ["allegato, punto 3(a), 7.8 REQ-7.8-14X"],
    "allegato, punto 3(a), 7.8 REQ-7.8-18X": ["allegato, punto 3(a), 7.8 REQ-7.8-18X"],
    "allegato, punto 3(a), 7.8 REQ-7.8-21X": ["allegato, punto 3(a), 7.8 REQ-7.8-21X"],
    "allegato, punto 3(a), 7.9.1 REQ-7.9.1-02X": ["allegato, punto 3(a), 7.9.1 REQ-7.9.1-02X"],
    "allegato, punto 3(a), 7.12 REQ-7.12-02 A": ["allegato, punto 3(a), 7.12 REQ-7.12-02 A"],
    "allegato, punto 3(b)": ["allegato, punto 3(b)"],
    "allegato, punto 3(b)(1)": ["allegato, punto 3(b)(1)"],
    "allegato, punto 3(b)(2)": ["allegato, punto 3(b)(2)"],
}

# Relazioni native (citazioni e adeguamenti letterali, non il prodotto della
# pipeline di Fase 6). Le relazioni verso ETSI EN 319 401 (Fonte 10) sono
# "modifica" e non "specifica": l'atto si presenta come elenco di
# *adattamenti* della norma censita, quindi il nodo integra il requisito della
# norma senza sostituirlo. Due avvertenze sulla mappatura id->id, entrambe
# dovute al fatto che l'atto adegua la V3.1.1 (2024-06) mentre la Fonte 10
# censisce la V3.2.1 (2026-01), fra cui la numerazione della clausola 7.8 e'
# cambiata (qui si aggancia per contenuto, non per numero):
# - REQ-7.8-18X (test di penetrazione almeno annuale) -> REQ-7.8-18, che nella
#   versione censita e' il requisito sul test di penetrazione (l'atto lo cita
#   come "REQ-7.8-17X", numerazione della versione che adegua);
# - REQ-7.8-21X (firewall) -> REQ-7.8-22, che nella versione censita contiene
#   la prescrizione sui protocolli non necessari.
# REQ-6.1-12 non ha controparte: la clausola 6.1 della Fonte 10 si ferma a
# REQ-6.1-11, quindi e' un requisito nuovo e non un adattamento - nessuna
# relazione, per non agganciarlo arbitrariamente all'ultimo requisito della
# clausola. Il chapeau del punto 3 specifica l'art. 45 terdecies §1 eIDAS2 (di
# cui i requisiti 7.5-03/-04/-05 dettagliano i singoli elementi: origine,
# ordine cronologico, integrita'), mentre il punto 3(a) rende vincolanti le
# specifiche di ETSI EN 319 401.
RELAZIONI = [
    {
        'nodo_da': ('principio', None, 'art. 1'),
        'nodo_a': ('principio', 2, 'art. 45 terdecies §3'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.95,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3'),
        'nodo_a': ('obbligo', 2, 'art. 45 terdecies §1'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('principio', None, 'allegato, punto 3(a)'),
        'nodo_a': ('principio', 10, 'clausola 1 (Scope)'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 6.2 REQ-6.2-03'),
        'nodo_a': ('obbligo', 10, 'REQ-6.2-03'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 6.3 REQ-6.3-04X'),
        'nodo_a': ('obbligo', 10, 'REQ-6.3-04'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 7.2 REQ-7.2-04X'),
        'nodo_a': ('obbligo', 10, 'REQ-7.2-04'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 7.2 REQ-7.2-05X'),
        'nodo_a': ('obbligo', 10, 'REQ-7.2-05'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 7.5 REQ-7.5-01X'),
        'nodo_a': ('obbligo', 10, 'REQ-7.5-01'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 7.5 REQ-7.5-02'),
        'nodo_a': ('obbligo', 10, 'REQ-7.5-05'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 7.8 REQ-7.8-14X'),
        'nodo_a': ('obbligo', 10, 'REQ-7.8-14'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 7.8 REQ-7.8-18X'),
        'nodo_a': ('obbligo', 10, 'REQ-7.8-18'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.8,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 7.8 REQ-7.8-21X'),
        'nodo_a': ('obbligo', 10, 'REQ-7.8-22'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.8,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 7.9.1 REQ-7.9.1-02X'),
        'nodo_a': ('obbligo', 10, 'REQ-7.9.1-02'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 7.12 REQ-7.12-02 A'),
        'nodo_a': ('obbligo', 10, 'REQ-7.12-02'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 7.12 REQ-7.12-02 A'),
        'nodo_a': ('principio', 2, 'art. 24 §5 (vigente, eIDAS2)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
]
