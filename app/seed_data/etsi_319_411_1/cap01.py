"""ETSI EN 319 411-1 V1.5.1 (2025-04) - Electronic Signatures and Trust
Infrastructures (ESI); Policy and security requirements for Trust Service
Providers issuing certificates; Part 1: General requirements. Fonte 17
(numerazione definitiva cablata dalla sessione principale in app/seed.py -
questo modulo NON tocca seed.py). Capitolo 1: clausole 1 (Scope), 2
(References: 2.1 Normative, 2.2 Informative), 3 (Definition of terms,
symbols, abbreviations and notations: 3.1 Terms, 3.2 Symbols, 3.3
Abbreviations, 3.4 Notations). Testo ufficiale in
app/.source_cache/etsi_319_411_1/cap01.txt.

Modellazione (ADR-0007), istruzioni esplicite dell'assegnazione (diverse dal
criterio "clausola 2 -> nessun nodo" applicato in altri capitoli/fonti dove
References era puro paratesto senza istruzione contraria):

- Clausola 1 (Scope) -> 1 Principio "scopo/ambito di applicazione",
  riferimento "Parte 1: clausola 1 (Scope)". Include il paragrafo di scope, l'elenco
  puntato di applicabilita' (cryptographic mechanisms/digital signature,
  TLS/SSL, autenticazione/cifratura), la precisazione sui limiti (non
  copre la valutazione di conformita' da parte terza) e la NOTE che rinvia
  a ETSI EN 319 403 (assorbita perche' precisa il perimetro di
  applicabilita' della valutazione, non mera bibliografia).
- Clausola 2 (References) -> per istruzione esplicita dell'assegnazione,
  censita (diversamente da altri capitoli di questo censimento dove la
  clausola References e' pura bibliografia senza nodo): 1 Principio
  "definitorio" per 2.1 (Normative references, [1]-[16]) e 1 Principio
  "definitorio" per 2.2 (Informative references, [i.1]-[i.23], incluso
  [i.13] Void). Non frammentato per singolo riferimento bibliografico.
  ANOMALIA DI ESTRAZIONE PDF->TXT documentata: nel file sorgente i marcatori
  numerici "[4]".."[16]" e i relativi titoli/i marcatori "[i.1]".."[i.5]" e
  i primi 5 titoli informativi (Direttiva 1999/93/EC .. ETSI EN 319 411-2)
  precedono, nell'ordine di estrazione grezzo, l'intestazione "#### 2.2
  Informative references" (probabile artefatto di layout a due colonne del
  PDF originale: la colonna con l'intestazione di clausola e' stata
  scansionata dopo la colonna con l'elenco numerato). Il contenuto e'
  comunque inequivocabilmente quello di 2.1 (16 riferimenti normativi,
  tutti citati altrove nel capitolo con "[N]", N=1..16) e 2.2 (23
  riferimenti informativi incl. [i.13] Void, tutti citati altrove nel
  capitolo con "[i.N]"): la mappatura numero->titolo e' stata verificata
  incrociando ogni "[N]"/"[i.N]" citato nelle NOTE di clausola 1 e 3
  (es. "EVCG [4]" in clausola 1 conferma [4]=CA/Browser Forum EVCG;
  "BRG [5]"/"BRG [6]" in clausola 3.4 confermano [5]=CA/Browser Forum
  V1.8.6 (versione specifica) e [6]=CA/Browser Forum senza versione
  (BRG generico, ultima versione applicabile); "ISO/IEC 7498-2/X.800 [i.8]" in
  clausola 3.1 conferma i.8; "IETF RFC 5246 [i.11]" nella NOTE di clausola
  3.3 conferma i.11; "ETSI TS 119 612 [i.12]" nella NOTE "trust anchor" di
  clausola 3.1 conferma i.12). testo_integrale riporta i due elenchi
  ricostruiti in ordine numerico logico (non nell'ordine di estrazione
  grezzo, che e' solo un artefatto di rendering, non contenuto normativo).
- Clausola 3.1 (Terms) -> 1 Principio "definitorio" riassuntivo (glossario
  alfabetico piatto di 29 termini, nessuna struttura a lettere/numeri
  propria oltre l'enumerazione 1)/2) interna alla definizione di
  "Certification Authority (CA)"). Tutte le NOTE sono mantenute in
  testo_integrale (incluse quelle di puro rimando bibliografico tipo "NOTE:
  See ISO/IEC 9594-8/Recommendation ITU-T X.509 [7]."): il criterio di
  omissione delle NOTE puramente bibliografiche e' opzionale per questo
  censimento, e per un glossario di 29 termini con NOTE numerate 1)/2)/3)
  intrecciate al testo si e' preferita la riproduzione integrale verbatim
  per azzerare il rischio di elisione accidentale. ANOMALIA VERBATIM
  documentata: la definizione di "revocation officer" nel testo sorgente
  include la stringa "ISO/IEC 7498-2/Recommendation ITU-T X.800 [i.8]"
  accodata senza il consueto prefisso "NOTE:" (a differenza di ogni altra
  citazione bibliografica del glossario, sempre introdotta da "NOTE:");
  riportata cosi' com'e' nel file sorgente, senza correggerla (non e'
  compito di questo censimento emendare il testo normativo).
- Clausola 3.2 (Symbols) -> 1 Principio "definitorio", riferimento
  "Parte 1: clausola 3.2 (Symbols)", testo_integrale "3.2 Symbols: Void." (a
  differenza di altri capitoli/fonti dove "Void." senza altro contenuto non
  genera nodo, qui e' incluso per coerenza con l'istruzione esplicita
  dell'assegnazione di censire integralmente la clausola 3 con le sue
  quattro sottoclausole).
- Clausola 3.3 (Abbreviations) -> 1 Principio "definitorio" riassuntivo, 47
  abbreviazioni. La tabella finale (dopo OVCP) arriva mal renderizzata
  dalla conversione PDF->markdown (celle disallineate con "||" finale su
  alcune righe: "|OVR General Requirement||", "|RA Registration
  Authority||", "|REQ Requirement||", "|SSL Secure Socket Layer||" -
  artefatto di layout a due colonne collassato). Ricostruita come
  prosecuzione alfabetica dell'elenco (OVR, PDF/A, PDS, PIN, PKI, RA, REG,
  REQ, REV, SDP, SSL, TLS, TLS/SSL, TSP, UTC), verificata per coerenza
  alfabetica sul raw in app/.source_cache/etsi_319_411_1/cap01.txt righe
  146-163. La NOTE finale "IETF RFC 5246 [i.11] or earlier equivalent
  Secure Socket Layer protocol." e' mantenuta (aggiunge contenuto
  interpretativo sull'abbreviazione SSL/TLS).
- Clausola 3.4 (Notations) -> 1 Principio "definitorio", riferimento
  "Parte 1: clausola 3.4 (Notations)". NODO CRUCIALE per l'intero documento e per i
  capitoli successivi (per esplicita istruzione dell'assegnazione): riporta
  verbatim le cinque marcature dei requisiti (nessuna marcatura, marcatura
  "[CONDITIONAL]", "[CHOICE]", marcatura di CP applicabile
  "[LCP]"/"[NCP]"/"[NCP+]"/"[EVCP]"/"[OVCP]"/"[IVCP]"/"[DVCP]", marcatura
  "[WEB]"), lo schema identificativo dei requisiti <3 lettere servizio>-
  <numero di clausola>-<numero progressivo a 2 cifre>, l'elenco dei sette
  service component (OVR, GEN, REG, REV, DIS, SDP, CSS) e le regole di
  gestione degli identificativi tra edizioni successive (inserimento a fine
  clausola, inserimento intermedio con lettere maiuscole accodate,
  identificativo di requisito eliminato marcato "Void", identificativo di
  requisito modificato con lettere maiuscole accodate) - quest'ultimo
  paragrafo non ha un'intestazione di sottoclausola propria nel testo
  sorgente (nessun "#### 3.5"), resta quindi parte dello stesso nodo 3.4.

RELAZIONI interne: nessuna. I sette nodi di questo capitolo sono cornice
definitoria/di ambito autonoma (scope, bibliografia normativa/informativa,
glossario termini/simboli/abbreviazioni, notazione degli id dei requisiti)
senza citazione testuale esplicita dell'id di un requisito di un altro nodo
dello stesso capitolo - si preferisce omettere una relazione "specifica"/
"richiama" arbitraria piuttosto che inventarla, coerente con il criterio
gia' adottato in ETSI EN 319 401 cap01.py e ETSI TS 119 461 cap01.py. Nessuna
relazione cross-fonte in questo modulo per vincolo esplicito
dell'assegnazione (RELAZIONI resta vuoto, punto 7 del contratto dati).
"""

RIGHE_OBBLIGHI: list[dict] = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "Parte 1: clausola 1 (Scope)",
        "testo": (
            "Il documento specifica requisiti di policy e sicurezza generalmente applicabili ai Trust "
            "Service Provider (TSP) che emettono certificati a chiave pubblica, inclusi i certificati per "
            "siti web fidati. I requisiti coprono l'emissione, il mantenimento e la gestione del ciclo di "
            "vita dei certificati, a supporto delle certificate policy di riferimento definite nelle "
            "clausole 4 e 5; un framework per requisiti di policy in contesti specifici e' definito nella "
            "clausola 7. Copre le gerarchie di CA solo nella misura in cui supportano tali policy (non le "
            "root CA/CA intermedie per altri scopi). E' applicabile ai requisiti generali di certificazione "
            "a supporto di meccanismi crittografici (incluse firme digitali per firme e sigilli elettronici), "
            "ai requisiti generali delle CA che emettono certificati TLS/SSL e ai requisiti generali sull'uso "
            "della crittografia per autenticazione e cifratura. Non specifica come tali requisiti possano "
            "essere valutati da una parte indipendente (NOTA: si veda ETSI EN 319 403 per la guida alla "
            "valutazione dei processi/servizi del TSP). Richiama ETSI EN 319 401 per i requisiti di policy "
            "generali comuni a tutte le classi di servizi TSP e include previsioni coerenti con i requisiti "
            "del CA/Browser Forum in EVCG e BRG."
        ),
        "testo_integrale": (
            "1 Scope: The present document specifies generally applicable policy and security requirements "
            "for Trust Service Providers (TSPs) issuing public key certificates, including trusted web site "
            "certificates. The policy and security requirements are defined in terms of requirements for the "
            "issuance, maintenance and life-cycle management of certificates. These policy and security "
            "requirements support several reference certificate policies, defined in clauses 4 and 5. A "
            "framework for the definition of policy requirements for TSPs issuing certificates in a specific "
            "context where particular requirements apply is defined in clause 7. The present document covers "
            "requirements for CA hierarchies, however this is limited to supporting the policies as specified "
            "in the present document. It does not include requirements for root CAs and intermediate CAs for "
            "other purposes. The present document is applicable to: "
            "- the general requirements of certification in support of cryptographic mechanisms, including "
            "digital signatures for electronic signatures and seals; "
            "- the general requirements of certification authorities issuing TLS/SSL certificates; "
            "- the general requirements of the use of cryptography for authentication and encryption. "
            "The present document does not specify how the requirements identified can be assessed by an "
            "independent party, including requirements for information to be made available to such "
            "independent assessors, or requirements on such assessors. NOTE: See ETSI EN 319 403 [i.2] for "
            "guidance on assessment of TSP's processes and services. The present document references ETSI EN "
            "319 401 [9] for general policy requirements common to all classes of TSP's services. The present "
            "document includes provisions consistent with the requirements from the CA/Browser Forum in EVCG "
            "[4] and BRG [6]."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 2.1 (Normative references)",
        "testo": (
            "Elenco dei 16 riferimenti normativi necessari all'applicazione del documento (citati "
            "puntualmente nel testo con [N]): ISO/IEC 15408 (criteri di valutazione IT security), ETSI EN "
            "319 412-4 (profilo certificati siti web), ISO/IEC 19790:2012 (requisiti moduli crittografici), "
            "CA/Browser Forum EVCG e BRG (in due varianti: versione fissata V1.8.6 e versione corrente), "
            "ISO/IEC 9594-8/ITU-T X.509, IETF RFC 5280, ETSI EN 319 401, ETSI EN 319 412-1/-2/-3, IETF RFC "
            "6960 (OCSP), FIPS PUB 140-2 (2001) e FIPS PUB 140-3 (2019), ETSI TS 119 461."
        ),
        "testo_integrale": (
            "2.1 Normative references: References are either specific (identified by date of publication "
            "and/or edition number or version number) or non-specific. For specific references, only the "
            "cited version applies. For non-specific references, the latest version of the referenced "
            "document (including any amendments) applies. Referenced documents which are not found to be "
            "publicly available in the expected location might be found in the ETSI docbox. NOTE: While any "
            "hyperlinks included in this clause were valid at the time of publication, ETSI cannot guarantee "
            "their long term validity. The following referenced documents are necessary for the application "
            "of the present document. "
            "[1] ISO/IEC 15408 (parts 1 to 3): \"Information security, cybersecurity and privacy protection "
            "— Evaluation criteria for IT security\". "
            "[2] ETSI EN 319 412-4: \"Electronic Signatures and Trust Infrastructures (ESI); Certificate "
            "Profiles; Part 4: Certificate profile for web site certificates\". "
            "[3] ISO/IEC 19790:2012: \"Information technology — Security techniques — Security requirements "
            "for cryptographic modules\". "
            "[4] CA/Browser Forum: \"Guidelines for the Issuance and Management of Extended Validation "
            "Certificates\". "
            "[5] CA/Browser Forum (V1.8.6): \"Baseline Requirements for the Issuance and Management of "
            "Publicly-Trusted Certificates\". "
            "[6] CA/Browser Forum: \"Baseline Requirements for the Issuance and Management of Publicly-"
            "Trusted Certificates\". "
            "[7] ISO/IEC 9594-8/Recommendation ITU-T X.509: \"Information technology — Open systems "
            "interconnection — Part 8: The Directory: Public-key and attribute certificate frameworks\". "
            "[8] IETF RFC 5280: \"Internet X.509 Public Key Infrastructure Certificate and Certificate "
            "Revocation List (CRL) Profile\". "
            "[9] ETSI EN 319 401: \"Electronic Signatures and Trust Infrastructures (ESI); General Policy "
            "Requirements for Trust Service Providers\". "
            "[10] ETSI EN 319 412-2: \"Electronic Signatures and Infrastructures (ESI); Certificate Profiles; "
            "Part 2: Certificate profile for certificates issued to natural persons\". "
            "[11] ETSI EN 319 412-3: \"Electronic Signatures and Infrastructures (ESI); Certificate Profiles; "
            "Part 3: Certificate profile for certificates issued to legal persons\". "
            "[12] IETF RFC 6960: \"X.509 Internet Public Key Infrastructure Online Certificate Status "
            "Protocol-OCSP\". "
            "[13] FIPS PUB 140-2 (2001): \"Security Requirements for Cryptographic Modules\". "
            "[14] ETSI EN 319 412-1: \"Electronic Signatures and Infrastructures (ESI); Certificate Profiles; "
            "Part 1: Overview and common data structures\". "
            "[15] ETSI TS 119 461: \"Electronic Signatures and Infrastructures (ESI); Policy and security "
            "requirements for trust service components providing identity proofing of trust service "
            "subjects\". "
            "[16] FIPS PUB 140-3 (2019): \"Security Requirements for Cryptographic Modules\"."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 2.2 (Informative references)",
        "testo": (
            "Elenco dei 23 riferimenti informativi (non necessari all'applicazione ma di ausilio, citati "
            "con [i.N]; [i.13] e' 'Void'): Direttiva 1999/93/EC, ETSI EN 319 403, IETF RFC 3647, ISO 19005, "
            "ETSI EN 319 411-2, ETSI TS 102 042, ISO/IEC 27002:2013, ISO/IEC 7498-2/ITU-T X.800, TS 419261, "
            "ETSI TS 119 312, IETF RFC 5246, ETSI TS 119 612, Regolamento (UE) 910/2014, ETSI EN 319 421, "
            "TS 419221-2/-3/-4, EN 419221-5, ETSI TR 119 411-4, ETSI TS 119 431-1, ETSI TS 119 511, IETF RFC "
            "9608."
        ),
        "testo_integrale": (
            "2.2 Informative references: References are either specific (identified by date of publication "
            "and/or edition number or version number) or non-specific. For specific references, only the "
            "cited version applies. For non-specific references, the latest version of the referenced "
            "document (including any amendments) applies. The following referenced documents are not "
            "necessary for the application of the present document but they assist the user with regard to "
            "a particular subject area. NOTE: While any hyperlinks included in this clause were valid at the "
            "time of publication, ETSI cannot guarantee their long term validity. "
            "[i.1] Directive 1999/93/EC of the European Parliament and of the Council of 13 December 1999 on "
            "a Community framework for electronic signatures. "
            "[i.2] ETSI EN 319 403: \"Electronic Signatures and Infrastructures (ESI); Trust Service Provider "
            "Conformity Assessment-Requirements for conformity assessment bodies assessing Trust Service "
            "Providers\". "
            "[i.3] IETF RFC 3647: \"Internet X.509 Public Key Infrastructure-Certificate Policy and "
            "Certification Practices Framework\". "
            "[i.4] ISO 19005 (parts 1 to 3): \"Document management — Electronic document file format for "
            "long-term preservation\". "
            "[i.5] ETSI EN 319 411-2: \"Electronic Signatures and Infrastructures (ESI); Policy and security "
            "requirements for Trust Service Providers issuing certificates; Part 2: Requirements for trust "
            "service providers issuing EU qualified certificates\". "
            "[i.6] ETSI TS 102 042: \"Electronic Signatures and Infrastructures (ESI); Policy requirements "
            "for certification authorities issuing public key certificates\". "
            "[i.7] ISO/IEC 27002:2013: \"Information technology — Security techniques — Code of practice "
            "for information security management\". "
            "[i.8] ISO/IEC 7498-2/Recommendation ITU-T X.800: \"Data communications network — Open systems "
            "interconnection — Security, structure and applications: Security architecture for open systems "
            "interconnection for CCITT applications\". "
            "[i.9] TS 419261: \"Security requirements for trustworthy systems managing certificates and "
            "time-stamps\", (produced by CEN). "
            "[i.10] ETSI TS 119 312: \"Electronic Signatures and Trust Infrastructures (ESI); Cryptographic "
            "Suites\". "
            "[i.11] IETF RFC 5246: \"The Transport Layer Security Protocol Version 1.2\". "
            "[i.12] ETSI TS 119 612: \"Electronic Signatures and Trust Infrastructures (ESI); Trusted "
            "Lists\". "
            "[i.13] Void. "
            "[i.14] Regulation (EU) No 910/2014 of the European Parliament and of the Council of 23 July "
            "2014 on electronic identification and trust services for electronic transactions in the "
            "internal market and repealing Directive 1999/93/EC. "
            "[i.15] ETSI EN 319 421: \"Electronic Signatures and Trust Infrastructures (ESI); Policy and "
            "Security Requirements for Trust Service Providers issuing Time-Stamps\". "
            "[i.16] TS 419221-2: \"Protection Profiles for TSP cryptographic modules-Part 2: Cryptographic "
            "module for CSP signing operations with backup\", (produced by CEN). "
            "[i.17] TS 419221-3: \"Protection Profiles for TSP Cryptographic modules-Part 3: Cryptographic "
            "module for CSP key generation services\", (produced by CEN). "
            "[i.18] TS 419221-4: \"Protection Profiles for TSP cryptographic modules-Part 4: Cryptographic "
            "module for CSP signing operations without backup\", (produced by CEN). "
            "[i.19] EN 419221-5: \"Protection Profiles for TSP Cryptographic modules-Part 5: Cryptographic "
            "module for Trust Services\", (produced by CEN). "
            "[i.20] ETSI TR 119 411-4: \"Electronic Signatures and Trust Infrastructures (ESI); Policy and "
            "security requirements for Trust Service Providers issuing certificates; Part 4: Checklist "
            "supporting audit of TSP against ETSI EN 319 411-1 or ETSI EN 319 411-2\". "
            "[i.21] ETSI TS 119 431-1: \"Electronic Signatures and Trust Infrastructures (ESI); Policy and "
            "security requirements for trust service providers; Part 1: TSP service components operating a "
            "remote QSCD / SCDev\". "
            "[i.22] ETSI TS 119 511: \"Electronic Signatures and Infrastructures (ESI); Policy and security "
            "requirements for trust service providers providing long-term preservation of digital signatures "
            "or general data using digital signature techniques\". "
            "[i.23] IETF RFC 9608: \"No Revocation Available for X.509 Public Key Certificates\"."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 3.1 (Terms)",
        "testo": (
            "Glossario di 29 termini specifici del documento (oltre a quelli gia' definiti in ETSI EN 319 "
            "401), raggruppabili per area: (i) ruoli - 'auditor', 'Registration Authority (RA)', "
            "'registration officer', 'revocation officer'; (ii) certificati e loro ciclo di vita - "
            "'certificate', 'Certificate Policy (CP)', 'Certificate Revocation List (CRL)', 'Certification "
            "Authority (CA)', 'Certification Authority Revocation List (CARL)', 'Certification Practice "
            "Statement (CPS)', 'cross certificate', 'Domain/Individual/Organizational Validation Certificate "
            "(DVC/IVC/OVC)', 'EV certificate'/'Extended Validation Certificate (EVC)', 'Publicly-Trusted "
            "Certificate', 'root CA', 'subordinate CA', 'short-term certificate', 'subject', 'revocation'; "
            "(iii) infrastruttura tecnica - 'digital signature', 'domain name', 'high security zone', "
            "'secure cryptographic device', 'secure zone', 'trust anchor'; (iv) tempo - 'Coordinated "
            "Universal Time (UTC)' (per rinvio a ETSI EN 319 401). Le definizioni sono per lo piu' brevi con "
            "NOTE numerate che rinviano a norme correlate (ISO/IEC 9594-8/X.509, IETF RFC 3647/5280, "
            "ISO/IEC 7498-2/X.800) o chiariscono il perimetro (es. CA come TSP o come servizio tecnico di "
            "generazione certificati per conto di un altro certification service provider)."
        ),
        "testo_integrale": (
            "3.1 Terms: For the purposes of the present document, the terms given in ETSI EN 319 401 [9] and "
            "the following apply: "
            "auditor: person who assesses conformity to requirements as specified in given requirements "
            "documents NOTE: See ETSI EN 319 403 [i.2]. "
            "certificate: public key of a user, together with some other information, rendered un-forgeable "
            "by encipherment with the private key of the certification authority which issued it NOTE 1: The "
            "term certificate is used for public key certificate within the present document. NOTE 2: See "
            "ISO/IEC 9594-8/Recommendation ITU-T X.509 [7]. "
            "Certificate Policy (CP): named set of rules that indicates the applicability of a certificate "
            "to a particular community and/or class of application with common security requirements NOTE 1: "
            "See clause 4.2 for explanation of the relative role of certificate policies and certification "
            "practice statement. NOTE 2: This is a specific type of trust service policy as specified in "
            "ETSI EN 319 401 [9]. NOTE 3: See ISO/IEC 9594-8/Recommendation ITU-T X.509 [7]. "
            "Certificate Revocation List (CRL): signed list indicating a set of certificates that have been "
            "revoked by the certificate issuer NOTE 1: Within the scope of the present document the set of "
            "certificates is related to end user certificates. NOTE 2: See ISO/IEC 9594-8/Recommendation "
            "ITU-T X.509 [7]. "
            "Certification Authority (CA): authority trusted by one or more users to create and assign "
            "certificates NOTE 1: A CA can be: 1) a trust service provider that creates and assigns public "
            "key certificates; or 2) a technical certificate generation service that is used by a "
            "certification service provider that creates and assign public key certificates. NOTE 2: See "
            "ISO/IEC 9594-8/Recommendation ITU-T X.509 [7]. "
            "Certification Authority Revocation List (CARL): revocation list containing a list of "
            "CA-certificates issued to certification authorities that have been revoked by the certificate "
            "issuer NOTE: See ISO/IEC 9594-8/Recommendation ITU-T X.509 [7]. "
            "Certification Practice Statement (CPS): statement of the practices which a Certification "
            "Authority employs in issuing managing, revoking, and renewing or re-keying certificates NOTE 1: "
            "See IETF RFC 3647 [i.3]. NOTE 2: This is a specific type of Trust Service practice statement as "
            "specified in ETSI EN 319 401 [9]. "
            "Coordinated Universal Time (UTC): As indicated in ETSI EN 319 401 [9]. "
            "cross certificate: certificate that is used to establish a trust relationship between two "
            "certification authorities. "
            "digital signature: data appended to, or a cryptographic transformation of a data unit that "
            "allows a recipient of the data unit to prove the source and integrity of the data unit and "
            "protect against forgery e.g. by the recipient NOTE: See ISO/IEC 7498-2/Recommendation ITU-T "
            "X.800 [i.8]. "
            "domain name: label assigned to a node in the Domain Name System NOTE: See BRG [5]. "
            "Domain Validation Certificate (DVC): certificate which has no validated organizational identity "
            "information for the subject, only identifying the subject by its domain name. "
            "EV certificate: See Extended Validation Certificate. "
            "Extended Validation Certificate (EVC): As indicated in the EVCG [4]. "
            "high security zone: specific physical location of the security zone where the Root CA key is "
            "held NOTE: See ETSI EN 319 401 [9], clause 7.8. "
            "Individual Validation Certificate (IVC): certificate that includes validated individual "
            "identity information for the subject. "
            "Organizational Validation Certificate (OVC): certificate that includes validated organizational "
            "identity information for the subject. "
            "Publicly-Trusted Certificate: certificate that is trusted by virtue of the fact that its "
            "corresponding Root Certificate is distributed as a trust anchor in widely-available application "
            "software. "
            "Registration Authority (RA): entity that is responsible for identification and authentication "
            "of subjects of certificates mainly NOTE 1: An RA can assist in the certificate application "
            "process or revocation process or both. NOTE 2: See IETF RFC 3647 [i.3]. "
            "registration officer: person responsible for verifying information that is necessary for "
            "certificate issuance and approval of certification requests. "
            "revocation: permanent termination of the certificate's validity before the expiry date "
            "indicated in the certificate. "
            "revocation officer: person responsible for operating certificate status changes ISO/IEC "
            "7498-2/Recommendation ITU-T X.800 [i.8]. "
            "root CA: certification authority which is at the highest level within TSP's domain and which is "
            "used to sign subordinate CA(s) NOTE 1: A Root CA certificate is generally self-signed but the "
            "Root-CA can also be certified by a (Root) CA from another domain (e.g. cross-certification, "
            "Root-Signed in the context of a root-signing program, etc.). NOTE 2: A Root CA can be used as "
            "the Trust Anchor for many applications (e.g. browsers) but nothing prevents the TSP to present "
            "subordinate CAs for this purpose, according to the business context. "
            "secure cryptographic device: device which holds the user's private key, protects this key "
            "against compromise and performs signing or decryption functions on behalf of the user. "
            "secure zone: area (physical or logical) protected by physical and logical controls that "
            "appropriately protect the confidentiality, integrity, and availability of the systems used by "
            "the TSP. "
            "short-term certificate: certificate whose validity period, i.e. the period of time from "
            "notBefore through notAfter, inclusive, is shorter than the maximum time to process a revocation "
            "request as specified in the certificate practice statement NOTE: Validity period as defined by "
            "IETF RFC 5280 [8]. "
            "subject: entity identified in a certificate as the holder of the private key associated with "
            "the public key given in the certificate NOTE: Relationship between subscriber and subject is "
            "described in clauses 5.4.2 and 6.3.5. "
            "subordinate CA: certification authority whose Certificate is signed by the Root CA, or another "
            "Subordinate CA NOTE: A subordinate CA normally either issues end user certificates or other "
            "subordinate CA certificates. "
            "trust anchor: entity that is trusted by a relying party and used for validating certificates in "
            "certification paths NOTE 1: See ISO/IEC 9594-8/Recommendation ITU-T X.509 [7]. NOTE 2: A Trust "
            "Anchor can also be a Root CA. NOTE 3: Examples of trust anchors are as in a trusted list (ETSI "
            "TS 119 612 [i.12]) or a list of trusted CA certificates distributed by an application software "
            "provider."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 3.2 (Symbols)",
        "testo": "La clausola dei simboli e' vuota: nessun simbolo specifico e' definito per il documento.",
        "testo_integrale": "3.2 Symbols: Void.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 3.3 (Abbreviations)",
        "testo": (
            "La clausola elenca 47 abbreviazioni specifiche del documento: AIA, BRG, CA, CAB Forum, CARL, "
            "CP, CPS, CRL, CSP (con NOTA che preferisce il termine generico Trust Service Provider tranne "
            "nei rinvii esterni), CSS, DIS, DV, DVC, DVCP, EAL, eID, EV, EVC, EVCG, EVCP, FIPS, GEN, IVC, "
            "IVCP, LCP, NCP, NCP+, OCSP, OID, OV, OVC, OVCP, OVR, PDF/A, PDS, PIN, PKI, RA, REG, REQ, REV, "
            "SDP, SSL, TLS, TLS/SSL, TSP, UTC."
        ),
        "testo_integrale": (
            "3.3 Abbreviations: For the purposes of the present document, the following abbreviations "
            "apply: "
            "AIA Authority Information Access; "
            "BRG Baseline Requirements Guidelines; "
            "CA Certification Authority; "
            "CAB Forum CA/Browser Forum; "
            "CARL Certification Authority Revocation List; "
            "CP Certificate Policy; "
            "CPS Certification Practice Statement; "
            "CRL Certificate Revocation List; "
            "CSP Certification Service Provider NOTE: The more general term Trust Service Provider is used "
            "in preference to CSP in the present document except in relation to external references; "
            "CSS Certificate Status Service; "
            "DIS DIssemination Services; "
            "DV Domain Validated; "
            "DVC Domain Validation Certificate; "
            "DVCP Domain Validation Certificate Policy; "
            "EAL Evaluation Assurance Level; "
            "eID Electronic IDentity; "
            "EV Extended Validation; "
            "EVC Extended Validation Certificate; "
            "EVCG Extended Validation Certificate Guidelines; "
            "EVCP Extended Validation Certificate Policy; "
            "FIPS Federal Information Processing Standard; "
            "GEN Certificate Generation Services; "
            "IVC Individual Validation Certificate; "
            "IVCP Individual Validation Certificate Policy; "
            "LCP Lightweight Certificate Policy; "
            "NCP Normalized Certificate Policy; "
            "NCP+ Extended Normalized Certificate Policy; "
            "OCSP Online Certificate Status Protocol; "
            "OID Object IDentifier; "
            "OV Organizational Validated; "
            "OVC Organizational Validation Certificate; "
            "OVCP Organizational Validation Certificate Policy; "
            "OVR General Requirement; "
            "PDF/A Portable Document Format/Archive; "
            "PDS PKI Disclosure Statement; "
            "PIN Personal Identification Number; "
            "PKI Public Key Infrastructure; "
            "RA Registration Authority; "
            "REG Registration Services; "
            "REQ Requirement; "
            "REV Revocation Services; "
            "SDP Subject Device Provisioning; "
            "SSL Secure Socket Layer; "
            "TLS Transport Layer Security; "
            "TLS/SSL Transport Layer Security/Secure Socket Layer protocol; "
            "TSP Trust Service Provider; "
            "UTC Coordinated Universal Time. "
            "NOTE: IETF RFC 5246 [i.11] or earlier equivalent Secure Socket Layer protocol."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: clausola 3.4 (Notations)",
        "testo": (
            "Clausola normativa che definisce lo schema di lettura di tutti i requisiti del documento. I "
            "requisiti includono: a) requisiti applicabili a qualunque CP (nessuna marcatura aggiuntiva); "
            "b) requisiti applicabili a certe condizioni (marcatura '[CONDITIONAL]'); c) requisiti con piu' "
            "opzioni tra cui scegliere (marcatura '[CHOICE]'); d) requisiti applicabili ai servizi offerti "
            "secondo la CP applicabile (marcature '[LCP]', '[NCP]', '[NCP+]', '[EVCP]', '[OVCP]', '[IVCP]', "
            "'[DVCP]'); e) requisiti marcati '[WEB]' applicabili alle CP per certificati di autenticazione "
            "web che si basano sul documento, comuni ai certificati web-authentication generici, che rinviano "
            "ai requisiti BRG. Ogni requisito e' identificato dallo schema <3 lettere componente di "
            "servizio>-<numero di clausola>-<numero progressivo a 2 cifre>. I componenti di servizio sono: "
            "OVR (requisito generale applicabile a piu' di un componente), GEN (Certificate Generation "
            "Services), REG (Registration Services), REV (Revocation Services), DIS (Dissemination "
            "Services), SDP (Subject Device Provisioning), CSS (Certificate Status Service). Per le edizioni "
            "successive del documento: un requisito inserito a fine clausola incrementa il numero progressivo "
            "a 2 cifre; un requisito inserito tra due requisiti esistenti e' distinto con lettere maiuscole "
            "accodate all'identificativo del requisito precedente; l'identificativo di un requisito eliminato "
            "resta e viene completato con 'Void'; l'identificativo di un requisito modificato resta vuoto e "
            "il requisito modificato e' identificato con lettere maiuscole accodate al numero del requisito "
            "iniziale."
        ),
        "testo_integrale": (
            "3.4 Notations: The requirements identified in the present document include: "
            "a) requirements applicable to any CP. Such requirements are indicated by clauses without any "
            "additional marking; "
            "b) requirements applicable under certain conditions. Such requirements are indicated by clauses "
            "marked by \"[CONDITIONAL]\"; "
            "c) requirements that include several choices which ought to be selected according to the "
            "applicable situation. Such requirements are indicated by clauses marked by \"[CHOICE]\"; "
            "d) requirements applicable to the services offered under the applicable CP. Such requirements "
            "are indicated by clauses marked by the applicable CP as follows \"[LCP]\", \"[NCP]\", \"[NCP+]\", "
            "\"[EVCP]\", \"[OVCP]\", \"[IVCP]\" and \"[DVCP]\"; "
            "e) [WEB] tagged requirements are applicable to CPs for web-authentication certificates building "
            "on the present document. These requirements are common to web-authentication certificates for "
            "general purpose. They relate to common topics and refer to requirements in BRG [5]. "
            "Incorporating [WEB] requirements in a policy for SSL/TLS certificates built on the present "
            "document does not necessarily require following the full and latest version of BRG [6], but "
            "requires following the selected requirements from version of BRG as stated in the normative "
            "reference [5]. "
            "Each requirement is identified as follows: <3 letters service component>-<the clause number>-"
            "<2 digit number incremental>. The service components are: "
            "- OVR: General requirement (requirement applicable to more than 1 component); "
            "- GEN: Certificate Generation Services; "
            "- REG: Registration Services; "
            "- REV: Revocation Services; "
            "- DIS: Dissemination Services; "
            "- SDP: Subject Device Provisioning; "
            "- CSS: Certificate Status Service. "
            "The management of the requirement identifiers for subsequent editions of the present document "
            "is as follows: "
            "- When a requirement is inserted at the end of a clause, the 2 digit number above is "
            "incremented to the next available digit. "
            "- When a requirement is inserted between two existing requirements, capital letters appended to "
            "the previous requirement identifier are used to distinguish new requirements. "
            "- The requirement identifier for a deleted requirement is left and completed with \"Void\". "
            "- The requirement identifier for a modified requirement is left void and the modified "
            "requirement is identified by capital letter(s) appended to the initial requirement number."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Parte 1: clausola 1 (Scope)",
    "Parte 1: clausola 2.1 (Normative references)",
    "Parte 1: clausola 2.2 (Informative references)",
    "Parte 1: clausola 3.1 (Terms)",
    "Parte 1: clausola 3.2 (Symbols)",
    "Parte 1: clausola 3.3 (Abbreviations)",
    "Parte 1: clausola 3.4 (Notations)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))
    from lib import verifica_copertura, verifica_completezza_testo_integrale

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    verifica_completezza_testo_integrale([sys.modules["__main__"]])
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
