"""Codice Civile (R.D. 16 marzo 1942, n. 262). Fonte 16.

IMPORT SELETTIVO, non granulare (deroga esplicita ad ADR-0007 concordata con
l'utente il 2026-09-23): il Codice Civile conta circa 3.000 articoli; la
copertura completa per articolo (ADR-0007) non è stata richiesta né voluta
per questa Fonte. Importati solo i 6 articoli che le Fonti già censite
(CAD, fonte_id 3; DPCM 22/2/2013, fonte_id 4) citano espressamente per
riferimento, individuati con una ricerca full-text `CONTAINS` case-insensitive
su "codice civile"/"cod. civ." nel campo `testo_integrale` di tutti i nodi
Obbligo/Principio del grafo in sessione interattiva (non pipeline
grep-su-testo-ufficiale, perché qui non esiste un testo ufficiale grezzo del
Codice Civile in `app/.source_cache/` — la fonte "grezza" per il grep è il
grafo stesso):

- art. 1350 c.c. (Atti che devono farsi per iscritto) — citato da CAD
  art. 21 c.2-bis.
- art. 2702 c.c. (Efficacia della scrittura privata) — citato da CAD
  art. 20 c.1-bis.
- art. 2703 c.c. (Sottoscrizione autenticata) — citato da CAD art. 25 c.1 e
  da DPCM 22/2/2013 art. 25 c.1.
- art. 2712 c.c. (Riproduzioni meccaniche) — CAD art. 23-quater c.1 lo
  modifica espressamente (novella che inserisce "informatiche" accanto a
  "fotografiche"); testo qui riportato già comprensivo della modifica (testo
  vigente).
- art. 2714 c.c. (Copie di atti pubblici) — citato da CAD art. 22 c.1.
- art. 2715 c.c. (Copie di scritture private originali depositate) —
  citato da CAD art. 22 c.1.

CAD art. 61 c.1 (rinvio generico "ai principi stabiliti dal codice civile",
senza articolo puntuale) è stato escluso su indicazione esplicita
dell'utente: riferimento troppo vago per giustificare un nodo/una relazione.

Testo verbatim recuperato da fonti secondarie che riproducono il testo
vigente Normattiva (ilcaso.it, brocardi.it, cross-verificate tra loro),
Normattiva stesso non restituisce testo articolo-per-articolo in lettura
programmatica (naviga via JavaScript). Nessun marcatore di elisione:
`testo_integrale` di ogni nodo è la disposizione per intero.

Modellazione: tutti e 6 gli articoli sono censiti come Principio (norme
dichiarative che stabiliscono un effetto giuridico/valore probatorio, senza
soggetto obbligato in senso QTSP) — nessuno impone un comportamento a un
soggetto censito nel senso di Obbligo. `tipo_principio`: "valore probatorio"
per 2702/2703/2712/2714/2715 (tutti disciplinano l'efficacia probatoria di un
documento/copia/sottoscrizione); "altro" per 1350 (requisito di forma ad
substantiam, non un valore probatorio in senso proprio — nessun tipo
dedicato in tassonomia).

Fase 6 (ADR-0009), direzione invertita rispetto al caso tipico: qui è la
Fonte già censita (CAD/DPCM) a citare il Codice Civile appena importato, non
il contrario. Le 7 relazioni sotto sono quindi codificate direttamente
(evidence_type "textual", confidence alta: citazione testuale esplicita
riconosciuta a mano durante l'analisi propedeutica all'import, non tramite
la pipeline grep+KNN+classificazione-LLM di ADR-0009 — shortlist già
esaustiva e verificata one-to-one nel turno di conversazione precedente,
KNN/LLM non avrebbero aggiunto nulla su un caso così piccolo e già
disambiguato). Verificato che nessun'altra Fonte censita (eIDAS/eIDAS2, DPCM
24/10/2014 SPID, DPCM 19/10/2021, standard ETSI, Regolamenti UE, Regolamenti
AgID) cita testualmente "codice civile"/"cod. civ." nei propri nodi (stessa
ricerca full-text, zero risultati fuori da CAD/DPCM 22/2/2013): nessuna
relazione aggiuntiva da queste Fonti verso il Codice Civile — esito
verificato, non fase saltata.
"""

RIGHE_OBBLIGHI: list[dict] = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 1350",
        "testo": "Un elenco tassativo di atti — trasferimento o costituzione di "
                 "diritti reali immobiliari, locazioni ultranovennali, conferimenti "
                 "societari di godimento immobiliare ultranovennale, rendite, "
                 "divisioni immobiliari, transazioni sui medesimi rapporti, e ogni "
                 "altro atto specialmente indicato dalla legge — deve rivestire la "
                 "forma dell'atto pubblico o della scrittura privata, a pena di "
                 "nullità.",
        "testo_integrale": "Devono farsi per atto pubblico o per scrittura privata, "
                            "sotto pena di nullità:\n"
                            "1) i contratti che trasferiscono la proprietà di beni "
                            "immobili;\n"
                            "2) i contratti che costituiscono, modificano o "
                            "trasferiscono il diritto di usufrutto su beni immobili, "
                            "il diritto di superficie, il diritto del concedente e "
                            "dell'enfiteuta;\n"
                            "3) i contratti che costituiscono la comunione di diritti "
                            "indicati dai numeri precedenti;\n"
                            "4) i contratti che costituiscono o modificano le "
                            "servitù prediali, il diritto di uso su beni immobili e "
                            "il diritto di abitazione;\n"
                            "5) gli atti di rinunzia ai diritti indicati dai numeri "
                            "precedenti;\n"
                            "6) i contratti di affrancazione del fondo enfiteutico;\n"
                            "7) i contratti di anticresi;\n"
                            "8) i contratti di locazione di beni immobili per una "
                            "durata superiore a nove anni;\n"
                            "9) i contratti di società o di associazione con i quali "
                            "si conferisce il godimento di beni immobili o di altri "
                            "diritti reali immobiliari per un tempo eccedente i nove "
                            "anni o per un tempo indeterminato;\n"
                            "10) gli atti che costituiscono rendite perpetue o "
                            "vitalizie, salve le disposizioni relative alle rendite "
                            "dello Stato;\n"
                            "11) gli atti di divisione di beni immobili e di altri "
                            "diritti reali immobiliari;\n"
                            "12) le transazioni che hanno per oggetto controversie "
                            "relative ai rapporti giuridici menzionati nei numeri "
                            "precedenti;\n"
                            "13) gli altri atti specialmente indicati dalla legge.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2702",
        "testo": "La scrittura privata fa piena prova, fino a querela di falso, "
                 "della provenienza delle dichiarazioni dal sottoscrittore, se "
                 "questi ne riconosce la sottoscrizione oppure se questa è "
                 "legalmente considerata come riconosciuta (es. autenticazione "
                 "notarile ex art. 2703 c.c., firma digitale ex art. 20 CAD).",
        "testo_integrale": "La scrittura privata fa piena prova, fino a querela di "
                            "falso, della provenienza delle dichiarazioni da chi "
                            "l'ha sottoscritta, se colui contro il quale la "
                            "scrittura è prodotta ne riconosce la sottoscrizione, "
                            "ovvero se questa è legalmente considerata come "
                            "riconosciuta.",
        "tipo_principio": "valore probatorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2703",
        "testo": "La sottoscrizione di una scrittura privata si ha per riconosciuta "
                 "quando è autenticata da un notaio o da altro pubblico ufficiale "
                 "autorizzato; l'autenticazione consiste nell'attestazione, da "
                 "parte del pubblico ufficiale, che la sottoscrizione è stata "
                 "apposta in sua presenza, previo accertamento dell'identità del "
                 "sottoscrittore.",
        "testo_integrale": "Si ha per riconosciuta la sottoscrizione autenticata "
                            "dal notaio o da altro pubblico ufficiale a ciò "
                            "autorizzato.\n"
                            "L'autenticazione consiste nell'attestazione da parte "
                            "del pubblico ufficiale che la sottoscrizione è stata "
                            "apposta in sua presenza. Il pubblico ufficiale deve "
                            "previamente accertare la identità della persona che "
                            "sottoscrive.",
        "tipo_principio": "valore probatorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2712",
        "testo": "Le riproduzioni fotografiche, informatiche o cinematografiche, le "
                 "registrazioni fonografiche e ogni altra rappresentazione "
                 "meccanica di fatti e cose formano piena prova dei fatti e delle "
                 "cose rappresentate, salvo disconoscimento di conformità da parte "
                 "di chi se le vede prodotte contro. Testo vigente, comprensivo "
                 "della modifica introdotta da CAD art. 23-quater c.1 (inserimento "
                 "di \"informatiche\" accanto a \"fotografiche\").",
        "testo_integrale": "Le riproduzioni fotografiche, informatiche o "
                            "cinematografiche, le registrazioni fonografiche e, in "
                            "genere, ogni altra rappresentazione meccanica di fatti "
                            "e di cose formano piena prova dei fatti e delle cose "
                            "rappresentate, se colui contro il quale sono prodotte "
                            "non ne disconosce la conformità ai fatti o alle cose "
                            "medesime.",
        "tipo_principio": "valore probatorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2714",
        "testo": "Le copie di atti pubblici spedite nelle forme prescritte da "
                 "depositari pubblici autorizzati fanno fede come l'originale; la "
                 "stessa fede fanno le copie di copie di atti pubblici originali, "
                 "spedite da depositari pubblici di esse a ciò autorizzati.",
        "testo_integrale": "Le copie di atti pubblici spedite nelle forme "
                            "prescritte da depositari pubblici autorizzati fanno "
                            "fede come l'originale.\n"
                            "La stessa fede fanno le copie di copie di atti "
                            "pubblici originali, spedite da depositari pubblici di "
                            "esse, a ciò autorizzati.",
        "tipo_principio": "valore probatorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2715",
        "testo": "Le copie delle scritture private depositate presso pubblici "
                 "uffici, se spedite da pubblici depositari autorizzati, hanno la "
                 "stessa efficacia probatoria della scrittura originale da cui "
                 "sono estratte.",
        "testo_integrale": "Le copie delle scritture private depositate presso "
                            "pubblici uffici e spedite da pubblici depositari "
                            "autorizzati hanno la stessa efficacia della scrittura "
                            "originale da cui sono estratte.",
        "tipo_principio": "valore probatorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 1350",
    "art. 2702",
    "art. 2703",
    "art. 2712",
    "art. 2714",
    "art. 2715",
]

MAPPATURA_LOCALE = {
    "art. 1350": ["art. 1350"],
    "art. 2702": ["art. 2702"],
    "art. 2703": ["art. 2703"],
    "art. 2712": ["art. 2712"],
    "art. 2714": ["art. 2714"],
    "art. 2715": ["art. 2715"],
}

RELAZIONI = [
    {
        "nodo_da": ("principio", 3, "art. 20 c.1-bis"),
        "nodo_a": ("principio", None, "art. 2702"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", 3, "art. 21 c.2-bis"),
        "nodo_a": ("principio", None, "art. 1350"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("principio", 3, "art. 22 c.1"),
        "nodo_a": ("principio", None, "art. 2714"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("principio", 3, "art. 22 c.1"),
        "nodo_a": ("principio", None, "art. 2715"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("principio", 3, "art. 23-quater c.1"),
        "nodo_a": ("principio", None, "art. 2712"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
    {
        "nodo_da": ("principio", 3, "art. 25 c.1"),
        "nodo_a": ("principio", None, "art. 2703"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", 4, "art. 25 c.1"),
        "nodo_a": ("principio", None, "art. 2703"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
]
