"""ETSI EN 319 102-1 V1.4.1 (2024-06) - Electronic Signatures and Trust
Infrastructures (ESI); Procedures for Creation and Validation of AdES Digital
Signatures; Part 1: Creation and Validation. Fonte la cui numerazione degli id
e' risolta per riferimento dalla sessione principale in app/seed.py - questo
modulo NON tocca seed.py. Capitolo 7 del manifest di split
(app/.source_cache/etsi_319_102/manifest.json): clausola 5.6 "Validation
process for Signatures providing Long Term Availability and Integrity of
Validation Material", limitatamente alle sottoclausole 5.6.1, 5.6.2.1.1-5.6.2.4.4
e 5.6.3.1-5.6.3.4. Testo ufficiale in app/.source_cache/etsi_319_102/cap07.txt.
La porzione si esaurisce con la clausola 5.6.3.4: non contiene la clausola 2
(References, paratesto, fuori dal censimento) ne' la sezione finale "History".

Copertura (ADR-0007): 21 item di indice e 21 nodi, uno per clausola numerata
con contenuto proprio - 5.6.1 (Introduction); cinque "Description"
(5.6.2.1.1, 5.6.2.2.1, 5.6.2.3.1, 5.6.2.4.1, 5.6.3.1); cinque "Input"
(5.6.2.1.2, 5.6.2.2.2, 5.6.2.3.2, 5.6.2.4.2, 5.6.3.2); cinque "Output"
(5.6.2.1.3, 5.6.2.2.3, 5.6.2.3.3, 5.6.2.4.3, 5.6.3.3); cinque "Processing"
(5.6.2.1.4, 5.6.2.2.4, 5.6.2.3.4, 5.6.2.4.4, 5.6.3.4). Di questi 21 nodi 8
sono Obblighi (le cinque clausole "Processing" e le tre clausole "Output" che
contengono un verbo prescrittivo) e 13 Principi (introduzione, descrizioni,
tabelle di input e le due tabelle di output puramente dichiarative). Nessuna
clausola coperta due volte, nessuna omessa: tutte le parole del file (piedini di
pagina esclusi) risultano distribuite fra i 21 nodi, le 28 intestazioni
numerate e le 2 righe di continuazione dei titoli lunghi.

Scelte di modellazione non ovvie:

- Intestazioni di puro raggruppamento -> NESSUN nodo e NESSUN item di indice:
  5.6, 5.6.2, 5.6.2.1, 5.6.2.2, 5.6.2.3, 5.6.2.4 e 5.6.3 contengono solo il
  titolo e il rinvio alle sottoclausole di livello inferiore, quindi non hanno
  contenuto proprio. Stesso trattamento gia' riservato ai titoli di livello
  intermedio degli altri standard ETSI censiti (es. clausola 7.2 di ETSI TS
  119 432).
- Clausole "Processing" (5.6.2.1.4, 5.6.2.2.4, 5.6.2.3.4, 5.6.2.4.4, 5.6.3.4)
  -> UN SOLO Obbligo ciascuna, non un nodo per passo numerato: i passi 1), 2),
  a), i. non sono clausole autonome ma l'articolazione interna di una stessa
  procedura, e l'unità di copertura e' la clausola numerata. Il testo_integrale
  riporta l'algoritmo completo passo per passo, comprese le NOTE e gli EXAMPLE
  ufficiali (ADR-0010).
- `tipo_obbligo`: "tecnico/sicurezza" per i sei nodi dei blocchi costitutivi
  aggiuntivi della clausola 5.6.2 (5.6.2.1.4, 5.6.2.2.4, 5.6.2.3.3, 5.6.2.3.4,
  5.6.2.4.3, 5.6.2.4.4: percorso di certificazione X.509, dati di revoca,
  vincoli crittografici e affidabilità degli algoritmi, POE e funzioni di hash),
  come per le clausole "Processing"/"Outputs" dei blocchi costitutivi di base
  della clausola 5.2 (app/seed_data/etsi_319_102/cap04.py); "procedurale" per i
  due nodi del processo di convalida a lungo termine 5.6.3 (5.6.3.3, 5.6.3.4),
  come per le clausole "Processing" dei processi di convalida 5.3-5.5
  (cap05.py e cap06.py della stessa Fonte).
- Clausole "Output" -> il tipo dipende dalla presenza di un verbo prescrittivo:
  5.6.2.3.3, 5.6.2.4.3 e 5.6.3.3 contengono "shall return"/"shall be" con
  destinatario individuabile (il processo o la SVA) e sono Obblighi; 5.6.2.1.3
  e 5.6.2.2.3 sono solo tabelle di indicazioni possibili, senza prescrizione, e
  sono Principi "altro". Nella clausola 5.2 (cap04.py) la stessa distinzione
  separa le clausole "Outputs" prescrittive (Obbligo) da quelle dichiarative;
  nelle clausole 5.3.3, 5.4.3 e 5.5.3 (cap05.py, cap06.py) la "Outputs" e' un
  Principio perché il verbo modale manca, come qui in 5.6.2.1.3 e 5.6.2.2.3.
- Clausole "Input" (5.6.2.1.2, 5.6.2.2.2, 5.6.2.3.2, 5.6.2.4.2, 5.6.3.2) ->
  Principi "altro": le tabelle 21, 23, 25, 26 e 27 dichiarano la firma
  dell'interfaccia del blocco costitutivo (input obbligatori o opzionali) senza
  imporre un comportamento a un soggetto, quindi non contengono alcun verbo
  modale. Stessa lettura delle clausole "Inputs" della clausola 5.2 (cap04.py);
  cap06.py ha invece censito come Obbligo la 5.5.2 (Inputs) del processo di
  convalida con tempo: la divergenza e' fra capitoli della stessa Fonte, non
  dentro questa porzione, dove tutte le tabelle prive di verbo modale sono
  Principi.
- Clausole "Description" (5.6.2.1.1, 5.6.2.2.1, 5.6.2.3.1, 5.6.2.4.1, 5.6.3.1)
  e "Introduction" (5.6.1) -> Principi "altro": espongono modello, razionale e
  presupposti dei processi, incluse NOTE ed EXAMPLE ufficiali. Per la 5.6.1 non
  si e' usato "scopo/ambito di applicazione": la clausola descrive il processo,
  non il perimetro applicativo del documento.
- `soggetti`: obbligato sempre "QTSP/gestore" (il soggetto che implementa o
  gestisce la SVA, l'applicazione di convalida che esegue i processi), stessa
  scelta gia' adottata per i controlli di convalida di ETSI TS 119 101 (cap03,
  clausola 8). Nessun destinatario esplicito: queste clausole disciplinano il
  processo di convalida, non l'informazione verso un terzo.
- `condizione_applicabilita` mai valorizzato: le condizioni ufficiali ("If the
  current status is PASSED", "when the validation policy requires to use the
  shell model") restano dove il testo le pone, cioe' dentro la prescrizione
  stessa. `severita`/`sanzioni` omessi: uno standard tecnico ETSI non commina
  sanzioni.
- Tabelle -> ricostruite nel testo_integrale riga per riga (una riga per
  record, formato markdown a barre verticali) senza perdere alcun valore:
  tabelle 21-27, tutte appartenenti alla clausola che le contiene.
- Normalizzazione meccanica del verbatim, senza tagliare una sola parola:
  rimossi i piedini di pagina della conversione PDF ("ETSI" centrato, numero di
  pagina e running head "ETSI EN 319 102-1 V1.4.1 (2024-06)"); le interruzioni
  fisiche di riga ricomposte con spazio singolo; il simbolo di elenco
  tipografico del PDF (carattere private-use U+F0A7) reso come "•"; i wrap
  fisici dentro una cella di tabella ricomposti in un'unica cella.
- RELAZIONI vuota per mandato del task di capitolo: i rinvii interni (clausole
  5.1.3, 5.2, 5.2.5, 5.2.6, 5.2.8, 5.4, 5.5, 5.6.2.x) e quelli esterni (IETF
  RFC 4998, IETF RFC 6283, IETF RFC 5280, CMS, PAdES, TSL) non diventano archi
  in questo modulo; il cross-collegamento e' demandato alla sessione principale
  (ADR-0009, Fase 6).
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 5.6.2.1.4 (Processing)",
        "testo": (
            "Convalida passata del certificato: il blocco costitutivo DEVE eseguire i cinque passi seguenti. 1) "
            "Costruire una nuova catena di certificati prospettica non ancora valutata: se nessuna nuova catena "
            "puo' essere costruita, restituire lo stato corrente e l'ultima catena costruita o, se nessuna catena "
            "e' stata costruita, l'indicazione INDETERMINATE con sotto-indicazione NO_CERTIFICATE_CHAIN_FOUND; "
            "altrimenti passare al passo successivo. 2) Eseguire la Certification Path Validation di IETF RFC "
            "5280, clausola 6.1, con la catena prospettica costruita al passo precedente, la trust anchor usata, "
            "i vincoli di convalida X.509 forniti in input e una data presa dall'intersezione degli intervalli di "
            "validita' di tutti i certificati della catena prospettica (quando la politica di convalida richiede "
            "il modello a guscio) oppure dalla validita' del certificato del firmatario (modello a catena); la "
            "convalida NON deve includere il controllo di revoca ne' la verifica che il tempo corrente preceda "
            "una sunset date della trust anchor definita dai vincoli di convalida X.509. Se la path validation "
            "restituisce PASSED si passa al passo successivo; se restituisce un'indicazione di fallimento lo "
            "stato corrente e' posto a INDETERMINATE/CERTIFICATE_CHAIN_GENERAL_FAILURE e si torna al passo 1). 3) "
            "Eseguire il processo di scorrimento del tempo di convalida (clausola 5.6.2.2) con la catena "
            "prospettica, l'insieme di POE, l'insieme dei dati di convalida dei certificati, la sunset date della "
            "trust anchor da cui la catena corrente e' stata costruita (quando i vincoli di convalida X.509 la "
            "specificano) e i vincoli crittografici: su indicazione di successo si passa al passo successivo, "
            "altrimenti si pone lo stato corrente all'indicazione e sotto-indicazione restituite e si torna al "
            "passo 1). 4) Applicare i vincoli di convalida X.509 alla catena: se la catena non li soddisfa, porre "
            "lo stato corrente a INDETERMINATE/CHAIN_CONSTRAINTS_FAILURE e tornare al passo 1). 5) Restituire lo "
            "stato corrente: se e' PASSED, restituire anche la catena di certificati e il tempo di convalida "
            "calcolato al passo 3)."
        ),
        "testo_integrale": (
            "1) The building block shall build a new prospective certificate chain that has not yet been "
            "evaluated:\n\n"
            "a) If no new chain can be built, the building block shall return the current status and the last "
            "chain built or, if no chain was built, the indication INDETERMINATE with the sub-indication "
            "NO_CERTIFICATE_CHAIN_FOUND.\n\n"
            "b) Otherwise, the building block shall go to the next step.\n\n"
            "2) The building block shall run the Certification Path Validation of IETF RFC 5280 [1], clause 6.1, "
            "with the following inputs: the prospective certificate chain built in the previous step, the trust "
            "anchor used in the previous step, the X.509 validation constraints provided in the inputs and "
            "either:\n\n"
            "i) when the validation policy requires to use the shell model, a date from the intersection of the "
            "validity intervals of all the certificates in the prospective certificate chain; or\n\n"
            "ii) when the validation policy requires to use the chain model, a date from the validity of the "
            "signer's certificate.\n\n"
            "The validation shall not include revocation checking nor verifying that current time is before a "
            "trust anchor sunset date when the X.509 validation constraints define such a sunset date:\n\n"
            "a) If the certificate path validation returns PASSED, the building block shall go to the next step.\n\n"
            "b) If the certificate path validation returns a failure indication, the building block shall set the "
            "current status to INDETERMINATE/CERTIFICATE_CHAIN_GENERAL_FAILURE and shall go to step 1).\n\n"
            "3) The building block shall perform the validation time sliding process as per clause 5.6.2.2 with "
            "the following inputs: the prospective chain, the set of POEs, the set of certificate validation "
            "data, the sunset date of the trust anchor from which the current chain has been built when the X.509 "
            "validation constraint specify such a date, and the cryptographic constraints. If it outputs a "
            "success indication, the building block shall go to the next step. Otherwise, the building block "
            "shall set the current status to the returned indication and sub-indication and shall go back to step "
            "1).\n\n"
            "4) The building block shall apply the X.509 validation constraints to the chain. If the chain does "
            "not match these constraints, the building block shall set the current status to "
            "INDETERMINATE/CHAIN_CONSTRAINTS_FAILURE and shall go to step 1).\n\n"
            "5) The building block shall return the current status. If the current status is PASSED, the building "
            "block shall also return the certificate chain as well as the calculated validation time returned in "
            "step 3)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.6.2.2.4 (Processing)",
        "testo": (
            "Scorrimento del tempo di convalida. 1) Inizializzare control-time a: a) la sunset date della trust "
            "anchor, quando questo input e' fornito ed e' anteriore alla data/ora corrente; oppure b) la data/ora "
            "corrente in ogni altro caso. Control-time e' una variabile interna usata dagli algoritmi e non fa "
            "parte dei risultati principali del processo di convalida (NOTA 1); inizializzarla con la data/ora "
            "corrente presuppone che la trust anchor sia ancora fidata al momento corrente, mentre inizializzarla "
            "a una data nota consente di catturare il caso, molto esotico, in cui la trust anchor sia compromessa "
            "(o non piu' fidata per altra ragione) a una data conosciuta (NOTA 2). 2) Per ogni certificato della "
            "catena, partendo dal primo certificato (quello emesso dalla trust anchor): a) selezionare dai dati "
            "di convalida forniti i dati di revoca che soddisfano tre condizioni - il dato di revoca e' coerente "
            "con le regole che ne condizionano l'uso per controllare lo stato di revoca del certificato "
            "considerato (nel caso di una CRL, i controlli di IETF RFC 5280, clausola 6.3.3 (b) a (l), con "
            "l'eccezione della verifica che control-time cada nel periodo di validita' del certificato "
            "dell'emittente della CRL); la data di emissione dell'informazione sullo stato di revoca contenuta "
            "nel dato di revoca e' anteriore a control-time; l'insieme di POE contiene una prova di esistenza del "
            "certificato e del dato di revoca contenente l'informazione sullo stato di revoca ad (o prima di) "
            "control-time - e, se almeno un dato di revoca e' selezionato, passare al passo successivo, "
            "altrimenti restituire l'indicazione INDETERMINATE con sotto-indicazione NO_POE; b) se il certificato "
            "risulta revocato in uno qualunque dei dati di revoca trovati al passo precedente, selezionare il "
            "dato di revoca emesso piu' di recente; porre control time al tempo di revoca quando la politica di "
            "convalida richiede il modello a guscio oppure, quando richiede il modello a catena, se la ragione di "
            "revoca e' compromissione della chiave o sconosciuta; quindi passare al passo d); c) se il "
            "certificato non risulta revocato in tutti i dati di revoca trovati al passo a), selezionare il dato "
            "di revoca emesso piu' di recente ed eseguire il Revocation Freshness Checker su quel dato di revoca, "
            "sul certificato di cui si controlla lo stato di revoca e su control time: se restituisce FAILED, "
            "porre control time al piu' antico fra il valore corrente di control time (tempo A) e il tempo di "
            "emissione dell'informazione sullo stato di revoca contenuta nel dato di revoca (tempo B); altrimenti "
            "non modificare il valore di control time; d) applicare i vincoli crittografici al certificato e al "
            "dato di revoca rispetto a control-time: se il certificato (o il dato di revoca) non soddisfa tali "
            "vincoli, porre control-time all'ultimo istante fino al quale gli algoritmi elencati erano tutti "
            "considerati affidabili; e) proseguire con il certificato successivo della catena o, se non esiste un "
            "ulteriore certificato, restituire l'indicazione PASSED con il control-time calcolato. Il razionale "
            "del passo 2)a) e' verificare che il dato di revoca sia 'in scope' per il certificato dato, cioe' che "
            "sia affidabile per accertare lo stato di revoca di quel certificato: per esempio il certificato non "
            "deve essere scaduto alla data di emissione del dato di revoca, salvo che la CA emittente dichiari di "
            "fornire informazioni di revoca per certificati scaduti (per esempio con l'estensione CRL "
            "expiredCertOnCRL) (NOTA 3). Se il certificato (o il dato di revoca) era autentico ma la firma e' "
            "stata falsificata sfruttando debolezze degli algoritmi usati, si assume che cio' sia possibile solo "
            "dopo la data in cui gli algoritmi sono dichiarati non piu' accettabili: il titolare della coppia di "
            "chiavi originale si presume quindi essere stato in controllo della propria chiave fino a quella "
            "data; e' il razionale dello scorrimento di control-time nei passi 2)b) e 2)c) (NOTA 4). L'algoritmo "
            "assume implicitamente che il dato di revoca sia firmato dall'emittente del certificato "
            "(l'impostazione di revoca piu' tradizionale, non l'unica): lo stesso algoritmo puo' essere adattato "
            "ai casi in cui il dato di revoca abbia una propria catena di certificati, applicando il processo di "
            "scorrimento di control-time a quella catena, che restituirebbe un control-time da confrontare con il "
            "control-time associato al certificato (NOTA 5). Quando tutti i certificati della catena sono "
            "convalidabili al momento corrente, control-time non scorre mai e viene restituito il tempo corrente "
            "(NOTA 6)."
        ),
        "testo_integrale": (
            "1) The building block shall initialize control-time to either:\n\n"
            "a) the trust anchor sunset date when this input is provided, and this date is before current "
            "date/time; or\n\n"
            "b) the current date/time in all other cases.\n\n"
            "NOTE 1: Control-time is an internal variable that is used within the algorithms and not part of the "
            "core results of the validation process.\n\n"
            "NOTE 2: Initializing control time with current date/time assumes that the trust anchor is still "
            "trusted at the current date/time. The algorithm can capture the very exotic case where the trust "
            "anchor is broken (or becomes untrusted for any other reason) at a known date by initializing control "
            "time to this date/time.\n\n"
            "2) For each certificate in the chain starting from the first certificate (the certificate issued by "
            "the trust anchor):\n\n"
            "a) The building block shall select revocation data from the provided certificate validation data, "
            "satisfying the following:\n\n"
            "• the revocation data is consistent with the rules conditioning its use to check the revocation "
            "status of the considered certificate. In the case of a CRL, it shall satisfy the checks specified in "
            "IETF RFC 5280 [1], clause 6.3.3 (b) to (l); with the exception of the verification of whether the "
            "control-time is within the validity period of the certificate of the issuer of the CRL; and\n\n"
            "• the issuance date of the revocation status information contained within the revocation data is "
            "before control-time; and\n\n"
            "• the set of POEs contains a proof of existence of the certificate and the revocation data "
            "containing revocation status information at (or before) control-time.\n\n"
            "If at least one revocation data is selected, the building block shall go to the next step. If there "
            "is no such information, the building block shall return the indication INDETERMINATE with the "
            "sub-indication NO_POE.\n\n"
            "b) If the certificate is marked as revoked in any of the revocation data found in the previous step, "
            "the building block shall perform the following steps:\n\n"
            "• select the revocation data that has been issued the latest;\n\n"
            "• set control time to the revocation time whenever the validation policy requires to use the shell "
            "model; or, when the validation policy requires to use the chain model and the revocation reason is "
            "key compromise or unknown;\n\n"
            "• go to step d).\n\n"
            "c) If the certificate is not marked as revoked in all of the revocation data found in step a), the "
            "building block shall select the revocation data that has been issued the latest, run the Revocation "
            "Freshness Checker with that revocation data, the certificate for which the revocation status is "
            "being checked and the control time. If it returns FAILED, the building block shall set control time "
            "to the time that is the earliest between time A and time B, where time A is the current value of "
            "control time and time B is the issuance time of the revocation status information contained within "
            "the revocation data. Otherwise, the building block shall not change the value of control time.\n\n"
            "d) The building block shall apply the cryptographic constraints to the certificate and the "
            "revocation data against the control-time. If the certificate (or the revocation data) does not match "
            "these constraints, the building block shall set control-time to the latest time up to which the "
            "listed algorithms were all considered reliable.\n\n"
            "e) The building block shall continue with the next certificate in the chain or, if no further "
            "certificate exists, the building block shall return the status indication PASSED and the calculated "
            "control-time.\n\n"
            "NOTE 3: The rationale of step 2)a) is to check that the revocation data is \"in scope\" for the given "
            "certificate. In other words, the rationale is to check that the revocation data is reliable to be "
            "used to ascertain the revocation status of the given certificate. For instance, this includes the "
            "fact the certificate is not expired at the issuance date of the revocation data, unless the issuing "
            "CA states that it provides revocation status information for expired certificates (for instance, "
            "using the CRL extension expiredCertOnCRL).\n\n"
            "NOTE 4: If the certificate (or the revocation data) was authentic, but the signature has been faked "
            "exploiting weaknesses of the algorithms used, this is assumed only to be possible after the date the "
            "algorithms are declared to be no longer acceptable. Therefore, the owner of the original key pair is "
            "assumed to having been under control of his key up to that date. This is the rationale of sliding "
            "control-time in steps 2)b) and 2)c).\n\n"
            "NOTE 5: For more readability, the algorithm above implicitly assumes that the revocation data is "
            "signed by the certificate's issuer, which is the most traditional revocation setting but not the "
            "only one. The same algorithm can be adapted to the cases where the revocation data has its own "
            "certificate chain by applying the control-time sliding process to this chain, which would output a "
            "control-time to be compared to the control-time associated to the certificate.\n\n"
            "NOTE 6: When all the certificates in the chain can be validated at the current time, the "
            "control-time never slides and the current time is returned."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.6.2.3.3 (Output)",
        "testo": (
            "Il processo di estrazione delle POE DEVE restituire un insieme di POE, che puo' essere un insieme "
            "vuoto."
        ),
        "testo_integrale": (
            "The POE extraction process shall return a set of POEs that may be an empty set."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.6.2.3.4 (Processing)",
        "testo": (
            "Estrazione delle POE, sei passi. 1) Determinare l'insieme S dei riferimenti a oggetti e degli "
            "oggetti che fanno parte della firma e sono protetti dalla marca temporale. 2) Se un oggetto "
            "dell'insieme S contiene altri oggetti non ancora contenuti in S e utilizzabili nella convalida della "
            "firma, aggiungerli a S (esempio: una PAdES Document Security Store o dati firmati come un elemento "
            "PAdES Signed Data). 3) Inizializzare l'insieme P delle POE a insieme vuoto. 4) Per ciascun "
            "riferimento a oggetti contenuto nell'insieme S, dove il riferimento contiene un valore di hash "
            "dell'oggetto referenziato O e la funzione di hash crittografica h e' asserita nei vincoli "
            "crittografici come fidata almeno fino a una data successiva al tempo di generazione della marca "
            "temporale (T1): a) aggiungere a P una POE per il valore di hash h(O) dell'oggetto O a T1; b) se "
            "l'insieme delle POE include una POE per un oggetto O a una data/ora T2 successiva a T1 e h e' "
            "asserita nei vincoli crittografici come fidata almeno fino a T2, aggiungere a P una POE per O a T1. "
            "5) Per ciascun oggetto contenuto in S, aggiungere a P una POE per quell'oggetto a T1. 6) Restituire "
            "l'insieme P delle POE."
        ),
        "testo_integrale": (
            "1) The building block shall determine the set S of references to objects and objects that are part "
            "of the signature and are protected by the time-stamp.\n\n"
            "2) If any of the objects in the set S contains other objects that are not yet contained in the set S "
            "and that can be used in signature validation, the building block shall add them to the set S.\n\n"
            "EXAMPLE: Such objects can be a PAdES Document Security Store or signed data like a PAdES Signed Data "
            "element.\n\n"
            "3) The building block shall initialize the set P of POE with an empty set.\n\n"
            "4) For each reference to objects contained in the set S where the reference contains a hash value of "
            "the referenced object O and the cryptographic hash function h is asserted in the cryptographic "
            "constraints to be trusted until at least a date after the time of the generation of the timestamp "
            "(named T1):\n\n"
            "a) The building block shall add to P a POE for the hash value h(O) of the object O at T1.\n\n"
            "b) If the set of POEs includes a POE for an object O at a date/time T2 after T1 and the "
            "cryptographic hash function h is asserted in the cryptographic constraints to be trusted until at "
            "least T2, the building block shall add to P a POE for O at T1.\n\n"
            "5) For each object contained in S, the building block shall add to P a POE for that object at T1.\n\n"
            "6) The building block shall return the set P of POEs."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.6.2.4.3 (Output)",
        "testo": (
            "Il processo DEVE restituire un'indicazione/sotto-indicazione, che e' o la stessa "
            "indicazione/sotto-indicazione del momento corrente fornita in input, oppure una tra PASSED e "
            "FAILED/NOT_YET_VALID."
        ),
        "testo_integrale": (
            "This process shall output an indication/sub-indication, which is either the same as the current time "
            "indication/sub-indication given in the inputs or one of the following: PASSED or "
            "FAILED/NOT_YET_VALID."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.6.2.4.4 (Processing)",
        "testo": (
            "Convalida passata della firma. 1) Verificare che esista almeno un dato di revoca noto per contenere "
            "informazioni sullo stato di revoca del certificato di firma per cui l'insieme di POE contiene una "
            "POE del certificato dell'emittente del certificato di firma successiva alla data di emissione e "
            "anteriore alla data di scadenza di tale certificato dell'emittente: a) se tale dato di revoca "
            "esiste, rimuovere dai dati di convalida dei certificati tutti i dati di revoca noti per contenere "
            "informazioni sullo stato di revoca del certificato di firma per cui non esiste tale POE e porre "
            "sig_cert_revocation_poe-status a PASSED; b) altrimenti porre sig_cert_revocation_poe-status a "
            "INDETERMINATE con sotto-indicazione REVOCATION_OUT_OF_BOUNDS_NO_POE. sig_cert_revocation_poe-status "
            "e' una variabile interna: restituire REVOCATION_OUT_OF_BOUNDS_NO_POE a questo passo in caso di "
            "fallimento perderebbe l'informazione fornita dall'indicazione/sotto-indicazione del momento corrente "
            "(NOTA). 2) Eseguire il processo di convalida passata del certificato specificato nella clausola "
            "5.6.2.1 con i seguenti input: firma, certificato obiettivo, parametri di convalida X.509, dati di "
            "convalida dei certificati, vincoli di convalida X.509, vincoli crittografici e insieme di POE. Se "
            "restituisce PASSED con tempo di convalida, passare al passo successivo; altrimenti restituire lo "
            "stato e la sotto-indicazione del momento corrente con una spiegazione del fallimento. 3) Se esiste "
            "una POE del valore di firma ad (o prima di) il tempo di convalida restituito al passo precedente: "
            "quando l'indicazione/sotto-indicazione del momento corrente e' "
            "INDETERMINATE/NO_CERTIFICATE_CHAIN_FOUND_NO_POE, se best-signature-time e' anteriore alla data di "
            "emissione del certificato di firma (campo notBefore) il blocco costitutivo DEVE restituire FAILED "
            "con sotto-indicazione NOT_YET_VALID, se e' successivo alla data di scadenza del certificato di firma "
            "DEVE restituire INDETERMINATE con sotto-indicazione OUT_OF_BOUNDS_NO_POE, altrimenti va al passo 7); "
            "quando e' INDETERMINATE/REVOKED_NO_POE, INDETERMINATE/REVOCATION_OUT_OF_BOUNDS_NO_POE o "
            "INDETERMINATE/TRY_LATER perche' il certificato e' stato trovato sospeso, se best-signature-time e' "
            "anteriore alla data di emissione del certificato di firma il processo restituisce FAILED con "
            "sotto-indicazione NOT_YET_VALID, se cade nel periodo di validita' del certificato di firma si va al "
            "passo 7), altrimenti si pone l'indicazione/sotto-indicazione del momento corrente a "
            "INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED e si prosegue; quando e' INDETERMINATE/REVOKED_CA_NO_POE, se "
            "esiste una POE del dato di revoca contenente l'informazione sullo stato di revoca del certificato "
            "del firmatario ad (o prima di) il tempo di revoca del certificato della CA, e il best signature time "
            "(il tempo piu' basso in cui esiste una POE per il valore di firma nell'insieme di POE) cade nel "
            "periodo di validita' del certificato di firma, si va al passo 7), altrimenti si pone "
            "l'indicazione/sotto-indicazione del momento corrente a OUT_OF_BOUNDS_NOT_REVOKED e si prosegue; se "
            "invece tale POE non esiste, si restituisce l'indicazione INDETERMINATE con sotto-indicazione "
            "REVOKED_CA_NO_POE; quando e' INDETERMINATE/OUT_OF_BOUNDS_NO_POE oppure OUT_OF_BOUNDS_NOT_REVOKED, se "
            "best-signature-time (il tempo piu' basso in cui esiste una POE per il valore di firma nell'insieme "
            "di POE) e' anteriore alla data di emissione del certificato di firma (campo notBefore) si "
            "restituisce FAILED con sotto-indicazione NOT_YET_VALID, se e' successivo alla data di emissione e "
            "anteriore alla data di scadenza del certificato di firma si va al passo 7). 4) Se "
            "l'indicazione/sotto-indicazione del momento corrente e' "
            "INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE e per ogni algoritmo (o dimensione di chiave) nella "
            "lista interessata dal fallimento esiste una POE del materiale che usa quell'algoritmo (o dimensione "
            "di chiave) a un tempo anteriore al tempo fino al quale l'algoritmo in questione era considerato "
            "sicuro, andare al passo 7). 5) Se l'indicazione/sotto-indicazione del momento corrente e' "
            "INDETERMINATE/TRY_LATER perche' le informazioni di revoca del certificato obiettivo non erano "
            "sufficientemente fresche: a) determinare dall'insieme di POE il tempo piu' antico in cui l'esistenza "
            "della firma puo' essere provata; b) eseguire il Revocation Freshness Checker (clausola 5.2.5) con le "
            "corrispondenti informazioni sullo stato di revoca, il certificato obiettivo e il tempo determinato "
            "al passo a); c) se il checker restituisce PASSED andare al passo 7), altrimenti restituire "
            "l'indicazione INDETERMINATE, la sotto-indicazione TRY_LATER e, se restituito dal Revocation "
            "Freshness Checker, il suggerimento su quando ritentare la convalida. 6) In tutti gli altri casi "
            "restituire l'indicazione/sotto-indicazione del momento corrente insieme a una spiegazione del "
            "fallimento. 7) Restituire l'indicazione e la sotto-indicazione contenute in "
            "sig_cert_revocation_poe-status."
        ),
        "testo_integrale": (
            "1) The building block shall verify that there is at least one revocation data instance that is known "
            "to contain revocation status information about the signing certificate for which the set of POEs "
            "contains a POE for the signing certificate issuer's certificate after the issuance date and before "
            "the expiration date of the signing certificate issuer's certificate:\n\n"
            "a) If there is such a revocation data, the building block shall remove from the Certificate "
            "Validation Data all revocation data known to contain revocation status information about the signing "
            "certificate for which there is no such POE and set sig_cert_revocation_poe-status to PASSED.\n\n"
            "b) Otherwise the building block shall set sig_cert_revocation_poe-status to INDETERMINATE with the "
            "sub-indication REVOCATION_OUT_OF_BOUNDS_NO_POE.\n\n"
            "NOTE: sig_cert_revocation_poe-status is an internal variable. This is done because returning "
            "REVOCATION_OUT_OF_BOUNDS_NO_POE at this step in case of failure would lose the information provided "
            "by the current time indication/sub-indication.\n\n"
            "2) The building block shall perform the past certificate validation process specified in clause "
            "5.6.2.1 with the following inputs: the signature, the target certificate, the X.509 validation "
            "parameters, certificate validation data, X.509 validation constraints, cryptographic constraints and "
            "the set of POEs. If it returns PASSED/validation time, the building block shall go to the next step. "
            "Otherwise, the building block shall return the current time status and sub-indication with an "
            "explanation of the failure.\n\n"
            "3) If there is a POE of the signature value at (or before) the validation time returned in the "
            "previous step:\n\n"
            "- If current time indication/sub indication is INDETERMINATE/NO_CERTIFICATE_CHAIN_FOUND_NO_POE:\n\n"
            "a) If best-signature-time is before the issuance date of the signing certificate (notBefore field), "
            "the building block shall return the indication FAILED with the sub-indication NOT_YET_VALID.\n\n"
            "b) If best-signature-time is after the expiration date of the signing certificate, the building "
            "block shall return the indication INDETERMINATE with the sub-indication OUT_OF_BOUNDS_NO_POE.\n\n"
            "c) Else the building block shall go to step 7).\n\n"
            "- If current time indication/sub-indication is INDETERMINATE/REVOKED_NO_POE, "
            "INDETERMINATE/REVOCATION_OUT_OF_BOUNDS_NO_POE or INDETERMINATE/TRY_LATER because the certificate has "
            "been found to be suspended, then:\n\n"
            "a) If best-signature-time is before the issuance date of the signing certificate, the process shall "
            "return the indication FAILED with the sub-indication NOT_YET_VALID\n\n"
            "b) If best-signature-time is within the validity period of the signing certificate, the building "
            "block shall go to step 7).\n\n"
            "c) Otherwise the building block shall set the current time indication/sub-indication to "
            "INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED and continue the process.\n\n"
            "- If current time indication/sub-indication is INDETERMINATE/REVOKED_CA_NO_POE then:\n\n"
            "a) If there is a POE for the revocation data containing the revocation status information of the "
            "signer certificate at (or before) the revocation time of the CA certificate, then:\n\n"
            "i. If best signature time (lowest time at which there exists a POE for the signature value in the "
            "set of POEs) is within the validity period of the signing certificate, the building block shall go "
            "to step 7).\n\n"
            "ii. Otherwise the building block shall set the current time indication/sub-indication to "
            "OUT_OF_BOUNDS_NOT_REVOKED and continue the process.\n\n"
            "b) Otherwise, the building block shall return with the indication INDETERMINATE and the "
            "sub-indication REVOKED_CA_NO_POE.\n\n"
            "- If current time indication/sub-indication is INDETERMINATE/OUT_OF_BOUNDS_NO_POE or "
            "OUT_OF_BOUNDS_NOT_REVOKED:\n\n"
            "a) If best-signature-time (lowest time at which there exists a POE for the signature value in the "
            "set of POEs) is before the issuance date of the signing certificate (notBefore field), the building "
            "block shall return the indication FAILED with the sub-indication NOT_YET_VALID.\n\n"
            "b) If best-signature-time (lowest time at which there exists a POE for the signature value in the "
            "set of POEs) is after the issuance date and before the expiration date of the signing certificate, "
            "the building block shall go to step 7).\n\n"
            "4) If current time indication/sub-indication is INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE and "
            "for each algorithm (or key size) in the list concerned by the failure, there is a POE for the "
            "material that uses this algorithm (or key size) at a time before the time up to which the algorithm "
            "in question was considered secure, the building block shall go to step 7).\n\n"
            "5) If current time indication/sub indication is INDETERMINATE/TRY_LATER because the revocation "
            "information of the target certificate was not fresh enough:\n\n"
            "a) The building block shall determine from the set of POEs the earliest time at which the existence "
            "of the signature can be proven.\n\n"
            "b) The building block shall run the Revocation Freshness Checker (clause 5.2.5) with the "
            "corresponding revocation status information, the target certificate and the time determined in step "
            "a) above.\n\n"
            "c) If the checker returns PASSED, the building block shall go to step 7). Otherwise, the building "
            "block shall return the indication INDETERMINATE, the sub indication TRY_LATER and, if returned from "
            "the Revocation Freshness Checker, the suggestion for when to try the validation again.\n\n"
            "6) In all other cases, the building block shall return the current time indication/sub-indication "
            "together with an explanation of the failure.\n\n"
            "7) The building block shall return the indication and subindication contained in "
            "sig_cert_revocation_poe-status."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.6.3.3 (Output)",
        "testo": (
            "L'output principale di questo processo di convalida della firma DEVE essere uno stato che indica la "
            "validita' della firma; tale stato puo' essere accompagnato da informazioni aggiuntive (clausola "
            "5.1.3)."
        ),
        "testo_integrale": (
            "The main output of this signature validation process shall be a status indicating the validity of "
            "the signature. This status may be accompanied by additional information (see clause 5.1.3)."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.6.3.4 (Processing)",
        "testo": (
            "Convalida a lungo termine, dieci passi. 1) Se esistono uno o piu' Evidence Records (ER): a) prendere "
            "il primo ER non ancora elaborato; b) verificare questo ER secondo IETF RFC 4998 o IETF RFC 6283, "
            "tenendo conto dei seguenti requisiti aggiuntivi quando si convalida un token di marca temporale al "
            "tempo della successiva Archive Timestamp: i) prima di convalidare una marca temporale, estrarre le "
            "POE (secondo la clausola 5.6.2.3) della marca temporale all'interno della successiva marca temporale "
            "di archiviazione e inizializzare l'insieme temporaneo di POE con le POE estratte; ii) la convalida "
            "della marca temporale DEVE essere eseguita secondo la clausola 5.4; iii) il processo di convalida "
            "passata della firma per la firma della marca temporale (clausola 5.6.2.4) va usato con i seguenti "
            "input: la marca temporale, il certificato della TSA, i parametri di convalida X.509, i vincoli di "
            "convalida X.509, i vincoli crittografici, i dati di convalida dei certificati, "
            "l'indicazione/sotto-indicazione restituita al passo ii) e l'insieme di POE disponibile fino a quel "
            "momento, insieme all'insieme temporaneo di POE; iv) se il passo iii) da' PASSED il processo prosegue "
            "la validazione dell'ER, altrimenti il blocco costitutivo fallisce con lo stato e la "
            "sotto-indicazione restituiti dal processo di convalida passata della firma. L'uso dell'insieme "
            "temporaneo di POE e' giustificato dal fatto che l'algoritmo di IETF RFC 4998 o IETF RFC 6283 parte "
            "dalla marca temporale piu' antica e, poiche' fallisce appena una marca temporale dell'ER non e' "
            "valida, si assume che esista una POE per il materiale di convalida coperto dalla marca temporale "
            "successiva anche se questa non era ancora stata convalidata (NOTA 1). c) Se il passo b) ha trovato "
            "l'ER valido, aggiungere una POE per ogni oggetto coperto dall'ER al valore di signing time della "
            "marca temporale di archiviazione iniziale; d) se tutti gli ER sono stati convalidati, proseguire con "
            "il passo 2); e) proseguire con il passo 1)a). Un ER prova che un oggetto di dato esisteva e non e' "
            "stato modificato dal tempo del token di marca temporale iniziale nella prima marca temporale di "
            "archiviazione: i dettagli di quali oggetti di dato siano effettivamente coperti dall'ER vanno "
            "identificati con chiarezza nei documenti che specificano come usare gli ER nelle firme AdES per "
            "ottenere disponibilita' e integrita' a lungo termine dei dati di convalida (NOTA 2). Esempio: IETF "
            "RFC 4998 specifica nella sua Appendice A come aggiungere ER ai dati firmati CMS; quanto a cosa copre "
            "effettivamente l'ER, l'appendice definisce due alternative: l'oggetto CMS nel suo insieme (il campo "
            "contentInfo del CMS e tutto il suo contenuto), dove l'ER e' una POE per il contentInfo e tutto il "
            "suo contenuto; oppure l'oggetto CMS e il contenuto firmato come oggetti separati, dove l'ER e' una "
            "POE per il contentInfo e tutto il suo contenuto e anche per il contenuto firmato, soluzione "
            "particolarmente adatta alle firme CMS detached. 2) La SVA DEVE aggiungere all'insieme di POE una POE "
            "per ciascun oggetto della firma al momento corrente. L'insieme di POE in input puo' essere stato "
            "inizializzato da fonti esterne (per esempio fornito da un sistema di archiviazione esterno); tali "
            "POE sono usate senza elaborazione aggiuntiva (NOTA 3). 3) La SVA DEVE eseguire il processo di "
            "convalida per firme con tempo e per firme con materiale di convalida a lungo termine secondo la "
            "clausola 5.5, con tutti gli input, inclusa l'elaborazione degli attributi firmati come specificato. "
            "Se la firma non contiene attributi per la disponibilita' e integrita' a lungo termine del materiale "
            "di convalida, il processo DEVE restituire l'indicazione/sotto-indicazione e le informazioni "
            "restituite da quel processo, includendo preferibilmente l'informazione che e' stato eseguito solo il "
            "processo di convalida della firma con tempo (esempio: attributi per la disponibilita' e integrita' a "
            "lungo termine del materiale di convalida sono archive time-stamp, un ER o un DocumentTimeStamp in "
            "PAdES). Se il processo di convalida per firme con tempo ha restituito PASSED: se non esiste alcun "
            "vincolo di convalida che imponga la convalida degli attributi per la disponibilita' e integrita' a "
            "lungo termine, la SVA DEVE restituire l'indicazione PASSED; altrimenti la SVA DEVE andare al passo "
            "4). Se il processo ha restituito una delle seguenti indicazioni/sotto-indicazioni: "
            "INDETERMINATE/REVOKED_NO_POE, INDETERMINATE/REVOKED_CA_NO_POE, INDETERMINATE/OUT_OF_BOUNDS_NO_POE, "
            "INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED, INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE, "
            "INDETERMINATE/REVOCATION_OUT_OF_BOUNDS_NO_POE, INDETERMINATE/SIG_CONSTRAINTS_FAILURE o "
            "INDETERMINATE/TRY_LATER, il processo di convalida a lungo termine DEVE andare al passo successivo. "
            "In tutti gli altri casi il processo DEVE restituire l'indicazione/sotto-indicazione e le "
            "informazioni restituite dal processo di convalida per firme con tempo e firme con materiale di "
            "convalida a lungo termine. La convalida prosegue nei casi INDETERMINATE/REVOKED_NO_POE, "
            "INDETERMINATE/REVOKED_CA_NO_POE, INDETERMINATE/OUT_OF_BOUNDS_NO_POE, "
            "INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED, INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE, "
            "INDETERMINATE/REVOCATION_OUT_OF_BOUNDS_NO_POE, INDETERMINATE/SIG_CONSTRAINTS_FAILURE e "
            "INDETERMINATE/TRY_LATER perche' prove di esistenza aggiuntive possono aiutare a passare da "
            "INDETERMINATE a uno stato determinato (NOTA 4); i passi 4) e 5) non fanno parte del processo di "
            "convalida in se' ma servono a raccogliere POE per i passi 6) e 7) (NOTA 5). 4) Il processo DEVE "
            "inizializzare best-signature-time al best-signature-time restituito al passo 3) e DEVE aggiungere "
            "questo tempo all'insieme di POE come POE per la firma. 5) Se esiste almeno un attributo di marca "
            "temporale: a) la SVA DEVE selezionare la marca temporale piu' recente non ancora elaborata e DEVE "
            "eseguire la convalida della marca temporale secondo la clausola 5.4; b) se e' restituito PASSED ed "
            "esiste una POE della marca temporale per un tempo in cui la funzione di hash crittografica usata "
            "nella marca temporale (messageImprint.hashAlgorithm) era considerata affidabile, la SVA DEVE "
            "eseguire il processo di estrazione delle POE (clausola 5.6.2.3) con firma, marca temporale e vincoli "
            "crittografici come input e DEVE aggiungere le POE restituite all'insieme di POE; c) se l'output "
            "della convalida e' INDETERMINATE/REVOKED_NO_POE, INDETERMINATE/REVOKED_CA_NO_POE, "
            "INDETERMINATE/OUT_OF_BOUNDS_NO_POE, INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED, "
            "INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE o INDETERMINATE/REVOCATION_OUT_OF_BOUNDS_NO_POE, la "
            "SVA DEVE eseguire il processo di convalida passata della firma (clausola 5.6.2.4) con i seguenti "
            "input: la marca temporale, l'indicazione/sotto-indicazione restituita dalla convalida della marca "
            "temporale al passo 5)a), il certificato della TSA, i parametri di convalida X.509, i vincoli di "
            "convalida X.509, i vincoli crittografici, i dati di convalida dei certificati e l'insieme di POE. "
            "Poi: i) se restituisce PASSED la SVA DEVE determinare dall'insieme di POE il tempo piu' antico in "
            "cui l'esistenza della marca temporale puo' essere provata; ii) la SVA DEVE eseguire il processo di "
            "Signature Acceptance Validation secondo la clausola 5.2.8 con i seguenti input: il/i Signed Data "
            "Object, il tempo determinato al passo i) come parametro validation time, i vincoli crittografici - "
            "se il processo restituisce PASSED la SVA DEVE andare al passo successivo, altrimenti DEVE andare al "
            "passo d); iii) se esiste una POE per la marca temporale per un tempo in cui la funzione di hash "
            "crittografica usata nella marca temporale era considerata affidabile, la SVA DEVE eseguire il "
            "processo di estrazione delle POE (clausola 5.6.2.3), DEVE aggiungere le POE restituite all'insieme "
            "di POE e DEVE proseguire con il passo 5)a) usando l'attributo di marca temporale successivo; d) in "
            "tutti gli altri casi: se nessun vincolo specifico che imponga la validita' dell'attributo e' "
            "specificato nei vincoli di convalida, la SVA DEVE ignorare l'attributo e DEVE proseguire con il "
            "passo 5) usando l'attributo di marca temporale successivo; altrimenti il processo DEVE fallire con "
            "l'indicazione/sotto-indicazione restituita e le spiegazioni associate; e) se tutti gli attributi di "
            "marca temporale sono stati elaborati, la SVA DEVE proseguire con il passo 6), altrimenti DEVE "
            "proseguire con il passo 5)a). 6) La SVA DEVE determinare dall'insieme di POE il tempo piu' antico in "
            "cui l'esistenza della firma puo' essere provata e DEVE porre best-signature-time a questo nuovo "
            "tempo determinato. 7) Convalida passata della firma: la SVA DEVE eseguire il processo di convalida "
            "passata della firma (clausola 5.6.2.4) con i seguenti input: la firma, "
            "l'indicazione/sotto-indicazione di stato restituita al passo 3), il certificato di firma, i "
            "parametri di convalida X.509, i dati di convalida dei certificati, i vincoli di convalida X.509, i "
            "vincoli crittografici, l'insieme di POE e best-signature-time - se restituisce PASSED la SVA DEVE "
            "andare al passo successivo, altrimenti DEVE restituire l'indicazione/sotto-indicazione e le "
            "spiegazioni associate restituite dal processo di convalida passata della firma. 8) Gestione del "
            "ritardo della marca temporale: se la firma contiene un token di marca temporale della firma e i "
            "vincoli di convalida specificano un ritardo della marca temporale (time stamp delay): a) se non e' "
            "presente alcuna proprieta'/attributo di signing time, il processo DEVE restituire l'indicazione "
            "INDETERMINATE con sotto-indicazione SIG_CONSTRAINTS_FAILURE; b) se e' presente una "
            "proprieta'/attributo di signing time, il processo DEVE verificare che il tempo dichiarato "
            "nell'attributo piu' il ritardo della marca temporale sia successivo al best-signature-time "
            "determinato al passo 6): se il controllo riesce si passa al passo successivo, altrimenti il processo "
            "DEVE restituire l'indicazione INDETERMINATE con sotto-indicazione SIG_CONSTRAINTS_FAILURE. 9) La SVA "
            "DEVE eseguire il processo di Signature Acceptance Validation secondo la clausola 5.2.8 con i "
            "seguenti input: il/i Signed Data Object; il tempo determinato al passo 7) come parametro validation "
            "time; i vincoli crittografici. Questo controllo e' gia' stato eseguito al passo 3) come parte della "
            "convalida di base della firma al tempo corrente, ma e' ripetuto per il tempo piu' antico in cui si "
            "sa che la firma e' esistita, per esempio per controllare se gli algoritmi erano affidabili a quel "
            "tempo; i vincoli sugli elementi della firma sono gia' stati trattati al passo 2) e non devono essere "
            "ricontrollati (NOTA 6). Se il processo di Signature Acceptance Validation restituisce PASSED la SVA "
            "DEVE andare al passo successivo, altrimenti DEVE restituire l'indicazione e la sotto-indicazione "
            "restituite dal processo di Signature Acceptance Validation. 10) Estrazione dei dati: la SVA DEVE "
            "restituire l'indicazione di successo PASSED; inoltre DOVREBBE restituire informazioni aggiuntive "
            "estratte dalla firma e/o usate dai passi intermedi, in particolare il best-signature-time "
            "determinato al passo 6) e risultati intermedi come i risultati di convalida di ogni token di marca "
            "temporale. Cio' che il DA fa di queste informazioni e' fuori dall'ambito del presente documento "
            "(NOTA 7)."
        ),
        "testo_integrale": (
            "1) If there is one or more Evidence Records (ERs):\n\n"
            "a) The process shall take the first ER that was not yet processed.\n\n"
            "b) The process shall verify this ER according to IETF RFC 4998 [i.9] or IETF RFC 6283 [i.10] taking "
            "into account the following additional requirements when validating a time-stamp token at the time of "
            "the following Archive Timestamp:\n\n"
            "i) Before validating a time-stamp the process shall extract POEs (as per clause 5.6.2.3) of the "
            "time-stamp within the next Archive timestamp and initialize the set of temporary POEs with the "
            "extracted POEs.\n\n"
            "ii) The time stamp validation of the time-stamp token shall be performed, as per clause 5.4.\n\n"
            "iii) The past signature validation process for the signature of the time-stamp token as per clause "
            "5.6.2.4 shall be used with the following inputs: the time-stamp, the TSA's certificate, the X.509 "
            "validation parameters, the X.509 validation constraints, the cryptographic constraints, certificate "
            "validation data, the indication/sub-indication returned in step ii) and the set of POEs available so "
            "far, and the set of temporary POEs.\n\n"
            "iv) If step iii) results in PASSED the process shall continue the ER validation, otherwise the "
            "building block shall fail with the status indication and sub-indication returned from the past "
            "signature validation process.\n\n"
            "NOTE 1: The usage of the temporary POEs set is justified by the fact that the validation algorithm "
            "within IETF RFC 4998 [i.9] or IETF RFC 6283 [i.10] starts with the earliest time-stamp. But since it "
            "fails as soon as one time-stamp within the ER is not valid, it is assumed there is a POE for the "
            "validation material covered be the next time-stamp even if this time-stamp was not yet validated "
            "before.\n\n"
            "c) If step b) found the ER to be valid, the process shall add a POE for every object covered by the "
            "ER at signing time value of the initial archive time-stamp.\n\n"
            "d) If all ERs have been validated, the process shall continue with step 2).\n\n"
            "e) The process shall continue with step 1)a).\n\n"
            "NOTE 2: An ER proves that a data object existed and has not been changed from the time of the "
            "initial time-stamp token within the first archive time-stamp. The details of what data objects are "
            "actually covered by the ER need to be clearly identified in the documents that specify how to use "
            "ERs in AdES signatures for achieving long term availability and integrity of validation data.\n\n"
            "EXAMPLE 1: IETF RFC 4998 [i.9] specifies, in its Appendix A, how to add ERs to CMS [i.8] signed "
            "data. In terms of what the ER actually covers, this appendix defines two alternatives:\n\n"
            "• The CMS object as a whole (the CMS contentInfo field and all its contents). In this case, the ER "
            "is a POE for the contentInfo and all its contents.\n\n"
            "• The CMS object and the signed content as separated objects. In this case, the ER is a POE for the "
            "contentInfo and all its contents, and also for the signed content. This is particularly suitable for "
            "detached CMS signatures.\n\n"
            "2) The SVA shall add a POE for each object in the signature at the current time to the set of POEs.\n\n"
            "NOTE 3: The set of POE in the input may have been initialized from external sources (e.g. provided "
            "from an external archiving system). These POEs are used without additional processing.\n\n"
            "3) The SVA shall perform the Validation process for Signatures with Time and Signatures with "
            "Long-Term Validation Material as per clause 5.5 with all the inputs, including the processing of any "
            "signed attributes as specified.\n\n"
            "- If the signature does not contain any attributes for long term availability and integrity of "
            "validation material, the process shall return the indication/sub-indication and information returned "
            "by the Validation process for Signatures with Time and Signatures with Long-Term Validation "
            "Material. Additional information should be included indicating that only the "
            "signature-with-time-validation process has been performed.\n\n"
            "EXAMPLE 2: Attributes for Long Term Availability and integrity of validation material are archive "
            "time-stamp, an ER or a DocumentTimeStamp in PAdES.\n\n"
            "- If the Validation process for Signatures with Time and Signatures with Long-Term Validation "
            "Material returned PASSED:\n\n"
            "• If there is no validation constraint mandating the validation of the attributes for Long Term "
            "Availability and integrity of validation material, the SVA shall return the indication PASSED.\n\n"
            "• Otherwise, the SVA shall go to step 4).\n\n"
            "- If the Validation process for Signatures with Time and Signatures with Long-Term Validation "
            "Material returned one of the following indications/sub-indications: INDETERMINATE/REVOKED_NO_POE, "
            "INDETERMINATE/REVOKED_CA_NO_POE, INDETERMINATE/OUT_OF_BOUNDS_NO_POE, "
            "INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED, INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE, "
            "INDETERMINATE/REVOCATION_OUT_OF_BOUNDS_NO_POE, INDETERMINATE/SIG_CONSTRAINTS_FAILURE or "
            "INDETERMINATE/TRY_LATER, the long-term validation process shall go to the next step.\n\n"
            "- In all other cases, the process shall return the indication/sub-indication and information "
            "returned by the Validation process for Signatures with Time and Signatures with Long-Term Validation "
            "Material.\n\n"
            "NOTE 4: Validation is continued in the cases INDETERMINATE/REVOKED_NO_POE, "
            "INDETERMINATE/REVOKED_CA_NO_POE, INDETERMINATE/OUT_OF_BOUNDS_NO_POE, "
            "INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED, INDETERMINATE/ CRYPTO_CONSTRAINTS_FAILURE_NO_POE, "
            "INDETERMINATE/REVOCATION_OUT_OF_BOUNDS_NO_POE INDETERMINATE/SIG_CONSTRAINTS_FAILURE and "
            "INDETERMINATE/TRY_LATER because additional proof of existences can help to go from INDETERMINATE to "
            "a determined status.\n\n"
            "NOTE 5: Steps 4) and 5) below are not part of the validation process per se, but are present to "
            "collect POEs for steps 6) and 7).\n\n"
            "4) The process shall initialize best-signature-time to the best-signature-time returned in step 3) "
            "and add this time as POE for the signature to the set of POEs.\n\n"
            "5) If there is at least one time-stamp attribute:\n\n"
            "a) The SVA shall select the newest time-stamp that has not been processed and shall perform the "
            "time-stamp validation, as per clause 5.4.\n\n"
            "b) If PASSED is returned and a POE exists for the time-stamp for a time when the cryptographic hash "
            "function used in the time-stamp (messageImprint.hashAlgorithm) has been considered reliable, the SVA "
            "shall perform the POE extraction process (clause 5.6.2.3) with the signature, the time-stamp and the "
            "cryptographic constraints as inputs. The SVA shall add the returned POEs to the set of POEs.\n\n"
            "c) If the output of the validation is INDETERMINATE/REVOKED_NO_POE, INDETERMINATE/REVOKED_CA_NO_POE, "
            "INDETERMINATE/OUT_OF_BOUNDS_NO_POE, INDETERMINATE/OUT_OF_BOUNDS_NOT_REVOKED, "
            "INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE or INDETERMINATE/REVOCATION_OUT_OF_BOUNDS_NO_POE,, "
            "the SVA shall perform past signature validation process (as per clause 5.6.2.4) with the following "
            "inputs: the time-stamp, the indication/sub-indication returned by the time-stamp validation process "
            "in step 5)a), the TSA's certificate, the X.509 validation parameters, X.509 validation constraints, "
            "cryptographic constraints, certificate validation data and the set of POEs. Then:\n\n"
            "i) If it returns PASSED the SVA shall determine from the set of POEs the earliest time the existence "
            "of the time-stamp can be proven.\n\n"
            "ii) The SVA shall perform the Signature Acceptance Validation process as per clause 5.2.8 with the "
            "following inputs:\n\n"
            "• The Signed Data Object(s).\n\n"
            "• The time determined in step i) above as the validation time parameter.\n\n"
            "• The Cryptographic Constraints.\n\n"
            "If the Signature Acceptance Validation process returns PASSED, the SVA shall go to the next step. "
            "Otherwise, the SVA shall go to step d).\n\n"
            "iii) If a POE exists for the time-stamp for a time when the cryptographic hash function used in the "
            "time-stamp has been considered reliable, the SVA shall perform the POE extraction process (clause "
            "5.6.2.3) and shall add the returned POEs to the set of POEs, and shall continue with step 5)a) using "
            "the next time-stamp attribute.\n\n"
            "d) In all other cases:\n\n"
            "• If no specific constraints mandating the validity of the attribute are specified in the validation "
            "constraints, the SVA shall ignore the attribute and shall continue with step 5) using the next "
            "time-stamp attribute.\n\n"
            "• Otherwise, the process shall fail with the returned indication/sub-indication and associated "
            "explanations.\n\n"
            "e) If all time-stamp attributes have been processed, the SVA shall continue with step 6). Otherwise, "
            "the SVA shall continue with step 5)a).\n\n"
            "6) The SVA shall determine from the set of POEs the earliest time the existence of the signature can "
            "be proven and set best-signature-time to this new determined time.\n\n"
            "7) Past signature validation: the SVA shall perform the past signature validation process (as per "
            "clause 5.6.2.4) with the following inputs: the signature, the status indication/sub-indication "
            "returned in step 3), the signing certificate, the X.509 validation parameters, certificate "
            "validation data, X.509 validation constraints, cryptographic constraints, the set of POEs and "
            "best-signature-time. If it returns PASSED, the SVA shall go to the next step. Otherwise, the SVA "
            "shall return the indication/sub-indication and associated explanations returned from the past "
            "signature validation process.\n\n"
            "8) Handling time-stamp delay: If the signature contains a signature time stamp token and the "
            "validation constraints specify a time stamp delay:\n\n"
            "a) If no signing time property/attribute is present, the process shall return the indication "
            "INDETERMINATE with the sub indication SIG_CONSTRAINTS_FAILURE.\n\n"
            "b) If a signing time property/attribute is present, the process shall check that the claimed time in "
            "the attribute plus the time stamp delay is after the best-signature-time determined in step 6) "
            "above. If the check is successful, the process shall go to the next step. Otherwise, the process "
            "shall return the indication INDETERMINATE with the sub indication SIG_CONSTRAINTS_FAILURE.\n\n"
            "9) The SVA shall perform the Signature Acceptance Validation process as per clause 5.2.8 with the "
            "following inputs:\n\n"
            "a) The Signed Data Object(s).\n\n"
            "b) The time determined in step 7) as the validation time parameter.\n\n"
            "c) The Cryptographic Constraints.\n\n"
            "NOTE 6: This check has been performed already in step 3) as part of basic signature validation for "
            "current time but is repeated here for the earliest time the signature is known to have existed to "
            "e.g. check if the algorithms were reliable at that time. Signature elements constraints have already "
            "been dealt with in step 2) and need not be rechecked.\n\n"
            "If the Signature Acceptance Validation process returns PASSED, the SVA shall go to the next step. "
            "Otherwise, the SVA shall return the indication and sub-indication returned by the Signature "
            "Acceptance Validation Process.\n\n"
            "10) Data extraction: the SVA shall return the success indication PASSED. In addition, the SVA should "
            "return additional information extracted from the signature and/or used by the intermediate steps. In "
            "particular, the SVA should return the best-signature-time determined in step 6) as well as "
            "intermediate results such as the validation results of any time-stamp token.\n\n"
            "NOTE 7: What the DA does with this information is out of the scope of the present document."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 5.6.1 (Introduction)",
        "testo": (
            "La clausola descrive un processo di convalida per le firme che garantiscono disponibilita' e "
            "integrita' a lungo termine del materiale di convalida (Long Term Availability and Integrity of "
            "Validation Material). E' utile in particolare quando le informazioni sullo stato di revoca e le "
            "prove di esistenza (POE, proof of existence) sono disponibili ma non come parte di una firma con "
            "disponibilita' e integrita' a lungo termine: la SVA (Signature Validation Application) assume allora "
            "tali evidenze aggiuntive come input, oltre alla firma di base da convalidare (NOTA 1). Tale "
            "convalida puo' essere eseguita off-line quando tutto il materiale di convalida richiesto e' "
            "disponibile all'interno della firma e nella configurazione locale (NOTA 2). Il processo si fonda sui "
            "blocchi costitutivi (building blocks) di base descritti nella clausola 5.2 e sui blocchi aggiuntivi "
            "definiti nella clausola 5.6.2."
        ),
        "testo_integrale": (
            "This clause describes a validation process for Signatures providing Long Term Availability and "
            "Integrity of Validation Material.\n\n"
            "NOTE 1: This is in particular useful in the case where revocation status information and proofs of "
            "existence are available, but not as part of a Signature providing Long Term Availability and "
            "Integrity of Validation Material. The SVA then takes such additional evidences as input, in addition "
            "to the Basic Signature to validate.\n\n"
            "NOTE 2: Such a validation can be done off-line when all required validation material is available "
            "within the signature and local configuration.\n\n"
            "The process builds on the building blocks described in clause 5.2 and the additional building blocks "
            "defined in clause 5.6.2."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.6.2.1.1 (Description)",
        "testo": (
            "Descrive il processo che convalida un certificato a una data/ora che puo' cadere nel passato: e' "
            "necessario nelle impostazioni di convalida a lungo termine quando un evento compromettente (per "
            "esempio la scadenza del certificato dell'entita' finale) impedisce all'algoritmo tradizionale di "
            "convalida dei certificati (clausola 5.2.6) di accertare lo stato di validita' del certificato - se "
            "il certificato dell'entita' finale e' scaduto al momento corrente, l'algoritmo tradizionale "
            "restituisce INDETERMINATE con sotto-indicazione OUT_OF_BOUNDS_NO_POE o OUT_OF_BOUNDS_NOT_REVOKED per "
            "effetto del passo 5) della clausola 5.2.6. Razionale: se una catena di certificati e' stata "
            "utilizzabile per convalidare un certificato in una data passata, la stessa catena puo' essere usata "
            "al momento corrente per derivare lo stesso stato di validita', purche' ogni certificato della catena "
            "soddisfi una delle due condizioni: a) lo stato di revoca del certificato e' accertabile al momento "
            "corrente (tipicamente se il certificato non e' ancora scaduto e si ottengono al momento corrente "
            "informazioni di revoca appropriate); oppure b) lo stato di revoca e' accertabile usando informazioni "
            "di revoca 'vecchie', se il certificato (rispettivamente il dato di revoca contenente l'informazione "
            "sullo stato di revoca) e' provato esistente a una data passata in cui l'emittente era ancora "
            "considerato affidabile e sotto il controllo della propria chiave di firma. Il processo di convalida "
            "passata fa scorrere il tempo di convalida dal momento corrente a una data passata ogni volta che "
            "incontra un certificato provato revocato, una violazione dei vincoli crittografici o una violazione "
            "della freschezza (processo di scorrimento del tempo di convalida, clausola 5.6.2.2). Oltre alla "
            "catena di certificati, il processo restituisce l'ultimo valore del tempo di convalida associato al "
            "certificato obiettivo (il certificato da convalidare): un istante in cui il certificato di firma e' "
            "valido e la catena e' convalidabile secondo il modello selezionato (modello a catena o modello a "
            "guscio). Qualunque oggetto firmato con il certificato obiettivo e provato esistente prima di questo "
            "tempo di convalida puo' essere accettato come valido; questa asserzione e' la base dei processi di "
            "convalida passata delle clausole successive."
        ),
        "testo_integrale": (
            "This process validates a certificate at a date/time which can be in the past. This may become "
            "necessary in the long term validation settings when a compromising event (for instance, expiration "
            "of the end-entity certificate) prevents the traditional certificate validation algorithm (see clause "
            "5.2.6) from asserting the validation status of a certificate (for instance, in case the end-entity "
            "certificate is expired at the current time, the traditional validation algorithm returns the "
            "indication INDETERMINATE with the sub-indication OUT_OF_BOUNDS_NO_POE or OUT_OF_BOUNDS_NOT_REVOKED "
            "due to the step 5) of the processing in clause 5.2.6).\n\n"
            "The rationale of the algorithm described below can be summarized in the following: if a certificate "
            "chain has been useable to validate a certificate at some date/time in the past, the same chain can "
            "be used at the current time to derive the same validity status, provided each certificate in the "
            "chain satisfies one of the following:\n\n"
            "a) The revocation status of the certificate can be ascertained at the current time (typically, if "
            "the certificate is not yet expired and appropriate revocation status information is obtained at the "
            "current time).\n\n"
            "b) The revocation status of the certificate can be ascertained using \"old\" revocation status "
            "information such that the certificate (respectively the revocation data containing the revocation "
            "status information) is proven to having existed at a date in the past when the issuer of the "
            "certificate (respectively the revocation data containing the revocation status information) was "
            "still considered reliable and under control of its signing key.\n\n"
            "The past certificate validation process will slide the validation time from the current time to some "
            "date in the past each time it encounters a certificate proven to be revoked, a cryptographic "
            "constraints failure or a freshness failure (see the Validation Time Sliding process in clause "
            "5.6.2.2). In addition to the certificate chain, the process outputs the last value of validation "
            "time associated with the target certificate (the certificate to validate) which is a point in time "
            "when the signing certificate is valid and the chain can be validated corresponding to the selected "
            "model (chain model or shell model). Any object signed with the target certificate and proven to "
            "exist before this validation time can be accepted as valid. This assertion is the basis of the past "
            "validation processes presented in the next clauses."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.6.2.1.2 (Input)",
        "testo": (
            "Tabella 21 - Input del blocco costitutivo di convalida passata del certificato: certificato "
            "obiettivo (obbligatorio); parametri di convalida X.509, incluso l'insieme delle trust anchor "
            "(obbligatorio); un insieme di POE (obbligatorio); dati di convalida dei certificati (obbligatorio); "
            "vincoli di convalida X.509 (opzionale); vincoli crittografici (opzionale)."
        ),
        "testo_integrale": (
            "**Table 21: Inputs to past certificate validation building block**\n\n"
            "|Input|Requirement|\n"
            "|---|---|\n"
            "|Target certificate|Mandatory|\n"
            "|X.509 Validation Parameters including set of trust anchors|Mandatory|\n"
            "|A set of POEs|Mandatory|\n"
            "|Certificate Validation Data|Mandatory|\n"
            "|X.509 Validation Constraints|Optional|\n"
            "|Cryptographic Constraints|Optional|"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.6.2.1.3 (Output)",
        "testo": (
            "Tabella 22 - Output del blocco costitutivo di convalida passata del certificato: PASSED con tempo di "
            "convalida e catena di certificati; oppure INDETERMINATE con sotto-indicazione "
            "NO_CERTIFICATE_CHAIN_FOUND, NO_POE, CERTIFICATE_CHAIN_GENERAL_FAILURE o CHAIN_CONSTRAINTS_FAILURE."
        ),
        "testo_integrale": (
            "**Table 22: Outputs of past certificate validation building block**\n\n"
            "|Indication|\n"
            "|---|\n"
            "|PASSED + validation time + certificate chain|\n"
            "|INDETERMINATE NO_CERTIFICATE_CHAIN_FOUND|\n"
            "|NO_POE|\n"
            "|CERTIFICATE_CHAIN_GENERAL_FAILURE|\n"
            "|CHAIN_CONSTRAINTS_FAILURE|"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.6.2.2.1 (Description)",
        "testo": (
            "Il blocco costitutivo fa scorrere il tempo di convalida dal momento corrente a una data passata ogni "
            "volta che incontra un certificato provato revocato, una violazione dei vincoli crittografici o una "
            "violazione della freschezza. Il processo restituisce l'ultimo valore del tempo di convalida "
            "associato al certificato obiettivo (il certificato da convalidare): un istante in cui il certificato "
            "di firma e' valido e la catena e' convalidabile secondo il modello selezionato (modello a catena o "
            "modello a guscio)."
        ),
        "testo_integrale": (
            "This building block slides the validation time from the current-time to some date in the past each "
            "time it encounters a certificate proven to be revoked, a cryptographic constraints failure or a "
            "freshness failure.\n\n"
            "The process outputs the last value of validation time associated with the target certificate (the "
            "certificate to validate) which is a point in time when the signing certificate is valid and the "
            "chain can be validated corresponding to the selected model (chain model or shell model)."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.6.2.2.2 (Input)",
        "testo": (
            "Tabella 23 - Input del blocco costitutivo di scorrimento del tempo di convalida: una catena di "
            "certificati prospettica (obbligatorio); un insieme di POE (obbligatorio); dati di convalida dei "
            "certificati (obbligatorio); una sunset date della trust anchor (opzionale); vincoli crittografici "
            "(opzionale); vincoli di convalida X.509 (opzionale)."
        ),
        "testo_integrale": (
            "**Table 23: Inputs to the validation time sliding building block**\n\n"
            "|Input|Requirement|\n"
            "|---|---|\n"
            "|A prospective certificate chain|Mandatory|\n"
            "|A set of POEs|Mandatory|\n"
            "|Certificate Validation Data|Mandatory|\n"
            "|A trust anchor sunset date|Optional|\n"
            "|Cryptographic constraints|Optional|\n"
            "|X.509 validation constraints|Optional|"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.6.2.2.3 (Output)",
        "testo": (
            "Tabella 24 - Output del blocco costitutivo di scorrimento del tempo di convalida: PASSED con tempo "
            "di convalida; oppure INDETERMINATE con sotto-indicazione NO_POE."
        ),
        "testo_integrale": (
            "**Table 24: Outputs of the validation time sliding building block**\n\n"
            "|Indication|\n"
            "|---|\n"
            "|PASSED + validation time|\n"
            "|INDETERMINATE NO_POE|"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.6.2.3.1 (Description)",
        "testo": (
            "Descrive il blocco costitutivo che deriva le POE da una data marca temporale, sotto due presupposti: "
            "la convalida della marca temporale ha restituito PASSED; e la funzione di hash crittografica usata "
            "nella marca temporale (messageImprint.hashAlgorithm) e' considerata affidabile al momento corrente "
            "o, se cosi' non e', esiste una POE per quella marca temporale relativa a un tempo in cui la funzione "
            "di hash era ancora considerata affidabile. Nel caso semplice una marca temporale fornisce una POE "
            "per ciascun elemento di dato protetto dalla marca temporale alla data/ora di generazione del token "
            "(esempio: una marca temporale sul valore di firma fornisce una POE del valore di firma alla data/ora "
            "di generazione della marca temporale). Una marca temporale puo' fornire anche una POE indiretta "
            "quando e' calcolata sul valore di hash di alcuni dati invece che sui dati stessi: una POE per DATA a "
            "T1 e' derivabile dalla marca temporale se esiste una POE per h(DATA) a una data T1, dove h e' una "
            "funzione di hash crittografica e DATA sono dei dati (per esempio un certificato); se esiste una POE "
            "per DATA a una data T2 successiva a T1; e se h e' asserita nei vincoli crittografici come fidata "
            "almeno fino a una data T successiva a T2."
        ),
        "testo_integrale": (
            "This building block derives POEs from a given time-stamp. Assumptions:\n\n"
            "• The time-stamp validation has returned PASSED.\n\n"
            "• The cryptographic hash function used in the time-stamp (messageImprint.hashAlgorithm) is "
            "considered reliable at current time or, if this is not the case, a POE for that time-stamp exists "
            "for a time when the hash function has still been considered reliable.\n\n"
            "In the simple case, a time-stamp gives a POE for each data item protected by the time-stamp at the "
            "generation date/time of the token.\n\n"
            "EXAMPLE: A time-stamp on the signature value gives a POE of the signature value at the generation "
            "date/time of the time-stamp.\n\n"
            "A time-stamp can also give an indirect POE when it is computed on the hash value of some data "
            "instead of the data itself. A POE for DATA at T1 can be derived from the time-stamp:\n\n"
            "• if there is a POE for h(DATA) at a date T1,where h is a cryptographic hash function and DATA is "
            "some data (e.g. a certificate); and\n\n"
            "• if there is a POE for DATA at a date T2 after T1; and\n\n"
            "• if h is asserted in the cryptographic constraints to be trusted until at least a date T after T2."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.6.2.3.2 (Input)",
        "testo": (
            "Tabella 25 - Input del blocco costitutivo di estrazione delle POE: firma (obbligatorio); un "
            "attributo con un token di marca temporale (obbligatorio); un insieme di POE (obbligatorio, ma puo' "
            "essere vuoto)."
        ),
        "testo_integrale": (
            "**Table 25: Inputs to the POE extraction building block**\n\n"
            "|Input|Requirement|\n"
            "|---|---|\n"
            "|Signature|Mandatory|\n"
            "|An attribute with a time-stamp token|Mandatory|\n"
            "|A set of POEs|Mandatory (but may be empty)|"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.6.2.4.1 (Description)",
        "testo": (
            "Il blocco costitutivo si usa quando la convalida di una firma (o di un token di marca temporale) "
            "fallisce al momento corrente con stato INDETERMINATE e le prove di esistenza fornite possono aiutare "
            "a passare a uno stato determinato."
        ),
        "testo_integrale": (
            "This building block is used when validation of a signature (or a time-stamp token) fails at the "
            "current time with an INDETERMINATE status such that the provided proofs of existence may help to go "
            "to a determined status."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.6.2.4.2 (Input)",
        "testo": (
            "Tabella 26 - Input del blocco costitutivo di convalida passata della firma: firma (obbligatorio); "
            "indicazione/sotto-indicazione dello stato al momento corrente (obbligatorio); certificato obiettivo "
            "(obbligatorio); parametri di convalida X.509 (obbligatorio); un insieme di POE (obbligatorio); "
            "best-signature-time (obbligatorio); dati di convalida dei certificati (opzionale); vincoli di "
            "convalida X.509 (opzionale); vincoli crittografici (opzionale)."
        ),
        "testo_integrale": (
            "**Table 26: Inputs to the past signature validation building block**\n\n"
            "|Input|Requirement|\n"
            "|---|---|\n"
            "|Signature|Mandatory|\n"
            "|The current time status indication/sub-indication|Mandatory|\n"
            "|Target certificate|Mandatory|\n"
            "|X.509 Validation Parameters|Mandatory|\n"
            "|A set of POEs|Mandatory|\n"
            "|Best-signature-time|Mandatory|\n"
            "|Certificate Validation Data|Optional|\n"
            "|X.509 Validation Constraints|Optional|\n"
            "|Cryptographic constraints|Optional|"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.6.3.1 (Description)",
        "testo": (
            "Descrive il processo usato per la convalida delle firme che garantiscono disponibilita' e integrita' "
            "a lungo termine del materiale di convalida. Diversi attributi non firmati possono essere presenti "
            "per conseguire conservazione e disponibilita' a lungo termine: marche temporali sul valore di firma "
            "(firma con tempo); marche temporali sui riferimenti ai dati di convalida; marche temporali sui "
            "riferimenti ai dati di convalida, sul valore di firma e sulla marca temporale della firma; attributi "
            "con i valori dei dati di convalida; attributi con riferimenti ai dati di convalida; marche temporali "
            "di archiviazione sull'intera firma esclusa l'ultima marca temporale di archiviazione; Evidence "
            "Records su parte o sull'intera firma. Il DA puo' fornire alla SVA un insieme iniziale di POE che "
            "provano l'esistenza di elementi usati nella convalida: la struttura o il formato di tali POE "
            "dipendono dall'implementazione. Esempio: tali POE possono essere fornite dal DA per firme, "
            "certificati o marche temporali e possono derivare da sistemi di archiviazione esterni e altre fonti; "
            "le POE per le CA possono essere estratte dalle Trusted Lists."
        ),
        "testo_integrale": (
            "This process is used for validation of Signatures providing Long Term Availability and Integrity of "
            "Validation Material. Several unsigned attributes can be present assisting in achieving long-term "
            "preservation and availability:\n\n"
            "• time-stamp(s) on the signature value (Signature with Time);\n\n"
            "• time-stamp(s) on the references of validation data;\n\n"
            "• time-stamp(s) on the references of validation data, the signature value and the signature "
            "time-stamp;\n\n"
            "• attributes with the values of validation data; or\n\n"
            "• attributes with references to validation data;\n\n"
            "• archive time-stamp(s) on the whole signature except the last archive time-stamp; or\n\n"
            "• Evidence Records on part or the whole signature.\n\n"
            "The DA may provide to the SVA an initial set of POEs proving the existence of elements used in "
            "validation. The structure or format of these POEs are implementation dependent.\n\n"
            "EXAMPLE: Such POEs can be provided by the DA for signatures, certificates or time-stamps and can be "
            "derived from external archival systems and other sources. POEs for CAs can be extracted from Trusted "
            "Lists."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.6.3.2 (Input)",
        "testo": (
            "Tabella 27 - Input del processo di convalida a lungo termine (Long Term Validation): Signed Data "
            "Object (obbligatorio); documento del firmatario o SDR, elenco delle trust anchor (per esempio TSL), "
            "politiche di convalida della firma, configurazione locale, un insieme di POE, certificato di firma, "
            "Evidence Records e dati di convalida dei certificati (tutti opzionali)."
        ),
        "testo_integrale": (
            "**Table 27: Inputs to the Long Term Validation process**\n\n"
            "|Input|Requirement|\n"
            "|---|---|\n"
            "|Signed Data Object|Mandatory|\n"
            "|Signer's Document or SDR|Optional|\n"
            "|Trust anchor list (e.g. TSL)|Optional|\n"
            "|Signature Validation Policies|Optional|\n"
            "|Local configuration|Optional|\n"
            "|A set of POEs|Optional|\n"
            "|Signing Certificate|Optional|\n"
            "|Evidence Records|Optional|\n"
            "|Certificate Validation Data|Optional|"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 5.6.1 (Introduction)",
    "clausola 5.6.2.1.1 (Description)",
    "clausola 5.6.2.1.2 (Input)",
    "clausola 5.6.2.1.3 (Output)",
    "clausola 5.6.2.1.4 (Processing)",
    "clausola 5.6.2.2.1 (Description)",
    "clausola 5.6.2.2.2 (Input)",
    "clausola 5.6.2.2.3 (Output)",
    "clausola 5.6.2.2.4 (Processing)",
    "clausola 5.6.2.3.1 (Description)",
    "clausola 5.6.2.3.2 (Input)",
    "clausola 5.6.2.3.3 (Output)",
    "clausola 5.6.2.3.4 (Processing)",
    "clausola 5.6.2.4.1 (Description)",
    "clausola 5.6.2.4.2 (Input)",
    "clausola 5.6.2.4.3 (Output)",
    "clausola 5.6.2.4.4 (Processing)",
    "clausola 5.6.3.1 (Description)",
    "clausola 5.6.3.2 (Input)",
    "clausola 5.6.3.3 (Output)",
    "clausola 5.6.3.4 (Processing)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Nessuna relazione interna a questa Fonte: i rinvii alle clausole 5.1.3, 5.2,
# 5.2.5, 5.2.6, 5.2.8, 5.4, 5.5 e 5.6.2.x e quelli esterni (IETF RFC 4998/6283/5280,
# CMS, PAdES, TSL) non sono trasformati in archi da questo modulo: il
# cross-collegamento e' demandato alla sessione principale (ADR-0009, Fase 6).
RELAZIONI: list[dict] = []
