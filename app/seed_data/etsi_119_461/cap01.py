"""ETSI TS 119 461 V2.1.1 (2025-02) - Electronic Signatures and Trust
Infrastructures (ESI); Policy and security requirements for trust service
components providing identity proofing of trust service subjects. Fonte 9,
capitolo 1: clausole 1 (Scope), 2 (References), 3 (Definition of terms,
symbols, abbreviations and notations). Testo ufficiale in
app/.source_cache/etsi_119_461/cap01.txt.

Modellazione (ADR-0007), stesso genere di fonte di ETSI EN 319 412-5 (Fonte
7) - standard tecnico ETSI a clausole/sottoclausole, non atto legislativo ad
articoli/commi - con l'aggiunta specifica di questo documento: i requisiti
sostanziali (clausole 5-11 e Annex C, coperti dagli altri capitoli) portano
un identificatore alfanumerico proprio nel testo (es. "INI-8.1-01X"), la cui
sintassi e legenda sono definite proprio in clausola 3.4, oggetto di questo
capitolo.

- Clausola 1 (Scope) -> 1 Principio "scopo/ambito di applicazione",
  riferimento "clausola 1 (Scope)". Testo integrale riportato per intero
  (4 paragrafi) perché definisce l'ambito applicativo esatto (Baseline vs
  Extended LoIP, rapporto con l'art. 24 eIDAS/eIDAS2 originale e modificato,
  clausole C.2/C.3/C.4 di raccordo con Annex C) che gli altri capitoli
  presuppongono senza ripeterlo.
- Clausola 2 (References, normative e informative) -> NESSUN nodo: è
  bibliografia/paratesto puro (elenco di documenti citati, incluse voci
  "Void" senza contenuto autonomo), stesso trattamento già riservato alla
  clausola 2 di ETSI EN 319 412-5 (mai un nodo in questo censimento).
- Clausola 3.1 (Terms) -> 1 Principio "definitorio" riassuntivo (non un nodo
  per singolo termine: la clausola è un glossario alfabetico piatto senza
  struttura a lettere/numeri, diversamente dall'art. 3 eIDAS che ha lettere
  numerate proprie - un nodo per sottoclausola è il livello di granularità
  coerente con quanto già fatto per la clausola 3 di ETSI EN 319 412-5).
  Include ~55 termini; NOTE esplicative (es. eIDAS v1/v2 shorthand) assorbite
  nel testo quando aggiungono contenuto sostanziale, altrimenti scartate.
- Clausola 3.2 (Symbols) -> NESSUN nodo: il testo è integralmente "Void."
  senza alcun contenuto oltre il rimando strutturale, stesso criterio già
  applicato alle voci "Void" di ETSI EN 319 412-5 (es. 3.2/4.3.5.2 in quel
  documento) e al rinvio generale di questo censimento per clausole prive di
  contenuto autonomo. Non genera un item di indice.
- Clausola 3.3 (Abbreviations) -> 1 Principio "definitorio" riassuntivo. La
  tabella a due colonne (abbreviazione | forma estesa) del testo ufficiale
  arriva mal renderizzata dalla conversione PDF->markdown (celle unite,
  ordine disallineato tra colonna sinistra e destra su più righe); l'elenco
  riportato in `testo`/`testo_integrale` è la ricostruzione delle 26 coppie
  corrette (ordine alfabetico originale: AI, APCER, BPCER, CAB, EAA, eID,
  eMRTD, ENISA, FAR, FRR, GDPR, IAD, ICAO, IPSP, LEI, LoA, LoIP, MRZ, NCP,
  OID, PAD, PRADO, QERDS, QTSP, TLS, TSP), verificabile per confronto con il
  raw della tabella in app/.source_cache/etsi_119_461/cap01.txt righe 374-394.
- Clausola 3.4 (Notations) -> 1 Principio "definitorio", riferimento
  "clausola 3.4 (Notations)". Nodo cruciale per l'intero documento: riporta
  la legenda COMPLETA e verbatim dei prefissi dei requisiti (formato
  <3 lettere>-<clausola>-<numero progressivo>, marcatura "[CONDITIONAL]",
  regole di gestione tra edizioni per inserimenti/soppressioni/modifiche),
  così che gli altri capitoli (che citano id di requisito come "INI-8.1-01X",
  "VAL-8.3-12" ecc.) e la sessione principale possano verificare per
  riferimento invece di ricopiare la legenda in ciascun modulo. Legenda
  letterale delle 8 famiglie: OVR (requisito generale, applicabile a più di
  un componente), INI (avvio dell'identity proofing), COL (raccolta di
  attributi ed evidenze), VAL (validazione di attributi ed evidenze), BIN
  (binding al richiedente), ISS (emissione del risultato/evidenze del
  processo), USE (casi d'uso), QTS (requisiti specifici identity proofing
  per servizi fiduciari qualificati UE, Annex C). NOTA per gli altri
  subagent: il testo di assegnazione del main citava come esempio
  "ATT-8.2-03", ma la legenda ufficiale di 3.4 non contiene alcun prefisso
  "ATT" (né "POL"/"ORG") - solo le 8 famiglie sopra; segnalato ai peer via
  hub, il capitolo che copre la clausola 8.2 deve attenersi al prefisso
  letteralmente presente nel proprio testo, non a questo esempio del main.

RELAZIONI interne: nessuna. I quattro nodi di questo capitolo sono cornice
definitoria/di ambito autonoma (scope, glossario termini/abbreviazioni,
notazione degli id) senza un rapporto tipizzato certo (specifica/attua/
richiama/...) verso una singola disposizione sostanziale di un altro
capitolo - ogni requisito degli altri capitoli presuppone implicitamente
tutta la clausola 3, non un singolo nodo di essa, per cui una relazione
esplicita sarebbe arbitraria; si preferisce ometterla piuttosto che
inventare un riferimento (criterio esplicito del contratto dati assegnato).
"""

RIGHE_OBBLIGHI: list[dict] = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 1 (Scope)",
        "testo": (
            "Il documento specifica requisiti di policy e sicurezza per i componenti di servizio "
            "fiduciario che effettuano l'identity proofing dei soggetti dei servizi fiduciari. Tale "
            "componente puo' essere erogato dal Trust Service Provider (TSP) stesso come parte "
            "integrante del servizio fiduciario, oppure da un Identity Proofing Service Provider "
            "(IPSP) specializzato che agisce come subappaltatore del TSP (l'identity proofing non e' "
            "considerato un servizio fiduciario a se' stante ma una componente del servizio fiduciario "
            "per cui viene svolto). Il documento definisce requisiti per due Livelli di Identity "
            "Proofing (LoIP), Baseline ed Extended, a supporto dell'identity proofing per standard "
            "ETSI di servizi fiduciari come ETSI EN 319 411-1, ETSI EN 319 411-2 ed ETSI EN 319 521, "
            "e requisiti per innalzare un identity proofing da Baseline a Extended LoIP quando il "
            "Baseline sia stato raggiunto tramite mezzi di identificazione elettronica (eID) di Level "
            "of Assurance (LoA) 'substantial' secondo il regolamento eIDAS modificato o un LoA "
            "equivalente di un framework di garanzia comparabile. Il Baseline LoIP mira a supportare "
            "l'identity proofing per i certificati qualificati ex art. 24.1 del regolamento eIDAS "
            "originale; l'Extended LoIP mira a supportare l'identity proofing per certificati "
            "qualificati e attestati elettronici qualificati di attributi ex artt. 24.1, 24.1a e 24.1b "
            "del regolamento eIDAS modificato. Il documento mira a soddisfare i requisiti del "
            "regolamento eIDAS originale tramite i requisiti di clausola C.2 e quelli del regolamento "
            "eIDAS modificato tramite i requisiti di clausola C.3; e' destinato a essere richiamato da "
            "un atto di esecuzione ex art. 24.1c del regolamento eIDAS modificato che stabilisca "
            "specifiche tecniche minime, standard e procedure per la verifica dell'identita' e degli "
            "attributi ex artt. 24.1, 24.1a, 24.1b eIDAS modificato. Mira inoltre a soddisfare i "
            "requisiti dell'art. 44 (identity proofing per i servizi qualificati di recapito "
            "elettronico certificato) tramite i requisiti di clausola C.4; eIDAS non pone requisiti "
            "specifici di identity proofing per gli altri servizi fiduciari qualificati. Il documento "
            "puo' essere usato dagli organismi di valutazione della conformita' (CAB) come base per "
            "confermare l'affidabilita' del processo di identity proofing di un'organizzazione. Pur "
            "avendo potenzialmente un'applicabilita' piu' ampia dell'ambito definito, l'applicazione "
            "per scopi diversi dai servizi fiduciari resta fuori ambito."
        ),
        "testo_integrale": (
            "1 Scope: The present document specifies policy and security requirements for trust "
            "service components providing identity proofing of trust service subjects. Such a trust "
            "service component can be provided by the Trust Service Provider (TSP) itself as an "
            "integral part of the trust service or by a specialized Identity Proofing Service "
            "Provider (IPSP) acting as a subcontractor to the TSP. The term \"trust service "
            "component\" is used because identity proofing is not considered as a trust service on "
            "its own but as a component of the trust service for which the identity proofing is "
            "done. The present document provides requirements for two Levels of Identity Proofing "
            "(LoIP), Baseline and Extended. These LoIPs aim to support identity proofing for ETSI "
            "trust services standards such as ETSI EN 319 411-1 [i.7], ETSI EN 319 411-2 [i.8] and "
            "ETSI EN 319 521 [i.12]. The present document also provides requirements to enhance an "
            "identity proofing from Baseline LoIP to Extended LoIP when the Baseline LoIP has been "
            "reached by use of electronic Identification means (eID) at Level of Assurance (LoA) "
            "'substantial' according to the amended eIDAS regulation [i.25] or a similar LoA based on "
            "a comparable assurance level framework. The present document aims at supporting identity "
            "proofing in European and other regulatory frameworks. Specifically, but not exclusively, "
            "the Baseline LoIP aims to support identity proofing for qualified certificates as "
            "defined in Regulation (EU) No 910/2014 [i.1] (the original eIDAS regulation) Article "
            "24.1, while the Extended LoIP aims to support identity proofing for qualified "
            "certificates and qualified attestations of attributes as defined in Articles 24.1, "
            "24.1a, and 24.1b of the amended eIDAS regulation [i.25]. The present document aims to "
            "meet the requirements of the original eIDAS regulation [i.1] by the requirements in "
            "clause C.2 and the requirements of the amended eIDAS regulation [i.25] by the "
            "requirements in clause C.3. The present document is intended to be applicable for "
            "reference from an implementing act according to Article 24.1c of the amended eIDAS "
            "regulation [i.25], setting out minimum technical specifications, standards and "
            "procedures with respect to the verification of identity and attributes in accordance "
            "with Articles 24.1, 24.1a, and 24.1b of the amended eIDAS regulation [i.25]. The present "
            "document aims to meet the requirements of Article 44 of the aforementioned regulations "
            "on identity proofing for qualified electronic registered delivery services by the "
            "requirements in clause C.4. eIDAS has no specific requirements for identity proofing for "
            "other qualified trust services. The present document can be used by Conformity "
            "Assessment Bodies (CAB) as the basis for confirming that an organization is trustworthy "
            "and reliable in its identity proofing process. NOTE 2: The present document has the "
            "potential to have wider applicability than the defined scope, but any application for "
            "other purposes than trust services is out of scope."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.1 (Terms)",
        "testo": (
            "Oltre ai termini gia' definiti in ETSI TR 119 001 ed ETSI EN 319 401, la clausola "
            "definisce un glossario di circa 55 termini specifici dell'identity proofing, raggruppabili "
            "per area: (i) contesto normativo eIDAS - 'amended eIDAS regulation' (Reg. 910/2014 come "
            "modificato da Reg. 2024/1183 e Direttiva 2022/2555, 'eIDAS v2'), 'original eIDAS "
            "regulation' (Reg. 910/2014 come pubblicato nel 2014, 'eIDAS v1'), 'electronic "
            "Identification means (eID means, eID)' e le sue declinazioni 'eID scheme', 'eIDAS "
            "certified/high/notified/substantial eID', 'eIDAS signature validation', 'electronic "
            "attestation of attributes'; (ii) attori del processo - 'applicant' (persona la cui "
            "identita' deve essere provata), 'subject' (persona arruolata a un servizio fiduciario), "
            "'subscriber', 'registration officer' (persona fisica che svolge il processo), "
            "'legitimate evidence holder'; (iii) il processo di identity proofing e i suoi livelli - "
            "'identity', 'identity proofing (process)', 'identity proofing context', 'identity "
            "proofing service policy', 'Level of Identity Proofing (LoIP)', 'Baseline LoIP' (livello "
            "di confidenza 'substantial'), 'Extended LoIP' (livello di confidenza 'high'), 'binding "
            "to applicant', 'validation', 'freshness'; (iv) modalita' di erogazione - 'attended/"
            "unattended remote identity proofing', 'physical presence', 'remote identity proofing'; "
            "(v) evidenze e fonti - 'authentic source', 'authoritative evidence', 'authoritative "
            "source', '(identity) attribute', '(identity) evidence', 'supplementary evidence', 'proof "
            "of access', 'trusted register', 'identity document', 'digital identity document', "
            "'physical identity document', 'pseudonym', '(IPSP) practice statement', 'trust service "
            "component'; (vi) sicurezza biometrica e attacchi - 'attack potential' e le sue "
            "graduazioni 'moderate'/'high attack potential', 'injection attack', 'Injection Attack "
            "Detection (IAD)', 'presentation attack', 'Presentation Attack Detection (PAD)', "
            "'liveness detection', 'Attack Presentation Classification Error Rate (APCER)', 'Bona "
            "fide Presentation Classification Error Rate (BPCER)', 'False Acceptance Rate (FAR)', "
            "'False Rejection Rate (FRR)'; (vii) definizioni trasversali - 'qualified electronic "
            "seal', 'qualified electronic signature'."
        ),
        "testo_integrale": (
            "3.1 Terms: For the purposes of the present document, the terms given in ETSI TR 119 001 "
            "[i.4], ETSI EN 319 401 [1] and the following apply - amended eIDAS regulation: "
            "Regulation (EU) No 910/2014 as amended by Regulation (EU) 2024/1183 and Directive (EU) "
            "2022/2555 (NOTE: sometimes called \"eIDAS v2\"). applicant: person (legal or natural) "
            "whose identity is to be proven. attack potential: measure of the effort needed to "
            "exploit a vulnerability in a Target Of Evaluation (TOE). Attack Presentation "
            "Classification Error Rate (APCER): proportion of attack presentations using the same "
            "presentation attack instrument species incorrectly classified as bona fide presentations "
            "in a specific scenario. attended remote identity proofing: identity proofing process by "
            "remote use of identity document where the capture of the identity document and the face "
            "video of the applicant are performed in a session supervised by a registration officer. "
            "authentic source: repository or system, held under the responsibility of a public sector "
            "body or private entity, that contains and provides attributes about a natural or legal "
            "person or object and that is considered a primary source of that information or "
            "recognized as authentic in accordance with Union or national law. authoritative "
            "evidence: evidence presented by the applicant, holding identifying attribute(s) of the "
            "identity, trusted for the binding of these attributes to the applicant. authoritative "
            "source: any source, irrespective of form, relied upon to provide accurate data, "
            "information and/or evidence usable to prove identity. (identity) attribute: "
            "characteristic, quality, right or permission of a natural or legal person or of an "
            "object. Baseline LoIP: LoIP reaching a substantial level of confidence based on "
            "fulfilment of good practice minimum requirements. binding to applicant: part of an "
            "identity proofing process that verifies the applicant is the person identified by the "
            "presented evidence. Bona fide Presentation Classification Error Rate (BPCER): "
            "proportion of bona fide presentations incorrectly classified as presentation attacks. "
            "digital identity document: identity document issued in machine-processable form, "
            "digitally signed by the issuer, in purely digital form. electronic attestation of "
            "attributes: attestation in electronic form that allows attributes to be authenticated. "
            "electronic Identification means (eID means, eID): material and/or immaterial unit "
            "containing person identification data used for authentication. eID scheme: governance "
            "model and technical specifications allowing interoperability between eID means. eIDAS "
            "certified eID: eID or eID scheme certified according to Article 12a of the amended "
            "eIDAS regulation. eIDAS high eID / eIDAS substantial eID: eID or eID scheme fulfilling "
            "the requirements for assurance level high/substantial in Article 8 of the amended eIDAS "
            "regulation and CIR (EU) 2015/1502. eIDAS notified eID: eID or eID scheme notified "
            "according to Article 9 of the amended eIDAS regulation. eIDAS signature validation: "
            "validation of an electronic signature or seal in compliance with the eIDAS regulation. "
            "(identity) evidence: information or documentation provided by the applicant or obtained "
            "from other sources, trusted to prove claimed identity attributes are correct. extended "
            "LoIP: LoIP reaching a high level of confidence based on fulfilment of good practice "
            "minimum requirements. False Acceptance Rate (FAR): proportion of verification "
            "transactions with false biometric claims erroneously accepted. False Rejection Rate "
            "(FRR): proportion of verification transactions with true biometric claims erroneously "
            "rejected. freshness: time between issuance of an evidence and time of use/validation of "
            "the evidence. high attack potential: effort needed by a highly skilled adversary with "
            "significant resources and opportunity to exploit a vulnerability. identity: attribute or "
            "set of attributes that uniquely identify a person within a given context. identity "
            "document: physical or digital identity document issued by an authoritative source "
            "attesting to the applicant's identity. identity proofing context: external requirements "
            "affecting the identity proofing process, given by the purpose, regulatory requirements, "
            "and restrictions on attributes/evidence/process. identity proofing (process): process by "
            "which the identity, and possibly additional attributes, of an applicant is verified by "
            "use of evidence attesting the required identity attributes. identity proofing service "
            "policy: set of rules indicating the applicability of an identity proofing service to a "
            "community/class of application with common security requirements. injection attack: "
            "attack consisting of injecting content controlled by the attacker into the data capture "
            "process. Injection Attack Detection (IAD): automated determination of an injection "
            "attack. legitimate evidence holder: person for whom the evidence is issued. Level of "
            "Identity Proofing (LoIP): confidence achieved in the identity proofing (Baseline / "
            "Extended). liveness detection: measurement and analysis of anatomical characteristics or "
            "involuntary/voluntary reactions to determine if a biometric sample is captured from a "
            "living subject present at capture. moderate attack potential: effort needed by a skilled "
            "adversary with significant resources and opportunity. original eIDAS regulation: "
            "Regulation (EU) No 910/2014 as published in 2014, without the 2024 amendments "
            "(\"eIDAS v1\"). physical identity document: identity document issued in physical and "
            "human-readable form. physical presence: identity proofing where the applicant is "
            "required to be physically present at the location of the identity proofing. (IPSP) "
            "practice statement: statement of the practices an IPSP employs in providing the identity "
            "proofing trust service component. presentation attack: presentation to the biometric "
            "data capture subsystem with the goal of interfering with the operation of the biometric "
            "system. Presentation Attack Detection (PAD): automated determination of a presentation "
            "attack. proof of access: any source, irrespective of form, trusted for reliable data/"
            "information/evidence usable in an identity proofing process, provided the applicant can "
            "demonstrate access to the source. pseudonym: fictitious identity assumed for a "
            "particular purpose, differing from the original or true identity. qualified electronic "
            "seal / qualified electronic signature: advanced electronic seal/signature created by a "
            "qualified creation device and based on a qualified certificate. registration officer: "
            "human being carrying out all or selected parts of an identity proofing process. remote "
            "identity proofing: identity proofing process where the applicant is physically distant "
            "from the location of the identity proofing. subject: legal or natural person enrolled to "
            "a trust service. subscriber: legal or natural person bound by an agreement with a trust "
            "service provider to any subscriber obligations. supplementary evidence: evidence used in "
            "addition to authoritative evidence to strengthen reliability and/or as evidence for "
            "attributes not evidenced by the authoritative evidence. trusted register: public "
            "register, database or other source that is an authoritative source for the conveyance of "
            "identity attributes in the identity proofing context. trust service component: one part "
            "of the overall service of a TSP. unattended remote identity proofing: identity proofing "
            "process by remote use of identity document where capture of the identity document and "
            "face video are performed in an automated, interactive session without human supervision. "
            "validation: part of an identity proofing process that determines whether attributes are "
            "validated by the presented evidence and whether the evidence is genuine, authoritative "
            "and valid."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.3 (Abbreviations)",
        "testo": (
            "Oltre alle abbreviazioni gia' definite in ETSI TR 119 001, la clausola elenca le "
            "abbreviazioni specifiche del documento: AI (Artificial Intelligence), APCER (Attack "
            "Presentation Classification Error Rate), BPCER (Bona fide Presentation Classification "
            "Error Rate), CAB (Conformity Assessment Bodies), EAA (Electronic Attestation of "
            "Attributes), eID (electronic Identification), eMRTD (electronic Machine Readable Travel "
            "Document), ENISA (European Union Agency for Cybersecurity), FAR (False Acceptance Rate), "
            "FRR (False Rejection Rate), GDPR (General Data Protection Regulation), IAD (Injection "
            "Attack Detection), ICAO (International Civil Aviation Organization), IPSP (Identity "
            "Proofing Service Provider), LEI (Legal Entity Identifier), LoA (Level of Assurance), "
            "LoIP (Level of Identity Proofing), MRZ (Machine Readable Zone), NCP (Normalized "
            "Certificate Policy), OID (Object IDentifier), PAD (Presentation Attack Detection), PRADO "
            "(Public Register of Authentic travel and identity Documents Online), QERDS (Qualified "
            "Electronic Registered Delivery Service), QTSP (Qualified Trust Service Provider), TLS "
            "(Transport Layer Security), TSP (Trust Service Provider)."
        ),
        "testo_integrale": (
            "3.3 Abbreviations: For the purposes of the present document, the abbreviations given in "
            "ETSI TR 119 001 [i.4] and the following apply - AI: Artificial Intelligence. APCER: "
            "Attack Presentation Classification Error Rate. BPCER: Bona fide Presentation "
            "Classification Error Rate. CAB: Conformity Assessment Bodies. EAA: Electronic "
            "Attestation of Attributes. eID: electronic Identification. eMRTD: electronic Machine "
            "Readable Travel Document. ENISA: European (Union Agency for) Cybersecurity (Agency). "
            "FAR: False Acceptance Rate. FRR: False Rejection Rate. GDPR: General Data Protection "
            "Regulation. IAD: Injection Attack Detection. ICAO: International Civil Aviation "
            "Organization. IPSP: Identity Proofing Service Provider. LEI: Legal Entity Identifier. "
            "LoA: Level of Assurance. LoIP: Level of Identity Proofing. MRZ: Machine Readable Zone. "
            "NCP: Normalized Certificate Policy. OID: Object IDentifier. PAD: Presentation Attack "
            "Detection. PRADO: Public Register of Authentic travel and identity Documents Online. "
            "QERDS: Qualified Electronic Registered Delivery Service. QTSP: Qualified Trust Service "
            "Provider. TLS: Transport Layer Security. TSP: Trust Service Provider. (Ricostruzione "
            "delle 26 coppie abbreviazione/forma estesa a partire dalla tabella a due colonne del "
            "testo ufficiale, la cui conversione PDF->markdown unisce piu' etichette nella stessa "
            "cella disallineando l'ordine tra colonna sinistra e destra su alcune righe - raw in "
            "app/.source_cache/etsi_119_461/cap01.txt righe 374-394.)"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.4 (Notations)",
        "testo": (
            "La clausola definisce la notazione degli identificatori dei requisiti normativi del "
            "documento e le regole della loro gestione tra edizioni successive. I requisiti si "
            "dividono in due categorie: (a) applicabili a qualunque attore conforme al documento, "
            "indicati senza marcatura aggiuntiva; (b) applicabili solo a determinate condizioni, "
            "marcati con '[CONDITIONAL]' davanti all'identificatore o da clausole introdotte da "
            "'[CONDITIONAL]'. Il formato dell'identificatore e': <3 lettere dell'elemento di "
            "servizio>-<numero di clausola>-<numero progressivo a 2 cifre>. Gli elementi di servizio "
            "(prefissi) sono: OVR (requisito generale, applicabile a piu' di un componente), INI "
            "(requisiti sull'avvio dell'identity proofing), COL (requisiti sulla raccolta di "
            "attributi ed evidenze), VAL (requisiti sulla validazione di attributi ed evidenze), BIN "
            "(requisiti sul binding al richiedente), ISS (requisiti sull'emissione del risultato "
            "dell'identity proofing e delle evidenze del processo), USE (requisiti sui casi d'uso), "
            "QTS (requisiti specifici per l'identity proofing dei servizi fiduciari qualificati UE, "
            "Annex C). Regole di gestione degli identificatori tra edizioni successive: quando un "
            "requisito e' inserito alla fine di una clausola, il numero progressivo a 2 cifre e' "
            "incrementato al successivo disponibile; quando e' inserito all'inizio di una clausola, "
            "si usa il numero '00'; quando e' inserito tra due requisiti esistenti, si usano lettere "
            "maiuscole aggiunte all'identificatore del requisito precedente per distinguere i nuovi "
            "requisiti; l'identificatore di un requisito soppresso e' mantenuto e completato con "
            "'VOID'; quando un requisito e' modificato rispetto all'edizione precedente del "
            "documento, il numero del requisito e' integrato con una lettera maiuscola 'X'."
        ),
        "testo_integrale": (
            "3.4 Notations: The requirements identified in the present document include: a) "
            "requirements applicable to any actor conforming to the present document. Such "
            "requirements are indicated without any additional marking; b) requirements applicable "
            "under certain conditions. Such requirements are marked by \"[CONDITIONAL]\" or indicated "
            "by clauses introduced by \"[CONDITIONAL]\". The requirements in the present document are "
            "identified as follows: <the 3 letters identifying the elements of services>-<the clause "
            "number>-<2 digit number-incremental>. The elements of services are: OVR: General "
            "requirement (requirement applicable to more than 1 component). INI: Requirements on the "
            "initiation of the identity proofing. COL: Requirements on attribute and evidence "
            "collection. VAL: Requirements on attribute and evidence validation. BIN: Requirements on "
            "binding to applicant. ISS: Requirements on issuing of result of the identity proofing "
            "and evidence of the identity proofing process. USE: Requirements on use cases. QTS: "
            "Requirements specific to identity proofing for EU qualified trust services (Annex C). "
            "The management of the requirement identifiers for subsequent editions of the present "
            "document is as follows: When a requirement is inserted at the end of a clause, the 2 "
            "digit number above is incremented to the next available digit. When a requirement is "
            "inserted at the start of a clause, the 2 digit number 00 is used. When a requirement is "
            "inserted between two existing requirements, capital letters appended to the previous "
            "requirement identifier are used to distinguish new requirements. The requirement "
            "identifier for a deleted requirement is left and completed with \"VOID\". When a "
            "requirement is modified from the previous edition of the present document, the "
            "requirement number is amended by a capital 'X' letter."
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
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
