"""ETSI EN 319 102-1 V1.4.1 (2024-06) — Electronic Signatures and
Infrastructures (ESI); Procedures for Creation and Validation of AdES Digital
Signatures; Part 1: Creation and Validation. Capitolo 4: clausola 5.2 "Basic
building blocks" (sottoclawse 5.2.1-5.2.9). Testo ufficiale in
app/.source_cache/etsi_319_102/cap04.txt; manifest di split in
app/.source_cache/etsi_319_102/manifest.json. Il file non importa nulla: id e
relazioni sono risolti per riferimento dalla sessione principale tramite
app/seed_data/lib.py (questo modulo NON tocca app/seed.py).

Perimetro coperto (36 item di indice, 30 Obblighi + 6 Principi):
- 5.2.1 (Description) -> Principio "altro"
- 5.2.2.1 (Description) -> Obbligo; 5.2.2.2 (Inputs) -> Obbligo; 5.2.2.3
  (Outputs) -> Obbligo
- 5.2.3.1 (Description) -> Principio; 5.2.3.2 (Inputs) -> Obbligo; 5.2.3.3
  (Outputs) -> Obbligo; 5.2.3.4 (Processing) -> Obbligo
- 5.2.4.1 (Description) -> Principio; 5.2.4.2 (Inputs) -> Obbligo; 5.2.4.3
  (Outputs) -> Obbligo; 5.2.4.4 (Processing) -> Obbligo
- 5.2.5.1 (Description) -> Principio; 5.2.5.2 (Inputs) -> Obbligo; 5.2.5.3
  (Output) -> Obbligo; 5.2.5.4 (Processing) -> Obbligo
- 5.2.6.1 (Description) -> Obbligo; 5.2.6.2 (Inputs) -> Obbligo; 5.2.6.3
  (Outputs) -> Obbligo; 5.2.6.4 (Processing) -> Obbligo
- 5.2.7.1 (Description) -> Principio; 5.2.7.2 (Inputs) -> Obbligo; 5.2.7.3
  (Outputs) -> Obbligo; 5.2.7.4 (Processing) -> Obbligo
- 5.2.8.1 (Description) -> Principio; 5.2.8.2 (Inputs) -> Obbligo; 5.2.8.3
  (Outputs) -> Obbligo; 5.2.8.4.1 (General requirements) -> Obbligo;
  5.2.8.4.2.1 - 5.2.8.4.2.7 (Processing ...) -> Obbligo ciascuna
- 5.2.9 (Signature validation presentation building block) -> Obbligo

Scelte di modellazione non ovvie:
- Intestazioni di puro raggruppamento, senza alcun periodo proprio oltre al
  titolo e ai riferimenti alle sottoclawse, NON generano nodo ne' item di
  indice: 5.2 (Basic building blocks), 5.2.2 (Format Checking), 5.2.3
  (Identification of the signing certificate), 5.2.4 (Validation context
  initialization), 5.2.5 (Revocation freshness checker), 5.2.6 (X.509
  certificate validation), 5.2.7 (Cryptographic verification), 5.2.8
  (Signature Acceptance Validation (SAV)), 5.2.8.4 (Processing) e 5.2.8.4.2
  (Processing AdES attributes). Stesso trattamento riservato ai titoli di
  raggruppamento delle altre fonti ETSI gia' censite.
- Clausole con tabella a colonna "Requirement" (valori Mandatory/Optional) ->
  Obbligo "tecnico/sicurezza", anche in assenza di un "shall" esplicito:
  regola Fonte-wide adottata dalla sessione principale dopo revisione di questo
  capitolo, per coerenza con i capitoli delle clausole 5.3-5.4 della stessa
  fonte (che censivano come Obbligo le stesse tabelle) e per superare
  l'incongruenza con i capitoli che le censivano come Principio. Riguarda le
  sette clausole "Inputs" di questa porzione - 5.2.2.2, 5.2.3.2, 5.2.4.2,
  5.2.5.2, 5.2.6.2, 5.2.7.2, 5.2.8.2 (Tabelle 8, 9, 10, 11A, 12, 14 e 16): le
  righe corrispondenti sono state spostate in RIGHE_OBBLIGHI con `testo` e
  `testo_integrale` invariati, perche' la prescrizione e' sul processo (quali
  ingressi sono obbligatori e quali facoltativi) e il destinatario e' chi
  implementa il processo di convalida (QTSP/gestore). Prima di questa revisione
  erano Principi "altro", sul criterio del verbo modale assente.
- Nessuna tabella "Outputs"/"Output" della porzione porta la colonna
  "Requirement" (Tabelle 11, 11B, 13, 15 e 17 contengono solo indicazioni,
  sotto-indicazioni, descrizioni e informazioni aggiuntive): quelle clausole
  restano Obblighi per via dell'enunciato prescrittivo esplicito che le
  introduce ("the output shall be ...", "The process shall output ..."), e le
  tabelle di indicazioni/sotto-indicazioni restano per intero nel loro
  `testo_integrale`. Restano Principi le sole clausole dichiarative o di
  interfaccia prive di quella colonna: 5.2.1, 5.2.3.1, 5.2.4.1, 5.2.5.1,
  5.2.7.1 e 5.2.8.1 (tutte "Description").
- Clausola 5.2.6.1 (Description) -> Obbligo: a differenza delle altre
  "Description" della porzione, contiene una prescrizione in senso proprio
  ("If the validation time is not provided as an input, the validation shall
  be performed at current time").
- Clausola 5.2.8.1 (Description) -> Principio: la NOTE finale dichiara
  esplicitamente che i controlli "are not mandatory to be implemented by an
  SVA", quindi la clausola non impone un comportamento.
- Clausola 5.2.9 -> Obbligo "informativo/trasparenza": e' un elenco di
  requisiti di presentazione ("should support:") in capo a chi realizza il
  blocco di presentazione della convalida; il contenuto e' resa di
  informazioni al verificatore (dati firmati, firmatario, data/ora dello
  stato, attributi firmati e non firmati, politica usata, stato complessivo,
  motivo dell'invalidita', parti del rapporto da evidenziare, rapporto di
  convalida), non un controllo tecnico-crittografico. Destinatario della
  presentazione e' un verificatore, censito come "Terzi affidanti/pubblico".
- Ricostruzione delle tabelle: una riga per record, celle separate da " | ",
  con la riga di intestazione come compare nel testo. Nella Tabella 15
  (output della verifica crittografica) e nella Tabella 17 (output dell'SAV)
  la colonna delle sotto-indicazioni non ha intestazione propria: indicazione
  e sotto-indicazione sono state unite con " / " (es. "FAILED /
  HASH_FAILURE"), per non inventare un'intestazione assente. Nella Tabella 13
  la cella "Additional Information" della riga PASSED e' spezzata dalla
  conversione su due righe non allineate ("The certificate chain used in the
  successful validation." e "Any additional validation data acquired"): e'
  stata riportata come unica cella della riga PASSED, senza perdere alcun
  valore.
- Refusi del testo ufficiale conservati perche' verbatim: "SIG_CONTRAINTS_
  FAILURE" (in 5.2.8.4.2.1, dove altrove lo standard usa
  SIG_CONSTRAINTS_FAILURE), "for which the the X.509 Validation Constraints
  explicitly state" (5.2.6.4) e "Signer's Document or Signer's Document
  Representation" (Tabella 14, riga d'ingresso).
- `condizione_applicabilita` valorizzata solo per le sei sottoclawse
  5.2.8.4.2.2 - 5.2.8.4.2.7, il cui enunciato e' esplicitamente condizionato
  al contenuto dei signature elements constraints; nessun'altra clausola
  della porzione porta una condizione di applicabilita' propria.
- Soggetti: obbligato sempre "QTSP/gestore" (chi implementa il processo di
  convalida / l'SVA / il blocco); "Terzi affidanti/pubblico" come
  destinatario solo in 5.2.9. La "DA" (Designated Authority) citata nelle
  procedure non e' mappata su una categoria soggetto: e' il richiedente della
  convalida, non un soggetto censito distinto da chi implementa il processo.
  `severita`/`sanzioni` assenti (standard tecnico, nessuna sanzione); `stato`
  sempre "vigente".
- RELAZIONI vuota: nessun collegamento tentato, nemmeno verso le clausole
  interne del documento citate dalle procedure (5.1.4, 5.2.5, 5.2.7, 5.2.8,
  5.4, Annesso C) ne' verso eIDAS o gli altri standard ETSI richiamati: i
  nodi di destinazione appartengono ad altri capitoli della stessa fonte o ad
  altre fonti e il collegamento e' costruito dalla sessione principale.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 5.2.2.1 (Description)",
        "testo": (
            "Il controllo di formato deve verificare che la firma da convalidare sia conforme al formato di base "
            "applicabile almeno nella misura in cui il suo contenuto interno sia processabile dal blocco di verifica "
            "crittografica (clausola 5.2.7). Nota: il controllo non include la conformita' a uno specifico profilo o "
            "livello di firma (es. XAdES-E-XL o PAdES-B-LTA); tale verifica, se richiesta dalla politica di convalida "
            "della firma, puo' essere inclusa nel blocco Signature Acceptance Validation come specificato nella "
            "clausola 5.2.8 (vedi Annesso C)."
        ),
        "testo_integrale": """This building block shall check that the signature to validate is conformant to the applicable base format to the extent that its inner contents would at least allow to be processed by the cryptographic verification building block (see clause 5.2.7).

NOTE: This checking process does not include any checks on conformance to a specific signature profile or a specific level of signature, like XAdES-E-XL or PAdES-B-LTA. Such checking, if required by the signature validation policy, can be included in the Signature Acceptance Validation building block as specified in clause 5.2.8. See Annex C for details.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.2.2 (Inputs)",
        "testo": (
            "Ingressi del blocco di controllo di formato (Tabella 8, Input | Requirement): Signed Data Object | "
            "Mandatory."
        ),
        "testo_integrale": """Table 8: Inputs to the format checking building block
Input | Requirement
Signed Data Object | Mandatory""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.2.3 (Outputs)",
        "testo": (
            "Se la firma e' conforme al formato di base applicabile, l'uscita deve essere l'indicazione PASSED; se la "
            "firma non e' conforme, l'uscita deve essere FAILED."
        ),
        "testo_integrale": """In case the signature is conformant to the applicable base format, the output shall be the indication PASSED. If the signature is not conformant, the output shall be FAILED.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.3.2 (Inputs)",
        "testo": (
            "Ingressi del blocco di identificazione del certificato di firma (Tabella 9, Input | Requirement): "
            "Signature | Mandatory; Signing Certificate | Optional."
        ),
        "testo_integrale": """Table 9: Inputs to the identification of the signing certificate building block
Input | Requirement
Signature | Mandatory
Signing Certificate | Optional""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.3.3 (Outputs)",
        "testo": (
            "In caso di successo l'uscita deve essere il certificato di firma; se il certificato di firma non e' "
            "identificabile, l'uscita deve essere l'indicazione INDETERMINATE con la sotto-indicazione "
            "NO_SIGNING_CERTIFICATE_FOUND. Nota: il processo puo' restituire INDETERMINATE solo se il certificato non "
            "e' contenuto nella firma e non puo' essere recuperato da una risorsa esterna puntata dal riferimento "
            "della firma."
        ),
        "testo_integrale": """• In case of success, the output shall be the signing certificate.

• In case the signing certificate cannot be identified, the output shall be the indication INDETERMINATE and the sub-indication NO_SIGNING_CERTIFICATE_FOUND.

NOTE: The process can only return INDETERMINATE in case the certificate is not contained in the signature and cannot be retrieved from an external resource pointed to by the signature reference.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.3.4 (Processing)",
        "testo": (
            "Il modo comune per identificare in modo univoco il certificato di firma e' usare una proprieta'/attributo "
            "della firma che lo referenzia (clausola 4.2.5.2); il certificato puo' trovarsi nella firma, essere "
            "ottenuto da fonti esterne o essere fornito dal DA. Se nessun certificato e' recuperabile, il blocco deve "
            "restituire l'indicazione INDETERMINATE con la sotto-indicazione NO_SIGNING_CERTIFICATE_FOUND. Se nella "
            "firma sono presenti attributi identificativi del certificato di firma, il certificato di firma deve "
            "essere confrontato con tutti i riferimenti presenti negli attributi identificativi firmati (uno di essi "
            "e' il riferimento al certificato di firma): 1) se il formato di firma usato consente di identificare "
            "direttamente il riferimento al certificato del firmatario nell'attributo, il blocco deve verificare che "
            "il digest del certificato referenziato corrisponda al digest del certificato di firma calcolato con "
            "l'algoritmo indicato; se corrispondono restituisce il certificato di firma, altrimenti passa al passo 2); "
            "2) il blocco deve prendere il primo riferimento e verificare che il digest del certificato referenziato "
            "corrisponda al digest del certificato di firma con l'algoritmo indicato; se non corrispondono passa "
            "all'elemento successivo ripetendo il passo finche' trova una corrispondenza o ha controllato tutti gli "
            "elementi; se corrispondono continua al passo 3); se si esauriscono gli elementi senza alcuna "
            "corrispondenza, la convalida di quella proprieta' e' considerata fallita e il blocco deve restituire "
            "INDETERMINATE con NO_SIGNING_CERTIFICATE_FOUND; 3) se nel riferimento sono presenti anche issuer e "
            "serial number, i dettagli del nome dell'issuer e il serial number dell'elemento IssuerSerial possono "
            "essere confrontati con quelli del certificato di firma e, se non corrispondono, deve essere restituito "
            "un warning aggiuntivo con l'uscita; 4) il blocco deve restituire il certificato di firma. Se non sono "
            "presenti attributi identificativi del certificato di firma, il blocco deve verificare se la firma "
            "contiene una copia firmata del certificato di firma e, in tal caso, restituire quella copia firmata. "
            "Note: una firma di base contiene un riferimento a o una copia del certificato di firma come attributo "
            "firmato, la cui posizione e' specifica del formato (clausola 4.3.2.3); il processo puo' avere successo "
            "anche se la firma non contiene tale riferimento o copia come attributo firmato."
        ),
        "testo_integrale": """The common way to unambiguously identify the signing certificate is by using a property/attribute of the signature containing a reference to it (see clause 4.2.5.2). The certificate can either be found in the signature or it can be obtained using external sources. The signing certificate can also be provided by the DA. If no certificate can be retrieved, the building block shall return the indication INDETERMINATE and the sub-indication NO_SIGNING_CERTIFICATE_FOUND.

When signing certificate identifier attributes are present in the signature, the signing certificate shall be checked against all references present in signed signing certificate identifier attributes, since one of these references is a reference to the signing certificate (see clause 4.2.5.2). The following steps are performed:

1) If the signature format used contains a way to directly identify the reference to the signers' certificate in the attribute, the building block shall check that the digest of the certificate referenced matches the result of digesting the signing certificate with the algorithm indicated; if they match, the building block shall return the signing certificate. Otherwise, the building block shall go to step 2).

2) The building block shall take the first reference and shall check that the digest of the certificate referenced matches the result of digesting the signing certificate with the algorithm indicated. If they do not match, the building block shall take the next element and shall repeat this step until a matching element has been found or all elements have been checked. If they do match, the building block shall continue with step 3). If the last element is reached without finding any match, the validation of this property shall be taken as failed and the building block shall return the indication INDETERMINATE with the sub-indication NO_SIGNING_CERTIFICATE_FOUND.

3) If the issuer and the serial number are additionally present in that reference, the details of the issuer's name and the serial number of the IssuerSerial element may be compared with those indicated in the signing certificate: if they do not match, an additional warning shall be returned with the output.

4) The building block shall return the signing certificate.

When no signing certificate identifier attributes are present in the signature, the building block shall check whether the signature contains a signed copy of the signing certificate and if the signature contains a signed copy of the signing certificate, the building block shall return the signed copy of the signing certificate.

NOTE 1: As specified in clause 4.3.2.3, a basic signature contains a reference to or a copy of the signing certificate as a signed attribute. The location of this signed attribute in a signature is format specific.

NOTE 2: This process can succeed even when the signature does not contain a reference to or a copy of the signing certificate as a signed attribute. Implementers that want to ensure that a signature meets this requirement can do so through either enforcing the presence of specific signed attributes in the signature elements constraints (see clause 5.1.4.4) that will be checked in the signature acceptance validation building block (see clause 5.2.8), or through a signature conformance checker mandating the compliance to specific AdES signature profiles as illustrated in Annex C.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.4.2 (Inputs)",
        "testo": (
            "Ingressi del blocco di inizializzazione del contesto di convalida (Tabella 10, Input | Requirement): "
            "Signature | Mandatory; Signature Validation Policies | Optional; Trust anchor list (e.g. TSL) | "
            "Optional; Local configuration | Optional."
        ),
        "testo_integrale": """Table 10: Inputs to the validation context initialization building block
Input | Requirement
Signature | Mandatory
Signature Validation Policies | Optional
Trust anchor list (e.g. TSL) | Optional
Local configuration | Optional""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.4.3 (Outputs)",
        "testo": (
            "In caso di fallimento il blocco deve produrre lo stato INDETERMINATE insieme a una sotto-indicazione "
            "definita nella Tabella 11; altrimenti deve produrre lo stato PASSED insieme agli insiemi di vincoli da "
            "usare nella convalida successiva, sempre secondo la Tabella 11. Tabella 11 (Indication | Additional "
            "Information/Sub-indication): PASSED | X.509 Validation Parameters; PASSED | Certificate Validation Data; "
            "PASSED | X.509 Validation Constraints; PASSED | Cryptographic Constraints; PASSED | Signature Elements "
            "Constraints; INDETERMINATE | POLICY_PROCESSING_ERROR; INDETERMINATE | SIGNATURE_POLICY_NOT_AVAILABLE."
        ),
        "testo_integrale": """In case of failure, the building block shall output a status indication INDETERMINATE together with a sub-indication as defined in Table 11. Otherwise, the building block shall output the status indication PASSED together with the sets of constraints that shall be used in further validation as defined in Table 11.

Table 11: Output of the Validation context initialization building block
Indication | Additional Information/Sub-indication
PASSED | X.509 Validation Parameters
PASSED | Certificate Validation Data
PASSED | X.509 Validation Constraints
PASSED | Cryptographic Constraints
PASSED | Signature Elements Constraints
INDETERMINATE | POLICY_PROCESSING_ERROR
INDETERMINATE | SIGNATURE_POLICY_NOT_AVAILABLE""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.4.4 (Processing)",
        "testo": (
            "Se il DA fornisce all'SVA una politica di convalida della firma da usare, il blocco deve selezionare i "
            "vincoli di convalida imposti da quella politica. Se il DA fornisce una mappatura tra politiche di "
            "creazione della firma accettabili e le corrispondenti politiche di convalida, il blocco deve determinare "
            "se la firma da convalidare contiene riferimenti a, o l'identificatore di, una di queste politiche di "
            "creazione nell'attributo di politica di firma. Se nessuna politica di creazione e' contenuta nella firma, "
            "il blocco dovrebbe selezionare una politica di convalida di default (che puo' essere fornita dal DA, "
            "dalla configurazione o stabilita secondo i requisiti tecnici minimi e i requisiti minimi di legge). Se la "
            "firma contiene un identificatore di politica di creazione presente nella lista delle mappature, l'SVA "
            "deve applicare la corrispondente politica di convalida durante la convalida. Se l'identificatore non e' "
            "nella lista delle mappature, e' una decisione di policy (configurazione locale) se si applichino le "
            "regole di default o se il processo di convalida debba essere terminato. Il blocco deve accedere al "
            "documento elettronico identificato dal contenuto della proprieta'/attributo contenente i dettagli della "
            "politica: se non e' disponibile, deve restituire INDETERMINATE con SIGNATURE_POLICY_NOT_AVAILABLE; se "
            "non puo' essere analizzato o processato per qualunque altro motivo, deve restituire INDETERMINATE con "
            "POLICY_PROCESSING_ERROR. Il blocco deve estrarre i vincoli di convalida dalle regole codificate nella "
            "politica e restituire PASSED insieme ai vincoli estratti."
        ),
        "testo_integrale": """If the DA provides the SVA with a signature validation policy to be used, the building block shall select the validation constraints mandated by that signature validation policy.

If the DA provides the SVA with a mapping between acceptable signature creation policies and their corresponding signature validation policies, this building block shall determine if the signature to be validated contains references to or the identifier of one of these signature creation policies in the signature policy attribute.

• If no signature creation policy is contained in the signature, the building block should select a default signature validation policy.

NOTE: A default signature validation policy can be provided by the DA, by the configuration or can be established according to the minimum technical requirements and minimum requirements by law, if applicable.

• If the signature contains one signature creation policy identifier, which is part of the list of mappings, the SVA shall apply the corresponding validation policy during validation.

• If the signature contains a signature creation policy identifier that is not contained in the list of mappings, it shall be a policy decision (local configuration) whether default rules apply for the validation, or if the validation process is to be terminated.

• The building block shall access the electronic document identified by the contents of the property/attribute and containing the details of the policy; if it is not available, the building block shall return the indication INDETERMINATE with the sub-indication SIGNATURE_POLICY_NOT_AVAILABLE. If it cannot be parsed or processed for any other reason, the building block shall return the indication INDETERMINATE with the sub-indication POLICY_PROCESSING_ERROR.

• The building block shall extract the validation constraints from the rules encoded in the validation policy and return the indication PASSED together with the extracted validation constraints.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.5.2 (Inputs)",
        "testo": (
            "Ingressi del processo Revocation Freshness Checker (Tabella 11A, Input | Requirement): Revocation data | "
            "Mandatory; The certificate for which the revocation is being checked | Mandatory; Validation time | "
            "Mandatory; X.509 validation constraints | Mandatory."
        ),
        "testo_integrale": """Table 11A: Inputs to the Revocation Freshness Checker process
Input | Requirement
Revocation data | Mandatory
The certificate for which the revocation is being checked | Mandatory
Validation time | Mandatory
X.509 validation constraints | Mandatory""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.5.3 (Output)",
        "testo": (
            "Il processo deve produrre una delle indicazioni della Tabella 11B insieme ai dati di rapporto di "
            "convalida associati: PASSED se l'informazione sullo stato di revoca contenuta nei dati di revoca e' "
            "considerata fresca; FAILED se l'informazione sullo stato di revoca contenuta nei dati di revoca non e' "
            "considerata fresca."
        ),
        "testo_integrale": """The process shall output one of the following indications together with the associated validation report data as defined in Table 11B.

Table 11B: Output of the Revocation Freshness Checker process
Indication
PASSED | The revocation status information contained within the revocation data is considered fresh.
FAILED | The revocation status information contained within the revocation data is not considered fresh.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.5.4 (Processing)",
        "testo": (
            "1) Il blocco deve ottenere la freschezza massima accettata di revoca dai vincoli di validazione X.509 "
            "per il certificato dato: se i vincoli contengono un valore per la freschezza massima accettata, passa al "
            "passo successivo; altrimenti, se i dati di revoca sono una CRL o una risposta OCSP (IETF RFC 5280, IETF "
            "RFC 6960) con un valore nel campo nextUpdate, il blocco deve impostare la freschezza massima accettata "
            "all'intervallo di tempo tra i campi thisUpdate e nextUpdate e passare al passo successivo; se nextUpdate "
            "non e' valorizzato, il blocco deve uscire con l'indicazione FAILED. 2) Se il tempo di emissione "
            "dell'informazione sullo stato di revoca e' successivo al tempo di convalida meno la freschezza massima "
            "considerata, il blocco deve restituire PASSED, altrimenti FAILED. Note 1-3: il campo nextUpdate e' usato "
            "solo quando i vincoli di validazione non contengono un valore per la freschezza massima accettata (se il "
            "campo non e' usato dalla CA il blocco fallisce perche' non puo' determinare la freschezza; se la CA usa "
            "un nextUpdate vuoto per indicare che nuova informazione di stato e' sempre disponibile, il DA puo' "
            "risolvere riavviando il processo di convalida impostando una freschezza appropriata oppure recuperando "
            "dati di revoca aggiornati e fornendoli all'SVA insieme a un signing time immediatamente precedente al "
            "recupero, dal momento che il DA ha prova che la firma esisteva a quel momento; con nextUpdate "
            "valorizzato l'algoritmo assicura che, se il tempo di convalida e' successivo al tempo indicato da "
            "nextUpdate, l'informazione non sia considerata fresca); se il tempo di convalida contiene il tempo "
            "corrente l'algoritmo accetta informazione emessa \"non troppo tempo prima\" secondo il parametro di "
            "freschezza, mentre in presenza di informazione sul signing time il tempo di convalida corrisponde a un "
            "momento in cui la firma esisteva gia' e, con freschezza massima posta a zero (0), l'algoritmo accetta "
            "l'informazione solo se emessa dopo quel momento; il tempo di emissione dell'informazione sullo stato di "
            "revoca e il tempo di emissione dei dati di revoca possono differire (in una risposta OCSP il primo e' "
            "la data/ora del campo thisUpdate, il secondo la data/ora del campo producedAt)."
        ),
        "testo_integrale": """1) The building block shall get the maximum accepted revocation freshness from the X.509 validation constraints for the given certificate. If the constraints contain a value for the maximum accepted revocation freshness, the building block shall go to the next step. Otherwise, if the revocation information data is a CRL or an OCSP response (IETF RFC 5280 [1], IETF RFC 6960 [i.12]) with a value in the nextUpdate field, the building block shall set the maximum accepted freshness to the time interval between the fields thisUpdate and nextUpdate and it shall go to the next step. If nextUpdate is not set, the building block shall return with the indication FAILED.

NOTE 1: The nextUpdate field is only used when the validation constraints do not contain a value for the maximum accepted revocation freshness. When this field is not used by the CA, the building block fails since it is unable to determine the freshness. When the CA uses an empty nextUpdate to indicate that new status information is available all the time, the DA can solve this problem in two ways by restarting the validation process, and:

1) by setting an appropriate freshness; or

2) by retrieving revocation data containing up-to-date revocation status information;

providing this freshly fetched revocation data to the SVA together with a signing time of just before the revocation data was retrieved. This is possible since the DA has proof that the signature existed at that point in time.

When the nextUpdate-field is set, the algorithm ensures that if the given validation time is after the time indicated by nextUpdate, the revocation status information will not be considered fresh.

2) If the issuance time of the revocation status information is after the validation time minus the considered maximum freshness, the building block shall return the indication PASSED. Otherwise, the building block shall return the indication FAILED.

NOTE 2: If the validation time parameter contains current time, the algorithm accepts revocation status information that has been issued "not too long ago" according to the revocation freshness parameter. In this scenario, one cannot know when the signature has been created so one cannot decide whether a specific instance of revocation status information has been issued after signature creation or not.

When there is information about the signing time, the validation time parameter corresponds to a time when it is known the signature already existed (this can also be the time when a signed document has been received for example). If the maximum accepted freshness is then set to zero (0), the algorithm ensures that revocation status information is only accepted if it has been issued after that point in time.

NOTE 3: Revocation status information issuance time and revocation data issuance time can be different: When the revocation status information is provided through an OCSP response, then the revocation status issuance time is the date and time indicated in the thisUpdate field of the OCSP response whereas the revocation data issuance time is the date and time indicated in the producedAt field of the OCSP response.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.6.1 (Description)",
        "testo": (
            "Il blocco convalida il certificato di firma al tempo di convalida; se il tempo di convalida non e' "
            "fornito come input, la convalida deve essere eseguita al tempo corrente."
        ),
        "testo_integrale": """This building block validates the signing certificate at validation time. If the validation time is not provided as an input, the validation shall be performed at current time.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.6.2 (Inputs)",
        "testo": (
            "Ingressi del blocco di convalida del certificato X.509 (Tabella 12, Input | Requirement): Signing "
            "certificate | Mandatory; X.509 Validation Constraints | Mandatory; Validation time | Optional; "
            "Certificate Validation Data | Optional; X.509 Validation Parameters | Optional; Cryptographic "
            "Constraints | Optional; Other Certificates | Optional; Trust Anchors | Mandatory. Il processo di "
            "convalida puo' acquisire dati aggiuntivi di convalida dei certificati da fonti esterne."
        ),
        "testo_integrale": """Table 12: Inputs to the X.509 certificate validation building block
Input | Requirement
Signing certificate | Mandatory
X.509 Validation Constraints | Mandatory
Validation time | Optional
Certificate Validation Data | Optional
X.509 Validation Parameters | Optional
Cryptographic Constraints | Optional
Other Certificates | Optional
Trust Anchors | Mandatory

The validation process may acquire additional certificate validation data from external sources.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.6.3 (Outputs)",
        "testo": (
            "Il processo deve produrre una delle indicazioni della Tabella 13 insieme alle informazioni aggiuntive "
            "ivi definite. Tabella 13 (Indication | Sub-indication | Additional Information): PASSED | - | The "
            "certificate chain used in the successful validation. Any additional validation data acquired; "
            "INDETERMINATE | NO_CERTIFICATE_CHAIN_FOUND | -; INDETERMINATE | NO_CERTIFICATE_CHAIN_FOUND_NO_POE | The "
            "last certificate chain built; INDETERMINATE | OUT_OF_BOUNDS_NO_POE | The validated certificate chain; "
            "INDETERMINATE | OUT_OF_BOUNDS_NOT_REVOKED | The validated certificate chain; INDETERMINATE | "
            "REVOKED_NO_POE | The validated certificate chain; INDETERMINATE | CRYPTO_CONSTRAINTS_FAILURE_NO_POE | "
            "The last certificate chain built; INDETERMINATE | TRY_LATER | The last certificate chain built, the "
            "content of the nextUpdate field of the relevant CRL or OCSP-response; INDETERMINATE | REVOKED_CA_NO_POE "
            "| The last certificate chain built; INDETERMINATE | CHAIN_CONSTRAINTS_FAILURE | The last certificate "
            "chain built; INDETERMINATE | CERTIFICATE_CHAIN_GENERAL_FAILURE | The last certificate chain built; "
            "INDETERMINATE | REVOCATION_OUT_OF_BOUNDS_NO_POE | The validated certificate chain."
        ),
        "testo_integrale": """The process shall output one of the following indications together with additional information defined in Table 13.

Table 13: Output of the X.509 certificate validation building block
Indication | Sub-indication | Additional Information
PASSED | - | The certificate chain used in the successful validation. Any additional validation data acquired
INDETERMINATE | NO_CERTIFICATE_CHAIN_FOUND | -
INDETERMINATE | NO_CERTIFICATE_CHAIN_FOUND_NO_POE | The last certificate chain built
INDETERMINATE | OUT_OF_BOUNDS_NO_POE | The validated certificate chain
INDETERMINATE | OUT_OF_BOUNDS_NOT_REVOKED | The validated certificate chain
INDETERMINATE | REVOKED_NO_POE | The validated certificate chain
INDETERMINATE | CRYPTO_CONSTRAINTS_FAILURE_NO_POE | The last certificate chain built
INDETERMINATE | TRY_LATER | The last certificate chain built, the content of the nextUpdate field of the relevant CRL or OCSP-response
INDETERMINATE | REVOKED_CA_NO_POE | The last certificate chain built
INDETERMINATE | CHAIN_CONSTRAINTS_FAILURE | The last certificate chain built
INDETERMINATE | CERTIFICATE_CHAIN_GENERAL_FAILURE | The last certificate chain built
INDETERMINATE | REVOCATION_OUT_OF_BOUNDS_NO_POE | The validated certificate chain""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.6.4 (Processing)",
        "testo": (
            "1) Se il certificato di firma rappresenta un trust anchor: a) se nei vincoli di validazione X.509 e' "
            "associata una sunset date a quel trust anchor, il blocco deve verificare che la convalida sia anteriore "
            "alla sunset date e, se il tempo di convalida e' pari o successivo, deve porre lo stato corrente a "
            "INDETERMINATE/NO_CERTIFICATE_CHAIN_FOUND_NO_POE e passare al passo 2); b) altrimenti il blocco puo', in "
            "base alla politica di firma o alla configurazione locale, uscire con l'indicazione PASSED, oppure deve "
            "passare al passo successivo. 2) Il blocco deve costruire una nuova catena prospettica di certificati non "
            "ancora valutata; se il parametro \"Other Certificates\" e' presente, solo i certificati di quell'insieme "
            "possono essere usati per costruire la catena; la catena deve soddisfare le condizioni di catena "
            "prospettica: a) se nessuna nuova catena e' costruibile, il blocco deve restituire lo stato corrente, "
            "l'ultima catena costruita e le informazioni aggiuntive salvate al passo 4-a) o, se nessuna catena e' "
            "stata costruita, INDETERMINATE con NO_CERTIFICATE_CHAIN_FOUND; b) altrimenti deve aggiungere la catena "
            "all'insieme delle catene prospettate e passare al passo 3). 3) Se nei vincoli X.509 una sunset date e' "
            "associata al trust anchor da cui la catena corrente e' stata costruita, il blocco deve verificare che la "
            "convalida sia anteriore alla sunset date e, se il tempo di convalida e' pari o successivo, porre lo stato "
            "corrente a INDETERMINATE/NO_CERTIFICATE_CHAIN_FOUND_NO_POE e passare al passo 2). 4) Il blocco deve "
            "eseguire la convalida della catena prospettica con input: la catena prospettica costruita al passo "
            "precedente, il trust anchor usato al passo precedente, i parametri X.509 forniti negli input e il tempo "
            "di convalida; la convalida deve seguire la PKIX Certification Path Validation di IETF RFC 5280, clausola "
            "6.1, con l'eccezione del modello di validita' e della verifica che il tempo di convalida cada nel "
            "periodo di validita' del certificato di firma (verifica fatta al passo 7). Sono possibili due modelli di "
            "validita', da specificare come vincolo di validazione X.509: shell model (tutti i certificati validi al "
            "tempo di convalida) oppure chain model (tutti i certificati validi al tempo in cui sono stati usati per "
            "emettere un certificato); per lo shell model valgono i vincoli di IETF RFC 5280, clausola 6.1, per il "
            "chain model i vincoli devono seguire l'algoritmo dei paragrafi 6 e 7 a partire da \"According to this "
            "model\", clausola 6 della Parte 9 di common PKI v2.0, sostituendo le due occorrenze del modale \"should\" "
            "con \"shall\" (il chain model e' usato in Paesi come la Germania). La convalida deve includere il "
            "controllo di revoca per ogni certificato della catena, salvo i certificati per cui i vincoli X.509 "
            "dichiarano esplicitamente che il controllo non e' eseguito; se l'SVA dispone di piu' istanze applicabili "
            "di dati di revoca per un certificato, deve usare l'istanza emessa piu' di recente nota per contenere "
            "informazione sullo stato di revoca di quel certificato. La convalida non deve includere la verifica che "
            "il tempo di convalida cada nel periodo di validita' del certificato dell'emittente l'informazione di "
            "revoca, ma deve includere la verifica che la data di emissione dei dati di revoca cada in quel periodo "
            "di validita' (verifica del tempo di convalida rispetto al certificato dell'emittente fatta al passo 8, "
            "quando tali certificati sono noti come non revocati): a) se la convalida del percorso restituisce "
            "successo, il blocco deve eseguire il Revocation Freshness Checker (clausola 5.2.5) per ogni certificato "
            "della catena, salvo i certificati per cui i vincoli X.509 dichiarano che il controllo di revoca non e' "
            "eseguito, con input i dati di revoca usati, il certificato corrispondente di cui si controlla lo stato e "
            "il tempo di convalida; se l'esito e' PASSED per tutti passa al passo successivo, altrimenti pone lo stato "
            "corrente a INDETERMINATE con sotto-indicazione TRY_LATER, salva i dati di revoca usati contenenti "
            "informazione non sufficientemente fresca e, se disponibile, un suggerimento su quando ritentare la "
            "convalida (es. il contenuto del campo nextUpdate della CRL o della risposta OCSP) e passa al passo 2); "
            "b) se la convalida fallisce perche' il certificato di firma e' determinato come revocato, il blocco deve "
            "restituire INDETERMINATE, REVOKED_NO_POE, la catena validata, la data di revoca e il motivo della "
            "revoca; c) se fallisce perche' il certificato di firma e' determinato come sospeso (on hold), deve "
            "restituire INDETERMINATE, TRY_LATER, la catena validata, il tempo di sospensione e, se disponibile, il "
            "contenuto del campo nextUpdate della CRL o risposta OCSP usata come suggerimento su quando ritentare; d) "
            "se fallisce perche' una CA intermedia e' revocata, deve porre lo stato corrente a "
            "INDETERMINATE/REVOKED_CA_NO_POE e passare al passo 2); e) se fallisce per qualunque altro motivo, deve "
            "porre lo stato corrente a INDETERMINATE/CERTIFICATE_CHAIN_GENERAL_FAILURE e passare al passo 2). 5) Il "
            "blocco deve applicare i vincoli di validazione X.509 alla catena; se la catena non li soddisfa, deve "
            "porre lo stato corrente a INDETERMINATE/CHAIN_CONSTRAINTS_FAILURE e passare al passo 2). 6) Il blocco "
            "deve applicare i vincoli crittografici alla catena; se la catena non li soddisfa, deve porre lo stato "
            "corrente a INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE e passare al passo 2). 7) Il blocco deve "
            "verificare che il tempo di convalida sia nell'intervallo di validita' del certificato di firma; se il "
            "vincolo non e' soddisfatto, deve restituire l'indicazione INDETERMINATE con la sotto-indicazione "
            "OUT_OF_BOUNDS_NOT_REVOKED e la catena di certificati validata quando il certificato di firma e' noto "
            "come non revocato, e l'indicazione INDETERMINATE con la sotto-indicazione OUT_OF_BOUNDS_NO_POE e la "
            "catena validata quando non e' noto se il certificato di firma sia stato revocato. 8) Il blocco deve "
            "verificare che il tempo di convalida sia nell'intervallo di validita' del certificato dell'emittente i "
            "dati di revoca; se il vincolo non e' soddisfatto, deve restituire INDETERMINATE con la sotto-indicazione "
            "REVOCATION_OUT_OF_BOUNDS_NO_POE. 9) Il blocco deve restituire la catena con l'indicazione PASSED. Note "
            "1-10: informazioni necessarie per l'algoritmo PKIX sono estratte dal certificato che rappresenta il "
            "trust anchor (nome nel campo subject come trusted issuer name, contenuto di subjectPublicKeyInfo come "
            "sorgente dell'algoritmo e della chiave pubblica fidata); la sunset date associata al trust anchor e' il "
            "tempo fino al quale i trust anchor erano considerati affidabili secondo ETSI TS 119 172-1, Tabella A.2 "
            "riga (m)1.1; la verifica del tempo di convalida rispetto al periodo di validita' del certificato di "
            "firma e' fatta al passo 7); l'uso dell'istanza di revoca piu' recente evita di usare una CRL fresca ma "
            "non ancora contenente la revoca, e consente di usare dati di revoca emessi dopo la scadenza del "
            "certificato quando la CA mantiene disponibile l'informazione oltre la scadenza; si assume che i dati di "
            "revoca siano forniti solo dal DA e che sia compito del DA richiederne di nuovi (le estensioni "
            "id-pkix-ocsp-nocheck e id-etsi-ext-valassured-ST-certs possono escludere il controllo di revoca e quindi "
            "anche il controllo di freschezza); un certificato e' noto come non revocato quando la CA continua a "
            "fornire informazione di stato dopo la scadenza e questa e' stata controllata, o quando la CA assicura "
            "che il certificato non era revocato al momento della firma; la costruzione della catena (passo 2) e la "
            "convalida (passo 4) possono usare dati di validazione estratti dalla firma o ottenuti da altre fonti "
            "(es. server LDAP), la cui gestione e' fuori ambito; per la costruzione della catena si rinvia a IETF RFC "
            "4158."
        ),
        "testo_integrale": """1) If the signing certificate represents a trust anchor, then:

a) If, in the X.509 Validation Constraints, a sunset date is associated to that trust anchor, the building block shall check whether validation is before the sunset date. If validation time is at or after the sunset date, the building block shall set the current status to INDETERMINATE/NO_CERTIFICATE_CHAIN_FOUND_NO_POE and shall go to step 2).

b) Else, the building block may, based on signature policy or local configuration, return with the indication PASSED. Otherwise, the building block shall go to the next step.

NOTE 1: A trust anchor can be represented by means of a certificate, in which case the trust anchor information necessary to perform the IETF RFC 5280 [1] path validation algorithm is extracted from the certificate as described in section 6.1.1 of IETF RFC 5280 [1] which states that the name in the subject field is used as the trusted issuer name and the contents of the subjectPublicKeyInfo field is used as the source of the trusted public key algorithm and the trusted public key.

2) The building block shall build a new prospective certificate chain that has not yet been evaluated. If the "Other Certificates" parameter is present, only certificates contained in that set of certificates may be used to build the chain. The chain shall satisfy the conditions of a prospective certificate chain:

a) If no new chain can be built, the building block shall return the current status, the last chain built and any additional information saved in step 4-a) or, if no chain has been built, the indication INDETERMINATE with the sub-indication NO_CERTIFICATE_CHAIN_FOUND.

b) Otherwise, the building block shall add this chain to the set of prospected chains and shall go to step 3).

3) If, in the X.509 Validation Constraints, a sunset date is associated to the trust anchor from which the current chain has been built, the building block shall check whether validation is before the sunset date. If validation time is at or after the sunset date, the building block shall set the current status to INDETERMINATE/NO_CERTIFICATE_CHAIN_FOUND_NO_POE and shall go to step 2).

NOTE 2: ETSI TS 119 172-1 [4], Table A.2 row (m)1.1. explicitly states that the X509 Certificate Validation Constraints may indicate alongside the set of trust anchors, "a time until when these trust anchors were considered reliable." This time is what is referred to here as a "sunset date associated to the trust anchor".

4) The building block shall perform validation of the prospective certificate chain with the following inputs: the prospective chain built in the previous step, the trust anchor used in the previous step, the X.509 parameters provided in the inputs and the validation time. The validation shall be following the PKIX Certification Path Validation of IETF RFC 5280 [1], clause 6.1 with the exception of the validity model and the verification of whether the validation time is during the validity period of the signing certificate.

NOTE 3: The verification of whether the validation time is during the validity period of the signing certificate is done in step 7).

• Two validity models may be supported:

- all certificates are valid at validation time (shell model); or

- all certificates are valid at the time they were used for issuing a certificate (chain model).

The validity model to be used shall be specified as a X.509 validation constraint.

For the shell model, the X.509 validation constraints shall be as defined in IETF RFC 5280 [1], clause 6.1.

For the chain model, the X.509 validation constraints shall follow the algorithm described in paragraphs 6 and 7, starting from "According to this model", clause 6 in Part 9 of common PKI v2.0 [5], where the two instances of the modal verb "should" shall be replaced with a "shall".

EXAMPLE 1: The chain model is used in countries like Germany.

The validation shall include revocation checking for each certificate in the chain, to the exception of the certificates for which the the X.509 Validation Constraints explicitly state that revocation checking is not performed. Whenever the SVA is in possession of multiple applicable instances of revocation data for a certificate, the SVA shall use the latest issued instance that is known to contain revocation status information about the certificate.

NOTE 4: This ensures that in the case of a revoked certificate the SVA does not use a CRL, which contains revocation status information that is considered fresh but does not yet contain the information of the fact that the certificate is revoked, whenever a fresher CRL is already available to the SVA. It also ensures that revocation data issued after expiration of the certificate can be used when the CA is known to keep revocation status information available beyond expiration of that certificate.

NOTE 5: Additional information and rationale about certificate revocation checking can be found in ISO/IEC 14533-4, Annexes E.3 and E.4 [i.20].

The validation shall not include the verification of whether the validation time is within the validity period of the certificate of the issuer of the revocation status information, however it shall include the verification of whether the issuance date of the revocation data containing the revocation status information is within that validity period:

NOTE 6: The verification of whether the validation time is within the validity period of the certificate of the issuer of the revocation data containing the revocation status information is done in step 8), when those certificates are known to be not revoked.

a) if the certificate path validation returns a success indication, the building block shall run the Revocation Freshness Checker (clause 5.2.5) for each certificate in the chain, with the exception of the certificates for which the X.509 Validation Constraints state that revocation checking is not performed, with the following inputs: the used revocation data, the corresponding certificate for which the revocation status is being checked and the validation time. If the checker returns PASSED for all of these, the building block shall go to the next step. Otherwise, the building block shall set the current status to the indication INDETERMINATE, the sub-indication TRY_LATER, shall save the used revocation data which contained revocation status information that was not fresh enough and, if available, a suggestion for when to try the validation again (e.g. the content of the nextUpdate field of the CRL or OCSP response), and shall go to step 2);

NOTE 7: While many implementations try to fetch revocation data online, the process here assumes that revocation data is supplied by the DA only and it is the task of the DA to request new revocation data.

EXAMPLE 2: In line with IETF RFC 6960 [i.12], a CA may specify that an OCSP client can trust a responder for the lifetime of the responder's certificate by including the extension id-pkix-ocsp-nocheck in the responder's certificate.
Similarly, in line with ETSI EN 319 412-1 [i.21], upon presence of the id-etsi-ext-valassured-ST-certs extension in the certificate, the relying party can decide not to check the certificate revocation status when validating a digital signature.
In those situations, because no revocation checking is performed for the certificates containing those extensions, revocation freshness checking is equally not performed on those certificates.

b) if the certificate path validation returns a failure indication because the signing certificate has been determined to be revoked, the building block shall return the indication INDETERMINATE, the sub-indication REVOKED_NO_POE, the validated chain, the revocation date and the reason for revocation;

c) if the certificate path validation returns a failure indication because the signing certificate has been determined to be on hold, the building block shall return the indication INDETERMINATE, the sub-indication TRY_LATER, the validated chain, the suspension time and, if available, the content of the nextUpdate -field of the CRL or OCSP-response used as the suggestion for when to try the validation again;

d) if the certificate path validation returns a failure indication because an intermediate CA is revoked, the building block shall set the current status to INDETERMINATE/REVOKED_CA_NO_POE and shall go to step 2); or

e) if the certificate path validation returns a failure indication with any other reason, the building block shall set the current status to INDETERMINATE/CERTIFICATE_CHAIN_GENERAL_FAILURE and shall go to step 2).

5) The building block shall apply the X.509 Validation Constraints to the chain. If the chain does not match these constraints, the building block shall set the current status to INDETERMINATE/CHAIN_CONSTRAINTS_FAILURE and shall go to step 2).

6) The building block shall apply the cryptographic constraints to the chain. If the chain does not match these constraints, the building block shall set the current status to INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE and shall go to step 2).

7) The building block shall check that the validation time is in the validity range of the signing certificate. If this constraint is not satisfied, the building block shall return the indication INDETERMINATE, the sub-indication OUT_OF_BOUNDS_NOT_REVOKED and the validated certificate chain when the signing certificate is known not having been revoked and the indication INDETERMINATE, the sub-indication OUT_OF_BOUNDS_NO_POE and the validated certificate chain when it is not known whether the signing certificate has been revoked or not.

NOTE 8: A certificate is known to not have been revoked when the CA keeps providing revocation status information after expiration of the certificate and this revocation status information has been checked or the CA assures that the certificate was not revoked at signing time.

8) The building block shall check that the validation time is within the validity range of the certificate of the issuer of the revocation data. If this constraint is not satisfied, the building block shall return the indication INDETERMINATE, the sub-indication REVOCATION_OUT_OF_BOUNDS_NO_POE.

9) The building block shall return the chain with the indication PASSED.

NOTE 9: Chain construction (step 2) and validation (step 4) can use validation data (certificates, CRLs, etc.) extracted from the signature or obtained from other sources (e.g. LDAP servers). The management of the sources for the retrieval of validation data is out of the scope of the present document.

NOTE 10: For more information and rationale about certificate chain construction, refer to IETF RFC 4158 [i.1].""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.7.2 (Inputs)",
        "testo": (
            "Ingressi del blocco di convalida crittografica (Tabella 14, Input | Requirement): Signature | "
            "Mandatory; Signing Certificate | Mandatory; Validated certificate chain | Optional; Signer's Document "
            "or Signer's Document Representation | Optional. Note: nella maggior parte dei casi la verifica "
            "crittografica richiede solo il certificato di firma e non l'intera catena validata, ma per alcuni "
            "algoritmi puo' servire l'intera catena (es. chiavi pubbliche DSS/DSA, che ereditano i parametri dal "
            "certificato dell'emittente); nella convalida di firme di tipo detached, dove sono firmati solo gli hash "
            "degli oggetti e gli oggetti non fanno parte della firma, non e' specificato se spetti al DA convalidare "
            "tali hash o se un'implementazione usi la presente clausola per farli convalidare all'SVA (entrambe le "
            "varianti sono possibili)."
        ),
        "testo_integrale": """Table 14: Inputs to the cryptographic validation building block
Input | Requirement
Signature | Mandatory
Signing Certificate | Mandatory
Validated certificate chain | Optional
Signer's Document or Signer's Document Representation | Optional

NOTE 1: In most cases, the cryptographic verification requires only the signing certificate and not the entire validated chain. However, for some algorithms the full chain can be required (e.g. the case of DSS/DSA public keys, which inherit their parameters from the issuer certificate).

NOTE 2: When validating signatures like detached signatures, where only the hashes of objects are signed but the objects themselves are not part of the signature, it is unspecified whether it is the task of the DA to validate these hashes or whether an implementation uses the present clause for having the hash(es) of such objects validated by the SVA. Both variants are possible.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.7.3 (Outputs)",
        "testo": (
            "Il processo deve produrre una delle indicazioni della Tabella 15 insieme ai dati di rapporto di "
            "convalida associati. Tabella 15: PASSED (nessuna sotto-indicazione) | The signature passed the "
            "cryptographic verification. | -; FAILED / HASH_FAILURE | The hash of at least one of the signed data "
            "items does not match the corresponding hash value in the signature. | The process should output: the "
            "identifier(s) (e.g. an URI) of the signed data that caused the failure; FAILED / SIG_CRYPTO_FAILURE | "
            "The cryptographic verification of the signature value failed. | -; INDETERMINATE / "
            "SIGNED_DATA_NOT_FOUND | Cannot obtain signed data. | The process should output: the identifier(s) (e.g. "
            "an URI) of the signed data that caused the failure."
        ),
        "testo_integrale": """The process shall output one of the following indications together with the associated validation report data as listed in Table 15.

Table 15: Outputs of the cryptographic validation building block
Indication | Description | Additional data items
PASSED | The signature passed the cryptographic verification. | -
FAILED / HASH_FAILURE | The hash of at least one of the signed data items does not match the corresponding hash value in the signature. | The process should output: • The identifier (s) (e.g. an URI) of the signed data that caused the failure.
FAILED / SIG_CRYPTO_FAILURE | The cryptographic verification of the signature value failed. | -
INDETERMINATE / SIGNED_DATA_NOT_FOUND | Cannot obtain signed data. | The process should output: • The identifier (s) (e.g. an URI) of the signed data that caused the failure.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.7.4 (Processing)",
        "testo": (
            "Il primo e il secondo passo e i dati da firmare dipendono dal tipo di firma; i dettagli tecnici sono "
            "fuori ambito e si rinvia a ETSI EN 319 122-1, ETSI EN 319 122-2, ETSI EN 319 132-1, ETSI EN 319 132-2, "
            "ETSI EN 319 142-1, ETSI EN 319 142-2 e IETF RFC 3852. 1) Il blocco deve ottenere gli elementi di dati "
            "firmati (es. SD o SDR) se non forniti negli input (es. dereferenziando un URI presente nella firma); se "
            "non possono essere ottenuti, deve restituire l'indicazione INDETERMINATE con la sotto-indicazione "
            "SIGNED_DATA_NOT_FOUND. 2) L'SVA deve verificare l'integrita' degli elementi di dati firmati; in caso di "
            "fallimento il blocco deve restituire l'indicazione FAILED con la sotto-indicazione HASH_FAILURE. 3) Il "
            "blocco deve verificare la firma crittografica usando la chiave pubblica estratta dal certificato di "
            "firma nella catena, il valore della firma e l'algoritmo di firma estratti dalla firma; se la verifica "
            "crittografica produce un esito di successo, il blocco deve restituire l'indicazione PASSED. 4) "
            "Altrimenti il blocco deve restituire l'indicazione FAILED e la sotto-indicazione SIG_CRYPTO_FAILURE."
        ),
        "testo_integrale": """The first and second steps as well as the Data To Be Signed depend on the signature type. The technical details on how to do this correctly are out of scope for the present document. See ETSI EN 319 122-1 [i.2], ETSI EN 319 122-2 [i.3], ETSI EN 319 132-1 [i.4], ETSI EN 319 132-2 [i.5], ETSI EN 319 142-1 [i.6], ETSI EN 319 142-2 [i.7] and IETF RFC 3852 [i.16] for details.

1) The building block shall obtain the signed data items (e.g. SD or SDR) if not provided in the inputs (e.g. by dereferencing an URI present in the signature). If the signed data items cannot be obtained, the building block shall return the indication INDETERMINATE with the sub-indication SIGNED_DATA_NOT_FOUND.

2) The SVA shall check the integrity of the signed data items. In case of failure, the building block shall return the indication FAILED with the sub-indication HASH_FAILURE.

3) The building block shall verify the cryptographic signature using the public key extracted from the signing certificate in the chain, the signature value and the signature algorithm extracted from the signature. If this cryptographic verification outputs a success indication, the building block shall return the indication PASSED.

4) Otherwise, the building block shall return the indication FAILED and the sub-indication SIG_CRYPTO_FAILURE.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.8.2 (Inputs)",
        "testo": (
            "Ingressi del blocco SAV (Tabella 16, Input | Requirement): Signature | Mandatory; Certificate Chain | "
            "Optional; Validation time | Optional; Cryptographic verification output | Optional; Cryptographic "
            "Constraints | Optional; Signature Elements Constraints | Optional."
        ),
        "testo_integrale": """Table 16: Inputs to the SAV building block
Input | Requirement
Signature | Mandatory
Certificate Chain | Optional
Validation time | Optional
Cryptographic verification output | Optional
Cryptographic Constraints | Optional
Signature Elements Constraints | Optional""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.8.3 (Outputs)",
        "testo": (
            "Il processo deve produrre una delle indicazioni della Tabella 17 insieme alle informazioni aggiuntive "
            "ivi definite. Tabella 17: PASSED | The signature is conformant with the validation constraints. | -; "
            "INDETERMINATE / SIG_CONSTRAINTS_FAILURE | The signature is not conformant with the validation "
            "constraints. | The set of constraints that are not verified by the signature; INDETERMINATE / "
            "CRYPTO_CONSTRAINTS_FAILURE_NO_POE | At least one of the algorithms used in validation of the signature "
            "together with the size of the key, if applicable, used with that algorithm is no longer considered "
            "reliable. | A list of algorithms, together with the size of the key, if applicable, that have been used "
            "in validation of the signature but no longer are considered reliable together with a time up to which "
            "each of the listed algorithms were considered secure."
        ),
        "testo_integrale": """The process shall output one of the following indications together with the additional information as defined in Table 17.

Table 17: Outputs of the SAV building block
Indication | Description | Additional data items
PASSED | The signature is conformant with the validation constraints. | -
INDETERMINATE / SIG_CONSTRAINTS_FAILURE | The signature is not conformant with the validation constraints. | The set of constraints that are not verified by the signature.
INDETERMINATE / CRYPTO_CONSTRAINTS_FAILURE_NO_POE | At least one of the algorithms used in validation of the signature together with the size of the key, if applicable, used with that algorithm is no longer considered reliable. | A list of algorithms, together with the size of the key, if applicable, that have been used in validation of the signature but no longer are considered reliable together with a time up to which each of the listed algorithms were considered secure.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.8.4.1 (General requirements)",
        "testo": (
            "Per ciascun vincolo: se il vincolo richiede l'elaborazione di una proprieta'/attributo nella firma, il "
            "blocco deve eseguire l'elaborazione come specificato nelle clausole 5.2.8.4.2.1-5.2.8.4.2.7; quando un "
            "attributo e' presente ma malformato, l'SVA deve procedere come se l'attributo non fosse presente (se la "
            "politica di convalida richiede la presenza di un attributo mancante o trattato come mancante la "
            "convalida fallisce con indicazione appropriata; se la presenza non e' richiesta, l'attributo e' "
            "ignorato; esempio: la codifica di un attributo signer-location e' rotta o contiene un valore errato, "
            "come un codice di Paese non valido). Se almeno uno degli algoritmi usati nella convalida della firma, o "
            "la dimensione delle chiavi usate con tali algoritmi, non e' considerato affidabile al tempo di "
            "convalida fornito come input (o, se non fornito, al tempo corrente), il blocco deve restituire "
            "INDETERMINATE con la sotto-indicazione CRYPTO_CONSTRAINTS_FAILURE_NO_POE insieme all'elenco degli "
            "algoritmi e delle dimensioni di chiave, se applicabili, interessati e al tempo fino al quale ciascun "
            "algoritmo e' stato considerato sicuro dai vincoli crittografici (controllo usato quando algoritmo o "
            "dimensione di chiave erano sicuri al momento della firma e sono decaduti solo anni dopo: una chiave RSA "
            "di 2 400 bit nel 2013 e' assunta sicura per circa 20 anni, e una firma creata con tale chiave puo' "
            "essere protetta dopo 25 anni con una marca temporale basata su una chiave RSA di circa 5 300 bit "
            "secondo ETSI TS 119 312; gli algoritmi interessati non sono solo quelli di hash e di firma della firma "
            "stessa ma anche quelli di certificati, CRL, marche temporali o altro materiale usato nel processo). Se "
            "uno o piu' controlli falliscono, il blocco deve restituire INDETERMINATE con la sotto-indicazione "
            "SIG_CONSTRAINTS_FAILURE insieme all'insieme dei vincoli non soddisfatti dalla firma; se tutti i vincoli "
            "sono soddisfatti, il blocco deve restituire PASSED. Il blocco puo' ignorare l'elaborazione di una "
            "proprieta'/attributo per cui non e' specificato alcun vincolo di validazione."
        ),
        "testo_integrale": """For each constraint:

• If the constraint necessitates processing a property/attribute in the signature, the building block shall perform the processing of the property/attribute as specified in clauses 5.2.8.4.2.1 to 5.2.8.4.2.7. When an attribute is present but is malformed, the SVA shall proceed as if the attribute was not present.

NOTE 1: When the signature validation policy requires the presence of an attribute that is missing or treated as missing since it is malformed, the validation will fail with an appropriate indication. When the presence is not required, the attribute will be ignored.

EXAMPLE: The encoding of a signer-location attribute is broken or the attribute contains an incorrect value (e.g. not a valid country code). Most often this does not affect the validity of the signature. When such a signer location is required by the policy, the validation algorithm will respect the requirement.

• If at least one of the algorithms that have been used in validation of the signature or the size of the keys used with such an algorithm is not considered reliable at the validation time provided as input or, if not provided as input at current time, the building block shall return the indication INDETERMINATE with the sub-indication CRYPTO_CONSTRAINTS_FAILURE_NO_POE together with the list of algorithms and key sizes, if applicable, that are concerned and the time for each of the algorithms up to which the respective algorithm has been considered secure by the cryptographic constraints.

NOTE 2: This check is used when the algorithm or key size used was at the time of signing the signed object secure and only expired years later. Long term validation still allows validation of the signed object if e.g. time-stamps using different, still secure, algorithms or key sizes have been applied in time. E.g. an RSA-key of 2 400 bits is, in 2013, assumed to be secure for ~20 years. If a signature created with such a key is to be verified using this algorithm in 25 years from now, it can be secured by e.g. creating a time-stamp using an RSA-key of ~5 300 bits according to ETSI TS 119 312 [i.14]. The algorithms of concern are not only the hash- and signature-algorithm for the signature itself, but also for any of the certificate, CRLs, time-stamps or other material used in the validation process.

• If one or more checks fail, the building block shall return the indication INDETERMINATE with the sub-indication SIG_CONSTRAINTS_FAILURE together with the set of constraints that are not satisfied by the signature. And

• If all the constraints are satisfied, the building block shall return the indication PASSED.

The building block may ignore processing a property/attribute for which no validation constraint is specified.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.8.4.2.1 (Processing signing certificate reference constraint)",
        "testo": (
            "Se l'attributo Signing Certificate Identifier contiene riferimenti ad altri certificati nel percorso, "
            "il blocco deve controllare ciascuno dei certificati del percorso di certificazione rispetto a quei "
            "riferimenti. Quando la proprieta' contiene uno o piu' riferimenti a certificati diversi da quelli "
            "presenti nel percorso di certificazione, il blocco deve restituire l'indicazione INDETERMINATE con la "
            "sotto-indicazione SIG_CONTRAINTS_FAILURE. Quando uno o piu' certificati del percorso non sono "
            "referenziati da questa proprieta' e la politica di firma impone che i riferimenti a tutti i certificati "
            "del percorso siano presenti, il blocco deve restituire INDETERMINATE con la sotto-indicazione "
            "SIG_CONTRAINTS_FAILURE (refuso del testo ufficiale, altrove SIG_CONSTRAINTS_FAILURE)."
        ),
        "testo_integrale": """If the Signing Certificate Identifier attribute contains references to other certificates in the path, the building block shall check each of the certificates in the certification path against these references.

When this property contains one or more references to certificates other than those present in the certification path, the building block shall return the indication INDETERMINATE with the sub-indication SIG_CONTRAINTS_FAILURE.

When one or more certificates in the certification path are not referenced by this property, and the signature policy mandates references to all the certificates in the certification path to be present, the building block shall return the indication INDETERMINATE with the sub-indication SIG_CONTRAINTS_FAILURE.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.8.4.2.2 (Processing claimed signing time)",
        "testo": (
            "Se i vincoli sugli elementi della firma contengono vincoli su questa proprieta', l'SVA deve seguire le "
            "loro regole per il controllo di questa proprieta' firmata. Altrimenti l'SVA deve rendere il valore di "
            "questa proprieta'/attributo disponibile al DA, perche' possa decidere un'elaborazione aggiuntiva "
            "adeguata, fuori dall'ambito del presente documento."
        ),
        "testo_integrale": """If the signature elements constraints contain constraints regarding this property, the SVA shall follow its rules for checking this signed property.

Otherwise, the SVA shall make the value of this property/attribute available to the DA, so that it can decide additional suitable processing, which is out of the scope of the present document.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Il controllo si applica se i signature elements constraints contengono vincoli riguardanti questa "
            "proprieta'/attributo."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.8.4.2.3 (Processing Signed Data Object format)",
        "testo": (
            "Se i vincoli sugli elementi della firma contengono vincoli su questa proprieta', il blocco deve seguire "
            "le loro regole per il controllo di questa proprieta' firmata. Altrimenti l'SVA deve rendere il valore di "
            "questa proprieta'/attributo disponibile al DA, perche' possa decidere un'elaborazione aggiuntiva "
            "adeguata, fuori dall'ambito del presente documento."
        ),
        "testo_integrale": """If the signature elements constraints contain constraints regarding this property, the building block shall follow its rules for checking this signed property.

Otherwise, the SVA shall make the value of this property/attribute available to the DA, so that it can decide additional suitable processing, which is out of the scope of the present document.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Il controllo si applica se i signature elements constraints contengono vincoli riguardanti questa "
            "proprieta'/attributo."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.8.4.2.4 (Processing indication of production place of the signature)",
        "testo": (
            "Se i vincoli sugli elementi della firma contengono vincoli su questa proprieta', il blocco deve seguire "
            "le loro regole per il controllo di questa proprieta' firmata. Altrimenti l'SVA deve rendere il valore di "
            "questa proprieta'/attributo disponibile al DA, perche' possa decidere un'elaborazione aggiuntiva "
            "adeguata, fuori dall'ambito del presente documento."
        ),
        "testo_integrale": """If the signature elements constraints contain constraints regarding this property, the building block shall follow its rules for checking this signed property.

Otherwise, the SVA shall make the value of this property/attribute available to the DA, so that it can decide additional suitable processing, which is out of the scope of the present document.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Il controllo si applica se i signature elements constraints contengono vincoli riguardanti questa "
            "proprieta'/attributo."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.8.4.2.5 (Processing time-stamps on Signed Data Objects)",
        "testo": (
            "Se i vincoli sugli elementi della firma contengono vincoli specifici per le marche temporali sui "
            "Signed Data Objects (i dati coperti dalla firma), il blocco deve verificare che siano soddisfatti. A tal "
            "fine, per ogni attributo content-time-stamp: 1) il blocco deve eseguire il processo di convalida per le "
            "marche temporali AdES definito nella clausola 5.4 con il token di marca temporale dell'attributo "
            "content-time-stamp; 2) il blocco deve controllare il message imprint verificando che l'hash dei dati "
            "firmati ottenuto con l'algoritmo indicato nel token di marca temporale corrisponda al message imprint "
            "indicato nel token; 3) il blocco deve applicare i vincoli per gli attributi content-time-stamp ai "
            "risultati restituiti nei passi precedenti; se un controllo fallisce, deve restituire l'indicazione "
            "INDETERMINATE con la sotto-indicazione SIG_CONSTRAINTS_FAILURE insieme a una spiegazione del vincolo "
            "non verificato."
        ),
        "testo_integrale": """If the signature elements constraints contain specific constraints for time-stamps on Signed Data Objects, i.e. the data covered by the signature, the building block shall check that they are satisfied. To do so, for each content-time-stamp attribute:

1) The building block shall perform the Validation Process for AdES time-stamps as defined in clause 5.4 with the time-stamp token of the content-time-stamp attribute.

2) The building block shall check the message imprint by checking that the hash of the signed data obtained using the algorithm indicated in the time-stamp token matches the message imprint indicated in the token. And

3) The building block shall apply the constraints for content-time-stamp attributes to the results returned in the previous steps. If any check fails, the building block shall return the indication INDETERMINATE with the sub-indication SIG_CONSTRAINTS_FAILURE together with an explanation of the unverified constraint.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Il controllo si applica se i signature elements constraints contengono vincoli specifici per le marche "
            "temporali sui Signed Data Objects."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.8.4.2.6 (Processing countersignatures)",
        "testo": (
            "Se i vincoli sugli elementi della firma definiscono vincoli specifici per gli attributi di "
            "controfirma, il blocco deve verificare che siano soddisfatti. A tal fine, per ogni attributo di "
            "controfirma: 1) il blocco deve eseguire il processo di convalida della firma usando la controfirma "
            "contenuta nella proprieta'/attributo come firma e la stringa di ottetti del valore di firma della firma "
            "come Signed Data Object; 2) il blocco deve applicare i vincoli per gli attributi di controfirma al "
            "risultato restituito nel passo precedente; se un controllo fallisce, deve restituire l'indicazione "
            "INDETERMINATE con la sotto-indicazione SIG_CONSTRAINTS_FAILURE insieme a una spiegazione del vincolo non "
            "verificato. Se i vincoli sugli elementi della firma non contengono alcun vincolo sulle controfirme, il "
            "blocco puo' comunque verificare la controfirma e fornire i risultati nel rapporto di convalida; non deve "
            "tuttavia considerare la convalida della firma come fallita se la controfirma non puo' essere convalidata "
            "con successo."
        ),
        "testo_integrale": """If the signature elements constraints define specific constraints for countersignature attributes, the building block shall check that they are satisfied. To do so, for each countersignature attribute:

1) The building block shall perform the signature validation process using the countersignature in the property/attribute as the signature and the signature value octet string of the signature as the Signed Data Object. And

2) The building block shall apply the constraints for countersignature attributes to the result returned in the previous step. If any check fails, the building block shall return the indication INDETERMINATE with the sub-indication SIG_CONSTRAINTS_FAILURE together with an explanation of the unverified constraint.

If the signature elements constraints do not contain any constraint on countersignatures, the building block may still verify the countersignature and provide the results in the validation report. However, it shall not consider the signature validation to having failed if the countersignature cannot be successfully validated.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Prima parte: si applica se i signature elements constraints definiscono vincoli specifici per gli "
            "attributi di controfirma; la parte finale si applica quando tali vincoli non sono presenti."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.8.4.2.7 (Processing signer attributes)",
        "testo": (
            "Se i vincoli sugli elementi della firma definiscono vincoli specifici per gli attributi certificati e "
            "le asserzioni firmate: 1) il blocco deve convalidare i certificati di attributo e le asserzioni firmate "
            "presenti in questa proprieta'/attributo seguendo le regole stabilite in ISO/IEC 9594-8; 2) il blocco "
            "deve verificare che i certificati di attributo e le asserzioni firmate corrispondano effettivamente "
            "alle regole specificate nei vincoli di input; 3) se un controllo fallisce, il blocco deve restituire "
            "l'indicazione INDETERMINATE con la sotto-indicazione SIG_CONSTRAINTS_FAILURE con maggiori informazioni "
            "sul vincolo che non e' stato possibile verificare. Se le regole di firma non specificano regole per "
            "attributi certificati o asserzioni firmate, l'SVA deve rendere il valore di tale attributo o asserzione "
            "firmata disponibile al DA, perche' possa decidere un'elaborazione aggiuntiva adeguata, fuori "
            "dall'ambito del presente documento."
        ),
        "testo_integrale": """If the signature elements constraints define specific constraints for certified attributes and signed assertions:

1) The building block shall validate the attribute certificate(s) and signed assertions present in this property/attribute following the rules established in ISO/IEC 9594-8 [2].

2) The building block shall check that the attribute certificate(s) and signed assertions actually match the rules specified in the input constraints. And

3) If any check fails, the building block shall return the indication INDETERMINATE with the sub-indication SIG_CONSTRAINTS_FAILURE with more information on the constraint that could not be verified.

If the signature rules do not specify rules for certified attributes or signed assertions, the SVA shall make the value of such attribute or signed assertions available to the DA so that it can decide on additional suitable processing, which is out of the scope of the present document.""",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Prima parte: si applica se i signature elements constraints definiscono vincoli specifici per gli "
            "attributi certificati e le asserzioni firmate; la parte finale si applica quando le regole di firma non "
            "ne specificano."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 5.2.9 (Signature validation presentation building block)",
        "testo": (
            "La Signature Validation Presentation e' un elemento facoltativo del processo di convalida della firma, "
            "che un verificatore puo' usare per controllare i risultati di un processo di convalida. Quando presente, "
            "il blocco di presentazione della convalida della firma dovrebbe supportare: la presentazione dei dati "
            "(SD) coperti dalla firma; la presentazione delle informazioni che identificano il firmatario; la "
            "presentazione di data e ora in cui e' stato determinato lo stato di convalida; la presentazione di "
            "qualunque attributo di firma incluso nella firma, chiarendo quali attributi erano firmati e quali non "
            "firmati; l'indicazione chiara della Signature Validation Policy usata per la convalida; la "
            "presentazione dello stato complessivo della convalida (TOTAL-PASSED, TOTAL-FAILED, INDETERMINATE); in "
            "caso di TOTAL-FAILED la presentazione del motivo per cui la firma e' invalida; in caso di "
            "INDETERMINATE l'evidenziazione delle parti del rapporto di convalida che indicano i passi da compiere "
            "per arrivare potenzialmente a un risultato determinato; la presentazione del rapporto di convalida."
        ),
        "testo_integrale": """The Signature Validation Presentation is an optional element in the signature validation process that can be used by a verifier to check the results of a validation process. When present, the signature validation presentation building block should support:

• Presenting the data (SD) that has been covered by the signature.

• Presenting information identifying the signer.

• Presenting the date and time for which the validation status was determined.

• Presenting any signature attributes that have been included in the signature and make clear which attributes were signed and which were unsigned.

• Making clear which Signature Validation Policy has been used for validation.

• Presenting the overall status of the signature validation (TOTAL-PASSED, TOTAL-FAILED, INDETERMINATE).

• In case of TOTAL-FAILED: Presenting the reason for the signature being invalid.

• In case of INDETERMINATE: Highlighting the parts of the validation report that indicate steps to be taken to potentially get to a determinate result. And

• Presenting the validation report.""",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 5.2.1 (Description)",
        "testo": (
            "La clausola presenta i blocchi costitutivi di base usati per costruire gli algoritmi di convalida dei "
            "diversi scenari; la Figura 12 mostra in forma semplificata come tali blocchi si combinino per realizzare "
            "la convalida della firma, in stretta analogia con la convalida di base specificata nella clausola 5.3."
        ),
        "testo_integrale": """This clause presents basic building blocks that are used to construct validation algorithms for specific scenarios.
Figure 12 shows, in a simplified way, how these building blocks are related to achieve signature validation. It closely resembles the basic validation specified in clause 5.3.
Figure 12: Basic Signature Validation""",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.3.1 (Description)",
        "testo": (
            "Questo blocco costitutivo e' responsabile dell'identificazione del certificato di firma che sara' usato "
            "per convalidare la firma."
        ),
        "testo_integrale": """This building block is responsible for identifying the signing certificate that will be used to validate the signature.""",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.4.1 (Description)",
        "testo": (
            "Il blocco inizializza i vincoli di convalida (vincoli di validazione X.509, vincoli crittografici, "
            "vincoli sugli elementi della firma) e i parametri correlati (parametri di validazione X.509, inclusi i "
            "trust anchor e i certificate validation data) che saranno usati per convalidare la firma; vincoli e "
            "parametri sono inizializzati da una qualunque delle fonti elencate nella clausola 5.1.4."
        ),
        "testo_integrale": """This building block initializes the validation constraints (X.509 validation constraints, cryptographic constraints, signature elements constraints) and related parameters (X.509 validation parameters including trust anchors and certificate validation data) that will be used to validate the signature. The constraints and parameters are initialized from any of the sources listed in clause 5.1.4.""",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.5.1 (Description)",
        "testo": (
            "Il blocco verifica che una data informazione sullo stato di revoca sia \"fresh\" a un dato tempo di "
            "convalida: la freschezza richiesta dell'informazione sullo stato di revoca e' la differenza massima "
            "accettata tra il tempo di convalida e il tempo di emissione dell'informazione sullo stato di revoca; il "
            "processo e' usato dagli altri blocchi di convalida quando controllano lo stato di revoca di un "
            "certificato. Nota: cio' rileva quando la firma convalidata e' una firma di base senza marca temporale "
            "affidabile e il tempo dichiarato non e' considerato sufficiente, perche' la firma potrebbe essere stata "
            "creata poco prima della convalida senza che il momento esatto sia noto, e un'informazione di revoca "
            "troppo vecchia potrebbe non indicare una revoca avvenuta prima della creazione della firma; in pratica "
            "si usa informazione emessa poco prima del tempo corrente, approssimando che il suo contenuto sia ancora "
            "affidabile."
        ),
        "testo_integrale": """This building block checks that a given revocation status information is "fresh" at a given validation time. The required freshness of the revocation status information is the maximum accepted difference between the validation time and the issuance time of the revocation status information. This process is used by other validation blocks when checking the revocation status of a certificate.

NOTE: This is important when the signature that is being validated is a basic signature without trustworthy time assertion and the claimed time is not considered sufficient. In those cases, the signature might be created just before the validation, but the exact moment is not known. If the revocation status information is too old, the certificate might have been revoked before the signature creation, which is not indicated in the revocation status information. In practice, revocation status information that has been issued shortly before the current time is used and the approximation made that the information it contains is still reliable at the current time.""",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.7.1 (Description)",
        "testo": (
            "Il blocco verifica l'integrita' dei dati firmati eseguendo le verifiche crittografiche."
        ),
        "testo_integrale": """This building block checks the integrity of the signed data by performing the cryptographic verifications.""",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 5.2.8.1 (Description)",
        "testo": (
            "Il blocco copre verifiche aggiuntive da eseguire sulla firma stessa o sugli attributi della firma. "
            "Nota: il processo puo' includere anche altre verifiche imposte da una politica di convalida della "
            "firma; i controlli elencati o meno non sono comunque obbligatori da implementare per un SVA."
        ),
        "testo_integrale": """This building block covers additional verification to be performed on the signature itself or on the attributes of the signature.

NOTE: This process can also include other checks mandated by a signature validation policy. Checks, listed here or not, are not mandatory to be implemented by an SVA however.""",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 5.2.1 (Description)",
    "clausola 5.2.2.1 (Description)",
    "clausola 5.2.2.2 (Inputs)",
    "clausola 5.2.2.3 (Outputs)",
    "clausola 5.2.3.1 (Description)",
    "clausola 5.2.3.2 (Inputs)",
    "clausola 5.2.3.3 (Outputs)",
    "clausola 5.2.3.4 (Processing)",
    "clausola 5.2.4.1 (Description)",
    "clausola 5.2.4.2 (Inputs)",
    "clausola 5.2.4.3 (Outputs)",
    "clausola 5.2.4.4 (Processing)",
    "clausola 5.2.5.1 (Description)",
    "clausola 5.2.5.2 (Inputs)",
    "clausola 5.2.5.3 (Output)",
    "clausola 5.2.5.4 (Processing)",
    "clausola 5.2.6.1 (Description)",
    "clausola 5.2.6.2 (Inputs)",
    "clausola 5.2.6.3 (Outputs)",
    "clausola 5.2.6.4 (Processing)",
    "clausola 5.2.7.1 (Description)",
    "clausola 5.2.7.2 (Inputs)",
    "clausola 5.2.7.3 (Outputs)",
    "clausola 5.2.7.4 (Processing)",
    "clausola 5.2.8.1 (Description)",
    "clausola 5.2.8.2 (Inputs)",
    "clausola 5.2.8.3 (Outputs)",
    "clausola 5.2.8.4.1 (General requirements)",
    "clausola 5.2.8.4.2.1 (Processing signing certificate reference constraint)",
    "clausola 5.2.8.4.2.2 (Processing claimed signing time)",
    "clausola 5.2.8.4.2.3 (Processing Signed Data Object format)",
    "clausola 5.2.8.4.2.4 (Processing indication of production place of the signature)",
    "clausola 5.2.8.4.2.5 (Processing time-stamps on Signed Data Objects)",
    "clausola 5.2.8.4.2.6 (Processing countersignatures)",
    "clausola 5.2.8.4.2.7 (Processing signer attributes)",
    "clausola 5.2.9 (Signature validation presentation building block)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
