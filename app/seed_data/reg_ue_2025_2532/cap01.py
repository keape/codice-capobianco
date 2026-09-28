"""Regolamento di esecuzione (UE) 2025/2532 della Commissione, del 16 dicembre
2025 - norme di riferimento e specifiche per i servizi di archiviazione
elettronica qualificati (articolo 45 undecies, paragrafo 2, del regolamento
(UE) n. 910/2014, come modificato dal regolamento (UE) 2024/1183). Fonte
`reg_ue_2025_2532`, capitolo unico (articoli 1-3 + allegato). Testo ufficiale
italiano in app/.source_cache/reg_ue_2025_2532/cap01.txt (provenienza CELLAR
in provenance.json; il preambolo e' fuori dalla porzione assegnata).

Modellazione (ADR-0007, nessun comma/lettera non coperto, nessuno coperto due
volte):
- Paratesto amministrativo (epigrafe "Fatto a Bruxelles", firma della
  presidente, note a pie' di pagina alle citazioni degli atti: (1) GU eIDAS,
  (2)-(6) regolamenti/direttiva citati nel preambolo, intestazione "ALLEGATO"
  e suo titolo, riga ELI/ISSN) -> nessun nodo: non sono articoli, commi o
  lettere dell'allegato. Le due note a pie' di pagina dell'allegato
  ((1) regolamento (UE) 2024/482, (2) regolamento (UE) 2024/3144) non
  producono nodi propri: il loro contenuto identificativo e' gia' citato in
  "allegato, adeguamento a), voce 5" e "voce 6", e la nota e' corredo
  bibliografico di quelle voci, non una disposizione autonoma.
- Art. 1 §1 (l'EATSP mantiene l'affidabilita' delle firme/sigilli qualificati
  archiviati anche oltre il periodo di validita' tecnologica e l'integrita' e
  l'esattezza dell'origine almeno fino alla fine del periodo di conservazione
  legale o contrattuale) -> Obbligo "di conservazione", soggetto obbligato
  "QTSP/gestore" (l'EATSP e' un prestatore di servizi fiduciari qualificato):
  il tipo "di conservazione" e' quello pertinente per gli obblighi di
  archiviazione.
- Art. 1 §2 -> Principio "altro", non Obbligo: la norma attribuisce una
  facolta' ("possono avvalersi di un servizio di conservazione qualificato"),
  non impone un comportamento (stessa convenzione gia' usata nel censimento
  per le disposizioni permissive).
- Art. 2 -> Principio "altro": disposizione di mero rinvio (designa
  l'allegato come sede delle norme di riferimento e delle specifiche di cui
  all'art. 45 undecies §2 eIDAS2), ne' definitoria ne' di scopo/ambito.
- Art. 3 -> UN SOLO nodo Principio "altro" ("art. 3, entrata in vigore", il
  ventesimo giorno successivo alla pubblicazione in GUUE): il testo non
  contiene una disposizione di applicazione differita separata. La formula di
  chiusura "obbligatorio in tutti i suoi elementi e direttamente applicabile
  in ciascuno degli Stati membri" non produce un nodo, come in
  tutte le Fonti gia' censite: e' la formula standard di ogni regolamento UE
  self-executing, senza contenuto normativo distinto dalla forma giuridica
  "regolamento" gia' presupposta dal censimento.
- Allegato, chapeau (la frase che designa CEN/TS 18170:2025 e annuncia gli
  adattamenti) -> Principio "altro", un nodo a se': designa la norma di
  riferimento senza imporre un comportamento proprio, mentre le lettere
  a)-i) ne adattano il contenuto.
- Allegato, lettere a)-i): UN nodo per lettera, non uno per voce. Le voci con
  trattino ("—") interne a una lettera sono indicizzate separatamente
  ("allegato, adeguamento <lettera>, voce N"), come richiesto dal contratto di
  copertura, ma restano nel `testo_integrale` del nodo della lettera a cui
  appartengono: la lettera e' l'unita' di adattamento alla norma di
  riferimento e ogni voce ne e' contenuto specificativo. Il campo `testo`
  nomina esplicitamente ciascuna prescrizione autonoma contenuta nella
  lettera (es. in b) le due notifiche all'organismo di vigilanza con i
  termini di un mese e di tre mesi; in e) il dispositivo crittografico sicuro
  e il monitoraggio degli algoritmi; in f) la scansione delle vulnerabilita'
  trimestrale, il test di penetrazione annuale e la configurazione dei
  firewall; in i) la marcatura temporale qualificata).
- Numerazione delle voci interne: progressiva nell'ordine del documento
  entro la lettera ("voce 1", "voce 2", ...), incluse le sotto-voci con
  trattino della lettera b) ("un mese prima ...", "tre mesi prima ..."),
  che nella conversione del testo ufficiale stanno allo stesso livello delle
  altre voci e quindi ricevono numeri propri (voce 5, voce 6). Le sottolettere
  a)/b)/c) che il testo ufficiale usa dentro la lettera e) hanno invece nome
  annidato ("voce 4(a)", "voce 4(b)", "voce 4(c)") perche' il legame con la
  voce che le introduce e' esplicitato dal testo stesso.
- Lettera a) (aggiunta ai riferimenti normativi del punto 2 di CEN/TS 18170)
  -> Principio "altro": e' un'aggiunta bibliografica, nessun comportamento
  imposto. Lettere b)-i) -> Obbligo ciascuna, soggetto obbligato
  "QTSP/gestore" (l'EATSP); destinatari valorizzati solo dove il testo li
  nomina (lettera c): "gli abbonati" -> "Utente/titolare" e "le parti facenti
  affidamento sul servizio fiduciario di archiviazione elettronica" ->
  "Terzi affidanti/pubblico"). I subcontraenti nominati nella lettera d) non
  sono modellati come soggetti a se': il precetto vincola l'EATSP a garantire
  che il personale e i subcontraenti in ruoli di fiducia soddisfino il
  requisito di competenza (stessa lettura del batch: il soggetto obbligato e'
  l'EATSP).
- tipo_obbligo per lettera, non ovvio dove la lettera accorpa prescrizioni di
  natura diversa; criterio: la norma di riferimento o la famiglia di obblighi
  a cui la lettera rinvia, allineata alla classificazione gia' presente nel
  censimento per il nodo corrispondente della Fonte richiamata, per non
  introdurre incoerenze di classificazione tra l'originale e l'adattamento:
  b) "organizzativo" (CEN/TS 18170 punto 6.1 e ETSI EN 319 401 punto 5,
  dichiarazione sulla politica e sulla pratica: organizzativo nella Fonte
  ETSI EN 319 401); c) "informativo/trasparenza" (termini e condizioni, come
  REQ-6.2-xx di ETSI EN 319 401 e REQ-6.2-03 del Reg. 2025/2531);
  d) "organizzativo" (risorse umane, come la clausola 7.3 di ETSI EN 319 401);
  e) "tecnico/sicurezza" (controlli crittografici, come la clausola 7.5 di
  ETSI EN 319 401); f) "tecnico/sicurezza" (rete, come la clausola 7.8 di
  ETSI EN 319 401); g) "di conservazione" (raccolta delle prove, come i
  REQ-7.10-xx di ETSI EN 319 401, classificati "di conservazione" nel
  censimento); h) "organizzativo" (cessazione e piano di cessazione, come la
  clausola 7.13 di ETSI EN 319 401 e REQ-7.12-02 del Reg. 2025/2531);
  i) "tecnico/sicurezza" (orario affidabile degli eventi e marcatura
  temporale qualificata, come par. 4.2 del regolamento tecnico AgID sulla
  conservazione).
- testo_integrale: sempre verbatim e integrale, ottenuto unendo le righe
  spezzate dalla conversione e mantenendo il separatore "—" di ciascuna voce
  dell'elenco (le righe isolate "—" del testo ufficiale diventano il prefisso
  "— " della voce che seguono). Il titolo dell'articolo/lettera e' premesso
  dove il testo ufficiale lo precede immediatamente (art. 1, art. 2, art. 3,
  chapeau, ciascuna lettera); non e' ripetuto per "art. 1 §2", che nel testo
  ufficiale segue direttamente il §1. Nessuna riga valorizza severita' o
  sanzioni: l'atto non gradua i requisiti ne' prevede sanzioni proprie.
- RELAZIONI = [] per istruzione del batch: i collegamenti verso eIDAS/eIDAS2
  (art. 45 undecies §2, art. 24 §5), verso ETSI EN 319 401, ETSI EN 319 421,
  ISO/IEC 15408, FIPS PUB 140-3, CEN/TS 18170 e i regolamenti EUCC li
  costruisce la sessione principale, non questo modulo.

Copertura: 53 item di indice, 14 righe (9 Obblighi + 5 Principi).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 1 §1",
        "testo": "Nell'archiviare dati o documenti elettronici recanti firme elettroniche qualificate o sigilli elettronici qualificati, l'EATSP (prestatore di servizi di archiviazione elettronica qualificati) garantisce che l'affidabilità di tali firme e sigilli qualificati sia mantenuta anche oltre il loro periodo di validità tecnologica e che siano mantenute l'integrità e l'esattezza dell'origine delle firme elettroniche qualificate e dei sigilli elettronici qualificati, almeno fino alla fine del periodo di conservazione legale o contrattuale.",
        "testo_integrale": "Articolo 1\n\nArchiviazione elettronica di documenti recanti una firma elettronica qualificata o un sigillo elettronico qualificato\n\n1. Nell'archiviare dati elettronici o documenti elettronici recanti firme elettroniche qualificate o sigilli elettronici qualificati, i prestatori di servizi di archiviazione elettronica qualificati garantiscono che sia mantenuta l'affidabilità di tali firme elettroniche qualificate o sigilli elettronici qualificati, anche oltre il loro periodo di validità tecnologica, e che siano mantenute l'integrità e l'esattezza dell'origine delle firme elettroniche qualificate e dei sigilli elettronici qualificati, almeno fino alla fine del periodo di conservazione legale o contrattuale.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, adeguamento b) dichiarazione sulla politica e sulla pratica",
        "testo": "Adattamento della dichiarazione sulla politica e sulla pratica (punto 6.1 di CEN/TS 18170): si applicano i requisiti di CEN/TS 18170 punto 6.1 e i requisiti di ETSI EN 319 401 punto 5; l'EATSP stabilisce procedure per notificare all'organismo di vigilanza eventuali modifiche nella prestazione del servizio fiduciario di archiviazione elettronica e l'intenzione di cessare tali attività, conformemente ai requisiti commerciali e alle disposizioni legislative e regolamentari pertinenti e agli atti di esecuzione adottati a norma dell'art. 24 §5 del regolamento (UE) n. 910/2014 [i.2]; la notifica all'organismo di vigilanza competente è effettuata almeno un mese prima dell'attuazione di qualsiasi modifica e almeno tre mesi prima della cessazione prevista di una prestazione di servizi fiduciari.",
        "testo_integrale": "dichiarazione sulla politica e sulla pratica (punto 6.1)\n\n— Si applicano i requisiti della norma CEN/TS 18170, punto 6.1.\n\n— Si applicano i requisiti della norma ETSI EN 319 401, punto 5.\n\n— L'EATSP stabilisce procedure per notificare all'organismo di vigilanza eventuali modifiche nella prestazione del servizio fiduciario di archiviazione elettronica e l'intenzione di cessare tali attività, conformemente ai requisiti commerciali e alle disposizioni legislative e regolamentari pertinenti, anche conformemente ai requisiti degli atti di esecuzione adottati a norma dell'articolo 24, paragrafo 5, del regolamento (UE) n. 910/2014 [i.2].\n\n— L'EATSP effettua la notifica all'organismo di vigilanza competente almeno:\n\n— un mese prima dell'attuazione di qualsiasi modifica;\n\n— tre mesi prima della cessazione prevista di una prestazione di servizi fiduciari;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, adeguamento c) termini e condizioni",
        "testo": "Adattamento dei termini e condizioni (punto 6.2 di CEN/TS 18170): si applicano i requisiti di CEN/TS 18170 punto 6.2; prima di avviare una relazione contrattuale gli abbonati e le parti facenti affidamento sul servizio fiduciario di archiviazione elettronica sono informati in modo chiaro, completo e facilmente accessibile, in uno spazio accessibile al pubblico e individualmente, di termini e condizioni precisi.",
        "testo_integrale": "termini e condizioni (punto 6.2)\n\n— Si applicano i requisiti della norma CEN/TS 18170, punto 6.2.\n\n— Prima di avviare una relazione contrattuale gli abbonati e le parti facenti affidamento sul servizio fiduciario di archiviazione elettronica sono informati in modo chiaro, completo e facilmente accessibile, in uno spazio accessibile al pubblico e individualmente, di termini e condizioni precisi;",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato, adeguamento d) risorse umane",
        "testo": "Adattamento delle risorse umane (punto 7.3 di CEN/TS 18170): si applicano i requisiti di CEN/TS 18170 punto 7.3; il personale dell'EATSP in ruoli di fiducia e, se del caso, i subcontraenti dell'EATSP in ruoli di fiducia sono in grado di soddisfare il requisito in materia di competenze, esperienza e qualifiche mediante formazione e credenziali formali, o effettiva esperienza, o una combinazione di entrambe, compresi aggiornamenti periodici (almeno ogni 12 mesi) sulle nuove minacce e sulle attuali pratiche di sicurezza.",
        "testo_integrale": "risorse umane (punto 7.3)\n\n— Si applicano i requisiti della norma CEN/TS 18170, punto 7.3.\n\n— Il personale dell'EATSP in ruoli di fiducia e, se del caso, i subcontraenti dell'EATSP in ruoli di fiducia sono in grado di soddisfare il requisito in materia di «competenze, esperienza e qualifiche» mediante formazione e credenziali formali, o effettiva esperienza, o una combinazione di entrambe. Sono compresi aggiornamenti periodici (almeno ogni 12 mesi) sulle nuove minacce e sulle attuali pratiche di sicurezza;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, adeguamento e) controlli e monitoraggio crittografici",
        "testo": "Adattamento dei controlli e del monitoraggio crittografici (punto 7.6 di CEN/TS 18170): il sistema di archiviazione deve garantire la riservatezza dei dati e dei documenti durante l'intero ciclo di vita dell'archivio, dal deposito all'eliminazione; si applicano i requisiti di ETSI EN 319 401 sottopunto 7.5 «Controlli crittografici»; l'origine dei dati da archiviare è stabilita dall'EATSP e, se a tal fine utilizza firme o sigilli elettronici, questi sono qualificati; la chiave di firma privata dell'EATSP è conservata e utilizzata all'interno di un dispositivo qualificato per la creazione di una firma elettronica o di un sigillo elettronico o di un dispositivo crittografico sicuro che è un sistema affidabile certificato conformemente a: a) i criteri comuni per la valutazione della sicurezza delle tecnologie informatiche (ISO/IEC 15408 o documento «Common Criteria for Information Technology Security Evaluation», versione CC:2022, parti da 1 a 5) e certificato a livello EAL 4 o superiore; b) il sistema europeo di certificazione della cibersicurezza basato sui criteri comuni (regolamento (UE) 2024/482, regolamento (UE) 2024/3144) e certificato a livello EAL 4 o superiore; c) fino al 31.12.2030, il FIPS PUB 140-3 livello 3; tale certificazione riguarda un obiettivo di sicurezza o un profilo di protezione, o la progettazione di un modulo e la documentazione di sicurezza, che soddisfano i requisiti del presente documento, sulla base di un'analisi dei rischi e tenendo conto delle misure di sicurezza fisiche e di altre misure di sicurezza non tecniche; se il dispositivo crittografico sicuro beneficia di una certificazione EUCC (regolamento (UE) 2024/482, regolamento (UE) 2024/3144) è configurato e utilizzato conformemente a tale certificazione; l'EATSP monitora la resistenza dell'algoritmo crittografico usato e, se uno degli algoritmi o dei parametri utilizzati diventa inadeguato come definito nella gestione dei rischi, aggiorna la relativa politica di archiviazione o crea un nuovo profilo di archiviazione per gestire i pacchetti di archiviazione (Archive Information Package, AIP) e definisce ed esegue misure adeguate; la valutazione degli algoritmi crittografici e il loro utilizzo sono conformi ai meccanismi crittografici concordati approvati dal gruppo europeo per la certificazione della cibersicurezza e pubblicati dall'ENISA (ACM-ECCG); i componenti tecnici dell'EATS si autenticano reciprocamente sulla base di tecniche crittografiche prima di comunicare.",
        "testo_integrale": "controlli e monitoraggio crittografici (punto 7.6)\n\n— Il sistema di archiviazione deve garantire la riservatezza dei dati e dei documenti durante l'intero ciclo di vita dell'archivio, dal deposito all'eliminazione.\n\n— Si applicano i requisiti specificati nella norma ETSI EN 319 401, sottopunto 7.5 «Controlli crittografici».\n\n— L'origine dei dati da archiviare nel sistema di archiviazione elettronica è stabilita dall'EATSP. Se a tal fine sono utilizzati firme elettroniche o sigilli elettronici, tali firme elettroniche o sigilli elettronici sono qualificati.\n\n— Quando l'EATSP appone una firma digitale su (parte di) un oggetto o una registrazione digitale, la chiave di firma privata dell'EATSP è conservata e utilizzata all'interno di un dispositivo qualificato per la creazione di una firma elettronica o di un sigillo elettronico o di un dispositivo crittografico sicuro che è un sistema affidabile certificato conformemente:\n\n— a) ai criteri comuni per la valutazione della sicurezza delle tecnologie informatiche, quali definiti nella norma ISO/IEC 15408 o nel documento «Common Criteria for Information Technology Security Evaluation», versione CC:2022, parti da 1 a 5, pubblicato dai partecipanti all'accordo «Arrangement on the Recognition of Common Criteria Certificates in the field of IT Security», e certificato a livello EAL 4 o superiore; o\n\n— b) al sistema europeo di certificazione della cibersicurezza basato sui criteri comuni (regolamento (UE) 2024/482, regolamento (UE) 2024/3144) e certificato a livello EAL 4 o superiore; o\n\n— c) fino al 31.12.2030, al FIPS PUB 140-3 livello 3.\n\n— Tale certificazione riguarda un obiettivo di sicurezza o un profilo di protezione, o la progettazione di un modulo e la documentazione di sicurezza, che soddisfano i requisiti del presente documento, sulla base di un'analisi dei rischi e tenendo conto delle misure di sicurezza fisiche e di altre misure di sicurezza non tecniche.\n\n— Se il dispositivo crittografico sicuro beneficia di una certificazione EUCC (regolamento (UE) 2024/482, regolamento (UE) 2024/3144), tale dispositivo è configurato e utilizzato conformemente a tale certificazione.\n\n— L'EATSP monitora la resistenza dell'algoritmo crittografico che è stato ed è utilizzato. Nel caso in cui si ritenga che uno degli algoritmi o dei parametri utilizzati diventi inadeguato come definito nella gestione dei rischi, l'EATSP aggiorna la relativa politica di archiviazione o crea un nuovo profilo di archiviazione per gestire i pacchetti di archiviazione (Archive Information Package, AIP) e definire ed eseguire misure adeguate.\n\n— La valutazione degli algoritmi crittografici e il loro utilizzo da parte dell'EATSP sono conformi ai meccanismi crittografici concordati approvati dal gruppo europeo per la certificazione della cibersicurezza e pubblicati dall'ENISA (ACM-ECCG).\n\n— I componenti tecnici dell'EATS si autenticano reciprocamente sulla base di tecniche crittografiche prima di comunicare;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, adeguamento f) rete",
        "testo": "Adattamento della rete (punto 7.9 di CEN/TS 18170): si applicano i requisiti di ETSI EN 319 401 sottopunto 7.8 «Sicurezza della rete»; la scansione delle vulnerabilità richiesta dal requisito REQ-7.8-13 di ETSI EN 319 401 è eseguita almeno una volta a trimestre; il test di penetrazione richiesto dal requisito REQ-7.8-17X di ETSI EN 319 401 è eseguito almeno una volta all'anno; i firewall sono configurati in modo da bloccare tutti i protocolli e gli accessi non richiesti per il funzionamento dell'EATSP.",
        "testo_integrale": "rete (punto 7.9)\n\n— Si applicano i requisiti specificati nella norma ETSI EN 319 401, sottopunto 7.8 «Sicurezza della rete».\n\n— La scansione delle vulnerabilità richiesta dal requisito REQ-7.8-13 della norma ETSI EN 319 401 è eseguita almeno una volta a trimestre.\n\n— Il test di penetrazione richiesto dal requisito REQ-7.8-17X della norma ETSI EN 319 401 è eseguito almeno una volta all'anno.\n\n— I firewall sono configurati in modo da bloccare tutti i protocolli e gli accessi non richiesti per il funzionamento dell'EATSP;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, adeguamento g) raccolta delle prove",
        "testo": "Adattamento della raccolta delle prove (punto 7.11 di CEN/TS 18170): si applicano i requisiti di ETSI EN 319 401 sottopunto 7.10 «Raccolta di prove», anche per gli eventi critici e non critici (cfr. sottopunto 13.2).",
        "testo_integrale": "raccolta delle prove (punto 7.11)\n\n— Si applicano i requisiti specificati nella norma ETSI EN 319 401, sottopunto 7.10 «Raccolta di prove», anche per gli eventi critici e non critici (cfr. sottopunto 13.2);",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, adeguamento h) cessazione dell'EATSP e piano di cessazione",
        "testo": "Adattamento della cessazione dell'EATSP e del piano di cessazione (punto 7.13 di CEN/TS 18170): si applicano i requisiti di CEN/TS 18170 punto 7.13; il piano di cessazione dell'EATSP è conforme ai requisiti stabiliti negli atti di esecuzione adottati a norma dell'art. 24 §5 del regolamento (UE) n. 910/2014.",
        "testo_integrale": "cessazione dell'EATSP e piano di cessazione (punto 7.13)\n\n— Si applicano i requisiti della norma CEN/TS 18170, punto 7.13.\n\n— Il piano di cessazione dell'EATSP è conforme ai requisiti stabiliti negli atti di esecuzione adottati a norma dell'articolo 24, paragrafo 5, del regolamento (UE) n. 910/2014;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato, adeguamento i) orario affidabile degli eventi",
        "testo": "Adattamento dell'orario affidabile degli eventi (punto 13.3.1 di CEN/TS 18170): si applicano i requisiti di CEN/TS 18170 punto 13.3.1; quando utilizza la marcatura temporale, l'EATSP utilizza una marcatura temporale qualificata.",
        "testo_integrale": "orario affidabile degli eventi (punto 13.3.1)\n\n— Si applicano i requisiti della norma CEN/TS 18170, punto 13.3.1.\n\n— Quando utilizza la marcatura temporale, l'EATSP utilizza una marcatura temporale qualificata.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 1 §2",
        "testo": "Facoltà e non obbligo: ai fini del paragrafo 1, i prestatori di servizi di archiviazione elettronica qualificati possono avvalersi di un servizio di conservazione qualificato delle firme elettroniche qualificate o di un servizio di conservazione qualificato dei sigilli elettronici qualificati.",
        "testo_integrale": "2. Ai fini del paragrafo 1, i prestatori di servizi di archiviazione elettronica qualificati possono avvalersi di un servizio di conservazione qualificato delle firme elettroniche qualificate o di un servizio di conservazione qualificato dei sigilli elettronici qualificati.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2",
        "testo": "Le norme di riferimento e le specifiche di cui all'art. 45 undecies §2 del regolamento (UE) n. 910/2014 figurano nell'allegato del presente regolamento: disposizione di mero rinvio, che designa la sede delle norme tecniche senza imporre comportamenti né introdurre definizioni.",
        "testo_integrale": "Articolo 2\n\nNorme di riferimento e specifiche per la prestazione di servizi di archiviazione elettronica qualificati\n\nLe norme di riferimento e le specifiche di cui all'articolo 45 undecies, paragrafo 2, del regolamento (UE) n. 910/2014 figurano nell'allegato del presente regolamento.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 3, entrata in vigore",
        "testo": "Il presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea; il testo non prevede alcuna disposizione di applicazione differita separata.",
        "testo_integrale": "Articolo 3\n\nEntrata in vigore\n\nIl presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato, chapeau (norma di riferimento)",
        "testo": "La norma CEN/TS 18170:2025 («CEN/TS 18170») si applica con gli adattamenti elencati alle lettere a)-i), che ne integrano o specificano il contenuto: la designazione della norma di riferimento non impone di per sé alcun comportamento.",
        "testo_integrale": "CEN/TS 18170: 2025 («CEN/TS 18170»), si applica con i seguenti adattamenti:",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato, adeguamento a) riferimenti normativi",
        "testo": "Adattamento dei riferimenti normativi (punto 2 di CEN/TS 18170): sono aggiunti ETSI EN 319 401 V3.1.1 (2024-06), ETSI EN 319 421 V1.3.1 (2025-07), ISO 14721:2025, i meccanismi crittografici concordati ACM-ECCG pubblicati dall'ENISA, i regolamenti di esecuzione (UE) 2024/482 e (UE) 2024/3144, ISO/IEC 15408:2022 (parti da 1 a 5) e FIPS PUB 140-3 (2019): aggiunta bibliografica, nessun comportamento imposto.",
        "testo_integrale": "riferimenti normativi (punto 2)\n\n— ETSI EN 319 401 V3.1.1 (2024-06), «Electronic Signatures and Trust Infrastructures (ESI)»; «General Policy Requirements for Trust Service Providers».\n\n— ETSI EN 319 421 V1.3.1 (2025-07), «Electronic Signatures and Infrastructures (ESI)»; «Policy and Security Requirements for Trust Service Providers issuing Time-Stamps».\n\n— ISO 14721:2025, «Space Data System Practices — Reference model for an open archival information system (OAIS)».\n\n— ACM-ECCG; gruppo europeo per la certificazione della cibersicurezza, sottogruppo sulla crittografia: «Agreed Cryptographic Mechanisms» (meccanismi crittografici concordati) pubblicati dall'Agenzia dell'Unione europea per la cibersicurezza (ENISA).\n\n— Regolamento (UE) 2024/482; regolamento di esecuzione (UE) 2024/482 della Commissione (1).\n\n— Regolamento (UE) 2024/3144; regolamento di esecuzione (UE) 2024/3144 della Commissione (2).\n\n— ISO/IEC 15408:2022 (parti da 1 a 5), «Information security, cybersecurity and privacy protection – Evaluation criteria for IT security».\n\n— FIPS PUB 140-3 (2019) «Security Requirements for Cryptographic Modules»;",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 1 §1",
    "art. 1 §2",
    "art. 2",
    "art. 3, entrata in vigore",
    "allegato, chapeau (norma di riferimento)",
    "allegato, adeguamento a) riferimenti normativi",
    "allegato, adeguamento a), voce 1",
    "allegato, adeguamento a), voce 2",
    "allegato, adeguamento a), voce 3",
    "allegato, adeguamento a), voce 4",
    "allegato, adeguamento a), voce 5",
    "allegato, adeguamento a), voce 6",
    "allegato, adeguamento a), voce 7",
    "allegato, adeguamento a), voce 8",
    "allegato, adeguamento b) dichiarazione sulla politica e sulla pratica",
    "allegato, adeguamento b), voce 1",
    "allegato, adeguamento b), voce 2",
    "allegato, adeguamento b), voce 3",
    "allegato, adeguamento b), voce 4",
    "allegato, adeguamento b), voce 5",
    "allegato, adeguamento b), voce 6",
    "allegato, adeguamento c) termini e condizioni",
    "allegato, adeguamento c), voce 1",
    "allegato, adeguamento c), voce 2",
    "allegato, adeguamento d) risorse umane",
    "allegato, adeguamento d), voce 1",
    "allegato, adeguamento d), voce 2",
    "allegato, adeguamento e) controlli e monitoraggio crittografici",
    "allegato, adeguamento e), voce 1",
    "allegato, adeguamento e), voce 2",
    "allegato, adeguamento e), voce 3",
    "allegato, adeguamento e), voce 4",
    "allegato, adeguamento e), voce 4(a)",
    "allegato, adeguamento e), voce 4(b)",
    "allegato, adeguamento e), voce 4(c)",
    "allegato, adeguamento e), voce 5",
    "allegato, adeguamento e), voce 6",
    "allegato, adeguamento e), voce 7",
    "allegato, adeguamento e), voce 8",
    "allegato, adeguamento e), voce 9",
    "allegato, adeguamento f) rete",
    "allegato, adeguamento f), voce 1",
    "allegato, adeguamento f), voce 2",
    "allegato, adeguamento f), voce 3",
    "allegato, adeguamento f), voce 4",
    "allegato, adeguamento g) raccolta delle prove",
    "allegato, adeguamento g), voce 1",
    "allegato, adeguamento h) cessazione dell'EATSP e piano di cessazione",
    "allegato, adeguamento h), voce 1",
    "allegato, adeguamento h), voce 2",
    "allegato, adeguamento i) orario affidabile degli eventi",
    "allegato, adeguamento i), voce 1",
    "allegato, adeguamento i), voce 2",
]

MAPPATURA_LOCALE = {
    "art. 1 §1": ["art. 1 §1"],
    "art. 1 §2": ["art. 1 §2"],
    "art. 2": ["art. 2"],
    "art. 3, entrata in vigore": ["art. 3, entrata in vigore"],
    "allegato, chapeau (norma di riferimento)": ["allegato, chapeau (norma di riferimento)"],
    "allegato, adeguamento a) riferimenti normativi": [
        "allegato, adeguamento a) riferimenti normativi",
        "allegato, adeguamento a), voce 1",
        "allegato, adeguamento a), voce 2",
        "allegato, adeguamento a), voce 3",
        "allegato, adeguamento a), voce 4",
        "allegato, adeguamento a), voce 5",
        "allegato, adeguamento a), voce 6",
        "allegato, adeguamento a), voce 7",
        "allegato, adeguamento a), voce 8",
    ],
    "allegato, adeguamento b) dichiarazione sulla politica e sulla pratica": [
        "allegato, adeguamento b) dichiarazione sulla politica e sulla pratica",
        "allegato, adeguamento b), voce 1",
        "allegato, adeguamento b), voce 2",
        "allegato, adeguamento b), voce 3",
        "allegato, adeguamento b), voce 4",
        "allegato, adeguamento b), voce 5",
        "allegato, adeguamento b), voce 6",
    ],
    "allegato, adeguamento c) termini e condizioni": [
        "allegato, adeguamento c) termini e condizioni",
        "allegato, adeguamento c), voce 1",
        "allegato, adeguamento c), voce 2",
    ],
    "allegato, adeguamento d) risorse umane": [
        "allegato, adeguamento d) risorse umane",
        "allegato, adeguamento d), voce 1",
        "allegato, adeguamento d), voce 2",
    ],
    "allegato, adeguamento e) controlli e monitoraggio crittografici": [
        "allegato, adeguamento e) controlli e monitoraggio crittografici",
        "allegato, adeguamento e), voce 1",
        "allegato, adeguamento e), voce 2",
        "allegato, adeguamento e), voce 3",
        "allegato, adeguamento e), voce 4",
        "allegato, adeguamento e), voce 4(a)",
        "allegato, adeguamento e), voce 4(b)",
        "allegato, adeguamento e), voce 4(c)",
        "allegato, adeguamento e), voce 5",
        "allegato, adeguamento e), voce 6",
        "allegato, adeguamento e), voce 7",
        "allegato, adeguamento e), voce 8",
        "allegato, adeguamento e), voce 9",
    ],
    "allegato, adeguamento f) rete": [
        "allegato, adeguamento f) rete",
        "allegato, adeguamento f), voce 1",
        "allegato, adeguamento f), voce 2",
        "allegato, adeguamento f), voce 3",
        "allegato, adeguamento f), voce 4",
    ],
    "allegato, adeguamento g) raccolta delle prove": [
        "allegato, adeguamento g) raccolta delle prove",
        "allegato, adeguamento g), voce 1",
    ],
    "allegato, adeguamento h) cessazione dell'EATSP e piano di cessazione": [
        "allegato, adeguamento h) cessazione dell'EATSP e piano di cessazione",
        "allegato, adeguamento h), voce 1",
        "allegato, adeguamento h), voce 2",
    ],
    "allegato, adeguamento i) orario affidabile degli eventi": [
        "allegato, adeguamento i) orario affidabile degli eventi",
        "allegato, adeguamento i), voce 1",
        "allegato, adeguamento i), voce 2",
    ],
}

# Relazioni native (citazioni letterali, non il prodotto della pipeline di
# Fase 6). art. 2 attua la base giuridica dichiarata nei "visti" (art. 45
# undecies §2); art. 1 §1 specifica l'obbligo sostanziale del §1. I rinvii di
# clausola ("si applicano i requisiti di ETSI EN 319 401, punto 5 / sottopunto
# 7.5 / 7.8 / 7.10") restano senza relazione: la Fonte 10 ha nodi per id di
# requisito, non per clausola, quindi non esiste un nodo controparte esatto e
# non ne e' stato scelto uno arbitrario. La lettera h) ripete la clausola sul
# piano di cessazione gia' presente in tre altri atti del lotto (Fonti 8, 12 e
# 23): con queste tre relazioni il gruppo di clausole identiche e' collegato a
# rete completa, cosi' che da ognuno dei quattro atti si vedano gli altri tre.
RELAZIONI = [
    {
        'nodo_da': ('principio', None, 'art. 2'),
        'nodo_a': ('principio', 2, 'art. 45 undecies §2'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.95,
    },
    {
        'nodo_da': ('obbligo', None, 'art. 1 §1'),
        'nodo_a': ('obbligo', 2, 'art. 45 undecies §1'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, adeguamento b) dichiarazione sulla politica e sulla pratica'),
        'nodo_a': ('principio', 2, 'art. 24 §5 (vigente, eIDAS2)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, adeguamento f) rete'),
        'nodo_a': ('obbligo', 10, 'REQ-7.8-13'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        # L'atto cita "REQ-7.8-17X della norma ETSI EN 319 401" per il test di
        # penetrazione: nella versione censita (V3.2.1) quel requisito e'
        # REQ-7.8-18, mentre REQ-7.8-17 e' il malware detection.
        'nodo_da': ('obbligo', None, 'allegato, adeguamento f) rete'),
        'nodo_a': ('obbligo', 10, 'REQ-7.8-18'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.8,
    },
    {
        'nodo_da': ('obbligo', None, "allegato, adeguamento h) cessazione dell'EATSP e piano di cessazione"),
        'nodo_a': ('principio', 2, 'art. 24 §5 (vigente, eIDAS2)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, "allegato, adeguamento h) cessazione dell'EATSP e piano di cessazione"),
        'nodo_a': ('obbligo', 8, 'allegato, punto 6 (OVR-7.12-02)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, "allegato, adeguamento h) cessazione dell'EATSP e piano di cessazione"),
        'nodo_a': ('obbligo', 12, 'allegato, punto 4 (OVR-6.4.9-02)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', None, "allegato, adeguamento h) cessazione dell'EATSP e piano di cessazione"),
        'nodo_a': ('obbligo', 23, 'allegato, punto 3(a), 7.12 REQ-7.12-02 A'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
]
