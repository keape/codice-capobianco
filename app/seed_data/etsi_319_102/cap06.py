"""Estrazione granulare ETSI EN 319 102-1 V1.4.1 (2024-06) — Capitolo 6: clausola
5.5 (Validation process for Signatures with Time and Signatures with Long-Term
Validation Material), sottoclausole 5.5.1 (Description), 5.5.2 (Inputs),
5.5.3 (Outputs), 5.5.4 (Processing).

Fonte 27 del lotto eIDAS2 (la numerazione degli id e' risolta per riferimento
dalla sessione principale in app/seed.py — questo modulo NON tocca seed.py).
Testo ufficiale in app/.source_cache/etsi_319_102/cap06.txt (estratto dal PDF
con pdftotext -layout). Manifest di split:
app/.source_cache/etsi_319_102/manifest.json.

Copertura (ADR-0007) — cosa genera un nodo e cosa no:
- La clausola 5.5 e' una intestazione di puro raggruppamento (solo titolo,
  seguito immediatamente dalla sottoclausola 5.5.1, senza alcun periodo
  proprio): non genera nodo ne' item di indice, come da criterio di copertura.
- Le quattro sottoclausole 5.5.1, 5.5.2, 5.5.3, 5.5.4 hanno contenuto proprio
  -> 4 item di indice, 4 nodi (2 Obblighi, 2 Principi).
- I passi numerati 1)-11) della clausola 5.5.4 e le relative NOTE 1-10 NON
  generano nodi a se': non sono clausole/sottoclausole numerate ma l'articolazione
  interna di una sola clausola, dello stesso genere delle sotto-liste a)/b)/c)
  assorbite nel nodo del requisito chapeau in ETSI EN 319 401 (cap03) e in
  ETSI EN 319 421. L'unita' di censimento di questo testo e' il numero di
  clausola: EN 319 102-1 non assegna ai propri requisiti alcun id proprio
  (nessun prefisso REQ-/SCP-/SVP-), quindi l'identita' del nodo puo' essere
  solo la clausola che li contiene (stesso caso di ETSI TS 119 312, citato
  come precedente in ETSI TS 119 101 cap03). L'intero algoritmo — passi 1)-11),
  NOTE 1-10 comprese, e le indicazioni di stato/sotto-indicazione che il
  processo deve restituire — e' riportato verbatim in `testo_integrale` del
  nodo di 5.5.4.
- La Tabella 20 (Inputs to validation of signatures with time) e' contenuto
  della clausola 5.5.2 che la contiene: ricostruita riga per riga nel suo
  `testo_integrale` (intestazione "| Input | Requirement |" + una riga per
  ciascuno degli 8 input, tutti conservati: Signed Data Object Mandatory; gli
  altri sette Optional), senza perdere alcun valore; stesso formato di tabella
  adottato dal capitolo 5 di questa fonte per le Tabelle 18 e 19.

Classificazione (regola shall -> Obbligo / dichiarativo -> Principio):
- 5.5.2 (Inputs) -> Obbligo "tecnico/sicurezza", soggetto QTSP/gestore
  obbligato: la Tabella 20 fissa quali input il processo di convalida
  richiede (Mandatory) e quali ammette (Optional) e il corpo della clausola
  prescrive alla DA come trattare il parametro di indicazione temporale
  ("it has to extract the value prior to calling the validation processes").
  Stesso trattamento riservato ai campi con "Presence: This field shall be
  present" di ETSI TS 119 612 (cap03): una tabella di presenza/obbligatorieta'
  e' un requisito di conformazione tecnica, non una descrizione.
- 5.5.3 (Outputs) -> Principio "altro": descrive l'output del processo
  ("is a status indicating ...", "may be accompanied by") senza imporre un
  comportamento a un soggetto.
- 5.5.4 (Processing) -> Obbligo "procedurale", soggetto QTSP/gestore
  obbligato. La clausola e' una sequenza ordinata di passi, con regole di
  confronto fra tempi e di prosecuzione/arresto dell'algoritmo ("shall go to
  the next step", "shall return the indication ..."): e' la categoria
  "procedurale" del criterio gia' applicato in ETSI TS 119 101 cap03
  (controlli su passi, sequenze e regole di processo), non "tecnico/sicurezza"
  che quel capitolo riserva alle proprieta' crittografiche in senso stretto.
  Il soggetto obbligato e' QTSP/gestore per la stessa ragione per cui TS 119 101
  cap03 (policy delle APPLICAZIONI di firma, non del prestatore) assegna a
  QTSP/gestore il ruolo di obbligato: e' il soggetto che implementa, fornisce
  o gestisce il processo/componente di convalida (qui l'SVA e i suoi building
  block). Nessun destinatario valorizzato in questo capitolo: il testo non
  beneficia espressamente un soggetto diverso dall'obbligato (l'uso che la DA
  fa del risultato e' dichiarato fuori perimetro dalla NOTE 8).
- 5.5.1 (Description) -> Principio "scopo/ambito di applicazione", come le
  omologhe clausole "Description" 5.3.1 e 5.4.1 nel capitolo 5 di questa
  fonte: la clausola non impone comportamenti, dichiara quale processo di
  convalida disciplina e a quali casi si applica, estendendo espressamente le
  procedure a ogni convalida che tenga conto di fattori temporali scelti dalla
  relying party ("The procedures are not limited to signatures containing
  time-stamps. They are equally applicable to any validation where relying
  party chosen time factors ... are taken into account."). Nota: e' un
  perimetro di applicazione della procedura, non lo scopo del documento
  (quello e' la clausola 1, censita nel capitolo 1).

Convenzioni di trascrizione di `testo_integrale` (nessuna parola rimossa; il
testo e' stato confrontato con cap06.txt normalizzando spazi e separatori di
tabella):
- i wrap fisici di riga introdotti da pdftotext -layout sono ricomposti in
  paragrafi, uno per capoverso/voce di elenco;
- le righe di paratesto di pagina del PDF (footer "ETSI" e numero di pagina
  con il carattere di controllo di cambio pagina) sono rimosse;
- ciascun `testo_integrale` si apre con la riga di intestazione della propria
  clausola (es. "5.5.4 Processing"), come nei capitoli gia' censiti degli
  altri standard ETSI: rende il nodo leggibile senza risalire al riferimento;
- nel testo convertito i tre bullet interni al passo 3)b) sono resi con il
  glifo di elenco della scheda a codice privato U+F0A7: marcatore di elenco
  privo di contenuto testuale, reso qui come "-", senza alterare alcuna
  parola.

RELAZIONI = [] per vincolo esplicito di fase: nessuna relazione, ne' interna
al capitolo ne' cross-capitolo ne' cross-fonte (nemmeno verso eIDAS o verso
gli altri standard ETSI citati nel testo, es. IETF RFC 3161). Il
collegamento e' demandato alla fase dedicata (ADR-0009), gestita dalla
sessione principale.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "clausola 5.5.2 (Inputs)",
        "testo": (
            "Input del processo di convalida delle firme con tempo (Tabella 20): il Signed Data Object e'"
            " obbligatorio; sono opzionali l'indicazione temporale di esistenza della firma, il documento del"
            " firmatario (Signer's Document o SDR), la lista dei trust anchor (es. TSL), le politiche di convalida"
            " della firma (Signature Validation Policies), la configurazione locale, il certificato di firma e i"
            " dati di convalida del certificato. L'indicazione temporale di esistenza della firma (time indication"
            " for signature existence) e' un valore di tempo fornito dalla DA alla SVA come indicazione di un"
            " momento in cui la DA sa o presume che la firma sia esistita: la DA puo' usarla per inizializzare la"
            " variabile interna best-signature-time quando la politica richiede di usare l'attributo claimed signing"
            " time come indicazione effettiva del momento di firma, o quando ha prove che la firma esisteva a quel"
            " momento; se vuole usare l'indicazione contenuta nell'attributo claimed signing time deve estrarne il"
            " valore prima di invocare i processi di convalida, oppure istruire la SVA a usare il claimed signing"
            " time come indicazione temporale se l'attributo e' presente e la funzione e' fornita dalla SVA; possono"
            " essere passate anche altre indicazioni temporali dichiarate (es. quella riferita da un notaio o da un"
            " altro testimone)."
        ),
        "testo_integrale": (
            "5.5.2 Inputs\n"
            "Table 20: Inputs to validation of signatures with time\n"
            "\n"
            "| Input | Requirement |\n"
            "|---|---|\n"
            "| Signed Data Object | Mandatory |\n"
            "| time indication for signature existence | Optional |\n"
            "| Signer's Document or SDR | Optional |\n"
            "| Trust anchor list (e.g. TSL) | Optional |\n"
            "| Signature Validation Policies | Optional |\n"
            "| Local configuration | Optional |\n"
            "| Signing Certificate | Optional |\n"
            "| Certificate Validation Data | Optional |\n"
            "\n"
            "The time indication for signature existence parameter is a time value which is provided by the DA to the SVA as an indication for a time the DA knows, or assumes, the signature has existed.\n"
            "NOTE 1: In the physical world, the date of signing contained in the document itself or affixed to the written signature can be accepted as prima facie evidence for the date of signing. An equivalent in the digital world is the claimed signing time attribute (see clause 4.2.5.8), which is (in general) not coming from a trusted source and therefore has only prima facie value as date of signing. The DA can use the time indication for signature existence parameter to provide an initialization of the internal best-signature-time whenever the policy requires to use the claimed signing time attribute as an actual indication of the signing time, or when the DA has proofs that the signature existed at that time.\n"
            "NOTE 2: If the DA wants to use the time indication included in a claimed signing time attribute, it has to extract the value prior to calling the validation processes. If the DA is not able to do the extraction itself, it can instruct the SVA to use the claimed signing time as a time indication, if the claimed signing time attribute is present and the feature is provided by the SVA.\n"
            "NOTE 3: Other claimed time indications can be passed through the time indication for signature existence parameter, e.g. a time indication reported by a natural person as a public notary or another witness.\n"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.5.4 (Processing)",
        "testo": (
            "Algoritmo del processo di convalida delle firme con tempo, in 11 passi: 1) inizializzare l'insieme dei"
            " token di marca temporale di firma (signature time-stamp) dagli attributi signature time-stamp della"
            " firma e inizializzare best-signature-time all'indicazione temporale di esistenza della firma fornita"
            " in input, o all'ora corrente se la DA non ha usato tale parametro; 2) eseguire la convalida della"
            " firma di base secondo la clausola 5.3 con tutti gli input, incluso il passaggio del materiale di"
            " convalida a lungo termine se la firma lo contiene; si prosegue solo se la convalida ritorna PASSED,"
            " INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE, INDETERMINATE/REVOKED_NO_POE,"
            " INDETERMINATE/REVOKED_CA_NO_POE, INDETERMINATE/TRY_LATER, INDETERMINATE/OUT_OF_BOUNDS_NO_POE o"
            " INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED, altrimenti il processo restituisce stato e informazioni"
            " ricevuti dalla convalida di base; 3) convalida delle marche temporali di firma: a) per ciascun token"
            " verificare che il message imprint sia stato generato secondo la specifica del formato di firma"
            " corrispondente, rimuovendo il token dall'insieme in caso di fallimento; b) per ciascun token residuo"
            " eseguire la convalida della marca temporale secondo la clausola 5.4 — se ritorna PASSED e il"
            " generation time e' anteriore a best-signature-time, aggiornare best-signature-time a quel tempo e"
            " passare al token successivo; negli altri casi, se nessun vincolo specifico impone la validita'"
            " dell'attributo, rimuovere il token e passare al successivo, altrimenti restituire"
            " indicazione/sotto-indicazione e spiegazioni ricevute; 4) confronto dei tempi: a) se il passo 2) ha"
            " restituito INDETERMINATE/REVOKED_NO_POE o REVOKED_CA_NO_POE e il revocation time e' posteriore a"
            " best-signature-time, allora FAILED/NOT_YET_VALID se best-signature-time e' anteriore alla data di"
            " emissione del certificato di firma, passo 4)e) se e' anteriore alla data di scadenza, altrimenti"
            " INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED; se il revocation time non e' posteriore, restituire"
            " INDETERMINATE con la stessa sotto-indicazione; b) se il passo 2) ha restituito PASSED o"
            " INDETERMINATE/OUT_OF_BOUNDS_NO_POE: FAILED/NOT_YET_VALID se best-signature-time e' anteriore"
            " all'emissione del certificato, altrimenti passo 4)e) se l'indicazione era PASSED, oppure"
            " restituzione di indicazione e sotto-indicazione del passo 2); c) se il passo 2) ha restituito"
            " INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE e il materiale interessato e' il valore di firma o"
            " un attributo firmato: proseguire con 4)e) se gli algoritmi interessati erano ancora considerati"
            " affidabili a best-signature-time, altrimenti restituire"
            " INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE; d) se il passo 2) ha restituito"
            " INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED: FAILED/NOT_YET_VALID se best-signature-time e' anteriore"
            " all'emissione del certificato, passo 4)e) se e' anteriore alla scadenza, altrimenti"
            " INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED; e) per ciascun token residuo verificare la coerenza dei"
            " tempi indicati: devono essere posteriori ai tempi indicati in qualunque content-time-stamp e si"
            " applicano le regole di IETF RFC 3161, clausola 2.4.2, sull'ordine dei token generati dalla stessa o"
            " da diverse TSA in base ai campi accuracy e ordering del TSTInfo, salvo diversa previsione dei"
            " vincoli di convalida della firma; in caso di esito negativo restituire"
            " INDETERMINATE/TIMESTAMP_ORDER_FAILURE; 5) gestione del ritardo della marca temporale (time-stamp"
            " delay): se i vincoli di convalida specificano un ritardo e non c'e' alcuna proprieta'/attributo"
            " signing-time, restituire INDETERMINATE/SIG_CONSTRAINTS_FAILURE; se presente, verificare che il tempo"
            " dichiarato piu' il ritardo sia successivo a best-signature-time, altrimenti restituire"
            " INDETERMINATE/SIG_CONSTRAINTS_FAILURE; 6) se il passo 2) ha restituito INDETERMINATE/TRY_LATER"
            " perche' i dati di revoca non erano sufficientemente freschi, eseguire il Revocation Freshness"
            " Checker (clausola 5.2.5) con i dati di stato di revoca restituiti dal passo 2), il certificato di"
            " cui si verifica lo stato e best-signature-time: se ritorna PASSED proseguire, altrimenti restituire"
            " INDETERMINATE/TRY_LATER e, se fornito dal checker, il suggerimento su quando ritentare la convalida;"
            " 7) se il passo 2) ha restituito INDETERMINATE/TRY_LATER perche' il certificato risulta sospeso: se"
            " best-signature-time e' anteriore al momento della sospensione proseguire al passo 8), altrimenti"
            " restituire INDETERMINATE/TRY_LATER con il suggerimento su quando ritentare la convalida; 8) eseguire"
            " il processo di Signature Acceptance Validation secondo la clausola 5.2.8 con i Signed Data Object,"
            " best-signature-time come parametro di tempo di convalida e i vincoli crittografici (Cryptographic"
            " Constraints); 9) se la Signature Acceptance Validation ritorna PASSED proseguire al passo successivo,"
            " altrimenti restituire indicazione e sotto-indicazione ricevute; 10) applicare i vincoli crittografici"
            " a tutti i certificati e alle informazioni di stato di revoca usati nella convalida rispetto all'ora"
            " corrente: se non rispettano i vincoli, restituire INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE"
            " con l'elenco degli algoritmi e delle dimensioni di chiave interessati e il tempo fino al quale"
            " ciascun algoritmo e' stato considerato sicuro dai vincoli crittografici, altrimenti proseguire; 11)"
            " estrazione dei dati: restituire l'indicazione di successo PASSED, la catena di certificati ottenuta"
            " al passo 2) e best-signature-time, e dovrebbe restituire anche le informazioni aggiuntive estratte"
            " dalla firma e/o usate dai passi intermedi, in particolare i risultati intermedi di convalida dei"
            " token di marca temporale."
        ),
        "testo_integrale": (
            "5.5.4 Processing\n"
            "1)    The process shall initialize the set of signature time-stamp tokens from the signature time-stamp attributes present in the signature and shall initialize the best-signature-time to the time indication for signature existence value provided as input, or the current time when this parameter has not been used by the DA.\n"
            "NOTE 1: Best-signature-time is an internal variable for the algorithm denoting the earliest time when it can be trusted by the SVA (either because proven by some POE present in the signature or passed by the DA and for this reason assumed to be trusted) that a signature has existed.\n"
            "2)    Signature validation: the process shall perform the validation process for Basic Signatures as per clause 5.3 with all the inputs, including the processing of any signed attributes as specified. If the Signature contains long-term validation material, this material shall be passed to the validation process for Basic Signatures.\n"
            "If this validation returns PASSED, INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE, INDETERMINATE/REVOKED_NO_POE, INDETERMINATE/REVOKED_CA_NO_POE, INDETERMINATE/TRY_LATER, INDETERMINATE/OUT_OF_BOUNDS_NO_POE or INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED, the SVA shall go to the next step. Otherwise, the process shall return the status and information returned by the validation process for Basic Signatures.\n"
            "NOTE 2: The process in the case INDETERMINATE/REVOKED_NO_POE or INDETERMINATE/REVOKED_CA_NO_POE is continued, because a proof that the signing occurred before the revocation date can help to go from INDETERMINATE to TOTAL-PASSED (step 4)a).\n"
            "NOTE 3: The process in the case PASSED or INDETERMINATE/OUT_OF_BOUNDS_NO_POE is continued, because a proof that the signing occurred before the beginning of the validity (notBefore) of the signing certificate can help to go to TOTAL-FAILED (step 4)b).\n"
            "NOTE 4: The process in the case INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE is continued, because a proof that the signing occurred before the time one of the algorithms used was no longer considered secure can help to go from INDETERMINATE to TOTAL-PASSED (step 4)c).\n"
            "NOTE 5: The process in the case INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED is continued, because a proof that the signing occurred before the expiration date can help to go from INDETERMINATE to TOTAL-PASSED (step 4)d).\n"
            "3)   Signature time-stamp validation:\n"
            "a)    For each time-stamp token in the set of signature time-stamp tokens, the process shall check that the message imprint has been generated according to the corresponding signature format specification. If the verification fails, the process shall remove the token from the set.\n"
            "b)    Time-stamp token validation: For each time-stamp token remaining in the set of signature time-stamp tokens, the process shall perform the time-stamp validation process as per clause 5.4:\n"
            "-     If PASSED is returned and if the returned generation time is before best-signature-time, the process shall set best-signature-time to this time and shall try the next token.\n"
            "In all other cases:\n"
            "-     If no specific constraints mandating the validity of the attribute are specified in the validation constraints, the process shall remove the time-stamp token from the set of signature time-stamp tokens and shall try the next token.\n"
            "-     Otherwise, the process shall return the indication/sub-indication and associated explanations returned from the Time-stamp token validation process.\n"
            "4)   Comparing times:\n"
            "a)    If step 2) returned the indication INDETERMINATE with the sub-indication REVOKED_NO_POE or REVOKED_CA_NO_POE:\n"
            "a.    If the returned revocation time is posterior to best-signature-time, then:\n"
            "i.     If best-signature-time is before the issuance date of the signing certificate, the process shall return the indication FAILED with the sub-indication NOT_YET_VALID.\n"
            "ii.    If best-signature-time is before the expiration date of the signing certificate, the process shall perform step 4)e).\n"
            "iii.   Otherwise, the process shall return the indication INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED.\n"
            "b.    Otherwise, the process shall return the indication INDETERMINATE with the sub-indication REVOKED_NO_POE or REVOKED_CA_NO_POE, respectively.\n"
            "b)    If step 2) returned the indication PASSED or the indication INDETERMINATE with the sub-indication OUT_OF_BOUNDS_NO_POE: If best-signature-time is before the issuance date of the signing certificate, the process shall return the indication FAILED with the sub-indication NOT_YET_VALID. Otherwise:\n"
            "a.    If the returned indication was PASSED, the process shall continue with step 4)e);\n"
            "b.    Else, the process shall return the indication and sub-indication which was returned by step 2).\n"
            "c)    If step 2) returned the indication INDETERMINATE with the sub-indication CRYPTO_CONSTRAINTS_FAILURE_NO_POE and the material concerned by this failure is the signature value or a signed attribute: If the algorithm(s) concerned were still considered reliable at best-signature-time, the process shall continue with step 4)e). Otherwise, the process shall return the indication INDETERMINATE with the sub-indication CRYPTO_CONSTRAINTS_FAILURE_NO_POE.\n"
            "d)    If step 2) returned the indication INDETERMINATE with the sub-indication OUT_OF_BOUNDS_NOT_REVOKED: If best-signature-time is before the issuance date of the signing certificate, the process shall return the indication FAILED with the sub-indication NOT_YET_VALID. Otherwise:\n"
            "a.    If best-signature-time is before the expiration date of the signing certificate, the process shall perform step 4)e).\n"
            "b.    Else, the process shall return the indication INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED.\n"
            "e)    For each time-stamp token remaining in the set of signature time-stamp tokens, the process shall check the coherence in the values of the times indicated in the time-stamp tokens. They shall be posterior to the times indicated in any time-stamp token computed on the signed data (content-time-stamp). The process shall apply the rules specified in IETF RFC 3161 [3], clause 2.4.2 regarding the order of time-stamp tokens generated by the same or different TSAs given the accuracy and ordering fields' values of the TSTInfo field, unless stated differently by the signature validation constraints. If all the checks end successfully, the process shall go to the next step. Otherwise the process shall return the indication INDETERMINATE with the sub-indication TIMESTAMP_ORDER_FAILURE.\n"
            "5)   Handling Time-stamp delay: If the signature contains a signature time-stamp token and the validation constraints specify a time-stamp delay:\n"
            "a)    If no signing-time property/attribute is present, the process shall return the indication INDETERMINATE with the sub-indication SIG_CONSTRAINTS_FAILURE.\n"
            "b)    If a signing-time property/attribute is present, the process shall check that the claimed time in the attribute plus the time-stamp delay is after the best-signature-time. If the check is successful, the process shall go to the next step. Otherwise, the process shall return the indication INDETERMINATE with the sub-indication SIG_CONSTRAINTS_FAILURE.\n"
            "6)   If step 2) returned the indication INDETERMINATE with the sub-indication TRY_LATER because the revocation data contained revocation status information that was not fresh enough: the building block shall run the Revocation Freshness Checker (clause 5.2.5) with the revocation status data returned in step 2), the certificate for which the revocation status is being checked and best-signature-time. If the checker returns PASSED, the building block shall go to the next step. Otherwise, the building block shall return the indication INDETERMINATE, the sub-indication TRY_LATER and, if returned from the Revocation Freshness Checker, the suggestion for when to try the validation again.\n"
            "7)   If step 2) returned the indication INDETERMINATE with the sub-indication TRY_LATER because the certificate has been found to be suspended:\n"
            "a)    If best-signature-time is before the time of suspension of the certificate: the process shall go to the step 8).\n"
            "b)    Otherwise, the building block shall return the indication INDETERMINATE, the sub-indication TRY_LATER and a suggestion on when to try the validation gain, if returned by the validation process in step 2).\n"
            "8)   The SVA shall perform the Signature Acceptance Validation process as per clause 5.2.8 with the following inputs:\n"
            "a)    The Signed Data Object(s).\n"
            "b)    Best-signature-time as the validation time parameter.\n"
            "c)    The Cryptographic Constraints.\n"
            "NOTE 6: This check has been performed already in step 2) as part of basic signature validation for current time but is repeated here for the earliest time the signature is known to have existed to e.g. check if the algorithms were reliable at that time. Signature elements constraints have already been dealt with in step 2) and need not be rechecked.\n"
            "9)    If the Signature Acceptance Validation process returns PASSED, the SVA shall go to the next step. Otherwise, the SVA shall return the indication and sub-indication returned by the Signature Acceptance Validation Process.\n"
            "10) The SVA shall apply the cryptographic constraints to all the certificates and revocation status information used in the validation process against the current time. If any of those certificates or revocation status information do not match these constraints, the SVA shall return the indication INDETERMINATE with the sub-indication CRYPTO_CONSTRAINTS_FAILURE_NO_POE together with the list of algorithms and key sizes, if applicable, that are concerned and the time for each of the algorithms up to which the respective algorithm has been considered secure by the cryptographic constraints. Otherwise, the SVA shall go to the next step.\n"
            "NOTE 7: The cryptographic constraints have already been applied in step 8) however the validation time parameter in step 8) is best-signature-time. Considering that best-signature-time is not, in general, a POE for the certificate and revocation status information it is necessary to apply the cryptographic constraints for those data at current time. In some cases, best-signature-time can provide an indirect POE on some certificates (e.g. the signing certificate) however this process is not designed to handle indirect POEs. Indirect POEs are handled by the validation process for Signatures providing Long Term Availability and Integrity of Validation Material specified in clause 5.6, through the POE extraction building block specified in clause 5.6.2.3.\n"
            "11) Data extraction: the process shall return the success indication PASSED, the certificate chain obtained in step 2) and best-signature-time. In addition, the process should return additional information extracted from the signature and/or used by the intermediate steps. In particular, the process should return intermediate results such as the validation results of any signature time-stamp token.\n"
            "NOTE 8: What the DA does with this information is out of the scope of the present document.\n"
            "NOTE 9: In the algorithm above, the signature-time-stamp protects the signature against the revocation of the signing certificate (step 4)a) but not always against expiration. The latter case can require validating the signing certificate in the past (see clause 5.6) because not all CAs provide revocation data for expired certificates or are willing to revoke certificates after expiration.\n"
            "NOTE 10: When the algorithm above terminates, best-signature-time indicates the earliest time at which the existence of the signature can be proven using the procedures specified by this algorithm. It is possible that other procedures, such as those specified in the present document for the Validation Process of Signatures providing Long Term Availability and Integrity of Validation Material (see clause 5.6.3), can determine a earlier time at which the existence of the signature can be proven.\n"
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 5.5.1 (Description)",
        "testo": (
            "La clausola descrive un processo di convalida per le firme in cui i fattori temporali possono incidere"
            " sulla convalida, incluse le Signatures with Time definite alla clausola 4.3.3 e le Signatures with"
            " Long-Term Validation Material definite alla clausola 4.3.4: queste ultime differiscono dalle"
            " Signatures with Time perche' contengono materiale di convalida aggiuntivo utilizzabile durante la"
            " convalida, ma i due processi di convalida sono identici. Le procedure non sono limitate alle firme"
            " contenenti marche temporali: si applicano ugualmente a qualunque convalida in cui si tenga conto di"
            " fattori temporali scelti dalla relying party (ora corrente oppure indicazione di tempo della Driving"
            " Application)."
        ),
        "testo_integrale": (
            "5.5.1 Description\n"
            "This clause describes a validation process for signatures where timing factors can affect the validation, including Signatures with Time as defined in clause 4.3.3 and Signatures with Long-Term Validation Material as defined in clause 4.3.4. Signatures with Long-Term Validation Material differ from Signatures with Time by the fact that they contain additional validation material that can be used during validation. The validation processes are identical.\n"
            "NOTE:      The procedures are not limited to signatures containing time-stamps. They are equally applicable to any validation where relying party chosen time factors (current time or Driving Application time indication) are taken into account.\n"
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.5.3 (Outputs)",
        "testo": (
            "L'output principale della convalida della firma e' uno stato che indica la validita' della firma"
            " insieme al piu' antico momento provato in cui la firma e' esistita (earliest time proven that the"
            " signature has existed) e alla catena di certificati usata per la convalida, se applicabile; tale"
            " stato puo' essere accompagnato da informazioni aggiuntive (clausola 5.1.3)."
        ),
        "testo_integrale": (
            "5.5.3 Outputs\n"
            "The main output of the signature validation is a status indicating the validity of the signature together with the earliest time proven that the signature has existed as well as the certificate chain used for validation, if applicable. This status may be accompanied by additional information (see clause 5.1.3).\n"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 5.5.1 (Description)",
    "clausola 5.5.2 (Inputs)",
    "clausola 5.5.3 (Outputs)",
    "clausola 5.5.4 (Processing)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
