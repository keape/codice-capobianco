"""Regolamento di esecuzione (UE) 2024/482 della Commissione, del 31 gennaio
2024 - modalita' di applicazione del regolamento (UE) 2019/881 del Parlamento
europeo e del Consiglio per quanto riguarda l'adozione del sistema europeo di
certificazione della cibersicurezza basato sui criteri comuni (EUCC). Fonte 29
(slug `reg_ue_2024_482`), capitolo 10 di 14 (vedi
app/.source_cache/reg_ue_2024_482/manifest.json): Allegato III - Profili di
protezione raccomandati. Gli artt. 1-50 e gli allegati I-II e IV-IX
appartengono ai capitoli 1-9 e 11-14 della stessa Fonte, assegnati ad altri
moduli: nessuno di quei file e' toccato qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_482/cap10.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R0482, lingua italiana; URL
risolto
http://publications.europa.eu/resource/cellar/687c0d05-c580-11ee-95d9-01aa75ed71a1.0014.03/DOC_1,
XHTML della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 540.435 byte
scaricati, 135.367 caratteri di testo, sha256 del raw.txt
b46d08cab6d63b2c190ae767042c07c1fc324955c22ef491eb314556b28ca5b8 - dettagli
completi in app/.source_cache/reg_ue_2024_482/provenance.json). La porzione
assegnata e' l'allegato III per intero: dall'intestazione "ALLEGATO III" alla
riga che precede "ALLEGATO IV". Il preambolo (considerando 1-33) e' a monte
degli allegati e non e' in questa porzione.

Modellazione (ADR-0007, nessun punto dell'allegato non coperto, nessuno
coperto due volte):
- Paratesto -> nessun nodo proprio: l'intestazione "ALLEGATO III" e il suo
  titolo ("Profili di protezione raccomandati (che illustrano i settori tecnici
  di cua all'allegato I)") non sono punti dell'allegato ma struttura dell'atto;
  restano comunque coperti perche' assorbiti nel `testo_integrale` della riga
  "allegato III" (stessa convenzione dell'allegato I del Reg. 2024/2979 cap05).
  In questa porzione non compaiono epigrafe, firma, formula di chiusura, note a
  pie' di pagina ne' riga ELI: nessuno di questi elementi produce nodo o item di
  indice. Il titolo dell'allegato contiene un refuso del testo ufficiale
  italiano ("che illustrano i settori tecnici di cua all'allegato I", per "di
  cui"): e' riportato verbatim come il testo lo pubblica, senza correggerlo.
- Chapeau ("Profili di protezione utilizzati per la certificazione di prodotti
  TIC che rientrano nella categoria di prodotti TIC indicata di seguito:") -> UN
  Principio, tipo "altro": designa l'elenco che segue senza imporre un
  comportamento a un soggetto identificato (stesso trattamento del chapeau
  dell'allegato del Reg. 2025/2532). Item di indice "allegato III".
- Lettere (a)-(f) -> UN Principio ciascuna, tipo "altro", non un Obbligo: il
  titolo dell'allegato qualifica i profili come "raccomandati" e nessun articolo
  del regolamento rende obbligatoria la certificazione rispetto ai profili di
  questo allegato (gli articoli che rinviano agli allegati citano l'allegato I e
  l'allegato II, mai l'allegato III; il considerando 31 dello stesso atto - non
  censito qui, e' preambolo - precisa che l'allegato III contiene i profili di
  protezione raccomandati, che al momento dell'entrata in vigore del regolamento
  non sono documenti sullo stato dell'arte). Ogni lettera designa una categoria
  di prodotti TIC e i profili raccomandati per essa: e' una designazione di
  norme di riferimento, senza effetto giuridico dichiarato e senza definizioni,
  quindi "altro" e non "definitorio" ne' "scopo/ambito di applicazione".
- Granularita': UNA riga per lettera, non una per punto numerato. La lettera e'
  l'unita' che designa la categoria di prodotti TIC, e i punti (1)-(N) che la
  seguono sono le voci dell'elenco retto dalla lettera, ciascuna delle quali e'
  il nome di un profilo di protezione senza precetto autonomo: stessa
  convenzione delle lettere a)-i) dell'allegato del Reg. 2025/2532 ("un nodo per
  lettera, non uno per voce") e dell'elenco di norme di riferimento degli
  allegati I e II del Reg. 2024/2979 cap05 (elenco puramente enumerativo = una
  riga). Ogni punto numerato riceve comunque un item di indice proprio
  ("allegato III, lettera b), punto 2") mappato alla riga della sua lettera:
  ogni punto dell'allegato e' coperto da esattamente una riga, e il campo
  `testo` nomina ciascun profilo raccomandato.
- `oggetti_giuridici` non valorizzato per nessuna delle sette righe: fra i
  valori censiti non ce n'e' uno che corrisponda alle categorie di prodotto
  dell'allegato (documenti di viaggio a lettura ottica, tachigrafi digitali,
  circuiti integrati sicuri e smart card, punti di interazione e terminali di
  pagamento, dispositivi hardware con box di sicurezza), e la voce generica
  "altro" non e' stata forzata (stesso criterio di Reg. 2024/482 cap01; il cap02
  della stessa Fonte usa invece ["altro"], scelta non replicata qui). Dubbio
  dichiarato per la lettera b): "dispositivi di creazione di firma sicura" e' il
  termine della direttiva 1999/93/CE, mentre il valore censito piu' vicino e'
  "dispositivo qualificato di creazione di firma elettronica"; l'equivalenza non
  e' dichiarata dall'allegato (che non parla di dispositivi qualificati) e non
  e' stata forzata. Stesso dubbio per la lettera f), i cui profili riguardano
  moduli crittografici per operazioni di firma di un CSP.
- Nessuna riga valorizza `severita` o `sanzioni`: l'atto non gradua i requisiti
  ne' prevede sanzioni proprie. `stato` = "vigente" per tutte le righe.
- `testo_integrale`: verbatim e integrale, ricucito dalle righe spezzate dalla
  conversione XHTML -> testo. I marker isolati su riga propria sono uniti alla
  riga che seguono ("(a)" + "per la categoria dei documenti di viaggio a lettura
  ottica:", "(1)" + nome del profilo), come per le voci dell'art. 2 del cap01 di
  questa Fonte; i blocchi restano separati da riga vuota. La punteggiatura
  ufficiale e' conservata com'e', compreso il punto (1) della lettera b), che
  nel testo ufficiale non termina con ";". Nessun marcatore di elisione (vincolo
  `verifica_completezza_testo_integrale`, ADR-0010).
- RELAZIONI: sei relazioni interne, tutte fra nodi dichiarati in questo modulo e
  tutte con `evidence_type` "inferred" (il legame e' dedotto dal contenuto, non
  citato: il chapeau rinvia alle categorie "indicate di seguito" senza citare le
  lettere): ciascuna lettera (a)-(f) "specifica" il chapeau "allegato III", cioe'
  il nodo generale e' reso concreto dai nodi che nominano la categoria di
  prodotto e i profili raccomandati per essa (direzione specifico -> generale,
  come la relazione "specifica" del Reg. 2025/2532 cap01). `confidence` None:
  nessuno score reale da riportare (ADR-0005, non va inventato). Nessuna
  relazione verso altri capitoli di questa Fonte o verso altre Fonti: le
  costruisce la sessione principale in fase 6, e dichiararle qui in import
  parallelo per capitolo fa fallire il merge con KeyError.
- Rinvii demandati alla fase 6 (nessuna relazione dichiarata qui): il titolo
  dell'allegato -> allegato I di questa Fonte (cap09, settori tecnici e documenti
  sullo stato dell'arte); lettera c) punto 1, punto 3 e punto 4 -> regolamento di
  esecuzione (UE) 2016/799 della Commissione e regolamento (UE) n. 165/2014;
  lettera c) punto 2 -> allegato IB del regolamento (CE) n. 1360/2002. I profili
  di protezione nominati (BSI-CC-PP-0068-V2-2011-MA-01, BSI-CC-PP-0056-2009,
  BSI-CC-PP-0056-V2-2012-MA-02, BSI-CC-PP-0055-2009, le sei parti della norma EN
  419211, BSI-CC-PP-0084-2014, BSI-CC-PP-0099-2017, BSI-CC-PP-0101-2017,
  ANSSI-CC-PP-2015/07, ANSSI-CC-PP-2010/04, BSI-CC-PP-0089-2015,
  ANSSI-CC-PP-2015/01, ANSSI-CC-PP-2015/02, ANSSI-CC-PP-2015/03,
  ANSSI-CC-PP-2015/04, ANSSI-CC-PP-2015/05, ANSSI-CC-PP-2015/06,
  ANSSI-CC-PP-2015/08, ANSSI-CC-PP-2015/09, ANSSI-CC-PP-2015/10) non sono
  Fonti censite: nessun arco.
  L'allegato VI di questa Fonte (cap13) cita a sua volta i profili di protezione
  "elencato/i come documento sullo stato dell'arte nell'allegato II o III"
  (valutazione inter pares di tipo 3): e' un rinvio entrante, da costruire in
  fase 6 sui nodi di questo modulo.

Copertura: 36 item di indice, 7 righe (0 Obblighi + 7 Principi), 6 relazioni
interne.
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "allegato III",
        "testo": "L'allegato III contiene i profili di protezione raccomandati, cioè i profili di protezione utilizzati per la certificazione di prodotti TIC che rientrano nelle categorie di prodotti TIC indicate di seguito (lettere da a) a f)). La designazione non impone di per sé alcun comportamento: i profili sono raccomandati, non obbligatori.",
        "testo_integrale": "ALLEGATO III\n\nProfili di protezione raccomandati (che illustrano i settori tecnici di cua all'allegato I)\n\nProfili di protezione utilizzati per la certificazione di prodotti TIC che rientrano nella categoria di prodotti TIC indicata di seguito:",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato III, lettera a)",
        "testo": "Per la categoria dei documenti di viaggio a lettura ottica sono raccomandati quattro profili di protezione: PP Machine Readable Travel Document using Standard Inspection Procedure with PACE (BSI-CC-PP-0068-V2-2011-MA-01), PP for a Machine Readable Travel Document with «ICAO Application» Extended Access Control (BSI-CC-PP-0056-2009), PP for a Machine Readable Travel Document with «ICAO Application» Extended Access Control with PACE (BSI-CC-PP-0056-V2-2012-MA-02) e PP for a Machine Readable Travel Document with «ICAO Application» Basic Access Control (BSI-CC-PP-0055-2009).",
        "testo_integrale": "(a) per la categoria dei documenti di viaggio a lettura ottica:\n\n(1) PP Machine Readable Travel Document using Standard Inspection Procedure with PACE, BSI-CC-PP-0068-V2-2011-MA-01;\n\n(2) PP for a Machine Readable Travel Document with «ICAO Application» Extended Access Control, BSI-CC-PP-0056-2009;\n\n(3) PP for a Machine Readable Travel Document with «ICAO Application» Extended Access Control with PACE, BSI-CC-PP-0056-V2-2012-MA-02;\n\n(4) PP for a Machine Readable Travel Document with «ICAO Application» Basic Access Control, BSI-CC-PP-0055-2009;",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato III, lettera b)",
        "testo": "Per la categoria dei dispositivi di creazione di firma sicura sono raccomandate le sei parti della norma EN 419211: parte 1: visione d'insieme (EN 419211-1:2014), parte 2: dispositivi con generatore di chiave (EN 419211-2:2013), parte 3: dispositivi con importazione di chiave (EN 419211-3:2013), parte 4: estensione per dispositivo con generatore di chiave e canale sicuro per applicazione di generazione di certificato (EN 419211-4:2013), parte 5: estensione per dispositivo con generatore di chiave e canale sicuro per applicazione di creazione di firma (EN 419211-5:2013) e parte 6: estensione per il dispositivo con importazione di chiave e canale attendibile per applicazione di creazione di firma (EN 419211-6:2014).",
        "testo_integrale": "(b) per la categoria dei dispositivi di creazione di firma sicura:\n\n(1) EN 419211-1:2014 – Profili di protezione per dispositivi di creazione di firma sicura – Parte 1: visione d'insieme\n\n(2) EN 419211-2:2013 – Profili di protezione per dispositivi di creazione di firma sicura – Parte 2: dispositivi con generatore di chiave;\n\n(3) EN 419211-3:2013 – Profili di protezione per dispositivi di creazione di firma sicura – Parte 3: dispositivi con importazione di chiave;\n\n(4) EN 419211-4:2013 – Profili di protezione per dispositivi di creazione di firma sicura – Parte 4: estensione per dispositivo con generatore di chiave e canale sicuro per applicazione di generazione di certificato;\n\n(5) EN 419211-5:2013 – Profili di protezione per dispositivi di creazione di firma sicura – Parte 5: estensione per dispositivo con generatore di chiave e canale sicuro per applicazione di creazione di firma;\n\n(6) EN 419211-6:2014 – Profili di protezione per dispositivi di creazione di firma sicura – Parte 6: estensione per il dispositivo con importazione di chiave e canale attendibile per applicazione di creazione di firma;",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato III, lettera c)",
        "testo": "Per la categoria dei tachigrafi digitali sono raccomandati quattro profili di protezione, identificati per rinvio agli allegati IC e IB del regolamento di esecuzione (UE) 2016/799 e del regolamento (CE) n. 1360/2002: la carta tachigrafica come indicato nel regolamento di esecuzione (UE) 2016/799 (allegato IC), l'unità elettronica di bordo di cui all'allegato IB del regolamento (CE) n. 1360/2002 destinata al montaggio in veicoli per i trasporti stradali, il dispositivo esterno del GNSS (EGF PP) di cui all'allegato IC del regolamento di esecuzione (UE) 2016/799 e il sensore di movimento (MS PP) di cui all'allegato IC dello stesso regolamento di esecuzione.",
        "testo_integrale": "(c) per la categoria dei tachigrafi digitali:\n\n(1) tachigrafo digitale – carta tachigrafica, come indicato nel regolamento di esecuzione (UE) 2016/799 della Commissione, del 18 marzo 2016, che applica il regolamento (UE) n. 165/2014 (allegato IC);\n\n(2) tachigrafo digitale – unità elettronica di bordo di cui all'allegato IB del regolamento (CE) n. 1360/2002 della Commissione destinata al montaggio in veicoli per i trasporti stradali;\n\n(3) tachigrafo digitale – dispositivo esterno del GNSS (EGF PP) di cui all'allegato IC del regolamento di esecuzione (UE) 2016/799 della Commissione, del 18 marzo 2016, che applica il regolamento (UE) n. 165/2014 del Parlamento europeo e del Consiglio;\n\n(4) tachigrafo digitale – sensore di movimento (MS PP) di cui all'allegato IC del regolamento di esecuzione (UE) 2016/799 della Commissione, del 18 marzo 2016, che applica il regolamento (UE) n. 165/2014 del Parlamento europeo e del Consiglio;",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato III, lettera d)",
        "testo": "Per la categoria dei circuiti integrati sicuri, delle smart card e dei relativi dispositivi sono raccomandati sei profili di protezione: Security IC Platform PP (BSI-CC-PP-0084-2014), Java Card System - Open Configuration, V3.0.5 (BSI-CC-PP-0099-2017), Java Card System - Closed Configuration (BSI-CC-PP-0101-2017), PP for a PC Client Specific Trusted Platform Module Family 2.0 Level 0 Revision 1.16 (ANSSI-CC-PP-2015/07), PP Universal SIM card, PU-2009-RT-79 (ANSSI-CC-PP-2010/04) e Embedded UICC (eUICC) for Machine-to-Machine Devices (BSI-CC-PP-0089-2015).",
        "testo_integrale": "(d) per la categoria dei circuiti integrati sicuri, delle smart card e dei relativi dispositivi:\n\n(1) Security IC Platform PP, BSI-CC-PP-0084-2014;\n\n(2) Java Card System - Open Configuration, V3.0.5 BSI-CC-PP-0099-2017;\n\n(3) Java Card System - Closed Configuration, BSI-CC-PP-0101-2017;\n\n(4) PP for a PC Client Specific Trusted Platform Module Family 2.0 Level 0 Revision 1.16, ANSSI-CC-PP-2015/07;\n\n(5) PP Universal SIM card, PU-2009-RT-79, ANSSI-CC-PP-2010/04;\n\n(6) Embedded UICC (eUICC) for Machine-to-Machine Devices, BSI-CC-PP-0089-2015;",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato III, lettera e)",
        "testo": "Per la categoria dei punti di interazione (di pagamento) e dei terminali di pagamento sono raccomandati sei profili di protezione: punto di interazione «POI-CHIP-ONLY» (ANSSI-CC-PP-2015/01), «POI-CHIP-ONLY and Open Protocol Package» (ANSSI-CC-PP-2015/02), «POI-COMPREHENSIVE» (ANSSI-CC-PP-2015/03), «POI-COMPREHENSIVE and Open Protocol Package» (ANSSI-CC-PP-2015/04), «POI-PED-ONLY» (ANSSI-CC-PP-2015/05) e «POI-PED-ONLY and Open Protocol Package» (ANSSI-CC-PP-2015/06).",
        "testo_integrale": "(e) per la categoria dei punti di interazione (di pagamento) e dei terminali di pagamento:\n\n(1) punto di interazione «POI-CHIP-ONLY», ANSSI-CC-PP-2015/01;\n\n(2) punto di interazione «POI-CHIP-ONLY and Open Protocol Package», ANSSI-CC-PP-2015/02;\n\n(3) punto di interazione «POI-COMPREHENSIVE», ANSSI-CC-PP-2015/03;\n\n(4) punto di interazione «POI-COMPREHENSIVE and Open Protocol Package», ANSSI-CC-PP-2015/04;\n\n(5) punto di interazione «POI-PED-ONLY», ANSSI-CC-PP-2015/05;\n\n(6) punto di interazione «POI-PED-ONLY and Open Protocol Package», ANSSI-CC-PP-2015/06;",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato III, lettera f)",
        "testo": "Per la categoria dei dispositivi hardware con box di sicurezza sono raccomandati tre profili di protezione: Cryptographic Module for CSP Signing Operations with Backup – PP CMCSOB, PP HSM CMCSOB 14167-2 (ANSSI-CC-PP-2015/08), Cryptographic Module for CSP key generation services – PP CMCSOB, PP HSM CMCSOB 14167-3 (ANSSI-CC-PP-2015/09) e Cryptographic Module for CSP Signing Operations without Backup – PP CMCSO, PP HSM CMCKG 14167-4 (ANSSI-CC-PP-2015/10).",
        "testo_integrale": "(f) per la categoria dei dispositivi hardware con box di sicurezza:\n\n(1) Cryptographic Module for CSP Signing Operations with Backup – PP CMCSOB, PP HSM CMCSOB 14167-2, ANSSI-CC-PP-2015/08;\n\n(2) Cryptographic Module for CSP key generation services – PP CMCSOB, PP HSM CMCSOB 14167-3, ANSSI-CC-PP-2015/09;\n\n(3) Cryptographic Module for CSP Signing Operations without Backup – PP CMCSO, PP HSM CMCKG 14167-4, ANSSI-CC-PP-2015/10.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "allegato III",
    "allegato III, lettera a)",
    "allegato III, lettera a), punto 1",
    "allegato III, lettera a), punto 2",
    "allegato III, lettera a), punto 3",
    "allegato III, lettera a), punto 4",
    "allegato III, lettera b)",
    "allegato III, lettera b), punto 1",
    "allegato III, lettera b), punto 2",
    "allegato III, lettera b), punto 3",
    "allegato III, lettera b), punto 4",
    "allegato III, lettera b), punto 5",
    "allegato III, lettera b), punto 6",
    "allegato III, lettera c)",
    "allegato III, lettera c), punto 1",
    "allegato III, lettera c), punto 2",
    "allegato III, lettera c), punto 3",
    "allegato III, lettera c), punto 4",
    "allegato III, lettera d)",
    "allegato III, lettera d), punto 1",
    "allegato III, lettera d), punto 2",
    "allegato III, lettera d), punto 3",
    "allegato III, lettera d), punto 4",
    "allegato III, lettera d), punto 5",
    "allegato III, lettera d), punto 6",
    "allegato III, lettera e)",
    "allegato III, lettera e), punto 1",
    "allegato III, lettera e), punto 2",
    "allegato III, lettera e), punto 3",
    "allegato III, lettera e), punto 4",
    "allegato III, lettera e), punto 5",
    "allegato III, lettera e), punto 6",
    "allegato III, lettera f)",
    "allegato III, lettera f), punto 1",
    "allegato III, lettera f), punto 2",
    "allegato III, lettera f), punto 3",
]

MAPPATURA_LOCALE = {
    "allegato III": ["allegato III"],
    "allegato III, lettera a)": [
        "allegato III, lettera a)",
        "allegato III, lettera a), punto 1",
        "allegato III, lettera a), punto 2",
        "allegato III, lettera a), punto 3",
        "allegato III, lettera a), punto 4",
    ],
    "allegato III, lettera b)": [
        "allegato III, lettera b)",
        "allegato III, lettera b), punto 1",
        "allegato III, lettera b), punto 2",
        "allegato III, lettera b), punto 3",
        "allegato III, lettera b), punto 4",
        "allegato III, lettera b), punto 5",
        "allegato III, lettera b), punto 6",
    ],
    "allegato III, lettera c)": [
        "allegato III, lettera c)",
        "allegato III, lettera c), punto 1",
        "allegato III, lettera c), punto 2",
        "allegato III, lettera c), punto 3",
        "allegato III, lettera c), punto 4",
    ],
    "allegato III, lettera d)": [
        "allegato III, lettera d)",
        "allegato III, lettera d), punto 1",
        "allegato III, lettera d), punto 2",
        "allegato III, lettera d), punto 3",
        "allegato III, lettera d), punto 4",
        "allegato III, lettera d), punto 5",
        "allegato III, lettera d), punto 6",
    ],
    "allegato III, lettera e)": [
        "allegato III, lettera e)",
        "allegato III, lettera e), punto 1",
        "allegato III, lettera e), punto 2",
        "allegato III, lettera e), punto 3",
        "allegato III, lettera e), punto 4",
        "allegato III, lettera e), punto 5",
        "allegato III, lettera e), punto 6",
    ],
    "allegato III, lettera f)": [
        "allegato III, lettera f)",
        "allegato III, lettera f), punto 1",
        "allegato III, lettera f), punto 2",
        "allegato III, lettera f), punto 3",
    ],
}

# Relazioni interne a questo modulo (fonte_id_o_None = None su entrambi gli
# estremi). Sei relazioni "specifica", tutte con `evidence_type` "inferred":
# il chapeau dell'allegato designa i profili "utilizzati per la certificazione
# di prodotti TIC che rientrano nella categoria di prodotti TIC indicata di
# seguito" senza citare le lettere, e ciascuna lettera nomina la categoria di
# prodotto e i profili raccomandati per essa, rendendo concreto il nodo
# generale. `confidence` None: nessuno score reale da riportare (ADR-0005, non
# va inventato). I rinvii ad altri capitoli di questa Fonte (allegato I nel
# titolo, allegato VI in entrata) e ad altre Fonti (regolamento di esecuzione
# (UE) 2016/799, regolamento (UE) n. 165/2014, regolamento (CE) n. 1360/2002)
# non sono dichiarati qui: sono collegamenti della fase 6, elencati nel
# docstring.
RELAZIONI = [
    {
        "nodo_da": ("principio", None, "allegato III, lettera a)"),
        "nodo_a": ("principio", None, "allegato III"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "allegato III, lettera b)"),
        "nodo_a": ("principio", None, "allegato III"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "allegato III, lettera c)"),
        "nodo_a": ("principio", None, "allegato III"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "allegato III, lettera d)"),
        "nodo_a": ("principio", None, "allegato III"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "allegato III, lettera e)"),
        "nodo_a": ("principio", None, "allegato III"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "allegato III, lettera f)"),
        "nodo_a": ("principio", None, "allegato III"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": None,
    },
]
