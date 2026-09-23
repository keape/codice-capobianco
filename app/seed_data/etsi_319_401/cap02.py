"""Estrazione granulare ETSI EN 319 401 V3.2.1 (2026-01) — Capitolo 2: clausole
5 (Risk Management Framework and Risk Assessment) e 6 (Policies and
practices: 6.1 Trust Service Practice statement, 6.2 Terms and Conditions,
6.3 Information and Network Security Policy).

Fonte 10 (numerazione definitiva cablata dalla sessione principale in
app/seed.py — questo modulo NON tocca seed.py). Testo ufficiale in
app/.source_cache/etsi_319_401/cap02.txt. Manifest di split:
app/.source_cache/etsi_319_401/manifest.json.

Modellazione (ADR-0007), stesso criterio già applicato a ETSI TS 119 461
(fonte 9, vedi app/seed_data/etsi_119_461/cap02.py) per un capitolo tecnico
ETSI a clausole/requisiti numerati:

Struttura del testo — entrambe le clausole 5 e 6 hanno solo intestazioni
di sezione seguite immediatamente dal primo requisito numerato (nessun
paragrafo introduttivo privo di REQ proprio da assorbire come Principio
autonomo): "## 5 Risk Management Framework..." precede direttamente
REQ-5-01; "## 6 Policies and practices" non ha testo proprio, seguito
direttamente da "#### 6.1 ..." e da REQ-6.1-01; stesso schema per 6.2/6.3.
Di conseguenza RIGHE_PRINCIPI è vuoto in questo capitolo: ogni item di
indice corrisponde 1:1 a un requisito REQ-x.y-nn -> 1 Obbligo.

Criterio per gli elenchi a lettere (a, b, c...) sotto un requisito: restano
nello stesso nodo del REQ che li introduce quando non hanno un prefisso
REQ/PRO proprio (es. REQ-5-01 a)-f), REQ-5-06 a)-e), REQ-5-07 a)-j),
REQ-5-08 a)-f), REQ-6.2-02 a)-k), REQ-6.3-01 a)-j|, REQ-6.3-03 a)-b),
REQ-6.3-04 a)-b) restano un solo nodo ciascuno). Quando invece il testo
introduce un paragrafo con "In particular:" seguito da un elenco di
requisiti che hanno ciascuno un proprio id REQ-x.y-nn distinto (REQ-6.1-02
-> REQ-6.1-03..11; REQ-6.3-02 -> REQ-6.3-03..09), il paragrafo introduttivo
resta comunque un nodo a sé (ha un proprio REQ e un proprio contenuto
prescrittivo — l'obbligo di approvazione/pubblicazione/comunicazione della
politica, distinto dal contenuto elencato nei requisiti seguenti), e i
requisiti elencati restano nodi separati con il proprio riferimento
letterale, secondo l'istruzione generale (non si spezza un REQ per le sue
lettere interne, ma qui le "lettere" hanno già un prefisso REQ proprio).

NOTE informative: omesse da `testo_integrale` quando puramente di rimando
bibliografico a un altro standard senza contenuto interpretativo proprio
(REQ-5-02 NOTE -> ISO/IEC 27005:2022; REQ-6.3-05 NOTE 2 -> ISO/IEC
27002:2022 clausola 5.1; REQ-6.3-09 NOTE 3 -> CA/Browser Forum network
security guide). Mantenute quando aggiungono contenuto sostanziale
interpretativo: REQ-5-07 NOTE (definisce "risk appetite"/"risk tolerance
level" ai fini del requisito, più l'EXAMPLE che li esemplifica),
REQ-6.1-03 NOTE 1 (chiarisce che non è richiesta una struttura specifica
per la practice statement), REQ-6.1-05 NOTE 2 (chiarisce il perimetro di
non-divulgazione delle informazioni sensibili), REQ-6.1-09 NOTE 3
(chiarisce il contenuto minimo del preavviso), REQ-6.3-04 NOTE 1
(applicabilità specifica ai TSP qualificati ex Regolamento (UE) 2014/910),
REQ-6.2-02 EXAMPLE 1/2 (esemplificano le lettere b) e d) della lista).

tipo_obbligo — come da assegnazione: "organizzativo" per clausola 5
(gestione del rischio, framework interno) e per 6.1/6.3 (governance delle
policy/practice statement e della politica di sicurezza — non sono
controlli tecnici in senso stretto, sono requisiti di definizione,
approvazione, revisione e comunicazione di documenti di governance);
"informativo/trasparenza" per 6.2 (Terms and Conditions: informazioni che
il TSP deve rendere disponibili a subscriber/relying party).

Casi particolari:
- REQ-6.1-09 è marcato "[CONDITIONAL]" -> `condizione_applicabilita`
  valorizzata, marcatura mantenuta in `testo_integrale` come da istruzione,
  omessa dal `riferimento`.
- REQ-5-08 e REQ-6.3-07 citano testualmente altri REQ dello stesso
  capitolo ("REQ-5.1, c)"; "REQ-6.1-07") — riportati letteralmente come
  nel testo ufficiale (incluso l'uso non uniforme del punto vs trattino in
  "REQ-5.1" nel testo originale), senza generare relazioni: per vincolo di
  fase RELAZIONI resta vuoto anche per i legami interni allo stesso
  capitolo, demandati a un'eventuale cura successiva della sessione
  principale.
- REQ-6.2-06 ("Terms and conditions may be transmitted electronically")
  usa "may" invece di "shall": modellato comunque come Obbligo (ogni
  REQ-x.y-nn numerato -> un nodo Obbligo, indipendentemente dal verbo
  modale) con tipo_obbligo "informativo/trasparenza" coerente con il resto
  di 6.2 — è una facoltà riconosciuta al TSP nell'ambito degli obblighi
  informativi sui T&C, non un requisito comportamentale a sé stante.

RELAZIONI: vuoto per vincolo di fase — nessuna relazione, né interna al
capitolo né cross-capitolo/cross-fonte. Verrà eventualmente popolato dalla
pipeline dedicata (ADR-0009) o da una cura editoriale successiva.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "REQ-5-01",
        "testo": (
            "Il TSP deve: a) effettuare e documentare valutazioni del rischio per "
            "identificare, analizzare e valutare i rischi del servizio fiduciario "
            "tenendo conto di aspetti aziendali e tecnici; b) definire, attuare e "
            "documentare un piano di trattamento del rischio basato sui risultati "
            "della valutazione; c) stabilire procedure di identificazione, analisi, "
            "valutazione e trattamento dei rischi ('processo di gestione del rischio "
            "di cybersicurezza'), che deve essere parte integrante del processo di "
            "gestione del rischio complessivo del TSP, ove applicabile; d) definire, "
            "attuare e applicare una politica e procedure per valutare se le misure "
            "di gestione del rischio di cybersicurezza sono effettivamente "
            "implementate e mantenute; e) definire e mantenere un adeguato framework "
            "di gestione del rischio per identificare e affrontare i rischi alla "
            "sicurezza dei sistemi di rete e informativi; f) rivedere e, se "
            "opportuno, aggiornare politica e procedure a intervalli pianificati, "
            "almeno annualmente, e quando si verificano incidenti significativi o "
            "cambiamenti significativi alle operazioni o ai rischi."
        ),
        "testo_integrale": (
            "REQ-5-01: The TSP shall: a) perform and document risk assessments to "
            "identify, analyse and evaluate trust service risks taking into account "
            "business and technical issues; b) establish, implement and document a "
            "risk treatment plan based on the risk assessment results; c) establish "
            "procedures for identification, analysis, assessment and treatment of "
            "risks ('cybersecurity risk management process'). The cybersecurity risk "
            "management process shall be an integral part of the TSP's overall risk "
            "management process, where applicable; d) establish, implement and apply "
            "a policy and procedures to assess whether the cybersecurity "
            "risk-management measures taken by the TSP are effectively implemented "
            "and maintained; e) establish and maintain an appropriate risk "
            "management framework to identify and address the risks posed to the "
            "security of network and information systems; and f) review and, where "
            "appropriate, update the policy and procedures at planned intervals, at "
            "least annually, and when significant incidents or significant changes "
            "to operations or risks occur."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-5-02",
        "testo": (
            "Il TSP deve, sulla base dei risultati della valutazione del rischio, "
            "definire, attuare e monitorare un piano di trattamento del rischio, "
            "che deve garantire un livello di sicurezza commisurato al grado di "
            "rischio."
        ),
        "testo_integrale": (
            "REQ-5-02: The TSP shall, based on the risk assessment results, "
            "establish, implement and monitor a risk treatment plan. The risk "
            "treatment plan shall ensure that the level of security is commensurate "
            "to the degree of risk."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-5-03",
        "testo": (
            "Il TSP deve determinare tutti i requisiti di sicurezza e le procedure "
            "operative necessarie per attuare le misure di trattamento del rischio "
            "scelte, come documentato nella politica di sicurezza delle informazioni "
            "e nella dichiarazione delle pratiche del servizio fiduciario (trust "
            "service practice statement, v. clausola 6)."
        ),
        "testo_integrale": (
            "REQ-5-03: The TSP shall determine all security requirements and "
            "operational procedures that are necessary to implement the risk "
            "treatment measures chosen, as documented in the information security "
            "policy and the trust service practice statement (see clause 6)."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-5-04",
        "testo": (
            "Il TSP deve rivedere e, se opportuno, aggiornare i risultati della "
            "valutazione del rischio e il piano di trattamento del rischio a "
            "intervalli pianificati e almeno annualmente, e quando si verificano "
            "cambiamenti significativi alle operazioni o ai rischi, o incidenti "
            "significativi."
        ),
        "testo_integrale": (
            "REQ-5-04: The TSP shall review and, where appropriate, update the risk "
            "assessment results and the risk treatment plan at planned intervals "
            "and at least annually, and when significant changes to operations or "
            "risks or significant incidents occur."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-5-05",
        "testo": (
            "Gli organi di gestione del TSP, o, se applicabile, le persone "
            "responsabili e dotate dell'autorità per gestire i rischi, devono: a) "
            "approvare il framework di valutazione del rischio, incluso il piano di "
            "valutazione del rischio e il processo di gestione del rischio di "
            "cybersicurezza; e b) accettare il rischio residuo identificato."
        ),
        "testo_integrale": (
            "REQ-5-05: The TSP's management bodies or, where applicable, the "
            "persons who are accountable and have the authority to manage risks "
            "shall: a) approve the risk assessment framework, including risk "
            "assessment plan and the cybersecurity risk management process; and b) "
            "accept the residual risk identified."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-5-06",
        "testo": (
            "Nell'identificare e definire le priorità delle opzioni e misure di "
            "trattamento del rischio appropriate, il TSP deve tenere conto di: a) i "
            "risultati della valutazione del rischio; b) i risultati della "
            "procedura di valutazione dell'efficacia delle misure di gestione del "
            "rischio di cybersicurezza; c) il costo di attuazione in relazione al "
            "beneficio atteso; d) la classificazione degli asset di cui alla "
            "clausola 7.3.2; e) l'analisi dell'impatto sul business di cui al piano "
            "di continuità operativa."
        ),
        "testo_integrale": (
            "REQ-5-06: When identifying and prioritising appropriate risk treatment "
            "options and measures, the TSP shall take into account: a) the risk "
            "assessment results; b) the results of the procedure to assess the "
            "effectiveness of cybersecurity risk-management measures; c) the cost of "
            "implementation in relation to the expected benefit; d) the asset "
            "classification referred to in clause 7.3.2; and e) the business impact "
            "analysis referred to in the business continuity plan."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-5-07",
        "testo": (
            "Come parte del processo di gestione del rischio di cybersicurezza, il "
            "TSP deve: a) seguire una metodologia di gestione del rischio; b) "
            "stabilire il livello di tolleranza al rischio in coerenza con il "
            "proprio risk appetite (l'ammontare e il tipo di rischio che il TSP è "
            "disposto ad accettare per i propri obiettivi di business, tipicamente "
            "espresso in una dichiarazione di alto livello approvata dagli organi di "
            "gestione; il livello di tolleranza al rischio ne è la traduzione in "
            "soglie quantificabili per specifiche categorie di rischio o processi di "
            "business — es. un risk appetite 'basso per i rischi che incidono sulla "
            "disponibilità del servizio fiduciario' può tradursi in una tolleranza "
            "'downtime massimo accettabile di 20 minuti al mese per l'emissione di "
            "certificati qualificati'); c) stabilire e mantenere criteri di rischio "
            "pertinenti; d) identificare e documentare, con un approccio "
            "all-hazards, i rischi alla sicurezza dei sistemi di rete e informativi, "
            "in particolare rispetto a terzi e ai rischi che potrebbero causare "
            "interruzioni della disponibilità, integrità, autenticità e "
            "riservatezza dei sistemi, inclusa l'identificazione dei singoli punti "
            "di guasto; e) analizzare tali rischi considerando minaccia, "
            "probabilità, impatto e livello di rischio, tenendo conto della cyber "
            "threat intelligence e delle vulnerabilità; f) valutare i rischi "
            "identificati in base ai criteri di rischio; g) identificare e definire "
            "le priorità delle opzioni e misure di trattamento del rischio "
            "appropriate; h) monitorare in modo continuo l'attuazione delle misure "
            "di trattamento del rischio; i) identificare chi è responsabile "
            "dell'attuazione delle misure di trattamento del rischio e quando "
            "devono essere attuate; j) documentare le misure di trattamento del "
            "rischio scelte in un piano di trattamento del rischio e le motivazioni "
            "che giustificano l'accettazione dei rischi residui, in modo "
            "comprensibile."
        ),
        "testo_integrale": (
            "REQ-5-07: As part of the cybersecurity risk management process, the "
            "TSP shall: a) follow a risk management methodology; b) establish the "
            "risk tolerance level in accordance with the risk appetite of the TSP; "
            "NOTE: For the purposes of this requirement: 'Risk appetite' refers to "
            "the amount and type of risk that a TSP is willing to accept in pursuit "
            "of its business objectives, typically expressed as a high-level "
            "statement approved by management bodies. 'Risk tolerance level' refers "
            "to the specific maximum risk that the TSP is willing to bear for "
            "particular risk categories or business processes, typically expressed "
            "through quantifiable metrics or thresholds. EXAMPLE: A TSP's risk "
            "appetite statement might indicate 'low appetite for risks affecting "
            "trust service availability', whilst the corresponding risk tolerance "
            "level might specify 'maximum acceptable downtime of 20 minutes per "
            "month for qualified certificate issuance services'. c) establish and "
            "maintain relevant risk criteria; d) in line with an all-hazards "
            "approach, identify and document the risks posed to the security of "
            "network and information systems, in particular in relation to third "
            "parties and risks that could lead to disruptions in the availability, "
            "integrity, authenticity and confidentiality of the network and "
            "information systems, including the identification of single point of "
            "failures; e) analyse the risks posed to the security of network and "
            "information systems, including threat, likelihood, impact, and risk "
            "level, taking into account cyber threat intelligence and "
            "vulnerabilities; f) evaluate the identified risks based on the risk "
            "criteria; g) identify and prioritise appropriate risk treatment "
            "options and measures; h) continuously monitor the implementation of "
            "the risk treatment measures; i) identify who is responsible for "
            "implementing the risk treatment measures and when they should be "
            "implemented; j) document the chosen risk treatment measures in a risk "
            "treatment plan and the reasons justifying the acceptance of residual "
            "risks in a comprehensible manner."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-5-08",
        "testo": (
            "La politica e le procedure di cui al REQ-5-01, lettera c), devono "
            "tenere conto dei risultati della valutazione del rischio di cui alla "
            "clausola 5 e degli incidenti significativi passati. Il TSP deve "
            "determinare: a) quali misure di gestione del rischio di cybersicurezza "
            "devono essere monitorate e misurate, inclusi processi e controlli; b) i "
            "metodi di monitoraggio, misurazione, analisi e valutazione, se "
            "applicabili, per garantire risultati validi; c) quando il monitoraggio "
            "e la misurazione devono essere effettuati; d) chi è responsabile del "
            "monitoraggio e della misurazione dell'efficacia delle misure di "
            "gestione del rischio di cybersicurezza; e) quando i risultati del "
            "monitoraggio e della misurazione devono essere analizzati e valutati; "
            "f) chi deve analizzare e valutare tali risultati."
        ),
        "testo_integrale": (
            "REQ-5-08: The policy and procedures referred to in REQ-5.1, c) shall "
            "take into account results of the risk assessment pursuant to clause 5 "
            "and past significant incidents. The TSP shall determine: a) what "
            "cybersecurity risk-management measures are to be monitored and "
            "measured, including processes and controls; b) the methods for "
            "monitoring, measurement, analysis and evaluation, as applicable, to "
            "ensure valid results; c) when the monitoring and measuring is to be "
            "performed; d) who is responsible for monitoring and measuring the "
            "effectiveness of the cybersecurity risk-management measures; e) when "
            "the results from monitoring and measurement are to be analysed and "
            "evaluated; f) who has to analyse and evaluate these results."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.1-01",
        "testo": (
            "Il TSP deve specificare l'insieme di politiche e pratiche appropriate "
            "per i servizi fiduciari che fornisce."
        ),
        "testo_integrale": (
            "REQ-6.1-01: The TSP shall specify the set of policies and practices "
            "appropriate for the trust services it is providing."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.1-02",
        "testo": (
            "L'insieme di politiche e pratiche deve essere approvato dalla "
            "direzione, pubblicato e comunicato ai dipendenti e alle parti esterne, "
            "per quanto rilevante (i requisiti seguenti REQ-6.1-03 a REQ-6.1-11 ne "
            "specificano il contenuto)."
        ),
        "testo_integrale": (
            "REQ-6.1-02: The set of policies and practices shall be approved by "
            "management, published and communicated to employees and external "
            "parties as relevant. In particular:"
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.1-03",
        "testo": (
            "Il TSP deve disporre di una dichiarazione delle pratiche e procedure "
            "usate per soddisfare tutti i requisiti della trust service policy "
            "applicabile identificata dal TSP (il presente documento non impone "
            "alcun requisito sulla struttura di tale dichiarazione)."
        ),
        "testo_integrale": (
            "REQ-6.1-03: The TSP shall have a statement of the practices and "
            "procedures used to address all the requirements of the applicable "
            "trust service policy as identified by the TSP. NOTE 1: The present "
            "document makes no requirement as to the structure of the trust service "
            "practice statement."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.1-04",
        "testo": (
            "La dichiarazione delle pratiche del TSP deve identificare gli obblighi "
            "di tutte le organizzazioni esterne che supportano i servizi del TSP, "
            "incluse le politiche e pratiche applicabili."
        ),
        "testo_integrale": (
            "REQ-6.1-04: The TSP's trust service practice statement shall identify "
            "the obligations of all external organizations supporting the TSP's "
            "services including the applicable policies and practices."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.1-05",
        "testo": (
            "Il TSP deve rendere disponibile a subscriber e relying party la "
            "propria dichiarazione delle pratiche e ogni altra documentazione "
            "rilevante, nella misura necessaria a dimostrare la conformità alla "
            "trust service policy (il TSP non è tenuto a divulgare gli aspetti "
            "contenenti informazioni sensibili in tale documentazione)."
        ),
        "testo_integrale": (
            "REQ-6.1-05: The TSP shall make available to subscribers and relying "
            "parties its practice statement, and other relevant documentation, as "
            "necessary to demonstrate conformance to the trust service policy. NOTE "
            "2: The TSP need not disclose any aspects containing sensitive "
            "information in the documentation that is made available to "
            "subscribers and relying parties."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.1-06",
        "testo": (
            "Il TSP deve disporre di un organo di gestione con responsabilità "
            "complessiva sul TSP e autorità finale per approvare la dichiarazione "
            "delle pratiche del TSP."
        ),
        "testo_integrale": (
            "REQ-6.1-06: The TSP shall have a management body with overall "
            "responsibility for the TSP with final authority for approving the "
            "TSP's practice statement."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.1-07",
        "testo": "La direzione del TSP deve attuare le pratiche.",
        "testo_integrale": (
            "REQ-6.1-07: The TSP's management shall implement the practices."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.1-08",
        "testo": (
            "Il TSP deve definire un processo di revisione delle pratiche, inclusa "
            "la responsabilità di mantenimento della dichiarazione delle pratiche "
            "del TSP."
        ),
        "testo_integrale": (
            "REQ-6.1-08: The TSP shall define a review process for the practices "
            "including responsibilities for maintaining the TSP's practice "
            "statement."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.1-09",
        "testo": (
            "Quando il TSP intende apportare modifiche alla propria dichiarazione "
            "delle pratiche che potrebbero incidere sull'accettazione del servizio "
            "da parte del soggetto, subscriber o relying party, deve dare loro "
            "adeguato preavviso delle modifiche (il preavviso non deve "
            "necessariamente indicare i dettagli delle modifiche, e può essere "
            "pubblicato nel repository del TSP)."
        ),
        "testo_integrale": (
            "[CONDITIONAL] REQ-6.1-09: When the TSP intends to make changes in its "
            "practice statement that might affect the acceptance of the service by "
            "the subject, subscriber or relying parties, it shall give due notice "
            "of changes to subscribers and relying parties. NOTE 3: The due notice "
            "does not need to provide the details of the changes. The due notice "
            "can be published on the TSP's repository."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "si applica solo se il TSP intende modificare la propria dichiarazione "
            "delle pratiche in un modo che potrebbe incidere sull'accettazione del "
            "servizio da parte di soggetto, subscriber o relying party"
        ),
    },
    {
        "riferimento": "REQ-6.1-10",
        "testo": (
            "Successivamente all'approvazione di cui al REQ-6.1-06, il TSP deve "
            "rendere immediatamente disponibile la dichiarazione delle pratiche "
            "revisionata, come richiesto dal REQ-6.1-05."
        ),
        "testo_integrale": (
            "REQ-6.1-10: The TSP shall, following approval as in REQ-6.1-06 above, "
            "make the revised TSP's practice statement immediately available as "
            "required under REQ-6.1-05 above."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.1-11",
        "testo": (
            "Il TSP deve indicare nelle proprie pratiche le disposizioni previste "
            "per la cessazione del servizio (v. clausola 7.12)."
        ),
        "testo_integrale": (
            "REQ-6.1-11: The TSP shall state in its practices the provisions made "
            "for termination of service (see clause 7.12)."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.2-01",
        "testo": (
            "Il TSP deve rendere disponibili a tutti i subscriber e relying party i "
            "termini e condizioni relativi ai propri servizi."
        ),
        "testo_integrale": (
            "REQ-6.2-01: TSP shall make the terms and conditions regarding its "
            "services available to all subscribers and relying parties."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.2-02",
        "testo": (
            "I termini e le condizioni devono specificare, per ciascuna trust "
            "service policy supportata dal TSP, almeno: a) la trust service policy "
            "applicata; b) eventuali limitazioni all'uso del servizio fornito, "
            "incluso il limite di responsabilità per danni derivanti da un uso del "
            "servizio che eccede tali limitazioni (es. la durata di vita prevista "
            "dei certificati a chiave pubblica); c) gli eventuali obblighi del "
            "subscriber; d) informazioni per le parti che si affidano al servizio "
            "fiduciario (es. come verificare il token del servizio fiduciario, "
            "eventuali limitazioni del periodo di validità associato al token); e) "
            "il periodo di conservazione dei log degli eventi del TSP; f) le "
            "limitazioni di responsabilità; g) l'ordinamento giuridico applicabile; "
            "h) le procedure per reclami e risoluzione delle controversie; i) se il "
            "servizio fiduciario del TSP è stato valutato conforme alla trust "
            "service policy e, in tal caso, attraverso quale schema di valutazione "
            "di conformità; j) i dati di contatto del TSP; e k) ogni impegno "
            "relativo alla disponibilità."
        ),
        "testo_integrale": (
            "REQ-6.2-02: The terms and conditions shall at least specify for each "
            "trust service policy supported by the TSP the following: a) the trust "
            "service policy being applied; b) any limitations on the use of the "
            "service provided including the limitation for damages arising from "
            "the use of services exceeding such limitations; EXAMPLE 1: The "
            "expected life-time of public key certificates. c) the subscriber's "
            "obligations, if any; d) information for parties relying on the trust "
            "service; EXAMPLE 2: How to verify the trust service token, any "
            "possible limitations on the validity period associated with the trust "
            "service token. e) the period of time during which TSP's event logs "
            "are retained; f) limitations of liability; g) the applicable legal "
            "system; h) procedures for complaints and dispute settlement; i) "
            "whether the TSP's trust service has been assessed to be conformant "
            "with the trust service policy, and if so through which conformity "
            "assessment scheme; j) the TSP's contact information; and k) any "
            "undertaking regarding availability."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.2-03",
        "testo": (
            "I subscriber e le parti che si affidano al servizio fiduciario devono "
            "essere informati, in modo chiaro, completo e facilmente accessibile, "
            "sia in uno spazio pubblicamente accessibile sia individualmente, dei "
            "termini e condizioni precisi, inclusi gli elementi elencati nel "
            "REQ-6.2-02, prima di stipulare un rapporto contrattuale."
        ),
        "testo_integrale": (
            "REQ-6.2-03: Subscribers and parties relying on the trust service shall "
            "be informed in a clear, comprehensive and easily accessible manner, in "
            "a publicly accessible space and individually of precise terms and "
            "conditions, including the items listed above, before entering into a "
            "contractual relationship."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.2-04",
        "testo": (
            "I termini e le condizioni devono essere resi disponibili tramite un "
            "mezzo di comunicazione duraturo."
        ),
        "testo_integrale": (
            "REQ-6.2-04: Terms and conditions shall be made available through a "
            "durable means of communication."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.2-05",
        "testo": (
            "I termini e le condizioni devono essere disponibili in un linguaggio "
            "facilmente comprensibile."
        ),
        "testo_integrale": (
            "REQ-6.2-05: Terms and conditions shall be available in a readily "
            "understandable language."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.2-06",
        "testo": "I termini e le condizioni possono essere trasmessi elettronicamente.",
        "testo_integrale": (
            "REQ-6.2-06: Terms and conditions may be transmitted electronically."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.3-01",
        "testo": (
            "Il TSP deve definire una politica sulla sicurezza dei sistemi di rete "
            "e informativi, approvata dalla direzione, che descriva l'approccio del "
            "TSP alla gestione della sicurezza dei propri sistemi di rete e "
            "informativi, e che: a) sia appropriata e complementare alla strategia "
            "e agli obiettivi di business del TSP; b) stabilisca gli obiettivi di "
            "sicurezza delle informazioni e della rete; c) includa un impegno al "
            "miglioramento continuo della sicurezza dei sistemi di rete e "
            "informativi; d) includa un impegno a fornire le risorse appropriate "
            "necessarie alla sua attuazione, incluso il personale, le risorse "
            "finanziarie, i processi, gli strumenti e le tecnologie necessari; e) "
            "sia comunicata e riconosciuta dai dipendenti rilevanti e dalle parti "
            "esterne interessate rilevanti; f) stabilisca ruoli e responsabilità ai "
            "sensi della clausola 7.1; g) elenchi la documentazione da conservare e "
            "la durata della sua conservazione; h) elenchi le politiche specifiche "
            "per argomento; i) stabilisca indicatori e misure per monitorare la sua "
            "attuazione e lo stato attuale del livello di maturità del TSP in "
            "materia di sicurezza delle informazioni e della rete; e j) indichi la "
            "data di approvazione formale da parte degli organi di gestione del "
            "TSP."
        ),
        "testo_integrale": (
            "REQ-6.3-01: The TSP shall define a policy on the security of network "
            "and information systems which is approved by management and which "
            "sets out the TSP's approach to managing the security of its network "
            "and information systems, that: a) are appropriate to and complementary "
            "with the TSP's business strategy and objectives; b) sets out network "
            "and information security objectives; c) includes a commitment to "
            "continual improvement of the security of network and information "
            "systems; d) includes a commitment to provide the appropriate resources "
            "needed for its implementation, including the necessary staff, "
            "financial resources, processes, tools and technologies; e) are "
            "communicated to and acknowledged by relevant employees and relevant "
            "interested external parties; f) lays down roles and responsibilities "
            "pursuant to clause 7.1; g) lists the documentation to be kept and the "
            "duration of retention of the documentation; h) lists the "
            "topic-specific policies; i) lays down indicators and measures to "
            "monitor its implementation and the current status of the TSP's "
            "maturity level of network and information security; and j) indicates "
            "the date of the formal approval by the management bodies of the TSP."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.3-02",
        "testo": (
            "Le modifiche alla politica di sicurezza delle informazioni devono "
            "essere comunicate alle terze parti, ove applicabile, inclusi "
            "subscriber, relying party, organismi di valutazione, organismi di "
            "supervisione o altri organismi regolatori (i requisiti seguenti "
            "REQ-6.3-03 a REQ-6.3-09 ne specificano il contenuto)."
        ),
        "testo_integrale": (
            "REQ-6.3-02: Changes to the information security policy shall be "
            "communicated to third parties, where applicable. This includes "
            "subscribers, relying parties, assessment bodies, supervisory or other "
            "regulatory bodies. In particular:"
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.3-03",
        "testo": (
            "La politica del TSP sulla sicurezza dei sistemi di rete e informativi "
            "deve essere: a) documentata, attuata e mantenuta, inclusi i controlli "
            "di sicurezza e le procedure operative per le strutture, i sistemi e "
            "gli asset informativi del TSP che forniscono i servizi; b) rivista e, "
            "se opportuno, aggiornata dagli organi di gestione almeno annualmente e "
            "quando si verificano incidenti significativi o cambiamenti "
            "significativi alle operazioni o ai rischi, documentando il risultato "
            "delle revisioni."
        ),
        "testo_integrale": (
            "REQ-6.3-03: A TSP's policy on the security of network and information "
            "systems shall be: a) documented, implemented and maintained including "
            "the security controls and operating procedures for TSP's facilities, "
            "systems and information assets providing the services. b) reviewed "
            "and, where appropriate, updated by management bodies at least "
            "annually and when significant incidents or significant changes to "
            "operations or risks occur. The result of the reviews shall be "
            "documented."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.3-04",
        "testo": (
            "Il TSP deve stabilire procedure per notificare all'organismo di "
            "supervisione le modifiche rilevanti nella fornitura del servizio "
            "fiduciario, incluse le modifiche nella fornitura dei servizi "
            "fiduciari e l'intenzione di cessarne la fornitura, in conformità ai "
            "requisiti di business e alle leggi e normative applicabili. Il TSP "
            "deve notificare l'organismo di supervisione almeno: a) un mese prima "
            "di attuare qualsiasi modifica; b) tre mesi prima della cessazione "
            "pianificata della fornitura di un servizio fiduciario (i prestatori di "
            "servizi fiduciari qualificati ai sensi del regolamento (UE) 2014/910 "
            "sono tenuti a informare l'organismo di supervisione di qualsiasi "
            "modifica nella fornitura dei propri servizi fiduciari qualificati e "
            "dell'intenzione di cessare tali attività)."
        ),
        "testo_integrale": (
            "REQ-6.3-04: The TSP shall establish procedures to notify of important "
            "changes in the provision of the trust service to the supervisory "
            "body, including changes in the provision of trust services and the "
            "intention to cease on its provision, in accordance with business "
            "requirements and relevant laws and regulations. The TSP shall notify "
            "the supervisory body at least: a) one month before implementing any "
            "change; b) three months before the planned cessation of a trust "
            "service provision. NOTE 1: Trust service providers qualified according "
            "to Regulation (EU) 2014/910 [i.1] are required to inform the "
            "supervisory body of any change in the provision of its qualified "
            "trust services and an intention to cease those activities."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.3-05",
        "testo": (
            "Il TSP deve pubblicare e comunicare la politica di sicurezza delle "
            "informazioni a tutti i dipendenti impattati da essa."
        ),
        "testo_integrale": (
            "REQ-6.3-05: The TSP shall publish and communicate the information "
            "security policy to all employees who are impacted by it."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.3-06",
        "testo": (
            "La politica del TSP sulla sicurezza dei sistemi di rete e informativi "
            "e l'inventario degli asset per la sicurezza delle informazioni (v. "
            "clausola 7.3) devono essere rivisti a intervalli pianificati, almeno "
            "annualmente, o in caso di cambiamenti significativi, per garantirne la "
            "continua idoneità, adeguatezza ed efficacia."
        ),
        "testo_integrale": (
            "REQ-6.3-06: The TSP's policy on the security of network and "
            "information systems and inventory of assets for information security "
            "(see clause 7.3) shall be reviewed at planned intervals, at least "
            "annually, or if significant changes occur to ensure their continuing "
            "suitability, adequacy and effectiveness."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.3-07",
        "testo": (
            "Le modifiche che incideranno sul livello di sicurezza fornito devono "
            "essere approvate dall'organo di gestione di cui al REQ-6.1-07."
        ),
        "testo_integrale": (
            "REQ-6.3-07: Any changes that will impact on the level of security "
            "provided shall be approved by the management body referred to in "
            "REQ-6.1-07."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.3-08",
        "testo": (
            "La configurazione dei sistemi del TSP deve essere controllata "
            "regolarmente per rilevare modifiche che violano le politiche di "
            "sicurezza del TSP."
        ),
        "testo_integrale": (
            "REQ-6.3-08: The configuration of the TSPs systems shall be regularly "
            "checked for changes which violate the TSPs security policies."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-6.3-09",
        "testo": (
            "L'intervallo massimo tra due controlli deve essere documentato nella "
            "dichiarazione delle pratiche del servizio fiduciario."
        ),
        "testo_integrale": (
            "REQ-6.3-09: The maximum interval between two checks shall be "
            "documented in the trust service practice statement."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = []

INDICE_ARTICOLI_LOCALE = [
    "REQ-5-01", "REQ-5-02", "REQ-5-03", "REQ-5-04", "REQ-5-05", "REQ-5-06",
    "REQ-5-07", "REQ-5-08",
    "REQ-6.1-01", "REQ-6.1-02", "REQ-6.1-03", "REQ-6.1-04", "REQ-6.1-05",
    "REQ-6.1-06", "REQ-6.1-07", "REQ-6.1-08", "REQ-6.1-09", "REQ-6.1-10",
    "REQ-6.1-11",
    "REQ-6.2-01", "REQ-6.2-02", "REQ-6.2-03", "REQ-6.2-04", "REQ-6.2-05",
    "REQ-6.2-06",
    "REQ-6.3-01", "REQ-6.3-02", "REQ-6.3-03", "REQ-6.3-04", "REQ-6.3-05",
    "REQ-6.3-06", "REQ-6.3-07", "REQ-6.3-08", "REQ-6.3-09",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from seed_data.lib import verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    print(
        f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
        f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti."
    )
