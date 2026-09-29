"""ETSI EN 319 122-1 V1.3.1 (2023-06) - Electronic Signatures and
Infrastructures (ESI); CAdES digital signatures; Part 1: Building blocks and
CAdES baseline signatures. Blocco B (famiglia AdES del lotto 2). Capitolo 1:
clausola 1 (Scope), clausola 2 (References, esclusa), clausola 3 (Definition
of terms, symbols and abbreviations: 3.1 Terms, 3.2 Symbols, 3.3
Abbreviations). Conteggio di questo capitolo: 0 Obblighi, 4 Principi, 4 item
di indice, 0 relazioni. Questo modulo NON tocca app/seed.py: gli id sono
risolti per riferimento dalla sessione principale tramite
app/seed_data/lib.py, e le relazioni verso altri capitoli della stessa fonte
o verso altre fonti le costruisce sempre la sessione principale (fase 6,
ADR-0009).

Provenienza del testo: app/.source_cache/etsi_319_122/cap01.txt (280 righe),
estratto dal PDF ufficiale ETSI deliver
https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf
versione 01.03.01_60, formato "PDF ETSI deliver (pdftotext -layout)",
data_fetch 2026-09-29T12:56:34Z, sha256 del PDF raw
e99e76e519d9bd8e1410775bccedb1a588021e5e7c705c9fcc1f91c6a6227c21 (tutti i
valori da app/.source_cache/etsi_319_122/provenance.json). Il file di
capitolo inizia alla riga "1 Scope" e termina con la clausola 3.3
(Abbreviations): front matter, Contents, Foreword e History sono gia' esclusi
dallo split deterministico (manifest.json), e la clausola 4 (General syntax)
apre il capitolo successivo (cap02).

Perimetro del capitolo — clausole 1-3, capitolo di cornice (nessuna
prescrizione con destinatario; tutti i "shall" di questo standard vivono
dalle clausole 4 in poi):

- Clausola 1 (Scope) -> 1 Principio "scopo/ambito di applicazione",
  riferimento "clausola 1 (Scope)". Contiene, in sei paragrafi piu' una
  NOTE: (a) l'oggetto (specifica delle firme digitali CAdES, costruite sulle
  firme CMS [7] incorporando attributi firmati e non firmati che soddisfano
  requisiti comuni come la validita' a lungo termine); (b) l'oggetto
  tecnico (definizioni ASN.1 di quegli attributi e loro uso nelle firme
  CAdES); (c) i formati delle firme CAdES baseline e la loro finalita'
  (casi d'uso aziendali e governativi, interoperabilita' fra comunita'
  diverse); (d) i quattro livelli di firma baseline con requisiti
  incrementali (ogni livello copre i requisiti dei livelli inferiori, ogni
  livello richiede certi attributi CAdES profilati per ridurre l'opzionalita'
  al minimo); (e) il fuori perimetro (procedure di creazione, augmentation e
  convalida, demandate a ETSI EN 319 102-1 [i.5]) e la guida esterna (ETSI
  TR 119 100 [i.4]); (f) la finalita' di supporto alle firme digitali nei
  diversi quadri regolatori, con la NOTE che la specifica al Regolamento
  (UE) n. 910/2014 [i.13] ("Specifically, but not exclusively": firme
  elettroniche, avanzate e qualificate, sigilli elettronici, avanzati e
  qualificati). Nessun Obbligo: il testo e' interamente descrittivo ("The
  present document specifies/defines/aims at"), non impone un comportamento a
  un soggetto identificabile e non contiene alcun verbo prescrittivo con
  destinatario. La NOTE e' assorbita nel `testo_integrale` perche' non e' un
  mero rimando bibliografico: precisa il perimetro funzionale del documento.
- Clausola 2 (References: 2.1 Normative references, 2.2 Informative
  references) -> NESSUN nodo e NESSUN item di indice. E' bibliografia e
  paratesto puro: 19 riferimenti normativi [1]-[19] e 22 informativi
  [i.1]-[i.22], con le NOTE ETSI di obsolescenza ("NOTE: Obsoletes IETF RFC
  3280"), le due voci segnaposto "[i.10] Void." e "[i.16] Void.", e i
  paragrafi redazionali uniformi a tutti i deliverable ETSI (riferimenti
  specifici identificati da data di pubblicazione e/o numero di edizione o
  versione e non specifici; per i riferimenti specifici vale solo la versione
  citata, per i non specifici l'ultima versione del documento richiamato,
  emendamenti inclusi; i documenti non reperibili si cercano su
  https://docbox.etsi.org/Reference; NOTE sull'irresponsabilita' ETSI in
  ordine alla validita' a lungo termine degli hyperlink). Nessuno di questi
  elementi e' un'unita' di prescrizione, e nessun altro documento puo'
  rinviare a una voce di bibliografia come a una clausola di questo standard.
  Stesso trattamento gia' riservato alla clausola 2 delle fonti ETSI censite
  (ETSI EN 319 102-1, EN 319 401, TS 119 451/119 461/119 612).
- Clausola 3 (Definition of terms, symbols and abbreviations) -> NESSUN nodo
  e NESSUN item di indice: intestazione di raggruppamento, priva di contenuto
  proprio oltre il titolo e le tre sottoclausole 3.1-3.3.
- Clausola 3.1 (Terms) -> 1 Principio "definitorio". Glossario piatto, senza
  struttura a lettere o numeri propri: 13 termini definiti, riportati tutti
  verbatim in `testo_integrale` nell'ordine alfabetico del testo ufficiale
  (CAdES signature, Certificate Revocation List (CRL), digital signature,
  digital signature value, electronic time-stamp, Legacy CAdES 101 733
  signature, Legacy CAdES baseline signature, Legacy CAdES signature,
  signature augmentation policy, signature creation policy, signature
  policy, signature validation policy, validation data), piu' la frase di
  rinvio iniziale ai termini gia' dati in ETSI TR 119 001 [i.3] e la NOTE su
  electronic time-stamp (identifica il campo timeStampToken dell'elemento
  TimeStampResp in IETF RFC 3161 [4]: aggiunge contenuto interpretativo
  sostanziale al termine, quindi e' mantenuta). Le NOTEs di obsolescenza e i
  riferimenti bibliografici interni alle singole definizioni (ETSI TS 101
  733 [1], ETSI TS 103 173 [i.1], ETSI EN 319 122-2 [i.6]) restano dentro il
  `testo_integrale` come parte integrante della definizione, senza generare
  relazione.
- Clausola 3.2 (Symbols) -> 1 Principio "definitorio" con `testo_integrale`
  "3.2 Symbols: Void.". Scelta di modellazione esplicita: la clausola dichiara
  che il documento non definisce simboli, quindi non ha contenuto oltre il
  segnaposto di redazione, e in questa famiglia di fonti esistono entrambe le
  convenzioni (ETSI EN 319 401 e EN 319 421 la escludono, ETSI TS 119 432,
  TS 119 612, EN 319 411-1 ed EN 319 102-1 la includono con il solo
  segnaposto). Qui si include: ADR-0007 vieta ogni discrimine di rilevanza in
  estrazione, e un item di indice in piu' per una sottoclavola numerata reale
  e' la scelta conservativa (l'omissione sarebbe un giudizio di merito non
  coperto dal criterio).
- Clausola 3.3 (Abbreviations) -> 1 Principio "definitorio". Tre
  abbreviazioni (ATSv2, ATSv3, MIME) con la frase di rinvio iniziale alle
  abbreviazioni gia' date in ETSI TR 119 001 [i.3]. La conversione
  PDF->testo rende la tabella come coppia etichetta/forma estesa sulla stessa
  riga con colonne allineate a spazi: in `testo_integrale` le coppie sono
  ricostruite nella forma esplicita "ETICHETTA: Forma estesa.", una per riga,
  nell'ordine del testo, senza perdere alcun valore (stessa convenzione gia'
  usata per la clausola 3.3 di ETSI EN 319 401 / 319 421 / 319 102-1). Le due
  NOTEs di rinvio interno (ATSv2 -> "clause A.2.4" dell'Annex A normativo;
  ATSv3 -> "clause 5.5.3") sono mantenute: delimitano il significato delle
  abbreviazioni e sono rinvii strutturali, non bibliografia.

Granularita' e convenzione dei riferimenti. "Un item di indice per voce" e'
letto come una riga e un item di indice per ciascuna delle sottoclausole
numerate della clausola 3 (3.1, 3.2, 3.3), non un nodo per singolo termine o
abbreviazione: e' la convenzione costante delle 9 fonti ETSI gia' censite
(un glossario alfabetico piatto non ha item di indice propri; spezzarlo in 13
item fittizi attribuirebbe a questa fonte una granularita' che il testo non
ha, e romperebbe i rinvii cross-fonte verso "clausola 3.1"). Anche i
`riferimento` seguono quella convenzione, senza prefisso di parte ("clausola
1 (Scope)", non "Parte 1: clausola 1 (Scope)"), per restare omogenei ai
moduli fratelli della stessa Fonte; i termini e le abbreviazioni sono
comunque indicizzati dal full-text su `testo_integrale`.

Esclusioni: front matter, pagine di copertina, Contents, Foreword (inclusa la
frase di partizione del deliverable "The present document is part 1 of a
multi-part deliverable ..." - paratesto, non norma), History, il paratesto di
pagina ripetuto dalla conversione PDF (footer "ETSI", intestazione
"ETSI EN 319 122-1 V1.3.1 (2023-06)", numeri di pagina), l'intera clausola 2
(vedi sopra) e l'intestazione della clausola 3.

Rinvii demandati alla fase 6 (nessuna relazione dichiarata in questo modulo,
che non contiene rinvii interni fra le proprie righe): ETSI EN 319 102-1
[i.5] e ETSI TR 119 100 [i.4] (procedure e guida di creazione, augmentation e
convalida, esplicitamente fuori perimetro), Regolamento (UE) n. 910/2014
[i.13] (quadro regolatorio sostenuto), ETSI TR 119 001 [i.3] (termini e
abbreviazioni richiamati dalle clausole 3.1 e 3.3), ETSI EN 319 122-2 [i.6]
(parte 2 del deliverable, richiamata dalla definizione di CAdES signature),
ETSI TS 101 733 [1] e ETSI TS 103 173 [i.1] (famiglie legacy), IETF RFC 3161
[4] (protocollo di marca temporale citato nella NOTE di electronic
time-stamp); internamente alla Fonte, "clause A.2.4" (Annex A normativo,
cap05) e "clause 5.5.3" (attributo archive-time-stamp-v3, cap03), citate
letteralmente nelle NOTEs della clausola 3.3, e le clausole 4-6 (cap02-cap04)
che danno contenuto prescrittivo al perimetro qui dichiarato.

Conteggio di copertura di questo capitolo: 4 item di indice, 4 righe (0
obblighi + 4 principi).
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 1 (Scope)",
        "testo": (
            "Il documento specifica le firme digitali CAdES, costruite sulle firme CMS "
            "[7] mediante incorporazione di attributi firmati e non firmati che soddisfano "
            "requisiti comuni (es. la validita' a lungo termine delle firme) in diversi casi "
            "d'uso, e specifica le definizioni ASN.1 di tali attributi e il loro uso "
            "nell'incorporarli alle firme CAdES. Specifica inoltre i formati delle firme "
            "CAdES baseline, che forniscono le funzionalita' di base necessarie per un'ampia "
            "gamma di casi d'uso aziendali e governativi di procedure e comunicazioni "
            "elettroniche, applicabili a comunita' diverse quando c'e' una chiara esigenza "
            "di interoperabilita' delle firme digitali usate nei documenti elettronici, e "
            "definisce quattro livelli di firma CAdES baseline con requisiti incrementali "
            "per mantenere la validita' delle firme a lungo termine, in modo che un livello "
            "soddisfi sempre tutti i requisiti dei livelli inferiori; ogni livello richiede "
            "la presenza di certi attributi CAdES, profilati per ridurre il piu' possibile "
            "l'opzionalita'. Fuori perimetro, e specificate in ETSI EN 319 102-1 [i.5], le "
            "procedure di creazione, augmentation e convalida delle firme CAdES; la guida "
            "su creazione, augmentation e convalida, incluso l'uso delle diverse proprieta' "
            "definite nel documento, e' fornita in ETSI TR 119 100 [i.4]. Il documento mira "
            "a supportare le firme digitali in diversi quadri regolatori: la NOTE precisa "
            "che, specificamente ma non esclusivamente, le firme CAdES qui specificate "
            "mirano a supportare firme elettroniche, firme elettroniche avanzate, firme "
            "elettroniche qualificate, sigilli elettronici, sigilli elettronici avanzati e "
            "sigilli elettronici qualificati ai sensi del Regolamento (UE) n. 910/2014 "
            "[i.13]. Clausola di perimetro, non una prescrizione: nessun soggetto obbligato."
        ),
        "testo_integrale": (
            "1 Scope: The present document specifies CAdES digital signatures. CAdES "
            "signatures are built on CMS signatures [7], by incorporation of signed and "
            "unsigned attributes, which fulfil certain common requirements (such as the long "
            "term validity of digital signatures, for instance) in a number of use cases.\n"
            "\n"
            "The present document specifies the ASN.1 definitions for the aforementioned "
            "attributes as well as their usage when incorporating them to CAdES signatures.\n"
            "\n"
            "The present document specifies formats for CAdES baseline signatures, which "
            "provide the basic features necessary for a wide range of business and "
            "governmental use cases for electronic procedures and communications to be "
            "applicable to a wide range of communities when there is a clear need for "
            "interoperability of digital signatures used in electronic documents.\n"
            "\n"
            "The present document defines four levels of CAdES baseline signatures "
            "addressing incremental requirements to maintain the validity of the signatures "
            "over the long term, in a way that a certain level always addresses all the "
            "requirements addressed at levels that are below it. Each level requires the "
            "presence of certain CAdES attributes, suitably profiled for reducing the "
            "optionality as much as possible.\n"
            "\n"
            "Procedures for creation, augmentation and validation of CAdES digital "
            "signatures are out of scope and specified in ETSI EN 319 102-1 [i.5]. Guidance "
            "on creation, augmentation and validation of CAdES digital signatures including "
            "the usage of the different properties defined in the present document is "
            "provided in ETSI TR 119 100 [i.4].\n"
            "\n"
            "The present document aims at supporting digital signatures in different "
            "regulatory frameworks.\n"
            "NOTE: Specifically, but not exclusively, CAdES digital signatures specified in "
            "the present document aim at supporting electronic signatures, advanced "
            "electronic signatures, qualified electronic signatures, electronic seals, "
            "advanced electronic seals, and qualified electronic seals as per Regulation "
            "(EU) No 910/2014 [i.13]."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.1 (Terms)",
        "testo": (
            "La clausola definisce 13 termini usati dal documento, oltre al rinvio generale "
            "ai termini gia' dati in ETSI TR 119 001 [i.3]: (i) firme e famiglie legacy - "
            "'CAdES signature' (firma digitale che soddisfa i requisiti della parte 1 o della "
            "parte 2 di ETSI EN 319 122), 'Legacy CAdES 101 733 signature' (generata secondo "
            "ETSI TS 101 733), 'Legacy CAdES baseline signature' (generata secondo ETSI TS "
            "103 173), 'Legacy CAdES signature' (l'una o l'altra); (ii) firma e dati di "
            "convalida - 'digital signature' (dati aggiunti a un'unita' di dati o "
            "trasformazione crittografica che consente al destinatario di provarne origine e "
            "integrita' e di proteggerla dalla falsificazione, anche da parte del "
            "destinatario), 'digital signature value' (risultato di quella trasformazione), "
            "'certificate revocation list (CRL)' (lista firmata di certificati di chiave "
            "pubblica non piu' considerati validi dall'emittente), 'validation data' (dati "
            "usati per convalidare una firma digitale); (iii) tempo - 'electronic "
            "time-stamp' (dati in forma elettronica che legano altri dati elettronici a un "
            "istante, provando che quei dati esistevano a quel tempo; NOTE: nel protocollo "
            "IETF RFC 3161 [4] la marca temporale elettronica e' il campo timeStampToken "
            "dell'elemento TimeStampResp, cioe' la risposta della TSA al client "
            "richiedente); (iv) politiche di firma - 'signature creation policy', 'signature "
            "augmentation policy' e 'signature validation policy' (insiemi di regole, "
            "applicabili a una o piu' firme digitali, che definiscono i requisiti tecnici e "
            "procedurali rispettivamente per la creazione, l'augmentation e la convalida al "
            "fine di soddisfare una particolare esigenza di business e al ricorrere dei "
            "quali le firme possono essere considerate conformi, rispettivamente valide), e "
            "'signature policy' (una qualunque di esse o loro combinazione, applicabile alla "
            "stessa firma o insieme di firme)."
        ),
        "testo_integrale": (
            "3.1 Terms: For the purposes of the present document, the terms given in ETSI TR "
            "119 001 [i.3] and the following apply:\n"
            "CAdES signature: digital signature that satisfies the requirements specified "
            "within ETSI EN 319 122 part 1 (the present document) or part 2 [i.6]\n"
            "Certificate Revocation List (CRL): signed list indicating a set of public key "
            "certificates that are no longer considered valid by the certificate issuer\n"
            "digital signature: data appended to, or cryptographic transformation (see "
            "cryptography) of a data unit that allows a recipient of the data unit to prove "
            "the source and integrity of the data unit and protect against forgery e.g. by "
            "the recipient\n"
            "digital signature value: result of the cryptographic transformation of a data "
            "unit that allows a recipient of the data unit to prove the source and integrity "
            "of the data unit and protect against forgery e.g. by the recipient\n"
            "electronic time-stamp: data in electronic form which binds other electronic "
            "data to a particular time establishing evidence that these data existed at "
            "that time\n"
            "NOTE: In the case of IETF RFC 3161 [4] protocol, the electronic time-stamp is "
            "referring to the timeStampToken field within the TimeStampResp element (the "
            "TSA's response returned to the requesting client).\n"
            "Legacy CAdES 101 733 signature: digital signature generated according to ETSI "
            "TS 101 733 [1]\n"
            "Legacy CAdES baseline signature: digital signature generated according to ETSI "
            "TS 103 173 [i.1]\n"
            "Legacy CAdES signature: legacy CAdES 101 733 signature or a legacy CAdES "
            "baseline signature\n"
            "signature augmentation policy: set of rules, applicable to one or more digital "
            "signatures, that defines the technical and procedural requirements for their "
            "augmentation, in order to meet a particular business need, and under which the "
            "digital signature(s) can be determined to be conformant\n"
            "signature creation policy: set of rules, applicable to one or more digital "
            "signatures, that defines the technical and procedural requirements for their "
            "creation, in order to meet a particular business need, and under which the "
            "digital signature(s) can be determined to be conformant\n"
            "signature policy: signature creation policy, signature augmentation policy, "
            "signature validation policy or any combination thereof, applicable to the same "
            "signature or set of signatures\n"
            "signature validation policy: set of rules, applicable to one or more digital "
            "signatures, that defines the technical and procedural requirements for their "
            "validation, in order to meet a particular business need, and under which the "
            "digital signature(s) can be determined to be valid\n"
            "validation data: data that is used to validate a digital signature"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.2 (Symbols)",
        "testo": (
            "La clausola non definisce alcun simbolo: il testo ufficiale della clausola 3.2 "
            "(Symbols) e' integralmente 'Void.', cioe' dichiara che per gli scopi del "
            "documento non si applica alcun simbolo. Nessun contenuto oltre il segnaposto di "
            "redazione, ma la sottoclavola numerata e' censita per copertura completa "
            "dell'intera clausola 3."
        ),
        "testo_integrale": "3.2 Symbols: Void.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.3 (Abbreviations)",
        "testo": (
            "La clausola elenca, oltre al rinvio generale alle abbreviazioni gia' date in "
            "ETSI TR 119 001 [i.3], tre abbreviazioni usate dal documento: ATSv2 "
            "(archive-time-stamp attribute; NOTE: come definito nella clausola A.2.4), ATSv3 "
            "(archive-time-stamp-v3 attribute; NOTE: come definito nella clausola 5.5.3) e "
            "MIME (Multipurpose Internet Mail Extensions)."
        ),
        "testo_integrale": (
            "3.3 Abbreviations: For the purposes of the present document, the abbreviations "
            "given in ETSI TR 119 001 [i.3] and the following apply:\n"
            "ATSv2: archive-time-stamp attribute\n"
            "NOTE: As defined in clause A.2.4.\n"
            "ATSv3: archive-time-stamp-v3 attribute\n"
            "NOTE: As defined in clause 5.5.3.\n"
            "MIME: Multipurpose Internet Mail Extensions"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 1 (Scope)",
    "clausola 3.1 (Terms)",
    "clausola 3.2 (Symbols)",
    "clausola 3.3 (Abbreviations)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
