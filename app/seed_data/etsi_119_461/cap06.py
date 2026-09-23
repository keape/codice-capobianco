"""ETSI TS 119 461 V2.1.1 (2025-02) - Policy and security requirements for
trust service components providing identity proofing of trust service
subjects. Fonte 9 (id cablato dal wiring finale in un'altra sessione).
Capitolo 6 di 8: clausola 8.4 "Binding to applicant" (sottoclausole 8.4.1-
8.4.5) e clausola 8.5 "Issuing of proof" (sottoclausole 8.5.1-8.5.2). Testo
ufficiale in app/.source_cache/etsi_119_461/cap06.txt.

Convenzione di indice (specifica di questo documento, vedi contesto del
batch): ogni requisito con id proprio in grassetto (prefissi BIN-8.4.x-nn e
ISS-8.5.x-nn, confermati nella legenda di clausola 3.4 letta da Etsi461Cap01)
-> un nodo, `riferimento` = id esatto senza il marcatore "[CONDITIONAL]" (che
va in `condizione_applicabilita`). "shall"/"shall not" -> Obbligo; "may" ->
Principio tipo "altro"; "should" -> trattato come Obbligo (raccomandazione
normativa ISO/ETSI, non mera facolta' come "may" - stessa convenzione gia'
usata in etsi_319_412_5/cap01.py per QCS-4.3.2-02/QCS-4.3.4-02). Nessun nodo
per BIN-8.4.2-10 ("VOID", puro rinvio strutturale senza contenuto autonomo).

Condizioni di applicabilita' a due livelli:
- Condizione generale di sottoclausola: 8.4.2, 8.4.3, 8.4.4 e 8.4.5 si aprono
  ciascuna con un paragrafo "[CONDITIONAL] If ..." che introduce l'intera
  sottoclausola (non ha un id di requisito proprio, quindi non genera un
  nodo a se' - il suo contenuto e' riportato nel campo `condizione_
  applicabilita` di OGNI riga della sottoclausola, non in un nodo Principio
  dedicato, perche' non ha contenuto sostanziale autonomo oltre la soglia di
  applicabilita' gia' interamente assorbita nei requisiti che la seguono).
- Condizione puntuale: alcuni requisiti portano un proprio marcatore
  "[CONDITIONAL]" davanti al proprio id (es. BIN-8.4.2-04, BIN-8.4.2-04B,
  BIN-8.4.5-02X) con una condizione aggiuntiva propria, che si somma a quella
  generale di sottoclausola nel campo `condizione_applicabilita` (elenco
  puntato "inoltre, ..."). Per questi, "[CONDITIONAL]" e' anche riportato in
  `testo_integrale` perche' precede letteralmente l'id nel testo ufficiale;
  per i requisiti soggetti solo alla condizione generale di sottoclausola
  (senza marcatore proprio), "[CONDITIONAL]" NON compare in `testo_integrale`
  (fedelta' al testo, la condizione resta comunque tracciata nel campo
  dedicato).

NOTE del testo: mai un nodo autonomo. Assorbite nel `testo`/`testo_integrale`
del requisito/sottoclausola a cui sono annesse quando aggiungono un contenuto
sostanziale (es. NOTE 1/2 di 8.4.1 sui casi in cui il binding e' gia'
implicito nella convalida della prova, assorbite in BIN-8.4.1-02X; NOTE 8/12
sull'obbligo dell'IPSP di aggiornamento continuo indipendente dalla verifica
esterna, assorbite in BIN-8.4.2-04D/07X; NOTE 1/2 di 8.4.5.4 sul registro
fidato come fonte autentica, assorbite in BIN-8.4.5-04X; NOTE 1 di 8.5.2 che
definisce il termine "evidence" in questa clausola, assorbita in ISS-8.5.2-
01), altrimenti scartate (mera esemplificazione tecnica: EXAMPLE 1-3 in
8.4.2-8.4.4, riferimenti a standard futuri come ISO/IEC 29794-5/20059, NOTE
puramente terminologiche o di razionale sui termini transitori 2026/2027).

Categoria soggetto e tipo_obbligo (istruzioni del batch):
- "QTSP/gestore" per il TSP/IPSP: tutti i requisiti di binding vero e proprio
  (cattura video, biometria automatizzata, verifica manuale, binding per
  persona giuridica) e i requisiti di emissione/conservazione della prova.
- "Terza parte" per i requisiti il cui soggetto e' esplicitamente un
  "accredited laboratory" che esegue un test/valutazione esterna (BIN-8.4.2-
  04B/04C/04D, BIN-8.4.2-07X/07A) - stessa convenzione gia' adottata in
  reg_ue_2025_1566/cap01.py (allegato punti 3 e 5) per requisiti "shall be
  tested/verified by an accredited [...]". I requisiti dove l'IPSP stesso
  esegue test sistematici SENZA menzione di un laboratorio esterno (BIN-
  8.4.2-05D/05E/06X/08X/09X, BIN-8.4.3-05A/05B/06X/07X/08X/09X) restano
  "QTSP/gestore" (regime di test interno, non valutazione di terze parti).
- tipo_obbligo "tecnico/sicurezza" per tutta la clausola 8.4 (istruzione del
  batch: binding biometrico/manuale). Per la clausola 8.5.1 (emissione del
  risultato), tipo_obbligo "procedurale" (e' l'ultimo passo del processo di
  identity proofing, il contenuto del requisito riguarda cosa il processo
  deve produrre/trasmettere, non un controllo di sicurezza in se'). Per la
  clausola 8.5.2 (prove del processo), tipo_obbligo "di conservazione"
  (istruzione esplicita del batch).

BIN-8.4.5-02X e BIN-8.4.5-03 (segnalati nel contesto del batch): condizionali
su "natural person representing legal person" -> `condizione_applicabilita`
esplicita. BIN-8.4.5-02X rimanda a "an applicable use case from clause 9 or
Annex C" per la prova dell'identita' della persona fisica: clausola 9 e'
cap07, Annex C e' cap08 di questo stesso documento (fonti diverse dal
capitolo corrente) - nessuna relazione verso quell'id e' stata costruita qui
perche' non risolvibile con certezza nel proprio capitolo (sara' aggiunta a
posteriori dalla sessione principale se necessario, come da istruzione).

RELAZIONI interne (fonte_id_o_None=None, stesso criterio di cad/cap03.py):
- "richiama" con evidence_type "textual" quando il testo cita esplicitamente
  "the requirements of clause 8.4.2" (BIN-8.4.3-01X, BIN-8.4.4-01X, verso lo
  specifico requisito di cattura immagine BIN-8.4.2-05X - confidence
  moderata perche' la citazione e' alla sottoclausola nel suo complesso, non
  a un id puntuale) o cita esplicitamente un altro id di requisito (ISS-
  8.5.2-08 verso ISS-8.5.2-04, confidence alta, id citato letteralmente nel
  testo "ISS 8.5.2-04").
- "specifica" con evidence_type "inferred" per le coppie regola generale/
  regola che ne declina un sottocaso o un adempimento conseguente, senza
  citazione testuale esplicita di id (es. BIN-8.4.5-02X/03 rispetto a BIN-
  8.4.5-01; BIN-8.4.2-04B/04C rispetto a BIN-8.4.2-04A; BIN-8.4.2-08X/09X
  rispetto a BIN-8.4.2-06X; ISS-8.5.1-02/03X in cascata).
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        'riferimento': 'BIN-8.4.1-01X',
        'testo': "Il processo di identity proofing deve verificare che il richiedente sia il legittimo titolare della prova autorevole.",
        'testo_integrale': "BIN-8.4.1-01X: The identity proofing process shall verify that the applicant is the legitimate holder of the authoritative evidence.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'BIN-8.4.1-02X',
        'testo': "Il processo di identity proofing deve verificare che la prova autorevole sia in possesso del richiedente. Per le prove autorevoli costituite da un mezzo di identificazione elettronica esistente o da un mezzo di firma elettronica esistente, non sono necessari ulteriori requisiti di binding poiche' la convalida della prova verifica gia' il binding, nell'assunto che solo il richiedente possa utilizzare tale mezzo. Per le prove supplementari (registro fidato, prova di accesso, documenti e attestazioni), se il binding della prova autorevole ha esito positivo e la prova supplementare convalidata identifica la stessa persona, quest'ultima si considera vincolata al richiedente.",
        'testo_integrale': "BIN-8.4.1-02X: The identity proofing process shall verify that the authoritative evidence is in the possession of the applicant. NOTE 1: For the authoritative evidence types existing eID means and existing digital signature means, no specific binding requirements are needed since the validation of the evidence also verifies the binding, under the assumption that only the applicant can use the eID means or digital signature means. NOTE 2: For the supplementary evidence types trusted register, proof of access, and documents and attestations, no specific binding requirements are needed: if the binding of the authoritative evidence is successful and the supplementary evidence is validated and identifies the same person, the supplementary evidence is considered bound to the applicant.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'BIN-8.4.2-01',
        'testo': "Deve essere catturato un flusso video del volto del richiedente.",
        'testo_integrale': "BIN-8.4.2-01: A video stream of the applicant's face shall be captured.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-01A',
        'testo': "La registrazione video deve utilizzare una frequenza dei fotogrammi e una risoluzione di qualita' sufficiente per il processo di identity proofing.",
        'testo_integrale': "BIN-8.4.2-01A: The video recording shall use frame rate and resolution of sufficient quality for the identity proofing process.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-02X',
        'testo': "Il processo di cattura video deve applicare misure di rilevamento degli attacchi di presentazione (presentation attack detection) per garantire che il flusso video ritragga una persona viva presente davanti alla telecamera al momento dell'identity proofing.",
        'testo_integrale': "BIN-8.4.2-02X: The video capture process shall apply presentation attack detection means to ensure that the video stream is of a live person present in front of the camera at the time of the identity proofing.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-02A',
        'testo': "La cattura video deve avvenire al momento dell'identity proofing. La presentazione di un flusso video preregistrato non e' considerata conforme ai requisiti di identity proofing per il livello Baseline o Extended LoIP.",
        'testo_integrale': "BIN-8.4.2-02A: The video capture process shall happen at the time of the identity proofing. NOTE 2: Submission of a pre-recorded video stream is considered not to meet the requirements for identity proofing to Baseline or Extended LoIP.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-03X',
        'testo': "Il processo di cattura del flusso video deve applicare misure per rilevare un aspetto del volto generato artificialmente o manipolato (attacchi cosiddetti 'deep fake').",
        'testo_integrale': "BIN-8.4.2-03X: The video stream capture shall apply means to detect artificially generated or manipulated face appearance. NOTE 5: Such attacks are sometimes termed \"deep fake\" attacks.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-04',
        'testo': "Se il flusso video e' catturato sul dispositivo del richiedente, il processo di identity proofing deve garantire che il flusso video sia trasmesso a un ambiente controllato dall'attore responsabile del processo di identity proofing in modo da assicurarne autenticita', integrita' e riservatezza.",
        'testo_integrale': "BIN-8.4.2-04: [CONDITIONAL] If the video stream is captured on the applicant's device, the identity proofing process shall ensure that the video stream is transmitted to an environment controlled by the actor responsible for the identity proofing process in a manner that ensures authenticity, integrity, and confidentiality of the video stream.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto; inoltre, il flusso video e' catturato sul dispositivo del richiedente.",
    },
    {
        'riferimento': 'BIN-8.4.2-04A',
        'testo': "Il processo di identity proofing deve applicare misure di prevenzione e rilevamento degli attacchi di iniezione biometrica, per garantire che ne' il richiedente ne' un attaccante esterno possano iniettare nel processo, senza essere rilevati, un flusso video precedentemente registrato o generato artificialmente.",
        'testo_integrale': "BIN-8.4.2-04A: The identity proofing process shall apply biometric injection attack prevention and detection means to ensure that neither the applicant nor an external attacker can undetectably inject into the process a previously recorded or artificially generated video stream.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-04B',
        'testo': "Se l'identity proofing e' mirato al livello Baseline LoIP, le misure di rilevamento degli attacchi di iniezione biometrica devono essere sottoposte a test da parte di un laboratorio accreditato secondo ETSI TS 18099, livello Substantial (livello 2), al piu' tardi entro la fine del 2026.",
        'testo_integrale': "BIN-8.4.2-04B: [CONDITIONAL] If the identity proofing targets Baseline LoIP, the biometric injection attack detection means shall be tested by an accredited laboratory according to TS 18099 [5] level Substantial (level 2) at the latest before the end of 2026.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto; inoltre, l'identity proofing e' mirato al livello Baseline LoIP.",
    },
    {
        'riferimento': 'BIN-8.4.2-04C',
        'testo': "Se l'identity proofing e' mirato al livello Extended LoIP, le misure di rilevamento degli attacchi di iniezione biometrica devono essere sottoposte a test da parte di un laboratorio accreditato secondo ETSI TS 18099, livello High (livello 3), al piu' tardi entro la fine del 2026.",
        'testo_integrale': "BIN-8.4.2-04C: [CONDITIONAL] If the identity proofing targets Extended LoIP, the biometric injection attack detection means shall be tested by an accredited laboratory according to TS 18099 [5] level High (level 3) at the latest before the end of 2026.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto; inoltre, l'identity proofing e' mirato al livello Extended LoIP.",
    },
    {
        'riferimento': 'BIN-8.4.2-04D',
        'testo': "La valutazione delle misure di rilevamento degli attacchi di iniezione biometrica da parte di un laboratorio accreditato secondo ETSI TS 18099 deve essere ripetuta almeno ogni due anni. Indipendentemente da tale valutazione, l'IPSP e' comunque tenuto a mantenere costantemente aggiornate le misure di rilevamento degli attacchi di iniezione biometrica secondo le proprie procedure di intelligence sui rischi (clausola 5 del presente documento).",
        'testo_integrale': "BIN-8.4.2-04D: Evaluation of biometric injection detection means by an accredited laboratory according to TS 18099 [5] shall be repeated at least every second year. NOTE 8: Regardless of the evaluation according to TS 18099 [5], the IPSP is required to keep biometric injection attack detection means constantly updated according to the IPSP's risk intelligence procedures, see clause 5 of the present document.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-05X',
        'testo': "Se la biometria facciale e' utilizzata per il binding al richiedente, almeno un'immagine di qualita' sufficiente per il binding al richiedente deve essere catturata come parte integrante della cattura video o estratta dal flusso video.",
        'testo_integrale': "BIN-8.4.2-05X: [CONDITIONAL] If face biometrics is used for binding to applicant, at least one image of sufficient quality for binding to applicant shall be captured integral to the video capturing or be extracted from the video stream.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto; inoltre, la biometria facciale e' utilizzata per il binding al richiedente.",
    },
    {
        'riferimento': 'BIN-8.4.2-05A',
        'testo': "Se la biometria facciale e' utilizzata per il binding al richiedente e un'immagine del volto del richiedente e' catturata nel processo, l'immagine del volto deve avere una risoluzione di qualita' sufficiente per il processo di identity proofing.",
        'testo_integrale': "BIN-8.4.2-05A: [CONDITIONAL] If face biometrics is used for binding to applicant, and a face image of the applicant is captured in the process, the face image shall have a resolution of sufficient quality for the identity proofing process.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto; inoltre, la biometria facciale e' utilizzata per il binding al richiedente e un'immagine del volto e' catturata nel processo.",
    },
    {
        'riferimento': 'BIN-8.4.2-05B',
        'testo': "Le condizioni (ad es. condizioni di illuminazione, riflessi, nitidezza) del video e delle immagini devono essere valutate; video e immagini devono essere respinti se non idonei al binding al richiedente, con istruzioni al richiedente di ripetere il processo in condizioni migliori.",
        'testo_integrale': "BIN-8.4.2-05B: The conditions (e.g. lighting conditions, reflections, sharpness) of video and images shall be assessed, and video and images shall be rejected if they are not suited for binding to applicant, with an instructions to the applicant to repeat the process under better conditions.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-05C',
        'testo': "Deve esistere un limite massimo al numero di tentativi prima che il processo venga interrotto con esito negativo.",
        'testo_integrale': "BIN-8.4.2-05C: There shall be an upper limit on the number of retries before the process is aborted with failed result.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-05D',
        'testo': "L'IPSP deve indicare nella propria dichiarazione delle pratiche (practice statement) obiettivi per i valori di APCER (tasso di errata classificazione delle presentazioni di attacco) e BPCER (tasso di errata classificazione delle presentazioni in buona fede) almeno al livello delle migliori pratiche di settore, che il servizio deve mirare a raggiungere.",
        'testo_integrale': "BIN-8.4.2-05D: The IPSP shall in its practice statement state goals for APCER (attack presentation classification error rate) and BPCER (bona fide presentation classification error rate) values that are at least at the level of industry best practice and that the service shall aim to achieve.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-05E',
        'testo': "L'IPSP deve mantenere aggiornati i propri obiettivi di APCER e BPCER sulla base della propria procedura di intelligence sulle minacce.",
        'testo_integrale': "BIN-8.4.2-05E: The IPSP shall keep its APCER and BPCER goals updated based on its threats intelligence procedure.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-06X',
        'testo': "Le misure di rilevamento degli attacchi di presentazione (PAD) e i tassi di APCER e BPCER devono essere sottoposti a test sistematici in conformita' a ISO/IEC 30107-3, rispetto a insiemi di dati di riferimento aggiornati e rispetto agli obiettivi fissati dall'IPSP.",
        'testo_integrale': "BIN-8.4.2-06X: The PAD means and APCER and BPCER rates shall be systematically tested in accordance with ISO/IEC 30107-3 [3] against updated reference data sets and against the goals set by the IPSP.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-07X',
        'testo': "Le misure PAD devono essere valutate da un laboratorio accreditato secondo ISO/IEC 19989-3, al piu' tardi entro la fine del 2026. Indipendentemente da tale valutazione, l'IPSP e' comunque tenuto a mantenere costantemente aggiornate le misure PAD secondo le proprie procedure di intelligence sui rischi (clausola 5 del presente documento).",
        'testo_integrale': "BIN-8.4.2-07X: The PAD means shall be evaluated by an accredited laboratory according to ISO/IEC 19989-3 [6] at the latest before the end of 2026. NOTE 12: Regardless of the evaluation according to ISO/IEC 19989-3 [6], the IPSP is required to keep PAD means constantly updated according to the IPSP's risk intelligence procedures, see clause 5 of the present document.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-07A',
        'testo': "La valutazione delle misure PAD da parte di un laboratorio accreditato secondo ISO/IEC 19989-3 deve essere ripetuta almeno ogni due anni.",
        'testo_integrale': "BIN-8.4.2-07A: Evaluation of PAD means by an accredited laboratory according to ISO/IEC 19989-3 [6] shall be repeated at least every second year.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-08X',
        'testo': "I risultati dei test per il PAD devono raggiungere un APCER, come definito da ISO/IEC 30107-3, conforme all'obiettivo indicato nella dichiarazione delle pratiche.",
        'testo_integrale': "BIN-8.4.2-08X: Test results for the PAD shall achieve an APCER as defined by ISO/IEC 30107-3 [3] in accordance with the goal stated in the practice statement.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.2-09X',
        'testo': "I risultati dei test per il PAD dovrebbero raggiungere un BPCER, come definito da ISO/IEC 30107-3, conforme all'obiettivo indicato nella dichiarazione delle pratiche.",
        'testo_integrale': "BIN-8.4.2-09X: Test results for the PAD should achieve BPCER as defined by ISO/IEC 30107-3 [3] in accordance with the goal stated in the practice statement.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona fisica, e' utilizzato un documento di identita' come prova, e il processo di identity proofing e' svolto da remoto.",
    },
    {
        'riferimento': 'BIN-8.4.3-01X',
        'testo': "Il processo deve fornire un confronto automatizzato affidabile tra l'immagine o le immagini del volto estratte dal documento di identita' presentato dal richiedente e l'immagine o le immagini del volto catturate secondo i requisiti della clausola 8.4.2 del presente documento.",
        'testo_integrale': "BIN-8.4.3-01X: The process shall provide a reliable, automated comparison between face image(s) extracted from the identity document presented by the applicant and face image(s) captured according to the requirements of clause 8.4.2 of the present document.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il binding al richiedente avviene tramite biometria facciale automatizzata.",
    },
    {
        'riferimento': 'BIN-8.4.3-03',
        'testo': "L'elaborazione del segnale biometrico, il confronto, la memorizzazione dei dati e la decisione devono essere svolti in un ambiente controllato dall'attore responsabile del processo di identity proofing.",
        'testo_integrale': "BIN-8.4.3-03: Biometric signal processing, comparison, data storage, and decision shall be carried out in an environment controlled by the actor responsible for the identity proofing process.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il binding al richiedente avviene tramite biometria facciale automatizzata.",
    },
    {
        'riferimento': 'BIN-8.4.3-04',
        'testo': "Se il riconoscimento facciale biometrico e' utilizzato con la presenza fisica del richiedente, devono essere utilizzate apparecchiature adeguatamente protette per leggere il documento di identita' presentato dal richiedente e ottenere un'immagine del volto del richiedente.",
        'testo_integrale': "BIN-8.4.3-04: [CONDITIONAL] If biometric face recognition is used with the physical presence of the applicant, properly secured equipment shall be used to read the identity document presented by the applicant and obtain a face image of the applicant.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il binding al richiedente avviene tramite biometria facciale automatizzata; inoltre, il riconoscimento facciale biometrico e' utilizzato con la presenza fisica del richiedente.",
    },
    {
        'riferimento': 'BIN-8.4.3-05A',
        'testo': "L'IPSP deve indicare nella propria dichiarazione delle pratiche obiettivi per i valori di FAR (tasso di falsa accettazione) e FRR (tasso di falso rigetto) almeno al livello delle migliori pratiche di settore, che il servizio deve mirare a raggiungere.",
        'testo_integrale': "BIN-8.4.3-05A: The IPSP shall in its practice statement state goals for False Acceptance Rate (FAR) and False Rejection Rate (FRR) values that are at least at the level of industry best practice and that the service shall aim to achieve.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il binding al richiedente avviene tramite biometria facciale automatizzata.",
    },
    {
        'riferimento': 'BIN-8.4.3-05B',
        'testo': "L'IPSP deve mantenere aggiornati i propri obiettivi di FAR e FRR sulla base della propria procedura di intelligence sulle minacce.",
        'testo_integrale': "BIN-8.4.3-05B: The IPSP shall keep its FAR and FRR goals updated based on its threats intelligence procedure.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il binding al richiedente avviene tramite biometria facciale automatizzata.",
    },
    {
        'riferimento': 'BIN-8.4.3-06X',
        'testo': "Gli algoritmi e le tecnologie biometriche applicate devono essere sottoposti a test sistematici in conformita' a ISO/IEC 19795-1, rispetto a insiemi di dati di riferimento aggiornati e rispetto agli obiettivi fissati dall'IPSP.",
        'testo_integrale': "BIN-8.4.3-06X: The biometric algorithms and technologies applied shall be systematically tested in accordance with ISO/IEC 19795-1 [4] against updated reference data sets and against the goals set by the IPSP.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il binding al richiedente avviene tramite biometria facciale automatizzata.",
    },
    {
        'riferimento': 'BIN-8.4.3-07X',
        'testo': "I risultati dei test per il riconoscimento facciale biometrico devono raggiungere un FAR conforme all'obiettivo indicato nella dichiarazione delle pratiche.",
        'testo_integrale': "BIN-8.4.3-07X: Test results for the biometric face recognition shall achieve FAR in accordance with the goal stated in the practice statement.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il binding al richiedente avviene tramite biometria facciale automatizzata.",
    },
    {
        'riferimento': 'BIN-8.4.3-08X',
        'testo': "I risultati dei test per il riconoscimento facciale biometrico dovrebbero raggiungere un FRR (tasso di falso rigetto) conforme all'obiettivo indicato nella dichiarazione delle pratiche.",
        'testo_integrale': "BIN-8.4.3-08X: Test results for the biometric face recognition should achieve False Rejection Rate (FRR) in accordance with the goal stated in the practice statement.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il binding al richiedente avviene tramite biometria facciale automatizzata.",
    },
    {
        'riferimento': 'BIN-8.4.3-09X',
        'testo': "Il riconoscimento facciale biometrico dovrebbe applicare misure per rilevare fotografie manipolate per fusione del volto di due o piu' persone diverse in un'unica immagine ('morphed'), che rischiano di essere riconosciute come appartenenti a piu' persone diverse sia da un operatore di registrazione sia dalla biometria facciale. Tali misure sono applicate al meglio nella fase di binding al richiedente, quando una nuova fotografia del richiedente, nota per non essere manipolata, puo' essere confrontata con la fotografia di riferimento potenzialmente manipolata.",
        'testo_integrale': "BIN-8.4.3-09X: The biometric face recognition should apply means to detect morphed photos in identity documents. NOTE 7: A morphed photo is created by merging the face photos of two or more different persons into one photo. Since some countries allow persons to bring their own photo for issuing a passport or national identity card, there is a risk that documents are issued with morphed photos. With a morphed photo, there is a risk that both/all the persons can be recognized both by a registration officer and by face biometrics with a reliability above the applied threshold, meaning more than one person can use the identity document containing the morphed photo. NOTE 8: Morphing detection means are best applied in the binding to applicant step of an identity proofing process when a new photo, known not to be morphed, of the applicant can be compared to the potentially morphed reference photo. The upcoming ISO/IEC 20059 [i.33] \"Methodologies to evaluate the resistance of biometric recognition systems to morphing attacks\" can in the future provide guidance.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il binding al richiedente avviene tramite biometria facciale automatizzata.",
    },
    {
        'riferimento': 'BIN-8.4.4-01X',
        'testo': "L'operatore di registrazione deve confrontare l'immagine del volto ottenuta dal documento di identita' del richiedente con l'aspetto fisico del richiedente, ricavato dalla presenza fisica del richiedente, da una sequenza video catturata secondo i requisiti della clausola 8.4.2 del presente documento, oppure da immagini derivate da o catturate insieme alla sequenza video.",
        'testo_integrale': "BIN-8.4.4-01X: The registration officer shall compare the face image obtained from the applicant's identity document with the applicant's physical appearance, either from the applicant's physical presence, from a video sequence captured according to the requirements of clause 8.4.2 of the present document, or from image(s) derived from or captured together with the video sequence.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando e' utilizzato il binding manuale del richiedente a un documento di identita'.",
    },
    {
        'riferimento': 'BIN-8.4.4-02',
        'testo': "L'operatore di registrazione che effettua il binding al richiedente deve ricevere una formazione prima di essere autorizzato a effettuare qualunque confronto, con formazione ripetuta o aggiornata almeno annualmente.",
        'testo_integrale': "BIN-8.4.4-02: The registration officer performing the binding to applicant shall receive training before being allowed to make any comparison, with training repeated or refreshed at least yearly.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando e' utilizzato il binding manuale del richiedente a un documento di identita'.",
    },
    {
        'riferimento': 'BIN-8.4.4-03',
        'testo': "L'operatore di registrazione deve effettuare un'analisi morfologica secondo un elenco di caratteristiche definito.",
        'testo_integrale': "BIN-8.4.4-03: The registration officer shall perform a morphological analysis according to a defined feature list.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando e' utilizzato il binding manuale del richiedente a un documento di identita'.",
    },
    {
        'riferimento': 'BIN-8.4.4-04X',
        'testo': "All'operatore di registrazione deve essere consentito di dedicare tempo sufficiente al confronto dei volti e deve disporre di condizioni di lavoro che non compromettano il suo giudizio. In generale, una valutazione secondo le linee guida FISWG sul confronto facciale puo' essere sufficiente, mentre una revisione secondo lo stesso documento puo' essere richiesta almeno per l'identity proofing da remoto.",
        'testo_integrale': "BIN-8.4.4-04X: The registration officer shall be allowed to spend sufficient time for the face comparison and have working conditions that do not impede the registration officer's judgement. NOTE 1: In general, an assessment according to the FISWG Facial Comparison Overview and Methodology Guidelines [i.20] can be sufficient, while a review according to the same document can be required at least for remote identity proofing.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando e' utilizzato il binding manuale del richiedente a un documento di identita'.",
    },
    {
        'riferimento': 'BIN-8.4.4-05',
        'testo': "L'operatore di registrazione dovrebbe disporre di strumenti per ingrandire le immagini al fine di visualizzarne i dettagli (ad es. una lente di ingrandimento in presenza fisica con documento fisico, oppure strumenti informatici quando sono utilizzate immagini del volto).",
        'testo_integrale': "BIN-8.4.4-05: The registration officer should have tools available to magnify images to view details. NOTE 2: With physical presence and physical identity document, this can be a magnifying glass for the face image printed on the document. If face images are used, computerized tools are assumed.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando e' utilizzato il binding manuale del richiedente a un documento di identita'.",
    },
    {
        'riferimento': 'BIN-8.4.4-06',
        'testo': "Se il binding al richiedente e' effettuato mediante confronto di immagini del volto o sequenze video, l'operatore di registrazione dovrebbe utilizzare strumenti informatizzati nel confronto dei volti.",
        'testo_integrale': "BIN-8.4.4-06: [CONDITIONAL] If binding to applicant is done by comparing face images or video sequences, the registration officer should use computerized tools in the face comparison.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando e' utilizzato il binding manuale del richiedente a un documento di identita'; inoltre, il binding al richiedente e' effettuato mediante confronto di immagini del volto o sequenze video.",
    },
    {
        'riferimento': 'BIN-8.4.5-01',
        'testo': "La prova convalidata deve dimostrare che la persona giuridica esiste e che la richiesta al servizio fiduciario costituisce un atto volontario compiuto per conto della persona giuridica.",
        'testo_integrale': "BIN-8.4.5-01: Validated evidence shall prove that the legal person exists and that the application to the trust service is a willful act carried out on behalf of the legal person.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Si applica quando il richiedente e' una persona giuridica o una persona fisica che rappresenta una persona giuridica.",
    },
    {
        'riferimento': 'BIN-8.4.5-02X',
        'testo': "Se il richiedente e' una persona fisica che rappresenta una persona giuridica, l'identita' della persona fisica deve essere dimostrata secondo un caso d'uso applicabile della clausola 9 o dell'Annex C del presente documento.",
        'testo_integrale': "BIN-8.4.5-02X: [CONDITIONAL] If the applicant is a natural person representing a legal person, the identity of the natural person shall be proven according to an applicable use case from clause 9 or Annex C of the present document.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Il richiedente e' una persona fisica che rappresenta una persona giuridica.",
    },
    {
        'riferimento': 'BIN-8.4.5-03',
        'testo': "Se il richiedente e' una persona fisica che rappresenta una persona giuridica, la prova convalidata deve dimostrare l'autorizzazione della persona fisica a rappresentare la persona giuridica.",
        'testo_integrale': "BIN-8.4.5-03: [CONDITIONAL] If the applicant is a natural person representing a legal person, validated evidence shall prove the natural person's authorization to represent the legal person.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Il richiedente e' una persona fisica che rappresenta una persona giuridica.",
    },
    {
        'riferimento': 'BIN-8.4.5-04X',
        'testo': "Se il richiedente e' una persona fisica che rappresenta una persona giuridica e la persona giuridica e' elencata in un registro fidato, l'autorizzazione della persona fisica a rappresentare la persona giuridica dovrebbe essere dimostrata tramite informazioni provenienti da tale registro. Cio' implica che la persona fisica ricopra uno dei ruoli elencati nel registro fidato e che tale ruolo sia autorizzato a rappresentare la persona giuridica nel contesto dell'identity proofing. Il registro fidato puo' costituire una fonte autentica ai sensi del regolamento eIDAS come modificato, e la prova puo' essere veicolata sotto forma di attestazione elettronica di attributi, qualificata o non qualificata, ai sensi dello stesso regolamento.",
        'testo_integrale': "BIN-8.4.5-04X: [CONDITIONAL] If the applicant is a natural person representing a legal person, and the legal person is listed in a trusted register, the natural person's authorization to represent the legal person should be proven by information from that register. NOTE 1: This implies that the natural person has one of the roles listed in the trusted register and that this role is authorized to represent the legal person in the identity proofing context. NOTE 2: The trusted register can be an authentic source as defined by the amended eIDAS regulation [i.25] and the evidence can be conveyed as a qualified or non-qualified electronic attestation of attributes as defined by the same regulation.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Il richiedente e' una persona fisica che rappresenta una persona giuridica, e la persona giuridica e' elencata in un registro fidato.",
    },
    {
        'riferimento': 'ISS-8.5.1-01',
        'testo': "Il risultato dell'identity proofing deve essere consegnato in modo sicuro al prestatore di servizi fiduciari, per quanto riguarda autenticita', integrita' e riservatezza del risultato.",
        'testo_integrale': "ISS-8.5.1-01: The result of the identity proofing shall be delivered securely to the trust service provider, regarding the authenticity, integrity, and confidentiality of the result.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'ISS-8.5.1-02',
        'testo': "Il risultato del processo di identity proofing deve trasmettere il livello di garanzia dell'identity proofing (LoIP) raggiunto dal processo per gli attributi di identita' richiesti ai fini dell'identificazione univoca del richiedente nel contesto dell'identity proofing.",
        'testo_integrale': "ISS-8.5.1-02: The result of the identity proofing process shall convey the LoIP achieved by the identity proofing process for the identity attributes required for the unique identification of the applicant in the identity proofing context.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'ISS-8.5.1-03X',
        'testo': "Se il processo di identity proofing trasmette attributi di identita' non richiesti per l'identificazione univoca nel contesto dell'identity proofing e la cui garanzia differisce dal LoIP del risultato complessivo del processo, un'indicazione della garanzia differente dovrebbe essere trasmessa nel risultato dell'identity proofing.",
        'testo_integrale': "ISS-8.5.1-03X: [CONDITIONAL] If the identity proofing process conveys identity attributes that are not required for unique identification in the identity proofing context, and whose assurance differ from the LoIP of the overall result of the identity proofing process, an indication of the differing assurance should be conveyed in the identity proofing result.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
        'condizione_applicabilita': "Il processo di identity proofing trasmette attributi di identita' non richiesti per l'identificazione univoca nel contesto dell'identity proofing, la cui garanzia differisce dal LoIP del risultato complessivo del processo.",
    },
    {
        'riferimento': 'ISS-8.5.2-01',
        'testo': "Le prove del processo di identity proofing - nel senso di informazioni di audit sul processo in se', distinte dalla prova autorevole/supplementare usata per la verifica dell'identita' (cfr. anche clausola 7.10 del presente documento) - devono essere raccolte e conservate in conformita' al contesto dell'identity proofing. Le prove possono essere conservate in formato digitale o cartaceo; la necessita' di conservare le prove di processi non completati con successo puo' essere determinata dal contesto dell'identity proofing; la raccolta e la conservazione delle prove sono necessarie per conformarsi alla normativa applicabile in materia di protezione dei dati, in particolare al GDPR se il processo di identity proofing e' svolto ai sensi della legislazione di uno Stato membro UE.",
        'testo_integrale': "ISS-8.5.2-01: Evidence of the identity proofing process shall be gathered and retained in compliance with the identity proofing context. NOTE 1: In this clause 8.5.2, the term \"evidence\" means audit information for the identity proofing process as such, and not authoritative or supplementary evidence as in other clauses of the document. See also clause 7.10 of the present document. NOTE 2: Evidence can be retained in digital or paper format. NOTE 3: The need to retain evidence of identity proofing processes that did not complete successfully can be determined by the identity proofing context. NOTE 4: Gathering and retention of evidence is required to comply with applicable data protection legislation, notably GDPR if the identity proofing process is carried out under the legislation of an EU Member State.",
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'ISS-8.5.2-02X',
        'testo': "Le prove del processo di identity proofing devono documentare la prova autorevole e la prova supplementare utilizzate nel processo di identity proofing e l'emittente o la fonte di tale prova.",
        'testo_integrale': "ISS-8.5.2-02X: The evidence of the identity proofing process shall document the authoritative and supplementary evidence used in the identity proofing process and the issuer or source of that evidence.",
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'ISS-8.5.2-03',
        'testo': "Le prove del processo di identity proofing dovrebbero documentare in modo completo il processo di identity proofing.",
        'testo_integrale': "ISS-8.5.2-03: The evidence of the identity proofing process should completely document the identity proofing process.",
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'ISS-8.5.2-04',
        'testo': "Le prove del processo di identity proofing devono essere conservate per il periodo di conservazione necessario stabilito dal contesto dell'identity proofing.",
        'testo_integrale': "ISS-8.5.2-04: Evidence of the identity proofing process shall be retained for the necessary retention time given by the identity proofing context.",
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'ISS-8.5.2-05',
        'testo': "Le prove del processo di identity proofing devono essere conservate in modo da impedirne la manomissione (tamper-proof).",
        'testo_integrale': "ISS-8.5.2-05: The evidence of the identity proofing process shall be stored in a tamper-proof way.",
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'ISS-8.5.2-05A',
        'testo': "Il momento del completamento del processo di identity proofing deve far parte delle prove.",
        'testo_integrale': "ISS-8.5.2-05A: The time of completion of the identity proofing process shall be part of the evidence.",
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'ISS-8.5.2-06',
        'testo': "Le prove del processo di identity proofing devono essere conservate in modo da garantire la riservatezza delle informazioni.",
        'testo_integrale': "ISS-8.5.2-06: The evidence of the identity proofing process shall be stored in a way that guarantees the confidentiality of the information.",
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'ISS-8.5.2-07',
        'testo': "Le prove del processo di identity proofing devono essere conservate in modo da garantire la possibilita' di ricercare, recuperare e riverificare il risultato dell'identity proofing.",
        'testo_integrale': "ISS-8.5.2-07: The evidence of the identity proofing process shall be stored in a way that ensures the possibility to search, retrieve, and re-verify the identity proofing result.",
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'ISS-8.5.2-08',
        'testo': "Al termine del periodo di conservazione definito da ISS-8.5.2-04, le prove del processo di identity proofing e tutti i dati personali relativi al richiedente devono essere cancellati.",
        'testo_integrale': "ISS-8.5.2-08: At the end of the retention time defined by ISS 8.5.2-04, the evidence of the identity proofing process and all personal data on the applicant shall be deleted.",
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        'riferimento': 'BIN-8.4.3-02X',
        'testo': "La cattura dei dati e la valutazione preliminare della qualita' dei dati possono essere effettuate su apparecchiature controllate dal richiedente.",
        'testo_integrale': "BIN-8.4.3-02X: Data capture and preliminary data quality assessment may be done in equipment controlled by the applicant.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il binding al richiedente avviene tramite biometria facciale automatizzata.",
    },
    {
        'riferimento': 'BIN-8.4.3-05',
        'testo': "Se il riconoscimento facciale biometrico e' utilizzato con la presenza fisica del richiedente, apparecchiature installate localmente e adeguatamente protette possono essere utilizzate per l'elaborazione del riconoscimento facciale biometrico.",
        'testo_integrale': "BIN-8.4.3-05: [CONDITIONAL] If biometric face recognition is used with the physical presence of the applicant, locally installed and properly secured equipment may be used for the biometric face recognition processing.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il binding al richiedente avviene tramite biometria facciale automatizzata; inoltre, il riconoscimento facciale biometrico e' utilizzato con la presenza fisica del richiedente.",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    'BIN-8.4.1-01X', 'BIN-8.4.1-02X',
    'BIN-8.4.2-01', 'BIN-8.4.2-01A', 'BIN-8.4.2-02X', 'BIN-8.4.2-02A', 'BIN-8.4.2-03X',
    'BIN-8.4.2-04', 'BIN-8.4.2-04A', 'BIN-8.4.2-04B', 'BIN-8.4.2-04C', 'BIN-8.4.2-04D',
    'BIN-8.4.2-05X', 'BIN-8.4.2-05A', 'BIN-8.4.2-05B', 'BIN-8.4.2-05C', 'BIN-8.4.2-05D', 'BIN-8.4.2-05E',
    'BIN-8.4.2-06X', 'BIN-8.4.2-07X', 'BIN-8.4.2-07A', 'BIN-8.4.2-08X', 'BIN-8.4.2-09X',
    'BIN-8.4.3-01X', 'BIN-8.4.3-02X', 'BIN-8.4.3-03', 'BIN-8.4.3-04', 'BIN-8.4.3-05',
    'BIN-8.4.3-05A', 'BIN-8.4.3-05B', 'BIN-8.4.3-06X', 'BIN-8.4.3-07X', 'BIN-8.4.3-08X', 'BIN-8.4.3-09X',
    'BIN-8.4.4-01X', 'BIN-8.4.4-02', 'BIN-8.4.4-03', 'BIN-8.4.4-04X', 'BIN-8.4.4-05', 'BIN-8.4.4-06',
    'BIN-8.4.5-01', 'BIN-8.4.5-02X', 'BIN-8.4.5-03', 'BIN-8.4.5-04X',
    'ISS-8.5.1-01', 'ISS-8.5.1-02', 'ISS-8.5.1-03X',
    'ISS-8.5.2-01', 'ISS-8.5.2-02X', 'ISS-8.5.2-03', 'ISS-8.5.2-04', 'ISS-8.5.2-05',
    'ISS-8.5.2-05A', 'ISS-8.5.2-06', 'ISS-8.5.2-07', 'ISS-8.5.2-08',
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.3-01X'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.2-05X'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.4-01X'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.2-05X'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('obbligo', None, 'ISS-8.5.2-08'),
        'nodo_a': ('obbligo', None, 'ISS-8.5.2-04'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.95,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.5-01'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.1-01X'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.5-02X'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.5-01'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.5-03'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.5-01'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.5-04X'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.5-03'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.2-04B'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.2-04A'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.2-04C'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.2-04A'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.2-04D'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.2-04B'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.2-04D'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.2-04C'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.2-07A'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.2-07X'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.2-08X'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.2-06X'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.2-09X'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.2-06X'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.3-07X'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.3-06X'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.3-08X'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.3-06X'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'BIN-8.4.4-06'),
        'nodo_a': ('obbligo', None, 'BIN-8.4.4-01X'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'ISS-8.5.1-02'),
        'nodo_a': ('obbligo', None, 'ISS-8.5.1-01'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
    {
        'nodo_da': ('obbligo', None, 'ISS-8.5.1-03X'),
        'nodo_a': ('obbligo', None, 'ISS-8.5.1-02'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': None,
    },
]
