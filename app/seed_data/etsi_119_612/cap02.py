"""ETSI TS 119 612 V2.4.1 (2025-08) - Electronic Signatures and Trust
Infrastructures (ESI); Trusted Lists.
Fonte 21 (fonte_id assegnato dalla sessione principale; gli id delle righe
sono risolti per riferimento dal registro di app/seed_data/lib.py - questo
modulo NON tocca app/seed.py). Capitolo 2: introduzione della clausola 5
(Trusted list format and content), 5.1 General principles for trusted lists
(5.1.1-5.1.5), 5.2 Trusted List tag (5.2.1), 5.3 Scheme information
(5.3.1-5.3.18, incluse 5.3.5.0/5.3.5.1/5.3.5.2). Testo ufficiale in
app/.source_cache/etsi_119_612/cap02.txt (letto sempre con selettore `:raw`,
altrimenti il tool tronca le righe lunghe a 768 caratteri introducendo "..."
e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_119_612/manifest.json.

Modellazione (ADR-0007), stesso criterio gia' applicato alle altre fonti ETSI
gia' censite e adattato alle sottoclausole di uno standard tecnico: un nodo
per ogni sottoclausola numerata con contenuto proprio. 26 righe, TUTTE
Obblighi (0 Principi): ogni sottoclausola di campo porta almeno un verbo
prescrittivo ("This field shall be present", "shall not be present", "shall be
set to", "shall use"), quindi ricade nel criterio `shall` -> Obbligo del
brief; il capitolo non contiene clausole di puro scopo/ambito ne'
definizioni.

Clausole SENZA nodo (intestazioni di puro raggruppamento, nessun testo
proprio, verificate programmaticamente sul file sorgente): 5 (Trusted list
format and content), 5.1 (General principles for trusted lists), 5.2 (Trusted
List tag), 5.3 (Scheme information), 5.3.5 (Scheme operator address, che apre
direttamente la sottoclausola 5.3.5.0). Nessun item di indice per esse.

Criterio di `tipo_obbligo` (documentato perche' il brief ammette piu'
classificazioni plausibili):
- "tecnico/sicurezza" per i requisiti di formato, sintassi, codifica e per i
  valori meccanici dei campi del TL: 5.1.1 (XML), 5.1.2 (URI/RFC 3986), 5.1.3
  (data-ora ISO 8601/UTC), 5.1.5 (Country Code), 5.2.1 (TSL Tag), 5.3.1
  (version identifier), 5.3.2 (sequence number), 5.3.3 (TSL type), 5.3.8
  (Status determination approach), 5.3.10 (Scheme territory), 5.3.13
  (Pointers/identita' digitali dei TSL puntati), 5.3.14 (List issue date and
  time), 5.3.15 (Next update), 5.3.16 (Distribution points), 5.3.17 (Scheme
  extensions/criticality), 5.3.18 (struttura della Trust Service Provider
  List).
- "informativo/trasparenza" per i campi che pubblicano informazione dello
  scheme/TLSO verso utenti e terzi affidanti: 5.1.4 (lingue supportate),
  5.3.4 (Scheme operator name), 5.3.5.0/5.3.5.1/5.3.5.2 (indirizzi dello
  scheme operator e help line), 5.3.6 (Scheme name), 5.3.7 (Scheme
  information URI), 5.3.9 (Scheme type/community/rules), 5.3.11 (TSL
  policy/legal notice).
- "di conservazione" per 5.3.12 (Historical information period: durata di
  mantenimento delle informazioni storiche, valore 65535 = mai rimosse).
Casi dubbi, risolti e motivati:
- 5.1.4 e' un requisito misto (accessibilita' linguistica dell'informazione
  pubblicata + regole tecniche di codifica UTF-8/tag RFC 5646): classificato
  "informativo/trasparenza" perche' la sua funzione e' rendere la TL
  comprensibile ai terzi affidanti in piu' lingue; le regole di codifica sono
  specifiche di dettaglio richiamate dall'annex E.
- 5.3.15 e' un campo date-time ma il suo contenuto normativo e' la cadenza di
  emissione/pubblicazione degli aggiornamenti (inclusa la regola dei sei mesi
  e la versione finale con servizi "expired"): classificato "tecnico/sicurezza"
  per non spezzare in due nature una singola sottoclausola di campo; la
  valenza procedurale e' descritta in `testo`. Non e' stato usato il tipo
  "procedurale" per non introdurre una classificazione incoerente con le altre
  sottoclausole di campo della clausola 5.3.
- Presenza condizionale/facoltativa registrata in `condizione_applicabilita`:
  5.3.13 (obbligatorio per gli SM UE, opzionale per non UE), 5.3.16
  (opzionale), 5.3.17 (vietato per gli SM UE, opzionale per non UE), 5.3.18
  (assente/presente a seconda che esistano TSP approvati).

NOTE ed EXAMPLE: il capitolo contiene tre NOTE ufficiali (5.3.1 sul version
identifier, 5.3.3 sul significato del tipo per Paesi non UE, 5.3.14 sul
rinvio alla clause 5.5.5); sono tutte riportate integralmente dentro
`testo_integrale` perche' aggiungono contenuto interpretativo/operativo
sostanziale (ADR-0010). Nessun EXAMPLE e nessuna tabella nel capitolo. Le
liste puntate sono riportate nel loro ordine e con i loro marcatori: il
simbolo tipografico di elenco del PDF (carattere private-use U+F0A7) e' reso
come "•" e il trattino di primo livello come "-", senza perdere una sola
parola; i wrap fisici di riga sono stati ricomposti con spazio singolo.

`soggetti`: obbligato sempre "QTSP/gestore" (nello schema della TL il soggetto
che stabilisce, pubblica e mantiene la trusted list e' il Trusted List Scheme
Operator o lo scheme dello Stato membro); "Terzi affidanti/pubblico" in ruolo
"destinatario" e' aggiunto dove la sottoclausola si rivolge esplicitamente a
utenti, terzi affidanti, applicazioni o sistemi che usano la TL (5.1.1, 5.1.2,
5.1.4, 5.3.3, 5.3.5.1, 5.3.5.2, 5.3.7, 5.3.9, 5.3.11, 5.3.13, 5.3.15,
5.3.17). `severita` e `sanzioni` sono omesse (None implicito): uno standard
tecnico ETSI non commina sanzioni.

RELAZIONI (47 in totale): tutte interne alla Fonte 21, tutte di tipo `richiama` (nessuna
`specifica`: il testo usa sempre formule di rinvio - "see clause", "as
specified in clause", "as defined in clause" - mai l'affermazione che una
clausola dettaglia l'altra), evidence_type "textual", confidence None. Sono
tratte solo da riscontri testuali puntuali presenti in `testo_integrale`.
I riferimenti verso altri capitoli usano le stringhe `riferimento` esattamente
concordate via hub con i peer che li producono (il registro risolve per
(tipo, fonte_id, riferimento), quindi una stringa diversa sarebbe un
KeyError): "clausola 4 (Overall structure of trusted lists)" e' un Principio
del cap01; "clausola 5.5.3 (Service digital identity)", "clausola 5.5.5
(Current status starting date and time)", "clausola 5.6.1 (Service type
identifier)" e "clausola 6.2.1.1 (HTTP-Media Type)" sono Obblighi del
cap03/cap04/cap05; "Annex B.0 (General requirements)" e "Annex E.1 (General
rules)" sono Obblighi del cap05/cap07; "Annex C (XML schema)", "Annex D.0
(General)", "Annex D.3 (Scheme registered URIs)", "Annex D.5 (EU specific
trusted lists URIs)", "Annex D.6 (Non-EU specific trusted lists URIs)" e
"Annex I.1 (Introduction)" sono Principi del cap06/cap08 (tranne "Annex D.4
(Common trusted lists URIs)", Obbligo). Le intestazioni di raggruppamento 5.4,
5.5, 5.6, 6.2, annex B, annex D e annex E non generano nodo, quindi i rinvii
generici sono agganciati alla sottoclausola di ingresso pertinente (6.2.1.1 per
i media type, 5.6.1 per la clausola 5.6, Annex B.0 e Annex D.0 per gli annessi
generici), mentre i rinvii di 5.3.18 a "clause 5.4" e "clause 5.5" sono omessi
perche' non esiste un nodo risolvibile che corrisponda all'oggetto citato
(puntare a 5.4.1 "TSP name" o 5.5.1.0 "General requirements" indicherebbe una
sottoparte, non l'elemento TSP Information / Service Information)
(prompt conservativo: nessuna relazione e' meglio di una che non risolve e fa
fallire il seed).
NESSUNA relazione cross-fonte in questa fase (vincolo del brief: il
collegamento con le altre 19 Fonti e' la fase 6/ADR-0009 della sessione
principale).
Citazioni esterne notate e NON trasformate in relazioni (ne' in nodi):
IETF RFC 3986 [8], IETF RFC 5646 [11], IETF RFC 2368 [6], IETF RFC 3966 [17],
ISO 8601 [16], ISO/IEC 10646 [5], ISO 3166-1 [15], Unicode Standard [i.13],
X.509 [1] (semantica della criticality delle estensioni), il regolamento
eIDAS e la LOTL notificata nella Gazzetta Ufficiale dell'Unione europea
(5.3.13).
I rinvii interni alla Fonte 21 sono invece modellati come relazioni `richiama`
verso il nodo risolvibile: annex B.0 e annex C (formato XML), annex
D.0/D.3/D.4/D.5/D.6 (registri degli URI), annex E.1 (requisiti multilingua),
annex I.1 (uso delle trusted list), clausola 4 (struttura complessiva della TL)
e le sottoclausole 5.5.3/5.5.5/5.6.1/6.2.1.1. Restano senza relazione soltanto
i rinvii di 5.3.18 a "clause 5.4" e "clause 5.5": sono intestazioni di
raggruppamento che non generano nodo e la sottoclausola piu' vicina
indicherebbe un oggetto diverso da quello citato.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 5.1.1 (Trusted List Format)",
        "testo": (
            "La trusted list (TL) deve essere emessa in formato XML come specificato negli annex B e C. Se lo "
            "scheme operator o qualunque parte fornisce mezzi per rappresentare una stessa TL in formati diversi, "
            "tali rappresentazioni devono contenere esattamente le stesse informazioni fornite dal formato XML "
            "della TL."
        ),
        "testo_integrale": (
            "A TL shall be issued in XML format as specified in annexes B and C. If the scheme operator or any "
            "party provides means to represent one TL in different formats, they shall contain exactly the same "
            "information as provided in the XML format of the TL."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.1.2 (Use of Uniform Resource Identifiers)",
        "testo": (
            "Nelle definizioni dei campi della TL molti usano Uniform Resource Identifier (URI) per indicare il "
            "significato del campo; i 'common name' impiegati in quelle definizioni rinviano alla loro "
            "dichiarazione nell'annex D, che enuncia formalmente tutti gli URI specifici usati nel documento con "
            "i relativi significati. Alcuni campi ammettono URI diversi con lo stesso scopo, registrati e "
            "descritti dallo scheme operator o da altra entità e riconosciuti dalla comunità di utenti "
            "destinataria; tali URI possono essere registrati presso ETSI (informazioni nella clause D.3). Dove i "
            "campi sono definiti del tipo URI, gli implementatori devono usare la sintassi generale specificata "
            "da IETF RFC 3986."
        ),
        "testo_integrale": (
            "In the definitions of TL fields given in the present document, many use Uniform Resource Identifiers "
            "(URIs) to indicate the meaning of the field concerned. Within these definitions a \"common name\" may "
            "be used to broadly and simply describe the specific values or meanings of the field. These common "
            "names are linked to their declaration in annex D, which formally states all specific URIs used in "
            "the present document, with their meanings. Some fields allow to use different URIs, which have the "
            "same purpose, to be registered and described by the scheme operator or another entity and recognized "
            "by the intended user community. Such URIs may be registered with ETSI. Information on URI "
            "registration can be found in clause D.3. Where fields are defined as being of or using the type URI, "
            "implementers shall use general syntax as specified by IETF RFC 3986 [8]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.1.3 (Date-time indication)",
        "testo": (
            "Tutti i campi che portano valori di data e ora devono rispettare due regole: il valore dev'essere "
            "una stringa di caratteri formattata secondo ISO 8601; e il valore dev'essere espresso in Coordinated "
            "Universal Time (UTC), contenendo anno di quattro cifre, mese, giorno, ora, minuto e secondo (senza "
            "frazione decimale) e il designatore UTC 'Z'. La scala temporale è basata sul secondo."
        ),
        "testo_integrale": (
            "All fields carrying date-time values shall comply with the following rules: 1) the date-time values "
            "shall be a character string formatted according to ISO 8601 [16]; and 2) the date-time value shall "
            "be expressed as Coordinated Universal Time (UTC): its value shall contain year with four digits, "
            "month, day, hour, minute, second (without decimal fraction) and the UTC designator \"Z\". The time "
            "scale shall be based on the second."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.1.4 (Language support)",
        "testo": (
            "Le trusted list devono essere emesse supportando almeno la lingua inglese UK, con il codice lingua "
            "'en' come specificato in IETF RFC 5646 e nell'annex E, e possono essere emesse supportando più "
            "lingue (nazionali). Per tutti i campi in cui è applicabile il supporto multilingua le specifiche di "
            "formato rinviano a stringhe di caratteri multilingua o a puntatori multilingua, cui si applicano "
            "regole generali: una stringa multilingua è una stringa di caratteri ISO/IEC 10646 codificata in "
            "UTF-8, composta da un tag conforme a IETF RFC 5646 in minuscolo che identifica la lingua e dal testo "
            "in quella lingua (contenuti uguali possono essere rappresentati in più lingue da una sequenza di "
            "stringhe); un puntatore multilingua è un URI che identifica una risorsa espressa in una particolare "
            "lingua, composto da un tag di lingua conforme a IETF RFC 5646 e dall'URI con la sintassi di IETF RFC "
            "3986. Quando i termini nativi non sono rappresentabili con l'alfabeto latino come definito in "
            "ISO/IEC 10646 vanno usate due occorrenze: il termine in lingua nativa e una traslitterazione in "
            "alfabeto latino. Gli implementatori dovrebbero inoltre rispettare lo Unicode Standard. Requisiti di "
            "dettaglio sull'implementazione multilingua sono nell'annex E normativo."
        ),
        "testo_integrale": (
            "Trusted lists shall be issued supporting at least the UK English language, using the 'en' language "
            "code as specified in IETF RFC 5646 [11] and annex E, and may be issued supporting multiple "
            "(national) languages. For all the fields where support of multiple language is applicable, the field "
            "format specifications refer to the use of multilingual character string or pointer to which the "
            "following general rules shall apply: 1) A multilingual character string shall be a character string "
            "as defined in ISO/IEC 10646 [5] encoded in UTF-8. Each multilingual character string shall consist "
            "of two parts: a tag, conformant to IETF RFC 5646 [11] and in lower case, that identifies the "
            "language in which the string is expressed, and the text in that language. The same content may be "
            "represented in multiple languages by a sequence of multilingual character strings. 2) A multilingual "
            "pointer shall be a URI that identifies a resource expressed in a particular language. Each "
            "multilingual pointer shall consist of two parts: a tag, conformant to IETF RFC 5646 [11], that "
            "identifies the language in which the content pointed-to by the URI is expressed, and the URI "
            "expressed as a character string with the syntax specified by IETF RFC 3986 [8], identifying a "
            "resource expressed in the given language. The same content may be represented in multiple languages "
            "by a sequence of multilingual pointers. Whenever the native terms cannot be represented using the "
            "Latin alphabet, as defined in ISO/IEC 10646 [5], one issue of the term in the native language plus "
            "one issue with a transliteration to the Latin alphabet shall be used. Implementers should also "
            "comply with the Unicode Standard [i.13]. Further detailed requirements regarding multilingual "
            "implementation are specified in normative annex E."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.1.5 (Value of Country Code fields)",
        "testo": (
            "Tutti i campi che portano valori di Country Code, denotati 'CC', devono essere in lettere maiuscole "
            "e conformi a: a) codici ISO 3166-1 Alpha 2, con le eccezioni del codice 'UK' per il Regno Unito e "
            "'EL' per la Grecia e con l'uso del codice 'EU' quando l'ambito del campo è l'Unione europea e/o la "
            "Commissione europea; oppure b) estensioni comunemente usate con ambito regionale (es. AP per Asia "
            "Pacific, ASIA); oppure c) altro identificatore riconosciuto per identificare raggruppamenti "
            "multi-stato e non in conflitto con a) o b) (es. GCC, ASEAN)."
        ),
        "testo_integrale": (
            "All fields carrying Country Codes values, denoted by \"CC\", shall be in capital letters and in "
            "accordance with either: a) ISO 3166-1 [15] Alpha 2 codes with the following exceptions: 1) the "
            "Country Code for United Kingdom shall be \"UK\"; 2) the Country Code for Greece shall be \"EL\"; 3) when "
            "the scope of the field is the European Union and/or the European Commission the code \"EU\" shall be "
            "used; or b) commonly used extensions with regional scope (e.g. AP for Asia Pacific, ASIA); or c) "
            "another identifier recognized for identifying multi-state grouping and that does not conflict with "
            "a), or b) (e.g. GCC, ASEAN)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.1 (TSL Tag)",
        "testo": (
            "Il campo TSL Tag deve essere presente: la TL è etichettata per facilitarne l'identificazione durante "
            "le ricerche elettroniche e il tag è un attributo dell'elemento radice <tsl:TrustServiceStatusList>. "
            "Il formato è una stringa di caratteri che indica che la struttura dati è una TL, ovvero la "
            "rappresentazione in caratteri dell'URI TSLTag. Il valore deve essere unico e consentire a uno "
            "strumento di ricerca sul web di stabilire, durante una ricerca mondiale di TL, che la risorsa "
            "individuata è effettivamente una TL; devono essere presenti solo i caratteri necessari a "
            "rappresentare compiutamente l'URI."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: The TL is tagged to facilitate its "
            "identification during electronic searches. The tag is an attribute of <tsl:TrustServiceStatusList> "
            "root element. Format: A character string which indicates that the data structure is a TL. This shall "
            "be the character representation of the TSLTag URI. Value: A unique value enabling a web-searching "
            "tool to establish during a WWW-wide search for TLs that a resource it has located is indeed a TL. "
            "Only the characters required to fully represent the URI shall be present."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.3.1 (TSL version identifier)",
        "testo": (
            "Il campo TSL version identifier deve essere presente e specifica la versione del formato della TL. "
            "Il formato è un intero e il valore deve essere '6'. Nota: il campo è incrementato solo quando "
            "cambiano le regole di parsing della TL, ad esempio per aggiunta/rimozione di un campo o per modifica "
            "dei valori o del significato di un campo esistente; revisioni della specifica che non cambiano le "
            "regole di parsing della TL possono essere fatte senza revisionare questo campo."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the version of the TL format. "
            "Format: Integer. Value: It shall be \"6\". NOTE: This field will only be incremented when the rules "
            "for parsing the TL change, e.g. through addition/removal of a field or a change to the values or "
            "meaning of an existing field. Revisions to the specification which do not change the parsing rules "
            "of the TL may be made without revision to this field."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.3.2 (TSL sequence number)",
        "testo": (
            "Il campo TSL sequence number deve essere presente e specifica il numero di sequenza della TL. Il "
            "formato è un intero. Alla prima emissione della TL il numero di sequenza deve essere 1; il valore "
            "deve essere incrementato a ogni emissione successiva e non può, in nessuna circostanza, essere "
            "riciclato a '1' né a un valore inferiore a quello della TL attualmente in vigore."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the sequence number of the TL. "
            "Format: Integer. Value: At the first release of the TL, the value of the sequence number shall be 1. "
            "The value shall be incremented at each subsequent release of the TL and shall not, under any "
            "circumstance, be re-cycled to \"1\" or to any value lower than the one of the TL currently in force."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.3.3 (TSL type)",
        "testo": (
            "Il campo TSL type deve essere presente e specifica il tipo di trusted list, permettendo a un parser "
            "di determinare la forma dei campi successivi attesi secondo il documento. Il formato è un indicatore "
            "espresso come URI: nel contesto delle trusted list degli Stati membri UE l'URI è "
            "'http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric' (clause D.5); i TLSO di Paesi non UE e "
            "organizzazioni internazionali usano l'URI "
            "'http://uri.etsi.org/TrstSvc/TrustedList/TSLType/CClist' (clause D.6, con 'CC' dal campo "
            "Scheme territory) oppure un URI definito ad hoc o registrato sotto l'ETSI Identified Organization "
            "Domain (clause D.3). Quando la TL contiene esclusivamente un elenco di puntatori verso altre TL e "
            "verso TL Issuer indipendentemente responsabili dell'approvazione o riconoscimento di una comunità di "
            "servizi fiduciari, l'URI va impostato a "
            "'http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUlistofthelists' (Stati membri UE, clause D.5) "
            "oppure a 'http://uri.etsi.org/TrstSvc/TrustedList/TSLType/CClistofthelists' (non UE, clause D.6) o a "
            "un URI definito ad hoc/registrato "
            "(clause D.3). Nota: per Paesi non UE e organizzazioni internazionali il tipo identifica una lista "
            "che soddisfa i requisiti del documento e fornisce informazioni di stato basate su uno scheme di "
            "approvazione, consentendo a qualunque interessato di determinare se un servizio fiduciario opera o "
            "ha operato sotto tale scheme; l'adozione del documento per queste liste favorisce la dichiarazione "
            "di mutuo riconoscimento tra servizi fiduciari e relativi output."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the type of the trusted list. It "
            "permits a parser to determine the form of any following field to expect according to the present "
            "document. Format: An indicator expressed as a URI. Value: In the context of EU Member State trusted "
            "lists, the URI shall be set to \"http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric\" as "
            "defined in clause D.5. TLSOs from non-EU countries and international organizations shall use: - the "
            "following URI as defined in clause D.6: \"http://uri.etsi.org/TrstSvc/TrustedList/TSLType/CClist "
            "where \"CC\" (see clause 5.1.5) identifies the community to which the URI applies and is as used in "
            "the 'Scheme territory field' (clause 5.3.10); or - a URI defined on purpose or registered under ETSI "
            "Identified Organization Domain as described in clause D.3 of the present document. NOTE: In the "
            "context of non-EU countries or international organizations, it refers to a list meeting the "
            "requirements of the present document and providing assessment scheme based approval status "
            "information about trust services from trust service providers which are approved by the competent "
            "trusted list scheme operator or by the State or body in charge and from which the TLSO depends or by "
            "which it is mandated, for compliance with the relevant provisions of the applicable approval scheme "
            "and the applicable legislation. This may be used to enable in practice any interested party to "
            "determine whether a trust service from a non-EU country or an international organization, is or was "
            "operating under an approval scheme, currently or at some time in the past (e.g. at the time the "
            "service was provided, or at the time at which a transaction reliant on that service took place). The "
            "adoption of the present document for such non-EU countries or international organizations trusted "
            "lists will facilitate the declaration of mutual recognition between trust services and trust "
            "services outputs. When the TL contains exclusively a list of pointers towards other TLs and TL "
            "Issuers which are independently responsible for the approval or recognition of a community of trust "
            "services through a process of direct oversight (whether voluntary or regulatory), the URI shall be "
            "set: - in the context of EU Member States' trusted lists, to: "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUlistofthelists\" as defined in clause D.5; or - in "
            "the context of non-EU countries and international organizations trusted lists, to: • "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/TSLType/CClistofthelists\" as defined in clause D.6 where "
            "\"CC\" (see clause 5.1.5) identifies the community to which the URI applies and is as used in the "
            "'Scheme territory field' (clause 5.3.10); or • a URI defined on purpose or registered under ETSI "
            "Identified Organization Domain as described in clause D.3 of the present document."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.3.4 (Scheme operator name)",
        "testo": (
            "Il campo Scheme operator name deve essere presente e specifica il nome dell'entità incaricata di "
            "stabilire, pubblicare, firmare e mantenere la trusted list. Il formato è una sequenza di stringhe "
            "multilingua. Il valore deve essere il nome formale con cui opera l'entità legale associata "
            "all'entità incaricata di stabilire, pubblicare e mantenere la TL, o l'entità mandataria (es. per le "
            "agenzie amministrative governative); deve essere il nome usato nella registrazione o autorizzazione "
            "formale e al quale indirizzare ogni comunicazione formale."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the name of the entity in charge of "
            "establishing, publishing, signing and maintaining the trusted list. Format: A sequence of "
            "multilingual character strings (see clause 5.1.4). Value: The name of the scheme operator shall be "
            "the formal name under which the associated legal entity or mandated entity (e.g. for governmental "
            "administrative agencies) associated with the legal entity in charge of establishing, publishing and "
            "maintaining the trusted list operates. It shall be the name used in formal legal registration or "
            "authorization and to which any formal communication should be addressed."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.3.5.0 (General)",
        "testo": (
            "Il campo Scheme operator address deve essere presente e specifica l'indirizzo dell'entità legale o "
            "dell'organizzazione mandataria identificata nel campo Scheme operator name (clause 5.3.4), per le "
            "comunicazioni sia postali sia elettroniche. È un campo multi-parte, composto dall'indirizzo fisico "
            "dello scheme operator (clause 5.3.5.1) e dall'indirizzo elettronico dello scheme operator (clause "
            "5.3.5.2)."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the address of the legal entity or "
            "mandated organization identified in the 'Scheme operator name' field (clause 5.3.4) for both postal "
            "and electronic communications. Format: This is a multi-part field consisting of the scheme operator "
            "physical address specified in clause 5.3.5.1 and the scheme operator electronic address specified in "
            "clause 5.3.5.2."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.3.5.1 (Scheme operator postal address)",
        "testo": (
            "Il campo Scheme operator postal address deve essere presente e specifica l'indirizzo postale "
            "dell'entità legale identificata nella clause 5.3.4, con la possibilità di includere l'indirizzo in "
            "più lingue. Il formato è una o più sequenze di stringhe multilingua, ciascuna delle quali deve dare "
            "gli attributi dell'entità legale: indirizzo (sottocomponenti delimitati internamente da ';'), "
            "località (città), facoltativamente Stato o Provincia se applicabile, codice postale se applicabile, "
            "nome del Paese come codice di due caratteri secondo la clause 5.1.5 lettera a. Il valore dev'essere "
            "un indirizzo postale presso cui lo scheme operator fornisce un servizio di help line gestito tramite "
            "posta ordinaria e trattato come ci si attende da normali servizi imprenditoriali; gli utenti "
            "(sottoscrittori, terzi affidanti) dovrebbero usare questo indirizzo come punto di contatto per "
            "richieste, reclami, ecc. verso lo scheme operator."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the postal address of the legal "
            "entity identified in clause 5.3.4, with the provision for the inclusion of the address in multiple "
            "languages. Format: Sequence(s) of multilingual character strings (see clause 5.1.4). Each sequence "
            "of character strings shall give the following attributes pertaining to the legal entity: - street "
            "address (sub-components internally delimited by \";\"); - locality (town/city); - optionally, if "
            "applicable, State or Province name; - postal code, if applicable; - country name as a two-character "
            "code in accordance with clause 5.1.5 (a). Value: This shall be a postal address at which the scheme "
            "operator provides a help line service which is operated through conventional (physical) mail and "
            "which is processed as would be expected by normal business services. Users (subscribers, relying "
            "parties) should use this address as the contact point for enquiries, complaints, etc. to the scheme "
            "operator."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.3.5.2 (Scheme operator electronic address)",
        "testo": (
            "Il campo Scheme operator electronic address deve essere presente e specifica l'indirizzo e-mail, "
            "l'URI del sito web e l'eventuale numero di telefono dell'entità legale identificata nella clause "
            "5.3.4 per le comunicazioni elettroniche. Il formato è una sequenza di stringhe multilingua che dà: "
            "obbligatoriamente un indirizzo e-mail come URI nella forma specificata da IETF RFC 3986 con lo "
            "schema URI definito in IETF RFC 2368; obbligatoriamente un sito web come URI nella forma specificata "
            "da IETF RFC 3986; facoltativamente un numero di telefono come URI nella forma specificata da IETF "
            "RFC 3986 con lo schema URI 'tel' definito in IETF RFC 3966. Le prime due stringhe di caratteri "
            "devono essere presenti, la terza è facoltativa. Il valore: l'indirizzo e-mail e, quando presente, il "
            "numero di telefono devono essere recapiti presso cui lo scheme operator fornisce un servizio di help "
            "line che tratta questioni relative alla TL e trattati come ci si attende da normali servizi "
            "imprenditoriali; l'URI del sito web deve condurre a una capacità tramite cui l'utente può comunicare "
            "con un servizio di help line che tratta questioni relative alla TL."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the email address, the web-site URI "
            "and optional telephone number of the legal entity identified in clause 5.3.4 for electronic "
            "communications. Format: A sequence of multilingual character strings (see clause 5.1.4) giving: - "
            "mandatorily, an e-mail address as a URI, in the form specified by IETF RFC 3986 [8], with the URI "
            "scheme defined in IETF RFC 2368 [6]; - mandatorily, a web-site as a URI, in the form specified by "
            "IETF RFC 3986 [8]; - optionally, a telephone number as a URI, in the form specified by IETF RFC 3986 "
            "[8], with the \"tel\" URI scheme defined in IETF RFC 3966 [17]. The first two character strings shall "
            "be present. The third one is optional. Value: The e-mail address, and the telephone number when "
            "present, shall be an address, and respectively a phone number when present, at which the scheme "
            "operator provides a help line service which addresses TL-related matters and which are processed as "
            "would be expected by normal business services. As regards a web-site URI, this shall lead to a "
            "capability whereby the user may communicate with a help line service which addresses TL-related "
            "matters and which is processed as would be expected by normal business services."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.3.6 (Scheme name)",
        "testo": (
            "Il campo Scheme name deve essere presente e specifica il nome con cui opera lo scheme. Il formato è "
            "una sequenza di stringhe multilingua definite come segue: la versione inglese dev'essere una stringa "
            "strutturata come 'CC:EN_name_value', dove 'CC' è il codice usato nel campo Scheme territory (clause "
            "5.3.10), ':' è il separatore e 'EN_name_value' è il nome dello scheme; ogni versione in lingua "
            "nazionale dev'essere una stringa strutturata come 'CC:name_value', dove 'name_value' è la traduzione "
            "ufficiale in lingua nazionale del suddetto EN_name_value. Il valore deve essere il nome usato nei "
            "riferimenti formali allo scheme, deve essere unico e non utilizzato da alcun altro scheme gestito "
            "dallo stesso soggetto."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the name under which the scheme "
            "operates. Format: A sequence of multilingual character strings (see clause 5.1.4), defined as "
            "follows: - The English version shall be a character string structured as follows: • "
            "CC:EN_name_value; where: • 'CC' is the code used in the 'Scheme territory field' (clause 5.3.10); • "
            "':' is used as the separator; • 'EN_name_value' is the name of the scheme. - Any national language "
            "version shall be a character string structured as follows: • CC:name_value; where: • 'CC' is the "
            "code used in the 'Scheme territory field' (clause 5.3.10); • ':' is used as the separator; • "
            "'name_value' is the national language official translation of the above EN_name_value. Value: The "
            "name of the scheme shall be the name which is used in formal references to the scheme in question, "
            "shall be unique and shall not be used by any other scheme operated by the same entity."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.3.7 (Scheme information URI)",
        "testo": (
            "Il campo Scheme information URI deve essere presente e specifica gli URI dove gli utenti (terzi "
            "affidanti) possono ottenere informazioni specifiche sullo scheme. Il formato è una sequenza di "
            "puntatori multilingua. Gli URI referenziati devono dare un percorso verso informazioni che "
            "descrivono: ambito e contesto della trusted list; descrizione generale e informazioni dettagliate "
            "sullo scheme (di approvazione) sottostante; informazioni sui processi e sulle procedure seguite dal "
            "TLSO, o dal corpo da cui dipende o da cui è mandatato, nell'approvare i TSP e dai TSP per essere "
            "approvati; informazioni sui criteri in base ai quali i TSP sono approvati; informazioni sui criteri "
            "e sulle regole usati per selezionare gli assessor e su come i TSP sono da essi valutati; "
            "responsabilità separate ed eventuali liability di ciascun corpo dove corpi distinti forniscono "
            "aspetti distinti di supervisione, accreditamento e gestione dello scheme; e altre informazioni di "
            "contatto e generali applicabili alla gestione dello scheme."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the URI(s) where users (relying "
            "parties) can obtain scheme-specific information. Format: A sequence of multilingual pointers (see "
            "clause 5.1.4). Value: The referenced URI(s) shall provide a path to information describing "
            "appropriate information about the scheme, including: - scope and context of the trusted list; - "
            "general description and detailed information about underlying (approval) scheme; - information about "
            "the process and procedures followed: • by the TLSO, or the body from which it depends or by which it "
            "is mandated, being in charge to approve TSPs; and • by the TSPs for being approved; - information "
            "about the criteria against which TSPs are approved; - information about the criteria and rules used "
            "to select assessors and defining how TSPs are assessed by them; - where separate bodies provide "
            "separate aspects of supervision, accreditation and scheme operation, the separate responsibilities "
            "and any liabilities of each body; and - other contact and general information that may apply to the "
            "scheme operation."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.3.8 (Status determination approach)",
        "testo": (
            "Il campo Status determination approach deve essere presente e specifica l'identificatore "
            "dell'approccio di determinazione dello stato. Il formato è un indicatore espresso come URI: nel "
            "contesto delle trusted list degli Stati membri UE l'URI è "
            "'http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate' (clause D.5); i TLSO di Paesi non "
            "UE e organizzazioni internazionali usano l'URI "
            "'http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/CCdetermination' (clause D.6, con "
            "'CC' sostituito dal codice usato nel campo Scheme territory, clause 5.3.10) oppure un URI definito "
            "ad hoc o registrato sotto l'ETSI Identified Organization Domain (clause D.3)."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the identifier of the status "
            "determination approach. Format: An indicator expressed as a URI. Value: In the context of EU Member "
            "State trusted lists, the URI shall be set to "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate\" as defined in clause D.5. TLSOs "
            "from non-EU countries and international organizations shall use either: - the "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/CCdetermination\" URI as defined in clause D.6 "
            "and where \"CC\" is replaced by the code used in the 'Scheme territory field' (clause 5.3.10); or - a "
            "URI defined on purpose or registered under ETSI Identified Organization Domain as described in "
            "clause D.3 of the present document."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.3.9 (Scheme type/community/rules)",
        "testo": (
            "Il campo Scheme type/community/rules deve essere presente e specifica gli URI dove gli utenti (terzi "
            "affidanti) possono ottenere informazioni su tipo, comunità e regole dello scheme rispetto alle quali "
            "i servizi inclusi nella lista sono approvati e valutati e da cui si può determinare il tipo di "
            "scheme o di comunità. Il formato è una sequenza di puntatori multilingua. Gli URI referenziati "
            "devono identificare la policy/regole specifiche rispetto alle quali i servizi sono approvati e "
            "valutati e la descrizione di come usare e interpretare il contenuto della trusted list. Dove è "
            "fornito più di un URI, ciascuno dev'essere un sottoinsieme completo della policy definita dal suo "
            "predecessore (es. una policy sovranazionale può essere omnicomprensiva e le singole nazioni parte di "
            "quell'entità possono avere proprie implementazioni nell'ambito di tale policy di alto livello). "
            "Quando i TLSO partecipano a uno scheme più ampio di trusted list che condividono regole comuni e "
            "puntano a un testo descrittivo che si applica alla TL di ciascun TLSO, va usato un URI comune a "
            "tutti i TLSO che denoti la partecipazione della trusted list (identificata tramite TSL type e Scheme "
            "name) a uno scheme più ampio di trusted list, identifichi una risorsa da cui gli utenti possono "
            "ottenere le policy/regole di valutazione e una risorsa da cui ottenere le regole d'uso comuni a "
            "tutte le trusted list dello scheme più ampio; nel contesto degli Stati membri UE questo URI comune è "
            "'http://uri.etsi.org/TrstSvc/TrustedList/schemerules/EUcommon' (clause D.5). Il campo deve includere "
            "inoltre un URI specifico della trusted list nazionale, che punta a un testo descrittivo applicabile "
            "a quella TL: l'URI 'http://uri.etsi.org/TrstSvc/TrustedList/schemerules/CC' (clause D.4, con CC "
            "sostituito dal codice del campo Scheme territory), da cui i TLSO possono definire ulteriori sub-URI "
            "sotto la propria responsabilità; oppure, solo per Paesi non UE e organizzazioni internazionali, un "
            "URI definito ad hoc o registrato (clause D.3)."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the URI(s) where users (relying "
            "parties) can obtain scheme type/community/rules information against which services included in the "
            "list are approved and assessed, and from which the type of scheme or community may be determined. "
            "Format: A sequence of multilingual pointers (see clause 5.1.4). Value: The referenced URI(s) shall "
            "identify: - the specific policy/rules against which services included in the list are approved and "
            "assessed, and from which the type of scheme or community may be determined; - the description about "
            "how to use and interpret the content of the trusted list. Where more than one URI is provided, each "
            "shall be a complete subset of the policy defined by its predecessor (e.g. a supra-national policy "
            "might be overarching; separate nations part of this supra- national entity may have their own "
            "implementations as part of this supra-national high-level policy). When TLSOs participate to a wider "
            "scheme for issuing trusted lists which share common rules and which point towards a descriptive text "
            "that applies to the TL of each TLSO, a URI common to all TLSO shall be used: - denoting "
            "participation of the trusted list (identified via the \"TSL type\" (see clause 5.3.3) and \"Scheme "
            "name\" (clause 5.3.6)) in a wider scheme of trusted lists (i.e. a TL listing pointers to all members "
            "publishing and maintaining a trusted list); - identifying a resource from where users can obtain "
            "policy/rules against which services included in the lists are assessed; - identifying a resource "
            "from where users can obtain description about how to use and interpret the content of the trusted "
            "lists. These usage rules shall be common to all trusted lists being part of the wider scheme of "
            "schemes whatever the type of listed services. In the context of EU Member States' trusted lists, "
            "this common URI shall be set to \"http://uri.etsi.org/TrstSvc/TrustedList/schemerules/EUcommon\" as "
            "defined in clause D.5. This field shall include a URI specific to a country's (national) trusted "
            "list and point towards a descriptive text that applies to this country's (national) TL: - using the "
            "following URI as defined in clause D.4: • http://uri.etsi.org/TrstSvc/TrustedList/schemerules/CC; • "
            "where CC is replaced by the code used in the 'Scheme territory' field (clause 5.3.10); • TLSOs may "
            "define additional URIs from the above specific URI (i.e. sub-URIs defined from this specific URI "
            "used as root). The definition and management of the sub-structure under the above URIs is under the "
            "responsibility of the TLSO; or - in the context of non-EU countries and international organizations "
            "only, using a URI defined on purpose or registered under ETSI Identified Organization Domain as "
            "described in clause D.3."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.3.10 (Scheme territory)",
        "testo": (
            "Il campo Scheme territory deve essere presente e specifica il Paese o territorio in cui lo scheme è "
            "stabilito e si applica. Il formato è una stringa di caratteri conforme alla clause 5.1.5."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the country or territory in which "
            "the scheme is established and applies. Format: Character string in accordance with clause 5.1.5."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.3.11 (TSL policy/legal notice)",
        "testo": (
            "Il campo TSL policy/legal notice deve essere presente e specifica la policy dello scheme oppure "
            "fornisce un avviso sullo stato giuridico dello scheme o sui requisiti legali soddisfatti dallo "
            "scheme per la giurisdizione in cui è stabilito e/o su vincoli e condizioni cui è soggetto il "
            "mantenimento e la pubblicazione della TL. Il formato è: a) una sequenza di puntatori multilingua per "
            "l'uso specifico come puntatore alla policy o all'avviso; oppure b) una sequenza di stringhe "
            "multilingua che forniscono il testo effettivo di tale policy o avviso, in tutte le lingue "
            "necessarie. Ogni testo referenziato deve fornire informazioni che descrivono la policy sotto cui "
            "opera lo scheme operator o gli avvisi legali rilevanti di cui gli utenti della TL devono essere "
            "consapevoli."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the scheme's policy or provides a "
            "notice concerning the legal status of the scheme or legal requirements met by the scheme for the "
            "jurisdiction in which the scheme is established and/or any constraints and conditions under which "
            "the TL is maintained and published. Format: Either: a) a sequence of multilingual pointers (see "
            "clause 5.1.4) for specific use as a pointer to the policy or notice; or b) a sequence of "
            "multilingual character strings (see clause 5.1.4) providing the actual text of any such policy or "
            "notice, in as many languages as necessary. Value: Any referenced text shall provide information "
            "describing the policy under which the Scheme Operator operates or any relevant legal notices with "
            "which users of the TL should be aware."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.3.12 (Historical information period)",
        "testo": (
            "Il campo Historical information period deve essere presente e specifica la durata per cui le "
            "informazioni storiche della TL sono mantenute una volta incluse. Il formato è un intero e il suo "
            "valore deve essere '65535', che significa che le informazioni storiche fornite nella trusted list "
            "non sono mai rimosse."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the duration over which historical "
            "information in the TL is maintained once it has been included. Format: Integer. Value: The value of "
            "this integer shall be '65535', which signifies that historical information provided in the trusted "
            "list shall never be removed."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.3.13 (Pointers to other TSLs)",
        "testo": (
            "Il campo Pointers to other TSLs deve essere presente per le trusted list degli Stati membri UE ed è "
            "opzionale per Paesi non UE e organizzazioni internazionali: referenzia trusted list rilevanti o "
            "liste di trusted list rilevanti. Il formato è una sequenza di una o più tuple, ciascuna con: una "
            "stringa contenente l'URI del formato machine processable di un'altra TL; una o più identità digitali "
            "che rappresentano tutte l'emittente della TL puntata, formattate come specificato nella clause "
            "5.5.3; e informazioni aggiuntive come insieme di TL Qualifier (TSLType, Scheme operator name, Scheme "
            "type/community/rules, Scheme territory e Mime type tra i media type definiti nella clause 6.2). Più "
            "identità digitali possono servire a gestire il processo di firma della lista puntata (es. per "
            "scadenza/sostituzione delle chiavi di firma o ammissione di più chiavi), ma almeno una di esse deve "
            "permettere l'autenticazione con successo della lista puntata prima del suo uso. Nel contesto degli "
            "Stati membri UE il campo deve includere il puntatore alla lista compilata dalla Commissione europea "
            "con i link a tutte le trusted list degli Stati membri (List Of Trusted Lists, LOTL) come notificata "
            "nella Gazzetta Ufficiale dell'Unione europea, con le identità digitali pubblicate nella Gazzetta "
            "Ufficiale; per Paesi non UE e organizzazioni internazionali il campo può referenziare qualunque "
            "trusted list o lista di trusted list rilevante."
        ),
        "testo_integrale": (
            "Presence: This field shall be present for EU Member States' trusted lists. It is optional for non-EU "
            "countries and international organizations. Description: It references any relevant trusted list or "
            "any relevant list of trusted lists. Format: Sequence of one or more tuples, each tuple giving: a) a "
            "string containing the URI of the machine processable format of another TL; b) one or more digital "
            "identities, all representing the issuer of the TL pointed to, formatted as specified in clause "
            "5.5.3; and c) additional information as a set of TL Qualifiers: • TSLType, as defined in clause "
            "5.3.3; • Scheme operator name, as defined in clause 5.3.4; • Scheme type/community/rules, as defined "
            "in clause 5.3.9; • Scheme territory, as defined in clause 5.3.10; and • Mime type, as one of the "
            "media types defined in clause 6.2. Value: More than one digital identity may be used to help the "
            "management of the pointed-to list signing process (e.g. in case of expiration/substitution of "
            "pointed-to list signing keys or more than a single signing key is allowed to sign this list). One of "
            "such digital identities shall allow successful authentication of the pointed-to list before its use. "
            "In the context of EU Member State trusted lists, this field shall include the pointer to a European "
            "Commission compiled list of links (pointers) towards all trusted lists from the Member States, the "
            "so-called List Of Trusted Lists (LOTL) as it is notified in the Official Journal of the European "
            "Union. The referenced digital identities, validly representing the issuer(s) of the LOTL pointed to, "
            "formatted as specified in clause 5.5.3 (Service digital identity) shall be as published in the "
            "Official Journal of the European Union. For non-EU countries and international organizations, this "
            "field may reference any relevant trusted list or list of trusted lists (e.g. the European List Of "
            "Trusted List as it is notified in the Official Journal of the European Union)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Presenza obbligatoria per le trusted list degli Stati membri UE; campo opzionale per i Paesi non UE "
            "e le organizzazioni internazionali."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.3.14 (List issue date and time)",
        "testo": (
            "Il campo List issue date and time deve essere presente e specifica la data e l'ora in cui la trusted "
            "list è stata emessa. Il formato è un valore di data-ora (clause 5.1.3) e il valore è il tempo "
            "Coordinated Universal Time (UTC) in cui la TL è stata emessa. Nota: si veda anche il requisito "
            "applicabile al TLSO di garantire la coerenza tra la (ri)emissione di una trusted list e la data "
            "effettiva in cui lo stato di un servizio è stato aggiornato (clause 5.5.5)."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the date and time on which the "
            "trusted list was issued. Format: Date-time value (see clause 5.1.3). Value: Coordinated Universal "
            "Time (UTC) at which the TL was issued. NOTE: See also the applicable requirement on TLSO to ensure "
            "the consistency of the (re)-issuance of a trusted list and the actual date when a service status has "
            "been updated (clause 5.5.5)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.3.15 (Next update)",
        "testo": (
            "Il campo Next update deve essere presente e specifica la data e l'ora entro cui, al più tardi, uno "
            "aggiornamento della TL sarà reso disponibile dallo scheme operator, oppure null per indicare una TL "
            "chiusa. Il formato è un valore di data-ora (clause 5.1.3) e il valore è il tempo Coordinated "
            "Universal Time (UTC) entro cui al più tardi un aggiornamento della TL deve essere emesso. Lo scheme "
            "operator deve emettere e pubblicare un aggiornamento della TL prima di tale data e ora ogni volta "
            "che lo scheme di approvazione sottostante lo richieda, in particolare quando cambiano informazioni "
            "relative a TSP o servizi (es. il loro stato). In assenza di cambi di stato intermedi di TSP o "
            "servizi coperti dallo scheme, la TL deve essere riemessa entro la scadenza dell'ultima TL emessa; le "
            "TL con Next update nel passato vanno scartate come scadute, come misura per ridurre il rischio di "
            "sostituzione con una vecchia TL da parte di un attaccante. Le applicazioni che implementano "
            "meccanismi di cache devono considerare che altre TL possono essere emesse e pubblicate prima della "
            "data e ora di Next update (si veda l'annex I). La differenza tra Next update e List issue date and "
            "time non deve superare i sei mesi. Se uno scheme cessa l'operatività o interrompe la pubblicazione "
            "della propria TL, va pubblicata una versione finale con lo stato di tutti i servizi indicato come "
            "'expired' e questo campo posto a null."
        ),
        "testo_integrale": (
            "Presence: This field shall be present. Description: It specifies the date and time by which, at the "
            "latest, an update of the TL will be made available by the scheme operator or be null to indicate a "
            "closed TL. Format: Date-time value (see clause 5.1.3). Value: Coordinated Universal Time (UTC) by "
            "which, at the latest, an update of the TL shall be issued. The scheme operator shall issue and "
            "publish an update of the TL before that Next Update date and time whenever the underlying approval "
            "scheme will require so, in particular when changes occur to TSP or service related information (e.g. "
            "its status). In the event of no interim status changes to any TSP or service covered by the scheme, "
            "the TL shall be re-issued by the time of expiration of the last TL issued. TL with a Next update "
            "occurring in the past shall be discarded as expired as a measure to reduce the risk of a "
            "substitution by an attacker with an old TL. Applications shall consider, in the event they implement "
            "some caching mechanism, that other TLs could be issued and published before 'Next update' date and "
            "time. See annex I for further information on application of trusted lists. The difference between "
            "the 'Next update' date and time and the 'List issue date and time' shall not exceed six (6) months. "
            "If a scheme ceases operations or halts publication of its TL, a final version shall be published "
            "with all services' status shown as \"expired\" (see Service current status) and this field set null."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.3.16 (Distribution points)",
        "testo": (
            "Il campo Distribution points è opzionale: quando usato specifica le ubicazioni in cui è pubblicata "
            "la TL corrente e in cui si possono trovare gli aggiornamenti della TL corrente. Il formato è una "
            "sequenza non vuota di URI. Il dereferenziamento dell'URI dato consegna sempre l'ultimo aggiornamento "
            "di questa TL; se sono specificati più distribution point, tutti devono fornire copie identiche della "
            "TL corrente o della sua versione aggiornata."
        ),
        "testo_integrale": (
            "Presence: This field is optional. Description: When used, it specifies locations where the current "
            "TL is published and where updates to the current TL can be found. Format: Non-empty sequence of "
            "URIs. Value: Dereferencing the given URI will always deliver the latest update of this TL. If "
            "multiple distribution points are specified, they all shall provide identical copies of the current "
            "TL or its updated version."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Campo opzionale: i requisiti di contenuto si applicano quando lo scheme operator lo utilizza."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.3.17 (Scheme extensions)",
        "testo": (
            "Il campo Scheme extensions non deve essere presente per le trusted list degli Stati membri UE ed è "
            "opzionale per Paesi non UE e organizzazioni internazionali: fornisce informazioni ed estensioni "
            "specifiche dello scheme che non richiedono un cambio del version identifier e che possono essere "
            "interpretate da tutte le parti accedenti secondo le regole dello scheme specifico. Il formato è una "
            "sequenza di Scheme extension dal formato lasciato aperto; ogni estensione deve avere un'indicazione "
            "della propria criticality. Ogni estensione della sequenza è selezionata dal TLSO secondo "
            "l'informazione che intende veicolare nella propria TL; il significato e il valore di ciascuna "
            "estensione sono definiti dalle sue specifiche di origine (definizione propria del TLSO o di altro "
            "soggetto, come una comunità o federazione di scheme, un ente di normazione, ecc.). L'indicazione di "
            "criticality ha la stessa semantica delle estensioni nei certificati X.509: un sistema che usa TL "
            "deve rifiutare la TL se incontra un'estensione critica che non riconosce, mentre un'estensione non "
            "critica può essere ignorata se non riconosciuta."
        ),
        "testo_integrale": (
            "Presence: This field shall not be present for EU Member States' trusted lists. It is optional for "
            "non-EU countries and international organizations. Description: It provides specific scheme-related "
            "information and enhancements that do not require a change in the version identifier, which can be "
            "interpreted by all accessing parties according to the specific scheme's rules. Format: Sequence of "
            "Scheme extensions whose format is left open. Each extension shall have an indication of its "
            "criticality. Value: Each extension of the sequence shall be selected by the TLSO according to the "
            "information it wishes to convey within its TL. The meaning and value of each extension shall be "
            "defined by its source specifications being either the TLSOs own definition or any other extension "
            "definition produced by another entity, such as a community or federation of schemes, a standards "
            "body, etc. The criticality indication shall have the same semantics as with extensions in "
            "X.509-certificates [1]. A system using TLs shall reject the TL if it encounters a critical extension "
            "it does not recognize, while a non-critical extension may be ignored if it is not recognized."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Campo vietato per le trusted list degli Stati membri UE; opzionale per i Paesi non UE e le "
            "organizzazioni internazionali."
        ),
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 5.3.18 (Trust Service Provider List)",
        "testo": (
            "Il campo Trust Service Provider List non deve essere presente se nessun TSP è o è stato approvato "
            "nel contesto dello scheme della trusted list; deve essere presente se uno o più servizi TSP sono o "
            "sono stati approvati sotto lo scheme. Contiene l'elenco dei TSP e dei loro servizi fiduciari "
            "approvati in conformità allo scheme della trusted list. Il formato è una sequenza di elementi Trust "
            "Service Provider, dove ciascun elemento è una tupla composta da un elemento TSP Information (clause "
            "5.4) e da un elemento TSP Services; l'elemento TSP Services è una sequenza di elementi TSP Service, "
            "ciascuno dei quali è una tupla composta da un elemento Service Information (clause 5.5) e da un "
            "elemento condizionale Service History; ciascun elemento Service History, quando presente, è una "
            "sequenza di elementi Service History Instance (clause 5.6). Il valore deve contenere una sequenza "
            "che identifica ogni TSP che fornisce uno o più servizi approvati, con dettagli sullo stato e sullo "
            "storico di stato di ciascun servizio del TSP, come illustrato nella figure 1 (clause 4)."
        ),
        "testo_integrale": (
            "Presence: If no TSP is or was approved in the context of the trusted list scheme, this field shall "
            "not be present. If one or more TSP services are or were approved under the TL scheme, this field "
            "shall be present. Description: List of TSPs and their trust services approved in accordance with the "
            "trusted list scheme. Format: Sequence of Trust Service Provider elements, where each Trust Service "
            "Provider element is a tuple made of a TSP Information element (see clause 5.4) and a TSP Services "
            "element, where the TSP Services element is a sequence of TSP Service elements, where each of such "
            "TSP Service element is a tuple made of a Service Information element (see clause 5.5) and a "
            "conditional Service History element. Each of such Service History element, when present, is a "
            "sequence of Service History Instance elements (see clause 5.6). Value: It shall contain a sequence "
            "identifying each TSP providing one or more of approved services, with details on the status and "
            "status history of each of the TSP's services, as illustrated in figure 1 (see clause 4)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Il campo è assente se nessun TSP è o è stato approvato nello scheme; è presente se uno o più servizi "
            "TSP sono o sono stati approvati."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = []

INDICE_ARTICOLI_LOCALE = [
    "clausola 5.1.1 (Trusted List Format)",
    "clausola 5.1.2 (Use of Uniform Resource Identifiers)",
    "clausola 5.1.3 (Date-time indication)",
    "clausola 5.1.4 (Language support)",
    "clausola 5.1.5 (Value of Country Code fields)",
    "clausola 5.2.1 (TSL Tag)",
    "clausola 5.3.1 (TSL version identifier)",
    "clausola 5.3.2 (TSL sequence number)",
    "clausola 5.3.3 (TSL type)",
    "clausola 5.3.4 (Scheme operator name)",
    "clausola 5.3.5.0 (General)",
    "clausola 5.3.5.1 (Scheme operator postal address)",
    "clausola 5.3.5.2 (Scheme operator electronic address)",
    "clausola 5.3.6 (Scheme name)",
    "clausola 5.3.7 (Scheme information URI)",
    "clausola 5.3.8 (Status determination approach)",
    "clausola 5.3.9 (Scheme type/community/rules)",
    "clausola 5.3.10 (Scheme territory)",
    "clausola 5.3.11 (TSL policy/legal notice)",
    "clausola 5.3.12 (Historical information period)",
    "clausola 5.3.13 (Pointers to other TSLs)",
    "clausola 5.3.14 (List issue date and time)",
    "clausola 5.3.15 (Next update)",
    "clausola 5.3.16 (Distribution points)",
    "clausola 5.3.17 (Scheme extensions)",
    "clausola 5.3.18 (Trust Service Provider List)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.1 (Trusted List Format)"),
        "nodo_a": ("obbligo", None, "Annex B.0 (General requirements)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.1 (Trusted List Format)"),
        "nodo_a": ("principio", None, "Annex C (XML schema)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.2 (Use of Uniform Resource Identifiers)"),
        "nodo_a": ("principio", None, "Annex D.0 (General)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.2 (Use of Uniform Resource Identifiers)"),
        "nodo_a": ("principio", None, "Annex D.3 (Scheme registered URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.4 (Language support)"),
        "nodo_a": ("obbligo", None, "Annex E.1 (General rules)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.3 (TSL type)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.5 (Value of Country Code fields)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.3 (TSL type)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.10 (Scheme territory)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.3 (TSL type)"),
        "nodo_a": ("principio", None, "Annex D.3 (Scheme registered URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.3 (TSL type)"),
        "nodo_a": ("principio", None, "Annex D.5 (EU specific trusted lists URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.3 (TSL type)"),
        "nodo_a": ("principio", None, "Annex D.6 (Non-EU specific trusted lists URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.4 (Scheme operator name)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4 (Language support)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.5.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.4 (Scheme operator name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.5.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.5.1 (Scheme operator postal address)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.5.0 (General)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.5.2 (Scheme operator electronic address)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.5.1 (Scheme operator postal address)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4 (Language support)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.5.1 (Scheme operator postal address)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.5 (Value of Country Code fields)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.5.1 (Scheme operator postal address)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.4 (Scheme operator name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.5.2 (Scheme operator electronic address)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4 (Language support)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.5.2 (Scheme operator electronic address)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.4 (Scheme operator name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.6 (Scheme name)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4 (Language support)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.6 (Scheme name)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.10 (Scheme territory)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.7 (Scheme information URI)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4 (Language support)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.8 (Status determination approach)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.10 (Scheme territory)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.8 (Status determination approach)"),
        "nodo_a": ("principio", None, "Annex D.3 (Scheme registered URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.8 (Status determination approach)"),
        "nodo_a": ("principio", None, "Annex D.5 (EU specific trusted lists URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.8 (Status determination approach)"),
        "nodo_a": ("principio", None, "Annex D.6 (Non-EU specific trusted lists URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.9 (Scheme type/community/rules)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4 (Language support)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.9 (Scheme type/community/rules)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.3 (TSL type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.9 (Scheme type/community/rules)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.6 (Scheme name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.9 (Scheme type/community/rules)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.10 (Scheme territory)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.9 (Scheme type/community/rules)"),
        "nodo_a": ("principio", None, "Annex D.3 (Scheme registered URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.9 (Scheme type/community/rules)"),
        "nodo_a": ("obbligo", None, "Annex D.4 (Common trusted lists URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.9 (Scheme type/community/rules)"),
        "nodo_a": ("principio", None, "Annex D.5 (EU specific trusted lists URIs)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.10 (Scheme territory)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.5 (Value of Country Code fields)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.11 (TSL policy/legal notice)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4 (Language support)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.13 (Pointers to other TSLs)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.3 (TSL type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.13 (Pointers to other TSLs)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.4 (Scheme operator name)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.13 (Pointers to other TSLs)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.9 (Scheme type/community/rules)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.13 (Pointers to other TSLs)"),
        "nodo_a": ("obbligo", None, "clausola 5.3.10 (Scheme territory)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.13 (Pointers to other TSLs)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.13 (Pointers to other TSLs)"),
        "nodo_a": ("obbligo", None, "clausola 6.2.1.1 (HTTP-Media Type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.14 (List issue date and time)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.3 (Date-time indication)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.14 (List issue date and time)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.5 (Current status starting date and time)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.15 (Next update)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.3 (Date-time indication)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.15 (Next update)"),
        "nodo_a": ("principio", None, "Annex I.1 (Introduction)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.18 (Trust Service Provider List)"),
        "nodo_a": ("principio", None, "clausola 4 (Overall structure of trusted lists)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3.18 (Trust Service Provider List)"),
        "nodo_a": ("obbligo", None, "clausola 5.6.1 (Service type identifier)"),
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
