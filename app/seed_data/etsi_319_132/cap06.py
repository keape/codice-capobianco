"""ETSI EN 319 132-1 V1.3.1 (2024-07) - Electronic Signatures and Trust
Infrastructures (ESI); XAdES digital signatures; Part 1: Building blocks and
XAdES baseline signatures. Blocco B (famiglia AdES del lotto 2). Capitolo 6
dello split: parte finale della clausola 5 (Qualifying properties semantics and
syntax), da 5.5.2.3 (Computation of the message digest for not distributed
case) a 5.5.3 (The RenewedDigestsV2 qualifying property) inclusa, che chiude la
clausola 5: il capitolo successivo dello split (cap07.txt) apre la clausola 6.

Provenienza del testo: app/.source_cache/etsi_319_132/cap06.txt (255 righe,
porzione dello split deterministico; testo ufficiale completo in
app/.source_cache/etsi_319_132/raw.txt, raw_body.txt e raw.pdf). Versione ETSI
EN 319 132-1 V1.3.1 (2024-07), deliver "01.03.01_60"; da
app/.source_cache/etsi_319_132/provenance.json: URL ufficiale
https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf,
data_fetch 2026-09-29T12:56:34Z, sha256 del PDF grezzo
83fc87ee09de90274131a1f60cb73edb742cebc7cd8961342586ed06133664c5, formato
"PDF ETSI deliver (pdftotext -layout)". Manifest di split:
app/.source_cache/etsi_319_132/manifest.json (cap06 = "5.5.2.3 - Computation of
the message digest for not distributed case"; il capitolo precedente, cap05.txt,
copre da 5.2.8.2 a 5.5.2.2 inclusa). Questo modulo e' puro dato: non importa
nulla e non legge file; la numerazione degli id e' risolta per riferimento dalla
sessione principale in app/seed.py (che questo modulo NON tocca), e le relazioni
verso altri capitoli di questa fonte o verso altre fonti le costruisce sempre la
sessione principale (fase 6, ADR-0009).

## Perimetro

Tre unita' numerate dal documento, tutte coperte per intero: 5.5.2.3
(Computation of the message digest for not distributed case), 5.5.2.4
(Computation of the message digest for distributed case) e 5.5.3 (The
RenewedDigestsV2 qualifying property, con le sue due etichette interne
"Semantics" e "Syntax"). Il file cap06.txt comincia con il titolo di 5.5.2.3 e
termina con l'ultimo passo numerato del processamento in convalida di 5.5.3:
nessun front matter, Contents, Foreword, History, References o appendice ricade
nel perimetro. La clausola 5.5.2.2 (a cui 5.5.2.3 e 5.5.2.4 rinviano per il
passo 2) e' in cap05.txt; 5.5.1 e le altre sottoclausole della clausola 5 sono
in cap04.txt/cap05.txt.

## Granularita' (ADR-0007, decisione dell'utente: granularita' fine)

27 item di indice, 27 righe. Regola applicata: la riga e' la clausola quando la
clausola ha prosa propria non indicizzata, ed e' la singola voce quando il
documento numera o etichetta i propri requisiti con un indice che usa anche
altrove come riferimento. In dettaglio:

- 5.5.2.3 -> 1 riga per la clausola (i tre capoversi di premessa, con la
  delimitazione dell'ambito "same parent" e i due "shall" che la enunciano) +
  1 riga per ciascuno dei sei passi numerati 1)-6) + 1 riga per ciascuna delle
  quattro lettere a)-d) del passo 3) + 1 riga per la variante del passo 5) usata
  in convalida = 12 righe. I passi numerati sono un indice vero del documento:
  5.5.2.4 e le due varianti di convalida li richiamano per numero ("substituting
  its step 5 by the one specified below", "steps 1) to 6), BUT replacing 5)",
  "continue with step 6)", "computed in step 4)", "identified in step 2)", "go to
  step 2)"), esattamente come la clausola 6.3 di ETSI EN 319 122-1 usa le lettere
  a)-t) come indice dei propri requisiti addizionali. Le lettere a)-d) sono a loro
  volta richiamate per lettera dal testo ("else proceed to step d)").
- 5.5.2.4 -> 3 righe: la clausola (i due capoversi di premessa), il passo 5)
  sostitutivo con la sua NOTE, la variante del passo 5) per la convalida.
- 5.5.3 -> 1 riga per la clausola (le etichette "Semantics" e "Syntax" unite
  alla prima frase della rispettiva sezione, i sei capoversi di semantica con la
  NOTE 1, il blocco di schema XML copiato in clausola, i due requisiti sui figli
  ds:CanonicalizationMethod e ds:DigestMethod e le tre frasi che introducono gli
  elenchi numerati) + 1 riga per ciascuno dei due requisiti numerati 1)-2) sui
  figli di RecomputedDigestValue + 1 riga per ciascuno dei tre passi numerati del
  calcolo di OriginalRefDigest + 1 riga per ciascuno dei sei passi numerati del
  processamento in convalida = 12 righe. Anche qui i tre elenchi numerati sono
  usati dal documento come indice al proprio interno ("go to step 2)", "not
  performed in step 3)", "In step 4)", "computed in step 4)", "identified in
  step 2)"), e i due requisiti 1)-2) sono chiamati "requirements" dal documento
  stesso.

Dove il documento non numera (le tre frasi di chapeau degli elenchi di 5.5.3,
l'elenco puntato dei tre elementi XMLDSIG del passo 4), le due alternative
puntate dentro le lettere b) e c) del passo 3), le NOTE), il testo resta nella
riga dell'unita' che lo contiene: i chapeau nella riga della clausola, i punti
puntati nella riga del passo o della lettera a cui appartengono, le NOTE nella
riga dell'unita' che annotano (NOTE 1 di 5.5.2.3 -> passo 3), lettera a); NOTE 2
-> passo 5); NOTE di 5.5.2.4 -> passo 5) sostitutivo; NOTE 1 -> riga della
clausola 5.5.3 perche' annota la semantica della property; NOTE 2-4 -> i tre
passi di convalida che annotano). Nessuna NOTA duplicata o spostata su un'altra
riga.

Condizione applicata per distinguere i due casi, la stessa che i capitoli
fratelli di questa fonte enunciano esplicitamente: una voce di elenco genera una
riga propria solo se il documento le ha dato un'etichetta e la richiama
altrove con quell'etichetta. In cap07 di questa fonte vale per le lettere
a)-cc) dei requisiti addizionali (richiamate dalla colonna "Additional
requirements and notes" della Tabella 2), in ETSI EN 319 122-1 clausola 6.3 per
le lettere a)-t); qui vale per i passi numerati di 5.5.2.3 e di 5.5.3 (richiamati
per numero da 5.5.2.4, dalle due varianti di convalida e fra loro: "continue
with step 6)", "computed in step 4)", "identified in step 2)", "go to step
2)") e per le lettere a)-d) del passo 3) (richiamate come "step d)"). Non vale
per le voci di elenco prive di etichetta (i tre elementi XMLDSIG del passo 4),
le due alternative dentro b) e c), le NOTE), che restano nella riga dell'unita'
che le contiene. In cap05, il capitolo precedente di questa stessa fonte, la
stessa condizione porta al risultato opposto sui suoi requisiti numerati 1)-6)
di 5.4.2 e sui passi 1)-6) di 5.5.2.2: nessuno di essi e' richiamato altrove con
un'etichetta, quindi restano nel nodo della sottoclausta che li contiene.

DUBBIO DI GRANULARITA' APERTO per la revisione umana: se si ritenesse che il
richiamo per numero interno alla clausola non basti a dare identita' a una voce
(lettura piu' restrittiva, quella dei capitoli cap03/cap04 di questa stessa
fonte e di cap03/cap04 di ETSI EN 319 122-1, dove i passi numerati di un
processing model o di una procedura restano dentro il nodo della clausola, come
la clausola 5.5.3 di ETSI EN 319 122-1 tiene il proprio processo di calcolo del
message imprint, quattro punti 1)-4), nel nodo della sottoclausta), le 27 righe
di questo modulo si riducono a 3 (una per 5.5.2.3, una per 5.5.2.4, una per
5.5.3) senza perdere una parola: e' una riorganizzazione dei nodi, non un cambio
di testo.

## Obbligo o Principio, riga per riga

Nessun Principio in questo capitolo: ogni riga porta almeno un verbo deontico
("shall use", "shall be built", "shall contain", "shall be generated", "shall
be defined as", "shall be processed", "shall identify"). Le frasi puramente
dichiarative (il primo capoverso di 5.5.2.3 e di 5.5.2.4, che delimitano il
caso di applicazione della procedura) non sono isolate in un nodo a se': sono
la premessa della prescrizione che le segue nella stessa clausola, e restano
nella riga di quella clausola, come cap04 di questa fonte tiene le frasi
descrittive dentro la riga della sottoclausta che le contiene.

- 5.5.2.3 (clausola) -> Obbligo "procedurale": la qualifying property deve usare
  il meccanismo implicito di identificazione degli oggetti marcatati e
  l'impronta va costruita secondo l'algoritmo che segue.
- 5.5.2.3, passi 1)-6) -> 6 Obblighi "procedurale": sono i passi dell'algoritmo
  di costruzione dell'impronta (incorporazione condizionata di RenewedDigestsV2,
  inizializzazione dello stream, processamento dei ds:Reference, canonicalizzazione
  e concatenazione di SignedInfo/SignatureValue/KeyInfo, delle qualifying
  property non firmate e dei ds:Object).
- 5.5.2.3, passo 3), lettere a)-d) -> 4 Obblighi "procedurale": recupero
  dell'oggetto dati, ramo senza ds:Transforms, ramo con ds:Transforms,
  concatenazione degli ottetti.
- 5.5.2.3, passo 5) sostitutivo in convalida -> Obbligo "procedurale".
- 5.5.2.4 (clausola) -> Obbligo "procedurale": l'input del calcolo va costruito
  come nel caso non distribuito, sostituendo il passo 5).
- 5.5.2.4, passo 5) -> Obbligo "procedurale" (cancellazione dei nodi commento
  prima della canonicalizzazione).
- 5.5.2.4, passo 5) sostitutivo in convalida -> Obbligo "procedurale" (gli
  elementi Include dell'ArchiveTimeStamp in corso di convalida).
- 5.5.3 (clausola) -> Obbligo "tecnico/sicurezza": semantica e sintassi della
  qualifying property RenewedDigestsV2, i due requisiti sui figli
  ds:CanonicalizationMethod e ds:DigestMethod e il blocco di schema XML.
- 5.5.3, requisito 1) (NewSDODigestValue) e requisito 2) (OriginalRefDigest) ->
  2 Obblighi "tecnico/sicurezza": contenuto prescritto dei due figli di
  RecomputedDigestValue (digest base 64 dell'oggetto distaccato ricalcolato con
  l'algoritmo nuovo; digest base 64 del ds:Reference canonicalizzato).
- 5.5.3, calcolo di OriginalRefDigest, passi 1)-3) -> 3 Obblighi "procedurale":
  sequenza ordinata di operazioni (prendere e canonicalizzare il ds:Reference,
  calcolarne il digest, codificarlo in base 64 nel figlio OriginalRefDigest).
- 5.5.3, convalida della firma, passi 1)-6) -> 6 Obblighi "procedurale": sequenza
  ordinata di operazioni del convalidatore, con i rinvii interni per numero.

Regola seguita per `tipo_obbligo`: "procedurale" quando la riga prescrive una
sequenza ordinata di operazioni da eseguire (passi di un algoritmo o di un
processo, come in ETSI EN 319 102-1 cap06, clausola 5.5.4 "Processing"),
"tecnico/sicurezza" quando la riga fissa il contenuto o la sintassi di un
elemento o di una property. DUBBIO DI CLASSIFICAZIONE APERTO: le righe
"procedurale" di 5.5.2.3/5.5.2.4 e i passi di 5.5.3 sono anche prescrizioni
tecniche sulla costruzione della firma, come i due processing model di cap04 di
questa fonte, classificati "tecnico/sicurezza"; e la riga di 5.5.3 che fissa il
contenuto della property e' classificata "tecnico/sicurezza" pur contenendo le
tre frasi di chapeau di elenchi che sono processi. La sostanza del testo non
cambia in nessuno dei due casi.

`severita` e `sanzioni` assenti (standard tecnico, nessuna sanzione); `stato`
sempre "vigente"; `condizione_applicabilita` mai valorizzata: le condizioni che
compaiono nel testo (firma che contiene ds:Manifest firmati con oggetti
distaccati, stesso genitore oppure no, algoritmo di digest prossimo alla fine
del periodo di raccomandazione, impossibilita' di recuperare gli ottetti) sono
condizioni interne alla prescrizione, non fatti esterni non tracciati dal
censimento.

## Soggetti e oggetti giuridici

Nessun `soggetti` valorizzato. Il capitolo non nomina mai il soggetto della
prescrizione: le righe prescrivono sul processo di calcolo dell'impronta
("the electronic time-stamp's message imprint shall be built"), sulla property
("The RenewedDigestsV2 qualifying property shall contain the digest values") o
sui suoi figli
("The OriginalRefDigest child shall contain the base-64 encoded digest value"),
sempre in forma impersonale
o passiva. L'unico soggetto nominato e' "the signer" nel passo 3) di 5.5.2.3
("referencing whatever the signer wants to sign including the SignedProperties
element") e non e' il soggetto obbligato: indica l'origine dei dati
referenziati. DUBBIO DI CLASSIFICAZIONE APERTO: cap04 di questa stessa fonte
assegna 'Utente/titolare' obbligato alle sottoclausole che nominano "the
signer" (5.2.1, 5.2.3, 5.2.5, 5.2.6); se la revisione volesse applicare lo
stesso criterio anche qui, l'unica riga candidata sarebbe "clausola 5.5.2.3,
passo 3)" con 'Utente/titolare'/'obbligato'.

Nessun `oggetti_giuridici`: il testo nomina firme XAdES, marche temporali
elettroniche, oggetti dati distaccati e tipi XML, mai uno degli oggetti della
tassonomia eIDAS. "electronic time-stamp" senza qualificazione non e' la marca
temporale elettronica qualificata: stesso criterio di cap04 di questa fonte.

## Fedelta' dell'estrazione

- pie' di pagina e testatine delle pagine 50-52 ("ETSI" e "50 ETSI EN 319 132-1
  V1.3.1 (2024-07)", separati dal carattere di cambio pagina): rimossi, sono
  paratesto di impaginazione intercalato al testo dalle interruzioni di pagina
  (una cade fra il passo 5) e il passo 6) di 5.5.2.3, le altre due dentro
  5.5.3, fra il quarto e il quinto capoverso della semantica e fra il requisito
  2) e il calcolo di OriginalRefDigest).
- righe spezzate a meta' frase: ricucite in un'unica riga. I due trattini di
  fine riga appartengono alla parola e sono stati ricomposti senza spazio: il
  nome del file di schema "1913201-" + "XAdES01903v141.xsd" e "electronic
  time-" + "stamp" (variante del passo 5) di 5.5.2.4).
- intestazione della clausola NON ripetuta dentro `testo_integrale` (il
  riferimento del nodo la porta gia'); le etichette interne "Semantics" e
  "Syntax" di 5.5.3 sono mantenute e unite alla prima frase della rispettiva
  sezione, come in cap04 di questa fonte.
- elenchi: il carattere privato \uf0a7 usato da pdftotext per i pallini (passi
  3) b) e c) e passo 4) di 5.5.2.3; lo stesso carattere gia' documentato in
  ETSI EN 319 122-1 cap03) e' normalizzato al pallino "•" con indentazione
  crescente per livello, come gia' applicato a cap03/cap04 di questa fonte; i
  passi numerati "1)" e le lettere "a)" restano a inizio riga come nel testo.
- blocco di schema XML di 5.5.3: riportato per intero come il testo lo presenta
  (compreso il commento targetNamespace), separato dal testo da riga vuota.
- refusi del testo ufficiale riportati verbatim, senza correzione: "the
  RecomputedDigestValue 's OriginalRefDigest" (spazio prima di 's, due
  occorrenze), "ds:CanonicalizationMehtod" nel requisito 2) di 5.5.3 (il figlio
  e' ds:CanonicalizationMethod), il punto finale mancante in coda all'ultimo
  passo della variante di 5.5.2.4 (che si chiude con "to the final octet
  stream" senza punto) e il maiuscolo enfatico "DOES NOT" nella NOTE 2 di 5.5.2.3 e "BEFORE" nella
  variante.

## Esclusioni (paratesto, non contenuto normativo)

- front matter, Contents, Foreword, History, elenco dei riferimenti
  bibliografici (clausola 2 References) e tutte le clausole fuori dal perimetro
  (5.1, 5.2, 5.3, 5.4, 5.5.1, 5.5.2.1, 5.5.2.2): non fanno parte di cap06.txt e
  non sono censiti qui;
- NOTE informative: nessuna esclusa, tutte mantenute nella riga dell'unita' che
  annotano (NOTE 1 e 2 di 5.5.2.3, NOTE di 5.5.2.4, NOTE 1-4 di 5.5.3), perche'
  aggiungono contenuto interpretativo sul testo normativo che accompagnano;
- nessuna tabella, figura, allegato o blocco ASN.1 nel perimetro: l'unico
  blocco tecnico copiato in clausola e' lo schema XML di RenewedDigestsV2,
  riportato per intero.

## Rinvii demandati alla fase 6 (nessuna relazione creata verso di essi)

- rinvii ad altre clausole di questa stessa fonte, in altri capitoli dello
  split: "clause 4.5" (canonicalizzazione, otto rinvii: passo 3) lettere b) e
  c), passi 4), 5) e 6) e variante di convalida di 5.5.2.3, passo 5) e variante
  di convalida di 5.5.2.4; clausola 4 General Syntax, cap03.txt); "step 2 in
  clause 5.5.2.2" (premessa di 5.5.2.3 e di 5.5.2.4, cap05.txt); "clause C.2"
  per la collocazione dello schema XML (Syntax di 5.5.3; Annex C, non coperto
  da alcun capitolo di questo split).
- rinvii a unita' indivise della stessa clausola, che la fase 6 collega alle
  partizioni generate dalle righe di questo modulo: 5.5.2.4 -> "clause 5.5.2.3"
  e "steps 1) to 6) of clause 5.5.2.3" (la partizione "clausola 5.5.2" esiste,
  quella "clausola 5.5.2.3" no: il marcatore "passo" non e' fra quelli
  riconosciuti da partizioni_di, che deriva la partizione solo per §, punto,
  comma e lett. -> per questo il legame fra la riga della clausola e le sue
  righe di dettaglio e' dichiarato esplicitamente in RELAZIONI come "specifica",
  vedi sotto); 5.5.2.3 -> "clause 5.5.3" (riga dichiarata in questo modulo);
  NOTE 2 di 5.5.2.3 -> la property ArchiveTimeStamp in costruzione (clausola
  5.5.2, cap05.txt); NOTE di 5.5.2.4 -> gli elementi Include
  dell'ArchiveTimeStamp.
- norme e specifiche esterne: XMLDSIG [1] clausola 4.4.3.2 (passo 3) lettera a)
  di 5.5.2.3 e NOTE 1 che vi si riferisce; passo 3) del processamento in
  convalida di 5.5.3 e NOTE 2 che lo integra; requisito 1) di 5.5.3).

## Relazioni dichiarate

35 relazioni, tutte fra righe di questo modulo (nessuna verso altri capitoli o
altre fonti: le partizioni e i collegamenti cross-fonte sono costruiti dalla
sessione principale in fase 6, ADR-0009/ADR-0012). `confidence` resta null su
tutte: non esiste uno score reale da riportare (ADR-0005).

11 relazioni con `evidence_type` "textual", tutte citazioni letterali di un
numero di clausola, di un numero di passo o di una lettera presenti nel
`testo_integrale` del nodo citante:
- passo 1) di 5.5.2.3 -> clausola 5.5.3 ("as specified in clause 5.5.3 of the
  present document"), "richiama";
- clausola 5.5.2.4 -> clausola 5.5.2.3 ("as for the not distributed case (clause
  5.5.2.3)"), "richiama";
- clausola 5.5.2.4 -> passo 5) di 5.5.2.3 ("substituting its step 5 by the one
  specified below"), "deroga a": la citazione letterale sta nel capoverso di
  premessa della clausola 5.5.2.4 (riga della clausola, non riga del passo 5)
  sostitutivo), e nel caso distribuito il passo generale non si applica pur
  restando pienamente vigente nel caso non distribuito, esattamente la
  fattispecie che ADR-0008 descrive per "deroga a";
- variante di convalida di 5.5.2.3 -> passo 5) di 5.5.2.3 ("BUT replacing 5)
  with the following one"), "deroga a";
- variante di convalida di 5.5.2.4 -> passo 5) di 5.5.2.3 ("as indicated in
  steps 1) to 6) of clause 5.5.2.3, BUT replacing 5) with the following one"),
  "deroga a";
- lettera b) e lettera c) del passo 3) di 5.5.2.3 -> lettera d) ("else proceed
  to step d)"), 2 "richiama";
- passo 3) del processamento in convalida di 5.5.3 -> passo 6) ("continue with
  step 6)"), "richiama";
- passo 5) -> passo 4) e passo 2) ("computed in step 4)", "identified in step
  2)"), 2 "richiama";
- passo 6) -> passo 2) ("go to step 2)"), "richiama".

24 relazioni con `evidence_type` "inferred": ricostruiscono la gerarchia fra la
riga di una clausola e le righe di dettaglio in cui e' stata scomposta
("specifica" = nodo generale reso operativo da un nodo piu' specifico,
CONTEXT.md), che il livello delle partizioni non puo' derivare perche' i
marcatori "passo"/"lettera"/"requisito" non sono fra quelli riconosciuti da
`partizioni_di`. Sono: clausola 5.5.2.3 -> passi 1)-6) e variante di convalida
(7); passo 3) -> lettere a)-d) (4); clausola 5.5.2.4 -> passo 5) e variante di
convalida (2); clausola 5.5.3 -> requisiti 1)-2), calcolo di OriginalRefDigest
passi 1)-3) e processamento in convalida passi 1)-6) (11). Senza queste
relazioni le righe di dettaglio resterebbero agganciate solo alle partizioni
"clausola 5.5.2"/"clausola 5.5"/"clausola 5" e non piu' alla clausola di cui
sono l'articolazione.

## Copertura

27 item di indice, 27 righe: 27 obblighi + 0 principi. Nessun item doppio,
nessun item mancante, nessuna riga fuori indice. Verifica di completezza
eseguita anche a livello di parola: l'unione dei `testo_integrale` delle 27
righe, normalizzata, riproduce tutte le parole del testo ufficiale del
perimetro (titoli di clausola, pie' di pagina e testatine esclusi) una sola
volta, senza aggiunte.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 5.5.2.3 (Computation of the message digest for not distributed case)",
        "testo": (
            "La clausola definisce il processo di calcolo del message imprint della marca temporale "
            "(esecuzione del passo 2 della clausola 5.5.2.2) nel caso in cui ArchiveTimeStamp e tutte le "
            "qualifying property non firmate marcatate dalle sue marche temporali abbiano lo stesso genitore: "
            "la qualifying property deve allora usare il meccanismo implicito di identificazione degli oggetti "
            "marcatati e l'impronta va costruita seguendo l'algoritmo specificato nella clausola stessa."
        ),
        "testo_integrale": (
            """This clause defines the process for computing the message imprint (performing step 2 in clause 5.5.2.2) when ArchiveTimeStamp and all the unsigned qualifying properties time-stamped by its electronic time-stamp(s) have the same parent.

In this case, this qualifying property shall use the implicit mechanism for identifying all the time-stamped data objects.

The electronic time-stamp's message imprint shall be built following the algorithm specified below:"""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.3, passo 1)",
        "testo": (
            "Se la firma XAdES contiene uno o piu' ds:Manifest firmati che referenziano oggetti dati distaccati "
            "dalla firma e alcuni degli algoritmi di digest indicati nei ds:Reference figli sono prossimi alla "
            "fine del periodo di uso raccomandato, va incorporata una nuova qualifying property RenewedDigestsV2 "
            "come specificato nella clausola 5.5.3: il valore del suo figlio ds:DigestMethod dev'essere "
            "l'identificatore di un algoritmo di digest piu' forte e la property deve contenere tanti figli "
            "RecomputedDigestValue quanti sono i ds:Reference dei ds:Manifest firmati con algoritmo prossimo alla "
            "fine del periodo di uso raccomandato."
        ),
        "testo_integrale": (
            """1) If the XAdES signature contains one or more signed ds:Manifest referencing data objects that are detached from the signature, and some of the digest algorithms indicated within ds:Reference children are known to be near the end of its recommended period of use, incorporate a new RenewedDigestsV2 qualifying property as specified in clause 5.5.3 of the present document. The value of its ds:DigestMethod child element shall be the identifier of a stronger digest algorithm, and it shall contain as many RecomputedDigestValue children as ds:Reference elements within the aforementioned signed ds:Manifest elements with digest algorithms known to be near the end of its recommended period of use."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.3, passo 2)",
        "testo": (
            "Lo stream di ottetti finale va inizializzato come stream di ottetti vuoto."
        ),
        "testo_integrale": (
            """2) Initialize the final octet stream as an empty octet stream."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.3, passo 3)",
        "testo": (
            "Vanno presi tutti gli elementi ds:Reference nell'ordine di comparsa dentro ds:SignedInfo che "
            "referenziano cio' che il firmatario vuole firmare, incluso l'elemento SignedProperties, e ciascuno "
            "va processato come indicato dalle lettere a) a d)."
        ),
        "testo_integrale": (
            """3) Take all the ds:Reference elements in their order of appearance within ds:SignedInfo referencing whatever the signer wants to sign including the SignedProperties element. Process each one as indicated below:"""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.3, passo 3), lettera a)",
        "testo": (
            "Va recuperato l'oggetto dati referenziato dall'attributo URI dell'elemento ds:Reference, come "
            "specificato nella clausola 4.4.3.2 di XMLDSIG [1]; la NOTE 1 ricorda che il dereferenziamento di un "
            "riferimento non 'same-document' produce sempre un octet-stream."
        ),
        "testo_integrale": (
            """a) Retrieve the data object referenced by the URI attribute of the ds:Reference element, as specified in clause 4.4.3.2 of XMLDSIG [1].

NOTE 1: Clause 4.4.3.2 of XMLDSIG [1], specifies rules for URI dereferencing. For instance, it mandates that the dereferencing of a non 'same-document' reference (which XMLDSIG [1] defines as "a URI-Reference that consists of a hash sign ('#') followed by a fragment or alternatively consists of an empty URI") is always an octet-stream."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.3, passo 3), lettera b)",
        "testo": (
            "Se l'elemento ds:Reference non contiene l'elemento ds:Transforms: se l'oggetto dati recuperato e' un "
            "node-set XML va canonicalizzato come specificato nella clausola 4.5 del presente documento, "
            "altrimenti si prosegue al passo d)."
        ),
        "testo_integrale": (
            """b) If the ds:Reference element does not contain the ds:Transforms element, then:

  •   if the retrieved data object is an XML node-set, then canonicalize it as specified in clause 4.5 of the present document;

  •   else proceed to step d)."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.3, passo 3), lettera c)",
        "testo": (
            "Se l'elemento ds:Reference contiene l'elemento ds:Transforms vanno applicate tutte le trasformazioni "
            "indicate nei figli ds:Transform; se l'output dell'ultima trasformazione e' un node-set XML secondo "
            "XMLDSIG [1] va canonicalizzato come specificato nella clausola 4.5 del presente documento, altrimenti "
            "si prosegue al passo d)."
        ),
        "testo_integrale": (
            """c) If the ds:Reference element contains the ds:Transforms element, then apply all the transforms indicated within the ds:Transform children elements. After that:

  •   if the output of the last transform is a XML node-set according to XMLDSIG [1], canonicalize it as specified in clause 4.5 of the present document;

  •   else proceed to step d)."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.3, passo 3), lettera d)",
        "testo": (
            "Gli ottetti risultanti vanno concatenati allo stream di ottetti finale."
        ),
        "testo_integrale": (
            """d) Concatenate the resulting octets to the final octet stream."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.3, passo 4)",
        "testo": (
            "Vanno presi i tre elementi XMLDSIG elencati (ds:SignedInfo, ds:SignatureValue e, se presente, "
            "ds:KeyInfo) nell'ordine in cui sono elencati, ciascuno canonicalizzato come specificato nella "
            "clausola 4.5, e ciascun flusso di ottetti risultante va concatenato allo stream di ottetti finale."
        ),
        "testo_integrale": (
            """4) Take the following XMLDSIG elements in the order they are listed below, canonicalize each one as specified in clause 4.5, and concatenate each resulting octet stream to the final octet stream:

  •   The ds:SignedInfo element.

  •   The ds:SignatureValue element.

  •   The ds:KeyInfo element, if present."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.3, passo 5)",
        "testo": (
            "Vanno prese le qualifying property di firma non firmate presenti nella firma XAdES nell'ordine in cui "
            "compaiono dentro UnsignedSignatureProperties, ciascuna canonicalizzata come specificato nella clausola "
            "4.5, e ciascun flusso di ottetti risultante va concatenato allo stream di ottetti finale; la NOTE 2 "
            "ricorda che in questo momento la firma XAdES non incorpora ancora la nuova qualifying property "
            "ArchiveTimeStamp in corso di costruzione."
        ),
        "testo_integrale": (
            """5) Take the unsigned signature qualifying properties present in the XAdES signature in the order they appear within the UnsignedSignatureProperties, canonicalize each one as specified in clause 4.5 and concatenate each resulting octet stream to the final octet stream.

NOTE 2: Notice that, at this point in time the XAdES signature DOES NOT incorporate yet the new ArchiveTimeStamp qualifying property under construction."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.3, passo 6)",
        "testo": (
            "Vanno presi tutti gli elementi ds:Object tranne quello che contiene l'elemento QualifyingProperties, "
            "nel loro ordine di comparsa, ciascuno canonicalizzato come specificato nella clausola 4.5, e ciascun "
            "flusso di ottetti risultante va concatenato allo stream di ottetti finale."
        ),
        "testo_integrale": (
            """6) Take all the ds:Object elements except the one containing QualifyingProperties element, in their order of appearance. Canonicalize each one as specified in clause 4.5 and concatenate each resulting octet stream to the final octet stream."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.3, passo 5) sostitutivo in convalida",
        "testo": (
            "Per convalidare una marca temporale collocata dentro una specifica qualifying property "
            "ArchiveTimeStamp l'impronta va costruita come ai passi da 1) a 6), ma sostituendo il passo 5) con la "
            "variante che segue: si prendono le qualifying property di firma non firmate che precedono (compaiono "
            "PRIMA de) la qualifying property ArchiveTimeStamp che contiene la marca temporale in corso di "
            "convalida, nell'ordine in cui compaiono dentro il componente UnsignedSignatureProperties, e ciascuna "
            "va canonicalizzata come specificato nella clausola 4.5 e concatenata allo stream di ottetti finale."
        ),
        "testo_integrale": (
            """As a consequence of the previous process, for validating an electronic time-stamp placed within one specific ArchiveTimeStamp qualifying property present in a XAdES signature as specified in the first paragraph of this clause, its message imprint shall be built as indicated in steps 1) to 6), BUT replacing 5) with the following one:

5) Take the unsigned signature qualifying properties present in the XAdES signature, that precede (appear BEFORE) the ArchiveTimeStamp qualifying property that contains the electronic time-stamp that is being validated, in the order they appear within the UnsignedSignatureProperties component, canonicalize each one as specified in clause 4.5, and concatenate each resulting octet stream to the final octet stream."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.4 (Computation of the message digest for distributed case)",
        "testo": (
            "La clausola definisce il processo di calcolo del message imprint (esecuzione del passo 2 della "
            "clausola 5.5.2.2) nel caso distribuito, in cui ArchiveTimeStamp e alcune delle qualifying property "
            "non firmate marcatate dalle sue marche temporali non hanno lo stesso genitore: l'input del calcolo "
            "dell'impronta della marca temporale va costruito come nel caso non distribuito (clausola 5.5.2.3), "
            "sostituendo il suo passo 5) con quello specificato nella clausola."
        ),
        "testo_integrale": (
            """This clause defines the process for computing the message imprint (performing step 2 in clause 5.5.2.2) when ArchiveTimeStamp and some of the unsigned qualifying properties time-stamped by its electronic time-stamp(s) do not have the same parent.

The input to the electronic time-stamp's message imprint computation shall be built as for the not distributed case (clause 5.5.2.3) substituting its step 5 by the one specified below:"""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.4, passo 5)",
        "testo": (
            "Vanno prese le qualifying property di firma non firmate presenti nella firma, vanno eliminati i nodi "
            "commento, ciascuna qualifying property non firmata va canonicalizzata come specificato nella clausola "
            "4.5 e ciascun flusso di ottetti risultante va concatenato allo stream di ottetti finale; la NOTE "
            "ricorda che la nuova qualifying property ArchiveTimeStamp avra' un elemento Include per ogni "
            "qualifying property non firmata marcata, collocati nello stesso ordine in cui le property "
            "referenziate sono state processate per costruire l'input del calcolo dell'impronta."
        ),
        "testo_integrale": (
            """5) Take the unsigned signature qualifying properties present in the signature, delete the comment nodes, canonicalize each unsigned signature qualifying property as specified in clause 4.5, and concatenate each resulting octet stream to the final octet stream.

NOTE: As it has been stated before, the new ArchiveTimeStamp qualifying property will have one Include element for each unsigned qualifying property time-stamped by its electronic time-stamp(s); the Include elements are placed within the ArchiveTimeStamp in the same order as the referenced unsigned qualifying properties have been processed to build the input to the message imprint computation."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2.4, passo 5) sostitutivo in convalida",
        "testo": (
            "Per convalidare una marca temporale collocata dentro una specifica qualifying property "
            "ArchiveTimeStamp l'impronta va costruita come ai passi da 1) a 6) della clausola 5.5.2.3, ma "
            "sostituendo il passo 5) con la variante che segue: vanno presi tutti gli elementi Include dentro "
            "l'elemento ArchiveTimeStamp che incapsula la marca temporale in corso di convalida, in ordine di "
            "comparsa, e per ciascuno va recuperata la qualifying property non firmata referenziata presente nella "
            "firma XAdES, eliminati i nodi commento, canonicalizzata come specificato nella clausola 4.5 e "
            "concatenato il flusso di ottetti risultante allo stream di ottetti finale."
        ),
        "testo_integrale": (
            """As a consequence of the previous process, for validating an electronic time-stamp placed within one specific ArchiveTimeStamp qualifying property present in a XAdES signature as specified in the first paragraph of this clause, its message imprint shall be built as indicated in steps 1) to 6) of clause 5.5.2.3, BUT replacing 5) with the following one:

5) Take all the Include elements within the ArchiveTimeStamp element encapsulating the electronic time-stamp being validated in order of appearance. For each Include element, retrieve the referenced unsigned qualifying property present in the XAdES signature, delete comment nodes, canonicalize it as specified in clause 4.5, and concatenate the resulting octet stream to the final octet stream"""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)",
        "testo": (
            "Semantica e sintassi della qualifying property non firmata RenewedDigestsV2: puo' essere usata quando "
            "la firma XAdES contiene uno o piu' ds:Manifest firmati che referenziano oggetti dati distaccati e non "
            "deve essere usata quando la firma non ne contiene nessuno; deve contenere i valori di digest di quegli "
            "oggetti distaccati firmati indirettamente, calcolati con un algoritmo diverso da quello usato nei "
            "ds:Reference del ds:Manifest, va incorporata quando un algoritmo di digest sta diventando debole e, "
            "quando lo diventa quello usato per costruirla, va rigenerata. La sintassi e' definita nel file di "
            "schema XML 1913201-XAdES01903v141.xsd, copiato nella clausola per informazione: i figli "
            "ds:CanonicalizationMethod e ds:DigestMethod devono identificare rispettivamente un algoritmo di "
            "canonicalizzazione e l'algoritmo di digest del ricalcolo, mentre il contenuto dei figli di "
            "RecomputedDigestValue, il calcolo di OriginalRefDigest e il processamento in convalida sono "
            "specificati nei requisiti e nei passi numerati della clausola stessa."
        ),
        "testo_integrale": (
            """Semantics: The RenewedDigestsV2 qualifying property is an unsigned qualifying property qualifying the signature.

The RenewedDigestsV2 qualifying property may be used when the XAdES signature contains one or more signed ds:Manifest referencing data objects that are detached from the signature.

The RenewedDigestsV2 qualifying property shall not be used if the XAdES signature does not contain any signed ds:Manifest referencing data objects that are detached from the signature.

The RenewedDigestsV2 qualifying property shall contain the digest values of the aforementioned indirectly signed detached data objects computed with a different digest algorithm than the one used for computing the digest values present within the ds:Manifest's ds:Reference children.

When a certain digest algorithm is becoming weak, one or more detached data objects have been indirectly signed using that algorithm with a signed ds:Manifest, when long term signatures are managed using ArchiveTimeStamp qualifying property, and when suspected that some of the aforementioned data objects might be substituted by others with the same digest value due to the weakness of the digest algorithm, the RenewedDigestsV2 element shall be incorporated into the XAdES signature including the digest values of the aforementioned data objects computed with a different algorithm.

NOTE 1: This will ensure that any substitution of a detached document indirectly signed through a signed ds:Manifest, will be detected even if the digest algorithm used for computing the references within the aforementioned ds:Manifest, has been broken.

Whenever it is detected that the digest algorithm used for building a RenewedDigestsV2 element is becoming weak, a new RenewedDigestsV2 element shall be generated incorporating digest values of the detached signed data objects computed with different algorithms.

Syntax: The RenewedDigestsV2 qualifying property shall be defined as in XML Schema file "1913201-XAdES01903v141.xsd", whose location is detailed in clause C.2, and is copied below for information.

<!-- targetNamespace="http://uri.etsi.org/01903/v1.4.1#" -->

<xsd:element name="RenewedDigestsV2" type="RenewedDigestsV2Type"/>

<xsd:complexType name="RenewedDigestsV2Type">
    <xsd:sequence>
        <xsd:element ref="ds:CanonicalizationMethod"/>
        <xsd:element ref="ds:DigestMethod"/>
        <xsd:element ref="RecomputedDigestValue" maxOccurs="unbounded"/>
    </xsd:sequence>
    <xsd:attribute name="Id" type="xsd:ID" use="optional"/>
</xsd:complexType>

<xsd:element name="RecomputedDigestValue" type="RecomputedDigestValueType"/>

<xsd:complexType name="RecomputedDigestValueType">
    <xsd:sequence>
        <xsd:element name="NewSDODigestValue" type="ds:DigestValueType"/>
        <xsd:element name="OriginalRefDigest" type="ds:DigestValueType"/>
    </xsd:sequence>
</xsd:complexType>

The ds:CanonicalizationMethod child shall identify a canonicalization algorithm.

The ds:DigestMethod child shall identify the digest algorithm used for recomputing the digest values of the detached signed data objects referenced by ds:Reference elements children of signed ds:Manifest elements.

RecomputedDigestValue's children elements satisfy the following requirements:

The content of the RecomputedDigestValue 's OriginalRefDigest shall be computed as indicated below:

When validating the signature, each RenewedDigestsV2 qualifying property incorporated to the XAdES signature shall be processed as follows:"""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.3, requisito 1) (NewSDODigestValue)",
        "testo": (
            "Il figlio NewSDODigestValue deve contenere il valore di digest codificato in base 64, calcolato con "
            "l'algoritmo identificato nel figlio ds:DigestMethod di RenewedDigestsV2, di un oggetto distaccato "
            "firmato; tale digest va calcolato sul risultato del processamento, secondo il modello di processamento "
            "dei riferimenti definito nella clausola 4.4.3.2 di XMLDSIG [1], dell'elemento ds:Reference figlio di "
            "uno dei ds:Manifest firmati che referenzia l'oggetto dati distaccato firmato suddetto."
        ),
        "testo_integrale": (
            """1) The NewSDODigestValue child shall contain the base-64 encoded digest value, computed using the algorithm identified in the RenewedDigestsV2's ds:DigestMethod child element, of one signed detached object. This digest value shall be computed on the result of processing, as specified by the reference processing model defined in clause 4.4.3.2 of XMLDSIG [1], the ds:Reference element, child of one of the signed ds:Manifest elements, referencing the aforementioned detached signed data object."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.3, requisito 2) (OriginalRefDigest)",
        "testo": (
            "Il figlio OriginalRefDigest deve contenere il valore di digest codificato in base 64 dell'elemento "
            "ds:Reference canonicalizzato, figlio di uno dei ds:Manifest firmati, che referenzia l'oggetto dati "
            "distaccato firmato il cui valore ricalcolato e' collocato nell'elemento NewSDODigestValue; l'elemento "
            "ds:Reference va canonicalizzato con l'algoritmo di canonicalizzazione identificato nel figlio "
            "ds:CanonicalizationMehtod (refuso del testo ufficiale) di RenewedDigestsV2 e il digest va calcolato "
            "con l'algoritmo identificato nel suo figlio ds:DigestMethod."
        ),
        "testo_integrale": (
            """2) The OriginalRefDigest child shall contain the base-64 encoded digest value of the canonicalized ds:Reference element, child of one of the signed ds:Manifest elements, referencing the detached signed data object whose recomputed value is placed in the NewSDODigestValue element. The ds:Reference shall be canonicalized using the canonicalization algorithm identified in the RenewedDigestsV2's ds:CanonicalizationMehtod child element. The digest value shall be computed using the algorithm identified in the RenewedDigestsV2's ds:DigestMethod child element."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.3, calcolo di OriginalRefDigest, passo 1)",
        "testo": (
            "Va preso il figlio ds:Reference dell'elemento ds:Manifest che referenzia l'oggetto dati distaccato "
            "firmato il cui nuovo valore di digest e' stato collocato nel figlio NewSDODigestValue di "
            "RecomputedDigestValue, e va canonicalizzato con l'algoritmo di canonicalizzazione presente nel figlio "
            "ds:CanonicalizationMethod di RenewedDigestsV2."
        ),
        "testo_integrale": (
            """1) Take the ds:Reference child of the ds:Manifest element referencing to the detached signed data object whose new digest value has been placed within RecomputedDigestValue's NewSDODigestValue child, and canonicalize it using the canonicalization algorithm present in the RenewedDigestsV2's ds:CanonicalizationMethod child."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.3, calcolo di OriginalRefDigest, passo 2)",
        "testo": (
            "Va calcolato il digest dell'elemento ds:Reference canonicalizzato usando l'algoritmo di digest "
            "identificato nel figlio ds:DigestMethod di RenewedDigestsV2."
        ),
        "testo_integrale": (
            """2) Compute the digest of the canonicalized ds:Reference using the digest algorithm identified in the RenewedDigestsV2's ds:DigestMethod child."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.3, calcolo di OriginalRefDigest, passo 3)",
        "testo": (
            "Il valore di digest risultante va codificato in base 64 e collocato nel figlio OriginalRefDigest di "
            "RecomputedDigestValue."
        ),
        "testo_integrale": (
            """3) Base-64 encode the resulting digest value and place it within the RecomputedDigestValue 's OriginalRefDigest child."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.3, convalida della firma, passo 1)",
        "testo": (
            "In convalida va preso il primo elemento figlio RecomputedDigestValue."
        ),
        "testo_integrale": (
            """1) Take the first RecomputedDigestValue child element."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.3, convalida della firma, passo 2)",
        "testo": (
            "Va recuperato l'elemento ds:Reference referenziato dal figlio OriginalRefDigest dell'elemento "
            "RecomputedDigestValue preso in esame."
        ),
        "testo_integrale": (
            """2) Retrieve the ds:Reference element referenced by the OriginalRefDigest child of the taken RecomputedDigestValue element."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.3, convalida della firma, passo 3)",
        "testo": (
            "Va recuperato l'oggetto dati referenziato da tale elemento ds:Reference e va processato il suo figlio "
            "ds:Transforms secondo il modello di processamento dei riferimenti di XMLDSIG [1], clausola 4.4.3.2; se "
            "non e' possibile recuperare gli ottetti referenziati va segnalato che non e' stato possibile "
            "recuperare con successo l'oggetto dati distaccato firmato referenziato dal ds:Reference identificato "
            "al passo precedente, e si prosegue al passo 6)."
        ),
        "testo_integrale": (
            """3) Retrieve the data object referenced by the aforementioned ds:Reference element and process its ds:Transforms child according to the reference-processing model of XMLDSIG [1], clause 4.4.3.2. If it is not possible to retrieve the referenced octets, then notify that it has not been possible to successfully retrieve the detached signed data object referenced by the ds:Reference element identified in the previous step, and continue with step 6).

NOTE 2: Clause 4.4.3.2 of XMLDSIG [1] specifies that the last step of the ds:Reference element is the computation of the digest of the retrieved and transformed signed data object with an algorithm identified in the ds:Reference's ds:DigestMethod child element. This computation is not performed in step 3)."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.3, convalida della firma, passo 4)",
        "testo": (
            "Va calcolato il valore di digest degli ottetti risultanti usando l'algoritmo di digest identificato "
            "nel figlio ds:DigestMethod di RenewedDigestsV2; la NOTE 3 precisa che l'oggetto dati firmato "
            "recuperato e trasformato viene digerito con quell'algoritmo, diverso da quello identificato nel figlio "
            "ds:DigestMethod del ds:Reference."
        ),
        "testo_integrale": (
            """4) Compute the digest value of the resulting octets using the digest algorithm identified in the RenewedDigestsV2's ds:DigestMethod child element.

NOTE 3: In step 4), the retrieved and transformed signed data object is digested using the digest algorithm identified within RenewedDigestsV2's ds:DigestMethod child element, which is different than the algorithm identified within the ds:DigestMethod child of the ds:Reference element."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.3, convalida della firma, passo 5)",
        "testo": (
            "Se il valore di digest calcolato al passo 4) e' diverso dal valore di digest presente nell'elemento "
            "NewSDODigestValue va segnalata una discordanza nel valore di digest dell'oggetto dati distaccato "
            "firmato referenziato dal ds:Reference identificato al passo 2); la NOTE 4 ricorda che per confrontare "
            "quei valori di digest occorre tenere conto che il contenuto di NewSDODigestValue e' un valore di "
            "digest codificato in base 64."
        ),
        "testo_integrale": (
            """5) If the digest value computed in step 4) is different from the digest value present within the NewSDODigestValue element, then notify that there is a mismatch in the digest value of the detached signed data object referenced by the ds:Reference element identified in step 2).

NOTE 4: For comparing the aforementioned digest values, it needs to be considered that the content of NewSDODigestValue element is a base-64 encoded digest value."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.3, convalida della firma, passo 6)",
        "testo": (
            "Se vi sono altri elementi RecomputedDigestValue non ancora processati va preso quello successivo e si "
            "torna al passo 2), altrimenti il processo si conclude."
        ),
        "testo_integrale": (
            """6) If there are other RecomputedDigestValue elements that have not been yet processed, take the next RecomputedDigestValue element and go to step 2); else finalize the process."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI: list[dict] = []

# UNA riga per clausola, per passo numerato, per lettera e per requisito numerato:
# il riferimento del nodo e' anche il suo item di indice (vedi docstring).
INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 5.5.2.3 (Computation of the message digest for not distributed case)",
    "clausola 5.5.2.3, passo 1)",
    "clausola 5.5.2.3, passo 2)",
    "clausola 5.5.2.3, passo 3)",
    "clausola 5.5.2.3, passo 3), lettera a)",
    "clausola 5.5.2.3, passo 3), lettera b)",
    "clausola 5.5.2.3, passo 3), lettera c)",
    "clausola 5.5.2.3, passo 3), lettera d)",
    "clausola 5.5.2.3, passo 4)",
    "clausola 5.5.2.3, passo 5)",
    "clausola 5.5.2.3, passo 6)",
    "clausola 5.5.2.3, passo 5) sostitutivo in convalida",
    "clausola 5.5.2.4 (Computation of the message digest for distributed case)",
    "clausola 5.5.2.4, passo 5)",
    "clausola 5.5.2.4, passo 5) sostitutivo in convalida",
    "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)",
    "clausola 5.5.3, requisito 1) (NewSDODigestValue)",
    "clausola 5.5.3, requisito 2) (OriginalRefDigest)",
    "clausola 5.5.3, calcolo di OriginalRefDigest, passo 1)",
    "clausola 5.5.3, calcolo di OriginalRefDigest, passo 2)",
    "clausola 5.5.3, calcolo di OriginalRefDigest, passo 3)",
    "clausola 5.5.3, convalida della firma, passo 1)",
    "clausola 5.5.3, convalida della firma, passo 2)",
    "clausola 5.5.3, convalida della firma, passo 3)",
    "clausola 5.5.3, convalida della firma, passo 4)",
    "clausola 5.5.3, convalida della firma, passo 5)",
    "clausola 5.5.3, convalida della firma, passo 6)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# 35 relazioni interne al perimetro di questo capitolo (vedi docstring): 11
# citazioni letterali di un passo o di una lettera del testo ("richiama"/"deroga
# a", evidence_type "textual") e 24 relazioni "specifica" dedotte dalla
# scomposizione della clausola nelle sue voci numerate (evidence_type
# "inferred"). Nessuna relazione verso altri capitoli di questa fonte o verso
# altre fonti: le partizioni e i collegamenti cross-fonte sono costruiti dalla
# sessione principale in fase 6 (ADR-0009, ADR-0012).
RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 1)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 3), lettera b)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 3), lettera d)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 3), lettera c)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 3), lettera d)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 5) sostitutivo in convalida"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 5)"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.4 (Computation of the message digest for distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3 (Computation of the message digest for not distributed case)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.4 (Computation of the message digest for distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 5)"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.4, passo 5) sostitutivo in convalida"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 5)"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 3)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 6)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 5)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 4)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 5)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 2)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 6)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 2)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3 (Computation of the message digest for not distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 1)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3 (Computation of the message digest for not distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 2)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3 (Computation of the message digest for not distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 3)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3 (Computation of the message digest for not distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 4)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3 (Computation of the message digest for not distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 5)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3 (Computation of the message digest for not distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 6)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3 (Computation of the message digest for not distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 5) sostitutivo in convalida"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 3)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 3), lettera a)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 3)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 3), lettera b)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 3)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 3), lettera c)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 3)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3, passo 3), lettera d)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.4 (Computation of the message digest for distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.4, passo 5)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.4 (Computation of the message digest for distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.4, passo 5) sostitutivo in convalida"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, requisito 1) (NewSDODigestValue)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, requisito 2) (OriginalRefDigest)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, calcolo di OriginalRefDigest, passo 1)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, calcolo di OriginalRefDigest, passo 2)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, calcolo di OriginalRefDigest, passo 3)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 1)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 2)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 3)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 4)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 5)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 6)"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
]
