"""ETSI TS 119 431-2 V1.2.1 (2023-06) - Electronic Signatures and Trust
Infrastructures (ESI); Policy and security requirements for trust service
providers; Part 2: TSP service components supporting AdES digital signature
creation. Fonte 12 (numerazione definitiva cablata dalla sessione principale
in app/seed.py - questo modulo NON tocca seed.py). Capitolo 1: clausole 1
(Scope), 2 (References, normative e informative), 3 (Definition of terms,
symbols, abbreviations and notations: 3.1 Terms, 3.2 Symbols, 3.3
Abbreviations, 3.4 Notations), 4 (General concepts: 4.1 General policy
requirements concepts, 4.2 SCASC applicable documentation con le sue
sottoclausole 4.2.1-4.2.4, 4.3 Architecture), 5 (Risk assessment), 6
(Policies and practices: 6.1 Trust service practice statement, 6.2 Terms and
Conditions, 6.3 Information security policy). Testo ufficiale in
app/.source_cache/etsi_119_431_2/cap01.txt. Manifest di split:
app/.source_cache/etsi_119_431_2/manifest.json.

Soggetto obbligato tipico di questo documento: lo SCASP (Signature Creation
Application Service Provider), il TSP che opera un SCASC (Signature Creation
Application Service Component) - categoria "QTSP/gestore", ruolo
"obbligato" per tutti gli Obblighi di questo capitolo.

Modellazione (ADR-0007), stesso criterio già applicato a ETSI EN 319 401
(Fonte 10) e a ETSI TS 119 431-1 (Fonte 11, capitolo gemello) per uno
standard tecnico ETSI a clausole/sottoclausole con requisiti numerati
(prefisso OVR-, "General requirement", clausola 3.4) invece di
articoli/commi di un atto legislativo:

- Clausola 1 (Scope) -> 1 Principio "scopo/ambito di applicazione",
  riferimento "clausola 1 (Scope)". Testo integrale riportato per intero
  (perimetro del documento: SCASC come componente di servizio TSP che
  implementa un'applicazione di creazione di firma AdES; nessuna
  restrizione sul tipo di TSP; NOTE 1-4 mantenute perché precisano
  l'applicabilità al Regolamento (UE) 910/2014, il contenuto dell'annesso
  B, i tipi di firma/sigillo coperti e i rinvii a ETSI EN 319 403 e ETSI TS
  119 432). oggetti_giuridici valorizzato con le quattro forme di firma/
  sigillo esplicitamente elencate nella NOTE 2 (qualificata, avanzata, per
  entrambe le funzioni firma e sigillo).
- Clausola 2 (References, 2.1 Normative + 2.2 Informative) -> NESSUN nodo:
  è bibliografia/paratesto puro (elenco di documenti citati con numerazione
  [1]-[9]/[i.1]-[i.10], nessun contenuto normativo autonomo), stesso
  trattamento già riservato alla clausola 2 di ETSI EN 319 401 (Fonte 10),
  ETSI TS 119 461 (Fonte 9) e ETSI EN 319 412-5 (Fonte 7). Non genera un
  item di indice.
- Clausola 3.1 (Terms) -> 1 Principio "definitorio" riassuntivo (non un
  nodo per singolo termine: la clausola è un glossario alfabetico piatto
  senza struttura a lettere/numeri propria, 16 termini specifici del
  documento oltre a quelli richiamati per rinvio da ETSI TR 119 001
  [i.2]). Testo integrale riportato per intero, incluse le due NOTE interne
  (su "signature applicability rules" e su "signature creation
  application") che aggiungono contenuto interpretativo.
- Clausola 3.2 (Symbols) -> NESSUN nodo: il testo è integralmente "Void."
  senza alcun contenuto oltre il rinvio strutturale, stesso trattamento
  già riservato alla clausola 3.2 di ETSI EN 319 401 (Fonte 10). Non genera
  un item di indice.
- Clausola 3.3 (Abbreviations) -> 1 Principio "definitorio" riassuntivo. 14
  abbreviazioni (CA, DTBSR, OID, QES, SCA, SCASC, SCASP, SCDev, SD, SLA,
  SSASC, SSASP, TSA, URI), riportate per intero e nell'ordine del testo
  ufficiale.
- Clausola 3.4 (Notations) -> 1 Principio "definitorio", riferimento
  "clausola 3.4 (Notations)". NODO CRUCIALE per l'intero documento e per il
  capitolo 2 (clausole 7-9): riporta la legenda COMPLETA e verbatim del
  formato identificativo dei requisiti (<3 lettere identificanti
  l'elemento di servizio>-<numero di clausola>-<numero progressivo a 2
  cifre>), delle due marcature - nessuna marcatura (requisito applicabile a
  qualunque TSP conforme) e "[CONDITIONAL]" (requisito applicabile solo a
  certe condizioni) - e delle due sole famiglie di prefisso usate nel
  documento: OVR (requisito generale applicabile a più di un componente) e
  ASI (interfaccia di firma AdES, usata nel capitolo 2). Include anche le
  regole di gestione degli identificativi nelle edizioni successive
  (inserimento a fine clausola, inserimento intermedio con lettera
  suffissa, "VOID" per requisito eliminato, lettera suffissa per requisito
  modificato) - regola che spiega direttamente perché nel testo di questo
  stesso capitolo compaiono id come "OVR-6.2-03A".
- Clausola 4.1 (General policy requirements concepts) -> 1 Principio
  "scopo/ambito di applicazione", riferimento "clausola 4.1 (General policy
  requirements concepts)". Dichiara che il documento è strutturato in linea
  con ETSI EN 319 401, ne incorpora i requisiti per riferimento e aggiunge
  requisiti specifici per lo SCASP - è cornice di rapporto tra i due
  documenti, non definizione di un concetto nuovo, per cui "scopo/ambito di
  applicazione" è più preciso di "definitorio" (stesso criterio già
  applicato alla clausola 4.1 "General" di ETSI EN 319 401, Fonte 10).
  Testo integrale riportato verbatim incluso il refuso ripetuto "guidance
  for guidance" presente nel testo ufficiale (non emendato: non è compito
  di questo censimento correggere il testo normativo).
- Clausola 4.2 (SCASC applicable documentation) -> NESSUN nodo proprio: è
  solo un titolo di raggruppamento senza testo introduttivo autonomo, il
  contenuto normativo è interamente nelle sue quattro sottoclausole.
  - 4.2.1 (SCASC practice statement) -> 1 Principio "definitorio": lo
    SCASP sviluppa/implementa/applica/aggiorna la SCASC practice statement
    (istanza della trust service practice statement di ETSI EN 319 401 per
    un SCASC, v. clausola 6.1), ne è proprietario, i destinatari sono
    auditor/subscriber/relying party; l'Annex A fornisce un indice
    raccomandato.
  - 4.2.2 (SCASC policy) -> 1 Principio "definitorio": descrive cosa offre
    una SCASC policy (indipendente dall'ambiente operativo specifico di
    uno SSASP) e riporta per intero, verbatim, i due OID specifici che il
    documento definisce (l'OID "main" per la conformità ai requisiti
    normativi principali esclusa l'annex B, l'OID "eu-advanced-x509" per
    la conformità che include anche l'annex B) - OID richiamati
    esplicitamente dagli Obblighi OVR-6.2-03/03A/04/05 di clausola 6.2.
  - 4.2.3 (Terms and conditions) -> 1 Principio "definitorio": lo SCASP
    emette anche i terms and conditions (v. clausola 6.2), specifici dello
    SCASP, con destinatari subscriber e relying party.
  - 4.2.4 (Other documents associated with signature creation) -> 1
    Principio "definitorio": introduce due ulteriori tipi di documento
    fuori dall'ambito della SCASC practice statement - la signature
    creation policy (vincoli di creazione della firma processati dalla
    SCA, identificabile con un OID) e le signature applicability rules
    (strutturabili secondo ETSI TS 119 172-1, fuori scope del presente
    documento) - e ne chiarisce la relazione/i rispettivi proprietari
    (SCASP per la practice statement, tipicamente il firmatario per le
    applicability rules).
  - 4.3 (Architecture) -> 1 Principio "definitorio", riferimento "clausola
    4.3 (Architecture)": descrive il funzionamento del SCASC (riceve
    documento/hash e parametri di firma, prepara la Data To Be Signed
    Representation - DTBSR, la invia allo SCDev, che può essere
    nell'ambiente dell'utente o gestito da remoto da un SSASC come
    descritto in ETSI TS 119 431-1 [i.8]), incluso il richiamo alla
    didascalia della Figura 1. Il rinvio a ETSI TS 119 431-1 [i.8] e a EN
    419241-1 [i.4] è riportato solo nel testo (nessuna relazione cross-
    fonte: deferita alla Fase 6 - pipeline dedicata della sessione
    principale, come da vincolo operativo di questo import).
- Clausola 5 (Risk assessment) -> 1 Obbligo OVR-5-01 (incorporazione per
  riferimento della clausola 5 di ETSI EN 319 401), tipo "organizzativo",
  categoria soggetto "QTSP/gestore", ruolo "obbligato" - stessa
  classificazione già usata per l'identica clausola di incorporazione in
  ETSI TS 119 461 (Fonte 9, cap02/cap03: OVR-5-01, OVR-6.1-01, OVR-6.2-01,
  OVR-6.3-01, OVR-7.x-01 tutti "organizzativo").
- Clausola 6.1 (Trust service practice statement) -> 6 Obblighi
  OVR-6.1-01..06, tutti "organizzativo" (specificano il contenuto della
  SCASC practice statement, coerente con la classificazione "organizzativo"
  già usata in ETSI EN 319 401 cap02.py per i REQ-6.1-03/04/05 di
  contenuto analogo, incluso REQ-6.1-04 che ha testo pressoché identico a
  OVR-6.1-06 sugli obblighi delle organizzazioni esterne). OVR-6.1-02 porta
  la marcatura "[CONDITIONAL]" (si applica solo se il SCASC supporta
  l'inclusione di marche temporali nella firma AdES) -> valorizzato
  condizione_applicabilita.
- Clausola 6.2 (Terms and Conditions) -> 10 Obblighi OVR-6.2-01..10 (incluso
  OVR-6.2-03A, inserito come requisito intermedio con lettera suffissa
  secondo la regola di clausola 3.4), tutti "organizzativo" (specificano il
  contenuto dei terms and conditions dello SCASC), stesso criterio delle
  clausole 6.1/6.3. OVR-6.2-03 è formulato con "may" (facoltà, non obbligo
  stringente) ma resta un requisito numerato con id OVR ai sensi della
  classificazione di clausola 3.4 ("The requirements identified in the
  present document include..."): modellato come Obbligo con la facoltà
  esplicitata nella sintesi italiana, coerente con l'obbligo di copertura
  ADR-0007 per ogni requisito numerato indipendentemente dal verbo modale
  usato. OVR-6.2-03A porta la marcatura "[Conditional]" (si applica solo
  se i terms and conditions referenziano una trust service policy con un
  OID diverso da quelli di clausola 4.2.2) -> valorizzato
  condizione_applicabilita; il rinvio interno a "requirements in clause 9"
  è riportato solo nel testo (clausola 9 appartiene al capitolo 2 di questa
  stessa fonte - non generata una relazione "specifica" perché il
  riferimento esatto del nodo in cap02.py non è verificabile da questo
  capitolo senza leggere cap02.py; si preferisce ometterla piuttosto che
  inventarla, come da vincolo operativo). OVR-6.2-07 include l'elenco
  puntato a)-d) delle opzioni minime da descrivere nei terms and
  conditions, riportato per intero.
- Clausola 6.3 (Information security policy) -> 2 Obblighi OVR-6.3-01
  (incorporazione per riferimento, "organizzativo") e OVR-6.3-02 (formulato
  con "should"; documentare i controlli di sicurezza e privacy a tutela dei
  dati personali, incluso il caso in cui il SCASP abbia accesso al
  documento da firmare - "tecnico/sicurezza" per il contenuto
  specificamente securitario/di protezione dati, a differenza delle
  clausole 6.1/6.2 che riguardano il contenuto documentale generale della
  pratica/dei termini contrattuali).

RELAZIONI: nessuna relazione interna. I dieci nodi Principio di clausole
1-4 sono cornice definitoria/di ambito autonoma (scope, glossario termini/
abbreviazioni, notazione degli id, documentazione applicabile,
architettura) senza citazione testuale esplicita dell'id di un requisito di
clausola 5/6 al loro interno. I diciannove Obblighi di clausole 5-6 sono
prevalentemente incorporazioni per riferimento di ETSI EN 319 401 (fonte
esterna non censita in questo grafo - nessuna relazione, solo menzione nel
testo) o requisiti autonomi elencati in sequenza, senza citazione testuale
esplicita dell'id di un altro requisito dello stesso capitolo (l'unico
rinvio interno esplicito, OVR-6.2-03A -> "clause 9", punta al capitolo 2 di
questa stessa fonte e non è verificabile senza leggerne il modulo - omesso
per lo stesso vincolo operativo sopra descritto). Nessuna relazione
cross-fonte: deferite alla Fase 6 (pipeline dedicata della sessione
principale, ADR-0009).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "OVR-5-01",
        "testo": (
            "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 5 (valutazione del rischio)."
        ),
        "testo_integrale": (
            "OVR-5-01: The requirements specified in ETSI EN 319 401 [9], clause 5 shall apply."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.1-01",
        "testo": (
            "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 6.1 (trust service practice "
            "statement); si applicano inoltre i requisiti particolari seguenti (OVR-6.1-02 - OVR-6.1-06)."
        ),
        "testo_integrale": (
            "OVR-6.1-01: The requirements specified in ETSI EN 319 401 [9], clause 6.1 shall apply. In "
            "addition, the following particular requirements apply:"
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.1-02",
        "testo": (
            "[CONDITIONAL] Quando il SCASC supporta l'inclusione di marche temporali (time-stamp token) "
            "nella firma digitale AdES, la SCASC practice statement deve elencare quali TSA (Time-Stamping "
            "Authority) sono utilizzate."
        ),
        "testo_integrale": (
            "OVR-6.1-02: [CONDITIONAL] When the SCASC supports the inclusion of time-stamp tokens in the "
            "AdES digital signature, the SCASC practice statement shall list which TSA are used."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Quando il SCASC supporta l'inclusione di marche temporali (time-stamp token) nella firma "
            "digitale AdES."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.1-03",
        "testo": "La SCASC practice statement deve specificare tutte le signature creation policy supportate.",
        "testo_integrale": (
            "OVR-6.1-03: The SCASC practice statement shall specify all the supported signature creation "
            "polices."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.1-04",
        "testo": "La SCASC practice statement deve specificare tutti i formati di firma supportati.",
        "testo_integrale": (
            "OVR-6.1-04: The SCASC practice statement shall specify all the supported signature formats."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.1-05",
        "testo": (
            "La SCASC practice statement deve specificare tutte le classi di firma supportate. NOTA: ETSI "
            "TS 119 102-1 descrive le diverse classi di firma."
        ),
        "testo_integrale": (
            "OVR-6.1-05: The SCASC practice statement shall specify all the supported signature classes. "
            "NOTE: ETSI TS 119 102-1 [2] describes different signature classes."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.1-06",
        "testo": (
            "Lo SCASP deve identificare, nella SCASC practice statement, gli obblighi di tutte le "
            "organizzazioni esterne che supportano i suoi servizi, incluse le politiche e prassi applicabili."
        ),
        "testo_integrale": (
            "OVR-6.1-06: The SCASP shall identify in the SCASC practice statements the obligations of all "
            "external organizations supporting its services including the applicable policies and practices."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-01",
        "testo": (
            "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 6.2 (terms and conditions); "
            "si applicano inoltre i requisiti particolari seguenti (OVR-6.2-02 - OVR-6.2-10)."
        ),
        "testo_integrale": (
            "OVR-6.2-01: The requirements specified in ETSI EN 319 401 [9], clause 6.2 shall apply. In "
            "addition, the following particular requirements apply:"
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-02",
        "testo": (
            "Per specificare la trust service policy applicata, i terms and conditions del SCASC devono "
            "elencare o richiamare (es. tramite OID), e descrivere brevemente, le SCASC policy supportate a "
            "cui si conforma."
        ),
        "testo_integrale": (
            "OVR-6.2-02: To specify the trust service policy being applied, the SCASC terms and conditions "
            "shall list or make reference to (e.g. through OIDs), and briefly describe, the supported SCASC "
            "policies it conforms to."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-03",
        "testo": (
            "Per specificare la trust service policy applicata, i terms and conditions del SCASC possono "
            "(facoltativamente) utilizzare gli OID definiti in clausola 4.2.2."
        ),
        "testo_integrale": (
            "OVR-6.2-03: To specify the trust service policy being applied, the SCASC terms and conditions "
            "may use the OIDs defined in clause 4.2.2."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-03A",
        "testo": (
            "[Conditional] Se i terms and conditions del SCASC fanno riferimento a una trust service policy "
            "tramite un OID diverso da quelli definiti in clausola 4.2.2, la trust service policy "
            "referenziata deve rispettare i requisiti della clausola 9."
        ),
        "testo_integrale": (
            "OVR-6.2-03A: [Conditional] If the SCASC terms and conditions reference a trust service policy "
            "using an OID other than the ones defined in clause 4.2.2, then the referenced trust service "
            "policy shall comply with requirements in clause 9."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Se i terms and conditions del SCASC fanno riferimento a una trust service policy tramite un "
            "OID diverso da quelli definiti in clausola 4.2.2."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-04",
        "testo": (
            "L'OID principale ('main'), come definito in clausola 4.2.2, deve essere utilizzato in "
            "relazione a un SCASC solo se il SCASC si conforma ai requisiti normativi della parte "
            "principale del presente standard (esclusa l'annex B)."
        ),
        "testo_integrale": (
            "OVR-6.2-04: The main OID, as defined in clause 4.2.2, shall only be used in relation with an "
            "SCASC if the SCASC conforms to the normative requirements in the main part of the present "
            "standard (excluding annex B)."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-05",
        "testo": (
            "L'OID 'eu-advanced-x509', come definito in clausola 4.2.2, deve essere utilizzato in relazione "
            "a un SCASC solo se il SCASC si conforma ai requisiti normativi della parte principale del "
            "presente standard e a quelli dell'annex B."
        ),
        "testo_integrale": (
            "OVR-6.2-05: The eu-advanced-x509 OID, as defined in clause 4.2.2, shall only be used in "
            "relation with an SCASC if the SCASC conforms to the normative requirements in the main part of "
            "the present standard and the ones in annex B."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-06",
        "testo": "I terms and conditions devono indicare i diritti e gli obblighi dello SCASP e del firmatario.",
        "testo_integrale": (
            "OVR-6.2-06: The terms and conditions shall indicate the rights and obligations of the SCASP "
            "and the signer."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-07",
        "testo": (
            "I terms and conditions devono descrivere le opzioni supportate dal servizio; almeno: a) i "
            "formati di firma supportati (esempio: CAdES, XAdES o PAdES); b) i parametri di firma "
            "supportati; c) se il documento da firmare può essere fornito solo come hash; e d) i "
            "Signature Creation Device (SCDev) supportati nell'ambiente dell'utente, o gli SSASC supportati "
            "che creano il valore della firma digitale per il firmatario."
        ),
        "testo_integrale": (
            "OVR-6.2-07: The terms and conditions shall describe the options supported by the service. At "
            "least: a) the supported signature formats; EXAMPLE: CAdES [3], [4], XAdES [5], [6] or PAdES "
            "[7], [8]. b) the supported signature parameters; c) if the to be signed document can be "
            "provided only as a hash; and d) the supported Signature Creation Devices (SCDev) in the user's "
            "environment or the supported SSASCs creating the digital signature value for the signer."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-08",
        "testo": (
            "I terms and conditions devono includere elementi di Service-Level Agreement (SLA) per la "
            "disponibilità del servizio e, ove applicabile, altre informazioni SLA come i tempi di risposta."
        ),
        "testo_integrale": (
            "OVR-6.2-08: The terms and conditions shall include Service-Level Agreement (SLA) elements for "
            "the availability of the service and when applicable, other SLA information such as response "
            "times."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-09",
        "testo": (
            "I terms and conditions devono fornire un avviso che l'SLA può essere condizionato dalle "
            "prassi, politiche e SLA di altri TSP non sotto il controllo dello SCASP, come la CA che "
            "emette il certificato usato per la firma o una TSA usata per una marca temporale."
        ),
        "testo_integrale": (
            "OVR-6.2-09: The terms and conditions shall provide a notice that the SLA can be affected by "
            "the practices, policies and SLAs of other TSPs, not under the control of the SCASP like the "
            "CA issuing the certificate used for the signature or a TSA used for a time-stamp."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.2-10",
        "testo": "I terms and conditions devono spiegare come lo SCASP tratta i dati personali.",
        "testo_integrale": (
            "OVR-6.2-10: The terms and conditions shall explain how the SCASP processes personal data."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.3-01",
        "testo": (
            "Si applicano i requisiti specificati in ETSI EN 319 401, clausola 6.3 (politica di sicurezza "
            "delle informazioni); si applica inoltre il requisito particolare seguente (OVR-6.3-02)."
        ),
        "testo_integrale": (
            "OVR-6.3-01: The requirements specified in ETSI EN 319 401 [9], clause 6.3 shall apply. In "
            "addition, the following particular requirement apply:"
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-6.3-02",
        "testo": (
            "La politica di sicurezza dovrebbe documentare i controlli di sicurezza e privacy implementati "
            "per proteggere i dati personali. NOTA: se lo SCASP ha accesso al documento da firmare, questo "
            "può contenere informazioni confidenziali oltre che dati personali."
        ),
        "testo_integrale": (
            "OVR-6.3-02: The security policy should document the security and privacy controls implemented "
            "to protect personal data. NOTE: If the SCASP has access to the data-to-be-signed, then this "
            "can contain confidential information as well as personal data."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 1 (Scope)",
        "testo": (
            "Il documento specifica requisiti di policy e sicurezza per i Trust Service Provider (TSP) che "
            "implementano un componente di servizio a supporto della creazione di firme digitali AdES "
            "(Signature Creation Application Service Component - SCASC), che contiene una signature "
            "creation application ma non si limita ad essa. Nessuna restrizione sul tipo di TSP che lo "
            "implementa. NOTA 1: il documento è rivolto in particolare, ma non esclusivamente, ai servizi "
            "fiduciari che supportano la creazione di firme digitali ai sensi del Regolamento (UE) 910/2014 "
            "per firme e sigilli elettronici (avanzati e qualificati); l'annex B contiene requisiti "
            "specifici per il SCASC nel contesto del Regolamento (UE) 910/2014, orientati a firme e sigilli "
            "elettronici avanzati basati su certificati X.509. NOTA 2: le firme digitali del documento "
            "possono essere usate per creare firme elettroniche, firme elettroniche avanzate, firme "
            "elettroniche qualificate, sigilli elettronici, sigilli elettronici avanzati e sigilli "
            "elettronici qualificati ai sensi del Regolamento (UE) 910/2014. Il documento può essere usato "
            "da organismi competenti come base per confermare l'affidabilità di un'organizzazione nella "
            "creazione di firme digitali AdES (NOTA 3: v. ETSI EN 319 403 per la valutazione di conformità). "
            "Il SCASC ha connessioni con servizi fiduciari esterni contattabili ad esempio per fornire "
            "informazioni da includere nella firma; il documento non pone requisiti sulla trust service "
            "policy di tali servizi esterni, né specifica alcun protocollo di accesso al SCASC o di "
            "comunicazione con uno SSASC o uno SCDev (NOTA 4: i protocolli sono definiti in ETSI TS 119 "
            "432). Il documento individua i controlli specifici necessari ad affrontare i rischi specifici "
            "associati ai servizi di creazione di firma AdES."
        ),
        "testo_integrale": (
            "1 Scope: The present document provides policy and security requirements for Trust Service "
            "Providers (TSPs) implementing a service component supporting AdES digital signature creation. "
            "This component contains a signature creation application and is thus called Signature "
            "Creation Application Service Component (SCASC). However, it is more than just the SCA. It "
            "contains service elements around which parts of the driving application as defined in ETSI TS "
            "119 102-1 [2] and ETSI TS 119 101 [1] can be implemented. The present document does not give "
            "restrictions on whether something is covered within a signature creation application or "
            "outside, as long as it is done by the SCASC. The present document gives no restrictions on "
            "the type of TSP implementing such a service component. The present document aims at "
            "supporting the creation of digital signatures in European and other regulatory frameworks. "
            "NOTE 1: Specifically, but not exclusively, the present document is aimed at trust services, "
            "supporting the creation of digital signatures in accordance with the requirements of the "
            "Regulation (EU) No 910/2014 [i.1] for electronic signatures and electronic seals (both "
            "advanced and qualified). Annex B contains specific requirements for SCASC in the context of "
            "Regulation (EU) No 910/2014 which aim at providing best practice requirements for the "
            "creation of advanced electronic signatures and seals based on X.509 certificates. NOTE 2: "
            "Specifically, but not exclusively, digital signatures in the present document can be used to "
            "create electronic signatures, advanced electronic signatures, qualified electronic signatures, "
            "electronic seals, advanced electronic seals, and qualified electronic seals as per Regulation "
            "(EU) No 910/2014 [i.1]. The present document may be used by competent bodies as the basis for "
            "confirming that an organization is trustworthy in creating AdES digital signatures. NOTE 3: "
            "See ETSI EN 319 403 [i.6] for guidance on assessment of TSP processes and services. The SCASC "
            "has connections with external (trust) services that can be contacted for example for "
            "provisioning information to be included within the signature. The present document does not "
            "put requirements on the trust service policy applied by such external services. The present "
            "document does not specify any protocol used to access the SCASC or how the SCACS can contact "
            "an SSASC or an SCDev. NOTE 4: Protocols to contact a SCASC or a SSASC are defined in ETSI TS "
            "119 432 [i.9]. The present document identifies specific controls needed to address specific "
            "risks associated with services providing AdES signature creation."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": [
            "firma elettronica qualificata",
            "sigillo elettronico qualificato",
            "firma elettronica avanzata",
            "sigillo elettronico avanzato",
        ],
    },
    {
        "riferimento": "clausola 3.1 (Terms)",
        "testo": (
            "La clausola definisce, oltre ai termini richiamati per rinvio da ETSI TR 119 001, un glossario "
            "di 16 termini specifici del documento: AdES (digital) signature (firma digitale CAdES, PAdES o "
            "XAdES); digital signature (dato allegato o trasformazione crittografica di un'unità di dati che "
            "consente di provarne origine e integrità e protegge dalla contraffazione); digital signature "
            "value (risultato della trasformazione crittografica con la stessa funzione); remote signature "
            "creation device (dispositivo di creazione firma usato da remoto rispetto al firmatario, "
            "controlla l'operazione di firma per suo conto); server signing application (applicazione che "
            "usa un remote signature creation device per creare un valore di firma digitale per conto di un "
            "firmatario) e i relativi service component/service provider (SSASC/SSASP); signature "
            "applicability rules (insieme di regole che definiscono i requisiti per stabilire se una firma è "
            "idonea a uno scopo di business o legale determinato - possono essere implicite o esplicite, "
            "anche in forma elaborabile da macchina secondo ETSI TS 119 172-1); signature creation "
            "application (applicazione che crea la firma digitale AdES e si affida allo SCDev per creare il "
            "valore di firma - nota: lo SCDev può essere gestito dallo SSASC) e i relativi service "
            "component/service provider (SCASC/SCASP); signature creation constraint (criteri usati nella "
            "creazione di una firma digitale); signature creation device (software o hardware configurato "
            "per implementare i dati di creazione della firma e creare un valore di firma digitale); "
            "signature creation policy (insieme dei vincoli di creazione firma processati dalla SCA); "
            "signature creation service (servizio TSP che implementa una signature creation application e/o "
            "una server signing application); signature creation service provider (fornitore di servizio di "
            "creazione firma, nota: come in EN 419 241-1)."
        ),
        "testo_integrale": (
            "3.1 Terms: For the purposes of the present document, the terms given in ETSI TR 119 001 [i.2] "
            "and the following apply: AdES (digital) signature: digital signature that is either a CAdES "
            "signature, or a PAdES signature or a XAdES signature digital signature: data appended to, or "
            "a cryptographic transformation of a data unit that allows a recipient of the data unit to "
            "prove the source and integrity of the data unit and protect against forgery e.g. by the "
            "recipient digital signature value: result of the cryptographic transformation of a data unit "
            "that allows a recipient of the data unit to prove the source and integrity of the data unit "
            "and protect against forgery e.g. by the recipient remote signature creation device: signature "
            "creation device used remotely from signer perspective and provides control of signing "
            "operation on the signer's behalf server signing application: application using a remote "
            "signature creation device to create a digital signature value on behalf of a signer server "
            "signing application service component: TSP service component employing a server signing "
            "application server signing application service provider: TSP operating a server signing "
            "application service component signature applicability rules: set of rules, applicable to one "
            "or more digital signatures, that defines the requirements for determination of whether a "
            "signature is fit for a particular business or legal purpose NOTE: Signature applicability "
            "rules can be implicit, or can be stated in a human readable document and/or in a machine "
            "processable from. ETSI TS 119 172-1 [i.3] can be used for this purpose. signature creation "
            "application: application within the signature creation system that creates the AdES digital "
            "signature and relies on the SCDev to create a digital signature value NOTE: The SCDev can be "
            "managed by the SSASC. signature creation application service component: TSP service component "
            "employing a signature creation application signature creation application service provider: "
            "TSP operating a signature creation application service component signature creation "
            "constraint: criteria used when creating a digital signature signature creation device: "
            "configured software or hardware used to implement the signature creation data and to create a "
            "digital signature value signature creation policy: set of signature creation constraints "
            "processed or to be processed by the SCA signature creation service: TSP service implementing "
            "a signature creation application and/or a server signing application signature creation "
            "service provider: service provider offering a signature creation service NOTE: As in EN 419 "
            "241-1 [i.4]."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.3 (Abbreviations)",
        "testo": (
            "La clausola definisce, oltre alle abbreviazioni richiamate per rinvio da ETSI TR 119 001, 14 "
            "abbreviazioni specifiche del documento: CA (Certification Authority), DTBSR (Data To Be Signed "
            "Representation), OID (Object IDentifier), QES (Qualified Electronic Signature o Qualified "
            "Electronic Seal), SCA (Signature Creation Application), SCASC (Signature Creation Application "
            "Service Component), SCASP (Signature Creation Application Service Provider), SCDev (Signature "
            "Creation Device), SD (Signer's Document), SLA (Service-Level Agreement), SSASC (Server Signing "
            "Application Service Component), SSASP (Server Signing Application Service Provider), TSA "
            "(Time-Stamping Authority), URI (Uniform Resource Identifier)."
        ),
        "testo_integrale": (
            "3.3 Abbreviations: For the purposes of the present document, the abbreviations given in ETSI "
            "TR 119 001 [i.2] and the following apply: CA Certification Authority; DTBSR Data To Be Signed "
            "Representation; OID Object IDentifier; QES Qualified Electronic Signature or Qualified "
            "Electronic Seal; SCA Signature Creation Application; SCASC Signature Creation Application "
            "Service Component; SCASP Signature Creation Application Service Provider; SCDev Signature "
            "Creation Device; SD Signer's Document; SLA Service-Level Agreement; SSASC Server Signing "
            "Application Service Component; SSASP Server Signing Application Service Provider; TSA "
            "Time-Stamping Authority; URI Uniform Resource Identifier."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.4 (Notations)",
        "testo": (
            "I requisiti del documento comprendono: a) requisiti applicabili a qualunque TSP conforme, "
            "indicati da clausole senza marcatura aggiuntiva; b) requisiti applicabili solo a certe "
            "condizioni, indicati da clausole marcate '[CONDITIONAL]'. Gli identificativi dei requisiti "
            "seguono il formato <3 lettere identificanti l'elemento di servizio>-<numero di clausola>-<numero "
            "progressivo a 2 cifre>. Gli elementi di servizio sono: OVR (requisito generale, applicabile a "
            "più di un componente) e ASI (interfaccia di firma AdES). Nelle edizioni successive del "
            "documento: un requisito inserito a fine clausola incrementa il numero progressivo al successivo "
            "disponibile; un requisito inserito tra due requisiti esistenti è distinto da lettere "
            "maiuscole appese all'identificativo del requisito precedente; l'identificativo di un requisito "
            "eliminato resta e viene completato con 'VOID'; l'identificativo di un requisito modificato "
            "resta vuoto (void) e il requisito modificato è identificato da lettere maiuscole appese "
            "all'identificativo iniziale."
        ),
        "testo_integrale": (
            "3.4 Notations: The requirements identified in the present document include: a) requirements "
            "applicable to any TSP conforming to the present document. Such requirements are indicated by "
            "clauses without any additional marking; b) requirements applicable under certain conditions. "
            "Such requirements are indicated by clauses marked by \"[CONDITIONAL]\". The requirements in "
            "the present document are identified as follows: <the 3 letters identifying the elements of "
            "services >-< the clause number>- <2 digit number-incremental> The elements of services are: - "
            "OVR: General requirement (requirement applicable to more than 1 component) - ASI: AdES "
            "signing interface The management of the requirement identifiers for subsequent editions of "
            "the present document is as follows: - When a requirement is inserted at the end of a clause, "
            "the 2 digit number above is incremented to the next available digit. - When a requirement is "
            "inserted between two existing requirements, capital letters appended to the previous "
            "requirement identifier are used to distinguish new requirements. - The requirement identifier "
            "for a deleted requirements is left and completed with \"VOID\". - The requirement identifier "
            "for a modified requirement is left void and the modified requirement is identified by capital "
            "letter(s) appended to the initial requirement number."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.1 (General policy requirements concepts)",
        "testo": (
            "Il documento è strutturato in linea con ETSI EN 319 401, di cui incorpora i requisiti per "
            "riferimento, aggiungendo i requisiti specifici rilevanti per lo SCASP; per guida sui requisiti "
            "di policy generali si rinvia a ETSI EN 319 401, clausola 4."
        ),
        "testo_integrale": (
            "4.1 General policy requirements concepts: The present document is structured in line with "
            "ETSI EN 319 401 [9]. It incorporates ETSI EN 319 401 [9] requirements by reference and adds "
            "requirements relevant for a SCASP. See ETSI EN 319 401 [9], clause 4 for guidance for "
            "guidance on general policy requirements."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.2.1 (SCASC practice statement)",
        "testo": (
            "Lo SCASP sviluppa, implementa, applica e aggiorna una SCASC practice statement, istanza della "
            "trust service practice statement definita in ETSI EN 319 401 per un signature creation "
            "application service component (v. clausola 6.1). La SCASC practice statement descrive come lo "
            "SCASP opera il proprio servizio, è di proprietà dello SCASP ed è adattata alla struttura "
            "organizzativa, alle procedure operative, alle strutture e all'ambiente informatico del TSP; i "
            "destinatari possono essere auditor, subscriber e relying party. NOTA: la presenza di alcuni "
            "elementi è obbligatoria come richiesto dal documento, ma non ci sono restrizioni sulla forma "
            "(può essere inclusa in una practice statement generale del TSP che copra altri servizi, o "
            "essere un documento a sé stante); l'annex A fornisce un indice raccomandato. Il documento "
            "fornisce i requisiti individuati come necessari per supportare una SCASC policy di alto "
            "livello, da approvare da parte dello SCASP e riflettere nella propria practice statement."
        ),
        "testo_integrale": (
            "4.2.1 Signature creation application service component practice statement: The Signature "
            "Creation Application Service Provider (SCASP) develops, implements, enforces, and updates a "
            "SCASC practice statement which is a trust service practice statement such as defined in ETSI "
            "EN 319 401 [9], instantiated for a signature creation application service component. See "
            "clause 6.1. The SCASC practice statement describes how the SCASP operates its service and is "
            "owned by the SCASP. The SCASC practice is tailored to the organizational structure, operating "
            "procedures, facilities, and computing environment of a TSP. The recipients of the practice "
            "statement can be auditors, subscribers and relying parties. NOTE: The presence of some "
            "elements is mandatory in the SCASC practice statement as requested in the present document, "
            "however the present document places no restriction on the form of the SCASC practice "
            "statement; it can be included in a general TSP practice statement document that covers other "
            "services delivered by that TSP or it can be a standalone document. Annex A provides a "
            "recommended table of content. The present document provides requirements identified as "
            "necessary to support a high-level SCASC policy, to be endorsed by a SCASP and reflected in "
            "its practice statement."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.2.2 (SCASC policy)",
        "testo": (
            "Una SCASC policy descrive cosa è offerto e può contenere informazioni ulteriori rispetto "
            "all'ambito del documento, per indicare l'applicabilità del servizio; è definita "
            "indipendentemente dai dettagli specifici dell'ambiente operativo di uno SSASP. I destinatari "
            "possono essere auditor, subscriber e relying party. Gli SCASP conformi ai requisiti normativi "
            "del documento esclusi quelli dell'annex B possono usare nella propria documentazione l'OID "
            "'main' (itu-t(0) identified-organization(4) etsi(0) CREATION SERVICE-policies(19431) ades(2) "
            "policy-identifiers(1) main(1)); gli SCASP conformi ai requisiti normativi del documento "
            "inclusi quelli dell'annex B possono usare l'OID 'eu-advanced-x509' (itu-t(0) "
            "identified-organization(4) etsi(0) CREATION SERVICE-policies(19431) ades(2) "
            "policy-identifiers(1) eu-advanced-x509(2)). La SCASC policy non fa necessariamente parte della "
            "documentazione dello SCASP (secondo ETSI EN 319 401 una practice statement e i termini e "
            "condizioni generali sono sufficienti); può essere condivisa da una comunità e non di proprietà "
            "dello SCASP, e non ci sono vincoli sulla forma (documento a sé stante o parte della practice "
            "statement e/o dei termini e condizioni generali) né sul contenuto, fermo restando che lo SCASP "
            "deve fornire informazioni minime sul servizio offerto (v. clausole 6.1 e 6.2)."
        ),
        "testo_integrale": (
            "4.2.2 Signature creation application service component policy: A SCASC policy describes what "
            "is offered and can contain diverse information beyond the scope of the present document to "
            "indicate the applicability of the service. A SCASC policy is defined independently of the "
            "specific details of the specific operating environment of a SSASP. The recipients of the "
            "service policy can be auditors, subscribers and relying parties. The present document can be "
            "referred by such a SCASC policy to provide information about the level of the service. SCASPs "
            "conforming to the present document's normative requirements except those defined in annex B "
            "may use in its documentation the following specific OID: itu-t(0) identified-organization(4) "
            "etsi(0) CREATION SERVICE-policies(19431) ades (2) policy-identifiers(1) main (1) SCASPs "
            "conforming to the present document's normative requirements including those defined in annex "
            "B may use in its documentation the following specific OID: itu-t(0) identified-organization(4) "
            "etsi(0) CREATION SERVICE-policies(19431) ades (2) policy-identifiers(1) eu-advanced- x509 (2) A "
            "SCASC policy is not necessarily part of the SCASP's documentation (as per ETSI EN 319 401 [9] "
            "a practice statement and general terms and conditions are sufficient); e.g. a SCASC policy can "
            "be shared by a community and not owned by the SCASP. Also, the present document does not put "
            "constraints on the form of the SCASC policies; a SCASC policy can be a stand-alone document or "
            "be provided as part of the practice statements and/or the general terms and conditions. The "
            "present document does not put any limitation on the content of the SCASC policies but it is "
            "requested that the SCASP provides minimal information about the service it offers (see "
            "clauses 6.1 and 6.2)."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.2.3 (Terms and conditions)",
        "testo": (
            "Oltre alla SCASC practice statement e, quando emessa, alla SCASC policy, lo SCASP emette anche "
            "termini e condizioni (v. clausola 6.2), che possono coprire un ampio ventaglio di termini "
            "commerciali o tecnici non necessariamente comunicati al cliente; sono specifici dello SCASP e "
            "i destinatari possono essere subscriber e relying party. NOTA: la presenza di alcuni elementi è "
            "obbligatoria come richiesto dal documento, ma non ci sono restrizioni sulla forma (documento a "
            "sé stante per il pubblico, o suddiviso tra accordo/i con il subscriber e informazioni per le "
            "relying party); forma e contenuto possono dipendere anche dalle normative nazionali."
        ),
        "testo_integrale": (
            "4.2.3 Terms and conditions: In addition to the SCASC practice statement and, when issued by "
            "the SCASP, the SCASC policy, the SCASP also issues terms and conditions, see clause 6.2. Terms "
            "and conditions can cover a broad range of commercial terms or technical terms that are not "
            "necessarily communicated to the customer, etc. The terms and conditions are specific to a "
            "SCASP. The recipients of the terms and conditions can be the subscribers and the relying "
            "parties. NOTE: The presence of some elements is mandatory in the terms and conditions as "
            "requested in the present document, however the present document places no restriction on the "
            "form of terms and conditions; it can be a standalone document for a public audience, or it can "
            "be split over subscriber's agreement(s) and information to relying parties. The form and "
            "content of the terms and conditions can also depend on national regulations."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.2.4 (Other documents associated with signature creation)",
        "testo": (
            "Oltre alla descrizione delle prassi impiegate dallo SCASP per offrire il servizio di creazione "
            "di firma AdES, è importante documentare i criteri di creazione delle firme e la loro idoneità a "
            "una determinata esigenza di business, tramite due possibili documenti: una signature creation "
            "policy, insieme dei vincoli di creazione firma processati dalla SCA, identificabile con un OID; "
            "oppure signature applicability rules, strutturabili secondo ETSI TS 119 172-1, che possono "
            "includere una signature creation policy oltre ad altri criteri sull'idoneità della firma creata "
            "rispetto a certe esigenze di business (NOTA: l'uso delle signature applicability rules è fuori "
            "dall'ambito del documento, ma può essere applicato come estensione al servizio di creazione "
            "firma). La SCASC practice statement, la signature creation policy e le signature applicability "
            "rules sono tipi di documentazione distinti: la practice statement descrive come lo SCASP opera "
            "il servizio, la signature creation policy stabilisce i vincoli processati dalla SCA nella "
            "creazione di una firma, le signature applicability rules vanno oltre e stabiliscono le regole e "
            "gli assunti usati da un utente per decidere se una firma creata secondo tali regole è idonea "
            "allo scopo. Il proprietario della SCASC practice statement è lo SCASP, mentre il proprietario "
            "delle signature applicability rules è di norma il firmatario."
        ),
        "testo_integrale": (
            "4.2.4 Other documents associated with signature creation: Besides the description of the "
            "practices employed by the SCASP to offer the AdES digital signature creation service, it is "
            "important to document the criteria under which the signatures are created and, beyond this, "
            "can then be determined as fitting a certain business need. Two documents can be used for "
            "these purposes: - A signature creation policy which is the set of signature creation "
            "constraints processed by the SCA. A signature creation policy can be identified by means of "
            "an OID. - Signature applicability rules that can be structured as per ETSI TS 119 172-1 [i.3] "
            "and can include a signature creation policy containing the signature creation constraints to "
            "be applied by the SCA, as well as other criteria showing the applicability of the created "
            "signature so certain business needs. NOTE: The use of signature applicability rules is "
            "outside the scope of the present document but can be applied as an extension to the signature "
            "creation service as covered by the present document. The SCASC practice statement, the "
            "signature creation policy and the signature applicability rules are different types of "
            "documentation; the SCASC practices statement describe how the SCASP operates its service, "
            "while the signature creation policy states the constraints to be processed by a SCA when "
            "creating a signature. Going beyond the scope of a signature creation policy, the signature "
            "applicability rules state the rules and assumptions used by a user to decide whether a "
            "signature created according to these rules is fit for purpose. The owner of the SCASC "
            "practice statement is a SCASP, while the owner of the signature applicability rules is usually "
            "the signatory."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3 (Architecture)",
        "testo": (
            "Un componente di servizio TSP a supporto della creazione di firme digitali AdES (SCASC) riceve "
            "il/i documento/i e/o hash da firmare ed eventuali parametri di firma, raccoglie le informazioni "
            "necessarie a creare la firma, prepara la Data To Be Signed Representation (DTBSR) e la invia "
            "allo SCDev. Lo SCDev può trovarsi nell'ambiente dell'utente oppure essere gestito da remoto da "
            "un Server Signing Application Service Component (SSASC), come descritto in ETSI TS 119 431-1. "
            "Ai fini del documento si assume che lo SCDev gestisca l'autenticazione e il consenso a firmare "
            "con l'utente e restituisca il valore della firma digitale, senza entrare nel dettaglio se ciò "
            "avvenga tramite lo SCDev stesso o il componente che lo gestisce; l'autorizzazione a usare la "
            "chiave di firma nello SCDev può avvenire tramite il SCASC oppure direttamente tra il firmatario "
            "e lo SCDev. Il valore della firma digitale è incluso dal SCASC nella firma digitale. NOTA: il "
            "SCASC rappresenta la signature creation application di EN 419241-1. La Figura 1 illustra le "
            "relazioni del componente di servizio TSP per la creazione di firma digitale AdES."
        ),
        "testo_integrale": (
            "4.3 Architecture: A TSP service component supporting AdES digital signature creation (SCASC) "
            "receives the document(s) and/or hash(es) of document(s) to be signed and optionally some "
            "signing parameters, collects all necessary information to create the signature, prepares the "
            "Data To Be Signed Representation (DTBSR) and sends this to the SCDev. The SCDev can be either "
            "in the user's environment or managed by a remote Server Signing Application Service Component "
            "(SSASC) as described in ETSI TS 119 431-1 [i.8]. For the purpose of the present document, it "
            "is assumed that the SCDev handles the authentication and the agreement to sign with the user "
            "and returns the digital signature value, without going into details if this is done by the "
            "SCDev itself or the component managing the SCDev. The authorization to use the signing key "
            "within the SCDev can go through the SCASC but can also be done directly by communication "
            "between the signer and the SCDev. The digital signature value is included by the SCASC into "
            "the digital signature. NOTE: The SCASC represents the signature creation application in EN "
            "419241-1 [i.4]. Figure 1: Relations of the TSP service component for AdES digital signature "
            "creation."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 1 (Scope)",
    "clausola 3.1 (Terms)",
    "clausola 3.3 (Abbreviations)",
    "clausola 3.4 (Notations)",
    "clausola 4.1 (General policy requirements concepts)",
    "clausola 4.2.1 (SCASC practice statement)",
    "clausola 4.2.2 (SCASC policy)",
    "clausola 4.2.3 (Terms and conditions)",
    "clausola 4.2.4 (Other documents associated with signature creation)",
    "clausola 4.3 (Architecture)",
    "OVR-5-01",
    "OVR-6.1-01",
    "OVR-6.1-02",
    "OVR-6.1-03",
    "OVR-6.1-04",
    "OVR-6.1-05",
    "OVR-6.1-06",
    "OVR-6.2-01",
    "OVR-6.2-02",
    "OVR-6.2-03",
    "OVR-6.2-03A",
    "OVR-6.2-04",
    "OVR-6.2-05",
    "OVR-6.2-06",
    "OVR-6.2-07",
    "OVR-6.2-08",
    "OVR-6.2-09",
    "OVR-6.2-10",
    "OVR-6.3-01",
    "OVR-6.3-02",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys

    referenziati = {rif for lista in MAPPATURA_LOCALE.values() for rif in lista}
    mancanti = set(INDICE_ARTICOLI_LOCALE) - referenziati
    extra = referenziati - set(INDICE_ARTICOLI_LOCALE)
    if mancanti or extra:
        sys.exit(f"copertura non allineata - mancanti: {mancanti}, extra: {extra}")
    totale_righe = len(RIGHE_OBBLIGHI) + len(RIGHE_PRINCIPI)
    print(f"OK: {totale_righe} righe ({len(RIGHE_OBBLIGHI)} obblighi, "
          f"{len(RIGHE_PRINCIPI)} principi), "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
