"""ETSI TS 119 101 V1.1.1 (2016-03) - Electronic Signatures and
Infrastructures (ESI); Policy and security requirements for applications
for signature creation and signature validation. Fonte ETSI 26 (conteggio
di Obblighi/Principi di questo capitolo: 34 Obblighi, 3 Principi, 37 item
di indice). Capitolo cap04: clausola 9 (Development and coding policy
requirements: 9.1 Secure development methods and application security -
controlli SDM, 9.2 Testing conformance requirements - controlli TC),
clausola 10 (Signature application practice statement), Annex A (normative,
Table of content for signature application practice statement: A.0,
A.1.1-A.1.6, A.2.1-A.2.5). Testo ufficiale in
app/.source_cache/etsi_119_101/cap04.txt (380 righe), manifest di split in
app/.source_cache/etsi_119_101/manifest.json. Questo modulo NON tocca
app/seed.py: gli id sono risolti per riferimento dalla sessione principale
tramite app/seed_data/lib.py. RELAZIONI vuota per istruzione del batch: i
collegamenti verso le altre Fonti (incluse le citazioni letterali interne,
es. clausola 10 -> annex A) li costruisce la sessione principale.

Modellazione (ADR-0007 + allineamento di granularita' di Fonte 26, deciso
dalla sessione principale): un nodo per unita' prescrittiva dotata di
identita' propria - l'id quando l'id c'e', la clausola quando non c'e'.
Nessun discrimine di rilevanza. Scelte voce per voce:

- Clausola 9 (Development and coding policy requirements) -> NESSUN nodo e
  NESSUN item di indice: intestazione di puro raggruppamento, contiene solo
  il titolo e il rimando alle sottoclavole 9.1/9.2. Stesso trattamento per
  A.1 (Introduction), A.1.2 (Business or application domain), A.1.5 (SAPS
  administration), A.2 (Signature creation/augmentation/validation
  application practice statements) e per il titolo dell'Annex A.
- Clausole 9.1 e 9.2 -> UN Obbligo per OGNI controllo dotato di id proprio
  (19 in tutto: SDM 1, SDM 1.1-SDM 1.4, SDM 2, SDM 2.1-SDM 2.3, SDM 3,
  SDM 4, TC 1, TC 2, TC 2.1-TC 2.6), con `riferimento` = SOLO l'id esatto
  ("SDM 1.3", "TC 2.6"), senza prefisso di clausola: sono i riferimenti che
  le citazioni gia' presenti nel grafo verso questa Fonte risolvono. La
  clausola di appartenenza resta tracciata in testa a `testo_integrale`
  ("9.1 Secure development methods and application security - SDM 1: ..."),
  stesso formato gia' usato per i requisiti di ETSI TS 119 461.
- SDM 1 e SDM 2 hanno un id e quindi un nodo proprio, pur essendo controlli
  di raggruppamento: SDM 1 porta la frase che introduce l'insieme di
  requisiti sulla metodologia di sviluppo, SDM 2 la sola intestazione
  "Functional and technical specifications:" che qualifica i tre controlli
  SDM 2.1-SDM 2.3. Nessuno dei due e' un'intestazione di puro raggruppamento
  ai sensi del criterio (SDM 1 ha testo prescrittivo proprio, SDM 2 e'
  citabile come id dalle citazioni del grafo).
- NOTE ed EXAMPLE restano assorbiti nel controllo a cui sono appesi, non
  hanno nodo proprio: la NOTE di TC 1 (rinvii a ETSI TS 119 104/119 124/
  119 134/119 144/119 164/119 174) e' dentro TC 1, l'EXAMPLE di SDM 1.2
  (ISO/IEC 15504 [i.3]) e' dentro SDM 1.2, i punti a)-d) di TC 2.5 sono
  dentro TC 2.5.
- La prosa non numerata delle clausole 9.1 e 9.2 (titolo di clausola,
  "Control objective" e intestazione "Controls (...)") -> UN Principio
  "altro" ciascuna, riferimento "clausola 9.1 (Secure development methods
  and application security)" / "clausola 9.2 (Testing conformance
  requirements)": e' un obiettivo di controllo, non una prescrizione con
  destinatario obbligato, e non ha id proprio.
- Clausola 10 -> UN Obbligo "informativo/trasparenza", riferimento "clausola 10 (Signature
  application practice statement)": la clausola non ha id di controllo (quindi la
  granularita' e' di clausola) ma contiene prescrizioni vincolanti per la SAPS
  istituita (indice conforme ai requisiti dell'annex A, ogni clausola presente
  tranne A.0, testo dell'annex A non copiato nella SAPS, clausola corrispondente
  ad A.2 conforme alla struttura di A.2), quindi e' modellata come Obbligo e non
  come Principio. `condizione_applicabilita` riflette la facolta' di istituire o
  meno la SAPS; destinatario: l'emittente della SAPS ("QTSP/gestore"), come per
  le clausole dell'annex A.
- Annex A.0 (The right to copy) -> UN Principio "altro": non impone un
  comportamento a un soggetto obbligato, attribuisce una facolta' (ETSI
  concede di riprodurre liberamente la proforma di SAPS e di pubblicare la
  SAPS compilata).
- Annex A.1.1-A.1.6 e A.2.1-A.2.5 -> UN Obbligo ciascuna, tipo
  "informativo/trasparenza": l'annex A e' una proforma normativa che
  prescrive il contenuto di ciascuna clausola della SAPS pubblicata ("This
  clause shall provide/include/describe/contain ...") e non ha id di
  controllo, quindi la granularita' di clausola e' quella corretta;
  destinatario l'emittente della SAPS ("QTSP/gestore"). La clausola 9.1/9.2
  di sviluppo e codifica, che A.2.5 richiama, e' censita con granularita' di
  controllo nelle righe SDM/TC.
- Annex B (informative): Bibliography e la sezione finale "History"/"Document
  history" -> NESSUN nodo e NESSUN item di indice: puro paratesto (elenco
  bibliografico di 4 voci, changelog di versione), stesso trattamento
  riservato alla clausola 2 References e, per ETSI EN 319 411-1, a
  bibliografia + History nel capitolo "escluso".

Tipi di obbligo per singolo controllo (non per clausola): "organizzativo"
per i controlli su metodologia, procedure e documentazione (SDM 1, SDM 1.1,
SDM 1.2, SDM 1.3, SDM 1.4, SDM 2.2, SDM 2.3); "tecnico/sicurezza" per i
controlli su specifiche tecniche del codice, correzioni di sicurezza e
misure di sicurezza dell'ambiente di sviluppo (SDM 2, SDM 2.1, SDM 3,
SDM 4); "procedurale" per i controlli sul conformance testing e la sua
registrazione (TC 1, TC 2, TC 2.1, TC 2.2, TC 2.3, TC 2.6);
"informativo/trasparenza" per la messa a disposizione dell'ICS e il suo
contenuto (TC 2.4, TC 2.5). `condizione_applicabilita` solo dove il testo
la contiene (TC 1).

Copertura di indice: `INDICE_ARTICOLI_LOCALE` elenca i 37 item in ordine di
testo (3 nodi di clausola/prosa di clausola + 19 id di controllo + 15
sottoclausole dell'annex A); `MAPPATURA_LOCALE` mappa ogni item su se stesso
(nessun accorpamento: ogni riga copre esattamente un item). Non sono item di
indice le 6 intestazioni di puro raggruppamento (clausola 9, titolo Annex A,
A.1, A.1.2, A.1.5, A.2) ne' il paratesto (Annex B, History).
"""

RIGHE_OBBLIGHI: list[dict] = [
    # ================= clausola 9.1: controlli SDM =========================
    {
        "riferimento": "SDM 1",
        "testo": (
            "Use of (software) development methodology: l'insieme di requisiti che segue riguarda l'uso e "
            "l'implementazione di una metodologia di sviluppo software da parte di chi sviluppa l'applicazione di "
            "firma (SCA/SVA/SAA); i requisiti operativi sono i controlli SDM 1.1-SDM 1.4."
        ),
        "testo_integrale": (
            "9.1 Secure development methods and application security - SDM 1: Use of (software) development "
            "methodology.\n\n"
            "The first set of requirements is related to the use and implementation of a software development "
            "methodology."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "SDM 1.1",
        "testo": (
            "Deve essere disponibile una descrizione della metodologia di sviluppo software usata e implementata."
        ),
        "testo_integrale": (
            "9.1 Secure development methods and application security - SDM 1.1: A description of the used and "
            "implemented software development methodology shall be available."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "SDM 1.2",
        "testo": (
            "La metodologia implementata dovrebbe seguire processi formali. Esempio ufficiale: un esempio di "
            "valutazione di processo per l'information technology si trova in ISO/IEC 15504 [i.3]."
        ),
        "testo_integrale": (
            "9.1 Secure development methods and application security - SDM 1.2: The implemented methodology "
            "should follow formal processes.\n\n"
            "EXAMPLE: An example for process assessment for Information technology can be found in ISO/IEC 15504 "
            "[i.3]."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "SDM 1.3",
        "testo": "Dovrebbero essere disponibili e documentate procedure di controllo.",
        "testo_integrale": (
            "9.1 Secure development methods and application security - SDM 1.3: Control procedures should be "
            "available and documented."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "SDM 1.4",
        "testo": (
            "L'implementazione della metodologia dovrebbe essere controllata rispetto a procedure esistenti e "
            "documentate."
        ),
        "testo_integrale": (
            "9.1 Secure development methods and application security - SDM 1.4: The implementation of the "
            "methodology should be controlled against existing and documented procedures."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "SDM 2",
        "testo": (
            "Functional and technical specifications: le specifiche funzionali e tecniche sono il termine di "
            "riferimento rispetto al quale il codice deve essere verificato (SDM 2.1) e controllato (SDM 2.3), con "
            "procedure di controllo del codice disponibili e documentate (SDM 2.2)."
        ),
        "testo_integrale": (
            "9.1 Secure development methods and application security - SDM 2: Functional and technical "
            "specifications:"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "SDM 2.1",
        "testo": "Il codice deve essere verificato secondo le proprie specifiche funzionali e tecniche.",
        "testo_integrale": (
            "9.1 Secure development methods and application security - SDM 2.1: The code shall be verified "
            "according to its functional and technical specifications."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "SDM 2.2",
        "testo": "Devono essere disponibili e documentate procedure di controllo del codice.",
        "testo_integrale": (
            "9.1 Secure development methods and application security - SDM 2.2: Code control procedures shall be "
            "available and documented."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "SDM 2.3",
        "testo": (
            "Il codice che implementa le specifiche funzionali e tecniche deve essere controllato rispetto a "
            "procedure esistenti e documentate."
        ),
        "testo_integrale": (
            "9.1 Secure development methods and application security - SDM 2.3: The code implementing the "
            "functional and technical specifications shall be controlled against existing and documented "
            "procedures."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "SDM 3",
        "testo": (
            "Nell'ambiente di sviluppo software devono essere usate correzioni di sicurezza (security fixes) "
            "aggiornate."
        ),
        "testo_integrale": (
            "9.1 Secure development methods and application security - SDM 3: Up to date security fixes in the "
            "software development environment shall be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "SDM 4",
        "testo": (
            "Le misure di sicurezza per l'ambiente di sviluppo software dovrebbero essere quelle di ISO/IEC "
            "27002 [i.6] oppure basate su un'analisi dei rischi dettagliata."
        ),
        "testo_integrale": (
            "9.1 Secure development methods and application security - SDM 4: The security measures for the "
            "software development environment should be as in ISO/IEC 27002 [i.6] or based on a detailed risk "
            "analysis."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # ================= clausola 9.2: controlli TC ==========================
    {
        "riferimento": "TC 1",
        "testo": (
            "Se viene dichiarata la conformita' a uno standard, la conformita' dell'applicazione deve essere "
            "testata come descritto nelle specifiche sul conformance testing, se tali specifiche esistono. "
            "Riferimenti ufficiali (NOTE): panoramica generale e requisiti su conformance testing e "
            "interoperabilita' in ETSI TS 119 104 [i.15]; per i singoli formati di firma, ETSI TS 119 124 [i.16] "
            "per CAdES, ETSI TS 119 134 [i.17] per XAdES, ETSI TS 119 144 [i.18] per PAdES, ETSI TS 119 164 "
            "[i.19] per ASiC; per conformance testing e interoperabilita' delle signature policy ETSI TS 119 174 "
            "[i.20]."
        ),
        "testo_integrale": (
            "9.2 Testing conformance requirements - TC 1: If conformance to a standard is stated, then the "
            "conformance of the application shall be tested as described in the specifications on conformance "
            "testing, if such specifications exist.\n\n"
            "NOTE: For general overview and requirements on conformance testing and interoperability see ETSI "
            "TS 119 104 [i.15]. For the implementation of specific signature formats see the corresponding "
            "documents for the implemented formats: ETSI TS 119 124 [i.16] for CAdES, ETSI TS 119 134 [i.17] for "
            "XAdES, ETSI TS 119 144 [i.18] for PAdES and ETSI TS 119 164 [i.19] for ASiC. For the conformance "
            "testing and interoperability of signature policies see ETSI TS 119 174 [i.20]."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "Si applica solo se il produttore/dichiarante afferma la conformita' a uno standard (\"If conformance "
            "to a standard is stated\"); il rinvio alle specifiche di conformance testing vale solo se tali "
            "specifiche esistono."
        ),
    },
    {
        "riferimento": "TC 2",
        "testo": "I test di conformita' applicati devono essere registrati e controllati.",
        "testo_integrale": (
            "9.2 Testing conformance requirements - TC 2: The applied conformance tests shall be recorded and "
            "controlled."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TC 2.1",
        "testo": (
            "Deve essere disponibile una descrizione della metodologia usata per il conformance testing."
        ),
        "testo_integrale": (
            "9.2 Testing conformance requirements - TC 2.1: A description of the used methodology for conformance "
            "testing shall be available."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TC 2.2",
        "testo": "Dovrebbero essere disponibili e documentate procedure di conformance testing.",
        "testo_integrale": (
            "9.2 Testing conformance requirements - TC 2.2: Conformance testing procedures should be available "
            "and documented."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TC 2.3",
        "testo": (
            "L'implementazione della metodologia dovrebbe essere controllata rispetto a procedure esistenti e "
            "documentate, come definito in TC 2.2."
        ),
        "testo_integrale": (
            "9.2 Testing conformance requirements - TC 2.3: The implementation of the methodology should be "
            "controlled against existing and documented procedures, as defined in TC 2.2."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TC 2.4",
        "testo": (
            "Deve essere resa disponibile una implementation conformance statement (ICS) per ogni implementazione "
            "che dichiari conformita' a un insieme di standard."
        ),
        "testo_integrale": (
            "9.2 Testing conformance requirements - TC 2.4: An implementation conformance statement (ICS) shall "
            "be made available for every implementation claiming conformance to a set of standards."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TC 2.5",
        "testo": (
            "L'ICS dovrebbe contenere le seguenti informazioni: a) informazioni amministrative che identificano "
            "il produttore e l'implementazione (es. nome del prodotto e numero di versione); b) identificazione "
            "degli standard a cui si dichiara conformita', inclusi i numeri di versione (e gli eventuali profili, "
            "se applicabili); c) indicazione di quali caratteristiche opzionali degli standard sono supportate, se "
            "ce ne sono; d) indicazione di eventuali limitazioni dipendenti dall'implementazione (intervalli, "
            "dimensioni, ecc.)."
        ),
        "testo_integrale": (
            "9.2 Testing conformance requirements - TC 2.5: The ICS should contain the following information:\n"
            "a) administrative information identifying the manufacturer and the implementation (e.g. product name "
            "and version number);\n"
            "b) identification of the standards to which conformance is claimed, including version numbers (and "
            "any profiles, if applicable);\n"
            "c) identify which optional features of the standards are supported, if any;\n"
            "d) identify any implementation dependent limitations (ranges, sizes, etc.)."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TC 2.6",
        "testo": (
            "A ogni rilascio di una nuova versione del prodotto devono essere eseguiti almeno test di "
            "regressione, che garantiscono il mantenimento della compatibilita'."
        ),
        "testo_integrale": (
            "9.2 Testing conformance requirements - TC 2.6: Whenever a new product version is released, at least "
            "regression tests shall be performed, which ensure that compatibility is maintained."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # ================= Annex A: proforma normativa della SAPS ==============
    {
        "riferimento": "Annex A.1.1 (Overview)",
        "testo": (
            "La clausola della SAPS deve fornire un'introduzione generale al documento redatto, con una sinossi "
            "del dominio business o applicativo e del processo business o applicativo specifico a cui la SAPS si "
            "applica. In funzione della complessita' e dell'ampiezza del particolare processo business o "
            "applicativo che implementa firme, puo' essere inclusa una rappresentazione diagrammatica."
        ),
        "testo_integrale": (
            "A.1.1 Overview\n"
            "This clause shall provide a general introduction to the document being written. It shall provide a "
            "synopsis of the business or application domain and the specific business or application process to "
            "which the SAPS applies. Depending on the complexity and scope of the particular business or "
            "application process implementing signatures, a diagrammatic representation may be included."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.1.2.1 (Scope and boundaries of SAPS)",
        "testo": (
            "La clausola deve descrivere lo scopo e i confini del dominio business (applicativo) in cui la SAPS "
            "e' adatta all'uso. Il dominio business (applicativo) e' qualsiasi processo di transazione business o "
            "commerciale che puo' coinvolgere piu' attori/partecipanti e/o piu' azioni e che puo' richiedere una "
            "o piu' firme per produrre effetto; puo' andare da un processo puramente interno all'organizzazione, "
            "a una rete commerciale multi-parte i cui soggetti negoziano e concordano termini e regole "
            "applicabili, fino a regole nazionali che disciplinano l'uso delle firme in processi di eGovernment "
            "ed eBusiness. La SAPS puo' essere applicabile a uno o piu' domini applicativi (es. B2B, B2C, Gov2B, "
            "Gov2C, contrattuale, finanziario, medico/sanitario, transazioni di consumo, servizi di e-notary, "
            "ecc.), mono-organizzazione, corporate o cross-organizzazione, nazionale o transfrontaliero, "
            "orizzontale o verticale (es. eProcurement, eInvoice, eHealth, eJustice, ecc.)."
        ),
        "testo_integrale": (
            "A.1.2.1 Scope and boundaries of SAPS\n"
            "This clause shall describe the scope and boundaries of the business (application) domain in which "
            "the SAPS is suitable for use.\n\n"
            "NOTE: The business (application) domain is any business or commercial transaction process(es), "
            "which can involve several actors/participants and/or multiple actions and which can require one or "
            "multiple signatures to give it effect.\n\n"
            "EXAMPLE: This can range from a purely corporate internal process or set of processes, through a "
            "multi-party trading network whose parties can negotiate and agree on the applicable terms and "
            "rules, up to nationwide rules governing the use of signatures in eGovernment and eBusiness "
            "processes.\n\n"
            "The SAPS may be applicable to one or several domains of applications (e.g. B2B, B2C, Gov2B, Gov2C, "
            "contractual, financial, medical/health, consumer transactions, e-notary services, etc.), whether "
            "mono-organization, corporate or cross-organizations, nationwide or cross-borders, horizontal or "
            "vertical (e.g. eProcurement, eInvoice, eHealth, eJustice, etc.)."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.1.2.2 (Domain of applications)",
        "testo": (
            "La clausola deve descrivere ulteriormente ciascun dominio applicativo considerato per l'uso di "
            "SCA/SVA/SAA."
        ),
        "testo_integrale": (
            "A.1.2.2 Domain of applications\n"
            "This clause shall further describe each domain of applications that is considered for the use of "
            "the SCA/SVA/SAA."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.1.2.3 (Transactional context)",
        "testo": (
            "La clausola deve fornire informazioni aggiuntive sul contesto transazionale, quando applicabile. "
            "Esempi ufficiali di contesto: richiesta di offerta, qualsiasi forma di offerta, scambio di documenti "
            "di tipi specifici, bozza di termini contrattuali e natura di tali termini (es. contratto, accordo di "
            "non divulgazione), approvazione, qualsiasi tipo di presa d'atto (es. di ricezione, di consegna, di "
            "invio), documenti che richiedono tipi specifici di autorizzazione (es. per valore, per legge "
            "applicabile o requisiti legali)."
        ),
        "testo_integrale": (
            "A.1.2.3 Transactional context\n"
            "This clause shall provide additional information about the transactional context, when "
            "applicable.\n\n"
            "EXAMPLE: Request for proposal, any form of offer, exchange of documents of certain specific types, "
            "draft of contractual terms and nature of those terms (e.g. contract, non-disclosure agreement, "
            "etc.), approval, any type of acknowledgement (e.g. of receipt, of delivery, of sending, etc.), "
            "documents requiring specific types of authorization (e.g. because of value, because of applicable "
            "law or legal requirements, etc.), etc."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "L'obbligo di fornire informazioni aggiuntive si attiva solo quando esiste un contesto transazionale "
            "da descrivere (\"when applicable\")."
        ),
    },
    {
        "riferimento": "Annex A.1.3 (SAPS distribution points)",
        "testo": (
            "La clausola deve fornire informazioni su dove la SAPS e' disponibile (es. un URL o via posta "
            "elettronica) e su come puo' essere resa disponibile una copia cartacea."
        ),
        "testo_integrale": (
            "A.1.3 SAPS distribution points\n"
            "This clause shall provide information about where the SAPS is available (e.g. a URL or by email) "
            "and how a paper/hard copy can be made available."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.1.4 (SAPS issuer)",
        "testo": (
            "La clausola deve includere il nome dell'organizzazione che emette la SAPS. Quando la SAPS e' "
            "firmata digitalmente, la clausola deve anche fornire le informazioni che identificano il certificato "
            "digitale che certifica la chiave pubblica corrispondente alla chiave privata usata dall'emittente "
            "della SAPS per firmare digitalmente la SAPS."
        ),
        "testo_integrale": (
            "A.1.4 SAPS issuer\n"
            "This clause shall include the name of the organization that is issuing the SAPS.\n\n"
            "When the SAPS is signed digitally, it shall also provide information identifying the digital "
            "certificate certifying the public key corresponding to the private key used by the SAPS issuer to "
            "digitally sign the SAPS."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "Il secondo comma (informazioni sul certificato digitale) si applica solo se la SAPS e' firmata "
            "digitalmente dall'emittente."
        ),
    },
    {
        "riferimento": "Annex A.1.5.1 (Organization administering the document)",
        "testo": (
            "La clausola deve includere il nome e l'indirizzo postale dell'organizzazione responsabile della "
            "redazione, della registrazione, del mantenimento e dell'aggiornamento della SAPS."
        ),
        "testo_integrale": (
            "A.1.5.1 Organization administering the document\n"
            "This clause shall include the name and mailing address of the organization that is responsible for "
            "the drafting, registering, maintaining, and updating of the SAPS."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.1.5.2 (Contact person)",
        "testo": (
            "Quando il punto di contatto e' una persona, la clausola deve includere: nome e cognome; indirizzo "
            "di posta elettronica; numero di telefono; e, se applicabile, numero di fax della persona. Negli "
            "altri casi deve includere: un titolo o ruolo; un alias di posta elettronica; e altre informazioni di "
            "contatto generalizzate. La clausola puo' dichiarare che il suo referente, da solo o in combinazione "
            "con altri, e' disponibile a rispondere a domande sulla SAPS."
        ),
        "testo_integrale": (
            "A.1.5.2 Contact person\n"
            "When the contact point is a person, this clause shall include the:\n"
            "• first name and last name;\n"
            "• electronic mail address;\n"
            "• telephone number; and\n"
            "• fax number, if applicable, of the person.\n\n"
            "In other cases, it shall include:\n"
            "• a title or role;\n"
            "• an electronic mail alias; and\n"
            "• other generalized contact information.\n\n"
            "This clause may state that its contact person, alone or in combination with others, is available to "
            "answer questions about the SAPS."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "Il contenuto richiesto dipende dalla natura del punto di contatto: se e' una persona fisica si "
            "applica il primo elenco (nome, cognome, e-mail, telefono, fax se applicabile), altrimenti il "
            "secondo (titolo o ruolo, alias di posta elettronica, altre informazioni generalizzate)."
        ),
    },
    {
        "riferimento": "Annex A.1.6 (Definitions and acronyms)",
        "testo": (
            "La clausola deve contenere un elenco, o un riferimento a un elenco, delle definizioni dei termini "
            "definiti usati nel documento, nonche' un elenco, o un riferimento a un elenco, degli acronimi e dei "
            "loro significati."
        ),
        "testo_integrale": (
            "A.1.6 Definitions and acronyms\n"
            "This clause shall contain a list or a reference to a list of definitions for defined terms used "
            "within the document, as well as a list or a reference to a list of acronyms and their meanings."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.2.1 (General requirements)",
        "testo": (
            "La clausola deve contenere gli altri requisiti generali, gli obiettivi di controllo e i controlli in "
            "relazione a: 1) l'interfaccia utente (come specificato nella clausola 5.1); 2) le misure di "
            "sicurezza generali (come specificato nella clausola 5.2); e 3) la completezza del sistema (come "
            "specificato nella clausola 5.3)."
        ),
        "testo_integrale": (
            "A.2.1 General requirements\n"
            "This clause shall contain other general requirements, control objectives and controls in connection "
            "with:\n"
            "1) the user interface (as specified in clause 5.1);\n"
            "2) general security measures (as specified in clause 5.2; and\n"
            "3) system completeness (as specified in clause 5.3)."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.2.2 (Legal driven policy requirements)",
        "testo": (
            "La clausola deve contenere requisiti, obiettivi di controllo e controlli in relazione a: 1) il "
            "trattamento dei dati personali (come specificato nella clausola 6.2); e 2) l'accessibilita' alle "
            "persone con disabilita' (come specificato nella clausola 6.3)."
        ),
        "testo_integrale": (
            "A.2.2 Legal driven policy requirements\n"
            "This clause shall contain requirements, control objectives and controls in connection with:\n"
            "1) the processing of personal data (as specified in clause 6.2); and\n"
            "2) the accessibility to persons with disabilities (as specified in clause 6.3)."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.2.3 (Information security (management system) requirements)",
        "testo": (
            "La clausola deve contenere requisiti, obiettivi di controllo e controlli in relazione alla sicurezza "
            "delle informazioni e ai sistemi di gestione della sicurezza delle informazioni, e in particolare: "
            "1) protezione della rete (come specificato nella clausola 7.2); 2) protezione del sistema "
            "informativo (clausola 7.3); 3) integrita' del software dell'applicazione (clausola 7.4); 4) "
            "sicurezza della memorizzazione dei dati (clausola 7.5); e 5) log degli eventi (clausola 7.6)."
        ),
        "testo_integrale": (
            "A.2.3 Information security (management system) requirements\n"
            "This clause shall contain requirements, control objectives and controls in connection with "
            "information security and information security management systems, and in particular:\n"
            "1) network protection (as specified in clause 7.2);\n"
            "2) information system protection (as specified in clause 7.3);\n"
            "3) software integrity of the application (as specified in clause 7.4);\n"
            "4) data storage security (as specified in clause 7.5); and\n"
            "5) event logs (as specified in clause 7.6)."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.2.4 (Signature creation, signature validation and signature augmentation processes requirements)",
        "testo": (
            "La clausola deve contenere requisiti, obiettivi di controllo e controlli in relazione a: 1) il "
            "processo e i sistemi di creazione della firma, e in particolare: a) funzionalita' principali "
            "(clausola 8.1.2); b) gestione del tipo di contenuto dei dati (8.1.3); c) attributi di firma "
            "(8.1.4); d) applicazione di tempistiche e sequenze (8.1.5); e) invocazione della firma (8.1.6); f) "
            "scelta dell'algoritmo crittografico (8.1.7); g) procedura di autenticazione del firmatario e "
            "gestione del controllo di accesso (8.1.8); h) preparazione dei DTBS (8.1.9); i) rappresentazione dei "
            "dati da firmare (DTBSR) (8.1.10); j) gestione del dispositivo di creazione della firma (8.1.11); k) "
            "protezione della comunicazione tra SCDev e SCA (8.1.12); e l) operazione di firma in blocco "
            "(bulk signing) (8.1.13); 2) il processo e i sistemi di convalida della firma, e in particolare: a) "
            "funzionalita' principali di convalida (8.2.2); b) applicazione delle regole del processo di "
            "convalida (8.2.3); c) validation policy (8.2.4); d) interfaccia utente di convalida (8.2.5); e e) "
            "conformita' relativa di input/output di convalida (correttezza della procedura di convalida "
            "implementata) (8.2.6); 3) il processo e i sistemi di augmentation della firma, e in particolare: a) "
            "funzionalita' principali di augmentation (8.3.3); b) applicazione delle regole del processo di "
            "augmentation (8.3.4); c) inclusione dei dati durante l'augmentation (8.3.5); e d) convalida della "
            "firma in input (8.3.6)."
        ),
        "testo_integrale": (
            "A.2.4 Signature creation, signature validation and signature augmentation processes "
            "requirements\n"
            "This clause shall contain requirements, control objectives and controls in connection with:\n"
            "1) Signature creation process and systems, and in particular:\n"
            "a) main functionalities (as specified in clause 8.1.2);\n"
            "b) data content type management (as specified in clause 8.1.3);\n"
            "c) signature attributes (as specified in clause 8.1.4);\n"
            "d) timing and sequencing enforcement (as specified in clause 8.1.5);\n"
            "e) signature invocation (as specified in clause 8.1.6);\n"
            "f) cryptographic algorithm choice (as specified in clause 8.1.7);\n"
            "g) signer's authentication procedure (and access control management) (as specified in clause "
            "8.1.8);\n"
            "h) DTBS preparation (as specified in clause 8.1.9);\n"
            "i) data to be signed representation (DTBSR) (as specified in clause 8.1.10);\n"
            "j) signature creation device management (as specified in clause 8.1.11);\n"
            "k) protection of the communication between SCDev and SCA (as specified in clause 8.1.12); and\n"
            "l) bulk signing operation (as specified in clause 8.1.13).\n\n"
            "2) Signature validation process and systems, and in particular:\n"
            "a) main validation functionalities (as specified in clause 8.2.2);\n"
            "b) validation process rules enforcement (as specified in clause 8.2.3);\n"
            "c) validation policy (as specified in clause 8.2.4);\n"
            "d) validation user interface (as specified in clause 8.2.5); and\n"
            "e) validation input/output relative conformance (correctness of the implemented validation "
            "procedure) (as specified in clause 8.2.6).\n\n"
            "3) Signature augmentation process and systems, and in particular:\n"
            "a) main augmentation functionalities (as specified in clause 8.3.3);\n"
            "b) augmentation process rules enforcement (as specified in clause 8.3.4);\n"
            "c) data inclusion during the augmentation (as specified in clause 8.3.5); and\n"
            "d) validation of the input signature (as specified in clause 8.3.6)."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A.2.5 (Development and coding policy requirements)",
        "testo": (
            "La clausola deve contenere requisiti, obiettivi di controllo e controlli in relazione alle policy "
            "di sviluppo e di codifica, in particolare con: 1) i metodi di sviluppo sicuro (come specificato "
            "nella clausola 9.1); e 2) il testing di conformita' (come specificato nella clausola 9.2)."
        ),
        "testo_integrale": (
            "A.2.5 Development and coding policy requirements\n"
            "This clause shall contain requirements, control objectives and controls in connection with the "
            "development and coding policies, in particular with:\n"
            "1) the secure development methods (as specified in clause 9.1); and\n"
            "2) testing conformance (as specified in clause 9.2)."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- clausola 10 ------------------------------------------------------
    {
        "riferimento": "clausola 10 (Signature application practice statement)",
        "testo": (
            "La signature application practice statement (SAPS) e' facoltativa: puo' essere istituita e puo' "
            "essere usata da sola per dichiarare le regole da applicare per conformarsi ai requisiti di sicurezza "
            "e di policy, oppure come parte di una signature policy come descritto in ETSI TS 119 172 [i.14]. "
            "Quando il documento e' istituito: il suo indice (table of content, ToC) deve essere conforme ai "
            "requisiti dell'annex A; la numerazione delle clausole dell'indice deve comparire nella SAPS "
            "rimuovendo il prefisso \"A.\"; ogni clausola deve comparire, tranne la clausola A.0; se la clausola "
            "non si applica, dopo il titolo deve essere scritto \"not applicable\"; il testo fornito in ciascuna "
            "clausola dell'annex A specifica il contenuto atteso di quella clausola e non deve essere copiato "
            "nella SAPS. La clausola della SAPS corrispondente alla clausola A.2 deve descrivere un insieme di "
            "regole sulle prassi usate dall'applicazione e dal suo ambiente per implementare correttamente la "
            "generazione, l'augmentation e/o la convalida delle firme; deve includere, per riferimento o "
            "esplicitamente, l'insieme dei requisiti di policy e di prassi di sicurezza che SCA, SAA e/o SVA "
            "dovranno soddisfare nel generare, aumentare e/o convalidare firme in conformita' alla SAPS e alla "
            "signature policy applicabile; quando si sceglie un insieme esplicito di requisiti di policy e "
            "prassi di sicurezza, la clausola deve conformarsi alla struttura definita nella clausola A.2. Una "
            "SAPS che dichiari tali prassi puo' essere paragonata a una signature policy come una certification "
            "practice statement puo' essere paragonata a una certificate policy."
        ),
        "testo_integrale": (
            "10 Signature application practice statement\n"
            "A signature application practice statement (SAPS) may be established. An SAPS may be used on its "
            "own to state the rules to be applied to conform to the security and policy requirements or as part "
            "of a signature policy as described in ETSI TS 119 172 [i.14].\n\n"
            "When such a document is established, its table of content (ToC) shall comply with the requirements "
            "stated in annex A.\n\n"
            "The numbering of the clauses of the table of content is provided as it shall appear in the SAPS by "
            "removing the starting \"A.\". Each clause shall appear except clause A.0. If the clause does not "
            "apply, \"not applicable\" shall be written after the clause title. The text provided in each clause "
            "of annex A specifies the expected content of each clause. This text shall not be copied in the "
            "SAPS.\n\n"
            "The clause in the SAPS corresponding to clause A.2 shall describe a set of rules with regards to "
            "the practices used by the application and its environment to properly implement the generation, "
            "augmentation and/or validation of signatures. This clause shall include, either by reference or "
            "explicitly, the set of policy and security practices requirements that the SCA, SAA and/or the SVA "
            "will have to meet when generating, augmenting and/or validating signatures in compliance with the "
            "SAPS and the applicable signature policy. When an explicit set of policy and security practices "
            "requirements is chosen, the clause shall conform to the structure defined in clause A.2.\n\n"
            "EXAMPLE 1: A community of users defines as part of a signature policy the applicable requirements "
            "with regards to those practices any application will have to meet in order to comply with the "
            "community signature policy.\n\n"
            "EXAMPLE 2: A signature policy refers to an external set of practice statements that describes the "
            "practices used by an application that generates, validates or augments signatures according to "
            "several signature policies defined by several communities of users.\n\n"
            "EXAMPLE 3: A signature policy is defined in the context of a specific legal context and defines a "
            "set of rules to create, validate or augment a signature meeting specific legal requirements (e.g. "
            "a qualified electronic signature as defined in the applicable European legislation framework) "
            "including specific requirements on signature creation applications (SCAs), signature validation "
            "applications (SVAs), and signature augmentation applications (SAAs) and their environments.\n\n"
            "NOTE: A SAPS stating such signature application practice defining requirements or making statements "
            "on the way signature applications are meeting application level policy and security requirements "
            "when creating or validating signatures, whatever and independently of the type of signature and of "
            "the set of requirements ruling the creation or validation of a type of signature (i.e. the applied "
            "signature policy), can be compared to a signature policy like a certification practice statement "
            "can be compared to a certificate policy."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "La SAPS e' facoltativa: gli obblighi sul suo contenuto si applicano solo se il documento viene "
            "istituito."
        ),
    },
]

RIGHE_PRINCIPI: list[dict] = [
    # --- prosa non numerata delle clausole 9.1 e 9.2 ----------------------
    {
        "riferimento": "clausola 9.1 (Secure development methods and application security)",
        "testo": (
            "Obiettivo di controllo della clausola 9.1: garantire l'uso di una metodologia (software) di sviluppo "
            "e di strumenti appropriati e l'attuazione di misure di sicurezza adeguate. La clausola raccoglie i "
            "controlli sui metodi di sviluppo sicuro (Security Development Methods), identificati come SDM 1 e "
            "SDM 1.1-SDM 1.4 (metodologia di sviluppo software), SDM 2 e SDM 2.1-SDM 2.3 (specifiche funzionali e "
            "tecniche del codice), SDM 3 (security fixes aggiornate nell'ambiente di sviluppo) e SDM 4 (misure di "
            "sicurezza dell'ambiente di sviluppo)."
        ),
        "testo_integrale": (
            "9.1 Secure development methods and application security\n"
            "Control objective\n\n"
            "Ensure the usage of appropriate (software) development methodology, tools and the implementation of "
            "adequate security measures.\n\n"
            "Controls (Security Development Methods)"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 9.2 (Testing conformance requirements)",
        "testo": (
            "Obiettivo di controllo della clausola 9.2: garantire che le implementazioni siano conformi agli "
            "standard che implementano. La clausola raccoglie i controlli sul conformance testing (Testing "
            "Conformance requirements), identificati come TC 1 (test di conformita' secondo le specifiche di "
            "conformance testing, se esistenti), TC 2 e TC 2.1-TC 2.6 (registrazione e controllo dei test, "
            "metodologia e procedure, implementation conformance statement, regression test)."
        ),
        "testo_integrale": (
            "9.2 Testing conformance requirements\n"
            "Control objective\n\n"
            "Ensure implementations are compliant with the standards they implement.\n\n"
            "Controls (Testing Conformance requirements)"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    # --- Annex A.0 --------------------------------------------------------
    {
        "riferimento": "Annex A.0 (The right to copy)",
        "testo": (
            "Fatte salve le disposizioni della clausola sul diritto d'autore relativa al testo del presente "
            "documento, ETSI concede che gli utenti del presente documento possano riprodurre liberamente la "
            "proforma di SAPS contenuta nel presente annesso, affinche' possa essere usata per gli scopi "
            "previsti, e possano ulteriormente pubblicare la SAPS compilata. E' una facolta' di riproduzione/"
            "pubblicazione, non un obbligo a carico di un soggetto."
        ),
        "testo_integrale": (
            "A.0 The right to copy\n"
            "Notwithstanding the provisions of the copyright clause related to the text of the present document, "
            "ETSI grants that users of the present document may freely reproduce the SAPS proforma in this annex "
            "so that it can be used for its intended purposes and may further publish the completed SAPS."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 9.1 (Secure development methods and application security)",
    "SDM 1",
    "SDM 1.1",
    "SDM 1.2",
    "SDM 1.3",
    "SDM 1.4",
    "SDM 2",
    "SDM 2.1",
    "SDM 2.2",
    "SDM 2.3",
    "SDM 3",
    "SDM 4",
    "clausola 9.2 (Testing conformance requirements)",
    "TC 1",
    "TC 2",
    "TC 2.1",
    "TC 2.2",
    "TC 2.3",
    "TC 2.4",
    "TC 2.5",
    "TC 2.6",
    "clausola 10 (Signature application practice statement)",
    "Annex A.0 (The right to copy)",
    "Annex A.1.1 (Overview)",
    "Annex A.1.2.1 (Scope and boundaries of SAPS)",
    "Annex A.1.2.2 (Domain of applications)",
    "Annex A.1.2.3 (Transactional context)",
    "Annex A.1.3 (SAPS distribution points)",
    "Annex A.1.4 (SAPS issuer)",
    "Annex A.1.5.1 (Organization administering the document)",
    "Annex A.1.5.2 (Contact person)",
    "Annex A.1.6 (Definitions and acronyms)",
    "Annex A.2.1 (General requirements)",
    "Annex A.2.2 (Legal driven policy requirements)",
    "Annex A.2.3 (Information security (management system) requirements)",
    "Annex A.2.4 (Signature creation, signature validation and signature augmentation processes requirements)",
    "Annex A.2.5 (Development and coding policy requirements)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Nessuna relazione in questo capitolo: per istruzione del batch i
# collegamenti (comprese le citazioni letterali interne, es. TC 2.3 -> TC 2.2,
# clausola 10 -> annex A) li costruisce la sessione principale.
RELAZIONI: list[dict] = []
