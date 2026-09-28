"""ETSI TS 119 312 V2.1.1 (2026-06) - Electronic Signatures and Trust
Infrastructures (ESI); Cryptographic Suites. Fonte ETSI (conteggio di
Obblighi/Principi di questo capitolo: 1 Obbligo, 5 Principi). Capitolo 1:
clausole 1 (Scope), 2 (References), 3 (Definition of terms, symbols,
abbreviations and notations: 3.1 Terms, 3.2 Symbols, 3.3 Abbreviations, 3.4
Notations), 4 (Use of ECCG Agreed Mechanisms and Maintenance of the present
document). Testo ufficiale in app/.source_cache/etsi_119_312/cap01.txt
(451 righe); manifest di split in
app/.source_cache/etsi_119_312/manifest.json. Questo modulo NON tocca
app/seed.py: gli id sono risolti per riferimento dalla sessione principale
tramite app/seed_data/lib.py.

Modellazione (ADR-0007), stesso criterio gia' applicato agli altri standard
tecnici ETSI censiti (ETSI EN 319 401, ETSI TS 119 461, ETSI TS 119 431-1,
ETSI EN 319 421): un nodo per ogni clausola/sottoclavola numerata con
contenuto proprio, nessun discrimine di rilevanza. Scelte voce per voce:

- Clausola 1 (Scope) -> 1 Principio "scopo/ambito di applicazione". Perimetro
  in senso proprio: elenca i servizi coperti (firme digitali, marche
  temporali, recapito elettronico certificato, archiviazione elettronica,
  registri elettronici e relativi certificati), dichiara la dipendenza da
  ECCG Agreed Mechanisms [14], l'inclusione della transizione PQC, e
  l'assunzione di fondo usata da tutte le tabelle di date del documento (il
  periodo di validita' tipico dei certificati di end-entity emessi dai
  prestatori di servizi fiduciari e' di tre anni). Entrambe le NOTE ufficiali
  sono mantenute in `testo_integrale`: delimitano il perimetro (cosa e'
  demandato al documento di migrazione post-quantistica - NOTE 1 - e cosa il
  documento NON copre oggi: EUDI-Wallet ex art. 5a eIDAS, servizi di
  conservazione ex artt. 34 e 40, recapito certificato ex artt. 43 e 44 -
  NOTE 2), quindi non sono bibliografia decorativa.
- Clausola 2 (References: 2.1 Normative references, 2.2 Informative
  references) -> NESSUN nodo e NESSUN item di indice, come da contratto
  assegnato: e' bibliografia/paratesto puro (29 riferimenti normativi [1]-[29]
  e 34 informativi [i.1]-[i.34], con le sole regole redazionali ETSI su
  riferimenti specifici/non specifici e voci "Void"). Stesso trattamento gia'
  riservato alla clausola 2 di ETSI EN 319 401 / ETSI TS 119 461.
- Clausola 3, intestazione ("Definition of terms, symbols, abbreviations and
  notations") -> NESSUN nodo e NESSUN item di indice: clausola di puro
  raggruppamento, non contiene nulla oltre il titolo e il rimando alle
  sottoclavole 3.1-3.4 (criterio esplicito del contratto di estrazione).
- Clausola 3.1 (Terms) -> 1 Principio "definitorio" riassuntivo, NON un nodo
  per singolo termine: la clausola e' un glossario alfabetico piatto senza
  struttura a lettere/numeri propria, quindi 13 nodi sarebbero 13 item di
  indice fittizi per un'unica clausola (stesso criterio gia' applicato alla
  clausola 3.1 di ETSI EN 319 401 / 119 461 / 319 421). I 13 termini definiti
  (AdES signature, CAdES signature, cryptographic suite, (digital) signature,
  hash function, hybrid cryptographic scheme, legacy mechanism, PAdES
  signature, recommended mechanism, security level, signature policy,
  signature scheme, XAdES signature) sono riportati verbatim in
  `testo_integrale`, ciascuno sulla propria riga (una voce di glossario per
  riga, come nel testo ufficiale), con le tre NOTE di clausola assorbite
  (le due NOTE "As defined in ECCG Agreed Cryptographic Mechanisms [14]" su
  legacy/recommended mechanism e la NOTE 2 su security level) perche'
  attribuiscono la fonte delle definizioni, cioe' il documento ECCG su cui
  poggia l'intero standard.
- Clausola 3.2 (Symbols) -> 1 Principio "definitorio": a differenza di altri
  standard ETSI censiti (dove 3.2 e' un "Void." puro), qui la clausola ha
  contenuto proprio - definisce il simbolo "FR" (Identifier for Elliptic
  Curves defined by ANSSI), usato dal capitolo delle suite di firma. Un solo
  item di indice, come da contratto ("anche le notazioni vanno censite").
- Clausola 3.3 (Abbreviations) -> 1 Principio "definitorio" riassuntivo: 42
  abbreviazioni (ACM ... XMSS), piu' la NOTE su ESI ("A Technical Committee of
  ETSI"). La tabella a due colonne del testo ufficiale arriva dalla
  conversione PDF->testo gia' come coppie etichetta/forma estesa sulla stessa
  riga (nessun disallineamento da ricostruire); in `testo_integrale` ogni
  coppia e' riportata su una riga propria, esattamente nell'ordine
  alfabetico del testo.
- Clausola 3.4 (Notations) -> 1 Principio "definitorio". NODO CRUCIALE per
  l'intero documento: definisce le sole quattro notazioni con cui i capitoli
  successivi (cap02-cap04) marcano l'idoneita' dei meccanismi - "L" (legacy,
  dismissione 31.12.2034, prorogabile), "L[yyyy]" (dismissione non oltre
  31.12.yyyy), "L[yyyy+]" (dismissione 31.12.yyyy, prorogabile), "R"
  (raccomandato, nessuna data di fine) - e la regola che genera tutte le date
  del documento: alle date di fine di [14] e' aggiunto un default di tre
  anni, per riflettere il periodo di validita' tipico dei certificati di
  end-entity assunto nello Scope (con l'equivalenza L = L[2034+]).
- Clausola 4 (Use of ECCG Agreed Mechanisms and Maintenance of the present
  document) -> 1 OBBLIGO "tecnico/sicurezza", destinatario QTSP/gestore
  (obbligato): la clausola contiene la raccomandazione normativa del
  documento ("only ECCG recommended mechanisms and key sizes or cryptographic
  suites using these cryptographic mechanisms and key sizes should be used to
  generate new signatures and seals (including certificate signatures)",
  con l'eccezione dei meccanismi legacy ammessi per interoperabilita' con
  infrastrutture esistenti e finche' restano "agreed"), che ricade nella
  regola di classificazione del contratto ("elenchi di raccomandazioni
  tecniche -> Obbligo tecnico/sicurezza, destinatario QTSP/gestore"). I
  paragrafi restanti della stessa clausola (delega a [14] della valutazione
  di sicurezza, ripetizione della classificazione per comodita' del lettore,
  manutenzione sincronizzata con i cicli ECCG, revisione in caso di nuovi
  attacchi) sono descrittivi e riguardano ETSI/l'ECCG, non un destinatario
  obbligato; restano comunque nella stessa riga perche' la clausola 4 non ha
  sottoclavole numerate e l'item di indice "clausola 4 (...) " deve essere
  coperto da esattamente una riga (guardia `verifica_copertura`).

RELAZIONI: vuota per contratto - nessun collegamento verso eIDAS o altri
standard ETSI citati e' costruito qui; i collegamenti cross-fonte li
costruisce la sessione principale.

Note sulla ricostruzione del verbatim: le righe di intestazione/piè di pagina
della conversione PDF ("ETSI", "N  ETSI TS 119 312 V2.1.1 (2026-06)") sono
state rimosse e le righe spezzate a 110 colonne sono state ricucite in
paragrafi. Unico valore ricostruito dal contesto: nella NOTE 1 di clausola 3.1
il PDF riporta "2100 operations" perche' la conversione ha perso l'esponente
del logaritmo in base 2; il valore e' reso come "2^100 operations" (100 bit di
sicurezza = 2^100 operazioni), coerente con la definizione di "security level"
nella stessa clausola.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": (
            "clausola 4 (Use of ECCG Agreed Mechanisms and Maintenance of the present document)"
        ),
        "testo": (
            "La valutazione della sicurezza degli schemi crittografici sottostanti e' delegata al documento "
            "ECCG Agreed Mechanisms [14], per evitare duplicazione di sforzo; l'ECCG distingue meccanismi "
            "'legacy' (schemi e scelte di parametri largamente diffusi ma non rappresentativi dello stato "
            "dell'arte) e meccanismi 'recommended' (schemi e parametri rappresentativi dello stato dell'arte), "
            "e il documento usa le due nozioni nello stesso senso di [14]. In generale, per generare nuove "
            "firme e sigilli (incluse le firme sui certificati) dovrebbero essere usati solo meccanismi e "
            "dimensioni di chiave raccomandati ECCG, o suite crittografiche che usano tali meccanismi e "
            "dimensioni di chiave; i meccanismi legacy ECCG possono tuttavia essere ancora usati per questo "
            "scopo quando cio' e' necessario per garantire l'interoperabilita' con infrastrutture esistenti e "
            "finche' restano meccanismi concordati (agreed). La classificazione legacy/recommended e' ripetuta "
            "nel documento per comodita' del lettore. Le attivita' di manutenzione seguono la procedura di "
            "manutenzione di ECCG Agreed Mechanisms [14], con revisioni su base regolare sincronizzate con i "
            "cicli di pubblicazione ECCG; in caso di nuovi attacchi, se emergesse la necessita' immediata di "
            "rimuovere un algoritmo, una nuova revisione del documento sara' pubblicata appena possibile."
        ),
        "testo_integrale": (
            "4 Use of ECCG Agreed Mechanisms and Maintenance of the present document: In order to avoid "
            "duplicated effort, the assessment of the security of underlying cryptographic schemes is "
            "delegated to the ECCG document [14]. The ECCG Agreed Mechanisms distinguishes between legacy "
            "mechanisms (schemes and parameter selections which may enjoy wide deployment, but do not "
            "represent the current state of the art in cryptography) and recommended mechanisms (schemes and "
            "parameters which do represent the current state of the art in cryptography). The present document "
            "uses the notion of \"recommended\" and \"legacy\" primitives in the same way as in [14]. In "
            "general, only ECCG recommended mechanisms and key sizes or cryptographic suites using these "
            "cryptographic mechanisms and key sizes should be used to generate new signatures and seals "
            "(including certificate signatures). ECCG legacy mechanisms may, however, still be used for this "
            "purpose when this is necessary to ensure interoperability with existing infrastructures as long "
            "as they remain agreed. For the reader's convenience, the classification of mechanisms as legacy "
            "or recommended is repeated in the present document. The maintenance activities will follow the "
            "maintenance procedure of ECCG Agreed Mechanisms [14] with revisions on a regular basis "
            "synchronized with ECCG publication cycles. In the case of new attacks, the immediate need to "
            "remove an algorithm could arise, and a new revision of the present document will be published as "
            "soon as possible."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 1 (Scope)",
        "testo": (
            "Il documento elenca le suite crittografiche usate per la creazione e la validazione di firme "
            "digitali, marche temporali elettroniche, servizi elettronici di recapito certificato, "
            "archiviazione elettronica, registri elettronici (ledger) e relativi certificati, e si fonda sui "
            "meccanismi crittografici concordati dal European Cybersecurity Certification Group (ECCG) [14]. "
            "Incorpora requisiti per la transizione alla crittografia post-quantistica (PQC), inclusi schemi "
            "ibridi e la dismissione progressiva dei meccanismi legacy, in linea con la valutazione di "
            "sicurezza di ECCG Agreed Mechanisms e con il regolamento (UE) n. 910/2014 [i.12]. A differenza "
            "delle versioni precedenti, indica date di fine specifiche allineate alle fasi di migrazione PQC e "
            "assume che il periodo di validita' (tra notBefore e notAfter) dei certificati (qualificati) di "
            "end-entity emessi dai prestatori di servizi fiduciari sia tipicamente di tre anni. Il documento "
            "si concentra sull'interoperabilita' e non duplica le considerazioni di sicurezza di altri "
            "organismi di standardizzazione, agenzie di sicurezza o autorita' di vigilanza degli Stati membri: "
            "fornisce invece guida sulla selezione di suite crittografiche concrete che usano meccanismi "
            "concordati, per assicurare un livello di sicurezza elevato nelle suite raccomandate e aumentare "
            "l'interoperabilita' semplificando le scelte di progetto. Non esiste alcun requisito normativo "
            "sulla scelta tra le alternative di suite crittografiche indicate, ma per tutte valgono requisiti "
            "normativi di sicurezza e interoperabilita'. Fornisce inoltre guida su funzioni di hash, schemi di "
            "firma (digitali) e suite di firma (digitali) da usare con le strutture dati impiegate nel "
            "contesto delle firme e dei sigilli digitali, specificando per ciascuna struttura dati l'insieme "
            "di algoritmi da usare. NOTA 1: la pianificazione della migrazione, le fasi di transizione e le "
            "scadenze di conformita' per la transizione alla PQC saranno trattate nel documento di migrazione "
            "post-quantistica attualmente in preparazione, non nel presente documento, che fornisce "
            "classificazioni di idoneita' dei meccanismi (R/L) indipendenti dalle tempistiche di deployment. "
            "NOTA 2: la presente specifica tecnica e' notoriamente incompleta rispetto alle esigenze "
            "dell'EUDI-Wallet ex art. 5a del regolamento (UE) n. 910/2014 [i.12] e di alcuni servizi "
            "fiduciari, inclusi i servizi di conservazione ex artt. 34 e 40 e i servizi elettronici di "
            "recapito certificato ex artt. 43 e 44; un aggiornamento del documento e' gia' in preparazione."
        ),
        "testo_integrale": (
            "1 Scope: The present document lists cryptographic suites used for the creation and validation of "
            "digital signatures, electronic timestamps, electronic registered delivery services, electronic "
            "archiving, electronic ledgers and related certificates. The present document builds on the agreed "
            "cryptographic mechanisms from the European Cybersecurity Certification Group (ECCG) [14]. It "
            "incorporates requirements for the transition to Post-Quantum Cryptography (PQC), including hybrid "
            "cryptographic schemes and the phasing out of legacy mechanisms in accordance with the security "
            "assessment of ECCG Agreed Mechanisms and Regulation (EU) No 910/2014 [i.12]. In contrast to "
            "previous versions of the present document, specific end dates are provided and aligned with the "
            "PQC migration phases. The present document works on the assumption that the validity period (i.e. "
            "between notBefore and notAfter) of (qualified) end-entity certificates issued by trust services "
            "providers is typically three years. The present document focuses on interoperability issues and "
            "does not duplicate security considerations given by other standardization bodies, security "
            "agencies or supervisory authorities of the Member States. It instead provides guidance on the "
            "selection of concrete cryptographic suites that use agreed mechanisms. The use of ECCG agreed "
            "mechanisms is meant to help ensure a high level of security in the recommended cryptographic "
            "suites, while the focus on specific suites of mechanisms is meant to increase interoperability "
            "and simplify design choices. There is no normative requirement on selection among the "
            "alternatives for cryptographic suites given here but for all of them normative requirements "
            "apply to ensure security and interoperability. The present document also provides guidance on "
            "hash functions, (digital) signature schemes and (digital) signature suites to be used with the "
            "data structures used in the context of digital signatures and seals. For each data structure, the "
            "set of algorithms to be used is specified. NOTE 1: Migration scheduling, transition phases, and "
            "compliance deadlines for the transition to Post-Quantum Cryptography is planned to be addressed "
            "in the applicable post-quantum migration document currently under development, not in the present "
            "document. The present document provides mechanism suitability classifications (R/L) that are "
            "independent of deployment-phase timelines. NOTE 2: The present technical specification is known "
            "to be incomplete with respect to addressing the needs for the EUDI-Wallet according to Article 5a "
            "of the Regulation (EU) No. 910/2014 [i.12] as well as certain trust services including "
            "preservation services according to Article 34 and Article 40 as well as electronic registered "
            "delivery services according to Article 43 and Article 44. Therefore, an update of the present "
            "document is already in preparation."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.1 (Terms)",
        "testo": (
            "La clausola definisce 13 termini usati dal documento. 'AdES (digital) signature': firma digitale "
            "che sia una firma CAdES, una firma PAdES o una firma XAdES. 'CAdES signature': firma digitale che "
            "soddisfa i requisiti specificati in ETSI EN 319 122 (parti 1 e 2) [i.17]. 'cryptographic suite': "
            "combinazione di uno schema di firma con un metodo di padding e una funzione di hash crittografica. "
            "'(digital) signature': dati associati a una unita' di dati, inclusiva di una trasformazione "
            "crittografica della stessa, che (a) consente di provare origine e integrita' dell'unita' di dati, "
            "(b) consente di proteggere l'unita' di dati dalla contraffazione e (c) consente di supportare il "
            "non ripudio della firma dell'unita' di dati da parte del firmatario. 'hash function': come "
            "definito in ISO/IEC 10118-3 [i.5]. 'hybrid cryptographic scheme': schema crittografico che "
            "combina un algoritmo crittografico classico e un algoritmo crittografico post-quantistico, tale "
            "che la sicurezza della combinazione dipende dalla sicurezza di almeno uno degli schemi componenti. "
            "'legacy mechanism': meccanismo diffuso su larga scala, che offre attualmente un livello di "
            "sicurezza di almeno 100 bit e fornisce una sicurezza accettabile nel breve periodo, ma che "
            "dovrebbe essere dismesso appena praticabile perche' non riflette piu' pienamente lo stato "
            "dell'arte e presenta limitazioni di garanzia di sicurezza (come definito in ECCG Agreed "
            "Cryptographic Mechanisms [14]). 'PAdES signature': firma digitale che soddisfa i requisiti di "
            "ETSI EN 319 142 (parti 1 e 2) [i.19]. 'recommended mechanism': meccanismo che riflette pienamente "
            "lo stato dell'arte della crittografia, offre attualmente un livello di sicurezza di almeno 125 "
            "bit, e' supportato da solidi argomenti di sicurezza e fornisce un livello adeguato di sicurezza "
            "contro tutte le minacce oggi note o congetturate, anche considerando i previsti incrementi di "
            "potenza di calcolo (come definito in ECCG Agreed Cryptographic Mechanisms [14]). 'security "
            "level': numero di operazioni necessarie a un avversario per violare con successo la sicurezza "
            "fornita dal meccanismo, espresso come logaritmo in base 2 (es. 100 bit di sicurezza = 2^100 "
            "operazioni). 'signature policy': insieme di regole per la creazione e la validazione di una "
            "firma, che definisce i requisiti tecnici e procedurali di creazione e validazione per soddisfare "
            "una particolare esigenza di business e in base al quale la firma puo' essere determinata come "
            "valida. 'signature scheme': tripletta di tre algoritmi composta da un algoritmo di creazione "
            "della firma, un algoritmo di verifica della firma e un algoritmo di generazione delle chiavi. "
            "'XAdES signature': firma digitale che soddisfa i requisiti di ETSI EN 319 132 (parti 1 e 2) "
            "[i.18]."
        ),
        "testo_integrale": (
            "3.1 Terms: For the purposes of the present document, the following terms apply:\n"
            "AdES (digital) signature: digital signature that is either a CAdES signature, or a PAdES "
            "signature or a XAdES signature\n"
            "CAdES signature: digital signature that satisfies the requirements specified within ETSI EN 319 "
            "122 (parts 1 and 2) [i.17]\n"
            "cryptographic suite: combination of a signature scheme with a padding method and a cryptographic "
            "hash function\n"
            "(digital) signature: data associated to, including a cryptographic transformation of, a data unit "
            "that: a) allows to prove the source and integrity of the data unit; b) allows to protect the data "
            "unit against forgery; and c) allows to support signer non-repudiation of signing the data unit.\n"
            "hash function: As defined in ISO/IEC 10118-3 [i.5].\n"
            "hybrid cryptographic scheme: cryptographic scheme combining a classical cryptographic algorithm "
            "and a post-quantum cryptographic algorithm, such that the security of the combination relies on "
            "the security of at least one of the component schemes\n"
            "legacy mechanism: mechanism deployed on a large scale, currently offering a security level of at "
            "least 100 bits and considered to provide an acceptable short-term security but which should be "
            "phased out as soon as practical because no longer fully reflecting the state of the art and "
            "suffering from some security assurance limitations NOTE: As defined in ECCG Agreed Cryptographic "
            "Mechanisms [14].\n"
            "PAdES signature: digital signature that satisfies the requirements specified within ETSI EN 319 "
            "142 (parts 1 and 2) [i.19]\n"
            "recommended mechanism: mechanism, that fully reflects the state of the art in cryptography, "
            "currently offers a security level of at least 125 bits, supported by strong security arguments "
            "and can be said to provide an adequate level of security against all presently known or "
            "conjectured threats even considering the generally expected increases in computing power NOTE: As "
            "defined in ECCG Agreed Cryptographic Mechanisms [14].\n"
            "security level: number of operations necessary for an adversary to successfully break the "
            "security provided by the mechanism, expressed as a base 2 logarithm NOTE 1: Security level is "
            "expressed as a base 2 logarithm, e.g. 100 bits of security means that 2^100 operations are "
            "necessary. NOTE 2: As defined in ECCG Agreed Cryptographic Mechanisms [14].\n"
            "signature policy: set of rules for the creation and validation of a signature, that defines the "
            "technical and procedural requirements for signature creation and validation, in order to meet a "
            "particular business need, and under which the signature can be determined to be valid\n"
            "signature scheme: triplet of three algorithms composed of a signature creation algorithm, a "
            "signature verification algorithm and a key generation algorithm\n"
            "XAdES signature: digital signature that satisfies the requirements specified within ETSI EN 319 "
            "132 (parts 1 and 2) [i.18]"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.2 (Symbols)",
        "testo": (
            "La clausola definisce un solo simbolo: 'FR', identificatore delle curve ellittiche (Elliptic "
            "Curves) definite da ANSSI, l'Agence Nationale de la Sécurité des Systèmes d'Information."
        ),
        "testo_integrale": (
            "3.2 Symbols: For the purposes of the present document, the following symbols apply:\n"
            "FR Identifier for Elliptic Curves defined by ANSSI"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.3 (Abbreviations)",
        "testo": (
            "La clausola elenca le 42 abbreviazioni usate dal documento: ACM (Association for Computing "
            "Machinery), ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information, National Agency "
            "for Security of Information Systems), CA (Certification Authority), CMS (Cryptographic Message "
            "Syntax), CNSA (Commercial National Security Algorithm Suite), CRL (Certificate Revocation List), "
            "CRQC (Cryptographically Relevant Quantum Computer), CSOR (Cryptographic Algorithm Object "
            "Registration), DSA (Digital Signature Algorithm), EC (Elliptic Curve), ECCG (European "
            "Cybersecurity Certification Group), ECDSA (Elliptic Curve Digital Signature Algorithm), "
            "EC-SDSA-opt (optimized Elliptic Curve Schnorr Digital Signature Algorithm), EdDSA (Edwards-Curve "
            "Digital Signature Algorithm), ESI (Electronic Signatures and Trust Infrastructure: comitato "
            "tecnico ETSI), FIPS (Federal Information Processing Standard), GF (Galois Field), HSM (Hardware "
            "Security Module), IETF (Internet Engineering Task Force), ISO (International Organization for "
            "Standardization), LMS (Leighton-Micali Signature(s)), NIST (National Institute of Standards and "
            "Technology), NSA (National Security Agency), OCSP (Online Certificate Status Protocol), OID "
            "(Object Identifier), PKCS (Public-Key Cryptography Standards), PKI (Public Key Infrastructure), "
            "PKIX (Public-Key Infrastructure (X.509)), PQC (Post-Quantum Cryptography), PSS (Probabilistic "
            "Signature Scheme), RFC (Request For Comments), RNG (Random Number Generator), RSA (Rivest, "
            "Shamir and Adleman algorithm), SHA (Secure Hash Algorithm), SLH (Stateless Hash-based, come in "
            "SLH-DSA, FIPS 205), SOG-IS (Senior Officials Group Information Systems Security), TST "
            "(Time-Stamp Token), TSU (Time-Stamping Unit), URI (Uniform Resource Identifier), URN (Uniform "
            "Resource Number), XML (eXtensible Markup Language), XMSS (eXtended Merkle Signature Scheme)."
        ),
        "testo_integrale": (
            "3.3 Abbreviations: For the purposes of the present document, the following abbreviations "
            "apply:\n"
            "ACM Association for Computing Machinery\n"
            "ANSSI Agence Nationale de la Sécurité des Systèmes d'Information (National Agency for Security "
            "of Information Systems)\n"
            "CA Certification Authority\n"
            "CMS Cryptographic Message Syntax\n"
            "CNSA Commercial National Security Algorithm (Suite)\n"
            "CRL Certificate Revocation List\n"
            "CRQC Cryptographically Relevant Quantum Computer\n"
            "CSOR Cryptographic Algorithm Object Registration\n"
            "DSA Digital Signature Algorithm\n"
            "EC Elliptic Curve\n"
            "ECCG European Cybersecurity Certification Group\n"
            "ECDSA Elliptic Curve Digital Signature Algorithm\n"
            "EC-SDSA-opt optimized Elliptic Curve Schnorr Digital Signature Algorithm\n"
            "EdDSA Edwards-Curve Digital Signature Algorithm\n"
            "ESI Electronic Signatures and Trust Infrastructure NOTE: A Technical Committee of ETSI.\n"
            "FIPS Federal Information Processing Standard\n"
            "GF Galois Field\n"
            "HSM Hardware Security Module\n"
            "IETF Internet Engineering Task Force\n"
            "ISO International Organization for Standardization\n"
            "LMS Leighton-Micali Signature(s)\n"
            "NIST National Institute of Standards and Technology\n"
            "NSA National Security Agency\n"
            "OCSP Online Certificate Status Protocol\n"
            "OID Object Identifier\n"
            "PKCS Public-Key Cryptography Standards\n"
            "PKI Public Key Infrastructure\n"
            "PKIX Public-Key Infrastructure (X.509)\n"
            "PQC Post-Quantum Cryptography\n"
            "PSS Probabilistic Signature Scheme\n"
            "RFC Request For Comments\n"
            "RNG Random Number Generator\n"
            "RSA Rivest, Shamir and Adleman algorithm\n"
            "SHA Secure Hash Algorithm\n"
            "SLH Stateless Hash-based (as in SLH-DSA, FIPS 205)\n"
            "SOG-IS Senior Officials Group Information Systems Security\n"
            "TST Time-Stamp Token\n"
            "TSU Time-Stamping Unit\n"
            "URI Uniform Resource Identifier\n"
            "URN Uniform Resource Number\n"
            "XML eXtensible Markup Language\n"
            "XMSS eXtended Merkle Signature Scheme"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.4 (Notations)",
        "testo": (
            "La clausola definisce le notazioni con cui il documento classifica i meccanismi come legacy o "
            "raccomandati (recommended). 'L': meccanismo legacy con data di dismissione (deprecation/phasing "
            "out) al 31.12.2034, prorogabile con future release del documento. 'L[yyyy]': meccanismo legacy "
            "con data di dismissione non oltre il 31.12.yyyy, dove yyyy e' un intero che esprime un anno. "
            "'L[yyyy+]': meccanismo legacy con data di dismissione al 31.12.yyyy, dove yyyy e' un intero che "
            "esprime un anno, prorogabile con future release del documento. 'R': meccanismo raccomandato "
            "(recommended) che non ha ancora alcuna data di fine definita. NOTA: a differenza di [14] e per "
            "riflettere il periodo di validita' tipico dei certificati di end-entity emessi dai prestatori di "
            "servizi fiduciari assunto nello Scope, a tutte le date di fine usate nel documento e' aggiunto "
            "un default di tre anni; 'L' e' semanticamente equivalente a 'L[2034+]'."
        ),
        "testo_integrale": (
            "3.4 Notations: The requirements identified in the present document include the following "
            "notations for the classification of mechanisms as legacy mechanisms or recommended mechanisms:\n"
            "L: denotes a legacy mechanism with a deprecation/phasing out date of 31.12.2034 and which might "
            "be extended with future releases of the present document. NOTE: In contrast to [14] and to "
            "reflect the assumed typical validity period of end-entity certificates issued by trust service "
            "providers as laid out in the Scope, a default of three years is added to all the end dates in "
            "the present document.\n"
            "L[yyyy]: denotes a legacy mechanism with a deprecation/phasing out date no later than "
            "31.12.yyyy, where yyyy is an integer expressing a year.\n"
            "L[yyyy+]: denotes a legacy mechanism with a deprecation/phasing out date of 31.12.yyyy, where "
            "yyyy is an integer expressing a year and which might be extended with future releases of the "
            "present document. NOTE: L is semantically equivalent to L[2034+].\n"
            "R: denotes a recommended mechanism which has no defined end date, yet."
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
    "clausola 3.4 (Notations)",
    "clausola 4 (Use of ECCG Agreed Mechanisms and Maintenance of the present document)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
