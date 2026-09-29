"""Regolamento di esecuzione (UE) 2024/482 della Commissione, del 31 gennaio
2024 - modalita' di applicazione del regolamento (UE) 2019/881 per quanto
riguarda l'adozione del sistema europeo di certificazione della cibersicurezza
basato sui criteri comuni (EUCC). Fonte 29 (`reg_ue_2024_482`), capitolo 5 di
14 (vedi app/.source_cache/reg_ue_2024_482/manifest.json): Capo V -
Monitoraggio, non conformita' e non compliance (articoli 25-31), con le due
sezioni interne "SEZIONE I - Monitoraggio della compliance" (artt. 25-27) e
"SEZIONE II - Conformita' e compliance" (artt. 28-31). Gli artt. 1-24, 32-50 e
gli allegati I-IX sono nei capitoli 1-4 e 6-14, assegnati ad altri moduli:
nessuno di quei file e' toccato qui. La porzione assegnata si chiude con
l'art. 31 §3(b): l'art. 32 apre il Capo VI ed e' nel cap06, quindi questa
porzione non contiene nessuna formula di chiusura dell'atto.

Provenienza del testo: app/.source_cache/reg_ue_2024_482/cap05.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R0482, lingua italiana; URL
risolto .../cellar/687c0d05-c580-11ee-95d9-01aa75ed71a1.0014.03/DOC_1, XHTML
della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 540.435 byte
scaricati, 135.367 caratteri di testo, sha256 del raw.txt
b46d08cab6d63b2c190ae767042c07c1fc324955c22ef491eb314556b28ca5b8 - dettagli
completi in provenance.json). Il preambolo (considerando) e' a monte del Capo I
e non e' in questa porzione.

Modellazione (ADR-0007, nessun discrimine di rilevanza):
- Paratesto -> nessun nodo: i marcatori di struttura "CAPO V" /
  "MONITORAGGIO, NON CONFORMITA' E NON COMPLIANCE", "SEZIONE I" / "Monitoraggio
  della compliance" e "SEZIONE II" / "Conformita' e compliance" e le
  intestazioni dei sette articoli ("Articolo N" + rubrica) non sono articoli,
  commi o lettere. Le rubriche restano coperte perche' incluse nel
  `testo_integrale` della prima riga di ogni articolo (convenzione dei moduli
  gia' censiti, es. art. 3 del Reg. 2024/2979 e art. 1 del Reg. 2025/2532); il
  titolo di capitolo e quello delle sezioni non sono item di indice. Non
  compaiono in questa porzione epigrafe, firma, note a pie' di pagina, riga ELI
  ne' formula di chiusura (sono nel cap08), quindi non producono nodi ne' item
  di indice. Il capitolo e' contiguo: nessuna disposizione di questa porzione
  e' stata saltata per irrilevanza.
- Unita' di copertura: un comma = una riga. Le lettere sono item di indice
  distinti ("art. 25 §1(a)" ... "art. 25 §1(d)") mappati tutti alla riga del
  loro comma, con il testo verbatim delle lettere dentro il `testo_integrale`
  di quella riga (stessa convenzione di "art. 5 §1(a)" ... "art. 5 §1(h)" del
  Reg. 2024/2979 e delle lettere dei commi del Reg. 2025/1569). Nessuna lettera
  di questo capitolo ha un precetto autonomo separabile dal proprio chapeau:
  tutte le lettere degli artt. 25 §1, 25 §2, 25 §4, 26 §1, 26 §2, 27 §1 e
  29 §1 sono sintagmi nominali retti da un chapeau che porta esso stesso il
  predicato ("controlla:", "svolge ... sulla base:", "seleziona ... tra cui:",
  "monitora:", "svolge i compiti seguenti:"), e nel caso dell'art. 29 §1 le
  lettere (a) e (b) sono le due condizioni alternative della protasi, con
  l'apodosi ("l'organismo di certificazione fissa un termine ...") dopo la
  lettera (b): il precetto sta nel chapeau e nella apodosi, non nelle lettere.
  Le lettere dell'art. 31 §1 ("identifica", "richiede", "analizza", "informa")
  e dell'art. 31 §3 ("segnala", "valuta") hanno invece un verbo proprio e un
  chapeau nudo (solo soggetto e due punti, come l'art. 6 §3 del Reg.
  2024/2979): restano comunque nella riga del comma - e non una riga per
  lettera - perche' sono i passi di un'unica reazione immediata ("senza
  indebito ritardo") attivata dal medesimo presupposto, e scinderle
  lascerebbe senza nodo di riferimento i rinvii testuali che il capo fa al
  "paragrafo 1" di quegli stessi articoli (art. 31 §2 e §3). Le lettere
  dell'art. 30 non esistono: i suoi sei commi sono righe autonome.
- Obbligo vs Principio. Sono Obblighi i commi che prescrivono un comportamento
  a un soggetto identificabile (in questo capo il verbo all'indicativo e' la
  forma prescrittiva corrente: "controlla", "monitora", "informa", "notifica",
  "sospende", "fissa un termine"). Sono Principi i quattro commi che non
  impongono alcun comportamento:
  * art. 25 §7 ("puo' svolgere indagini o avvalersi di qualsiasi altro potere
    di monitoraggio") -> Principio "altro", potere conferito all'autorita'
    nazionale;
  * art. 26 §3 ("puo' elaborare norme volte a promuovere un dialogo
    periodico") -> Principio "altro", mera facolta' dell'autorita';
  * art. 28 §4 ("puo' sospendere senza indebito ritardo il certificato EUCC")
    -> Principio "altro", mera facolta' dell'organismo di certificazione;
  * art. 28 §7 ("Il presente articolo non si applica ai casi di
    vulnerabilita' ...") -> Principio "scopo/ambito di applicazione": e' una
    clausola di delimitazione dell'ambito dell'articolo 28, non un precetto.
  Stessa scelta del Reg. 2025/1569 cap02 per le facolta' di "puo'" e per le
  clausole di ambito. Fa eccezione, ed e' dichiarata qui, l'art. 30 §6: comma
  misto (facolta' di autorizzare la proroga della sospensione + limite
  imperativo "Il periodo complessivo di sospensione non puo' superare un
  anno") in cui prevale la parte prescrittiva, quindi Obbligo "procedurale"
  con `condizione_applicabilita` "in casi debitamente giustificati" - stesso
  criterio dei commi misti del Reg. 2025/1569 (art. 8 §3, art. 9 §5).
- Soggetti. Questo capo non riguarda i QTSP: i soggetti sono attori
  istituzionali e organismi di valutazione della conformita'. Le quattro
  categorie censite sono state applicate cosi' (convenzione gia' in uso nel
  Reg. 2025/1569 cap02):
  * "Terza parte" (ruolo "obbligato") per l'autorita' nazionale di
    certificazione della cibersicurezza, l'organismo di certificazione,
    l'ITSEF, l'organismo nazionale di accreditamento, le autorita' di
    vigilanza del mercato, l'ENISA e il gruppo europeo per la certificazione
    della cibersicurezza: soggetti con un ruolo identificabile e tracciabile,
    non QTSP ne' utenti finali;
  * "Utente/titolare" per il titolare di un certificato EUCC e per il
    richiedente la certificazione (art. 27 §1, art. 27 §2, art. 28 §3): la
    categoria e' descritta in CONTEXT.md come "il cliente/titolare del
    servizio (es. titolare di un certificato o di una firma)" ed e' l'unica
    che nomina il titolare del certificato;
  * "Terzi affidanti/pubblico" (ruolo "destinatario") solo nell'art. 30 §3,
    dove la sospensione va comunicata agli acquirenti dei prodotti TIC e resa
    pubblica: acquirenti e pubblico sono le parti che fanno affidamento sul
    certificato EUCC, e sono l'unica categoria di destinatari non
    istituzionali del capitolo.
  Nessuna riga ha soggetto "QTSP/gestore". Dove l'unico destinatario e' un
  altro attore "Terza parte" (art. 25 §8, art. 28 §2, art. 29 §4, art. 30 §2
  secondo destinatario, art. 30 §4, art. 31 §3(a)) il ruolo "destinatario" non
  e' stato valorizzato: il destinatario sarebbe della stessa categoria del
  soggetto obbligato e la riga direbbe due volte la stessa cosa.
- `tipo_obbligo` riga per riga. "procedurale" per le attivita' di controllo,
  campionamento, riesame, fissazione di termini, decisioni e notifiche interne
  alla procedura di certificazione (art. 25 §1-§4, §6; art. 26 §1-§2;
  art. 27 §2; art. 28 §1, §3, §5; art. 29 §1; art. 30 §1, §6; art. 31 §1-§3);
  "informativo/trasparenza" per i commi il cui contenuto e' informare o
  notificare a un soggetto esterno (art. 25 §5, §8, §9; art. 28 §2; art. 29
  §4; art. 30 §2, §3, §4, §5); "tecnico/sicurezza" per l'art. 27 §1, che e' il
  monitoraggio delle vulnerabilita' e delle dipendenze note del prodotto TIC
  certificato e del livello di affidabilita' del certificato - un controllo di
  sicurezza sul prodotto, non un adempimento documentale; "sanzionatorio" per
  le tre righe che stabiliscono la conseguenza della non conformita' o della
  non compliance (art. 28 §6, art. 29 §2, art. 29 §3): sospensione o revoca del
  certificato EUCC, stessa lettura gia' data nel censimento alla sospensione e
  alla revoca disposte per violazione (SPID art. 10 c.1 lett. e) e art. 12).
  Divergenza dichiarata rispetto ai capitoli gemelli di questa Fonte: il cap02
  classifica "procedurale" la revoca del certificato EUCC (art. 13 §2 e art. 14
  §1) e il cap04 fa lo stesso per la revoca dell'autorizzazione (art. 21 §5 e
  art. 22 §6, che il cap04 stesso segnala come dubbio aperto). Qui le tre righe
  prescrivono la conseguenza della violazione, non un atto di gestione del
  titolo - le rubriche degli articoli 28 e 29 sono "Conseguenze della non
  conformita'" e "Conseguenze della non compliance" - quindi il tipo
  "sanzionatorio" e' sembrato quello pertinente; la lettura alternativa
  ("procedurale", per coerenza con i capitoli gemelli, non essendoci ne'
  sanzione pecuniaria ne' procedimento sanzionatorio) e' dichiarata come dubbio
  di classificazione aperto in chiusura. L'art. 28 §1, che "informa il titolare
  ... e richiede misure correttive", e'
  classificato "procedurale" e non "informativo/trasparenza": l'informazione e'
  un atto interno alla procedura di non conformita' e il comma non persegue la
  trasparenza verso utenti o pubblico. L'art. 31 §2 e' "procedurale" e non
  "sanzionatorio": il comma impone di scegliere fra mantenere inalterato il
  certificato e revocarlo, quindi la decisione, non la sanzione, ne e' il
  contenuto.
- `sanzioni` e' valorizzato solo sulle tre righe "sanzionatorio" (art. 28 §6,
  art. 29 §2, art. 29 §3), con il tipo di conseguenza e il rinvio agli articoli
  che la disciplinano. `severita` non e' valorizzata da nessuna riga: il
  regolamento non gradua la gravita' delle violazioni.
- `condizione_applicabilita` valorizzata dove il comma subordina la propria
  applicabilita' a una circostanza enunciata (art. 25 §7, §9; art. 28 §1, §2,
  §4, §6; art. 29 §1, §2; art. 30 §4, §6; art. 31 §1). Non valorizzata dove il
  comma rinvia a un altro comma ("Al ricevimento delle informazioni di cui al
  paragrafo 1" in art. 28 §3, "Sulla base delle misure di cui al paragrafo 1"
  in art. 31 §2 e §3): quello e' un rinvio tra nodi tracciati, dichiarato come
  relazione, non una condizione su un fatto esterno. Il "Fatto salvo l'articolo
  58, paragrafo 7, del regolamento (UE) 2019/881" dell'art. 25 §1 e' una
  clausola di salvezza a favore di un'altra fonte: non e' una condizione di
  applicabilita' di questa riga ed e' elencata tra i rinvii demandati alla
  fase 6.
- `oggetti_giuridici` non valorizzato per nessuno dei quattro Principi: gli
  oggetti censiti sono quelli dei servizi fiduciari eIDAS (firme, sigilli,
  marche temporali, attestati, portafogli, ...) e il certificato EUCC di un
  prodotto TIC non vi rientra. L'art. 28 §7 (clausola di ambito) e l'art. 25 §7
  (potere di indagine) non si legano ad alcun oggetto giuridico specifico.
- `testo_integrale`: verbatim e integrale, ricucendo le righe spezzate dalla
  conversione XHTML -> testo. In questa porzione ogni comma e' una riga fisica
  del file e ogni lettera e' spezzata in due righe (il marcatore "(a)" da solo
  e poi il testo): il marcatore ufficiale e' stato ricucito al testo della
  lettera ("(a) il rispetto, da parte di ..."), mantenendo le parentesi come
  nel testo ufficiale, e i commi sono separati da riga vuota. Il marcatore
  nudo e i livelli annidati sono conservati come nel testo (art. 27 §1:
  "(a) monitoraggio ... in considerazione di:" seguito da "(1) ..." e
  "(2) ..."). L'intestazione "Articolo N" + rubrica e' premessa alla riga
  "art. N §1" di ciascun articolo, dove il testo ufficiale la precede
  immediatamente: e' ripetuta in tutte e sette le righe "§1" di questo
  capitolo perche' in tutti e sette i casi la rubrica precede il comma 1.
  Nessun marcatore di elisione (vincolo
  `verifica_completezza_testo_integrale`, ADR-0010). `testo` e' invece la
  sintesi compressa (1-3 frasi) di ciascun comma, che nomina anche le
  condizioni e i limiti determinanti (4 % annuo e valutazione dei rischi in
  art. 25 §3; 30 giorni in art. 28 §3 e art. 29 §1; 42 giorni in art. 30 §1;
  un anno in art. 30 §6; l'esclusione delle parti a rischio di sicurezza in
  art. 30 §3; la riserva ai casi di vulnerabilita' in art. 28 §7).
- Unita' di indice: articolo + paragrafo con "§" ("art. 25 §1") e lettera o
  punto tra parentesi ("art. 25 §1(a)", "art. 27 §1(a)(1)"), convenzione gia'
  in uso in questo censimento per gli atti UE (Reg. 2024/2979 "art. 5 §1(a)",
  Reg. 2025/1569 "art. 6 §3(a)"). Le rubriche degli articoli, i titoli di
  capitolo e di sezione non sono item di indice; l'art. 31 §1 e' coperto anche
  dall'item "art. 31 §1" perche' il chapeau, pur nudo di predicato, e' la sede
  della fattispecie ("In caso di mancato rispetto ... qualora sia individuata
  una non compliance") e i rinvii degli art. 31 §2 e §3 puntano a quel
  paragrafo.
- RELAZIONI: solo interne a questo capitolo, tutte con `fonte_id_o_None = None`
  su entrambi gli estremi, tutte rinvii letterali verificati sul
  `testo_integrale` della riga citante, quindi `evidence_type = "textual"`;
  `confidence` resta None perche' non esiste uno score reale da riportare
  (ADR-0005: non va inventato). Sono tredici: art. 25 §2 -> art. 25 §3 ("del
  campionamento effettuato in conformita' del paragrafo 3"); art. 28 §3 ->
  art. 28 §1 ("delle informazioni di cui al paragrafo 1"); art. 28 §6 ->
  art. 28 §3 ("durante il periodo di cui al paragrafo 3") e -> art. 30 §1
  ("sospeso in conformita' dell'articolo 30"); art. 28 §4 -> art. 30 §1 ("in
  conformita' dell'articolo 30"); art. 29 §1 -> art. 27 §1 e -> art. 27 §2
  ("gli impegni e gli obblighi di cui ... agli articoli 27 e 41": i due commi
  dell'art. 27 sono entrambi obblighi del titolare, quindi due archi, come
  l'art. 3 §2 -> art. 6 §1/§2 del Reg. 2024/2979); art. 29 §2 -> art. 29 §1
  ("durante il periodo di cui al paragrafo 1") e -> art. 30 §1 ("in
  conformita' dell'articolo 30"); art. 29 §3 -> art. 29 §1 ("degli obblighi di
  cui al paragrafo 1"); art. 29 §4 -> art. 29 §1 ("le constatazioni di cui al
  paragrafo 1"); art. 31 §2 -> art. 31 §1 e art. 31 §3 -> art. 31 §1 ("le
  misure di cui al paragrafo 1"). Dove il testo cita "l'articolo 30" in blocco
  il bersaglio e' il §1, che e' il comma che disciplina la sospensione (l'art.
  30 §2-§6 ne regola notifica, comunicazione agli acquirenti, informazione
  dell'autorita' di vigilanza, ENISA e proroga): stesso trattamento del rinvio
  "di cui all'articolo 6" nel Reg. 2024/2979. Avvertenza per l'audit
  `verifica_relazioni_textual.py`: le relazioni verso "art. 30 §1" e verso
  "art. 27 §1"/"art. 27 §2" sono rinvii letterali ma a livello di articolo
  ("dell'articolo 30", "agli articoli 27 e 41"); il gate di quello script cerca
  una traccia del riferimento citato e la trova nel numero dell'articolo, non
  in "paragrafo N". Non e' stata dichiarata alcuna relazione inferita: i
  legami sostanziali che il testo non cita sarebbero un giudizio non
  verificabile dal testo.
- Rinvii demandati alla fase 6 (nessuna relazione dichiarata, per istruzione
  del batch: i collegamenti tra capitoli della stessa fonte e verso altre fonti
  li costruisce la sessione principale con ADR-0009). Verso altre fonti:
  regolamento (UE) 2019/881 (Cybersecurity Act) e segnatamente l'articolo 58,
  paragrafo 7 (art. 25 §1) e paragrafo 8 (art. 25 §7), l'articolo 55,
  paragrafo 1, lettera c) (art. 27 §1(a)(1)) e l'articolo 56, paragrafo 8
  (art. 29 §1(b)). Verso altri capitoli di questa fonte, con il capitolo in cui
  il bersaglio e' censito secondo il manifest: allegato IV, sezione IV.2
  (art. 25 §6, cap11); articolo 9, paragrafo 2 (art. 26 §2(a) e art. 26 §3,
  cap02); articolo 17, paragrafo 2 (art. 29 §1(a), cap03); articolo 41
  (art. 29 §1(a), cap07); articoli 13 e 19 (art. 28 §5, cap02 e cap03);
  articoli 14 e 20 (art. 28 §6, art. 29 §2, art. 29 §3, art. 31 §2, cap02 e
  cap03); articolo 42, paragrafo 3 (art. 30 §5, cap07); capo VI (art. 28 §7 e
  art. 29 §1(b), cap06).

Dubbi di classificazione lasciati aperti (segnalati, non risolti in
autonomia):
- art. 28 §6, art. 29 §2, art. 29 §3 -> "sanzionatorio" anziche'
  "procedurale" (motivi e alternativa nella sezione `tipo_obbligo` sopra:
  stesso tipo scelto dal censimento per la sospensione e la revoca disposte
  per violazione in SPID art. 10 c.1 lett. e) e art. 12 e per la revoca in
  CAD art. 32-bis §2). Da riconciliare con i capitoli 2 e 4 di questa Fonte.
- art. 27 §1 -> "tecnico/sicurezza" anziche' "procedurale": il contenuto e'
  un monitoraggio (attivita' continua, non un requisito tecnico puntuale), ma
  l'oggetto e' la sicurezza del prodotto certificato (vulnerabilita',
  dipendenze, livello di affidabilita'), e questa e' la lettura seguita.
- art. 30 §5 -> soggetto obbligato "Terza parte" senza ulteriore
  specificazione: la forma passiva ("La sospensione di un certificato e'
  notificata all'ENISA") non nomina il notificante, che l'articolo 42,
  paragrafo 3 (cap07, fuori da questo modulo) identifica; la categoria
  assegnata copre sia l'ipotesi dell'organismo di certificazione sia quella
  dell'autorita' nazionale.
- art. 30 §6 -> Obbligo e non Principio (facolta' di proroga + limite
  imperativo di un anno): la scelta e' argomentata nella sezione sopra, ma la
  prima meta' del comma e' una mera facolta' e l'alternativa ("altro") resta
  difendibile.

Copertura: 68 item di indice, 34 righe (30 Obblighi + 4 Principi), 13
relazioni interne.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 25 §1",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza controlla il rispetto, da parte dell'organismo di certificazione e dell'ITSEF, degli obblighi loro incombenti a norma del presente regolamento e del regolamento (UE) 2019/881, il rispetto degli stessi obblighi da parte dei titolari di un certificato EUCC, il rispetto dei requisiti stabiliti nell'EUCC da parte dei prodotti TIC certificati e il livello di affidabilità espresso nel certificato EUCC in relazione all'evoluzione del panorama delle minacce.",
        "testo_integrale": "Articolo 25\n\nAttività di monitoraggio da parte dell'autorità nazionale di certificazione della cibersicurezza\n\n1. Fatto salvo l'articolo 58, paragrafo 7, del regolamento (UE) 2019/881, l'autorità nazionale di certificazione della cibersicurezza controlla:\n\n(a) il rispetto, da parte dell'organismo di certificazione e dell'ITSEF, degli obblighi a essi incombenti a norma del presente regolamento e del regolamento (UE) 2019/881;\n\n(b) il rispetto, da parte dei titolari di un certificato EUCC, degli obblighi a essi incombenti a norma del presente regolamento e del regolamento (UE) 2019/881;\n\n(c) il rispetto, da parte dei prodotti TIC certificati, dei requisiti stabiliti nell'EUCC;\n\n(d) il livello di affidabilità espresso nel certificato EUCC in relazione all'evoluzione del panorama delle minacce.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 25 §2",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza svolge le sue attività di monitoraggio in particolare sulla base delle informazioni provenienti dagli organismi di certificazione, dagli organismi nazionali di accreditamento e dalle autorità di vigilanza del mercato competenti, delle informazioni derivanti da audit e indagini propri o di altre autorità, del campionamento effettuato in conformità del paragrafo 3 e dei reclami ricevuti.",
        "testo_integrale": "2. L'autorità nazionale di certificazione della cibersicurezza svolge le sue attività di monitoraggio in particolare sulla base:\n\n(a) delle informazioni provenienti dagli organismi di certificazione, dagli organismi nazionali di accreditamento e dalle autorità di vigilanza del mercato competenti;\n\n(b) delle informazioni derivanti da audit e indagini propri o di altre autorità;\n\n(c) del campionamento effettuato in conformità del paragrafo 3;\n\n(d) dei reclami ricevuti.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 25 §3",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza, in collaborazione con altre autorità di vigilanza del mercato, campiona annualmente almeno il 4 % dei certificati EUCC in base a una valutazione dei rischi; su richiesta e per conto dell'autorità nazionale di certificazione della cibersicurezza competente, gli organismi di certificazione e, se necessario, l'ITSEF assistono tale autorità nel monitoraggio della compliance.",
        "testo_integrale": "3. L'autorità nazionale di certificazione della cibersicurezza, in collaborazione con altre autorità di vigilanza del mercato, campiona annualmente almeno il 4 % dei certificati EUCC, in base a una valutazione dei rischi. Su richiesta e per conto dell'autorità nazionale di certificazione della cibersicurezza competente, gli organismi di certificazione e, se necessario, l'ITSEF assistono tale autorità nel monitoraggio della compliance.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 25 §4",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza seleziona il campione di prodotti TIC certificati da controllare utilizzando criteri oggettivi, tra cui la categoria di prodotti, i livelli di affidabilità dei prodotti, il titolare di un certificato, l'organismo di certificazione e, se del caso, l'ITSEF a cui sono state subappaltate le attività, e qualsiasi altra informazione portata all'attenzione dell'autorità.",
        "testo_integrale": "4. L'autorità nazionale di certificazione della cibersicurezza seleziona il campione di prodotti TIC certificati da controllare utilizzando criteri oggettivi tra cui:\n\n(a) la categoria di prodotti;\n\n(b) i livelli di affidabilità dei prodotti;\n\n(c) il titolare di un certificato;\n\n(d) l'organismo di certificazione e, se del caso, l'ITSEF a cui sono state subappaltate le attività;\n\n(e) qualsiasi altra informazione portata all'attenzione dell'autorità.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 25 §5",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza informa i titolari del certificato EUCC in merito ai prodotti TIC selezionati e ai criteri di selezione.",
        "testo_integrale": "5. L'autorità nazionale di certificazione della cibersicurezza informa i titolari del certificato EUCC in merito ai prodotti TIC selezionati e ai criteri di selezione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 25 §6",
        "testo": "Su richiesta dell'autorità nazionale di certificazione della cibersicurezza, e con l'assistenza della rispettiva ITSEF, l'organismo di certificazione che ha certificato il prodotto TIC oggetto di campionamento procede a un riesame supplementare in conformità della procedura di cui all'allegato IV, sezione IV.2, e informa l'autorità nazionale di certificazione della cibersicurezza in merito ai risultati.",
        "testo_integrale": "6. Su richiesta dell'autorità nazionale di certificazione della cibersicurezza, e con l'assistenza della rispettiva ITSEF, l'organismo di certificazione che ha certificato il prodotto TIC oggetto di campionamento procede a un riesame supplementare in conformità della procedura di cui all'allegato IV, sezione IV.2, e informa l'autorità nazionale di certificazione della cibersicurezza in merito ai risultati.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 25 §8",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza informa l'organismo di certificazione e l'ITSEF in questione delle indagini in corso relative ai prodotti TIC selezionati.",
        "testo_integrale": "8. L'autorità nazionale di certificazione della cibersicurezza informa l'organismo di certificazione e l'ITSEF in questione delle indagini in corso relative ai prodotti TIC selezionati.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 25 §9",
        "testo": "Se rileva che un'indagine in corso riguarda prodotti TIC certificati da organismi di certificazione stabiliti in altri Stati membri, l'autorità nazionale di certificazione della cibersicurezza ne informa le autorità nazionali di certificazione della cibersicurezza degli Stati membri interessati ai fini della collaborazione alle indagini, se del caso; informa inoltre il gruppo europeo per la certificazione della cibersicurezza in merito alle indagini transfrontaliere e ai relativi risultati.",
        "testo_integrale": "9. Se rileva che un'indagine in corso riguarda prodotti TIC certificati da organismi di certificazione stabiliti in altri Stati membri, l'autorità nazionale di certificazione della cibersicurezza ne informa le autorità nazionali di certificazione della cibersicurezza degli Stati membri interessati ai fini della collaborazione alle indagini, se del caso. Tale autorità nazionale di certificazione della cibersicurezza informa inoltre il gruppo europeo per la certificazione della cibersicurezza in merito alle indagini transfrontaliere e ai relativi risultati.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se l'indagine in corso riguarda prodotti TIC certificati da organismi di certificazione stabiliti in altri Stati membri.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 26 §1",
        "testo": "L'organismo di certificazione monitora il rispetto, da parte dei titolari di un certificato, degli obblighi loro incombenti a norma del presente regolamento e del regolamento (UE) 2019/881 per quanto riguarda il certificato EUCC da esso rilasciato, il rispetto dei rispettivi requisiti di sicurezza da parte dei prodotti TIC che ha certificato e il livello di affidabilità espresso nei profili di protezione certificati.",
        "testo_integrale": "Articolo 26\n\nAttività di monitoraggio da parte dell'organismo di certificazione\n\n1. L'organismo di certificazione monitora:\n\n(a) il rispetto, da parte dei titolari di un certificato, degli obblighi a essi incombenti a norma del presente regolamento e del regolamento (UE) 2019/881 per quanto riguarda il certificato EUCC rilasciato dall'organismo di certificazione;\n\n(b) il rispetto, da parte dei prodotti TIC che ha certificato, dei rispettivi requisiti di sicurezza;\n\n(c) il livello di affidabilità espresso nei profili di protezione certificati.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 26 §2",
        "testo": "L'organismo di certificazione svolge le proprie attività di monitoraggio sulla base delle informazioni fornite in base agli impegni del richiedente la certificazione di cui all'articolo 9, paragrafo 2, delle informazioni derivanti dalle attività di altre autorità di vigilanza del mercato competenti, dei reclami ricevuti e delle informazioni sulle vulnerabilità che potrebbero avere un impatto sui prodotti TIC che ha certificato.",
        "testo_integrale": "2. L'organismo di certificazione svolge le proprie attività di monitoraggio sulla base:\n\n(a) delle informazioni fornite in base agli impegni del richiedente la certificazione di cui all'articolo 9, paragrafo 2;\n\n(b) delle informazioni derivanti dalle attività di altre autorità di vigilanza del mercato competenti;\n\n(c) dei reclami ricevuti;\n\n(d) delle informazioni sulle vulnerabilità che potrebbero avere un impatto sui prodotti TIC che ha certificato.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 27 §1",
        "testo": "Al fine di monitorare la conformità del prodotto TIC certificato ai suoi requisiti di sicurezza, il titolare di un certificato EUCC monitora le informazioni sulle vulnerabilità relative al prodotto TIC certificato, comprese le dipendenze note, con mezzi propri e anche in considerazione della pubblicazione o presentazione di informazioni sulle vulnerabilità da parte di un utente o di un ricercatore nel settore della sicurezza di cui all'articolo 55, paragrafo 1, lettera c), del regolamento (UE) 2019/881 e delle informazioni presentate da qualsiasi altra fonte, e monitora il livello di affidabilità espresso nel certificato EUCC.",
        "testo_integrale": "Articolo 27\n\nAttività di monitoraggio da parte del titolare del certificato\n\n1. Al fine di monitorare la conformità del prodotto TIC certificato ai suoi requisiti di sicurezza, il titolare di un certificato EUCC svolge i compiti seguenti:\n\n(a) monitoraggio delle informazioni sulle vulnerabilità relative al prodotto TIC certificato, comprese le dipendenze note, con mezzi propri ma anche in considerazione di:\n\n(1) una pubblicazione o una presentazione di informazioni sulle vulnerabilità da parte di un utente o di un ricercatore nel settore della sicurezza di cui all'articolo 55, paragrafo 1, lettera c), del regolamento (UE) 2019/881;\n\n(2) informazioni presentate da qualsiasi altra fonte;\n\n(b) monitoraggio del livello di affidabilità espresso nel certificato EUCC.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 27 §2",
        "testo": "Il titolare di un certificato EUCC collabora con l'organismo di certificazione, l'ITSEF e, se del caso, l'autorità nazionale di certificazione della cibersicurezza per sostenere le loro attività di monitoraggio.",
        "testo_integrale": "2. Il titolare di un certificato EUCC collabora con l'organismo di certificazione, l'ITSEF e, se del caso, l'autorità nazionale di certificazione della cibersicurezza per sostenere le loro attività di monitoraggio.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 28 §1",
        "testo": "Se un prodotto TIC certificato o un profilo di protezione certificato non è conforme ai requisiti stabiliti nel presente regolamento e nel regolamento (UE) 2019/881, l'organismo di certificazione informa il titolare del certificato EUCC della non conformità individuata e richiede misure correttive.",
        "testo_integrale": "Articolo 28\n\nConseguenze della non conformità di un prodotto TIC certificato o di un profilo di protezione\n\n1. Se un prodotto TIC certificato o un profilo di protezione certificato non è conforme ai requisiti stabiliti nel presente regolamento e nel regolamento (UE) 2019/881, l'organismo di certificazione informa il titolare del certificato EUCC della non conformità individuata e richiede misure correttive.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se un prodotto TIC certificato o un profilo di protezione certificato non è conforme ai requisiti stabiliti nel presente regolamento e nel regolamento (UE) 2019/881.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 28 §2",
        "testo": "Qualora un caso di non conformità alle disposizioni del presente regolamento possa influire sul rispetto di altre normative pertinenti dell'Unione che prevedono la possibilità di dimostrare la presunzione di conformità ai requisiti imposti da tali atti giuridici utilizzando il certificato EUCC, l'organismo di certificazione ne informa senza indugio l'autorità nazionale di certificazione della cibersicurezza e questa notifica immediatamente il caso all'autorità di vigilanza del mercato responsabile di tali altre normative dell'Unione.",
        "testo_integrale": "2. Qualora un caso di non conformità alle disposizioni del presente regolamento possa influire sul rispetto di altre normative pertinenti dell'Unione, che prevedono la possibilità di dimostrare la presunzione di conformità ai requisiti imposti da tali atti giuridici utilizzando il certificato EUCC, l'organismo di certificazione ne informa senza indugio l'autorità nazionale di certificazione della cibersicurezza. L'autorità nazionale di certificazione della cibersicurezza notifica immediatamente il caso di non conformità individuato all'autorità di vigilanza del mercato responsabile di tali altre normative pertinenti dell'Unione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica qualora un caso di non conformità alle disposizioni del presente regolamento possa influire sul rispetto di altre normative pertinenti dell'Unione che prevedono la possibilità di dimostrare la presunzione di conformità ai requisiti imposti da tali atti giuridici utilizzando il certificato EUCC.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 28 §3",
        "testo": "Al ricevimento delle informazioni di cui al paragrafo 1, il titolare del certificato EUCC propone all'organismo di certificazione, entro il termine stabilito da quest'ultimo e che non può superare i 30 giorni, la misura correttiva necessaria per sanare la non conformità.",
        "testo_integrale": "3. Al ricevimento delle informazioni di cui al paragrafo 1 il titolare del certificato EUCC propone all'organismo di certificazione, entro il termine stabilito da quest'ultimo, che non può superare i 30 giorni, la misura correttiva necessaria per sanare la non conformità.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 28 §5",
        "testo": "L'organismo di certificazione effettua un riesame in conformità degli articoli 13 e 19, valutando se la misura correttiva sani la non conformità.",
        "testo_integrale": "5. L'organismo di certificazione effettua un riesame in conformità degli articoli 13 e 19, valutando se la misura correttiva sani la non conformità.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 28 §6",
        "testo": "Se il titolare del certificato EUCC non propone una misura correttiva adeguata durante il periodo di cui al paragrafo 3, il certificato è sospeso in conformità dell'articolo 30 o revocato in conformità dell'articolo 14 o 20.",
        "testo_integrale": "6. Se il titolare del certificato EUCC non propone una misura correttiva adeguata durante il periodo di cui al paragrafo 3, il certificato è sospeso in conformità dell'articolo 30 o revocato in conformità dell'articolo 14 o 20.",
        "tipo_obbligo": "sanzionatorio",
        "stato": "vigente",
        "sanzioni": "Sospensione del certificato EUCC in conformità dell'articolo 30 oppure revoca in conformità dell'articolo 14 o 20, se il titolare del certificato non propone una misura correttiva adeguata nel termine di cui all'articolo 28, paragrafo 3.",
        "condizione_applicabilita": "Si applica se il titolare del certificato EUCC non propone una misura correttiva adeguata durante il periodo di cui all'articolo 28, paragrafo 3.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 29 §1",
        "testo": "Se constata che il titolare del certificato EUCC o il richiedente la certificazione non rispettano gli impegni e gli obblighi di cui all'articolo 9, paragrafo 2, all'articolo 17, paragrafo 2, e agli articoli 27 e 41, oppure che il titolare del certificato EUCC non rispetta quanto stabilito dall'articolo 56, paragrafo 8, del regolamento (UE) 2019/881 o dal capo VI del presente regolamento, l'organismo di certificazione fissa un termine non superiore a 30 giorni entro il quale il titolare del certificato EUCC adotta misure correttive.",
        "testo_integrale": "Articolo 29\n\nConseguenze della non compliance da parte del titolare del certificato\n\n1. Se constata che:\n\n(a) il titolare del certificato EUCC o il richiedente la certificazione non rispettano gli impegni e gli obblighi di cui all'articolo 9, paragrafo 2, all'articolo 17, paragrafo 2, e agli articoli 27 e 41; oppure\n\n(b) il titolare del certificato EUCC non rispetta quanto stabilito dall'articolo 56, paragrafo 8, del regolamento (UE) 2019/881 o dal capo VI del presente regolamento,\n\nl'organismo di certificazione fissa un termine non superiore a 30 giorni entro il quale il titolare del certificato EUCC adotta misure correttive.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se l'organismo di certificazione constata che il titolare del certificato EUCC o il richiedente la certificazione non rispettano gli impegni e gli obblighi di cui all'articolo 9, paragrafo 2, all'articolo 17, paragrafo 2, e agli articoli 27 e 41, oppure che il titolare non rispetta quanto stabilito dall'articolo 56, paragrafo 8, del regolamento (UE) 2019/881 o dal capo VI del presente regolamento.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 29 §2",
        "testo": "Se il titolare del certificato EUCC non propone misure correttive adeguate durante il periodo di cui al paragrafo 1, il certificato è sospeso in conformità dell'articolo 30 o revocato in conformità degli articoli 14 e 20.",
        "testo_integrale": "2. Se il titolare del certificato EUCC non propone misure correttive adeguate durante il periodo di cui al paragrafo 1, il certificato è sospeso in conformità dell'articolo 30 o revocato in conformità degli articoli 14 e 20.",
        "tipo_obbligo": "sanzionatorio",
        "stato": "vigente",
        "sanzioni": "Sospensione del certificato EUCC in conformità dell'articolo 30 o revoca in conformità degli articoli 14 e 20, se il titolare del certificato non propone misure correttive adeguate nel termine di cui all'articolo 29, paragrafo 1.",
        "condizione_applicabilita": "Si applica se il titolare del certificato EUCC non propone misure correttive adeguate durante il periodo di cui all'articolo 29, paragrafo 1.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 29 §3",
        "testo": "La violazione continuata o ricorrente da parte del titolare del certificato EUCC degli obblighi di cui al paragrafo 1 fa scattare la revoca del certificato EUCC in conformità dell'articolo 14 o dell'articolo 20.",
        "testo_integrale": "3. La violazione continuata o ricorrente da parte del titolare del certificato EUCC degli obblighi di cui al paragrafo 1 fa scattare la revoca del certificato EUCC in conformità dell'articolo 14 o dell'articolo 20.",
        "tipo_obbligo": "sanzionatorio",
        "stato": "vigente",
        "sanzioni": "Revoca del certificato EUCC in conformità dell'articolo 14 o dell'articolo 20 in caso di violazione continuata o ricorrente degli obblighi di cui all'articolo 29, paragrafo 1.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 29 §4",
        "testo": "L'organismo di certificazione informa l'autorità nazionale di certificazione della cibersicurezza in merito alle constatazioni di cui al paragrafo 1; se il caso di non compliance incide sul rispetto di altre normative pertinenti dell'Unione, l'autorità nazionale di certificazione della cibersicurezza notifica immediatamente all'autorità di vigilanza del mercato responsabile di tali altre normative il caso di non compliance individuato.",
        "testo_integrale": "4. L'organismo di certificazione informa l'autorità nazionale di certificazione della cibersicurezza in merito alle constatazioni di cui al paragrafo 1. Se il caso di non compliance incide sul rispetto di altre normative pertinenti dell'Unione, l'autorità nazionale di certificazione della cibersicurezza notifica immediatamente all'autorità di vigilanza del mercato responsabile di tali altre normative il caso di non compliance individuato.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "La notifica all'autorità di vigilanza del mercato si applica se il caso di non compliance incide sul rispetto di altre normative pertinenti dell'Unione.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 30 §1",
        "testo": "Laddove il presente regolamento faccia riferimento alla sospensione di un certificato EUCC, l'organismo di certificazione sospende il certificato EUCC in questione per un periodo adeguato alle circostanze che hanno determinato la sospensione, che non supera i 42 giorni e decorre dal giorno successivo a quello in cui l'organismo di certificazione ha adottato la decisione; la sospensione non pregiudica la validità del certificato.",
        "testo_integrale": "Articolo 30\n\nSospensione del certificato EUCC\n\n1. Laddove il presente regolamento faccia riferimento alla sospensione di un certificato EUCC, l'organismo di certificazione sospende il certificato EUCC in questione per un periodo adeguato alle circostanze che hanno determinato la sospensione, che non supera i 42 giorni. Il periodo di sospensione decorre dal giorno successivo a quello in cui l'organismo di certificazione ha adottato la decisione. La sospensione non pregiudica la validità del certificato.",
        "tipo_obbligo": "sanzionatorio",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 30 §2",
        "testo": "L'organismo di certificazione notifica la sospensione al titolare del certificato e all'autorità nazionale di certificazione della cibersicurezza senza indebito ritardo e indica i motivi della sospensione, le misure da intraprendere e il periodo di sospensione.",
        "testo_integrale": "2. L'organismo di certificazione notifica la sospensione al titolare del certificato e all'autorità nazionale di certificazione della cibersicurezza senza indebito ritardo e indica i motivi della sospensione, le misure da intraprendere e il periodo di sospensione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 30 §3",
        "testo": "I titolari della certificazione informano gli acquirenti dei prodotti TIC in questione in merito alla sospensione e alla relativa motivazione fornita dall'organismo di certificazione, ad eccezione di quelle parti la cui condivisione costituirebbe un rischio per la sicurezza o che contengono informazioni sensibili; tali informazioni sono rese pubbliche anche dal titolare del certificato.",
        "testo_integrale": "3. I titolari della certificazione informano gli acquirenti dei prodotti TIC in questione in merito alla sospensione e alla relativa motivazione fornita dall'organismo di certificazione, ad eccezione di quelle parti la cui condivisione costituirebbe un rischio per la sicurezza o che contengono informazioni sensibili. Tali informazioni sono rese pubbliche anche dal titolare del certificato.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 30 §4",
        "testo": "Qualora altre normative pertinenti dell'Unione prevedano una presunzione di conformità basata su certificati rilasciati a norma delle disposizioni del presente regolamento, l'autorità nazionale di certificazione della cibersicurezza informa l'autorità di vigilanza del mercato responsabile di tali normative in merito alla sospensione.",
        "testo_integrale": "4. Qualora altre normative pertinenti dell'Unione prevedano una presunzione di conformità basata su certificati rilasciati a norma delle disposizioni del presente regolamento, l'autorità nazionale di certificazione della cibersicurezza informa l'autorità di vigilanza del mercato responsabile di tali normative in merito alla sospensione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica qualora altre normative pertinenti dell'Unione prevedano una presunzione di conformità basata su certificati rilasciati a norma delle disposizioni del presente regolamento.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 30 §5",
        "testo": "La sospensione di un certificato è notificata all'ENISA in conformità dell'articolo 42, paragrafo 3.",
        "testo_integrale": "5. La sospensione di un certificato è notificata all'ENISA in conformità dell'articolo 42, paragrafo 3.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 30 §6",
        "testo": "In casi debitamente giustificati l'autorità nazionale di certificazione della cibersicurezza può autorizzare una proroga del periodo di sospensione di un certificato EUCC, ma il periodo complessivo di sospensione non può superare un anno.",
        "testo_integrale": "6. In casi debitamente giustificati l'autorità nazionale di certificazione della cibersicurezza può autorizzare una proroga del periodo di sospensione di un certificato EUCC. Il periodo complessivo di sospensione non può superare un anno.",
        "tipo_obbligo": "sanzionatorio",
        "stato": "vigente",
        "condizione_applicabilita": "La proroga si applica in casi debitamente giustificati; il periodo complessivo di sospensione non può in ogni caso superare un anno.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 31 §1",
        "testo": "In caso di mancato rispetto dei propri obblighi da parte di un organismo di certificazione o da parte dell'organismo di certificazione competente, qualora sia individuata una non compliance da parte di un'ITSEF, l'autorità nazionale di certificazione della cibersicurezza, senza indebito ritardo, identifica con il sostegno dell'ITSEF in questione i certificati EUCC potenzialmente interessati, richiede se necessario l'esecuzione di attività di valutazione su uno o più prodotti TIC o profili di protezione da parte dell'ITSEF che ha effettuato la valutazione o di qualsiasi altra ITSEF accreditata e autorizzata che possa trovarsi in una posizione tecnica migliore, analizza gli impatti della non compliance e informa il titolare del certificato EUCC interessato.",
        "testo_integrale": "Articolo 31\n\nConseguenze della non compliance da parte dell'organismo di valutazione della conformità\n\n1. In caso di mancato rispetto dei propri obblighi da parte di un organismo di certificazione o da parte dell'organismo di certificazione competente, qualora sia individuata una non compliance da parte di un'ITSEF, l'autorità nazionale di certificazione della cibersicurezza, senza indebito ritardo:\n\n(a) identifica con il sostegno dell'ITSEF in questione i certificati EUCC potenzialmente interessati;\n\n(b) richiede, se necessario, l'esecuzione di attività di valutazione su uno o più prodotti TIC o profili di protezione da parte dell'ITSEF che ha effettuato la valutazione o di qualsiasi altra ITSEF accreditata e, se del caso, autorizzata che possa trovarsi in una posizione tecnica migliore per sostenere tale identificazione;\n\n(c) analizza gli impatti della non compliance;\n\n(d) informa il titolare del certificato EUCC interessato dalla non compliance.",
        "tipo_obbligo": "sanzionatorio",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica in caso di mancato rispetto dei propri obblighi da parte di un organismo di certificazione o dell'organismo di certificazione competente e qualora sia individuata una non compliance da parte di un'ITSEF.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 31 §2",
        "testo": "Sulla base delle misure di cui al paragrafo 1, l'organismo di certificazione adotta, in relazione a ciascun certificato EUCC interessato, la decisione di mantenere il certificato EUCC inalterato oppure di revocarlo in conformità dell'articolo 14 o dell'articolo 20 e, se del caso, di rilasciare un nuovo certificato EUCC.",
        "testo_integrale": "2. Sulla base delle misure di cui al paragrafo 1, l'organismo di certificazione adotta, in relazione a ciascun certificato EUCC interessato, una delle decisioni indicate di seguito:\n\n(a) mantenere il certificato EUCC inalterato;\n\n(b) revocare il certificato EUCC in conformità dell'articolo 14 o dell'articolo 20 e, se del caso, rilasciare un nuovo certificato EUCC.",
        "tipo_obbligo": "sanzionatorio",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 31 §3",
        "testo": "Sulla base delle misure di cui al paragrafo 1, l'autorità nazionale di certificazione della cibersicurezza segnala, se necessario, la non compliance dell'organismo di certificazione o della relativa ITSEF all'organismo nazionale di accreditamento e valuta, se del caso, il potenziale impatto sull'autorizzazione.",
        "testo_integrale": "3. Sulla base delle misure di cui al paragrafo 1 l'autorità nazionale di certificazione della cibersicurezza:\n\n(a) segnala, se necessario, la non compliance dell'organismo di certificazione o della relativa ITSEF all'organismo nazionale di accreditamento;\n\n(b) valuta, se del caso, il potenziale impatto sull'autorizzazione.",
        "tipo_obbligo": "sanzionatorio",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 25 §7",
        "testo": "Qualora abbia motivi sufficienti per ritenere che un prodotto TIC certificato non sia più conforme al presente regolamento o al regolamento (UE) 2019/881, l'autorità nazionale di certificazione della cibersicurezza può svolgere indagini o avvalersi di qualsiasi altro potere di monitoraggio di cui all'articolo 58, paragrafo 8, del regolamento (UE) 2019/881: è un potere conferito all'autorità, non un comportamento imposto.",
        "testo_integrale": "7. Qualora abbia motivi sufficienti per ritenere che un prodotto TIC certificato non sia più conforme al presente regolamento o al regolamento (UE) 2019/881, l'autorità nazionale di certificazione della cibersicurezza può svolgere indagini o avvalersi di qualsiasi altro potere di monitoraggio di cui all'articolo 58, paragrafo 8, del regolamento (UE) 2019/881.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica qualora l'autorità abbia motivi sufficienti per ritenere che un prodotto TIC certificato non sia più conforme al presente regolamento o al regolamento (UE) 2019/881.",
    },
    {
        "riferimento": "art. 26 §3",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza può elaborare norme volte a promuovere un dialogo periodico tra gli organismi di certificazione e i titolari di certificati EUCC al fine di verificare il rispetto degli impegni assunti a norma dell'articolo 9, paragrafo 2, e riferire in merito, fatte salve le attività connesse ad altre autorità di vigilanza del mercato competenti: è una facoltà, non un comportamento imposto.",
        "testo_integrale": "3. L'autorità nazionale di certificazione della cibersicurezza può elaborare norme volte a promuovere un dialogo periodico tra gli organismi di certificazione e i titolari di certificati EUCC al fine di verificare il rispetto degli impegni assunti a norma dell'articolo 9, paragrafo 2, e riferire in merito, fatte salve le attività connesse ad altre autorità di vigilanza del mercato competenti.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 28 §4",
        "testo": "L'organismo di certificazione può sospendere senza indebito ritardo il certificato EUCC in conformità dell'articolo 30 in caso di emergenza o se il titolare del certificato EUCC non collabora debitamente con l'organismo di certificazione: è una facoltà conferita all'organismo di certificazione, non un comportamento imposto.",
        "testo_integrale": "4. L'organismo di certificazione può sospendere senza indebito ritardo il certificato EUCC in conformità dell'articolo 30 in caso di emergenza o se il titolare del certificato EUCC non collabora debitamente con l'organismo di certificazione.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica in caso di emergenza o se il titolare del certificato EUCC non collabora debitamente con l'organismo di certificazione.",
    },
    {
        "riferimento": "art. 28 §7",
        "testo": "Il presente articolo non si applica ai casi di vulnerabilità che interessano un prodotto TIC certificato: tali casi sono trattati in conformità del capo VI. È una clausola di delimitazione dell'ambito di applicazione dell'articolo 28, non un precetto.",
        "testo_integrale": "7. Il presente articolo non si applica ai casi di vulnerabilità che interessano un prodotto TIC certificato, che saranno trattati in conformità del capo VI.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 25 §1",
    "art. 25 §1(a)",
    "art. 25 §1(b)",
    "art. 25 §1(c)",
    "art. 25 §1(d)",
    "art. 25 §2",
    "art. 25 §2(a)",
    "art. 25 §2(b)",
    "art. 25 §2(c)",
    "art. 25 §2(d)",
    "art. 25 §3",
    "art. 25 §4",
    "art. 25 §4(a)",
    "art. 25 §4(b)",
    "art. 25 §4(c)",
    "art. 25 §4(d)",
    "art. 25 §4(e)",
    "art. 25 §5",
    "art. 25 §6",
    "art. 25 §7",
    "art. 25 §8",
    "art. 25 §9",
    "art. 26 §1",
    "art. 26 §1(a)",
    "art. 26 §1(b)",
    "art. 26 §1(c)",
    "art. 26 §2",
    "art. 26 §2(a)",
    "art. 26 §2(b)",
    "art. 26 §2(c)",
    "art. 26 §2(d)",
    "art. 26 §3",
    "art. 27 §1",
    "art. 27 §1(a)",
    "art. 27 §1(a)(1)",
    "art. 27 §1(a)(2)",
    "art. 27 §1(b)",
    "art. 27 §2",
    "art. 28 §1",
    "art. 28 §2",
    "art. 28 §3",
    "art. 28 §4",
    "art. 28 §5",
    "art. 28 §6",
    "art. 28 §7",
    "art. 29 §1",
    "art. 29 §1(a)",
    "art. 29 §1(b)",
    "art. 29 §2",
    "art. 29 §3",
    "art. 29 §4",
    "art. 30 §1",
    "art. 30 §2",
    "art. 30 §3",
    "art. 30 §4",
    "art. 30 §5",
    "art. 30 §6",
    "art. 31 §1",
    "art. 31 §1(a)",
    "art. 31 §1(b)",
    "art. 31 §1(c)",
    "art. 31 §1(d)",
    "art. 31 §2",
    "art. 31 §2(a)",
    "art. 31 §2(b)",
    "art. 31 §3",
    "art. 31 §3(a)",
    "art. 31 §3(b)",
]

# Ogni riga copre il proprio comma per intero, lettere comprese (vedi la
# docstring: un comma = una riga): per questo le lettere sono mappate al
# riferimento del comma e non a un item proprio.
MAPPATURA_LOCALE = {
    "art. 25 §1": ["art. 25 §1", "art. 25 §1(a)", "art. 25 §1(b)", "art. 25 §1(c)", "art. 25 §1(d)"],
    "art. 25 §2": ["art. 25 §2", "art. 25 §2(a)", "art. 25 §2(b)", "art. 25 §2(c)", "art. 25 §2(d)"],
    "art. 25 §3": ["art. 25 §3"],
    "art. 25 §4": ["art. 25 §4", "art. 25 §4(a)", "art. 25 §4(b)", "art. 25 §4(c)", "art. 25 §4(d)", "art. 25 §4(e)"],
    "art. 25 §5": ["art. 25 §5"],
    "art. 25 §6": ["art. 25 §6"],
    "art. 25 §7": ["art. 25 §7"],
    "art. 25 §8": ["art. 25 §8"],
    "art. 25 §9": ["art. 25 §9"],
    "art. 26 §1": ["art. 26 §1", "art. 26 §1(a)", "art. 26 §1(b)", "art. 26 §1(c)"],
    "art. 26 §2": ["art. 26 §2", "art. 26 §2(a)", "art. 26 §2(b)", "art. 26 §2(c)", "art. 26 §2(d)"],
    "art. 26 §3": ["art. 26 §3"],
    "art. 27 §1": ["art. 27 §1", "art. 27 §1(a)", "art. 27 §1(a)(1)", "art. 27 §1(a)(2)", "art. 27 §1(b)"],
    "art. 27 §2": ["art. 27 §2"],
    "art. 28 §1": ["art. 28 §1"],
    "art. 28 §2": ["art. 28 §2"],
    "art. 28 §3": ["art. 28 §3"],
    "art. 28 §4": ["art. 28 §4"],
    "art. 28 §5": ["art. 28 §5"],
    "art. 28 §6": ["art. 28 §6"],
    "art. 28 §7": ["art. 28 §7"],
    "art. 29 §1": ["art. 29 §1", "art. 29 §1(a)", "art. 29 §1(b)"],
    "art. 29 §2": ["art. 29 §2"],
    "art. 29 §3": ["art. 29 §3"],
    "art. 29 §4": ["art. 29 §4"],
    "art. 30 §1": ["art. 30 §1"],
    "art. 30 §2": ["art. 30 §2"],
    "art. 30 §3": ["art. 30 §3"],
    "art. 30 §4": ["art. 30 §4"],
    "art. 30 §5": ["art. 30 §5"],
    "art. 30 §6": ["art. 30 §6"],
    "art. 31 §1": ["art. 31 §1", "art. 31 §1(a)", "art. 31 §1(b)", "art. 31 §1(c)", "art. 31 §1(d)"],
    "art. 31 §2": ["art. 31 §2", "art. 31 §2(a)", "art. 31 §2(b)"],
    "art. 31 §3": ["art. 31 §3", "art. 31 §3(a)", "art. 31 §3(b)"],
}

# Relazioni interne a questa Fonte (fonte_id_o_None = None su entrambi gli
# estremi), tutte rinvii letterali verificati sul `testo_integrale` della riga
# citante: art. 25 §2 cita "del campionamento effettuato in conformità del
# paragrafo 3"; art. 28 §3 cita "delle informazioni di cui al paragrafo 1";
# art. 28 §4 e art. 28 §6 citano "in conformità dell'articolo 30" (bersaglio il
# §1, il comma che disciplina la sospensione); art. 28 §6 cita anche "durante il
# periodo di cui al paragrafo 3"; art. 29 §1 cita "gli impegni e gli obblighi di
# cui ... agli articoli 27 e 41" (i due commi dell'art. 27 sono entrambi
# obblighi del titolare del certificato); art. 29 §2 cita "durante il periodo di
# cui al paragrafo 1" e "in conformità dell'articolo 30"; art. 29 §3 cita "degli
# obblighi di cui al paragrafo 1"; art. 29 §4 cita "le constatazioni di cui al
# paragrafo 1"; art. 31 §2 e art. 31 §3 citano "le misure di cui al paragrafo
# 1". I rinvii ad altri capitoli di questa fonte (allegato IV sezione IV.2,
# artt. 9, 13, 14, 17, 19, 20, 41, 42, capo VI) e ad altre fonti (regolamento
# (UE) 2019/881) non sono dichiarati qui: sono collegamenti demandati alla
# sessione principale (fase ADR-0009), elencati nella docstring. `confidence` =
# None: nessuno score reale da riportare.
RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "art. 25 §2"),
        "nodo_a": ("obbligo", None, "art. 25 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §3"),
        "nodo_a": ("obbligo", None, "art. 28 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §6"),
        "nodo_a": ("obbligo", None, "art. 28 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 28 §6"),
        "nodo_a": ("obbligo", None, "art. 30 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "art. 28 §4"),
        "nodo_a": ("obbligo", None, "art. 30 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §1"),
        "nodo_a": ("obbligo", None, "art. 27 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §1"),
        "nodo_a": ("obbligo", None, "art. 27 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §2"),
        "nodo_a": ("obbligo", None, "art. 29 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §2"),
        "nodo_a": ("obbligo", None, "art. 30 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §3"),
        "nodo_a": ("obbligo", None, "art. 29 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 29 §4"),
        "nodo_a": ("obbligo", None, "art. 29 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 31 §2"),
        "nodo_a": ("obbligo", None, "art. 31 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 31 §3"),
        "nodo_a": ("obbligo", None, "art. 31 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
