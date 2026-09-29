"""ETSI EN 319 132-1 V1.3.1 (2024-07) - Electronic Signatures and Trust
Infrastructures (ESI); XAdES digital signatures; Part 1: Building blocks and
XAdES baseline signatures. Blocco B (famiglia AdES del lotto 2). Capitolo 1
dello split deterministico: clausola 1 (Scope) soltanto. Conteggio di questo
capitolo: 0 Obblighi, 1 Principio, 1 item di indice, 0 relazioni. Questo
modulo NON tocca app/seed.py: gli id sono risolti per riferimento dalla
sessione principale tramite app/seed_data/lib.py, e le relazioni verso altri
capitoli della stessa fonte o verso altre fonti le costruisce sempre la
sessione principale (fase 6, ADR-0009). Il modulo e' puro dato: nessun import,
nessuna lettura di file, nessuna scrittura.

Provenienza del testo: app/.source_cache/etsi_319_132/cap01.txt (179 righe;
porzione dello split deterministico, testo ufficiale completo in
app/.source_cache/etsi_319_132/raw.txt, raw_body.txt e raw.pdf), dal PDF
ufficiale ETSI deliver
https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf
versione 01.03.01_60, formato "PDF ETSI deliver (pdftotext -layout)",
data_fetch 2026-09-29T12:56:34Z, sha256 del PDF raw
83fc87ee09de90274131a1f60cb73edb742cebc7cd8961342586ed06133664c5 (tutti i
valori da app/.source_cache/etsi_319_132/provenance.json). Manifest di split:
app/.source_cache/etsi_319_132/manifest.json. Il file di capitolo inizia alla
riga "1             Scope" (righe 1-28 del file) e prosegue con la clausola 2
(References), fuori perimetro.

## Perimetro del capitolo

Solo la clausola 1 (Scope), capitolo di cornice: nessuna prescrizione con
destinatario (tutti i "shall" di questo standard vivono dalle clausole 4 in
poi).

- Clausola 1 (Scope) -> 1 Principio "scopo/ambito di applicazione",
  riferimento "clausola 1 (Scope)". Contiene, in sei paragrafi piu' una NOTE:
  (a) l'oggetto (specifica delle firme digitali XAdES, costruite sulle firme
  digitali XML [1] incorporando proprieta' qualificanti firmate e non firmate
  che soddisfano requisiti comuni, come la validita' a lungo termine delle
  firme, in diversi casi d'uso); (b) l'oggetto tecnico (definizioni di XML
  Schema di quelle proprieta' qualificanti e meccanismi per incorporarle nelle
  firme XAdES); (c) i formati delle firme XAdES baseline e la loro finalita'
  (casi d'uso aziendali e governativi di procedure e comunicazioni
  elettroniche, applicabili a comunita' diverse quando c'e' una chiara
  esigenza di interoperabilita' delle firme digitali usate nei documenti
  elettronici); (d) i quattro livelli di firma XAdES baseline con requisiti
  incrementali (ogni livello copre i requisiti dei livelli inferiori, ogni
  livello richiede la presenza di certe proprieta' qualificanti XAdES
  profilate per ridurre il piu' possibile l'opzionalita'); (e) il fuori
  perimetro (procedure di creazione, augmentation e convalida, demandate a
  ETSI EN 319 102-1 [i.6]) e la guida esterna (ETSI TR 119 100 [i.11]); (f) la
  finalita' di supporto alle firme elettroniche nei diversi quadri regolatori,
  con la NOTE che la specifica al Regolamento (UE) n. 910/2014 [i.1]
  ("Specifically but not exclusively": firme elettroniche, firme elettroniche
  avanzate, firme elettroniche qualificate, sigilli elettronici, sigilli
  elettronici avanzati e sigilli elettronici qualificati). Nessun Obbligo: il
  testo e' interamente descrittivo ("The present document
  specifies/defines/aims at"), non impone un comportamento a un soggetto
  identificabile e non contiene alcun verbo prescrittivo con destinatario. La
  NOTE e' assorbita nel `testo_integrale` perche' non e' un mero rimando
  bibliografico: precisa il perimetro funzionale del documento, cioe' quali
  strumenti giuridici le firme XAdES mirano a supportare.

## Granularita' e convenzione dei riferimenti

"Un item di indice per unita' di prescrizione" e' letto qui come **una riga e
un item per la clausola 1**, non un nodo per singolo paragrafo: la clausola 1
di uno standard ETSI non numera i propri capoversi (nessun 1.1, nessuna
lettera a), b), ...), e i paragrafi non sono unita' citabili singolarmente da
altre clausole. E' la convenzione costante delle fonti ETSI gia' censite (es.
ETSI EN 319 122-1 cap01 e ETSI EN 319 401 cap01: "clausola 1 (Scope)" come
item unico, riferimento "clausola 1 (Scope)"), e il gemello diretto di questo
capitolo nella stessa famiglia AdES: la clausola 1 di ETSI EN 319 122-1
(CAdES), che ha forma e NOTE quasi identiche, e' censita con lo stesso
riferimento e lo stesso tipo di principio. Spezzare la clausola in sei item
fittizi attribuirebbe a questa fonte una granularita' che il testo non ha e
romperebbe i rinvii cross-fonte verso "clausola 1". Il riferimento segue la
forma italiana convenzionale (procedura passo 2-bis) senza prefisso di parte,
per restare omogeneo ai moduli fratelli della stessa Fonte; il testo
integrale resta in inglese verbatim.

## Esclusioni

- Clausola 2 (References), interamente contenuta in cap01.txt ma fuori
  perimetro: e' bibliografia e paratesto puro (2.1 Normative references con i
  riferimenti [1]-[18]; 2.2 Informative references con [i.1]-[i.22]), con le
  NOTE ETSI di irresponsabilita' sulla validita' a lungo termine degli
  hyperlink e i paragrafi redazionali uniformi a tutti i deliverable ETSI
  (riferimenti specifici identificati da data di pubblicazione e/o numero di
  edizione o versione e non specifici; per i riferimenti specifici vale solo
  la versione citata, per i non specifici l'ultima versione del documento
  richiamato, emendamenti inclusi; i documenti non reperibili si cercano su
  https://docbox.etsi.org/Reference/). Nessuno di questi elementi e' un'unita'
  di prescrizione e nessun altro documento puo' rinviare a una voce di
  bibliografia come a una clausola di questo standard. Stesso trattamento gia'
  riservato alla clausola 2 delle altre fonti ETSI censite (ETSI EN 319 122-1,
  EN 319 102-1, EN 319 401, TS 119 612).
- Front matter, pagine di copertina, Contents, Foreword (inclusa la frase di
  partizione del deliverable multi-parte), History e il paratesto di pagina
  ripetuto dalla conversione PDF (piede "ETSI", intestazione "ETSI EN 319
  132-1 V1.3.1 (2024-07)", numeri di pagina): gia' esclusi dallo split
  deterministico, nessuno di essi ricade nel file di capitolo.
- Nessun elenco di riferimenti bibliografici e' riportato nel `testo_integrale`
  della riga: la NOTE della clausola 1 cita il Regolamento (UE) n. 910/2014
  [i.1] per il suo contenuto normativo (gli strumenti giuridici supportati),
  non come voce di bibliografia.

## Oggetti giuridici: nessuno valorizzato (dubbio di classificazione aperto)

La riga NON porta `oggetti_giuridici`, per coerenza con il gemello ETSI EN 319
122-1 cap01 (stessa NOTE, stesso blocco AdES) e con tutte le clausole di
"Scope" delle fonti ETSI gia' censite, nessuna delle quali valorizza l'attributo:
la clausola e' una dichiarazione di perimetro, non una disposizione che si
applica a un oggetto giuridico determinato, e l'enumerazione della NOTE e'
l'elenco degli strumenti che il documento "aims at supporting", non la
qualificazione giuridica di cio' che il documento disciplina.
DUBBIO DI CLASSIFICAZIONE APERTO per la revisione umana: la NOTE nomina
letteralmente "electronic signatures, advanced electronic signatures, qualified
electronic signatures, electronic seals, advanced electronic seals, and
qualified electronic seals as per Regulation (EU) No 910/2014 [i.1]", cioe' sei
voci della tassonomia eIDAS del censimento (firma elettronica, firma
elettronica avanzata, firma elettronica qualificata, sigillo elettronico,
sigillo elettronico avanzato, sigillo elettronico qualificato). Se la revisione
preferisse la lettura letterale della regola "valorizzare `oggetti_giuridici`
quando il testo nomina un oggetto della tassonomia eIDAS", la riga andrebbe
integrata con quelle sei voci; il testo normativo non cambierebbe.

## Rinvii demandati alla fase 6 (nessuna relazione creata qui)

Il modulo ha una sola riga: non esiste alcuna coppia interna da collegare, e le
citazioni della clausola 1 puntano tutte fuori dal modulo. Nessuna relazione
verso altri capitoli di questa Fonte ne' verso altre fonti viene dichiarata
qui: la costruzione degli archi e' demandata alla sessione principale in fase 6
(ADR-0009), e i bersagli di unita' indivise (partizioni) sono derivati dal
livello strutturale (ADR-0012). Citazioni annotate, da risolvere in fase 6:

- "XML digital signatures [1]" (W3C Recommendation, XML Signature Syntax and
  Processing 1.1): fonte esterna, riferimento bibliografico [1] della clausola
  2.1.
- "ETSI EN 319 102-1 [i.6]" (procedure di creazione e convalida delle firme
  AdES, esplicitamente fuori perimetro): fonte esterna gia' censita.
- "ETSI TR 119 100 [i.11]" (guida all'uso degli standard per la creazione e la
  convalida delle firme): fonte esterna, informativa.
- "Regulation (EU) No 910/2014 [i.1]" (quadro regolatorio sostenuto): fonte
  esterna gia' censita (eIDAS).
- Internamente alla Fonte: la clausola 1 dichiara il perimetro di cui le
  clausole 4-6 (cap03-cap07) e l'Annex A normativo (cap08) danno il contenuto
  prescrittivo. Un rinvio generico al perimetro non e' un bersaglio tipizzabile
  su una singola clausola: nessun arco dichiarato, neanche in fase 6, salvo
  riscontro testuale puntuale.
- Nota ADR-0012: "clausola 1 (Scope)" e' una clausola di primo livello, quindi
  la sua unita' indivisa **e'** la riga stessa: `partizioni_di` non genera
  alcuna partizione per questo riferimento, e una citazione di "clause 1" da
  un altro modulo punta direttamente a questo nodo.

## Conteggio di copertura di questo capitolo

1 item di indice, 1 riga: 0 obblighi + 1 principio.
"""

RIGHE_OBBLIGHI: list[dict] = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 1 (Scope)",
        "testo": (
            "Il documento specifica le firme digitali XAdES, costruite sulle firme digitali XML [1] "
            "mediante incorporazione di proprieta' qualificanti firmate e non firmate che soddisfano "
            "requisiti comuni (es. la validita' a lungo termine delle firme) in diversi casi d'uso, e ne "
            "specifica le definizioni di XML Schema nonche' i meccanismi per incorporarle nelle firme "
            "XAdES. Specifica inoltre i formati delle firme XAdES baseline - le funzionalita' di base "
            "necessarie per un'ampia gamma di casi d'uso aziendali e governativi di procedure e "
            "comunicazioni elettroniche, applicabili a comunita' diverse quando c'e' una chiara esigenza "
            "di interoperabilita' delle firme digitali usate nei documenti elettronici - e definisce "
            "quattro livelli di firma XAdES baseline con requisiti incrementali per mantenere la validita' "
            "delle firme a lungo termine, in modo che un livello soddisfi sempre tutti i requisiti dei "
            "livelli inferiori, ciascuno con la presenza richiesta di certe proprieta' qualificanti XAdES "
            "profilate per ridurre il piu' possibile l'opzionalita'. Restano fuori perimetro le procedure "
            "di creazione, augmentation e convalida delle firme XAdES, specificate in ETSI EN 319 102-1 "
            "[i.6] (la guida su creazione, augmentation e convalida, incluso l'uso delle diverse "
            "proprieta' definite nel documento, e' fornita in ETSI TR 119 100 [i.11]); il documento mira "
            "a supportare le firme elettroniche in diversi quadri regolatori e la NOTE precisa che, "
            "specificamente ma non esclusivamente, le firme XAdES qui specificate mirano a supportare "
            "firme elettroniche, firme elettroniche avanzate, firme elettroniche qualificate, sigilli "
            "elettronici, sigilli elettronici avanzati e sigilli elettronici qualificati ai sensi del "
            "Regolamento (UE) n. 910/2014 [i.1]. Clausola di perimetro, non una prescrizione: nessun "
            "soggetto obbligato."
        ),
        "testo_integrale": (
            "1 Scope: The present document specifies XAdES digital signatures. XAdES signatures build on "
            "XML digital signatures [1], by incorporation of signed and unsigned qualifying properties, "
            "which fulfil certain common requirements (such as the long term validity of digital "
            "signatures, for instance) in a number of use cases.\n"
            "\n"
            "The present document specifies XML Schema definitions for the aforementioned qualifying "
            "properties as well as mechanisms for incorporating them into XAdES signatures.\n"
            "\n"
            "The present document specifies formats for XAdES baseline signatures, which provide the basic "
            "features necessary for a wide range of business and governmental use cases for electronic "
            "procedures and communications to be applicable to a wide range of communities when there is a "
            "clear need for interoperability of digital signatures used in electronic documents.\n"
            "\n"
            "The present document defines four levels of XAdES baseline signatures addressing incremental "
            "requirements to maintain the validity of the signatures over the long term, in a way that a "
            "certain level always addresses all the requirements addressed at levels that are below it. "
            "Each level requires the presence of certain XAdES qualifying properties, suitably profiled "
            "for reducing the optionality as much as possible.\n"
            "\n"
            "Procedures for creation, augmentation, and validation of XAdES digital signatures are out of "
            "scope and specified in ETSI EN 319 102-1 [i.6]. Guidance on creation, augmentation and "
            "validation of XAdES digital signatures including the usage of the different properties "
            "defined in the present document is provided in ETSI TR 119 100 [i.11].\n"
            "\n"
            "The present document aims at supporting electronic signatures in different regulatory "
            "frameworks.\n"
            "NOTE: Specifically but not exclusively, XAdES digital signatures specified in the present "
            "document aim at supporting electronic signatures, advanced electronic signatures, qualified "
            "electronic signatures, electronic seals, advanced electronic seals, and qualified electronic "
            "seals as per Regulation (EU) No 910/2014 [i.1]."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 1 (Scope)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Nessuna relazione: il modulo ha una sola riga e tutte le sue citazioni
# (W3C XML Signature [1], ETSI EN 319 102-1 [i.6], ETSI TR 119 100 [i.11],
# Regolamento (UE) n. 910/2014 [i.1]) puntano fuori dal modulo. Il
# collegamento e' demandato alla Fase 6 della sessione principale (ADR-0009).
RELAZIONI: list[dict] = []
