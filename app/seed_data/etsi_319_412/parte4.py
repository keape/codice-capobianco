"""ETSI EN 319 412-4 V1.4.1 (2025-06) - Electronic Signatures and Trust
Infrastructures (ESI); Certificate Profiles; Part 4: Certificate profile for
web site certificates. Fonte 7 (stessa fonte multi-parte gia' usata per la
Parte 5/QCStatements), un unico capitolo (documento tecnico di 12 pagine,
sta comodamente nel contesto di una sessione principale - nessuna
suddivisione per subagent necessaria). Testo ufficiale in
app/.source_cache/etsi_319_412/parte4_raw.txt (fetch diretto dal repository
ETSI deliver, 2026-09-23).

Modellazione (ADR-0007), stesso criterio gia' applicato alla Parte 5:

- Ogni "item di indice" di questo capitolo e' una clausola descrittiva o un
  requisito numerato del testo (es. "WEB-4.1.2-03", "clausola 1 (Scope)"),
  stesso principio "un nodo per disposizione" applicato all'unita'
  strutturale propria di questo genere di fonte.
- Front matter puramente amministrativo/bibliografico (Intellectual Property
  Rights, Foreword, Modal verbs terminology, Introduction, clausola 2
  References, Annex A informative Change history, History) NON e' modellato
  come nodo: stesso trattamento riservato alla Parte 5.
- Clausola 3 "Definition of terms, symbols, abbreviations and notations"
  (3.1 Terms, 3.2 Symbols - Void, 3.3 Abbreviations, 3.4 Notations) e'
  accorpata in un UNICO nodo Principio "definitorio": le quattro
  sottoclausole non hanno contenuto normativo/tecnico autonomo separabile
  (rinvii a ETSI EN 319 412-1 piu' una tabella di abbreviazioni proprie di
  questa parte), stesso trattamento gia' riservato alla clausola 3
  accorpata della Parte 5.
- Requisiti "shall"/"shall not" con soggetto obbligato implicito (il QTSP
  che emette il certificato) -> Obbligo, categoria_soggetto "QTSP/gestore",
  ruolo "obbligato", tipo_obbligo "tecnico/sicurezza" (sono tutti requisiti
  di profilo tecnico del certificato, stessa convenzione della Parte 5).
- Requisiti "if...then...shall"/"when...shall"/"shall apply for EU Qualified
  Certificates" -> Obbligo con condizione_applicabilita esplicita: la
  clausola 4.1.3 (NCP/QNCP-w-gen) e' interamente condizionale sul tipo di
  soggetto (persona fisica/giuridica) e sulla policy applicata - WEB-4.1.3-2
  si applica solo a persona fisica, WEB-4.1.3-3 solo a persona giuridica,
  WEB-4.1.3-4 sostituisce l'eccezione prevista dagli altri due per i campi
  coperti dalla BRG [9]; QCS-4.2-1/QCS-4.3-1 sono condizionati all'emissione
  come EU Qualified Certificate.
- Clausole facoltative con "may" -> Principio "altro" (nessun obbligo
  imposto, facolta' del QTSP), stessa convenzione della Parte 5
  (QCS-4.3.5-01, "may include").
- Clausola 1 (Scope) -> Principio "scopo/ambito di applicazione".
- QCS-4.3-1 combina una raccomandazione ("should include") con un requisito
  vincolante subordinato ("shall be consistent with", applicabile solo se
  un identificatore di policy e' stato effettivamente incluso) -> Obbligo
  con condizione_applicabilita che documenta entrambe le sfumature modali,
  perche' il nodo impone comunque un vincolo di coerenza cogente quando la
  fattispecie (identificatore incluso) si avvera - stessa logica gia'
  applicata a QCS-4.3.5-02 nella Parte 5 per i requisiti "[CONDITIONAL]".
- Il NOTE informativo collegato a WEB-4.1.1-1 (chiarimento sulla sezione
  7.1.6.4 della BRG) e' incluso nel testo_integrale dello stesso nodo:
  chiarisce esclusivamente quel requisito, non ha contenuto normativo
  autonomo separabile.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "Parte 4: WEB-4.1.1-1",
        "testo": "Per i certificati emessi secondo le certificate policy DVCP, IVCP o OVCP (definite in ETSI EN 319 411-1), tutti i campi e le estensioni del certificato devono rispettare i requisiti sui certificati sottoscrittore stabiliti nella BRG del CA/Browser Forum. Nota: secondo la sezione 7.1.6.4 della BRG, i sistemi conformi alla certificate policy per i certificati domain-validated (2.23.140.1.2.1) non possono contenere attributi relativi a persone fisiche o giuridiche.",
        "testo_integrale": "WEB-4.1.1-1: For certificates issued following the certificate policies DVCP, IVCP or OVCP, as defined in ETSI EN 319 411-1 [6], all certificate fields and extensions shall comply with requirements on subscriber certificates stated in the BRG [2]. NOTE: According to BRG [2], section 7.1.6.4 implementations systems complying to the certificate policy for domain-validated certificates 2.23.140.1.2.1 cannot contain natural person or legal person related attributes.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 4: WEB-4.1.2-1",
        "testo": "Per i certificati emessi secondo la certificate policy EVCP (definita in ETSI EN 319 411-1) o QEVCP-w (definita in ETSI EN 319 411-2), tutti i campi e le estensioni del certificato devono rispettare i requisiti sui certificati sottoscrittore stabiliti nelle EVCG del CA/Browser Forum, con le modifiche specificate nelle clausole 4.2 e 4.3 del presente documento per i certificati qualificati UE.",
        "testo_integrale": "WEB-4.1.2-1: For certificates issued following the certificate policies EVCP, as defined in ETSI EN 319 411-1 [6], or QEVCP-w, as defined in ETSI EN 319 411-2 [7], all certificate fields and extensions shall comply with requirements on subscriber certificates stated in the EVCG [3], with the amendments specified in clauses 4.2 and 4.3 of the present document for EU Qualified Certificates.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 4: WEB-4.1.2-3",
        "testo": "Se il certificato e' un certificato qualificato UE ed esiste un numero di registrazione appropriato noto per l'emittente, il campo issuer deve contenere l'attributo organizationIdentifier.",
        "testo_integrale": "WEB-4.1.2-3: If the certificate is EU Qualified, and an appropriate registration number is known to exist for the issuer, then the issuer field shall contain the attribute organizationIdentifier.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo ai certificati EU Qualified per i quali esiste un numero di registrazione appropriato noto per l'emittente",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.2-4",
        "testo": "Se il certificato e' un certificato qualificato UE ed esiste un numero di registrazione appropriato noto per il soggetto, il campo subject deve contenere l'attributo organizationIdentifier.",
        "testo_integrale": "WEB-4.1.2-4: If the certificate is EU Qualified, and an appropriate registration number is known to exist for the subject, then the subject field shall contain the attribute organizationIdentifier.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo ai certificati EU Qualified per i quali esiste un numero di registrazione appropriato noto per il soggetto",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.2-5",
        "testo": "Se presente, l'organizationIdentifier dell'emittente e del soggetto deve avere un valore diverso dall'organizationName.",
        "testo_integrale": "WEB-4.1.2-5: If present, the issuer and subject organizationIdentifier shall have a value different from the organizationName.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'attributo organizationIdentifier e' presente nel certificato",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.3-1",
        "testo": "Per i certificati emessi secondo le certificate policy NCP (definita in ETSI EN 319 411-1) o QNCP-w-gen (definita in ETSI EN 319 411-2), si applicano i requisiti seguenti (WEB-4.1.3-2..6).",
        "testo_integrale": "WEB-4.1.3-1: For certificates issued following the certificate policies NCP, as defined in ETSI EN 319 411-1 [6], or QNCP-w-gen, as defined in ETSI EN 319 411-2 [7], the following requirements shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 4: WEB-4.1.3-2",
        "testo": "Se il certificato e' emesso a una persona fisica, si applicano i requisiti specificati nella clausola 4 di ETSI EN 319 412-2, ad eccezione dei campi per cui si applica WEB-4.1.3-4.",
        "testo_integrale": "WEB-4.1.3-2: If the certificate is issued to a natural person the requirements specified in ETSI EN 319 412-2 [4] clause 4 shall apply with the exception of fields where WEB-4.1.3-4 applies.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo ai certificati NCP/QNCP-w-gen emessi a una persona fisica; per i campi coperti da WEB-4.1.3-4 si applica quest'ultimo requisito in luogo di ETSI EN 319 412-2 clausola 4",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.3-3",
        "testo": "Se il certificato e' emesso a una persona giuridica, si applicano i requisiti specificati nella clausola 4.2 di ETSI EN 319 412-3, ad eccezione dei campi per cui si applica WEB-4.1.3-4.",
        "testo_integrale": "WEB-4.1.3-3: If the certificate is issued to a legal person the requirements specified in ETSI EN 319 412-3 [5] clause 4.2 shall apply with the exception of fields where WEB-4.1.3-4 applies.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo ai certificati NCP/QNCP-w-gen emessi a una persona giuridica; per i campi coperti da WEB-4.1.3-4 si applica quest'ultimo requisito in luogo di ETSI EN 319 412-3 clausola 4.2",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.3-4",
        "testo": "I requisiti di profilo del certificato specificati nella BRG [9] devono applicarsi ai campi del certificato soggetto coperti dalle seguenti sotto-sezioni della BRG (la versione della BRG [9] e' quella referenziata in ETSI EN 319 411-1 per i requisiti [WEB]): a) 7.1.2.3 f) extKeyUsage; b) 7.1.4.2.1 Subject Alternative Name; c) 7.1.4.2.2 Subject Distinguished Name - commonName; d) se necessario per distinguere il sito web identificato dal nome del soggetto, il commonName del soggetto puo' contenere un domain name o un Wildcard Domain Name (come definito nella BRG) che sia uno dei valori dNSName dell'estensione subjectAltName di un certificato di autenticazione di sito web.",
        "testo_integrale": "WEB-4.1.3-4: The following certificate profile requirements specified in the BRG [9] shall apply for subject certificate fields addressed by the following sub-sections of BRG [9] (the version of BRG [9] shall be as referenced in ETSI EN 319 411-1 [6] for [WEB] requirements): a) 7.1.2.3 f) extKeyUsage. b) 7.1.4.2.1 Subject Alternative Name. c) 7.1.4.2.2 Subject Distinguished Name - commonName. d) If necessary to distinguish the website identified by the subject name, the subject commonName may contain a domain name or a Wildcard Domain Name (as defined in BRG [9]) which is one of the dNSName values of the subjectAltName extension of a website authentication certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica in sostituzione dell'eccezione prevista da WEB-4.1.3-2/WEB-4.1.3-3, ai soli campi del certificato soggetto coperti dalle sotto-sezioni elencate della BRG [9]",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.3-5",
        "testo": "Le modifiche specificate nelle clausole 4.2 e 4.3 del presente documento devono applicarsi ai certificati qualificati UE.",
        "testo_integrale": "WEB-4.1.3-5: The amendments specified in clauses 4.2 and 4.3 of the present document shall apply for EU Qualified Certificates.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo ai certificati EU Qualified emessi secondo le policy NCP o QNCP-w-gen",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.4-1",
        "testo": "Per i certificati emessi secondo la certificate policy QNCP-w (definita in ETSI EN 319 411-2), tutti i campi e le estensioni del certificato devono rispettare i requisiti sui certificati sottoscrittore stabiliti nella BRG del CA/Browser Forum.",
        "testo_integrale": "WEB-4.1.4-1: For certificates issued following the certificate policies QNCP-w, as defined in ETSI EN 319 411-2 [7], all certificate fields and extensions shall comply with requirements on subscriber certificates stated in the BRG [2].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 4: WEB-4.1.4-4",
        "testo": "Le modifiche specificate nelle clausole 4.2 e 4.3 del presente documento devono applicarsi ai certificati qualificati UE.",
        "testo_integrale": "WEB-4.1.4-4: The amendments specified in clauses 4.2 and 4.3 of the present document shall apply for EU Qualified Certificates.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo ai certificati EU Qualified emessi secondo la policy QNCP-w",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.4-5",
        "testo": "Se esiste un numero di registrazione appropriato noto per l'emittente, e l'emittente e' una persona giuridica, il campo issuer deve contenere organizationIdentifier.",
        "testo_integrale": "WEB-4.1.4-5: If an appropriate registration number is known to exist for the issuer, and the issuer is a legal person, then the issuer field shall contain organizationIdentifier.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se esiste un numero di registrazione appropriato noto per l'emittente e l'emittente e' una persona giuridica",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.4-6",
        "testo": "Se esiste un numero di registrazione appropriato noto per il soggetto, e il soggetto e' una persona giuridica, il campo subject deve contenere organizationIdentifier.",
        "testo_integrale": "WEB-4.1.4-6: If an appropriate registration number is known to exist for the subject, and the subject is a legal person, then the subject field shall contain organizationIdentifier.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se esiste un numero di registrazione appropriato noto per il soggetto e il soggetto e' una persona giuridica",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.4-7",
        "testo": "Se presente, l'organizationIdentifier dell'emittente e del soggetto deve avere un valore diverso dall'organization name.",
        "testo_integrale": "WEB-4.1.4-7: If present, the issuer and subject organizationIdentifier shall have a value different from the organization name.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo se l'attributo organizationIdentifier e' presente nel certificato",
    },
    {
        "riferimento": "Parte 4: QCS-4.2-1",
        "testo": "Quando i certificati sono emessi come certificati qualificati UE, devono includere QCStatement come specificato nelle clausole 4 e 5 di ETSI EN 319 412-5.",
        "testo_integrale": "QCS-4.2-1: When certificates are issued as EU Qualified Certificates, they shall include QCStatements as specified in clauses 4 and 5 of ETSI EN 319 412-5 [1].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "si applica solo ai certificati emessi come EU Qualified Certificate",
    },
    {
        "riferimento": "Parte 4: QCS-4.3-1",
        "testo": "Quando i certificati sono emessi come certificati qualificati UE, dovrebbero includere, nell'estensione certificate policies, uno degli identificatori di policy del certificato definiti nella clausola 5.3 di ETSI EN 319 411-2. Gli identificatori di policy inclusi nell'estensione certificate policies dei certificati qualificati UE devono essere coerenti con le EU Qualified Certificate Statement di cui alla clausola 4.2.",
        "testo_integrale": "QCS-4.3-1: When the certificates are issued as EU Qualified Certificates, they should include, in the certificate policies extension, one of the certificate policy identifiers defined in clause 5.3 of ETSI EN 319 411-2 [7]. Policy identifiers included in the certificate policies extension of EU Qualified Certificates shall be consistent with the EU Qualified Certificate Statements according to clause 4.2.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "raccomandazione (should) applicabile solo ai certificati EU Qualified; ove vengano effettivamente inclusi identificatori di policy nell'estensione certificate policies, questi devono (shall) essere coerenti con le QCStatement dichiarate secondo la clausola 4.2",
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "Parte 4: clausola 1 (Scope)",
        "testo": "Il documento definisce un profilo di certificato per i certificati di siti web (website certificates) acceduti tramite il protocollo TLS. Il profilo si basa sui Baseline Requirements e sulle Extended Validation Guidelines del CA/Browser Forum e sulle altre parti del presente deliverable multi-parte. Il documento si concentra sui requisiti relativi al contenuto del certificato; i requisiti di decodifica ed elaborazione sono limitati agli aspetti necessari a elaborare tale contenuto e sono specificati solo quando aggiungono informazioni necessarie all'interoperabilita'. Il profilo puo' essere usato sia per persone giuridiche sia per persone fisiche: per i certificati emessi a persone giuridiche il profilo si basa sull'EV Profile o sui Baseline Requirements del CA/Browser Forum; per i certificati emessi a persone fisiche il profilo si basa solo sui Baseline Requirements.",
        "testo_integrale": "1 Scope: The present document specifies a certificate profile for web site certificates that are accessed by the TLS protocol [i.1]. The profile defined in the present document builds on the CA/Browser Forum Baseline requirements [2], Extended validation guidelines [3] and other parts of the present multi-part deliverable. The present document focuses on requirements on certificate content. Requirements on decoding and processing rules are limited to aspects required to process certificate content defined in the present document. Further processing requirements are only specified for cases where it adds information that is necessary for the sake of interoperability. This profile can be used for legal and natural persons. For certificates issued to legal persons, the profile builds on the CA/Browser Forum EV Profile [3] or baseline requirements [2]. For certificates issued to natural persons, the profile builds only on CA/Browser Forum baseline requirements [2].",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 4: clausola 3 (Definition of terms, symbols, abbreviations and notations)",
        "testo": "Per i termini si rinvia a ETSI EN 319 412-1. La sottoclausola sui simboli e' vuota (Void). Elenca le abbreviazioni proprie di questa parte: BRG (Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates), DVCP (Domain Validation Certificate Policy), EVCG (Extended Validation Certificate Guidelines), EVCP (Extended Validation Certificate Policy), IVCP (Individual Validation Certificate Policy), NCP (Normalized Certificate Policy), OVCP (Organizational Validation Certificate Policy), QEVCP-w (policy per certificato di sito web qualificato UE emesso a persona giuridica basata sulle EVCG), QNCP-w (policy per certificato di sito web qualificato UE emesso a persona fisica o giuridica basata sulla BRG), QNCP-w-gen (policy per certificato di sito web qualificato UE emesso a persona fisica o giuridica basata su requisiti selezionati della BRG), TLS (Transport Layer Security). Per le notazioni si rinvia a ETSI EN 319 412-1.",
        "testo_integrale": "3 Definition of terms, symbols, abbreviations and notations. 3.1 Terms: For the purposes of the present document, the terms given in ETSI EN 319 412-1 [i.5] apply. 3.2 Symbols: Void. 3.3 Abbreviations: For the purposes of the present document, the abbreviations given in ETSI EN 319 412-1 [i.5] and the following apply: BRG Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates [2]. DVCP Domain Validation Certificate Policy. EVCG Extended Validation Certificate Guidelines. EVCP Extended Validation Certificate Policy. IVCP Individual Validation Certificate Policy. NCP Normalized Certificate Policy. OVCP Organizational Validation Certificate Policy. QEVCP-w Policy for EU qualified website certificate issued to a legal person and linking the website to that person based on the EVCG [3]. QNCP-w Policy for EU qualified website certificate issued to a natural or a legal person and linking the website to that person based on the BRG [2]. QNCP-w-gen Policy for EU qualified website certificate issued to a natural or a legal person and linking the website to that person based on selected requirements in BRG [9]. TLS Transport Layer Security. 3.4 Notations: For the purposes of the present document, the notations given in ETSI EN 319 412-1 [i.5] apply.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.1-2",
        "testo": "I certificati conformi a IVCP o OVCP possono includere uno o piu' identificatori di semantica, come specificato nella clausola 5 di ETSI EN 319 412-1, per fornire definizioni semantiche rilevanti a determinare l'identita' del soggetto del certificato.",
        "testo_integrale": "WEB-4.1.1-2: Certificates following IVCP or OVCP may include one or more semantics identifiers as specified in clause 5 of ETSI EN 319 412-1 [i.5] to provide relevant semantics definitions to determine the identity of the subject of the certificate.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.2-2",
        "testo": "I certificati possono includere uno o piu' identificatori di semantica, come specificato nella clausola 5 di ETSI EN 319 412-1, per fornire definizioni semantiche rilevanti a determinare l'identita' del soggetto del certificato.",
        "testo_integrale": "WEB-4.1.2-2: Certificates may include one or more semantics identifiers as specified in clause 5 of ETSI EN 319 412-1 [i.5] to provide relevant semantics definitions to determine the identity of the subject of the certificate.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.2-6",
        "testo": "I certificati possono includere un identificatore di semantica per persona giuridica, come specificato nella clausola 5.1.4 di ETSI EN 319 412-1.",
        "testo_integrale": "WEB-4.1.2-6: Certificates may include a legal person semantic identifier as specified in clause 5.1.4 of ETSI EN 319 412-1 [i.5].",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.3-6",
        "testo": "I certificati possono includere uno o piu' identificatori di semantica, come specificato nella clausola 5 di ETSI EN 319 412-1, per fornire definizioni semantiche rilevanti a determinare l'identita' del soggetto del certificato.",
        "testo_integrale": "WEB-4.1.3-6: Certificates may include one or more semantics identifiers as specified in clause 5 of ETSI EN 319 412-1 [i.5] to provide relevant semantics definitions to determine the identity of the subject of the certificate.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.4-2",
        "testo": "Se necessario per distinguere il sito web identificato dal nome del soggetto, il commonName del soggetto puo' contenere un domain name o un Wildcard Domain Name (come definito nella BRG) che sia uno dei valori dNSName dell'estensione subjectAltName di un certificato di autenticazione di sito web.",
        "testo_integrale": "WEB-4.1.4-2: If necessary to distinguish the website identified by the subject name, the subject commonName may contain a domain name or a Wildcard Domain Name (as defined in BRG [2]) which is one of the dNSName values of the subjectAltName extension of a website authentication certificate.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.4-3",
        "testo": "I certificati conformi a QNCP-w possono includere uno o piu' identificatori di semantica, come specificato nella clausola 5 di ETSI EN 319 412-1, per fornire definizioni semantiche rilevanti a determinare l'identita' del soggetto del certificato.",
        "testo_integrale": "WEB-4.1.4-3: Certificates following QNCP-w may include one or more semantics identifiers as specified in clause 5 of ETSI EN 319 412-1 [i.5] to provide relevant semantics definitions to determine the identity of the subject of the certificate.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 4: WEB-4.1.4-8",
        "testo": "I certificati possono includere un identificatore di semantica per persona giuridica, come specificato nella clausola 5.1.4 di ETSI EN 319 412-1.",
        "testo_integrale": "WEB-4.1.4-8: Certificates may include a legal person semantic identifier as specified in clause 5.1.4 of ETSI EN 319 412-1 [i.5].",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Parte 4: clausola 1 (Scope)",
    "Parte 4: clausola 3 (Definition of terms, symbols, abbreviations and notations)",
    "Parte 4: WEB-4.1.1-1", "Parte 4: WEB-4.1.1-2",
    "Parte 4: WEB-4.1.2-1", "Parte 4: WEB-4.1.2-2", "Parte 4: WEB-4.1.2-3",
    "Parte 4: WEB-4.1.2-4", "Parte 4: WEB-4.1.2-5", "Parte 4: WEB-4.1.2-6",
    "Parte 4: WEB-4.1.3-1", "Parte 4: WEB-4.1.3-2", "Parte 4: WEB-4.1.3-3",
    "Parte 4: WEB-4.1.3-4", "Parte 4: WEB-4.1.3-5", "Parte 4: WEB-4.1.3-6",
    "Parte 4: WEB-4.1.4-1", "Parte 4: WEB-4.1.4-2", "Parte 4: WEB-4.1.4-3",
    "Parte 4: WEB-4.1.4-4", "Parte 4: WEB-4.1.4-5", "Parte 4: WEB-4.1.4-6",
    "Parte 4: WEB-4.1.4-7", "Parte 4: WEB-4.1.4-8",
    "Parte 4: QCS-4.2-1", "Parte 4: QCS-4.3-1",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
