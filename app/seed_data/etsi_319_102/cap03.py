"""ETSI EN 319 102-1 V1.4.1 (2024-06) - Electronic Signatures and
Infrastructures (ESI); Procedures for Creation and Validation of AdES Digital
Signatures; Part 1: Creation and Validation. Capitolo 3: clausola 5.1
(Signature validation model: modello di convalida e requisiti generali).
Testo ufficiale in app/.source_cache/etsi_319_102/cap03.txt (raw completo in
app/.source_cache/etsi_319_102/raw.txt). Manifest di split:
app/.source_cache/etsi_319_102/manifest.json.

Copertura (ADR-0007): un nodo per ogni clausola/sottoclavola numerata con
contenuto proprio - 5.1.1, 5.1.2, 5.1.3, 5.1.4.1, 5.1.4.2, 5.1.4.3, 5.1.4.4
(7 item di indice, 7 Obblighi, 0 Principi). Le due intestazioni di puro
raggruppamento - 5.1 ("Signature validation model") e 5.1.4 ("Validation
constraints") - non contengono nulla oltre il titolo e sono immediatamente
seguite dalla prima sottoclausola: nessun nodo e nessun item di indice, la
loro materia e' interamente nelle sottoclausole (stesso criterio applicato
alle intestazioni di raggruppamento delle altre fonti ETSI del censimento,
es. ETSI TS 119 312 clausole 5, 5.2, 6, 6.2, 6.2.2, 6.4). La clausola 2
(References) non ricade in questo capitolo ed e' paratesto: mai un nodo.
Nessuna sezione "History" nella porzione assegnata.

Nessun Principio in questa porzione: tutte e 7 le clausole contengono almeno
un "shall"/"should" con destinatario individuabile (la Signature Validation
Application e il processo di convalida che essa esegue), quindi la regola
"chi impone un comportamento -> Obbligo" prevale in tutti i casi. Anche le
parti dichiarative (il modello concettuale SVA/DA di 5.1.1, le semantiche
delle indicazioni di stato delle Tabelle 5-6, le Tabelle 6-7) restano
assorbite nel nodo Obbligo della clausola che le ospita: la clausola e'
indivisibile (nessuna numerazione propria delle frasi) e lo schema ha un
solo tipo prescrittivo. Precedente identico: ETSI TS 119 432 clausola 5.1
(Introduction) modellata come Obbligo perche' contiene un "shall" con
soggetto esplicito.

Classificazione per clausola:
- 5.1.1 (General requirements) -> Obbligo "procedurale": il "shall" centrale
  ("The SVA shall validate the signature against a signature validation
  policy ... and shall output a status indication and validation report") e
  i valori ammessi per lo stato di un building block e per lo stato della
  convalida completa (PASSED/FAILED/INDETERMINATE;
  TOTAL-PASSED/TOTAL-FAILED/INDETERMINATE) sono il quadro procedurale della
  convalida; il modello concettuale (SVA/DA) e' il perimetro in cui il
  requisito opera.
- 5.1.2 (Selecting validation processes) -> Obbligo "procedurale": scelta del
  processo di convalida in funzione della classe di firma supportata e
  sequenza di passi 1)-7).
- 5.1.3 (Status indication ... and signature validation report) -> Obbligo
  "informativo/trasparenza": il contenuto obbligatorio del validation report
  e delle regole di indicazione (incluse le Tabelle 5, 6 e 7) e' un obbligo
  di messa a disposizione di informazioni alla DA.
- 5.1.4.1 (General requirements sui vincoli di convalida) -> Obbligo
  "procedurale": provenienza dei vincoli, tre classi di vincoli da
  supportare, obbligo di elencare i controlli disabilitati dalla policy,
  obbligo di documentare il significato degli altri vincoli implementati.
- 5.1.4.2 (X.509 Validation Constraints), 5.1.4.3 (Cryptographic
  Constraints), 5.1.4.4 (Signature Elements Constraints) -> Obbligo
  "tecnico/sicurezza": ciascuna fissa il contenuto tecnico che quella classe
  di vincoli deve indicare, con rinvio puntuale a ETSI TS 119 172-1 [4],
  clausola A.4.2.1, Tabella A.2 (righe m e p per X.509 e crittografici).

Soggetti: la categoria di soggetto del censimento non ha un valore dedicato
all'applicazione di convalida. Il soggetto grammaticale di tutte le clausole
e' l'SVA (e, in 5.1.1/5.1.3, la DA che la guida), cioe' il software di
convalida che opera dal lato di chi si affida alla firma, non il QTSP che
eroga il servizio fiduciario. Convenzione gia' adottata nel censimento per i
soggetti non-QTSP e non-utente: categoria "Terza parte" con ruolo
"obbligato" (ETSI TS 119 612 Annex B.0, applicazione che consuma la TL; ETSI
TS 119 432 cap02/cap06, driving application e relying party). Nessun
destinatario aggiuntivo valorizzato: la DA e' a sua volta software del lato
terzo affidante e ricade nella stessa categoria, quindi registrarla due volte
non aggiungerebbe informazione (la sua posizione e' nel campo `testo`).

Formulazioni non prescrittive: i "should" e i "may" restano dentro la riga
Obbligo della clausola (lo schema ha un solo tipo prescrittivo; precedente:
tutti i REQ di ETSI EN 319 401); la forza deontica e' conservata nel campo
`testo` ("deve" / "dovrebbe" / "puo'") e in `testo_integrale` resta il testo
ufficiale. Non sono state introdotte relazioni "deroga a"/"attua" per queste
sfumature: nessun riscontro testuale le collega ad altri nodi (ADR-0008).

Tabelle: la Tabella 5 (Status indications of the signature validation
process), la Tabella 6 (Validation Report Structure and Semantics) e la
Tabella 7 (Conditions for retrying validation) sono contenuto della clausola
5.1.3 che le ospita, quindi il loro contenuto e' riportato per intero nel
`testo_integrale` di quel solo nodo, una riga per record con le colonne
separate da " | " (stessa convenzione di ETSI TS 119 312). La conversione
`pdftotext -layout` spezza ogni riga della tabella su piu' righe di testo e
disallinea le colonne: la ricostruzione riguarda solo l'ordine e la
spaziatura delle colonne, nessuna cella e' stata abbreviata o riscritta. Due
celle risultano vuote nel testo ufficiale (non "-", che invece marca
esplicitamente l'assenza di dati di report in altre righe):
NO_CERTIFICATE_CHAIN_FOUND_NO_POE e OUT_OF_BOUNDS_NO_POE; sono riportate
vuote, come nel testo. Nella Tabella 6 compaiono due ellissi che sono testo
autentico dello standard, non troncature (abbreviazione di un elenco
esemplificativo dentro parentesi: "(e.g. the signature value, a
certificate...)" e "(e.g. an URI)" senza ellissi): la guardia
`verifica_completezza_testo_integrale` le riconosce tramite
`_ELLISSI_IN_PARENTESI_ESEMPLIFICATIVA` in app/seed_data/lib.py. Nella
Tabella 6 una cella di dati di report si sovrappone al testo della colonna
adiacente per effetto della conversione ("shall provide the following:process
results into" nella riga REVOKED): il testo delle due celle e' stato
ricostruito dal proprio contesto ("The validation process shall provide the
following:" / "The signature validation process results into TOTAL-FAILED
because:") senza aggiungere parole. Le intestazioni di colonna che il testo ufficiale
ripete in testa a ogni pagina della tabella ("Reported Validation
Information", "Main indication", "Sub-indication", "Associated Validation
report data", "Semantics") sono riportate una sola volta, come riga di
intestazione della tabella; le intestazioni di clausola sono portate dal
campo `riferimento`.

Figure: la Figure 11 (Conceptual Model of Signature Validation) e' un
diagramma immagine; la sua resa testuale e' un dump di riquadri disallineato
e non testo normativo, quindi - come gia' fatto per la figure 1 di ETSI TS
119 612 - e' riportata solo la sua didascalia nel flusso del `testo_integrale`
di 5.1.1. Il contenuto informativo dei riquadri (classi di vincoli, rapporto
di conformita', validation report, SD/SDR) e' comunque tutto nelle clausole
5.1.3 e 5.1.4.1.

RELAZIONI: lista vuota. I collegamenti con le altre fonti (eIDAS/eIDAS2,
regolamenti di esecuzione, altri standard ETSI citati come ETSI TS 119 172-1
o IETF RFC 5280) sono costruiti dalla sessione principale in Fase 6: questo
modulo non ne tenta nessuno, nemmeno verso le clausole interne 5.2, 5.3, 5.5
e 5.6.3, i cui nodi appartengono ad altri capitoli della stessa fonte.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 5.1.1 (General requirements)",
        "testo": (
            "Il modello concettuale divide il software con funzioni di convalida di firma in due parti: la "
            "Signature Validation Application (SVA), che riceve la firma AdES e altri input dalla Driving "
            "Application (DA), e la DA stessa. L'SVA deve convalidare la firma rispetto a una signature validation "
            "policy (insieme di vincoli di convalida) e deve produrre una indicazione di stato e un validation "
            "report che dettaglia la convalida tecnica di ciascun vincolo applicabile, informazioni rilevanti per "
            "la DA nell'interpretazione del risultato. Salvo che la DA richieda l'esecuzione di un processo di "
            "convalida specifico, la convalida parte sempre dal processo per firme che garantiscono disponibilita' "
            "e integrita' a lungo termine del materiale di convalida (clausola 5.6.3), che richiama il processo "
            "per firme con tempo e con materiale di convalida a lungo termine (5.5) e poi quello per firme di base "
            "(5.3): segue il ciclo di vita della firma (Figure 4), si arresta alla prima conclusione definitiva "
            "(positiva o negativa) e altrimenti prosegue per classi di firma aumentate (firma con tempo, con "
            "materiale LTV, con disponibilita'/integrita' a lungo termine) fino a esaurimento; il risultato "
            "dell'ultimo processo applicato e' il risultato finale, che puo' restare indeterminato per carenza di "
            "informazioni. Lo stato di ogni singolo validation building block (clausola 5.2) deve essere uno fra "
            "PASSED, FAILED o INDETERMINATE. Lo stato della convalida completa di una classe di firma nel contesto "
            "di una data policy deve essere: TOTAL-PASSED quando i controlli crittografici della firma (incluse le "
            "impronte degli oggetti firmati indirettamente) e tutti i controlli prescritti dalla policy sono "
            "superati; TOTAL-FAILED quando i controlli crittografici sono falliti, o e' provato che il "
            "certificato di firma era invalido al momento della generazione, o la firma non e' conforme a uno "
            "degli standard di base al punto che il building block di verifica crittografica non puo' elaborarla; "
            "INDETERMINATE quando gli esiti dei controlli non consentono di stabilire se la firma sia "
            "TOTAL-PASSED o TOTAL-FAILED. L'indicazione principale puo' essere accompagnata da informazioni "
            "aggiuntive (requisiti alla clausola 5.1.3). L'output dell'SVA e' destinato alla DA. Il documento non "
            "prescrive comportamenti alla DA (nessun requisito di elaborazione delle informazioni restituite): se "
            "l'SVA restituisce TOTAL-PASSED la DA dovrebbe considerare la firma tecnicamente valida secondo i "
            "vincoli di convalida (NOTE 1: cio' non significa che sia utile a uno scopo particolare); se "
            "TOTAL-FAILED la DA non dovrebbe considerarla tecnicamente valida; su INDETERMINATE, se la "
            "sotto-indicazione segnala che il risultato puo' cambiare rieseguendo l'algoritmo, la DA puo' "
            "ritentare la convalida con informazioni aggiuntive o in un momento successivo, altrimenti "
            "l'accettazione e' decisa dalla DA o dall'utente nell'ambito del controllo delle regole di "
            "applicabilita'. Su esito INDETERMINATE il risultato puo' cambiare a una nuova esecuzione (Tabella 7 "
            "elenca sotto-indicazioni e condizioni). Il documento presenta il processo di convalida in forma di "
            "algoritmi, che costituiscono il comportamento conforme di un'applicazione di convalida; "
            "implementazioni alternative sono ammesse purche' producano la stessa indicazione di stato principale "
            "a parita' di input (NOTE 3: applicazione su PC con interfaccia grafica, servizio web, applicazione "
            "web, strumento a riga di comando, libreria integrata o middleware)."
        ),
        "testo_integrale": (
            "This clause defines the conceptual model shown in Figure 11 by dividing software with signature "
            "validation functions into two parts:\n"
            "- a Signature Validation Application (SVA); and\n"
            "- a Driving Application (DA).\n"
            "A Signature Validation Application (SVA) receives an AdES digital signature and other input from the "
            "Driving Application (DA).\n"
            "The SVA shall validate the signature against a signature validation policy, consisting of a set of "
            "validation constraints, and shall output a status indication and validation report providing the "
            "details of the technical validation of each of the applicable constraints, which can be relevant for "
            "the DA in interpreting the results.\n"
            "Unless the DA requests the SVA to execute a specific validation process, validation always starts "
            "with the validation process for Signature providing Long Term Availability and Integrity of "
            "Validation Material (see clause 5.6.3). One of the first steps of this process is to call the process "
            "for Signatures with Time and Signatures with Long-Term Validation Material (see clause 5.5) which "
            "again calls the process for Basic Signatures (see clause 5.3). In effect, the validation follows the "
            "signature lifecycle as depicted in Figure 4 and evaluates the status of the signature based on the "
            "validation process for the first signature class of that lifecycle (Basic Signature) first. If this "
            "leads to a definitive validation conclusion (positive or negative) the validation can be stopped. "
            "However, it is possible that this signature class does not offer the information that is required to "
            "come to a definitive conclusion. In that case, the validation continues with the validation process "
            "for the next augmented signature class (Signature with Time, Signature with Long-Term Validation "
            "Material, Signature providing Long Term Availability and Integrity of Validation Material), until "
            "either a definitive conclusion is possible or no further validation process for an augmented "
            "signature class is available. The validation result of the signature validation process applied last "
            "is then the final validation result for the signature (which may remain undetermined for lack of "
            "information).\n"
            "In order to conclude the validation of one of the signature classes, several validation building "
            "blocks are applied (see clause 5.2). The status indication of each single validation building block "
            "shall be one of the following values: PASSED, FAILED or INDETERMINATE. The exact meaning of these "
            "status indications are defined in the building blocks below.\n"
            "The status on the full validation of one of the signature classes in the context of a particular "
            "signature validation policy shall be:\n"
            "TOTAL-PASSED: when the cryptographic checks of the signature (including checks of hashes of "
            "individual data objects that have been signed indirectly) succeeded as well as all checks prescribed "
            "by the signature validation policy have been passed.\n"
            "TOTAL-FAILED: the cryptographic checks of the signature failed (including checks of hashes of "
            "individual data objects that have been signed indirectly), or it is proven that the signing "
            "certificate was invalid at the time of generation of the signature, or because the signature is not "
            "conformant to one of the base standards to the extent that the cryptographic verification building "
            "block is unable to process it.\n"
            "INDETERMINATE: the results of the performed checks do not allow to ascertain the signature to be "
            "TOTAL-PASSED or TOTAL-FAILED.\n"
            "The main status indication can be accompanied by additional information. Detailed requirements are "
            "specified in clause 5.1.3.\n"
            "The output of the SVA is meant to be processed by the DA (e.g. to be presented to the verifier).\n"
            "Figure 11: Conceptual Model of Signature Validation\n"
            "The present document does not stipulate any required behaviour by the DA, especially no processing "
            "requirements for any of the returned information, since this is application specific and out of the "
            "scope of the present document. However:\n"
            "- If SVA returns TOTAL-PASSED for a certain signature, DA should consider the signature as a "
            "technically valid signature according to the validation constraints.\n"
            "NOTE 1: This does not necessarily mean that the signature is useful for a particular purpose.\n"
            "- If SVA returns TOTAL-FAILED, the DA should not consider the signature as technically valid.\n"
            "- In case the SVA returns INDETERMINATE, if the subindication indicates the result can change when "
            "rerunning the algorithm, the DA may retry validation based on additional information or at a later "
            "point in time. In all other cases, the acceptation of the signature has to be determined by the DA, "
            "or beyond, by the user, as part of the applicability rules checking.\n"
            "When the status indication is INDETERMINATE, the result may change when the DA runs the validation "
            "process again at a later point in time. Table 7 lists the subindications for the INDETERMINATE "
            "indication and corresponding conditions necessary to allow the validation results to be different "
            "when the DA reruns the validation process.\n"
            "NOTE 2: This assumes that the SVA was able to process all validation constraints. There can be cases, "
            "where this cannot be done. For example, if the validation constraints state that the claimed signing "
            "time of a signature is assumed to be the actual signing time even if there are no proofs of "
            "existence for that fact, and the SVA is unable to take this consideration into the decision process, "
            "the SVA will return INDETERMINATE with an indication for the reason. This will allow the DA to still "
            "accept the signature as valid according to the policy in place.\n"
            "The present document presents the validation process in the form of algorithms, which provide a "
            "conformant behaviour when implemented by a signature validation application.\n"
            "Alternative implementations may be used provided that they produce the same main status indication "
            "when given the same set of input information.\n"
            "NOTE 3: There are varieties of ways to implement the signature validation procedures, such as:\n"
            "- running as (part of) an application software on a device like a PC with a graphical user "
            "interface;\n"
            "- as a web service;\n"
            "- a web application;\n"
            "- a command-line tool;\n"
            "- an integrated library or a middleware for other applications."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.1.2 (Selecting validation processes)",
        "testo": (
            "Selezione del processo di convalida in funzione della classe di firma che l'SVA sa convalidare. "
            "Supportando solo la convalida di firme di base, l'SVA deve supportare il processo di convalida per "
            "firme di base (clausola 5.3), processo che puo' essere selezionato per firme in cui il momento della "
            "convalida cade nel periodo di validita' del certificato di firma e il certificato non e' revocato "
            "(NOTE: la convalida di firme con certificati scaduti ma non revocati dipende dalla policy in uso, che "
            "puo' benissimo ammettere il processo per firme di base per una firma creata due giorni prima con "
            "certificato scaduto il giorno prima); tale processo puo' essere usato a prescindere dalla classe di "
            "firma presentata (firma di base, con tempo, con materiale di convalida a lungo termine, con "
            "disponibilita' e integrita' a lungo termine del materiale di convalida), ignorando il materiale "
            "aggiuntivo presente negli attributi, e i certificati e i dati di revoca raccolti in quella convalida "
            "possono essere usati per creare una firma con materiale di convalida a lungo termine. Supportando la "
            "convalida di firme con tempo e con materiale LTV, l'SVA deve supportare il processo per firme di base "
            "(5.3) e il processo per firme con tempo e con materiale LTV (5.5) e deve saper usare i dati di "
            "convalida memorizzati nella firma. Supportando la convalida di firme con disponibilita' e integrita' "
            "a lungo termine del materiale di convalida, deve supportare i processi 5.3, 5.5 e 5.6. Nel convalidare "
            "una firma l'SVA dovrebbe procedere per passi: 1) se la DA non richiede un processo specifico, o "
            "l'SVA non supporta la selezione di un processo dedicato, va al passo 2; se richiede il processo per "
            "firme di base va al passo 4; se richiede il processo per firme con tempo e materiale LTV va al passo "
            "3; se richiede il processo per firme con disponibilita' e integrita' a lungo termine va al passo 2; "
            "2) se l'SVA non supporta il processo per firme con disponibilita' e integrita' a lungo termine passa "
            "al passo successivo, altrimenti lo esegue e va al passo 5; 3) se non supporta il processo per firme "
            "con tempo e materiale LTV passa al passo successivo, altrimenti lo esegue e va al passo 5; 4) esegue "
            "il processo per firme di base; 5) se il processo selezionato ha restituito PASSED fornisce alla DA "
            "TOTAL-PASSED con le informazioni della clausola 5.1.3; 6) se ha restituito FAILED fornisce "
            "TOTAL-FAILED con le informazioni della clausola 5.1.3; 7) altrimenti fornisce INDETERMINATE con le "
            "informazioni della clausola 5.1.3."
        ),
        "testo_integrale": (
            "The clauses below offer several validation processes. Depending on the classes of signatures an SVA "
            "is able to validate, an appropriate validation process needs to be selected if multiple choices are "
            "possible:\n"
            "- When supporting only validation of Basic Signatures, the SVA shall support the Validation Process "
            "for Basic Signatures (clause 5.3). This process may be selected for signatures where the time of "
            "validation lies within the validity period of the signing certificate and the signing certificate "
            "has not been revoked.\n"
            "NOTE: Validation of signatures where involved certificates are expired at validation time, but not "
            "revoked, depends on the signature validation policy in use. A policy can e.g. well allow using the "
            "Validation Process for Basic Signatures for validating a signature that has been created two days "
            "ago, and the involved certificate expired yesterday.\n"
            "The Validation Process for Basic Signatures may be used irrespective of the class of signature "
            "presented: Basic Signatures, Signatures with Time, Signatures with Long-Term Validation Material and "
            "Signatures providing Long Term Availability and Integrity of Validation Material. Any additional "
            "material present in attributes may be ignored.\n"
            "Certificate and revocation data collected during that validation may be used to create a Signature "
            "with Long-Term Validation Material.\n"
            "- When supporting validation for Signatures with Time and Signatures with Long-Term Validation "
            "Material, the SVA shall support the Validation Process for Basic Signatures (clause 5.3), and the "
            "Validation Process for Signatures with Time and Signatures with Long-Term Validation Material (see "
            "clause 5.5). The SVA shall also be able to use the validation data stored within the signature for "
            "validation.\n"
            "- When supporting validation for Signatures providing Long Term Availability and Integrity of "
            "Validation Material, the SVA shall support the Validation Process for Basic Signatures (clause 5.3), "
            "the Validation Process for Signatures with Time and Signatures with Long-Term Validation Material "
            "(see clause 5.5) and the Validation process for Signatures providing Long Term Availability and "
            "Integrity of Validation Material (see clause 5.6).\n"
            "When validating an instance of a signature, the SVA should proceed as follows:\n"
            "1) When the DA:\n"
            "a) does not require the SVA to perform a specific validation process or if the SVA does not support "
            "selection of a dedicated validation process, the SVA shall go to step 2);\n"
            "b) requires the SVA to perform the Validation Process for Basic Signatures, the SVA shall go to step "
            "4);\n"
            "c) requires the SVA to perform the Validation Process for Signatures with Time and Signatures with "
            "Long-Term Validation Material, the SVA shall go to step 3);\n"
            "d) requires the SVA to perform the Validation process for Signatures providing Long Term "
            "Availability and Integrity of Validation Material, the SVA shall go to step 2).\n"
            "2) If the SVA does not support the Validation process for Signatures providing Long Term "
            "Availability and Integrity of Validation Material, the SVA shall go to the next step. Otherwise, it "
            "shall perform the Validation process for Signatures providing Long Term Availability and Integrity "
            "of Validation Material and it shall go to step 5).\n"
            "3) If the SVA does not support the Validation Process for Signatures with Time and Signatures with "
            "Long-Term Validation Material, the SVA shall go to the next step. Otherwise, it shall perform the "
            "Validation Process for Signatures with Time and Signatures with Long-Term Validation Material and "
            "it shall go to step 5).\n"
            "4) The SVA shall perform the Validation Process for Basic Signatures.\n"
            "5) When the selected validation process returned the status indication PASSED, the SVA shall provide "
            "the status indication TOTAL-PASSED together with the information as defined in clause 5.1.3 to the "
            "DA.\n"
            "6) When the selected validation process returned the status indication FAILED, the SVA shall provide "
            "the status indication TOTAL-FAILED together with the information as defined in clause 5.1.3 to the "
            "DA.\n"
            "7) Otherwise, the SVA shall provide the status indication INDETERMINATE together with the "
            "information as defined in clause 5.1.3 to the DA."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": (
            "clausola 5.1.3 (Status indication of the signature validation process and signature validation "
            "report)"
        ),
        "testo": (
            "L'SVA deve fornire un report completo della convalida, che consenta alla DA di ispezionare le "
            "decisioni prese durante la convalida e di risalire alle cause dettagliate dell'indicazione di stato; "
            "la clausola fissa i requisiti minimi del contenuto del report e impone che la DA, quando e' "
            "coinvolto un utente umano, lo sappia presentare in modo comprensibile all'utente. In ogni caso il "
            "processo di convalida deve produrre: l'indicazione di stato del risultato (Tabella 5), l'indicazione "
            "della policy o dell'insieme di vincoli rispetto a cui la firma e' stata convalidata, la data e ora in "
            "cui lo stato e' stato determinato con i dati di convalida impiegati (NOTE 1: per le firme di base e' "
            "il momento corrente, per firme con tempo, con materiale LTV o con disponibilita' e integrita' a lungo "
            "termine puo' essere anche un istante passato) e il processo di convalida usato (clausole 5.3, 5.5 e "
            "5.6.3). In aggiunta il processo dovrebbe produrre i dati di report aggiuntivi delle Tabelle 5 e 6 e "
            "puo' produrre una sotto-indicazione di stato (Tabella 6: valori possibili e dati di report associati) "
            "e altre voci di dati estratte dalla firma. Regole per le indicazioni restituite dall'SVA: su esito "
            "PASSED del processo selezionato in 5.1.2 il risultato complessivo deve essere TOTAL-PASSED e l'SVA "
            "dovrebbe restituire i dati di Tabella 5; su esito FAILED il risultato deve essere TOTAL-FAILED, l'SVA "
            "deve restituire una sotto-indicazione di Tabella 6 e dovrebbe restituire i dati di Tabella 5 e 6; su "
            "esito INDETERMINATE il risultato deve essere INDETERMINATE e l'SVA dovrebbe restituire i dati di "
            "Tabella 5, e inoltre, quando una o piu' sotto-indicazioni di Tabella 6 sono mappabili alla causa "
            "dell'INDETERMINATE, deve restituirne una corrispondente e dovrebbe restituire i dati associati di "
            "Tabella 6, mentre negli altri casi deve restituire una diagnostica personalizzata della causa "
            "(NOTE 2: le cause finali possono dipendere dall'implementazione). Riproducibilita' con esito "
            "TOTAL-PASSED o TOTAL-FAILED: a) a parita' di input ogni esecuzione dell'SVA deve restituire "
            "rispettivamente TOTAL-PASSED o TOTAL-FAILED; b) con gli stessi input e dati di convalida aggiuntivi "
            "(es. piu' certificati o informazioni sullo stato di revoca) il risultato deve restare quello del "
            "punto a); c) con gli stessi input e POE aggiuntivi (es. marca temporale) il risultato puo' differire. "
            "Con esito INDETERMINATE: a) a parita' di input deve restituire INDETERMINATE; b) con gli stessi "
            "input e dati di convalida aggiuntivi puo' restituire TOTAL-PASSED, TOTAL-FAILED o INDETERMINATE "
            "(NOTE 4: la data/ora di esecuzione e' un input implicito; NOTE 5: 'stessi input' comprende la policy "
            "o l'insieme di vincoli di convalida usati). Tabelle di contenuto: Tabella 5 elenca i tre stati "
            "principali (TOTAL-PASSED, TOTAL-FAILED, INDETERMINATE) con i dati di report associati e la semantica "
            "(TOTAL-PASSED richiede formato, controlli crittografici e validazione positiva dei vincoli sul "
            "certificato del firmatario, con output della catena di certificati validata); Tabella 6 elenca 6 "
            "sotto-indicazioni per TOTAL-FAILED (FORMAT_FAILURE, HASH_FAILURE, SIG_CRYPTO_FAILURE, REVOKED, "
            "EXPIRED, NOT_YET_VALID) e 20 per INDETERMINATE (SIG_CONSTRAINTS_FAILURE, CHAIN_CONSTRAINTS_FAILURE, "
            "CERTIFICATE_CHAIN_GENERAL_FAILURE, CRYPTO_CONSTRAINTS_FAILURE, POLICY_PROCESSING_ERROR, "
            "SIGNATURE_POLICY_NOT_AVAILABLE, TIMESTAMP_ORDER_FAILURE, NO_SIGNING_CERTIFICATE_FOUND, "
            "NO_CERTIFICATE_CHAIN_FOUND, NO_CERTIFICATE_CHAIN_FOUND_NO_POE, REVOKED_NO_POE, REVOKED_CA_NO_POE, "
            "OUT_OF_BOUNDS_NOT_REVOKED, OUT_OF_BOUNDS_NO_POE, REVOCATION_OUT_OF_BOUNDS_NO_POE, "
            "CRYPTO_CONSTRAINTS_FAILURE_NO_POE, NO_POE, TRY_LATER, SIGNED_DATA_NOT_FOUND, CUSTOM) con i dati di "
            "report dovuti da parte dell'SVA e la semantica; Tabella 7 elenca le condizioni per ritentare la "
            "convalida (possibilita' di costruire una catena di certificati diversa, disponibilita' di una nuova "
            "copia del file di policy formale, disponibilita' del documento di policy, disponibilita' del "
            "certificato di firma, disponibilita' di certificati di CA, disponibilita' di POE aggiuntivi, "
            "disponibilita' di informazioni sulla revoca aggiornate)."
        ),
        "testo_integrale": (
            "An SVA shall provide a comprehensive report of the validation, allowing the DA to inspect details "
            "of the decisions made during validation and investigate the detailed causes for the status "
            "indication provided by the SVA.\n"
            "This clause specifies minimum requirements for the content of such a report.\n"
            "The DA shall, when a human user is involved, be able to present the report in a way meaningful to "
            "the user.\n"
            "In all cases, the signature validation process shall output:\n"
            "- a status indication of the results of the signature validation process. Table 5 lists the possible "
            "values of the main status indication and their semantics;\n"
            "- an indication of the policy or an indication of the set of constraints against which the signature "
            "has been validated;\n"
            "- the date and time for which the validation status was determined together with the validation data "
            "used for the determination; and\n"
            "NOTE 1: The date and time returned is the current time for Basic Signature validation; it can be "
            "either the current time or a point in time in the past when validating Signatures with Time, "
            "Signatures with Long-Term Validation Material or Signatures providing Long Term Availability and "
            "Integrity of Validation Material.\n"
            "- the validation process (clauses 5.3, 5.5 and 5.6.3) that has been used in validation.\n"
            "In addition, the signature validation process should output additional validation report data as "
            "specified in Table 5 and Table 6. For this purpose, the signature validation process may output:\n"
            "- a status subindication. Table 6 lists possible values and additional report data associated to "
            "these values;\n"
            "- additional data items extracted from the signature.\n"
            "Indications returned by SVAs shall conform to the following rules:\n"
            "- When the validation process selected as in clause 5.1.2 returns PASSED:\n"
            "- The overall result of the validation shall be TOTAL-PASSED.\n"
            "- The SVA should return the associated validation report data as specified in Table 5.\n"
            "- When the validation process selected as in clause 5.1.2 returns FAILED:\n"
            "- The overall result of the validation shall be TOTAL-FAILED.\n"
            "- The SVA shall return a sub-indication as specified in Table 6.\n"
            "- The SVA should return the associated validation report data as specified in Table 5 and Table 6.\n"
            "- When the validation process selected as in clause 5.1.2 returns INDETERMINATE:\n"
            "- The overall result of the validation shall be INDETERMINATE.\n"
            "- The SVA should return the associated validation report data as specified in Table 5.\n"
            "- When one or more of the sub-indications in Table 6 can be mapped to the reason(s) why the "
            "validation process returned INDETERMINATE:\n"
            "- The SVA shall return any of the corresponding sub-indications.\n"
            "- The SVA should return the associated validation report data as specified in Table 6.\n"
            "- Otherwise:\n"
            "- The SVA shall return a custom diagnostic of the reason for INDETERMINATE.\n"
            "NOTE 2: In the case of INDETERMINATE, there can be different reasons why the validation process "
            "returned INDETERMINATE. The final reason(s) in the result of the SVA can depend on the specific "
            "implementation.\n"
            "When the result is TOTAL-PASSED or TOTAL-FAILED:\n"
            "a) Any execution of an SVA with the same inputs shall return TOTAL-PASSED or TOTAL-FAILED, "
            "respectively.\n"
            "NOTE 3: Validation time, usually current-time, can be an input to the SVA. Execution of the SVA with "
            "different values for validation time will still return TOTAL-PASSED, as long as e.g. no certificate "
            "involved in the validation expires or becomes revoked and no cryptographic algorithm is broken. Then "
            "it can also return INDETERMINATE.\n"
            "b) Any execution of an SVA with the same inputs and additional validation data (e.g. more "
            "certificates or revocation status information) shall return the same result as it has returned in a) "
            "(i.e. TOTAL-PASSED or TOTAL-FAILED).\n"
            "c) Any execution of an SVA with the same inputs and additional POEs (e.g. timestamp) may return a "
            "different result from the original (i.e. TOTAL-PASSED or TOTAL-FAILED).\n"
            "When the result is INDETERMINATE:\n"
            "a) Any execution of an SVA with the same inputs shall return INDETERMINATE.\n"
            "b) Any execution of an SVA with the same inputs and additional validation data shall return "
            "TOTAL-PASSED, TOTAL-FAILED or INDETERMINATE.\n"
            "NOTE 4: The date/time at which the SVA is executed is an implicit input to the validation process. "
            "Running the SVA at a later point in time can give different results in case additional data becomes "
            "available (e.g. new certificate status information).\n"
            "NOTE 5: The term \"same inputs\" includes the signature validation policy or set of validation "
            "constraints to be used. Different validation constraints in general result in different validation "
            "results. Also, if the SVA fetches validation information from e.g. a CA, this is considered as input "
            "to the validation.\n"
            "Table 5: Status indications of the signature validation process\n"
            "Reported Validation Information | Semantics\n"
            "Status indication | Associated Validation report data\n"
            "TOTAL-PASSED | The validation process shall output the validated certificate chain, including the "
            "signing certificate, used in the validation process. - In addition, the validation process may "
            "provide the result of the validation for each of the validation constraints. - The validation "
            "process should provide the DA access to the signed attributes present in the signature, the identity "
            "of the signer. | The signature validation process results into TOTAL-PASSED based on the following "
            "considerations: - the format check succeeded; - the cryptographic checks of the signature succeeded "
            "(including checks of hashes of individual data objects that have been signed indirectly); - any "
            "constraints applicable to the signer's certificate have been positively validated (e.g. the signing "
            "certificate consequently has been found trustworthy); and - the signature has been positively "
            "validated against the validation constraints and hence is considered conformant to these "
            "constraints.\n"
            "TOTAL-FAILED | The validation process shall output additional information to explain the "
            "TOTAL-FAILED indication for each of the validation constraints that have been taken into account and "
            "for which a negative result occurred. | The signature validation process results into TOTAL-FAILED "
            "because the format-check failed, cryptographic checks of the signature failed (including checks of "
            "hashes of individual data objects that have been signed indirectly) or it has been proven that the "
            "signing certificate was invalid at the time of generation of the signature.\n"
            "INDETERMINATE | The validation process shall output additional information to explain the "
            "INDETERMINATE indication and to help the verifier to identify where relevant what data is missing "
            "to complete the validation process. In particular, it shall provide validation result indications "
            "for those validation constraints that have been taken into account and for which an indeterminate "
            "result occurred. | The available information is insufficient to ascertain the signature to be "
            "TOTAL-PASSED or TOTAL-FAILED.\n"
            "Table 6: Validation Report Structure and Semantics\n"
            "Reported Validation Information | Semantics\n"
            "Main indication | Sub-indication | Associated Validation report data\n"
            "TOTAL-FAILED | FORMAT_FAILURE | The validation process shall provide any information available why "
            "parsing of the signature failed. | The signature is not conformant to one of the base standards to "
            "the extent that the cryptographic verification building block is unable to process it.\n"
            "TOTAL-FAILED | HASH_FAILURE | The validation process shall provide: - An identifier (s) (e.g. an "
            "URI or OID) uniquely identifying the element within the Signed Data Object (such as the signature "
            "attributes, or the SD) that caused the failure. | The signature validation process results into "
            "TOTAL-FAILED because at least one hash of a Signed Data Object(s) that has been included in the "
            "signing process does not match the corresponding hash value in the signature.\n"
            "TOTAL-FAILED | SIG_CRYPTO_FAILURE | The validation process shall output: - The signing certificate "
            "used in the validation process. | The signature validation process results into TOTAL-FAILED because "
            "the signature value in the signature could not be verified using the signer's public key in the "
            "signing certificate.\n"
            "TOTAL-FAILED | REVOKED | The validation process shall provide the following: - The certificate "
            "chain used in the validation process. - The time and, if available, the reason of revocation of the "
            "signing certificate. | The signature validation process results into TOTAL-FAILED because: - the "
            "signing certificate has been revoked; and - there is proof that the signature has been created "
            "after the revocation time.\n"
            "TOTAL-FAILED | EXPIRED | The process shall output: The validated certificate chain. | The signature "
            "validation process results into TOTAL-FAILED because there is proof that the signature has been "
            "created after the expiration date (notAfter) of the signing certificate.\n"
            "TOTAL-FAILED | NOT_YET_VALID | - | The signature validation process results into TOTAL-FAILED "
            "because there is proof that the signature was created before the issuance date (notBefore) of the "
            "signing certificate.\n"
            "INDETERMINATE | SIG_CONSTRAINTS_FAILURE | The validation process shall provide: - The set of "
            "constraints that have not been met by the signature. | The signature validation process results "
            "into INDETERMINATE because one or more attributes of the signature do not match the validation "
            "constraints.\n"
            "INDETERMINATE | CHAIN_CONSTRAINTS_FAILURE | The validation process shall output: - The certificate "
            "chain used in the validation process. - The set of constraints that have not been met by the chain. "
            "| The signature validation process results into INDETERMINATE because the certificate chain used in "
            "the validation process does not match the validation constraints related to the certificate.\n"
            "INDETERMINATE | CERTIFICATE_CHAIN_GENERAL_FAILURE | The process shall output: - Additional "
            "information regarding the reason. | The signature validation process results into INDETERMINATE "
            "because the set of certificates available for chain validation produced an error for an unspecified "
            "reason.\n"
            "INDETERMINATE | CRYPTO_CONSTRAINTS_FAILURE | The process shall output: - Identification of the "
            "material (signature, certificate) that is produced using an algorithm or key size below the "
            "required cryptographic security level. - If known, the time up to which the algorithm or key size "
            "were considered secure. | The signature validation process results into INDETERMINATE because at "
            "least one of the algorithms that have been used in material (e.g. the signature value, a "
            "certificate...) involved in validating the signature, or the size of a key used with such an "
            "algorithm, is below the required cryptographic security level, and: - this material was produced "
            "after the time up to which this algorithm/key was considered secure (if such a time is known); and "
            "- the material is not protected by a sufficiently strong time-stamp applied before the time up to "
            "which the algorithm/key was considered secure (if such a time is known).\n"
            "INDETERMINATE | POLICY_PROCESSING_ERROR | The validation process shall provide additional "
            "information on the problem. | The signature validation process results into INDETERMINATE because a "
            "given formal policy file could not be processed for any reason (e.g. not accessible, not parseable, "
            "digest mismatch, etc.).\n"
            "INDETERMINATE | SIGNATURE_POLICY_NOT_AVAILABLE | - | The signature validation process results into "
            "INDETERMINATE because the electronic document containing the details of the policy is not "
            "available.\n"
            "INDETERMINATE | TIMESTAMP_ORDER_FAILURE | The validation process shall output the list of "
            "time-stamps that do no respect the ordering constraints. | The signature validation process results "
            "into INDETERMINATE because some constraints on the order of signature time-stamps and/or Signed "
            "Data Object(s) time-stamps are not respected.\n"
            "INDETERMINATE | NO_SIGNING_CERTIFICATE_FOUND | - | The signature validation process results into "
            "INDETERMINATE because the signing certificate cannot be identified.\n"
            "INDETERMINATE | NO_CERTIFICATE_CHAIN_FOUND | - | The signature validation process results into "
            "INDETERMINATE because no certificate chain has been found for the identified signing certificate.\n"
            "INDETERMINATE | NO_CERTIFICATE_CHAIN_FOUND_NO_POE |  | The signature validation process results "
            "into INDETERMINATE because no certificate chain has been found for the identified signing "
            "certificate due to the trust anchor not being trusted at the validation date/time by the validation "
            "policy in use. However the Signature Validation Algorithm cannot ascertain that the signing time "
            "lies before or after a time when the trust anchor was trusted by the validation policy in use.\n"
            "INDETERMINATE | REVOKED_NO_POE | The validation process shall provide the following: - The "
            "certificate chain used in the validation process. - The time and the reason of revocation of the "
            "signing certificate. | The signature validation process results into INDETERMINATE because the "
            "signing certificate was revoked at the validation date/time. However, the Signature Validation "
            "Algorithm cannot ascertain that the signing time lies before or after the revocation time.\n"
            "INDETERMINATE | REVOKED_CA_NO_POE | The validation process shall provide the following: - The "
            "certificate chain which includes the revoked CA certificate. - The time and the reason of "
            "revocation of the certificate. | The signature validation process results into INDETERMINATE "
            "because at least one certificate chain was found but an intermediate CA certificate is revoked.\n"
            "INDETERMINATE | OUT_OF_BOUNDS_NOT_REVOKED | - | The signature validation process results into "
            "INDETERMINATE because the signing certificate is expired or not yet valid at the validation "
            "date/time and the Signature Validation Algorithm cannot ascertain that the signing time lies "
            "within the validity interval of the signing certificate. The certificate is known not to be "
            "revoked.\n"
            "INDETERMINATE | OUT_OF_BOUNDS_NO_POE |  | The signature validation process results into "
            "INDETERMINATE because the signing certificate is expired or not yet valid at the validation "
            "date/time and the Signature Validation Algorithm cannot ascertain that the signing time lies "
            "within the validity interval of the signing certificate.\n"
            "INDETERMINATE | REVOCATION_OUT_OF_BOUNDS_NO_POE | The validation process shall provide the "
            "following: - The certificate chain used in the validation process. - The revocation data that is "
            "concerned by the failure. | The signature validation process results into INDETERMINATE because the "
            "signing certificate of the revocation data containing the revocation status information of the "
            "signature signing certificate is expired or not yet valid at the validation date/time and the "
            "Signature Validation Algorithm cannot ascertain that the revocation data is proven to have existed "
            "at a time that is within the validity interval of the signing certificate of that revocation "
            "data.\n"
            "INDETERMINATE | CRYPTO_CONSTRAINTS_FAILURE_NO_POE | The process shall output: - Identification of "
            "the material (signature, certificate) that is produced using an algorithm or key size below the "
            "required cryptographic security level. - If known, the time up to which the algorithm or key size "
            "were consider secure. | The signature validation process results into INDETERMINATE because at "
            "least one of the algorithms that have been used in objects (e.g. the signature value, a "
            "certificate, etc.) involved in validating the signature, or the size of a key used with such an "
            "algorithm, is below the required cryptographic security level, and there is no proof that this "
            "material was produced before the time up to which this algorithm/key was considered secure.\n"
            "INDETERMINATE | NO_POE | The validation process shall identify at least the signed objects for "
            "which the POEs are missing: - The validation process should provide additional information on the "
            "problem. | The signature validation process results into INDETERMINATE because a proof of existence "
            "is missing to ascertain that a signed object has been produced before some compromising event "
            "(e.g. broken algorithm).\n"
            "INDETERMINATE | TRY_LATER | The validation process shall output the point of time where the "
            "necessary revocation status information is expected to become available. | The signature validation "
            "process results into INDETERMINATE because not all constraints can be fulfilled using available "
            "information. However, it may be possible to do so using additional revocation status information "
            "that will be available at a later point of time.\n"
            "INDETERMINATE | SIGNED_DATA_NOT_FOUND | The process should output when available: - The "
            "identifier(s) (e.g. an URI) of the signed data that caused the failure. | The signature validation "
            "process results into INDETERMINATE because signed data cannot be obtained.\n"
            "INDETERMINATE | CUSTOM | The process shall output information allowing identification of the "
            "reason for the custom diagnostic result. | The signature validation process results into "
            "INDETERMINATE for a custom diagnostic not specified in the present document.\n"
            "Table 7 lists the sub-indications for the INDETERMINATE indication and corresponding conditions "
            "necessary to allow the validation results to be different when the DA reruns the validation "
            "process. For the listed sub-indications the DA may rerun the validation process.\n"
            "Table 7: Conditions for retrying validation\n"
            "Sub-indication | Conditions\n"
            "CHAIN_CONSTRAINTS_FAILURE, CERTIFICATE_CHAIN_GENERAL_FAILURE | It is possible to construct a "
            "different certificate chain. EXAMPLE: - Adding a cross-certificate which allows constructing a "
            "certificate chain to a different root.\n"
            "POLICY_PROCESSING_ERROR | A new copy of the required formal policy file is available that can now "
            "be accessed, parsed, etc.\n"
            "SIGNATURE_POLICY_NOT_AVAILABLE | The electronic document containing the details of the policy is "
            "available.\n"
            "NO_SIGNING_CERTIFICATE_FOUND | The signing certificate is available.\n"
            "NO_CERTIFICATE_CHAIN_FOUND | CA-certificates are available that can allow constructing a "
            "certificate chain.\n"
            "REVOKED_NO_POE, REVOKED_CA_NO_POE, OUT_OF_BOUNDS_NOT_REVOKED, OUT_OF_BOUNDS_NO_POE, "
            "CRYPTO_CONSTRAINTS_FAILURE_NO_POE, NO_POE | Additional POEs have been made available. This is only "
            "relevant for the validation process for Signatures providing Long Term Availability and Integrity "
            "of Validation Material.\n"
            "TRY_LATER | Revocation status information has been made available that may be fresh enough."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.1.4.1 (General requirements)",
        "testo": (
            "Il processo di convalida deve essere controllato da un insieme di vincoli di convalida, che possono "
            "essere definiti: con una specifica formale di policy, che dovrebbe essere quella di ETSI TS 119 172-1 "
            "[4] o un equivalente elaborabile dalla macchina; esplicitamente in dati di controllo specifici del "
            "sistema (es. file di configurazione tradizionali come file di proprieta' o .ini, o memorizzati in un "
            "registro o database); oppure implicitamente dall'implementazione stessa. I vincoli non impliciti "
            "nell'implementazione possono provenire dal contenuto della firma (direttamente, inclusi nella firma o "
            "negli attributi firmati, o indirettamente per riferimento a un documento esterno, in forma leggibile "
            "dall'uomo e/o elaborabile dalla macchina) oppure da una fonte locale del verificatore (es. file di "
            "configurazione, policy di convalida elaborabile dalla macchina) (NOTE 1: l'elaborazione di fonti "
            "aggiuntive di vincoli e' fuori dal perimetro del documento). Vincoli aggiuntivi possono essere "
            "forniti dalla DA all'SVA tramite parametri scelti dall'applicazione o dall'utente e influenzano il "
            "processo e il risultato a prescindere da dove siano stati definiti (NOTE 2: alcuni vincoli "
            "riguardano elementi del processo largamente implementati e gia' standardizzati altrove, es. IETF RFC "
            "5280 [1]; i dettagli di verifica non sono dati dal documento). Se l'algoritmo di convalida prescrive "
            "un controllo e l'insieme dei vincoli stabilisce che quel controllo non e' richiesto (es. verifica "
            "della revoca), l'SVA puo' saltare il passo e proseguire come se il controllo fosse riuscito, ma in "
            "tal caso deve restituire nel report finale alla DA l'elenco dei controlli disabilitati per effetto "
            "della policy. Il documento non prescrive sempre quando i vincoli vanno verificati (dipende "
            "dall'implementazione), ma l'SVA deve comunque verificare tutti i vincoli prescritti, e l'insieme dei "
            "vincoli usati non deve forzare l'SVA a non eseguire un controllo che, se eseguito, porterebbe a un "
            "risultato TOTAL-FAILED. Devono essere supportati: vincoli di validazione X.509 (clausola 5.1.4.2), "
            "vincoli crittografici (clausola 5.1.4.3) e vincoli sugli elementi della firma (clausola 5.1.4.4). "
            "Se sono implementati altri vincoli, il loro significato deve essere documentato esplicitamente per "
            "un'implementazione, direttamente o indirettamente per riferimento a uno standard o a una specifica "
            "pubblicamente disponibile (EXAMPLE: i vincoli possono imporre all'SVA di ignorare lo stato di revoca "
            "dei certificati intermedi, portandolo a restituire TOTAL-PASSED anche dove ci si attenderebbe "
            "INDETERMINATE; questo overruling della policy e' possibile per tutte le decisioni del documento)."
        ),
        "testo_integrale": (
            "The validation process shall be controlled by a set of validation constraints. These constraints "
            "may be defined:\n"
            "- using a formal policy specification which should be as specified in ETSI TS 119 172-1 [4] or "
            "machine processable equivalents;\n"
            "- explicitly in system specific control data: e.g. in conventional configuration-files like "
            "property or .ini-files or stored in a registry or database; or\n"
            "- implicitly by the implementation itself.\n"
            "Any validation constraints not implied by the implementation may originate from different sources:\n"
            "- the signature content itself, either directly (included in the signature or signed attributes) or "
            "indirectly, i.e. by reference to an external document, provided either in a human readable and/or "
            "machine processable form; or\n"
            "- a local source from the verifier (e.g. configuration file, (machine processable) signature "
            "validation policy).\n"
            "NOTE 1: The processing of additional sources for validation constraint (implicity by the "
            "implementation, local configuration) is out of the scope of the present document.\n"
            "Additional constraints may be provided by the DA to the SVA via parameters selected by the "
            "application or the user. These constraints influence the validation process and the validation "
            "result, irrespective of where these constraints have been defined.\n"
            "NOTE 2: Some of the constraints are related to elements of the signature validation process that "
            "are widely implemented in applications and already have been standardized elsewhere, e.g. in IETF "
            "RFC 5280 [1]. Details on how to check that the signature matches such constraints are not given in "
            "the present document.\n"
            "If the validation algorithm prescribes a certain check and the set of constraints state that such a "
            "check is not required (e.g. revocation checking), an SVA may skip that step and continue as if the "
            "check has succeeded. In such cases, the SVA shall return, in its final report to the DA, the list of "
            "checks that were disabled due to the policy.\n"
            "NOTE 3: The verifier can select a signature validation policy that contains additional constraints, "
            "which are not mentioned in the present document. It is not foreseeable, which constraints a DA will "
            "impose on the SVA. It is assumed that an implementation handles all constraints properly.\n"
            "EXAMPLE: Validation constraints can force the SVA to ignore revocation status of intermediate "
            "certificates. The SVA will then return TOTAL-PASSED, even if it would be expected to return "
            "INDETERMINATE. Such overruling by the policy is possible for all decisions made by the present "
            "document and cannot be mentioned in all places they can appear.\n"
            "The present document does not always prescribe exactly when constraints are to be checked, since "
            "this is implementation dependent. The SVA shall however check all constraints that are prescribed.\n"
            "The set of validation constraints used for validation shall not force the SVA not to check a "
            "constraint that, when checked, would, according to the present document, lead to a TOTAL-FAILED "
            "result.\n"
            "The following constraints shall be supported:\n"
            "- X.509 validation constraints, as defined in clause 5.1.4.2;\n"
            "- cryptographic constraints as defined in clause 5.1.4.3;\n"
            "- signature elements constraints as defined in clause 5.1.4.4.\n"
            "Where other constraints are implemented, their meaning shall be explicitly documented for an "
            "implementation either directly or indirectly by reference to a standard or publicly available "
            "specification."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.1.4.2 (X.509 Validation Constraints)",
        "testo": (
            "I vincoli di validazione X.509 devono indicare requisiti per la verifica della revoca e per l'uso "
            "nel processo di convalida del percorso di certificazione (certificate path validation), come "
            "specificato in ETSI TS 119 172-1 [4], clausola A.4.2.1, Tabella A.2 riga m."
        ),
        "testo_integrale": (
            "X.509 validation constraints shall indicate requirements for revocation checking and for use in the "
            "certificate path validation process as specified in ETSI TS 119 172-1 [4], clause A.4.2.1, Table "
            "A.2 row m."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.1.4.3 (Cryptographic Constraints)",
        "testo": (
            "I vincoli crittografici devono indicare requisiti su algoritmi e parametri usati nella creazione "
            "delle firme o nella convalida di oggetti firmati, come specificato in ETSI TS 119 172-1 [4], "
            "clausola A.4.2.1, Tabella A.2 riga p."
        ),
        "testo_integrale": (
            "Cryptographic constraints shall indicate requirements on algorithms and parameters used when "
            "creating signatures or used when validating signed objects as specified in ETSI TS 119 172-1 [4], "
            "clause A.4.2.1, Table A.2 row p."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.1.4.4 (Signature Elements Constraints)",
        "testo": (
            "I vincoli sugli elementi della firma devono indicare i requisiti aggiuntivi rispetto ai vincoli "
            "X.509 e crittografici di cui sopra, come specificato in ETSI TS 119 172-1 [4], clausola A.4.2.1, "
            "Tabella A.2."
        ),
        "testo_integrale": (
            "Signature elements constraints shall indicate any requirements additional to X.509 and "
            "cryptographic constraints defined above as specified in ETSI TS 119 172-1 [4], clause A.4.2.1, "
            "Table A.2."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = []

INDICE_ARTICOLI_LOCALE = [
    "clausola 5.1.1 (General requirements)",
    "clausola 5.1.2 (Selecting validation processes)",
    (
        "clausola 5.1.3 (Status indication of the signature validation process and signature validation report)"
    ),
    "clausola 5.1.4.1 (General requirements)",
    "clausola 5.1.4.2 (X.509 Validation Constraints)",
    "clausola 5.1.4.3 (Cryptographic Constraints)",
    "clausola 5.1.4.4 (Signature Elements Constraints)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
