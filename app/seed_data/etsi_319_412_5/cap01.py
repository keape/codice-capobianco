"""ETSI EN 319 412-5 V2.5.1 (2025-06) - Electronic Signatures and Trust
Infrastructures (ESI); Certificate Profiles; Part 5: QCStatements. Fonte 7,
un unico capitolo (documento tecnico di 21 pagine, sta comodamente nel
contesto di una sessione principale — nessuna suddivisione per subagent
necessaria). Testo ufficiale in app/.source_cache/etsi-319-412-5/raw.txt
(fetch diretto dal repository ETSI deliver, 2026-09-21).

Modellazione (ADR-0007), adattata a una fonte che non e' un atto legislativo
ma uno standard tecnico ETSI strutturato in clausole/sottoclausole invece che
articoli/commi:

- Ogni "item di indice" di questo capitolo e' una clausola o un requisito
  numerato del testo (es. "QCS-4.1-01", "clausola 4.2.2", "Annex B"), stesso
  principio "un nodo per disposizione" di ADR-0007 applicato all'unita'
  strutturale propria di questo genere di fonte.
- Front matter puramente amministrativo/bibliografico (Contents, Intellectual
  Property Rights, Foreword, Modal verbs terminology, Introduction, clausola
  2 References, Annex C Change history, History) NON e' modellato come nodo:
  stesso trattamento riservato al preambolo/"considerando" delle fonti
  legislative gia' censite (mai un nodo Obbligo/Principio in questo
  censimento), qui esteso per analogia ai paratesti equivalenti di uno
  standard tecnico (indice, bibliografia, cronologia versioni). Nessun
  discrimine di rilevanza sulle clausole sostanziali: ogni clausola/requisito
  con contenuto normativo/tecnico proprio (incluse quelle "void", riportate
  nel testo ma prive di contenuto autonomo, es. 3.2/4.3.5.2) e' comunque
  coperta se genera un item di indice distinto - "void" non genera un nodo
  autonomo perche' non ha contenuto oltre il rimando strutturale.
- Requisiti "shall"/"shall not" con soggetto obbligato implicito (il QTSP
  che emette il certificato qualificato) -> Obbligo, categoria_soggetto
  "QTSP/gestore", ruolo "obbligato", tipo_obbligo "tecnico/sicurezza" (sono
  tutti requisiti di profilo tecnico del certificato, non organizzativi/
  informativi/di conservazione in senso proprio).
- Clausole puramente descrittive/dichiarative (definiscono il significato di
  un QCStatement senza imporre un comportamento, o clausole facoltative con
  "may") -> Principio. tipo_principio "definitorio" per le clausole che
  definiscono il significato tecnico di uno statement; "altro" per le
  clausole che descrivono una facolta' (QCS-4.3.5-01, "may include");
  "scopo/ambito di applicazione" per Scope/Introduction/4.3.1.
- Annex A (informative, mapping con Allegati I/III/IV Reg. 910/2014) ->
  3 Principio "altro" (mapping informativo cross-standard, non definitorio in
  senso stretto). Usati come base testuale per le relazioni cross-fonte verso
  eIDAS/eIDAS2 in fase 6 (modulo cap02_relazioni_cross.py).
- Annex B (normative, modulo ASN.1) -> 1 Principio "definitorio" (il modulo
  ASN.1 completo e' il riferimento tecnico autoritativo gia' richiamato da
  QCS-4.1-04, che ne impone l'uso come "shall be as provided in Annex B").
- QCS-4.3.5-02 e' condizionale ("if this qcStatement is included") ->
  Obbligo con condizione_applicabilita esplicita, non un Principio, perche'
  impone comunque un comportamento vincolante quando la condizione si
  avvera (stessa convenzione gia' usata nel censimento per obblighi
  condizionati, es. art. 24 §2(k) CAD/eIDAS "se rilascia certificati
  qualificati...").
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "QCS-4.1-01",
        "testo": "L'estensione qcStatements del certificato qualificato deve essere conforme a quanto specificato nella clausola 3.2.6 di IETF RFC 3739.",
        "testo_integrale": "QCS-4.1-01: The qcStatements extension shall be as specified in clause 3.2.6 of IETF RFC 3739 [2].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QCS-4.1-02",
        "testo": "L'estensione qcStatements del certificato qualificato non deve essere marcata come critica.",
        "testo_integrale": "QCS-4.1-02: The qcStatements extension shall not be marked as critical.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QCS-4.1-03",
        "testo": "La sintassi degli statement definiti nel presente standard deve rispettare l'ASN.1 (Raccomandazioni ITU-T X.680-X.683).",
        "testo_integrale": "QCS-4.1-03: The syntax of the defined statements shall comply with ASN.1 (Recommendations ITU-T X.680 to X.683 [3]).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QCS-4.1-04",
        "testo": "Il modulo ASN.1 completo per tutti gli statement definiti deve essere quello riportato nell'Annex B, che prevale sulle definizioni ASN.1 fornite nel corpo del documento in caso di discrepanza.",
        "testo_integrale": "QCS-4.1-04: The complete ASN.1 module for all defined statements shall be as provided in Annex B. Annex B takes precedence over the ASN.1 definitions provided in the body of the present document, in case of discrepancy.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QCS-4.2.1-01",
        "testo": "Un certificato che include lo statement esi4-qcStatement-1 per dichiarare che e' un certificato qualificato UE: non deve includere lo statement QcCClegislation; e deve rispettare tutti i requisiti della clausola 5.",
        "testo_integrale": "QCS-4.2.1-01: A certificate that includes the esi4-qcStatement-1 statement with the aim to declare that it is an EU qualified certificate that is issued according to Directive 1999/93/EC [i.3] or the Annex I, III or IV of Regulation (EU) No 910/2014 [i.8] whichever is in force at the time of issuance: a) shall not include the QcCClegislation statement; and b) shall comply with all requirements defined in clause 5.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il certificato include lo statement esi4-qcStatement-1 per dichiarare la qualifica di certificato qualificato UE",
    },
    {
        "riferimento": "QCS-4.2.4-01",
        "testo": "Se il certificato e' emesso secondo la Direttiva 1999/93/CE o il Regolamento (UE) 910/2014, lo statement QcCClegislation (paese/i sotto la cui legislazione il certificato e' qualificato) non deve essere presente.",
        "testo_integrale": "QCS-4.2.4-01: If the certificate is issued according to Directive 1999/93/EC [i.3] or Regulation (EU) No 910/2014 [i.8], this QCStatement shall not be present.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo ai certificati emessi secondo la Direttiva 1999/93/CE o il Regolamento (UE) 910/2014",
    },
    {
        "riferimento": "QCS-4.2.5-01",
        "testo": "Il valore di CountryName nello statement QcQSCDlegislation non deve identificare un paese UE, un paese SEE, un gruppo di paesi UE/SEE, o il valore \"EU\".",
        "testo_integrale": "QCS-4.2.5-01: CountryName shall not have as value any code identifying: a country of the European Union (EU); or a country of the European Economic Area (EEA); or a group of EU or EEA countries; or the value of \"EU\".",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QCS-4.3.2-01",
        "testo": "I codici valuta nello statement sui limiti di valore delle transazioni devono essere quelli definiti dalla norma ISO 4217.",
        "testo_integrale": "QCS-4.3.2-01: The currency codes shall be as defined in ISO 4217 [i.14].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il certificato include lo statement esi4-qcStatement-2 (limiti di valore delle transazioni)",
    },
    {
        "riferimento": "QCS-4.3.2-02",
        "testo": "Dovrebbe essere utilizzata la forma alfabetica dei codici valuta nello statement sui limiti di valore delle transazioni.",
        "testo_integrale": "QCS-4.3.2-02: The alphabetic form of currency codes should be used.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il certificato include lo statement esi4-qcStatement-2 (limiti di valore delle transazioni)",
    },
    {
        "riferimento": "QCS-4.3.4-01",
        "testo": "La lingua indicata nello statement sulla localizzazione dei PKI Disclosure Statement (PDS) deve essere definita secondo ISO 639-1.",
        "testo_integrale": "QCS-4.3.4-01: The language shall be as defined in ISO 639-1 [1].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il certificato include lo statement esi4-qcStatement-5 (localizzazione dei PDS)",
    },
    {
        "riferimento": "QCS-4.3.4-02",
        "testo": "I PKI Disclosure Statement (PDS) referenziati dovrebbero essere strutturati secondo l'Annex A di ETSI EN 319 411-1.",
        "testo_integrale": "QCS-4.3.4-02: Referenced PKI Disclosure Statements should be structured according to Annex A of ETSI EN 319 411-1 [i.10]. The signature of the certificate does not cover the content of the PDS and hence does not protect the integrity of the PDS which can change over time. End users trust in the accuracy of a PDS is therefore based on the mechanisms used to protect the authenticity of the PDS.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il certificato include lo statement esi4-qcStatement-5 (localizzazione dei PDS)",
    },
    {
        "riferimento": "QCS-4.3.4-03",
        "testo": "L'URL a un PDS fornito nello statement deve usare almeno lo schema \"https\" (RFC 2818 o documenti successivi che lo aggiornano).",
        "testo_integrale": "QCS-4.3.4-03: As a minimum, a URL to a PDS provided in this statement shall use the \"https\" (https://) scheme, IETF RFC 2818 [5] or later documents updating this specification.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il certificato include lo statement esi4-qcStatement-5 (localizzazione dei PDS)",
    },
    {
        "riferimento": "QCS-4.3.5-02",
        "testo": "Se lo statement sul metodo di identificazione eIDAS/eIDAS2 art. 24 e' incluso nel certificato, deve contenere il valore OID corrispondente al metodo di identificazione usato per la verifica dell'identita' del certificato.",
        "testo_integrale": "QCS-4.3.5-02: [CONDITIONAL] If this qcStatement is included in the certificate, it shall contain the OID value corresponding to the identification used for identity verification of the certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se il QTSP ha scelto di includere lo statement esi4-qcStatement-8 (metodo di identificazione eIDAS/eIDAS2 art. 24) nel certificato qualificato",
    },
    {
        "riferimento": "QCS-5-01",
        "testo": "I certificati qualificati UE devono includere gli statement QCStatements secondo la tabella 2: esi4-qcStatement-1 (clausola 4.2.1) obbligatorio; esi4-qcStatement-7 (clausola 4.2.4) vietato; esi4-qcStatement-4 (clausola 4.2.2) opzionale, ma obbligatorio se la chiave privata risiede in un QSCD/SSCD; esi4-qcStatement-6 (clausola 4.2.3) opzionale, ma obbligatorio se il certificato e' emesso secondo l'Allegato III o IV del Regolamento 910/2014; esi4-qcStatement-2 (clausola 4.3.2), esi4-qcStatement-3 (clausola 4.3.3), esi4-qcStatement-8 (clausola 4.3.5) e esi4-qcStatement-9 (clausola 4.2.5) opzionali; esi4-qcStatement-5 (clausola 4.3.4) opzionale, con l'obbligo aggiuntivo di fornire almeno un URL a un PDS in inglese e di non referenziare piu' di un PDS per lingua.",
        "testo_integrale": "QCS-5-01: EU qualified certificates shall include QCStatements in accordance with table 2. The column \"Presence\" contains the specification of the presence of the statement as follows: M: Mandatory. The statement shall be present. O: Optional. The statement may be present. X: Forbidden. The statement shall not be present. Table 2: Requirements on QCStatements. Clause 4.2.1 (esi4-qcStatement-1): M. Clause 4.2.4 (esi4-qcStatement-7): X. Clause 4.2.2 (esi4-qcStatement-4): O - When the certificate is issued as a certificate where the private key related to the certified public key resides in a qualified signature/seal creation device in accordance with Regulation (EU) No 910/2014 [i.8] or in a secure signature creation device as defined in Directive 1999/93/EC [i.3], this statement shall be present. Clause 4.2.3 (esi4-qcStatement-6): O - When the certificate is issued in accordance with Annex III or Annex IV of Regulation (EU) No 910/2014 [i.8], this statement shall be present. Clause 4.3.2 (esi4-qcStatement-2): O. Clause 4.3.3 (esi4-qcStatement-3): O. Clause 4.3.4 (esi4-qcStatement-5): O - a) It shall provide at least one URL to a PDS in English. Other PDS documents in other languages may be referenced using this QCStatement provided that they provide information that corresponds to the information given in the referenced English PDS; and b) It shall not reference more than one PDS per language. Clause 4.3.5 (esi4-qcStatement-8): O. Clause 4.2.5 (esi4-qcStatement-9): O.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica ai certificati qualificati UE (che includono esi4-qcStatement-1 per dichiarare tale qualifica)",
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 1 (Scope)",
        "testo": "Il documento definisce i QCStatement specifici per l'estensione qcStatements (RFC 3739), inclusi i requisiti per il loro uso nei certificati qualificati UE; alcuni QCStatement possono essere usati anche per altre forme di certificato e con qualunque profilo di certificato (ETSI EN 319 412-2/3/4 o altrove). I QCStatement della clausola 4.3 sono applicabili anche fuori dall'UE; gli altri requisiti della clausola 4 sono specifici del Regolamento (UE) 910/2014 ma possono essere adattati ad altri contesti regolatori.",
        "testo_integrale": "1 Scope: The present document defines specific QCStatement for the qcStatements extension as defined in IETF RFC 3739 [2], clause 3.2.6, including requirements for their use in EU qualified certificates. Some of these QCStatements can be used for other forms of certificate. The QCStatements defined in the present document can be used in combination with any certificate profile, either defined in ETSI EN 319 412-2 [i.2], ETSI EN 319 412-3 [i.5] and ETSI EN 319 412-4 [i.6], or defined elsewhere. The QCStatements defined in clause 4.3 can be applied to regulatory environments outside the EU. Other requirements specified in clause 4 are specific to Regulation (EU) No 910/2014 [i.8] but may be adapted for other regulatory environments.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3 (definizioni, simboli, abbreviazioni, notazioni)",
        "testo": "Definisce i termini \"EU qualified certificate\" (certificato qualificato conforme all'Allegato I/III/IV Reg. 910/2014 o Allegato I Direttiva 1999/93/CE), \"QCStatement\" (statement incluso nell'estensione qcStatements ex RFC 3739), \"dispositivo qualificato di creazione di firma/sigillo elettronico\" (come da Reg. 910/2014) e \"secure signature creation device\" (come da Direttiva 1999/93/CE); elenca le abbreviazioni usate nel documento (ASN.1, CA, CRL, EEA, PDS, PKI, QC, QSCD, ecc.) e rinvia a ETSI EN 319 412-1 per le notazioni.",
        "testo_integrale": "3.1 Terms: EU qualified certificate: qualified certificate that is stated to be in accordance with Annex I, III or IV of Regulation (EU) No 910/2014 [i.8] or Annex I of Directive 1999/93/EC [i.3] whichever is in force at the time of issuance. QCStatement: statement for inclusion in a qcStatements certificates extension as specified in IETF RFC 3739 [2]. qualified electronic signature/seal creation device: As specified in Regulation (EU) No 910/2014 [i.8]. secure signature creation device: As specified in Directive 1999/93/EC [i.3]. 3.2 Symbols: Void. 3.3 Abbreviations: ASN.1, CA, CRL, EC, EEA, EU, IETF, ISO, PDS, PKI, QC, QSCD, RFC, URL (vedi testo per esteso). 3.4 Notations: For the purposes of the present document, the notations given in ETSI EN 319 412-1 [i.1] apply.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.2.1 (significato)",
        "testo": "Lo statement esi4-qcStatement-1 dichiara che il certificato e' un certificato qualificato UE emesso secondo la Direttiva 1999/93/CE o l'Allegato I/III/IV del Regolamento (UE) 910/2014, oppure che e' un certificato qualificato secondo un quadro giuridico definito di un paese o gruppo di paesi identificato; il significato preciso e' precisato dallo statement sul tipo di certificato (clausola 4.2.3, tabella 1) e dallo statement QcCClegislation (clausola 4.2.4, tabella 1A).",
        "testo_integrale": "This Qcstatement claims: i) either that the certificate is an EU qualified certificate that is issued according to Directive 1999/93/EC [i.3] or the Annex I, III or IV of Regulation (EU) No 910/2014 [i.8] whichever is in force at the time of issuance; or ii) that the certificate is a certificate that is issued as qualified within a defined legal framework from an identified country or set of countries. Syntax: esi4-qcStatement-1 QC-STATEMENT ::= { IDENTIFIED BY id-etsi-qcs-QcCompliance } id-etsi-qcs-QcCompliance OBJECT IDENTIFIER ::= { id-etsi-qcs 1 }. The precise meaning of this statement is enhanced by: a) the QC type statement defined in clause 4.2.3 according to table 1; and b) the QcCClegislation statement defined in clause 4.2.4 according to table 1A. Table 1: esi4-qcStatement-1 meaning (QC type statement absent/present -> meaning of esi4-qcStatement-1, in combinazione con Annex I/III/IV Reg. 910/2014). Table 1A: esi4-qcStatement-1 meaning (QcCClegislation statement absent/present -> regime giuridico applicabile).",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["certificato qualificato di firma elettronica", "certificato qualificato di sigillo elettronico", "certificato qualificato di autenticazione di siti web"],
    },
    {
        "riferimento": "clausola 4.2.2",
        "testo": "Lo statement esi4-qcStatement-4 dichiara che la chiave privata collegata alla chiave pubblica certificata risiede in un dispositivo qualificato di creazione di firma/sigillo (QSCD) secondo il Regolamento (UE) 910/2014, o in un secure signature creation device secondo la Direttiva 1999/93/CE.",
        "testo_integrale": "This Qcstatement declares that the private key related to the certified public key resides in a Qualified Signature/Seal Creation Device (QSCD) according to Regulation (EU) No 910/2014 [i.8] or a secure signature creation device as defined in Directive 1999/93/EC [i.3].",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["dispositivo qualificato di creazione di firma elettronica", "dispositivo qualificato di creazione di sigillo elettronico"],
    },
    {
        "riferimento": "clausola 4.2.3",
        "testo": "Lo statement esi4-qcStatement-6 dichiara che il certificato e' emesso per una sola delle finalita' di firma elettronica, sigillo elettronico o autenticazione di siti web; se combinato con lo statement 4.2.1 identifica un tipo di certificato qualificato secondo il Regolamento 910/2014, altrimenti puo' indicare la finalita' di un certificato non qualificato secondo il quadro giuridico indicato dallo statement 4.2.4.",
        "testo_integrale": "This QCStatement declares that a certificate is issued as one and only one of the purposes of electronic signature, electronic seal or web site authentication. When used in combination with the qcStatement as defined in clause 4.2.1, this QCStatement states that a qualified certificate, within a specific legislative context, such as Regulation (EU) No 910/2014 [i.8], is issued as one and only one of the purposes of electronic signature, electronic seal or web site authentication. When not used in combination with the qcStatement as defined in clause 4.2.1, it indicates that a certificate is issued as one and only one of the purposes of electronic signatures, seals or web site authentication for \"non-qualified certificates\" within a legislative context, which may be indicated by the qcStatement defined in clause 4.2.4.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["certificato qualificato di firma elettronica", "certificato qualificato di sigillo elettronico", "certificato qualificato di autenticazione di siti web"],
    },
    {
        "riferimento": "clausola 4.2.4 (significato)",
        "testo": "Lo statement esi4-qcStatement-7 (QcCClegislation) identifica il paese o l'insieme di paesi sotto la cui legislazione il certificato e' emesso come certificato qualificato.",
        "testo_integrale": "This QCStatement identifies the country or set of countries under the legislation of which the certificate is issued as a qualified certificate.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.2.5 (significato)",
        "testo": "Lo statement esi4-qcStatement-9 (QcQSCDlegislation) dichiara che la chiave privata collegata alla chiave pubblica certificata risiede in un dispositivo di creazione di firma riconosciuto come qualificato in un quadro giuridico definito di un paese o insieme di paesi identificato, esterno all'Unione Europea e allo Spazio Economico Europeo.",
        "testo_integrale": "This QCStatement declares that the private key related to the certified public key resides in a signature creation device recognized as qualified within a defined legal framework from an identified country, or set of countries, outside the European Union and outside the European Economic Area.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["dispositivo qualificato di creazione di firma elettronica", "dispositivo qualificato di creazione di sigillo elettronico"],
    },
    {
        "riferimento": "clausola 4.3.1 (Introduction)",
        "testo": "I QCStatement definiti nelle clausole 4.3 e seguenti possono essere usati con qualunque quadro regolatorio applicabile, non solo quello UE.",
        "testo_integrale": "4.3.1 Introduction: QCStatements defined in the following clauses can be used with any applicable regulatory framework.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.2 (significato)",
        "testo": "Lo statement esi4-qcStatement-2 dichiara una limitazione sul valore delle transazioni per cui il certificato puo' essere usato.",
        "testo_integrale": "This QCStatement declares a limitation on the value of transaction for which a certificate can be used. NOTE 1: This QCStatement was aimed at supporting Directive 1999/93/EC [i.3] which declared that qualified certificates could declare \"limits on the value of transactions for which the certificate can be used, if applicable\". The definition of EU qualified certificates according to Regulation (EU) No 910/2014 [i.8] does not include any requirements on such declaration. NOTE 2: It is outside the scope of this QCStatement to define how CA liability is affected by inclusion of this QCStatement.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.3",
        "testo": "Lo statement esi4-qcStatement-3 dichiara un periodo di conservazione (in anni dopo la scadenza del certificato) per le informazioni rilevanti ai fini dell'uso e dell'affidamento sul certificato, tenuto conto che l'affidamento sui certificati qualificati puo' dipendere dall'esistenza di informazioni esterne conservate dalla CA.",
        "testo_integrale": "Reliance on qualified certificates can depend on the existence of external information retained by the CA. This QCStatement declares a retention period for material information relevant to the use of and reliance on a certificate, expressed as a number of years after the expiry date of the certificate.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.4 (significato)",
        "testo": "Lo statement esi4-qcStatement-5 contiene URL a PKI Disclosure Statement (PDS) in accordo con l'Annex A di ETSI EN 319 411-1.",
        "testo_integrale": "This QCStatement holds URLs to PKI Disclosure Statements (PDS) in accordance with Annex A of ETSI EN 319 411-1 [i.10].",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "QCS-4.3.5-01",
        "testo": "Un prestatore di servizi fiduciari qualificato puo' includere nello statement lo statement sul metodo di identificazione usato per la verifica dell'identita' secondo l'art. 24 eIDAS1/eIDAS2 (facolta', non obbligo).",
        "testo_integrale": "QCS-4.3.5-01: A qualified TSP may include this qcStatement in the issued qualified certificates.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 4.3.5.3 (metodi di identificazione eIDAS successivi a eIDAS2)",
        "testo": "Definisce due identificatori OID utilizzabili nello statement esi4-qcStatement-8: id-etsi-qct-eIDAS2-acd, assegnabile a un certificato qualificato di firma o sigillo emesso in conformita' dell'art. 24, §1-bis, lett. a), c) o d) del Regolamento (UE) 2024/1183 (utilizzabile per emettere successivamente un certificato qualificato o un attestato elettronico qualificato di attributi); id-etsi-qct-eIDAS2-b, assegnabile a un certificato emesso in conformita' dell'art. 24, §1-bis, lett. b) (non utilizzabile per emissioni successive).",
        "testo_integrale": "The following identifiers can be used for Identification according to Regulation (EU) 910/2014 [i.8] Article 24.1 with amendment in Regulation (EU) 2024/1183 [i.13]: Identification according to eIDAS2 [i.13] Article 24. paragraph 1a a) or c) or d): id-etsi-qct-eIDAS2-acd OBJECT IDENTIFIER ::= { id-etsi-qcs-QcIdentMethod 3 }. May be assigned to a certificate of a qualified electronic signature or of a qualified electronic seal issued in compliance with Regulation (EU) 2024/1183 Article 24.1a point (a), (c) or (d); can subsequently be used to issue a qualified certificate or QEAA. Identification according to eIDAS2 Article 24. paragraph 1a b): id-etsi-qct-eIDAS2-b OBJECT IDENTIFIER ::= { id-etsi-qcs-QcIdentMethod 4 }. May be assigned to a certificate issued in compliance with Regulation (EU) 2024/1183 Article 24.1a point (b); cannot subsequently be used to issue a qualified certificate or QEAA.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["certificato qualificato di firma elettronica", "certificato qualificato di sigillo elettronico", "attestato elettronico di attributi qualificato"],
    },
    {
        "riferimento": "Annex A.1 (mapping con Allegato I Reg. 910/2014)",
        "testo": "Tabella informativa che mappa ciascun requisito dell'Allegato I del Regolamento (UE) 910/2014 (certificati qualificati di firma elettronica) sulla clausola del presente documento (o di ETSI EN 319 412-2, o di IETF RFC 5280) che ne fornisce l'implementazione tecnica: dall'indicazione automatizzabile della qualifica (clausole 4.2.1/4.2.3) all'indicazione che la firma risiede in un QSCD (clausola 4.2.2).",
        "testo_integrale": "Annex A (informative): Relationship with Regulation (EU) No 910/2014. A.1 EU qualified certificates for electronic signatures — Table A.1: Mapping with Annex I of Regulation (EU) No 910/2014 [i.8]. (a) indication automated-processing-readable of qualified certificate for electronic signature -> clauses 4.2.1 and 4.2.3. (b) data representing the QTSP issuer -> issuer field, clause 4.2.3 of ETSI EN 319 412-2. (c) name of signatory/pseudonym -> clause 4.2.4 of ETSI EN 319 412-2. (d) signature validation data -> public key, RFC 5280 + clause 4.2.5 of ETSI EN 319 412-2. (e) validity period -> RFC 5280. (f) certificate identity code -> serial number, RFC 5280. (g) advanced signature/seal of issuing QTSP -> digital signature of issuer, RFC 5280. (h) location of supporting certificate -> Authority Info Access extension, RFC 5280 + clause 4.4.1 EN 319 412-2. (i) location of validity status services -> CRL Distribution point / Authority Info Access, RFC 5280 + clauses 4.3.11/4.4.1 EN 319 412-2. (j) indication that signature creation data resides in QSCD -> explicit statement, clause 4.2.2.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["certificato qualificato di firma elettronica"],
    },
    {
        "riferimento": "Annex A.2 (mapping con Allegato III Reg. 910/2014)",
        "testo": "Tabella informativa analoga a A.1, che mappa ciascun requisito dell'Allegato III del Regolamento (UE) 910/2014 (certificati qualificati di sigillo elettronico) sulla clausola del presente documento (o di ETSI EN 319 412-2/3, o di IETF RFC 5280) che ne fornisce l'implementazione tecnica.",
        "testo_integrale": "A.2 EU qualified certificates for electronic seals - Table A.2: Mapping with Annex III of Regulation (EU) No 910/2014 [i.8]. Stessa struttura di A.1, mutatis mutandis per i sigilli elettronici; (a) indicazione automatizzabile -> clausole 4.2.1 e 4.2.3; (c) nome del creatore del sigillo -> clausola 4.2.1 di ETSI EN 319 412-3; (j) indicazione che la chiave risiede in un QSCD -> clausola 4.2.2.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["certificato qualificato di sigillo elettronico"],
    },
    {
        "riferimento": "Annex A.3 (mapping con Allegato IV Reg. 910/2014)",
        "testo": "Tabella informativa che mappa ciascun requisito dell'Allegato IV del Regolamento (UE) 910/2014 (certificati qualificati di autenticazione di siti web) sulla clausola del presente documento (per l'indicazione automatizzabile della qualifica, clausole 4.2.1/4.2.3) o sui requisiti del CA/Browser Forum Baseline Requirements/Extended Validation Requirements e di IETF RFC 5280 per tutti gli altri elementi (dati del QTSP, identita' del titolare, indirizzo, domain name, validita', firma, location, status di validita').",
        "testo_integrale": "A.3 EU qualified certificates for website authentication — Table A.3: Mapping with Annex IV of Regulation (EU) No 910/2014 [i.8]. (a) indicazione automatizzabile di certificato qualificato per autenticazione siti web -> clauses 4.2.1 and 4.2.3. (b)-(j): dati rappresentativi del QTSP, nome/pseudonimo, indirizzo, domain name, validita', codice identita', firma avanzata, location, status di validita' -> CA/Browser Forum Baseline Requirements [i.11] e Extended Validation Requirements [i.12], RFC 5280 (nessun rinvio a clausole del presente documento).",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["certificato qualificato di autenticazione di siti web"],
    },
    {
        "riferimento": "Annex B (dichiarazioni ASN.1)",
        "testo": "Modulo ASN.1 normativo completo (ETSIQCstatementsMod) che definisce tutti gli statement esi4-qcStatement-1..9 e i relativi object identifier, richiamato come autoritativo da QCS-4.1-04: in caso di discrepanza con le definizioni ASN.1 riportate nel corpo del documento, prevale il testo di questo Annex.",
        "testo_integrale": "Annex B (normative): ASN.1 declarations. ETSIQCstatementsMod { itu-t(0) identified-organization(4) etsi(0) id-qc-statements(194125) id-mod(0) id-mod-qc-statements(0) v2(1) } DEFINITIONS EXPLICIT TAGS ::= BEGIN -- EXPORTS All IMPORTS QC-STATEMENT, qcStatement-2 FROM PKIXqualified97 {iso(1) identified-organization(3) dod(6) internet(1) security(5) mechanisms(5) pkix(7) id-mod(0) id-mod-qualified-cert-97(35)}; -- statements esi4-qcStatement-1 QC-STATEMENT ::= { IDENTIFIED BY id-etsi-qcs-QcCompliance } -- EU qualified certificate declaration esi4-qcStatement-2 QC-STATEMENT ::= { SYNTAX QcEuLimitValue IDENTIFIED BY id-etsi-qcs-QcLimitValue } -- Declaration of limit value QcEuLimitValue ::= MonetaryValue MonetaryValue ::= SEQUENCE { currency Iso4217CurrencyCode, amount INTEGER, exponent INTEGER } Iso4217CurrencyCode ::= CHOICE { alphabetic PrintableString (SIZE (3)), numeric INTEGER (1..999) } esi4-qcStatement-3 QC-STATEMENT ::= { SYNTAX QcEuRetentionPeriod IDENTIFIED BY id-etsi-qcs-QcRetentionPeriod } -- Retention period declaration QcEuRetentionPeriod ::= INTEGER esi4-qcStatement-4 QC-STATEMENT ::= { IDENTIFIED BY id-etsi-qcs-QcSSCD } -- SSCD and QSCD declaration esi4-qcStatement-5 QC-STATEMENT ::= { SYNTAX QcEuPDS IDENTIFIED BY id-etsi-qcs-QcPDS } -- PKI Disclosure statements QcEuPDS ::= PdsLocations PdsLocations ::= SEQUENCE SIZE (1..MAX) OF PdsLocation PdsLocation ::= SEQUENCE { url IA5String, language PrintableString (SIZE(2)) } esi4-qcStatement-6 QC-STATEMENT ::= { SYNTAX QcType IDENTIFIED BY id-etsi-qcs-QcType } -- Certificate type QcType ::= SEQUENCE SIZE (1) OF OBJECT IDENTIFIER (id-etsi-qct-esign | id-etsi-qct-eseal | id-etsi-qct-web | ...) esi4-qcStatement-7 QC-STATEMENT ::= { SYNTAX QcCClegislation IDENTIFIED BY id-etsi-qcs-QcCClegislation } -- country or set of countries QcCClegislation ::= SEQUENCE OF CountryName CountryName ::= PrintableString (SIZE (2)) (CONSTRAINED BY { -- ISO 3166-1 [6] alpha-2 codes only -- }) esi4-qcStatement-8 QC-STATEMENT ::= { SYNTAX QcIdentMethod IDENTIFIED BY id-etsi-qcs-QcIdentMethod } -- identification method eIDAS1/eIDAS2 QcIdentMethod ::= SEQUENCE SIZE (1) OF OBJECT IDENTIFIER (id-etsi-qct-eIDAS1-ab | id-etsi-qct-eIDAS1-cd | id-etsi-qct-eIDAS2-acd | id-etsi-qct-eIDAS2-b | ...) id-etsi-qcs-QcQSCDlegislation OBJECT IDENTIFIER ::= { id-etsi-qcs 9 } -- Non-EU QSCD QcQSCDlegislation ::= SEQUENCE SIZE (1..MAX) OF CountryName -- object identifiers id-etsi-qcs OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4) etsi(0) id-qc-profile(1862) 1 } id-etsi-qcs-QcCompliance OBJECT IDENTIFIER ::= { id-etsi-qcs 1 } id-etsi-qcs-QcLimitValue OBJECT IDENTIFIER ::= { id-etsi-qcs 2 } id-etsi-qcs-QcRetentionPeriod OBJECT IDENTIFIER ::= { id-etsi-qcs 3 } id-etsi-qcs-QcSSCD OBJECT IDENTIFIER ::= { id-etsi-qcs 4 } id-etsi-qcs-QcPDS OBJECT IDENTIFIER ::= { id-etsi-qcs 5 } id-etsi-qcs-QcType OBJECT IDENTIFIER ::= { id-etsi-qcs 6 } id-etsi-qcs-QcCClegislation OBJECT IDENTIFIER ::= { id-etsi-qcs 7 } id-etsi-qcs-QcIdentMethod OBJECT IDENTIFIER ::= { id-etsi-qcs 8 } id-etsi-qcs-QcQSCDlegislation OBJECT IDENTIFIER ::= { id-etsi-qcs 9 } id-etsi-qct-esign OBJECT IDENTIFIER ::= { id-etsi-qcs-QcType 1 } id-etsi-qct-eseal OBJECT IDENTIFIER ::= { id-etsi-qcs-QcType 2 } id-etsi-qct-web OBJECT IDENTIFIER ::= { id-etsi-qcs-QcType 3 } id-etsi-qct-eIDAS1-ab OBJECT IDENTIFIER ::= { id-etsi-qcs-QcIdentMethod 1 } -- Identification according to eIDAS1 Article 24. paragraph 1 a) or b) id-etsi-qct-eIDAS1-cd OBJECT IDENTIFIER ::= { id-etsi-qcs-QcIdentMethod 2 } -- Identification according to eIDAS1 Article 24. paragraph 1 c) or d) id-etsi-qct-eIDAS2-acd OBJECT IDENTIFIER ::= { id-etsi-qcs-QcIdentMethod 3 } -- Identification according to eIDAS2 Article 24. paragraph 1a a) or c) or d) id-etsi-qct-eIDAS2-b OBJECT IDENTIFIER ::= { id-etsi-qcs-QcIdentMethod 4 } -- Identification according to eIDAS2 Article 24. paragraph 1a b) SupportedStatements QC-STATEMENT ::= { qcStatement-2 | esi4-qcStatement-1 | esi4-qcStatement-2 | esi4-qcStatement-3 | esi4-qcStatement-4 | esi4-qcStatement-5 | esi4-qcStatement-6 | esi4-qcStatement-7 | esi4-qcStatement-8 | esi4-qcStatement-9 | ... } END",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "QCS-4.1-01", "QCS-4.1-02", "QCS-4.1-03", "QCS-4.1-04",
    "QCS-4.2.1-01", "QCS-4.2.4-01", "QCS-4.2.5-01",
    "QCS-4.3.2-01", "QCS-4.3.2-02",
    "QCS-4.3.4-01", "QCS-4.3.4-02", "QCS-4.3.4-03",
    "QCS-4.3.5-02", "QCS-5-01",
    "clausola 1 (Scope)",
    "clausola 3 (definizioni, simboli, abbreviazioni, notazioni)",
    "clausola 4.2.1 (significato)", "clausola 4.2.2", "clausola 4.2.3",
    "clausola 4.2.4 (significato)", "clausola 4.2.5 (significato)",
    "clausola 4.3.1 (Introduction)", "clausola 4.3.2 (significato)", "clausola 4.3.3",
    "clausola 4.3.4 (significato)", "QCS-4.3.5-01",
    "clausola 4.3.5.3 (metodi di identificazione eIDAS successivi a eIDAS2)",
    "Annex A.1 (mapping con Allegato I Reg. 910/2014)",
    "Annex A.2 (mapping con Allegato III Reg. 910/2014)",
    "Annex A.3 (mapping con Allegato IV Reg. 910/2014)",
    "Annex B (dichiarazioni ASN.1)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
