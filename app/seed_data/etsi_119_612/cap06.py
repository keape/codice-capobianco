"""ETSI TS 119 612 V2.4.1 (2025-08) - Electronic Signatures and Trust
Infrastructures (ESI); Trusted Lists. Fonte 21 (id risolto per riferimento
dalla sessione principale in app/seed.py - questo modulo NON tocca seed.py).
Capitolo 6 del manifest di split: Annex C (normativo) XML schema e Annex D
(normativo) Registered Uniform Resource Identifiers, sottoclausole D.0-D.6
incluse D.5.1-D.5.6. Testo ufficiale in
app/.source_cache/etsi_119_612/cap06.txt (letto sempre con selettore `:raw`,
altrimenti il tool tronca le righe lunghe a 768 caratteri introducendo "..."
e mutilando la copia verbatim).

Modellazione (ADR-0007), stesso criterio delle altre fonti ETSI gia' censite:
un nodo per ogni clausola/sottoclausola numerata con contenuto proprio. Esito:
3 Obblighi, 11 Principi, 14 item di indice.

Scelte voce per voce:

- Annex C (XML schema) -> 1 Principio "altro". L'annesso dichiara il file ZIP
  elettronico associato ("ts_119612v020401p0.zip") i cui XML schema sono parti
  integranti del documento, la regola di prevalenza del testo del documento in
  caso di conflitto con gli schema e il repository Forge dove gli schema sono
  pubblicati. Non contiene un "shall" che imponga un comportamento a un
  soggetto identificabile ("the present document shall prevail" e' una regola
  dichiarativa di prevalenza, non una prescrizione a un obbligato): tipo
  "altro" e non Obbligo. L'obbligo di conformita' agli schema XML e' posto
  altrove (clausola 6, cap05).

- Annex D.0 (General) -> 1 Principio "definitorio": dichiara quali URI sono
  registrati in connessione con il documento (radix "…/19612/……" registrati
  per la loro presenza nel documento; radix "…/TrstSvc/……" registrati da ETSI
  come Common Domain per conto del TC ESI) e il layout delle tabelle.

- Annex D.1, D.2, D.3, D.5.1, D.5.2, D.5.3, D.5.5, D.6 -> Principi
  "definitorio": registri/dichiarazioni di URI e loro significato, senza
  comportamento imposto. D.2 e' dichiarata "Void" nel testo ufficiale: il nodo
  e' conservato come nodo di cornice per copertura completa della numerazione
  (ADR-0007), con il solo testo della clausola.

- Annex D.4 (Common trusted lists URIs), D.5.4 (Service information
  extensions/Qualifications Extension/Qualifiers) e D.5.6 (Service current and
  previous statuses) -> Obblighi: accanto al significato dei valori URI,
  contengono prescrizioni esplicite su un soggetto ("shall be published by the
  TLSO"; "This value shall not be used if the service type is not
  http://uri.etsi.org/TrstSvc/Svctype/CA/QC"; "…status shall be used when a TSP
  directly ceases its related services under supervision; it shall not be used
  when supervision has been revoked"; "…shall be provided in 'Scheme service
  definition URI' … and in the 'TakenOverBy' extension"). Tipo obbligo:
  "informativo/trasparenza" per D.4 (pubblicazione per gli utenti del testo
  descrittivo puntato dall'URI), "tecnico/sicurezza" per D.5.4 e D.5.6 (uso
  corretto dei valori registrati nel contenuto della TL). Soggetto obbligato:
  il TLSO / scheme operator, modellato come "QTSP/gestore"; per D.4 e D.5.6 i
  fruitori finali (relying party) sono "Terzi affidanti/pubblico" come
  destinatari.

- Annex D.5 (EU specific trusted lists URIs) -> 1 Principio "definitorio" di
  cornice: sottoclausola di raggruppamento senza prosa propria oltre al titolo,
  tenuta come nodo perche' e' bersaglio esplicito dei rinvii testuali "as
  defined in clause D.5" di questa Fonte (clausole 5.3.3, 5.3.8, 5.3.9, 5.4.x,
  5.5.4) e copre la numerazione D.0-D.6 richiesta per l'Annex D.

- Intestazione del solo "Annex D (normative): Registered Uniform Resource
  Identifiers" -> NESSUN nodo aggiuntivo: non porta testo proprio (segue subito
  D.0). Un rinvio generico del documento ad "annex D" e' quindi modellato verso
  "Annex D.0 (General)", che e' la clausola introduttiva del registro. Nessun
  nodo per il front matter, che non e' in questo capitolo.

Tabelle (ADR-0010): il testo ufficiale presenta i registri di URI come tabelle
a tre colonne (URI / Meaning / "Related TSL field (if any)"); l'estrazione
pdftotext -layout disallinea le celle (la terza colonna finisce a destra delle
righe di significato). Tutte le righe sono state riportate in `testo_integrale`
ricostruendo le coppie in forma esplicita ("<URI> - Meaning: … Related TSL
field (if any): …", e per i qualificatori di D.5.4/D.5.5/D.5.6 "<URI> -
<etichetta>: …"), separate da " | " per non alterare alcun frammento verbatim
(nessuna punteggiatura aggiunta in coda al testo ufficiale), senza omettere
alcun URI: D.1 = 3, D.3 = 2, D.4 = 2,
D.5.1 = 2, D.5.2 = 1, D.5.3 = 2, D.5.4 = 13, D.5.5 = 3, D.5.6 = 13, D.6 = 3.
Le spezzature di parola introdotte dal wrap del PDF nelle celle sono state
ricomposte (es. "extensions/additionalServi" + "ceInformation Extension/" ->
"extensions/additionalServiceInformation Extension/").

Ellissi autentica: in D.0 e nell'intestazione di D.6 il testo ufficiale abbrevia
il radix con "……" ("http://uri.etsi.org/19612/……",
"http://uri.etsi.org/TrstSvc/……"): e' contenuto autentico del documento, non
un'elisione di estrazione, ed e' riportato verbatim (3 occorrenze, gestite da
`_senza_omissis_legittimi` in app/seed_data/lib.py). In D.3 compare inoltre
l'URI d'esempio "http://"scheme_op_URI_root"/.../schemerules/"schemename""
("..." come segnaposto nel testo ufficiale), anch'esso verbatim.

NOTE/EXAMPLE: il capitolo non contiene clausole NOTE o EXAMPLE ufficiali; nulla
e' stato scartato per "pulizia".

RELAZIONI: 14 relazioni interne "richiama", tutte da riscontri testuali
puntuali e verificate sulle stringhe `riferimento` concordate con gli autori dei
capitoli che possiedono i nodi: D.4 -> 5.3.10, 5.5.6, 5.5.9; D.5.4 -> 5.5.3;
D.5.6 -> 5.3.4, 5.3.10, 5.4.1, 5.5.1.1, 5.5.1.2, 5.5.1.3, 5.5.3, 5.5.6,
5.5.9.3; D.6 -> 5.3.10. Nessuna relazione cross-fonte (Fase 6 della sessione
principale, ADR-0009).

Citazioni esterne notate ma non trasformate in relazioni: ETSI TS 119 612
stessa (edizioni storiche, in D.1), ETSI Identified Organization Domain e
portale ETSI pnns/xml.asp (D.0, D.3), repository Forge ETSI
https://forge.etsi.org/rep/esi/x19_612_trusted_lists (Annex C), ISO 3166-1
[i.15] (D.6), Regolamento (UE) n. 910/2014 [i.10] (D.5.6), le specifiche dei
servizi "SSCD"/"QSCD" e la legislazione europea applicabile (D.5.4).

Oggetti giuridici: nessuno dei Principi di questo capitolo e' riconducibile a
uno specifico oggetto giuridico dell'elenco (sono registri di URI di formato),
quindi il campo e' omesso. Verifica finale: `python3
app/seed_data/etsi_119_612/cap06.py`.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "Annex D.4 (Common trusted lists URIs)",
        "testo": (
            "Registra sotto il radix \"http://uri.etsi.org/TrstSvc/TrustedList/\" due URI. L'URI "
            "http://uri.etsi.org/TrstSvc/TrustedList/schemerules/CC (dove CC e' il codice usato nel campo "
            "\"Scheme territory\", clausola 5.3.10) punta a un testo descrittivo che deve essere pubblicato dal "
            "TLSO ed e' applicabile alla trusted list di quel CC: dove gli utenti trovano le policy/regole "
            "specifiche del CC rispetto alle quali i servizi in elenco devono essere valutati in conformita' agli "
            "approval schemes appropriati del CC, e dove trovano la descrizione di come usare e interpretare il "
            "contenuto della trusted list (es. in UE per i servizi non legati all'emissione di certificati "
            "qualificati, con la granularita' dei sistemi nazionali di supervisione/accreditamento e l'uso del "
            "campo \"Scheme service definition URI\", clausola 5.5.6, e del campo \"Service information "
            "extension\", clausola 5.5.9). L'URI http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/RootCA-QC "
            "identifica una Root Certification Authority da cui si puo' costruire un certification path fino a "
            "una CA che emette certificati qualificati; tale valore non deve essere usato se il tipo di servizio "
            "non e' http://uri.etsi.org/TrstSvc/Svctype/CA/QC."
        ),
        "testo_integrale": (
            "D.4 Common trusted lists URIs: The following URIs, are registered under the radix "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/\": http://uri.etsi.org/TrstSvc/TrustedList/schemerules/CC "
            "- Meaning: where CC is replaced with the code used in the \"Scheme territory\" field (see clause "
            "5.3.10). A URI specific to CC's trusted list pointing towards a descriptive text that shall be "
            "published by the TLSO and applicable to this CC's trusted list: • Where users can obtain the "
            "referenced CC's specific policy/rules against which services included in the list shall be assessed "
            "in compliance with the CC's appropriate approval schemes. • Where users can obtain a referenced CC's "
            "specific description about how to use and interpret the content of the trusted list (e.g. in the EU "
            "with regard to the trust services not related to the issuing of qualified certificates, where this "
            "may be used to indicate a potential granularity in the national supervision/accreditation systems "
            "related to trust service providers not issuing qualified certificates and how the \"Scheme service "
            "definition URI\" (see clause 5.5.6) and the \"Service information extension\" field (see clause "
            "5.5.9) are used for this purpose). | Related TSL field (if any): Scheme type/community/rules | "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/RootCA-QC - Meaning: A Root Certification "
            "Authority from which a certification path can be established down to a Certification Authority "
            "issuing qualified certificates. This value shall not be used if the service type is not "
            "http://uri.etsi.org/TrstSvc/Svctype/CA/QC | Related TSL field (if any): Service information "
            "extensions/additionalServiceInformation Extension/"
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Il testo descrittivo puntato dall'URI .../schemerules/CC e' specifico della trusted list del CC cui "
            "si riferisce (CC = codice del campo \"Scheme territory\", clausola 5.3.10); il valore "
            ".../SvcInfoExt/RootCA-QC non e' utilizzabile se il tipo di servizio non e' "
            "http://uri.etsi.org/TrstSvc/Svctype/CA/QC."
        ),
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "Annex D.5.4 (Service information extensions/Qualifications Extension/Qualifiers)",
        "testo": (
            "Registra tredici URI .../SvcInfoExt/... che qualificano l'informazione aggiuntiva di servizio "
            "(qualificatori) per i certificati qualificati emessi dal servizio identificato in \"Service digital "
            "identity\" e filtrati tramite Sdi: QCWithSSCD, QCNoSSCD, QCSSCDStatusAsInCert, QCForLegalPerson, "
            "QCStatement, QCWithQSCD, QCNoQSCD, QCQSCDStatusAsInCert, QCQSCDManagedOnBehalf (supporto/assenza di "
            "supporto SSCD o QSCD, stato SSCD/QSCD come in certificato, gestione della chiave privata in QSCD per "
            "conto dell'entita' certificata, certificati emessi a persone giuridiche, certificati emessi come "
            "qualificati), QCForESig, QCForESeal, QCForWSA (certificati qualificati rispettivamente per firme "
            "elettroniche, sigilli elettronici e autenticazione di siti web, in conformita' alla legislazione "
            "applicabile) e NotQualified (certificati da non considerare qualificati). Per ciascun valore il "
            "testo stabilisce che esso non deve essere usato se il tipo di servizio non e' "
            "http://uri.etsi.org/TrstSvc/Svctype/CA/QC."
        ),
        "testo_integrale": (
            "D.5.4 Service information extensions/Qualifications Extension/Qualifiers: "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCWithSSCD - QCWithSSCD: it is ensured by the "
            "trust service provider and controlled (supervision model) or audited (accreditation model) by the "
            "referenced Member State (respectively its Supervisory Body or Accreditation Body) that all Qualified "
            "Certificates issued under the service identified in \"Service digital identity\" and further "
            "identified by the filters information used to further identify under the \"Sdi\" identified trust "
            "service that precise set of Qualified Certificates for which this additional information is required "
            "with regards to the presence or absence of Secure Signature Creation Device (SSCD) support ARE "
            "supported by an SSCD (i.e. that means that the private key associated with the public key in the "
            "certificate is stored in a Secure Signature Creation Device conformant with the applicable European "
            "legislation). This value shall not be used if the service type is not "
            "http://uri.etsi.org/TrstSvc/Svctype/CA/QC. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCNoSSCD - QCNoSSCD: it is ensured by the trust "
            "service provider and controlled (supervision model) or audited (accreditation model) by the "
            "referenced Member State (respectively its Supervisory Body or Accreditation Body) that all Qualified "
            "Certificates issued under the service identified in \"Service digital identity\" and further "
            "identified by the filters information used to further identify under the \"Sdi\" identified trust "
            "service that precise set of Qualified Certificates for which this additional information is required "
            "with regards to the presence or absence of Secure Signature Creation Device (SSCD) support ARE NOT "
            "supported by an SSCD (i.e. that means that the private key associated with the public key in the "
            "certificate is not stored in a Secure Signature Creation Device conformant with the applicable "
            "European legislation). This value shall not be used if the service type is not "
            "http://uri.etsi.org/TrstSvc/Svctype/CA/QC. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCSSCDStatusAsInCert - QCSSCDStatusAsInCert: it "
            "is ensured by the trust service provider and controlled (supervision model) or audited "
            "(accreditation model) by the referenced Member State (respectively its Supervisory Body or "
            "Accreditation Body) that all Qualified Certificates issued under the service identified in \"Service "
            "digital identity\" and further identified by the filters information used to further identify under "
            "the \"Sdi\" identified trust service that precise set of Qualified Certificates for which this "
            "additional information is required with regards to the presence or absence of Secure Signature "
            "Creation Device (SSCD) support DO contain the machine-processable information indicating whether or "
            "not the Qualified Certificate is supported by an SSCD. This value shall not be used if the service "
            "type is not http://uri.etsi.org/TrstSvc/Svctype/CA/QC. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCForLegalPerson - QCForLegalPerson: it is "
            "ensured by the trust service provider and controlled (supervision model) or audited (accreditation "
            "model) by the referenced Member State (respectively its Supervisory Body or Accreditation Body) that "
            "all Qualified Certificates issued under the service identified in \"Service digital identity\" and "
            "further identified by the filters information used to further identify under the \"Sdi\" identified "
            "trust service that precise set of Qualified Certificates for which this additional information is "
            "required with regards to the issuance to Legal Person ARE issued to Legal Persons. This value shall "
            "not be used, if the service type is not http://uri.etsi.org/TrstSvc/Svctype/CA/QC. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCStatement - QCStatement: it is ensured by the "
            "trust service provider and supervised by the Member State Supervisory Body that all certificates "
            "issued under the service identified in 'Service digital identity' (clause 5.5.3) and further "
            "identified by the filters information used to further identify under the 'Sdi' identified trust "
            "service that precise set of certificates are issued as qualified certificates. This value shall not "
            "be used, if the service type is not http://uri.etsi.org/TrstSvc/Svctype/CA/QC. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCWithQSCD - QCWithQSCD: it is ensured by the "
            "trust service provider and supervised by the Member State Supervisory Body that all Qualified "
            "Certificates issued under the service identified in \"Service digital identity\" and further "
            "identified by the filters information used to further identify under the \"Sdi\" identified trust "
            "service that precise set of Qualified Certificates for which this additional information is required "
            "with regards to the presence or absence of Qualified Signature or Seal Creation Device (QSCD) "
            "support ARE supported by a QSCD (i.e. that means that the private key associated with the public key "
            "in the certificate resides in a QSCD conformant with the applicable European legislation); This "
            "value shall not be used if the service type is not http://uri.etsi.org/TrstSvc/Svctype/CA/QC. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCNoQSCD - QCNoQSCD: it is ensured by the trust "
            "service provider and supervised by the Member State Supervisory Body that all Qualified Certificates "
            "issued under the service identified in \"Service digital identity\" and further identified by the "
            "filters information used to further identify under the \"Sdi\" identified trust service that precise "
            "set of Qualified Certificates for which this additional information is required with regards to the "
            "presence or absence of Qualified Signature or Seal Creation Device (QSCD) support ARE NOT supported "
            "by a QSCD (i.e. that means that the private key associated with the public key in the certificate "
            "does not reside in a QSCD conformant with the applicable European legislation). This value shall not "
            "be used if the service type is not http://uri.etsi.org/TrstSvc/Svctype/CA/QC. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCQSCDStatusAsInCert - QCQSCDStatusAsInCert: it "
            "is ensured by the trust service provider and supervised by the Member State Supervisory Body that "
            "all Qualified Certificates issued under the service identified in \"Service digital identity\" and "
            "further identified by the filters information used to further identify under the \"Sdi\" identified "
            "trust service that precise set of Qualified Certificates for which this additional information is "
            "required with regards to the presence or absence of Qualified Signature or Seal Creation Device "
            "(QSCD) support DO contain the machine-processable information indicating whether or not the "
            "Qualified Certificate is supported by a QSCD. This value shall not be used if the service type is "
            "not http://uri.etsi.org/TrstSvc/Svctype/CA/QC. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCQSCDManagedOnBehalf - QCQSCDManagedOnBehalf: it "
            "is ensured by the trust service provider and supervised by the Member State Supervisory Body that "
            "all Qualified Certificates issued under the service identified in \"Service digital identity\" and "
            "further identified by the filters information used to further identify under the \"Sdi\" identified "
            "trust service that precise set of Qualified Certificates for which this additional information is "
            "required with regards to the presence or absence of Qualified Signature or Seal Creation Device "
            "(QSCD) support have their private key residing in a QSCD for which the generation and management of "
            "that private key is done by the qualified TSP on behalf of the entity whose identity is certified in "
            "the certificate in accordance with the applicable legislation. This value shall not be used if the "
            "service type is not http://uri.etsi.org/TrstSvc/Svctype/CA/QC. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCForESig - QCForESig: it is ensured by the trust "
            "service provider and supervised by the Member State Supervisory Body that all Qualified Certificates "
            "issued under the service identified in \"Service digital identity\" and further identified by the "
            "filters information used to further identify under the \"Sdi\" identified trust service that precise "
            "set of qualified certificates for which this additional information is required with regards to the "
            "nature of the qualified certificate ARE qualified certificates for electronic signatures in "
            "accordance with the applicable legislation. This value shall not be used if the service type is not "
            "http://uri.etsi.org/TrstSvc/Svctype/CA/QC | "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCForESeal - QCForESeal: it is ensured by the "
            "trust service provider and supervised by the Member State Supervisory Body that all Qualified "
            "Certificates issued under the service identified in \"Service digital identity\" and further "
            "identified by the filters information used to further identify under the \"Sdi\" identified trust "
            "service that precise set of qualified certificates for which this additional information is required "
            "with regards to the nature of the qualified certificate ARE qualified certificates for electronic "
            "seals in accordance with the applicable legislation. This value shall not be used if the service "
            "type is not http://uri.etsi.org/TrstSvc/Svctype/CA/QC | "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCForWSA - QCForWSA: it is ensured by the trust "
            "service provider and supervised by the Member State Supervisory Body that all Qualified Certificates "
            "issued under the service identified in \"Service digital identity\" and further identified by the "
            "filters information used to further identify under the \"Sdi\" identified trust service that precise "
            "set of qualified certificates for which this additional information is required with regards to the "
            "nature of the qualified certificate ARE qualified certificates for web site authentication in "
            "accordance with the applicable legislation. This value shall not be used if the service type is not "
            "http://uri.etsi.org/TrstSvc/Svctype/CA/QC | "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/NotQualified - NotQualified: it is ensured by the "
            "trust service provider, and supervised by the Member State Supervisory Body that all certificates "
            "issued under the service identified in 'Service digital identity' (clause 5.5.3) and further "
            "identified by the filters information used to further identify under the 'Sdi' identified trust "
            "service that precise set of certificates are not to be considered as qualified certificates. This "
            "value shall not be used, if the service type is not http://uri.etsi.org/TrstSvc/Svctype/CA/QC"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "I qualificatori si riferiscono ai certificati qualificati del servizio di tipo "
            "http://uri.etsi.org/TrstSvc/Svctype/CA/QC identificato in \"Service digital identity\" (clausola "
            "5.5.3) e ulteriormente identificati dalle informazioni di filtro Sdi; ciascun valore non e' "
            "utilizzabile se il tipo di servizio non e' http://uri.etsi.org/TrstSvc/Svctype/CA/QC."
        ),
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "Annex D.5.6 (Service current and previous statuses)",
        "testo": (
            "Registra tredici URI di stato del servizio sotto il radix Common Domain, con significato e regole "
            "normative d'uso: undersupervision (Under Supervision), supervisionincessation (Supervision of "
            "Service in Cessation), supervisionceased (Supervision Ceased), supervisionrevoked (Supervision "
            "Revoked), accredited (Accredited), accreditationceased (Accreditation Ceased), accreditationrevoked "
            "(Accreditation Revoked), granted (Granted), withdrawn (Withdrawn), setbynationallaw (Set by national "
            "law), recognisedatnationallevel (Recognized at national level), deprecatedbynationallaw (Deprecated "
            "by national law) e deprecatedatnationallevel (Deprecated at national level). Regole prescrittive: "
            "l'identificazione del soggetto subentrante (fallback trust service provider) deve essere fornita nel "
            "campo \"Scheme service definition URI\" (clausola 5.5.6) e nell'estensione \"TakenOverBy\" (clausola "
            "5.5.9.3); gli stati \"Supervision of Service in Cessation\" e \"Supervision Ceased\" devono essere "
            "usati quando un TSP cessa direttamente i propri servizi sotto supervisione e non quando la "
            "supervisione e' stata revocata; lo stato \"Supervision Revoked\" puo' essere definitivo e non deve "
            "essere migrato (senza stato intermedio) verso \"Supervision of Service in Cessation\" o "
            "\"Supervision Ceased\", e il servizio deve essere considerato dai relying party come cessato per "
            "tale ragione."
        ),
        "testo_integrale": (
            "D.5.6 Service current and previous statuses: "
            "http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/undersupervision - Under Supervision: The service "
            "identified in \"Service digital identity\" (see clause 5.5.3) provided by the trust service provider "
            "identified in \"TSP name\" (see clause 5.4.1) is currently under supervision, for compliance with "
            "the provisions laid down in the applicable European legislation, by the Member State identified in "
            "the \"Scheme territory\" (see clause 5.3.10) in which the trust service provider is established. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionincessation - Supervision of Service in "
            "Cessation: The service identified in \"Service digital identity\" (see clause 5.5.3) provided by the "
            "trust service provider identified in \"TSP name\" (see clause 5.4.1) is currently in a cessation "
            "phase but still supervised until supervision is ceased or revoked. In the event a different person "
            "than the one identified in \"TSP name\" has taken over the responsibility of ensuring this cessation "
            "phase, the identification of this new or fallback person (fallback trust service provider) shall be "
            "provided in \"Scheme service definition URI\" (clause 5.5.6) and in the \"TakenOverBy\" extension "
            "(clause 5.5.9.3) of the service entry. \"Supervision of Service in Cessation\" status shall be used "
            "when a TSP directly ceases its related services under supervision; it shall not be used when "
            "supervision has been revoked. | http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionceased "
            "- Supervision Ceased: The validity of the supervision assessment has lapsed without the service "
            "identified in \"Service digital identity\" (see clause 5.5.3) being re-assessed. The service is "
            "currently not under supervision any more from the date of the current status as the service is "
            "understood to have ceased operations. \"Supervision Ceased\" status shall be used when a TSP "
            "directly ceases its related services under supervision; it shall not be used when supervision has "
            "been revoked. | http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionrevoked - Supervision "
            "Revoked: Having been previously supervised, the trust service provider's service and potentially the "
            "trust service provider itself has failed to continue to comply with the provisions laid down in the "
            "applicable European legislation, as determined by the Member State identified in the \"Scheme "
            "territory\" (see clause 5.3.10) in which the trust service provider is established. Accordingly the "
            "service has been required to cease its operations and shall be considered by relying parties as "
            "ceased for the above reason. The status value \"Supervision Revoked\" may be a definitive status, "
            "even if the trust service provider then completely ceases its activity; it shall not be migrated "
            "(without any intermediate status) to either \"Supervision of Service in Cessation\" or to "
            "\"Supervision Ceased\" status in this case. The only way to change the \"Supervision Revoked\" "
            "status is to recover from non-compliance to compliance with the provisions laid down in the "
            "applicable European legislation according to the appropriate supervision system in force in the "
            "Member State owing the trusted list, and regaining \"Under Supervision\" status. \"Supervision of "
            "Service in Cessation\" status, or \"Supervision Ceased\" status shall be used when a TSP directly "
            "ceases its related services under supervision; they shall not be used when supervision has been "
            "revoked. | http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/accredited - Accredited: An "
            "accreditation assessment has been performed by the Accreditation Body on behalf of the Member State "
            "identified in the \"Scheme territory\" (see clause 5.3.10) and the service identified in \"Service "
            "digital identity\" (see clause 5.5.3) provided by the trust service provider identified in \"TSP "
            "name\" (see clause 5.4.1) is found to be in compliance with the provisions laid down in the "
            "applicable legislation. This accredited trust service provider may be established in another Member "
            "State than the one identified in the \"Scheme territory\" (see clause 5.3.10) of the trusted list or "
            "in a non-EU country. | http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/accreditationceased - "
            "Accreditation Ceased: The validity of the accreditation assessment has lapsed without the service "
            "identified in \"Service digital identity\" (see clause 5.5.3) being re-assessed. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/accreditationrevoked - Accreditation Revoked: "
            "Having been previously found to be in conformance with the scheme criteria, the service identified "
            "in \"Service digital identity\" (see clause 5.5.3) provided by the trust service provider identified "
            "in \"TSP name\" (see clause 5.4.1) and potentially the trust service provider itself have failed to "
            "continue to comply with the provisions laid down in the applicable European legislation. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted - Granted: Following ex ante and active "
            "approval activities, in compliance with the provisions laid down in the applicable national "
            "legislation and Regulation (EU) No 910/2014 [i.10], it indicates that the Supervisory Body "
            "identified in the \"Scheme operator name\" (see clause 5.3.4) on behalf of the Member State "
            "identified in the \"Scheme territory\" (see clause 5.3.10) has granted a qualified status: to the "
            "corresponding trust service being of a service type specified in clause 5.5.1.1 and identified in "
            "\"Service digital identity\" (see clause 5.5.3), and to the trust service provider identified in "
            "\"TSP name\" (see clause 5.4.1) for the provision of that service. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn - Withdrawn: In compliance with the "
            "provisions laid down in the applicable national legislation and Regulation (EU) No 910/2014 [i.10], "
            "it indicates that the qualified status has not been initially granted or has been withdrawn by the "
            "Supervisory Body on behalf of the Member State identified in the \"Scheme territory\" (see clause "
            "5.3.10): from the trust service being of a service type specified in clause 5.5.1.1 and identified "
            "in \"Service digital identity\" (see clause 5.5.3), and from its trust service provider identified "
            "in \"TSP name\" (see clause 5.4.1) for the provision of that service. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/setbynationallaw - Set by national law: For "
            "NationalRootCA-QC type: The service is set by national law in accordance with the applicable "
            "European legislation and operated by the responsible national body issuing root-signing or qualified "
            "certificates to accredited trust service providers. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/recognisedatnationallevel - Recognized at national "
            "level: For trust services listed under a service type specified in clause 5.5.1.2: In compliance "
            "with the provisions laid down in the applicable national legislation, it indicates that the "
            "Supervisory Body identified in the \"Scheme operator name\" (see clause 5.3.4) on behalf of the "
            "Member State identified in the \"Scheme territory\" (see clause 5.3.10) has granted an \"approved\" "
            "status, as recognized at national level, to the corresponding trust service identified in \"Service "
            "digital identity\" (see clause 5.5.3) and to the trust service provider identified in \"TSP name\" "
            "(see clause 5.4.1) for the provision of that service, as both the TSP and the trust service it "
            "provides meet the provisions laid down in Regulation (EU) No 910/2014 [i.10] and the applicable "
            "national legislation. For NationalRootCA-QC type: The service is set by national law in accordance "
            "with the applicable European legislation and operated by the responsible national body issuing "
            "root-signing or qualified certificates to accredited trust service providers. For other trust "
            "services listed under a service type specified in clause 5.5.1.3: In compliance with the provisions "
            "laid down in the applicable national legislation, it indicates that the Supervisory Body identified "
            "in the \"Scheme operator name\" (see clause 5.3.4) on behalf of the Member State identified in the "
            "\"Scheme territory\" (see clause 5.3.10) has granted an \"approved\" status, as recognized at "
            "national level, to the corresponding trust service identified in \"Service digital identity\" (see "
            "clause 5.5.3) and to the trust service provider identified in \"TSP name\" (see clause 5.4.1) for "
            "the provision of that service, as both the TSP and the trust service it provides meet the provisions "
            "laid down in the applicable national legislation. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/deprecatedbynationallaw - Deprecated by national "
            "law [i.10]: For NationalRootCA-QC type: The service is deprecated by national law in accordance with "
            "the applicable European legislation and by the responsible national body issuing root-signing or "
            "qualified certificates to accredited trust service providers. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/deprecatedatnationallevel - Deprecated at national "
            "level: For NationalRootCA-QC type: The service is deprecated by national law in accordance with the "
            "applicable European legislation and by the responsible national body issuing root-signing or "
            "qualified certificates to accredited trust service providers. For other trust services listed under "
            "a service type specified in clause 5.5.1.2 or in clause 5.5.1.3: In compliance with the provisions "
            "laid down in the applicable EU or national legislation, it indicates that the previously "
            "\"approved\" status has been withdrawn by the Supervisory Body on behalf of the Member State "
            "identified in the \"Scheme territory\" (see clause 5.3.10) from the trust service identified in "
            "\"Service digital identity\" (see clause 5.5.3) and from its trust service provider identified in "
            "\"TSP name\" (see clause 5.4.1) for the provision of that service."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "Annex C (XML schema)",
        "testo": (
            "L'Annex C (normativo) dichiara che il documento ha un file ZIP elettronico associato "
            "\"ts_119612v020401p0.zip\" che contiene gli XML schema che sono parti integranti del documento "
            "stesso e ulteriormente descritti nello stesso annesso: in caso di conflitto tra una parte del modulo "
            "e/o degli schema dell'allegato elettronico e il testo del documento, il testo del documento prevale "
            "come fonte autoritativa. I file XML Schema sono inoltre disponibili nel repository "
            "https://forge.etsi.org/rep/esi/x19_612_trusted_lists. Non enuncia un requisito comportamentale "
            "autonomo ne' individua un soggetto obbligato (la regola di prevalenza e' dichiarativa); l'obbligo di "
            "conformita' agli schema XML e' posto dalla clausola 6."
        ),
        "testo_integrale": (
            "Annex C (normative): XML schema The present document has an associated electronic ZIP file "
            "\"ts_119612v020401p0.zip\" that contains the XML schemas that are integral parts of the present "
            "document and further described below. In the event that any part of the module and/or schemas within "
            "this electronic attachment are in conflict with the text of the present document, the present "
            "document shall prevail as the authoritative source. The XML Schema files are also available in the "
            "following repository: https://forge.etsi.org/rep/esi/x19_612_trusted_lists."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex D.0 (General)",
        "testo": (
            "Introduzione del registro normativo degli URI dell'Annex D: sono registrati in connessione con il "
            "documento gli URI con radix (base) \"http://uri.etsi.org/19612/……\", registrati e dichiarati per la "
            "loro stessa presenza nel documento per un uso specifico al suo interno, e quelli con radix "
            "\"http://uri.etsi.org/TrstSvc/……\", registrati da ETSI come Common Domain per conto del TC ESI in "
            "ragione della loro applicabilita' e uso piu' ampi. Descrive inoltre il layout di ogni dichiarazione "
            "di URI: l'URI come stringa non interrotta, il significato rientrato in relazione all'URI precedente "
            "e il campo TSL correlato (se presente); quando piu' URI afferiscono a un medesimo campo TL la "
            "seconda colonna si estende su tutte le dichiarazioni (coppie di righe) applicabili."
        ),
        "testo_integrale": (
            "D.0 General: This annex specifies those Uniform Resource Identifiers (URIs) which have been "
            "registered in connection with the present document. Those with the radix (base) "
            "\"http://uri.etsi.org/19612/……\" are registered and declared by their presence in the present "
            "document, for specific usage within the present document: those with the radix "
            "\"http://uri.etsi.org/TrstSvc/……\" are registered by ETSI as a Common Domain (see "
            "http://portal.etsi.org/pnns/xml.asp#Common_Domain) on behalf of the TC ESI because they have a wider "
            "applicability and usage and are defined in the present document. In the following tables the "
            "following layout is used for each URI declaration: The URI is given as an unbroken string. The "
            "meaning of the URI is given, indented to emphasize its relationship to the preceding URI. Related "
            "TSL field (if any). Where more than one URI relates to a specific TL field the second column will "
            "extend across all URI declarations (row-pairs) which apply."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex D.1 (URIs registered within the present document)",
        "testo": (
            "Dichiara e registra sotto il radix assegnato al documento tre URI: http://uri.etsi.org/19612/TSLTag "
            "(struttura dati conforme alla specifica TSL pubblicata in ETSI TS 119 612 in qualunque sua edizione "
            "storica o in questa, campo TSL \"TSL tag\"); http://uri.etsi.org/02231/v2# (identificatore del "
            "namespace XML relativo alla versione TSL specificata in questa edizione del documento, campo TSL "
            "\"N/a\"); http://uri.etsi.org/19612/TDPContainer (qualificatore per pagine web che contengono uno o "
            "piu' TDP, utilizzabile come valore dell'attributo \"profile\" dell'elemento \"head\" della pagina, "
            "campo TSL \"N/a\")."
        ),
        "testo_integrale": (
            "D.1 URIs registered within the present document: The following URIs are hereby declared and "
            "registered under the present document's assigned radix: http://uri.etsi.org/19612/TSLTag - Meaning: "
            "A data structure which conforms to the TSL specification published in ETSI TS 119 612 in any of its "
            "historical issues or this one. | Related TSL field (if any): TSL tag | http://uri.etsi.org/02231/v2# "
            "- Meaning: The XML namespace identifier relating to the TSL version specified in this issue of ETSI "
            "TS 119 612. | Related TSL field (if any): N/a | http://uri.etsi.org/19612/TDPContainer - Meaning: A "
            "qualifier for web pages that contain one or more TDPs which can be used as a value of the attribute "
            "\"profile\" for the \"head\" element of the web page. | Related TSL field (if any): N/a"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex D.2 (ETSI Common Domain URIs)",
        "testo": (
            "Sottoclausola dichiarata \"Void\": nessun URI dell'ETSI Common Domain e' registrato in questo "
            "documento. Nodo di cornice conservato per copertura completa della numerazione dell'Annex D "
            "(ADR-0007); non enuncia alcun requisito."
        ),
        "testo_integrale": (
            "D.2 ETSI Common Domain URIs Void."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex D.3 (Scheme registered URIs)",
        "testo": (
            "Descrive la facolta' di un'organizzazione che gestisce uno scheme di creare URI propri per i propri "
            "fini (o di chiedere a ETSI l'assegnazione di un URI root registrato sotto l'ETSI Identified "
            "Organization Domain) e di registrarne alcuni quando integrano gli URI richiesti o utilizzabili nella "
            "pubblicazione di una TL. Riporta due esempi non normativi (\"Potential URI\") con il rispettivo "
            "significato e il campo TSL correlato (Scheme type/community/rules al livello secondario): "
            "http://uri.etsi.org/\"registered_org\"/\"schemename\" e "
            "http://\"scheme_op_URI_root\"/.../schemerules/\"schemename\"."
        ),
        "testo_integrale": (
            "D.3 Scheme registered URIs: Any organization operating a scheme might choose to create its own URIs "
            "for its own specific purposes or request ETSI to assign a registered URI root under the ETSI "
            "Identified Organization Domain (see http://portal.etsi.org/pnns/xml.asp), and then define its own "
            "URIs under this root. It might be appropriate to register certain of those URIs where they "
            "complement URIs required by or which might be used in the context of the publication of a TL. The "
            "following examples suggest how additional URIs could be created, including showing a second level of "
            "rules, after using the applicable Optional URI as shown above. Potential URI: "
            "http://uri.etsi.org/\"registered_org\"/\"schemename\" - Meaning: This could mean an assessment "
            "scheme called \"schemename\" being operated by \"registered_org\", where \"registered_org\" is "
            "replaced by the name of the scheme operator and \"schemename\" is replaced by the actual scheme "
            "name. | Potential URI: http://\"scheme_op_URI_root\"/.../schemerules/\"schemename\" - Meaning: This "
            "URI would be registered under a different root, e.g. the scheme operator's, distinguished by "
            "\"scheme_op_URI_root\", or it could be another organization which maintains a registry of URIs. This "
            "URI could mean an assessment scheme called \"schemename\" being operated by \"scheme_op\" where "
            "\"scheme_op\" is replaced by the name of the scheme operator and \"schemename\" is replaced by the "
            "actual scheme name. | Related TSL field (if any): Scheme type/community/rules (at the secondary "
            "level)"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex D.5 (EU specific trusted lists URIs)",
        "testo": (
            "Sottoclausola di raggruppamento dell'Annex D, priva di prosa propria oltre al titolo: introduce la "
            "sezione degli URI specifici dell'Unione europea, i cui valori registrati sono dichiarati nelle "
            "sottoclausole D.5.1-D.5.6 ed e' il bersaglio dei rinvii testuali \"as defined in clause D.5\" di "
            "questo standard."
        ),
        "testo_integrale": (
            "D.5 EU specific trusted lists URIs"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex D.5.1 (TSL Type)",
        "testo": (
            "Registra sotto il radix http://uri.etsi.org/TrstSvc/TrustedList/ gli URI TSLType/EUgeneric "
            "(implementazione di TL come lista di stati di supervisione/accreditamento di servizi fiduciari "
            "sottoposti a oversight diretto dello Stato membro titolare, volontario o regolamentato) e "
            "TSLType/EUlistofthelists (implementazione di TL come lista compilata di puntatori verso le liste di "
            "stato dei servizi fiduciari degli Stati membri)."
        ),
        "testo_integrale": (
            "D.5.1 TSL Type: The following URIs, are registered under the radix "
            "http://uri.etsi.org/TrstSvc/TrustedList/. http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric "
            "- Meaning: A TL implementation of a supervision/accreditation status list of trust services from "
            "trust service providers which are supervised/accredited by the referenced Member State owning the TL "
            "implementation for compliance with the relevant provisions laid down in the applicable European "
            "legislation, through a process of direct oversight (whether voluntary or regulatory). | "
            "http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUlistofthelists - Meaning: A TL implementation of a "
            "compiled list of pointers towards Member States supervision/accreditation status lists of trust "
            "services from trust service providers which are supervised/accredited by the referenced Member State "
            "owning the pointed TL implementation for compliance with the relevant provisions laid down in the "
            "applicable European legislation, through a process of direct oversight (whether voluntary or "
            "regulatory)."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex D.5.2 (Status determination approach)",
        "testo": (
            "Registra l'URI StatusDetn/EUappropriate: gli stati dei servizi elencati sono determinati da o per "
            "conto dello Scheme Operator secondo un sistema appropriato definito dall'implementazione nazionale "
            "della legislazione europea applicabile e ulteriormente descritto nelle informazioni puntate dal "
            "campo \"Scheme information URI\"."
        ),
        "testo_integrale": (
            "D.5.2 Status determination approach: "
            "http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate - Meaning: Services listed have "
            "their status determined by or on behalf of the Scheme Operator under an appropriate system as "
            "defined by the Member State implementation of the applicable European legislation and further "
            "described in the 'Scheme information URI' pointed-to information."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex D.5.3 (Scheme type/community/rules)",
        "testo": (
            "Registra gli URI schemerules/EUlistofthelists (testo descrittivo sullo scheme of schemes e sulle "
            "regole e policy che lo guidano) e schemerules/EUcommon (testo descrittivo applicabile a tutte le "
            "trusted list degli Stati membri UE: partecipazione al scheme generale, policy/regole di valutazione "
            "dei servizi elencati e regole comuni di uso e interpretazione del contenuto)."
        ),
        "testo_integrale": (
            "D.5.3 Scheme type/community/rules: "
            "http://uri.etsi.org/TrstSvc/TrustedList/schemerules/EUlistofthelists - Meaning: A URI pointing "
            "towards a descriptive text where users can obtain information about the scheme of schemes type (i.e. "
            "a compiled list listing pointers to all trusted lists published as part of the scheme of schemes and "
            "maintained in the form of a TL) and the relevant driving rules and policy. | "
            "http://uri.etsi.org/TrstSvc/TrustedList/schemerules/EUcommon - Meaning: A URI pointing towards a "
            "descriptive text that applies to all EU Member States' trusted lists: • By which participation of "
            "the Member States' trusted lists is denoted in the general scheme of the EU Member States trusted "
            "lists. • Where users can obtain policy/rules against which services included in the trusted list are "
            "assessed. • Where users can obtain description about how to use and interpret the content of the EU "
            "Member States' trusted list. These usage rules are common to all EU Member States' trusted lists "
            "whatever the type of listed services."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex D.5.5 (Service information extensions/additionalServiceInformation Extension)",
        "testo": (
            "Registra tre URI .../SvcInfoExt/... che specificano ulteriormente che il servizio identificato dal "
            "\"Service type identifier\" e' fornito, rispettivamente, per firme elettroniche (ForeSignatures), "
            "sigilli elettronici (ForeSeals) e autenticazione di siti web (ForWebSiteAuthentication)."
        ),
        "testo_integrale": (
            "D.5.5 Service information extensions/additionalServiceInformation Extension: "
            "http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/ForeSignatures - For eSignatures: Further "
            "specifies the \"Service type identifier\" identified service as being provided for electronic "
            "signatures. | http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/ForeSeals - For eSeals: Further "
            "specifies the \"Service type identifier\" identified service as being provided for electronic seals. "
            "| http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/ForWebSiteAuthentication - For Web Site "
            "Authentication: Further specifies the \"Service type identifier\" identified service as being "
            "provided for web site authentication."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex D.6 (Non-EU specific trusted lists URIs)",
        "testo": (
            "Registra sotto il radix \"http://uri.etsi.org/TrstSvc/……\" gli URI TSLType/CClist e "
            "TSLType/CClistofthelists (campo TSL \"TSL type\") e StatusDetn/CCdetermination (campo TSL \"Status "
            "determination approach\"), dove \"CC\" e' sostituito da una stringa che identifica la community cui "
            "si applica (es. \"ASEAN\", \"GCC\" o il Country Code alpha-2 ISO 3166-1 usato nel campo \"Scheme "
            "territory\", clausola 5.3.10). TSLType/CClist indica una trusted list con informazioni di stato di "
            "approvazione basate su un assessment scheme; TSLType/CClistofthelists una lista compilata di "
            "puntatori verso le liste dei membri della community."
        ),
        "testo_integrale": (
            "D.6 Non-EU specific trusted lists URIs The following URIs, are registered under the radix "
            "\"http://uri.etsi.org/TrstSvc/……\": http://uri.etsi.org/TrstSvc/TrustedList/TSLType/CClist - "
            "Meaning: where \"CC\" is replaced by a character string identifying the community to which it "
            "applies (e.g. \"ASEAN\", \"GCC\" or the ISO 3166-1 [15] alpha-2 Country Code used in the 'Scheme "
            "territory field' (clause 5.3.10)). Indicates a trusted list providing assessment scheme based "
            "approval status information about trust services from trust service providers which are approved by "
            "the competent trusted list scheme operator or by the State or body in charge from which the scheme "
            "operator depends or by which it is mandated, for compliance with the relevant provisions of the "
            "applicable approval scheme and/or the applicable legislation. | Related TSL field (if any): TSL type "
            "| http://uri.etsi.org/TrstSvc/TrustedList/TSLType/CClistofthelists - Meaning: where \"CC\" is "
            "replaced by a character string identifying the community to which it applies (e.g. \"ASEAN\", "
            "\"GCC\" or the ISO 3166-1 [15] alpha-2 Country Code used in the 'Scheme territory field' (clause "
            "5.3.10)). Indicates a compiled list of pointers towards community members' lists of trust services "
            "from trust service providers which are approved by the competent trusted list scheme operator or by "
            "the State or body in charge from which the scheme operator depends or by which it is mandated, for "
            "compliance with the relevant provisions of the applicable approval scheme and/or the applicable "
            "legislation. | Related TSL field (if any): TSL type | "
            "http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/CCdetermination - Meaning: where \"CC\" is "
            "replaced by a character string identifying the community to which it applies (e.g. \"ASEAN\", "
            "\"GCC\" or the ISO 3166-1 [15] alpha-2 Country Code used in the 'Scheme territory field' (clause "
            "5.3.10)). Services listed have their status determined after assessment by or on behalf of the "
            "scheme operator against the scheme's criteria (active approval/recognition) and as further described "
            "in the 'Scheme information URI' pointed-to information. | Related TSL field (if any): Status "
            "determination approach"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "Annex D.4 (Common trusted lists URIs)",
    "Annex D.5.4 (Service information extensions/Qualifications Extension/Qualifiers)",
    "Annex D.5.6 (Service current and previous statuses)",
    "Annex C (XML schema)",
    "Annex D.0 (General)",
    "Annex D.1 (URIs registered within the present document)",
    "Annex D.2 (ETSI Common Domain URIs)",
    "Annex D.3 (Scheme registered URIs)",
    "Annex D.5 (EU specific trusted lists URIs)",
    "Annex D.5.1 (TSL Type)",
    "Annex D.5.2 (Status determination approach)",
    "Annex D.5.3 (Scheme type/community/rules)",
    "Annex D.5.5 (Service information extensions/additionalServiceInformation Extension)",
    "Annex D.6 (Non-EU specific trusted lists URIs)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "Annex D.4 (Common trusted lists URIs)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.10 (Scheme territory)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D.4 (Common trusted lists URIs)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.6 (Scheme service definition URI)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D.4 (Common trusted lists URIs)"),
        "nodo_a": ("principio", None, "clausola 5.5.9 (Service information extensions)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D.5.4 (Service information extensions/Qualifications Extension/Qualifiers)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D.5.6 (Service current and previous statuses)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.4 (Scheme operator name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D.5.6 (Service current and previous statuses)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.10 (Scheme territory)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D.5.6 (Service current and previous statuses)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.1 (TSP name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D.5.6 (Service current and previous statuses)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.1 (Regulation (EU) No 910/2014 qualified trust service types)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D.5.6 (Service current and previous statuses)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.2 (Regulation (EU) No 910/2014 non qualified trust service types)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D.5.6 (Service current and previous statuses)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.3 (Trust service types not defined in Regulation (EU) No 910/2014 but nationally defined)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D.5.6 (Service current and previous statuses)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D.5.6 (Service current and previous statuses)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.6 (Scheme service definition URI)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D.5.6 (Service current and previous statuses)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.3 (TakenOverBy Extension)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Annex D.6 (Non-EU specific trusted lists URIs)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.10 (Scheme territory)"),
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
