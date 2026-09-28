"""ETSI EN 319 102-1 V1.4.1 (2024-06) - Electronic Signatures and
Infrastructures (ESI); Procedures for Creation and Validation of AdES Digital
Signatures; Part 1: Creation and Validation.

Fonte ETSI del lotto di import 2026-09-28 (`fonte_id=27`,
`docs/plan-import-lotto-eidas2-standard.md`), capitolo 1: clausola 1 (Scope),
clausola 2 (References, esclusa), clausola 3 (Definition of terms, symbols
and abbreviations: 3.1 Terms, 3.2 Symbols, 3.3 Abbreviations). Conteggio di
questo capitolo: 0 Obblighi, 4 Principi, 4 item di indice. Testo ufficiale in
app/.source_cache/etsi_319_102/cap01.txt (448 righe estratte dal PDF ETSI con
`pdftotext -layout`, front matter gia' rimosso; nessuna sezione "History" in
questo capitolo). Questo modulo NON tocca app/seed.py: gli id sono risolti per
riferimento dalla sessione principale tramite app/seed_data/lib.py. RELAZIONI
e' vuoto per contratto: i collegamenti con le altre fonti li costruisce la
sessione principale (Fase 6, ADR-0009).

Nessun prefisso di parte nei `riferimento` ("clausola 1 (Scope)", non "Parte
1: clausola 1 (Scope)"), benche' ETSI EN 319 102 sia un deliverable
multi-parte e questa Fonte copra per ora la sola Parte 1 (la Parte 2, ETSI TS
119 102-2 "Signature Validation Report", si aggiungera' come incremento
successivo nella stessa Fonte). Il criterio "Parte N: " e' prescritto dal
piano di import per le Fonti multi-parte gia' censite (ETSI EN 319 412, TS
119 431, EN 319 411) ed e' l'unico che renderebbe distinguibili due clausole
omonime di Parti diverse nel registro dei nodi; qui prevale pero' la forma
senza prefisso, per due ragioni: (a) il contratto di estrazione di questo
import la fissa esplicitamente cosi' ("clausola 5.2 (Title)"), (b) i moduli
fratelli della stessa Fonte 27 gia' scritti (cap03, cap05) usano quella
forma, e una Fonte con riferimenti disomogenei romperebbe le relazioni
cross-capitolo. Divergenza segnalata alla sessione principale, che resta
l'autorita' sulla convenzione globale: se sceglie il prefisso, va applicato a
tutti i moduli della Fonte 27, non solo a questo.

Copertura (ADR-0007), criterio applicato voce per voce:

- Clausola 1 (Scope) -> 1 Principio "scopo/ambito di applicazione". Perimetro
  in senso proprio: le procedure specificate (creazione delle firme AdES
  definite in ETSI EN 319 122-1 [i.2] CAdES, ETSI EN 319 132-1 [i.4] XAdES,
  ETSI EN 319 142-1 [i.6] PAdES; e determinazione della validita' tecnica di
  una firma AdES), il presupposto di applicazione (crittografia a chiave
  pubblica con certificati di chiave pubblica, PKC), i tre ambiti
  esplicitamente fuori perimetro (generazione/distribuzione dei Signature
  Creation Data e scelta degli algoritmi; formato, sintassi e codifica degli
  oggetti dati; interpretazione giuridica della firma, in particolare la
  validita' legale), e le due NOTE: la NOTE 1 dichiara che il documento mira
  a supportare il Regolamento (UE) n. 910/2014 [i.15] per la creazione e la
  convalida di firme e sigilli elettronici avanzati implementati come firme
  AdES, la NOTE 2 che le opzioni e possibilita' offerte dalle procedure sono
  selezionate da una politica di creazione, di augmentation o di convalida
  della firma (i requisiti legali arrivano da politiche specifiche, es.
  firme elettroniche qualificate ex Reg. 910/2014). Nessun verbo prescrittivo
  con destinatario obbligato in tutta la clausola, quindi nessun Obbligo.
- Clausola 2 (References: 2.1 Normative references, 2.2 Informative
  references) -> NESSUN nodo e NESSUN item di indice, come da contratto
  assegnato: bibliografia/paratesto puro (5 riferimenti normativi [1]-[5],
  IETF RFC 5280, ISO/IEC 9594-8:2020, IETF RFC 3161, ETSI TS 119 172-1, T7 &
  TeleTrusT Common PKI Specifications Part 9 SigG-Profile 2.0; 21
  informativi [i.1]-[i.21], con la voce [i.11] "Void" e il rinvio a
  Regulation (EU) No 910/2014 come [i.15], piu' le regole redazionali ETSI
  sui riferimenti specifici/non specifici e le NOTE sugli hyperlink). Stesso
  trattamento gia' riservato alla clausola 2 delle altre fonti ETSI censite.
- Clausola 3 (Definition of terms, symbols and abbreviations) -> NESSUN nodo
  e NESSUN item di indice: intestazione di puro raggruppamento, non contiene
  nulla oltre il titolo e le sottoclawse 3.1-3.3 (criterio esplicito del
  contratto: non genera nodo).
- Clausola 3.1 (Terms) -> 1 Principio "definitorio" riassuntivo, NON un nodo
  per singolo termine: la clausola e' un glossario alfabetico piatto senza
  struttura a lettere/numeri propria, quindi 63 nodi sarebbero 63 item di
  indice fittizi per un'unica clausola numerata (stesso criterio gia'
  applicato alla clausola 3.1 di ETSI EN 319 401 / 319 421 / TS 119 101). I
  63 termini definiti sono riportati verbatim in `testo_integrale`, con le
  NOTE e gli EXAMPLE ufficiali di clausola (unico blocco normativo di questa
  parte del documento: le definizioni in nota - catena prospective/shell,
  modello chain, Example per revocation data e signature class, NOTE 1 e NOTE
  2 di signature augmentation, NOTE 1 e NOTE 2 di signature augmentation
  policy, NOTE di signature validation policy con i tre possibili esiti
  PASSED/FAILED/INDETERMINED, NOTE di shell model sul tempo di validazione
  come input, NOTE di signature invocation sul "Wilful Act" del firmatario -
  delimitano il significato dei termini usati da tutto il resto del
  documento, quindi non sono paratesto decorativo). I singoli termini sono
  comunque indicizzati separatamente dal full-text su `testo_integrale`.
- Clausola 3.2 (Symbols) -> 1 Principio "definitorio" con `testo_integrale`
  "3.2 Symbols: Void.". Scelta di modellazione esplicita: la clausola dichiara
  che il documento non definisce simboli, quindi non ha contenuto oltre il
  segnaposto, e in questa famiglia di fonti esistono entrambe le convenzioni
  (la escludono dalla copertura "fuori perimetro in quanto paratesto" per
  ETSI EN 319 401 e EN 319 421; la includono con `testo_integrale` = "3.2
  Symbols: Void." per ETSI TS 119 432, TS 119 612 ed EN 319 411-1). Qui si
  sceglie di includerla: ADR-0007 vieta ogni discrimine di rilevanza in
  estrazione, e un item di indice in piu' per una sottoclavola numerata reale
  e' la scelta conservativa (l'omissione sarebbe un giudizio di merito non
  coperto dal criterio). Nessun'altra fonte puo' produrre un riferimento a
  questa clausola se non al nodo qui creato.
- Clausola 3.3 (Abbreviations) -> 1 Principio "definitorio" riassuntivo con
  le 43 abbreviazioni della clausola (ASIC, BES, CA, CMS, CRL, DA, DTBS,
  DTBSF, DTBSR, EPES, ER, ERS, HTML, LDAP, LT, LTA, LTV, OCSP, ODA, OID, PC,
  PKC, PKI, PKIX, POE, RSA, SAV, SCA, SCDev, SCE, SCS, SD, SDO, SDOC, SDR,
  SGML, SVA, TSA, TSL, TSP, URI, XML, XSL). La conversione PDF->testo rende
  la tabella a due colonne come coppia etichetta/forma estesa sulla stessa
  riga, con colonne allineate a spazi: in `testo_integrale` le coppie sono
  ricostruite in forma esplicita "ETICHETTA: Forma estesa.", una per riga e
  nell'ordine alfabetico del testo, senza perdere alcun valore (stessa
  convenzione gia' usata per la clausola 3.3 di ETSI EN 319 401 / 319 421 e
  per la clausola 3.3 di ETSI TS 119 312). Le capitalizzazioni anomale del
  testo ufficiale sono riportate come stanno nella fonte ("Associated
  SIgnature Container", "Public Key Infrastructure X. 509").

Nessun Obbligo in questo capitolo: le uniche clausole con contenuto proprio
sono di scopo e di glossario, prive di destinatario obbligato (i "shall" e i
requirement del documento vivono nelle clausole 4-5, capitoli cap02-cap07).
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 1 (Scope)",
        "testo": (
            "Il documento specifica le procedure per: la creazione delle firme elettroniche "
            "avanzate (AdES) definite negli standard di formato CAdES (ETSI EN 319 122-1 [i.2]), "
            "XAdES (ETSI EN 319 132-1 [i.4]) e PAdES (ETSI EN 319 142-1 [i.6]); e la "
            "determinazione della validita' tecnica di una firma AdES. Presupposto di "
            "applicazione: la firma AdES si basa su crittografia a chiave pubblica ed e' "
            "supportata da certificati di chiave pubblica (PKC); nel documento il termine "
            "'firma' designa sempre la firma AdES. Il documento mira a supportare il Regolamento "
            "(UE) n. 910/2014 (eIDAS) per la creazione e la convalida di firme e sigilli "
            "elettronici avanzati implementati come firme AdES, e introduce principi generali, "
            "oggetti e funzioni rilevanti nella creazione e nella convalida a partire dai "
            "vincoli (constraint) di creazione e di convalida, definendo classi generali di "
            "firma che ne consentono la verificabilita' su lunghi periodi. Fuori perimetro: (i) "
            "generazione e distribuzione dei dati di creazione della firma (chiavi, ecc.) e "
            "scelta e uso degli algoritmi crittografici; (ii) formato, sintassi o codifica degli "
            "oggetti dati coinvolti, in particolare il formato o la codifica dei documenti da "
            "firmare e delle firme create; (iii) l'interpretazione giuridica di qualunque firma, "
            "specialmente la sua validita' legale. Le opzioni e le possibilita' offerte dalle "
            "procedure sono selezionate da una politica di creazione, di augmentation o di "
            "convalida della firma; i requisiti legali possono arrivare da politiche specifiche "
            "(es. nel contesto delle firme elettroniche qualificate ex Reg. 910/2014)."
        ),
        "testo_integrale": (
            "1 Scope: The present document specifies procedures for:\n"
            "• the creation of AdES digital signatures (specified in ETSI EN 319 122-1 [i.2], "
            "ETSI EN 319 132-1 [i.4], ETSI EN 319 142-1 [i.6] respectively);\n"
            "• establishing whether an AdES digital signature is technically valid;\n"
            "whenever the AdES digital signature is based on public key cryptography and "
            "supported by Public Key Certificates (PKCs). To improve readability of the present "
            "document, AdES digital signatures are meant when the term signature is being "
            "used.\n"
            "NOTE 1: Regulation (EU) No 910/2014 [i.15] defines the terms electronic signature, "
            "advanced electronic signature, electronic seals and advanced electronic seal. These "
            "signatures and seals are usually created using digital signature technology. The "
            "present document aims at supporting the Regulation (EU) No 910/2014 [i.15] for "
            "creation and validation of advanced electronic signatures and seals when they are "
            "implemented as AdES digital signatures.\n"
            "The present document introduces general principles, objects and functions relevant "
            "when creating or validating signatures based on signature creation and validation "
            "constraints and defines general classes of signatures that allow for verifiability "
            "over long periods.\n"
            "The following aspects are considered to be out of scope:\n"
            "• generation and distribution of Signature Creation Data (keys, etc.), and the "
            "selection and use of cryptographic algorithms;\n"
            "• format, syntax or encoding of data objects involved, specifically format or "
            "encoding for documents to be signed or signatures created; and\n"
            "• the legal interpretation of any signature, especially the legal validity of a "
            "signature.\n"
            "NOTE 2: The signature creation and validation procedures specified in the present "
            "document provide several options and possibilities. The selection of these options "
            "is driven by a signature creation policy, a signature augmentation policy or a "
            "signature validation policy respectively. Note that legal requirements can be "
            "provided through specific policies, e.g. in the context of qualified electronic "
            "signatures as defined in the Regulation (EU) 910/2014 [i.15]."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.1 (Terms)",
        "testo": (
            "La clausola definisce un glossario di 63 termini del documento, raggruppabili per "
            "area: (i) firma e creazione della firma - 'digital signature' (dati aggiunti a "
            "un'unita' di dati o trasformazione crittografica che consente al destinatario di "
            "provarne origine e integrita' e di proteggerla dalla falsificazione), 'digital "
            "signature value', 'detached (digital) signature' (ne' enveloping ne' enveloped "
            "rispetto al Signed Data Object), 'enveloped (digital) signature', 'enveloping "
            "(digital) signature', 'signature scheme' (terzetto di algoritmi: creazione, "
            "verifica, generazione della chiave), 'cryptographic suite' (schema di firma + "
            "metodo di padding + funzione di hash crittografica), 'signature creation data' "
            "(dati unici come codici o chiavi private), 'Signature Creation Device (SCDev)', "
            "'Signature Creation Application (SCA)', 'Signature Creation System (SCS)' "
            "(SCA + SCDev), 'Signature Creation Environment (SCE)', 'signature creation policy' "
            "(regole tecniche e procedurali di creazione per una specifica esigenza di business, "
            "che determinano la conformita' delle firme), '(signature) creation constraint' "
            "(criteri usati per creare la firma), 'signature invocation' (interazione non banale "
            "tra firmatario e SCA/SCDev necessaria ad avviare il processo di firma - NOTE: e' il "
            "'Wilful Act' del firmatario), '(signature) commitment type', 'signature attribute', "
            "'signer', 'claimed signing time' (tempo dichiarato dal firmatario che da solo non "
            "costituisce prova indipendente del tempo effettivo); (ii) convalida - 'validation' "
            "(verifica e conferma della validita' di un certificato o di una firma), 'signature "
            "validation' (verifica e conferma che la firma digitale e' tecnicamente valida), "
            "'Signature Validation Application (SVA)', 'signature verification' e 'signature "
            "verification data', '(signature) validation constraint' e 'signature validation "
            "policy' (insieme dei vincoli processati dalla SVA; NOTE: concetto puramente tecnico, "
            "uno degli input che determinano il risultato PASSED/FAILED/INDETERMINED; puo' essere "
            "imposta da regole di applicabilita' della firma), 'signature validation report', "
            "'signature validation status' (TOTAL-PASSED, TOTAL-FAILED o INDETERMINATE), "
            "'signature acceptance' (verifica tecnica sulla firma o sui suoi attributi, i "
            "'signature elements constraints'), 'validation data', 'verifier', 'Driving "
            "Application (DA)'; (iii) augmentation e classi di firma - 'signature augmentation' "
            "(incorporare nella firma informazioni per mantenerne la validita' a breve e/o lungo "
            "termine; NOTE su materiale incorporato e su raccolta di informazioni e creazione di "
            "nuove strutture), 'signature augmentation constraint', 'signature augmentation "
            "policy' (NOTE: identificabile univocamente da un OID/URI; il documento non ne "
            "specifica il contenuto), 'signature augmentation report', 'signature augmentation "
            "result' (firma aumentata o messaggio di errore, con report opzionale), 'signature "
            "class' (insieme di firme che realizzano una data funzionalita'; EXAMPLE: firma con "
            "tempo, firma con materiale di convalida a lungo termine, firma che fornisce "
            "disponibilita' e integrita' a lungo termine del materiale di convalida); (iv) "
            "certificati e catene - 'certificate' (rinvio a PKC), 'Public Key Certificate (PKC)', "
            "'certificate identifier', 'certificate validation', 'certificate path (chain) "
            "validation', 'chain model' (tutti i certificati di CA validi al momento dell'uso e "
            "certificato di end-entity valido al momento della firma), 'shell model' (tutti i "
            "certificati validi a un tempo dato, che e' un parametro di input della convalida), "
            "'prospective certificate chain' (sequenza di n certificati che soddisfa le "
            "condizioni (a)-(c) di IETF RFC 5280 [1] clausola 6.1, con trust anchor fidata "
            "secondo la politica di convalida in uso), 'trust anchor', 'trust anchor sunset "
            "date', 'certification authority', 'attribute authority', 'attribute certificate', "
            "'Certificate Revocation List (CRL)', 'revocation data' (dati emessi da un servizio "
            "di stato di revoca, con la firma dell'autorita' emittente; EXAMPLE: CRL, risposta "
            "OCSP; NOTE: ETSI EN 319 411-1 [i.19] definisce il servizio di stato di revoca come "
            "servizio componente dei servizi di certificazione); (v) marche temporali, prove e "
            "archiviazione - 'time-stamp token' (IETF RFC 3161 [3]), 'time-assertion' (token di "
            "marca temporale o evidence record), 'Evidence Record (ER)' (NOTE: IETF RFC 4998 "
            "[i.9] e RFC 6283 [i.10]), 'proof of existence', 'evidence'; (vi) altro - "
            "'electronic document', 'signature policy' (creazione, augmentation, convalida o "
            "combinazione delle tre applicabile alla stessa firma o insieme di firme), 'trust "
            "service', 'Trust service Status List (TSL)', 'Signed Data Object (SDO)' (NOTE: "
            "vedi clausola 4.2.10)."
        ),
        "testo_integrale": (
            "3.1 Terms: For the purposes of the present document, the following terms apply:\n"
            "attribute authority: authority which assigns privileges by issuing attribute certificates\n"
            "attribute certificate: data structure, digitally signed by an attribute authority, "
            "that binds some attribute values with identification information about its holder\n"
            "certificate: See Public Key Certificate (PKC).\n"
            "certificate identifier: unambiguous identifier of a certificate\n"
            "certificate path (chain) validation: process of verifying and confirming that a "
            "certificate path (chain) is valid\n"
            "Certificate Revocation List (CRL): signed list indicating a set of certificates "
            "that are no longer considered valid by the certificate issuer\n"
            "certificate validation: process of verifying and confirming that a certificate is valid\n"
            "certification authority: authority trusted by one or more users to create and "
            "assign public-key certificates\n"
            "chain model: model for validation of X.509 certificate chains where all CA "
            "certificates have to be valid at the time they were used for issuing a certificate "
            "and the end-entity certificate was valid when creating the signature\n"
            "claimed signing time: time of signing claimed by the signer which on its own does "
            "not provide independent evidence of the actual signing time\n"
            "(signature) commitment type: signer-selected indication of the exact implication "
            "of a digital signature\n"
            "(signature) creation constraint: criteria used when creating a digital signature\n"
            "cryptographic suite: combination of a signature scheme with a padding method and a "
            "cryptographic hash function\n"
            "detached (digital) signature: digital signature that, with respect to the Signed "
            "Data Object, is neither enveloping nor enveloped\n"
            "digital signature: data appended to, or a cryptographic transformation of a data "
            "unit that allows a recipient of the data unit to prove the source and integrity of "
            "the data unit and protect against forgery, e.g. by the recipient\n"
            "digital signature value: result of the cryptographic transformation of a data unit "
            "that allows a recipient of the data unit to prove the source and integrity of the "
            "data unit and protect against forgery, e.g. by the recipient\n"
            "Driving Application (DA): application that uses a Signature Creation System (SCS) "
            "to create a signature or a Signature Validation Application (SVA) in order to "
            "validate digital signatures or a signature augmentation application to augment "
            "digital signatures\n"
            "electronic document: any content stored in electronic form, in particular text or "
            "sound, visual or audiovisual recording\n"
            "enveloped (digital) signature: digital signature embedded within the Signed Data "
            "Object\n"
            "enveloping (digital) signature: digital signature embedding the Signed Data Object\n"
            "evidence: information that can be used to resolve a dispute about various aspects "
            "of authenticity of archived data objects\n"
            "Evidence Record (ER): unit of data, which can be used to prove the existence of an "
            "archived data object or an archived data object group at a certain time\n"
            "NOTE: See IETF RFC 4998 [i.9] and IETF RFC 6283 [i.10].\n"
            "proof of existence: evidence that proves that an object existed at a specific "
            "date/time\n"
            "prospective certificate chain: sequence of n certificates which satisfies the "
            "conditions (a) to (c) in IETF RFC 5280 [1] clause 6.1, and the trust anchor is "
            "trusted according to the signature validation policy in use\n"
            "Public Key Certificate (PKC): public key of an entity, together with some other "
            "information, rendered unforgeable by digital signature with the private key of the "
            "certification authority which issued it\n"
            "revocation data: data issued by a revocation status service, including the "
            "signature of the issuing authority, for the purpose of providing revocation status "
            "information about one or more certificates\n"
            "EXAMPLE: Certificate Revocation List, OCSP response.\n"
            "NOTE: ETSI EN 319 411-1 [i.19] defines the revocation status service as a "
            "component service of the certification services.\n"
            "shell model: model for validation of X.509 certificate chains where all "
            "certificates have to be valid at a given time\n"
            "NOTE: The given time is an input parameter to the validation.\n"
            "signature acceptance: technical verification to be performed on the signature "
            "itself or on the attributes of the signature (i.e. the \"signature elements "
            "constraints\")\n"
            "signature attribute: signature property\n"
            "signature augmentation: process of incorporating to a digital signature "
            "information aiming to maintain the validity of that signature over the near term "
            "and/or the long term\n"
            "NOTE 1: Augmenting signatures is the process by which certain material (e.g. time "
            "stamps, validation data and even archival-related material) is incorporated to the "
            "signatures for making them more resilient to change or for enlarging their "
            "longevity.\n"
            "NOTE 2: This covers collection of information and creation of new structures that "
            "allows performing, on the long term, validations of a signature.\n"
            "signature augmentation constraint: technical criteria used when augmenting a "
            "signature to a specific signature class\n"
            "signature augmentation policy: set of signature augmentation constraints\n"
            "NOTE 1: An augmentation policy can be uniquely identified by an OID/URI.\n"
            "NOTE 2: The present document does not further specify the content of such a policy.\n"
            "signature augmentation report: information about the augmentation provided by the "
            "Signature Augmentation Application to the Driving Application\n"
            "NOTE: The present document does not further specify the content of such a report.\n"
            "signature augmentation result: either the augmented signature or an error message "
            "that augmentation did not succeed, and optionally a signature augmentation report\n"
            "NOTE: ETSI TS 119 442 [i.17] specifies how to convey such signature augmentation "
            "result.\n"
            "signature class: set of signatures achieving a given functionality\n"
            "EXAMPLE: Signature with time, signature with Long-Term Validation Material, "
            "Signature providing Long Term Availability and Integrity of Validation Material "
            "are possible signature classes.\n"
            "Signature Creation Application (SCA): application within the Signature Creation "
            "System (SCS), complementing the Signature Creation Device (SCDev), that creates a "
            "signature data object\n"
            "signature creation data: unique data, such as codes or private cryptographic keys, "
            "which are used by the signer to create a digital signature value\n"
            "Signature Creation Device (SCDev): configured software or hardware used to "
            "implement the signature creation data and to create a digital signature value\n"
            "Signature Creation Environment (SCE): physical, geographical and computational "
            "environment of the Signature Creation System (SCS)\n"
            "signature creation policy: set of rules, applicable to one or more digital "
            "signatures, that defines the technical and procedural requirements for their "
            "creation, in order to meet a particular business need, and under which the digital "
            "signature(s) can be determined to be conformant\n"
            "Signature Creation System (SCS): overall system, consisting of the Signature "
            "Creation Application (SCA) and the Signature Creation Device (SCDev), that creates "
            "a digital signature\n"
            "signature invocation: non-trivial interaction between the signer and the SCA or "
            "SCDev that is necessary to invoke the start of the signing process\n"
            "NOTE: It is the 'Wilful Act' of the signer.\n"
            "signature policy: signature creation policy, signature augmentation policy, "
            "signature validation policy or any combination thereof, applicable to the same "
            "signature or set of signatures\n"
            "signature scheme: triplet of algorithms composed of a signature creation "
            "algorithm, a signature verification algorithm and a key generation algorithm\n"
            "signature validation: process of verifying and confirming that a digital "
            "signature is technically valid\n"
            "Signature Validation Application (SVA): application that validates a signature "
            "against a signature validation policy, and that outputs a status indication (i.e. "
            "the signature validation status) and a signature validation report\n"
            "(signature) validation constraint: technical criteria against which a digital "
            "signature can be validated\n"
            "EXAMPLE: Criteria can be expressed as an abstract formulation of rule, value, "
            "parameter, range and computation result.\n"
            "NOTE: Validation constraints can be defined in a formal signature validation "
            "policy, can be given in configuration parameter files or implied by the behaviour "
            "of the Signature Validation Application (SVA).\n"
            "signature validation policy: set of signature validation constraints processed or "
            "to be processed by the Signature Validation Application (SVA)\n"
            "NOTE 1: A signature validation policy is a purely technical concept. It is one of "
            "the inputs of a validation process (other inputs include the signed data and the "
            "signature) that determine the validation result (PASSED, FAILED or INDETERMINED).\n"
            "NOTE 2: A signature validation policy can be imposed by signature applicability "
            "rules.\n"
            "signature validation report: comprehensive report of the validation provided by "
            "the Signature Validation Application (SVA) to the Driving Application and allowing "
            "the Driving Application and any party beyond the DA, to inspect details of the "
            "decisions made during validation and investigate the detailed causes for the "
            "status indication provided by the Signature Validation Application (SVA)\n"
            "EXAMPLE: Clause 5.1.3 specifies minimum requirements for the content of such a "
            "report and ETSI TS 119 102-2 [i.18] specifies such a report.\n"
            "signature validation status: one of the following indications: TOTAL-PASSED, "
            "TOTAL-FAILED or INDETERMINATE\n"
            "signature verification: process of checking the cryptographic value of a "
            "signature using signature verification data\n"
            "signature verification data: data, such as codes or public cryptographic keys, "
            "used for the purpose of verifying a signature\n"
            "Signed Data Object (SDO): data structure containing the signature value, "
            "signature attributes and other information\n"
            "NOTE: See clause 4.2.10.\n"
            "signer: entity being the creator of a digital signature\n"
            "time-assertion: time-stamp token or evidence record\n"
            "time-stamp token: data object defined in IETF RFC 3161 [3], representing a "
            "time-stamp\n"
            "trust anchor: entity that is trusted by a relying party and used for validating "
            "certificates in certification paths\n"
            "trust anchor sunset date: time until when the trust anchor was or is considered "
            "reliable\n"
            "trust service: electronic service which enhances trust and confidence in "
            "electronic transactions\n"
            "Trust service Status List (TSL): form of a signed list as the basis for "
            "presentation of trust service status information\n"
            "validation: process of verifying and confirming that a certificate or a digital "
            "signature is valid\n"
            "validation data: data that is used to validate a digital signature\n"
            "verifier: entity that wants to validate or verify a digital signature"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.2 (Symbols)",
        "testo": (
            "La clausola non definisce alcun simbolo: il testo ufficiale della clausola 3.2 "
            "(Symbols) e' integralmente 'Void.', cioe' dichiara che per gli scopi del documento "
            "non si applica alcun simbolo. Nessun contenuto oltre il segnaposto di redazione, "
            "ma la sottoclavola numerata e' censita per copertura completa dell'intera clausola 3."
        ),
        "testo_integrale": "3.2 Symbols: Void.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.3 (Abbreviations)",
        "testo": (
            "La clausola elenca 43 abbreviazioni usate dal documento: ASIC (Associated "
            "SIgnature Container), BES (Basic Electronic Signature), CA (Certification "
            "Authority), CMS (Cryptographic Message Syntax), CRL (Certificate Revocation "
            "List), DA (Driving Application), DTBS (Data To Be Signed), DTBSF (Data To Be "
            "Signed (Formatted)), DTBSR (Data To Be Signed Representation), EPES (Explicit "
            "Policy based Electronic Signature), ER (Evidence Record), ERS (Evidence Record "
            "Syntax), HTML (HyperText Markup Language), LDAP (Lightweight Directory Access "
            "Protocol), LT (Long Term), LTA (Long Term Archival), LTV (Long Term Validation), "
            "OCSP (Online Certificate Status Protocol), ODA (Office Document Architecture), "
            "OID (Object IDentifier), PC (Personal Computer), PKC (Public Key Certificate), "
            "PKI (Public Key Infrastructure), PKIX (Public Key Infrastructure X. 509), POE "
            "(Proof Of Existence), RSA (Rivest, Shamir and Adleman algorithm), SAV (Signature "
            "Acceptance Validation), SCA (Signature Creation Application), SCDev (Signature "
            "Creation Device), SCE (Signature Creation Environment), SCS (Signature Creation "
            "System), SD (Signer's Document), SDO (Signed Data Object), SDOC (Signed Data "
            "Object Composer), SDR (Signer's Document Representation), SGML (Standard "
            "Generalized Markup Language), SVA (Signature Validation Application), TSA (Time "
            "Stamping Authority), TSL (Trust service Status List), TSP (Trust Service "
            "Provider), URI (Uniform Resource Identifier), XML (eXtensible Mark-up Language), "
            "XSL (eXtensible Stylesheet Language). Le capitalizzazioni anomale del testo "
            "ufficiale ('Associated SIgnature Container', 'Object IDentifier', 'Public Key "
            "Infrastructure X. 509') sono riportate come stanno nella fonte"
        ),
        "testo_integrale": (
            "3.3 Abbreviations: For the purposes of the present document, the following "
            "abbreviations apply:\n"
            "ASIC: Associated SIgnature Container\n"
            "BES: Basic Electronic Signature\n"
            "CA: Certification Authority\n"
            "CMS: Cryptographic Message Syntax\n"
            "CRL: Certificate Revocation List\n"
            "DA: Driving Application\n"
            "DTBS: Data To Be Signed\n"
            "DTBSF: Data To Be Signed (Formatted)\n"
            "DTBSR: Data To Be Signed Representation\n"
            "EPES: Explicit Policy based Electronic Signature\n"
            "ER: Evidence Record\n"
            "ERS: Evidence Record Syntax\n"
            "HTML: HyperText Markup Language\n"
            "LDAP: Lightweight Directory Access Protocol\n"
            "LT: Long Term\n"
            "LTA: Long Term Archival\n"
            "LTV: Long Term Validation\n"
            "OCSP: Online Certificate Status Protocol\n"
            "ODA: Office Document Architecture\n"
            "OID: Object IDentifier\n"
            "PC: Personal Computer\n"
            "PKC: Public Key Certificate\n"
            "PKI: Public Key Infrastructure\n"
            "PKIX: Public Key Infrastructure X. 509\n"
            "POE: Proof Of Existence\n"
            "RSA: Rivest, Shamir and Adleman algorithm\n"
            "SAV: Signature Acceptance Validation\n"
            "SCA: Signature Creation Application\n"
            "SCDev: Signature Creation Device\n"
            "SCE: Signature Creation Environment\n"
            "SCS: Signature Creation System\n"
            "SD: Signer's Document\n"
            "SDO: Signed Data Object\n"
            "SDOC: Signed Data Object Composer\n"
            "SDR: Signer's Document Representation\n"
            "SGML: Standard Generalized Markup Language\n"
            "SVA: Signature Validation Application\n"
            "TSA: Time Stamping Authority\n"
            "TSL: Trust service Status List\n"
            "TSP: Trust Service Provider\n"
            "URI: Uniform Resource Identifier\n"
            "XML: eXtensible Mark-up Language\n"
            "XSL: eXtensible Stylesheet Language"
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

MAPPATURA_LOCALE = {
    "clausola 1 (Scope)": ["clausola 1 (Scope)"],
    "clausola 3.1 (Terms)": ["clausola 3.1 (Terms)"],
    "clausola 3.2 (Symbols)": ["clausola 3.2 (Symbols)"],
    "clausola 3.3 (Abbreviations)": ["clausola 3.3 (Abbreviations)"],
}

RELAZIONI = []
