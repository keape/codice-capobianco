"""ETSI EN 319 412-1 V1.7.1 (2026-05) - Electronic Signatures and Trust
Infrastructures (ESI); Certificate Profiles; Part 1: Overview and common
data structures. Fonte 7 (stessa fonte multi-parte gia' usata per la Parte 5
QCStatements, app/seed_data/etsi_319_412/parte5.py), un unico capitolo
(documento tecnico di 18 pagine, sta comodamente nel contesto di una
sessione principale - nessuna suddivisione ulteriore necessaria). Testo
ufficiale in app/.source_cache/etsi_319_412/parte1_raw.txt.

Modellazione (ADR-0007), stesso approccio della Parte 5: un nodo per ogni
clausola/sottoclausola/requisito numerato con contenuto normativo/tecnico
proprio; front matter puramente amministrativo/bibliografico (Contents,
Intellectual Property Rights, Foreword, Modal verbs terminology,
Introduction, clausola 2 References normative+informative, Annex A
informative Change history, History) NON e' modellato come nodo, stesso
trattamento gia' riservato alla Parte 5.

Convenzione di disambiguazione cross-parte: ogni `riferimento` porta il
prefisso "Parte 1: " (le 5 parti del deliverable ETSI EN 319 412
rinumerano le clausole indipendentemente le une dalle altre - stesso
prefisso gia' retrofittato sui 31 nodi della Parte 5 con "Parte 5: ").

- Clausola 1 (Scope) -> Principio "scopo/ambito di applicazione".
- Clausola 3 (Definition of terms, symbols, abbreviations and notations,
  sottoclausole 3.1-3.4) -> un solo Principio "definitorio" aggregato per
  l'intera clausola (stesso pattern usato per la clausola 3 della Parte 5):
  e' un blocco terminologico/di notazione coeso, non una sequenza di
  requisiti numerati propri (a differenza delle clausole 5.1.x/5.2.x, che
  usano invece la notazione a identificatore di requisito GEN-/NAT-/LEG-
  definita proprio in questa clausola 3.4).
- Clausola 4 "ETSI EN 319 412 certificate profiles": 4.1 General approach
  -> Principio "definitorio" (descrive la base comune IETF RFC 5280 di
  tutti i profili, nessun requisito numerato proprio); 4.2.1/4.2.2/4.2.3/
  4.2.4 (rispettivamente Overview di Part 2/3/4/5) -> 4 Principio
  "definitorio" distinti, uno per sottoclausola, perche' ciascuno descrive
  lo scope di una parte diversa del deliverable con contenuto testuale
  proprio e non intercambiabile. La clausola 4.2 (header senza corpo
  proprio, va direttamente a 4.2.1) non genera un nodo a se'.
- Clausola 5 "Common data structures": ogni sottoclausola 5.1.1/5.1.2/
  5.1.3/5.1.4/5.1.5/5.1.6/5.2.1/5.2.2/5.2.3 e' coperta. Le sottoclausole
  5.1.1, 5.2.1 e 5.2.2 sono descrittive/di cornice (nessun requisito
  numerato GEN-/NAT-/LEG- proprio oltre a quelli esplicitamente elencati
  sotto) -> Principio "definitorio". Le sottoclausole 5.1.2-5.1.6 e 5.2.3
  sono interamente composte da requisiti numerati secondo la notazione
  <profilo>-<clausola>-<NN> definita in 3.4 (GEN-5.1.2-01, NAT-5.1.3-01..07,
  LEG-5.1.4-01..08, NAT-5.1.5-01..04, LEG-5.1.6-01..04, GEN-5.2.3-01): ogni
  requisito e' un nodo Obbligo distinto (soggetto implicito QTSP/gestore,
  ruolo "obbligato", tipo_obbligo "tecnico/sicurezza" - sono tutti requisiti
  di profilo tecnico del certificato, stessa convenzione della Parte 5),
  indipendentemente dal verbo modale con cui e' scritto il singolo
  requisito (incluse le sfumature "should"/"may" interne a NAT-5.1.3-04 e
  LEG-5.1.4-04): l'identificatore di requisito esplicito assegnato dal
  documento stesso e' qui il criterio di granularita' del nodo, non il
  singolo verbo modale.
- Eccezione esplicita in 5.1.1: GEN-5.1.1-01/02/03 sono tre requisiti
  numerati ma non ricadono nella regola precedente perche' non sono
  interamente "shall" come il resto della clausola 5 - due usano "may"
  (GEN-5.1.1-01/02, uso di codici paese transnazionali/'XG') e uno usa
  "shall" (GEN-5.1.1-03, interpretazione dei codici utente-definiti):
  modellati per verbo modale, "may" -> Principio "altro" (facolta', non
  prescrizione), "shall" -> Obbligo.
- Requisiti condizionali (testo con "If"/"When"/"In case" che introduce una
  dipendenza da una scelta/attributo/policy specifica, es. NAT-5.1.3-02
  "When the natural person semantics identifier is included...",
  LEG-5.1.4-04 "In case VAT... is used...", NAT-5.1.5-01/02 "If using
  electronic identity attributes...") -> Obbligo con
  condizione_applicabilita esplicita valorizzata, mai omessa. I requisiti
  che riprendono/derivano la stessa condizione di un requisito immediatamente
  precedente nella stessa struttura enumerata (es. NAT-5.1.5-03/04 sotto la
  condizione di NAT-5.1.5-02, LEG-5.1.6-03/04 sotto quella di
  LEG-5.1.6-02) ereditano la medesima condizione_applicabilita.
- La NOTE conclusiva di 5.1.1 (sul meccanismo di semantics identifier nel
  campo issuer) segue testualmente GEN-5.1.1-03 nel documento ma descrive
  il meccanismo generale della clausola, non lo specifico requisito su
  codici utente-definiti: e' quindi accorpata nel nodo Principio di 5.1.1
  General, non in GEN-5.1.1-03, per evitare di mescolare contenuto
  descrittivo generale con un requisito normativo puntuale (nessun testo
  perso: ogni frase del documento compare in esattamente un nodo).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "Parte 1: GEN-5.1.1-03",
        "testo": "Gli identificatori che utilizzano codici paese definiti dall'utente devono essere interpretati nel contesto dell'emittente del certificato, poiché non vi è garanzia di unicità tra tutti gli emittenti; i codici non assegnati non dovrebbero essere usati.",
        "testo_integrale": "GEN-5.1.1-03: Identifiers using user-defined country codes shall be interpreted under the context of the certificate issuer as there is no guarantee that such identifier is unique across all issuers. Unassigned codes should not be used.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo agli identificatori che utilizzano codici paese definiti dall'utente (user-defined country codes, es. 'XG').",
    },
    {
        "riferimento": "Parte 1: GEN-5.1.2-01",
        "testo": "La sintassi dell'identificatore di semantica per persona fisica e per persona giuridica deve essere quella definita dal modulo ASN.1 ETSISemanticsIdentifierMod, che definisce gli OID id-etsi-qcs-semanticsId-Natural, id-etsi-qcs-SemanticsId-Legal, id-etsi-qcs-semanticsId-eIDASNatural e id-etsi-qcs-SemanticsId-eIDASLegal.",
        "testo_integrale": "GEN-5.1.2-01: This clause defines semantics identifiers for inclusion in qcStatement-2. The syntax for the natural person semantics identifier and legal person semantics identifier shall be as defined by the following ASN.1 module: ETSISemanticsIdentifierMod { itu-t(0) identified-organization(4) etsi(0) id-cert-profile(194121) id-mod(0) id-mod-semantics-identifier(0) v2(1)} DEFINITIONS EXPLICIT TAGS::= BEGIN -- EXPORTS All -- Semantics identifiers id-etsi-qcs-semantics-identifiers OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4) etsi(0) id-cert-profile(194121) 1 } -- Semantics identifier for natural person identifier id-etsi-qcs-semanticsId-Natural OBJECT IDENTIFIER ::= { id-etsi-qcs-semantics-identifiers 1 } -- Semantics identifier for legal person identifier id-etsi-qcs-SemanticsId-Legal OBJECT IDENTIFIER ::= { id-etsi-qcs-semantics-identifiers 2 } -- Semantics identifier for eIDAS natural person identifier id-etsi-qcs-semanticsId-eIDASNatural OBJECT IDENTIFIER ::= { id-etsi-qcs-semantics-identifiers 3 } -- Semantics identifier for legal person identifier id-etsi-qcs-SemanticsId-eIDASLegal OBJECT IDENTIFIER ::= { id-etsi-qcs-semantics-identifiers 4 } END The following clauses provide the semantics definitions of the natural person and legal person semantics identifiers.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: NAT-5.1.3-01",
        "testo": "La semantica di id-etsi-qcs-SemanticsId-Natural è quella definita nella presente clausola.",
        "testo_integrale": "NAT-5.1.3-01: The semantics of id-etsi-qcs-SemanticsId-Natural shall be as follows.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: NAT-5.1.3-02",
        "testo": "Se incluso l'identificatore di semantica per persona fisica, l'eventuale attributo serialNumber nel campo subject deve contenere le informazioni secondo la struttura: 3 caratteri di tipo di identità, 2 caratteri di codice paese ISO 3166-1 (salvo eccezioni NAT-5.1.3-03(5)), trattino \"-\", identificatore.",
        "testo_integrale": "NAT-5.1.3-02: When the natural person semantics identifier is included, any present serialNumber attribute in the subject field shall contain information using the following structure in the presented order: 3 character natural person identity type reference; 2 character ISO 3166-1 [2] country code, except as allowed by NAT-5.1.3-03 (5); hyphen-minus \"-\" (0x2D (ASCII), U+002D (UTF-8)); and identifier (according to country and identity type reference).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'identificatore di semantica per persona fisica (id-etsi-qcs-SemanticsId-Natural) è incluso nel certificato.",
    },
    {
        "riferimento": "Parte 1: NAT-5.1.3-03",
        "testo": "I tre caratteri iniziali del riferimento di tipo di identità naturale devono avere uno dei valori definiti: \"PAS\" (passaporto), \"IDC\" (carta d'identità nazionale), \"PNO\" (numero di identificazione personale/civica nazionale), \"TAX\" (numero di riferimento fiscale personale), \"TIN\" (Tax Identification Number secondo la Commissione Europea), \"EID\" (mezzi di identificazione elettronica), oppure due caratteri di definizione locale seguiti da \":\". Altre sequenze iniziali sono riservate a future modifiche del documento.",
        "testo_integrale": "NAT-5.1.3-03: The three initial characters shall have one of the following defined values: 1) \"PAS\" for identification based on passport number. 2) \"IDC\" for identification based on national identity card number. 3) \"PNO\" for identification based on (national) personal number (national civic registration number). 4) \"TAX\" for identification based on a personal tax reference number issued by a national tax authority. 5) \"TIN\" Tax Identification Number according to the European Commission - Tax and Customs Union (https://ec.europa.eu/taxation_customs/tin/tinByCountry.html). NOTE: This means for Greece, the \"EL\" can be used instead of \"GR\". 6) \"EID\" for identification based on electronic identification means (e.g. national eID). 7) Two characters according to local definition within the specified country and name registration authority, identifying a national scheme that is considered appropriate for national and European level, followed by the character \":\" (colon). Other initial character sequences are reserved for future amendments of the present document. EXAMPLE: \"PASSK-P3000180\", \"IDCBE-590082394654\", \"TINEL-123456789\" and \"EI:SE-200007292386\".",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: NAT-5.1.3-04",
        "testo": "Il valore \"TAX\" è deprecato; dovrebbe essere usato \"TIN\" al suo posto.",
        "testo_integrale": "NAT-5.1.3-04: The value \"TAX\" is deprecated. The value \"TIN\" should be used instead.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: NAT-5.1.3-05",
        "testo": "Se viene fornito un riferimento di tipo di identità definito localmente (due caratteri seguiti da \":\"), l'elemento nameRegistrationAuthorities di SemanticsInformation deve essere presente.",
        "testo_integrale": "NAT-5.1.3-05: When a locally defined identity type reference is provided (two characters followed by \":\"), the nameRegistrationAuthorities element of SemanticsInformation (IETF RFC 3739 [1]) shall be present.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se viene fornito un riferimento di tipo di identità naturale definito localmente (due caratteri seguiti dal carattere ':').",
    },
    {
        "riferimento": "Parte 1: NAT-5.1.3-06",
        "testo": "L'elemento nameRegistrationAuthorities di SemanticsInformation deve contenere almeno un generalName di tipo uniformResourceIdentifier.",
        "testo_integrale": "NAT-5.1.3-06: The nameRegistrationAuthorities element of SemanticsInformation (IETF RFC 3739 [1]) shall contain at least a uniformResourceIdentifier generalName.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: NAT-5.1.3-07",
        "testo": "Il riferimento di tipo di identità a due lettere che precede il carattere \":\" deve essere unico nel contesto dell'uniformResourceIdentifier specificato.",
        "testo_integrale": "NAT-5.1.3-07: The two-letter identity type reference preceding the \":\" character shall be unique within the context of the specified uniformResourceIdentifier.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: LEG-5.1.4-01",
        "testo": "La semantica di id-etsi-qcs-SemanticsId-Legal è quella definita nella presente clausola.",
        "testo_integrale": "LEG-5.1.4-01: The semantics of id-etsi-qcs-SemanticsId-Legal shall be as follows.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: LEG-5.1.4-02",
        "testo": "Se incluso l'identificatore di semantica per persona giuridica, l'eventuale attributo organizationIdentifier nel campo subject deve contenere le informazioni secondo la struttura: 3 caratteri di tipo di identità, 2 caratteri di codice paese ISO 3166-1 (salvo eccezioni LEG-5.1.4-04), trattino \"-\", identificatore.",
        "testo_integrale": "LEG-5.1.4-02: When the legal person semantics identifier is included, any present organizationIdentifier attribute in the subject field shall contain information using the following structure in the presented order: 3 character legal person identity type reference; 2 character ISO 3166-1 [2] country code, except as allowed by LEG-5.1.4-04; hyphen-minus \"-\" (0x2D (ASCII), U+002D (UTF-8)); and identifier (according to country and identity type reference).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'identificatore di semantica per persona giuridica (id-etsi-qcs-SemanticsId-Legal) è incluso nel certificato.",
    },
    {
        "riferimento": "Parte 1: LEG-5.1.4-03",
        "testo": "I tre caratteri iniziali del riferimento di tipo di identità giuridica devono avere uno dei valori definiti: \"VAT\" (numero di identificazione IVA nazionale), \"NTR\" (identificatore da registro delle imprese nazionale), \"PSD\" (numero di autorizzazione nazionale di un prestatore di servizi di pagamento ex Direttiva 2015/2366, con struttura estesa ETSI TS 119 495 clausola 5.2.1), \"LEI\" (Legal Entity Identifier globale ISO 17442, con codice paese fisso 'XG'), \"EOR\" (numero EORI), \"EXC\" (numero di accisa ex Regolamento (CE) 389/2012), oppure due caratteri di definizione locale seguiti da \":\". Altre sequenze iniziali sono riservate a future modifiche del documento.",
        "testo_integrale": "LEG-5.1.4-03: The three initial characters shall have one of the following defined values: 1) \"VAT\" for identification based on a national value added tax identification number. 2) \"NTR\" for identification based on an identifier from a national trade register. 3) \"PSD\" for identification based on national authorization number of a payment service provider under Payments Services Directive (EU) 2015/2366 [i.13] or equivalent national or international legislation. This shall use the extended structure as defined in ETSI TS 119 495 [3], clause 5.2.1. 4) \"LEI\" for a global Legal Entity Identifier as specified in ISO 17442 [4] and as referred to in Commission Implementing Regulation (EU) No 2022/18602 [i.20]. The 2 character ISO 3166-1 [2] country code shall be set to 'XG'. 5) \"EOR\" for Economic Operators Registration and Identification (EORI) number as referred to in Commission Implementing Regulation (EU) No 1352/20131 [i.18]. 6) \"EXC\" for an excise number as specified in Article 2(12) of Council Regulation (EC) No 389/20123 [i.19]. 7) Two characters according to local definition within the specified country and name registration authority, identifying a national scheme that is considered appropriate for national and European level, followed by the character \":\" (colon). Other initial character sequences are reserved for future amendments of the present document.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: LEG-5.1.4-04",
        "testo": "Se si usa il riferimento di tipo di identità giuridica \"VAT\", al posto del codice paese ISO 3166-1 a 2 caratteri può essere usato il prefisso paese di cui alla Direttiva 2006/112/CE art. 215, come modificato dalla Direttiva 2020/1756.",
        "testo_integrale": "LEG-5.1.4-04: In case \"VAT\" legal person identity type reference is used , the country prefix described in Council Directive 2006/112/EC [i.12], article 215 as amended by Council Directive 2020/1756 [i.16] may be used instead of the 2 character ISO 3166-1 [2] country code. EXAMPLE 1: \"VATBE-0876866142\", \"VATEL-123456789\", \"VATXI-123456789\" and \"EI:SE-5567971433\".",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se si utilizza il riferimento di tipo di identità giuridica \"VAT\".",
    },
    {
        "riferimento": "Parte 1: LEG-5.1.4-05",
        "testo": "Se viene fornito un riferimento di tipo di identità definito localmente (due caratteri seguiti da \":\"), l'elemento nameRegistrationAuthorities di SemanticsInformation deve essere presente e contenere almeno un generalName di tipo uniformResourceIdentifier.",
        "testo_integrale": "LEG-5.1.4-05: When a locally defined identity type reference is provided (two characters followed by \":\"), the nameRegistrationAuthorities element of SemanticsInformation (IETF RFC 3739 [1]) shall be present and shall contain at least a uniformResourceIdentifier generalName.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se viene fornito un riferimento di tipo di identità giuridica definito localmente (due caratteri seguiti dal carattere ':').",
    },
    {
        "riferimento": "Parte 1: LEG-5.1.4-06",
        "testo": "Il riferimento di tipo di identità a due lettere che segue il carattere \":\" deve essere unico nel contesto dell'uniformResourceIdentifier specificato.",
        "testo_integrale": "LEG-5.1.4-06: The two letter identity type reference following the \":\" character shall be unique within the context of the specified uniformResourceIdentifier.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: LEG-5.1.4-07",
        "testo": "Per il riferimento \"NTR\", se l'identificatore è unico a livello nazionale, l'attributo organizationIdentifier deve usare la struttura di LEG-5.1.4-02 con identificatore pari a: a) l'identificatore nazionale; oppure b) l'identificatore EUID del Business Registers Interconnection System (Reg. (UE) 2021/1042), composto da Business Register Identifier, punto \".\" e Business Registration Number.",
        "testo_integrale": "LEG-5.1.4-07: In the case of the \"NTR\" legal person identity type reference, if the identifier is unique at the national level, the organizationIdentifier attribute in the subject field shall use the structure defined in LEG-5.1.4-02 where the identifier, shall be one of the followings: a) the national identifier; b) the EUID identifier as available from the Business Registers Interconnection System according to Implementing Regulation (EU) 2021/1042 [8]: i) the Business Register Identifier, for the particular section or office of the public register having attributed the business registration number to the legal person in question; ii) dot-sign '.' (U+002E); iii) the Business Registration Number, as attributed to the legal person by the national business register in point (i) above. EXAMPLE 2: DED2601V.HRB12345 (Amtsgericht München). NOTE: It is recommended that business whose products relate to the European Product Registry for Energy Labelling (EPREL) [i.15] to use the b) option above because after April 22, 2025 the EPREL system of the EU will not accept a certificate with other identity types than EUID.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo al riferimento di tipo di identità giuridica \"NTR\" quando l'identificatore è unico a livello nazionale.",
    },
    {
        "riferimento": "Parte 1: LEG-5.1.4-08",
        "testo": "Per il riferimento \"NTR\", se gli identificatori sono assegnati a livello di suddivisione (stato/provincia) e non sono unici a livello nazionale, l'attributo organizationIdentifier deve usare: a) la struttura di LEG-5.1.4-07; oppure b) 3 caratteri di tipo di identità, 2 caratteri di codice paese, \"+\" seguito da un identificatore ISO 3166-2 della suddivisione (fino a 3 caratteri), trattino \"-\", identificatore.",
        "testo_integrale": "LEG-5.1.4-08: In the case of the \"NTR\" legal person identity type reference, if the identifiers are assigned at the subdivision (state or province) level and are not unique at the national level, the organizationIdentifier attribute in the subject field shall contain information using one the following structure in the presented order: a) as defined in LEG-5.1.4-07; b) in the following structure: 3 character legal person identity type reference; 2 character ISO 3166-1 [2] country; plus \"+\" (0x2B (ASCII), U+002B (UTF-8)) followed by an up-to-three character ISO 3166-2 [7] identifier for the subdivision; hyphen-minus \"-\" (0x2D (ASCII), U+002D (UTF-8)); and identifier (according to country and identity type reference). EXAMPLE 3: \"NTRDE+HE-123456\" (Germany, Hessen), \"NTRUS+CA-123456\" (United States, California).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo al riferimento di tipo di identità giuridica \"NTR\" quando gli identificatori sono assegnati a livello di suddivisione (stato/provincia) e non sono unici a livello nazionale.",
    },
    {
        "riferimento": "Parte 1: NAT-5.1.5-01",
        "testo": "Se si usano attributi di identità elettronica secondo l'eIDAS SAML Attribute Profile per un certificato emesso a persona fisica, la semantica di id-etsi-qcs-SemanticsId-eIDASNatural è quella definita nella presente clausola.",
        "testo_integrale": "NAT-5.1.5-01: If using electronic identity attributes as specified in eIDAS SAML attribute profile [5] for a certificate issued to natural persons, the semantics of id-etsi-qcs-SemanticsId-eIDASNatural shall be as follows.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se si utilizzano attributi di identità elettronica come specificato nell'eIDAS SAML Attribute Profile [5] per un certificato emesso a una persona fisica.",
    },
    {
        "riferimento": "Parte 1: NAT-5.1.5-02",
        "testo": "Se incluso l'identificatore di semantica eIDAS per persona fisica, i valori degli attributi nel campo subject devono soddisfare i requisiti di contenuto degli attributi corrispondenti definiti dall'eIDAS SAML Attribute Profile, secondo i requisiti NAT-5.1.5-03 e NAT-5.1.5-04.",
        "testo_integrale": "NAT-5.1.5-02: If the eIDAS natural person semantics identifier is included, the values of attributes in the subject field shall meet the content requirements of corresponding attributes defined by the eIDAS SAML attribute profile [5] according to the following requirements.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'identificatore di semantica eIDAS per persona fisica (id-etsi-qcs-SemanticsId-eIDASNatural) è incluso nel certificato.",
    },
    {
        "riferimento": "Parte 1: NAT-5.1.5-03",
        "testo": "L'eventuale attributo serialNumber presente nel campo subject del certificato deve rispettare il requisito di contenuto specificato per l'attributo eIDAS PersonIdentifier.",
        "testo_integrale": "NAT-5.1.5-03: Any serialNumber attribute present in the subject field of the certificate shall comply with the content requirement specified for the eIDAS PersonIdentifier attribute.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'identificatore di semantica eIDAS per persona fisica (id-etsi-qcs-SemanticsId-eIDASNatural) è incluso nel certificato.",
    },
    {
        "riferimento": "Parte 1: NAT-5.1.5-04",
        "testo": "Gli attributi presenti nel campo subject del certificato sono equivalenti agli attributi eIDAS definiti secondo la tabella 5.1.5-1 (serialNumber~PersonIdentifier, surname~FamilyName, givenName~FirstName, dateOfBirth~DateOfBirth): l'attributo presente deve contenere un'informazione equivalente, anche se il formato usato per esprimerla differisce.",
        "testo_integrale": "NAT-5.1.5-04: Attributes present in subject field of the certificate are equivalent to defined attributes in accordance with table 5.1.5-1. This means that the present attribute shall hold equivalent information, even if the format used to express that information differs. Table 5.1.5-1: Attribute equivalence. Certificate attribute serialNumber, defined by Recommendation ITU-T X.520 [i.10], equivalent eIDAS eID attribute (FriendlyName) PersonIdentifier. Certificate attribute surname, defined by Recommendation ITU-T X.520 [i.10], equivalent eIDAS eID attribute (FriendlyName) FamilyName. Certificate attribute givenName, defined by Recommendation ITU-T X.520 [i.10], equivalent eIDAS eID attribute (FriendlyName) FirstName. Certificate attribute dateOfBirth, defined by IETF RFC 3739 [1], equivalent eIDAS eID attribute (FriendlyName) DateOfBirth.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'identificatore di semantica eIDAS per persona fisica (id-etsi-qcs-SemanticsId-eIDASNatural) è incluso nel certificato.",
    },
    {
        "riferimento": "Parte 1: LEG-5.1.6-01",
        "testo": "Se si usano attributi di identità elettronica secondo l'eIDAS SAML Attribute Profile per un certificato emesso a persona giuridica, la semantica di id-etsi-qcs-SemanticsId-eIDASLegal è quella definita nella presente clausola.",
        "testo_integrale": "LEG-5.1.6-01: If using electronic identity attributes as specified in eIDAS SAML attribute profile [5] for a certificate issued to legal persons, the semantics of id-etsi-qcs-SemanticsId-eIDASLegal shall be as follows.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se si utilizzano attributi di identità elettronica come specificato nell'eIDAS SAML Attribute Profile [5] per un certificato emesso a una persona giuridica.",
    },
    {
        "riferimento": "Parte 1: LEG-5.1.6-02",
        "testo": "Se incluso l'identificatore di semantica eIDAS per persona giuridica, i valori degli attributi nel campo subject devono soddisfare i requisiti di contenuto degli attributi corrispondenti definiti dall'eIDAS SAML Attribute Profile, secondo i requisiti LEG-5.1.6-03 e LEG-5.1.6-04.",
        "testo_integrale": "LEG-5.1.6-02: If the eIDAS legal person semantics identifier is included, the values of attributes in the subject field shall meet the content requirements of corresponding attributes defined by the eIDAS SAML attribute profile [5] according to the following requirements.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'identificatore di semantica eIDAS per persona giuridica (id-etsi-qcs-SemanticsId-eIDASLegal) è incluso nel certificato.",
    },
    {
        "riferimento": "Parte 1: LEG-5.1.6-03",
        "testo": "L'eventuale attributo organizationIdentifier presente nel campo subject del certificato deve rispettare il requisito di contenuto specificato per l'attributo eIDAS LegalPersonIdentifier.",
        "testo_integrale": "LEG-5.1.6-03: Any organizationIdentifier attribute present in the subject field of the certificate shall comply with the content requirement specified for the eIDAS LegalPersonIdentifier attribute.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'identificatore di semantica eIDAS per persona giuridica (id-etsi-qcs-SemanticsId-eIDASLegal) è incluso nel certificato.",
    },
    {
        "riferimento": "Parte 1: LEG-5.1.6-04",
        "testo": "Gli attributi presenti nel campo subject del certificato sono equivalenti agli attributi eIDAS definiti secondo la tabella 5.1.6-1 (organizationIdentifier~LegalPersonIdentifier, organizationName~LegalName): l'attributo presente deve contenere un'informazione equivalente, anche se il formato usato per esprimerla differisce.",
        "testo_integrale": "LEG-5.1.6-04: Attributes present in the subject field of the certificate are equivalent to defined attributes in accordance with table 5.1.6-1. This means that the present attribute shall hold equivalent information, even if the format used to express that information differs. Table 5.1.6-1: Attribute equivalence. Certificate attribute organizationIdentifier, defined by Recommendation ITU-T X.520 [i.10], equivalent eIDAS attribute (FriendlyName) LegalPersonIdentifier. Certificate attribute organizationName, defined by Recommendation ITU-T X.520 [i.10], equivalent eIDAS attribute (FriendlyName) LegalName.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'identificatore di semantica eIDAS per persona giuridica (id-etsi-qcs-SemanticsId-eIDASLegal) è incluso nel certificato.",
    },
    {
        "riferimento": "Parte 1: GEN-5.2.3-01",
        "testo": "Il modulo ASN.1 ETSIValAssuredCertMod deve importare i tipi e le strutture da IETF RFC 5912 come indicato nella sua sezione IMPORTS; definisce l'estensione id-etsi-ext-valassured-ST-certs (certificato a breve termine), con sintassi NULL.",
        "testo_integrale": "GEN-5.2.3-01: The ASN.1 module defined in the present clause shall import the types and structures from IETF RFC 5912 [6] as written in the import part of the module. ETSIValAssuredCertMod { itu-t(0) identified-organization(4) etsi(0) id-cert-profile(194121) id-mod(0) id-mod-validity-assured(1) v1(0) } DEFINITIONS ::= BEGIN -- EXPORTS All IMPORTS EXTENSION FROM PKIX-CommonTypes-2009 { iso(1) identified-organization(3) dod(6) internet(1) security(5) mechanisms(5) pkix(7) id-mod(0) id-mod-pkixCommon-02(57) }; -- Extensions id-etsi-ext OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4) etsi(0) id-cert-profile(194121) 2 } -- Extension for short-term certificate id-etsi-ext-valassured-ST-certs OBJECT IDENTIFIER ::= { id-etsi-ext 1 } ext-etsi-valassured-ST-certs EXTENSION ::= { SYNTAX NULL IDENTIFIED BY id-etsi-ext-valassured-ST-certs } END",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "Parte 1: clausola 1 (Scope)",
        "testo": "Il documento fornisce una panoramica dei profili di certificato basati su Raccomandazione ITU-T X.509 | ISO/IEC 9594-8 e degli statement per i certificati qualificati UE specificati nelle altre parti di ETSI EN 319 412; specifica le strutture dati comuni richiamate dalle altre parti. I profili mirano a supportare sia il Regolamento (UE) 910/2014 sia l'uso dei certificati in un contesto internazionale più ampio, incluse sia i certificati qualificati UE sia altre forme di certificato.",
        "testo_integrale": "1 Scope: The present document provides an overview of the Recommendation ITU-T X.509 | ISO/IEC 9594-8 [i.3] based certificate profiles and the statements for EU Qualified Certificates specified in other parts of ETSI EN 319 412 ([i.4] to [i.7]). It specifies common data structures that are referenced from other parts of ETSI EN 319 412 ([i.4] to [i.7]). The profiles specified in this multi-part deliverable aim to support both Regulation (EU) No 910/2014 [i.9] and the use of certificates in a wider international context. Within the European context, it aims to support both EU Qualified Certificates and other forms of certificate.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 3 (definizioni, simboli, abbreviazioni, notazioni)",
        "testo": "Definisce (3.1) i termini \"EU Qualified Certificate\" e \"short-term certificate\" (oltre a quelli di ETSI EN 319 401); (3.2) nessun simbolo (Void); (3.3) le abbreviazioni usate nel documento (ASN.1, CA, CIR, CRL, eID, eIDAS, EORI, EPREL, EUID, LEI, OCSP, OID, SAML, TLS, TSP, UN); (3.4) la notazione degli identificativi dei requisiti (prefisso a 3 lettere di profilo - numero di clausola - numero progressivo a 2 cifre; profili GEN/NAT/LEG/WEB/QCS) e le regole di gestione degli identificativi nelle edizioni successive del documento (nuovo requisito a fine clausola, inserimento intermedio con lettere maiuscole, requisito soppresso marcato \"Void\", requisito modificato con lettere aggiunte).",
        "testo_integrale": "3 Definition of terms, symbols, abbreviations and notations. 3.1 Terms: For the purposes of the present document, the terms given in ETSI EN 319 401 [i.2] and the following apply: EU Qualified Certificate: qualified certificate that is stated to be in accordance with Annex I, III or IV of Regulation (EU) No 910/2014 [i.9] or Annex I of Directive 1999/93/EC [i.1] whichever is in force at the time of issuance. short-term certificate: certificate whose validity period, i.e. the period of time from notBefore through notAfter, inclusive, is shorter than the maximum time to process a revocation request as specified in the certificate practice statement. 3.2 Symbols: Void. 3.3 Abbreviations: For the purposes of the present document, the following abbreviations apply: ASN.1 Abstract Syntax Notation 1. CA Certification Authority. CIR Commission Implementing Regulation. CRL Certificate Revocation List. eID electronic IDentity. NOTE: In line with eIDAS SAML Attribute Profile [5]. eIDAS electronic IDentification, Authentication and trust Services. EORI Economic Operators Registration and Identification. EPREL European Product Registry for Energy Labelling. NOTE: See Commission Implementing Regulation (EU) 2024/994 [i.15]. EUID European Unique IDentifier. NOTE: See Implementing Regulation (EU) 2021/1042 [8]. LEI Legal Entity Identifier. OCSP Online Certificate Status Protocol. OID Object IDentifier. SAML Security Assertion Markup Language. TLS Transport Layer Security protocol. NOTE: As specified in IETF RFC 5246 [i.8]. TSP Trust Service Provider. UN United Nations. 3.4 Notations: The requirements identified in the present document are preceded by a 3-letter prefix to denote the applicability to specific profiles as covered by the present multi-part deliverable. Each requirement is identified as follows: <3 letters profile> - <the clause number> - <2 digit number - incremental>. The profile is identified as follows: GEN: Requirements generally applicable to certificate profiles. NAT: Requirements specifically applicable to profiles for certificates issued to natural persons. LEG: Requirements specifically applicable to profiles for certificates issued to legal persons. WEB: Requirements specifically applicable to profiles for certificates issued for specifically for website authentication. NOTE: Such requirements can override requirements for the above classes of profiles. QCS: Requirements specifically applicable to profiles for certificates using qualified certificates statements and EU Qualified Certificates. The management of the requirement identifiers for subsequent editions of the present document is as follows: When a requirement is inserted at the end of a clause, the 2 digit number above is incremented to the next available digit. When a requirement is inserted between two existing requirements, capital letters appended to the previous requirement identifier are used to distinguish new requirements. The requirement identifier for a deleted requirement is left and completed with \"Void\". The requirement identifier for a modified requirement is left void and the modified requirement is identified by capital letter(s) appended to the initial requirement number.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 4.1 (General approach)",
        "testo": "Tutti i profili di certificato specificati in ETSI EN 319 412 (parti 2, 3, 4, 5 e la presente parte 1) si basano su IETF RFC 5280 per la profilatura generica della Raccomandazione ITU-T X.509 | ISO/IEC 9594-8. I profili specificano sia i certificati qualificati UE sia i certificati non qualificati, ove pertinente; per i requisiti relativi ai QCStatement si rinvia a ETSI EN 319 412-5.",
        "testo_integrale": "4.1 General approach: All the certificate profiles specified in ETSI EN 319 412 (parts 2 [i.4], 3 [i.5], 4 [i.6], 5 [i.7] and the present document) are based upon IETF RFC 5280 [i.11] for generic profiling of Recommendation ITU-T X.509 | ISO/IEC 9594-8 [i.3]. The certificate profiles specify profiles for both EU Qualified Certificates and non-qualified certificates as relevant. Reference is made to ETSI EN 319 412-5 [i.7] for requirements relating to QCStatements.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 4.2.1 (Overview of ETSI EN 319 412-2)",
        "testo": "ETSI EN 319 412-2 specifica i requisiti sul contenuto dei certificati emessi a persone fisiche dai TSP, per facilitare l'interoperabilità di certificati usati per firme digitali, autenticazione peer-to-peer, autenticazione dei dati e riservatezza dei dati; specifica un profilo sia per i certificati qualificati UE (Reg. 910/2014) sia per i certificati non qualificati, rinviando a ETSI EN 319 412-5 per i QCStatement quando emessi come certificati qualificati UE.",
        "testo_integrale": "4.2.1 ETSI EN 319 412-2: Electronic Signatures and Trust Infrastructures (ESI); Certificate Profiles; Part 2: Certificate profile for certificates issued to natural persons. Scope: This part specifies the requirements on certificate content for TSPs issuing certificates to natural persons. It provides a certificate profile, which facilitates interoperability of certificates issued to natural persons for the purposes of supporting digital signatures, peer entity authentication, data authentication as well as data confidentiality. It specifies a profile for both EU Qualified Certificates as specified in Regulation (EU) No 910/2014 [i.9], and non-qualified certificates. When certificates for natural persons are issued as EU Qualified Certificates, it makes reference to ETSI EN 319 412-5 [i.7] for requirements relating to QCStatements.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 4.2.2 (Overview of ETSI EN 319 412-3)",
        "testo": "ETSI EN 319 412-3 specifica i requisiti sul contenuto dei certificati emessi a persone giuridiche dai TSP, per facilitare l'interoperabilità di certificati usati per firme digitali, autenticazione peer-to-peer, autenticazione dei dati e riservatezza dei dati; specifica un profilo sia per i certificati qualificati UE sia per i certificati non qualificati, rinviando a ETSI EN 319 412-5 per i QCStatement quando emessi come certificati qualificati UE.",
        "testo_integrale": "4.2.2 ETSI EN 319 412-3: Electronic Signatures and Infrastructures (ESI); Certificate Profiles; Part 3: Certificate profile for certificates issued to legal persons. Scope: This part specifies the requirements on certificate content for TSPs issuing certificates to legal persons. It provides a certificate profile, which facilitates interoperability of certificates issued to legal persons for the purposes of supporting digital signatures, peer entity authentication, data authentication as well as data confidentiality. It specifies a profile for both EU Qualified Certificates and non-qualified certificates. When certificates for legal persons are issued as EU Qualified Certificates, it makes reference to ETSI EN 319 412-5 [i.7] for requirements relating to QCStatements.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 4.2.3 (Overview of ETSI EN 319 412-4)",
        "testo": "ETSI EN 319 412-4 specifica i requisiti sul contenuto dei certificati per siti web accessibili via TLS (IETF RFC 5246), emessi dai TSP a persone fisiche o giuridiche; specifica un profilo sia per i certificati qualificati UE sia per i certificati non qualificati, rinviando a ETSI EN 319 412-5 per i QCStatement quando emessi come certificati qualificati UE.",
        "testo_integrale": "4.2.3 ETSI EN 319 412-4: Electronic Signatures and Trust Infrastructures (ESI); Certificate Profiles; Part 4: Certificate profile for web site certificates. Scope: This part specifies the requirements on certificate content for TSPs issuing website certificates for sites that are accessed via the TLS protocol as specified in IETF RFC 5246 [i.8]. It provides a certificate profile, which enables interoperability of website certificates issued to legal or natural persons. It specifies a profile for both EU Qualified Certificates and non-qualified certificates. When certificates for web site authentication are issued as EU Qualified Certificates, it makes reference to ETSI EN 319 412-5 [i.7] for requirements relating to QCStatements.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 4.2.4 (Overview of ETSI EN 319 412-5)",
        "testo": "ETSI EN 319 412-5 specifica i requisiti sui QCStatement richiesti per i certificati qualificati di cui alle parti 2-4; i QCStatement della clausola 4.3 sono applicabili anche fuori dall'UE, mentre gli altri requisiti della clausola 4 sono specifici del Regolamento (UE) 910/2014 ma possono essere adattati ad altri contesti regolatori.",
        "testo_integrale": "4.2.4 ETSI EN 319 412-5: Electronic Signatures and Trust Infrastructures (ESI); Certificate Profiles; Part 5: QCStatements. Scope: This part specifies the requirements on the QCStatements as required for qualified certificates as specified in parts 2 to 4 [i.4], [i.5] and [i.6] of ETSI EN 319 412. The QCStatements defined in clause 4.3 of ETSI EN 319 412-5 [i.7] can be applied to regulatory environments outside the EU. Other requirements specified in clause 4 of [i.7] are specific to Regulation (EU) No 910/2014 [i.9] but may be adapted for other regulatory environments.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 5.1.1 (General)",
        "testo": "I nomi subject e issuer possono includere attributi (es. serialNumber, organizationIdentifier) che non ne rivelano la semantica; IETF RFC 3739 clausola 3.2.6.1 definisce lo statement \"qcStatement-2\" (SemanticsInformation), che fornisce informazioni sulla semantica dei dati negli attributi/nomi del certificato. Gli identificatori di semantica delle clausole seguenti usano codici paese ISO 3166-1 alpha-2. Il meccanismo di semantica riguarda solo gli attributi del campo subject, non del campo issuer; per gli attributi issuer occorre consultare il certificato CA emittente, coerente col requisito di path validation di IETF RFC 5280.",
        "testo_integrale": "5.1.1 General: Subject and issuer names (Recommendation ITU-T X.509 | ISO/IEC 9594-8 [i.3]) can include attributes that do not disclose the semantics of its information content. serialNumber (Recommendation ITU-T X.509 | ISO/IEC 9594-8 [i.3]) and organizationIdentifier (Recommendation ITU-T X.520 [i.10]) are examples of such attributes. The serialNumber attribute can contain a national identification number, passport number or any type of locally defined identifier such as random or pseudo-random generated identifier. The organizationIdentifier attribute can contain several types of organizational identifiers. IETF RFC 3739 [1], clause 3.2.6.1 defines the predefined statement \"qcStatement-2\" identified by the OID id-qcs-pkixQCSyntax-v2 with the SemanticsInformation syntax. The SemanticsInformation type, when present, provides information about the semantics of data stored in attributes and/or names in the certificate. The semantics identifiers in the following clauses use 2 character ISO 3166-1 [2] country codes (Alpha-2) to specify the country where the identifier is registered. NOTE: The semantics identifiers in the following clauses define semantics information for attributes stored in the subject field. No corresponding mechanism is defined in the present document for specifying semantics information for attributes in the issuer field. IETF RFC 5280 [i.11] path validation requires the issuer field to be consistent with the subject field of the CA certificate assigned to the issuing CA. Name attributes of the issuing CA can be constructed according the semantics identifier defined in the following clauses and stored in the subject field of the CA certificate. In such case, the appropriate place to include semantics identifiers for these attributes is in the CA certificate. Consequently, a relying party will have to consult information in the issuing CA certificate to obtain semantics information about attributes in the issuer field of a certificate.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: GEN-5.1.1-01",
        "testo": "I codici paese transnazionali di ISO 3166-1 possono essere usati quando rilevante, come EU (Unione Europea) e UN (Nazioni Unite).",
        "testo_integrale": "GEN-5.1.1-01: Trans-national country codes as specified in ISO 3166-1 [2] may be used when relevant such as EU (European Union) and UN (United Nations).",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: GEN-5.1.1-02",
        "testo": "Il codice paese definito dall'utente 'XG' può essere usato per identificatori assegnati nell'ambito di uno schema globale.",
        "testo_integrale": "GEN-5.1.1-02: User-defined country code 'XG' may be used for identifiers allocated under a global scheme.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 5.2.1 (Validity Assured General)",
        "testo": "Le estensioni di certificato descritte nella presente clausola indicano che l'emittente garantisce la validità del certificato al momento dell'uso della relativa chiave privata. Se presente, il relying party può decidere di non verificare lo stato di revoca del certificato (es. in fase di validazione di una firma digitale); la parte superiore del percorso di certificazione non è impattata dalla presenza dell'estensione e va validata secondo le proprie regole (es. OCSP o CRL). Il presente documento definisce una sola estensione di questo tipo.",
        "testo_integrale": "5.2.1 Validity Assured General: The following certificate extensions indicate that the certificate issuer ensures that the validity of the certificate is assured at time of use of the corresponding private key. NOTE 1: Upon presence of such statement in the certificate, the relying party can decide not to check the certificate revocation status, for example, when validating a digital signature. NOTE 2: The upper part of the certificate path is not impacted by the presence of the extension in a certain certificate; upper certificates in the chain are to be validated as expressed by the certificate and/or the certificate policy/certificate practice statement (e.g. they can be validated with OCSP or CRL). NOTE 3: In the present document only one extension is defined.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 5.2.2 (Validity Assured - Short Term)",
        "testo": "L'estensione indica che la validità del certificato è garantita perché il certificato è un \"short-term certificate\": il periodo da notBefore a notAfter è inferiore al tempo massimo per processare una richiesta di revoca come specificato dalla certificate practice statement o dalla certificate policy. Per il requisito REV-6.2.4-03A di ETSI EN 319 411-1, la validità di un \"short-term certificate\" è comunque limitata a un massimo di 24 ore.",
        "testo_integrale": "5.2.2 Validity Assured - Short Term: This extension indicates that the validity of the certificate is assured because the certificate is a \"short-term certificate\". That is, the time as indicated in the certificate attribute from notBefore through notAfter, inclusive, is shorter than the maximum time to process a revocation request as specified by the certificate practice statement or certificate policy. NOTE: Due to requirement REV-6.2.4-03A of ETSI EN 319 411-1 [i.17], the validity of a \"short-term certificate\" is limited to at most 24 hours.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Parte 1: GEN-5.1.1-03", "Parte 1: GEN-5.1.2-01",
    "Parte 1: NAT-5.1.3-01", "Parte 1: NAT-5.1.3-02", "Parte 1: NAT-5.1.3-03",
    "Parte 1: NAT-5.1.3-04", "Parte 1: NAT-5.1.3-05", "Parte 1: NAT-5.1.3-06",
    "Parte 1: NAT-5.1.3-07",
    "Parte 1: LEG-5.1.4-01", "Parte 1: LEG-5.1.4-02", "Parte 1: LEG-5.1.4-03",
    "Parte 1: LEG-5.1.4-04", "Parte 1: LEG-5.1.4-05", "Parte 1: LEG-5.1.4-06",
    "Parte 1: LEG-5.1.4-07", "Parte 1: LEG-5.1.4-08",
    "Parte 1: NAT-5.1.5-01", "Parte 1: NAT-5.1.5-02", "Parte 1: NAT-5.1.5-03",
    "Parte 1: NAT-5.1.5-04",
    "Parte 1: LEG-5.1.6-01", "Parte 1: LEG-5.1.6-02", "Parte 1: LEG-5.1.6-03",
    "Parte 1: LEG-5.1.6-04",
    "Parte 1: GEN-5.2.3-01",
    "Parte 1: clausola 1 (Scope)",
    "Parte 1: clausola 3 (definizioni, simboli, abbreviazioni, notazioni)",
    "Parte 1: clausola 4.1 (General approach)",
    "Parte 1: clausola 4.2.1 (Overview of ETSI EN 319 412-2)",
    "Parte 1: clausola 4.2.2 (Overview of ETSI EN 319 412-3)",
    "Parte 1: clausola 4.2.3 (Overview of ETSI EN 319 412-4)",
    "Parte 1: clausola 4.2.4 (Overview of ETSI EN 319 412-5)",
    "Parte 1: clausola 5.1.1 (General)",
    "Parte 1: GEN-5.1.1-01", "Parte 1: GEN-5.1.1-02",
    "Parte 1: clausola 5.2.1 (Validity Assured General)",
    "Parte 1: clausola 5.2.2 (Validity Assured - Short Term)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
