"""ETSI EN 319 132-1 V1.3.1 (2024-07) - Electronic Signatures and Trust
Infrastructures (ESI); XAdES digital signatures; Part 1: Building blocks and
XAdES baseline signatures. Blocco B (famiglia AdES del lotto 2). Capitolo 9
dello split: Annex D (normative), "Deprecated qualifying properties" (le
qualifying property di XAdES, definite in ETSI TS 101 903 V1.4.2, che non
devono piu' comparire in una firma XAdES, ciascuna con la property V2 che la
sostituisce). Questo modulo e' puro dato: non importa nulla, non legge file e
NON tocca app/seed.py - la numerazione degli id e' risolta per riferimento
dalla sessione principale tramite app/seed_data/lib.py, e le relazioni verso
altri capitoli di questa fonte o verso altre fonti le costruisce sempre la
sessione principale (fase 6, ADR-0009).

Provenienza del testo
---------------------
- Testo ufficiale: ETSI EN 319 132-1 V1.3.1 (2024-07), "Electronic Signatures
  and Trust Infrastructures (ESI); XAdES digital signatures; Part 1: Building
  blocks and XAdES baseline signatures".
- File di capitolo: app/.source_cache/etsi_319_132/cap09.txt (55 righe),
  porzione dello split deterministico descritto in
  app/.source_cache/etsi_319_132/manifest.json (capitolo "cap09", titolo
  "Annex D (normative):"), ritagliata dal testo ufficiale completo in
  app/.source_cache/etsi_319_132/raw.txt (il PDF grezzo dello stesso
  documento e' raw.pdf, raw_body.txt ne e' la copia senza intestazioni
  ripetute).
- Da app/.source_cache/etsi_319_132/provenance.json: url ufficiale
  https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf,
  versione "01.03.01_60", data_fetch 2026-09-29T12:56:34Z, sha256_raw_pdf
  83fc87ee09de90274131a1f60cb73edb742cebc7cd8961342586ed06133664c5, formato
  "PDF ETSI deliver (pdftotext -layout)". La porzione di capitolo riproduce
  raw.txt righe 4646-4700: comincia con il titolo "Annex D (normative):" e
  termina con la NOTE 2; il capitolo successivo dello split (cap10) apre
  l'Annex E (informative, Change history).
- NOTA DI PERIMETRO: la traccia di dispatch descriveva questo capitolo come
  "definizioni ASN.1, attributi e OID XAdES, blocchi ASN.1 verbatim". Il file
  assegnato (cap09.txt) NON e' quello: contiene l'Annex D vero e proprio
  dell'EN 319 132-1, che e' un annesso normativo di elenco (deprecazione e
  redirezione), senza blocchi ASN.1 e senza OID. Le definizioni ASN.1 e gli
  attributi con OID stanno altrove nello stesso documento: l'Annex A
  (qualifying property per i dati di validazione, con i tipi ASN.1) sta nel
  capitolo 8 dello split (cap08.txt), le definizioni ASN.1 complete nella
  loro forma X.680 negli annessi successivi. Questo modulo copre percio',
  fedelmente, cio' che cap09.txt contiene: nessun contenuto e' stato
  spostato, omesso o inventato per far coincidere la descrizione del
  dispatch con il testo.

Granularita' (ADR-0007, granularita' fine)
------------------------------------------
8 item di indice = 8 righe:

- 1 riga per la premessa dell'annesso (le due frasi che enunciano la
  deprecazione e il divieto generale "XAdES signatures shall not include any
  of these qualifying properties", con le due NOTE di annesso che la
  seguono);
- 1 riga per ciascuno dei 7 punti numerati 1)-7), ognuno dei quali identifica
  una singola qualifying property deprecata, il suo namespace, la fonte che
  la definisce e la property V2 che la sostituisce (con il rinvio alla
  clausola che la specifica).

Perche' il singolo punto numerato e' un item di indice e non dettaglio della
premessa: i punti sono le voci stesse dell'elenco che l'annesso intitola, e
ciascuno porta una redirezione propria e nominata (SigningCertificate ->
SigningCertificateV2, CompleteCertificateRefs -> CompleteCertificateRefsV2,
SigAndRefsTimeStamp -> SigAndRefsTimeStampV2, ecc.) con un bersaglio
differente; la premessa enuncia invece la regola generale che vale per
l'elenco intero e non ha numerazione propria. E' lo stesso schema di ETSI EN
319 122-1 cap05 (Annex A.2.1 "Usage of deprecated attributes" = regola
generale, riga a se', e A.2.2-A.2.6 = singolo attributo deprecato, una riga
ciascuno) e, per le lettere dei requisiti addizionali, del precedente fissato
in ETSI EN 319 122-1 clausola 6.3 (cap04 di quella fonte, venti requisiti
a)-t)). Alternativa scartata: un'unica riga per l'intero Annex D - avrebbe
reso non rintracciabili singolarmente sette prescrizioni di redirezione
distinte, con bersagli diversi (clausole 5.2.2, 5.2.5, 5.2.6, A.1.1, A.1.3).

Le intestazioni "Annex D (normative):" e "Deprecated qualifying properties"
non generano un item a se': sono titolazione dell'annesso, assorbita nella
riga della premessa (che le riporta in testa al `testo_integrale`), come da
criterio gia' applicato alle intestazioni di raggruppamento delle altre fonti
ETSI censite.

Vocabolario dei `riferimento`: forma italiana convenzionale per un annesso in
lingua inglese (procedura di import, passo 2-bis). La premessa usa il titolo
dell'annesso ("Annex D (Deprecated qualifying properties)"); i punti usano
"Annex D, punto N)" con il nome della property deprecata fra parentesi
("Annex D, punto 1) (The SigningCertificate qualifying property)"), coerente
con la forma gia' in uso per le voci numerate degli allegati ("allegato IV,
sezione IV.3, punto 5") e con la forma "Annex A.1.1.1 (titolo)" usata dai
moduli degli annessi di questo stesso standard. Il testo integrale resta in
inglese verbatim, i riferimenti-bersaglio citati dai punti restano nella
forma del testo ("clause 5.2.2", "clause A.1.1").

Classificazione Obbligo/Principio, riga per riga
------------------------------------------------
Tutte le 8 righe sono Obblighi "tecnico/sicurezza"; nessun Principio.

- Premessa dell'annesso -> Obbligo "tecnico/sicurezza": non e' una
  descrizione, e' un divieto ("XAdES signatures shall not include any of
  these qualifying properties") che vincola il contenuto della firma XAdES.
  Le NOTE 1 e 2 sono assorbite perche' delimitano la portata del divieto:
  NOTE 1 chiarisce che la ArchiveTimeStamp del namespace v1.3.2 era gia'
  deprecata in ETSI TS 101 903 V1.4.2 e che quella ammessa dal presente
  documento e' la ArchiveTimeStamp del namespace v1.4.1; NOTE 2 rinvia alla
  clausola 6.4 per i requisiti delle firme XAdES baseline legacy. Entrambe
  annotano l'annesso nel suo complesso (non un singolo punto), quindi vivono
  in questa riga e non in una riga 1)-7).
- Punti 1)-7) -> 7 Obblighi "tecnico/sicurezza". Ciascuno ha la forma "the X
  qualifying property ... is deprecated. Instead the XV2 qualifying property
  ... shall be used": un divieto di uso del vecchio elemento con redirezione
  obbligatoria al nuovo. Stessa classificazione gia' adottata per gli
  attributi deprecati di ETSI EN 319 122-1 Annex A.2 (cap05 di quella fonte).

Nessun `soggetti` e nessun `oggetti_giuridici` sono valorizzati in questo
capitolo: il testo nomina solo tipi di qualifying property e le firme XAdES
in forma impersonale ("XAdES signatures shall not include ..."), senza
nominare alcuna delle quattro categorie di soggetto censite ("QTSP/gestore",
"Utente/titolare", "Terza parte", "Terzi affidanti/pubblico") ne' uno degli
oggetti giuridici della tassonomia eIDAS. Stesso criterio di ETSI EN 319
122-1 Annex A.2 (nessun soggetto sulle righe degli attributi deprecati).
Nessun `severita`, `sanzioni` o `condizione_applicabilita`: lo standard non
prevede sanzioni ne' subordina la deprecazione a un fatto esterno.

Completezza verbatim (ADR-0010)
-------------------------------
`testo_integrale` riporta il testo ufficiale per intero, senza elisioni,
riassunti o tagli. Convenzioni di ricostruzione applicate:

- la premessa e' ricucita dallo spezzamento di riga della conversione PDF
  ("... are deprecated. XAdES | signatures shall not include ..." -> unico
  periodo);
- ogni punto 1)-7) e' ricucito dalle tre righe in cui il PDF lo dispone
  (riquadro con rientro a scalare) in un unico periodo, mantenendo la
  numerazione originale "1)" ... "7)" e la spaziatura interna del testo;
- le NOTE sono ricucite allo stesso modo, mantenendo l'etichetta "NOTE 1:" /
  "NOTE 2:";
- paratesto escluso: piede/testatina di pagina "ETSI" e "74 ETSI EN 319 132-1
  V1.3.1 (2024-07)" / "75 ETSI EN 319 132-1 V1.3.1 (2024-07)" (righe 4643,
  4697-4698 di raw.txt), righe vuote di impaginazione.

Peculiarita' del testo ufficiale riportate come stanno (nessuna correzione
silenziosa, perche' `testo_integrale` e' verbatim):
- punto 4): l'etichetta bibliografica sta dopo il punto fermo ("... (V1.4.2).
  [i.2] Instead the ..."), a differenza degli altri punti;
- punto 6): il periodo si chiude con un "And" sospeso ("... shall be used.
  And"), evidente refuso del documento, che continua nel punto 7);
- punti 5), 6) e 7): tutti e tre rinviano a "clause A.1.3 of the present
  document"; nell'Annex A di questo standard la sigla A.1.3 e' "The
  AttributeCertificateRefsV2 qualifying property", mentre SigAndRefsTimeStampV2
  e RefsOnlyTimeStampV2 sono definite in A.1.5.1 e A.1.5.2. Il riferimento e'
  riportato come stampato; la discordanza e' annotata qui e, per la fase 6,
  qui sotto.
- punto 7): il nome della property e' stampato "RefsOnlyTimeStamp V2" (con lo
  spazio), mentre la property corrente e' "RefsOnlyTimeStampV2".
- Nome file XML Schema, namespace e URI sono riportati carattere per
  carattere come nel testo (http://uri.etsi.org/01903/v1.3.2# e
  http://uri.etsi.org/01903/v1.4.1#).
Nessun blocco ASN.1 in questo capitolo (non ce n'e' alcuno nell'Annex D): il
punto della traccia di dispatch su blocchi ASN.1 verbatim non trova
applicazione nel file assegnato.

Rinvii demandati alla fase 6 (nessuna relazione creata qui)
-----------------------------------------------------------
`RELAZIONI` e' vuoto: tutti i rinvii di questo annesso hanno per bersaglio
un'unita' che non e' una riga di questo modulo. Criterio applicato (identico
a ETSI EN 319 122-1 cap05): dentro il modulo si crea un arco solo quando la
citazione porta un puntatore verificabile a un'altra riga *dichiarata qui*;
il "listed below" della premessa non porta numerazione di punto e non e'
stato trasformato in sette archi.

- Verso clausole di questa stessa Fonte, capitoli 1-7 dello split:
  punto 1) -> clausola 5.2.2 (The SigningCertificateV2 qualifying property,
  cap04); punto 2) -> clausola 5.2.5 (The SignatureProductionPlaceV2
  qualifying property, cap04); punto 3) -> clausola 5.2.6 (The SignerRoleV2
  qualifying property, cap04); NOTE 1 -> clausola 5.5.2 (The ArchiveTimeStamp
  qualifying property definita nel namespace v1.4.1, cap05); NOTE 2 ->
  clausola 6.4 (Legacy XAdES baseline signatures, cap07).
- Verso l'Annex A (normativo) di questa stessa Fonte, capitolo 8 dello split:
  punto 4) -> Annex A.1.1 (The CompleteCertificateRefsV2 qualifying
  property); punto 5) -> Annex A.1.3 (The AttributeCertificateRefsV2
  qualifying property); punti 6) e 7) -> Annex A.1.3 come stampato dal
  testo, mentre le sottoclauste pertinenti dell'Annex A sono A.1.5.1 (The
  SigAndRefsTimeStampV2 qualifying property) e A.1.5.2 (The
  RefsOnlyTimeStampV2 qualifying property). Da decidere in fase 6 se ancorare
  l'arco al riferimento stampato (A.1.3) o alla sottoclausta che definisce
  davvero la property; le partizioni "Annex A" / "Annex A, clausola A.1.5"
  / "Annex A, clausola A.1.3" esistono comunque (ADR-0012) e la scelta va
  documentata, non fatta in silenzio qui.
- Verso fonti esterne (collegamento cross-fonte, ADR-0009): ETSI TS 101 903
  (V1.4.2) [i.2], citata in tutti e sette i punti e nella premessa come fonte
  che definisce le property deprecate (fonte non censita nel grafo: nessun
  arco possibile, la citazione resta tracciata nel `testo_integrale`).

Esclusioni
----------
Fuori perimetro, nessun nodo ne' item di indice: il front matter e il
Contents dello standard (dove Annex D compare come voce di indice alle righe
215-216 di raw.txt), la Foreword, la History e l'elenco dei riferimenti
bibliografici (clausola 2 e References finali), l'Annex E (informative,
Change history, capitolo 10 dello split) e tutto l'Annex A (capitolo 8 dello
split), incluse la sua A.2 "Deprecated qualifying properties" e A.2.1/A.2.2
(RenewedDigests): pur trattando materia affine, sono sezioni dell'Annex A, non
di questo annesso, e sono coperte dal modulo di quel capitolo.

Conteggio finale: 8 item di indice, 8 righe: 8 obblighi + 0 principi, 0
relazioni interne.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "Annex D (Deprecated qualifying properties)",
        "testo": (
            "Le qualifying property di XAdES elencate nell'Annex D, definite in ETSI TS 101 903 "
            "(V1.4.2) [i.2], sono deprecate: una firma XAdES non deve includerne nessuna. La NOTE 1 "
            "chiarisce che la ArchiveTimeStamp del namespace http://uri.etsi.org/01903/v1.3.2# era "
            "gia' deprecata in ETSI TS 101 903 (V1.4.2) [i.2] e che la ArchiveTimeStamp ammessa dal "
            "presente documento e' quella del namespace http://uri.etsi.org/01903/v1.4.1#; la NOTE 2 "
            "rinvia alla clausola 6.4 per i requisiti delle firme XAdES baseline legacy."
        ),
        "testo_integrale": (
            """Annex D (normative): Deprecated qualifying properties

The qualifying properties, specified in ETSI TS 101 903 (V1.4.2) [i.2] and listed below, are deprecated. XAdES signatures shall not include any of these qualifying properties.

NOTE 1: The ArchiveTimeStamp qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.3.2# had already been deprecated in ETSI TS 101 903 (V1.4.2) [i.2] by the ArchiveTimeStamp qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.4.1#, which is the one defined and allowed by the present document.

NOTE 2: For legacy XAdES baseline signatures requirements see clause 6.4."""
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, punto 1) (The SigningCertificate qualifying property)",
        "testo": (
            "La qualifying property SigningCertificate, definita nel namespace "
            "http://uri.etsi.org/01903/v1.3.2# e specificata in ETSI TS 101 903 (V1.4.2) [i.2], e' "
            "deprecata: al suo posto una firma XAdES deve usare la SigningCertificateV2, definita nello "
            "stesso namespace e specificata nella clausola 5.2.2 del presente documento."
        ),
        "testo_integrale": (
            "1) The SigningCertificate qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#, and specified in ETSI TS 101 903 (V1.4.2) [i.2]. Instead the SigningCertificateV2 qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#, specified in clause 5.2.2 of the present document, shall be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, punto 2) (The SignatureProductionPlace qualifying property)",
        "testo": (
            "La qualifying property SignatureProductionPlace, definita nel namespace "
            "http://uri.etsi.org/01903/v1.3.2# e specificata in ETSI TS 101 903 (V1.4.2) [i.2], e' "
            "deprecata: al suo posto una firma XAdES deve usare la SignatureProductionPlaceV2, "
            "definita nello stesso namespace e specificata nella clausola 5.2.5 del presente documento."
        ),
        "testo_integrale": (
            "2) The SignatureProductionPlace qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#, and specified in ETSI TS 101 903 (V1.4.2) [i.2]. Instead the SignatureProductionPlaceV2 qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#, specified in clause 5.2.5 of the present document, shall be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, punto 3) (The SignerRole qualifying property)",
        "testo": (
            "La qualifying property SignerRole, definita nel namespace "
            "http://uri.etsi.org/01903/v1.3.2# e specificata in ETSI TS 101 903 (V1.4.2) [i.2], e' "
            "deprecata: al suo posto una firma XAdES deve usare la SignerRoleV2, definita nello stesso "
            "namespace e specificata nella clausola 5.2.6 del presente documento."
        ),
        "testo_integrale": (
            "3) The SignerRole qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#, and specified in ETSI TS 101 903 (V1.4.2) [i.2]. Instead the SignerRoleV2 qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#, specified in clause 5.2.6 of the present document, shall be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, punto 4) (The CompleteCertificateRefs qualifying property)",
        "testo": (
            "La qualifying property CompleteCertificateRefs, definita nel namespace "
            "http://uri.etsi.org/01903/v1.3.2# e specificata in ETSI TS 101 903 (V1.4.2) [i.2], e' "
            "deprecata: al suo posto una firma XAdES deve usare la CompleteCertificateRefsV2, definita "
            "nel namespace http://uri.etsi.org/01903/v1.4.1# e specificata nella clausola A.1.1 del "
            "presente documento."
        ),
        "testo_integrale": (
            "4) The CompleteCertificateRefs qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#, and specified in ETSI TS 101 903 (V1.4.2). [i.2] Instead the CompleteCertificateRefsV2 qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.4.1#, specified in clause A.1.1 of the present document, shall be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, punto 5) (The AttributeCertificateRefs qualifying property)",
        "testo": (
            "La qualifying property AttributeCertificateRefs, definita nel namespace "
            "http://uri.etsi.org/01903/v1.3.2# e specificata in ETSI TS 101 903 (V1.4.2) [i.2], e' "
            "deprecata: al suo posto una firma XAdES deve usare la AttributeCertificateRefsV2, "
            "definita nel namespace http://uri.etsi.org/01903/v1.4.1# e specificata nella clausola "
            "A.1.3 del presente documento."
        ),
        "testo_integrale": (
            "5) The AttributeCertificateRefs qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#, and specified in ETSI TS 101 903 (V1.4.2) [i.2]. Instead the AttributeCertificateRefsV2 qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.4.1#, specified in clause A.1.3 of the present document, shall be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, punto 6) (The SigAndRefsTimeStamp qualifying property)",
        "testo": (
            "La qualifying property SigAndRefsTimeStamp, definita nel namespace "
            "http://uri.etsi.org/01903/v1.3.2# e specificata in ETSI TS 101 903 (V1.4.2) [i.2], e' "
            "deprecata: al suo posto una firma XAdES deve usare la SigAndRefsTimeStampV2, definita nel "
            "namespace http://uri.etsi.org/01903/v1.4.1# e specificata nella clausola A.1.3 del "
            "presente documento (riferimento cosi' stampato nel testo ufficiale; la sottoclausta "
            "dell'Annex A che definisce la property e' A.1.5.1). Il periodo termina con un \"And\" "
            "sospeso nel testo ufficiale."
        ),
        "testo_integrale": (
            "6) The SigAndRefsTimeStamp qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#, and specified in ETSI TS 101 903 (V1.4.2) [i.2]. Instead the SigAndRefsTimeStampV2 qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.4.1#, specified in clause A.1.3 of the present document, shall be used. And"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D, punto 7) (The RefsOnlyTimeStamp qualifying property)",
        "testo": (
            "La qualifying property RefsOnlyTimeStamp, definita nel namespace "
            "http://uri.etsi.org/01903/v1.3.2# e specificata in ETSI TS 101 903 (V1.4.2) [i.2], e' "
            "deprecata: al suo posto una firma XAdES deve usare la RefsOnlyTimeStamp V2 (nel testo "
            "ufficiale il nome e' stampato con uno spazio), definita nel namespace "
            "http://uri.etsi.org/01903/v1.4.1# e specificata nella clausola A.1.3 del presente "
            "documento (riferimento cosi' stampato nel testo ufficiale; la sottoclausta dell'Annex A "
            "che definisce la property e' A.1.5.2)."
        ),
        "testo_integrale": (
            "7) The RefsOnlyTimeStamp qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.3.2#, and specified in ETSI TS 101 903 (V1.4.2) [i.2]. Instead the RefsOnlyTimeStamp V2 qualifying property defined in the namespace whose URI is http://uri.etsi.org/01903/v1.4.1#, specified in clause A.1.3 of the present document, shall be used."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
    },
]

RIGHE_PRINCIPI: list[dict] = []

INDICE_ARTICOLI_LOCALE: list[str] = [
    "Annex D (Deprecated qualifying properties)",
    "Annex D, punto 1) (The SigningCertificate qualifying property)",
    "Annex D, punto 2) (The SignatureProductionPlace qualifying property)",
    "Annex D, punto 3) (The SignerRole qualifying property)",
    "Annex D, punto 4) (The CompleteCertificateRefs qualifying property)",
    "Annex D, punto 5) (The AttributeCertificateRefs qualifying property)",
    "Annex D, punto 6) (The SigAndRefsTimeStamp qualifying property)",
    "Annex D, punto 7) (The RefsOnlyTimeStamp qualifying property)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Nessuna relazione interna: tutti i rinvii dell'Annex D (clausole 5.2.2,
# 5.2.5, 5.2.6, 5.5.2, 6.4 e Annex A.1.1/A.1.3) hanno per bersaglio righe
# dichiarate in altri capitoli di questa fonte; il "listed below" della
# premessa non porta numerazione di punto. Li costruisce la sessione
# principale in fase 6 (ADR-0009/ADR-0012) - vedi docstring.
RELAZIONI: list[dict] = []
