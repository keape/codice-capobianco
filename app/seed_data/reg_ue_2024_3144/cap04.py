"""Regolamento di esecuzione (UE) 2024/3144 della Commissione, del 18 dicembre
2024, recante modifica e rettifica del regolamento di esecuzione (UE) 2024/482
(EUCC). Fonte 30 (slug `reg_ue_2024_3144`), capitolo 4 di 5 (vedi
app/.source_cache/reg_ue_2024_3144/manifest.json): Allegato I dell'atto
modificativo, cioe' il testo del NUOVO allegato I del regolamento di
esecuzione (UE) 2024/482, "Documenti sullo stato dell'arte a sostegno dei
settori tecnici e altri documenti sullo stato dell'arte". L'art. 1 punti 1-8,
l'art. 2 (rettifiche), l'art. 3 (entrata in vigore) e l'allegato II stanno nei
capitoli 1, 2, 3 e 5 della stessa Fonte, assegnati ad altri moduli: nessuno di
quei file e' toccato qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_3144/cap04.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R3144, CELEX 32024R3144,
lingua italiana; URL risolto
http://publications.europa.eu/resource/cellar/12c401d0-bdaa-11ef-91ed-01aa75ed71a1.0014.03/DOC_1,
XHTML della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 74.420 byte
scaricati, 22.217 caratteri di testo, sha256 del raw.txt
7ced6d4bfe633cf367b3c72ec593ebd5e49c369c7f86f4386984fe81cb81493a - dettagli
completi in app/.source_cache/reg_ue_2024_3144/provenance.json).

Che cos'e' questa porzione (atto modificativo). Il punto dell'atto che
introduce questo testo e' l'art. 1, punto 7 di Fonte 30 ("l'allegato I e'
sostituito dal testo di cui all'allegato I del presente regolamento"), che e'
una riga del capitolo 2 di questa Fonte e non compare qui: l'intervento e'
quindi una SOSTITUZIONE INTEGRALE dell'allegato I di Fonte 29, non una
modifica puntuale. Le due righe di questo modulo sostituiscono
rispettivamente le righe "allegato I, punto 1" e "allegato I, punto 2" di
Fonte 29 (app/seed_data/reg_ue_2024_482/cap09.py), che sono l'allegato I
previgente. Il riferimento interno delle righe resta quello dell'allegato
dell'atto modificativo ("allegato I, punto 1" / "allegato I, punto 2") e
coincide testualmente con il riferimento del nuovo allegato I di Fonte 29: la
distinzione tra i due nodi omonimi e' il fonte_id (30 qui, 29 per le righe
sostituite), percio' in fase 6 le relazioni vanno risolte con la tupla
completa (tipo, fonte_id, riferimento) e non con il solo riferimento. Il
testo e' racchiuso tra virgolette di citazione («« ... ».»): conservate
verbatim dove il testo ufficiale le colloca (sotto). Perimetro: il solo
contenuto del nuovo allegato; nessuna disposizione del regolamento modificato
ripubblicata qui (i due punti dell'allegato I sono testo nuovo, non richiami a
commi di Fonte 29).

Modellazione (ADR-0007, nessun punto/lettera/vocetta non coperto, nessuno
coperto due volte):
- Unita' di copertura: i due punti numerati dell'allegato ("1." e "2."), con
  le loro lettere e i loro elenchi. Due righe, entrambe Principi "altro": 0
  Obblighi + 2 Principi.
- "allegato I, punto 1" (chapeau "Documenti sullo stato dell'arte a sostegno
  dei settori tecnici al livello AVA_VAN 4 o 5:", lettera a) con sette
  documenti per il settore tecnico "smart card e dispositivi simili", lettera
  b) con tre documenti per il settore tecnico "dispositivi hardware con box di
  sicurezza") -> UNA sola riga Principio "altro". Le due lettere sono
  frammenti nominali ("i seguenti documenti relativi alla valutazione
  armonizzata del settore tecnico ...:") senza verbo proprio, retti dal
  chapeau del punto; le dieci vocette numerate si differenziano solo per il
  titolo del documento e per la versione dichiarata, non hanno precetto
  autonomo e non nominano alcun soggetto, quindi non producono righe proprie e
  restano nel `testo_integrale` della riga con i loro item di indice separati.
  Scelta allineata a quella gia' presa per la versione previgente di questo
  stesso allegato (cap09 di Fonte 29, "allegato I, punto 1", unica riga per
  chapeau + lettere (a) e (b) + dieci documenti) e per l'elenco di norme
  dell'allegato I del Reg. 2024/2979 (cap05) e del Reg. 2025/2532 (cap01):
  qui come li' la lettera e' il ramo di una stessa designazione e il chapeau
  che le regge non ha contenuto proprio, quindi spezzare per lettera avrebbe
  richiesto una terza riga di solo chapeau senza guadagno di informazione.
  Item di indice mappati a questa riga: "allegato I, punto 1", "allegato I,
  punto 1(a)", "allegato I, punto 1(a)(1)" ... "1(a)(7)", "allegato I, punto
  1(b)", "allegato I, punto 1(b)(1)" ... "1(b)(3)".
- "allegato I, punto 2" (chapeau "Documenti sullo stato dell'arte relativi
  all'accreditamento armonizzato degli organismi di valutazione della
  conformita':", lettera a) "Accreditation of ITSEFs for the EUCC" versione
  1.1 per gli accreditamenti rilasciati prima dell'8 luglio 2025, lettera b)
  la stessa norma versione 1.6c per i nuovi accreditamenti o per quelli
  riesaminati dopo l'8 luglio 2025, lettera c) "Accreditation of CBs for the
  EUCC" versione 1.6b) -> UNA sola riga Principio "altro", per la stessa
  ragione del punto 1 (designazione di documenti, nessun soggetto, nessun
  comportamento imposto). Item di indice mappati: "allegato I, punto 2",
  "allegato I, punto 2(a)", "allegato I, punto 2(b)", "allegato I, punto
  2(c)". `condizione_applicabilita` NON valorizzata: le due delimitazioni
  temporali (accreditamenti prima / dopo l'8 luglio 2025) valgono per le
  lettere a) e b) ma non per la lettera c), quindi un unico valore sulla riga
  sarebbe falso per una parte del suo contenuto; le delimitazioni stanno
  integralmente nel `testo_integrale` e sono richiamate nella sintesi di
  `testo`.
- Classificazione (dubbio dichiarato, non nascosto). Entrambe le righe sono
  Principi "altro", non Obblighi: l'allegato designa documenti di riferimento,
  non nomina alcun soggetto ne' enuncia un precetto ("documenti sullo stato
  dell'arte a sostegno dei settori tecnici ..." e' un elenco di titoli con la
  versione). La lettura alternativa - Obbligo "tecnico/sicurezza" con soggetto
  obbligato "Terza parte" (le ITSEF e gli organismi di certificazione
  accreditati) e destinatari "QTSP/gestore" - sarebbe sostenibile muovendo
  dagli articoli di Fonte 29 che impongono di valutare conformemente ai
  documenti dell'allegato I (art. 7 §1(d), art. 7 §3(a), art. 15 §1(c),
  art. 22 §1(b)(2), art. 34 §2, art. 42 §1(f), art. 44 §3(a), allegato VI
  sezione VI.1 punto 1(b)) e dal nuovo art. 20 bis introdotto dall'art. 1,
  punto 3 di questa stessa Fonte ("L'accreditamento degli organismi di
  valutazione della conformita' tiene conto della specificazione dei requisiti
  per l'accreditamento degli organismi di certificazione e delle ITSEF di cui
  ai documenti sullo stato dell'arte applicabili figuranti all'allegato I,
  punto 2"): scelto il Principio perche' l'allegato in se' non nomina un
  soggetto ne' comanda un comportamento, e per non introdurre qui una
  classificazione divergente da quella gia' censita per la versione previgente
  dello stesso allegato (cap09 di Fonte 29) e per gli elenchi di norme di
  riferimento degli altri regolamenti del lotto. Chi in fase 6 vuole collegare
  queste righe ai precetti che le rendono operative usa "richiama" dalle righe
  di Fonte 29 verso queste (elenco sotto), non una riclassificazione.
- `oggetti_giuridici` non valorizzato: i documenti designati riguardano smart
  card e dispositivi simili, dispositivi hardware con box di sicurezza, ITSEF,
  organismi di certificazione e accreditamento EUCC; nessuno corrisponde a un
  valore dell'insieme censito (firma elettronica, sigillo elettronico, marca
  temporale elettronica qualificata, documento elettronico, servizio di
  recapito elettronico certificato, identificazione elettronica, ...).
  `severita'`/`sanzioni` non valorizzati: l'allegato non gradua requisiti ne'
  prevede sanzioni proprie.
- `testo_integrale` (verbatim, ADR-0010). Riga "allegato I, punto 1": il testo
  ufficiale della porzione comincia con le virgolette di citazione e con
  l'intestazione dell'allegato sostitutivo ("««ALLEGATO I") seguita dal suo
  titolo ("Documenti sullo stato dell'arte a sostegno dei settori tecnici e
  altri documenti sullo stato dell'arte"), che precedono immediatamente il
  punto 1 e non hanno un nodo proprio: sono assorbiti, verbatim e con le
  virgolette, in testa a questa riga. L'intestazione NON quotata "ALLEGATO I"
  che apre cap04.txt resta invece esclusa: e' la struttura dell'atto
  modificativo, non unita' normativa dell'allegato sostitutivo (stesso
  trattamento dei titoli di allegato in cap09 di Fonte 29). Riga "allegato I,
  punto 2": in coda e' assorbita la chiusura delle virgolette di citazione
  ("».»") che segue immediatamente la lettera c), perche' non esiste altro nodo
  dove collocarla. In entrambe le righe i numeri di punto, di lettera e di
  vocetta, che la conversione a testo isola su una riga propria, sono ricuciti
  in testa alla voce che introducono ("1. ", "a) ", "1) "), con riga vuota tra
  punto, lettera e voce: nessuna parola e' stata tolta o aggiunta, incluse le
  virgolette ufficiali “ ” dei titoli dei documenti, l'apostrofo della
  Gazzetta in “Certification of ‘open' smart card products” (riprodotto com'e',
  non corretto), l'underscore di "(ADV_ARC)" e la punteggiatura di fine voce
  (";" su tutte le voci tranne l'ultima di ciascuna lettera, che chiude con
  ".").

Esclusioni: il preambolo (considerando), l'epigrafe "Fatto a Bruxelles, il 18
dicembre 2024", la firma della presidente, la formula di chiusura ("Il presente
regolamento e' obbligatorio in tutti i suoi elementi e direttamente applicabile
in ciascuno degli Stati membri"), le note a pie' di pagina (1)-(6) dell'atto e
la riga ELI/ISSN non sono in questa porzione (stanno in coda all'art. 3 e al
documento, cioe' nel capitolo 3 di questa Fonte): nessun nodo, come in tutte le
Fonti gia' censite. Nella porzione l'unico testo che non entra in un nodo e'
l'intestazione non quotata "ALLEGATO I" (struttura dell'atto modificativo,
motivo sopra). L'allegato non ha note a pie' di pagina proprie: i documenti
sono citati solo per titolo e versione.

Rinvii demandati alla fase 6 (qui RELAZIONI = []: le uniche relazioni
possibili sarebbero verso i capitoli di questa stessa Fonte o verso Fonte 29,
e la loro costruzione spetta alla sessione principale; nessuna relazione tra i
due nodi di questo modulo, che sono due elenchi distinti senza gerarchia ne'
rinvio testuale tra loro):
1. art. 1, punto 7 di Fonte 30 (cap02): "l'allegato I e' sostituito dal testo
   di cui all'allegato I del presente regolamento" -> "sostituisce" verso
   entrambe le righe di questo modulo, e "e' sostituito da" da ciascuna riga
   di questo modulo verso la riga corrispondente di Fonte 29 (allegato I,
   punto 1 / allegato I, punto 2, cap09 di Fonte 29).
2. art. 1, punto 3 di Fonte 30 (nuovo art. 20 bis, cap01): rinvio letterale a
   "allegato I, punto 2" -> "richiama" verso "allegato I, punto 2" di questo
   modulo (evidence_type "textual": il rinvio e' letterale).
3. art. 1, punto 5 di Fonte 30 (nuovo art. 48 §4, cap02): "Salvo diversa
   indicazione nell'allegato I o II, i documenti sullo stato dell'arte si
   applicano a decorrere dalla data di applicazione dell'atto modificativo
   mediante il quale sono stati introdotti nell'allegato I o II" -> "richiama"
   verso entrambe le righe di questo modulo; e' la norma che rende rilevanti
   le indicazioni temporali delle lettere a) e b) del punto 2.
4. righe di Fonte 29 che citano l'allegato I e restano quindi collegate al
   testo sostitutivo: art. 7 §1(d), art. 7 §3(a), art. 15 §1(c), art. 22
   §1(b)(2), art. 34 §2, art. 42 §1(f), art. 44 §3(a), allegato III (chapeau),
   allegato VI sezione VI.1 punto 1(b) - tutte "richiama" verso la riga
   pertinente (verso il punto 1 di questo allegato dove il rinvio e' ai
   settori tecnici e alla valutazione, verso il punto 2 dove riguarda
   l'accreditamento).
5. nessun rinvio, in questa porzione, a norme esterne censite come Fonti: i
   documenti elencati (documenti ECCG, "Minimum ITSEF requirements",
   "Minimum Site Security Requirements", "Accreditation of ITSEFs for the
   EUCC", ...) non sono Fonti del censimento, quindi non esistono nodi
   bersaglio per collegare le singole voci.

Copertura: 17 item di indice, 2 righe (0 Obblighi + 2 Principi).
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "allegato I, punto 1",
        "testo": "Le valutazioni effettuate al livello AVA_VAN 4 o 5 si sostengono sui documenti sullo stato dell'arte elencati: sette documenti per la valutazione armonizzata del settore tecnico “smart card e dispositivi simili” (lettera a; sei in versione 1.1 e “Application of Attack Potential to Smartcards and Similar Devices” in versione 1.2) e tre documenti per la valutazione armonizzata del settore tecnico “dispositivi hardware con box di sicurezza” (lettera b; versioni 1.1 e 1.2). È un elenco di designazione di documenti di riferimento — nessun soggetto obbligato, nessun comportamento imposto — e ogni voce vale nella versione dichiarata.",
        "testo_integrale": "««ALLEGATO I\n\nDocumenti sullo stato dell'arte a sostegno dei settori tecnici e altri documenti sullo stato dell'arte\n\n1. Documenti sullo stato dell'arte a sostegno dei settori tecnici al livello AVA_VAN 4 o 5:\n\na) i seguenti documenti relativi alla valutazione armonizzata del settore tecnico “smart card e dispositivi simili”:\n\n1) “Minimum ITSEF requirements for security evaluations of smart cards and similar devices”, versione 1.1;\n\n2) “Minimum Site Security Requirements”, versione 1.1;\n\n3) “Application of Common Criteria to integrated circuits”, versione 1.1;\n\n4) “Security Architecture requirements (ADV_ARC) for smart cards and similar devices”, versione 1.1;\n\n5) “Certification of ‘open' smart card products”, versione 1.1;\n\n6) “Composite product evaluation for smart cards and similar devices”, versione 1.1;\n\n7) “Application of Attack Potential to Smartcards and Similar Devices”, versione 1.2;\n\nb) i seguenti documenti relativi alla valutazione armonizzata del settore tecnico “dispositivi hardware con box di sicurezza”:\n\n1) “Minimum ITSEF requirements for security evaluations of hardware devices with security boxes”, versione 1.1;\n\n2) “Minimum Site Security Requirements”, versione 1.1;\n\n3) “Application of Attack Potential to hardware devices with security boxes”, versione 1.2.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato I, punto 2",
        "testo": "Documenti sullo stato dell'arte relativi all'accreditamento armonizzato degli organismi di valutazione della conformità: “Accreditation of ITSEFs for the EUCC” versione 1.1 per gli accreditamenti rilasciati prima dell'8 luglio 2025 (lettera a), la stessa norma versione 1.6c per i nuovi accreditamenti o per quelli riesaminati dopo l'8 luglio 2025 (lettera b) e “Accreditation of CBs for the EUCC” versione 1.6b (lettera c). Designazione di documenti di riferimento con una delimitazione temporale delle versioni: nessun soggetto obbligato e nessun comportamento imposto.",
        "testo_integrale": "2. Documenti sullo stato dell'arte relativi all'accreditamento armonizzato degli organismi di valutazione della conformità:\n\na) “Accreditation of ITSEFs for the EUCC”, versione 1.1 per gli accreditamenti rilasciati prima dell'8 luglio 2025;\n\nb) “Accreditation of ITSEFs for the EUCC”, versione 1.6c, per i nuovi accreditamenti o per gli accreditamenti riesaminati dopo l'8 luglio 2025;\n\nc) “Accreditation of CBs for the EUCC”, versione 1.6b.\n\n».»",
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
    "allegato I, punto 2(b)",
    "allegato I, punto 2(c)",
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
        "allegato I, punto 2(b)",
        "allegato I, punto 2(c)",
    ],
}

# Nessuna relazione interna: i due punti dell'allegato sono due elenchi distinti
# di documenti, senza gerarchia ne' rinvio testuale tra loro. Le relazioni verso
# le righe di Fonte 29 sostituite e verso gli articoli che richiamano l'allegato
# I sono elencate nel docstring e costruite dalla sessione principale (fase 6).
RELAZIONI = []
