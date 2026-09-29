"""Regolamento di esecuzione (UE) 2024/2979 della Commissione, del 28 novembre
2024 - modalita' di applicazione del regolamento (UE) n. 910/2014 per quanto
riguarda l'integrita' e le funzionalita' di base dei portafogli europei di
identita' digitale (articolo 5 bis, paragrafo 23, eIDAS). Fonte 28
(`reg_ue_2024_2979`), capitolo 2 di 5 (vedi
app/.source_cache/reg_ue_2024_2979/manifest.json): Capo II - Integrita' dei
portafogli europei di identita' digitale (articoli 3-7). Gli artt. 1-2, 8-14,
15 e gli allegati I-V sono nei capitoli 1, 3, 4 e 5, assegnati ad altri
moduli: nessuno di quei file e' toccato qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_2979/cap02.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R2979, lingua italiana;
URL risolto .../cellar/a7576de1-b1e0-11ef-acb1-01aa75ed71a1.0014.03/DOC_1,
XHTML della Gazzetta ufficiale; fetch 2026-09-28, 38.236 caratteri di testo,
sha256 del raw.txt
c0bebf5c6707ddb9c70999245e38999f63f154afee2afc6009aad72d1d09cad0 - dettagli
completi in provenance.json). Il preambolo (considerando 1-48) e' a monte del
Capo I e non e' in questa porzione.

Modellazione (ADR-0007, nessun discrimine di rilevanza):
- Paratesto -> nessun nodo: l'intestazione di capitolo "CAPO II / INTEGRITA'
  DEI PORTAFOGLI EUROPEI DI IDENTITA' DIGITALE" e le intestazioni dei cinque
  articoli ("Articolo N" + rubrica) non sono articoli, commi o lettere, ma
  struttura dell'atto; le rubriche restano coperte perche' incluse nel
  `testo_integrale` della prima riga di ogni articolo (convenzione dell'art. 3
  del Reg. 2025/1569 e dell'art. 1 del Reg. 2025/2532). Non compaiono in
  questa porzione epigrafe, firma, riga ELI ne' la formula di chiusura
  (sono nel cap04), quindi non producono nodi ne' item di indice.
- Nota a pie' di pagina (11) (rinvio al regolamento di esecuzione (UE)
  2015/1502) -> nessun nodo: e' un riferimento bibliografico all'atto citato,
  non una disposizione di questo regolamento (stesso criterio del cap04 di
  questa Fonte per le note (1)-(11)). Il segnaposto "(11)" resta nel
  `testo_integrale` verbatim dell'art. 4 §3, dove il testo ufficiale lo
  colloca.
- Unita' di copertura: un articolo/comma = una riga, con UNA eccezione
  motivata comma per comma (sotto). Art. 3 -> 2 Obblighi (§1, §2); art. 4 -> 3
  Obblighi (§1, §2, §3); art. 5 -> 2 Obblighi (§1, §2); art. 6 -> 2 Obblighi
  (§1, §2) + 3 Obblighi (una riga per ciascuna lettera di §3, vedi sotto);
  art. 7 -> 1 Principio (§1) + 3 Obblighi (§2, §3, §4). Totale 15 Obblighi, 1
  Principio, 16 righe.
- Art. 3 §1 (le unita' di portafoglio non eseguono alcuna funzionalita' di cui
  all'art. 5 bis §4 eIDAS, eccetto l'autenticazione dell'utente per l'accesso
  all'unita', fino all'autenticazione riuscita) -> Obbligo
  "tecnico/sicurezza": il comma prescrive un comportamento verificabile di un
  componente (la sequenza "autentica l'utente, poi abilita le funzionalita'"),
  non enuncia un effetto giuridico; non e' quindi un Principio.
- Art. 3 §2 (una firma o un sigillo su almeno un attestato di unita' di
  portafoglio conforme ai requisiti dell'art. 6; certificato emesso sulla base
  di un certificato dell'elenco di fiducia del Reg. 2024/2980) -> Obbligo
  "tecnico/sicurezza". Le due frasi del comma (apposizione della firma/sigillo
  e catena di emissione del certificato) concorrono allo stesso precetto
  tecnico: un solo nodo, entrambe integralmente nel `testo_integrale`.
- Art. 4 §1 (per gestire le risorse critiche le istanze di portafoglio
  utilizzano almeno un dispositivo crittografico sicuro) -> Obbligo
  "tecnico/sicurezza". Art. 4 §2 (integrita', autenticita' e riservatezza
  della comunicazione tra istanze di portafoglio e applicazioni crittografiche
  sicure) -> Obbligo "tecnico/sicurezza". Art. 4 §3 (se le risorse critiche
  riguardano l'identificazione elettronica a livello di garanzia elevato, le
  operazioni crittografiche o altre operazioni su risorse critiche sono
  effettuate conformemente ai requisiti del Reg. 2015/1502) -> Obbligo
  "tecnico/sicurezza" con `condizione_applicabilita` (il precetto vale solo
  per le risorse critiche che riguardano l'identificazione elettronica a
  livello di garanzia elevato).
- Soggetto obbligato: e' dichiarato "QTSP/gestore" (ruolo "obbligato") in
  tutte le righe Obbligo di questo capitolo, anche quando il comma non nomina
  "i fornitori di portafogli" ma prescrive un comportamento di un componente
  del portafoglio (art. 3 §1 "le unita' di portafoglio", art. 4 §1 "le istanze
  di portafoglio", art. 4 §3 costruzione passiva "sono effettuate"). Motivo: i
  componenti sono forniti dal fornitore del portafoglio - l'art. 3 §2 dello
  stesso articolo e gli artt. 8-9 di questa Fonte imputano espressamente al
  fornitore la garanzia del comportamento delle soluzioni di portafoglio - ed
  e' lo stesso trattamento gia' riservato in `app/seed.py` alle prescrizioni
  di eIDAS2 art. 5 bis §4/§5, formulate sul portafoglio e non su una persona
  (tutte con soggetto obbligato "QTSP/gestore"). L'alternativa (nessun
  soggetto, come in 274 righe gia' censite di fonti nazionali) lascerebbe
  queste righe fuori da qualunque interrogazione per soggetto obbligato pur
  essendo precetti tecnici del fornitore: scelta dichiarata qui perche' e'
  un'attribuzione per implicazione del testo, non una menzione letterale.
- Art. 5 §1 (chapeau "I fornitori di portafogli garantiscono che le
  applicazioni crittografiche sicure per il portafoglio:" + lettere a)-h)) ->
  UNA SOLA riga Obbligo "tecnico/sicurezza". Le otto lettere sono specificative
  di un unico precetto: nessuna ha un verbo proprio all'indicativo, tutte sono
  rette dal chapeau con il congiuntivo ("effettuino", "siano in grado",
  "proteggano", "soddisfino"), tutte hanno lo stesso soggetto e lo stesso
  oggetto (le applicazioni crittografiche sicure per il portafoglio) e
  nessuna e' autonomamente azionabile senza il chapeau che nomina il fornitore
  obbligato. Restano percio' integralmente nel `testo_integrale` della riga
  "art. 5 §1", ma sono indicizzate separatamente come item di indice
  ("art. 5 §1(a)" ... "art. 5 §1(h)") e mappate tutte a quella riga, come da
  istruzione e come gia' fatto per le lettere di ogni singolo comma (es.
  art. 4 §3 del Reg. 2025/1569, "art. 4 §3(a)" ... "art. 4 §3(c)"; eIDAS2
  art. 5 bis §4(a)-(g) in `app/seed.py`). Nessuna delle lettere ha precetto
  autonomo e distinto: a) subordina le operazioni crittografiche su risorse
  critiche all'autenticazione riuscita dell'utente, b) impone la conformita'
  al Reg. 2015/1502 per l'autenticazione a livello elevato, c)-e) richiedono
  capacita' di generazione/cancellazione/prova di possesso, f) protegge le
  chiavi private, g) impone di nuovo i requisiti del Reg. 2015/1502, h)
  riserva alle sole applicazioni crittografiche sicure le operazioni
  crittografiche nel contesto dell'identificazione a livello elevato: sette
  condizioni tecniche e una delimitazione di competenza, tutte condizioni del
  medesimo precetto "il fornitore garantisce che".
- Art. 5 §2 (qualora decidano di fornire un'applicazione crittografica sicura
  a un elemento sicuro integrato, i fornitori basano la soluzione tecnica
  sulle specifiche tecniche dell'allegato I o su altre specifiche equivalenti)
  -> Obbligo "tecnico/sicurezza" con `condizione_applicabilita` (vale solo se
  il fornitore decide di fornire l'applicazione a un elemento sicuro
  integrato). Il rinvio all'allegato I e' dichiarato come relazione: il
  riferimento non e' indovinato, il modulo gemello del cap05 (scritto nella
  stessa tornata, allo stesso path assegnato dal manifest) espone la riga
  "allegato I", dove l'elenco delle norme di cui all'articolo 5 e' censito.
- Art. 6 §1 (i fornitori garantiscono che ciascuna unita' di portafoglio
  contenga attestati di unita' di portafoglio) -> Obbligo
  "tecnico/sicurezza"; art. 6 §2 (gli attestati contengano chiavi pubbliche e
  le chiavi private corrispondenti siano protette da un dispositivo
  crittografico sicuro) -> Obbligo "tecnico/sicurezza".
- Art. 6 §3 (chapeau "I fornitori di portafogli:" + lettere a)-c)) -> TRE righe
  Obbligo, una per lettera: e' l'eccezione ammessa dalla regola di
  granularita', motivata sul testo. Qui il chapeau e' un semplice soggetto
  seguito dai due punti, senza predicato ("I fornitori di portafogli:"), e
  ciascuna lettera ha un verbo proprio all'indicativo, un oggetto diverso e
  un tipo di obbligo diverso: a) "informano gli utenti del portafoglio in
  merito ai loro diritti e obblighi" (informativo/trasparenza), b) "forniscono
  meccanismi, indipendenti dalle unita' di portafoglio, per l'identificazione
  e l'autenticazione sicure degli utenti" (tecnico/sicurezza), c)
  "garantiscono che gli utenti del portafoglio abbiano il diritto di chiedere
  la revoca dei loro attestati" (procedurale: istituisce il canale/istanza con
  cui l'utente esercita il diritto, utilizzando i meccanismi di b)). Ciascuna
  lettera e' quindi un precetto autonomo e distinto, non una specificazione di
  un precetto unico. Il chapeau nudo non riceve un item di indice proprio:
  non ha contenuto normativo da coprire e un item senza riga farebbe fallire
  `verifica_copertura` (stesso criterio dell'art. 2 c.2 CAD e del par. 4.2
  punto 4 del regolamento AgID, dove a un chapeau enumerativo seguono righe
  per lettera). Gli item sono "art. 6 §3(a)", "art. 6 §3(b)", "art. 6 §3(c)".
  La differenza con art. 5 §1 non e' un'incoerenza: li' il chapeau e' parte del
  precetto unico e quindi e' esso stesso l'item di quella riga, qui non
  identifica alcuna riga.
- Art. 7 §1 (i fornitori di portafogli sono le uniche entita' in grado di
  revocare gli attestati di unita' di portafoglio per le unita' che hanno
  fornito) -> Principio tipo "altro": enuncia una posizione giuridica di
  esclusivita' (non impone un comportamento al fornitore - la revoca gli e'
  riservata, non ordinata - ne' individua un diverso soggetto obbligato),
  quindi non rientra nella definizione di Obbligo di CONTEXT.md. Stesso
  trattamento dell'art. 4 §2 del Reg. 2025/1569, formulato in modo identico
  ("gli unici soggetti in grado di revocare"). `oggetti_giuridici` =
  ["portafoglio europeo di identità digitale"]: e' l'oggetto giuridico piu'
  vicino fra i valori censiti in `oggetti_giuridici` e la stessa scelta dei
  moduli gia' censiti che trattano il portafoglio (cap05 di questa Fonte,
  ETSI TS 119 432 cap04/cap07). L'"attestato di unità di portafoglio", che il
  testo nomina, non esiste come valore nell'insieme: non e' stato forzato.
- Art. 7 §2 (politica pubblicamente disponibile con condizioni e tempistiche
  di revoca) -> Obbligo "organizzativo" (documento di policy del fornitore),
  destinatario "Terzi affidanti/pubblico" perche' la politica e' destinata al
  pubblico (stesso trattamento dell'art. 4 §1 del Reg. 2025/1569). Art. 7 §3
  (informare gli utenti interessati entro 24 ore dalla revoca, indicando
  motivo e conseguenze, in modo conciso e con linguaggio semplice e chiaro) ->
  Obbligo "informativo/trasparenza", destinatario "Utente/titolare" (il testo
  nomina "gli utenti del portafoglio interessati"). Art. 7 §4 (rendere
  pubblicamente disponibile lo stato di validita' dell'attestato, con modalita'
  che ne preservano la riservatezza, e descrivere l'ubicazione di tali
  informazioni nell'attestato) -> Obbligo "informativo/trasparenza",
  destinatario "Terzi affidanti/pubblico" (la pubblicazione e' verso il
  pubblico, la riservatezza e' una modalita' della pubblicazione).
- Nessuna riga valorizza `severita` o `sanzioni`: l'atto non gradua i requisiti
  ne' prevede sanzioni proprie (identica scelta del cap04 e di tutte le Fonti
  di atti di esecuzione gia' censite). `stato` = "vigente" per tutte le righe.
- Unita' di indice: articolo + paragrafo numerato con "§" ("art. 3 §1") e
  lettera tra parentesi ("art. 5 §1(a)"), convenzione gia' in uso in questo
  censimento per gli atti di esecuzione eIDAS2 (Reg. 2025/1569 "art. 4 §3",
  "art. 4 §3(a)"; eIDAS2 "art. 5 bis §4(a)" in `app/seed.py`; Reg. 2025/2532
  "voce 4(a)"). Le rubriche degli articoli non sono item di indice (l'articolo
  e' coperto dai suoi commi) e neppure il titolo del Capo.
- `testo_integrale`: verbatim e integrale, ricucito dalle righe spezzate dalla
  conversione XHTML -> testo (lettere isolate su riga propria riunite al loro
  testo: "a) effettuino ...", "a) informano ..."), con l'intestazione
  "Articolo N" + rubrica nella prima riga di ogni articolo, dove il testo
  ufficiale la precede immediatamente. Le lettere di art. 5 §1 restano tutte
  dentro il `testo_integrale` della riga "art. 5 §1". Nessun marcatore di
  elisione (vincolo `verifica_completezza_testo_integrale`, ADR-0010).
  `testo` e' invece la sintesi compressa (1-3 frasi) di ogni comma.
- RELAZIONI: solo interne a questa Fonte, tutte con `fonte_id_o_None = None`
  su entrambi gli estremi e tutte verificate sul `testo_integrale` delle righe
  citate, quindi `evidence_type = "textual"`; `confidence` resta None perche'
  non esiste uno score reale da riportare (ADR-0005: non va inventato). Sono
  cinque rinvii letterali interni a questo capitolo: art. 3 §2 -> art. 6 §1 e
  art. 6 §2 ("attestato di unita' di portafoglio conforme ai requisiti di cui
  all'articolo 6": i requisiti sugli attestati sono nel §1 e nel §2, il §3
  riguarda i diritti dell'utente), art. 6 §2 -> art. 6 §1 ("di cui al
  paragrafo 1"), art. 6 §3(c) -> art. 6 §3(b) ("utilizzando i meccanismi di
  autenticazione di cui alla lettera(b)", citazione letterale con la
  parentesi come nel testo ufficiale) e art. 5 §2 -> allegato I ("le specifiche
  tecniche elencate nell'allegato I": unico rinvio che attraversa il confine
  di capitolo, dichiarato perche' la riga "allegato I" del cap05 e'
  verificabile sul file assegnato dal manifest, non perche' sia stato
  indovinato un riferimento). Non e' stata dichiarata alcuna
  relazione verso altre Fonti (art. 5 bis §4 eIDAS2 in art. 3 §1, Reg.
  2015/1502 in art. 4 §3, art. 5 §1(b) e §1(g), Reg. 2024/2980 in art. 3 §2):
  il collegamento cross-fonte e' la fase ADR-0009 della sessione principale,
  tentarlo qui in import parallelo per capitolo fa fallire il merge con
  KeyError. Nessuna relazione inferita e' stata aggiunta: i legami sostanziali
  che il testo non cita (es. la condizione di autenticazione riuscita condivisa
  da art. 3 §1 e art. 5 §1(a)) sarebbero un giudizio non verificabile dal
  testo e il capitolo resta leggibile integralmente contiguo. Avvertenza per
  l'audit `verifica_relazioni_textual.py`: tre di queste cinque relazioni
  compaiono nella sua sezione A ("citazioni dichiarate senza traccia del
  riferimento citato"). Non e' un'etichetta gonfiata: i rinvii sono letterali,
  ma lo strumento cerca nel testo citante una traccia del riferimento citato
  ("§ N"/"paragrafo N") e scarta le tracce di un solo carattere, mentre qui la
  forma usata dal testo ufficiale e' a livello di articolo ("i requisiti di cui
  all'articolo 6" in art. 3 §2) o di lettera ("i meccanismi di autenticazione
  di cui alla lettera(b)" in art. 6 §3(c)); fa eccezione art. 6 §2 -> art. 6
  §1, il cui testo cita "di cui al paragrafo 1" e supera il gate; anche art. 5
  §2 -> allegato I lo supera, perche' il suo testo cita "nell'allegato I".

Copertura: 24 item di indice, 16 righe (15 Obblighi + 1 Principio), 5
relazioni interne.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 3 §1",
        "testo": "Le unità di portafoglio non eseguono alcuna funzionalità di cui all'art. 5 bis, paragrafo 4, del regolamento (UE) n. 910/2014, con la sola eccezione dell'autenticazione dell'utente del portafoglio per l'accesso all'unità di portafoglio: le funzionalità del portafoglio restano inibite fino a quando l'unità di portafoglio non abbia autenticato con successo l'utente del portafoglio.",
        "testo_integrale": "Articolo 3\n\nIntegrità dell'unità di portafoglio\n\n1. Le unità di portafoglio non eseguono alcuna funzionalità di cui all'articolo 5 bis, paragrafo 4, del regolamento (UE) n. 910/2014, eccetto l'autenticazione dell'utente del portafoglio per l'accesso all'unità di portafoglio, fino a quando l'unità di portafoglio non abbia autenticato con successo l'utente del portafoglio.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 3 §2",
        "testo": "Per ciascuna unità di portafoglio, i fornitori di portafogli appongono una firma o un sigillo su almeno un attestato di unità di portafoglio conforme ai requisiti di cui all'art. 6; il certificato utilizzato per firmare o sigillare l'attestato è rilasciato sulla base di un certificato che figura nell'elenco di fiducia di cui al regolamento di esecuzione (UE) 2024/2980.",
        "testo_integrale": "2. Per ciascuna unità di portafoglio, i fornitori di portafogli appongono una firma o un sigillo su almeno un attestato di unità di portafoglio conforme ai requisiti di cui all'articolo 6. Il certificato utilizzato per firmare o sigillare l'attestato di unità di portafoglio è rilasciato sulla base di un certificato che figura nell'elenco di fiducia di cui al regolamento di esecuzione (UE) 2024/2980.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 4 §1",
        "testo": "Per gestire le risorse critiche le istanze di portafoglio utilizzano almeno un dispositivo crittografico sicuro per il portafoglio.",
        "testo_integrale": "Articolo 4\n\nIstanze di portafoglio\n\n1. Per gestire le risorse critiche le istanze di portafoglio utilizzano almeno un dispositivo crittografico sicuro per il portafoglio.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 4 §2",
        "testo": "I fornitori di portafogli garantiscono l'integrità, l'autenticità e la riservatezza della comunicazione tra le istanze di portafoglio e le applicazioni crittografiche sicure per il portafoglio.",
        "testo_integrale": "2. I fornitori di portafogli garantiscono l'integrità, l'autenticità e la riservatezza della comunicazione tra le istanze di portafoglio e le applicazioni crittografiche sicure per il portafoglio.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 4 §3",
        "testo": "Se le risorse critiche riguardano l'esecuzione dell'identificazione elettronica a un livello di garanzia elevato, le operazioni crittografiche del portafoglio o altre operazioni di trattamento di risorse critiche sono effettuate conformemente ai requisiti per le caratteristiche e la progettazione dei mezzi di identificazione elettronica a un livello di garanzia elevato stabiliti dal regolamento di esecuzione (UE) 2015/1502 della Commissione.",
        "testo_integrale": "3. Se le risorse critiche riguardano l'esecuzione dell'identificazione elettronica ad un livello di garanzia elevato, le operazioni crittografiche del portafoglio o altre operazioni di trattamento di risorse critiche sono effettuate conformemente ai requisiti per le caratteristiche e la progettazione dei mezzi di identificazione elettronica a un livello di garanzia elevato, come stabilito nel regolamento di esecuzione (UE) 2015/1502 della Commissione (11).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo se le risorse critiche riguardano l'esecuzione dell'identificazione elettronica ad un livello di garanzia elevato.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 5 §1",
        "testo": "I fornitori di portafogli garantiscono che le applicazioni crittografiche sicure per il portafoglio: a) effettuino operazioni crittografiche del portafoglio su risorse critiche diverse da quelle necessarie all'autenticazione dell'utente da parte dell'unità di portafoglio soltanto dopo aver autenticato con successo gli utenti; b) autentichino gli utenti, nel contesto dell'identificazione elettronica a un livello di garanzia elevato, conformemente ai requisiti del regolamento di esecuzione (UE) 2015/1502; c) siano in grado di generare in modo sicuro chiavi crittografiche nuove; d) siano in grado di effettuare la cancellazione sicura di risorse critiche; e) siano in grado di generare una prova del possesso di chiavi private; f) proteggano le chiavi private generate da tali applicazioni durante l'esistenza delle chiavi stesse; g) soddisfino i requisiti per le caratteristiche e la progettazione dei mezzi di identificazione elettronica a un livello di garanzia elevato del regolamento di esecuzione (UE) 2015/1502; h) siano gli unici componenti in grado di eseguire operazioni crittografiche del portafoglio e qualsiasi altra operazione con risorse critiche nel contesto dell'identificazione elettronica a un livello di garanzia elevato.",
        "testo_integrale": "Articolo 5\n\nApplicazioni crittografiche sicure per il portafoglio\n\n1. I fornitori di portafogli garantiscono che le applicazioni crittografiche sicure per il portafoglio:\n\na) effettuino operazioni crittografiche del portafoglio che coinvolgono risorse critiche diverse da quelle necessarie per l'autenticazione dell'utente del portafoglio da parte dell'unità di portafoglio soltanto nei casi in cui tali applicazioni abbiano autenticato con successo gli utenti del portafoglio;\n\nb) laddove autentichino gli utenti del portafoglio nel contesto della realizzazione dell'identificazione elettronica ad un livello di garanzia elevato, effettuino l'autenticazione degli utenti del portafoglio in conformità ai requisiti per le caratteristiche e la progettazione di mezzi di identificazione elettronica a un livello di garanzia elevato, come stabilito nel regolamento di esecuzione (UE) 2015/1502;\n\nc) siano in grado di generare in modo sicuro chiavi crittografiche nuove;\n\nd) siano in grado di effettuare la cancellazione sicura di risorse critiche;\n\ne) siano in grado di generare una prova del possesso di chiavi private;\n\nf) proteggano le chiavi private generate da tali applicazioni crittografiche sicure per il portafoglio durante l'esistenza delle chiavi stesse;\n\ng) soddisfino i requisiti per le caratteristiche e la progettazione di mezzi di identificazione elettronica a un livello di garanzia elevato, come stabilito nel regolamento di esecuzione (UE) 2015/1502;\n\nh) siano gli unici componenti in grado di eseguire operazioni crittografiche del portafoglio e qualsiasi altra operazione con risorse critiche nel contesto della realizzazione di un'identificazione elettronica ad un livello di garanzia elevato.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 5 §2",
        "testo": "Qualora decidano di fornire un'applicazione crittografica sicura per il portafoglio a un elemento sicuro integrato, i fornitori di portafogli basano la loro soluzione tecnica sulle specifiche tecniche elencate nell'allegato I o su altre specifiche tecniche equivalenti.",
        "testo_integrale": "2. Qualora decidano di fornire un'applicazione crittografica sicura per il portafoglio a un elemento sicuro integrato, i fornitori di portafogli basano la loro soluzione tecnica sulle specifiche tecniche elencate nell'allegato I o su altre specifiche tecniche equivalenti.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo qualora il fornitore di portafogli decida di fornire un'applicazione crittografica sicura per il portafoglio a un elemento sicuro integrato.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 6 §1",
        "testo": "I fornitori di portafogli garantiscono che ciascuna unità di portafoglio contenga attestati di unità di portafoglio.",
        "testo_integrale": "Articolo 6\n\nAutenticità e validità dell'unità di portafoglio\n\n1. I fornitori di portafogli garantiscono che ciascuna unità di portafoglio contenga attestati di unità di portafoglio.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 6 §2",
        "testo": "I fornitori di portafogli garantiscono che gli attestati di unità di portafoglio di cui al paragrafo 1 contengano chiavi pubbliche e che le corrispondenti chiavi private siano protette da un dispositivo crittografico sicuro per il portafoglio.",
        "testo_integrale": "2. I fornitori di portafogli garantiscono che gli attestati di unità di portafoglio di cui al paragrafo 1 contengano chiavi pubbliche e che le corrispondenti chiavi private siano protette da un dispositivo crittografico sicuro per il portafoglio.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 6 §3(a)",
        "testo": "I fornitori di portafogli informano gli utenti del portafoglio in merito ai loro diritti e obblighi in relazione alla loro unità di portafoglio.",
        "testo_integrale": "3. I fornitori di portafogli:\n\na) informano gli utenti del portafoglio in merito ai loro diritti e obblighi in relazione alla loro unità di portafoglio;",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 6 §3(b)",
        "testo": "I fornitori di portafogli forniscono meccanismi, indipendenti dalle unità di portafoglio, per l'identificazione e l'autenticazione sicure degli utenti del portafoglio.",
        "testo_integrale": "b) forniscono meccanismi, indipendenti dalle unità di portafoglio, per l'identificazione e l'autenticazione sicure degli utenti del portafoglio;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 6 §3(c)",
        "testo": "I fornitori di portafogli garantiscono che gli utenti del portafoglio abbiano il diritto di chiedere la revoca dei loro attestati di unità di portafoglio, utilizzando i meccanismi di autenticazione di cui alla lettera b).",
        "testo_integrale": "c) garantiscono che gli utenti del portafoglio abbiano il diritto di chiedere la revoca dei loro attestati di unità di portafoglio, utilizzando i meccanismi di autenticazione di cui alla lettera(b).",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 7 §2",
        "testo": "I fornitori di portafogli stabiliscono una politica pubblicamente disponibile che specifichi le condizioni e le tempistiche per la revoca degli attestati di unità di portafoglio.",
        "testo_integrale": "2. I fornitori di portafogli stabiliscono una politica pubblicamente disponibile che specifichi le condizioni e le tempistiche per la revoca degli attestati di unità di portafoglio.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 7 §3",
        "testo": "Qualora abbiano revocato gli attestati di unità di portafoglio, i fornitori di portafogli informano gli utenti del portafoglio interessati entro 24 ore dalla revoca delle loro unità di portafoglio, indicando il motivo della revoca e le conseguenze per l'utente; le informazioni sono fornite in maniera concisa, facilmente accessibile e con un linguaggio semplice e chiaro.",
        "testo_integrale": "3. Qualora abbiano revocato gli attestati di unità di portafoglio, i fornitori di portafogli informano gli utenti del portafoglio interessati entro 24 ore dalla revoca delle loro unità di portafoglio, indicando altresì il motivo della revoca e le conseguenze per l'utente del portafoglio. Tali informazioni sono fornite in maniera concisa, facilmente accessibile e utilizzando un linguaggio semplice e chiaro.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 7 §4",
        "testo": "Qualora abbiano revocato gli attestati di unità di portafoglio, i fornitori di portafogli rendono pubblicamente disponibili lo stato di validità dell'attestato secondo modalità che ne preservano la riservatezza e descrivono l'ubicazione di tali informazioni nell'attestato di unità di portafoglio.",
        "testo_integrale": "4. Qualora abbiano revocato gli attestati di unità di portafoglio, i fornitori di portafogli rendono pubblicamente disponibili lo stato di validità dell'attestato di unità di portafoglio secondo modalità che ne preservano la riservatezza e descrivono l'ubicazione di tali informazioni nell'attestato di unità di portafoglio.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 7 §1",
        "testo": "I fornitori di portafogli sono le uniche entità in grado di revocare gli attestati di unità di portafoglio per le unità di portafoglio che hanno fornito.",
        "testo_integrale": "Articolo 7\n\nRevoca degli attestati di unità di portafoglio\n\n1. I fornitori di portafogli sono le uniche entità in grado di revocare gli attestati di unità di portafoglio per le unità di portafoglio che hanno fornito.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["portafoglio europeo di identità digitale"],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 3 §1",
    "art. 3 §2",
    "art. 4 §1",
    "art. 4 §2",
    "art. 4 §3",
    "art. 5 §1",
    "art. 5 §1(a)",
    "art. 5 §1(b)",
    "art. 5 §1(c)",
    "art. 5 §1(d)",
    "art. 5 §1(e)",
    "art. 5 §1(f)",
    "art. 5 §1(g)",
    "art. 5 §1(h)",
    "art. 5 §2",
    "art. 6 §1",
    "art. 6 §2",
    "art. 6 §3(a)",
    "art. 6 §3(b)",
    "art. 6 §3(c)",
    "art. 7 §1",
    "art. 7 §2",
    "art. 7 §3",
    "art. 7 §4",
]

MAPPATURA_LOCALE = {
    "art. 3 §1": ["art. 3 §1"],
    "art. 3 §2": ["art. 3 §2"],
    "art. 4 §1": ["art. 4 §1"],
    "art. 4 §2": ["art. 4 §2"],
    "art. 4 §3": ["art. 4 §3"],
    "art. 5 §1": [
        "art. 5 §1",
        "art. 5 §1(a)",
        "art. 5 §1(b)",
        "art. 5 §1(c)",
        "art. 5 §1(d)",
        "art. 5 §1(e)",
        "art. 5 §1(f)",
        "art. 5 §1(g)",
        "art. 5 §1(h)",
    ],
    "art. 5 §2": ["art. 5 §2"],
    "art. 6 §1": ["art. 6 §1"],
    "art. 6 §2": ["art. 6 §2"],
    "art. 6 §3(a)": ["art. 6 §3(a)"],
    "art. 6 §3(b)": ["art. 6 §3(b)"],
    "art. 6 §3(c)": ["art. 6 §3(c)"],
    "art. 7 §1": ["art. 7 §1"],
    "art. 7 §2": ["art. 7 §2"],
    "art. 7 §3": ["art. 7 §3"],
    "art. 7 §4": ["art. 7 §4"],
}

# Relazioni interne a questa Fonte (fonte_id_o_None = None su entrambi gli
# estremi), tutte rinvii letterali verificati sul `testo_integrale` delle righe
# coinvolte: art. 3 §2 cita "i requisiti di cui all'articolo 6" (rinvio all'art.
# 6 in blocco, i cui requisiti sugli attestati stanno nel §1 e nel §2 - il §3
# riguarda i diritti dell'utente e non e' un requisito dell'attestato); art. 6
# §2 cita "gli attestati di unità di portafoglio di cui al paragrafo 1"; art. 6
# §3(c) cita "i meccanismi di autenticazione di cui alla lettera(b)"; art. 5 §2
# cita "le specifiche tecniche elencate nell'allegato I". I rinvii ad altre
# Fonti (art. 5 bis §4 eIDAS2 in art. 3 §1, Reg. 2015/1502 in art. 4 §3 e
# art. 5 §1, Reg. 2024/2980 in art. 3 §2) non sono dichiarati qui: sono
# collegamenti cross-fonte di competenza della sessione principale (fase
# ADR-0009). Il rinvio all'allegato I e' invece dichiarato: la riga "allegato I"
# del cap05 e' verificabile sul file assegnato dal manifest, non indovinata.
# `confidence` = None: nessuno score reale da riportare.
RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "art. 3 §2"),
        "nodo_a": ("obbligo", None, "art. 6 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 3 §2"),
        "nodo_a": ("obbligo", None, "art. 6 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 6 §2"),
        "nodo_a": ("obbligo", None, "art. 6 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 6 §3(c)"),
        "nodo_a": ("obbligo", None, "art. 6 §3(b)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 5 §2"),
        "nodo_a": ("principio", None, "allegato I"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
