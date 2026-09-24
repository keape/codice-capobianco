"""Estrazione granulare ETSI EN 319 411-1 V1.5.1 (2025-04) — Capitolo 4:
clausole 6.4 (Facility, management and operational controls, 6.4.1-6.4.9),
6.5 (Technical security controls, 6.5.1-6.5.8), 6.6 (Certificate, CRL and
OCSP profiles, 6.6.1-6.6.3), 6.7 (Compliance audit and other assessment),
6.8 (Other business and legal matters, 6.8.1-6.8.16) e 6.9 (Other
provisions, 6.9.1-6.9.4).

Fonte 17 (assegnata dalla sessione principale, non ancora scritta in
Neo4j). Testo ufficiale: app/.source_cache/etsi_319_411_1/cap04.txt.

Modellazione (ADR-0007), stesso criterio già applicato a ETSI EN 319 401
(fonte 10) e ETSI TS 119 461 (fonte 9) per capitoli tecnici ETSI a
clausole/requisiti numerati con prefisso <SIGLA>-<clausola>-<NN>:

- Ogni id di requisito numerato che compare nel testo (**OVR-x.y-nn**,
  **GEN-...**, **REG-...**, **REV-...**, **SDP-...**, **DIS-...**,
  **CSS-...**) genera un nodo. Verbo "shall"/"shall not" -> Obbligo;
  "should"/"should not" e "may"/"may not" -> Principio, tipo_principio
  "altro" (raccomandazione o facoltà operativa su un requisito comunque
  numerato, non una definizione né una disposizione di scopo), stesso
  criterio usato in ETSI TS 119 461.
- Elenchi a lettere a)/b)/c)... SENZA prefisso di requisito proprio
  restano nello stesso nodo del requisito che li introduce (es.
  REG-6.4.5-04 a)-g); OVR-6.4.9-02 a)-c); GEN-6.5.1-12 a)-d); OVR-6.5.2-01
  a)-b); OVR-6.9.4-02 a)-f); GEN-6.6.1-02, tre alternative). Alcuni di
  questi elenchi (GEN-6.5.1-13A, tabella di OVR-6.4.6-01) sono stati
  estratti dal PDF originale con lettere di punteggiatura mancanti o
  spezzate su un'interruzione di pagina (`***ETSI***` / `<!-- Page N -->`
  nel testo grezzo): il contenuto testuale integrale è stato preservato
  parola per parola, riformattando solo l'impaginazione della lista
  (rimozione delle etichette a)/b)/... corrotte dall'estrazione, nessuna
  perdita di contenuto — non è un'elisione ai sensi di ADR-0010).
- **id numerati marcati "Void."/"Void" senza alcun contenuto proprio oltre
  il rinvio strutturale** (OVR-6.4.3-01, GEN-6.4.3-03, GEN-6.4.5-07,
  OVR-6.4.8-14, OVR-6.5.5-01, OVR-6.5.6-03, OVR-6.8.6-03, OVR-6.9.2-02,
  OVR-6.9.2-02A, OVR-6.9.2-03, OVR-6.9.2-04, OVR-6.9.4-04) -> NESSUN nodo,
  stesso trattamento delle voci "Void" già usato in ETSI EN 319 401/TS 119
  461 (non generano un item di indice: la numerazione stessa del documento
  li salta). Eccezione: **OVR-6.8.6-01** è marcato "Void." ma porta due
  NOTE con contenuto interpretativo sostanziale (responsabilità del TSP
  anche se le funzioni sono esternalizzate; estensione di OVR-6.4.1-01 e
  OVR-6.9.1-01 al rapporto con i "trust service component provider") ->
  qui il "Void" NON è vuoto di contenuto, quindi genera un nodo Principio
  "altro" (a differenza delle voci Void realmente prive di seguito).
- **Sottoclausole titolate senza alcun requisito numerato** (6.4.7 "Key
  changeover": "No policy requirement."; 6.5.8 "Timestamping": rinvio a
  EN 319 421; 6.7 "Compliance audit...": rinvio a EN 319 403; 6.8.1, 6.8.3,
  6.8.5, 6.8.7, 6.8.8, 6.8.9, 6.8.10, 6.8.11, 6.8.12, 6.8.14, 6.8.16 di
  "Other business and legal matters", tutte "No policy requirement."/
  rinvio/fuori scopo) -> 1 nodo Principio "altro" a testa di clausola
  (`riferimento` = "clausola 6.X.Y"), per istruzione esplicita di
  assegnazione (copertura completa ADR-0007 anche per le clausole prive di
  contenuto prescrittivo proprio, non solo quelle con un requisito
  numerato "shall apply" verso EN 319 401).
- **Requisiti che si limitano a rendere applicabile un'intera clausola di
  EN 319 401 ("The requirement(s) ... shall apply")** restano invece
  Obbligo (non Principio): "shall apply" è di per sé un contenuto
  prescrittivo autonomo (rende vincolante nel presente documento quanto
  previsto altrove), distinto dalle sottoclausole sopra che non hanno
  alcun verbo prescrittivo, solo "No policy requirement."/rinvio
  informativo.
- NOTE/EXAMPLE annesse a un requisito: assorbite in `testo_integrale`
  quando aggiungono contenuto interpretativo/di eccezione sostanziale
  (es. NOTE 1 su CSS-6.6.3-01A sui rischi della scelta di non-check;
  NOTE 3 su GEN-6.5.2-13 sull'ambito della distruzione delle chiavi; NOTE
  sotto OVR-6.4.8-09/OVR-6.4.9-04); omesse quando sono puro rimando
  bibliografico senza contenuto proprio (NOTE su OVR-6.4.5-01 e in testa a
  6.4.6, entrambe mero rimando a ETSI TS 119 511; EXAMPLE su OVR-6.5.5-07 e
  OVR-6.9.2-01C, mera esemplificazione priva di condizione normativa
  aggiuntiva) — quando omesse, il resto del testo è scritto come se la
  NOTE non ci fosse, mai con marcatori di elisione (ADR-0010).
- Frasi di transizione puramente strutturali ("In addition the following
  particular requirements apply:", label di sottosezione come "CA key
  compromise:", "Algorithm compromise:", "In the case of compromise as a
  minimum:") non generano contenuto proprio e non sono riportate: sono
  scaffolding editoriale del documento, non testo normativo.
- Marcature tra parentesi quadre ([CONDITIONAL], [CHOICE], [WEB], [NCP],
  [NCP+]) mantenute in `testo_integrale`, `condizione_applicabilita`
  valorizzata con sintesi breve, marcatura omessa dal solo `riferimento`
  (per le condizioni implicite senza marcatura esplicita, es. "If the CA
  generates the subject's keys" già dentro SDP-6.5.1-17..25 che sono
  comunque etichettate [CONDITIONAL] nel testo, o le clausole
  "Should any of the algorithms... become insufficient" di OVR-6.4.8-15/16
  che NON portano l'etichetta esplicita: qui la condizione resta descritta
  solo dentro `testo`/`testo_integrale`, senza valorizzare il campo
  dedicato, per applicare la marcatura solo dove il testo la rende
  esplicita con la propria etichetta quadra).
- tipo_obbligo, per assegnazione di lavoro: "tecnico/sicurezza" per tutti
  gli Obbligo di 6.4/6.5/6.6 (controlli operativi, di sicurezza tecnica e
  profili di certificato/CRL/OCSP); "organizzativo" per gli Obbligo di
  6.8/6.9 (materie commerciali/legali e disposizioni organizzative) quando
  il nodo ha un contenuto prescrittivo proprio (anche se di mero rinvio
  "shall apply"), non quando è solo Principio di rinvio/void.
- Categoria soggetto: default "QTSP/gestore" (obbligato) per ogni Obbligo,
  essendo il TSP l'attore quasi universale di questo capitolo. Aggiunto un
  soggetto "destinatario" esplicito solo dove il testo nomina
  espressamente il beneficiario di un obbligo informativo/di
  riservatezza: "Utente/titolare" per REG-6.4.5-05 (riservatezza del
  subject) e per la parte di OVR-6.8.4-02/OVR-6.4.8-11/13/15/16 relativa a
  subscriber/subject; "Terzi affidanti/pubblico" per la parte delle stesse
  righe relativa a relying party/pubblico.
- RELAZIONI resta vuoto per vincolo di fase (né interno al capitolo né
  cross-capitolo/cross-fonte, demandato a ADR-0009/cura editoriale
  successiva), anche per i numerosi rinvii letterali a requisiti di ETSI
  EN 319 401 (es. "REQ-7.4-02X to REQ-7.4-12X") o ad altre clausole dello
  stesso capitolo (es. "see clause 6.4.4"): riportati solo nel testo, mai
  come arco.

Dubbi di modellazione aperti per revisione umana:
- OVR-6.8.6-01 (Void con due NOTE sostanziali) è stato modellato come
  Principio "altro" anziché escluso come le altre voci Void, in deroga al
  criterio generale "Void senza contenuto = nessun nodo": è l'unico caso
  in questo capitolo in cui un id "Void" porta comunque testo normativo
  interpretativo. Verificare in revisione se preferibile fonderlo con
  OVR-6.8.6-02 invece di un nodo a sé.
- GEN-6.5.1-13A: la lista lettera del report di key ceremony risulta
  spezzata/duplicata nel testo grezzo estratto dal PDF a causa di
  un'interruzione di pagina; il contenuto è stato ricomposto in prosa
  continua preservando ogni singola voce elencata, senza inventare né
  omettere alcuna lettera. Verificare contro il PDF originale se
  disponibile.
"""

SOGGETTO_QTSP = [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}]

RIGHE_OBBLIGHI: list[dict] = [
    # ---- 6.4.1 General ----
    {
        "riferimento": "Parte 1: OVR-6.4.1-01",
        "testo": "Si applicano i requisiti delle clausole 5, 6.3 e 7.3 di ETSI EN 319 401.",
        "testo_integrale": "6.4.1 General — OVR-6.4.1-01: The requirements identified in ETSI EN 319 401 [9], clauses 5, 6.3 and 7.3, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.4.2 Physical security controls ----
    {
        "riferimento": "Parte 1: OVR-6.4.2-01",
        "testo": "Si applica il requisito della clausola 7.6 di ETSI EN 319 401.",
        "testo_integrale": "6.4.2 Physical security controls — OVR-6.4.2-01: The requirements identified in ETSI EN 319 401 [9], clause 7.6, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.2-02",
        "testo": "Le strutture per la generazione dei certificati e la gestione delle revoche devono operare in un ambiente che le protegga fisicamente da compromissioni per accesso non autorizzato a sistemi o dati.",
        "testo_integrale": "6.4.2 Physical security controls — OVR-6.4.2-02: The facilities concerned with certificate generation and revocation management shall be operated in an environment which physically protects the services from compromise through unauthorized access to systems or data.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.2-03",
        "testo": "Ogni accesso all'area fisicamente sicura deve essere soggetto a supervisione indipendente e le persone non autorizzate devono essere accompagnate da personale autorizzato mentre si trovano nell'area sicura.",
        "testo_integrale": "6.4.2 Physical security controls — OVR-6.4.2-03: Every entry to the physically secure area shall be subject to independent oversight and non-authorized person shall be accompanied by an authorized person whilst in the secure area.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.2-04",
        "testo": "Ogni ingresso e uscita deve essere registrato.",
        "testo_integrale": "6.4.2 Physical security controls — OVR-6.4.2-04: Every entry and exit shall be logged.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.2-05",
        "testo": "La protezione fisica deve essere realizzata mediante perimetri di sicurezza chiaramente definiti (barriere fisiche) attorno ai servizi di generazione certificati e gestione revoche.",
        "testo_integrale": "6.4.2 Physical security controls — OVR-6.4.2-05: Physical protection shall be achieved through the creation of clearly defined security perimeters (i.e. physical barriers) around the certificate generation and revocation management services.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.2-06",
        "testo": "Le parti dei locali condivise con altre organizzazioni devono essere esterne al perimetro dei servizi di generazione certificati e gestione revoche.",
        "testo_integrale": "6.4.2 Physical security controls — OVR-6.4.2-06: Any parts of the premises shared with other organizations shall be outside the perimeter of the certificate generation and revocation management services.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.2-07",
        "testo": "Devono essere implementati controlli di sicurezza fisica e ambientale a protezione della struttura che ospita le risorse di sistema, delle risorse stesse e delle strutture di supporto al loro funzionamento.",
        "testo_integrale": "6.4.2 Physical security controls — OVR-6.4.2-07: Physical and environmental security controls shall be implemented to protect the facility housing system resources, the system resources themselves, and the facilities used to support their operation.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.2-08",
        "testo": "La politica di sicurezza fisica e ambientale del TSP per i sistemi coinvolti nella generazione certificati e gestione revoche deve indirizzare il controllo degli accessi fisici, la protezione da disastri naturali, gli antincendio, i guasti alle utenze di supporto, il crollo strutturale, le perdite idrauliche, la protezione contro furto/effrazione e il disaster recovery.",
        "testo_integrale": "6.4.2 Physical security controls — OVR-6.4.2-08: The TSP's physical and environmental security policy for systems concerned with certificate generation and revocation management services shall address the physical access control, natural disaster protection, fire safety factors, failure of supporting utilities (e.g. power, telecommunications), structure collapse, plumbing leaks, protection against theft, breaking and entering, and disaster recovery.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.2-09",
        "testo": "Devono essere implementati controlli per impedire che apparecchiature, informazioni, supporti e software relativi ai servizi del TSP siano portati fuori sede senza autorizzazione.",
        "testo_integrale": "6.4.2 Physical security controls — OVR-6.4.2-09: Controls shall be implemented to protect against equipment, information, media and software relating to the TSP's services being taken off-site without authorization.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.2-11",
        "testo": "Le chiavi private della Root CA devono essere conservate e utilizzate fisicamente isolate dalle normali operazioni, in modo che solo personale designato di fiducia possa accedervi per firmare i certificati delle CA subordinate.",
        "testo_integrale": "6.4.2 Physical security controls — OVR-6.4.2-11: Root CA private keys shall be held and used physically isolated from normal operations such that only designated trusted personnel have access to the keys for use in signing subordinate CA certificates.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.4.3 Procedural controls ----
    {
        "riferimento": "Parte 1: OVR-6.4.3-01A",
        "testo": "Si applicano i requisiti da REQ-7.4-02X a REQ-7.4-12X di ETSI EN 319 401.",
        "testo_integrale": "6.4.3 Procedural controls — OVR-6.4.3-01A: The requirements REQ-7.4-02X to REQ-7.4-12X in ETSI EN 319 401 [9], shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.4.3-02",
        "testo": "L'emissione di certificati da parte della root CA deve avvenire sotto almeno doppio controllo da parte di personale autorizzato e di fiducia, in modo che nessuna singola persona possa firmare certificati subordinati da sola.",
        "testo_integrale": "6.4.3 Procedural controls — GEN-6.4.3-02: Certificate issuance by the root CA shall be under at least dual control by authorized, trusted personnel such that one person cannot sign subordinate certificates on his/her own.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.4.4 Personnel controls ----
    {
        "riferimento": "Parte 1: OVR-6.4.4-01",
        "testo": "Si applica il requisito della clausola 7.2 di ETSI EN 319 401.",
        "testo_integrale": "6.4.4 Personnel controls — OVR-6.4.4-01: The requirements identified in ETSI EN 319 401 [9], clause 7.2 shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.4-03",
        "testo": "Deve essere previsto il ruolo di validation specialist come specificato dal Baseline Requirements Guideline (BRG). (NOTA: il registration officer può anche essere un validation specialist.)",
        "testo_integrale": "6.4.4 Personnel controls — [WEB] OVR-6.4.4-03: The role of validation specialist shall be included as specified in BRG [5]. NOTE: The registration officer may also be a validation specialist.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando la certificate policy applicabile è WEB (certificati per siti web).",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.4.5 Audit logging procedures ----
    {
        "riferimento": "Parte 1: OVR-6.4.5-01",
        "testo": "Si applica il requisito della clausola 7.10 di ETSI EN 319 401.",
        "testo_integrale": "6.4.5 Audit logging procedures — OVR-6.4.5-01: The requirements identified in ETSI EN 319 401 [9], clause 7.10, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.5-02",
        "testo": "Tutti gli eventi di sicurezza devono essere registrati, incluse le modifiche relative alla politica di sicurezza, l'avvio e l'arresto del sistema, i crash di sistema e i guasti hardware, le attività di firewall e router e i tentativi di accesso al sistema PKI.",
        "testo_integrale": "6.4.5 Audit logging procedures — OVR-6.4.5-02: All security events shall be logged, including changes relating to the security policy, system start-up and shutdown, system crashes and hardware failures, firewall and router activities and PKI system access attempts.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.4.5-03",
        "testo": "Tutti gli eventi relativi alla registrazione, incluse le richieste di re-key o rinnovo del certificato, devono essere registrati.",
        "testo_integrale": "6.4.5 Audit logging procedures — REG-6.4.5-03: All events related to registration including requests for certificate re-key or renewal shall be logged.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.4.5-04",
        "testo": "Devono essere registrate tutte le informazioni di registrazione, tra cui: il tipo di documento presentato dal richiedente; il numero/dato identificativo univoco dei documenti di identificazione; la posizione di conservazione delle copie delle domande e dei documenti di identificazione, incluso l'accordo con il subscriber; le scelte specifiche nell'accordo con il subscriber; l'identità dell'entità che accetta la domanda; il metodo usato per validare i documenti di identificazione; il nome del TSP ricevente e/o della RA che ha trasmesso la domanda.",
        "testo_integrale": "6.4.5 Audit logging procedures — REG-6.4.5-04: All registration information including the following shall be recorded: a) type of document(s) presented by the applicant to support registration; b) record of unique identification data, numbers, or a combination thereof (e.g. applicant's identity card or passport) of identification documents, if applicable; c) storage location of copies of applications and identification documents, including the subscriber agreement (see requirement REG-6.3.4-07); d) any specific choices in the subscriber agreement (e.g. consent to publication of certificate, see requirement REG-6.3.4-07); e) identity of entity accepting the application; f) method used to validate identification documents, if any; and g) name of receiving TSP and/or submitting Registration Authority, if applicable.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.5-04A",
        "testo": "Il TSP deve documentare come l'informazione registrata ai sensi di REG-6.4.5-04 sia accessibile.",
        "testo_integrale": "6.4.5 Audit logging procedures — OVR-6.4.5-04A: The TSP shall document how the information recorded as per REG-6.4.5-04 is accessible.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.4.5-05",
        "testo": "Il TSP deve mantenere la riservatezza delle informazioni relative al subject.",
        "testo_integrale": "6.4.5 Audit logging procedures — REG-6.4.5-05: The TSP shall maintain the privacy of subject information.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP + [{"categoria": "Utente/titolare", "ruolo": "destinatario"}],
    },
    {
        "riferimento": "Parte 1: GEN-6.4.5-06",
        "testo": "Il TSP deve registrare tutti gli eventi relativi al ciclo di vita delle chiavi della CA.",
        "testo_integrale": "6.4.5 Audit logging procedures — GEN-6.4.5-06: The TSP shall log all events relating to the life-cycle of CA keys.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.5-07A",
        "testo": "Il TSP deve registrare tutti gli eventi relativi al ciclo di vita dei certificati come richiesto da REV-6.3.9-18, REG-6.4.5-03, GEN-6.4.5-08, REV-6.4.5-09, SDP-6.4.5-10, nonché tutti gli eventi relativi a generazione e disseminazione dei certificati.",
        "testo_integrale": "6.4.5 Audit logging procedures — OVR-6.4.5-07A: The TSP shall log all events relating to the life-cycle of certificates as requested by REV-6.3.9-18, REG-6.4.5-03, GEN-6.4.5-08, REV-6.4.5-09, SDP-6.4.5-10 as well as all events relating to certificates generation and dissemination.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.4.5-08",
        "testo": "Il TSP deve registrare tutti gli eventi relativi al ciclo di vita delle chiavi gestite dalla CA, incluse le chiavi del subject generate dalla CA.",
        "testo_integrale": "6.4.5 Audit logging procedures — GEN-6.4.5-08: The TSP shall log all events relating to the life cycle of keys managed by the CA, including any subject keys generated by the CA.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.4.5-09",
        "testo": "Il TSP deve registrare tutte le richieste e le segnalazioni relative alla revoca, così come l'azione risultante.",
        "testo_integrale": "6.4.5 Audit logging procedures — REV-6.4.5-09: The TSP shall log all requests and reports relating to revocation, as well as the resulting action.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.4.5-10",
        "testo": "Il TSP deve registrare tutti gli eventi relativi alla preparazione del dispositivo del subject.",
        "testo_integrale": "6.4.5 Audit logging procedures — [NCP+] SDP-6.4.5-10: The TSP shall log all events relating to the preparation of the subject's device.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando la certificate policy applicabile è NCP+ (certificati con dispositivo sicuro).",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.5-11",
        "testo": "Il TSP deve documentare con precisione, nelle proprie dichiarazioni di practice, il periodo di conservazione delle informazioni sopra menzionate e indicare quali informazioni siano soggette a consegna tramite il proprio piano di cessazione.",
        "testo_integrale": "6.4.5 Audit logging procedures — OVR-6.4.5-11: The TSP shall document precisely the period of retention of the information mentioned above in its practices statements and shall indicate which information is subject to be handed-over through its termination plan.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.4.6 Records archival ----
    {
        "riferimento": "Parte 1: OVR-6.4.6-01",
        "testo": "Il TSP deve conservare per almeno sette anni dopo che un certificato basato su tali record cessa di essere valido: il registro di tutti gli eventi relativi al ciclo di vita delle chiavi gestite dalla CA, incluse le coppie di chiavi del subject generate dalla CA (vedi GEN-6.4.5-08); la documentazione identificata alla clausola 6.3.4.",
        "testo_integrale": "6.4.6 Records archival — OVR-6.4.6-01: The TSP shall retain the following for at least seven years after any certificate based on these records ceases to be valid: a) log of all events relating to the life cycle of keys managed by the CA, including any subject key pairs generated by the CA (see requirement GEN-6.4.5-08); b) documentation as identified in clause 6.3.4.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.4.8 Compromise and disaster recovery ----
    {
        "riferimento": "Parte 1: OVR-6.4.8-01",
        "testo": "Si applicano i requisiti delle clausole 7.9 e 7.11 di ETSI EN 319 401.",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — OVR-6.4.8-01: The requirements identified in ETSI EN 319 401 [9], clauses 7.9 and 7.11, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-02",
        "testo": "I dati di sistema del TSP necessari per riprendere le operazioni della CA devono essere sottoposti a backup e conservati in luoghi sicuri, preferibilmente anche remoti, adatti a consentire al TSP di ritornare tempestivamente operativo in caso di incidente/disastro.",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — TSP systems data backup and recovery — OVR-6.4.8-02: TSP's systems data necessary to resume CA operations shall be backed up and stored in safe places, preferably also remote, suitable to allow the TSP to timely go back to operations in case of incident/disasters.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-06",
        "testo": "Le funzioni di backup e ripristino devono essere svolte dai ruoli di fiducia pertinenti specificati alla clausola 6.4.4.",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — TSP systems data backup and recovery — OVR-6.4.8-06: Backup and restore functions shall be performed by the relevant trusted roles specified in clause 6.4.4.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-08",
        "testo": "Il piano di continuità operativa (o disaster recovery plan) del TSP deve trattare la compromissione, perdita o sospetta compromissione della chiave privata di una CA come un disastro.",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — CA key compromise — OVR-6.4.8-08: The TSP's business continuity plan (or disaster recovery plan) shall address the compromise, loss or suspected compromise of a CA's private key as a disaster.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-09",
        "testo": "I processi pianificati ai sensi di OVR-6.4.8-08 devono essere in essere. (NOTA: si suggerisce che il piano includa la revoca di tutti i certificati dei subject; ciò non è necessariamente applicabile ai certificati di breve durata.)",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — CA key compromise — OVR-6.4.8-09: The processes planned as per requirement OVR-6.4.8-08 shall be in place. NOTE: It is suggested that the plan includes a requirement that all subject certificates are revoked. This is not necessarily applicable to short-term certificates.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-10",
        "testo": "In seguito a un disastro, il TSP deve, laddove praticabile, adottare misure per evitare il ripetersi di un disastro.",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — CA key compromise — OVR-6.4.8-10: Following a disaster, the TSP shall, where practical, take steps to avoid repetition of a disaster.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-11",
        "testo": "In caso di compromissione, il TSP deve informare tutti i subscriber e le altre entità con cui ha accordi o altre forme di relazione stabilita, tra cui relying party e altri TSP.",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — CA key compromise — In the case of compromise as a minimum — OVR-6.4.8-11: The TSP shall inform the following of the compromise: all subscribers and other entities with which the TSP has agreements or other form of established relations, among which relying parties and TSPs.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP
        + [
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-12",
        "testo": "Il TSP deve rendere disponibile ad altre relying party l'informazione di cui a OVR-6.4.8-11.",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — CA key compromise — In the case of compromise as a minimum — OVR-6.4.8-12: The TSP shall make the information in OVR-6.4.8-11 available to other relying parties.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP + [{"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"}],
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-13",
        "testo": "Il TSP deve indicare che i certificati e le informazioni di stato di revoca emessi utilizzando la chiave di CA compromessa possono non essere più validi.",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — CA key compromise — In the case of compromise as a minimum — OVR-6.4.8-13: The TSP shall indicate that certificates and revocation status information issued using this CA key may no longer be valid.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP
        + [
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-14A",
        "testo": "Il TSP deve revocare qualsiasi certificato di CA da esso emesso quando venga informato della compromissione di tale CA (anche quando la CA compromessa fa parte del TSP stesso o è gestita da un altro TSP).",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — CA key compromise — In the case of compromise as a minimum — OVR-6.4.8-14A: The TSP shall revoke any CA certificate it has issued when the TSP is informed of the compromise of such a CA (including when the compromised CA is part of the TSP or is managed by another TSP).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-15",
        "testo": "Se un algoritmo, o i relativi parametri, usati dal TSP o dai suoi subscriber diventano insufficienti per l'uso previsto residuo, il TSP deve informarne tutti i subscriber e relying party con cui ha accordi o altre relazioni stabilite, e deve rendere l'informazione disponibile anche alle altre relying party.",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — Algorithm compromise — OVR-6.4.8-15: Should any of the algorithms, or associated parameters, used by the TSP or its subscribers become insufficient for its remaining intended usage then the TSP shall inform all subscribers and relying parties with whom the TSP has agreement or other form of established relations. In addition, the TSP shall make this information available to other relying parties.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP
        + [
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-16",
        "testo": "Se un algoritmo, o i relativi parametri, usati dal TSP o dai suoi subscriber diventano insufficienti per l'uso previsto residuo, il TSP deve pianificare la revoca di ogni certificato interessato.",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — Algorithm compromise — OVR-6.4.8-16: Should any of the algorithms, or associated parameters, used by the TSP or its subscribers become insufficient for its remaining intended usage then the TSP shall schedule a revocation of any affected certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.4.9 Certification Authority or Registration Authority termination ----
    {
        "riferimento": "Parte 1: OVR-6.4.9-01",
        "testo": "Si applica il requisito della clausola 7.12 di ETSI EN 319 401.",
        "testo_integrale": "6.4.9 Certification Authority or Registration Authority termination — OVR-6.4.9-01: The requirements identified in ETSI EN 319 401 [9], clause 7.12, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.9-02",
        "testo": "Il requisito REQ-7.12-06 di ETSI EN 319 401 deve applicarsi, per il rispettivo periodo indicato al subscriber e alla relying party, a: informazioni di registrazione (clausole 6.2.2, 6.3.1 e 6.3.4); informazioni sullo stato di revoca (clausola 6.3.10); archivi dei log degli eventi (clausole 6.4.5 e 6.4.6).",
        "testo_integrale": "6.4.9 Certification Authority or Registration Authority termination — OVR-6.4.9-02: Requirement REQ-7.12-06 of ETSI EN 319 401 [9], shall apply to the following information for their respective period of time as indicated to the subscriber and relying party (see in particular REG-6.3.4-17 and CSS-6.3.10-02): a) registration information (see clauses 6.2.2, 6.3.1 and 6.3.4); b) revocation status information (see clause 6.3.10); c) event log archives (see clauses 6.4.5 and 6.4.6).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.9-03",
        "testo": "Il requisito REQ-7.12-10 di ETSI EN 319 401 deve includere anche la gestione dello stato di revoca per i certificati emessi non ancora scaduti.",
        "testo_integrale": "6.4.9 Certification Authority or Registration Authority termination — OVR-6.4.9-03: Requirement REQ-7.12-10 of ETSI EN 319 401 [9], shall also include the handling of the revocation status for unexpired certificates that have been issued.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.4.9-04",
        "testo": "Quando un altro TSP con cross-certificazione cessa tutte le operazioni, inclusa la gestione della revoca (vedi OVR-6.4.9-03), tutti i cross-certificati verso quel TSP devono essere revocati. (NOTA: tra le entità interessate da informare della cessazione ai sensi di REQ-7.12-10 di ETSI EN 319 401 rientra il TSP cross-certificato.)",
        "testo_integrale": "6.4.9 Certification Authority or Registration Authority termination — OVR-6.4.9-04: When another cross certified TSP stops all operations, including handling revocation (see OVR-6.4.9-03), all cross certificates to that TSP shall be revoked. NOTE: Affected entities to be informed of termination under ETSI EN 319 401 [9], REQ-7.12-10 include cross certified TSP.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.5.1 Key pair generation and installation ----
    {
        "riferimento": "Parte 1: OVR-6.5.1-01",
        "testo": "Si applica il requisito della clausola 7.5 di ETSI EN 319 401.",
        "testo_integrale": "6.5.1 Key pair generation and installation — OVR-6.5.1-01: The requirements identified in ETSI EN 319 401 [9], clause 7.5, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-02",
        "testo": "Il TSP deve generare in modo sicuro le chiavi della CA, incluse quelle usate dai servizi di revoca e registrazione, e la chiave privata deve rimanere segreta.",
        "testo_integrale": "6.5.1 Key pair generation and installation — GEN-6.5.1-02: The TSP shall generate CA keys, including keys used by revocation and registration services, securely and the private key shall be secret.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-03",
        "testo": "La generazione della coppia di chiavi della CA e la successiva certificazione della chiave pubblica devono avvenire in un ambiente fisicamente sicuro (clausola 6.4.2) da parte di personale in ruoli di fiducia (clausola 6.4.4).",
        "testo_integrale": "6.5.1 Key pair generation and installation — GEN-6.5.1-03: The CA key pair generation and the subsequent certification of the public key, shall be undertaken in a physically secured environment (see clause 6.4.2) by personnel in trusted roles (see clause 6.4.4).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-04",
        "testo": "La coppia di chiavi della CA usata per firmare i certificati deve essere creata sotto almeno doppio controllo.",
        "testo_integrale": "6.5.1 Key pair generation and installation — GEN-6.5.1-04: The CA key pair used for signing certificates shall be created under, at least, dual control.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-05",
        "testo": "Il numero di personale autorizzato a effettuare la generazione della coppia di chiavi della CA deve essere ridotto al minimo e coerente con le prassi del TSP.",
        "testo_integrale": "6.5.1 Key pair generation and installation — GEN-6.5.1-05: The number of personnel authorized to carry out CA key pair generation shall be kept to a minimum and be consistent with the TSP's practices.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-08",
        "testo": "Prima della scadenza del certificato di CA usato per firmare le chiavi dei subject, se il servizio continua, la CA deve generare un nuovo certificato per firmare le coppie di chiavi dei subject e applicare tutte le azioni necessarie a evitare interruzioni per chi si affida al certificato di CA.",
        "testo_integrale": "6.5.1 Key pair generation and installation — GEN-6.5.1-08: Before expiration of its CA certificate which is used for signing subject keys (for example as indicated by expiration of CA certificate), in case of continuing with the service, the CA shall generate a new certificate for signing subject key pairs, and shall apply all necessary actions to avoid disruption to the operations of any entity that may rely on the CA certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-09",
        "testo": "Prima della scadenza del certificato di CA usato per firmare le chiavi dei subject, se il servizio continua, il nuovo certificato di CA deve anche essere generato e distribuito in conformità al presente documento.",
        "testo_integrale": "6.5.1 Key pair generation and installation — GEN-6.5.1-09: Before expiration of its CA certificate which is used for signing subject keys (for example, as indicated by expiration of CA certificate), in case of continuing with the service, the new CA certificate shall also be generated and distributed in accordance with the present document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-11",
        "testo": "Il TSP deve avere una procedura documentata per la generazione delle coppie di chiavi di firma dei certificati per tutte le CA, root o subordinate, incluse quelle che emettono certificati agli utenti finali.",
        "testo_integrale": "6.5.1 Key pair generation and installation — GEN-6.5.1-11: The TSP shall have a documented procedure for conducting CA key pair generation for certificate signing keys for all CAs, whether root CAs or subordinate CAs, including CAs that issue certificates to end users.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-12",
        "testo": "La procedura di GEN-6.5.1-11 deve indicare almeno: i ruoli partecipanti alla cerimonia (interni ed esterni all'organizzazione); le funzioni svolte da ciascun ruolo e in quali fasi; le responsabilità durante e dopo la cerimonia; i requisiti di evidenza da raccogliere della cerimonia.",
        "testo_integrale": "6.5.1 Key pair generation and installation — GEN-6.5.1-12: The procedure of GEN-6.5.1-11 shall indicate, at least, the following: a) roles participating in the ceremony (internal and external from the organization); b) functions to be performed by every role and in which phases; c) responsibilities during and after the ceremony; and d) requirements of evidence to be collected of the ceremony.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-13",
        "testo": "Il TSP deve produrre un rapporto che dimostri che la cerimonia, come da GEN-6.5.1-11, è stata svolta in conformità alla procedura stabilita e che l'integrità e la riservatezza della coppia di chiavi sono state garantite.",
        "testo_integrale": "6.5.1 Key pair generation and installation — GEN-6.5.1-13: The TSP shall produce a report proving that the ceremony, as in GEN-6.5.1-11 above, was carried out in accordance with the stated procedure and that the integrity and confidentiality of the key pair was ensured.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-13A",
        "testo": "Il rapporto della key ceremony deve includere almeno: i ruoli partecipanti (interni ed esterni all'organizzazione); le funzioni svolte da ciascun ruolo e in quali fasi; le responsabilità durante e dopo la cerimonia; le evidenze raccolte della cerimonia; la data in cui si è svolta la cerimonia; un inventario delle chiavi generate (identificatore univoco, algoritmo, dimensione della chiave e fingerprint della chiave pubblica, minimo SHA256, per ciascuna chiave); l'identificatore univoco e il modello del dispositivo crittografico sicuro (es. HSM) usato per la cerimonia di generazione; l'algoritmo di generazione delle chiavi e le impostazioni configurate nel dispositivo crittografico sicuro durante la cerimonia (es. modalità operativa, generatore di numeri casuali usato e altri parametri crittografici).",
        "testo_integrale": (
            "6.5.1 Key pair generation and installation — GEN-6.5.1-13A: The report for the key ceremony "
            "shall include at least the following information: roles participating in the ceremony "
            "(internal and external from the organization); functions performed by every role and in which "
            "phases; responsibilities during and after the ceremony; evidence collected of the ceremony; the "
            "date the ceremony was carried out; an inventory of the keys generated, which includes, at least, "
            "the following information for each key: a unique identifier for the key, algorithm, key size and "
            "public key fingerprint (SHA256 minimum); the unique identifier and model of the secure "
            "cryptographic device (e.g. HSM) used for this generation ceremony; the key generation algorithm "
            "and settings configured in the secure cryptographic device during the key ceremony, e.g. "
            "operation mode, used random number generator and other cryptographic parameters."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-13B",
        "testo": "Se il TSP intende conservare chiavi pre-generate per un uso successivo, queste devono essere chiaramente marcate come tali e il TSP deve garantire che l'algoritmo/impostazioni di generazione e il dispositivo inizialmente usati siano ancora idonei all'uso previsto e che la chiave sia ancora crittograficamente sicura al momento della sua installazione (certificazione da parte della CA), confrontando le informazioni registrate con le raccomandazioni correnti di ETSI TS 119 312; se la chiave non è più idonea, non deve essere usata.",
        "testo_integrale": (
            "6.5.1 Key pair generation and installation — [CONDITIONAL] GEN-6.5.1-13B: In case the TSP "
            "intends to keep pre-generated keys for later use, they shall be clearly marked as "
            "\"pre-generated\". If the TSP keeps pre-generated keys for later use, the TSP shall ensure "
            "that: the pre-generated key by the initially used key generation algorithm and settings (e.g. "
            "RNG) and the initially used device for key-generation (e.g. HSM) is still regarded to be fit "
            "for the intended use case at the time of taking the key into operation; and the pre-generated "
            "key is still deemed cryptographically secure for the intended use at the time of its "
            "installation (i.e. certification by the CA). This should be done by comparing the key algorithm "
            "and length information recorded for the key to be used in the related key ceremony (as required "
            "in GEN-6.5.1-13A) against current recommendations as specified in ETSI TS 119 312 [i.10] for the "
            "intended key usage. In case the key is no longer deemed fit for the intended use case it shall "
            "not be used. NOTE 3: The device characteristic initially used for key pre-generation, the RNG, "
            "the cryptographic algorithms and key lengths initially used may have weakened, so that the key "
            "cannot be regarded of being fit for the intended use case anymore. NOTE 4: Cryptographic suites "
            "recommendations defined in ETSI TS 119 312 [i.10] can be superseded by national recommendations."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se il TSP intende conservare chiavi pre-generate per uso successivo.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-14",
        "testo": "Il rapporto deve essere firmato: per la root CA, dal ruolo di fiducia responsabile della sicurezza della cerimonia (es. security officer) e da una persona indipendente dalla direzione del TSP (es. notaio, auditor) come testimone; per le CA subordinate, dal solo ruolo di fiducia responsabile della sicurezza della cerimonia come testimone.",
        "testo_integrale": (
            "6.5.1 Key pair generation and installation — [CHOICE] GEN-6.5.1-14: This report shall be "
            "signed: For root CA: by the trusted role responsible for the security of the TSP's key "
            "management ceremony (e.g. security officer) and a trustworthy person independent of the TSP's "
            "management (e.g. Notary, auditor) as witness that the report correctly records the key "
            "management ceremony as carried out. For subordinate CAs: by the trusted role responsible for "
            "the security of the TSP's key management ceremony (e.g. security officer) as witness that the "
            "report correctly records the key management ceremony as carried out."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica in una delle due forme alternative secondo che si tratti di CA radice o di CA subordinata.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-15",
        "testo": "Si applica la clausola 6.1.1.1 del Baseline Requirements Guideline (BRG).",
        "testo_integrale": "6.5.1 Key pair generation and installation — [WEB] GEN-6.5.1-15: Clause 6.1.1.1 of the BRG [5] shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando la certificate policy applicabile è WEB (certificati per siti web).",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: DIS-6.5.1-16",
        "testo": "Le chiavi pubbliche di verifica della firma della CA devono essere disponibili alle relying party in modo tale da garantire l'integrità della chiave pubblica della CA e autenticarne l'origine. (NOTA: es. distribuzione in certificati auto-firmati con dichiarazione di autenticità, o emessi da altra CA; misure aggiuntive come il controllo del fingerprint sono necessarie per l'attendibilità.)",
        "testo_integrale": (
            "6.5.1 Key pair generation and installation — DIS-6.5.1-16: CA signature verification (public) "
            "keys shall be available to relying parties in a manner that assures the integrity of the CA "
            "public key and authenticates its origin. NOTE 5: For example, CA public keys can be distributed "
            "in self-signed certificates, along with a declaration that the key authenticates the CA, or "
            "issued by another CA. By itself a self-signed certificate cannot be known to come from the CA. "
            "Additional measures, such as checking the fingerprint of the certificate against information "
            "provided by a trusted source, is needed to give assurance of the correctness of this "
            "certificate."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP + [{"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"}],
    },
    {
        "riferimento": "Parte 1: SDP-6.5.1-17",
        "testo": "Se la CA genera le chiavi del subject, queste devono essere generate usando un algoritmo riconosciuto idoneo agli usi identificati nella CP durante la validità del certificato.",
        "testo_integrale": "6.5.1 Key pair generation and installation — When the CA generates the subject's keys — [CONDITIONAL] SDP-6.5.1-17: If the CA generates the subject's keys, CA-generated subject keys shall be generated using an algorithm recognized as being fit for the uses identified in the CP during the validity time of the certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se la CA genera le chiavi del subject.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.5.1-19",
        "testo": "Se la CA genera le chiavi del subject, queste devono essere generate e conservate in modo sicuro mentre sono detenute dal TSP.",
        "testo_integrale": "6.5.1 Key pair generation and installation — When the CA generates the subject's keys — [CONDITIONAL] SDP-6.5.1-19: If the CA generates the subject's keys, CA-generated subject keys shall be generated and stored securely whilst held by the TSP.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se la CA genera le chiavi del subject.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.5.1-20",
        "testo": "Se la CA genera le chiavi del subject, la chiave privata del subject deve essere consegnata al dispositivo del subject o al TSP che gestisce la chiave privata del subject, in modo tale che segretezza e integrità della chiave non siano compromesse.",
        "testo_integrale": "6.5.1 Key pair generation and installation — When the CA generates the subject's keys — [CONDITIONAL] SDP-6.5.1-20: If the CA generates the subject's keys, the subject's private key shall be delivered to the subject's device or to the TSP managing the subject's private key, in a manner such that the secrecy and integrity of the key is not compromised.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se la CA genera le chiavi del subject.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.5.1-21",
        "testo": "Se la CA genera le chiavi del subject e il TSP o le sue RA designate scoprono che una chiave privata del subject è stata comunicata a una persona non autorizzata o a un'organizzazione non affiliata al subject, il TSP deve revocare tutti i certificati che includono la chiave pubblica corrispondente.",
        "testo_integrale": "6.5.1 Key pair generation and installation — When the CA generates the subject's keys — [CONDITIONAL] SDP-6.5.1-21: If the CA generates the subject's keys and if the TSP or any of its designated RAs become aware that a subject's private key has been communicated to an unauthorized person or an organization not affiliated with the subject, then the TSP shall revoke all certificates that include the public key corresponding to the communicated private key.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se la CA genera le chiavi del subject.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.5.1-22",
        "testo": "Se la CA genera le chiavi del subject, la CA deve eliminare tutte le copie della chiave privata del subject dopo la consegna al subject, salvo le condizioni descritte alla clausola 6.3.12.",
        "testo_integrale": "6.5.1 Key pair generation and installation — When the CA generates the subject's keys — [CONDITIONAL] SDP-6.5.1-22: If the CA generates the subject's keys, the CA shall delete all copies of a subject private key after delivery of the private key to the subject, except for conditions as described in clause 6.3.12.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se la CA genera le chiavi del subject.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.5.1-23",
        "testo": "Se la CA genera le chiavi del subject, il TSP deve assicurare l'emissione di un dispositivo crittografico sicuro al subject.",
        "testo_integrale": "6.5.1 Key pair generation and installation — When the CA generates the subject's keys — [NCP+] [CONDITIONAL] SDP-6.5.1-23: If the CA generates the subject's keys, the TSP shall secure the issuance of a secure cryptographic device to the subject.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se la CA genera le chiavi del subject, nell'ambito della certificate policy NCP+.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.5.1-24",
        "testo": "Se la CA genera le chiavi del subject, la preparazione del dispositivo crittografico sicuro deve avvenire in modo sicuro.",
        "testo_integrale": "6.5.1 Key pair generation and installation — When the CA generates the subject's keys — [CONDITIONAL] SDP-6.5.1-24: If the CA generates the subject's keys, secure cryptographic device preparation shall be done securely.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se la CA genera le chiavi del subject.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.5.1-25",
        "testo": "Se la CA genera le chiavi del subject, il dispositivo crittografico sicuro deve essere conservato e distribuito in modo sicuro.",
        "testo_integrale": "6.5.1 Key pair generation and installation — When the CA generates the subject's keys — [CONDITIONAL] SDP-6.5.1-25: If the CA generates the subject's keys, secure cryptographic device shall be securely stored and distributed.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se la CA genera le chiavi del subject.",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.5.2 Private key protection and cryptographic module engineering controls ----
    {
        "riferimento": "Parte 1: OVR-6.5.2-01",
        "testo": "La generazione della coppia di chiavi del TSP, incluse quelle usate dai servizi di revoca e registrazione, deve avvenire in un dispositivo crittografico sicuro, un sistema affidabile che: sia certificato EAL4 o superiore secondo ISO/IEC 15408 (o criteri equivalenti, in base a un'analisi del rischio); oppure soddisfi i requisiti di ISO/IEC 19790, FIPS PUB 140-2 livello 3 o FIPS PUB 140-3 livello 3. (NOTA: standard di common criteria protection profile per i moduli crittografici dei TSP conformi a ISO/IEC 15408 sono TS 419221-2, TS 419221-3, TS 419221-4 o EN 419221-5.)",
        "testo_integrale": (
            "6.5.2 Private key protection and cryptographic module engineering controls — OVR-6.5.2-01: "
            "TSP's key pair generation, including keys used by revocation and registration services, shall "
            "be carried out within a secure cryptographic device which is a trustworthy system which: a) is "
            "assured to EAL 4 or higher in accordance with ISO/IEC 15408 [1], or equivalent national or "
            "internationally recognized evaluation criteria for IT security provided this is a security "
            "target or protection profile which meets the requirements of the present document, based on a "
            "risk analysis and taking into account physical and other non-technical security measures; or "
            "NOTE 1: Standards specifying common criteria protection profiles for TSP's cryptographic "
            "modules, in accordance with ISO/IEC 15408 [1], are TS 419221-2 [i.16], TS 419221-3 [i.17], TS "
            "419221-4 [i.18], or EN 419221-5 [i.19]. b) meets the requirements identified in ISO/IEC 19790 "
            "[3], FIPS PUB 140-2 [13] level 3 or FIPS PUB 140-3 [16] level 3."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.5.2-02",
        "testo": "Il dispositivo crittografico sicuro deve essere utilizzato nella configurazione descritta nella documentazione di certificazione, o in una configurazione equivalente che raggiunga lo stesso obiettivo di sicurezza.",
        "testo_integrale": "6.5.2 Private key protection and cryptographic module engineering controls — OVR-6.5.2-02: The secure cryptographic device shall be operated in its configuration as described in the appropriate certification guidance documentation or in an equivalent configuration which achieves the same security objective.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.2-04",
        "testo": "La chiave privata di firma della CA deve essere detenuta e utilizzata all'interno di un dispositivo crittografico sicuro conforme a OVR-6.5.2-01 e OVR-6.5.2-02.",
        "testo_integrale": "6.5.2 Private key protection and cryptographic module engineering controls — GEN-6.5.2-04: The CA private signing key shall be held and used within a secure cryptographic device meeting the requirements of OVR-6.5.2-01 and OVR-6.5.2-02 above.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.2-05",
        "testo": "Quando si trova fuori dal dispositivo crittografico sicuro, la chiave privata della CA deve essere protetta in modo da garantire lo stesso livello di protezione fornito dal dispositivo.",
        "testo_integrale": "6.5.2 Private key protection and cryptographic module engineering controls — [CONDITIONAL] GEN-6.5.2-05: When outside the secure cryptographic device (see GEN-6.5.2-04 above) the CA private key shall be protected in a way that ensures the same level of protection as provided by the secure cryptographic device.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando la chiave privata della CA si trova fuori dal dispositivo crittografico sicuro.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.2-06",
        "testo": "La chiave privata di firma della CA deve essere sottoposta a backup, conservata e recuperata solo da personale in ruoli di fiducia con almeno doppio controllo, in un ambiente fisicamente sicuro (clausola 6.4.2).",
        "testo_integrale": "6.5.2 Private key protection and cryptographic module engineering controls — GEN-6.5.2-06: The CA private signing key shall be backed up, stored and recovered only by personnel in trusted roles using, at least, dual control in a physically secured environment (see clause 6.4.2).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.2-07",
        "testo": "Il numero di personale autorizzato a effettuare il backup, la conservazione e il recupero della chiave privata di firma della CA deve essere ridotto al minimo e coerente con le prassi della CA.",
        "testo_integrale": "6.5.2 Private key protection and cryptographic module engineering controls — GEN-6.5.2-07: The number of personnel authorized to carry out the CA private signing key back up, storage and recovery shall be kept to a minimum and be consistent with the CA's practices.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.2-08",
        "testo": "Le copie delle chiavi private di firma della CA devono essere soggette allo stesso livello di controlli di sicurezza, o superiore, delle chiavi attualmente in uso.",
        "testo_integrale": "6.5.2 Private key protection and cryptographic module engineering controls — GEN-6.5.2-08: Copies of the CA private signing keys shall be subject to the same or greater level of security controls as keys currently in use.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.2-09",
        "testo": "Quando le chiavi private di firma della CA e le relative copie sono conservate in un dispositivo crittografico sicuro dedicato, devono essere in atto controlli di accesso che assicurino che le chiavi non siano accessibili fuori da tale dispositivo.",
        "testo_integrale": "6.5.2 Private key protection and cryptographic module engineering controls — [CONDITIONAL] GEN-6.5.2-09: Where the CA private signing keys and any copies are stored in a dedicated secure cryptographic device, access controls shall be in place to ensure that the keys are not accessible outside this device.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando le chiavi private di firma della CA e le loro copie sono conservate in un dispositivo crittografico sicuro dedicato.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.5.2-10",
        "testo": "Il dispositivo crittografico sicuro non deve essere manomesso durante la spedizione.",
        "testo_integrale": "6.5.2 Private key protection and cryptographic module engineering controls — OVR-6.5.2-10: The secure cryptographic device shall not be tampered with during shipment.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.5.2-11",
        "testo": "Il dispositivo crittografico sicuro non deve essere manomesso durante la conservazione.",
        "testo_integrale": "6.5.2 Private key protection and cryptographic module engineering controls — OVR-6.5.2-11: The secure cryptographic device shall not be tampered with while stored.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.5.2-12",
        "testo": "Il dispositivo crittografico sicuro deve funzionare correttamente.",
        "testo_integrale": "6.5.2 Private key protection and cryptographic module engineering controls — OVR-6.5.2-12: The secure cryptographic device shall be functioning correctly.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.2-13",
        "testo": "Le chiavi private di firma della CA conservate sul dispositivo crittografico sicuro della CA devono essere distrutte al momento del ritiro del dispositivo. (NOTA: la distruzione non riguarda necessariamente tutte le copie della chiave privata, ma solo l'istanza fisica conservata nel dispositivo in questione.)",
        "testo_integrale": "6.5.2 Private key protection and cryptographic module engineering controls — GEN-6.5.2-13: The CA private signing keys stored on the CA's secure cryptographic device shall be destroyed upon device retirement. NOTE 3: This destruction does not necessarily affect all copies of the private key. Only the physical instance of the key stored in the secure cryptographic device under consideration will be destroyed.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.5.3 Other aspects of key pair management ----
    {
        "riferimento": "Parte 1: OVR-6.5.3-01",
        "testo": "Il TSP deve utilizzare in modo appropriato le chiavi private di firma della CA.",
        "testo_integrale": "6.5.3 Other aspects of key pair management — OVR-6.5.3-01: The TSP shall use appropriately the CA private signing keys.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.5.3-02",
        "testo": "Il TSP non deve utilizzare le chiavi private di firma della CA oltre la fine del loro ciclo di vita.",
        "testo_integrale": "6.5.3 Other aspects of key pair management — OVR-6.5.3-02: The TSP shall not use the CA private signing keys beyond the end of their life cycle.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.3-03",
        "testo": "Le chiavi di firma della CA usate per generare certificati (clausola 6.3.3) e/o emettere informazioni di stato di revoca non devono essere usate per alcun altro scopo.",
        "testo_integrale": "6.5.3 Other aspects of key pair management — GEN-6.5.3-03: CA signing key(s) used for generating certificates as defined in clause 6.3.3, and/or issuing revocation status information, shall not be used for any other purpose.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.3-04",
        "testo": "Le chiavi di firma dei certificati devono essere usate solo all'interno di locali fisicamente sicuri.",
        "testo_integrale": "6.5.3 Other aspects of key pair management — GEN-6.5.3-04: The certificate signing keys shall only be used within physically secure premises.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.3-05",
        "testo": "L'uso della chiave privata della CA deve essere compatibile con l'algoritmo di hash, l'algoritmo di firma e la lunghezza della chiave di firma usati per generare i certificati, in linea con la prassi corrente di cui a GEN-6.5.1-07.",
        "testo_integrale": "6.5.3 Other aspects of key pair management — GEN-6.5.3-05: The use of the CA's private key shall be compatible with the hash algorithm, the signature algorithm and signature key length used for generating certificates, in line with current practice as in requirement GEN-6.5.1-07.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.3-06",
        "testo": "Tutte le copie delle chiavi private di firma della CA devono essere distrutte al termine del loro ciclo di vita.",
        "testo_integrale": "6.5.3 Other aspects of key pair management — GEN-6.5.3-06: All copies of the CA private signing keys shall be destroyed at the end of their life cycle.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.3-07",
        "testo": "Se un certificato auto-firmato è emesso dalla CA, gli attributi del certificato devono essere conformi al key usage definito in ISO/IEC 9594-8/Recommendation ITU-T X.509 e coerenti con GEN-6.5.3-05.",
        "testo_integrale": "6.5.3 Other aspects of key pair management — [CONDITIONAL] GEN-6.5.3-07: If a self-signed certificate is issued by the CA, the attributes of the certificate shall be compliant with the defined key usage as defined in ISO/IEC 9594-8/Recommendation ITU-T X.509 [7] and aligned with GEN-6.5.3-05.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se un certificato auto-firmato è emesso dalla CA.",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.5.4 Activation data ----
    {
        "riferimento": "Parte 1: GEN-6.5.4-01",
        "testo": "L'installazione e il recupero delle coppie di chiavi della CA in un dispositivo crittografico sicuro devono richiedere il controllo simultaneo di almeno due dipendenti di fiducia.",
        "testo_integrale": "6.5.4 Activation data — GEN-6.5.4-01: The installation and recovery of the CA's key pairs in a secure cryptographic device shall require simultaneous control of at least two trusted employees.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.5.4-02",
        "testo": "Se il TSP emette un dispositivo crittografico sicuro, la disattivazione e riattivazione del dispositivo (es. smartcard) devono avvenire in modo sicuro.",
        "testo_integrale": "6.5.4 Activation data — [CONDITIONAL] SDP-6.5.4-02: If the TSP issues a secure cryptographic device, secure cryptographic device (e.g. smartcard) deactivation and reactivation shall be done securely.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se il TSP emette un dispositivo crittografico sicuro.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.5.4-03",
        "testo": "Se il TSP emette un dispositivo crittografico sicuro personalizzato con dati di attivazione utente associati (es. PIN), tali dati devono essere preparati e distribuiti in modo sicuro, separatamente dal dispositivo. (NOTA: la separazione può avvenire distribuendo i dati di attivazione e consegnando il dispositivo in momenti diversi o tramite un canale diverso.)",
        "testo_integrale": "6.5.4 Activation data — [CONDITIONAL] SDP-6.5.4-03: If the TSP issues a secure cryptographic device, and where the personalized secure cryptographic device (e.g. smartcard) has associated user activation data (e.g. PIN code), the activation data shall be securely prepared and distributed separately from the secure cryptographic device. NOTE: Separation can be achieved by ensuring distribution of activation data and delivery of secure cryptographic device at different times, or via a different channel.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se il TSP emette un dispositivo crittografico sicuro personalizzato con dati di attivazione utente associati.",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.5.5 Computer security controls ----
    {
        "riferimento": "Parte 1: OVR-6.5.5-01A",
        "testo": "Si applicano i requisiti REQ-7.4-01, REQ-7.4-02X, REQ-7.4-05X, REQ-7.4-06X e REQ-7.4-13X di ETSI EN 319 401. (NOTE: l'affidabilità dei sistemi può essere garantita usando sistemi conformi a TS 419261 o un adeguato protection profile secondo ISO/IEC 15408; i 'dati sensibili' del requisito REQ-7.4-13X includono le informazioni di registrazione.)",
        "testo_integrale": (
            "6.5.5 Computer security controls — OVR-6.5.5-01A: The requirements REQ-7.4-01, REQ-7.4-02X, "
            "REQ-7.4-05X, REQ-7.4-06X and REQ-7.4-13X in ETSI EN 319 401 [9] shall apply. NOTE 1: "
            "Requirements for the trustworthy systems can be ensured using, for example, systems conforming "
            "to TS 419261 [i.9] or to a suitable protection profile (or profiles), defined in accordance "
            "with ISO/IEC 15408 [1]. NOTE 2: With regards general to requirement REQ-7.4-13X \"Sensitive "
            "data shall be protected\" in ETSI EN 319 401 [9], Sensitive data includes registration "
            "information."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.5-02",
        "testo": "I componenti di rete locale (es. router) devono essere conservati in un ambiente fisicamente e logicamente sicuro.",
        "testo_integrale": "6.5.5 Computer security controls — GEN-6.5.5-02: Local network components (e.g. routers) shall be kept in a physically and logically secure environment.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.5-03",
        "testo": "Le configurazioni dei componenti di rete locale (es. router) devono essere periodicamente verificate per la conformità ai requisiti specificati dal TSP.",
        "testo_integrale": "6.5.5 Computer security controls — GEN-6.5.5-03: Local network components (e.g. routers) configurations shall be periodically checked for compliance with the requirements specified by the TSP.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.5.5-04",
        "testo": "Il TSP deve imporre l'autenticazione multi-fattore per tutti gli account in grado di causare direttamente l'emissione di certificati.",
        "testo_integrale": "6.5.5 Computer security controls — GEN-6.5.5-04: The TSP shall enforce multi-factor authentication for all accounts capable of directly causing certificate issuance.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: DIS-6.5.5-05",
        "testo": "L'applicazione di disseminazione deve applicare il controllo degli accessi sui tentativi di aggiungere o eliminare certificati e modificare altre informazioni associate.",
        "testo_integrale": "6.5.5 Computer security controls — DIS-6.5.5-05: Dissemination application shall enforce access control on attempts to add or delete certificates and modify other associated information.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.5.5-06",
        "testo": "L'applicazione di stato di revoca deve applicare il controllo degli accessi sui tentativi di modificare le informazioni di stato di revoca.",
        "testo_integrale": "6.5.5 Computer security controls — CSS-6.5.5-06: Revocation status application shall enforce access control on attempts to modify revocation status information.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.5.5-07",
        "testo": "Devono essere fornite strutture di monitoraggio continuo e allarme per consentire al TSP di individuare, registrare e reagire tempestivamente a qualsiasi tentativo non autorizzato e/o irregolare di accesso alle proprie risorse.",
        "testo_integrale": "6.5.5 Computer security controls — OVR-6.5.5-07: Continuous monitoring and alarm facilities shall be provided to enable the TSP to detect, register and react in a timely manner upon any unauthorized and/or irregular attempts to access its resources.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.5.6 Life cycle security controls ----
    {
        "riferimento": "Parte 1: OVR-6.5.6-01",
        "testo": "Si applicano i requisiti delle clausole 7.7 e 7.14 di ETSI EN 319 401 per tutti i componenti del servizio.",
        "testo_integrale": "6.5.6 Life cycle security controls — OVR-6.5.6-01: The requirements identified in ETSI EN 319 401 [9], clauses 7.7 and 7.14 shall apply for all service components.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.5.6-02",
        "testo": "La domanda di capacità deve essere monitorata e devono essere fatte previsioni sui futuri requisiti di capacità per garantire che siano disponibili potenza di elaborazione e storage adeguati.",
        "testo_integrale": "6.5.6 Life cycle security controls — [NCP] OVR-6.5.6-02: Capacity demands shall be monitored and projections of future capacity requirements shall be made to ensure that adequate processing power and storage are available.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando la certificate policy applicabile è NCP.",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.5.7 Network security controls ----
    {
        "riferimento": "Parte 1: OVR-6.5.7-01",
        "testo": "Si applica il requisito della clausola 7.8 di ETSI EN 319 401.",
        "testo_integrale": "6.5.7 Network security controls — OVR-6.5.7-01: The requirements identified in ETSI EN 319 401 [9], clause 7.8 shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.5.7-02",
        "testo": "Il TSP deve mantenere e proteggere tutti i sistemi della CA almeno in una zona sicura e implementare/configurare una procedura di sicurezza che protegga sistemi e comunicazioni tra sistemi all'interno di zone sicure e zone ad alta sicurezza.",
        "testo_integrale": "6.5.7 Network security controls — OVR-6.5.7-02: The TSP shall maintain and protect all CA systems in at least a secure zone and shall implement and configure a security procedure that protects systems and communications between systems inside secure zones and high security zones.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.5.7-03",
        "testo": "Il TSP deve configurare tutti i sistemi della CA rimuovendo o disabilitando tutti gli account, applicazioni, servizi, protocolli e porte non usati nelle operazioni della CA.",
        "testo_integrale": "6.5.7 Network security controls — OVR-6.5.7-03: The TSP shall configure all CA systems by removing or disabling all accounts, applications, services, protocols, and ports that are not used in the CA's operations.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.5.7-04",
        "testo": "Il TSP deve concedere l'accesso alle zone sicure e alle zone ad alta sicurezza solo ai ruoli di fiducia.",
        "testo_integrale": "6.5.7 Network security controls — OVR-6.5.7-04: The TSP shall grant access to secure zones and high security zones to only trusted roles.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.5.7-05",
        "testo": "Il sistema della Root CA deve trovarsi in una zona ad alta sicurezza.",
        "testo_integrale": "6.5.7 Network security controls — OVR-6.5.7-05: The Root CA system shall be in a high security zone.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.6.1 Certificate profile ----
    {
        "riferimento": "Parte 1: GEN-6.6.1-01",
        "testo": "I certificati devono soddisfare i requisiti di ISO/IEC 9594-8/Recommendation ITU-T X.509 o IETF RFC 5280.",
        "testo_integrale": "6.6.1 Certificate profile — GEN-6.6.1-01: The certificates shall meet the requirements specified in ISO/IEC 9594-8/Recommendation ITU-T X.509 [7] or IETF RFC 5280 [8].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.6.1-02",
        "testo": "Il certificato deve essere emesso secondo il profilo di certificato pertinente: per persone fisiche (esclusi certificati per siti web), sotto LCP/NCP/NCP+, secondo ETSI EN 319 412-2; per persone giuridiche (esclusi siti web), sotto LCP/NCP/NCP+, secondo ETSI EN 319 412-3; per siti web o dispositivi, sotto OVCP/IVCP/DVCP/EVCP e LCP/NCP/NCP+, secondo ETSI EN 319 412-4.",
        "testo_integrale": (
            "6.6.1 Certificate profile — [CHOICE] GEN-6.6.1-02: The certificate shall be issued according to "
            "the relevant certificate profile: [LCP, NCP and NCP+] for issuance of certificates to natural "
            "persons (excluding for web site certificates): ETSI EN 319 412-2 [10]. [LCP, NCP and NCP+] for "
            "issuance of certificates to legal persons (excluding for web site certificates): ETSI EN 319 "
            "412-3 [11]. [OVCP], [IVCP], [DVCP], [EVCP], and [LCP], [NCP] and [NCP+] for issuance of "
            "certificates for web sites or devices: ETSI EN 319 412-4 [2]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica secondo il profilo di certificato pertinente (persona fisica, persona giuridica, o sito web/dispositivo) e la certificate policy applicabile.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.6.1-04",
        "testo": "Il TSP che emette certificati di breve durata non deve usare l'estensione ext-etsi-valassured-ST-certs di ETSI EN 319 412-1 nei certificati di breve durata revocabili.",
        "testo_integrale": "6.6.1 Certificate profile — GEN-6.6.1-04: The TSP issuing short-term certificates shall not use the validity assured extension ext-etsi-valassured-ST-certs defined in ETSI EN 319 412-1 [14] in short-term certificates which can be revoked.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.6.1-05",
        "testo": "Il TSP non deve usare l'estensione ext-etsi-valassured-ST-certs di ETSI EN 319 412-1 in certificati che non siano di breve durata.",
        "testo_integrale": "6.6.1 Certificate profile — GEN-6.6.1-05: The TSP shall not use the validity assured extension ext-etsi-valassured-ST-certs defined in ETSI EN 319 412-1 [14] in certificates which are not short-term certificates.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.6.2 CRL profile ----
    {
        "riferimento": "Parte 1: OVR-6.6.2-01",
        "testo": "La CRL deve essere conforme a ISO/IEC 9594-8/Recommendation ITU-T X.509 o IETF RFC 5280.",
        "testo_integrale": "6.6.2 CRL profile — OVR-6.6.2-01: The CRL shall be as defined in ISO/IEC 9594-8/Recommendation ITU-T X.509 [7] or IETF RFC 5280 [8].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.6.3 OCSP profile ----
    {
        "riferimento": "Parte 1: OVR-6.6.3-01",
        "testo": "L'OCSP deve essere conforme a IETF RFC 6960.",
        "testo_integrale": "6.6.3 OCSP profile — OVR-6.6.3-01: The OCSP shall be as defined in IETF RFC 6960 [12].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.6.3-01B",
        "testo": "Il TSP non deve usare l'estensione AIA 'id-ad-ocsp' accessMethod nel certificato dell'OCSP. (NOTA: per evitare un loop nella validazione del certificato dell'OCSP.)",
        "testo_integrale": "6.6.3 OCSP profile — CSS-6.6.3-01B: The TSP shall not use the AIA extension \"id-ad-ocsp\" accessMethod in the OCSP's certificate. NOTE 2: This is to avoid loop in the validation of the OCSP's certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.6.3-02",
        "testo": "Se il responder OCSP riceve una richiesta di stato per un certificato non emesso, non deve rispondere con stato 'good' secondo la clausola 2.2 di IETF RFC 6960. (NOTA: quando sono forniti sia OCSP che CRL, il TSP deve configurare le risposte OCSP per i certificati non emessi in modo coerente con il requisito CSS-6.3.10-09; se la risposta è 'revoked', la motivazione di non-emissione deve essere identificabile.)",
        "testo_integrale": "6.6.3 OCSP profile — OVR-6.6.3-02: If the OCSP responder receives a request for status of a certificate that has not been issued then the responder shall not respond with a \"good\" status as per clause 2.2 of IETF RFC 6960 [12]. NOTE 3: When both OCSP and CRL are provided, the TSP needs to configure OCSP answers for non-issued certificates in a way which is appropriate to meet the consistency requirement CSS-6.3.10-09. In particular, if the responder sends a \"revoked\" response, the non-issued reason needs to be identifiable (knowing that non-issued certificates do not appear in a CRL).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.8.2 Financial responsibility ----
    {
        "riferimento": "Parte 1: OVR-6.8.2-01",
        "testo": "Si applica il requisito REQ-7.1.1-04 di ETSI EN 319 401.",
        "testo_integrale": "6.8.2 Financial responsibility — OVR-6.8.2-01: The requirement REQ-7.1.1-04 identified in ETSI EN 319 401 [9], shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.8.4 Privacy of personal information ----
    {
        "riferimento": "Parte 1: OVR-6.8.4-01",
        "testo": "Si applica il requisito REQ-7.13-05 di ETSI EN 319 401.",
        "testo_integrale": "6.8.4 Privacy of personal information — OVR-6.8.4-01: The requirement REQ 7.13-05 identified in ETSI EN 319 401 [9], shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.8.4-02",
        "testo": "La riservatezza e l'integrità dei dati di registrazione devono essere protette, specialmente quando scambiati con il subscriber/subject o tra componenti di sistema distribuiti del TSP.",
        "testo_integrale": "6.8.4 Privacy of personal information — OVR-6.8.4-02: The confidentiality and integrity of registration data shall be protected, especially when exchanged with the subscriber/subject or between distributed TSP's system components.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP + [{"categoria": "Utente/titolare", "ruolo": "destinatario"}],
    },
    # ---- 6.8.6 Representations and warranties ----
    {
        "riferimento": "Parte 1: OVR-6.8.6-02",
        "testo": "Il TSP deve fornire tutti i propri servizi di certificazione in modo coerente con la propria CPS.",
        "testo_integrale": "6.8.6 Representations and warranties — OVR-6.8.6-02: The TSP shall provide all its certification services consistent with its CPS.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.8.13 Dispute resolution procedures ----
    {
        "riferimento": "Parte 1: OVR-6.8.13-01",
        "testo": "Si applicano la lettera h) del requisito REQ-6.2-02 e il requisito REQ-7.1.1-06 di ETSI EN 319 401.",
        "testo_integrale": "6.8.13 Dispute resolution procedures — OVR-6.8.13-01: The item h) of requirement REQ-6.2-02 identified in ETSI EN 319 401 [9], and the requirement REQ-7.1.1-06 identified in ETSI EN 319 401 [9], shall apply. NOTE: See clause A.2 for additional information.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.8.15 Compliance with applicable law ----
    {
        "riferimento": "Parte 1: OVR-6.8.15-01",
        "testo": "Si applicano i requisiti REQ-7.13-01 e REQ-7.13-02 di ETSI EN 319 401.",
        "testo_integrale": "6.8.15 Compliance with applicable law — OVR-6.8.15-01: The requirements REQ-7.13-01 and REQ-7.13-02 identified in ETSI EN 319 401 [9], shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.9.1 Organizational ----
    {
        "riferimento": "Parte 1: OVR-6.9.1-01",
        "testo": "Si applica il requisito della clausola 7.1 di ETSI EN 319 401.",
        "testo_integrale": "6.9.1 Organizational — OVR-6.9.1-01: The requirements identified in ETSI EN 319 401 [9], clause 7.1 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.9.1-02",
        "testo": "Le parti del TSP coinvolte nella generazione dei certificati e nella gestione delle revoche devono essere indipendenti da altre organizzazioni per le proprie decisioni relative a stabilire, fornire, mantenere e sospendere i servizi in conformità alle certificate policy applicabili.",
        "testo_integrale": "6.9.1 Organizational — OVR-6.9.1-02: The parts of the TSP concerned with certificate generation and revocation management shall be independent of other organizations for its decisions relating to the establishing, provisioning and maintaining and suspending of services in conformance with the applicable certificate policies.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.9.1-03",
        "testo": "I dirigenti, il personale senior e il personale in ruoli di fiducia del TSP coinvolti nella generazione dei certificati e nella gestione delle revoche devono essere liberi da qualsiasi pressione commerciale, finanziaria o di altro tipo che possa influenzare negativamente la fiducia nei servizi forniti. (NOTA: il TSP potrebbe dover tenere conto dei requisiti sulla privacy.)",
        "testo_integrale": "6.9.1 Organizational — OVR-6.9.1-03: The senior executive, senior staff and staff in trusted roles, of the TSP concerned with certificate generation and revocation management shall be free from any commercial, financial and other pressures which might adversely influence trust in the services it provides. NOTE: The TSP may need to take into account privacy requirements.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.9.1-04",
        "testo": "Le parti del TSP coinvolte nella generazione dei certificati e nella gestione delle revoche devono avere una struttura documentata che salvaguardi l'imparzialità delle operazioni.",
        "testo_integrale": "6.9.1 Organizational — OVR-6.9.1-04: The parts of the TSP concerned with certificate generation and revocation management shall have a documented structure which safeguards impartiality of operations.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.9.2 Additional testing ----
    {
        "riferimento": "Parte 1: OVR-6.9.2-01",
        "testo": "Il TSP deve fornire la capacità di consentire a terzi di controllare e testare tutti i tipi di certificato che emette.",
        "testo_integrale": "6.9.2 Additional testing — OVR-6.9.2-01: The TSP shall provide the capability to allow third parties to check and test all the certificate types that the TSP issues.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.9.2-01B",
        "testo": "Quando i certificati emessi sull'ambiente di produzione sono usati per finalità di test nel contesto di OVR-6.9.2-01A, tali certificati di produzione devono conformarsi ai requisiti della certificate policy applicabile. (NOTA: il TSP può usare uno pseudonimo per garantire la riservatezza dei dati.)",
        "testo_integrale": "6.9.2 Additional testing — [CONDITIONAL] OVR-6.9.2-01B: When certificates issued on the production environment are used for testing purpose in the context of OVR-6.9.2-01A, such production certificates shall conform to the applicable certificate policy requirements. NOTE: The TSP can use a pseudonym to ensure data privacy.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando certificati emessi sull'ambiente di produzione sono usati per finalità di test.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.9.2-01C",
        "testo": "Quando i certificati emessi sull'ambiente di produzione sono usati per finalità di test, il TSP deve indicare nella propria CPS come fornisce una ragionevole garanzia che i certificati di test non possano essere usati fuori dall'ambito del test.",
        "testo_integrale": "6.9.2 Additional testing — [CONDITIONAL] OVR-6.9.2-01C: When certificates issued on the production environment are used for testing purpose, the TSP shall state in its CPS how it provides reasonable assurance that testing certificates cannot be used outside of the testing scope.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando certificati emessi sull'ambiente di produzione sono usati per finalità di test.",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.9.3 Disabilities ----
    {
        "riferimento": "Parte 1: OVR-6.9.3-01",
        "testo": "Si applicano i requisiti REQ-7.13-03 e REQ-7.13-04 di ETSI EN 319 401.",
        "testo_integrale": "6.9.3 Disabilities — OVR-6.9.3-01: The requirements REQ-7.13-03 and REQ-7.13-04 identified in ETSI EN 319 401 [9], shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    # ---- 6.9.4 Terms and conditions ----
    {
        "riferimento": "Parte 1: OVR-6.9.4-01",
        "testo": "Si applica il requisito della clausola 6.2 di ETSI EN 319 401.",
        "testo_integrale": "6.9.4 Terms and conditions — OVR-6.9.4-01: The requirements identified in ETSI EN 319 401 [9], clause 6.2 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.9.4-02",
        "testo": "I termini e condizioni devono includere almeno: l'indicazione di cosa costituisce accettazione del certificato (OVR-6.3.4-01); il periodo di conservazione dei record (OVR-6.3.4-17); gli obblighi del subscriber (OVR-6.3.5-01); ove applicabile, gli obblighi del subject (OVR-6.3.5-02); l'avviso alle relying party (OVR-6.3.5-03); i modi in cui una specifica policy si aggiunge o restringe ulteriormente i requisiti della CP (OVR-7.2-01).",
        "testo_integrale": (
            "6.9.4 Terms and conditions — OVR-6.9.4-02: The terms and conditions shall include at minimum "
            "the following elements: a) the indication of what constitutes certificate acceptance, as "
            "specified in OVR-6.3.4-01; b) the period of time for which the records are retained according "
            "to OVR-6.3.4-17; c) the subscriber's obligations as specified in OVR-6.3.5-01; d) where "
            "applicable, the subject's obligations as specified in OVR-6.3.5-02; e) the notice to relying "
            "parties as specified in OVR-6.3.5-03; f) the ways in which a specific policy adds to or further "
            "constrains the requirements of the CP as defined in the present document, see OVR-7.2-01."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP
        + [
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "Parte 1: OVR-6.4.2-10",
        "testo": "Altre funzioni relative alle operazioni del TSP possono essere supportate all'interno della stessa area protetta, a condizione che l'accesso sia limitato al personale autorizzato.",
        "testo_integrale": "6.4.2 Physical security controls — OVR-6.4.2-10: Other functions relating to TSP's operations may be supported within the same secured area provided that the access is limited to authorized personnel.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Facoltà applicabile se l'accesso all'area è limitato al personale autorizzato.",
    },
    {
        "riferimento": "Parte 1: clausola 6.4.7",
        "testo": "La clausola 6.4.7 (Key changeover) non impone alcun requisito di policy proprio.",
        "testo_integrale": "6.4.7 Key changeover — No policy requirement.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: OVR-6.4.4-02",
        "testo": "Oltre ai ruoli di fiducia identificati da ETSI EN 319 401 (clausola 7.2-15), dovrebbero essere supportati i ruoli di fiducia di registration officer e revocation officer con le responsabilità definite in TS 419261.",
        "testo_integrale": "6.4.4 Personnel controls — OVR-6.4.4-02: In addition to the trusted roles identified in ETSI EN 319 401 [9], (clause 7.2-15), the trusted roles of the registration and revocation officers with responsibilities as defined in TS419261 [i.9] should be supported.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-03",
        "testo": "In linea con la clausola 12.3 di ISO/IEC 27002, le copie di backup delle informazioni e del software essenziali dovrebbero essere effettuate regolarmente.",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — TSP systems data backup and recovery — OVR-6.4.8-03: In line with ISO/IEC 27002 [i.7], clause 12.3: Back-up copies of essential information and software should be taken regularly.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-04",
        "testo": "Dovrebbero essere fornite strutture di backup adeguate a garantire che tutte le informazioni e il software essenziali possano essere recuperati dopo un disastro o un guasto dei supporti.",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — TSP systems data backup and recovery — OVR-6.4.8-04: Adequate back-up facilities should be provided to ensure that all essential information and software can be recovered following a disaster or media failure.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-05",
        "testo": "Le disposizioni di backup dovrebbero essere testate regolarmente per garantire che soddisfino i requisiti dei piani di continuità operativa.",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — TSP systems data backup and recovery — OVR-6.4.8-05: Back-up arrangements should be regularly tested to ensure that they meet the requirements of business continuity plans.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: OVR-6.4.8-07",
        "testo": "Se l'analisi del rischio individua informazioni che richiedono un doppio controllo per la gestione (es. chiavi), il doppio controllo dovrebbe essere applicato anche al recupero.",
        "testo_integrale": "6.4.8 Compromise and disaster recovery — TSP systems data backup and recovery — [CONDITIONAL] OVR-6.4.8-07: If risk analysis identifies information requiring dual control for management, for example keys, then dual control should be applied to recovery.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se l'analisi del rischio individua informazioni che richiedono un doppio controllo per la gestione.",
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-06",
        "testo": "La generazione della coppia di chiavi della CA dovrebbe usare un algoritmo specificato in ETSI TS 119 312 per le finalità di firma della CA. (Le raccomandazioni sulle suite crittografiche di TS 119 312 possono essere superate da raccomandazioni nazionali.)",
        "testo_integrale": "6.5.1 Key pair generation and installation — GEN-6.5.1-06: CA key pair generation should be performed using an algorithm as specified in ETSI TS 119 312 [i.10] for the CA's signing purposes. NOTE 1: Cryptographic suites recommendations defined in ETSI TS 119 312 [i.10] can be superseded by national recommendations.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-07",
        "testo": "La lunghezza della chiave e l'algoritmo scelti per la chiave di firma della CA dovrebbero essere quelli specificati in ETSI TS 119 312. (Le raccomandazioni sulle suite crittografiche di TS 119 312 possono essere superate da raccomandazioni nazionali.)",
        "testo_integrale": "6.5.1 Key pair generation and installation — GEN-6.5.1-07: The selected key length and algorithm for CA signing key should be one which is specified in ETSI TS 119 312 [i.10] for the CA's signing purposes. NOTE 2: Cryptographic suites recommendations defined in ETSI TS 119 312 [i.10] can be superseded by national recommendations.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: GEN-6.5.1-10",
        "testo": "Le operazioni di GEN-6.5.1-08 e GEN-6.5.1-09 dovrebbero essere svolte con un intervallo adeguato tra la data di scadenza del certificato e l'ultimo certificato firmato, per consentire a tutte le parti in relazione con il TSP di essere consapevoli del cambio di chiave e implementare le operazioni necessarie; ciò non si applica a un TSP che cesserà le operazioni prima della scadenza del proprio certificato di firma.",
        "testo_integrale": "6.5.1 Key pair generation and installation — GEN-6.5.1-10: The operations described in GEN-6.5.1-08 and GEN-6.5.1-09 should be performed with a suitable interval between certificate expiry date and the last certificate signed to allow all parties that have relationships with the TSP (subjects, subscribers, relying parties, CAs higher in the CA hierarchy, etc.) to be aware of this key changeover and to implement the required operations to avoid inconveniences and malfunctions. This does not apply to a TSP which will cease its operations before its own certificate-signing certificate expiration date.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: SDP-6.5.1-18",
        "testo": "Se la CA genera le chiavi del subject, queste dovrebbero avere una lunghezza e un algoritmo a chiave pubblica specificati in ETSI TS 119 312 per gli usi indicati nella CP durante la validità del certificato.",
        "testo_integrale": "6.5.1 Key pair generation and installation — When the CA generates the subject's keys — [CONDITIONAL] SDP-6.5.1-18: If the CA generates the subject's keys, CA-generated subject keys should be of a key length and for use with a public key algorithm as specified in ETSI TS 119 312 [i.10] for the purposes stated in the CP during the validity time of the certificate. NOTE 4: Cryptographic suites recommendations defined in ETSI TS 119 312 [i.10] can be superseded by national recommendations.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se la CA genera le chiavi del subject.",
    },
    {
        "riferimento": "Parte 1: OVR-6.5.2-03",
        "testo": "Il dispositivo crittografico sicuro sopra descritto dovrebbe essere certificato secondo ISO/IEC 15408, come per OVR-6.5.2-01-a). (Ciò si applica anche alla generazione di chiavi svolta in un sistema separato.)",
        "testo_integrale": "6.5.2 Private key protection and cryptographic module engineering controls — OVR-6.5.2-03: The above secure cryptographic device should be assured using ISO/IEC 15408 [1], as per OVR-6.5.2-01-a), above. NOTE 2: This applies also to key generation even if carried out in a separate system.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.5.8",
        "testo": "Il timestamping non è nell'ambito del presente documento; per i requisiti di policy dei TSP che emettono marche temporali si rinvia a ETSI EN 319 421.",
        "testo_integrale": "6.5.8 Timestamping — NOTE: Not in the scope of the present document. See ETSI EN 319 421 [i.15] for policy requirements for TSPs issuing time-stamps.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: GEN-6.6.1-03",
        "testo": "Un TSP che emette certificati di breve durata dovrebbe usare l'estensione ext-etsi-valassured-ST-certs di ETSI EN 319 412-1 nei certificati di breve durata non revocabili.",
        "testo_integrale": "6.6.1 Certificate profile — GEN-6.6.1-03: A TSP issuing short-term certificate should use the validity assured extension ext-etsi-valassured-ST-certs defined in ETSI EN 319 412-1 [14] within the short-term certificates which cannot be revoked.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: CSS-6.6.3-01A",
        "testo": "Il TSP dovrebbe includere l'estensione OCSPnoCheck nel certificato dell'OCSP. (NOTA: la scelta di non-check comporta rischi aggiuntivi paragonabili alla compromissione della chiave della CA emittente, da considerare nella gestione del rischio e nella durata del certificato del responder; alcune applicazioni terze potrebbero non gestire l'estensione non critica, con possibili problemi operativi se non è previsto un fallback come una CRL complementare.)",
        "testo_integrale": (
            "6.6.3 OCSP profile — CSS-6.6.3-01A: The TSP should include the OCSPnoCheck extension in the "
            "OCSP's certificate. NOTE 1: A TSP can decide to use the id-pkix-ocsp-nocheck extension in the "
            "certificate profile of a delegated OCSP responder as described in clause 4.2.2.2.1 (Revocation "
            "Checking of an Authorized Responder) of IETF RFC 6960 [12]. In that case, no revocation status "
            "information is required for determining the status of the corresponding responder certificate "
            "which may be considered as useful for various reasons. However, a TSP who decides to do so "
            "takes the following additional risks into account in its risk assessment: As stipulated in "
            "IETF RFC 6960 [12], an OCSP responder key compromise is, in this case, as severe as a "
            "compromise of the corresponding issuing CA key. To this reason, the TSP carefully considers "
            "OCSP responder key management and particularly considers reducing responder certificate "
            "lifetime to a reasonable duration. Third party applications like Signature Validation "
            "Authorities that rely on the TSP's certificate status information services may not be able to "
            "handle this non-critical extension. Consequently they can end up with operational issues when "
            "no fall back scenario like complementary provisioning of a CRL is implemented for revealing the "
            "responder status, or can end up in invalidating the signature. This can be documented within "
            "the CPS/CP."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: OVR-6.6.3-03",
        "testo": "La CA dovrebbe monitorare le richieste relative a certificati non emessi sul responder, come parte delle proprie procedure di risposta alla sicurezza, per verificare se ciò sia indicativo di un attacco.",
        "testo_integrale": "6.6.3 OCSP profile — OVR-6.6.3-03: The CA should monitor such requests concerning non-issued certificates on the responder as part of its security response procedures to check if this is an indication of an attack.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.7",
        "testo": "Per l'audit di conformità e le altre valutazioni si rinvia a ETSI EN 319 403.",
        "testo_integrale": "6.7 Compliance audit and other assessment — NOTE: See ETSI EN 319 403 [i.2].",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.8.1",
        "testo": "I presenti requisiti di policy non intendono implicare alcuna restrizione sulla facoltà del TSP di applicare tariffe per i propri servizi.",
        "testo_integrale": "6.8.1 Fees — These policy requirements are not meant to imply any restrictions on charging for TSP's services.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.8.3",
        "testo": "La clausola 6.8.3 (Confidentiality of business information) non impone alcun requisito di policy proprio.",
        "testo_integrale": "6.8.3 Confidentiality of business information — No policy requirement.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: OVR-6.8.4-03",
        "testo": "Alcuni record potrebbero necessitare di conservazione sicura per soddisfare requisiti di legge e supportare le attività essenziali del business (clausole 6.4.5 e 6.4.6). (NOTA: le questioni di protezione dati specifiche sono affrontate in: registrazione, clausola 6.2.2; riservatezza dei record, REG-6.3.2-02 e REG-6.4.5-05; protezione dell'accesso alle informazioni personali, OVR-6.8.4-02; consenso dell'utente, REG-6.3.4-07 e REG-6.3.4-08.)",
        "testo_integrale": (
            "6.8.4 Privacy of personal information — OVR-6.8.4-03: Some records may need to be securely "
            "retained to meet statutory requirements, as well as to support essential business activities "
            "(see clauses 6.4.5 and 6.4.6). NOTE: Data protection issues specific to these policy "
            "requirements are addressed in: a) registration (see clause 6.2.2); b) confidentiality of "
            "records (see requirements REG-6.3.2-02 and REG-6.4.5-05); c) protecting access to personal "
            "information (OVR-6.8.4-02); d) user consent (see requirement REG-6.3.4-07 and REG-6.3.4-08)."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.8.5",
        "testo": "La clausola 6.8.5 (Intellectual property rights) non impone alcun requisito di policy proprio.",
        "testo_integrale": "6.8.5 Intellectual property rights — No policy requirement.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: OVR-6.8.6-01",
        "testo": "Il TSP resta responsabile della conformità alle procedure prescritte da questa policy anche quando le sue funzionalità sono svolte da outsourcer. I requisiti OVR-6.4.1-01 e OVR-6.9.1-01 del presente documento, che richiamano i requisiti REQ-7.14.3-01X, -02X, -04X, -05X e -06X di ETSI EN 319 401, si applicano anche al rapporto tra il TSP e i fornitori di componenti di trust service, quando parte delle operazioni del TSP è affidata a tali fornitori separati.",
        "testo_integrale": "6.8.6 Representations and warranties — OVR-6.8.6-01: Void. NOTE 1: TSP has the responsibility for conformance with the procedures prescribed in this policy, even when the TSP's functionality is undertaken by outsourcers. NOTE 2: The requirements OVR-6.4.1-01 and OVR-6.9.1-01 of the present document, referencing REQ-7.14.3-01X, REQ-7.14.3-02X, REQ-7.14.3-04X, REQ-7.14.3-05X and REQ-7.14.3-06X identified in ETSI EN 319 401 [9], apply also to the relationship between the TSP and trust service component providers, when part of the TSP operations are provided by separate trust service component providers.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.8.7",
        "testo": "Per le esclusioni di garanzia si rinvia alla clausola 6.8.6 (e alla clausola A.2 per informazioni aggiuntive).",
        "testo_integrale": "6.8.7 Disclaimers of warranties — See clause 6.8.6. NOTE: See also clause A.2 for additional information.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.8.8",
        "testo": "Le limitazioni di responsabilità sono trattate nei termini e condizioni ai sensi della clausola 6.9.4. (NOTA: per i TSP operanti nell'UE, si rinvia all'articolo 13 del Regolamento (UE) n. 910/2014.)",
        "testo_integrale": "6.8.8 Limitations of liability — Limitations on liability are covered in the terms and conditions as per clause 6.9.4. NOTE: For TSP operating in EU, see article 13 of the Regulation (EU) No 910/2014 [i.14].",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.8.9",
        "testo": "La clausola 6.8.9 (Indemnities) non impone alcun requisito di policy proprio.",
        "testo_integrale": "6.8.9 Indemnities — No policy requirement.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.8.10",
        "testo": "La clausola 6.8.10 (Term and termination) non impone alcun requisito di policy proprio.",
        "testo_integrale": "6.8.10 Term and termination — No policy requirement.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.8.11",
        "testo": "La clausola 6.8.11 (Individual notices and communications with participants) non impone alcun requisito di policy proprio.",
        "testo_integrale": "6.8.11 Individual notices and communications with participants — No policy requirement.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.8.12",
        "testo": "La clausola 6.8.12 (Amendments) non impone alcun requisito di policy proprio.",
        "testo_integrale": "6.8.12 Amendments — No policy requirement.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.8.14",
        "testo": "La legge applicabile (Governing law) non è nell'ambito del presente documento.",
        "testo_integrale": "6.8.14 Governing law — Not in the scope of the present document.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.8.16",
        "testo": "La clausola 6.8.16 (Miscellaneous provisions) non impone alcun requisito di policy proprio.",
        "testo_integrale": "6.8.16 Miscellaneous provisions — No policy requirement.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: OVR-6.9.2-01A",
        "testo": "Nel contesto di OVR-6.9.2-01, il TSP può usare certificati emessi sull'ambiente di produzione.",
        "testo_integrale": "6.9.2 Additional testing — OVR-6.9.2-01A: In the context of OVR-6.9.2-01, the TSP may use certificates issued on the production environment.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: OVR-6.9.4-03",
        "testo": "Il TSP può limitare le proprie responsabilità come indicato alla clausola 9.8 del Baseline Requirements Guideline (BRG). (NOTA: tale clausola offre al TSP la possibilità di limitare le proprie responsabilità per i profili OVCP, IVCP, DVCP o EVCP.)",
        "testo_integrale": "6.9.4 Terms and conditions — [WEB] OVR-6.9.4-03: The TSP may limit its responsibilities as indicated in clause 9.8 of BRG [5]. NOTE: Clause 9.8 of BRG [6] provides possibilities for the TSP to limit its responsibilities for [OVCP], [IVCP], [DVCP] or [EVCP].",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Facoltà applicabile quando la certificate policy applicabile è WEB (certificati per siti web).",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    # 6.4.1
    "Parte 1: OVR-6.4.1-01",
    # 6.4.2
    "Parte 1: OVR-6.4.2-01", "Parte 1: OVR-6.4.2-02", "Parte 1: OVR-6.4.2-03", "Parte 1: OVR-6.4.2-04", "Parte 1: OVR-6.4.2-05",
    "Parte 1: OVR-6.4.2-06", "Parte 1: OVR-6.4.2-07", "Parte 1: OVR-6.4.2-08", "Parte 1: OVR-6.4.2-09", "Parte 1: OVR-6.4.2-10",
    "Parte 1: OVR-6.4.2-11",
    # 6.4.3
    "Parte 1: OVR-6.4.3-01A", "Parte 1: GEN-6.4.3-02",
    # 6.4.4
    "Parte 1: OVR-6.4.4-01", "Parte 1: OVR-6.4.4-02", "Parte 1: OVR-6.4.4-03",
    # 6.4.5
    "Parte 1: OVR-6.4.5-01", "Parte 1: OVR-6.4.5-02", "Parte 1: REG-6.4.5-03", "Parte 1: REG-6.4.5-04", "Parte 1: OVR-6.4.5-04A",
    "Parte 1: REG-6.4.5-05", "Parte 1: GEN-6.4.5-06", "Parte 1: OVR-6.4.5-07A", "Parte 1: GEN-6.4.5-08", "Parte 1: REV-6.4.5-09",
    "Parte 1: SDP-6.4.5-10", "Parte 1: OVR-6.4.5-11",
    # 6.4.6
    "Parte 1: OVR-6.4.6-01",
    # 6.4.7
    "Parte 1: clausola 6.4.7",
    # 6.4.8
    "Parte 1: OVR-6.4.8-01", "Parte 1: OVR-6.4.8-02", "Parte 1: OVR-6.4.8-03", "Parte 1: OVR-6.4.8-04", "Parte 1: OVR-6.4.8-05",
    "Parte 1: OVR-6.4.8-06", "Parte 1: OVR-6.4.8-07", "Parte 1: OVR-6.4.8-08", "Parte 1: OVR-6.4.8-09", "Parte 1: OVR-6.4.8-10",
    "Parte 1: OVR-6.4.8-11", "Parte 1: OVR-6.4.8-12", "Parte 1: OVR-6.4.8-13", "Parte 1: OVR-6.4.8-14A", "Parte 1: OVR-6.4.8-15",
    "Parte 1: OVR-6.4.8-16",
    # 6.4.9
    "Parte 1: OVR-6.4.9-01", "Parte 1: OVR-6.4.9-02", "Parte 1: OVR-6.4.9-03", "Parte 1: OVR-6.4.9-04",
    # 6.5.1
    "Parte 1: OVR-6.5.1-01", "Parte 1: GEN-6.5.1-02", "Parte 1: GEN-6.5.1-03", "Parte 1: GEN-6.5.1-04", "Parte 1: GEN-6.5.1-05",
    "Parte 1: GEN-6.5.1-06", "Parte 1: GEN-6.5.1-07", "Parte 1: GEN-6.5.1-08", "Parte 1: GEN-6.5.1-09", "Parte 1: GEN-6.5.1-10",
    "Parte 1: GEN-6.5.1-11", "Parte 1: GEN-6.5.1-12", "Parte 1: GEN-6.5.1-13", "Parte 1: GEN-6.5.1-13A", "Parte 1: GEN-6.5.1-13B",
    "Parte 1: GEN-6.5.1-14", "Parte 1: GEN-6.5.1-15", "Parte 1: DIS-6.5.1-16", "Parte 1: SDP-6.5.1-17", "Parte 1: SDP-6.5.1-18",
    "Parte 1: SDP-6.5.1-19", "Parte 1: SDP-6.5.1-20", "Parte 1: SDP-6.5.1-21", "Parte 1: SDP-6.5.1-22", "Parte 1: SDP-6.5.1-23",
    "Parte 1: SDP-6.5.1-24", "Parte 1: SDP-6.5.1-25",
    # 6.5.2
    "Parte 1: OVR-6.5.2-01", "Parte 1: OVR-6.5.2-02", "Parte 1: OVR-6.5.2-03", "Parte 1: GEN-6.5.2-04", "Parte 1: GEN-6.5.2-05",
    "Parte 1: GEN-6.5.2-06", "Parte 1: GEN-6.5.2-07", "Parte 1: GEN-6.5.2-08", "Parte 1: GEN-6.5.2-09", "Parte 1: OVR-6.5.2-10",
    "Parte 1: OVR-6.5.2-11", "Parte 1: OVR-6.5.2-12", "Parte 1: GEN-6.5.2-13",
    # 6.5.3
    "Parte 1: OVR-6.5.3-01", "Parte 1: OVR-6.5.3-02", "Parte 1: GEN-6.5.3-03", "Parte 1: GEN-6.5.3-04", "Parte 1: GEN-6.5.3-05",
    "Parte 1: GEN-6.5.3-06", "Parte 1: GEN-6.5.3-07",
    # 6.5.4
    "Parte 1: GEN-6.5.4-01", "Parte 1: SDP-6.5.4-02", "Parte 1: SDP-6.5.4-03",
    # 6.5.5
    "Parte 1: OVR-6.5.5-01A", "Parte 1: GEN-6.5.5-02", "Parte 1: GEN-6.5.5-03", "Parte 1: GEN-6.5.5-04", "Parte 1: DIS-6.5.5-05",
    "Parte 1: CSS-6.5.5-06", "Parte 1: OVR-6.5.5-07",
    # 6.5.6
    "Parte 1: OVR-6.5.6-01", "Parte 1: OVR-6.5.6-02",
    # 6.5.7
    "Parte 1: OVR-6.5.7-01", "Parte 1: OVR-6.5.7-02", "Parte 1: OVR-6.5.7-03", "Parte 1: OVR-6.5.7-04", "Parte 1: OVR-6.5.7-05",
    # 6.5.8
    "Parte 1: clausola 6.5.8",
    # 6.6.1
    "Parte 1: GEN-6.6.1-01", "Parte 1: GEN-6.6.1-02", "Parte 1: GEN-6.6.1-03", "Parte 1: GEN-6.6.1-04", "Parte 1: GEN-6.6.1-05",
    # 6.6.2
    "Parte 1: OVR-6.6.2-01",
    # 6.6.3
    "Parte 1: OVR-6.6.3-01", "Parte 1: CSS-6.6.3-01A", "Parte 1: CSS-6.6.3-01B", "Parte 1: OVR-6.6.3-02", "Parte 1: OVR-6.6.3-03",
    # 6.7
    "Parte 1: clausola 6.7",
    # 6.8.1-6.8.16
    "Parte 1: clausola 6.8.1", "Parte 1: OVR-6.8.2-01", "Parte 1: clausola 6.8.3", "Parte 1: OVR-6.8.4-01", "Parte 1: OVR-6.8.4-02",
    "Parte 1: OVR-6.8.4-03", "Parte 1: clausola 6.8.5", "Parte 1: OVR-6.8.6-01", "Parte 1: OVR-6.8.6-02", "Parte 1: clausola 6.8.7",
    "Parte 1: clausola 6.8.8", "Parte 1: clausola 6.8.9", "Parte 1: clausola 6.8.10", "Parte 1: clausola 6.8.11",
    "Parte 1: clausola 6.8.12", "Parte 1: OVR-6.8.13-01", "Parte 1: clausola 6.8.14", "Parte 1: OVR-6.8.15-01",
    "Parte 1: clausola 6.8.16",
    # 6.9.1
    "Parte 1: OVR-6.9.1-01", "Parte 1: OVR-6.9.1-02", "Parte 1: OVR-6.9.1-03", "Parte 1: OVR-6.9.1-04",
    # 6.9.2
    "Parte 1: OVR-6.9.2-01", "Parte 1: OVR-6.9.2-01A", "Parte 1: OVR-6.9.2-01B", "Parte 1: OVR-6.9.2-01C",
    # 6.9.3
    "Parte 1: OVR-6.9.3-01",
    # 6.9.4
    "Parte 1: OVR-6.9.4-01", "Parte 1: OVR-6.9.4-02", "Parte 1: OVR-6.9.4-03",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

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
