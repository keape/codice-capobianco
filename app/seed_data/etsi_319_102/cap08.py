"""ETSI EN 319 102-1 V1.4.1 (2024-06) - Electronic Signatures and
Infrastructures (ESI); Procedures for Creation and Validation of AdES Digital
Signatures; Part 1: Creation and Validation. Capitolo 8: annessi informativi
A-D. Testo ufficiale in app/.source_cache/etsi_319_102/cap08.txt; manifest di
split in app/.source_cache/etsi_319_102/manifest.json. La numerazione degli id
e' risolta per riferimento dalla sessione principale: questo modulo NON tocca
app/seed.py.

PERIMETRO E GRANULARITA' (ADR-0007). Un nodo per ogni clausola/sottoclavola
numerata con contenuto proprio. Questo capitolo copre 12 righe, tutte Principi
(tipo "altro"), 0 Obblighi:

  Annex A.1 (General remarks and assumptions)
  Annex A.2 (Symbols)
  Annex A.3.1 (Introduction)
  Annex A.3.2 (Basic signature validation)
  Annex A.3.3 (Validating a Signature with Time)
  Annex A.3.4 (Example 2: Revoked CA certificate)
  Annex A.3.5 (Basic signature validation)
  Annex A.3.6 (Validation of a Signature with Time)
  Annex A.3.7 (Long-Term Validation)
  Annex B (Signature Classes and AdES Signatures)
  Annex C.1 (Applicability checking)
  Annex C.2 (Format conformance)

Nessun Obbligo in tutto il capitolo: gli annessi A-D sono informativi e nessuno
usa "shall"/"should"/"is required to"/"is recommended to" con un destinatario
individuabile. Gli esempi di convalida (A) sono descrizioni di esecuzione
dell'algoritmo su casi concreti, coniugate al presente descrittivo; B e' una
tabella di corrispondenza tra classi e livelli; C distingue la convalida dal
controllo di applicabilita'/conformita'. Categoria soggetto: nessuna, in
nessuna riga (i destinatari eventualmente impliciti, es. l'implementatore di
una SVA, non sono una categoria di soggetto del censimento).

SCELTE DI MODELLAZIONE NON OVVIE.

- Intestazioni di puro raggruppamento, nessun nodo e nessun item di indice:
  "Annex A (informative): Validation examples" (seguita immediatamente da
  A.1), "Annex C (informative): Applicability rules checking and format
  conformance check" (seguita immediatamente da C.1) e "A.3 Example 1:
  Revoked certificate" (seguita immediatamente da A.3.1). Portano solo la
  titolazione, che e' incorporata nel riferimento del primo nodo.
- A.3.4 e' numerata come sottoclavola di A.3 ma e' titolata "Example 2:
  Revoked CA certificate": anomalia di numerazione dello standard (il secondo
  esempio e' formalmente annidato sotto il primo). Riprodotta fedelmente nel
  riferimento, senza rinumerare nulla; ha contenuto proprio (cronologia t0-t9
  e assunzione sul certificato TSA), quindi resta un nodo.
- A.3.5 e A.3.6 portano lo stesso titolo di A.3.2 e A.3.3 ("Basic signature
  validation", "Validation of a Signature with Time") ma su un caso diverso
  (revoca del certificato della CA invece del certificato di firma): restano
  nodi distinti perche' numerati distintamente e con esito diverso
  (INDETERMINATE/REVOKED_CA_NO_POE). Il numero nel riferimento li disambigua.
- Annex A.2 (Symbols): il contenuto testuale e' una sola frase piu' la
  didascalia della figura (il disegno dei simboli non e' testo): e' comunque
  contenuto proprio della clausola, quindi genera un nodo.
- Annex C.2 contiene enunciati con effetto di vincolo ("implementations
  conforming to the present document cannot include conformance checking in
  the status indication", "An SVA indicating a TOTAL-FAILED or INDETERMINATE
  result just because of a failed conformance check will not be conformant to
  the present document"), ma nessuno dei marcatori prescrittivi della regola
  di classificazione ("shall", "should", "is required to", "is recommended
  to") e nessun destinatario che sia una categoria di soggetto del
  censimento: sono enunciati che definiscono cosa significa essere conformi
  al documento (perimetro dello standard) dentro un annesso informativo.
  Modellati quindi come Principio "altro", non come Obbligo. Se una
  revisione futura volesse leggerli come prescrizione, il nodo e' uno solo e
  il cambio di tipo e' localizzato.
- Esclusi, come paratesto editoriale: la sezione finale "History" / "Document
  history" (tabella delle edizioni pubblicate) e l'Annex D (informative)
  "Change history" (registro di versioni e change request, dal V1.1.1 del
  maggio 2016 al V1.4.1 del giugno 2024, senza prescrizioni, principi o
  soggetti). Stesso trattamento sistematico riservato a "Change history" /
  "History" dagli altri moduli ETSI di questo censimento (EN 319 401 cap05,
  EN 319 412-1 parte1, TS 119 431-1 cap02, TS 119 431-2 cap02, TS 119 432
  cap05/cap07, EN 319 421 cap06), su decisione esplicita della sessione
  principale. La clausola 2 (References) non cade in questo file: e' nel
  capitolo 1 ed e' comunque esclusa come bibliografia.
- I rimandi testuali alle clausole della parte normativa (clausola 5.3, 5.4,
  5.5, 5.6, 5.6.2.3, 5.6.2.4, 4.3) e alle specifiche AdES-Formats (ETSI EN
  319 122-1/-2, 319 132-1/-2, 319 142-1/-2) restano nel corpo dei
  `testo_integrale` senza generare relazioni: in questa fase `RELAZIONI` e'
  vuota per vincolo di consegna, i collegamenti li costruisce la sessione
  principale (ADR-0009).
- Le tabelle esempio di A.3.7 (Table A.3.7-1, -2, -3) sono contenuto della
  clausola e stanno per intero in `testo_integrale`, ricostruite riga per
  riga in formato Markdown (una riga per record, due colonne "Content" /
  "Exists at time").

TESTO VERBATIM (ADR-0010). `testo_integrale` e' la copia letterale integrale
della clausola in inglese, con la sola normalizzazione degli spazi di
impaginazione: righe del PDF ricomposte con uno spazio singolo, marcatori di
pagina ("ETSI", numero di pagina, "ETSI EN 319 102-1 V1.4.1 (2024-06)")
esclusi perche' paratesto, rientri logici conservati e resi con
indentazione/deguenza. Punti di attenzione della conversione, risolti in
ricostruzione senza togliere parole:

- le pseudo-tabelle "Expected result / Rationale" di A.3.2, A.3.3, A.3.5,
  A.3.6 e A.3.7 sono rese come due righe etichettate ("Expected result: <esito>"
  e "Rationale: <motivazione>"), perche' la conversione le rende come testo
  incolonnato su piu' righe;
- Table B.1 e' resa come tabella Markdown a 4 righe di dati. La conversione ha
  perso il glifo del segno di spunta (leggibile nel raw come carattere di
  controllo U+0006) conservandone pero' la posizione di colonna: la cella
  spuntata e' resa con "X" nella colonna corrispondente, le altre celle della
  riga restano vuote. Le due colonne di sinistra sono raggruppate nel testo
  ufficiale sotto l'unica intestazione "AdES-Level" (che in Markdown non e'
  rappresentabile): le intestazioni riportano "Baseline (AdES-Level)" e
  "Extended (AdES-Level)" senza alterare alcun valore;
- in tutte le tabelle le celle che il PDF spezzava su piu' righe (es. la cella
  "The signing certificate (and other certificates required to form a chain to a
  trust anchor)", spezzata dopo "to form") sono ricomposte in un'unica cella,
  nessun valore eliminato;
- in A.3.7 la chiusura dell'esempio riporta "a final TOTAL- PASSED" con lo
  spazio interno anomalo presente nel testo ufficiale: riprodotto verbatim,
  non corretto (ADR-0010: la correzione sarebbe una congettura).

`testo` e' la sintesi in italiano (bozza LLM compressa, da validare in coda di
revisione); `testo_integrale` e' la fonte autorevole per l'interpretazione.
"""

RIGHE_OBBLIGHI: list[dict] = []

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "Annex A.1 (General remarks and assumptions)",
        "testo": (
            "A.1 enuncia oggetto e assunzioni degli esempi di convalida dell'Annex A: la convalida di una "
            "Signature with Time e' specificata in una clausola separata (clausola 5.5) solo per mantenere "
            "semplice questo caso speciale, mentre il processo di convalida a lungo termine sarebbe stato "
            "ugualmente utilizzabile per una Signature with Time; negli esempi la distinzione e' ignorata e "
            "viene presentata solo la logica dell'algoritmo, applicabile agli esempi scelti. Gli esempi "
            "assumono che i controlli di base (crittografici, di formato) riescano e mostrano come le "
            "proprieta' fondamentali di una firma AdES - la prova dell'esistenza di determinati oggetti in "
            "determinati momenti - permettano di convalidare firme del passato. Assunzioni comuni a tutti gli "
            "esempi: il certificato di firma e' identificabile perche' fornito dentro la firma; nessun vincolo "
            "specifico sul processo di convalida salvo diversa indicazione; per tutti i certificati usati si "
            "puo' costruire un percorso valido verso una trust anchor, salvo diversa indicazione; come input "
            "serve solo la firma, salvo diversa indicazione; sintassi/formato di tutti gli elementi corretto; "
            "tutti gli elementi richiesti presenti; marche temporali e firme calcolate sui dati corretti; "
            "nessun altro difetto di base simile, salvo diversa indicazione."
        ),
        "testo_integrale": (
            "A.1 General remarks and assumptions\n\n"
            "This clause gives some examples that aim at helping to better understand the signature validation "
            "algorithm presented in the normative part of the present document.\n\n"
            "- While validating a Signature with Time is specified in a separate clause (see clause 5.5), this "
            "has been done only to keep this special case simple. It would have been perfectly possible to use "
            "the long-term validation process also for Signature with Time. In the examples, this distinction "
            "is ignored and only the logic behind the algorithm is presented as applicable to the examples "
            "chosen.\n\n"
            "- These examples also assume that basic checks like cryptographic or format checks succeed. The "
            "focus is on examples showing how the fundamental properties of an AdES signature, proving the "
            "existence of certain objects at certain times, help to validate signatures from the past.\n\n"
            "- For all validation examples, the following assumptions are made:\n\n"
            "  - The signing certificate can be identified, as it is provided within the signature.\n\n"
            "  - There are no specific constraints on the validation process unless noted otherwise.\n\n"
            "  - A valid path to a trust anchor can be built for all certificates used unless noted "
            "otherwise.\n\n"
            "  - Only the signature is needed as an input unless noted otherwise.\n\n"
            "  - The syntax/format of all elements is correct.\n\n"
            "  - All required elements are present.\n\n"
            "  - Time-stamps and signatures have been calculated over the right data.\n\n"
            "  - No other similar basic flaws exist, unless noted otherwise."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex A.2 (Symbols)",
        "testo": (
            "A.2 introduce i simboli usati negli esempi: la Figure A.1 mostra i simboli utilizzati nelle "
            "figure degli esempi che seguono."
        ),
        "testo_integrale": (
            "A.2 Symbols\n\n"
            "Figure A.1: Symbols used in examples\n\n"
            "Figure A.1 shows the symbols used in the following graphics."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex A.3.1 (Introduction)",
        "testo": (
            "Caso semplice: un certificato viene revocato prima della convalida successiva di una firma "
            "(Figure A.2, Revoked Certificate Example). Cronologia degli eventi rilevanti: a t1 il certificato "
            "e' emesso; a t2 la firma e' creata usando quel certificato; a t3 e' creata una marca temporale di "
            "firma (Signature with Time); a t4 il certificato e' revocato; a t5 si tenta la convalida del "
            "certificato. Tutti gli altri certificati usati nel processo si assumono ancora validi."
        ),
        "testo_integrale": (
            "A.3.1 Introduction\n\n"
            "Figure A.2: Revoked Certificate Example\n\n"
            "In this example, a simple case is shown where a certificate is revoked before subsequent "
            "validation of a signature. Figure A.2 shows the timeline for the relevant events:\n\n"
            "- At time t1 the certificate is issued.\n\n"
            "- At time t2 the signature is created using the certificate.\n\n"
            "- At time t3 a signature time-stamp is created (Signature with Time).\n\n"
            "- At time t4 the certificate is revoked.\n\n"
            "- At time t5 validation of the certificate is tried.\n\n"
            "- All other certificates used in the process are assumed to being still valid."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex A.3.2 (Basic signature validation)",
        "testo": (
            "Risultato atteso: INDETERMINATE/REVOKED_NO_POE. Motivazione: l'algoritmo di Basic Signature "
            "validation non elabora l'attributo signature-time-stamp e quindi non puo' accertare se il momento "
            "della firma precede la data di revoca; lo stato di validita' resta indeterminato. Applicazione "
            "dell'algoritmo di convalida definito nella clausola 5.3: l'identificazione del certificato di "
            "firma riesce per assunzione; l'inizializzazione dei vincoli e dei parametri di convalida riesce "
            "per assunzione; la convalida del certificato di firma restituisce INDETERMINATE/REVOKED_NO_POE "
            "poiche' il certificato di firma e' stato revocato. L'algoritmo termina con "
            "INDETERMINATE/REVOKED_NO_POE, esito atteso e corretto."
        ),
        "testo_integrale": (
            "A.3.2 Basic signature validation\n\n"
            "Expected result: INDETERMINATE/REVOKED_NO_POE\n"
            "Rationale: The Basic Signature validation algorithm does not process the signature-time-stamp "
            "attribute and hence cannot ascertain whether the signing time is before the revocation date. "
            "Hence, the validity status is indeterminate.\n\n"
            "The validation algorithm defined in clause 5.3 proceeds as follows:\n\n"
            "- The identification of the signing certificate succeeds by assumption.\n\n"
            "- The initialization of the validation constraints and parameters succeeds by assumption.\n\n"
            "- The validation of the signing certificate returns INDETERMINATE/REVOKED_NO_POE since the "
            "signing certificate has been revoked.\n\n"
            "The algorithm terminates with INDETERMINATE/REVOKED_NO_POE which is expected and correct."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex A.3.3 (Validating a Signature with Time)",
        "testo": (
            "Risultato atteso: TOTAL-PASSED. Motivazione: lo stato passa da INDETERMINATE/REVOKED_NO_POE "
            "(con l'algoritmo di convalida di base) a TOTAL-PASSED perche' l'algoritmo di convalida per "
            "Signature with Time elabora l'attributo signature-time-stamp e rileva che il momento della firma "
            "precede la data di revoca. Applicazione dell'algoritmo della clausola 5.5: l'insieme dei token di "
            "marca temporale di firma e' inizializzato all'unica marca presente nella firma (step 1); "
            "best-signature-time e' posto al tempo corrente (step 1); si esegue la convalida Basic Signature, "
            "che restituisce INDETERMINATE/REVOKED_NO_POE e consente di proseguire perche' le marche esistenti "
            "possono ancora permettere di verificare la firma; la verifica (step 3)a)) dell'impronta del "
            "messaggio della marca riesce per assunzione; la convalida del token di marca temporale (step 3)b)) "
            "e' eseguita come da clausola 5.4; la convalida Basic Signature della firma sul token di marca "
            "riesce, poiche' il certificato della TSA non e' ne' scaduto ne' revocato per assunzione; essendo "
            "lo step precedente TOTAL-PASSED, la firma e' stata creata prima della marca e il "
            "best-signature-time e' posto al tempo della marca (step 4)b); lo step 4)a) confronta il best "
            "signature time con la data di revoca del certificato e, essendo il certificato revocato solo dopo "
            "la generazione della marca, il processo prosegue con lo step 4)d); la coerenza dei valori "
            "temporali e' verificata e ok (step 4)c); non esistono vincoli sul ritardo della marca (step 5), "
            "quindi si passa allo step successivo; il processo restituisce TOTAL-PASSED e il report di "
            "convalida generato alla DA (step 6)."
        ),
        "testo_integrale": (
            "A.3.3 Validating a Signature with Time\n\n"
            "Expected result: TOTAL-PASSED\n"
            "Rationale: The status goes from INDETERMINATE/REVOKED_NO_POE (using the basic validation "
            "algorithm) to TOTAL-PASSED because the Signature with Time validation algorithm processes the "
            "signature time-stamp attribute and finds that the signing time lies before the revocation "
            "date.\n\n"
            "The validation algorithm for signatures with time defined in clause 5.5 proceeds as follows:\n\n"
            "- The set of signature time-stamp tokens is initialized to the single time-stamp present in the "
            "signature (step 1).\n\n"
            "- Best-signature-time is set to current time (step 1).\n\n"
            "- The Basic Signature validation is performed. As shown before, this returns "
            "INDETERMINATE/REVOKED_NO_POE, and the rest of the algorithm can be run, since existing "
            "time-stamps can still allow to verify the signature.\n\n"
            "- The verification (step 3)a) of the message imprint of the time-stamp succeeds by assumption.\n\n"
            "- The Time-stamp token validation (step 3)b) is performed as per clause 5.4 for verifying the "
            "time-stamp.\n\n"
            "- The Basic Signature validation of the signature on the time-stamp token succeeds, since the "
            "certificate of the TSA has neither expired nor been revoked by assumption.\n\n"
            "- Since the previous step returned TOTAL-PASSED, the signature has been created before the "
            "time-stamp and the best-signature-time is set to the time of the time-stamp (step 4)b).\n\n"
            "- Step 4)a) compares this best signature time with the revocation date of the certificate. Since "
            "the certificate has been revoked only after the time-stamp has been generated, the process "
            "continues with step 4)d).\n\n"
            "- The coherence of the time values is checked and found to be ok (step 4)c).\n\n"
            "- No constraints on time-stamp delay exist (step 5), so the process skips to the next step.\n\n"
            "- The process returns TOTAL-PASSED and returns the validation report generated to the DA "
            "(step 6)."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex A.3.4 (Example 2: Revoked CA certificate)",
        "testo": (
            "Secondo esempio, piu' complesso: e' revocato il certificato della CA che ha emesso il "
            "certificato di firma (Figure A.3, Revoked CA Certificate). Cronologia degli eventi rilevanti: a "
            "t0 il certificato della CA e' emesso da un'altra CA; a t1 il certificato di firma e' emesso da "
            "quella CA; a t2 la firma e' creata usando il certificato; a t3 e' creata una marca temporale di "
            "firma (Signature with Time); a t4 sono emesse CRL da parte della CA che ha emesso il certificato "
            "di firma; a t5 e' creata una firma che fornisce disponibilita' e integrita' a lungo termine del "
            "materiale di convalida (Signatures providing Long Term Availability and Integrity of Validation "
            "Material) con produzione di un archive time-stamp; a t6 sono emesse CRL per il certificato della "
            "Time Stamping Authority (TSA) che ha emesso la marca temporale di firma; a t7 scade il "
            "certificato di quella TSA; a t8 il certificato della CA e' revocato; a t9 si tenta la convalida "
            "del certificato. Tutti gli altri certificati usati nel processo si assumono ancora validi. Si "
            "assume che il certificato della TSA sia stato emesso da un'autorita' diversa dalla CA."
        ),
        "testo_integrale": (
            "A.3.4 Example 2: Revoked CA certificate\n\n"
            "Figure A.3: Revoked CA Certificate\n\n"
            "This is a slightly more complex case, where the CA certificate that issued the signing "
            "certificate has been revoked. Figure A.3 shows the timeline for the relevant events:\n\n"
            "- At time t0 the CA certificate is issued by another CA.\n\n"
            "- At time t1 the signing certificate is issued by that CA.\n\n"
            "- At time t2 the signature is created using the certificate.\n\n"
            "- At time t3 a signature time-stamp is created (Signature with Time).\n\n"
            "- At time t4 CRLs were issued by the CA that issued the signing certificate.\n\n"
            "- At time t5 a Signatures providing Long Term Availability and Integrity of Validation Material "
            "is created and an archive time-stamp produced.\n\n"
            "- At time t6 CRLs were issued for the certificate of the Time Stamping Authority (TSA) that "
            "issued the signature time-stamp.\n\n"
            "- At time t7 the certificate of the Time Stamping Authority (TSA) that issued the signature "
            "time-stamp expires.\n\n"
            "- At time t8 the CA certificate is revoked.\n\n"
            "- At time t9 validation of the certificate is tried.\n\n"
            "- All other certificates used in the process are assumed to being still valid.\n\n"
            "It is assumed that the TSA certificate has been issued by a different authority than the CA "
            "certificate."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex A.3.5 (Basic signature validation)",
        "testo": (
            "Risultato atteso: INDETERMINATE/REVOKED_CA_NO_POE. Motivazione: l'algoritmo per le Basic "
            "Signatures non gestisce gli attributi LTV. Applicazione dell'algoritmo definito nella clausola "
            "5.3: l'identificazione del certificato di firma riesce per assunzione; l'inizializzazione dei "
            "vincoli e dei parametri di convalida riesce per assunzione; la convalida del certificato di firma "
            "restituisce INDETERMINATE/REVOKED_CA poiche' il certificato della CA e' stato revocato. "
            "L'algoritmo termina qui con INDETERMINATE/REVOKED_CA_NO_POE, esito atteso e corretto."
        ),
        "testo_integrale": (
            "A.3.5 Basic signature validation\n\n"
            "Expected result: INDETERMINATE/REVOKED_CA_NO_POE\n"
            "Rationale: The algorithm for Basic Signatures does not handle the LTV attributes.\n\n"
            "The validation algorithm defined in clause 5.3 proceeds as follows:\n\n"
            "- The identification of the signing certificate succeeds by assumption.\n\n"
            "- The initialization of the validation constraints and parameters succeeds by assumption.\n\n"
            "- The validation of the signing certificate returns INDETERMINATE/REVOKED_CA because the CA "
            "certificate has been revoked.\n\n"
            "The algorithm terminates here with INDETERMINATE/REVOKED_CA_NO_POE, which is expected and "
            "correct."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex A.3.6 (Validation of a Signature with Time)",
        "testo": (
            "Risultato atteso: INDETERMINATE/REVOKED_CA_NO_POE. Motivazione: l'algoritmo per le firme con "
            "tempo non gestisce gli attributi LTV; l'attributo signature-time-stamp protegge solo il valore "
            "della firma e il certificato di firma e non aiuta quando e' revocata una CA intermedia. "
            "Applicazione del processo definito nella clausola 5.5: l'insieme dei token di marca temporale di "
            "firma e' inizializzato all'unico token presente nella firma; best-signature-time e' posto al "
            "tempo corrente; si esegue il processo di convalida per le Basic Signatures, che restituisce "
            "INDETERMINATE/REVOKED_CA_NO_POE; poiche' la convalida della firma non ha riportato TOTAL-PASSED "
            "ne' INDETERMINATE/REVOKED_NO_POE ne' INDETERMINATE/OUT_OF_BOUNDS, l'algoritmo termina con "
            "INDETERMINATE/REVOKED_CA_NO_POE."
        ),
        "testo_integrale": (
            "A.3.6 Validation of a Signature with Time\n\n"
            "Expected result: INDETERMINATE/REVOKED_CA_NO_POE\n"
            "Rationale: The algorithm for signatures with time does not handle the LTV attributes. The "
            "signature-time-stamp attribute protects only the signature value and the signing certificate but "
            "does not help when an intermediary CA is revoked.\n\n"
            "The validation process defined in clause 5.5 proceeds as follows:\n\n"
            "- The set of signature time-stamp tokens is initialized to the single signature time-stamp token "
            "present in the signature.\n\n"
            "- Best-signature-time is set to current time.\n\n"
            "- The validation process for Basic Signatures is performed and returns "
            "INDETERMINATE/REVOKED_CA_NO_POE.\n\n"
            "- Since the signature validation did not report TOTAL-PASSED nor INDETERMINATE/REVOKED_NO_POE "
            "nor INDETERMINATE/OUT_OF_BOUNDS, the algorithm terminates with "
            "INDETERMINATE/REVOKED_CA_NO_POE."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex A.3.7 (Long-Term Validation)",
        "testo": (
            "Si applica l'algoritmo di convalida a lungo termine (Long-Term Validation). Risultato atteso: "
            "TOTAL-PASSED; motivazione: INDETERMINATE diventa TOTAL-PASSED grazie all'archive time-stamp, "
            "prodotto a t5 prima di qualunque evento compromettente. Il processo parte dalla clausola 5.6.3: "
            "inizializzazione dei POE (step 1) con tutti gli oggetti (Table A.3.7-1: firma; certificato di "
            "firma e altri certificati necessari a formare una catena verso una trust anchor; informazioni di "
            "revoca per il certificato di firma e per tutti i certificati della catena; marca temporale di "
            "firma; certificato TSA relativo alla marca temporale di firma e relativi certificati di catena; "
            "informazioni di revoca per quel certificato TSA; archive time-stamp; certificato TSA relativo "
            "all'archive time-stamp e relativi certificati di catena; informazioni di revoca per quel "
            "certificato TSA - tutti esistenti a t9); non esiste evidence record, quindi lo step 1) e' "
            "saltato; un primo insieme di POE e' creato usando tutti gli oggetti della firma; il processo di "
            "convalida per le Signatures with time restituisce INDETERMINATE/REVOKED_CA_NO_POE e prosegue "
            "perche' le marche esistenti possono ancora permettere di verificare la firma; la convalida del "
            "token di marca temporale (step 4) e' eseguita come da clausola 5.4 per verificare l'archive "
            "time-stamp, e la convalida Basic Signature della firma su quel token riesce poiche' il "
            "certificato della TSA che lo ha prodotto non e' ne' scaduto ne' revocato; i POE sono estratti al "
            "tempo dell'archive time-stamp (clausola 5.6.2.3) per firma, certificato di firma (con gli altri "
            "certificati della catena), informazioni di revoca del certificato di firma, marca temporale di "
            "firma, certificato TSA relativo alla marca temporale di firma, e ne risulta la Table A.3.7-2 "
            "(firma, certificato di firma, relative informazioni di revoca, marca temporale di firma, "
            "certificato TSA relativo a quella marca e relative informazioni di revoca: esistenti a t5; "
            "archive time-stamp, certificato TSA relativo all'archive time-stamp e relative informazioni di "
            "revoca: esistenti a t9); allo step 4)c) il processo di convalida della marca temporale (clausola "
            "5.4) restituisce, per la Basic Signature validation della firma sul token, "
            "INDETERMINATE/OUT_OF_BOUNDS_NO_POE poiche' il certificato di quella TSA e' scaduto; poiche' lo "
            "step ha dato INDETERMINATE/OUT_OF_BOUNDS_NO_POE, si esegue il processo di convalida passata "
            "della firma per la marca temporale (clausola 5.6.2.4): la convalida passata del certificato "
            "della TSA costruisce la catena prospettica (tutte le informazioni sono presenti nell'archivio), "
            "la path validation riesce in un punto nel tempo in cui il certificato TSA non era ancora "
            "scaduto, il validation-time sliding e' eseguito con la catena prospettica e l'insieme dei POE "
            "(control-time al tempo corrente; oggetti di revoca per il certificato TSA presenti nell'insieme "
            "dei POE; prova di esistenza degli oggetti rilevanti a t5; l'oggetto di revoca si assume non "
            "fresco, quindi il control-time e' posto al tempo di creazione di quell'oggetto di revoca, t7; "
            "vincoli di certificato e crittografici applicati alla catena e riusciti per assunzione; "
            "restituiti PASSED e control-time t7) e, essendo lo stato al tempo corrente "
            "INDETERMINATE/OUT_OF_BOUNDS_NO_POE ed esistendo un POE per la marca temporale di firma a t5 "
            "precedente t7, la convalida passata della firma restituisce PASSED; il processo di estrazione "
            "dei POE e' eseguito per quella marca temporale e genera un nuovo elenco di POE (Table A.3.7-3: "
            "firma e certificato di firma esistenti a t3; informazioni di revoca del certificato di firma a "
            "t4; marca temporale di firma, certificato TSA relativo a quella marca e relative informazioni di "
            "revoca a t5; archive time-stamp, certificato TSA relativo all'archive time-stamp e relative "
            "informazioni di revoca a t9); si esegue quindi il processo di convalida passata della firma: la "
            "convalida passata del certificato di firma costruisce la catena (per assunzione) e la path "
            "validation riesce, e il validation time sliding e' eseguito per il certificato di firma "
            "(control-time al tempo corrente; esiste un POE al tempo corrente per il certificato della CA e "
            "per il corrispondente stato delle informazioni di revoca; essendo la CA revocata a t8 il "
            "control-time assume quel valore, assumendo che la freschezza non si applichi; prova di esistenza "
            "degli oggetti rilevanti per il certificato di firma a t3, precedente t8; l'oggetto di revoca si "
            "assume fresco, quindi il control-time non cambia; vincoli di certificato e crittografici "
            "applicati alla catena e riusciti per assunzione; restituiti PASSED e control-time t8) e, essendo "
            "lo stato al tempo corrente INDETERMINATE/REVOKED_CA_NO_POE ed esistendo un POE per la firma a "
            "t3 precedente t8, la convalida passata della firma restituisce PASSED. L'algoritmo di convalida "
            "restituisce un esito finale TOTAL-PASSED insieme al report di convalida."
        ),
        "testo_integrale": (
            "A.3.7 Long-Term Validation\n\n"
            "The Long-Term Validation Algorithm is applied.\n\n"
            "Expected result: TOTAL-PASSED\n"
            "Rationale: INDETERMINATE turns into TOTAL-PASSED due to the archive time-stamp, which was "
            "produced at t5 before any compromising event.\n\n"
            "The process starts in clause 5.6.3:\n\n"
            "- POE initialization (step 1): the POE is initialized with all objects.\n\n"
            "Table A.3.7-1\n\n"
            "| Content | Exists at time |\n"
            "|---|---|\n"
            "| The signature | t9 |\n"
            "| The signing certificate (and other certificates required to form a chain to a trust anchor) | "
            "t9 |\n"
            "| Revocation Information for the signing certificate (as well as for all certificates required "
            "to form a chain to a trust anchor) | t9 |\n"
            "| The signature time-stamp | t9 |\n"
            "| The TSA certificate related to the signature time-stamp (and other certificates required to "
            "form a chain to a trust anchor) | t9 |\n"
            "| Revocation Information for that TSA certificate (as well as for all certificates required to "
            "form a chain to a trust anchor) | t9 |\n"
            "| The archive time-stamp | t9 |\n"
            "| The TSA certificate related to the archive time-stamp (and other certificates required to form "
            "a chain to a trust anchor) | t9 |\n"
            "| Revocation Information for that TSA certificate (as well as for all certificates required to "
            "form a chain to a trust anchor) | t9 |\n\n"
            "- There is no evidence record, so step 1) is skipped.\n\n"
            "- A first set of POEs is created using all the objects in the signature.\n\n"
            "- The validation process for Signatures with time returns INDETERMINATE/REVOKED_CA_NO_POE. The "
            "process continues as existing time-stamps can still allow verifying the signature.\n\n"
            "- The Time-stamp token validation (step 4) is performed as per clause 5.4 for verifying the "
            "archive time-stamp:\n\n"
            "  - Basic signature validation of the signature on the archive time-stamp token succeeds, since "
            "the certificate of the TSA that has produced that time-stamp token has neither expired nor been "
            "revoked.\n\n"
            "- POEs are extracted at the time of the archive time-stamp (see clause 5.6.2.3) for:\n\n"
            "  - The signature.\n\n"
            "  - The signing certificate (and other certificates required to form a chain to a trust "
            "anchor).\n\n"
            "  - Revocation Information for the signing certificate (as well as for all certificates "
            "required to form a chain to a trust anchor).\n\n"
            "  - The signature time-stamp.\n\n"
            "  - The TSA certificate related to the signature time-stamp (and other certificates required to "
            "form a chain to a trust anchor).\n\n"
            "It results in the following set of POEs.\n\n"
            "Table A.3.7-2\n\n"
            "| Content | Exists at time |\n"
            "|---|---|\n"
            "| The signature | t5 |\n"
            "| The signing certificate (and other certificates required to form a chain to a trust anchor) | "
            "t5 |\n"
            "| Revocation Information for the signing certificate (as well as for all certificates required "
            "to form a chain to a trust anchor) | t5 |\n"
            "| The signature time-stamp | t5 |\n"
            "| The TSA certificate related to the signature time-stamp (and other certificates required to "
            "form a chain to a trust anchor) | t5 |\n"
            "| Revocation Information for that TSA certificate (as well as for all certificates required to "
            "form a chain to a trust anchor) | t5 |\n"
            "| The archive time-stamp | t9 |\n"
            "| The TSA certificate related to the archive time-stamp (and other certificates required to form "
            "a chain to a trust anchor) | t9 |\n"
            "| Revocation Information for that TSA certificate (as well as for all certificates required to "
            "form a chain to a trust anchor) | t9 |\n\n"
            "- Step 4)c): the time-stamp validation process is performed (clause 5.4):\n\n"
            "  - The Basic Signature validation of the signature on the time-stamp token returns "
            "INDETERMINATE/OUT_OF_BOUNDS_NO_POE, since the certificate of that TSA has expired.\n\n"
            "- Since this step returned INDETERMINATE/OUT_OF_BOUNDS_NO_POE, the past signature validation "
            "process for the time-stamp is performed (see clause 5.6.2.4):\n\n"
            "  - The past certificate validation for the TSA certificate is performed:\n\n"
            "    - The prospective chain can be built (all information is present in the archive).\n\n"
            "    - Since the TSA certificate has only expired, path validation, at a point in time where the "
            "TSA certificate was not yet expired, succeeds.\n\n"
            "    - The validation-time sliding process is performed with the following inputs: the "
            "prospective chain and the set of POEs:\n\n"
            "      - Control-time is current time.\n\n"
            "      - Revocation objects for the TSA certificate are in the set of POE.\n\n"
            "      - Proof of existence of the relevant objects exists at t5.\n\n"
            "      - The revocation object is assumed not to be fresh and thus the control-time is set to the "
            "time this revocation object has been created (t7).\n\n"
            "      - The certificate constraints and cryptographic constraints are applied to the chain, and "
            "succeed by assumption.\n\n"
            "      - PASSED and control-time t7 are returned.\n\n"
            "    - Since the current time status is INDETERMINATE/OUT_OF_BOUNDS_NO_POE and there is a POE for "
            "the signature time-stamp at t5 before t7, the past signature validation returns PASSED.\n\n"
            "- The POE-extraction process is performed for that time-stamp and a new list of POEs is "
            "generated.\n\n"
            "Table A.3.7-3\n\n"
            "| Content | Exists at time |\n"
            "|---|---|\n"
            "| The signature | t3 |\n"
            "| The signing certificate (and other certificates required to form a chain to a trust anchor) | "
            "t3 |\n"
            "| Revocation Information for the signing certificate (as well as for all certificates required "
            "to form a chain to a trust anchor) | t4 |\n"
            "| The signature time-stamp | t5 |\n"
            "| The TSA certificate related to the signature time-stamp (and other certificates required to "
            "form a chain to a trust anchor) | t5 |\n"
            "| Revocation Information for that TSA certificate (as well as for all certificates required to "
            "form a chain to a trust anchor) | t5 |\n"
            "| The archive time-stamp | t9 |\n"
            "| The TSA certificate related to the archive time-stamp (and other certificates required to form "
            "a chain to a trust anchor) | t9 |\n"
            "| Revocation Information for that TSA certificate (as well as for all certificates required to "
            "form a chain to a trust anchor) | t9 |\n\n"
            "- The past signature validation process for the signature is performed:\n\n"
            "  - The past certificate validation is performed for the signing certificate:\n\n"
            "    - Certificate chain can be built by assumption.\n\n"
            "    - Certificate path validation succeeds.\n\n"
            "    - The validation time sliding process is performed for the signing certificate:\n\n"
            "      - Control-time is current time.\n\n"
            "      - A POE exists at the current time for the CA certificate as well as the corresponding "
            "revocation info status.\n\n"
            "      - Since the CA is revoked at t8, control-time takes this value (assuming that freshness "
            "does not apply).\n\n"
            "      - Proof of existence of the relevant objects for the signing certificate exists at t3 "
            "before t8.\n\n"
            "      - The revocation object is assumed to be fresh and thus the change control-time is "
            "unchanged.\n\n"
            "      - The certificate constraints and cryptographic constraints are applied to the chain, and "
            "succeed by assumption.\n\n"
            "      - PASSED and control-time t8 are returned.\n\n"
            "    - Since the current time status is INDETERMINATE/REVOKED_CA_NO_POE and there is a POE for "
            "the signature at t3 before t8, the past signature validation returns PASSED.\n\n"
            "- The validation algorithm returns a final TOTAL- PASSED plus the validation report."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex B (Signature Classes and AdES Signatures)",
        "testo": (
            "Annex B (informativo) mappa le signature class specificate nel presente documento con i "
            "signature level specificati nelle specifiche AdES-Formats (ETSI EN 319 122-1 [i.2], ETSI EN 319 "
            "122-2 [i.3], ETSI EN 319 132-1 [i.4], ETSI EN 319 132-2 [i.5], ETSI EN 319 142-1 [i.6], ETSI EN "
            "319 142-2 [i.7]). La Table B.1 associa: CAdES-B-B/XAdES-B-B/PAdES-B-B (estese: CAdES-E-BES, "
            "CAdES-E-EPES, XAdES-E-BES, XAdES-E-EPES, PAdES-E-BES, PAdES-E-EPES) -> Basic Signature; "
            "CAdES-B-T/XAdES-B-T/PAdES-B-T (estese: CAdES-E-T, CAdES-E-C, CAdES-E-X, XAdES-E-T, XAdES-E-C, "
            "XAdES-E-X) -> Signature With Time; CAdES-B-LT/XAdES-B-LT/PAdES-B-LT (estese: CAdES-E-X-L, "
            "XAdES-E-X-L) -> Signatures with Long-Term Validation Material; "
            "CAdES-B-LTA/XAdES-B-LTA/PAdES-B-LTA (estese: CAdES-E-A, XAdES-E-A, PAdES-E-LTV) -> Signatures "
            "providing Long Term Availability and Integrity of Validation Material."
        ),
        "testo_integrale": (
            "Annex B (informative): Signature Classes and AdES Signatures\n\n"
            "This annex maps the signature classes specified in the present document with signature levels "
            "specified in the specification of AdES-Formats (ETSI EN 319 122-1 [i.2], ETSI EN 319 122-2 "
            "[i.3], ETSI EN 319 132-1 [i.4], ETSI EN 319 132-2 [i.5], ETSI EN 319 142-1 [i.6] and ETSI EN "
            "319 142-2 [i.7]).\n\n"
            "Table B.1\n\n"
            "| Baseline (AdES-Level) | Extended (AdES-Level) | Basic Signature | Signature With Time | "
            "Signatures with Long-Term Validation Material | Signatures providing Long Term Availability and "
            "Integrity of Validation Material |\n"
            "|---|---|---|---|---|---|\n"
            "| CAdES-B-B, XAdES-B-B, PAdES-B-B | CAdES-E-BES, CAdES-E-EPES, XAdES-E-BES, XAdES-E-EPES, "
            "PAdES-E-BES, PAdES-E-EPES | X | | | |\n"
            "| CAdES-B-T, XAdES-B-T, PAdES-B-T | CAdES-E-T, CAdES-E-C, CAdES-E-X, XAdES-E-T, XAdES-E-C, "
            "XAdES-E-X | | X | | |\n"
            "| CAdES-B-LT, XAdES-B-LT, PAdES-B-LT | CAdES-E-X-L, XAdES-E-X-L | | | X | |\n"
            "| CAdES-B-LTA, XAdES-B-LTA, PAdES-B-LTA | CAdES-E-A, XAdES-E-A, PAdES-E-LTV | | | | X |"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex C.1 (Applicability checking)",
        "testo": (
            "Mentre la convalida della firma e' il processo che verifica e conferma che una firma e' "
            "tecnicamente valida, il controllo delle regole di applicabilita' (applicability rules checking) "
            "determina se una firma e' conforme ai requisiti di una specifica o di un regolamento: convalida "
            "della firma e controllo delle regole di applicabilita' sono quindi processi indipendenti. In "
            "particolare: una firma puo' essere valida ma non raggiungere un certo signature level atteso; "
            "una firma puo' essere conforme a un certo signature level atteso ma la convalida puo' restituire "
            "uno stato INDETERMINATE o TOTAL-FAILED."
        ),
        "testo_integrale": (
            "C.1 Applicability checking\n\n"
            "While signature validation is the process of verifying and confirming that a signature is "
            "technically valid, applicability rules checking determines whether a signature complies with "
            "the requirements of a specification or regulation. Thus, signature validation and applicability "
            "rules checking of signatures are independent processes. In particular:\n\n"
            "- A signature can be valid but not achieving a certain expected signature level.\n\n"
            "- A signature can comply to a certain expected signature level but validation returns an "
            "INDETERMINATE or TOTAL-FAILED status indication."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
    {
        "riferimento": "Annex C.2 (Format conformance)",
        "testo": (
            "I processi di convalida descritti nelle clausole 5.3, 5.5 e 5.6 non riguardano la valutazione "
            "della conformita' di una firma a una specifica signature class (definita nella clausola 4.3) o a "
            "un signature level delle specifiche AdES-Formats (ETSI EN 319 122-1 [i.2], ETSI EN 319 122-2 "
            "[i.3], ETSI EN 319 132-1 [i.4], ETSI EN 319 132-2 [i.5], ETSI EN 319 142-1 [i.6], ETSI EN 319 "
            "142-2 [i.7]); la valutazione di conformita' per applicazioni e procedure di creazione e "
            "convalida di firme e' prevista in una Technical Specification e i test di conformita' specifici "
            "per formato saranno coperti da ETSI TS 119 1x4 (non ancora disponibili). Il conformance checking "
            "e' in linea di principio ortogonale alla convalida (una firma puo' essere valida ma non "
            "conforme) e puo' essere richiesto da una signature validation policy per specifici contesti di "
            "business; il presente documento non lo disciplina, quindi le implementazioni conformi al presente "
            "documento non possono includere il conformance checking nella status indication e una SVA che "
            "indichi TOTAL-FAILED o INDETERMINATE solo per un controllo di conformita' fallito non e' conforme "
            "al presente documento. Futuri deliverable ETSI potranno occuparsi specificamente del conformance "
            "checking, specificando modelli funzionali estesi, indicazioni di stato e report di convalida "
            "estesi; nel frattempo chi vuole eseguire il conformance checking insieme alla convalida puo' "
            "implementarlo direttamente nella DA (in modo indipendente dal controllo di validita' della "
            "firma) oppure come parte del processo di convalida della firma (Figure C.1 e C.2)."
        ),
        "testo_integrale": (
            "C.2 Format conformance\n\n"
            "Therefore, the signature validation processes described in clauses 5.3, 5.5 and 5.6 do not "
            "address the assessment of the conformity of a signature with a specific class, as defined in "
            "clause 4.3, or signature level as specified in the specification of AdES-Formats (ETSI EN 319 "
            "122-1 [i.2], ETSI EN 319 122-2 [i.3], ETSI EN 319 132-1 [i.4], ETSI EN 319 132-2 [i.5], ETSI EN "
            "319 142-1 [i.6] and ETSI EN 319 142-2 [i.7]). Conformity assessment for signature creation and "
            "validation applications and procedures is planned to be specified in a Technical Specification. "
            "Format-specific conformance testing will be covered in ETSI TS 119 1x4 (which are not yet "
            "available).\n\n"
            "While conformance checking is in principle orthogonal to signature validation (a signature may "
            "be valid, but not conformant), conformance checking can be required by a signature validation "
            "policy for specific business contexts. The present document does not address conformance "
            "checking however, so implementations conforming to the present document cannot include "
            "conformance checking in the status indication. An SVA indicating a TOTAL-FAILED or "
            "INDETERMINATE result just because of a failed conformance check will not be conformant to the "
            "present document. Future ETSI deliverables can specifically target conformance checking. Such "
            "documents can specify extended functional models to support as well as extended status "
            "indications and validation reports. Meanwhile, implementers that want to perform conformance "
            "checking together with validation can implement conformance checking according to the following "
            "approaches:\n\n"
            "- Directly by the DA (independent of checking the validity of the signature) (see Figure C.1).\n\n"
            "- As part of the signature validation process (see Figure C.2).\n\n"
            "Figure C.1: Conformance Checking independent of Signature Validation\n\n"
            "Figure C.2: Conformance Checking as part of Signature Validation"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "Annex A.1 (General remarks and assumptions)",
    "Annex A.2 (Symbols)",
    "Annex A.3.1 (Introduction)",
    "Annex A.3.2 (Basic signature validation)",
    "Annex A.3.3 (Validating a Signature with Time)",
    "Annex A.3.4 (Example 2: Revoked CA certificate)",
    "Annex A.3.5 (Basic signature validation)",
    "Annex A.3.6 (Validation of a Signature with Time)",
    "Annex A.3.7 (Long-Term Validation)",
    "Annex B (Signature Classes and AdES Signatures)",
    "Annex C.1 (Applicability checking)",
    "Annex C.2 (Format conformance)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
