"""Estrazione granulare CAD (D.Lgs. 82/2005) - Capo IV fine (art. 48: PEC; art. 49: segretezza
della corrispondenza trasmessa per via telematica), Capo V parte 1 (artt. 50-61: disponibilita' dei
dati delle pubbliche amministrazioni, Piattaforma Digitale Nazionale Dati, sicurezza e disponibilita'
dei dati/sistemi/infrastrutture delle PA, accesso telematico e riutilizzo dei dati, siti internet e
contenuto dei siti delle PA, dati identificativi delle questioni pendenti, dati territoriali, basi di
dati di interesse nazionale, delocalizzazione dei registri informatici).

Testo ufficiale vigente al 16/09/2026, fonte app/.source_cache/cad/cap05.txt (ADR-0007).
Modulo generato secondo il contratto di app/seed_data/lib.py: nessun discrimine di rilevanza,
copertura completa comma/lettera per comma/lettera.
"""

RIGHE_OBBLIGHI = [{'riferimento': 'art. 48 c.1',
  'testo': 'Le comunicazioni telematiche che richiedono ricevuta di invio e di consegna '
           'devono avvenire tramite posta elettronica certificata secondo il DPR 68/2005, '
           'oppure mediante altre soluzioni tecnologiche individuate dalle Linee guida.',
  'testo_integrale': 'La trasmissione telematica di comunicazioni che necessitano di una '
                     'ricevuta di invio e di una ricevuta di consegna avviene mediante la '
                     'posta elettronica certificata ai sensi del decreto del Presidente della '
                     'Repubblica 11 febbraio 2005, n. 68, o mediante altre soluzioni '
                     'tecnologiche individuate con le Linee guida.',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 49 c.1',
  'testo': 'Gli addetti alle operazioni di trasmissione telematica di atti, dati e documenti '
           'informatici non possono prendere cognizione della corrispondenza telematica, né '
           "duplicare o cedere a terzi, anche in forma sintetica, informazioni sull'esistenza "
           'o sul contenuto di corrispondenza, comunicazioni o messaggi trasmessi per via '
           'telematica, salvo che si tratti di informazioni per loro natura o per espressa '
           'indicazione del mittente destinate a essere rese pubbliche.',
  'testo_integrale': 'Gli addetti alle operazioni di trasmissione per via telematica di atti, '
                     'dati e documenti formati con strumenti informatici non possono prendere '
                     'cognizione della corrispondenza telematica, duplicare con qualsiasi '
                     'mezzo o cedere a terzi a qualsiasi titolo informazioni anche in forma '
                     "sintetica o per estratto sull'esistenza o sul contenuto di "
                     'corrispondenza, comunicazioni o messaggi trasmessi per via telematica, '
                     'salvo che si tratti di informazioni per loro natura o per espressa '
                     'indicazione del mittente destinate ad essere rese pubbliche.',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente',
  'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}]},
 {'riferimento': 'art. 50 c.1',
  'testo': 'I dati delle pubbliche amministrazioni sono formati, raccolti, conservati, resi '
           "disponibili e accessibili con l'uso delle tecnologie dell'informazione e della "
           'comunicazione, in modo da consentirne la fruizione e il riutilizzo alle '
           "condizioni fissate dall'ordinamento da parte di altre pubbliche amministrazioni e "
           'dei privati, fermi restando i limiti di conoscibilità previsti dalla legge, le '
           'norme sulla protezione dei dati personali e la normativa comunitaria in materia '
           'di riutilizzo delle informazioni del settore pubblico.',
  'testo_integrale': 'I dati delle pubbliche amministrazioni sono formati, raccolti, '
                     "conservati, resi disponibili e accessibili con l'uso delle tecnologie "
                     "dell'informazione e della comunicazione che ne consentano la fruizione "
                     "e riutilizzazione, alle condizioni fissate dall'ordinamento, da parte "
                     'delle altre pubbliche amministrazioni e dai privati; restano salvi i '
                     "limiti alla conoscibilita' dei dati previsti dalle leggi e dai "
                     'regolamenti, le norme in materia di protezione dei dati personali ed il '
                     'rispetto della normativa comunitaria in materia di riutilizzo delle '
                     'informazioni del settore pubblico.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 50 c.2',
  'testo': 'Qualunque dato trattato da una pubblica amministrazione, salve le esclusioni '
           "dell'art. 2 c.6 e i casi dell'art. 24 L. 241/1990, e nel rispetto della normativa "
           'privacy, deve essere reso accessibile e fruibile alle altre amministrazioni '
           "quando l'utilizzo del dato sia necessario per lo svolgimento dei loro compiti "
           'istituzionali, senza oneri a loro carico salvo per elaborazioni aggiuntive; resta '
           "fermo quanto previsto dall'art. 43 commi 4 e 71 del DPR 445/2000.",
  'testo_integrale': 'Qualunque dato trattato da una pubblica amministrazione, con le '
                     "esclusioni di cui all'articolo 2, comma 6, salvi i casi previsti "
                     "dall'articolo 24 della legge 7 agosto 1990, n. 241, e nel rispetto "
                     "della normativa in materia di protezione dei dati personali, e' reso "
                     'accessibile e fruibile alle altre amministrazioni quando '
                     "l'utilizzazione del dato sia necessaria per lo svolgimento dei compiti "
                     "istituzionali dell'amministrazione richiedente, senza oneri a carico di "
                     "quest'ultima, salvo per la prestazione di elaborazioni aggiuntive; e' "
                     'fatto comunque salvo il disposto degli articoli 43, commi 4 e 71, del '
                     'decreto del Presidente della Repubblica 28 dicembre 2000, n. 445.',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 50 c.2-bis',
  'testo': "Le pubbliche amministrazioni, nell'ambito delle proprie funzioni istituzionali, "
           'analizzano i propri dati anche in combinazione con quelli detenuti da altri '
           "soggetti di cui all'art. 2 c.2, fermi i limiti del comma 1; l'attività si svolge "
           "secondo le modalità individuate dall'AgID con le Linee guida.",
  'testo_integrale': "Le pubbliche amministrazioni, nell'ambito delle proprie funzioni "
                     "istituzionali, procedono all'analisi dei propri dati anche in "
                     "combinazione con quelli detenuti da altri soggetti di cui all'articolo "
                     '2, comma 2, fermi restando i limiti di cui al comma 1. La predetta '
                     "attivita' si svolge secondo le modalita' individuate dall'AgID con le "
                     'Linee guida.',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 50 c.2-ter',
  'testo': 'Le pubbliche amministrazioni certificanti detentrici dei dati del comma 1 ne '
           'assicurano la fruizione da parte dei soggetti che hanno diritto ad accedervi. Le '
           'pubbliche amministrazioni detentrici dei dati assicurano, su richiesta dei '
           "soggetti privati di cui all'art. 2 DPR 445/2000, conferma scritta della "
           'corrispondenza tra quanto dichiarato e le risultanze dei dati da esse custoditi, '
           "secondo le modalità dell'art. 71 c.4 dello stesso DPR.",
  'testo_integrale': 'Le pubbliche amministrazioni certificanti detentrici dei dati di cui al '
                     'comma 1 ne assicurano la fruizione da parte dei soggetti che hanno '
                     'diritto ad accedervi. Le pubbliche amministrazioni detentrici dei dati '
                     "assicurano, su richiesta dei soggetti privati di cui all'articolo 2 del "
                     'decreto del Presidente della Repubblica 28 dicembre 2000, n. 445, '
                     'conferma scritta della corrispondenza di quanto dichiarato con le '
                     "risultanze dei dati da essa custoditi, con le modalita' di cui "
                     "all'articolo 71, comma 4 del medesimo decreto. (38)",
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 50 c.2-quater',
  'testo': "Le pubbliche amministrazioni, in attuazione del principio di unicità dell'invio, "
           'non richiedono a cittadini e imprese dati e informazioni già detenuti da '
           "un'amministrazione e assicurano lo scambio delle informazioni mediante la "
           "piattaforma di cui all'art. 50-ter fin dalla progettazione dei servizi e mediante "
           "l'identificativo univoco di cui all'art. 62, integrato nei propri sistemi; la "
           'consultazione diretta effettuata a tal fine si considera operata per finalità di '
           "rilevante interesse pubblico ai sensi dell'art. 43 DPR 445/2000; le banche dati "
           "pubbliche e i relativi servizi di accertamento d'ufficio sono resi "
           'automaticamente disponibili tramite la piattaforma a semplice richiesta dei '
           "soggetti dell'art. 2 c.2, con vigilanza sugli accessi secondo le Linee guida "
           'AgID.',
  'testo_integrale': "Le pubbliche amministrazioni, in attuazione del principio dell'unicita' "
                     "dell'invio, non richiedono ai cittadini e alle imprese dati e "
                     "informazioni gia' detenuti da un'amministrazione e assicurano ((lo "
                     'scambio)) delle informazioni mediante la piattaforma di cui '
                     "all'articolo 50-ter fin dalla progettazione dei servizi e mediante "
                     "l'identificativo univoco di cui all'articolo 62, integrato nei loro "
                     "sistemi. Ai sensi dell'articolo 43 del testo unico delle disposizioni "
                     'legislative e regolamentari in materia di documentazione '
                     'amministrativa, di cui al decreto del Presidente della Repubblica 28 '
                     "dicembre 2000, n. 445, si considera operata per finalita' di rilevante "
                     'interesse pubblico la consultazione diretta ai sensi del presente comma '
                     "da parte dei soggetti di cui all'articolo 2, comma 2, delle banche dati "
                     "pubbliche e i relativi servizi di accertamento d'ufficio di atti, "
                     "fatti, qualita' e stati soggettivi sono resi automaticamente "
                     "disponibili mediante la piattaforma di cui all'articolo 50-ter a "
                     "semplice richiesta per i soggetti di cui all'articolo 2, comma 2. La "
                     "vigilanza sugli accessi e' effettuata secondo quanto previsto dalle "
                     "linee guida adottate dall'AgID.",
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 50 c.3-ter',
  'testo': "L'inadempimento dell'obbligo di rendere disponibili i dati ai sensi "
           "dell'articolo, ovvero il ritardo nell'abilitare l'accesso ai servizi della "
           "piattaforma di cui all'art. 50-ter, costituisce mancato raggiungimento di uno "
           'specifico risultato e di un rilevante obiettivo per i dirigenti responsabili '
           'delle strutture competenti e comporta la riduzione, non inferiore al 30%, della '
           'retribuzione di risultato e del trattamento accessorio collegato alla performance '
           'individuale, oltre al divieto di attribuire premi o incentivi nelle medesime '
           "strutture; l'AgID effettua controlli annuali sul rispetto di tali obblighi e, in "
           "caso di violazione, si applica l'art. 18-bis.",
  'testo_integrale': "L'inadempimento dell'obbligo di rendere disponibili i dati ai sensi del "
                     "presente articolo ovvero il ritardo nell'abilitazione dell'accesso ai "
                     "servizi della piattaforma di cui all'articolo 50-ter costituisce "
                     'mancato raggiungimento di uno specifico risultato e di un rilevante '
                     'obiettivo da parte dei dirigenti responsabili delle strutture '
                     'competenti e comporta la riduzione, non inferiore al 30 per cento, '
                     'della retribuzione di risultato e del trattamento accessorio collegato '
                     'alla performance individuale dei dirigenti competenti, oltre al divieto '
                     "di attribuire premi o incentivi nell'ambito delle medesime strutture. "
                     "L'AgID effettua controlli annuali sul rispetto degli obblighi di cui al "
                     'presente articolo. In caso di violazione degli obblighi di cui al '
                     "presente articolo si applica l'articolo 18-bis.",
  'tipo_obbligo': 'sanzionatorio',
  'stato': 'vigente',
  'sanzioni': 'Riduzione non inferiore al 30% della retribuzione di risultato e del '
              'trattamento accessorio collegato alla performance individuale dei dirigenti '
              'responsabili, divieto di attribuire premi o incentivi nella struttura, '
              "applicazione dell'art. 18-bis in caso di violazione."},
 {'riferimento': 'art. 50-ter c.1',
  'testo': 'La Presidenza del Consiglio dei ministri promuove la progettazione, lo sviluppo e '
           'la realizzazione della Piattaforma Digitale Nazionale Dati (PDND), finalizzata a '
           "favorire la conoscenza e l'utilizzo del patrimonio informativo detenuto per "
           "finalità istituzionali dai soggetti dell'art. 2 c.2, nonché la condivisione dei "
           "dati tra i soggetti che hanno diritto ad accedervi ai fini dell'attuazione "
           "dell'art. 50 e della semplificazione degli adempimenti amministrativi di "
           'cittadini e imprese, in conformità alla disciplina vigente.',
  'testo_integrale': 'La Presidenza del Consiglio dei ministri promuove la progettazione, lo '
                     'sviluppo e la realizzazione di una Piattaforma Digitale Nazionale Dati '
                     "(PDND) finalizzata a favorire la conoscenza e l'utilizzo del patrimonio "
                     "informativo detenuto, per finalita' istituzionali, dai soggetti di cui "
                     "all'articolo 2, comma 2, nonche' la condivisione dei dati tra i "
                     "soggetti che hanno diritto ad accedervi ai fini dell'attuazione "
                     "dell'articolo 50 e della semplificazione degli adempimenti "
                     "amministrativi dei cittadini e delle imprese, in conformita' alla "
                     'disciplina vigente. (38)',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 50-ter c.2',
  'testo': 'La PDND è gestita dalla Presidenza del Consiglio dei ministri ed è '
           "un'infrastruttura tecnologica che rende possibile l'interoperabilità dei sistemi "
           'informativi e delle basi di dati delle pubbliche amministrazioni e dei gestori di '
           'servizi pubblici, mediante accreditamento, identificazione e gestione dei livelli '
           'di autorizzazione dei soggetti abilitati, nonché raccolta e conservazione delle '
           'informazioni su accessi e transazioni; la condivisione avviene tramite interfacce '
           'di programmazione delle applicazioni (API) raccolte nel «catalogo API»; i '
           "soggetti dell'art. 2 c.2 sono tenuti ad accreditarsi, sviluppare le interfacce e "
           'rendere disponibili le proprie basi dati senza nuovi o maggiori oneri; in prima '
           "applicazione la Piattaforma assicura prioritariamente l'interoperabilità con le "
           "basi di dati di interesse nazionale dell'art. 60 c.3-bis e con le banche dati "
           "dell'Agenzia delle entrate; l'AgID, sentiti il Garante privacy e la Conferenza "
           'unificata, adotta linee guida su standard tecnologici, sicurezza, accessibilità, '
           'disponibilità e interoperabilità, nonché sul processo di accreditamento e '
           'fruizione del catalogo API.',
  'testo_integrale': "La Piattaforma Digitale Nazionale Dati e' gestita dalla Presidenza del "
                     "Consiglio dei ministri ed e' costituita da un'infrastruttura "
                     "tecnologica che rende possibile l'interoperabilita' dei sistemi "
                     'informativi e delle basi di dati delle pubbliche amministrazioni e dei '
                     "gestori di servizi pubblici per le finalita' di cui al comma 1, "
                     "mediante l'accreditamento, l'identificazione e la gestione dei livelli "
                     'di autorizzazione dei soggetti abilitati ad operare sulla stessa, '
                     "nonche' la raccolta e conservazione delle informazioni relative agli "
                     'accessi e alle transazioni effettuate suo tramite. La condivisione di '
                     'dati e informazioni avviene attraverso la messa a disposizione e '
                     "l'utilizzo, da parte dei soggetti accreditati, di interfacce di "
                     'programmazione delle applicazioni (API). Le interfacce, sviluppate dai '
                     'soggetti abilitati con il supporto della Presidenza del Consiglio dei '
                     "ministri e in conformita' alle Linee guida AgID in materia "
                     'interoperabilita\', sono raccolte nel "catalogo API" reso disponibile '
                     'dalla Piattaforma ai soggetti accreditati. I soggetti di cui '
                     "all'articolo 2, comma 2, sono tenuti ad accreditarsi alla piattaforma, "
                     'a sviluppare le interfacce e a rendere disponibili le proprie basi dati '
                     'senza nuovi o maggiori oneri per la finanza pubblica. In fase di prima '
                     'applicazione, la Piattaforma assicura prioritariamente '
                     "l'interoperabilita' con le basi di dati di interesse nazionale di cui "
                     "all'articolo 60, comma 3-bis e con le banche dati dell'Agenzie delle "
                     "entrate individuate dal Direttore della stessa Agenzia. L'AgID, sentito "
                     'il Garante per la protezione dei dati personali e acquisito il parere '
                     "della Conferenza unificata, di cui all'articolo 8 del decreto "
                     'legislativo 28 agosto 1997, n. 281, adotta linee guida con cui '
                     'definisce gli standard tecnologici e criteri di sicurezza, di '
                     "accessibilita', di disponibilita' e di interoperabilita' per la "
                     "gestione della piattaforma nonche' il processo di accreditamento e di "
                     'fruizione del catalogo API con i limiti e le condizioni di accesso '
                     'volti ad assicurare il corretto trattamento dei dati personali ai sensi '
                     'della normativa vigente. (38)',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 50-ter c.2-bis',
  'testo': 'Ultimati i test e le prove tecniche di corretto funzionamento della piattaforma, '
           "il Presidente del Consiglio dei Ministri o il Ministro delegato per l'innovazione "
           "tecnologica fissa il termine entro cui i soggetti dell'art. 2 c.2 devono "
           'accreditarsi alla piattaforma, sviluppare le interfacce del comma 2 e rendere '
           'disponibili le proprie basi dati.',
  'testo_integrale': 'Il Presidente del Consiglio dei Ministri o il Ministro delegato per '
                     "l'innovazione tecnologica e la transizione digitale, ultimati i test e "
                     'le prove tecniche di corretto funzionamento della piattaforma, fissa il '
                     "termine entro il quale i soggetti di cui all'articolo 2, comma 2, sono "
                     'tenuti ad accreditarsi alla stessa, a sviluppare le interfacce di cui '
                     'al comma 2 e a rendere disponibili le proprie basi dati. (38)',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 50-ter c.3',
  'testo': 'Nella PDND non sono conservati né trattati, oltre quanto strettamente necessario '
           'per le finalità del comma 1, i dati che possono essere resi disponibili relativi '
           'a ordine e sicurezza pubblica, difesa e sicurezza nazionale, difesa civile e '
           'soccorso pubblico, indagini preliminari, polizia giudiziaria e polizia '
           'economico-finanziaria; non possono comunque essere conferiti, conservati né '
           'trattati i dati coperti da segreto o riservati in tali materie.',
  'testo_integrale': "Nella Piattaforma Digitale Nazionale Dati non sono conservati, ne' "
                     'comunque trattati, oltre quanto strettamente necessario per le '
                     "finalita' di cui al comma 1, i dati, che possono essere resi "
                     'disponibili, attinenti a ordine e sicurezza pubblica, difesa e '
                     'sicurezza nazionale, difesa civile e soccorso pubblico, indagini '
                     'preliminari, polizia giudiziaria e polizia economico-finanziaria. Non '
                     "possono comunque essere conferiti, conservati, ne' trattati i dati "
                     "coperti da segreto o riservati nell'ambito delle materie indicate al "
                     'periodo precedente.',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente'},
 {'riferimento': 'art. 50-ter c.4',
  'testo': 'Con decreto del Presidente del Consiglio dei ministri, di concerto con il '
           "Ministero dell'economia e delle finanze e il Ministero dell'interno, sentiti il "
           'Garante privacy e la Conferenza Unificata, è stabilita la strategia nazionale '
           'dati, che identifica tipologie, limiti, finalità e modalità di messa a '
           'disposizione, su richiesta della Presidenza del Consiglio, dei dati aggregati e '
           "anonimizzati di cui sono titolari i soggetti dell'art. 2 c.2, in "
           "un'infrastruttura tecnologica della PDND separata da quella dedicata "
           "all'interoperabilità del comma 2; il decreto è comunicato alle Commissioni "
           'parlamentari competenti.',
  'testo_integrale': 'Con decreto adottato dal Presidente del Consiglio dei ministri entro '
                     'sessanta giorni dalla data di entrata in vigore della presente '
                     "disposizione,, di concerto con il Ministero dell'economia e delle "
                     "finanze e il Ministero dell'interno, sentito il Garante per la "
                     'protezione dei dati personali e acquisito il parere della Conferenza '
                     "Unificata di cui all'articolo 8 del decreto legislativo 28 agosto 1997, "
                     "n. 281, e' stabilita la strategia nazionale dati. Con la strategia "
                     "nazionale dati sono identificate le tipologie, i limiti, le finalita' e "
                     "le modalita' di messa a disposizione, su richiesta della Presidenza del "
                     'Consiglio dei ministri, dei dati aggregati e anonimizzati di cui sono '
                     "titolari i soggetti di cui all'articolo 2, comma 2, in apposita "
                     'infrastruttura tecnologica della Piattaforma Digitale Nazionale Dati '
                     'finalizzata al supporto di politiche pubbliche basate sui dati, '
                     "separata dall'infrastruttura tecnologica dedicata all'interoperabilita' "
                     'dei sistemi informativi di cui al comma 2. Il decreto di cui al '
                     "presente comma e' comunicato alle Commissioni parlamentari competenti. "
                     '(38)',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 50-ter c.5',
  'testo': "L'inadempimento dell'obbligo di rendere disponibili e accessibili le proprie basi "
           'dati, ovvero i dati aggregati e anonimizzati, costituisce mancato raggiungimento '
           'di uno specifico risultato e di un rilevante obiettivo per i dirigenti '
           'responsabili delle strutture competenti e comporta la riduzione, non inferiore al '
           '30%, della retribuzione di risultato e del trattamento accessorio collegato alla '
           'performance individuale, oltre al divieto di attribuire premi o incentivi nelle '
           'medesime strutture.',
  'testo_integrale': "L'inadempimento dell'obbligo di rendere disponibili e accessibili le "
                     'proprie basi dati ovvero i dati aggregati e anonimizzati costituisce '
                     'mancato raggiungimento di uno specifico risultato e di un rilevante '
                     'obiettivo da parte dei dirigenti responsabili delle strutture '
                     'competenti e comporta la riduzione, non inferiore al 30 per cento, '
                     'della retribuzione di risultato e del trattamento accessorio collegato '
                     'alla performance individuale dei dirigenti competenti, oltre al divieto '
                     "di attribuire premi o incentivi nell'ambito delle medesime strutture.",
  'tipo_obbligo': 'sanzionatorio',
  'stato': 'vigente',
  'sanzioni': 'Riduzione non inferiore al 30% della retribuzione di risultato e del '
              'trattamento accessorio collegato alla performance individuale dei dirigenti '
              'responsabili, divieto di attribuire premi o incentivi nella struttura.'},
 {'riferimento': 'art. 50-quater c.1',
  'testo': 'Al fine di valorizzare il patrimonio informativo pubblico per fini statistici, di '
           'ricerca e per i compiti istituzionali delle pubbliche amministrazioni, nei '
           'contratti e capitolati con cui le pubbliche amministrazioni affidano servizi in '
           "concessione è previsto l'obbligo del concessionario di rendere disponibili "
           "all'amministrazione concedente — che a sua volta li rende disponibili alle altre "
           "pubbliche amministrazioni per i medesimi fini e nel rispetto dell'art. 50 — tutti "
           'i dati acquisiti e generati nella fornitura del servizio agli utenti, inclusi '
           "quelli relativi al suo utilizzo, come dati di tipo aperto ai sensi dell'art. 1 "
           'c.1 lett. l-ter), nel rispetto delle linee guida AgID e sentito il Garante '
           'privacy.',
  'testo_integrale': 'Al fine di promuovere la valorizzazione del patrimonio informativo '
                     'pubblico, per fini statistici e di ricerca e per lo svolgimento dei '
                     'compiti istituzionali delle pubbliche amministrazioni, nei contratti e '
                     'nei capitolati con i quali le pubbliche amministrazioni affidano lo '
                     "svolgimento di servizi in concessione e' previsto l'obbligo del "
                     "concessionario di rendere disponibili all'amministrazione concedente "
                     '((, che a sua volta li rende disponibili alle altre pubbliche '
                     "amministrazioni per i medesimi fini e nel rispetto dell'articolo 50,)) "
                     'tutti i dati acquisiti e generati nella fornitura del servizio agli '
                     "utenti e relativi anche all'utilizzo del servizio medesimo da parte "
                     "degli utenti, come dati di tipo aperto ai sensi dell'articolo 1, comma "
                     '1, lettera l-ter), nel rispetto delle linee guida adottate da AgID, '
                     'sentito il Garante per la protezione dei dati personali.',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 51 c.1',
  'testo': 'Con le Linee guida sono individuate le soluzioni tecniche idonee a garantire la '
           "protezione, la disponibilità, l'accessibilità, l'integrità e la riservatezza dei "
           'dati, nonché la continuità operativa dei sistemi e delle infrastrutture.',
  'testo_integrale': 'Con le ((Linee guida)) sono individuate le soluzioni tecniche idonee a '
                     "garantire la protezione, la disponibilita', l'accessibilita', "
                     "l'integrita' e la riservatezza dei dati e la continuita' operativa dei "
                     'sistemi e delle infrastrutture.',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente'},
 {'riferimento': 'art. 51 c.1-bis lett.a',
  'testo': "L'AgID attua, per quanto di competenza e in raccordo con le altre autorità "
           'competenti, il Quadro strategico nazionale per la sicurezza dello spazio '
           'cibernetico e il Piano nazionale per la sicurezza cibernetica e informatica; in '
           'tale ambito coordina, tramite il CERT-PA istituito al suo interno, le iniziative '
           'di prevenzione e gestione degli incidenti di sicurezza informatici.',
  'testo_integrale': 'AgID attua, per quanto di competenza e in raccordo con le altre '
                     "autorita' competenti in materia, il Quadro strategico nazionale per la "
                     'sicurezza dello spazio cibernetico e il Piano nazionale per la '
                     'sicurezza cibernetica e la sicurezza informatica. AgID, in tale ambito: '
                     'a) coordina, tramite il Computer Emergency Response Team Pubblica '
                     'Amministrazione (CERT-PA) istituito nel suo ambito, le iniziative di '
                     'prevenzione e gestione degli incidenti di sicurezza informatici;',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 51 c.1-bis lett.b',
  'testo': "L'AgID promuove intese con le analoghe strutture internazionali.",
  'testo_integrale': 'b) promuove intese con le analoghe strutture internazionali;',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 51 c.1-bis lett.c',
  'testo': "L'AgID segnala al Ministro per la semplificazione e la pubblica amministrazione "
           'il mancato rispetto, da parte delle pubbliche amministrazioni, delle regole '
           'tecniche di cui al comma 1.',
  'testo_integrale': 'c) segnala al Ministro per ((la semplificazione e la pubblica '
                     'amministrazione)) il mancato rispetto delle regole tecniche di cui al '
                     'comma 1 da parte delle pubbliche amministrazioni.',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 51 c.2',
  'testo': 'I documenti informatici delle pubbliche amministrazioni devono essere custoditi e '
           'controllati con modalità tali da ridurre al minimo i rischi di distruzione, '
           'perdita, accesso non autorizzato o non consentito o non conforme alle finalità '
           'della raccolta.',
  'testo_integrale': 'I documenti informatici delle pubbliche amministrazioni devono essere '
                     "custoditi e controllati con modalita' tali da ridurre al minimo i "
                     'rischi di distruzione, perdita, accesso non autorizzato o non '
                     "consentito o non conforme alle finalita' della raccolta.",
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente'},
 {'riferimento': 'art. 51 c.2-ter',
  'testo': "I soggetti di cui all'art. 2 c.2 aderiscono ogni anno ai programmi di sicurezza "
           "preventiva coordinati e promossi dall'AgID secondo le procedure dettate dalla "
           'medesima AgID con le Linee guida.',
  'testo_integrale': "I soggetti di cui all'articolo 2, comma 2, aderiscono ogni anno ai "
                     'programmi di sicurezza preventiva coordinati e promossi da AgID secondo '
                     'le procedure dettate dalla medesima AgID con le Linee guida.',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente'},
 {'riferimento': 'art. 51 c.2-quater',
  'testo': "I soggetti di cui all'art. 2 c.2, nel rispetto delle Linee guida AgID, "
           'predispongono piani di emergenza in grado di assicurare la continuità operativa '
           'delle operazioni indispensabili per i servizi erogati e il ritorno alla normale '
           "operatività; a tal fine è possibile ricorrere all'art. 15 L. 241/1990 per "
           "l'erogazione di servizi applicativi, infrastrutturali e di dati, con ristoro dei "
           'soli costi di funzionamento; per le Amministrazioni dello Stato coinvolte si '
           'provvede mediante rimodulazione degli stanziamenti dei pertinenti capitoli di '
           'spesa o mediante riassegnazione alla spesa degli importi versati a tale titolo ad '
           'apposito capitolo di entrata del bilancio statale.',
  'testo_integrale': 'I soggetti di cui articolo 2, comma 2, predispongono, nel rispetto '
                     "delle Linee guida adottate dall'AgID, piani di emergenza in grado di "
                     "assicurare la continuita' operativa delle operazioni indispensabili per "
                     "i servizi erogati e il ritorno alla normale operativita'. Onde "
                     "garantire quanto previsto, e' possibile il ricorso all'articolo 15 "
                     "della legge 7 agosto 1990, n. 241, per l'erogazione di servizi "
                     'applicativi, infrastrutturali e di dati, con ristoro dei soli costi di '
                     'funzionamento. Per le Amministrazioni dello Stato coinvolte si provvede '
                     'mediante rimodulazione degli stanziamenti dei pertinenti capitoli di '
                     'spesa o mediante riassegnazione alla spesa degli importi versati a tale '
                     'titolo ad apposito capitolo di entrata del bilancio statale.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 52 c.3',
  'testo': 'Nella definizione dei capitolati o degli schemi dei contratti di appalto relativi '
           'a prodotti e servizi che comportino la formazione, la raccolta e la gestione di '
           "dati, i soggetti di cui all'art. 2 c.2 prevedono clausole idonee a consentirne "
           "l'utilizzazione in conformità a quanto previsto dall'art. 50.",
  'testo_integrale': 'Nella definizione dei capitolati o degli schemi dei contratti di '
                     'appalto relativi a prodotti e servizi che comportino ((la formazione, '
                     "la raccolta e la gestione di dati, i soggetti di cui all'articolo 2, "
                     "comma 2, prevedono clausole idonee a consentirne l'utilizzazione in "
                     "conformita' a quanto previsto dall'articolo 50)).",
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 52 c.4',
  'testo': "Le attività volte a garantire l'accesso telematico e il riutilizzo dei dati delle "
           'pubbliche amministrazioni rientrano tra i parametri di valutazione della '
           'performance dirigenziale.',
  'testo_integrale': "Le attivita' volte a garantire l'accesso telematico e il riutilizzo dei "
                     'dati delle pubbliche amministrazioni rientrano tra i parametri di '
                     'valutazione della performance dirigenziale ((...)).',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 52 c.9',
  'testo': "L'Agenzia svolge le attività indicate dall'articolo con le risorse umane, "
           'strumentali e finanziarie previste a legislazione vigente.',
  'testo_integrale': "L'Agenzia svolge le attivita' indicate dal presente articolo con le "
                     'risorse umane, strumentali, e finanziarie previste a legislazione '
                     'vigente.(19)',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 53 c.1',
  'testo': 'Le pubbliche amministrazioni realizzano siti istituzionali su reti telematiche '
           'che rispettano i principi di accessibilità, elevata usabilità e reperibilità '
           'anche per le persone disabili, completezza di informazione, chiarezza di '
           'linguaggio, affidabilità, semplicità di consultazione, qualità, omogeneità e '
           'interoperabilità; sono in particolare resi facilmente reperibili e consultabili i '
           "dati di cui all'art. 54.",
  'testo_integrale': 'Le pubbliche amministrazioni realizzano siti istituzionali su reti '
                     "telematiche che rispettano i principi di accessibilita', nonche' di "
                     "elevata usabilita' e reperibilita', anche da parte delle persone "
                     'disabili, completezza di informazione, chiarezza di linguaggio, '
                     "affidabilita', semplicita' di' consultazione, qualita', omogeneita' ed "
                     "interoperabilita'. Sono in particolare resi facilmente reperibili e "
                     "consultabili i dati di cui all'articolo 54.",
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 53 c.1-bis',
  'testo': "Le pubbliche amministrazioni pubblicano, ai sensi dell'art. 9 D.Lgs. 33/2013, "
           'anche il catalogo dei dati e dei metadati nonché delle relative banche dati in '
           "loro possesso e i regolamenti che disciplinano l'esercizio della facoltà di "
           'accesso telematico e il riutilizzo di tali dati e metadati, fatti salvi i dati '
           'presenti in Anagrafe tributaria.',
  'testo_integrale': "Le pubbliche amministrazioni pubblicano, ai sensi dell'articolo 9 del "
                     'decreto legislativo 14 marzo 2013, n. 33, anche il catalogo dei dati e '
                     "dei metadati ((...)), nonche' delle relative banche dati in loro "
                     "possesso e i regolamenti che disciplinano l'esercizio della facolta' di "
                     'accesso telematico e il riutilizzo di tali dati e metadati, fatti salvi '
                     'i dati presenti in Anagrafe tributaria.',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 54 c.1',
  'testo': 'I siti delle pubbliche amministrazioni contengono i dati di cui al D.Lgs. 33/2013 '
           'e successive modificazioni, recante il riordino della disciplina sugli obblighi '
           'di pubblicità, trasparenza e diffusione di informazioni da parte delle pubbliche '
           'amministrazioni, nonché quelli previsti dalla legislazione vigente.',
  'testo_integrale': 'I siti delle pubbliche amministrazioni contengono i dati di cui al '
                     'decreto legislativo 14 marzo 2013, n. 33, e successive modificazioni, '
                     'recante il riordino della disciplina riguardante gli obblighi di '
                     "pubblicita', trasparenza e diffusione di informazioni da parte delle "
                     "pubbliche amministrazioni ((, nonche' quelli previsti dalla "
                     'legislazione vigente)).',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 56 c.1',
  'testo': 'I dati identificativi delle questioni pendenti dinanzi al giudice amministrativo '
           'e contabile sono resi accessibili a chi vi abbia interesse mediante pubblicazione '
           'sul sistema informativo interno e sul sito istituzionale delle autorità emananti.',
  'testo_integrale': 'I dati identificativi delle questioni pendenti dinanzi al giudice '
                     'amministrativo e contabile sono resi accessibili a chi vi abbia '
                     'interesse mediante pubblicazione sul sistema informativo interno e sul '
                     "sito istituzionale ((...)) delle autorita' emananti.",
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 56 c.2',
  'testo': 'Le sentenze e le altre decisioni del giudice amministrativo e contabile, rese '
           'pubbliche mediante deposito in segreteria, sono contestualmente inserite nel '
           'sistema informativo interno e sul sito istituzionale, osservando le cautele '
           'previste dalla normativa sulla tutela dei dati personali.',
  'testo_integrale': 'Le sentenze e le altre decisioni del giudice amministrativo e '
                     'contabile, rese pubbliche mediante deposito in segreteria, sono '
                     'contestualmente inserite nel sistema informativo interno e sul sito '
                     'istituzionale ((...)), osservando le cautele previste dalla normativa '
                     'in materia di tutela dei dati personali.',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 59 c.3',
  'testo': 'Per agevolare la pubblicità dei dati di interesse generale, disponibili presso le '
           "pubbliche amministrazioni a livello nazionale, regionale e locale, presso l'AgID "
           'è istituito il Repertorio nazionale dei dati territoriali, quale infrastruttura '
           "di riferimento per l'erogazione dei servizi di ricerca dei dati territoriali e "
           "relativi servizi, e punto di accesso nazionale ai fini dell'attuazione della "
           'direttiva 2007/2/CE (INSPIRE) per quanto riguarda i metadati.',
  'testo_integrale': "Per agevolare la pubblicita' dei dati di interesse generale, "
                     'disponibili presso le pubbliche amministrazioni a livello nazionale, '
                     "regionale e locale, presso l'AgID e' istituito il Repertorio nazionale "
                     'dei dati territoriali, quale infrastruttura di riferimento per '
                     "l'erogazione dei servizi di ricerca dei dati territoriali, e relativi "
                     "servizi, e punto di accesso nazionale ai fini dell'attuazione della "
                     'direttiva 2007/2/CE (direttiva INSPIRE) per quanto riguarda i metadati.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 59 c.5',
  'testo': "Ai sensi dell'art. 71 sono adottate, anche su proposta delle amministrazioni "
           "competenti, le regole tecniche per la definizione e l'aggiornamento del contenuto "
           'del Repertorio nazionale dei dati territoriali di cui al comma 3, nonché per la '
           'formazione, la documentazione, lo scambio e il riutilizzo dei dati territoriali '
           'detenuti dalle amministrazioni stesse.',
  'testo_integrale': "((Ai)) sensi dell'articolo 71 sono adottate, anche su proposta delle "
                     'amministrazioni competenti, le regole tecniche per la definizione e '
                     "l'aggiornamento del contenuto del Repertorio nazionale dei dati "
                     "territoriali di cui al comma 3 nonche' per la formazione, la "
                     'documentazione, lo scambio e il riutilizzo dei dati territoriali '
                     'detenuti dalle amministrazioni stesse.',
  'tipo_obbligo': 'procedurale',
  'stato': 'vigente'},
 {'riferimento': 'art. 59 c.7',
  'testo': 'Agli oneri finanziari di cui al comma 3 si provvede con il fondo di finanziamento '
           "per i progetti strategici del settore informatico di cui all'art. 27 c.2 della "
           'legge 16 gennaio 2003, n. 3.',
  'testo_integrale': 'Agli oneri finanziari di cui al comma 3 si provvede con il fondo di '
                     'finanziamento per i progetti strategici del settore informatico di cui '
                     "all'articolo 27, comma 2, della legge 16 gennaio 2003, n. 3.",
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.2',
  'testo': 'Ferme le competenze di ciascuna pubblica amministrazione, le basi di dati di '
           'interesse nazionale costituiscono, per ciascuna tipologia di dati, un sistema '
           'informativo unitario che tiene conto dei diversi livelli istituzionali e '
           "territoriali e garantisce l'allineamento delle informazioni e l'accesso alle "
           'medesime da parte delle pubbliche amministrazioni interessate; tali sistemi '
           'informativi possiedono le caratteristiche minime di sicurezza, accessibilità e '
           'interoperabilità e sono realizzati e aggiornati secondo le Linee guida e le '
           'vigenti regole del Sistema statistico nazionale di cui al D.Lgs. 322/1989.',
  'testo_integrale': 'Ferme le competenze di ciascuna pubblica amministrazione, le basi di '
                     'dati di interesse nazionale costituiscono, per ciascuna tipologia di '
                     'dati, un sistema informativo unitario che tiene conto dei diversi '
                     "livelli istituzionali e territoriali e che garantisce l'allineamento "
                     "delle informazioni e l'accesso alle medesime da parte delle pubbliche "
                     'amministrazioni interessate. Tali sistemi informativi possiedono le '
                     "caratteristiche minime di sicurezza, accessibilita' e interoperabilita' "
                     'e sono realizzati e aggiornati secondo le Linee guida e secondo le '
                     'vigenti regole del Sistema statistico nazionale di cui al decreto '
                     'legislativo 6 settembre 1989, n. 322, e successive modificazioni.',
  'tipo_obbligo': 'tecnico/sicurezza',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.2-bis',
  'testo': 'Le pubbliche amministrazioni responsabili delle basi dati di interesse nazionale '
           "consentono il pieno utilizzo delle informazioni ai soggetti di cui all'art. 2 "
           'c.2, secondo standard e criteri di sicurezza e di gestione definiti nelle Linee '
           "guida e mediante la piattaforma di cui all'art. 50-ter.",
  'testo_integrale': 'Le pubbliche amministrazioni responsabili delle basi dati di interesse '
                     'nazionale consentono il pieno utilizzo delle informazioni ai soggetti '
                     "di cui all'articolo 2, comma 2, secondo standard e criteri di sicurezza "
                     'e di gestione definiti nelle Linee guida e mediante la piattaforma di '
                     "cui all'articolo 50-ter.",
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.3-ter',
  'testo': "L'AgID, tenuto conto delle esigenze delle pubbliche amministrazioni e degli "
           'obblighi derivanti dai regolamenti comunitari, individua, aggiorna e pubblica '
           "l'elenco delle basi di dati di interesse nazionale, ulteriori rispetto a quelle "
           'individuate in via prioritaria dal comma 3-bis.',
  'testo_integrale': 'AgID, tenuto conto delle esigenze delle pubbliche amministrazioni e '
                     'degli obblighi derivanti dai regolamenti comunitari, individua, '
                     "aggiorna e pubblica l'elenco delle basi di dati di interesse nazionale, "
                     'ulteriori rispetto a quelle individuate in via prioritaria dal comma '
                     '3-bis. ((38))',
  'tipo_obbligo': 'informativo/trasparenza',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.4',
  'testo': "Agli oneri finanziari di cui all'articolo si provvede con il fondo di "
           "finanziamento per i progetti strategici del settore informatico di cui all'art. "
           '27 c.2 della legge 16 gennaio 2003, n. 3.',
  'testo_integrale': 'Agli oneri finanziari di cui al presente articolo si provvede con il '
                     'fondo di finanziamento per i progetti strategici del settore '
                     "informatico di cui all'articolo 27, comma 2, della legge 16 gennaio "
                     '2003, n. 3.',
  'tipo_obbligo': 'organizzativo',
  'stato': 'vigente'},
 {'riferimento': 'art. 61 c.1',
  'testo': 'I pubblici registri immobiliari possono essere formati e conservati su supporti '
           'informatici in conformità alle disposizioni del codice, secondo le Linee guida, '
           'nel rispetto della normativa speciale e dei principi stabiliti dal codice civile; '
           'in tal caso i registri possono essere conservati anche in luogo diverso '
           "dall'Ufficio territoriale competente.",
  'testo_integrale': 'I pubblici registri immobiliari possono essere formati e conservati su '
                     "supporti informatici in conformita' alle disposizioni del presente "
                     'codice, secondo le ((Linee guida)), nel rispetto della normativa '
                     'speciale e dei principi stabiliti dal codice civile. In tal caso i '
                     'predetti registri possono essere conservati anche in luogo diverso '
                     "dall'Ufficio territoriale competente.",
  'tipo_obbligo': 'di conservazione',
  'stato': 'vigente'}]

RIGHE_PRINCIPI = [{'riferimento': 'art. 48 c.2',
  'testo': 'La trasmissione del documento informatico per via telematica effettuata secondo '
           'il comma 1 equivale, salvo diversa disposizione di legge, alla notificazione a '
           'mezzo posta.',
  'testo_integrale': 'La trasmissione del documento informatico per via telematica, '
                     'effettuata ai sensi del comma 1, equivale, salvo che la legge disponga '
                     'diversamente, alla notificazione per mezzo della posta.',
  'tipo_principio': 'equivalenza giuridica',
  'stato': 'vigente'},
 {'riferimento': 'art. 48 c.3',
  'testo': 'Data e ora di trasmissione e ricezione di un documento informatico trasmesso ai '
           'sensi del comma 1 sono opponibili ai terzi se conformi al DPR 68/2005 e alle '
           'relative regole tecniche, oppure conformi alle Linee guida.',
  'testo_integrale': "La data e l'ora di trasmissione e di ricezione di un documento "
                     'informatico trasmesso ai sensi del comma 1 sono opponibili ai terzi se '
                     'conformi alle disposizioni di cui al decreto del Presidente della '
                     'Repubblica 11 febbraio 2005, n. 68, ed alle relative regole tecniche, '
                     'ovvero conformi alle Linee guida.',
  'tipo_principio': 'valore probatorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 49 c.2',
  'testo': 'Ai fini del codice, gli atti, i dati e i documenti trasmessi per via telematica '
           'si considerano, nei confronti del gestore del sistema di trasporto delle '
           'informazioni, di proprietà del mittente fino a quando non sia avvenuta la '
           'consegna al destinatario.',
  'testo_integrale': 'Agli effetti del presente codice, gli atti, i dati e i documenti '
                     'trasmessi per via telematica si considerano, nei confronti del gestore '
                     "del sistema di trasporto delle informazioni, di proprieta' del mittente "
                     'sino a che non sia avvenuta la consegna al destinatario.',
  'tipo_principio': 'presunzione legale',
  'stato': 'vigente',
  'oggetti_giuridici': ['documento elettronico']},
 {'riferimento': 'art. 50 c.3',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 13 DICEMBRE 2017, N. 217.',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 50 c.3-bis',
  'testo': 'Il trasferimento di un dato da un sistema informativo a un altro non modifica la '
           'titolarità del dato e del trattamento, ferme restando le responsabilità delle '
           'amministrazioni che ricevono e trattano il dato quali titolari autonomi del '
           'trattamento.',
  'testo_integrale': 'Il trasferimento di un dato da un sistema informativo a un altro non '
                     "modifica la titolarita' del dato e del trattamento, ferme restando le "
                     "responsabilita' delle amministrazioni che ricevono e trattano il dato "
                     "in qualita' di titolari autonomi del trattamento. (38)",
  'tipo_principio': 'altro',
  'stato': 'vigente'},
 {'riferimento': 'art. 50-bis',
  'testo': 'Articolo abrogato dal D.Lgs. 26 agosto 2016, n. 179.',
  'testo_integrale': '((ARTICOLO ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179))',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 50-ter c.6',
  'testo': "L'accesso ai dati tramite la PDND non modifica la disciplina sulla titolarità del "
           "trattamento, ferme restando le specifiche responsabilità dell'art. 28 GDPR in "
           'capo al soggetto gestore della Piattaforma e le responsabilità dei soggetti '
           'accreditati che trattano i dati quali titolari autonomi del trattamento.',
  'testo_integrale': "L'accesso ai dati attraverso la Piattaforma Digitale Nazionale Dati non "
                     "modifica la disciplina relativa alla titolarita' del trattamento, ferme "
                     "restando le specifiche responsabilita' ai sensi dell'articolo 28 del "
                     'Regolamento (UE) 2016/679 del Parlamento Europeo e del Consiglio del 27 '
                     "aprile 2016 in capo al soggetto gestore della Piattaforma nonche' le "
                     "responsabilita' dei soggetti accreditati che trattano i dati in "
                     "qualita' di titolari autonomi del trattamento.",
  'tipo_principio': 'altro',
  'stato': 'vigente'},
 {'riferimento': 'art. 50-ter c.7',
  'testo': "Resta fermo che i soggetti dell'art. 2 c.2 possono continuare a utilizzare anche "
           'i sistemi di interoperabilità già attivi.',
  'testo_integrale': "Resta fermo che i soggetti di cui all'articolo 2, comma 2, possono "
                     "continuare a utilizzare anche i sistemi di interoperabilita' gia' "
                     '((attivi)).',
  'tipo_principio': 'altro',
  'stato': 'vigente'},
 {'riferimento': 'art. 50-ter c.8',
  'testo': "Le attività previste dall'articolo si svolgono con le risorse umane, finanziarie "
           'e strumentali disponibili a legislazione vigente.',
  'testo_integrale': "Le attivita' previste dal presente articolo si svolgono con le risorse "
                     'umane, finanziarie e strumentali disponibili a legislazione vigente.',
  'tipo_principio': 'altro',
  'stato': 'vigente'},
 {'riferimento': 'art. 51 c.2-bis',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 52 c.1',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 52 c.2',
  'testo': "I dati e i documenti che i soggetti di cui all'art. 2 c.2 pubblicano, con "
           "qualsiasi modalità, senza l'espressa adozione di una licenza ai sensi dell'art. 2 "
           'c.1 lett. h) del D.Lgs. 36/2006, si intendono rilasciati come dati di tipo aperto '
           "ai sensi dell'art. 1 c.1 lett. l-bis) e l-ter) del codice, salvo che la "
           'pubblicazione riguardi dati personali.',
  'testo_integrale': "I dati e i documenti che ((i soggetti di cui all'articolo 2, comma 2,)) "
                     "pubblicano, con qualsiasi modalita', senza l'espressa adozione di una "
                     "licenza di cui all'articolo 2, comma 1, lettera h), del decreto "
                     'legislativo 24 gennaio 2006, n. 36, si intendono rilasciati come dati '
                     "di tipo aperto ai sensi ((all'articolo 1, comma 1, lettere l-bis) e "
                     'l-ter),)) del presente Codice, ad eccezione dei casi in cui la '
                     'pubblicazione riguardi dati personali del presente Codice. ((PERIODO '
                     'SOPPRESSO DAL D.LGS. 13 DICEMBRE 2017, N. 217)).',
  'tipo_principio': 'presunzione legale',
  'stato': 'vigente'},
 {'riferimento': 'art. 52 c.5',
  'testo': 'Comma abrogato.',
  'testo_integrale': '((COMMA ABROGATO DAL D.LGS. 13 DICEMBRE 2017, N. 217)).',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 52 c.6',
  'testo': 'Comma abrogato.',
  'testo_integrale': '((COMMA ABROGATO DAL D.LGS. 13 DICEMBRE 2017, N. 217)).',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 52 c.7',
  'testo': 'Comma abrogato.',
  'testo_integrale': '((COMMA ABROGATO DAL D.LGS. 13 DICEMBRE 2017, N. 217)).',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 52 c.8',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 53 c.1-ter',
  'testo': 'Con le Linee guida sono definite le modalità per la realizzazione e la modifica '
           'dei siti delle amministrazioni.',
  'testo_integrale': "Con le ((Linee guida)) sono definite le modalita' per la realizzazione "
                     'e la modifica dei siti delle amministrazioni.',
  'tipo_principio': 'altro',
  'stato': 'vigente'},
 {'riferimento': 'art. 53 c.2',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 53 c.3',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 55',
  'testo': 'Articolo abrogato dal D.Lgs. 26 agosto 2016, n. 179.',
  'testo_integrale': '((ARTICOLO ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179))',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 56 c.2-bis',
  'testo': 'I dati identificativi delle questioni pendenti, le sentenze e le altre decisioni '
           "depositate in cancelleria o segreteria dell'autorità giudiziaria di ogni ordine e "
           "grado sono comunque rese accessibili ai sensi dell'art. 51 del Codice privacy "
           '(D.Lgs. 196/2003).',
  'testo_integrale': 'I dati identificativi delle questioni pendenti, le sentenze e le altre '
                     "decisioni depositate in cancelleria o segreteria dell'autorita' "
                     'giudiziaria di ogni ordine e grado sono, comunque, rese accessibili ai '
                     "sensi dell'articolo 51 del codice in materia di protezione dei dati "
                     'personali approvato con decreto legislativo n. 196 del 2003.',
  'tipo_principio': 'altro',
  'stato': 'vigente'},
 {'riferimento': 'art. 57',
  'testo': 'Articolo abrogato dal D.Lgs. 14 marzo 2013, n. 33.',
  'testo_integrale': '((ARTICOLO ABROGATO DAL D.LGS. 14 MARZO 2013, N. 33)).',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 57-bis',
  'testo': 'Articolo abrogato dal D.Lgs. 26 agosto 2016, n. 179.',
  'testo_integrale': '((ARTICOLO ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179))',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 58',
  'testo': 'Articolo abrogato dal D.Lgs. 26 agosto 2016, n. 179.',
  'testo_integrale': '((ARTICOLO ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179))',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 59 c.1',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 59 c.2',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 59 c.4',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 59 c.6',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 59 c.7-bis',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 60 c.1',
  'testo': "Si definisce base di dati di interesse nazionale l'insieme delle informazioni "
           'raccolte e gestite digitalmente dalle pubbliche amministrazioni, omogenee per '
           'tipologia e contenuto e la cui conoscenza è rilevante per lo svolgimento delle '
           'funzioni istituzionali delle altre pubbliche amministrazioni, anche solo per fini '
           'statistici, nel rispetto delle competenze e delle normative vigenti, e che '
           'possiedono i requisiti di cui al comma 2.',
  'testo_integrale': "Si definisce base di dati di interesse nazionale l'insieme delle "
                     'informazioni raccolte e gestite digitalmente dalle pubbliche '
                     'amministrazioni, omogenee per tipologia e contenuto e la cui conoscenza '
                     "e' rilevante per lo svolgimento delle funzioni istituzionali delle "
                     'altre pubbliche amministrazioni, anche solo per fini statistici, nel '
                     'rispetto delle competenze e delle normative vigenti e possiedono i '
                     'requisiti di cui al comma 2.',
  'tipo_principio': 'definitorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.2-ter',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.L. 16 LUGLIO 2020, N. 76.',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 60 c.3',
  'testo': 'Comma abrogato.',
  'testo_integrale': 'COMMA ABROGATO DAL D.LGS. 26 AGOSTO 2016, N. 179.',
  'tipo_principio': 'altro',
  'stato': 'abrogato'},
 {'riferimento': 'art. 60 c.3-bis lett.a',
  'testo': 'In sede di prima applicazione, sono individuate come basi di dati di interesse '
           'nazionale, tra le altre: il repertorio nazionale dei dati territoriali.',
  'testo_integrale': 'In sede di prima applicazione , sono individuate le seguenti basi di '
                     'dati di interesse nazionale: a) repertorio nazionale dei dati '
                     'territoriali;',
  'tipo_principio': 'definitorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.3-bis lett.b',
  'testo': 'In sede di prima applicazione, sono individuate come basi di dati di interesse '
           "nazionale, tra le altre: l'anagrafe nazionale della popolazione residente.",
  'testo_integrale': 'In sede di prima applicazione , sono individuate le seguenti basi di '
                     'dati di interesse nazionale: b) anagrafe nazionale della popolazione '
                     'residente;',
  'tipo_principio': 'definitorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.3-bis lett.c',
  'testo': 'In sede di prima applicazione, sono individuate come basi di dati di interesse '
           'nazionale, tra le altre: la banca dati nazionale dei contratti pubblici di cui '
           "all'art. 62-bis.",
  'testo_integrale': 'In sede di prima applicazione , sono individuate le seguenti basi di '
                     'dati di interesse nazionale: c) banca dati nazionale dei contratti '
                     "pubblici di cui all'articolo 62-bis;",
  'tipo_principio': 'definitorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.3-bis lett.d',
  'testo': 'In sede di prima applicazione, sono individuate come basi di dati di interesse '
           'nazionale, tra le altre: il casellario giudiziale.',
  'testo_integrale': 'In sede di prima applicazione , sono individuate le seguenti basi di '
                     'dati di interesse nazionale: d) casellario giudiziale;',
  'tipo_principio': 'definitorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.3-bis lett.e',
  'testo': 'In sede di prima applicazione, sono individuate come basi di dati di interesse '
           'nazionale, tra le altre: il registro delle imprese.',
  'testo_integrale': 'In sede di prima applicazione , sono individuate le seguenti basi di '
                     'dati di interesse nazionale: e) registro delle imprese;',
  'tipo_principio': 'definitorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.3-bis lett.f',
  'testo': 'In sede di prima applicazione, sono individuate come basi di dati di interesse '
           'nazionale, tra le altre: gli archivi automatizzati in materia di immigrazione e '
           "di asilo di cui all'art. 2 c.2 del DPR 242/2004.",
  'testo_integrale': 'In sede di prima applicazione , sono individuate le seguenti basi di '
                     'dati di interesse nazionale: f) gli archivi automatizzati in materia di '
                     "immigrazione e di asilo di cui all'articolo 2, comma 2, del decreto del "
                     'Presidente della Repubblica 27 luglio 2004, n. 242;',
  'tipo_principio': 'definitorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.3-bis lett.f-bis',
  'testo': 'In sede di prima applicazione, sono individuate come basi di dati di interesse '
           "nazionale, tra le altre: l'Anagrafe nazionale degli assistiti (ANA).",
  'testo_integrale': 'f-bis) Anagrafe nazionale degli assistiti (ANA);',
  'tipo_principio': 'definitorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.3-bis lett.f-ter',
  'testo': 'In sede di prima applicazione, sono individuate come basi di dati di interesse '
           "nazionale, tra le altre: l'anagrafe delle aziende agricole di cui all'art. 1 c.1 "
           'del regolamento DPR 503/1999.',
  'testo_integrale': "f-ter) anagrafe delle aziende agricole di cui all'articolo 1, comma 1, "
                     'del regolamento di cui al decreto del Presidente della Repubblica 1º '
                     'dicembre 1999, n. 503.',
  'tipo_principio': 'definitorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.3-bis lett.f-quater',
  'testo': 'In sede di prima applicazione, sono individuate come basi di dati di interesse '
           "nazionale, tra le altre: l'archivio nazionale dei veicoli e l'anagrafe nazionale "
           'degli abilitati alla guida di cui agli artt. 225 e 226 del D.Lgs. 285/1992 '
           '(codice della strada).',
  'testo_integrale': "f-quater) l'archivio nazionale dei veicoli e l'anagrafe nazionale degli "
                     'abilitati alla guida di cui agli articoli 225 e 226 del decreto '
                     'legislativo 30 aprile 1992, n. 285; ((38))',
  'tipo_principio': 'definitorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.3-bis lett.f-quinquies',
  'testo': 'In sede di prima applicazione, sono individuate come basi di dati di interesse '
           "nazionale, tra le altre: il sistema informativo dell'indicatore della situazione "
           "economica equivalente (ISEE) di cui all'art. 5 D.L. 201/2011.",
  'testo_integrale': "f-quinquies) il sistema informativo dell'indicatore della situazione "
                     "economica equivalente (ISEE) di cui all'articolo 5 del decreto-legge 6 "
                     'dicembre 2011, n. 201, convertito, con modificazioni, dalla legge 22 '
                     'dicembre 2011, n. 214; ((38))',
  'tipo_principio': 'definitorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.3-bis lett.f-sexies',
  'testo': 'In sede di prima applicazione, sono individuate come basi di dati di interesse '
           "nazionale, tra le altre: l'anagrafe nazionale dei numeri civici e delle strade "
           "urbane (ANNCSU) di cui all'art. 3 D.L. 179/2012.",
  'testo_integrale': "f-sexies) l'anagrafe nazionale dei numeri civici e delle strade urbane "
                     "(ANNCSU), di cui all'articolo 3 del decreto-legge 18 ottobre 2012, n. "
                     '179 convertito, con modificazioni, dalla legge 17 dicembre 2012, n. '
                     '221; ((38))',
  'tipo_principio': 'definitorio',
  'stato': 'vigente'},
 {'riferimento': 'art. 60 c.3-bis lett.f-septies',
  'testo': 'In sede di prima applicazione, sono individuate come basi di dati di interesse '
           "nazionale, tra le altre: l'indice nazionale dei domicili digitali delle persone "
           'fisiche, dei professionisti e degli altri enti di diritto privato non tenuti '
           "all'iscrizione in albi, elenchi o registri professionali o nel registro delle "
           "imprese di cui all'art. 6-quater.",
  'testo_integrale': "f-septies) l'indice nazionale dei domicili digitali delle persone "
                     'fisiche, dei professionisti e degli altri enti di diritto privato, non '
                     "tenuti all'iscrizione in albi, elenchi o registri professionali o nel "
                     "registro delle imprese di cui all'articolo 6-quater. ((38))",
  'tipo_principio': 'definitorio',
  'stato': 'vigente'}]

INDICE_ARTICOLI_LOCALE = ['art. 48 c.1',
 'art. 49 c.1',
 'art. 50 c.1',
 'art. 50 c.2',
 'art. 50 c.2-bis',
 'art. 50 c.2-ter',
 'art. 50 c.2-quater',
 'art. 50 c.3-ter',
 'art. 50-ter c.1',
 'art. 50-ter c.2',
 'art. 50-ter c.2-bis',
 'art. 50-ter c.3',
 'art. 50-ter c.4',
 'art. 50-ter c.5',
 'art. 50-quater c.1',
 'art. 51 c.1',
 'art. 51 c.1-bis lett.a',
 'art. 51 c.1-bis lett.b',
 'art. 51 c.1-bis lett.c',
 'art. 51 c.2',
 'art. 51 c.2-ter',
 'art. 51 c.2-quater',
 'art. 52 c.3',
 'art. 52 c.4',
 'art. 52 c.9',
 'art. 53 c.1',
 'art. 53 c.1-bis',
 'art. 54 c.1',
 'art. 56 c.1',
 'art. 56 c.2',
 'art. 59 c.3',
 'art. 59 c.5',
 'art. 59 c.7',
 'art. 60 c.2',
 'art. 60 c.2-bis',
 'art. 60 c.3-ter',
 'art. 60 c.4',
 'art. 61 c.1',
 'art. 48 c.2',
 'art. 48 c.3',
 'art. 49 c.2',
 'art. 50 c.3',
 'art. 50 c.3-bis',
 'art. 50-bis',
 'art. 50-ter c.6',
 'art. 50-ter c.7',
 'art. 50-ter c.8',
 'art. 51 c.2-bis',
 'art. 52 c.1',
 'art. 52 c.2',
 'art. 52 c.5',
 'art. 52 c.6',
 'art. 52 c.7',
 'art. 52 c.8',
 'art. 53 c.1-ter',
 'art. 53 c.2',
 'art. 53 c.3',
 'art. 55',
 'art. 56 c.2-bis',
 'art. 57',
 'art. 57-bis',
 'art. 58',
 'art. 59 c.1',
 'art. 59 c.2',
 'art. 59 c.4',
 'art. 59 c.6',
 'art. 59 c.7-bis',
 'art. 60 c.1',
 'art. 60 c.2-ter',
 'art. 60 c.3',
 'art. 60 c.3-bis lett.a',
 'art. 60 c.3-bis lett.b',
 'art. 60 c.3-bis lett.c',
 'art. 60 c.3-bis lett.d',
 'art. 60 c.3-bis lett.e',
 'art. 60 c.3-bis lett.f',
 'art. 60 c.3-bis lett.f-bis',
 'art. 60 c.3-bis lett.f-ter',
 'art. 60 c.3-bis lett.f-quater',
 'art. 60 c.3-bis lett.f-quinquies',
 'art. 60 c.3-bis lett.f-sexies',
 'art. 60 c.3-bis lett.f-septies']

MAPPATURA_LOCALE = {'art. 48 c.1': ['art. 48 c.1'],
 'art. 49 c.1': ['art. 49 c.1'],
 'art. 50 c.1': ['art. 50 c.1'],
 'art. 50 c.2': ['art. 50 c.2'],
 'art. 50 c.2-bis': ['art. 50 c.2-bis'],
 'art. 50 c.2-ter': ['art. 50 c.2-ter'],
 'art. 50 c.2-quater': ['art. 50 c.2-quater'],
 'art. 50 c.3-ter': ['art. 50 c.3-ter'],
 'art. 50-ter c.1': ['art. 50-ter c.1'],
 'art. 50-ter c.2': ['art. 50-ter c.2'],
 'art. 50-ter c.2-bis': ['art. 50-ter c.2-bis'],
 'art. 50-ter c.3': ['art. 50-ter c.3'],
 'art. 50-ter c.4': ['art. 50-ter c.4'],
 'art. 50-ter c.5': ['art. 50-ter c.5'],
 'art. 50-quater c.1': ['art. 50-quater c.1'],
 'art. 51 c.1': ['art. 51 c.1'],
 'art. 51 c.1-bis lett.a': ['art. 51 c.1-bis lett.a'],
 'art. 51 c.1-bis lett.b': ['art. 51 c.1-bis lett.b'],
 'art. 51 c.1-bis lett.c': ['art. 51 c.1-bis lett.c'],
 'art. 51 c.2': ['art. 51 c.2'],
 'art. 51 c.2-ter': ['art. 51 c.2-ter'],
 'art. 51 c.2-quater': ['art. 51 c.2-quater'],
 'art. 52 c.3': ['art. 52 c.3'],
 'art. 52 c.4': ['art. 52 c.4'],
 'art. 52 c.9': ['art. 52 c.9'],
 'art. 53 c.1': ['art. 53 c.1'],
 'art. 53 c.1-bis': ['art. 53 c.1-bis'],
 'art. 54 c.1': ['art. 54 c.1'],
 'art. 56 c.1': ['art. 56 c.1'],
 'art. 56 c.2': ['art. 56 c.2'],
 'art. 59 c.3': ['art. 59 c.3'],
 'art. 59 c.5': ['art. 59 c.5'],
 'art. 59 c.7': ['art. 59 c.7'],
 'art. 60 c.2': ['art. 60 c.2'],
 'art. 60 c.2-bis': ['art. 60 c.2-bis'],
 'art. 60 c.3-ter': ['art. 60 c.3-ter'],
 'art. 60 c.4': ['art. 60 c.4'],
 'art. 61 c.1': ['art. 61 c.1'],
 'art. 48 c.2': ['art. 48 c.2'],
 'art. 48 c.3': ['art. 48 c.3'],
 'art. 49 c.2': ['art. 49 c.2'],
 'art. 50 c.3': ['art. 50 c.3'],
 'art. 50 c.3-bis': ['art. 50 c.3-bis'],
 'art. 50-bis': ['art. 50-bis'],
 'art. 50-ter c.6': ['art. 50-ter c.6'],
 'art. 50-ter c.7': ['art. 50-ter c.7'],
 'art. 50-ter c.8': ['art. 50-ter c.8'],
 'art. 51 c.2-bis': ['art. 51 c.2-bis'],
 'art. 52 c.1': ['art. 52 c.1'],
 'art. 52 c.2': ['art. 52 c.2'],
 'art. 52 c.5': ['art. 52 c.5'],
 'art. 52 c.6': ['art. 52 c.6'],
 'art. 52 c.7': ['art. 52 c.7'],
 'art. 52 c.8': ['art. 52 c.8'],
 'art. 53 c.1-ter': ['art. 53 c.1-ter'],
 'art. 53 c.2': ['art. 53 c.2'],
 'art. 53 c.3': ['art. 53 c.3'],
 'art. 55': ['art. 55'],
 'art. 56 c.2-bis': ['art. 56 c.2-bis'],
 'art. 57': ['art. 57'],
 'art. 57-bis': ['art. 57-bis'],
 'art. 58': ['art. 58'],
 'art. 59 c.1': ['art. 59 c.1'],
 'art. 59 c.2': ['art. 59 c.2'],
 'art. 59 c.4': ['art. 59 c.4'],
 'art. 59 c.6': ['art. 59 c.6'],
 'art. 59 c.7-bis': ['art. 59 c.7-bis'],
 'art. 60 c.1': ['art. 60 c.1'],
 'art. 60 c.2-ter': ['art. 60 c.2-ter'],
 'art. 60 c.3': ['art. 60 c.3'],
 'art. 60 c.3-bis lett.a': ['art. 60 c.3-bis lett.a'],
 'art. 60 c.3-bis lett.b': ['art. 60 c.3-bis lett.b'],
 'art. 60 c.3-bis lett.c': ['art. 60 c.3-bis lett.c'],
 'art. 60 c.3-bis lett.d': ['art. 60 c.3-bis lett.d'],
 'art. 60 c.3-bis lett.e': ['art. 60 c.3-bis lett.e'],
 'art. 60 c.3-bis lett.f': ['art. 60 c.3-bis lett.f'],
 'art. 60 c.3-bis lett.f-bis': ['art. 60 c.3-bis lett.f-bis'],
 'art. 60 c.3-bis lett.f-ter': ['art. 60 c.3-bis lett.f-ter'],
 'art. 60 c.3-bis lett.f-quater': ['art. 60 c.3-bis lett.f-quater'],
 'art. 60 c.3-bis lett.f-quinquies': ['art. 60 c.3-bis lett.f-quinquies'],
 'art. 60 c.3-bis lett.f-sexies': ['art. 60 c.3-bis lett.f-sexies'],
 'art. 60 c.3-bis lett.f-septies': ['art. 60 c.3-bis lett.f-septies']}

RELAZIONI = [{'nodo_da': ('principio', None, 'art. 48 c.2'),
  'nodo_a': ('obbligo', None, 'art. 48 c.1'),
  'tipo_relazione': 'specifica',
  'evidence_type': 'textual',
  'confidence': 0.9},
 {'nodo_da': ('principio', None, 'art. 48 c.3'),
  'nodo_a': ('obbligo', None, 'art. 48 c.1'),
  'tipo_relazione': 'specifica',
  'evidence_type': 'textual',
  'confidence': 0.9},
 {'nodo_da': ('obbligo', None, 'art. 50 c.3-ter'),
  'nodo_a': ('obbligo', None, 'art. 50 c.2'),
  'tipo_relazione': 'sanziona',
  'evidence_type': 'textual',
  'confidence': 0.75},
 {'nodo_da': ('obbligo', None, 'art. 50 c.3-ter'),
  'nodo_a': ('obbligo', None, 'art. 50-ter c.2-bis'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.8},
 {'nodo_da': ('obbligo', None, 'art. 50-ter c.2-bis'),
  'nodo_a': ('obbligo', None, 'art. 50-ter c.2'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.85},
 {'nodo_da': ('obbligo', None, 'art. 50-ter c.4'),
  'nodo_a': ('obbligo', None, 'art. 50-ter c.2'),
  'tipo_relazione': 'si applica a',
  'evidence_type': 'textual',
  'confidence': 0.75},
 {'nodo_da': ('obbligo', None, 'art. 50-ter c.5'),
  'nodo_a': ('obbligo', None, 'art. 50-ter c.2'),
  'tipo_relazione': 'sanziona',
  'evidence_type': 'textual',
  'confidence': 0.75},
 {'nodo_da': ('obbligo', None, 'art. 50-ter c.2'),
  'nodo_a': ('principio', None, 'art. 60 c.1'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.7},
 {'nodo_da': ('obbligo', None, 'art. 51 c.1-bis lett.c'),
  'nodo_a': ('obbligo', None, 'art. 51 c.1'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.85},
 {'nodo_da': ('obbligo', None, 'art. 52 c.3'),
  'nodo_a': ('obbligo', None, 'art. 50 c.1'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.8},
 {'nodo_da': ('obbligo', None, 'art. 53 c.1'),
  'nodo_a': ('obbligo', None, 'art. 54 c.1'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.85},
 {'nodo_da': ('obbligo', None, 'art. 59 c.5'),
  'nodo_a': ('obbligo', None, 'art. 59 c.3'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.85},
 {'nodo_da': ('obbligo', None, 'art. 60 c.2-bis'),
  'nodo_a': ('obbligo', None, 'art. 50-ter c.1'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.8},
 {'nodo_da': ('obbligo', None, 'art. 50-quater c.1'),
  'nodo_a': ('obbligo', None, 'art. 50 c.1'),
  'tipo_relazione': 'richiama',
  'evidence_type': 'textual',
  'confidence': 0.75}]
