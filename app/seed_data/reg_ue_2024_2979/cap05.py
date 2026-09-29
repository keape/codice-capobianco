"""Regolamento di esecuzione (UE) 2024/2979 della Commissione, del 28 novembre
2024 - modalita' di applicazione del regolamento (UE) n. 910/2014 per quanto
riguarda l'integrita' e le funzionalita' di base dei portafogli europei di
identita' digitale (articolo 5 bis, paragrafo 23, eIDAS). Fonte
`reg_ue_2024_2979`, capitolo 5 di 5 (vedi
app/.source_cache/reg_ue_2024_2979/manifest.json): Allegati I-V. Gli articoli
1-2, 3-7, 8-14 e 15 sono nei capitoli 1-4, assegnati ad altri moduli. Testo
ufficiale italiano in app/.source_cache/reg_ue_2024_2979/cap05.txt, acquisito
per content negotiation CELLAR (CELEX 32024R2979, lingua italiana; URL risolto
http://publications.europa.eu/resource/cellar/a7576de1-b1e0-11ef-acb1-01aa75ed71a1.0014.03/DOC_1,
XHTML in Gazzetta ufficiale; provenienza completa, caratteri e sha256 in
provenance.json). La riga ELI
(http://data.europa.eu/eli/reg_impl/2024/2979/oj) e la riga "ISSN 1977-0707
(electronic edition)" chiudono il documento in coda all'allegato V.

Modellazione (ADR-0007, nessun discrimine di rilevanza):
- Paratesto -> nessun nodo: l'intestazione di ciascun allegato ("ALLEGATO N") e
  il suo titolo non sono articoli, commi, punti o voci, e la riga ELI e la riga
  ISSN sono paratesto di pubblicazione. Non compaiono in
  INDICE_ARTICOLI_LOCALE, dove un item privo di riga farebbe fallire
  `verifica_copertura` (stesso trattamento del cap04 di questa Fonte). Fanno
  eccezione gli allegati I, II e V, il cui contenuto e' coperto da UNA sola
  riga che rappresenta l'allegato intero: li' l'intestazione e il titolo sono
  assorbiti nel `testo_integrale` della riga (convenzione del chapeau
  dell'allegato del Reg. 2025/1567) e l'item a livello di allegato esiste come
  item proprio.
- Allegato I (elenco delle norme di cui all'articolo 5: sette voci GSMA/
  GlobalPlatform introdotte da un trattino) -> UNA sola riga Principio "altro":
  e' un elenco puramente enumerativo di norme di riferimento, senza precetto
  autonomo voce per voce (stesso criterio della lista definitoria dell'art. 2
  e delle liste di norme di riferimento del Reg. 2025/2531 e 2025/2532). Le
  sette voci sono indicizzate separatamente ("allegato I, voce 1" ... "allegato
  I, voce 7") e mappate tutte a questa riga, insieme all'item "allegato I" che
  copre intestazione e titolo dell'allegato.
- Allegato II (elenco delle norme di cui all'articolo 8: ISO/IEC 18013-5:2021
  e Verifiable Credentials Data Model 1.1 del W3C) -> UNA sola riga Principio
  "altro", stessa struttura dell'allegato I: item "allegato II" piu' "allegato
  II, voce 1" e "allegato II, voce 2", tutti mappati a quella riga.
- Allegato III (tre politiche di divulgazione incorporate comuni di cui
  all'articolo 10) -> TRE righe Principio "definitorio", una per punto, non una
  riga unica: ciascun punto enuncia il contenuto proprio e distinto di una
  politica ("«Nessuna politica» indica che...", "La politica «...» indica
  che..."), cioe' l'effetto di ciascuna politica sulla divulgazione degli
  attestati elettronici di attributi, e non una voce di un elenco unitario. Il
  tipo "definitorio" e' quello dei punti 1-3 perche' la forma e' definitoria
  (ogni punto spiega che cosa significa la designazione di una politica);
  scartato "altro" perche' qui c'e' una definizione in senso proprio, e scartato
  "equivalenza giuridica"/"presunzione legale" perche' nessuno dei tre punti
  dichiara effetti di quel tipo. Nessuna riga e' un Obbligo: il punto 2 formula
  una facolta' limitata ("gli utenti del portafoglio possono divulgare ... solo
  a parti ... autenticate") e il punto 3 una raccomandazione ("dovrebbero
  divulgare ... soltanto a ..."), non un comportamento imposto; l'obbligo di
  trattare queste politiche e' in capo ai fornitori di portafogli dall'art. 10
  §1, che appartiene al cap03. Per la stessa ragione le righe non hanno
  `soggetti`: gli utenti del portafoglio e le parti facenti affidamento nominati
  nei punti 2 e 3 sono i termini della definizione, non soggetti obbligati
  censiti come tali. Item di indice: "allegato III, punto 1", "allegato III,
  punto 2", "allegato III, punto 3"; nessun item a livello di allegato, perche'
  l'intestazione e' paratesto e un item unico non sarebbe mappabile su tre righe
  distinte.
- Allegato IV (formati per firme e sigilli di cui all'articolo 12):
  * punto 1 ("Formato obbligatorio per firme o sigilli: a) PAdES ...") ->
    Obbligo, tipo "tecnico/sicurezza": l'allegato stesso qualifica il formato
    come obbligatorio, e l'art. 12 §2(c) impone alle applicazioni per la
    creazione di firme di produrre firme o sigilli "come minimo nei formati
    obbligatori di cui all'allegato IV", quindi la designazione ha effetto
    prescrittivo. Nessun `soggetti`: il testo dell'allegato non nomina il
    soggetto tenuto (le applicazioni per la creazione di firme e il fornitore
    del portafoglio sono nominati nell'art. 12, che appartiene al cap03), e la
    regola del batch vieta di forzare categorie di soggetto non nominate nel
    testo. Item: "allegato IV, punto 1" e "allegato IV, punto 1(a)".
  * punto 2 ("Elenco dei formati facoltativi per firme o sigilli: a) XAdES,
    b) JAdES, c) CAdES, d) ASiC") -> UNA sola riga Principio "altro": nessun
    precetto autonomo, i quattro formati sono dichiarati facoltativi dallo
    stesso allegato; le lettere sono indicizzate separatamente ("allegato IV,
    punto 2(a)" ... "allegato IV, punto 2(d)") e mappate a questa riga, insieme
    all'item "allegato IV, punto 2".
  * punto 3 ("Interfaccia di programmazione di un'applicazione: — Cloud
    Signature Consortium (CSC), specifica v2.0 (20 aprile 2023)") -> UNA riga
    Principio "altro": e' la designazione della specifica di riferimento -
    l'"interfaccia di programmazione di un'applicazione di cui all'allegato IV"
    che le applicazioni per la creazione di firme integrate nelle istanze di
    portafoglio devono supportare e' imposta dall'art. 12 §3, non dall'allegato
    - con la stessa struttura dell'allegato I; item "allegato IV, punto 3" e
    "allegato IV, punto 3, voce 1" (la voce con trattino). Criterio che
    distingue il punto 1 dal punto 3: il punto 1 qualifica il formato
    "obbligatorio", il punto 3 si limita a nominare la specifica.
- Le norme e le specifiche citate negli allegati (SAM.01 GSMA, GPC_GUI_217,
  GPC_SPE_034, GPC_SPE_007, GPC_SPE_013, GPC_SPE_093 e GPD_SPE_075
  GlobalPlatform, ETSI EN 319 142-1, ETSI EN 319 132-1, ETSI TS 119 182-1,
  ETSI EN 319 122-1, ETSI EN 319 162-1 e 162-2, ISO/IEC 18013-5:2021,
  Verifiable Credentials Data Model 1.1 del W3C, Cloud Signature Consortium CSC
  v2.0, Web Authentication Level 2 del W3C) NON ricevono nodi propri e non
  producono relazioni: non sono Fonti del censimento (le ETSI della famiglia
  AdES sono il blocco B di docs/plan-import-lotto-2-backlog-e-ades.md, non
  ancora importato). Restano nel `testo_integrale` delle righe che le
  designano, cosi' come sono elencate nel testo ufficiale.
- `testo_integrale`: verbatim e integrale, ricucito dalle righe spezzate dalla
  conversione XHTML -> testo. Le righe "—" isolate del testo ufficiale
  diventano il prefisso "— " della voce che seguono (allegati I, II, V e punto
  3 dell'allegato IV); i marcatori isolati su riga propria ("1."/"2."/"3." per i
  punti, "a)"-"d)" per le lettere) sono riuniti al testo della voce che
  introducono. Nessun marcatore di elisione (vincolo
  `verifica_completezza_testo_integrale`, ADR-0010). Nessuna riga valorizza
  `severita` o `sanzioni`: questo regolamento non prevede sanzioni proprie.
- `testo` e' la sintesi compressa (1-3 frasi), che nomina le norme e le
  specifiche designate per renderle cercabili senza aprire il
  `testo_integrale`.
- `oggetti_giuridici` valorizzato dove il testo lo indica: portafoglio europeo
  di identita' digitale per gli allegati I e V; identificazione elettronica e
  attestato elettronico di attributi per l'allegato II (le due norme riguardano
  i dati di identificazione personale e gli attestati); attestato elettronico
  di attributi per l'allegato III (le politiche vi sono incorporate); firma
  elettronica e sigillo elettronico per i punti 1 e 2 dell'allegato IV (formati
  per firme o sigilli); firma elettronica qualificata per il punto 3 (la
  specifica CSC governa la firma a distanza tramite dispositivi qualificati, per
  l'art. 12 §3).
- `stato` = vigente per tutte le righe (il regolamento e' in vigore).
- RELAZIONI = [] (come nei cap01 e cap04 di questa Fonte, scritti in
  parallelo): gli allegati rinviano agli articoli che li richiamano (art. 5 §2
  per l'allegato I, art. 8 per il II, art. 10 §1 per il III, art. 12 §2(c) e §3
  per il IV, art. 14 §1 per il V), ma quei nodi appartengono ai cap02 e cap03,
  scritti da moduli paralleli: dichiarare qui la relazione imporrebbe di
  indovinare il loro `riferimento` ("art. 5 §2" o "art. 5, paragrafo 2"?) e un
  riferimento sbagliato farebbe fallire l'intero seed con KeyError. Le relazioni
  interne ("richiama"/"e' richiamato da") le costruisce la sessione principale
  dopo il merge, insieme ai collegamenti cross-fonte (ADR-0009).

Copertura: 25 item di indice, 9 righe (1 Obbligo + 8 Principi).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "allegato IV, punto 1",
        "testo": "Formato obbligatorio per firme o sigilli: PAdES (PDF Advanced Electronic Signature, firma elettronica avanzata per PDF) come specificato nella norma ETSI EN 319 142-1 V1.1.1 (2016-04), Electronic Signatures and Infrastructures (ESI), PAdES digital signatures, parte 1: Building blocks and PAdES baseline signatures.",
        "testo_integrale": "1. Formato obbligatorio per firme o sigilli:\n\na) PAdES (PDF Advanced Electronic Signature, firma elettronica avanzata per PDF) come specificato nella norma ETSI EN 319 142-1 V1.1.1 (2016-04); Electronic Signatures and Infrastructures (ESI); PAdES digital signatures; parte 1: Building blocks and PAdES baseline signatures.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "allegato I",
        "testo": "Elenco delle sette norme di cui all'articolo 5, sulle applicazioni sicure per dispositivi mobili: SAM.01 (GSMA, requisiti per il supporto di applet di terzi su eSIM ed eSE via SAM), GPC_GUI_217 (GlobalPlatform, configurazione SAM), GPC_SPE_034 (GlobalPlatform Card Specification per smart card), GPC_SPE_007 (GlobalPlatform Amendment A, gestione riservata del contenuto della carta), GPC_SPE_013 (GlobalPlatform Amendment D, Secure Channel Protocol 03), GPC_SPE_093 (GlobalPlatform Amendment F, Secure Channel Protocol 11) e GPD_SPE_075 (GlobalPlatform, Open Mobile API/OMAPI per l'accesso delle app mobili agli elementi sicuri dei dispositivi degli utenti).",
        "testo_integrale": "ALLEGATO I\n\nELENCO DELLE NORME DI CUI ALL'ARTICOLO 5\n\n— SAM.01 Secured Applications for Mobile - Requirements for support 3 third party Applets on eSIM and eSE via SAM. v1.1 2023, GSMA;\n\n— GPC_GUI_ 217 GlobalPlatform SAM Configuration Technical specification for implementation of SAM v1.0 2024-04;\n\n— GPC_SPE_0 34 GlobalPlatform Card Specification Technical specification for smart cards v2.3.1 2018-03;\n\n— GPC_SPE_0 07 GlobalPlatform Amendment A Confidential Card Content Management v1.2 2019-07;\n\n— GPC_SPE_0 13 GlobalPlatform Amendment D Secure Channel Protocol 03 v1.2 2020-04;\n\n— GPC_SPE_0 93 GlobalPlatform Amendment F Secure Channel Protocol 11 v1.4 2024-03;\n\n— GPD_SPE_0 75 Open Mobile API Specification OMAPI API for mobile apps to access secure elements on user devices. v3.3 2018-08, GlobalPlatform.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["portafoglio europeo di identità digitale"],
    },
    {
        "riferimento": "allegato II",
        "testo": "Elenco delle norme di cui all'articolo 8 per i dati di identificazione personale e per gli attestati elettronici di attributi: ISO/IEC 18013-5:2021 e «Verifiable Credentials Data Model 1.1», W3C Recommendation del 3 marzo 2022.",
        "testo_integrale": "ALLEGATO II\n\nELENCO DELLE NORME DI CUI ALL'ARTICOLO 8\n\n— ISO/IEC 18013-5:2021\n\n— Verifiable Credentials Data Model 1.1, W3C Recommendation, 3 marzo 2022.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica", "attestato elettronico di attributi"],
    },
    {
        "riferimento": "allegato III, punto 1",
        "testo": "La politica di divulgazione incorporata «Nessuna politica» indica che non si applica alcuna politica agli attestati elettronici di attributi.",
        "testo_integrale": "1. «Nessuna politica» indica che non si applica alcuna politica agli attestati elettronici di attributi.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["attestato elettronico di attributi"],
    },
    {
        "riferimento": "allegato III, punto 2",
        "testo": "La politica di divulgazione incorporata «solo le parti facenti affidamento sulla certificazione autorizzate» indica che gli utenti del portafoglio possono divulgare attestati elettronici di attributi solo a parti facenti affidamento sulla certificazione autenticate, esplicitamente elencate nelle politiche di divulgazione.",
        "testo_integrale": "2. La politica «solo le parti facenti affidamento sulla certificazione autorizzate» indica che gli utenti del portafoglio possono divulgare attestati elettronici di attributi solo a parti facenti affidamento sulla certificazione autenticate, che sono esplicitamente elencate nelle politiche di divulgazione.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["attestato elettronico di attributi"],
    },
    {
        "riferimento": "allegato III, punto 3",
        "testo": "La politica di divulgazione incorporata «Root of trust specifica» indica che gli utenti del portafoglio dovrebbero divulgare lo specifico attestato elettronico di attributi soltanto alle parti facenti affidamento sul portafoglio autenticate con certificati di accesso derivati da una root specifica (o da un elenco di root specifiche) o da certificati intermedi.",
        "testo_integrale": "3. «Root of trust specifica» indica che gli utenti del portafoglio dovrebbero divulgare lo specifico attestato elettronico di attributi soltanto alle parti facenti affidamento sul portafoglio autenticate con certificati di accesso di dette parti derivati da una root specifica (o da un elenco di root specifiche) o da certificati intermedi.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["attestato elettronico di attributi"],
    },
    {
        "riferimento": "allegato IV, punto 2",
        "testo": "Elenco dei formati facoltativi per firme o sigilli: XAdES per firme in formato XML (ETSI EN 319 132-1 V1.2.1 (2022-02)), JAdES per firme in formato JSON (ETSI TS 119 182-1 V1.2.1 (2024-07)), CAdES per firme in formato CMS (ETSI EN 319 122-1 V1.3.1 (2023-06)) e ASiC per la firma di contenitori (ETSI EN 319 162-1 V1.1.1 (2016-04) e ETSI EN 319 162-2 V1.1.1 (2016-04)).",
        "testo_integrale": "2. Elenco dei formati facoltativi per firme o sigilli:\n\na) XAdES come specificato nella norma ETSI EN 319 132-1 V1.2.1 (2022-02) Electronic Signatures and Infrastructures (ESI); XAdES digital signatures; parte 1: Building blocks and XAdES baseline signatures (XAdES) per firme in formato XML;\n\nb) JAdES come specificato nella norma ETSI TS 119 182-1 V1.2.1 (2024-07) Electronic Signatures and Infrastructures (ESI); JAdES digital signatures; parte 1: Building blocks and JAdES baseline signatures per firme in formato JSON;\n\nc) CAdES (CMS Advanced Electronic Signature) come specificato nella norma ETSI EN 319 122-1 V1.3.1 (2023-06) Electronic Signatures and Infrastructures (ESI); CAdES digital signatures; parte 1: Building blocks and CAdES baseline signatures per firme in formato CMS;\n\nd) ASiC (Associated Signature Container) come specificato nella norma ETSI EN 319 162-1 V1.1.1 (2016-04) Electronic Signatures and Infrastructures (ESI); Associated Signature Containers (ASiC); parte 1: Building blocks and ASiC baseline containers e norma ETSI EN 319 162-2 V1.1.1 (2016-04) Electronic Signatures and Infrastructures (ESI); Associated Signature Containers (ASiC); parte 2: Additional ASiC containers' per la firma di contenitori.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica", "sigillo elettronico"],
    },
    {
        "riferimento": "allegato IV, punto 3",
        "testo": "Interfaccia di programmazione di un'applicazione: Cloud Signature Consortium (CSC), specifica v2.0 (20 aprile 2023).",
        "testo_integrale": "3. Interfaccia di programmazione di un'applicazione:\n\n— Cloud Signature Consortium (CSC), specifica v2.0 (20 aprile 2023).",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["firma elettronica qualificata"],
    },
    {
        "riferimento": "allegato V",
        "testo": "Specifiche tecniche per la generazione di pseudonimi di cui all'articolo 14: «Web Authentication – Level 2», W3C Recommendation dell'8 aprile 2021 (https://www.w3.org/TR/2021/REC-webauthn-2-20210408/).",
        "testo_integrale": "ALLEGATO V\n\nSPECIFICHE TECNICHE PER LA GENERAZIONE DI PSEUDONIMI DI CUI ALL'ARTICOLO 14\n\nSpecifiche tecniche:\n\n— Web Authentication – Level 2, W3C Recommendation, 8 aprile 2021, https://www.w3.org/TR/2021/REC-webauthn-2-20210408/.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["portafoglio europeo di identità digitale"],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "allegato I",
    "allegato I, voce 1",
    "allegato I, voce 2",
    "allegato I, voce 3",
    "allegato I, voce 4",
    "allegato I, voce 5",
    "allegato I, voce 6",
    "allegato I, voce 7",
    "allegato II",
    "allegato II, voce 1",
    "allegato II, voce 2",
    "allegato III, punto 1",
    "allegato III, punto 2",
    "allegato III, punto 3",
    "allegato IV, punto 1",
    "allegato IV, punto 1(a)",
    "allegato IV, punto 2",
    "allegato IV, punto 2(a)",
    "allegato IV, punto 2(b)",
    "allegato IV, punto 2(c)",
    "allegato IV, punto 2(d)",
    "allegato IV, punto 3",
    "allegato IV, punto 3, voce 1",
    "allegato V",
    "allegato V, voce 1",
]

MAPPATURA_LOCALE = {
    "allegato I": [
        "allegato I",
        "allegato I, voce 1",
        "allegato I, voce 2",
        "allegato I, voce 3",
        "allegato I, voce 4",
        "allegato I, voce 5",
        "allegato I, voce 6",
        "allegato I, voce 7",
    ],
    "allegato II": [
        "allegato II",
        "allegato II, voce 1",
        "allegato II, voce 2",
    ],
    "allegato III, punto 1": ["allegato III, punto 1"],
    "allegato III, punto 2": ["allegato III, punto 2"],
    "allegato III, punto 3": ["allegato III, punto 3"],
    "allegato IV, punto 1": [
        "allegato IV, punto 1",
        "allegato IV, punto 1(a)",
    ],
    "allegato IV, punto 2": [
        "allegato IV, punto 2",
        "allegato IV, punto 2(a)",
        "allegato IV, punto 2(b)",
        "allegato IV, punto 2(c)",
        "allegato IV, punto 2(d)",
    ],
    "allegato IV, punto 3": [
        "allegato IV, punto 3",
        "allegato IV, punto 3, voce 1",
    ],
    "allegato V": [
        "allegato V",
        "allegato V, voce 1",
    ],
}

RELAZIONI = []
