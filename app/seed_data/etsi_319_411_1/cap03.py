"""Estrazione granulare ETSI EN 319 411-1 V1.5.1 (2025-04) — Capitolo 3:
clausola 6.1 (Publication and repository responsibilities), 6.2
(Identification and authentication: 6.2.1 Naming, 6.2.2 Initial identity
validation, 6.2.3 Identification and authentication for Re-key requests,
6.2.4 per revocation requests) e 6.3 (Certificate Life-Cycle operational
requirements: 6.3.1-6.3.12, da Certificate application a Key escrow and
recovery).

Fonte 17 (numerazione definitiva cablata dalla sessione principale in
app/seed.py — questo modulo NON tocca seed.py). Testo ufficiale in
app/.source_cache/etsi_319_411_1/cap03.txt. Manifest di split:
app/.source_cache/etsi_319_411_1/manifest.json.

RIPETIZIONE DI UN TENTATIVO PRECEDENTE: la prima estrazione di questo
capitolo è stata interrotta da un crash del kernel del subagent (race
condition infrastrutturale, non un problema di contenuto) prima di
scrivere il file finale. Questo modulo è stato ricostruito da zero
ripercorrendo l'intero capitolo clausola per clausola.

RICOSTRUZIONE DI TESTO CORROTTO DALL'ESTRAZIONE PDF — clausola 6.3.9
(Certificate revocation and suspension): sia il testo cache del progetto
(cap03.txt/raw.txt) sia una rilettura diretta del PDF ufficiale ETSI
tramite conversione markdown presentano la stessa tabella di
CRL/CARL/short-term-certificate destrutturata dall'estrazione, con frasi
spezzate fuori dal loro ordine di lettura naturale. Risolto scaricando il
PDF ufficiale (ETSI EN 319 411-1 V1.5.1, 2025-04) ed estraendolo con
`pdftotext -layout` (che preserva l'ordine delle colonne), ottenendo testo
pulito e nell'ordine corretto per l'intera clausola 6.3.9; l'ordine
ricostruito è: REV-6.3.9-01 -> REV-6.3.9-02 (a, b+NOTE1, c) ->
REV-6.3.9-03+NOTE2 -> REV-6.3.9-04 -> blocco CRL (NOTE3, CSS-6.3.9-05,
CSS-6.3.9-06+NOTE4, CSS-6.3.9-07, CSS-6.3.9-08, CSS-6.3.9-09/10/11 Void) ->
blocco CARL (CSS-6.3.9-12, CSS-6.3.9-13, CSS-6.3.9-14) -> REV-6.3.9-15 ->
REV-6.3.9-15A+NOTE5+NOTE6 -> REV-6.3.9-16+NOTE7 -> REV-6.3.9-17 ->
REV-6.3.9-18 -> REV-6.3.9-19+NOTE8. La stessa estrazione pulita è stata
usata per ricontrollare l'intero capitolo (clausole 6.1, 6.2.1-6.2.4,
6.3.1-6.3.8, 6.3.10-6.3.12): nessun'altra sezione presenta questo tipo di
corruzione, il testo cache del progetto risulta affidabile altrove.

Modellazione (ADR-0007), stesso criterio già applicato agli altri
capitoli di questa fonte (cap01, cap02, cap04, cap05) e a ETSI EN 319 401/
ETSI TS 119 461 per capitoli tecnici ETSI a clausole/requisiti numerati
con prefisso <SIGLA>-<clausola>-<NN> (qui "DIS-", "REG-", "REV-", "GEN-",
"SDP-", "CSS-", "OVR-"):

- Ogni id di requisito numerato genera un nodo. Verbo "shall"/"shall not"
  -> Obbligo. "should"/"may" restano comunque Obbligo quando il requisito
  numerato ha un soggetto obbligato chiaramente identificabile (quasi
  sempre il TSP in questo capitolo) — stesso criterio già applicato in
  cap02.py (es. OVR-5.1-03 "should" -> Obbligo organizzativo) e cap05.py:
  "dichiarativo" nella regola "should/may/dichiarativo -> Principio"
  qualifica congiuntamente l'assenza di un soggetto obbligato, non il solo
  verbo. Principio "altro" resta riservato ai casi realmente privi di
  contenuto prescrittivo diretto: titoli di sottoclausola senza requisito
  proprio, premesse definitorie, requisiti "Void" con NOTE sostanziale.
- Elenchi a lettere a)/b)/c)... SENZA prefisso di requisito proprio
  restano nello stesso nodo del requisito che li introduce (es.
  REG-6.2.2-06 a)-b); REG-6.2.2-09 a)-g); REG-6.3.4-10A/11A a)-f)/a)-c);
  OVR-6.3.5-01 a)-j); GEN-6.3.3-12, liste CHOICE per policy).
- Frasi di transizione puramente strutturali ("In particular:", "When the
  subject is a natural person:", "Where CRLs...are used:", "Where the
  subscriber and subject are two separate entities...:") non generano
  contenuto proprio e non sono riportate: sono scaffolding editoriale del
  documento, non testo normativo (stesso criterio di cap04.py).
- **Requisiti "Void" senza NOTE con contenuto interpretativo proprio**
  (DIS-6.1-01/02/03/06/07; REG-6.2.2-02/03/04/11/14/14B/15/17/24/24A;
  REG-6.3.4-10/11/14/15; REG-6.3.6-01/03/04/05/09; REG-6.3.7-01/02;
  REG-6.3.8-01; REV-6.2.4-02/03/03B/04/05/06; CSS-6.3.9-09/10/11;
  GEN-6.3.3-04; SDP 6.3.3-09) -> NESSUN nodo, la numerazione del documento
  li salta. Eccezioni con NOTE sostanziale allegata -> Principio "altro"
  con il proprio id come riferimento: REG-6.3.1-02 (NOTE 3 sulla procedura
  a doppio controllo EVCG) e CSS-6.3.10-07 (NOTE 3 sui contesti in cui
  OCSP può essere obbligatorio).
- **Sottoclausole titolate senza alcun requisito numerato proprio** ->
  Principio "altro", riferimento "clausola 6.X" o "clausola 6.X (premessa)"
  quando il contenuto è la definizione concettuale che introduce clausole
  con requisiti propri: "Parte 1: clausola 6.2.1" (Naming, solo una NOTE di
  rinvio), "Parte 1: clausola 6.2.3" (Re-key: NOTE di rinvio a 6.3.7 + il proprio
  REG-6.2.3-01 Void, entrambi assorbiti in un unico nodo), "clausola 6.3.6
  (premessa)"/"Parte 1: clausola 6.3.7 (premessa)"/"Parte 1: clausola 6.3.8 (premessa)" (le
  NOTE definitorie di cosa siano rinnovo/re-key/modifica del certificato,
  sostanziali e non mero rinvio bibliografico), "Parte 1: clausola 6.3.11" (End of
  subscription: "No policy requirement.").
- NOTE/EXAMPLE annesse a un requisito: assorbite in `testo_integrale`
  quando aggiungono contenuto interpretativo/di eccezione sostanziale
  (es. NOTE 1 su REV-6.3.9-02 sul non dover monitorare il contenuto; NOTE
  su GEN-6.3.3-10 sull'eccezione DVCP al non-riassegnamento del DN; NOTE
  su SDP-6.3.12-03 sulla non preclusione della gestione delle chiavi per
  conto dell'utente); omesse quando sono puro rimando bibliografico o mera
  esemplificazione priva di condizione normativa aggiuntiva (NOTE 5/6/7 di
  REG-6.2.2-04/14B sul rinvio a BRG/EVCG per i metodi di verifica; EXAMPLE
  1 di REG-6.2.2-05C; EXAMPLE 2 di REG-6.2.2-18; EXAMPLE di
  OVR-6.3.5-03/6.3.10-09). **Eccezione ADR-0010**: l'EXAMPLE 2 di
  REG-6.3.1-00E (citazione della BRG relativa a OVCP) contiene, nel testo
  ufficiale stesso, due omissis tra parentesi quadre "[…]" propri della
  citazione — non un troncamento introdotto in estrazione. Poiché la
  guardia `verifica_completezza_testo_integrale` non ha un'eccezione
  codificata per questo caso (a differenza di Normattiva "((...))" e
  dell'estensibilità ASN.1), l'intero EXAMPLE illustrativo è stato omesso
  da `testo_integrale` (il requisito normativo di REG-6.3.1-00E resta
  comunque completo e verbatim).
- Marcature tra parentesi quadre ([CONDITIONAL], [CHOICE], [WEB], [NCP],
  [NCP+], [EVCP], [DVCP], [OVCP], [IVCP], "except [...]") mantenute in
  `testo_integrale`, sintetizzate in `condizione_applicabilita`, omesse
  dal solo `riferimento`.
- tipo_obbligo: "informativo/trasparenza" per la clausola 6.1
  (Publication and repository, per sua natura di divulgazione/
  disclosure) e per i requisiti di comunicazione/notifica verso
  sottoscrittore, soggetto o relying party (es. REV-6.3.9-03, OVR-6.3.5-03,
  CSS-6.3.10-09A/10); "tecnico/sicurezza" prevalente per 6.2 (identity
  validation) e 6.3.9/6.3.10 (revocation/status services), oltre ai
  requisiti crittografici/di gestione chiavi di 6.3.3/6.3.5/6.3.12;
  "organizzativo"/"procedurale" per il resto (documentazione di CP/CPS,
  rinvii di applicabilità a BRG/EVCG/EN 319 401, gestione degli accordi);
  "di conservazione" per REG-6.3.4-17 (conservazione dei registri per il
  periodo indicato al sottoscrittore).
- Categoria soggetto: default "QTSP/gestore" (obbligato) per la quasi
  totalità degli Obbligo, essendo il TSP l'attore quasi universale di
  questo capitolo — incluse le clausole che usano "the subscriber
  shall"/"the subject shall" come soggetto grammaticale (es.
  REG-6.2.2-21, "the subscriber shall provide a physical address"): il
  presente documento vincola il TSP (è il TSP che deve richiedere/
  garantire che il sottoscrittore fornisca l'informazione tramite il
  proprio processo di registrazione), non il sottoscrittore direttamente
  — stesso criterio universale già applicato in cap01/02/04/05.
  **Eccezione deliberata**: OVR-6.3.5-01 e OVR-6.3.5-02 ("The subscriber's
  obligations... shall include", "the subject's obligations shall comply
  with...") enumerano un catalogo di doveri sostanziali direttamente in
  capo al sottoscrittore/soggetto (protezione della chiave privata,
  obblighi di notifica) distinti dal dovere del TSP di includerli
  nell'accordo (già coperto separatamente da REG-6.3.4-07/08/10A/11A):
  modellati con soggetto obbligato "Utente/titolare" anziché "QTSP/
  gestore" — primo caso di questo tipo tra i capitoli di questa fonte,
  segnalato per revisione. Aggiunto "destinatario" esplicito solo dove il
  testo nomina espressamente il beneficiario di un obbligo informativo:
  "Utente/titolare" per REV-6.3.9-03 (comunicazione del cambio di stato al
  soggetto); "Terzi affidanti/pubblico" per OVR-6.3.5-03 (comunicazione
  alle relying party).
- RELAZIONI resta vuoto per vincolo di fase — nessuna relazione, né
  interna al capitolo né cross-capitolo (verso cap01/cap02/cap04/cap05 di
  questa stessa fonte) né cross-fonte (incluso il rinvio a ETSI EN 319 401,
  a BRG/EVCG del CA/Browser Forum, a ETSI TS 119 461/119 431-1/119 312, e
  ai numerosi rinvii interni verso clausole 6.4/6.5 di cap04.py, es.
  REG-6.4.5-03/04, OVR-6.4.1-01/6.4.2-01, SDP-6.5.1-21): riportati solo nel
  testo, mai come arco. Verrà eventualmente popolato dalla pipeline
  dedicata (ADR-0009) o da una cura editoriale successiva.

Dubbi di modellazione aperti per revisione umana:
- OVR-6.3.5-01/02 con soggetto obbligato "Utente/titolare" (v. sopra):
  verificare se preferibile comunque "QTSP/gestore" con "Utente/titolare"
  come destinatario, per coerenza stretta con il criterio "TSP quasi
  universale" degli altri capitoli, oppure se l'eccezione qui adottata sia
  preferibile perché più fedele al contenuto letterale (obblighi
  imposti al sottoscrittore/soggetto in quanto tali).
- REG-6.3.1-00E: l'EXAMPLE 2 illustrativo (citazione BRG su OVCP) è stato
  omesso interamente da `testo_integrale` per l'omissis "[…]" proprio
  della citazione originale, che la guardia ADR-0010 non riconosce come
  legittimo (a differenza di Normattiva/ASN.1); il requisito normativo
  resta comunque completo. Verificare se la guardia debba eventualmente
  essere estesa con una terza eccezione codificata per citazioni verbatim
  di altri standard che portano il proprio omissis, invece di richiedere
  l'omissione dell'intero EXAMPLE.

Conteggio finale: 151 Obbligo, 8 Principio (159 nodi totali), copertura
completa delle clausole 6.1-6.3.12 verificata da verifica_copertura.
"""

SOGGETTO_QTSP = [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}]
SOGGETTO_UTENTE_OBBLIGATO = [{"categoria": "Utente/titolare", "ruolo": "obbligato"}]

RIGHE_OBBLIGHI = [
    {
        "riferimento": "Parte 1: DIS-6.1-01A",
        "testo": "Il TSP deve rendere disponibili i certificati a sottoscrittori e soggetti.",
        "testo_integrale": "DIS-6.1-01A: The TSP shall make certificates available to subscribers and subjects.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: DIS-6.1-01B",
        "testo": "Il TSP può rendere disponibili i certificati alle relying party solo se è stato ottenuto il consenso del soggetto.",
        "testo_integrale": "DIS-6.1-01B: The TSP may make certificates available to relying parties only if subject's consent has been obtained.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Richiede il previo consenso del soggetto.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: DIS-6.1-01C",
        "testo": "Se il soggetto è un dispositivo o sistema, il consenso di cui a DIS-6.1-01B deve essere ottenuto dalla persona fisica o giuridica responsabile dell'esercizio del dispositivo o sistema, anziché dal soggetto.",
        "testo_integrale": "DIS-6.1-01C [CONDITIONAL]: If the subject is a device or system, the consent for DIS-6-1-01B shall be obtained from the natural or legal person responsible for operating the device or system, instead of the subject.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando il soggetto è un dispositivo o sistema.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: DIS-6.1-02A",
        "testo": "Il certificato completo e accurato deve essere disponibile per l'uso da parte del sottoscrittore o del soggetto o, se necessario, del TSP che gestisce la chiave privata per conto dell'utente; il certificato non deve necessariamente essere disponibile per l'uso immediatamente dopo la generazione.",
        "testo_integrale": "DIS-6.1-02A: The complete and accurate certificate shall be available for use by the subscriber or subject or, if needed, TSP managing the private key on behalf of the user. NOTE: The certificate does not need to be available for use immediately upon generation.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: DIS-6.1-04",
        "testo": "Il TSP deve rendere disponibili alle relying party i termini e le condizioni relativi all'uso del certificato.",
        "testo_integrale": "DIS-6.1-04: The TSP shall make available to relying parties the terms and conditions regarding the use of the certificate (see clause 6.9.4).",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: DIS-6.1-05",
        "testo": "I termini e le condizioni applicabili devono essere facilmente identificabili per un dato certificato.",
        "testo_integrale": "DIS-6.1-05: The applicable terms and conditions shall be readily identifiable for a given certificate.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: DIS-6.1-06A",
        "testo": "Per la policy LCP, le informazioni di cui a DIS-6.1-01A, DIS-6.1-01B e DIS-6.1-04 devono essere disponibili secondo quanto specificato nella CPS del TSP.",
        "testo_integrale": "DIS-6.1-06A [LCP]: The information identified in DIS-6.1-01A, DIS-6.1-01B and DIS-6.1-04 above shall be available as specified in the TSP's CPS.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy LCP.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: DIS-6.1-07A",
        "testo": "Per la policy NCP, le informazioni di cui a DIS-6.1-01A, DIS-6.1-01B e DIS-6.1-04 devono essere disponibili 24 ore su 24, 7 giorni su 7; in caso di guasto di sistema, di servizio o di altri fattori non sotto il controllo del TSP, il TSP deve adoperarsi al meglio affinché tale servizio informativo non risulti indisponibile per più del periodo massimo indicato nella CPS.",
        "testo_integrale": "DIS-6.1-07A [NCP]: The information identified in DIS-6.1-01A, DIS-6.1-01B and DIS-6.1-04 above shall be available 24 hours per day, 7 days per week. Upon system failure, service or other factors which are not under the control of the TSP, the TSP shall apply best endeavours to ensure that this information service is not unavailable for longer than a maximum period of time as denoted in the CPS.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: DIS-6.1-08",
        "testo": "Le informazioni di cui a DIS-6.1-04 dovrebbero essere disponibili pubblicamente e a livello internazionale.",
        "testo_integrale": "DIS-6.1-08: The information identified in DIS-6.1-04 above should be publicly and internationally available.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: DIS-6.1-09",
        "testo": "Se il TSP emette certificati pubblicamente fidati, le informazioni di cui a DIS-6.1-04 devono essere disponibili pubblicamente e a livello internazionale.",
        "testo_integrale": "DIS-6.1-09 [CONDITIONAL]: If the TSP is issuing publicly-trusted certificates, the information identified in DIS-6.1-04 above shall be publicly and internationally available.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se il TSP emette certificati pubblicamente fidati.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: DIS-6.1-10",
        "testo": "Per i cross certificate, il TSP dovrebbe divulgare pubblicamente tutti i Cross-Certified Subordinate CA Certificates che identificano la CA come soggetto, a condizione che il TSP abbia predisposto o accettato l'instaurazione del rapporto di fiducia.",
        "testo_integrale": "DIS-6.1-10: For cross certificates, the TSP should disclose publicly all Cross‐Certified Subordinate CA Certificates that identify the CA as the Subject, provided that the TSP arranged for or accepted the establishment of the trust relationship.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: DIS-6.1-10A",
        "testo": "Per la policy WEB, per i cross certificate, il TSP deve divulgare pubblicamente tutti i Cross-Certified Subordinate CA Certificates che identificano la CA come soggetto, a condizione che il TSP abbia predisposto o accettato l'instaurazione del rapporto di fiducia.",
        "testo_integrale": "DIS-6.1-10A [WEB]: For cross certificates, the TSP shall disclose publicly all Cross‐Certified Subordinate CA Certificates that identify the CA as the Subject, provided that the TSP arranged for or accepted the establishment of the trust relationship.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy WEB.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-01",
        "testo": "Il TSP deve verificare l'identità del sottoscrittore e del soggetto. In fase di registrazione, il soggetto è identificato come persona con specifici attributi, che possono indicare ad esempio un'associazione a un'organizzazione ed eventualmente un ruolo al suo interno; la validazione dell'identità fa parte di almeno uno dei seguenti processi: richiesta del certificato, emissione del certificato, fornitura del dispositivo al soggetto.",
        "testo_integrale": "REG-6.2.2-01: The TSP shall verify the identity of the subscriber and subject. NOTE 1: When registering, a subject is identified as a person with specific attributes. The specific attributes can indicate, for example, an association within an organization and possibly, a role within that organization. NOTE 2: Identity validation is part of at least one of processes: certificate application, certificate issuance, subject device provisioning.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-02A",
        "testo": "Il TSP deve raccogliere e validare prove dirette o un'attestazione da una fonte appropriata e autorizzata, dell'identità (es. nome) e, se applicabile, di qualsiasi attributo specifico dei soggetti a cui è rilasciato un certificato.",
        "testo_integrale": "REG-6.2.2-02A: The TSP shall collect and validate either direct evidence or an attestation from an appropriate and authorized source, of the identity (e.g. name) and if applicable, any specific attributes of subjects to whom a certificate is issued.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-02AB",
        "testo": "La raccolta di attributi e prove sull'identità del soggetto, nonché la loro validazione, dovrebbe avvenire secondo quanto specificato alle clausole 8.2 e 8.3 di ETSI TS 119 461; le prove presentate possono essere in forma cartacea o elettronica.",
        "testo_integrale": "REG-6.2.2-02AB: The collection of attributes and evidence on the subject's identity as well as their validation should be as specified in clauses 8.2 and 8.3 of ETSI TS 119 461 [15]. NOTE 3: Submitted evidence may be in the form of either paper or electronic documentation.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-02AC",
        "testo": "Il TSP deve verificare che le richieste di certificato siano accurate, autorizzate e complete secondo le prove raccolte o l'attestazione di identità.",
        "testo_integrale": "REG-6.2.2-02AC: The TSP shall check that certificate requests are accurate, authorized and complete according to the collected evidence or attestation of identity.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-02B",
        "testo": "La verifica dell'identità del soggetto deve avvenire al momento della registrazione con mezzi appropriati; la raccolta delle prove può includere la copia di dati personali come carta d'identità o passaporto, e le normative nazionali variano quanto alla necessità di archiviare tali informazioni a lungo termine (v. REG-6.2.2-18).",
        "testo_integrale": "REG-6.2.2-02B: Verification of the subject's identity shall be at time of registration by appropriate means. NOTE 4: The collection of evidence may include the copy of personal data, such as identity card or passport. National regulations vary as to whether it is necessary or not to archive this information as such over long term. See REG-6.2.2-18.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-03A",
        "testo": "Per la policy WEB, i metodi di verifica delle informazioni relative a nomi di dominio e indirizzi IP devono seguire quanto specificato alle clausole da 3.2.2.4 a 3.2.2.9 della BRG.",
        "testo_integrale": "REG-6.2.2-03A [WEB]: The verification methods for information relating to domain names and IP addresses shall follow those specified in clauses 3.2.2.4 to 3.2.2.9 of BRG [6].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy WEB.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-05",
        "testo": "Se il soggetto è una persona fisica, la prova dell'identità del soggetto (es. nome) deve essere verificata rispetto a tale persona fisica direttamente tramite presenza fisica (salvo che un sottoscrittore debitamente mandatato rappresenti il soggetto), oppure deve essere stata verificata indirettamente con mezzi che offrono un livello di garanzia equivalente alla presenza fisica.",
        "testo_integrale": "REG-6.2.2-05 [NCP] [CONDITIONAL]: If the subject is a natural person (i.e. physical person as opposed to legal person), evidence of the subject's identity (e.g. name) shall be checked against this natural person either directly by physical presence of the person (the subject shall be witnessed in person unless a duly mandated subscriber represents the subject), or shall have been checked indirectly using means which provides equivalent assurance to physical presence.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP quando il soggetto è una persona fisica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-05A",
        "testo": "Se la prova dell'identità è verificata rispetto alla presenza fisica della persona fisica, ciò dovrebbe avvenire secondo quanto specificato alla clausola 9.2.1 di ETSI TS 119 461 (\"casi d'uso con presenza fisica del richiedente\").",
        "testo_integrale": "REG-6.2.2-05A [NCP] [CONDITIONAL]: If evidence of the identity is checked against the physical presence of the natural person, this should be as specified in clause 9.2.1 of ETSI TS 119 461 [15] \"Use cases with physical presence of the applicant\".",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP quando la prova dell'identità è verificata tramite presenza fisica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-05B",
        "testo": "Se la prova dell'identità è verificata con mezzi che offrono un livello di garanzia equivalente alla presenza fisica, ciò dovrebbe avvenire secondo quanto specificato alle clausole 9.2.2 (identity proofing remoto assistito), 9.2.3 (identity proofing remoto non assistito), 9.2.4 (identity proofing tramite autenticazione con mezzi eID) o 9.2.5 (identity proofing tramite firma digitale con certificato) di ETSI TS 119 461.",
        "testo_integrale": "REG-6.2.2-05B [NCP] [CONDITIONAL]: If evidence of the identity is checked by means which provide equivalent assurance to physical presence, this should be as specified in clauses 9.2.2 \"Use cases for attended remote identity proofing\", 9.2.3 \"Use cases for unattended remote identity proofing\", 9.2.4 \"Use case for identity proofing by authentication using eID means\", or 9.2.5 \"Use case for identity proofing using digital signature with certificate\" of ETSI TS 119 461 [15].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP quando la prova dell'identità è verificata con mezzi equivalenti alla presenza fisica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-05C",
        "testo": "La prova dell'identità può essere fornita da una persona subappaltata che abbia verificato l'identità della persona in linea con i requisiti della presente clausola.",
        "testo_integrale": "REG-6.2.2-05C: Evidence of identity may be provided by a person subcontracted to have checked the persons' identity in line with the requirements of this clause.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-06",
        "testo": "Se il soggetto è una persona fisica, deve essere fornita prova di: a) nome completo (inclusi cognome e nomi coerenti con le prassi di identificazione nazionali); b) data e luogo di nascita, riferimento a un documento di identità riconosciuto a livello nazionale, o altri attributi utilizzabili per distinguere, per quanto possibile, la persona da altre con lo stesso nome.",
        "testo_integrale": "REG-6.2.2-06 [CONDITIONAL]: If the subject is a natural person (i.e. physical person as opposed to legal person), evidence shall be provided of: a) full name (including surname and given names consistent with the national identification practices); b) date and place of birth, reference to a nationally recognized identity document, or other attributes which can be used to, as far as possible, distinguish the person from others with the same name.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando il soggetto è una persona fisica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-07",
        "testo": "Se il soggetto è una persona fisica, il luogo di nascita dovrebbe essere indicato secondo le convenzioni nazionali o altre convenzioni applicabili per la registrazione delle nascite.",
        "testo_integrale": "REG-6.2.2-07 [CONDITIONAL]: If the subject is a natural person (i.e. physical person as opposed to legal person), the place of birth should be given in accordance with national or other applicable conventions for registering births.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando il soggetto è una persona fisica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-08",
        "testo": "Se il soggetto è una persona fisica identificata in associazione a una persona giuridica (es. il sottoscrittore), la prova dell'identità, in particolare quelle elencate in REG-6.2.2-09, deve essere verificata rispetto a tale persona fisica direttamente tramite presenza fisica (salvo che un sottoscrittore debitamente mandatato rappresenti il soggetto), oppure deve essere stata verificata indirettamente con mezzi che offrono un livello di garanzia equivalente alla presenza fisica.",
        "testo_integrale": "REG-6.2.2-08 [NCP] [CONDITIONAL]: If the subject is a natural person who is identified in association with a legal person (e.g. the subscriber), evidence of the identity, in particular the ones listed in REG-6.2.2-09, shall be checked against a natural person either directly by physical presence of the person (the subject shall be witnessed in person unless a duly mandated subscriber represents the subject), or shall have been checked indirectly using means which provides equivalent assurance to physical presence.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP quando il soggetto è una persona fisica identificata in associazione a una persona giuridica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-08A",
        "testo": "La prova dell'identità dovrebbe avvenire secondo quanto specificato alla clausola 9.4 di ETSI TS 119 461 (\"caso d'uso per l'identity proofing di persona fisica rappresentante una persona giuridica\").",
        "testo_integrale": "REG-6.2.2-08A [NCP]: The evidence of the identity should be as specified in clause 9.4 of ETSI TS 119 461 [15]: \"Use case for identity proofing of natural person representing legal person\".",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-09",
        "testo": "Se il soggetto è una persona fisica identificata in associazione a una persona giuridica (es. il sottoscrittore), deve essere fornita prova di: a) nome completo del soggetto; b) data e luogo di nascita, riferimento a un documento di identità riconosciuto, o altri attributi del sottoscrittore utilizzabili per distinguere la persona da altre con lo stesso nome; c) nome completo e status giuridico della persona giuridica o altra entità organizzativa associata (es. il sottoscrittore); d) informazioni di registrazione esistenti e pertinenti (es. registrazione societaria) della persona giuridica o entità organizzativa associata; e) affiliazione della persona fisica alla persona giuridica; f) quando applicabile, l'associazione tra la persona giuridica e qualsiasi entità organizzativa associata che comparirebbe nell'attributo organization del certificato; e g) approvazione da parte della persona giuridica e della persona fisica del fatto che gli attributi del soggetto identificano anche tale organizzazione.",
        "testo_integrale": "REG-6.2.2-09 [CONDITIONAL]: If the subject is a natural person who is identified in association with a legal person (e.g. the subscriber), evidence shall be provided of: a) full name (including surname and given names, consistently with the national or other applicable identification practices) of the subject; b) date and place of birth, reference to a nationally recognized identity document, or other attributes of the subscriber which can be used to, as far as possible, distinguish the person from others with the same name; c) full name and legal status of the associated legal person or other organizational entity (e.g. the subscriber); d) any relevant existing registration information (e.g. company registration) of the associated legal person or other organizational entity identified in association with the legal person, consistent with the national or other applicable identification practices; e) affiliation of the natural person to the legal person consistent with national or other applicable identification practices; f) [CONDITIONAL]: when applicable, the association between the legal person and any organizational entity identified in association with this legal person that would appear in the organization attribute of the certificate, consistent with the national or other applicable identification practices; and g) approval by the legal person and the natural person that the subject attributes also identify such organization.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando il soggetto è una persona fisica identificata in associazione a una persona giuridica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-10",
        "testo": "Se il soggetto è una persona giuridica, o altra entità organizzativa identificata in associazione a una persona giuridica, la prova dell'identità, in particolare quelle elencate in REG-6.2.2-12, deve essere verificata rispetto a un sottoscrittore debitamente mandatato direttamente, tramite presenza fisica di una persona autorizzata a rappresentare la persona giuridica, oppure deve essere stata verificata indirettamente con mezzi che offrono un livello di garanzia equivalente alla presenza fisica.",
        "testo_integrale": "REG-6.2.2-10 [NCP] except [EVCP] [CONDITIONAL]: If the subject is a legal person, or other organizational entity identified in association with a legal person, evidence of the identity, in particular the ones listed in REG-6.2.2-12, shall be checked against a duly mandated subscriber either directly, by physical presence of a person allowed to represent the legal person, or shall have been checked indirectly using means which provides equivalent assurance to physical presence.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP, esclusa EVCP, quando il soggetto è una persona giuridica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-10A",
        "testo": "La prova dell'identità dovrebbe avvenire secondo quanto specificato alla clausola 9.4 di ETSI TS 119 461 (\"caso d'uso per l'identity proofing di persona fisica rappresentante una persona giuridica\").",
        "testo_integrale": "REG-6.2.2-10A [NCP]: The evidence of the identity should be as specified in clause 9.4 of ETSI TS 119 461 [15]: \"Use case for identity proofing of natural person representing legal person\".",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-12",
        "testo": "Se il soggetto è una persona giuridica, o altra entità organizzativa identificata in associazione a una persona giuridica, deve essere fornita prova di: a) nome completo dell'entità organizzativa (organizzazione privata, ente governativo, entità commerciale o non commerciale) coerente con le prassi di identificazione applicabili; b) quando applicabile, l'associazione tra la persona giuridica e l'altra entità organizzativa associata che comparirebbe nell'attributo organization del certificato.",
        "testo_integrale": "REG-6.2.2-12 [CONDITIONAL]: If the subject is a legal person, or other organizational entity identified in association with a legal person, evidence shall be provided of: a) Full name of the organizational entity (private organization, government entity, business entity or non-commercial entity) consistent with the national or other applicable identification practices. b) [CONDITIONAL]: when applicable, the association between the legal person and the other organizational entity identified in association with this legal person that would appear in the organization attribute of the certificate, consistent with the national or other applicable identification practices.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando il soggetto è una persona giuridica o entità organizzativa associata.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-13",
        "testo": "Se il soggetto è un dispositivo o sistema operato da o per conto di una persona giuridica, o altra entità organizzativa identificata in associazione a una persona giuridica, la prova dell'identità, in particolare quelle elencate in REG-6.2.2-15A, deve essere verificata rispetto a un sottoscrittore debitamente mandatato direttamente, tramite presenza fisica di una persona, oppure deve essere stata verificata indirettamente con mezzi che offrono un livello di garanzia equivalente alla presenza fisica.",
        "testo_integrale": "REG-6.2.2-13 [NCP] except [EVCP] [CONDITIONAL]: If the subject is a device or system operated by or on behalf of a legal person, or other organizational entity identified in association with a legal person, evidence of the identity, in particular the ones listed in REG-6.2.2-15A, shall be checked against a duly mandated subscriber either directly, by physical presence of a person, or shall have been checked indirectly using means which provides equivalent assurance to physical presence.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP, esclusa EVCP, quando il soggetto è un dispositivo o sistema operato per conto di una persona giuridica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-13A",
        "testo": "La prova dell'identità dovrebbe avvenire secondo quanto specificato alla clausola 9.4 di ETSI TS 119 461 (\"caso d'uso per l'identity proofing di persona fisica rappresentante una persona giuridica\").",
        "testo_integrale": "REG-6.2.2-13A [NCP]: The evidence of the identity should be as specified in clause 9.4 of ETSI TS 119 461 [15]: \"Use case for identity proofing of natural person representing legal person\".",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-14A",
        "testo": "Per la policy EVCP, se il soggetto è un dispositivo o sistema operato da o per conto di una persona giuridica, o altra entità organizzativa identificata in associazione a una persona giuridica, la prova dell'identità, in particolare quelle elencate in REG-6.2.2-15A, deve essere verificata rispetto a un sottoscrittore debitamente mandatato direttamente, tramite presenza fisica di una persona, oppure deve essere stata verificata indirettamente con mezzi che offrono un livello di garanzia equivalente alla presenza fisica, con l'eccezione della verifica del nome assunto.",
        "testo_integrale": "REG-6.2.2-14A [EVCP] [CONDITIONAL]: If the subject is a device or system operated by or on behalf of a legal person, or other organizational entity identified in association with a legal person, evidence of the identity, in particular the ones listed in REG-6.2.2-15A, shall be checked against a duly mandated subscriber either directly, by physical presence of a person, or shall have been checked indirectly using means which provides equivalent assurance to physical presence with the exception of the verification of assumed name.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy EVCP quando il soggetto è un dispositivo o sistema operato per conto di una persona giuridica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-15A",
        "testo": "Salvo che per la policy DVCP, se il soggetto è un dispositivo o sistema operato da o per conto di una persona giuridica, o altra entità organizzativa identificata in associazione a una persona giuridica, deve essere fornita prova di: a) identificatore del dispositivo tramite cui può essere referenziato (es. nome di dominio Internet); b) nome completo dell'entità organizzativa; c) qualsiasi informazione di registrazione esistente e pertinente (es. registrazione societaria) della persona giuridica o entità organizzativa associata che comparirebbe nell'attributo organization del certificato; d) un numero identificativo riconosciuto a livello nazionale, o altri attributi utilizzabili per distinguere l'entità organizzativa da altre con lo stesso nome; ed e) quando applicabile, l'associazione tra la persona giuridica e l'altra entità organizzativa associata che comparirebbe nell'attributo organization del certificato.",
        "testo_integrale": "REG-6.2.2-15A except [DVCP] [CONDITIONAL]: If the subject is a device or system operated by or on behalf of a legal person, or other organizational entity identified in association with a legal person, evidence shall be provided of: a) identifier of the device by which it can be referenced (e.g. Internet domain name); b) full name of the organizational entity; c) any relevant existing registration information (e.g. company registration) of the legal person or other organizational entity identified in association with the legal person that would appear in the organization attribute of the certificate, consistent with the national or other applicable identification practices; d) a nationally recognized identity number, or other attributes which can be used to, as far as possible, distinguish the organizational entity from others with the same name; and e) [CONDITIONAL]: when applicable, the association between the legal person and the other organizational entity identified in association with this legal person that would appear in the organization attribute of the certificate, consistent with the national or other applicable identification practices.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica a tutte le policy salvo DVCP, quando il soggetto è un dispositivo o sistema operato per conto di una persona giuridica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-16",
        "testo": "Se il soggetto è un dispositivo o sistema operato da una persona fisica, la prova dell'identità, in particolare quelle elencate in REG-6.2.2-17A, deve essere verificata rispetto a tale persona fisica direttamente, tramite presenza fisica della persona fisica, oppure deve essere stata verificata indirettamente con mezzi che offrono un livello di garanzia equivalente alla presenza fisica.",
        "testo_integrale": "REG-6.2.2-16 [NCP] [CONDITIONAL]: If the subject is a device or system operated by a natural person, evidence of the identity, in particular the ones listed in REG-6.2.2-17A, shall be checked against a natural person either directly, by physical presence of the natural person, or shall have been checked indirectly using means which provides equivalent assurance to physical presence.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP quando il soggetto è un dispositivo o sistema operato da una persona fisica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-16A",
        "testo": "Se la prova dell'identità è verificata rispetto alla presenza fisica della persona fisica, ciò dovrebbe avvenire secondo quanto specificato alla clausola 9.2.1 di ETSI TS 119 461 (\"casi d'uso con presenza fisica del richiedente\").",
        "testo_integrale": "REG-6.2.2-16A [NCP] [CONDITIONAL]: If evidence of the identity is checked against the physical presence of the natural person, this should be as specified in clause 9.2.1 of ETSI TS 119 461 [15] \"Use cases with physical presence of the applicant\".",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP quando la prova dell'identità è verificata tramite presenza fisica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-16B",
        "testo": "Se la prova dell'identità è verificata con mezzi che offrono un livello di garanzia equivalente alla presenza fisica, ciò dovrebbe avvenire secondo quanto specificato alle clausole 9.2.2, 9.2.3, 9.2.4 o 9.2.5 di ETSI TS 119 461.",
        "testo_integrale": "REG-6.2.2-16B [NCP] [CONDITIONAL]: If evidence of the identity is checked by means which provide equivalent assurance to physical presence, this should be as specified in clauses 9.2.2 \"Use cases for attended remote identity proofing\", 9.2.3 \"Use cases for unattended remote identity proofing\", 9.2.4 \"Use case for identity proofing by authentication using eID means\", or 9.2.5 \"Use case for identity proofing using digital signature with certificate\" of ETSI TS 119 461 [15].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP quando la prova dell'identità è verificata con mezzi equivalenti alla presenza fisica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-17A",
        "testo": "Salvo che per la policy DVCP, se il soggetto è un dispositivo o sistema operato da una persona fisica, deve essere fornita prova di: a) identificatore del dispositivo tramite cui può essere referenziato (es. nome di dominio Internet); b) un numero identificativo riconosciuto a livello nazionale, o altri attributi utilizzabili per distinguere la persona fisica da altre con lo stesso nome.",
        "testo_integrale": "REG-6.2.2-17A except [DVCP] [CONDITIONAL]: If the subject is a device or system operated by a natural person, evidence shall be provided of: a) identifier of the device by which it can be referenced (e.g. Internet domain name); b) a nationally recognized identity number, or other attributes which can be used to, as far as possible, distinguish the natural person from others with the same name.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica a tutte le policy salvo DVCP, quando il soggetto è un dispositivo o sistema operato da una persona fisica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-18",
        "testo": "Il TSP deve registrare tutte le informazioni necessarie a verificare l'identità del soggetto e, se applicabile, ogni attributo specifico del soggetto, incluso qualsiasi numero di riferimento sulla documentazione usata per la verifica e qualsiasi limitazione sulla sua validità; per rispettare REG-6.4.5-03 e REG-6.4.5-04 il TSP non deve necessariamente archiviare a lungo termine tutti i dati raccolti in fase di registrazione, e può limitarsi a un riferimento alla documentazione usata in quel momento.",
        "testo_integrale": "REG-6.2.2-18: The TSP shall record all the information necessary to verify the subject's identity and if applicable, any specific attributes of the subject, including any reference number on the documentation used for verification, and any limitations on its validity. NOTE 8: In order to comply with REG-6.4.5-03 and REG-6.4.5-04 below, the TSP does not need to archive all data collected during the registration over long term, and can limit the record to a reference to the documentation used at that time.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-19",
        "testo": "Se un'entità diversa dal soggetto sottoscrive i servizi del TSP (ossia sottoscrittore e soggetto sono entità separate, v. clausola 5.4.2), deve essere fornita prova che il sottoscrittore è autorizzato ad agire per il soggetto come identificato, in particolare: a) nome completo del sottoscrittore; b) quando il sottoscrittore rappresenta una persona fisica (non associata a una persona giuridica), un accordo su tale rappresentanza; oppure, quando il sottoscrittore rappresenta una persona giuridica, un accordo che il sottoscrittore è autorizzato a rappresentare la persona giuridica e a richiedere certificati per essa o i suoi membri.",
        "testo_integrale": "REG-6.2.2-19 [CONDITIONAL]: If an entity other than the subject is subscribing to the TSP's services (i.e. the subscriber and subject are separate entities - see clause 5.4.2), evidence shall be provided that the subscriber is authorized to act for the subject as identified (e.g. is authorized for all members of the identified organization), in particular: a) full name (including surname and given names consistent with the national or other applicable identification practices) of the subscriber; b) [CHOICE]: when the subscriber represents a natural person (not associated with a legal person) an agreement to this representation; or when the subscriber represents a legal person (either for requesting a certificate for that legal person or to request a certificate for a natural person identified in association with the legal person), an agreement that the subscriber is allowed to represent the legal person and is entitled to request certificates for that legal person or its members.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando sottoscrittore e soggetto sono entità separate; il punto b) è a scelta alternativa (CHOICE) secondo il tipo di soggetto rappresentato.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-20",
        "testo": "Se un'entità diversa dal soggetto sottoscrive i servizi del TSP e il sottoscrittore non è una persona fisica, esso deve essere rappresentato da una persona fisica la cui autorizzazione a rappresentare il sottoscrittore deve essere comprovata.",
        "testo_integrale": "REG-6.2.2-20 [CONDITIONAL]: If an entity other than the subject is subscribing to the TSP's services (i.e. the subscriber and subject are separate entities - see clause 5.4.2) and if the subscriber is not a natural person, it shall be represented by a natural person whose authorization to represent the subscriber shall be proved.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando sottoscrittore e soggetto sono entità separate e il sottoscrittore non è una persona fisica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-21",
        "testo": "Il sottoscrittore deve fornire un indirizzo fisico, o altri attributi, che descrivano come il sottoscrittore può essere contattato.",
        "testo_integrale": "REG-6.2.2-21: The subscriber shall provide a physical address, or other attributes, which describe how the subscriber shall be contacted.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-22",
        "testo": "Il TSP deve fornire prova di come rispetta la normativa applicabile in materia di protezione dei dati nell'ambito del proprio processo di registrazione.",
        "testo_integrale": "REG-6.2.2-22: The TSP shall provide evidence of how they meet applicable data protection legislation within their registration process.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-23",
        "testo": "La policy di verifica del TSP deve richiedere la raccolta di prove di identità solo nella misura sufficiente a soddisfare i requisiti dell'uso previsto del certificato.",
        "testo_integrale": "REG-6.2.2-23: The TSP's verification policy shall only require the capture of evidence of identity sufficient to satisfy the requirements of the intended use of the certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-25",
        "testo": "I certificati che un TSP emette per sé stesso o per persone ad esso appartenenti (come soggetto) devono essere richiesti, validati e gestiti secondo i processi definiti dal TSP per il tipo di certificato selezionato.",
        "testo_integrale": "REG-6.2.2-25: Certificates that a TSP issues for itself or persons belonging to it (as a subject) shall be requested, validated and handled according to the TSP's defined processes for the selected type of certificates.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.2.2-26",
        "testo": "Il responsabile della registrazione (Registration Officer) che verifica l'identità non deve essere la persona fisica a cui è rilasciato il certificato (come soggetto).",
        "testo_integrale": "REG-6.2.2-26: The Registration Officer(s) that verifies the identity shall not be the natural person to whom the certificate is issued to (as a subject).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.2.4-01",
        "testo": "Il TSP deve documentare nella propria CPS le procedure per la revoca dei certificati di utente finale e di CA, includendo: a) chi può presentare richieste di revoca o segnalazioni di eventi che possano indicare la necessità di revocare un certificato; b) come possono essere presentate; c) eventuali requisiti per la conferma successiva delle richieste di revoca o delle segnalazioni; d) se e per quali motivi i certificati possono essere sospesi o revocati; e) il meccanismo usato per diffondere le informazioni sullo stato di revoca; f) il ritardo massimo tra la ricezione di una richiesta di revoca o sospensione e la disponibilità della decisione di modifica dello stato alle relying party; g) il ritardo massimo tra la conferma della revoca o sospensione e l'effettiva modifica dello stato resa disponibile alle relying party.",
        "testo_integrale": "REV-6.2.4-01: The TSP shall document as part of its CPS (see clause 5.2) the procedures for revocation of end user and CA certificates including: a) Who can submit requests for revocation or reports of events which may indicate the need to revoke a certificate. b) How they can be submitted. c) Any requirements for subsequent confirmation of requests for revocation or reports of events which may indicate the need to revoke a certificate. EXAMPLE 1: Confirmation can be required from the subscriber if a compromise is reported by a third party. d) Whether and for what reasons certificates can be suspended or revoked. e) The mechanism used for distributing revocation status information. f) The maximum delay between receipt of a revocation or suspension request and the decision to change its status information being available to all relying parties. g) The maximum delay between the confirmation of the revocation of a certificate, or its suspension, to become effective and the actual change of the status information of this certificate being made available to relying parties.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.2.4-03A",
        "testo": "Il ritardo massimo tra la ricezione di una richiesta di revoca o sospensione del certificato e l'effettiva disponibilità della modifica delle informazioni sullo stato del certificato per tutte le relying party deve essere al massimo di 24 ore.",
        "testo_integrale": "REV-6.2.4-03A: The maximum delay between receipt of a certificate revocation or suspension request and the actual change of the certificate status information being available to all relying parties shall be at most 24 hours.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.2.4-03BA",
        "testo": "La CPS del TSP deve specificare la o le procedure eccezionali da seguire nel caso in cui la richiesta di revoca non possa essere confermata entro 24 ore.",
        "testo_integrale": "REV-6.2.4-03BA: The TSP's CPS shall specify exception procedure(s) to be followed in case the revocation request cannot be confirmed within 24 hours.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.2.4-03BB",
        "testo": "Se la revoca non può essere confermata entro 24 ore, le azioni intraprese, insieme alla motivazione, devono essere registrate.",
        "testo_integrale": "REV-6.2.4-03BB [CONDITIONAL]: If the revocation cannot be confirmed within 24 hours, the actions taken along with the justification, shall be recorded.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando la revoca non può essere confermata entro 24 ore.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.2.4-03C",
        "testo": "Se un TSP supporta sia CRL sia un servizio di stato del certificato online per fornire informazioni sullo stato di revoca e vi sono o possono esservi ritardi diversi nell'aggiornamento delle informazioni per ciascun metodo, il ritardo massimo di 24 ore deve applicarsi a entrambi i metodi.",
        "testo_integrale": "REV-6.2.4-03C [CONDITIONAL]: If a TSP supports both CRL and on-line certificate status service to provide revocation status and delays in updating the status information for all the methods exist or are possible, the maximum delay of 24 hours shall apply to both methods.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando il TSP supporta sia CRL sia un servizio di stato online.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.2.4-05A",
        "testo": "Se la richiesta di revoca prevede la revoca a una data futura (es. cessazione pianificata delle funzioni del soggetto a una certa data), la data programmata può essere considerata come il momento in cui si è verificata la ricezione della richiesta.",
        "testo_integrale": "REV-6.2.4-05A [CONDITIONAL]: If the revocation request requires revocation at a future date (e.g. subject's planned cessation from his/her duties at a certain date), then the scheduled date may be considered as the time at which receipt of the request has occurred.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando la richiesta di revoca prevede una revoca a data futura.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.2.4-06A",
        "testo": "Un TSP può prevedere tempi di elaborazione più rapidi rispetto al termine richiesto in REV-6.2.4-03A per determinati motivi di revoca.",
        "testo_integrale": "REV-6.2.4-06A: A TSP may give faster process times than the time required in REV-6.2.4-03A for certain revocation reasons.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.2.4-07",
        "testo": "L'orario usato per la fornitura dei servizi di revoca deve essere sincronizzato con l'UTC almeno una volta ogni 24 ore.",
        "testo_integrale": "REV-6.2.4-07: The time used for the provision of revocation services shall be synchronized with UTC at least once every 24 hours.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.2.4-08",
        "testo": "Le richieste di revoca e le segnalazioni di eventi relativi alla revoca devono essere elaborate al momento della ricezione (es. compromissione della chiave privata del soggetto, decesso del soggetto, cessazione imprevista dell'accordo o delle funzioni aziendali del sottoscrittore/soggetto, violazione di obblighi contrattuali).",
        "testo_integrale": "REV-6.2.4-08: Requests for revocation and reports of events relating to revocation shall be processed on receipt. EXAMPLE 2: Compromise of subject's private key, death of the subject, unexpected termination of a subscriber's or subject's agreement or business functions, violation of contractual obligations.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.2.4-09",
        "testo": "Le richieste di revoca e le segnalazioni di eventi relativi alla revoca devono essere autenticate e verificate come provenienti da una fonte autorizzata; tali segnalazioni e richieste saranno confermate secondo quanto richiesto dalle prassi del TSP.",
        "testo_integrale": "REV-6.2.4-09: Requests for revocation and reports of events relating to revocation shall be authenticated, checked to be from an authorized source. NOTE 2: Such reports and requests will be confirmed as required under the TSP's practices.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.1-00A",
        "testo": "I requisiti della presente clausola si applicano tanto all'emissione iniziale del certificato quanto al rinnovo, al re-key e alla modifica del certificato. Il sottoscrittore deve essere stato registrato secondo la clausola 6.2.2, e l'identità del sottoscrittore e del soggetto deve essere stata validata di conseguenza.",
        "testo_integrale": "NOTE 1: The requirements in this clause apply to initial certificate issuance as well as to certificate renewal, re-key, and modification. REG-6.3.1-00A: The subscriber shall have been registered as per clause 6.2.2, and the subscriber and subject's identity validated accordingly.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.1-00B",
        "testo": "Gli attributi del soggetto e le altre informazioni nel certificato da emettere devono essere valutati come corretti al momento dell'emissione del certificato; ciò è importante per gli attributi che possono cambiare nel tempo, specialmente quando il momento dell'emissione non è immediatamente successivo alla validazione iniziale dell'identità.",
        "testo_integrale": "REG-6.3.1-00B: The subject's attributes and other information in the certificate to be issued shall be assessed to be correct at the time of issuing the certificate. NOTE 2: This is important for attributes that may change over time, especially when the time of issuance of the certificate is not immediately after the initial identity validation.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.1-00C",
        "testo": "Il processo usato per la verifica iniziale dell'identità e degli attributi del soggetto deve essere ancora un processo applicabile per l'identity proofing secondo la CPS al momento dell'emissione del certificato; certi metodi non più usati possono comunque essere considerati validi, ma un metodo non più usato per motivi di sicurezza è da considerarsi non valido e non può essere utilizzato per emettere il certificato.",
        "testo_integrale": "REG-6.3.1-00C: The process used for initial verification of the subject's identity and attributes shall still be an applicable process for identity proofing as per the CPS at the time issuing the certificate. EXAMPLE 1: Certain methods not used anymore can still be considered valid, but a method not used anymore because of security concerns is to be considered as invalid and cannot be relied upon to issue certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.1-00D",
        "testo": "Il TSP deve specificare nella propria CP/CPS per quanto tempo un certificato può essere emesso dopo la validazione iniziale dell'identità, senza una nuova validazione dell'identità del sottoscrittore e del soggetto secondo la clausola 6.2.2.",
        "testo_integrale": "REG-6.3.1-00D: The TSP shall specify in its CP/CPS how much time a certificate is allowed to be issued after the initial identity validation, without a new identity validation of the subscriber and subject according to clause 6.2.2.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.1-00E",
        "testo": "Il TSP deve specificare nella propria CP/CPS al massimo con quale frequenza e/o a quali condizioni un certificato può essere emesso dopo la validazione iniziale dell'identità senza una nuova validazione del sottoscrittore e del soggetto secondo la clausola 6.2.2.",
        "testo_integrale": "REG-6.3.1-00E: The TSP shall specify in its CP/CPS at most how often and/or under which conditions a certificate is allowed to be issued after the initial identity validation without a new identity validation of the subscriber and subject according to clause 6.2.2.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.1-00F",
        "testo": "Se il sottoscrittore e il soggetto non coincidono, il sottoscrittore deve autorizzare l'emissione del certificato al soggetto.",
        "testo_integrale": "REG-6.3.1-00F [CONDITONAL]: If the subscriber and the subject are not the same, the subscriber shall authorize the issuance of the certificate to the subject.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando sottoscrittore e soggetto non coincidono.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.1-01",
        "testo": "Se la coppia di chiavi del soggetto non è generata dalla CA, il processo di richiesta del certificato deve fornire una ragionevole garanzia che il soggetto possieda o controlli la chiave privata associata alla chiave pubblica presentata per la certificazione.",
        "testo_integrale": "REG-6.3.1-01 [CONDITIONAL]: If the subject's key pair is not generated by the CA, the certificate request process shall provide reasonable assurance that the subject has possession or control of the private key associated with the public key presented for certification.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando la coppia di chiavi del soggetto non è generata dalla CA.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.3.2-00A",
        "testo": "I requisiti della presente clausola si applicano tanto all'emissione iniziale del certificato quanto al rinnovo, al re-key e alla modifica del certificato. La procedura di emissione del certificato deve essere collegata in modo sicuro e inequivocabile alla relativa registrazione, inclusa l'identificazione del soggetto e la fornitura di qualsiasi chiave pubblica generata da un attore diverso dal TSP.",
        "testo_integrale": "NOTE 1: The requirements in this clause apply to initial certificate issuance as well as to certificate renewal, re-key, and modification. GEN-6.3.2-00A: The procedure of issuing the certificate shall be securely and unambiguously linked to the associated registration, including the identification of the subject and the provision of any public key generated by another actor than the TSP.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.2-00B",
        "testo": "Il TSP deve verificare che le richieste di certificato siano accurate, autorizzate e complete secondo le prove raccolte o l'attestazione di identità di cui alla clausola 6.2.2.",
        "testo_integrale": "REG-6.3.2-00B: The TSP shall check that certificate requests are accurate, authorized and complete according to the collected evidence or attestation of identity as in clause 6.2.2.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.2-01",
        "testo": "La richiesta di certificati deve provenire da una fonte fidata e autorizzata, come un servizio di registrazione o un sottoscrittore debitamente autenticato e già registrato; i requisiti generali sulla sicurezza del TSP (risorse umane, sicurezza operativa, reti e privacy, clausole 6.4.4, 6.5.6, 6.5.7 e 6.8.4) si applicano anche alle registration authority esterne. Ad esempio, se la richiesta di certificazione proviene dal sottoscrittore, il metodo di autenticazione del sottoscrittore può essere un mezzo eID o un altro mezzo di autenticazione associato al sottoscrittore durante la validazione iniziale dell'identità, o un certificato valido già emesso al soggetto.",
        "testo_integrale": "REG-6.3.2-01: Application for certificates shall be from a trusted and authorized source such as a registration service or a duly authenticated subscriber previously registered. NOTE 2: General requirements on the security of the TSP including human resources, operational security, and networks and privacy as specified in clauses 6.4.4, 6.5.6, 6.5.7 and 6.8.4 apply to external registration authorities. EXAMPLE: In case the certification application comes from the subscriber, the subscriber's authentication method can be an eID means or another authentication means associated with the subscriber during the initial identity validation, or a valid certificate already issued to the subject.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.2-02",
        "testo": "Quando sono utilizzati fornitori esterni di servizi di registrazione, i dati di registrazione devono essere scambiati in modo sicuro e solo con fornitori di servizi di registrazione riconosciuti, la cui identità è autenticata.",
        "testo_integrale": "REG-6.3.2-02 [CONDITIONAL]: When external registration service providers are used registration data shall be exchanged securely and only with recognized registration service providers, whose identity is authenticated.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando sono utilizzati fornitori esterni di servizi di registrazione.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.3.3-01",
        "testo": "La CA deve emettere i certificati in modo sicuro per mantenerne l'autenticità (v. clausola 6.6.1 per i profili di certificato).",
        "testo_integrale": "See clause 6.6.1 for certificate profiles. GEN-6.3.3-01: The CA shall issue certificates securely to maintain their authenticity.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.3.3-02",
        "testo": "La CA deve adottare misure contro la falsificazione dei certificati.",
        "testo_integrale": "GEN-6.3.3-02: The CA shall take measures against forgery of certificates.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.3.3-02A",
        "testo": "Per la policy NCP, la CA dovrebbe introdurre casualità nel numero di serie del certificato.",
        "testo_integrale": "GEN-6.3.3-02A [NCP]: The CA should introduce randomness in certificate's serial number.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.3.3-03",
        "testo": "Nei casi in cui la CA genera la coppia di chiavi dei soggetti, la CA deve garantire la riservatezza durante il processo di generazione di tali dati.",
        "testo_integrale": "GEN-6.3.3-03 [CONDITONAL]: In cases where the CA generates the subjects' key pair, the CA shall guarantee confidentiality during the process of generating such data.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando la CA genera la coppia di chiavi dei soggetti.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.3.3-05",
        "testo": "Il TSP non dovrebbe emettere certificati la cui durata ecceda quella del certificato di firma della CA.",
        "testo_integrale": "GEN-6.3.3-05: The TSP should not issue certificates whose lifetime exceeds that of the CA's signing certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.3.3-06",
        "testo": "Se il TSP emette certificati la cui durata eccede quella del certificato di firma della CA, il TSP deve garantire che lo stato del certificato (v. clausola 6.3.10) possa comunque essere verificato dalle relying party dopo la scadenza del certificato della CA.",
        "testo_integrale": "GEN-6.3.3-06 [CONDITIONAL]: If the TSP does issue certificates whose lifetime exceeds the lifetime of the CA's signing certificate, the TSP shall ensure that the certificate status (see clause 6.3.10) can still be verified by relying parties after expiry of the CA certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando il TSP emette certificati la cui durata eccede quella del certificato di firma della CA.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.3.3-07",
        "testo": "Se la CA ha generato la coppia di chiavi del soggetto, la procedura di emissione del certificato deve essere collegata in modo sicuro alla generazione della coppia di chiavi da parte della CA.",
        "testo_integrale": "GEN-6.3.3-07 [CONDITIONAL]: If the CA generated the subject's key pair, the procedure of issuing the certificate shall be securely linked to the generation of the key pair by the CA.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando la CA ha generato la coppia di chiavi del soggetto.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.3.3-08",
        "testo": "Per le policy LCP e NCP, se la CA ha generato la coppia di chiavi del soggetto, la chiave privata deve essere consegnata in modo sicuro al soggetto registrato, oppure al TSP che gestisce la chiave privata del soggetto.",
        "testo_integrale": "GEN-6.3.3-08 [LCP] and [NCP] [CONDITIONAL]: If the CA generated the subject's key pair, the private key shall be securely passed to the registered subject; or to the TSP managing the subject's private key.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alle policy LCP e NCP quando la CA ha generato la coppia di chiavi del soggetto.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.3.3-09A",
        "testo": "Per la policy NCP+, se la CA ha generato la coppia di chiavi del soggetto, il dispositivo crittografico sicuro contenente la chiave privata del soggetto deve essere consegnato in modo sicuro al soggetto registrato o, nel caso di un TSP terzo che gestisce la chiave per conto del soggetto, a tale TSP terzo.",
        "testo_integrale": "SDP-6.3.3-09A [NCP+][CONDITIONAL]: If the CA generated the subject's key pair, the secure cryptographic device containing the subject's private key shall be securely delivered to the registered subject or, in the case of a third party TSP managing the key on behalf of the subject, to that third party TSP.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP+ quando la CA ha generato la coppia di chiavi del soggetto.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.3.3-10",
        "testo": "Per tutte le policy tranne DVCP, nel corso della vita della CA un nome distinto del soggetto già usato in un certificato non deve mai essere riassegnato a un altro soggetto; per la policy DVCP, nel corso della vita della CA un nome distinto del soggetto già usato in un certificato può essere riassegnato a un altro soggetto quando il sottoscrittore ha fornito prova della legittima titolarità del nome.",
        "testo_integrale": "GEN-6.3.3-10: [All policies except DVCP]: Over the life time of the CA a subject distinguished name which has been used in a certificate shall never be re-assigned to another subject. NOTE: For [DVCP] over the life time of the CA a subject distinguished name which has been used in a certificate may be re-assigned to another subject when the subscriber has provided evidence of rightful ownership of the name.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica a tutte le policy tranne DVCP (per DVCP vale l'eccezione descritta nella NOTE).",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.3.3-11",
        "testo": "Se un certificato è emesso a una persona fisica identificata in associazione a una persona giuridica, gli attributi del soggetto che identificano l'organizzazione nel certificato dovrebbero rappresentare la persona giuridica o una sua sotto-entità, e l'identificatore del soggetto nel certificato deve essere la persona fisica.",
        "testo_integrale": "GEN-6.3.3-11 [CONDITIONAL]: If a certificate is issued to a natural person identified in association with the legal person, then the subject attributes identifying the organization in the certificate should represent the legal person or sub-entity of that legal person and the subject identifier in the certificate shall be the natural person.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando un certificato è emesso a una persona fisica identificata in associazione a una persona giuridica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.3.3-12",
        "testo": "L'identificatore di CP deve essere, a scelta secondo la policy applicabile: per NCP, quello di cui alla clausola 5.3 lettera a) e/o un OID assegnato dal TSP o da altro soggetto interessato o da ulteriore standardizzazione per una certificate policy che rafforza i requisiti di policy del presente documento; per NCP+, quello di cui alla clausola 5.3 lettera b) e/o un OID analogo; per LCP, quello di cui alla clausola 5.3 lettera c) e/o un OID analogo; per EVCP, un OID come specificato nella EVCG clausola 7.1.6.1 e almeno uno tra: quello di cui alla clausola 5.3 lettera d) e/o un OID analogo; per DVCP, un OID come specificato nella BRG clausola 1.2 o 7.1.6.1 e almeno uno tra: quello di cui alla clausola 5.3 lettera e) e/o un OID analogo; per OVCP, un OID come specificato nella BRG clausola 1.2 o 7.1.6.1 e almeno uno tra: quello di cui alla clausola 5.3 lettera f) e/o un OID analogo; per IVCP, un OID come specificato nella BRG clausola 1.2 o 7.1.6.1 e almeno uno tra: quello di cui alla clausola 5.3 lettera g) e/o un OID analogo.",
        "testo_integrale": "GEN-6.3.3-12: The CP identifier shall be [CHOICE]: [NCP]: as specified in clause 5.3 item a); and/or an OID, allocated by the TSP, other relevant stakeholder or further standardization for a certificate policy enhancing the policy requirements defined in the present document. [NCP+]: as specified in clause 5.3 item b); and/or an OID, allocated by the TSP, other relevant stakeholder or further standardization for a certificate policy enhancing the policy requirements defined in the present document. [LCP]: as specified in clause 5.3 item c); and/or an OID, allocated by the TSP, other relevant stakeholder or further standardization for a certificate policy enhancing the policy requirements defined in the present document. [EVCP]: an OID as specified in EVCG [4], clause 7.1.6.1 and at least one of the following policy identifiers: as specified in clause 5.3, item d); and/or an OID, allocated by the TSP, other relevant stakeholder or further standardization for a certificate policy enhancing the policy requirements defined in the present document. [DVCP]: an OID as specified in BRG [6], clause 1.2 or 7.1.6.1 and at least one of the following policy identifiers: as specified in clause 5.3, item e); and/or an OID, allocated by the TSP, other relevant stakeholder or further standardization for a certificate policy enhancing the policy requirements defined in the present document. [OVCP]: an OID as specified in BRG [6], clause 1.2 or 7.1.6.1 and at least one of the following policy identifiers: as specified in clause 5.3 item f); and/or an OID, allocated by the TSP, other relevant stakeholder or further standardization for a certificate policy enhancing the policy requirements defined in the present document. [IVCP]: an OID as specified in BRG [6], clause 1.2 or 7.1.6.1 and at least one of the following policy identifiers: as specified in clause 5.3 item g); and/or an OID, allocated by the TSP, other relevant stakeholder or further standardization for a certificate policy enhancing the policy requirements defined in the present document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Scelta (CHOICE) dell'identificatore di CP secondo la policy applicabile (NCP/NCP+/LCP/EVCP/DVCP/OVCP/IVCP).",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.3.4-01",
        "testo": "I termini e le condizioni devono indicare cosa costituisce l'accettazione del certificato (v. clausola 6.9.4).",
        "testo_integrale": "OVR-6.3.4-01: The terms and conditions shall indicate what is deemed to constitute acceptance of the certificate. See clause 6.9.4.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.4-02",
        "testo": "Prima di stabilire un rapporto contrattuale con un sottoscrittore, il TSP deve informare il sottoscrittore dei termini e delle condizioni relativi all'uso del certificato di cui alla clausola 6.9.4.",
        "testo_integrale": "REG-6.3.4-02: Before entering into a contractual relationship with a subscriber, the TSP shall inform the subscriber of the terms and conditions regarding use of the certificate as given in clause 6.9.4.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.4-03",
        "testo": "Se il soggetto è una persona (non un dispositivo) e non coincide con il sottoscrittore, il soggetto deve essere informato dei propri obblighi.",
        "testo_integrale": "REG-6.3.4-03 [CONDITIONAL]: If the subject is a person (i.e. not a device), and not the same as the subscriber, the subject shall be informed of his/her obligations.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando il soggetto è una persona diversa dal sottoscrittore.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.3.4-04",
        "testo": "Il TSP deve comunicare i termini e le condizioni tramite un mezzo di comunicazione duraturo (cioè che ne conserva l'integrità nel tempo) e in forma leggibile dall'uomo prima dell'accordo.",
        "testo_integrale": "OVR-6.3.4-04: The TSP shall communicate the terms and conditions through a durable (i.e. with integrity over time) means of communication, and in a human readable form before the agreement.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.3.4-05",
        "testo": "I termini e le condizioni possono essere trasmessi elettronicamente.",
        "testo_integrale": "OVR-6.3.4-05: The terms and conditions may be transmitted electronically.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.3.4-06",
        "testo": "I termini e le condizioni possono utilizzare il modello di PKI disclosure statement di cui all'allegato A.",
        "testo_integrale": "OVR-6.3.4-06: The terms and conditions may use the model PKI disclosure statement given in annex A.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.4-07",
        "testo": "Il TSP deve registrare l'accordo con il sottoscrittore e, se sottoscrittore e soggetto sono due entità distinte e il soggetto è una persona fisica o giuridica, anche con il soggetto.",
        "testo_integrale": "REG-6.3.4-07: The TSP shall record the agreement with the subscriber and if the subscriber and subject are two separate entities and the subject is a natural or legal person, with the subject.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.4-08",
        "testo": "L'accordo di cui a REG-6.3.4-07 deve comportare l'accettazione esplicita dei termini e delle condizioni tramite un atto volontario successivamente comprovabile con prove.",
        "testo_integrale": "REG-6.3.4-08: The agreement in requirement REG-6.3.4-07 shall involve explicit acceptance of the terms and conditions by a wilful act which can be later supported by evidence.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.4-09",
        "testo": "Se sottoscrittore e soggetto sono due entità distinte e il soggetto è una persona fisica o giuridica, l'accordo deve essere articolato in 2 parti.",
        "testo_integrale": "REG-6.3.4-09 [CONDITIONAL]: If the subscriber and subject are two separate entities and the subject is a natural or legal person, the agreement shall be in 2 parts.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando sottoscrittore e soggetto sono entità distinte e il soggetto è una persona fisica o giuridica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.4-10A",
        "testo": "Se sottoscrittore e soggetto sono entità distinte e il soggetto è una persona fisica o giuridica, la prima parte dell'accordo deve essere ratificata dal sottoscrittore tramite un atto tracciabile (es. spuntare una casella o firmare) e deve includere: a) l'accettazione degli obblighi del sottoscrittore (v. clausola 6.9.4); b) se le prassi del TSP richiedono l'uso di un dispositivo crittografico sicuro, l'accettazione da parte del sottoscrittore di usarlo; c) il consenso alla conservazione da parte del TSP di un registro delle informazioni usate in registrazione, nella fornitura del dispositivo al soggetto (incluso se destinata al sottoscrittore o al soggetto, ove diversi), e di ogni successiva revoca (v. clausole 6.4.5 e 6.4.6), dell'identità e degli attributi specifici inseriti nel certificato, e della trasmissione di tali informazioni a terzi alle stesse condizioni richieste dalla presente policy in caso di cessazione dei servizi del TSP; d) se e a quali condizioni il sottoscrittore richiede e il soggetto acconsente alla pubblicazione del certificato; e) la conferma che le informazioni da inserire nel certificato sono corrette (ciò può essere ottenuto per rinvio, es. rinvio alla CP per i campi del certificato fissati dalla CP); f) gli obblighi applicabili ai soggetti (v. clausola 6.9.4).",
        "testo_integrale": "REG-6.3.4-10A [CONDITIONAL]: If the subscriber and subject are two separate entities and the subject is a natural or legal person, the first part of the agreement shall be ratified by the subscriber by means of a traceable action (e.g. ticking a box or signing) and shall include: a) agreement to the subscriber's obligations (see clause 6.9.4); b) if the TSP's practices require use of a secure cryptographic device, agreement by the subscriber to use a secure cryptographic device; c) consent to the keeping of a record by the TSP of information used in registration, subject device provision, including whether this is to the subscriber or to the subject where they differ, and any subsequent revocation (see clauses 6.4.5 and 6.4.6), the identity and any specific attributes placed in the certificate, and the passing of this information to third parties under the same conditions as required by this policy in the case of the TSP terminating its services; d) whether, and under what conditions, the subscriber requires and the subject consents to the publication of the certificate; e) confirmation that the information to be held in the certificate is correct; NOTE 1: This can be achieved by reference (e.g. reference to the CP for the fields of the certificate that are fixed by the CP). f) obligations applicable to subjects (see clause 6.9.4).",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando sottoscrittore e soggetto sono entità distinte e il soggetto è una persona fisica o giuridica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.4-11A",
        "testo": "Se sottoscrittore e soggetto sono entità distinte e il soggetto è una persona fisica o giuridica, la seconda parte dell'accordo deve essere ratificata dal soggetto tramite un atto tracciabile (es. spuntare una casella o firmare) e deve includere: a) l'accettazione da parte del soggetto degli obblighi applicabili ai soggetti (v. clausola 6.9.4); b) se le prassi del TSP richiedono l'uso di un dispositivo crittografico sicuro, l'accettazione da parte del soggetto di usarlo; c) il consenso alla conservazione da parte del TSP di un registro delle informazioni usate in registrazione, nella fornitura del dispositivo al soggetto, e di ogni successiva revoca, dell'identità e degli attributi specifici inseriti nel certificato, e della trasmissione di tali informazioni a terzi alle stesse condizioni richieste dalla presente policy in caso di cessazione dei servizi del TSP. Se il sottoscrittore è il rappresentante ufficiale della persona giuridica che è il soggetto, o il rappresentante ufficiale del sottoscrittore coincide col soggetto, le voci della parte 1 (REG-6.3.4-10A) e della parte 2 possono essere ratificate insieme.",
        "testo_integrale": "REG-6.3.4-11A [CONDITIONAL]: Where the subscriber and subject are two separate entities and the subject is a natural or legal person, the second part of the agreement shall be ratified by the subject by means of a traceable action (e.g. ticking a box or signing) and shall include: a) the agreement by the subject on the obligations applicable to subjects (see clause 6.9.4); b) if the TSP's practices require use of a secure cryptographic device, agreement by the subject to use a secure cryptographic device; c) consent to the keeping of a record by the TSP of information used in registration, subject device provision, including whether this is to the subscriber or to the subject where they differ, and any subsequent revocation (see clauses 6.4.5 and 6.4.6), the identity and any specific attributes placed in the certificate, and the passing of this information to third parties under the same conditions as required by this policy in the case of the TSP terminating its services. NOTE 2: If the subscriber is the official representative of the legal person that is the subject, or the official representative of the subscriber and the subject is the same, part 1 (see REG-6.3.4-10A) and part 2 (see REG-6.3.4-11A) items listed above can be ratified together.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando sottoscrittore e soggetto sono entità distinte e il soggetto è una persona fisica o giuridica.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.4-12",
        "testo": "Se soggetto e sottoscrittore sono la stessa entità o il soggetto è un dispositivo, l'accordo deve essere articolato in una o due parti.",
        "testo_integrale": "REG-6.3.4-12 [CONDITIONAL]: If the subject and subscriber are the same entity or the subject is a device, the agreement shall be in one or two parts.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando soggetto e sottoscrittore coincidono o il soggetto è un dispositivo.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.4-13",
        "testo": "Se soggetto e sottoscrittore sono la stessa entità o il soggetto è un dispositivo, l'accordo deve includere le voci della parte 1 (REG-6.3.4-10A) e della parte 2 (REG-6.3.4-11A) sopra elencate; il sottoscrittore può accettare i diversi aspetti dell'accordo in fasi diverse della registrazione (es. la conferma che le informazioni nel certificato sono corrette può avvenire in un momento successivo rispetto ad altri aspetti dell'accordo).",
        "testo_integrale": "REG-6.3.4-13 [CONDITIONAL]: If the subject and subscriber are the same entity or the subject is a device, the agreement shall include the part 1 (see REG-6.3.4-10A) and part 2 (see REG-6.3.4-11A) items listed above. NOTE 3: The subscriber can agree to different aspects of this agreement during different stages of registration. For example, agreement that the information held in the certificate is correct can be carried out subsequent to other aspects of the agreement.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando soggetto e sottoscrittore coincidono o il soggetto è un dispositivo.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.4-16",
        "testo": "L'accordo può essere in forma elettronica.",
        "testo_integrale": "REG-6.3.4-16: The agreement may be in electronic form.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.4-17",
        "testo": "I registri sopra identificati devono essere conservati per il periodo di tempo indicato al sottoscrittore (come parte dei termini e delle condizioni).",
        "testo_integrale": "REG-6.3.4-17: The records identified above shall be retained for the period of time as indicated to the subscriber (as part of the terms and conditions). NOTE 4: See also clause 6.4.6 regarding retention of information.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.3.5-01",
        "testo": "Gli obblighi del sottoscrittore (v. clausola 6.3.4) devono includere: a) l'obbligo di fornire al TSP informazioni accurate e complete secondo i requisiti del presente documento, in particolare riguardo alla registrazione; b) l'obbligo di usare la coppia di chiavi solo in conformità con le limitazioni notificate al sottoscrittore e al soggetto se questo è una persona fisica o giuridica; c) il divieto di uso non autorizzato della chiave privata del soggetto; d) se il sottoscrittore o il soggetto genera le chiavi del soggetto, l'obbligo o la raccomandazione di generarle usando un algoritmo secondo ETSI TS 119 312 per gli usi della chiave certificata identificati nella CP, e di usare lunghezza e algoritmo di chiave secondo ETSI TS 119 312 per tutta la validità del certificato (le raccomandazioni di ETSI TS 119 312 possono essere sostituite da raccomandazioni nazionali); e) se il sottoscrittore o il soggetto genera le chiavi del soggetto e l'uso della chiave del certificato è di tipo A, B o F secondo la clausola 4.3.2 di ETSI EN 319 412-2, quando il soggetto è una persona fisica: l'obbligo che la chiave privata del soggetto sia mantenuta sotto il suo controllo esclusivo; quando il soggetto è una persona giuridica: l'obbligo che la chiave privata sia mantenuta sotto il controllo del soggetto; f) per la policy NCP+, l'obbligo di usare la o le chiavi private del soggetto solo per funzioni crittografiche all'interno del dispositivo crittografico sicuro; g) per la policy NCP+, se le chiavi del soggetto sono generate sotto il controllo del sottoscrittore o del soggetto, l'obbligo di generarle all'interno del dispositivo crittografico sicuro; h) l'obbligo di notificare al TSP senza ritardo, fino alla fine del periodo di validità indicato nel certificato, se: la chiave privata del soggetto è stata persa, rubata o potenzialmente compromessa; il controllo sulla chiave privata del soggetto è stato perso per compromissione dei dati di attivazione (es. codice PIN) o altri motivi; vi sono imprecisioni o modifiche al contenuto del certificato notificate al sottoscrittore o al soggetto; i) l'obbligo, a seguito della compromissione della chiave privata del soggetto, di interromperne immediatamente e permanentemente l'uso, salvo che per la decifratura; e j) l'obbligo, in caso di comunicazione che il certificato del soggetto è stato revocato o che la CA emittente è stata compromessa, di garantire che la chiave privata non sia più usata dal soggetto (v. clausola 6.3.9 per la gestione della revoca e i motivi di revoca).",
        "testo_integrale": "OVR-6.3.5-01: The subscriber's obligations (see clause 6.3.4) shall include: a) an obligation to provide the TSP with accurate and complete information in accordance with the requirements of the present document, particularly with regards to registration; b) an obligation for the key pair to be only used in accordance with any limitations notified to the subscriber and the subject if the subject is a natural or legal person; c) prohibition of unauthorized use of the subject's private key; d) [CONDITIONAL] if the subscriber or subject generates the subject's keys: i) an obligation or recommendation to generate the subject keys using an algorithm as specified in ETSI TS 119 312 [i.10] for the uses of the certified key as identified in the CP; and ii) an obligation or recommendation to use key length and algorithm as specified in ETSI TS 119 312 [i.10] for the uses of the certified key as identified in the CP during the validity time of the certificate; NOTE 1: Cryptographic suites recommendations defined in ETSI TS 119 312 [i.10] can be superseded by national recommendations. e) [CONDITIONAL] if the subscriber or subject generates the subject's keys and the certificate key usage is of type A, B or F as specified in clause 4.3.2 of ETSI EN 319 412-2 [10]: i) when the subject is a natural person: an obligation for the subject's private key to be maintained under the subject's sole control; ii) when the subject is a legal person: an obligation for the subject's private key to be maintained under the subject's control; f) [NCP+] an obligation to only use the subject's private key(s) for cryptographic functions within the secure cryptographic device; g) [NCP+] [CONDITIONAL] if the subject's keys are generated under control of the subscriber or subject: an obligation to generate the subject's keys within the secure cryptographic device; h) an obligation to notify the TSP without any reasonable delay, if any of the following occur up to the end of the validity period indicated in the certificate: i) the subject's private key has been lost, stolen, potentially compromised; ii) control over the subject's private key has been lost due to compromise of activation data (e.g. PIN code) or other reasons; iii) inaccuracy or changes to the certificate content, as notified to the subscriber or to the subject; i) an obligation, following compromise of the subject's private key, to immediately and permanently discontinue the use of this key, except for key decipherment; and j) an obligation, in the case of being informed that the subject's certificate has been revoked, or that the issuing CA has been compromised, to ensure that the private key is no longer used by the subject. NOTE 2: See clause 6.3.9 for details on revocation management and on reasons for revocation.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_UTENTE_OBBLIGATO,
    },
    {
        "riferimento": "Parte 1: OVR-6.3.5-02",
        "testo": "Se il soggetto e il sottoscrittore sono entità separate e il soggetto è una persona fisica o giuridica, gli obblighi del soggetto devono conformarsi a OVR-6.3.5-01 per le lettere b), c), e), f), h), i) e j).",
        "testo_integrale": "OVR-6.3.5-02 [CONDITIONAL]: If the subject and subscriber are separate entities and the subject is a natural or legal person, the subject's obligations shall comply with OVR-6.3.5-01 for items b), c), e), f), h), i) and j).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando soggetto e sottoscrittore sono entità separate e il soggetto è una persona fisica o giuridica.",
        "soggetti": SOGGETTO_UTENTE_OBBLIGATO,
    },
    {
        "riferimento": "Parte 1: OVR-6.3.5-03",
        "testo": "La comunicazione alle relying party (v. clausola 6.9.4) deve raccomandare alla relying party di: a) verificare la validità, sospensione o revoca del certificato usando le informazioni correnti sullo stato di revoca indicate alla relying party (v. clausole 6.2.4, 6.3.9 e 6.3.10 per i requisiti su revoca e sospensione); b) tenere conto di eventuali limitazioni sull'uso del certificato indicate alla relying party nel certificato o nei termini e condizioni di cui alla clausola 6.9.4; e c) adottare qualsiasi altra precauzione prescritta negli accordi o altrove (a seconda delle prassi della CA in materia di segnalazione di problemi e richieste di revoca, ciò può includere istruzioni sulla segnalazione di potenziali problemi).",
        "testo_integrale": "OVR-6.3.5-03: The notice to relying parties (see clause 6.9.4) shall recommend the relying party to: a) verify the validity, suspension or revocation of the certificate using current revocation status information as indicated to the relying party (see clause 6.9.4); NOTE 3: See clauses 6.2.4, 6.3.9 and 6.3.10 for requirements on certificate revocation and suspension. b) take account of any limitations on the usage of the certificate indicated to the relying party either in the certificate or the terms and conditions supplied as required in clause 6.9.4; and c) take any other precautions prescribed in agreements or elsewhere. NOTE 4: Depending on CA's practices related to problem reporting and revocation requests (e.g. see clause 4.9.3 of BRG [5]) this can include instructions regarding reporting potential problems.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP + [{"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"}],
    },
    {
        "riferimento": "Parte 1: OVR-6.3.5-04",
        "testo": "Per la policy NCP, se il TSP gestisce la chiave privata per conto del soggetto e l'uso della chiave del certificato è di tipo A, B o F secondo la clausola 4.3.2 di ETSI EN 319 412-2, il TSP deve garantire che il soggetto abbia il controllo esclusivo (o, se il soggetto è una persona giuridica, il \"controllo\") sulla propria chiave privata.",
        "testo_integrale": "OVR-6.3.5-04 [NCP][CONDITIONAL]: If the TSP manages the private key on behalf of the subject and the certificate key usage is of type A, B, or F as specified in clause 4.3.2 of ETSI EN 319 412-2 [10], the TSP shall ensure that the subject has sole control (or if the subject is a legal person, \"control\") over its private key.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP quando il TSP gestisce la chiave privata per conto del soggetto e l'uso della chiave è di tipo A, B o F.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.3.5-05",
        "testo": "Per la policy NCP, se un TSP terzo gestisce la chiave privata per conto del soggetto e l'uso della chiave del certificato è di tipo A, B o F secondo la clausola 4.3.2 di ETSI EN 319 412-2, il TSP deve confermare che il TSP che gestisce la chiave garantisce che il soggetto abbia il controllo esclusivo (o, se il soggetto è una persona giuridica, il \"controllo\") sulla propria chiave privata.",
        "testo_integrale": "OVR-6.3.5-05 [NCP][CONDITIONAL]: If a third party TSP manages the private key on behalf of the subject and the certificate key usage is of type A, B, or F as specified in clause 4.3.2 of ETSI EN 319 412-2 [10], the TSP shall confirm that the TSP managing the key ensures that the subject has sole control (or if the subject is a legal person, \"control\") over its private key.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy NCP quando un TSP terzo gestisce la chiave privata per conto del soggetto e l'uso della chiave è di tipo A, B o F.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: OVR-6.3.5-06",
        "testo": "La conformità a ETSI TS 119 431-1 dovrebbe essere usata per dimostrare che il TSP che gestisce la chiave per conto del soggetto soddisfa i requisiti per garantire il controllo (esclusivo) richiesto in OVR-6.3.5-04 o OVR-6.3.5-05.",
        "testo_integrale": "OVR-6.3.5-06: Conformance to ETSI TS 119 431-1 [i.21], should be used to demonstrate that the TSP managing the key on behalf of the subject meets the requirements for ensuring (sole) control as required in OVR-6.3.5-04 or OVR-6.3.5-05.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.6-01A",
        "testo": "Si applicano tutti i requisiti delle clausole 6.3.1 e 6.3.2; per il rinnovo del certificato, quando la coppia di chiavi non cambia, REG-6.3.1-01 non deve essere ripetuto rispetto all'emissione iniziale del certificato. La clausola 6.3.2 della EVCG specifica un periodo di validità massimo.",
        "testo_integrale": "REG-6.3.6-01A: All requirements from clauses 6.3.1 and 6.3.2 shall apply. NOTE 2: For certificate renewal, where the key pair does not change, REG-6.3.1-01 does not need to be repeated from the initial certificate issuance. NOTE 3: Clause 6.3.2 of the EVCG [4] specifies a maximum validity period.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.6-02",
        "testo": "Quando il certificato precedente è usato per autenticare la richiesta, il TSP deve verificarne l'esistenza e la validità.",
        "testo_integrale": "REG-6.3.6-02 [CONDITIONAL]: When the previous certificate is used to authenticate the request, the TSP shall check the existence and validity of that certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando il certificato precedente è usato per autenticare la richiesta.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.6-06",
        "testo": "Per la policy WEB, le informazioni di validazione ottenute dal TSP possono essere riutilizzate se compatibili con la clausola 4.2.1 della BRG.",
        "testo_integrale": "REG-6.3.6-06 [WEB]: Validation information obtained by the TSP may be reused if compatible with clause 4.2.1 of BRG [5].",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy WEB.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.6-07",
        "testo": "Per la policy WEB, si applica la clausola 6.3.2 della BRG, che specifica il periodo di validità massimo.",
        "testo_integrale": "REG-6.3.6-07 [WEB]: Clause 6.3.2 of BRG [5], specifying the maximum validity period, shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy WEB.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.6-08",
        "testo": "Se sono cambiati i termini e le condizioni del TSP, questi devono essere comunicati al sottoscrittore e accettati secondo i requisiti REG-6.3.4-02, REG-6.3.4-03, OVR-6.3.4-04, OVR-6.3.4-05, OVR-6.3.4-06, REG-6.3.4-07 e REG-6.3.4-08 della clausola 6.3.4.",
        "testo_integrale": "REG-6.3.6-08: If any of the TSP's terms and conditions has changed, these shall be communicated to the subscriber and agreed to in accordance with requirements REG-6.3.4-02, REG-6.3.4-03, OVR-6.3.4-04 to OVR-6.3.4-06, REG-6.3.4-07 and REG-6.3.4-08 of clause 6.3.4.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: GEN-6.3.6-10",
        "testo": "La CA deve emettere un nuovo certificato usando la chiave pubblica del soggetto già certificata solo se la sua sicurezza crittografica è ancora sufficiente per il periodo di validità del nuovo certificato e non esistono indicazioni che la chiave privata del soggetto sia stata compromessa né che il certificato sia stato revocato per qualsiasi altra violazione di sicurezza.",
        "testo_integrale": "GEN-6.3.6-10: The CA shall issue a new certificate using the subject's previously certified public key, only if its cryptographic security is still sufficient for the new certificate's validity period and no indications exist that the subject's private key has been compromised nor that the certificate has been revoked due to any other security breach.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.7-01A",
        "testo": "Si applicano tutti i requisiti delle clausole 6.3.1 e 6.3.2.",
        "testo_integrale": "REG-6.3.7-01A: All requirements from clauses 6.3.1 and 6.3.2 shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.7-01B",
        "testo": "Se sono cambiati nomi o attributi certificati, le relative informazioni di registrazione devono essere verificate, registrate e accettate dal sottoscrittore secondo REG-6.3.1-00B e la clausola 6.2.2.",
        "testo_integrale": "REG-6.3.7-01B [CONDITIONAL]: If any certified names or attributes have changed, the related registration information shall be verified, recorded, agreed to by the subscriber in accordance with REG-6.3.1-00B and clause 6.2.2.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando sono cambiati nomi o attributi certificati.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.7-02A",
        "testo": "Il TSP deve specificare nella propria CP/CPS se, o in quali circostanze, sia consentita o meno la modifica della data di scadenza e/o degli attributi certificati in caso di re-key del certificato.",
        "testo_integrale": "REG-6.3.7-02A: The TSP shall specify in its CP/CPS if, or under which circumstances, change of expiry date and/or certified attributes is allowed or not for certificate re-key.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.7-03",
        "testo": "Quando il certificato precedente è usato per autenticare la richiesta, il TSP deve verificarne l'esistenza e la validità.",
        "testo_integrale": "REG-6.3.7-03 [CONDITIONAL]: when the previous certificate is used to authenticate the request, the TSP shall check the existence and validity of that certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando il certificato precedente è usato per autenticare la richiesta.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.7-04",
        "testo": "Se sono cambiati i termini e le condizioni del TSP, questi devono essere comunicati al sottoscrittore e accettati secondo i requisiti REG-6.3.4-02, REG-6.3.4-03, OVR-6.3.4-04, OVR-6.3.4-05, OVR-6.3.4-06, REG-6.3.4-07 e REG-6.3.4-08.",
        "testo_integrale": "REG-6.3.7-04: If any of the TSP's terms and conditions has changed, these shall be communicated to the subscriber and agreed to in accordance with requirements REG-6.3.4-02, REG-6.3.4-03, OVR-6.3.4-04 to OVR-6.3.4-06, REG-6.3.4-07 and REG-6.3.4-08.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.7-05",
        "testo": "Per la policy WEB, le informazioni di validazione ottenute dal TSP possono essere riutilizzate se compatibili con la clausola 4.2.1 della BRG.",
        "testo_integrale": "REG-6.3.7-05 [WEB]: Validation information obtained by the TSP may be reused if compatible with clause 4.2.1 of BRG [5].",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy WEB.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.7-06",
        "testo": "Per la policy WEB, si applica la clausola 6.3.2 della BRG, che specifica il periodo di validità massimo.",
        "testo_integrale": "REG-6.3.7-06 [WEB]: Clause 6.3.2 of BRG [5], specifying the maximum validity period, shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla policy WEB.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.8-01A",
        "testo": "Si applicano i requisiti della clausola 6.3.6.",
        "testo_integrale": "REG-6.3.8-01A: The requirements of clause 6.3.6 apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REG-6.3.8-02",
        "testo": "Se sono cambiati nomi o attributi certificati, le relative informazioni di registrazione devono essere verificate, registrate e accettate dal sottoscrittore secondo REG-6.3.1-00B e la clausola 6.2.2.",
        "testo_integrale": "REG-6.3.8-02 [CONDITIONAL]: If any certified names or attributes have changed, the related registration information shall be verified, recorded, agreed to by the subscriber in accordance with REG-6.3.1-00B and clause 6.2.2.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando sono cambiati nomi o attributi certificati.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.3.9-01",
        "testo": "Il TSP deve revocare i certificati in modo tempestivo sulla base di richieste di revoca autorizzate e validate (v. anche REV-6.2.4-03A).",
        "testo_integrale": "REV-6.3.9-01: The TSP shall revoke certificates in a timely manner based on authorized and validated certificate revocation requests (see also REV-6.2.4-03A).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.3.9-02",
        "testo": "Il TSP deve revocare qualsiasi certificato non scaduto: a) che non sia più conforme alla CP secondo cui è stato emesso; o b) di cui il TSP sia a conoscenza di modifiche che incidono sulla validità del certificato (non si intende che il TSP debba monitorare le informazioni relative al contenuto); o c) per il quale la crittografia utilizzata non garantisca più il collegamento tra il soggetto e la chiave pubblica.",
        "testo_integrale": "REV-6.3.9-02: The TSP shall revoke any non expired certificate: a) that is no longer compliant with the CP under which it has been issued; or b) that the TSP is aware of changes which impact the validity of the certificate; or NOTE 1: It is not implied that the TSP needs to monitor information relating to the content. c) for which the used cryptography is no longer ensuring the binding between the subject and the public key.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.3.9-03",
        "testo": "Il soggetto, e se applicabile il sottoscrittore, di un certificato revocato o sospeso deve, ove possibile, essere informato del cambiamento di stato del certificato; potrebbe non essere possibile informare il soggetto, ad esempio se noto come deceduto o altrimenti non contattabile.",
        "testo_integrale": "REV-6.3.9-03: The subject, and where applicable the subscriber, of a revoked or suspended certificate, where possible, shall be informed of the change of status of the certificate. NOTE 2: It may not be possible to inform the subject for example if known to be deceased or otherwise not available to be contacted.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP + [{"categoria": "Utente/titolare", "ruolo": "destinatario"}],
    },
    {
        "riferimento": "Parte 1: REV-6.3.9-04",
        "testo": "Una volta che un certificato è definitivamente revocato (cioè non sospeso), non deve essere ripristinato.",
        "testo_integrale": "REV-6.3.9-04: Once a certificate is definitively revoked (i.e. not suspended) it shall not be reinstated.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.9-05",
        "testo": "Se sono usate Certificate Revocation List (CRL) relative ai certificati degli utenti finali, incluse le loro varianti, la CRL o la variante deve essere pubblicata almeno ogni 24 ore fino alla pubblicazione di un'ultima CRL (v. clausola 6.6.2 per i requisiti sul profilo CRL).",
        "testo_integrale": "Where Certificate Revocation Lists (CRLs) concerning end users' certificates including any variants (e.g. Delta CRLs) are used: NOTE 3: See clause 6.6.2 regarding CRL profile requirements. CSS-6.3.9-05 [CONDITIONAL]: If Certificate Revocation Lists (CRLs) concerning end users certificates are used, including any variants, either the CRL or the variant shall be published at least every 24 hours until a last CRL has been published.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando sono usate CRL relative ai certificati degli utenti finali (incluse le varianti).",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.9-06",
        "testo": "Se sono usate CRL relative ai certificati degli utenti finali, incluse le loro varianti (es. Delta CRL), ogni CRL deve indicare l'orario della successiva emissione programmata, a meno che non sia l'ultima CRL emessa per quei certificati nell'ambito della CRL, nel qual caso il campo nextUpdate della CRL definito in IETF RFC 5280 deve essere impostato a \"99991231235959Z\" (valore definito da IETF RFC 5280 per i certificati privi di una data di scadenza ben definita, qui esteso alla CRL).",
        "testo_integrale": "CSS-6.3.9-06 [CONDITIONAL]: If Certificate Revocation Lists (CRLs) concerning end users certificates including any variants (e.g. Delta CRLs) are used, every CRL shall state a time for next scheduled CRL issue, unless it is the last CRL issued for those certificates in the scope of the CRL, in which case the nextUpdate field in the CRL defined in IETF RFC 5280 [8], shall be set to \"99991231235959Z\". NOTE 4: This value, defined in IETF RFC 5280 [8] for certificates that have no well-defined expiration date, is here extended for CRL.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando sono usate CRL relative ai certificati degli utenti finali (incluse le varianti).",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.9-07",
        "testo": "Se sono usate CRL relative ai certificati degli utenti finali, incluse le loro varianti (es. Delta CRL), una nuova CRL può essere pubblicata prima dell'orario indicato per la successiva emissione.",
        "testo_integrale": "CSS-6.3.9-07 [CONDITIONAL]: If Certificate Revocation Lists (CRLs) concerning end users certificates including any variants (e.g. Delta CRLs) are used, a new CRL may be published before the stated time of the next CRL issue.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando sono usate CRL relative ai certificati degli utenti finali (incluse le varianti).",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.9-08",
        "testo": "Se sono usate CRL relative ai certificati degli utenti finali, incluse le loro varianti (es. Delta CRL), la CRL deve essere firmata dalla CA o da un'entità designata dal TSP.",
        "testo_integrale": "CSS-6.3.9-08 [CONDITIONAL]: If Certificate Revocation Lists (CRLs) concerning end users certificates including any variants (e.g. Delta CRLs) are used, the CRL shall be signed by the CA or an entity designated by the TSP.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando sono usate CRL relative ai certificati degli utenti finali (incluse le varianti).",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.9-12",
        "testo": "Se è usata la CARL, una nuova CARL deve essere generata almeno una volta all'anno con un nextUpdate al massimo 1 anno dopo la data di emissione.",
        "testo_integrale": "Where CARL is used: CSS-6.3.9-12 [CONDITIONAL]: If CARL is used, a new CARL shall be generated at least once a year with a nextUpdate of at most 1 year after the issuing date.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando è usata la CARL.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.9-13",
        "testo": "Se è usata la CARL, una nuova CARL deve essere generata quando un certificato di CA è stato revocato.",
        "testo_integrale": "CSS-6.3.9-13 [CONDITIONAL]: If CARL is used, a new CARL shall be generated once a CA certificate has been revoked.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando è usata la CARL.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.9-14",
        "testo": "Nel caso di cross-certificate emessi dalla CA verso altri TSP, la CARL dovrebbe essere emessa almeno ogni 31 giorni.",
        "testo_integrale": "CSS-6.3.9-14: In the case of any cross-certificates issued by the CA to other TSPs, the CARL should be issued at least every 31 days.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.3.9-15",
        "testo": "Per i certificati a breve termine, un TSP non è tenuto ad avere un servizio di gestione della revoca per soddisfare i requisiti REV-6.2.4-01, REV-6.2.4-03A, REV-6.2.4-03BA, da REV-6.2.4-05A a REV-6.2.4-09, REV-6.3.9-01, REV-6.3.9-02 e SDP-6.5.1-21, in quanto tali requisiti non sono necessariamente applicabili ai certificati a breve termine.",
        "testo_integrale": "REV-6.3.9-15: A TSP need not have a revocation management service to address requirements REV-6.2.4-01, REV-6.2.4-03A, REV-6.2.4-03BA, REV-6.2.4-05A to REV-6.2.4-09, REV-6.3.9-01, REV-6.3.9-02 and SDP-6.5.1-21 for short-term certificates, as these requirements are not necessarily applicable to short-term certificates.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica ai certificati a breve termine.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.3.9-15A",
        "testo": "Per i certificati a breve termine che possono essere revocati, il TSP deve soddisfare i requisiti REV-6.2.4-01, REV-6.2.4-03A, REV-6.2.4-03BA, da REV-6.2.4-05A a REV-6.2.4-09, REV-6.3.9-01, REV-6.3.9-02 e SDP-6.5.1-21. Il requisito CSS-6.3.10-08 continua ad applicarsi al TSP che emette certificati a breve termine: un TSP che li emette può fornire risposte OCSP \"good\" o una CRL vuota per il certificato a breve termine interessato per compatibilità con sistemi precedenti, ma la verifica di tali servizi di stato di revoca non fornirà informazioni aggiuntive sulla validità del certificato. Le possibilità offerte da REV-6.3.9-15 si applicano solo ai certificati degli utenti finali; se un TSP non rispetta la certificate policy applicabile, il suo certificato di CA può essere revocato.",
        "testo_integrale": "REV-6.3.9-15A [CONDITIONAL]: For short-term certificates which can be revoked the TSP shall fulfil requirements REV-6.2.4-01, REV-6.2.4-03A, REV-6.2.4-03BA, REV-6.2.4-05A to REV-6.2.4-09, REV-6.3.9-01, REV-6.3.9-02 and SDP-6.5.1-21. NOTE 5: Requirement CSS-6.3.10-08 still applies to TSP issuing short-term certificates. A TSP issuing short-term certificate can provide \"good\" OCSP responses or empty CRL for the concerned short-term certificate for backward compatibility, however, checking such revocation status services will not provide additional information about the validity of the certificate. NOTE 6: Possibilities offered by REV-6.3.9-15 applies only to end user certificates; if a TSP fails to apply the applicable certificate policy, then its CA certificate can be revoked.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica ai certificati a breve termine che possono essere revocati.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.3.9-16",
        "testo": "Un TSP che emette certificati a breve termine deve descrivere esplicitamente nella CPS quali certificati non possono essere revocati tramite un servizio di gestione della revoca e quali certificati non possono essere revocati nemmeno dal TSP di propria iniziativa; la spiegazione che un certo gruppo di certificati non può essere revocato e che il loro stato non cambia mai può essere considerata un'alternativa a REV-6.2.4-01.",
        "testo_integrale": "REV-6.3.9-16: A TSP issuing short-term certificates shall explicitly describe in the CPS which certificates cannot be revoked through a revocation management service and which certificates cannot be revoked even by the TSP on its own initiative. NOTE 7: The explanation that certain group of certificates cannot be revoked and their status never changes can be considered as an alternative to REV-6.2.4-01.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.3.9-17",
        "testo": "Per il TSP che emette certificati a breve termine non revocabili, il TSP deve fornire un meccanismo per notificare problemi relativi a tali certificati non revocabili e per richiedere informazioni su tali problemi notificati.",
        "testo_integrale": "REV-6.3.9-17 [CONDITIONAL]: For TSP issuing short-term certificates which cannot be revoked, the TSP shall provide a mechanism to notify problems with these non-revocable certificates and to request information on these notified problems.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica al TSP che emette certificati a breve termine non revocabili.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.3.9-18",
        "testo": "Per il TSP che emette certificati a breve termine non revocabili, il TSP deve registrare in un log di audit ogni problema notificato relativo a tali certificati non revocabili.",
        "testo_integrale": "REV-6.3.9-18 [CONDITIONAL]: For TSP issuing short-term certificates which cannot be revoked, the TSP shall record any notified problem with these non-revocable certificates in an audit log.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica al TSP che emette certificati a breve termine non revocabili.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: REV-6.3.9-19",
        "testo": "Per il TSP che emette certificati a breve termine non revocabili, il TSP deve descrivere nella propria CPS come possano essere notificati eventuali problemi con i certificati non revocabili e come possano essere richieste informazioni su tale notifica; la prova della notifica di un problema potrebbe essere necessaria in un procedimento giudiziario.",
        "testo_integrale": "REV-6.3.9-19 [CONDITIONAL]: For TSP issuing short-term certificates which cannot be revoked, the TSP shall describe in its CPS how any problems with non-revocable certificates can be notified and how information on this notification can be requested. NOTE 8: Proof of the notification of a problem might be needed during a juridical procedure.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica al TSP che emette certificati a breve termine non revocabili.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.10-01",
        "testo": "Il TSP deve fornire servizi per verificare lo stato dei certificati.",
        "testo_integrale": "CSS-6.3.10-01: The TSP shall provide services for checking the status of the certificates.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.10-01A",
        "testo": "Il TSP non è tenuto a fornire servizi di stato per i certificati che contengono un'estensione di validità garantita (ETSI EN 319 412-1, clausola 5.2); fornire servizi di verifica per i certificati con validità garantita può comunque migliorare l'interoperabilità con servizi di validazione privi di supporto specifico per tali certificati.",
        "testo_integrale": "CSS-6.3.10-01A [CONDITIONAL]: The TSP need not provide status services for certificates that contain a validity assured extension (ETSI EN 319 412-1 [14], clause 5.2). NOTE: Providing services for checking validity-assured certificates can improve interoperability with validation services lacking specific support for validity-assured certificates.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica ai certificati che contengono un'estensione di validità garantita.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.10-01B",
        "testo": "Se un certificato include l'estensione di validità garantita ma non include né un punto di distribuzione CRL né la posizione di accesso a un responder OCSP, il certificato dovrebbe avere le estensioni No Revocation Available come specificato in IETF RFC 9608.",
        "testo_integrale": "CSS-6.3.10-01B [CONDITIONAL]: If a certificate includes the validity assured extension, but neither include a CRL distribution point nor access location of an OCSP responder is included, then the certificate should have No Revocation Available extensions as specified in IETF RFC 9608 [i.23].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando un certificato con estensione di validità garantita non include né CRL distribution point né OCSP responder.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.10-02",
        "testo": "Le informazioni sullo stato di revoca devono essere disponibili 24 ore su 24, 7 giorni su 7; in caso di guasto di sistema, di servizio o di altri fattori non sotto il controllo del TSP, il TSP deve adoperarsi al meglio affinché tale servizio informativo non risulti indisponibile per più del periodo massimo indicato nella CPS.",
        "testo_integrale": "CSS-6.3.10-02: Revocation status information shall be available 24 hours per day, 7 days per week. Upon system failure, service or other factors which are not under the control of the TSP, the TSP shall make best endeavours to ensure that this information service is not unavailable for longer than a maximum period of time as denoted in the CPS.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.10-03",
        "testo": "L'integrità e l'autenticità delle informazioni di stato devono essere protette.",
        "testo_integrale": "CSS-6.3.10-03: The integrity and authenticity of the status information shall be protected.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.10-04",
        "testo": "Le informazioni sullo stato di revoca devono includere informazioni sullo stato dei certificati almeno fino alla scadenza del certificato; ETSI EN 319 411-2 specifica un modo standard per fornire informazioni sullo stato del certificato anche oltre la scadenza.",
        "testo_integrale": "CSS-6.3.10-04: Revocation status information shall include information on the status of certificates at least until the certificate expires. NOTE 1: ETSI EN 319 411-2 [i.5] specifies a standard way of providing certificate status information beyond expiry.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.10-05",
        "testo": "Deve essere supportato OCSP o CRL.",
        "testo_integrale": "CSS-6.3.10-05: OCSP or CRL shall be supported.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.10-06",
        "testo": "OCSP dovrebbe essere supportato; il supporto di OCSP è raccomandato, in particolare quando le CRL rischiano di avere dimensioni elevate, come può accadere per i certificati la cui validità al momento dell'uso della chiave privata non può essere garantita dal TSP.",
        "testo_integrale": "CSS-6.3.10-06: OCSP should be supported. NOTE 2: The support of OCSP is recommended. It is particularly important where CRLs are susceptible to be big in size, which can be the case for certificates whose validity at the time of use of the private key cannot be assured by the TSP.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.10-08",
        "testo": "Se un TSP supporta più metodi (CRL e servizio di stato del certificato online) per fornire lo stato di revoca, qualsiasi aggiornamento allo stato di revoca deve essere disponibile per tutti i metodi.",
        "testo_integrale": "CSS-6.3.10-08 [CONDITIONAL]: If a TSP supports multiple methods (CRL and on-line certificate status service) to provide revocation status, any updates to revocation status shall be available for all methods.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando il TSP supporta più metodi (CRL e servizio online) per lo stato di revoca.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.10-09",
        "testo": "Se un TSP supporta più metodi (CRL e servizio di stato del certificato online) per fornire lo stato di revoca, le informazioni fornite da tutti i servizi devono essere coerenti nel tempo, tenendo conto dei diversi ritardi di aggiornamento delle informazioni di stato per ciascun metodo. La coerenza nel tempo consente di tenere conto della differenza dei ritardi purché lo stato del certificato risulti alla fine lo stesso e purché sia rispettato REV-6.2.4-03C; ciò può basarsi sulle informazioni fornite ai sensi di CSS-6.3.10-09A (es. se OCSP può essere aggiornato immediatamente, OCSP e CRL possono differire finché non è generata la nuova CRL).",
        "testo_integrale": "CSS-6.3.10-09 [CONDITIONAL]: If a TSP supports multiple methods (CRL and on-line certificate status service) to provide revocation status, the information provided by all services shall be consistent over time taking into account different delays in updating the status information for all the methods. NOTE 6: Consistency over time allows for the difference in delays to be taken into account provided that the status of the certificate is ultimately the same and provided REV-6.2.4-03C can be respected. This can be done on the basis of the information provided under CSS-6.3.10-09A. EXAMPLE: If OCSP can be updated immediately, OCSP and CRL may differ, until the new CRL has been generated.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando il TSP supporta più metodi (CRL e servizio online) per lo stato di revoca.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.10-09A",
        "testo": "Se un TSP supporta più metodi (CRL e servizio di stato del certificato online) per fornire lo stato di revoca e vi sono o possono esservi ritardi diversi nell'aggiornamento delle informazioni per ciascun metodo, il TSP deve documentare nella propria CPS l'origine di tali ritardi e come interpretare i risultati in caso di differenze.",
        "testo_integrale": "CSS-6.3.10-09A [CONDITIONAL]: If a TSP supports multiple methods (CRL and on-line certificate status service) to provide revocation status and delays in updating the status information for all the methods exist or are possible, the TSP shall document in its CPS the origin of such delays and how to interpret the results in case of differences.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando il TSP supporta più metodi (CRL e servizio online) per lo stato di revoca e vi sono possibili ritardi differenziati.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: CSS-6.3.10-10",
        "testo": "Le informazioni sullo stato di revoca devono essere disponibili pubblicamente e a livello internazionale.",
        "testo_integrale": "CSS-6.3.10-10: The revocation status information shall be publicly and internationally available.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.3.12-01",
        "testo": "La sicurezza di eventuali copie duplicate delle chiavi private del soggetto deve essere allo stesso livello delle chiavi private originali del soggetto.",
        "testo_integrale": "SDP-6.3.12-01: The security of any duplicated subject's private keys shall be at the same level as for the original subject's private keys.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.3.12-02",
        "testo": "Il numero di eventuali copie duplicate delle chiavi private del soggetto non deve eccedere il minimo necessario a garantire la continuità del servizio.",
        "testo_integrale": "SDP-6.3.12-02: The number of any duplicated subject's private keys shall not exceed the minimum needed to ensure continuity of the service.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.3.12-03",
        "testo": "Se l'uso della chiave del certificato è di tipo A, B o F secondo la clausola 4.3.2 di ETSI EN 319 412-2, la CA non deve detenere le chiavi private di firma del soggetto in un modo che fornisca una capacità di decifratura di backup (comunemente detta key escrow) e che comporti che il loro uso non sia sotto il controllo esclusivo (o, se il soggetto è una persona giuridica, il \"controllo\") del firmatario o del titolare; ciò non preclude che il TSP generi e gestisca la chiave per conto dell'utente, purché la chiave sia mantenuta sotto il controllo esclusivo (o \"controllo\", per persona giuridica) dell'utente.",
        "testo_integrale": "SDP-6.3.12-03 [CONDITIONAL]: If the certificate key usage is of type A, B, or F as specified in clause 4.3.2 of ETSI EN 319 412-2 [10], then the CA shall not hold the subject's private signing keys in a way which provides a backup decryption capability (commonly called key escrow), and results in its use not being under the sole control (or if the subject is a legal person \"control\") of the signer or owner. NOTE: This does not preclude the TSP generating and managing the key on behalf of the user provided that the key is kept under the sole control (or if the subject is a legal person \"control\") of the user.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando l'uso della chiave del certificato è di tipo A, B o F.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.3.12-04",
        "testo": "Se la chiave privata del soggetto è destinata all'autenticazione, la CA non dovrebbe detenere le chiavi private di firma del soggetto in un modo che fornisca una capacità di decifratura di backup (key escrow) e che comporti che il loro uso non sia sotto il controllo del firmatario o del titolare.",
        "testo_integrale": "SDP-6.3.12-04 [CONDITIONAL]: If the subject's private key is to be used for authentication, then the CA should not hold the subject's private signing keys in a way which provides a backup decryption capability (commonly called key escrow), and results in its use not being under the control of the signer or owner.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando la chiave privata del soggetto è destinata all'autenticazione.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.3.12-05",
        "testo": "Se la chiave privata del soggetto è destinata alla decifratura, la CA può effettuarne il backup.",
        "testo_integrale": "SDP-6.3.12-05 [CONDITIONAL]: If the subject's private key is to be used for decryption, then the CA may back it up.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando la chiave privata del soggetto è destinata alla decifratura.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.3.12-06",
        "testo": "Se la CA richiede che una chiave privata del soggetto usata per la decifratura sia posta in escrow dalla CA o da un'entità designata, tale chiave privata non deve avere altri usi.",
        "testo_integrale": "SDP-6.3.12-06 [CONDITIONAL]: If the CA requires a subject private key used for decryption to be escrowed by the CA or a designated entity, then this private key shall not have other key usages.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando la CA richiede l'escrow di una chiave privata del soggetto usata per la decifratura.",
        "soggetti": SOGGETTO_QTSP,
    },
    {
        "riferimento": "Parte 1: SDP-6.3.12-07",
        "testo": "Se una copia della chiave del soggetto è conservata dalla CA per escrow, la CA deve mantenere segreta la chiave privata e renderla disponibile solo a persone opportunamente autorizzate.",
        "testo_integrale": "SDP-6.3.12-07 [CONDITIONAL]: If a copy of the subject's key is kept by the CA for escrow then the CA shall keep secret the private key and only make it available to appropriately authorized persons.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica quando una copia della chiave del soggetto è conservata dalla CA per escrow.",
        "soggetti": SOGGETTO_QTSP,
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "Parte 1: clausola 6.2.1",
        "testo": "Per i requisiti sul naming nei certificati si rimanda a ISO/IEC 9594-8 (ITU-T X.509) o IETF RFC 5280 e alle parti pertinenti di ETSI EN 319 412 (parti 2, 3 e 4); v. clausola 6.6.1 del presente documento.",
        "testo_integrale": "6.2.1 Naming: NOTE: Requirements for naming in certificates are as specified in ISO/IEC 9594-8/Recommendation ITU-T X.509 [7] or IETF RFC 5280 [8] and the appropriate part of ETSI EN 319 412 parts 2 [10], 3 [11] and 4 [2]. See clause 6.6.1 of the present document.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.2.3",
        "testo": "I requisiti per il re-key sono trattati alla clausola 6.3.7 (Certificate Re-key); il requisito numerato originariamente previsto in questa sottoclausola (REG-6.2.3-01) è stato soppresso (Void).",
        "testo_integrale": "6.2.3 Identification and authentication for Re-key requests. NOTE: Requirements for re-key are addressed in the certificate re-key clause 6.3.7. REG-6.2.3-01: Void.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: REG-6.3.1-02",
        "testo": "Requisito soppresso (Void); la NOTE collegata chiarisce che la clausola 5.2.4 della EVCG specifica una procedura a doppio controllo nel processo di validazione per la policy EVCP.",
        "testo_integrale": "REG-6.3.1-02: Void. NOTE 3: Clause 5.2.4 of the EVCG [4] specify a dual control procedure in the validation process for [EVCP].",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.3.6 (premessa)",
        "testo": "Il rinnovo del certificato consiste nell'emissione di un nuovo certificato a un soggetto a cui un certificato è già stato emesso dallo stesso TSP, senza modificare il soggetto, le chiavi pubbliche di altri partecipanti o qualsiasi altra informazione nel certificato (salvo il numero di serie del certificato, aggiornato secondo IETF RFC 5280). Il processo di rinnovo può avvenire nel periodo di validità di un certificato esistente o dopo la sua data di scadenza (dopo la data nel campo notAfter); quando il rinnovo avviene durante la validità del certificato precedente, la data di scadenza può essere aggiornata.",
        "testo_integrale": "6.3.6 Certificate renewal. NOTE 1: Certificate renewal refers to the issuance of a new certificate to a subject to whom a certificate has previously been issued by the same TSP without changing the subject or other participant's public keys or any other information in the certificate (see IETF RFC 3647 [i.3]), except the certificate serialNumber that is updated as per IETF RFC 5280 [8]. The certificate renewal process can happen within the validity period of an existing certificate, or after the former certificate expiry date (i.e. after the date in the notAfter field). When the renewal happens during the validity period of the former certificate, the expiry date can be updated.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.3.7 (premessa)",
        "testo": "Il re-key del certificato consiste nell'emissione di un nuovo certificato con una nuova chiave pubblica del soggetto per un soggetto a cui un certificato è già stato emesso dallo stesso TSP; gli attributi del soggetto e gli altri attributi certificati possono essere aggiornati. Il processo di re-key può avvenire nel periodo di validità di un certificato esistente (incluso il re-key a seguito di revoca o prima della scadenza), o dopo la data di scadenza del certificato precedente; quando il re-key avviene durante la validità del certificato precedente, la data di scadenza può essere aggiornata (es. il re-key può avvenire dopo la revoca di un certificato per compromissione della chiave, o dopo la scadenza di un certificato e del periodo di utilizzo della coppia di chiavi).",
        "testo_integrale": "6.3.7 Certificate Re-key. NOTE: Certificate re-key refers to the issuance of a new certificate with a new subject public key for a subject to whom a certificate has previously been issued by the same TSP (see IETF RFC 3647 [i.3]). Subject attributes and other certified attributes can be updated. The certificate rekey process can happen within the validity period of an existing certificate (this includes re-key following revocation or prior to expiration), or after the former certificate expiry date (i.e. after the date in the notAfter field). When the rekey happens during the validity period of the former certificate, the expiry date can be updated. EXAMPLE: Rekey can occur after a certificate is revoked for reasons of key compromise or after a certificate has expired and the usage period of the key pair has also expired.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.3.8 (premessa)",
        "testo": "La modifica del certificato consiste nell'emissione di un nuovo certificato per un soggetto a cui un certificato è già stato emesso dallo stesso TSP, a causa di cambiamenti nelle informazioni del certificato diversi dalla chiave pubblica del sottoscrittore; la modifica implica l'aggiornamento di uno o più attributi del soggetto. Il processo di modifica può avvenire nel periodo di validità di un certificato esistente o dopo la sua data di scadenza; la chiave resta la stessa. Quando la modifica avviene durante la validità del certificato precedente, la data di scadenza può essere aggiornata.",
        "testo_integrale": "6.3.8 Certificate modification. NOTE: Certificate modification refers to the issuance of a new certificate for a subject to whom a certificate has previously been issued by the same TSP due to changes in the information in the certificate other than the subscriber public key (see IETF RFC 3647 [i.3]). The modification implies the update of subject's attribute(s). The certificate modification process can happen within the validity period of an existing certificate, or after the former certificate expiry date (i.e. after the date in the notAfter field). The key remains the same. When the modification happens during the validity period of the former certificate, the expiry date can be updated.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: CSS-6.3.10-07",
        "testo": "Requisito soppresso (Void); la NOTE collegata chiarisce che il supporto di OCSP può essere obbligatorio in alcuni contesti (es. le CP OV/IV/DV della BRG o la policy EVCP della EVCG).",
        "testo_integrale": "CSS-6.3.10-07: Void. NOTE 3: OCSP can be mandatory for some contexts (e.g. OV/IV/DV CPs in BRG [6] or EVCP in EVCG [4]).",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 6.3.11",
        "testo": "Nessun requisito di policy per la fine della sottoscrizione.",
        "testo_integrale": "6.3.11 End of subscription. No policy requirement.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "Parte 1: DIS-6.1-01A",
    "Parte 1: DIS-6.1-01B",
    "Parte 1: DIS-6.1-01C",
    "Parte 1: DIS-6.1-02A",
    "Parte 1: DIS-6.1-04",
    "Parte 1: DIS-6.1-05",
    "Parte 1: DIS-6.1-06A",
    "Parte 1: DIS-6.1-07A",
    "Parte 1: DIS-6.1-08",
    "Parte 1: DIS-6.1-09",
    "Parte 1: DIS-6.1-10",
    "Parte 1: DIS-6.1-10A",
    "Parte 1: clausola 6.2.1",
    "Parte 1: REG-6.2.2-01",
    "Parte 1: REG-6.2.2-02A",
    "Parte 1: REG-6.2.2-02AB",
    "Parte 1: REG-6.2.2-02AC",
    "Parte 1: REG-6.2.2-02B",
    "Parte 1: REG-6.2.2-03A",
    "Parte 1: REG-6.2.2-05",
    "Parte 1: REG-6.2.2-05A",
    "Parte 1: REG-6.2.2-05B",
    "Parte 1: REG-6.2.2-05C",
    "Parte 1: REG-6.2.2-06",
    "Parte 1: REG-6.2.2-07",
    "Parte 1: REG-6.2.2-08",
    "Parte 1: REG-6.2.2-08A",
    "Parte 1: REG-6.2.2-09",
    "Parte 1: REG-6.2.2-10",
    "Parte 1: REG-6.2.2-10A",
    "Parte 1: REG-6.2.2-12",
    "Parte 1: REG-6.2.2-13",
    "Parte 1: REG-6.2.2-13A",
    "Parte 1: REG-6.2.2-14A",
    "Parte 1: REG-6.2.2-15A",
    "Parte 1: REG-6.2.2-16",
    "Parte 1: REG-6.2.2-16A",
    "Parte 1: REG-6.2.2-16B",
    "Parte 1: REG-6.2.2-17A",
    "Parte 1: REG-6.2.2-18",
    "Parte 1: REG-6.2.2-19",
    "Parte 1: REG-6.2.2-20",
    "Parte 1: REG-6.2.2-21",
    "Parte 1: REG-6.2.2-22",
    "Parte 1: REG-6.2.2-23",
    "Parte 1: REG-6.2.2-25",
    "Parte 1: REG-6.2.2-26",
    "Parte 1: clausola 6.2.3",
    "Parte 1: REV-6.2.4-01",
    "Parte 1: REV-6.2.4-03A",
    "Parte 1: REV-6.2.4-03BA",
    "Parte 1: REV-6.2.4-03BB",
    "Parte 1: REV-6.2.4-03C",
    "Parte 1: REV-6.2.4-05A",
    "Parte 1: REV-6.2.4-06A",
    "Parte 1: REV-6.2.4-07",
    "Parte 1: REV-6.2.4-08",
    "Parte 1: REV-6.2.4-09",
    "Parte 1: REG-6.3.1-00A",
    "Parte 1: REG-6.3.1-00B",
    "Parte 1: REG-6.3.1-00C",
    "Parte 1: REG-6.3.1-00D",
    "Parte 1: REG-6.3.1-00E",
    "Parte 1: REG-6.3.1-00F",
    "Parte 1: REG-6.3.1-01",
    "Parte 1: REG-6.3.1-02",
    "Parte 1: GEN-6.3.2-00A",
    "Parte 1: REG-6.3.2-00B",
    "Parte 1: REG-6.3.2-01",
    "Parte 1: REG-6.3.2-02",
    "Parte 1: GEN-6.3.3-01",
    "Parte 1: GEN-6.3.3-02",
    "Parte 1: GEN-6.3.3-02A",
    "Parte 1: GEN-6.3.3-03",
    "Parte 1: GEN-6.3.3-05",
    "Parte 1: GEN-6.3.3-06",
    "Parte 1: GEN-6.3.3-07",
    "Parte 1: GEN-6.3.3-08",
    "Parte 1: SDP-6.3.3-09A",
    "Parte 1: GEN-6.3.3-10",
    "Parte 1: GEN-6.3.3-11",
    "Parte 1: GEN-6.3.3-12",
    "Parte 1: OVR-6.3.4-01",
    "Parte 1: REG-6.3.4-02",
    "Parte 1: REG-6.3.4-03",
    "Parte 1: OVR-6.3.4-04",
    "Parte 1: OVR-6.3.4-05",
    "Parte 1: OVR-6.3.4-06",
    "Parte 1: REG-6.3.4-07",
    "Parte 1: REG-6.3.4-08",
    "Parte 1: REG-6.3.4-09",
    "Parte 1: REG-6.3.4-10A",
    "Parte 1: REG-6.3.4-11A",
    "Parte 1: REG-6.3.4-12",
    "Parte 1: REG-6.3.4-13",
    "Parte 1: REG-6.3.4-16",
    "Parte 1: REG-6.3.4-17",
    "Parte 1: OVR-6.3.5-01",
    "Parte 1: OVR-6.3.5-02",
    "Parte 1: OVR-6.3.5-03",
    "Parte 1: OVR-6.3.5-04",
    "Parte 1: OVR-6.3.5-05",
    "Parte 1: OVR-6.3.5-06",
    "Parte 1: clausola 6.3.6 (premessa)",
    "Parte 1: REG-6.3.6-01A",
    "Parte 1: REG-6.3.6-02",
    "Parte 1: REG-6.3.6-06",
    "Parte 1: REG-6.3.6-07",
    "Parte 1: REG-6.3.6-08",
    "Parte 1: GEN-6.3.6-10",
    "Parte 1: clausola 6.3.7 (premessa)",
    "Parte 1: REG-6.3.7-01A",
    "Parte 1: REG-6.3.7-01B",
    "Parte 1: REG-6.3.7-02A",
    "Parte 1: REG-6.3.7-03",
    "Parte 1: REG-6.3.7-04",
    "Parte 1: REG-6.3.7-05",
    "Parte 1: REG-6.3.7-06",
    "Parte 1: clausola 6.3.8 (premessa)",
    "Parte 1: REG-6.3.8-01A",
    "Parte 1: REG-6.3.8-02",
    "Parte 1: REV-6.3.9-01",
    "Parte 1: REV-6.3.9-02",
    "Parte 1: REV-6.3.9-03",
    "Parte 1: REV-6.3.9-04",
    "Parte 1: CSS-6.3.9-05",
    "Parte 1: CSS-6.3.9-06",
    "Parte 1: CSS-6.3.9-07",
    "Parte 1: CSS-6.3.9-08",
    "Parte 1: CSS-6.3.9-12",
    "Parte 1: CSS-6.3.9-13",
    "Parte 1: CSS-6.3.9-14",
    "Parte 1: REV-6.3.9-15",
    "Parte 1: REV-6.3.9-15A",
    "Parte 1: REV-6.3.9-16",
    "Parte 1: REV-6.3.9-17",
    "Parte 1: REV-6.3.9-18",
    "Parte 1: REV-6.3.9-19",
    "Parte 1: CSS-6.3.10-01",
    "Parte 1: CSS-6.3.10-01A",
    "Parte 1: CSS-6.3.10-01B",
    "Parte 1: CSS-6.3.10-02",
    "Parte 1: CSS-6.3.10-03",
    "Parte 1: CSS-6.3.10-04",
    "Parte 1: CSS-6.3.10-05",
    "Parte 1: CSS-6.3.10-06",
    "Parte 1: CSS-6.3.10-07",
    "Parte 1: CSS-6.3.10-08",
    "Parte 1: CSS-6.3.10-09",
    "Parte 1: CSS-6.3.10-09A",
    "Parte 1: CSS-6.3.10-10",
    "Parte 1: clausola 6.3.11",
    "Parte 1: SDP-6.3.12-01",
    "Parte 1: SDP-6.3.12-02",
    "Parte 1: SDP-6.3.12-03",
    "Parte 1: SDP-6.3.12-04",
    "Parte 1: SDP-6.3.12-05",
    "Parte 1: SDP-6.3.12-06",
    "Parte 1: SDP-6.3.12-07",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from seed_data.lib import verifica_copertura, verifica_completezza_testo_integrale

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    verifica_completezza_testo_integrale([sys.modules["__main__"]])
    print(
        f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
        f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti."
    )
