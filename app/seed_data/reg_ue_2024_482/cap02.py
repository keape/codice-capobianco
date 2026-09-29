"""Regolamento di esecuzione (UE) 2024/482 della Commissione, del 31 gennaio
2024 - sistema europeo di certificazione della cibersicurezza basato sui
criteri comuni (EUCC). Fonte 29 (`reg_ue_2024_482`), capitolo 2 di 14 (elenco
completo in app/.source_cache/reg_ue_2024_482/manifest.json): Capo II -
Certificazione dei prodotti TIC, sezioni I ("Norme e requisiti specifici per la
valutazione") e II ("Rilascio, rinnovo e revoca dei certificati EUCC"),
articoli 7-14. Gli artt. 1-6 sono nel cap01, 15-20 nel cap03, 21-24 nel cap04,
25-31 nel cap05, 32-39 nel cap06, 40-43 nel cap07, 44-50 nel cap08 e gli
allegati I-IX nei cap09-cap14: nessuno di quei file e' toccato qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_482/cap02.txt, estratto
dal raw.txt acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R0482, lingua italiana; URL
risolto .../cellar/687c0d05-c580-11ee-95d9-01aa75ed71a1.0014.03/DOC_1, XHTML
della Gazzetta ufficiale; fetch 2026-09-29T10:29:08Z, 135.367 caratteri di
testo, sha256 del raw.txt
b46d08cab6d63b2c190ae767042c07c1fc324955c22ef491eb314556b28ca5b8 - dettagli
completi in app/.source_cache/reg_ue_2024_482/provenance.json). Il preambolo
(considerando) e' a monte del Capo I e non e' in questa porzione.

Paratesto escluso (nessun nodo, nessun item di indice):
- le intestazioni strutturali "CAPO II" / "CERTIFICAZIONE DEI PRODOTTI TIC",
  "SEZIONE I" / "Norme e requisiti specifici per la valutazione", "SEZIONE II" /
  "Rilascio, rinnovo e revoca dei certificati EUCC": sono la partizione
  dell'atto, non disposizioni; non hanno precetto proprio e non sono
  indicizzabili (le sezioni non hanno articoli propri che le coprano);
- le intestazioni "Articolo N" + rubrica dei singoli articoli non producono
  righe proprie ne' item propri: restano nel `testo_integrale` della prima riga
  di ciascun articolo, dove il testo ufficiale le premette immediatamente al
  primo comma (stessa convenzione del cap01 di questa Fonte e dell'art. 3 del
  Reg. 2025/2532);
- in questa porzione non compaiono epigrafe, firma, nota a pie' di pagina,
  formula di chiusura ne' riga ELI (sono tutte nel cap08), quindi non c'e'
  nulla da escludere a quel titolo. Nessun nodo valorizza `severita` o
  `sanzioni`: il regolamento non gradua i requisiti ne' stabilisce sanzioni
  proprie (le sanzioni del sistema EUCC discendono dal regolamento (UE)
  2019/881 e dal diritto nazionale).

Unita' di copertura e scelta della grana. Regola applicata: un comma = una
riga; quando il comma si apre con un chapeau che porta il predicato e le
lettere ne sono il contenuto (elementi, condizioni, informazioni, impegni,
contenuti del marchio, esiti possibili del riesame), la riga resta una sola e
ogni lettera riceve un item di indice proprio, tutti mappati su quella riga
(come l'art. 5 §1 del Reg. 2024/2979, esempio di stile di questo batch). Non ho
percio' spezzato per lettera nessuno degli articoli 7-14: in tutti i casi il
precetto sta nel chapeau e la lettera lo specifica. Le quattro alternative di
art. 13 §2 sono poi per costruzione mutuamente esclusive (esiti possibili di
una decisione unica), non precetti cumulativi; le sei lettere di art. 9 §2 sono
altrettanto legate fra loro dal testo, che le richiama in blocco come "tutti
gli impegni di cui al paragrafo 2" in art. 9 §1(b). I punti (1)-(4) di art. 11
§3(b) non ricevono item proprio: sono le componenti dell'identificatore unico
del certificato, non unita' autonome (restano integrali nel `testo_integrale`
della riga).

Criterio Obbligo/Principio. Obbligo = comma che impone un comportamento a un
soggetto identificabile (anche in forma passiva: "è valutato", "sono
apposti", "è conservata") o che disciplina in modo vincolante un atto del
procedimento; Principio "altro" = comma il cui contenuto operativo e' una mera
facolta' o un potere discrezionale, senza comportamento imposto ne' obbligo
correlativo di terzi. Applicato comma per comma:
- art. 8 §3 (i richiedenti *possono* fornire risultati di precedenti
  certificazioni), art. 8 §4 (l'ITSEF *può* riutilizzarli, con le condizioni di
  conformita' e autenticita'), art. 11 §1 (il titolare *può* apporre marchio ed
  etichetta: la facolta' e l'effetto dichiarato del marchio; il rinvio di
  conformita' a questo articolo e all'allegato IX e' la condizione modale della
  facolta', il cui contenuto prescrittivo sta nei §2-§4), art. 13 §3 (potere di
  sospendere il certificato in conformita' dell'art. 30), art. 14 §3 (diritto
  del titolare di richiedere la revoca) -> Principi. Stessa lettura gia' usata
  nel censimento per le disposizioni permissive (Reg. 2025/2532 art. 1 §2, CAD
  art. 3-bis c.1-bis, SPID art. 5 c.2, DPCM art. 13 c.2).
- art. 12 §3 (facolta' di superare i cinque anni *previa approvazione*
  dell'autorita' nazionale, che *notifica* senza indebito ritardo al gruppo
  europeo) e' invece Obbligo "procedurale": oltre alla facolta' il comma
  impone l'atto di approvazione e la notifica, esattamente come SPID art. 8 c.2
  ("l'utente può chiedere ... e il gestore provvede tempestivamente") e' stato
  censito come Obbligo procedurale e non come Principio.
- art. 13 §1 (l'organismo *può decidere* di riesaminare, ma "il riesame è
  effettuato conformemente all'allegato IV", l'organismo *determina* la
  portata, *chiede* all'ITSEF la nuova valutazione) e' Obbligo "procedurale":
  il comma non si esaurisce nel potere, prescrive come il riesame si svolge.
- tutti gli altri commi di artt. 7-14 impongono un comportamento e sono
  Obblighi (dettaglio riga per riga sotto).

Riga per riga (Obblighi in ordine di documento):
- art. 7 §1 -> Obbligo "tecnico/sicurezza": enuncia i criteri e i metodi con
  cui il prodotto TIC presentato ai fini della certificazione e' valutato
  almeno (norme dell'art. 3, classi di garanzia, livello di rischio e funzioni
  di sicurezza degli artt. 51-52 del Reg. 2019/881, documenti sullo stato
  dell'arte dell'allegato I, profili di protezione certificati dell'allegato
  II). Le lettere (a)-(e) sono elementi nominali del medesimo predicato "è
  valutato conformemente a": una riga, sei item.
- art. 7 §2 -> Obbligo "procedurale": procedura di eccezione ai documenti
  sullo stato dell'arte (richiesta motivata dell'organismo di valutazione della
  conformita', valutazione e approvazione dell'autorita' nazionale, divieto di
  rilasciare certificati in pendenza, notifica senza indebito ritardo al gruppo
  europeo, parere di quest'ultimo tenuto nella massima considerazione).
- art. 7 §3 -> Obbligo "tecnico/sicurezza": i tre soli scenari in cui e'
  possibile certificare al livello AVA_VAN 4 o 5 e la metodologia di
  valutazione da applicare in ciascuno (lettere (a)-(c) sono scenari alternativi
  del medesimo precetto, non precetti autonomi: una riga, quattro item).
- art. 7 §4 -> Obbligo "procedurale": notifica della certificazione prevista
  all'autorita' nazionale con giustificazione e proposta di metodologia;
  l'autorita' approva o modifica la metodologia, l'organismo non rilascia
  certificati in pendenza, l'autorita' segnala la certificazione prevista al
  gruppo europeo.
- art. 7 §5 -> Obbligo "procedurale": l'ITSEF che ha valutato il prodotto TIC
  sottostante condivide le informazioni pertinenti con l'ITSEF che valuta il
  prodotto composito. Condivisione fra organismi dentro il procedimento di
  certificazione: "procedurale" e non "informativo/trasparenza", che nel
  censimento copre le informazioni verso utenti, mercato e pubblico.
- art. 8 §1 -> Obbligo "procedurale": il richiedente fornisce o mette a
  disposizione dell'organismo di certificazione e dell'ITSEF tutte le
  informazioni necessarie per la certificazione. La documentazione di domanda
  fornita agli organismi e' un adempimento del procedimento, come le notifiche
  alle autorita' gia' censite (Reg. 2025/1569 art. 5 §1, eIDAS art. 24 §2(a)).
- art. 8 §2 -> Obbligo "procedurale": contenuto e formato degli elementi di
  prova (sezioni «Azioni dello sviluppatore» e «Contenuto e presentazione
  dell'elemento di prova» dei criteri comuni e della metodologia comune di
  valutazione), compresi i dettagli sul prodotto TIC e sul codice sorgente,
  fatte salve le salvaguardie contro la divulgazione non autorizzata.
- art. 8 §5 -> Obbligo "procedurale" (condizionato: solo se l'organismo di
  certificazione consente la certificazione di prodotto composito): il
  richiedente mette a disposizione tutti gli elementi necessari in conformita'
  del documento sullo stato dell'arte.
- art. 8 §6 -> Obbligo "procedurale": ulteriori informazioni da fornire
  all'organismo e all'ITSEF (link al sito web con le informazioni
  supplementari sulla cibersicurezza dell'art. 55 del Reg. 2019/881;
  descrizione delle procedure di gestione e divulgazione delle vulnerabilita').
  La classificazione "procedurale" segue il destinatario (gli organismi della
  certificazione), non il contenuto informativo dei due elementi.
- art. 8 §7 -> Obbligo "di conservazione": la documentazione dell'articolo e'
  conservata da organismo di certificazione, ITSEF e richiedente per cinque
  anni dopo la scadenza del certificato. Unico comma dell'atto con un termine
  di conservazione: tipo "di conservazione", come gli obblighi di archiviazione
  gia' censiti.
- art. 9 §1 -> Obbligo "procedurale": le cinque condizioni cumulative per il
  rilascio del certificato EUCC (ambito di accreditamento, dichiarazione di
  impegni del richiedente, valutazione ITSEF senza obiezioni, riesame
  dell'organismo senza obiezioni, verifica di coerenza delle relazioni
  tecniche). Soggetto obbligato: l'organismo di certificazione che rilascia.
- art. 9 §2 -> Obbligo "informativo/trasparenza": i sei impegni che il
  richiedente assume con la dichiarazione richiamata da art. 9 §1(b) -
  informazioni necessarie, complete e corrette; nessuna promozione come
  certificato prima del rilascio; promozione solo nell'ambito di applicazione
  del certificato; cessazione immediata della promozione in caso di
  sospensione, revoca o scadenza; identita' dei prodotti venduti con il
  certificato; rispetto delle norme di utilizzo del marchio e dell'etichetta.
  Il baricentro del comma e' la comunicazione corretta sullo stato di
  certificazione (informazioni e promozione), non un adempimento interno.
- art. 9 §3 -> Obbligo "procedurale": l'organismo che ha certificato il
  prodotto sottostante condivide le informazioni pertinenti con l'organismo che
  certifica il prodotto composito (gemello di art. 7 §5).
- art. 10 §1 -> Obbligo "informativo/trasparenza": il certificato EUCC contiene
  almeno le informazioni dell'allegato VII. I §1-§2 dell'art. 10 sono requisiti
  sul contenuto del certificato e della relazione di certificazione, cioe'
  sull'informazione resa al mercato e al titolare: "informativo/trasparenza".
- art. 10 §2 -> Obbligo "informativo/trasparenza": ambito e limiti del prodotto
  certificato specificati in modo inequivocabile nel certificato o nella
  relazione di certificazione, con indicazione se la certificazione riguarda
  l'intero prodotto o solo alcune parti.
- art. 10 §3 -> Obbligo "procedurale": l'organismo fornisce al richiedente il
  certificato almeno in formato elettronico.
- art. 10 §4 -> Obbligo "procedurale": l'organismo elabora una relazione di
  certificazione conforme all'allegato V per ciascun certificato, sulla base
  della relazione tecnica di valutazione dell'ITSEF; entrambe le relazioni
  indicano i criteri e i metodi di valutazione specifici dell'art. 7 usati.
- art. 10 §5 -> Obbligo "procedurale": trasmissione in formato elettronico di
  tutti i certificati e di tutte le relazioni di certificazione all'autorita'
  nazionale di certificazione della cibersicurezza e all'ENISA.
- art. 11 §2 -> Obbligo "informativo/trasparenza": modalita' di apposizione del
  marchio e dell'etichetta (visibile, leggibile e indelebile sul prodotto o
  sulla targhetta identificativa; su imballaggio o documenti di accompagnamento
  se l'apposizione sul prodotto e' impossibile o difficilmente realizzabile;
  per il software sui documenti di accompagnamento o su documenti resi
  facilmente e direttamente accessibili agli utenti via sito web).
- art. 11 §3 -> Obbligo "informativo/trasparenza": conformita' del marchio e
  dell'etichetta all'allegato IX e contenuto minimo (livello di affidabilita' e
  livello AVA_VAN; identificatore unico del certificato con denominazione del
  sistema, denominazione e numero di riferimento dell'accreditamento,
  anno e mese di rilascio, numero di identificazione).
- art. 11 §4 -> Obbligo "informativo/trasparenza": codice QR con link a un sito
  web contenente almeno informazioni su validita' del certificato,
  informazioni di certificazione degli allegati V e VII, informazioni che il
  titolare deve rendere pubbliche ai sensi dell'art. 55 del Reg. 2019/881 e,
  se del caso, informazioni storiche per la tracciabilita'.
- art. 12 §1 -> Obbligo "procedurale": l'organismo stabilisce un periodo di
  validita' per ciascun certificato rilasciato, tenendo conto delle
  caratteristiche del prodotto certificato.
- art. 12 §2 -> Obbligo "procedurale": limite dei cinque anni al periodo di
  validita'.
- art. 12 §3 -> Obbligo "procedurale": deroga al limite dei cinque anni previa
  approvazione dell'autorita' nazionale di certificazione della
  cibersicurezza, con notifica dell'approvazione al gruppo europeo senza
  indebito ritardo.
- art. 13 §1 -> Obbligo "procedurale": riesame del certificato su richiesta del
  titolare o per altri motivi giustificati, effettuato secondo l'allegato IV,
  con portata determinata dall'organismo e, se necessario, nuova valutazione
  richiesta all'ITSEF.
- art. 13 §2 -> Obbligo "procedurale": gli esiti possibili del riesame
  (conferma; revoca conforme all'art. 14; revoca e nuovo certificato con
  identico ambito e validita' prorogata; revoca e nuovo certificato con ambito
  diverso).
- art. 14 §1 -> Obbligo "procedurale": il certificato EUCC e' revocato
  dall'organismo di certificazione che lo ha rilasciato, fatto salvo l'art. 58
  §8(e) del Reg. 2019/881.
- art. 14 §2 -> Obbligo "procedurale": notifica della revoca all'autorita'
  nazionale di certificazione della cibersicurezza, trasmissione all'ENISA per
  i compiti dell'art. 50 del Reg. 2019/881, informazione delle altre autorita'
  di vigilanza del mercato competenti.

Principi (ordine di documento):
- art. 8 §3 (facolta' dei richiedenti di fornire risultati di precedenti
  certificazioni; le lettere (a)-(c) indicano i tre regimi di provenienza),
  art. 8 §4 (facolta' dell'ITSEF di riutilizzare i risultati pertinenti,
  conformi e con autenticita' confermata), art. 11 §1 (facolta' del titolare di
  apporre marchio ed etichetta e effetto dichiarato: il marchio dimostra la
  certificazione), art. 13 §3 (potere di sospendere il certificato in attesa di
  misura correttiva), art. 14 §3 (diritto del titolare di richiedere la revoca).
  Sono tutti Principi "altro": nessuno rientra fra non discriminazione,
  equivalenza giuridica, valore probatorio, presunzione legale, scopo/ambito di
  applicazione o definitorio; `oggetti_giuridici` = ["altro"], perche' l'atto
  non disciplina firme, sigilli, marcature temporali, documenti elettronici,
  recapito certificato, identificazione elettronica o gli altri oggetti
  censiti, ma la certificazione di prodotti TIC (oggetto non presente
  nell'insieme).

Soggetti. Nessuna delle categorie censite descrive gli attori di questo Capo
(richiedente la certificazione, organismo di certificazione, ITSEF, autorita'
nazionale di certificazione della cibersicurezza, ENISA, gruppo europeo per la
certificazione della cibersicurezza): sono soggetti con ruolo identificabile e
tracciabile ma non prestatori di servizi fiduciari, non utenti e non terzi
affidanti. Ho quindi usato "Terza parte" per tutti gli obbligati di soggetto
istituzionale o industriale, come gia' fatto per gli Stati membri e la
Commissione in Reg. 2025/1569 art. 5 e per l'organismo di convalida in
regolamento tecnico AgID cap03. In particolare il "richiedente la
certificazione" (artt. 8, 9 §2) non e' un QTSP per definizione del testo: e' il
soggetto che domanda la certificazione di un prodotto TIC, e la categoria
"Terza parte" e' l'unica disponibile che lo rappresenti (l'alternativa
"QTSP/gestore" presupporrebbe che il richiedente sia sempre un prestatore
qualificato, cosa che il regolamento non presuppone). Il destinatario
"Terza parte" e' valorizzato dove il testo nomina il destinatario dell'atto
(organismo di certificazione, ITSEF, autorita' nazionale, ENISA, altro
organismo); "Utente/titolare" solo in art. 11 §2, dove il testo nomina "gli
utenti". Non ho inferito destinatari non nominati.

`condizione_applicabilita` (testo libero, fatti esterni non tracciati come
nodi): art. 7 §2, art. 7 §3, art. 7 §5, art. 8 §3, art. 8 §4, art. 8 §5,
art. 9 §3, art. 12 §3, art. 13 §1, art. 13 §3, art. 14 §1 (riserva dell'art. 58
§8(e) del Reg. 2019/881). Non l'ho usata dove la condizione e' un nodo di questo stesso
modulo: in quei casi la condizionalita' e' dichiarata come relazione
("è condizionato da" per art. 11 §2-§4 verso art. 11 §1, richiama per art. 7 §4
verso art. 7 §3).

`testo_integrale`: verbatim e integrale di ogni comma, ricucendo le righe
spezzate dalla conversione XHTML -> testo (i marcatori di lettera "(a)", "(b)"
... e i punti "(1)"-"(4)" di art. 11 §3(b), isolati su riga propria nel testo
ufficiale, sono riuniti al testo che segue; i commi restano separati da riga
vuota; l'intestazione "Articolo N" + rubrica e' premessa al primo comma di
ciascun articolo, mai ripetuta nei commi successivi). Nessun marcatore di
elisione (guardia `verifica_completezza_testo_integrale`, ADR-0010); simboli
ufficiali (« », gli apici dritti del testo CELLAR, "AVA_VAN 4 o 5") conservati
come pubblicati, senza correggere gli errori del testo ufficiale (es. "sono
conformi al quanto disposto nell'allegato IX" in art. 11 §3 resta "al quanto").
`testo` e' la sintesi in 1-3 frasi di ciascun comma, che nomina tutte le
prescrizioni autonome contenute nelle lettere accorpate.

Rinvii demandati alla fase 6 (nessuna relazione dichiarata verso di essi: sono
altri capitoli di questa stessa Fonte o altre Fonti):
- allegati di questa Fonte: allegato I e allegato II (art. 7 §1(d), §1(e),
  §3(a), §3(b)) -> cap09; allegato VII (art. 10 §1) -> cap13; allegato V
  (art. 10 §4, art. 11 §4(b)) -> cap12; allegato IX (art. 11 §1, art. 11 §3)
  -> cap14; allegato IV (art. 13 §1) -> cap11;
- articoli di questa Fonte in altri capitoli: art. 3 (art. 7 §1(a) e §1(b),
  art. 9 §1(c)) -> cap01; art. 30 (art. 13 §3) -> cap05; art. 49 (art. 8
  §3(c)) -> cap08; art. 58 e art. 50 del regolamento (UE) 2019/881 (art. 14 §1
  e §2), artt. 51-52 e art. 55 del medesimo regolamento (art. 7 §1(c),
  art. 8 §6(a), art. 11 §4(c)) e art. 49 del medesimo regolamento (art. 8
  §3(b)) -> altra Fonte;
- il richiamo dell'art. 2 del presente regolamento all'atto di esecuzione non
  compare in questa porzione.

Relazioni dichiarate (solo fra righe di questo modulo, `fonte_id_o_None=None`
su entrambi gli estremi): tredici. Dieci sono rinvii letterali verificati sul
`testo_integrale` della riga citante, quindi `evidence_type="textual"`:
art. 7 §3 -> art. 7 §4 ("alle condizioni di cui al paragrafo 4") e
art. 7 §4 -> art. 7 §3 ("di cui al paragrafo 3, lettera c)") sono i due versi
dello stesso rinvio, ciascuno citato nel proprio comma; art. 9 §1 -> art. 9 §2
("gli impegni di cui al paragrafo 2"); art. 9 §1 -> art. 7 §1, art. 10 §4 ->
art. 7 §1 e art. 9 §2 -> art. 11 §1 e art. 11 §2 sono rinvii ad articolo intero
("di cui agli articoli 3 e 7", "di cui all'articolo 7", "in conformità
dell'articolo 11"): il bersaglio e' il comma che regge la materia citata
(art. 7 §1, che elenca i criteri e i metodi di valutazione; art. 11 §1 che
istituisce il marchio e ne rinvia la disciplina a questo articolo e all'allegato
IX, art. 11 §2 che ne stabilisce l'apposizione), mentre gli altri commi dell'art.
7 (procedura di eccezione, scenari AVA_VAN, condivisione fra ITSEF) e dell'art.
11 (contenuto del marchio, codice QR) non contengono la materia citata; per la
stessa ragione i due rinvii all'art. 7 sono diretti al solo §1. Avvertenza per
l'audit `verifica_relazioni_textual.py`: le due relazioni verso art. 7 §1 (da
art. 9 §1 e da art. 10 §4) cadono nella sua sezione A, perche' lo strumento
cerca nel testo citante una traccia del riferimento citato e per un articolo a
una cifra la traccia e' solo "paragrafo 1"/"§ 1", che il testo ufficiale non
contiene (cita l'articolo in blocco); i rinvii ad articolo intero verso
art. 11 §1/§2 e art. 14 §1 superano invece il gate, perche' quei numeri di
articolo hanno due cifre ("11", "14") e compaiono nel testo citante. Le due
segnalazioni restano `textual`: la citazione all'articolo e' letterale, e' solo
la grana del bersaglio a essere piu' fine di quella della citazione.
Per art. 13 §2 -> art. 14 §1 ("in conformità dell'articolo 14", tre volte nelle
lettere (b), (c) e (d), tutte accorpate nella riga "art. 13 §2") e per
art. 14 §2 -> art. 14 §1 ("di cui al paragrafo 1") vale la stessa regola di
miratura: il §1 e' la norma che dispone la revoca, il §2 ne disciplina la
notifica e il §3 il diritto del titolare. Art. 12 §3 -> art. 12 §2 e'
`deroga a` letterale ("In deroga al paragrafo 2"). Tre relazioni sono
`è condizionato da` con `evidence_type="inferred"`: art. 11 §2, §3 e §4 si
applicano solo se il titolare appone il marchio e l'etichetta, facolta'
tracciata in art. 11 §1 - la dipendenza e' dedotta dal contenuto, non citata,
quindi non e' `textual`. `confidence` = None per tutte: non esiste uno score
reale da riportare (ADR-0005).

Copertura: 67 item di indice, 33 righe (28 Obblighi + 5 Principi), 13
relazioni interne.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 7 §1",
        "testo": "Un prodotto TIC presentato ai fini della certificazione è valutato almeno conformemente a: gli elementi applicabili delle norme di cui all'articolo 3; le classi dei requisiti di garanzia della sicurezza per la valutazione della vulnerabilità e le prove funzionali indipendenti stabilite nelle norme di valutazione di cui all'articolo 3; il livello di rischio associato all'uso previsto dei prodotti TIC a norma dell'articolo 52 del regolamento (UE) 2019/881 e le loro funzioni di sicurezza a sostegno degli obiettivi di sicurezza di cui all'articolo 51 del medesimo regolamento; i documenti sullo stato dell'arte applicabili di cui all'allegato I; i profili di protezione certificati applicabili di cui all'allegato II.",
        "testo_integrale": "Articolo 7\n\nCriteri e metodi di valutazione dei prodotti TIC\n\n1. Un prodotto TIC presentato ai fini della certificazione è valutato almeno conformemente a quanto segue:\n\n(a) gli elementi applicabili delle norme di cui all'articolo 3;\n\n(b) le classi dei requisiti di garanzia della sicurezza per la valutazione della vulnerabilità e le prove funzionali indipendenti, come stabilito nelle norme di valutazione di cui all'articolo 3;\n\n(c) il livello di rischio associato all'uso previsto dei prodotti TIC in questione a norma dell'articolo 52 del regolamento (UE) 2019/881 e le loro funzioni di sicurezza a sostegno degli obiettivi di sicurezza di cui all'articolo 51 del medesimo regolamento;\n\n(d) i documenti sullo stato dell'arte applicabili di cui all'allegato I; e\n\n(e) i profili di protezione certificati applicabili di cui all'allegato II.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 §2",
        "testo": "In casi eccezionali e debitamente giustificati un organismo di valutazione della conformità può chiedere di non applicare il pertinente documento sullo stato dell'arte: in tal caso informa l'autorità nazionale di certificazione della cibersicurezza fornendo una giustificazione debitamente motivata; l'autorità valuta se l'eccezione sia giustificata e, in caso affermativo, la approva; in attesa della decisione l'organismo non rilascia alcun certificato; l'autorità notifica senza indebito ritardo l'eccezione approvata al gruppo europeo per la certificazione della cibersicurezza, che può formulare un parere, e ne tiene nella massima considerazione il parere.",
        "testo_integrale": "2. In casi eccezionali e debitamente giustificati, un organismo di valutazione della conformità può chiedere di non applicare il pertinente documento sullo stato dell'arte. In tali casi l'organismo di valutazione della conformità informa l'autorità nazionale di certificazione della cibersicurezza fornendo una giustificazione debitamente motivata della propria richiesta. L'autorità nazionale di certificazione della cibersicurezza valuta se l'eccezione sia giustificata e, in caso affermativo, la approva. In attesa della decisione dell'autorità nazionale di certificazione della cibersicurezza, l'organismo di valutazione della conformità non rilascia alcun certificato. L'autorità nazionale di certificazione della cibersicurezza notifica senza indebito ritardo l'eccezione approvata al gruppo europeo per la certificazione della cibersicurezza, che può formulare un parere. L'autorità nazionale di certificazione della cibersicurezza tiene nella massima considerazione il parere del gruppo europeo per la certificazione della cibersicurezza.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica ai casi eccezionali e debitamente giustificati in cui l'organismo di valutazione della conformità chiede di non applicare il pertinente documento sullo stato dell'arte.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 7 §3",
        "testo": "La certificazione dei prodotti TIC al livello AVA_VAN 4 o 5 è possibile solo in tre scenari: se il prodotto rientra in uno dei settori tecnici di cui all'allegato I è valutato conformemente ai documenti sullo stato dell'arte applicabili di tali settori tecnici; se rientra in una categoria di prodotti TIC contemplati da un profilo di protezione certificato che comprende il livello AVA_VAN 4 o 5 e figura nell'allegato II come profilo di protezione avanzato è valutato conformemente alla metodologia di valutazione specificata per tale profilo; se le lettere a) e b) non sono applicabili e l'inclusione di un settore tecnico nell'allegato I o di un profilo di protezione certificato nell'allegato II è improbabile nel prossimo futuro, solo in casi eccezionali e debitamente giustificati e alle condizioni di cui al paragrafo 4.",
        "testo_integrale": "3. La certificazione dei prodotti TIC al livello AVA_VAN 4 o 5 è possibile solo negli scenari seguenti:\n\n(a) se rientra in uno dei settori tecnici di cui all'allegato I, il prodotto TIC è valutato conformemente ai documenti sullo stato dell'arte applicabili di tali settori tecnici;\n\n(b) se rientra in una categoria di prodotti TIC contemplati da un profilo di protezione certificato che comprende il livello AVA_VAN 4 o 5 e che figura nell'allegato II come profilo di protezione avanzato, il prodotto TIC è valutato conformemente alla metodologia di valutazione specificata per tale profilo di protezione;\n\n(c) se le lettere a) e b) del presente paragrafo non sono applicabili e se l'inclusione di un settore tecnico nell'allegato I o di un profilo di protezione certificato nell'allegato II è improbabile nel prossimo futuro, e solo in casi eccezionali e debitamente giustificati, alle condizioni di cui al paragrafo 4.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo alla certificazione dei prodotti TIC al livello AVA_VAN 4 o 5.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 §4",
        "testo": "Qualora ritenga di trovarsi di fronte a un caso eccezionale e debitamente giustificato di cui al paragrafo 3, lettera c), l'organismo di valutazione della conformità notifica la certificazione prevista all'autorità nazionale di certificazione della cibersicurezza fornendo una giustificazione e una proposta di metodologia di valutazione; l'autorità valuta se l'eccezione sia giustificata e, in caso affermativo, approva o modifica la metodologia che l'organismo dovrà applicare; in attesa della decisione l'organismo non rilascia alcun certificato; l'autorità segnala senza indebito ritardo la certificazione prevista al gruppo europeo per la certificazione della cibersicurezza, che può formulare un parere, e ne tiene nella massima considerazione il parere.",
        "testo_integrale": "4. Qualora ritenga di trovarsi di fronte a un caso eccezionale e debitamente giustificato di cui al paragrafo 3, lettera c), l'organismo di valutazione della conformità notifica la certificazione prevista all'autorità nazionale di certificazione della cibersicurezza fornendo una giustificazione e una proposta di metodologia di valutazione. L'autorità nazionale di certificazione della cibersicurezza valuta se l'eccezione sia giustificata e, in caso affermativo, approva o modifica la metodologia di valutazione che dovrà essere applicata dall'organismo di valutazione della conformità. In attesa della decisione dell'autorità nazionale di certificazione della cibersicurezza, l'organismo di valutazione della conformità non rilascia alcun certificato. L'autorità nazionale di certificazione della cibersicurezza segnala senza indebito ritardo la certificazione prevista al gruppo europeo per la certificazione della cibersicurezza, che può formulare un parere. L'autorità nazionale di certificazione della cibersicurezza tiene nella massima considerazione il parere del gruppo europeo per la certificazione della cibersicurezza.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 7 §5",
        "testo": "Nel caso di un prodotto TIC sottoposto a una valutazione di prodotto composito conformemente ai pertinenti documenti sullo stato dell'arte, l'ITSEF che ha effettuato la valutazione del prodotto TIC sottostante condivide le informazioni pertinenti con l'ITSEF che effettua la valutazione del prodotto TIC composito.",
        "testo_integrale": "5. Nel caso di un prodotto TIC sottoposto a una valutazione di prodotto composito conformemente ai pertinenti documenti sullo stato dell'arte, l'ITSEF che ha effettuato la valutazione del prodotto TIC sottostante condivide le informazioni pertinenti con l'ITSEF che effettua la valutazione del prodotto TIC composito.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando un prodotto TIC è sottoposto a una valutazione di prodotto composito.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 8 §1",
        "testo": "Il richiedente la certificazione nel quadro dell'EUCC fornisce o mette altrimenti a disposizione dell'organismo di certificazione e dell'ITSEF tutte le informazioni necessarie per le attività di certificazione.",
        "testo_integrale": "Articolo 8\n\nInformazioni necessarie per la certificazione\n\n1. Il richiedente la certificazione nel quadro dell'EUCC fornisce o mette altrimenti a disposizione dell'organismo di certificazione e dell'ITSEF tutte le informazioni necessarie per le attività di certificazione.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 8 §2",
        "testo": "Le informazioni di cui al paragrafo 1 comprendono tutti gli elementi di prova pertinenti in conformità delle sezioni relative alle «Azioni dello sviluppatore», nel formato indicato nelle sezioni «Contenuto e presentazione dell'elemento di prova» dei criteri comuni e della metodologia comune di valutazione per il livello di affidabilità selezionato e i requisiti di garanzia della sicurezza associati; gli elementi di prova includono, se necessario, dettagli sul prodotto TIC e sul suo codice sorgente in conformità del presente regolamento, fatte salve le salvaguardie contro la divulgazione non autorizzata.",
        "testo_integrale": "2. Le informazioni di cui al paragrafo 1 comprendono tutti gli elementi di prova pertinenti in conformità delle sezioni relative alle «Azioni dello sviluppatore» nel formato appropriato, come indicato nelle sezioni «Contenuto e presentazione dell'elemento di prova» dei criteri comuni e della metodologia comune di valutazione per il livello di affidabilità selezionato e i requisiti di garanzia della sicurezza associati. Gli elementi di prova includono, se necessario, dettagli sul prodotto TIC e sul suo codice sorgente in conformità del presente regolamento, fatte salve le salvaguardie contro la divulgazione non autorizzata.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 8 §5",
        "testo": "Se l'organismo di certificazione consente di sottoporre il prodotto a una certificazione di prodotto composito, il richiedente la certificazione mette a disposizione dell'organismo di certificazione e dell'ITSEF tutti gli elementi necessari, se del caso, in conformità del documento sullo stato dell'arte.",
        "testo_integrale": "5. Se l'organismo di certificazione consente di sottoporre il prodotto a una certificazione di prodotto composito, il richiedente la certificazione mette a disposizione dell'organismo di certificazione e dell'ITSEF tutti gli elementi necessari, se del caso, in conformità del documento sullo stato dell'arte.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se l'organismo di certificazione consente di sottoporre il prodotto a una certificazione di prodotto composito.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 8 §6",
        "testo": "I richiedenti la certificazione forniscono inoltre all'organismo di certificazione e all'ITSEF: il link al proprio sito web contenente le informazioni supplementari sulla cibersicurezza di cui all'articolo 55 del regolamento (UE) 2019/881; una descrizione delle procedure di gestione e divulgazione delle vulnerabilità del richiedente.",
        "testo_integrale": "6. I richiedenti la certificazione forniscono inoltre all'organismo di certificazione e all'ITSEF le informazioni seguenti:\n\n(a) il link al proprio sito web contenente le informazioni supplementari sulla cibersicurezza di cui all'articolo 55 del regolamento (UE) 2019/881;\n\n(b) una descrizione delle procedure di gestione e divulgazione delle vulnerabilità del richiedente.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 8 §7",
        "testo": "Tutta la documentazione pertinente di cui al presente articolo è conservata dall'organismo di certificazione, dall'ITSEF e dal richiedente per un periodo di cinque anni dopo la scadenza del certificato.",
        "testo_integrale": "7. Tutta la documentazione pertinente di cui al presente articolo è conservata dall'organismo di certificazione, dall'ITSEF e dal richiedente per un periodo di cinque anni dopo la scadenza del certificato.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 9 §1",
        "testo": "Gli organismi di certificazione rilasciano un certificato EUCC se sono soddisfatte tutte le condizioni seguenti: la categoria di prodotto TIC rientra nell'ambito di applicazione dell'accreditamento, ed eventualmente dell'autorizzazione, dell'organismo di certificazione e dell'ITSEF coinvolti nella certificazione; il richiedente ha firmato una dichiarazione con cui si assume tutti gli impegni di cui al paragrafo 2; l'ITSEF ha concluso la valutazione senza obiezioni in conformità delle norme, dei criteri e dei metodi di valutazione di cui agli articoli 3 e 7; l'organismo di certificazione ha concluso il riesame dei risultati della valutazione senza obiezioni; l'organismo ha verificato che le relazioni tecniche di valutazione fornite dall'ITSEF siano coerenti con gli elementi di prova forniti e che le norme, i criteri e i metodi di valutazione di cui agli articoli 3 e 7 siano stati applicati correttamente.",
        "testo_integrale": "Articolo 9\n\nCondizioni per il rilascio di un certificato EUCC\n\n1. Gli organismi di certificazione rilasciano un certificato EUCC se sono soddisfatte tutte le condizioni seguenti:\n\n(a) la categoria di prodotto TIC rientra nell'ambito di applicazione dell'accreditamento, ed eventualmente dell'autorizzazione, dell'organismo di certificazione e dell'ITSEF coinvolti nella certificazione;\n\n(b) il richiedente la certificazione ha firmato una dichiarazione con cui si assume tutti gli impegni di cui al paragrafo 2;\n\n(c) l'ITSEF ha concluso la valutazione senza obiezioni in conformità delle norme, dei criteri e dei metodi di valutazione di cui agli articoli 3 e 7;\n\n(d) l'organismo di certificazione ha concluso il riesame dei risultati della valutazione senza obiezioni;\n\n(e) l'organismo di certificazione ha verificato che le relazioni tecniche di valutazione fornite dall'ITSEF siano coerenti con gli elementi di prova forniti e che le norme, i criteri e i metodi di valutazione di cui agli articoli 3 e 7 siano stati applicati correttamente.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 9 §2",
        "testo": "Il richiedente la certificazione si assume gli impegni seguenti: presentazione all'organismo di certificazione e all'ITSEF di tutte le informazioni necessarie, complete e corrette, e di ulteriori informazioni necessarie, se richiesto; astensione dalla promozione del prodotto TIC come certificato nel quadro dell'EUCC prima che il certificato EUCC sia stato rilasciato; promozione del prodotto TIC come certificato solo in relazione all'ambito di applicazione stabilito nel certificato EUCC; cessazione immediata della promozione del prodotto TIC come certificato in caso di sospensione, revoca o scadenza del certificato EUCC; garanzia che i prodotti TIC venduti facendo riferimento al certificato EUCC siano esattamente identici al prodotto TIC oggetto della certificazione; rispetto delle norme di utilizzo del marchio e dell'etichetta stabilite per il certificato EUCC in conformità dell'articolo 11.",
        "testo_integrale": "2. Il richiedente la certificazione si assume gli impegni seguenti:\n\n(a) presentazione all'organismo di certificazione e all'ITSEF di tutte le informazioni necessarie, complete e corrette, e di ulteriori informazioni necessarie, se richiesto;\n\n(b) astensione dalla promozione del prodotto TIC come certificato nel quadro dell'EUCC prima che il certificato EUCC sia stato rilasciato;\n\n(c) promozione del prodotto TIC come certificato solo in relazione all'ambito di applicazione stabilito nel certificato EUCC;\n\n(d) cessazione immediata della promozione del prodotto TIC come certificato in caso di sospensione, revoca o scadenza del certificato EUCC;\n\n(e) garanzia che i prodotti TIC venduti facendo riferimento al certificato EUCC siano esattamente identici al prodotto TIC oggetto della certificazione;\n\n(f) rispetto delle norme di utilizzo del marchio e dell'etichetta stabilite per il certificato EUCC in conformità dell'articolo 11.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 9 §3",
        "testo": "Nel caso di un prodotto TIC sottoposto a una certificazione di prodotto composito conformemente ai pertinenti documenti sullo stato dell'arte, l'organismo di certificazione che ha effettuato la certificazione del prodotto TIC sottostante condivide le informazioni pertinenti con l'organismo di certificazione che effettua la certificazione del prodotto TIC composito.",
        "testo_integrale": "3. Nel caso di un prodotto TIC sottoposto a una certificazione di prodotto composito conformemente ai pertinenti documenti sullo stato dell'arte, l'organismo di certificazione che ha effettuato la certificazione del prodotto TIC sottostante condivide le informazioni pertinenti con l'organismo di certificazione che effettua la certificazione del prodotto TIC composito.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando un prodotto TIC è sottoposto a una certificazione di prodotto composito.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 10 §1",
        "testo": "Il certificato EUCC contiene almeno le informazioni di cui all'allegato VII.",
        "testo_integrale": "Articolo 10\n\nContenuto e formato del certificato EUCC\n\n1. Il certificato EUCC contiene almeno le informazioni di cui all'allegato VII.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 §2",
        "testo": "Nel certificato EUCC o nella relazione di certificazione sono specificati in modo inequivocabile l'ambito e i limiti del prodotto TIC certificato, ed è indicato se la certificazione riguarda l'intero prodotto TIC o solo alcune sue parti.",
        "testo_integrale": "2. Nel certificato EUCC o nella relazione di certificazione sono specificati in modo inequivocabile l'ambito e i limiti del prodotto TIC certificato, ed è indicato se la certificazione riguarda l'intero prodotto TIC o solo alcune sue parti.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 §3",
        "testo": "L'organismo di certificazione fornisce al richiedente il certificato EUCC almeno in formato elettronico.",
        "testo_integrale": "3. L'organismo di certificazione fornisce al richiedente il certificato EUCC almeno in formato elettronico.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 10 §4",
        "testo": "L'organismo di certificazione elabora una relazione di certificazione in conformità dell'allegato V per ciascun certificato EUCC rilasciato; la relazione di certificazione si basa sulla relazione tecnica di valutazione redatta dall'ITSEF; la relazione tecnica di valutazione e la relazione di certificazione indicano i criteri e i metodi di valutazione specifici di cui all'articolo 7 utilizzati per la valutazione.",
        "testo_integrale": "4. L'organismo di certificazione elabora una relazione di certificazione in conformità dell'allegato V per ciascun certificato EUCC rilasciato. La relazione di certificazione si basa sulla relazione tecnica di valutazione redatta dall'ITSEF. La relazione tecnica di valutazione e la relazione di certificazione indicano i criteri e i metodi di valutazione specifici di cui all'articolo 7 utilizzati per la valutazione.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 §5",
        "testo": "L'organismo di certificazione fornisce all'autorità nazionale di certificazione della cibersicurezza e all'ENISA tutti i certificati EUCC e tutte le relazioni di certificazione in formato elettronico.",
        "testo_integrale": "5. L'organismo di certificazione fornisce all'autorità nazionale di certificazione della cibersicurezza e all'ENISA tutti i certificati EUCC e tutte le relazioni di certificazione in formato elettronico.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 11 §2",
        "testo": "Il marchio e l'etichetta sono apposti in modo visibile, leggibile e indelebile sul prodotto TIC certificato o sulla sua targhetta identificativa; qualora ciò sia impossibile o difficilmente realizzabile a causa della natura del prodotto, sono apposti sull'imballaggio o sui documenti di accompagnamento; se il prodotto certificato è fornito sotto forma di software, figurano in modo visibile, leggibile e indelebile sui documenti di accompagnamento, o tali documenti sono resi facilmente e direttamente accessibili agli utenti attraverso un sito web.",
        "testo_integrale": "2. Il marchio e l'etichetta sono apposti in modo visibile, leggibile e indelebile sul prodotto TIC certificato o sulla sua targhetta identificativa. Qualora ciò sia impossibile o difficilmente realizzabile a causa della natura del prodotto, essi sono apposti sull'imballaggio o sui documenti di accompagnamento. Se il prodotto TIC certificato è fornito sotto forma di software, il marchio e l'etichetta figurano in modo visibile, leggibile e indelebile sui documenti di accompagnamento, o tali documenti sono resi facilmente e direttamente accessibili agli utenti attraverso un sito web.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 11 §3",
        "testo": "Il marchio e l'etichetta sono conformi al quanto disposto nell'allegato IX e contengono: il livello di affidabilità e il livello AVA_VAN del prodotto TIC certificato; l'identificatore unico del certificato, costituito da denominazione del sistema, denominazione e numero di riferimento dell'accreditamento dell'organismo di certificazione che ha rilasciato il certificato, anno e mese di rilascio, numero di identificazione assegnato dall'organismo di certificazione che ha rilasciato il certificato.",
        "testo_integrale": "3. Il marchio e l'etichetta sono conformi al quanto disposto nell'allegato IX e contengono:\n\n(a) il livello di affidabilità e il livello AVA_VAN del prodotto TIC certificato;\n\n(b) l'identificatore unico del certificato, costituito dagli elementi seguenti:\n\n(1) denominazione del sistema;\n\n(2) denominazione e numero di riferimento dell'accreditamento dell'organismo di certificazione che ha rilasciato il certificato;\n\n(3) anno e mese di rilascio;\n\n(4) numero di identificazione assegnato dall'organismo di certificazione che ha rilasciato il certificato.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 §4",
        "testo": "Il marchio e l'etichetta sono accompagnati da un codice QR con un link a un sito web contenente almeno: le informazioni sulla validità del certificato; le informazioni necessarie sulla certificazione di cui agli allegati V e VII; le informazioni che il titolare del certificato deve rendere pubblicamente disponibili conformemente all'articolo 55 del regolamento (UE) 2019/881; nonché, se del caso, le informazioni storiche relative alla certificazione o alle certificazioni specifiche del prodotto TIC per consentire la tracciabilità.",
        "testo_integrale": "4. Il marchio e l'etichetta sono accompagnati da un codice QR con un link a un sito web contenente almeno:\n\n(a) le informazioni sulla validità del certificato;\n\n(b) le informazioni necessarie sulla certificazione, di cui agli allegati V e VII;\n\n(c) le informazioni che il titolare del certificato deve rendere pubblicamente disponibili conformemente all'articolo 55 del regolamento (UE) 2019/881; nonché\n\n(d) se del caso, le informazioni storiche relative alla certificazione o alle certificazioni specifiche del prodotto TIC per consentire la tracciabilità.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 12 §1",
        "testo": "L'organismo di certificazione stabilisce un periodo di validità per ciascun certificato EUCC rilasciato tenendo conto delle caratteristiche del prodotto TIC certificato.",
        "testo_integrale": "Articolo 12\n\nPeriodo di validità del certificato EUCC\n\n1. L'organismo di certificazione stabilisce un periodo di validità per ciascun certificato EUCC rilasciato tenendo conto delle caratteristiche del prodotto TIC certificato.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 12 §2",
        "testo": "Il periodo di validità del certificato EUCC non supera i cinque anni.",
        "testo_integrale": "2. Il periodo di validità del certificato EUCC non supera i cinque anni.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 12 §3",
        "testo": "In deroga al paragrafo 2 tale periodo può superare i cinque anni, previa approvazione da parte dell'autorità nazionale di certificazione della cibersicurezza; l'autorità nazionale di certificazione della cibersicurezza notifica al gruppo europeo per la certificazione della cibersicurezza l'approvazione concessa senza indebito ritardo.",
        "testo_integrale": "3. In deroga al paragrafo 2 tale periodo può superare i cinque anni, previa approvazione da parte dell'autorità nazionale di certificazione della cibersicurezza. L'autorità nazionale di certificazione della cibersicurezza notifica al gruppo europeo per la certificazione della cibersicurezza l'approvazione concessa senza indebito ritardo.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica previa approvazione da parte dell'autorità nazionale di certificazione della cibersicurezza.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 13 §1",
        "testo": "Su richiesta del titolare del certificato o per altri motivi giustificati, l'organismo di certificazione può decidere di riesaminare il certificato EUCC per un prodotto TIC; il riesame è effettuato conformemente all'allegato IV; l'organismo determina la portata del riesame e, se necessario, chiede all'ITSEF di effettuare una nuova valutazione del prodotto TIC certificato.",
        "testo_integrale": "Articolo 13\n\nRiesame del certificato EUCC\n\n1. Su richiesta del titolare del certificato o per altri motivi giustificati, l'organismo di certificazione può decidere di riesaminare il certificato EUCC per un prodotto TIC. Il riesame è effettuato conformemente all'allegato IV. L'organismo di certificazione determina la portata del riesame. Se necessario per il riesame, l'organismo di certificazione chiede all'ITSEF di effettuare una nuova valutazione del prodotto TIC certificato.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica su richiesta del titolare del certificato o per altri motivi giustificati.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 13 §2",
        "testo": "A seguito dei risultati del riesame e, se del caso, della nuova valutazione, l'organismo di certificazione: conferma il certificato EUCC; oppure revoca il certificato EUCC in conformità dell'articolo 14; oppure revoca il certificato EUCC in conformità dell'articolo 14 e rilascia un nuovo certificato EUCC con un ambito di applicazione identico e un periodo di validità prorogato; oppure revoca il certificato EUCC in conformità dell'articolo 14 e rilascia un nuovo certificato EUCC con un ambito di applicazione diverso.",
        "testo_integrale": "2. A seguito dei risultati del riesame e, se del caso, della nuova valutazione, l'organismo di certificazione:\n\n(a) conferma il certificato EUCC;\n\n(b) revoca il certificato EUCC in conformità dell'articolo 14;\n\n(c) revoca il certificato EUCC in conformità dell'articolo 14 e rilascia un nuovo certificato EUCC con un ambito di applicazione identico e un periodo di validità prorogato; oppure\n\n(d) revoca il certificato EUCC in conformità dell'articolo 14 e rilascia un nuovo certificato EUCC con un ambito di applicazione diverso.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 14 §1",
        "testo": "Fatto salvo l'articolo 58, paragrafo 8, lettera e), del regolamento (UE) 2019/881, un certificato EUCC è revocato dall'organismo di certificazione che lo ha rilasciato.",
        "testo_integrale": "Articolo 14\n\nRevoca del certificato EUCC\n\n1. Fatto salvo l'articolo 58, paragrafo 8, lettera e), del regolamento (UE) 2019/881, un certificato EUCC è revocato dall'organismo di certificazione che lo ha rilasciato.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Fatto salvo l'articolo 58, paragrafo 8, lettera e), del regolamento (UE) 2019/881.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 14 §2",
        "testo": "L'organismo di certificazione di cui al paragrafo 1 notifica la revoca del certificato all'autorità nazionale di certificazione della cibersicurezza; la notifica è trasmessa anche all'ENISA al fine di facilitare l'esecuzione dei suoi compiti a norma dell'articolo 50 del regolamento (UE) 2019/881; l'autorità nazionale di certificazione della cibersicurezza informa le altre autorità di vigilanza del mercato competenti.",
        "testo_integrale": "2. L'organismo di certificazione di cui al paragrafo 1 notifica la revoca del certificato all'autorità nazionale di certificazione della cibersicurezza. Tale notifica è trasmessa anche all'ENISA al fine di facilitare l'esecuzione dei suoi compiti a norma dell'articolo 50 del regolamento (UE) 2019/881. L'autorità nazionale di certificazione della cibersicurezza informa le altre autorità di vigilanza del mercato competenti.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 8 §3",
        "testo": "I richiedenti la certificazione possono fornire all'organismo di certificazione e all'ITSEF risultati della valutazione adeguati provenienti da una precedente certificazione a norma del presente regolamento, di un altro sistema europeo di certificazione della cibersicurezza adottato a norma dell'articolo 49 del regolamento (UE) 2019/881 o di un sistema nazionale di cui all'articolo 49 del presente regolamento.",
        "testo_integrale": "3. I richiedenti la certificazione possono fornire all'organismo di certificazione e all'ITSEF risultati della valutazione adeguati provenienti da una precedente certificazione a norma:\n\n(a) del presente regolamento;\n\n(b) di un altro sistema europeo di certificazione della cibersicurezza adottato a norma dell'articolo 49 del regolamento (UE) 2019/881;\n\n(c) di un sistema nazionale di cui all'articolo 49 del presente regolamento.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica ai richiedenti che dispongono di risultati di valutazione provenienti da una precedente certificazione.",
        "oggetti_giuridici": ["altro"],
    },
    {
        "riferimento": "art. 8 §4",
        "testo": "Se i risultati della valutazione sono pertinenti ai suoi compiti, l'ITSEF può riutilizzarli, a condizione che siano conformi ai requisiti applicabili e che la loro autenticità sia confermata.",
        "testo_integrale": "4. Se i risultati della valutazione sono pertinenti ai suoi compiti, l'ITSEF può riutilizzarli, a condizione che siano conformi ai requisiti applicabili e che la loro autenticità sia confermata.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica ai risultati della valutazione pertinenti ai compiti dell'ITSEF, conformi ai requisiti applicabili e con autenticità confermata.",
        "oggetti_giuridici": ["altro"],
    },
    {
        "riferimento": "art. 11 §1",
        "testo": "Il titolare di un certificato può apporre un marchio e un'etichetta su un prodotto TIC certificato; il marchio e l'etichetta dimostrano che il prodotto TIC è stato certificato in conformità del presente regolamento e sono apposti in conformità del presente articolo e dell'allegato IX.",
        "testo_integrale": "Articolo 11\n\nMarchio ed etichetta\n\n1. Il titolare di un certificato può apporre un marchio e un'etichetta su un prodotto TIC certificato. Il marchio e l'etichetta dimostrano che il prodotto TIC è stato certificato in conformità del presente regolamento. Essi sono apposti in conformità del presente articolo e dell'allegato IX.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["altro"],
    },
    {
        "riferimento": "art. 13 §3",
        "testo": "L'organismo di certificazione può decidere di sospendere, senza indebito ritardo, il certificato EUCC in conformità dell'articolo 30, in attesa di una misura correttiva da parte del titolare del certificato EUCC.",
        "testo_integrale": "3. L'organismo di certificazione può decidere di sospendere, senza indebito ritardo, il certificato EUCC in conformità dell'articolo 30, in attesa di una misura correttiva da parte del titolare del certificato EUCC.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica in attesa di una misura correttiva da parte del titolare del certificato EUCC.",
        "oggetti_giuridici": ["altro"],
    },
    {
        "riferimento": "art. 14 §3",
        "testo": "Il titolare di un certificato EUCC può richiedere la revoca del certificato.",
        "testo_integrale": "3. Il titolare di un certificato EUCC può richiedere la revoca del certificato.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["altro"],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 7 §1",
    "art. 7 §1(a)",
    "art. 7 §1(b)",
    "art. 7 §1(c)",
    "art. 7 §1(d)",
    "art. 7 §1(e)",
    "art. 7 §2",
    "art. 7 §3",
    "art. 7 §3(a)",
    "art. 7 §3(b)",
    "art. 7 §3(c)",
    "art. 7 §4",
    "art. 7 §5",
    "art. 8 §1",
    "art. 8 §2",
    "art. 8 §3",
    "art. 8 §3(a)",
    "art. 8 §3(b)",
    "art. 8 §3(c)",
    "art. 8 §4",
    "art. 8 §5",
    "art. 8 §6",
    "art. 8 §6(a)",
    "art. 8 §6(b)",
    "art. 8 §7",
    "art. 9 §1",
    "art. 9 §1(a)",
    "art. 9 §1(b)",
    "art. 9 §1(c)",
    "art. 9 §1(d)",
    "art. 9 §1(e)",
    "art. 9 §2",
    "art. 9 §2(a)",
    "art. 9 §2(b)",
    "art. 9 §2(c)",
    "art. 9 §2(d)",
    "art. 9 §2(e)",
    "art. 9 §2(f)",
    "art. 9 §3",
    "art. 10 §1",
    "art. 10 §2",
    "art. 10 §3",
    "art. 10 §4",
    "art. 10 §5",
    "art. 11 §1",
    "art. 11 §2",
    "art. 11 §3",
    "art. 11 §3(a)",
    "art. 11 §3(b)",
    "art. 11 §4",
    "art. 11 §4(a)",
    "art. 11 §4(b)",
    "art. 11 §4(c)",
    "art. 11 §4(d)",
    "art. 12 §1",
    "art. 12 §2",
    "art. 12 §3",
    "art. 13 §1",
    "art. 13 §2",
    "art. 13 §2(a)",
    "art. 13 §2(b)",
    "art. 13 §2(c)",
    "art. 13 §2(d)",
    "art. 13 §3",
    "art. 14 §1",
    "art. 14 §2",
    "art. 14 §3",
]

MAPPATURA_LOCALE = {
    # art. 7 §1 e art. 7 §3: il chapeau porta il precetto, le lettere ne sono
    # elementi/scenari - una riga per comma, tutti gli item mappati su di essa.
    "art. 7 §1": [
        "art. 7 §1",
        "art. 7 §1(a)",
        "art. 7 §1(b)",
        "art. 7 §1(c)",
        "art. 7 §1(d)",
        "art. 7 §1(e)",
    ],
    "art. 7 §2": ["art. 7 §2"],
    "art. 7 §3": [
        "art. 7 §3",
        "art. 7 §3(a)",
        "art. 7 §3(b)",
        "art. 7 §3(c)",
    ],
    "art. 7 §4": ["art. 7 §4"],
    "art. 7 §5": ["art. 7 §5"],
    "art. 8 §1": ["art. 8 §1"],
    "art. 8 §2": ["art. 8 §2"],
    "art. 8 §3": [
        "art. 8 §3",
        "art. 8 §3(a)",
        "art. 8 §3(b)",
        "art. 8 §3(c)",
    ],
    "art. 8 §4": ["art. 8 §4"],
    "art. 8 §5": ["art. 8 §5"],
    "art. 8 §6": [
        "art. 8 §6",
        "art. 8 §6(a)",
        "art. 8 §6(b)",
    ],
    "art. 8 §7": ["art. 8 §7"],
    "art. 9 §1": [
        "art. 9 §1",
        "art. 9 §1(a)",
        "art. 9 §1(b)",
        "art. 9 §1(c)",
        "art. 9 §1(d)",
        "art. 9 §1(e)",
    ],
    "art. 9 §2": [
        "art. 9 §2",
        "art. 9 §2(a)",
        "art. 9 §2(b)",
        "art. 9 §2(c)",
        "art. 9 §2(d)",
        "art. 9 §2(e)",
        "art. 9 §2(f)",
    ],
    "art. 9 §3": ["art. 9 §3"],
    "art. 10 §1": ["art. 10 §1"],
    "art. 10 §2": ["art. 10 §2"],
    "art. 10 §3": ["art. 10 §3"],
    "art. 10 §4": ["art. 10 §4"],
    "art. 10 §5": ["art. 10 §5"],
    "art. 11 §1": ["art. 11 §1"],
    "art. 11 §2": ["art. 11 §2"],
    "art. 11 §3": [
        "art. 11 §3",
        "art. 11 §3(a)",
        "art. 11 §3(b)",
    ],
    "art. 11 §4": [
        "art. 11 §4",
        "art. 11 §4(a)",
        "art. 11 §4(b)",
        "art. 11 §4(c)",
        "art. 11 §4(d)",
    ],
    "art. 12 §1": ["art. 12 §1"],
    "art. 12 §2": ["art. 12 §2"],
    "art. 12 §3": ["art. 12 §3"],
    "art. 13 §1": ["art. 13 §1"],
    # art. 13 §2: le quattro lettere sono gli esiti possibili (alternativi) di
    # una decisione unica dell'organismo di certificazione, non precetti
    # cumulativi distinti: una riga, quattro item mappati su di essa.
    "art. 13 §2": [
        "art. 13 §2",
        "art. 13 §2(a)",
        "art. 13 §2(b)",
        "art. 13 §2(c)",
        "art. 13 §2(d)",
    ],
    "art. 13 §3": ["art. 13 §3"],
    "art. 14 §1": ["art. 14 §1"],
    "art. 14 §2": ["art. 14 §2"],
    "art. 14 §3": ["art. 14 §3"],
}

# Relazioni interne a questo modulo (fonte_id_o_None = None su entrambi gli
# estremi), dettagliate nel docstring in testa al file. Nessuna relazione verso
# altri capitoli o altre Fonti: i rinvii esterni sono elencati nel docstring
# sotto "rinvii demandati alla fase 6".
RELAZIONI = [
    # art. 7 §3 -> art. 7 §4: "alle condizioni di cui al paragrafo 4".
    {
        "nodo_da": ("obbligo", None, "art. 7 §3"),
        "nodo_a": ("obbligo", None, "art. 7 §4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # art. 7 §4 -> art. 7 §3: "di cui al paragrafo 3, lettera c)".
    {
        "nodo_da": ("obbligo", None, "art. 7 §4"),
        "nodo_a": ("obbligo", None, "art. 7 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # art. 9 §1 -> art. 9 §2: "gli impegni di cui al paragrafo 2".
    {
        "nodo_da": ("obbligo", None, "art. 9 §1"),
        "nodo_a": ("obbligo", None, "art. 9 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # art. 9 §1 -> art. 7 §1: "i criteri e i metodi di valutazione di cui agli
    # articoli 3 e 7" (il rinvio all'art. 3 e' demandato alla fase 6).
    {
        "nodo_da": ("obbligo", None, "art. 9 §1"),
        "nodo_a": ("obbligo", None, "art. 7 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # art. 10 §4 -> art. 7 §1: "i criteri e i metodi di valutazione specifici di
    # cui all'articolo 7 utilizzati per la valutazione".
    {
        "nodo_da": ("obbligo", None, "art. 10 §4"),
        "nodo_a": ("obbligo", None, "art. 7 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # art. 9 §2 -> art. 11 §1 e §2: "le norme di utilizzo del marchio e
    # dell'etichetta stabilite per il certificato EUCC in conformità
    # dell'articolo 11".
    {
        "nodo_da": ("obbligo", None, "art. 9 §2"),
        "nodo_a": ("principio", None, "art. 11 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 §2"),
        "nodo_a": ("obbligo", None, "art. 11 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # art. 13 §2 -> art. 14 §1: "revoca il certificato EUCC in conformità
    # dell'articolo 14" (lettere (b), (c) e (d)).
    {
        "nodo_da": ("obbligo", None, "art. 13 §2"),
        "nodo_a": ("obbligo", None, "art. 14 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # art. 14 §2 -> art. 14 §1: "L'organismo di certificazione di cui al
    # paragrafo 1".
    {
        "nodo_da": ("obbligo", None, "art. 14 §2"),
        "nodo_a": ("obbligo", None, "art. 14 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    # art. 12 §3 -> art. 12 §2: "In deroga al paragrafo 2".
    {
        "nodo_da": ("obbligo", None, "art. 12 §3"),
        "nodo_a": ("obbligo", None, "art. 12 §2"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": None,
    },
    # art. 11 §2, §3, §4 -> art. 11 §1: si applicano solo se il titolare appone
    # il marchio e l'etichetta (facolta' di art. 11 §1). Condizionalita'
    # dedotta dal contenuto, non citata: evidence_type "inferred".
    {
        "nodo_da": ("obbligo", None, "art. 11 §2"),
        "nodo_a": ("principio", None, "art. 11 §1"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 11 §3"),
        "nodo_a": ("principio", None, "art. 11 §1"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 11 §4"),
        "nodo_a": ("principio", None, "art. 11 §1"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "inferred",
        "confidence": None,
    },
]
