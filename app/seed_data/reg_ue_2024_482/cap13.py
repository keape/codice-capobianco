"""Regolamento di esecuzione (UE) 2024/482 della Commissione, del 31 gennaio
2024 - modalita' di applicazione del regolamento (UE) 2019/881 del Parlamento
europeo e del Consiglio per quanto riguarda l'adozione del sistema europeo di
certificazione della cibersicurezza basato sui criteri comuni (EUCC). Fonte 29
(slug `reg_ue_2024_482`), capitolo 13 di 14 (vedi
app/.source_cache/reg_ue_2024_482/manifest.json): Allegati VI-VIII (valutazione
inter pares, contenuto del certificato EUCC, dichiarazione del pacchetto di
affidabilita'). Gli artt. 1-50 e gli allegati I-V e IX appartengono ai capitoli
1-12 e 14 della stessa Fonte, assegnati ad altri moduli: nessuno di quei file e'
toccato qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_482/cap13.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R0482, lingua italiana; URL
risolto
http://publications.europa.eu/resource/cellar/687c0d05-c580-11ee-95d9-01aa75ed71a1.0014.03/DOC_1,
XHTML della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 540.435 byte
scaricati, 135.367 caratteri di testo, sha256 del raw.txt
b46d08cab6d63b2c190ae767042c07c1fc324955c22ef491eb314556b28ca5b8 - dettagli
completi in app/.source_cache/reg_ue_2024_482/provenance.json). La porzione
assegnata contiene tre allegati per intero: l'allegato VI (dall'intestazione
"ALLEGATO VI" alla riga che precede "ALLEGATO VII"), l'allegato VII
(dall'intestazione "ALLEGATO VII" alla riga che precede "ALLEGATO VIII") e
l'allegato VIII (dall'intestazione "ALLEGATO VIII" a fine porzione; la riga ELI
e la riga ISSN chiudono il documento in coda all'allegato IX, cioe' nel cap14).
Il preambolo (considerando 1-33) e' a monte degli allegati e non e' in questa
porzione.

Modellazione (ADR-0007, nessun punto o lettera non coperto, nessuno coperto due
volte):
- Paratesto -> nessun nodo proprio: le tre intestazioni di allegato ("ALLEGATO
  VI/VII/VIII") con i loro titoli ("AMBITO DELLA VALUTAZIONE INTER PARES E
  COMPOSIZIONE DEL GRUPPO DI VALUTAZIONE", "Contenuto del certificato EUCC",
  "Dichiarazione del pacchetto di affidabilita'") e le due intestazioni di
  sezione interne all'allegato VI ("VI.1 Ambito della valutazione inter pares",
  "VI.2 Gruppo di valutazione inter pares") non sono unita' normative ma
  struttura dell'atto: intestazioni e titoli restano assorbiti nel
  `testo_integrale` della prima riga di ciascun allegato/sezione (convenzione
  dell'allegato III del cap10 di questa Fonte), i marcatori isolati su riga
  propria ("1.", "(a)", "(1)") sono riuniti al testo che introducono. In questa
  porzione non compaiono epigrafe, firma, formula di chiusura, note a pie' di
  pagina ne' riga ELI: nessuno di questi elementi produce nodo o item di
  indice.
- Riferimenti delle righe: i tre allegati sono distinti dal nome dell'allegato
  ("allegato VI", "allegato VII", "allegato VIII", come richiesto dalla nota di
  capitolo). All'interno dell'allegato VI i due gruppi di punti numerati sono
  separati dal numero di sezione ("allegato VI, sezione VI.1, punto 2" rispetto
  a "allegato VI, sezione VI.2, punto 2"): la numerazione dei punti riparte da
  1 in ciascuna sezione e due riferimenti identici colliderebbero nel registro
  del seed. Nell'allegato VII gli elementi di primo livello sono lettere
  (a)-(d), quindi i punti annidati si riferiscono come "allegato VII, lettera
  b), punto 3"; nell'allegato VIII i punti numerati 1-3 sono di primo livello e
  le loro lettere si riferiscono come "allegato VIII, punto 3(a)".
- Item a livello di allegato: esiste solo dove una riga copre intestazione,
  titolo e chapeau dell'allegato intero ("allegato VII", il cui chapeau "Il
  certificato EUCC deve contenere almeno i seguenti elementi:" e' il veicolo
  dell'obbligo di contenuto minimo del certificato). Per gli allegati VI e VIII
  non esiste item a livello di allegato: li' la prima unita' numerata assorbe
  intestazione e titolo e non c'e' un chapeau proprio dell'allegato (convenzione
  del cap05 del Reg. 2024/2979, "nessun item a livello di allegato perche' un
  item unico non sarebbe mappabile su righe distinte").
- Allegato VI, sezione VI.1, punto 1 (chapeau "Sono contemplati i tipi di
  valutazione inter pares seguenti:" + lettere (a)-(c): tipo 1, attivita' di
  certificazione al livello AVA_VAN.3; tipo 2, attivita' di certificazione
  relative a un settore tecnico elencato come documento sullo stato dell'arte
  nell'allegato I; tipo 3, attivita' al di sopra del livello AVA_VAN.3 facendo
  uso di un profilo di protezione elencato nell'allegato II o III) -> UN SOLO
  Principio "scopo/ambito di applicazione", con i quattro item ("punto 1",
  "punto 1(a)", "punto 1(b)", "punto 1(c)") mappati alla stessa riga: il punto
  delimita quali attivita' di certificazione rientrano nella valutazione inter
  pares e non impone un comportamento ne' attribuisce un diritto; le tre
  lettere non hanno precetto autonomo, sono le voci dell'elenco retto dal
  chapeau (stessa struttura del chapeau con elenco del cap10 di questa Fonte e
  dell'elenco definitorio di un articolo). Scartato "definitorio": le lettere
  non definiscono un termine impiegato altrove nel censimento ma descrivono
  l'attivita' di certificazione contemplata, cioe' l'ambito della valutazione -
  la voce che il censimento riserva alle clausole di ambito. Nessun
  `oggetti_giuridici`: fra gli oggetti censiti non c'e' la certificazione di
  prodotti TIC, e la voce generica "altro" non e' stata forzata (stesso
  criterio del cap10 di questa Fonte).
- Allegato VI, sezione VI.1, punto 2 (chapeau "L'organismo di certificazione
  oggetto di valutazione inter pares presenta l'elenco dei prodotti TIC
  certificati che possono essere candidati al riesame da parte del gruppo di
  valutazione inter pares in conformita' delle norme seguenti:" + lettere
  (a)-(c)) -> UNA SOLA riga Obbligo "procedurale", con i quattro item ("punto
  2", "punto 2(a)", "2(b)", "2(c)") mappati alla stessa riga: il chapeau porta
  predicato e soggetto (l'organismo presenta l'elenco) e le lettere sono le
  norme di composizione di quell'elenco (copertura dell'ambito di applicazione
  tecnico dell'autorizzazione, con almeno due diverse valutazioni di prodotti
  al livello di affidabilita' «elevato» e un profilo di protezione se
  l'organismo ha rilasciato un certificato a quel livello; almeno un prodotto
  per settore tecnico e per ITSEF per la valutazione di tipo 2; almeno un
  prodotto candidato conforme a un profilo di protezione applicabile e
  pertinente per la valutazione di tipo 3) - modello dell'art. 11 §3 del cap02
  di questa Fonte (chapeau + lettere = una riga). Tipo "procedurale" e non
  "informativo/trasparenza": l'elenco e' l'input documentale del riesame
  condotto dal gruppo di valutazione, non una comunicazione verso il mercato o
  il pubblico (stessa discriminante dell'art. 16 del cap03 di questa Fonte).
  Soggetto obbligato "Terza parte": l'organismo di certificazione oggetto di
  valutazione e' l'attore nominato dal testo.
- Allegato VI, sezione VI.2, punto 1 (composizione del gruppo: almeno due
  esperti, ciascuno selezionato da un diverso organismo di certificazione di un
  diverso Stato membro che rilascia certificati al livello di affidabilita'
  «elevato»; gli esperti devono dimostrare di possedere le competenze
  necessarie per le norme di cui all'articolo 3 e per i documenti sullo stato
  dell'arte che rientrano nell'ambito della valutazione) -> Obbligo
  "organizzativo": il punto non si limita a descrivere una composizione, ma
  prescrive un requisito di competenza in capo agli esperti ("devono
  dimostrare"), ed e' un requisito su persone e ruoli, cioe' organizzativo -
  nessuna delle lettere ha precetto autonomo, trattandosi di un unico requisito
  di composizione. Soggetto obbligato "Terza parte" (gli esperti selezionati
  dagli organismi di certificazione, attori del sistema EUCC).
- Allegato VI, sezione VI.2, punto 2 (in caso di delega per il rilascio dei
  certificati o previa approvazione degli stessi di cui all'articolo 56,
  paragrafo 6, del regolamento (UE) 2019/881, al gruppo partecipa anche un
  esperto dell'autorita' nazionale di certificazione della cibersicurezza
  correlata all'organismo interessato) -> Obbligo "organizzativo", con
  `condizione_applicabilita` (la prescrizione opera solo in caso di delega o
  previa approvazione dei certificati da parte di un'autorita' nazionale ai
  sensi dell'art. 56 §6 del regolamento (UE) 2019/881: e' un fatto esterno non
  tracciato come nodo, quindi va in testo libero e non in una relazione -
  criterio dichiarato nel cap02 di questa Fonte). Soggetto obbligato "Terza
  parte" (l'autorita' nazionale correlata, tramite il proprio esperto).
- Allegato VI, sezione VI.2, punto 3 (per una valutazione inter pares di tipo
  2, i membri del gruppo sono selezionati tra gli organismi di certificazione
  autorizzati per il settore tecnico in questione) -> Obbligo "organizzativo":
  requisito di selezione dei membri del gruppo. La condizione dell'applicabilita'
  e' un nodo di questo stesso modulo (i tipi di valutazione inter pares definiti
  dal punto 1 della sezione VI.1), quindi non e' ripetuta in
  `condizione_applicabilita` ma dichiarata come relazione "è condizionato da"
  verso "allegato VI, sezione VI.1, punto 1" (criterio del cap02 di questa
  Fonte). Soggetto obbligato "Terza parte" (i membri selezionati, cioe' gli
  organismi di certificazione autorizzati per il settore tecnico).
- Allegato VI, sezione VI.2, punto 4 (ogni membro del gruppo possiede almeno
  due anni di esperienza nello svolgimento di attivita' di certificazione
  presso un organismo di certificazione) -> Obbligo "organizzativo": requisito
  di esperienza dei membri. Soggetto obbligato "Terza parte" (i membri del
  gruppo).
- Allegato VI, sezione VI.2, punto 5 (per una valutazione inter pares di tipo 2
  o 3, ogni membro possiede almeno due anni di esperienza nel settore tecnico o
  nel profilo di protezione pertinente e una comprovata esperienza e
  partecipazione nell'ambito dell'autorizzazione di un'ITSEF) -> Obbligo
  "organizzativo", condizionato dai tipi 2 e 3: come per il punto 3 la
  condizione e' un nodo di questo modulo, dichiarata con la relazione
  "è condizionato da" verso "allegato VI, sezione VI.1, punto 1". Soggetto
  obbligato "Terza parte" (i membri del gruppo).
- Allegato VI, sezione VI.2, punto 6 (l'autorita' nazionale di certificazione
  della cibersicurezza che controlla e vigila sull'organismo oggetto di
  valutazione e almeno un'autorita' nazionale di certificazione della
  cibersicurezza il cui organismo non e' soggetto alla valutazione inter pares
  partecipano in qualita' di osservatori; anche l'ENISA puo' partecipare in
  qualita' di osservatore) -> UNA SOLA riga Obbligo "procedurale": la prima
  frase e' una prescrizione di partecipazione, la seconda una facolta' di ENISA
  nello stesso punto - classificato Obbligo perche' l'unita' di copertura
  contiene un precetto autonomo, e "procedurale" e non "organizzativo" perche'
  disciplina lo svolgimento della valutazione inter pares (partecipazione di
  osservatori), non la composizione del gruppo di esperti. Soggetto obbligato
  "Terza parte" (le autorita' nazionali di certificazione della cibersicurezza;
  l'ENISA e' il titolare della facolta' della seconda frase).
- Allegato VI, sezione VI.2, punto 7 (la composizione del gruppo e' presentata
  all'organismo di certificazione oggetto di valutazione; in casi giustificati
  quest'ultimo puo' contestarla e chiederne la revisione) -> UNA SOLA riga
  Obbligo "procedurale", con `condizione_applicabilita` per la facolta' di
  contestazione ("in casi giustificati", fatto esterno non tracciato): la
  presentazione della composizione e' un adempimento procedurale del processo
  di valutazione inter pares, e la contestazione e' il diritto correlativo
  nello stesso punto. Soggetto obbligato "Terza parte": il testo non nomina chi
  presenta la composizione (costruzione passiva), ma l'attore e' il processo di
  valutazione inter pares, cioe' il gruppo e gli organismi che lo compongono -
  la convenzione di questo capitolo (sotto) e' di attribuire "Terza parte" a
  tutti gli obbligati di soggetto istituzionale del sistema EUCC, come fa il
  cap02 di questa Fonte.
- Allegato VII, chapeau ("Il certificato EUCC deve contenere almeno i seguenti
  elementi:") -> riga Obbligo "informativo/trasparenza" con item "allegato VII"
  (intestazione, titolo e chapeau): il chapeau e' il veicolo dell'obbligo di
  contenuto minimo del certificato - il testo non nomina l'organismo che
  rilascia il certificato, ma l'obbligo di contenuto grava su chi lo rilascia
  (la lettera (c) punto 1 nomina "l'organismo di certificazione che ha
  rilasciato il certificato"), quindi la riga ha soggetto obbligato "Terza
  parte" per la stessa ragione dell'art. 10 §1 del cap02 di questa Fonte
  ("Il certificato EUCC contiene almeno le informazioni di cui all'allegato
  VII", Obbligo "informativo/trasparenza" con soggetto obbligato "Terza
  parte"). Tipo "informativo/trasparenza": e' contenuto informativo del
  certificato, cioe' informazione resa al mercato e al titolare (criterio
  dichiarato nel cap02 di questa Fonte per l'art. 10 §1-§2).
- Allegato VII, lettere (a)-(d): UNA riga per lettera, non una per punto
  annidato. La lettera e' l'unita' che raggruppa un insieme omogeneo di
  elementi del certificato (a: identificatore unico; b: informazioni sul
  prodotto TIC o profilo di protezione certificato e sul titolare; c:
  informazioni sulla valutazione e sulla certificazione; d: marchio ed
  etichetta), i punti (1)-(5) della lettera b) e (1)-(11) della lettera c) ne
  sono il contenuto specificativo senza precetto autonomo: stessa convenzione
  delle lettere dell'allegato III del cap10 di questa Fonte (un nodo per
  lettera, item separato per ogni punto, mappato alla riga della lettera).
  Tutte Obbligo "informativo/trasparenza" (contenuto informativo del
  certificato) con soggetto obbligato "Terza parte" (l'organismo di
  certificazione che rilascia il certificato). La lettera (d) rinvia al marchio
  e all'etichetta dell'articolo 11: la riga resta un Obbligo di contenuto del
  certificato (il certificato deve contenere anche il marchio e l'etichetta
  associati), non una mera designazione. La lettera (c) punto 8 cita "in
  conformita' dell'allegato VIII": la citazione e' all'allegato intero, che in
  questo modulo non ha un nodo proprio (l'allegato VIII non ha chapeau, quindi
  nessun item a livello di allegato), per cui la relazione e' dichiarata verso
  i due punti che ne disciplinano il contenuto richiamato (punto 1, incrementi;
  punto 3, pacchetti di affidabilita') con `evidence_type` "inferred", non
  "textual": un arco verso un riferimento inesistente farebbe fallire il seed
  con KeyError.
- Allegato VIII, punto 1 (chapeau "Contrariamente alle definizioni di cui ai
  criteri comuni, un incremento:" + lettere (a)-(c): non identificato con
  l'abbreviazione «+»; indicato in dettaglio con un elenco di tutti i
  componenti interessati; descritto dettagliatamente nella relazione di
  certificazione) -> UNA SOLA riga Obbligo "informativo/trasparenza", con i
  quattro item ("punto 1", "punto 1(a)", "punto 1(b)", "punto 1(c)") mappati
  alla stessa riga: il chapeau non contiene un predicato proprio e le tre
  lettere sono le regole sul trattamento dell'incremento, che e' unico. Tipo
  "informativo/trasparenza": le tre lettere riguardano come l'incremento e'
  designato e documentato (divieto dell'abbreviazione «+», elenco dei
  componenti, descrizione nella relazione di certificazione), cioe' il
  contenuto della documentazione di certificazione - stessa classificazione
  dell'art. 10 §2 del cap02 di questa Fonte. Scartato "definitorio" (il punto
  non definisce un termine ma prescrive come si presenta l'incremento, "non e'
  identificato", "e' indicato", "e' descritto") e scartato "procedurale" (non
  disciplina un passo del procedimento ma il contenuto documentale). Soggetto
  obbligato "Terza parte" (gli organismi che producono certificato e relazione
  di certificazione).
- Allegato VIII, punto 2 ("Il livello di affidabilita' confermato in un
  certificato EUCC puo' essere integrato dal livello di garanzia della
  valutazione di cui all'articolo 3 del presente regolamento.") -> Principio
  "altro": il punto e' una facolta' (il livello puo' essere integrato), non un
  comportamento imposto ne' un diritto esercitabile nei confronti di un altro
  soggetto - stesso trattamento della disposizione permissiva dell'art. 18 §2
  del cap03 di questa Fonte e dell'art. 1 §2 del Reg. 2025/2532. Nessun
  `oggetti_giuridici`: l'oggetto e' il livello di affidabilita' del certificato
  EUCC, che non figura fra gli oggetti censiti.
- Allegato VIII, punto 3 (se il livello di affidabilita' confermato in un
  certificato EUCC non si riferisce a un incremento, il certificato EUCC indica
  uno dei pacchetti seguenti: "il pacchetto di affidabilita' specifico";
  "il pacchetto di affidabilita' conforme a un profilo di protezione" nel caso
  in cui si faccia riferimento a un profilo di protezione senza un livello di
  garanzia della valutazione) -> UNA SOLA riga Obbligo "informativo/trasparenza"
  con i tre item ("punto 3", "punto 3(a)", "punto 3(b)") mappati alla stessa
  riga: il chapeau contiene predicato e soggetto (il certificato EUCC indica uno
  dei pacchetti seguenti) e le due lettere sono le alternative ammesse, non
  precetti autonomi; tipo "informativo/trasparenza" perche' riguarda
  l'informazione resa sul certificato. `condizione_applicabilita` valorizzata
  con la condizione del chapeau (il livello di affidabilita' confermato non si
  riferisce a un incremento), che e' un fatto del certificato e non un nodo
  tracciato. Soggetto obbligato "Terza parte".
- Soggetti: tutte le righe Obbligo di questo capitolo dichiarano `soggetti` =
  [{"categoria": "Terza parte", "ruolo": "obbligato"}] e nessuna dichiara un
  destinatario. Motivo: nessun attore di questi tre allegati e' un QTSP, un
  utente/titolare o un terzo affidante - sono l'organismo di certificazione
  oggetto di valutazione inter pares, gli esperti e il gruppo di valutazione,
  l'ITSEF, l'autorita' nazionale di certificazione della cibersicurezza e
  l'ENISA - e "Terza parte" e' la categoria con cui il cap02 di questa stessa
  Fonte ha dichiarato tutti gli obbligati di soggetto istituzionale o
  industriale del sistema EUCC (richiedente la certificazione, organismo di
  certificazione, ITSEF, autorita' nazionale, ENISA). L'alternativa (nessun
  soggetto, come per le righe che gravano su una pubblica amministrazione senza
  categoria propria) e' stata scartata per coerenza con il cap02 della stessa
  Fonte, che ha gia' trattato questi attori come "Terza parte". Nessun
  destinatario e' stato inferito: l'unico destinatario nominato e' il gruppo di
  valutazione inter pares (l'elenco dei prodotti candidati del punto 2) e
  l'organismo di certificazione oggetto di valutazione (la composizione del
  gruppo nel punto 7), cioe' gli stessi attori del sistema gia' rappresentati
  come obbligati.
- `condizione_applicabilita`: valorizzata solo dove la condizione e' un fatto
  esterno non tracciato ("allegato VI, sezione VI.2, punto 2": delega o
  approvazione dei certificati ai sensi dell'art. 56 §6 del regolamento (UE)
  2019/881; "punto 7": i "casi giustificati" della contestazione; "allegato
  VIII, punto 3": il livello di affidabilita' confermato non si riferisce a un
  incremento). Non e' stata usata per i tipi 1/2/3 di valutazione inter pares,
  che sono un nodo di questo modulo e sono dichiarati con la relazione
  "è condizionato da" (punti 3 e 5 della sezione VI.2).
- `testo_integrale`: verbatim e integrale, ricucito dalle righe spezzate dalla
  conversione XHTML -> testo. I marcatori isolati su riga propria ("1.", "2.",
  "(a)", "(1)") sono riuniti al testo che introducono; i punti, le lettere e i
  capoversi restano separati da riga vuota; l'intestazione dell'allegato con il
  suo titolo e' premessa alla prima riga di ciascun allegato e l'intestazione di
  sezione alla prima riga della sezione (mai ripetute nelle righe successive);
  non e' ripetuto in ogni riga il chapeau degli elenchi (allegato VI punto 1 e
  punto 2, allegato VIII punto 1 e punto 3): il suo contenuto resta nel nodo che
  lo contiene. Simboli ufficiali (« ») conservati come pubblicati; nessun
  marcatore di elisione (vincolo `verifica_completezza_testo_integrale`,
  ADR-0010). `testo` e' la sintesi in 1-3 frasi di ciascuna riga, che nomina
  tutte le prescrizioni autonome contenute nelle lettere accorpate.
- `stato` = "vigente" per tutte le righe. Nessuna riga valorizza `severita` o
  `sanzioni`: l'atto non gradua i requisiti ne' prevede sanzioni proprie.

Relazioni dichiarate (solo fra righe di questo modulo, `fonte_id_o_None = None`
su entrambi gli estremi): dodici. Una sola e' `evidence_type` "textual", perche'
cita letteralmente la riga di destinazione: "allegato VI, sezione VI.2, punto
2" -> "allegato VI, sezione VI.2, punto 1" ("al gruppo di esperti selezionato in
conformita' del paragrafo 1 della presente sezione"). Le altre undici sono
"inferred": le due relazioni di "allegato VII, lettera c)" verso "allegato
VIII, punto 1" e "allegato VIII, punto 3" (la citazione letterale e' all'allegato
VIII intero, che non ha un nodo proprio: vedi sopra); le quattro lettere
dell'allegato VII
"specificano" il chapeau "allegato VII" (il chapeau designa "i seguenti
elementi" senza citare le lettere; direzione specifico -> generale, come le
lettere dell'allegato III del cap10 di questa Fonte); "allegato VI, sezione
VI.1, punto 2" e "allegato VI, sezione VI.2, punto 7" "richiamano"
rispettivamente i tipi di valutazione inter pares di "allegato VI, sezione VI.1,
punto 1" (lettere b) e c), le sole condizionate al tipo) e la composizione del
gruppo di "allegato VI, sezione VI.2, punto 1"; "allegato VI, sezione VI.2,
punto 3" e "punto 5" sono "è condizionato da" "allegato VI, sezione VI.1, punto
1"; "allegato VIII, punto 3" "richiama" "allegato VIII, punto 1" (la condizione
del punto 3 e' che il livello confermato non si riferisca a un incremento,
istituto del punto 1). `confidence` resta None su tutte: nessuno score reale da
riportare (ADR-0005: non va inventato).

Rinvii demandati alla fase 6 (nessuna relazione dichiarata verso di essi: sono
altri capitoli di questa stessa Fonte o altre Fonti):
- allegati e articoli di questa Fonte: allegato I e allegato II/III (lettere b)
  e c) del punto 1 della sezione VI.1) -> cap09 e cap10; allegato V (lettera c)
  punto 5 dell'allegato VII) -> cap12; articolo 3 (punto 1 della sezione VI.2 e
  lettere c) punti 7 e 8 dell'allegato VII, punto 2 dell'allegato VIII) ->
  cap01; articolo 4 (lettera c) punto 6 dell'allegato VII) -> cap01; articolo 11
  (lettera d) dell'allegato VII) -> cap02; articolo 56 §6 del regolamento (UE)
  2019/881 (punto 2 della sezione VI.2) e articolo 55 del medesimo regolamento
  (lettera b) punto 5 dell'allegato VII) -> altra Fonte, non censita;
- "i criteri comuni" richiamati dal punto 1 dell'allegato VIII (le definizioni
  dello standard ISO/IEC 15408, citato dall'art. 3 di questa Fonte ma non
  censito come Fonte autonoma): nessun arco;
- il rinvio entrante dall'art. 10 §1 di questa Fonte (cap02) all'allegato VII e
  il rinvio dall'articolo 3 al livello di garanzia della valutazione (punto 2
  dell'allegato VIII) sono collegamenti da costruire in fase 6 sui nodi di
  questo modulo, non su questo file.

Copertura: 44 item di indice, 17 righe (15 Obblighi + 2 Principi), 12 relazioni
interne.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "allegato VI, sezione VI.1, punto 2",
        "testo": "L'organismo di certificazione oggetto di valutazione inter pares presenta l'elenco dei prodotti TIC certificati che possono essere candidati al riesame da parte del gruppo di valutazione inter pares in conformità delle norme seguenti: i prodotti candidati coprono l'ambito di applicazione tecnico dell'autorizzazione dell'organismo, con almeno due diverse valutazioni di prodotti al livello di affidabilità «elevato» e un profilo di protezione se l'organismo ha rilasciato un certificato a quel livello; per una valutazione inter pares di tipo 2 presenta almeno un prodotto per settore tecnico e per ITSEF interessata; per una valutazione inter pares di tipo 3 è valutato almeno un prodotto candidato conformemente a un profilo di protezione applicabile e pertinente.",
        "testo_integrale": "2. L'organismo di certificazione oggetto di valutazione inter pares presenta l'elenco dei prodotti TIC certificati che possono essere candidati al riesame da parte del gruppo di valutazione inter pares in conformità delle norme seguenti:\n\n(a) i prodotti candidati coprono l'ambito di applicazione tecnico dell'autorizzazione dell'organismo di certificazione, di cui saranno analizzate almeno due diverse valutazioni di prodotti al livello di affidabilità «elevato» attraverso la valutazione inter pares, e un profilo di protezione se l'organismo di certificazione ha rilasciato un certificato al livello di affidabilità «elevato»;\n\n(b) per una valutazione inter pares di tipo 2, l'organismo di certificazione presenta almeno un prodotto per settore tecnico e per ITSEF interessata;\n\n(c) per una valutazione inter pares di tipo 3, è valutato almeno un prodotto candidato conformemente a un profilo di protezione applicabile e pertinente.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato VI, sezione VI.2, punto 1",
        "testo": "Il gruppo di valutazione è composto da almeno due esperti, ciascuno dei quali selezionato da un diverso organismo di certificazione di un diverso Stato membro che rilascia certificati al livello di affidabilità «elevato»; gli esperti devono dimostrare di possedere le competenze necessarie per quanto riguarda le norme di cui all'articolo 3 e i documenti sullo stato dell'arte che rientrano nell'ambito della valutazione inter pares.",
        "testo_integrale": "VI.2 Gruppo di valutazione inter pares\n\n1. Il gruppo di valutazione è composto da almeno due esperti, ciascuno dei quali selezionato da un diverso organismo di certificazione di un diverso Stato membro che rilascia certificati al livello di affidabilità «elevato». Gli esperti devono dimostrare di possedere le competenze necessarie per quanto riguarda le norme di cui all'articolo 3 e i documenti sullo stato dell'arte che rientrano nell'ambito della valutazione inter pares.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato VI, sezione VI.2, punto 2",
        "testo": "In caso di delega per il rilascio dei certificati o previa approvazione degli stessi di cui all'articolo 56, paragrafo 6, del regolamento (UE) 2019/881, al gruppo di esperti selezionato in conformità del paragrafo 1 della presente sezione partecipa anche un esperto dell'autorità nazionale di certificazione della cibersicurezza correlata all'organismo di certificazione interessato.",
        "testo_integrale": "2. In caso di delega per il rilascio dei certificati o previa approvazione degli stessi di cui all'articolo 56, paragrafo 6, del regolamento (UE) 2019/881, al gruppo di esperti selezionato in conformità del paragrafo 1 della presente sezione partecipa anche un esperto dell'autorità nazionale di certificazione della cibersicurezza correlata all'organismo di certificazione interessato.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica in caso di delega per il rilascio dei certificati o di previa approvazione degli stessi di cui all'articolo 56, paragrafo 6, del regolamento (UE) 2019/881.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato VI, sezione VI.2, punto 3",
        "testo": "Per una valutazione inter pares di tipo 2, i membri del gruppo sono selezionati tra gli organismi di certificazione autorizzati per il settore tecnico in questione.",
        "testo_integrale": "3. Per una valutazione inter pares di tipo 2, i membri del gruppo sono selezionati tra gli organismi di certificazione autorizzati per il settore tecnico in questione.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato VI, sezione VI.2, punto 4",
        "testo": "Ogni membro del gruppo di valutazione possiede almeno due anni di esperienza nello svolgimento di attività di certificazione presso un organismo di certificazione.",
        "testo_integrale": "4. Ogni membro del gruppo di valutazione possiede almeno due anni di esperienza nello svolgimento di attività di certificazione presso un organismo di certificazione.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato VI, sezione VI.2, punto 5",
        "testo": "Per una valutazione inter pares di tipo 2 o 3, ogni membro del gruppo di valutazione possiede almeno due anni di esperienza nello svolgimento di attività di certificazione nel settore tecnico o nel profilo di protezione pertinente e una comprovata esperienza e partecipazione nell'ambito dell'autorizzazione di un'ITSEF.",
        "testo_integrale": "5. Per una valutazione inter pares di tipo 2 o 3, ogni membro del gruppo di valutazione possiede almeno due anni di esperienza nello svolgimento di attività di certificazione nel settore tecnico o nel profilo di protezione pertinente e una comprovata esperienza e partecipazione nell'ambito dell'autorizzazione di un'ITSEF.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato VI, sezione VI.2, punto 6",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza che controlla l'organismo di certificazione oggetto di valutazione inter pares e vigila sullo stesso e almeno un'autorità nazionale di certificazione della cibersicurezza, il cui organismo di certificazione non è soggetto alla valutazione inter pares, partecipano alla valutazione inter pares in qualità di osservatori; anche l'ENISA può partecipare alla valutazione inter pares in qualità di osservatore.",
        "testo_integrale": "6. L'autorità nazionale di certificazione della cibersicurezza che controlla l'organismo di certificazione oggetto di valutazione inter pares e vigila sullo stesso e almeno un'autorità nazionale di certificazione della cibersicurezza, il cui organismo di certificazione non è soggetto alla valutazione inter pares, partecipano alla valutazione inter pares in qualità di osservatori. Anche l'ENISA può partecipare alla valutazione inter pares in qualità di osservatore.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato VI, sezione VI.2, punto 7",
        "testo": "La composizione del gruppo di valutazione inter pares è presentata all'organismo di certificazione oggetto di valutazione inter pares; in casi giustificati quest'ultimo può contestare la composizione di tale gruppo e chiederne la revisione.",
        "testo_integrale": "7. La composizione del gruppo di valutazione inter pares è presentata all'organismo di certificazione oggetto di valutazione inter pares. In casi giustificati, quest'ultimo può contestare la composizione di tale gruppo e chiederne la revisione.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "La facoltà dell'organismo di certificazione oggetto di valutazione inter pares di contestare la composizione del gruppo e chiederne la revisione si esercita nei casi giustificati previsti dal punto.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato VII",
        "testo": "Il certificato EUCC deve contenere almeno i seguenti elementi: l'identificatore unico stabilito dall'organismo di certificazione che rilascia il certificato (lettera a); le informazioni relative al prodotto TIC o al profilo di protezione certificato e al titolare del certificato (lettera b); le informazioni relative alla valutazione e alla certificazione del prodotto TIC o del profilo di protezione (lettera c); il marchio e l'etichetta associati al certificato in conformità dell'articolo 11 (lettera d).",
        "testo_integrale": "ALLEGATO VII\n\nContenuto del certificato EUCC\n\nIl certificato EUCC deve contenere almeno i seguenti elementi:",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato VII, lettera a)",
        "testo": "Il certificato EUCC contiene l'identificatore unico stabilito dall'organismo di certificazione che rilascia il certificato.",
        "testo_integrale": "(a) identificatore unico stabilito dall'organismo di certificazione che rilascia il certificato;",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato VII, lettera b)",
        "testo": "Il certificato EUCC contiene le informazioni relative al prodotto TIC o al profilo di protezione certificato e al titolare del certificato, tra cui il nome del prodotto TIC o del profilo di protezione e, se del caso, dell'oggetto della valutazione; il tipo del prodotto TIC o del profilo di protezione e, se del caso, dell'oggetto della valutazione; la versione del prodotto TIC o del profilo di protezione; il nome, l'indirizzo e le informazioni di contatto del titolare del certificato; il link al sito web del titolare contenente le informazioni supplementari sulla cibersicurezza di cui all'articolo 55 del regolamento (UE) 2019/881.",
        "testo_integrale": "(b) informazioni relative al prodotto TIC o al profilo di protezione certificato e al titolare del certificato, tra cui:\n\n(1) nome del prodotto TIC o del profilo di protezione e, se del caso, dell'oggetto della valutazione;\n\n(2) tipo del prodotto TIC o del profilo di protezione e, se del caso, dell'oggetto della valutazione;\n\n(3) versione del prodotto TIC o del profilo di protezione;\n\n(4) nome, indirizzo e informazioni di contatto del titolare del certificato;\n\n(5) link al sito web del titolare del certificato contenente le informazioni supplementari sulla cibersicurezza di cui all'articolo 55 del regolamento (UE) 2019/881;",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato VII, lettera c)",
        "testo": "Il certificato EUCC contiene le informazioni relative alla valutazione e alla certificazione del prodotto TIC o del profilo di protezione, tra cui il nome, l'indirizzo e le informazioni di contatto dell'organismo di certificazione che ha rilasciato il certificato; il nome dell'ITSEF che ha effettuato la valutazione, se differente dall'organismo di certificazione; il nome dell'autorità nazionale di certificazione della cibersicurezza responsabile; il riferimento al presente regolamento; il riferimento alla relazione di certificazione associata di cui all'allegato V; il livello di affidabilità applicabile in conformità dell'articolo 4; il riferimento alla versione delle norme utilizzate per la valutazione di cui all'articolo 3; l'identificazione del livello o del pacchetto di affidabilità specificato nelle norme di cui all'articolo 3 e in conformità dell'allegato VIII, compresi i componenti dell'affidabilità utilizzati e il livello AVA_VAN coperto; se del caso, il riferimento a uno o più profili di protezione che il prodotto TIC o il profilo di protezione rispettano; la data di rilascio; il periodo di validità del certificato.",
        "testo_integrale": "(c) informazioni relative alla valutazione e alla certificazione del prodotto TIC o del profilo di protezione, tra cui:\n\n(1) nome, indirizzo e informazioni di contatto dell'organismo di certificazione che ha rilasciato il certificato;\n\n(2) se differente dall'organismo di certificazione, nome dell'ITSEF che ha effettuato la valutazione;\n\n(3) nome dell'autorità nazionale di certificazione della cibersicurezza responsabile;\n\n(4) riferimento al presente regolamento;\n\n(5) riferimento alla relazione di certificazione associata al certificato di cui all'allegato V;\n\n(6) livello di affidabilità applicabile in conformità dell'articolo 4;\n\n(7) riferimento alla versione delle norme utilizzate per la valutazione di cui all'articolo 3;\n\n(8) identificazione del livello o del pacchetto di affidabilità specificato nelle norme di cui all'articolo 3 e in conformità dell'allegato VIII, compresi i componenti dell'affidabilità utilizzati e il livello AVA_VAN coperto;\n\n(9) se del caso, riferimento a uno o più profili di protezione che il prodotto TIC o il profilo di protezione rispettano;\n\n(10) data di rilascio;\n\n(11) periodo di validità del certificato;",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato VII, lettera d)",
        "testo": "Il certificato EUCC contiene il marchio e l'etichetta associati al certificato in conformità dell'articolo 11.",
        "testo_integrale": "(d) il marchio e l'etichetta associati al certificato in conformità dell'articolo 11.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato VIII, punto 1",
        "testo": "Contrariamente alle definizioni di cui ai criteri comuni, un incremento non è identificato con l'abbreviazione «+», è indicato in dettaglio con un elenco di tutti i componenti interessati ed è descritto dettagliatamente nella relazione di certificazione.",
        "testo_integrale": "ALLEGATO VIII\n\nDichiarazione del pacchetto di affidabilità\n\n1. Contrariamente alle definizioni di cui ai criteri comuni, un incremento:\n\n(a) non è identificato con l'abbreviazione «+»;\n\n(b) è indicato in dettaglio con un elenco di tutti i componenti interessati;\n\n(c) è descritto dettagliatamente nella relazione di certificazione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato VIII, punto 3",
        "testo": "Se il livello di affidabilità confermato in un certificato EUCC non si riferisce a un incremento, il certificato EUCC indica uno dei pacchetti seguenti: «il pacchetto di affidabilità specifico»; «il pacchetto di affidabilità conforme a un profilo di protezione», nel caso in cui si faccia riferimento a un profilo di protezione senza un livello di garanzia della valutazione.",
        "testo_integrale": "3. Se il livello di affidabilità confermato in un certificato EUCC non si riferisce a un incremento, il certificato EUCC indica uno dei pacchetti seguenti:\n\n(a) «il pacchetto di affidabilità specifico»;\n\n(b) «il pacchetto di affidabilità conforme a un profilo di protezione» nel caso in cui si faccia riferimento a un profilo di protezione senza un livello di garanzia della valutazione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando il livello di affidabilità confermato in un certificato EUCC non si riferisce a un incremento.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "allegato VI, sezione VI.1, punto 1",
        "testo": "Sono contemplati tre tipi di valutazione inter pares: il tipo 1, quando un organismo di certificazione effettua attività di certificazione al livello AVA_VAN.3; il tipo 2, quando effettua attività di certificazione relative a un settore tecnico elencato come documento sullo stato dell'arte nell'allegato I; il tipo 3, quando effettua attività di certificazione al di sopra del livello AVA_VAN.3 facendo uso di un profilo di protezione elencato come documento sullo stato dell'arte nell'allegato II o III.",
        "testo_integrale": "ALLEGATO VI\n\nAMBITO DELLA VALUTAZIONE INTER PARES E COMPOSIZIONE DEL GRUPPO DI VALUTAZIONE\n\nVI.1 Ambito della valutazione inter pares\n\n1. Sono contemplati i tipi di valutazione inter pares seguenti:\n\n(a) tipo 1: quando un organismo di certificazione effettua attività di certificazione al livello AVA_VAN.3;\n\n(b) tipo 2: quando un organismo di certificazione effettua attività di certificazione relative a un settore tecnico elencato come documento sullo stato dell'arte nell'allegato I;\n\n(c) tipo 3: quando un organismo di certificazione effettua attività di certificazione al di sopra del livello AVA_VAN.3 facendo uso di un profilo di protezione elencato come documento sullo stato dell'arte nell'allegato II o III.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato VIII, punto 2",
        "testo": "Il livello di affidabilità confermato in un certificato EUCC può essere integrato dal livello di garanzia della valutazione di cui all'articolo 3 del presente regolamento.",
        "testo_integrale": "2. Il livello di affidabilità confermato in un certificato EUCC può essere integrato dal livello di garanzia della valutazione di cui all'articolo 3 del presente regolamento.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "allegato VI, sezione VI.1, punto 1",
    "allegato VI, sezione VI.1, punto 1(a)",
    "allegato VI, sezione VI.1, punto 1(b)",
    "allegato VI, sezione VI.1, punto 1(c)",
    "allegato VI, sezione VI.1, punto 2",
    "allegato VI, sezione VI.1, punto 2(a)",
    "allegato VI, sezione VI.1, punto 2(b)",
    "allegato VI, sezione VI.1, punto 2(c)",
    "allegato VI, sezione VI.2, punto 1",
    "allegato VI, sezione VI.2, punto 2",
    "allegato VI, sezione VI.2, punto 3",
    "allegato VI, sezione VI.2, punto 4",
    "allegato VI, sezione VI.2, punto 5",
    "allegato VI, sezione VI.2, punto 6",
    "allegato VI, sezione VI.2, punto 7",
    "allegato VII",
    "allegato VII, lettera a)",
    "allegato VII, lettera b)",
    "allegato VII, lettera b), punto 1",
    "allegato VII, lettera b), punto 2",
    "allegato VII, lettera b), punto 3",
    "allegato VII, lettera b), punto 4",
    "allegato VII, lettera b), punto 5",
    "allegato VII, lettera c)",
    "allegato VII, lettera c), punto 1",
    "allegato VII, lettera c), punto 2",
    "allegato VII, lettera c), punto 3",
    "allegato VII, lettera c), punto 4",
    "allegato VII, lettera c), punto 5",
    "allegato VII, lettera c), punto 6",
    "allegato VII, lettera c), punto 7",
    "allegato VII, lettera c), punto 8",
    "allegato VII, lettera c), punto 9",
    "allegato VII, lettera c), punto 10",
    "allegato VII, lettera c), punto 11",
    "allegato VII, lettera d)",
    "allegato VIII, punto 1",
    "allegato VIII, punto 1(a)",
    "allegato VIII, punto 1(b)",
    "allegato VIII, punto 1(c)",
    "allegato VIII, punto 2",
    "allegato VIII, punto 3",
    "allegato VIII, punto 3(a)",
    "allegato VIII, punto 3(b)",
]

MAPPATURA_LOCALE = {
    "allegato VI, sezione VI.1, punto 1": [
        "allegato VI, sezione VI.1, punto 1",
        "allegato VI, sezione VI.1, punto 1(a)",
        "allegato VI, sezione VI.1, punto 1(b)",
        "allegato VI, sezione VI.1, punto 1(c)",
    ],
    "allegato VI, sezione VI.1, punto 2": [
        "allegato VI, sezione VI.1, punto 2",
        "allegato VI, sezione VI.1, punto 2(a)",
        "allegato VI, sezione VI.1, punto 2(b)",
        "allegato VI, sezione VI.1, punto 2(c)",
    ],
    "allegato VI, sezione VI.2, punto 1": ["allegato VI, sezione VI.2, punto 1"],
    "allegato VI, sezione VI.2, punto 2": ["allegato VI, sezione VI.2, punto 2"],
    "allegato VI, sezione VI.2, punto 3": ["allegato VI, sezione VI.2, punto 3"],
    "allegato VI, sezione VI.2, punto 4": ["allegato VI, sezione VI.2, punto 4"],
    "allegato VI, sezione VI.2, punto 5": ["allegato VI, sezione VI.2, punto 5"],
    "allegato VI, sezione VI.2, punto 6": ["allegato VI, sezione VI.2, punto 6"],
    "allegato VI, sezione VI.2, punto 7": ["allegato VI, sezione VI.2, punto 7"],
    "allegato VII": ["allegato VII"],
    "allegato VII, lettera a)": ["allegato VII, lettera a)"],
    "allegato VII, lettera b)": [
        "allegato VII, lettera b)",
        "allegato VII, lettera b), punto 1",
        "allegato VII, lettera b), punto 2",
        "allegato VII, lettera b), punto 3",
        "allegato VII, lettera b), punto 4",
        "allegato VII, lettera b), punto 5",
    ],
    "allegato VII, lettera c)": [
        "allegato VII, lettera c)",
        "allegato VII, lettera c), punto 1",
        "allegato VII, lettera c), punto 2",
        "allegato VII, lettera c), punto 3",
        "allegato VII, lettera c), punto 4",
        "allegato VII, lettera c), punto 5",
        "allegato VII, lettera c), punto 6",
        "allegato VII, lettera c), punto 7",
        "allegato VII, lettera c), punto 8",
        "allegato VII, lettera c), punto 9",
        "allegato VII, lettera c), punto 10",
        "allegato VII, lettera c), punto 11",
    ],
    "allegato VII, lettera d)": ["allegato VII, lettera d)"],
    "allegato VIII, punto 1": [
        "allegato VIII, punto 1",
        "allegato VIII, punto 1(a)",
        "allegato VIII, punto 1(b)",
        "allegato VIII, punto 1(c)",
    ],
    "allegato VIII, punto 2": ["allegato VIII, punto 2"],
    "allegato VIII, punto 3": [
        "allegato VIII, punto 3",
        "allegato VIII, punto 3(a)",
        "allegato VIII, punto 3(b)",
    ],
}

# Relazioni interne a questo modulo (fonte_id_o_None = None su entrambi gli
# estremi). Una sola e' "textual" perche' cita letteralmente la riga di
# destinazione; le altre undici sono "inferred" (legame dedotto dal contenuto,
# non citato). `confidence` None su tutte: nessuno score reale da riportare
# (ADR-0005, non va inventato). Nessuna relazione verso altri capitoli di questa
# Fonte (allegato V, allegato I, allegato II/III, artt. 3, 4, 11) ne' verso
# altre Fonti (regolamento (UE) 2019/881, criteri comuni ISO/IEC 15408): le
# costruisce la sessione principale in fase 6, elencate nel docstring.
RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "allegato VI, sezione VI.1, punto 2"),
        "nodo_a": ("principio", None, "allegato VI, sezione VI.1, punto 1"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VI, sezione VI.2, punto 2"),
        "nodo_a": ("obbligo", None, "allegato VI, sezione VI.2, punto 1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VI, sezione VI.2, punto 3"),
        "nodo_a": ("principio", None, "allegato VI, sezione VI.1, punto 1"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VI, sezione VI.2, punto 5"),
        "nodo_a": ("principio", None, "allegato VI, sezione VI.1, punto 1"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VI, sezione VI.2, punto 7"),
        "nodo_a": ("obbligo", None, "allegato VI, sezione VI.2, punto 1"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VII, lettera a)"),
        "nodo_a": ("obbligo", None, "allegato VII"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VII, lettera b)"),
        "nodo_a": ("obbligo", None, "allegato VII"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VII, lettera c)"),
        "nodo_a": ("obbligo", None, "allegato VII"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VII, lettera d)"),
        "nodo_a": ("obbligo", None, "allegato VII"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    # La lettera c) punto 8 cita "in conformita' dell'allegato VIII": la
    # citazione e' all'allegato intero, che in questo modulo non ha un nodo
    # proprio (l'allegato VIII non ha chapeau), quindi l'arco e' verso i due
    # punti che disciplinano il contenuto richiamato (incrementi e pacchetti di
    # affidabilita') ed e' "inferred", non "textual".
    {
        "nodo_da": ("obbligo", None, "allegato VII, lettera c)"),
        "nodo_a": ("obbligo", None, "allegato VIII, punto 1"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VII, lettera c)"),
        "nodo_a": ("obbligo", None, "allegato VIII, punto 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato VIII, punto 3"),
        "nodo_a": ("obbligo", None, "allegato VIII, punto 1"),
        "tipo_relazione": "richiama",
        "evidence_type": "inferred",
        "confidence": None,
    },
]
