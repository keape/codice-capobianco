"""Regolamento di esecuzione (UE) 2024/482 della Commissione, del 31 gennaio
2024, recante modalita' di applicazione del regolamento (UE) 2019/881 per
quanto riguarda l'adozione del sistema europeo di certificazione della
cibersicurezza basato sui criteri comuni (EUCC). Fonte 29
(`reg_ue_2024_482`), capitolo 4 di 14 (vedi
app/.source_cache/reg_ue_2024_482/manifest.json): Capo IV - Organismi di
valutazione della conformita' (articoli 21-24). Gli artt. 1-20 (capi I-III) e
25-50 (capi V-XI) e gli allegati I-IX sono nei capitoli 1-3 e 5-14, assegnati
ad altri moduli: nessuno di quei file e' toccato qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_482/cap04.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R0482, lingua italiana;
URL risolto
http://publications.europa.eu/resource/cellar/687c0d05-c580-11ee-95d9-01aa75ed71a1.0014.03/DOC_1,
XHTML della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 135.367
caratteri di testo, sha256 del raw.txt
b46d08cab6d63b2c190ae767042c07c1fc324955c22ef491eb314556b28ca5b8 - dettagli
completi in app/.source_cache/reg_ue_2024_482/provenance.json). Il presente
capitolo e' preceduto dal preambolo (considerando 1-33) e dai capi I-III, non
inclusi in questa porzione; lo segue il Capo V (art. 25). Il considerando 32
precisa che i requisiti del capo IV non richiedono un periodo di transizione e
si applicano dall'entrata in vigore del regolamento: tutte le righe di questo
modulo sono percio' `stato` "vigente".

Modellazione (ADR-0007, nessun discrimine di rilevanza):
- Paratesto -> nessun nodo: l'intestazione di capitolo "CAPO IV / ORGANISMI DI
  VALUTAZIONE DELLA CONFORMITA'" e le intestazioni dei quattro articoli
  ("Articolo N" + rubrica) non sono articoli, commi o lettere, ma struttura
  dell'atto. Le rubriche restano coperte perche' incluse nel `testo_integrale`
  della prima riga di ogni articolo ("Articolo 21 / Requisiti specifici o
  supplementari per un organismo di certificazione" in "art. 21 §1", e cosi'
  per gli artt. 22, 23 e 24). In questa porzione non compaiono epigrafe,
  firma, riga ELI ne' nota a pie' di pagina (in questa porzione non cade
  nessuno dei richiami numerici fra parentesi del regolamento, che stanno
  tutti nel preambolo e negli allegati), quindi non producono nodi ne' item di
  indice.
- Unita' di copertura: un comma = una riga, con le lettere e i punti numerati
  di ciascun comma indicizzati separatamente e mappati tutti sulla riga del
  proprio comma quando non hanno precetto autonomo (chapeau + elenco
  specificativo: stesso trattamento delle lettere di art. 5 §1 del Reg.
  2024/2979 e delle liste definitorie di eIDAS art. 3). Nessun comma di questo
  capitolo ha lettere con precetto autonomo: sono tutte condizioni, contenuti
  informativi o basi giuridiche rette dal chapeau. Righe: art. 21 -> 5
  Obblighi (§1, §2, §3, §4, §5); art. 22 -> 6 Obblighi (§1, §2, §3, §4, §5,
  §6); art. 23 -> 5 Obblighi (§1, §2, §3, §4, §5); art. 24 -> 1 Obbligo
  (articolo senza commi numerati). Totale 17 Obblighi, 0 Principi, 17 righe.
- Nessun Principio in questo capitolo: sono disposizioni che attribuiscono
  poteri/facolta' solo come elemento interno di un comma che prescrive un
  comportamento (art. 21 §2 secondo capoverso "puo' riutilizzare elementi di
  prova"; art. 21 §4 "puo' essere rinnovata su richiesta"; art. 22 §3, §5
  idem; art. 23 §5 ultimo periodo "puo' presentare a quest'ultima una
  richiesta"). Nessuno di questi capoversi ha struttura autonoma (non e' un
  comma numerato ne' una lettera: e' la prosecuzione dello stesso comma), quindi
  non e' stato aperto un secondo nodo, coerentemente con la granularita' di
  comma seguita in questo capitolo; la facolta' resta integralmente nel
  `testo_integrale` della riga e citata nella sintesi.
- Obbligo vs. Principio: art. 21 §1 e art. 22 §1 sono Obblighi, non Principi.
  Il comma e' costruito come condizione di autorizzazione ("e' autorizzato ...
  se ... dimostra" / "dimostra di rispettare tutte le condizioni seguenti"), ma
  il suo contenuto e' l'insieme dei requisiti che l'organismo di certificazione
  o l'ITSEF deve soddisfare e provare (competenze, collaborazione, misure di
  protezione delle informazioni): prescrizione di comportamento a soggetto
  identificabile, non dichiarazione di effetto giuridico senza obbligato.
- Distinzione ITSEF / organismo di certificazione (nota del capitolo): tenuta
  riga per riga, non solo nello `stesso` campo soggetti. Art. 21 = organismo di
  certificazione (autorizzato a rilasciare certificati EUCC di livello
  "elevato"); art. 22 = ITSEF (autorizzata a effettuare la valutazione dei
  prodotti TIC per il livello "elevato"); art. 23 = notifica degli organismi di
  certificazione; art. 24 = estensione della notifica alle ITSEF. I commi
  speculari dei due articoli (art. 21 §2/art. 22 §3 riutilizzo elementi di
  prova; art. 21 §3/art. 22 §4 relazione di autorizzazione; art. 21 §4/art. 22
  §5 ambito, validita' e rinnovo dell'autorizzazione; art. 21 §5/art. 22 §6
  revoca) restano righe distinte e nessuna relazione e' dichiarata tra loro:
  il tipo "si sovrappone a" di CONTEXT.md e' definito per lo stesso contenuto
  sostanziale espresso in fonti diverse, mentre qui la duplicazione e'
  strutturale all'interno della stessa fonte (due destinatari diversi).
- Soggetto obbligato: "Terza parte" (ruolo "obbligato") per tutte le righe in
  cui il precetto e' indirizzato all'autorita' nazionale di certificazione
  della cibersicurezza, agli organismi di certificazione o alle ITSEF. Non e'
  un QTSP/gestore: la categoria e' quella dei terzi con ruolo identificabile
  (organismo di valutazione della conformita', laboratorio accreditato,
  autorita' nazionale competente), come stabilito dai criteri di modellazione
  degli atti di esecuzione in docs/plan-import-lotto-eidas2-standard.md §5
  ("distinzione gia' in uso fra QTSP/gestore ... e Terza parte (organismo di
  valutazione della conformita', laboratorio accreditato, autorita' nazionale
  competente)") e gia' applicata in
  app/seed_data/reg_ue_2025_1569/cap03.py. La Commissione e l'ENISA, meri
  destinatari dei flussi informativi degli artt. 23-24, sono registrate come
  "Terza parte" con ruolo "destinatario". Nessuna riga valorizza una categoria
  di soggetto diversa da "Terza parte".
- tipo_obbligo: "organizzativo" per art. 21 §1 e art. 22 §1 (requisiti di
  competenza, di collaborazione e di organizzazione dell'organismo che chiede
  l'autorizzazione; art. 21 §1(c) e art. 22 §1(c) contengono anche misure
  tecniche e operative di protezione delle informazioni riservate, ma il
  requisito dominante del comma resta la capacita' organizzativa dell'organismo,
  non un requisito tecnico sul prodotto o sul sistema); "procedurale" per
  art. 21 §2-§5 e art. 22 §2-§6 (valutazione dell'autorita', relazione di
  autorizzazione, ambito/validita'/rinnovo, revoca) e per art. 23 §5 (esame
  delle modifiche dello stato dell'accreditamento e informazione alla
  Commissione); "informativo/trasparenza" per art. 23 §1-§4 e art. 24 (flussi
  informativi verso la Commissione e l'ENISA e contenuto minimo della
  notifica).
- Revoca dell'autorizzazione (art. 21 §5, art. 22 §6) -> "procedurale" e non
  "sanzionatorio": e' un provvedimento di ritiro dell'autorizzazione
  conseguente al venir meno delle condizioni, senza sanzione pecuniaria ne'
  procedimento sanzionatorio; stesso trattamento riservato dal censimento alla
  revoca dei certificati qualificati in app/seed_data/cad/cap04.py art. 36.
  Dubbio di classificazione dichiarato in chiusura (vedi sotto).
- condizione_applicabilita valorizzata solo dove il testo subordina il precetto
  a un fatto esplicito esterno al comportamento prescritto: art. 21 §5 e
  art. 22 §6 (venir meno delle condizioni di autorizzazione) e art. 23 §5
  (revoca dell'accreditamento o dell'autorizzazione). Non valorizzata per
  art. 21 §1, art. 21 §4, art. 22 §1, art. 22 §5: li' il "se"/"a condizione
  che" e' parte integrante della condizione di autorizzazione o di rinnovo ed
  e' gia' nella sintesi `testo`. Nessuna riga valorizza `severita` o
  `sanzioni`: il regolamento non gradua i requisiti di questo capo ne' prevede
  sanzioni proprie (le misure di monitoraggio e non conformita' stanno negli
  artt. 25-31, cap05).
- Fedelta' al testo ufficiale: le lettere sono riportate nella forma del testo
  ufficiale ("(a)", "(1)"), non normalizzate; i refusi del testo italiano della
  Gazzetta ufficiale sono conservati senza correzione (ADR-0010), fra cui i
  segni di punteggiatura incoerenti dell'art. 23 §3 ("il paese di
  registrazione dell'organismo di certificazione," con virgola al posto del
  punto e virgola; "la data dell'autorizzazione:" con i due punti al posto del
  punto e virgola) e il minuscolo di art. 21 §2 ("concesse a norma:") e di
  art. 23 §5 ("e puo' presentare"). I decreti di esecuzione non sono ricostruiti
  a memoria.
- Escluso da questo modulo: i rinvii ad articoli di questa stessa fonte fuori
  dal capitolo (art. 3 in art. 22 §1(b)(1), art. 43 in art. 21 §1(c) e art. 22
  §1(c), allegato I in art. 22 §1(b)(2), art. 49 in art. 21 §2(c) e art. 22
  §3(c)), che appartengono ai capitoli 1, 7 e 9; i rinvii al regolamento (UE)
  2019/881 (art. 49 del considerando normativo e del art. 21 §2(b) e art. 22
  §3(b), art. 59 §3(d) in art. 21 §3 e art. 22 §4, art. 60 §1 in art. 21 §1 e
  art. 22 §1, art. 61 §4 in art. 23 §5, allegato dello stesso regolamento in
  art. 21 §1 e art. 22 §1); e il rinvio implicito dell'art. 23 §2 alla
  "decisione di autorizzazione" di cui agli artt. 21-22 (non e' una citazione
  letterale, quindi non produce relazione "textual").

Rinvii demandati alla fase 6 (nessuna relazione dichiarata in questo modulo):
- art. 3 del presente regolamento (norme di riferimento) <- art. 22 §1(b)(1);
- allegato I del presente regolamento (documenti sullo stato dell'arte) <-
  art. 22 §1(b)(2);
- art. 43 del presente regolamento (protezione delle informazioni) <-
  art. 21 §1(c) e art. 22 §1(c);
- art. 49 del presente regolamento (sistemi nazionali di certificazione) <-
  art. 21 §2(c) e art. 22 §3(c);
- regolamento (UE) 2019/881: art. 49 <-> art. 21 §2(b), art. 22 §3(b); art. 59
  §3(d) <-> art. 21 §3, art. 22 §4; art. 60 §1 e allegato (accreditamento degli
  organismi di valutazione della conformita') <-> art. 21 §1, art. 22 §1;
  art. 61 §4 <-> art. 23 §5.

Relazioni interne dichiarate (bersagli verificabili su questo file): art. 21
§1 -> art. 22 §1 (citazione letterale "in conformita' dell'articolo 22"); art.
24 -> art. 23 §1, §2, §3, §4, §5 (la citazione e' all'articolo 23 in blocco -
"gli obblighi di notifica ... di cui all'articolo 23" - e viene propagata a
ciascun comma dell'articolo che porta un obbligo di notifica o un suo
corollario).

Dubbi di classificazione lasciati aperti (segnalati, non risolti in autonomia):
- art. 21 §5 e art. 22 §6: classificati "procedurale" (ritiro dell'autorizzazione
  per venir meno delle condizioni). Il tipo "sanzionatorio" sarebbe difendibile
  per analogia con la cancellazione dall'elenco pubblico di CAD art. 32-bis §2
  (classificata "sanzionatorio" in app/seed_data/cad/cap04.py): qui pero' non
  c'e' sanzione pecuniaria ne' procedimento sanzionatorio, solo il venir meno
  del titolo abilitativo.
- art. 21 §1 e art. 22 §1: classificati Obbligo perche' il contenuto e' la
  serie di condizioni che l'organismo/ITSEF deve soddisfare e dimostrare; la
  lettura alternativa (Principio "altro" come mero effetto giuridico
  dell'autorizzazione condizionata) non e' stata seguita perche' il soggetto
  obbligato e il comportamento richiesto sono entrambi espliciti.
- I capoversi di facolta' (art. 21 §2 secondo capoverso, art. 21 §4, art. 22 §3,
  art. 22 §5, art. 23 §5 ultimo periodo) non sono stati aperti come nodi
  Principio separati: non hanno numerazione propria nel testo ufficiale e
  restano coperti dalla riga del comma che li contiene. Se la convenzione del
  censimento volesse un nodo per ciascuna facolta', andrebbero introdotti
  riferimenti di capoverso non previsti dalla convenzione dei riferimenti.

Copertura: 44 item di indice, 17 righe (17 Obblighi + 0 Principi), 6
relazioni interne.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 21 §1",
        "testo": "Un organismo di certificazione è autorizzato dall'autorità nazionale di certificazione della cibersicurezza a rilasciare certificati EUCC di livello di affidabilità «elevato» solo se, oltre a soddisfare i requisiti di cui all'articolo 60, paragrafo 1, e all'allegato del regolamento (UE) 2019/881 per quanto riguarda l'accreditamento degli organismi di valutazione della conformità, dimostra: (a) di possedere le conoscenze e le competenze necessarie per la decisione relativa alla certificazione di livello «elevato»; (b) di svolgere le proprie attività di certificazione in collaborazione con un'ITSEF autorizzata in conformità dell'articolo 22; (c) di possedere le competenze richieste e di aver adottato misure tecniche e operative adeguate per proteggere efficacemente le informazioni riservate e sensibili per il livello «elevato», oltre a soddisfare i requisiti di cui all'articolo 43.",
        "testo_integrale": "Articolo 21\n\nRequisiti specifici o supplementari per un organismo di certificazione\n\n1. Un organismo di certificazione è autorizzato dall'autorità nazionale di certificazione della cibersicurezza a rilasciare certificati EUCC di livello di affidabilità «elevato» se, oltre a soddisfare i requisiti di cui all'articolo 60, paragrafo 1, e all'allegato del regolamento (UE) 2019/881 per quanto riguarda l'accreditamento degli organismi di valutazione della conformità, dimostra:\n\n(a) di possedere le conoscenze e le competenze necessarie per la decisione relativa alla certificazione del livello di affidabilità «elevato»;\n\n(b) di svolgere le proprie attività di certificazione in collaborazione con un'ITSEF autorizzata in conformità dell'articolo 22; e\n\n(c) di possedere le competenze richieste e di aver adottato misure tecniche e operative adeguate per proteggere efficacemente le informazioni riservate e sensibili per il livello di affidabilità «elevato», oltre a soddisfare i requisiti di cui all'articolo 43.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 21 §2",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza valuta se un organismo di certificazione soddisfa tutti i requisiti del paragrafo 1, con una valutazione che comprende almeno interviste strutturate e un riesame di almeno una certificazione pilota effettuata dall'organismo di certificazione in conformità del regolamento; nella sua valutazione l'autorità può riutilizzare elementi di prova adeguati provenienti da una precedente autorizzazione o da attività analoghe concesse a norma del presente regolamento, di un altro sistema europeo di certificazione della cibersicurezza adottato a norma dell'articolo 49 del regolamento (UE) 2019/881 o di un sistema nazionale di cui all'articolo 49 del presente regolamento.",
        "testo_integrale": "2. L'autorità nazionale di certificazione della cibersicurezza valuta se un organismo di certificazione soddisfa tutti i requisiti di cui al paragrafo 1. Tale valutazione comprende almeno interviste strutturate e un riesame di almeno una certificazione pilota effettuata dall'organismo di certificazione in conformità del presente regolamento.\n\nNella sua valutazione, l'autorità nazionale di certificazione della cibersicurezza può riutilizzare elementi di prova adeguati provenienti da una precedente autorizzazione o da attività analoghe concesse a norma:\n\n(a) del presente regolamento;\n\n(b) di un altro sistema europeo di certificazione della cibersicurezza adottato a norma dell'articolo 49 del regolamento (UE) 2019/881;\n\n(c) di un sistema nazionale di cui all'articolo 49 del presente regolamento.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 21 §3",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza elabora una relazione di autorizzazione soggetta a valutazione inter pares in conformità dell'articolo 59, paragrafo 3, lettera d), del regolamento (UE) 2019/881.",
        "testo_integrale": "3. L'autorità nazionale di certificazione della cibersicurezza elabora una relazione di autorizzazione soggetta a valutazione inter pares in conformità dell'articolo 59, paragrafo 3, lettera d), del regolamento (UE) 2019/881.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 21 §4",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza specifica le categorie di prodotti TIC e i profili di protezione a cui si estende l'autorizzazione; l'autorizzazione è valida per un periodo non superiore alla validità dell'accreditamento e può essere rinnovata su richiesta a condizione che l'organismo di certificazione continui a soddisfare i requisiti dell'articolo, mentre per il rinnovo non sono richieste valutazioni pilota.",
        "testo_integrale": "4. L'autorità nazionale di certificazione della cibersicurezza specifica le categorie di prodotti TIC e i profili di protezione a cui si estende l'autorizzazione. L'autorizzazione è valida per un periodo non superiore alla validità dell'accreditamento. Tale autorizzazione può essere rinnovata su richiesta, a condizione che l'organismo di certificazione continui a soddisfare i requisiti di cui al presente articolo. Per il rinnovo dell'autorizzazione non sono richieste valutazioni pilota.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 21 §5",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza revoca l'autorizzazione dell'organismo di certificazione se quest'ultimo non soddisfa più le condizioni dell'articolo; in caso di revoca, l'organismo di certificazione cessa immediatamente di presentarsi come organismo di certificazione autorizzato.",
        "testo_integrale": "5. L'autorità nazionale di certificazione della cibersicurezza revoca l'autorizzazione dell'organismo di certificazione se quest'ultimo non soddisfa più le condizioni di cui al presente articolo. In caso di revoca dell'autorizzazione, l'organismo di certificazione cessa immediatamente di presentarsi come organismo di certificazione autorizzato.",
        "tipo_obbligo": "sanzionatorio",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo se l'organismo di certificazione non soddisfa più le condizioni di cui all'articolo 21.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 22 §1",
        "testo": "Un'ITSEF è autorizzata dall'autorità nazionale di certificazione della cibersicurezza a effettuare la valutazione dei prodotti TIC soggetti a certificazione con il livello di affidabilità «elevato» solo se, oltre a soddisfare i requisiti di cui all'articolo 60, paragrafo 1, e all'allegato del regolamento (UE) 2019/881 per quanto riguarda l'accreditamento degli organismi di valutazione della conformità, dimostra di rispettare tutte le condizioni seguenti: (a) possesso delle competenze necessarie per determinare la resistenza agli attacchi informatici avanzati commessi da attori con abilità e risorse significative; (b) per quanto riguarda i settori tecnici e i profili di protezione che fanno parte del processo TIC di tali prodotti, possesso delle competenze per determinare metodicamente la resistenza dell'oggetto della valutazione agli attacchi di soggetti qualificati nel suo ambiente operativo, ipotizzando un potenziale di attacco «moderato» o «elevato» come stabilito nelle norme di cui all'articolo 3, e possesso delle competenze tecniche specificate nei documenti sullo stato dell'arte di cui all'allegato I; (c) possesso delle competenze richieste e adozione di misure tecniche e operative adeguate per proteggere efficacemente le informazioni riservate e sensibili per il livello «elevato», oltre al soddisfacimento dei requisiti di cui all'articolo 43.",
        "testo_integrale": "Articolo 22\n\nRequisiti specifici o supplementari per un ITSEF\n\n1. Un'ITSEF è autorizzata dall'autorità nazionale di certificazione della cibersicurezza a effettuare la valutazione dei prodotti TIC soggetti a certificazione con il livello di affidabilità «elevato» se, oltre a soddisfare i requisiti di cui all'articolo 60, paragrafo 1, e all'allegato del regolamento (UE) 2019/881 per quanto riguarda l'accreditamento degli organismi di valutazione della conformità, dimostra di rispettare tutte le condizioni seguenti:\n\n(a) possesso delle competenze necessarie per svolgere le attività di valutazione al fine di determinare la resistenza agli attacchi informatici avanzati commessi da attori che dispongono di abilità e risorse significative;\n\n(b) per quanto riguarda i settori tecnici e i profili di protezione, che fanno parte del processo TIC per tali prodotti TIC:\n\n(1) possesso delle competenze per svolgere le attività di valutazione specifiche necessarie a determinare metodicamente la resistenza di un oggetto della valutazione agli attacchi commessi da soggetti qualificati nel suo ambiente operativo, ipotizzando un potenziale di attacco «moderato» o «elevato», come stabilito nelle norme di cui all'articolo 3;\n\n(2) possesso delle competenze tecniche specificate nei documenti sullo stato dell'arte di cui all'allegato I;\n\n(c) possesso delle competenze richieste e adozione di misure tecniche e operative adeguate per proteggere efficacemente le informazioni riservate e sensibili per il livello di affidabilità «elevato», oltre al soddisfacimento dei requisiti di cui all'articolo 43.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 22 §2",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza valuta se un'ITSEF soddisfa tutti i requisiti del paragrafo 1, con una valutazione che comprende quanto meno interviste strutturate e il riesame di almeno una valutazione pilota effettuata dall'ITSEF in conformità del regolamento.",
        "testo_integrale": "2. L'autorità nazionale di certificazione della cibersicurezza valuta se un'ITSEF soddisfa tutti i requisiti di cui al paragrafo 1. Tale valutazione comprende quanto meno interviste strutturate e un riesame di almeno una valutazione pilota effettuata dall'ITSEF in conformità del presente regolamento.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 22 §3",
        "testo": "Nella sua valutazione l'autorità nazionale di certificazione della cibersicurezza può riutilizzare elementi di prova adeguati provenienti da una precedente autorizzazione o da attività analoghe concesse a norma del presente regolamento, di un altro sistema europeo di certificazione della cibersicurezza adottato a norma dell'articolo 49 del regolamento (UE) 2019/881 o di un sistema nazionale di cui all'articolo 49 del presente regolamento.",
        "testo_integrale": "3. Nella sua valutazione, l'autorità nazionale di certificazione della cibersicurezza può riutilizzare elementi di prova adeguati provenienti da una precedente autorizzazione o da attività analoghe concesse a norma:\n\n(a) del presente regolamento;\n\n(b) di un altro sistema europeo di certificazione della cibersicurezza adottato a norma dell'articolo 49 del regolamento (UE) 2019/881;\n\n(c) di un sistema nazionale di cui all'articolo 49 del presente regolamento.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 22 §4",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza elabora una relazione di autorizzazione soggetta a valutazione inter pares in conformità dell'articolo 59, paragrafo 3, lettera d), del regolamento (UE) 2019/881.",
        "testo_integrale": "4. L'autorità nazionale di certificazione della cibersicurezza elabora una relazione di autorizzazione soggetta a valutazione inter pares in conformità dell'articolo 59, paragrafo 3, lettera d), del regolamento (UE) 2019/881.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 22 §5",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza specifica le categorie di prodotti TIC e i profili di protezione a cui si estende l'autorizzazione; l'autorizzazione è valida per un periodo non superiore alla validità dell'accreditamento e può essere rinnovata su richiesta a condizione che l'ITSEF continui a soddisfare i requisiti dell'articolo, mentre per il rinnovo dell'autorizzazione non devono essere richieste valutazioni pilota.",
        "testo_integrale": "5. L'autorità nazionale di certificazione della cibersicurezza specifica le categorie di prodotti TIC e i profili di protezione a cui si estende l'autorizzazione. L'autorizzazione è valida per un periodo non superiore alla validità dell'accreditamento. Tale autorizzazione può essere rinnovata su richiesta, a condizione che l'ITSEF continui a soddisfare i requisiti di cui al presente articolo. Per il rinnovo dell'autorizzazione non devono essere richieste valutazioni pilota.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 22 §6",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza revoca l'autorizzazione dell'ITSEF se quest'ultima non soddisfa più le condizioni dell'articolo; in caso di revoca dell'autorizzazione, l'ITSEF cessa di presentarsi come un'ITSEF autorizzata.",
        "testo_integrale": "6. L'autorità nazionale di certificazione della cibersicurezza revoca l'autorizzazione dell'ITSEF se quest'ultima non soddisfa più le condizioni di cui al presente articolo. In caso di revoca dell'autorizzazione, l'ITSEF cessa di presentarsi come un'ITSEF autorizzata.",
        "tipo_obbligo": "sanzionatorio",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo se l'ITSEF non soddisfa più le condizioni di cui all'articolo 22.",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 23 §1",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza notifica alla Commissione gli organismi di certificazione presenti sul suo territorio che sono competenti a certificare al livello di affidabilità «sostanziale» in base al loro accreditamento.",
        "testo_integrale": "Articolo 23\n\nNotifica degli organismi di certificazione\n\n1. L'autorità nazionale di certificazione della cibersicurezza notifica alla Commissione gli organismi di certificazione presenti sul suo territorio che sono competenti a certificare al livello di affidabilità «sostanziale» in base al loro accreditamento.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 23 §2",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza notifica alla Commissione gli organismi di certificazione presenti sul suo territorio che sono competenti a certificare al livello di affidabilità «elevato» in base al loro accreditamento e alla decisione di autorizzazione.",
        "testo_integrale": "2. L'autorità nazionale di certificazione della cibersicurezza notifica alla Commissione gli organismi di certificazione presenti sul suo territorio che sono competenti a certificare al livello di affidabilità «elevato» in base al loro accreditamento e alla decisione di autorizzazione.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 23 §3",
        "testo": "All'atto della notifica alla Commissione degli organismi di certificazione, l'autorità nazionale di certificazione della cibersicurezza fornisce almeno: (a) il livello o i livelli di affidabilità per i quali l'organismo è competente a rilasciare certificati EUCC; (b) le informazioni relative all'accreditamento (data, nome e indirizzo dell'organismo, paese di registrazione, numero di riferimento, ambito e durata di validità, indirizzo, sede e link al sito web dell'organismo nazionale di accreditamento); (c) le informazioni relative all'autorizzazione per il livello «elevato» (data, numero di riferimento, durata di validità, ambito di applicazione compreso il livello AVA_VAN più elevato e, se del caso, il settore tecnico contemplato).",
        "testo_integrale": "3. All'atto della notifica alla Commissione degli organismi di certificazione, l'autorità nazionale di certificazione della cibersicurezza fornisce almeno le informazioni seguenti:\n\n(a) il livello o i livelli di affidabilità per i quali l'organismo di certificazione è competente a rilasciare certificati EUCC;\n\n(b) le informazioni relative all'accreditamento indicate di seguito:\n\n(1) la data dell'accreditamento;\n\n(2) il nome e l'indirizzo dell'organismo di certificazione;\n\n(3) il paese di registrazione dell'organismo di certificazione,\n\n(4) il numero di riferimento dell'accreditamento;\n\n(5) l'ambito di applicazione e la durata di validità dell'accreditamento;\n\n(6) l'indirizzo, la sede e il link al pertinente sito web dell'organismo nazionale di accreditamento; e\n\n(c) le informazioni relative all'autorizzazione per il livello «elevato» indicate di seguito:\n\n(1) la data dell'autorizzazione:\n\n(2) il numero di riferimento dell'autorizzazione;\n\n(3) la durata di validità dell'autorizzazione;\n\n(4) l'ambito di applicazione dell'autorizzazione, compreso il livello AVA_VAN più elevato e, se del caso, il settore tecnico contemplato.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 23 §4",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza invia una copia della notifica di cui ai paragrafi 1 e 2 all'ENISA, per la pubblicazione di informazioni accurate in merito all'ammissibilità degli organismi di certificazione sul sito web relativo alla certificazione della cibersicurezza.",
        "testo_integrale": "4. L'autorità nazionale di certificazione della cibersicurezza invia una copia della notifica di cui ai paragrafi 1 e 2 all'ENISA per la pubblicazione di informazioni accurate in merito all'ammissibilità degli organismi di certificazione sul sito web relativo alla certificazione della cibersicurezza.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 23 §5",
        "testo": "L'autorità nazionale di certificazione della cibersicurezza esamina senza indebito ritardo qualsiasi informazione relativa a una modifica dello stato dell'accreditamento fornita dall'organismo nazionale di accreditamento; se l'accreditamento o l'autorizzazione sono stati revocati, ne informa la Commissione e può presentare a quest'ultima una richiesta conformemente all'articolo 61, paragrafo 4, del regolamento (UE) 2019/881.",
        "testo_integrale": "5. L'autorità nazionale di certificazione della cibersicurezza esamina senza indebito ritardo qualsiasi informazione relativa a una modifica dello stato dell'accreditamento fornita dall'organismo nazionale di accreditamento. Se l'accreditamento o l'autorizzazione sono stati revocati, l'autorità nazionale di certificazione della cibersicurezza ne informa la Commissione e può presentare a quest'ultima una richiesta conformemente all'articolo 61, paragrafo 4, del regolamento (UE) 2019/881.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo se l'accreditamento o l'autorizzazione sono stati revocati.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 24",
        "testo": "Gli obblighi di notifica delle autorità nazionali di certificazione della cibersicurezza di cui all'articolo 23 si applicano anche alle ITSEF; la notifica include l'indirizzo dell'ITSEF, l'accreditamento valido e, se del caso, l'autorizzazione valida di tale ITSEF.",
        "testo_integrale": "Articolo 24\n\nNotifica dell'ITSEF\n\nGli obblighi di notifica delle autorità nazionali di certificazione della cibersicurezza di cui all'articolo 23 si applicano anche alle ITSEF. La notifica include l'indirizzo dell'ITSEF, l'accreditamento valido e, se del caso, l'autorizzazione valida di tale ITSEF.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = [
    "art. 21 §1",
    "art. 21 §1(a)",
    "art. 21 §1(b)",
    "art. 21 §1(c)",
    "art. 21 §2",
    "art. 21 §2(a)",
    "art. 21 §2(b)",
    "art. 21 §2(c)",
    "art. 21 §3",
    "art. 21 §4",
    "art. 21 §5",
    "art. 22 §1",
    "art. 22 §1(a)",
    "art. 22 §1(b)",
    "art. 22 §1(b)(1)",
    "art. 22 §1(b)(2)",
    "art. 22 §1(c)",
    "art. 22 §2",
    "art. 22 §3",
    "art. 22 §3(a)",
    "art. 22 §3(b)",
    "art. 22 §3(c)",
    "art. 22 §4",
    "art. 22 §5",
    "art. 22 §6",
    "art. 23 §1",
    "art. 23 §2",
    "art. 23 §3",
    "art. 23 §3(a)",
    "art. 23 §3(b)",
    "art. 23 §3(b)(1)",
    "art. 23 §3(b)(2)",
    "art. 23 §3(b)(3)",
    "art. 23 §3(b)(4)",
    "art. 23 §3(b)(5)",
    "art. 23 §3(b)(6)",
    "art. 23 §3(c)",
    "art. 23 §3(c)(1)",
    "art. 23 §3(c)(2)",
    "art. 23 §3(c)(3)",
    "art. 23 §3(c)(4)",
    "art. 23 §4",
    "art. 23 §5",
    "art. 24",
]

MAPPATURA_LOCALE = {
    "art. 21 §1": [
        "art. 21 §1",
        "art. 21 §1(a)",
        "art. 21 §1(b)",
        "art. 21 §1(c)",
    ],
    "art. 21 §2": [
        "art. 21 §2",
        "art. 21 §2(a)",
        "art. 21 §2(b)",
        "art. 21 §2(c)",
    ],
    "art. 21 §3": ["art. 21 §3"],
    "art. 21 §4": ["art. 21 §4"],
    "art. 21 §5": ["art. 21 §5"],
    "art. 22 §1": [
        "art. 22 §1",
        "art. 22 §1(a)",
        "art. 22 §1(b)",
        "art. 22 §1(b)(1)",
        "art. 22 §1(b)(2)",
        "art. 22 §1(c)",
    ],
    "art. 22 §2": ["art. 22 §2"],
    "art. 22 §3": [
        "art. 22 §3",
        "art. 22 §3(a)",
        "art. 22 §3(b)",
        "art. 22 §3(c)",
    ],
    "art. 22 §4": ["art. 22 §4"],
    "art. 22 §5": ["art. 22 §5"],
    "art. 22 §6": ["art. 22 §6"],
    "art. 23 §1": ["art. 23 §1"],
    "art. 23 §2": ["art. 23 §2"],
    "art. 23 §3": [
        "art. 23 §3",
        "art. 23 §3(a)",
        "art. 23 §3(b)",
        "art. 23 §3(b)(1)",
        "art. 23 §3(b)(2)",
        "art. 23 §3(b)(3)",
        "art. 23 §3(b)(4)",
        "art. 23 §3(b)(5)",
        "art. 23 §3(b)(6)",
        "art. 23 §3(c)",
        "art. 23 §3(c)(1)",
        "art. 23 §3(c)(2)",
        "art. 23 §3(c)(3)",
        "art. 23 §3(c)(4)",
    ],
    "art. 23 §4": ["art. 23 §4"],
    "art. 23 §5": ["art. 23 §5"],
    "art. 24": ["art. 24"],
}

# Relazioni interne a questa Fonte (fonte_id_o_None = None su entrambi gli
# estremi), tutte rinvii letterali verificati sul `testo_integrale` delle righe
# coinvolte: art. 21 §1 richiede che l'ITSEF sia "autorizzata in conformità
# dell'articolo 22" e il bersaglio e' "art. 22 §1", il comma che enuncia
# l'autorizzazione e le relative condizioni (i commi successivi dell'art. 22
# sono la procedura di valutazione, non il requisito di conformita' citato);
# art. 24 estende alle ITSEF "gli obblighi di notifica ... di cui all'articolo
# 23" e la citazione e' all'articolo in blocco, quindi la relazione e'
# propagata a ciascuno dei cinque commi dell'art. 23 che portano un obbligo di
# notifica o un suo corollario (§1 e §2 notifica alla Commissione, §3 contenuto
# minimo della notifica, §4 copia all'ENISA, §5 esame delle modifiche dello
# stato dell'accreditamento). Nessuna relazione e' dichiarata fra i commi
# speculari dell'art. 21 e dell'art. 22 (divieto/ITSEF): la duplicazione e'
# strutturale all'interno della stessa fonte e il tipo "si sovrappone a" di
# CONTEXT.md e' riservato allo stesso contenuto sostanziale espresso in fonti
# diverse. Nessuna relazione verso l'esterno del capitolo (art. 3, 43, 49 e
# allegato I della stessa fonte; regolamento (UE) 2019/881): sono rinvii
# demandati alla fase 6, elencati nel docstring del modulo. `confidence` =
# None: nessuno score reale da riportare.
RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "art. 21 §1"),
        "nodo_a": ("obbligo", None, "art. 22 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 24"),
        "nodo_a": ("obbligo", None, "art. 23 §1"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 24"),
        "nodo_a": ("obbligo", None, "art. 23 §2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 24"),
        "nodo_a": ("obbligo", None, "art. 23 §3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 24"),
        "nodo_a": ("obbligo", None, "art. 23 §4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 24"),
        "nodo_a": ("obbligo", None, "art. 23 §5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
