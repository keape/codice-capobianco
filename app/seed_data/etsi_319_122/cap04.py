"""ETSI EN 319 122-1 V1.3.1 (2023-06) - Electronic Signatures and Trust
Infrastructures (ESI); CAdES baseline signatures. Capitolo 4 dello split:
clausola 6 (CAdES baseline signatures), sottoclausole 6.1 (Signature levels),
6.2.1 (Algorithm requirements), 6.2.2 (Notation for requirements), 6.3
(Requirements on components and services) e 6.4 (Legacy CAdES baseline
signatures).

Provenienza del testo: app/.source_cache/etsi_319_122/cap04.txt (porzione
dello split deterministico; testo ufficiale completo in
app/.source_cache/etsi_319_122/raw.txt, raw_body.txt e raw.pdf). Versione
ETSI EN 319 122-1 V1.3.1 (2023-06), deliver "01.03.01_60"; da
app/.source_cache/etsi_319_122/provenance.json: data_fetch
2026-09-29T12:56:34Z, sha256_raw_pdf
e99e76e519d9bd8e1410775bccedb1a588021e5e7c705c9fcc1f91c6a6227c21, formato
"PDF ETSI deliver (pdftotext -layout)". Manifest di split:
app/.source_cache/etsi_319_122/manifest.json. Questo modulo e' puro dato: non
importa nulla e non legge file; la numerazione degli id e' risolta per
riferimento dalla sessione principale in app/seed.py (che questo modulo NON
tocca).

## Granularita' (ADR-0007)

Il capitolo NON usa identificatori di requisito nella forma
<SIGLA>-<clausola>-<NN> (REQ-x.y-nn, OVR-x.y-nn, GEN-x.y-nn): le unita'
numerate con contenuto proprio sono le clausole 6.1, 6.2.1, 6.2.2, 6.3 e
6.4, piu' i 20 requisiti aggiuntivi della clausola 6.3 etichettati con le
lettere a)-t).

Decisione: 25 item di indice = 5 sottoclausole + 20 requisiti aggiuntivi (un
id = una riga). Le lettere a)-t) NON sono un elenco di dettaglio interno a
un requisito: sono i requisiti stessi, numerati dal documento e usati come
indice dalla colonna "Additional requirements and notes" della Tabella 1
(clausola 6.2.2, punto 8: "This cell contains numbers referencing notes
and/or letters referencing additional requirements on the attribute or the
signature field. Both notes and additional requirements are listed below
table 1."). Ciascuna lettera ha un soggetto esplicito ("the generator") e un
verbo deontico proprio, quindi e' un'unita' di prescrizione autonoma.

Le righe della Tabella 1 NON sono item di indice a se': non hanno un id
proprio (la loro identita' e' il nome dell'attributo, del campo di firma o
del servizio) e il loro contenuto prescrittivo per livello e' indicizzato dal
documento attraverso le lettere dei requisiti aggiuntivi; la tabella resta
quindi contenuto del nodo della clausola 6.3, come da criterio gia' applicato
alle tabelle di ETSI TS 119 312 (cap02/cap04) e di ETSI EN 319 102-1
(clausola 5.1.3, tabelle 5-7 nello stesso nodo).
Alternativa scartata: un unico nodo per l'intera clausola 6.3 (paragrafo
introduttivo + NOTE 1-8 + Tabella 1 + lettere a)-t)). Avrebbe reso non
rintracciabili singolarmente 20 prescrizioni che il documento stesso numera e
che la tabella cita una per una, e avrebbe prodotto un nodo di oltre 10 KB
con prescrizioni di tipo diverso (ricostruzione del percorso di
certificazione, protezione dell'algoritmo di hash, dati di revoca, archiviazione
a lungo termine).

Intestazioni senza contenuto proprio -> nessun nodo, nessun item: "6 CAdES
baseline signatures" (titolo della clausola) e "6.2 General requirements"
(seguito immediatamente dal titolo 6.2.1). Stesso criterio delle intestazioni
di raggruppamento delle altre fonti ETSI censite (ETSI TS 119 312 clausole
5/5.2/6/6.2/6.2.2/6.4, ETSI EN 319 401 clausola 6, ETSI EN 319 411-2
clausola 7).

## Obbligo o Principio, riga per riga

- 6.1 (Signature levels) -> Principio "definitorio". Disposizione
  dichiarativa: definisce i quattro livelli CAdES baseline (B-B, B-T, B-LT,
  B-LTA) e la finalita' di ciascuno, senza imporre alcun comportamento a un
  soggetto; le NOTE 1-4 (informative, sul ciclo di vita della firma, sui casi
  d'uso dei livelli c) e d), sulla disponibilita'/integrita' a lungo termine
  e sul rapporto con altre tecniche di conservazione) restano nel nodo, come
  da convenzione gia' adottata per le NOTE informative interne a una clausola
  (ETSI TS 119 312 cap04).
- 6.2.1 (Algorithm requirements) -> Obbligo "tecnico/sicurezza". La
  sottoclausola contiene una raccomandazione ("should be as specified in ETSI
  TS 119 312 [i.8]") e un divieto secco ("MD5 algorithm shall not be used as
  digest algorithm"): la clausola e' indivisibile ai fini dell'indice (una
  sola sottoclausola numerata), quindi un solo nodo Obbligo, con il verbo
  modale conservato nel `testo`. La NOTE bibliografica interna (le
  raccomandazioni di ETSI TS 119 312 possono essere superate da
  raccomandazioni nazionali) e' mantenuta in `testo_integrale` perche'
  aggiunge contenuto interpretativo, non e' mera citazione.
- 6.2.2 (Notation for requirements) -> Principio "definitorio". Definisce la
  notazione della Tabella 1: il significato delle 8 colonne, i valori ammessi
  nelle colonne di presenza ("shall be present", "shall not be present", "may
  be present", "shall be provided", "conditioned presence", "*"), i valori di
  cardinalita' (0, 1, 0 o 1, maggiore o uguale a 0, maggiore o uguale a 1) e
  un EXAMPLE di lettura della tabella. I "shall" che vi compaiono sono la
  definizione del significato dei valori di notazione, non prescrizioni
  autonome su un soggetto: nessun comportamento e' imposto qui (i
  comportamenti sono nelle righe della Tabella 1 e nei requisiti a)-t), nodi
  separati).
- 6.3 (Requirements on components and services) -> Obbligo
  "tecnico/sicurezza": la Tabella 1 fissa presenza e cardinalita' obbligatorie
  di ciascun attributo, campo di firma e servizio per i quattro livelli
  ("shall be present", "shall not be present", "shall be provided",
  "conditioned presence", "*"), collegando ogni riga alla clausola che
  definisce l'elemento e alle lettere dei requisiti aggiuntivi.
- a)-t) (Additional requirements) -> 20 Obblighi "tecnico/sicurezza". Ogni
  lettera nomina l'elemento a cui si riferisce ("Requirement for
  SignedData.certificates", "Requirement for signature-time-stamp", ...) e
  prescrive al generatore della firma come costruire o aumentare la firma
  CAdES (inclusione di certificati e dati di revoca, codifica DER, uso di
  ESS signing-certificate/v2, migrazione da SHA-1, protezione
  dell'algoritmo di hash, materiale di validazione per archive-time-stamp-v3,
  tipo dei dati firmati).
- 6.4 (Legacy CAdES baseline signatures) -> Obbligo "tecnico/sicurezza" con
  `condizione_applicabilita`: la clausola si applica quando nuovi attributi
  non firmati vengono incorporati in firme CAdES baseline legacy, che devono
  risultare conformi al presente documento.

Modulazione deontica: i requisiti con "should"/"may" (b), c), e), g), j), p),
piu' la facolta' di k) e la raccomandazione di 6.2.1) restano Obblighi, non
Principi: il censimento non ha un tipo di obbligo "raccomandazione" e nessuna
delle categorie di `tipo_principio` descrive una raccomandazione operativa
rivolta a un soggetto identificabile; la forza deontica resta nel campo
`testo` ("dovrebbe"/"puo'") e in `testo_integrale` resta il testo ufficiale.
Precedenti in questo senso: ETSI EN 319 401 (ogni requisito numerato ->
Obbligo, indipendentemente dal verbo modale) ed ETSI EN 319 102-1 cap03 (i
"should"/"may" restano nella riga Obbligo della clausola). Precedente di
segno opposto, non seguito qui: ETSI EN 319 411-1 cap04, dove i "should" a
livello di id di requisito generano Principi "altro".
DUBBIO DI CLASSIFICAZIONE APERTO per la revisione umana: b), c), e), g), j),
p) sono i sei requisiti in cui l'unico verbo modale e' "should"/"should not";
se la revisione preferisse la convenzione di ETSI EN 319 411-1 andrebbero
riclassificati come Principi "altro" (la sostanza del testo non cambia).

Soggetti: il soggetto grammaticale dei requisiti e' "the generator" (chi
genera o aumenta la firma: firmatario / applicazione di creazione della
firma) -> categoria "Utente/titolare", ruolo "obbligato". Convenzione
analoga a quella con cui ETSI EN 319 102-1 cap03 ha mappato "the SVA" su
"Terza parte" (li' il lato e' quello del verificatore, qui quello del
firmatario). I requisiti b) e c) nominano espressamente i "verifiers" come
destinatari dell'inclusione dei certificati -> aggiunta "Terza parte",
ruolo "destinatario". Nel nodo 6.3 la prosa della clausola non enuncia un
soggetto grammaticale (la tabella dice "shall be present"/"shall not be
present" degli elementi della firma): il soggetto e' comunque registrato
come "Utente/titolare"/"obbligato" perche' le prescrizioni di presenza e
cardinalita' vincolano chi genera la firma, nominato nei requisiti
addizionali della stessa clausola a)-t).
Nessun `oggetti_giuridici` valorizzato: il testo nomina "CAdES baseline
signatures" e attributi CMS, mai firma/sigillo qualificato o altro oggetto
dello schema (l'oggetto_giuridico ammette solo valori enumerati dal
censimento e va dichiarato solo se il testo lo nomina davvero).

## Fedelta' dell'estrazione

- Tabella 1: `pdftotext -layout` spezza ogni record su piu' righe e
  disallinea le colonne (le celle lunghe traboccano nella colonna adiacente,
  le celle corte vanno a capo). Ricostruzione: una riga per record, colonne
  separate da " | ", zero celle riscritte o abbreviate. Riportati come nel
  testo ufficiale, senza correzioni: la cella "References" vuota della riga
  "Service: revocation values in long-term validation"; la spaziatura
  irregolare di due celle di cardinalita' ("B-B, B-T : 0 or 1" e "B=LT,
  B=LTA: 0", refuso del documento); la cella "Additional requirements and
  notes" della riga SignedData.certificates, ricucita da due righe ("a, b, c,
  d, e" + "2, 3, 4"); la cella "t, 6,7" della riga "Service: identifying the
  signed data type" (spaziatura come nel testo). Le intestazioni di colonna
  ripetute in testa a ogni pagina della tabella sono riportate una sola
  volta, in testa alla tabella.
- NOTE: le NOTE 1-4 (in 6.1), la NOTE di 6.2.1 e le NOTE 2-8 (in 6.3) sono
  mantenute per intero in `testo_integrale`. Le NOTE 2-8 annotano righe della
  Tabella 1 (non singole lettere) e quindi vivono nel nodo della clausola
  6.3, benche' il testo ufficiale le collochi dopo i requisiti addizionali
  a)-t): il nodo 6.3 riporta percio' la rubrica "Additional requirements:"
  (l'etichetta del blocco i cui item sono i nodi a)-t) di questo modulo) e
  subito dopo le NOTE 2-8, che sono apparato della tabella. Nessuna NOTA e'
  stata spostata o duplicata in un nodo a)-t).
- Paratesto escluso: piede di pagina "ETSI", testatina "ETSI EN 319 122-1
  V1.3.1 (2023-06)", numeri di pagina 33-39, righe vuote di impaginazione.
- Nessun front matter, Contents, Foreword, References (clausola 2), History o
  sezione di bibliografia ricade nel file assegnato: cap04.txt comincia con
  il titolo della clausola 6 e termina con la clausola 6.4. Nessuna tabella
  di soli riferimenti bibliografici nel perimetro.

## Rinvii demandati alla fase 6 (nessuna relazione creata qui)

- 6.2.2 rinvia a "table 1", che e' contenuta nel nodo della clausola 6.3 di
  questo stesso modulo: bersaglio-tabella (non un nodo di prescrizione, non
  una partizione ex ADR-0012), quindi nessun arco; la citazione e' comunque
  interna a questo modulo e verificabile nel `testo_integrale` di 6.2.2.
- Rinvii ad altre parti del presente documento (capitoli coperti da altri
  moduli dello split): f), l) e n) -> clausole 4.2, 4.7.1, 5.2.6.1; 6.1 ->
  Annex B; colonna "References" della Tabella 1 -> clausole 4.4, 5.1.1,
  5.1.2, 5.2.1, 5.2.2, 5.2.2.2, 5.2.2.3, 5.2.3, 5.2.4, 5.2.4.1, 5.2.4.2,
  5.2.5, 5.2.6.1, 5.2.7, 5.2.8, 5.2.9.1, 5.2.10, 5.2.11, 5.2.12, 5.2.13,
  5.3, 5.5.3, A.1.1.1, A.1.1.2, A.1.2.1, A.1.2.2, A.1.3, A.1.4, A.1.5.1,
  A.1.5.2.
- Rinvii ad altre fonti (collegamento cross-fonte, ADR-0009): ETSI TS 119 312
  [i.8] (6.2.1 e j)), ETSI TR 119 100 [i.4] e ETSI TS 119 511 [i.20] e IETF
  RFC 4998 [i.15] (NOTE 1 e NOTE 4 di 6.1), ETSI TS 119 612 [i.11] (c)),
  IETF RFC 5940 [13] (r)), riferimenti [6] CRL e [14] OCSP (o), q), r)),
  CD 2009/767/EC [i.12] modificata da CD 2010/425/EU (NOTE 3), IETF RFC
  [i.21]/[i.22] (NOTE 8).

## Relazioni dichiarate

Le 20 relazioni sono i rinvii interni della Tabella 1 ai requisiti
addizionali della stessa clausola, letti nella colonna "Additional
requirements and notes" (es. riga "signature-time-stamp ... l, m, 5"; riga
"SignedData.certificates ... a, b, c, d, e 2, 3, 4"; riga "Service:
identifying the signed data type ... t, 6,7"). `nodo_da` = nodo della
clausola 6.3, `nodo_a` = singolo requisito addizionale, `tipo_relazione`
"richiama" (rinvio/citazione esplicita di un nodo verso un altro, CONTEXT.md),
`evidence_type` "textual" (la lettera compare letteralmente nel
`testo_integrale` del nodo citante, nella cella della tabella), `confidence`
None (nessuno score reale, ADR-0005). Una relazione per lettera: la dedup
evita archi multipli quando la stessa lettera compare in piu' righe della
tabella (g in tre righe, j e n in due). Nessuna relazione verso altri
capitoli di questa fonte ne' verso altre fonti: le partizioni e i
collegamenti cross-fonte sono costruiti dalla sessione principale in fase 6
(ADR-0012, ADR-0009).

## Copertura

25 item di indice, 25 righe: 23 obblighi + 2 principi.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "clausola 6.2.1 (Algorithm requirements)",
        "testo": (
            "Gli algoritmi e le lunghezze di chiave usati per generare e per aumentare le firme "
            "digitali dovrebbero essere quelli specificati in ETSI TS 119 312 [i.8]; l'algoritmo MD5 "
            "non deve essere usato come algoritmo di digest."
        ),
        "testo_integrale": (
            """6.2.1 Algorithm requirements: The algorithms and key lengths used to generate and augment digital signatures should be as specified in ETSI TS 119 312 [i.8].

NOTE: Cryptographic suites recommendations defined in ETSI TS 119 312 [i.8] can be superseded by national recommendations.

In addition, MD5 algorithm shall not be used as digest algorithm."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3 (Requirements on components and services)",
        "testo": (
            "La Tabella 1 fissa, per le firme CAdES-B-B, CAdES-B-T, CAdES-B-LT e CAdES-B-LTA, la "
            "presenza e la cardinalita' di ciascun attributo, campo di firma e servizio elencato nella "
            "prima colonna (ciascuna riga rinvia alla clausola che definisce l'elemento e alle lettere "
            "dei requisiti aggiuntivi che lo dettagliano); i requisiti aggiuntivi a)-t) sono riportati "
            "sotto la tabella e le NOTE 2-8 annotano singole righe o elementi della tabella."
        ),
        "testo_integrale": (
            """6.3 Requirements on components and services: Table 1 shows the presence and cardinality requirements on the attributes, signature fields, and services indicated in the first column for the four CAdES baseline signature levels, namely: CAdES-B-B, CAdES-B-T, CAdES-B-LT and CAdES-B-LTA. Additional requirements are detailed below the table suitably labelled with the letter indicated in the last column.

NOTE 1: CAdES-B-B signatures that incorporate only the elements/qualifying properties that are mandatory in table 1, and that implement the mandatory requirements, contain the lowest number of elements/qualifying properties, with the consequent benefits for interoperability.

Table 1: Requirements for CAdES-B-B, CAdES-B-T, CAdES-B-LT and CAdES-B-LTA signatures

Signature fields / Attributes / Services | Presence in B-B level | Presence in B-T level | Presence in B-LT level | Presence in B-LTA level | Cardinality | References | Additional requirements and notes
SignedData.certificates | shall be present | shall be present | shall be present | shall be present | 1 | Clause 4.4 | a, b, c, d, e 2, 3, 4
content-type | shall be present | shall be present | shall be present | shall be present | 1 | Clause 5.1.1 | f
message-digest | shall be present | shall be present | shall be present | shall be present | 1 | Clause 5.1.2 |
Service: protection of signing certificate | shall be provided | shall be provided | shall be provided | shall be provided | 1 | Clause 5.2.2 |
SPO: ESS signing-certificate | conditioned presence | conditioned presence | conditioned presence | conditioned presence | 0 or 1 | Clause 5.2.2.2 | g, h, j
SPO: ESS signing-certificate-v2 | conditioned presence | conditioned presence | conditioned presence | conditioned presence | 0 or 1 | Clause 5.2.2.3 | g, i, j
signing-time | shall be present | shall be present | shall be present | shall be present | 1 | Clause 5.2.1 |
commitment-type-indication | may be present | may be present | may be present | may be present | 0 or 1 | Clause 5.2.3 |
Service: identifying the signed data type | should be present | should be present | should be present | should be present | 0 or 1 | Clause 5.2.4 | t, 6,7
SPO: content-hints | conditioned presence | conditioned presence | conditioned presence | conditioned presence | 0 or 1 | Clause 5.2.4.1 |
SPO: mime-type | conditioned presence | conditioned presence | conditioned presence | conditioned presence | 0 or 1 | Clause 5.2.4.2 |
signer-location | may be present | may be present | may be present | may be present | 0 or 1 | Clause 5.2.5 |
signer-attributes-v2 | may be present | may be present | may be present | may be present | 0 or 1 | Clause 5.2.6.1 |
countersignature | may be present | may be present | may be present | may be present | ≥0 | Clause 5.2.7 |
content-time-stamp | may be present | may be present | may be present | may be present | ≥0 | Clause 5.2.8 | 5
signature-policy-identifier | may be present | may be present | may be present | may be present | 0 or 1 | Clause 5.2.9.1 |
signature-policy-store | conditioned presence | conditioned presence | conditioned presence | conditioned presence | 0 or 1 | Clause 5.2.10 | k
content-reference | may be present | may be present | may be present | may be present | 0 or 1 | Clause 5.2.11 |
content-identifier | may be present | may be present | may be present | may be present | 0 or 1 | Clause 5.2.12 |
cms-algorithm-protection | may be present | may be present | may be present | may be present | 0 or 1 | Clause 5.2.13 | 8
signature-time-stamp | * | shall be present | shall be present | shall be present | ≥1 | Clause 5.3 | l, m, 5
certificate-values | * | * | shall not be present | shall not be present | B-B, B-T: 0 or 1 B-LT, B-LTA: 0 | Clause A.1.1.2 |
complete-certificate-references | * | * | shall not be present | shall not be present | B-B, B-T: 0 or 1 B-LT, B-LTA: 0 | Clause A.1.1.1 | g
revocation-values | * | * | shall not be present | shall not be present | B-B, B-T : 0 or 1 B-LT, B-LTA: 0 | Clause A.1.2.2 |
complete-revocation-references | * | * | shall not be present | shall not be present | B-B, B-T: 0 or 1 B-LT, B-LTA: 0 | Clause A.1.2.1 |
attribute-certificate-references | * | * | shall not be present | shall not be present | B-B, B-T : 0 or 1 B=LT, B=LTA: 0 | Clause A.1.3 | j, n
attribute-revocation-references | * | * | shall not be present | shall not be present | B-B, B-T: 0 or 1 B-LT, B-LTA: 0 | Clause A.1.4 | n
CAdES-C-timestamp | * | * | shall not be present | shall not be present | B-B, B-T: ≥ 0 B-LT, B-LTA: 0 | Clause A.1.5.2 | 5
time-stamped-certs-crls-references | * | * | shall not be present | shall not be present | B-B, B-T: ≥ 0 B-LT, B-LTA: 0 | Clause A.1.5.1 | 5
Service: revocation values in long-term validation | * | * | shall be provided | shall be provided | 1 | | o, p
SPO: SignedData.crls.crl | * | * | conditioned presence | conditioned presence | 0 or 1 | Clause 4.4 | q
SPO: SignedData.crls.other | * | * | conditioned presence | conditioned presence | 0 or 1 | Clause 4.4 | r
archive-time-stamp-v3 | * | * | * | shall be provided | ≥1 | Clause 5.5.3 | s

Additional requirements:

NOTE 2: On SignedData.certificates. A certificate is considered available to the verifier, if reliable information about its location is known and allows automated retrieval of the certificate (for instance through an Authority Info Access Extension or equivalent information present in a TSL).

NOTE 3: On SignedData.certificates. Requirement c) applies specifically but not exclusively to signing certificates that are EU qualified and supported by Trusted Lists as defined in CD 2009/767/EC [i.12] amended by CD 2010/425/EU.

NOTE 4: On SignedData.certificates. In the general case, different verifiers can have different trust parameters and can validate the signing certificate through different chains. Therefore, generators may not know which certificates will be relevant for path building. However, in practice, such certificates can often clearly be identified. In this case, it is advised that generators include them unless they can be automatically retrieved by verifiers.

NOTE 5: On content-time-stamp, signature-time-stamp, CAdES-C-timestamp, and time-stamped-certs-crls-references. Several instances of this attribute can be incorporated to the signature, coming from different TSUs.

NOTE 6: Without the mime-type, the signed data might be interpreted in different ways. This might lead to misunderstandings when the data is shown in one way to the signer, and might be shown after the signature in a different way. Adding the mime-type used to show the document at the moment of signature can help avoiding such situations.

NOTE 7: In case of a detached signature, where the creator of the signature has no knowledge of the content of the signed data, the mime-type application/octet-stream can be used.

NOTE 8: In some cases, like RSA with PKCS#1v5 [i.21], the hash algorithm is already protected by the signature. In other cases, like ECDSA [i.22] or RSA with PSS [i.21], this is not the case. Whenever the hash algorithm is not protected, this might lead to algorithm substitution attacks. Such an attack consists of replacing a strong hash algorithm with a weaker one, which has the same output length. The cms-algorithm-protection signed attribute can be used to protect the hash algorithm if this is not naturally done."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale a)",
        "testo": (
            "Il generatore deve includere il certificato di firma nel campo "
            "SignedData.certificates."
        ),
        "testo_integrale": (
            "a) Requirement for SignedData.certificates. The generator shall include the signing "
            "certificate in the SignedData.certificates field."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale b)",
        "testo": (
            "Per facilitare la costruzione del percorso di certificazione (path building), il "
            "generatore dovrebbe includere nel campo SignedData.certificates tutti i certificati non "
            "disponibili ai verificatori che possono essere usati durante la costruzione del percorso."
        ),
        "testo_integrale": (
            "b) Requirement for SignedData.certificates. In order to facilitate path building, the "
            "generator should include in the SignedData.certificates field all certificates not "
            "available to verifiers that can be used during path building."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale c)",
        "testo": (
            "Quando la firma e' destinata a essere convalidata tramite una Trusted List come "
            "specificato in ETSI TS 119 612 [i.11], il generatore dovrebbe includere tutti i "
            "certificati intermedi che formano una catena fra il certificato di firma e una CA "
            "presente nella Trusted List e che non sono disponibili ai verificatori."
        ),
        "testo_integrale": (
            "c) Requirement for SignedData.certificates. In the case that the signature is meant to "
            "be validated through a Trusted List as specified in ETSI TS 119 612 [i.11] the generator "
            "should include all intermediary certificates forming a chain between the signing "
            "certificate and a CA present in the Trusted List, which are not available to verifiers."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale d)",
        "testo": (
            "Il generatore deve includere l'insieme completo dei certificati usati per convalidare la "
            "firma, comprese le trust anchor quando disponibili in forma di certificato: i "
            "certificati necessari a convalidare il certificato di firma, gli eventuali certificati di "
            "attributo presenti nella firma, le informazioni di revoca (risposta OCSP e CRL) se i "
            "certificati non sono gia' inclusi e il certificato di firma di ogni marca temporale "
            "(certificato TSA) gia' incorporata nella firma."
        ),
        "testo_integrale": (
            "d) Requirement for SignedData.certificates. The generator shall include the full set of "
            "certificates, including the trust anchors when they are available in the form of "
            "certificates that have been used to validate the signature. This set includes "
            "certificates required for validating the signing certificate, for validating any "
            "attribute certificate present in the signature, for validating revocation information "
            "(i.e. OCSP response and CRL) if certificates are not already included, and for validating "
            "any time-stamp token's signing certificate (i.e. a TSA certificate) already incorporated "
            "to the signature."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale e)",
        "testo": (
            "La duplicazione di valori di certificato all'interno della firma dovrebbe essere evitata."
        ),
        "testo_integrale": (
            "e) Requirement for SignedData.certificates. Duplication of certificate values within the "
            "signature should be avoided."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale f)",
        "testo": (
            "L'attributo content-type deve avere valore id-data (v. clausola 4.2)."
        ),
        "testo_integrale": (
            "f) Requirement for content-type. The content-type attribute shall have value id-data "
            "(see clause 4.2)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale g)",
        "testo": (
            "Il campo issuerSerial non dovrebbe essere incluso nella codifica del tipo ESSCertID, "
            "ESSCertIDv2 o OtherCertID."
        ),
        "testo_integrale": (
            "g) Requirement for SPO: ESS signing-certificate, SPO: ESS signing-certificate-v2, and "
            "complete-certificate-references. The issuerSerial field should not be included in the "
            "encoding of the ESSCertID, ESSCertIDv2 or OtherCertID type."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale h)",
        "testo": (
            "L'attributo ESS signing-certificate deve essere usato se si utilizza l'algoritmo di hash "
            "SHA-1."
        ),
        "testo_integrale": (
            "h) Requirement for SPO: ESS signing-certificate. The ESS signing-certificate attribute "
            "shall be used if the SHA-1 hash algorithm is used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale i)",
        "testo": (
            "L'attributo ESS signing-certificate-v2 deve essere usato quando si utilizza un algoritmo "
            "di hash diverso da SHA-1."
        ),
        "testo_integrale": (
            "i) Requirement for SPO: ESS signing-certificate-v2. The ESS signing-certificate-v2 "
            "attribute shall be used when another hash algorithm than SHA-1 is used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale j)",
        "testo": (
            "Il generatore dovrebbe migrare all'uso di ESS signing-certificate-v2, preferendolo a ESS "
            "signing-certificate, in linea con le indicazioni sulla durata limitata dell'uso di SHA-1 "
            "fornite in ETSI TS 119 312 [i.8]."
        ),
        "testo_integrale": (
            "j) Requirement for SPO: ESS signing-certificate and SPO: ESS signing-certificate-v2 and "
            "attribute-certificate-references. The generator should migrate to the use of ESS "
            "signing-certificate-v2 in preference to ESS signing-certificate in line with the guidance "
            "regarding limited lifetime for the use of SHA-1 given in ETSI TS 119 312 [i.8]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale k)",
        "testo": (
            "L'attributo signature-policy-store puo' essere incorporato nella firma CAdES solo se e' "
            "incorporato anche l'attributo signature-policy-identifier e questo contiene in "
            "sigPolicyHash il valore di digest del documento di signature policy; altrimenti "
            "signature-policy-store non deve essere incorporato nella firma CAdES."
        ),
        "testo_integrale": (
            "k) Requirement for signature-policy-store. The signature-policy-store attribute may be "
            "incorporated in the CAdES signature only if the signature-policy-identifier attribute is "
            "also incorporated and it contains in sigPolicyHash the digest value of the signature "
            "policy document, Otherwise the signature-policy-store shall not be incorporated in the "
            "CAdES signature."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale l)",
        "testo": (
            "Il generatore deve usare la codifica DER (clausola 4.7.1) per ogni attributo "
            "signature-time-stamp, preservando la codifica di ogni altro campo di attributo."
        ),
        "testo_integrale": (
            "l) Requirement for signature-time-stamp. The generator shall use DER encoding "
            "(clause 4.7.1) for any signature-time-stamp attribute, whilst preserving the encoding "
            "of any other attribute field."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale m)",
        "testo": (
            "Le marche temporali incapsulate negli attributi signature-time-stamp devono essere "
            "create prima che il certificato di firma sia stato revocato o sia scaduto."
        ),
        "testo_integrale": (
            "m) Requirement for signature-time-stamp. The time-stamp tokens encapsulated within the "
            "signature-time-stamp attributes shall be created before the signing certificate has been "
            "revoked or has expired."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale n)",
        "testo": (
            "Gli attributi attribute-certificate-references e attribute-revocation-references "
            "possono essere usati quando almeno un attributo certificato del firmatario "
            "(certifiedAttributesV2 come definito in clausola 5.2.6.1) o un'asserzione firmata "
            "(signedAssertions come definito in clausola 5.2.6.1) e' presente fra gli attributi del "
            "firmatario nella firma digitale; altrimenti non devono essere usati."
        ),
        "testo_integrale": (
            "n) Requirements for attribute-certificate-references and attribute-revocation-"
            "references. The attribute-certificate-references and attribute-revocation-"
            "references attributes may be used when a at least a certified signer attribute "
            "(certifiedAttributesV2 as defined in clause 5.2.6.1) or a signed assertion "
            "(signedAssertions as defined in clause 5.2.6.1) is present within the signer attributes "
            "in the digital signature. Otherwise, attribute-certificate-references and "
            "attribute-revocation-references attributes shall not be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale o)",
        "testo": (
            "Il generatore deve includere l'insieme completo dei dati di revoca (CRL o risposte "
            "OCSP) usati nella convalida della firma: tutte le informazioni sullo stato dei "
            "certificati necessarie a convalidare il certificato di firma, gli eventuali certificati "
            "di attributo o asserzioni firmate presenti nella firma, le informazioni di revoca "
            "(risposta OCSP e CRL) se non gia' incluse e il certificato di firma di ogni marca "
            "temporale (certificato TSA) gia' incorporata nella firma."
        ),
        "testo_integrale": (
            "o) Requirement for Service: revocation values in long-term validation. The generator "
            "shall include the full set of revocation data (CRL or OCSP responses) that have been "
            "used in the validation of the signature. This set includes all certificate status "
            "information required for validating the signing certificate, for validating any "
            "attribute certificate or signed assertion present in the signature, for validating "
            "revocation information (i.e. OCSP response and CRL) if they are not already included and "
            "for validating any time-stamp token's signing certificate (i.e. a TSA certificate) "
            "already incorporated to the signature."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale p)",
        "testo": (
            "La duplicazione di valori di revoca all'interno della firma dovrebbe essere evitata."
        ),
        "testo_integrale": (
            "p) Requirement for Service: revocation values in long-term validation. Duplication of "
            "revocation values within the signature should be avoided."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale q)",
        "testo": (
            "Quando l'insieme completo dei dati di revoca contiene CRL [6], i valori delle CRL "
            "devono essere inclusi in SignedData.crls.crl."
        ),
        "testo_integrale": (
            "q) Requirement for SPO: SignedData.crls.crl. When the full set of revocation data "
            "contains CRLs [6], then the CRL values shall be included within SignedData.crls.crl."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale r)",
        "testo": (
            "Quando l'insieme completo dei dati di revoca contiene risposte OCSP [14], i valori "
            "delle risposte OCSP devono essere inclusi in SignedData.crls.other come specificato in "
            "IETF RFC 5940 [13]."
        ),
        "testo_integrale": (
            "r) Requirement for SPO: SignedData.crls.other. When the full set of revocation data "
            "contains OCSP responses [14], then the OCSP response values shall be included within "
            "SignedData.crls.other as specified in IETF RFC 5940 [13]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale s)",
        "testo": (
            "Prima di generare e incorporare un attributo archive-time-stamp-v3 deve essere incluso "
            "tutto il materiale di validazione necessario a verificare la firma che non sia gia' "
            "nella firma, compreso il materiale di validazione usato per convalidare la marca "
            "temporale di archivio precedente."
        ),
        "testo_integrale": (
            "s) Requirement for archive-time-stamp-v3. Before generating and incorporating an "
            "archive-time-stamp-v3 attribute, all the validation material required for verifying the "
            "signature, which are not already in the signature, shall be included. This validation "
            "material includes validation material used to validate previous archive time stamp."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3, requisito addizionale t)",
        "testo": (
            "Almeno uno fra gli attributi content-hints o mime-type dovrebbe essere presente e deve "
            "descrivere il tipo di dati firmati."
        ),
        "testo_integrale": (
            "t) Requirement for Service: identifying the signed data type. At least one of the "
            "attributes, content-hints or mime-type should be present and shall describe the signed "
            "data type."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.4 (Legacy CAdES baseline signatures)",
        "testo": (
            "Quando a firme CAdES baseline legacy vengono incorporati nuovi attributi non firmati, "
            "questi attributi devono essere conformi al presente documento."
        ),
        "testo_integrale": (
            "6.4 Legacy CAdES baseline signatures: When new unsigned attributes are incorporated to "
            "legacy CAdES baseline signatures, these attributes shall comply with the present "
            "document."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Si applica quando vengono incorporati nuovi attributi non firmati in firme CAdES "
            "baseline legacy."
        ),
        "soggetti": [{"categoria": "Utente/titolare", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 6.1 (Signature levels)",
        "testo": (
            "La clausola 6 definisce quattro livelli di firma CAdES baseline, volti a facilitare "
            "l'interoperabilita' e a coprire il ciclo di vita della firma elettronica: B-B "
            "(incorporazione di attributi firmati e di alcuni attributi non firmati quando la firma "
            "viene effettivamente generata), B-T (generazione e inclusione, per una firma esistente, "
            "di un token fidato che provi che la firma esisteva a una certa data e ora), B-LT "
            "(incorporazione nel documento di firma di tutto il materiale necessario a convalidare la "
            "firma, per la disponibilita' a lungo termine) e B-LTA (incorporazione di marche "
            "temporali che consentono la convalida della firma molto tempo dopo la sua generazione, "
            "per la disponibilita' e l'integrita' a lungo termine del materiale di convalida)."
        ),
        "testo_integrale": (
            """6.1 Signature levels: Clause 6 defines four levels of CAdES baseline signatures, intended to facilitate interoperability and to encompass the life cycle of electronic signature, namely:

a) B-B level provides requirements for the incorporation of signed and some unsigned attributes when the signature is actually generated.

b) B-T level provides requirement for the generation and inclusion, for an existing signature, of a trusted token proving that the signature itself actually existed at a certain date and time.

c) B-LT level provides requirements for the incorporation of all the material required for validating the signature in the signature document. This level aims to tackle the long term availability of the validation material.

d) B-LTA level provides requirements for the incorporation of time-stamp tokens that allow validation of the signature long time after its generation. This level aims to tackle the long term availability and integrity of the validation material.

NOTE 1: ETSI TR 119 100 [i.4] provides a description on the life-cycle of a signature and the rationales on which level is suitable in which situation.

NOTE 2: The levels c) to d) are appropriate where the technical validity of signature needs to be preserved for a period of time after signature creation where certificate expiration, revocation and/or algorithm obsolescence is of concern. The specific level applicable depends on the context and use case.

NOTE 3: B-LTA level targets long term availability and integrity of the validation material of digital signatures. The B-LTA level can help to validate the signature beyond many events that limit its validity (for instance, the weakness of used cryptographic algorithms, or expiration of validation data). The use of B-LTA level is considered an appropriate preservation and transmission technique for signed data.

NOTE 4: Conformance to B-LT level, when combined with appropriate additional preservation techniques tackling the long term availability and integrity of the validation material is sufficient to allow validation of the signature long time after its generation. The assessment of the effectiveness of preservation techniques for signed data other than implementing the B-LTA level are out of the scope of the present document. The reader is advised to consider legal instruments in force and/or other standards (for example ETSI TS 119 511 [i.20] or IETF RFC 4998 [i.15]) that can indicate other preservation techniques. Annex B defines what needs to be taken into account when using other techniques for long term availability and integrity of validation data and including a new unsigned attribute derived from these techniques into the signature."""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 6.2.2 (Notation for requirements)",
        "testo": (
            "Clausola che definisce la notazione usata per i requisiti dei livelli di firma CAdES: "
            "il significato delle 8 colonne della Tabella 1 (attributo/campo/servizio, presenza nei "
            "quattro livelli B-B, B-T, B-LT e B-LTA, cardinalita', riferimenti, note e requisiti "
            "aggiuntivi), i valori ammessi nelle colonne di presenza (\"shall be present\", \"shall "
            "not be present\", \"may be present\", \"shall be provided\", \"conditioned presence\", "
            "\"*\"), i valori di cardinalita' (0, 1, 0 o 1, maggiore o uguale a 0, maggiore o uguale "
            "a 1) e un esempio di lettura della tabella."
        ),
        "testo_integrale": (
            """6.2.2 Notation for requirements: The present clause describes the notation used for defining the requirements of the different CAdES signature levels.

The requirements on the attributes and certain signature fields for each CAdES signature level are expressed in table 1. A row in the table either specifies requirements for an attribute, a signature field or a service.

A service can be provided by different attributes or other mechanisms (service provision options hereinafter). In this case, the specification of the requirements for a service is provided by two or more rows. The first row contains the requirements of the service. The requirements for the attributes and/or mechanisms used to provide the service are stated in the following rows.

Table 1 contains 8 columns. Below follows a detailed explanation of their meanings and contents:

1) Column "Attribute/Field/Service":
a) In the case where the cell identifies a Service, the cell content starts with the keyword "Service" followed by the name of the service.
b) In the case where the attribute or signature field provides a service, this cell contains "SPO" (for Service Provision Option), followed by the name of the attribute or signature field.
c) Otherwise, this cell contains the name of the attribute or signature field.

2) Column "Presence in B-B-Level": This cell contains the specification of the presence of the attribute or signature field, or the provision of a service, for CAdES-B-B signatures.

3) Column "Presence in B-T level": This cell contains the specification of the presence of the attribute or signature field, or the provision of a service, for CAdES-B-T signatures.

4) Column "Presence in B-LT level": This cell contains the specification of the presence of the attribute or signature field, or the provision of a service, for CAdES-B-LT signatures.

5) Column "Presence in B-LTA level": This cell contains the specification of the presence of the attribute or signature field, or the provision of a service, for CAdES-B-LTA signatures.

Below follows the values that can appear in columns "Presence in B-B", "Presence in B-T", "Presence in B-LT", and "Presence in B-LTA":

- "shall be present": means that the attribute or signature field shall be present, and shall be as specified in the document referenced in column "References", further profiled with the additional requirements referenced in column "Requirements", and with the cardinality indicated in column "Cardinality".

- "shall not be present": means that the attribute or signature field shall not be present. In these cases the content of the "Cardinality" column can indicate, the cardinality for each level if this value is not the same for all the levels. See example at the end of the present clause.

- "may be present": means that the attribute or signature field may be present, and shall be as specified in the document referenced in column "References", further profiled with the additional requirements referenced in column "Requirements", and with the cardinality indicated in column "Cardinality".

- "shall be provided": means that the service identified in the first column of the row shall be provided as further specified in the SPO-related rows. This value only appears in rows that contain requirements for services. It does not appear in rows that contain requirements for attributes or signature fields.

- "conditioned presence": means that the presence of the item identified in the first column is conditioned as per the requirement(s) specified in column "Requirements" and requirements referenced by column "References" with the cardinality indicated in column "Cardinality".

- "*": means that the attribute or the signature field (service) identified in the first column should not be present (provided) in the corresponding level. Upper signature levels may specify other requirements.

NOTE: Adding an unsigned attribute that is marked with a "*" to a signature can lead to cases where a higher level cannot be achieved, except by removing the corresponding unsigned attribute.

6) Column "Cardinality": This cell indicates the cardinality of the attribute or the signature field. If the cardinality is the same for all the levels, only the values listed below appear. Otherwise the content specifies the cardinality for each level. See the example at the end of the present clause showing this situation. Below follow the values indicating the cardinality:

- 0: The signature shall not incorporate any instance of the attribute or signature field.

- 1: The signature shall incorporate exactly one instance of the attribute or signature field.

- 0 or 1: The signature shall incorporate zero or one instance of the attribute or signature field.

- ≥ 0: The signature shall incorporate zero or more instances of the attribute or signature field.
- ≥ 1: The signature shall incorporate one or more instances of the attribute or signature field.

7) Column "References": This cell contains either the number of the clause specifying the attribute in the present document, or a reference to the document and clause that specifies the signature field.

8) Column "Additional notes and requirements": This cell contains numbers referencing notes and/or letters referencing additional requirements on the attribute or the signature field. Both notes and additional requirements are listed below table 1.

EXAMPLE: In table 1, the row corresponding to complete-certificate-references attribute has a value "*" in the cells in columns "Presence in B-B level" and "Presence in B-T level", and "shall not be present" in cells in columns "Presence in B-LT level" and "Presence in B-LTA level". The cell in column "Cardinality" indicates the cardinality for each level as follows: "B-B, B-T: 0 or 1" indicates that CAdES-B-B and CAdES-B-T signatures can incorporate one instance of complete-certificate-references attribute; "B-LT, B-LTA: 0" indicates that CAdES-B-LT and CAdES-B-LTA do not incorporate the complete-certificate-references attribute."""
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 6.1 (Signature levels)",
    "clausola 6.2.1 (Algorithm requirements)",
    "clausola 6.2.2 (Notation for requirements)",
    "clausola 6.3 (Requirements on components and services)",
    "clausola 6.3, requisito addizionale a)",
    "clausola 6.3, requisito addizionale b)",
    "clausola 6.3, requisito addizionale c)",
    "clausola 6.3, requisito addizionale d)",
    "clausola 6.3, requisito addizionale e)",
    "clausola 6.3, requisito addizionale f)",
    "clausola 6.3, requisito addizionale g)",
    "clausola 6.3, requisito addizionale h)",
    "clausola 6.3, requisito addizionale i)",
    "clausola 6.3, requisito addizionale j)",
    "clausola 6.3, requisito addizionale k)",
    "clausola 6.3, requisito addizionale l)",
    "clausola 6.3, requisito addizionale m)",
    "clausola 6.3, requisito addizionale n)",
    "clausola 6.3, requisito addizionale o)",
    "clausola 6.3, requisito addizionale p)",
    "clausola 6.3, requisito addizionale q)",
    "clausola 6.3, requisito addizionale r)",
    "clausola 6.3, requisito addizionale s)",
    "clausola 6.3, requisito addizionale t)",
    "clausola 6.4 (Legacy CAdES baseline signatures)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Relazioni interne alla clausola 6.3 (rinvii della Tabella 1 ai requisiti
# addizionali, colonna "Additional requirements and notes"), una per lettera.
# Nessuna relazione verso altri capitoli di questa fonte o verso altre fonti:
# vedi docstring di modulo e ADR-0009/ADR-0012.
RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale a)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale b)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale c)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale d)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale e)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale f)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale g)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale h)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale i)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale j)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale k)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale l)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale m)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale n)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale o)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale p)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale q)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale r)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale s)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 6.3, requisito addizionale t)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
