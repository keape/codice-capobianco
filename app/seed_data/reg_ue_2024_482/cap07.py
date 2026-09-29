"""Regolamento di esecuzione (UE) 2024/482 della Commissione, del 31 gennaio
2024 - sistema europeo di certificazione della cibersicurezza basato sui
criteri comuni (EUCC), modalita' di applicazione del regolamento (UE) 2019/881.
Fonte 29 (`reg_ue_2024_482`), capitolo 7 di 14 (elenco completo in
app/.source_cache/reg_ue_2024_482/manifest.json): Capo VII - Conservazione,
divulgazione e protezione delle informazioni, articoli 40-43. Il capitolo non
ha sezioni interne (a differenza dei capi II, V e VI). Gli artt. 1-39 sono nei
cap01-cap06, gli artt. 44-50 nel cap08 e gli allegati I-IX nei cap09-cap14,
assegnati ad altri moduli: nessuno di quei file e' toccato qui. La porzione
assegnata comincia con l'intestazione "CAPO VII" e finisce con l'art. 43,
ultimo articolo prima del Capo VIII: non contiene percio' ne' l'epigrafe ne' la
formula di chiusura dell'atto, che stanno nel cap08.

Provenienza del testo: app/.source_cache/reg_ue_2024_482/cap07.txt, estratto
dal raw.txt acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R0482, lingua italiana; URL
risolto .../cellar/687c0d05-c580-11ee-95d9-01aa75ed71a1.0014.03/DOC_1, XHTML
della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 540.435 byte
scaricati, 135.367 caratteri di testo, sha256 del raw.txt
b46d08cab6d63b2c190ae767042c07c1fc324955c22ef491eb314556b28ca5b8 - dettagli
completi in app/.source_cache/reg_ue_2024_482/provenance.json). Il preambolo
(considerando) e' a monte del Capo I e non e' in questa porzione.

Paratesto escluso (nessun nodo, nessun item di indice):
- le intestazioni strutturali "CAPO VII" / "CONSERVAZIONE, DIVULGAZIONE E
  PROTEZIONE DELLE INFORMAZIONI": sono la partizione dell'atto, non
  disposizioni, e non hanno articoli propri che le coprano;
- le intestazioni "Articolo N" + rubrica dei quattro articoli non producono
  righe proprie ne' item propri: restano nel `testo_integrale` della prima
  riga di ciascun articolo, dove il testo ufficiale le premette immediatamente
  al primo comma (stessa convenzione del cap02 e del cap05 di questa Fonte);
- in questa porzione non compaiono epigrafe, firma, note a pie' di pagina,
  formula di chiusura ne' riga ELI (sono tutte nel cap08), quindi non c'e'
  nulla da escludere a quel titolo. Nessun nodo valorizza `severita` o
  `sanzioni`: il regolamento non gradua i requisiti ne' stabilisce sanzioni
  proprie (le sanzioni del sistema EUCC discendono dal regolamento (UE)
  2019/881 e dal diritto nazionale, come gia' dichiarato nei cap02-cap06 di
  questa Fonte).

Unita' di copertura e scelta della grana. Regola applicata: un comma = una
riga; le lettere di un comma ricevono un item di indice proprio, mappato alla
riga del comma (come negli altri capitoli di questa Fonte). Gli artt. 40, 41 e 42
hanno i commi numerati; l'art. 43 e' un unico periodo non numerato e riceve il
riferimento "art. 43". Casi specifici:
- art. 41 §2 -> UNA SOLA riga con tre item ("art. 41 §2", "art. 41 §2(a)",
  "art. 41 §2(b)"): il chapeau porta il predicato e la sua protasi ("Il titolare
  di un certificato EUCC archivia in modo sicuro per il periodo ...:"), le due
  lettere sono i due oggetti dell'archiviazione (i registri delle informazioni
  fornite durante la certificazione, un esemplare del prodotto TIC certificato)
  retti dal medesimo predicato, senza verbo proprio e senza soggetto diverso:
  nessuna delle due e' autonomamente azionabile senza il chapeau che nomina il
  titolare obbligato e il termine di conservazione.
- art. 42 §1 -> UNA SOLA riga con nove item ("art. 42 §1", "art. 42 §1(a)" ...
  "art. 42 §1(h)"): il chapeau ("L'ENISA pubblica sul sito web ... le
  informazioni seguenti:") e' l'unico precetto, e le otto lettere sono
  l'elenco chiuso delle informazioni pubblicate, tutte sullo stesso soggetto
  e rivolte allo stesso pubblico (il sito web pubblico di cui all'art. 50 §1
  del regolamento (UE) 2019/881); nessuna lettera ha un verbo proprio e nessun
  destinatario e' stato valorizzato, perche' il testo non lo nomina
  (convenzione del cap02). Stessa struttura dell'art. 5 §1 del Reg. 2024/2979 e
  dell'art. 4 §3 del Reg. 2025/1569, gia' censiti come riga unica con item
  per lettera.
- art. 40 §2, art. 41 §3 e art. 43 contengono piu' periodi dentro un solo
  comma/paragrafo: restano una riga ciascuno (il periodo aggiuntivo di
  art. 40 §2 e di art. 41 §3 e' lo stesso precetto di conservazione esteso al
  caso del nuovo certificato, non una seconda disposizione autonoma; i tre
  periodi di art. 43 concorrono all'unico precetto "garantiscono ... e
  adottano le misure tecniche e organizzative").

Criterio Obbligo/Principio. Obbligo = comma che impone un comportamento a un
soggetto identificabile, anche quando e' formulato in forma passiva
(convenzione dichiarata dal cap02 di questa Fonte, che censisce come Obblighi
i commi passivi in cui il soggetto obbligato si ricava dal contesto).
Applicato comma per comma, TUTTI gli undici commi di questo capitolo sono
Obblighi e RIGHE_PRINCIPI = [] (come nel cap04 di questa Fonte): il capo non
contiene facolta', poteri discrezionali, clausole di ambito, definizioni ne'
effetti giuridici dichiarati, solo prescrizioni di tenuta, archiviazione,
messa a disposizione e protezione delle informazioni. Nessun comma e' stato
declassato a Principio perche' le uniche formulazioni passive (art. 41 §1,
art. 42 §2) hanno un soggetto ricavabile dal contesto immediato (l'articolo in
cui stanno e il suo titolo) e il precetto e' verificabile.
- art. 41 §1 -> Obbligo "informativo/trasparenza" e non Principio: la frase e'
  passiva ("sono disponibili"), ma la rubrica dell'articolo nomina il soggetto
  dell'articolo ("Informazioni messe a disposizione dal titolare di un
  certificato") e l'art. 55 del regolamento (UE) 2019/881, che il comma
  richiama, e' la disposizione che impone al titolare di rendere pubbliche
  quelle informazioni; il comma aggiunge un requisito di linguaggio
  comprensibile agli utenti, cioe' una modalita' del comportamento di
  divulgazione. Resta come dubbio di classificazione dichiarato: una lettura
  alternativa lo tratterebbe come Principio "altro" (disposizione
  dichiarativa sulla leggibilita' delle informazioni), ma sarebbe incoerente
  con l'art. 42 §2 (stessa forma passiva, stesso tipo di precetto) e con il
  cap02 di questa Fonte.
- art. 42 §2 -> Obbligo "informativo/trasparenza": stessa forma passiva
  ("sono messe a disposizione almeno in inglese"), soggetto ricavabile dal
  paragrafo 1 che nomina l'ENISA come pubblicatore.
- art. 43 -> Obbligo "tecnico/sicurezza": il comma impone di garantire
  sicurezza e protezione dei segreti aziendali e delle informazioni riservate
  e di adottare le misure tecniche e organizzative necessarie e appropriate;
  il baricentro e' la protezione delle informazioni (confidenzialita' e
  proprieta' intellettuale), non un adempimento documentale, quindi
  "tecnico/sicurezza" e non "organizzativo".

Tipo di obbligo, riga per riga:
- art. 40 §1 e art. 40 §2 -> "di conservazione": tenuta di un sistema di
  registri e loro archiviazione sicura con termine minimo di cinque anni dopo
  la revoca del certificato EUCC (stesso tipo del cap02 art. 8 §7).
- art. 41 §1 -> "informativo/trasparenza" (informazioni verso gli utenti).
- art. 41 §2, art. 41 §3 -> "di conservazione": archiviazione sicura dei
  registri e dell'esemplare del prodotto, e conservazione della documentazione
  del certificato revocato insieme a quella del nuovo.
- art. 41 §4 -> "procedurale": i registri e le copie sono messi a disposizione
  dell'organismo di certificazione o dell'autorita' nazionale su richiesta; e'
  un adempimento verso gli organismi del sistema di certificazione, non un
  obbligo informativo verso il mercato o il pubblico (stessa lettura del cap02
  art. 8 §1 e art. 10 §5, dove il destinatario e' un organismo o l'ENISA).
- art. 42 §1, art. 42 §2, art. 42 §3, art. 42 §4 -> "informativo/trasparenza":
  pubblicazione, lingua, aggiornamento e qualita' delle informazioni sul
  sistema EUCC destinate al mercato e al pubblico.

Soggetti (le quattro categorie censite sono state applicate cosi', con la
convenzione del cap05 di questa Fonte):
- "Terza parte" (ruolo "obbligato") per l'ITSEF, gli organismi di
  certificazione, le autorita' nazionali di certificazione della
  cibersicurezza, l'ECCG, l'ENISA, la Commissione, gli organismi di
  valutazione della conformita' e "tutte le altre parti" dell'art. 43:
  attori istituzionali o industriali con ruolo identificabile e tracciabile,
  non QTSP ne' utenti finali;
- "Utente/titolare" (ruolo "obbligato") per il titolare di un certificato
  EUCC, che e' il soggetto di tutti i commi dell'art. 41 (la rubrica lo
  nomina: "Informazioni messe a disposizione dal titolare di un certificato");
- "Utente/titolare" (ruolo "destinatario") in art. 41 §1, dove il testo nomina
  "gli utenti" destinatari della leggibilita' delle informazioni: stessa
  scelta del cap02 art. 11 §2 per identica locuzione del testo. La categoria
  coincide con quella del soggetto obbligato dello stesso comma, ma i ruoli
  sono distinti (il titolare pubblica, gli utenti leggono): scelta dichiarata,
  in alternativa alla convenzione piu' restrittiva del cap05 (che in quel caso
  non valorizza il destinatario);
- "Terza parte" (ruolo "destinatario") in art. 41 §4 (l'organismo di
  certificazione e l'autorita' nazionale che richiedono i registri) e in
  art. 42 §3 (l'ENISA, destinataria dell'informazione).
Nessuna riga ha soggetto "QTSP/gestore": il capo non riguarda i prestatori di
servizi fiduciari. Destinatari non nominati dal testo non sono stati inferiti
(convenzione del cap02): l'art. 43 nomina un elenco aperto ("tutte le altre
parti") che non e' stato scomposto in categorie ulteriori.

`condizione_applicabilita` (testo libero, fatti esterni non tracciati come
nodi): art. 40 §2 e art. 41 §3 (la seconda frase / il comma valgono solo se
l'organismo di certificazione ha rilasciato un nuovo certificato EUCC in
conformita' dell'art. 13 §2(c) - disposizione di un altro capitolo di questa
fonte, non tracciata come nodo in questo modulo), art. 41 §4 (su richiesta
dell'organismo di certificazione o dell'autorita' nazionale), art. 42 §3
(per le autorita' nazionali l'obbligo di informare l'ENISA vale "se del
caso"). Non l'ho usata dove la condizione e' un nodo di questo stesso modulo:
in quei casi il legame e' dichiarato come relazione (le relazioni "richiama" di
questo file).

Unita' di indice: articolo + paragrafo numerato con "§" ("art. 40 §2") e
lettera tra parentesi ("art. 42 §1(a)"), convenzione gia' in uso in questo
censimento per gli atti di esecuzione. L'art. 43, non numerato in commi,
riceve l'item "art. 43". Le rubriche degli articoli non sono item di indice
(l'articolo e' coperto dai suoi commi) e neppure il titolo del Capo.

`testo_integrale`: verbatim e integrale di ogni comma, ricucendo le righe
spezzate dalla conversione XHTML -> testo (i marcatori di lettera "(a)"/"(b)"
isolati su riga propria nel testo ufficiale sono riuniti al testo che segue;
i commi restano separati da riga vuota; l'intestazione "Articolo N" + rubrica
e' premessa al primo comma di ciascun articolo, mai ripetuta nei commi
successivi, ed e' premessa anche all'unico periodo dell'art. 43, che il testo
ufficiale la fa precedere immediatamente). Nessun marcatore di elisione
(guardia `verifica_completezza_testo_integrale`, ADR-0010); simboli e
punteggiatura ufficiali conservati come nel testo scaricato. `testo` e' invece
la sintesi compressa (1-3 frasi) di ogni comma.

RELAZIONI: solo interne a questo modulo, tutte con `fonte_id_o_None = None`
su entrambi gli estremi. Quattro sono rinvii letterali, verificati sul
`testo_integrale` del nodo citante, quindi `evidence_type = "textual"`:
art. 41 §4 -> art. 41 §2 ("i registri e le copie di cui al paragrafo 2"),
art. 42 §2 -> art. 42 §1 ("Le informazioni di cui al paragrafo 1"),
art. 42 §3 -> art. 42 §1 ("un certificato EUCC di cui al paragrafo 1, lettera
b)": le lettere di art. 42 §1 sono mappate tutte sulla riga del §1, non hanno
un nodo proprio), art. 42 §4 -> art. 42 §1 ("le informazioni pubblicate in
conformita' del paragrafo 1, lettere a), b) e c)"). Una sola relazione
`evidence_type = "inferred"`: art. 41 §3 -> art. 41 §2, dove il rinvio e'
esplicito ma senza numero di paragrafo ("per lo stesso periodo di tempo", cioe'
il termine minimo di cinque anni stabilito dal paragrafo 2). `confidence` =
None per tutte: nessuno score reale da riportare (ADR-0005). Non ho dichiarato
relazioni di condizionalita' verso l'art. 13 §2(c) ne' verso l'art. 42 §1(h)
(citazioni che escono dal capitolo) ne' verso l'art. 40 §2 / art. 41 §3
(disposizioni parallele per soggetti diversi): sono collegamenti demandati alla
fase 6.

Rinvii demandati alla fase 6 (nessuna relazione dichiarata qui, perche'
attraversano il confine di capitolo o di fonte):
- art. 40 §2 e art. 41 §3 -> art. 13, paragrafo 2, lettera c) (cap02 di questa
  fonte);
- art. 41 §1 -> art. 55 del regolamento (UE) 2019/881 (altra fonte);
- art. 42 §1 -> art. 50, paragrafo 1, del regolamento (UE) 2019/881 (altra
  fonte);
- art. 42 §1(f) -> allegato I di questa fonte (cap09);
- art. 42 §1(g) -> art. 62, paragrafo 4, lettera c), del regolamento (UE)
  2019/881 (altra fonte);
- art. 42 §1(h) -> art. 47 di questa fonte (cap08).

Copertura: 21 item di indice, 11 righe (11 Obblighi + 0 Principi).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 40 §1",
        "testo": "L'ITSEF e gli organismi di certificazione mantengono un sistema di registri in cui sono contenuti tutti i documenti prodotti in relazione a ciascuna valutazione e certificazione da essi effettuata.",
        "testo_integrale": "Articolo 40\n\nConservazione dei registri da parte degli organismi di certificazione e dell'ITSEF\n\n1. L'ITSEF e gli organismi di certificazione mantengono un sistema di registri in cui sono contenuti tutti i documenti prodotti in relazione a ciascuna valutazione e certificazione da essi effettuata.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 40 §2",
        "testo": "Gli organismi di certificazione e l'ITSEF archiviano i registri in modo sicuro e li conservano per il periodo necessario ai fini del presente regolamento e per almeno cinque anni dopo la revoca del relativo certificato EUCC; qualora abbia rilasciato un nuovo certificato EUCC in conformità dell'articolo 13, paragrafo 2, lettera c), l'organismo di certificazione conserva la documentazione relativa al certificato EUCC revocato insieme a quella relativa al nuovo certificato EUCC, per lo stesso periodo di tempo.",
        "testo_integrale": "2. Gli organismi di certificazione e l'ITSEF archiviano i registri in modo sicuro e li conservano per il periodo necessario ai fini del presente regolamento e per almeno cinque anni dopo la revoca del relativo certificato EUCC. Qualora abbia rilasciato un nuovo certificato EUCC in conformità dell'articolo 13, paragrafo 2, lettera c), l'organismo di certificazione conserva la documentazione relativa al certificato EUCC revocato insieme a quella relativa al nuovo certificato EUCC, per lo stesso periodo di tempo.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "condizione_applicabilita": "La seconda frase si applica solo nel caso in cui l'organismo di certificazione abbia rilasciato un nuovo certificato EUCC in conformità dell'articolo 13, paragrafo 2, lettera c) — disposizione di un altro capitolo della stessa fonte, non tracciata come nodo in questo modulo (rinvio demandato alla fase 6).",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 41 §1",
        "testo": "Le informazioni di cui all'articolo 55 del regolamento (UE) 2019/881 sono disponibili in un linguaggio facilmente comprensibile dagli utenti; soggetto dell'articolo è il titolare di un certificato EUCC (rubrica), al quale è imputata la messa a disposizione di tali informazioni.",
        "testo_integrale": "Articolo 41\n\nInformazioni messe a disposizione dal titolare di un certificato\n\n1. Le informazioni di cui all'articolo 55 del regolamento (UE) 2019/881 sono disponibili in un linguaggio facilmente comprensibile dagli utenti.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 41 §2",
        "testo": "Il titolare di un certificato EUCC archivia in modo sicuro, per il periodo necessario ai fini del presente regolamento e per almeno cinque anni dopo la revoca del relativo certificato EUCC: i registri delle informazioni fornite all'organismo di certificazione e all'ITSEF durante il processo di certificazione; un esemplare del prodotto TIC certificato.",
        "testo_integrale": "2. Il titolare di un certificato EUCC archivia in modo sicuro per il periodo necessario ai fini del presente regolamento e per almeno cinque anni dopo la revoca del relativo certificato EUCC:\n\n(a) i registri delle informazioni fornite all'organismo di certificazione e all'ITSEF durante il processo di certificazione;\n\n(b) un esemplare del prodotto TIC certificato.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 41 §3",
        "testo": "Qualora l'organismo di certificazione abbia rilasciato un nuovo certificato EUCC in conformità dell'articolo 13, paragrafo 2, lettera c), il titolare conserva la documentazione relativa al certificato EUCC revocato insieme a quella relativa al nuovo certificato EUCC, per lo stesso periodo di tempo.",
        "testo_integrale": "3. Qualora l'organismo di certificazione abbia rilasciato un nuovo certificato EUCC in conformità dell'articolo 13, paragrafo 2, lettera c), il titolare conserva la documentazione relativa al certificato EUCC revocato insieme a quella relativa al nuovo certificato EUCC, per lo stesso periodo di tempo.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "condizione_applicabilita": "Il comma si applica solo nel caso in cui l'organismo di certificazione abbia rilasciato un nuovo certificato EUCC in conformità dell'articolo 13, paragrafo 2, lettera c) — disposizione di un altro capitolo della stessa fonte, non tracciata come nodo in questo modulo (rinvio demandato alla fase 6).",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 41 §4",
        "testo": "Su richiesta dell'organismo di certificazione o dell'autorità nazionale di certificazione della cibersicurezza, il titolare di un certificato EUCC mette a disposizione i registri e le copie di cui al paragrafo 2.",
        "testo_integrale": "4. Su richiesta dell'organismo di certificazione o dell'autorità nazionale di certificazione della cibersicurezza, il titolare di un certificato EUCC mette a disposizione i registri e le copie di cui al paragrafo 2.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica su richiesta dell'organismo di certificazione o dell'autorità nazionale di certificazione della cibersicurezza.",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 42 §1",
        "testo": "L'ENISA pubblica sul sito web di cui all'articolo 50, paragrafo 1, del regolamento (UE) 2019/881: tutti i certificati EUCC; le informazioni sullo stato dei certificati EUCC, in particolare se sono in vigore, sospesi, revocati o scaduti; le relazioni di certificazione corrispondenti a ciascun certificato EUCC; un elenco degli organismi di valutazione della conformità accreditati; un elenco di quelli autorizzati; i documenti sullo stato dell'arte di cui all'allegato I; i pareri del gruppo europeo per la certificazione della cibersicurezza di cui all'articolo 62, paragrafo 4, lettera c), del regolamento (UE) 2019/881; le relazioni di valutazione inter pares emesse in conformità dell'articolo 47.",
        "testo_integrale": "Articolo 42\n\nInformazioni che l'ENISA deve mettere a disposizione\n\n1. L'ENISA pubblica sul sito web di cui all'articolo 50, paragrafo 1, del regolamento (UE) 2019/881, le informazioni seguenti:\n\n(a) tutti i certificati EUCC;\n\n(b) le informazioni sullo stato dei certificati EUCC, in particolare se sono in vigore, sospesi, revocati o scaduti;\n\n(c) le relazioni di certificazione corrispondenti a ciascun certificato EUCC;\n\n(d) un elenco degli organismi di valutazione della conformità accreditati;\n\n(e) un elenco degli organismi di valutazione della conformità autorizzati;\n\n(f) i documenti sullo stato dell'arte di cui all'allegato I;\n\n(g) i pareri del gruppo europeo per la certificazione della cibersicurezza di cui all'articolo 62, paragrafo 4, lettera c), del regolamento (UE) 2019/881;\n\n(h) le relazioni di valutazione inter pares emesse in conformità dell'articolo 47.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 42 §2",
        "testo": "Le informazioni di cui al paragrafo 1 sono messe a disposizione almeno in inglese.",
        "testo_integrale": "2. Le informazioni di cui al paragrafo 1 sono messe a disposizione almeno in inglese.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 42 §3",
        "testo": "Gli organismi di certificazione e, se del caso, le autorità nazionali di certificazione della cibersicurezza informano senza indugio l'ENISA in merito alle loro decisioni che incidono sul contenuto o sullo stato di un certificato EUCC di cui al paragrafo 1, lettera b).",
        "testo_integrale": "3. Gli organismi di certificazione e, se del caso, le autorità nazionali di certificazione della cibersicurezza informano senza indugio l'ENISA in merito alle loro decisioni che incidono sul contenuto o sullo stato di un certificato EUCC di cui al paragrafo 1, lettera b).",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Per le autorità nazionali di certificazione della cibersicurezza l'obbligo di informare l'ENISA vale \"se del caso\"; per gli organismi di certificazione è incondizionato.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 42 §4",
        "testo": "L'ENISA garantisce che le informazioni pubblicate in conformità del paragrafo 1, lettere a), b) e c), identifichino chiaramente le versioni di un prodotto TIC certificato che sono contemplate da un certificato EUCC.",
        "testo_integrale": "4. L'ENISA garantisce che le informazioni pubblicate in conformità del paragrafo 1, lettere a), b) e c), identifichino chiaramente le versioni di un prodotto TIC certificato che sono contemplate da un certificato EUCC.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 43",
        "testo": "Gli organismi di valutazione della conformità, le autorità nazionali di certificazione della cibersicurezza, l'ECCG, l'ENISA, la Commissione e tutte le altre parti garantiscono la sicurezza e la protezione dei segreti aziendali e di altre informazioni riservate, compresi i segreti commerciali, nonché la salvaguardia dei diritti di proprietà intellettuale, e adottano le misure tecniche e organizzative necessarie e appropriate.",
        "testo_integrale": "Articolo 43\n\nProtezione delle informazioni\n\nGli organismi di valutazione della conformità, le autorità nazionali di certificazione della cibersicurezza, l'ECCG, l'ENISA, la Commissione e tutte le altre parti garantiscono la sicurezza e la protezione dei segreti aziendali e di altre informazioni riservate, compresi i segreti commerciali, nonché la salvaguardia dei diritti di proprietà intellettuale, e adottano le misure tecniche e organizzative necessarie e appropriate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = [
    "art. 40 §1",
    "art. 40 §2",
    "art. 41 §1",
    "art. 41 §2",
    "art. 41 §2(a)",
    "art. 41 §2(b)",
    "art. 41 §3",
    "art. 41 §4",
    "art. 42 §1",
    "art. 42 §1(a)",
    "art. 42 §1(b)",
    "art. 42 §1(c)",
    "art. 42 §1(d)",
    "art. 42 §1(e)",
    "art. 42 §1(f)",
    "art. 42 §1(g)",
    "art. 42 §1(h)",
    "art. 42 §2",
    "art. 42 §3",
    "art. 42 §4",
    "art. 43",
]

# Ogni riga copre il proprio comma per intero, lettere comprese (vedi la
# docstring: un comma = una riga, con lettere indicate separatamente ma mappate
# alla riga del comma); l'art. 43 non ha commi numerati e copre il solo item
# "art. 43".
MAPPATURA_LOCALE = {
    "art. 40 §1": ["art. 40 §1"],
    "art. 40 §2": ["art. 40 §2"],
    "art. 41 §1": ["art. 41 §1"],
    "art. 41 §2": ["art. 41 §2", "art. 41 §2(a)", "art. 41 §2(b)"],
    "art. 41 §3": ["art. 41 §3"],
    "art. 41 §4": ["art. 41 §4"],
    "art. 42 §1": [
        "art. 42 §1",
        "art. 42 §1(a)",
        "art. 42 §1(b)",
        "art. 42 §1(c)",
        "art. 42 §1(d)",
        "art. 42 §1(e)",
        "art. 42 §1(f)",
        "art. 42 §1(g)",
        "art. 42 §1(h)",
    ],
    "art. 42 §2": ["art. 42 §2"],
    "art. 42 §3": ["art. 42 §3"],
    "art. 42 §4": ["art. 42 §4"],
    "art. 43": ["art. 43"],
}

# Relazioni interne a questo capitolo (fonte_id_o_None = None su entrambi gli
# estremi). Quattro sono rinvii letterali verificati sul `testo_integrale` del
# nodo citante; l'ultima e' un rinvio esplicito ma privo del numero di
# paragrafo ("per lo stesso periodo di tempo"), quindi `inferred`. I rinvii
# che escono dal capitolo (art. 13 §2(c) in art. 40 §2 e art. 41 §3, allegato I
# e art. 47 in art. 42 §1, art. 55, art. 50 §1 e art. 62 §4(c) del regolamento
# (UE) 2019/881) sono elencati nella docstring e demandati alla fase 6.
# `confidence` = None: nessuno score reale da riportare (ADR-0005).
RELAZIONI = [
    # art. 41 §4 -> art. 41 §2: "i registri e le copie di cui al paragrafo 2".
    {
        "nodo_da": ("obbligo", None, "art. 41 §4"),
        "nodo_a": ("obbligo", None, "art. 41 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # art. 42 §2 -> art. 42 §1: "Le informazioni di cui al paragrafo 1".
    {
        "nodo_da": ("obbligo", None, "art. 42 §2"),
        "nodo_a": ("obbligo", None, "art. 42 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # art. 42 §3 -> art. 42 §1: "un certificato EUCC di cui al paragrafo 1,
    # lettera b)" (le lettere di art. 42 §1 sono coperte dalla riga del §1).
    {
        "nodo_da": ("obbligo", None, "art. 42 §3"),
        "nodo_a": ("obbligo", None, "art. 42 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # art. 42 §4 -> art. 42 §1: "le informazioni pubblicate in conformità del
    # paragrafo 1, lettere a), b) e c)".
    {
        "nodo_da": ("obbligo", None, "art. 42 §4"),
        "nodo_a": ("obbligo", None, "art. 42 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # art. 41 §3 -> art. 41 §2: "per lo stesso periodo di tempo", cioe' il
    # termine minimo di cinque anni stabilito dal paragrafo 2. Rinvio esplicito
    # nel testo ma senza numero di paragrafo: `inferred`.
    {
        "nodo_da": ("obbligo", None, "art. 41 §3"),
        "nodo_a": ("obbligo", None, "art. 41 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
]
