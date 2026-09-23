"""ETSI EN 319 401 V3.2.1 (2026-01) - Electronic Signatures and Trust
Infrastructures (ESI); General Policy Requirements for Trust Service
Providers. Fonte 10 (numerazione definitiva cablata dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 1:
clausole 1 (Scope), 2 (References, normative e informative), 3 (Definition
of terms, symbols, abbreviations and notation: 3.1 Terms, 3.2 Symbols, 3.3
Abbreviations, 3.4 Notation), 4 (Overview: 4.1 General, 4.2 Applicability of
Conditional Requirements). Testo ufficiale in
app/.source_cache/etsi_319_401/cap01.txt. Manifest di split:
app/.source_cache/etsi_319_401/manifest.json.

Modellazione (ADR-0007), stesso criterio già applicato a ETSI TS 119 461
(Fonte 9) per uno standard tecnico ETSI a clausole/sottoclausole invece che
articoli/commi di un atto legislativo:

- Clausola 1 (Scope) -> 1 Principio "scopo/ambito di applicazione",
  riferimento "clausola 1 (Scope)". Testo integrale riportato per intero (un
  solo paragrafo + una NOTE che rinvia a ETSI EN 319 403-1 per i requisiti
  degli organismi di valutazione della conformità - assorbita perché
  precisa il perimetro di applicabilità, non mera bibliografia).
- Clausola 2 (References, 2.1 Normative + 2.2 Informative) -> NESSUN nodo:
  è bibliografia/paratesto puro (elenco di documenti citati con numerazione
  [1]/[i.N], nessun contenuto normativo autonomo), stesso trattamento già
  riservato alla clausola 2 di ETSI TS 119 461 (Fonte 9) e di ETSI EN 319
  412-5 (Fonte 7). Non genera un item di indice.
- Clausola 3.1 (Terms) -> 1 Principio "definitorio" riassuntivo (non un nodo
  per singolo termine: la clausola è un glossario alfabetico piatto senza
  struttura a lettere/numeri propria). Include 36 termini; le NOTE "Source:
  ISO/IEC 27002:2022 [i.11]"/"Source: NIS2 Directive [i.13]"/"Source: ISO
  Guide 73:2009 [i.20]" ripetute su quasi ogni termine sono puro rimando
  bibliografico e sono scartate da `testo_integrale`; le NOTE che aggiungono
  contenuto interpretativo sostanziale (es. l'estensione di "trust service"
  oltre il perimetro eIDAS, l'esempio di "relying party", gli esempi di
  "trust service token", il rinvio interno "See clause 6.2" per "trust
  service practice statement") sono mantenute.
- Clausola 3.2 (Symbols) -> NESSUN nodo: il testo è integralmente "Void."
  senza alcun contenuto oltre il rinvio strutturale. Non genera un item di
  indice.
- Clausola 3.3 (Abbreviations) -> 1 Principio "definitorio" riassuntivo. La
  tabella arriva mal renderizzata dalla conversione PDF->markdown (celle
  disallineate: una riga markdown unisce le etichette di più righe
  originali in una sola cella, con la forma estesa dell'ultima abbreviazione
  elencata riportata da sola in fondo alla riga). Ricostruzione verificata
  per coerenza alfabetica (17 abbreviazioni, ordine originale: CA, CER, CRA,
  CSIRT, DGA, DNS, DORA, DSA, eIDAS, ICT, IP, IT, QTSP, SLA, SSASC, TSP,
  UTC) confrontando il raw della tabella in
  app/.source_cache/etsi_319_401/cap01.txt righe 87-108: la riga markdown
  "|ICT IP Internet Protocol IT Information Technology||Information &
  Communication Technology|" si scompone in tre coppie (ICT -> Information &
  Communication Technology, riportata in fondo riga; IP -> Internet
  Protocol; IT -> Information Technology, entrambe già appaiate inline);
  analogamente "|QTSP SLA Service-Level Agreement||Qualified Trust Service
  Provider|" si scompone in QTSP -> Qualified Trust Service Provider
  (riportata in fondo riga) e SLA -> Service-Level Agreement (appaiata
  inline). Le NOTE che identificano il regolamento/direttiva UE sotteso a
  un'abbreviazione (CER, CRA, DGA, DORA, DSA, eIDAS) sono mantenute perché
  aggiungono contenuto interpretativo sostanziale (individuano l'atto UE di
  riferimento), non mera bibliografia generica.
- Clausola 3.4 (Notation) -> 1 Principio "definitorio", riferimento
  "clausola 3.4 (Notation)". NODO CRUCIALE per l'intero documento e per i
  capitoli successivi: riporta la legenda COMPLETA e verbatim del formato
  identificativo dei requisiti (<3 lettere>-<numero di clausola>-<numero
  progressivo a 2 cifre>), delle quattro marcature - nessuna marcatura
  (requisito applicabile a qualunque TSP), "[CONDITIONAL]" (requisito
  applicabile solo a certe condizioni), "[CHOICE]" (requisito con più
  opzioni tra cui scegliere), "[PRO]" (requisito la cui implementazione può
  essere determinata su criteri di proporzionalità, clausola 4.1/4.2) - e
  delle due sole famiglie di prefisso usate nel documento: REQ (requisito
  generale applicabile a qualunque TSP) e PRO (requisito a implementazione
  determinata su criteri di proporzionalità). NOTA per gli altri capitoli e
  per la sessione principale: il testo ufficiale di questa clausola
  richiama "clause 4.1" per la proporzionalità sia al punto d) sia nella
  definizione del prefisso PRO, mentre clausola 4.1 (letta per questo stesso
  capitolo) dichiara che i criteri di proporzionalità sono "established in
  clause 4.2" - una apparente imprecisione interna al testo ufficiale,
  riportata verbatim in `testo_integrale` senza correzione (non è compito di
  questo censimento emendare il testo normativo).
- Clausola 4.1 (General) -> 1 Principio "scopo/ambito di applicazione",
  riferimento "clausola 4.1 (General)". Elenca i servizi fiduciari in ambito
  (non esaustivo: emissione di certificati a chiave pubblica, servizi di
  registrazione, marcatura temporale, conservazione a lungo termine,
  e-delivery, validazione di firme) e stabilisce la natura vincolante dei
  requisiti del documento per i TSP, soggetta ai criteri di proporzionalità
  di clausola 4.2, con guida di implementazione ISO/IEC 27002:2022 per i
  controlli di clausola 7 - è cornice di ambito/vincolatività, non
  definizione di un concetto nuovo, per cui "scopo/ambito di applicazione"
  è più preciso di "definitorio".
- Clausola 4.2 (Applicability of Conditional Requirements) -> 6 Obblighi
  REQ-4.2-01..06, categoria_soggetto "QTSP/gestore", ruolo "obbligato".
  Nessuno dei sei porta marcatura "[CONDITIONAL]"/"[PRO]" propria (sono tutti
  REQ semplici): impongono al TSP l'analisi di proporzionalità e la sua
  documentazione, non condizioni di applicabilità del requisito stesso.
  - REQ-4.2-01/02: "organizzativo" (fattori di proporzionalità da
    considerare nell'implementazione; implementazione dei requisiti "[PRO]"
    su base di criteri di proporzionalità, con l'EXAMPLE di applicazione
    mantenuto in `testo_integrale` perché parte integrante del requisito).
  - REQ-4.2-03: "procedurale" (documentare l'analisi di applicabilità come
    parte del framework di gestione del rischio - è l'atto procedurale di
    produrre la documentazione, non la sua conservazione).
  - REQ-4.2-04: "di conservazione" (mantenimento dell'analisi e dei suoi
    esiti come parte della documentazione di valutazione del rischio,
    disponibile per la revisione delle autorità competenti - obbligo di
    conservazione/disponibilità documentale in senso proprio).
  - REQ-4.2-05/06: "organizzativo" (governance sui requisiti PRO non
    applicati: divieto di scarto ingiustificato; effetto cumulativo che non
    deve compromettere la postura di sicurezza complessiva).

RELAZIONI interne: nessuna. I sette nodi di questo capitolo sono cornice
definitoria/di ambito autonoma (scope, glossario termini/abbreviazioni,
notazione degli id, overview generale) più i sei obblighi di clausola 4.2,
che sono tra loro una sequenza di prescrizioni sullo stesso oggetto
(l'analisi di proporzionalità) ma senza citazione testuale esplicita
dell'id di un requisito nel testo di un altro - si preferisce omettere una
relazione "specifica"/"richiama" arbitraria piuttosto che inventarla,
coerente con il criterio già adottato in ETSI TS 119 461 cap01.py.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "REQ-4.2-01",
        "testo": (
            "Nell'implementare i requisiti del presente documento, il TSP deve tenere in debito conto: il "
            "grado della propria esposizione ai rischi; le dimensioni del TSP; la probabilita' di accadimento "
            "di incidenti; e la gravita' dell'incidente, incluso il suo impatto sociale ed economico."
        ),
        "testo_integrale": (
            "REQ-4.2-01: When implementing the requirements in the present document, the TSP shall take due "
            "account of: the degree of its exposure to risks; the TSP's size; the likelihood of occurrence of "
            "incidents; and the incident's severity, including their societal and economic impact."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-4.2-02",
        "testo": (
            "I requisiti marcati '[PRO]' devono essere implementati sulla base di criteri di proporzionalita'. "
            "Esempio: un TSP di dimensioni micro con risorse limitate puo' implementare controlli compensativi "
            "quando la piena segregazione dei compiti non e' realizzabile, come una maggiore supervisione "
            "manageriale o un aumento del monitoraggio e della registrazione (logging); un TSP operante in un "
            "solo Stato membro con un numero limitato di utenti puo' implementare accordi di ridondanza meno "
            "complessi rispetto a un TSP operante in piu' Stati membri; oppure un TSP che fornisce servizi con "
            "criticita' minore puo' applicare intervalli di test di sicurezza meno frequenti rispetto a chi "
            "fornisce servizi altamente critici."
        ),
        "testo_integrale": (
            "REQ-4.2-02: Requirements indicated by \"[PRO]\" shall be implemented based on proportionality "
            "criteria. In addition: EXAMPLE: Examples of how proportionality criteria can be applied include: "
            "a micro-sized TSP with limited resources can implement compensating controls where full "
            "segregation of duties is not feasible, such as enhanced management oversight or increased "
            "monitoring and logging; a TSP operating in a single Member State with a limited number of users "
            "can implement less complex redundancy arrangements than a TSP operating across multiple Member "
            "States; or a TSP providing services with lower criticality can apply less frequent security "
            "testing intervals than those providing highly critical services."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-4.2-03",
        "testo": (
            "Il TSP deve documentare l'analisi di applicabilita' di tali requisiti come parte del proprio "
            "framework di gestione del rischio."
        ),
        "testo_integrale": (
            "REQ-4.2-03: The TSP shall document the analysis of applicability of such requirements as part of "
            "their risk management framework."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-4.2-04",
        "testo": (
            "Tale analisi e i relativi esiti devono essere mantenuti come parte della documentazione di "
            "valutazione del rischio ed essere disponibili per la revisione da parte delle autorita' "
            "competenti."
        ),
        "testo_integrale": (
            "REQ-4.2-04: This analysis and its outcomes shall be maintained as part of the risk assessment "
            "documentation and be available for review by relevant authorities."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-4.2-05",
        "testo": (
            "I requisiti PRO non devono essere scartati senza adeguata giustificazione, indipendentemente "
            "dalle dimensioni o dall'ambito operativo del TSP."
        ),
        "testo_integrale": (
            "REQ-4.2-05: PRO requirements shall not be dismissed without proper justification regardless of "
            "the TSP's size or scope of operations."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-4.2-06",
        "testo": (
            "Il TSP deve assicurare che l'effetto cumulativo degli eventuali requisiti PRO non applicati non "
            "comprometta la postura di sicurezza complessiva dei propri servizi ne' pregiudichi gli obiettivi "
            "del presente documento."
        ),
        "testo_integrale": (
            "REQ-4.2-06: The TSP shall ensure that the cumulative effect of any non-applied PRO requirements "
            "does not compromise the overall security posture of their services or undermine the objectives "
            "of the present document."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 1 (Scope)",
        "testo": (
            "Il documento specifica requisiti di policy generali per i Trust Service Provider (TSP), "
            "indipendenti dal tipo di TSP: requisiti di policy sulle prassi operative e di gestione dei TSP. "
            "Altre specifiche affinano ed estendono tali requisiti per le forme particolari di TSP. Il "
            "documento non specifica come i requisiti individuati possano essere valutati da una parte "
            "indipendente, inclusi i requisiti sulle informazioni da rendere disponibili a tali valutatori "
            "indipendenti, ne' requisiti sui valutatori stessi. Il documento mira a supportare i requisiti "
            "della direttiva NIS2 e affronta i requisiti generali di gestione della sicurezza e di "
            "cybersecurity dei servizi fiduciari (qualificati e non qualificati)."
        ),
        "testo_integrale": (
            "1 Scope: The present document specifies general policy requirements relating to Trust Service "
            "Providers (TSPs) that are independent of the type of TSP. It defines policy requirements on the "
            "operation and management practices of TSPs. Other specifications refine and extend these "
            "requirements as applicable to particular forms of TSP. The present document does not specify how "
            "the requirements identified can be assessed by an independent party, including requirements for "
            "information to be made available to such independent assessors, or requirements on such "
            "assessors. The present document aims to support the requirements on NIS2 Directive [i.13] and "
            "addresses the general requirements for security management and cybersecurity of trust services "
            "(qualified and non-qualified). NOTE: See ETSI EN 319 403-1 [i.2] for details about requirements "
            "for conformity assessment bodies assessing Trust Service Providers."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.1 (Terms)",
        "testo": (
            "La clausola definisce un glossario di 36 termini specifici del documento, raggruppabili per "
            "area: (i) sicurezza delle informazioni e gestione del rischio - 'access control', 'asset', "
            "'attack', 'authentication', 'authenticity', 'impact', 'incident', 'incident handling', "
            "'information security breach/event/incident/incident management', 'information system', "
            "'multi-factor authentication', 'near miss', 'policy', 'procedure', 'process', 'risk', 'risk "
            "analysis', 'risk assessment', 'risk management', 'risk treatment', 'vulnerability'; (ii) "
            "cybersecurity e NIS2 - 'cybersecurity', 'cyber threat', 'large-scale cybersecurity incident'; "
            "(iii) tempo - 'Coordinated Universal Time (UTC)' (scala temporale basata sul secondo secondo la "
            "Raccomandazione ITU-R TF.460-6); (iv) servizi fiduciari - 'relying party' (con nota: include chi "
            "verifica una firma digitale tramite certificato a chiave pubblica), 'subscriber', 'trust "
            "service' (nota: copre i servizi fiduciari eIDAS ma con formulazione applicabile anche oltre quel "
            "framework regolatorio), 'trust service component' (con esempio: quelli di clausola 4.4 di ETSI "
            "EN 319 411-1 e il Server Signing Application Service Component - SSASC - di ETSI TS 119 431-1), "
            "'trust service policy' (con nota su indipendenza dall'ambiente operativo specifico del TSP e "
            "possibile definizione da parte di TSP, standard, organizzazioni nazionali/internazionali o "
            "clienti), 'trust service practice statement' (rinvio a clausola 6.2), 'Trust Service Provider "
            "(TSP)', 'trust service token' (con esempio: certificati, CRL, token di marca temporale, risposte "
            "OCSP)."
        ),
        "testo_integrale": (
            "3.1 Terms: For the purposes of the present document, the following terms apply: access control: "
            "physical and logical access to assets that is authorized and/or restricted based on business and "
            "information security requirements. asset: anything that has value to the organization. attack: "
            "successful or unsuccessful unauthorized attempt to destroy, alter, disable, gain access to an "
            "asset or any attempt to expose, steal, or make unauthorized use of an asset. authentication: "
            "provision of assurance that a claimed characteristic of an entity is correct. authenticity: "
            "property that an entity is what it claims to be. Coordinated Universal Time (UTC): time scale "
            "based on the second as defined in Recommendation ITU-R TF.460-6 [i.4]. cybersecurity: activities "
            "necessary to protect network and information systems, the users of such systems, and other "
            "persons affected by cyber threats. cyber threat: potential circumstance, event or action that "
            "could damage, disrupt or otherwise adversely impact network and information systems, the users "
            "of such systems and other persons. impact: harm that may be suffered when a threat compromises "
            "an information asset. incident: any event compromising the availability, authenticity, integrity "
            "or confidentiality of stored, transmitted or processed data or of the services offered by, or "
            "accessible via, network and information systems. incident handling: any actions and procedures "
            "aiming to prevent, detect, analyse, and contain or to respond to and recover from an incident. "
            "information security breach: compromise of information security that leads to the undesired "
            "destruction, loss, alteration, disclosure of, or access to, protected information transmitted, "
            "stored or otherwise processed. information security event: occurrence indicating a possible "
            "information security breach or failure of security controls. information security incident: one "
            "or multiple related and identified information security events that can harm an organization's "
            "assets or compromise its operations. information security incident management: exercise of a "
            "consistent and effective approach to the handling of information security incidents. information "
            "system: set of applications, services, information technology assets, or other "
            "information-handling components. large-scale cybersecurity incident: incident whose disruption "
            "exceeds a Member State's capacity to respond to it or with a significant impact on at least two "
            "Member States. multi-factor authentication: authentication mechanism consisting of two or more "
            "of the independent categories of credentials (knowledge, possession and inherence factor) to "
            "verify the user's identity for a login or other transaction. near miss: event that could have "
            "compromised the availability, authenticity, integrity or confidentiality of stored, transmitted "
            "or processed data or of the services offered by, or accessible via, network and information "
            "systems, but was successfully prevented from transpiring or did not materialize. policy: "
            "intentions and direction of an organization, as formally expressed by its top management. "
            "procedure: specified way to carry out an activity or a process. process: set of interrelated or "
            "interacting activities that uses or transforms inputs to deliver a result. relying party: "
            "natural or legal person that relies upon an electronic identification or a trust service NOTE: "
            "Relying parties include parties verifying a digital signature using a public key certificate. "
            "risk: potential for loss or disruption caused by an incident and is to be expressed as a "
            "combination of the magnitude of such loss or disruption and the likelihood of occurrence of that "
            "incident. risk analysis: process of estimating the likelihood that an event will create an "
            "impact and include as necessary components, the foreseeability of a threat, the expected "
            "effectiveness of Safeguards, and an evaluated result. risk assessment: overall process of risk "
            "identification, risk analysis and risk evaluation. risk management: process for analysing, "
            "mitigating, overseeing, and reducing risk. risk treatment: process to modify risk. subscriber: "
            "legal or natural person bound by agreement with a trust service provider to any subscriber "
            "obligations. trust service: electronic service which enhances trust and confidence in electronic "
            "transactions NOTE: This definition is intended to cover trust services as defined in Regulation "
            "(EU) No 910/2014 [i.1], although its formulation allows for applicability beyond that specific "
            "regulatory framework. trust service component: one part of the overall service of a TSP EXAMPLE: "
            "Those identified in clause 4.4 of ETSI EN 319 411-1 [i.5]. Also, ETSI TS 119 431-1 [i.9] defines "
            "requirements for a Server Signing Application Service Component (SSASC) which can be implemented "
            "as part of TSP's service which also includes other service components. NOTE: Other standards, "
            "including ETSI standards, can specify requirements for other service components which can form "
            "part of a wider TSP's service. trust service policy: set of rules that indicates the "
            "applicability of a trust service to a particular community and/or class of application with "
            "common security requirements NOTE: A trust service policy describes what is offered and "
            "provides information about the level of the service. It is defined independently of the "
            "specific details of the specific operating environment of a TSP; a trust service policy can "
            "apply to a community to which several TSPs belong that abide by the common set of rules "
            "specified in that policy. It can be defined for example by the TSP, by standards, by national "
            "(e.g. government) or international organizations, by the customers (subscribers) of the TSP and "
            "it is not necessarily part of the TSP's documentation. trust service practice statement: "
            "statement of the practices that a TSP employs in providing a trust service NOTE: See clause 6.2 "
            "for further information on practice statement. Trust Service Provider (TSP): entity which "
            "provides one or more trust services. trust service token: physical or binary (logical) object "
            "generated or issued as a result of the use of a trust service NOTE: Examples of trust service "
            "tokens are: certificates, CRLs, time-stamp tokens, OCSP responses. vulnerability: weakness of an "
            "asset or control that can be exploited by one or more threats."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.3 (Abbreviations)",
        "testo": (
            "La clausola elenca 17 abbreviazioni specifiche del documento: CA (Certification Authority), CER "
            "(Critical Entities Resilience, Direttiva (UE) 2022/2557), CRA (Cyber Resilience Act, Regolamento "
            "(UE) 2024/2847), CSIRT (Computer Security Incident Response Team), DGA (Data Governance Act, "
            "Regolamento (UE) 2022/868), DNS (Domain Name System/Service), DORA (Digital Operational "
            "Resilience Act, Regolamento (UE) 2022/2554), DSA (Digital Services Act, Regolamento (UE) "
            "2022/2065), eIDAS (electronic IDentification, Authentication and trust Services - nome informale "
            "del Regolamento (UE) n. 910/2014 come modificato dal Regolamento (UE) 2024/1183), ICT "
            "(Information & Communication Technology), IP (Internet Protocol), IT (Information Technology), "
            "QTSP (Qualified Trust Service Provider), SLA (Service-Level Agreement), SSASC (Server Signing "
            "Application Service Component), TSP (Trust Service Provider), UTC (Coordinated Universal Time)."
        ),
        "testo_integrale": (
            "3.3 Abbreviations: For the purposes of the present document, the following abbreviations apply: "
            "CA: Certification Authority. CER: Critical Entities Resilience NOTE: See Directive (EU) 2022/2557 "
            "[i.22]. CRA: Cyber Resilience Act NOTE: See Regulation (EU) 2024/2847 [i.23]. CSIRT: Computer "
            "Security Incident Response Team. DGA: Data Governance Act NOTE: See Regulation (EU) 2022/868 "
            "[i.25]. DNS: Domain Name System/Service. DORA: Digital Operational Resilience Act NOTE: See "
            "Regulation (EU) 2022/2554 [i.21]. DSA: Digital Services Act NOTE: See Regulation (EU) 2022/2065 "
            "[i.24]. eIDAS: electronic IDentification, Authentication and trust Services NOTE: Informal name "
            "for Regulation (EU) No 910/2014 [i.1] amended by Regulation (EU) 2024/1183 [i.26]. ICT: "
            "Information & Communication Technology. IP: Internet Protocol. IT: Information Technology. QTSP: "
            "Qualified Trust Service Provider. SLA: Service-Level Agreement. SSASC: Server Signing "
            "Application Service Component. TSP: Trust Service Provider. UTC: Coordinated Universal Time. "
            "(Ricostruzione delle 17 coppie abbreviazione/forma estesa a partire dalla tabella del testo "
            "ufficiale, la cui conversione PDF->markdown unisce piu' etichette nella stessa cella "
            "disallineando l'ordine tra colonna sinistra e destra su alcune righe - raw in "
            "app/.source_cache/etsi_319_401/cap01.txt righe 87-108.)"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.4 (Notation)",
        "testo": (
            "La clausola definisce la notazione degli identificatori dei requisiti del documento. I requisiti "
            "si dividono in quattro categorie: (a) applicabili a qualunque TSP, indicati senza marcatura "
            "aggiuntiva; (b) applicabili solo a determinate condizioni, marcati '[CONDITIONAL]'; (c) che "
            "comprendono piu' opzioni tra cui scegliere secondo la situazione applicabile, marcati "
            "'[CHOICE]'; (d) la cui implementazione da parte del TSP puo' essere determinata sulla base di "
            "criteri di proporzionalita' descritti in clausola 4.1, marcati '[PRO]'. Il formato "
            "dell'identificatore di ciascun requisito e': <3 lettere identificative>-<numero di "
            "clausola>-<numero progressivo a 2 cifre>. Gli elementi di servizio (prefissi) usati nel "
            "documento sono due: REQ (requisito generale applicabile a qualunque TSP) e PRO (requisito la cui "
            "implementazione da parte del TSP puo' essere determinata sulla base di criteri di "
            "proporzionalita' descritti in clausola 4.1)."
        ),
        "testo_integrale": (
            "3.4 Notation: The requirements identified in the present document include: a) requirements "
            "applicable to any TSP. Such requirements are indicated by clauses without any additional "
            "marking; b) requirements applicable under certain conditions. Such requirements are indicated by "
            "clauses marked by \"[CONDITIONAL]\"; c) requirements that include several choices which ought to "
            "be selected according to the applicable situation. Such requirements are indicated by clauses "
            "marked by \"[CHOICE]\"; d) Requirements where the TSP's implementation may be determined based "
            "on proportionality criteria as described in clause 4.1. Such requirements are indicated by "
            "\"[PRO]\". Each requirement is identified as follows: <3 letters identifier>-<the clause "
            "number>-<2 digit number-incremental>. The service components are: REQ: General requirement "
            "applicable to any TSP. PRO: Requirements where the TSP's implementation may be determined based "
            "on proportionality criteria as described in clause 4.1."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.1 (General)",
        "testo": (
            "I servizi fiduciari possono comprendere, senza limitarsi a questi, l'emissione di certificati a "
            "chiave pubblica, la fornitura di servizi di registrazione, servizi di marcatura temporale, "
            "servizi di conservazione a lungo termine, servizi di recapito elettronico e/o servizi di "
            "validazione delle firme. I presenti requisiti di policy non intendono implicare alcuna "
            "restrizione sulla tariffazione dei servizi del TSP. I requisiti specificati nel documento sono "
            "obbligatori per i TSP e devono essere implementati come indicato, fatti salvi i criteri di "
            "proporzionalita' stabiliti in clausola 4.2. Nell'implementare i controlli di clausola 7, si "
            "dovrebbe applicare, ove opportuno, la guida fornita da ISO/IEC 27002:2022. La determinazione di "
            "dettaglio dei controlli necessari a soddisfare un obiettivo e' un bilanciamento tra il "
            "conseguimento della necessaria fiducia e la minimizzazione delle restrizioni sulle tecniche che "
            "un TSP puo' impiegare nell'erogazione dei servizi."
        ),
        "testo_integrale": (
            "4.1 General: Trust services can encompass but is not limited to the issuance of public key "
            "certificates, provision of registration services, time-stamping services, long term preservation "
            "services, e-delivery services and/or signature validation services. These policy requirements "
            "are not meant to imply any restrictions on charging for TSP's services. The requirements "
            "specified in the present document are mandatory for TSPs and shall be implemented as indicated, "
            "subject to the proportionality criteria established in clause 4.2. When implementing controls of "
            "clause 7, guidance given in ISO/IEC 27002:2022 [i.11] should be applied as appropriate. NOTE: The "
            "details of controls required to meet an objective is a balance between achieving the necessary "
            "confidence whilst minimizing the restrictions on the techniques that a TSP can employ in "
            "providing services."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 1 (Scope)",
    "clausola 3.1 (Terms)",
    "clausola 3.3 (Abbreviations)",
    "clausola 3.4 (Notation)",
    "clausola 4.1 (General)",
    "REQ-4.2-01",
    "REQ-4.2-02",
    "REQ-4.2-03",
    "REQ-4.2-04",
    "REQ-4.2-05",
    "REQ-4.2-06",
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
