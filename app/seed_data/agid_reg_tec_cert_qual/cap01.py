"""Regole Tecniche e Raccomandazioni AgID afferenti la generazione di
certificati elettronici qualificati, firme e sigilli elettronici qualificati
e validazioni temporali elettroniche qualificate (AgID, 13 feb 2020, ex
art. 71 CAD). Capitolo 1 di 3 (vedi
app/seed_data/agid_reg_tec_cert_qual/cap0[1-3].py): Capitolo 1 (Definizioni),
Capitolo 2 (Scopo e ambito di applicazione), Capitolo 3 (Obblighi). Testo
ufficiale in app/.source_cache/agid_reg_tec_cert_qual/raw.txt (fetch diretto
da docs.italia.it, documento breve non frazionato con split_source.py).

Modellazione (ADR-0007):
- Capitolo 1 (Definizioni): 5 voci del glossario introdotto dall'art. 1
  ("Agenzia", "CAD", "servizi", "regolamento eIDAS", "QTSP") -> 5 Principi
  distinti, tipo "definitorio" (un nodo per voce, non un riassunto unico,
  perché ciascuna voce ha contenuto normativo proprio distinto - a
  differenza del glossario alfabetico piatto di ETSI EN 319 401 cap01 dove
  la sintesi unica era giustificata dalla numerosità: qui sono solo 5 voci).
- Capitolo 2 (Scopo): il testo prosa (non numerato per commi) è diviso in 4
  unità logiche distinte:
  - §1 (primo paragrafo, "il regolamento eIDAS dispone...") -> Principio
    "scopo/ambito di applicazione" (individua il perimetro sostanziale:
    obblighi eIDAS in capo ai QTSP, requisiti di convalida di firme/
    sigilli/validazione temporale).
  - §2 (secondo paragrafo, "tali disposizioni individuano requisiti
    minimi... esempio del codice fiscale") -> Principio "altro" (motivazione
    del provvedimento, non designazione di perimetro in senso proprio, ma
    disposizione di cornice con contenuto interpretativo autonomo -
    l'esempio del codice fiscale è rilevante per intendere la ratio delle
    Raccomandazioni del capitolo 4).
  - §3 (terzo paragrafo, base giuridica art. 71 CAD, struttura del
    provvedimento, natura RFC 2119 delle "raccomandazioni") -> Principio
    "definitorio" (definisce la forza normativa delle "raccomandazioni" del
    capitolo 4: applicazione fortemente consigliata secondo RFC 2119, ma la
    disapplicazione non invalida firme/sigilli qualificati - nodo di
    riferimento per interpretare correttamente i nodi Obbligo del
    capitolo 4, che pur essendo modellati come Obbligo nel nostro schema
    - "prescrizione che impone un comportamento" - restano legalmente
    "raccomandazioni" e non "obblighi" nel senso stretto del testo
    originale, si veda nota di modellazione in cap02.py).
  - §4 (ultimo paragrafo, clausola di prevalenza/disapplicazione in caso di
    contrasto con future versioni del regolamento eIDAS) -> Principio
    "altro" (clausola di gerarchia delle fonti, non impone un comportamento
    a un soggetto specifico).
- Capitolo 3 (Obblighi, art. 24 §2 lett. e) e lett. d) eIDAS):
  - 3.1 §1 (liberta' di scelta di hash/algoritmi crittografici, purche'
    adeguati) -> Obbligo, tipo "tecnico/sicurezza": pur formulato in termini
    di liberta' di scelta, il vincolo di adeguatezza e' il contenuto
    prescrittivo proprio (il QTSP deve accertarsi che hash/algoritmi
    scelti siano adeguati).
  - 3.1 §2 (obbligo di informare l'Agenzia sulla scelta effettuata) ->
    Obbligo, tipo "informativo/trasparenza". Soggetto obbligato QTSP;
    nessuna categoria "destinatario" valorizzata per l'Agenzia (non e' una
    categoria di soggetto censita - stesso trattamento gia' riservato alle
    norme CAD/SPID indirizzate ad AgID, vedi note di modellazione in
    app/seed_data/cad/cap04.py e app/seed_data/spid/cap02.py).
  - 3.2 (obbligo di informare i destinatari dei servizi sull'applicazione o
    disapplicazione delle raccomandazioni del capitolo 4) -> Obbligo, tipo
    "informativo/trasparenza". Soggetto obbligato QTSP, soggetto
    destinatario "Utente/titolare" (i "destinatari dei servizi").
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "par. 3.1 §1",
        "testo": "Nell'ambito dei servizi fiduciari qualificati volti all'emissione di certificati qualificati e ai sistemi di validazione temporale elettronica qualificata, i QTSP sono liberi di scegliere le funzioni di hash e gli algoritmi crittografici con lunghezza delle chiavi, purché adeguati a ottemperare all'art. 24 §2 lett. e) del regolamento eIDAS.",
        "testo_integrale": "Nell'ambito dei servizi fiduciari qualificati volti all'emissione di certificati qualificati e ai sistemi di validazione temporale elettronica qualificata, i prestatori di servizi fiduciari qualificati sono liberi di utilizzare le funzioni di hash e gli algoritmi crittografici con lunghezza delle chiavi purché adeguati al fine di ottemperare a quanto prescritto dall'articolo 24, paragrafo 2, lettera e del regolamento eIDAS.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 3.1 §2",
        "testo": "Ai fini dell'art. 21 §2 e dell'art. 24 §2 lett. a) del regolamento eIDAS, i QTSP devono informare l'Agenzia in merito alla scelta effettuata di hash/algoritmi crittografici e di come essa soddisfi l'art. 24 §2 lett. e) eIDAS.",
        "testo_integrale": "Ai fini dell'articolo 21, paragrafo 2, e dell'articolo 24, paragrafo 2, lettera a del regolamento eIDAS, detti prestatori di servizi devono informare l'Agenzia in merito alla scelta effettuata e di come soddisfi quanto prescritto dall'articolo 24, paragrafo 2, lettera e del regolamento eIDAS.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 3.2",
        "testo": "Ai sensi dell'art. 24 §2 lett. d) del regolamento eIDAS, i QTSP devono informare in modo chiaro e completo i destinatari dei servizi in merito all'applicazione o eventuale disapplicazione delle raccomandazioni del successivo paragrafo 4 e delle possibili conseguenze.",
        "testo_integrale": "Ai sensi dell'art. 24, paragrafo 2, lettera d del regolamento eIDAS, i destinatari dei servizi devono essere informati in modo chiaro e completo anche in merito all'applicazione o eventuale disapplicazione delle raccomandazioni di cui al successivo paragrafo 4 e delle possibili conseguenze.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 1, def. «Agenzia»",
        "testo": "Definisce «Agenzia»: l'Agenzia per l'Italia Digitale.",
        "testo_integrale": "Agenzia: l'Agenzia per l'Italia Digitale;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 1, def. «CAD»",
        "testo": "Definisce «CAD»: D.Lgs. 7 marzo 2005 n.82, Codice dell'Amministrazione Digitale, e successive modificazioni.",
        "testo_integrale": "CAD: D.Lgs. 7 marzo 2005 №82, Codice dell'Amministrazione Digitale, e successive modificazioni;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 1, def. «servizi»",
        "testo": "Definisce «servizi»: i servizi di cui all'art. 29 comma 1 del CAD.",
        "testo_integrale": "servizi: i servizi di cui all'art.29 comma 1 del CAD;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 1, def. «regolamento eIDAS»",
        "testo": "Definisce «regolamento eIDAS»: Regolamento (UE) n.910/2014 del Parlamento Europeo e del Consiglio, del 23 luglio 2014, in materia di identificazione elettronica e servizi fiduciari per le transazioni elettroniche nel mercato interno, che abroga la direttiva 1999/93/CE.",
        "testo_integrale": "regolamento eIDAS: Regolamento (UE) №910/2014 del Parlamento Europeo e del Consiglio, del 23 luglio 2014, in materia di identificazione elettronica e servizi fiduciari per le transazioni elettroniche nel mercato interno e che abroga la direttiva 1999/93/CE;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1, def. «QTSP»",
        "testo": "Definisce «QTSP»: prestatore di servizi fiduciari qualificati ai sensi del regolamento eIDAS.",
        "testo_integrale": "QTSP: prestatore di servizi fiduciari qualificati ai sensi del regolamento eIDAS.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "par. 2 §1",
        "testo": "Il regolamento eIDAS dispone alcuni obblighi in capo ai QTSP che emettono certificati qualificati per la generazione di firme e sigilli, individua i requisiti per la convalida delle firme elettroniche qualificate (art. 32) e, mutatis mutandis, dei sigilli elettronici qualificati (art. 40), come anche i requisiti per la validazione temporale elettronica qualificata (art. 42).",
        "testo_integrale": "Il regolamento eIDAS dispone alcuni obblighi in capo ai QTSP che emettono certificati qualificati per la generazione di firme e sigilli, individua i requisiti per la convalida delle firme elettroniche qualificate (art. 32) e mutatis mutandis, dei sigilli elettronici qualificati (art. 40), come anche i requisiti per la validazione temporale elettronica qualificata (art. 42).",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": [
            "certificato qualificato di firma elettronica",
            "certificato qualificato di sigillo elettronico",
            "marca temporale elettronica qualificata",
        ],
    },
    {
        "riferimento": "par. 2 §2",
        "testo": "Le disposizioni eIDAS individuano requisiti minimi che possono risultare non adeguati per la fruizione di servizi in rete nel contesto italiano: ad esempio l'assenza dell'obbligo di indicare nel certificato qualificato di firma il codice fiscale del titolare, elemento indispensabile per diverse pubbliche amministrazioni italiane. Questa è la ratio delle Raccomandazioni del paragrafo 4.",
        "testo_integrale": "Tali disposizioni individuano dei requisiti minimi che possono risultare non adeguati per la fruizione di servizi in rete offerti nello specifico contesto italiano. Un esempio in tal senso è l'assenza dell'obbligo di indicare nel certificato qualificato per la generazione della firma il codice fiscale del titolare, elemento indispensabile per diverse pubbliche amministrazioni italiane.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["certificato qualificato di firma elettronica"],
    },
    {
        "riferimento": "par. 2 §3",
        "testo": "Il provvedimento, emanato ex art. 71 CAD, contiene nel paragrafo 3 (Obblighi) previsioni rese obbligatorie in forza/attuazione del regolamento eIDAS, e nel paragrafo 4 (Raccomandazioni) indicazioni per l'interoperabilità nel contesto italiano. Le «raccomandazioni», pur non essendo «obblighi», vanno interpretate nel significato RFC 2119: applicazione fortemente consigliata, ma la loro disapplicazione non comporta l'invalidità di firme o sigilli elettronici qualificati. Il paragrafo 5 contiene indicazioni per il processo di convalida.",
        "testo_integrale": "Pertanto, il presente provvedimento, emanato ai sensi dell'articolo 71 del CAD, contiene nel paragrafo 3 (pagina 7) (Obblighi) alcune previsioni rese obbligatorie in forza o in attuazione del regolamento eIDAS, mentre nel paragrafo 4 (pagina 9) (Raccomandazioni) indicazioni volte a garantire maggiormente l'interoperabilità e la fruizione dei servizi in rete nel contesto italiano. Sebbene indicate come \"raccomandazioni\" devono essere interpretate nel significato previsto nella RFC 2119, pertanto la loro applicazione è fortemente consigliata. È evidente che trattandosi di raccomandazioni e non di obblighi, la loro disapplicazione non possa comportare l'invalidità di firme o sigilli elettronici qualificati. Il paragrafo 5 (pagina 13) contiene alcune indicazioni per il processo di convalida di firme e sigilli elettronici.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "par. 2 §4",
        "testo": "Le disposizioni delle presenti regole tecniche in contrasto con future versioni del regolamento eIDAS o dei regolamenti esecutivi derivanti devono essere disapplicate (clausola di prevalenza del diritto UE sovraordinato).",
        "testo_integrale": "Le disposizioni contenute nelle presenti regole tecniche che risultino in contrasto con future versioni del regolamento eIDAS o dei regolamenti esecutivi derivanti, devono essere disapplicate.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 1, def. «Agenzia»",
    "art. 1, def. «CAD»",
    "art. 1, def. «servizi»",
    "art. 1, def. «regolamento eIDAS»",
    "art. 1, def. «QTSP»",
    "par. 2 §1",
    "par. 2 §2",
    "par. 2 §3",
    "par. 2 §4",
    "par. 3.1 §1",
    "par. 3.1 §2",
    "par. 3.2",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "par. 3.1 §1"),
        "nodo_a": ("obbligo", None, "par. 3.1 §2"),
        "tipo_relazione": "richiede come precondizione",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("principio", None, "par. 2 §3"),
        "nodo_a": ("principio", None, "par. 2 §1"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
    {
        "nodo_da": ("principio", None, "par. 2 §2"),
        "nodo_a": ("principio", None, "par. 2 §1"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
]
