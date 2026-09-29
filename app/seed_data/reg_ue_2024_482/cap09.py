"""Regolamento di esecuzione (UE) 2024/482 della Commissione, del 31 gennaio
2024 - modalita' di applicazione del regolamento (UE) 2019/881 del Parlamento
europeo e del Consiglio per quanto riguarda l'adozione del sistema europeo di
certificazione della cibersicurezza basato sui criteri comuni (EUCC). Fonte 29
(slug `reg_ue_2024_482`), capitolo 9 di 14 (vedi
app/.source_cache/reg_ue_2024_482/manifest.json): Allegati I-II - settori
tecnici e documenti sullo stato dell'arte (allegato I) e profili di protezione
certificati al livello AVA_VAN 4 o 5 (allegato II). Gli artt. 1-50 e gli
allegati III-IX appartengono ai capitoli 1-8 e 10-14 della stessa Fonte,
assegnati ad altri moduli: nessuno di quei file e' toccato qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_482/cap09.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R0482, lingua italiana; URL
risolto
http://publications.europa.eu/resource/cellar/687c0d05-c580-11ee-95d9-01aa75ed71a1.0014.03/DOC_1,
XHTML della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 135.367
caratteri di testo, sha256 del raw.txt
b46d08cab6d63b2c190ae767042c07c1fc324955c22ef491eb314556b28ca5b8 - dettagli
completi in app/.source_cache/reg_ue_2024_482/provenance.json). La porzione e'
l'ultima del documento dopo gli artt. 1-50: non contiene preambolo
(considerando, a monte del Capo I), epigrafe, firma, note a pie' di pagina ne'
formula di chiusura (la formula "obbligatorio in tutti i suoi elementi e
direttamente applicabile in ciascuno degli Stati membri", la firma e le note a
pie' di pagina (1)-(5) stanno in coda all'art. 50, quindi nel cap08), e la riga
ELI / "ISSN 1977-0707 (electronic edition)" chiude il documento dopo
l'allegato IX (cap14): nessuno di questi elementi produce nodo o item di
indice in questo modulo.

Modellazione (ADR-0007, nessun discrimine di rilevanza):
- Paratesto -> nessun nodo: le intestazioni "ALLEGATO I" e "ALLEGATO II" e i
  loro titoli ("Tettori tecnici e documenti sullo stato dell'arte", "Profili di
  protezione certificati al livello AVA_VAN 4 o 5") sono struttura dell'atto,
  non punti numerati, lettere o voci: non producono item di indice e non sono
  assorbiti nel `testo_integrale` delle righe (stesso trattamento dei titoli
  degli allegati del Reg. 2025/1569 cap03 e delle intestazioni di capitolo di
  questa stessa Fonte). Il titolo dell'allegato I reca un refuso della Gazzetta
  ufficiale italiana ("Tettori" per "Settori"), riprodotto tale e quale dalla
  fonte ufficiale e non corretto (ADR-0010); non essendo unita' normativa non
  entra nel grafo, ma e' segnalato qui perche' chi legge il testo ufficiale lo
  incontra.
- Unita' di copertura: i due punti numerati di ciascun allegato ("1." e "2."),
  con le loro lettere e i loro elenchi numerati. Allegato I -> 2 righe (punto 1
  con le due lettere (a) e (b) e i dieci documenti; punto 2 con la lettera (a));
  allegato II -> 2 righe (punto 1 con i due profili di protezione; punto 2, il
  cui elenco e' il segnaposto [BLANK] della Gazzetta ufficiale). Nessun item a
  livello di allegato ("allegato I" / "allegato II"): qui i punti sono numerati,
  la convenzione del censimento riserva l'item a livello di allegato ai testi
  che non numerano i punti, e un item unico non sarebbe mappabile su due righe
  distinte (stesso criterio dell'allegato III del Reg. 2024/2979 cap05).
  Item di indice: "allegato I, punto 1", "allegato I, punto 1(a)", "allegato I,
  punto 1(a)(1)" fino a "1(a)(7)", "allegato I, punto 1(b)", "allegato I, punto
  1(b)(1)" fino a "1(b)(3)", "allegato I, punto 2", "allegato I, punto 2(a)",
  "allegato II, punto 1", "allegato II, punto 1(1)", "allegato II, punto 1(2)",
  "allegato II, punto 2": 19 item, 4 righe.
- Allegato I, punto 1 (chapeau "Settori tecnici al livello AVA_VAN 4 o 5:" con
  le lettere (a) settore tecnico «smart card e dispositivi simili» e (b) settore
  tecnico «dispositivi hardware con box di sicurezza», per un totale di dieci
  documenti di valutazione armonizzata) -> UNA sola riga Principio "altro".
  Le due lettere sono frammenti nominali ("documenti relativi alla valutazione
  armonizzata del settore tecnico «smart card e dispositivi simili» e in
  particolare i seguenti documenti, nelle rispettive versioni in vigore il
  [data di entrata in vigore]:", e la formula corrispondente per il settore dei
  dispositivi hardware con box di sicurezza), senza verbo proprio e retti dal
  chapeau del punto: nessuna delle due ha precetto autonomo, quindi non
  producono righe proprie e restano nel `testo_integrale` della riga (con i
  loro item di indice separati). Scelta dichiarata in
  attuazione della nota del capitolo ("gli elenchi di documenti possono
  richiedere una riga per punto e non una per ciascun documento citato"): i
  dieci documenti non hanno precetti distinti al loro interno - sono designati
  tutti con la stessa formula ("inizialmente approvato dall'ECCG il 20 ottobre
  2023") e si differenziano solo per il titolo e per il settore tecnico di
  appartenenza -, quindi una riga per documento avrebbe duplicato dieci volte
  la stessa designazione. Alternativa considerata e scartata: una riga per
  lettera (a) e (b); le due lettere sono i due rami della stessa designazione
  ("i settori tecnici al livello AVA_VAN 4 o 5") e il chapeau che le regge non
  ha contenuto proprio, per cui spezzarle avrebbe richiesto una terza riga di
  solo chapeau, senza guadagno di informazione. Dubbio di classificazione
  dichiarato: Obbligo "tecnico/sicurezza" con soggetto "Terza parte" (gli
  ITSEF) sarebbe sostenibile leggendo il punto insieme all'art. 7 §1(d) e §3(a)
  di questa Fonte (cap02), che impongono di valutare il prodotto TIC
  conformemente ai documenti sullo stato dell'arte applicabili di cui
  all'allegato I; scelto il Principio perche' l'allegato non nomina alcun
  soggetto ne' enuncia un precetto: e' una designazione di documenti di
  riferimento, con la stessa classificazione dell'elenco di norme
  dell'allegato I del Reg. 2024/2979 cap05 e della designazione di norma di
  riferimento dell'allegato punto 3(a) del Reg. 2025/2531.
- Allegato I, punto 2 ("Documenti sullo stato dell'arte nelle rispettive
  versioni in vigore il [data di entrata in vigore]:", lettera (a) con il
  documento "Accreditation of ITSEFs for the EUCC") -> UNA sola riga Principio
  "altro", item "allegato I, punto 2" e "allegato I, punto 2(a)": stessa
  designazione di documenti di riferimento del punto 1 (qui un solo documento,
  quindi il rapporto riga/item e' uno a due per la presenza della lettera).
- Allegato II, punto 1 ("Per la categoria dei dispositivi qualificati per la
  creazione di firme e sigilli a distanza:", con i due profili di protezione
  EN 419241-2:2019 e EN 419221-5:2018) -> UNA sola riga Principio "altro":
  designa i profili di protezione certificati al livello AVA_VAN 4 o 5
  applicabili a quella categoria, senza comportamento imposto ne' soggetto
  nominato. Dubbio di classificazione dichiarato: Obbligo "tecnico/sicurezza"
  sarebbe sostenibile sulla base dell'art. 7 §1(e) e §3(b) (cap02), che
  impongono di valutare il prodotto TIC conformemente alla metodologia
  specificata per il profilo di protezione che figura nell'allegato II; vale
  qui la stessa ragione del punto 1 dell'allegato I. `oggetti_giuridici`
  valorizzato, perche' la categoria nominata dal chapeau corrisponde a due
  valori censiti: "dispositivo qualificato di creazione di firma elettronica" e
  "dispositivo qualificato di creazione di sigillo elettronico".
- Allegato II, punto 2 ("Profili di protezione che sono stati adottati come
  documenti sullo stato dell'arte:") -> UNA sola riga Principio "altro", item
  "allegato II, punto 2" e nessun item per un elenco che non esiste: la
  Gazzetta ufficiale italiana pubblica in luogo dei profili il segnaposto
  letterale "[BLANK]" (verificato sull'XHTML CELLAR della stessa acquisizione:
  `<p class="oj-normal">[BLANK]</p>` subito dopo il chapeau del punto, nella
  stessa divisione di enumerazione dei punti dell'allegato). Il segnaposto e'
  riportato verbatim nel `testo_integrale`, perche' e' contenuto ufficiale e
  non un'elisione introdotta in estrazione: la guardia
  `verifica_completezza_testo_integrale` cerca i marcatori di troncamento (i
  puntini di sospensione e l'ellissi racchiusa fra parentesi quadre) e
  "[BLANK]" non e' nessuno di essi. Nessun `testo` alternativo e' stato
  costruito a memoria: il punto resta censito per quello che la fonte pubblica,
  senza inventare i profili mancanti.
- Segnaposto "[data di entrata in vigore]": ricorre tre volte (punto 1 lettere
  (a) e (b) e punto 2 dell'allegato I) e la Gazzetta ufficiale lo pubblica
  cosi', letteralmente, in luogo della data. Riportato verbatim e non
  interpretato: l'art. 50 §2 di questa Fonte (cap08) fissa al 27 febbraio 2025
  la data di applicazione del regolamento, ma sostituire il segnaposto con
  quella data sarebbe una ricostruzione del modello, non il testo pubblicato
  (ADR-0010).
- Documenti e norme citati negli allegati (i dieci documenti SOG-IS/ECCG del
  punto 1 e il documento di accreditamento del punto 2 dell'allegato I; le
  norme EN 419241-2:2019 e EN 419221-5:2018 dell'allegato II) NON ricevono
  nodi propri e non producono relazioni: non sono Fonti del censimento (le
  norme EN 419xxx per i dispositivi qualificati di firma e sigillo non risultano
  fra le Fonti censite in docs/fonti-censite.md). Restano integralmente nel
  `testo_integrale` delle righe che li designano.
- `testo_integrale`: verbatim e integrale, ricucito dalle righe spezzate dalla
  conversione XHTML -> testo. I marcatori isolati su riga propria del dump
  ("1.", "2.", "(a)", "(b)" e le voci numerate da "(1)" a "(7)") sono
  riuniti al testo che seguono, per esempio "1. Settori tecnici al livello
  AVA_VAN 4 o 5:" e "(a) documenti relativi alla valutazione armonizzata del
  settore tecnico «smart card e dispositivi simili» e in particolare i seguenti
  documenti, nelle rispettive versioni in vigore il [data di entrata in
  vigore]:"; ogni punto, lettera o voce numerata resta in un blocco separato da
  riga vuota nell'ordine del testo ufficiale. Nessun marcatore di elisione
  (vincolo `verifica_completezza_testo_integrale`, ADR-0010). `testo` e'
  invece la sintesi compressa (1-3 frasi) di ogni riga, che nomina i documenti
  e le norme designati per renderli cercabili senza aprire l'integrale.
- Nessuna riga valorizza `severita`, `sanzioni` o `condizione_applicabilita`:
  l'atto non gradua i requisiti ne' prevede sanzioni proprie (stessa scelta
  degli altri atti di esecuzione gia' censiti), e la condizione di
  applicabilita' delle designazioni (valutazioni al livello AVA_VAN 4 o 5
  nell'ambito dell'EUCC) e' enunciata dagli stessi allegati e dagli articoli
  che li richiamano, non da un fatto esterno non tracciato. `stato` =
  "vigente" per tutte le righe. Nessun `oggetti_giuridici` sulle due righe
  dell'allegato I: fra i valori censiti non ce n'e' uno che corrisponda a
  "prodotto TIC" o a "settore tecnico" e la voce generica "altro" non e' stata
  forzata (stesso criterio del Reg. 2024/2979 cap02 e del cap01 di questa
  Fonte).
- RELAZIONI = []: le quattro righe di questa porzione non si citano a vicenda
  (nessun rinvio letterale interno agli allegati I e II) e le relazioni verso
  altri capitoli della stessa Fonte o verso altre Fonti le costruisce la
  sessione principale in fase 6, non questo modulo (dichiararle qui, in import
  parallelo per capitolo, imporrebbe di indovinare i `riferimento` dei nodi
  scritti da altri moduli e un riferimento sbagliato fa fallire il seed con
  KeyError).
- Rinvii demandati alla fase 6 (nessuna relazione dichiarata qui; accanto a
  ogni rinvio letterale e' indicato il `riferimento` con cui il nodo bersaglio
  e' dichiarato nel modulo del capitolo che lo contiene, per evitare KeyError
  in fase 6): art. 7 §1(d), §1(e) -> riga "art. 7 §1" (cap02); art. 7 §3(a) e
  §3(b) -> riga "art. 7 §3" (cap02); art. 15 §1(c) -> riga "art. 15 §1"
  (cap03); art. 15 §2 (regime eccezionale di mancata applicazione dei documenti
  sullo stato dell'arte) -> riga "art. 15 §2" (cap03); art. 22 §1(b)(2) -> riga
  "art. 22 §1" (cap04); art. 34 §2 -> riga "art. 34 §2" (cap06); art. 42 §1(f)
  -> riga "art. 42 §1" (cap07); art. 48 §2 e §3 (parere di approvazione del
  gruppo europeo per la certificazione della cibersicurezza e pubblicazione dei
  documenti sullo stato dell'arte da parte dell'ENISA) -> cap08; art. 50 §2
  (data di applicazione del regolamento) -> segnaposto "[data di entrata in
  vigore]" dell'allegato I (cap08). Il considerando che prevede la modifica
  degli allegati I e II secondo la procedura dell'art. 66 §2 del regolamento
  (UE) 2019/881 non e' censito (il preambolo non produce nodi) e non genera
  alcun arco.

Copertura: 19 item di indice, 4 righe (0 Obblighi + 4 Principi), 0 relazioni
interne.

Dubbi di classificazione rimasti aperti (dichiarati, non risolti in modo
univoco dal testo): (1) le quattro righe sono tutte Principi "altro" perche'
gli allegati designano elenchi senza soggetto e senza verbo; chi volesse
leggere l'effetto prescrittivo degli allegati attraverso gli articoli che li
richiamano (art. 7 §1(d)-§1(e), §3(a)-§3(b) per il cap02; art. 15 §1(c) per il
cap03) otterrebbe Obblighi "tecnico/sicurezza" in capo agli ITSEF e agli
organismi di valutazione della conformita', ma sarebbe un'inferenza costruita
sul rinvio, non sul testo dell'allegato. (2) Allegato I, punto 1 tenuto come
una sola riga per entrambi i settori tecnici: la lettura alternativa (una riga
per settore) e' legittima e lascerebbe invariati gli item di indice, ma
introdurrebbe una riga di solo chapeau; la scelta fatta privilegia la
corrispondenza riga/punto numerato.
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "allegato I, punto 1",
        "testo": "Settori tecnici certificabili al livello AVA_VAN 4 o 5 e documenti per la loro valutazione armonizzata, nelle rispettive versioni in vigore alla data di entrata in vigore (il testo ufficiale pubblica il segnaposto «[data di entrata in vigore]»): per il settore tecnico «smart card e dispositivi simili» i documenti «Minimum ITSEF requirements for security evaluations of smart cards and similar devices», «Minimum Site Security Requirements», «Application of Common Criteria to integrated circuits», «Security Architecture requirements (ADV_ARC) for smart cards and similar devices», «Certification of “open” smart card products», «Composite product evaluation for smart cards and similar devices» e «Application of Attack Potential to Smartcards»; per il settore tecnico «dispositivi hardware con box di sicurezza» i documenti «Minimum ITSEF requirements for security evaluations of hardware devices with security boxes», «Minimum Site Security Requirements» e «Application of Attack Potential to hardware devices with security boxes». Tutti i documenti sono inizialmente approvati dall'ECCG il 20 ottobre 2023.",
        "testo_integrale": "1. Settori tecnici al livello AVA_VAN 4 o 5:\n\n(a) documenti relativi alla valutazione armonizzata del settore tecnico «smart card e dispositivi simili» e in particolare i seguenti documenti, nelle rispettive versioni in vigore il [data di entrata in vigore]:\n\n(1) «Minimum ITSEF requirements for security evaluations of smart cards and similar devices», inizialmente approvato dall'ECCG il 20 ottobre 2023;\n\n(2) «Minimum Site Security Requirements», inizialmente approvato dall'ECCG il 20 ottobre 2023;\n\n(3) «Application of Common Criteria to integrated circuits», inizialmente approvato dall'ECCG il 20 ottobre 2023;\n\n(4) «Security Architecture requirements (ADV_ARC) for smart cards and similar devices», inizialmente approvato dall'ECCG il 20 ottobre 2023;\n\n(5) «Certification of “open” smart card products», inizialmente approvato dall'ECCG il 20 ottobre 2023;\n\n(6) «Composite product evaluation for smart cards and similar devices», inizialmente approvato dall'ECCG il 20 ottobre 2023;\n\n(7) «Application of Attack Potential to Smartcards», inizialmente approvato dall'ECCG il 20 ottobre 2023;\n\n(b) documenti relativi alla valutazione armonizzata del settore tecnico «dispositivi hardware con box di sicurezza» e in particolare i seguenti documenti, nelle rispettive versioni in vigore il [data di entrata in vigore]:\n\n(1) «Minimum ITSEF requirements for security evaluations of hardware devices with security boxes», inizialmente approvato dall'ECCG il 20 ottobre 2023;\n\n(2) «Minimum Site Security Requirements», inizialmente approvato dall'ECCG il 20 ottobre 2023;\n\n(3) «Application of Attack Potential to hardware devices with security boxes», inizialmente approvato dall'ECCG il 20 ottobre 2023.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato I, punto 2",
        "testo": "Documenti sullo stato dell'arte, nelle rispettive versioni in vigore alla data di entrata in vigore (il testo ufficiale pubblica il segnaposto «[data di entrata in vigore]»): il documento sull'accreditamento armonizzato degli organismi di valutazione della conformità «Accreditation of ITSEFs for the EUCC», inizialmente approvato dall'ECCG il 20 ottobre 2023.",
        "testo_integrale": "2. Documenti sullo stato dell'arte nelle rispettive versioni in vigore il [data di entrata in vigore]:\n\n(a) documento relativo all'accreditamento armonizzato degli organismi di valutazione della conformità: «Accreditation of ITSEFs for the EUCC», inizialmente approvato dall'ECCG il 20 ottobre 2023.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato II, punto 1",
        "testo": "Profili di protezione certificati al livello AVA_VAN 4 o 5 per la categoria dei dispositivi qualificati per la creazione di firme e sigilli a distanza: la norma EN 419241-2:2019 (sistemi affidabili che supportano la firma lato server, parte 2: profili di protezione per QSCD per la firma lato server) e la norma EN 419221-5:2018 (profili di protezione per moduli crittografici TSP, parte 5: moduli crittografici per servizi fiduciari).",
        "testo_integrale": "1. Per la categoria dei dispositivi qualificati per la creazione di firme e sigilli a distanza:\n\n(1) EN 419241-2:2019 – Sistemi affidabili che supportano la firma lato server – Parte 2: profili di protezione per QSCD per la firma lato server;\n\n(2) EN 419221-5:2018 – Profili di protezione per moduli crittografici TSP – Parte 5: moduli crittografici per servizi fiduciari.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "dispositivo qualificato di creazione di firma elettronica",
            "dispositivo qualificato di creazione di sigillo elettronico",
        ],
    },
    {
        "riferimento": "allegato II, punto 2",
        "testo": "Profili di protezione che sono stati adottati come documenti sullo stato dell'arte: il testo ufficiale pubblicato nella Gazzetta ufficiale dell'Unione europea non reca alcun profilo, ma il segnaposto letterale «[BLANK]» in luogo dell'elenco.",
        "testo_integrale": "2. Profili di protezione che sono stati adottati come documenti sullo stato dell'arte:\n\n[BLANK]",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "allegato I, punto 1",
    "allegato I, punto 1(a)",
    "allegato I, punto 1(a)(1)",
    "allegato I, punto 1(a)(2)",
    "allegato I, punto 1(a)(3)",
    "allegato I, punto 1(a)(4)",
    "allegato I, punto 1(a)(5)",
    "allegato I, punto 1(a)(6)",
    "allegato I, punto 1(a)(7)",
    "allegato I, punto 1(b)",
    "allegato I, punto 1(b)(1)",
    "allegato I, punto 1(b)(2)",
    "allegato I, punto 1(b)(3)",
    "allegato I, punto 2",
    "allegato I, punto 2(a)",
    "allegato II, punto 1",
    "allegato II, punto 1(1)",
    "allegato II, punto 1(2)",
    "allegato II, punto 2",
]

MAPPATURA_LOCALE = {
    "allegato I, punto 1": [
        "allegato I, punto 1",
        "allegato I, punto 1(a)",
        "allegato I, punto 1(a)(1)",
        "allegato I, punto 1(a)(2)",
        "allegato I, punto 1(a)(3)",
        "allegato I, punto 1(a)(4)",
        "allegato I, punto 1(a)(5)",
        "allegato I, punto 1(a)(6)",
        "allegato I, punto 1(a)(7)",
        "allegato I, punto 1(b)",
        "allegato I, punto 1(b)(1)",
        "allegato I, punto 1(b)(2)",
        "allegato I, punto 1(b)(3)",
    ],
    "allegato I, punto 2": [
        "allegato I, punto 2",
        "allegato I, punto 2(a)",
    ],
    "allegato II, punto 1": [
        "allegato II, punto 1",
        "allegato II, punto 1(1)",
        "allegato II, punto 1(2)",
    ],
    "allegato II, punto 2": ["allegato II, punto 2"],
}

# Nessuna relazione interna a questo capitolo: le quattro righe degli allegati
# I e II non si citano a vicenda (nessun rinvio letterale dentro la porzione).
# I collegamenti verso gli articoli che richiamano gli allegati (art. 7 §1(d),
# §1(e), §3(a), §3(b) nel cap02; art. 15 §1(c) e §2 nel cap03; art. 22 §1(b)(2)
# nel cap04; art. 34 §2 nel cap06; art. 42 §1(f) nel cap07; art. 48 §2 e §3 nel
# cap08) e verso l'art. 50 §2 per il segnaposto "[data di entrata in vigore]"
# sono relazioni di fase 6, elencate nel docstring: dichiararle qui
# significherebbe indovinare i `riferimento` dei nodi scritti da moduli
# paralleli, con il rischio di far fallire l'intero seed (KeyError).
RELAZIONI = []
