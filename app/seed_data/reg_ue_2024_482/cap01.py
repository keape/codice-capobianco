"""Regolamento di esecuzione (UE) 2024/482 della Commissione, del 31 gennaio
2024 - modalita' di applicazione del regolamento (UE) 2019/881 del Parlamento
europeo e del Consiglio per quanto riguarda l'adozione del sistema europeo di
certificazione della cibersicurezza basato sui criteri comuni (EUCC). Fonte 29
(slug `reg_ue_2024_482`), capitolo 1 di 14 (vedi
app/.source_cache/reg_ue_2024_482/manifest.json): Capo I - Disposizioni
generali (artt. 1-6). Gli artt. 7-50 e gli allegati I-IX appartengono ai
capitoli 2-14 della stessa Fonte, assegnati ad altri moduli: nessuno di quei
file e' toccato qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_482/cap01.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R0482, lingua italiana; URL
risolto
http://publications.europa.eu/resource/cellar/687c0d05-c580-11ee-95d9-01aa75ed71a1.0014.03/DOC_1,
XHTML della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 540.435 byte
scaricati, 135.367 caratteri di testo, sha256 del raw.txt
b46d08cab6d63b2c190ae767042c07c1fc324955c22ef491eb314556b28ca5b8 - dettagli
completi in app/.source_cache/reg_ue_2024_482/provenance.json).

Modellazione (ADR-0007, nessun discrimine di rilevanza):
- Paratesto -> nessun nodo: l'intestazione di capitolo ("CAPO I" + rubrica
  "DISPOSIZIONI GENERALI") e le intestazioni dei sei articoli ("Articolo N" +
  rubrica) non sono articoli, commi o lettere, ma struttura dell'atto; le
  rubriche restano comunque coperte perche' incluse nel `testo_integrale`
  della prima riga di ogni articolo (convenzione dei moduli gia' censiti di
  atti di esecuzione UE). In questa porzione non compaiono preambolo
  (considerando, a monte del Capo I), epigrafe, firma, formula di chiusura,
  nota a pie' di pagina ne' riga ELI: nessuno di questi elementi produce nodo
  o item di indice. Il Capo I non contiene disposizioni finali: entrata in
  vigore, applicazione e abrogazioni sono negli artt. 44-50 (cap08).
- Art. 1 (oggetto e ambito di applicazione) -> UN solo Principio, tipo
  "scopo/ambito di applicazione": l'articolo ha due capoversi non numerati,
  entrambi dichiarativi (il primo istituisce l'EUCC, il secondo ne delimita
  l'ambito a prodotti TIC e profili di protezione) e nessuno dei due impone
  un comportamento a un soggetto. Un solo nodo e un solo item di indice "art.
  1": il testo ufficiale non numera i capoversi, quindi una numerazione per
  comma ("art. 1 §1"/"art. 1 §2") sarebbe inventata - stesso criterio degli
  "articoli a comma unico senza numerazione di paragrafo" del Reg.
  2024/2979 (cap03). Entrambi i capoversi restano verbatim, separati da riga
  vuota, nel `testo_integrale`.
- Art. 2 (definizioni) -> UNA riga Principio, tipo "definitorio", con tutte
  le 15 voci nel `testo_integrale` verbatim; item di indice "art. 2, punto 1"
  fino a "art. 2, punto 15", tutti mappati a questa riga. Nessun item proprio
  per il chapeau ("Ai fini del presente regolamento si applicano le
  definizioni seguenti:") ne' per la rubrica: il chapeau non ha precetto
  autonomo e il task prescrive un item per ogni voce definitoria (diverso da
  reg_ue_2025_1569/cap01, dove l'item del chapeau e' stato aggiunto: scelta
  non replicata qui per non coprire due volte la stessa disposizione).
- Art. 3 (norme di valutazione) -> UN solo Principio, tipo "altro": il
  chapeau enuncia in forma impersonale quali norme si applicano nell'ambito
  del sistema EUCC, senza imporre un comportamento a un soggetto identificato
  ne' dichiarare un effetto giuridico - e' una designazione delle norme
  applicabili, stesso trattamento dell'art. 2 del Reg. 2025/2532 e dell'art.
  1 del Reg. 2025/1566. Dubbio dichiarato: leggendo "si applicano" come
  precetto rivolto agli organismi di certificazione/valutazione la riga
  sarebbe un Obbligo; la formulazione impersonale e la collocazione fra le
  disposizioni generali (accanto a oggetto e definizioni) hanno fatto
  preferire il Principio. Le lettere (a) e (b) non hanno verbo proprio e sono
  il contenuto dell'elenco retto dal chapeau: restano nel `testo_integrale`
  della riga e ricevono item di indice propri ("art. 3(a)", "art. 3(b)"),
  come le lettere di art. 5 §1 di questa stessa Fonte di esempio (Reg.
  2024/2979 cap02).
- Art. 4 §1 -> Obbligo, tipo "procedurale", soggetto obbligato "Terza parte"
  (gli organismi di certificazione, la cui attivita' e' l'attivita' di
  certificazione come definita dall'art. 2 punto 12 di questa Fonte): il
  comma prescrive con quale livello di affidabilita' («sostanziale» o
  «elevato») i certificati EUCC sono rilasciati. Dubbio dichiarato:
  "tecnico/sicurezza" sarebbe sostenibile (il livello e' una proprieta'
  tecnica del certificato); scelto "procedurale" perche' il precetto governa
  il rilascio del certificato, non il contenuto tecnico della valutazione.
- Art. 4 §2 e §3 -> due Principi, tipo "altro": enunciazioni dichiarative di
  corrispondenza fra i livelli di affidabilita' EUCC e i livelli AVA_VAN
  (nessun comportamento imposto a un soggetto, nessuna condizione di
  applicabilita'). Non "equivalenza giuridica": nel censimento quel tipo
  copre l'equivalenza di effetti giuridici fra strumenti diversi (es. Cad),
  non la corrispondenza fra scale tecniche di livelli.
- Art. 4 §4 -> Principio, tipo "altro": il comma dichiara che cosa distingue
  il livello di affidabilita' confermato in un certificato EUCC (uso conforme
  rispetto a uso aumentato dei componenti), non impone un comportamento. Il
  rinvio all'allegato VIII resta nel `testo_integrale` (rinvii demandati alla
  fase 6, sotto).
- Art. 4 §5 -> Obbligo, tipo "tecnico/sicurezza", soggetto obbligato "Terza
  parte" (gli organismi di valutazione della conformita', nominati dal
  comma): applicare le componenti dell'affidabilita' da cui dipende il
  livello AVA_VAN selezionato, in conformita' delle norme di cui all'art. 3.
- Art. 5 §1 -> Obbligo, tipo "procedurale", soggetto obbligato "Terza parte".
  Il comma e' costruito al passivo ("La certificazione di un prodotto TIC e'
  effettuata rispetto al suo traguardo di sicurezza"): l'attore non e'
  nominato nel comma, ma la certificazione e' l'attivita' dell'organismo di
  certificazione (art. 2 punto 12 e art. 4 §1 di questo stesso capitolo),
  quindi la categoria e' attribuita per implicazione dichiarata. Le lettere
  (a) e (b) sono le due alternative dello stesso precetto (traguardo di
  sicurezza come definito dal richiedente, oppure integrando un profilo di
  protezione certificato): nessuna delle due ha precetto autonomo ("come
  definito dal richiedente" non e' una prescrizione autosufficiente), restano
  entrambe nel `testo_integrale` della riga e ricevono item di indice propri
  ("art. 5 §1(a)", "art. 5 §1(b)"). Il "richiedente" nominato nella lettera
  (a) non e' modellato come soggetto (ne' obbligato ne' destinatario):
  individua di chi sia il traguardo di sicurezza usato, non chi debba tenere
  il comportamento.
- Art. 5 §2 -> Principio, tipo "altro": delimita lo scopo per cui i profili
  di protezione possono essere certificati ("al solo scopo di certificare i
  prodotti TIC che rientrano nella categoria specifica"), senza imporre un
  comportamento a un soggetto.
- Art. 6 -> Obbligo, tipo "procedurale": divieto di autovalutazione della
  conformita' (l'astensione e' il comportamento imposto). Nessun `soggetti`:
  il comma non nomina il soggetto tenuto - esclude la via dell'autovalutazione
  di conformita' prevista dall'art. 53 del regolamento (UE) 2019/881, che
  riguarda chi chiede la certificazione - e la regola del batch vieta di
  forzare categorie di soggetto non nominate nel testo (stessa scelta di
  "allegato IV, punto 1" in Reg. 2024/2979 cap05). Dubbio dichiarato:
  l'assegnazione a "Terza parte" sarebbe plausibile ma inferita.
- Unita' di indice: articolo ("art. 1", "art. 3", "art. 6") per gli articoli
  senza commi numerati; "art. 4 §N" e "art. 5 §N" per gli articoli con commi
  numerati; lettera in coda ("art. 3(a)", "art. 5 §1(a)") in analogia alla
  notazione "art. 7 §1(a)" quando l'articolo non ha commi numerati; "art. 2,
  punto N" per le voci definitorie. Le rubriche degli articoli non sono item
  di indice (l'articolo e' coperto dai suoi commi) e neppure il titolo del
  Capo.
- `testo_integrale`: verbatim e integrale, ricucito dalle righe spezzate
  dalla conversione XHTML -> testo. In particolare: i capoversi dell'art. 1 e
  i commi degli artt. 4 e 5 restano ciascuno in un blocco separato da riga
  vuota; le lettere isolate su riga propria sono riunite al loro testo; le
  voci dell'art. 2, il cui numero ("(1)") e la definizione che segue sono
  separati in due blocchi dal dump, sono ricucite in un'unica riga ("(1)
  «criteri comuni»: i criteri comuni per la valutazione della sicurezza delle
  tecnologie dell'informazione quali definiti nella norma ISO/IEC 15408;");
  l'intestazione "Articolo N" + rubrica e' premessa alla prima riga di ogni
  articolo, dove il testo ufficiale la precede immediatamente (art. 1, art.
  2, art. 3, art. 4 §1, art. 5 §1, art. 6). Nessun marcatore di elisione
  (vincolo `verifica_completezza_testo_integrale`, ADR-0010). `testo` e'
  invece la sintesi compressa (1-3 frasi) di ogni disposizione.
- RELAZIONI: una sola relazione, interna a questo capitolo e verificata sul
  `testo_integrale` delle righe coinvolte - art. 4 §5 -> art. 3, "richiama",
  `evidence_type` "textual" ("in conformita' delle norme di cui all'articolo
  3"), `confidence` None perche' non esiste uno score reale da riportare
  (ADR-0005). Non e' stata dichiarata alcuna relazione verso altri capitoli
  di questa Fonte o verso altre Fonti (elenco sotto): le costruisce la
  sessione principale in fase 6, e dichiararle qui in import parallelo per
  capitolo fa fallire il merge con KeyError. Non sono state dichiarate
  nemmeno relazioni "definisce" dalla riga "art. 2" verso i nodi che usano i
  concetti definiti (art. 1 usa "criteri comuni"; art. 4 §2, §3 e §5 usano
  "livello AVA_VAN"; art. 5 §1 e §2 usano "traguardo di sicurezza" e "profilo
  di protezione"): sarebbero relazioni inferite a livello di articolo (art. 2
  e' un unico nodo per 15 definizioni) e non citazioni letterali.
  Avvertenza per l'audit `verifica_relazioni_textual.py`: la relazione
  dichiarata cade nella sua sezione A ("citazioni dichiarate senza traccia
  del riferimento citato") perche' lo strumento cerca nel testo citante una
  traccia del riferimento citato ("§ N"/"paragrafo N") e scarta le tracce di
  un solo carattere, mentre qui la forma usata dal testo ufficiale e' a
  livello di articolo ("le norme di cui all'articolo 3").
- Rinvii demandati alla fase 6 (nessuna relazione dichiarata qui): art. 2
  punto 1 -> norma ISO/IEC 15408; art. 2 punto 2 -> norma ISO/IEC 18045; art.
  2 punto 7 -> art. 2, punto 13), del regolamento (CE) n. 765/2008; art. 2
  punto 11 -> art. 58, paragrafo 1, del regolamento (UE) 2019/881; art. 2
  punto 15 -> art. 3, punto 4), del regolamento (UE) 2019/1020; art. 4 §4 ->
  allegato VIII di questa Fonte (cap13); art. 6 -> art. 53 del regolamento
  (UE) 2019/881. Anche il rinvio implicito dell'art. 3 al "sistema EUCC"
  istituito dall'art. 1 resta senza arco: il testo non lo cita.
- Nessuna riga valorizza `severita` o `sanzioni`: l'atto non gradua i
  requisiti ne' prevede sanzioni proprie (stessa scelta degli altri atti di
  esecuzione gia' censiti). `stato` = "vigente" per tutte le righe. Nessun
  `oggetti_giuridici` valorizzato: fra i valori censiti non ce n'e' uno che
  corrisponda a "prodotto TIC" o "certificato EUCC", e la voce generica
  "altro" non e' stata forzata (stesso criterio del Reg. 2024/2979 cap02).

Copertura: 29 item di indice, 11 righe (4 Obblighi + 7 Principi), 1 relazione
interna.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 4 §1",
        "testo": "Gli organismi di certificazione rilasciano certificati EUCC con un livello di affidabilità «sostanziale» o «elevato».",
        "testo_integrale": "Articolo 4\n\nLivelli di affidabilità\n\n1. Gli organismi di certificazione rilasciano certificati EUCC con un livello di affidabilità «sostanziale» o «elevato».",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 4 §5",
        "testo": "Gli organismi di valutazione della conformità applicano le componenti dell'affidabilità da cui dipende il livello AVA_VAN selezionato, in conformità delle norme di cui all'articolo 3 (i criteri comuni e la metodologia comune di valutazione).",
        "testo_integrale": "5. Gli organismi di valutazione della conformità applicano le componenti dell'affidabilità da cui dipende il livello AVA_VAN selezionato in conformità delle norme di cui all'articolo 3.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 5 §1",
        "testo": "La certificazione di un prodotto TIC è effettuata rispetto al suo traguardo di sicurezza: come definito dal richiedente (a), oppure integrando un profilo di protezione certificato come parte del processo TIC, qualora il prodotto TIC rientri nella categoria di prodotti TIC contemplata da tale profilo di protezione (b).",
        "testo_integrale": "Articolo 5\n\nMetodi di certificazione dei prodotti TIC\n\n1. La certificazione di un prodotto TIC è effettuata rispetto al suo traguardo di sicurezza:\n\n(a) come definito dal richiedente; oppure\n\n(b) integrando un profilo di protezione certificato come parte del processo TIC, qualora il prodotto TIC rientri nella categoria di prodotti TIC contemplata da tale profilo di protezione.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 6",
        "testo": "Non è consentita l'autovalutazione della conformità ai sensi dell'articolo 53 del regolamento (UE) 2019/881.",
        "testo_integrale": "Articolo 6\n\nAutovalutazione della conformità\n\nNon è consentita l'autovalutazione della conformità ai sensi dell'articolo 53 del regolamento (UE) 2019/881.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 1",
        "testo": "Il regolamento istituisce il sistema europeo di certificazione della cibersicurezza basato sui criteri comuni (EUCC); il regolamento si applica a tutti i prodotti delle tecnologie dell'informazione e della comunicazione (TIC), compresa la relativa documentazione, presentati ai fini della certificazione nel quadro dell'EUCC, nonché a tutti i profili di protezione presentati ai fini della certificazione come parte del processo TIC alla base della certificazione dei prodotti TIC.",
        "testo_integrale": "Articolo 1\n\nOggetto e ambito di applicazione\n\nIl presente regolamento istituisce il sistema europeo di certificazione della cibersicurezza basato sui criteri comuni (EUCC).\n\nIl presente regolamento si applica a tutti i prodotti delle tecnologie dell'informazione e della comunicazione (TIC), compresa la relativa documentazione, che sono presentati ai fini della certificazione nel quadro dell'EUCC, nonché a tutti i profili di protezione che sono presentati ai fini della certificazione come parte del processo TIC alla base della certificazione dei prodotti TIC.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2",
        "testo": "Definizioni applicabili ai fini del regolamento, in quindici voci: «criteri comuni» (ISO/IEC 15408); «metodologia comune di valutazione» (ISO/IEC 18045); «oggetto della valutazione»; «traguardo di sicurezza»; «profilo di protezione»; «relazione tecnica di valutazione»; «ITSEF»; «livello AVA_VAN»; «certificato EUCC»; «prodotto composito»; «autorità nazionale di certificazione della cibersicurezza»; «organismo di certificazione»; «settore tecnico»; «documento sullo stato dell'arte»; «autorità di vigilanza del mercato».",
        "testo_integrale": "Articolo 2\n\nDefinizioni\n\nAi fini del presente regolamento si applicano le definizioni seguenti:\n\n(1) «criteri comuni»: i criteri comuni per la valutazione della sicurezza delle tecnologie dell'informazione quali definiti nella norma ISO/IEC 15408;\n\n(2) «metodologia comune di valutazione»: la metodologia comune per la valutazione della sicurezza delle tecnologie dell'informazione quale definita nella norma ISO/IEC 18045;\n\n(3) «oggetto della valutazione»: un prodotto TIC o una sua parte, o un profilo di protezione come parte di un processo TIC, sottoposto a valutazione di cibersicurezza allo scopo di ricevere la certificazione EUCC;\n\n(4) «traguardo di sicurezza»: una dichiarazione dei requisiti di sicurezza dipendenti dall'implementazione per uno specifico prodotto TIC;\n\n(5) «profilo di protezione»: un processo TIC che stabilisce i requisiti di sicurezza per una categoria specifica di prodotti TIC, che affronta le esigenze di sicurezza indipendenti dall'implementazione e che può essere utilizzato per valutare i prodotti TIC rientranti in tale categoria specifica ai fini della loro certificazione;\n\n(6) «relazione tecnica di valutazione»: un documento prodotto da un'ITSEF per presentare i risultati, i verdetti e le giustificazioni ottenuti durante la valutazione di un prodotto TIC o di un profilo di protezione in conformità delle norme e degli obblighi stabiliti nel presente regolamento;\n\n(7) «ITSEF»: una struttura di valutazione della sicurezza delle tecnologie dell'informazione, che è un organismo di valutazione della conformità quale definito nell'articolo 2, punto 13), del regolamento (CE) n. 765/2008, che svolge attività di valutazione;\n\n(8) «livello AVA_VAN»: un livello di analisi della vulnerabilità dell'affidabilità che indica il grado delle attività di valutazione della cibersicurezza svolte per determinare il livello di resistenza rispetto alla potenziale possibilità di sfruttare i difetti o i punti deboli dell'oggetto della valutazione nel suo ambiente operativo, come stabilito nei criteri comuni;\n\n(9) «certificato EUCC»: un certificato di cibersicurezza rilasciato nell'ambito dell'EUCC per prodotti TIC o per profili di protezione che possono essere utilizzati esclusivamente nel processo TIC di certificazione dei prodotti TIC;\n\n(10) «prodotto composito»: un prodotto TIC che è valutato insieme a un altro prodotto TIC sottostante che ha già ricevuto un certificato EUCC e dalla cui funzionalità di sicurezza dipende il prodotto TIC composito;\n\n(11) «autorità nazionale di certificazione della cibersicurezza»: un'autorità designata da uno Stato membro a norma dell'articolo 58, paragrafo 1, del regolamento (UE) 2019/881;\n\n(12) «organismo di certificazione»: un organismo di valutazione della conformità quale definito nell'articolo 2, punto 13), del regolamento (CE) n. 765/2008, che svolge attività di certificazione;\n\n(13) «settore tecnico»: un quadro tecnico comune relativo a una particolare tecnologia per la certificazione armonizzata con una serie di requisiti di sicurezza caratteristici;\n\n(14) «documento sullo stato dell'arte»: documento in cui sono specificati i metodi, le tecniche e gli strumenti di valutazione che si applicano alla certificazione dei prodotti TIC, o ai requisiti di sicurezza di una categoria generica di prodotti TIC, o a qualsiasi altro requisito necessario per la certificazione, al fine di armonizzare la valutazione, in particolare dei settori tecnici o dei profili di protezione;\n\n(15) «autorità di vigilanza del mercato»: un'autorità quale definita nell'articolo 3, punto 4), del regolamento (UE) 2019/1020.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 3",
        "testo": "Alle valutazioni effettuate nell'ambito del sistema EUCC si applicano le norme seguenti: i criteri comuni (a) e la metodologia comune di valutazione (b).",
        "testo_integrale": "Articolo 3\n\nNorme di valutazione\n\nAlle valutazioni effettuate nell'ambito del sistema EUCC si applicano le norme seguenti:\n\n(a) i criteri comuni;\n\n(b) la metodologia comune di valutazione.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 4 §2",
        "testo": "I certificati EUCC al livello di affidabilità «sostanziale» corrispondono ai certificati relativi al livello AVA_VAN 1 o 2.",
        "testo_integrale": "2. I certificati EUCC al livello di affidabilità «sostanziale» corrispondono ai certificati relativi al livello AVA_VAN 1 o 2.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 4 §3",
        "testo": "I certificati EUCC al livello di affidabilità «elevato» corrispondono ai certificati relativi al livello AVA_VAN 3, 4 o 5.",
        "testo_integrale": "3. I certificati EUCC al livello di affidabilità «elevato» corrispondono ai certificati relativi al livello AVA_VAN 3, 4 o 5.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 4 §4",
        "testo": "Il livello di affidabilità confermato in un certificato EUCC distingue tra l'uso conforme e l'uso aumentato dei componenti dell'affidabilità specificati nei criteri comuni in conformità dell'allegato VIII.",
        "testo_integrale": "4. Il livello di affidabilità confermato in un certificato EUCC distingue tra l'uso conforme e l'uso aumentato dei componenti dell'affidabilità specificati nei criteri comuni in conformità dell'allegato VIII.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 5 §2",
        "testo": "I profili di protezione sono certificati al solo scopo di certificare i prodotti TIC che rientrano nella categoria specifica di prodotti TIC contemplata dal profilo di protezione.",
        "testo_integrale": "2. I profili di protezione sono certificati al solo scopo di certificare i prodotti TIC che rientrano nella categoria specifica di prodotti TIC contemplata dal profilo di protezione.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 1",
    "art. 2, punto 1",
    "art. 2, punto 2",
    "art. 2, punto 3",
    "art. 2, punto 4",
    "art. 2, punto 5",
    "art. 2, punto 6",
    "art. 2, punto 7",
    "art. 2, punto 8",
    "art. 2, punto 9",
    "art. 2, punto 10",
    "art. 2, punto 11",
    "art. 2, punto 12",
    "art. 2, punto 13",
    "art. 2, punto 14",
    "art. 2, punto 15",
    "art. 3",
    "art. 3(a)",
    "art. 3(b)",
    "art. 4 §1",
    "art. 4 §2",
    "art. 4 §3",
    "art. 4 §4",
    "art. 4 §5",
    "art. 5 §1",
    "art. 5 §1(a)",
    "art. 5 §1(b)",
    "art. 5 §2",
    "art. 6",
]

MAPPATURA_LOCALE = {
    "art. 1": ["art. 1"],
    "art. 2": [
        "art. 2, punto 1",
        "art. 2, punto 2",
        "art. 2, punto 3",
        "art. 2, punto 4",
        "art. 2, punto 5",
        "art. 2, punto 6",
        "art. 2, punto 7",
        "art. 2, punto 8",
        "art. 2, punto 9",
        "art. 2, punto 10",
        "art. 2, punto 11",
        "art. 2, punto 12",
        "art. 2, punto 13",
        "art. 2, punto 14",
        "art. 2, punto 15",
    ],
    "art. 3": ["art. 3", "art. 3(a)", "art. 3(b)"],
    "art. 4 §1": ["art. 4 §1"],
    "art. 4 §2": ["art. 4 §2"],
    "art. 4 §3": ["art. 4 §3"],
    "art. 4 §4": ["art. 4 §4"],
    "art. 4 §5": ["art. 4 §5"],
    "art. 5 §1": ["art. 5 §1", "art. 5 §1(a)", "art. 5 §1(b)"],
    "art. 5 §2": ["art. 5 §2"],
    "art. 6": ["art. 6"],
}

# Relazioni interne a questo capitolo (fonte_id_o_None = None su entrambi gli
# estremi). Una sola relazione: art. 4 §5 cita letteralmente "le norme di cui
# all'articolo 3", cioe' il Principio "art. 3" di questo stesso modulo (i
# criteri comuni e la metodologia comune di valutazione), quindi
# `evidence_type` = "textual" e `confidence` = None: nessuno score reale da
# riportare (ADR-0005, non va inventato). I rinvii ad altri capitoli di questa
# Fonte (allegato VIII in art. 4 §4) e ad altre Fonti (ISO/IEC 15408 e 18045,
# reg. (CE) 765/2008, reg. (UE) 2019/881, reg. (UE) 2019/1020) non sono
# dichiarati qui: sono collegamenti della fase 6, elencati nel docstring.
RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "art. 4 §5"),
        "nodo_a": ("principio", None, "art. 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
