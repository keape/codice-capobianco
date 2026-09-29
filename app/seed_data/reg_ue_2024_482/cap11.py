"""Regolamento di esecuzione (UE) 2024/482 della Commissione, del 31 gennaio
2024 - modalita' di applicazione del regolamento (UE) 2019/881 del Parlamento
europeo e del Consiglio per quanto riguarda l'adozione del sistema europeo di
certificazione della cibersicurezza basato sui criteri comuni (EUCC). Fonte 29
(slug `reg_ue_2024_482`), capitolo 11 di 14 (vedi
app/.source_cache/reg_ue_2024_482/manifest.json): Allegato IV - Continuita'
dell'affidabilita' e riesame dei certificati. Gli artt. 1-50 e gli allegati
I-III e V-IX appartengono ai capitoli 1-10 e 12-14 della stessa Fonte,
assegnati ad altri moduli: nessuno di quei file e' toccato qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_482/cap11.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R0482, lingua italiana; URL
risolto
http://publications.europa.eu/resource/cellar/687c0d05-c580-11ee-95d9-01aa75ed71a1.0014.03/DOC_1,
XHTML della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 540.435 byte
scaricati, 135.367 caratteri di testo, sha256 del raw.txt
b46d08cab6d63b2c190ae767042c07c1fc324955c22ef491eb314556b28ca5b8 - dettagli
completi in app/.source_cache/reg_ue_2024_482/provenance.json). La porzione
assegnata e' l'allegato IV per intero: dall'intestazione "ALLEGATO IV" alla
riga che precede "ALLEGATO V". Il preambolo (considerando 1-33) e' a monte
degli allegati e non e' in questa porzione; qui non compaiono epigrafe, firma,
formula di chiusura, note a pie' di pagina ne' riga ELI, quindi nessuno di
questi elementi produce nodo o item di indice.

Convenzione dei riferimenti (nota di capitolo: allegato strutturato in sezioni
numerate):
- le quattro sezioni sono numerate "IV.1" ... "IV.4" nel testo ufficiale,
  quindi il riferimento e' "allegato IV, sezione IV.1" e cosi' via: il numero
  romano della sezione non e' convertito in arabo, si censisce la numerazione
  come la Gazzetta ufficiale la pubblica. E' la stessa forma gia' usata dal
  cap05 di questa Fonte (art. 25 §6, "la procedura di cui all'allegato IV,
  sezione IV.2");
- i punti numerati dentro una sezione sono "allegato IV, sezione IV.N, punto
  M"; le lettere e le sotto-numerazioni seguono la convenzione del censimento:
  "..., punto M(a)" e "..., punto M(a)(1)" (stessa forma del cap09 di questa
  Fonte per l'allegato I);
- gli stessi riferimenti sono usati da INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE
  e RELAZIONI.

Modellazione (ADR-0007, nessun punto dell'allegato non coperto, nessuno
coperto due volte; un articolo/comma = una riga, con le eccezioni motivate
sotto):
- Paratesto -> nessuna riga e nessun item: l'intestazione "ALLEGATO IV" e il
  suo titolo ("CONTINUITA' DELL'AFFIDABILITA' E RIESAME DEI CERTIFICATI") non
  sono punti ma struttura dell'atto, e non sono assorbiti nel `testo_integrale`
  di nessuna riga (stesso trattamento dei titoli degli allegati I e II nel
  cap09 di questa Fonte). Nessun item a livello di allegato ("allegato IV"): i
  punti dell'allegato sono numerati, e la convenzione del censimento riserva
  l'item di livello-allegato ai testi che non numerano i punti (cap09).
- Intestazioni di sezione ("IV.1 Continuita' dell'affidabilita': ambito di
  applicazione", "IV.2 Nuova valutazione", "IV.3 Modifiche di un prodotto TIC
  certificato", "IV.4 Gestione delle patch") -> UNA riga Principio "altro"
  ciascuna, con il solo titolo verbatim nel `testo_integrale` e il contenuto
  della sezione riassunto nel `testo`. Qui le intestazioni NON sono trattate
  come il paratesto degli allegati del cap09 (che le esclude dal grafo) per due
  ragioni dichiarate: (1) la nota di capitolo di questo import prescrive
  riferimenti a livello di sezione; (2) il cap05 di questa stessa Fonte (art.
  25 §6) rinvia alla "procedura di cui all'allegato IV, sezione IV.2" e la
  relazione della fase 6 deve risolversi su una riga con quel riferimento, che
  esiste solo se la sezione ha un nodo proprio. tipo_principio "altro" e non
  "scopo/ambito di applicazione": la rubrica non enuncia essa stessa l'ambito
  (lo enuncia il punto 1 della sezione IV.1). Cinque delle 32 righe di questo
  modulo non enunciano un precetto proprio: le quattro intestazioni di sezione
  e il chapeau del punto 5 della sezione IV.4 (descritto sotto).
- IV.1, punto 1 ("I seguenti requisiti ... si applicano alle attivita' di
  mantenimento relative a quanto segue:" + lettere (a)-(d)) -> UNA riga
  Principio "scopo/ambito di applicazione", con i cinque item (punto 1 e
  lettere). Le quattro lettere sono frammenti nominali ("una nuova valutazione
  se un prodotto TIC certificato rimasto invariato soddisfa ancora i requisiti
  di sicurezza;" e simili) senza verbo proprio, retti dall'unico predicato del
  chapeau: nessuna ha precetto autonomo e nessuna e' azionabile da sola, quindi
  non producono righe proprie (stessa soluzione del punto 1 dell'allegato I nel
  cap09 di questa Fonte). E' la sezione che l'intero allegato intitola "ambito
  di applicazione", quindi il tipo e' quello dedicato e non "altro":
  l'allegato dichiara a quali attivita' di mantenimento si applicano i propri
  requisiti, senza imporre un comportamento a un soggetto identificato.
- IV.1, punto 2 ("Il titolare di un certificato EUCC puo' richiedere il riesame
  del certificato nei casi seguenti:" + lettere (a)-(c)) -> UNA riga Principio
  "altro", con i quattro item. Le tre lettere elencano casi di fatto (scadenza
  entro nove mesi, modifica del prodotto o di un altro fattore, richiesta di
  nuova valutazione delle vulnerabilita'), non prescrizioni autonome: il
  precetto del comma e' uno solo, la facolta' di chiedere il riesame. Dubbio di
  classificazione dichiarato: il criterio del batch include fra gli Obblighi
  anche le disposizioni che "conferiscono un diritto esercitabile nei confronti
  di un altro", lettura con cui questo punto sarebbe un Obbligo "procedurale"
  del titolare verso l'organismo di certificazione; scelto il Principio perche'
  il testo attribuisce una facolta' e non impone un comportamento al titolare,
  perche' il template riserva ai Principi i "poteri conferiti" e perche' e' lo
  stesso trattamento che il cap02 di questa Fonte riserva alla facolta'
  simmetrica ("Il titolare di un certificato EUCC puo' richiedere la revoca del
  certificato", art. 14 §3, Principio "altro"). Da riconciliare, se serve, con
  i capitoli 2 e 14 di questa Fonte.
- IV.2: una riga per ciascuno dei cinque punti numerati, tutte Obbligo, tutte
  con soggetto desumibile dal testo tranne il punto 1 (sotto).
  * punto 1 (richiesta di nuova valutazione presentata all'organismo di
    certificazione) -> Obbligo "procedurale" senza `soggetti`: il comma e'
    interamente impersonale e non nomina chi presenta la richiesta (puo' essere
    il titolare del certificato, come nel punto 2 della sezione IV.1, o
    l'autorita' nazionale di certificazione della cibersicurezza, come
    nell'art. 25 §6 del cap05 di questa Fonte), quindi nessuna categoria e'
    affermata dal testo. E' lo stesso trattamento riservato dal cap03 di questa
    Fonte alle righe impersonali (art. 17 §4 e art. 20 §2, senza `soggetti`).
  * punto 2 (nuova valutazione effettuata dalla stessa ITSEF, con
    riutilizzazione dei risultati validi e concentrazione su AVA_VAN e ALC) ->
    Obbligo "procedurale", soggetto "Terza parte" (l'ITSEF e' l'organismo
    esterno che valuta, come in tutto il cap02 di questa Fonte): il tipo scelto
    e' "procedurale" e non "tecnico/sicurezza" perche' il comma disciplina il
    metodo della rivalutazione, non una proprieta' tecnica del prodotto.
  * punto 3 (l'ITSEF descrive i cambiamenti e presenta i risultati aggiornando
    la relazione tecnica di valutazione) -> Obbligo "procedurale", "Terza
    parte".
  * punto 4 (l'organismo esamina la relazione aggiornata, redige la relazione
    di nuova valutazione e modifica lo stato del certificato iniziale in
    conformita' dell'articolo 13) -> Obbligo "procedurale", "Terza parte";
    l'articolo 13 e' fuori da questo modulo (cap02): rinvio demandato alla fase
    6, nessuna relazione dichiarata qui.
  * punto 5 (relazione di nuova valutazione e certificato aggiornato forniti
    all'autorita' nazionale di certificazione della cibersicurezza e all'ENISA
    per la pubblicazione) -> Obbligo "informativo/trasparenza", categorie
    "Terza parte" (obbligato e destinatario), come per il flusso informativo
    gemello dell'art. 23 §4 (cap04) di questa Fonte; l'obbligato non e' nominato
    (costruzione passiva) ed e' desunto dal punto 4, che assegna all'organismo
    di certificazione la redazione della relazione e del certificato.
- IV.3: una riga per ciascuno dei nove punti numerati, tutte Obbligo. Le due
  eccezioni di granularita' sono il punto 2 (chapeau + cinque lettere) e il
  punto 5 (chapeau + lettere (a) e (b) con le sotto-voci (1)-(3)): in entrambi i
  casi le lettere non hanno predicato proprio - sono voci dell'elenco retto dal
  chapeau o condizioni poste al rilascio del nuovo certificato - quindi restano
  nel `testo_integrale` della riga del punto, con item di indice separati
  (stessa soluzione del cap09 per l'allegato I e dell'art. 5 §1 del Reg.
  2024/2979 cap02, chapeau con le otto lettere in una sola riga). Categorie: le righe che descrivono il comportamento
  del titolare del certificato (punti 1 e 2) hanno "Utente/titolare" obbligato
  (il titolare del certificato EUCC e' la categoria "Utente/titolare" in tutto
  il censimento, vedi art. 41 §§2-4 del cap07 di questa Fonte), le righe che
  descrivono l'attivita' dell'organismo di certificazione e dell'ITSEF (punti
  3-5, 7, 8) "Terza parte" obbligato, le righe di fornitura all'ENISA (punti 6
  e 9) "Terza parte" obbligato e destinatario. `condizione_applicabilita`
  valorizzata dove il comma e' subordinato a un fatto: punto 1 (prodotto
  certificato modificato che il titolare intende mantenere), punto 5 (modifiche
  confermate di minore entita'), punto 7 (modifiche confermate di maggiore
  entita'), punto 8 (al termine della valutazione dell'oggetto modificato).
- IV.4: sei punti numerati, due dei quali (5 e 6) si scompongono in chapeau +
  lettere perche' le lettere hanno precetto autonomo:
  * punto 1 (che cosa prevede una procedura di gestione delle patch; la
    procedura puo' essere utilizzata dopo la certificazione sotto la
    responsabilita' dell'organismo di valutazione della conformita') ->
    Principio "altro": descrive l'istituto e attribuisce una facolta', senza
    imporre un comportamento; il tipo non e' "definitorio" perche' il comma non
    e' un elenco definitorio (chapeau + definizioni numerate), ma una
    descrizione con una facolta' in coda.
  * punto 2 (facolta' del richiedente di includere nella certificazione un
    meccanismo di patch, a una delle tre condizioni elencate) -> Principio
    "altro" con i quattro item: le lettere (a)-(c) sono condizioni della
    facolta', non prescrizioni autonome.
  * punto 3 ("si applicano le disposizioni dell'articolo 13") -> Principio
    "altro": e' una disposizione di rinvio condizionato, senza soggetto ne'
    comportamento proprio (stesso trattamento dell'art. 17 §2 del cap03 di
    questa Fonte). L'articolo 13 e' nel cap02: rinvio demandato alla fase 6.
  * punto 4 (elementi di cui la procedura di gestione delle patch e' composta)
    -> Obbligo "procedurale" con i quattro item: il comma prescrive il
    contenuto obbligatorio della procedura (le tre lettere sono voci dell'elenco
    retto dal chapeau, senza predicato proprio). Soggetto "Terza parte",
    desunto dai punti 2 e 5(a), che attribuiscono la procedura e la sua
    descrizione al richiedente la certificazione (categoria "Terza parte" per il
    richiedente la certificazione in tutto il cap02 di questa Fonte, es. art. 8
    §1).
  * punto 5 (chapeau "Durante la certificazione del prodotto TIC:" + tre
    lettere) -> QUATTRO righe: il chapeau, che enuncia la sola cornice temporale
    di applicazione, come Principio "scopo/ambito di applicazione" (prima
    occorrenza del modulo in cui un chapeau non e' assorbito in una riga di
    lettera: qui le tre lettere hanno soggetti diversi - richiedente, ITSEF,
    organismo di certificazione - e ciascuna un precetto autonomo, quindi
    ognuna ha la propria riga Obbligo, con item "punto 5(a)", "punto 5(b)" e
    "punto 5(c)"). La lettera (b) resta una riga sola con le sotto-voci (1)-(3)
    nel `testo_integrale`, perche' sono gli elementi che l'ITSEF deve
    verificare, elencati senza predicato proprio. tipo_obbligo: "procedurale"
    per 5(a) (fornitura della descrizione della procedura) e 5(c) (inclusione
    dell'esito nella relazione di certificazione), "tecnico/sicurezza" per 5(b)
    (verifica tecnica dei meccanismi di patch, della separazione dei limiti
    dell'oggetto della valutazione e del funzionamento del meccanismo, come per
    la valutazione del prodotto dell'art. 7 §1 del cap02). Il chapeau non e'
    ripetuto nei `testo_integrale` delle lettere (niente duplicazione verbatim,
    convenzione del Reg. 2025/1569 cap03).
  * punto 6 (chapeau: facolta' del titolare di applicare la patch + obbligo di
    adottare le misure indicate entro cinque giorni lavorativi nei casi
    elencati) -> QUATTRO righe: il chapeau come Obbligo "procedurale" (contiene
    l'unico termine perentorio del punto: cinque giorni lavorativi) con soggetto
    "Utente/titolare" obbligato, e le tre lettere come altrettanti Obblighi,
    perche' ciascuna prescrive un'attivita' distinta e autonomamente azionabile
    (segnalazione all'organismo di certificazione; sottoposizione all'ITSEF per
    il riesame; sottoposizione all'ITSEF per la nuova valutazione) in un caso
    diverso. Alternativa considerata e scartata: una riga unica per il punto 6,
    leggendo le lettere come semplici specificazioni della misura unica del
    chapeau; scartata perche' le tre attivita' hanno destinatari e conseguenze
    diverse e la voce di indice del punto resta comunque coperta dal chapeau.
    tipo_obbligo: "informativo/trasparenza" per 6(a) (segnalazione alla
    autorita' di certificazione), "procedurale" per il chapeau, per 6(b) e per
    6(c). Le lettere (b) e (c) contengono anche gli adempimenti conseguenti
    dell'ITSEF e dell'organismo di certificazione (informare, emettere la nuova
    versione del certificato e aggiornare la relazione di certificazione;
    avviare le attivita' di certificazione): restano nella riga della lettera,
    perche' sono il seguito del medesimo fatto, e il soggetto "Terza parte" e'
    dichiarato obbligato accanto a "Utente/titolare".
- `severita` e `sanzioni` non valorizzate in nessuna riga: il regolamento non
  gradua i requisiti qui censiti ne' prevede sanzioni proprie (l'unico
  riferimento a un sistema sanzionatorio, l'art. 44 §3(a)(3) del cap08 di
  questa Fonte, e' un requisito richiesto al paese terzo, non una sanzione di
  questo atto). `stato` = "vigente" per tutte le righe.
  `oggetti_giuridici` non valorizzato per nessuno dei dieci Principi: fra i
  valori censiti non ce n'e' uno che corrisponda alla certificazione EUCC di
  prodotti TIC e la voce generica "altro" non e' stata forzata (stesso criterio
  del cap09 e del cap10 di questa Fonte).
- `testo_integrale`: verbatim e integrale, ricucito dalle righe spezzate dalla
  conversione XHTML -> testo. I marcatori isolati su riga propria del dump
  ("1.", "2.", "(a)", "(b)", "(1)", "(2)", "(3)") sono uniti al testo che
  seguono ("1. I seguenti requisiti ...", "(a) una nuova valutazione ..."), come
  nei moduli del cap09 e del cap10 di questa Fonte; i blocchi restano separati
  da riga vuota. L'intestazione di sezione e' la prima riga del `testo_integrale`
  della riga di sezione ("IV.1 Continuita' dell'affidabilita': ambito di
  applicazione") e la numerazione del punto resta in testa al chapeau ("5."
  oppure "(a)", secondo il livello). La punteggiatura ufficiale e' conservata
  com'e', comprese le virgole finali delle lettere e il punto fermo che chiude
  alcuni elenchi. Nessun marcatore di elisione (vincolo
  `verifica_completezza_testo_integrale`, ADR-0010).
- RELAZIONI: nove relazioni interne, tutte fra nodi dichiarati in questo
  modulo. Tre sono citazioni letterali verificate nel `testo_integrale` del
  nodo citante (`evidence_type` "textual"): le lettere del punto 6 della sezione
  IV.4 richiamano il punto 2 della stessa sezione ("nel caso di cui al punto 2,
  lettera a)", "lettera b)", "lettera c)"). Sei sono dedotte dal contenuto
  (`evidence_type` "inferred"): la nuova valutazione presuppone la richiesta
  (IV.2 punto 2 -> IV.2 punto 1); l'esame dell'organismo presuppone la relazione
  sull'analisi dell'impatto (IV.3 punto 3 -> IV.3 punto 1); la determinazione
  dell'entita' della modifica presuppone l'esame (IV.3 punto 4 -> IV.3 punto 3);
  il rilascio del nuovo certificato e la nuova valutazione presuppongono la
  determinazione di modifiche minori o maggiori (IV.3 punto 5 -> IV.3 punto 4 e
  IV.3 punto 7 -> IV.3 punto 4); la verifica dell'ITSEF presuppone che il
  richiedente abbia fornito la descrizione della procedura di gestione delle
  patch (IV.4 punto 5(b) -> IV.4 punto 5(a)). `confidence` None su tutte:
  nessuno score reale da riportare (ADR-0005, non va inventato). Nessuna
  relazione verso altre righe di questa Fonte o verso altre Fonti: le costruisce
  la sessione principale in fase 6 (ADR-0009), e dichiararle qui in import
  parallelo per capitolo farebbe fallire il merge.
- Rinvii demandati alla fase 6 (nessuna relazione dichiarata qui):
  articolo 13 di questa Fonte, citato letteralmente dal punto 4 della sezione
  IV.2 ("Lo stato del certificato iniziale e' quindi modificato in conformita'
  dell'articolo 13") e dal punto 3 della sezione IV.4 ("si applicano le
  disposizioni dell'articolo 13") -> censito nel cap02; allegato IV in blocco,
  citato dall'art. 13 §1 (cap02, "Il riesame e' effettuato conformemente
  all'allegato IV") e richiamato in entrata dall'art. 25 §6 (cap05, "la
  procedura di cui all'allegato IV, sezione IV.2") -> il bersaglio del rinvio
  entrante e' la riga di sezione "allegato IV, sezione IV.2" dichiarata qui; sito web relativo alla certificazione della cibersicurezza e
  pubblicazione dei certificati e delle relazioni, di cui ai punti 5 della
  sezione IV.2 e 6 e 9 della sezione IV.3 -> disciplina generale nell'art. 42
  (cap07); "relazione di manutenzione", "relazione di nuova valutazione" e
  "nuova relazione di certificazione" -> contenuto della relazione di
  certificazione nell'allegato V (cap12), quando censito; "developer evidence",
  famiglie AVA_VAN e ALC -> terminologia dei criteri comuni (regolamento (UE)
  2019/881), non una fonte censita.
- Dubbi di classificazione lasciati aperti (segnalati, non risolti in
  autonomia):
  * IV.1 punto 2 -> Principio "altro" invece di Obbligo "procedurale" (diritto
    esercitabile): motivi sopra, da riconciliare con cap02 art. 14 §3 e cap14;
  * IV.4 punto 3 -> Principio "altro" (rinvio condizionato) invece di Obbligo
    con `condizione_applicabilita`: la sostanza del punto e' "si applicano le
    disposizioni dell'articolo 13", senza soggetto ne' comportamento;
  * IV.2 punto 5 e IV.3 punti 6 e 9 -> "informativo/trasparenza" invece di
    "procedurale": il flusso informativo e' verso l'ENISA per la pubblicazione
    (come art. 23 §4 del cap04), ma l'art. 10 §5 del cap02, di contenuto
    analogo, e' censito come "procedurale";
  * IV.2 punto 1 -> riga senza `soggetti` perche' il comma non nomina chi
    presenta la richiesta (titolare o autorita' nazionale).

Copertura: 58 item di indice, 32 righe (22 Obblighi + 10 Principi), 9 relazioni
interne.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "allegato IV, sezione IV.2, punto 1",
        "testo": "Qualora sia necessario valutare l'impatto dei cambiamenti nel panorama delle minacce di un prodotto TIC certificato rimasto invariato, è presentata all'organismo di certificazione una richiesta di nuova valutazione. Il comma non nomina chi presenta la richiesta.",
        "testo_integrale": "1. Qualora sia necessario valutare l'impatto dei cambiamenti nel panorama delle minacce di un prodotto TIC certificato rimasto invariato, è presentata all'organismo di certificazione una richiesta di nuova valutazione.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica qualora sia necessario valutare l'impatto dei cambiamenti nel panorama delle minacce di un prodotto TIC certificato rimasto invariato.",
    },
    {
        "riferimento": "allegato IV, sezione IV.2, punto 2",
        "testo": "La nuova valutazione è effettuata dalla stessa ITSEF che ha partecipato alla valutazione precedente, che riutilizza tutti i risultati ancora validi; si concentra sulle attività di garanzia dell'affidabilità potenzialmente interessate dai cambiamenti nel panorama delle minacce, in particolare la famiglia AVA_VAN pertinente e la famiglia del ciclo di vita dell'affidabilità (assurance lifecycle, ALC), per le quali sono nuovamente raccolti elementi di prova sufficienti sulla manutenzione dell'ambiente di sviluppo.",
        "testo_integrale": "2. La nuova valutazione è effettuata dalla stessa ITSEF che ha partecipato alla valutazione precedente, che riutilizza tutti i risultati ancora validi. La valutazione si concentra sulle attività di garanzia dell'affidabilità che sono potenzialmente interessate dai cambiamenti nel panorama delle minacce del prodotto TIC certificato, in particolare la famiglia AVA_VAN pertinente, nonché la famiglia del ciclo di vita dell'affidabilità (assurance lifecycle, ALC) per le quali sono nuovamente raccolti elementi di prova sufficienti sulla manutenzione dell'ambiente di sviluppo.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato IV, sezione IV.2, punto 3",
        "testo": "L'ITSEF descrive i cambiamenti e presenta nel dettaglio i risultati della nuova valutazione con un aggiornamento della precedente relazione tecnica di valutazione.",
        "testo_integrale": "3. L'ITSEF descrive i cambiamenti e presenta nel dettaglio i risultati della nuova valutazione con un aggiornamento della precedente relazione tecnica di valutazione.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato IV, sezione IV.2, punto 4",
        "testo": "L'organismo di certificazione esamina la relazione tecnica di valutazione aggiornata e redige una relazione di nuova valutazione; lo stato del certificato iniziale è quindi modificato in conformità dell'articolo 13.",
        "testo_integrale": "4. L'organismo di certificazione esamina la relazione tecnica di valutazione aggiornata e redige una relazione di nuova valutazione. Lo stato del certificato iniziale è quindi modificato in conformità dell'articolo 13.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato IV, sezione IV.2, punto 5",
        "testo": "La relazione di nuova valutazione e il certificato aggiornato sono forniti all'autorità nazionale di certificazione della cibersicurezza e all'ENISA per la pubblicazione sul sito web relativo alla certificazione della cibersicurezza. Il comma non nomina chi fornisce i documenti; l'obbligato è l'organismo di certificazione di cui al punto 4.",
        "testo_integrale": "5. La relazione di nuova valutazione e il certificato aggiornato sono forniti all'autorità nazionale di certificazione della cibersicurezza e all'ENISA per la pubblicazione sul sito web relativo alla certificazione della cibersicurezza.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato IV, sezione IV.3, punto 1",
        "testo": "Se un prodotto TIC certificato è stato soggetto a modifiche, il titolare del certificato che intende mantenerlo fornisce all'organismo di certificazione una relazione sull'analisi dell'impatto.",
        "testo_integrale": "1. Se un prodotto TIC certificato è stato soggetto a modifiche, il titolare del certificato che intende mantenerlo fornisce all'organismo di certificazione una relazione sull'analisi dell'impatto.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se il prodotto TIC certificato è stato soggetto a modifiche e il titolare del certificato intende mantenerlo.",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato IV, sezione IV.3, punto 2",
        "testo": "Nella relazione sull'analisi dell'impatto sono forniti: un'introduzione con le informazioni necessarie per identificare la relazione e l'oggetto della valutazione modificato (a), una descrizione delle modifiche apportate al prodotto (b), l'identificazione della developer evidence interessata (c), una descrizione delle modifiche della developer evidence (d) e i risultati e le conclusioni in merito all'impatto sull'affidabilità per ciascuna modifica (e).",
        "testo_integrale": "2. Nella relazione sull'analisi dell'impatto sono forniti gli elementi seguenti:\n\n(a) un'introduzione contenente le informazioni necessarie per identificare la relazione sull'analisi dell'impatto e l'oggetto della valutazione soggetto a modifiche;\n\n(b) una descrizione delle modifiche apportate al prodotto;\n\n(c) l'identificazione della developer evidence interessata;\n\n(d) una descrizione delle modifiche della developer evidence;\n\n(e) i risultati e le conclusioni in merito all'impatto sull'affidabilità per ciascuna modifica.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato IV, sezione IV.3, punto 3",
        "testo": "L'organismo di certificazione esamina le modifiche descritte nella relazione sull'analisi dell'impatto per convalidare il loro impatto sull'affidabilità dell'oggetto della valutazione certificato, come proposto nelle conclusioni di detta relazione.",
        "testo_integrale": "3. L'organismo di certificazione esamina le modifiche descritte nella relazione sull'analisi dell'impatto per convalidare il loro impatto sull'affidabilità dell'oggetto della valutazione certificato, come proposto nelle conclusioni di detta relazione.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato IV, sezione IV.3, punto 4",
        "testo": "A seguito dell'esame, l'organismo di certificazione stabilisce l'entità di una modifica definendola minore o maggiore in base al suo impatto.",
        "testo_integrale": "4. A seguito dell'esame, l'organismo di certificazione stabilisce l'entità di una modifica definendola minore o maggiore in base al suo impatto.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato IV, sezione IV.3, punto 5",
        "testo": "Qualora l'organismo di certificazione abbia confermato che le modifiche sono di minore entità, è rilasciato un nuovo certificato per il prodotto TIC modificato ed è redatta una relazione di manutenzione in riferimento alla relazione di certificazione iniziale, alle condizioni seguenti: la relazione di manutenzione è inclusa come sottoinsieme della relazione sull'analisi dell'impatto e contiene introduzione, descrizione delle modifiche e developer evidence interessata (a); la data di validità del nuovo certificato non supera quella del certificato iniziale (b).",
        "testo_integrale": "5. Qualora l'organismo di certificazione abbia confermato che le modifiche sono di minore entità, è rilasciato un nuovo certificato per il prodotto TIC modificato ed è redatta una relazione di manutenzione in riferimento alla relazione di certificazione iniziale alle condizioni seguenti:\n\n(a) la relazione di manutenzione è inclusa come sottoinsieme della relazione sull'analisi dell'impatto e contiene le sezioni seguenti:\n\n(1) introduzione;\n\n(2) descrizione delle modifiche;\n\n(3) developer evidence interessata;\n\n(b) la data di validità del nuovo certificato non supera quella del certificato iniziale.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica qualora l'organismo di certificazione abbia confermato che le modifiche sono di minore entità.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato IV, sezione IV.3, punto 6",
        "testo": "Il nuovo certificato, compresa la relazione di manutenzione, è fornito all'ENISA per la pubblicazione sul sito web relativo alla certificazione della cibersicurezza.",
        "testo_integrale": "6. Il nuovo certificato, compresa la relazione di manutenzione, è fornito all'ENISA per la pubblicazione sul sito web relativo alla certificazione della cibersicurezza.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica al nuovo certificato rilasciato a seguito della conferma di modifiche di minore entità (punto 5).",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato IV, sezione IV.3, punto 7",
        "testo": "Nel caso in cui sia stato confermato che le modifiche sono di maggiore entità, si procede a una nuova valutazione nel contesto della valutazione precedente e riutilizzando tutti i risultati della valutazione precedente ancora validi.",
        "testo_integrale": "7. Nel caso in cui sia stato confermato che le modifiche sono di maggiore entità, si procede a una nuova valutazione nel contesto della valutazione precedente e riutilizzando tutti i risultati della valutazione precedente ancora validi.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica nel caso in cui sia stato confermato che le modifiche sono di maggiore entità.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato IV, sezione IV.3, punto 8",
        "testo": "Al termine della valutazione dell'oggetto della valutazione modificato, l'ITSEF redige una nuova relazione tecnica di valutazione; l'organismo di certificazione esamina la relazione tecnica di valutazione aggiornata e, se del caso, redige un nuovo certificato con una nuova relazione di certificazione.",
        "testo_integrale": "8. Al termine della valutazione dell'oggetto della valutazione modificato, l'ITSEF redige una nuova relazione tecnica di valutazione. L'organismo di certificazione esamina la relazione tecnica di valutazione aggiornata e, se del caso, redige un nuovo certificato con una nuova relazione di certificazione.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica al termine della valutazione dell'oggetto della valutazione modificato (valutazione svolta nel contesto della valutazione precedente, punto 7).",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato IV, sezione IV.3, punto 9",
        "testo": "Il nuovo certificato e la nuova relazione di certificazione sono forniti all'ENISA per la pubblicazione.",
        "testo_integrale": "9. Il nuovo certificato e la nuova relazione di certificazione sono forniti all'ENISA per la pubblicazione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica al nuovo certificato e alla nuova relazione di certificazione redatti a seguito di una modifica di maggiore entità (punti 7 e 8).",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato IV, sezione IV.4, punto 4",
        "testo": "La procedura di gestione delle patch per un prodotto TIC è composta dai seguenti elementi: il processo di sviluppo e rilascio della patch per il prodotto TIC (a), il meccanismo tecnico e le funzioni per l'adozione della patch nel prodotto TIC (b) e una serie di attività di valutazione relative all'efficacia e alle prestazioni del meccanismo tecnico (c). Il soggetto obbligato non è nominato dal comma: è il richiedente la certificazione che la procedura è tenuta a descrivere (punto 5, lettera a).",
        "testo_integrale": "4. La procedura di gestione delle patch per un prodotto TIC sarà composta dagli elementi seguenti:\n\n(a) il processo di sviluppo e rilascio della patch per il prodotto TIC;\n\n(b) il meccanismo tecnico e le funzioni per l'adozione della patch nel prodotto TIC;\n\n(c) una serie di attività di valutazione relative all'efficacia e alle prestazioni del meccanismo tecnico.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato IV, sezione IV.4, punto 5(a)",
        "testo": "Durante la certificazione del prodotto TIC, il richiedente la certificazione fornisce la descrizione della procedura di gestione delle patch.",
        "testo_integrale": "(a) il richiedente la certificazione del prodotto TIC fornisce la descrizione della procedura di gestione delle patch;",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Durante la certificazione del prodotto TIC (chapeau del punto 5).",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato IV, sezione IV.4, punto 5(b)",
        "testo": "Durante la certificazione del prodotto TIC, l'ITSEF verifica che lo sviluppatore abbia implementato i meccanismi di patch nel prodotto TIC in conformità della procedura di gestione delle patch presentata ai fini della certificazione (1), che i limiti dell'oggetto della valutazione siano separati in modo che le modifiche apportate ai processi separati non influiscano sulla sicurezza dell'oggetto della valutazione (2) e che il meccanismo tecnico delle patch funzioni in conformità delle disposizioni della sezione e delle dichiarazioni del richiedente (3).",
        "testo_integrale": "(b) l'ITSEF verifica gli elementi seguenti:\n\n(1) lo sviluppatore ha implementato i meccanismi di patch nel prodotto TIC in conformità della procedura di gestione delle patch presentata ai fini della certificazione;\n\n(2) i limiti dell'oggetto della valutazione sono separati in modo che le modifiche apportate ai processi separati non influiscano sulla sicurezza dell'oggetto della valutazione;\n\n(3) il meccanismo tecnico delle patch funziona in conformità delle disposizioni della presente sezione e delle dichiarazioni del richiedente;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Durante la certificazione del prodotto TIC (chapeau del punto 5).",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato IV, sezione IV.4, punto 5(c)",
        "testo": "Durante la certificazione del prodotto TIC, l'organismo di certificazione include nella relazione di certificazione l'esito della procedura di gestione delle patch valutata.",
        "testo_integrale": "(c) l'organismo di certificazione include nella relazione di certificazione l'esito della procedura di gestione delle patch valutata.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Durante la certificazione del prodotto TIC (chapeau del punto 5).",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato IV, sezione IV.4, punto 6",
        "testo": "Il titolare del certificato può procedere all'applicazione della patch prodotta nel rispetto della procedura di gestione delle patch certificata al prodotto TIC certificato in questione e adotta le misure indicate nelle lettere entro cinque giorni lavorativi, nei casi ivi indicati.",
        "testo_integrale": "6. Il titolare del certificato può procedere all'applicazione della patch prodotta nel rispetto della procedura di gestione delle patch certificata al prodotto TIC certificato in questione e adotta le seguenti misure entro cinque giorni lavorativi nei casi indicati di seguito:",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Le misure vanno adottate entro cinque giorni lavorativi e presuppongono che la patch sia stata prodotta nel rispetto della procedura di gestione delle patch certificata.",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato IV, sezione IV.4, punto 6(a)",
        "testo": "Nel caso di cui al punto 2, lettera a), il titolare del certificato segnala la patch in questione all'organismo di certificazione, che non modifica il corrispondente certificato EUCC; la segnalazione va fatta entro cinque giorni lavorativi.",
        "testo_integrale": "(a) nel caso di cui al punto 2, lettera a), segnala la patch in questione all'organismo di certificazione, che non modifica il corrispondente certificato EUCC;",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Nel caso di cui al punto 2, lettera a) (patch che non incide sull'oggetto della valutazione); misura da adottare entro cinque giorni lavorativi (chapeau del punto 6).",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "allegato IV, sezione IV.4, punto 6(b)",
        "testo": "Nel caso di cui al punto 2, lettera b), il titolare del certificato sottopone la patch in questione all'ITSEF per il riesame; l'ITSEF informa l'organismo di certificazione della ricezione della patch e l'organismo di certificazione adotta le misure appropriate per l'emissione di una nuova versione del corrispondente certificato EUCC e per l'aggiornamento della relazione di certificazione; la misura va adottata entro cinque giorni lavorativi.",
        "testo_integrale": "(b) nel caso di cui al punto 2, lettera b), sottopone la patch in questione all'ITSEF per il riesame. L'ITSEF informa l'organismo di certificazione della ricezione della patch, e l'organismo di certificazione adotta le misure appropriate per l'emissione di una nuova versione del corrispondente certificato EUCC e l'aggiornamento della relazione di certificazione;",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Nel caso di cui al punto 2, lettera b) (patch relativa a una modifica di piccola entità predeterminata); misura da adottare entro cinque giorni lavorativi (chapeau del punto 6).",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "allegato IV, sezione IV.4, punto 6(c)",
        "testo": "Nel caso di cui al punto 2, lettera c), il titolare del certificato sottopone la patch in questione all'ITSEF per la nuova valutazione necessaria, ma può distribuire la patch in parallelo; l'ITSEF informa l'organismo di certificazione, che a sua volta avvia le relative attività di certificazione; la misura va adottata entro cinque giorni lavorativi.",
        "testo_integrale": "(c) nel caso di cui al punto 2, lettera c), sottopone la patch in questione all'ITSEF per la nuova valutazione necessaria, ma può distribuire la patch in parallelo. L'ITSEF informa l'organismo di certificazione, che a sua volta avvia le relative attività di certificazione.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Nel caso di cui al punto 2, lettera c) (patch relativa a una vulnerabilità confermata con effetti critici); misura da adottare entro cinque giorni lavorativi (chapeau del punto 6).",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "allegato IV, sezione IV.1",
        "testo": "La sezione IV.1 dell'allegato IV reca la rubrica «Continuità dell'affidabilità: ambito di applicazione» e contiene i punti 1 e 2: l'ambito di applicazione dei requisiti per la continuità dell'affidabilità (le attività di mantenimento) e i casi in cui il titolare di un certificato EUCC può richiedere il riesame del certificato. La riga è la rubrica della sezione: nessun precetto proprio.",
        "testo_integrale": "IV.1 Continuità dell'affidabilità: ambito di applicazione",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato IV, sezione IV.1, punto 1",
        "testo": "I requisiti per la continuità dell'affidabilità si applicano alle attività di mantenimento relative a: una nuova valutazione se un prodotto TIC certificato rimasto invariato soddisfa ancora i requisiti di sicurezza (a), una valutazione dell'impatto delle modifiche apportate a un prodotto TIC certificato sulla sua certificazione (b), l'applicazione di patch in conformità di un processo di gestione delle patch valutato, se inclusa nella certificazione (c) e il riesame dei processi di produzione o di gestione del ciclo di vita del titolare del certificato, se incluso (d). Il punto dichiara l'ambito di applicazione dei requisiti dell'allegato senza imporre un comportamento a un soggetto.",
        "testo_integrale": "1. I seguenti requisiti per la continuità dell'affidabilità si applicano alle attività di mantenimento relative a quanto segue:\n\n(a) una nuova valutazione se un prodotto TIC certificato rimasto invariato soddisfa ancora i requisiti di sicurezza;\n\n(b) una valutazione dell'impatto delle modifiche apportate a un prodotto TIC certificato sulla sua certificazione;\n\n(c) se inclusa nella certificazione, l'applicazione di patch in conformità di un processo di gestione delle patch valutato;\n\n(d) se incluso, il riesame dei processi di produzione o di gestione del ciclo di vita del titolare del certificato.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato IV, sezione IV.1, punto 2",
        "testo": "Il titolare di un certificato EUCC può richiedere il riesame del certificato in tre casi: il certificato scadrà entro i successivi nove mesi (a), si è verificata una modifica del prodotto TIC certificato o di un altro fattore che potrebbe avere un impatto sulla sua funzionalità di sicurezza (b), il titolare chiede che sia effettuata nuovamente la valutazione delle vulnerabilità al fine di riconfermare l'affidabilità del certificato EUCC associata alla resistenza del prodotto TIC agli attuali attacchi informatici (c). Il comma attribuisce una facoltà, non impone un comportamento.",
        "testo_integrale": "2. Il titolare di un certificato EUCC può richiedere il riesame del certificato nei casi seguenti:\n\n(a) il certificato EUCC scadrà entro i successivi nove mesi;\n\n(b) si è verificata una modifica del prodotto TIC certificato o di un altro fattore che potrebbe avere un impatto sulla sua funzionalità di sicurezza;\n\n(c) il titolare del certificato richiede che sia effettuata nuovamente la valutazione delle vulnerabilità al fine di riconfermare l'affidabilità del certificato EUCC associata alla resistenza del prodotto TIC agli attuali attacchi informatici.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato IV, sezione IV.2",
        "testo": "La sezione IV.2 dell'allegato IV reca la rubrica «Nuova valutazione» e contiene i punti da 1 a 5, che disciplinano la richiesta di nuova valutazione di un prodotto TIC certificato rimasto invariato, lo svolgimento della valutazione da parte della stessa ITSEF, la relazione tecnica aggiornata, la relazione di nuova valutazione dell'organismo di certificazione e la fornitura dei documenti all'autorità nazionale di certificazione della cibersicurezza e all'ENISA. La riga è la rubrica della sezione: nessun precetto proprio, ed è il bersaglio del rinvio dell'art. 25 §6 di questa Fonte alla procedura dell'allegato IV, sezione IV.2.",
        "testo_integrale": "IV.2 Nuova valutazione",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato IV, sezione IV.3",
        "testo": "La sezione IV.3 dell'allegato IV reca la rubrica «Modifiche di un prodotto TIC certificato» e contiene i punti da 1 a 9, che disciplinano la relazione sull'analisi dell'impatto del titolare del certificato, l'esame e la determinazione dell'entità della modifica da parte dell'organismo di certificazione, il rilascio del nuovo certificato in caso di modifiche di minore entità e la nuova valutazione in caso di modifiche di maggiore entità. La riga è la rubrica della sezione: nessun precetto proprio.",
        "testo_integrale": "IV.3 Modifiche di un prodotto TIC certificato",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato IV, sezione IV.4",
        "testo": "La sezione IV.4 dell'allegato IV reca la rubrica «Gestione delle patch» e contiene i punti da 1 a 6, che disciplinano la procedura di gestione delle patch, l'inclusione di un meccanismo di patch nella certificazione, il rinvio all'articolo 13 per le modifiche di grande entità, il contenuto della procedura, le verifiche durante la certificazione e le misure del titolare del certificato in caso di applicazione della patch. La riga è la rubrica della sezione: nessun precetto proprio.",
        "testo_integrale": "IV.4 Gestione delle patch",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato IV, sezione IV.4, punto 1",
        "testo": "Una procedura di gestione delle patch prevede un processo strutturato di aggiornamento di un prodotto TIC certificato; la procedura, compreso il meccanismo attuato nel prodotto TIC dal richiedente la certificazione, può essere utilizzata dopo la certificazione del prodotto TIC sotto la responsabilità dell'organismo di valutazione della conformità.",
        "testo_integrale": "1. Una procedura di gestione delle patch prevede un processo strutturato di aggiornamento di un prodotto TIC certificato. La procedura di gestione delle patch, compreso il meccanismo attuato nel prodotto TIC dal richiedente la certificazione, può essere utilizzata dopo la certificazione del prodotto TIC sotto la responsabilità dell'organismo di valutazione della conformità.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato IV, sezione IV.4, punto 2",
        "testo": "Il richiedente la certificazione può includere nella certificazione del prodotto TIC un meccanismo di patch come parte di una procedura di gestione certificata implementata nel prodotto TIC, a una delle condizioni seguenti: le funzionalità interessate dalla patch non rientrano nell'oggetto della valutazione del prodotto TIC certificato (a), la patch riguarda una modifica di piccola entità predeterminata (b), la patch riguarda una vulnerabilità confermata con effetti critici sulla sicurezza del prodotto TIC certificato (c).",
        "testo_integrale": "2. Il richiedente la certificazione può includere nella certificazione del prodotto TIC un meccanismo di patch come parte di una procedura di gestione certificata implementata nel prodotto TIC a una delle condizioni seguenti:\n\n(a) le funzionalità interessate dalla patch non rientrano nell'oggetto della valutazione del prodotto TIC certificato;\n\n(b) la patch riguarda una modifica di piccola entità predeterminata del prodotto TIC certificato;\n\n(c) la patch riguarda una vulnerabilità confermata con effetti critici sulla sicurezza del prodotto TIC certificato.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "La facoltà è esercitabile a una delle tre condizioni elencate nelle lettere a), b) e c): patch che non incide sull'oggetto della valutazione; modifica di piccola entità predeterminata; vulnerabilità confermata con effetti critici sulla sicurezza del prodotto TIC certificato.",
    },
    {
        "riferimento": "allegato IV, sezione IV.4, punto 3",
        "testo": "Se la patch si riferisce a una modifica di grande entità dell'oggetto della valutazione del prodotto TIC certificato in relazione a una vulnerabilità precedentemente non rilevata che non ha effetti critici per la sicurezza del prodotto TIC, si applicano le disposizioni dell'articolo 13. Il punto è un rinvio condizionato, senza soggetto e senza comportamento proprio.",
        "testo_integrale": "3. Se la patch si riferisce a una modifica di grande entità dell'oggetto della valutazione del prodotto TIC certificato in relazione a una vulnerabilità precedentemente non rilevata che non ha effetti critici per la sicurezza del prodotto TIC, si applicano le disposizioni dell'articolo 13.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se la patch si riferisce a una modifica di grande entità dell'oggetto della valutazione in relazione a una vulnerabilità precedentemente non rilevata che non ha effetti critici per la sicurezza del prodotto TIC.",
    },
    {
        "riferimento": "allegato IV, sezione IV.4, punto 5",
        "testo": "Il chapeau del punto 5 fissa il momento di applicazione delle prescrizioni che seguono: durante la certificazione del prodotto TIC. Non impone un comportamento proprio; gli adempimenti sono nelle lettere a) (descrizione della procedura di gestione delle patch fornita dal richiedente), b) (verifiche dell'ITSEF) e c) (inclusione dell'esito nella relazione di certificazione).",
        "testo_integrale": "5. Durante la certificazione del prodotto TIC:",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "allegato IV, sezione IV.1",
    "allegato IV, sezione IV.1, punto 1",
    "allegato IV, sezione IV.1, punto 1(a)",
    "allegato IV, sezione IV.1, punto 1(b)",
    "allegato IV, sezione IV.1, punto 1(c)",
    "allegato IV, sezione IV.1, punto 1(d)",
    "allegato IV, sezione IV.1, punto 2",
    "allegato IV, sezione IV.1, punto 2(a)",
    "allegato IV, sezione IV.1, punto 2(b)",
    "allegato IV, sezione IV.1, punto 2(c)",
    "allegato IV, sezione IV.2",
    "allegato IV, sezione IV.2, punto 1",
    "allegato IV, sezione IV.2, punto 2",
    "allegato IV, sezione IV.2, punto 3",
    "allegato IV, sezione IV.2, punto 4",
    "allegato IV, sezione IV.2, punto 5",
    "allegato IV, sezione IV.3",
    "allegato IV, sezione IV.3, punto 1",
    "allegato IV, sezione IV.3, punto 2",
    "allegato IV, sezione IV.3, punto 2(a)",
    "allegato IV, sezione IV.3, punto 2(b)",
    "allegato IV, sezione IV.3, punto 2(c)",
    "allegato IV, sezione IV.3, punto 2(d)",
    "allegato IV, sezione IV.3, punto 2(e)",
    "allegato IV, sezione IV.3, punto 3",
    "allegato IV, sezione IV.3, punto 4",
    "allegato IV, sezione IV.3, punto 5",
    "allegato IV, sezione IV.3, punto 5(a)",
    "allegato IV, sezione IV.3, punto 5(a)(1)",
    "allegato IV, sezione IV.3, punto 5(a)(2)",
    "allegato IV, sezione IV.3, punto 5(a)(3)",
    "allegato IV, sezione IV.3, punto 5(b)",
    "allegato IV, sezione IV.3, punto 6",
    "allegato IV, sezione IV.3, punto 7",
    "allegato IV, sezione IV.3, punto 8",
    "allegato IV, sezione IV.3, punto 9",
    "allegato IV, sezione IV.4",
    "allegato IV, sezione IV.4, punto 1",
    "allegato IV, sezione IV.4, punto 2",
    "allegato IV, sezione IV.4, punto 2(a)",
    "allegato IV, sezione IV.4, punto 2(b)",
    "allegato IV, sezione IV.4, punto 2(c)",
    "allegato IV, sezione IV.4, punto 3",
    "allegato IV, sezione IV.4, punto 4",
    "allegato IV, sezione IV.4, punto 4(a)",
    "allegato IV, sezione IV.4, punto 4(b)",
    "allegato IV, sezione IV.4, punto 4(c)",
    "allegato IV, sezione IV.4, punto 5",
    "allegato IV, sezione IV.4, punto 5(a)",
    "allegato IV, sezione IV.4, punto 5(b)",
    "allegato IV, sezione IV.4, punto 5(b)(1)",
    "allegato IV, sezione IV.4, punto 5(b)(2)",
    "allegato IV, sezione IV.4, punto 5(b)(3)",
    "allegato IV, sezione IV.4, punto 5(c)",
    "allegato IV, sezione IV.4, punto 6",
    "allegato IV, sezione IV.4, punto 6(a)",
    "allegato IV, sezione IV.4, punto 6(b)",
    "allegato IV, sezione IV.4, punto 6(c)",
]

MAPPATURA_LOCALE = {
    "allegato IV, sezione IV.1": [
        "allegato IV, sezione IV.1",
    ],
    "allegato IV, sezione IV.1, punto 1": [
        "allegato IV, sezione IV.1, punto 1",
        "allegato IV, sezione IV.1, punto 1(a)",
        "allegato IV, sezione IV.1, punto 1(b)",
        "allegato IV, sezione IV.1, punto 1(c)",
        "allegato IV, sezione IV.1, punto 1(d)",
    ],
    "allegato IV, sezione IV.1, punto 2": [
        "allegato IV, sezione IV.1, punto 2",
        "allegato IV, sezione IV.1, punto 2(a)",
        "allegato IV, sezione IV.1, punto 2(b)",
        "allegato IV, sezione IV.1, punto 2(c)",
    ],
    "allegato IV, sezione IV.2": [
        "allegato IV, sezione IV.2",
    ],
    "allegato IV, sezione IV.2, punto 1": [
        "allegato IV, sezione IV.2, punto 1",
    ],
    "allegato IV, sezione IV.2, punto 2": [
        "allegato IV, sezione IV.2, punto 2",
    ],
    "allegato IV, sezione IV.2, punto 3": [
        "allegato IV, sezione IV.2, punto 3",
    ],
    "allegato IV, sezione IV.2, punto 4": [
        "allegato IV, sezione IV.2, punto 4",
    ],
    "allegato IV, sezione IV.2, punto 5": [
        "allegato IV, sezione IV.2, punto 5",
    ],
    "allegato IV, sezione IV.3": [
        "allegato IV, sezione IV.3",
    ],
    "allegato IV, sezione IV.3, punto 1": [
        "allegato IV, sezione IV.3, punto 1",
    ],
    "allegato IV, sezione IV.3, punto 2": [
        "allegato IV, sezione IV.3, punto 2",
        "allegato IV, sezione IV.3, punto 2(a)",
        "allegato IV, sezione IV.3, punto 2(b)",
        "allegato IV, sezione IV.3, punto 2(c)",
        "allegato IV, sezione IV.3, punto 2(d)",
        "allegato IV, sezione IV.3, punto 2(e)",
    ],
    "allegato IV, sezione IV.3, punto 3": [
        "allegato IV, sezione IV.3, punto 3",
    ],
    "allegato IV, sezione IV.3, punto 4": [
        "allegato IV, sezione IV.3, punto 4",
    ],
    "allegato IV, sezione IV.3, punto 5": [
        "allegato IV, sezione IV.3, punto 5",
        "allegato IV, sezione IV.3, punto 5(a)",
        "allegato IV, sezione IV.3, punto 5(a)(1)",
        "allegato IV, sezione IV.3, punto 5(a)(2)",
        "allegato IV, sezione IV.3, punto 5(a)(3)",
        "allegato IV, sezione IV.3, punto 5(b)",
    ],
    "allegato IV, sezione IV.3, punto 6": [
        "allegato IV, sezione IV.3, punto 6",
    ],
    "allegato IV, sezione IV.3, punto 7": [
        "allegato IV, sezione IV.3, punto 7",
    ],
    "allegato IV, sezione IV.3, punto 8": [
        "allegato IV, sezione IV.3, punto 8",
    ],
    "allegato IV, sezione IV.3, punto 9": [
        "allegato IV, sezione IV.3, punto 9",
    ],
    "allegato IV, sezione IV.4": [
        "allegato IV, sezione IV.4",
    ],
    "allegato IV, sezione IV.4, punto 1": [
        "allegato IV, sezione IV.4, punto 1",
    ],
    "allegato IV, sezione IV.4, punto 2": [
        "allegato IV, sezione IV.4, punto 2",
        "allegato IV, sezione IV.4, punto 2(a)",
        "allegato IV, sezione IV.4, punto 2(b)",
        "allegato IV, sezione IV.4, punto 2(c)",
    ],
    "allegato IV, sezione IV.4, punto 3": [
        "allegato IV, sezione IV.4, punto 3",
    ],
    "allegato IV, sezione IV.4, punto 4": [
        "allegato IV, sezione IV.4, punto 4",
        "allegato IV, sezione IV.4, punto 4(a)",
        "allegato IV, sezione IV.4, punto 4(b)",
        "allegato IV, sezione IV.4, punto 4(c)",
    ],
    "allegato IV, sezione IV.4, punto 5": [
        "allegato IV, sezione IV.4, punto 5",
    ],
    "allegato IV, sezione IV.4, punto 5(a)": [
        "allegato IV, sezione IV.4, punto 5(a)",
    ],
    "allegato IV, sezione IV.4, punto 5(b)": [
        "allegato IV, sezione IV.4, punto 5(b)",
        "allegato IV, sezione IV.4, punto 5(b)(1)",
        "allegato IV, sezione IV.4, punto 5(b)(2)",
        "allegato IV, sezione IV.4, punto 5(b)(3)",
    ],
    "allegato IV, sezione IV.4, punto 5(c)": [
        "allegato IV, sezione IV.4, punto 5(c)",
    ],
    "allegato IV, sezione IV.4, punto 6": [
        "allegato IV, sezione IV.4, punto 6",
    ],
    "allegato IV, sezione IV.4, punto 6(a)": [
        "allegato IV, sezione IV.4, punto 6(a)",
    ],
    "allegato IV, sezione IV.4, punto 6(b)": [
        "allegato IV, sezione IV.4, punto 6(b)",
    ],
    "allegato IV, sezione IV.4, punto 6(c)": [
        "allegato IV, sezione IV.4, punto 6(c)",
    ],
}

# Relazioni interne a questo modulo (fonte_id_o_None = None su entrambi gli
# estremi). Tre "richiama" con `evidence_type` "textual": le lettere del punto 6
# della sezione IV.4 citano letteralmente il punto 2 della stessa sezione ("nel
# caso di cui al punto 2, lettera a)", "lettera b)", "lettera c)"), verificato
# nel `testo_integrale` delle righe citanti. Sei relazioni con `evidence_type`
# "inferred": i legami sono dedotti dal contenuto (la nuova valutazione
# presuppone la richiesta; l'esame e la determinazione dell'entita' della
# modifica presuppongono la relazione sull'analisi dell'impatto; il rilascio del
# nuovo certificato e la nuova valutazione presuppongono la determinazione
# dell'entita' della modifica; la verifica dell'ITSEF presuppone la descrizione
# della procedura fornita dal richiedente). `confidence` None su tutte: nessuno
# score reale da riportare (ADR-0005, non va inventato). I rinvii all'articolo
# 13 di questa Fonte (cap02) e all'allegato V (cap12) non sono dichiarati qui:
# sono collegamenti della fase 6, elencati nel docstring.
RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "allegato IV, sezione IV.4, punto 6(a)"),
        "nodo_a": ("principio", None, "allegato IV, sezione IV.4, punto 2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato IV, sezione IV.4, punto 6(b)"),
        "nodo_a": ("principio", None, "allegato IV, sezione IV.4, punto 2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato IV, sezione IV.4, punto 6(c)"),
        "nodo_a": ("principio", None, "allegato IV, sezione IV.4, punto 2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato IV, sezione IV.2, punto 2"),
        "nodo_a": ("obbligo", None, "allegato IV, sezione IV.2, punto 1"),
        "tipo_relazione": "richiede come precondizione",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato IV, sezione IV.3, punto 3"),
        "nodo_a": ("obbligo", None, "allegato IV, sezione IV.3, punto 1"),
        "tipo_relazione": "richiede come precondizione",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato IV, sezione IV.3, punto 4"),
        "nodo_a": ("obbligo", None, "allegato IV, sezione IV.3, punto 3"),
        "tipo_relazione": "richiede come precondizione",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato IV, sezione IV.3, punto 5"),
        "nodo_a": ("obbligo", None, "allegato IV, sezione IV.3, punto 4"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato IV, sezione IV.3, punto 7"),
        "nodo_a": ("obbligo", None, "allegato IV, sezione IV.3, punto 4"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "allegato IV, sezione IV.4, punto 5(b)"),
        "nodo_a": ("obbligo", None, "allegato IV, sezione IV.4, punto 5(a)"),
        "tipo_relazione": "richiede come precondizione",
        "evidence_type": "inferred",
        "confidence": None,
    },
]
