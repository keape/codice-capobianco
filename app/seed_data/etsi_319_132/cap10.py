"""ETSI EN 319 132-1 V1.3.1 (2024-07) - Electronic Signatures and Trust
Infrastructures (ESI); XAdES digital signatures; Part 1: Building blocks and
XAdES baseline signatures. Blocco B (famiglia AdES del lotto 2). Capitolo 10
dello split: Annex E (informative) "Change history", cioe' la tabella di
cronologia redazionale delle versioni del documento (Date / Version /
Information about changes). Conteggio di questo capitolo: 0 Obblighi, 1
Principio, 1 item di indice, 0 relazioni. Questo modulo e' puro dato: non
importa nulla, non legge file e NON tocca app/seed.py - la numerazione degli
id e' risolta per riferimento dalla sessione principale tramite
app/seed_data/lib.py, e le relazioni verso altri capitoli di questa fonte o
verso altre fonti le costruisce sempre la sessione principale (fase 6,
ADR-0009).

Nota sulla traccia di dispatch: il perimetro assegnato descrive l'Annex E come
"informative: esempi". Il testo ufficiale assegna all'Annex E di questo
documento il titolo "Change history" (e' l'Annex E di ETSI EN 319 122-1,
"Example Structured Contents and MIME", a contenere gli esempi, non questo
documento - si veda cap07 di quella fonte). La parte sostanziale della traccia
("tutti gli annessi presenti nel file, distinguendo i riferimenti per
annesso") e' stata applicata cosi' com'e': l'unico annesso presente in
cap10.txt e' l'Annex E (Change history) ed e' censito; la sezione "History"
con la tabella "Document history" che lo segue non e' un annesso ed e'
esclusa (vedi "Esclusioni"). Nessun annesso successivo esiste nel file: cap10
e' l'ultimo capitolo dello split e finisce con la sezione History.

Provenienza del testo
---------------------
- testo ufficiale: ETSI EN 319 132-1 V1.3.1 (2024-07), "Electronic Signatures
  and Trust Infrastructures (ESI); XAdES digital signatures; Part 1: Building
  blocks and XAdES baseline signatures", deliver "01.03.01_60", formato "PDF
  ETSI deliver (pdftotext -layout)".
- file di capitolo: app/.source_cache/etsi_319_132/cap10.txt (140 righe),
  porzione dello split deterministico di app/.source_cache/etsi_319_132/raw.txt
  descritto in app/.source_cache/etsi_319_132/manifest.json (capitolo "cap10",
  titolo "Annex E (informative):"); in raw.txt l'Annex E comincia a riga 4701
  ("Annex E (informative):", con "Change history" a riga 4702) e la sezione
  History a riga 4825.
- metadati da app/.source_cache/etsi_319_132/provenance.json: url
  https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf,
  versione "01.03.01_60", data_fetch 2026-09-29T12:56:34Z, sha256_raw_pdf
  83fc87ee09de90274131a1f60cb73edb742cebc7cd8961342586ed06133664c5 (stessa
  fonte di cap01-cap09 di questo standard).

Perimetro
---------
Dal titolo "Annex E (informative):" / "Change history" (righe 1-2 del file di
capitolo) fino all'ultima riga della tabella dell'Annex E ("Other minor
editorial changes.", che e' anche l'ultima riga della cella della versione
V1.2.8). Il file assegnato non contiene front matter, Contents, Foreword ne'
l'elenco dei riferimenti bibliografici: comincia con l'Annex E (a monte, in
raw.txt, c'e' la fine della clausola 6.4 piu' piede di pagina 75) e prosegue
con la sola sezione History, esclusa.

L'Annex E e' un annesso non suddiviso: non ha numerazione interna (nessun
E.1, E.2, ...), il suo contenuto e' interamente la tabella di cronologia a
tre colonne "Date | Version | Information about changes". Il file non contiene
altri annessi e nessun testo dello standard fuori dagli annessi.

Granularita' (ADR-0007, nessun discrimine di rilevanza)
------------------------------------------------------
1 item di indice -> 1 riga, 1:1. L'unita' di indice e' l'annesso nel suo
complesso, come per gli annessi non suddivisi gia' censiti in questo
censimento ("Annex D (Deprecated qualifying properties)" di questa stessa
fonte, cap09; "Annex F (Change History)" di ETSI EN 319 122-1, cap07 di quella
fonte).

Le 10 righe della tabella (una per versione: 1.1.1, 1.2.0, 1.2.1, 1.2.2a,
1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7, 1.2.8) NON generano un item ciascuna:
non sono unita' numerate del documento (nessuna compare nel Contents, che
elenca la sola voce "Annex E (informative): Change history", raw.txt riga
216), non hanno un id proprio (la chiave e' la coppia data+versione, non una
numerazione di clausola) e non portano alcun requisito da rendere
rintracciabile singolarmente. Stesso criterio gia' applicato alle righe di
cronologia dell'Annex F di ETSI EN 319 122-1 (un solo nodo per l'annesso).
Alternativa scartata: una riga per versione, che avrebbe creato 10 item di
indice inesistenti nel documento e 10 nodi il cui contenuto (data, versione,
nota redazionale) non ha ne' soggetto ne' effetto giuridico.

Intestazioni senza testo proprio -> nessun item a se' (stesso criterio delle
altre fonti ETSI censite): "Annex E (informative):" e "Change history" sono
titolazione dell'annesso, assorbita nella riga (riportata in testa al
`testo_integrale`); la riga di intestazione della tabella "Date | Version |
Information about changes" e' struttura della tabella stessa.

Obbligo o Principio
-------------------
RIGHE_OBBLIGHI e' vuoto e l'unica riga e' un Principio.

- Annex E (Change history) -> Principio "altro". Tabella di cronologia
  redazionale: nessun comportamento imposto a un soggetto identificabile,
  nessun effetto giuridico dichiarato. Il testo contiene una sola occorrenza
  di "shall" ed e' dentro una citazione di testo normativo ("...the following
  steps shall be performed:", il periodo che la V1.2.8 ha sostituito nella
  clausola 5.5.2.2) descritta come modifica storica, non una prescrizione del
  presente documento; l'unico altro verbo modale e' il "may have" descrittivo
  della clausola 5.4.1 introdotta dalla V1.2.6. Verificato sull'intero testo
  dell'annesso: nessun altro "shall"/"should". "altro" e non "definitorio":
  l'annesso non definisce termini usati altrove (i termini dello standard sono
  nella clausola 3.1, e le qualifying property nelle clausole 5.x/A.x). Non
  "scopo/ambito di applicazione": l'ambito del documento sta nella clausola 1.
  Nessuna delle quattro categorie sostanziali (non discriminazione, equivalenza
  giuridica, valore probatorio, presunzione legale) ha riscontro in una tabella
  di cronologia.

`stato` = "vigente": l'annesso e' parte della versione corrente del documento
(EN 319 132-1 V1.3.1, 2024-07); l'ultima riga della tabella e' la V1.3.1
pubblicata nel luglio 2024.

Nessun `soggetti`, nessun `oggetti_giuridici`, nessun `severita`, `sanzioni` o
`condizione_applicabilita` valorizzati: il testo nomina firme XAdES, qualifying
property (RenewedDigestsV2, RenewedDigests, AnyValidationData,
AllDataObjectsTimeStamp, IndividualDataObjectsTimeStamp, ArchiveTimeStamp,
DataObjectFormat, ValidationValuesForAll), validation data, marche temporali e
versioni del documento, mai una delle quattro categorie di soggetto censite
("QTSP/gestore", "Utente/titolare", "Terza parte", "Terzi affidanti/pubblico")
ne' un oggetto giuridico della tassonomia eIDAS. Il documento non prevede
sanzioni.

Completezza verbatim (ADR-0010)
-------------------------------
`testo_integrale` riporta il testo ufficiale per intero, senza elisioni,
riassunti o tagli. Convenzioni di ricostruzione applicate:

- la tabella e' resa una riga per ogni riga di versione del documento, nella
  forma "Data | Version | Information about changes", con le righe di cella
  spezzate dalla conversione PDF ricucite in un periodo continuo e i punti
  elenco (carattere "•" del testo ufficiale) mantenuti come voci separate
  introdotte da " • ";
- la colonna delle etichette (Data, Version) e' centrata verticalmente nel PDF
  rispetto alla cella di testo: pdftotext -layout stampa percio' l'etichetta a
  meta' del blocco di testo che le appartiene (es. "June 2021 1.2.0" in mezzo
  all'elenco puntato che le appartiene, "October 2023 1.2.6" dentro il
  capoverso della clausola 5.4.1). L'attribuzione di ogni capoverso alla riga
  di versione giusta NON e' stata dedotta dall'ordine di stampa ma verificata
  sui bordi di riga della tabella nel PDF ufficiale (coordinate delle linee di
  separazione estratte da raw.pdf): l'assegnazione di "Below is a
  non-exhaustive list..." e dei suoi 11 punti alla riga V1.2.0 (June 2021),
  di "Other editoral issues spotted in the comments to version 1.2.3" alla
  riga V1.2.4, di "Fix references in additional requirements p), r), t), and
  w)..." alla riga V1.2.5, di "Clause 5.4 Qualifying properties for validation
  data values..." alla riga V1.2.6 e di "Clause 5.5.2.2 Replacement of
  sentence: ..." alla riga V1.2.8 e' quella dei riquadri della tabella;
- la riga V1.2.6 attraversa il salto di pagina tra pagina 75 e pagina 76 del
  PDF: il testo prosegue nella pagina successiva sotto la riga di intestazione
  ripetuta, senza ripetizione dell'etichetta data/versione (il riquadro di
  pagina 76 che porta quel testo e' privo di etichetta e non esiste alcuna
  versione del documento senza data). Nella resa e' ricomposta in un'unica
  riga (V1.2.6), e non spezzata in due voci. Riscontro incrociato
  sull'attribuzione: la V1.2.7 reinserisce esattamente il testo che la V1.2.6
  dichiara di aver eliminato dalla clausola 5.5.2.1 ("Deleted text requiring
  to incorporate all the validation data for counter-signature" -> "Reinserted
  text requiring to incorporate all the validation data for counter-signature
  ... for keeping backwards compatibility"), il che conferma che quel blocco
  appartiene alla V1.2.6;
- righe di testa/piede di pagina rimosse: "ETSI", "75 ETSI EN 319 132-1 V1.3.1
  (2024-07)", "76 ETSI EN 319 132-1 V1.3.1 (2024-07)" e relativo "ETSI" a
  pie' di pagina, righe vuote di impaginazione, e l'intestazione di tabella
  "Date Version Information about changes" ripetuta a pagina 76 (resa una sola
  volta);
- parole spezzate a fine riga: l'unico trattino a fine riga della cella V1.2.6
  ("electronic time-" + "stamp(s)") fa parte della parola del testo ufficiale
  ("time-stamp(s)") e la ricucitura lo mantiene.

Peculiarita' del testo ufficiale riportate come stanno (nessuna correzione
silenziosa, perche' `testo_integrale` e' verbatim):
- "certifcates" (V1.2.6), per "certificates";
- "Other editoral issues" (V1.2.4), per "editorial", senza punto finale;
- "Reinserted text requiring to requiring to incorporate" (V1.2.7),
  ripetizione presente nel documento;
- spazio prima del due punti in "on the content of AnyValidationData : the
  former" (V1.2.5);
- "v.1.1.1" e "N+1th" come stampati (V1.2.6);
- nell'impaginazione ufficiale il capoverso di V1.2.8 che sostituisce la
  frase e' introdotto dalla parola "By" su riga propria, fra le due frasi
  virgolettate (nella resa a una riga per versione il "By" resta in sequenza,
  fra le due frasi).

Rinvii demandati alla fase 6 (nessuna relazione creata qui)
-----------------------------------------------------------
`RELAZIONI` e' vuoto: il capitolo ha una sola riga, quindi nessun bersaglio
interno possibile. Le citazioni elencate qui sotto stanno tutte dentro il
`testo_integrale` dell'Annex E e sono menzioni storiche (descrivono modifiche
gia' apportate alle clausole), non rinvii normativi dell'annesso: la fase 6
decidera' se e come modellarle, verosimilmente senza arco, perche' un annesso
di cronologia non rinvia a nulla da applicare. Elenco completo per la fase 6:

- clausole di questa stessa Fonte (capitoli 1-7 dello split): 5.1.4.3
  ("Unambiguous wording in clause 5.1.4.3"), 5.2.4 (DataObjectFormat
  qualifying property), 5.2.8.1 (AllDataObjectsTimeStamp), 5.2.8.2
  (IndividualDataObjectsTimeStamp), 5.5.2.1 (Semantics and syntax of
  ArchiveTimeStamp), 5.5.2.2 (Generation and incorporation of
  ArchiveTimeStamp), 5.5.3 (RenewedDigestsV2 e digest rinnovati), 6
  (requisiti di cardinalita' di AnyValidationData), 6.3 (requisiti su
  RenewedDigestsV2 nelle firme XAdES baseline; livello B-LTA), 5.4 e 5.4.1
  (Qualifying Properties for validation data values / Introduction);
- Annex A (normativo) di questa stessa Fonte, capitolo 8 dello split: "clause
  A.2" (nuova clausola sulle qualifying property deprecate introdotta dalla
  V1.2.0);
- fonti esterne: ETSI TS 103 171 (V2.1.1) (definizione di Legacy XAdES
  baseline signature), IETF RFC 2045 (MIME Part One; la V1.2.0 cita
  esplicitamente un riferimento normativo aggiunto), IETF RFC 3161 (electronic
  time-stamps), XAdES-B-LTA (livello definito nella clausola 6, cap07 dello
  split).

Esclusioni
----------
Nessun nodo e nessun item di indice per:

- la sezione "History" con la tabella "Document history" (raw.txt righe
  4825-4835; cap10.txt righe 125-135), colonne Versione / Data / Informazioni: V1.0.1 July 2015 "Publication as ETSI TS 119 132-1
  (Withdrawn)", V1.1.1 April 2016 "Publication", V1.2.1 February 2022
  "Publication", V1.3.0 April 2024 "EN Approval Procedure - AP 20240723:
  2024-04-24 to 2024-07-23", V1.3.1 July 2024 "Publication". E' paratesto
  editoriale (storico delle pubblicazioni ETSI dell'EN), non un annesso: nel
  Contents compare come voce di primo livello a se' ("History", raw.txt riga
  217), non porta numero di annesso e non ha il titolo "Annex". Stessa
  convenzione gia' applicata alla sezione History di ETSI EN 319 122-1 (cap07
  di quella fonte) e delle altre fonti ETSI censite;
- il front matter, il Contents, la Foreword e l'elenco dei riferimenti
  bibliografici dello standard: non presenti in questo file di capitolo (sono
  a monte, in cap01 e nei capitoli precedenti dello split);
- righe di testa/piede di pagina e righe vuote di impaginazione (elencate
  sopra in "Completezza verbatim").

DUBBIO DI CLASSIFICAZIONE APERTO per la revisione umana, sul confine adottato
fra annesso e paratesto: qui l'Annex E (cronologia delle modifiche) e'
censito, perche' e' un annesso reale del documento (voce del Contents con
propria numerazione di annesso) e ADR-0007 vieta ogni discrimine di rilevanza;
la sezione History resta fuori, perche' non e' un annesso. Altri batch di
questo censimento hanno dato istruzione opposta per il blocco "Change
history"/"History" (ETSI EN 319 431-1, EN 319 431-2, TS 119 461, TS 119 432,
EN 319 102-1), escludendolo in blocco come paratesto editoriale; se la
revisione preferisse quella convenzione, la riga "Annex E (Change history)" va
rimossa insieme al suo item di indice (resterebbero 0 item e 0 righe); se
invece preferisse includere anche la tabella delle pubblicazioni ETSI, andrebbe
aggiunta una seconda riga (Principio "altro", riferimento "History (Document
history)") con il proprio item di indice. Entrambe le alternative sono
deliberate e non silenziose: la scelta di questo modulo e' la prima (annesso
censito, History esclusa), identica a quella gia' presa per ETSI EN 319 122-1
cap07.

Conteggio finale: 1 item di indice, 1 riga: 0 obblighi + 1 principio, 0
relazioni interne.
"""

RIGHE_OBBLIGHI: list[dict] = []

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "Annex E (Change history)",
        "testo": (
            "Annesso informativo con la cronologia redazionale delle modifiche del documento: "
            "per ciascuna versione (1.1.1, 1.2.0, 1.2.1, 1.2.2a, 1.2.3, 1.2.4, 1.2.5, 1.2.6, "
            "1.2.7, 1.2.8) la data e l'elenco dei cambiamenti apportati (aggiunta di "
            "riferimenti normativi, rinominazioni di qualifying property - RenewedDigestsV2, "
            "RenewedDigests, AnyValidationData - regole di incorporazione della "
            "ArchiveTimeStamp e delle validation data, requisiti di cardinalita', rubriche di "
            "clausola riviste e refusi editoriali). Non contiene requisiti propri ne' effetti "
            "giuridici: e' cronologia redazionale, censita per copertura completa degli "
            "annessi del capitolo assegnato."
        ),
        "testo_integrale": (
            """Annex E (informative): Change history

Date | Version | Information about changes
April 2016 | 1.1.1 | Publication.
June 2021 | 1.2.0 | Below is a non-exhaustive list of the changes carried out since V1.1.1. • Added normative reference to IETF RFC 2045: "Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies". • Redefinition of Legacy XAdES baseline signature: is a signature compliant with ETSI TS 103 171 (V2.1.1) (note the restriction to a specific version). • Unambiguous wording in clause 5.1.4.3. Now it clearly states that the IETF RFC 3161 electronic time-stamps are instance of TimeStampToken type, that this element allows encapsulating XML electronic time-stamps and other formats of electronic time-stamps. • Clarifies that the mime type in a DataObjectFormat qualifying property is a string containing values defined in IETF RFC 2045 (clause 5.2.4). • Clarifies the message imprint computation process for AllDataObjectsTimeStamp qualifying property (clause 5.2.8.1). • Clarifies the message imprint computation process for IndividualDataObjectsTimeStamp qualifying property (clause 5.2.8.2). • Clarifies when to incorporate a new RenewedDigestsV2 qualifying property in the context of adding a new ArchiveTimeStamp qualifying property (text in clause 5.5.2.2). • Clarifies the message imprint computation process for ArchiveTimeStamp qualifying property (clause 5.5.2.2). • Defines the new RenewedDigestsV2 qualifying property, which deprecates the RenewedDigests qualifying property. This new property incorporates a better mechanism for identifying the renewed digest values. Which work in complex frameworks of indirectly signed data objects (clause 5.5.3). • Defines requirements to be met by the new RenewedDigestsV2 qualifying property in XAdES baseline signatures (clause 6.3). • Adds a new clause on deprecated qualifying properties because the RenewedDigestsV2 qualifying property deprecates RenewedDigests qualifying property (clause A.2).
February 2022 | 1.2.1 | Publication
April 2023 | 1.2.2a | Incorporated ValidationValuesForAll unsigned qualifying property for having a component for placing validation material for validating any signature present within XAdES.
April 2023 | 1.2.3 | Renamed ValidationValuesForAll unsigned qualifying property to AnyValidationData. Reworked clauses on generation of message imprint computation input for archive electronic time-stamps taking into account AnyValidationData. Specification of requirements of cardinality for AnyValidationData in clause 6.
September 2023 | 1.2.4 | Reformulation of the process for generating and incorporating a new ArchiveTimeStamp. Reformulation of the process for computing the corresponding message imprint when the ArchiveTimeStamp is created and incorporated, and when this same ArchiveTimeStamp is being validated. Modification of AnyValidationData specification for banning the presence of the URI attribute. Other editoral issues spotted in the comments to version 1.2.3
September 2023 | 1.2.5 | Reformulation of requirements on the content of AnyValidationData : the former formulation could be interpreted as if both certificates and revocation data must be present. The presence of certificates and/or revocation data will depend on the contents of the rest of XAdES signature. This new reformulation makes it clear that this qualifying property must contain certificates, or revocation data, or both of them. Fix references in additional requirements p), r), t), and w) so that their text reference the right steps in clause 5.5.2.2.
October 2023 | 1.2.6 | Clause 5.4 Qualifying Properties for validation data values. Added new clause 5.4.1 Introduction for stating that a XAdES signature may have certifcates and/or revocation data in any of the qualifying properties specified within 5.4. Clause 5.5.2.1 Semantics and syntax (of ArchiveTimeStamp) Deleted text requiring to incorporate all the validation data for counter-signature before adding the archive time-stamp. This is not mandatory in general. It is made mandatory for B-LTA level in clause 6.3. Clause 5.5.2.2 Generation and incorporation of ArchiveTimeStamp Changed the rules for the incorporation of validation material before incorporating the new ArchiveTimeStamp as follows: For first ArchiveTimeStamp: incorporation of validation data is now optional. For N+1th ArchiveTimeStamp: mandatory to incorporate all missing validation data required for validating all signed data time-stamped by electronic time-stamp(s) in Nth ArchiveTimeStamp. Validation data in any of the qualifying properties specified in clause 5.4. NOTE noting that these requirements can be changed in the specifications of levels. Also remarks that the XAdES-B-LTA level requirements have not changed since v.1.1.1. Dropped the paragraphs discussing the details of the incorporation of validation material to each qualifying property specified in clause 5.4. Editorial changes for improving sentences and fixing typos.
December 2023 | 1.2.7 | Clause 5.5.2.1 Semantics and syntax (of ArchiveTimeStamp) Reinserted text requiring to incorporate all the validation data for counter-signature before adding the archive time-stamp for keeping backwards compatibility. Clause 5.5.2.2 Generation and incorporation of ArchiveTimeStamp Reinserted text requiring to requiring to incorporate all the validation data for any signed data object within XAdES signature before adding the archive time-stamp for keeping backwards compatibility.
January 2024 | 1.2.8 | Clause 5.5.2.2 Replacement of sentence: "The present clause describes the steps to perform for augmenting a XAdES signature by incorporation of a new ArchiveTimeStamp qualifying property." By "For augmenting a XAdES signature by incorporation of a new ArchiveTimeStamp qualifying property, the following steps shall be performed:" Other minor editorial changes."""
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "Annex E (Change history)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Nessuna relazione interna: il capitolo ha una sola riga, quindi non esiste
# alcun bersaglio dichiarato in questo modulo. Le citazioni presenti nel testo
# dell'Annex E (clausole 5.1.4.3, 5.2.4, 5.2.8.1, 5.2.8.2, 5.4, 5.4.1, 5.5.2.1,
# 5.5.2.2, 5.5.3, 6, 6.3 di questa Fonte, Annex A.2 del capitolo 8, e le fonti
# esterne ETSI TS 103 171 (V2.1.1), IETF RFC 2045, IETF RFC 3161, XAdES-B-LTA)
# sono menzioni storiche dentro la tabella di cronologia, non rinvii normativi
# di questo annesso: restano elencate nel docstring e demandate alla fase 6
# (ADR-0009), che decide se e come modellarle.
RELAZIONI: list[dict] = []
