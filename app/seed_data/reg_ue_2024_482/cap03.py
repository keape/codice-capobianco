"""Regolamento di esecuzione (UE) 2024/482 della Commissione, del 31 gennaio
2024 - modalita' di applicazione del regolamento (UE) 2019/881 per quanto
riguarda l'adozione del sistema europeo di certificazione della cibersicurezza
basato sui criteri comuni (EUCC). Fonte 29 (`reg_ue_2024_482`), capitolo 3 di 14
(vedi app/.source_cache/reg_ue_2024_482/manifest.json): Capo III -
Certificazione dei profili di protezione (articoli 15-20), con le due sezioni
interne "Norme e requisiti specifici per la valutazione" (art. 15) e "Rilascio,
rinnovo e revoca dei certificati EUCC per i profili di protezione" (artt. 16-20).
Gli artt. 1-14 e 21-50 e gli allegati I-IX sono nei capitoli 1, 2 e 4-14,
assegnati ad altri moduli: nessuno di quei file e' toccato qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_482/cap03.txt, estratto dal
raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R0482, lingua italiana; URL
risolto .../cellar/687c0d05-c580-11ee-95d9-01aa75ed71a1.0014.03/DOC_1, XHTML
della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 135.367 caratteri di
testo, sha256 del raw.txt
b46d08cab6d63b2c190ae767042c07c1fc324955c22ef491eb314556b28ca5b8 - dettagli
completi in provenance.json). Il preambolo (considerando) e' a monte del Capo I
e non e' in questa porzione.

Modellazione (ADR-0007, nessun discrimine di rilevanza):
- Paratesto -> nessun nodo: le intestazioni "CAPO III / CERTIFICAZIONE DEI
  PROFILI DI PROTEZIONE", "SEZIONE I / Norme e requisiti specifici per la
  valutazione" e "SEZIONE II / Rilascio, rinnovo e revoca dei certificati EUCC
  per i profili di protezione" sono struttura dell'atto, non articoli, commi o
  lettere; le intestazioni dei sei articoli ("Articolo N" + rubrica) restano
  coperte perche' incluse nel `testo_integrale` della prima riga di ciascun
  articolo, dove il testo ufficiale le premette immediatamente al comma, ma non
  sono item di indice (l'articolo e' coperto dai suoi commi).
- In questa porzione non compaiono preambolo/considerando, epigrafe, firma,
  note a pie' di pagina, formula di chiusura ("obbligatorio in tutti i suoi
  elementi e direttamente applicabile in ciascuno degli Stati membri") ne' riga
  ELI/ISSN: il preambolo e' a monte del Capo I (cap01), le formule finali sono
  nel cap08. Nessuno di questi elementi produce percio' un nodo o un item di
  indice in questo modulo, e nessuna nota a pie' di pagina attraversa il
  capitolo (i segnaposto "(11)"/"(1)" che compaiono in altri moduli di questa
  Fonte non ricadono nel Capo III).
- Unita' di copertura: un articolo/comma = una riga; le lettere ricevono un
  item di indice proprio, ma restano nella stessa riga del comma quando non
  hanno precetto autonomo (sotto, articolo per articolo). Art. 15 -> 2 Obblighi
  (§1 con le lettere a)-c), §2); art. 16 -> 1 Obbligo (articolo senza commi
  numerati); art. 17 -> 3 Obblighi (§1, §3, §4 con le lettere a)-b)) + 1
  Principio (§2); art. 18 -> 1 Obbligo (§1) + 1 Principio (§2); art. 19 -> 2
  Obblighi (§1, §2 con le lettere a)-d)); art. 20 -> 2 Obblighi (§1, §2).
  Totale 11 Obblighi e 2 Principi su 13 righe.
- Art. 15 §1 ("Un profilo di protezione e' valutato quanto meno conformemente a
  quanto segue:" + lettere a)-c)) -> UNA SOLA riga Obbligo "tecnico/sicurezza":
  le tre lettere sono frammenti nominali ("gli elementi applicabili delle norme
  di cui all'articolo 3", "il livello di rischio ... e le loro funzioni di
  sicurezza ...", "i pertinenti documenti sullo stato dell'arte di cui
  all'allegato I"), privi di verbo proprio, retti dal chapeau: nessuna e'
  azionabile senza di esso e tutte concorrono allo stesso precetto di
  valutazione. Restano integralmente nel `testo_integrale` della riga e sono
  indicizzate separatamente come "art. 15 §1(a)", "art. 15 §1(b)", "art. 15
  §1(c)". La seconda frase della lettera c) ("Un profilo di protezione
  contemplato da un settore tecnico e' certificato rispetto ai requisiti
  stabiliti in tale settore tecnico") sta, nel testo ufficiale, dentro il
  paragrafo della lettera c) e non ha item proprio: e' trattata nella stessa
  riga e nominata nella sintesi `testo` perche' e' determinante (aggiunge un
  criterio di certificazione settoriale). Tipo "tecnico/sicurezza" e non
  "procedurale": la lettera b) e la lettera c) riguardano rischio, funzioni di
  sicurezza e stato dell'arte, cioe' il contenuto tecnico della valutazione -
  stessa classificazione dell'articolo gemello art. 7 §1 della stessa Fonte
  (criteri e metodi di valutazione dei prodotti TIC), che resta nel cap02.
- Art. 15 §2 -> Obbligo "procedurale" con `condizione_applicabilita` (il
  precetto vale solo "in casi eccezionali e debitamente giustificati"): il
  comma disciplina la deroga all'applicazione dei documenti sullo stato
  dell'arte e la relativa procedura di autorizzazione (informazione e
  giustificazione all'autorita' nazionale di certificazione della
  cibersicurezza, valutazione e approvazione da parte di questa, blocco del
  rilascio dei certificati in attesa della decisione, notifica al gruppo
  europeo per la certificazione della cibersicurezza che puo' formulare un
  parere, considerazione massima del parere). Il comma e' un'unica unita' di
  copertura e coinvolge due attori: l'organismo di valutazione della conformita'
  (soggetto dei primi due periodi e del periodo sul blocco dei certificati) e
  l'autorita' nazionale di certificazione della cibersicurezza (soggetto dei
  periodi rimanenti), per la quale il censimento non ha una categoria soggetto
  (vedi sotto): `soggetti` dichiara percio' solo l'organismo di valutazione
  della conformita'.
- Art. 16 -> Obbligo "procedurale", riferimento "art. 16" senza paragrafi
  numerati (il testo ufficiale non numera i commi): il richiedente la
  certificazione di un profilo di protezione fornisce, o mette altrimenti a
  disposizione dell'organismo di certificazione e dell'ITSEF, tutte le
  informazioni necessarie per le attivita' di certificazione; il rinvio "Si
  applicano, mutatis mutandis, le disposizioni dell'articolo 8, paragrafi 2, 3,
  4 e 7" e' la seconda frase dello stesso comma, quindi resta nella stessa riga.
  Tipo "procedurale" e non "informativo/trasparenza": le informazioni sono
  l'input documentale del procedimento di certificazione consegnato agli
  organismi che certificano, non una comunicazione verso utenti o pubblico.
- Art. 17 §1 -> Obbligo "procedurale": il richiedente fornisce all'organismo di
  certificazione e all'ITSEF "tutte le informazioni necessarie, complete e
  corrette" (il requisito di completezza/correttezza, che l'art. 16 non
  ripete, sta solo qui).
- Art. 17 §2 ("Gli articoli 9 e 10 si applicano mutatis mutandis.") ->
  Principio "altro": e' una norma di mero rinvio, senza soggetto e senza
  comportamento proprio - rende applicabili al profilo di protezione
  disposizioni dettate per i prodotti TIC (condizioni di rilascio e contenuto e
  formato del certificato, artt. 9 e 10, cap02) e non descrive ne' un obbligo
  ne' un effetto giuridico autonomo. Stesso trattamento della norma di rinvio
  dell'art. 2 del Reg. 2025/2532 (Principio "altro") e dell'art. 2 del Reg.
  2024/2979. Divergenza dichiarata dall'import storico in `app/seed.py`, dove
  una clausola analoga (eIDAS2 art. 5 bis §20, "si applica, mutatis mutandis,
  ai fornitori dei portafogli") era stata censita come Obbligo "procedurale":
  li' la clausola identificava il soggetto gravato via via dall'estensione delle
  disposizioni richiamate, qui il testo non nomina alcun soggetto.
- Art. 17 §3 -> Obbligo "tecnico/sicurezza": l'ITSEF valuta se il profilo di
  protezione e' completo, coerente, tecnicamente valido ed efficace per l'uso
  previsto e gli obiettivi di sicurezza della categoria di prodotti TIC
  contemplati; e' un giudizio tecnico vincolato, quindi Obbligo e non Principio.
- Art. 17 §4 ("Un profilo di protezione e' certificato unicamente:" + lettere
  a)-b)) -> UNA SOLA riga Obbligo "procedurale", senza `soggetti`: le due
  lettere sono frammenti alternativi retti dal chapeau ("da un'autorita'
  nazionale di certificazione della cibersicurezza o da un altro organismo
  pubblico accreditato come organismo di certificazione; oppure da un
  organismo di certificazione, previa approvazione ..."), non precetti
  autonomi, e l'item di indice resta separato per ciascuna lettera ("art. 17
  §4(a)", "art. 17 §4(b)"). Il comma delimita quali entita' possono certificare
  un profilo di protezione: autorita' nazionale di certificazione della
  cibersicurezza, altro organismo pubblico accreditato, organismo di
  certificazione (con approvazione preventiva per ogni singolo profilo).
  Nessuna di esse ha una categoria nel set (QTSP/gestore, Utente/titolare,
  Terza parte, Terzi affidanti/pubblico) e dichiarare la sola "Terza parte"
  (l'organismo di certificazione) avrebbe descritto una sola delle alternative
  e taciuto l'autorita' pubblica: preferibile nessun soggetto, come per le
  righe che in questo censimento gravano su una pubblica amministrazione (es.
  CAD art. 5 c.4, AgID).
- Art. 18 §1 -> Obbligo "procedurale": l'organismo di certificazione stabilisce
  un periodo di validita' per ciascun certificato EUCC (a differenza dell'art.
  12 §1, che per i prodotti TIC impone di tener conto delle caratteristiche del
  prodotto: qui il comma non aggiunge criteri).
- Art. 18 §2 ("Il periodo di validita' puo' durare fino al termine del ciclo di
  vita del profilo di protezione in questione.") -> Principio "altro":
  delimita la facolta' riconosciuta dal §1 (durata massima ancorata al ciclo di
  vita del profilo di protezione) senza imporre alcun comportamento a chi
  certifica. Stesso trattamento delle disposizioni permissive gia' censite (es.
  art. 1 §2 del Reg. 2025/2532). La classificazione alternativa - Obbligo di
  non eccedere il ciclo di vita - e' stata scartata perche' il testo non
  formula un divieto ma la misura della facolta'.
- Art. 19 §1 -> Obbligo "procedurale" con `condizione_applicabilita` (il comma
  si applica quando l'organismo di certificazione decide di riesaminare il
  certificato, su richiesta del titolare o per altri motivi giustificati): la
  forma e' in parte permissiva ("puo' decidere di riesaminare"), ma il resto
  del comma e' prescrittivo - il riesame "e' effettuato applicando le
  condizioni di cui all'articolo 15", la portata e' determinata dall'organismo
  di certificazione e, se necessario, questi chiede all'ITSEF una nuova
  valutazione del profilo certificato. Classificarlo come Principio
  perderebbe il metodo obbligatorio del riesame.
- Art. 19 §2 ("A seguito dei risultati del riesame ... l'organismo di
  certificazione procede in uno dei modi seguenti:" + lettere a)-d)) -> UNA
  SOLA riga Obbligo "procedurale" con `condizione_applicabilita`: il chapeau
  contiene il predicato e il soggetto ("l'organismo di certificazione procede
  in uno dei modi seguenti"), quindi le quattro lettere sono modalita'
  alternative del medesimo passo procedurale (conferma; revoca ai sensi
  dell'art. 20; revoca piu' nuovo certificato con ambito identico e validita'
  prorogata; revoca piu' nuovo certificato con ambito diverso) e non precetti
  autonomi: e' il modello dell'art. 5 §1 del Reg. 2024/2979, non quello
  dell'art. 6 §3 dello stesso (chapeau ridotto al solo soggetto e lettere con
  verbo proprio, che li' avevano ricevuto righe separate). Gli item restano
  separati per lettera ("art. 19 §2(a)" ... "art. 19 §2(d)").
- Art. 20 §1 -> Obbligo "procedurale": la revoca del certificato EUCC per un
  profilo di protezione e' operata dall'organismo di certificazione che lo ha
  rilasciato, fatte salve le competenze di cui all'art. 58, paragrafo 8,
  lettera e), del regolamento (UE) 2019/881, e l'art. 14 (revoca dei
  certificati dei prodotti TIC: notifica all'autorita' nazionale di
  certificazione della cibersicurezza e all'ENISA) si applica mutatis mutandis.
  Non si tratta di una mera designazione di competenza: il rinvio all'art. 14
  importa doveri di notifica in capo all'organismo che revoca, quindi la riga
  e' un Obbligo e non un Principio.
- Art. 20 §2 -> Obbligo "procedurale", senza `soggetti`: per i certificati
  rilasciati conformemente all'art. 17 §4(b) (organismo di certificazione
  approvato dall'autorita'), la revoca spetta all'autorita' nazionale di
  certificazione della cibersicurezza che li ha approvati; l'autorita' non ha
  una categoria nel set dei soggetti (vedi sopra, art. 17 §4). Tenuto come
  Obbligo e non come Principio perche' completa la disciplina della revoca
  dell'articolo (l'art. 20 e' "Revoca del certificato EUCC per un profilo di
  protezione": il §1 indica chi revoca i certificati in generale e richiama
  l'art. 14, il §2 indica chi revoca quelli approvati ai sensi dell'art. 17
  §4(b)) - classificarlo come dichiarativo toglierebbe dal censimento un tratto
  della procedura di revoca; il dubbio resta annotato sotto.
- Soggetti obbligati dichiarati come "Terza parte": organismo di valutazione
  della conformita' e ITSEF (art. 15 §1, art. 15 §2, art. 17 §3), organismo di
  certificazione (art. 18 §1, art. 19 §1, art. 19 §2, art. 20 §1) e richiedente
  la certificazione (art. 16, art. 17 §1). CONTEXT.md indica esplicitamente
  l'auditor tra gli esempi di "Terza parte" (soggetto con rapporto
  identificabile e tracciabile): gli organismi del sistema EUCC vi rientrano
  per analogia dichiarata, e il richiedente e' una parte esterna al censimento
  (sponsor/sviluppatore del profilo di protezione, tipicamente non un QTSP) -
  nessuna di queste righe descrive un QTSP, e la categoria e' quindi un uso
  approssimato del set disponibile, non una menzione letterale del testo.
  L'autorita' nazionale di certificazione della cibersicurezza e il gruppo
  europeo per la certificazione della cibersicurezza (autorita' pubbliche e
  organo consultivo) non hanno categoria e non sono dichiarati come soggetti.
- Nessuna riga valorizza `severita` o `sanzioni`: questo capitolo non gradua i
  requisiti ne' prevede sanzioni proprie (stessa scelta di tutti i moduli di
  atti di esecuzione gia' censiti). `stato` = "vigente" per tutte le righe.
- Unita' di indice: articolo + paragrafo numerato con "§" ("art. 15 §1",
  "art. 19 §2") e lettera tra parentesi ("art. 15 §1(a)", "art. 17 §4(b)",
  "art. 19 §2(d)"), come negli altri atti di esecuzione eIDAS2/EUCC gia'
  censiti; "art. 16" senza paragrafo perche' l'articolo non numera i commi.
- `testo_integrale`: verbatim e integrale, ricucito dalle righe spezzate dalla
  conversione XHTML -> testo (le lettere isolate su riga propria - "(a)", "(b)"
  - sono riunite al proprio testo nella forma "a) gli elementi applicabili
  ..."), con l'intestazione "Articolo N" + rubrica nella prima riga di ogni
  articolo, dove il testo ufficiale la precede immediatamente al comma. Nessun
  marcatore di elisione (vincolo `verifica_completezza_testo_integrale`,
  ADR-0010). `testo` e' invece la sintesi compressa (1-3 frasi) di ogni comma.
- RELAZIONI: solo interne a questo capitolo, con `fonte_id_o_None = None` su
  entrambi gli estremi e tutte verificate sul `testo_integrale` delle righe
  citate, quindi `evidence_type = "textual"`; `confidence` resta None perche'
  non esiste uno score reale da riportare (ADR-0005: non va inventato). Regola
  adottata per i rinvii a un articolo "in blocco": si dichiara il bersaglio su
  ogni paragrafo che porta la regola richiamata - "Il riesame e' effettuato
  applicando le condizioni di cui all'articolo 15" (art. 19 §1) verso i due
  paragrafi dell'art. 15 (criteri del §1, regime eccezionale sul metodo del
  §2); "revoca il certificato EUCC in conformita' dell'articolo 20" (art. 19
  §2, lettere b), c) e d)) verso i due paragrafi dell'art. 20 (revoca
  dall'organismo di certificazione nel §1, revoca dall'autorita' che ha
  approvato nel §2); "rilasciato conformemente all'articolo 17, paragrafo 4,
  lettera b)" (art. 20 §2) verso "art. 17 §4", che e' l'unica riga dell'art. 17
  §4 e contiene entrambe le lettere. Avvertenza per l'audit
  `verifica_relazioni_textual.py`: le relazioni verso un bersaglio "art. N §M"
  sono tracciate dal numero dell'articolo (2 caratteri) e non da un riferimento
  di paragrafo, perche' i testi citanti rinviano all'articolo intero ("di cui
  all'articolo 15", "in conformita' dell'articolo 20"): il gate meccanico passa,
  ma la verifica sostanziale e' la lettura del `testo_integrale` fatta qui.
  Nessuna relazione inferita e' stata aggiunta (i legami non citati - es. il
  riesame dell'art. 19 e il rilascio dell'art. 17 condividono l'organismo di
  certificazione - non sono verificabili sul testo).

Rinvii demandati alla fase 6 (ADR-0009, non dichiarati come relazioni perche'
verso altri capitoli della stessa Fonte o verso altre Fonti): art. 15 §1(a) ->
art. 3 della stessa Fonte (norme di valutazione, cap01); art. 15 §1(b) -> artt.
51 e 52 del regolamento (UE) 2019/881; art. 15 §1(c) -> allegato I della stessa
Fonte (cap09); art. 16 -> art. 8, paragrafi 2, 3, 4 e 7 (cap02); art. 17 §2 ->
artt. 9 e 10 (cap02); art. 20 §1 -> art. 14 (cap02) e art. 58, paragrafo 8,
lettera e), del regolamento (UE) 2019/881. Il gruppo europeo per la
certificazione della cibersicurezza (art. 15 §2) e' un organo, non un nodo del
censimento.

Copertura: 22 item di indice, 13 righe (11 Obblighi + 2 Principi), 5 relazioni
interne.

Dubbi di classificazione rimasti aperti: (1) art. 20 §2 tenuto come Obbligo
"procedurale" senza soggetti - la lettura alternativa e' Principio "altro",
come per la designazione di competenza dell'art. 7 §1 del Reg. 2024/2979; (2)
art. 18 §2 e art. 17 §2 come Principi "altro", mentre l'import storico in
`app/seed.py` tendeva a censire come Obbligo le clausole di mero rinvio; (3)
l'uso di "Terza parte" per gli organismi del sistema EUCC e' un'approssimazione
dichiarata del set di categorie, non una scelta del testo.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 15 §1",
        "testo": "Un profilo di protezione è valutato quanto meno conformemente: a) agli elementi applicabili delle norme di cui all'articolo 3; b) al livello di rischio associato all'uso previsto dei prodotti TIC in questione a norma dell'articolo 52 del regolamento (UE) 2019/881 e alle loro funzioni di sicurezza a sostegno degli obiettivi di sicurezza di cui all'articolo 51 del medesimo regolamento; e c) ai pertinenti documenti sullo stato dell'arte di cui all'allegato I. Un profilo di protezione contemplato da un settore tecnico è certificato rispetto ai requisiti stabiliti in tale settore tecnico.",
        "testo_integrale": "Articolo 15\n\nCriteri e metodi di valutazione\n\n1. Un profilo di protezione è valutato quanto meno conformemente a quanto segue:\n\na) gli elementi applicabili delle norme di cui all'articolo 3;\n\nb) il livello di rischio associato all'uso previsto dei prodotti TIC in questione a norma dell'articolo 52 del regolamento (UE) 2019/881 e le loro funzioni di sicurezza a sostegno degli obiettivi di sicurezza di cui all'articolo 51 del medesimo regolamento; e\n\nc) i pertinenti documenti sullo stato dell'arte di cui all'allegato I. Un profilo di protezione contemplato da un settore tecnico è certificato rispetto ai requisiti stabiliti in tale settore tecnico.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 15 §2",
        "testo": "In casi eccezionali e debitamente giustificati un organismo di valutazione della conformità può certificare un profilo di protezione senza applicare i pertinenti documenti sullo stato dell'arte: informa l'autorità nazionale di certificazione della cibersicurezza competente fornendo una giustificazione e una proposta di metodologia di valutazione, e non rilascia alcun certificato per il profilo di protezione in attesa della decisione dell'autorità, che valuta la giustificazione e, se la ritiene valida, approva la mancata applicazione dei documenti e approva o modifica la metodologia di valutazione; l'autorità notifica senza indebito ritardo l'autorizzazione al gruppo europeo per la certificazione della cibersicurezza, che può formulare un parere, e tiene il parere nella massima considerazione.",
        "testo_integrale": "2. In casi eccezionali e debitamente giustificati, un organismo di valutazione della conformità può certificare un profilo di protezione senza applicare i pertinenti documenti sullo stato dell'arte. In tali casi informa l'autorità nazionale di certificazione della cibersicurezza competente e fornisce una giustificazione per la prevista certificazione senza l'applicazione dei pertinenti documenti sullo stato dell'arte, nonché una proposta di metodologia di valutazione. L'autorità nazionale di certificazione della cibersicurezza valuta la giustificazione e, qualora la ritenga valida, approva la mancata applicazione dei pertinenti documenti sullo stato dell'arte e approva o modifica, se del caso, la metodologia di valutazione che dovrà essere applicata dall'organismo di valutazione della conformità. In attesa della decisione dell'autorità nazionale di certificazione della cibersicurezza, l'organismo di valutazione della conformità non rilascia alcun certificato per il profilo di protezione. L'autorità nazionale di certificazione della cibersicurezza notifica senza indebito ritardo l'autorizzazione della mancata applicazione dei pertinenti documenti sullo stato dell'arte al gruppo europeo per la certificazione della cibersicurezza, che può formulare un parere. L'autorità nazionale di certificazione della cibersicurezza tiene nella massima considerazione il parere del gruppo europeo per la certificazione della cibersicurezza.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo in casi eccezionali e debitamente giustificati, quando l'organismo di valutazione della conformità intende certificare un profilo di protezione senza applicare i pertinenti documenti sullo stato dell'arte.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 16",
        "testo": "Il richiedente la certificazione di un profilo di protezione fornisce, o mette altrimenti a disposizione, dell'organismo di certificazione e dell'ITSEF tutte le informazioni necessarie per le attività di certificazione; si applicano, mutatis mutandis, le disposizioni dell'articolo 8, paragrafi 2, 3, 4 e 7.",
        "testo_integrale": "Articolo 16\n\nInformazioni necessarie per la certificazione dei profili di protezione\n\nIl richiedente la certificazione di un profilo di protezione fornisce o mette altrimenti a disposizione dell'organismo di certificazione e dell'ITSEF tutte le informazioni necessarie per le attività di certificazione. Si applicano, mutatis mutandis, le disposizioni dell'articolo 8, paragrafi 2, 3, 4 e 7.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 17 §1",
        "testo": "Il richiedente la certificazione fornisce all'organismo di certificazione e all'ITSEF tutte le informazioni necessarie, complete e corrette.",
        "testo_integrale": "Articolo 17\n\nRilascio di certificati EUCC per i profili di protezione\n\n1. Il richiedente la certificazione fornisce all'organismo di certificazione e all'ITSEF tutte le informazioni necessarie, complete e corrette.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 17 §3",
        "testo": "L'ITSEF valuta se un profilo di protezione è completo, coerente, tecnicamente valido ed efficace per l'uso previsto e gli obiettivi di sicurezza della categoria di prodotti TIC da esso contemplati.",
        "testo_integrale": "3. L'ITSEF valuta se un profilo di protezione è completo, coerente, tecnicamente valido ed efficace per l'uso previsto e gli obiettivi di sicurezza della categoria di prodotti TIC da esso contemplati.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 17 §4",
        "testo": "Un profilo di protezione è certificato unicamente: a) da un'autorità nazionale di certificazione della cibersicurezza o da un altro organismo pubblico accreditato come organismo di certificazione; oppure b) da un organismo di certificazione, previa approvazione dell'autorità nazionale di certificazione della cibersicurezza per ogni singolo profilo di protezione.",
        "testo_integrale": "4. Un profilo di protezione è certificato unicamente:\n\na) da un'autorità nazionale di certificazione della cibersicurezza o da un altro organismo pubblico accreditato come organismo di certificazione; oppure\n\nb) da un organismo di certificazione, previa approvazione dell'autorità nazionale di certificazione della cibersicurezza per ogni singolo profilo di protezione.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 18 §1",
        "testo": "L'organismo di certificazione stabilisce un periodo di validità per ciascun certificato EUCC.",
        "testo_integrale": "Articolo 18\n\nPeriodo di validità del certificato EUCC per i profili di protezione\n\n1. L'organismo di certificazione stabilisce un periodo di validità per ciascun certificato EUCC.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 19 §1",
        "testo": "Su richiesta del titolare del certificato o per altri motivi giustificati, l'organismo di certificazione può decidere di riesaminare un certificato EUCC per un profilo di protezione; il riesame è effettuato applicando le condizioni di cui all'articolo 15, la portata del riesame è determinata dall'organismo di certificazione che, se necessario, chiede all'ITSEF di effettuare una nuova valutazione del profilo di protezione certificato.",
        "testo_integrale": "Articolo 19\n\nRiesame del certificato EUCC per i profili di protezione\n\n1. Su richiesta del titolare del certificato o per altri motivi giustificati, l'organismo di certificazione può decidere di riesaminare un certificato EUCC per un profilo di protezione. Il riesame è effettuato applicando le condizioni di cui all'articolo 15. L'organismo di certificazione determina la portata del riesame. Se necessario per il riesame, l'organismo di certificazione chiede all'ITSEF di effettuare una nuova valutazione del profilo di protezione certificato.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando l'organismo di certificazione decide di riesaminare il certificato EUCC, su richiesta del titolare del certificato o per altri motivi giustificati.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 19 §2",
        "testo": "A seguito dei risultati del riesame e, se del caso, della nuova valutazione, l'organismo di certificazione: a) conferma il certificato EUCC; b) revoca il certificato EUCC in conformità dell'articolo 20; c) revoca il certificato EUCC in conformità dell'articolo 20 e rilascia un nuovo certificato EUCC con un ambito di applicazione identico e un periodo di validità prorogato; oppure d) revoca il certificato EUCC in conformità dell'articolo 20 e rilascia un nuovo certificato EUCC con un ambito di applicazione diverso.",
        "testo_integrale": "2. A seguito dei risultati del riesame e, se del caso, della nuova valutazione, l'organismo di certificazione procede in uno dei modi seguenti:\n\na) conferma il certificato EUCC;\n\nb) revoca il certificato EUCC in conformità dell'articolo 20;\n\nc) revoca il certificato EUCC in conformità dell'articolo 20 e rilascia un nuovo certificato EUCC con un ambito di applicazione identico e un periodo di validità prorogato;\n\nd) revoca il certificato EUCC in conformità dell'articolo 20 e rilascia un nuovo certificato EUCC con un ambito di applicazione diverso.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica a seguito dei risultati del riesame e, se del caso, della nuova valutazione del profilo di protezione certificato.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 20 §1",
        "testo": "Fatto salvo l'articolo 58, paragrafo 8, lettera e), del regolamento (UE) 2019/881, un certificato EUCC per un profilo di protezione è revocato dall'organismo di certificazione che lo ha rilasciato; l'articolo 14 si applica mutatis mutandis.",
        "testo_integrale": "Articolo 20\n\nRevoca del certificato EUCC per un profilo di protezione\n\n1. Fatto salvo l'articolo 58, paragrafo 8, lettera e), del regolamento (UE) 2019/881, un certificato EUCC per un profilo di protezione è revocato dall'organismo di certificazione che lo ha rilasciato. L'articolo 14 si applica mutatis mutandis.",
        "tipo_obbligo": "sanzionatorio",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 20 §2",
        "testo": "Un certificato per un profilo di protezione rilasciato conformemente all'articolo 17, paragrafo 4, lettera b), è revocato dall'autorità nazionale di certificazione della cibersicurezza che lo ha approvato.",
        "testo_integrale": "2. Un certificato per un profilo di protezione rilasciato conformemente all'articolo 17, paragrafo 4, lettera b), è revocato dall'autorità nazionale di certificazione della cibersicurezza che lo ha approvato.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 17 §2",
        "testo": "Norma di mero rinvio: gli articoli 9 e 10 (condizioni per il rilascio del certificato EUCC e contenuto e formato del certificato EUCC, dettati per i prodotti TIC) si applicano mutatis mutandis alla certificazione dei profili di protezione.",
        "testo_integrale": "2. Gli articoli 9 e 10 si applicano mutatis mutandis.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 18 §2",
        "testo": "Il periodo di validità stabilito per il certificato EUCC può durare fino al termine del ciclo di vita del profilo di protezione in questione.",
        "testo_integrale": "2. Il periodo di validità può durare fino al termine del ciclo di vita del profilo di protezione in questione.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 15 §1",
    "art. 15 §1(a)",
    "art. 15 §1(b)",
    "art. 15 §1(c)",
    "art. 15 §2",
    "art. 16",
    "art. 17 §1",
    "art. 17 §2",
    "art. 17 §3",
    "art. 17 §4",
    "art. 17 §4(a)",
    "art. 17 §4(b)",
    "art. 18 §1",
    "art. 18 §2",
    "art. 19 §1",
    "art. 19 §2",
    "art. 19 §2(a)",
    "art. 19 §2(b)",
    "art. 19 §2(c)",
    "art. 19 §2(d)",
    "art. 20 §1",
    "art. 20 §2",
]

MAPPATURA_LOCALE = {
    "art. 15 §1": [
        "art. 15 §1",
        "art. 15 §1(a)",
        "art. 15 §1(b)",
        "art. 15 §1(c)",
    ],
    "art. 15 §2": ["art. 15 §2"],
    "art. 16": ["art. 16"],
    "art. 17 §1": ["art. 17 §1"],
    "art. 17 §2": ["art. 17 §2"],
    "art. 17 §3": ["art. 17 §3"],
    "art. 17 §4": [
        "art. 17 §4",
        "art. 17 §4(a)",
        "art. 17 §4(b)",
    ],
    "art. 18 §1": ["art. 18 §1"],
    "art. 18 §2": ["art. 18 §2"],
    "art. 19 §1": ["art. 19 §1"],
    "art. 19 §2": [
        "art. 19 §2",
        "art. 19 §2(a)",
        "art. 19 §2(b)",
        "art. 19 §2(c)",
        "art. 19 §2(d)",
    ],
    "art. 20 §1": ["art. 20 §1"],
    "art. 20 §2": ["art. 20 §2"],
}

# Relazioni interne a questa Fonte (fonte_id_o_None = None su entrambi gli
# estremi), tutte rinvii letterali verificati sul `testo_integrale` delle righe
# coinvolte: art. 19 §1 cita "le condizioni di cui all'articolo 15" (rinvio
# all'articolo in blocco: criteri di valutazione del §1 e regime eccezionale sul
# metodo del §2); art. 19 §2 (lettere b), c) e d), accorpate nella riga del
# comma) cita "in conformita' dell'articolo 20" (rinvio all'articolo in blocco:
# revoca dall'organismo di certificazione nel §1 e dall'autorita' che ha
# approvato i certificati di cui all'art. 17 §4(b) nel §2); art. 20 §2 cita
# "l'articolo 17, paragrafo 4, lettera b)", cioe' la riga "art. 17 §4" che
# contiene entrambe le lettere. I rinvii ad altri capitoli di questa Fonte
# (art. 3 in art. 15 §1(a), allegato I in art. 15 §1(c), art. 8 §2-§4 e §7 in
# art. 16, artt. 9 e 10 in art. 17 §2, art. 14 in art. 20 §1) e ad altre Fonti
# (artt. 51 e 52 e art. 58 §8(e) del regolamento (UE) 2019/881) non sono
# dichiarati qui: sono collegamenti della fase ADR-0009, demandati alla
# sessione principale ed elencati nel docstring. `confidence` = None: nessuno
# score reale da riportare.
RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "art. 19 §1"),
        "nodo_a": ("obbligo", None, "art. 15 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 19 §1"),
        "nodo_a": ("obbligo", None, "art. 15 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 19 §2"),
        "nodo_a": ("obbligo", None, "art. 20 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 19 §2"),
        "nodo_a": ("obbligo", None, "art. 20 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 20 §2"),
        "nodo_a": ("obbligo", None, "art. 17 §4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
