"""ETSI EN 319 412-3 V1.4.1 (2026-07) - Electronic Signatures and Trust
Infrastructures (ESI); Certificate Profiles; Part 3: Certificate profile for
certificates issued to legal persons. Fonte 7 (ETSI EN 319 412, fonte unica
multi-parte, comprende gia' la Parte 5 QCStatements), un unico capitolo
(documento tecnico breve, ~9 pagine di contenuto sostanziale, sta comodamente
nel contesto di una sessione principale - nessuna suddivisione per subagent
necessaria). Testo ufficiale in
app/.source_cache/etsi_319_412/parte3_raw.txt.

Modellazione (ADR-0007), stesso criterio gia' applicato a Parte 5
(app/seed_data/etsi_319_412/parte5.py):

- Ogni "item di indice" e' una clausola o un requisito numerato del testo
  (es. "LEG-4.2.1-1", "clausola 1 (Scope)"), un nodo per disposizione.
- Front matter puramente amministrativo/bibliografico (Contents, Intellectual
  Property Rights, Foreword, Modal verbs terminology, Introduction, clausola
  2 References - normative e informative, e' solo bibliografia -, Annex A
  informative Change history, History) NON e' modellato come nodo, stesso
  trattamento riservato alla Parte 5. Nessun discrimine di rilevanza sulle
  clausole sostanziali: la clausola 3 (Definition of terms, symbols,
  abbreviations and notations) e' comunque coperta con un unico nodo
  aggregato "definitorio" anche se il contenuto e' quasi interamente un
  rinvio ad altre parti dello stesso deliverable (3.1/3.4 rinviano a Part 1,
  3.3 rinvia a Part 2, 3.2 e' "Void.") - stesso trattamento gia' riservato a
  clausole di rinvio/void nella Parte 5.
- Requisiti "shall"/"shall not"/"should" con soggetto obbligato implicito (il
  QTSP/gestore che emette il certificato) -> Obbligo, categoria_soggetto
  "QTSP/gestore", ruolo "obbligato", tipo_obbligo "tecnico/sicurezza" (sono
  tutti requisiti di profilo tecnico del certificato, coerente con la
  Parte 5). Le clausole 4.1 (Generic requirements), 4.2.1 (Subject) e 4.3.1
  (Key usage) sono interamente requisiti di questo tipo, incluse le
  disapplicazioni esplicite di clausole di ETSI EN 319 412-2 (LEG-4.2.1-1,
  LEG-4.3.1-1) che sono comunque un vincolo tecnico vincolante sul profilo
  risultante, non una mera nota descrittiva.
- Requisiti con condizione esplicita ("if present", "may include") ->
  Obbligo con condizione_applicabilita valorizzato, mai escluso: LEG-4.2.1-7
  (semantics identifiers opzionali, applicabile solo se inclusi) e
  LEG-4.2.1-9 (limite di lunghezza IETF RFC 5280 derogabile solo se
  l'attributo e' presente e supera il limite).
- Clausola 1 (Scope) -> Principio "scopo/ambito di applicazione".
- Clausola 3 (Definition of terms...) -> Principio "definitorio" aggregato
  (un solo nodo per l'intera clausola 3, comprese le sue 4 sottoclausole
  3.1-3.4, coerente con l'istruzione di censimento assegnata).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "Parte 3: LEG-4.1-1",
        "testo": "Tutti i campi ed estensioni del certificato devono rispettare ETSI EN 319 412-2, con le modifiche specificate nel presente documento.",
        "testo_integrale": "LEG-4.1-1: All certificate fields and extensions shall comply with ETSI EN 319 412-2 [2] with the amendments specified in the present document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 3: LEG-4.2.1-1",
        "testo": "La clausola 4.2.4 di ETSI EN 319 412-2 (relativa al subject nei certificati per persone fisiche) non si applica ai certificati per persone giuridiche disciplinati dal presente documento.",
        "testo_integrale": "LEG-4.2.1-1: Clause 4.2.4 of ETSI EN 319 412-2 [2] shall not apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 3: LEG-4.2.1-2",
        "testo": "Il campo subject deve includere almeno i seguenti attributi, come specificato nella Raccomandazione ITU-T X.520: countryName; organizationName; organizationIdentifier; e commonName.",
        "testo_integrale": "LEG-4.2.1-2: The subject field shall include at least the following attributes as specified in Recommendation ITU-T X.520 [1]: \u2022 countryName; \u2022 organizationName; \u2022 organizationIdentifier; and \u2022 commonName.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 3: LEG-4.2.1-3",
        "testo": "Deve essere presente una sola istanza di ciascuno degli attributi countryName, organizationName, organizationIdentifier e commonName; possono essere presenti attributi aggiuntivi.",
        "testo_integrale": "LEG-4.2.1-3: Only one instance of each of these attributes shall be present. Additional attributes may be present.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 3: LEG-4.2.1-4",
        "testo": "L'attributo countryName deve specificare il paese in cui il soggetto (persona giuridica) e' stabilito.",
        "testo_integrale": "LEG-4.2.1-4: The countryName attribute shall specify the country in which the subject (legal person) is established.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 3: LEG-4.2.1-5",
        "testo": "L'attributo organizationName deve contenere il nome completo registrato del soggetto (persona giuridica).",
        "testo_integrale": "LEG-4.2.1-5: The organizationName attribute shall contain the full registered name of the subject (legal person).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 3: LEG-4.2.1-6",
        "testo": "L'attributo organizationIdentifier deve contenere un identificativo dell'organizzazione soggetto, distinto dal nome dell'organizzazione.",
        "testo_integrale": "LEG-4.2.1-6: The organizationIdentifier attribute shall contain an identification of the subject organization different from the organization name.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 3: LEG-4.2.1-7",
        "testo": "I certificati possono includere uno o piu' semantics identifier come specificato nella clausola 5 di ETSI EN 319 412-1.",
        "testo_integrale": "LEG-4.2.1-7: Certificates may include one or more semantics identifiers as specified in clause 5 of ETSI EN 319 412-1 [i.4].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il QTSP/gestore sceglie di includere uno o piu' semantics identifier nel certificato",
    },
    {
        "riferimento": "Parte 3: LEG-4.2.1-8",
        "testo": "Il valore dell'attributo commonName deve contenere un nome comunemente usato dal soggetto per rappresentarsi; tale nome non deve necessariamente corrispondere esattamente al nome dell'organizzazione integralmente registrato.",
        "testo_integrale": "LEG-4.2.1-8: The commonName attribute value shall contain a name commonly used by the subject to represent itself. This name needs not be an exact match of the fully registered organization name.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 3: LEG-4.2.1-9",
        "testo": "Se presenti, i valori di organizationName, organizationalUnitName e commonName possono essere piu' lunghi del limite previsto da IETF RFC 5280 (nota: se si applicano altri limiti, si prevede che questo sia dichiarato nella certification practice statement o nei termini e condizioni pubblicati dal TSP).",
        "testo_integrale": "LEG-4.2.1-9: If present, the size of organizationName, organizationalUnitName and commonName may be longer than the limit as stated in IETF RFC 5280 [3]. NOTE: If other limits are applied it is expected that this is stated in the TSP's published certification practice statement or terms and conditions.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se gli attributi organizationName, organizationalUnitName o commonName sono presenti e il TSP sceglie di superare il limite di lunghezza previsto da IETF RFC 5280",
    },
    {
        "riferimento": "Parte 3: LEG-4.3.1-1",
        "testo": "La clausola 4.3.2 di ETSI EN 319 412-2 (key usage) non si applica, salvo per le parti richiamate espressamente di seguito.",
        "testo_integrale": "LEG-4.3.1-1: Clause 4.3.2 of ETSI EN 319 412-2 [2] shall not apply, except those parts which are referenced below.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 3: LEG-4.3.1-2",
        "testo": "Il paragrafo 1 e la successiva tabella 1 della clausola 4.3.2 di ETSI EN 319 412-2 si applicano.",
        "testo_integrale": "LEG-4.3.1-2: Clause 4.3.2 of ETSI EN 319 412-2 [2], paragraph 1 and subsequent table 1 shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 3: LEG-4.3.1-3",
        "testo": "I certificati usati per validare firme digitali su contenuti (es. documenti, accordi e/o transazioni) che forniscono evidenza di origine e integrita' del contenuto devono essere limitati ai tipi A, B o F.",
        "testo_integrale": "LEG-4.3.1-3: Certificates used to validate digital signatures over content (e.g. documents, agreements and/or transactions) that provide evidence of origin and integrity of the content shall be limited to type A, B or F. EXAMPLE: Digital signatures which are aimed to be used as advanced electronic seals as defined in Regulation (EU) No 910/2014 [i.3] are considered to provide evidence of origin and integrity of the content. NOTE 1: See note 1 in clause 4.3.2 of ETSI EN 319 412-2 [2]. NOTE 2: See note 2 in clause 4.3.2 of ETSI EN 319 412-2 [2].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 3: LEG-4.3.1-4",
        "testo": "Tra le alternative dei tipi A, B o F, dovrebbe essere usato il tipo A (vedi la security note 2 di cui sopra).",
        "testo_integrale": "LEG-4.3.1-4: Of these alternatives, type A should be used (see the security note 2 below).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "Parte 3: clausola 1 (Scope)",
        "testo": "Il documento specifica un profilo di certificato per certificati emessi a persone giuridiche, che si basa sui requisiti definiti in ETSI EN 319 412-2 (profilo per persone fisiche). Il documento supporta i requisiti dei certificati qualificati UE come specificato nel Regolamento (UE) 910/2014, oltre che altre forme di certificato.",
        "testo_integrale": "1 Scope: The present document specifies a certificate profile for certificates issued to legal persons. The profile defined in the present document builds on requirements defined in ETSI EN 319 412-2 [2]. The present document supports the requirements of EU qualified certificates as specified in the Regulation (EU) No 910/2014 [i.3] as well as other forms of certificate.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 3: clausola 3 (definizioni, simboli, abbreviazioni, notazioni)",
        "testo": "Per i termini si applicano quelli dati in ETSI EN 319 412-1 (clausola 3.1); i simboli sono \"Void\" (clausola 3.2, nessun simbolo definito); per le abbreviazioni si applicano quelle date in ETSI EN 319 412-2 (clausola 3.3); per le notazioni si applicano quelle date in ETSI EN 319 412-1 (clausola 3.4).",
        "testo_integrale": "3.1 Terms: For the purposes of the present document, the terms given in ETSI EN 319 412-1 [i.4] apply. 3.2 Symbols: Void. 3.3 Abbreviations: For the purposes of the present document, the abbreviations given in ETSI EN 319 412-2 [2] apply. 3.4 Notations: For the purposes of the present document, the notations given in ETSI EN 319 412-1 [i.4] apply.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Parte 3: clausola 1 (Scope)",
    "Parte 3: clausola 3 (definizioni, simboli, abbreviazioni, notazioni)",
    "Parte 3: LEG-4.1-1",
    "Parte 3: LEG-4.2.1-1",
    "Parte 3: LEG-4.2.1-2",
    "Parte 3: LEG-4.2.1-3",
    "Parte 3: LEG-4.2.1-4",
    "Parte 3: LEG-4.2.1-5",
    "Parte 3: LEG-4.2.1-6",
    "Parte 3: LEG-4.2.1-7",
    "Parte 3: LEG-4.2.1-8",
    "Parte 3: LEG-4.2.1-9",
    "Parte 3: LEG-4.3.1-1",
    "Parte 3: LEG-4.3.1-2",
    "Parte 3: LEG-4.3.1-3",
    "Parte 3: LEG-4.3.1-4",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
