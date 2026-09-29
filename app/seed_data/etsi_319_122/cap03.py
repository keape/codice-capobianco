"""Estrazione granulare ETSI EN 319 122-1 V1.3.1 (2023-06) — Capitolo 3: clausola 5
(Attribute semantics and syntax: 5.1 attributi CMS di base, 5.2 attributi CAdES di
base, 5.3 marca temporale di firma, 5.4 attributi per i dati di validazione, 5.5
attributi per la disponibilita' a lungo termine del materiale di validazione).

Fonte del blocco B (famiglia AdES del lotto 2); la numerazione definitiva della fonte
e' cablata dalla sessione principale in app/seed.py — questo modulo NON tocca seed.py,
non importa nulla e non legge file: e' puro dato.

Provenienza del testo
---------------------
- testo ufficiale: ETSI EN 319 122-1 V1.3.1 (2023-06), "Electronic Signatures and
  Infrastructures (ESI); CAdES digital signatures; Part 1: Building blocks and CAdES
  baseline signatures".
- file di capitolo: app/.source_cache/etsi_319_122/cap03.txt (1.184 righe), porzione
  della conversione PDF (pdftotext -layout) di app/.source_cache/etsi_319_122/raw.pdf.
- metadati da app/.source_cache/etsi_319_122/provenance.json: url
  https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf,
  versione "01.03.01_60", data_fetch 2026-09-29T12:56:34Z, sha256_raw_pdf
  e99e76e519d9bd8e1410775bccedb1a588021e5e7c705c9fcc1f91c6a6227c21.
- perimetro: la sola clausola 5 (5.1, 5.2, 5.3, 5.4, 5.5), dal titolo "5 Attribute
  semantics and syntax" all'ultima riga della pagina 32. Confine di split pulito:
  cap04.txt inizia con "6 CAdES baseline signatures" e cap03.txt non contiene code
  della clausola 4 (che sta in cap02.txt), quindi nessun testo del capitolo resta
  fuori dal file letto.

Criterio di granularita' (ADR-0007, nessun discrimine di rilevanza)
------------------------------------------------------------------
Granularita' alla sottoclausta/attributo: clausola 5 e' la parte dello standard che
definisce semantica e sintassi di ciascun attributo CAdES, e ogni attributo ha una
propria sottoclausta numerata (5.1.1, 5.1.2, 5.2.1, 5.2.2.1 ... 5.5.3), delimitata
dalle intestazioni "Semantics" e "Syntax" e portante testo normativo proprio. Uno
standard che numera i requisiti con id propri (GEN-x.y-z) viene censito all'id di
requisito; ETSI EN 319 122-1 non numera i requisiti in questo capitolo, quindi
l'unita' di prescrizione e' la sottoclausta/attributo. Bilancio: 29 item di indice ->
29 righe, 1:1.

Intestazioni di solo raggruppamento, senza testo proprio: non generano nodo ne' item
di indice (stesso criterio gia' applicato a ETSI EN 319 422 e alle altre fonti ETSI
gia' censite). Sono: "5 Attribute semantics and syntax", "5.1 CMS defined basic signed
attributes", "5.2 Basic attributes for CAdES signatures", "5.2.2 Signing certificate
reference attributes", "5.2.4 Attributes for identifying the signed data type",
"5.2.6 Incorporating attributes of the signer", "5.2.9 The signature-policy-identifier
attribute and the SigPolicyQualifierInfo type", "5.4 Attributes for validation data
values", "5.4.2 OCSP responses", "5.5 Attributes for long term availability and
integrity of validation material": ciascuna e' seguita immediatamente dalla prima
sottoclausta (rispettivamente 5.1, 5.2, 5.2.2.1, 5.2.4.1, 5.2.6.1, 5.2.9.1, 5.4.1,
5.4.2.1, 5.5.1) senza una riga di testo proprio da assorbire.

Criterio Obbligo/Principio applicato in questo capitolo
------------------------------------------------------
Ogni sottoclausta che contiene almeno un requisito prescrittivo (shall / should / "is
required" / "shall not be used" / "shall be as defined in ...") e' un Obbligo: la
clausola 5 vincola il contenuto e la codifica di cio' che finisce nella firma CAdES
(attributo presente, codifica ammessa, campo valorizzato, campo vietato), quindi
prescrive un comportamento a un soggetto identificabile (il sistema di creazione della
firma, il sistema di validazione, la parte che incorpora dati di validazione). Solo le
sottoclauste puramente dichiarative, prive di qualunque requisito, sono Principi: in
questo capitolo sono le due Introduction (5.4.1 e 5.5.1), che descrivono dove e come
i dati di validazione vengono incorporati senza imporre nulla. Le sottoclausole il cui
unico contenuto e' un rinvio per valore a un'altra specifica ("shall be as defined in
CMS/RFC/ESS") restano Obblighi con tipo_obbligo "tecnico/sicurezza": il rinvio e'
prescrittivo (fissa la sola codifica ammessa), non una mera citazione bibliografica.
Nessun Obbligo di questo capitolo e' "organizzativo", "informativo/trasparenza",
"procedurale", "di conservazione" o "sanzionatorio": sono tutti requisiti di formato e
codifica -> "tecnico/sicurezza".

soggetti/oggetti_giuridici valorizzati solo dove il testo nomina davvero il soggetto:
"the signer" / "signature creation applications" -> 'Utente/titolare' (ruolo obbligato);
"signature validation applications" -> 'Terza parte' (ruolo obbligato). Dove il testo
non nomina alcun soggetto (la maggior parte degli attributi: "the X attribute shall
contain ...") la riga resta senza soggetti, come ammesso dal contratto di lib.py.

Decisioni di modellazione, riga per riga
----------------------------------------
- clausola 5.1.1 (The content-type attribute) -> Obbligo "tecnico/sicurezza", senza
  soggetti. Semantica dichiarativa ("is a signed attribute", "indicates the type of the
  signed content") + Syntax prescrittiva (conforme a CMS, IETF RFC 5652 clausola 11.1);
  la NOTE ufficiale (valore di ContentType = eContentType di EncapsulatedContentInfo) e'
  contenuto interpretativo, quindi assorbita in testo_integrale.
- clausola 5.1.2 (The message-digest attribute) -> Obbligo "tecnico/sicurezza", senza
  soggetti. Attributo e processo di calcolo del digest definiti da CMS (11.2 e 5.4).
- clausola 5.2.1 (The signing-time attribute) -> Obbligo "tecnico/sicurezza", soggetto
  'Utente/titolare' obbligato: il testo nomina il firmatario ("the time at which the
  signer claims to having performed the signing process").
- clausola 5.2.2.1 (General requirements) -> Obbligo "tecnico/sicurezza", senza
  soggetti. Requisiti comuni agli attributi di riferimento al certificato (un
  riferimento al certificato di firma, valore di digest per ogni certificato); NOTE 1 e
  2 (ruolo della signature validation policy, semantica del primo certificato nella
  sequenza) assorbite perche' interpretano il requisito.
- clausola 5.2.2.2 (ESS signing-certificate attribute) -> Obbligo "tecnico/sicurezza",
  senza soggetti. Attributo SHA-1 conforme a ESS (IETF RFC 2634, clausola 5.4) piu' il
  divieto esplicito "The policies field shall not be used."; NOTE 1 e 2 assorbite
  (calcolo di certHash, valore solo indicativo di IssuerSerial).
- clausola 5.2.2.3 (ESS signing-certificate-v2 attribute) -> Obbligo
  "tecnico/sicurezza", senza soggetti. Speculare alla precedente con RFC 5035, clausola
  4 e hash diverso da SHA-1; stesso divieto sul campo policies.
- clausola 5.2.3 (The commitment-type-indication attribute) -> Obbligo
  "tecnico/sicurezza", soggetto 'Utente/titolare' obbligato (il commitment e' "made by
  the signer when signing the data object"). NOTE 1 e 2 assorbite: la prima descrive le
  due specie di commitment type, la seconda rinvia a ETSI TS 119 172-1 per gli
  identificatori predefiniti (rinvio di contenuto, tenuto letteralmente).
- clausola 5.2.4.1 (The content-hints attribute) -> Obbligo "tecnico/sicurezza", senza
  soggetti. Include il divieto d'uso in controfirma, il rinvio a ESS (IETF RFC 2634,
  clausole 1.3.4 e 2.9) e le due liste di requisiti sul contentType/contentDescription
  (formato preciso dei dati da presentare all'utente; formato definito da tipi MIME).
- clausola 5.2.4.2 (The mime-type attribute) -> Obbligo "tecnico/sicurezza", senza
  soggetti. NOTE 1 (somiglianza con contentDescription) e NOTE 2 (esempio in annex E)
  assorbite: la prima delimita l'ambito dell'attributo, la seconda sono paratesto di
  rinvio mantenuto per completezza verbatim della sottoclausta.
- clausola 5.2.5 (The signer-location attribute) -> Obbligo "tecnico/sicurezza",
  soggetto 'Utente/titolare' obbligato (indirizzo "associated with the signer"). I due
  requisiti "should" sul contenuto di countryName/localityName (X.520, clausole 6.3.1 e
  6.3.2) restano nello stesso nodo: non sono sottoclausole numerate a se'.
- clausola 5.2.6.1 (The signer-attributes-v2 attribute) -> Obbligo "tecnico/sicurezza",
  soggetto 'Utente/titolare' obbligato (attributi "claimed by the signer"). Include
  l'intero blocco ASN.1 copiato in clausola, i requisiti su claimedAttributes /
  certifiedAttributes / signedAssertions, il divieto "Empty signer-attributes-v2 shall
  not be created." e le quattro NOTE ufficiali. La NOTE 4 ("A possible content of such
  a qualifier can be a signed SAML assertion, see of SAML [18]") e' riportata
  letteralmente, compreso l'evidente refuso "see of SAML" del testo ufficiale, che non
  va emendato in un modulo dati.
- clausola 5.2.6.2 (claimed-SAML-assertion) -> Obbligo "tecnico/sicurezza", senza
  soggetti. Attributo rivendicato che deve includere una SAML assertion, utilizzabile
  solo nel campo claimedAttributes di signer-attributes-v2.
- clausola 5.2.6.3 (signed-SAML-assertion) -> Obbligo "tecnico/sicurezza", senza
  soggetti. Sottoclausta senza intestazioni Semantics/Syntax nel testo ufficiale, con
  contenuto proprio (OID, tipo OCTET STRING, ASN.1) -> nodo autonomo.
- clausola 5.2.7 (The countersignature attribute) -> Obbligo "tecnico/sicurezza", senza
  soggetti. La controfirma e' apposta da una parte diversa dal firmatario, ma il testo
  non nomina il soggetto ("shall include a counter signature on the CAdES signature
  where this attribute is included"): per la regola "soggetti solo se il testo li nomina"
  la riga resta senza soggetti (dubbio di classificazione residuo, vedi sotto).
- clausola 5.2.8 (The content-time-stamp attribute) -> Obbligo "tecnico/sicurezza",
  senza soggetti: il testo nomina il token di marca temporale, non la TSU che lo emette.
  Include i requisiti su messageImprint (hash di eContent per firma attached, dati
  esterni per firma detached, calcolato sui dati grezzi senza tag e length ASN.1).
- clausola 5.2.9.1 (The signature-policy-identifier attribute) -> Obbligo
  "tecnico/sicurezza", soggetti 'Utente/titolare' obbligato (le "Signature creation
  applications that generate a zero-hash value") e 'Terza parte' obbligato (le
  "signature validation applications" che devono interpretare il valore zero-hash). La
  sottoclausta e' ampia (ASN.1, regole sul valore zero-hash, tre NOTE) e include il
  rinvio interno alla clausola 5.2.9.2 e l'obbligo di usare il qualificatore
  sp-doc-specification quando la specifica non e' chiara dal contesto.
- clausola 5.2.9.2 (The SigPolicyQualifierInfo type) -> Obbligo "tecnico/sicurezza",
  senza soggetti. Semantica dichiarativa (il tipo "may be used to further qualify", con
  i tre qualificatori SPuri/SPUserNotice/SPDocSpecification) ma Syntax fortemente
  prescrittiva (ASN.1 di clausola + ASN.1 dei qualificatori, requisiti su SPuri,
  explicitText, noticeRef, SPDocSpecification e sulle due scelte oid/uri): nodo unico
  Obbligo, non Principio. NOTE 1, 2 e 3 assorbite (delimitano il valore dei qualificatori).
- clausola 5.2.10 (The signature-policy-store attribute) -> Obbligo
  "tecnico/sicurezza", senza soggetti: la NOTE 2 nomina "the entity adding the signature
  policy into the signature-policy-store", ma e' una descrizione generica del soggetto
  responsabile, non una delle categorie censite. Include il rinvio interno alla clausola
  5.2.9.2 per SPDocSpecification e la NOTE 3 sull'assenza di protezione crittografica
  dell'attributo (unsigned).
- clausola 5.2.11 (The content-reference attribute) -> Obbligo "tecnico/sicurezza",
  senza soggetti. Attributo firmato conforme a ESS (IETF RFC 2634, clausole 1.3.4 e
  2.11) che collega un SignedData a un altro; la frase finale sul suo uso (risposta a un
  messaggio precedente, incorporazione per riferimento) resta nello stesso nodo.
- clausola 5.2.12 (The content-identifier attribute) -> Obbligo "tecnico/sicurezza",
  senza soggetti. Attributo firmato con valore ContentIdentifier di ESS (IETF RFC 2634,
  clausole 1.3.4 e 2.7) e requisito "should" sul contenuto minimo (informazioni
  identificative dell'utente, GeneralizedTime, numero casuale); il testo nomina l'utente
  solo come esempio di contenuto, non come soggetto obbligato.
- clausola 5.2.13 (The cms-algorithm-protection attribute) -> Obbligo
  "tecnico/sicurezza", senza soggetti. Attributo firmato conforme a IETF RFC 6211 (il
  testo ufficiale porta la parentesi tonda sbilanciata "[19])", riportata verbatim).
- clausola 5.3 (The signature-time-stamp attribute) -> Obbligo "tecnico/sicurezza",
  soggetto 'Utente/titolare' obbligato (la marca temporale e' "computed on the digital
  signature value for a specific signer"). La NOTE finale (firme multiple: una marca per
  ogni firmatario, oppure solo per alcuni) e' contenuto interpretativo, assorbita.
- clausola 5.4.1 (Introduction) -> PRINCIPIO "altro", senza oggetti giuridici: due frasi
  dichiarative che descrivono dove incorporare i dati di validazione mancanti e rinviano
  a 5.5 e A.1, senza alcun requisito e senza soggetto obbligato.
- clausola 5.4.2.1 (OCSP response types) -> Obbligo "tecnico/sicurezza", senza soggetti:
  un OCSP response va incorporato con la codifica OCSPResponse o BasicOCSPResponse
  (clausola 4.8.2), con preferenza ("should") per OCSPResponse.
- clausola 5.4.2.2 (OCSP responses within RevocationInfoChoices) -> Obbligo
  "tecnico/sicurezza", senza soggetti: tipo RevocationInfoChoices (clausola 4.8.2),
  inclusione delle OCSP response nel campo other e codifica OCSPResponse di IETF RFC 5940.
- clausola 5.4.3 (CRLs) -> Obbligo "tecnico/sicurezza", senza soggetti: sottoclausta di
  un solo periodo, rinvio prescrittivo alle CRL di IETF RFC 5280.
- clausola 5.5.1 (Introduction) -> PRINCIPIO "altro", senza oggetti giuridici: dichiara
  che il documento specifica un attributo archive-time-stamp che usa ats-hash-index-v3
  (entrambi unsigned) e che cosa l'archive-time-stamp protegge. Nessun requisito.
- clausola 5.5.2 (The ats-hash-index-v3 attribute) -> Obbligo "tecnico/sicurezza",
  senza soggetti. La sottoclausta piu' densa del capitolo: semantica (cos'e' l'impronta
  non ambigua dei componenti essenziali), le regole di validazione dell'ATSv3 a partire
  dall'ats-hash-index-v3 con i tre casi di invalidita' (certificatesHashIndex,
  crlsHashIndex, unsignedAttrValuesHashIndex), sintassi (un solo componente
  AttributeValue, DER, ATSHashIndexV3, OID) e i requisiti per campo, piu' le NOTE 1-7.
- clausola 5.5.3 (The archive-time-stamp-v3 attribute) -> Obbligo "tecnico/sicurezza",
  senza soggetti. Include il processo di calcolo del message imprint (quattro punti
  numerati 1)-4) del testo ufficiale), l'obbligo di includere il singolo
  ats-hash-index-v3, l'estensione del SignedData con i dati di validazione mancanti, le
  due strategie di inclusione dei dati di validazione (con le rispettive alternative),
  le regole di codifica DER in augmenting, le NOTE 1-7 e i due rinvii interni. Il testo
  ufficiale indica come OID dell'attributo id-aa-signatureTimeStampToken (lo stesso
  della clausola 5.3) mentre l'ASN.1 copiato in clausola definisce
  id-aa-ets-archiveTimestampV3: e' un refuso del testo ufficiale, riportato verbatim e
  NON corretto (compito del censimento non e' emendare lo standard).

Anomalie di conversione PDF -> testo normalizzate (non contenuto normativo)
--------------------------------------------------------------------------
- pie' di pagina delle pagine 15-32 ("ETSI" e "15 ETSI EN 319 122-1 V1.3.1
  (2023-06)"): rimosse, sono paratesto di impaginazione intercalato alle
  sottoclausole dalle interruzioni di pagina;
- righe spezzate a meta' frase: ricucite in un'unica riga. Quando il trattino a fine
  riga appartiene alla parola (non e' una sillabazione da rimuovere) la parola e'
  ricomposta mantenendo il trattino: "the value of the attribute content-\ntype" ->
  "content-type" (5.1.1 NOTE), "the signer-attributes-\nv2 attribute" ->
  "the signer-attributes-v2 attribute" (5.2.6.2), "independent archive time-\nstamps"
  -> "archive time-stamps" (5.5.3 NOTE 4), "a long-term-\nvalidation attribute" ->
  "long-term-validation attribute" (5.5.3 NOTE 6), "electronic-signature-standard"
  (OID), "X509/SignedData/TimeStampToken" spezzati a meta' parola;
- intestazione di clausola/sottoclausta: NON ripetuta dentro testo_integrale (il
  riferimento del nodo la porta gia'). Nei casi in cui la conversione PDF incolla
  l'intestazione alla riga di testo immediatamente successiva senza riga vuota in
  mezzo (5.4.1 Introduction, 5.4.2.1 OCSP response types, 5.5.1 Introduction) la
  prima frase e' comunque riportata per intero, senza il numero e il titolo di
  clausola;
- elenchi puntati: il carattere privato \uf0a7 usato da pdftotext per i pallini di
  secondo livello e' stato normalizzato al pallino "•" (stessa normalizzazione gia'
  applicata a ETSI TS 119 432, cap04), con i sottopunti resi con "-" e l'indentazione
  ridotta, essendo i trattini di continuazione di una stessa voce di elenco,
  ricomposti nella voce;
- "SignedSAMLAssertion ::= OCTET          STRING": spaziatura multipla di rendering
  ridotta a una sola, essendo whitespace non significativo in ASN.1;
- i blocchi ASN.1 (OID, SEQUENCE, CLASS/WITH SYNTAX) sono riportati per intero e con
  l'indentazione del testo; i due ASN.1 copiati in clausola nella 5.5.3 e nella 5.5.2
  restano separati dal testo da riga vuota.

Esclusioni (paratesto, non contenuto normativo)
-----------------------------------------------
- front matter, Contents, Foreword, History, elenchi di figure/tabelle: non fanno parte
  del file di capitolo (stanno in raw.txt) e non sono censiti;
- intestazioni di raggruppamento della clausola 5 senza testo proprio (elencate sopra):
  nessun nodo e nessun item di indice, per non creare item fittizi;
- la didascalia "Figure 1: Hashing process" e l'immagine della figura 1: la figura e' un
  disegno, non testo estraibile; le frasi che vi rinviano ("The items included in the
  hashing procedure and the concatenation order are shown in figure 1.", "Figure 1
  illustrates the hashing process." e la NOTE 7 della 5.5.2) sono mantenute nei
  rispettivi testo_integrale. Unico elemento del capitolo non riproducibile come testo:
  il contenuto grafico della figura;
- nessuna tabella di soli riferimenti bibliografici in questo capitolo (la clausola 2
  References sta in cap01.txt).

Rinvii demandati alla fase 6 (nessuna relazione creata verso di essi)
--------------------------------------------------------------------
- verso il capitolo 4 (cap02.txt) della stessa fonte: 5.2.4.1 -> "clause 4.2" (id-data);
  5.2.8 -> "clause 4.8.1" (messageImprint di TimeStampToken); 5.4.2.1 e 5.4.2.2 ->
  "clause 4.8.2" (codifiche OCSPResponse/BasicOCSPResponse e tipo RevocationInfoChoices);
  5.5.2 -> "clause 4.4" (SignedData.crls); 5.5.3 -> "clause 4.4" (SignedData da
  estendere con i dati di validazione); vari riferimenti a "clause 4.7.1" (codifica DER)
  nelle clausole 5.5.2 e 5.5.3;
- verso l'annex A (cap05.txt) della stessa fonte: 5.4.1 -> "clause A.1"; 5.5.3 ->
  "clause A.2.4" (attributi ATSv2) e "clause A.2.5" (long-term-validation);
- verso l'annex B e l'annex D (cap06.txt / altro capitolo della stessa fonte): "annex D"
  e' citato come sede delle definizioni ASN.1 copiate nelle clausole 5.2.3, 5.2.4.2,
  5.2.5, 5.2.6.1, 5.2.6.2, 5.2.6.3, 5.2.8, 5.2.9.1, 5.2.9.2, 5.2.10, 5.3, 5.5.2 e
  5.5.3; "annex B" e' citato nella 5.5.3 (attributi ammessi in unsignedAttrs);
- verso la partizione "clausola 5.4.2" (unita' indivisa senza nodo: e' una pura
  intestazione di raggruppamento): 5.5.3 -> "OCSP responses shall be included as defined
  in clause 5.4.2.";
- verso fonti esterne (nessuna relazione in questa fase): IETF RFC 5652 [7] (CMS, 5.1.1,
  5.1.2, 5.2.1, 5.2.7), IETF RFC 2634 [3] e IETF RFC 5035 [5] (ESS, 5.2.2.1-5.2.2.3,
  5.2.4.1, 5.2.11, 5.2.12), IETF RFC 6211 [19] (5.2.13), IETF RFC 2045 [2] (MIME,
  5.2.4.1, 5.2.4.2), IETF RFC 5280 [6] (CRL, 5.4.3), IETF RFC 5940 [13] (5.4.2.2),
  Recommendation ITU-T X.520 [15] (5.2.5), Recommendation ITU-T X.509 [i.18] e SAML
  [18] (5.2.6.1-5.2.6.3), ETSI TS 101 733 [1] (archivio, 5.2.9.1, 5.5.3), ETSI TS 119
  312 [i.8] (5.5.2), ETSI TS 119 172-1 [i.7] (5.2.3).

Relazioni dichiarate (solo fra righe di questo modulo)
-----------------------------------------------------
Sette relazioni "richiama" su rinvii interni al capitolo, tutte con evidenza textual
(citazione letterale presente nel testo_integrale del nodo citante): 5.2.6.1 ->
5.2.6.3 (esempio di signedAssertions) e -> 5.2.6.2 (NOTE 2, nuovo attributo per il
ruolo rivendicato); 5.2.9.1 -> 5.2.9.2 (il campo sigPolicyQualifiers contiene istanze
di SigPolicyQualifierInfo definite in 5.2.9.2); 5.2.10 -> 5.2.9.2 (SPDocSpecification);
5.5.2 -> 5.5.3 (attributo archive-time-stamp-v3 che contiene il token di marca
temporale) e 5.5.3 -> 5.5.2 (istanza di ATSHashIndexV3) e -> 5.4.2.2 (OCSP response
inclusa in SignedData.crls). confidence resta null: non esiste uno score reale.

Conteggio di copertura
----------------------
29 item di indice, 29 righe: 27 obblighi + 2 principi. Nessun item doppio, nessun item
mancante, nessuna riga fuori indice.

Dubbi di classificazione lasciati aperti (per la revisione umana)
----------------------------------------------------------------
1) clausola 5.2.7 (countersignature): la controfirma e' per definizione apposta da una
   parte terza rispetto al firmatario, ma il testo non la nomina; la riga resta senza
   soggetti invece di attribuirle 'Terza parte' per inferenza.
2) clausole 5.1.1, 5.1.2, 5.2.2.1-5.2.2.3, 5.2.4.1, 5.2.4.2, 5.2.6.2, 5.2.6.3, 5.2.8,
   5.2.9.2, 5.2.10, 5.2.11, 5.2.12, 5.2.13, 5.4.2.1, 5.4.2.2, 5.4.3, 5.5.2, 5.5.3:
   il requisito e' formulato sull'attributo ("the X attribute shall ..."), non su un
   soggetto nominato; se la revisione preferisse imputarle al sistema di creazione della
   firma, la categoria sarebbe 'Utente/titolare' obbligato su tutte queste righe.
3) clausola 5.2.10 NOTE 2: "the entity adding the signature policy into the
   signature-policy-store" e' il responsabile nominato dal testo, ma non corrisponde a
   nessuna delle quattro categorie disponibili (puo' essere il firmatario o un
   prestatore di servizi di conservazione): nessun soggetto dichiarato.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "clausola 5.1.1 (The content-type attribute)",
        "testo": (
            "Attributo firmato che indica il tipo del contenuto firmato e deve essere "
            "conforme alla definizione CMS di IETF RFC 5652, clausola 11.1. La NOTE "
            "ufficiale chiarisce che il valore di ContentType coincide con "
            "l'eContentType dell'EncapsulatedContentInfo firmato."
        ),
        "testo_integrale": (
            """Semantics: The content-type attribute is a signed attribute.

The content-type attribute indicates the type of the signed content.

Syntax: The content-type attribute shall be as defined in CMS (IETF RFC 5652 [7], clause 11.1).

NOTE: As stated in IETF RFC 5652 [7], the content of ContentType (the value of the attribute content-type) is the same as the eContentType of the EncapsulatedContentInfo value being signed."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.1.2 (The message-digest attribute)",
        "testo": (
            "Attributo firmato che specifica il message digest del contenuto firmato; "
            "sia l'attributo sia il processo di calcolo del digest devono essere "
            "conformi a IETF RFC 5652 (clausole 11.2 e 5.4)."
        ),
        "testo_integrale": (
            """Semantics: The message-digest attribute is a signed attribute.

The message-digest attribute specifies the message digest of the content being signed.

Syntax: The message-digest attribute shall be as defined in CMS (IETF RFC 5652 [7], clause 11.2).

The message digest calculation process shall be as defined in CMS (IETF RFC 5652 [7], clause 5.4)."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.1 (The signing-time attribute)",
        "testo": (
            "Attributo firmato che deve indicare l'ora in cui il firmatario dichiara di "
            "aver eseguito il processo di firma; deve essere conforme alla definizione "
            "CMS di IETF RFC 5652, clausola 11.3."
        ),
        "testo_integrale": (
            """Semantics: The signing-time attribute is a signed attribute.

The signing-time attribute shall specify the time at which the signer claims to having performed the signing process.

Syntax: The signing-time attribute shall be as defined in CMS (IETF RFC 5652 [7], clause 11.3)."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.2.1 (General requirements)",
        "testo": (
            "Requisiti comuni agli attributi di riferimento al certificato di firma: "
            "devono contenere un riferimento al certificato di firma, possono contenere "
            "riferimenti ad alcuni o a tutti i certificati del percorso del certificato "
            "di firma (incluso il trust anchor quando e' un certificato) e devono "
            "contenere un valore di digest per ogni certificato. Le NOTE 1 e 2 precisano "
            "il ruolo della signature validation policy e la semantica del primo "
            "certificato nella sequenza (IETF RFC 2634 e RFC 5035)."
        ),
        "testo_integrale": (
            """Semantics: The attributes specified in clauses below shall contain one reference to the signing certificate.

The attributes specified in clauses below may contain references to some of or all the certificates within the signing certificate path, including one reference to the trust anchor when this is a certificate.

For each certificate, these attributes shall contain a digest value.

NOTE 1: For instance, the signature validation policy can mandate other certificates to be present which can include all the certificates up to the trust anchor.

NOTE 2: IETF RFC 2634 [3] and IETF RFC 5035 [5] state that the first certificate in the sequence is the certificate used to verify the signature and that other certificates in the sequence can be attribute certificates or other certificate types."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.2.2 (ESS signing-certificate attribute)",
        "testo": (
            "ESS signing-certificate: attributo firmato di riferimento al certificato di "
            "firma basato su SHA-1, conforme a Enhanced Security Services (IETF RFC 2634, "
            "clausola 5.4) e ulteriormente specificato dal presente documento; il campo "
            "policies non deve essere usato. NOTE 1 e 2 precisano il calcolo di certHash "
            "da ESSCertID e il carattere solo indicativo di IssuerSerial."
        ),
        "testo_integrale": (
            """Semantics: The ESS signing-certificate attribute is a signed attribute.

The ESS signing-certificate attribute is a signing certificate attribute using the SHA-1 hash algorithm.

Syntax: The signing-certificate attribute shall be as defined in Enhanced Security Services (ESS), IETF RFC 2634 [3], clause 5.4, and further specified in the present document.

NOTE 1: The certHash from ESSCertID is computed using SHA-1 over the entire DER encoded certificate (IETF RFC 2634 [3]).

The policies field shall not be used.

NOTE 2: The information in the IssuerSerial element is only a hint that can help to identify the certificate whose digest matches the value present in the reference. But the binding information is the digest of the certificate."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.2.3 (ESS signing-certificate-v2 attribute)",
        "testo": (
            "ESS signing-certificate-v2: attributo firmato di riferimento al certificato "
            "di firma basato su un algoritmo di hash diverso da SHA-1, conforme a \"ESS "
            "Update: Adding CertID Algorithm Agility\" (IETF RFC 5035, clausola 4) e "
            "ulteriormente specificato dal presente documento; il campo policies non deve "
            "essere usato. NOTE 1 e 2 speculari a quelle della clausola 5.2.2.2."
        ),
        "testo_integrale": (
            """Semantics: The ESS signing-certificate-v2 attribute is a signed attribute.

The ESS signing-certificate-v2 attribute is a signing certificate attribute using a hash algorithm different from SHA-1.

Syntax: The signing-certificate-v2 attribute shall be as defined in "ESS Update: Adding CertID Algorithm Agility", IETF RFC 5035 [5], clause 4 and further specified in the present document.

NOTE 1: The certHash from ESSCertID is computed over the entire DER encoded certificate (IETF RFC 5035 [5]).

The policies field shall not be used.

NOTE 2: The information in the IssuerSerial element is only a hint that can help to identify the certificate whose digest matches the value present in the reference. But the binding information is the digest of the certificate."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.3 (The commitment-type-indication attribute)",
        "testo": (
            "Attributo firmato che qualifica l'oggetto dati firmato e deve indicare un "
            "commitment assunto dal firmatario al momento della firma. Deve contenere "
            "esattamente un componente di tipo AttributeValue, il valore deve essere "
            "un'istanza del tipo ASN.1 CommitmentTypeIndication e l'attributo deve essere "
            "identificato dall'OID id-aa-ets-commitmentType; il campo "
            "commitmentTypeQualifier permette di aggiungere informazioni qualificanti."
        ),
        "testo_integrale": (
            """Semantics: The commitment-type-indication attribute shall be a signed attribute that qualifies the signed data object.

The commitment-type-indication attribute shall indicate a commitment made by the signer when signing the data object.

NOTE 1: The commitment type can be:

  •   defined as part of the signature policy, in which case, the commitment type has precise semantics that are defined as part of the signature policy; or

  •   be a registered type, in which case, the commitment type has precise semantics defined by registration, under the rules of the registration authority. Such a registration authority can be a trading association or a legislative authority.

NOTE 2: The specification of commitment type identifiers is outside the scope of the present document. For a list of predefined commitment type identifiers, see the document on signature policies, ETSI TS 119 172-1 [i.7].

Syntax: The commitment-type-indication attribute shall contain exactly one component of AttributeValue type.

The commitment-type-indication attribute value shall be an instance of CommitmentTypeIndication ASN.1 type.

The commitment-type-indication attribute shall be identified by the id-aa-ets-commitmentType OID.

The commitmentTypeQualifier field provides means to include additional qualifying information on the commitment made by the signer.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-commitmentType OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 16}

CommitmentTypeIndication ::= SEQUENCE {
  commitmentTypeId         CommitmentTypeIdentifier,
  commitmentTypeQualifier SEQUENCE SIZE (1..MAX) OF CommitmentTypeQualifier OPTIONAL
}

CommitmentTypeIdentifier ::= OBJECT IDENTIFIER

CommitmentTypeQualifier ::= SEQUENCE {
  commitmentQualifierId   COMMITMENT-QUALIFIER.&id,
  qualifier               COMMITMENT-QUALIFIER.&Qualifier OPTIONAL
}

COMMITMENT-QUALIFIER ::= CLASS {
  &id         OBJECT IDENTIFIER UNIQUE,
  &Qualifier OPTIONAL }
WITH SYNTAX {
  COMMITMENT-QUALIFIER-ID &id
  [COMMITMENT-TYPE         &Qualifier] }"""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.4.1 (The content-hints attribute)",
        "testo": (
            "Attributo firmato che non deve essere usato all'interno di una controfirma e "
            "che deve fornire informazioni sul contenuto firmato piu' interno di un "
            "messaggio a piu' livelli. Deve essere conforme a ESS (IETF RFC 2634, clausole "
            "1.3.4 e 2.9); il contentDescription puo' completare un contentType definito "
            "altrove, con requisiti specifici quando serve indicare il formato preciso dei "
            "dati da presentare all'utente e quando il formato e' definito da tipi MIME."
        ),
        "testo_integrale": (
            """Semantics: The content-hints attribute shall be a signed attribute.

The content-hints attribute shall not be used within a countersignature.

The content-hints attribute shall provide information on the innermost signed content of a multi-layer message where one content is encapsulated in another.

Syntax: The content-hints attribute shall be as defined in ESS (IETF RFC 2634 [3], clauses 1.3.4 and 2.9).

The contentDescription may be used to complement a contentType defined elsewhere.

When used to indicate the precise format of the data to be presented to the user:

  •   the contentType shall indicate the type of the associated content. It is an object identifier assigned by an authority that defines the content type; and

  •   when the contentType is id-data (see clause 4.2) the contentDescription shall define the presentation format.

When the format of the content is defined by Multipurpose Internet Mail Extensions (MIME) types:

  •   the contentType shall be id-data (see clause 4.2);

  •   the contentDescription shall be used to indicate the encoding and the intended presentation application of the data, in accordance with the rules defined in IETF RFC 2045 [2]; see annex E for an example of structured contents and MIME."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.4.2 (The mime-type attribute)",
        "testo": (
            "Attributo firmato che non deve essere usato all'interno di una controfirma e "
            "che deve indicare il mime-type dei dati firmati. Deve contenere esattamente "
            "un componente di tipo AttributeValue, il valore deve essere un'istanza del "
            "tipo ASN.1 MimeType e l'attributo deve essere identificato dall'OID "
            "id-aa-ets-mimeType; il MimeType deve indicare la codifica e l'applicazione di "
            "presentazione prevista, in conformita' a IETF RFC 2045."
        ),
        "testo_integrale": (
            """Semantics: The mime-type attribute shall be a signed attribute.

The mime-type attribute shall not be used within a countersignature.

The mime-type attribute shall indicate the mime-type of the signed data.

NOTE 1: This attribute is similar in spirit to the contentDescription field of the content-hints attribute, but can be used without a multi-layered document.

Syntax: The mime-type attribute shall contain exactly one component of AttributeValue type.

The mime-type attribute value shall be an instance of MimeType ASN.1 type.

The mime-type attribute shall be identified by the id-aa-ets-mimeType OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-mimeType OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4) etsi(0)
    electronic-signature-standard (1733) attributes(2) 1 }

MimeType::= UTF8String

The MimeType shall indicate the encoding and the intended presentation application of the signed data. The content of MimeType shall be in accordance with the rules defined in IETF RFC 2045 [2].

NOTE 2: See annex E for an example of structured contents and MIME."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.5 (The signer-location attribute)",
        "testo": (
            "Attributo firmato che deve specificare un indirizzo associato al firmatario "
            "in una determinata localita' geografica (es. la citta'). Deve contenere "
            "esattamente un componente AttributeValue, il valore deve essere un'istanza "
            "del tipo ASN.1 SignerLocation e l'attributo deve essere identificato dall'OID "
            "id-aa-ets-signerLocation; almeno uno fra countryName, localityName e "
            "postalAddress deve essere presente e il contenuto di countryName e "
            "localityName dovrebbe seguire Recommendation ITU-T X.520, clausole 6.3.1 e "
            "6.3.2."
        ),
        "testo_integrale": (
            """Semantics: The signer-location attribute shall be a signed attribute.

The signer-location attribute shall specify an address associated with the signer at a particular geographical (e.g. city) location.

Syntax: The signer-location attribute shall contain exactly one component of AttributeValue type.

The signer-location attribute value shall be an instance of SignerLocation ASN.1 type.

The signer-location attribute shall be identified by the id-aa-ets-signerLocation OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-signerLocation OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 17 }

SignerLocation ::= SEQUENCE { -- at least one of the following shall be present
  countryName   [0] DirectoryString OPTIONAL, -- As used to name a Country in X.520
  localityName [1] DirectoryString OPTIONAL, -- As used to name a locality in X.520
  postalAddress [2] PostalAddress OPTIONAL
}

PostalAddress ::= SEQUENCE SIZE(1..6) OF DirectoryString{maxSize}
                                -- maxSize parametrization as specified in X.683

At least one of the fields countryName, localityName or postalAddress shall be present.

The content of countryName should be used to name a country a specified in Recommendation ITU-T X.520 [15], clause 6.3.1.

The content of localityName should be used to name a locality a specified in Recommendation ITU-T X.520 [15], clause 6.3.2."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.6.1 (The signer-attributes-v2 attribute)",
        "testo": (
            "Attributo firmato che incapsula attributi del firmatario (es. il ruolo): "
            "attributi rivendicati dal firmatario, attributi certificati in certificati "
            "di attributo emessi da un'Attribute Authority e/o asserzioni firmate da una "
            "terza parte. Deve contenere esattamente un componente AttributeValue, il "
            "valore deve essere un'istanza del tipo ASN.1 SignerAttributeV2 e l'attributo "
            "deve essere identificato dall'OID id-aa-ets-signerAttrV2; claimedAttributes "
            "contiene attributi rivendicati non certificati, certifiedAttributesV2 una "
            "sequenza non vuota di attributi certificati e signedAssertions una sequenza "
            "non vuota di asserzioni firmate da terzi. Non deve essere creato un "
            "signer-attributes-v2 vuoto."
        ),
        "testo_integrale": (
            """Semantics: The signer-attributes-v2 attribute shall be a signed attribute.

The signer attributes shall encapsulate signer attributes (e.g. role). This attribute may encapsulate:

  •   attributes claimed by the signer;

  •   attributes certified in attribute certificates issued by an Attribute Authority; or/and

  •   assertions signed by a third party.

Syntax: The signer-attributes-v2 attribute shall contain exactly one component of AttributeValue type.

The signer-attributes-v2 attribute value shall be an instance of SignerAttributeV2 ASN.1 type.

The signer-attributes-v2 attribute shall be identified by the id-aa-ets-signerAttrV2 OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-signerAttrV2 OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4)
    etsi(0) cades(19122) attributes(1) 1 }

SignerAttributeV2 ::= SEQUENCE {
  claimedAttributes     [0] ClaimedAttributes OPTIONAL,
  certifiedAttributesV2 [1] CertifiedAttributesV2 OPTIONAL,
  signedAssertions      [2] SignedAssertions OPTIONAL
}

ClaimedAttributes ::= SEQUENCE OF Attribute

CertifiedAttributesV2 ::= SEQUENCE OF CHOICE {
  attributeCertificate      [0] AttributeCertificate,
  otherAttributeCertificate [1] OtherAttributeCertificate
}

OtherAttributeCertificate ::= SEQUENCE {
  otherAttributeCertID OTHER-ATTRIBUTE-CERT.&id,
  otherAttributeCert    OTHER-ATTRIBUTE-CERT.&OtherAttributeCert OPTIONAL
}

OTHER-ATTRIBUTE-CERT ::= CLASS {
  &id                  OBJECT IDENTIFIER UNIQUE,
  &OtherAttributeCert OPTIONAL }
WITH SYNTAX {
  OTHER-ATTRIBUTE-CERT-ID    &id
  [OTHER-ATTRIBUTE-CERT-TYPE    &OtherAttributeCert] }

SignedAssertions ::= SEQUENCE OF SignedAssertion

SignedAssertion ::= SEQUENCE {
  signedAssertionID SIGNED-ASSERTION.&id,
  signedAssertion    SIGNED-ASSERTION.&Assertion OPTIONAL
}

SIGNED-ASSERTION::= CLASS {
  &id         OBJECT IDENTIFIER UNIQUE,
  &Assertion OPTIONAL }
WITH SYNTAX {
  SIGNED-ASSERTION-ID     &id
  [SIGNED-ASSERTION-TYPE &Assertion] }

Attribute and AttributeCertificate shall be as defined in clause 4.8.2.

The claimedAttributes field shall contain a sequence of attributes claimed by the signer but which are not certified. These signer attributes are expressed using Attribute types.

NOTE 1: A user who wants to add a claimed role attribute can use the RoleAttribute as defined in Recommendation ITU-T X.509 [i.18].

NOTE 2: Clause 5.2.6.2 defines a new attribute that can be used to describe a claimed role by encapsulating a SAML assertion.

The certifiedAttributes field shall contain a non-empty sequence of certified attributes. These signer attributes shall be expressed by:

  •   attributeCertificate: an attribute certificate issued to the signer by an Attribute Authority; or

  •   otherAttributeCertificate: an attribute certificate (issued, in consequence, by an Attribute Authority) in different syntax than the one used for X509 attribute certificates. The definition of specific otherAttributeCertificates is outside of the scope of the present document.

The signedAssertions field shall contain a non-empty sequence of assertions signed by a third party.

NOTE 3: A signed assertion is stronger than a claimed attribute, since a third party asserts with a signature that the attribute of the signer is valid. However, it may be less restrictive than an attribute certificate.

An example of a definition of a specific signedAssertions is provided in clause 5.2.6.3. Any assertion encapsulated within this sequence shall be signed by third party.

NOTE 4: A possible content of such a qualifier can be a signed SAML assertion, see of SAML [18].

Empty signer-attributes-v2 shall not be created."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.6.2 (claimed-SAML-assertion)",
        "testo": (
            "Claimed-SAML-assertion: asserzione rivendicata che deve includere una SAML "
            "assertion e che puo' essere usata solo nel campo claimedAttributes "
            "dell'attributo signer-attributes-v2. E' di tipo ASN.1 Attribute, deve "
            "contenere esattamente un componente AttributeValue, il valore deve essere "
            "un'istanza del tipo ASN.1 ClaimedSAMLAssertion e l'attributo deve essere "
            "identificato dall'OID id-aa-ets-claimedSAML; il valore deve contenere la "
            "rappresentazione in byte della SAML assertion definita in SAML [18]."
        ),
        "testo_integrale": (
            """Semantics: The claimed-SAML-assertion is a claimed assertion that shall include a SAML assertion.

The claimed-SAML-assertion may be used in a claimedAttributes field of the signer-attributes-v2 attribute. It shall not be used anywhere else.

Syntax: The claimed-SAML-assertion is of ASN.1 type Attribute.

The claimed-SAML-assertion shall contain exactly one component of AttributeValue type.

The claimed-SAML-assertion value shall be an instance of ClaimedSAMLAssertion ASN.1 type.

The claimed-SAML-assertion shall be identified by the id-aa-ets-claimedSAML OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-claimedSAML OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4)
    etsi(0) cades(19122) attributes(1) 2 }

ClaimedSAMLAssertion ::= OCTET STRING

The value of ClaimedSAMLAssertion shall contain the byte representation of SAML assertion as defined in SAML [18]."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.6.3 (signed-SAML-assertion)",
        "testo": (
            "Signed-SAML-assertion: deve essere identificata dall'OID id-ets-signeddSAML "
            "ed essere di tipo OCTET STRING; le definizioni ASN.1 corrispondenti sono "
            "nell'annex D e sono copiate qui per informazione. Il valore di "
            "ClaimedSAMLAssertion deve contenere la rappresentazione in byte di una SAML "
            "assertion firmata come definita in SAML [18]."
        ),
        "testo_integrale": (
            """The signed-SAML-assertion shall be identified by the id-ets-signeddSAML OID.

The signed-SAML-assertion shall be of type OCTET STRING.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-ets-signedSAML OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4)
    etsi(0) cades(19122) additional(3) 0 }

SignedSAMLAssertion ::= OCTET STRING

The value of ClaimedSAMLAssertion shall contain the byte representation of a signed SAML assertion as defined in SAML [18]."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.7 (The countersignature attribute)",
        "testo": (
            "Attributo unsigned che deve includere una controfirma sulla firma CAdES in "
            "cui l'attributo e' incluso; deve essere conforme alla definizione CMS di "
            "IETF RFC 5652, clausola 11.4."
        ),
        "testo_integrale": (
            """Semantics: The countersignature attribute is an unsigned attribute.

The countersignature attribute shall include a counter signature on the CAdES signature where this attribute is included.

Syntax: The countersignature attribute shall be as defined in CMS (IETF RFC 5652 [7], clause 11.4)."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.8 (The content-time-stamp attribute)",
        "testo": (
            "Attributo firmato che deve incapsulare un token di marca temporale sul "
            "contenuto dei dati firmati prima che sia firmato. Deve contenere esattamente "
            "un componente AttributeValue, il valore deve essere un'istanza del tipo ASN.1 "
            "ContentTimestamp e l'attributo deve essere identificato dall'OID "
            "id-aa-ets-contentTimestamp; il valore di messageImprint del TimeStampToken "
            "deve essere l'hash del valore di eContent per firme attached o dei dati "
            "esterni per firme detached, calcolato sui dati grezzi senza tag e length "
            "ASN.1."
        ),
        "testo_integrale": (
            """Semantics: The content-time-stamp attribute shall be a signed attribute.

The content-time-stamp attribute shall encapsulate one time-stamp token of the signed data content before it is signed.

Syntax: The content-time-stamp attribute shall contain exactly one component of AttributeValue type.

The content-time-stamp attribute value shall be an instance of ContentTimestamp ASN.1 type.

The content-time-stamp attribute shall be identified by the id-aa-ets-contentTimestamp OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-contentTimestamp OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 20 }

ContentTimestamp::= TimeStampToken

The value of messageImprint of TimeStampToken (see clause 4.8.1) shall be a hash of:

  •   the value of eContent in the case of an attached signature; or

  •   the external data in the case of a detached signature.

In both cases, the hash shall be computed over the raw data, without ASN.1 tag and length."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.9.1 (The signature-policy-identifier attribute)",
        "testo": (
            "Attributo firmato che deve contenere un identificatore esplicito della "
            "signature policy: esattamente un componente AttributeValue, valore istanza "
            "del tipo ASN.1 SignaturePolicyIdentifier e OID id-aa-ets-sigPolicyId. La "
            "scelta signaturePolicyImplied non deve essere usata; sigPolicyId deve "
            "contenere un OID che identifica univocamente una versione specifica della "
            "policy, sigPolicyHash l'identificatore dell'algoritmo di hash e il valore di "
            "hash della policy oppure un valore zero-hash (ottetto di lunghezza qualsiasi "
            "con tutti gli ottetti a zero, che indica hash non noto e deve essere "
            "interpretato come tale dalle applicazioni di validazione, mentre le "
            "applicazioni di creazione dovrebbero generarlo con lunghezza coerente "
            "all'algoritmo). Se la specifica della policy non e' chiara dal contesto va "
            "usato il qualificatore sp-doc-specification; il campo sigPolicyQualifiers "
            "puo' qualificare ulteriormente l'attributo con istanze di "
            "SigPolicyQualifierInfo definite nella clausola 5.2.9.2."
        ),
        "testo_integrale": (
            """Semantics: The signature-policy-identifier attribute shall be a signed attribute.

The signature-policy-identifier shall contain an explicit identifier of the signature policy.

Syntax: The signature-policy-identifier attribute shall contain exactly one component of AttributeValue type.

The signature-policy-identifier attribute value shall be an instance of SignaturePolicyIdentifier ASN.1 type.

The signature-policy-identifier attribute shall be identified by the id-aa-ets-sigPolicyId OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-sigPolicyId OBJECT IDENTIFIER ::= { iso(1) member-body(2) us(840)
    rsadsi(113549) pkcs(1) pkcs9(9) smime(16) id-aa(2) 15 }

SignaturePolicyIdentifier ::= CHOICE {
  signaturePolicyId      SignaturePolicyId,
  signaturePolicyImplied SignaturePolicyImplied -- not used in this version
}

SignaturePolicyId ::= SEQUENCE {
  sigPolicyId          SigPolicyId,
  sigPolicyHash        SigPolicyHash,
  sigPolicyQualifiers SEQUENCE SIZE (1..MAX) OF SigPolicyQualifierInfo OPTIONAL
}

SignaturePolicyImplied ::= NULL

SigPolicyId ::= OBJECT IDENTIFIER

SigPolicyHash ::= OtherHashAlgAndValue

OtherHashAlgAndValue ::= SEQUENCE {
  hashAlgorithm AlgorithmIdentifier,
  hashValue      OtherHashValue }

OtherHashValue ::= OCTET STRING

The signaturePolicyImplied choice shall not be used.

The sigPolicyId field shall contain an object-identifier that uniquely identifies a specific version of the signature policy.

The sigPolicyHash field shall contain the identifier of the hash algorithm, and either the hash of the value of the signature policy or a zero-hash value.

A zero-hash value shall be an octet string of any length (including zero length) whose octets all have the value zero.

A zero-hash value shall be used to indicate that the policy hash value is not known.

If the hashValue field of the sigPolicyHash field contains a zero-hash value, signature validation applications shall interpret that value as indicating that the policy hash value is not known.

Signature creation applications that generate a zero-hash value should generate it with a length consistent with the hash algorithm specified by the hashAlgorithm field of the sigPolicyHash field.

NOTE 1: The use of a zero-hash value in the hashValue of the sigPolicyHash is to ensure backwards compatibility with earlier versions of ETSI TS 101 733 [1].

NOTE 2: Earlier versions of the present document were unclear on what exactly constitutes a zero-hash value, with the consequence that different implementations chose values of different length. The present document therefore requires that zero-hash values of any length have to be accepted. The recommendation to create zero-hash values with a length consistent with the specified hash algorithm is for compatibility with existing implementations - in particular those created prior to the introduction of zero-hash values - that may be unprepared to handle hash values with a different length.

NOTE 3: Depending on the hash algorithm, the actual computed hash value of a signature policy document may theoretically (although exceedingly unlikely) happen to be zero. Where applicable, applications can reject policy documents that would result in a zero-hash value, as the present document requires such values to be interpreted as an unknown hash value.

The input to hash computation of sigPolicyHash depends on the technical specification of the signature policy. In the case where the specification is not clear from the context of the signature, the sp-doc-specification qualifier shall be used to identify the used specification.

The sigPolicyQualifiers field may further qualify the signature-policy-identifier attribute. It contains a sequence of instances of SigPolicyQualifierInfo type which is defined in clause 5.2.9.2.

The sigPolicyQualifiers field may contain one or more qualifiers of the same type."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "clausola 5.2.9.2 (The SigPolicyQualifierInfo type)",
        "testo": (
            "Tipo SigPolicyQualifierInfo, che puo' essere usato per qualificare "
            "ulteriormente l'attributo signature-policy-identifier. Sono stati identificati "
            "tre qualificatori: un URI/URL da cui ottenere una copia del documento di "
            "signature policy (SPuri), un avviso all'utente da mostrare quando la firma "
            "viene validata (SPUserNotice) e un identificatore della specifica tecnica che "
            "definisce la sintassi del documento di policy (SPDocSpecification). La "
            "definizione ASN.1 e le definizioni dei singoli qualificatori (id-spq-ets-uri, "
            "id-spq-ets-unotice, id-spq-ets-docspec) devono essere quelle dell'annex D, "
            "copiate nella clausola; un elemento SPuri deve contenere un URL da cui "
            "ottenere il documento, un elemento SPUserNotice informazioni da mostrare alla "
            "validazione con explicitText contenente il testo dell'avviso e noticeRef che "
            "nomina un'organizzazione e identifica per numeri un gruppo di dichiarazioni "
            "testuali, mentre SPDocSpecification deve identificare la specifica tecnica "
            "(con la scelta oid o uri a seconda di come e' identificata)."
        ),
        "testo_integrale": (
            """Semantics: The SigPolicyQualifierInfo type may be used to further qualify the signature-policy-identifier attribute.

Three qualifiers for the signature policy have been identified so far:

  •   a URI or URL where a copy of the signature policy document can be obtained (an element of type SPuri);

  •   a user notice that should be displayed whenever the signature is validated (an element of type SPUserNotice); and

  •   an identifier of the technical specification that defines the syntax used for producing the signature policy document (an element of type SPDocSpecification).

Syntax: The ASN.1 definition of the SigPolicyQualifierInfo qualifier shall be as defined in annex D and is copied here for information:

SigPolicyQualifierInfo ::= SEQUENCE {
  sigPolicyQualifierId SIG-POLICY-QUALIFIER.&id ({SupportedSigPolicyQualifiers}),
  qualifier             SIG-POLICY-QUALIFIER.&Qualifier
     ({SupportedSigPolicyQualifiers} {@sigPolicyQualifierId}) OPTIONAL
}

SupportedSigPolicyQualifiers SIG-POLICY-QUALIFIER ::= { noticeToUser |
  pointerToSigPolSpec | sigPolDocSpecification }

SIG-POLICY-QUALIFIER ::= CLASS {
  &id         OBJECT IDENTIFIER UNIQUE,
  &Qualifier OPTIONAL }
WITH SYNTAX {
  SIG-POLICY-QUALIFIER-ID &id
  [SIG-QUALIFIER-TYPE      &Qualifier] }

noticeToUser SIG-POLICY-QUALIFIER ::= {
  SIG-POLICY-QUALIFIER-ID id-spq-ets-unotice SIG-QUALIFIER-TYPE SPUserNotice }

pointerToSigPolSpec SIG-POLICY-QUALIFIER ::= {
  SIG-POLICY-QUALIFIER-ID id-spq-ets-uri SIG-QUALIFIER-TYPE SPuri }

sigPolDocSpecification SIG-POLICY-QUALIFIER ::= {
  SIG-POLICY-QUALIFIER-ID id-spq-ets-docspec SIG-QUALIFIER-TYPE SPDocSpecification }

The semantics and syntax of the qualifier is as identified by the object-identifier in the sigPolicyQualifierId field. The ASN.1 definition of the qualifiers shall be as defined in annex D and is copied here for information:

-- spuri
id-spq-ets-uri OBJECT IDENTIFIER ::= { iso(1)
    member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs9(9)
    smime(16) id-spq(5) 1 }

SPuri ::= IA5String

-- sp-user-notice
id-spq-ets-unotice OBJECT IDENTIFIER ::= { iso(1)
    member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs9(9)
    smime(16) id-spq(5) 2 }

SPUserNotice ::= SEQUENCE {
  noticeRef     NoticeReference OPTIONAL,
  explicitText DisplayText OPTIONAL
}

NoticeReference ::= SEQUENCE {
  organization   DisplayText,
  noticeNumbers SEQUENCE OF INTEGER
}

DisplayText ::= CHOICE {
  visibleString VisibleString          (SIZE (1..200)),
  bmpString      BMPString             (SIZE (1..200)),
  utf8String     UTF8String            (SIZE (1..200))
}

-- sp-doc-specification
id-spq-ets-docspec OBJECT IDENTIFIER ::=            { itu-t(0) identified-organization(4)
    etsi(0) cades(19122) id-spq (2) 1 }

SPDocSpecification ::= CHOICE {
  oid OBJECT IDENTIFIER,
  uri IA5String
}

An element of type SPuri shall contain a URL value where a copy of the signature policy document can be obtained.

NOTE 1: This URL can reference, for instance, a remote site (which can be managed by an entity entitled for this purpose) from where (signing/validating) applications can retrieve the signature policy document.

An element of type SPUserNotice shall contain information that is intended for being displayed whenever the signature is validated.

The explicitText field shall contain the text of the notice to be displayed.

NOTE 2: Other notices can come from the organization issuing the signature policy.

The noticeRef field shall name an organization and shall identify by numbers (noticeNumbers field) a group of textual statements prepared by that organization, so that the application can get the explicit notices from a notices file.

The SPDocSpecification shall identify the technical specification that defines the syntax used for producing the signature policy.

If the technical specification is identified using an OID, then the oid choice shall be used to contain the OID of the specification.

If the technical specification is identified using a URI, then the uri choice shall be used to contain this URI.

NOTE 3: This qualifier allows identifying whether the signature policy document is human readable, XML encoded, or ASN.1 encoded, by identifying the specific technical specifications where these formats will be defined."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.10 (The signature-policy-store attribute)",
        "testo": (
            "Attributo unsigned che deve contenere o il documento di signature policy "
            "referenziato nell'attributo signature-policy-identifier (cosi' da poter essere "
            "usato per la validazione offline e a lungo termine) o un URI che referenzia "
            "uno store locale da cui recuperarlo. Deve contenere esattamente un componente "
            "AttributeValue, il valore deve essere un'istanza del tipo ASN.1 "
            "SignaturePolicyStore e l'attributo deve essere identificato dall'OID "
            "id-aa-ets-sigPolicyStore; spDocument contiene il documento codificato o l'URI "
            "locale, spDocSpec identifica la specifica tecnica con la SPDocSpecification "
            "definita nella clausola 5.2.9.2."
        ),
        "testo_integrale": (
            """Semantics: The signature-policy-store attribute shall be an unsigned attribute.

The signature-policy-store attribute shall contain either:

  •   the signature policy document which is referenced in the signature-policy-identifier attribute so that the signature policy document can be used for offline and long-term validation; or

  •   a URI referencing a local store where the signature policy document can be retrieved.

Syntax: The signature-policy-store attribute shall contain exactly one component of AttributeValue type.

The signature-policy-store attribute value shall be an instance of SignaturePolicyStore ASN.1 type.

The signature-policy-store attribute shall be identified by the id-aa-ets-sigPolicyStore OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-sigPolicyStore OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4)
    etsi(0) cades(19122) attributes(1) 3 }

SignaturePolicyStore ::= SEQUENCE {
  spDocSpec   SPDocSpecification ,
  spDocument SignaturePolicyDocument
}

SignaturePolicyDocument ::= CHOICE {
  sigPolicyEncoded OCTET STRING,
  sigPolicyLocalURI IA5String
}

The spDocument shall contain the encoded signature policy document as content of the sigPolicyEncoded element, or an URI to a local store where the present document can be retrieved as sigPolicyLocalURI.

NOTE 1: Contrary to the SPuri, the sigPolicyLocalURI points to a local file.

The spDocSpec shall identify the technical specification that defines the syntax of the signature policy. The SPDocSpecification shall be as defined in clause 5.2.9.2.

NOTE 2: It is the responsibility of the entity adding the signature policy into the signature-policy-store to make sure that the correct document is stored.

NOTE 3: Being an unsigned attribute, the signature-policy-store attribute is not protected by the digital signature. If the signature-policy-identifier attribute is incorporated to the signature and contains in sigPolicyHash the digest value of the signature policy document, any alteration of the signature policy document present within signature-policy-store attribute or within a local store, would be detected by the failure of the digests comparison."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.11 (The content-reference attribute)",
        "testo": (
            "Attributo firmato che deve collegare un elemento SignedData a un altro; deve "
            "essere conforme a ESS (IETF RFC 2634, clausole 1.3.4 e 2.11). E' un "
            "collegamento da un SignedData a un altro, usato per collegare una risposta al "
            "messaggio originale a cui si riferisce o per incorporare per riferimento un "
            "SignedData in un altro."
        ),
        "testo_integrale": (
            """Semantics: The content-reference attribute is a signed attribute.

The content-reference attribute shall link one SignedData element to another.

Syntax: The content-reference attribute shall be as defined in ESS (IETF RFC 2634 [3], clauses 1.3.4 and 2.11).

The content-reference attribute is a link from one SignedData to another. It is used to link a reply to the original message to which it refers, or to incorporate by reference one SignedData into another."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.12 (The content-identifier attribute)",
        "testo": (
            "Attributo firmato che fornisce un identificatore del contenuto firmato, per "
            "quando in seguito si renda necessaria una referenza a quel contenuto (es. "
            "nell'attributo content-reference di altri dati firmati inviati piu' tardi); "
            "deve avere valore ContentIdentifier come definito in ESS (IETF RFC 2634, "
            "clausole 1.3.4 e 2.7). Il content-identifier minimo dovrebbe contenere la "
            "concatenazione di informazioni identificative specifiche dell'utente (come un "
            "nome utente o informazioni di identificazione di materiale di chiave "
            "pubblica), una stringa GeneralizedTime e un numero casuale."
        ),
        "testo_integrale": (
            """Semantics: The content-identifier attribute is a signed attribute.

The content-identifier attribute provides an identifier for the signed content, for use when a reference may be later required to that content; for example, in the content-reference attribute in other signed data sent later.

Syntax: The content-identifier attribute shall have attribute value ContentIdentifier as defined in ESS (IETF RFC 2634 [3], clauses 1.3.4 and 2.7).

The minimal content-identifier attribute should contain a concatenation of user-specific identification information (such as a user name or public keying material identification information), a GeneralizedTime string, and a random number."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.13 (The cms-algorithm-protection attribute)",
        "testo": (
            "Attributo firmato che deve contenere e proteggere l'algoritmo di digest e "
            "l'algoritmo di firma usati; deve essere conforme a IETF RFC 6211."
        ),
        "testo_integrale": (
            """Semantics: The cms-algorithm-protection attribute is a signed attribute.

The cms-algorithm-protection attribute shall contain and protect the digest algorithm and signature algorithm used.

Syntax: The cms-algorithm-protection attribute shall be as defined in IETF RFC 6211 [19])."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.3 (The signature-time-stamp attribute)",
        "testo": (
            "Attributo unsigned che deve incapsulare un token di marca temporale calcolato "
            "sul valore della firma digitale di un firmatario specifico. Deve contenere "
            "esattamente un componente AttributeValue, il valore deve essere un'istanza del "
            "tipo ASN.1 SignatureTimeStampToken e l'attributo deve essere identificato "
            "dall'OID id-aa-signatureTimeStampToken; il valore di messageImprint nel "
            "TimeStampToken deve essere il valore di hash del campo signature (senza tag e "
            "length ASN.1) nel SignerInfo per cui l'attributo e' creato."
        ),
        "testo_integrale": (
            """Semantics: The signature-time-stamp attribute shall be an unsigned attribute.

The signature-time-stamp attribute shall encapsulate one time-stamp token computed on the digital signature value for a specific signer.

Syntax: The signature-time-stamp attribute shall contain exactly one component of AttributeValue type.

The signature-time-stamp attribute value shall be an instance of SignatureTimeStampToken ASN.1 type.

The signature-time-stamp attribute shall be identified by the id-aa-signatureTimeStampToken OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-signatureTimeStampToken OBJECT IDENTIFIER ::= { iso(1) member-body(2)
    us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) id-aa(2) 14 }

SignatureTimeStampToken ::= TimeStampToken

The value of the messageImprint field within the TimeStampToken shall be the hash value of the signature field (without the ASN.1 tag and length) within SignerInfo for which the signature-time-stamp attribute is created.

NOTE: In the case of multiple signatures, it is possible to have a:

  •   signature-time-stamp computed for each and all signers; or

  •   signature-time-stamp on some signers' signatures and none on other signers' signatures."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.4.2.1 (OCSP response types)",
        "testo": (
            "Una OCSP response deve essere incorporata nella firma usando la codifica del "
            "tipo OCSPResponse o del tipo BasicOCSPResponse come definiti nella clausola "
            "4.8.2; il tipo OCSPResponse dovrebbe essere preferito."
        ),
        "testo_integrale": (
            """An OCSP response shall be incorporated into the signature either by using the encoding of the OCSPResponse type or the BasicOCSPResponse type as defined in clause 4.8.2.

The OCSPResponse type should be used."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.4.2.2 (OCSP responses within RevocationInfoChoices)",
        "testo": (
            "Il tipo RevocationInfoChoices deve essere quello definito nella clausola "
            "4.8.2; le OCSP response devono essere incluse nel campo other del tipo "
            "RevocationInfoChoices e dovrebbero essere aggiunte usando la codifica di "
            "OCSPResponse specificata in IETF RFC 5940."
        ),
        "testo_integrale": (
            """The RevocationInfoChoices type shall be as defined in clause 4.8.2.

OCSP responses shall be included within the other field of the RevocationInfoChoices type.

OCSP responses should be added using the encoding of OCSPResponse as specified in IETF RFC 5940 [13]."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.4.3 (CRLs)",
        "testo": (
            "Le Certificate Revocation Lists (CRL) devono essere come definite in IETF "
            "RFC 5280."
        ),
        "testo_integrale": (
            """Certificate Revocation Lists (CRLs) shall be as defined in IETF RFC 5280 [6]."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.2 (The ats-hash-index-v3 attribute)",
        "testo": (
            "Attributo unsigned della firma CMS del token di marca temporale incluso "
            "nell'attributo archive-time-stamp-v3 (clausola 5.5.3), che deve fornire "
            "un'impronta non ambigua dei componenti essenziali di una firma CAdES per la "
            "marca temporale di archiviazione. Deve contenere esattamente un componente "
            "AttributeValue, essere codificato in DER, avere valore istanza del tipo ASN.1 "
            "ATSHashIndexV3 ed essere identificato dall'OID id-aa-ATSHashIndex-v3. Nella "
            "validazione dell'archive-time-stamp-v3 si valida prima l'ats-hash-index-v3 "
            "contenuto, ricalcolando tutti i valori di hash di certificati, informazioni di "
            "revoca e attributi unsigned: solo quelli che corrispondono a un valore di hash "
            "nell'istanza di ATSHashIndexV3 sono protetti dalla marca temporale, e "
            "l'attributo e' invalido se contiene un riferimento il cui valore originale non "
            "e' reperito (voci di certificatesHashIndex, crlsHashIndex o "
            "unsignedAttrValuesHashIndex senza corrispondente istanza). hashIndAlgorithm "
            "deve essere lo stesso algoritmo di hash del message imprint del token di "
            "marca temporale, certificatesHashIndex e crlsHashIndex devono contenere un "
            "valore di hash per ogni istanza, rispettivamente, di CertificateChoices e di "
            "RevocationInfoChoice presenti al momento della richiesta della marca "
            "temporale, senza altri valori, mentre unsignedAttrValuesHashIndex deve "
            "contenere una stringa di ottetti per ogni componente del campo attrValues di "
            "ogni istanza di Attribute nel campo unsignedAttrs, con l'hash della "
            "concatenazione di Attribute.attrType e di una delle istanze di AttributeValue. "
            "Tutti i valori di hash sono calcolati sull'intero componente o sulla "
            "concatenazione dei componenti codificati, inclusi tag, length e value, e le "
            "istanze di OtherCertificateFormat devono essere codificate in DER "
            "preservando la codifica dei campi firmati in otherCert."
        ),
        "testo_integrale": (
            """Semantics: For the purpose of long term availability and integrity of validation data in the context of the present document, the ats-hash-index-v3 attribute shall be an unsigned attribute of the CMS signature of the time-stamp token included in the archive-time-stamp-v3 attribute as defined in clause 5.5.3.

The ats-hash-index-v3 attribute shall provide an unambiguous imprint of the essential components of a CAdES signature for use in the archive time-stamp.

When validating the archive-time-stamp-v3, first the contained ats-hash-index-v3 shall be validated. All the hash values of all of the certificates, revocation information and unsigned attributes are recalculated. Only those which match one of the hash values in the instance of the ATSHashIndexV3 type are known to be protected by the corresponding archive time-stamp. The validation of the archive-time-stamp-v3 requires to have all the original values referenced in the ats-hash-index-v3 attribute. The ats-hash-index-v3 is invalid if it contains a reference for which the original value is not found, i.e.:

  •   a reference represented by an entry in certificatesHashIndex which corresponds to no instance of CertificateChoices within certificates field of the root SignedData;

  •   a reference represented by an entry in crlsHashIndex which corresponds to no instance of RevocationInfoChoice within crls field of the root SignedData; or

  •   a reference represented by an entry in unsignedAttrValuesHashIndex which corresponds to no octet stream resulting from concatenating one of the AttributeValue instances within field Attribute.attrValues and the corresponding Attribute.attrType within one Attribute instance in unsignedAttrs field of the SignerInfo.

Once the ats-hash-index-v3 is validated, the archive-time-stamp-v3 can be validated by recalculating the message imprint in the same way as in the creation of the attribute.

Syntax: The ats-hash-index-v3 attribute shall contain exactly one component of AttributeValue type.

The ats-hash-index-v3 attribute shall be DER encoded (see clause 4.7.1).

The ats-hash-index-v3 attribute value shall be an instance of ATSHashIndexV3 ASN.1 type.

The ats-hash-index-v3 attribute shall be identified by the id-aa-ATSHashIndex-v3 OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ATSHashIndex-v3 OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4)
    etsi(0) cades(19122) attributes(1) 5 }

ATSHashIndexV3 ::= SEQUENCE {
  hashIndAlgorithm                  AlgorithmIdentifier,
  certificatesHashIndex             SEQUENCE OF OCTET STRING,
  crlsHashIndex                     SEQUENCE OF OCTET STRING,
  unsignedAttrValuesHashIndex       SEQUENCE OF OCTET STRING
}

The elements covered by the ats-hash-index-v3 attribute are included in the following ASN.1 SET OF structures: unsignedAttrs, SignedData.certificates, and SignedData.crls, where the SignedData field is the one of the CAdES signature being archive time-stamped.

NOTE 1: The SignedData.crls component (see clause 4.4) can include OCSP and/or CRL revocation information.

The field hashIndAlgorithm shall contain an identifier of the hash algorithm used to compute the hash values contained in certificatesHashIndex, crlsHashIndex, and unsignedAttrValuesHashIndex. This algorithm shall be the same as the hash algorithm used for computing the message imprint included in the time-stamp token enveloped in the archive time-stamp unsigned attribute.

NOTE 2: ETSI TS 119 312 [i.8] provides guidance on the choice of hash algorithms.

The field certificatesHashIndex shall be a sequence of octet strings. Each one shall contain the hash value of one instance of CertificateChoices within the certificates field of the root SignedData. A hash value for every instance of CertificateChoices, as present at the time when the corresponding archive time-stamp is requested, shall be included in certificatesHashIndex. No other hash value shall be included in this field.

The field crlsHashIndex shall be a sequence of octet strings. Each one shall contain the hash value of one instance of RevocationInfoChoice within the crls field of the root SignedData. A hash value for every instance of RevocationInfoChoice, as present at the time when the corresponding archive time-stamp is requested, shall be included in crlsHashIndex. No other hash values shall be included in this field.

NOTE 3: The encoding of certificateHashIndex and crlsHashIndex have the value empty and length zero, if the signature contains, respectively, no corresponding CertificateChoices or RevocationInfoChoice instance.

The field unsignedAttrValuesHashIndex shall be a sequence of octet strings. The sequence shall contain one octet string for every component within the attrValues field in every instance of Attribute contained in the unsignedAttrs field as present at time when the corresponding archive time-stamp is requested. No other octet string shall be included in this field. Each octet string shall contain the hash value of the octets resulting from concatenating the corresponding Attribute.attrType field and one of the instances of AttributeValue within the Attribute.attrValues field.

NOTE 4: The idea is that the unsigendAttrValueHashIndex covers all instances of AttributeValue of all instances of Attribute within the unsignedAttrs field separately so that there is no problem when in the future new attributes or new attribute values are added.

Each of the aforementioned hash values shall be the result of a hash computation on the entire component or the concatenation of the entire encoded components including their tag, length and value octets. Instances of OtherCertificateFormat shall be encoded in DER (see clause 4.7.1), whilst preserving the encoding of any signed field included in the otherCert item.

NOTE 5: Use of the ats-hash-index-v3 attribute makes it possible to add additional certificate / revocation information / unsigned attribute or value within an unsigned attribute within SignedData.certificates / SignedData.crls / unsignedAttrs of the CAdES signature (for instance counter signatures or further archive time-stamps), after an archive time-stamp has been applied to a signature, without invalidating such an archive time-stamp. Its use also allows the inclusion of components required by parallel signatures at a later time.

NOTE 6: In case a countersignature attribute is contained in a signature protected by an ATSv3, the adding of a new countersignature in the same attribute or as a new countersignature attribute is possible. However, the adding of a countersignature as an unsigned attribute to an existing countersignature that is protected by an ATSv3 will break the ATSv3 protection, because it changes the hash of the original countersignature attributed covered by the ats-hash-index-v3 attribute.

NOTE 7: Figure 1 illustrates the computation of the ats-hash-index-v3 and its combination with the ATSv3."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.3 (The archive-time-stamp-v3 attribute)",
        "testo": (
            "Attributo unsigned che deve essere un token di marca temporale del documento "
            "firmato e della firma, inclusi gli attributi firmati e tutti gli altri "
            "componenti essenziali della firma protetti dall'attributo ats-hash-index-v3. "
            "Deve contenere esattamente un componente AttributeValue, il valore deve essere "
            "un'istanza del tipo ASN.1 ArchiveTimeStampToken e l'attributo deve essere "
            "identificato dall'OID id-aa-signatureTimeStampToken (cosi' nel testo ufficiale, "
            "mentre l'ASN.1 copiato definisce id-aa-ets-archiveTimestampV3). L'input per il "
            "calcolo del message imprint e' la concatenazione, nell'ordine indicato, di "
            "SignedData.encapContentInfo.eContentType, degli ottetti che rappresentano "
            "l'hash dei dati firmati, dei campi version, sid, digestAlgorithm, signedAttrs, "
            "signatureAlgorithm e signature del SignerInfo interessato e di una singola "
            "istanza di ATSHashIndexV3 contenuta nell'attributo ats-hash-index-v3; "
            "l'archive-time-stamp-v3 deve includere come attributo unsigned un singolo "
            "ats-hash-index-v3 contenente l'istanza inclusa al punto 4. Prima di "
            "incorporare un nuovo archive-time-stamp-v3 il SignedData deve essere esteso "
            "con i dati di validazione mancanti (in caso di Delta CRL va incluso l'intero "
            "insieme di CRL), secondo due strategie di inclusione a seconda che siano gia' "
            "presenti attributi ATSv2 o forme precedenti di marca temporale di "
            "archiviazione o l'attributo long-term-validation: in tal caso il contenuto di "
            "SignedData.certificates e SignedData.crls non deve essere modificato e il "
            "nuovo materiale va fornito nel TimeStampToken dell'ultima marca temporale di "
            "archiviazione o nell'ultimo attributo long-term-validation, con gli attributi "
            "certificate-values e revocation-values come attributi unsigned del "
            "TimeStampToken; nessun altro attributo oltre ATSv3 o quelli dell'annex B puo' "
            "essere aggiunto a unsignedAttrs, e in validazione tali attributi ATSv3 vanno "
            "validati per primi e poi ignorati per la validazione delle marche temporali "
            "precedenti. Le OCSP response vanno incluse come nella clausola 5.4.2 e, se "
            "incluse in SignedData.crls, come nella clausola 5.4.2.2; ogni nuovo attributo "
            "che include dati di validazione deve essere codificato in DER preservando la "
            "codifica dei campi firmati, l'augmentation deve preservare la codifica binaria "
            "degli attributi unsigned gia' presenti e di ogni componente che contribuisce "
            "all'input del calcolo del message imprint, e i nuovi attributi aggiunti dopo "
            "che la firma e' stata protetta da un ATSv3 dovrebbero essere codificati in DER."
        ),
        "testo_integrale": (
            """Semantics: The archive-time-stamp-v3 attribute shall be an unsigned attribute.

The archive-time-stamp-v3 attribute shall be a time-stamp token of the signed document and the signature, including signed attributes, and all other essential components of the signature as protected by the ats-hash-index-v3 attribute.

Syntax: The archive-time-stamp-v3 attribute shall contain exactly one component of AttributeValue type.

The archive-time-stamp-v3 attribute value shall be an instance of ArchiveTimeStampToken ASN.1 type.

The archive-time-stamp-v3 attribute shall be identified by the id-aa-signatureTimeStampToken OID.

The corresponding definitions shall be as defined in annex D and are copied here for information.

id-aa-ets-archiveTimestampV3 OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4)
    etsi(0) electronic-signature-standard(1733) attributes(2) 4 }

ArchiveTimeStampToken ::= TimeStampToken

The input for the archive-time-stamp-v3's message imprint computation shall be the concatenation (in the order shown by the list below) of the signed data hash (see step 2 below) and certain fields in their binary encoded form without any modification and including the tag, length and value octets:

   1)    The SignedData.encapContentInfo.eContentType.

   2)    The octets representing the hash of the signed data. The hash is computed on the same content that was used for computing the hash value that is encapsulated within the message-digest signed attribute of the CAdES signature being archive-time-stamped. The hash algorithm applied shall be the same as the hash algorithm used for computing the archive time-stamp's message imprint. The hash algorithm identifier should be included in the SignedData.digestAlgorithms set.

   NOTE 1: To validate the archive-time-stamp-v3, the hash of the signed data, as defined in point 2) is needed. In case of detached signatures, the hash can be provided from an external trusted source.

   3)    The fields version, sid, digestAlgorithm, signedAttrs, signatureAlgorithm, and signature within the SignedData.signerInfos's item corresponding to the signature being archive time-stamped, in their order of appearance.

   4)    A single instance of ATSHashIndexV3 type (as defined in clause 5.5.2) contained in the ats-hash-index-v3 attribute.

The archive-time-stamp-v3 shall include as an unsigned attribute a single ats-hash-index-v3 attribute containing the instance included in step 4.

   NOTE 2: The inclusion of the ats-hash-index-v3 unsigned attribute's component in the process that builds the input to the computation of the archive time-stamp's message imprint ensures that all the essential components of the signature (including certificates, revocation information, and unsigned attributes) are protected by the time-stamp.

The items included in the hashing procedure and the concatenation order are shown in figure 1.

   NOTE 3: When validated, an archive-time-stamp-v3 unsigned attribute is a proof of existence at the time indicated in its time-stamp token, of the items that have contributed to the computation of its message imprint. This proof of existence can be used in validation procedures to ensure that signature validation is based on objects that truly existed in the past. This, for example, protects against a private signing key being compromised after the associated public key certificate expires resulting in the signature being considered invalid.

   NOTE 4: Counter-signatures stored in countersignature attributes do not require independent archive time-stamps as they are protected by the archive time-stamp as an unsigned attribute.

Before incorporating a new archive-time-stamp-v3 attribute, the SignedData (see clause 4.4) shall be extended to include any validation data, not already present, which is required for validating the signature being archive time-stamped. Validation data may include certificates, CRLs, OCSP responses, as required to validate any signed object within the signature including the existing signature, counter-signatures, time-stamps, OCSP responses, certificates, attribute certificates and signed assertions. In the case that the validation data contains a Delta CRL, then the whole set of CRLs shall be included to provide a complete revocation list.

   NOTE 5: Validation data already present for example in the time-stamp token need not be included again.

The present document specifies two strategies for the inclusion of validation data, depending on whether attributes for long term availability, as defined in different versions of ETSI TS 101 733 [1], have already been added to the SignedData:

  •   If none of ATSv2 attributes (see clause A.2.4), or an earlier form of archive time-stamp as defined in ETSI TS 101 733 [1] or long-term-validation (see clause A.2.5) attributes is already present in any SignerInfo of the root SignedData, then the new validation material shall be included within the root SignedData.certificates, or SignedData.crls as applicable.

  •   If an ATSv2, or other earlier form of archive time-stamp or a long-term-validation attribute, is present in any SignerInfo of the root SignedData then the root SignedData.certificates and SignedData.crls contents shall not be modified. The new validation material shall be provided within the TimeStampToken of the latest archive time-stamp (which can be an ATSv2 as defined in ETSI TS 101 733 [1], or an ATSv3) or within the latest long-term-validation attribute (defined in ETSI TS 101 733 [1]) already contained in the SignerInfo, by one of the following methods:

      -   the TSU provides the information in the SignedData of the timestamp token;

      -   adding the certificate-values attribute and the revocation-values attribute as unsigned attributes within the TimeStampToken.

   NOTE 6: In the case where an ATSv2, or other earlier form of archive time-stamp or a long-term-validation attribute, is present, once an ATSv3 is added, "the latest archive time-stamp already contained in the SignerInfo" will be of type ATSv3.

If an ATSv2, or other earlier form of archive time-stamp or a long-term-validation attribute, is present then no other attributes than ATSv3 or attributes specified as per annex B shall be added to the unsignedAttrs. During the validation, these ATSv3 attributes or attributes specified as per annex B shall be first validated, and subsequently ignored for the validation of the older archive time-stamp or long-term-validation attributes.

OCSP responses shall be included as defined in clause 5.4.2.

If the OCSP response is included within SignedData.crls, it shall be included as defined in clause 5.4.2.2.

When generating a new attribute to include validation data, either initially when creating the signature or later when augmenting the signature, it shall be encoded in DER (see clause 4.7.1), whilst preserving the encoding of any signed field included in the attribute. The augmentation shall preserve the binary encoding of already present unsigned attributes and any component contributing to the archive time-stamp's message imprint computation input. When adding any new attribute after the signature was protected by an ATSv3, the new attributes should be DER encoded.

   NOTE 7: In case the encoding of any of the elements protected by the ats-hash-index-v3 attribute, is changed, the validation of the ats-hash-index-v3 attribute will fail, because the corresponding hash value is not found. The encoding may change in case of BER encoded elements, which are reencoded.

Figure 1 illustrates the hashing process."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 5.4.1 (Introduction)",
        "testo": (
            "Introduzione alla clausola 5.4 sui dati di validazione: il documento "
            "specifica i diversi luoghi in cui incorporare i dati di validazione mancanti "
            "(rinvio alle clausole 5.5 e A.1 per i dettagli) e, per alcuni tipi di dati di "
            "validazione, le clausole seguenti fissano requisiti aggiuntivi di "
            "incorporamento nella firma. Nessun requisito e nessun soggetto obbligato."
        ),
        "testo_integrale": (
            """The present document specifies different places where to incorporate missing validation data. See clauses 5.5 and A.1 for additional details.

For some types of validation data, the following clauses specify additional requirements when incorporating them into the signature."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.1 (Introduction)",
        "testo": (
            "Introduzione alla clausola 5.5 sulla disponibilita' e integrita' a lungo "
            "termine del materiale di validazione: il documento specifica un attributo "
            "archive-time-stamp che usa l'attributo ats-hash-index-v3 (entrambi unsigned); "
            "l'archive-time-stamp corrisponde a un singolo elemento SignerInfo, incluse "
            "tutte le sue controfirme, e protegge quell'elemento SignerInfo e tutti i dati "
            "del SignedData necessari a validarlo. Disposizione dichiarativa, senza "
            "requisiti ne' soggetto obbligato."
        ),
        "testo_integrale": (
            """The present document specifies an archive-time-stamp attribute that uses the ats-hash-index-v3 attribute. Both attributes are unsigned.

The archive-time-stamp attribute corresponds to a single SignerInfo element, including all its counter signatures. It protects the corresponding SignerInfo element, and all data from the SignedData needed to validate the SignerInfo element."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 5.1.1 (The content-type attribute)",
    "clausola 5.1.2 (The message-digest attribute)",
    "clausola 5.2.1 (The signing-time attribute)",
    "clausola 5.2.2.1 (General requirements)",
    "clausola 5.2.2.2 (ESS signing-certificate attribute)",
    "clausola 5.2.2.3 (ESS signing-certificate-v2 attribute)",
    "clausola 5.2.3 (The commitment-type-indication attribute)",
    "clausola 5.2.4.1 (The content-hints attribute)",
    "clausola 5.2.4.2 (The mime-type attribute)",
    "clausola 5.2.5 (The signer-location attribute)",
    "clausola 5.2.6.1 (The signer-attributes-v2 attribute)",
    "clausola 5.2.6.2 (claimed-SAML-assertion)",
    "clausola 5.2.6.3 (signed-SAML-assertion)",
    "clausola 5.2.7 (The countersignature attribute)",
    "clausola 5.2.8 (The content-time-stamp attribute)",
    "clausola 5.2.9.1 (The signature-policy-identifier attribute)",
    "clausola 5.2.9.2 (The SigPolicyQualifierInfo type)",
    "clausola 5.2.10 (The signature-policy-store attribute)",
    "clausola 5.2.11 (The content-reference attribute)",
    "clausola 5.2.12 (The content-identifier attribute)",
    "clausola 5.2.13 (The cms-algorithm-protection attribute)",
    "clausola 5.3 (The signature-time-stamp attribute)",
    "clausola 5.4.1 (Introduction)",
    "clausola 5.4.2.1 (OCSP response types)",
    "clausola 5.4.2.2 (OCSP responses within RevocationInfoChoices)",
    "clausola 5.4.3 (CRLs)",
    "clausola 5.5.1 (Introduction)",
    "clausola 5.5.2 (The ats-hash-index-v3 attribute)",
    "clausola 5.5.3 (The archive-time-stamp-v3 attribute)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Sette rinvii interni al capitolo, tutti literalmente presenti nel testo citante
# (evidence_type "textual"); i rinvii verso la clausola 4, gli annessi A/B/D e le
# fonti esterne sono elencati nel docstring e restano alla fase 6.
RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.6.1 (The signer-attributes-v2 attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.6.3 (signed-SAML-assertion)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.6.1 (The signer-attributes-v2 attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.6.2 (claimed-SAML-assertion)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.9.1 (The signature-policy-identifier attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.9.2 (The SigPolicyQualifierInfo type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.10 (The signature-policy-store attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.9.2 (The SigPolicyQualifierInfo type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2 (The ats-hash-index-v3 attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (The archive-time-stamp-v3 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The archive-time-stamp-v3 attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2 (The ats-hash-index-v3 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The archive-time-stamp-v3 attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.2.2 (OCSP responses within RevocationInfoChoices)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from seed_data.lib import verifica_completezza_testo_integrale, verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    verifica_completezza_testo_integrale([sys.modules[__name__]])
    print(
        f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
        f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti, "
        f"{len(RELAZIONI)} relazioni."
    )
