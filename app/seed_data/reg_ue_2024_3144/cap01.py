"""Regolamento di esecuzione (UE) 2024/3144 della Commissione, del 18 dicembre
2024, che modifica il regolamento di esecuzione (UE) 2024/482 per quanto
riguarda le norme internazionali applicabili e che rettifica tale regolamento
di esecuzione. Fonte 30 (`reg_ue_2024_3144`), capitolo 1 di 5 (vedi
app/.source_cache/reg_ue_2024_3144/manifest.json): articolo 1, punti 1-3
(definizioni di «criteri comuni» e «metodologia comune di valutazione», norme
di valutazione, nuovo articolo 20 bis sull'accreditamento). I punti 4-8
dell'articolo 1, gli articoli 2-3 e gli allegati I e II sono nei capitoli 2-5
della stessa Fonte, assegnati ad altri moduli: nessuno di quei file e' toccato
qui.

Avvertenza di perimetro: questa Fonte e' un atto MODIFICATIVO e RETTIFICATIVO
del regolamento di esecuzione (UE) 2024/482, censito in questa stessa
lavorazione come Fonte 29 (`reg_ue_2024_482`, 14 capitoli; l'id numerico della
Fonte lo assegna il seed della sessione principale). Le righe di questo modulo
non sono disposizioni autonome del nuovo atto: sono i punti con cui l'atto
modificativo interviene sul regolamento modificato, e il loro `testo_integrale`
riporta verbatim il punto, compreso il testo sostitutivo fra virgolette («...»)
con i suoi paragrafi, lettere e note. Le disposizioni del regolamento
modificato richiamate dai punti NON sono censite qui come nodi autonomi (vivono
in Fonte 29) e le relazioni verso Fonte 29 (modifica / sostituisce / abroga) le
costruisce la sessione principale in fase 6: questo modulo non ne dichiara
nessuna e documenta sotto, riga per riga, quale articolo del regolamento
modificato ciascun punto tocca e con quale tipo di intervento.

Provenienza del testo: app/.source_cache/reg_ue_2024_3144/cap01.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R3144, lingua italiana; URL
risolto
http://publications.europa.eu/resource/cellar/12c401d0-bdaa-11ef-91ed-01aa75ed71a1.0014.03/DOC_1,
XHTML della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 74.420 byte
scaricati, 22.217 caratteri di testo, sha256 del raw.txt
7ced6d4bfe633cf367b3c72ec593ebd5e49c369c7f86f4386984fe81cb81493a - dettagli
completi in provenance.json). La porzione cap01.txt e' stata confrontata con la
corrispondente porzione del raw.txt (dall'intestazione "Articolo 1" fino a
"... figuranti all'allegato I, punto 2.»;"): identica a meno della
normalizzazione degli spazi, come previsto dallo split in capitoli.

Modellazione (ADR-0007 adattato all'atto modificativo: nessun punto del
perimetro non coperto, nessuno coperto due volte):
- Unita' di copertura: il punto numerato dell'atto modificativo, non l'articolo
  del regolamento modificato. Tre item di indice e tre righe, mappatura 1:1:
  "art. 1, punto 1" (sostituzione dei punti 1 e 2 dell'art. 2 di Fonte 29),
  "art. 1, punto 2" (sostituzione integrale dell'art. 3 di Fonte 29), "art. 1,
  punto 3" (inserimento del nuovo art. 20 bis nel capo IV di Fonte 29). Il testo
  sostitutivo di un intero articolo (punto 2) resta dentro l'unica riga di quel
  punto, con i suoi quattro paragrafi, le lettere e le note: l'articolo nuovo
  introdotto e' descritto nel `testo` della riga, non indicizzato come articolo
  autonomo della Fonte 30.
- Paratesto -> nessun nodo e nessun item di indice: l'epigrafe ("Gazzetta
  ufficiale dell'Unione europea ... 19.12.2024"), il titolo dell'atto, la
  formula "(Testo rilevante ai fini del SEE)", il preambolo (visti, "LA
  COMMISSIONE EUROPEA,", considerando 1-14), la formula "HA ADOTTATO IL PRESENTE
  REGOLAMENTO:", la firma ("Fatto a Bruxelles, il 18 dicembre 2024 / Per la
  Commissione / La presidente / Ursula VON DER LEYEN"), le note a pie' di pagina
  (1)-(6) alle citazioni degli atti e la riga finale ELI/ISSN non ricadono in
  questa porzione (il manifest la fa partire dall'intestazione "Articolo 1") e
  non producono nodi in questo modulo.
- L'art. 1 dell'atto modificativo non ha rubrica: il testo ufficiale premette
  solo "Articolo 1" al chapeau "Il regolamento di esecuzione (UE) 2024/482 è
  così modificato:", quindi non c'e' alcuna rubrica da includere.
- Chapeau dell'articolo: la frase "Il regolamento di esecuzione (UE) 2024/482 è
  così modificato:" non ha precetto autonomo (introduce l'enumerazione dei
  punti) ne' un item di indice proprio: resta, insieme all'intestazione
  "Articolo 1", all'inizio del `testo_integrale` della prima riga del capitolo
  ("art. 1, punto 1"), dove il testo ufficiale li precede immediatamente (stessa
  convenzione della riga "art. 2" di Fonte 29 cap01, che tiene il chapeau "Ai
  fini del presente regolamento si applicano le definizioni seguenti:" dentro la
  riga delle definizioni).
- "art. 1, punto 1" -> UN SOLO nodo Principio, tipo "definitorio". Il punto
  sostituisce i punti 1 e 2 dell'art. 2 di Fonte 29, cioe' le definizioni di
  "criteri comuni" e "metodologia comune di valutazione": il contenuto
  sostitutivo e' interamente definitorio (nessun soggetto, nessun comportamento
  imposto), ed e' lo stesso tipo del nodo "art. 2" di Fonte 29 che la fase 6
  colleghera' a questa riga. I due punti sostituiti formano un unico nodo (non
  due) perche' l'unita' di copertura e' il punto dell'atto modificativo: la
  numerazione interna alla citazione ("1)" e "2)") resta nel `testo_integrale`.
  Dubbio dichiarato: chi leggesse la riga come "disposizione che dispone una
  sostituzione" (un effetto giuridico sul testo di un altro atto, non una
  definizione) sceglierebbe Principio tipo "altro"; la scelta fatta privilegia la
  natura del contenuto sostitutivo, coerente con il trattamento delle definizioni
  in tutto il censimento.
- "art. 1, punto 2" -> UN SOLO nodo Principio, tipo "altro". Il punto sostituisce
  integralmente l'art. 3 di Fonte 29 con un nuovo articolo "Norme di valutazione"
  di quattro paragrafi: il §1 designa in forma impersonale le norme applicabili
  ("Alle valutazioni effettuate nell'ambito del sistema EUCC si applicano le
  norme seguenti: ... a) i criteri comuni; b) la metodologia comune di
  valutazione."), i §2, §3 e §4 disciplinano in forma permissiva ("può essere
  rilasciato ... un certificato che applica ...") il regime transitorio fino al
  31 dicembre 2027. Nessun soggetto e' nominato e nessun comportamento e'
  imposto: tipo "altro" e non "scopo/ambito di applicazione" (la disposizione non
  delimita l'ambito del regolamento). E' la stessa classificazione del nodo "art.
  3" di Fonte 29 che questa riga sostituisce (Principio "altro", con il dubbio
  Principio/Obbligo dichiarato nel cap01 di quella Fonte) e la stessa scelta
  fatta per le disposizioni permissive gia' censite (art. 1 §2 del Reg.
  2025/2532). Dubbio dichiarato: leggendo la facolta' di rilascio del certificato
  transitorio come diritto esercitabile nei confronti dell'organismo di
  certificazione, i §2-§4 sarebbero Obblighi "procedurali"; la riga e' una sola e
  il §1 (designazione delle norme) ne e' il nucleo, quindi la classificazione
  unitaria e' Principio "altro".
- "art. 1, punto 3" -> UN SOLO nodo Obbligo, tipo "procedurale", senza
  `soggetti`. Il punto inserisce nel capo IV di Fonte 29 il nuovo art. 20 bis,
  che prescrive come l'accreditamento degli organismi di valutazione della
  conformita' debba tenere conto della specificazione dei requisiti per
  l'accreditamento degli organismi di certificazione e delle ITSEF di cui ai
  documenti sullo stato dell'arte applicabili figuranti all'allegato I, punto 2:
  e' una prescrizione sul contenuto della procedura di accreditamento, non la
  mera designazione di documenti (che in questo censimento sono Principi "altro":
  le due righe dell'allegato I di Fonte 29 cap09), quindi Obbligo e non
  Principio; tipo "procedurale" perche' governa lo svolgimento
  dell'accreditamento (l'alternativa "organizzativo" e' sostenibile e resta come
  dubbio dichiarato). Nessun `soggetti`: il testo non nomina il soggetto tenuto
  (il soggetto grammaticale e' "L'accreditamento") e l'organismo nazionale di
  accreditamento che lo esegue non ha una categoria nell'insieme
  `categorie_soggetto` (QTSP/gestore, Utente/titolare, Terza parte, Terzi
  affidanti/pubblico): assegnare "Terza parte" sarebbe un'inferenza, e la regola
  del batch vieta di forzare categorie di soggetto non nominate nel testo (stessa
  scelta delle righe "art. 6" e "art. 17 §4" di Fonte 29, prive di `soggetti`).
- `testo_integrale`: verbatim e integrale per ciascun punto, ricucito dalle righe
  spezzate dalla conversione XHTML -> testo. Le lettere isolate su riga propria
  sono riunite al testo che seguono ("a) i criteri comuni;"), ogni
  comma/lettera/paragrafo resta in un blocco separato da riga vuota nell'ordine
  del testo ufficiale, e la virgoletta caporale « che il testo ufficiale isola su
  riga propria davanti all'intestazione dell'articolo sostitutivo e' mantenuta
  dov'e': su riga propria, subito prima di "Articolo 3" ("... è sostituito dal
  seguente:", riga vuota, "«" e a capo "Articolo 3", senza riga vuota fra i
  due come nel testo ufficiale). Il testo e' riportato com'e', compreso l'errore tipografico del
  testo ufficiale italiano alla fine del punto 1 ("IT Security”;»;", con le
  virgolette doppie curve invertite: non corretto, si censisce il testo
  pubblicato) e compresa la doppia numerazione dei punti sostituiti (il "1)" e il
  "2)" interni alla citazione del punto 1 non vanno confusi con i numeri dei
  punti dell'art. 1 dell'atto modificativo). Nessun marcatore di elisione
  (vincolo `verifica_completezza_testo_integrale`, ADR-0010). `testo` e' invece
  la sintesi compressa (1-3 frasi) di ogni riga.
- Note a pie' di pagina interne alla citazione: le tre note (*1), (*2) e (*3)
  del punto 2, i cui richiami compaiono nel §4 dell'articolo sostitutivo, fanno
  parte del testo sostitutivo citato dall'atto modificativo e restano
  integralmente nel `testo_integrale` di "art. 1, punto 2"; non producono un nodo
  proprio in questo modulo (sono corredo identificativo degli atti citati -
  regolamento di esecuzione (UE) 2016/799, regolamento (UE) n. 910/2014,
  decisione di esecuzione (UE) 2016/650 - e non disposizioni dell'atto
  modificativo). In Fonte 29 cap01 non esistono: il testo previgente dell'art. 3
  non le aveva.
- `condizione_applicabilita` non valorizzata: la condizione del §4 dell'articolo
  sostitutivo ("a condizione che l'uso di tale profilo di protezione sia
  richiesto a norma del regolamento di esecuzione (UE) 2016/799 ..., del
  regolamento (UE) n. 910/2014 ... o della decisione di esecuzione (UE) 2016/650
  ...") e i limiti temporali "Fino al 31 dicembre 2027" dei §2 e §3 valgono per
  singoli paragrafi, non per l'intero nodo, che accorpa i quattro paragrafi del
  punto: restano verbatim nel `testo_integrale` e sono nominati nella sintesi
  `testo`, ma non diventano un attributo di nodo che li estenderebbe all'intera
  riga. Nessuna riga valorizza `severita` o `sanzioni`: l'atto non gradua i
  requisiti ne' prevede sanzioni proprie. `stato` = "vigente" per tutte e tre le
  righe: l'atto modificativo e' in vigore e il termine del 31 dicembre 2027 e' un
  limite interno al testo sostitutivo, non lo stato del nodo. Nessun
  `oggetti_giuridici` valorizzato: fra i valori censiti non ce n'e' uno che
  corrisponda a "criteri comuni", "metodologia comune di valutazione",
  "certificato EUCC" o "accreditamento", e la voce generica "altro" non e' stata
  forzata (stesso criterio di Fonte 29 cap01 e cap09).
- RELAZIONI = []: le tre righe di questo capitolo non si citano a vicenda con un
  rinvio letterale. I soli collegamenti testuali presenti sono i rinvii al
  regolamento modificato dentro ciascun punto ("all'articolo 2", "l'articolo 3 è
  sostituito dal seguente", "al capo IV è inserito il seguente articolo 20 bis")
  e il rinvio del nuovo art. 20 bis all'"allegato I, punto 2": attraversano tutti
  il confine di capitolo o di Fonte e appartengono alla fase 6 (sotto). Non e'
  stata dichiarata nemmeno una relazione "definisce" da "art. 1, punto 1" verso
  "art. 1, punto 2" (le lettere a) e b) del nuovo art. 3 usano i termini "criteri
  comuni" e "metodologia comune di valutazione" definiti dal punto 1): sarebbe
  una relazione inferita per uso di un termine, non una citazione letterale, e
  Fonte 29 cap01 ha scartato la stessa ipotesi sulle proprie definizioni.
- Rinvii demandati alla fase 6 (nessuna relazione dichiarata qui; accanto a ogni
  rinvio e' indicato il `riferimento` con cui il nodo bersaglio e' dichiarato nel
  modulo che lo contiene, per evitare KeyError in fase 6):
  * "art. 1, punto 1" -> Fonte 29 (`reg_ue_2024_482`), riga "art. 2" del cap01
    (Principio "definitorio"). Intervento: MODIFICA parziale dell'art. 2 - il
    punto sostituisce integralmente il testo dei punti 1 e 2 (definizioni di
    "criteri comuni" e "metodologia comune di valutazione"), mentre i punti 3-15
    restano invariati; il nodo "art. 2" di Fonte 29 resta quindi pertinente e il
    tipo di relazione appropriato e' "modifica", non "sostituisce". Il bersaglio
    e' un nodo unico per tutte e 15 le definizioni: gli item di indice interessati
    di Fonte 29 sono "art. 2, punto 1" e "art. 2, punto 2" del suo cap01.
  * "art. 1, punto 2" -> Fonte 29, riga "art. 3" del cap01 (Principio "altro").
    Intervento: SOSTITUZIONE integrale dell'art. 3 (il testo previgente, "Alle
    valutazioni effettuate nell'ambito del sistema EUCC si applicano le norme
    seguenti: (a) i criteri comuni; (b) la metodologia comune di valutazione.", e'
    interamente sostituito dal nuovo articolo di quattro paragrafi), quindi tipo
    di relazione "sostituisce".
  * "art. 1, punto 3" -> Fonte 29, capo IV "Organismi di valutazione della
    conformita'" (artt. 21-24, cap04 di Fonte 29). Intervento: INSERIMENTO di un
    articolo nuovo (art. 20 bis), per il quale in Fonte 29 non esiste un nodo
    corrispondente: la fase 6 non ha quindi un bersaglio diretto verso cui
    costruire la relazione. Se vorra' rappresentare l'inserimento, le opzioni sono
    collegare la riga come "modifica" ai nodi del capo IV (artt. 21-24) o
    lasciarla senza arco in attesa di un nodo per l'art. 20 bis nel testo
    consolidato di Fonte 29: decisione che non spetta a questo modulo.
  * "art. 1, punto 3" -> "allegato I, punto 2" citato dal nuovo art. 20 bis.
    Bersaglio: il nuovo allegato I introdotto da questa stessa Fonte 30 con
    l'art. 1, punto 7 (cap02 del manifest) e pubblicato nell'ALLEGATO I (cap04):
    il `riferimento` del nodo bersaglio sara' quello dichiarato dal modulo
    cap04.py (per Fonte 29 cap09 la convenzione in uso e' "allegato I, punto 2"),
    da verificare in fase 6 prima di costruire l'arco. Intervento: RINVIO, non
    modifica - l'art. 20 bis richiama i documenti di accreditamento elencati al
    punto 2 dell'allegato I; relazione candidata "richiama".
  * Nessun'altra relazione cross-fonte: gli atti e i documenti citati dentro il
    testo sostitutivo (regolamento di esecuzione (UE) 2016/799, regolamento (UE)
    n. 910/2014, decisione di esecuzione (UE) 2016/650, norme ISO/IEC 15408 e
    18045, documenti "Common Criteria" e "Common Methodology" del CCRA,
    regolamento (UE) 2019/881 e regolamento (CE) n. 765/2008 nelle note) non sono
    Fonti di questo censimento o non sono collegate a questo capitolo: restano
    verbatim nel `testo_integrale` e non generano archi in questo modulo.

Copertura: 3 item di indice, 3 righe (1 Obbligo + 2 Principi), 0 relazioni
interne.

Dubbi di classificazione rimasti aperti (dichiarati, non risolti in modo
univoco dal testo): (1) tipo_principio di "art. 1, punto 1", "definitorio" (qui
scelto, per la natura del contenuto sostitutivo) oppure "altro" (se si guarda
all'atto del disporre la sostituzione di norme di un altro regolamento); (2)
tipo_principio di "art. 1, punto 2", "altro" (qui scelto, con il §1 designazione
di norme) oppure Obbligo "procedurale" se si legge la facolta' di rilascio dei
certificati transitori dei §2-§4 come posizione giuridica attiva esercitabile
verso l'organismo di certificazione; (3) "art. 1, punto 3", Obbligo
"procedurale" (qui scelto) oppure "organizzativo", e in ogni caso senza
`soggetti` perche' l'organismo nazionale di accreditamento non esiste fra le
categorie di soggetto censite e il testo non lo nomina.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 1, punto 3",
        "testo": "Nel regolamento di esecuzione (UE) 2024/482 è inserito, nel capo IV, il nuovo articolo 20 bis: l'accreditamento degli organismi di valutazione della conformità tiene conto della specificazione dei requisiti per l'accreditamento degli organismi di certificazione e delle ITSEF di cui ai documenti sullo stato dell'arte applicabili figuranti all'allegato I, punto 2.",
        "testo_integrale": "3) al capo IV è inserito il seguente articolo 20 bis:\n\n«\nArticolo 20 bis\n\nSpecificazione dei requisiti per l'accreditamento degli organismi di valutazione della conformità\n\nL'accreditamento degli organismi di valutazione della conformità tiene conto della specificazione dei requisiti per l'accreditamento degli organismi di certificazione e delle ITSEF di cui ai documenti sullo stato dell'arte applicabili figuranti all'allegato I, punto 2.»;",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 1, punto 1",
        "testo": "Nell'art. 2 del regolamento di esecuzione (UE) 2024/482 sono sostituiti i punti 1 e 2: i «criteri comuni» sono quelli definiti nelle norme ISO/IEC 15408-1:2022, ISO/IEC 15408-2:2022, ISO/IEC 15408-3:2022, ISO/IEC 15408-4:2022 o ISO/IEC 15408-5:2022, oppure nella norma «Common Criteria for Information Technology Security Evaluation», versione CC:2022, parti da 1 a 5, pubblicata dai partecipanti all'accordo CCRA; la «metodologia comune di valutazione» è quella definita nella norma ISO/IEC 18045:2022 o nella norma «Common Methodology for Information Technology Security Evaluation», versione CEM:2022, pubblicata dai partecipanti allo stesso accordo.",
        "testo_integrale": "Articolo 1\n\nIl regolamento di esecuzione (UE) 2024/482 è così modificato:\n\n1) all'articolo 2, i punti 1 e 2 sono sostituiti dai seguenti:\n\n«1) «criteri comuni»: i criteri comuni per la valutazione della sicurezza delle tecnologie dell'informazione quali definiti nelle norme ISO/IEC 15408-1:2022, ISO/IEC 15408-2:2022, ISO/IEC 15408-3:2022, ISO/IEC 15408-4:2022 o ISO/IEC 15408-5:2022, o quali definiti nella norma «Common Criteria for Information Technology Security Evaluation», versione CC:2022, parti da 1 a 5, pubblicata dai partecipanti all'accordo «Arrangement on the Recognition of Common Criteria Certificates in the field of IT Security»;\n\n2) «metodologia comune di valutazione»: la metodologia comune per la valutazione della sicurezza delle tecnologie dell'informazione quale definita nella norma ISO/IEC 18045:2022, o nella norma «Common Methodology for Information Technology Security Evaluation», versione CEM:2022, pubblicata dai partecipanti all'accordo «Arrangement on the Recognition of Common Criteria Certificates in the field of IT Security”;»;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 1, punto 2",
        "testo": "L'art. 3 del regolamento di esecuzione (UE) 2024/482 è sostituito integralmente dal nuovo art. 3 «Norme di valutazione»: alle valutazioni effettuate nell'ambito del sistema EUCC si applicano i criteri comuni e la metodologia comune di valutazione (§1); fino al 31 dicembre 2027 può essere rilasciato nell'ambito dell'EUCC un certificato che applica le norme precedenti (ISO/IEC 15408-1:2009, 15408-2:2008 o 15408-3:2008, «Common Criteria» versione 3.1 revisione 5, ISO/IEC 18045:2008, «Common Methodology» revisione 5 versione 3.1) (§2) oppure un certificato che applica le norme del §1 e dichiari la conformità a un profilo di protezione che ha applicato le norme del §2 (§3); può inoltre essere rilasciato un certificato che dichiari la conformità a un profilo di protezione che ha applicato il «Common Criteria» o il «Common Methodology» versione 3.1, revisioni da 1 a 4, a condizione che l'uso di tale profilo di protezione sia richiesto dal regolamento di esecuzione (UE) 2016/799, dal regolamento (UE) n. 910/2014 o dalla decisione di esecuzione (UE) 2016/650 (§4).",
        "testo_integrale": "2) l'articolo 3 è sostituito dal seguente:\n\n«\nArticolo 3\n\nNorme di valutazione\n\n1. Alle valutazioni effettuate nell'ambito del sistema EUCC si applicano le norme seguenti:\n\na) i criteri comuni;\n\nb) la metodologia comune di valutazione.\n\n2. Fino al 31 dicembre 2027 può essere rilasciato nell'ambito del sistema EUCC un certificato che applica una delle norme seguenti:\n\na) ISO/IEC 15408-1:2009, ISO/IEC 15408-2:2008 o ISO/IEC 15408-3:2008;\n\nb) «Common Criteria for Information Technology Security Evaluation», versione 3.1, revisione 5, pubblicata dai partecipanti all'accordo «Arrangement on the Recognition of Common Criteria Certificates in the field of IT Security»;\n\nc) ISO/IEC 18045:2008;\n\nd) «Common Methodology for Information Technology Security Evaluation», revisione 5, versione 3.1, pubblicata dai partecipanti all'accordo «Arrangement on the Recognition of Common Criteria Certificates in the field of IT Security».\n\n3. Fino al 31 dicembre 2027 può essere rilasciato nell'ambito del sistema EUCC un certificato che applica le norme di cui al paragrafo 1 e che dichiari la conformità a un profilo di protezione che ha applicato le norme di cui al paragrafo 2.\n\n4. Può essere rilasciato nell'ambito del sistema EUCC anche un certificato che applica le norme di cui al paragrafo 1 e che dichiari la conformità a un profilo di protezione che ha applicato una delle due norme seguenti, a condizione che l'uso di tale profilo di protezione sia richiesto a norma del regolamento di esecuzione (UE) 2016/799 della Commissione (*1), del regolamento (UE) n. 910/2014 del Parlamento europeo e del Consiglio (*2) o della decisione di esecuzione (UE) 2016/650 della Commissione (*3):\n\na) «Common Criteria for Information Technology Security Evaluation», versione 3.1, revisioni da 1 a 4, pubblicata dai partecipanti all'accordo «Arrangement on the Recognition of Common Criteria Certificates in the field of IT Security»;\n\nb) «Common Methodology for Information Technology Security Evaluation», versione 3.1, revisioni da 1 a 4, pubblicata dai partecipanti all'accordo «Arrangement on the Recognition of Common Criteria Certificates in the field of IT Security».\n\n(*1) Regolamento di esecuzione (UE) 2016/799 della Commissione, del 18 marzo 2016, che applica il regolamento (UE) n. 165/2014 del Parlamento europeo e del Consiglio recante le prescrizioni per la costruzione, il collaudo, il montaggio, il funzionamento e la riparazione dei tachigrafi e dei loro componenti (GU L 139 del 26.5.2016, pag. 1, ELI: http://data.europa.eu/eli/reg_impl/2016/799/oj).\"\n\n(*2) Regolamento (UE) n. 910/2014 del Parlamento europeo e del Consiglio, del 23 luglio 2014, in materia di identificazione elettronica e servizi fiduciari per le transazioni elettroniche nel mercato interno e che abroga la direttiva 1999/93/CE (GU L 257 del 28.8.2014, pag. 73, ELI: http://data.europa.eu/eli/reg/2014/910/oj).\"\n\n(*3) Decisione di esecuzione (UE) 2016/650 della Commissione, del 25 aprile 2016, che stabilisce norme per la valutazione di sicurezza dei dispositivi per la creazione di una firma e di un sigillo qualificati a norma dell'articolo 30, paragrafo 3, e dell'articolo 39, paragrafo 2, del regolamento (UE) n. 910/2014 del Parlamento europeo e del Consiglio in materia di identificazione elettronica e servizi fiduciari per le transazioni elettroniche nel mercato interno (GU L 109 del 26.4.2016, pag. 40, ELI: http://data.europa.eu/eli/dec_impl/2016/650/oj).»;\"",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 1, punto 1",
    "art. 1, punto 2",
    "art. 1, punto 3",
]

MAPPATURA_LOCALE = {
    "art. 1, punto 1": ["art. 1, punto 1"],
    "art. 1, punto 2": ["art. 1, punto 2"],
    "art. 1, punto 3": ["art. 1, punto 3"],
}

RELAZIONI = []
