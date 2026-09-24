"""ETSI EN 319 421 V1.3.1 (2025-07) - Electronic Signatures and Trust
Infrastructures (ESI); Policy and Security Requirements for Trust Service
Providers issuing Time-Stamps. Fonte 18 (numerazione definitiva cablata
dalla sessione principale in app/seed.py - questo modulo NON tocca seed.py).
Capitolo 2: clausola 5 (Introduction to time-stamp policies and general
requirements: 5.1 General requirements, 5.2 Policy name and identification,
5.3 User community and applicability) e clausola 6 (Policies and practices:
6.1 Risk assessment, 6.2 Trust Service Practice Statement, 6.3 Terms and
conditions, 6.4 Information security policy, 6.5 TSA obligations, 6.6
Information for relying parties). Testo ufficiale in
app/.source_cache/etsi_319_421/cap02.txt. Manifest di split:
app/.source_cache/etsi_319_421/manifest.json.

Modellazione (ADR-0007), stesso criterio applicato alle altre fonti ETSI
gia' censite (in particolare ETSI EN 319 401, Fonte 10, e ETSI EN 319 411-1,
che usa lo stesso prefisso OVR-): un nodo per ogni requisito numerato, un
solo nodo Principio per le clausole di cornice prive di requisito numerato.

Copertura voce per voce (18 Obblighi, 1 Principio, 19 item di indice):

- Clausola 5 (heading "Introduction to time-stamp policies and general
  requirements") e clausola 6 (heading "Policies and practices"): heading
  strutturali senza alcun contenuto normativo proprio -> nessun nodo e
  nessun item di indice; la loro materia e' interamente nei requisiti
  numerati delle sottoclausole.
- 5.1 General requirements -> 3 Obblighi OVR-5.1-01/02/03. Il preambolo
  discorsivo non numerato ("The policy requirements are defined in the
  present document in terms of a time-stamp policy. The present document
  specifies one time-stamp policy: a Best practices Time-Stamp Policy
  (BTSP) for TSAs issuing time-stamps, supported by public key
  certificates, with an accuracy of 1 second or better.") e' incorporato
  nella riga del primo requisito della clausola (OVR-5.1-01), come parte
  integrante del perimetro del requisito, con separatore " — " tra titolo
  di clausola, preambolo e requirement id (precedente di stile:
  app/seed_data/etsi_119_461/cap04.py). Non genera un item di indice
  proprio: il manifest/indice di questo capitolo censisce i requirement id,
  non i preamboli.
- 5.2 Policy name and identification -> 3 Obblighi OVR-5.2-01, OVR-5.2-01A,
  OVR-5.2-02. Il preambolo non numerato (frase "The identifier of the
  time-stamp policy specified in the present document is:", lettera "a)
  BTSP: a best practices policy for time-stamp.", il blocco OID in code
  fence "itu-t(0) identified-organization(4) etsi(0) /
  time-stamp-policy(2023) / policy-identifiers(1) best-practices-ts-policy
  (1)" e la frase "By including this object identifier in a time-stamp, the
  TSA claims conformance to the identified time-stamp policy.") e'
  incorporato nella riga OVR-5.2-01: e' li' che il testo ufficiale lo
  attribuisce (il requisito parla dell'identificatore e della sua
  inclusione nella disclosure statement). Il blocco OID, che nel PDF e'
  reso come code fence su tre righe, e' riportato in `testo_integrale` come
  sequenza continua delle tre righe originali separate da spazio, senza
  aggiungere punteggiatura non presente nel testo ufficiale (nessuna
  elisione, nessuna omissione). OVR-5.2-01A conserva il suffisso letterale
  "A" nel riferimento (requisito aggiunto senza rinumerazione dei
  successivi, stessa convenzione di ETSI EN 319 411-1).
- 5.3 User community and applicability -> 5.3.1 Best practices time-stamp
  policy -> 1 Obbligo OVR-5.3-01, con il preambolo non numerato "This
  policy is aimed at meeting the requirements of time-stamp for long term
  validity (e.g. as defined in ETSI EN 319 122-1 [i.1]) but is generally
  applicable to any use which has a requirement for equivalent quality."
  incorporato prima del requisito (come da istruzione di capitolo).
- 6.1 Risk assessment -> 1 Obbligo OVR-6.1-01 (rinvio alla clausola 5 di
  ETSI EN 319 401).
- 6.2 Trust Service Practice Statement -> 6 Obblighi OVR-6.2-01..06.
  OVR-6.2-02 e' un unico requisito con lettere a)-g): lettere riportate per
  intero in `testo_integrale`, inclusa la congiunzione "and" prima della
  lettera g) e il rinvio interno a clausola 6.5.2 e 6.6.
- 6.3 Terms and conditions -> 1 Obbligo OVR-6.3-01 (rinvio alla clausola
  6.2 di ETSI EN 319 401).
- 6.4 Information security policy -> 1 Obbligo OVR-6.4-01 (rinvio alla
  clausola 6.3 di ETSI EN 319 401).
- 6.5 TSA obligations -> 6.5.1 General -> 1 Obbligo OVR-6.5-01; 6.5.2 "TSA
  obligations towards subscribers" -> 1 Principio dedicato, riferimento
  "clausola 6.5.2 (TSA obligations towards subscribers)" (la sottoclausola
  non contiene alcun requisito numerato: il suo testo e' una dichiarazione
  discorsiva che delimita l'ambito degli obblighi del sottoscrittore).
- 6.6 Information for relying parties -> 1 Obbligo OVR-6.6-01 con lettere
  a)-c) e la NOTE interna alla lettera a).
- 6.5.2 -> tipo_principio "scopo/ambito di applicazione" (preferito ad
  "altro"): la disposizione non definisce un concetto ne' enuncia un
  effetto giuridico autonomo, ma perimetra espressamente l'ambito degli
  obblighi del sottoscrittore ("places no specific obligations on the
  subscriber beyond any TSA specific requirements stated in the TSA's terms
  and conditions"), esattamente la funzione di una clausola di
  scopo/ambito. Nessun `oggetti_giuridici` valorizzato: la clausola vale
  per qualunque servizio di marcatura temporale della TSA (non solo
  qualificato) e non individua un oggetto giuridico specifico.

Trattamento delle formulazioni non prescrittive in senso stretto:
OVR-5.1-01 ("may define"), OVR-5.3-01 ("may be used") e OVR-6.2-03/04/05/06
("should"/"may") sono comunque modellati come Obbligo, non come Principio:
lo schema ha un solo tipo prescrittivo e il precedente consolidato (tutti i
REQ di ETSI EN 319 401, Fonte 10) tratta allo stesso modo raccomandazioni e
facolta' esplicite. Non sono state introdotte relazioni "deroga a"/"attua"
per queste sfumature di forza normativa: non vi e' alcun riscontro testuale
che le colleghi ad altri nodi (ADR-0008: nessuna istanza senza riscontro).

Trattamento di NOTE/EXAMPLE:
- OVR-6.2-03 porta un EXAMPLE (tempo medio tra guasti, tempo medio di
  ripristino, disposizioni di disaster recovery): mantiene il testo di
  esempio perche' e' parte integrante del requisito (indica quali
  informazioni di disponibilita' devono essere pubblicate), non mera
  bibliografia.
- OVR-6.6-01 lettera a) porta una NOTE interpretativa (come verificare la
  validita' della chiave di firma della TSU e rinvio all'allegato D per le
  verifiche oltre la fine del periodo di validita' del certificato):
  mantenuta, aggiunge contenuto operativo sostanziale.
- In questo capitolo non compaiono NOTE puramente bibliografiche (rinvio in
  blocco a uno standard esterno): nulla e' stato scartato per questo
  motivo.

`condizione_applicabilita`: valorizzata per i soli tre requisiti marcati
"[CONDITIONAL]" nel testo ufficiale (OVR-5.1-02, OVR-5.1-03, OVR-5.2-02),
con la condizione desunta dalla stessa protasi del requisito; la marcatura
"[CONDITIONAL]" resta in `testo_integrale` (subito dopo il requirement id) e
non entra nel `riferimento`, che resta il solo requirement id.

`soggetti`: QTSP/gestore, ruolo "obbligato" per la generalita' dei
requisiti (la TSA/TSP che eroga il servizio di marcatura temporale).
Unica eccezione OVR-6.6-01: il requisito impone alla TSA di inserire nei
termini e condizioni un obbligo a carico del terzo affidante, quindi la riga
porta anche {"categoria": "Terzi affidanti/pubblico", "ruolo":
"destinatario"} (precedente identico: OVR-6.3.5-03 di ETSI EN 319 411-1).

`tipo_obbligo` attribuito caso per caso: "organizzativo" per i requisiti di
rinvio a ETSI EN 319 401 (valutazione del rischio, practice statement,
termini e condizioni, politica di sicurezza delle informazioni - stesso
criterio dei rinvii analoghi di ETSI EN 319 411-1), per la definizione di
una policy propria (OVR-5.1-01/02), per l'ambito di applicazione della
policy (OVR-5.3-01), per gli obblighi aggiuntivi della TSA (OVR-6.5-01) e
per le modalita' di redazione/messa a disposizione della disclosure
statement (OVR-6.2-04/05/06); "informativo/trasparenza" per i requisiti che
prescrivono il contenuto di cio' che la TSA dichiara o rende disponibile
(OVR-5.1-03, OVR-5.2-01, OVR-5.2-01A, OVR-5.2-02, OVR-6.2-02, OVR-6.2-03,
OVR-6.6-01).

RELAZIONI interne: nessuna, come da istruzione di capitolo. I rinvii di
questo capitolo sono a numeri di clausola ("see clause 6.3", "see clause
6.6", "as defined in clause 6.5.2"), ad allegati ("annex B", "annex D") o a
standard esterni (ETSI EN 319 401, ETSI EN 319 122-1): nessuno cita
letteralmente il requirement id di un altro nodo di questa fonte, unica
condizione ammessa per creare una relazione interna. I quattro rinvii a
ETSI EN 319 401 clausole 5/6.1/6.2/6.3 (OVR-6.1-01, OVR-6.2-01, OVR-6.3-01,
OVR-6.4-01) sono verso un'altra fonte (Fonte 10, gia' censita): il loro
collegamento cross-fonte e' demandato alla Fase 6/ADR-0009 della sessione
principale, non costruito qui.

Artefatti di conversione PDF->markdown esclusi dal testo: i marcatori di
impaginazione "***ETSI***" e "<!-- Page N -->" e la formattazione in
grassetto dei requirement id ("**OVR-5.1-01:**" nel sorgente, reso come
"OVR-5.1-01:" in `testo_integrale` come negli altri moduli ETSI).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "OVR-5.1-01",
        "testo": (
            "La policy di riferimento del presente documento e' una Best practices Time-Stamp Policy "
            "(BTSP) per TSA che emettono marche temporali supportate da certificati a chiave pubblica, "
            "con un'accuratezza di 1 secondo o migliore; i requisiti di policy sono definiti in termini di "
            "tale policy. La TSA puo' definire una propria policy che potenzia (enhances) la policy "
            "definita nel presente documento."
        ),
        "testo_integrale": (
            "5.1 General requirements — The policy requirements are defined in the present document in "
            "terms of a time-stamp policy. The present document specifies one time-stamp policy: a Best "
            "practices Time-Stamp Policy (BTSP) for TSAs issuing time-stamps, supported by public key "
            "certificates, with an accuracy of 1 second or better. OVR-5.1-01: A TSA may define its own "
            "policy which enhances the policy defined in the present document."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-5.1-02",
        "testo": (
            "Se la TSA definisce una propria policy, essa deve incorporare o ulteriormente limitare "
            "(further constrain) i requisiti identificati nel presente documento."
        ),
        "testo_integrale": (
            "OVR-5.1-02 [CONDITIONAL]: If the TSA defines its own policy it shall incorporate or further "
            "constrain the requirements identified in the present document."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Si applica se la TSA definisce una propria policy di marca temporale che potenzia quella "
            "definita nel presente documento."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-5.1-03",
        "testo": (
            "Se la TSA fornisce un'accuratezza migliore di 1 secondo, tale accuratezza deve essere "
            "indicata nella dichiarazione informativa della TSA (TSA disclosure statement, v. clausola "
            "6.3) e in ciascuna marca temporale emessa con accuratezza migliore di 1 secondo."
        ),
        "testo_integrale": (
            "OVR-5.1-03 [CONDITIONAL]: If an accuracy of better than 1 second is provided by the TSA then "
            "the accuracy shall be indicated in the TSA disclosure statement (see clause 6.3) and in each "
            "time-stamp issued to an accuracy of better than 1 second."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Si applica se la TSA fornisce un'accuratezza migliore di 1 secondo."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-5.2-01",
        "testo": (
            "L'identificatore della policy di marca temporale specificata nel presente documento e' "
            "l'OID itu-t(0) identified-organization(4) etsi(0) time-stamp-policy(2023) "
            "policy-identifiers(1) best-practices-ts-policy (1), corrispondente alla policy a) BTSP "
            "(best practices policy for time-stamp); includendo tale identificatore di oggetto in una "
            "marca temporale, la TSA dichiara la conformita' alla policy di marca temporale "
            "identificata. La TSA deve includere l'identificatore delle policy di marca temporale "
            "supportate nella dichiarazione informativa della TSA che rende disponibile a sottoscrittori "
            "e terzi affidanti, per indicare la propria dichiarazione di conformita'."
        ),
        "testo_integrale": (
            "5.2 Policy name and identification — The identifier of the time-stamp policy specified in "
            "the present document is: a) BTSP: a best practices policy for time-stamp. itu-t(0) "
            "identified-organization(4) etsi(0) time-stamp-policy(2023) policy-identifiers(1) "
            "best-practices-ts-policy (1) By including this object identifier in a time-stamp, the TSA "
            "claims conformance to the identified time-stamp policy. OVR-5.2-01: A TSA shall include the "
            "identifier for the time-stamp policies being supported in the TSA disclosure statement that "
            "the TSA makes available to subscribers and relying parties, to indicate its claim of "
            "conformance."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-5.2-01A",
        "testo": (
            "La TSA deve supportare e includere l'identificatore BTSP sopra definito nella policy di "
            "marca temporale e nella dichiarazione informativa della TSA resa disponibile a "
            "sottoscrittori e terzi affidanti, per indicare la propria dichiarazione di conformita'."
        ),
        "testo_integrale": (
            "OVR-5.2-01A: The TSA shall support and include the above defined BTSP identifier in the "
            "time-stamp policy and in the TSA disclosure statement that the TSA makes available to "
            "subscribers and relying parties, to indicate its claim of conformance."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-5.2-02",
        "testo": (
            "Se la TSA utilizza uno o piu' identificatori, incluso un identificatore proprio, per le "
            "policy di marca temporale, essa deve indicare nella propria policy di marca temporale e "
            "nella propria dichiarazione informativa gli identificatori di tutte le policy di marca "
            "temporale supportate e il suddetto identificatore BTSP, per dichiarare la conformita' a "
            "tutte le policy applicabili, purche' tali policy supportate potenzino la policy BTSP senza "
            "deviazioni."
        ),
        "testo_integrale": (
            "OVR-5.2-02 [CONDITIONAL]: If the TSA uses one or more identifiers, including its own "
            "identifier, for the time-stamp policies, the TSA shall indicate in its time-stamp policy "
            "and in its TSA disclosure statement, identifiers of all supported time-stamp policies and "
            "the above defined BTSP identifier to indicate its claim of conformance to all applicable "
            "policies, provided those supported policies enhances the BTSP policy without deviation."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Si applica se la TSA utilizza uno o piu' identificatori, incluso un identificatore proprio, "
            "per le policy di marca temporale."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-5.3-01",
        "testo": (
            "La BTSP e' finalizzata a soddisfare i requisiti della marca temporale per la validita' a "
            "lungo termine (es. come definiti in ETSI EN 319 122-1) ma e' generalmente applicabile a "
            "qualsiasi uso che richieda una qualita' equivalente. Tale policy puo' essere usata per "
            "servizi di marcatura temporale pubblici o per servizi di marcatura temporale usati "
            "all'interno di una comunita' chiusa."
        ),
        "testo_integrale": (
            "5.3.1 Best practices time-stamp policy — This policy is aimed at meeting the requirements "
            "of time-stamp for long term validity (e.g. as defined in ETSI EN 319 122-1 [i.1]) but is "
            "generally applicable to any use which has a requirement for equivalent quality. "
            "OVR-5.3-01: This policy may be used for public time-stamping services or time-stamping "
            "services used within a closed community."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.1-01",
        "testo": (
            "Si applicano i requisiti identificati nella clausola 5 di ETSI EN 319 401 [4] (valutazione "
            "del rischio)."
        ),
        "testo_integrale": (
            "OVR-6.1-01: The requirements identified in ETSI EN 319 401 [4], clause 5 shall apply."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-01",
        "testo": (
            "Si applicano i requisiti specificati nella clausola 6.1 di ETSI EN 319 401 [4] (Trust "
            "Service Practice Statement)."
        ),
        "testo_integrale": (
            "OVR-6.2-01: The requirements specified in ETSI EN 319 401 [4], clause 6.1 shall apply."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-02",
        "testo": (
            "La Trust Service Practice Statement deve specificare almeno quanto segue, per ciascuna "
            "policy di marca temporale supportata dalla TSA: a) l'algoritmo o gli algoritmi di hashing "
            "usati per rappresentare il dato da marcare temporalmente; b) l'accuratezza dell'ora nelle "
            "marche temporali rispetto al UTC; c) eventuali limitazioni all'uso del servizio di "
            "marcatura temporale; d) gli obblighi del sottoscrittore come definiti nella clausola 6.5.2, "
            "se ve ne sono; e) gli obblighi del terzo affidante come definiti nella clausola 6.6; "
            "f) le informazioni su come verificare la marca temporale affinche' il terzo affidante sia "
            "considerato fare affidamento \"ragionevole\" sulla stessa (v. clausola 6.6), e su eventuali "
            "possibili limitazioni del periodo di validita' della marca temporale; e g) qualsiasi "
            "dichiarazione di conformita' ai requisiti sui servizi di marcatura temporale previsti dalla "
            "legge nazionale."
        ),
        "testo_integrale": (
            "OVR-6.2-02: The Trust Service Practice Statement shall at least specify the following for "
            "each time-stamp policy supported by the TSA: a) the hashing algorithm (or algorithms) used "
            "to represent the datum being time-stamped; b) the accuracy of the time in the time-stamps "
            "with respect to UTC; c) any limitations on the use of the time-stamping service; d) the "
            "subscriber's obligations as defined in clause 6.5.2, if any; e) the relying party's "
            "obligations as defined in clause 6.6; f) information on how to verify the time-stamp such "
            "that the relying party is considered to \"reasonably rely\" on the time-stamp (see clause "
            "6.6), and on any possible limitations on the validity period of the time-stamp; and g) any "
            "claim to meet the requirements on time-stamping services under national law."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-03",
        "testo": (
            "La TSA dovrebbe includere nella propria dichiarazione informativa le informazioni sulla "
            "disponibilita' del proprio servizio di marcatura temporale. Esempio: tempo medio atteso tra "
            "i guasti del servizio di marcatura temporale, tempo medio atteso di ripristino a seguito di "
            "un guasto e disposizioni adottate per il disaster recovery, inclusi i servizi di backup."
        ),
        "testo_integrale": (
            "OVR-6.2-03: The TSA should include in its TSA disclosure statement information about the "
            "availability of its time-stamping service. EXAMPLE: Expected mean time between failure of "
            "the time-stamping service, expected mean time to recovery following a failure and "
            "provisions made for disaster recovery including back-up services."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-04",
        "testo": (
            "La dichiarazione informativa della TSA puo' essere redatta secondo il modello fornito "
            "nell'allegato B (annex B)."
        ),
        "testo_integrale": (
            "OVR-6.2-04: The TSA disclosure statement may be created according to the template given in "
            "annex B."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-05",
        "testo": (
            "La dichiarazione informativa della TSA puo' essere fornita come parte di un accordo tra "
            "sottoscrittore e terzo affidante (subscriber/relying party agreement)."
        ),
        "testo_integrale": (
            "OVR-6.2-05: The TSA disclosure statement may be provided as part of a subscriber/relying "
            "party agreement."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-06",
        "testo": (
            "La dichiarazione informativa della TSA puo' essere inclusa in una TSA practice statement, "
            "purche' sia ben visibile (conspicuous) al lettore."
        ),
        "testo_integrale": (
            "OVR-6.2-06: The TSA disclosure statement may be included in a TSA practice statement "
            "provided that it is conspicuous to the reader."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.3-01",
        "testo": (
            "Si applicano i requisiti identificati nella clausola 6.2 di ETSI EN 319 401 [4] (termini e "
            "condizioni)."
        ),
        "testo_integrale": (
            "OVR-6.3-01: The requirements identified in ETSI EN 319 401 [4], clause 6.2 shall apply."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.4-01",
        "testo": (
            "Si applicano i requisiti identificati nella clausola 6.3 di ETSI EN 319 401 [4] (politica "
            "di sicurezza delle informazioni)."
        ),
        "testo_integrale": (
            "OVR-6.4-01: The requirements identified in ETSI EN 319 401 [4], clause 6.3 shall apply."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.5-01",
        "testo": (
            "La TSA deve rispettare qualsiasi obbligo aggiuntivo indicato nella marca temporale, "
            "direttamente o incorporato per riferimento."
        ),
        "testo_integrale": (
            "OVR-6.5-01: The TSA shall adhere to any additional obligations indicated in the time-stamp "
            "either directly or incorporated by reference."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.6-01",
        "testo": (
            "I termini e le condizioni resi disponibili ai terzi affidanti (v. clausola 6.3) devono "
            "includere un obbligo, a carico del terzo affidante che si affida a una marca temporale, "
            "di: a) verificare che la marca temporale sia stata firmata correttamente e che la chiave "
            "privata usata per firmare la marca temporale non sia stata compromessa fino al momento "
            "della verifica (NOTA: durante il periodo di validita' del certificato della TSU, la "
            "validita' della chiave di firma puo' essere verificata usando lo stato di revoca corrente "
            "del certificato della TSU; se il momento della verifica eccede la fine del corrispondente "
            "periodo di validita' del certificato, v. l'allegato D per una guida); b) tenere conto di "
            "eventuali limitazioni all'uso della marca temporale indicate dalla policy di marca "
            "temporale; e c) tenere conto di qualsiasi altra precauzione prescritta negli accordi o "
            "altrove."
        ),
        "testo_integrale": (
            "OVR-6.6-01: The terms and conditions made available to relying parties (see clause 6.3) "
            "shall include an obligation on the relying party, when relying on a time-stamp, to: "
            "a) verify that the time-stamp has been correctly signed and that the private key used to "
            "sign the time-stamp has not been compromised until the time of the verification; NOTE: "
            "During the TSU's certificate validity period, the validity of the signing key can be "
            "checked using current revocation status for the TSU's certificate. If the time of "
            "verification exceeds the end of the corresponding certificate validity period, see annex D "
            "for guidance. b) take into account any limitations on the usage of the time-stamp "
            "indicated by the time-stamp policy; and c) take into account any other precautions "
            "prescribed in agreements or elsewhere."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 6.5.2 (TSA obligations towards subscribers)",
        "testo": (
            "Il presente documento non pone obblighi specifici a carico del sottoscrittore oltre a "
            "eventuali requisiti specifici della TSA indicati nei termini e condizioni della TSA stessa: "
            "gli obblighi del sottoscrittore sono quindi solo quelli che la TSA stabilisce nei propri "
            "termini e condizioni."
        ),
        "testo_integrale": (
            "6.5.2 TSA obligations towards subscribers — The present document places no specific "
            "obligations on the subscriber beyond any TSA specific requirements stated in the TSA's "
            "terms and conditions."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "OVR-5.1-01",
    "OVR-5.1-02",
    "OVR-5.1-03",
    "OVR-5.2-01",
    "OVR-5.2-01A",
    "OVR-5.2-02",
    "OVR-5.3-01",
    "OVR-6.1-01",
    "OVR-6.2-01",
    "OVR-6.2-02",
    "OVR-6.2-03",
    "OVR-6.2-04",
    "OVR-6.2-05",
    "OVR-6.2-06",
    "OVR-6.3-01",
    "OVR-6.4-01",
    "OVR-6.5-01",
    "clausola 6.5.2 (TSA obligations towards subscribers)",
    "OVR-6.6-01",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
