"""ETSI TS 119 612 V2.4.1 (2025-08) - Electronic Signatures and Trust
Infrastructures (ESI); Trusted Lists.
Fonte 21 (la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 4 del
manifest: clausola 5.5.9 Service information extensions (5.5.9.0 General,
5.5.9.1 expiredCertsRevocationInfo Extension, 5.5.9.2 Qualifications Extension
con 5.5.9.2.0 General, 5.5.9.2.1 QualificationElement, 5.5.9.2.2 CriteriaList
con 5.5.9.2.2.0 General, 5.5.9.2.2.1 KeyUsage, 5.5.9.2.2.2 PolicySet,
5.5.9.2.2.3 OtherCriteria e 5.5.9.2.3 Qualifier, 5.5.9.3 TakenOverBy
Extension, 5.5.9.4 additionalServiceInformation Extension), clausola 5.5.10
Service history, clausola 5.6 Service history instance (5.6.1-5.6.6) e
clausola 5.7 Digital signature (5.7.1-5.7.3). Testo ufficiale in
app/.source_cache/etsi_119_612/cap04.txt (letto sempre con selettore `:raw`,
altrimenti il tool tronca le righe lunghe a 768 caratteri introducendo "..."
e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_119_612/manifest.json.

Modellazione (ADR-0007), stesso criterio dei capitoli cap01-cap03 di questa
fonte e delle altre fonti ETSI censite: un nodo per ogni
clausola/sottoclausola numerata con contenuto proprio, nessun discrimine di
rilevanza. Il capitolo produce 21 Obblighi e 1 Principio su 22 item di indice.

Intestazioni di puro raggruppamento, senza nodo (nessun periodo proprio nel
testo ufficiale, seguono immediatamente la prima sottoclausola): 5.5.9.2
(Qualifications Extension), 5.5.9.2.2 (CriteriaList), 5.6 (Service history
instance) e 5.7 (Digital signature).

Eccezione motivata: 5.5.9 (Service information extensions) -> 1 nodo Principio
"altro", creato su richiesta esplicita della sessione principale per renderlo
citabile come target dei rinvii cross-capitolo (annex D in cap06, annex J in
cap08 e la clausola 5.6.6 di questo stesso capitolo). Il testo ufficiale non
associa alla clausola alcun periodo proprio, quindi `testo_integrale` riporta
verbatim la sola intestazione e la sintesi `testo` documenta il
raggruppamento e le quattro estensioni predefinite. Alternative scartate:
nessun nodo (avrebbe reso irrisolvibili per stringa i rinvii di altri
capitoli) e accorpamento con 5.5.9.0 (avrebbe duplicato il testo del campo).
Nessun altro nodo di raggruppamento e' stato creato.

Classificazione: tutte le sottoclausole del capitolo sono clausole di campo
(Presence/Description/Format/Value) e portano "shall"/"shall not" - o
"should"/"may" espliciti che enunciano una facolta'/comportamento del soggetto
(TLSO/scheme operator) - quindi sono Obblighi (criterio del brief: lo schema
ha un solo tipo prescrittivo). In particolare sono Obblighi anche le
sottoclausole formalmente definitorie 5.5.9.2.1 e 5.5.9.2.2.0, perche'
contengono "This field shall be present" e "the description shall be expressed
in UK English". L'unico Principio del capitolo e' il nodo di raggruppamento
5.5.9 (tipo_principio "altro"); nessuna clausola e' risultata puramente
dichiarativa.

Tipo di obbligo, voce per voce (scelte non ovvie):
- "informativo/trasparenza" per le clausole il cui nucleo prescrittivo e' il
  veicolare/registrare una informazione nella TL (5.5.9.0, 5.5.9.2.3,
  5.5.9.4, 5.5.10, 5.6.1-5.6.6). Per 5.5.9.2.3 (Qualifier) l'alternativa
  "tecnico/sicurezza" e' stata scartata: i qualificatori dichiarano
  proprieta' dei certificati nella TL, mentre il divieto d'uso fuori dal tipo
  "CA/QC" e' una condizione di applicabilita' del campo.
- "tecnico/sicurezza" per le clausole che vincolano formato/crittografia del
  contenuto (5.5.9.1, 5.5.9.2.0, 5.5.9.2.1, 5.5.9.2.2.0-5.5.9.2.2.3,
  5.7.1-5.7.3).
- "procedurale" per 5.5.9.3 (TakenOverBy): il nucleo prescrittivo non e' il
  formato dell'estensione ma la condotta del TLSO sul subentro (voce di
  servizio non copiata ne' spostata, trust state mantenuto aggiornato, nuova
  voce in caso di nuova identita' digitale, mantenimento dello stato del
  servizio precedente fino a cessazione).
- 5.5.10 e' stata classificata "informativo/trasparenza" e non "di
    conservazione": la clausola non impone la conservazione di documenti ma la
  pubblicazione della storia degli stati nella TL.

Mappa completa voce per voce (riferimento -> tipo_obbligo):
  5.5.9.0 General -> informativo/trasparenza; 5.5.9.1 expiredCertsRevocationInfo
  Extension -> tecnico/sicurezza; 5.5.9.2.0 General -> tecnico/sicurezza;
  5.5.9.2.1 QualificationElement -> tecnico/sicurezza; 5.5.9.2.2.0 General ->
  tecnico/sicurezza; 5.5.9.2.2.1 KeyUsage -> tecnico/sicurezza; 5.5.9.2.2.2
  PolicySet -> tecnico/sicurezza; 5.5.9.2.2.3 OtherCriteria ->
  tecnico/sicurezza; 5.5.9.2.3 Qualifier -> informativo/trasparenza; 5.5.9.3
  TakenOverBy Extension -> procedurale; 5.5.9.4 additionalServiceInformation
  Extension -> informativo/trasparenza; 5.5.10 Service history ->
  informativo/trasparenza; 5.6.1-5.6.6 -> informativo/trasparenza (5.6.2
  contiene l'unica NOTE del capitolo, riportata in `testo_integrale`);
  5.7.1 Digitally signed Trusted List -> tecnico/sicurezza; 5.7.2 Digital
  signature algorithm identifier -> tecnico/sicurezza; 5.7.3 Digital signature
  value -> tecnico/sicurezza. Unico Principio: 5.5.9 -> "altro".

Soggetti: il soggetto obbligato tipico e' il Trusted List Scheme Operator
(TLSO), censito come "QTSP/gestore" (ruolo "obbligato") - il vocabolario
chiuso non prevede una categoria per lo scheme/Stato membro. In 5.5.9.2.3 il
testo nomina anche MS Scheme Operator e organismi di vigilanza/accreditamento
(Autorita' di Vigilanza): mappati anch'essi su "QTSP/gestore" per assenza di
categoria dedicata, con il ruolo effettivo esplicitato in `testo`. Le clausole
che nominano espressamente parti affidanti, sottoscrittori o l'utente finale
(5.5.9.0, 5.5.9.3, 5.5.9.4, 5.7.1) portano in aggiunta il soggetto
"Terzi affidanti/pubblico" con ruolo "destinatario". `condizione_applicabilita`
e' valorizzata dove il testo la enuncia in modo esplicito (5.5.9.1, 5.5.9.2.0,
5.5.9.3, 5.5.10). `severita`/`sanzioni` restano None (standard tecnico,
nessuna sanzione). `stato` sempre "vigente".

Convenzioni di trascrizione applicate a `testo_integrale` (nessuna incide sul
contenuto normativo, nessuna parola rimossa: per ogni clausola il conteggio
delle parole del file sorgente e' stato confrontato con quello del paragrafo
ricomposto):
- i wrap fisici di riga introdotti da pdftotext -layout sono ricomposti in
  paragrafi (separati da riga vuota), come gia' fatto per ETSI TS 119 432;
- i marcatori di pagina `<!-- Page N -->` (paratesto della conversione) sono
  rimossi;
- il padding dei label di campo ("Presence:", "Description:", "Format:",
  "Value:", "NOTE:") e' normalizzato a un solo spazio;
- il glifo privato U+F0A7 (pallino di elenco in font Symbol prodotto dalla
  conversione) e' normalizzato al pallino "•", stessa convenzione di ETSI TS
  119 432;
- in 5.5.9.2.3 l'URI del qualificatore QCSSCDStatusAsInCert era spezzato dal
  PDF su due righe (".../SvcInfoExt/ QCSSCDStatusAsInCert"): le due meta' sono
  state ricongiunte senza spazio, perche' lo spazio e' un artefatto di layout e
  avrebbe mutilato l'URI. Tutte le altre coppie qualificatore-URI e gli altri
  elenchi di URI sono rimasti identici al sorgente;
- in 5.5.9.1 la coppia di URI che il PDF presenta nella stessa voce di elenco
  (Certstatus/OCSP e Certstatus/OCSP/QC, cosi' come Certstatus/CRL e
  Certstatus/CRL/QC) e' mantenuta nella stessa voce, senza separarla in due
  item di elenco inesistenti nel testo ufficiale;
- il blocco ASN.1 degli OID id-tsl/id-tsl-kp/id-tsl-kp-tslSigning in 5.7.1 e'
  contenuto normativo autentico ed e' riportato verbatim;
- l'unica NOTE del capitolo (in 5.6.2) e' inclusa in `testo_integrale` e
  richiamata nella sintesi; gli EXAMPLES di 5.5.9.4 sono contenuto
  interpretativo sostanziale (granularita' RGS, "qualified TST" nazionale,
  campo "Sdi") e sono riportati integralmente.

Nessun marcatore di elisione in questo capitolo: non contiene ne' ellissi
autentiche (il caso noto di questo documento e' confinato all'annex D) ne'
((...)).

RELAZIONI: 40 relazioni, tutte "richiama", tutte da riscontri testuali
puntuali e tutte interne a ETSI TS 119 612 (fonte_id None). Le stringhe dei
nodi di destinazione appartenenti ad altri capitoli sono state concordate via
`hub` con i rispettivi autori in parallelo: 5.1.3, 5.3.4, 5.3.9, 5.3.10,
5.3.12 (cap02); 5.4.1, 5.5.1.0, 5.5.2, 5.5.3, 5.5.4, 5.5.5 (cap03);
Annex B.0 (cap05); Annex C, Annex D.3, Annex D.4, Annex D.5 (cap06), con il
tipo di nodo (obbligo/principio) comunicato da cap06.
Attenzione ai riferimenti del testo ufficiale che cadono su intestazioni di
raggruppamento prive di nodo: "clause 5.5.1" e' risolto su "clausola 5.5.1.0
(General requirements)", "clause 5.6" su "clausola 5.6.1 (Service type
identifier)", "see clause 5.6" in 5.5.10 su 5.6.1, "clause 5.5.9" in 5.6.6 sul
nodo 5.5.9 di questo capitolo, "see clause 5.5.9.2" in 5.5.9.0 su "clausola
5.5.9.2.0 (General)", "requirements as stated in annex B" in 5.7.1 su "Annex
B.0 (General requirements)" (l'intestazione "Annex B (normative):
Implementation in XML" non ha testo proprio).
Citazioni esterne notate ma NON trasformate in relazioni (collegamento
cross-fonte demandato alla Fase 6 della sessione principale, ADR-0009):
ETSI EN 319 132-1 [3] (formato XAdES-B-B della firma della TL), ETSI TS 119
312 [2] (tabelle 4, 6 e 7, requisiti di sicurezza per chiavi utilizzabili
almeno 3 anni), ISO/IEC 9594-8 [i.12] (estensione expiredCertsOnCRL e clausola
8.5.2.12), IETF RFC 5280 [12] (metodi SubjectKeyIdentifier), IETF RFC 6960
[i.11] (estensione ArchiveCutoff), Recommendation ITU-T X.509 [1] (KeyUsage ed
ExtendedKeyUsage), QcCompliance [i.9] e OID QCP/QCP+ [i.5] (qualificatori).
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 5.5.9.0 (General)",
        "testo": (
            "Il campo 'Service information extensions' della Service information e' opzionale: specifica "
            "informazioni relative al servizio come sequenza di estensioni informative di servizio, ciascuna "
            "formattata secondo le sottoclausole seguenti e ciascuna selezionabile dal TLSO in base al "
            "significato e alle informazioni che intende o deve veicolare nella propria TL. Le estensioni "
            "predefinite riguardano: il tempo dal quale un servizio fiduciario elencato che crea e firma CRL o "
            "risposte OCSP conserva gli avvisi di revoca anche dopo la scadenza dei certificati (clausola "
            "5.5.9.1); le informazioni sulle caratteristiche dei certificati qualificati (natura qualificata, "
            "emissione a persona giuridica, residenza o meno della chiave privata in SSCD o QSCD) create e "
            "firmate da un servizio elencato quando tali informazioni non sono parte dei certificati (clausola "
            "5.5.9.2); le informazioni sul subentro di un TSP diverso da quello identificato dal TSP Name "
            "(clausola 5.4.1) nella titolarita' del servizio, con identificazione del TSP subentrante, processo "
            "di subentro e conseguenze per sottoscrittori e parti affidanti (clausola 5.5.9.3); informazioni "
            "aggiuntive di servizio (clausola 5.5.9.4)."
        ),
        "testo_integrale": (
            """Presence: This field is optional.

Description: It specifies specific service-related information.

Format: Sequence of service information extensions, each of which is formatted as specified in next clauses and each of which may be selected by the TLSO according to the meaning and information it wishes or needs to convey within its TL.

Value: Pre-defined extensions are specified in next clauses with regards to:

-    indication of the time from which a listed trust service creating and signing CRLs or signed OCSP responses keeps revocation notices for revoked certificates also after they have expired (see clause 5.5.9.1);

-    information provided on characteristics of qualified certificates (i.e. qualified certificate nature, issuance to legal person, corresponding private key residing or not in an SSCD or in a QSCD) created and signed by a listed trust service when such information is not part of the certificates (see clause 5.5.9.2);

-    information on the taking over of a listed trust service by another trust service provider than the one identified by the TSP Name (clause 5.4.1), including the identification of the taking over trust service provider, the taking over process and its consequences on subscribers and relying parties (see clause 5.5.9.3);

-    additional service information (see clause 5.5.9.4)."""
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.5.9.1 (expiredCertsRevocationInfo Extension)",
        "testo": (
            "Estensione 'expiredCertsRevocationInfo': campo opzionale, presente solo se usato con i 'Service "
            "types' CA/PKC, CA/QC, NationalRootCA-QC, Certstatus/OCSP, Certstatus/OCSP/QC, Certstatus/CRL, "
            "Certstatus/CRL/QC e altri tipi di servizio applicabili definiti dal TLSO ai sensi della clausola "
            "D3; non va usata con altri tipi e non va impostata come critica. L'estensione svolge la stessa "
            "funzione della clausola 8.5.2.12 di ISO/IEC 9594-8 e indica: che il perimetro di ogni CRL e "
            "risposta OCSP emessa dal servizio cui l'estensione si applica e' esteso a includere lo stato di "
            "revoca dei certificati scaduti al momento indicato nell'estensione o successivamente; che lo stato "
            "di revoca di un certificato non viene aggiornato dopo la scadenza (comportamento consentito da "
            "ISO/IEC 9594-8 e IETF RFC 5280); e che eventuali limitazioni del perimetro della CRL (per reason "
            "code o distribution point) valgono anche per i certificati scaduti. Formato: valore data-ora "
            "(clausola 5.1.3). Se una CRL contiene l'estensione expiredCertsOnCRL definita in ISO/IEC 9594-8, "
            "questa prevale sul valore dell'estensione di TL ma solo per quella specifica CRL; analogamente, se "
            "una risposta OCSP contiene l'estensione ArchiveCutoff della sezione 4.4.4 di IETF RFC 6960, questa "
            "prevale ma solo per quella specifica risposta OCSP."
        ),
        "testo_integrale": (
            """Presence: This field is optional but may only be present when used with the following 'Service types' (clause 5.5.1):

-    "http://uri.etsi.org/TrstSvc/Svctype/CA/PKC";

-    "http://uri.etsi.org/TrstSvc/Svctype/CA/QC";

-    "http://uri.etsi.org/TrstSvc/Svctype/NationalRootCA-QC";

-    "http://uri.etsi.org/TrstSvc/Svctype/Certstatus/OCSP"; "http://uri.etsi.org/TrstSvc/Svctype/Certstatus/OCSP/QC";

-    "http://uri.etsi.org/TrstSvc/Svctype/Certstatus/CRL"; "http://uri.etsi.org/TrstSvc/Svctype/Certstatus/CRL/QC";

-    other applicable service types defined by the TLSO in accordance with clause D3.

It shall not be used with other types.

This extension shall not be set critical.

Description: This extension supports the same function as in ISO/IEC 9594-8 [i.12], clause 8.5.2.12.

It indicates:

-    that the scope of each CRL and OCSP response, issued by the service to which this extension applies, is extended to include the revocation status of certificates that expired at the exact time specified in the extension or after that time;

-    that the revocation status of a certificate will not be updated once the certificate has expired (this behaviour being openly allowed by ISO/IEC 9594-8 [i.12] and IETF RFC 5280 [12]); and

-    that if limitations in the CRL's scope are specified (by either reason codes or by distribution points), they apply to expired certificates as well.

Format: Date-time value (see clause 5.1.3).

Value: If a CRL contains the extension expiredCertsOnCRL defined in [i.12], it shall prevail over the TL extension value but only for that specific CRL.

If an OCSP response contains the extension ArchiveCutoff defined in section 4.4.4 of IETF RFC 6960 [i.11], it shall prevail over the TL extension value but only for that specific OCSP response."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": "Campo opzionale: utilizzabile solo con i 'Service types' elencati (CA/PKC, CA/QC, NationalRootCA-QC, Certstatus/OCSP, Certstatus/OCSP/QC, Certstatus/CRL, Certstatus/CRL/QC) e con altri tipi definiti dal TLSO ai sensi della clausola D3; vietato con altri tipi.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.5.9.2.0 (General)",
        "testo": (
            "General della Qualifications Extension: il campo deve essere presente quando le informazioni "
            "presenti nei certificati qualificati creati e firmati da (o sotto) un servizio fiduciario elencato "
            "di tipo 'CA/QC' non consentono l'identificazione elaborabile automaticamente della natura di "
            "certificato qualificato rivendicato, della residenza o meno della chiave privata corrispondente "
            "alla chiave pubblica certificata in un SSCD o in un QSCD, dell'emissione a persona giuridica e "
            "della destinazione a firme elettroniche, sigilli elettronici o autenticazione di siti web. Se "
            "l'estensione e' marcata 'critical', un processo di validazione del certificato deve scartare il "
            "certificato in validazione che non riesca a interpretarne l'intera semantica. L'estensione delle "
            "qualificazioni e' specificata da un insieme di Qualification Elements, ciascuno espresso come "
            "lista di asserzioni da verificare e lista di qualificatori applicabili al certificato esaminato "
            "quando tutte le asserzioni sono verificate; il certificato e' qualificato con tutti i "
            "qualificatori ottenuti dall'applicazione di tutti gli elementi di qualificazione. Formato: "
            "sequenza non vuota di uno o piu' Qualification Elements definiti nella clausola 5.5.9.2.1; per la "
            "definizione formale, elemento Qualifications dello schema richiamato dall'annex C."
        ),
        "testo_integrale": (
            """Presence: This field shall be present when the information present in the qualified certificates created and signed by or under a listed trust service of the type "CA/QC" does not allow machine-processable identification:

-    of the fact that it is a claimed qualified certificate or not; and/or

-    whether or not the private key corresponding to the certified public key resides in an SSCD or in a QSCD; and/or

-    whether the certificate has been issued to a legal person; and/or

-    whether the certificate has been issued for electronic signatures, for electronic seals or for web site authentication.

If this extension is marked "critical" a certificate validation process shall discard the certificate under validation if it cannot parse and understand its entire semantic.

Description: The qualifications extension is specified by a set of Qualification Elements, each one expressed as a list of assertions to be verified and a list of qualifiers that apply to the examined certificate when all the assertions are verified. The certificate is qualified with all the qualifiers obtained with the application of all the qualification elements.

Format: A non-empty sequence of one or more Qualification Elements defined below in clause 5.5.9.2.1. For the formal definition see Qualifications element in the schema referenced by annex C."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": "Obbligatoria quando le informazioni nei certificati qualificati creati e firmati da (o sotto) un servizio elencato di tipo 'CA/QC' non consentono l'identificazione machine-processable delle caratteristiche elencate.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.5.9.2.1 (QualificationElement)",
        "testo": (
            "QualificationElement: campo obbligatorio che raggruppa una lista di asserzioni (criteri) che "
            "specificano gli attributi identificanti i certificati (es. determinati key-usage-bit impostati) "
            "cui si applica una lista di qualificatori che specificano proprieta' del certificato (es. se e' o "
            "meno un certificato qualificato, se la chiave privata corrispondente risiede in un SSCD/QSCD, se "
            "il soggetto del certificato e' una persona giuridica). Formato: tupla composta da una lista di "
            "asserzioni (CriteriaList, clausola 5.5.9.2.2) e da una lista di qualificatori (Qualifiers, "
            "clausola 5.5.9.2.3); per la definizione formale, elemento QualificationElementType dello schema "
            "richiamato dall'annex C."
        ),
        "testo_integrale": (
            """Presence: This field shall be present.

Description: This field bundles a list of assertions (criteria) that specifies the attributes identifying the certificates (e.g. certain key-usage-bits set) to which a list of qualifiers apply that specify some certificate properties (e.g. it is a qualified certificate or not, the corresponding private key resides in an SSCD/QSCD or not, the subject of the certificate is a legal person).

Format: A tuple consisting of a list of assertions (CriteriaList, see clause 5.5.9.2.2) and a list of qualifiers (Qualifiers, see clause 5.5.9.2.3). For the formal definition see QualificationElementType element in the schema referenced by annex C."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.5.9.2.2.0 (General)",
        "testo": (
            "General della CriteriaList: campo obbligatorio che fornisce una lista di asserzioni relative al "
            "contenuto (es. key usage) e/o allo stato (es. valutazione aggiuntiva) del certificato, usate per "
            "filtrare i certificati; un'asserzione puo' essere essa stessa una CriteriaList (definizione "
            "ricorsiva) e un campo Description opzionale consente allo schema operator di specificare la ratio "
            "dei criteri definiti. Formato: sequenza non vuota di asserzioni la cui sintassi e' specificata "
            "nelle clausole 5.5.9.2.2.1-5.5.9.2.2.3, seguita da un indicatore di corrispondenza dei criteri con "
            "valori 'all' (tutte le asserzioni devono essere soddisfatte), 'atLeastOne' (almeno una) o 'none' "
            "(nessuna), perche' l'insieme di qualificatori collegato alla CriteriaList si applichi; per la "
            "definizione formale, elemento CriteriaListType dello schema richiamato dall'annex C. Il campo "
            "opzionale Description e' una stringa di caratteri e, se presente, deve essere espressa in inglese "
            "britannico."
        ),
        "testo_integrale": (
            """Presence: This field shall be present.

Description: It provides a list of assertions related to certificate contents (e.g. key usage) and/or status (e.g. additional assessment) used to filter certificates. An assertion can be itself a CriteriaList allowing a recursive definition. An optional Description field allows the schema operator to specify the rationale of the defined criteria.

Format: A non-empty sequence of assertions whose syntax is specified in clauses 5.5.9.2.2.1 to 5.5.9.2.2.3 followed by a matching criteria indicator that can have the following values:

-    "all" if all of the assertion shall be met;

-    "atLeastOne" if at least one of the assertion shall be met; or

-    "none" if all the assertions shall not be met;

for the given set of qualifiers, related to the CriteriaList, to apply.

For the formal definition see CriteriaListType element in the schema referenced by annex C.

An optional Description field expressed as a character string. If present the description shall be expressed in UK English."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.5.9.2.2.1 (KeyUsage)",
        "testo": (
            "KeyUsage: campo opzionale che fornisce una lista di valori di bit di key usage da confrontare con "
            "i bit corrispondenti presenti nell'estensione keyUsage del certificato; l'asserzione e' verificata "
            "se l'estensione KeyUsage e' presente nel certificato e tutti i bit di key usage forniti "
            "corrispondono al bit corrispondente nell'estensione KeyUsage del certificato. Formato: sequenza "
            "non vuota di tuple composte da un identificatore di Key Usage Bit e dal valore asserito; gli "
            "identificatori dei bit devono essere quelli definiti nella Raccomandazione ITU-T X.509 per "
            "l'estensione KeyUsage. Per la definizione formale, elemento KeyUsageType dello schema richiamato "
            "dall'annex C."
        ),
        "testo_integrale": (
            """Presence: This field is optional.

Description: It provides a list of key usage bit-values to match with the correspondent bits present in the keyUsage certificate Extension. The assertion is verified if the KeyUsage Extension is present in the certificate and all key usage bits provided are matched with the corresponding bit in the certificate KeyUsage Extension.

Format: A non-empty sequence of tuples composed by a Key Usage Bit identifier and the asserted value. The key usage bits identifiers shall be those defined in Recommendation ITU-T X.509 [1] for the KeyUsage Extension. For the formal definition see KeyUsageType element in the schema referenced by annex C."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.5.9.2.2.2 (PolicySet)",
        "testo": (
            "PolicySet: campo opzionale che fornisce una lista di identificatori di Certificate Policy da "
            "confrontare con il contenuto dell'estensione CertificatePolicy del certificato; l'asserzione e' "
            "verificata se l'estensione CertificatePolicy e' presente nel certificato e tutti gli "
            "identificatori di Certificate Policy forniti sono presenti in tale estensione. Formato: sequenza "
            "di uno o piu' Object Identifier che indicano una Certificate Policy; per la definizione formale, "
            "elemento PoliciesListType dello schema richiamato dall'annex C."
        ),
        "testo_integrale": (
            """Presence: This field is optional.

Description: It provides list of Certificate Policy identifiers to match with the content of the CertificatePolicy certificate Extension. The assertion is verified if the CertificatePolicy Extension is present in the certificate and all the Certificate Policy identifiers provided are present in the certificate CertificatePolicy Extension.

Format: A sequence of one of more Object Identifiers indicating a Certificate Policy. For the formal definition see PoliciesListType element in the schema referenced by annex C."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.5.9.2.2.3 (OtherCriteria)",
        "testo": (
            "OtherCriteria: campo opzionale che consente di includere nuovi criteri richiesti dai TL Scheme "
            "Operator per asserzioni aggiuntive su contenuto/stato del certificato; nuovi criteri potranno "
            "essere aggiunti in futuro e, se non inclusi nell'elenco seguente, e' responsabilita' del TLSO che "
            "definisce un nuovo criterio pubblicarne la relativa definizione in modo efficace. Sono elencati "
            "due criteri: 1) ExtendedKeyUsage (campo opzionale: lista non vuota di valori di key purpose da "
            "confrontare con i KeyPurposes corrispondenti presenti nell'estensione ExtendedKeyUsage del "
            "certificato; l'asserzione e' verificata se l'estensione e' presente e tutti i key purpose forniti "
            "vi sono presenti; formato: sequenza non vuota di KeyPurposes con semantica definita nella "
            "Raccomandazione ITU-T X.509 per l'estensione ExtendedKeyUsage, elemento ExtendedKeyUsage dello "
            "schema dell'annex C); 2) CertSubjectDNAttribute (campo opzionale: insieme non vuoto di OID, "
            "ciascuno mappato a un possibile attributo nel Subject DN del certificato, con criterio soddisfatto "
            "se tutti gli OID riferiscono un attributo presente nel DN; formato: sequenza non vuota di OID "
            "rappresentanti attributi Directory, elemento CertSubjectDNAttribute dello schema dell'annex C)."
        ),
        "testo_integrale": (
            """Presence: This field is optional.

Description: It allows the inclusion of new criteria that can be required by TL Scheme Operators for additional assertions on certificate content/status. Here follows some OtherCriteria definition, new criteria can be added in future. If not included in the following list it is the responsibility of the TLSO that defines a new criteria to publish the related definition in an effective way.

1)   ExtendedKeyUsage:

Presence: This field is optional.

Description: It provides a non-empty list of key purposes values to match with the correspondent KeyPurposes present in the ExtendedKeyUsage certificate Extension. The assertion is verified if the ExtendedKeyUsage Extension is present in the certificate and all key purposes provided are present in the certificate ExtendedKeyUsage Extension.

Format: A non-empty sequence of KeyPurposes, whose semantic shall be as defined in Recommendation ITU-T X.509 [1] for the ExtendedKeyUsage Extension. For the formal definition see ExtendedKeyUsage element in the schema referenced by annex C.

2)   CertSubjectDNAttribute:

Presence: This field is optional.

Description: It provides a non-empty set of OIDs. Each OID maps to a possible attribute in the Subject DN of the certificate. The criterion is matched if all OID refers to an attribute present in the DN.

Format: A non-empty sequence of OIDs representing Directory attributes, whose meaning respect the description above. For the formal definition see CertSubjectDNAttribute element in the schema referenced by annex C."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.5.9.2.3 (Qualifier)",
        "testo": (
            "Qualifier: campo obbligatorio che specifica le proprieta' possedute da un certificato con i "
            "criteri indicati; formato: sequenza di indicatori espressi come URI. I qualificatori seguenti "
            "vanno usati solo quando il tipo del servizio cui si applicano e' 'CA/QC' e sono definiti nella "
            "clausola D.5: QCWithSSCD, QCNoSSCD, QCSSCDStatusAsInCert, QCWithQSCD, QCNoQSCD, "
            "QCQSCDStatusAsInCert, QCQSCDManagedOnBehalf, QCForLegalPerson, QCForESig, QCForESeal, QCForWSA, "
            "NotQualified, QCStatement (quest'ultimo indica che tutti i certificati identificati dai criteri "
            "applicabili sono emessi come certificati qualificati e va usato con estrema cautela da MS Scheme "
            "Operator e organismi di vigilanza/accreditamento, e solo quando esistono prove solide che i "
            "certificati identificati tramite i filtri applicati siano effettivamente da considerare "
            "qualificati e non sia presente nei certificati alcuna informazione elaborabile che lo indichi, "
            "cioe' nessun uso di QcCompliance statement o di OID QCP/QCP+)."
        ),
        "testo_integrale": (
            """Presence: This field shall be present.

Description: It specifies the properties a certificate with the specified criteria possesses.

Format: Sequence of indicators expressed as URIs.

Value: The following qualifiers shall only be used when the type of the service to which it applies is "CA/QC". They are defined in clause D.5:

-    QCWithSSCD ("http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCWithSSCD"): to indicate that all certificates identified by the applicable list of criteria, when they are claimed or stated as being qualified, have their private key residing in an SSCD;

-    QCNoSSCD ("http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCNoSSCD"): to indicate that all certificates identified by the applicable list of criteria, when they are claimed or stated as being qualified, do not have their private key residing in an SSCD;

-    QCSSCDStatusAsInCert ("http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCSSCDStatusAsInCert"): to indicate that all certificates identified by the applicable list of criteria, when they are claimed or stated as being qualified, do contain proper machine processable information about whether or not their private key residing in an SSCD;

-    QCWithQSCD ("http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCWithQSCD"): to indicate that all certificates identified by the applicable list of criteria, when they are claimed or stated as being qualified, have their private key residing in a QSCD;

-    QCNoQSCD ("http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCNoQSCD"): to indicate that all certificates identified by the applicable list of criteria, when they are claimed or stated as being qualified, do not have their private key residing in a QSCD;

-    QCQSCDStatusAsInCert ("http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCQSCDStatusAsInCert"): to indicate that all certificates identified by the applicable list of criteria, when they are claimed or stated as being qualified, do contain proper machine processable information about whether or not their private key residing in a QSCD;

-    QCQSCDManagedOnBehalf ("http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCQSCDManagedOnBehalf"): to indicate that all certificates identified by the applicable list of criteria, when they are claimed or stated as being qualified, have their private key residing in a QSCD for which the generation and management of that private key is done by the qualified TSP on behalf of the entity whose identity is certified in the certificate;

-    QCForLegalPerson ("http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCForLegalPerson"): to indicate that all certificates identified by the applicable list of criteria, when they are claimed or stated as being qualified, are issued to legal persons;

-    QCForESig ("http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCForESig"): to indicate that all certificates identified by the applicable list of criteria, when they are claimed or stated as being qualified, are issued for electronic signatures;

-    QCForESeal ("http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCForESeal"): to indicate that all certificates identified by the applicable list of criteria, when they are claimed or stated as being qualified, are issued for electronic seals;

-    QCForWSA ("http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCForWSA"): to indicate that all certificates identified by the applicable list of criteria, when they are claimed or stated as being qualified, are issued for web site authentication;

-    NotQualified ("http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/NotQualified"): to indicate that all certificates identified by the applicable list of criteria are not to be considered as qualified certificates;

-    QCStatement ("http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCStatement"): to indicate that all certificates identified by the applicable list of criteria are issued as qualified certificates.

The QCStatement qualifier shall be used with extreme caution by MS Scheme Operators and Supervisory/Accreditation Bodies when and only when:

•     strong evidence exists that certificates identified through the applied filters are indeed to be considered as qualified certificates; and

•     no machine processable information is present in the certificates to indicate that it is used as a qualified certificate (i.e. no use of QcCompliance statement [i.9] or a QCP/QCP+ OID [i.5])."""
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.5.9.3 (TakenOverBy Extension)",
        "testo": (
            "Estensione 'TakenOverBy': campo obbligatorio quando un servizio precedentemente sotto la "
            "responsabilita' legale di un TSP viene assunto da un altro TSP; specifica l'identita' del TSP che "
            "ha assunto la responsabilita' del servizio cui l'estensione si applica e serve a dichiarare "
            "formalmente la natura di tale responsabilita' legale e a consentire al software di verifica di "
            "mostrare all'utente i dettagli legali. Formato: un URI e una sequenza di attributi (il TSP name "
            "come definito nella clausola 5.4.1; lo Scheme operator name come specificato nella clausola 5.3.4; "
            "lo Scheme territory come specificato nella clausola 5.3.10; un campo opzionale di informazioni "
            "aggiuntive per ulteriore qualificazione del TSP subentrante, da definire in versioni future del "
            "documento o dagli schema operator come specifico dello scheme). Quando un servizio elencato viene "
            "assunto da un TSP diverso da quello sotto cui e' elencato, la relativa voce di servizio non deve "
            "essere copiata dal TLSO ne' spostata dentro la lista di servizi del TSP subentrante, ed e' "
            "responsabilita' del TLSO mantenere aggiornato il corretto service trust state; se il TSP "
            "subentrante emette una nuova identita' digitale relativa al servizio assunto (es. un nuovo "
            "certificato self-signed per una CA) deve essere creata una nuova voce di servizio sotto il TSP "
            "subentrante; se il servizio precedente e' ancora operativo, anche per un perimetro limitato (es. "
            "emissione di CRL), il suo stato deve essere mantenuto dal TLSO secondo le regole stabilite fino "
            "alla cessazione delle operazioni. L'URI contenuto punta a un testo descrittivo che deve fornire "
            "informazioni dettagliate all'utente su chi e' l'entita' attualmente responsabile del servizio e "
            "sul processo di subentro e le sue conseguenze per sottoscrittori e parti affidanti; l'estensione "
            "contiene inoltre un insieme di attributi che identificano univocamente il TSP subentrante per "
            "localizzarlo nella TL, se presente, e mostrarne i dettagli. Il contenuto dell'estensione non e' "
            "inteso a imporre alcuna azione specifica sulla validazione della firma. Se l'estensione e' marcata "
            "'critical', un processo di validazione del certificato deve scartare il certificato in validazione "
            "che non riesca a interpretarne l'intera semantica. L'estensione deve essere implementata con "
            "l'elemento TakenOverBy definito nello schema richiamato dall'annex C."
        ),
        "testo_integrale": (
            """Presence: This field shall be present when a service that was formerly under the legal responsibility of a TSP is taken over by another TSP.

Description: It specifies the identity of the TSP having taken over the responsibility of the service to which this extension applies and is meant to state formally the nature of this legal responsibility and to enable the verification software to display to the user some legal detail.

Format: This extension contains an URI, and a sequence of the following attributes:

-    The TSP name, as defined in clause 5.4.1.

-    The Scheme operator name as specified in clause 5.3.4.

-    The Scheme territory as specified in clause 5.3.10.

-    An optional additional information field for further qualification of the taking over TSP, to be defined in future versions of the present document or by schema operators as schema specific.

Value: When a listed service is taken over by another TSP than the one under which the service is listed, the related service entry in the TL shall not be copied by the TLSO or moved inside the taking over TSP list of services and it is under the responsibility of the TLSO to maintain up to date the correct service trust state. If the taking over TSP issues a new digital identity related to the taken over service (e.g. a new self-signed certificate for a CA) then a new service entry shall be created under the taking over TSP. If the previous service is still in operation, even for a limited scope (e.g. CRL issuing as for the example above) its status shall be maintained by the TLSO, according to the established rules, until the service terminates its operations.

This extension contains an URI, pointing towards a descriptive text that shall provide detailed information to the user about who is the entity currently responsible for the service and detailed information about the taken over process and its consequences on subscribers and relying parties.

In addition this extension contains a set of attributes, uniquely identifying the taking over TSP allowing the application to locate this TSP in the TL, if present, and to display its details.

The content of this extension is not meant to enforce any specific action on the signature validation.

If this extension is marked "critical" a certificate validation process shall discard the certificate under validation if it cannot parse and understand its entire semantic.

This extension shall be implemented with the TakenOverBy element defined in the schema referenced by annex C."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": "Obbligatoria quando un servizio precedentemente sotto la responsabilita' legale di un TSP viene assunto da un altro TSP.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.5.9.4 (additionalServiceInformation Extension)",
        "testo": (
            "Estensione 'additionalServiceInformation': campo opzionale che specifica informazioni aggiuntive "
            "su un servizio; formato: sequenza di una o piu' tuple, ciascuna con le informazioni sotto "
            "dettagliate, con possibilita' per una TL di avere piu' estensioni additionalServiceInformation "
            "nella stessa voce di servizio, ciascuna estensione fornendo: a) un URI che identifica "
            "l'informazione aggiuntiva, con valori possibili non limitati ai seguenti: ForeSignatures, "
            "ForeSeals e ForWebSiteAuthentication (per specificare ulteriormente che il servizio identificato "
            "dal 'Service type identifier' e' erogato rispettivamente per firme elettroniche, sigilli "
            "elettronici o autenticazione di siti web), un URI registrato per qualificare ulteriormente un "
            "'Service type identifier' (clausola 5.5.1) per specificare che il servizio e' un servizio "
            "componente di un prestatore di servizi fiduciari che emette certificati qualificati (es. "
            "l'estensione di qualificazione di tipo di servizio 'RootCA-QC' di un tipo di servizio 'CA/QC' come "
            "specificato nella clausola D.4), oppure un URI indicante una qualificazione specifica definita a "
            "livello nazionale per un servizio di erogazione di Trust Service Token sottoposto a "
            "vigilanza/accreditamento; gli EXAMPLES ufficiali citano un livello specifico di granularita' di "
            "sicurezza/qualita' rispetto al sistema nazionale di vigilanza/accreditamento per TSP che non "
            "emettono certificati qualificati (es. RGS */**/*** in Francia, status di 'supervision' stabilito "
            "da legislazione nazionale per TSP specifici che emettono certificati qualificati in Germania), uno "
            "status legale specifico per un servizio di erogazione di Trust Service Token sottoposto a "
            "vigilanza/accreditamento (es. 'qualified TST' definito a livello nazionale in Germania, Ungheria o "
            "Italia) e il significato di uno specifico identificatore di Policy presente in un certificato "
            "X.509v3 fornito nel campo 'Sdi'; b) una stringa opzionale contenente la classificazione "
            "serviceInformation, con significato specificato nello scheme (es. in Francia i servizi sono "
            "classificati con URI specificamente registrati in linea con i possibili valori di classificazione "
            "RGS); c) ogni ulteriore informazione opzionale fornita in formato specifico dello scheme. "
            "L'estensione puo' essere usata per fornire, per un dato servizio, informazioni aggiuntive che "
            "possono aiutare a verificare l'applicabilita' del servizio a un certo scopo; il dereferenziamento "
            "dell'URI dovrebbe condurre a informazioni leggibili da una persona (come minimo in inglese "
            "britannico e potenzialmente in una o piu' lingue nazionali) ritenute appropriate e sufficienti "
            "perche' una parte affidante comprenda l'estensione, spiegando in particolare il significato degli "
            "URI dati e specificando i possibili valori di serviceInformation e il significato di ciascun "
            "valore."
        ),
        "testo_integrale": (
            """Presence: This field is optional.

Description: It specifies additional information on a service.

Format: A sequence of one or more tuples, each tuple providing the information detailed below. A TL may have more than one additionalServiceInformation extension in the same service entry, each extension giving:

a)   an URI identifying the additional information. Possible values, not limited to the following:

i)    "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/ForeSignatures": in order to further specify the "Service type identifier" identified service as being provided for electronic signatures;

ii)   "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/ForeSeals": in order to further specify the "Service type identifier" identified service as being provided for electronic seals;

iii) "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/ForWebSiteAuthentication": in order to further specify the "Service type identifier" identified service as being provided for web site authentication;

iv)   a registered URI to further qualify a "Service type identifier" (clause 5.5.1), in order to further specify the "Service type identifier" identified service as being a component service of a trust service provider issuing QC (e.g. "RootCA-QC" service type qualification extension of a "CA/QC" service type as specified in clause D.4);

v)    an URI indicating some nationally defined specific qualification for a supervised/accredited Trust Service Token provisioning service.

EXAMPLES: •       a specific security/quality granularity level with regard to national supervision/accreditation system for TSPs not issuing QCs (e.g. RGS */**/*** in France, specific "supervision" status set by national legislation for specific TSPs issuing QCs in Germany); or

•       a specific legal status for a supervised/accredited Trust Service Token provisioning (e.g. nationally defined "qualified TST" as in Germany, Hungary or Italy); or

•       meaning of a specific Policy identifier present in a X.509v3 certificate provided in "Sdi" field.

b)   an optional string containing the serviceInformation classification, with a meaning as specified in the scheme (e.g. in France services are classified with specifically registered URI in line with the possible RGS classification values);

c)   any optional additional information provided in a scheme-specific format.

Value: This extension may be used to provide, for a given service, additional information that may help to verify the applicability of the given service for a certain purpose.

Dereferencing the URI should lead to human readable information (as a minimum in UK English language and potentially in one or more national languages) which is deemed appropriate and sufficient for a relying party to understand the extension, and in particular explaining the meaning of the given URIs, specifying the possible values for serviceInformation and the meaning for each value."""
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.5.10 (Service history)",
        "testo": (
            "Campo 'Service history': deve essere presente solo quando informazione storica e' applicabile al "
            "servizio considerato, e non deve essere presente quando il servizio non ha storia precedente allo "
            "stato corrente (cioe' primo stato registrato o informazione storica non conservata dallo scheme "
            "operator); specifica informazioni storiche sui servizi fiduciari elencati come sequenza di tutte "
            "le precedenti voci di stato registrate dallo scheme per il servizio del TSP. Formato: sequenza di "
            "elementi Service History Instance (clausola 5.6). Per ogni variazione dello stato di approvazione "
            "del servizio TSP intervenuta entro il periodo di informazione storica specificato nella clausola "
            "5.3.12, le informazioni sul precedente stato di approvazione devono essere fornite in ordine "
            "decrescente di data e ora del cambio di stato (cioe' la data e ora in cui il successivo stato di "
            "approvazione e' divenuto efficace)."
        ),
        "testo_integrale": (
            """Presence: This field shall be present only when historical information is applicable to the related service. In the case the service has no history prior to the current status (i.e. a first recorded status or history information not retained by the scheme operator) this field shall not be present.

Description: It specifies historical information on listed trust services as a sequence of all previous status entries which the scheme has recorded for the given TSP service.

Format: A sequence of Service History Instance elements (see clause 5.6).

Value: For each change in TSP service approval status which occurred within the historical information period as specified in clause 5.3.12, information on the previous approval status shall be provided in descending order of status change date and time (i.e. the date and time on which the subsequent approval status became effective)."""
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": "Presenza subordinata all'esistenza di informazione storica applicabile al servizio considerato.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.6.1 (Service type identifier)",
        "testo": (
            "Service type identifier dell'istanza di storia del servizio: campo obbligatorio che specifica "
            "l'identificatore del tipo di servizio, con Formato e Valore usati nella clausola 5.5.1."
        ),
        "testo_integrale": (
            """Presence: This field shall be present.

Description: It specifies the identifier of the service type, with the Format and Value used in clause 5.5.1."""
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.6.2 (Service name)",
        "testo": (
            "Service name dell'istanza di storia del servizio: campo obbligatorio che specifica il nome con cui "
            "il TSP erogava il servizio identificato nella clausola 5.5.1, con Formato e Valore usati nella "
            "clausola 5.5.2. NOTE ufficiale: la clausola non richiede che il nome sia lo stesso specificato "
            "nella clausola 5.5.2, e un cambio di nome puo' essere una delle circostanze che richiedono un "
            "nuovo stato."
        ),
        "testo_integrale": (
            """Presence: This field shall be present.

Description: It specifies the name under which the TSP provided the service identified in clause 5.5.1, with the Format and Value used in clause 5.5.2.

NOTE: This clause does not require the name to be the same as that specified in clause 5.5.2. A change of name may be one of the circumstances requiring a new status."""
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.6.3 (Service digital identity)",
        "testo": (
            "Service digital identity dell'istanza di storia del servizio: campo obbligatorio che specifica "
            "almeno una rappresentazione di un identificatore digitale del servizio usato nella clausola 5.5.1, "
            "con il Formato e il Valore usati nella clausola 5.5.3 per ogni rappresentazione, con almeno "
            "l'elemento X509SKI e a eccezione di qualsiasi certificato."
        ),
        "testo_integrale": (
            """Presence: This field shall be present.

Description: It specifies at least one representation of a digital identifier of the service used in clause 5.5.1, with the Format and Value used in clause 5.5.3 for any representation, with at least the X509SKI element and to the exception of any certificate."""
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.6.4 (Service previous status)",
        "testo": (
            "Service previous status dell'istanza di storia del servizio: campo obbligatorio che specifica "
            "l'identificatore dello stato precedente del servizio, con Formato e Valore usati nella clausola "
            "5.5.4."
        ),
        "testo_integrale": (
            """Presence: This field shall be present.

Description: It specifies the identifier of the previous status of the service, with the Format and Value used in clause 5.5.4."""
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.6.5 (Previous status starting date and time)",
        "testo": (
            "Previous status starting date and time dell'istanza di storia del servizio: campo obbligatorio che "
            "specifica la data e ora in cui il precedente stato in questione e' divenuto efficace, con Formato "
            "e Valore usati nella clausola 5.5.5."
        ),
        "testo_integrale": (
            """Presence: This field shall be present.

Description: It specifies the date and time on which the previous status in question became effective, with the Format and Value used in clause 5.5.5."""
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.6.6 (Service information extensions)",
        "testo": (
            "Service information extensions dell'istanza di storia del servizio: campo opzionale, utilizzabile "
            "dai TLSO per fornire informazioni specifiche sul servizio da interpretare secondo le regole dello "
            "scheme, con Formato e Valore usati nella clausola 5.5.9."
        ),
        "testo_integrale": (
            """Presence: This field is optional.

Description: It may be used by TLSOs to provide specific service-related information, to be interpreted according to the specific scheme's rules, with the Format and Value used in clause 5.5.9."""
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.7.1 (Digitally signed Trusted List)",
        "testo": (
            "La trusted list deve essere firmata digitalmente dallo 'Scheme operator name' (clausola 5.3.4) per "
            "garantirne autenticita' e integrita'. Il formato della firma digitale deve essere XAdES-B-B come "
            "definito in ETSI EN 319 132-1 e l'implementazione della firma deve soddisfare i requisiti "
            "enunciati nell'annex B; l'algoritmo di firma digitale e la chiave di firma certificata devono "
            "conformarsi ai requisiti di sicurezza per una chiave utilizzabile almeno 3 anni specificati nelle "
            "tabelle 4, 6 e 7 di ETSI TS 119 312. Il certificato del TLSO usato per validare la firma digitale "
            "sulla TL deve essere protetto dalla firma digitale incorporandolo nell'elemento ds:KeyInfo, che "
            "non deve contenere alcun altro certificato costituente una catena di certificazione associata. Il "
            "certificato di firma digitale dello Scheme Operator deve essere conforme alle seguenti "
            "restrizioni: l'Issuer deve essere il TLSO stesso (certificato self-signed) o un servizio "
            "fiduciario di un TSP elencato nella TL o in una delle TL facenti parte della stessa comunita' "
            "(clausola 5.3.9); i campi 'Country code' e 'Organization' del Subject Distinguished Name devono "
            "corrispondere rispettivamente allo 'Scheme Territory' e a uno dei valori dello 'Scheme operator "
            "name' (per quest'ultimo dovrebbe essere usato il valore in inglese britannico, preferito, o in "
            "lingua locale traslitterata in caratteri latini); l'estensione KeyUsage deve essere impostata a "
            "digitalSignature e/o a nonRepudiation (contentCommitment) con esclusione di ogni altro valore di "
            "KeyUsage; l'estensione ExtendedKeyUsage dovrebbe essere presente e contenere id-tsl-kp-tslSigning; "
            "l'uso delle estensioni KeyUsage ed ExtendedKeyUsage deve essere coerente con lo scopo di firmare "
            "trusted list; l'estensione SubjectKeyIdentifier deve essere presente usando uno dei primi 2 metodi "
            "specificati nella clausola 4.2.1.2 di IETF RFC 5280; l'estensione BasicConstraints deve indicare "
            "CA=false. Per indicare che l'uso delle coppie di chiavi e' ristretto alla sola firma digitale di "
            "TL, un certificato X.509 v3 dovrebbe includere il seguente key purpose id OID nell'estensione "
            "extended key usage (id-tsl, id-tsl-kp, id-tsl-kp-tslSigning). Ulteriori requisiti generali su "
            "questa firma digitale sono enunciati nelle clausole seguenti."
        ),
        "testo_integrale": (
            """The trusted list shall be digitally signed by the 'Scheme operator name' (clause 5.3.4) to ensure its authenticity and integrity.

The format of the digital signature shall be XAdES-B-B as defined by ETSI EN 319 132-1 [3]. Such digital signature implementation shall meet requirements as stated in annex B. The digital signature algorithm as well as the certified digital signature key shall conform to security requirement for a minimum 3 years usable key as specified in tables 4, 6 and 7 of ETSI TS 119 312 [2].

The TLSO certificate, to be used to validate its digital signature on the TL, shall be protected with the digital signature by incorporating the TLSO certificate within the ds:KeyInfo element that shall not contain any other certificate forming any kind of associated certificate chain.

The Scheme Operator's digital signature certificate shall be conformant to the following restrictions:

•     The Issuer shall be the TLSO itself (i.e. a self-signed certificate) or a TSP trust service listed in the TL or in one of the TL that is part of the same community (see clause 5.3.9).

•     "Country code" and "Organization" fields in Subject Distinguished Name shall match respectively the "Scheme Territory" and one of the "Scheme operator name" values. For the latter, the value in UK English language (preferred) or local language (transliterated to Latin script), as available, should be used.

•     KeyUsage extension shall be set to digitalSignature and/or to nonRepudiation (contentCommitment) to the exclusion of any other KeyUsage value.

•     ExtendedKeyUsage extension should be present containing id-tsl-kp-tslSigning (see below).

•     The use of the KeyUsage and ExtendedKeyUsage extensions shall be consistent with the purpose of signing trusted lists.

•     SubjectKeyIdentifier extension shall be present using one of the first 2 methods specified in clause 4.2.1.2 of IETF RFC 5280 [12].

•     BasicConstraints extension shall indicate CA=false.

In order to indicate that the use of key-pairs is restricted to digitally sign TLs only, an X.509 v3 certificate should include the following key purpose id OID in the extended key usage extension: -- OID for TSL signing KeyPurposeID for ExtKeyUsageSyntax

id-tsl OBJECT IDENTIFIER { itu-t(0) identified-organization(4) etsi(0) tsl-specification (2231) } id-tsl-kp OBJECT IDENTIFIER ::= { id-tsl kp(3) } id-tsl-kp-tslSigning OBJECT IDENTIFIER ::= { id-tsl-kp tsl-signing(0) }

Additional general requirements regarding this digital signature are stated in the following clauses."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.7.2 (Digital signature algorithm identifier)",
        "testo": (
            "Digital signature algorithm identifier: campo obbligatorio che specifica l'algoritmo crittografico "
            "usato per creare la firma digitale; a seconda dell'algoritmo usato, il campo puo' richiedere "
            "parametri aggiuntivi. Formato: stringa di caratteri o stringa di bit, suggerito secondo "
            "l'implementazione. Il campo deve essere incluso nel calcolo della firma digitale."
        ),
        "testo_integrale": (
            """Presence: This field shall be present.

Description: It specifies the cryptographic algorithm that has been used to create the digital signature. Depending on the algorithm used, this field may require additional parameters.

Format: Character string or Bit string is suggested, depending on the implementation.

Value: This field shall be included in the calculation of the digital signature."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.7.3 (Digital signature value)",
        "testo": (
            "Digital signature value: campo obbligatorio che contiene il valore effettivo della firma digitale. "
            "Tutti i campi della TL eccetto il valore di firma stesso devono essere inclusi nel calcolo della "
            "firma digitale."
        ),
        "testo_integrale": (
            """Presence: This field shall be present.

Description: It contains the actual value of the digital signature.

Value: All fields of the TL except the signature value itself shall be included in the calculation of the digital signature."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 5.5.9 (Service information extensions)",
        "testo": (
            "Clausola di raggruppamento delle estensioni informative di servizio della Service information di "
            "una Trusted List: il testo ufficiale non le associa alcun periodo proprio (segue immediatamente la "
            "sottoclausola 5.5.9.0 General) e questa clausola funge da punto di ingresso dei rinvii all'insieme "
            "delle estensioni informative di servizio (cosi' la clausola 5.6.6 di questo capitolo e i rinvii "
            "dell'annex D e dell'annex J). Il campo e' opzionale e il TLSO seleziona quali estensioni veicolare "
            "nella propria TL; le estensioni predefinite sono specificate in 5.5.9.1 "
            "(expiredCertsRevocationInfo), 5.5.9.2 (Qualifications), 5.5.9.3 (TakenOverBy) e 5.5.9.4 "
            "(additionalServiceInformation)."
        ),
        "testo_integrale": (
            """5.5.9 Service information extensions"""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "oggetti_giuridici": ["altro"],
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 5.5.9 (Service information extensions)",
    "clausola 5.5.9.0 (General)",
    "clausola 5.5.9.1 (expiredCertsRevocationInfo Extension)",
    "clausola 5.5.9.2.0 (General)",
    "clausola 5.5.9.2.1 (QualificationElement)",
    "clausola 5.5.9.2.2.0 (General)",
    "clausola 5.5.9.2.2.1 (KeyUsage)",
    "clausola 5.5.9.2.2.2 (PolicySet)",
    "clausola 5.5.9.2.2.3 (OtherCriteria)",
    "clausola 5.5.9.2.3 (Qualifier)",
    "clausola 5.5.9.3 (TakenOverBy Extension)",
    "clausola 5.5.9.4 (additionalServiceInformation Extension)",
    "clausola 5.5.10 (Service history)",
    "clausola 5.6.1 (Service type identifier)",
    "clausola 5.6.2 (Service name)",
    "clausola 5.6.3 (Service digital identity)",
    "clausola 5.6.4 (Service previous status)",
    "clausola 5.6.5 (Previous status starting date and time)",
    "clausola 5.6.6 (Service information extensions)",
    "clausola 5.7.1 (Digitally signed Trusted List)",
    "clausola 5.7.2 (Digital signature algorithm identifier)",
    "clausola 5.7.3 (Digital signature value)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.1 (expiredCertsRevocationInfo Extension)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.2.0 (General)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.3 (TakenOverBy Extension)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.4 (additionalServiceInformation Extension)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.1 (TSP name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.1 (expiredCertsRevocationInfo Extension)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.0 (General requirements)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.1 (expiredCertsRevocationInfo Extension)"),
        "nodo_a": ("principio", None, "Annex D.3 (Scheme registered URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.1 (expiredCertsRevocationInfo Extension)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.3 (Date-time indication)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.2.1 (QualificationElement)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.0 (General)"),
        "nodo_a": ("principio", None, "Annex C (XML schema)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.1 (QualificationElement)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.2.2.0 (General)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.1 (QualificationElement)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.2.3 (Qualifier)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.1 (QualificationElement)"),
        "nodo_a": ("principio", None, "Annex C (XML schema)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.2.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.2.2.1 (KeyUsage)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.2.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.2.2.2 (PolicySet)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.2.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.2.2.3 (OtherCriteria)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.2.0 (General)"),
        "nodo_a": ("principio", None, "Annex C (XML schema)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.2.1 (KeyUsage)"),
        "nodo_a": ("principio", None, "Annex C (XML schema)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.2.2 (PolicySet)"),
        "nodo_a": ("principio", None, "Annex C (XML schema)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.2.3 (OtherCriteria)"),
        "nodo_a": ("principio", None, "Annex C (XML schema)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.2.3 (Qualifier)"),
        "nodo_a": ("principio", None, "Annex D.5 (EU specific trusted lists URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.3 (TakenOverBy Extension)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.1 (TSP name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.3 (TakenOverBy Extension)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.4 (Scheme operator name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.3 (TakenOverBy Extension)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.10 (Scheme territory)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.3 (TakenOverBy Extension)"),
        "nodo_a": ("principio", None, "Annex C (XML schema)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.4 (additionalServiceInformation Extension)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.0 (General requirements)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.9.4 (additionalServiceInformation Extension)"),
        "nodo_a": ("obbligo", None, "Annex D.4 (Common trusted lists URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.10 (Service history)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.12 (Historical information period)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.10 (Service history)"),
        "nodo_a": ("obbligo", None, "clausola 5.6.1 (Service type identifier)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.6.1 (Service type identifier)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.0 (General requirements)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.6.2 (Service name)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.0 (General requirements)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.6.2 (Service name)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2 (Service name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.6.3 (Service digital identity)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.0 (General requirements)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.6.3 (Service digital identity)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.6.4 (Service previous status)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.4 (Service current status)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.6.5 (Previous status starting date and time)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.5 (Current status starting date and time)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.6.6 (Service information extensions)"),
        "nodo_a": ("principio", None, "clausola 5.5.9 (Service information extensions)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.7.1 (Digitally signed Trusted List)"),
        "nodo_a": ("obbligo", None, "Annex B.0 (General requirements)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.7.1 (Digitally signed Trusted List)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.4 (Scheme operator name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.7.1 (Digitally signed Trusted List)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.9 (Scheme type/community/rules)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
