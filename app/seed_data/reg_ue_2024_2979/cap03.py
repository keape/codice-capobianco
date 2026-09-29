"""Regolamento di esecuzione (UE) 2024/2979 della Commissione, del 28 novembre
2024 - modalita' di applicazione del regolamento (UE) n. 910/2014 per quanto
riguarda l'integrita' e le funzionalita' di base dei portafogli europei di
identita' digitale (articolo 5 bis, paragrafo 23, eIDAS). Fonte 28 (id
assegnato dal wiring della sessione principale: questo modulo NON tocca
`app/seed.py`, gli id sono risolti per riferimento dal registro di
`app/seed_data/lib.py`).

Porzione di questo modulo (cap03 di 5, come da manifest di
`app/tools/split_source.py`): Capo III - Funzionalita' e caratteristiche di
base dei portafogli europei di identita' digitale (articoli 8-14). Testo
ufficiale italiano in app/.source_cache/reg_ue_2024_2979/cap03.txt, acquisito
con content negotiation CELLAR
(publications.europa.eu/resource/celex/32024R2979, lingua italiana): url
risolto
http://publications.europa.eu/resource/cellar/a7576de1-b1e0-11ef-acb1-01aa75ed71a1.0014.03/DOC_1
(XHTML della Gazzetta ufficiale), fetch 2026-09-28, sha256 del raw.txt
c0bebf5c6707ddb9c70999245e38999f63f154afee2afc6009aad72d1d09cad0 (provenienza
completa in provenance.json). Gli articoli 1-2 (Capo I), 3-7 (Capo II), 15
(Capo IV) e gli allegati I-V appartengono ad altri capitoli di questa Fonte e
non sono toccati qui.

Modellazione (ADR-0007, nessun discrimine di rilevanza):
- Paratesto: l'intestazione di capitolo ("CAPO III" + rubrica "FUNZIONALITA' E
  CARATTERISTICHE DI BASE DEI PORTAFOGLI EUROPEI DI IDENTITA' DIGITALE") non
  produce nodo e non e' un item di indice: e' un'intestazione di partizione
  del testo, non un articolo/comma/lettera e non contiene prescrizioni (stesso
  trattamento dell'intestazione di capitolo in tutte le Fonti gia' censite).
  Nella porzione non compaiono preambolo, epigrafe (Fatto a Bruxelles), firma,
  formula di chiusura o note a pie' di pagina: sono a monte (considerando) o
  nell'art. 15 del capitolo 4.
- Articoli a comma unico senza numerazione di paragrafo: art. 8 ("I fornitori
  di portafogli garantiscono che le soluzioni di portafoglio supportino ...")
  e art. 13 ("Laddove tecnicamente fattibile ... le unita' di portafoglio
  supportano l'esportazione sicura e la portabilita' ...") -> UNA riga ciascuno
  (un nodo per articolo), item di indice "art. 8" e "art. 13": il testo
  ufficiale non numera alcun paragrafo, quindi una numerazione per comma
  ("art. 8 §1") sarebbe inventata.
- Granularita': un comma = una riga (l'unita' di copertura e' il comma).
  Art. 9 (7 commi) -> 7 righe; art. 10 (3 commi) -> 3 righe; art. 11 (3 commi)
  -> 3 righe; art. 12 (3 commi) -> 3 righe; art. 14 (2 commi) -> 2 righe.
- Lettere interne a un comma: le quattro lettere dell'art. 9 §2 (contenuto
  minimo delle registrazioni) e le quattro dell'art. 12 §2 (funzioni delle
  applicazioni per la creazione di firme) NON hanno precetto autonomo e
  distinto: sono il contenuto specificativo del comma che le introduce
  (elenco enumerativo: "figurano come minimo: a) ... d)" / "dispongono delle
  funzioni seguenti: a) ... d)"). Restano quindi integralmente nel
  `testo_integrale` del comma e non ricevono righe proprie; sono pero'
  indicizzate separatamente ("art. 9 §2(a)" ... "art. 9 §2(d)", "art. 12
  §2(a)" ... "art. 12 §2(d)") e mappate tutte alla riga del rispettivo comma.
  Nessun'altra lettera compare in questa porzione, quindi nessuna eccezione
  alla regola "le lettere restano dentro il comma".
- Soggetto obbligato delle righe di comportamento: "QTSP/gestore", con
  l'ancoraggio testuale nella definizione (7) dell'art. 2 di questa stessa
  Fonte ("fornitore del portafoglio": persona fisica o giuridica che fornisce
  soluzioni di portafoglio). Le righe di art. 8, art. 9 §1-§7, art. 10 §1-§3,
  art. 11 §1-§3, art. 12 §2-§3, art. 13 e art. 14 §1-§2 nominano il fornitore
  (o il soggetto tecnico di cui esso risponde: le istanze di portafoglio, le
  unita' di portafoglio, le soluzioni di portafoglio, le applicazioni per la
  creazione di firme) e sono quindi in capo a lui. Il fornitore resta il
  soggetto obbligato anche nei commi in cui il testo non lo nomina
  espressamente e descrive il comportamento del componente tecnico ("Le
  istanze di portafoglio sono in grado di ...", art. 10 §2; "Le applicazioni
  per la creazione di firme dispongono delle funzioni seguenti:", art. 12
  §2): nessun'altra categoria di soggetto e' nominata come obbligata in
  questa porzione.
- Destinatari (ruolo "destinatario") valorizzati solo dove il testo nomina il
  soggetto a favore del quale il comportamento e' posto: "Utente/titolare" in
  art. 9 §4 (le segnalazioni sono dell'utente), art. 9 §5 (il consenso e'
  dell'utente), art. 9 §7 ("consentono agli utenti ... di esportare"), art. 10
  §3 ("informano l'utente ... in merito all'esito"), art. 11 §1 ("gli utenti
  ... possano ricevere certificati qualificati"), art. 11 §3 (accesso gratuito
  per gli utenti persone fisiche), art. 12 §2 (le funzioni servono l'utente:
  dati forniti dall'utente, informazione degli utenti) e art. 13 (la
  portabilita' serve a consentire all'utente di migrare); "Terzi
  affidanti/pubblico" solo in art. 14 §2, dove lo pseudonimo specifico e'
  fornito alla parte facente affidamento sul portafoglio. Nessun destinatario
  in art. 8, art. 9 §1-§3 e §6, art. 10 §1-§2, art. 11 §2, art. 12 §3: il testo
  non nomina un beneficiario e la categoria non viene inferita (meglio
  omettere che forzare).
- Tipo di nodo: art. 9 §5 e §6, pur essendo formulati in modo dichiarativo
  ("sono accessibili al fornitore ...", "rimangono accessibili fintantoche'"),
  sono Obblighi e non Principi: il primo subordina l'accesso del fornitore
  alle registrazioni a un consenso preventivo esplicito dell'utente e il
  secondo impone di mantenere le registrazioni accessibili per il periodo
  richiesto dal diritto dell'Unione o interno, cioe' vincolano il
  comportamento del fornitore (che e' il soggetto obbligato, come per le altre
  righe dell'art. 9). Art. 12 §1 ("Le applicazioni per la creazione di firme
  ... possono essere fornite da fornitori di portafogli, da prestatori di
  servizi fiduciari o da parti facenti affidamento sul portafoglio") e' invece
  un Principio, tipo "altro": attribuisce una facolta' a tre categorie di
  soggetti senza imporre alcun comportamento (stesso trattamento riservato
  dall'art. 5 §4 del Reg. 2025/1569 alla facolta' della Commissione di
  chiedere informazioni supplementari agli Stati membri).
- Art. 12 §3 e' un comma misto: il primo periodo e' una facolta' ("possono
  essere integrate in istanze di portafoglio o essere esterne a queste
  ultime"), il secondo una prescrizione con soggetto ("le applicazioni ...
  supportano l'interfaccia di programmazione di un'applicazione di cui
  all'allegato IV"). Poiche' un comma e' coperto da una sola riga, il nodo e'
  un Obbligo (la frase prescrittiva e' la seconda) e la facolta' resta
  integralmente nel `testo_integrale` e richiamata nel `testo` (stesso criterio
  dell'art. 3 §2 del Reg. 2025/1569).
- tipo_obbligo: "di conservazione" per art. 9 §1, §2, §4 e §6 (registrazione e
  conservazione delle transazioni: stessa famiglia dei nodi "event logs" di
  ETSI TS 119 101, clausola 7.6, gia' censiti come "di conservazione"); "tecnico/sicurezza" per
  art. 9 §3 (integrita', autenticita' e riservatezza delle registrazioni), art.
  8, art. 10 §1-§2 (capacita' tecniche delle unita' di portafoglio), art. 11
  §1-§2 (certificati qualificati e dispositivi per la creazione di firme), art.
  12 §2-§3 (funzioni e interfaccia delle applicazioni di firma) e art. 14 §1-§2
  (generazione di pseudonimi); "procedurale" per art. 9 §5 (condizione di
  accesso subordinata al consenso preventivo esplicito dell'utente: come la
  condizione di consenso gia' censita in ETSI EN 319 102 come "procedurale");
  "informativo/trasparenza" per art. 10 §3 (verifica della parte facente
  affidamento + informazione dell'utente sull'esito: il riscontro verso
  l'utente e' il precetto che caratterizza il comma, e la verifica delle
  politiche di divulgazione incorporate e' gia' coperta da art. 10 §1-§2);
  "organizzativo" per art. 9 §7, art. 11 §3 e art. 13, allineati ai nodi
  corrispondenti di eIDAS2 art. 5 bis §4(f) (scaricare i propri dati), §4(g)
  (portabilita') e §5(g) (accesso gratuito per le persone fisiche), censiti
  come "organizzativo" in `seed.py`: sono prestazioni del fornitore al livello
  del servizio, non controlli tecnici puntuali, e mantenerne la stessa
  classificazione evita un'incoerenza tra la norma madre e il suo atto di
  esecuzione.
- `condizione_applicabilita`: valorizzata dove il testo pone una condizione
  esplicita - art. 9 §5 (accesso ammesso solo ove necessario per la
  prestazione dei servizi di portafoglio e sulla base del consenso preventivo
  esplicito dell'utente), art. 11 §3 (utenti che sono persone fisiche, quanto
  meno per fini non professionali), art. 12 §3 (applicazioni che fanno
  affidamento su dispositivi qualificati per la creazione di firme a distanza
  e sono integrate nelle istanze di portafoglio), art. 13 (laddove tecnicamente
  fattibile e fatta eccezione per i casi di risorse critiche). Non valorizzata
  in art. 9 §6: il comma non pone una condizione di applicabilita' ma una
  durata (il periodo richiesto dal diritto dell'Unione o dal diritto interno),
  che e' riportata nel `testo`.
- `testo_integrale`: verbatim e integrale, ricucito dalle righe spezzate dalla
  conversione XHTML -> testo. Per ogni articolo include l'intestazione e la
  rubrica ("Articolo N" + titolo), che nel testo ufficiale precedono
  immediatamente il corpo della prima riga dell'articolo (convenzione dei
  moduli gemelli del Reg. 2025/1569 e del Reg. 2025/2531); per i commi
  successivi al primo dello stesso articolo l'intestazione non e' ripetuta,
  perche' nel testo ufficiale non li precede e ripeterla renderebbe il testo
  non contiguo alla fonte. I marcatori di lettera isolati su riga propria dalla
  conversione ("a)", "b)", ...) sono riuniti al testo della rispettiva lettera
  ("a) l'ora e la data della transazione;") e le lettere sono separate da riga
  vuota, sciogliendo la spaziatura della conversione. Nessun marcatore di
  elisione (vincolo `verifica_completezza_testo_integrale`, ADR-0010).
- `testo` e' la sintesi compressa (1-3 frasi): per art. 9 §2 e art. 12 §2
  riassume le lettere senza sostituirsi al `testo_integrale`, che le riporta
  per intero. Nessuna riga valorizza `severita` o `sanzioni`: l'atto non
  gradua i requisiti ne' prevede sanzioni proprie.
- `stato` = "vigente" per tutte le righe (il regolamento e' in vigore).
- RELAZIONI: solo relazioni INTERNE a questa Fonte, con `fonte_id_o_None` =
  None su entrambi gli estremi. Otto relazioni "richiama" con
  `evidence_type` = "textual", ciascuna verificata su una citazione letterale
  del testo: art. 9 §5 -> art. 9 §1 e art. 9 §2 e art. 9 §6 -> art. 9 §1 e §2
  ("Le registrazioni di cui ai paragrafi 1 e 2"), art. 9 §7 -> art. 9 §2
  ("le informazioni registrate di cui al paragrafo 2"), art. 10 §2 -> art. 10
  §1 ("tali politiche di divulgazione incorporate di cui al paragrafo 1"), art.
  11 §2 -> art. 11 §1 e art. 11 §3 -> art. 11 §1 ("i certificati qualificati di
  cui al paragrafo 1"). Una relazione "specifica" con `evidence_type` =
  "inferred": art. 9 §2 rende operativo l'obbligo generale di registrazione di
  art. 9 §1 indicando il contenuto minimo delle registrazioni (nessuna
  citazione letterale del paragrafo 1, quindi non "textual"). `confidence` non
  e' valorizzata (None) su nessuna relazione: non esiste uno score reale da
  riportare e inventarlo falserebbe la provenienza dell'arco (ADR-0005).
  Nessuna relazione verso altre Fonti (il collegamento cross-fonte e' la fase
  ADR-0009 della sessione principale: tentarlo durante il merge parallelo per
  capitolo causa KeyError sul registro) e nessuna relazione verso i nodi degli
  allegati I-V di questa stessa Fonte, che stanno nel capitolo 5 (rinvii
  testuali presenti in questa porzione: art. 8 -> allegato II, art. 10 §1 ->
  allegato III, art. 12 §2(c) e art. 12 §3 -> allegato IV, art. 14 §1 ->
  allegato V). Motivo: il capitolo 5 indicizza gli allegati a granularita' piu'
  fine (punti e voci: "allegato III, punto 1", "allegato IV, punto 2", ...),
  quindi un rinvio all'allegato nel suo complesso non ha necessariamente un
  nodo corrispondente, e i riferimenti del capitolo 5 non sono congelati
  mentre i capitoli della Fonte vengono scritti in parallelo: un riferimento
  sbagliato farebbe fallire l'intero import con KeyError a fronte di un
  beneficio nullo (stesso criterio dichiarato dal modulo cap01 di questa
  Fonte). Questi rinvii li costruisce la sessione principale dopo il merge dei
  capitoli, quando i riferimenti di tutti i moduli sono finali.

Copertura: 28 item di indice (art. 8; art. 9 §1-§7 con le lettere di §2; art.
10 §1-§3; art. 11 §1-§3; art. 12 §1-§3 con le lettere di §2; art. 13; art. 14
§1-§2), 20 righe (19 Obblighi + 1 Principio).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 8",
        "testo": "I fornitori di portafogli garantiscono che le soluzioni di portafoglio supportino l'utilizzo di dati di identificazione personale e attestati elettronici di attributi rilasciati in conformità all'elenco di norme di cui all'allegato II.",
        "testo_integrale": "Articolo 8\n\nFormati per i dati di identificazione personale e per gli attestati elettronici di attributi\n\nI fornitori di portafogli garantiscono che le soluzioni di portafoglio supportino l'utilizzo di dati di identificazione personale e attestati elettronici di attributi rilasciati in conformità all'elenco di norme di cui all'allegato II.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 9 §1",
        "testo": "Indipendentemente dal fatto che una transazione sia completata o meno, le istanze di portafoglio registrano tutte le transazioni con le parti facenti affidamento sul portafoglio e altre unità di portafoglio, comprese l'apposizione di firme e sigilli elettronici.",
        "testo_integrale": "Articolo 9\n\nRegistrazioni di transazioni\n\n1. Indipendentemente dal fatto che una transazione sia completata o meno, le istanze di portafoglio registrano tutte le transazioni con le parti facenti affidamento sul portafoglio e altre unità di portafoglio, comprese l'apposizione di firme e sigilli elettronici.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 9 §2",
        "testo": "Le informazioni registrate figurano come minimo: l'ora e la data della transazione; il nome, i dati di contatto e l'identificatore univoco della corrispondente parte facente affidamento sul portafoglio e dello Stato membro in cui è stabilita o, per altre unità di portafoglio, le informazioni pertinenti desunte dall'attestato di unità di portafoglio; il tipo o i tipi di dati richiesti e presentati nel contesto della transazione; il motivo del mancato completamento per le transazioni non completate.",
        "testo_integrale": "2. Tra le informazioni registrate figurano come minimo:\n\na) l'ora e la data della transazione;\n\nb) il nome, i dati di contatto e l'identificatore univoco della corrispondente parte facente affidamento sul portafoglio e dello Stato membro in cui tale parte è stabilita o, nel caso di altre unità di portafoglio, le informazioni pertinenti desunte dall'attestato di unità di portafoglio;\n\nc) il tipo o i tipi di dati richiesti e presentati nel contesto della transazione;\n\nd) nel caso di transazioni non completate, il motivo di tale mancato completamento.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 9 §3",
        "testo": "I fornitori di portafogli garantiscono l'integrità, l'autenticità e la riservatezza delle informazioni registrate.",
        "testo_integrale": "3. I fornitori di portafogli garantiscono l'integrità, l'autenticità e la riservatezza delle informazioni registrate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 9 §4",
        "testo": "Le istanze di portafoglio registrano le segnalazioni inviate dall'utente del portafoglio alle autorità di protezione dei dati attraverso la loro unità di portafoglio.",
        "testo_integrale": "4. Le istanze di portafoglio registrano le segnalazioni inviate dall'utente del portafoglio alle autorità di protezione dei dati attraverso la loro unità di portafoglio.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 9 §5",
        "testo": "Le registrazioni di cui ai paragrafi 1 e 2 sono accessibili al fornitore del portafoglio, ove necessario per la prestazione di servizi di portafoglio, sulla base di un consenso preventivo esplicito prestato dall'utente del portafoglio.",
        "testo_integrale": "5. Le registrazioni di cui ai paragrafi 1 e 2 sono accessibili al fornitore del portafoglio, ove necessario per la prestazione di servizi di portafoglio, sulla base di un consenso preventivo esplicito prestato dall'utente del portafoglio.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "L'accesso del fornitore del portafoglio alle registrazioni è ammesso solo ove necessario per la prestazione di servizi di portafoglio e sulla base di un consenso preventivo esplicito prestato dall'utente del portafoglio.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 9 §6",
        "testo": "Le registrazioni di cui ai paragrafi 1 e 2 rimangono accessibili fintantoché ciò è richiesto dal diritto dell'Unione o dal diritto interno.",
        "testo_integrale": "6. Le registrazioni di cui ai paragrafi 1 e 2 rimangono accessibili fintantoché ciò è richiesto dal diritto dell'Unione o dal diritto interno.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 9 §7",
        "testo": "I fornitori di portafogli consentono agli utenti del portafoglio di esportare le informazioni registrate di cui al paragrafo 2.",
        "testo_integrale": "7. I fornitori di portafogli consentono agli utenti del portafoglio di esportare le informazioni registrate di cui al paragrafo 2.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 10 §1",
        "testo": "I fornitori di portafogli garantiscono che gli attestati elettronici di attributi con politiche di divulgazione incorporate comuni di cui all'allegato III possano essere trattati dalle unità di portafoglio che forniscono.",
        "testo_integrale": "Articolo 10\n\nDivulgazione incorporata\n\n1. I fornitori di portafogli garantiscono che gli attestati elettronici di attributi con politiche di divulgazione incorporate comuni di cui all'allegato III possano essere trattati dalle unità di portafoglio che forniscono.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 §2",
        "testo": "Le istanze di portafoglio sono in grado di elaborare e presentare le politiche di divulgazione incorporate di cui al paragrafo 1 in combinazione con i dati ricevuti dalla parte facente affidamento sul portafoglio.",
        "testo_integrale": "2. Le istanze di portafoglio sono in grado di elaborare e presentare tali politiche di divulgazione incorporate di cui al paragrafo 1 in combinazione con i dati ricevuti dalla parte facente affidamento sul portafoglio.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 §3",
        "testo": "Le istanze di portafoglio verificano se la parte facente affidamento sul portafoglio soddisfa i requisiti della politica di divulgazione incorporata e informano l'utente del portafoglio in merito all'esito di tale verifica.",
        "testo_integrale": "3. Le istanze di portafoglio verificano se la parte facente affidamento sul portafoglio soddisfa i requisiti della politica di divulgazione incorporata e informano l'utente del portafoglio in merito all'esito di tale verifica.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 11 §1",
        "testo": "I fornitori di portafogli garantiscono che gli utenti del portafoglio possano ricevere certificati qualificati per firme elettroniche qualificate o sigilli elettronici qualificati collegati a dispositivi per la creazione di firme qualificate o sigilli qualificati che sono locali, esterne/i o remote/i in relazione alle istanze di portafoglio.",
        "testo_integrale": "Articolo 11\n\nFirme e sigilli elettronici qualificati\n\n1. I fornitori di portafogli garantiscono che gli utenti del portafoglio possano ricevere certificati qualificati per firme elettroniche qualificate o sigilli elettronici qualificati collegati a dispositivi per la creazione di firme qualificate o sigilli qualificati che sono locali, esterne/i o remote/i in relazione alle istanze di portafoglio.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 11 §2",
        "testo": "I fornitori di portafogli garantiscono che le soluzioni di portafoglio siano in grado di interfacciarsi in modo sicuro con uno dei tipi seguenti di dispositivi per la creazione di firme qualificate o sigilli qualificati: dispositivi per la creazione di firme qualificate o sigilli qualificati locali, esterni o gestiti a distanza ai fini dell'utilizzo dei certificati qualificati di cui al paragrafo 1.",
        "testo_integrale": "2. I fornitori di portafogli garantiscono che le soluzioni di portafoglio siano in grado di interfacciarsi in modo sicuro con uno dei tipi seguenti di dispositivi per la creazione di firme qualificate o sigilli qualificati: dispositivi per la creazione di firme qualificate o sigilli qualificati locali, esterni o gestiti a distanza ai fini dell'utilizzo dei certificati qualificati di cui al paragrafo 1.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 §3",
        "testo": "I fornitori di portafogli garantiscono che gli utenti del portafoglio che sono persone fisiche dispongano, quanto meno per fini non professionali, di un accesso gratuito alle applicazioni per la creazione di firme che consentono la creazione di firme elettroniche qualificate gratuite utilizzando i certificati di cui al paragrafo 1.",
        "testo_integrale": "3. I fornitori di portafogli garantiscono che gli utenti del portafoglio che sono persone fisiche dispongano, quanto meno per fini non professionali, di un accesso gratuito alle applicazioni per la creazione di firme che consentono la creazione di firme elettroniche qualificate gratuite utilizzando i certificati di cui al paragrafo 1.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica agli utenti del portafoglio che sono persone fisiche, quanto meno per fini non professionali.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 12 §2",
        "testo": "Le applicazioni per la creazione di firme dispongono delle funzioni seguenti: apposizione di una firma o di un sigillo su dati forniti dall'utente del portafoglio; apposizione di una firma o di un sigillo su dati forniti dalla parte facente affidamento sulla certificazione; creazione di firme o sigilli come minimo nei formati obbligatori di cui all'allegato IV; informazione degli utenti del portafoglio in merito al risultato del processo di creazione della firma o del sigillo.",
        "testo_integrale": "2. Le applicazioni per la creazione di firme dispongono delle funzioni seguenti:\n\na) apposizione di una firma o di un sigillo su dati forniti dall'utente del portafoglio;\n\nb) apposizione di una firma o di un sigillo su dati forniti dalla parte facente affidamento sulla certificazione;\n\nc) creazione di firme o sigilli come minimo nei formati obbligatori di cui all'allegato IV;\n\nd) informazione degli utenti del portafoglio in merito al risultato del processo di creazione della firma o del sigillo.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 12 §3",
        "testo": "Le applicazioni per la creazione di firme possono essere integrate in istanze di portafoglio o essere esterne a queste ultime; qualora facciano affidamento su dispositivi qualificati per la creazione di firme a distanza e siano integrate nelle istanze di portafoglio, supportano l'interfaccia di programmazione di un'applicazione di cui all'allegato IV.",
        "testo_integrale": "3. Le applicazioni per la creazione di firme possono essere integrate in istanze di portafoglio o essere esterne a queste ultime. Qualora facciano affidamento su dispositivi qualificati per la creazione di firme a distanza e siano integrate nelle istanze di portafoglio, le applicazioni per la creazione di firme supportano l'interfaccia di programmazione di un'applicazione di cui all'allegato IV.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Il supporto dell'interfaccia di programmazione di un'applicazione di cui all'allegato IV è dovuto solo qualora le applicazioni per la creazione di firme facciano affidamento su dispositivi qualificati per la creazione di firme a distanza e siano integrate nelle istanze di portafoglio.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 13",
        "testo": "Laddove tecnicamente fattibile e fatta eccezione per i casi di risorse critiche, le unità di portafoglio supportano l'esportazione sicura e la portabilità dei dati personali dell'utente del portafoglio al fine di consentire a quest'ultimo di migrare verso un'unità di portafoglio di una soluzione di portafoglio diversa in un modo che assicuri un livello di garanzia elevato di cui al regolamento di esecuzione (UE) 2015/1502.",
        "testo_integrale": "Articolo 13\n\nEsportazione e portabilità dei dati\n\nLaddove tecnicamente fattibile e fatta eccezione per i casi di risorse critiche, le unità di portafoglio supportano l'esportazione sicura e la portabilità dei dati personali dell'utente del portafoglio al fine di consentire a quest'ultimo di migrare verso un'unità di portafoglio di una soluzione di portafoglio diversa in un modo che assicuri un livello di garanzia elevato di cui al regolamento di esecuzione (UE) 2015/1502.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica laddove tecnicamente fattibile e fatta eccezione per i casi di risorse critiche.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 14 §1",
        "testo": "Le unità di portafoglio supportano la generazione di pseudonimi per gli utenti del portafoglio conformemente alle specifiche tecniche di cui all'allegato V.",
        "testo_integrale": "Articolo 14\n\nPseudonimi\n\n1. Le unità di portafoglio supportano la generazione di pseudonimi per gli utenti del portafoglio conformemente alle specifiche tecniche di cui all'allegato V.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 14 §2",
        "testo": "Le unità di portafoglio supportano la generazione, su richiesta di una parte facente affidamento sul portafoglio, di uno pseudonimo specifico e unico per tale parte e forniscono detto pseudonimo alla parte facente affidamento sul portafoglio o da solo, o in combinazione con qualsiasi dato di identificazione personale o attestato elettronico di attributi richiesto da tale parte.",
        "testo_integrale": "2. Le unità di portafoglio supportano la generazione, su richiesta di una parte facente affidamento sul portafoglio, di uno pseudonimo specifico e unico per tale parte e forniscono detto pseudonimo alla parte facente affidamento sul portafoglio o da solo, o in combinazione con qualsiasi dato di identificazione personale o attestato elettronico di attributi richiesto da tale parte.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 12 §1",
        "testo": "Le applicazioni per la creazione di firme utilizzate dalle unità di portafoglio possono essere fornite da fornitori di portafogli, da prestatori di servizi fiduciari o da parti facenti affidamento sul portafoglio.",
        "testo_integrale": "Articolo 12\n\nApplicazioni per la creazione di firme\n\n1. Le applicazioni per la creazione di firme utilizzate dalle unità di portafoglio possono essere fornite da fornitori di portafogli, da prestatori di servizi fiduciari o da parti facenti affidamento sul portafoglio.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 8",
    "art. 9 §1",
    "art. 9 §2",
    "art. 9 §2(a)",
    "art. 9 §2(b)",
    "art. 9 §2(c)",
    "art. 9 §2(d)",
    "art. 9 §3",
    "art. 9 §4",
    "art. 9 §5",
    "art. 9 §6",
    "art. 9 §7",
    "art. 10 §1",
    "art. 10 §2",
    "art. 10 §3",
    "art. 11 §1",
    "art. 11 §2",
    "art. 11 §3",
    "art. 12 §1",
    "art. 12 §2",
    "art. 12 §2(a)",
    "art. 12 §2(b)",
    "art. 12 §2(c)",
    "art. 12 §2(d)",
    "art. 12 §3",
    "art. 13",
    "art. 14 §1",
    "art. 14 §2",
]

MAPPATURA_LOCALE = {
    "art. 8": ["art. 8"],
    "art. 9 §1": ["art. 9 §1"],
    "art. 9 §2": [
        "art. 9 §2",
        "art. 9 §2(a)",
        "art. 9 §2(b)",
        "art. 9 §2(c)",
        "art. 9 §2(d)",
    ],
    "art. 9 §3": ["art. 9 §3"],
    "art. 9 §4": ["art. 9 §4"],
    "art. 9 §5": ["art. 9 §5"],
    "art. 9 §6": ["art. 9 §6"],
    "art. 9 §7": ["art. 9 §7"],
    "art. 10 §1": ["art. 10 §1"],
    "art. 10 §2": ["art. 10 §2"],
    "art. 10 §3": ["art. 10 §3"],
    "art. 11 §1": ["art. 11 §1"],
    "art. 11 §2": ["art. 11 §2"],
    "art. 11 §3": ["art. 11 §3"],
    "art. 12 §1": ["art. 12 §1"],
    "art. 12 §2": [
        "art. 12 §2",
        "art. 12 §2(a)",
        "art. 12 §2(b)",
        "art. 12 §2(c)",
        "art. 12 §2(d)",
    ],
    "art. 12 §3": ["art. 12 §3"],
    "art. 13": ["art. 13"],
    "art. 14 §1": ["art. 14 §1"],
    "art. 14 §2": ["art. 14 §2"],
}

# Relazioni INTERNE a questa Fonte (fonte_id_o_None = None su entrambi gli
# estremi). Le otto "richiama" sono citazioni letterali verificate sul testo
# ("di cui ai paragrafi 1 e 2", "di cui al paragrafo 2", "di cui al paragrafo
# 1": evidence_type "textual"); la "specifica" e' dedotta dal rapporto tra
# l'obbligo generale di registrazione (art. 9 §1) e il contenuto minimo delle
# registrazioni che lo rende operativo (art. 9 §2): evidence_type "inferred".
# `confidence` resta None su tutte: nessuno score reale da riportare.
RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "art. 9 §2"),
        "nodo_a": ("obbligo", None, "art. 9 §1"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 §5"),
        "nodo_a": ("obbligo", None, "art. 9 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 §5"),
        "nodo_a": ("obbligo", None, "art. 9 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 §6"),
        "nodo_a": ("obbligo", None, "art. 9 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 §6"),
        "nodo_a": ("obbligo", None, "art. 9 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 §7"),
        "nodo_a": ("obbligo", None, "art. 9 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 10 §2"),
        "nodo_a": ("obbligo", None, "art. 10 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 11 §2"),
        "nodo_a": ("obbligo", None, "art. 11 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 11 §3"),
        "nodo_a": ("obbligo", None, "art. 11 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
