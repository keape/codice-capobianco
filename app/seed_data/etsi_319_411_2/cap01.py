"""Estrazione granulare ETSI EN 319 411-2 V2.6.1 (2025-06) — "Electronic
Signatures and Trust Infrastructures (ESI); Policy and security requirements
for Trust Service Providers issuing certificates; Part 2: Requirements for
trust service providers issuing EU qualified certificates". Fonte 18
(assegnata dalla sessione principale — questo modulo NON tocca seed.py),
capitolo 1: clausole 1 (Scope), 2 (References: 2.1 normative, 2.2
informative), 3 (Definition of terms, symbols, abbreviations and notations)
e 4 (General concepts: 4.1, 4.2 con 4.2.1/4.2.2/4.2.3, 4.3). Testo ufficiale
in app/.source_cache/etsi_319_411_2/cap01.txt.

Modellazione (ADR-0007). ETSI EN 319 411-2 è costruita "sopra" ETSI EN 319
411-1 (Fonte 17, estratta in parallelo da un sibling subagent): quasi ogni
sottoclausola di questo capitolo 1 non ripete i requisiti generali ma rinvia
esplicitamente a una clausola di EN 319 411-1 ("ETSI EN 319 411-1 [2],
clause X applies"/"apply"). Per vincolo di fase ogni rinvio è comunque
censito come proprio nodo con il testo di rimando riportato verbatim, ma
SENZA creare relazione verso Fonte 17 (RELAZIONI resta vuoto in questo
capitolo, sia interne sia cross-fonte — verranno costruite nella pipeline
dedicata di collegamento cross-fonte, ADR-0009, in sessione principale).

Un solo tipo di nodo in questo capitolo — Principio — perché nessuna
sottoclausola di 1-4.3 porta un identificatore di requisito in formato
<3 lettere>-<clausola>-<NN> (quello schema, definito proprio in clausola
3.4 di questo capitolo, si applica solo dalla clausola 5 in poi, coperta
dagli altri capitoli di questa fonte). RIGHE_OBBLIGHI resta quindi vuoto.

Dettaglio per clausola:

- Clausola 1 (Scope) -> Principio "scopo/ambito di applicazione". Include
  la NOTE (rimando a ETSI EN 319 403 [i.6] per la valutazione di
  conformità) perché delimita esplicitamente cosa il documento NON
  specifica (i requisiti per gli organismi di valutazione), non è mero
  rimando bibliografico.
- Clausola 2 (References) -> 2 Principi distinti "altro" (2.1 normative,
  2.2 informative), come da istruzione esplicita di questo batch (diverge
  dal precedente applicato a ETSI TS 119 461/ETSI EN 319 401, dove la
  clausola References non genera alcun nodo — qui il criterio di
  assegnazione la include esplicitamente nell'elenco delle clausole di
  cornice da censire come Principio). Per ciascuna, la NOTE generica sui
  link ipertestuali ("hyperlinks... valid at the time of publication") è
  omessa per puro contenuto di disclaimer senza valore interpretativo,
  riscritta come se non ci fosse (nessun marcatore di elisione, ADR-0010);
  le due NOTE su [i.3]/[i.7] in 2.2 sono invece mantenute perché
  disambiguano quale versione di un documento esterno non versionato
  (BRG/EVCG del CA/Browser Forum) si applica — contenuto interpretativo
  sostanziale, non bibliografia pura.
- Clausola 3.1 (Terms) -> Principio "definitorio" (2 termini: EU Qualified
  Certificate, QSCD).
- Clausola 3.2 (Symbols) -> NESSUN nodo: il testo è integralmente "Void."
  senza alcun contenuto oltre il rimando strutturale, stesso criterio già
  applicato alla clausola 3.2 di ETSI TS 119 461 (Fonte 9,
  app/seed_data/etsi_119_461/cap01.py) — non genera un item di indice.
- Clausola 3.3 (Abbreviations) -> Principio "definitorio" (7 sigle QCP-l,
  QCP-l-qscd, QCP-n, QCP-n-qscd, QEVCP-w, QNCP-w, QNCP-w-gen, più QSCD).
  Il testo ufficiale arriva come un unico blocco piatto senza separatori
  espliciti tra sigla e definizione (artefatto di conversione PDF->testo);
  ricostruito con ": " tra sigla e definizione e "." di chiusura per
  leggibilità, nessuna parola aggiunta/rimossa. NOTE su QEVCP-w (le
  versioni precedenti usavano "QCP-w") mantenuta: chiarimento storico
  sostanziale sulla sigla.
- Clausola 3.4 (Notations) -> Principio "definitorio". Nodo cruciale:
  riporta la legenda completa e verbatim dei prefissi dei requisiti
  (formato <3 lettere>-<clausola>-<NN>, marcature "[CONDITIONAL]"/
  "[CHOICE]"/indicatori di certificate policy, le 7 famiglie di componente
  di servizio OVR/GEN/REG/REV/DIS/SDP/CSS, regole di gestione tra
  edizioni), così che gli altri capitoli di questa fonte possano
  verificare per riferimento invece di ricopiare la legenda.
- Clausola 4.1 (General policy requirements concepts) -> Principio "altro"
  di puro rimando: "ETSI EN 319 411-1 [2], clause 4.1 applies." — l'intero
  contenuto normativo di questa sottoclausola in 411-2 è quel rimando.
- Clausola 4.2.1 (Certification Practice Statement) -> Principio "altro",
  stesso pattern di puro rimando a EN 319 411-1 clausola 4.2.1.
- Clausola 4.2.2 (Certificate Policy) -> la sottoclausola più densa del
  capitolo: 9 nodi Principio "altro" distinti:
  1) il paragrafo introduttivo (ha contenuto prescrittivo/definitorio
     proprio: definisce gli "EU qualified certificate policy identifiers",
     rinvia alla clausola 5.3 per la loro assegnazione, ed elenca le 5
     basi di requisiti NCP/NCP+/EVCP/OVCP-IVCP-DVCP/[WEB] su cui le policy
     qualificate sono costruite — non è solo "the following apply:");
  2)-8) le 7 policy EU qualificate enumerate 1)-7) nel testo (QCP-n,
     QCP-l, QCP-n-qscd, QCP-l-qscd, QEVCP-w, QNCP-w, QNCP-w-gen), ciascuna
     con proprio contenuto prescrittivo distinto (quali requisiti di base
     — NCP/NCP+/EVCP/ecc. — la policy incorpora), come da istruzione
     esplicita di assegnazione ("ogni policy enumerata 1)-7) è un nodo
     distinto se ha contenuto prescrittivo proprio" — tutte e 7 lo hanno);
  9) il paragrafo di chiusura ("Clause 7 specifies a framework...") è
     contenuto distinto (rinvio in avanti alla clausola 7, non specifico a
     nessuna delle 7 policy singolarmente) -> nodo a sé.
  NOTA testuale: gli item 2) e 4) del testo ufficiale (QCP-l e QCP-l-qscd)
  contengono ciascuno una frase che cita letteralmente "the requirements
  for QCP-n" dove ci si aspetterebbe "QCP-l"/"QCP-l-qscd" — refuso
  presente nel testo ufficiale ETSI, riportato verbatim in
  `testo_integrale` senza correzione (nessuna competenza per emendare il
  testo normativo in fase di estrazione), segnalato qui per trasparenza.
- Clausola 4.2.3 (Terms and conditions and PKI disclosure statement) ->
  Principio "altro", puro rimando a EN 319 411-1 clausola 4.2.3.
- Clausola 4.3 (Certification services) -> Principio "altro", rimanda alla
  scomposizione in servizi component di EN 319 411-1 clausola 4.4.

RELAZIONI: vuoto per vincolo di fase esplicito di questo batch — nessuna
relazione, né interna al capitolo né (soprattutto) cross-fonte verso Fonte
17, nonostante quasi ogni nodo di questo capitolo sia testualmente un
rimando diretto a una clausola di EN 319 411-1. Il collegamento cross-fonte
è demandato alla pipeline dedicata (ADR-0009) in sessione principale, che
avrà la vista simultanea di entrambe le fonti già inserite in Neo4j.
"""

RIGHE_OBBLIGHI: list[dict] = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "Parte 2: clausola 1 (Scope)",
        "testo": (
            "Il documento specifica requisiti di policy e sicurezza per l'emissione, il mantenimento "
            "e la gestione del ciclo di vita dei certificati qualificati UE come definiti dal "
            "regolamento (UE) n. 910/2014. Tali requisiti supportano policy di certificazione di "
            "riferimento per l'emissione, mantenimento e gestione del ciclo di vita di certificati "
            "qualificati UE rilasciati a persone fisiche (incluse quelle associate a una persona "
            "giuridica o a un sito web) e a persone giuridiche (incluse quelle associate a un sito "
            "web). Il documento non specifica come i requisiti individuati possano essere valutati da "
            "una parte indipendente, né i requisiti informativi verso tali valutatori né i requisiti "
            "sui valutatori stessi (per la valutazione di conformità dei processi/servizi del TSP si "
            "rimanda a ETSI EN 319 403). Il documento fa riferimento a ETSI EN 319 411-1 per i "
            "requisiti generali sui TSP che rilasciano certificati."
        ),
        "testo_integrale": (
            "1 Scope: The present document specifies policy and security requirements for the "
            "issuance, maintenance and life-cycle management of EU qualified certificates as defined "
            "in Regulation (EU) No 910/2014 [i.1]. These policy and security requirements support "
            "reference certificate policies for the issuance, maintenance and life-cycle management "
            "of EU qualified certificates issued to natural persons (including natural persons "
            "associated with a legal person or a website) and to legal persons (including legal "
            "persons associated with a website), respectively. The present document does not specify "
            "how the requirements identified can be assessed by an independent party, including "
            "requirements for information to be made available to such independent assessors, or "
            "requirements on such assessors. NOTE: See ETSI EN 319 403 [i.6] for guidance on "
            "assessment of TSP's processes and services. The present document references ETSI EN 319 "
            "411-1 [2] for general requirements on TSP issuing certificates."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 2.1 (Normative references)",
        "testo": (
            "Le referenze normative sono specifiche (si applica solo la versione citata) o non "
            "specifiche (si applica l'ultima versione, incluse le modifiche). I documenti "
            "referenziati necessari per l'applicazione del documento sono: [1] ETSI EN 319 401 "
            "(requisiti generali di policy per i TSP); [2] ETSI EN 319 411-1 (requisiti generali per "
            "i TSP che rilasciano certificati); [3] ETSI EN 319 412-5 (profili di certificato — "
            "QCStatements); [4] ISO/IEC 9594-8/ITU-T X.509 (framework dei certificati a chiave "
            "pubblica e di attributo); [5] ETSI EN 319 412-1 (profili di certificato — struttura dati "
            "comuni)."
        ),
        "testo_integrale": (
            "2.1 Normative references: References are either specific (identified by date of "
            "publication and/or edition number or version number) or non-specific. For specific "
            "references, only the cited version applies. For non-specific references, the latest "
            "version of the referenced document (including any amendments) applies. Referenced "
            "documents which are not found to be publicly available in the expected location might "
            "be found in the ETSI docbox. The following referenced documents are necessary for the "
            "application of the present document. [1] ETSI EN 319 401: \"Electronic Signatures and "
            "Trust Infrastructures (ESI); General Policy Requirements for Trust Service Providers\". "
            "[2] ETSI EN 319 411-1: \"Electronic Signatures and Trust Infrastructures (ESI); Policy "
            "and security requirements for trust service providers issuing certificates; Part 1: "
            "General requirements\". [3] ETSI EN 319 412-5: \"Electronic Signatures and Trust "
            "Infrastructures (ESI); Certificate Profiles; Part 5: QCStatements\". [4] ISO/IEC "
            "9594-8/Recommendation ITU-T X.509: \"Information technology — Open Systems "
            "Interconnection — Part 8: The Directory: Public-key and attribute certificate "
            "frameworks\". [5] ETSI EN 319 412-1: \"Electronic Signatures and Trust Infrastructures "
            "(ESI); Certificate Profiles; Part 1: Overview and common data structures\"."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 2.2 (Informative references)",
        "testo": (
            "Le referenze informative (non necessarie per l'applicazione del documento ma di ausilio "
            "su un'area tematica specifica) sono: [i.1] regolamento (UE) n. 910/2014 (eIDAS); [i.2] "
            "ETSI TS 101 456 (requisiti di policy per le CA che rilasciano certificati qualificati — "
            "predecessore storico); [i.3] CA/Browser Forum Baseline Requirements (versione come "
            "referenziata in ETSI EN 319 411-1); [i.4] IETF RFC 3647 (framework di certificate policy "
            "e certification practice statement X.509); [i.5] direttiva 95/46/CE (protezione dati "
            "personali); [i.6] ETSI EN 319 403 (requisiti per gli organismi di valutazione della "
            "conformità dei TSP); [i.7] CA/Browser Forum Extended Validation Guidelines (versione "
            "come referenziata in ETSI EN 319 411-1); [i.8] ETSI TS 119 612 (Trusted Lists); [i.9] "
            "IETF RFC 6960 (OCSP); [i.10] ETSI TR 119 411-4 (checklist di audit per EN 319 411-1/-2); "
            "[i.11] decisione di esecuzione (UE) 2015/1505 (specifiche tecniche delle trusted list ex "
            "art. 22(5) eIDAS); [i.12] ETSI TS 119 615 (procedure per l'uso e l'interpretazione delle "
            "trusted list nazionali); [i.13] ETSI TS 119 172-4 (regole di applicabilità delle firme/"
            "sigilli qualificati UE tramite trusted list)."
        ),
        "testo_integrale": (
            "2.2 Informative references: References are either specific (identified by date of "
            "publication and/or edition number or version number) or non-specific. For specific "
            "references, only the cited version applies. For non-specific references, the latest "
            "version of the referenced document (including any amendments) applies. The following "
            "referenced documents are not necessary for the application of the present document but "
            "they assist the user with regard to a particular subject area. [i.1] Regulation (EU) No "
            "910/2014 of the European Parliament and of the Council of 23 July 2014 on electronic "
            "identification and trust services for electronic transactions in the internal market "
            "and repealing Directive 1999/93/EC. [i.2] ETSI TS 101 456: \"Electronic Signatures and "
            "Infrastructures (ESI); Policy requirements for certification authorities issuing "
            "qualified certificates\". [i.3] CA/Browser Forum: \"Baseline Requirements for the "
            "Issuance and Management of Publicly-Trusted Certificates\". NOTE: The version is as "
            "referenced in ETSI EN 319 411-1 [2]. [i.4] IETF RFC 3647: \"Internet X.509 Public Key "
            "Infrastructure Certificate Policy and Certification Practices Framework\". [i.5] "
            "Directive 95/46/EC of the European Parliament and of the Council of 24 October 1995 on "
            "the protection of individuals with regard to the processing of personal data and on the "
            "free movement of such data. [i.6] ETSI EN 319 403: \"Electronic Signatures and "
            "Infrastructures (ESI); Trust Service Provider Conformity Assessment-Requirements for "
            "conformity assessment bodies assessing Trust Service Providers\". [i.7] CA/Browser "
            "Forum: \"Guidelines for The Issuance and Management of Extended Validation "
            "Certificates\". NOTE: The version is as referenced in ETSI EN 319 411-1 [2]. [i.8] ETSI "
            "TS 119 612: \"Electronic Signatures and Trust Infrastructures (ESI); Trusted Lists\". "
            "[i.9] IETF RFC 6960: \"Internet X.509 Public Key Infrastructure Online Certificate "
            "Status Protocol-OCSP\". [i.10] ETSI TR 119 411-4: \"Electronic Signatures and Trust "
            "Infrastructures (ESI); Policy and security requirements for Trust Service Providers "
            "issuing certificates; Part 4: Checklist supporting audit of TSP against ETSI EN 319 "
            "411-1 or ETSI EN 319 411-2\". [i.11] Commission implementing decision (EU) 2015/1505 of "
            "8 September 2015 laying down technical specifications and formats relating to trusted "
            "lists pursuant to Article 22(5) of Regulation (EU) No 910/2014 of the European "
            "Parliament and of the Council on electronic identification and trust services for "
            "electronic transactions in the internal market. [i.12] ETSI TS 119 615: \"Electronic "
            "Signatures and Infrastructures (ESI); Trusted Lists; Procedures for using and "
            "interpreting European Union Member States national trusted lists\". [i.13] ETSI TS 119 "
            "172-4: \"Electronic Signatures and Trust Infrastructures (ESI); Signature policies; Part "
            "4: Signature applicability rules (validation policy) for European qualified electronic "
            "signatures/seals using trusted lists\"."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 3.1 (Terms)",
        "testo": (
            "Ai fini del documento si applicano i termini di ETSI EN 319 401, ETSI EN 319 411-1 e del "
            "regolamento (UE) n. 910/2014, oltre ai seguenti: Certificato Qualificato UE = Certificato "
            "Qualificato come specificato nel regolamento (UE) n. 910/2014; Dispositivo Qualificato di "
            "Creazione di Firma/Sigillo Elettronico (QSCD) = come specificato nel regolamento (UE) n. "
            "910/2014."
        ),
        "testo_integrale": (
            "3.1 Terms: For the purposes of the present document, the terms given in ETSI EN 319 401 "
            "[1], ETSI EN 319 411-1 [2], Regulation (EU) No 910/2014 [i.1] and the following apply: "
            "EU Qualified Certificate: Qualified Certificate as specified in Regulation (EU) No "
            "910/2014 [i.1]. Qualified electronic Signature/Seal Creation Device (QSCD): As specified "
            "in Regulation (EU) No 910/2014 [i.1]."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 3.3 (Abbreviations)",
        "testo": (
            "Ai fini del documento si applicano le abbreviazioni di ETSI EN 319 401, ETSI EN 319 "
            "411-1 e le seguenti: QCP-l = policy per certificato qualificato UE a persona giuridica; "
            "QCP-l-qscd = QCP-l con chiave privata e certificato residenti su QSCD; QCP-n = policy per "
            "certificato qualificato UE a persona fisica; QCP-n-qscd = QCP-n con chiave privata e "
            "certificato residenti su QSCD; QEVCP-w = policy per certificato qualificato UE di sito "
            "web a persona giuridica basata sulle EVCG (le versioni precedenti del documento usavano "
            "la sigla QCP-w); QNCP-w = policy per certificato qualificato UE di sito web basata sulle "
            "BRG; QNCP-w-gen = policy per certificato qualificato UE di sito web per scopo generale; "
            "QSCD = Dispositivo Qualificato di Creazione di Firma/Sigillo Elettronico."
        ),
        "testo_integrale": (
            "3.3 Abbreviations: For the purposes of the present document, the abbreviations given in "
            "ETSI EN 319 401 [1], ETSI EN 319 411-1 [2] and the following apply: QCP-l: Policy for EU "
            "Qualified Certificate issued to a legal person. QCP-l-qscd: Policy for EU Qualified "
            "Certificate issued to a legal person where the private key and the related certificate "
            "reside on a QSCD. QCP-n: Policy for EU Qualified Certificate issued to a natural person. "
            "QCP-n-qscd: Policy for EU Qualified Certificate issued to a natural person where the "
            "private key and the related certificate reside on a QSCD. QEVCP-w: Policy for EU "
            "qualified website certificate issued to a legal person and linking the website to that "
            "person based on the EVCG. NOTE: Previous versions of the present document used the "
            "abbreviation QCP-w. QNCP-w: Policy for EU qualified website certificate issued to a "
            "natural or a legal person and linking the website to that person based on the BRG. "
            "QNCP-w-gen: Policy for EU qualified website certificate issued to a natural or a legal "
            "person and linking the website to that person, applicable for general purpose "
            "certificate for qualified website authentication. QSCD: Qualified electronic "
            "Signature/Seal Creation Device."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 3.4 (Notations)",
        "testo": (
            "Definisce la notazione dei requisiti del documento: a) requisiti applicabili a "
            "qualunque certificate policy, senza marcatura; b) requisiti applicabili in determinate "
            "condizioni, marcati \"[CONDITIONAL]\"; c) requisiti con più scelte alternative, marcati "
            "\"[CHOICE]\"; d) requisiti applicabili ai servizi offerti sotto una specifica certificate "
            "policy, marcati con l'indicatore della policy applicabile (\"[QCP-l]\", \"[QCP-n]\", "
            "\"[QCP-l-qscd]\", \"[QCP-n-qscd]\", \"[QEVCP-w]\", \"[QNCP-w]\" e/o \"[QNCP-w-gen]\"). "
            "Ogni requisito è identificato dal formato <3 lettere componente di servizio>-<numero "
            "clausola>-<numero progressivo a 2 cifre>. I componenti di servizio sono: OVR (requisito "
            "generale, applicabile a più di un componente), GEN (servizi di generazione del "
            "certificato), REG (servizi di registrazione), REV (servizi di revoca), DIS (servizi di "
            "divulgazione), SDP (provisioning del dispositivo del soggetto), CSS (servizio di stato "
            "del certificato). Regole di gestione degli identificatori tra edizioni: inserimento a "
            "fine clausola -> incremento del numero progressivo; inserimento tra due requisiti "
            "esistenti -> lettere maiuscole aggiunte all'identificatore precedente; requisito "
            "soppresso -> identificatore mantenuto e completato con \"Void\"; requisito modificato -> "
            "numero lasciato vuoto e requisito modificato identificato da lettera(e) maiuscola(e) "
            "aggiunta al numero iniziale."
        ),
        "testo_integrale": (
            "3.4 Notations: The requirements identified in the present document include: a) "
            "requirements applicable to any certificate policy. Such requirements are indicated by "
            "clauses without any additional marking; b) requirements applicable under certain "
            "conditions. Such requirements are indicated by clauses marked by \"[CONDITIONAL]\"; c) "
            "requirements that include several choices which ought to be selected according to the "
            "applicable situation. Such requirements are indicated by clauses marked by "
            "\"[CHOICE]\"; d) requirements applicable to the services offered under the applicable "
            "certificate policy. Such requirements are indicated by clauses marked by the applicable "
            "certificate policy indicator: \"[QCP-l]\", \"[QCP-n]\", \"[QCP-l-qscd]\", "
            "\"[QCP-n-qscd]\", \"[QEVCP-w]\", \"[QNCP-w]\" and/or \"[QNCP-w-gen]\". Each requirement "
            "is identified as follows: <3 letters service component>-<the clause number>-<2 digit "
            "number – incremental>. The service components are: OVR: General requirement "
            "(requirement applicable to more than 1 component); GEN: Certificate Generation "
            "Services; REG: Registration Services; REV: Revocation Services; DIS: Dissemination "
            "Services; SDP: Subject Device Provisioning; CSS: Certificate Status Service. The "
            "management of the requirement identifiers throughout subsequent editions of the present "
            "document is as follows: when a requirement is inserted at the end of a clause, the 2 "
            "digit number above is incremented to the next available digit; when a requirement is "
            "inserted between two existing requirements, capital letters appended to the previous "
            "requirement identifier are used to distinguish new requirements; the requirement "
            "identifier for a deleted requirement is left and completed with \"Void\"; the "
            "requirement identifier for a modified requirement is left void and the modified "
            "requirement is identified by capital letter(s) appended to the initial requirement "
            "number."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 4.1 (General policy requirements concepts)",
        "testo": "Si applica la clausola 4.1 di ETSI EN 319 411-1 (concetti generali di policy).",
        "testo_integrale": (
            "4.1 General policy requirements concepts: ETSI EN 319 411-1 [2], clause 4.1 applies."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 4.2.1 (Certification Practice Statement)",
        "testo": (
            "Si applicano le spiegazioni della clausola 4.2.1 di ETSI EN 319 411-1 sulla "
            "Certification Practice Statement."
        ),
        "testo_integrale": (
            "4.2.1 Certification Practice Statement: The explanations identified in ETSI EN 319 "
            "411-1 [2], clause 4.2.1 apply."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 4.2.2 (Certificate Policy — introduzione)",
        "testo": (
            "Il documento definisce un certo numero di certificate policy e assegna a ciascuna un "
            "identificatore di policy, detto \"identificatore di policy per certificati qualificati "
            "UE\" (definiti in clausola 5.3). Le certificate policy sono basate sui seguenti requisiti "
            "di policy specificati in ETSI EN 319 411-1: requisiti della Normalized Certificate "
            "Policy (NCP); requisiti della enhanced Normalized Certificate Policy (NCP+); requisiti "
            "della Extended Validation Certificate Policy (EVCP); requisiti della Organizational "
            "Validation Certificate Policy (OVCP), della Individual Validation Certificate Policy "
            "(IVCP) e della Domain Validation Certificate Policy (DVCP); requisiti comuni ai "
            "certificati di autenticazione web per scopo generale, contrassegnati [WEB] (alcune "
            "relying party, ad es. i produttori di browser, possono richiedere anche la piena "
            "conformità ai Baseline Requirements o alle Extended Validation Guidelines del CA/"
            "Browser Forum o ad altri requisiti di policy)."
        ),
        "testo_integrale": (
            "4.2.2 Certificate Policy: The present document defines a number of certificate policies "
            "and allocates a policy identifier for each of them. These policy identifiers are called "
            "\"EU qualified certificate policy identifiers\"; they are defined in clause 5.3. The "
            "certificate policies are based on the following policy requirements specified in ETSI "
            "EN 319 411-1 [2]: - Requirements of the Normalized Certificate Policy (NCP). - "
            "Requirements of the enhanced Normalized Certificate Policy (NCP+). - Requirements of the "
            "Extended Validation Certificate Policy (EVCP). - Requirements of the Organizational "
            "Validation Certificate Policy (OVCP), the Individual Validation Certificate Policy "
            "(IVCP) and the Domain Validation Certificate Policy (DVCP). - Requirements common to "
            "web-authentication certificates for general purpose tagged [WEB]. NOTE: Some relying "
            "parties (e.g. vendors of Internet browser software) may also require conformance to the "
            "entirety of CA/Browser Forum Baseline Requirements or Extended Validation Guidelines or "
            "other policy requirements. The EU qualified certificate policies are:"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 4.2.2, policy 1) (QCP-n)",
        "testo": (
            "Policy per certificati qualificati UE rilasciati a persone fisiche (QCP-n), al livello "
            "di qualità del regolamento (UE) n. 910/2014: i requisiti includono tutti quelli della "
            "NCP più requisiti aggiuntivi per l'emissione e gestione dei certificati qualificati UE; "
            "se l'implementazione del TSP richiede un dispositivo crittografico sicuro, includono "
            "invece tutti i requisiti NCP+ più i requisiti aggiuntivi."
        ),
        "testo_integrale": (
            "1) A policy for EU qualified certificates issued to natural persons (QCP-n) offering the "
            "level of quality defined in Regulation (EU) No 910/2014 [i.1] for EU qualified "
            "certificates: - The requirements for QCP-n include all the NCP policy requirements, plus "
            "additional requirements suited to support EU qualified certificates issuance and "
            "management as specified in Regulation (EU) No 910/2014 [i.1]. - If the TSP's "
            "implementation of this policy requires a secure cryptographic device, the requirements "
            "for QCP-n include all the NCP+ requirements, plus the additional requirements suited to "
            "support EU qualified certificates issuance and management as specified in Regulation "
            "(EU) No 910/2014 [i.1]."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 4.2.2, policy 2) (QCP-l)",
        "testo": (
            "Policy per certificati qualificati UE rilasciati a persone giuridiche (QCP-l), al "
            "livello di qualità del regolamento (UE) n. 910/2014: i requisiti includono tutti quelli "
            "della NCP più requisiti aggiuntivi; se l'implementazione del TSP richiede un dispositivo "
            "crittografico sicuro, includono invece tutti i requisiti NCP+ più i requisiti aggiuntivi "
            "(il testo ufficiale riporta qui letteralmente \"requirements for QCP-n\", refuso rispetto "
            "a QCP-l, riportato verbatim in testo_integrale)."
        ),
        "testo_integrale": (
            "2) A policy for EU qualified certificates issued to legal persons (QCP-l) offering the "
            "level of quality defined in Regulation (EU) No 910/2014 [i.1] for EU qualified "
            "certificates: - The requirements for QCP-l include all the NCP policy requirements, plus "
            "additional requirements suited to support EU qualified certificates issuance and "
            "management as specified in Regulation (EU) No 910/2014 [i.1]. - If the TSP's "
            "implementation of this policy requires a secure cryptographic device, the requirements "
            "for QCP-n include all the NCP+ requirements, plus the additional requirements suited to "
            "support EU qualified certificates issuance and management as specified in Regulation "
            "(EU) No 910/2014 [i.1]."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 4.2.2, policy 3) (QCP-n-qscd)",
        "testo": (
            "Policy per certificati qualificati UE rilasciati a persone fisiche (QCP-n-qscd), al "
            "livello di qualità del regolamento (UE) n. 910/2014 e che richiede l'uso di un "
            "Qualified Signature Creation Device (QSCD), con la chiave privata residente sul QSCD: i "
            "requisiti includono tutti quelli QCP-n (incluso NCP+) più le disposizioni aggiuntive "
            "specifiche per la fornitura del QSCD."
        ),
        "testo_integrale": (
            "3) A policy for EU qualified certificates issued to natural persons (QCP-n-qscd) "
            "offering the level of quality defined in Regulation (EU) No 910/2014 [i.1] for EU "
            "qualified certificates and requiring the use of a Qualified Signature Creation Device "
            "(QSCD). Such policy requires that the private key related to the certified public key "
            "resides in the QSCD: - The requirements for QCP-n-qscd include all the QCP-n "
            "requirements (including all the NCP+ requirements), plus additional provisions suited "
            "to support EU qualified certificates issuance and management as specified in Regulation "
            "(EU) No 910/2014 [i.1], including those specific to the QSCD provision."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 4.2.2, policy 4) (QCP-l-qscd)",
        "testo": (
            "Policy per certificati qualificati UE rilasciati a persone giuridiche (QCP-l-qscd), al "
            "livello di qualità del regolamento (UE) n. 910/2014 e che richiede l'uso di un Qualified "
            "Seal Creation Device (QSCD), con la chiave privata residente sul QSCD: i requisiti "
            "includono tutti quelli QCP-l (incluso NCP+) più le disposizioni aggiuntive specifiche "
            "per la fornitura del QSCD."
        ),
        "testo_integrale": (
            "4) A policy for EU qualified certificates issued to legal persons (QCP-l-qscd) offering "
            "the level of quality defined in Regulation (EU) No 910/2014 [i.1] for EU qualified "
            "certificates and requiring the use of a Qualified Seal Creation Device (QSCD). Such "
            "policy requires that the private key related to the certified public key resides in the "
            "QSCD: - The requirements for QCP-l-qscd include all the QCP-l requirements (including "
            "all the NCP+ requirements), plus additional provisions suited to support EU qualified "
            "certificates issuance and management as specified in Regulation (EU) No 910/2014 [i.1], "
            "including those specific to the QSCD provision."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 4.2.2, policy 5) (QEVCP-w)",
        "testo": (
            "Policy per certificati qualificati UE di sito web (QEVCP-w) conforme all'ultima versione "
            "delle EVCG, che offre almeno il livello di garanzia \"Extended Validated\" del CA/"
            "Browser Forum e il livello di qualità del regolamento (UE) n. 910/2014 per "
            "l'autenticazione di siti web: i requisiti includono tutti quelli EVCP per certificati a "
            "persone giuridiche più le disposizioni aggiuntive per l'emissione e gestione dei "
            "certificati qualificati UE."
        ),
        "testo_integrale": (
            "5) A policy for EU qualified website certificates (QEVCP-w) that conforms to the latest "
            "version of EVCG [i.7], offering at a minimum the \"Extended Validated\" level of "
            "assurance as defined by the CA/Browser Forum, and the level of quality defined in "
            "Regulation (EU) No 910/2014 [i.1] for EU qualified certificates used in support of "
            "websites authentication: - The requirements for QEVCP-w include all the EVCP "
            "requirements for certificates issued to legal persons, plus additional provisions "
            "suited to support EU qualified certificates issuance and management as specified in "
            "Regulation (EU) No 910/2014 [i.1]."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 4.2.2, policy 6) (QNCP-w)",
        "testo": (
            "Policy per certificati qualificati UE di sito web (QNCP-w) conforme all'ultima versione "
            "delle BRG, che offre almeno il livello di garanzia \"Organization Validated\" o "
            "\"Individual Validated\" del CA/Browser Forum e il livello di qualità del regolamento "
            "(UE) n. 910/2014 per l'autenticazione di siti web: i requisiti includono tutti quelli "
            "NCP per certificati a persone fisiche o giuridiche più, alternativamente, i requisiti "
            "IVCP o OVCP, più le disposizioni aggiuntive per l'emissione e gestione dei certificati "
            "qualificati UE."
        ),
        "testo_integrale": (
            "6) A policy for EU qualified website certificates (QNCP-w) that conforms to the latest "
            "version of BRG [i.3], offering at a minimum the \"Organization Validated\" or "
            "\"Individual Validated\" level of assurance as defined by the CA/Browser Forum and the "
            "level of quality defined in Regulation (EU) No 910/2014 [i.1] for EU qualified "
            "certificates used in support of websites authentication: - The requirements for QNCP-w "
            "include all the NCP requirements for certificates issued to natural or legal persons, "
            "plus either the IVCP or the OVCP requirements, plus additional provisions suited to "
            "support EU qualified certificates issuance and management as specified in Regulation "
            "(EU) No 910/2014 [i.1]."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 4.2.2, policy 7) (QNCP-w-gen)",
        "testo": (
            "Policy per certificati qualificati UE di sito web per scopo generale (QNCP-w-gen), al "
            "livello di qualità del regolamento (UE) n. 910/2014 per l'autenticazione di siti web: i "
            "requisiti includono tutti quelli NCP per certificati a persone fisiche o giuridiche più "
            "i requisiti selezionati delle BRG contrassegnati [WEB] in ETSI EN 319 411-1, più le "
            "disposizioni aggiuntive per l'emissione e gestione dei certificati qualificati UE."
        ),
        "testo_integrale": (
            "7) A policy for EU qualified website certificates (QNCP-w-gen) offering the level of "
            "quality defined in Regulation (EU) No 910/2014 [i.1] for EU qualified certificates used "
            "in support of websites authentication for general purpose certificate for qualified "
            "website authentication: - The requirements for QNCP-w-gen include all the NCP "
            "requirements for certificates issued to natural or legal persons, plus selected "
            "requirements from BRG [i.3] tagged as [WEB] in ETSI EN 319 411-1 [2], plus additional "
            "provisions suited to support EU qualified certificates issuance and management as "
            "specified in Regulation (EU) No 910/2014 [i.1]."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 4.2.2 (chiusura — rinvio a clausola 7)",
        "testo": (
            "La clausola 7 specifica un framework per ulteriori certificate policy che ampliano o "
            "restringono ulteriormente le 7 policy sopra elencate."
        ),
        "testo_integrale": (
            "Clause 7 specifies a framework for other certificate policies which enhance or further "
            "constrain the above policies."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 4.2.3 (Terms and conditions and PKI disclosure statement)",
        "testo": (
            "Si applicano le spiegazioni della clausola 4.2.3 di ETSI EN 319 411-1 su termini e "
            "condizioni e PKI disclosure statement."
        ),
        "testo_integrale": (
            "4.2.3 Terms and conditions and PKI disclosure statement: The explanations identified in "
            "ETSI EN 319 411-1 [2], clause 4.2.3 apply."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: clausola 4.3 (Certification services)",
        "testo": (
            "Il servizio di emissione dei certificati qualificati UE è scomposto nei servizi "
            "component presentati in ETSI EN 319 411-1, clausola 4.4, ai fini della classificazione "
            "dei requisiti."
        ),
        "testo_integrale": (
            "4.3 Certification services: The service of issuing EU qualified certificates is broken "
            "down in component services presented in ETSI EN 319 411-1 [2], clause 4.4 for the "
            "purposes of classifying requirements."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Parte 2: clausola 1 (Scope)",
    "Parte 2: clausola 2.1 (Normative references)",
    "Parte 2: clausola 2.2 (Informative references)",
    "Parte 2: clausola 3.1 (Terms)",
    "Parte 2: clausola 3.3 (Abbreviations)",
    "Parte 2: clausola 3.4 (Notations)",
    "Parte 2: clausola 4.1 (General policy requirements concepts)",
    "Parte 2: clausola 4.2.1 (Certification Practice Statement)",
    "Parte 2: clausola 4.2.2 (Certificate Policy — introduzione)",
    "Parte 2: clausola 4.2.2, policy 1) (QCP-n)",
    "Parte 2: clausola 4.2.2, policy 2) (QCP-l)",
    "Parte 2: clausola 4.2.2, policy 3) (QCP-n-qscd)",
    "Parte 2: clausola 4.2.2, policy 4) (QCP-l-qscd)",
    "Parte 2: clausola 4.2.2, policy 5) (QEVCP-w)",
    "Parte 2: clausola 4.2.2, policy 6) (QNCP-w)",
    "Parte 2: clausola 4.2.2, policy 7) (QNCP-w-gen)",
    "Parte 2: clausola 4.2.2 (chiusura — rinvio a clausola 7)",
    "Parte 2: clausola 4.2.3 (Terms and conditions and PKI disclosure statement)",
    "Parte 2: clausola 4.3 (Certification services)",
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
