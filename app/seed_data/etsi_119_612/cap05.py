"""ETSI TS 119 612 V2.4.1 (2025-08) - Electronic Signatures and Trust
Infrastructures (ESI); Trusted Lists.
Fonte 21 (la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 5 del
manifest: clausola 6 Operations (6.1 TL publication, 6.2.1.1 HTTP-Media Type,
6.2.2 MIME registrations, 6.3 TL Distribution Points in trust service tokens,
6.4 TL availability, 6.5 TLSO practices), Annex A (informative: A.1
Authenticating and trusting a TL, A.2 Ensuring continuity in TL
authentication) e Annex B (normative: B.0 General requirements, B.1.0 General,
B.1.1 The scheme operator identifier in XAdES signatures, B.1.2 Algorithm and
parameters). Testo ufficiale in app/.source_cache/etsi_119_612/cap05.txt (letto
sempre con selettore `:raw`, altrimenti il tool tronca le righe lunghe a 768
caratteri introducendo "..."), mutilando la copia verbatim. Manifest di split:
app/.source_cache/etsi_119_612/manifest.json.

Modellazione (ADR-0007), stesso criterio dei capitoli cap01-cap04 di questa
fonte e delle altre fonti ETSI censite: un nodo per ogni clausola o
sottoclausola numerata con contenuto proprio, un nodo per ogni clausola di
cornice priva di requisito numerato; le intestazioni di puro raggruppamento non
generano nodo. Scelte voce per voce:

- Clausola 6 (Operations) -> NESSUN nodo: intestazione di puro raggruppamento,
  seguita immediatamente dalla sottoclausola 6.1, senza periodo proprio. Lo
  stesso vale per 6.2 (Transport Protocols), seguita subito da 6.2.1, e per
  6.2.1 (HTTP-Transport), seguita subito da 6.2.1.1. Si noti che 6.2.2 (MIME
  registrations) e' figlia diretta di 6.2 e non di 6.2.1: la numerazione del
  documento salta 6.2.1.2 e il testo e' riportato come sta.
- Clausola 6.1 (TL publication) -> 1 Obbligo "informativo/trasparenza",
  soggetto QTSP/gestore (il Trusted List Scheme Operator) obbligato, con "Terzi
  affidanti/pubblico" destinatario. La clausola mescola vincoli tecnici sulla
  forma dell'URI HTTP e obblighi di pubblicazione della TL e del suo digest
  SHA-256: si e' scelto "informativo/trasparenza" perche' la finalita' e' la
  messa a disposizione della TL al pubblico e la rilevabilita' degli
  aggiornamenti (digest .sha2, cache-control entro 4 ore), non la sicurezza del
  trattamento. Il digest "shall not be used to authenticate the TL": e'
  dichiaratamente un'informazione di aggiornamento, non un mezzo di
  autenticazione.
- Clausola 6.2.1.1 (HTTP-Media Type) -> 1 Obbligo "tecnico/sicurezza":
  requisito di conformazione tecnica del trasporto (media type
  application/vnd.etsi.tsl+xml; header HTTP Accept opzionale).
- Clausola 6.2.2 (MIME registrations) -> 1 Obbligo "tecnico/sicurezza": e' il
  lato documentale dello stesso vincolo di formato del payload. La tabella del
  PDF allinea le celle su colonne, quindi le coppie sono ricostruite in forma
  esplicita "ETICHETTA: valore." senza perdere alcun valore (stesso criterio
  gia' applicato alle tabelle di ETSI EN 319 421/319 422). Le "Security
  considerations" riportano che le TL non contengono codice attivo, sono
  firmate, non richiedono integrita' aggiuntiva ne' riservatezza: sono
  contenuto autentico e restano verbatim.
- Clausola 6.3 (TL Distribution Points in trust service tokens) -> 1 Obbligo
  "tecnico/sicurezza". Il soggetto vincolato in senso proprio e' il TSP ("The
  TSP shall guarantee that the distribution point in each trust service token
  is always resolved to the latest available applicable TL"), mentre i primi
  periodi sono facolta' ("may wish", "may include"), un "should not be marked
  critical" e un "should remain accessible": per il precedente consolidato di
  questa fonte (unico tipo prescrittivo disponibile, lo schema non distingue
  shall da should) restano nello stesso nodo Obbligo.
  `condizione_applicabilita` valorizzata: si applica ai TSP che includono nei
  propri trust service token un'estensione con il distribution point della TL
  dello schema.
- Clausola 6.4 (TL availability) -> 1 Obbligo "tecnico/sicurezza" (24 ore al
  giorno, 7 giorni su 7, disponibilita' minima 99,9 % su un anno), soggetto
  QTSP/gestore obbligato e "Terzi affidanti/pubblico" destinatario: e' un
  requisito di disponibilita' del servizio, non un processo organizzativo ne'
  un adempimento informativo.
- Clausola 6.5 (TLSO practices) -> 1 Obbligo "organizzativo": definire,
  mantenere e attuare misure, pratiche e policy - incluse procedure di change
  management e di sicurezza - per stabilire, pubblicare e mantenere la TL, con
  informazioni tempestive, accurate, complete e autentiche.
- Annex A (informative) -> 2 Principi "altro" (A.1, A.2). L'annesso e' marcato
  "(informative)"; A.2 usa pero' un linguaggio quasi prescrittivo ("TL scheme
  operators need to make sure that at all times two or more scheme operator
  public key certificates, with shifted validity periods, corresponding to the
  private keys entitled to be used to digitally sign the TL are available",
  "need to re-issue, without any delay", "need to promptly notify"):
  classificarlo Obbligo attribuirebbe
  valore cogente a un testo che il documento dichiara informativo, quindi la
  scelta e' Principio "altro" per entrambe le clausole, con il testo integrale
  (comprese le 4 NOTE di A.1 e le liste di A.2) e `oggetti_giuridici`
  ["altro"]: nessuno degli oggetti enumerati calza davvero, perche' l'oggetto
  e' il modello di fiducia e autenticazione della TL, non un servizio
  fiduciario specifico. Se in futuro servisse un nodo prescrittivo per la
  continuita' delle chiavi di firma dello scheme operator, A.2 e' la clausola
  da riclassificare.
- Annex B (normative) -> 4 Obblighi "tecnico/sicurezza" (B.0, B.1.0, B.1.1,
  B.1.2). B.0 vincola sia chi produce la TL (conformita' agli XML schema, uso
  di UTF-8, contenuto degli URI di ElectronicAddressType) sia chi la processa
  ("Applications shall reject the TL if they encounter a critical extension
  that they do not recognize"): per questo i soggetti sono QTSP/gestore (TLSO)
  e "Terza parte" (l'applicazione che consuma la TL), entrambi in ruolo
  obbligato. B.1.1 fissa l'uso di xades:SigningCertificateV2 per proteggere
  l'identificatore dello scheme operator; B.1.2 elenca gli algoritmi e i
  formati ammessi (XML-Signature, ECDSA, SHA-2).
- Annex B.1 (The Signature element) -> NESSUN nodo: intestazione di puro
  raggruppamento, seguita immediatamente da B.1.0.

NOTE ed EXAMPLE: la NOTE di B.0 (perche' il namespace conserva "02231" di ETSI
TS 102 231), le NOTE 1-2 di B.1.0 (modello di processing della firma enveloped,
ammissibilita' di proprieta' firmate XAdES) e le NOTE 1-4 di A.1 (ruolo della
LOTL, certificati dello scheme operator inclusi nelle TL nazionali, procedura
di autenticazione in 6 passi) hanno contenuto interpretativo sostanziale e sono
riportate per intero in `testo_integrale`. In 6.1 il blocco introdotto da "For
example" (strategia di download basata su TL.sha2 e su nextUpdate) non usa la
keyword EXAMPLE ma e' un esempio operativo ufficiale: riportato integralmente,
con la struttura dei due elenchi annidati. Nessun testo del documento e' stato
scartato; nessun marcatore di elisione e' stato introdotto (in questo capitolo
il documento non contiene ellissi autentiche: il caso noto di questa fonte e'
confinato all'annex D).

Conteggi: 10 Obblighi, 2 Principi, 12 item di indice (esattamente uno per
nodo), 5 relazioni interne.

RELAZIONI (5, tutte interne a ETSI TS 119 612, tutte "richiama", tutte da
riscontro testuale esplicito e puntuale; `evidence_type` "textual",
`confidence` None perche' nessuna estrazione LLM ha prodotto uno score):
- 6.1 -> "clausola 5.3.15 (Next update)": "not wait until the time contained in
  the Next update field (clause 5.3.15)" (stringa e tipo Obbligo confermati da
  Etsi612Cap02).
- Annex A.1 -> "clausola 5.3.3 (TSL type)": "designed on the model of
  "EUlistofthelists" type as specified in clause 5.3.3" (confermata da
  Etsi612Cap02).
- Annex A.1 -> "Annex D.5 (EU specific trusted lists URIs)": "The
  "EUlistofthelists" type of such a LOTL is defined in clause D.5" (stringa e
  tipo Principio confermati da Etsi612Cap06).
- Annex B.0 -> "Annex C (XML schema)": "the XML schemas attached to the present
  document as part of a ZIP file identified in annex C" (stringa e tipo
  Principio confermati da Etsi612Cap06).
- Annex B.1.0 -> "clausola 5.7.1 (Digitally signed Trusted List)": il testo
  cita "Clause 5.7 requires that the TL is digitally signed"; 5.7 e'
  intestazione di puro raggruppamento (nessun nodo) e il requisito di firma
  vive nella sottoclausola 5.7.1 (stringa e tipo Obbligo confermati da
  Etsi612Cap04): la relazione punta al nodo risolvibile, non alla sigla vuota.
Nessuna relazione cross-fonte: il collegamento con le altre Fonti e' la Fase 6
della sessione principale (ADR-0009). Citazioni esterne notate e volutamente
NON trasformate in relazioni, perche' documenti non censiti nel grafo o non
ancora collegabili: IETF RFC 2616 [7] (HTTP), IETF RFC 5322 [9] e IETF RFC 2368
[6] (indirizzo e-mail e schema URI "mailto:" nel tipo ElectronicAddressType),
IETF RFC 5280 [12] (campo critical delle estensioni dei certificati X.509 v3),
XML-Signature [4] (compreso il processing model della sua clausola 4.3.3.3),
XAdES [3] (xades:SigningCertificateV2), ECDSA [1], SHA-2 [10], ETSI TS 102 231
[i.6] (origine del namespace "02231"), oltre ai riferimenti al LOTL e all'OJEU
e all'URL https://eidas.ec.europa.eu/efda/tl-browser/#/screen/home.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 6.1 (TL publication)",
        "testo": (
                "I TLSO devono rendere le TL disponibili via HTTP (IETF RFC 2616 [7]); possono in aggiunta supportare"
                " la pubblicazione via LDAP o FTP. L'URI HTTP della TL deve essere privo di caratteri speciali,"
                " contenere un nome di dominio pienamente qualificato nella sezione host e un percorso assoluto senza"
                " sezione di query; deve essere il piu' stabile e permanente possibile, non implicare redirezioni,"
                " non richiedere l'accettazione di cookie o un'azione esplicita per il download, e condurre"
                " direttamente al file .xml/.xtsl scaricabile da un'applicazione; il percorso assoluto deve terminare"
                " con \".xml\" o \".xtsl\" e il file non deve contenere header o trailer estranei. Il cache-control"
                " va impostato su un periodo ragionevole, limitato a un massimo non superiore a 4 ore. I TLSO devono"
                " pubblicare, nelle stesse locazioni della TL, un digest SHA-256 della rappresentazione binaria della"
                " TL, a un URI HTTP derivato sostituendo la stringa \".xml\"/\".xtsl\" finale con \".sha2\": il"
                " digest serve a rilevare la pubblicazione di una TL aggiornata e non deve essere usato per"
                " autenticare la TL. Le applicazioni dovrebbero controllare regolarmente la pubblicazione di nuove"
                " versioni senza attendere la scadenza del campo Next update (clausola 5.3.15); l'esempio ufficiale"
                " descrive la strategia di download basata su TL.sha2 e sul campo nextUpdate."
            ),
        "testo_integrale": (
                "6.1 TL publication: TL Scheme Operators shall make TLs available through the Hypertext Transfer"
                " Protocol (HTTP) defined in IETF RFC 2616 [7]. TLSOs may in addition support publication through"
                " LDAP, or FTP.\nThe HTTP URI pointing to the TL shall be without any special character, shall"
                " contain a fully qualified domain name in the host section, and an absolute path, without a query"
                " section. It shall be an as stable and permanent URI as possible, without implying any redirection,"
                " without requiring acceptance of cookies or explicit action for downloading, and it shall lead"
                " directly to the .xml/.xtsl file that shall be downloadable by an application. The absolute path"
                " shall end with the string \".xml\" or \".xtsl\". There shall not be any extraneous header or"
                " trailer information in the file.\nWhen publishing their TLs, TLSOs should make sure that the cache"
                " control is set to a reasonable period, i.e. avoiding that an old version of the TL is allowed to"
                " linger in network caches long after it was replaced by a new one by the TLSO. The use of this"
                " cache-control should be limited to a maximum value not exceeding 4 hours.\nTLSOs shall publish, at"
                " the same locations where they publish their trusted list, a digest that shall be computed as the"
                " SHA-256 hash value [10] of the binary representation of the trusted list as it can be retrieved by"
                " the server resolving the HTTP URI. The digest shall be published at an HTTP URI derived from the TL"
                " URI replacing the \".xml\" or \".xtsl\" string at the end of the absolute path with \".sha2\".\n"
                "This digest may be used to detect if an updated TL was published and shall not be used to"
                " authenticate the TL. Applications should regularly check for publication of a new version of a TL"
                " and not wait until the time contained in the Next update field (clause 5.3.15) of the previous TL"
                " or the previously downloaded TL is elapsed.\nFor example, the TLSOx's TL published at the location"
                " http://www.TLSOx.xyz/TrustedList/TL.xml is accompanied by its sha2 digest file i.e. on location"
                " http://www.TLSOx.xyz/TrustedList/TL.sha2. Downloaders may adopt the following strategy for"
                " downloading file TL.xml:\n• check whether TL.sha2 is available for download:\n- if TL.sha2 has been"
                " successfully downloaded, verify the digest against the cached TL.xml file. If different, download"
                " and process TL.xml;\n- if TL.sha2 has not been successfully downloaded, download and process TL.xml"
                " directly.\n• TL.xml should be downloaded/processed anyway if the nextUpdate (in the cached file)"
                " has been reached."
            ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}, {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"}],
    },
    {
        "riferimento": "clausola 6.2.1.1 (HTTP-Media Type)",
        "testo": (
                "Requisito di trasporto: la clausola specifica il mezzo di trasporto delle TL via Internet usando"
                " HTTP. I payload delle TL devono essere inviati con il media type application/vnd.etsi.tsl+xml; il"
                " client puo', inviando richieste, fornire un header HTTP Accept, che dovrebbe indicare la capacita'"
                " di accettare application/vnd.etsi.tsl+xml."
            ),
        "testo_integrale": (
                "6.2.1.1 HTTP-Media Type: This clause specifies a means for transport of TLs via the Internet using"
                " HTTP.\nTL payloads shall be sent using the following media type:\n• application/vnd.etsi.tsl+xml\n"
                "The client may, when sending requests, provide an HTTP Accept header field. This header field should"
                " indicate an ability to accept \"application/vnd.etsi.tsl+xml\"."
            ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.2.2 (MIME registrations)",
        "testo": (
                "Registrazione MIME a supporto del trasferimento delle TL: nome del media type Application, sottotipo"
                " vnd.etsi.tsl+xml, nessun parametro richiesto, considerazioni di encoding binarie, estensione di"
                " file xml o xtsl. Considerazioni di sicurezza: le TL non contengono codice attivo ne' invocano"
                " elaborazione automatica; si prevede che i client si limitino a fare il parsing della TL e che non"
                " vi sia rischio di sicurezza; le TL sono firmate e non richiedono protezione di integrita'"
                " aggiuntiva; le TL sono tipicamente pubbliche e non richiedono riservatezza. Specifica pubblicata:"
                " il formato TL definito nel presente documento."
            ),
        "testo_integrale": (
                "6.2.2 MIME registrations: A MIME-Type and a file-extensions support the transfer of TLs:\nMIME media"
                " type name: Application\nMIME subtype name: vnd.etsi.tsl+xml\nRequired parameters: none\nencoding"
                " considerations: binary\nFile extension: xml or xtsl\nSecurity considerations: TLs do not contain"
                " any active code or invoke any automated processing by itself. It is expected that clients only"
                " parse the TL and that there is no security risk. TLs are signed; no additional integrity protection"
                " is required. TLs typically are meant to be public, no confidentiality is required.\nPublished"
                " specification: The TL format as defined in the present document."
            ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3 (TL Distribution Points in trust service tokens)",
        "testo": (
                "I Trust Service Provider che vogliono indicare come localizzare la TL dello schema sotto cui operano"
                " possono includere un'estensione appropriata nei propri trust service token (certificati, CRL, token"
                " di marca temporale, risposte OCSP e altri). Se il meccanismo di estensione consente di esprimere la"
                " criticality, l'estensione non dovrebbe essere marcata critica; un distribution point dovrebbe"
                " restare accessibile finche' tutti i trust service token che lo referenziano non sono scaduti. Il"
                " TSP deve garantire che il distribution point in ogni trust service token si risolva sempre alla TL"
                " applicabile piu' recente o a uno schema che la punti (es. LOTL)."
            ),
        "testo_integrale": (
                "6.3 TL Distribution Points in trust service tokens: Trust Service Providers may wish to give"
                " information on how to locate a TL of the scheme they operate under. To do so, they may include an"
                " appropriate extension in their trust service tokens (e.g. certificates, CRLs, time-stamp tokens,"
                " OCSP responses and other). If such extension mechanism allows for the expression of criticality,"
                " this extension should not be marked critical. A distribution point should remain accessible until"
                " all trust service tokens it is referenced in have expired. The TSP shall guarantee that the"
                " distribution point in each trust service token is always resolved to the latest available"
                " applicable TL or to a scheme including a pointer to it (e.g. LOTL)."
            ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
                "Si applica ai TSP che scelgono di includere nei propri trust service token un'estensione recante il"
                " distribution point della TL dello schema."
            ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.4 (TL availability)",
        "testo": (
                "I TLSO devono rendere le proprie TL disponibili 24 ore al giorno e 7 giorni su 7, con una"
                " percentuale di disponibilita' minima del 99,9 % su un anno."
            ),
        "testo_integrale": (
                "6.4 TL availability: TLSOs shall make their TLs available 24 hours a day and 7 days a week, with an"
                " availability percentage of minimum 99,9 % over one year."
            ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}, {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"}],
    },
    {
        "riferimento": "clausola 6.5 (TLSO practices)",
        "testo": (
                "Il TLSO deve definire, mantenere e attuare misure, pratiche e policy appropriate - incluse procedure"
                " di gestione del cambiamento e di sicurezza - per stabilire, pubblicare e mantenere l'elenco"
                " fiduciario, assicurando che le informazioni in esso fornite siano tempestive, accurate, complete e"
                " autentiche."
            ),
        "testo_integrale": (
                "6.5 TLSO practices: The TLSO shall define, maintain and implement appropriate measures, practices"
                " and policies, including change management and security procedures, for establishing, publishing and"
                " maintaining the trusted list to ensure that the information provided in the trusted list is timely,"
                " accurate, complete and authentic."
            ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex B.0 (General requirements)",
        "testo": (
                "Una TL deve essere conforme agli XML schema allegati al documento come parte di un file ZIP"
                " identificato nell'annex C, ciascuno dei quali definisce elementi e tipi in un namespace diverso"
                " (http://uri.etsi.org/02231/v2#,"
                " http://uri.etsi.org/TrstSvc/SvcInfoExt/eSigDir-1999-93-EC-TrustedList/#,"
                " http://uri.etsi.org/02231/v2/additionaltypes#). Le applicazioni devono usare la codifica UTF-8 per"
                " le TL XML. Nel tipo ElectronicAddressType il contenuto di ogni elemento URI deve rappresentare un"
                " indirizzo e-mail IETF RFC 5322 espresso con lo schema URI \"mailto:\" definito da IETF RFC 2368,"
                " oppure un indirizzo di sito web. Il trattamento dell'attributo Critical e' quello definito da IETF"
                " RFC 5280 per il campo critical delle estensioni dei certificati X.509 v3: le applicazioni devono"
                " rifiutare la TL se incontrano un'estensione critica che non riconoscono, mentre possono ignorare"
                " un'estensione non critica che non riconoscono."
            ),
        "testo_integrale": (
                "Annex B.0 General requirements: Annex B (normative): Implementation in XML.\nA TL shall comply with"
                " the XML schemas attached to the present document as part of a ZIP file identified in annex C, each"
                " one defining elements and types in a different namespace, respectively:\n•"
                " http://uri.etsi.org/02231/v2#\n•"
                " http://uri.etsi.org/TrstSvc/SvcInfoExt/eSigDir-1999-93-EC-TrustedList/#\n•"
                " http://uri.etsi.org/02231/v2/additionaltypes#\nNOTE: \"02231\" in the name space does not"
                " correspond to the ETSI document number of the present document because the name space was initially"
                " defined in ETSI TS 102 231 [i.6]. The previously defined name space is kept for compatibility"
                " reasons.\nApplications shall use UTF-8 encoding for XML TLs.\nWith regards to the"
                " ElectronicAddressType type, the contents of each URI element shall represent a IETF RFC 5322 [9]"
                " e-mail address, expressed by using the \"mailto:\" URI scheme as defined by IETF RFC 2368 [6], or a"
                " web site address.\nProcessing of Critical attribute shall be as the one defined by IETF RFC 5280"
                " [12] for the critical field of extensions of X.509 v3 certificates. Applications shall reject the"
                " TL if they encounter a critical extension that they do not recognize. However, they may ignore a"
                " non-critical extension that they do not recognize."
            ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}, {"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex B.1.0 (General)",
        "testo": (
                "La clausola 5.7 richiede che la TL sia firmata digitalmente, incluso l'uso di firme XAdES; la"
                " struttura della TL contiene un elemento ds:Signature che rappresenta una firma digitale di tipo"
                " enveloped. Il documento impone i seguenti vincoli a ogni firma digitale basata su XML-Signature"
                " applicata a una TL: 1) deve essere una firma enveloped; 2) il suo elemento ds:SignedInfo deve"
                " contenere un elemento ds:Reference con attributo URI che referenzia l'elemento"
                " TrustServiceStatusList che incapsula la firma stessa e tale ds:Reference deve contenere un solo"
                " ds:Transforms, con due ds:Transform (enveloped transformation"
                " http://www.w3.org/2000/09/xmldsig#enveloped-signature e canonicalizzazione esclusiva"
                " http://www.w3.org/2001/10/xml-exc-c14n#); 3) ds:CanonicalizationMethod deve essere"
                " http://www.w3.org/2001/10/xml-exc-c14n#; 4) sono ammessi altri elementi ds:Reference. Le NOTE"
                " ufficiali chiariscono il modello di processing della firma e l'ammissibilita' di proprieta' firmate"
                " (es. XAdES)."
            ),
        "testo_integrale": (
                "Annex B.1.0 General: Clause 5.7 requires that the TL is digitally signed: this includes use of XAdES"
                " [3] signatures. The TL-structure contains a ds:Signature element that represents an enveloped"
                " digital signature-type. The present document mandates the following constraints to any"
                " XML-Signature [4]-based digital signature applied to a TL:\n1) It shall be an enveloped digital"
                " signature.\n2) Its ds:SignedInfo element shall contain a ds:Reference element with the URI"
                " attribute set to a value referencing the TrustServiceStatusList element enveloping the digital"
                " signature itself. This ds:Reference element shall satisfy the following requirements:\na) It shall"
                " contain only one ds:Transforms element.\nb) This ds:Transforms element shall contain two"
                " ds:Transform elements. The first one will be one whose Algorithm attribute indicates the enveloped"
                " transformation with the value: \"http://www.w3.org/2000/09/xmldsig#enveloped-signature\". The"
                " second one will be one whose Algorithm attribute instructs to perform the exclusive"
                " canonicalization \"http://www.w3.org/2001/10/xml-exc-c14n#\".\n3) ds:CanonicalizationMethod shall"
                " be \"http://www.w3.org/2001/10/xml-exc-c14n#\".\n4) It may have other ds:Reference elements.\nNOTE"
                " 1: Rules 2 and 3 ensure that the enveloping TrustServiceStatusList element is actually digitally"
                " signed as mandated by the processing model in clause 4.3.3.3 of XML-Signature [4] (with reference"
                " to same-document URI references). They also ensure that if relative referencing mechanisms are used"
                " in the ds:Reference element, the TrustServiceStatusList may be safely inserted within other xml"
                " documents.\nNOTE 2: Rule 4 allows, among other things, for inclusion of signed properties in the"
                " digital signature, like the ones standardized in XAdES [3]."
            ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex B.1.1 (The scheme operator identifier in XAdES signatures)",
        "testo": (
                "XAdES definisce xades:SigningCertificateV2 come proprieta' firmata che contiene un identificatore"
                " del certificato del firmatario e il suo digest: deve essere usata come modo efficace di proteggere"
                " l'identificatore dello scheme operator. Se il figlio dell'elemento ds:X509Data e' un ds:X509SKI o"
                " un elemento che incapsula una chiave pubblica, il suo contenuto deve essere coerente con il"
                " contenuto della proprieta' firmata xades:SigningCertificateV2, se presente."
            ),
        "testo_integrale": (
                "Annex B.1.1 The scheme operator identifier in XAdES signatures: XAdES [3] defines the"
                " xades:SigningCertificateV2 as a signed property that contains an identifier of the signer's"
                " certificate and its digest. This shall be used as an effective way of securing the scheme operator"
                " identifier.\nShould the child of ds:X509Data element be a ds:X509SKI or an element encapsulating a"
                " public key, its contents shall be consistent with the contents of the xades:SigningCertificateV2"
                " signed property, if present."
            ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex B.1.2 (Algorithm and parameters)",
        "testo": (
                "Gli algoritmi, i loro parametri e i formati supportati dal presente documento devono essere: quelli"
                " supportati da XML-Signature; oppure l'algoritmo di firma digitale su curve ellittiche (ECDSA) come"
                " definito in [1]; oppure gli algoritmi SHA-2 come definiti in [10]."
            ),
        "testo_integrale": (
                "Annex B.1.2 Algorithm and parameters: The algorithms, their parameters and formats supported by the"
                " present document shall be:\n• those supported by XML-Signature [4]; or\n• the Elliptic Curve"
                " Digital Signature Algorithm (ECDSA) as defined in [1]; or\n• the SHA-2 algorithms as defined in"
                " [10]."
            ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "Annex A.1 (Authenticating and trusting a TL)",
        "testo": (
                "Annesso informativo sull'autenticazione e l'affidamento della TL: una TL e' un dato firmato"
                " digitalmente e, per verificarne la firma, le relying party devono poter accedere alla chiave"
                " pubblica applicabile; poiche' lo schema che emette le TL e' di fatto posizionato \"sopra\" i TSP"
                " approvati, l'autenticita' della chiave pubblica non puo' essere verificata sulla sola base della"
                " sua certificazione da parte di un TSP interno o esterno allo schema. Quando piu' TL partecipano"
                " allo stesso schema di approvazione o occorre raggrupparne e facilitarne l'accesso, puo' essere"
                " istituito e pubblicato un elenco compilato di puntatori a tali TL, sul modello del tipo"
                " \"EUlistofthelists\" come specificato nella clausola 5.3.3; la List Of Trusted Lists (LOTL) della"
                " Commissione europea, il cui tipo e' definito nella clausola D.5, ne e' l'istanza concreta. Le"
                " quattro NOTE ufficiali illustrano il ruolo della LOTL (pubblicata anche in formato XML elaborabile"
                " a macchina, con firma o sigillo qualificato) e la procedura in 6 passi con cui una relying party"
                " autentica e si affida a una TL di uno Stato membro: download della LOTL dalla locazione protetta"
                " pubblicata in OJEU, validazione della firma/sigillo della LOTL, verifica della perdurante validita'"
                " della LOTL, parsing della LOTL per la locazione e le informazioni di autenticazione della TL di"
                " destinazione, download di tale TL, validazione della sua firma/sigillo; se uno dei controlli"
                " fallisce, l'autenticazione della TL fallisce. La procedura puo' essere eseguita da ogni utente o a"
                " livello di organizzazione secondo la propria policy, con ambienti preconfigurati e aggiornati"
                " dall'amministrazione di sistema o dal security officer e, in prospettiva, con certificati o chiavi"
                " pubbliche preinstallate nei browser."
            ),
        "testo_integrale": (
                "Annex A.1 Authenticating and trusting a TL: Annex A (informative): Authenticating and trusting"
                " trusted lists.\nA TL is a digitally signed data. To verify the digital signature, relying parties"
                " need to be able to access the applicable public key. Since the scheme issuing the TLs is"
                " effectively positioned \"above\" the TSPs approved by that scheme, the authenticity of the public"
                " key cannot be verified solely on the basis of its certification by any TSP inside or outside the"
                " scheme. Providing the scheme's public key is therefore a problem very similar to providing the"
                " public key of a CA service.\nIn the case where several TLs participate to the same global approval"
                " scheme or participate to a common approval scheme or when there is a need to group and facilitate"
                " access to such TLs, a compiled list of pointers towards such TLs may be established, published and"
                " maintained. This compiled list of pointers can be designed on the model of \"EUlistofthelists\""
                " type as specified in clause 5.3.3.\nNOTE 1: To allow access to the trusted lists of all Member"
                " States in an easy manner, the European Commission publishes a central list with links to the"
                " locations where the trusted lists are published as notified by Member States. This central list,"
                " called the List Of Trusted Lists (LOTL), is available in both a human readable format and in a"
                " format suitable for automated (machine) processing XML. The \"EUlistofthelists\" type of such a"
                " LOTL is defined in clause D.5.\nSuch a compiled list of pointers towards logically grouped TLs can"
                " also play an important role in authenticating and trusting each TL which is pointed to by the"
                " compiled list. As a TL is digitally signed by its TLSO, the certificate to be used to verify such a"
                " digital signature can be included in the compiled list together with the corresponding pointer to"
                " this TL. The compiled list of pointers can be digitally signed and the certificate to be used to"
                " verify the digital signature on the compiled list can be published in an official journal or in"
                " another trustworthy publication.\nNOTE 2: The European Commission LOTL plays an important role in"
                " authenticating and trusting EU MS trusted lists. Each national trusted list is electronically"
                " signed/sealed by its scheme operator and the certificate to be used to verify such an electronic"
                " signature/seal is included in the LOTL after notification to the European Commission. The public"
                " key certificate(s) corresponding to the private key(s) entitled to be used to electronically"
                " sign/seal MS trusted lists and hence to be used by relying parties to validate those TLs"
                " signatures/seals are published in the LOTL. The authenticity and integrity of the machine"
                " processable version of the LOTL is ensured through a qualified electronic signature or seal"
                " supported by a qualified certificate which can be authenticated and directly trusted through one of"
                " the digests published in the Official Journal of the European Union (OJEU).\nSee"
                " https://eidas.ec.europa.eu/efda/tl-browser/#/screen/home.\nNOTE 3: Additionally the certificate(s)"
                " of the LOTL scheme operator is(are) included in any EU MS trusted list.\nNOTE 4: In order to"
                " authenticate and trust an EU Member State trusted list, relying parties can:\n1) download the LOTL"
                " from the protected location published in the OJEU, after having authenticated the trusted channel"
                " on the basis of the trusted channel certificate whose digest is published in the OJEU;\n2) validate"
                " the electronic signature/seal on the downloaded LOTL, once having verified that the digest of the"
                " LOTL scheme operator public key certificate to be used to validate the signature/seal maps one of"
                " the digests of the public key certificate(s) corresponding to the private key(s) entitled to be"
                " used to sign/seal the LOTL as published in OJEU;\n3) verify, once the LOTL signature/seal being"
                " validated, the continued validity of the LOTL, by ensuring that the validity period of the LOTL has"
                " not expired;\n4) parse the LOTL to retrieve the location and authentication information with"
                " regards to the target MS trusted list (one or more public key certificates may be associated to a"
                " MS TL as the public key certificate(s) corresponding to the private key(s) entitled to be used to"
                " sign the TL);\n5) download the target MS TL;\n6) validate the signature/seal on the target MS TL,"
                " once having verified that the digest of the TL scheme operator public key certificate to be used to"
                " validate the signature/seal maps one of the digests of the public key certificate(s) corresponding"
                " to the private key(s) entitled to be used to sign/seal the target TL as published in the LOTL.\nIf"
                " either of the above checks fails, the TL authentication fails.\nThe procedure described above can"
                " be performed by each user, but will in many cases be carried out on the level of an organization"
                " according to their own policy. In this case, the software environment of each user's machine would"
                " typically be pre-configured and updated by the system administration or by the security officer. In"
                " time it is likely and certainly possible that such TLSOs or LOTL scheme operators certificates or"
                " public keys could also be pre-installed and updated in browsers, so enabling personal users to gain"
                " advantage from this approach."
            ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["altro"],
    },
    {
        "riferimento": "Annex A.2 (Ensuring continuity in TL authentication)",
        "testo": (
                "Annesso informativo sulla continuita' dell'autenticazione della TL: il TL scheme operator deve"
                " assicurarsi che in ogni momento siano disponibili in modo affidabile per le relying party due o"
                " piu' certificati di chiave pubblica dello scheme operator, con periodi di validita' sfalsati,"
                " corrispondenti alle chiavi private abilitate a firmare digitalmente la TL (es. pubblicati nella"
                " LOTL, nel contesto delle TL degli Stati membri UE, o in una Gazzetta ufficiale). Tali certificati"
                " possono essere emessi in modo che non abbiano date di inizio e fine uguali o troppo vicine, siano"
                " creati su nuove coppie di chiavi (nessuna coppia gia' usata va ricertificata), siano allocati a due"
                " o piu' trustee dello scheme operator secondo la policy applicabile e siano notificati in tempo"
                " utile alle relying party. L'annesso descrive inoltre, per la compromissione o dismissione di una"
                " chiave privata di firma della TL o dell'elenco compilato e per la compromissione di tutte le"
                " chiavi, le condotte richieste: riemissione immediata di una nuova TL/elenco firmato con chiave non"
                " compromessa, notifica tempestiva alle relying party delle circostanze e del nuovo elenco di"
                " certificati, pubblicazione del nuovo elenco con deprecazione dei certificati compromessi o"
                " dismessi. Chiude chiarendo che, nel modello di fiducia diretta sottostante il riconoscimento di"
                " affidabilita', la revoca dei certificati dello scheme operator della TL e dell'elenco compilato e'"
                " di fatto attuata dalla deprecazione dei certificati compromessi o dismessi nella pubblicazione"
                " ufficiale."
            ),
        "testo_integrale": (
                "Annex A.2 Ensuring continuity in TL authentication: In order to ensure continuity in TL"
                " authentication, TL scheme operators need to make sure that at all times two or more scheme operator"
                " public key certificates, with shifted validity periods, corresponding to the private keys entitled"
                " to be used to digitally sign the TL are available in a trustworthy manner to relying parties (e.g."
                " published in the LOTL in the context of EUMS TLs, or in an Official Journal). Those certificates"
                " can be issued so that they:\n• do not have the same or too close validity start and end dates;\n•"
                " are created on new key pairs as no previously used key pair are to be re-certified;\n• are"
                " allocated to two or more scheme operator trustees in accordance with the scheme operator applicable"
                " policy; and\n• are notified in due time to relying parties (e.g. to the EC for inclusion in the"
                " LOTL in the context of EUMS TLs).\nIn the case of compromise or decommissioning of one trusted list"
                " digital signature private key, TL scheme operators:\n• when the current (into force) TL was signed"
                " with such a compromised or decommissioned private key, need to re-issue, without any delay, a new"
                " trusted list signed with a non-compromised private key entitled to be used to digitally sign the TL"
                " and whose corresponding public key certificate was already made available in a trustworthy manner"
                " to relying parties (e.g. is published in the LOTL);\n• need to promptly notify to the relying"
                " parties in a trustworthy manner:\n- of such a key compromise or decommissioning and the associated"
                " circumstances or reasons; and\n- a new list of public key certificate(s) corresponding to the"
                " private key(s) entitled to be used to digitally sign the TL.\nIn the case of compromise (or"
                " decommissioning) of all the digital signature private keys corresponding to the public key"
                " certificates that were entitled to be used to validate one TL and were available to relying parties"
                " (e.g. published in the LOTL), scheme operators:\n• need to generate new key pairs and public key"
                " certificates corresponding to the private keys to be entitled to be used to digitally sign the TL;"
                "\n• need to re-issue, without any delay, a new trusted list signed with one of those new private"
                " keys entitled to be used to digitally sign the TL and whose corresponding public key certificate is"
                " to be made available in a trustworthy manner to relying parties;\n• need to promptly notify to the"
                " relying parties in a trustworthy manner:\n- of a such a key compromise; and\n- the new list of"
                " public key certificates corresponding to the private keys entitled to be used to digitally sign the"
                " TL.\nIn the case of compromise or decommissioning of one digital signature private key related to a"
                " compiled list of pointers to several TLs, the compiled list scheme operator:\n• when the current"
                " (into force) compiled list was digitally signed with such a compromised or decommissioned private"
                " key, needs to re-issue, without any delay, a new compiled list digitally signed with a"
                " non-compromised private key entitled to be used to digitally sign the compiled list and whose"
                " corresponding public key certificate is published e.g. in an official journal;\n• needs to promptly"
                " publish, e.g. in an official journal, a new list of public key certificate(s) corresponding to the"
                " private key(s) entitled to be used to digitally sign the compiled list;\n• needs to inform relying"
                " parties and stakeholders of such an official publication update together with the associated"
                " circumstances or reasons for such an update.\nIn the case of compromise (or decommissioning) of all"
                " compiled list digital signature private keys corresponding to the public key certificates entitled"
                " to be used to digitally sign the compiled list and published, e.g. in an official journal, the"
                " compiled list scheme operator:\n• needs to generate new key pairs and public key certificates"
                " corresponding to the private keys to be entitled to be used to digitally sign the compiled list;\n•"
                " needs to re-issue, without any delay, a new compiled list digitally signed with one of those new"
                " private keys entitled to be used to digitally sign the compiled list and whose corresponding public"
                " key certificate is to be published, e.g. in an official journal;\n• needs to promptly publish, e.g."
                " in an official journal, the new list of public key certificates corresponding to the private keys"
                " entitled to be used to digitally sign the compiled list, deprecating compromised or decommissioned"
                " certificates;\n• needs to inform the relying parties and stakeholders of such an official"
                " publication update together with the associated circumstances or reasons for such an update.\nIn"
                " the context of the direct trust model underlying their trustworthiness recognition, the revocation"
                " of TLSO and compiled list scheme operator certificate(s) are de facto implemented by the fact that"
                " the issuance of a new update of the related TL or compiled list deprecates the updated one and the"
                " deprecation of the compromised or decommissioned certificate(s) respectively in the compiled list"
                " and/or in the related official publication."
            ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["altro"],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 6.1 (TL publication)",
    "clausola 6.2.1.1 (HTTP-Media Type)",
    "clausola 6.2.2 (MIME registrations)",
    "clausola 6.3 (TL Distribution Points in trust service tokens)",
    "clausola 6.4 (TL availability)",
    "clausola 6.5 (TLSO practices)",
    "Annex B.0 (General requirements)",
    "Annex B.1.0 (General)",
    "Annex B.1.1 (The scheme operator identifier in XAdES signatures)",
    "Annex B.1.2 (Algorithm and parameters)",
    "Annex A.1 (Authenticating and trusting a TL)",
    "Annex A.2 (Ensuring continuity in TL authentication)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "clausola 6.1 (TL publication)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.15 (Next update)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Annex A.1 (Authenticating and trusting a TL)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.3 (TSL type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Annex A.1 (Authenticating and trusting a TL)"),
        "nodo_a": ("principio", None, "Annex D.5 (EU specific trusted lists URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex B.0 (General requirements)"),
        "nodo_a": ("principio", None, "Annex C (XML schema)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex B.1.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.7.1 (Digitally signed Trusted List)"),
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
