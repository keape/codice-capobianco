"""Estrazione granulare ETSI EN 319 102-1 V1.4.1 (2024-06) — Capitolo 5:
clausola 5.3 (Validation process for Basic Signatures: 5.3.1 Description,
5.3.2 Inputs, 5.3.3 Outputs, 5.3.4 Processing) e clausola 5.4 (Time-stamp
validation building block: 5.4.1 Description, 5.4.2 Inputs, 5.4.3 Outputs,
5.4.4 Processing).

Fonte: ETSI EN 319 102-1 V1.4.1, "Electronic Signatures and Infrastructures
(ESI); Procedures for Creation and Validation of AdES Digital Signatures;
Part 1: Creation and Validation". Testo ufficiale della porzione in
app/.source_cache/etsi_319_102/cap05.txt (righe 1-226; la riga 228 e' il
solo a capo finale). Manifest di split:
app/.source_cache/etsi_319_102/manifest.json. La numerazione definitiva
della Fonte e' cablata dalla sessione principale: questo modulo NON tocca
app/seed.py.

Perimetro: SOLO le clausole 5.3.1-5.3.4 e 5.4.1-5.4.4. Il file .txt del
capitolo non contiene altri contenuti (nessun annesso, nessuna sezione
"History"), quindi non c'e' nulla di escluso oltre il front matter gia'
ripulito a monte; la clausola 2 "References" e' in cap01 e non riguarda
questo capitolo.

Copertura (ADR-0007): un nodo per ciascuna sottoclavola numerata con
contenuto proprio -> 8 item di indice, 4 Obblighi e 4 Principi. Le
intestazioni 5.3 ("Validation process for Basic Signatures") e 5.4
("Time-stamp validation building block") sono pure intestazioni di
raggruppamento: non contengono nulla oltre il titolo e il rimando alle
sottoclausole, quindi NON generano nodo e non compaiono in
INDICE_ARTICOLI_LOCALE.

Scelte di modellazione non ovvie (motivate):

- 5.3.1 e 5.4.1 "Description" -> Principio "scopo/ambito di applicazione":
  le due clausole non impongono comportamenti, dichiarano soltanto quale
  processo la clausola descrive, a quali altri processi serve da blocco
  costitutivo (5.4 marche temporali, 5.5 firme con tempo) e su quali blocchi
  costitutivi si fonda (5.2); e' la stessa classificazione gia' adottata in
  questo censimento per le clausole di tipo "Description"/"Introduction"
  degli altri standard ETSI.
- 5.3.2 e 5.4.2 "Inputs" -> Obbligo "tecnico/sicurezza", destinatario
  obbligato "QTSP/gestore": le due Tabelle 18 e 19 non usano "shall", ma la
  colonna "Requirement" (Mandatory/Optional) e' vincolante e fissa i
  parametri tecnici in ingresso al processo di convalida (il solo input
  obbligatorio e' il Signed Data Object, rispettivamente il token di marca
  temporale). Stesso trattamento riservato in questo censimento alle tabelle
  di parametri/algoritmi: elenco di parametri tecnici -> Obbligo
  "tecnico/sicurezza" con obbligato il soggetto che implementa o gestisce il
  processo di convalida. Le tabelle sono contenuto della clausola che le
  contiene e sono riportate per intero in `testo_integrale`, ricostruite riga
  per riga (una riga per record) senza perdere alcun valore.
- 5.3.3 e 5.4.3 "Outputs" -> Principio "altro": dichiarano soltanto quale
  sia l'output principale del processo (un esito che indica la validita'
  della firma al tempo corrente, rispettivamente della marca temporale, con
  eventuale catena di certificati e informazioni aggiuntive) senza
  destinatario obbligato: e' la dichiarazione di un modello/risultato, non
  una prescrizione.
- 5.3.4 e 5.4.4 "Processing" -> Obbligo "procedurale": le due clausole sono
  interamente costruite su "shall" e disciplinano passi, sequenza, regole di
  processo e transizioni di stato (le sotto-indicazioni di esito), cioe' il
  criterio con cui il censimento classifica "procedurale" le clausole di
  processo. Il testo verbatim include per intero i passi 1)-7) di 5.3.4 (con
  le NOTE 1-5) e i passi 1)-3) di 5.4.4: le NOTE non sono state scorporate in
  nodi propri (una NOTA non e' una clausola numerata) ne' omesse (NOTE 1 di
  5.3.4 e NOTE 4 di 5.3.4 hanno contenuto sostanziale).
- Soggetti: il processo di convalida (SVA) dello standard ETSI EN 319 102-1
  e' implementato o erogato dal prestatore di servizi fiduciari; come nelle
  altre fonti ETSI gia' censite, il ruolo "obbligato" e' assegnato a
  "QTSP/gestore". Nessuna riga di questo capitolo individua un soggetto
  obbligato diverso, e nessuna configura un destinatario distinto (il
  testo non dice a chi vanno comunicati gli esiti: la DA e' fuori ambito,
  vedi NOTE 5 di 5.3.4), quindi il ruolo "destinatario" non e' valorizzato.
- `condizione_applicabilita` non valorizzato in nessuna riga: le condizioni
  presenti nel testo ("if the signature contains a content-time-stamp
  attribute", "if provided as input", "if the signature algorithm requires
  the full certificate chain", "if defined by the validation policy") sono
  interne alla prescrizione e restano dove il testo ufficiale le pone.
- `oggetti_giuridici` non valorizzato: il capitolo descrive il processo di
  convalida e le sue transizioni di stato in modo indipendente dallo
  strumento giuridico convalidato (firma di base, marca temporale intesa come
  firma di base); nessun aggancio univoco e non ambiguo a un solo oggetto
  giuridico.
- `severita`/`sanzioni` restano assenti (standard tecnico, nessuna sanzione);
  `stato` sempre "vigente".
- RELAZIONI: lista vuota per contratto del capitolo. I rinvii testuali
  interni (5.2.2, 5.2.3, 5.2.4, 5.2.6, 5.2.7, 5.2.8, 5.4, 5.5, 5.1.3,
  clausola 4.3.2) e i riferimenti esterni (IETF RFC 3161, ETSI EN 319 422)
  sono lasciati alla sessione principale (ADR-0009).

Convenzioni di trascrizione di `testo_integrale` (nessuna parola rimossa; il
testo e' stato confrontato riga per riga con cap05.txt):
- i wrap fisici di riga introdotti da pdftotext -layout sono ricomposti in
  paragrafi, uno per capoverso/voce di elenco, separati da riga vuota;
- i marcatori di pagina (riga "ETSI" + numero pagina + intestazione del
  documento, righe 46-47 e 118-119 del sorgente) sono rimossi;
- le intestazioni dei titoli di clausola ripetuti nel sorgente NON sono
  duplicate: ciascun titolo di clausola e' implicito nel proprio
  `riferimento` e il testo della clausola comincia dal suo primo capoverso;
- le due tabelle (Table 18, Table 19) sono ricostruite riga per riga con
  separatore "|": tutte le celle del sorgente sono integre (nessuna cella
  tagliata dalla conversione), non c'e' stato bisogno di ricostruirne
  nessuna dal contesto.

Self-check eseguito dalla radice del repo (vedi rapporto finale): 4 obblighi,
4 principi, 8 item di indice, copertura e completezza di `testo_integrale`
verificate con `seed_data.lib`.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 5.3.2 (Inputs)",
        "testo": (
            "Input del processo di convalida di una firma di base (Tabella 18). Il solo input "
            "obbligatorio (Mandatory) e' il Signed Data Object; sono opzionali (Optional) il Signer's "
            "Document o l'SDR (Signed Data Object Representation), il Signing Certificate, la Trust anchor "
            "list (es. TSL), le Signature Validation Policies, la Local configuration e i Certificate "
            "Validation Data."
        ),
        "testo_integrale": (
            """Table 18: Inputs to Basic Validation

| Input | Requirement |
|---|---|
| Signed Data Object | Mandatory |
| Signer's Document or SDR | Optional |
| Signing Certificate | Optional |
| Trust anchor list (e.g. TSL) | Optional |
| Signature Validation Policies | Optional |
| Local configuration | Optional |
| Certificate Validation Data | Optional |"""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.3.4 (Processing)",
        "testo": (
            "Elaborazione del processo di convalida di una firma di base. L'ordine dei passi non e' "
            "vincolante: essendo l'elaborazione largamente dipendente dall'implementazione, e' ammesso "
            "qualunque ordine che produca gli stessi risultati, anche l'elaborazione in parallelo. Passi: "
            "1) format checking come da clausola 5.2.2 - se il processo restituisce PASSED si prosegue, "
            "altrimenti si restituisce l'indicazione FAILED con la sotto-indicazione FORMAT_FAILURE; "
            "2) identificazione del certificato di firma (clausola 5.2.3) con la firma e il certificato di "
            "firma se fornito come parametro - se tale processo restituisce INDETERMINATE con la "
            "sotto-indicazione NO_SIGNING_CERTIFICATE_FOUND si restituisce INDETERMINATE con la stessa "
            "sotto-indicazione, altrimenti si prosegue; 3) Validation Context Initialization come da "
            "clausola 5.2.4 - se il processo restituisce INDETERMINATE con una sotto-indicazione si "
            "restituisce INDETERMINATE con quella sotto-indicazione, altrimenti si prosegue; 4) X.509 "
            "Certificate Validation come da clausola 5.2.6 con input il certificato di firma ottenuto al "
            "passo 2) e i vincoli di convalida X.509, i certificate validation-data e i vincoli "
            "crittografici ottenuti al passo 3) o forniti in input - se restituisce PASSED imposta la "
            "variabile interna X509_validation-status a PASSED e passa al passo 5); se restituisce "
            "INDETERMINATE/REVOKED_NO_POE e la firma contiene un attributo content-time-stamp esegue la "
            "convalida della marca temporale AdES (clausola 5.4) e imposta X509_validation-status a "
            "FAILED/REVOKED se la marca temporale e' PASSED e il suo tempo di generazione e' successivo al "
            "tempo di revoca, altrimenti a INDETERMINATE/REVOKED_NO_POE; se restituisce "
            "INDETERMINATE/OUT_OF_BOUNDS_NO_POE o OUT_OF_BOUNDS_NOT_REVOKED e la firma contiene un "
            "attributo content-time-stamp esegue la convalida della marca temporale AdES (clausola 5.4) e "
            "imposta X509_validation-status a FAILED/EXPIRED se la marca temporale e' PASSED e il suo "
            "tempo di generazione e' successivo alla data di scadenza del certificato di firma, altrimenti "
            "a INDETERMINATE con la sotto-indicazione OUT_OF_BOUNDS_NO_POE o OUT_OF_BOUNDS_NOT_REVOKED, "
            "rispettivamente; se restituisce INDETERMINATE/NO_CERTIFICATE_CHAIN_FOUND e l'algoritmo di "
            "firma richiede la catena completa dei certificati per determinare la chiave pubblica "
            "restituisce INDETERMINATE/NO_CERTIFICATE_CHAIN_FOUND; in tutti gli altri casi copia in "
            "X509_validation-status l'indicazione e la sotto-indicazione restituite dalla convalida X.509 "
            "e continua dal passo 5); 5) Cryptographic Verification come da clausola 5.2.7 con input il "
            "Signed Data Object, il certificato di firma del passo 2), la catena di certificati del passo "
            "4) se restituita e l'SD o l'SDR se dato in input - se restituisce PASSED e "
            "X509_validation-status contiene PASSED si prosegue, se X509_validation-status contiene "
            "INDETERMINATE o FAILED con qualunque sotto-indicazione si restituiscono l'indicazione e la "
            "sotto-indicazione contenute in X509_validation-status con le informazioni associate sulla "
            "ragione, altrimenti si restituiscono l'indicazione, la sotto-indicazione e le informazioni "
            "associate fornite dalla verifica crittografica; 6) Signature Acceptance Validation (SAV) come "
            "da clausola 5.2.8 con input il o i Signed Data Object, la catena di certificati ottenuta al "
            "passo 4), i Cryptographic Constraints e i Signature Elements Constraints - se restituisce "
            "PASSED si prosegue; se restituisce INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE e il "
            "materiale interessato dal guasto e' il valore di firma e la firma contiene un attributo "
            "content-time-stamp, esegue la convalida della marca temporale AdES (clausola 5.4) e "
            "restituisce INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE se la marca temporale e' PASSED e gli "
            "algoritmi interessati non erano piu' considerati affidabili al tempo di generazione della "
            "marca temporale, altrimenti in tutti i casi INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE "
            "(in quest'ultimo caso, se esistono altri POE, per esempio da un archivio fidato, si puo' "
            "usare il processo di convalida per le firme che forniscono disponibilita' e integrita' a "
            "lungo termine del materiale di convalida); in tutti gli altri casi restituisce l'indicazione "
            "e le informazioni associate restituite dal blocco SAV; 7) restituzione dell'indicazione di "
            "successo PASSED insieme alla catena di certificati ottenuta al passo 4) e, in aggiunta, delle "
            "informazioni estratte dalla firma e/o usate dai passi intermedi - in particolare la SVA "
            "dovrebbe fornire alla DA tutte le informazioni relative agli attributi firmati e non firmati, "
            "incluse quelle non elaborate durante il processo di convalida (cio' che la DA fa di queste "
            "informazioni e' fuori dall'ambito del documento)."
        ),
        "testo_integrale": (
            """NOTE 1: Since processing is largely implementation dependent, the steps listed in this clause are not necessarily to be processed exactly in the given order. Any ordering that produces the same results can be used, even parallel processing is possible.

1) The Basic Signature validation process shall perform the format checking as per clause 5.2.2. If the process returns PASSED, the Basic Signature validation process shall continue with the next step. Otherwise, the Basic Signature validation process shall return the indication FAILED with the sub-indication FORMAT_FAILURE.

2) The Basic Signature validation process shall perform the identification of the signing certificate (as per clause 5.2.3) with the signature and the signing certificate, if provided as a parameter. If the identification of the signing certificate process returns the indication INDETERMINATE with the sub-indication NO_SIGNING_CERTIFICATE_FOUND, the Basic Signature validation process shall return the indication INDETERMINATE with the sub-indication NO_SIGNING_CERTIFICATE_FOUND, otherwise it shall go to the next step.

3) The Basic Signature validation process shall perform the Validation Context Initialization as per clause 5.2.4. If the process returns INDETERMINATE with some sub-indication, the Basic Signature validation process shall return the indication INDETERMINATE together with that sub-indication, otherwise it shall go to the next step.

4) The Basic Signature validation process shall perform the X.509 Certificate Validation as per clause 5.2.6 with the following inputs:

a) The signing certificate obtained in step 2); and

b) X.509 validation constraints, certificate validation-data and cryptographic constraints obtained in step 3) or provided as input.

If the X.509 Certificate Validation process returns the indication PASSED, the Basic Signature validation process shall set X509_validation-status to PASSED and it shall go to step 5).

NOTE 2: X509_validation-status is an internal variable. This is done because the cryptographic validation has not been performed yet. Other building blocks assume that when this building block returns an INDETERMINATE status with a sub-indication related to X.509 certificate validation, cryptographic validation has been performed successfully. Cryptographic validation can, in some cases, only be performed after X.509 validation.

If the X.509 Certificate Validation process returns the indication INDETERMINATE with the sub-indication REVOKED_NO_POE and if the signature contains a content-time-stamp attribute, the Basic Signature validation process shall perform the validation process for AdES time-stamps as defined in clause 5.4. If this process returns the indication PASSED and the generation time of the time-stamp token is after the revocation time, the Basic Signature validation process shall set X509_validation-status to FAILED with the sub-indication REVOKED. In all other cases, the Basic Signature validation process shall set X509_validation-status to INDETERMINATE with the sub-indication REVOKED_NO_POE. The process shall continue with step 5).

If the X.509 Certificate Validation process returns the indication INDETERMINATE with the sub-indication OUT_OF_BOUNDS_NO_POE or OUT_OF_BOUNDS_NOT_REVOKED, and if the signature contains a content-time-stamp attribute, the Basic Signature validation process shall perform the validation process for AdES time-stamps as defined in clause 5.4. If it returns the indication PASSED and the generation time of the time-stamp token is after the expiration date of the signing certificate, the Basic Signature validation process shall set X509_validation-status to FAILED with the sub-indication EXPIRED. Otherwise, the Basic Signature validation process shall set X509_validation-status to INDETERMINATE with the sub-indication OUT_OF_BOUNDS_NO_POE or OUT_OF_BOUNDS_NOT_REVOKED, respectively. The process shall continue with step 5).

If the X.509 Certificate Validation process returns the indication INDETERMINATE with the sub-indication NO_CERTIFICATE_CHAIN_FOUND and if the signature algorithm requires the full certificate chain for determining the public key, the Basic Signature validation process shall return the indication INDETERMINATE with the sub-indication NO_CERTIFICATE_CHAIN_FOUND.

In all other cases, the Basic Signature validation process shall set X509_validation-status to the indication and sub-indication returned by the X.509 Certificate Validation process and continue with step 5).

5) The Basic Signature validation process shall perform the Cryptographic Verification process as per clause 5.2.7 with the following inputs:

a) the Signed Data Object;

b) the signing certificate obtained in step 2);

c) the certificate chain returned in the previous step, if it was returned in step 4); and

d) the SD or SDR, if given in the input.

If the Cryptographic Verification process returns PASSED:

e) if the X509_validation-status set in the previous step contains the indication PASSED, the Basic Signature validation process shall go to the next step;

f) if the X509_validation-status set in the previous step contains the indication INDETERMINATE or FAILED with any subindication, the Basic Signature validation process shall return the indication and subindication contained in X509_validation-status, with any associated information about the reason.

Otherwise, the Basic Signature validation process shall return the returned indication, sub-indication and associated information provided by the Cryptographic Verification process.

6) The Basic Signature validation process shall perform the Signature Acceptance Validation (SAV) process as per clause 5.2.8 with the following inputs:

a) the Signed Data Object(s);

b) the certificate chain obtained in step 4);

c) the Cryptographic Constraints; and

d) the Signature Elements Constraints.

If the Signature Acceptance Validation process returns PASSED, the Basic Signature validation process shall go to the next step.

If the Signature Acceptance Validation process returns the indication INDETERMINATE with the sub-indication CRYPTO_CONSTRAINTS_FAILURE_NO_POE and the material concerned by this failure is the signature value and if the signature contains a content-time-stamp attribute, the Basic Signature validation process shall perform the validation process for AdES time-stamps as defined in clause 5.4. If it returns the indication PASSED and the algorithm(s) concerned were no longer considered reliable at the generation time of the time-stamp token, the Basic Signature validation process shall return the indication INDETERMINATE with the sub-indication CRYPTO_CONSTRAINTS_FAILURE. In all other cases, the Basic Signature validation process shall return the indication INDETERMINATE with the sub-indication CRYPTO_CONSTRAINTS_FAILURE_NO_POE.

NOTE 3: The content time-stamp is a signed attribute and hence proves that the signature value was produced after the generation time of the time-stamp token.

NOTE 4: In case this clause returns INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE, the validation process for Signatures providing Long Term Availability and Integrity of Validation Material can be used to validate the signature, if other POE (e.g. from a trusted archive) exist.

In all other cases, the Basic Signature validation process shall return the indication and associated information returned by the Signature Acceptance Validation building block.

7) The Basic Signature validation process shall return the success indication PASSED together with the certificate chain obtained in step 4). In addition, the Basic Signature validation process should return additional information extracted from the signature and/or used by the intermediate steps. In particular, the SVA should provide to the DA all information related to signed and unsigned attributes, including those which were not processed during the validation process.

NOTE 5: What the DA does with this information is out of the scope of the present document."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.4.2 (Inputs)",
        "testo": (
            "Input del blocco costitutivo di convalida della marca temporale (Tabella 19). Il solo input "
            "obbligatorio (Mandatory) e' il Time-stamp token; sono opzionali (Optional) la Trust anchor "
            "list (es. TSL), le Signature Validation Policies, la Local configuration e il Time-Stamp "
            "Certificate."
        ),
        "testo_integrale": (
            """Table 19: Inputs to time-stamp validation

| Input | Requirement |
|---|---|
| Time-stamp token | Mandatory |
| Trust anchor list (e.g. TSL) | Optional |
| Signature Validation Policies | Optional |
| Local configuration | Optional |
| Time-Stamp Certificate | Optional |"""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.4.4 (Processing)",
        "testo": (
            "Elaborazione del blocco costitutivo di convalida della marca temporale. 1) Convalida della "
            "firma del token: il blocco esegue il processo di convalida delle firme di base come da "
            "clausola 5.3 con input il token di marca temporale come Signed Data Object, una trust anchor "
            "list applicabile alla convalida delle marche temporali secondo la politica di convalida, una "
            "politica di convalida applicabile alla convalida delle marche temporali se definita dalla "
            "politica di convalida, e il certificato di marca temporale come certificato di firma se "
            "fornito in input. 2) Se il passo 1) restituisce PASSED il blocco prosegue, altrimenti "
            "restituisce l'indicazione e le informazioni restituite dal processo di convalida. 3) "
            "Estrazione dei dati: oltre agli elementi dati restituiti al passo 1), il blocco restituisce il "
            "tempo di generazione e il message imprint presenti nel campo TSTInfo del token di marca "
            "temporale, e puo' restituire altri elementi dati presenti nello stesso campo TSTInfo; questi "
            "elementi possono essere usati dagli altri blocchi costitutivi nel processo di convalida della "
            "firma AdES."
        ),
        "testo_integrale": (
            """1) Token signature validation: the building block shall perform the validation process for Basic Signatures as per clause 5.3 with the following inputs:

- the time-stamp token as the Signed Data Object;

- a trust anchor list applicable for validating time-stamps according to the validation policy;

- a validation policy applicable for validating time-stamps if defined by the validation policy; and

- the time-stamp certificate as the signing-certificate, if provided as input.

2) If step 1) returns PASSED, the building block shall go to the next step. Otherwise, the building block shall return the indication and information returned by the validation process.

3) Data extraction: in addition to the data items returned in step 1), the building block:

- shall return the generation time and the message imprint present in the TSTInfo field of the time-stamp token; and

- may return other data items present in the TSTInfo field of the time-stamp token.

These items may be used by the other building blocks in the process of validating the AdES signature."""
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 5.3.1 (Description)",
        "testo": (
            "La clausola descrive un processo di convalida per validare le firme di base (Basic "
            "Signatures) come da clausola 4.3.2. Il processo stesso e' usato anche come blocco "
            "costitutivo dal processo di convalida delle marche temporali (clausola 5.4) e delle firme "
            "con tempo (clausola 5.5). Il processo si fonda sui blocchi costitutivi descritti nella "
            "clausola 5.2."
        ),
        "testo_integrale": (
            "This clause describes a validation process for validating Basic Signatures as per clause "
            "4.3.2. This process itself is also used as a building block by the validation process of "
            "time-stamps (see clause 5.4) and of Signatures with Time (see clause 5.5). The process "
            "builds on the building blocks described in clause 5.2."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.3.3 (Outputs)",
        "testo": (
            "Output principale della convalida della firma: un esito (status) che indica la validita' "
            "della firma al tempo corrente e, se applicabile, la catena di certificati usata nel processo "
            "di convalida. Questo esito puo' essere accompagnato da informazioni aggiuntive (clausola "
            "5.1.3)."
        ),
        "testo_integrale": (
            "The main output of the signature validation is a status indicating the validity of the "
            "signature at current time and the certificate chain used in the validation process, if "
            "applicable. This status may be accompanied by additional information (see clause 5.1.3)."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.4.1 (Description)",
        "testo": (
            "La clausola descrive un blocco costitutivo per la convalida di un token di marca temporale "
            "IETF RFC 3161 [3] o ETSI EN 319 422 [i.13]. Un token di marca temporale IETF RFC 3161 o "
            "ETSI EN 319 422 e' una firma di base: il processo di convalida si fonda quindi sul processo "
            "di convalida di una firma di base."
        ),
        "testo_integrale": (
            """This clause describes a building block for the validation of an IETF RFC 3161 [3] or ETSI EN 319 422 [i.13] time-stamp token.

An IETF RFC 3161 [3] or ETSI EN 319 422 [i.13] time-stamp token is a Basic Signature. Hence, the validation process builds on the validation process of a Basic Signature."""
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.4.3 (Outputs)",
        "testo": (
            "Output principale della convalida della marca temporale: un esito (status) che indica la "
            "validita' della marca temporale. Questo esito puo' essere accompagnato da informazioni "
            "aggiuntive (clausola 5.1.3)."
        ),
        "testo_integrale": (
            "The main output of the time-stamp validation is a status indicating the validity of the "
            "time-stamp. This status may be accompanied by additional information (see clause 5.1.3)."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 5.3.1 (Description)",
    "clausola 5.3.2 (Inputs)",
    "clausola 5.3.3 (Outputs)",
    "clausola 5.3.4 (Processing)",
    "clausola 5.4.1 (Description)",
    "clausola 5.4.2 (Inputs)",
    "clausola 5.4.3 (Outputs)",
    "clausola 5.4.4 (Processing)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
