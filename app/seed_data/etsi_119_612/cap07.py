"""ETSI TS 119 612 V2.4.1 (2025-08) - Electronic Signatures and Trust
Infrastructures (ESI); Trusted Lists.
Fonte 21 (la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 7:
Annex E (normative) Implementation requirements for multilingual support
(E.1-E.4), Annex F (informative) TL manual/auto field usage (Table F.1),
Annex G (normative) Management and policy considerations (G.0-G.8). Testo
ufficiale in app/.source_cache/etsi_119_612/cap07.txt (letto sempre con
selettore `:raw`, altrimenti il tool tronca le righe lunghe a 768 caratteri
introducendo "..." e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_119_612/manifest.json.

Modellazione (ADR-0007), stesso criterio gia' applicato alle altre fonti
ETSI gia' censite (ETSI EN 319 401/412/421/422, ETSI TS 119 431-1/2, 119 432,
119 461) e adattato alle clausole/sottoclausole di uno standard tecnico: un
nodo per ogni clausola/sottoclasse numerata che porta contenuto proprio; per
le clausole di cornice prive di requisito numerato un solo nodo Principio
dedicato. Questo capitolo produce 11 Obblighi e 3 Principi, 14 item di
indice. Scelte voce per voce:

- Intestazioni di annesso ("Annex E (normative): Implementation requirements
  for multilingual support", "Annex F (informative): TL manual/auto field
  usage", "Annex G (normative): Management and policy considerations") ->
  NESSUN nodo: sono titoli di puro raggruppamento, seguiti immediatamente
  dalla prima sottoclausola (E.1, Table F.1, G.0) e privi di testo proprio,
  esattamente come le intestazioni 5.3/5.4/5.5/5.6 del corpo del documento.

- Annex E.1 (General rules) -> 1 Obbligo "tecnico/sicurezza". "shall use"
  esplicito a carico dei TLSO ("When establishing their trusted lists, TLSOs
  shall use: language codes in lower case and country codes in upper case;
  language and country codes according to table E.1 with regards to EU MS").
  La tabella E.1 non genera un nodo proprio (non e' una clausola numerata ma
  il corredo della clausola E.1): tutte le 33 righe (nome breve in lingua
  sorgente, nome breve inglese, codice paese, codici lingua, eventuali note,
  traslitterazione latina) e la NOTE finale sui tre nomi traslitterati sono
  riportate in `testo_integrale` della riga E.1, ricostruite in forma
  esplicita leggibile ("ETICHETTA: valori") perche' pdftotext disallinea le
  celle (la nota "also Catalan (ca), Basque (eu), Galician (gl)" esce
  spezzata su due righe attorno a quella della Spagna: verificato a mano
  sulla posizione di colonna, la nota appartiene alla riga España/Spain).

- Annex E.2 (Multilingual character string) -> 1 Obbligo "tecnico/sicurezza".
  "shall fulfil the requirements of annex N of ISO/IEC 10646 [5] subject to
  the following restrictions" con 9 restrizioni numerate: le restrizioni 8) e
  9) sono formulate con "should" ("should follow the semantic rules defined
  by the Unicode Standard", "combining characters should not be used") e
  restano dentro la stessa riga perche' non sono una clausola numerata
  autonoma ma commi della stessa prescrizione, che complessivamente impone un
  comportamento al TLSO (raccomandazione modellata come Obbligo, precedente
  consolidato delle altre fonti ETSI: lo schema ha un solo tipo
  prescrittivo). La NOTE finale (livello di implementazione richiesto il piu'
  basso possibile per le applicazioni di parsing) e' contenuto interpretativo
  sostanziale e resta dentro `testo_integrale`.

- Annex E.3 (Multilingual pointer) -> 1 Obbligo "tecnico/sicurezza".
  Clausola condizionata: "If the content pointed by the multilingual pointer
  is plain text, it shall meet the following requirements" -> il vincolo
  vale solo per contenuti plain text; 9 restrizioni numerate, la 7) con
  sotto-voci a) e b) su SGML/HTML/XML/XHTML (a sua volta con "should"/"may",
  anch'esse dentro la stessa riga). Condizione registrata in
  `condizione_applicabilita`.

- Annex E.4 (Overall requirements) -> 1 Obbligo "tecnico/sicurezza". Il
  primo periodo ("The requirements of W3C Technical Report #20 [i.7] should
  be met") e' una raccomandazione; segue il requisito primario "all
  applications parsing TLs shall be able to store and manage all characters
  defined by ISO/IEC 10646 [5]". La NOTE finale (avviso all'utente su
  rappresentazione scorretta dei caratteri non supportati) e' sostanziale e
  resta in `testo_integrale`.

- Annex F (informative) -> 1 solo nodo, Principio "altro". L'annesso e' un
  blocco unico non numerato (due paragrafi di prosa + Table F.1): non esiste
  alcuna clausola numerata da cui ricavare piu' nodi, e generarne uno per
  riga di tabella sarebbe la stessa forzatura gia' scartata per i glossari
  (item di indice fittizi). La prosa e' dichiarativa/descrittiva (spiega
  cosa elencano le colonne 2 e 3 della tabella), quindi Principio e non
  Obbligo: l'annex e' etichettato "informative" e la frase "implementers are
  strongly recommended to satisfy the guidance which it provides" non
  introduce un requisito di conformita' (non c'e' alcun "shall" nell'annesso;
  la raccomandazione vale come guida di coerenza per gli implementatori).
  Tutte le righe di Table F.1 sono riportate in `testo_integrale`: i segni di
  spunta del PDF escono da pdftotext come glifo di uso privato U+F0FC, quindi
  ogni riga e' ricostruita in forma esplicita ("campo: Human-readable: si/no;
  Machine-processable: si/no", con i valori testuali "where recognized and
  meaningful" / "where recognized" delle righe "extensions"), conservando gli
  intestatari di raggruppamento originali (Identification Tag, Scheme
  information, TSP information, Service information, Historical service
  information, TSL signature information) come titoli di gruppo: nessun
  valore della tabella e' perso.

- Annex G.0 (General) -> 1 Principio "altro". Due frasi puramente
  introduttivo ("Specific criteria for the provision of revisions to TL
  information apply. These revisions will fall into the following
  categories."), nessun verbo prescrittivo e nessun soggetto obbligato: e' la
  cornice dell'annesso, non un requisito. Copre le categorie poi declinate
  in G.1-G.8.

- Annex G.1 (Change of scheme administrative information) -> 1 Obbligo
  "procedurale". "the TL shall be re-issued" in caso di modifiche materiali;
  nello stesso testo anche "the scheme should continue to operate with
  changes with regards to information related to the Scheme Operator and the
  TL being re-issued" (raccomandazione modellata come Obbligo). La NOTE
  (nessuna necessita' di modificare la TL se cambia l'informazione
  referenziata ma non il riferimento) e' interpretativa sostanziale e resta
  in `testo_integrale`.

- Annex G.2 (Trust-service identification) -> 1 Principio "altro". Testo
  interamente dichiarativo (importanza di identificare senza ambiguita' lo
  status del servizio; il campo della identita' digitale come unica opzione
  per un'identificazione sicura): nessun "shall"/"should" e nessun soggetto
  obbligato, quindi non diventa Obbligo.

- Annex G.3 (Change of trust service status) -> 1 Obbligo "procedurale".
  Requisito primario: "When any such change occurs the TL shall be re-issued
  with the previous current status becoming the most recent historical status
  and current status being amended". La stessa clausola contiene anche
  prescrizioni di conservazione ("This shall then be retained for the
  published retention period", "No service's \"Historical information\" shall
  be discarded"): la riga e' classificata "procedurale" perche' l'oggetto
  della clausola e' la gestione del cambio di stato della TL, mentre il
  profilo di conservazione resta descritto in `testo`. Rinvii testuali
  puntuali a clausole della stessa Fonte: "Service current status" (see
  clause 5.5.4) e "History information" (see clause 5.5.10) -> due relazioni
  "richiama" (stringhe di riferimento concordate con gli autori di cap03 e
  cap04).

- Annex G.4 (Change in trust service digital identity) -> 1 Obbligo
  "procedurale". Due casi puntati su "Service digital identity" (see clause
  5.5.3): nuova chiave pubblica -> "shall be added in the TL as a new service
  entry"; nuovo certificato per la stessa chiave pubblica -> "rules in clause
  5.5.3 apply", ammissibilita' del nuovo certificato all'insieme esistente di
  rappresentazioni e "no service history instance shall be generated". La
  frase "it may be added to the existing set of representations" e' una
  facolta' del TLSO e rientra nella stessa riga (un solo tipo prescrittivo).
  Rinvio interno a clause 5.5.3 -> 1 relazione "richiama".

- Annex G.5 (Amendment response times) -> 1 Obbligo "procedurale".
  "Changes to any TL information shall be provided in a timely fashion, not
  exceeding 24 hours"; la seconda prescrizione ("the corresponding change
  should be implemented and the TL re-issued in less than four working
  hours") e' una raccomandazione modellata come Obbligo, nella stessa riga
  perche' non numerata separatamente.

- Annex G.6 (On-going verification of authenticity) -> 1 Obbligo
  "tecnico/sicurezza". La clausola e' per meta' descrittiva (rischio di
  replica/sostituzione della TL e della PKC surrogata), ma enuncia il
  comportamento del soggetto: "This should be protected against by the scheme
  operator itself making frequent verification of its own TL and all
  authorized and recognized replications of it", piu' la riemissione regolare
  come garanzia di rotazione del valore della firma. Il contenuto non e'
  numerato in commi distinti, quindi una sola riga.

- Annex G.7 (User reference to TL) -> 1 Obbligo "informativo/trasparenza".
  "Scheme operators should assist in this by offering additional services to
  notify when a new TL is issued, or to guarantee frequent re-issue of a TL":
  raccomandazione di trasparenza verso gli utenti (destinatari
  "Terzi affidanti/pubblico") modellata come Obbligo. Il secondo periodo
  (limiti dei meccanismi di copie contemporanee) e' descrittivo e resta in
  `testo_integrale`.

- Annex G.8 (TL size) -> 1 Obbligo "tecnico/sicurezza". "Implementers should
  therefore take advantage of the opportunity to use URIs and limit embedded
  text as much as is reasonable": raccomandazione su dimensione della TL,
  tempi di scaricamento/parsing e banda dell'utente tipico, modellata come
  Obbligo; destinatario "Terzi affidanti/pubblico" (utente tipico della TL).

Nessuna delle clausole di questo capitolo contiene EXAMPLE. Le NOTE presenti
(E.1, E.2, E.3, E.4, G.1) sono contenuto interpretativo sostanziale e sono
tutte conservate verbatim in `testo_integrale`.

Citazioni esterne notate ma NON trasformate in relazioni (vietato in questa
fase; il collegamento cross-fonte e' demandato alla Fase 6 della sessione
principale, ADR-0009): ISO/IEC 10646 [5] (annex N, annex H, annex T, annex A,
clause 10, clause 14, clause B.1), ISO/IEC 6429 [13], ISO/IEC 2022 [14],
W3C Technical Report #20 [i.7] e Unicode Standard [i.13]. Le uniche relazioni
create sono interne a ETSI TS 119 612 e derivano da rinvii testuali puntuali
nel testo (G.3 -> 5.5.4 e 5.5.10, G.4 -> 5.5.3).
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "Annex E.1 (General rules)",
        "testo": (
            "Nell'istituire le proprie trusted list i TLSO devono usare codici di lingua in minuscolo e codici "
            "di paese in maiuscolo; per gli Stati membri UE i codici di lingua e paese sono quelli della tabella "
            "E.1. Quando e' presente una scrittura latina (con il relativo codice di lingua) si aggiunge una "
            "traslitterazione in scrittura latina con i codici di lingua indicati nella tabella E.1 (es. bg-Latn, "
            "el-Latn)."
        ),
        "testo_integrale": (
            "E.1 General rules: When establishing their trusted lists, TLSOs shall use: "
            "• Language codes in lower case and country codes in upper case. "
            "• Language and country codes according to table E.1 with regards to EU MS. "
            "When a Latin script is present (with its proper language code) a transliteration in Latin script "
            "with the related language codes specified in table E.1 is added. "
            "Table E.1 (columns: Short name (source language); Short name (English); Country Code; Language Code; "
            "Notes; Transliteration in Latin script), reconstructed row by row: "
            "Belgique/België: Belgium, BE, fr, de, nl. "
            "България (*): Bulgaria, BG, bg, transliteration in Latin script bg-Latn. "
            "Česká republika: Czech Republic, CZ, cs. "
            "Danmark: Denmark, DK, da. "
            "Deutschland: Germany, DE, de. "
            "Eesti: Estonia, EE, et. "
            "Éire/Ireland: Ireland, IE, ga, en. "
            "Ελλάδα (*): Greece, EL, el, notes: Country code recommended by EU, transliteration in Latin script el-Latn. "
            "España: Spain, ES, es, notes: also Catalan (ca), Basque (eu), Galician (gl). "
            "France: France, FR, fr. "
            "Hrvatska: Croatia, HR, hr. "
            "Italia: Italy, IT, it. "
            "Κύπρος/Kıbrıs (*): Cyprus, CY, el, tr, transliteration in Latin script el-Latn. "
            "Latvija: Latvia, LV, lv. "
            "Lietuva: Lithuania, LT, lt. "
            "Luxembourg: Luxembourg, LU, fr, de, lb. "
            "Magyarország: Hungary, HU, hu. "
            "Malta: Malta, MT, mt, en. "
            "Nederland: Netherlands, NL, nl. "
            "Österreich: Austria, AT, de. "
            "Polska: Poland, PL, pl. "
            "Portugal: Portugal, PT, pt. "
            "România: Romania, RO, ro. "
            "Slovenija: Slovenia, SI, sl. "
            "Slovensko: Slovakia, SK, sk. "
            "Suomi/Finland: Finland, FI, fi, sv. "
            "Sverige: Sweden, SE, sv. "
            "United Kingdom: United Kingdom, UK, en, notes: Country code recommended by EU. "
            "Ísland: Iceland, IS, is. "
            "Liechtenstein: Liechtenstein, LI, de. "
            "Norge/Noreg: Norway, NO, no, nb, nn. "
            "NOTE: (*) Latin transliteration: България = Bulgaria; Ελλάδα = Elláda; Κύπρος = Kýpros."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex E.2 (Multilingual character string)",
        "testo": (
            "La stringa contenuta in un multilingual character string deve soddisfare i requisiti dell'annex N di "
            "ISO/IEC 10646 [5] con le seguenti restrizioni: contenuto come stringa di caratteri dello Universal "
            "Character Set (UCS), codifica UTF-8, nessuna firma per identificare lo UCS, nessuna funzione di "
            "controllo, sequenza di escape o sequenza/stringa di controllo (quindi niente TAB, CR, LF), nessun "
            "carattere di uso privato (E000-F8FF nel Basic Multilingual Plane e piani 0F e 10 del Group 00), "
            "nessun Tag Character (collezione TAGS 3001), solo testo semplice senza elementi di markup o tag "
            "(SGML, HTML, XML, XHTML, RTF, TeX e altri); il contenuto dovrebbe inoltre seguire le regole "
            "semantiche dello Unicode Standard e non dovrebbe usare caratteri combinatori quando il contenuto e' "
            "esprimibile senza."
        ),
        "testo_integrale": (
            "E.2 Multilingual character string: The string contained within a multilingual character string shall "
            "fulfil the requirements of annex N of ISO/IEC 10646 [5] subject to the following restrictions: "
            "1) the content shall be a string of characters from the Universal Character Set (UCS) as defined by "
            "ISO/IEC 10646 [5]; "
            "2) the content shall be UTF-8 encoded; "
            "3) the content shall not include any signature to identify the UCS (see annex H of ISO/IEC 10646 [5]); "
            "4) control functions (ISO/IEC 6429 [13]), escape sequences (ISO/IEC 2022 [14]) and control sequences "
            "or strings shall not be used; therefore control characters such as TAB, CR, LF shall not be present; "
            "5) private-use characters (see clause 10 of ISO/IEC 10646 [5]) from the private use zone (code points "
            "E000 to F8FF) in the Basic Multilingual Plane (BMP) and from the private-use Planes 0F and 10 in "
            "Group 00, shall not be used; "
            "6) Tag Characters (see annex T of ISO/IEC 10646 [5]) shall not to be used: therefore the characters "
            "from the TAGS (3001) collection shall not be used (see annex A of ISO/IEC 10646 [5] for the list of "
            "defined collections); "
            "7) the content shall be plain text without any mark-up elements or tags from languages as SGML, HTML, "
            "XML, XHTML, RTF, TeX and others; "
            "8) the content should follow the semantic rules defined by the Unicode Standard [i.13] (available at "
            "http://www.unicode.org/standard/standard.html) for the corresponding characters; "
            "9) combining characters should not be used if the content can be expressed without them; if there is "
            "the need to use combining characters but it is possible not to use the ones listed in clause B.1 of "
            "ISO/IEC 10646 [5], then that latter set shall not be used. "
            "NOTE: This helps to keep as low as possible the required implementation level (as defined by clause "
            "14 of ISO/IEC 10646 [5]) for parsing applications."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex E.3 (Multilingual pointer)",
        "testo": (
            "Se il contenuto puntato dal multilingual pointer e' testo semplice, deve rispettare i seguenti "
            "requisiti, che esprimono la conformita' all'annex N di ISO/IEC 10646 [5] con restrizioni aggiuntive: "
            "contenuto puntato come stringa di caratteri UCS, codifica UTF-8 (la firma per UTF-8 e' ammessa), "
            "funzioni di controllo, sequenze di escape e sequenze/stringhe di controllo ammesse, nessun carattere "
            "di uso privato (E000-F8FF nel BMP e piani 0F e 10 del Group 00), nessun Tag Character (collezione "
            "TAGS 3001); se il contenuto e' espresso con linguaggi di markup (SGML, HTML, XML, XHTML) i requisiti "
            "del W3C Technical Report #20 dovrebbero essere soddisfatti e puo' essere presente un'indicazione di "
            "lingua; il contenuto dovrebbe seguire le regole semantiche dello Unicode Standard e non dovrebbe "
            "usare caratteri combinatori quando e' esprimibile senza."
        ),
        "testo_integrale": (
            "E.3 Multilingual pointer: If the content pointed by the multilingual pointer is plain text, it shall "
            "meet the following requirements that express the conformity to annex N of ISO/IEC 10646 [5] and add "
            "further restrictions: "
            "1) the pointed content shall be a string of characters from the Universal Character Set (UCS) as "
            "defined by ISO/IEC 10646 [5]; "
            "2) the pointed-to content shall be UTF-8 encoded; "
            "3) the pointed-to content may include the signature for UTF-8 (see annex H of ISO/IEC 10646 [5]) to "
            "identify the UCS; "
            "4) control functions (ISO/IEC 6429 [13]), escape sequences (ISO/IEC 2022 [14]) and control sequences "
            "or strings may be used; "
            "5) private-use characters (see clause 10 of ISO/IEC 10646 [5]) from the private use zone (code points "
            "E000 to F8FF) in the Basic Multilingual Plane (BMP) and from the private-use Planes 0F and 10 in "
            "Group 00, shall not be used; "
            "6) Tag Characters (see annex T of ISO/IEC 10646 [5]) shall not to be used: therefore the characters "
            "from the TAGS (3001) collection shall not be used (see annex A of ISO/IEC 10646 [5] for the list of "
            "defined collections); "
            "7) if the pointed-to content is expressed by means of mark-up languages as SGML, HTML, XML, XHTML "
            "then: a) the requirements described in W3C Technical Report #20 [i.7] should be met; b) a language "
            "indication may be present according to the mechanisms listed in W3C Technical Report #20 [i.7]. "
            "8) the pointed-to content should follow the semantic rules defined by the Unicode Standard [i.13] "
            "(available at http://www.unicode.org/standard/standard.html) for the corresponding characters; "
            "9) combining characters should not be used if the pointed-to content can be expressed without them; "
            "if there is the need to use combining characters but it is possible not to use the ones listed in "
            "clause B.1 of ISO/IEC 10646 [5], then that latter set shall not be used. "
            "NOTE: This helps to keep as low as possible the required implementation level (as defined by clause "
            "14 of ISO/IEC 10646 [5] for parsing applications)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": (
            "Il contenuto puntato dal multilingual pointer e' testo semplice (plain text); per contenuti non plain "
            "text restano applicabili i requisiti generali del documento."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex E.4 (Overall requirements)",
        "testo": (
            "I requisiti del W3C Technical Report #20 [i.7] dovrebbero essere soddisfatti. Per finalita' di "
            "interoperabilita', tutte le applicazioni che fanno il parsing di trusted list devono essere in grado "
            "di memorizzare e gestire tutti i caratteri definiti da ISO/IEC 10646 [5], cosi' che la firma digitale "
            "applicata alla TL sia sempre verificabile qualunque carattere UCS sia usato al suo interno; "
            "l'applicazione di parsing puo' comunque non essere in grado di presentare correttamente tutti i "
            "caratteri."
        ),
        "testo_integrale": (
            "E.4 Overall requirements: The requirements of W3C Technical Report #20 [i.7] should be met. For "
            "interoperability purposes, all applications parsing TLs shall be able to store and manage all "
            "characters defined by ISO/IEC 10646 [5]. This way the digital signature applied to the TL can be "
            "always verified, whatever UCS characters are used within the TL. However the parsing application may "
            "not be able to correctly present all characters. NOTE: Developers of TL parsing applications are "
            "advised that if their application does not support some of these characters, the application should "
            "give notice to the user about possible incorrect representation of the content of multilingual "
            "fields; the precise behaviour of the application while presenting unsupported characters is left to "
            "developers [i.7]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex G.1 (Change of scheme administrative information)",
        "testo": (
            "La categoria comprende ogni modifica alle informazioni concernenti lo schema incorporate nella TL "
            "(tra cui, ad esempio, cambio degli indirizzi dello schema, revisioni dei criteri di accettazione, "
            "politica dello schema). Quando tali modifiche si verificano e sono modifiche materiali alle "
            "informazioni incluse nella TL, la TL deve essere riemessa. Se le modifiche derivano da un cambio di "
            "proprieta' dell'entita' che gestisce lo schema, lo schema dovrebbe continuare a operare con le "
            "modifiche relative alle informazioni sul Scheme Operator e con la TL riemessa."
        ),
        "testo_integrale": (
            "G.1 Change of scheme administrative information: This category includes any changes to information "
            "concerning the scheme and which is embedded within the TL. Such changes could include, inter alia, "
            "change of scheme addresses, revisions to acceptance criteria, scheme policy. When these changes occur "
            "and are material changes to information included in the TL, the TL shall be re-issued. NOTE: If there "
            "are material changes to information directly referenced through the TL but the reference itself does "
            "not change then there will be no need to amend the TL. If the changes were the result of a change of "
            "ownership of the entity operating the scheme then the scheme should continue to operate with changes "
            "with regards to information related to the Scheme Operator and the TL being re-issued."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": (
            "In caso di modifiche materiali alle informazioni dello schema incluse nella TL (o di cambio di "
            "proprieta' dell'entita' che gestisce lo schema)."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex G.3 (Change of trust service status)",
        "testo": (
            "Queste modifiche sono quelle che incidono direttamente sull'inclusione o sullo stato riportato di un "
            "servizio fiduciario nella TL (e possibilmente anche sulle informazioni relative al suo fornitore) e "
            "sulla natura corrente o storica delle informazioni (es. introduzione di un nuovo TSP e servizio; "
            "revoca di un servizio). Quando si verifica una tale modifica la TL deve essere riemessa, con il "
            "precedente stato corrente che diventa lo stato storico piu' recente e lo stato corrente aggiornato "
            "per riflettere la situazione. Il servizio che di fatto cessa l'attivita' deve avere il \"Service "
            "current status\" (clausola 5.5.4) revisionato al significato di operazioni cessate o ritirate, con le "
            "informazioni sul precedente stato collocate nella \"History information\" (clausola 5.5.10) della TL: "
            "tali informazioni devono poi essere conservate per il periodo di conservazione pubblicato e nessuna "
            "\"Historical information\" di un servizio deve essere scartata."
        ),
        "testo_integrale": (
            "G.3 Change of trust service status: These changes are those directly affecting the inclusion or "
            "reported status of any trust service within the TL (and possibly also information concerning their "
            "provider) and whether the information is current or historical (e.g. the introduction of a new TSP "
            "and service; the revocation of a service). When any such change occurs the TL shall be re-issued with "
            "the previous current status becoming the most recent historical status and current status being "
            "amended to reflect the situation. The service which is effectively stopping should have its \"Service "
            "current status\" (see clause 5.5.4) revised to meaning \"ceased\" operations or \"withdrawn\" status "
            "and the previous status information placed into the \"History information\" (see clause 5.5.10) of "
            "the TL. This shall then be retained for the published retention period (since there may be "
            "requirements to check on services rendered during its period of activity). No service's \"Historical "
            "information\" shall be discarded."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": (
            "In caso di variazione dell'inclusione o dello stato riportato di un servizio fiduciario nella TL (o "
            "della cessazione/revoca di un servizio)."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex G.4 (Change in trust service digital identity)",
        "testo": (
            "Quando un servizio cambia la propria \"Service digital identity\" (clausola 5.5.3): in caso di nuova "
            "chiave pubblica (es. ri-branding o rinnovo dei dati digitali associati per ragioni di sicurezza), il "
            "servizio relativo alla nuova identita' digitale deve essere aggiunto alla TL come nuova voce di "
            "servizio e, essendo un nuovo servizio, la \"History information\" e' assente; in caso di nuovo "
            "certificato per la stessa chiave pubblica si applicano le regole della clausola 5.5.3, per cui due o "
            "piu' certificati con la stessa chiave pubblica non sono considerati due identificatori separati ma "
            "due rappresentazioni dello stesso identificatore, purche' abbiano identici valori di X.509 Subject "
            "Name; quando il nuovo certificato e' ammissibile puo' essere aggiunto all'insieme esistente di "
            "rappresentazioni della stessa chiave pubblica, senza generare alcuna istanza di service history."
        ),
        "testo_integrale": (
            "G.4 Change in trust service digital identity: Where a service changes its \"Service digital identity\" "
            "(see clause 5.5.3): "
            "• In the case of a new public key (e.g. as a result of a re-branding or a renewal of associated "
            "digital data for security reasons), the service related to the new digital identity (public key) "
            "shall be added in the TL as a new service entry. As new service, the \"History information\" is "
            "absent. "
            "• In the case of a new certificate for the same public key, rules in clause 5.5.3 apply. Providing "
            "two or more certificates with the same public key is not regarded as two separate identifiers, but "
            "two representations of the same identifier provided they both have identical X.509 Subject Name "
            "values. When the new certificate is eligible, it may be added to the existing set of representations "
            "for the same public key; no service history instance shall be generated."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": (
            "Quando un servizio cambia la propria \"Service digital identity\" (nuova chiave pubblica o nuovo "
            "certificato per la stessa chiave pubblica)."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex G.5 (Amendment response times)",
        "testo": (
            "Le modifiche a qualsiasi informazione della TL devono essere fornite in modo tempestivo, non oltre 24 "
            "ore. In particolare, una volta efficace la decisione di cambiare lo stato di una certificazione o di "
            "un servizio fiduciario elencato, la modifica corrispondente dovrebbe essere implementata e la TL "
            "riemessa in meno di quattro ore lavorative."
        ),
        "testo_integrale": (
            "G.5 Amendment response times: Changes to any TL information shall be provided in a timely fashion, "
            "not exceeding 24 hours. In particular, once the decision to change the status of a listed "
            "certification or trust service is effective, the corresponding change should be implemented and the "
            "TL re-issued in less than four working hours."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex G.6 (On-going verification of authenticity)",
        "testo": (
            "La frequenza con cui le informazioni di una TL cambiano e' probabilmente bassa, il che potrebbe dare "
            "a un hacker determinato tempo sufficiente per replicare e sostituire tutte le istanze di una TL, se "
            "riuscisse a sostituire tutti gli esemplari della TL stessa e una PKC surrogata per lo scheme "
            "operator. A questo lo scheme operator dovrebbe proteggersi effettuando frequenti verifiche della "
            "propria TL e di tutte le sue replicazioni autorizzate e riconosciute; inoltre la riemissione "
            "regolare della TL, anche in assenza di cambi di stato, assicura che almeno il valore della firma "
            "cambi periodicamente."
        ),
        "testo_integrale": (
            "G.6 On-going verification of authenticity: The frequency at which information within a TL will change "
            "is likely to be low. This could give a determined hacker sufficient time to replicate and replace all "
            "instances of a TL, IF they were able to replace all examples of the TL itself and a surrogate PKC for "
            "the TL scheme operator. This should be protected against by the scheme operator itself making "
            "frequent verification of its own TL and all authorized and recognized replications of it. In "
            "addition, the regular re-issuing of the TL, even when there is no change to any statuses within it, "
            "will also ensure that, at the least, the signature value changes periodically."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": None,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex G.7 (User reference to TL)",
        "testo": (
            "Gli scheme operator dovrebbero contribuire offrendo servizi aggiuntivi che notifichino quando una "
            "nuova TL e' emessa, oppure garantendo una riemissione frequente della TL a una frequenza che puo' "
            "comportare numerose riemissioni senza variazione dello stato dei servizi. I meccanismi previsti per "
            "avere piu' copie di TL esistenti contemporaneamente sono pero' pensati per il basso tasso di "
            "variazione delle informazioni e possono non essere adatti a riemissioni frequenti."
        ),
        "testo_integrale": (
            "G.7 User reference to TL: Scheme operators should assist in this by offering additional services to "
            "notify when a new TL is issued, or to guarantee frequent re-issue of a TL at a frequency which may "
            "mean numerous re-issues without change of any services' status. However, the mechanisms proposed for "
            "having multiple copies of TLs existing contemporaneously are designed to cater for the low rate of "
            "information change already discussed, and these may not be suitable for frequent TL re-issue."
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
        "riferimento": "Annex G.8 (TL size)",
        "testo": (
            "Il documento prevede numerosi campi in cui lo scheme operator puo' scegliere di fornire testo in "
            "linguaggio naturale invece di un URI o di altro riferimento a una fonte informativa; l'inclusione di "
            "grandi quantita' di testo ha un'influenza diretta sui tempi di scaricamento e di parsing, tanto piu' "
            "se riguarda le descrizioni dei servizi in uno schema con molti servizi fiduciari elencati. Gli "
            "implementatori dovrebbero quindi sfruttare l'opportunita' di usare URI e limitare il testo "
            "incorporato per quanto ragionevole, tenendo conto della dimensione complessiva della TL e della banda "
            "e capacita' di memorizzazione disponibili per l'utente tipico della loro TL; il riferimento ad altri "
            "documenti consente inoltre di avvalersi di opzioni di presentazione piu' sofisticate, abilitate da "
            "formati come PDF."
        ),
        "testo_integrale": (
            "G.8 TL size: The present document provides a number of fields in which the scheme operator may choose "
            "to provide actual natural language text in preference to a URI or other reference to a source of "
            "information. Clearly the inclusion of large quantities of text will have a direct influence on "
            "download and parsing times, this especially so if e.g. it relates to the descriptions of services, "
            "and the scheme has a large number of trust services listed. Implementers should therefore take "
            "advantage of the opportunity to use URIs and limit embedded text as much as is reasonable, accounting "
            "for the overall size of the TL and the available bandwidth and storage capacities of the typical user "
            "of their TL. Referencing other documents also allows advantage to be taken of more sophisticated "
            "presentation options which formats such as PDF and other formats enable."
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
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "Annex F (TL manual/auto field usage)",
        "testo": (
            "L'annesso F, informativo, elenca nella tabella F.1 tutti i campi definiti per la TL e indica, per "
            "ciascuno, se il contenuto dovrebbe essere reso disponibile agli utenti nella presentazione in forma "
            "leggibile (colonna \"Human-readable?\") e se il campo e' considerato essenziale per un parsing "
            "automatico efficace (colonna \"Machine-processable?\"), fermo restando che tutti i campi sono "
            "accessibili attraverso un processo automatizzato. Benche' l'annesso sia informativo, agli "
            "implementatori e' vivamente raccomandato di soddisfare le indicazioni che fornisce, per offrire agli "
            "utenti informazioni sulle TL in modo coerente. La tabella copre l'identificazione (TSL tag), le "
            "informazioni di schema, di TSP, di servizio, di servizio storico e di firma della TSL, con i campi "
            "di estensione resi disponibili solo dove riconosciuti (e significativi)."
        ),
        "testo_integrale": (
            "Annex F (informative): TL manual/auto field usage: Table F.1 lists all fields defined for the TL and "
            "indicates whether the field contents should be made available to users when presenting the TL in a "
            "human-readable form (column 2) or whether the field is considered to be essential for effective "
            "automatic parsing (column 3), noting that all fields will be accessible through an automated process. "
            "Although this annex is informative implementers are strongly recommended to satisfy the guidance "
            "which it provides, in order to provide users with information about TLs in a consistent manner. "
            "Table F.1 (columns: Field name; Human-readable?; Machine-processable?) reconstructed row by row, with "
            "the original group headings: "
            "Identification Tag: TSL tag: Human-readable: no; Machine-processable: yes. "
            "Scheme information: TSL version identifier: Human-readable: yes; Machine-processable: yes. "
            "TSL sequence number: Human-readable: yes; Machine-processable: yes. "
            "TSL type: Human-readable: yes; Machine-processable: yes. "
            "Scheme operator name: Human-readable: yes; Machine-processable: no. "
            "Scheme operator address: Human-readable: yes; Machine-processable: no. "
            "Scheme name: Human-readable: yes; Machine-processable: no. "
            "Scheme information URI: Human-readable: yes; Machine-processable: yes. "
            "Status determination approach: Human-readable: yes; Machine-processable: yes. "
            "Scheme type/community/rules: Human-readable: yes; Machine-processable: yes. "
            "Scheme territory: Human-readable: yes; Machine-processable: yes. "
            "TSL policy/legal notice: Human-readable: yes; Machine-processable: yes. "
            "Historical information period: Human-readable: yes; Machine-processable: yes. "
            "Pointers to other TSLs: Human-readable: yes; Machine-processable: yes. "
            "List issue date and time: Human-readable: yes; Machine-processable: yes. "
            "Next update: Human-readable: yes; Machine-processable: yes. "
            "Scheme extensions: Human-readable: where recognized and meaningful; Machine-processable: where "
            "recognized. "
            "TSP information: TSP name: Human-readable: yes; Machine-processable: no. "
            "TSP trade name: Human-readable: yes; Machine-processable: no. "
            "TSP address: Human-readable: yes; Machine-processable: no. "
            "TSP information URI: Human-readable: yes; Machine-processable: yes. "
            "TSP information extensions: Human-readable: where recognized and meaningful; Machine-processable: "
            "where recognized. "
            "Service information: Service type identifier: Human-readable: yes; Machine-processable: yes. "
            "Service name: Human-readable: yes; Machine-processable: no. "
            "Service digital identity: Human-readable: yes; Machine-processable: yes. "
            "Service current status: Human-readable: yes; Machine-processable: yes. "
            "Current status starting date and time: Human-readable: yes; Machine-processable: yes. "
            "Scheme service definition URI: Human-readable: yes; Machine-processable: yes. "
            "Service supply points: Human-readable: yes; Machine-processable: yes. "
            "TSP service definition URI: Human-readable: yes; Machine-processable: yes. "
            "Service information extensions: Human-readable: where recognized and meaningful; "
            "Machine-processable: where recognized. "
            "Historical service information: Service type identifier: Human-readable: yes; Machine-processable: "
            "yes. "
            "Service name: Human-readable: yes; Machine-processable: no. "
            "Service digital identity: Human-readable: yes; Machine-processable: yes. "
            "Service previous status: Human-readable: yes; Machine-processable: yes. "
            "Previous status starting date and time: Human-readable: yes; Machine-processable: yes. "
            "Service information extensions: Human-readable: where recognized and meaningful; "
            "Machine-processable: where recognized. "
            "TSL signature information: Scheme identification: Human-readable: no; Machine-processable: yes. "
            "Textual certificate details, time and date of signing: Human-readable: yes; Machine-processable: yes. "
            "Cryptographic data: Human-readable: no; Machine-processable: yes."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "oggetti_giuridici": ["altro"],
    },
    {
        "riferimento": "Annex G.0 (General)",
        "testo": (
            "Alla fornitura di revisioni delle informazioni di una trusted list si applicano criteri specifici; "
            "tali revisioni ricadono nelle categorie declinate nelle clausole dell'annesso (cambio delle "
            "informazioni amministrative dello schema, identificazione del trust service, cambio di stato del "
            "servizio, cambio di identita' digitale del servizio, tempi di risposta alle modifiche, verifica "
            "continua dell'autenticita', riferimento dell'utente alla TL, dimensione della TL)."
        ),
        "testo_integrale": (
            "G.0 General: Specific criteria for the provision of revisions to TL information apply. These "
            "revisions will fall into the following categories."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "oggetti_giuridici": ["altro"],
    },
    {
        "riferimento": "Annex G.2 (Trust-service identification)",
        "testo": (
            "Quando uno scheme operator aggiunge un servizio fiduciario a una TL, per gli utenti della TL e' "
            "importante poter identificare senza ambiguita' la definizione dello stato di quel servizio. Nome e "
            "indirizzo possono essere altamente rilevanti e quindi molto importanti, ma il campo dell'identita' "
            "digitale e' l'unica opzione in grado di fornire un'identificazione sicura del servizio fiduciario e "
            "dei token che esso fornisce."
        ),
        "testo_integrale": (
            "G.2 Trust-service identification: Whenever a scheme operator adds trust service to a TL, it is "
            "important to users of the TL to be able to unambiguously identify that service's status definition. "
            "While name and address may be highly relevant and therefore very important, the digital "
            "identity-field is the only option that can provide secure identification of the trust service and "
            "tokens which it supplies."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "oggetti_giuridici": ["altro"],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Annex E.1 (General rules)",
    "Annex E.2 (Multilingual character string)",
    "Annex E.3 (Multilingual pointer)",
    "Annex E.4 (Overall requirements)",
    "Annex F (TL manual/auto field usage)",
    "Annex G.0 (General)",
    "Annex G.1 (Change of scheme administrative information)",
    "Annex G.2 (Trust-service identification)",
    "Annex G.3 (Change of trust service status)",
    "Annex G.4 (Change in trust service digital identity)",
    "Annex G.5 (Amendment response times)",
    "Annex G.6 (On-going verification of authenticity)",
    "Annex G.7 (User reference to TL)",
    "Annex G.8 (TL size)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Uniche relazioni interne derivabili da rinvii testuali puntuali in questo capitolo:
# G.3 rinvia a clause 5.5.4 ("Service current status") e clause 5.5.10 ("History
# information"); G.4 rinvia a clause 5.5.3 ("Service digital identity"). Sono tutti
# richiami a nodi di altri capitoli della stessa Fonte, risolti dal registro al merge
# (stringhe di riferimento concordate con gli autori di cap03 e cap04). E.1 cita la
# propria tabella E.1 e G.0 annuncia le proprie sottoclausole: nessun nodo separato da
# collegare. Tutte le altre citazioni del capitolo sono esterne (ISO/IEC 10646 [5],
# ISO/IEC 6429 [13], ISO/IEC 2022 [14], W3C Technical Report #20 [i.7], Unicode
# Standard [i.13]) e non generano relazioni: il collegamento cross-fonte e' demandato
# alla Fase 6 della sessione principale (ADR-0009).
RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "Annex G.3 (Change of trust service status)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.4 (Service current status)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex G.3 (Change of trust service status)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.10 (Service history)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex G.4 (Change in trust service digital identity)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (Service digital identity)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_completezza_testo_integrale, verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    verifica_completezza_testo_integrale([sys.modules[__name__]])
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
