"""Estrazione granulare ETSI EN 319 401 V3.2.1 (2026-01) — Capitolo 5 (ultimo):
clausole 7.10 (Collection of evidence), 7.11 (Business continuity management:
7.11.1 General, 7.11.2 Back up, 7.11.3 Crisis management), 7.12 (TSP
termination and termination plans), 7.13 (Compliance), 7.14 (Supply chain:
7.14.1 Supply chain policy, 7.14.2 Supply chain procedures and processes,
7.14.3 Responsibility, third parties agreements and SLA).

Fonte 10 (numerazione definitiva cablata dalla sessione principale in
app/seed.py — questo modulo NON tocca seed.py). Testo ufficiale in
app/.source_cache/etsi_319_401/cap05.txt. Manifest di split:
app/.source_cache/etsi_319_401/manifest.json.

Perimetro: SOLO le clausole 7.10-7.14 (righe 1-169 del testo capitolo).
Gli Annex A (mapping DORA), B (mapping eIDAS), C (mapping Reg. UE 2024/2690
NIS2) e D (Change history) più la sezione finale "History", presenti nello
stesso file .txt dopo la clausola 7.14, sono FUORI PERIMETRO: sono tabelle
di corrispondenza puramente informative che rimappano id di requisiti già
coperti come nodi nei capitoli 1-5 del presente documento, senza introdurre
contenuto normativo autonomo — stesso trattamento riservato altrove nel
censimento alla clausola 2 "References" (paratesto bibliografico). Nessun
item di indice generato per gli Annex, coerentemente con l'istruzione
dell'incarico.

Modellazione (ADR-0007), stesso criterio già applicato ai capitoli
precedenti di questa Fonte: ogni requisito con id proprio (prefisso
"REQ-x.y-nn" o "PRO-x.y-nn") -> un Obbligo, `riferimento` = id esatto senza
markup aggiuntivo. Le sotto-liste puntate a)/b)/c)... che fanno parte dello
stesso requisito (senza un proprio id REQ/PRO distinto) restano fuse nello
stesso nodo. Nessun Principio in questo capitolo: le intestazioni di
clausola/sottoclausola (7.10, 7.11, 7.11.1-3, 7.12, 7.13, 7.14, 7.14.1-3)
sono puri contenitori organizzativi la cui prosa introduttiva coincide con
(o è già assorbita in) il primo REQ della sezione — a differenza delle
sottoclausole 4.1-4.6 del capitolo 2, qui non c'è contenuto descrittivo o
definitorio autonomo che giustifichi un nodo separato.

Tutti i 74 requisiti hanno come unico soggetto obbligato il TSP
("QTSP/gestore", ruolo "obbligato") — nessun requisito di questo capitolo
individua un soggetto obbligato diverso dal TSP stesso.

Note tecniche puntuali:

- REQ-7.10-01..08: clausola 7.10 "Collection of evidence" -> tutti
  `tipo_obbligo` "di conservazione" (per istruzione esplicita
  dell'incarico). REQ-7.10-01 è il requisito generale di
  registrazione/conservazione; REQ-7.10-02..08 sono ciascuno un requisito
  puntuale introdotto dalla stessa frase "In particular:" ma con proprio id
  REQ distinto -> 7 nodi separati (non fusi in REQ-7.10-01), coerente con
  la regola "una lettera/voce con proprio prefisso REQ/PRO distinto ->
  nodo proprio". La NOTE 1 di REQ-7.10-01 ("See requirement REQ-7.13-05")
  è un mero rinvio incrociato interno, omesso da `testo_integrale` (nessun
  contenuto sostanziale proprio, e comunque nessuna relazione cross-nodo è
  popolata in questa fase). La NOTE 2 (rinvio a ISO/IEC 27002:2022) è
  bibliografica, omessa. L'EXAMPLE di REQ-7.10-08 (tecniche concrete di
  tamper-evidence) è sostanziale e mantenuto in `testo_integrale`.
- REQ-7.11-1-02: id riportato ESATTAMENTE come appare nel testo ufficiale
  ("REQ-7.11-1-02", con il trattino al posto del punto dopo "7.11" — refuso
  del documento ETSI, non corretto/rinumerato qui per istruzione esplicita
  dell'incarico: il riferimento deve essere l'id letterale). La sua NOTE 2
  ("Other disaster situations include failure of critical components...")
  è sostanziale (amplia la nozione di "disastro") ed è mantenuta in
  `testo_integrale`; la NOTE 1 (rinvio a clausole ISO/IEC 27002:2022) è
  bibliografica, omessa.
- PRO-7.11.2-05: prefisso "PRO-" (non "REQ-") -> comunque 1 Obbligo per
  istruzione esplicita dell'incarico ("ogni requisito con prefisso REQ-x.y-nn
  o PRO-x.y-nn -> 1 Obbligo"). Non è marcato con il tag bracket
  "[CONDITIONAL]"/"[PRO]" nel testo (la clausola "Where appropriate" è
  intrinseca alla formulazione del requisito, non un tag esplicito separato
  come nei REQ-7.14.3-01/05/06) -> `condizione_applicabilita` non
  valorizzata per questo nodo.
- REQ-7.11.2-03/04/06: tre requisiti distinti e non ridondanti nel testo
  ufficiale nonostante la somiglianza superficiale (integrity check
  periodico; test di ripristino a intervalli pianificati con azioni
  correttive documentate; test periodico di affidabilità del recupero in
  condizioni di ripristino) -> mantenuti come tre nodi separati, ciascuno
  con proprio id REQ.
- REQ-7.12-01..11: clausola 7.12 interamente `tipo_obbligo` "organizzativo"
  per istruzione esplicita dell'incarico. REQ-7.12-02 e REQ-7.12-03..09 sono
  introdotti da prosa di raccordo priva di proprio id ("Before the TSP
  terminates its services at least the following procedures apply:") ->
  nessun nodo autonomo per quella prosa, assorbita concettualmente nei REQ
  che la seguono. REQ-7.12-08 usa "should" (raccomandazione, non "shall")
  ma resta un Obbligo con id proprio REQ, senza campo `severita` (non usato
  altrove nel censimento senza indicazione esplicita di sanzione/livello).
- REQ-7.13-01..06: clausola 7.13 interamente "organizzativo" per istruzione
  esplicita, incluse le sotto-voci su accessibilità (REQ-7.13-03/04) e
  protezione dei dati personali (REQ-7.13-05) — pur trattandosi di
  contenuti che in altri capitoli di questo censimento sarebbero stati
  classificati "informativo/trasparenza" o "tecnico/sicurezza", qui si è
  seguita l'istruzione esplicita dell'incarico che fissa "organizzativo"
  per l'intera clausola 7.13. La NOTE 1 di REQ-7.13-05 contiene, oltre al
  rinvio bibliografico al Regolamento (UE) 2016/679, una precisazione
  sostanziale sul principio di minimizzazione dei dati identificativi
  raccolti in autenticazione -> mantenuta in `testo_integrale`; NOTE 2 e
  NOTE 3 (rinvii bibliografici a ISO/IEC 27701:2019 e ISO/IEC 27002:2022)
  omesse.
- Clausola 7.14 (Supply chain): `tipo_obbligo` deciso caso per caso tra
  "organizzativo" e "procedurale" in base al contenuto specifico, per
  istruzione dell'incarico. Criterio applicato: requisiti che istituiscono
  una policy, un accordo contrattuale, un registro o assegnano una
  responsabilità/ruolo di governo -> "organizzativo"; requisiti che
  impongono un'attività ricorrente di monitoraggio, revisione, verifica,
  selezione o gestione operativa continuativa -> "procedurale".
- REQ-7.14.3-01/05/06: unici tre requisiti di questo capitolo marcati
  "[CONDITIONAL]" nel testo ufficiale -> `condizione_applicabilita`
  valorizzata con la condizione testuale (uso di altre parti/di una
  componente di servizio fiduciario fornita da terzi); "[CONDITIONAL]"
  mantenuto in `testo_integrale`, omesso da `riferimento` come da
  istruzione generale del censimento.
- REQ-7.14.3-11: EXAMPLE e NOTE 4 (integrazione del registro fornitori con
  altri registri di conformità, es. GDPR) sono sostanziali e mantenuti in
  `testo_integrale`; negli altri REQ di 7.14.2/7.14.3 le NOTE che rinviano
  a singole clausole di ISO/IEC 27002:2022 per mera guidance bibliografica
  (NOTE 1/NOTE 2/NOTE 3/NOTE 5 di REQ-7.14.2-13/14/15 e REQ-7.14.3-03/10/12)
  sono state omesse da `testo_integrale`, salvo la parte sostanziale di
  NOTE 4 in REQ-7.14.2-15 (spiegazione del modello di responsabilità
  condivisa nei servizi cloud) e di NOTE 1 in REQ-7.14.3-03 (applicabilità
  esplicita ai fornitori cloud), entrambe mantenute perché aggiungono
  contenuto interpretativo sostanziale oltre il mero rinvio bibliografico.

RELAZIONI: vuoto in questa fase per vincolo esplicito dell'incarico (nessuna
relazione cross-capitolo/cross-fonte durante l'import granulare parallelo;
il collegamento cross-fonte è demandato alla Fase 6/ADR-0009 della sessione
principale).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "REQ-7.10-01",
        "testo": "Il TSP deve registrare e mantenere accessibili, per un periodo di tempo adeguato, incluso dopo la cessazione delle proprie attività, tutte le informazioni rilevanti relative ai dati emessi e ricevuti dal TSP, in particolare ai fini di fornire prova in procedimenti legali e di assicurare la continuità del servizio.",
        "testo_integrale": "REQ-7.10-01: The TSP shall record and keep accessible for an appropriate period of time, including after the activities of the TSP have ceased, all relevant information concerning data issued and received by the TSP, in particular, for the purpose of providing evidence in legal proceedings and for the purpose of ensuring continuity of the service.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.10-02",
        "testo": "Deve essere mantenuta la riservatezza e l'integrità delle registrazioni correnti e archiviate relative al funzionamento dei servizi.",
        "testo_integrale": "REQ-7.10-02: The confidentiality and integrity of current and archived records concerning operation of services shall be maintained.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.10-03",
        "testo": "Le registrazioni relative al funzionamento dei servizi devono essere archiviate in modo completo e riservato, in conformità alle prassi commerciali dichiarate.",
        "testo_integrale": "REQ-7.10-03: Records concerning the operation of services shall be completely and confidentially archived in accordance with disclosed business practices.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.10-04",
        "testo": "Le registrazioni relative al funzionamento dei servizi devono essere rese disponibili, se richiesto, ai fini di fornire prova del corretto funzionamento dei servizi in procedimenti legali.",
        "testo_integrale": "REQ-7.10-04: Records concerning the operation of services shall be made available if required for the purposes of providing evidence of the correct operation of the services for the purpose of legal proceedings.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.10-05",
        "testo": "Deve essere registrato l'orario preciso degli eventi ambientali, di gestione delle chiavi e di sincronizzazione dell'orologio significativi del TSP.",
        "testo_integrale": "REQ-7.10-05: The precise time of significant TSP's environmental, key management and clock synchronization events shall be recorded.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.10-06",
        "testo": "L'orario usato per registrare gli eventi richiesti nel log di audit deve essere sincronizzato con l'UTC almeno una volta al giorno.",
        "testo_integrale": "REQ-7.10-06: The time used to record events as required in the audit log shall be synchronized with UTC at least once a day.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.10-07",
        "testo": "Le registrazioni relative ai servizi devono essere conservate per un periodo di tempo adeguato a fornire la necessaria prova legale, come comunicato nei termini e condizioni del TSP.",
        "testo_integrale": "REQ-7.10-07: Records concerning services shall be held for a period of time as appropriate for providing necessary legal evidence and as notified in the TSP's terms and conditions (see clause 6.2).",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.10-08",
        "testo": "Gli eventi devono essere registrati in modo che non possano essere facilmente cancellati o distrutti (salvo trasferimento affidabile su supporto a lungo termine) per il periodo di tempo in cui è richiesto conservarli.",
        "testo_integrale": "REQ-7.10-08: The events shall be logged in a way that they cannot be easily deleted or destroyed (except if reliably transferred to long-term media) within the period of time that they are required to be held. EXAMPLE: This can be achieved, for example, through the use of write-only media, a record of each removable storage media used and the use of off-site backup or by parallel storage of the information at several (e.g. 2 or 3) independent sites.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.11.1-01",
        "testo": "Il TSP deve mantenere copie di backup dei dati e fornire risorse disponibili sufficienti, incluse strutture, sistemi di rete e informativi e personale, per assicurare un adeguato livello di ridondanza in conformità alla valutazione del rischio e al piano di continuità operativa.",
        "testo_integrale": "REQ-7.11.1-01: The TSP shall maintain backup copies of data and provide sufficient available resources, including facilities, network and information systems and staff, to ensure an appropriate level of redundancy in accordance with risk assessment and business continuity plan.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.11-1-02",
        "testo": "In caso di disastro, incluso il compromesso di una chiave privata di firma o di un'altra credenziale del TSP, le operazioni devono essere ripristinate entro il termine stabilito nel piano di continuità, dopo aver affrontato con misure correttive adeguate ogni causa del disastro che possa ripetersi (es. una vulnerabilità di sicurezza). Altre situazioni di disastro includono il guasto di componenti critici del sistema affidabile del TSP, incluso hardware e software.",
        "testo_integrale": "REQ-7.11-1-02: In the event of a disaster, including compromise of a private signing key or compromise of some other credential of the TSP, operations shall be restored within the delay established in the continuity plan, having addressed any cause for the disaster which may recur (e.g. a security vulnerability) with appropriate remediation measures. NOTE 2: Other disaster situations include failure of critical components of a TSP's trustworthy system, including hardware and software.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.11.1-03",
        "testo": "Sulla base dei risultati della valutazione del rischio e del piano di continuità operativa, il TSP deve assicurare una disponibilità sufficiente di risorse mediante almeno una ridondanza parziale di: a) sistemi di rete e informativi; b) beni, incluse strutture, apparecchiature e forniture; c) personale con la responsabilità, autorità e competenza necessarie; d) canali di comunicazione appropriati.",
        "testo_integrale": "REQ-7.11.1-03: Based on the results of the risk assessment and the business continuity plan, the TSP shall ensure sufficient availability of resources by at least partial redundancy of the following: a) network and information systems; b) assets, including facilities, equipment and supplies; c) personnel with the necessary responsibility, authority and competence; d) appropriate communication channels.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.11.1-04",
        "testo": "Il TSP deve documentare i risultati dei test e, ove necessario, adottare azioni correttive.",
        "testo_integrale": "REQ-7.11.1-04: The TSP shall document the results of the tests and, where needed, take corrective action.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.11.2-01",
        "testo": "Il TSP deve mantenere un piano di backup e aggiornarlo regolarmente.",
        "testo_integrale": "REQ-7.11.2-01: The TSP shall maintain backup plan and update it regularly.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.11.2-02",
        "testo": "Il TSP deve definire i piani di backup tenendo conto almeno di quanto segue: a) tempi di recupero; b) garanzia di completezza e accuratezza delle copie di backup, inclusi i dati di configurazione e le informazioni memorizzate in ambiente di cloud service; c) conservazione delle copie di backup in una o più ubicazioni sicure, esterne alla rete del sistema di cui è stato fatto il backup e a distanza sufficiente da sfuggire a danni derivanti da un disastro presso il sito principale; d) controlli fisici e logici appropriati per le copie di backup in conformità al loro livello di classificazione delle informazioni; e) processi per il ripristino delle informazioni dalle copie di backup, incluse le procedure di approvazione; f) periodi di conservazione basati sui requisiti aziendali e normativi.",
        "testo_integrale": "REQ-7.11.2-02: The TSP shall define backup plans taking into account at least the following: a) recovery times; b) assurance of the backup copies' completeness and accuracy, including configuration data and information stored in cloud service environment; c) storage of backup copies at a safe location or locations, which are outside the network of the system backed up and are at sufficient distance to escape any damage from a disaster at the main site; d) appropriate physical and logical controls for backup copies in accordance with their information classification level; and e) processes for restoring information from backup copies, including approval processes; and f) retention periods based on business and regulatory requirements.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.11.2-03",
        "testo": "Il TSP deve effettuare un controllo di integrità regolare sulle copie di backup.",
        "testo_integrale": "REQ-7.11.2-03: The TSP shall perform regular integrity check on the backup copies.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.11.2-04",
        "testo": "Il TSP deve testare, a intervalli pianificati, il ripristino delle copie di backup e delle ridondanze, adottando azioni correttive in caso di riscontri; i risultati di tali test devono essere documentati.",
        "testo_integrale": "REQ-7.11.2-04: The TSP shall test at planed intervals the recovery of backup copies and redundancies and shall take corrective actions in case of findings. The results of these tests shall be documented.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "PRO-7.11.2-05",
        "testo": "Ove appropriato, il TSP deve assicurare che il monitoraggio e l'adeguamento delle risorse, incluse strutture, sistemi e personale, sia debitamente informato dai requisiti di backup e ridondanza.",
        "testo_integrale": "PRO-7.11.2-05: Where appropriate, the TSP shall ensure that monitoring and adjustment of resources, including facilities, systems and personnel, is duly informed by backup and redundancy requirements.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.11.2-06",
        "testo": "Il TSP deve effettuare test periodici del ripristino delle copie di backup e delle ridondanze, per assicurare che, in condizioni di ripristino, esse siano affidabili e coprano le copie, i processi e le competenze necessari a un recupero efficace.",
        "testo_integrale": "REQ-7.11.2-06: The TSP shall carry out regular testing of the recovery of backup copies and redundancies to ensure that, in recovery conditions, they can be relied upon and cover the copies, processes and knowledge to perform an effective recovery.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.11.3-01",
        "testo": "Il TSP deve istituire processi di gestione delle crisi che affrontino almeno: a) ruoli e responsabilità per il personale e, ove appropriato, per fornitori e prestatori di servizi, specificando l'assegnazione dei ruoli nelle situazioni di crisi, inclusi i passi specifici da seguire; b) mezzi di comunicazione appropriati tra il TSP e le autorità competenti rilevanti, incluse sia le comunicazioni obbligatorie, quali le segnalazioni di incidente e le relative tempistiche, sia le comunicazioni non obbligatorie; c) applicazione di controlli appropriati per mantenere la sicurezza dei sistemi di rete e informativi nelle situazioni di crisi.",
        "testo_integrale": "REQ-7.11.3-01: The TSP shall establish processes for crisis management addressing at least: a) roles and responsibilities for personnel and, where appropriate, suppliers and service providers, specifying the allocation of roles in crisis situations, including specific steps to follow; b) appropriate communication means between the TSP and relevant competent authorities, including both obligatory communications, such as incident reports and related timelines, and non-obligatory communications; and c) application of appropriate controls to maintain network and information system security in crisis situations.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.11.3-02",
        "testo": "Il TSP deve implementare un processo per gestire e utilizzare le informazioni ricevute dal CSIRT nazionale o, ove applicabile, dalle autorità competenti, relative a incidenti, vulnerabilità, minacce o possibili misure di mitigazione.",
        "testo_integrale": "REQ-7.11.3-02: The TSP shall implement a process for managing and making use of information received from National CSIRT or, where applicable, competent authorities, concerning incidents, vulnerabilities, threats or possible mitigation measures.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.11.3-03",
        "testo": "Il TSP deve testare e rivedere il proprio piano di gestione delle crisi a intervalli pianificati.",
        "testo_integrale": "REQ-7.11.3-03: The TSP shall test and review its crisis management plan at planned intervals.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.11.3-04",
        "testo": "Il TSP deve inoltre aggiornare il piano di gestione delle crisi, ove appropriato, a seguito di incidenti significativi o di modifiche significative alle operazioni o ai rischi.",
        "testo_integrale": "REQ-7.11.3-04: Additionally, the TSP shall update the crisis management plan, where appropriate, following significant incidents or significant changes to operations or risks.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.12-01",
        "testo": "Le potenziali interruzioni a danno di sottoscrittori e parti facenti affidamento devono essere ridotte al minimo a seguito della cessazione dei servizi del TSP, e in particolare deve essere assicurata la continua manutenzione delle informazioni necessarie a verificare la correttezza dei servizi fiduciari.",
        "testo_integrale": "REQ-7.12-01: Potential disruptions to subscribers and relying parties shall be minimized as a result of the cessation of the TSP's services, and in particular continued maintenance of information required to verify the correctness of trust services shall be provided.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.12-02",
        "testo": "Il TSP deve disporre di un piano di cessazione aggiornato.",
        "testo_integrale": "REQ-7.12-02: The TSP shall have an up-to-date termination plan.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.12-03",
        "testo": "Prima di cessare i propri servizi, il TSP deve informare della cessazione: tutti i sottoscrittori e le altre entità con cui il TSP ha accordi o altre forme di rapporto stabilito, tra cui le parti facenti affidamento, altri TSP e le autorità rilevanti quali gli organismi di vigilanza.",
        "testo_integrale": "REQ-7.12-03: Before the TSP terminates its services, the TSP shall inform the following of the termination: all subscribers and other entities with which the TSP has agreements or other form of established relations, among which relying parties, TSPs and relevant authorities such as supervisory bodies.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.12-04",
        "testo": "Prima di cessare i propri servizi, il TSP deve rendere disponibile alle altre parti facenti affidamento l'informazione relativa alla cessazione.",
        "testo_integrale": "REQ-7.12-04: Before the TSP terminates its services, the TSP shall make the information of the termination available to other relying parties.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.12-05",
        "testo": "Prima di cessare i propri servizi, il TSP deve revocare l'autorizzazione di tutti i subappaltatori ad agire per proprio conto nello svolgimento di funzioni relative al processo di emissione dei token di servizio fiduciario.",
        "testo_integrale": "REQ-7.12-05: Before the TSP terminates its services, the TSP shall terminate authorization of all subcontractors to act on behalf of the TSP in carrying out any functions relating to the process of issuing trust service tokens.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.12-06",
        "testo": "Prima di cessare i propri servizi, il TSP deve trasferire a una parte affidabile gli obblighi di mantenimento di tutte le informazioni necessarie a fornire prova dell'operatività del TSP per un periodo ragionevole, salvo dimostri di non detenere tali informazioni.",
        "testo_integrale": "REQ-7.12-06: Before the TSP terminates its services, the TSP shall transfer obligations to a reliable party for maintaining all information necessary to provide evidence of the operation of the TSP for a reasonable period, unless it can be demonstrated that the TSP does not hold any such information.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.12-07",
        "testo": "Prima di cessare i propri servizi, le chiavi private del TSP, incluse le copie di backup, devono essere distrutte o ritirate dall'uso, in modo tale che non possano essere recuperate.",
        "testo_integrale": "REQ-7.12-07: Before the TSP terminates its services, the TSP's private keys, including backup copies, shall be destroyed, or withdrawn from use, in a manner such that the private keys cannot be retrieved.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.12-08",
        "testo": "Prima di cessare i propri servizi, ove possibile il TSP dovrebbe adottare accordi per trasferire l'erogazione dei servizi fiduciari ai propri clienti esistenti a un altro TSP.",
        "testo_integrale": "REQ-7.12-08: Before the TSP terminates its services, where possible TSP should make arrangements to transfer provision of trust services for its existing customers to another TSP.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.12-09",
        "testo": "Il TSP deve disporre di un accordo per coprire i costi necessari a soddisfare questi requisiti minimi nel caso in cui il TSP fallisca o non sia per altri motivi in grado di coprire i costi da sé, per quanto possibile nei limiti della legislazione applicabile in materia fallimentare.",
        "testo_integrale": "REQ-7.12-09: The TSP shall have an arrangement to cover the costs to fulfil these minimum requirements in case the TSP becomes bankrupt or for other reasons is unable to cover the costs by itself, as far as possible within the constraints of applicable legislation regarding bankruptcy.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.12-10",
        "testo": "Il TSP deve indicare nelle proprie prassi le disposizioni adottate per la cessazione del servizio, che devono includere: a) la notifica alle entità interessate; b) ove applicabile, il trasferimento degli obblighi del TSP ad altre parti.",
        "testo_integrale": "REQ-7.12-10: The TSP shall state in its practices the provisions made for termination of service. This shall include: a) notification of affected entities; and b) where applicable, transferring the TSP's obligations to other parties.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.12-11",
        "testo": "Il TSP deve mantenere o trasferire a una parte affidabile i propri obblighi di rendere disponibile la propria chiave pubblica o i propri token di servizio fiduciario alle parti facenti affidamento per un periodo ragionevole.",
        "testo_integrale": "REQ-7.12-11: The TSP shall maintain or transfer to a reliable party its obligations to make available its public key or its trust service tokens to relying parties for a reasonable period.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.13-01",
        "testo": "Il TSP deve assicurare di operare in modo legale e affidabile.",
        "testo_integrale": "REQ-7.13-01: The TSP shall ensure that it operates in a legal and trustworthy manner.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.13-02",
        "testo": "Il TSP deve fornire prova di come soddisfa i requisiti legali applicabili.",
        "testo_integrale": "REQ-7.13-02: The TSP shall provide evidence on how it meets the applicable legal requirements.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.13-03",
        "testo": "I servizi fiduciari erogati e i prodotti per l'utente finale utilizzati nell'erogazione di tali servizi devono essere resi accessibili alle persone con disabilità, ove possibile.",
        "testo_integrale": "REQ-7.13-03: Trust services provided and end user products used in the provision of those services shall be made accessible for persons with disabilities, where feasible.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.13-04",
        "testo": "Dovrebbero essere tenuti in considerazione gli standard applicabili in materia di accessibilità, come ETSI EN 301 549.",
        "testo_integrale": "REQ-7.13-04: Applicable standards on accessibility such as ETSI EN 301 549 [i.6] should be taken into account.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.13-05",
        "testo": "Devono essere adottate misure tecniche e organizzative appropriate contro il trattamento non autorizzato o illecito dei dati personali e contro la perdita, distruzione o danneggiamento accidentali dei dati personali. A tal riguardo, l'autenticazione per un servizio online riguarda il trattamento solo dei dati identificativi adeguati, pertinenti e non eccessivi per concedere l'accesso a tale servizio online.",
        "testo_integrale": "REQ-7.13-05: Appropriate technical and organizational measures shall be taken against unauthorized or unlawful processing of personal data and against accidental loss or destruction of, or damage to, personal data. NOTE 1: TSPs operating in Europe are required to ensure that personal data is processed in accordance with Regulation (EU) 2016/679 [i.8]. In this respect, authentication for a service online concerns processing of only those identification data which are adequate, relevant and not excessive to grant access to that service online.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.13-06",
        "testo": "Il TSP deve implementare un sistema efficace di reporting sulla conformità: a) appropriato alle proprie strutture, ambienti operativi e panorami di minacce; b) capace di fornire agli organi di gestione una visione informata dello stato attuale della gestione dei rischi del TSP.",
        "testo_integrale": "REQ-7.13-06: The TSP shall put in place an effective compliance reporting system: a) appropriate to their structures, operating environments and threat landscapes. b) capable to provide to the management bodies an informed view of the current state of the TSP's management of risks.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.1-01",
        "testo": "Il TSP deve stabilire, implementare e applicare una politica di sicurezza della supply chain che disciplini i rapporti con i propri fornitori diretti e prestatori di servizi al fine di mitigare i rischi individuati per la sicurezza dei sistemi di rete e informativi. Nella politica di sicurezza della supply chain, il TSP deve identificare il proprio ruolo nella supply chain e comunicarlo ai propri fornitori diretti e prestatori di servizi.",
        "testo_integrale": "REQ-7.14.1-01: The TSP shall establish, implement and apply a supply chain security policy which governs the relations with their direct suppliers and service providers in order to mitigate the identified risks to the security of network and information systems. In the supply chain security policy, the TSP shall identify their role in the supply chain and communicate it to their direct suppliers and service providers.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.1-02",
        "testo": "Il TSP deve definire, documentare e implementare processi e procedure per gestire i rischi di sicurezza delle informazioni associati all'uso di prodotti o servizi dei fornitori, inclusi i criteri per selezionare e contrattualizzare fornitori e prestatori di servizi.",
        "testo_integrale": "REQ-7.14.1-02: The TSP shall define, document and implement processes and procedures to manage the information security risks associated with the use of supplier's products or services, including criteria to select and contract suppliers and service providers.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.1-03",
        "testo": "La politica di supply chain deve identificare e comunicare il ruolo del TSP nella supply chain.",
        "testo_integrale": "REQ-7.14.1-03: The supply chain policy shall identify and communicate the TSP's role in the supply chain.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.1-04",
        "testo": "La politica di supply chain deve definire i criteri per selezionare e contrattualizzare fornitori o prestatori di servizi, che devono includere: a) le pratiche di cybersecurity dei fornitori e prestatori di servizi, incluse le loro procedure di sviluppo sicuro; b) la capacità del fornitore o prestatore di servizi di soddisfare le specifiche di cybersecurity, i rischi e i livelli di classificazione dei servizi, sistemi o prodotti del TSP forniti dal fornitore o prestatore di servizi; c) la qualità complessiva e la resilienza dei prodotti e servizi ICT e le misure di gestione del rischio di cybersecurity in essi incorporate, inclusi i rischi e il livello di classificazione dei prodotti e servizi ICT; d) la capacità del TSP di diversificare le fonti di approvvigionamento e di limitare il vendor lock-in; e) i risultati delle valutazioni coordinate del rischio di sicurezza delle supply chain critiche.",
        "testo_integrale": "REQ-7.14.1-04: The supply chain policy shall define criteria for selecting and contracting suppliers or service providers. Criteria shall include: a) the cybersecurity practices of the suppliers and service providers, including their secure development procedures; b) the ability of the supplier or service provider to meet the cybersecurity specifications, risks and classification levels of the TSP's services, systems or products delivered by the supplier or service provider; c) the overall quality and resilience of ICT products and ICT services and the cybersecurity risk-management measures embedded in them, including the risks and classification level of the ICT products and ICT services; d) the ability of the TSP to diversify sources of supply and to limit vendor lock-in; and e) the results of the coordinated security risk assessments of critical supply chains.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.1-05",
        "testo": "Il TSP deve rivedere la politica di sicurezza della supply chain, e monitorare, valutare e, ove necessario, intervenire sui cambiamenti nelle pratiche di cybersecurity di fornitori e prestatori di servizi, a intervalli pianificati e quando si verificano cambiamenti significativi alle operazioni o ai rischi, o incidenti significativi relativi alla fornitura di servizi ICT o con impatto sulla sicurezza dei prodotti ICT dei fornitori e prestatori di servizi.",
        "testo_integrale": "REQ-7.14.1-05: The TSP shall review the supply chain security policy, and monitor, evaluate and, where necessary, act upon changes in the cybersecurity practices of suppliers and service providers, at planned intervals and when significant changes to operations or risks or significant incidents related to the provision of ICT services or having impact on the security of the ICT products from suppliers and service providers occur.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.1-06",
        "testo": "Per monitorare i cambiamenti nelle pratiche di cybersecurity, il TSP deve: a) monitorare regolarmente i report sull'implementazione degli accordi sul livello di servizio, ove applicabile; b) rivedere gli incidenti relativi a prodotti e servizi ICT dei fornitori e prestatori di servizi; c) valutare la necessità di revisioni non pianificate e documentare i riscontri in modo comprensibile; d) analizzare i rischi presentati dai cambiamenti relativi ai prodotti e servizi ICT dei fornitori e prestatori di servizi e, ove appropriato, adottare tempestivamente misure di mitigazione.",
        "testo_integrale": "REQ-7.14.1-06: For monitoring changes in cybersecurity practices, the TSP shall: a) regularly monitor reports on the implementation of the service level agreements, where applicable; b) review incidents related to ICT products and ICT services from suppliers and service providers; c) assess the need for unscheduled reviews and document the findings in a comprehensible manner; d) analyse the risks presented by changes related to ICT products and ICT services from suppliers and service providers and, where appropriate, take mitigating measures in a timely manner.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-01",
        "testo": "Devono essere definiti e implementati processi e procedure per gestire i rischi di sicurezza delle informazioni associati alla supply chain di prodotti e servizi delle tecnologie dell'informazione e della comunicazione.",
        "testo_integrale": "REQ-7.14.2-01: Processes and procedures shall be defined and implemented to manage information security risks associated with the information and communication technologies products and services supply chain.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-02",
        "testo": "Il TSP deve definire i requisiti di sicurezza delle informazioni da applicare all'acquisizione di prodotti o servizi ICT.",
        "testo_integrale": "REQ-7.14.2-02: TSP shall define information security requirements to apply to ICT product or service acquisition.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-03",
        "testo": "Il TSP deve richiedere che i fornitori di servizi ICT propaghino i requisiti di sicurezza del TSP lungo tutta la supply chain qualora subappaltino parti del servizio ICT fornito al TSP.",
        "testo_integrale": "REQ-7.14.2-03: TSP shall require that ICT services suppliers propagate the TSP's security requirements throughout the supply chain if they sub-contract for parts of the ICT service provided to the TSP.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-04",
        "testo": "Il TSP deve richiedere che i fornitori di prodotti ICT propaghino pratiche di sicurezza appropriate lungo tutta la supply chain qualora tali prodotti includano componenti acquistate o acquisite da altri fornitori o entità.",
        "testo_integrale": "REQ-7.14.2-04: TSP shall require that ICT products suppliers propagate appropriate security practices throughout the supply chain if these products include components purchased or acquired from other suppliers or other entities.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-05",
        "testo": "Il TSP deve richiedere ai fornitori di prodotti ICT di fornire informazioni che descrivano i componenti software utilizzati nei prodotti.",
        "testo_integrale": "REQ-7.14.2-05: TSP shall request that ICT products suppliers provide information describing the software components used in products.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-06",
        "testo": "Il TSP deve richiedere ai fornitori di prodotti ICT di fornire informazioni che descrivano le funzioni di sicurezza implementate nel loro prodotto e la configurazione richiesta per il suo funzionamento sicuro.",
        "testo_integrale": "REQ-7.14.2-06: TSP shall request that ICT products suppliers provide information describing the implemented security functions of their product and the configuration required for its secure operation.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-07",
        "testo": "Il TSP deve implementare un processo di monitoraggio e metodi accettabili per validare che i prodotti e servizi ICT siano conformi ai requisiti di cybersecurity dichiarati.",
        "testo_integrale": "REQ-7.14.2-07: TSP shall implement a monitoring process and acceptable methods for validating ICT products and services conform to stated cybersecurity requirements.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-08",
        "testo": "Il TSP deve implementare un processo per identificare e documentare i componenti di prodotto o servizio critici per il mantenimento della funzionalità.",
        "testo_integrale": "REQ-7.14.2-08: TSP shall implement a process for identifying and documenting product or service components that are critical for maintaining functionality.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-09",
        "testo": "Il TSP deve ottenere garanzia che i componenti critici e la loro origine possano essere tracciati lungo tutta la supply chain.",
        "testo_integrale": "REQ-7.14.2-09: TSP shall obtain assurance that critical components and their origin can be traced throughout the supply chain.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-10",
        "testo": "Il TSP deve ottenere garanzia che i prodotti ICT consegnati funzionino come previsto, senza funzionalità inattese o indesiderate.",
        "testo_integrale": "REQ-7.14.2-10: TSP shall obtain assurance that the delivered ICT products are functioning as expected without any unexpected or unwanted features.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-11",
        "testo": "Il TSP deve implementare processi per assicurare che i componenti provenienti dai fornitori siano genuini e non alterati rispetto alla loro specifica.",
        "testo_integrale": "REQ-7.14.2-11: TSP shall implement processes to ensure that components from suppliers are genuine and unaltered from their specification.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-12",
        "testo": "Il TSP deve definire regole per la condivisione di informazioni riguardanti la supply chain ed eventuali problemi e compromissioni tra il TSP e i propri fornitori.",
        "testo_integrale": "REQ-7.14.2-12: TSP shall define rules for sharing of information regarding the supply chain and any potential issues and compromises among the TSP and its suppliers.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-13",
        "testo": "Il TSP deve implementare processi specifici per gestire il ciclo di vita e la disponibilità dei componenti ICT e i relativi rischi di sicurezza.",
        "testo_integrale": "REQ-7.14.2-13: TSP shall implement specific processes for managing ICT component life cycle and availability and associated security risks.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-14",
        "testo": "Il TSP deve monitorare, rivedere, valutare e gestire regolarmente i cambiamenti nelle pratiche di sicurezza delle informazioni dei fornitori e nell'erogazione del servizio.",
        "testo_integrale": "REQ-7.14.2-14: TSP shall regularly monitor, review, evaluate and manage change in supplier information security practices and service delivery.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.2-15",
        "testo": "Il TSP deve definire, implementare e comunicare a tutte le parti interessate rilevanti politiche specifiche sull'uso dei servizi cloud e su come il TSP intende gestire i rischi di sicurezza delle informazioni ad essi associati. L'uso dei servizi cloud comporta, secondo contratto, una responsabilità condivisa per la sicurezza delle informazioni e uno sforzo collaborativo tra il fornitore del servizio cloud e il TSP che agisce come cliente del servizio cloud; è essenziale che le responsabilità sia del fornitore del servizio cloud sia dell'organizzazione, in qualità di cliente del servizio cloud, siano definite e implementate in modo appropriato.",
        "testo_integrale": "REQ-7.14.2-15: The TSP shall define, implement and communicate to all relevant interested parties topic-specific policies on the use of cloud services and on how the TSP intends to manage information security risks associated with them. NOTE 4: The use of cloud services involves, as per contract, shared responsibility for information security and collaborative effort between the cloud service provider and the TSP acting as the cloud service provider customer. It is essential that the responsibilities for both the cloud service provider and the organization, acting as the cloud service customer, are defined and implemented appropriately.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.3-01",
        "testo": "Quando il TSP si avvale di altre parti, inclusi i fornitori di componenti di servizio fiduciario, per fornire parti del proprio servizio tramite subappalto, esternalizzazione o altri accordi con terzi, deve mantenere la responsabilità complessiva per la conformità con la politica di supply chain, la propria politica di sicurezza delle informazioni e i requisiti definiti nella politica di servizio fiduciario.",
        "testo_integrale": "REQ-7.14.3-01 [CONDITIONAL]: When the TSP makes use of other parties, including trust service component providers, to provide parts of its service through subcontracting, outsourcing or other third party arrangements, it shall maintain overall responsibility for conformance with the supply chain policy, its information security policy and the requirements defined in the trust service policy.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica quando il TSP si avvale di altre parti (inclusi fornitori di componenti di servizio fiduciario) per fornire parti del proprio servizio tramite subappalto, esternalizzazione o altri accordi con terzi",
    },
    {
        "riferimento": "REQ-7.14.3-02",
        "testo": "Il TSP deve definire la responsabilità degli esternalizzatori e assicurare che questi siano vincolati a implementare tutti i controlli richiesti dal TSP.",
        "testo_integrale": "REQ-7.14.3-02: The TSP shall define the outsourcers' liability and ensure that outsourcers are bound to implement any controls required by the TSP.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.3-03",
        "testo": "Tali processi e procedure devono includere: a) quelli da implementare a cura del TSP; b) quelli che il TSP richiede al fornitore di implementare per l'avvio dell'uso dei prodotti o servizi del fornitore; c) quelli che il TSP richiede al fornitore di implementare per la cessazione dell'uso dei prodotti e servizi del fornitore. Ciò si applica anche all'uso da parte del TSP di risorse dei fornitori di servizi cloud.",
        "testo_integrale": "REQ-7.14.3-03: These processes and procedures shall include: a) those to be implemented by the TSP; b) those the TSP requires the supplier to implement for the commencement of use of a supplier's products or services; and c) those the TSP requires the supplier to implement for the termination of use of a supplier's products and services. NOTE 1: This applies to TSP's use of resources of cloud service providers.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.3-04",
        "testo": "Il TSP deve disporre di un accordo documentato e di un rapporto contrattuale quando l'erogazione dei servizi comporta subappalto, esternalizzazione o altri accordi con terzi, per assicurare una chiara comprensione tra il TSP e il fornitore riguardo agli obblighi di entrambe le parti di soddisfare i requisiti di sicurezza delle informazioni rilevanti.",
        "testo_integrale": "REQ-7.14.3-04: The TSP shall have a documented agreement and contractual relationship in place where the provisioning of services involves subcontracting, outsourcing or other third party arrangements to ensure that there is clear understanding between the TSP and the supplier regarding both parties' obligations to fulfil relevant information security requirements.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.3-05",
        "testo": "Quando il TSP si avvale di una componente di servizio fiduciario fornita da un'altra parte, deve assicurare che l'uso dell'interfaccia della componente soddisfi i requisiti specificati dal fornitore della componente di servizio fiduciario.",
        "testo_integrale": "REQ-7.14.3-05 [CONDITIONAL]: When the TSP makes use of a trust service component provided by another party it shall ensure that the use of the component interface meets the requirements as specified by the trust service component provider.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica quando il TSP si avvale di una componente di servizio fiduciario fornita da un'altra parte",
    },
    {
        "riferimento": "REQ-7.14.3-06",
        "testo": "Quando il TSP si avvale di una componente di servizio fiduciario fornita da un'altra parte, deve assicurare che la sicurezza e la funzionalità richieste dalla componente di servizio fiduciario soddisfino i requisiti appropriati della politica e delle prassi applicabili.",
        "testo_integrale": "REQ-7.14.3-06 [CONDITIONAL]: When the TSP makes use of a trust service component provided by another party it shall ensure that the security and functionality required by the trust service component meet the appropriate requirements of the applicable policy and practices.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica quando il TSP si avvale di una componente di servizio fiduciario fornita da un'altra parte",
    },
    {
        "riferimento": "REQ-7.14.3-07",
        "testo": "Il TSP deve includere nei propri accordi di servizio 'accordi sul livello di servizio' (SLA) e/o meccanismi di audit che assicurino che i fornitori diretti e i prestatori di servizi, inclusi i fornitori di cloud computing, adottino misure di sicurezza appropriate che rispondano ai requisiti di sicurezza del TSP allineati alla sua valutazione del rischio.",
        "testo_integrale": "REQ-7.14.3-07: The TSP shall include in their services agreements \"Service level agreements\" and/or auditing mechanisms ensuring that direct suppliers and service providers, including cloud computing providers, take appropriate security measures addressing the TSP's security requirements aligned with the TSP's risk assessment.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.3-08",
        "testo": "La conformità alle politiche e ai requisiti di sicurezza del TSP deve essere presa in considerazione nel processo di selezione di qualsiasi fornitore diretto o prestatore di servizi, come parte del processo di approvvigionamento.",
        "testo_integrale": "REQ-7.14.3-08: Compliance with TSPs security policies and requirements shall be considered in the selection process of any direct supplier or service provider as part of the procurement process.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.3-09",
        "testo": "Le politiche e i requisiti di sicurezza applicabili del TSP devono essere inclusi nei contratti con i fornitori diretti o i prestatori di servizi.",
        "testo_integrale": "REQ-7.14.3-09: Applicable TSPs security policies and requirements and shall be included in contracts with direct suppliers or service providers.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.3-10",
        "testo": "Il TSP deve rivedere la politica di supply chain e monitorare, rivedere, valutare e gestire i cambiamenti nelle pratiche di cybersecurity dei fornitori diretti o prestatori di servizi a intervalli pianificati, almeno annualmente, o dopo un incidente relativo alla fornitura di servizi da parte di fornitori diretti o prestatori di servizi.",
        "testo_integrale": "REQ-7.14.3-10: The TSP shall review the supply chain policy and monitor, review, evaluate and manage changes in the cybersecurity practices of direct suppliers or service providers at planned intervals, at least annually, or after an incident related to the provision of services from direct suppliers or service providers.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.3-11",
        "testo": "Il TSP deve istituire e mantenere un registro dei fornitori e dei relativi accordi, per tracciare dove sono gestite e/o archiviate le informazioni del TSP (utile ad esempio per identificare dove le informazioni vengono scambiate). Tale registro potrebbe essere integrato con altri registri di conformità mantenuti dal TSP, come quelli richiesti ai sensi del GDPR per le attività di trattamento dei dati, purché tutte le informazioni richieste siano acquisite e prontamente accessibili.",
        "testo_integrale": "REQ-7.14.3-11: The TSP shall establish and maintain a register of suppliers and their agreements to track where the TSP information is managed and/or archived. EXAMPLE: This can help identify where information is exchanged. NOTE 4: This registry could be integrated with other compliance registries maintained by the TSP, such as those required under GDPR for data processing activities, provided all required information is captured and readily accessible.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.3-12",
        "testo": "Il TSP deve rivedere, convalidare e aggiornare regolarmente il proprio registro dei fornitori e dei relativi accordi, per assicurare che siano ancora validi, adeguati allo scopo e includano le clausole di sicurezza delle informazioni rilevanti.",
        "testo_integrale": "REQ-7.14.3-12: The TSP shall regularly review, validate and update its registry of suppliers and their agreements to ensure that they are still valid, fit for purpose, and include the relevant information security clauses.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.3-13",
        "testo": "Sulla base della politica di sicurezza della supply chain e tenendo conto dei risultati della valutazione del rischio, il TSP deve assicurare che i propri contratti con i fornitori e i prestatori di servizi specifichino, ove appropriato anche tramite accordi sul livello di servizio: a) i requisiti di cybersecurity per i fornitori o prestatori di servizi, inclusi i requisiti relativi alla sicurezza nell'acquisizione di servizi o prodotti ICT; b) i requisiti relativi a consapevolezza, competenze e formazione e, ove appropriato, alle certificazioni richieste al personale dei fornitori o prestatori di servizi; c) i requisiti relativi alla verifica dei precedenti del personale dei fornitori e dei prestatori di servizi; d) l'obbligo per fornitori e prestatori di servizi di notificare senza indebito ritardo al TSP gli incidenti che presentano un rischio per la sicurezza dei sistemi di rete e informativi del TSP; e) il diritto di audit o il diritto di ricevere i relativi report; f) l'obbligo per fornitori e prestatori di servizi di gestire le vulnerabilità che presentano un rischio per la sicurezza dei sistemi di rete e informativi del TSP; g) i requisiti relativi al subappalto e, ove il TSP lo consenta, i requisiti di cybersecurity per i subappaltatori in conformità ai requisiti di cybersecurity di cui alla lettera a); h) gli obblighi dei fornitori e prestatori di servizi alla cessazione del contratto, quali il recupero e lo smaltimento delle informazioni ottenute nell'esercizio dei propri compiti.",
        "testo_integrale": "REQ-7.14.3-13: Based on the supply chain security policy and taking into account the results of the risk assessment, the TSP shall ensure that their contracts with the suppliers and service providers specify, where appropriate through service level agreements, the following, where appropriate: a) cybersecurity requirements for the suppliers or service providers, including requirements regarding the security in acquisition of ICT services or ICT products; b) requirements regarding awareness, skills and training, and where appropriate certifications, required from the suppliers' or service providers' employees; c) requirements regarding the verification of the background of the suppliers' and service providers' employees; d) an obligation on suppliers and service providers to notify, without undue delay, the TSP of incidents that present a risk to the security of the network and information systems of the TSP; e) the right to audit or right to receive audit reports; f) an obligation on suppliers and service providers to handle vulnerabilities that present a risk to the security of the network and information systems of the TSP; g) requirements regarding subcontracting and, where the TSP allows subcontracting, cybersecurity requirements for subcontractors in accordance with the cybersecurity requirements referred to in point a); h) obligations on the suppliers and service providers at the termination of the contract, such as retrieval and disposal of the information obtained by the suppliers and service providers in the exercise of their tasks.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "REQ-7.14.3-14",
        "testo": "Il TSP deve mantenere e tenere aggiornato un registro dei propri fornitori diretti e prestatori di servizi, che includa: a) i punti di contatto per ciascun fornitore diretto e prestatore di servizi; b) un elenco dei prodotti ICT, dei servizi ICT e dei processi ICT forniti al TSP dal fornitore diretto o prestatore di servizi.",
        "testo_integrale": "REQ-7.14.3-14: The TSP shall maintain and keep up to date a registry of their direct suppliers and service providers, including: a) contact points for each direct supplier and service provider; b) a list of ICT products, ICT services, and ICT processes provided by the direct supplier or service provider to the TSP.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = []

INDICE_ARTICOLI_LOCALE = [
    "REQ-7.10-01",
    "REQ-7.10-02",
    "REQ-7.10-03",
    "REQ-7.10-04",
    "REQ-7.10-05",
    "REQ-7.10-06",
    "REQ-7.10-07",
    "REQ-7.10-08",
    "REQ-7.11.1-01",
    "REQ-7.11-1-02",
    "REQ-7.11.1-03",
    "REQ-7.11.1-04",
    "REQ-7.11.2-01",
    "REQ-7.11.2-02",
    "REQ-7.11.2-03",
    "REQ-7.11.2-04",
    "PRO-7.11.2-05",
    "REQ-7.11.2-06",
    "REQ-7.11.3-01",
    "REQ-7.11.3-02",
    "REQ-7.11.3-03",
    "REQ-7.11.3-04",
    "REQ-7.12-01",
    "REQ-7.12-02",
    "REQ-7.12-03",
    "REQ-7.12-04",
    "REQ-7.12-05",
    "REQ-7.12-06",
    "REQ-7.12-07",
    "REQ-7.12-08",
    "REQ-7.12-09",
    "REQ-7.12-10",
    "REQ-7.12-11",
    "REQ-7.13-01",
    "REQ-7.13-02",
    "REQ-7.13-03",
    "REQ-7.13-04",
    "REQ-7.13-05",
    "REQ-7.13-06",
    "REQ-7.14.1-01",
    "REQ-7.14.1-02",
    "REQ-7.14.1-03",
    "REQ-7.14.1-04",
    "REQ-7.14.1-05",
    "REQ-7.14.1-06",
    "REQ-7.14.2-01",
    "REQ-7.14.2-02",
    "REQ-7.14.2-03",
    "REQ-7.14.2-04",
    "REQ-7.14.2-05",
    "REQ-7.14.2-06",
    "REQ-7.14.2-07",
    "REQ-7.14.2-08",
    "REQ-7.14.2-09",
    "REQ-7.14.2-10",
    "REQ-7.14.2-11",
    "REQ-7.14.2-12",
    "REQ-7.14.2-13",
    "REQ-7.14.2-14",
    "REQ-7.14.2-15",
    "REQ-7.14.3-01",
    "REQ-7.14.3-02",
    "REQ-7.14.3-03",
    "REQ-7.14.3-04",
    "REQ-7.14.3-05",
    "REQ-7.14.3-06",
    "REQ-7.14.3-07",
    "REQ-7.14.3-08",
    "REQ-7.14.3-09",
    "REQ-7.14.3-10",
    "REQ-7.14.3-11",
    "REQ-7.14.3-12",
    "REQ-7.14.3-13",
    "REQ-7.14.3-14",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
