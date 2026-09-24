"""ETSI EN 319 412-2 V2.5.1 (2026-08) - Electronic Signatures and Trust
Infrastructures (ESI); Certificate Profiles; Part 2: Certificate profile for
certificates issued to natural persons. Fonte 7 (stessa fonte multi-parte di
parte5.py/QCStatements), un unico modulo (documento tecnico di 16 pagine).
Testo ufficiale in app/.source_cache/etsi_319_412/parte2_raw.txt (fetch
diretto dal repository ETSI deliver, 2026-09-23).

Modellazione (ADR-0007), stesso approccio di parte5.py adattato a questa
parte del deliverable:

- Ogni "item di indice" e' una clausola o un requisito numerato del testo
  (es. "GEN-4.1-1", "NAT-4.2.4-12A", "clausola 1 (Scope)"). Front matter
  puramente amministrativo/bibliografico (Intellectual Property Rights,
  Foreword, Modal verbs terminology, Introduction, clausola 2 References,
  Annex A Change history, History) NON e' modellato come nodo, stesso
  trattamento riservato al front matter di parte5.py. Nessun discrimine di
  rilevanza sulle clausole sostanziali: ogni requisito numerato genera un
  nodo distinto anche quando il contenuto e' minimo o meramente strutturale
  (es. i chapeau condizionali GEN-4.2.3.1-1/GEN-4.2.3.2-1, che introducono i
  requisiti applicabili quando l'emittente e' rispettivamente persona
  giuridica/fisica: modellati come Obbligo con condizione_applicabilita
  perche' la forma testuale e' "if X the following requirements shall
  apply:", coerente con la convenzione dei requisiti condizionali).
- Requisiti "shall"/"shall not"/"should"/"should not" con soggetto obbligato
  implicito (il QTSP che emette il certificato) -> Obbligo, categoria_soggetto
  "QTSP/gestore", ruolo "obbligato", tipo_obbligo "tecnico/sicurezza" (sono
  tutti requisiti di profilo tecnico del certificato, stessa convenzione di
  parte5.py). Requisiti espliciti "if...then"/"(CONDITIONAL)" -> Obbligo con
  condizione_applicabilita valorizzato, mai escluso e mai declassato a
  Principio.
- Clausole/requisiti puramente permissivi ("may", nessun "shall" nello stesso
  identificatore) -> Principio "altro" (facoltativo/di supporto): es.
  GEN-4.2.3.1-4, NAT-4.2.4-5/-6/-7/-14/-16/-17/-18/-20. La Tabella 1 (key
  usage settings, clausola 4.3.2) e' di supporto descrittivo a NAT-4.3.2-1
  (che la referenzia con "as defined in table 1") -> Principio "altro" con
  nodo proprio, per evitare di duplicare l'intera tabella dentro
  NAT-4.3.2-1.
- Clausole puramente descrittive che spiegano la semantica di un attributo
  senza imporre un comportamento -> Principio "definitorio": NAT-4.2.4-8
  (semantica di countryName nel subject) e NAT-4.2.4-9 (semantica di
  serialNumber).
- Clausola 1 (Scope) -> Principio "scopo/ambito di applicazione".
- Clausola 3 (Definition of terms, symbols, abbreviations and notations) ->
  un solo nodo Principio "definitorio" aggregato: 3.1 Terms e 3.4 Notations
  rinviano interamente a ETSI EN 319 412-1 (Parte 1, non ancora censita come
  modulo separato in questo import), 3.2 Symbols e' "Void", 3.3
  Abbreviations elenca le sigle usate nel documento - nessun contenuto
  sostanziale autonomo che giustifichi la suddivisione in piu' nodi, stesso
  trattamento di parte5.py.
- NOTE informative del testo ufficiale: quelle generiche/ripetute (es. i
  richiami alle dimensioni storiche degli attributi ITU-T X.520, le NOTE
  sulle raccomandazioni crittografiche di ETSI TS 119 312 superabili da
  raccomandazioni nazionali, "some natural persons do not have both a given
  name and a surname") non generano contenuto normativo proprio e non sono
  riportate; le NOTE che aggiungono un dettaglio normativo/tecnico
  specificamente legato a un unico requisito numerato (es. la NOTE su
  registrazione in audit log di NAT-4.2.4-12A, la "security note" cui
  rimanda esplicitamente NAT-4.3.2-3, la NOTE su eIDAS Annex I(i) di
  GEN-4.3.11-2A/GEN-4.4.1-8A) sono riportate per intero in coda al
  testo_integrale del requisito che le richiama, per non perdere contenuto
  tecnico sostanziale senza introdurre un identificatore che il testo
  ufficiale non assegna.
- Nella tabella 1 e nella "security note" di NAT-4.3.2-3 il glifo elenco
  puntato di uso privato dell'estrazione PDF originale (Wingdings) e'
  normalizzato al bullet "•" gia' usato ovunque altrove nel documento
  per liste identiche (es. gli attributi X.520 di GEN-4.2.3.1-2/GEN-4.2.3.2-2/
  NAT-4.2.4-1): normalizzazione tipografica, non elisione di contenuto.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "Parte 2: GEN-4.1-1",
        "testo": "Tutti i campi e le estensioni del certificato devono rispettare IETF RFC 5280, con gli emendamenti specificati nel presente documento.",
        "testo_integrale": "GEN-4.1-1: All certificate fields and extensions shall comply with IETF RFC 5280 [1] with the amendments specified in the present document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.1-2",
        "testo": "Le estensioni del certificato non devono essere marcate come critiche, salvo che la criticita' sia esplicitamente consentita o richiesta dal presente documento o da IETF RFC 5280.",
        "testo_integrale": "GEN-4.1-2: Certificate extensions shall not be marked critical unless criticality is explicitly allowed or required in the present document or in IETF RFC 5280 [1].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.2.1-1",
        "testo": "La versione del certificato deve essere V3 (definita dal valore intero 2).",
        "testo_integrale": "GEN-4.2.1-1: The version shall be V3 (defined by the integer value 2).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.2.2-1",
        "testo": "L'algoritmo di firma dovrebbe essere selezionato secondo ETSI TS 119 312.",
        "testo_integrale": "GEN-4.2.2-1: Signature algorithm should be selected according to ETSI TS 119 312 [i.7].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.1-1",
        "testo": "Se l'emittente e' una persona giuridica, si applicano i requisiti specifici di questa sottoclausola (GEN-4.2.3.1-2..9).",
        "testo_integrale": "GEN-4.2.3.1-1: If the issuer is a legal person the following requirements shall apply:",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'emittente del certificato e' una persona giuridica",
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.1-2",
        "testo": "L'identita' dell'emittente deve contenere almeno gli attributi countryName, organizationName e commonName, come specificato nella Raccomandazione ITU-T X.520.",
        "testo_integrale": "GEN-4.2.3.1-2: The identity of the issuer, shall contain at least the following attributes as specified in Recommendation ITU-T X.520 [6]: • countryName; • organizationName; and • commonName.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.1-3",
        "testo": "Se e' noto un numero di registrazione appropriato, l'identita' dell'emittente deve contenere l'attributo organizationIdentifier con valore diverso dal nome dell'organizzazione (es. un numero di registrazione elencato in una trusted list ETSI TS 119 612).",
        "testo_integrale": "GEN-4.2.3.1-3: If an appropriate registration number is known to exist, then the identity of the issuer shall contain organizationIdentifier and with value different from the organization name. EXAMPLE: An appropriate registration number can be listed in a ETSI TS 119 612 [i.9] trusted list.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se e' noto un numero di registrazione appropriato per l'emittente",
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.1-5",
        "testo": "Ogni attributo deve essere limitato a una singola istanza; attributi aggiuntivi possono essere presenti.",
        "testo_integrale": "GEN-4.2.3.1-5: Each attribute shall be limited to a single instance of the attribute. Additional attributes may be present.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.1-6",
        "testo": "L'attributo countryName deve specificare il paese in cui l'emittente del certificato e' stabilito.",
        "testo_integrale": "GEN-4.2.3.1-6: The countryName attribute shall specify the country in which the issuer of the certificate is established.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.1-7",
        "testo": "L'attributo organizationName deve contenere il nome registrato completo dell'organizzazione emittente il certificato.",
        "testo_integrale": "GEN-4.2.3.1-7: The organizationName attribute shall contain the full registered name of the certificate issuing organization.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.1-8",
        "testo": "L'attributo organizationIdentifier deve contenere un'identificazione dell'organizzazione emittente il certificato diversa dal nome dell'organizzazione.",
        "testo_integrale": "GEN-4.2.3.1-8: The organizationIdentifier attribute shall contain an identification of the certificate issuing organization different from the organization name.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.1-9",
        "testo": "Il valore dell'attributo commonName deve contenere un nome comunemente usato dal soggetto per rappresentare se stesso; tale nome non deve necessariamente coincidere esattamente con il nome registrato completo dell'organizzazione.",
        "testo_integrale": "GEN-4.2.3.1-9: The commonName attribute value shall contain a name commonly used by the subject to represent itself. This name need not be an exact match of the fully registered organization name.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.2-1",
        "testo": "Se l'emittente e' una persona fisica, si applicano i requisiti specifici di questa sottoclausola (GEN-4.2.3.2-2..7).",
        "testo_integrale": "GEN-4.2.3.2-1: If the issuer is a natural person the following requirements shall apply:",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'emittente del certificato e' una persona fisica",
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.2-2",
        "testo": "L'identita' dell'emittente deve contenere almeno gli attributi countryName, la scelta fra (givenName e/o surname) oppure pseudonym, serialNumber e commonName, come specificato nella Raccomandazione ITU-T X.520.",
        "testo_integrale": "GEN-4.2.3.2-2: The identity of the issuer shall contain at least the following attributes as specified in Recommendation ITU-T X.520 [6]: • countryName; • choice of (givenName and/or surname) or pseudonym; • serialNumber; and • commonName.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.2-3",
        "testo": "Ogni attributo deve essere limitato a una singola istanza; attributi aggiuntivi possono essere presenti.",
        "testo_integrale": "GEN-4.2.3.2-3: Each attribute shall be limited to a single instance of the attribute. Additional attributes may be present.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.2-4",
        "testo": "L'attributo countryName deve specificare un paese coerente con la giurisdizione legale in base alla quale i certificati sono emessi.",
        "testo_integrale": "GEN-4.2.3.2-4: The countryName attribute shall specify a country that is consistent with the legal jurisdiction under which certificates are issued.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.2-5",
        "testo": "Nel caso dell'alternativa (givenName e/o surname), se il nome proprio dell'emittente e' noto, l'attributo givenName deve essere presente.",
        "testo_integrale": "GEN-4.2.3.2-5: In case of the (givenName and/or surname) alternative, if the given name of the issuer is known, then the givenName attribute shall be present.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il nome proprio (given name) dell'emittente persona fisica e' noto",
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.2-6",
        "testo": "Nel caso dell'alternativa (givenName e/o surname), se il cognome dell'emittente e' noto, l'attributo surname deve essere presente. Non tutte le persone fisiche hanno sia nome che cognome; il Regolamento (UE) 910/2014 non consente l'uso dello pseudonimo per gli emittenti persona fisica.",
        "testo_integrale": "GEN-4.2.3.2-6: In case of the (givenName and/or surname) alternative, if the surname of the issuer is known, then the surname attribute shall be present. NOTE 1: Some natural persons do not have both a given name and a surname. NOTE 2: Regulation (EU) No 910/2014 [i.5] does not allow the usage of pseudonym for natural person issuers.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il cognome (surname) dell'emittente persona fisica e' noto",
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.2-7",
        "testo": "Gli altri attributi sopra elencati devono rispettare i requisiti stabiliti nella clausola 4.2.4.",
        "testo_integrale": "GEN-4.2.3.2-7: Other attributes listed above shall comply with requirements stated in clause 4.2.4.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-1",
        "testo": "Il campo subject deve includere gli attributi countryName, la scelta fra (givenName e/o surname) oppure pseudonym, e commonName, come specificato nella Raccomandazione ITU-T X.520.",
        "testo_integrale": "NAT-4.2.4-1: The subject field shall include the following attributes as specified in Recommendation ITU-T X.520 [6]: • countryName; • choice of (givenName and/or surname) or pseudonym; and • commonName.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-2",
        "testo": "Se questi attributi obbligatori non sono sufficienti a garantire l'unicita' del nome del soggetto nel contesto dell'emittente, l'attributo serialNumber deve essere presente.",
        "testo_integrale": "NAT-4.2.4-2: If these mandatory attributes are not sufficient to ensure Subject name uniqueness within the context of the issuer then the serialNumber shall be present.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se gli attributi obbligatori non sono sufficienti a garantire l'unicita' del nome del soggetto nel contesto dell'emittente",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-3",
        "testo": "Il campo subject non deve contenere piu' di un'istanza di commonName e countryName.",
        "testo_integrale": "NAT-4.2.4-3: The subject field shall not contain more than one instance of commonName and countryName.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-4",
        "testo": "L'attributo pseudonym non deve essere presente se sono presenti gli attributi givenName e/o surname.",
        "testo_integrale": "NAT-4.2.4-4: The pseudonym attribute shall not be present if the givenName and/or surname attribute are present.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se sono presenti gli attributi givenName e/o surname del soggetto",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-10",
        "testo": "Nel caso dell'alternativa (givenName e/o surname), se il nome proprio del soggetto e' noto, l'attributo givenName deve essere presente.",
        "testo_integrale": "NAT-4.2.4-10: In case of the (givenName and/or surname) alternative, if the given name of the subject is known, then the givenName attribute shall be present.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il nome proprio (given name) del soggetto e' noto",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-11",
        "testo": "Nel caso dell'alternativa (givenName e/o surname), se il cognome del soggetto e' noto, l'attributo surname deve essere presente.",
        "testo_integrale": "NAT-4.2.4-11: In case of the (givenName and/or surname) alternative, if the surname of the subject is known, then the surname attribute shall be present.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il cognome (surname) del soggetto e' noto",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-12",
        "testo": "givenName e surname devono contenere la rappresentazione formale dell'identita' dell'utente, come indicata su un documento di identita' ufficiale dell'utente.",
        "testo_integrale": "NAT-4.2.4-12: The givenName with surname shall contain formal representation of the user's identity, such as indicated on a user's official identity document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-12A",
        "testo": "Se la rappresentazione formale di givenName e/o surname richiede una traslitterazione, tale traslitterazione deve seguire l'edizione in vigore dell'ICAO Doc 9303 Parte 3, sezione 6.A (traslitterazione di caratteri multinazionali basati sul latino). Il fatto e il motivo della traslitterazione vanno registrati come parte delle informazioni di registrazione e ciclo di vita nel log di audit, in conformita' a ETSI EN 319 411-1, clausola 6.4.5.",
        "testo_integrale": "NAT-4.2.4-12A: (CONDITIONAL) If the givenName and/or surname formal representation needs transliteration then that transliteration shall follow the actual edition of ICAO Doc 9303 Part 3 [7] Section 6. A. Transliteration of Multinational Latin-Based Characters. NOTE 2: The fact and reason for the transliteration are to be recorded as part of the registration and lifecycle information in the audit log in accordance with ETSI EN 319 411-1 [i.10], clause 6.4.5.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se la rappresentazione formale di givenName e/o surname richiede una traslitterazione",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-13",
        "testo": "La CA deve garantire che il serialNumber sia sufficiente a risolvere eventuali collisioni fra nomi soggetto.",
        "testo_integrale": "NAT-4.2.4-13: The CA shall ensure that the serialNumber is sufficient to resolve any subject name collisions.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-15",
        "testo": "Il valore dell'attributo commonName deve contenere un nome del soggetto.",
        "testo_integrale": "NAT-4.2.4-15: The commonName attribute value shall contain a name of the subject.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-19",
        "testo": "La CA non dovrebbe usare una codifica linguistica diversa tra i campi del subject DN \"givenName\", \"surname\" e \"commonName\" (es. \"C=GR, givenName=Δημήτριος, surname=Ζαχαρόπουλος, commonName=Dimitrios Zacharopoulos\" non e' consentito).",
        "testo_integrale": "NAT-4.2.4-19: The CA should not use different language encoding between subject DN fields \"givenName\", \"surname\" and \"commonName\". EXAMPLE: \"C=GR, givenName=Δημήτριος, surname=Ζαχαρόπουλος, commonName=Dimitrios Zacharopoulos\" is not allowed.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.2.5-1",
        "testo": "La chiave pubblica del soggetto dovrebbe essere selezionata secondo ETSI TS 119 312.",
        "testo_integrale": "GEN-4.2.5-1: The subject public key should be selected according to ETSI TS 119 312 [i.7].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.3.1-1",
        "testo": "L'estensione authority key identifier deve essere presente, contenente un identificatore della chiave pubblica della CA emittente.",
        "testo_integrale": "GEN-4.3.1-1: The authority key identifier extension shall be present, containing a key identifier for the issuing CA's public key.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: NAT-4.3.2-1",
        "testo": "L'estensione key usage deve essere presente e deve contenere una (e una sola) delle impostazioni definite nella tabella 1 (A, B, C, D, E o F); dovrebbero essere usati i tipi A, C o E per evitare un uso misto delle chiavi.",
        "testo_integrale": "NAT-4.3.2-1: The key usage extension shall be present and shall contain one (and only one) of the key usage settings defined in table 1 (A, B, C, D, E or F). Type A, C or E should be used to avoid mixed usage of keys.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: NAT-4.3.2-2",
        "testo": "I certificati usati per validare l'impegno (commitment) al contenuto firmato (es. documenti, accordi e/o transazioni) devono essere limitati al tipo A, B o F; le firme digitali destinate a essere usate come firme elettroniche avanzate ai sensi del Regolamento (UE) 910/2014 sono considerate segnalare l'impegno al contenuto firmato.",
        "testo_integrale": "NAT-4.3.2-2: Certificates used to validate commitment to signed content (e.g. documents, agreements and/or transactions) shall be limited to type A, B or F. EXAMPLE: Digital signatures which are aimed to be used as advanced electronic signatures as defined in Regulation (EU) No 910/2014 [i.5] are considered to signal commitment to signed content.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: NAT-4.3.2-3",
        "testo": "Tra queste alternative, dovrebbe essere usato il tipo A (vedi la nota di sicurezza 2). Lo standard X.509 ha rinominato il bit nonRepudiation in \"contentCommitment\"; IETF RFC 5280 ha mantenuto il nome originale nonRepudiation per compatibilita' con versioni precedenti: i bit sono equivalenti per funzione e significato indipendentemente dal nome. Nota di sicurezza: combinare il bit non-repudiation (bit 1) nell'estensione keyUsage con altri bit keyUsage puo' avere implicazioni di sicurezza a seconda dell'ambiente in cui il certificato e' usato. Se l'ambiente del soggetto e' pienamente controllato e affidabile, non vi sono implicazioni di sicurezza specifiche (es. il soggetto e' pienamente consapevole di quali dati firma o delle caratteristiche di sicurezza del protocollo di autenticazione usato). Se l'ambiente del soggetto non e' pienamente controllato o affidabile, e' possibile una firma non intenzionale di impegni (es. scambi di autenticazione malformati o componenti software malevoli). Se il soggetto usa ambienti non affidabili, tali implicazioni di sicurezza possono essere limitate: non combinando l'impostazione non-repudiation con altre impostazioni di key usage nello stesso certificato e usando la chiave privata corrispondente solo con quel certificato; limitando l'uso delle chiavi private associate a certificati con il bit non-repudiation impostato ad ambienti considerati adeguatamente controllati e affidabili.",
        "testo_integrale": "NAT-4.3.2-3: Of these alternatives, type A should be used (see the security note 2 below). NOTE 1: The X.509 standard [i.3] has renamed the nonRepudiation bit to \"contentCommitment\". IETF RFC 5280 [1] has kept the original name nonRepudiation for backwards compatibility reasons. These bits are equivalent in function and meaning regardless of their different names. NOTE 2: [security note] Combining the non-repudiation bit (bit 1) in the keyUsage certificate extension with other keyUsage bits can have security implications depending on the security environment in which the certificate is to be used. If the subject's environment can be fully controlled and trusted, then there are no specific security implications. For example, in cases where the subject is fully confident about exactly which data is signed or cases where the subject is fully confident about the security characteristics of the authentication protocol being used. If the subject's environment is not fully controlled or not fully trusted, then unintentional signing of commitments is possible. Examples include the use of badly formed authentication exchanges and the use of a rogue software component. If untrusted environments are used by a subject, these security implications can be limited through use of the following measures: • to not combine non-repudiation key usage setting in certificates with any other key usage setting and to use the corresponding private key only with this certificate; • to limit the use of private keys associated with certificates that have the non-repudiation key usage bit set, to environments which are considered adequately controlled and trustworthy.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.3.3-1",
        "testo": "L'estensione certificate policies non dovrebbe essere marcata come critica.",
        "testo_integrale": "GEN-4.3.3-1: This extension should not be marked critical.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.3.3-2",
        "testo": "L'estensione certificate policies deve essere presente e deve contenere l'identificatore di almeno una certificate policy che rifletta le pratiche e le procedure adottate dalla CA.",
        "testo_integrale": "GEN-4.3.3-2: The certificate policies extension shall be present and shall contain the identifier of at least one certificate policy which reflects the practices and procedures undertaken by the CA.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.3.4-1",
        "testo": "L'estensione policy mappings non deve essere presente: non e' applicabile ai certificati di entita' finale disciplinati dal presente documento.",
        "testo_integrale": "GEN-4.3.4-1: This extension shall not be present. This extension is not applicable to end entity certificates addressed by the present document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.3.5-1",
        "testo": "L'estensione subject alternative name non deve essere marcata come critica.",
        "testo_integrale": "GEN-4.3.5-1: This extension shall not be marked critical.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.3.6-1",
        "testo": "L'estensione issuer alternative name non deve essere marcata come critica.",
        "testo_integrale": "GEN-4.3.6-1: This extension shall not be marked critical.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.3.7-1",
        "testo": "L'estensione subject directory attributes, se presente, non deve essere usata per memorizzare alcuno degli attributi di identificazione elencati nella clausola 4.2.5.",
        "testo_integrale": "GEN-4.3.7-1: The subject directory attributes extension, if present, shall not be used to store any of the identification attribute listed in clause 4.2.5.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'estensione subject directory attributes e' presente nel certificato",
    },
    {
        "riferimento": "Parte 2: GEN-4.3.8-1",
        "testo": "L'estensione name constraints non deve essere presente: non e' applicabile ai certificati di entita' finale disciplinati dal presente documento.",
        "testo_integrale": "GEN-4.3.8-1: This extension shall not be present. This extension is not applicable to end entity certificates addressed by the present document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.3.9-1",
        "testo": "L'estensione policy constraints non deve essere presente: non e' applicabile ai certificati di entita' finale disciplinati dal presente documento.",
        "testo_integrale": "GEN-4.3.9-1: This extension shall not be present. This extension is not applicable to end entity certificates addressed by the present document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.3.10-1",
        "testo": "L'estensione extended key usage non deve essere marcata come critica.",
        "testo_integrale": "GEN-4.3.10-1: This extension shall not be marked critical.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.3.11-1",
        "testo": "Se la CRL e' supportata dalla CA emittente, l'estensione CRL distribution point deve essere presente nei certificati.",
        "testo_integrale": "GEN-4.3.11-1: If CRL is supported by the issuing CA, the CRL distribution point extension shall be present in certificates.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se la CRL e' supportata dalla CA emittente",
    },
    {
        "riferimento": "Parte 2: GEN-4.3.11-1A",
        "testo": "Per i certificati di risponditore OCSP, i requisiti della presente clausola (CRL distribution points) non si applicano.",
        "testo_integrale": "GEN-4.3.11-1A: For OCSP responder certificates the requirements in the present clause shall not apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica ai certificati diversi dai certificati di risponditore OCSP; per i certificati di risponditore OCSP i requisiti della clausola non si applicano",
    },
    {
        "riferimento": "Parte 2: GEN-4.3.11-2",
        "testo": "Se il certificato non include alcuna access location di un risponditore OCSP (clausola 4.4.1) e non include l'estensione validity assured (ETSI EN 319 412-1), il certificato deve includere un'estensione CRL distribution point.",
        "testo_integrale": "GEN-4.3.11-2: If the certificate does not include any access location of an OCSP responder as specified in clause 4.4.1, and the certificate does not include the validity assured extension as defined in ETSI EN 319 412-1 [i.4], then the certificate shall include a CRL distribution point extension.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il certificato non include ne' un'access location di risponditore OCSP ne' l'estensione validity assured",
    },
    {
        "riferimento": "Parte 2: GEN-4.3.11-2A",
        "testo": "Se un certificato include l'estensione validity assured ma non include ne' un CRL distribution point ne' un'access location di risponditore OCSP (clausola 4.4.1), il certificato deve avere l'estensione No Revocation Available secondo IETF RFC 9608. Un certificato validity assured non necessita di CRL distribution point o di access location OCSP, ma e' consentito per ragioni di compatibilita' includerli (poiche' molto software attuale necessita di informazioni di revoca): se nessuno dei due e' incluso, l'estensione No Revocation Available e' obbligatoria per soddisfare l'Allegato I(i) di eIDAS.",
        "testo_integrale": "GEN-4.3.11-2A: If a certificate includes the validity assured extension, but neither include a CRL distribution point nor access location of an OCSP responder (as specified in clause 4.4.1) is included, then the certificate shall have No Revocation Available extensions as specified in IETF RFC 9608 [8]. NOTE: A validity assured certificate does not need to have CRL distribution point extension or access location of an OCSP responder (as specified in clause 4.4.1) included in the certificate, but it is allowed for compatibility reasons to have those. (Because most of the software available at the moment needs revocation info.) If none of them included, then the No Revocation Available extension is mandatory to fulfil the eIDAS [i.5], Annex I (i).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il certificato include l'estensione validity assured e non include ne' CRL distribution point ne' access location di risponditore OCSP",
    },
    {
        "riferimento": "Parte 2: GEN-4.3.11-3",
        "testo": "Quando presente, l'estensione CRL distribution point deve includere almeno un riferimento a una CRL pubblicamente disponibile.",
        "testo_integrale": "GEN-4.3.11-3: When present, the CRL distribution point extension shall include at least one reference to a publicly available CRL.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'estensione CRL distribution point e' presente nel certificato",
    },
    {
        "riferimento": "Parte 2: GEN-4.3.11-4",
        "testo": "Almeno uno dei riferimenti presenti deve usare lo schema http (IETF RFC 9110) o ldap (IETF RFC 4516).",
        "testo_integrale": "GEN-4.3.11-4: At least one of the present references shall use either http (http://) IETF RFC 9110 [3] or ldap (ldap://) IETF RFC 4516 [4] scheme.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.3.11-5",
        "testo": "L'estensione CRL distribution point non deve essere marcata come critica.",
        "testo_integrale": "GEN-4.3.11-5: The extension shall not be marked critical.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.3.12-1",
        "testo": "L'estensione inhibit any-policy non deve essere presente: non e' applicabile ai certificati di entita' finale disciplinati dal presente documento.",
        "testo_integrale": "GEN-4.3.12-1: This extension shall not be present. This extension is not applicable to end entity certificates addressed by the present document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.4.1-1",
        "testo": "Per i certificati di risponditore OCSP, i requisiti della presente clausola (Authority Information Access) non si applicano.",
        "testo_integrale": "GEN-4.4.1-1: For OCSP responder certificates the requirements in the present clause shall not apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica ai certificati diversi dai certificati di risponditore OCSP; per i certificati di risponditore OCSP i requisiti della clausola non si applicano",
    },
    {
        "riferimento": "Parte 2: GEN-4.4.1-2",
        "testo": "L'estensione Authority Information Access deve essere presente.",
        "testo_integrale": "GEN-4.4.1-2: The Authority Information Access extension shall be present.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.4.1-3",
        "testo": "L'estensione Authority Information Access deve includere un accessMethod OID id-ad-caIssuers, con un valore accessLocation che specifichi almeno una access location di un certificato CA valido della CA emittente.",
        "testo_integrale": "GEN-4.4.1-3: The Authority Information Access extension shall include an accessMethod OID, id-ad-caIssuers, with an accessLocation value specifying at least one access location of a valid CA certificate of the issuing CA.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.4.1-4",
        "testo": "Almeno una accessLocation deve usare lo schema http o https (IETF RFC 9110).",
        "testo_integrale": "GEN-4.4.1-4: At least one accessLocation shall use the http (http://) or https (https://) IETF RFC 9110 [3] scheme.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: GEN-4.4.1-5",
        "testo": "Se OCSP e' supportato dalla CA emittente, l'estensione Authority Information Access deve includere un accessMethod OID id-ad-ocsp, con un valore accessLocation che specifichi almeno una access location di un risponditore OCSP autorevole a fornire informazioni sullo stato del presente certificato.",
        "testo_integrale": "GEN-4.4.1-5: If OCSP is supported by the issuing CA, the Authority Information Access extension shall include an accessMethod OID, id-ad-ocsp, with an accessLocation value specifying at least one access location of an OCSP [i.2] responder authoritative to provide certificate status information for the present certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se OCSP e' supportato dalla CA emittente",
    },
    {
        "riferimento": "Parte 2: GEN-4.4.1-6",
        "testo": "Se OCSP e' supportato dalla CA emittente, almeno una access location deve specificare lo schema http o https (IETF RFC 9110).",
        "testo_integrale": "GEN-4.4.1-6: If OCSP is supported by the issuing CA, at least one access location shall specify either the http (http://) or https (https://) IETF RFC 9110 [3] scheme.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se OCSP e' supportato dalla CA emittente",
    },
    {
        "riferimento": "Parte 2: GEN-4.4.1-7",
        "testo": "Se OCSP e' supportato dalla CA emittente, la access location deve fare riferimento a un risponditore OCSP pubblicamente disponibile, che accetti richieste di stato non firmate e non autenticate.",
        "testo_integrale": "GEN-4.4.1-7: If OCSP is supported by the issuing CA, the access location shall reference a publicly available OCSP responder, which accepts unsigned and unauthenticated status requests.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se OCSP e' supportato dalla CA emittente",
    },
    {
        "riferimento": "Parte 2: GEN-4.4.1-8",
        "testo": "Se il certificato non include alcuna estensione CRL distribution point (clausola 4.3.11) e non include l'estensione validity assured (ETSI EN 319 412-1), deve essere presente un riferimento ad almeno un risponditore OCSP.",
        "testo_integrale": "GEN-4.4.1-8: If the certificate does not include any CRL distribution point extension in accordance with clause 4.3.11, and the certificate does not include the validity assured extension as defined in ETSI EN 319 412-1 [i.4], a reference to at least one OCSP responder shall be present.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il certificato non include ne' un'estensione CRL distribution point ne' l'estensione validity assured",
    },
    {
        "riferimento": "Parte 2: GEN-4.4.1-8A",
        "testo": "Se un certificato include l'estensione validity assured ma non include ne' un CRL distribution point ne' un'access location di risponditore OCSP (clausola 4.4.1), il certificato deve avere l'estensione No Revocation Available secondo IETF RFC 9608. Un certificato validity assured non necessita di CRL distribution point o di access location OCSP, ma e' consentito per ragioni di compatibilita' includerli: se nessuno dei due e' incluso, l'estensione No Revocation Available e' obbligatoria per soddisfare l'Allegato I(i) di eIDAS.",
        "testo_integrale": "GEN-4.4.1-8A: If a certificate includes the validity assured extension, but neither include a CRL distribution point nor access location of an OCSP responder (as specified in clause 4.4.1) is included, then the certificate shall have No Revocation Available extensions as specified in IETF RFC 9608 [8]. NOTE: A validity assured certificate does not need to have CRL distribution point extension or access location of an OCSP responder (as specified in clause 4.4.1) included in the certificate, but it is allowed for compatibility reasons to have those. (Because most of the software available at the moment needs revocation info.) If none of them included, then the No Revocation Available extension is mandatory to fulfil the eIDAS [i.5], Annex I (i).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il certificato include l'estensione validity assured e non include ne' CRL distribution point ne' access location di risponditore OCSP",
    },
    {
        "riferimento": "Parte 2: QCS-5.1-1",
        "testo": "Se i certificati sono emessi come certificati qualificati UE, devono includere gli QCStatements in conformita' a ETSI EN 319 412-5.",
        "testo_integrale": "QCS-5.1-1: If certificates are issued as EU Qualified Certificates, they shall include QCStatements in accordance with ETSI EN 319 412-5 [2].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo ai certificati emessi come certificati qualificati UE",
    },
    {
        "riferimento": "Parte 2: QCS-5.2-1",
        "testo": "Quando i certificati sono emessi come certificati qualificati UE, dovrebbero includere, nell'estensione certificate policies, uno degli identificatori di certificate policy definiti nella clausola 5.3 di ETSI EN 319 411-2.",
        "testo_integrale": "QCS-5.2-1: When certificates are issued as EU Qualified Certificates, they should include, in the certificate policies extension, one of the certificate policy identifiers defined in clause 5.3 of ETSI EN 319 411-2 [i.6].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo ai certificati emessi come certificati qualificati UE",
    },
    {
        "riferimento": "Parte 2: QCS-5.2-2",
        "testo": "Gli identificatori di policy inclusi nell'estensione certificate policies dei certificati qualificati UE devono essere coerenti con gli QCStatements di cui alla clausola 5.1.",
        "testo_integrale": "QCS-5.2-2: Policy identifiers included in the certificate policies extension of EU Qualified Certificates shall be consistent with the QCStatements according to clause 5.1.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "Parte 2: clausola 1 (Scope)",
        "testo": "Il documento specifica i requisiti sul contenuto dei certificati emessi a persone fisiche, basandosi su IETF RFC 5280 per il profiling generico di ITU-T X.509/ISO 9594-8. Supporta i requisiti dei certificati qualificati UE del Regolamento 910/2014 oltre ad altre forme di certificato; l'ambito e' limitato a facilitare l'elaborazione e la visualizzazione interoperabile delle informazioni del certificato, escludendo opzioni di contenuto valide in contesti locali ma non rilevanti per applicazioni ampiamente diffuse. Il documento si concentra sui requisiti di contenuto del certificato; i requisiti su decodifica ed elaborazione sono limitati agli aspetti necessari a elaborare il contenuto definito nel documento. E' fuori ambito specificare requisiti di contenuto certificato specifici di applicazioni o protocolli, dati per adeguatamente definiti dalla rispettiva applicazione/protocollo.",
        "testo_integrale": "1 Scope: The present document specifies requirements on the content of certificates issued to natural persons. This profile builds on IETF RFC 5280 [1] for generic profiling of Recommendation ITU-T X.509 | ISO/IEC 9594-8 [i.3]. This profile supports the requirements of EU Qualified Certificates as specified in the Regulation (EU) No 910/2014 [i.5] as well as other forms of certificate. The scope of the present document is primary limited to facilitate interoperable processing and display of certificate information. This profile therefore excludes support for some certificate information content options, which can be perfectly valid in a local context but which are not regarded as relevant or suitable for use in widely deployed applications. The present document focuses on requirements on certificate content. Requirements on decoding and processing rules are limited to aspects required to process certificate content defined in the present document. Further processing requirements are only specified for cases where it adds information that is necessary for the sake of interoperability. Certain applications or protocols impose specific requirements on certificate content. The present document is based on the assumption that these requirements are adequately defined by the respective application or protocol. It is therefore outside the scope of the present document to specify such application or protocol specific certificate content.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 3 (Definition of terms, symbols, abbreviations and notations)",
        "testo": "Per i termini, il documento rinvia interamente a ETSI EN 319 412-1 (Parte 1). I simboli sono 'Void' (nessuno definito). Le abbreviazioni usate nel documento sono: CA (Certification Authority), CRL (Certificate Revocation List), DN (Distinguished Name), EC (European Commission), EU (European Union), ISO (International Standards Organization), ML-KEM (Module-Lattice-based Key-Encapsulation Mechanism), OCSP (Online Certificate Status Protocol), OID (Object IDentifier), RFC (Request For Comments), TSP (Trust Service Provider). Per le notazioni, il documento rinvia anch'esso a ETSI EN 319 412-1 (Parte 1).",
        "testo_integrale": "3.1 Terms: For the purposes of the present document, the terms given in ETSI EN 319 412-1 [i.4] apply. 3.2 Symbols: Void. 3.3 Abbreviations: For the purposes of the present document, the following abbreviations apply: CA Certification Authority CRL Certificate Revocation List DN Distinguished Name EC European Commission EU European Union ISO International Standards Organization ML-KEM Module-Lattice-based Key-Encapsulation Mechanism OCSP Online Certificate Status Protocol OID Object IDentifier RFC Request For Comments TSP Trust Service Provider. 3.4 Notations: For the purposes of the present document, the notations given in ETSI EN 319 412-1 [i.4] apply.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: GEN-4.2.3.1-4",
        "testo": "I certificati possono includere un identificatore semantico di persona giuridica come specificato nella clausola 5.1.4 di ETSI EN 319 412-1.",
        "testo_integrale": "GEN-4.2.3.1-4: Certificates may include a legal person semantic identifier as specified in clause 5.1.4 of ETSI EN 319 412-1 [i.4].",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-5",
        "testo": "Attributi ulteriori rispetto a quelli sopra elencati possono essere presenti nel campo subject.",
        "testo_integrale": "NAT-4.2.4-5: Additional attributes other than those listed above may be present.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-6",
        "testo": "Quando un soggetto persona fisica e' associato a un'organizzazione, gli attributi del subject possono anche identificare tale organizzazione tramite attributi come organizationName e organizationIdentifier.",
        "testo_integrale": "NAT-4.2.4-6: When a natural person subject is associated with an organization, the subject attributes may also identify such organization using attributes such as organizationName and organizationIdentifier.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-7",
        "testo": "I certificati possono includere uno o piu' identificatori semantici come specificato nella clausola 5 di ETSI EN 319 412-1, che definisce la semantica dell'attributo organizationIdentifier.",
        "testo_integrale": "NAT-4.2.4-7: Certificates may include one or more semantics identifiers as specified in ETSI EN 319 412-1 [i.4], clause 5 which defines the semantics for the organizationIdentifier attribute.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-8",
        "testo": "Il valore dell'attributo countryName specifica un contesto generale in cui vanno intesi gli altri attributi; il verificatore potrebbe dover consultare la certificate policy dell'emittente per determinare la semantica esatta di tale attributo.",
        "testo_integrale": "NAT-4.2.4-8: The countryName attribute value specifies a general context in which other attributes are to be understood. The verifier may have to consult the certificate policy of the issuer to determine the exact semantics of this attribute.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-9",
        "testo": "L'attributo serialNumber non ha semantica definita oltre a garantire l'unicita' dei nomi soggetto; puo' contenere un numero o codice assegnato dalla CA o un identificatore assegnato da un'autorita' governativa o civile.",
        "testo_integrale": "NAT-4.2.4-9: The serialNumber attribute has no defined semantics beyond ensuring uniqueness of subject names. It may contain a number or code assigned by the CA or an identifier assigned by a government or civil authority.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-14",
        "testo": "I certificati possono includere uno o piu' identificatori semantici come specificato nella clausola 5 di ETSI EN 319 412-1, che definisce la semantica dell'attributo serialNumber.",
        "testo_integrale": "NAT-4.2.4-14: Certificates may include one or more semantics identifiers as specified in ETSI EN 319 412-1 [i.4], clause 5 which define the semantics for the serialNumber attribute.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-16",
        "testo": "Il valore dell'attributo commonName puo' essere nel formato di presentazione preferito dal soggetto, in un formato preferito dalla CA, o in un altro formato.",
        "testo_integrale": "NAT-4.2.4-16: The commonName attribute value may be in the subject's preferred presentation format, or a format preferred by the CA, or some other format.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-17",
        "testo": "Pseudonimi, soprannomi e nomi con grafia diversa da quella del nome registrato possono essere usati nel valore dell'attributo commonName; commonName ha uno scopo d'uso diverso dalla scelta obbligatoria fra pseudonym o givenName/surname: serve per una rappresentazione user-friendly del nome della persona, mentre givenName/surname serve dove e' richiesta una rappresentazione o verifica piu' formale dell'identita' specifica dell'utente. Per massimizzare l'interoperabilita' entrambi sono considerati necessari.",
        "testo_integrale": "NAT-4.2.4-17: Pseudonyms, nicknames, and names with spelling other than defined by the registered name may be used in the commonName attribute value. NOTE 3: The commonName attribute has a usage purpose that is different from the required choice of pseudonym or givenName/surname. commonName is used for user friendly representation of the person's name, whereas givenName/surname is used where more formal representation or verification of specific identity of the user is required. To maximize interoperability both are considered necessary.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-18",
        "testo": "Se presenti, la dimensione di givenName, surname, pseudonym, commonName, organizationName e organizationalUnitName puo' essere superiore al limite indicato in IETF RFC 5280.",
        "testo_integrale": "NAT-4.2.4-18: If present, the size of givenName, surname, pseudonym, commonName, organizationName and organizationalUnitName may be longer than the limit as stated in IETF RFC 5280 [1].",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: NAT-4.2.4-20",
        "testo": "Se la CA desidera includere il nome del soggetto nel certificato con una codifica aggiuntiva (nazionale o latina), puo' usare l'estensione Subject Alternative Name a tale scopo, aggiungendo i valori con il tipo directoryName.",
        "testo_integrale": "NAT-4.2.4-20: If the CA wants to include the Subject's name in the certificate with an additional encoding national or latin, it may use the Subject Alternative Name extension for this purpose and add the values using the directoryName value type.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: Tabella 1 (key usage settings)",
        "testo": "Tabella di supporto a NAT-4.3.2-1 che definisce sei combinazioni ammesse (Type A-F) dei bit non-repudiation, digital signature e key encipherment/key agreement dell'estensione key usage. I bit key agreement e key encipherment sono tipicamente mutuamente esclusivi o correlati tra loro; il loro uso e' determinato dall'algoritmo della coppia di chiavi e corrisponde alle operazioni eseguibili con la chiave: key encipherment secondo IETF RFC 3279 §2.3.1 per RSA, key agreement secondo IETF RFC 5480 §3 per curve ellittiche, key encipherment secondo IETF RFC 9935 §5 per ML-KEM.",
        "testo_integrale": "Table 1: Key usage settings. Type A: Non-Repudiation (Bit 1) X. Type B: Non-Repudiation (Bit 1) X; Digital Signature (Bit 0) X. Type C: Digital Signature (Bit 0) X. Type D: Digital Signature (Bit 0) X; Key Encipherment or Key Agreement (Bit 2 or 4) X. Type E: Key Encipherment or Key Agreement (Bit 2 or 4) X. Type F: Non-Repudiation (Bit 1) X; Digital Signature (Bit 0) X; Key Encipherment or Key Agreement (Bit 2 or 4) X. NOTE 0: The Key Agreement and Key Encipherment bits are typically mutually exclusive or related to each other, their use is determined by the key pair algorithm and corresponds to the operations that can be performed with the key. In end-user certificates, Key Encipherment is interpreted and used in accordance with section 2.3.1 of IETF RFC 3279 [i.11] for the RSA algorithm, Key Agreement is interpreted and used in accordance with section 3 of IETF RFC 5480 [i.12] for the elliptic curve algorithm, and Key Encipherment is interpreted and used in accordance with section 5 of IETF RFC 9935 [i.13] for the ML-KEM.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Parte 2: GEN-4.1-1", "Parte 2: GEN-4.1-2", "Parte 2: GEN-4.2.1-1", "Parte 2: GEN-4.2.2-1",
    "Parte 2: GEN-4.2.3.1-1", "Parte 2: GEN-4.2.3.1-2", "Parte 2: GEN-4.2.3.1-3",
    "Parte 2: GEN-4.2.3.1-4", "Parte 2: GEN-4.2.3.1-5", "Parte 2: GEN-4.2.3.1-6",
    "Parte 2: GEN-4.2.3.1-7", "Parte 2: GEN-4.2.3.1-8", "Parte 2: GEN-4.2.3.1-9",
    "Parte 2: GEN-4.2.3.2-1", "Parte 2: GEN-4.2.3.2-2", "Parte 2: GEN-4.2.3.2-3",
    "Parte 2: GEN-4.2.3.2-4", "Parte 2: GEN-4.2.3.2-5", "Parte 2: GEN-4.2.3.2-6",
    "Parte 2: GEN-4.2.3.2-7",
    "Parte 2: NAT-4.2.4-1", "Parte 2: NAT-4.2.4-2", "Parte 2: NAT-4.2.4-3", "Parte 2: NAT-4.2.4-4",
    "Parte 2: NAT-4.2.4-5", "Parte 2: NAT-4.2.4-6", "Parte 2: NAT-4.2.4-7", "Parte 2: NAT-4.2.4-8",
    "Parte 2: NAT-4.2.4-9", "Parte 2: NAT-4.2.4-10", "Parte 2: NAT-4.2.4-11", "Parte 2: NAT-4.2.4-12",
    "Parte 2: NAT-4.2.4-12A", "Parte 2: NAT-4.2.4-13", "Parte 2: NAT-4.2.4-14", "Parte 2: NAT-4.2.4-15",
    "Parte 2: NAT-4.2.4-16", "Parte 2: NAT-4.2.4-17", "Parte 2: NAT-4.2.4-18", "Parte 2: NAT-4.2.4-19",
    "Parte 2: NAT-4.2.4-20",
    "Parte 2: GEN-4.2.5-1",
    "Parte 2: GEN-4.3.1-1",
    "Parte 2: Tabella 1 (key usage settings)",
    "Parte 2: NAT-4.3.2-1", "Parte 2: NAT-4.3.2-2", "Parte 2: NAT-4.3.2-3",
    "Parte 2: GEN-4.3.3-1", "Parte 2: GEN-4.3.3-2",
    "Parte 2: GEN-4.3.4-1",
    "Parte 2: GEN-4.3.5-1",
    "Parte 2: GEN-4.3.6-1",
    "Parte 2: GEN-4.3.7-1",
    "Parte 2: GEN-4.3.8-1",
    "Parte 2: GEN-4.3.9-1",
    "Parte 2: GEN-4.3.10-1",
    "Parte 2: GEN-4.3.11-1", "Parte 2: GEN-4.3.11-1A", "Parte 2: GEN-4.3.11-2",
    "Parte 2: GEN-4.3.11-2A", "Parte 2: GEN-4.3.11-3", "Parte 2: GEN-4.3.11-4",
    "Parte 2: GEN-4.3.11-5",
    "Parte 2: GEN-4.3.12-1",
    "Parte 2: GEN-4.4.1-1", "Parte 2: GEN-4.4.1-2", "Parte 2: GEN-4.4.1-3", "Parte 2: GEN-4.4.1-4",
    "Parte 2: GEN-4.4.1-5", "Parte 2: GEN-4.4.1-6", "Parte 2: GEN-4.4.1-7", "Parte 2: GEN-4.4.1-8",
    "Parte 2: GEN-4.4.1-8A",
    "Parte 2: QCS-5.1-1", "Parte 2: QCS-5.2-1", "Parte 2: QCS-5.2-2",
    "Parte 2: clausola 1 (Scope)",
    "Parte 2: clausola 3 (Definition of terms, symbols, abbreviations and notations)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
